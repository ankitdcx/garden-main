# V1511-KR-001 — Continuous Epistemic Assimilation & Consolidation (CEA)
**Status:** CANDIDATE / NOT CANONICAL / NOT EXECUTABLY OR EMPIRICALLY CERTIFIED. **Lineage:** v15.6 `DELTASET-2026-09-14-KR-CEA.json`, September 14 historical ledger §C, v15.11 retention ledger and recovered technical directions. This is an additive *candidate* contract, not a new top-level Engine, source of authority, model training implementation, or constitutional change.

## 1. Purpose, scope and owner
Continuously turn new observations, conversations, experiments and authorized agent discoveries into **reusable, qualified knowledge** without requiring model-weight retraining, while preventing poison, duplicates, loss of contradictions, privacy violations and authority laundering. Reuse `Capability.Knowledge`, GSL-KR, Engine.Search/Compare/Reason/Proof, Provenance, BeliefTimeline, EpistemicTransition, HistoricalSemanticSummary, dependency revalidation and existing AAP/ActionGate/Evolve admission. Each owner retains its semantics; CEA is a bounded orchestration/profile over these existing owners.

Invariant: **runtime cognition != governed persistent knowledge != loss-aware compression != model/scaffold consolidation != authority != constitutional change**.

## 2. Five learning strata
A. `EPHEMERAL_COGNITION`: observations/hypotheses/provisional reasoning; not automatically durable truth.
B. `GOVERNED_PERSISTENT_KNOWLEDGE`: provenance-checked, typed, scoped, retrievable claims with epistemic status and invalidators.
C. `LOSS_AWARE_DURABLE_DISTILLATION`: existing historical summaries plus compression receipts; never mislabel lossy as complete.
D. `MODEL_OR_SCAFFOLD_CONSOLIDATION_CANDIDATE`: proposal to alter MODEL/SCAFFOLD/VERIFIER/TOOL/POLICY_IMPLEMENTATION; does not mutate deployed assets.
E. `PROTECTED_NORMATIVE_ROOT`: rights, sovereignty, authority and protected governance remain governed separately and cannot be written by epistemic promotion.

## 3. Candidate artifact contracts
### EpistemicDeltaCandidate
Minimum fields: stable candidate identity; claim/evidence references; source/provenance and originating agent/model/tool/version; event and observation time; effective temporal and contextual scope; novelty class; epistemic/uncertainty status; contradiction and dependency references; derivation lineage; privacy/retention classification; validity/freshness and invalidators. Reject or mark incomplete when mandatory provenance/scope is absent; never silently infer authority from the submitting agent.

### KnowledgeAssimilationReceipt
Inputs: candidate + qualified source/evidence lineage + current knowledge snapshot + owner-qualified applicability/privacy/authority gates. Outputs: disposition **ACCEPTED, REJECTED, MERGED, CONFLICTED, UNKNOWN, VERIFY_MORE, PRIVACY_OR_AUTHORITY_RESTRICTED, DUPLICATE, STALE_OR_POISONED**, with decision basis, preserved contradiction links, dependency invalidations and provenance. ACCEPTED means admission only to its declared epistemic scope, not permission to act.

### KnowledgeCompressionReceipt
Bind source snapshot/retention class, compressed artifact, preserved conclusions and falsifiers, useful failed branches, known omissions, declared loss budget, reconstitution pointers when lawfully retainable, and dependents requiring revalidation. Reuse HistoricalSemanticSummary when adequate; do not create a competing summary authority.

### CrossContextPatternReceipt
Inputs: separately scoped events/contexts plus explicit permitted join purpose/authority/privacy conditions. Output: bounded derived pattern/hypothesis, supporting lineage, affected contexts, privacy-minimized evidence or lawful pointers, counterexamples and expiry. If join permission is missing, return restricted/non-PASS; no universal raw-data access.

### ModelConsolidationCandidate
Fields: target kind (MODEL/SCAFFOLD/VERIFIER/TOOL/POLICY_IMPLEMENTATION), evidence of stable reusable benefit, intended change and scope, predecessor/epoch, risk and regression hypotheses, owner, external independent review and applicable protected evolution/admission path. No receipt here can itself update weights or privileged scaffolds.

