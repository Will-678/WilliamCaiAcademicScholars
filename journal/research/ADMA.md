# ADMA research record, method 2.0

As of 2026-11-15T08:09:00-05:00. Status: **watch**, confidence medium. Scores: null (incomplete). Validator: see data/quality_run56_ADMA.json. Close 13.68 USD on 2026-11-13 (Nasdaq; two publishers, publisher-level independence only).

## Sector model
Healthcare biopharma / plasma biologics (small-mid): earnings, FCF after capex, product concentration, inventory, leverage; GAAP and adjusted both shown

## Thesis and valuation
ADMA Biologics (Nasdaq: ADMA), plasma-derived immune globulins (ASCENIV, BIVIGAM). Q3 2026 release (8-K 0001140361-26-041959 Ex99.1, relevant sections read) and 10-Q 0001140361-26-041977 (statements and notes read; MD&A cut at 100,000 characters): revenue 141.1M vs 134.2M (+5.1%), 9M 380.0M vs 371.0M (+2.4%); ASCENIV 124.7M (+30.7%, 88% of Q3 revenue), BIVIGAM 15.4M (-35.2%), intermediates and other 0.9M vs 15.0M. Gross margin 71% vs 56%; net income 49.9M vs 36.4M (Q3), 133.0M 9M vs 97.6M; GAAP EPS 0.22; adjusted net income 51.1M, adjusted EBITDA 77.3M. 9M OCF 105.2M vs 14.8M, capex 6.8M. Guidance 2026: revenue at least 530M (reiterated), adjusted EBITDA at least 275M and adjusted net income at least 180M (both raised). Balance sheet 2026-09-30: cash 124.6M, debt 195.9M (JPM revolver 125.0M drawn in 2026, term loan 72.2M), inventories 266.1M, equity 438.5M; 16.5M shares repurchased in 9M (180.3M; 6.3% of shares), shares outstanding 222.8M (237.9M at Dec 2025), 221.85M at cover date 2026-10-30. Valuation: close 13.68 (2026-11-13) x 221,854,389 = market cap 3.03B; TTM GAAP net income 182.4M (146.9 + 133.0 - 97.6) = 16.6x; 16.9x adjusted net income guide floor 180M; TTM FCF 132.9M (OCF 140.8M less capex 7.9M) = 4.4% yield (3.6% after TTM SBC 24.1M); net debt 71.3M. Close rose from 10.48 (2026-11-04) to 13.21 (2026-11-05) after the print, +26%. Market view: a one-drug growth story with falling BIVIGAM; evidence for: ASCENIV +31%, margin expansion, buybacks, raised floors; evidence against: total growth slowed to 2.4% in 9M, three customers are about 86% of Q3 revenue.

## Countercase
Concentration and quality of growth: three customers were about 86% of Q3 revenue and two customers about 84% of receivables (10-Q), so one lost contract or distributor pricing change breaks the story. ASCENIV is 88% of Q3 revenue; BIVIGAM fell 47% over 9M to competitive pricing and channel inventory, and total 9M revenue grew only 2.4% while gross margin gains (yield enhancement, mix) drove earnings; margin gains are finite. Inventory is 266.1M against TTM revenue of 519.2M, and the 71% gross margin includes yield enhancement add-backs (small) and a plasma center gain of 8.0M in 9M. Buybacks of 180.3M and a 125M revolver draw increased debt from 72.1M to 195.9M; share count is down 6.3% but financed partly with debt. Securities class action (Mazzarino, D.N.J., lead plaintiff appointed 2026-10-16), derivative suits and three Section 220 demands are open with no accrual. The 2026 revenue floor of 530M implies Q4 revenue of at least about 150M, a step-up; guidance is a floor not a forecast. The +26% jump after results compresses the margin of safety. Peers (GRFS, CSL, Kedrion, Octapharma private) not compared and no valuation history read.

## Invalidation
Thesis fails if ASCENIV growth stalls or a top customer cuts volume, gross margin falls below about 65% on pricing or plasma costs, Q4 revenue misses the implied step-up for the 530M floor, inventory builds without sales, or litigation or debt-funded buybacks weaken liquidity.

## Checks
- latest_filing_checked: pass: SEC submissions list the 10-Q and release both filed 2026-11-04 as the latest; no later 10-Q/10-K; 10-K and MD&A not fully read.
- balance_sheet_verified: pass: Cash 124,555K, debt net 195,857K (revolver 125,000K, term loan 72,188K), inventories 266,115K, equity 438,507K at 2026-09-30 per 10-Q and release.
- cashflow_basis_verified: pass: OCF TTM 140.8M = 50.396 + 105.156 - 14.757; capex TTM 7.9M = 22.575 + 6.801 - 21.491 (XBRL, USD, matching periods); FCF 132.9M; SBC TTM 24.1M.
- share_count_basis_verified: pass: 221,854,389 shares at 2026-10-30 (10-Q cover); 222,793,831 at 2026-09-30 on the balance sheet; cover count used.
- valuation_complete: NOT passed: TTM GAAP and guided adjusted multiples and FCF yield computed; peers and ADMA history not compared; the post-earnings jump of 26% not explained beyond guidance.
- sector_model_appropriate: pass: Biopharma commercial-stage model on profits and FCF after capex with concentration and inventory checks; single-product risk noted.
- accounting_red_flags_reviewed: NOT passed: Adjusted items, plasma center gain, yield enhancement and customer concentration identified; inventory valuation, revenue allowances, deferred tax asset 70.7M and auditor items not read.
- counterthesis_written: pass: Covers concentration, growth deceleration, margin finiteness, leverage-funded buybacks, litigation, guidance floor and post-print price jump.

## Sources
- e: earnings_release, relevant_sections: Q3 2026 earnings release via WebFetch; issuer release (https://www.sec.gov/Archives/edgar/data/1368514/000114036126041959/ef20084542_ex99-1.htm)
- q: quarterly_filing, relevant_sections: Q3 2026 10-Q via WebFetch: statements, concentration, debt, legal and plasma supply notes; last 3,038 characters and parts of MD&A not read (https://www.sec.gov/Archives/edgar/data/1368514/000114036126041977/ef20080522_10q.htm)
- fy: annual_filing, relevant_sections: FY2025 10-K (filed 2026-02-25) figures via SEC XBRL companyfacts only; 10-K text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0001368514.json)
- qa: quote, relevant_sections: stockanalysis.com via WebFetch: USD close 2026-11-13 (https://stockanalysis.com/stocks/adma/history/)
- qb: quote, relevant_sections: Yahoo Finance via WebFetch: USD close 2026-11-13 (https://finance.yahoo.com/quote/ADMA/history/)

## Unresolved gaps
- Peers (GRFS, CSL) and ADMA history not compared
- 10-K, 10-Q MD&A, revenue allowances, inventory and deferred tax notes not read
- Customer identity and contract terms for the three customers about 86% of revenue unknown
- Reason for the 26% post-print jump beyond raised guidance not verified
- Quote independence is publisher level only
- Scores not assigned

Benchmark and paper reference: pending; no outperformance claim.
