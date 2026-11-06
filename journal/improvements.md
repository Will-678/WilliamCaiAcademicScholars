# Research process improvements

## 2026-11-06, method 2.0
Baseline research branch commit: a088cc2010af702963bcf176fdc456afe1d7ffd8.
Reason: the first reports and screener revealed reproducible data and provenance weaknesses.

Implemented:
* Missing capital spending stays missing, rather than becoming zero free cash flow spending.
* Flow periods and balance dates must align; dates, tags and accessions remain attached.
* Zero denominators, conflicting revenue tags, nonfinite facts and tiny equity are handled explicitly.
* The numeric screen has coverage metadata and is labelled an annual preliminary ranking.
* Structured research records and a deterministic promotion checker block unsupported attractive ratings.
* Quote agreement, underlying source independence, score sums and cash flow arithmetic are checked.
* A documented queue, countercase, staged valuation, immutable reports and decision history guide both tasks.
* Unconfirmed historical benchmark references remain pending.
* Sunday quality reviews and an independent weekly audit support continuing improvement.

Validation: 25 offline regression tests passed using synthetic fixtures. The blank research template is a valid incomplete draft and is blocked from promotion. No fixture represents a real recommendation.
Live source access and a worker run must be checked separately; offline success does not establish investment performance or source truth.
Preserve the existing portfolio preferences and schedule. Do not weaken requirements or tune scores to a few winners.

## Live verification completed, 2026-11-06

The corrected four hour worker finished and pushed its output in commit d64beccea270fe2b6b1b5ffc54516dfe90d64f14.
The live annual screen observed 4,392 revenue filers, 1,142 comparable rows and 419 preliminary passes. The reduction from the earlier screen reflects exclusions for missing spending, mismatched periods and other disclosed gaps, not a change to the market.

The worker saved EXEL and USLM markdown and structured records, a persisted queue, decisions and validation results. Both records passed the structural/arithmetic checker but remained ineligible for an attractive label. Missing independent quote confirmation, incomplete valuation and accounting review remained explicit; total scores stayed null. The benchmark stayed pending and no paper reference was fabricated.
The two saved records were independently fetched from GitHub and rechecked with the published validator locally, exit code 0, with the same promotion blockers.

The repository attachment and both method 2.0 task briefs are saved. An independent weekly ChatGPT quality review is enabled for Sunday mornings, in addition to the compiler's documented Sunday retrospective.
Remaining: observe the next morning compilation and future scheduled runs; finish missing source evidence; expand international coverage only when reliable authorized data exists. No investment edge or performance claim is established.
