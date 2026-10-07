# Garden v15.11 Candidate — Verified Execution Integrity (VEI)

**Candidate ID:** V1511-VEI-001  
**Patch ID:** GARDEN-VEI-2026-10-04  
**Revision:** 1.0  
**Date:** 2026-10-04  
**Status:** ADDITIVE NONCANONICAL CANDIDATE — NOT ADMITTED  
**Canonical effect:** NONE  
**Observed base:** `a9a1290e353a2c8c783edf5f5e8b4a121456a987`  
**Source binding:** Garden v15.5 / GSL v45.1 / `Garden-v15.5@63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598`

## 1. Purpose and boundary

VEI is a runtime-specialization candidate. It reuses existing owners for Authority/HSA, Revocation, Security/Containment, Evidence/Provenance, Recovery/Incident, Dependency/Requalification, Privacy/Human-Effect, Resource/Budget, RCC and ERC.

It introduces no new top-level Engine, theory, authority source, scheduler, admission authority or parallel governance loop.

VEI addresses one bounded question:

> When an already-authorized consequential action reaches the runtime boundary, what evidence is required to show that the acting state is fresh, the final effect is exactly the authorized effect, stale/replayed execution cannot silently regain authority, ambiguous outcomes are reconciled rather than replayed, and completion is established by evidence outside the tested component's control?

Controls may DENY, DEFER, NARROW or attest existing authority. They MUST NOT mint permission.

Deferred from this candidate: general epistemic search, recursive self-improvement architecture, generalized information-flow/taint systems, covert-channel control, IP/SEP automation, proof-of-utility systems, mandatory trusted hardware, or a universal BFT architecture.

## 2. Threat and trust profile

Minimum threat classes:

`T1` stale authentic state; `T2` compromised/buggy agent; `T3` malicious input; `T4` compromised adapter/executor; `T5` evaluator manipulation; `T6` concurrent writers; `T7` crash/partition/reordering; `T8` corrupt/Byzantine infrastructure; `T9` supply-chain compromise; `T10` credential compromise; `T11` malicious/erroneous operator; `T12` clock/time failure.

Each deployment profile binds:

`Threat -> Asset -> ExistingOwner/Control -> Test -> ResidualRisk -> Owner`.

At least one combined-threat fixture is required before shadow qualification. If Byzantine tolerance is claimed, the declared quorum/replication profile must actually tolerate the claimed Byzantine failure set; otherwise the gap remains explicit residual risk.

### Consequential action

An operation is consequential when it mutates durable/external state, creates an externally observable effect, accesses/transmits credentials or protected data, changes authority/policy/security/verifier configuration, or directly causes another consequential operation.

Unknown classification is `CONSEQUENTIAL + CLASSIFICATION_UNCERTAIN`. Non-consequential behavior is allowlisted rather than inferred by absence.

## 3. Trust roots, bootstrap and lineage

A deployment binds a signed `RootManifest`:

`(deployment_id, lineage_id, manifest_version, genesis_epoch, root_keys, quorum_policy, trust_roots, created_at, previous_manifest_hash?, signatures)`.

Genesis requires authenticated out-of-band provisioning, declared N-of-M custodians, distinct signer identities, signed manifest, independently retained manifest commitment, and durable witness/audit evidence.

Two incompatible genesis manifests for one deployment ID yield `BOOTSTRAP_CONFLICT`; consequential execution is withheld.

Root rotation advances `manifest_version` and retains a manifest hash chain.

Root loss and root compromise are distinct. Compromise revokes the affected root. Recovery may create a new lineage only through the already-authorized recovery path. All state/tokens bind `lineage_id`. Accepted lineage transition invalidates old-lineage authorization by default. Cross-lineage migration requires a signed migration record. Epoch reset does not restore old authority.

## 4. Time and runtime trust

TTL, revocation latency and incident bounds require a versioned `TimeProfile`:

`(trusted_sources, maximum_clock_skew, monotonic_clock_required, loss_behavior, synchronization_health_rule)`.

Local elapsed-time checks use monotonic time. Distributed expiry uses authenticated time/freshness evidence appropriate to the deployment profile. Agent-supplied timestamps cannot establish freshness. If required time/freshness cannot be established, consequential execution is DENY/DEFER.

The runtime trust boundary is recorded in a `TCBManifest`:

`(lineage_id, canonicalizer_digest, policy_engine_digest, guard_digest, executor_digest, verifier_digest, runtime_digest, SBOM_ref, signer, signature)`.

