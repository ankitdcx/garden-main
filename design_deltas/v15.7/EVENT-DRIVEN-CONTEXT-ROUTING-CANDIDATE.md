# Garden v15.7 candidate — Event-Driven Context Routing

Status: NON_CANONICAL_CANDIDATE / PROPOSAL_ONLY / NO_AUTHORITY / NO_PROMOTION
Date: 2026-09-16
Candidate ID: CAND-EDCR-001
Work package: WP-EVENT-DRIVEN-CONTEXT-ROUTING-V15-7
Amendment: `EVENT-DRIVEN-CONTEXT-ROUTING-CORRECTION-2026-09-16.md`

**Current interpretation:** event/delta/context semantics in this file remain active, but any earlier reading that routed an Astra frontier reviewer through OpenRouter is superseded. The frontier role is the external ChatGPT lane; the repository does not hardcode a changing ChatGPT product model name. OpenRouter remains a separate worker/reviewer provider surface.

## 1. Purpose

Strengthen existing Garden execution, cognition and knowledge contracts so recurring agent work is triggered by meaningful state change and consumes compact, provenance-preserving context deltas instead of repeatedly rebuilding large unstructured prompts.

This is an additive binding across existing owners. It does **not** create a new top-level engine, authority source, truth source or autonomous actor.

Primary existing owners:
- GardenProcess / completion-driven execution for work selection and sequencing.
- GSL-KR for governed reusable knowledge, conflict handling, retention and query.
- ObservationRecord / AttestedObservation for observation semantics.
- Evidence, Proof, Compare, Reason, DesignEpoch and Audit for epistemic and change-control boundaries.
- ActionGate / AAP / authority contracts for effects.

## 2. Problem being solved

Repeatedly sending unchanged or weakly relevant source material to many models wastes compute and can lower review quality by mixing signal with stale or duplicated context. Pure model-routing does not solve this when every call still rebuilds the same context.

The candidate therefore optimizes **information movement before model choice**:

`external/repository event -> cheap bounded normalization -> governed observation ledger -> relevance/materiality gate -> compact context delta -> specialist review -> external ChatGPT frontier synthesis only when warranted -> reusable snapshot`

No event, observation, summary, reviewer agreement or frontier-model output becomes truth, proof, authority or canonical Garden semantics merely by entering this pipeline.

## 3. Normalized observation contract

A worker may emit a `NormalizedContextObservation` only with at least:
- observation_id and idempotency/fingerprint key;
- event/valid/observation times where applicable;
- subject and event kind;
- changed fields or claimed delta;
- exact source/evidence references and source hashes when available;
- provenance / producing lane / model identity where model-produced;
- declared risk and uncertainty;
- contradiction or supersession links when known;
- freshness/expiry or revalidation condition;
- public/private classification and permitted processing envelope;
- parent observation IDs / evidence ancestry;
- a bounded summary that cannot replace the cited underlying evidence.

Duplicate fingerprints are not re-expanded into new context unless a material binding (source, time, state, evidence or interpretation) changed.

## 4. Context ledger and snapshot semantics

The context layer is an indexed view over governed records, not a second truth store.

1. Raw evidence and required immutable observations remain retained according to their owning retention contract.
2. Context snapshots are derived, versioned and hash-bound to their source observations.
3. A snapshot MUST preserve source back-pointers and evidence ancestry.
4. Compression MUST declare what was omitted, the compression policy and any loss bound that can be stated honestly.
5. A compressed snapshot MUST NOT erase a contradictory observation merely because it is inconvenient or lower-confidence.
6. A summary can expire independently of its source evidence.
7. New evidence that invalidates a snapshot creates a successor; it does not rewrite historical state.

## 5. Relevance and materiality gate

Cheap/free deterministic or low-cost workers should perform classification, extraction, normalization, deduplication and bounded routing before expensive reasoning.

A frontier review is eligible only when a `MaterialContextChange` is supported by one or more explicit triggers, such as:
- HIGH/CRITICAL risk;
- contradiction between currently relevant observations;
- a semantic-design delta or changed governing assumption;
- authority, rights, ActionGate, privacy or security boundary change;
- failed verification / regression / invariant or proof-obligation change;
- newly available evidence that can overturn a prior conclusion;
- unresolved uncertainty above the profile threshold;
- dependency change that invalidates a previously reusable result;
- maximum snapshot staleness reached for a still-active high-value question.

Mere clock passage, unchanged repository state, repeated identical news/input, reviewer count or token availability is not by itself a material event.

The gate produces a reason-coded receipt. `NOT_MATERIAL` means no frontier handoff is made; it does not mean the underlying event was false or unimportant in every other context.

## 6. Frontier ChatGPT profile

When materiality is established, one external ChatGPT frontier reviewer may receive the **smallest sufficient context packet** rather than the whole corpus by default.

The packet includes:
- question/decision scope;
- current snapshot hash;
- only the new/changed observations required for the question;
- contradictory/counterevidence observations;
- source/evidence back-pointers;
- prior conclusion only when needed to test whether it should change;
- explicit unknowns and omitted-context declaration.

Garden represents this as `GardenFrontierReviewRequest/v1` targeting `EXTERNAL_CHATGPT_FRONTIER_REVIEW`. The concrete ChatGPT model is selected by the user/product context and is not a repository constant. If the user explicitly selects Astra in ChatGPT, Astra may fill the role; otherwise another current ChatGPT model may fill it. Garden therefore MUST NOT configure `openai/...astra` as an OpenRouter surrogate for this lane.

