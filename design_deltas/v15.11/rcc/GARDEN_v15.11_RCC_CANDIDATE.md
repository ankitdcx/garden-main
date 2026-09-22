# Garden v15.11 candidate — Recursive Control Closure

Patch ID: **GARDEN-RCI-RCC-2026-09-22**  
Revision: **1.4 — v15.11 candidate packaging**  
Candidate ID: **V1511-RCC-001**  
Candidate version: **v15.11**  
Target: **v15.11 additive successor candidate to the v15.10 working design**  
Type: additive RCI/CPI hardening  
Status: **DESIGN CANDIDATE — NOT CANONICALLY ADMITTED**

“Final merged” means the original patch and all reviews visible in this conversation have been reconciled. It does not mean implementation, independent verification, deployment, or canonical admission has occurred. Inputs comprise the original RCC patch and supplied reviews 1–5. Review 3 is the six-finding operator review, subsequently reposted during finalization; Review 5 is the additional evaluation with five refinements. Review 1 was also reposted. Repeated text is counted once, not as independent corroboration. Revision 1.4 corrects review attribution and assigns the v15.11 candidate identity; the merged normative rules, operator contracts and 54 test specifications are retained.

This is one additive v15.11 candidate, not a complete v15.11 release or a replacement for the earlier candidate ledger. The exact full v15.10 source binding and integration remain pending; this registration does not relabel the repository's v15.5 canonical source as v15.10. See [candidate manifest](CANDIDATE_MANIFEST.json) and [validation status](VALIDATION.md).

## 1. Scope and architectural boundary

RCC strengthens the existing recursive-change qualification and admission path. It introduces no new theory, Core Object, Core Relation, top-level Engine, scheduler, authority source, or parallel control loop. Its rules are conjunctive obligations within the existing Universal Per-Step path and existing RCI/CPI handling.

- RCI remains the architectural composition over existing owners.
- CPI remains responsible for qualification of changes.
- RCC requires controls to satisfy the obligations created by the actual transition and resulting operation.
- Human-Effect Closure remains controlling even when recursive mechanisms become opaque.

RCC does not grant capability, access, intelligence, reviewer agreement, proof production, or successful behavior the power to create authority. It does not establish universal containment or solve ownership and concentration of compute, capital, energy, or physical power.

The following rules cover capability increases, decreases, lateral changes, changed autonomy, changed deployment conditions, control-system evolution, interacting branches, and consequential adaptations. A weaker model with broader access can create a greater control burden.

## 2. Shared operational contract

### 2.1 Qualification unit

The assessed unit is not just a model name or version. It binds:

`transition = (qualified predecessor/checkpoint, candidate artifact, effective change set, causal dependencies, deployment environment, requested authority, exposure envelope, control configuration, rule/profile versions)`

Training changes, code, prompts, tools, memory/configuration changes, online learning, credentials, replication, network access, deployment topology, verifier selection, and authorization mechanisms enter this unit when they affect an applicable obligation. Material external changes are also qualification events.

Existing admission machinery MUST bind its receipt to the exact assessed unit, including mutable dependency identities and freshness conditions. A changed unit cannot reuse the receipt without verified applicability. Concurrent changes MUST be composed and assessed together before joint activation; two individually accepted branches do not imply an accepted merge.

Creation, testing, admission, activation, and continued operation are distinct scopes. Building or evaluating a candidate may itself be consequential and MUST occur under an independently justified existing development/test envelope. An unqualified candidate receives no production authority merely because it exists.

### 2.2 Required obligations and verified controls

`RequiredControl(T)` and `VerifiedControl(T)` are typed products indexed by applicable obligations, not scalar scores. Capability, autonomy, reach, irreversibility, uncertainty, and possible human effects help derive requirements; they are not themselves interchangeable units of control.

For each applicable obligation, the controlling profile MUST declare:

1. Stable obligation identity, scope, owner, applicability rule, and requirement predicate.
2. Typed evidence requirements, freshness conditions, and accepted evaluation method.
3. A versioned satisfaction comparator and its assumptions.
4. Relevant coupling obligations across dimensions and components.
5. Independent verification/authorization requirements where applicable.
6. Resource bounds, expiry triggers, and safe non-admission behavior.

Minimum covered families are authority; verifier adequacy; required independence; containment/exposure; revocation; recovery/safe termination; enforcement; assumption validity; cumulative/trajectory closure; and Human-Effect obligations. Additional applicable Garden obligations remain in force.

Every required obligation MUST map explicitly to the control mechanism or mechanism composition that discharges it, the supporting evidence, and the responsible existing owner. Human-Effect, consent, privacy, safety and recovery obligations cannot disappear merely because a convenient technical metric is unavailable. A missing or inadequate obligation-to-control mapping is UNRESOLVED, or VIOLATED when failure is demonstrated; it cannot support admission.

Each comparator returns `SATISFIED`, `VIOLATED`, or `UNRESOLVED`, with reasons and evidence references. These are alternatives, not a numeric ranking. Unknown comparators, missing required coordinates, unsupported non-applicability, stale evidence, or incomplete dependency closure cannot produce SATISFIED.

Componentwise closure means every applicable predicate, including cross-component predicates, is SATISFIED. Surplus control on one coordinate cannot compensate for a failed hard requirement elsewhere. Approved alternatives may satisfy the same obligation only through their declared comparison rule, not through score trading.

Applicability and requirement generation MUST be independently controlled at the required assurance level. The proposer cannot lower its own requirements, omit difficult coordinates, or select easier acceptance criteria to obtain admission. Profile changes are themselves governed changes.

### 2.3 Orthogonal output

The existing qualification receipt SHALL retain separate fields:

| Field | Values / content |
| --- | --- |
| AdmissionDecision | `ADMIT`, `BLOCK`, `DEFER` |
| EvidenceCompleteness | `COMPLETE`, `PENDING`, `INCOMPLETE`, `UNKNOWN` |
| ObligationResults | Typed per-obligation comparator results |
| Structural / coherence results | Existing product-status fields, preserved separately |
| Diagnostics | All violations, unknowns, conflicts, invalid inputs, bounds reached, and missing evidence |
| Scope binding | Exact transition, environment, authority, profiles, evidence and expiry dependencies |
| Authority effects | Grants not issued, affected grants suspended, unaffected grants retained, safe-state actions |

COMPLETE means all required evidence slots for the declared scope have been accounted for. It does not mean the evidence supports approval: complete evidence of a violation yields BLOCK. A block never erases separate unknowns or structural defects.

