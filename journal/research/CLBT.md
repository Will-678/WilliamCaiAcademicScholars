# CLBT (Nasdaq) research record, run 48

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run48_CLBT.json (valid, not attractive-eligible).
As of 2026-11-14T05:05:19+00:00. Close 11.53 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Cellebrite DI Ltd. (Nasdaq: CLBT), Israeli digital-forensics software for law enforcement, small-mid cap; files 20-F and 6-K (no 10-Q), US GAAP in USD. Q3 2026 (release 2026-11-12): revenue 149.0M (+18%), ARR 528.5M (+20%), GAAP net income 26.7M (EPS 0.10 diluted), OCF 56.6M, capex 4.8M, FCF 51.8M (34.8% margin), TTM FCF 166.0M (company figure, 30.9% margin), adjusted EBITDA 53.6M. Cash, deposits and securities about 593.3M, no borrowings line. Guidance 2026: revenue 553-558M, ARR 550-560M (14-16%, reaffirmed, below the current 20% pace), adjusted EBITDA 163-166M (raised); Q4 revenue 145-150M. At 11.53 (2026-11-13 close, +5.9% on the day, 52-week 9.58-19.98) market cap is about 2.89B (250.79M shares), net cash about 593M, EV about 2.30B, FCF yield 5.7% of market cap (7.2% of EV), EV/FCF 13.8x. FY2025 SBC was 44.9M (9% of revenue), so FCF after SBC is nearer 120M (about 4%). Trailing P/E about 46x GAAP (stockanalysis; 0.10 quarterly EPS), forward 17.6x (unverified). The market may be discounting the growth reset after the Q2 ARR miss and the CEO change; the evidence that differs is steady 18-20% growth, 30%+ FCF margins and large net cash, but the Q4 ARR guide implies a sharp slowdown.

## Countercase
The price fell about 30% after Q2 (per search summaries, unverified) because ARR missed and full-year guidance was cut; ARR guide of 14-16% growth for 2026 against 20% in Q3 suggests either conservatism or a deceleration, and the stock fell 14% on 11-12 despite a beat before rebounding 5.9%. The Corellium acquisition remains under CFIUS review with possible divestment. A CEO transition (Shiv Ramji replacing Thomas Hogan, per search summaries, unverified) adds execution risk. Revenue depends on government and law-enforcement budgets and a few legal and privacy constraints; GAAP profit is small (net margin about 16% for 2025) with 9% SBC; Forms 144 filed 11-10 and Form 4 on 11-12/13 indicate insider sales or transfers I did not read. Foreign private issuer reporting gives less frequent disclosure and I did not read the 20-F.

## What would change the view
Thesis fails if ARR growth drops below about 12%, FCF margin falls under 25%, the CFIUS review forces a Corellium divestment on poor terms, or large insider selling and customer budget cuts follow.

## Checks
- latest_filing_checked: passed. Q3 2026 release (6-K, 2026-11-12) read; submissions show no later 6-K; 20-F text for 2025 not read.
- balance_sheet_verified: passed. Cash 223.1M, short-term deposits 121.2M, marketable securities 139.6M current and 109.4M non-current; no borrowings line in the release; lease obligations and other liabilities beyond 25.4M not read.
- cashflow_basis_verified: passed. Q3 OCF 56.581M minus capex 4.784M = FCF 51.797M reconciles; TTM FCF 166.0M is a company figure (20-F FY2025 OCF 173.5M less capex 13.2M = 160.3M); capitalized software and acquired intangibles are excluded from capex.
- share_count_basis_verified: NOT passed. 250.79M shares from stockanalysis only; release gives weighted basic 249.48M and diluted 254.36M for Q3; period-end count from the 6-K/20-F cover not read.
- valuation_complete: NOT passed. FCF yield and EV computed; forward P/E unverified; no peers (Axon, Palantir, Tyler, Verint) or history; SBC for TTM not read.
- sector_model_appropriate: passed. Subscription software: ARR, revenue growth, FCF after SBC, net cash; bank ratios not applicable.
- accounting_red_flags_reviewed: NOT passed. Adjusted EBITDA definition, SBC, capitalized software, deferred revenue and CFIUS contingency not read in the 20-F; insider Forms 144/4 unread.
- counterthesis_written: passed. Covers deceleration, CFIUS, CEO change, SBC and insider sales.

## Unresolved gaps
- 20-F text, SBC, leases and adjusted EBITDA reconciliation unread
- Peers and history not done
- Period-end share count not from a filing
- CEO change and Q2 guidance cut known only from search summaries
- Quotes: two publishers, publisher-level independence only
- Scores not assigned

## Sources
- e1: https://www.sec.gov/Archives/edgar/data/1854587/000121390026118368/ea031199501ex99-1.htm (earnings_release, relevant_sections) Q3 2026 press release, Exhibit 99.1 to 6-K filed 2026-11-12 via WebFetch (issuer release)
- k1: https://www.sec.gov/Archives/edgar/data/1854587/000162828026013790/cele-20251231.htm (annual_filing, relevant_sections) Annual report on Form 20-F for 2025 filed 2026-03-03; facts taken from SEC XBRL companyfacts only, text not read
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001854587.json (annual_filing, relevant_sections) SEC XBRL companyfacts FY2025 20-F: revenue 475.675M, NI 78.326M, OCF 173.544M, capex 13.225M, SBC 44.892M
- sub: https://data.sec.gov/submissions/CIK0001854587.json (secondary, relevant_sections) SEC submissions JSON 2026-11-14: files 20-F and 6-K (foreign private issuer, no 10-Q); latest 6-K 2026-11-12, Forms 144 on 11-10
- n1: https://www.calcalistech.com/ctechnews/article/r1kdphslml (secondary, snippet) Search result listing only (snippet); CEO change and Q2 guidance cut context is from search summaries, unverified
- qa: https://stockanalysis.com/stocks/clbt/ (quote, relevant_sections) stockanalysis.com via WebFetch: close 11.53 at 4:00 PM EST 2026-11-13, 250.79M shares, 52-week 9.58-19.98
- qb: https://finance.yahoo.com/quote/CLBT/history/ (quote, relevant_sections) Yahoo Finance via WebFetch: close 11.53 on 2026-11-13; 10.89 on 11-12; 12.70 on 11-11
