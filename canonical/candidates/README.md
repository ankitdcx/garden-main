# Whole-release candidates

**Noncanonical.** This directory holds complete five-file Garden successor *working candidates*, currently [v15.6](v15.6/README.md) and [v15.7](v15.7/README.md). The only canonical controlling source remains [v15.5](../current/README.md).

The similarly named [design_deltas/v15.6 and v15.7](../../design_deltas/README.md) folders hold **supporting incremental candidate patches, process drafts, recovery notes and evidence**, not duplicate full releases. Keep both types; later directory names do not grant admission or prove no-loss equivalence.

Read `CURRENT_CANDIDATE.json` as a pointer to the most recently selected full working candidate, **not** the canonical current. Each candidate's `SOURCE_MANIFEST.json` declares file names, sizes and hashes. The manual integrity checker can verify those declarations; a matching hash does not prove semantic correctness or admission.
