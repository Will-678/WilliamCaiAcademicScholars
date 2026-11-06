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
