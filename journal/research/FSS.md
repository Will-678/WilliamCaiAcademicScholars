# FSS research record, method 2.0

As of 2026-11-15T08:09:00-05:00. Status: **watch**, confidence medium. Scores: null (incomplete). Validator: see data/quality_run56_FSS.json. Close 115.36 USD on 2026-11-13 (NYSE; two publishers, publisher-level independence only).

## Sector model
Industrials specialty vehicles (mid): earnings, FCF after capex, backlog and orders, leverage; cyclical municipal and industrial demand

## Thesis and valuation
Federal Signal (NYSE: FSS), maker of street sweepers, vacuum trucks, hydro-excavators and public-safety equipment. Q3 2026 10-Q (0001628280-26-068175, financial statements read; MD&A cut off) and Ex99.1 release (relevant sections read): net sales 655.5M vs 555.0M (+18.1%), operating income 111.4M (+18.5%), net income 79.6M, GAAP EPS 1.29 vs 1.11, adjusted EPS 1.34 vs 1.14; 9M sales 1,951.3M (+23.2%), net income 236.1M (+27.1%), GAAP EPS 3.84. Orders Q3 620.1M vs 466.9M (+33%; ESG 529.7M vs 371.1M, SSG 90.4M vs 95.8M); backlog 966.6M vs 992.0M (down on planned reduction of discontinued third-party Labrie refuse trucks; SSG backlog 65.4M vs 88.2M). ESG Q3 operating margin 18.0% (18.3%), adjusted EBITDA margin 22.4%; consolidated adjusted EBITDA 140.4M (21.4%). 2026 guidance raised to adjusted EPS 5.20-5.32 (from 5.12-5.30), sales 2.61-2.64B (narrowed). 9M OCF 305.6M vs 157.5M, capex 30.0M; debt and finance leases 421.5M vs 566.6M, cash 73.7M, equity 1,578.8M; acquisitions Mega (45M), Western Technology (9.2M), Global Vacuum Systems (about 29M, closed 2026-10-28), New Way earn-out up to 54M remaining. Valuation: close 115.36 x 61,016,459 shares (10-Q cover 2026-09-30) = market cap 7.04B; TTM GAAP net income 296.9M (246.6 + 236.1 - 185.8) = 23.7x; 21.9x adjusted guide midpoint 5.26; TTM FCF 365.1M (OCF 402.8M less capex 37.7M) = 5.2% yield; net debt 347.8M. Market view: a compounder with strong orders priced near 22x earnings; evidence for: orders +33%, margin steady, deleveraging; evidence against: part of growth is acquired, backlog fell y/y and the sales guide narrowed on delivery delays.

## Countercase
Priced at about 22x adjusted EPS, the stock is a cyclical capital-goods name whose strong orders are a one-quarter signal. Backlog fell 2.6% y/y and the sales outlook narrowed because of third-party refuse truck delivery delays, so the 33% order growth includes acquired and pull-forward effects not separated (ESG orders had 'high-teens organic growth' per a search summary, not read in the filing). Operating cash flow of 305.6M in 9M is nearly double last year's partly on working capital; receivables 300.1M and inventories 470.4M are not reconciled. Acquisitions (Mega, Western Technology, New Way, Global Vacuum, earn-out up to 54M) add integration and purchase accounting. A hearing loss litigation liability is recognized; the filing says the incremental loss is not expected to be material but the amount was not read. Tariffs and trade conflicts appear only as general risk factors. Peers (specialty vehicle names such as ALG, REVG, OSK, TTEK) not compared.

## Invalidation
Thesis fails if ESG orders turn down with municipal budget stress, adjusted EBITDA margin drops below about 20%, backlog keeps shrinking while sales rely on acquisitions, or working capital reverses and FCF falls well below net income.

## Checks
- latest_filing_checked: pass: SEC submissions list the 10-Q filed 2026-10-29 as the latest periodic filing; no later 10-Q/10-K; MD&A text and notes not fully read; the 2026-10-28 Global Vacuum acquisition is from the release.
- balance_sheet_verified: pass: Borrowings and finance leases 421.5M, cash 73.7M, equity 1,578.8M at 2026-09-30 per 10-Q; receivables 300.1M, inventories 470.4M, payables 111.3M per release.
- cashflow_basis_verified: pass: OCF TTM 402.8M = 254.7 + 305.6 - 157.5; capex TTM 37.7M = 27.6 + 30.0 - 19.9 (XBRL, USD millions, matching periods); FCF 365.1M; working capital contribution not reconciled.
- share_count_basis_verified: pass: 61,016,459 shares from the 10-Q cover (dated 2026-09-30 in the extract); used for market cap.
- valuation_complete: NOT passed: TTM GAAP and guided adjusted multiples and FCF yield computed; peers and FSS history not compared; no dated price history read.
- sector_model_appropriate: pass: Nonfinancial industrial model: earnings, FCF after capex, orders and backlog, leverage.
- accounting_red_flags_reviewed: NOT passed: Adjusted items (acquisition, discontinued ops, purchase accounting) listed; hearing loss liability amount, goodwill and earn-out accounting not read.
- counterthesis_written: pass: Covers cyclicality, acquired growth, backlog, working capital, litigation and tariffs.

## Sources
- e: earnings_release, relevant_sections: Q3 2026 earnings release exhibit attached to filing, via WebFetch; issuer release (https://www.sec.gov/Archives/edgar/data/0000277509/000162828026068175/fss-20260930x10qexhx991.htm)
- q: quarterly_filing, relevant_sections: Q3 2026 10-Q via WebFetch: financial statements, cover and acquisitions note; MD&A and risk notes cut off (https://www.sec.gov/Archives/edgar/data/277509/000162828026068175/fss-20260930.htm)
- fy: annual_filing, relevant_sections: FY2025 10-K (filed 2026-02-25) figures via SEC XBRL companyfacts only; 10-K text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0000277509.json)
- qa: quote, relevant_sections: stockanalysis.com via WebFetch: USD close 2026-11-13 (https://stockanalysis.com/stocks/fss/history/)
- qb: quote, relevant_sections: Yahoo Finance via WebFetch: USD close 2026-11-13 (https://finance.yahoo.com/quote/FSS/history/)

## Unresolved gaps
- Peers (ALG, REVG, OSK, TTEK) and FSS history not compared
- 10-Q MD&A, hearing loss note, goodwill and earn-out accounting, and 10-K not read
- Organic versus acquired order growth not separated in the filing
- Working capital effect on 9M OCF not reconciled
- Quote independence is publisher level only
- Scores not assigned

Benchmark and paper reference: pending; no outperformance claim.
