# Garden v15.10 — mandatory release blockers inherited from v15.9 review

**Date:** 2026-09-18  
**Status:** NONCANONICAL REVIEW / HANDOFF EVIDENCE — MANDATORY INPUT TO v15.10 CLOSURE  
**Canonical effect:** NONE  
**Purpose:** Ensure the parallel v15.10 abstraction/rewrite does not preserve known v15.9 compression defects or silently lose 15.x/scattered accepted semantics.

## 1. Exact v15.9 rewrite files reviewed

The review findings below were bound to these five current-design v15.9 text files generated in the ChatGPT project:

| Role | File | Bytes | SHA-256 |
|---|---|---:|---|
| User | `garden_user_v15.9.txt` | 113789 | `d20846d680c2a0a167a97785fe97e0ffce07239f4b666503c9db00295469409f` |
| System | `garden_system_v15.9.txt` | 232805 | `4005a9277d80eb249b2aa4b65572577a29022209bfa3ae19b4cb460aa479fb7e` |
| Technical | `garden_technical_v15.9.txt` | 829833 | `1e6319b7d68e7d7ec93035d3b8cbd4947b6ee9568c9208ee2ffe627f527b1c4b` |
| Theories | `garden_theories_v15.9.txt` | 161896 | `abb04d5602c3f022bd9dbf38cf5e171b6a30bac51c0a2fcf21fb48003cf4dd6a` |
| Annexure | `garden_annexure_v15.9.txt` | 691676 | `fb10089b4f426ed51156127ed4475854aa21b0e9adeb7a135eed8e328a9778c8` |

Total: **2,029,999 bytes**.

These files are not promoted by this note. They are the audited transition input that v15.10 must supersede safely.

## 2. Review disposition

**v15.9 is not accepted as gap-free final source.**  
The abstraction direction is sound, but the current rewrite compressed some candidate assurance/traceability material too aggressively.

Do **not** repair v15.9 as a separate release unless explicitly requested. v15.10 should absorb and close the findings below while performing its broader abstraction work.

## 3. Mandatory v15.10 blockers

### B-01 — Candidate test/assurance obligations were dropped from the publication

A deterministic comparison against retained 15.x/review material found **at least 94 candidate test identifiers/definitions absent from the current five-file v15.9 publication**. Examples observed included families such as:

- `TEST-CON-EVT-005..007`
- `TEST-KR-CEA-001..012`
- `TEST-REASON-R0-001`
- `TEST-RIGHTS-VIEW-001`
- material `TEST-SPH*` process-hardening families

This does **not** imply 94 capabilities vanished. In many cases the governing concept survived while the exact candidate obligation/test definition did not.

**v15.10 requirement:** every retained 15.x candidate obligation/test must be:
1. preserved directly; or
2. mapped to an abstract invariant/test family with explicit equivalence/coverage evidence; or
3. explicitly superseded/deferred/rejected with reason and owner.

No silent omission is permitted. Recompute the exact count from the full 15.x/scattered-upgrade corpus; do not trust the number 94 as a permanent catalogue count.

### B-02 — Dangling owner/anchor references

Observed unresolved references include:

- `[A-CPI]`
- `[A-CANDIDATE-TRACE]`

The v15.10 owner/namespace abstraction must resolve them to exactly one current owner or explicitly mark them historical/deferred/unresolved.

### B-03 — Duplicate semantic owner anchors

Observed duplicate/current-owner risk included:

- `[S-REFERENCE-CLOSURE]`
- `[RA-PROFILES]`
- `[A-REFERENCE-CLOSURE]`

v15.10 must enforce one authoritative semantic owner per fact/anchor. Additional appearances must be typed references/projections, not competing owner definitions.

### B-04 — Blank SemanticAnchor declarations

Two blank `SemanticAnchor:` declarations were found in the v15.9 rewrite.

**v15.10 requirement:** zero blank/invalid current anchors.

### B-05 — Stale current-version/current-release wording

