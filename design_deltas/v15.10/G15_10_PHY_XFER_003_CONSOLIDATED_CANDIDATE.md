# G15.10-PHY-XFER-003 — Physical Invariant Transfer Consolidation

**Status:** CANDIDATE / NONCANONICAL / NOT IMPLEMENTED / NOT VALIDATED  
**Date:** 2026-10-10  
**Lineage:** PHY-XFER-001 + PHY-XFER-002 + critical reviews + conceptual candidate register.  
**Authority:** v15.5 remains canonical; this document does not amend it.

## Summary

Physical abstraction does not require a second fundamental ontology. Reuse established bond graphs, port-Hamiltonian systems, Modelica/FMI, differential-equation models and measured data. Garden adds *candidate* (A) physical-model adaptation, (B) cross-domain invariant/constraint transfer, and (C) novelty, evidence and value discrimination. Discovery advantage is unproven.

Preserve v15.10's six pillars, ten objects (TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM), 24 relations, seven forms and GCSC/SAL/SAC. Physical objects are typed facets, not autonomous agents. No self-admission.

## A. Physical model adapter

`PhysicalModelRecord`: model_id/version, source_ref/hash/span, owner/status, formalism, typed graph/ports, equations, variables, units/frames, states/transitions, boundary/initial conditions, assumptions/validity, uncertainties, evidence_refs, conservation/constitutive constraints, translation_map, round_trip_tests, loss_report.

Translation never outranks its source. Require pre-registered observable equivalence margins, round-trip checks and explicit LOSS_UNRESOLVED for unsupported or lossy conversions. Dimensional agreement is necessary but insufficient.

## B. Transfer operator (bounded candidate algorithm)

1. Parse source and target into deterministic, typed, unit-annotated dependency/port graphs.
2. Canonicalize variables, units, boundary conditions, dynamics and constitutive assumptions.
3. Enumerate partial mappings with bounded graph matching (VF2 is an implementation option). Prune by types, ports, units and assumptions; prioritize conservation, storage/dissipation, then weaker analogies. Record *all* attempted mappings and the candidate cap.
4. Verify the source theorem's assumptions in the target, or explicitly condition the prediction. Conservation/passivity/entropy gates apply only when independently justified for that model.
5. Transfer a specific constraint, equation, failure mode or control technique; derive a falsifiable prediction against the strongest named target baseline. Without discrimination, label non-actionable analogy.
6. Rank deterministically by pre-registered discrimination, uncertainty, test cost and plausibility under a fixed budget. Record formula, seeds, rankings and rejected cases.
7. Emit `CandidateTransferRecord`; structural correspondence is not empirical evidence.

`CandidateTransferRecord`: source/target IDs, mapping, assumptions/applicability, transferred statement, rank/score, predicted residual, falsifier, baseline, test/budget, full search denominator, prior_art_technique, prior_art_application, prior_art_coverage (date/corpora/queries/gaps), physics/novelty/value/review statuses, receipts, decision/rationale.

Use PASS / FAIL / UNKNOWN / NOT_APPLICABLE distinctly; UNKNOWN is not PASS.

## C. Novelty, experiment and economic discriminator

Prior-art screening covers *both* the technique and its target application, including research, patents, standards and practice. Incomplete coverage => NOVELTY_UNKNOWN. Compare against strong specialist and generic-search baselines with matched information, compute and parameters. Require calibration, uncertainty, held-out observations, explicit falsifiers and negative results. No hypothesis is a discovery or verified economic gain without independent external evidence.

For value: sourced opportunity base × measured effect × plausible adoption minus implementation, operation, measurement, compute, safety and maintenance costs; report uncertainty and sensitivity. Do not substitute speculative annual savings for evidence. Science-register G0–G9 remain controlling; no parallel admission path.

K-INT-001 and K-INT-009 references are **UNVERIFIED SOURCE BINDINGS** until exact authoritative source/span/hash is pinned. Independently enforce observation ≠ validated knowledge and prediction ≠ evidence as local requirements.

## Benchmark / acceptance

**Test A (rediscovery):** Before runs, freeze ≥20 dated historical successful transfers **and ≥20 plausible invalid/decoy transfers**, inclusion criteria, source/answer separation, baseline, thresholds and search budget. Use a deterministic model-free operator where possible; report residual designer/training contamination. Score recall@10, precision@10, false positives, rank, time and complete enumeration. No positive-only survivorship evaluation.

**Test B (incremental value):** Calibrate on known electrical RC↔thermal RC, hydraulic↔electrical, battery thermal↔industrial heat-transfer pairs; these are *not novel*. Add at least one independently selected non-obvious pair, frozen before outcome inspection. Three arms: specialist; specialist+generic search; specialist+Garden transfer. Primary endpoint: held-out predictive error, with matched budget. Secondary: false discoveries, test cost, decision/economic value. Preregister effect size, equivalence margin, power, multiple-comparison family/FDR, stopping rule and independence class. Test B is gated on preregistered Test A success. No universal arbitrary success percentage is adopted.