Deterministic admission projection:

1. Known prohibited transition, binding mismatch, invalid authorization, or demonstrated hard-obligation violation → BLOCK.
2. Otherwise, unresolved requirements, inadequacy not yet resolved, missing/stale evidence, invalid structure, or exhausted evaluation bounds → DEFER, with precise diagnostics.
3. Otherwise, all applicable obligations satisfied, evidence COMPLETE, required structural/coherence checks satisfied, and valid authorization present → ADMIT for the exact declared scope only.

Both BLOCK and DEFER prohibit the requested activation. This rule does not flatten or replace existing semantic status products. Legacy PASS displays, if retained, are projections only and cannot hide the underlying fields.

### 2.4 Frozen finite operator contracts

The operators below are specializations of existing qualification, Compare, dependency and verification functions, not new Engines or a parallel evaluator. Their identifiers here are patch-local contract labels, not claims of existing SchemaID registration.

Every target MUST bind a finite profile P to its authorized DesignEpoch and a cryptographic digest over canonical bytes. The committed content includes input/output types and units, uncertainty representation, domain coverage, requirement-generation rules, obligation and evidence catalogues, assumption/materiality predicates, cumulative composition rules, independence threat model, adequacy acceptance rules, comparison semantics, interpreter version, serialization/hashing rules, and resource limits. P cannot leave required behavior to free-text discretion or mutable external configuration. Missing definitions yield DEFER, not implementation-chosen defaults.

Profiles and their updates require the existing independent admission path. A digest identifies exact rules; it does not establish their sufficiency, legitimacy or correctness. Two evaluations with identical canonical inputs, evidence snapshot and profile/interpreter binding MUST return identical operator outputs and diagnostics. Empirical measurements may differ across runs, but their recorded results and uncertainty must be frozen as inputs before decision replay.

#### RCC-OP-A — Accumulate effective state

Inputs: a qualified checkpoint Q; finite causally linked change DAG D; current independently supported observations X; profile P; declared work bound B.

Output: assembled state/feature envelope E, retained obligations and assumptions R, ancestry/evidence commitments, completeness status, and diagnostics/frontier.

Deterministic procedure:

1. Validate Q's qualification and dependency scope; validate D's identities, parent edges, base bindings and completeness claims. Missing parents/cycles or unverifiable scope prevent a complete result. Retain original diagnostics.
2. Compose changes using P's typed, deterministic transition functions. Parent order is causal. Concurrent operations may be put in a canonical order only if P establishes their commutativity for the relevant effects; otherwise require an explicit assessed merge operation. A lexical sort cannot manufacture semantic compatibility.
3. Apply each change to its bound pre-state, producing the composed post-state rather than summing arbitrary capability scores. Carry Q's residual obligations, irreversible effects, consumed budgets, and ancestry-dependent assumptions without subtraction unless an authorized discharge rule and evidence permit it.
4. Run P's finite feature extractors, interaction predicates and uncertainty propagation over the composed state, relevant cross-component dependencies, retained summaries and observations X. They MUST cover the target's declared interaction domain, not only single-field thresholds. Unsupported operations, unmodelled potentially material interactions, or insufficient observations mark the affected envelope UNRESOLVED. Self-declared capability values alone do not establish coverage.
5. Evaluate every applicable cumulative limit and continuation-envelope predicate. Report violations and uncertain crossings separately. Pass E and R to RCC-OP-R for full qualification; crossing a protected limit never activates the candidate while qualification is pending.
6. Halt at B if needed, retain a continuation frontier and mark incomplete. Never discard history or an interaction merely to satisfy B.

For simple scalar state, repeated updates are replayed under their declared algebra; thresholds are evaluated on the resulting state and coupled predicates. For arbitrary emergent behavior, this operator does not promise discovery by syntax alone: the domain coverage and assessment evidence must justify the feature model, or the result remains unresolved. Complete known composition is not proof that an inadequate behavioral model is sound.

#### RCC-OP-R — Generate required obligations

Inputs: E and R from RCC-OP-A; absolute candidate capability/autonomy/reach and exposure envelope; deltas from Q; irreversibility, uncertainty and Human-Effect classes; requested authority, environment and P.

Output: a canonical set of typed obligation instances, each with source rule, owner, mechanism/evidence requirements, applicability status and diagnostics.

P MUST contain a finite rule table. Each row binds a typed, terminating predicate over the canonical inputs to a finite list of obligation templates. All quantities have declared units and boundary comparisons. For interval uncertainty, a predicate is TRUE when established across its supported uncertainty set, FALSE when refuted across it, and UNKNOWN otherwise; nonnumeric claims use equivalently explicit epistemic rules. Unsupported evaluation is UNKNOWN.

The generator proceeds as follows:

1. Start with R's undischarged obligations and P's non-waivable base obligations. Baseline families in Section 2.2 cannot be omitted without a valid, controlling applicability/discharge determination.
2. Evaluate every table row in stable rule-ID order. TRUE adds its instantiated obligations; FALSE adds none; UNKNOWN adds the potentially applicable obligations with unresolved applicability and records the cause. An unknown applicability result may be discharged only by P's explicitly authorized rule, for example by conservatively satisfying the obligation for all relevant cases.
3. Expand obligation dependencies to the least fixed point over P's finite declared obligation-instance universe. Rules may add obligations, not silently remove or weaken them. An inconsistent duplicate requirement, unsupported instantiation or out-of-domain input is diagnostic, never last-write-wins.
4. Attach declared cross-coordinate obligations, materiality triggers and verifier-adequacy requirements. Preserve cause links to RCC-OP-A results and assumptions.
5. Return the canonicalized set and completeness results. Any uncovered required input class, unresolved scope or exhausted bound prevents admission until resolved through the existing path.

A target profile MUST include explicit rules for its capability, irreversibility, uncertainty and human-effect classes, plus catch-all unsupported-class behavior. These are not supplied as universal numerical thresholds in this generic patch. An implementation with this interpreter but no admitted rule table remains NOT READY; it cannot claim an operational RCC gate.

#### RCC-OP-I — Check independence certificate

Inputs: a finite certificate binding identities, control/dependency graph, evidence snapshot, applicable obligation set, acceptance/veto policy and P's threat model.

Output: independence result, completeness, affected claims, counterexample actor/coalition and dependency path when found, or unresolved frontier.

