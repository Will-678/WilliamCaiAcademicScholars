# Independent research quality review, 2026-11-22

Snapshot: 63e83404f25a9bd28cb5003744d40d39ddc8d9a2, branch claude/hopeful-hamilton-8b3avz. This reviews the existing bot, not stock selections.

## Scope and results

Read standing AGENT.md and RESEARCH_WORKFLOW.md, the seven morning reports November 15 through 21 (November 22 morning compilation had not yet been saved), current company JSON/markdown records, queue/state, decision history, improvement history, screen metadata, latest and per-run validation outputs, screener, validator and tests. Retrieved 658 relevant text files; historical records and decisions remain intact.

Re-executed validation over all 188 structured records: 188 structurally valid, zero eligible attractive. All 188 scores/totals remain incomplete; statuses are 184 watch, two avoid, two insufficient_evidence. These are incomplete research records, not 188 completed deep reviews. All 188 have the independent quote-origin blocker; 179 lack the required annual document plus a distinct recent document. Data API facts do not count as reading a 10-K. Structural validation proves neither factual accuracy nor source support.

The November 21 annual screen reports 4,404 supported revenue filers, 1,142 comparable rows and 419 preliminary passes. Its USD/US GAAP scope, missing capex exclusions, flow/balance date checks and lack of current valuation coverage remain disclosed. Two SalesRevenueNet frame requests returned 404. No inference of global or current-quarter coverage is justified. Missing fields stay unknown, not zero.

## Reproducible defects and applied correction

The persisted queue contains 190 historical rows, 94 overdue as of November 22, 95 rows with at least one flagged issue, two old quote-verification assertions (USLM and EXEL) contradicted by current recorded quote evidence, and one markdown-only entry (CPRX) without a structured record. Rows are not unique-company counts. The header also understates how recently additions occurred. Reusing queue prose can bypass the caution correctly expressed in company records.

Added tools/queue_quality.py and three regression tests, then added a required workflow checkpoint. The read-only check reports overdue rows, missing JSON and quote assertions inconsistent with the existing validator's independent-origin requirement. It does not invent source proof, alter ratings, choose investments or erase queue history. A successful check still cannot prove a quote true. Exit 1 exposes issues while allowing useful research to continue.

Baseline: 28 Python unittest tests passed. New test initially reproduced missing queue protection via ModuleNotFoundError. After implementation, 31 tests passed, including stale assertions, missing legacy records, nonmutation and acceptance of the documented-origin previous-close fixture. Live execution found the counts above. All 188 company JSON records also passed the existing structural validator on this review's clock. No new evidence standards or investment weights were introduced.

## Three primary-source checks

* HubSpot: the September 30, 2026 10-Q income statement reports Q3 revenue USD 947,565 thousand and nine month revenue 2,740,301 thousand. These support the record's rounded USD 947.6M and 2,740.3M claims. https://www.sec.gov/Archives/edgar/data/1404655/000119312526447363/hubs-20260930.htm
* Trex: the September 30, 2026 10-Q reports Q3 sales USD 359,504 thousand versus 285,348 thousand, up 26.0%, and gross margin 36.0% versus 40.5%. These support the record's operating claims. https://www.sec.gov/Archives/edgar/data/1069878/000119312526447251/trex-20260930.htm
* NVR: the September 30, 2026 10-Q reports nine month OCF USD 412,096 thousand, PP&E purchases 29,879 thousand and treasury stock purchases 1,242,774 thousand. FCF under the record's definition is 382,217 thousand. Buybacks divided by FCF is 3.2515 times, not the thesis's 1.8 times. Appended a correction to NVR.md and the decision log, preserving the original research snapshot and watch decision. https://www.sec.gov/Archives/edgar/data/906163/000090616326000104/nvr-20260930.htm

These checks address the stated periods, USD units and specific claims only. Other prose arithmetic is not checked by the structural validator, which validates a structured FCF object when supplied; the NVR narrative ratio demonstrates the remaining limitation. Proposed next process improvement: encode consequential derived ratios as explicit sourced inputs and tested calculations instead of relying on prose arithmetic. Do not treat this proposal as already implemented.

## Remaining research blockers

The watchlist grew from 105 structured records at the prior independent review to 188, while no score became complete. ZTS, GMED and CARG remain compilation leaders with annual/history, earnings-call, accounting/reconciliation and peer gaps. Later workers document attempts at the EXEL ruling gap, but repeated SEC submissions polling closes no evidence gap and does not establish the ruling's absence. The prior workflow requirement improved attempt disclosure; it has not demonstrated completed diligence.

Quote publishers agreeing does not establish independent origins. No quote was promoted or newly verified here. Current filing access for the three sampled records succeeded; earlier HUBS/TREX failures are preserved in state and later direct archive retries succeeded. A successful retry does not erase the failed attempt. Full latest-filing coverage for every company was not independently re-established.

No legacy record was observed promoted to attractive. CPRX remains markdown-only and must be validated before compiler promotion. Queue dates and old valuation statements remain historical context until rechecked. Benchmarks and post-publication paper references remain pending; the oldest research is under 30 days old, so no matching 30/90/180/365-day performance assessment or outperformance claim is available. No returns were estimated.

## Change control and rollback

The shared branch head was rechecked before creating the update; use an expected-head, non-forced fast-forward update. Preserve unrelated files, dated reports and decisions. Rollback reference is 63e83404f25a9bd28cb5003744d40d39ddc8d9a2: revert this audit's commit in a new commit, never reset the shared branch. This run changes only the queue diagnostic/tests/workflow, appends the NVR correction and decision, and saves this review and improvements entry. No portfolio preferences, cadence, permissions or score thresholds changed.
