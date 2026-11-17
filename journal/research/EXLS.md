# EXLS (Nasdaq) research record, run 68

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run68_EXLS.json.
As of 2026-11-17T08:10:00-05:00. Close 43.6 USD on 2026-11-16 (stockanalysis.com and Yahoo Finance agree; publisher-level only, origin undocumented). Benchmark VTI pending; no paper reference.

## Sector model
IT and business process services with analytics (mid): organic versus acquired growth, client concentration, India wage and INR exposure, buyback funded by debt, capitalized software; not a software or bank screen.

## Thesis and evidence
ExlService Holdings (Nasdaq: EXLS). Q3 2026 10-Q and release filed 2026-10-27. Q3 revenue 634.0M, +19.7% reported (+19.9% constant currency); Data and AI-led 406.9M (+36.3%, release says 31% organic), Digital operations 227.1M (-1.7%). 9M revenue 1,799.1M (+16.4%). Adjusted EPS Q3 0.62 (+28.5%), GAAP diluted 0.45; adjusted operating margin 19.3% vs 19.4%, GAAP 14.0%. FY26 guide raised: revenue 2.430B to 2.440B (15% organic), adjusted EPS 2.34 to 2.36. TTM (FY25 + 9M26 - 9M25): revenue 2,341.7M, NI 260.6M, OCF 326.2M, capex 55.0M, FCF 271.2M; SBC TTM 93.0M leaves 178.2M. Close 43.60 x 150,788,731 shares (cover 2026-10-23) = market cap 6,574M = 25.2x TTM GAAP NI, 18.6x FY26 adjusted EPS midpoint 2.35; FCF yield 4.1% (2.7% after SBC). Cash 154.1M plus short-term investments 178.6M, borrowings 511.0M (new 1B secured facility Aug 2026), total liabilities 1,145.3M vs 789.5M at year-end; iMerit acquired 2026-06-22 (153.8M net cash). 9M buybacks cash 212.4M.

## Counterthesis
Growth in Data and AI-led includes acquisitions (31% organic vs 36% reported), and the legacy Digital operations line is shrinking; AI-driven automation could cut revenue per task in the BPO base. Debt rose about 217M in 2026 while buybacks consumed 212M, so shareholder returns are partly debt funded. GAAP operating margin 14.0% sits well below adjusted 19.3%; SBC is 93M TTM. Stock is up about 7% since earnings (40.93 on 10-27). Rupee (INR guide 95) and wage inflation are margin risks. Customer concentration: no customer above 10%, a strength.

## Invalidation
Fails if organic Data and AI-led growth decelerates sharply, AI substitution erodes Digital operations faster, margins compress, or leverage from acquisitions and buybacks constrains flexibility.

## Unresolved gaps
- MD&A, Item 4, organic growth in total, acquisition accounting unread
- Peers and own-history multiples not compared
- Quote independence is publisher level only
- Scores not assigned

## Checks
- latest_filing_checked: passed; 10-Q and 8-K filed 2026-10-27 read in part; 8-K 2026-08-18 (credit facility) and 2026-09-02 (Item 5.02) not read.
- balance_sheet_verified: passed; 2026-09-30 cash 154.066M, short-term investments 178.612M, borrowings 511.049M, total liabilities 1,145.321M, total assets 2,073.409M, leases 104.298M; facility split unread.
- cashflow_basis_verified: passed; OCF FY25 350.717M, 9M26 208.804M, 9M25 233.336M; capex 52.598M, 44.125M, 41.727M; capitalized software not separated.
- share_count_basis_verified: passed; 150,788,731 shares at 2026-10-23 cover; buybacks reduce count; dilution not modeled.
- valuation_complete: NOT passed; P/E, adjusted P/E, FCF yield computed; no peer (ACN, GLOB, EPAM, WNS) or history comparison.
- sector_model_appropriate: NOT passed; Needs organic growth by line, attrition, wage and AI-substitution evidence; MD&A unread.
- accounting_red_flags_reviewed: NOT passed; Adjusted vs GAAP gap noted; audit matters, Item 4 and acquisition accounting unread.
- counterthesis_written: passed; Covers acquired growth, shrinking Digital ops, debt-funded buybacks, margin, AI risk.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1297989/000129798926000031/exls-20260930.htm (quarterly_filing, relevant_sections); Q3 2026 10-Q via WebFetch, statements and revenue note; excerpt cut at Note 7, MD&A and Item 4 unread
- r: https://www.sec.gov/Archives/edgar/data/1297989/000129798926000028/exlq326pressrelease.htm (earnings_release, relevant_sections); Earnings release Ex 99.1 via WebFetch (same underlying data as the 10-Q, not independent)
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001297989.json (annual_filing, relevant_sections); SEC XBRL companyfacts by script: FY2025 10-K 0001297989-26-000008, 9M26 and 9M25 matched
- qa: https://stockanalysis.com/stocks/exls/history/ (quote, relevant_sections); stockanalysis.com via WebFetch; close 2026-11-16 (origin undocumented)
- qb: https://finance.yahoo.com/quote/EXLS/history/ (quote, relevant_sections); Yahoo Finance via WebFetch; close 2026-11-16 (origin undocumented)