PHY-001..010 remain required: translation equivalence, unit/frame rejection, conditional physical counterexamples, known prior-art control, UNKNOWN control, matched baseline, negative value control, independent reviewer, regression, and blind incremental value. A headline result requires blinded domain-expert or different-family evaluation with disclosed common dependencies.

## Unverified hypothesis inventory (NOT operator outputs)

The following ideas arose from conceptual discussion, not executed code, literature screens, or passed physics checks. All novelty and physical admissibility statuses are UNKNOWN:

1. Marangoni fingering → tumor invasion; capillary-gravity scaling cannot be imported without deriving the active-tissue mechanism.
2. Anderson localization → T-cell receptor signaling; coherent-wave assumptions may fail in stochastic dissipative membranes.
3. Vortex depinning → cell migration in ECM; active adaptation may smear a critical threshold.
4. Kibble–Zurek → neural-network training defects; learning-rate changes are not automatically thermodynamic quenches.
5. FDT violation → tumor microrheology; active-matter prior art likely relevant.
6. Variable-range hopping → biomolecular charge transport; strong prior-art risk.
7. Tracy–Widom → wildfire extremes; random-matrix edge mechanism not established.
8. BKT → epithelial monolayer transition; nonequilibrium applicability unknown.
9. Griffiths rare regions → epidemic heterogeneity; contact-process literature likely relevant.
10. Keldysh → driven quantum biology; existing open-quantum-system methods require comparison.
11. Nematic defects → wound healing; substantial prior art.
12. Random-matrix spectral statistics → transformer dissolved-gas noise; ensemble undefined.
13. KPZ → bacterial colony expansion; likely known.
14. Percolation → neuronal ion-channel clustering; likely known.
15. Spin-glass models → protein conformations; likely known.
16. Viscous fingering → tumor morphology; likely known.
17. Spinodal decomposition → biomolecular condensates; established.
18. Turing patterns → vegetation; established.
19. Kuramoto → circadian coupling; established.
20. Lévy flights → foraging; established.
21. Self-organized criticality → neural avalanches; established.
22. Adaptive network switching → battery cooling/transport under actuator budget; adaptive thermal management already exists, exact residual unknown.

These are **unverified input hypotheses**, not four or twenty validated discoveries. No novelty ranking based on mental generation is accepted as a result.

## Physical telemetry (future, not connected)

Potential battery evidence: calibrated EIS; synchronized voltage/current/capacity cycling; spatial thermal mapping; mechanical degradation/strain; operando XRD/CT where appropriate. EIS interpretation is model-dependent; XRD/CT alone do not directly establish local lithium concentration. All sources require provenance, calibration and uncertainty. No data feed is connected by this patch.

## Receipts, rollback, next action

Keep source hashes, exact mappings, unit/assumption checks, all candidates and rejections, budget/seeds, baselines, preregistration, independent reviews and final decisions. Existing Garden source ownership, human-effect safeguards, GCSC/SAL/SAC and no-self-admission remain unchanged. Rollback disables optional PHY-XFER machinery.

**Completed:** consolidated candidate specification and risk-labeled idea inventory.  
**Not completed:** executable operator, frozen benchmark, tests, validated novelty, measured savings.  
**Next:** implement bounded typed-graph operator; freeze Test A positives+decoys; execute and publish receipts; only then consider Test B. Stop conceptual expansion until a concrete test failure warrants revision.


## 2026-10-10 follow-up — separate within-system discovery track

The research discussion distinguished (1) fundamental invariants, (2) derived model-specific invariants, and (3) empirical regularities. PHY-XFER transfers constraints **across** models; [INV-DISC-001](G15_10_UNIFIED_SCIENTIFIC_DISCOVERY_THEORY.md) tests whether structural guidance helps discover invariants **within** one model. It is a separate noncanonical research candidate, not an expansion of PHY-XFER's admission status.

A previous write-up confused the derivative sign for the unit disk. For g=x²+y²−1<=0, dg/dt=−2(x²+y²)+2xy²<0 on the boundary; the positive derivative belongs to h=−g>=0. The conclusion of forward invariance survives the correction. A reproducible 20-case SymPy sufficient-bound control was executed; 20/20 cases passed. This is a deliberately easy positive control, **not** a Garden search success, SOS/SMT comparison, independent certification, or new discovery. See the INV-DISC-001 file and script for exact method and limitations.

Claims that dated source restrictions and provenance watermarking guarantee historical blindness are **not supported** for pretrained models. Source-bound controls and leakage audits remain required; named legacy K-INT/v10.25 controls are unverified unless pinned to authoritative source spans.