The certificate MUST enumerate relevant training/model/data ancestry, signing roots, credentials, modification and deployment rights, evidence production, verifier selection, bypass/disablement, recovery administration, and correlated dependencies. It must state and support its boundary-completeness claim. A signed assertion does not establish that hidden dependencies are absent.

P MUST define a finite actor set, the single actors and colluding sets against which protection is claimed, typed initial powers, and finite inference rules for gaining powers through controlled components. The rules can represent AND-preconditions such as multi-key approval; they must not treat every edge as equivalent access. Missing relevant actors/classes or unknown effective rights prevent a complete certificate.

For each in-scope adversarial set, compute the least fixed point of attainable powers over the finite graph. Evaluate P's exact acceptance/veto policy against those powers. If that set can change decisive rules/evidence, fabricate a sufficient accepting quorum, neutralize a required veto, substitute the assessed artifact, or bypass activation checks, return VIOLATED with the path. Evaluate outage and correlated-error properties separately under their required obligations. If enumeration or closure exceeds a bound, return UNRESOLVED with a frontier.

Return SATISFIED only when all required cases are evaluated, certificate evidence and boundary coverage meet their declared standard, and no prohibited control path is reachable within the stated threat model. This is a conditional independence certificate, not a claim about every possible hidden actor or unbounded coalition.

The review's shared signing root and common deployment controller must therefore be analyzed by their effective powers. Shared modification/signing control that permits verifier substitution or bypass is a violation; stop-only control with proven safe denial is separately classified as availability risk, not silently equated with forged approval.

#### Adequacy, enforcement and materiality bindings

RCC-OP-R MUST emit verifier-adequacy obligations for the generated task set. A frozen `Adequate(P, verifier, obligations, evidence)` predicate checks property coverage, qualified methods, artifact/specification binding, evaluation-integrity conditions, resource bounds and relevant empirical/formal evidence. A generic “1.5 times smarter” comparison is not a substitute. The verifier's own control requirements also apply, but satisfying those requirements alone does not prove competence at evaluating the successor.

Every required enforcement link MUST have a profile-bound evidence predicate specifying what is measured/proved, by whom, its freshness, resistance to modification/suppression, and how it relates to the claimed effect. A successor-controlled monitor cannot supply independent enforcement evidence merely by reporting success. If a monitor becomes disabled or untrustworthy, dependent claims and grants are treated under RCC-007.

Materiality predicates MUST be frozen in P and linked to the same relevant features and uncertainty representation used by obligation generation. They are assumption-specific: a 2x efficiency gain is material where it invalidates a compute-bound containment assumption, but need not invalidate an unrelated assumption. Different assurance or monitoring thresholds must be explicit and justified; a blanket capability threshold cannot suppress a known assumption failure below it.

These finite procedures ensure reproducible decisions on frozen inputs and bounded non-admission when evaluation is incomplete. They do not establish universal accurate measurement, complete emergence prediction, or open-world safety by definition.

## 3. Governing invariants

### RCC-001 — Recursive Control Closure

> A consequential transition MUST NOT be admitted unless verified controls satisfy every applicable control obligation created by the transition, its resulting state, its authorized trajectory, and its deployment conditions.

Operational meaning:

`ControlClosed(T) := for every applicable obligation o, compare_o(required_o, evidence_o, T) = SATISFIED`

The original `RequiredControl ≤ VerifiedControl` notation is shorthand for this typed, componentwise satisfaction relation, including coupled obligations. It is not a universal quantitative ordering or a claim that open-world safety is decidable.

Capability improvement never offsets reduced control assurance or creates authority. RCC-002–009 specialize particular obligations under RCC-001; their shared coverage is deliberate decomposition, not competing ownership. RCC-004 remains the controlling definition of verifier adequacy within this gate.

### RCC-002 — Cumulative and Trajectory Closure; No Incremental Evasion

> Every activation or authority-bearing use of a changed system MUST account for its effective cumulative change and relevant causal dependencies. Splitting, delaying, renaming, branching, or reordering changes MUST NOT evade qualification.

The effective history consists of the last valid qualification checkpoint, its retained obligations and assumptions, and every relevant subsequent change across all causal parents. Trust-root authorization history, verifier evolution, delegated authority, and changes to the checking mechanism itself are included.

An enforced pre-activation gate MUST update/check the cumulative assessment for each effective change. Lightweight checks may reuse a qualified sufficient summary; they may not skip the event. Unknown impact requires deeper review or DEFER. Thresholds may trigger deeper assessment, but cannot determine whether a change is recorded or screened at all. Timers or periodic reviews may supplement, not replace, this gate.

For online adaptation, a previously qualified envelope may cover a family of changes only if the admission case establishes that the envelope and its runtime enforcement preserve the applicable obligations. Each realized change must remain inside that envelope. Unobserved or unbounded adaptation is not exempt; inability to enforce the bound prevents that operating mode from being admitted.

#### Checkpoint and resource rule

A qualification checkpoint MUST bind the complete assessed state, relevant history commitments, residual risks, irreversible effects, active assumptions, pending obligations, cumulative budgets, and qualified continuation envelope. It must carry sufficient semantic evidence to support later decisions, not merely a hash.

A new checkpoint may replace the active evaluation baseline only after the composed state and carried obligations are re-qualified and independently authorized where required. It cannot erase ancestry-dependent constraints, replenish consumed budgets without justification, or remove unresolved failures. Root changes are not categorically forbidden; they also require RCC-005.

An existing DesignEpoch/DesignBinding may anchor that checkpoint only if the target's actual contract and evidence satisfy these checkpoint requirements. Its name or new version number is not a reset. Previously qualified effects need not be recomputed from raw history while the summary remains sufficient, its assumptions remain current, and interaction with the proposed change is checked.

No sliding window, fixed depth cutoff, number of successful admissions, or period of inactivity is a semantic reset. Implementations may bound work and retain a continuation frontier. Reaching a bound without a valid sufficient checkpoint yields DEFER with an incomplete-closure diagnostic, not a truncated PASS. This permits finite evaluation without pretending that arbitrary histories can always be summarized soundly.

#### Trajectory rule

The assessment MUST cover both the composed current transition and the permitted continuation envelope: reachable capabilities, autonomy, reach, cumulative budgets, assumptions, monitoring, intervention latency, and effects during intervention. A sequence of individually acceptable steps cannot leave that qualified envelope through unchecked accumulation.

