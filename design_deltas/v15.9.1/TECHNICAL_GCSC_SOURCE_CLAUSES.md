# Garden v15.9.1 — Technical added GCSC clauses

Exact source extraction from the **earlier byte-prefix edition** of Garden_v15.9.1_Technical.txt, lines 15779–15841. Candidate, not canonical. Later COMPLETE-archive suffixes remain separate and are not claimed here.

---

[T-GCSC-1591] GENERATIVE SEMANTIC CLOSURE — EXECUTABLE CONTRACT

Core structures
RelationInstance = {relation, source, target, bindings, context_ref?, time_ref?, scope_ref?, criteria_ref?,
                    authority_ref?, dependency_kind?, validity, provenance, epoch_id}.
Core Relation remains binary; RelationInstance carries the finite qualifiers needed to preserve scoped/n-ary meaning.

SALResult is a product, not one ladder:
  structural_status; completeness_status; join_status; coherence_status; interpretation_status; diagnostics[];
  missing_bindings[]; witnesses[]; completion_frontier.
No silent defaults are permitted. Unknown source/target types yield UNRESOLVED, not TYPE_INADMISSIBLE.

SAL uses epoch-frozen finite registries: RelationSignatureRegistry, BindingDomainRegistry, ConstraintLanguageRegistry,
JoinWitnessRegistry, StructuralIncoherenceRegistry, InterpretationSchemaRegistry and DiagnosticCounterexampleRegistry.
Interpretability is decidable only through the finite InterpretationSchemaRegistry; exhaustion returns UNRESOLVED.
Joinability is structural-only and requires an explicit registered join witness. Normative compatibility is downstream.
Binding consistency checks internal well-formedness only; normative permission/prohibition remains downstream.

CompletionFrontier is a finite dependency DAG of unresolved slots. Slots instantiate in topological order with
revalidation after each assignment.

Materiality
pi_material : SALAdmittedSituation -> ObligationProfile
is epoch-frozen and coverage-independent. ObligationProfile is distinct from Facets and records applicable material
requirements/effects, including authority, consent, rights, safety, legality/jurisdiction, epistemic/evidence state,
human effects, privacy, dependency validity, resources/termination, audit/explanation, recovery/reversibility,
state mutation and temporal validity where applicable. Non-applicable dimensions remain explicit.

Composition
⊕ combines obligation profiles without assuming a total order. Hard obligations union; conflicts/unknowns are
preserved; authority never amplifies by composition; consent remains scope-bound; irreversible/state-mutating effects
remain visible; evidence dependence is preserved.

ValidityState is a product of diagnostic sets rather than a total scalar lattice. Canonical terminal labels include
VALID, INVALID_TYPE, PROHIBITED, CONTEXT_REQUIRED, AMBIGUOUS, CONFLICT and UNKNOWN, but simultaneous diagnostics may
coexist. No precedence rule may erase a non-PASS diagnostic.

Emergence
A composition is materially novel when a registered property oracle activates an obligation, prohibition, invalidator,
status or effect not derivable from the components under the frozen composition rules. Emergence is operationalized by
finite named property oracles; no unrestricted semantic-equivalence theorem is assumed. Failing cases are shrunk to a
minimal witness.

SAC
SAC maps a minimal semantic witness to candidate invariant families, required schema fields/bindings, FunctionContract
requirements, positive/negative/boundary/composition tests and proof/receipt obligations. It first binds semantically to
existing owners. Existing coverage is reused; partial coverage is extended; only absent material semantics become
NEW_CANDIDATE. Generated candidates are never self-admitted.

Generation levels
L0: all 2,400 raw Object-Relation-Object skeletons, classified by signature/SAL.
L1: applicable Pillar/Form/Facet/Macro lifts; no blind Cartesian multiplication. Pillars are projections; Facets are
     lenses; Forms/Macros are topology/pattern lifts with explicit applicability predicates.
L2: connected two-edge motifs under registered typed join witnesses.
L3: connected three-edge motifs under the same discipline.
L4: targeted constitutional/consequential motifs, especially human effects, authority, consent, rights, safety,
     privacy, evidence, collective effects, conflict, revocation, recovery and self-modification.
L5: bounded property/adversarial generation up to canonical depth 64 with shrinking and resource termination.

Anti-gaming
Coverage schemas/invariants/tests cannot determine SAL admissibility. Relation signatures require explicit semantic
justification and epoch hashing. RAW cannot shrink inside an epoch. Name/SchemaID match is not semantic coverage.
UNKNOWN/INCONCLUSIVE/NOT_EXECUTABLE are never PASS. Generated artifacts cannot certify themselves.
