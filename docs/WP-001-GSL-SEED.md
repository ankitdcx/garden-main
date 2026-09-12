# WP-001 — Minimal executable GSL semantic kernel

This is a deliberately small **seed transport/profile**, not the complete GSL v45.1 compiler.

Profile: `GSL-SEED-JSON-0.1`

It implements the exact 10 Garden Core Object names, typed values, explicit CLAIM status, CONTEXT references, typed dependency kinds, BUILD DAG checking, explicit RUNTIME feedback grouping, obligations/tests/scoped receipts, conservative evidence-gated epistemic transitions, and fail-closed handling for unsupported profiles/statuses/object kinds.

It does **not** claim full GSL v45.1 grammar coverage, semantic equivalence to every canonical construct, truth from successful parsing, or proof/certification of Garden or AGI.

Run:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```