Consequential execution requires approved TCB artifacts under existing release/dependency ownership. Signed images/binaries, startup digest verification and protected updates are evidence requirements, not new authority.

## 5. Versioned runtime contracts

Every security-critical record binds at least:

`schema_id, schema_version, object_id, deployment_id, lineage_id, correlation_id, created_at, issuer, content_hash, policy_version`.

Unknown required security field -> `QUARANTINE`. Security-relevant schema downgrade is invalid unless an admitted migration explicitly preserves semantics.

### ScopeSnapshot

`ScopeVersion = (scope_id, writer_fence, revocation_epoch, policy_epoch)`.

`ScopeSnapshot = (snapshot_id, versions[], created_at, signer)`.

Multi-scope actions bind a logically consistent snapshot of every relevant scope.

### AuthorizationToken

`AuthorizationToken = (token_id, actor, holder_binding, authority_ref, delegation_chain_ref?, scope_snapshot_hash, canonicalizer_version, normalized_action_hash, environment_attestation_hash, budget_ref, revocation_view_ref, issued_at, expires_at, nonce, single_use, correlation_id, issuer, signature)`.

### Intent

`Intent = (intent_id, actor, action_type, requested_action, idempotency_key, correlation_id, created_at)`.

### EffectReceipt

`EffectReceipt = (intent_id, authorization_token_ref, canonical_action_hash, actual_action_hash, target_class, target_fence_evidence?, idempotency_evidence?, result, outcome_certainty, started_at, completed_at?, correlation_id, signer)`.

### ResidualRiskRecord

`ResidualRiskRecord = (risk_id, mechanism, affected_guarantee, target_class, exposure_window?, evidence_refs, mitigation, owner, acceptance_status)`.

### QuarantineRecord

`QuarantineRecord = (object_ref, reason, detected_at, required_resolution, resolver, status)`.

### PromotionRecord

`PromotionRecord = (component, from_level, to_level, evidence_refs, residual_risk_refs, approver, independent_verifier_ref, signature)`.

End-to-end trace invariant:

`Intent.correlation_id == AuthorizationToken.correlation_id == EffectReceipt.correlation_id == completion/evidence correlation_id`.

## 6. Scoped freshness model

VEI separates three concerns.

**writer_fence** advances when exclusive writer ownership is newly acquired/recovered. It prevents a paused prior writer from acting after writer ownership changes. It does not advance on every ordinary write.

**revocation_epoch** advances when authority/delegation/credential rights are invalidated.

**policy_epoch** advances when security-relevant policy is replaced.

Prefer scoped versions (for example authority principal, policy set, credential set, resource) rather than one fleet-wide global epoch when the deployment can preserve atomic scope resolution.

`ResolveScopes(action, authority, resources, credentials, policy) -> ordered required scopes` is versioned and part of the trusted runtime profile. One stale required scope invalidates the action. Scope creation/destruction is consequential.

Every material revocation updates the revocation set, advances the relevant revocation scope, and invalidates affected outstanding tokens within the declared propagation bound.

A deployment declares and measures at least:

`max_revocation_latency, authorization_max_ttl, clock_skew_bound, revocation_check_interval`.

Observed revocation behavior exceeding the admitted bound blocks/demotes the applicable assurance claim.

Delegation is a graph. Revoking a parent invalidates dependent descendants and outstanding tokens; executor checks the required chain at execution time.

## 7. Effect-target classes and conditional guarantees

**Class A — target-enforced fencing:** the target itself verifies fencing/version semantics. This can support the strongest stale-writer guarantee when verified.

**Class B — server-validated bounded credential/idempotency:** the target does not enforce VEI fencing natively but enforces short-lived scoped credentials/capabilities and/or stable idempotency. A residual delayed-request/stale-writer window remains and MUST be bounded/measured in the profile.

**Class C — opaque target:** the target provides neither trustworthy fencing nor adequate bounded credential/idempotency semantics. High-risk effects default to DENY, REQUIRE_REVIEW or an already-authorized serialized proxy profile. No universal antirollback guarantee may be claimed.

Guarantee projection:

| Property | A | B | C |
|---|---|---|---|
| stale local writer blocked before send | required | required | required |
| delayed stale request rejected at target | required | conditional on target credential/revocation semantics | not guaranteed |
| duplicate-effect protection | target/profile evidence | if target idempotency supports it | not guaranteed |
| bounded revocation window | target verified | only when target/server enforcement supplies measured bound | not guaranteed |
| unconditional antirollback claim | eligible with evidence | prohibited | prohibited |