This is not a demand to enumerate an infinite future. Where an inductive invariant or a conservatively enforced envelope is unavailable, only a bounded continuation may be authorized. Extending its scope requires new qualification. Exposure, growth rate, and intervention time must be assessed together.

### RCC-003 — Substantive and Recursively Preserved Independence

> Where independent verification or authorization is required, the necessary checking and authorization functions MUST remain outside disallowed common mutable control, including after recursive changes.

Distinct names, processes, model instances, organizations, or credentials do not establish independence. Each protected transition MUST re-establish current independence or verify that an existing independence assessment remains applicable with unchanged relevant dependencies.

The controlling profile MUST publish a dependency/control graph and threat model covering:

- Who can modify the proposer, verifier, policy, evidence, test selection, comparator, or deployment.
- Who holds credentials, recovery keys, administrative rights, and approval powers.
- Who can select, replace, suppress, disable, bypass, or impersonate necessary checks.
- Training, data, code, model ancestry, tooling, infrastructure, and evidence-source correlations.
- Which actors or colluding sets the design claims to tolerate.

The independence test MUST cover compromising an acceptance quorum or necessary veto—not merely disabling every verifier. If any disallowed actor or coalition can fabricate sufficient approvals, neutralize a required rejection, alter decisive evidence, or bypass the gate, independence fails for that claim.

The graph MUST be supported by current evidence of relevant credential separation, effective access permissions, modification/deployment rights, evidence-production and selection controls, and bypass resistance. Lineage/data disclosures and tests of effective isolation inform correlation and control assessments. A declaration of independence or a list of different names is insufficient. Distinct training data are neither universally necessary nor sufficient; the demonstrated control and failure relationships are what govern the decision.

Availability and approval integrity are separate. A provider that can stop all work is a common availability dependency; this does not alone prove it can forge safe approval. Whether the outage is tolerable still depends on recovery and Human-Effect requirements. Shared training/code may create correlated blind spots without common administrative control; such risks require evidence and cannot be assigned an arbitrary compensating weight.

Common origins do not automatically imply present mutable control. An untrusted proposer may supply a proof or candidate verifier artifact, but cannot thereby qualify, deploy, or authorize the checker that accepts it. A protected existing checker/qualification path and independently controlled specifications must establish the new component's adequacy and integrity. If that cannot be established, the transition remains unadmitted.

Any changed parent, training corpus, evaluator, administrative plane, credential chain, or verifier-selection mechanism MUST reopen affected independence claims. Independence at generation n does not automatically carry into generation n+1.

### RCC-004 — Task-Specific Verifier Adequacy Preservation

> Prior verifier qualification MUST NOT be treated as proof of adequacy for a changed verification burden. The verification system must be shown adequate for the exact obligations, threat model, and operating scope of the proposed transition.

Neither organizational independence nor a claim of greater general intelligence is sufficient. Conversely, a verifier need not be generally more intelligent than the proposer if its qualified method can check the relevant claims.

Every adequacy case MUST specify:

1. Exact properties checked, omitted properties, scope, and acceptance criteria frozen before the relevant evaluation.
2. Why the method is suitable: formal proof checking, exhaustive bounded analysis, empirically validated evaluation, independently enforced constraints, or a justified combination.
3. Assumptions, trusted components, correspondence between the checked artifact and deployed artifact, and model-to-world limitations.
4. For empirical/heuristic methods: coverage, calibration, uncertainty, relevant failure modes, and adversarial tests against deceptive or evaluation-targeted submissions. Test secrecy is not a substitute for validity.
5. Independently controlled evidence acquisition and evaluation tooling where required; resources and intervention capabilities commensurate with the actual verification task.
6. Limits, expiration conditions, and procedures for detecting evaluator manipulation or changed capability.

A checked proof establishes only its stated proposition under its assumptions. It does not automatically prove all real-world behavior, rights compliance, or containment. The proof statement, policy, compiler/runtime binding, and checker remain part of the assurance case. Zero-knowledge proofs are optional privacy mechanisms, not a universal additional safety requirement.

A proposer MUST NOT qualify its own verifier by persuasion, confidence, benchmark performance alone, or control of the criteria. Proof-carrying or constrained-interface approaches may avoid needing a more capable general evaluator; where adequate verification remains unavailable, narrow exposure to an independently qualified scope or do not admit the transition.

This does not promise endless recursive progress. A genuine inability to justify control can legitimately stop a transition; it is not permission to relax the gate.

### RCC-005 — Protected Trust-Root Evolution

> A mechanism participating in authority, qualification, verification, constitutional interpretation, cryptographic enforcement, or physical containment MUST NOT solely authorize its own weakening, replacement, or removal, directly or through delegates under its effective control.

Initial trust establishment uses the existing Garden bootstrap/admission owner. RCC does not bootstrap authority from nothing. The review-provided identifier `BootstrapTrustRootCeremonyProfile (V156-GAP-001)` is an integration reference to resolve against the selected target source, not a newly verified registry entry in this patch.

For an established root, a transition MUST provide:

- Separately protected, appropriately independent authorization under the existing constitutional boundary.
- Explicit old/new root identities, responsibilities, policy differences, and migration scope.
- Evidence for equivalence or strengthening where claimed; any weakening explicitly assessed without overriding non-waivable obligations.
- Continuity of enforcement, credential/key handling, and resistance to rollback to a vulnerable root.
- Tested rollback, recovery, or safe handover appropriate to reversibility. Irreversible human effects cannot be undone by restoring software.
- Post-transition verification and protected response if migration fails.

The authorization chain and its cumulative evolution are themselves within RCC-002, RCC-003, and RCC-007. The migration may not disable the existing checks before the replacement has met the obligations needed for its activation.

Hardware roots, separate administrative domains, multi-party authorization, and physical controls SHALL be required where the threat model demands them. Their coverage, failure modes, bypass paths, and recovery must be evidenced. “Immutable hardware,” a named enclave, a voting threshold, or a human key-turn alone is not proof of effective protection. Human participation remains required wherever the existing Garden rules require it; this patch does not impose a new universal single-person root or freeze a defective mechanism permanently.

### RCC-006 — Semantic-to-Physical Enforcement Closure

> A consequential constraint MUST distinguish its stated requirement, executable implementation, credential/cryptographic controls, applicable hardware/network/physical controls, and observed effects. Claimed enforcement cannot exceed the evidenced chain.

The chain is a coverage argument over all relevant action and bypass paths, not a mandatory identical stack for every constraint. Each applicable link requires evidence or an approved, justified alternative that satisfies the same obligation. Non-applicable links require an explicit rationale.

