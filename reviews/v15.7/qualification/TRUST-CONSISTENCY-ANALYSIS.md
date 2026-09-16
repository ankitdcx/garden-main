# Trust and consistency analysis for v15.7 completion work

Status: bounded implementation analysis; not admission, certification, whole-platform proof, or a new engine.

This analysis addresses the requested trust, consistency, partition, multi-agent hazard, and implementation-boundary questions (items 31–35) against the code currently present in this candidate. It distinguishes demonstrated local properties from missing production adapters.

## 1. Action boundaries and minimum trusted computing base

| Action boundary | Minimum TCB needed for the claimed property | Existing enforcement and exact seam | Principal bypass or unproved path |
|---|---|---|---|
| Advance a governed process state | The persisted `CompletionStore`, the supplied trusted gate verifier, `ProcessFactory`, bound `CycleBinding`, and current algebra profile | `CompletionStore.restore` rejects changed bindings/profile; `CompletionStore.advance` verifies every required gate through the caller-supplied trusted adapter before recording the transition (`implementation/garden_kernel/completion_runner.py`) | The module does not authenticate the caller or construct the gate adapter. A malicious host/database replacement is outside the hash chain; the module explicitly requires an external checkpoint. |
| Reserve and dispatch an external model call | Shared `CompletionStore`, transaction-capable SQLite, trusted clock, budget configuration, worker implementation, and provider adapter that calls the required pre-dispatch validators | `CompletionStore.enqueue`, claim/reservation logic, leases, budgets, and UNKNOWN handling in `completion_runner.py`; `ContextRouter.validate_claim` rechecks packet, policy, context, freshness, claim token, and lease immediately before the provider call (`context_routing.py`) | `ContextRouter` cannot authenticate ingress or a provider. The public adapter is not implemented here; bypass remains possible if an adapter calls the provider without `validate_claim`. Clock rollback and hostile DB replacement are not solved. |
| Commit a permissioned local effect | `PermissionRecoveryBoundary`, its SQLite transaction, authoritative permission/revocation state, fencing epoch, stable effect identity, and the target participating in the same transaction/protocol | `admit` checks current permission; `dispatch` atomically rechecks permission and revocation, rejects stale fencing epochs, and commits an idempotent effect; `reconcile` requires committed state or authoritative nonexecution evidence (`permission_recovery.py`) | This is a local reference boundary, not production-wired. A distributed target outside the transaction can ignore the fence, execute after revocation, or duplicate an effect. Fixture permission is explicitly not authority. |
| Admit a protected repository proposal | Base-checked workflow/code, protected base commit, Git object integrity, source identity, authority registry, exact changed-path classification, PR-specific human admission record when constitutional, and ActionGate | `.github/workflows/trusted-human-admission.yml`; `scripts/gate_human_admitted_update.py`; `base_pinned_attestation` in `base_admission.py`; `verify_governance_receipt`/`verify_attestation_receipts` in `evolution_trust.py`; `_decide_evolution_action` in `evolution_gate.py` | Candidate records cannot self-authorize because admission is read from the base. Repository administration, branch protection, account authentication, and the human/operator act remain external trust roots. ALLOW covers PROPOSE/TRIAGE, not canonical promotion. |
| Apply shared physical actuation | Authenticated controller identity, fresh epoch/fence, exclusive allocator, qualified sensors/clock, independent fallback, and actuator-side enforcement | Bounded simulation rejects stale epochs, requires revalidation and fresh authorization for primary return, and models shared-actuator conflicts (`physical_assurance.py`: `transfer_is_authenticated`, `TankSimulation.actuator_command`, `request_primary_return`, `shared_actuator_decision`) | HMAC is only a simulation token; there is no production key management, hardware root, actuator adapter, or continuous-time proof. Identical commands from two agents are treated as coordinated only in the toy decision helper; production coordination identity is absent. |
| Verify a release artifact | Trusted metadata root and rotation policy, trusted fetch/transport, expected source materials and command, in-toto/TUF verifier, and artifact consumer enforcing the result | `verify_release` checks trusted metadata, link command/materials, artifact digest and emits `promotion_authorized: false` (`release_verification.py`) | No repository-wide deployment adapter forces every artifact consumer through this function. Trusted-root provisioning, online metadata origin, rollback/freeze policy, and production signing ceremony remain external. |

The minimum TCB is action-specific. `CompletionStore` is not an authority service; `ContextRouter` is not a truth store; the permission boundary is not a distributed coordinator; the physical model is not a certified controller; and release verification does not promote a release.

## 2. Zero Trust mapping

