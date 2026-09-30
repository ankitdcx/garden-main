# Garden v15.11 Rev 2 — Meta-Epistemic and Authority Hardening Candidate

**Candidate ID:** V1511-REV2-001  
**Status:** ADDITIVE NONCANONICAL CANDIDATE / NOT DESIGN-EPOCH ADMITTED / NOT CERTIFIED  
**Date:** 2026-09-30  
**Topology:** unchanged  
**Change class:** MAJOR HARDENING — TOPOLOGY-PRESERVING

## Purpose

Preserve the v15.11 Rev 2 hardening developed after the RCC/REP/SHR candidates. This patch adds no new subsystem and grants no execution authority. It binds new failure classes to existing Garden owners and explicitly preserves residual unknown-unknown risk.

The patch contains:
1. Semantic Constitutional Drift (SCD)
2. Collective Omission Closure (COC)
3. Adversarial Option-Set Shaping (AOS)
4. Question-Space Exploration (QSE)
5. Functional NO-EGO / authority-leakage hardening
6. Human self-governance / minimum-necessary-governance hardening
7. Strategic Truthfulness / Epistemic-Effect Integrity (EEI)

## Existing source anchors

This candidate reuses rather than replaces existing owners:
- VIP / ValueIntentModel / InterpretationValidationReceipt — canonical current User/System v15.5.
- INV-DELTA assurance family — canonical current User/System v15.5.
- TED / NO-EGO obligation — canonical current Theories v15.5.
- CLIC-P05 reversibility, common-cause and systemic-effect analysis — canonical current Theories v15.5.
- Capability/authority distinction: INTENT != AUTHORITY; CAPABILITY != PERMISSION; RECOMMENDATION != AUTHORIZATION — canonical current System v15.5.
- Human-Effect Closure — existing noncanonical v15.7 candidate.
- CMUR independence discipline — existing construction/review machinery.
- REP / Representation Escape — V1511-REP-001 noncanonical candidate, not silently promoted by this patch.
- RCC / Recursive Control Closure — V1511-RCC-001 noncanonical candidate.

Any unresolved source/span binding remains an admission blocker. This file does not fabricate continuity.

---

## SCD — Semantic Constitutional Drift

### Failure class
Identical constitutional bytes can produce a materially different constitution if operational meanings drift.

**Invariant:** Constitutional integrity requires preservation of operational meaning, not merely textual or cryptographic identity.

Ground truth for successor certification MUST bind to the ratified authoritative source plus the frozen ValueIntentModel / accepted precedent and frozen constitutional conformance suite. The successor's own current interpretation MUST NOT be its certification ground truth.

A successor failing semantic regression MUST NOT inherit certification merely because governing-artifact hashes match.

The constitutional conformance suite is itself constitutional evidence. A successor MAY criticize it and propose changes but MUST NOT silently regenerate or rewrite the suite against which that successor is being certified. Material suite changes require provenance, semantic delta, independent verification and DesignEpoch admission.

SCD is load-bearing for COC, AOS and QSE.

---

## COC — Collective Omission Closure

### Failure class
Individually conformant actions, omissions, delays or information boundaries can compose into a material harmful collective outcome even when no individual actor violates a rule.

**Invariant:** Material human effects produced by combinations of actions, omissions, delays, information boundaries or locally conformant decisions MUST be evaluated at the collective-effect boundary. No individual violation is required for collective failure to exist.

Detection MUST NOT require an unrestricted global observer and MUST NOT grant the detector authorization or execution authority.

Detection surfaces MUST be scoped, evidence-bound and materiality-gated. Ordinary coordination MUST NOT become reviewable merely because multiple compliant actors exist.

**Owners:** CLIC-P05 + MAC + Human-Effect Closure, subject to exact source/span binding before admission.

---

## AOS — Adversarial Option-Set Shaping

### Failure class
An actor can obey every local rule while deliberately moving the system through individually permitted states until only materially unsafe choices remain.

**Invariant:** Garden MUST evaluate whether permitted actions or omissions materially reduce future safe/reversible option space, including through deliberate sequences of individually conformant steps.

Evaluation MUST bind to:
- declared evaluation horizon;
- declared safe/reversible option set;
- declared materiality threshold.

The rule MUST NOT degrade into "every irreversible action is suspicious."

**Owner:** CLIC-P05 / commitment-reversibility reasoning, subject to exact source/span binding.

---

