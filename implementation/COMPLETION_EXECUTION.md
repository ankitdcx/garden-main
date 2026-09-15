# Completion-driven Garden execution

The user requested completion-driven work on 2026-09-15: do not wait for an hourly
slot; start the next eligible item when the previous item finishes. Better review
quality remains mandatory. GardenCanonicalUpdateProcess 1.4 remains the route and
gate authority; immutable Garden v15.5 remains the source baseline.

`garden_kernel.completion_runner.CompletionWorker.run_ready` executes ready tasks
sequentially and continues immediately after successful completion. Each task is
one bounded work unit. Dependencies join only after all predecessors succeed.
There is one shared claim across all cycles and provider families. Every handler
must make at most one external call. A wake is bounded to 32 tasks and the durable
host must enqueue a continuation when eligible work remains.

The runtime starts paused. A deployment must supply one persistent SQLite store,
trusted handlers, fresh source/repository observations, independent gate verifiers,
and verified budget balances before paid operation. Separate ephemeral databases
in GitHub jobs do **not** provide global serialization or accounting.

Use one authenticated owner for the database. SQLite serializes claims with
`BEGIN IMMEDIATE`; external effects occur after committed reservations. Persist
the database on a durable local filesystem, not a network filesystem. Backups and
externally retained event-chain checkpoints are required operational controls.
The event hash chain detects accidental record corruption, not hostile rewriting
of the database or its materialized state. No receipt creates authority.

## Execution and recovery

1. Create an immutable cycle with exact source, repository heads, process version,
   route receipt and algebra-profile hash.
2. Enqueue idempotently named tasks in dependency order. A changed task body or
   cycle cannot reuse an existing task ID. Missing/cross-cycle dependencies fail.
3. Observe current bindings and claim the highest-priority ready task atomically.
4. For external calls, reserve maximum cost before dispatch; unknown balances block
   paid work. Routine, challenger, escalation and reserve balances remain separate.
   The aggregate UTC-day ceiling is $1. Free requests share 48/rolling-day and
   2/rolling-hour ceilings; failed attempts count. These are conservative existing
   limits, not an instruction to spend or hit provider quotas.
5. Persist the result before continuing. A 429 persists a shared cooldown using
   the greater of Retry-After and bounded exponential backoff. It does not complete
   the task or advance the Garden process. The host must arrange one delayed wake;
   this module does not install an hourly poller.
6. A timeout, crash, absent charge or charge above reservation is UNKNOWN and blocks
   dispatch until a trusted operator/provider reconciliation resolves the effect.
   Expired claims cannot be completed by stale workers or reclaimed automatically.
7. `advance` restores the process from its exact receipt prefix, obtains the engine's
   required gates, and requires an external verifier to validate each piece of
   evidence against the binding. Persistence and the transition are transactional.

Budget initialization must cover all historical spending on the account. Every
caller must use this database. The library cannot bound spending by unrelated
clients using the same provider key. A provider cap must bound actual call cost;
post-response accounting cannot prevent an unbounded provider-side charge.

## Review quality

`review_packet.packet` checks exact content against a caller-derived closure
inventory. It does not claim that the inventory itself is complete. Unexplained
objects, exclusions and unresolved closure frontiers block the bounded packet.
`ReviewSet` binds reviewers to the same packet/cycle, provides detached blind
inputs, prohibits duplicate families and waits for every allocated blind review
before exposing peer findings for cross-examination. All allocated cross-examiners
must finish before a closure receipt. The builder cannot independently verify its
own fix; an exact candidate SHA and external evidence verifier are required.

Reviewer family identity, provider provenance and post-fix evidence must be checked
by trusted adapters. A model's own family/status/independence claim is insufficient.
Current policy determines the required family count; a lower constructor argument
must never be substituted to work around resource limits. No live provider adapter
is connected by this implementation.

## Remaining deployment acceptance

- Durable host, completion/continuation and delayed-wake delivery, and authenticated
  handlers must be selected and installed. GitHub PR merge webhooks are available;
  task completion, delayed retries and review results need the worker host.
- Connect all provider lanes to the shared store, enforce one call per handler,
  reconcile existing account spending and test actual rate-limit behavior.
- Mechanically derive complete source closure, verify family/provenance claims,
  implement real independent gate verifiers and persist/reconstruct ReviewSet
  receipts through the host's task results.
- Demonstrate a real packet through review, cross-examination, repair and independent
  post-fix verification. Unit tests use controlled verifiers and are not independent
  review evidence or release certification.

All legacy timers and provider batch workers remain paused until these conditions
are met. This document does not claim that every Process 1.4 rule or all twelve
general Process Algebra operators are implemented. In particular, domain-specific
rollback/compensation and formal reconstruction attestations remain separate work;
an ordinary database restore is not an authority reconstruction proof.
