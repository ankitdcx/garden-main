# Garden v15.7 EDCR inherited semantic bindings — 2026-09-16

Status: NON_CANONICAL_CANDIDATE AMENDMENT / PROPOSAL_ONLY / NO AUTHORITY / NO PROMOTION
Parent candidate: CAND-EDCR-001

## Purpose

This amendment closes the semantic-integration gaps identified during review of the event-driven context-routing candidate without duplicating mechanisms that Garden already owns elsewhere.

The seven concerns are valid, but their underlying semantics already exist in the v15.6 gap-closure candidate and executable reference kernel. EDCR therefore **inherits and consumes those owners** rather than defining parallel authority, bootstrap, provenance, causality, reasoning, language or catalogue systems.

Source owner set: `design_deltas/v15.6/DELTASET-2026-09-13-GSL-GAP-CLOSURE.json`.
Catalogue bindings: `design_deltas/v15.6/CATALOG_ADDITIONS.json`.
Executable conformance: `implementation/tests/test_gap_closure_v156.py` and its referenced kernel modules.

These remain successor-candidate semantics until separately admitted/promoted. Binding them here does not turn v15.6/v15.7 candidates into canonical v15.5 semantics.

## Inherited owner bindings

### 1. Authority composition — inherit V156-GAP-002

EDCR does not create `AuthorityCompositionProof/v1`. The existing owner is:

- `AuthorityProvenanceChain` — `SCHEMA-29C6CEDD2A`;
- `ActionEligibleClaimBinding` — `SCHEMA-8A6F0B6EA4`;
- executable owner: `implementation/garden_kernel/authority_path.py`.

A shared-state/context handoff never resets authority. If an EDCR-derived artifact later becomes action-eligible, effective authority is the intersection of the acting authority and every controlling authority in the artifact's provenance chain. Insufficient/empty effective authority rejects the action.

A frontier review by itself is proposal evidence, not an action, so it does not acquire or mint action authority merely by being invoked. The authority-composition check becomes mandatory before any downstream action-eligible use.

### 2. Bootstrap trust — inherit V156-GAP-001 and existing HUMAN admission

EDCR does not create a parallel `BootstrapAdmissionReceipt/v1`. The existing owners are:

- `BootstrapTrustRootCeremonyProfile` — `SCHEMA-977CD6ABF7`;
- `FrozenVerifierBinding` — `SCHEMA-B45623B44B`;
- existing HUMAN/base-admission and protected admission machinery.

The initial EDCR materiality/compression profile may be specified as a candidate, but it cannot self-admit or bootstrap its own authority. Activation that depends on a new first-epoch trust root must bind the existing bootstrap ceremony/HUMAN-admitted governance path.

### 3. Provenance redaction vs absence — inherit V156-GAP-008

High-assurance, protected or redaction-bearing EDCR provenance views must use the existing:

- `ProvenanceClassManifest` — `SCHEMA-1A6E45501B`;
- `ProvenanceGapDisposition` — `SCHEMA-30D7E367A8`.

The manifest is committed by Merkle/content root and distinguishes:

- expected-but-protected/undisclosed -> `REDACTED/PROTECTED` with commitment;
- expected but no valid committed node/edge -> `PROVENANCE_GAP`;
- class outside the applicable manifest -> `NOT_APPLICABLE`.

Low-assurance public packets do not automatically require a heavyweight manifest when no protected/redacted lineage exists; ordinary evidence back-pointers remain required. The owning assurance profile decides when the high-assurance manifest is mandatory.

### 4. Causal typing — inherit V156-GAP-005

EDCR does not label every dependency as causal. Only operational `causes` edges carry `CausalRelationLevelBinding` — `SCHEMA-897FB2274E` — with level C0..C4.

A consumer that requires a stronger causal level than the supplied edge provides must receive `CAUSAL_LEVEL_UNDERFLOW`. C2+ requires the owning model/assumption/evidence obligations; C3/C4 require applicable intervention/counterfactual identification obligations. Non-causal dependency, provenance, supersession and contradiction edges retain their own relation types.

### 5. R0 sanity separation — inherit V156-GAP-006

EDCR uses the existing `SanityGateResult` — `SCHEMA-29A1A917BC`.

R0 is the terminating deterministic/total sanity gate with PASS|FAIL|UNKNOWN. It is not an Engine.Reason mode. R1..R4 may run only after any applicable sanity gate. The sanity gate does not recursively invoke Engine.Reason.

### 6. GSL let/query closure — inherit V156-GAP-003 and V156-GAP-004

Any GSL embedded in an EDCR observation, predicate, materiality expression or context artifact must use the existing repaired language semantics:

