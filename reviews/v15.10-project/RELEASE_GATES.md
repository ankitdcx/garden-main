# v15.10 Hard Release Gates

A positive release claim requires every gate below.

## G1 — Source completeness
PASS only if the frozen source inventory covers the complete identified 15.x semantic universe, including scattered upgrades and review blockers.
UNKNOWN/BLOCKED is not PASS.

## G2 — Item-level coverage
Every unique semantic item has a ledger row and explicit disposition.
Count of UNACCOUNTED items = 0.

## G3 — Exact-detail preservation
All unique IDs, SchemaIDs, rights, registries, invariants, FunctionContracts, tests, equations, algorithms, bounds,
fallbacks, exceptions, profiles and mappings are either present directly or have explicit proven equivalent current owners.

## G4 — One current owner
No semantic fact has competing controlling current definitions.
Duplicate appearances are references/projections/aliases only.

## G5 — Current self-containment
BOOK + TECHNICAL + CATALOGUE are sufficient to interpret current Garden.
No prior version, historical file, compressed archive, database, network resource or model answer supplies missing current semantics.

## G6 — No old-version dependency in current sources
BOOK, TECHNICAL and CATALOGUE contain no semantic dependency on old Garden releases.
Version numbers older than v15.10 may appear only where unavoidable as non-semantic identifiers/hashes during review; final current source must remove them.
VERSION_HISTORY is exempt because lineage is its purpose.

## G7 — Reference closure
Zero unresolved current anchors, paths, IDs, owner references, schema/test references or aliases.

## G8 — Status preservation
CURRENT/CANDIDATE/DEFERRED/RESEARCH/ON_HOLD/RESERVED and other material statuses are not silently promoted or collapsed.

## G9 — Theory/formal preservation
All retained theory equations, applicability conditions, assumptions, non-equivalences, falsifiers/limits and authority boundaries are preserved.

## G10 — Rights/authority/safety preservation
No compaction weakens Constitution, human sovereignty, Human-Effect Closure, consent, privacy, authority, K0P, emergency, security, law/policy or required assurance.

## G11 — Independent specialist review
GPT Worker + DeepSeek + Qwen + Gemini each complete a frozen review or the unavailable lane is explicitly BLOCKED.
A claimed "full specialist board reviewed" status is forbidden if any required lane is blocked.

## G12 — Independent GPT verification
A separate GPT Verifier that did not draft/integrate the candidate must audit process integrity and attack the frozen integrated candidate.
Positive release requires verifier PASS or PASS_WITH_CAVEATS with no unresolved material caveat.
Verifier FAIL or UNKNOWN blocks COMPLETE_LOSSLESS_CANDIDATE.

## G13 — Re-review after integration
Material fixes are reviewed against the integrated candidate, not only against source fragments.

## G14 — Machine checks
Run identifier inventory, reference closure, duplicate-owner detection, forbidden-old-version scan, source-item coverage accounting and deterministic hashes over final text files.

## G15 — Human decisions
Any unresolved major architecture/constitutional/original-intent choice is presented to the human; it is not silently chosen by reviewers.

## Allowed completion labels

- COMPLETE_LOSSLESS_CANDIDATE — all gates pass.
- CANDIDATE_WITH_OPEN_GAPS — candidate exists but at least one non-authority gap remains.
- BLOCKED — required source/reviewer/evidence unavailable.
- PROCESS_FAIL — review integrity was materially broken.

No smaller file size, majority vote, reviewer confidence or prose quality can substitute for these gates.
