# Contributing to the private Garden build

Every change starts from a bounded work package.
Do not merge based on prose confidence or model consensus.
Preserve exact source/version and test evidence.
Record counterexamples and failed attempts.
Changes to the Minimum Stable Core, HumanCore/HSA, ownership/IP, or Garden identity require founder/HITL review.

## Multi-agent change composition

Before implementing or opening a guarded PR, declare an `AgentWorkIntent/v1` bound to the actual PR base SHA, canonical source root/DesignEpoch, bounded work package, changed paths/symbols, semantic domains, affected invariants/contracts, and intended effect. See `implementation/INTEGRATION_PROVENANCE.md` and the PR template.

Git conflict-freedom is not evidence of semantic compatibility. Different files can implement the same responsibility or interact through the same invariant/FunctionContract. Overlapping declared work therefore requires an `IntegrationReceipt/v1` with explicit composition evidence and post-integration tests before it can pass the repository guard.

Older concurrent PRs without declared intent remain semantically UNKNOWN outside direct path overlap. Do not infer independence from different filenames.

These receipts are repository evidence only. They do not mint authority, approve Garden semantics, alter Human/HITL boundaries, or promote canonical source.
