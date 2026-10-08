# GARDEN-RSDC-001 — Recursive Semantic Discovery & Compression

**Status:** NONCANONICAL ADDITIVE CANDIDATE; not implemented, tested, certified or admitted  
**Target:** v15.10 GCSC/SAL/Materiality/SAC + IDTD-001  
**Compatible:** v15.5 canonical; v15.11 RCC/REP/SHR/VEI and recovered EVO/SEM  
**Topology:** UNCHANGED · **Canonical effect:** NONE · **New authority:** NONE

## Purpose and existing owners

Discover new obligations/theories while compressing independently maintained design, without losing semantics. Reuse existing owners rather than creating eight subsystems. The **Explicit Seed** is the irreducible seed from the v15.10 Generative Semantic Kernel note: PrimitiveMeanings, ProtectedProperties, ConstitutionalCommitments, AuthorityConsentEvidenceAxioms, GeneratorTrustBoundary and NonReconstructibleExceptions, together with justified fundamental invariants. External facts are evidence inputs, not invented seeds.

```text
Seed → GCSC → SAL → Materiality → SAC → IDTD + adversarial tests
     → independent comparison/falsification → noncanonical candidate artifacts
Reverse: corpus → proposed smaller seed → independently verified reconstruction
```

Neither loop may admit its own results. OCFP and the theory–invariant loop reapply the same Materiality and Human-Effect gates as SAC at each materially changed consequence.

**Ownership:** OCFP and AMG extend GCSC/property oracles; ownership compression extends Tree Core/retention; EDA extends dependency validity and SHR; recursive portfolios extend REP; duality extends IDTD; compile/runtime qualification extends DesignEpoch and VEI; minimal seed extraction extends the v15.10 reconstruction program. RCC governs recursively changing controls; EVO/SEM remain recovered complementary directions, not superseded owners. No new top-level Form, engine, or admission authority.

## Common operator contract

Each operator freezes its input profile **before execution**: SourceEpoch, SeedRoot, registry/interpreter versions, topology/domain, depth bound, budget, termination criterion, applicable property oracles, materiality profile and independent review requirements. No post-hoc change to denominator or success criterion.

```text
RSDCReceipt {
 OperatorID, SourceEpoch, SeedRoot, GeneratorVersion, RegistryRoots,
 InputHashes[], SearchProfile, DepthBound, BudgetConsumed,
 TerminationReason, GeneratedArtifactRefs[], Unknowns[], Conflicts[],
 Invalidators[], EvidenceRefs[], AdmissionStatus
}
```

All receipt types below extend this record. Terminal outcomes include BOUNDED_FIXED_POINT, INCOMPLETE, RESOURCE_UNKNOWN, CONFLICT and FAILED. Completion claims require replayable iteration traces, not just a final hash.

## Eight incremental operator extensions

### RSDC-01 — Obligation Closure Fixed-Point (GCSC)

`O[n+1] = O[n] ∪ MaterialClosure(GCSC(O[n]))`, starting from explicit seed obligations and applicable rights/Human-Effect constraints. Canonicalize by **meaning, subject, scope, context, status, dependencies, exceptions and modality**. Preserve conflicts/unknowns. New iterations count *new material obligation classes*, not textual variants or hashes. Stop only at a declared bounded fixed point; exhaustion returns INCOMPLETE/RESOURCE_UNKNOWN. **Output:** ObligationClosureReceipt.

### RSDC-02 — Adversarial Motif Generator (GCSC/property oracles)

Given protected property P, finite threat model, relation grammar and budget, generate hostile *synthetic* compositions: delegation chains, swarms, cycles, representation loss, stale/revoked states, side channels, hidden dependencies and cumulative effects. SAL checks meaning; Materiality checks obligations; property oracles test P; deterministic shrinking minimizes failures; independent reviewers validate. No unauthorized real-world attacks. **Output:** AdversarialMotifReceipt.

### RSDC-03 — Ownership Graph Compression (Tree Core/retention)

Take atomic owner graph with source spans/hashes, typed statuses, dependencies, exceptions and applicability. Propose fewer explicit owners plus derivation rules; re-expand; compare semantic obligations and owner assignments. Require byte equality only where contractually necessary, otherwise independently proven semantic equivalence. Any missing material item, exception, status or controlling owner blocks reduction. **Output:** CompressionEquivalenceReceipt.

### RSDC-04 — Epistemic Debt & Revalidation (dependency validity/SHR)

```text
EpistemicDebtVector {
 evidence_age, changed_dependencies, representation_drift,
 environmental_change, unresolved_assumptions, assurance_scope, uncertainty
}
```

Use typed predicates per coordinate. Hard invalidation suspends dependent claims/permissions immediately; scalar scores may prioritize but never override hard failures. Freeze justified profile-specific thresholds; revalidation produces a new receipt without overwriting history. **Output:** RevalidationReceipt.

### RSDC-05 — Bounded Recursive Representation Portfolio (REP)

