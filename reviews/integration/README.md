# Garden integration admission records

The integration layer is itself reviewable. A model finding does not become an accepted Garden finding merely because an integrator agrees with it.

## Required chain

`candidate finding -> IntegrationDecisionReceipt -> challenger audit -> test/commit or admitted design delta -> ledger`

Every substantive disposition MUST have a stable `finding_id` and `decision_id`. The authoritative receipt shape is `decision.schema.json`.

## Canonical absence / coverage claims

Claims equivalent to "Garden lacks X" or "Garden already covers X" require a deterministic whole-source trace generated from all five current canonical files. Use `scripts/search_canonical.py` with the direct term plus relevant synonyms, identifiers, invariant/test IDs, and alternative spellings. Record the resulting source hashes and line hits in `evidence.whole_source_search_trace`.

A zero lexical-hit result is not semantic proof of absence. It must be combined with obligation/reference evidence and the uncertainty field must say what could still have been missed.

## Independent reproduction

HIGH/CRITICAL findings and substantive semantic design deltas require an independent same-question reproduction attempt from a different model family when an admissible route is available. Agreement is evidence, not proof; disagreement stays visible.

## DO_NOTHING

Any semantic design change must compare the proposed delta against retaining the predecessor unchanged. `ACCEPT_DESIGN_DELTA_CANDIDATE` is invalid without a concrete `do_nothing_comparison`.

## Challenger

Challenger receipts do not silently overwrite integration decisions. They link to the original decision, state the attempted falsification, and either confirm the decision or leave an explicit disagreement that blocks semantic promotion when material.

## Successor drift

Successor materialization requires an admitted delta manifest and `scripts/check_successor_drift.py`. The candidate is valid only if every observed per-file unified diff exactly matches the previously admitted expected diff hash. Unexplained text drift is a materialization defect, not an improvement.
