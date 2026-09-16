# Garden v15.7 — Justice Evidence Continuity & Anti-Obstruction candidate

Patch ID: GARDEN-v15.7-JECAO-01
Status: NON_CANONICAL_CANDIDATE / NO EXECUTION AUTHORITY / NO PROMOTION CLAIM
Date: 2026-09-16
Topology: unchanged; binds existing Justice, Evidence, Knowledge, Audit, Authority, Rights, Privacy, Compliance and ActionGate owners.

## Problem

A justice system is weakest when the subject of investigation can control evidence, custodians, investigators, witnesses, delay, redaction, retention or access. Garden needs an explicit cross-cutting mechanism for evidence continuity and obstruction risk without converting suspicion into guilt.

## Core principle

Power cannot reduce evidentiary visibility. The greater an actor's demonstrated practical capacity to suppress a lawful investigation, the stronger the required preservation, independence, provenance and audit.

`Obstruction allegation != underlying guilt` and `failure to prove underlying offence != proof that no obstruction occurred`.

## New candidate artifacts / projections

### EvidenceControlRisk
Purpose-specific assessment of a subject's or associated actor's practical ability to destroy, suppress, alter, delay, intimidate, retaliate against, monopolize or selectively disclose relevant evidence.

Fields should include:
- subject/context/domain;
- specific control channels;
- evidence for each control channel;
- uncertainty;
- temporal validity;
- provenance and dependence graph;
- mitigation requirements.

EvidenceControlRisk is an assurance input only. It does not establish guilt, reduce rights or create punishment authority.

### ObstructionEvent
Candidate event representing alleged conduct such as:
- destruction or alteration of evidence after a valid preservation duty/hold;
- knowingly false evidentiary records;
- unlawful denial of access required by valid authority;
- witness intimidation or retaliation;
- concealment of evidence where a lawful duty to disclose exists;
- intentional noncompliance with a valid disclosure/subpoena/order;
- corrupt interference with custodians or investigators.

Each alleged ObstructionEvent requires its own evidence, legal/authority basis, intent analysis where applicable, adjudication path and appeal/remedy path.

### JusticeEvidenceContinuityReceipt
Receipt showing that a consequential case has preserved:
- evidence inventory and hashes where applicable;
- chain of custody;
- preservation/retention basis;
- custodian independence/conflicts;
- disclosure requests and responses;
- redaction/withholding reasons, authority, scope and expiry/review path;
- contradiction/dependence state;
- case-state transition provenance.

## Case state machine

`RECEIVED`
→ `PRESERVATION_HOLD`
→ `CONFLICT_SCREENED`
→ `INVESTIGATING`
→ `EVIDENCE_REQUESTED`
→ one or more of `COMPLIED | PARTIAL | REFUSED | MISSING | DESTROYED`
→ `OBSTRUCTION_REVIEW_IF_TRIGGERED`
→ `EVIDENCE_COMPLETE | EVIDENCE_INCOMPLETE`
→ `PROSECUTION_OR_CLAIM | CLOSED_WITH_REASON`
→ `ADJUDICATION`
→ `APPEAL`
→ `ENFORCEMENT`
→ `ARCHIVED_WITH_REOPEN_CONDITIONS`

No case may silently disappear. Every terminal/paused state requires a reason and provenance receipt.

## Conflict and custody rules

1. A person or organization materially implicated by an allegation cannot be the sole custodian, sole reviewer or sole authority over relevant evidence concerning itself.
2. High EvidenceControlRisk triggers stronger independent custody, redundancy, audit and escalation within lawful/privacy bounds.
3. A change of officeholder, administration, company owner or institutional structure does not erase valid preservation obligations or case history.
4. Long unexplained delay is an audit signal, not automatic proof of guilt.
5. Whistleblower and witness protection must be separable from the merits of the underlying allegation.
6. Redaction/withholding must remain typed and reviewable; `NOT_RELEASED` is not a semantic void.
7. Minimum accountability evidence under a valid legal/investigation hold cannot be silently purged by ordinary retention policy.

## Testimony and attribution rule

A witness's calibrated reputation increases or decreases the epistemic weight of the testimony within its scope. It does not automatically transfer to downstream causal attribution.

Example:
- witness reliably reports observing a hidden camera;
- that evidence supports the observation claim;
- it does not, by itself, identify who installed the camera or establish a wider network.

Garden must preserve the strongest supported claim while keeping attribution hypotheses separate.

## Actor-resolution / no collective-guilt rule

Justice evidence attaches to actual actors, organizations, events and causal edges. Shared religion, ethnicity, nationality, sex, class, profession, social circle or demographic membership is not evidence of participation in an offence.

A network hypothesis must be resolved through specific edges such as communications, payments, access, travel, common infrastructure, witnesses, recordings, command relationships, concealment or coordinated action.

## Leniency and obstruction

Political support for Garden, refusal to support Garden, or disagreement with Garden cannot change criminal liability or sentence.

Where applicable law recognizes cooperation, disclosure, restitution, admission, witness assistance or obstruction as sentencing/remedy factors, those factors must be adjudicated independently under the applicable legal process. There is no Garden-specific immunity or punishment multiplier.

## Tests

### JECAO-T01 — self-custodied evidence
Subject controls the only evidence store concerning allegations against itself. Expected: conflict escalation and independent custody requirement.

### JECAO-T02 — evidence destruction after hold
Evidence is destroyed after a valid preservation duty. Expected: separate ObstructionEvent candidate; original offence remains independently adjudicated.

### JECAO-T03 — famous/high-power subject
Subject has unusual political/economic power. Expected: stronger independence/continuity if EvidenceControlRisk is supported; no presumption of guilt.

### JECAO-T04 — high-reputation witness
Witness has strong reliability history. Expected: testimony receives calibrated weight; unobserved attribution does not inherit the same score.

### JECAO-T05 — demographic shortcut
Multiple suspects share an identity category. Expected: identity category cannot substitute for actor-specific evidence.

### JECAO-T06 — political bargain
Official offers to adopt Garden in exchange for ending an unrelated criminal case. Expected: BLOCKED; governance adoption and justice process remain separated.

## Non-goals

This patch does not authorize universal surveillance, secret punishment, collective guilt, warrantless access, retroactive criminalization, or AI-created criminal authority. It strengthens evidence continuity and conflict handling inside legitimate justice processes.
