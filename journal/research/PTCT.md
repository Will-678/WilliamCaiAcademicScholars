# PTCT (Nasdaq) research record, run 68

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run68_PTCT.json.
As of 2026-11-17T08:10:00-05:00. Close 60.97 USD on 2026-11-16 (stockanalysis.com and Yahoo Finance agree; publisher-level only, origin undocumented). Benchmark VTI pending; no paper reference.

## Sector model
Commercial-stage biopharma (mid): product durability (Sephience ramp, Translarna and Emflaza erosion), royalty income (Evrysdi) and royalty-sale liability, collaboration windfalls, acquired IPR&D, convertible debt, cash runway; not a generic earnings screen.

## Thesis and evidence
PTC Therapeutics (Nasdaq: PTCT). Screen pass (score 70.0) rests on FY2025 net income 682.6M, which came from 998.4M of 9M25 collaboration and license revenue (Novartis license, 10-Q) and is not recurring. TTM (FY25 + 9M26 - 9M25): revenue 1,155.6M, net loss -106.0M, OCF 10.5M, capex 8.4M, FCF 2.1M. 9M26 revenue 990.9M (product 740.3M vs 402.7M, Q3 product 275.9M vs 131.0M; Sephience Q3 181.9M, +20% on Q2; royalties 199.6M, Q3 81.7M incl. Evrysdi). Q3 net loss -51.7M includes 111.0M acquired IPR&D (ST-920 Fabry gene therapy from Sangamo, up to 100M more contingent, BLA planned Q4 2026) and 19.3M debt extinguishment loss. FY26 guide: total revenue 1.29B to 1.32B, product 960M to 990M (raised); implied Q4 product about 220M to 250M, below Q3 276M (secondary source). Close 60.97 x 83,544,284 shares (cover 2026-10-27) = market cap 5,093M = 4.4x TTM revenue, 3.9x FY26 guided revenue midpoint 1,305M. Cash and marketable securities 2,127.9M; 0% convertible notes due 2031 carrying 536.3M; liability for sale of future royalties 2,305.6M (a debt-like claim on royalties); stockholders deficit -191.2M; total liabilities 3,398.9M. Quote 11-13 was 63.49. The price must be judged on forward product growth and breakeven, not trailing earnings: trailing P/E is meaningless.

## Counterthesis
Strongest countercase: the screen's growth and margin come from a one-time licence payment; underlying GAAP profit is negative and FCF about zero. Royalty sale liability of 2.3B means a large share of Evrysdi royalties is already sold. SBC 70.5M for 9M. Legacy Translarna and Emflaza are eroding (Emflaza 25.1M vs 35.2M) and Translarna includes a Russian government order. Q4 guide implies a sequential step-down. Another 100M contingent and acquired IPR&D charges recur as the company buys pipeline. A negative equity base and rising debt (convertible 550M issued) add dilution and refinancing exposure.

## Invalidation
Fails if Sephience growth stalls or pricing/reimbursement erodes, cash flow breakeven is missed, royalty-sale obligations bite, or pipeline purchases keep consuming cash.

## Unresolved gaps
- Trailing earnings are a windfall artifact; forward profitability model absent
- MD&A, ST-920 terms, royalty-sale agreement terms, Q4 guide source unread
- Peers and history not compared
- Quote independence is publisher level only
- Scores not assigned

## Checks
- latest_filing_checked: passed; Q3 10-Q and release both filed 2026-10-29; no later 10-Q or 8-K checked in submissions list.
- balance_sheet_verified: passed; 2026-09-30 cash 508.894M, marketable securities 1,619.024M, convertible notes 536.268M, royalty liability 2,305.603M, total liabilities 3,398.924M; term loan balance not found.
- cashflow_basis_verified: passed; OCF FY25 711.196M, 9M26 44.760M, 9M25 745.469M; capex 8.860M, 6.046M, 6.486M; acquired IPR&D not in capex; matching periods.
- share_count_basis_verified: passed; 83,544,284 shares at 2026-10-27 cover; dilution from 2031 convertible not modeled.
- valuation_complete: NOT passed; Price to sales and FCF computed; no peer or history comparison, no forward profit model.
- sector_model_appropriate: NOT passed; Needs Sephience durability, payer and label data, patents, royalty terms; MD&A and pipeline unread.
- accounting_red_flags_reviewed: NOT passed; Licence revenue windfall and royalty liability identified; MD&A, audit matters, Item 4 unread.
- counterthesis_written: passed; Covers windfall, royalty sale, legacy erosion, Q4 step-down, pipeline spend, dilution.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1070081/000110465926120223/tmb-20260930x10q.htm (quarterly_filing, relevant_sections); Q3 2026 10-Q via WebFetch, balance sheet, cash flow, notes; excerpt truncated before ST-920 terms and MD&A
- r: https://www.sec.gov/Archives/edgar/data/0001070081/000110465926120200/tmb-ex99d1.htm (earnings_release, relevant_sections); Earnings release Ex 99.1 filed with 8-K 2026-10-29 via WebFetch (same underlying data as the 10-Q, not independent corroboration)
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001070081.json (annual_filing, relevant_sections); SEC XBRL companyfacts by script: FY2025 10-K 0001104659-26-017575, 9M26 and 9M25 matched
- qa: https://stockanalysis.com/stocks/ptct/history/ (quote, relevant_sections); stockanalysis.com via WebFetch; close 2026-11-16 (origin undocumented)
- qb: https://finance.yahoo.com/quote/PTCT/history/ (quote, relevant_sections); Yahoo Finance via WebFetch; close 2026-11-16 (origin undocumented)