Current-design text still contained statements referring to older v14.8.x material as the current documentation release, plus at least one obsolete theories filename/current-reading reference.

**v15.10 requirement:** historical versions may remain only as explicitly historical provenance. No stale predecessor statement may present itself as current v15.10 state.

### B-06 — Stale catalogue/count metadata

Some fixed catalogue-count wording no longer matched the current inventory after consolidation.

**v15.10 requirement:** derive counts from the current authoritative registry/catalogue or remove brittle duplicated counts. A count is metadata, not an authority source.

### B-07 — RVH-4 disposition unresolved

The rationalization/verification-hardening lineage expected `RVH-1..RVH-6`. Several RVH semantics survive, but the review did not establish an explicit surviving v15.9 disposition/equivalence for **RVH-4**.

**v15.10 requirement:** assign one explicit disposition:
`RETAIN | ALIAS | MERGE | SUPERSEDE | DEFER | REJECT`,
with owner and equivalence/traceability evidence where applicable.

### B-08 — Human-Effect Closure and similar candidate owner/status/schema/test closure

Prior v15.9 review evidence already identified cases where a semantic rule existed but source-bound owner/status/schema/test closure was incomplete, especially Human-Effect Closure.

**v15.10 requirement:** do not invent closure. For each such item:
- prove existing owner/binding; or
- formally introduce/admit the missing binding under the successor process; or
- retain an explicit unresolved/candidate state with a named resolution condition.

### B-09 — Full scattered-upgrade accounting remains mandatory

v15.10 must not use the five rewritten v15.9 files as its only semantic source because that would faithfully preserve v15.9 omissions.

Required review basis:

`v15.10 input = v15.9 current rewrite + full 15.x lineage + scattered accepted upgrades + prior reviewed v15.9 evidence + this blocker ledger`.

## 4. Abstraction-specific rule

The purpose of v15.10 is to abstract repeated modules, invariants, schemas, tests and contracts. Abstraction is allowed to reduce text substantially, but it must preserve semantics.

For every removed/replaced item:

`legacy/current item -> abstract family/template -> parameterization/specialization -> owner -> status -> coverage/equivalence evidence`

must be reconstructible.

Text reduction is not evidence of semantic preservation.

## 5. Mandatory v15.10 release gate

Do not call v15.10 semantically closed until all of the following are true:

- `all 15.x semantic obligations accounted for = PASS`
- `all scattered accepted upgrades accounted for = PASS`
- `old invariant/test -> abstract family mapping = 100%`
- `dangling current references = 0`
- `duplicate semantic owners = 0`
- `blank/invalid anchors = 0`
- `stale current-version claims = 0`
- `unexplained removed IDs = 0`
- `candidate/deferred/research/unresolved status preserved = 100%`
- `RVH-4 disposition = explicit`
- `Human-Effect Closure owner/status/schema/test disposition = explicit`
- `machine-binding incompleteness is not silently promoted`
- `specification != implementation != validation != certification` remains explicit
- `fresh independent semantic-loss/adversarial reviewer pass on final v15.10 bytes = PASS or all findings dispositioned`

## 6. Reviewer boundary

The 2026-09-18 chat-side review that produced this handoff included deterministic/source comparison and architectural review. A **fresh external reviewer Agent was not successfully dispatched against the final v15.9 bytes from that chat surface**.

Therefore this handoff must **not** be cited as completion of the final independent v15.10 reviewer requirement.

The final v15.10 candidate should be challenged by a genuinely separate reviewer/model after its exact five-file bytes are frozen. That reviewer should search for semantic loss, false equivalence, owner drift, hidden status promotion, abstraction overreach and cross-layer gaps rather than merely confirm the intended conclusion.

## 7. Authority / promotion boundary

This document:
- does not change Garden canon;
- does not promote v15.9 or v15.10;
- does not allocate new authority;
- does not certify machine bindings;
- does not turn review agreement into Proof;
- exists only so parallel/current/future workstreams cannot miss the known release blockers.
