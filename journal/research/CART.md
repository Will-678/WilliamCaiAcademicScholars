# CART (Nasdaq) research record, run 62

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run62_CART.json (valid, not attractive-eligible).
As of 2026-11-16T08:10:00-05:00. Close 58.87 USD on 2026-11-13 (stockanalysis.com and Yahoo Finance agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Thesis and evidence
Maplebear (Instacart, Nasdaq: CART) is under a definitive agreement to be acquired by DoorDash (10-Q note, signed 2026-10-28). Per a search summary of the 8-K and 425 filings (documents not opened): 65.00 per share, cash or 0.3372 DoorDash shares or 48.75 cash plus 0.0843 shares, stock capped at 25%, about 17B equity value, 26% premium to the 2026-10-22 close, expected close end 2027 or first half 2028, needs HSR, Canada, Israel and shareholder approval; holders of about 19% have agreed to vote in favor. Close 58.87 on 2026-11-13 (two aggregators agree) leaves a 10.4% gross spread to 65.00 (cash election; stock election moves with DoorDash). Standalone: Q3 revenue 1,095M vs 939M (+17%), net income 147M, EPS 0.60; TTM revenue 4,149M, NI 484M, OCF 1,268M, capex 58M, FCF 1,210M (SBC 440M TTM: 770M after SBC), market cap 13.93B at 236.63M shares: 28.8x TTM, FCF yield 8.7% (5.5% after SBC). Cash 830M plus 105M securities. Conclusion: a stock whose price is anchored to a cash takeover, so ordinary valuation research is not the right lens. It is merger arbitrage with long timing and antitrust risk, not a long term growth or value idea, and the 10% spread over 1 to 1.5 years is compensation for break risk (the pre-deal price was about 51.6 by implication of the 26% premium).

## Countercase
Antitrust review of two leading US delivery platforms could take until 2028 or block the deal; if it breaks the price may fall toward the undisturbed level near 52 (derived from the stated premium, not a read quote). Capital is tied up for 1 to 1.5 years for about 10% gross, before opportunity cost. Upside above 65 is capped. SBC is large. Deal terms were taken from a search summary, not read filings.

## Invalidation
Interest changes if an HSR second request or regulatory block emerges, the spread widens sharply, or DoorDash financing or votes fail.

## Sources
- q: https://www.sec.gov/Archives/edgar/data/1579091/000157909126000055/cart-20260930.htm (quarterly_filing, relevant_sections; Q3 2026 10-Q via WebFetch extraction (statements; MD&A, Note 17 and legal truncated))
- fy: https://data.sec.gov/api/xbrl/companyfacts/CIK0001579091.json (annual_filing, relevant_sections; SEC XBRL companyfacts fetched by curl; FY2025 10-K (0001579091-26-000018) and 10-Q periods matched)
- sub: https://data.sec.gov/submissions/CIK0001579091.json (secondary, relevant_sections; SEC submissions list read 2026-11-16: 10-Q 2026-11-05, many 425 filings 10-29 to 11-13)
- deal: https://www.sec.gov/Archives/edgar/data/0001579091/000119312526437075/d171568dex991.htm (secondary, snippet; Deal terms from a web search summary of the 8-K and 425 filings; the documents themselves were not opened)
- qa: https://stockanalysis.com/stocks/cart/statistics/ (quote, relevant_sections; stockanalysis.com via WebFetch; close 2026-11-13 (origin undocumented))
- qb: https://finance.yahoo.com/quote/CART/history/ (quote, relevant_sections; Yahoo Finance via WebFetch; close 2026-11-13 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-05 read in part; numerous 425 merger filings through 2026-11-13 seen in the list, not read.
- balance_sheet_verified: pass: Cash 830M, marketable securities 105M, restricted cash 93M at 2026-09-30; no borrowings seen, revolver drawn amount and total liabilities not read.
- cashflow_basis_verified: pass: OCF FY25 971M, 9M26 1,085M, 9M25 788M; PP&E capex 61M, 46M, 49M; SBC 352M, 341M, 253M; TTM matched from XBRL. Capitalized software not separated.
- share_count_basis_verified: pass: 236,630,090 shares at 2026-10-30 from the cover.
- valuation_complete: NOT passed: Standalone multiples computed but the price is governed by the 65.00 cash offer; spread analysis rests on an unread-document summary; no peers.
- sector_model_appropriate: NOT passed: Marketplace model (GOV, orders, take rate) not read: MD&A truncated; situation is a pending merger so standalone model is secondary.
- accounting_red_flags_reviewed: NOT passed: SBC 440M TTM flagged; legal, FTC, Note 17 and merger agreement termination terms not read.
- counterthesis_written: pass: Covers antitrust timing, capped upside, SBC, break risk.

## Unresolved gaps
- Merger agreement, 8-K and proxy not opened: terms, termination fee, outside date, regulatory conditions unverified
- MD&A (GOV, orders, take rate) and legal proceedings not read
- Total liabilities and revolver not read
- Peers not compared; standalone valuation secondary to deal price
- Quote independence is publisher level only
- Scores not assigned

## Update 2026-11-16 (morning compile): deal terms now read from the issuer release
I opened the DoorDash press release (SEC Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/0001579091/000119312526437075/d171568dex991.htm). Confirmed: 65.00 per share (26% premium to the 2026-10-22 close, about 17B equity value); at least 75% cash; stock capped at 25% of total consideration with proration; close expected end of 2027 or first half of 2028; conditions are Instacart holder vote, Hart-Scott-Rodino waiting period, Canada and Israel competition clearances; holders of about 19% have agreed to vote yes; no financing condition; JPMorgan 364-day bridge commitment. The release states no termination fee amounts, so those remain unverified. The merger agreement and proxy are still unread. The record JSON was not changed (its deal source stays marked snippet until the agreement is read). Gross spread at the 2026-11-13 close of 58.87 is 10.4% over roughly 13 to 20 months, before break risk. Rating unchanged: watch, medium, score incomplete.
