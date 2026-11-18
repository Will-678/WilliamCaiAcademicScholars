# UCB (NYSE) research record, run 76

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run76_UCB.json.
As of 2026-11-18T16:08:21-05:00. Close 36.56 USD on 2026-11-18 (stockanalysis.com and Yahoo Finance agree within 0.1%; underlying origin undocumented, fetched after the 4 p.m. ET close). Benchmark VTI pending; no paper reference.

## Sector model
Regional bank (mid): value on price to tangible book, operating earnings and ROTCE, credit quality, capital and funding; GAAP earnings distorted by one-time balance sheet repositioning; no FCF.

## Thesis and evidence
United Community Banks (NYSE: UCB). Q3 2026 earnings release (8-K Ex 99.1 filed 2026-10-20) read in full for the figures cited; the 10-Q filed 2026-11-04 returned only XBRL header text, so its narrative is unread. Q3 GAAP net loss 139.7M (EPS -1.16) from a 366.1M pre-tax securities repositioning loss (2.5B amortized cost of long-dated securities sold for 2.1B; proceeds and 2.0B Navitas sale cash redeployed into higher-yielding securities and used to repay borrowings), partly offset by a 62.2M gain on the Navitas Credit sale (closed 2026-09-01 at a 7% premium to par, about 1.8 to 1.9B of equipment finance loans left the books), 6.5M merger charges and a 76.9M tax effect. Operating net income 93.7M (EPS 0.77; Q3 2025 94.2M, 0.75), ROTCE operating 13.9%, NIM 3.68%, efficiency 53.1%; 9M operating net income 264.8M, GAAP 60.2M. Peach State Bancshares closed 2026-08-01 (520M loans, 678M deposits). Balance sheet: assets 28.88B, loans 18.99B, deposits 24.89B, equity 3.51B, BVPS 29.27, TBVPS 20.80; NPAs 81.3M (0.28% of assets), annualized net charge-offs 0.09%, ACL 1.05%, CET1 13.0% preliminary; debt fell to 39.7M long-term and no short-term borrowings. Price: close 36.56 on 2026-11-18 x 119,827,028 shares = 4,381M = 1.25x book, 1.76x tangible book, dividend yield 2.8% (1.02 annualized), about 12.4x 9M operating earnings scaled by 4/3 (approximation, not TTM). Buyback 50M in Q3 at 35.81 average, new 100M authorization. The market is pricing a healthy southeastern bank at a modest premium to tangible book; the repositioning should lift future net interest income but the earnings benefit is management's expectation, not shown in reported results.

## Counterthesis
The headline GAAP loss is from a deliberate 366M securities loss; tangible book was reduced and the payback depends on rates and reinvestment yield that are not quantified in the release. Operating earnings exclude that loss, merger charges and the Navitas gain, which management chooses. Selling Navitas removes a high-yield equipment finance business with its earnings. Credit looks clean now (NPAs 0.28%) but the cycle is untested and the 10-Q credit and CRE concentration text is unread. Pro forma earnings, deposit beta and the Peach State deal terms were not read.

## Invalidation
Invalidated if operating ROTCE falls below about 11%, NIM does not rise after the repositioning, NPAs exceed about 0.8% of assets, CET1 falls below 11%, or deposit costs rise faster than asset yields.

## Unresolved gaps
- 10-Q narrative unread (credit, CRE concentration, securities, capital detail)
- Peers and own history not compared; TTM operating earnings unavailable
- Earnings power after repositioning and Navitas sale not quantified
- Quote origins undocumented (publisher level only)

## Checks
- latest_filing_checked: pass. Submissions list shows 10-Q 2026-11-04 and earnings 8-K 2026-10-20; the release was read, the 10-Q narrative was not.
- balance_sheet_verified: pass. Assets 28,882.0M, deposits 24,887.9M, equity 3,507.3M at 2026-09-30 (USD), release and XBRL agree.
- cashflow_basis_verified: not passed. Not applicable to bank valuation; earnings basis used instead (GAAP TTM 146.6M and 9M operating 264.8M); cash flow statement unread.
- share_count_basis_verified: pass. 119,827,028 shares at 2026-09-30 from the release; point in time; 10-Q cover share count not read.
- valuation_complete: not passed. P/B, P/TBV, yield and approximate operating multiple computed; peers (Synovus, Pinnacle, Ameris, Cadence), history and TTM operating earnings not compared.
- sector_model_appropriate: pass. Bank model on tangible book, operating earnings, credit and capital.
- accounting_red_flags_reviewed: not passed. Held-to-maturity reclassification, 366M loss and operating adjustments noted; 10-Q notes, CRE mix and fair value disclosures unread.
- counterthesis_written: pass. Covers repositioning loss, adjusted earnings, Navitas loss of earnings, untested credit.

## Sources
- er: https://www.sec.gov/Archives/edgar/data/857855/000110465926117113/tm2627820d1_ex99-1.htm (earnings_release, relevant_sections)
- q: https://www.sec.gov/Archives/edgar/data/857855/000085785526000092/ucbi-20260930.htm (quarterly_filing, snippet)
- x: https://data.sec.gov/api/xbrl/companyfacts/CIK0000857855.json (annual_filing, relevant_sections)
- sub: https://data.sec.gov/submissions/CIK0000857855.json (secondary, relevant_sections)
- qa: https://stockanalysis.com/stocks/ucb/history/ (quote, relevant_sections)
- qb: https://finance.yahoo.com/quote/UCB/history/ (quote, relevant_sections)
