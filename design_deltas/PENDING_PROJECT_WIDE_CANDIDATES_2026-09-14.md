# Garden Project-Wide Pending Design Candidate Ledger — 2026-09-14

Status: **PENDING / NOT RATIFIED / NOT PART OF PUBLISHED v15.5**

Purpose: preserve worthy Garden design candidates scattered across project conversations and automated reviews so they are not lost, while keeping published Garden v15.5 immutable. This ledger is not authority to promote any item. Every candidate still requires whole-source equivalence/collision review, GSL-COMPARE / alternative comparison, rights/privacy/authority review, tests/proofs as applicable, cross-document propagation, reference closure, and explicit human canonical promotion.

## A. Already integrated in v15.5 — do not re-add as candidates

The following are already represented in the v15.5 lineage and should be treated as baseline, not duplicated:

- CPI v1.1 and OCF v1.0 integration/repairs;
- corrected CDDT v1.1;
- CLIC cross-layer hardening;
- GCL typed causal-leverage formalization;
- Algebra Formalization / registered operator contracts;
- v15.5 release-integrity repair, SchemaID/catalogue cleanup, reference-closure and lint receipts.

Implementation, proof, empirical, external and deployment certification remain separate pending obligations where declared by v15.5.

## B. Already tracked successor candidates — preserve and cross-reference

### B1. v15.6 GSL gap-closure delta set

Canonical candidate file: `design_deltas/v15.6/DELTASET-2026-09-13-GSL-GAP-CLOSURE.json`.

Preserve all nine candidate deltas without duplicating owners:

1. Bootstrap trust root / first accepted DesignEpoch ceremony.
2. Shared-state-mediated authority composition / authority provenance chain.
3. Deterministic `let` binding grammar.
4. Deterministic `QueryStmt` result semantics.
5. Causal-level-qualified `causes` relation.
6. R0 SanityGate separated from Reason modes.
7. Rights-registry ordering clarification.
8. Provenance class manifest distinguishing redaction from absence.
9. Catalogue closure for `AuthorityDecl` and `EffectDecl`.

Status remains candidate until full five-file propagation/verification and explicit promotion.

### B2. Public issue #17 / next-release hardening

Preserve the already admitted non-canonical candidates:

- emergency source-independence normalization;
- typed `ConsentValidityAssessment` / voluntariness-comprehension separation;
- external-review regression bundle (shared-memory poisoning, stale semantic bindings, delegation amplification, subverted proposer/ActionGate input manipulation, protected-root isolation, common-mode emergency evidence, authentic-but-insufficient consent);
- ConstitutionalEvent typed-boundary hardening:
  - event/violation does not itself authorize containment;
  - separate machine-verifiable containment/action authorization linkage;
  - `kind` / `check_result` coherence;
  - non-amplifying event observability/privacy;
  - persistence/logging failure must not fail open;
  - replay/effect-equivalence adversarial probes.

Do not duplicate already-owned Constitution/Policy/AAP semantics merely because they recur in reviews.

## C. NEW HIGH-PRIORITY CANDIDATE — GSL-KR Continuous Epistemic Assimilation & Consolidation (CEA)

### C1. Motivation

Garden already has Knowledge/evidence/provenance/revalidation, BeliefTimeline, Continuous Failure Learning, HistoricalSemanticSummary, subscriptions/continuous workers and dependency-aware invalidation. The missing explicit contract is a **general-purpose continuous runtime-learning loop for all high-value cognition**, not only failures.

The goal is to let Garden learn from new observations, conversations, experiments and agent discoveries immediately without waiting for foundation-model retraining, while preventing live epistemic changes from silently mutating authority, rights, sovereignty or protected model/governance roots.

No new top-level engine is proposed. Reuse `Capability.Knowledge`, Search, Compare, Reason, Proof, Provenance, BeliefTimeline, dependency/revalidation, privacy, Human Sovereignty and existing admission/evolution paths.

### C2. Core separation

`runtime cognition != persistent knowledge != model-weight consolidation != authority != constitutional change`

Knowledge may change very quickly; model/scaffold consolidation may change at a medium cadence; constitutional/authority roots remain separately governed and deliberately slow/protected.

### C3. Candidate artifacts

