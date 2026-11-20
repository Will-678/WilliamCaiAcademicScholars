# CBU (NYSE, USD)

Run 85, 2026-11-20T04:07:36-05:00. Status: **watch**. Confidence: medium. Scores: null (incomplete). Fresh idea: yes (annual SEC screen lead, CIK 723188). Validator: data/quality_run85_CBU.json. Benchmark VTI pending; no paper reference.

## Sector model
Regional bank with fee businesses: P/E, price to book and tangible book, ROE, NIM, credit and capital ratios; do not annualize one period as definitive; no free cash flow model.

## Thesis and evidence
Community Financial System (NYSE: CBU), Upstate New York and Pennsylvania community bank with employee benefit services (36.4M of Q3 fee revenue), insurance and wealth management. Q3 2026 10-Q (filed 2026-11-06) read. 9M NI 179.9M vs 156.0M (+15%); Q3 NI 61.3M vs 55.1M; Q3 net interest income 143.5M vs 128.2M (+12%); NIM 3.54% (3.30% a year earlier) for 9M; efficiency ratio 62.0% (operating 59.8%); ROE 11.8%, ROA 1.37% (9M, annualized by the company); noninterest revenue 246.3M (+7%). Credit: allowance 92.0M = 0.80% of loans of 11.52B; ACL/nonperforming loans 152%; nonaccrual 0.43% of loans; Q3 net charge-offs 0.18% annualized (5.1M, including 2.7M on two business relationships); 65% of nonperforming loans are consumer mortgages. Capital: CET1 13.73%, leverage 9.37% (company), well capitalized; but AOCI loss of 484.2M on 2.56B AFS securities (unrealized loss 619.6M pretax on securities) equals about 24% of equity and is excluded from regulatory CET1, so tangible book 21.17 per share (1,108.7M / 52.377M shares) includes it. TTM NI (USD M) = FY2025 210.455 + 9M26 179.856 - 9M25 156.033 = 234.3. Close 62.45 (2026-11-19) x 52,377K period end shares = 3.27B = 14.0x TTM NI; 1.61x book (38.77) and 2.95x tangible book (21.17); dividend 0.49 per quarter = 3.1% yield, Q3 payout about 41%. Deposits 14.87B (noninterest bearing 3.89B, 26%), borrowings 0.64B, loans to deposits 77%. Possible market view: slow growth Northeast bank with large unrealized securities losses. Differing evidence: ROE near 12% with improving NIM, 15% earnings growth, strong capital, 37% fee income, tangible book stable (20.57 a year ago to 21.17). Price implies about 14x TTM and 12.6x annualized 9M (own arithmetic, not a forecast). Stock fell from 64.26 on 11-16 to 62.45 (-2.8%).

## Countercase
Net charge-offs doubled year over year to 0.18% and business lending charge-offs rose to 0.23%; commercial real estate exposure was not examined here. AOCI losses of 484M show rate sensitivity: a fall in long yields helps tangible book, a rise hurts it; 4.05B of securities is 23% of assets. Fee income depends on employee benefit services which is competitive. Goodwill and intangibles 967M are 48% of equity, leaving tangible common equity at 6.2% of assets (1,108.7M / 17.79B, own arithmetic) and the Bank level CET1 (11.73%) is below the holding company's. Acquisitions (intangibles rose 25M in 9M) carry integration risk; amortization of intangibles 13.0M in 9M. NIM expansion of 24 bp may not persist if deposit costs rise; Q3 included a 2.9M securities loss. Peers (WSFS, Tompkins, NBTB, FNB) and own history not compared; 10-K audit matters not read.

## Invalidation
Invalidated if nonperforming loans or charge-offs rise sharply (especially commercial real estate or business lending), if NIM reverses below about 3.2%, if long rates rise enough to widen the AOCI loss and force capital raising or buyback cuts, or if a large acquisition dilutes tangible book without return.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/723188/000110465926123882/cbu-20260930x10q.htm (quarterly_filing, relevant_sections): 10-Q quarter ended 2026-09-30 filed 2026-11-06; downloaded and converted to text; balance sheet, income statement, credit quality summary, regulatory capital table and non-GAAP reconciliation section read; commercial real estate detail, deposits detail and risk factors not fully read
- x: https://data.sec.gov/api/xbrl/companyfacts/CIK0000723188.json (annual_filing, relevant_sections): SEC XBRL company facts: FY2025 NI 210.455M (10-K accession 0001104659-26-021651)
- sub: https://data.sec.gov/submissions/CIK0000723188.json (secondary, relevant_sections): SEC submissions list: 10-Q 2026-11-06; 8-K 2026-10-27 (earnings, not read); later items Form 4 and 144 only
- qa: https://stockanalysis.com/stocks/cbu/history/ (quote, relevant_sections): stockanalysis.com via WebFetch; close 2026-11-19 4:00 PM EST (origin undocumented)
- qb: https://finance.yahoo.com/quote/CBU/history/ (quote, relevant_sections): Yahoo Finance via WebFetch; regular close Nov 19 (origin undocumented)

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-06 is the latest periodic filing; the 2026-10-27 earnings 8-K exhibit was not read, but the 10-Q reports the same results.
- balance_sheet_verified: pass: At 2026-09-30 (USD thousands): total assets 17,787,973; loans 11,518,055; allowance 92,020; deposits 14,865,106; borrowings 636,009 (repo 215,037 + FHLB and other 420,972); total liabilities 15,757,388; equity 2,030,585; goodwill and intangibles 967,421.
- cashflow_basis_verified: pass: Bank model: free cash flow not used. NI periods matched: FY2025 210.455M + 9M26 179.856M - 9M25 156.033M = 234.278M.
- share_count_basis_verified: pass: Period end common shares outstanding 52,377K at 2026-09-30 from the 10-Q book value reconciliation (book value 38.77 = 2,030,585K / 52,377K).
- valuation_complete: OPEN: P/E, P/B, P/TBV and yield computed; peers and own history not compared; Q3 annualization not used as a definitive valuation.
- sector_model_appropriate: pass: Bank model: NIM, ACL coverage, nonperforming loans, CET1 and tangible book, not generic FCF or liabilities ratios.
- accounting_red_flags_reviewed: OPEN: AOCI, allowance, CET1 and goodwill read; CRE concentration, 10-K audit matters (allowance judgment), deposit mix and risk factors not read.
- counterthesis_written: pass: Covers charge-offs, AOCI rate risk, intangibles heavy equity, NIM durability, acquisitions.

## Unresolved gaps
- Peers (WSFS, TOMK, NBTB, FNB) and own history not compared
- CRE concentration, deposit mix and 10-K audit matters not read
- 2026-10-27 earnings exhibit and guidance not read
- Quote origins undocumented (two aggregators)
