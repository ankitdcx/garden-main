# Garden Main — Private Build Repository

Status: private implementation workspace.

## Latest working candidate: v15.7

[Garden v15.7](canonical/candidates/v15.7/README.md) carries the complete prepared v15.6 draft forward and adds six registered programs: TRACE, focused cognitive increment, cognitive qualification, comparative coverage, design closure and event-driven context routing. The user authorized a direct version jump. Its canonical predecessor remains v15.5; no intermediate v15.6 promotion is claimed. The candidate consists of five separate design documents. Bounded recovery, release verification, physical simulation and context-routing implementations now have scoped evidence under [qualification](reviews/v15.7/qualification/README.md). See [integration evidence](reviews/v15.7/SOURCE-INTEGRATION-RECEIPT.json) and [release status](reviews/v15.7/RELEASE-STATUS.md).

## Retained v15.6 draft lineage

The retained [five-file v15.6 candidate](canonical/candidates/v15.6/README.md) consolidates the pending upgrade queue, 15 corrected engineering patterns and 38 additional assurance work items. It is not yet canonical. See the [release status and remaining gates](reviews/v15.6/RELEASE-STATUS.md), [pending dispositions](design_deltas/v15.6/PENDING-RECONCILIATION-2026-09-15.json) and [reference migration inventory](reviews/v15.6/REFERENCE-MIGRATION-INVENTORY.json).

An exact [v15.5 archival copy](canonical/archive/v15.5/SOURCE_MANIFEST.json) preserves predecessor bytes. Current canonical pointers and historical evidence bindings remain v15.5 until the existing promotion gates pass.

## Current canonical source

- Garden v15.5 / GSL v45.1 five-file canonical source is pinned under `canonical/current/`.
- SCEP v1.1 remains the recursive construction/bootstrap seed where applicable; it is not the current Garden release identifier.
- OCF + CPI + TML + CMUR + SCEP remain construction/review machinery around the canonical source.
- User remains Garden Human-in-the-Loop for major Garden-level design decisions.
- No repository content grants an external licence or transfers Garden ownership/IP.
- `described != proved != implemented != empirically validated != certified`

## How this repository works

Garden is built as small bounded work packages.

1. Take the highest-priority OPEN work package.
2. Freeze the work-package text and source version.
3. Use AI to propose an implementation.
4. Use separate blind reviewers: skeptical/red-team, formal, implementation, evidence.
5. Run deterministic tests/checkers.
6. Resolve blockers; do not vote them away.
7. Store failures/counterexamples/corrections.
8. Merge only a scoped improvement.
9. Repeat.

## Current implementation sequence

- WP-001 — Minimal executable GSL semantic kernel
- WP-002 — Garden source -> OCF obligation/gap extractor
- WP-003 — Minimal GSL-KR claim/evidence/dependency store
- WP-004 — Typed verifier bridge
- WP-005 — Public-swarm candidate intake and full-source cross-reference
- WP-006 — Canonical successor materialization after an admitted semantic delta

`implementation/` contains a non-certified reference slice spanning WP-001..004. The source-extraction and change-impact tooling advances WP-002, but no partial implementation is evidence of complete GSL conformance or certification.

The first major milestone remains:

`Garden source -> machine-readable obligations -> bounded work packages -> reviews/checkers -> scoped closure receipt`

Public `garden-swarm` findings enter only through the WP-005 candidate-intake/cross-reference path. They do not modify `canonical/current/` or become Garden semantics merely because one or more models agree. WP-006 may materialize a successor candidate only after a coherent semantic delta survives full-corpus cross-reference, applicable tests/evidence, and the required Garden-level human decision boundary.

## Important

Do not treat chatbot consensus as proof.
Do not let generated code modify its own protected verifier.
Do not turn technical reputation into governance authority.
Do not make the repository public without an intentional IP/disclosure decision.
