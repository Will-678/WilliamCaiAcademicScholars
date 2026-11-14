# MRVL (Nasdaq) research record, run 48

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run48_MRVL.json (valid, not attractive-eligible).
As of 2026-11-14T05:05:19+00:00. Close 156.76 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Marvell Technology (Nasdaq: MRVL), custom AI silicon and data-center connectivity, large cap. FY27 Q2 (to 2026-08-01, 10-Q filed 2026-08-28): revenue 2.739B (+36.5%), GAAP net income 308M (EPS 0.33), cash 3.93B, debt principal 5.00B (no maturities before FY2029; 1.5B revolver undrawn), 876.9M shares. TTM (FY26 10-K + 6M FY27 - 6M FY26): revenue 9.45B, GAAP NI 2.64B (EPS 3.02, includes a large FY26 Q3 profit of 1.90B that I did not trace to a cause), OCF 2.20B, capex 0.47B, FCF 1.73B. At 156.76 (2026-11-13 close, -4.7% on the day, 52-week 70.69-329.88, about 52% below the high) market cap is about 137.6B: 52x TTM GAAP EPS, FCF yield 1.26% (0.65% after 0.83B SBC). The new fact is the all-stock deal to buy Lumentum announced 2026-11-02 (agreement 2026-11-01): 4.500 Marvell shares per Lumentum share, about 115B enterprise value (about 1,132 per share, 23.9% premium to 10-28), Marvell holders to own about 67% of the combined company, expected close first half 2028, outside date 2027-11-01 extendable to 2028-08-01. Marvell would issue roughly 430M shares (about 49% more than today's count; my estimate from the 67/33 split) and pays 5.8B if its board withdraws support, 3.2B regulatory break fee. Stock moved from 171.97 (11-03) to 133.55 (11-05) and 168.80 (11-11). So a growing AI hardware supplier is priced on forward earnings (forward P/E 27.8x per stockanalysis, unverified) while trailing cash yield is thin and the standalone company is about to become a different, larger, less visible one.

## Countercase
Trailing cash yield 1.3% (0.7% after SBC) and 52x GAAP EPS leave no cushion if AI capex slows. The deal is a very large, stock-funded bet: about 49% dilution, 5.8B/3.2B termination exposure, regulatory risk (HSR, China is 42% of revenue by destination so approvals elsewhere may matter), integration of a different business, a 1.5 to 2 year wait with deal uncertainty, and Marvell's own shares are the currency, so a falling share price changes what Lumentum holders receive in value terms. Barron's items cited on stockanalysis tie the recent drop to dilution and merger doubts and a separate report about Nvidia's CEO; I did not verify them. I have not read Lumentum financials, so I cannot judge what is being bought. Customer concentration, custom silicon dependence on a few hyperscalers, and the FY26 one-off profit are unresolved.

## What would change the view
Evidence for the thesis fails if revenue growth falls well below 20% for two quarters, FCF stays under about 2% of market value while capex rises, or the Lumentum deal terms or approval risk turn out worse than the stock price implies; deal termination would reset the case.

## Checks
- latest_filing_checked: passed. 10-Q 2026-08-28 is latest periodic filing; 8-Ks of 11-02 and 11-12 and the 425 stream checked through submissions; Q3 FY27 report is not due until about late Nov (unverified date).
- balance_sheet_verified: passed. Cash 3,932.8M, debt face 4,999.9M (net 4,962.9M), maturities FY2029 1,249.9M, 2030 500M, 2031 500M, thereafter 2,750M, revolver 1.5B undrawn at 2026-08-01; last 1,272 characters of the 10-Q unread.
- cashflow_basis_verified: passed. TTM OCF and reported PP&E capex from matching FY26 10-K and 10-Q periods; SBC separate; capitalized software and acquisition spending not included.
- share_count_basis_verified: passed. 876.9M cover shares at 2026-08-21 vs 877.99M on stockanalysis; point-in-time count used; Lumentum deal would add roughly 430M (estimate from the 67/33 split).
- valuation_complete: NOT passed. Trailing P/E and FCF yield computed; forward P/E from one aggregator; no peer (AVGO, NVDA, CRDO, ALAB) multiples; pro forma combined valuation not possible without Lumentum figures.
- sector_model_appropriate: passed. Fabless semiconductor: growth, margins, FCF after SBC, net debt, customer concentration; bank ratios not applicable.
- accounting_red_flags_reviewed: NOT passed. FY26 Q3 profit of 1.90B unexplained, acquisitions/divestiture effects, purchased intangibles and customer concentration not traced; 10-K risk factors not read.
- counterthesis_written: passed. Covers valuation, dilution, termination fees, regulatory and AI-cycle risks.

## Unresolved gaps
- Lumentum financials, deal accretion and pro forma leverage unread
- Peer multiples and own history not done
- FY26 Q3 1.90B profit not traced; 10-K risk factors unread
- Quotes: two publishers, publisher-level independence only
- Scores not assigned

## Sources
- q1: https://www.sec.gov/Archives/edgar/data/1835632/000183563226000025/mrvl-20260801.htm (quarterly_filing, relevant_sections) 10-Q quarter ended 2026-08-01 filed 2026-08-28 via WebFetch; first 100,000 of 101,272 characters read
- a1: https://www.sec.gov/Archives/edgar/data/1835632/000119312526442717/d352474d8k.htm (secondary, relevant_sections) 8-K item 1.01 filed 2026-11-02 (merger agreement with Lumentum) via WebFetch
- a2: https://www.sec.gov/Archives/edgar/data/1835632/000119312526442714/d81187d8k.htm (secondary, relevant_sections) 8-K items 2.02/7.01 filed 2026-11-02; exhibits (press release, preliminary Q3 revenue) not read
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001835632.json (annual_filing, relevant_sections) SEC XBRL companyfacts: FY2026 10-K (filed 2026-03-11) revenue 8.1946B, NI 2.6701B, OCF 1.7505B, capex 0.3541B, SBC 0.5908B, plus 10-Q YTD figures
- sub: https://data.sec.gov/submissions/CIK0001835632.json (secondary, relevant_sections) SEC submissions JSON 2026-11-14: latest 10-Q 2026-08-28; 8-Ks 11-02 and 11-12; many 425 filings; Forms 3 on 11-13
- d1: https://benton.org/node/361537 (secondary, relevant_sections) Republished Marvell/Lumentum deal press release via WebFetch: 4.500 exchange ratio, about 115B EV, about 1,132 per Lumentum share, 23.9% premium, 67%/33% ownership
- qa: https://stockanalysis.com/stocks/mrvl/ (quote, relevant_sections) stockanalysis.com via WebFetch: close 156.76 at 4:00 PM EST 2026-11-13, 877.99M shares, market cap 137.63B, 52-week 70.69-329.88
- qb: https://finance.yahoo.com/quote/MRVL/history/ (quote, relevant_sections) Yahoo Finance via WebFetch: close 156.76 on 2026-11-13; 164.45 on 11-12; 168.80 on 11-11; 171.41 on 11-02
