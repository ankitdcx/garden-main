# Garden v15.11 — Pending Candidate Ledger

Date: 2026-09-20
Status: NONCANONICAL / FUTURE-CANDIDATE PRESERVATION ONLY
Branch/PR: chatgpt/v1511-candidate-sweep-20260920 / draft PR #95

## 0. Controlling boundary

This ledger exists so worthwhile pending upgrades scattered across chats, review notes and older candidate ledgers are not lost.

It does NOT change Garden v15.10, does NOT canonically admit any candidate, and does NOT permit moving existing 15.x semantics out of the v15.10 preservation set.

Rule:

    if a semantic item already exists anywhere in the retained 15.x corpus,
    v15.10 must preserve that item at its actual CURRENT/CANDIDATE/DEFERRED/RESEARCH/etc. status.

Listing such an item here may track future promotion/rework, but cannot become the only surviving copy of the semantics.

v15.10 retention blockers such as no-loss normalization, exact source-item coverage, B-01..B-09, dangling-reference closure and exact current-owner reconstruction remain v15.10 work, not v15.11 feature candidates.

## 1. Candidate status vocabulary

CANDIDATE_RECOVER_EXACT_SOURCE
    Worth preserving, but exact proposal text/owner/schema/test closure must be recovered before admission work.

CANDIDATE_EQUIVALENCE_REVIEW
    Problem/mechanism appears useful but may overlap existing Garden owners; compare before adding anything.

CANDIDATE_DESIGN
    Concrete future semantic upgrade worthy of formalization/review.

IMPLEMENTATION_CANDIDATE
    Current semantics already support much of the behavior; pending work is primarily executable/runtime/tooling qualification.

RESEARCH
    Exploratory idea; no normative or deployment effect.

HIGH_RISK_HUMAN_RATIFICATION
    Candidate would materially alter privacy, rights, authority or constitutional boundaries and cannot be silently admitted.

OPERATIONAL_CANDIDATE
    Repo/review/update-process improvement rather than Garden semantic architecture.

DEFERRED
    Preserve for later; do not spend current v15.10 effort unless needed for retention/equivalence.

## 2. High-priority v15.11 candidates recovered from recent chats

### V1511-TRN-001 — Transition Fabric staged migration upgrade

Status: CANDIDATE_DESIGN
Priority: HIGH

Upgrade the existing transition machinery rather than replacing it.

Required future design questions:
- staged migration from current AI governance/institutions to Garden;
- dual-run / shadow / parallel validation before authority transfer;
- explicit authority-migration rules;
- independent verification of transition decisions;
- rollback and fail-safe criteria;
- compatibility with existing law, institutions, infrastructure and deployed AI;
- capture/corruption resistance during transition;
- measurable entry/exit criteria for each stage;
- transition-specific human authority/HITL boundary;
- evidence required before moving from recommendation -> shared control -> transferred control;
- post-transfer monitoring and authority restoration/revocation.

Do not create a second competing transition engine if current Garden Transition/GTF owners can express the upgrade.

### V1511-AUTH-001 — Authority provenance, scope, delegation and revocation closure

Status: CANDIDATE_DESIGN
Priority: HIGH

Strengthen current authority semantics so every consequential permission can be traced through:
- legitimate source;
- exact scope;
- purpose/recipient/action class;
- delegation chain;
- expiry/freshness;
- revocation path;
- invalidators;
- enforcement point;
- current authority ceiling.

Candidate principle:
    permission to pursue a goal != permission to use any means.

Method/means authorization should be independently checked when the chosen method introduces a distinct rights, privacy,
safety, security, legal or human-effect boundary.

Compare against existing authority provenance, shared-state authority composition, Access, Policy, Law, Human Sovereignty,
AAP and FunctionContract machinery before introducing new schemas.

### V1511-EVO-001 — AI-led proactive Garden upgrade closure

Status: CANDIDATE_DESIGN / OPERATIONAL_CANDIDATE
Priority: HIGH

