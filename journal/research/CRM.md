# CRM (Salesforce) research record, method 2.0

As of 2026-11-15T04:08:30-05:00. Status: **watch**, confidence medium. Scores: null (incomplete). Validator: valid, not attractive-eligible (data/quality_run55_CRM.json). Close 217.84 USD on 2026-11-13 (two publishers, publisher-level independence only).

## Sector model
Enterprise software: subscription growth, GAAP and non-GAAP margin, FCF after SBC, leverage after debt-funded buyback and acquisitions

## Thesis and valuation
Salesforce (NYSE: CRM), CRM and data software. Q2 FY27 release (quarter ended 2026-07-31, read in full from IR page) and 10-Q 0001108524-26-000190 (XBRL; text fetch returned HTTP 503): revenue 11,345M (+11%, includes 456M from Informatica), subscription 10,820M (+12%), GAAP operating margin 20.5%, non-GAAP 34.1%; GAAP net income 3,526M includes 2,613M gains on strategic investments (about 2.43 of 4.29 EPS), so operating income was flat (2,331M vs 2,332M). Q2 OCF 1,269M, FCF 1,098M; cRPO 33.5B (+14% CC), RPO 66.3B. FY27 guide: revenue 46.1-46.4B, non-GAAP EPS 16.67-16.71, GAAP EPS 10.21-10.25, OCF growth 4-5%. Capital structure changed sharply: debt 39,288M (versus 14,439M at 2026-01-31; net proceeds 24,842M in six months) funded a 27,332M six-month buyback including a 25B accelerated share repurchase (final settlement expected October 2026); cash and securities about 11.4B. New deals: Braze at 47.50 cash per share, about 5.66B enterprise value (8-K 2026-10-20, close in FY28), Contentful and Fin pending. Price 217.84 (2026-11-13 close; 242.43 on 2026-10-20 before the Braze news = -10%); 823M shares (10-Q cover 2026-08-20, before final ASR delivery, so overstated) gives market cap at most about 179B. TTM GAAP net income 9,662M (FY26 7,457 + H1 FY27 5,633 - H1 FY26 3,428; includes gains) = 18.6x; TTM FCF 15,154M (OCF 15,750 - capex 596) = 8.5% yield, 6.4% after 3,665M SBC; EV about 207B; about 13.1x guided non-GAAP EPS. Market view: a mature software franchise priced below history on AI disruption fear; evidence for: cash generation, cRPO +14%, huge buyback; evidence against: leverage and growth that is partly acquired.

## Countercase
Organic growth is lower than 11%: Informatica adds about 3 points, and Contentful and Fin add 200M to the guide, so organic is perhaps 8%. GAAP net income is inflated by 2.6B of investment gains, and non-GAAP EPS (16.69) excludes about 3.7B SBC and acquired-intangible amortisation. Debt rose from 14.4B to 39.3B to fund the buyback, adding interest cost; FCF yield is on a market cap that may include shares not yet retired and excludes about 25B of debt-funded purchase, and the company now plans 5.66B cash for Braze plus further deals, which increases leverage and integration risk and shows acquisition appetite. Operating cash flow growth guide is only 4-5%, FCF growth the same, so earnings growth leans on the lower share count. AI agents could erode seat-based pricing. Price fell after the Braze announcement. Peers (MSFT, NOW, ADBE, SAP) and history not compared; 10-Q text (debt note, tax, legal), 10-K and Q3 FY27 results (due early December, date unverified) not read.

## Invalidation
Thesis fails if organic cRPO growth falls below about 10%, non-GAAP operating margin drops below about 33%, leverage rises further through acquisitions without FCF growth, or AI-driven seat compression shows in subscription renewals.

## Checks
- latest_filing_checked: pass: Latest periodic filing is the 10-Q filed 2026-08-27; newer 8-Ks (2026-09-04, 09-17, 10-20) listed in submissions, only the Braze 8-K read; Q3 FY27 results not yet released; 10-Q text not opened (503).
- balance_sheet_verified: pass: Debt 39,288M noncurrent, cash 8,310M plus marketable securities 3,093M at 2026-07-31 per release; XBRL LongTermDebt 39,288M and cash 8,310M agree; debt components not read.
- cashflow_basis_verified: pass: TTM OCF 15,750M = 14,996 + 7,970 - 7,216; capex 596M = 594 + 316 - 314; SBC 3,665M = 3,509 + 1,763 - 1,607 (XBRL, USD); capitalized software not separately found.
- share_count_basis_verified: pass: 823M shares at 2026-08-20 from 10-Q cover dei (rounded); final ASR delivery in October will reduce the count, so market cap is an upper bound.
- valuation_complete: NOT passed: P/E, FCF yield, EV computed; non-GAAP multiple uses management EPS; peers and history not compared; shares post-ASR unknown.
- sector_model_appropriate: pass: Software model with FCF after SBC and leverage after debt-funded buyback.
- accounting_red_flags_reviewed: NOT passed: Investment gains, SBC, acquired revenue, non-GAAP exclusions noted; 10-Q notes and auditor items unread (503).
- counterthesis_written: pass: Covers organic growth, gains, leverage, deals, AI risk and missing peers.

## Sources
- e: earnings_release, full: Issuer IR release via WebFetch (same underlying document as 8-K 0001108524-26-000187 Ex99.1, which returned HTTP 503) (https://investor.salesforce.com/news/news-details/2026/Salesforce-Delivers-Record-Second-Quarter-Fiscal-2027-Results/default.aspx)
- b: secondary, full: Braze acquisition joint press release 2026-10-20 via WebFetch; issuer release (https://www.sec.gov/Archives/edgar/data/1108524/000119312526425881/d516983dex991.htm)
- q: quarterly_filing, snippet: Q2 FY27 10-Q cover share count, cash flow, SBC via SEC XBRL companyfacts; 10-Q text fetch returned HTTP 503 (https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json)
- fy: annual_filing, relevant_sections: FY2026 10-K 0001108524-26-000060 figures via SEC XBRL only; 10-K text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0001108524.json)
- qa: quote, relevant_sections: stockanalysis.com via WebFetch: USD close 2026-11-13 (https://stockanalysis.com/stocks/crm/history/)
- qb: quote, relevant_sections: Yahoo Finance via WebFetch: USD close 2026-11-13 (https://finance.yahoo.com/quote/CRM/history/)

## Unresolved gaps
- Peer multiples (MSFT, NOW, ADBE, SAP) and CRM history not compared
- 10-Q text (debt note, tax, legal) and 10-K not read (HTTP 503)
- Post-ASR share count and Braze, Contentful, Fin financing unknown
- Q3 FY27 results not yet released
- Quote independence is publisher level only
- Scores not assigned

Benchmark and paper reference: pending; no outperformance claim.
