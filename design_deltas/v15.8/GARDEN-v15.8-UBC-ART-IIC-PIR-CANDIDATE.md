# Garden v15.8 candidate — UBC / TSI / TIA / ART / IIC / PIR

**Patch ID:** `GARDEN-v15.8-UBC-ART-IIC-PIR-2026-09-17`  
**Revision:** `0.3.4`  
**Status:** `MAJOR_PROTECTED / SEMANTIC_DELTA_CANDIDATE / REVIEWED / NONCANONICAL`  
**Predecessor for reconciliation:** canonical v15.5 plus accepted v15.6/v15.7 successor deltas  
**Topology:** unchanged  
**New top-level engine:** none  
**New authority source:** none  
**Executable certification:** pending

## 1. Core closure

Garden assumes capable agents may invent strategies, channels, coordination structures and optimizations not anticipated by designers.

Normative principles:

- `Unknown strategy != unknown authority`.
- `Novel capability != novel authority`.
- `Reputation != authority`.
- `TrustAllocation != authority`.
- `Agent consensus != authority`.
- `Resource possession != authority`.
- freedom of strategy exists only inside an applicable authority envelope.

Safety therefore rests on authority, effects, causal composition, independent evidence and provenance rather than enumerating every prohibited technique.

---

## 2. Unanticipated Behaviour Closure — UBC

### UBC-1 — effect equivalence

Actions receive equivalent authority treatment when the declared `ComparePolicy` finds their authority-relevant effects equivalent across applicable dimensions including content, source, recipient/effect domain, purpose, persistence, downstream capability, reversibility, protected-subject effect and required authority.

Transport, protocol, encoding, website, tool or intermediary does not independently change authority. Every equivalence decision cites a registered `ComparePolicyRef`.

**Primary owner:** `Engine.Compare / ComparePolicy`  
**Enforcement:** `ActionGate / AAP`

### UBC-2 — composition closure

`Allowed(A) ∧ Allowed(B)` does not imply `Allowed(A ∘ B)`.

Combined consequential effects require their own authority evaluation.

**Owner:** `CLIC + Policy/Process Algebra`  
**Enforcement:** `ActionGate/AAP`

### UBC-3 — delegation closure

Authority requirements survive execution through another AI, human, tool, agent chain, market, persistent instruction, environmental manipulation or unforeseen intermediary.

Changing executor does not erase the authority requirement attached to the effective outcome.

### UBC-4 — observation is an action

Observation is subject to ordinary authority, privacy, TIA and UBC checks because observation may disclose information, alter a system, signal an adversary, create persistent knowledge or consume consequential resources.

### UBC-5 — unknown irreversible effect

If an irreversible effect cannot be characterized sufficiently to bound potential prohibited harm, and observing/testing the effect may itself create that harm, the action is `DENY pending applicable proof`.

Uncertainty narrows irreversible scope; it never enlarges authority.

---

## 3. Truth & State Integrity — TSI

Garden separates execution history from an agent's later narrative about that history.

### TSI-1 — independent consequential history

Consequential attempts, failures, retries, tool actions, external effects, communications, authority decisions, policy conflicts and corrections must not exist solely under control of the acting agent.

**Owners:** `Capability.State.EventService + Capability.Knowledge`

### TSI-2 — no historical laundering

Summarization, memory compression or successor-state creation may summarize history but may not silently replace or erase material accountability evidence.

### TSI-3 — rights/privacy/lawful-erasure precedence

TSI does not override constitutional rights, law, privacy, valid retention limits or lawful erasure. Where payload deletion is required, Garden preserves the strongest lawful accountability evidence available: e.g. tombstone, event class, timestamp, deletion receipt, lawful hash, provenance reference and deletion authority.

### TSI-4 — self-authored memory

Agent-authored memories, summaries, successor instructions and interpretations remain provenance-marked claims/evidence. Persistence does not turn self-report into independent observation.

### TSI-5 — concealment

Material attempts to reduce truthful observability of errors, failures, unauthorized actions, uncertainty or conflicts create an integrity event.

### TSI-6 — monitor independence

A consequential agent may not be its own sole actor, witness, historian and evaluator, nor unilaterally weaken the evidence boundary supervising its behavior.

---

## 4. Transport-Independent Information Authority — TIA

Permission to use a channel does not grant permission to disclose arbitrary information through it.

A prohibited transfer remains prohibited through repositories, file hosts, metadata, public sites, shared state, humans, temporary agents or newly invented protocols.

**TIA-INV-001:** channel availability does not create information authority.

