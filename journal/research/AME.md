# AME (NYSE) research record, run 65

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run65_AME.json.
As of 2026-11-16T20:07:48-05:00. Close 235.75 USD on 2026-11-16 (stockanalysis.com table and Yahoo Finance page header agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Sector model
Diversified industrial instrumentation and electromechanical (large cap): organic growth, margins, FCF conversion, acquisition leverage and goodwill; not a generic liabilities screen.

## Thesis and evidence
AMETEK (NYSE: AME), Q3 2026 10-Q (0001037868-26-000196, filed 2026-11-03; financial statements and notes read, MD&A not in extraction) and earnings release Ex 99.1 (8-K 0001037868-26-000194). Q3 sales 2,220.3M vs 1,892.6M (+17.3%), 9M 6,193.1M vs 5,402.7M (+14.6%); GAAP NI 9M 1,232.6M vs 1,081.5M, GAAP diluted EPS 9M 5.36 vs 4.67; Q3 operating margin 26.3% GAAP, 26.8% adjusted (+60 bps); Q3 OCF 560.6M (+27%), FCF 527.4M (124% of NI). FY2026 guidance raised: GAAP EPS 7.29 to 7.33, adjusted EPS 8.53 to 8.57 (prior 8.20 to 8.30), sales growth mid-teens, Q4 sales growth low 20% range. TTM (FY2025 + 9M26 - 9M25): revenue 8,191.6M, NI 1,631.2M, OCF 2,080.1M, capex 147.7M, FCF 1,932.4M, SBC 50.2M. Close 235.75 on 2026-11-16 and 229,317,998 shares (cover 2026-10-29): market cap 54,060M = 33.1x TTM GAAP NI, FCF yield 3.57% (3.48% after SBC). Indicor Instrumentation bought 2026-08-26 for 5,154.1M (cash 4,921.4M; about 1.1B annual sales; goodwill 2,698.5M, intangibles 2,454.1M, preliminary), funded by 4.0B term loans and revolver (975.7M outstanding). Sept 30 balance sheet: cash 666.2M, debt 6,669.4M (639.8M short-term), net debt 6,003.2M, equity 11,696.2M, goodwill 10,210.7M (7,170.8M at year end). Why the market may pay 33x: consistent compounding, high margins, bolt-on acquisition record; the evidence that supports it is the beat and raise, 124% FCF conversion, and 11% pro forma 9M growth including acquisitions. What it assumes: continued mid-to-high single digit organic growth plus accretive deals at low leverage.

## Countercase
The price already assumes sustained quality: 33x GAAP earnings and a 3.5% FCF yield leave little margin for error. Reported growth of 17% includes the 5.2B Indicor deal; the 10-Q gives only pro forma growth of about 8% in Q3 and 11% in 9M (including acquisitions), and the release does not quantify organic growth or orders, so underlying growth is unverified. Net debt rose to about 6.0B (about 3.2x TTM OCF) and Q3 interest expense is 39.8M vs 22.5M; purchase accounting is preliminary and goodwill (2,698.5M) plus intangibles (2,454.1M) account for essentially the whole 5.15B Indicor price; total goodwill is 10.2B against 11.7B equity. Buybacks were cut to 28.2M in 9M26 from 163.6M. Notes offerings in USD, EUR and CAD (three 424B5 filings 2026-11-12 and three FWPs 2026-11-16, sizes not read) are meant to repay the term loans and commercial paper, so refinancing cost is live. Cyclical exposure (electronics, aerospace, process) and tariff or FX effects were not read. Peers (e.g. ROP, FTV, ITW) and own-history multiples were not compared.

## Invalidation
Thesis fails if organic growth (once disclosed) is flat to negative, FCF conversion drops below about 100% of net income, net leverage stays above roughly 3x EBITDA without deleveraging, or Indicor underperforms its purchase price (goodwill impairment).

## Sources
- q: quarterly_filing, relevant_sections: https://www.sec.gov/Archives/edgar/data/1037868/000103786826000196/ame-20260930.htm (Q3 2026 10-Q via WebFetch extraction (statements, acquisition note, debt; MD&A not in extraction))
- er: earnings_release, relevant_sections: https://www.sec.gov/Archives/edgar/data/1037868/000103786826000194/ametek8kexhibit99111032026.htm (Earnings release Ex 99.1 to 8-K filed 2026-11-03 via WebFetch (same underlying document as the issuer IR release))
- fy: annual_filing, relevant_sections: https://data.sec.gov/api/xbrl/companyfacts/CIK0001037868.json (SEC XBRL companyfacts by script; FY2025 10-K 0001037868-26-000016 and 10-Q periods matched)
- ob: secondary, relevant_sections: https://www.sec.gov/Archives/edgar/data/1037868/000110465926125615/tm2629569-2_424b5.htm (424B5 (CAD notes prospectus supplement, filed 2026-11-12) first 100,000 characters via WebFetch; used for Indicor price, debt and use of proceeds)
- sub: secondary, relevant_sections: https://data.sec.gov/submissions/CIK0001037868.json (SEC submissions list read 2026-11-16: 10-Q 2026-11-03, 8-K 2026-11-06 (unread), FWP and 424B5 2026-11-12 to 2026-11-16)
- qa: quote, relevant_sections: https://stockanalysis.com/stocks/ame/history/ (stockanalysis.com via WebFetch; close 2026-11-16 (origin undocumented))
- qb: quote, relevant_sections: https://finance.yahoo.com/quote/AME/history/ (Yahoo Finance via WebFetch page header close 2026-11-16 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-03 read in part; submissions list shows 8-K 2026-11-06 (unread) and debt offering documents 11-10 to 11-16; no newer periodic filing.
- balance_sheet_verified: pass: At 2026-09-30: cash 666,152K, total debt 6,669,388K (short-term and current 639.8M, long-term 6,029.6M), net debt 6,003,236K, equity 11,696,208K, goodwill 10,210.7M; the 424B5 and 10-Q agree on debt and cash.
- cashflow_basis_verified: pass: OCF FY25 1,801.763M, 9M26 1,495.857M, 9M25 1,217.499M; capex 130.248M, 90.722M, 73.251M; SBC 47.767M, 37.674M, 35.229M; TTM matched; capex is PP&E purchases as reported.
- share_count_basis_verified: pass: 229,317,998 shares at 2026-10-29 from the cover; market cap uses point-in-time shares.
- valuation_complete: NOT passed: Trailing P/E and FCF yield computed; adjusted P/E 27.6x on guided 8.55 midpoint is a derived figure; peers, own history and EBITDA-based leverage not compared.
- sector_model_appropriate: NOT passed: Margins, FCF conversion, acquisition accounting read; organic growth, orders, backlog and segment detail not obtained (MD&A not extracted).
- accounting_red_flags_reviewed: NOT passed: Preliminary purchase accounting, goodwill growth and adjusted versus GAAP EPS gap (2.21 vs 1.85 in Q3) noted; 10-K audit matters and non-GAAP reconciliation unread.
- counterthesis_written: pass: Covers valuation, acquisition share of growth, leverage, refinancing, buyback cut, cyclicality.

## Calculations
```
{
 "valuation": {
  "price": 235.75,
  "shares_outstanding": 229317998,
  "share_basis": "10-Q cover 2026-10-29",
  "market_cap_usd": 54061718028,
  "ttm_revenue_musd": 8191.6,
  "ttm_net_income_musd": 1631.2,
  "pe_ttm": 33.1,
  "ttm_fcf_musd": 1932.4,
  "fcf_yield_pct": 3.57,
  "basis": "TTM = FY2025 + 9M26 - 9M25, USD millions: revenue 7401.116+6193.140-5402.668; NI 1480.142+1232.553-1081.541; OCF 1801.763+1495.857-1217.499=2080.121; capex 130.248+90.722-73.251=147.719; FCF=1932.402. Market cap 235.75*229,317,998=54,059.6M"
 },
 "cash_flow": {
  "ocf_ttm_musd": 2080.1,
  "capex_ttm_musd": 147.7,
  "ocf_9m26_musd": 1495.9,
  "capex_9m26_musd": 90.7,
  "fcf_q3_musd": 527.4,
  "basis": "USD millions; FCF Q3 per company release"
 },
 "balance_sheet": {
  "cash_musd": 666.2,
  "debt_musd": 6669.4,
  "total_liabilities_musd": null,
  "basis": "10-Q 2026-09-30; debt = short-term borrowings and current portion 639.8M + long-term 6,029.6M; total liabilities not extracted"
 }
}
```

## Unresolved gaps
- Organic growth, orders and backlog not quantified in sources read
- Peers and own-history multiples not compared
- MD&A, 8-K 2026-11-06 and 10-K risk factors and audit matters unread
- Quote independence is publisher level only
- Scores not assigned

## Run 72 update (2026-11-18, gap check)
8-K 2026-11-03 Ex 99.1 read: Q3 sales 2,220.3M (+17%), GAAP EPS 1.85, adjusted 2.21, OCF 560.6M, FCF 527.4M, cash 666.2M, total debt 6.67B (derived), net debt about 6.0B; guidance raised to adjusted EPS 8.53 to 8.57; Q4 sales up low 20% range. Organic growth percent, orders and backlog are NOT quantified in the release; the 10-Q MD&A could not be retrieved (text ended before Item 2). 10-Q notes: Indicor price 5,154.1M, goodwill 2,698.5M, Indicor sales about 1.1B, RPO beyond one year 767.7M. 424B5 filings 2026-11-12 (CAD tranche read; USD, EUR concurrent) repay term loan (4.0B, maturities 2029 to 2031) and revolver (975.7M drawn) borrowings; no pro forma leverage in the draft. Gap partly closed; rating unchanged.
