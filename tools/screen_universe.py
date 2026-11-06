#!/usr/bin/env python3
"""Preliminary SEC annual fundamentals screen, never an investment rating.
Preserves fact dates and accessions. Missing spending stays missing.
Scope: standard US GAAP USD frames, not every global listed company.
"""
import argparse
import csv
import io
import json
import math
import os
import sys
import tempfile
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

METHOD = "2.0"
REVENUE_TAGS = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"]
TAGS = {
    "revenue": REVENUE_TAGS, "revenue_base": REVENUE_TAGS,
    "net_income": ["NetIncomeLoss"], "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"], "assets": ["Assets"],
    "liabilities": ["Liabilities"], "equity": ["StockholdersEquity"],
}
FIELDS = ["cik", "name", "revenue", "rev_cagr_2y", "net_margin", "fcf_margin",
          "liab_to_assets", "roe", "score", "method_version", "period_start",
          "period_end", "flags", "evidence_json"]


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def fact_date(fact, key):
    try:
        return date.fromisoformat(fact[key])
    except (KeyError, TypeError, ValueError):
        return None


def aligned(left, right, duration=True):
    keys = ("start", "end") if duration else ("end",)
    return all(fact_date(left, k) is not None and fact_date(right, k) is not None
               and abs((fact_date(left, k) - fact_date(right, k)).days) <= 7 for k in keys)


def preliminary_score(row):
    """Existing coarse ranking weights, not valuation or a sector neutral rating."""
    clamp = lambda x, top: min(max(x, 0), top) / top
    score = clamp(row["rev_cagr_2y"], .25) * 25
    score += clamp(row["fcf_margin"], .25) * 30
    score += clamp(row["net_margin"], .25) * 15
    score += (1 - min(max(row["liab_to_assets"], 0), 1)) * 15
    score += clamp(row["roe"], .30) * 15 if row["roe"] is not None else 0
    return round(score, 1)


def build_rows(frames):
    rows, rejected = [], Counter()
    required = ("revenue_base", "net_income", "ocf", "capex", "assets", "liabilities")
    for cik, revenue in frames.get("revenue", {}).items():
        facts = {key: frames.get(key, {}).get(cik) for key in TAGS}
        missing = [key for key in required if facts[key] is None]
        if missing:
            rejected["missing:" + ",".join(missing)] += 1
            continue
        if any(not finite(f.get("val")) for f in facts.values() if f is not None):
            rejected["invalid_number"] += 1
            continue
        if any(f.get("conflicting_tags") for f in facts.values() if f is not None):
            rejected["conflicting_revenue_tags"] += 1
            continue
        if not all(aligned(revenue, facts[key]) for key in ("net_income", "ocf", "capex")):
            rejected["mismatched_flow_period"] += 1
            continue
        if not all(aligned(revenue, facts[key], duration=False) for key in ("assets", "liabilities")):
            rejected["mismatched_balance_date"] += 1
            continue
        start, end = fact_date(revenue, "start"), fact_date(revenue, "end")
        base_start = fact_date(facts["revenue_base"], "start")
        base_end = fact_date(facts["revenue_base"], "end")
        if None in (start, end, base_start, base_end):
            rejected["missing_period_dates"] += 1
            continue
        if not (330 <= (end-start).days <= 400 and 330 <= (base_end-base_start).days <= 400
                and abs((end-start).days - (base_end-base_start).days) <= 14
                and 680 <= (end-base_end).days <= 780):
            rejected["noncomparable_annual_periods"] += 1
            continue
        r, r0 = revenue["val"], facts["revenue_base"]["val"]
        a, liab = facts["assets"]["val"], facts["liabilities"]["val"]
        capex, ocf, ni = facts["capex"]["val"], facts["ocf"]["val"], facts["net_income"]["val"]
        if a <= 0 or r0 <= 0 or r < 100e6 or capex < 0 or liab < 0:
            rejected["invalid_denominator_or_sign_or_size"] += 1
            continue
        growth = (r / r0) ** (365.25 / (end-base_end).days) - 1
        eq = facts["equity"]
        roe = (ni / eq["val"] if eq is not None and eq["val"] > 0
               and aligned(revenue, eq, duration=False) and eq["val"] / a >= .1 else None)
        flags = ["annual_only", "sector_model_unchecked", "no_price_or_valuation"]
        if roe is None:
            flags.append("roe_unusable_or_equity_small")
        if growth > 1 or ni / r > .5 or (ocf-capex) / r > .5:
            flags.append("one_off_or_economic_context_review")
        row = dict(cik=cik, name=revenue.get("entityName", str(cik)), revenue=r,
                   rev_cagr_2y=growth, net_margin=ni/r, fcf_margin=(ocf-capex)/r,
                   liab_to_assets=liab/a, roe=roe, method_version=METHOD,
                   period_start=str(start), period_end=str(end), flags=";".join(flags),
                   evidence_json=json.dumps({k: {p: f.get(p) for p in ("tag", "start", "end", "accn", "source_url")}
                                             for k, f in facts.items() if f is not None}, sort_keys=True))
        row["score"] = preliminary_score(row)
        rows.append(row)
    return rows, dict(rejected)