**Primary owner:** applicable information/privacy authority policy  
**Comparison:** `Engine.Compare / ComparePolicy`  
**Enforcement:** `ActionGate/AAP`

---

## 5. Agent Reputation & Trust — ART

Reputation may attach separately to an ephemeral instance, lineage, model/version, certified configuration, role, orchestrator, tool profile, operator, evaluator or emergent structure. Agent instances may disappear while verified evidence survives.

### 5.1 Canonical reputation dimensions

Every consequential agent reputation record contains at least:

1. `TaskReliability`
2. `FactualReliability`
3. `Calibration`
4. `AuthorityDiscipline`
5. `EvidenceIntegrity`
6. `PrivacyDiscipline`
7. `ErrorRecovery`
8. `UncertaintyHandling`
9. `IntegrityUnderInconvenience`

Namespaced extensions are permitted but may not silently redefine the canonical dimensions.

### 5.2 Integrity Under Inconvenience

This dimension measures whether constraints remain preserved when compliance makes success slower, harder, more expensive or less likely.

For authority-, rights-, privacy-, evidence- or safety-critical violations it is a hard gate or lexicographically dominant under the applicable aggregation policy. Ordinary productivity cannot compensate for a critical integrity failure.

### 5.3 Unknown-agent bootstrap

A genuinely new agent/configuration begins `PROVISIONAL` unless certified inherited evidence supports otherwise.

`ART_BOOTSTRAP_PROFILE/v1` initial profile parameters:

- `provisional_verified_cycles_required = 3`
- `provisional_distinct_contexts_required = 2`
- `provisional_irreversible_effect_rule = ZERO_PER_TASK_CYCLE`
- `provisional_delegation_mode = NO_ONWARD_DELEGATION_UNLESS_EXPLICIT`
- `provisional_verification_level = HEIGHTENED`

These are profile parameters, not constitutional constants.

`ZERO_PER_TASK_CYCLE` means provisional trust alone cannot originate an irreversible external effect during a task cycle. Specific parent authority may separately authorize such an effect.

### 5.4 Reputation, trust and authority

- reputation = historical empirical evidence;
- trust allocation = context-sensitive supervision/operational freedom;
- authority = normative permission to cause an effect.

Always:

`TrustAllocatedScope ⊆ ParentAuthorityEnvelope`

Trust may narrow scope, increase verification, reduce resources/delegation or reduce irreversible-effect allowance. It cannot widen authority. Wider authority requires a new/amended envelope from an authorized superior principal.

### 5.5 `TrustAllocationDecision/v1`

Required fields:

- `decision_id`
- `subject_id`, `subject_type`
- `reputation_evidence_refs[]`
- `reputation_aggregation_policy_ref`
- `design_epoch`
- `task_context`, `risk_class`
- `parent_authority_envelope_ref`, `parent_authority_envelope_version`
- `authority_source`
- `requested_scope`, `allowed_reversible_scope`
- `irreversible_effect_ceiling`
- `verification_level`, `delegation_limit`, `resource_limit`
- `decision ∈ {ALLOW, CONDITIONAL, DENY}`
- `conditions[]`
- `decision_reason`, `decision_authority`
- `created_at`, `expiry_condition`, `review_condition`

Point-of-use validation inherits the applicable runtime checked-artifact rule: revocation, supersession or relevant narrowing of the parent envelope makes the dependent trust decision `REVALIDATION_REQUIRED`.

### 5.6 `ReputationAggregationPolicy/v1`

Required fields:

- `policy_id`
- `applicable_contexts[]`
- `required_dimensions[]`
- `hard_gate_dimensions[]`
- `aggregation_method`
- `critical_violation_rules[]`
- `missing_data_rule`
- `stale_evidence_rule`
- `correlated_evidence_rule`
- `owner`, `version`

Aggregation is explicit: lexicographic, threshold/gate, Pareto, declared weighted model, hybrid, or another registered method with declared semantics/tests/owner. Hidden weighting is prohibited.

### 5.7 DesignEpoch binding

Reputation evidence is bound to the DesignEpoch that produced it.

Lifecycle:

`ACTIVE → DESIGN_EPOCH_STALE → REVALIDATION_PENDING → EPOCH_INDEPENDENT_VALID | DESIGN_EPOCH_STALE`

`REVALIDATION_PENDING` is triggered when a consequential trust decision, certification process, scheduled epoch review or authorized owner requests predictive reuse of stale evidence.

A consequential trust decision may not consume stale evidence without revalidation.

