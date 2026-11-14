# VRTX (Nasdaq) research record, run 49

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run49_VRTX.json.
As of 2026-11-14T04:07:15-05:00. Close 538.6 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Vertex Pharmaceuticals (Nasdaq: VRTX), cystic fibrosis franchise plus Journavx, Casgevy and, since 2026-09-01, Crinetics (Palsonify, atumelnant). Q3 2026 (10-Q filed 2026-11-03): revenue 3,440.8M (+11.8% vs 3,076.4M), operating income 712.9M (vs 1,186.2M), net income 653.6M (diluted EPS 2.56 vs 4.20). The profit drop reflects the Crinetics deal: 409.6M accelerated equity award expense and 58.9M transaction costs in SG&A, SG&A 844.1M vs 445.1M, R&D 1,320.6M vs 977.7M. Crinetics cost 10.0B cash equity value (9.0B net of acquired cash); goodwill 1,335.4M, Palsonify intangible 3,010.0M, atumelnant IPR&D 5,116.0M. Financing: 4,496.8M term loan proceeds in 9M; debt 999.6M short-term plus 3,497.0M long-term (about 4.50B) vs zero at 2025-12-31. Cash and marketable securities 9,821.2M (vs 12,320.4M at year end), so net cash about 5.32B. 9M OCF 3,196.6M less capex 342.9M = FCF 2,853.7M; TTM OCF 3,694.6M (FY25 3,631.4 - 9M25 3,133.4 + 3,196.6) less TTM capex 492.3M = FCF 3,202.3M. At 538.60 (2026-11-13 close, 52-week 412.27-568.67) and 253.54M shares, market cap about 136.6B, EV about 131.2B, TTM FCF yield 2.3%, EV/FCF 41x; TTM SBC about 668.6M (includes the 409.6M one-off acceleration), FCF after SBC about 2.53B (1.9%). Trailing GAAP P/E about 34.6x (stockanalysis) is depressed by acquisition charges, so ex-charge multiples are lower but I did not reconcile them. Buybacks 933.1M in 9M but only 120.8M in Q3 as cash went to the deal. Why the market may price it this way: a 34x trailing multiple on 12% growth assumes Journavx and Casgevy ramps plus pipeline value; what differs: the CF franchise is highly cash generative and net cash remains large; what would close the gap: product revenue splits and guidance, which I did not read.

## Countercase
Quality is high but price attractiveness is not shown: FCF yield about 2.3% with 12% growth. Cystic fibrosis revenue is concentrated, with competition and patent timelines I did not review. The 10B Crinetics deal paid for pre-revenue IPR&D (5.1B atumelnant) that can be written down on trial failure, and leverage went from zero to 4.5B (term loan terms, rates and covenants unread). Opioid-alternative Journavx and Casgevy ramps are unverified. Product revenue breakdown, guidance and legal proceedings were in truncated parts of the 10-Q and the earnings release (8-K 2026-11-02, URL not retrievable) was not read. Form 144 filings 11-06 and 11-12 indicate insider sales (content unread).

## What would change the view
Thesis would fail if CF revenue growth stalls, Journavx or Casgevy ramps disappoint, atumelnant trials fail forcing impairment, or the term loan and integration costs constrain buybacks and returns.

## Checks
- latest_filing_checked: passed. 10-Q filed 2026-11-03 read in part; submissions show no later periodic report, only Forms 4/144 and a 13G/A.
- balance_sheet_verified: passed. Cash 4,979.3M, current securities 1,324.0M, long-term securities 3,517.9M; short-term debt 999.6M, long-term debt 3,497.0M; leases and other liabilities not read.
- cashflow_basis_verified: passed. 9M26 OCF 3,196.6M less capex 342.9M = 2,853.7M; TTM built from FY25 10-K minus 9M25 plus 9M26, all from SEC XBRL with matching periods.
- share_count_basis_verified: passed. 253,537,674 shares at 2026-10-31 from 10-Q cover (XBRL dei) agrees with stockanalysis 253.54M.
- valuation_complete: NOT passed. FCF yield and EV computed; no peers (REGN, GILD, AMGN, BIIB), history, or ex-charge earnings; guidance unread.
- sector_model_appropriate: passed. Biopharma: FCF after SBC, net cash, acquired IPR&D, product concentration; bank ratios not applicable.
- accounting_red_flags_reviewed: NOT passed. Acquisition charges identified, but purchase accounting, term loan covenants, legal proceedings and audit matters not read.
- counterthesis_written: passed. Covers valuation, concentration, IPR&D impairment, leverage and insider sales.

## Unresolved gaps
- Earnings release and guidance unread
- Product revenue split unread
- Peers and history not done
- Term loan terms and covenants unread
- Legal proceedings unread
- Quotes: two publishers, publisher-level independence only
- Scores not assigned

## Sources
- k1: https://www.sec.gov/Archives/edgar/data/875320/000087532026000291/vrtx-20260930.htm (quarterly_filing, relevant_sections) Form 10-Q for quarter ended 2026-09-30 filed 2026-11-03 via WebFetch extract; income statement, Crinetics note, debt, cash and repurchases read; product revenue, guidance and legal sections truncated
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0000875320.json (annual_filing, relevant_sections) SEC XBRL companyfacts: FY2025 10-K and 2026 10-Qs: OCF, capex, SBC, EPS, shares 253,537,674 at 2026-10-31
- sub: https://data.sec.gov/submissions/CIK0000875320.json (secondary, relevant_sections) SEC submissions JSON 2026-11-14: 8-K 2.02 on 2026-11-02, 10-Q 2026-11-03, Forms 144 on 11-06 and 11-12
- e1: https://www.sec.gov/Archives/edgar/data/875320/000087532026000100/vrtx-20261102.htm (earnings_release, unread) Earnings 8-K filed 2026-11-02; URL guess returned 404 so the release was not read
- qa: https://stockanalysis.com/stocks/vrtx/ (quote, relevant_sections) stockanalysis.com via WebFetch: close 538.60 at 4:00 PM EST 2026-11-13, 253.54M shares, market cap 136.56B, P/E 34.64
- qb: https://finance.yahoo.com/quote/VRTX/history/ (quote, relevant_sections) Yahoo Finance via WebFetch: close 538.60 on 2026-11-13; 542.62 on 11-12