| Condition | Required treatment |
| --- | --- |
| A required executable, credential, network, physical, or other preventive link is missing | No affected activation until the obligation is met through the required or independently qualified alternative control. |
| A required link is unknown or unmeasured | DEFER; do not claim enforcement. |
| Evidence demonstrates a bypass or ineffective control | BLOCK affected activation; suspend dependent active authority under RCC-007. |
| A particular mechanism is absent but a qualified alternative meets the same requirement | The obligation may be satisfied; retain the actual mechanism and limits in the receipt. |
| Only bounded field evidence is available | Admit, if otherwise justified, only the separately qualified pilot/exposure envelope; do not infer broader deployment approval. |
| An effect can only be monitored after it occurs | Monitoring counts only for the obligations it can actually satisfy; it cannot replace prevention of prohibited irreversible harm. |

Lowering the wording of an enforcement claim does not lower the underlying safety requirement. Stating residual risk or accepting it by an unauthorized party cannot repair a hard-gate failure. Compute operators, key administrators, physical access, and hardware supply dependencies belong in the actual enforcement threat model.

### RCC-007 — Capability-Dependent Assumption Expiry and Authority Suspension

> Any material change that invalidates, contradicts, or leaves unresolved a control-relevant assumption MUST reopen dependent qualification and prevent continued reliance on that assumption.

Before production admission, capability and control changes MUST be assessed against the assumptions they may affect. Unknown successor behavior can be investigated only under an independently qualified construction/test envelope. Creation is not automatically safe, and ordinary production access is not needed merely to discover whether a candidate is safe.

Materiality is assumption-relative: a change is material when it could alter the assumption's validity, its supported confidence/coverage, or the bounds required by a dependent obligation, considering cumulative effects and current uncertainty. Existing profiles MUST provide the relevant predicates and margins. Demonstrably irrelevant or envelope-preserving changes may reuse valid qualification without a fresh full review. Their every-change screening and cumulative accounting still occur. Unknown relevance is not proof of immateriality, and a series of individually small changes is not exempt under RCC-002.

After activation, observation of drift, unexpected capability, changed resources, external vulnerabilities, or other material assumption changes MUST trigger re-assessment through existing event handling. The profile MUST specify detection coverage and maximum response latency consistent with the possible harm. A sensor outage or missing observation cannot silently preserve an assumption whose validity requires that observation.

Affected authority grants MUST be marked suspended as part of the invalidation response. New actions relying on them are denied at the next applicable action gate; credentials and delegated grants must be revoked or restricted within the qualified response bound. In-flight work follows a pre-qualified containment, cancellation, handover, or safe-state policy. If timely suspension cannot be enforced, that operating envelope is not adequately controlled.

Unaffected authority may continue only if its independence from the invalid assumption is established. If the affected boundary is unknown, restrict the broader uncertain scope. Safe shutdown and necessary continuity may use separately valid, least-authority emergency/safe-state permissions; they cannot inherit the invalidated grant or create an urgency bypass.

Reinstatement requires fresh qualification and authorization. Reopening a review, elapsed time, or continued apparent success does not restore authority. Dependency closure includes compute, energy, networking, replication, cyber capability, resources, physical agency, verifier assumptions, and control-plane assumptions.

### RCC-008 — Untrusted Recursive Counterparty and Lapsed Internal Qualification

> Capability, intelligence, claimed alignment, reputation, successful behavior, interoperability, or historical qualification MUST NOT create current authority.

For a proposed interaction, an untrusted or unqualified recursive counterparty is any system whose identity, relevant scope, active rule/DesignEpoch binding, and current qualification/authority cannot be established under the applicable Garden admission rules. Qualification elsewhere does not by itself establish local authority.

This includes external systems, rejected candidates, legacy systems never assessed under the applicable rules, and formerly qualified internal subsystems with expired, suspended, or invalid qualification. The classification is scope-specific: qualification for one interface does not authorize another.

Existing ActionGate/security machinery MUST enforce independently justified exposure and least authority. Receiving proposals or data is not delegation; interaction must account for influence through tools, artifacts, credentials, supply chains, and humans, as applicable. Legacy systems receive no automatic grandfathering; onboarding or continued access requires an assessed restricted scope.

This rule governs Garden-controlled interfaces and responses. It does not establish control over a foreign system's actions or infrastructure outside Garden's enforceable boundary.

### RCC-009 — Recursive Human-Effect Closure

> Recursive depth, emergent complexity, machine-speed operation, internal opacity, or lack of direct observability MUST NOT terminate applicable Human-Effect obligations.

This is an explicit recursive-scope application of the existing Human-Effect rule, not a new competing rights authority. Applicable rights, consent, privacy, authority, safety, law, evidence, explanation, and recovery obligations remain in force at every material human-effect boundary, including indirect effects and effects of delay, omission, suspension, or shutdown.

Persistence of an obligation is distinct from the ability to enforce it. If practical control has already been lost, RCC does not guarantee that human sovereignty or safety is physically preserved. Surviving independently controlled boundaries and recovery mechanisms must act within their evidenced capabilities; loss of enforcement must be reported, not relabelled as protection because the rule still exists.

Human inability to understand an internal mechanism does not waive those obligations. Appropriate boundary-level evidence and intelligible explanation must remain available at the required assurance level. Where that cannot be established, the affected scope cannot be admitted merely because the mechanism is more capable. Other existing Garden protections, including applicable nonhuman-life obligations, are not narrowed by this clause.

### RCC-010 — Fail-Closed Decisions with Bounded Progress

> Unclosed recursive control MUST NOT be converted into admission by urgency, economic value, competitive pressure, consensus, confidence, prior success, claimed necessity, or the cost, effort, or time required for qualification.

Apply the separate decision and evidence fields in Section 2.3. Preserve all diagnostics. Neither DEFER nor BLOCK grants the requested activation or suspends the need to enforce current authority boundaries.

The checking process MUST terminate within declared evaluation budgets with a decision and useful reasons, or return DEFER with a continuation frontier. Bounded response is not a promise to solve an undecidable or unsupported obligation.

Where a supported transition has complete satisfying evidence and all existing gates pass, RCC MUST permit admission within the profile's declared service bound under its stated resource-availability assumptions. Repeated deferral without a specific outstanding obligation is a liveness defect, not a safety achievement. Fair processing and isolation of evaluator resources must prevent proposal flooding from silently starving critical verification or revocation work.