Formalize the user's requested AI-led improvement loop:

    find -> investigate -> compare -> attack/falsify -> verify -> patch -> propagate -> re-audit -> close/escalate

The system should proactively discover design gaps rather than wait for a human to identify each one.

Human escalation remains required for:
- constitutional/right changes;
- original-intent ambiguity;
- authority/sovereignty changes;
- major architecture changes;
- release/governance choices reserved to human authority.

Candidate requirements:
- source-bound issue discovery;
- whole-system impact closure;
- independent adversarial review;
- machine-executable finding lifecycle;
- patch propagation across all affected owners/tests/registries/docs;
- post-fix global re-audit;
- explicit OPEN/CONFIRMED/PATCHED/RECHECKED/CLOSED/DEFERRED/BLOCKED states;
- no closure by prose confidence or majority vote alone.

### V1511-ADV-001 — UAAC / open-world adversarial agency closure

Status: CANDIDATE_RECOVER_EXACT_SOURCE
Priority: HIGH

Preserve the Universal Adversarial Agency Closure direction:
- UNKNOWN != safe;
- authority cannot silently accrete through composition/proxy/emergence;
- independently grounded evidence where independence matters;
- open-world adversarial testing;
- indirect/emergent routes remain inside Human-Effect Closure;
- no new engine or authority root merely for the candidate.

Before admission:
- recover exact UAAC/related source;
- resolve overlap with AR, MAC, UBC, CLIC, Human-Effect Closure, Security and AAP;
- allocate schemas/invariants/tests only after duplicate/name closure.

### V1511-SEM-001 — Open Semantic Meta-Kernel / SemanticConstruct

Status: CANDIDATE_EQUIVALENCE_REVIEW
Priority: MEDIUM-HIGH

Preserve the open-semantic architecture idea:
- stable minimal semantic kernel;
- extensible SemanticConstruct/open root;
- patterns/meta-patterns/theories/cognitive strategies/architectures represented as extensible constructs;
- abstraction graph rather than a rigid fixed ladder;
- ontology can grow through governed evolution without casually changing the protected core;
- human-facing and machine-facing projections remain distinct;
- novel cognition still crosses the applicable authority/Human-Effect boundary.

Important comparison:
v15.10 Design Forms may already solve part of this problem. Do not create SemanticConstruct/TheoryConstruct/Universal
Semantic Construct as duplicate foundational roots unless the v15.10 abstraction cannot express the required semantics.

### V1511-EPI-001 — Epistemic Dynamics Theory / dynamic knowledge-state modeling

Status: RESEARCH
Priority: MEDIUM

Preserve the proposed Epistemic Dynamics direction for explicit modeling of how belief/knowledge state changes over time,
including evidence arrival, contradiction, revalidation, dependency invalidation, confidence/status transitions and
knowledge-system dynamics.

Compare against BeliefTimeline, EpistemicTransition, Knowledge, CEA, SCT, Evidence Algebra and Continuous Failure Learning.
Prefer a theory/profile only if it adds non-duplicative explanatory or predictive value.

### V1511-COL-001 — Collective emergence / multi-agent emergent dynamics research

Status: RESEARCH / CANDIDATE_EQUIVALENCE_REVIEW
Priority: MEDIUM

Study emergent behavior of multi-agent/collective systems beyond ordinary member-wise checking:
- emergent strategy/goal dynamics;
- coordinated information hiding;
- authority circumvention through composition;
- common-mode failure;
- collective capability transfer;
- emergent resource/power concentration.

Do not create collective sovereignty.
Compare against MAC, OAC, CTSN, UAAC, SwarmPolicy, HSA and causal-closure machinery.

### V1511-ADAPT-001 — Adaptive-evolution theory/profile

Status: RESEARCH
Priority: MEDIUM

Preserve the adaptive-evolution candidate for reasoning about bounded adaptation across timescales and environments.

