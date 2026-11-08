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

## 2026-11-08 independent audit

Fixed stale quote eligibility when an old record is revalidated. Reproduced with a failing regression, then all 26 tests passed; all 26 saved real records remained structurally valid and none attractive-eligible. Three specific financial claims were checked against primary filings. Remaining priorities: annual filing versus XBRL provenance, independent quote origins, peer/accounting gaps and honest depth counts. Full evidence: reviews/2026-11-08-independent.md. Rollback versions of the two changed code/test files are at 85d19726c0ce76bf8a5f9001641a04fb48361d48; restore through a new commit, never a reset. No strategy thresholds or task cadence changed.

## 2026-11-08 compiler review
Validator no longer counts XBRL or submissions API URLs as the annual filing read (evidence: five records labelled companyfacts as annual_filing). Regression test added; 27 tests pass; 26 records still valid, 0 eligible. Rollback reference 50e22e01ab5b519a4a389f03310742cd5754d604 for tools/validate_research.py and tests/test_research_quality.py. Details in reviews/2026-11-08.md.
