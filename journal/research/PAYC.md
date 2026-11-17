# PAYC (NYSE) research record, run 65

Status: watch. Confidence: medium. Scores: null (incomplete). Validator: data/quality_run65_PAYC.json.
As of 2026-11-16T20:07:48-05:00. Close 254.75 USD on 2026-11-16 (stockanalysis.com table and Yahoo Finance page header agree; publisher-level independence only, origin not documented). Benchmark VTI pending; no paper reference.

## Sector model
Payroll and HCM software (take-rate on recurring revenue plus float income): recurring revenue growth, adjusted EBITDA, SBC, capitalized software, interest on client funds (client funds asset and obligation equal and excluded from cash and debt); not valued on total liabilities.

## Thesis and evidence
Paycom Software (NYSE: PAYC), Q3 2026 10-Q (0001193125-26-449828, filed 2026-11-05; cover, statements read, MD&A and notes beyond cash flow not in extraction) and earnings release Ex 99.1 (8-K 0001193125-26-447248, 2026-11-04). Q3 revenue 543.8M vs 493.3M (+10.2%), recurring and other 519.3M (+11.3%), 9M revenue 1,646.8M (+9.2%); GAAP NI Q3 133.2M, 9M 396.3M vs 339.6M; diluted EPS 9M 8.40 vs 6.02; adjusted EBITDA Q3 268.1M (49.3% margin). FY2026 guidance (raised): revenue 2.213B to 2.218B (about +8%), adjusted EBITDA 1.069B to 1.079B, interest on client funds about 107M. TTM (FY2025 + 9M26 - 9M25): revenue 2,191.1M, NI 510.1M, OCF 810.0M, PP&E capex 150.9M, FCF 659.1M, SBC 78.9M (FCF after SBC 580.2M); capitalized software cash spending not found (only 2.6M of capitalized SBC), so FCF may be overstated. Close 254.75 on 2026-11-16 and 45,034,789 shares (cover 2026-10-27, including 727,631 restricted): market cap 11,473M = 22.5x TTM GAAP NI, FCF yield 5.7% (5.1% after SBC). Balance sheet 2026-09-30: cash 193.9M, long-term debt 750.0M (zero at year end), equity 707.3M, total liabilities 5,381.9M of which client funds obligation 3,891.3M (matched by client fund assets). 9M26 buybacks 1,390.9M cash (vs 218.9M) funded by operating cash 613.9M and 900M credit facility borrowings; treasury shares 19.7M vs 8.8M at year end. The market may price slowing growth, AI and competition risk to payroll software, and falling float income; evidence that differs: growth still about 10% at 49% EBITDA margin, EPS +40% helped by a lower share count, and OCF up 27% in 9M.

## Countercase
Growth is slowing to about 8% guided for the year and 9M interest on client funds fell to 78.3M from 85.8M, with rates lower; EPS growth of 40% is largely a shrinking share count (1.39B buyback in 9M, more than double OCF less capex of 536.5M) funded by 900M new borrowings, so owner earnings growth is much lower than EPS growth and balance sheet flexibility fell from no debt to 750M debt against 194M cash. Interest expense rose to 26.2M in 9M from 2.7M. Cash flow quality: 9M capex fell to 77.4M from 197.4M (capital build-out of headquarters finished) which flatters FCF versus prior year; SBC fell to 52.0M from 91.8M, a drop that is not explained in sources read; capitalized software is unconfirmed. Large insider selling and Form 144 filings were seen on the submissions list (not read). Peers (ADP, PAYX, PCTY, DAY), own-history multiple, customer metrics and legal proceedings were not compared or read. The buyback average price (about 127 per share implied by treasury share change, unverified) suggests it was executed at much lower prices than now, so tender or accelerated structure details are unread.

## Invalidation
Thesis fails if recurring revenue growth falls below about 8% with margins compressing, OCF falls below about 600M annualized, debt keeps rising to fund repurchases, or net client additions turn negative.

