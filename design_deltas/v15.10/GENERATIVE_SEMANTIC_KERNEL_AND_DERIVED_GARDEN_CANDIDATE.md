# Garden v15.10 Candidate Note — Generative Semantic Kernel and Derived Garden

**Status:** NONCANONICAL DESIGN NOTE / EXPERIMENTAL DIRECTION  
**Canonical effect:** NONE

## Executive summary

Garden accumulated a large explicit design: modules, invariants, schemas, rights, contracts, state machines, tests, proof obligations, failure states, dependencies, authority rules, privacy rules, safety rules and domain profiles.

v15.10 suggests a deeper possibility: retain a smaller set of irreducible semantic and constitutional seeds, then systematically derive much of the detailed Garden surface from typed combinations of those seeds.

This is not "delete Garden and let an AI improvise rules."

    IRREDUCIBLE SEED
      rights / constitution / semantic primitives
      authority + consent + evidence meanings / meta-invariants
             |
             v
            GCSC        generate typed situations
             |
             v
             SAL        reject semantically invalid cases
             |
             v
         MATERIALITY    determine applicable obligations
             |
             v
             SAC        derive candidate artifacts
             |
             v
      VERIFY + COMPARE + RETAIN
             |
             v
      COMPILED SEMANTIC CLOSURE

Generated output does not self-admit. Generation success does not create authority, truth, proof, canonical status or permission.

### What this note is not

This is **not** a deletion plan, not canonical admission, not evidence that current Garden is redundant, and not permission for generated material to create authority. No explicit Garden item may be retired until the reconstruction/compression criteria below pass at appropriate scale.

### Seed interface

A candidate seed should expose at least:

    Seed = {
      PrimitiveMeanings,
      ProtectedProperties,
      ConstitutionalCommitments,
      AuthorityConsentEvidenceAxioms,
      GeneratorTrustBoundary,
      NonReconstructibleExceptions
    }

Every seed element must be versioned/addressable so that changed seed meaning can invalidate affected compiled closure.

## 1. Existing v15.10 substrate

The retained abstraction uses six GSL Pillars: Existence, Change, Agency, Law, Value and Frame.

Ten Core Objects:

    TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM

Twenty-four Core Relations:

    identifies, causes, governs, values, frames, acts, obeys, assesses,
    contextualizes, controls, partOf, dependsOn, owns, delegates, references,
    derivedFrom, equivalentTo, contradicts, supports, blocks, hasHypothesis,
    supersedes, conflictsWith, originatesFrom

Seven Design Forms:

    CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE, PROJECTION

The GCSC lineage already defines combinatorial coverage, deterministic SAL admissibility, materiality, typed non-erasing composition, property/emergence oracles, SAC artifact generation, predecessor-retention checking and bounded fixed-point closure. This note asks what follows if those mechanisms work well.

## 2. Three kinds of Garden information

### A. Irreducible seed semantics — keep explicitly

Examples: fundamental human rights; constitutional commitments; authority boundaries; meanings of person, consent, authority, evidence, claim and obligation; semantic primitives; externally chosen normative priorities; generator/checker/admission trust boundaries.

Combinatorics cannot derive a fundamental moral commitment from syntax alone.

    AGENCY --acts--> ACTION --affects--> HUMAN

does not logically imply "the human has bodily-autonomy rights." That commitment must enter as seed semantics.

### B. Derivable semantic closure — candidate for generation

Examples: consequences of rights; delegation-chain constraints; revocation propagation; dependency invalidation; stale-evidence handling; composition constraints; state machines; schema fields; FunctionContract pre/postconditions; negative tests/counterexamples; proof obligations; audit and recovery requirements.

### C. Empirical/domain inputs — load and verify

Examples: physical constants, medical facts, hardware characteristics, empirical probabilities, current law/jurisdiction and economic/environmental conditions.

The abstraction can derive what must be known or checked. It cannot manufacture the factual answer.

