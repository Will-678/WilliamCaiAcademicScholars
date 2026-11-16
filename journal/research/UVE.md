# UVE (NYSE) research record, run 64

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run64_UVE.json.
As of 2026-11-16T16:08:00-05:00. Close 48.57 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Sector model
Property and casualty insurer (Florida homeowners, hurricane exposed): combined ratio, reinsurance cost and retention, reserve development, book value and ROE; price to book and earnings; generic FCF not used (capex not read; insurer OCF is not owner earnings).

## Thesis and evidence
Universal Insurance Holdings (NYSE: UVE), Q3 2026 10-Q (0000891166-26-000094, filed 2026-10-29; financial statements read, MD&A not present in the extract) and earnings release Ex 99.1 (8-K 0000891166-26-000092, 2026-10-22). Q3 revenue 439.3M (+9.6%), NI 52.5M, diluted EPS 1.80 (adjusted 1.93); 9M revenue 1,259.9M, NI 166.0M, EPS 5.73. Net combined ratio 91.0% vs 96.4% (loss 64.6% vs 70.2%, expense 26.4%); ceded premium ratio 27.6% vs 32.7% after the new reinsurance program from 2026-06-01. Direct premiums written 608.9M (+2.7%): Florida 414.4M (-3.3%), other states 194.5M (+18.5%); policies in force 953,611 (+7.9%; Florida 598,104, other 355,507). Book value per share 23.37 (+32.4%), annualized ROCE 32.7% (9M 37.0%). TTM NI 232.6M (FY2025 183.0M + 9M26 166.0M - 9M25 116.4M). Close 48.57 on 2026-11-13 (stockanalysis, Yahoo agree), 27,670,206 shares (cover 2026-10-26): market cap 1,344M, 5.8x TTM NI, 2.08x book (646.0M equity). Debt 97.3M (new 100M issued and 101.1M repaid in 9M26), cash 569.5M, invested assets 1,606.0M, total liabilities 2,537.5M, unpaid losses and LAE 616.1M (680.7M at year end). Dividend raised to 0.29 per quarter (8-K 2026-11-05, from 0.16; 2.4% annualized yield); 9M buybacks 19.2M. The market probably discounts the cyclical softening of Florida pricing and hurricane tail risk; evidence that differs is two years of falling ratios, growth outside Florida and a book growing 32%. The trailing multiple is likely at a cyclical peak of profitability, not a stable earnings level.

## Countercase
Earnings are at a cyclical high: a combined ratio of 91% after 96% a year ago, with the 2026 hurricane season partly unplayed (a post-quarter storm, Hurricane Isaias near Destin, is reported with no loss estimate; the release says claims were less significant than anticipated). Florida direct premiums are falling 3.3% as rates soften; growth comes from other states with less history. A single large storm could exhaust a reinsurance tower whose retention, limit and cost were not disclosed in what I read. Reserve development, catastrophe losses, statutory surplus, Citizens depopulation exposure and reinsurer credit were not read. ROE of 32% to 37% is unlikely to persist and low P/E on peak earnings is a classic insurer trap. Adjusted EPS excludes unrealized investment losses; AOCI loss 69.9M. Insurer cash flow includes float and timing, not owner earnings. Peers (HCI, HRTG, KINS, PGR), own-history multiples and 10-K reserve disclosures not compared.

## Invalidation
Thesis fails if a major Florida hurricane or reserve strengthening pushes the combined ratio above about 100% for a year, if reinsurance costs rise sharply at the 2027 renewal, if prior-year development turns adverse, or if Florida policy counts and premiums keep falling while non-Florida growth reverts to losses.

