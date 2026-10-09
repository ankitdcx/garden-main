# v15.9.1 — source-defined GCSC semantic contracts (incremental)

**Status:** CURRENT CANDIDATE CONTRACT; machine execution and admission separately receipt-bound. This document records the actual new contracts, not a replacement for v15.9.

## Meaning and scope
GCSC = Generative Combinatorial Semantic Closure: bounded construction and checking of combinations of Garden semantic objects, relations and qualifiers. SAL = Semantic Admissibility Layer: finite-registry checks that a generated construction is structurally meaningful and interpretable, without granting permission or truth. SAC = Semantic Artifact Compiler: derives candidate schemas, invariants, tests and proof/receipt obligations from semantic witnesses. These are compiler/assurance mechanisms, not new engines, authority roots, rights or an eighth theory.

## Typed structures
```text
RelationInstance = {
  relation, source, target, bindings,
  context_ref?, time_ref?, scope_ref?, criteria_ref?,
  authority_ref?, dependency_kind?, validity, provenance, epoch_id
}
SALResult = {
  structural_status, completeness_status, join_status,
  coherence_status, interpretation_status, diagnostics[],
  missing_bindings[], witnesses[], completion_frontier
}
pi_material: SALAdmittedSituation -> ObligationProfile
```
Core Relations stay binary. RelationInstance qualifiers preserve contextual or n-ary meaning without inventing new primitives. SALResult is a product of independent diagnostics, not a scalar PASS ladder. Missing source/target types return UNRESOLVED rather than TYPE_INADMISSIBLE; no silent defaults.

## SAL registries and evaluation
Epoch-frozen finite registries: RelationSignatureRegistry, BindingDomainRegistry, ConstraintLanguageRegistry, JoinWitnessRegistry, StructuralIncoherenceRegistry, InterpretationSchemaRegistry and DiagnosticCounterexampleRegistry. Interpretation is decidable only by a registered finite interpretation schema; exhausted search returns UNRESOLVED. Joinability requires an explicit typed registered join witness and is structural, not normative compatibility. Binding consistency checks internal well-formedness, not legal or moral permission. CompletionFrontier is a finite dependency DAG: instantiate unresolved slots topologically and revalidate after each assignment.

## Materiality and composition
The epoch-frozen, coverage-independent `pi_material` maps a SAL-admitted situation to an ObligationProfile, recording applicable requirements/effects across authority, consent, rights, safety, law/jurisdiction, evidence, human effects, privacy, dependency validity, resource/termination, audit, recovery/reversibility, state mutation and time. Explicitly mark non-applicable dimensions. `⊕` composes profiles without a total order: union hard obligations, retain conflicts and unknowns, never amplify authority, keep consent scope-bound, preserve irreversible/state-mutating effects and evidence dependence.

ValidityState is a **product of diagnostic sets**; labels include VALID, INVALID_TYPE, PROHIBITED, CONTEXT_REQUIRED, AMBIGUOUS, CONFLICT and UNKNOWN. Simultaneous diagnostics remain visible; no priority rule may erase a non-PASS result.

## Emergence and SAC
A composition is materially novel when a finite registered property oracle detects an obligation, prohibition, invalidator, status or effect not derivable from its components under frozen composition rules. Do not assume a general semantic-equivalence theorem. Shrink failing examples to minimal witnesses. SAC maps witnesses to candidate invariant families, schema fields/bindings, FunctionContract requirements, positive/negative/boundary/composition tests, and proof/receipt obligations. First compare with existing owners: REUSE if covered; EXTEND if partial; NEW_CANDIDATE only for absent material semantics. Never self-admit generated output.

## Generation stages
- **L0:** classify all 10 × 24 × 10 = 2,400 raw Object–Relation–Object skeletons by signature/SAL. Preserve rejected cells in the RAW denominator.
- **L1:** applicable Pillar/Form/Facet/Macro lifts with explicit predicates, never blind Cartesian multiplication.
- **L2:** connected two-edge motifs using registered typed join witnesses.
- **L3:** connected three-edge motifs under the same join discipline.
- **L4:** targeted constitutional/consequential motifs: human effects, authority, consent, rights, safety, privacy, evidence, collective effects, conflict, revocation, recovery, self-modification.
- **L5:** bounded property/adversarial generation, canonical depth ≤64, shrinking and resource termination.

## Frozen Epoch-1 vocabulary and registry IDs
Six Pillars: Existence, Change, Agency, Law, Value, Frame. Ten Core Objects: TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM. Twenty-four Core Relations and seven Forms are inherited unchanged. Ten Facets: IdentityLifecycle, ScopeContext, EpistemicsProvenance, AuthorityHumanBoundary, EffectsSafety, DependencyValidity, ResourceTermination, PrivacyRetention, AuditExplanation, RecoveryEvolution. Twenty-one Macros: ArchitectureObject, Function, Lifecycle, Schema, Receipt, Registry, Test, ProofObligation, Theory, Algebra, Profile, EventRecord, Binding, Plan, FailureMode, Query, EventSubscription, ContinuousWorker, DynamicalSystemProfile, AuthorityGatedContract, RecoveryEnvelope.

Registry IDs: REG-GCSC-001, REG-SAL-001, REG-SAC-001, REG-GCSC-PROPERTY-001, REG-GCSC-COVERAGE-001. Generated-artifact lifecycle: GENERATED_CANDIDATE → VERIFIED_GENERATED → CANONICAL **only through ordinary Garden admission**, never generation alone. Coverage FULL/PARTIAL/NONE/UNKNOWN/NOT_EXECUTABLE is assessed separately for semantic contract, schema, invariant, test, proof/receipt and end-to-end execution.

## Epoch-1 reported evidence (not universal constants)
2,400 L0 raw skeletons; 346 signature/SAL-admissible L0 candidates; 12,249 generated typed L2 motifs; 12 SAC semantic families; 66 cross-family pairs; 220 cross-family triples; 704 generated cross-family assurance-test candidates. These are reported pinned-run counts, **not** proof of semantic completeness.

## Anti-gaming and retention
Coverage tests/invariants/schemas cannot determine SAL admissibility. Relation signatures need explicit justification and epoch hashes; RAW cannot shrink inside an epoch. Matching a name or SchemaID is not semantic coverage. UNKNOWN/INCONCLUSIVE/NOT_EXECUTABLE cannot become PASS. Predecessor material semantics require PRESERVED/GENERALIZED/MERGED/SUPERSEDED_WITH_PROOF mapping; UNMAPPED material semantics block lossless release. All human/rights/safety/authority and theory rules remain inherited unless exactly and lawfully superseded.

## Source binding / extraction boundary
Source-derived from the historical v15.9.1 Technical `[T-GCSC-1591]` and Annexure `[A-GCSC-1591]` byte-prefix editions, plus System `[S-GCSC-1591]`. This is a **detailed contract extraction**, not a certified exhaustive delta: the manifest-verified COMPLETE archive contains further GCSC closure suffixes absent from these earlier editions. Its additional machine algorithm/schema/validity, JOIN, CONSTRAINT, INTERPRETATION, MATERIALITY, PRIMITIVE-DISPOSITION, GENERATED-ASSURANCE, COVERAGE-METRICS, RETENTION and RELEASE-GATE clauses require separate exact extraction.