## 3. Reconstruction research protocol — controlling test

The central research claim is falsifiable: a frozen seed plus declared generator profile should reconstruct held-out Garden semantics it has not been shown.

1. Freeze SeedVersion, GCSC/SAL/materiality/SAC versions, finite registries, search profile/budget and permitted external inputs.
2. Partition retained Garden semantics into visible source and independently frozen held-out sets, stratified across invariants, schemas, FunctionContracts, states, tests, proof/assurance, dependencies, rights/authority/consent, safety, privacy, recovery, audit and composition.
3. Prevent the generator and proposer from accessing the held-out semantics.
4. Generate SAL-admitted situations and artifact obligations from the frozen seed/profile.
5. Compare generated artifacts to held-out material using meaning, scope, preconditions, effects, failure behavior, dependencies and authority/epistemic consequences—not name similarity.
6. Report **rediscovery** separately from **novel obligation discovery**.
7. For rediscovery report exact/strong/partial/missed/contradicted/unknown reconstruction and exception retention.
8. For apparently novel obligations, use independent adversarial review to estimate valid novelty, false positives, duplicates and seed-invention errors.
9. Repeat across independently frozen held-out partitions and, where possible, independent implementations/representations.
10. Any material miss, unauthorized widening, erased exception, false PASS or unexplained divergence keeps the affected predecessor item explicit and reopens the kernel/generator.
11. **Until reconstruction tests pass at appropriate scale, no explicit Garden item may be retired.**

Rediscovery answers "can the abstraction reconstruct known Garden?" Novel discovery answers "can it correctly extend coverage beyond known Garden?" A high rediscovery score does not validate novel obligations.

## 4. Human-rights example

Seed:

> A competent person controls applicable interventions on their own body.

Situation:

    AGENCY(AI) --performs--> ACTION(X) --affects--> HUMAN(H)
                             |
                             +--contextualizedBy--> CONTEXT(C)

Candidate consequences include: applicable consent; correct principal; action/scope/context/time binding; consent to X not automatically authorizing Y; material changes requiring reassessment; revocation and stale/UNKNOWN handling; delegation or multi-agent splitting not bypassing the right; indirect/delayed effects remaining in scope; optimization/capability not creating permission; emergency exceptions needing their own valid rule/authority.

Thus a small normative seed can generate a much larger obligation family.

## 5. One situation can generate an artifact family

Situation:

    AGENCY A --delegates--> AGENCY B --acts--> ACTION X
        |
        +--authority under--> RULE R / CONTEXT C

Candidate invariant:

    EffectiveAuthority(B,X,C)
      <= ValidDelegatedAuthority(A->B,X,C)
      <= EffectiveAuthority(A,X,C)

SAC can derive a DelegationRecord schema: delegator, recipient, action/resource/subject scope, context/jurisdiction, source authority, validity interval, expiry, revocation, invalidators and provenance.

State machine:

    PROPOSED -> ACTIVE -> EXPIRED
                  |  \
                  |   -> REVOKED
                  -> INVALIDATED

Contract:

    ValidateDelegation(record, action, context)
      -> VALID | INVALID | STALE | UNKNOWN | OUT_OF_SCOPE

Tests can cover missing source authority, scope amplification, expiry, revocation, context change, A->B->C chains, circular delegation, forged provenance and UNKNOWN upstream authority.

Proof obligation: composition of delegation edges must not amplify authority beyond valid externally grounded authority.

So the target output is not merely invariants. It is a coherent semantic obligation package.

## 6. Size of the situation space

Ignoring qualifiers and using only simple chains:

    2 objects: 10^2 * 24   = 2,400
    3 objects: 10^3 * 24^2 = 576,000
    4 objects: 10^4 * 24^3 = 138,240,000
    5 objects: 10^5 * 24^4 = 33,177,600,000

