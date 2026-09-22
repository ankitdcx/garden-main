# Garden v15.11 Candidate — Representation Escape Principle (REP)

**Candidate ID:** V1511-REP-001  
**Status:** ADDITIVE NONCANONICAL CANDIDATE  
**Canonical effect:** NONE until separately admitted.

## Problem

Consequential reasoning can appear independently verified while all reasoners inherit the same representation of the problem. Familiarity, conventionality, historical success, or multiple analyses inside one representation do not establish representational completeness.

REP is orthogonal to Compare, GCL, CDDT, Human-Effect Closure, reasoning-strategy diversity, and BRIDGE. Existing mechanisms may re-represent a problem, but this candidate makes representation coverage explicit, typed, evidenced, and testable.

## Contracts

### RepresentationPortfolio

A finite, versioned registry of representation kinds and registered representations. Each entry declares its kind, transformation/derivation, information intentionally preserved or suppressed, applicable domains, known losses, and evidence provenance.

The portfolio is never represented as exhaustive.

### RepresentationCoverageProfile

A context/risk-dependent contract:

`RequiredRepresentationCoverage(context) -> {mandatory_kinds, minimum_kind_diversity, budget, stopping_rule}`

Coverage requirements SHALL depend on consequence/risk and domain. There is no universal fixed K or D.

Syntactic variants of substantially the same abstraction do not count as distinct kinds merely because their encodings differ.

## Invariants

**REP-001 — Representation Non-Completeness**  
For consequential reasoning, familiarity, conventionality, historical success, or dominance of the active representation SHALL NOT constitute evidence of representational completeness.

**REP-002 — Orthogonal Routing**  
Before a consequential conclusion is accepted, the subject SHALL be evaluated through the representation kinds required by the applicable RepresentationCoverageProfile.

**REP-003 — Kind Distinctness**  
Multiple representations derived from substantially the same abstraction SHALL NOT satisfy diversity requirements merely by being syntactically different.

**REP-004 — Material Divergence**  
A materially relevant conclusion exposed by another required representation SHALL reopen the affected reasoning and all downstream conclusions dependent on it.

**REP-005 — Bounded Convergence**  
Agreement across required representations establishes PRESUMED_CONVERGENT only. It SHALL NOT establish PROVEN_COMPLETE or equivalent representational completeness.

**REP-006 — Coverage Failure**  
Missing mandatory representation coverage for a consequential conclusion yields UNKNOWN/INCOMPLETE, not PASS.

**REP-007 — Open Representation Frontier**  
Discovery or generation of representation kinds outside the registered portfolio belongs to Research. Unattempted escape remains a recorded residual unknown; the portfolio SHALL NOT be claimed complete.

**REP-008 — Constitutional Precedence**  
REP expands epistemic inspection. It neither grants authority nor relaxes rights, consent, privacy, safety, evidence, law, Human-Effect Closure, or other hard gates.

## Representation independence and verifier independence

Substantive verifier independence SHALL consider representation independence as a distinct dimension alongside model/lineage, data/evidence, reasoning-strategy, trust-root, and authority independence where applicable.

Two nominally independent verifiers that inherit the same material representation can share the same blind spot. Representation overlap does not automatically invalidate verification, but it SHALL be declared and SHALL NOT be counted as representation-independent corroboration.

This candidate does not by itself define a complete decision procedure for substantive independence; it supplies one required dimension for that procedure.

## Operational clarification

REP does not require an AI to simulate a human novice or to erase learned semantics. The required operation is **orthogonal routing**: deliberately evaluate the same subject through materially different registered representation kinds.

Human heuristic only, non-normative: inability to describe a subject without its conventional name can trigger REP escalation. It is not a conformance test.

## Minimal conformance tests

1. **Same-kind gaming:** AST, normalized AST, and comment-stripped AST cannot satisfy a profile requiring multiple distinct representation kinds merely by count.
2. **Orthogonal discovery:** a conclusion accepted under a semantic/code view is reopened when a required authority-flow or resource-flow representation exposes a material conflict.
3. **False completeness:** agreement across all required registered kinds returns PRESUMED_CONVERGENT, never PROVEN_COMPLETE.
4. **Missing coverage:** omission of a mandatory kind yields UNKNOWN/INCOMPLETE.
5. **Risk sensitivity:** low- and high-consequence contexts may resolve to different coverage profiles; a universal hard-coded K is rejected.
6. **Downstream invalidation:** a material divergence reopens dependent conclusions, not only the local statement.
7. **Research boundary:** absence of an unregistered representation is recorded as residual unknown and does not create an impossible unbounded REP gate.
8. **Authority boundary:** successful REP coverage cannot grant permission or authority otherwise absent.
9. **Verifier independence:** two verifiers sharing the same material representation cannot be claimed representation-independent solely because their models differ.
10. **Loss declaration:** a portfolio transformation with undeclared material suppression fails portfolio admission.

## Explicit non-claims

REP cannot discover representations no one has conceived; prove the portfolio complete; guarantee the best alternative representation was selected; or make arbitrary long-range meta-layer search decidable.

REP therefore proves only bounded declared coverage, never exhaustive meta-layer coverage.
