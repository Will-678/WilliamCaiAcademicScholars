# CAMT (Nasdaq) research record, run 49

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run49_CAMT.json.
As of 2026-11-14T04:07:15-05:00. Close 101.73 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Camtek Ltd. (Nasdaq: CAMT; also TASE), Israeli inspection and metrology equipment for advanced packaging and HBM; files 20-F and 6-K, US GAAP in USD. Q3 2026 (6-K filed 2026-11-04): revenue 161.3M (+28% vs 126.0M), GAAP gross margin 50.0%, GAAP net income 42.8M (EPS 0.84 diluted; non-GAAP 0.99) vs a 53.2M net loss in Q3 2025, OCF 71.1M (Q2 was only 12.2M, so lumpy). Cash, deposits and securities 877.1M; convertible notes 489.2M, so net cash about 388M. Guidance: Q4 revenue about 180M (+40%), 2026 about 595M, 2027 above 800M (+35%), management says it has a year of visibility. At 101.73 (2026-11-13 close, -3.5%, 52-week 89.13-215.99, about 53% below the high) and 46.73M shares (stockanalysis; point-in-time count unread), market cap about 4.75B, EV about 4.36B, EV/TTM revenue 8.0x (544.3M), EV/2026 guide 7.3x, EV/2027 guide 5.4x. Trailing GAAP P/E 38.4x and forward 20.5x per stockanalysis (unverified forward). FCF cannot be computed because capex was not read; it is missing, not zero. Market view: the fall from about 216 likely prices an AI packaging capex cycle peak and a weak H1 (Q2 revenue +8%); the evidence that differs is the guided second-half and 2027 acceleration, but that is management guidance, unverified by orders.

## Countercase
Guidance is management's own and a customer-concentrated, cyclical industry can reverse; H1 2026 growth was only about 8% so the stock may be right to doubt the ramp. Q3 2025 had a 53.2M GAAP loss (cause unread, probably convertible or FX revaluation), so GAAP earnings swing on non-operating items and TTM P/E is unreliable. Quarterly OCF is lumpy (12.2M vs 71.1M). Convertible notes 489M are a dilution and refinancing claim. Export controls, China exposure and customer concentration (largest customers and backlog not read) are unreviewed. Foreign private issuer, so disclosure is semi-annual style plus 6-Ks; the 20-F was not read. SEC XBRL on file shows only FY2025 revenue 496.1M, net income 50.7M, OCF 141.9M.

## What would change the view
Thesis fails if Q4 revenue falls short of about 180M, 2027 visibility weakens, gross margin falls below about 47%, or key customers cut advanced packaging inspection orders.

## Checks
- latest_filing_checked: passed. Q3 2026 6-K (2026-11-04) read via extract; submissions show nothing later; 20-F text not read.
- balance_sheet_verified: passed. Cash, deposits and securities 877.1M and convertible notes 489.2M at 2026-09-30 from release; other liabilities and leases not read.
- cashflow_basis_verified: NOT passed. Q3 OCF 71.1M and Q2 12.2M read, but capex and the cash flow statement were not shown, so FCF is missing (not zero).
- share_count_basis_verified: NOT passed. 46.73M shares from stockanalysis only; period-end and diluted counts from the filing not read.
- valuation_complete: NOT passed. EV to revenue computed; no FCF, no peers (NVMI, ONTO, KLAC, BESI), no verified forward P/E or history.
- sector_model_appropriate: passed. Semiconductor equipment: growth, margins, OCF, net cash after converts; cyclicality noted.
- accounting_red_flags_reviewed: NOT passed. Q3 2025 net loss cause, convertible terms, revenue recognition and customer concentration not read.
- counterthesis_written: passed. Covers guidance risk, cyclicality, GAAP volatility, converts and concentration.

## Unresolved gaps
- Capex and FCF missing
- 20-F, convertible terms, customer concentration unread
- Peers and history not done
- Period-end share count not from a filing
- Q3 2025 loss cause unread
- Quotes: two publishers, publisher-level independence only
- Scores not assigned

## Sources
- e1: https://www.sec.gov/Archives/edgar/data/1109138/000117891326005000/zk2636329.htm (earnings_release, relevant_sections) Q3 2026 earnings release inside Form 6-K filed 2026-11-04 via WebFetch extract (issuer release); capex and cash flow statement not shown
- e2: https://www.sec.gov/Archives/edgar/data/1109138/000117891326003975/zk2635905.htm (earnings_release, relevant_sections) Q2 2026 earnings release inside Form 6-K filed 2026-08-10 via WebFetch extract
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001109138.json (annual_filing, relevant_sections) SEC XBRL companyfacts FY2025 20-F: revenue 496.072M, NI 50.722M, OCF 141.871M; 20-F text not read
- sub: https://data.sec.gov/submissions/CIK0001109138.json (secondary, relevant_sections) SEC submissions JSON 2026-11-14: latest 6-K 2026-11-04, no later 6-K
- qa: https://stockanalysis.com/stocks/camt/ (quote, relevant_sections) stockanalysis.com via WebFetch: close 101.73 at 4:00 PM EST 2026-11-13, 46.73M shares, market cap 4.75B, TTM revenue 544.32M
- qb: https://finance.yahoo.com/quote/CAMT/history/ (quote, relevant_sections) Yahoo Finance via WebFetch: close 101.73 on 2026-11-13; 105.42 on 11-12