Review object-level representations (L0), then independent representations of their portfolio (L1), optionally meta-review (L2…N). Freeze depth N, threat model, representation-diversity requirements and budget beforehand. Shared lineage/control and residual unknown blind spots remain explicit. Additional levels never prove independence merely by number. **Output:** RepresentationReviewReceipt.

### RSDC-06 — Theory–Invariant Duality (IDTD)

Seed-justified invariants → IDTD candidate theories → extracted candidate invariants → Materiality/Human-Effect recheck → independent falsification → existing-owner comparison → next bounded discovery cycle. No circular self-verification, seed invention, or automatic module creation. Require explanatory gain (multiple material consequences or distinct testable prediction). **Output:** TheoryInvariantDerivationReceipt.

### RSDC-07 — Compile–Runtime Qualification (DesignEpoch/VEI)

```text
CompiledArtifact {
 CompileEpoch, SeedRoot, GeneratorVersion, RegistryRoot,
 QualificationProfile, DependencyRoots, RuntimeApplicabilityPredicate
}
```

At use time compare current state and relevant dependencies with the qualified compile profile. Epoch mismatch triggers *dependency-sensitive* reassessment, not automatic denial for irrelevant changes or automatic acceptance for matching IDs. Material changes requalify. Existing ActionGate/VEI controls current authority, final action parameters and actual effects. **Output:** RuntimeQualificationReceipt.

### RSDC-08 — Minimal Seed Extraction (v15.10 reconstruction)

Search for a smaller explicit seed S such that `VerifiedClosure(S)` reconstructs the frozen controlling corpus C at required semantic fidelity. Fundamental rights/constitutional commitments stay explicit. All material obligations, exceptions, failures, UNKNOWN states and dependencies must be preserved; percentage thresholds never excuse a missing hard rule. Search can claim a minimum only inside a declared proven finite domain. **Output:** MinimalSeedCandidate + ReconstructionReceipt.

## Common change artifact

```text
ObligationDiff {
 SourceEpoch, TargetEpoch, SeedAndRegistryRoots,
 Added[], Removed[], Strengthened[], Weakened[], Unchanged[],
 Conflicts[], Unknowns[], Exceptions[], DependencyChanges[],
 HumanEffectChanges[], EvidenceRefs[], TestRefs[], AdmissionStatus
}
```

Every proposed upgrade emits ObligationDiff. Removed/weakened controlling obligations require explicit justification, independent checking and admission; a generated diff never approves itself.

## Hard invariants

- **RSDC-I01:** No generated authority, rights or constitutional commitments without valid external grounding.
- **RSDC-I02:** No silent predecessor-obligation or exception loss.
- **RSDC-I03:** UNKNOWN/CONFLICT/INCOMPLETE cannot silently become PASS.
- **RSDC-I04:** No circular self-verification or self-admission.
- **RSDC-I05:** No material Human-Effect omission through recursion, composition or abstraction.
- **RSDC-I06:** No false independence from added reviewers or representation levels.
- **RSDC-I07:** No stale qualification reuse after material dependency change.
- **RSDC-I08:** No corpus reduction without independent full-fidelity reconstruction.
- **RSDC-I09:** No unbounded recursion or unreported resource exhaustion.
- **RSDC-I10:** No duplicate controlling semantic ownership.

## Supporting automation

- **Coverage-guided search:** prioritize uncovered SAL-valid material classes, never treat coverage percentage as authority.
- **Blind triangulation:** separate proposer, falsifier, evidence and admission control under REP.
- **Historical counterexamples:** retain past failures/UNKNOWN/blocked cases as context-bound test seeds.
- **Differential DesignEpoch replay:** compare qualified behavior under old/new epochs; flag unauthorized deltas.
- **ObligationDiff checking:** machine-readable classification and independent validation of semantic changes.

## Conformance plan and acceptance

**A. Operator correctness:** synthetic frozen fixtures; deterministic replay, types, bounds, receipts, non-PASS and termination.

**B. Blinded reconstruction:** hide stratified existing v15.5/v15.10/v15.11 invariants, schemas, contracts, states, tests, proof obligations, exceptions and dependencies; score each independently.

**C. Novel discovery:** assess new obligations/theories against existing owners; independent falsification, explanatory gain, false-positive/duplicate rates and Human-Effect analysis.

**D. Adversarial regression:** seed invention, colluding verifiers, representation convergence, drift, false fixed points, exception erasure, runtime mismatch and self-admission.

**E. Existing admission decision:** independent evidence/receipts, unresolved frontier and exact source-owner mappings; no automatic promotion.

All applicable hard invariants must PASS for claimed scope. Freeze statistical thresholds before testing. Any material unexplained reconstruction loss or UNKNOWN equivalence blocks retiring affected explicit semantics.

**Implementation order:** OCFP + ObligationDiff → AMG → IDTD duality → Minimal Seed Extraction → owner/REP/epistemic/runtime integration.

**Status discipline:** Candidate specification only. No operator is claimed implemented, tested, proven or admitted. Canonical v15.5 and predecessor source remain unchanged.