## Sources
- q: quarterly_filing, relevant_sections: https://www.sec.gov/Archives/edgar/data/1590955/000119312526449828/payc-20260930.htm (Q3 2026 10-Q via WebFetch extraction (cover, income statement, balance sheet, cash flow start; text only 27,000 characters, MD&A and notes not reached))
- er: earnings_release, relevant_sections: https://www.sec.gov/Archives/edgar/data/1590955/000119312526447248/payc-ex99_1.htm (Earnings release Ex 99.1 to 8-K filed 2026-11-04 via WebFetch (same underlying document as the issuer IR release))
- fy: annual_filing, relevant_sections: https://data.sec.gov/api/xbrl/companyfacts/CIK0001590955.json (SEC XBRL companyfacts by script; FY2025 10-K 0001193125-26-059372 and 10-Q periods matched)
- sub: secondary, relevant_sections: https://data.sec.gov/submissions/CIK0001590955.json (SEC submissions list read 2026-11-16: 10-Q 2026-11-05, 8-Ks 2026-11-02 and 11-04, Form 144 2026-11-13, 13G/A 2026-11-16)
- qa: quote, relevant_sections: https://stockanalysis.com/stocks/payc/history/ (stockanalysis.com via WebFetch; close 2026-11-16 (origin undocumented))
- qb: quote, relevant_sections: https://finance.yahoo.com/quote/PAYC/history/ (Yahoo Finance via WebFetch page header close 2026-11-16 (origin undocumented))

## Checks
- latest_filing_checked: pass: 10-Q filed 2026-11-05 and earnings 8-K 2026-11-04 read in part; 8-K 2026-11-02 and Form 144 2026-11-13 unread; no later periodic filing.
- balance_sheet_verified: pass: At 2026-09-30: cash 193.9M, funds held for clients 3,891.3M equal to client funds obligation 3,891.3M, long-term debt 750.0M (borrowed 900.0M, repaid 150.0M in 9M), equity 707.3M, total liabilities 5,381.9M; debt agrees between 10-Q and release.
- cashflow_basis_verified: pass: OCF FY25 678.9M, 9M26 613.9M, 9M25 482.8M; PP&E capex 270.9M, 77.4M, 197.4M; SBC 118.7M, 52.0M, 91.8M; NI 453.4M, 396.3M, 339.6M; TTM matched; capitalized software spending not obtained, so FCF is before it.
- share_count_basis_verified: pass: 45,034,789 shares at 2026-10-27 from the cover (includes 727,631 restricted shares); market cap uses point-in-time shares.
- valuation_complete: NOT passed: Trailing P/E and FCF yield computed; peers, own history and forward multiples not compared.
- sector_model_appropriate: NOT passed: Recurring revenue growth, adjusted EBITDA, guidance and float interest read; client counts, retention, capitalized software and MD&A not reached.
- accounting_red_flags_reviewed: NOT passed: SBC drop, capex drop, debt-funded buyback noted; 10-K audit matters, notes and legal proceedings unread.
- counterthesis_written: pass: Covers slowing growth, float income, debt-funded buyback driving EPS, capex normalization, SBC swing, insider sales.

## Calculations
```
{
 "valuation": {
  "price": 254.75,
  "shares_outstanding": 45034789,
  "share_basis": "10-Q cover 2026-10-27 (includes 727,631 restricted shares)",
  "market_cap_usd": 11472612498,
  "ttm_revenue_musd": 2191.1,
  "ttm_net_income_musd": 510.1,
  "pe_ttm": 22.5,
  "ttm_fcf_musd": 659.1,
  "fcf_yield_pct": 5.7,
  "basis": "TTM = FY2025 + 9M26 - 9M25, USD millions: revenue 2051.7+1646.8-1507.4=2191.1; NI 453.4+396.3-339.6=510.1; OCF 678.9+613.9-482.8=810.0; PP&E capex 270.9+77.4-197.4=150.9; FCF=659.1 before any capitalized software. Market cap 254.75*45,034,789=11,472.5M"
 },
 "cash_flow": {
  "ocf_ttm_musd": 810.0,
  "capex_ttm_musd": 150.9,
  "ocf_9m26_musd": 613.9,
  "capex_9m26_musd": 77.4,
  "fcf_q3_musd": null,
  "basis": "USD millions; capex = purchases of property and equipment; capitalized software cash not found"
 },
 "balance_sheet": {
  "cash_musd": 193.9,
  "debt_musd": 750.0,
  "total_liabilities_musd": 5381.9,
  "basis": "10-Q 2026-09-30; total liabilities include 3,891.3M client funds obligation matched by client fund assets; debt is long-term debt only"
 }
}
```

## Unresolved gaps
- Capitalized software spending and MD&A client metrics not read
- Buyback structure (tender or open market, average price) unread
- Peers and own-history multiples not compared
- 8-K 2026-11-02, Form 144 2026-11-13, 10-K risk factors unread
- Quote independence is publisher level only
- Scores not assigned
