# Minimal Garden Implementation Kernel — WP-001..004

Status: **NON-CERTIFIED REFERENCE IMPLEMENTATION**.

This stdlib-only package implements a deliberately small subset of the first four private Garden work packages. It does not claim to implement all of GSL, prove Garden, or certify any deployment.

## Components

- `garden_kernel/core.py` — typed CLAIM/CONTEXT/value/dependency/obligation/receipt subset; unsupported fields fail explicitly.
- `garden_kernel/extractor.py` — conservative source-to-obligation extractor; unsupported structured records become unresolved `GapRecord`s rather than silent omissions.
- `garden_kernel/store.py` — SQLite claim/evidence/dependency/correction store; storage or repetition cannot promote epistemic status without an explicit admitted transition.
- `garden_kernel/verifier.py` — typed verifier registry and receipts; verifier class, implementation hash, artifact hash and DesignEpoch remain explicit; unprotected candidate verifiers cannot issue admission receipts.
- `tests/test_kernel.py` — positive/negative deterministic fixtures.

## Run

```bash
PYTHONPATH=implementation python -m unittest discover -s implementation/tests -v
```

## Boundary

This package is a reference engineering artifact. `PASS` from its tests means only that these declared fixtures pass. It does not transform design text into machine certification, empirical validation, security certification, or deployment permission.
