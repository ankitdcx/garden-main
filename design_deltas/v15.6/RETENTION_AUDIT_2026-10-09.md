# v15.6 redundancy and no-loss audit — 2026-10-09

**Result: NO SAFE DELETIONS CERTIFIED.** The proposed “keep v1.4 only” cleanup fails the first structural retention check. v1.0–v1.3 have distinct fields/requirements absent from the standalone v1.4 JSON. Later versions reference base process candidates and do not reproduce every earlier clause. Deleting earlier files without an explicit governed consolidation would lose material.

## Process-version chain

| File | Distinct content observed (not all reproduced in v1.4) | Disposition |
|---|---|---|
| GardenCanonicalUpdateProcess v1.0 | section_unit, review_profile, evidence_hierarchy, implementation_validation_modes, light_track, move_equivalence, successor_classification, human_availability, canonical_rollback, process_transition, config_surface_coupling | RETAIN AS VERSIONED SOURCE |
| v1.1 | opening_milestones, evidence_class_attribution, delta_dependency_semantics, rollback_trigger, sweep_scaling, human_permanent_unavailability, simplification_pressure | RETAIN AS VERSIONED SOURCE |
| v1.2 | step0_routing, review_packet, evidence_requirement_matrix, major_split, process_change_impact, lineage_unknown, rollback_window, promotion_capacity, enforcement_status, budget_routing, reviewer_scoring, pipeline_change_control, zero_delta_health | RETAIN AS VERSIONED SOURCE |
| v1.3 | enforcement_maturity, delegation_envelope, process_rule_change_authority, lane_inventory, budget_depletion, required_tests, required_review_before_admission | RETAIN AS VERSIONED SOURCE |
| v1.4 | major_simplification_gate, audit_ladder_base_case, verification_binding, pipeline_health_controls, lane_registry_derivation, free_only_cross_exam, execution_first_transition | LATEST VERSIONED CANDIDATE; NOT SELF-CONTAINED REPLACEMENT |

All listed files also contain shared metadata. Field presence is not a proof of semantic uniqueness, but field absence **disproves any claim that v1.4 alone contains the entire prior JSON contract verbatim**.

## Successor-Process-Hardening chain

The base plus V1.1–V1.4 each retain distinct `delta_set_id` and `findings`, `candidate_invariants`, `candidate_tests` packages. The final V1.4 has a smaller serialized body than the base; no full source-to-source semantic equivalence proof is available. **Retain all** until a source-qualified merged delta reproduces all accepted unique requirements, negative cases and tests.

## Large-file review

| File | Observed distinctive role | Decision |
|---|---|---|
| PENDING-RECONCILIATION-2026-09-15.json | Broad cross-source reconciliation, explicit source hashes, dispositions and canonical_effect=false | RETAIN historical reconciliation; no replacement proof |
| DELTASET-2026-09-15-ENGINEERING-HARDENING.json | Machine-readable V156-EH patterns, extension fields, invariants, tests and status | RETAIN candidate data |
| ENGINEERING-HARDENING-SPECIFICATION.txt | Detailed normative candidate T-EH anchors, exact predecessor owner locations, FunctionContract requirement profiles and implementation limits | RETAIN distinct source text; JSON does not automatically replace |
| PENDING-CONSOLIDATED-SPECIFICATION.txt | Cross-domain owner-bound pending clauses and process-lineage reconciliation, including human assurance | RETAIN pending working source pending exact comparison |

**Navigation:** dated pending indexes are historical tracking only; v15.11 retention ledger and current source packages are later navigation, not a certified replacement for every earlier disposition. The September 14 project-wide pending ledger is already visibly labelled HISTORICAL. No files were deleted, moved or reidentified in this audit.

## Release gate for future deletions
Before any removal: freeze byte hashes; enumerate every old atomic rule/schema/invariant/test/exception/unknown; map to an exact qualified successor span; prove retained semantics and applicability, record unresolved conflicts; independently challenge the mapping; only then remove an active duplicate while retaining Git history. **UNKNOWN ≠ PASS.**