| Zero Trust function | Existing mapping | Reevaluation point | Missing adapter or limitation |
|---|---|---|---|
| Subject authentication | Repository workflow obtains GitHub event base/head and repository context; base admission binds an observed instruction recorder. Physical simulation authenticates a transfer token. | Base workflow validates exact event OIDs for each run; physical transfer is checked before acceptance. | No general workload identity, mTLS/SPIFFE, hardware identity, provider identity, or production key lifecycle adapter. Simulation HMAC is not production authentication. |
| Authorization | Evolution envelopes restrict action/resource/delegation (`evolution_authority.py`: `can_execute`, `delegate_within_envelope`); shared-state authority intersects all controlling scopes (`authority_path.py`: `effective_authority_for_artifact_trigger`); ActionGate requires scope and human signoff for constitutional changes. | ActionGate evaluates each action; artifact-trigger authority is recomputed for each target action/resource. | No common authorization adapter connects these checks to model providers, OS processes, databases, physical actuators, or cloud IAM. Revocation distribution is not unified. |
| Policy enforcement | Process gates, permission dispatch recheck, context `validate_claim`, release verification, and physical epoch rejection are explicit enforcement seams. | Immediately before transition, local effect commit, provider dispatch, artifact acceptance, or actuator command. | Enforcement is not ambient. Callers can bypass unwired library functions. Production adapters must make these seams mandatory and fail closed. |
| Continuous reevaluation | `ContextRouter.validate_claim` recomputes relevant context/freshness; `PermissionRecoveryBoundary.dispatch` rechecks permission/revocation/fence; `request_primary_return` requires fresh authorization and state recovery; ActionGate verifies current DesignEpoch/dependencies. | At consequential use, not merely at initial ingest or admission. | No universal event bus distributes identity, revocation, dependency, or policy changes. Clock trust and bounded-staleness policy are deployment obligations. |
| Least privilege | Evolution authority composition intersects permissions and delegation cannot widen them; context packets restrict classification/envelope and bounded content; completion budgets are per pool/call. | On delegation, routing, claim, and gate evaluation. | Provider credentials and filesystem/network sandboxing are outside these modules. Budget limits are not permission grants. |
| Evidence and audit | Completion events form a hash chain; trusted receipts bind exact identities; permission recovery records trace events; release checks bind materials and commands. | Each transition/effect/check records a receipt or event. | A hash chain detects mutation under the assumed checkpoint; it does not prevent hostile store replacement. Durable external checkpointing and protected log export are missing. |

## 3. Per-object consistency requirements

The system must not apply one generic “eventual consistency” rule to all objects.

| Object class | Safe merge model | Required coordination | Partition behavior |
|---|---|---|---|
| Immutable observations and attributed model outputs | Content-addressed union is acceptable when identities, provenance, timestamps, contradiction/supersession edges, and classification remain intact. `ContextRouter.ingest` deduplicates equal fingerprints and rejects observation-ID rebinding. | No global lock for additive ingest; deterministic conflict/supersession processing is still required before consequential use. | May accept bounded local observations, but they remain `OBSERVATION_NOT_VERIFIED_FACT`; unresolved contradiction or stale state blocks provider routing where required. |
| Derived context packets and materiality receipts | Recompute from source observation state and versioned policy; do not merge packets as truth. | Compare exact source-state root, policy and missing-contradiction set at dispatch through `validate_claim`. | A stale or incomplete packet must fail dispatch and be reevaluated. Historical observations may be retained but cannot support a current claim without revalidation. |
| Evidence/claims/knowledge | Preserve separate records and support/defeat edges; contradictory claims may coexist. | Owning epistemic/admission process resolves status; model agreement is not coordination or proof. | UNKNOWN/CONFLICTED persists. Do not choose an arbitrary winner while disconnected. |
| Authority grants, admissions, and policy | Never union grants. Effective authority is intersection/bounded delegation; admissions bind exact action, source identity, base/head and expiry. | Strong coordination through the protected authority owner and base-pinned gate. | No fresh trusted state means no new consequential authorization. Cached authority may be used only inside an explicitly valid, bounded, unrevoked envelope whose offline semantics are separately approved. No such general offline envelope adapter is implemented here. |
| Revocations | Monotone deny within the local permission boundary; revocation overrides prior admission before effect commit. | Revocation must reach every enforcement point, with ordering/fencing against stale writers. | Fail closed for new consequential effects when revocation freshness is unknown. Already-committed effects require observation/reconciliation or compensation; they cannot be undone by relabeling. |
| Exclusive allocations, leases, and actuator ownership | Single-writer/fenced ownership; concurrent commands do not merge unless an allocator proves the same coordinated command and authority. | Consensus/linearizable allocator or a physically enforced fencing service for distributed deployment. SQLite serialization is sufficient only for the single local reference boundary. | Do not grant or transfer exclusive ownership during loss of coordinator/quorum. Existing safe controller may continue only under an explicitly bounded fail-operational safety case; otherwise enter minimum-risk/fallback. |
| External effects and charge-bearing calls | Stable idempotency/effect identity plus authoritative outcome reconciliation. An unknown result is not “not executed.” | Reserve before dispatch; fence duplicates; reconcile with provider/target evidence. | Stop automatic retry when effect or charge is uncertain. `CompletionStore` marks interrupted external calls UNKNOWN; `PermissionRecoveryBoundary.reconcile` requires committed or authoritative nonexecution evidence. |
| Release/canonical pointers | Immutable artifacts may be replicated; the active pointer is a protected, atomic decision, not a mergeable register. | Protected update gate and explicit promotion authority. | Continue serving the last admitted pointer. A candidate or verified artifact cannot self-promote during partition. |

