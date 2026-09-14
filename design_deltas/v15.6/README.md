# Garden v15.6 Design Delta Ledger

`DELTA_LEDGER.json` is the machine-readable per-delta tracking layer for the v15.6 successor line.

The older `DELTASET-*.json` files remain authoritative source artifacts for the detailed candidate text they already contain. The ledger does not rewrite or ratify them. Instead, each candidate/delta receives a `DeltaRecord/v1` carrying lifecycle state, provenance, semantic-impact status, blind-review/cross-exam links, reviewer-family quorum status, Challenger status, and canonical-effect boundary.

## Required flow for new hourly design findings

1. Finding is recorded and evidence-bound.
2. If it is a plausible semantic design candidate, create/update one `DeltaRecord/v1` in `DELTA_LEDGER.json`.
3. Populate `SemanticImpactAssessment` reference when performed.
4. Populate blind-review and cross-examination references; never infer quorum from model count without valid evidence.
5. Populate Challenger decision where required.
6. Only transition to `ADMITTED_FOR_SUCCESSOR` when the ledger validator's admission conditions are satisfied and all external Garden/GSL gates also pass.
7. Daily materialization consumes only admitted records; tracking alone has no canonical effect.

Legacy grouped candidates migrated on 2026-09-14 retain their original source status and begin conservatively at `PROPOSED` or `DEFERRED` unless the source explicitly established otherwise. Migration does not manufacture missing review or Challenger evidence.

Validation:

```bash
python tools/validate_delta_ledger.py
python -m unittest tests.test_delta_ledger -v
```

CI: `.github/workflows/delta-ledger-ci.yml`.