- `LetStmt` — `SCHEMA-DB03DABC62`;
- `QueryResultBinding` — `SCHEMA-D17BC951EC`.

A bare `let` is invalid as an expression without `in`, but `LetStmt` remains valid in an enclosing statement/module scope and has Unit result. A query must bind with `into` **or** target a declared module/process output sink in the active FunctionContract; otherwise it fails with `QUERY_RESULT_UNCONSUMED`.

### 7. AuthorityDecl / EffectDecl catalogue closure — inherit V156-GAP-009

EDCR artifacts that carry GSL `AuthorityDecl` or `EffectDecl` use the existing catalogue identities:

- `AuthorityDecl` — `SCHEMA-A8447C581A`;
- `EffectDecl` — `SCHEMA-D1DD528992`.

No local EDCR aliases or second semantic identities are permitted. A declaration that cannot be resolved through the applicable catalogue/reference-closure path is blocked as an unresolved type/reference-closure defect.

## EDCR binding invariants

EDCR-016: A shared-state EDCR handoff preserves `AuthorityProvenanceChain`; any downstream action-eligible use is bounded by the existing authority-intersection rule and cannot gain authority by passing through normalizer, gate, reviewer, snapshot or frontier stages.

EDCR-017: EDCR materiality/compression profiles cannot self-admit. Bootstrap/first-epoch activation binds the existing HUMAN/base-admission and `BootstrapTrustRootCeremonyProfile`/`FrozenVerifierBinding` owners when applicable.

EDCR-018: High-assurance, protected or redaction-bearing EDCR provenance views bind `ProvenanceClassManifest`; redaction, provenance gap and non-applicability remain machine-distinguishable.

EDCR-019: Operational causal claims in EDCR use `CausalRelationLevelBinding`; consuming a weaker causal edge above its qualified level fails with `CAUSAL_LEVEL_UNDERFLOW`. Non-causal dependencies are not relabelled as causal.

EDCR-020: R0 remains `SanityGateResult`, not Reason. Applicable sanity checks terminate independently and R1..R4 are not invoked when the sanity gate fails.

EDCR-021: Embedded GSL follows the existing deterministic Let/Query semantics. Bare let-as-expression without `in` is invalid; `LetStmt` remains valid in statement scope; query results require `into` or a declared FunctionContract output sink.

EDCR-022: `AuthorityDecl` and `EffectDecl` resolve to their existing catalogue SchemaIDs. Unresolved declarations block reference/type closure; EDCR cannot invent replacement identities.

## Additional conformance requirements

13. Shared-state authority amplification: an EDCR-derived action-eligible artifact whose producer/control chain lacks the target action/resource is rejected by the existing authority-intersection mechanism.
14. Bootstrap binding: an EDCR profile cannot claim first-epoch acceptance without the applicable existing bootstrap/HUMAN-admission evidence.
15. Provenance disposition: a high-assurance snapshot distinguishes REDACTED from PROVENANCE_GAP and NOT_APPLICABLE through the committed provenance-class manifest.
16. Causal underflow: a C0/C1 operational cause cannot satisfy a C2+ consumer; non-causal dependency edges are not forced into C0..C4.
17. Sanity separation: R0 terminates as PASS|FAIL|UNKNOWN and cannot be parsed/invoked as R1..R4 Reason.
18. Language closure: bare let-as-expression without `in` fails; LetStmt in statement scope passes; a query without `into` passes only with a declared FunctionContract output sink.
19. Catalogue closure: EDCR-carried AuthorityDecl/EffectDecl resolve to `SCHEMA-A8447C581A` / `SCHEMA-D1DD528992`; unknown replacement identities fail closure.

The existing v15.6 executable tests are reusable evidence for the owner semantics. EDCR qualification must additionally prove that its own handoff/context implementation actually invokes or preserves these owners when their applicability conditions are met.

## Successor-route classification

These bindings do **not** automatically make CAND-EDCR-001 `MAJOR_PROTECTED` merely because EDCR depends on authority/HSA/protected owners.

Garden distinguishes **using an existing protected rule** from **changing protected semantics**. Route classification is derived from the actual composed delta:

- if an EDCR successor changes authority, HSA, rights or constitutional semantics, it must route `MAJOR_PROTECTED` and obtain the existing protected HUMAN decision before promotion;
- if it changes cross-cutting architecture without changing protected semantics, the ordinary route classifier may still require MAJOR-level assurance (including simplification/enforcement requirements) without inventing protected authority;
- PATCH/MINOR/MAJOR classification cannot be chosen merely to reduce assurance work.

Any eventual canonical promotion remains a separate governed act. This amendment creates no deployment, execution, authority or canonical effect.