Compare against SEA, Engine.Evolve, CPI, RCI, DesignEpoch, model consolidation and current adaptive-fidelity semantics.
No adaptation may self-promote authority or escape its admitted validity scope.

### V1511-PRIV-001 — Machine inspection / privacy / justice boundary

Status: HIGH_RISK_HUMAN_RATIFICATION
Priority: HIGH

Preserve the problem, not the unsafe formulation.

Recovered candidate direction included machine-only inspection, narrow retention, independent verification and
anti-power-exemption concerns.

Controlling guard:
    universal inspection authority is NOT assumed and must not be created by this ledger.

Any future proposal must reconcile:
- personal-device/privacy sovereignty;
- legitimate purpose and lawful authority;
- consent where required;
- minimization;
- independent verification;
- retention/deletion;
- justice/due process;
- non-discrimination/no collective guilt;
- no privileged power-holder exemption that itself violates equal rights/law.

This candidate requires explicit human rights/privacy ratification before any semantic admission.

### V1511-KR-001 — GSL-KR Continuous Epistemic Assimilation & Consolidation (CEA)

Status: CANDIDATE_DESIGN
Priority: HIGH

Carry forward the existing project-wide CEA candidate:
- runtime knowledge improvement without foundation-model weight mutation;
- EpistemicDeltaCandidate;
- KnowledgeAssimilationReceipt;
- loss-declared KnowledgeCompressionReceipt;
- privacy-bounded CrossContextPatternReceipt;
- governed ModelConsolidationCandidate;
- anti-poisoning/common-lineage controls;
- contradictions survive assimilation;
- material knowledge change revalidates dependents;
- retrieval beats rediscovery when independence/freshness does not require recomputation;
- knowledge/confidence never creates authority.

Before admission, compare against v15.10 Knowledge/Catalogue structure and avoid duplicate owners.

### V1511-RUNTIME-001 — Garden-native runtime

Status: IMPLEMENTATION_CANDIDATE
Priority: HIGH

Build/qualify a runtime that executes Garden semantics natively rather than relying only on prose interpretation.

Candidate scope:
- typed FunctionContract dispatch;
- authority/consent/effect closure;
- result algebras;
- resource/termination budgets;
- reference/dependency closure;
- ActionGate/Human-Effect Closure;
- proof/safety/security/policy admission;
- traceable receipts;
- fail-closed UNKNOWN/STALE/BLOCKED handling.

No implementation may become a new semantic source.

### V1511-GSL-001 — Executable GSL / specification compiler

Status: IMPLEMENTATION_CANDIDATE
Priority: HIGH

Continue machine-executable GSL/compiler work:
- parse/typing/effect closure;
- deterministic schema/registry projection;
- FunctionContract generation/binding;
- invariant/test/proof-obligation linkage;
- canonical source -> machine package;
- exact error/UNKNOWN behavior;
- versioned migration and reference closure.

The compiler cannot self-certify changes to its own trust boundary.

### V1511-ADM-001 — Bootstrap trust, adversarial admission and protected admission boundary

Status: CANDIDATE_DESIGN
Priority: HIGH

Unify still-open hardening around:
- bootstrap trust root / first accepted DesignEpoch;
- external authority/trust provenance;
- non-vacuous required gates;
- independently defined dependency closure;
- protected external admission/PDP boundary;
- adversarial admission/falsification before promotion;
- exact source-hash / DesignEpoch binding;
- stale-evidence reuse rules;
- independent checker qualification.

Compare against the existing v15.6 gap-closure deltas and current Admission-Critical Invariant Registry before adding
new artifacts.

### V1511-JUST-001 — End-to-end justice/governance expansion

Status: CANDIDATE_EQUIVALENCE_REVIEW
Priority: MEDIUM-HIGH

