#!/usr/bin/env python3
"""Check record structure, arithmetic, provenance and promotion requirements.
This cannot establish whether a cited page actually supports a claim.
It performs no network calls and never places trades.
"""
import argparse
import json
import math
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit

WEIGHTS = {"business_quality": 25, "cash_generation_growth": 20,
           "financial_resilience": 15, "valuation": 30, "catalysts_evidence": 10}
CHECKS = ("latest_filing_checked", "balance_sheet_verified", "cashflow_basis_verified",
          "share_count_basis_verified", "valuation_complete", "sector_model_appropriate",
          "accounting_red_flags_reviewed", "counterthesis_written")
STATUSES = {"attractive", "watch", "avoid", "insufficient_evidence"}


def number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def timestamp(value):
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return result if result.utcoffset() is not None else None
    except (AttributeError, TypeError, ValueError):
        return None


def public_url(value):
    try:
        parsed = urlsplit(value)
        return parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password
    except (TypeError, ValueError):
        return False


def fcf(ocf, capex):
    """Same period, same units. An absent capex figure can never mean zero."""
    if not isinstance(ocf, dict) or not isinstance(capex, dict):
        raise ValueError("Operating cash flow and capex are both required")
    for key in ("unit", "period_start", "period_end"):
        if not ocf.get(key) or ocf[key] != capex.get(key):
            raise ValueError("Cash flow periods and units must match")
    if not number(ocf.get("value")) or not number(capex.get("value")) or capex["value"] < 0:
        raise ValueError("Use finite operating cash flow and nonnegative reported spending")
    return ocf["value"] - capex["value"]


def annualized_scenario(price, terminal_price, dividends, years):
    if not all(number(v) for v in (price, terminal_price, dividends, years)):
        raise ValueError("Scenario values must be finite")
    if price <= 0 or years <= 0 or terminal_price < 0 or dividends < 0:
        raise ValueError("Scenario values have invalid signs")
    return ((terminal_price + dividends) / price) ** (1 / years) - 1


