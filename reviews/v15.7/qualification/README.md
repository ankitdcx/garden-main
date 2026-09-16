# v15.7 qualification obligations

This is an evidence snapshot and pending-work register. It does not declare all pending work complete or promote a canonical release.

Accounted for: **20 engineering profiles, all 38 individual user work items, 174 inherited queue dispositions, six v15.7 programs, seven cognitive functions, seven baseline matching axes, ten comparator scopes and eleven design-decision rows**. There are 328 register rows.

| Status | Register rows |
|---|---:|
| DEFERRED | 10 |
| IMPLEMENTED | 5 |
| PARTIAL | 95 |
| SPECIFIED | 218 |

Five IMPLEMENTED rows concern only the named finite model or reference-simulation deliverable. PARTIAL means useful work exists and material obligations remain. Source blocks retain their exact text/span/hash, including metadata; accounting rows are not independent defects.

The following executed receipts are present and inspected:

- `recovery-model/TLC-RECEIPT.json`: bounded TLA+ exploration and a disabled-fence counterexample.
- `recovery-runtime/RUNTIME-RECEIPT.json`: local SQLite permission, fencing, crash and uncertain-effect recovery.
- `release/release-verification-receipt.json`: real upstream TUF/in-toto verification on signed local fixtures, including invalid inputs, rollback and authorized key rotation.
- `physical/physical-assurance-receipt.json`: scalar tank trajectories, timing assumptions, unsafe-delay counterexample and assurance-loss recording.
- `context-routing/context-routing-receipt.json`: local provenance, freshness, contradiction, routing and budget scenarios with zero live provider calls.

These receipts do not establish distributed recovery, hardware safety, full STPA, production trust, total-root-compromise recovery, live cognitive capability, provider cost savings or independent model-family review quorum. `TRUST-CONSISTENCY-ANALYSIS.md` is linked to items 31–35 and deferred product choices 37–38; it describes present reference boundaries and missing production adapters.

FunctionContract registries bind **selected methods only**. Unlisted or unbound public functions remain **FRONTIER**; no neighboring method receipt closes them automatically. Complete callable-surface inventory and affected per-function qualification remain required.

Files in this accounting package:

- `OBLIGATION-REGISTER.json`: every item, owner, current/anticipated evidence and next action.
- `COGNITIVE-FUNCTION-DISPOSITIONS.json`: seven existing source interfaces; concrete algorithms and qualification remain unresolved.
- `BASELINE-MATCHING.json`: B0/B1/B2 matching plan and claim limitations; no matched live trials.
- `COMPARATOR-SCOPES.json`: ten fixed scopes; all external artifact pins unresolved, with concrete resolution work.
- `DESIGN-DECISION-ROWS.json`: no-addition/smaller/full decisions without measured superiority claims.

Temporal, seL4 and incompletely defined historical profiles remain explicitly deferred. Canonical v15.5 remains the authority baseline. The v15.7 working-candidate source root is bound as a source identity, not an accepted DesignEpoch.

Snapshot revision: **2026-09-16-accounting-freeze-1**. Evidence hashes were checked when recorded; model/runtime checker work and independent review may still update files after this snapshot. Before publication or admission, refresh each changed receipt by rerunning its qualification, verify its source bindings, and then refresh the register hash. Merely replacing a stale hash is not requalification.
