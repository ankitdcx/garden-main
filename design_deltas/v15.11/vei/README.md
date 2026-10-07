# v15.11 VEI Candidate

**V1511-VEI-001 — Verified Execution Integrity** is a bounded, additive, noncanonical v15.11 candidate.

It specializes existing Authority/Revocation/Security/Evidence/Recovery/Dependency owners at the runtime effect boundary. It does **not** create a new top-level engine, theory, authority source, scheduler, or canonical rule.

The candidate closes a narrower implementation gap:

> A policy can be correct on paper while stale state, delayed writers, adapter rewriting, replay, ambiguous external effects, compromised runtime artifacts, or self-reported completion still produce the wrong real-world effect.

VEI therefore binds consequential execution to fresh scoped state, exact final parameters, target capabilities, durable intent/effect receipts, reconciliation, and verifier-isolated completion evidence.

Key boundaries:
- RCC remains the recursive-change/control-closure candidate; VEI does not replace it.
- ERC remains the evaluation-reachability candidate; VEI does not replace it.
- Canonical Garden v15.5 remains unchanged.
- Class A/B/C target guarantees are explicitly conditional; no universal antirollback claim is made.
- Runtime implementation, formal checking, staging, independent review and canonical admission remain pending.

Files:
- [Candidate specification](GARDEN_v15.11_VEI_CANDIDATE.md)
- [Manifest](CANDIDATE_MANIFEST.json)
- [Validation / deduplication](VALIDATION.md)