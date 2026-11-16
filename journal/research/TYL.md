# TYL (NYSE) research record, run 63

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run63_TYL.json (valid, not attractive-eligible).
As of 2026-11-16T12:07:44-05:00. Close 424.06 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Tyler Technologies (NYSE: TYL), Q3 2026 10-Q (0000860731-26-000058, filed 2026-10-28). Q3 revenue 647.6M vs 595.9M (+8.7%), 9M 1,906.2M vs 1,757.2M (+8.5%); recurring revenue 1,667.0M in 9M (87%); SaaS 695.2M. 9M operating income 311.9M vs 282.7M, NI 269.8M vs 250.1M. TTM (FY2025 + 9M26 - 9M25): revenue 2,481.3M, NI 335.3M, OCF 758.0M, PP&E capex 17.0M, capitalized software 5.8M, FCF 735.2M, SBC 158.7M (FCF after SBC 576.5M). Close 424.06 on 2026-11-13 (stockanalysis, Yahoo agree), 39,759,524 shares (cover 2026-10-26): market cap 16.86B, 50.3x TTM GAAP NI, FCF yield 4.4% (3.4% after SBC); aggregator forward P/E 28.7, EV/EBITDA 37. Balance sheet 2026-09-30: cash 788.2M plus 116.5M investments; 1,410.1M 2031 convertible notes (2026 converts of 600M repaid; capped calls 187.2M); total liabilities 2,855.1M; deferred revenue 864.3M (98% recognized within 12 months). 9M buybacks 1,124.1M cash for about 3.57M shares (about 320 average) exceeded 9M FCF of about 498M, funded by the new converts and cash; shares outstanding fell. Quality high (sticky municipal software), but price already implies steady 8 to 9% growth with margin expansion; the market view may be that AI or procurement shifts threaten vertical software, yet reported growth is steady. Not a bargain on trailing earnings.

## Countercase
50x trailing GAAP earnings and 37x EV/EBITDA leave little margin for slower growth; growth is only 8.5% and partly acquired (9M acquisitions 239.0M, CODY and BFT; prices not read). Buybacks of 1.1B in 9M exceeded free cash flow and were funded by 1.44B converts, raising net debt to about 0.5B and diluting if converts convert; equity fell from 3.70B to 2.79B. SBC 159M TTM is 47% of net income. Government budget or federal funding cuts could slow contract wins. Remaining buyback authorization, convert terms, MD&A, peers and own history not read.

## Invalidation
Thesis fails if organic growth drops below about 6%, SaaS transition margins stall, buybacks continue to exceed FCF with rising leverage, or a large government customer or funding shock appears.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/860731/000086073126000058/tyl-20260930.htm (quarterly_filing, relevant_sections; Q3 2026 10-Q via WebFetch extraction (statements, cash flow, equity, debt notes; MD&A truncated after Note 6))
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0000860731.json (annual_filing, relevant_sections; SEC XBRL companyfacts by curl; FY2025 10-K 0000860731-26-000016 and 10-Q periods matched)
- sub: https://data.sec.gov/submissions/CIK0000860731.json (secondary, relevant_sections; SEC submissions list read 2026-11-16: 10-Q and 8-K 2026-10-28, Form 144 sales 11-13 and 11-16, no later 8-K)
- qa: https://stockanalysis.com/stocks/tyl/statistics/ (quote, relevant_sections; stockanalysis.com via WebFetch; close 2026-11-13 (origin undocumented))
- qb: https://finance.yahoo.com/quote/TYL/history/ (quote, relevant_sections; Yahoo Finance via WebFetch; close 2026-11-13 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-10-28 read in part; submissions list shows no newer 8-K than the 2026-10-28 earnings 8-K (unread) and Form 144 filings 11-13 and 11-16.
- balance_sheet_verified: pass: Cash 788.2M, short and long investments 116.5M, 2031 converts 1,410.1M, total liabilities 2,855.1M, equity 2,790.3M, deferred revenue 864.3M at 2026-09-30. Revolver and covenants not read.
- cashflow_basis_verified: pass: OCF FY25 653.5M, 9M26 514.1M, 9M25 409.7M; PP&E capex 16.0, 12.7, 11.7M; capitalized software 16.8, 3.2, 14.1M (from XBRL PaymentsForSoftware; 10-Q shows 3.2M for 9M26); TTM matched periods.
- share_count_basis_verified: pass: 39,759,524 shares at 2026-10-26 from the cover; aggregator 39.76M agrees.
- valuation_complete: NOT passed: Trailing multiples and FCF yield computed; peers (PTC, MANH, ROP, CSGP) and own history not compared.
- sector_model_appropriate: NOT passed: SaaS revenue mix, deferred revenue, SBC read; ARR or net retention not disclosed; MD&A not read.
- accounting_red_flags_reviewed: NOT passed: SBC, convert and capped call accounting, buyback funding noted; acquisition accounting, audit matters, MD&A not read.
- counterthesis_written: pass: Covers valuation, acquired growth, buybacks above FCF, leverage, SBC, funding risk.

## Calculations
{
 "price": 424.06,
 "shares_outstanding": 39759524,
 "share_basis": "10-Q cover 2026-10-26",
 "market_cap_usd": 16859000000.0,
 "ttm_revenue_musd": 2481.3,
 "ttm_net_income_musd": 335.3,
 "pe_ttm": 50.3,
 "ttm_fcf_musd": 735.2,
 "fcf_yield_pct": 4.4,
 "basis": "TTM = FY2025 + 9M26 - 9M25, USD millions: revenue 2,332.3+1,906.2-1,757.2; NI 315.6+269.8-250.1; OCF 653.5+514.1-409.7 = 758.0; PP&E capex 16.0+12.7-11.7 = 17.0; capitalized software 16.8+3.2-14.1 = 5.8; FCF 735.2"
}

## Unresolved gaps
- MD&A, organic growth, acquisition prices and convert terms not read
- Peers and own-history multiples not compared
- Remaining buyback authorization and revolver unread
- Quote independence is publisher level only
- Scores not assigned