## Sources
- q: quarterly_filing, relevant_sections: https://www.sec.gov/Archives/edgar/data/891166/000089116626000094/uve-20260930.htm (Q3 2026 10-Q via WebFetch extraction (cover, balance sheet, income statement, cash flow items, early notes; MD&A and most notes not in extract))
- er: earnings_release, relevant_sections: https://www.sec.gov/Archives/edgar/data/0000891166/000089116626000092/a3q26uveex-991xearningspre.htm (Earnings release Ex 99.1 (8-K 2026-10-22) via WebFetch; ratios, policies, DPW, BVPS, ROCE, reconciliation items)
- div: secondary, relevant_sections: https://www.sec.gov/Archives/edgar/data/891166/000089116626000096/uve-20261105.htm (8-K 2026-11-05 via WebFetch: Item 7.01 dividend 0.29 per share payable 2026-12-11; press release exhibit itself not read)
- fy: annual_filing, relevant_sections: https://data.sec.gov/api/xbrl/companyfacts/CIK0000891166.json (SEC XBRL companyfacts by curl; FY2025 and 9M periods (revenue, NI, OCF, equity, liabilities, debt))
- sub: secondary, relevant_sections: https://data.sec.gov/submissions/CIK0000891166.json (SEC submissions list read 2026-11-16: 8-K 2026-11-05, 10-Q 2026-10-29; no later periodic filing)
- qa: quote, relevant_sections: https://stockanalysis.com/stocks/uve/history/ (stockanalysis.com via WebFetch; close 2026-11-13 (origin undocumented))
- qb: quote, relevant_sections: https://finance.yahoo.com/quote/UVE/history/ (Yahoo Finance via WebFetch; close 2026-11-13 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q 2026-10-29, earnings 8-K 2026-10-22 and 8-K 2026-11-05 (dividend) read in part; no later filing in submissions list.
- balance_sheet_verified: pass: Cash 569,461K, invested assets 1,605,981K, total assets 3,183,570K, total liabilities 2,537,534K, debt 97,336K, equity 646,036K, unpaid losses and LAE 616,079K at 2026-09-30.
- cashflow_basis_verified: NOT passed: OCF FY25 381.5M, 9M26 338.9M, 9M25 355.4M known (TTM 365.0M) but capex not read, so FCF is intentionally not computed; insurer valuation uses earnings and book.
- share_count_basis_verified: pass: 27,670,206 shares at 2026-10-26 from the cover.
- valuation_complete: NOT passed: P/E and P/B computed; peers, own history, normalized combined ratio not compared.
- sector_model_appropriate: NOT passed: Combined ratio, ceded ratio, policies, DPW read; reserve development, catastrophe losses, reinsurance retention and statutory capital not read.
- accounting_red_flags_reviewed: NOT passed: Adjusted EPS excludes realized and unrealized gains and interest; reserve adequacy, Note on reinsurance recoverables and debt terms not read.
- counterthesis_written: pass: Covers peak earnings, Florida shrinkage, hurricane and reinsurance, reserves.

## Calculations
```
{
 "valuation": {
  "price": 48.57,
  "shares_outstanding": 27670206,
  "share_basis": "10-Q cover 2026-10-26",
  "market_cap_usd": 1343941905,
  "ttm_revenue_musd": 1667.8,
  "ttm_net_income_musd": 232.6,
  "pe_ttm": 5.8,
  "ttm_fcf_musd": null,
  "fcf_yield_pct": null,
  "basis": "TTM = FY2025 + 9M26 - 9M25, USD millions: revenue 1,603.9+1,259.9-1,196.0; NI 183.0+166.0-116.4 = 232.6; price to book 1,344/646.0 = 2.08; FCF not computed (capex not read, missing not zero)"
 },
 "cash_flow": {
  "ocf_ttm_musd": 365.0,
  "capex_ttm_musd": null,
  "ocf_9m26_musd": 338.9,
  "capex_9m26_musd": null,
  "fcf_q3_musd": null,
  "basis": "USD millions; OCF 381.5+338.9-355.4; capex missing"
 },
 "balance_sheet": {
  "cash_musd": 569.5,
  "debt_musd": 97.3,
  "total_liabilities_musd": 2537.5,
  "basis": "10-Q 2026-09-30; cash excludes restricted cash 68.6M and invested assets 1,606.0M"
 }
}
```

## Unresolved gaps
- MD&A, reserve development, catastrophe losses and reinsurance retention not read
- Post-quarter storm loss not estimated
- Capex missing so FCF not computed
- Peers and own-history not compared
- Quote independence is publisher level only
- Scores not assigned