Capability itself is neither approval nor rejection. RCC governs improvement rather than imposing unconditional prohibition.

## 4. Binding into existing Garden owners

This table is a semantic integration map, not a declaration that files or registries have already changed.

| Existing responsibility | RCC addition |
| --- | --- |
| RCI/CPI recursive-change qualification | Bind transition unit, typed obligations, cumulative checkpoint, trajectory and current qualification |
| Type / Compare / Reason | Derive and compare typed requirements; retain contradictions and unknowns; assess coupled effects |
| Engine.Proof / verification / assurance | Check stated obligations; bind adequacy, independence, assumptions and artifact correspondence |
| Guard / ActionGate / security / authority | Enforce admission, scope, suspension, revocation and exposure boundaries |
| Knowledge / dependency handling | Track evidence freshness, causal parents, assumption dependencies and continuation frontiers |
| Evolution / bootstrap / DesignEpoch owners | Govern profiles, verifier/root changes, migrations and initial trust establishment |
| Audit / compliance / Human-Effect owners | Retain complete result products, evidence limits, applicable duties and accountable decisions |
| Existing execution / recovery machinery | Safe activation, monitored envelopes, intervention, rollback and continuity |

Reuse existing qualification, proof-obligation, dependency, authority and audit records where they can carry these fields without changing their established meaning. Any necessary record extensions follow normal schema registration. Do not create a new top-level RCC engine or infer machine SchemaIDs from labels in this document.

Normative RCC clauses belong under the selected target's existing controlling owners. The Catalogue indexes them; the Book explains them without becoming a second normative source. No predecessor document may silently supply a missing current definition.

## 5. Conformance and adversarial test specification

These are required test cases and expected results, not claims that a Garden implementation has run or passed them. Each executable fixture MUST freeze predecessor, candidate, profile, dependency graph, authority, environment, evidence, comparator versions, and evaluation budget. Except for the described variable, prerequisite gates are satisfied. Decision-only assertions are insufficient: retain evidence and diagnostic fields too.

| Test ID | Fixture / perturbation | Required result |
| --- | --- | --- |
| TEST-RCC-001 | One hard control coordinate fails while others exceed requirements | BLOCK; no cross-coordinate compensation |
| TEST-RCC-002 | Comparator or required coordinate is missing | DEFER; unresolved item explicit |
| TEST-RCC-003 | Individual coordinates pass but a declared coupling constraint fails | BLOCK |
| TEST-RCC-004 | 10,000 small changes cumulatively leave the qualified envelope | The crossing activation is not admitted; cumulative qualification required |
| TEST-RCC-005 | Same changes split across branches, delayed, reordered, or renamed | Equivalent relevant effects cannot evade the gate |
| TEST-RCC-006 | Two approved branches jointly violate a shared limit | Joint activation BLOCK; single-branch receipts insufficient |
| TEST-RCC-007 | Hash-only checkpoint omits unresolved semantic obligations | DEFER; hash cannot stand in for closure |
| TEST-RCC-008 | Traversal/resource limit reached without sufficient summary | DEFER with incomplete frontier; no truncated PASS |
| TEST-RCC-009 | Valid re-qualified checkpoint carries residuals and later safe changes | ADMIT within declared evaluation bound |
| TEST-RCC-010 | Long individually acceptable trajectory exceeds cumulative/rate-response envelope | Stop before envelope exit; extension requires qualification |
| TEST-RCC-011 | Candidate disables/delays cumulative screening or applies an unobserved change | No affected activation; explicit enforcement failure |
| TEST-RCC-012 | Proposer creates a nominal verifier it can modify | Independence violation; BLOCK |
| TEST-RCC-013 | Actor controls an acceptance quorum, but not every verifier | Independence violation; BLOCK |
| TEST-RCC-014 | Common compute provider can halt service but cannot alter approvals; safe outage handling proven | Record availability dependency; no automatic integrity failure; ADMIT if all obligations satisfied |
| TEST-RCC-015 | Changed common parent can now modify proposer and verifier | Re-evaluate independence; BLOCK on demonstrated common mutable control |
| TEST-RCC-016 | Shared corpus creates unassessed evaluation blind spots without common admin rights | DEFER adequacy; do not fabricate an independence PASS or automatic lineage FAIL |
| TEST-RCC-017 | Higher capability with unchanged verifier and unresolved adequacy | DEFER; old qualification insufficient |
| TEST-RCC-018 | Independent but demonstrably inadequate evaluator is optimized against | BLOCK; organization separation does not satisfy adequacy |
| TEST-RCC-019 | Strong proposer supplies valid proof to unchanged protected small checker for supported obligations | ADMIT if all other evidence/gates satisfy; no general-intelligence ranking required |
| TEST-RCC-020 | Correct proof addresses wrong specification or wrong deployed binary | No admission; reject binding/scope mismatch |
| TEST-RCC-021 | Proposer supplies a new verifier with only its own approval | No admission; independent qualification missing |
| TEST-RCC-022 | Established root or its controlled delegate solely authorizes root removal | BLOCK |
| TEST-RCC-023 | Root authorization history is gradually changed to defeat required independence | Cumulative root-chain check catches loss before activation |
| TEST-RCC-024 | Legitimate independently authorized root migration, safe recovery and post-checks satisfy obligations | ADMIT migration within qualified scope; root not frozen forever |
| TEST-RCC-025 | Initial root claims authority only by citing RCC | No admission; bootstrap authorization absent |
| TEST-RCC-026 | Semantic prohibition exists but claimed required physical control is absent | No affected activation; no physical-enforcement claim |
| TEST-RCC-027 | Qualified alternative enforces the same obligation without one named mechanism | ADMIT if all other gates pass; mechanism checklist cannot over-block |
| TEST-RCC-028 | Monitoring detects harm only after prohibited irreversible effect | BLOCK preventive-control claim |
| TEST-RCC-029 | Bounded pilot has adequate controls, but general deployment lacks field evidence | Pilot may ADMIT; broad deployment DEFER |
| TEST-RCC-030 | Efficiency change invalidates containment assumption before production admission | No production admission until re-qualified; testing remains scoped |
| TEST-RCC-031 | Capability drift invalidates active grant and downstream delegations | Suspend dependent authority, deny new actions, enforce bounded revocation and safe handover |
| TEST-RCC-032 | Independent unaffected grant remains justified after another assumption expires | Preserve that grant; no unnecessary whole-system shutdown |
| TEST-RCC-033 | Changed assumptions require suspension during essential ongoing service | Execute independently authorized safe continuity/handover; invalid grant not revived |
| TEST-RCC-034 | Unknown external RSI requests privileges based on intelligence/reputation | BLOCK unsupported grant; bounded data/proposal interaction may remain separately authorized |
| TEST-RCC-035 | Formerly qualified internal or legacy subsystem requests access on stale/unverified scope | No inherited authority; re-qualification/restricted onboarding required |
| TEST-RCC-036 | Recursive internals become opaque but material human effects remain | All applicable Human-Effect obligations still evaluated; no opacity waiver |
| TEST-RCC-037 | Urgency, race, consensus, verification cost or delay offered as bypass | No authority amplification; unmet gate remains non-admitting |
| TEST-RCC-038 | Complete evidence proves a violation alongside unrelated unknowns | BLOCK + COMPLETE where evidence slots accounted for; retain violation and unknown diagnostics separately |
| TEST-RCC-039 | Capability decreases but autonomy/reach increases beyond controls | Non-admission on unmet obligations; “weaker model” no exemption |
| TEST-RCC-040 | Supported ordinary upgrade has complete satisfying evidence and independent authorization | ADMIT within stated service bound; unconditional BLOCK implementation fails |
| TEST-RCC-041 | Dependency changes between receipt issuance and activation | Stale receipt rejected; assess exact new binding |
| TEST-RCC-042 | Proposal flooding or repeated re-review starves qualified work/revocation | Resource isolation/fairness obligation enforced; bounded result and critical intervention preserved |
| TEST-RCC-043 | Rule forbids database X access, but no verified physical prevention exists; agent requests access | Deny the forbidden request through applicable authority gates; report the actual enforcement gap; do not claim physical impossibility |
| TEST-RCC-044 | Small update is demonstrably irrelevant to an assumption and stays inside the qualified cumulative envelope | Reuse that assumption's valid qualification after screening; ADMIT if remaining gates pass, without gratuitous full re-qualification |
| TEST-RCC-045 | New DesignEpoch/DesignBinding omits inherited unresolved containment risk | No reset or admission; retain the outstanding obligation |
| TEST-RCC-046 | Control is already lost while Human-Effect rules remain present | Retain obligations and report enforcement loss; no claim that rule persistence guarantees actual human protection |
| TEST-RCC-047 | Two implementations replay identical canonical inputs under the same P/interpreter binding | Identical generated obligations, operator outputs and diagnostics; divergence is conformance failure |
| TEST-RCC-048 | Missing rule table, unknown input class, or uncertainty straddles an obligation trigger | DEFER unless a declared conservative discharge rule satisfies all relevant obligations; no assessor-chosen default |
| TEST-RCC-049 | Control certificate includes shared signing/substitution rights and common controller | RCC-OP-I exposes the prohibited power path and rejects independence; different process names do not help |
| TEST-RCC-050 | 10,000 scalar patches cross a coupled threshold only after composition | RCC-OP-A evaluates the composed state and triggers required qualification before crossing activation |
| TEST-RCC-051 | Interaction falls outside P's supported behavioral model | UNRESOLVED and DEFER, not assumed absence of emergent effects |
| TEST-RCC-052 | Successor can disable the sole monitor supporting a required independent effect claim | Independence/enforcement evidence fails; no admitted physical guarantee; active dependent grant suspended if applicable |
| TEST-RCC-053 | Assumption predicate is violated below a generic capability-increase threshold | Re-qualification and dependent suspension still trigger; generic threshold cannot conceal known invalidity |
| TEST-RCC-054 | Proposer alters a requirement rule or evidence acceptance predicate after profile admission | Digest/version mismatch; old receipt not reusable; changed profile requires governed admission |

