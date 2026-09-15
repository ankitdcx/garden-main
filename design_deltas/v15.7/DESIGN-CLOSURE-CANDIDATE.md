# Design closure — supporting amendment
Patch ID: GARDEN-v15.7-DESIGN-CLOSURE-01
Revision: 2, consolidated with final accepted clarifications.
Status: NON_CANONICAL_CANDIDATE_PENDING_RECONCILIATION_AND_ADMISSION.
Target: v15.7, additive to the pinned v15.6 working candidate (not a promoted release); no new top-level engine or parallel review process.

## Relationship and independent progress
Support Candidate A (COGNITIVE-CORE-CANDIDATE.md) and Candidate B (COGNITIVE-COMPARE-CANDIDATE.md) by reusing their versioned records.
Qualification, comparison and design closure may proceed in any order and finish at different times. Shared records do not impose automatic completion gates. A claim requiring combined evidence waits for that evidence.
Qualification tests behavior; comparison accounts for bounded external mechanisms; design closure checks explicitness, coherence, justified choices and earned complexity. This amendment does not establish universal best-design status, capability, safety or comparative performance.

## 1. Mechanism completeness
For each of Candidate A's seven cognitive functions, bind input/output types, internal state, concrete decision/learning procedure, preconditions, uncertainty, dependencies, progress/termination, resource exhaustion, failure detection, recovery and invalidation.
A function name or another unspecified component cannot close a missing explanation. Preserve implementation alternatives where required properties are explicit; record missing procedures as bounded design obligations.
Include a worked normal case and a difficult case with transitions. Difficulty must use declared axes: boundary conditions, unfamiliar inputs, conflicting obligations, degraded resources or increased uncertainty. Define expected behavior before tracing execution and reuse Candidate A evaluation criteria where applicable.

## 2. Bounded composition review
Start with the seven functions, their immediate contracts and four explicit cross-cutting areas:
1. Integrated execution and recovery.
2. Evaluation and baseline bindings.
3. Budget and regression controls.
4. Admission and release dependencies.
Record necessary outward dependencies; unresolved mandatory dependencies prevent affected closure. Scope expansion must be explicit, bounded and justified, not a hidden whole-architecture review.
Check producer/consumer compatibility; circular authority delegation; learning access to protected criteria; compatible precedence of revocation/recovery/continuity; resource ownership and waiting; failure/uncertainty propagation.
Distinguish legitimate feedback from circular justification. Verify exact source/applicability of cited RSN-005, K-INT-002 and REG-GSL-STRUCT-001 SCC/fixed-point provisions before binding them; reuse rather than restate divergent invariants. Check initial conditions, transition bounds and stopping/containment conditions under those owners. Extend only verified gaps.
Contradictory mandatory requirements block affected composition until existing policy owners resolve them. Do not silently weaken requirements.

## 3. Comparative design decisions
Reuse Candidate B's bounded comparator set and rows. Per relevant choice record problem, assumptions, Garden mechanism, named alternative, benefits/costs, limitations and dependency burden, and decision to retain/simplify/extend/replace or leave unresolved.
Broader scope is not superiority. Structural analysis and empirical performance require separate evidence.
Required advantage_type: STRUCTURAL, PERFORMANCE, BOTH, NONE_DEMONSTRATED or UNRESOLVED. A structural advantage does not establish better performance; BOTH needs support for both claims.

## 4. Complexity justification
For each addition compare no addition, smaller/shared extension, and full proposal under existing simplification machinery. Assess duplicate state, interfaces, trusted components, coordination, configuration and verification obligations.
Retain the smallest assessed option satisfying requirements. Preserve justified redundancy for independence/recovery; remove duplication without distinct benefit.
RETAIN_FULL_JUSTIFIED is a positive result when evidence shows removal fails the requirement and assessed smaller alternatives are insufficient. It is bounded to alternatives actually examined, not proof of global minimality.

## 5. One requirement-level consolidated view
One row per stable requirement_id, with one-to-many linked mechanisms, contracts, alternatives and evidence where needed. Columns:
- Requirement: identity, exact source/version, intended behavior and mandatory status.
- Mechanism: concrete owner/procedure and completeness result.
- Composition: dependency and conflict findings.
- Alternatives: comparison-row references, assumptions and trade-offs.
- Complexity assessment: no-addition/smaller/full results.
- Decision: retain, simplify, extend, replace, RETAIN_FULL_JUSTIFIED or unresolved.
- Advantage type with separately supported structural/performance claims.
- Justification/evidence and claim limitations.
- Remaining work, separating design obligations from implementation and empirical questions.
Join Candidate A through requirement_id and function_id; join Candidate B through comparison_row_id and comparator_id. Bind references to record/source versions and preserve multiplicity rather than forcing one comparator per requirement.
If no external comparator applies in the bounded set, record NO_COMPARATOR_IN_BOUNDED_SET and report separately from unresolved mappings. This proves neither defect nor external validation and must not inflate unresolved counts or hide coverage limits.
UNRESOLVED means insufficient evidence/mapping, not an established gap.

## 6. Completion and admission boundaries
Each mandatory requirement must have supported closure or explicit unresolved status with a bounded work item. Finishing review does not mean all requirements closed. Report closed/unresolved and no-comparator coverage separately.
Partial closure is valid; unresolved mandatory design questions block only dependent scope. New mechanisms require separately justified deltas.
Do not infer root cause from underperformance: record observed failure before investigating design, algorithm, implementation, assumptions and evaluation. Verify cited RES-007 if used as an owner; failure itself does not establish causation.
Design closure cannot close qualification failures or measured deficits. Acceptance remains separate:
- Candidate A: declared behavioral criteria and scoped test/admission evidence.
- Candidate B: all bounded comparison rows reviewed/accounted for, not adequacy.
- This amendment: supported or explicitly unresolved design obligations with justified decisions.
Reuse existing review/admission process and artifacts; no new authority from this table or model consensus.
Pin actual predecessor/source and candidate DesignEpoch during reconciliation. Preserve v15.6 and immutable canonical releases.

## Current evidence and next work
Registration preserves user/assistant design review, not source reconciliation or qualified evidence. No tests, root-cause findings, comparator conclusions or admissions are claimed.
Next output: first-pass requirement-level design-decision rows linked to Candidate A per-function dispositions and Candidate B per-comparator scope rows. Record existing coverage/NO_CHANGE where supported rather than force new patches.


## Direct v15.7 release binding — 2026-09-15
The user authorized carrying the prepared v15.6 draft directly into v15.7. The actual canonical predecessor remains Garden v15.5 at source root 63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598. The retained v15.6 working candidate is e3ed83a6607a42d22b5bf3f3ceda425c0a2c807180ac6a69918216807077911b. References to completing v15.6 mean qualifying the necessary inherited scope; no intermediate canonical promotion is required merely to construct v15.7. This binding corrects the earlier anticipated lineage, preserves requirement semantics and grants no execution or qualification authority.
