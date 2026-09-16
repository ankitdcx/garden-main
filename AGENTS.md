# Garden agent entry

Before any GitHub write, branch creation, file mutation, pull request, workflow rerun, merge attempt, or branch replacement in this repository, read `GIT_OPERATING_CONTEXT.md` first and refresh the live `main` head/ruleset snapshot when required by that file.

For parallel ChatGPT Git work, also read `CHATGPT_WORKSTREAM_POLICY.json`: one chat thread + one bounded work package uses its own `chatgpt/...` branch and early draft PR; genuine semantic collisions are reconciled on a fresh `integration/...` branch and final main admission is serialized through the merge train.

For design or implementation semantics, also use the repository's canonical/source manifests, governance/process records, tests, and `.github/PULL_REQUEST_TEMPLATE.md`. `GIT_OPERATING_CONTEXT.md` and `CHATGPT_WORKSTREAM_POLICY.json` are operational Git/process sources only; they do not change Garden canonical semantics, grant authority, or authorize promotion.

Do not bypass strict required checks, rewrite protected branch history, fabricate human/reviewer approval, or treat a failed fail-closed Garden assurance gate as a Git error merely to make CI green.