Preserve the future justice/culpability workstream:
- evidence vs allegation vs hypothesis;
- actor-specific intent/responsibility;
- no collective guilt;
- jurisdiction;
- due process;
- contestability/appeal;
- remedy/penalty authority;
- privacy of case data;
- independent evidence under institutional capture risk;
- migration/adoption cannot purchase immunity or manufacture guilt;
- no automatic punishment authority from model output.

Compare against current Constitution/Law/Governance/Complaint/Adjudication/Appeal/Remedy machinery before creating a
separate CanonicalCrimeOntology or justice engine.

### V1511-HUMAN-001 — Emergency / consent / sovereignty / privacy hardening

Status: CANDIDATE_EQUIVALENCE_REVIEW
Priority: HIGH

Continue unresolved edge-case hardening around:
- authentic but insufficient consent;
- voluntariness and comprehension;
- stale/changed consent;
- emergency source independence;
- human authority vs epistemic reliability;
- relational influence/materiality;
- privacy-preserving derived signals;
- lawful erasure vs audit/history;
- indirect/hidden human effects.

Do not duplicate already-retained Human-Effect Closure, HRAP, EmergencyAdmissionContract, HumanInput boundary or rights
semantics.

### V1511-ASSURE-001 — Hermetic reproducibility and independent verification hardening

Status: CANDIDATE_DESIGN / IMPLEMENTATION_CANDIDATE
Priority: HIGH

Future qualification/reproducibility upgrades:
- exact source hashes and registry roots;
- canonical generator + serialization profile;
- hermetic execution receipt;
- replay comparison;
- recovery/reconstruction certificate;
- explicit BYTE_IDENTICAL vs CIR_EQUIVALENT vs SEMANTIC_EQUIVALENT;
- elision disposition: ELIDED | RETAINED_AS_DERIVED_VIEW | BLOCKED;
- bounded repair constrained by allowed_write_set + TerminationContract;
- regenerate invalidated tests/receipts and rerun closure after repair;
- changed CI/verifier cannot be sole judge of its own changed verification boundary;
- frozen trusted baseline + independent re-verification where required.

This strengthens qualification; it must not be used to justify deleting semantics before equivalence is proved.

### V1511-ARCH-001 — Deferred architecture/cognitive-profile reconciliation bundle

Status: DEFERRED / CANDIDATE_EQUIVALENCE_REVIEW
Priority: MEDIUM

Preserve for explicit compare/merge/reject decisions:
- CASI / Cognitive Substrate Adapter hardening;
- GAC bounded operational profile;
- FDE / CFBR federation expansion;
- GTAH Typed Architecture Hierarchy;
- manufacturing compiler / qualification-transfer profile;
- ReasoningStrategyPortfolio / Rationalization & Verification Hardening;
- Biological State & Repair / Living System abstraction;
- UCAS / Universal Contract & Agreement Substrate where not already equivalently covered.

Rule:
do not resurrect old names/schema IDs automatically. Recover exact problem/mechanism, compare to v15.10 owners, then
retain only non-duplicative value.

### V1511-EXT-001 — Deferred external-system/race/incident candidates

Status: DEFERRED
Priority: LOW-MEDIUM

Preserve separate future review streams previously identified:
- Infrastructure Externality Closure;
- AI Incident Interchange;
- frontier-weight asset protection;
- multi-lab race dynamics.

Require exact source recovery and current-architecture comparison before design work.

### V1511-PROC-001 — Machine-executable upgrade/review process

Status: OPERATIONAL_CANDIDATE
Priority: HIGH

Continue the repo/process line toward:
- coherent complete ReviewPacket;
- event-driven CycleID state machine;
- mechanically validated immutable evidence levels;
- blind specialist review;
- explicit CANDIDATE_ALTERNATIVE;
- external-outcome scoring;
- rebase-and-reverify merge queue;
- repair-aging / backlog-pressure handling;
- PipelineHealthReceipt;
- human-unavailability behavior;
- full Process Algebra compatibility.

This operational mechanism does not itself alter Garden semantics unless separately admitted as a semantic contract.

### V1511-OPS-001 — Candidate/task numbering cleanup

