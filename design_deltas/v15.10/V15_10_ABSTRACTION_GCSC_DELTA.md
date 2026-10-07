# Garden v15.10 — Abstraction and GCSC Design Delta

**Status:** retained working-design delta; not canonical admission.

v15.10's major design change was a move toward a compact, typed, generative representation of Garden. This file preserves that idea directly rather than preserving multi-megabyte generated catalogues.

## Abstract substrate

Six GSL Pillars remain interpretive projections: **Existence, Change, Agency, Law, Value, Frame**.

Ten Core Objects:
`TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM`.

Twenty-four Core Relations:
`identifies, causes, governs, values, frames, acts, obeys, assesses, contextualizes, controls, partOf, dependsOn, owns, delegates, references, derivedFrom, equivalentTo, contradicts, supports, blocks, hasHypothesis, supersedes, conflictsWith, originatesFrom`.

Seven Design Forms:
`CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE, PROJECTION`.

Ten cross-cutting inspection facets:
`IdentityLifecycle, ScopeContext, EpistemicsProvenance, AuthorityHumanBoundary, EffectsSafety, DependencyValidity, ResourceTermination, PrivacyRetention, AuditExplanation, RecoveryEvolution`.

The abstraction organizes specialist meaning; it does not erase it. Theory and Algebra are compositions/specializations over the Forms, not extra top-level Forms. A readable projection does not become controlling merely because it is simpler.

## GCSC / SAL / SAC

**Generative Combinatorial Semantic Coverage (GCSC)** constructs bounded combinations of objects, relations and qualified situations and asks what each meaningful combination requires.

**Semantic Admissibility Layer (SAL)** decides whether a proposed combination is structurally/semantically meaningful and what remains unresolved.

**Semantic Artifact Compiler (SAC)** may convert uncovered requirements into *candidate* schemas, invariants, FunctionContracts, tests and proof obligations.

Generated/derived material is not an independent source of authority. A successful build, hash, model agreement or generated candidate cannot self-admit a semantic change.

## Deterministic expansion

Compact controlling source may expand deterministically:

`G0 -> F(G0) -> F^2(G0) -> ... -> G*`

Expansion must have a declared termination/fixed-point condition. A model may not invent missing semantics during expansion. Unique equations, algorithms, assumptions, fallbacks, exceptions and special-case semantics remain seed material when they cannot be deterministically reconstructed. Generated material records its source root and generation rule. Divergent independent expansions do not establish equivalence.

## Ownership and no-loss

Every controlling semantic item needs a stable qualified identity and one controlling owner. The later Tree Core work sharpened the required owner record to include exact source/span/hash, release/effective scope, typed status axes, applicability, dependencies, relations, exceptions and historical disposition.

Compaction removes duplication, not meaning. UNKNOWN/CONFLICT/INCOMPLETE remain explicit non-PASS states where applicable. Authority, consent, rights, privacy, safety and Human-Effect obligations cannot be widened or dropped through composition or generation.

See `TREE_CORE_v0.8.1_2026-09-23.txt` for the later structural integration candidate.
