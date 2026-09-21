# Garden v15.10 Lossless Rewrite & Review Project

Status: ACTIVE / NONCANONICAL REVIEW PROJECT
Lead: ChatGPT lead-integrator
Durable coordination: GitHub repository for connected workers; file/share-link handoff for phone-app reviewers
Human text relay: FORBIDDEN for long reviewer prompts/outputs

## Objective

Produce Garden v15.10 so that:

1. no meaningful 15.x semantic content is silently lost;
2. the current design does not depend on, cite as authority, or instruct readers to consult an older Garden version;
3. every current semantic fact has exactly one controlling current owner;
4. duplicated wording may be collapsed only with explicit coverage/equivalence evidence;
5. all current design sources are ordinary readable UTF-8 text;
6. the final user-facing package is:
   - GARDEN_BOOK_v15.10.txt
   - GARDEN_TECHNICAL_v15.10.txt
   - GARDEN_CATALOGUE_v15.10.txt
   - GARDEN_VERSION_HISTORY_v15.10.txt
7. only the first three are current design sources; Version History is lineage only.

## Meaning of "nothing lost from 15.x"

Every unique 15.x semantic item must receive an explicit disposition:

- RETAIN_CURRENT
- MERGE_EQUIVALENT
- CURRENT_ALIAS
- CANDIDATE
- DEFERRED
- RESEARCH
- SUPERSEDED_WITH_CURRENT_OWNER
- REJECT_HISTORY_ONLY

Silent omission is forbidden.

Items include, at minimum:
rules, rights, schemas, SchemaIDs, registries, invariants, tests, FunctionContracts, equations, algorithms, time bounds,
fallbacks, exceptions, profiles, theory details, authority rules, migration rules, aliases, status constraints,
proof obligations, reference-closure requirements and scattered accepted upgrades.

"Rejected" or superseded material is not made current merely to preserve history; its disposition belongs in history/evidence.

## Meaning of "no reference to old versions"

BOOK, TECHNICAL and CATALOGUE may not depend on a previous release for meaning.

They must not contain instructions such as:
- "see v15.9"
- "same as v15.5"
- "retained from v15.8" as the definition
- "use predecessor file"
- any other external-predecessor dependency

Current semantics must be written directly as v15.10 semantics.

Compatibility aliases may remain when they are useful current names, but their meaning must be defined in v15.10 itself.

Only VERSION_HISTORY may narrate old version numbers/lineage.

## Source universe

The review source universe is larger than the five rewritten v15.9 files.

Required inputs:
- complete canonical v15.x baseline source available in the repositories;
- all v15.x design deltas, candidate amendments and admitted upgrades;
- the complete final v15.9 five-file rewrite;
- scattered accepted upgrades not faithfully carried into v15.9;
- prior review evidence, including PR #91 blocker ledger;
- recoverable v15.10 r6 source/build evidence;
- explicit human design directives relevant to v15.10.

A source item is not excluded merely because it is inconvenient or duplicated.

## Board

### Lead — current ChatGPT chat
Owns:
- source freeze;
- work decomposition;
- reviewer packet construction;
- reconciliation;
- finding dispositions;
- candidate integration;
- coverage and release gates;
- escalation of true design choices to the human.

Lead does not gain truth/authority by role.

### GPT Worker — separate ChatGPT chat
Primary task:
- exhaustive source extraction and source->v15.10 coverage accounting;
- detect dropped exact details;
- propose current owners without rewriting by summary;
- remain independent of the lead's integrated candidate during the initial worker phase.

### GPT Verifier — second separate ChatGPT chat
Primary task:
- stay outside worker drafting/integration;
- audit process integrity;
- independently attack the integrated candidate after it is frozen;
- verify source coverage, exact-detail preservation, current-owner completeness, reference closure, status preservation and old-version-dependency removal;
- return PASS, PASS_WITH_CAVEATS, FAIL or UNKNOWN with evidence.

Verifier is not counted as a second drafting worker and must not be used to manufacture agreement.

### DeepSeek app
Primary task:
- formal/technical consistency;
- implementation feasibility;
- exact equations/algorithms/contracts/tests that abstraction could accidentally erase;
- contradiction and underspecification detection.

### Qwen app
Primary task:
- exhaustive catalogue/identifier/registry/reference audit;
- IDs, SchemaIDs, invariants, tests, FunctionContracts, mappings, profiles and cross-reference closure;
- duplicate-owner and missing-owner detection.

### Gemini app
Primary task:
- whole-architecture coherence and abstraction quality;
- detect semantic collapse caused by overcompression;
- check whether Book/Technical/Catalogue separation is understandable and current-owner-complete.

## Review flow

1. Lead freezes source universe and review packets.
2. GPT Worker + DeepSeek + Qwen + Gemini review independently.
3. Lead freezes raw outputs and reconciles findings.
4. Lead produces integrated candidate and complete finding-disposition log.
5. GPT Verifier receives:
   - frozen source packet;
   - frozen reviewer outputs;
   - frozen integrated candidate;
   - decision/disposition log.
6. GPT Verifier audits process first, then attacks candidate.
7. Any material verifier failure reopens the affected finding/coverage rows.
8. Lead fixes and rechecks until release gates pass or the project is explicitly blocked.
9. Major unresolved architecture/constitutional/original-intent choices go to the human.

## Blindness / independence

Initial reviewers do not receive peer outputs before freezing their own review.
Agreement is not a quality score.
The GPT Verifier is intentionally delayed until after integration and must not participate in candidate drafting.

## Reconciliation

Lead classifies every finding:
OPEN -> CONFIRMED / REJECTED_WITH_EVIDENCE / DUPLICATE / NEEDS_HUMAN_DECISION
-> PATCHED -> RECHECKED -> CLOSED.

Blocking/minority findings cannot be discarded without a recorded evidence-backed reason.

## Final gate

v15.10 is not called lossless/final while any source item is UNACCOUNTED, any current reference is dangling,
any required current owner is missing, any old-version dependency remains in current design, or independent verification
finds an unresolved material loss.

This project produces review evidence and a candidate. Canonical admission remains a separate governed action.
