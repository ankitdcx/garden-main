# Garden v15.6 Design Delta Ledger

`DELTA_LEDGER.json` is the machine-readable per-delta tracking layer for the v15.6 successor line.

The older `DELTASET-*.json` files remain authoritative source artifacts for the detailed candidate text they already contain. The ledger does not rewrite or ratify them. Instead, each candidate/delta receives a `DeltaRecord/v1` carrying lifecycle state, provenance, semantic-impact status, blind-review/cross-exam links, reviewer-family quorum status, Challenger status, and canonical-effect boundary.

## Admission-readiness boundary

The historical `admission_eligible` boolean is retained only as a migration/process-candidacy marker. It is **deprecated and non-authorizing**. It MUST NOT be interpreted as proof that a delta is ready for successor admission.

Current readiness is derived fail-closed by normative rule `RULE-DELTA-ADMISSION-FAIL-CLOSED`, executable check `CHECK-DELTA-ADMISSION-READINESS`, implemented by `tools/validate_delta_ledger.py`. The check emits a typed `DeltaAdmissionReadinessReceipt/v1` bound to the exact repository commit, Garden predecessor version, DesignEpoch reference, ledger SHA-256, and per-delta blocking reasons.

A delta can report `ready=true` only when all of the following are true:

- lifecycle state is `ACCEPTED` or already `ADMITTED_FOR_SUCCESSOR`;
- semantic impact is resolved to `YES` or `NO` and has an assessment receipt reference;
- independent review quorum is `SATISFIED` with at least three reviewer families, at least three blind-review references, and at least three cross-examination references;
- no evidence conflict remains `UNRESOLVED`;
- Challenger status is `PASS` with a Challenger receipt reference;
- `canonical_effect` remains `false`.

Unknown, missing, insufficient, pending, challenged, escalated, or unresolved assurance state is therefore mechanically not ready. The legacy candidacy marker cannot override this derived result.

## Required flow for new hourly design findings

1. Finding is recorded and evidence-bound.
2. If it is a plausible semantic design candidate, create/update one `DeltaRecord/v1` in `DELTA_LEDGER.json`.
3. Populate `SemanticImpactAssessment` reference when performed.
4. Populate blind-review and cross-examination references; never infer quorum from model count without valid evidence.
5. Populate Challenger decision where required.
6. Run the fail-closed readiness check bound to the exact repository commit.
7. Only transition to `ADMITTED_FOR_SUCCESSOR` when the typed readiness receipt reports `ready=true` for that delta and all external Garden/GSL gates also pass.
8. Daily materialization consumes only admitted records; tracking alone has no canonical effect.

Legacy grouped candidates migrated on 2026-09-14 retain their original source status and begin conservatively at `PROPOSED` or `DEFERRED` unless the source explicitly established otherwise. Migration does not manufacture missing review or Challenger evidence.

Validation:

```bash
python tools/validate_delta_ledger.py --repository-commit <exact-40-hex-commit>
python -m unittest tests.test_delta_ledger -v
```

CI: `.github/workflows/delta-ledger-ci.yml`. CI binds the readiness receipt to `${GITHUB_SHA}`. A structural PASS does not ratify a design delta or lift any active freeze by itself.