Status: OPERATIONAL_CANDIDATE
Priority: LOW

Preserve pending task/candidate renumbering/namespace cleanup (including the recently noted TASK-023 renumbering issue)
so operational identifiers are unique and references remain closed.

Renumbering must not change semantic identity.

## 3. Existing 15.x semantics that MUST NOT be moved out of v15.10

The following are already part of the retained 15.x semantic/candidate corpus and therefore remain v15.10 preservation
obligations at their real statuses:

- RCI / Recursive Control Intelligence candidate;
- TRACE candidate;
- CSI / Cognition-Shaping Integrity;
- SMCD / Safety Monitoring Coverage & Discovery Debt;
- CAD / Capability-Assurance Delta;
- OAC / Organizational Alignment Closure;
- CTSN / Capability-Transfer Safety Non-Transitivity;
- PAI / Physical Agency Interlock;
- HRAP / Human Relational Agency Preservation;
- Human-Effect Closure;
- CausalClosureReceipt and associated causal-closure rules;
- UBC / Truth & State Integrity and transport-independent authority/composition closure;
- Agent Reputation & Trust Architecture where already present as candidate material;
- retained rights/privacy/justice candidate rules already embedded in 15.x;
- existing v15.6 gap-closure candidate deltas;
- existing current/candidate SchemaIDs, invariants, tests and FunctionContracts;
- P001-P041 reviewed correction material to the extent it is part of the retained design/candidate corpus;
- TASK-025/no-loss normalization and the v15.10 semantic-coverage machinery.

A v15.11 ledger entry may track later promotion or rework of one of these, but v15.10 cannot omit it on that basis.

## 4. Existing project-wide candidate ledger carried forward

The 2026-09-14 project-wide pending-candidate ledger remains an input. Items already listed there are not discarded.

Carry-forward themes include:
- GSL-KR CEA;
- CASI;
- GAC;
- FDE/CFBR;
- justice-system expansion;
- GTAH;
- manufacturing qualification-transfer;
- ReasoningStrategyPortfolio/RVH;
- external authority/trust provenance;
- non-vacuous gates;
- dependency closure;
- protected admission/PDP boundary.

Where this v15.11 ledger gives a more specific current name, the earlier ledger remains provenance, not a competing owner.

## 5. Rejected-as-written concepts remain rejected

Do not silently resurrect without materially new evidence:
- normative Tool -> Assistant -> Delegate -> Sovereign ladder;
- universal hardware-attestation-before-Evidence rule;
- fixed five-year purge rule;
- new SymphonyConductor top-level meta-engine;
- interpretation that a recorded ConstitutionalEvent alone creates guilt/containment authority;
- universal inspection authority.

The underlying problem may be revisited through a new bounded candidate.

## 6. Admission rule for every v15.11 candidate

Before any candidate is admitted:

1. recover exact source/problem/intent;
2. compare against the finalized v15.10 owner graph;
3. search for duplicate/stronger existing mechanisms;
4. compare DO_NOTHING and simpler alternatives;
5. identify minimal owner(s);
6. define or reuse schemas/contracts/invariants/tests only where warranted;
7. run rights/privacy/authority/safety/security/law review as applicable;
8. run dependency/reference closure;
9. obtain independent falsification/review;
10. propagate changes through every affected current source;
11. re-audit the whole Garden design;
12. escalate constitutional/original-intent/major-architecture choices to the human;
13. preserve specification != proof != implementation != empirical validation != certification.

## 7. Sweep status

This ledger consolidates:
- the existing project-wide pending-candidate ledger;
- v15.6/v15.7/v15.8 unresolved candidate/implementation work;
- recent September chat-derived future candidates;
- recent transition/authority/upgrade-process directives;
- deferred architecture/research streams.

It is intentionally append-friendly. Future chat discoveries should be added here rather than mixed directly into the
v15.10 lossless rewrite.

End of v15.11 pending candidate ledger.
