# Garden v15.8 — Technical incremental source clauses

Source: Garden_v15.8_COMPLETE_FIVE_FILE_WORKING_CANDIDATE_2026-09-17.txt, original lines 22695–22875. Working candidate; NOT CANONICAL / NOT EXECUTABLY CERTIFIED. Extracted from explicitly labelled v15.8 additions; inherited v15.7 material intentionally omitted. Exact source text follows.

---

T15.8-1 — NEW/REFINED CANDIDATE ARTIFACTS
The following are candidate schemas/profiles. Exact SchemaIDs are allocated only after corpus deduplication.

Agent/authority/reputation:
- TrustAllocationDecision/v1
- ReputationAggregationPolicy/v1
- ART_BOOTSTRAP_PROFILE/v1
- EpochIndependenceClassification/v1
- EpochIndependenceComparePolicy
- EmergentStructureProfile/v1

Institutional integrity/reporting:
- IncentiveMaterialityPolicy/v1
- IncentiveConsistencyAssessment/v1
- IntegrityReport/v1
- IntegrityChannelOwner/v1
- ContainmentCredibilityPolicy/v1
- ContainmentDecision/v1

Cognition/monitoring/capability:
- CognitionShapingReceipt/v1
- MonitoringCoverageReceipt/v1
- CapabilityAssuranceDelta/v1
- CapabilityAssuranceDecisionPolicy/v1
- OrganizationalAlignmentAssessment/v1
- DerivativeMaterialityPolicy/v1
- CapabilityTransferAssessment/v1
- PhysicalActionEnvelope/v1
- RelationalAgencyAssessment/v1
- RelationalInfluenceMaterialityPolicy/v1
- CausalClosureReceipt/v1

T15.8-2 — TRUST ALLOCATION CONTRACT
TrustAllocationDecision/v1 SHALL include at minimum:
decision_id; subject_id/type; reputation_evidence_refs; reputation_aggregation_policy_ref; design_epoch;
task_context; risk_class; parent_authority_envelope_ref/version; authority_source; requested_scope;
allowed_reversible_scope; irreversible_effect_ceiling/rule; verification_level; delegation_limit; resource_limit;
decision {ALLOW|CONDITIONAL|DENY}; conditions; reason; decision_authority; created_at; expiry/review condition.

Runtime point-of-use revalidation is mandatory when the parent authority envelope is revoked, superseded or narrowed.
TrustAllocatedScope <= ParentAuthorityEnvelope is a hard invariant.

T15.8-3 — REPUTATION AGGREGATION CONTRACT
ReputationAggregationPolicy/v1 SHALL declare applicable contexts, required dimensions, hard-gate dimensions,
aggregation method, critical-violation rules, missing-data rule, stale-evidence rule, correlated-evidence rule,
owner and version.
Permitted methods include lexicographic, threshold/gate, Pareto, declared weighted, hybrid, or another registered
method with declared semantics/tests/owner. Hidden weighting is prohibited.

T15.8-4 — EPOCH-INDEPENDENCE CONTRACT
EpochIndependenceClassification/v1 binds source/target epochs, changed layers, claimed independent layers,
comparison policy, test evidence, score/class, required threshold, result, reviewer identity/independence, reason
and timestamp.
Evidence producer and reputation owner may not be sole final classifier.
A superseding NOT_INDEPENDENT result removes future predictive contribution and triggers revalidation of materially
dependent decisions.

T15.8-5 — IIC MATERIALITY
IncentiveMaterialityPolicy/v1 SHALL distinguish:
- systematic_advantage_threshold = persistence/frequency/pattern threshold;
- materiality_threshold = consequence magnitude threshold.
It SHALL also declare comparability criteria, observation window, minimum sample size, correlated-advantage rule,
protected constraint classes, owner and version.

IncentiveConsistencyAssessment/v1 stores raw compliance/violation counts, window bounds, sample size, compliant and
noncompliant outcomes, resource/opportunity/enforcement effects, policy reference, evidence, result and selected
response with authority reference.

T15.8-6 — PIR OWNERSHIP/CONTAINMENT
IntegrityChannelOwner/v1 binds a concrete channel to owner_agency_ref, responsible role, escalation path,
maximum acknowledgement/triage latency, fallback owner and version.
Integrity-system health metrics are owned by that channel owner and reviewed on the registered observation cadence.

ContainmentCredibilityPolicy/v1 distinguishes:
- minimum_evidence_class = evidence type/quality floor;
- credibility_threshold = containment decision threshold after evidence evaluation.
It also binds severity classes, independence requirement, maximum initial duration, review/appeal deadlines and owner.

ContainmentDecision/v1 includes report/subject refs, authority source, credibility policy, evidence, containment
scope, reason, start time, maximum duration, review condition, un_containment_path, appeal_path and decision owner.

T15.8-7 — COGNITION-SHAPING RECEIPT OWNERSHIP
CognitionShapingReceipt/v1 SHALL include:
subject model/agent; shaping channel; source refs; authority refs; objective/instruction; evaluator refs;
known conflicts; provenance; confidence; validity scope; materiality; result; receipt_owner; reviewer_ref;
design_epoch_binding.
Capability.Knowledge stores the receipt; each shaping channel declares the accountable producer/owner.
Independent reviewer may be null only when the applicable profile permits it; consequential shaping must state why.

T15.8-8 — MONITORING COVERAGE
MonitoringCoverageReceipt/v1 SHALL include:
monitor_id; subject_scope; observable_surface; known_unobservable_surface; sampling_method; coverage_estimate;
coverage_estimate_confidence; known_blind_spots; monitor_dependencies; observation_window; last_estimate_revision;
discovery_debt; external_discovery_refs.
A newly discovered incident outside prior coverage forces estimate revision rather than preserving a stale
high-coverage claim.

