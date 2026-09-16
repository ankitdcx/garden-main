# v15.7 executable reference boundaries

Status: candidate implementation contracts, version 1, 2026-09-16. Existing owners remain authoritative. These packages exercise selected requirements; they do not implement the entire Garden design, authorize effects, or establish qualification of a deployment.

## Permission, revocation and recovery

Existing Process, Runtime, authority and recovery owners retain their roles. `formal/permission_recovery/Recovery.tla` models two workers, one effect and bounded epochs. Its configuration, assumptions, invariants, fairness assumptions and checked state counts are retained with the TLC receipt. Counterexamples, complete bounded exploration and incomplete runs are distinct outcomes. The fence-disabled negative control checks that the selected property can actually fail.

`implementation/garden_kernel/permission_recovery.py` is a durable SQLite reference target. Effect identity binds payload; repeated delivery cannot rebind it. Permission and the target fence are checked at the target commit boundary. Dispatch, commit, acknowledgment, uncertain completion and reconciliation remain distinct. Revocation before commit prevents that commit; revocation after commit cannot erase it. Uncertain completion requires authoritative reconciliation. A new attempt requires fresh admission. This shared-transaction example does not establish atomicity, idempotence or fencing for an arbitrary remote actuator.

Runtime traces are compared with named model actions. Such correspondence is a bounded test observation, not a proved refinement relation. Deployment requires target-specific commitment points, authenticated grants, lease/clock assumptions, recovery authority, containment and compensation behavior, plus crash and concurrency qualification on the actual storage/transport.

## Release verification

`implementation/garden_kernel/release_verification.py` composes upstream TUF and in-toto verification under the existing release/admission owner. Required acceptance is the conjunction of valid TUF metadata and content checks, valid in-toto policy/attestations and an identical artifact hash at both stages. Any invalid or incomplete required check blocks this reference verification result. A verified result grants no promotion authority.

The caller must supply a pinned trusted root, pinned layout policy, authorized layout keys, exact source-material and build-command policy, and persistent repository-specific TUF state. Resetting the cache can lose rollback history. Key rotation must authenticate the new root with the applicable old and new thresholds; compromised-root recovery requires an independently trusted root update. Synthetic signed fixtures demonstrate library behavior, not custody or security of production release keys.

Inputs are snapshotted for one verification so later reads cannot silently change the policy or attestations that were checked. Receipts retain identities, individual results and verifier versions. Layout inspection commands are prohibited in this bounded profile. Expiry, insufficient signatures, missing steps, unauthorized builders, downgraded metadata, content substitution and cross-stage identity mismatch are separate failure cases.

## Physical fallback

`implementation/garden_kernel/physical_assurance.py` uses one bounded tank process with explicit dynamics, uncertainty, sensing, control and handoff delay. Switching margins and recoverable regions follow from the declared outward speed and delay bounds. The reference scenario records trajectories, measured timing, envelope observations and loss of assurance. STPA records include switching and shared-actuator conflict hazards.

The fallback controller and epoch-fenced actuator are simulated components. HMAC-authenticated state transfer uses a fixture key; it does not qualify production key management or hardware independence. Leaving the recoverable region or breaching assumptions triggers a recorded minimum-risk response with loss of assurance, not a safety guarantee. Return to the primary controller needs revalidation, fresh authorization and a recoverable state.

Discrete simulation evidence is not a continuous-time proof. Production assurance additionally needs measured sensor/actuator behavior, scheduler and hardware timing, validated uncertainty bounds, independent fallback resources and physically unavoidable safety mediation across normal, emergency, maintenance and recovery paths.

## Event-driven context routing

`implementation/garden_kernel/context_routing.py` exercises the existing Process, Knowledge, Event, FunctionContract and provenance boundaries. Normalization and deduplication bind source identity and content. Materiality decisions carry reasons. Compact packets preserve source links, uncertainty, contradictions and freshness; compression is neither evidence nor authority. Budget uncertainty blocks admission unless an explicit bounded reservation is available. Queueing public specialist review does not authorize any subsequent action. The external ChatGPT frontier lane receives a separately attributable GardenFrontierReviewRequest, never an OpenRouter model substitute. Unknown/incomplete dependency closure or required whole-context review blocks compact routing or requests context expansion. Source-root and DesignEpoch bindings participate in revalidation.

Reference tests do not establish frontier-model quality, provider cost, latency or public-adapter qualification. Those results require separately authorized provider runs with pinned models, inputs, budget measurements and matched evaluation conditions.

## Evidence and activation

`reviews/v15.7/qualification/OBLIGATION-REGISTER.json` accounts for the 38 agreed work items, 20 engineering profiles and successor programs against existing coverage and remaining gaps. Per-package receipts bind actual code, tests, assumptions and results. Per-package FunctionContract declarations bind selected executable functions; declarations alone are not proof that every invariant holds or a replacement for canonical registry admission.

Reference packages are opt-in qualification tools. No live worker, release promotion path or hardware adapter automatically adopts them. Production integration requires its own exact contract and owner bindings, target-specific tests, review and authority. Temporal and seL4 remain deferred decisions, contingent on recovery results and trust-boundary analysis respectively. Effective independent-family review, full semantic closure and protected enforcement evidence remain separate promotion obligations.
