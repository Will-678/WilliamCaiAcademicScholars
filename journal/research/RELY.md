# RELY (Nasdaq, USD)

Run 85, 2026-11-20T04:07:36-05:00. Status: **watch**. Confidence: medium. Scores: null (incomplete). Fresh idea: yes (annual SEC screen lead, CIK 1782170). Validator: data/quality_run85_RELY.json. Benchmark VTI pending; no paper reference.

## Sector model
Cross-border payments platform: P/E (distorted by tax benefit), 9M FCF after SBC, send volume and active customer growth, customer funds and prefunding liquidity; customer funds are not owned cash.

## Thesis and evidence
Remitly Global (Nasdaq: RELY), digital remittances. Q3 2026 10-Q (filed 2026-11-04) and Ex 99.1 read. Q3 revenue 509.8M vs 419.5M (+22%), 9M revenue 1,457.8M vs 1,193.0M (+22%); send volume Q3 24.4B (+25%), 9M 70.0B (+29%); active customers 10.34M vs 8.86M (+17%); 9M income from operations 189.8M vs 38.7M; 9M net income 322.5M vs 26.7M but includes a 136.0M tax benefit from releasing the US deferred tax valuation allowance (9M pre-tax income 186.5M; at an assumed 21% rate normalized 9M NI would be about 147M, own estimate). Guidance (Ex 99.1): FY2026 revenue 1.989 to 1.991B (+22%), Adjusted EBITDA 441 to 443M; Q4 revenue 531 to 533M (+20% to +21%), Adjusted EBITDA 104 to 106M (non-GAAP, not reconciled by the company). TTM NI (USD M) = FY2025 67.9 + 9M26 322.5 - 9M25 26.7 = 363.7. Close 20.06 (2026-11-19) x 214,012,570 shares (10-Q cover, 2026-11-02) = 4.29B = 11.8x TTM NI (inflated by the one time tax benefit; normalized, about 22x annualized 9M at an assumed 21% tax rate: own rough arithmetic, not a TTM figure). 9M FCF (OCF 309.5 less PP&E 8.5 less capitalized software 10.4) = 290.6M = 6.8% of market cap (9M, not annualized); after 9M SBC 101.7M = 189.0M (4.4%). TTM FCF is not computed: 2025 cash flow was reclassified (customer funds moved from operating to financing, 49.7M in 9M25) so the FY2025 10-K OCF 325.1M is on an older basis. Balance sheet 2026-09-30: cash 669.1M, disbursement prefunding 287.4M, customer funds receivable 357.1M, customer liabilities 213.3M, debt 2.9M short term and none long term (155M repaid), revolver upsized to 1.0B on 2026-10-26 (10-30 8-K), total liabilities 426.9M, equity 1,226.4M. Buyback: 4.5M shares for 80.0M in 9M, authorization raised to 500M (96.1M left at 9-30 before the raise). Possible market view: remittance is a low moat, price competitive, immigration policy sensitive business and the earnings jump is accounting. Differing evidence: 29% volume growth, customers +17%, operating margin 13.0% in 9M vs 3.2%, essentially no debt, buyback. Stock fell about 8% in the four sessions to 11-19 (21.93 on 11-16 to 20.06; cause not investigated). What could close the gap: continued 20% growth with rising GAAP operating margin.

## Countercase
Remittances are exposed to US immigration enforcement, remittance taxes and corridor concentration (India, Mexico, Philippines); marketing 294.7M in 9M (20% of revenue) is the growth engine and customer acquisition cost can rise. Competitors (Wise, Western Union, Intermex, banks, stablecoin rails) can compress take rates; revenue grows slower than send volume (+22% vs +29% in 9M), implying a falling take rate. SBC 101.7M is 7% of 9M revenue and diluted shares are 220.5M vs 214.0M outstanding. The headline net income is flattered by a 136M valuation allowance release. Customer funds and prefunding (about 644M of receivables and prefunding versus 213M customer liabilities) depend on revolver and bank partners; operational or regulatory problems with money transmission licenses could be severe. Adjusted EBITDA guidance is non-GAAP and unreconciled. Peers and history not compared; legal and risk factors not read.

