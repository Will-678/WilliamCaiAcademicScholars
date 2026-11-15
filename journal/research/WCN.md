# WCN (Waste Connections) research record, method 2.0

As of 2026-11-15T04:08:30-05:00. Status: **watch**, confidence medium. Scores: null (incomplete). Validator: valid, not attractive-eligible (data/quality_run55_WCN.json). Close 193.97 USD on 2026-11-13 (two publishers, publisher-level independence only).

## Sector model
Waste collection and disposal (infrastructure like): adjusted EBITDA, adjusted free cash flow after capex, leverage, acquisitions, pricing; GAAP earnings include closure-liability adjustments

## Thesis and valuation
Waste Connections (NYSE: WCN), North American solid waste collector and landfill owner. Q3 2026 release (8-K 0001104659-26-117838 Ex99.1, read in full) and 10-Q 0001104659-26-117943 (XBRL): revenue 2,638M (+7.3%); net income 359.2M, diluted EPS 1.43, adjusted EPS 1.58 vs 1.44; adjusted EBITDA 895.8M (34.0% margin vs 33.8%); Q3 OCF 691.9M, capex 294.8M, adjusted FCF 386.9M. 9M26: revenue 7,570M, net income 875.0M, OCF 1,970.8M, capex 893.7M (plus 56.2M undeveloped land), adjusted FCF 1,090M; 9M results include 139.9M impairments and other operating items and a 132.0M closure and post-closure liability adjustment (cash flow line). 2026 outlook: revenue about 10.09B, adjusted EBITDA about 3.345B, adjusted FCF 1.40-1.45B, capex about 1.25B, net income about 1.18B. Debt about 9.43B against 95.7M cash; debt to book capitalisation 54%; repurchases 944.4M and dividends 265.5M in 9M26; quarterly dividend 0.35 (+11%). Price 193.97 (2026-11-13 close, up from 168.28 on 2026-10-21 = +15%), 250.18M shares (10-Q cover 2026-10-09) = market cap about 48.5B; TTM net income 1,133.5M (FY25 1,076.6 + 9M26 875.0 - 9M25 818.1) = 42.8x; TTM FCF 1,249.7M (OCF 2,527.7 - capex 1,278.0 PP&E, excludes land) = 2.6% yield; EV about 57.9B = 17.3x guided adjusted EBITDA; net debt about 2.8x guided EBITDA. Market view: a premium, defensive compounder; evidence for: steady margin expansion, pricing, buybacks; the post-earnings 15% rerating leaves little margin of safety.

## Countercase
At 42.8x TTM GAAP earnings and a 2.6% FCF yield (about 3% on management adjusted FCF guide) the stock prices in years of high single digit growth; revenue growth 7.3% includes about 2 points from acquisitions (acquired revenue 53.4M in Q3 on 2,458M base). The stock jumped about 15% in the three weeks after the print, so the earnings catch-up is in the price. Debt 9.43B with 54% debt to book capital, interest rates and buybacks funded by debt (944M repurchases versus 1,250M TTM FCF before dividends of 266M+) leave little cushion. GAAP earnings are affected by 139.9M impairments and other operating items and a 132.0M closure liability adjustment, and management adjusted FCF excludes book overdraft changes and adds back transaction costs. Landfill closure liabilities, recycling commodity prices, fuel, and volume weakness in construction-linked waste are risks. Peers (WM, RSG, GFL) and WCN history not compared; MD&A, closure note, 10-K audit matters not read.

## Invalidation
Thesis fails if organic price-led growth drops below about 5%, adjusted EBITDA margin stalls below 33%, leverage rises above about 3x with continued debt-funded buybacks, or closure and post-closure liabilities require repeated large adjustments.

## Checks
- latest_filing_checked: pass: Release 2026-10-21 read in full; 10-Q filed 2026-10-22 identified in SEC submissions with no newer 10-Q/10-K; 10-Q text not opened.
- balance_sheet_verified: pass: Debt about 9.43B (long-term 9.427B plus 7.8M current), cash 95.7M, restricted cash 183.1M at 2026-09-30 per release; XBRL cash 95,694,000 matches.
- cashflow_basis_verified: pass: TTM OCF 2,527.7M = 2,414.1 + 1,970.8 - 1,857.2; PP&E capex 1,278.0M = 1,179.2 + 893.7 - 794.9 (XBRL, USD); land purchases (56.2M 9M26) and acquisitions excluded; release adjusted FCF reconciliation read.
- share_count_basis_verified: pass: 250,175,523 shares at 2026-10-09 from 10-Q cover dei.
- valuation_complete: NOT passed: P/E, FCF yield, EV/EBITDA computed on guided EBITDA; peers (WM, RSG, GFL) and history not compared; TTM adjusted EBITDA not assembled.
- sector_model_appropriate: pass: Waste model on adjusted EBITDA, FCF after capex, leverage and acquisitions; GAAP and adjusted shown.
- accounting_red_flags_reviewed: NOT passed: Impairments, closure liability adjustment and adjusted FCF add-backs noted; closure note, audit matters and 10-K unread.
- counterthesis_written: pass: Covers valuation, post-earnings rerating, leverage, buybacks, adjustments and missing peers.

## Sources
- e: earnings_release, full: Q3 2026 earnings release via WebFetch; issuer release (https://www.sec.gov/Archives/edgar/data/1318220/000110465926117838/wcn-ex99d1.htm)
- q: quarterly_filing, snippet: Q3 2026 10-Q cover shares, cash, cash flow via SEC XBRL companyfacts; 10-Q text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0001318220.json)
- fy: annual_filing, relevant_sections: FY2025 10-K 0001104659-26-013700 figures via SEC XBRL only; 10-K text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0001318220.json)
- qa: quote, relevant_sections: stockanalysis.com via WebFetch: USD close 2026-11-13 (https://stockanalysis.com/stocks/wcn/history/)
- qb: quote, relevant_sections: Yahoo Finance via WebFetch: USD close 2026-11-13 (https://finance.yahoo.com/quote/WCN/history/)

## Unresolved gaps
- Peer multiples (WM, RSG, GFL) and WCN history not compared
- 10-Q MD&A, closure and post-closure note and 10-K not read
- TTM adjusted EBITDA not assembled
- Quote independence is publisher level only
- Scores not assigned

Benchmark and paper reference: pending; no outperformance claim.
