# TRACE — Garden v15.7 candidate
Patch: GARDEN-v15.7-TRACE-01
Revision: 3, consolidated with the four final accepted clarifications.
Status: NON_CANONICAL_CANDIDATE_PENDING_RECONCILIATION_AND_ADMISSION.
TRACE is a memorable name, not an acronym.

## Scope and lineage
TRACE v0.2 is a versioned experimental runtime candidate, not merely a pattern, a new foundation model, or demonstrated AGI. This increment is additive to completed v15.6. It does not modify v15.6's parallel build or canonical/current. Supersede any earlier conversational v15.6 assignment for TRACE with this v15.7 target; no TRACE entry was found in the v15.6 main index at registration base.

This specification includes requirements not yet implemented in v0.2. Architectural impact is minor; implementation and assurance impact is moderate. Formal change routing remains subject to reconciliation. No new top-level engine, authority source or canonical SchemaID is registered here.

## 1. Existing responsibilities and mandatory action gate
Map planner to Reason; dispatcher to authorization/execution; memory to knowledge/provenance; evaluator to verification; receipts to audit. Exact FunctionContract owners and schema equivalents remain pending source reconciliation.
Run: propose → authorize → execute → observe → evaluate → retry or finish.
Every tool invocation passes through Garden's action gate before dispatch. Proposals, evaluator acceptance and retrieved content cannot grant authority, alter policy or register tools.
Recheck relevant authority at the commitment boundary under the existing action contract. Failed recheck after preparation but before commitment requires abort and prohibits dispatch. Release reservations through the abort contract. If commitment may already have occurred, record uncertain completion and reconcile; never claim successful abort without evidence.

## 2. Fixed budget and recovery
Each run receives an externally authorized immutable grant for applicable attempts, calls, tokens, cost and elapsed time. Planner, evaluator and feedback loop cannot enlarge, reset or self-renew it. Failures consume applicable budgets; retries share the grant.
Exhaustion terminates further ordinary dispatch with BUDGET_EXHAUSTED. Further ordinary work requires a separately authorized run linked to its predecessor.
Abort, uncertain-effect reconciliation and necessary containment draw on a separately authorized, bounded recovery allowance. They cannot use it for ordinary retries. In-flight effects follow existing recovery/containment contracts rather than being abandoned. Exhaustion or failure of recovery follows those contracts and records unresolved effects honestly.

## 3. Role independence
For consequential use apply existing Generator/Reviewer/Verifier separation through protected identities, permissions and appropriate trust boundaries. The proposer cannot modify evaluators, criteria, evidence requirements or verification records. Separate processes alone do not establish independence.
Record shared models, hosts and dependencies that may cause correlated errors. Any role sharing requires an explicit allowance in the applicable assurance profile. Shared-role experiments cannot claim independent verification.

## 4. Evidence and dependence
References resolve to identified observations with provenance; current-run requirements reject foreign-run or unknown references. Required evidence tools are operator/policy configured. A correct guess cannot satisfy required tool evidence.
Reject repeated references used to inflate independent support. Allow an observation to support multiple claims through explicit claim-to-evidence links.
The protected evaluator or evidence service determines dependence from recorded provenance and derivation links, not the citer's assertion. Missing provenance means dependence UNKNOWN, not independent. Shared IDs are only one detectable dependence.
Record required/provided evidence and each check result. Presence/type is distinct from semantic support, which the task criterion must check where required. TRACE cannot waive requirements; any externally authorized exception is explicit and policy-bound.

## 5. Mutation and record protection
Deep-copy supported structures or use immutable representations to prevent nested callback mutation of observations, evaluation inputs and recorded answers. This is accidental-mutation protection, not malicious-code isolation.
Committed observations, evaluations and receipts are append-only under existing privacy/retention/deletion rules. Corrections create linked superseding records, preserving originals subject to those rules.
Storage permissions prevent ordinary runtime rewriting. Content addressing detects changes against protected references; it does not prevent overwrite/deletion. Stronger authenticity or tamper-resistance claims require independent controls and evidence.