## 4. Partition and revocation analysis

The safe default for permissions and exclusive resources is fail closed, while observation capture can remain available under bounded labeling.

- Permission cache: this candidate provides no general offline permission token. Consequently, loss of the authority/revocation source must block new consequential actions rather than interpret silence as permission. `PermissionRecoveryBoundary.dispatch` demonstrates the necessary final recheck, but only inside one SQLite transaction.
- Revocation race: a locally admitted attempt is still rejected if `revoke` occurs before `dispatch`. For a remote target, the same property requires target-side fencing and a revocation epoch. That adapter is absent.
- In-flight effects: if connectivity fails after dispatch, state is UNKNOWN. Automatic retry is prohibited until authoritative reconciliation. Compensation requires separate authority and cannot be assumed equivalent to rollback.
- Exclusive allocation: no quorum means no new lease or transfer. A stale holder must be rejected by an actuator/resource-side epoch. The physical simulation demonstrates epoch rejection but not distributed allocation.
- Fail-operational exception: continued action while disconnected is permissible only for a pre-authorized, bounded safety envelope with local enforcement, expiry, resource limits, and a transition to minimum risk. The tank fallback is a bounded illustration, not a general offline authorization mechanism.
- Rejoin: recovered nodes must reauthenticate, obtain current policy/revocation/allocation epochs, reconcile UNKNOWN effects and charges, and revalidate context/dependencies before resuming.

## 5. Multi-agent STPA linkage and limits

The selected concrete multi-agent hazard is already represented as `UCA-7-two-agent-shared-actuator` in `physical_assurance.py`. Its constraint is that conflicting valid agents require coordinated exclusive allocation; `shared_actuator_decision` rejects commands with different epochs or values. This is a useful STPA-style unsafe-control-action fixture because it demonstrates that individually valid agents do not imply a safe composed command.

The evidence is deliberately narrow:

- it is a bounded reference simulation, not hardware testing or a continuous-time proof;
- it does not authenticate real agents, elect an allocator, distribute revocations, prove Byzantine tolerance, or enforce a fence at physical hardware;
- accepting identical `(epoch, command)` tuples does not prove common authorization or absence of replay;
- broader multi-agent hazards—omitted commands, timing, unsafe duration, shared-sensor corruption, allocator compromise, and common-mode fallback failure—remain outside this one fixture.

Accordingly, the physical receipt may support the UCA-7 test claim only, not platform-wide multi-agent safety.

## 6. Temporal and seL4 decisions

### Temporal

Decision: defer production adoption. A durable workflow engine could improve timer, retry, and crash recovery semantics, but the present risk is not lack of another scheduler. `CompletionStore` already establishes bounded local reservation and UNKNOWN handling; adding Temporal before defining permission/revocation, provider idempotency, and authoritative reconciliation adapters would move rather than close the trust boundary. A future evaluation should compare exact workflow-history semantics, activity idempotency, credential isolation, cancellation/revocation propagation, and partition behavior against the existing effect states. No Temporal dependency is justified by current evidence.

### seL4

Decision: defer. seL4 could reduce the trusted OS/kernel surface for a narrowly partitioned physical enforcement appliance, but current evidence is Python/SQLite reference behavior without a hardware target, capability allocation, verified device drivers, WCET argument, or refinement from these contracts to an seL4 component model. Introducing seL4 now would not supply the missing distributed allocator, identity/key management, sensor qualification, or actuator-side fence. Revisit only after the physical action boundary and minimal enforcement component are stable enough to state a refinement theorem and hardware assurance case.

## 7. Remaining concrete blockers

1. Production identity/authentication and key-management adapters for workers, providers, sensors, controllers, and artifact signers.
2. Mandatory wiring that makes ActionGate, `ContextRouter.validate_claim`, permission/fence recheck, and release verification unavoidable at their respective effect points.
3. Distributed revocation propagation and a linearizable/fenced exclusive-allocation service for shared resources.
4. Authoritative reconciliation adapters for external effects and unknown provider charges.
5. Trusted clock, rollback/freeze protection, durable external audit checkpointing, and hostile-store replacement controls.
6. Hardware-qualified sensor/actuator enforcement, independent fallback evidence, and broader STPA coverage beyond UCA-7.
7. Exact deployment profiles specifying when bounded offline operation is permitted; until then, consequential offline permission is denied.

These are integration and assurance obligations under existing owners. They do not justify a new top-level engine, and completion of one boundary must not be generalized into whole-platform consistency, Zero Trust, release, or physical-safety proof.