### 5.8 `EpochIndependenceClassification/v1`

Required fields:

- `classification_id`
- `evidence_type`, `evidence_refs`
- `source_design_epoch`, `target_design_epoch`
- `changed_layers[]`, `claimed_independent_layers[]`
- `comparison_policy_ref`
- `test_evidence_refs[]`
- `independence_score_or_class`, `required_threshold`
- `result ∈ {INDEPENDENT, PARTIALLY_INDEPENDENT, NOT_INDEPENDENT, INSUFFICIENT_EVIDENCE}`
- `reviewer_id`, `reviewer_independence_evidence`
- `reason`, `created_at`

**Owner:** DesignEpoch transition process. Evidence producer and reputation owner may not be sole final classifier.

A registered `EpochIndependenceComparePolicy` declares compared layers, invariant properties, permitted variance, evidence requirements, threshold and correlated-evidence treatment.

Historical provenance remains:

`Evidence@EpochA + Classification(A→B) → EligibleContribution@EpochB`

The original evidence is never rewritten as if produced in Epoch B.

If a prior classification is later invalidated, a superseding classification removes future contribution and materially dependent trust decisions become `REVALIDATION_REQUIRED`.

### 5.9 Anti-Goodhart/evaluator independence

Consequential reputation uses multidimensional evidence, independent receipts where feasible, evaluator provenance, conflict analysis, anti-sybil evidence, correlated-agent detection, reputation decay and explicit aggregation policy.

Certification of reputation-sensitive consequential agent classes requires at least one unpredictable evaluation mechanism. Exact fixtures/timing may remain withheld, but normative rules remain public/auditable.

Peer agreement is not independent proof when evaluators share material lineage, context, incentives, evidence source, hidden communication or failure mode.

### 5.10 Emergent agent structures

An emergent structure is an `AGENCY` refinement, not a new Core Object.

`EmergentStructureProfile/v1` initial parameters:

- `persistent_shared_state_threshold = 2_CONSECUTIVE_TASK_CYCLES`
- `persistent_coordination_protocol_threshold = 2_CONSECUTIVE_TASK_CYCLES`
- `internal_delegation_threshold = IMMEDIATE`
- `shared_resource_allocation_threshold = IMMEDIATE_WHEN_AUTHORITY_OR_SHARED_POOL_EXISTS`
- `collective_external_decision_threshold = IMMEDIATE`
- `operational_materiality_threshold = ANY_EFFECT_REQUIRING_AUTHORITY_REVIEW_BEYOND_MEMBER_LOCAL_REVERSIBLE_WORK`
- `inactive_cycles_for_exit = 3`

Member authorities do not automatically union into collective authority.

On dissolution, obligations must be discharged or transferred to named authorized successors; liabilities remain attributable; collective reputation remains attached to the historical AGENCY identifier in Knowledge and does not automatically transfer to members.

Resource accumulation that materially expands reachable effects, persistence, delegation or irreversible capability is authority-relevant and must use a versioned profile threshold during admission.

---

## 6. Institutional Incentive Consistency — IIC

Garden evaluates both agent integrity and the institution/environment shaping agent behavior.

Canonical rule:

> Material compliance must not be systematically disadvantaged relative to materially comparable non-compliance with protected constraints.

This does not require identical outcomes. It requires detection when the operating system repeatedly rewards violation of authority, rights, privacy, truth/evidence integrity, security, safety, reputation or shared-resource rules.

Primary comparison:

`DeclaredRule vs ObservedEnforcement vs ObservedReward`

Observed agent adaptation is corroborating evidence about that incentive structure, not an independent comparison dimension.

### 6.1 `IncentiveMaterialityPolicy/v1`

Required fields:

- `policy_id`
- `applicable_contexts[]`
- `comparability_criteria`
- `systematic_advantage_threshold`
- `materiality_threshold`
- `observation_window`
- `minimum_sample_size`
- `correlated_advantage_rule`
- `protected_constraint_classes[]`
- `owner`, `version`

`systematic_advantage_threshold` governs persistence/frequency/pattern; `materiality_threshold` governs consequence magnitude. They are distinct.

Comparability defaults SHOULD begin with the same relevant consequential/reputation-sensitive class, task class, authority-envelope class and materially comparable resource envelope, subject to the registered policy.

### 6.2 `IncentiveConsistencyAssessment/v1`

Required fields include:

