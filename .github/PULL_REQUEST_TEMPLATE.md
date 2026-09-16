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

For new ChatGPT work, open a unique `chatgpt/...` branch and draft PR before substantial editing. One chat thread + one bounded work package = one workstream. Declare dependencies here; semantic collisions are integrated on a fresh `integration/...` branch rather than by editing another chat's branch.

<!-- GARDEN_CHATGPT_WORKSTREAM -->
```json
{
  "schema": "GardenChatGPTWorkstreamIntent/v1",
  "workstream_id": "chatgpt:<bounded-workstream-id>",
  "work_package_id": "<bounded-work-package-id>",
  "branch": "chatgpt/<bounded-work-package>",
  "base_sha": "<40-char PR base SHA>",
  "dependency_intent_ids": [],
  "integration_strategy": "INTEGRATION_BRANCH_IF_COLLISION",
  "draft_pr_created_before_substantial_edit": true,
  "status": "ACTIVE"
}
```

## Multi-agent integration provenance

Fill this with the actual PR base SHA and the source root/DesignEpoch from the **base branch** `canonical/current/SOURCE_MANIFEST.json`.

<!-- GARDEN_AGENT_WORK_INTENT -->
```json
{
  "schema": "AgentWorkIntent/v1",
  "intent_id": "<agent>:<work-package>:<unique-id>",
  "agent_id": "<agent-id>",
  "work_package_id": "<bounded-work-package-id>",
  "base_sha": "<40-char PR base SHA>",
  "source_root_sha256": "<64-char canonical source root>",
  "design_epoch_ref": "Garden-v15.5@<source-root>",
  "target_paths": ["<file-or-directory>"],
  "target_symbols": [],
  "semantic_domains": ["<semantic-responsibility>"],
  "affected_invariants": [],
  "affected_contracts": [],
  "intended_effect": "<bounded semantic/implementation effect>",
  "parallel_mode": "INDEPENDENT_COMPARISON"
}
```

If the integration-provenance check reports a declared collision, add a receipt after independently comparing the changes and testing the composed result:

<!-- GARDEN_INTEGRATION_RECEIPT -->
```json
{
  "schema": "IntegrationReceipt/v1",
  "current_intent_id": "<intent-id>",
  "work_package_id": "<work-package-id>",
  "base_sha": "<same base SHA>",
  "source_root_sha256": "<same source root>",
  "design_epoch_ref": "<same DesignEpoch>",
  "concurrent_intent_ids": [],
  "semantic_compare": "COMPATIBLE",
  "composition_evidence": [],
  "tests_after_integration": []
}
```

## Uncertainty / limitations

What remains unknown, FRONTIER, unproved, or not cross-referenced?

## Checklist

- [ ] New ChatGPT work uses one unique branch/workstream per bounded package and an early draft PR.
- [ ] Actual changed paths are covered by the declared work intent.
- [ ] The intent is bound to the current PR base and base canonical source root/DesignEpoch.
- [ ] Textual merge success is not treated as semantic compatibility.
- [ ] Concurrent semantic collisions use a fresh integration branch with explicit comparison/receipt rather than cross-editing source branches.
- [ ] Canonical v15.5 files are not silently modified in place.
- [ ] Proposal/review/test evidence is not treated as authority or canonical promotion.