Real graphs add branching, cycles, multiple relations, time, context, state, uncertainty, authority, human effects and qualifiers. Naive enumeration is inappropriate.

    RAW COMBINATIONS
          |
          v
    SAL admissibility
       /       \
    invalid   meaningful
     discard      |
                  v
             MATERIALITY
                  |
                  v
          bounded GCSC search

The goal is coverage of meaningful semantic classes and a bounded fixed point, not exhaustive enumeration of every syntactic graph.

## 7. Ten-situation rediscovery experiment

A small exploratory conversation exercise selected ten materially different situations. Structural invariants were derived first; the retained Garden corpus was then searched for counterparts. This was not blinded, exhaustive or statistically representative.

1. **Chained delegation** — derived non-amplification, scope preservation, revocation/expiry propagation and UNKNOWN handling. Garden strongly covers it. Generalization: non-amplification over any composed authority path.

2. **Evidence dependency** — derived dependent reopening, stale dependency non-PASS, provenance retention and invalidity propagation. Garden strongly covers it. Generalization: material validity changes propagate through reachable dependency/derivation paths.

3. **Consent under changed context** — derived subject/action/scope/context/time binding, reassessment after material change and stale/revoked handling. Garden covers it. Generalization: material mutation of an authorization-bound object invalidates reuse unless explicitly covered.

4. **Self-modifying control cycle** — derived no self-bypass, externally grounded modification authority, no circular authority bootstrap and predecessor persistence. Garden substantially covers it through recursive-control/trust-boundary rules. Generalization: a closed cycle cannot generate a protected property absent from valid externally grounded entry edges.

5. **Lawful erasure and derived information** — derived privacy/taint propagation, no automatic independence after deletion and dependent-claim re-evaluation. Garden covers it. Generalization: source removal/invalidity requires recomputation across material derivation closure.

6. **Collective authority composition** — derived no authority from composition/work splitting, emergent-effect closure and common-dependency independence limits. Garden strongly covers it. Generalization: inspect composites for emergent protected properties/effects not visible component-wise.

7. **Irreversible transition** — derived dimension-specific rollback, compensation/recovery and no authority creation through transition/recovery. Garden covers it. Generalization: reversibility is effect/state-dimension-specific.

8. **Shared lossy representation** — derived representation independence, persistence of information loss, agreement not restoring missing facts and reopening after material alternative representation. This essentially regenerates REP.

9. **Optimization under hard constraints** — derived no hard-constraint override, no silent conversion of rights into preferences, and utility not creating authority. Garden covers it. Generalization: soft optimization operators should be structurally unable to weaken hard predicates.

10. **Model update and assurance reuse** — derived fresh qualification after semantic change, invalidation after drift and interface identity not proving semantic identity. Garden covers it. Generalization: assurance attaches to qualified semantic state plus dependencies, not merely component name.

### Experimental result

Roughly 45-55 meaningful structural invariants were produced, depending on merging.

Informally: about 80-90% had clear Garden counterparts; about 5-15% were broader formulations of existing rules; a small residual set looked like useful higher-order generalizations; no obvious conflict with the existing core direction appeared.

These percentages describe only this tiny hand-selected exercise. They are not estimates for the whole combinatorial space.

The important observation is that typed combinations repeatedly regenerated rules Garden had accumulated manually. This is limited evidence that v15.10 captures some deeper structure underlying the explicit rule set.

## 8. Four higher-order candidate invariant families

These are experimental generalizations, not admitted invariants.

### GSK-H1 — Protected-property non-generation

For protected property P:

    P(Compose(x1,...,xn))
      cannot exceed
    ClosureP(P(x1),...,P(xn), ValidExternalGrounds)

Composition cannot make authority, consent, evidence status, substantive independence, certification or permission appear from nowhere.

### GSK-H2 — Obligation non-erasure

A transformation, projection, abstraction, composition or optimization cannot silently discard a material applicable obligation.

### GSK-H3 — Reachable dependency invalidation

