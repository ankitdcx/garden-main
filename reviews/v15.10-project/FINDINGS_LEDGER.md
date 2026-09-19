# v15.10 Findings Ledger

This file is the lead's reconciliation index. Raw reviewer outputs remain immutable in their own GitHub artifacts.

Finding states:
OPEN -> CONFIRMED | REJECTED_WITH_EVIDENCE | DUPLICATE | NEEDS_HUMAN_DECISION
CONFIRMED -> PATCHED -> RECHECKED -> CLOSED

Rules:
- never close by majority vote alone;
- preserve minority/blocking findings;
- rejection requires evidence and a reason;
- patching does not equal closure;
- a material candidate change must be rechecked;
- no reviewer output may directly mutate canonical Garden.

| Finding | Source reviewer | Severity | Area | State | Candidate owner | Evidence/disposition |
|---|---|---|---|---|---|---|
| B-01..B-09 | PR #91 | BLOCKING | v15.9->v15.10 preservation | OPEN | TBD | Mandatory inherited blocker set |