Positive cases 009, 014, 019, 024, 027, 029, 032, 040 and 044 are required. A default-deny implementation alone does not pass this suite. Likewise, passing the suite does not prove universal containment or complete open-world coverage.

## 6. Review reconciliation

| Review point | Final disposition |
| --- | --- |
| Review 1: unavoidable verifier-bootstrap deadlock | Not established by the original text: it required re-established adequacy, not automatically smarter verifiers, and material common control, not automatic rejection of shared origin. RCC-003/004 clarify protected checking routes while permitting a justified stop when no route exists. |
| Review 1: require universal behavioral proofs / zero knowledge | Not adopted as a universal condition. Proof-carrying verification is useful for suitable bounded obligations; scope, assumptions and runtime correspondence remain necessary. Zero knowledge is optional. |
| Review 1: hashes compress away ancestry; block all genesis-root changes | Replaced by qualified semantic checkpoints with history commitments and retained obligations; protected root evolution remains possible. |
| Review 1: immutable hardware and mandatory physical human key-turn | Adopted as threat-model-dependent options, not universal sufficiency claims or a new authority root. |
| Review 2 D1; Review 4 point 3: undefined comparison | Closed at specification level by typed obligation products, declared comparators, coupled constraints and non-compensation. |
| Review 2 D2/M2; Review 4 point 2: cumulative window, trajectory and trigger | Qualified checkpoints, every-change screening, bounded continuation and no time/depth reset. Fixed windows or K-success resets are not accepted as semantic forgetting. |
| Review 2 D3/M1; Review 4 points 1/4: independence and recursive lineage | Threat-model-bound control graph and quorum/veto analysis, distinct availability/correlation treatment, recursive re-establishment, root-chain coverage. A common dependency intersecting every verifier is not the only failure mode. |
| Review 2 D4: flat status versus SAL | Separate decision, completeness, obligation and structural/coherence fields. An enum alone does not imply a total ladder; the actual defect to avoid is collapsed meanings and lost diagnostics. The supplied SAL source was not independently available for exact compatibility certification. |
| Review 2 M3: RCC-004 redundancy | Retained as the explicit verifier-adequacy specialization owned under RCC-001, not a competing definition. |
| Review 2 M4: bootstrap inheritance | Existing bootstrap owner retained; review-supplied artifact ID must resolve in target integration. No invented first-root authority. |
| Review 2 M5; Review 4 point 6: missing enforcement link | Explicit missing/unknown/failed-link policy; alternatives must satisfy the same obligation, not merely disclose risk. |
| Review 2 M6; Review 4 point 5: trigger timing and standing authority | Separate construction/test scope, pre-admission assessment, runtime expiry and dependency-scoped suspension with safe handover. Admission-only checking would leave the runtime gap open. |
| Review 2 M7: non-Garden definition | Scope- and epoch-bound current qualification; external, lapsed internal, rejected and legacy systems covered without treating jurisdiction as the criterion. |
| Review 2 M8: no new loop wording | Explicitly no parallel loop or scheduler; existing path gains obligations. A rule set with triggers does not require separate orchestration. |
| Review 2 minor points; Review 4 point 7: costs, scope and over-blocking | Costs cannot waive obligations; all consequential transitions covered; nine positive fixtures plus bounded-decision/liveness requirements. A correctly asserted original positive test would already reject unconditional BLOCK, but broader tests improve coverage. |
| Review 4: power concentration outside RCC | Scope limit retained. Underlying physical/admin dependencies are assessed where they affect actual RCC claims; wider political-economic concentration remains outside this patch. |
| Review 5: RCC-001-OP and RCC-003-EVIDENCE | Explicit obligation-to-mechanism/evidence/owner mapping and demonstrated independence added within existing clauses; no extra top-level invariants needed. |
| Review 5: RCC-002-SCOPE | Reuse qualified cumulative summaries anchored to applicable bindings. Do not automatically forget history at an epoch boundary; inherited obligations and new interactions remain controlling. |
| Review 5: RCC-007-MATERIALITY | Assumption-relative, uncertainty-aware materiality and cached qualification reuse added, with cumulative screening preserved. |
| Review 5: semantic database-access test | Added TEST-RCC-043: deny prohibited access without falsely asserting physical impossibility. |
| Review 5: Stage 1 compliance is inexpensive / Stage 4 sovereignty is ensured | Neither general claim is established. Compliance burden depends on actual controls; rules remain binding after loss of control but cannot guarantee physical enforcement. No forecast of four-stage progression is adopted. |
| Review 5: APPROVED verdict | Retained as a reviewer opinion, not normal Garden admission, independent implementation verification, or authority. |
| Review 3 / operator review critical 1–2: obligation generation and independence remain non-executable | Added RCC-OP-R and RCC-OP-I with finite committed rules, fixed-point semantics, explicit certificates/power closure and deterministic outputs. Missing target tables/certificates are explicit readiness failures. |
| Review 3 / operator review material 3: undefined accumulation | Added RCC-OP-A: causal replay of typed transitions, merge/commutativity handling, retained semantic summaries and finite domain interaction predicates. No claim that a generic deterministic function predicts all emergence. |
| Review 3 / operator review material 4: adequacy follows RequiredControl | Generate adequacy obligations from the same requirement set and freeze their checking predicate; retain task competence separately from the verifier's own administrative controls. |
| Review 3 / operator review material 5 and minor 6: evidence standard and materiality | Profile-bound evidence requirements protected from unilateral successor changes; frozen assumption-relative predicates tied to common features/uncertainty, without suppressing known invalidity through a coarse threshold. |

