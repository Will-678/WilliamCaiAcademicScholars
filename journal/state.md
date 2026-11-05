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