## Invalidation
Invalidated if send volume growth slows below about 15% while marketing stays near 20% of revenue, if take rate compression outpaces operating leverage, if regulatory action or a remittance tax materially cuts volume, or if GAAP operating income falls back toward 2025 levels.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1782170/000162828026070142/rely-20260930.htm (quarterly_filing, relevant_sections): 10-Q quarter ended 2026-09-30 filed 2026-11-04; downloaded and converted to text; balance sheet, operations, cash flow, debt, repurchase, tax and MD&A KPI sections read; legal, risk factors and segment/geography tables not fully read
- r: https://www.sec.gov/Archives/edgar/data/1782170/000162828026070130/rely3q26-earningspr.htm (earnings_release, relevant_sections): Issuer earnings release Ex 99.1 of 8-K filed 2026-11-04 (same underlying results as the 10-Q; guidance read; non-GAAP tables not read)
- x: https://data.sec.gov/api/xbrl/companyfacts/CIK0001782170.json (annual_filing, relevant_sections): SEC XBRL company facts: FY2025 NI 67.933M, OCF 325.082M (older cash flow presentation), PP&E capex 29.431M, SBC 155.114M (10-K filed 2026-02-18)
- sub: https://data.sec.gov/submissions/CIK0001782170.json (secondary, relevant_sections): SEC submissions list: 10-Q and 8-K (Items 2.02, 7.01) 2026-11-04; 8-K 2026-10-30 (Items 1.01, 2.03) read in full; nothing newer than Form 4 and 144 filings through 2026-11-12
- qa: https://stockanalysis.com/stocks/rely/history/ (quote, relevant_sections): stockanalysis.com via WebFetch; close 2026-11-19 4:00 PM EST (origin undocumented)
- qb: https://finance.yahoo.com/quote/RELY/history/ (quote, relevant_sections): Yahoo Finance via WebFetch; regular close Nov 19 (origin undocumented)

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-04 is the latest periodic filing; earnings 8-K same day; credit facility 8-K 2026-10-30 read; later SEC items are insider Form 4 and Form 144 only.
- balance_sheet_verified: pass: At 2026-09-30 (USD thousands): cash 669,082; prefunding 287,434; customer funds receivable 357,108; customer liabilities 213,292; short term debt 2,938; long term debt 0; total liabilities 426,892; equity 1,226,414; total assets 1,653,306.
- cashflow_basis_verified: pass: 9M26 OCF 309,526K, PP&E 8,542K, capitalized software 10,393K (FCF 290.6M); 9M25 OCF 225,172K on the reclassified basis. FY2025 OCF 325.1M is on the pre reclassification basis, so a TTM FCF was deliberately not computed.
- share_count_basis_verified: pass: 214,012,570 shares at 2026-11-02 from 10-Q cover; 214,013K at 2026-09-30 on the balance sheet; weighted diluted 9M 220,540K.
- valuation_complete: OPEN: Market cap, P/E and 9M FCF yield computed; normalized TTM earnings, peers (WU, Wise, IMXI) and own history not compared.
- sector_model_appropriate: pass: Payments/remittance model with customer funds excluded from owned cash; not a bank, insurer or REIT.
- accounting_red_flags_reviewed: OPEN: Valuation allowance release, cash flow reclassification, SBC and debt read; 10-K audit matters, transaction loss reserves, legal proceedings and risk factors not read.
- counterthesis_written: pass: Covers regulation, take rate, marketing intensity, SBC, tax distortion, customer funds, competition.

## Unresolved gaps
- Peers (Wise, Western Union, Intermex) and own history not compared
- Normalized earnings and TTM FCF on a consistent basis not computed
- 10-K audit matters, legal proceedings and risk factors (immigration, remittance tax) not read
- Cause of 8% decline 11-16 to 11-19 not investigated
- Quote origins undocumented (two aggregators)