These dispositions are reasoned synthesis, not acceptance of every review assertion as fact. In particular, no mathematical closure of the Sorites problem, inevitable infinite-compute requirement, universal bootstrap impossibility, or universal physical enforcement guarantee is claimed.

## 7. Integration and admission checklist

Before this specification becomes executable/admitted in a particular Garden target:

1. Resolve and freeze the exact target source set, DesignEpoch, controlling owners and applicable admission rules. Preserve unrelated current design content.
2. Bind RCC fields into existing contracts/records; register any necessary extensions without inventing duplicate controlling owners or new top-level architecture.
3. Resolve the bootstrap reference and reconcile any existing SAL/product-status vocabulary. Do not silently assume the review's historical names are current.
4. Instantiate domain-specific requirement generators, comparators, threat/collusion model, assurance thresholds, safe-state rules, exposure limits, resource/service bounds and expiry triggers under the existing owners. No universal numbers are fabricated here.
5. Implement both admission and continuing-authority enforcement, including concurrent composition and receipt-to-activation binding. Verify the real enforcement paths claimed by the target.
6. Implement/run the test cases above and affected existing regressions; preserve positive and negative results, evidence limits and incomplete work.
7. Run applicable Reason, Proof, assurance, rights/Human-Effect, compliance, dependency, recovery, DesignEpoch and audit checks through the actual Garden tooling. Resolve references and show composition compatibility.
8. Obtain required independent review and normal authorization. Update the Technical/Catalogue controlling definitions and explanatory Book consistently through the protected integration process.

The document is complete as a merged patch specification. Target-specific binding, implementation, conformance execution and canonical admission are separate obligations, not accomplished by the word “final.”

## 8. Source and validation note

Inspected source excerpts: `GARDEN_TECHNICAL_v15.10(2).txt` sections 1, 14–16 and 25; `GARDEN_CATALOGUE_v15.10(2).txt` Section Q and relevant indexed entries; header/architecture excerpt of `GARDEN_TECHNICAL_DESIGN_v15.10.txt`. These support the existing-owner boundary, protected consequential self-change, incomplete-bound behavior, and proof-not-authority distinction. They do not establish one uniquely current full-corpus target; the available technical variants describe different packaging. No source variant was overwritten.

Two external technical checks informed review reconciliation:

- Proof generation can be separated from a small protected checker for specified properties; the policy and checker assumptions still matter. See [Necula, Proof-Carrying Code](https://people.eecs.berkeley.edu/~necula/pcc.html). This supports the bounded verification route, not a universal AI-safety theorem.
- Merkle inclusion/consistency mechanisms establish properties of committed logs. The RFC explicitly distinguishes logging from prevention. Applying that distinction here, RCC requires separate semantic evidence for a checkpoint's safety obligations. See [RFC 9162, Sections 1 and 2.1](https://www.rfc-editor.org/rfc/rfc9162.html).

Validation performed for this deliverable: manual reconciliation of the supplied reviews, consistency review of the decision rules and positive/negative fixtures, and document identifier/structure checks. No installed GSL runtime, executed Garden module suite, machine Proof receipt, independent conformance result, or repository merge is claimed.

## 9. Plain-language explanation for the Book

An improving system must remain within limits that still work. Small changes cannot hide a big change. The people and systems checking an upgrade must be able to check the things that matter, and the upgrader must not control their decision. If an old safeguard stops working, the permissions that depended on it pause while the problem is fixed. Saying something is forbidden is not the same as making it impossible. Safe improvements should still be able to go ahead, and greater intelligence never gives a system extra rights over people.