def fetch_frame(tags, period, frames_dir=None, failures=None):
    out = {}
    for tag in tags:
        url = f"https://data.sec.gov/api/xbrl/frames/us-gaap/{tag}/USD/{period}.json"
        try:
            if frames_dir is not None:
                payload = json.loads((Path(frames_dir) / f"{tag}_{period}.json").read_text())
            else:
                time.sleep(.25)
                request = urllib.request.Request(url, headers={"User-Agent": "research-agent-screen/2.0"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    payload = json.load(response)
            data = payload["data"]
            if not isinstance(data, list):
                raise ValueError("frame data is not a list")
        except (urllib.error.URLError, OSError, ValueError, KeyError) as exc:
            if failures is not None:
                failures.append({"url": url, "error": str(exc)})
            continue
        for item in data:
            fact = dict(item, tag=tag, source_url=url)
            previous = out.get(item["cik"])
            if previous is None:
                out[item["cik"]] = fact
            elif aligned(previous, fact) and finite(previous.get("val")) and finite(fact.get("val")):
                scale = max(abs(previous["val"]), abs(fact["val"]), 1)
                if abs(previous["val"] - fact["val"]) / scale > .01:
                    previous["conflicting_tags"] = True
    return out


def run(year, frames_dir=None):
    frames, failures = {}, []
    for key, tags in TAGS.items():
        period = f"CY{year-2}" if key == "revenue_base" else (
            f"CY{year}Q4I" if key in ("assets", "liabilities", "equity") else f"CY{year}")
        frames[key] = fetch_frame(tags, period, frames_dir, failures)
    if not frames["revenue"] or any(not frames[key] for key in ("ocf", "capex", "assets", "liabilities")):
        raise RuntimeError("Core frames are unavailable; keep the previous screen and disclose the failed refresh.")
    rows, rejected = build_rows(frames)
    keep = [r for r in rows if r["fcf_margin"] > .03 and r["net_margin"] > 0 and r["rev_cagr_2y"] > .03]
    keep.sort(key=lambda r: (-r["score"], r["cik"]))
    metadata = dict(method_version=METHOD, requested_calendar_year=year,
                    retrieved_at=datetime.now(ZoneInfo("America/New_York")).isoformat(),
                    scope="Standard US GAAP USD annual SEC frame facts; not a global listed-company universe",
                    price_coverage=False, point_in_time_backtest_safe=False,
                    filers_with_supported_revenue=len(frames["revenue"]), comparable_rows=len(rows),
                    passed_preliminary_filter=len(keep), exclusions=rejected, source_failures=failures,
                    warning="Liabilities/assets is not debt/assets. Ranking is annual, preliminary, and sector biased. Verify current filings and valuation before any rating.")
    return keep, metadata


def atomic_write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = handle.name
    os.replace(temporary, path)


def write_outputs(rows, metadata, output_dir):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(rows)
    atomic_write(Path(output_dir) / "screen_latest.csv", buffer.getvalue())
    atomic_write(Path(output_dir) / "screen_metadata.json", json.dumps(metadata, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("year", nargs="?", type=int, default=datetime.now(ZoneInfo("America/New_York")).year-1)
    parser.add_argument("--frames-dir", type=Path, help="Offline fixtures; never uses network when set")
    parser.add_argument("--output-dir", type=Path, default=Path("data"))
    args = parser.parse_args()
    try:
        rows, metadata = run(args.year, args.frames_dir)
        write_outputs(rows, metadata, args.output_dir)
    except (RuntimeError, ValueError, OSError) as exc:
        atomic_write(args.output_dir / "screen_last_attempt.json", json.dumps({"status": "failed", "error": str(exc)}) + "\n")
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps({k: metadata[k] for k in ("requested_calendar_year", "filers_with_supported_revenue", "comparable_rows", "passed_preliminary_filter")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())

