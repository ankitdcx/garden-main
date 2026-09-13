# SWARM-001 — Garden v15.5 free-swarm calibration cross-reference

Status: CANDIDATE TRIAGE — NOT A SUCCESSOR PATCH
Date: 2026-09-13
Public source: ankitdcx/garden-swarm PR #25 calibration, Garden v15.5 first Human-file work package
Admission rule: public-agent outputs are proposals only; full-corpus evidence controls disposition.

## Summary

The four-role zero-cost calibration generated 18 candidate findings. Cross-reference against the full Garden v15.5 System, Technical and Annexure source shows that most are bounded-context false gaps: the Human file intentionally points to lower-level owners for schema/contract detail. No candidate is automatically admitted.

## Dispositions

1. Release-integrity repair claims absent from Human chunk — **ALREADY_COVERED**. Annexure [A-V155]/A.61-A.63 contains typed GCL repair, CLIC bindings, reference-closure rules and the v15.5 release-receipt identity.
2. Epistemic-boundary assertion lacks formal grounding — **ALREADY_COVERED / MISFRAMED**. K-INT-001..010 and Technical epistemic/type/stage rules formalize the relevant separations; the Human/header sentence is a scope disclaimer, not a standalone proof claim.
3. DesignSimulationReceipt / GlobalInvariantConsistencyReceipt undefined — **ALREADY_COVERED**. Technical [T-DESIGN-MIRROR] and [T-GLOBAL-CONSISTENCY] provide schemas and contracts.
4. ConstitutionalEvent semantics underspecified — **ALREADY_COVERED**. Technical [T-CONSTITUTIONAL-EVENTS] defines SCHEMA-92D37B160F, event fields and VETO semantics.
5. BeliefTimeline / EpistemicTransition lack contract — **ALREADY_COVERED**. Technical [T-BELIEF-TIMELINE] defines HistoricalEpistemicState, BeliefTimeline, EpistemicTransition and query interface.
6. Human 0-9 view can drift from typed graph — **ALREADY_COVERED**. [T-ARCH] plus Annexure REG-ARCH-NAME-001 make stable identity/qualified binding authoritative and explicitly deny authority from display position.
7. Scheduling responsibility overlap — **ALREADY_COVERED**. Human/System explicitly separate Runtime queues, Time temporal eligibility, Event delivery/subscriptions and Orchestrate/AAP admission; Technical scheduling/backpressure contracts define failure/load dispositions.
8. Constitutional violation may wait indefinitely for containment — **NEEDS_EVIDENCE, NOT A CONFIRMED DEFECT**. VETO blocks the transition and containment has separate authority/evidence rules. A universal fixed deadline is not justified; test whether applicable risk/deadline profiles can leave a consequential blocked transition without bounded disposition.
9. BeliefTimeline historical isolation mechanism unspecified — **ALREADY_COVERED**. HistoricalEpistemicState binds DesignEpoch, KnowledgeSnapshot, event boundary, reconstruction completeness and provenance; timeline explicitly records gaps/unknown intervals.
10. DesignMirror MERGE_READY gate unclear — **ALREADY_COVERED**. [T-DESIGN-MIRROR] states that when simulation is required, MERGE_READY requires a fresh acceptable DesignSimulationReceipt or terminal BLOCKED/UNKNOWN, and all applicable obligations still pass ordinary gates.
11. Chunk ends before implementation detail — **REJECTED AS COVERAGE LIMITATION**. The calibration deliberately supplied one bounded Human chunk; absence there is not absence from Garden.
12. v15.5 wrapper contains embedded 'CURRENT v14.8.5 RELEASE PROFILE' labels — **IMPROVEMENT_CANDIDATE (DOCUMENT IDENTITY CLARITY)**. The top-level v15.5 header, SOURCE_MANIFEST and Annexure [A-V155] establish the current release unambiguously, so this is not release-identity loss; however retained 'CURRENT v14.8.5' wording inside current v15.5 files can confuse readers/tools and should be normalized or explicitly marked historical/embedded in the next source successor.
13. Canonical identity control undefined — **ALREADY_COVERED**. Annexure REG-ARCH-NAME-001 owns naming/alias resolution and collision/ambiguity rules.
14. Activation paths lack bounded failure contract — **ALREADY_COVERED IN PRINCIPLE**. Technical trigger/scheduling contracts include rate/resource/circuit bounds and ADMIT/COALESCE/DEFER/SHED_OPTIONAL/REJECT/SAFE_FALLBACK/ESCALATE; failed/unknown hard gates remain explicit. Implementation conformance is still pending, as the release already states.
15. Emergency-envelope crossing/atomic validation incomplete — **NEEDS_EVIDENCE / HARDENING CANDIDATE**. Existing AuthorityLease/SafetyEnvelope/DesignEpoch invalidation machinery covers bounded authority and expiry, but this calibration did not establish a single atomic crossing contract for every emergency/degradation profile. Review owner contracts and derive a concrete race/staleness counterexample before patching.
16. ConstitutionalEvent observability may not imply timely/atomic detection — **NEEDS_EVIDENCE / HARDENING CANDIDATE**. Current contract guarantees typed event emission, VETO blocking and immutable history, but a concrete implementation must show fail-closed behavior if event persistence/routing fails. Derive a reproducible fault-injection test before changing source semantics.
17. BeliefTimeline completeness/staleness contract missing — **ALREADY_COVERED / IMPLEMENTATION PENDING**. Schemas contain event boundary, snapshots, DesignEpoch, reconstruction completeness, gaps/unknown intervals, dependency closure and provenance. Runtime enforcement remains to be implemented/certified.
18. DesignMirror closure/receipt acceptance criteria missing — **ALREADY_COVERED**. DesignMirror records included/omitted refs with justification and dependency closure; DesignSimulationReceipt records unsupported obligations and comparison; MERGE_READY remains conditional on applicable obligations.

## Net result

- Confirmed current-source defects: **0**
- Documentation-clarity successor candidate: **1** (#12)
- Concrete hardening hypotheses requiring counterexample/tests: **3** (#8, #15, #16)
- Already covered / bounded-context false gaps / implementation-status restatements: **14**

## Required next work

For #8, #15 and #16, construct harmless deterministic fixtures/fault-injection tests before proposing any new schema or invariant. For #12, compare a minimal release-banner normalization against DO_NOTHING and verify hashes/reference closure in a future successor; do not rewrite published v15.5 source in place.
