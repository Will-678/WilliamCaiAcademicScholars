# Independent audit, 2026-11-15

Snapshot: e71a5351372e70d2ca5fe66acea0cd34c61cc2d9. Reviewed the seven saved daily reports November 8 through 14, AGENT.md and workflow, all 105 company JSON records and companion notes, 117 decision entries, queue/state handoffs, improvements and prior audits, screening metadata, saved validation outputs and code/tests. The November 15 morning report was not yet present at this snapshot.

## Finding and correction
Different publisher labels were sufficient to satisfy the quote origin count, despite repeated report admissions that underlying feed independence was unproven. A complete synthetic attractive record with two different origin strings but no origin documentation passed. A new regression failed before the change.
The validator now counts a quote toward independent confirmation only when its source explicitly records origin_verified=true and an HTTPS origin_evidence_url, in addition to existing agreement, currency, timestamp and distinct-origin checks. Updated positive fixtures represent documented synthetic origins. Workflow explains that humans/agents must actually check that evidence; the boolean and URL do not prove factual truth.

Validation: baseline 27 tests passed; the new regression failed before the fix; all 28 tests passed after. Revalidated all 105 current records with the updated checker: 105 structurally valid, zero attractive-eligible, with 103 watch, one avoid and one insufficient_evidence. All totals remain incomplete. No source flags or ratings were fabricated or backfilled.

## Three primary-source spot checks
Matched the records' specific figures against actual financial material:
* ADMA Q3 revenue $141.1M, ASCENIV $124.7M and GAAP net income $49.9M: https://www.sec.gov/Archives/edgar/data/1368514/000114036126041959/ef20084542_ex99-1.htm
* Federal Signal Q3 sales $655.5M versus $555.0M, in USD millions: https://www.sec.gov/Archives/edgar/data/277509/000162828026068175/fss-20260930.htm
* Philip Morris Q3 net revenues $11,438M and operating income $4,866M: https://www.sec.gov/Archives/edgar/data/1413329/000162828026066976/pm-20260930.htm
These checks support only those claims. They do not validate every calculation, price, adjustment or investment thesis.

## Progress and unresolved weaknesses
The prior validation-clock freshness fix remains present, as does the compiler's exclusion of XBRL API URLs from annual-filing reading credit.
Coverage expanded from 26 records at the previous independent audit to 105. Saved reports repeatedly carry the same three leaders and unresolved peer/accounting/source gaps. More files have not produced completed diligence or a complete score. Added an explicit worker reporting requirement for an existing leader's priority gap, attempt and outcome before new leads.
Latest annual screen: 4,397 supported revenue filers, 1,142 comparable rows, 419 preliminary passes, refreshed November 14 at 20:04 Eastern. Annual US GAAP USD scope, exclusions and two fallback-tag 404s are disclosed. This is not global coverage or current-quarter filing review.
The November 14 summary accurately called validation structural, preserved null scores and identified unsupported quote independence. Some individual notes still label companyfacts as annual_filing while admitting the text was not opened; the existing API exclusion prevents those entries satisfying annual-reading credit. Do not describe them as full annual filing reads.
Period/unit arithmetic checks are useful but do not normalize working capital, one-off taxes, acquisitions, equity gains or stock compensation automatically. Peer sets, MD&A and relevant notes remain incomplete. In PM's countercase, avoid adding interest again to FCF-based coverage because operating cash flow generally already reflects cash interest; reconcile classifications before using a debt-service comparison.
The benchmark remains unverified, no usable post-publication paper references are established and no 30-day observation horizon exists for these November ideas. No outperformance conclusion is justified.
Saved worker artifacts and queue show continued progress through run 56; actual scheduler failures and usage outside the repository were not independently inspected. Prior source-access restrictions must be respected. No browser, brokerage, credential or paid-data access was used.

## Rollback and boundaries
Restore only this audit's validator, test and workflow changes from e71a5351372e70d2ca5fe66acea0cd34c61cc2d9 through a new corrective commit if needed, preserving subsequent research. Never reset or force push. Weights, thresholds, task cadence, access and personal portfolio preferences are unchanged.
