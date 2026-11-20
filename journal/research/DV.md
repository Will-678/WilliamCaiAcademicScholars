# DV (NYSE, USD)

Run 86, 2026-11-20T08:09:03-05:00. Status: **avoid**. Confidence: medium. Scores: null (incomplete). Fresh idea: yes (annual SEC screen lead, CIK 1819928); surfaced a pending merger. Validator: data/quality_run86_DV.json. Benchmark VTI pending; no paper reference.

## Sector model
Software and ad verification, but the stock is governed by a pending all-cash merger: price is pinned to the 13.60 deal price, so valuation is a merger spread and deal-completion risk question, not an operating-value question. FCF and P/E are context only.

## Thesis and evidence
DoubleVerify Holdings (NYSE: DV), digital ad verification. Q3 2026 10-Q (filed 2026-10-30) read: Q3 revenue 205.6M (+9%), 9M revenue 580.3M vs 542.7M (+7%), Q3 NI 15.9M vs 10.2M, 9M NI 35.3M vs 21.3M; 9M operating cash flow 136.4M, purchases of PP&E 31.4M (capitalized software not separately extracted); cash 250.9M; total liabilities 216.5M vs equity 1,133.4M; 156.2M shares outstanding at 2026-09-30. KEY FACT: on 2026-08-06 DV agreed to be acquired by Neptune BidCo US Inc. (parent of Nielsen Company (US) LLC) for 13.60 in cash per share; stockholders adopted the merger agreement on 2026-10-29; German, Cypriot and Australian competition clearances received by 2026-10-13 (Australian 14-day wait period after publication); 2026-11-09 8-K says closing is expected in Q4 2026; outside date 2026-05-06 (auto-extends to 2027-08-06 in some cases); financing includes a new revolving facility and a marketing period. Close 13.56 (2026-11-19) = 0.29% below 13.60 (spread 0.04, own arithmetic). Market cap 13.56 x 156.189M = 2.12B (approximation: period-end outstanding, excludes dilutive awards) = 32.8x TTM NI 64.6M (50.650 FY2025 + 35.257 - 21.321). Conclusion: this is a deal-arbitrage situation. Holding gives at most about 0.3% to the deal price if it closes within weeks, with downside to an unaffected price if it breaks. It is not a researched long idea and not a fresh value thesis.

## Countercase
If the deal closes, upside is capped at 13.60 (about 0.3% over the last close) and the shares are cashed out, creating a taxable event for no gain beyond the spread. If it breaks (financing, regulatory, litigation; two stockholder complaints alleging proxy disclosure deficiencies, unserved), the stock could fall materially below 13.56; the unaffected price was not researched here. A superior proposal is unlikely this late. Business quality (revenue +7%, rising GAAP NI) matters only if the deal fails.

## Invalidation
Not applicable as a long thesis. Reclassify if the merger agreement is terminated (then research as an operating company at the unaffected price) or if the closing 8-K is filed (then delisted).

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1819928/000110465926120666/dv-20260930x10q.htm (quarterly_filing, relevant_sections): 10-Q quarter ended 2026-09-30 filed 2026-10-30; downloaded and converted to text; balance sheet, income statement, cash flow, merger note, subsequent events, legal proceedings read; MD&A and risk factors skimmed only
- m: https://www.sec.gov/Archives/edgar/data/1819928/000110465926124574/tm2629362d1_8k.htm (secondary, full): 8-K Item 7.01 filed 2026-11-09, read in full: closing expected Q4 2026
- p: https://www.sec.gov/Archives/edgar/data/1819928/000110465926117471/tm2627835d1_8k.htm (secondary, relevant_sections): 8-K filed 2026-10-20 supplementing proxy: 13.60 per share, regulatory clearances; relevant sections read
- x: https://data.sec.gov/api/xbrl/companyfacts/CIK0001819928.json (annual_filing, relevant_sections): SEC XBRL company facts: FY2025 NI 50.650M (10-K accession 0001104659-26-020499), 9M25 NI 21.321M
- sub: https://data.sec.gov/submissions/CIK0001819928.json (secondary, relevant_sections): SEC submissions list: 10-Q and 8-K earnings 2026-10-30, 8-K 5.07 2026-10-29, 8-K 7.01 2026-11-09; earnings exhibit 99.1 not read
- qa: https://stockanalysis.com/stocks/dv/history/ (quote, relevant_sections): stockanalysis.com via WebFetch; close 2026-11-19 (origin undocumented)
- qb: https://finance.yahoo.com/quote/DV/history/ (quote, relevant_sections): Yahoo Finance via WebFetch; regular close Nov 19 (origin undocumented)

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-10-30 is latest periodic filing; 8-Ks through 2026-11-09 identified and the 11-09 and 10-20 ones read; earnings exhibit 99.1 not read.
- balance_sheet_verified: pass: At 2026-09-30 (USD thousands): cash 250,852; total assets 1,349,938; total liabilities 216,540; equity 1,133,398.
- cashflow_basis_verified: OPEN: 9M OCF 136,383 and purchase of PP&E 31,353 read; capitalized software spending not separately confirmed, so no FCF figure is claimed.
- share_count_basis_verified: pass: 156,189K shares outstanding at 2026-09-30 per balance sheet parenthetical; dilutive awards excluded, so market cap is an approximation.
- valuation_complete: OPEN: Merger spread computed only; no standalone valuation because price is deal-pinned.
- sector_model_appropriate: pass: Event-driven model for a stock under a signed cash merger; operating multiples are not the pricing driver.
- accounting_red_flags_reviewed: OPEN: Merger note and legal proceedings read; risk factors, audit matters and financing terms not read.
- counterthesis_written: pass: Capped upside, deal break risk, litigation.

## Unresolved gaps
- Closing conditions remaining and financing terms not read in the proxy
- Unaffected price and deal premium not researched
- Quote origins undocumented (two aggregators)
