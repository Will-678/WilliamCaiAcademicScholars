# BMY (NYSE) research record, run 63

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run63_BMY.json (valid, not attractive-eligible).
As of 2026-11-16T12:07:44-05:00. Close 63.43 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Bristol-Myers Squibb (NYSE: BMY), Q3 2026 10-Q (0000014272-26-000024, filed 2026-10-29). Q3 revenue 13,069M vs 12,222M (+6.9%), 9M 37,532M vs 35,692M (+5.2%). Growth Portfolio 9M 21,448M +12.8% (Camzyos +60.9%, Reblozyl +22.8%, Breyanzi +47.2%, Cobenfy 176M); Legacy 16,114M -3.4% (Revlimid -54.2%, Pomalyst -58.5%, Opdivo -4.8%, Eliquis +21.1%). 9M GAAP NI 8,156M vs 5,967M (tax rate 17.3% vs 24.0%; amortization of intangibles 1,332M vs 2,491M; acquired IPRD 1,651M vs 2,328M). TTM (FY2025 + 9M26 - 9M25): revenue 50,034M, NI 9,243M, OCF 10,652M, capex 1,366M, FCF 9,286M, SBC 552M (FCF after SBC 8,734M). 9M OCF fell to 8,678M from 12,182M, largely a rebates and discounts swing of (3,869)M vs +1,957M. Close 63.43 on 2026-11-13 (stockanalysis, Yahoo agree), 2,044,085,831 shares (cover 2026-10-21): market cap 129.7B, 14.0x TTM GAAP NI, FCF yield 7.2% (6.7% after SBC); aggregator forward P/E 9.8, EV/EBITDA 8.9, dividend yield 4.0%. TTM dividends 5,119M (FCF covers 1.8x). Cash 9,574M plus marketable securities 3,385M; short-term debt 1,028M, long-term debt 41,849M, net debt about 29.9B; total liabilities 65,368M, equity 23,404M. The market likely prices the 2028 era Eliquis and Opdivo exclusivity losses and Revlimid and Pomalyst erosion; evidence that differs is Growth Portfolio compounding at 13% and falling debt (long-term debt 44.8B to 42.6B including current in 9M). Cheap on forward earnings, but forward earnings and Eliquis strength are the key unverified inputs.

## Countercase
Eliquis (13.3B in 9M, 35% of revenue) and Opdivo face loss of exclusivity around 2028 (not verified from the 10-Q; MD&A truncated) and Medicare price negotiation; Eliquis +25% in Q3 needs an explanation (not read). Legacy erosion of Revlimid and Pomalyst is steep. GAAP earnings are flattered by lower amortization and a low tax rate (14.8% in Q3), and IPRD charges of 1.6B in Q3 (600M Hengrui, 500M BioNTech) recur with deals. Net debt 29.9B; 9M OCF fell 29% on rebates. Pipeline setbacks, impairments (834M in 9M) and IRS transfer pricing appeals (2008 to 2012) are risks. Guidance, IRA, LOE dates, peers and non-GAAP reconciliation not read.

## Invalidation
Thesis fails if Eliquis or Opdivo erosion arrives early, Growth Portfolio growth falls below about 8%, OCF stays below 10B with dividends rising, or pipeline write-offs and IPRD charges keep absorbing cash.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/14272/000001427226000024/bmy-20260930.htm (quarterly_filing, relevant_sections; Q3 2026 10-Q via WebFetch extraction (statements, product table, cash flow, debt; MD&A, Note 18 and guidance truncated))
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0000014272.json (annual_filing, relevant_sections; SEC XBRL companyfacts by curl; FY2025 10-K 0000014272-26-000004 and 10-Q periods matched)
- sub: https://data.sec.gov/submissions/CIK0000014272.json (secondary, relevant_sections; SEC submissions list read 2026-11-16: 10-Q and 8-K (2.02, 7.01) 2026-10-29, no later 8-K seen)
- qa: https://stockanalysis.com/stocks/bmy/statistics/ (quote, relevant_sections; stockanalysis.com via WebFetch; close 2026-11-13 (origin undocumented))
- qb: https://finance.yahoo.com/quote/BMY/history/ (quote, relevant_sections; Yahoo Finance via WebFetch; close 2026-11-13 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-10-29 read in part; earnings 8-K 2026-10-29 unread; no later 8-K in the submissions list.
- balance_sheet_verified: pass: Cash 9,574M, marketable securities 3,007M current and 378M non-current, short-term debt 1,028M, long-term debt 41,849M, total liabilities 65,368M, equity 23,404M at 2026-09-30.
- cashflow_basis_verified: pass: OCF FY25 14,156M, 9M26 8,678M, 9M25 12,182M; capex 1,311M, 996M, 941M; dividends 5,045M, 3,857M, 3,783M; TTM matched periods.
- share_count_basis_verified: pass: 2,044,085,831 shares at 2026-10-21 from the cover; aggregator 2.04B agrees.
- valuation_complete: NOT passed: Trailing multiples and FCF yield computed; forward EPS is an aggregator figure only; peers (MRK, PFE, ABBV, LLY) and own history not compared.
- sector_model_appropriate: NOT passed: Product table, IPRD and amortization read; LOE schedule, IRA, pipeline and guidance not read because MD&A is truncated.
- accounting_red_flags_reviewed: NOT passed: Low tax rate, lower amortization, IPRD charges, impairments 834M, rebate swing noted; Note 18, tax appeals, non-GAAP not read.
- counterthesis_written: pass: Covers LOE, Legacy erosion, flattered GAAP, net debt, IPRD, OCF drop.

## Calculations
{
 "price": 63.43,
 "shares_outstanding": 2044085831,
 "share_basis": "10-Q cover 2026-10-21",
 "market_cap_usd": 129661000000.0,
 "ttm_revenue_musd": 50034,
 "ttm_net_income_musd": 9243,
 "pe_ttm": 14.0,
 "ttm_fcf_musd": 9286,
 "fcf_yield_pct": 7.2,
 "basis": "TTM = FY2025 + 9M26 - 9M25, USD millions: revenue 48,194+37,532-35,692; NI 7,054+8,156-5,967; OCF 14,156+8,678-12,182 = 10,652; capex 1,311+996-941 = 1,366; FCF 9,286"
}

## Unresolved gaps
- MD&A, LOE dates, IRA effect, guidance and Eliquis Q3 driver not read
- Peers and own-history multiples not compared
- Forward EPS is an aggregator figure only
- Quote independence is publisher level only
- Scores not assigned
