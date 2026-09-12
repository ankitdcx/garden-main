# Garden SCEP v1.1 — Merged Genesis Seed

This package merges the useful Swarm Genesis v0.1 ideas into SCEP v1.0 and corrects false-certification paths.

## Key repairs
- local-first ledger; distributed storage is optional
- exact artifact hashes, not fake/example pins
- typed verifier semantics; compiler success is not correctness
- technical credits never become authority
- honest BLOCKED/DISCOVERY can earn credit
- scoped network capability is allowed when the work requires it
- threat-model design is separated from empirical sandbox validation
- abstract isolation proof is separated from actual implementation validation
- no invented initial gap-count estimate

Run: `python -m unittest discover -s tests -v`

The reference implementation uses Python standard library only and launches no LLMs.