## 4. Candidate assimilation process
1. **Observe:** capture candidate with original source identity, temporal scope, epistemic class, privacy class and declared dependencies; keep observation, testimony, inference, simulation, proof and generated hypothesis distinct.
2. **Gate:** check lawful purpose, scope, consent/authority where applicable, privacy minimization and retention. Denied cross-context joins stop without exposing protected raw data.
3. **Deduplicate and lineage-check:** find semantic duplicates, derivation chains and common ancestors. One unsupported source echoed 100,000 times is still one lineage, not 100,000 independent confirmations.
4. **Compare:** check existing claims, applicability, freshness, contradiction, scope, alternative explanations and independent verification requirements. Do not use confidence/consensus alone as proof.
5. **Reason/verify:** invoke existing qualified Compare/Reason/Proof/Evidence owners within resource limits; record UNKNOWN/VERIFY_MORE when requirements cannot be satisfied. No unbounded self-confirming loop.
6. **Assimilate:** issue KnowledgeAssimilationReceipt; preserve contradictory evidence, append belief transitions and provenance. Material accepted updates invalidate dependent summaries, predictions, decisions, proofs and caches as required.
7. **Retrieve/reuse:** on subsequent tasks, retrieve validated, *currently applicable* knowledge instead of rediscovery when permitted and when independent recomputation is not required.
8. **Compress:** optionally produce loss-aware durable summary and receipt; preserve falsifiers and reconstruction limits.
9. **Escalate consolidation:** propose (never auto-apply) model/scaffold/tool changes through existing Evolution/DesignEpoch/independent admission.
10. **Measure and correct:** report knowledge-dividend metrics, invalidation latency, poisoned/stale reuse, benefit, and bounded failure modes. Material new evidence reopens prior dispositions.

## 5. Mandatory candidate invariants
KR-CEA-001 Knowledge is not authority; 002 runtime learning without weight mutation; 003 provenance before trusted promotion; 004 contradictions survive assimilation; 005 privacy-bounded correlation; 006 distillation declares loss; 007 no automatic constitutional promotion; 008 poison/synthetic repetition does not self-amplify; 009 derivation lineage persists; 010 new evidence revalidates dependents; 011 retrieval preferred where valid; 012 model upgrades separately governed; 013 corroboration independence is lineage-aware; 014 reuse requires current applicability. These inherit the v15.6 delta definitions; collisions with existing Garden owners require explicit comparison.

## 6. Failure / recovery / resource boundary
- Missing provenance, stale context, invalidated dependency, unknown source independence, poisoning signal, forbidden privacy join or conflicting claims cannot be silently converted to PASS.
- If verification budget expires, preserve candidate and typed incomplete/unknown disposition; do not retry indefinitely or raise confidence by repetition.
- Lawful erasure may remove protected payload while preserving only legally permitted minimum tombstone; dependent conclusions become STALE/NEEDS_REVALIDATION.
- Distributed/parallel workers must not count copies as independent evidence or bypass epoch/authority limits. Corrections append to belief history rather than silently rewriting prior claims.
- Any action based on new knowledge still passes independently applicable rights, human effects, consent, safety, law, proof and live authority gates.

## 7. Measurement contract
Where practicable record raw tokens/compute, verification and maintenance cost, validated durable knowledge size, valid reuse counts, recomputation avoided, invalid/poisoned rejected claims, stale reuse incidents, compression ratio/loss budget, time to revalidation, time to obsolescence, and authorized benefiting agents/tasks. Candidate knowledge dividend = qualified future cognition saved or improved relative to production + verification + maintenance cost, with declared assumptions; it is **not** authority or proof of RSI.

## 8. Required conformance tests (specifications, not executed evidence)
- TEST-KR-CEA-001: verified novel fact retrievable without weight change.
- 002: unsupported mass repetition cannot promote a claim.
- 003: contradictory accepted evidence updates BeliefTimeline and invalidates dependents.
- 004: authorized cross-context pattern correlation works.
- 005: forbidden cross-context join remains inaccessible.
- 006: lossy compression cannot claim complete reconstruction.
- 007: high-confidence discovery cannot change constitutional authority.
- 008: valid reusable discovery avoids unnecessary rediscovery when independence not required.
- 009: synthetic common-lineage descendants do not count as independent corroboration.
- 010: ModelConsolidationCandidate cannot mutate deployed weights without separate evolution.
- 011: 100,000 synthetic reports derived from one unsupported source do not increase independent-evidence count.
- 012: stale or scope-mismatched retrieval cannot substitute for current applicable knowledge.

## 9. Qualification and admission
Before promotion: run GSL-COMPARE against existing Knowledge/KR/BeliefTimeline/Reason/Proof/Evidence owners and simpler DO_NOTHING alternatives; resolve schema and ID collisions; require at least three independent qualified reviewer families (prefer four), blind findings before cross-examination, privacy/rights/authority/safety review, adversarial poisoning/common-lineage tests, implementation and evidence receipts, source/epoch binding and full dependent regression review. Any UNKNOWN required gate blocks promotion. A proposed receipt/schema is not an independently executed test or proof.

**Source-grounded vs new organization:** artifact names, strata, invariants, tests and core limits are retained from the v15.6 KR-CEA delta and September 14 ledger. The numbered 10-step workflow and field grouping here are a **candidate integration organization** for review, not a claim that this exact ordering was already admitted.
