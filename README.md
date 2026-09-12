# Garden Main — Private Build Repository

Status: private implementation workspace.

## Current seed

- Garden v15.2 + SCEP v1.1 merged five-file candidate
- OCF + CPI + TML + CMUR + SCEP recursive construction architecture
- User remains Garden founder / Human-in-the-Loop for major Garden-level design decisions.
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

## First implementation sequence

- WP-001 — Minimal executable GSL semantic kernel
- WP-002 — Garden source -> OCF obligation/gap extractor
- WP-003 — Minimal GSL-KR claim/evidence/dependency store
- WP-004 — Typed verifier bridge

The first major milestone is:

`Garden source -> machine-readable obligations -> bounded work packages -> reviews/checkers -> scoped closure receipt`

Once this loop works, Garden can increasingly generate its own engineering backlog.

## Important

Do not treat chatbot consensus as proof.
Do not let generated code modify its own protected verifier.
Do not turn technical reputation into governance authority.
Do not make the repository public without an intentional IP/disclosure decision.