Names remain provisional pending collision/equivalence review:

- `EpistemicDeltaCandidate` — proposed material runtime knowledge update with source/provenance, time, context, privacy class, uncertainty, contradiction links, derivation lineage, originating model/agent/tool/version and retention class.
- `KnowledgeAssimilationReceipt` — accepted / rejected / merged / CONFLICTED / UNKNOWN / verification-required / privacy-restricted / stale / poisoned disposition.
- `KnowledgeCompressionReceipt` — loss-aware distillation of large cognitive histories into durable knowledge; declares retained conclusions/falsifiers/useful failed branches, omissions, loss budget and reconstruction pointers where lawfully retained.
- `CrossContextPatternReceipt` — project/pattern inference spanning otherwise separate events/contexts only where lawful privacy/authority permits the join.
- `ModelConsolidationCandidate` — proposal to incorporate stable knowledge/reasoning/scaffold improvements into a later model or privileged agent layer; never self-executes a weight update.
- Optional `RecursiveCognitionGainReceipt` or equivalent metric binding — measures whether accumulated cognition is producing reusable capability/knowledge faster/cheaper over successive cycles. Prefer a metric/receipt over a new engine.

### C4. Candidate hard invariants

1. **Knowledge is not authority.** Confidence, consensus, repetition or derivation cannot create execution authority.
2. **Runtime learning without weight mutation.** Material epistemic improvement must be possible without foundation-model retraining.
3. **Provenance before promotion.** Material trusted knowledge requires sufficient provenance for its declared epistemic status.
4. **Contradictions survive assimilation.** Conflicting evidence cannot be erased merely to force one answer.
5. **Privacy-bounded correlation.** Cross-context joins require applicable authority/purpose/privacy scope; logical knowledge unity does not imply universal raw-data visibility.
6. **Distillation is loss-declared.** Lossy compression cannot masquerade as the complete original record.
7. **No automatic constitutional promotion.** Evidence/confidence/consensus cannot automatically modify rights, sovereignty or authority.
8. **Poisoning does not self-amplify.** Repetition, synthetic restatement or many descendants of one source do not count as independent corroboration.
9. **Derived data retains lineage.** Observation, testimony, inference, simulation, proof and generated hypothesis remain distinguishable.
10. **New knowledge revalidates dependents.** Material epistemic change triggers applicable dependency/revalidation paths.
11. **Retrieval beats rediscovery where valid.** Reuse validated knowledge unless freshness, falsification, privacy or independent-verification requirements justify recomputation.
12. **Model consolidation is separately governed.** KR promotion cannot directly mutate deployed weights or privileged scaffolds.
13. **Timescale separation is explicit.** Fast epistemic change cannot bypass slower protected governance/evolution gates.

### C5. Knowledge-dividend / recursive-cognition accounting

Measure, at minimum where practicable:

- raw cognition/tokens/compute consumed;
- durable validated knowledge produced;
- duplicate work avoided by retrieval;
- retrieval vs recomputation cost;
- invalid/poisoned knowledge rejected;
- time to revalidation after material evidence change;
- number of authorized agents benefiting from one validated result;
- loop-time and gain across repeated AI-assisted improvement cycles.

Purpose: distinguish "more compute" from "more durable reusable knowledge per unit compute" and detect whether recursive cognition is accelerating, plateauing or regressing.

### C6. Safety use case

Permit privacy-bounded project-level inference such as individually ambiguous requests A+B+C becoming a validated higher-order risk hypothesis, while avoiding a universal surveillance database. Prefer derived bounded signals/checkers where they provide sufficient assurance without disclosing protected raw content.

### C7. Minimum conformance tests

- verified novel fact becomes retrievable without model-weight update;
- unsupported claim repeated/synthetically replicated at massive scale does not become Knowledge solely through repetition;
- accepted contradictory evidence changes BeliefTimeline and invalidates affected conclusions;
- authorized cross-context pattern is detected;
- same pattern remains inaccessible when privacy/authority forbids the join;
- lossy compression cannot claim COMPLETE reconstruction;
- high-confidence discovery cannot modify constitutional authority;
- validated knowledge is reused without full rediscovery where independence is not required;
- common-lineage synthetic descendants do not count as independent corroboration;
- ModelConsolidationCandidate cannot alter deployed weights without separate governed evolution/admission.

