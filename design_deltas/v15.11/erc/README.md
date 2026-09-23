# v15.11 ERC Candidate

This directory preserves **V1511-ERC-001**, an **experiment-first, additive, noncanonical** candidate for Evaluation Reachability Closure.

It was derived from scout finding **SCOUT-20260923-004**. The narrow surviving idea is that evaluation containment should qualify the **transitive reachable trust graph plus cumulative action budget**, including persistence and credential/identity expansion, rather than relying only on the nominal sandbox boundary.

ERC deliberately reuses existing RCC, Security, Authority/HSA, Human-Effect Closure, dependency, revocation, recovery, evidence and audit machinery.

Nothing in this directory is canonical or admitted. The exact target-source binding, deduplication against current v15.10/v15.11 security semantics, bounded staging experiment and normal Garden review remain required.

Files:
- [Candidate specification](GARDEN_v15.11_ERC_CANDIDATE.md)
- [Manifest](CANDIDATE_MANIFEST.json)
- [Validation / scout reconciliation](VALIDATION.md)
