# Garden agent entry

Before any GitHub write, branch creation, file mutation, pull request, workflow rerun, merge attempt, recovery action, or branch replacement in this repository, use this loading order:

1. `GIT_OPERATING_CONTEXT_SOURCE.json` (or the generated `GIT_OPERATING_CONTEXT.md` view).
2. Refresh the live `main` head and applicable GitHub rulesets when required by the source.
3. `governance/PROCESS_CURRENT.json`.
4. The exact process file named by `governance/PROCESS_CURRENT.json`.
5. `CHATGPT_WORKSTREAM_POLICY.json` for parallel ChatGPT Git work.
6. Canonical/source manifests and applicable Garden policies/modules.

For new ChatGPT work, one chat thread + one bounded work package uses its own `chatgpt/...` branch. The only allowed mutation before the draft PR/preflight receipt is the small intent-only bootstrap commit needed to make the draft PR possible. Before substantial editing, the draft PR must contain `GardenChatGPTWorkstreamIntent/v1` and `GardenGitPreflightReceipt/v1`.

Genuine semantic collisions are reconciled on a fresh `integration/...` branch. Final admission to `main` is serialized through the merge train and ordinary repository/Garden gates.

`GIT_OPERATING_CONTEXT_SOURCE.json`, `CHATGPT_WORKSTREAM_POLICY.json`, preflight receipts, and Git recovery receipts are operational process sources/evidence only. They do not change Garden canonical semantics, grant authority, prove correctness, or authorize promotion.

Do not bypass strict required checks, rewrite protected history, fabricate human/reviewer approval, silently swap reviewer models, lower assurance to make CI green, or reset/force-push `main` to undo a bad merge. Bad merges recover through a revert-or-forward-fix PR from current `main`.