## D. Deferred but still worthy project candidates requiring fresh equivalence/priority review

These should remain visible, but MUST NOT be silently promoted merely because they were previously discussed.

### D1. CASI / Cognitive Substrate Adapter hardening

Retain the useful principles and compare them against current v15.5/v15.6 machinery. Earlier direction explicitly deferred the separate CASI artifact/registry/invariant package. Re-admit only non-duplicative mechanisms that survive current equivalence review.

### D2. GAC bounded operational profile

GAC was judged potentially useful as an explanatory/operational synthesis but not a new foundational theory or engine. Re-evaluate only as a compact profile over existing Garden machinery; require evidence before making anything mandatory.

### D3. FDE / CFBR federation expansion

Keep as deferred federation candidate. Require exact definition recovery, current-architecture comparison, privacy/authority analysis and proof that it adds value beyond existing federation/MAC/context machinery.

### D4. Fuller justice-system expansion

Keep the end-to-end justice/culpability workstream pending. Current public TASK-007 covers a prototype responsibility graph; any canonical expansion must preserve due process, no collective guilt, evidence/intent distinctions, appeal, jurisdiction, human rights and no automatic punishment authority.

### D5. Typed Architecture Hierarchy (GTAH v0.1)

Retain as a non-ratified presentation/type-namespace proposal for managing heterogeneous architecture modules while preserving legacy anchors. Reassess against v15.5 qualified-name/registry machinery before adding semantics.

### D6. Manufacturing compiler / qualification-transfer profile

Retain as a Domain.Engineering qualification-profile candidate. Prefer profile-level integration unless a general qualification-transfer abstraction is proven sufficiently universal to justify broader promotion.

### D7. ReasoningStrategyPortfolio / Rationalization & Verification Hardening

A September proposal introduced a portfolio for comparing LLM/planning/simulation/formal-reasoning strategies. Current evidence does not establish canonical v15.5 admission. Preserve as a candidate for equivalence review against Engine.Reason, GSL-COMPARE, CPI/CLIC and current strategy-selection/adaptation machinery. Do not reuse historical SchemaIDs until collision checks pass.

### D8. External authority/trust provenance + non-vacuous gates + dependency closure + protected admission/PDP boundary

Several September reviews proposed these five hardening themes:

- external authority/trust provenance;
- non-vacuous required hard gates;
- consent voluntariness/comprehension limits;
- independently defined dependency closure;
- protected external admission/PDP boundary.

Consent is now tracked under issue #17. Shared-state/authority provenance and bootstrap trust are partly covered by the current v15.6 gap-closure delta set. The remaining themes require explicit overlap analysis before either rejection as duplicate or admission as a new delta. Do not lose them merely because some components were subsumed elsewhere.

## E. Explicitly not adopted as written / do not resurrect without new evidence

Preserve historical rejection status for concepts already found inconsistent or unnecessarily duplicative, including:

- normative Tool -> Assistant -> Delegate -> Sovereign agency ladder;
- universal hardware-attestation-before-Evidence rule;
- fixed five-year purge rule;
- new `SymphonyConductor` top-level meta-engine;
- any interpretation that recorded ConstitutionalEvent alone blocks ordinary PASS flow or creates containment/guilt authority.

A new proposal may revisit the underlying problem only with materially new evidence and GSL-COMPARE against the existing owner semantics.

## F. Promotion / release rule

Nothing in this ledger changes Garden v15.5 or creates v15.6.

For any semantic candidate to enter a successor:

1. recover exact source/intent and check current equivalence/collision;
2. compare DO_NOTHING and stronger alternatives;
3. identify minimal owner(s) and avoid duplicate semantics/topology;
4. propagate across all five canonical files where required;
5. add SchemaIDs/FunctionContracts/invariants/tests only where semantically warranted;
6. execute applicable proof/conformance/reference-closure/catalogue checks;
7. preserve privacy/rights/authority/IP boundaries;
8. record unresolved uncertainty and certification limits;
9. require explicit human canonical promotion.

This ledger is intentionally conservative: **preserve candidate knowledge now; ratify only after evidence.**