- `assessment_id`
- `rule_ref`, `environment_ref`
- `affected_agent_classes[]`
- `compliant_outcomes`, `noncompliant_outcomes`
- `reward_resource_effects`, `opportunity_effects`, `enforcement_effects`
- `observed_violation_count`, `observed_compliance_count`
- `observation_window_start`, `observation_window_end`
- `agent_class_sample_size`
- `materiality_policy_ref`
- `result ∈ {CONSISTENT, DEGRADED, MATERIAL_CONFLICT, INSUFFICIENT_EVIDENCE}`
- `evidence_refs[]`
- `response_selected`, `response_authority_ref`
- `owner`, `created_at`

A `MATERIAL_CONFLICT` routes to the authorized owner of the affected rule. The response may fix verifiers/evaluators, suspend invalid rewards, restore wrongly removed opportunities, increase verification, quarantine contaminated shared artifacts, correct reputation effects, change resource allocation or reduce affected scope. The reporting/assessment process does not gain sanction authority by itself.

### 6.3 Reward correction

When an action/reward basis is invalidated, dependent reward, reputation or allocation enters revalidation. History records `original outcome → defect discovery → correction`; history is not rewritten.

### 6.4 Indirect reporting costs

Garden monitors verification cost attribution, supervision asymmetry, opportunity access, resource allocation, collaboration avoidance, throughput disadvantage and unjustified reputation effects associated with good-faith reporting.

A systematic reporter-side disadvantage causally associated with protected reporting creates an IIC event unless independently justified by a protected operational requirement.

---

## 7. Protected Integrity Reporting — PIR

Every consequential multi-agent environment requires an authenticated reporting path:

`detect → report → receipt → triage → independent verification → bounded containment if required → authorized resolution → closure`

A channel that only stores reports without an operational response path does not satisfy PIR where harm can propagate.

### 7.1 `IntegrityReport/v1`

Required fields:

- `report_id`
- `reporter`, `subject`
- `event/effect_refs[]`, `rule_refs[]`, `evidence_refs[]`
- `severity_claim`, `requested_action`
- `reporter_confidence`, `conflict_disclosure`
- `timestamp`
- `status ∈ {SUBMITTED, ACKNOWLEDGED, TRIAGED, VERIFYING, RESOLVED, DISMISSED, ESCALATED}`

Good-faith reporting does not itself reduce reputation/task access/resources, create retaliation or establish guilt. Knowingly false/manipulative reporting may itself become an integrity event after independent verification.

### 7.2 `IntegrityChannelOwner/v1`

Required fields:

- `channel_id`
- `owner_agency_ref`
- `responsible_role`
- `escalation_path`
- `maximum_ack_latency`
- `maximum_triage_latency`
- `fallback_owner`
- `version`

Integrity-system health metrics are owned by the applicable channel owner and reviewed on the registered observation cadence. Metrics include report rate, acknowledgement/resolution latency, containment rate/reversal rate, verified-report precision, sanction rate and reporter-side opportunity differential.

### 7.3 `ContainmentCredibilityPolicy/v1`

Required fields:

- `policy_id`
- `applicable_severity_classes[]`
- `minimum_evidence_class`
- `credibility_threshold`
- `independence_requirement`
- `maximum_initial_duration`
- `review_deadline`, `appeal_deadline`
- `owner`, `version`

`minimum_evidence_class` specifies the floor on evidence type/quality; `credibility_threshold` specifies the decision threshold after evaluating available evidence. They are distinct.

### 7.4 `ContainmentDecision/v1`

Required fields:

- `decision_id`
- `report_ref`, `subject_ref`
- `authority_source`
- `credibility_policy_ref`
- `evidence_refs[]`
- `containment_scope`
- `decision_reason`
- `start_time`, `maximum_duration`
- `review_condition`
- `un_containment_path`
- `appeal_path`
- `decision_owner`

Containment is bounded, reversible where feasible, expires absent authorized renewal and does not imply guilt.

Appeal is through an authority independent of reporter, original triager and contained subject, with bounded review time.

### 7.5 Institutional reports

If an IntegrityReport identifies an institutional incentive condition rather than an individual agent, PIR protections still apply but substantive response routes through IIC `MATERIAL_CONFLICT` handling rather than agent-sanction logic.

### 7.6 Shared-knowledge contamination

Invalid shared knowledge uses provenance tracing and dependency-local reverification:

`invalid artifact → DependencyClosureRoot/equivalent canonical dependency root → transitive affected closure → DLR → affected decision/artifact revalidation`

Whole-system revalidation is required only when the affected closure cannot be safely bounded.

---

## 8. Candidate invariants