OpenRouter cheap/free/paid families may perform normalization and bounded independent review, and may help produce the compact request. Their role ends at the OpenRouter provider boundary. ChatGPT frontier review remains separately attributable proposal evidence and cannot replace independent-family requirements, whole-source cross-reference, Proof/Evidence obligations, protected human authority, merge gates or canonical promotion.

## 7. Staleness and contamination controls

The context layer MUST fail closed against silent contamination:
- observations carry freshness and provenance;
- low-trust or model-generated observations are never silently promoted to facts;
- contradictions remain explicit until resolved under an owning epistemic rule;
- downstream summaries preserve ancestry to the observations they relied on;
- an overturned observation triggers dependency-aware revalidation of affected snapshots/findings;
- UNKNOWN and INCONCLUSIVE remain representable outcomes;
- stale context is excluded from present-tense claims unless explicitly used as historical evidence.

## 8. Compute and cost accounting

Efficiency claims are measured, not assumed. Each governed review cycle should record, where available:
- raw event count;
- normalized/deduplicated observation count;
- context characters/tokens before and after compaction;
- model/reviewer calls or handoffs avoided by `NOT_MATERIAL`;
- frontier handoffs made and why;
- input/output tokens and monetary cost where a provider exposes them;
- cache/batch use where applicable to provider lanes;
- full-context fallback count/reason;
- quality/regression outcomes against the prior routing policy.

The optimization objective is not minimum spend alone. It is lower repeated compute **without weakening evidence, independence, freshness, falsification, authority or safety requirements**.

## 9. Repo-wide applicability

The same pattern applies to post-merge verification, canonical design review, public research intake, ReviewPacket construction, blind review, cross-examination, branch/PR hygiene, implementation/integration, pipeline health, repo reconciliation, protocol/pipeline simplification, successor composition and knowledge refresh. The executable applicability profile is `governance/EVENT_DRIVEN_WORK_POLICY_v1.json`.

Delta-first processing is only the default. Wider/full context is mandatory when dependency closure is unknown/incomplete, DesignEpoch or source root changed, HIGH/CRITICAL semantics cross owners/files, affected contracts/invariants cannot be bounded, whole-source Compare/Proof/Evidence/Tier-A closure is required, an assurance/audit obligation explicitly requires full revalidation, or contradiction/contamination cannot be resolved from the compact packet.

## 10. Required invariants

EDCR-001: No materiality receipt -> no frontier-review handoff.

EDCR-002: A context snapshot cannot become authority, truth, Proof or canonical status by compression or model agreement.

EDCR-003: Every model-derived claim in a snapshot retains model/provenance ancestry and underlying evidence references.

EDCR-004: Raw/required evidence retention is controlled by the evidence/knowledge owner; snapshot compression cannot delete it.

EDCR-005: Contradictory relevant observations cannot be silently discarded by summarization.

EDCR-006: Expired/stale observations cannot support current claims without explicit revalidation or historical qualification.

EDCR-007: Duplicate event fingerprints do not trigger repeated frontier handoffs unless a material binding changed.

EDCR-008: Frontier review does not satisfy independent-family quorum by itself and never self-admits a semantic delta.

EDCR-009: Budget exhaustion, provider ambiguity or unknown charge state in provider lanes fails closed and preserves retry/reconciliation semantics.

EDCR-010: Materiality thresholds and compression policy are versioned profile inputs, not hidden prompt conventions.

EDCR-011: OpenRouter cannot stand in for the external ChatGPT frontier lane.

EDCR-012: Garden does not hardcode a changing ChatGPT product model name as a semantic architecture dependency.

EDCR-013: Due intervals are freshness constraints and do not authorize polling unchanged state.

EDCR-014: Delta-first processing cannot weaken whole-source closure, Tier-A, Challenger, Proof, Evidence or protected-authority requirements.

EDCR-015: Reusable context is invalidated by affected dependency change, source-root/DesignEpoch change, expiry or overturning evidence and must then be selectively or fully revalidated according to closure.

## 11. Minimum conformance tests

1. Replaying an identical observation produces no new frontier handoff.
2. A changed source hash with identical prose remains distinguishable and is re-evaluated under policy.
3. A HIGH-risk contradiction produces a materiality receipt and includes both sides in the frontier packet.
4. An all-NO_CHANGE, unchanged, fresh snapshot produces `NOT_MATERIAL` and zero frontier handoff.
5. Expired evidence cannot silently survive into a present-tense snapshot.
6. Compression preserves evidence references and records omitted-context policy.
7. A frontier output that claims authority/canonical admission is rejected or stored only as proposal evidence.
8. Provider 429/unknown charge never advances governed process state.
9. OpenRouter policy contains no Astra-as-frontier model binding.
10. ChatGPT handoff request contains no provider credential or provider-side model route.
11. A forced incomplete dependency closure expands context or blocks rather than silently compressing.
12. Quality comparison measures whether compaction changed conclusions, false-negative rate, contradiction detection or required evidence coverage.

## 12. Candidate disposition

This candidate is worthy because it strengthens mechanisms Garden already contains: completion-driven execution, observation/evidence separation, reusable governed knowledge, truth maintenance, freshness and dependency-aware revalidation. It should be applied incrementally across the repository where repeated unchanged processing exists, measured there, and only then considered for canonical admission.

Canonical promotion remains a separate governed act.