def validate(record, now=None):
    now = now or datetime.now(timezone.utc)
    errors, blockers = [], []
    if not isinstance(record, dict):
        return {"valid": False, "eligible_attractive": False, "errors": ["Record must be an object"], "blockers": []}
    if record.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    for key in ("ticker", "exchange", "currency", "sector_model", "thesis", "counterthesis", "invalidation"):
        if not isinstance(record.get(key), str) or not record[key].strip():
            errors.append(f"Missing {key}")
    as_of = timestamp(record.get("as_of"))
    if as_of is None or as_of > now + timedelta(minutes=5):
        errors.append("as_of needs a real timezone and cannot be in the future")
    status = record.get("status")
    if status not in STATUSES:
        errors.append("Unknown status")
    if record.get("confidence") not in ("low", "medium", "high"):
        errors.append("Unknown confidence")
    sources = record.get("sources", [])
    if not isinstance(sources, list) or any(not isinstance(s, dict) for s in sources):
        sources = []
        errors.append("sources must be a list of objects")
    by_id = {}
    for source in sources:
        identity = source.get("id")
        if not isinstance(identity, str) or not identity or identity in by_id:
            errors.append("Source IDs must be nonempty and unique")
            continue
        by_id[identity] = source
        if not public_url(source.get("url")):
            errors.append(f"{identity}: a public HTTPS URL is required")
        if not source.get("document_id") or not source.get("origin"):
            errors.append(f"{identity}: document_id and underlying origin are required")
        accessed = timestamp(source.get("accessed_at"))
        if accessed is None or accessed > now + timedelta(minutes=5):
            errors.append(f"{identity}: invalid accessed_at")
        elif as_of is not None and accessed > as_of + timedelta(minutes=5):
            errors.append(f"{identity}: source access is later than the research snapshot")
        if source.get("read_status") not in ("relevant_sections", "full", "snippet", "unread"):
            errors.append(f"{identity}: invalid read_status")
    primary = [s for s in sources if s.get("kind") in ("annual_filing", "quarterly_filing", "earnings_release")
               and s.get("read_status") in ("relevant_sections", "full")
               and not any(m in str(s.get("url", "")).lower() for m in ("/companyfacts/", "/api/xbrl/", "/submissions/"))]
    kinds = {s.get("kind") for s in primary}
    if "annual_filing" not in kinds or len({s.get("document_id") for s in primary}) < 2:
        blockers.append("Read the annual filing and a distinct recent filing or earnings document")
    checks = record.get("checks", {})
    if not isinstance(checks, dict):
        checks = {}
        errors.append("checks must be an object")
    for key in CHECKS:
        check = checks.get(key, {})
        if not isinstance(check, dict):
            check = {}
        refs = check.get("source_ids", [])
        supported = isinstance(refs, list) and bool(refs) and all(
            isinstance(ref, str) and ref in by_id and by_id[ref].get("read_status") in ("full", "relevant_sections") for ref in refs)
        if check.get("passed") is not True or not supported or not check.get("note"):
            blockers.append(key + " requires a passed, explained, sourced check")
    price = record.get("price", {})
    if not isinstance(price, dict):
        price = {}
    price_time = timestamp(price.get("as_of"))
    if not number(price.get("value")) or price.get("value", 0) <= 0:
        blockers.append("A positive dated quote is required")
    if price.get("currency") != record.get("currency"):
        blockers.append("Quote and valuation currencies differ")
    if price_time is None or as_of is None or price_time > as_of + timedelta(minutes=5):
        blockers.append("Quote time is missing or later than the research")
    elif as_of - price_time > timedelta(days=7):
        blockers.append("Quote is stale")
    if price_time is not None and now - price_time > timedelta(days=7):
        blockers.append("Quote is stale at validation time")
    if price.get("status") not in ("live", "delayed", "previous_close"):
        blockers.append("Quote availability status is unverified")
    expected_session = price.get("last_completed_session")
    if not isinstance(expected_session, str) or price_time is None or expected_session != price_time.date().isoformat():
        blockers.append("Verify the last completed market session and use a matching quote")
    quote_sources = price.get("sources", [])
    origins, matching = set(), 0
    if not isinstance(quote_sources, list):
        quote_sources = []
    for quote in quote_sources:
        if not isinstance(quote, dict):
            errors.append("Quote sources must be objects")
            continue
        source_id = quote.get("source_id")
        source = by_id.get(source_id, {}) if isinstance(source_id, str) else {}
        qt = timestamp(quote.get("as_of"))
        if (source.get("kind") == "quote" and source.get("read_status") in ("full", "relevant_sections")
                and number(quote.get("value")) and number(price.get("value")) and price["value"] > 0
                and abs(quote["value"] / price["value"] - 1) <= .005
                and quote.get("currency") == price.get("currency")
                and qt is not None and price_time is not None
                and abs((qt-price_time).total_seconds()) <= 60):
            origins.add(str(source.get("origin", "")).strip().lower())
            matching += 1
    if matching < 2 or len(origins - {""}) < 2:
        blockers.append("Two matching quote sources with different underlying origins are required")
    scores = record.get("scores", {})
    if not isinstance(scores, dict):
        scores = {}
        errors.append("scores must be an object")
    complete_scores = True
    for key, maximum in WEIGHTS.items():
        value = scores.get(key)
        if value is None:
            complete_scores = False
        elif not number(value) or not 0 <= value <= maximum:
            errors.append(f"{key} must be between 0 and {maximum}")
            complete_scores = False
    total = record.get("score_total")
    if complete_scores:
        if not number(total) or abs(total - sum(scores[k] for k in WEIGHTS)) > .001:
            errors.append("score_total does not equal its components")
    elif total is not None:
        errors.append("An incomplete score must have a null total")
    calculations = record.get("calculations", {})
    if not isinstance(calculations, dict):
        calculations = {}
        errors.append("calculations must be an object")
    cash = calculations.get("fcf")
    if cash is not None:
        try:
            if not isinstance(cash, dict):
                raise ValueError("FCF calculation must be an object")
            computed = fcf(cash.get("ocf"), cash.get("capex"))
            if not number(cash.get("value")) or not math.isclose(computed, cash["value"], rel_tol=1e-6, abs_tol=.01):
                errors.append("FCF arithmetic does not reconcile")
        except ValueError as exc:
            errors.append(str(exc))
    if not complete_scores:
        blockers.append("Complete the score components before promotion")
    if record.get("unresolved_critical_gaps"):
        blockers.append("Critical evidence gaps remain")
    if record.get("confidence") == "high" and blockers:
        errors.append("High confidence is inconsistent with unresolved promotion checks")
    if status == "attractive":
        if blockers:
            errors.extend("Attractive blocked: " + b for b in blockers)
        if not number(total) or total < 75 or not number(scores.get("valuation")) or scores["valuation"] < 21:
            errors.append("Attractive requires total >=75 and valuation >=21/30 (provisional method 2 rule)")
        if record.get("confidence") != "high":
            errors.append("Attractive requires high evidence confidence")
    return {"valid": not errors, "eligible_attractive": status == "attractive" and not errors and not blockers,
            "errors": errors, "blockers": blockers}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", nargs="+", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    results = []
    for path in args.records:
        try:
            result = validate(json.loads(path.read_text()))
        except (OSError, ValueError) as exc:
            result = {"valid": False, "eligible_attractive": False, "errors": [str(exc)], "blockers": []}
        results.append(dict(path=str(path), **result))
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "records": results,
              "valid": bool(results) and all(r["valid"] for r in results)}
    text = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n")
    print(text)
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