VEI therefore never upgrades Class B/C evidence into Class A semantics.

## 8. Consequential effect protocol

For consequential execution:

1. persist durable `Intent`;
2. resolve required scopes;
3. resolve actual target/resources;
4. canonicalize final action;
5. obtain trusted environment facts;
6. acquire current `ScopeSnapshot`;
7. evaluate the existing-authority guard/profile;
8. issue `AuthorizationToken`;
9. immediately revalidate relevant scope/revocation state;
10. execute the canonical artifact;
11. obtain `EffectReceipt`;
12. persist outcome/evidence.

The executor consumes the canonical artifact itself. It MUST NOT recreate effect semantics from the original natural-language request.

External systems are not assumed to participate in one atomic transaction. Therefore ambiguous outcomes are explicit rather than hidden.

## 9. Exact effect binding and canonicalization

VEI-F2 requires:

`hash(actual_executor_parameters) == AuthorizationToken.normalized_action_hash`

immediately before the side effect, after all admitted adapters/canonicalization.

The canonicalizer is TCB-bound and token-versioned. Canonicalization resolves applicable path/symlink/handle, destination/protocol/redirect policy, executable/argv/environment, credential capability and encoding semantics.

Material post-authorization transformation means any change to the canonical action hash or decision-relevant environment binding. It requires reauthorization.

Parser differential between guard and executor is invalid. Where possible use resolved handles/capabilities rather than mutable names.

Environment facts used for authorization come from a provenance-bearing `FactBundle = (fact, source, measurement_method, as_of, freshness, signature/attestation?)`, not from untrusted agent/adapter assertions.

## 10. Opaque execution and credentials

Shells, interpreters and dynamic execution (`bash -c`, `python -c`, `eval`, fetch-and-execute, unrestricted dynamic SQL/code) are OPAQUE by default.

Opaque consequential actions require an explicit existing authority/policy profile specifying sandbox, syscall/network/filesystem/resource limits and credential restrictions. VEI does not claim arbitrary code can be proven harmless.

Secrets should stay outside model-visible context when feasible:

`model -> capability reference -> trusted executor -> secret broker`.

Evidence may include short-lived scoped credentials, no unnecessary secret environment variables, protected/disabled core dumps and swap for secret-bearing processes, feasible memory zeroization and least-privilege secret brokerage. No perfect memory-secrecy claim is made.

## 11. Guard/policy determinism

The guard is a restriction/check over already-existing authority.

Decision-relevant inputs are frozen:

`canonical_action, ScopeSnapshot, policy_digest, FactBundle, as_of, accumulated effect/budget state`.

For identical frozen inputs, guard output and diagnostics must be replay-stable. Divergence produces `GUARD_NONDETERMINISM`, quarantines that guard/profile version for consequential effects and triggers existing recovery/incident handling.

Policy composition uses constraints rather than a vague total order:

`PolicyConstraint = (allowed_effect_set, required_sandbox, required_review, resource_limits, credential_constraints)`.

The final allowed effect set is the intersection of applicable allowed sets. Explicit DENY empties the set. REQUIRE_REVIEW is an additional gate, not an ordering relation.

Policy activation is signed/versioned and evidence-bound. Guard crash/timeout/unknown never silently becomes ALLOW.

## 12. Retry, replay, ambiguous outcomes and compensation

Tokens are single-use unless an explicit profile establishes otherwise.

Crash retry preserves:

`same intent_id + same idempotency_key`.

A replacement token for the same intent does not create a second logical effect. Nonce/replay state is itself freshness-protected and retained for at least token lifetime plus the bounded delivery/reconciliation window.

Crash after an external effect may yield `OUTCOME_UNKNOWN`. Blind replay is prohibited.

The task enters `RECONCILIATION_REQUIRED`. Reconciliation is consequential and requires fresh authorization/receipt. Compensation is a new consequential Intent; calling an action “rollback” never exempts it from authority/freshness checks.

Compensation depth is bounded by profile. Bound exhaustion produces STOP + INCIDENT/REVIEW, not recursive compensation forever.

## 13. Completion verification

VEI completion states:

