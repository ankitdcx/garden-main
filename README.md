# Garden Main — Public Archive / Free Use

**Current status: the owner has made Garden free for everyone.**

The owner believes Garden ideas may be worth a very large amount of money—potentially billions or trillions if their claimed usefulness proves out. Even so, the present choice is that Garden remains freely available to everyone under the root [LICENSE](LICENSE).

## If anyone wants to change the free status

There are only two intended outcomes:

1. **Fully free for everyone.** This is the current state.
2. **Garden Common Fund.** If Garden is ever moved away from the fully-free model for rights or value that remain controllable, those rights, assets and proceeds must go to a Garden Common Fund rather than private or political control. Spending and economic decisions would be made democratically by approximately **100,000 randomly selected, periodically rotating ordinary people**, using a system designed to be politically independent and strongly resistant to corruption, coercion, government interference, corporate capture, concentrated wealth and organized capture.

The voters would be temporary governors, not shareholders. They would not receive transferable personal ownership stakes. The Common Fund would hold the relevant common assets and the selected community would decide spending.

The exact selection, voting, audit, rotation and anti-capture mechanism can be designed and tested if Option 2 ever needs to be activated.

**No third option is intended.** In particular, changing the free status must not turn Garden into permanent government, political-party, corporate, billionaire, administrator or other privileged private control.

The 2026-10-06 public release included permissions expressly described as perpetual or irrevocable. Nothing here claims to retroactively cancel rights already validly granted under that release.

## Version status at a glance

| Line | Status | Meaning |
| --- | --- | --- |
| **v15.5 / GSL v45.1** | **CANONICAL** | Current pinned five-file source under `canonical/current/`. |
| **v15.6** | retained draft | Prepared successor lineage; not canonical. |
| **v15.7** | materialized whole-release candidate | Last whole-release candidate currently materialized in `canonical/candidates/`; not canonical. |
| **v15.10** | later working-design / review lineage | Substantial successor redesign/review work exists, but it is not the current canonical source and is not materialized here as the current whole-release pointer. |
| **v15.11** | **active additive candidate set** | Multiple noncanonical hardening/cognition/runtime candidates are registered or under active PR review. |

The repository landing page previously made v15.7 look like the newest design work. That is no longer a complete picture: later v15.10/v15.11 work is retained as **pending successor work**, while **v15.5 remains the canonical baseline until separately admitted**.

## Pending v15.10 / v15.11 successor work

### v15.10 working-design lineage

v15.10 introduced a later redesign/review lineage beyond the v15.7 whole-release candidate. Its review artifacts are retained in repository history, including the archived [v15.10 review project](archive/retired-work/2026-09-21/chatgpt__v1510-review-project-20260919/reviews/v15.10-project/PROJECT.md). Later v15.11 candidates explicitly target or build on the v15.10 working design where applicable.

**Status:** pending/noncanonical lineage; not a replacement for `canonical/current/`.

### v15.11 additive candidates already registered on main

- [V1511-RCC-001 — Recursive Control Closure](design_deltas/v15.11/rcc/README.md): recursive-change/control qualification hardening, including cumulative control, independence, revocation/recovery and typed obligation closure.
- [V1511-REP-001 — Representation Escape Principle](design_deltas/v15.11/rep/README.md): reduces shared blind spots caused by multiple reviewers inheriting the same problem representation.
- [V1511-SHR-001 — Search-History Resilience](design_deltas/v15.11/shr/README.md): hardens retained search/history reuse, rebasing and dependency-aware invalidation.

These are **additive noncanonical candidates**, not a complete v15.11 release and not canonical admission.

### v15.11 candidate work currently under PR/review

- [PR #107 — Evaluation Reachability Closure](https://github.com/ankitdcx/garden-main/pull/107): transitive evaluation/containment reachability, persistent paths, credential/identity expansion and evidence-grounded evaluation fixtures.
- [PR #109 — Rev 2 meta-epistemic / QSE hardening](https://github.com/ankitdcx/garden-main/pull/109): preserves the later question-space / meta-epistemic hardening candidate work.
- [PR #110 — Verified Execution Integrity](https://github.com/ankitdcx/garden-main/pull/110): runtime freshness/antirollback, exact final-effect binding, target-class fencing, intent→authorization→receipt traceability, ambiguous-effect reconciliation and verifier-isolated completion.

Additional bounded regression/candidate branches may exist without being admitted to main. Open PR, branch or CI status is **evidence of pending work only**, not canonical promotion.

## v15.7 whole-release candidate

[Garden v15.7](canonical/candidates/v15.7/README.md) carries the prepared v15.6 draft forward and adds five registered programs: TRACE, focused cognitive increment, cognitive qualification, comparative coverage and design closure. Its canonical predecessor remains v15.5; no intermediate v15.6 promotion is claimed. See [integration evidence](reviews/v15.7/SOURCE-INTEGRATION-RECEIPT.json) and [release status](reviews/v15.7/RELEASE-STATUS.md).

## Retained v15.6 draft lineage

The retained [five-file v15.6 candidate](canonical/candidates/v15.6/README.md) consolidates the pending upgrade queue, 15 corrected engineering patterns and 38 additional assurance work items. It is not yet canonical. See the [release status and remaining gates](reviews/v15.6/RELEASE-STATUS.md), [pending dispositions](design_deltas/v15.6/PENDING-RECONCILIATION-2026-09-15.json) and [reference migration inventory](reviews/v15.6/REFERENCE-MIGRATION-INVENTORY.json).

An exact [v15.5 archival copy](canonical/archive/v15.5/SOURCE_MANIFEST.json) preserves predecessor bytes. Current canonical pointers and historical evidence bindings remain v15.5 until the existing promotion gates pass.

## Current canonical source

- Garden v15.5 / GSL v45.1 five-file canonical source is pinned under `canonical/current/`.
- SCEP v1.1 remains the recursive construction/bootstrap seed where applicable; it is not the current Garden release identifier.
- OCF + CPI + TML + CMUR + SCEP remain construction/review machinery around the canonical source.
- Historical Garden governance/design roles remain part of the archived design record only; they are not conditions on reuse.
- Repository material controlled by the project owner is freely released under the root [LICENSE](LICENSE), including outside-Garden and commercial use.
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
The repository is intentionally public and released for unrestricted reuse under [LICENSE](LICENSE).
