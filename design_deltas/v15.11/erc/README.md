# v15.11 ERC Candidate

This directory preserves **V1511-ERC-001**, an **experiment-first, additive, noncanonical** candidate for Evaluation Reachability Closure.

**Current revision:** 1.1 — 26 September 2026 scout evidence hardening.

The core idea remains narrow: evaluation containment should qualify the **transitive reachable trust graph plus cumulative action budget**, including persistence and credential/identity expansion, rather than relying only on the nominal sandbox boundary.

Revision 1.1 adds only evidence hardening that survived scout testing and source comparison:
- typed fixture coverage/provenance metadata;
- environment/task-grounded completion evidence;
- conditional stochastic-measurement sufficiency for comparative claims;
- an explicit boundary between evaluation coverage and incident prevalence/risk.

ERC deliberately reuses existing RCC, Security, Evaluation, Evidence/Provenance, Authority/HSA, Human-Effect Closure, Dependency, Revocation, Recovery, uncertainty, DO_NOTHING and Audit machinery. It creates no new top-level engine, authority source, theory or general statistics subsystem.

Nothing in this directory is canonical or admitted. The exact target-source binding, bounded staging experiment, independent review and normal Garden admission remain required.

Files:
- [Candidate specification](GARDEN_v15.11_ERC_CANDIDATE.md)
- [Manifest](CANDIDATE_MANIFEST.json)
- [Validation / scout reconciliation](VALIDATION.md)