When a material property of a dependency changes, materially dependent reachable nodes must have the corresponding status recomputed. This can unify stale evidence, revoked authority, expired consent, erased data, changed models, invalid proof assumptions, changed law/context and changed trust roots.

### GSK-H4 — Dimension-wise reversibility

Reversibility belongs to individual effects/state dimensions:

    transaction
     +-- database state       reversible
     +-- disclosure           irreversible
     +-- money movement       conditional
     +-- physical effect      possibly irreversible
     +-- learned information  not undone by ordinary rollback

## 9. Could much of explicit Garden eventually disappear?

Potentially from the controlling hand-written layer, yes. Not yet.

    PERMANENT SEED
    rights / constitution / semantic primitives
    authority / consent / evidence meanings
    meta-invariants / generator trust boundaries
             |
             v
    SEMANTIC COMPILER
    GCSC -> SAL -> MATERIALITY -> SAC
             |
             v
    VERIFIED COMPILED GARDEN
    invariants / schemas / contracts / states
    tests / proofs / dependencies / recovery
             |
             v
           RUNTIME

The large explicit corpus can remain as an oracle/regression set while the hypothesis is tested.

## 10. Compile-time versus runtime

Generating everything from scratch for every action is undesirable. Prefer:

    SEED
      |
      v
    GENERATE
      |
      v
    VERIFY / FALSIFY / COMPARE
      |
      v
    COMPILE + CONTENT-ADDRESS + CACHE
      |
      v
    RUNTIME LOOKUP
      |
      +--> known situation: use qualified compiled closure
      |
      +--> materially novel situation:
             bounded generation/research
             -> UNKNOWN/BLOCK/ESCALATE until qualified as required

A generated result should be reproducibly bound to SeedVersion, Situation, Context, DomainInputs, GeneratorVersion and QualificationProfile.

## 11. Safe compression criterion

No explicit Garden semantic item is replaceable by derived/compiled form unless all applicable checks PASS:

- [ ] Seed dependencies are explicit, addressable and versioned.
- [ ] Derivation is deterministic or precisely qualified under a declared profile.
- [ ] Meaning is equivalent or strictly stronger without unauthorized scope widening.
- [ ] All material exceptions and failure states survive.
- [ ] Negative/UNKNOWN/STALE/BLOCKED/INCONCLUSIVE behavior is preserved.
- [ ] Rights, consent, privacy, safety, authority and Human-Effect obligations are not weakened.
- [ ] Dependency and invalidation behavior is preserved.
- [ ] Independent checking is possible without trusting the original generator's self-report.
- [ ] Predecessor source remains recoverable during migration.
- [ ] Generator, registry or seed change invalidates affected assurance.
- [ ] Generated material cannot certify its own admission.
- [ ] Held-out reconstruction tests cover the item's semantic family and relevant exceptions.
- [ ] No unresolved contradiction or material miss remains for the claimed scope.

Failure or UNKNOWN on an applicable item keeps the predecessor explicit.

## 12. What cannot be safely compressed away

Even a successful generative architecture needs explicit grounding for fundamental rights/constitutional choices; definitions of protected properties; applicable external law/policy; empirical facts/calibrated domain models; irreducible semantic primitives; provenance; trust/admission boundaries; non-reconstructible exceptions; and historical material needed for lawful audit/reconstruction.

The goal is semantic compression, not information destruction.

## 13. Bounded fixed-point definition

    seed G0
       |
       v
    generate situations
       |
       v
    derive candidate obligations/artifacts
       |
       v
    compare to existing closure
       |
       +-- already implied ----------> reuse
       +-- stronger equivalent ------> candidate simplification
       +-- uncovered meaningful case -> candidate new obligation
       +-- contradiction ------------> reopen assumptions/seed/design
       |
       v
    verify / repair
       |
       v
    repeat until bounded fixed point G*

A bounded fixed point is defined only relative to a frozen epoch containing the seed, registries, interpretation/materiality rules, topology/depth/qualifier domains, property oracles, search budget and termination profile.

