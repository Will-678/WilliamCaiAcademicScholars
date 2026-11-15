# ALL (Allstate) research record, method 2.0

As of 2026-11-15T04:08:30-05:00. Status: **watch**, confidence medium. Scores: null (incomplete). Validator: valid, not attractive-eligible (data/quality_run55_ALL.json). Close 267.64 USD on 2026-11-13 (two publishers, publisher-level independence only).

## Sector model
Insurer (personal lines P&C): earnings, book value, combined ratio, catastrophe and reserve development, investment portfolio; no FCF model (operating cash flow includes float)

## Thesis and valuation
Allstate (NYSE: ALL), largest US personal auto and homeowners insurer. Q3 2026 release (8-K 0000899051-26-000156 Ex99.1, read in full) and 10-Q 0000899051-26-000157 (XBRL only): revenues 17,348M (+0.5%); net income to common 2,050M vs 3,717M (Q3 2025 included a 720M gain on sale of group health); adjusted net income 2,493M vs 2,976M, adjusted EPS 9.76 vs 11.17; Property-Liability combined ratio 86.6 vs 80.1 (underlying 80.5 vs 78.7); catastrophe losses 1,650M vs 558M; Auto recorded 83.2, underlying 89.8 vs 86.0; Homeowners recorded 89.5. Net investment income 1,177M vs 949M. Policies in force +3.9% to 217.6M, premiums earned +3.8%. Book value per common share 120.23 (+25.3%), shares 248.8M (-5.1% y/y) after 2,904M repurchases in 9M26; trailing 12 month ROE 41.3%, adjusted 39.7%. Debt 7,494M. Price 267.64 (2026-11-13 close), 247.45M shares (10-Q cover 2026-10-19) = market cap about 66.2B; 2.2x book (120.23, Sep 30 BVPS), 5.7x TTM net income to common (11,522M = Q4 2025 3,803M + 9M26 7,719M, XBRL). Market view: a peak-margin personal lines insurer priced at under 6x earnings because auto margins are expected to normalise; evidence for: strong buybacks, rising PIF, book value growth; evidence against: underlying auto combined ratio rising and growth is volume not price.

## Countercase
A 5.7x multiple on a 41% ROE reflects a peak underwriting cycle, not a bargain: underlying auto combined ratio worsened 3.8 points y/y to 89.8 and the release shows premiums earned +3.8% against PIF +3.4%, so average premium growth is near zero while loss costs rise. Q3 homeowners catastrophe losses nearly tripled (1,330M vs 479M); a worse cat year would cut TTM earnings sharply. Prior-year reserve reestimates moved to 5.1 points of combined ratio (Auto 9.1) from 2.7, and the release excerpt did not state the direction here; if unfavorable, reserve adequacy is a thesis breaker (not verified). Unrealized net capital losses reached 2.6B pre-tax and the portfolio returned -2.1% in the quarter. TTM earnings include items not adjusted (realized gains, pension remeasurement); TTM adjusted earnings not assembled. Peers (PGR, TRV, CB, Allstate history) not compared. Arity acquisitions (INRIX, Replica) and restructuring add execution risk. 10-Q MD&A, reserve note, reinsurance and 10-K not read. The price already rose from 259.87 (2026-10-30) to 267.64 after results.

## Invalidation
Thesis fails if underlying auto combined ratio exceeds about 92 on rising severity with flat pricing, reserve development is unfavourable and growing, cat losses stay at or above Q3 levels, or buybacks cannot continue without eroding capital.

## Checks
- latest_filing_checked: pass: Release 2026-11-04 read in full; 10-Q filed 2026-11-04 identified in SEC submissions (no later 10-Q/10-K; later 8-K 2026-10-15 and earlier are before it); 10-Q text not opened.
- balance_sheet_verified: pass: Debt 7,494M, equity 32,311M, liabilities 95,557M, assets 127,849M at 2026-09-30 per release and XBRL; insurer balance sheet, reserves and investment detail not analyzed.
- cashflow_basis_verified: pass: OCF TTM 12,968M = 10,110 + 9,979 - 7,121 (XBRL, USD); insurer OCF includes float and is not used as owner earnings; capex 145M 9M26.
- share_count_basis_verified: pass: 247,449,496 shares at 2026-10-19 (10-Q cover dei); release shows 248.8M at 2026-09-30.
- valuation_complete: NOT passed: P/E, P/B computed; TTM adjusted earnings, peers (PGR, TRV, CB) and through-cycle ROE not compared.
- sector_model_appropriate: pass: Insurer model on book value, combined ratio and ROE; FCF yield not used.
- accounting_red_flags_reviewed: NOT passed: Reserve development direction, realized gains, pension remeasurement and unrealized losses noted from release; notes and auditor items unread.
- counterthesis_written: pass: Covers cycle peak, auto margin, cats, reserves, investments, acquisitions and missing peers.

## Sources
- e: earnings_release, full: Q3 2026 earnings release via WebFetch; issuer release (https://www.sec.gov/Archives/edgar/data/899051/000089905126000156/allcorp93026earningsreleas.htm)
- q: quarterly_filing, snippet: Q3 2026 10-Q accession and cover share count, debt, equity via SEC XBRL companyfacts; 10-Q text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0000899051.json)
- fy: annual_filing, relevant_sections: FY2025 10-K 0000899051-26-000031 figures via SEC XBRL only; 10-K text not opened (https://data.sec.gov/api/xbrl/companyfacts/CIK0000899051.json)
- qa: quote, relevant_sections: stockanalysis.com via WebFetch: USD close 2026-11-13 (https://stockanalysis.com/stocks/all/history/)
- qb: quote, relevant_sections: Yahoo Finance via WebFetch: USD close 2026-11-13 (https://finance.yahoo.com/quote/ALL/history/)

## Unresolved gaps
- Peer multiples (PGR, TRV, CB) and Allstate history not compared
- Reserve development direction and reserve note not read
- TTM adjusted earnings and through-cycle ROE not assembled
- 10-Q MD&A, 10-K and investment portfolio detail not read
- Quote independence is publisher level only
- Scores not assigned

Benchmark and paper reference: pending; no outperformance claim.
