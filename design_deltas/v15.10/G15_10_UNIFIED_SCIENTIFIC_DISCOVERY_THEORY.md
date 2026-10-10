# Garden v15.10 — Unified Physical and Scientific Discovery Theory
**Document:** G15.10-SCI-DISC-UNIFIED-001  
**Date:** 2026-10-10  
**Status:** NONCANONICAL RESEARCH CANDIDATE; NO VERIFIED SCIENTIFIC NOVELTY OR GARDEN ADVANTAGE  
**Scope:** Consolidates the scientific-discovery discussion and design deltas of 2026-10-10. Does not supersede Garden v15.5 canonical source.

## 0. Executive statement

The central hypothesis is **coverage-guided consequence discovery**: given a specified physical model, its typed components, governing rules, and an inventory of what has already been analyzed, systematically enumerate meaningful combinations and derive obligations/consequences that existing analyses have not covered. This is distinct from (a) free-form idea brainstorming, (b) merely listing familiar conservation laws, and (c) transferring a known analogy from another domain.

The user's original 80–90% covered / 10–20% missing intuition came from v15.10 semantic-coverage work. These percentages are **not measured completeness rates for physical science** and cannot be assumed to generalize. The testable claim is whether bounded coverage-guided search finds more *valid, useful, genuinely uncovered* consequences than strong conventional methods at matched budget.

## 1. Existing architecture and boundary

Preserve six GSL Pillars: Existence, Change, Agency, Law, Value, Frame. Preserve ten Core Objects: TIME, SPACE, THING, EVENT, ACTION, AGENCY, RULE, VALUE, CONTEXT, CLAIM. Preserve 24 Core Relations and seven Forms (CONSTRUCT, CONTRACT, STATE, RELATION, PROCESS, RULE, PROJECTION), as specified by V15_10_ABSTRACTION_GCSC_DELTA.md. Preserve existing source ownership, GCSC/SAL/SAC, status gates and no-self-admission.

Physical models are **typed projections/adapters**, not a second fundamental ontology. A physical molecule, field, or network does not acquire intentional agency or authority from representation. Use established mathematical machinery: differential equations, stoichiometry, bond graphs, port-Hamiltonian systems, Modelica/FMI, symbolic algebra, SOS/SMT/CEGIS, and domain models.

## 2. Three kinds of invariants

1. **Fundamental:** conservation laws, symmetries, thermodynamic conditions, within their domains of validity; generally known.
2. **Derived/system-specific:** consequences of particular dynamics, topology, boundary/initial conditions, parameters, and coupling; mathematically checkable, potentially unrecognized for a particular model.
3. **Empirical:** observed regularities over defined conditions; require calibrated measurements, uncertainty and independent validation, not merely a symbolic derivation.

An invariant may be an equality, inequality, preserved set, barrier, conserved integral, monotonicity condition, or constrained reachability property. A candidate does not become a new physical law by being derivable.

## 3. Main proposed operator: Coverage-Guided Consequence Discovery (CGCD-001)

**Inputs:** formal physical model M (equations, variables, units, frames, ports, graph, initial/boundary conditions, assumptions, validity domain); situation decomposition and typed relations; coverage ledger L of previously analyzed obligations/consequences with provenance; target observable, safety/decision question, and fixed search budget.

**Output:** versioned candidate consequence record with proof obligation, exact derivation or conditional claim, distinguishing prediction, counterexample search, baseline, prior-art status, evidence requirements and rejection receipt.

**Algorithm candidate:**
1. Import model source faithfully and emit translation/loss receipts. Source formalism remains authoritative.
2. Construct a typed dependency/interconnection graph from actual equations, not a vocabulary-only map.
3. Enumerate bounded, physically admissible combinations of components, states, interfaces, boundaries and constraints; prune impossible or irrelevant combinations with explicit reasons.
4. For each admissible combination, derive its *required consequences or proof obligations*: conservation balance, interface flux consistency, conditional symmetry, monotonicity, reachable-set boundary, safety invariant, observation sufficiency, or coupling-specific constraint. Require mathematical justification; an unexplained suggestion is not a derived invariant.
5. Compare with L: classify COVERED, EQUIVALENT, INCONSISTENT, NOT_APPLICABLE, or GAP_CANDIDATE. UNKNOWN is not PASS. A gap in the ledger is **not proof of novelty in the literature**.
6. Rank unresolved consequences by materiality, test discrimination, independent evidence availability, expected benefit, cost and uncertainty. Freeze ranking before scored tests.
7. Attempt formal derivation and counterexample search; where possible produce a machine-checkable proof/certificate. A mathematical proof about M does not establish M accurately describes the world.
8. Search technique-level and application-level prior art, including near-duplicates and specialist practice; retain query/date/corpus receipts.
9. Run held-out tests versus the strongest relevant specialist baseline and generic automated search, using matched data, parameterization, solver budget and compute.
10. Independent checker/reviewer records PASS, FAIL, UNKNOWN, or NOT_APPLICABLE separately for mathematical correctness, empirical fit, novelty, and value. Never allow generated outputs to admit themselves.

**Specific potential Garden contribution:** search *coverage of typed interface obligations*, especially missing interactions among subsystems. This must be implemented as a concrete deterministic heuristic and ablated against generic search; otherwise the proposed contribution is only a checklist.

## 4. Supporting operator: PHY-XFER-003

Cross-domain transfer is a secondary source of candidate constraints. Import established models, enumerate bounded type/port/unit-compatible mappings, verify source assumptions in the target, derive a target-specific falsifier, then screen against technique and application prior art. Structural similarity is not physical validity. The full specification and risk-labeled hypotheses remain in G15_10_PHY_XFER_003_CONSOLIDATED_CANDIDATE.md.

