## Problem / bounded work package

What exact work package, defect, gap, or implementation obligation does this PR address?

## Change

What changed?

## Evidence / tests

What reproducible evidence supports the change?

## Garden impact

- Source anchors / obligations:
- Affected invariants:
- Affected FunctionContracts:
- Rights / privacy / authority / safety impact:
- Canonical effect: NONE unless separately authorized successor work

## ChatGPT workstream isolation

For new ChatGPT work, create one bounded `chatgpt/...` branch, make only an intent-only bootstrap commit, then open this draft PR before substantial editing. Genuine semantic collisions use a fresh `integration/...` branch.

<!-- GARDEN_CHATGPT_WORKSTREAM -->
```json
{"schema":"GardenChatGPTWorkstreamIntent/v1","workstream_id":"chatgpt:<bounded-workstream-id>","work_package_id":"<bounded-work-package-id>","branch":"chatgpt/<bounded-work-package>","base_sha":"<40-char PR base SHA>","dependency_intent_ids":[],"integration_strategy":"INTEGRATION_BRANCH_IF_COLLISION","draft_pr_created_before_substantial_edit":true,"draft_opened_at":"<ISO-8601 UTC>","last_activity_at":"<ISO-8601 UTC>","status":"ACTIVE"}
```

## Git preflight acknowledgement

<!-- GARDEN_GIT_PREFLIGHT_RECEIPT -->
```json
{"schema":"GardenGitPreflightReceipt/v1","workstream_id":"chatgpt:<bounded-workstream-id>","repository":"ankitdcx/garden-main","base_sha":"<40-char PR base SHA>","git_context_revision":2,"git_context_source_sha256":"<sha256 of base GIT_OPERATING_CONTEXT_SOURCE.json>","process_pointer":"governance/PROCESS_CURRENT.json","process_version":"<current process version>","verified_merge_ruleset_id":23542743,"overlap_checked_open_prs":[],"overlap_result":"NO_MATERIAL_COLLISION_WITH_DECLARED_SCOPE","created_before_substantial_edit":true,"authority_effect":"NONE"}
```

## Multi-agent integration provenance

<!-- GARDEN_AGENT_WORK_INTENT -->
```json
{"schema":"AgentWorkIntent/v1","intent_id":"<agent>:<work-package>:<unique-id>","agent_id":"<agent-id>","work_package_id":"<bounded-work-package-id>","base_sha":"<40-char PR base SHA>","source_root_sha256":"<64-char canonical source root>","design_epoch_ref":"Garden-v15.5@<source-root>","target_paths":["<file-or-directory>"],"target_symbols":[],"semantic_domains":["<semantic-responsibility>"],"affected_invariants":[],"affected_contracts":[],"intended_effect":"<bounded semantic/implementation effect>","parallel_mode":"INDEPENDENT_COMPARISON"}
```

If a collision is declared, add `GARDEN_INTEGRATION_RECEIPT` only after semantic comparison and post-composition tests.

## Recovery, if this PR repairs a bad merge

Use `REVERT` or `FORWARD_FIX`, identify the bad merge SHA and downstream invalidations, and never reset/force-push `main`.

## Checklist

- [ ] Loaded Git context source, current process pointer/process file, and applicable Garden policies.
- [ ] Early draft PR + preflight receipt exist before substantial edits.
- [ ] Actual diff is covered by AgentWorkIntent.
- [ ] Semantic collisions use a fresh integration branch.
- [ ] Structured files parse and generated Git-context views match source.
- [ ] Changed content passed central secret scanning.
- [ ] No evidence/receipt is treated as authority or canonical promotion.