## 6. Receipts, environment and trust manifest
Extend equivalent existing schemas after reconciliation. Receipt content includes:
- Run/attempt IDs, initiating principal, executing/evaluating identities, privacy-preserving where appropriate.
- DesignEpoch, runtime version/source hash, task hash, policy identity/configuration/hash, evaluator identity/version.
- Observation and evaluated-answer hashes, outcome, exact criterion/scope, failure reason, uncertainty and limitations.
- Event time, clock basis/uncertainty where relevant, prior_attempt_receipt_id.
- Initial grant, budget consumed/remaining, separate recovery allowance and consumption.
- Required/provided evidence, claim links/dependence, per-requirement results and authorized exceptions.
- Relevant authorization-decision references.
- supersedes_receipt_id and correction reason, distinct from the prior-attempt relation.
- Environment manifest digest: relevant OS/runtime/tool versions, hardware class, execution configuration, and network conditions/external-service identities affecting the claim. Mark unavailable information explicitly.
A versioned admission manifest declares trusted components, compromise assumptions and which controls survive TRACE compromise. Receipts reference its digest.
Identify environment attestation source and verification status. Runtime self-report does not establish integrity against compromised TRACE. Claims requiring external attestation remain unestablished without it. Hashes identify content, not correctness or authenticity; recording environment does not guarantee reproducibility.

## 7. Outcomes and uncertainty
Keep execution and evaluation status separate:
- Optional evaluator absent: ANSWER_UNVERIFIED.
- Required evaluator absent: BLOCKED; no verified completion or dependent consequential action.
- Rejection: recorded, retry only within budget.
- Evaluator failure/inability to finish: EVALUATION_INCOMPLETE, never default acceptance.
- Acceptance: scoped to the specified criterion.
- Budget exhausted: terminal BUDGET_EXHAUSTED for ordinary execution.
Uncertainty accompanies evaluation. Where a probability is meaningful, bind method, assumptions and calibration evidence, or mark uncalibrated. Acceptance with uncertainty requires externally defined policy permission. Confidence never grants action authority.

## 8. Reconciliation against completed v15.6
Pin completed v15.6 source identity and the proposed v15.7 DesignEpoch before qualification; neither is invented at registration.
Map EVERY requirement to contracts, schemas, invariants and tests, with status EXISTING_EQUIVALENT, EXTENSION_REQUIRED, NEW_CONTRACT_REQUIRED or UNRESOLVED. Mandatory unresolved requirements block affected admission.
Run automated schema/reference/duplicate checks and semantic review of authority, overlap, dependencies and whole-source closure under the applicable Garden process, including GSL-COMPARE where required.
Record conflicts, decisions and outstanding obligations. Prefer reuse and NO_CHANGE where equivalent. Any actual replacement requires an explicit amendment; do not silently supersede v15.6.
Registration is not a reconciliation result, canonical admission or promotion.

## 9. Admission evidence
Fresh Garden-adapter runtime and enforcement tests bind to the admission DesignEpoch and hash of the exact tested configuration. Configuration changes require explicit evidence-reuse/revalidation assessment.
Cover budget reset/self-extension/exhaustion and recovery separation; absent/failed evaluator; evaluator/policy modification; nested mutation/record rewriting; multi-claim citations/inflated counts/unknown dependence; direct-dispatch bypass/revoked authority/prepare-abort/uncertain commitment; receipt completeness/chaining/environment trust/uncertainty.
Assess enforcement through code review, trust-boundary analysis and adversarial integration tests; record method and coverage. Bounded tests do not establish universal absence of bypasses.
Controls only inside TRACE assume its correct behavior. A compromised TRACE may bypass them; independently enforced Garden gates, protected credentials and storage may survive. Document and test that boundary rather than assuming all protections fail or survive.
Separate runtime-correctness, enforcement-assurance and live-model-capability receipts. Capability receipts bind model/environment/evaluation configuration; runtime tests do not establish intelligence.

## Evidence state and next work
Historical TRACE v0.2 package records 14 passing runtime/mock-adapter tests; the prior turn inspected that record. This registration does not rerun them, certify revision 3 or claim live-model performance.
No source runtime is activated/imported by this tracking change. Artifact hashes can identify the available package without treating its historical receipts as admission evidence.
Next bounded work: reconcile against completed v15.6, then implement residual requirements and run fresh adapter/enforcement qualification under the bound candidate epoch. Required independent review and canonical promotion remain separate.
