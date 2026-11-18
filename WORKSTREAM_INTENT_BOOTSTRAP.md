# Temporary workstream bootstrap — removed after draft PR creation

GardenChatGPTWorkstreamIntent/v1
- repository: ankitdcx/garden-main
- branch: chatgpt/docs-onboarding-2026-11-18
- base_ref: main
- base_sha: ea538d5e934f3ddcf3a458a7dcbe96fd665dc46f
- work_package: Improve newcomer orientation, navigation, glossary, version history, contribution guidance, architecture visualization, and existing directory guides. Add scoped GitHub issue templates. Documentation-only; no canonical source edits.
- expected_paths:
  - README.md
  - OVERVIEW.md
  - GLOSSARY.md
  - VERSION_HISTORY.md
  - ARCHITECTURE.md
  - CONTRIBUTING.md
  - canonical/current/README.md
  - canonical/candidates/README.md
  - design_deltas/README.md
  - history/README.md
  - .github/ISSUE_TEMPLATE/config.yml
  - .github/ISSUE_TEMPLATE/specification-proposal.yml
  - .github/ISSUE_TEMPLATE/clarification-request.yml
  - .github/ISSUE_TEMPLATE/design-defect.yml
- dependencies: none identified; documentation links must resolve against current main tree.
- integration_strategy: one bounded branch; draft PR before substantive edits; validate links, YAML, Mermaid syntax and canonical-manifest immutability; merge only through protected PR.
- substantial_edit_started: false

AgentWorkIntent/v1
- base_sha: ea538d5e934f3ddcf3a458a7dcbe96fd665dc46f
- source_root: 63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598
- design_epoch: Garden-v15.5@63561ce9fcd4a72f44af333662b342fd18c4e99930209c30c5f801bcc5c74598
- changed_paths: same as expected_paths above
- affected_symbols: README navigation; canonical/current reader guide; candidate/delta/history reader guides; glossary entries; contribution issue categories; architecture overview.
- semantic_domains: repository navigation; documentation; provenance; candidate/canonical status; contributor process.
- invariants: canonical v15.5 source bytes and SOURCE_MANIFEST unchanged; candidate status never inferred as admission; specification/proof/implementation/validation/certification remain distinct; historical records preserved; all links point to existing paths.
- contracts: source-manifest identity; canonical/candidate/delta authority boundary; protected-PR merge path.
- intended_effect: improve discoverability and reader comprehension without changing Garden semantics, canonical authority, source files, or historical evidence.
