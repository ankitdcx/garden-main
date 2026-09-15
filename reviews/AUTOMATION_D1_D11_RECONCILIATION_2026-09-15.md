# Additional automation audit — 15 September 2026

All eleven supplied findings were reconciled against both repositories. Public repair PR #176 merged as `12c973e2b22f97dec57e1d87d55ba5a9410598ca`, after integrity, constitutional guard and integration-provenance checks passed. Local verification passed 80 tests, bounded GSL conformance and 295 repository references with zero unresolved links. Provider tests used mocks; the Coordinator remains paused.

The complete per-finding disposition and exact remaining conditions are maintained in [the public D-1–D-11 report](https://github.com/ankitdcx/garden-swarm/blob/main/docs/AUTOMATION_AUDIT_D1_D11_2026-09-15.md). Existing issues #148, #75, #65, #66 and #137 were updated rather than duplicated or closed prematurely.

## Confirmed repairs

- All six provider workflows are dispatch-only, share one concurrency group, and fail before provider calls while paused. Legacy multi-call workers stay blocked pending a qualified incremental dispatcher.
- Free, paid and origin-inventory batches stop after the first failed provider response and preserve partial evidence.
- Budget pools explicitly represent the initial $20 lifetime allocation, constrained by $1/day. Current remaining balance is unknown, not invented. Shared execution caps and cycle diversity targets are distinct.
- Free-swarm, specialist and execution policy fields now participate in producer/consumer fingerprints.
- Hourly inline boundary assertions are extracted into a registered, tested check that remains active under Python optimization.
- A read-only CI aggregate rejects missing, wrong-head, failed or superseded successful run evidence. Its claim is limited to its three named repository workflows.
- Public paused-status and 266-section denominator receipts are published without inventing dispatch successes or qualified reviews.

## Corrections to the supplied review

The private repository already implements CycleBinding, ProcessFactory/GardenProcess, route and transition receipts, required_gates and restoration from a receipt prefix. The section inventory/count generator already exists. Public CI already emits a bounded CIConformancePipelineReceipt. The supplied claims of their total absence were incorrect; the real gaps are durable integration, observability and aggregate scope. Not all workflows were dispatch-only: normal test/guard CI remains event-triggered, and two residual provider push triggers were found and removed.

## Work still open

1. Durable single-review dispatch, claim/lease ownership, cooldown/resume and Coordinator-to-engine receipt integration (#148/#138/#114).
2. Global atomic spending/free-quota reservations and ambiguous-charge reconciliation (#75).
3. Protected dependency-list and integrity-artifact migration. The exact unapplied candidate is in the public report. Existing CHANGE_POLICY requires external/trusted-base approval verification; this repair does not supply or bypass that verifier (#66/#77).
4. Durable selected CI/release evidence publication and enforced aggregate branch-protection integration (#65/#52). An aggregate artifact alone does not enforce a merge gate.
5. Genuine qualified/stale section review ledger, independent review and a complete successor package (#137 and existing WP-005/WP-006).
6. Full newer project transcripts. The broader keyword/excerpt history pass and its limits remain as recorded in the earlier reconciliation; no new exhaustive-history claim is made.

User action is not required for each small repair. Keep the pause until the resumable/budgeted path is qualified and the user directs resumption. Repository protection and protected promotion/approval boundaries remain the specific external controls requiring user/admin participation.