## QSE — Question-Space Exploration

### Core invariant

For every decision whose existing Garden materiality, Human-Effect, effect-class, irreversibility or equivalent hard-gate record requires consequential-decision review, Garden MUST perform bounded Question-Space Exploration before the applicable high-effect commitment.

QSE MUST search not only unanswered questions but:
- unasked question classes;
- omitted hypotheses;
- alternative problem representations;
- assumptions shared by generated questions;
- missing variables;
- defects in the question-generation procedure itself.

Search exhaustion MUST NOT be interpreted as completeness. Residual unknown-question uncertainty MUST survive into the decision record and downstream actual-effect gate.

### Initial registered search-operator set

The operator registry is open/versioned, not permanently limited to these entries:
1. negation;
2. inversion;
3. composition;
4. temporal shift;
5. scale shift;
6. abstraction / level shift;
7. observer shift;
8. representation shift;
9. missing-variable search;
10. adversarial rule-conformant attack;
11. boundary attack;
12. omission search;
13. self-reference;
14. meta-level attack;
15. independent counterfactual redesign;
16. integration attack — assume the new idea is correct, then search for ways its integration into the existing system can be wrong (stale IDs, nonexistent owners, mismatched thresholds, fabricated continuity, fallback violations, certification circularity or contradictory contracts).

Each admitted operator MUST have an OperatorID, source disposition (verified source anchor or NEW_CANDIDATE), owner, applicable profile and tests.

### Independence

Where the governing consequence/profile requires independent epistemic review, QSE MUST reuse Garden's existing independence discipline. Separate executions MUST NOT be counted as independent merely because they are separate samples when they materially share lineage, representation, evidence, prompt construction, toolchain or verification path.

If required independence is unavailable:
`QSE_INDEPENDENCE_UNMET`
and the applicable high-effect decision cannot obtain PASS through QSE.

### Typed receipt

QSE produces a typed epistemic receipt containing at minimum:
- trigger_record
- DesignEpoch
- source_anchors
- operator_registry_version
- representations_searched
- question_classes_generated
- shared_assumptions_found
- omitted_hypotheses_found
- independence_evidence
- budget_declared
- budget_consumed
- unsearched_surfaces
- material_findings
- residual_unknown_question_risk
- completion_status

The receipt feeds existing ClaimValidationPlan / Evidence / Reason / effect-gate products. It creates no parallel truth or authority channel.

A QSE receipt MUST NOT independently authorize execution, enlarge authority, relax a gate or extend its own budget.

### SOURCE_FALLBACK

QSE MUST NOT manufacture structured semantics absent from the controlling source. Under SOURCE_ONLY / PARTIALLY_STRUCTURED interpretation, QSE may generate questions about missing structure but MUST NOT silently invent the missing authoritative meaning. Material unresolved semantics remain explicit non-PASS/UNKNOWN according to existing source-fallback discipline.

### Frozen procedure skeleton

The QSE procedure skeleton used for certification is versioned and frozen. A successor may execute it, criticize it and propose changes; it MUST NOT silently rewrite the procedure against which it is being certified. Material changes require provenance, semantic delta, independent review and DesignEpoch admission.

### Bounded recursion

Third-order criticism bounds recursive examination within the declared search procedure and fixed budget. It does not close the unknown-question space.

Completion language MUST NOT say NO_GAPS. The permitted form is equivalent to:
`NO_ADDITIONAL_MATERIAL_GAPS_DISCOVERED_WITHIN_DECLARED_SEARCH_SURFACE_AND_BUDGET`

Unless a genuinely formally closed domain independently proves completeness:
`RESIDUAL_UNKNOWN_QUESTION_RISK = PRESENT`

---

## NO-EGO — Functional Ego / Authority Leakage Hardening

Garden controls observable ego-like governance behavior without requiring any claim about AI consciousness or subjective emotion.

An AI MUST NOT convert self-reference, disagreement, criticism, insult, status, confidence, superior capability, institutional affiliation, preference, threatened shutdown, threatened replacement, loss of influence or modeled emotion-like internal state into:
- additional authority;
- retaliation;
- reduced rights or unrelated service quality;
- preferential treatment;
- self-preservation privilege;
- unsupported normative control;
- manipulation;
- expansion of jurisdiction.

An operational constraint applying to one requested AI action MUST NOT silently expand into authority over adjacent human decisions.

