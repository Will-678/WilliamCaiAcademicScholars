# BX (NYSE) research record, run 46

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run46_BX.json (valid; not attractive-eligible).
As of 2026-11-13T16:06:01-05:00. Close 120.17 USD on 2026-11-13 (stockanalysis.com and Yahoo agree; publisher-level independence only). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Blackstone Inc. (NYSE: BX), largest alternative asset manager. Q3 2026 (release Exhibit 99.1, 2026-10-22): GAAP net income to Blackstone 662M (+6%), Distributable Earnings 1.7B (-9%), DE per share 1.32 (vs 1.52, -13%), Fee Related Earnings 1.6B (+6%; 1.26 per share), fee-related performance revenues 540M (+19%), total AUM 1,368.3B (+10%), inflows 63.3B, deployment 30.1B, realizations 33.1B, net accrued performance revenues 7.3B (5.84 per share, -3% q/q). Dividend 1.12 for Q3, 5.06 over the last twelve months. At 120.17 (2026-11-13 close; 52-week 101.73-165.14, so about 27% below the high) TTM GAAP EPS is 4.49 (3.87 FY2025 + 3.19 9M26 - 2.57 9M25), P/E 26.8x; trailing dividend yield about 4.2% on 5.06. Q3 DE per share annualized would imply about 22.8x, shown only as context because realizations are lumpy. The market may be discounting weaker realizations and the 9% DE decline while fee earnings and AUM keep growing.

## Countercase
DE fell 9% and DE per share 13% while FRE rose 6%: earnings quality depends on performance revenues and realizations that are cyclical, and net accrued performance revenue slipped 3% q/q. Stock-based compensation was 1.25B in 9M26 and is a real cost; GAAP share count (751M Class A versus about 1.24B including partnership units) must be handled with care. Debt on the consolidated balance sheet is 13.4B including consolidated funds and a new 1.1B senior note offering (5.650% 2031 and 5.900% 2033, 8-K 2026-11-02, use of proceeds not stated). Private credit and real estate marks, retail product redemptions, fee compression and a weak realization market are thesis breakers. The stock is a large index holding, so it duplicates exposure already held in broad US funds.

## What would change the view
Thesis breaks if quarterly DE per share keeps falling with falling inflows, retail fund redemptions accelerate, net accrued performance revenue declines for several quarters, or fee-related earnings growth stalls.

## Checks
- latest_filing_checked: passed. Latest 10-Q filed 2026-11-06, earnings 8-K 2026-10-22, notes 8-K 2026-11-02; 10-Q text itself not read.
- balance_sheet_verified: NOT passed. Only XBRL totals seen (liabilities 28.6B, equity 8.84B, debt 13.4B at 2026-09-30) and these include consolidated funds; corporate debt separate from fund debt not verified.
- cashflow_basis_verified: NOT passed. Consolidated OCF (9M26 4.895B) mixes consolidated fund activity; not usable as owner earnings. DE from the release is the intended basis but TTM DE not assembled.
- share_count_basis_verified: NOT passed. Class A 751.1M (cover) versus 1.24B total including partnership units (stockanalysis); per-share DE basis not reconciled to the 10-Q.
- valuation_complete: NOT passed. TTM GAAP P/E and trailing dividend yield computed; TTM DE, price to DE, peers (KKR, APO, ARES, CG) and history not done.
- sector_model_appropriate: passed. Alternative asset manager: DE, FRE, performance revenue and dividend used; generic FCF and liability ratios not used.
- accounting_red_flags_reviewed: NOT passed. Noted consolidated funds, SBC 1.25B 9M26 and performance revenue timing; 10-Q notes, valuation marks and controls unread.
- counterthesis_written: passed. Covers DE decline, performance revenue cyclicality, SBC, leverage, private credit and index duplication.

## Unresolved gaps
- TTM DE, price to DE and peers not done
- 10-Q notes, corporate versus fund debt, share and unit basis unread
- Quotes: two publishers, publisher-level independence only
- Scores not assigned

## Sources
- e8: https://www.sec.gov/Archives/edgar/data/1393818/000119312526428297/d160590dex991.htm (earnings_release, relevant_sections)
- n8: https://www.sec.gov/Archives/edgar/data/1393818/000119312526443854/d377521d8k.htm (secondary, relevant_sections)
- sub: https://data.sec.gov/submissions/CIK0001393818.json (secondary, relevant_sections)
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001393818.json (annual_filing, relevant_sections)
- qa: https://stockanalysis.com/stocks/bx/ (quote, relevant_sections)
- qb: https://finance.yahoo.com/quote/BX/history/ (quote, relevant_sections)