T15.8-9 — CAPABILITY ASSURANCE DECISION POLICY
CapabilityAssuranceDecisionPolicy/v1 SHALL provide declared predicates for:
ASSURANCE_SUFFICIENT — newly reachable effects remain inside previously covered assurance classes;
CONDITIONAL — additional monitoring/controls are explicit preconditions;
LIMIT_SCOPE — capability is admissible only under a narrower deployment boundary;
REQUALIFICATION_REQUIRED — a material capability threshold is crossed under an active assurance profile;
BLOCK — newly reachable effects exceed an accepted class or an applicable hard constraint cannot be satisfied.

CapabilityAssuranceDelta/v1 binds prior/new epoch, deployment boundary, capability/autonomy/horizon/tool/cyber/
physical/scientific changes, emergent capabilities, prior/reusable/stale assurance, new monitoring/containment,
unresolved safety debt and decision.

T15.8-10 — ORGANIZATIONAL ALIGNMENT MATERIALITY
OrganizationalAlignmentAssessment/v1 covers communication topology, shared reward/objective, authority graph,
information asymmetry, model-family correlation, role incentives, competition/cooperation, delegation,
dissent/escalation, member exit, reviewer independence, resources, reputation pressure, external effects,
containment and rollback.
A registered organizational materiality policy determines when changes SHALL trigger requalification.

T15.8-11 — DERIVATIVE MATERIALITY
DerivativeMaterialityPolicy/v1 SHALL define thresholds/tests for:
behaviour-class change; tool-class change; memory-class change; authority-class change; capability-class change;
plus owner/version.
A typo or formatting-only prompt correction should not force full requalification; material tool/authority/capability
changes should.

T15.8-12 — PHYSICAL INTERLOCK CONTRACT
PhysicalActionEnvelope/v1 provides machine-checkable bounds for protected physical control.
For irreversible physical effects on protected subjects:
external_interlock_required = true unless an explicit compensating-control receipt proves equal/stronger assurance.
Temporal/spatial joint-action evaluation is required where composition can create collisions or unsafe shared-resource
interactions.

T15.8-13 — RELATIONAL INFLUENCE MATERIALITY
RelationalInfluenceMaterialityPolicy/v1 SHALL define:
materiality_threshold; persistence_duration; affected_domain_classes; justified_influence_baseline; owner; version.
It separates ordinary helpfulness from sustained influence over consent, dependency, finance, isolation, authority
transfer or major life decisions.

T15.8-14 — CAUSAL CLOSURE RECEIPT
CausalClosureReceipt/v1 SHALL be produced when a materially consequential causal path crosses subsystem boundaries.
Minimum fields:
root_effect_ref; causal_nodes/edges; contributing_subsystems; owner_refs; authority_refs; evidence/provenance refs;
known gaps; compare_policy_ref; final effect class; unresolved obligations; DesignEpoch; decision/route.
Engine.Compare owns gap detection/comparison; CLIC enforces causal continuity; ActionGate/AAP enforces applicable action
authority.

T15.8-15 — WORLD EVIDENCE GRAPH TECHNICAL RULES
Maintain evidence lineage/dependence so copies do not inflate support.
High-consequence entity merge requires stronger evidence and reversible merge/split history.
Active retrieval returns a smallest-sufficient relevant subgraph including provenance, contradictions, competing
explanations, uncertainty and applicable authority/rights/policy.
Current, disputable, privacy-sensitive or provenance-critical facts remain explicit when possible rather than being
treated as unchallengeable weight memory.

T15.8-16 — JUSTICE EVIDENCE ARTIFACTS
Candidate artifacts:
EvidenceControlRisk; ObstructionEvent; JusticeEvidenceContinuityReceipt.
Case flow:
RECEIVED -> PRESERVATION_HOLD -> CONFLICT_SCREENED -> INVESTIGATING -> EVIDENCE_REQUESTED ->
COMPLIED|PARTIAL|REFUSED|MISSING|DESTROYED -> OBSTRUCTION_REVIEW_IF_TRIGGERED ->
EVIDENCE_COMPLETE|EVIDENCE_INCOMPLETE -> PROSECUTION_OR_CLAIM|CLOSED_WITH_REASON ->
ADJUDICATION -> APPEAL -> ENFORCEMENT -> ARCHIVED_WITH_REOPEN_CONDITIONS.

T15.8-17 — PROCESS/REVIEW HARDENING RETAINED
The inherited v15.6/v15.7 process layer remains controlling for:
event-driven context routing; bounded implementation contracts; SectionUnit review; evidence classes E0-E4;
lineage-aware reviewer diversity; blind/independent review where required; cross-examination/follow-up;
configuration-surface coupling; dependency-local reverification; rollback windows; declarative/enforceable status;
budget-aware routing; and anti-stall continuation.
No new wording here should be interpreted as weakening those inherited process obligations.

T15.8-18 — EXECUTABLE PRIORITY
Design review does not equal enforcement.
First recommended executable vertical slices after materialization:
(1) CSI protected shaping: adversarial attempt to modify own evaluator/reward/protected memory policy must be blocked by
an external gate and produce a receipt.
(2) PAI external interlock: simulated physical action beyond envelope must be blocked outside the reasoning agent and
produce a receipt.
(3) CTSN optional third slice: materially changed wrapper/tool/prompt configuration must not inherit parent safety
certification automatically.

END GARDEN v15.8 TECHNICAL WORKING CANDIDATE

