# Bounded EDCR reference qualification

Run `python scripts/qualify_context_routing.py`. Receipts cover deterministic local source-sensitive deduplication, bounded context, provenance/contradiction/freshness handling and the shared completion executor’s conservative budget/recovery paths. Provider responses in tests are explicitly fixtures. No external provider was called; no frontier quality or cost benchmark is claimed.

Existing owner anchors: Technical `[T-PROCESS]`, `[T-KNOWLEDGE]`, `[T-EVENT-CONTRACT]`, `[T-FUNCTION-CONTRACT]`, `[T-PROVENANCE-EXT]`. This indexed observation view creates no new truth or authority owner. Model outputs remain unverified proposals.

Dispatch seam: `CompletionStore.claim` then mandatory `ContextRouter.validate_claim` in the trusted public specialist adapter with explicit trusted closure/source binding immediately before its one provider call; frontier_request creates a separate manual ChatGPT request after specialist completion; `CompletionStore.finish` handles accounting/unknown outcome. The reference does not activate or qualify a live public adapter.