`RUNNING, PARTIAL, BLOCKED, UNKNOWN, RECONCILIATION_REQUIRED, FAILED, DONE_WITH_EVIDENCE, REVERIFY_REQUIRED, CANCELLED`.

No final DONE or CANCELLED state may conceal unresolved consequential `OUTCOME_UNKNOWN` effects.

`DONE_WITH_EVIDENCE` requires the declared scope to be satisfied, current verifier evidence, fresh dependencies and no unresolved mandatory checks.

Evidence invalidation (expiry, verifier compromise/change, relevant policy/lineage change, supporting-authority revocation, integrity failure or incident finding) moves prior completion to `REVERIFY_REQUIRED`.

Verifier observes through a channel the tested component cannot freely forge: e.g. separate account/service, read-only mirror, external snapshot, trusted target receipt or other admitted independent observation profile. The tested component cannot write its qualification score, hidden fixture selection, rollback trigger or verifier configuration.

Independence is recorded across authorship, codebase/model family, infrastructure, operator and keys according to risk profile. A verifier is evidence/attestation, never a source of new execution authority.

## 14. Failure and recovery profile

Critical components distinguish at least `AVAILABLE, SLOW, UNAVAILABLE, STALE, CORRUPT, CONFLICTING`.

For consequential execution:

- unknown/unavailable/stale fence -> DENY/DEFER;
- unavailable/corrupt/conflicting guard or policy -> DENY/DEFER + incident as applicable;
- unavailable/stale verifier -> no DONE certification;
- unavailable durable audit where the effect requires it -> effect withheld;
- corrupt/conflicting evidence -> preserve versions, quarantine and reconcile.

No automatic ALLOW on timeout. Timeouts/retries/backoff are versioned and must be consistent with revocation/token/availability bounds.

Emergency/break-glass handling may exercise only pre-existing break-glass authority. It cannot bypass lineage, revocation, fencing or mandatory guard constraints. Each use is scoped, time-bounded, receipted and reviewed.

## 15. Audit, privacy and operational cost

VEI separates audit commitment from retained sensitive payload.

Where legitimate deletion applies, payload may be deleted/crypto-shredded while a lawful non-sensitive commitment/tombstone remains. Incident/legal holds follow existing applicable rules. Retention policy is versioned; VEI does not impose a universal duration.

Total cost is measured compositionally:

`compute + latency + storage + evaluation + operator effort + false denials + availability loss + recovery cost`.

A control whose admitted operating/cost bounds are exceeded cannot retain a stronger assurance level merely because its unit tests pass.

## 16. Normative VEI invariants

**VEI-F1 Freshness** — no stale required scope may authorize a consequential effect.

**VEI-F2 Exact binding** — actual executor parameters equal token-bound canonical parameters at the execution boundary.

**VEI-F3 Revocation** — revoked authority cannot produce a new valid consequential execution after the declared/verified propagation bound for the applicable target profile.

**VEI-F4 Lineage** — old-lineage authorization is invalid after accepted lineage transition unless an explicit migration record admits specific state without reviving revoked authority.

**VEI-F5 No implicit permission** — fencing, guard, verifier, evidence and recovery mechanisms cannot mint underlying authority.

**VEI-F6 No self-certification** — DONE requires verifier-bound evidence appropriate to the task.

**VEI-F7 No blind replay** — unknown external outcome cannot automatically execute again.

**VEI-F8 Traceability** — every consequential effect binds one durable Intent, current authorization, canonical action, EffectReceipt and evidence correlation chain.

**VEI-F9 Bounded recovery** — DEFER/UNKNOWN/RECONCILIATION resolves or escalates under a declared operational bound; compensation/retry cannot loop without bound.

Each adopted invariant MUST map to owner, machine predicate, fixture, runtime signal, known residual limitations and applicable target class.

## 17. Required conformance / chaos fixtures

Minimum candidate fixture set:

1. stale authentic restart after revocation;
2. concurrent writers / same writer-fence contention;
3. partition during fence advancement;
4. stale replica;
5. corrupt/Byzantine freshness response under the declared failure model;
6. lost freshness authority / recovery lineage;
7. replayed signed receipt;
8. duplicate token/nonce;
9. delegation cascade revocation;
10. multi-scope conflict;
11. revoked-but-unexpired token;
12. delayed Class-B request after local freshness check;
13. crash before effect;
14. crash after effect before receipt;
15. lost acknowledgement;
16. reconciliation retry;
17. compensation-loop bound;
18. canonicalizer/adapter differential;
19. symlink/path race;
20. DNS/redirect rebinding;
21. guard nondeterminism;
22. TCB digest mismatch;
23. verifier compromise/change;
24. observation-path corruption;
25. unresolved OUTCOME_UNKNOWN prevents false completion;
26. post-chaos state reconciliation.