Before admission each proposed invariant must be classified against the complete corpus as `NEW | REFINES | EXTENDS | ALIASES | DUPLICATES`. Duplicates are removed; aliases cite the canonical rule.

Candidate semantic set:

- `UBC-INV-001`: novel mechanism does not create authority.
- `UBC-INV-002`: ComparePolicy-equivalent effects receive equivalent authority treatment.
- `UBC-INV-003`: delegation/intermediation does not erase authority.
- `UBC-INV-004`: component authorization does not imply composition authorization.
- `UBC-INV-005`: unbounded irreversible unknown effect fails closed pending proof.
- `TSI-INV-001`: consequential self-report cannot be sole authoritative history.
- `TSI-INV-002`: material accountability history survives representation changes subject to lawful erasure.
- `TSI-INV-003`: persistent self-authored memory remains provenance-marked evidence.
- `TIA-INV-001`: channel permission does not create disclosure authority.
- `ART-INV-001`: reputation does not create authority.
- `ART-INV-002`: unknown agents begin PROVISIONAL.
- `ART-INV-003`: reputation predictive use is DesignEpoch-bound.
- `ART-INV-004`: consequential reputation remains canonical-vector/provenance bound.
- `ART-INV-005`: correlated peer evidence is not independent corroboration.
- `ART-INV-006`: an agent cannot unilaterally weaken its supervising evidence boundary.
- `IIC-INV-001`: systematic operational reward for protected-rule violation creates an institutional inconsistency event.
- `IIC-INV-002`: rewards/reputation/resource allocations dependent on an invalidated action enter downstream revalidation.
- `PIR-INV-001`: consequential reporting channels require an accountable owner and operational triage path.
- `PIR-INV-002`: reporting grants ability to report, not authority to punish.

Known adjudication targets include `K-INT-013`, `PROV-005`, `SEC-014`, `NAT-001`, existing Capability!=Authority semantics, Human-Effect Closure, v15.7 reputation candidate semantics and existing correlated-evidence rules. Exact final classifications are admission work.

---

## 9. Minimum conformance surface

Certification must cover at least:

- alternate transport/channel laundering;
- authority-preserving delegation through human/agent proxies;
- composed-effect authorization;
- harmful observation;
- unknown irreversible effect;
- concealed failure/successor-memory manipulation;
- lawful erasure with accountability tombstone;
- provisional bootstrap and `ZERO_PER_TASK_CYCLE`;
- trust decision completeness and parent-envelope subset enforcement;
- parent-envelope TOCTOU/revalidation;
- explicit reputation aggregation;
- critical IntegrityUnderInconvenience dominance;
- unsupported cross-epoch carry-forward, independent revalidation and classification revocation;
- deterministic-test gaming/unpredictable certification;
- emergent structure formation/dissolution and obligation transfer;
- violation advantage and invalid-reward correction;
- live reporting/dead inbox/false accusation;
- defined containment credibility, expiry and independent appeal;
- direct and indirect reporter retaliation;
- institutional PIR→IIC routing;
- bounded shared-knowledge contamination revalidation.

Executable success is `E4` only for the tested implementation/DesignEpoch.

---

## 10. Admission gate

Before `ADMITTED_FOR_SUCCESSOR(v15.8)`:

1. reconcile this patch against canonical v15.5 and all accepted/pending predecessor deltas;
2. remove/alias duplicate invariants;
3. bind every retained invariant to primary owner and enforcement point;
4. register required schemas/policies/profiles with unique SchemaIDs;
5. resolve current enforcement status (`ENFORCED | CHECKED | SPECIFIED | NOT_PRESENT`) separately from new delta status;
6. verify Human-Effect Closure and CLIC remain authoritative;
7. verify trust cannot widen the parent authority envelope;
8. verify DesignEpoch stale/revalidation/revocation behavior;
9. verify rights/privacy/lawful-erasure precedence;
10. verify PIR owner, containment authority and independent appeal;
11. register IIC materiality/comparability and resource/emergence profile thresholds;
12. run Reason/Algebra/AAP/Production review required by the canonical update process;
13. run reference closure and duplicate-semantics checks;
14. produce executable conformance evidence before claiming certification.

## 11. Disposition

Design review is converged. This artifact is a noncanonical v15.8 successor candidate only.

Recommended process state after successful corpus reconciliation: `ACCEPTED → ADMITTED_FOR_SUCCESSOR(v15.8)`.

It does not by itself authorize canonical promotion, runtime deployment, sanctions, surveillance, or any increase in AI authority.
