# State and handoff

## Reader profile
Known (2026-11-05, from William):
- Monthly contribution about $1,000, invested as one lump sum on one day each month (day not yet chosen).
- Current IBKR balance under $1,000.
- Time horizon: none of the money is needed within 4 years; all can stay 10+ years.
- Loss tolerance: says he would keep buying through a 30% drop (stated, not yet tested; revisit after a real drawdown).
- U.S. tax resident, taxable IBKR account.
Still unknown: current holdings, IBKR fee tier and fractional share eligibility, preferred contribution day.

## Targets
50% US stock index, 25% international stock index, 20% short Treasuries/insured savings, 5% researched stocks.

## Environment limits found on 2026-11-04
- WebSearch works but returns weak, often undated aggregator pages.
- WebFetch could not reach federalreserve.gov, home.treasury.gov, or bls.gov (host not in the session's allowed domains).
  Until those are allowed, official data cannot be verified in a run.
- No live or delayed price feed. Prices must come from a cited page with a timestamp, or be reported unavailable.

## Access check 2026-11-05
Reachable: federalreserve.gov, home.treasury.gov, data.sec.gov, investor.vanguard.com, interactivebrokers.com.
Still 403: www.bls.gov, www.sec.gov (bot blocking, not the allowlist). Use data.sec.gov for filings; use BLS via other sources.

## Fund vehicles to verify (unverified, from secondary sources only)
- US stock: VTI (Vanguard Total Stock Market ETF). Expense ratio 0.03% in several secondary sources.
- International: VXUS (Vanguard Total International Stock ETF). Secondary sources disagree (0.05% to 0.08%); check Vanguard.
- Short Treasuries: not yet researched.
- IBKR availability for William's account type and country: not verified.

## Known calendar facts
- Last FOMC meeting: Oct 27-28, 2026; minutes due Nov 18 (per a Fed calendar page seen via search; not fetched directly).
- Next FOMC: Dec 8-9, 2026 (same caveat).

## Handoff for next run
1. Check whether federalreserve.gov, treasury.gov, bls.gov, sec.gov are now reachable; if so, pull the fed funds range, yield curve, and next jobs/CPI dates.
2. Verify VTI, VXUS, and one short Treasury ETF on issuer pages (expense ratio, holdings, minimums).
3. Start screening candidates from filings; no candidates yet.
4. Ask William for the profile items above if a dollar or suitability question comes up.

## Handoff 2026-11-05 (run date corrected from 2026-11-06)
- Data method that works: built-in WebFetch/WebSearch; company IR pages and SEC 8-K exhibits via WebFetch. Do not put personal details in any request or header (user instruction 2026-11-06). Avoid shell loops with dynamic URLs.
- Watchlist: ABT, LOW, PEP (see journal/watchlist_long.md). Screened 15; V, MMC, ADP failed to load.
- Next: read Abbott Q3 10-Q for debt/cash; verify LOW and PEP next earnings dates; compute PEP core EPS valuation; check CSCO; look at sectors not covered (banks, energy, industrials, utilities); verify VTI 2026-11-05 close from a second source (benchmark pending).

## Handoff 2026-11-05 run2 (clock 23:50 ET; saved as reports/2026-11-05-run2.md)
- Scheduler said 2026-11-06 but the ET clock said Nov 5. Next run: check TZ clock; if it is Nov 6 or later, write reports/2026-11-06.md replacing the correction notice.
- Done: ABT debt/cash verified; JPM and NEE added (watch). VTI baseline 360.52 on 11-05 (fell 4.35% that day; cause unknown, find a news source).
- Next: read JPM 10-Q and NEE 10-Q for credit and debt; Abbott NEC accrual note; LOW/PEP dates from company IR; PEP full year valuation; screen energy and industrials (e.g. CAT, XOM) ; compare paper prices to VTI.

## Universe screen (added 2026-11-06)
tools/screen_universe.py pulls SEC XBRL "frames" for every U.S. filer in seconds and writes data/screen_latest.csv.
First run (CY2025 data): 4,392 filers with revenue; 2,019 with complete data; 824 passed the basic quality filter.
Limits: U.S. SEC filers only (no non-U.S. exchange coverage); fundamentals only, no prices or valuation; some rows are distorted
by one-off revenue (e.g. biotech collaboration payments), so stage 2 must check each name before it is trusted.
Pipeline: stage 1 screen all filers -> stage 2 add price and valuation for the top ~50 -> stage 3 read filings for the top few -> morning compile.

## Authoritative operational handoff, method 2.0, 2026-11-06
Read RESEARCH_WORKFLOW.md and the latest dated records before following older handoffs.
The single-source VTI value mentioned above remains unverified and must not become a performance baseline.
Old markdown ratings are historical method 1.0 notes, not validated method 2.0 candidates.
The four hour worker repository attachment has been fixed. Both tasks must explicitly fetch and use claude/hopeful-hamilton-8b3avz before reading state.
Refresh the updated annual screener when metadata is missing or older than 24 hours. Its new counts may be lower because missing capex and mismatched fiscal periods are now excluded.
Next: validate the updated screener in a live worker, research one existing candidate into the structured template, run its quality checks, and prioritize unresolved evidence over adding more shallow names.
Sunday compilation includes a recorded quality review. A separate weekly ChatGPT audit will inspect actual outputs and propose or test bounded improvements.

## Worker run 2026-11-06 00:30 ET (method 2.0)
- Branch claude/hopeful-hamilton-8b3avz fast-forwarded and used. Screen refreshed (CY2025): 4,392 filers with revenue, 1,142 comparable rows, 419 preliminary passes; many exclusions are missing capex (1,029+) and mismatched dates. Not global, not valuation.
- Researched in depth: USLM and EXEL (both watch, medium confidence, scores incomplete). Third name not finished: Qualys has no Q3 10-Q yet.
- Blocker: no second independent quote origin reachable (stooq 404; only stockanalysis.com gave a dated close). Benchmark still pending; no paper references created for these names.
- Validator results saved to data/quality_latest.json. Queue is in journal/queue.md; decisions in journal/decision_log.jsonl.
- Next: get a second quote origin, read the EXEL and USLM earnings releases, watch EXEL November '039 trial outcome, then QLYS after its 10-Q.

## Worker run 2026-11-06 ~04:30 ET (method 2.0, run 2)
- Screen not refreshed (last refresh 00:26 ET, under 24 hours). QLYS still has no Q3 10-Q.
- Researched IDCC and MEDP (both watch, medium, scores incomplete). Closed the second-quote gap for USLM and EXEL: stockanalysis.com and Yahoo Finance agree on 2026-11-05 closes (publisher-level independence only). Benchmark VTI still pending; no paper references created.
- Validator: all four records valid, none attractive-eligible (data/quality_latest.json).
- Not done: FSLR; earnings release exhibits (IDCC, MEDP, USLM, EXEL); peer multiples; MEDP and IDCC annual filing financials.
- Next: FSLR valuation, QLYS after 10-Q, read releases, EXEL '039 ruling, cause of IDCC drop.

## Worker run 2026-11-06 ~08:15 ET (method 2.0, run 3)
- Screen not refreshed. Researched FSLR only (watch, medium, scores null; valid, not attractive-eligible). 11.3x TTM earnings, FCF yield 1.1%, 45X dependent. Benchmark pending; no paper references.
- Next: FSLR MD&A and 10-K, QLYS after 10-Q, AGX valuation, release exhibits for IDCC/MEDP/USLM/EXEL, EXEL '039 ruling.

## Morning compile 2026-11-06 09:09 ET
Report reports/2026-11-06-090906.md (also latest.md). All five records revalidated (data/quality_compile_2026-11-06.json), none attractive eligible. EXEL release read; no new 8-Ks for EXEL or IDCC. Next: IDCC release and drop cause, EXEL tax normalization and '039 ruling, QLYS 10-Q, second quote source.

## Worker run 2026-11-06 ~12:20 ET (method 2.0, run 4)
- Screen not refreshed (about 12 hours old). Researched AGX (watch, medium, scores null; valid, not attractive-eligible). IDCC release read: gap closed. QLYS still has no Q3 10-Q or earnings 8-K.
- AGX fell 27% from 10-29 to 11-05 (cause unconfirmed); 20.4x TTM earnings, but FCF yield of 14.9% is inflated by customer advances. Benchmark VTI still pending; no paper references.
- Next: AGX peer multiples and MD&A, QLYS after 10-Q, FSLR 10-K, EXEL '039 ruling, USLM/MEDP releases, a second quote origin that is truly independent.

## Worker run 2026-11-06 ~16:40 ET (method 2.0, run 5)
- Screen not refreshed (~16 hours old). QLYS still has no Q3 10-Q. Researched TW (watch, medium, scores null; valid, not attractive-eligible; 28.7x TTM, FCF yield 3.65%, Trumid 1.97B deal). CPRX screened out (acquired by Angelini). Two quote publishers agree on the TW 11-06 close; benchmark VTI still pending; no paper references.
- Next: TW peer multiples and Trumid 8-K, QLYS after 10-Q, AGX peers, FSLR 10-K, EXEL '039 ruling, a truly independent quote origin.

## Worker run 2026-11-06 ~20:10 ET (method 2.0, run 6)
- Screen not refreshed (~20 hours old). QLYS still has no Q3 10-Q. Researched UTHR (watch, medium, scores null; valid, not attractive-eligible). 19.5x TTM, FCF yield 3.6%, flat 9M revenue; Q4 will include +330.4M Liquidia gain and -525M Arena charge. Quote 562.32/562.02 (11-06). Benchmark VTI still pending; no paper references.
- Next: UTHR peers, drop cause and PDUFA dates; QLYS after 10-Q; TW/AGX peers; EXEL '039 ruling; truly independent quote origin.

## Worker run 2026-11-07 ~00:07 ET (method 2.0, run 7)
- Screen not refreshed (about 24 hours old at the boundary; refresh on next run). QLYS still has no Q3 10-Q. Researched KNSL (insurer, 16.4x TTM, 4.5x book, premiums -3.5%) and MPWR (65x TTM, FCF yield 1.05%, revenue +46.5%): both watch, medium, scores null, valid, not attractive-eligible (data/quality_run7_*.json; all 10 JSON records revalidated in data/quality_latest.json).
- Benchmark VTI still pending; no paper references. Only one quote origin type found (stockanalysis.com and Yahoo agree, publisher-level independence).
- Next: refresh screen if older than 24h; peers for KNSL/MPWR/TW/AGX/UTHR; read KNSL and MPWR release exhibits; QLYS after 10-Q; EXEL '039 ruling; energy, utilities and bank sector names still uncovered.

## Worker run 2026-11-07 ~04:10 ET (method 2.0, run 8)
- Screen refreshed 04:05 ET (previous 27 hours old): 4,393 filers with revenue, 1,142 comparable, 419 preliminary passes. QLYS still has no Q3 10-Q.
- Researched DTM (midstream) and GMED (medtech): both watch, medium, scores null, valid, not attractive-eligible (data/quality_run8_*.json). DTM 24.6x TTM, FCF yield 4.6%; GMED 16.9x TTM, FCF yield 8.1% after a 12.8% drop on a revenue guidance cut.
- Benchmark VTI still pending; no paper references. Quote origins are two publishers only.
- Next: peers for DTM/GMED/KNSL/MPWR/TW/AGX/UTHR; GMED call commentary; QLYS after 10-Q; EXEL '039 ruling; banks, utilities, REITs, consumer names uncovered.

## Worker run 2026-11-07 ~08:10 ET (method 2.0, run 9)
- Screen not refreshed (refreshed 04:05 ET). QLYS still has no Q3 10-Q.
- Researched CARG (consumer internet) and VCTR (asset manager): both watch, medium, scores null, valid, not attractive-eligible (data/quality_run9_*.json; all 14 JSON records revalidated in data/quality_latest.json). CARG 16.0x TTM, FCF yield 10.0%; VCTR 21x TTM, FCF yield 6.4% but a pending 7.03B First Eagle deal makes trailing numbers unrepresentative.
- Benchmark VTI still pending; no paper references. Quote origins are two publishers only.
- Next: VCTR deal financing; peers for CARG/VCTR/DTM/GMED/KNSL/MPWR/TW/AGX/UTHR; CARG drop cause; QLYS after 10-Q; EXEL '039 ruling; banks, utilities, REITs uncovered.

## Morning compile 2026-11-07 ~09:15 ET
Report reports/2026-11-07-090707.md. 14 records revalidated (data/quality_compile_2026-11-07.json), none eligible. No new filings for GMED, CARG, EXEL, QLYS (no Q3 10-Q). EXEL 11-06 close 69.57. Sunday review due 2026-11-08. Next: peers, GMED/CARG call commentary, EXEL 039 ruling, QLYS, uncovered sectors.

## Worker run 2026-11-07 ~12:10 ET (method 2.0, run 10)
- Screen not refreshed (refreshed 04:05 ET). QLYS still has no Q3 10-Q.
- Researched NMIH (mortgage insurer) and GABC (regional bank): both watch, medium, scores null, valid, not attractive-eligible (data/quality_run10_*.json). NMIH 7.4x TTM, 1.08x book, -11.8% on 11-06 (cause unconfirmed); GABC 12.9x TTM, 2.5x tangible book, strong credit. 10-Ks and GABC release not read.
- Benchmark VTI still pending; no paper references. Quote origins are two publishers only.
- Next: peers for NMIH/GABC and earlier names; NMIH drop cause; QLYS after 10-Q; EXEL '039 ruling; utilities and REITs uncovered.
