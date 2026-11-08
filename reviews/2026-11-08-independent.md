# Independent research audit, 2026-11-08

Reviewed branch head 85d19726c0ce76bf8a5f9001641a04fb48361d48. Scope: all saved reports from November 4 through November 7 (the available portion of the requested seven days), 26 structured company records and their notes, 32 decision-log entries, queue and state handoffs, standing instructions, workflow, screening metadata, saved validation results, tools and tests. No November 8 morning report was present at the audited head.

## Applied correction
The quote freshness test compared quote time only with the record's original as_of. A historically complete attractive fixture still passed on November 20 with a November 5 quote. Reproduced the failure with a regression test before changing code.
Added a separate seven-calendar-day maximum quote-age check against the actual validation clock. Existing snapshot chronology checks remain. Historical records remain readable but cannot stay promotion-eligible indefinitely. This is the existing freshness limit applied at validation time, not a new score threshold or a market-session calendar.

Validation: original 25 tests passed; new regression failed before the fix; all 26 tests passed after. All 26 saved real records passed structural validation before and after; none was attractive-eligible. This does not establish factual correctness.
Rollback reference: 85d19726c0ce76bf8a5f9001641a04fb48361d48. Restore only tools/validate_research.py and tests/test_research_quality.py from that commit through a new corrective commit if needed; never reset the branch or discard subsequent research.

## Three primary-source spot checks
1. Zoetis Q3 2026 net income of $591 million and diluted EPS $1.44 agree with its November 5 earnings exhibit:
https://www.sec.gov/Archives/edgar/data/1555280/000155528026000048/exhibit99q32026.htm
2. Corcept Q3 revenue of about $340.5 million agrees with the 10-Q's $340.472 million, versus $207.638 million in Q3 2025:
https://www.sec.gov/Archives/edgar/data/1088856/000162828026069501/cort-20260930.htm
3. USLM cash of about $439.2 million agrees with the September 30 balance sheet's $439.248 million:
https://www.sec.gov/Archives/edgar/data/82020/000110465926120712/uslm-20260930x10q.htm
These spot checks support those specific claims only, not the complete investment theses.

## Research quality and remaining issues
The latest annual screen was refreshed November 8 at 04:05 Eastern: 4,393 supported revenue filers, 1,142 comparable rows, 419 preliminary passes. It clearly discloses annual US GAAP USD scope, exclusions, lack of valuation and two fallback-tag 404s. This is not global coverage.
Worker history progressed through run 15 and has diversified across sectors. It repeatedly adds new watch entries while peer comparisons, accounting reviews, annual filing reading and quote independence stay incomplete. Prioritize closing those gaps over adding more shallow names. Repeated QLYS checks could be consolidated around an issuer-confirmed event without changing cadence.
Some companyfacts API sources are mislabelled annual_filing (including ZTS and CORT). Numeric XBRL retrieval is not evidence that the annual filing's business and risk sections were read. Two quote publishers are also not proof of independent underlying feeds. Keep both explicit limitations; do not turn structural validity into the phrase fully sourced, as the November 7 summary did.
The benchmark remains pending and no usable post-publication stock/benchmark paper references were demonstrated. No elapsed-horizon performance or investment edge claim is supported.
State documents one blocked attempt to change a user-agent after SEC download refusal. It reports abandoning the attempt and using permitted alternatives. Respect source access restrictions; do not retry by disguising traffic.
No cadence, credentials, portfolio preferences, score weights, permissions or paid services changed. Future scheduled execution and task failures outside saved repository artifacts were not independently inspected.
