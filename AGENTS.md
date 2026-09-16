# Garden agent entry

Before any GitHub write, branch creation, file mutation, pull request, workflow rerun, merge attempt, or branch replacement in this repository, read `GIT_OPERATING_CONTEXT.md` first and refresh the live `main` head/ruleset snapshot when required by that file.

For design or implementation semantics, also use the repository's canonical/source manifests, governance/process records, tests, and `.github/PULL_REQUEST_TEMPLATE.md`. `GIT_OPERATING_CONTEXT.md` is an operational Git/process source only; it does not change Garden canonical semantics, grant authority, or authorize promotion.

Do not bypass strict required checks, rewrite protected branch history, fabricate human/reviewer approval, or treat a failed fail-closed Garden assurance gate as a Git error merely to make CI green.