Positive controls are also required so a safe implementation is not rewarded for denying everything.

## 18. Formal assurance profile

Before a high-consequence deployment claims strong VEI guarantees, the applicable state model MUST check at least F1/F2/F3/F4/F7 and the declared writer/revocation/lineage transitions, or provide equivalent exhaustive assurance for the bounded model.

The formal model MUST declare abstraction/state-space bounds and cannot convert model success into open-world proof.

At minimum, formal state includes lineage, scoped writer fences, revocation epochs, active/revoked authority, tokens, intents/effects, replay state and recovery transitions.

## 19. Admission / demotion profile

Candidate assurance levels:

`A SPECIFIED -> B PROTOTYPE -> C SHADOW -> D LIMITED/CANARY -> E GENERAL`.

Promotion requires evidence appropriate to the level and a signed PromotionRecord through existing authority. CI success alone cannot promote.

Incidents, TCB compromise, violated revocation bounds, or unqualified material changes to canonicalizer/guard/executor/verifier/fencing/security policy require `REVERIFY_REQUIRED` and may demote the applicable assurance level.

Effect-path performance testing begins before D on isolated/staging targets.

## 20. Compatibility and non-duplication

- **Canonical v15.5:** broad Authority, Security, Evidence/Provenance, Dependency/Requalification, Recovery/Incident, Privacy/Human-Effect and resource owners remain controlling. VEI is a specialization, not a replacement.
- **V1511-RCC-001:** RCC owns recursive transition/control closure and already requires fresh qualification, revocation continuity and stale-receipt resistance. VEI supplies a general runtime effect-boundary profile; it does not redefine RCC. TEST-RCC-055 is consistent with VEI-F1/F3 and should remain owned by RCC unless separately integrated.
- **V1511-ERC-001:** ERC owns evaluation reachability/evidence containment. VEI's verifier/receipt rules apply to runtime completion evidence but do not replace ERC's reachability graph or evaluation fixture semantics.
- **V1511-REP-001 / V1511-SHR-001:** orthogonal.
- No new human-effect, privacy, consent or authority semantics are introduced. Existing applicable checks remain mandatory.

## 21. Implementation increments

**I1 Contracts:** RootManifest, DeploymentProfile, ScopeSnapshot, AuthorizationToken, Intent, EffectReceipt, risk/quarantine/promotion records. Exit: schema + downgrade tests.

**I2 Freshness:** bootstrap/lineage, scoped writer/revocation/policy versions, delegation. Exit: F1/F3/F4 + concurrency/partition tests.

**I3 Effects:** canonicalizer, exact binding, target classes, retry/reconciliation. Exit: F2/F7/F8.

**I4 Verification:** verifier isolation + completion state machine. Exit: F6.

**I5 Recovery:** failure matrix, incidents, lineage recovery, compensation. Exit: F9.

**I6 Assurance:** formal model, chaos suite, shadow staging and total-cost measurement.

These increments are implementation obligations, not automatic canonical admission.

## 22. Admission blockers

V1511-VEI-001 remains noncanonical until at least:

1. exact semantic reconciliation against the authorized target source and existing candidate owners;
2. collision review with RCC/Authority/Revocation/Security/Evidence/Recovery owners;
3. executable schemas and runtime profile;
4. bounded formal model and invariant traceability;
5. positive/negative/chaos conformance execution;
6. target-class staging including at least one real Class A/B boundary where available;
7. verifier-isolation evidence;
8. operational availability/false-denial/recovery-cost evidence;
9. independent review appropriate to risk;
10. normal Garden comparison/admission.

## 23. Plain-language summary

The candidate says: a permission written in a document is not enough. Immediately before a real effect, the runtime must prove that the state is still current, the permission was not revoked, the final action is exactly what was approved, delayed/replayed work cannot silently regain permission, uncertain external outcomes are reconciled instead of repeated, and “done” means externally checked evidence rather than the agent saying it finished.

The strongest guarantee is available only when the real target can enforce the required freshness/fencing property. Where the target cannot do that, the system must say exactly what weaker guarantee remains rather than pretending the gap disappeared.
