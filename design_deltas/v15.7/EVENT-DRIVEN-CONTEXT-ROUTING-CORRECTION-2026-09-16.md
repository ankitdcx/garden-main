# Garden v15.7 EDCR correction and generalization — 2026-09-16

Status: NON_CANONICAL_CANDIDATE AMENDMENT / PROPOSAL_ONLY / NO AUTHORITY / NO PROMOTION
Parent candidate: CAND-EDCR-001

## Clarification being applied

The useful EDCR mechanism remains: event-driven work, structured observations, reusable context, deduplication, materiality gating and compact evidence-bound deltas before expensive reasoning.

One implementation interpretation is corrected. The earlier candidate described GPT-6 Astra as an OpenRouter frontier reviewer. The user clarified that the intended Astra/frontier role is the ChatGPT-side reviewer, not another OpenRouter hop. Garden therefore MUST NOT hardcode an Astra model ID or route the frontier step through OpenRouter.

The repository now represents the frontier role as `EXTERNAL_CHATGPT_FRONTIER_REVIEW`. The concrete ChatGPT model is selected by the user/product context and is not a Garden repository constant. If the user explicitly selects Astra in ChatGPT, Astra can fill that role; otherwise the current ChatGPT model may fill it. The semantic role is stable even when product model names change.

## Corrected pipeline

`event -> cheap/deterministic normalization -> governed observation/context state -> deduplication -> relevance/materiality -> bounded specialist/independent review -> compact GardenFrontierReviewRequest -> external ChatGPT frontier review when warranted -> governed response/proposal -> dependency-aware reuse`

OpenRouter ends at its own reviewer/evidence boundary. It may help create normalized observations, independent findings and the compact request. It does not impersonate or automatically invoke the ChatGPT frontier lane.

## Repo-wide application rule

The mechanism is not limited to OpenRouter review. It applies wherever repeated processing of unchanged state would waste compute or obscure evidence:

- post-merge verification: inspect the merge delta and affected closure first;
- canonical design review: review the changed SectionUnit/dependency closure first;
- public research intake: process new/changed sources and skip duplicate fingerprints;
- ReviewPacket construction: update changed closure frontiers rather than rebuild unrelated context;
- blind review: do not rerun a completed family on an unchanged packet hash;
- cross-examination: wake on new independent evidence or contradiction, not a clock;
- branch/PR hygiene: react to branch/PR state changes or freshness expiry;
- implementation/integration: use changed paths, contracts, tests and collision evidence;
- pipeline health: inspect changed/stale/failing health evidence before broad audits;
- repo reconciliation: process changed receipts/pending identities;
- protocol/pipeline simplification: wake from measured growth/duplication or a due assurance obligation;
- successor composition: compose from newly admitted deltas, while retaining complete release closure;
- knowledge refresh: revalidate the affected dependency subtree rather than rebuilding fresh unaffected knowledge;
- ChatGPT frontier review: only after a reason-coded materiality receipt.

The executable applicability profile is `governance/EVENT_DRIVEN_WORK_POLICY_v1.json`.

## Whole-context fallback is mandatory when needed

Delta-first is an optimization, not an epistemic shortcut. Garden must expand to wider or full context when:

1. dependency closure is unknown or incomplete;
2. DesignEpoch or canonical source root changed;
3. a high-risk semantic change crosses multiple owners/files;
4. a compact packet cannot establish affected invariants/contracts;
5. whole-source Compare/Proof/Evidence/Tier-A closure is required;
6. an assurance/audit obligation explicitly requires full revalidation;
7. contradiction or contamination cannot be resolved from the compact packet.

If sufficiency is uncertain, the result is `PACKET_INCOMPLETE`, `UNKNOWN`, `INCONCLUSIVE`, or an explicit context-expansion request — never an invented conclusion.

## Additional invariants

EDCR-011: OpenRouter cannot stand in for the external ChatGPT frontier lane.

EDCR-012: Garden does not hardcode a changing ChatGPT product model name as a semantic architecture dependency.

EDCR-013: Due intervals are freshness constraints and do not authorize polling unchanged state.

EDCR-014: Delta-first processing cannot weaken whole-source closure, Tier-A, Challenger, Proof, Evidence or protected-authority requirements.

EDCR-015: Reusable context is invalidated by affected dependency change, source-root/DesignEpoch change, expiry or overturning evidence and must then be selectively or fully revalidated according to closure.

## Admission boundary

This amendment corrects and broadens CAND-EDCR-001. It does not promote v15.7, modify canonical v15.5 semantics, grant deployment permission or resume the paused Garden coordinator. Canonical incorporation remains a separate governed decision.