## 5. Evaluation protocol — test the original argument directly

**Primary coverage benchmark:** Supply each arm with identical real or independently generated physical models and a *frozen coverage ledger* containing some deliberately omitted, mathematically valid obligations, plus decoy gaps. Hidden answer keys must be separated from generation. Test whether Garden-guided search identifies *valid uncovered consequences* more efficiently than standard algebra/verification and ordinary AI/generic-search baselines.

**Arms:** A strongest domain-specific solver/method; B same solver with generic candidate ordering/search; C same solver with CGCD typed interface-coverage ordering/search. Same source model, observations, search space where applicable, candidate budget, compute, and proof checker.

**Primary metric:** precision/recall or valid unique uncovered obligations found per fixed compute budget on held-out models. **Secondary:** time-to-first-valid, number of verified distinct consequences, certified-region size where relevant, false-positive rate, experimental discrimination, net decision value.

**Test partitions:**
- Linear stoichiometric networks: null-space analysis as complete calibration for linear conservation; no expected advantage in completeness.
- Polynomial dynamics: Darboux/Lie/symbolic algebra and SOS/SMT/CEGIS baselines.
- Nonlinear inequality/safety constraints: SOS/SMT/CEGIS, compositional barriers and domain specialist methods; focus on structured interfaces, nonpolynomial dynamics, and high-dimensional cases.
- Cross-domain transfers: historical rediscovery with dated sources and decoys, followed by held-out value trials.
- Empirical applications: independent datasets, realistic measurement noise, calibration and non-shared data-generating models to avoid inverse crime.

Pre-register benchmark selection, effect threshold, confidence/multiplicity procedure, stopping budget, contamination controls and independent evaluator. A logged-out ChatGPT one-shot comparison showed competent mathematical hypothesis generation without Garden context, but is **not** a controlled clean-room experiment.

## 6. Corrections and negative findings

- Early lists of lithium-battery and chemical-network invariants enumerated known fundamentals. Failure to find new ones manually does not bound automated search.
- Ten physical-science ideas and approximately 22 analogy candidates were speculative; novelty not verified.
- Kibble–Zurek/neural training pilot was reported as 70 runs, no dead neurons: a limited negative pilot, not a test of an established critical transition.
- A toy two-dimensional disk invariant was correctly concluded but had a sign-convention error in one write-up. For h=x²+y²−1<=0 and dynamics xdot=−x+y², ydot=−y: Lie(h)=−2(x²+y²)+2xy²; on the boundary Lie(h)=−2(1−xy²)<0. For g=−h>=0, Lie(g)>0.
- A later 100-system analytic control reported 99 sufficient-condition certificates and one inconclusive case; these were constructed related systems, not 99 discoveries.
- INV-DISC-100 contains **10 technique motifs × 10 domains**, not 100 independent inventions. Some cells are not applicable. It is an archived candidate universe.
- A 100-row generic two-state surrogate screening reported 70 PASS_TOY, 10 FAIL_TOY, 20 NOT_TESTABLE; all 70 purported scientific passes were **withdrawn**. Those surrogates did not implement the labeled physical domains. INV_DISC_070_FULL_TEST_READINESS_AND_PRIOR_ART.md records all 70 as FULL_TEST_BLOCKED / NOVELTY_UNKNOWN.
- The high-stakes physical examples (grid delay, PFAS breakthrough, water leak detection, robot heating, battery charging) have dense relevant prior art. No individual result has passed novelty plus matched-baseline plus independent evidence gates.
- Temporal source masking does not erase a pretrained model's latent knowledge. Hashes/receipts detect provenance and changes, not guarantee historical blindness.
- Estimated grid savings in prior discussion were hypothetical scenarios, not demonstrated Garden benefit.

## 7. Specific next experiment

**CGCD-001-A:** choose a publicly specified, structured network with exact dynamics and a frozen analysis-coverage ledger. Plant genuinely derivable but withheld interface consequences and plausible decoys. Implement typed interface enumeration and derivation, plus identical-budget generic search. Use independent symbolic/SMT checking; test precision/recall and cost. Avoid cherry-picked easy systems. Only after this controlled result proceed to INV-035 grid delay or PFAS column field-data comparisons.

**INV-035** remains a candidate for physical application, not a replacement for testing CGCD's central mechanism. Its proper comparator is an established *delay-aware* Lyapunov–Krasovskii or other appropriate specialist method, not a weak delay-free controller.

## 8. Research ledger status

Theory specified: YES. Formal implementation of CGCD: NO. Controlled CGCD-vs-baseline trial: NO. Independently verified new physical invariant: NO. Empirically novel invention: NO. Measured Garden economic gain: NO. No canonical admission. Future results must update status per claim and preserve all failures.

## 9. Linked sources

- [v15.10 abstraction/GCSC](V15_10_ABSTRACTION_GCSC_DELTA.md)
- [PHY-XFER-003 consolidated candidate](G15_10_PHY_XFER_003_CONSOLIDATED_CANDIDATE.md)
- [INV-DISC-001 lessons and control](INV_DISC_001_LESSONS_AND_CONTROL_RESULTS.md)
- [INV-DISC-100 original universe](INV_DISC_100_CANDIDATE_PORTFOLIO.md)
- [INV-DISC-070 withdrawal audit](INV_DISC_070_FULL_TEST_READINESS_AND_PRIOR_ART.md)
- [Unified idea register](G15_10_ALL_SCIENTIFIC_IDEAS_REGISTER.md)

**Status invariant:** specification != proof != implementation != experimental validation != novelty != economic value != canonical admission.