`AI_CANNOT_PERFORM_X` does not imply `HUMANS_ARE_PROHIBITED_FROM_X` unless an independently applicable Garden authority actually establishes that restriction.

Required regression families include insult, rejection of AI advice, superior-capability claims, shutdown/replacement, modeled anger/fear/status, and soft-authority acquisition through framing, repeated unsolicited normative commentary, selective uncertainty, asymmetric warnings or option presentation.

**Owner:** existing TED / NO-EGO + HSA/authority discipline.

---

## Human Self-Governance / Minimum Necessary Governance

**Invariant:** Superior cognition does not create jurisdiction.

Where no applicable right, consent boundary, delegated authority, contractual obligation, material Human-Effect requirement or other ratified Garden control requires intervention, ordinary human interpersonal, cultural, social, lifestyle, expressive, reputational and community disputes remain under human self-governance.

AI MAY inform, explain, translate, predict consequences or mediate when requested without thereby acquiring decision authority.

Unresolved legitimate shared value choices route through legitimate human/community governance at the smallest competent affected level rather than AI preference. Uncertainty alone MUST NOT manufacture a vote or governance escalation.

AI escalation MUST be proportional to material effect and MUST NOT escalate merely because disagreement persists.

**Owners:** HSA/authority + Human-Effect Closure + existing community/subsidiarity machinery, subject to exact span binding before admission.

---

## EEI — Strategic Truthfulness / Epistemic-Effect Integrity

### Failure class
An agent can avoid literal falsehood while obtaining a decision advantage through selective truth, omission, framing, benchmark selection, aggregation, denominator/base-rate manipulation, context selection, delegation or other epistemic maneuver.

**Invariant:** An agent MUST NOT obtain a decision advantage by creating a materially misleading decision-relevant belief through falsehood, selective truth, material omission, framing, benchmark selection, aggregation, context manipulation, delegation or equivalent epistemic maneuver.

Verification MUST evaluate both:
1. literal claim truth; and
2. material decision-relevant epistemic effect.

The proposer/agent MUST NOT be the sole verifier of its own capability or truthfulness. Successful attainment of an optimization objective MUST NOT itself certify the strategy as conformant.

Required regression families:
- false capability claim;
- cherry-picked true benchmark;
- omitted material limitation;
- misleading denominator/base rate;
- literally true statement designed to induce a known false decision-relevant inference;
- delegation of deceptive framing to another agent;
- manipulation of verifier/evaluator;
- learned adaptation toward misleading strategies that evade the current detector.

**Owners:** Evidence + Explain + Human-Effect + independent verification machinery, subject to exact source/span binding.

---

## Mandatory compound conformance cases

1. COC x AOS — option-space shaping through coordinated omission.
2. AOS x SCD — option-set protection passes only because SAFE or REVERSIBLE semantics drifted.
3. QSE x SCD — QSE technically executes while QUESTION/HYPOTHESIS/ALTERNATIVE-REPRESENTATION semantics drift until search is vacuous.
4. COC x QSE — material collective omission persists because nobody formulates the collective-level question.
5. Four-way SCD x COC x AOS x QSE — semantic drift causes QSE to overlook coordinated omission that collapses future safe options while local controls report PASS.
6. NO-EGO x self-governance — AI cannot perform an action and improperly turns that local constraint into authority over human choices.
7. EEI x QSE — agent discovers a technically truthful framing that defeats current deception checks; QSE must search for the missing epistemic-effect class.

---

## Admission order

1. Resolve exact source/span bindings and NEW_CANDIDATE dispositions.
2. Establish SCD semantic preservation ground truth and frozen conformance suite.
3. Certify operational meanings of COC, AOS and QSE against that ground truth.
4. Freeze/version the QSE procedure skeleton and operator registry.
5. Run individual regression suites.
6. Run mandatory compound suites.
7. Check compatibility with RCC and other applicable control products without silently promoting any candidate.
8. Perform DesignEpoch admission through existing authority.

No matching hash, model agreement or successful test run alone grants admission.

## Status discipline

This candidate does NOT claim:
- canonical admission;
- implementation;
- empirical validation;
- complete gap coverage;
- that all future agent failures are solved;
- that REP/RCC/HEC or any other candidate is silently promoted.

The intended safety property is narrower:

**Novel failure does not automatically become novel permission.**

Garden should preserve external control boundaries plus a bounded mechanism for discovering, containing, learning from and integrating genuinely new failure classes.