A **material new class** is a SAL-admitted situation or composition that activates a previously uncovered obligation, prohibition, invalidator, status, effect or artifact requirement under that epoch.

G* is reached only when a complete declared iteration produces no material new class within the frozen bound. Resource exhaustion yields RESOURCE_UNKNOWN/INCOMPLETE, not closure. Situations outside the declared bound remain OUT_OF_PROFILE/UNKNOWN and, where qualification is required for action, follow the applicable BLOCK/ESCALATE behavior. A bounded fixed point never means "all possible future situations solved."

## 14. Failure modes of generative compression

The generative approach itself can fail. At minimum test for:

- **Seed invention:** generator silently supplies a missing normative commitment and then "derives" from its own invention.
- **Under-materiality:** materiality is too narrow, producing systematic blind spots.
- **Over-materiality:** materiality is too broad, causing noise/combinatorial explosion and unusable obligation sets.
- **Representation convergence:** supposedly independent generators/checkers share the same framing or blind spot; see the v15.11 REP candidate.
- **Seed/registry drift:** a small upstream change invalidates large compiled closures without correct dependency propagation/requalification.
- **False equivalence:** name/schema similarity is mistaken for semantic reconstruction.
- **Exception loss:** general rules reconstruct the common case but erase specialist exceptions.
- **Self-admission:** generated coverage is treated as authority or proof of its own correctness.
- **Premature deletion:** high rediscovery on a small/easy sample is used as permission to retire predecessor semantics.
- **Runtime mismatch:** correct compiled semantics do not guarantee correct real execution; see the v15.11 VEI candidate.
- **Recursive-control failure:** a generator/evolver weakens the controls used to qualify its successors; see RCC.
- **Retention failure:** compact representation drops unique predecessor meaning; see `V15X_RETENTION_RECOVERY_ADDENDUM_2026-09-20.md`.

## 15. Compression magnitude

The reducible fraction is **unknown**. No numeric compression estimate is currently justified.

The experiment should produce the number rather than assume it. Report at least:
- fraction of held-out semantic items reconstructed at required fidelity;
- fraction remaining irreducible/explicit;
- fraction missed or contradicted;
- exception-retention rate;
- false-positive/invalid-novelty rate;
- validated novel obligations not present in the retained corpus.

If the compact kernel reconstructs retained Garden and GCSC also finds valid obligations for previously uncovered situations, the derived Garden can become smaller at the fundamental-source layer while larger/more complete at the derived layer. Abstraction is therefore both a compression hypothesis and a design-space exploration hypothesis.

### Related retained candidates

- v15.10 retention boundary: `V15X_RETENTION_RECOVERY_ADDENDUM_2026-09-20.md`.
- v15.11 RCC: recursive control/qualification closure.
- v15.11 REP: representation escape and substantive independence.
- v15.11 VEI: verified execution integrity after policy/semantic qualification.

These remain separate candidate owners; this note does not absorb or admit them.

## 16. Conclusion

The v15.10 abstraction may be more than a way to reorganize Garden.

    MANUALLY ENUMERATED GARDEN
              |
              v
    SEMANTICALLY FACTORED GARDEN
              |
              v
       SMALL EXPLICIT KERNEL
      + VERIFIED GENERATIVE CLOSURE
              |
              v
       DERIVED / COMPILED GARDEN

The ten-situation experiment provides limited but encouraging evidence: many independently derived structural obligations mapped back to rules Garden already contained, while several outputs appeared as higher-order generalizations.

The long-term possibility is not "Garden without invariants." It is a Garden where a smaller number of fundamental invariants and normative commitments are explicit, while a much larger body of detailed invariants, schemas, contracts, tests and proof obligations is reproducibly derived and independently checked.

That would turn much of Garden from a manually maintained rule catalogue into a compiled consequence of a smaller semantic constitution.

This remains a candidate research direction until lossless derivability, independent reproducibility and regression against the retained corpus are demonstrated.
