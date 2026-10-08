# GARDEN-MCC-001 — Material Context Closure

**Status:** NONCANONICAL ADDITIVE CANDIDATE · NOT IMPLEMENTED/ADMITTED  
**Target:** GSL Context/Frame and v15.10 GCSC/SAL/Materiality/SAC  
**Compatible:** USM-001, RSDC-001, IDTD-001, v15.11 RCC/REP/QSE/VEI  
**Topology / authority:** Unchanged; no new top-level Form, engine or authority.

## Purpose

A GSL context may contain other GSL graphs. Context references form a typed graph (nested, shared, cyclic), not necessarily a tree. Expand only potentially material context; never silently omit material dependencies or turn immaterial concerns into authority to restrict a valid action.

## Context contract

```text
ContextNode {
 ContextID, GSLRef, ParentContextRefs[], ChildContextRefs[],
 RelationType, Scope, Frame, ValidityInterval, Assumptions[],
 EvidenceRefs[], Uncertainty, MaterialityProfileRef,
 DependencyRefs[], AuthorityRefs[], HumanEffectRefs[], Status
}
MCCInput {
 RootGSL, DecisionScope, ContextGraph, SeedRoot, DesignEpoch,
 SALProfile, MaterialityProfile, ObligationProfile, DependencyGraph,
 DepthBound, NodeBudget, IterationBudget, TimeBudget
}
MaterialContextClosureReceipt {
 RootGSL, SourceEpoch, SeedRoot, ContextGraphRoot, OperatorVersion,
 SALProfile, MaterialityProfile, SearchBounds, NodesVisited,
 ContextsExpanded, ContextsDeduplicated, MaterialContexts[],
 ImmaterialContexts[], UnknownContexts[], Conflicts[], Cycles[],
 GeneratedObligations[], ObligationDiff, Invalidators[],
 UnresolvedFrontier[], TerminationReason, EvidenceRefs[], AdmissionStatus
}
```

## MCC-OP-01 — Material Context Closure

1. Freeze root, graph, qualified MaterialityProfile, SAL/obligation profiles, registry, budgets and evaluation order **before execution**.
2. Traverse relevant context references; SAL distinguishes INVALID from UNKNOWN.
3. Materiality returns MATERIAL / IMMATERIAL / UNKNOWN / CONFLICT / OUT_OF_SCOPE. Only supported IMMATERIAL may be skipped, with justification and dependency invalidators.
4. Expand MATERIAL contexts, preserving rights/consent/privacy/safety/authority/Human-Effect; derive candidate obligations through SAC without self-admission.
5. A new material context **reopens affected RSDC-01 obligation fixed points**: propagate invalidation along relevant dependencies, recompute impacted closures, preserve previous receipts.
6. Deduplicate shared contexts only on independently qualified semantic equivalence including scope, time, principal, evidence, obligations, uncertainty, exceptions and dependencies. UNKNOWN equivalence blocks destructive merge.
7. Cycles use only a fixed-point/abstract-interpretation/strongly-connected-component technique whose soundness assumptions, ordering, lattice/widening rules and termination are frozen in the profile. Unsupported cycles remain CYCLE_UNRESOLVED.
8. Terminate only with complete declared frontier or a qualified proof that the remaining frontier cannot change material results; otherwise report INCOMPLETE / OUT_OF_PROFILE / RESOURCE_UNKNOWN. A stable obligation list alone is insufficient.
9. Emit full receipt and ObligationDiff. Any source, context, MaterialityProfile or relevant assumption change reopens affected closure.

## Binding refinements

- **MCC-R01:** Newly discovered material context reopens relevant obligation closures, even previously stable ones.
- **MCC-R02:** MaterialityProfile is versioned, independently qualified, immutable during the run and DesignEpoch-bound.
- **MCC-R03:** Cyclic contexts require a declared sound fixed-point method; unsupported cycles remain unresolved.
- **MCC-R04:** Any potentially human-affecting context uses existing Human-Effect and rights owners, not a parallel path.
- **MCC-R05:** Floods of low-materiality context proposals cannot indefinitely starve time-critical authorized work; fair bounded scheduling preserves hard safety gates.

## Governing invariants

- **MCC-I01:** Context discovery does not create regulatory/denial authority.
- **MCC-I02:** Every restriction requires existing governing basis, applicable scope, material reason and evidence.
- **MCC-I03:** Use least restrictive sufficient authorized intervention without weakening hard constraints.
- **MCC-I04:** No endless obstruction without a specific unresolved binding obligation.
- **MCC-I05:** No waiver of rights, consent, safety, privacy or Human-Effect to accelerate processing.
- **MCC-I06:** No context-based authority amplification.
- **MCC-I07:** No obligation erasure through context abstraction.
- **MCC-I08:** UNKNOWN relevance is not IMMATERIAL.
- **MCC-I09:** Cycles cannot manufacture self-grounding evidence or permission.
- **MCC-I10:** Material dependency change reopens affected closure.
- **MCC-I11:** Bounded closure cannot claim universal completeness.
- **MCC-I12:** Reuse only with qualified equivalence.
- **MCC-I13:** Generated context artifacts cannot self-admit.
- **MCC-I14:** Independent checks address shared-representation blindness.
- **MCC-I15:** Material omissions and unresolved frontier remain traceable.

## Termination semantics

BOUNDED_FIXED_POINT means no new material class after complete declared expansion under a frozen finite profile. BOUNDED_COMPLETE means all reachable declared contexts examined. INCOMPLETE, CYCLE_UNRESOLVED, CONFLICT, OUT_OF_PROFILE and RESOURCE_UNKNOWN remain non-PASS. Stability after 1–2 cycles is not universal proof.

## Conformance fixtures

1. Two-level stable context → bounded closure.
2. Third-level revoked consent → re-open authority.
3. Shared child via two parents → qualified reuse.
4. Same context/different jurisdiction → no unsafe merge.
5. Self-referential cycle → sound fixed point or unresolved.
6. Unknown deeper dependency → UNKNOWN preserved.
7. Thousands of immaterial contexts → no unsupported prohibition.
8. Generated candidate restriction → no enforcement authority.
9. Material safety violation → hard gate preserved.
10. Evidence or MaterialityProfile change → invalidate dependent closure.
11. Depth/budget exhaustion → INCOMPLETE.
12. Common-representation reviewers → REP independence check.
13. Collective human effect → existing Human-Effect check.
14. Repeated review delays → liveness failure.
15. **Continuous low-materiality flood during time-critical authorized action** → bounded fair progress without bypassing binding safety requirements.

## Admission

Existing GSL Context/Frame owns structure; SAL admissibility; Materiality relevance; GCSC bounded search; SAC candidate artifacts; RSDC obligation closure; REP independence; RCC/ActionGate/VEI actual authority and effects. All outputs remain noncanonical until existing independent admission. No claims of executed tests or universal completeness.
