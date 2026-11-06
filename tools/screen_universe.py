#!/usr/bin/env python3
"""Stage 1 screen: every U.S. SEC filer with annual XBRL data, using SEC 'frames' bulk endpoints.
Fundamentals only (no prices). Writes data/screen_latest.csv ranked by a simple quality score.
Usage: python3 tools/screen_universe.py [YEAR]   (default: latest year with broad coverage)
Uses a generic User-Agent; never put personal contact details in it.
"""
import csv, json, sys, time, urllib.request, urllib.error

UA = "research-agent-screen/1.0"
BASE = "https://data.sec.gov/api/xbrl/frames/us-gaap/{tag}/USD/{per}.json"

def frame(tags, per):
    """Return {cik: (value, name)} using the first tag that has data for each company."""
    out = {}
    for tag in tags:
        url = BASE.format(tag=tag, per=per)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)["data"]
        except urllib.error.HTTPError:
            continue
        for d in data:
            out.setdefault(d["cik"], (d["val"], d["entityName"]))
        time.sleep(0.2)
    return out

def run(year):
    cy, base = f"CY{year}", f"CY{year-2}"
    inst = f"CY{year}Q4I"
    rev_tags = ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "SalesRevenueNet"]
    rev, rev0 = frame(rev_tags, cy), frame(rev_tags, base)
    ni = frame(["NetIncomeLoss"], cy)
    ocf = frame(["NetCashProvidedByUsedInOperatingActivities"], cy)
    capex = frame(["PaymentsToAcquirePropertyPlantAndEquipment"], cy)
    assets = frame(["Assets"], inst)
    liab = frame(["Liabilities"], inst)
    equity = frame(["StockholdersEquity"], inst)
    rows = []
    for cik, (r, name) in rev.items():
        if r < 100e6 or cik not in rev0 or rev0[cik][0] <= 0:
            continue
        if cik not in ocf or cik not in ni or cik not in assets or cik not in liab:
            continue
        o, n, a, l = ocf[cik][0], ni[cik][0], assets[cik][0], liab[cik][0]
        cx = capex.get(cik, (0, ""))[0]
        fcf = o - cx
        cagr = (r / rev0[cik][0]) ** 0.5 - 1
        eq = equity.get(cik, (None, ""))[0]
        roe = n / eq if eq and eq > 0 else None
        rows.append(dict(cik=cik, name=name, revenue=r, rev_cagr_2y=cagr, net_margin=n / r,
                         fcf_margin=fcf / r, liab_to_assets=l / a, roe=roe))
    def score(x):
        s = 0
        s += min(max(x["rev_cagr_2y"], 0), 0.25) / 0.25 * 25
        s += min(max(x["fcf_margin"], 0), 0.25) / 0.25 * 30
        s += min(max(x["net_margin"], 0), 0.25) / 0.25 * 15
        s += (1 - min(max(x["liab_to_assets"], 0), 1)) * 15
        s += (min(max(x["roe"], 0), 0.30) / 0.30 * 15) if x["roe"] is not None else 0
        return round(s, 1)
    for x in rows:
        x["score"] = score(x)
    keep = [x for x in rows if x["fcf_margin"] > 0.03 and x["net_margin"] > 0 and x["rev_cagr_2y"] > 0.03]
    keep.sort(key=lambda x: -x["score"])
    return len(rev), len(rows), keep

if __name__ == "__main__":
    year = int(sys.argv[1]) if len(sys.argv) > 1 else 2025
    n_rev, n_rows, keep = run(year)
    with open("data/screen_latest.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(keep[0].keys()))
        w.writeheader()
        for x in keep:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in x.items()})
    print(f"year={year} filers_with_revenue={n_rev} usable={n_rows} passed={len(keep)}")
    for x in keep[:15]:
        print(x["score"], x["name"], f"cagr={x['rev_cagr_2y']:.1%}", f"fcf={x['fcf_margin']:.1%}", f"liab/assets={x['liab_to_assets']:.0%}")
