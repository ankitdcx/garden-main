# Multi-agent integration provenance

`garden-main` is a private implementation workspace. Textual Git merge success is not evidence that two agent changes compose semantically.

This repository therefore uses the same shared Garden concept introduced in `garden-swarm`, with a stricter private-build profile.

## AgentWorkIntent/v1

Before a guarded PR can be treated as merge-ready, its body declares:

- `intent_id` and `agent_id`;
- bounded `work_package_id`;
- exact PR `base_sha`;
- canonical `source_root_sha256`;
- `design_epoch_ref` (`Garden-v15.5@<source-root>` for the current baseline);
- intended paths and symbols;
- semantic domains;
- affected invariants and FunctionContracts;
- intended effect;
- parallel mode.

The CI guard resolves the canonical source manifest from the PR's **base commit**, not from the proposed branch. An agent cannot make a stale/self-chosen source identity current by editing its own copy of the manifest.

## Collision model

Two declared intents require explicit integration evidence when they overlap by any of:

- repository path/directory;
- symbol;
- semantic domain/responsibility;
- invariant;
- FunctionContract.

Different files can therefore still collide. Divergent base/source/DesignEpoch bindings are preserved in the comparison evidence and must not be hidden by a clean textual merge.

## Legacy/undeclared concurrent PRs

For an open PR without `AgentWorkIntent/v1`:

- direct path/directory overlap fails closed;
- otherwise cross-file semantic overlap remains **UNKNOWN** and is reported as a warning;
- absence outside the evidence pack is never inferred.

## IntegrationReceipt/v1

If declared work collides, a non-blocking integration receipt must bind:

- current intent and work package;
- base SHA, source root and DesignEpoch;
- every colliding intent;
- semantic comparison result;
- composition evidence;
- post-integration tests for `COMPATIBLE` composition.

`BLOCKED` remains blocking. A receipt is evidence only: it does not grant authority, approve a Garden semantic delta, or promote canonical source.

## Canonical boundary

`canonical/current/` remains immutable in place. This mechanism governs repository change composition only. It does not alter Garden v15.5, mint HITL approval, replace ActionGate/evolution governance, or create canonical-promotion authority.

## Enforcement limitation

The workflow is executable CI, but repository branch/ruleset protection is a separate GitHub administration control. Until `main` requires successful checks and disallows direct bypass, CI existence alone is not proof that every merge must pass it.
