# HRTG (NYSE, USD)

Run 86, 2026-11-20T08:09:03-05:00. Status: **watch**. Confidence: medium. Scores: null (incomplete). Fresh idea: yes (annual SEC screen lead, CIK 1598665). Validator: data/quality_run86_HRTG.json. Benchmark VTI pending; no paper reference.

## Sector model
P&C insurer (Florida and Northeast homeowners): P/E on normalized cat load, price to book, combined ratio, reserve development, reinsurance tower and retention, debt service; no free cash flow model; one benign year is not run-rate earnings.

## Thesis and evidence
Heritage Insurance Holdings (NYSE: HRTG), property insurer concentrated in Florida and other coastal states. Q3 2026 10-Q (filed 2026-11-06) read in relevant sections. Q3 revenue 219.2M (+3.2%), Q3 NI 51.1M vs 50.4M; 9M revenue 646.1M (+2.2%), 9M NI 149.3M (4.94 per diluted share) vs 128.9M. Q3 net loss ratio 39.6%, expense ratio 33.4%, combined ratio 73.0% (72.9% a year ago), with net favorable prior-year development, attributed to lower claim frequency and severity and a favorable Florida legal environment. Balance sheet at 2026-09-30: total assets 2,262.8M, total liabilities 1,663.7M, equity 599.1M (505.3M at year end); unpaid losses fell to 459.9M from 579.5M; cash 532.1M; debt: term loan 71.3M (SOFR-based, 6.19%, matures July 2030), 0.9M convertible notes outstanding, 50M revolver. 9M operating cash flow 176.2M. Buybacks 27.9M (1.10M shares) in 9M. Shares outstanding 29,632,416 (2026-09-30 and 2026-10-28 cover). TTM NI 216.0M (FY2025 195.594 + 9M26 149.3 - 9M25 128.919, own arithmetic). Close 32.41 (2026-11-19) x 29.632M = 960.4M = 4.4x TTM NI, 1.60x book, about 36% ROE on TTM NI over period-end equity (own arithmetic, not a forecast). 2026-27 reinsurance: first-event cat limit up to 1.865B for Heritage P&C, aggregate 3.2B with reinstatement, 40% net quota share, first-event retention in a 1-in-100 event 50M for Heritage P&C. Possible market view: a benign-weather peak in a cyclical Florida property market, with soft reinsurance pricing and tort reform tailwinds fading. Differing evidence: sustained sub-75% combined ratios, growing book value, falling share count. Stock fell from 33.83 (11-16) to 32.41 (-4.2%); a Form 144 sale notice was filed 2026-11-18 (insider, not examined).

## Countercase
Earnings come from a period without a major Florida hurricane (not verified for the whole of 2025 and 2026 season) and from favorable reserve development, which can reverse; a 4.4x multiple signals the market prices in a cat or reserve reversal. A first-event retention of 50M for Heritage P&C is small against 599M equity, but NBIC and Zephyr retentions and a second event were not analyzed, and reinsurer credit and renewal pricing (June 2027) were not examined. Equity of 599.1M is after a 22.7M AOCI loss on bonds. Ceding 40% of premiums under quota share lowers net revenue growth. Regulatory and rate-adequacy risk in Florida, Citizens depopulation and policy count were not read. Peers (UVE, HCI, UFCS, SKWD) and history not compared; the 10-K audit matters (reserves) not read; 10-Q risk factors not fully read.

## Invalidation
Invalidated by adverse reserve development, a combined ratio above about 90% outside a catastrophe, a large hurricane exceeding retention and reinstatement costs, reinsurance renewal costs rising sharply, or regulators forcing rate cuts or policy takeouts.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1598665/000119312526451363/hrtg-20260930.htm (quarterly_filing, relevant_sections): 10-Q quarter ended 2026-09-30 filed 2026-11-06; downloaded and converted to text; MD&A results, liquidity, debt note, reinsurance note, balance sheet totals read; risk factors and reserve triangles not fully read
- x: https://data.sec.gov/api/xbrl/companyfacts/CIK0001598665.json (annual_filing, relevant_sections): SEC XBRL company facts: FY2025 NI 195.594M (10-K accession 0001193125-26-103715), 9M25 NI 128.919M
- sub: https://data.sec.gov/submissions/CIK0001598665.json (secondary, relevant_sections): SEC submissions list: 10-Q 2026-11-06; 8-K 2.02 earnings 2026-10-28 (not read); Form 144 on 2026-11-18, 2026-10-19, 2026-09-18
- qa: https://stockanalysis.com/stocks/hrtg/history/ (quote, relevant_sections): stockanalysis.com via WebFetch; close 2026-11-19 (origin undocumented)
- qb: https://finance.yahoo.com/quote/HRTG/history/ (quote, relevant_sections): Yahoo Finance via WebFetch; regular close Nov 19 (origin undocumented)

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-06 is latest periodic filing; 2026-10-28 earnings 8-K not read; only Forms 144 and 4 after the 10-Q.
- balance_sheet_verified: pass: At 2026-09-30 (USD millions): total assets 2,262.8; total liabilities 1,663.7; equity 599.1; cash 532.1; unpaid losses and LAE 459.9; term loan principal 71.3.
- cashflow_basis_verified: pass: Insurer model: no FCF. NI periods matched: FY2025 195.594 + 9M26 149.3 - 9M25 128.919 = 216.0M; 9M OCF 176.2M reported.
- share_count_basis_verified: pass: 29,632,416 shares outstanding at 2026-09-30 per equity note and 2026-10-28 per cover; unvested restricted shares not added.
- valuation_complete: OPEN: P/E and P/B computed; peers, history and normalized cat load not compared.
- sector_model_appropriate: pass: Insurer model: combined ratio, reserves, reinsurance retention, book value; no generic FCF.
- accounting_red_flags_reviewed: OPEN: Reserve development, debt and reinsurance read; 10-K audit matters, reserve triangles and risk factors not read.
- counterthesis_written: pass: Benign-year earnings, reserve reversal, reinsurance cost, regulation.

## Unresolved gaps
- Peers (UVE, HCI, UFCS, SKWD) and own history not compared
- Reserve adequacy, 10-K audit matters and risk factors not read
- 2026-10-28 earnings exhibit not read
- Quote origins undocumented (two aggregators)
