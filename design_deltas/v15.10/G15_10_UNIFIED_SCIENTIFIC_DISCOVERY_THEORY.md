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
- A 100-row generic two-state surrogate screening reported 70 PASS_TOY, 10 FAIL_TOY, 20 NOT_TESTABLE; all 70 purported scientific passes were **withdrawn**. Those surrogates did not implement the labeled physical domains. The consolidated ideas register retains the 70 statuses as FULL_TEST_BLOCKED / NOVELTY_UNKNOWN.
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
- Prior toy controls and withdrawn surrogate results are summarized in §6; historical source remains available in Git history.
- [Unified idea register](G15_10_ALL_SCIENTIFIC_IDEAS_REGISTER.md)

**Status invariant:** specification != proof != implementation != experimental validation != novelty != economic value != canonical admission.


## 10. G15.10-ABSTRACT-002 + H1 — Operational hardening (2026-10-11)

**Status:** NONCANONICAL, additive; no changes to 6 pillars / 10 objects / 24 relations / 7 forms. Supersedes no source semantics. The earlier `G15.10-ABSTRACT-001` architecture is treated as the conceptual view, `ABSTRACT-002` as the bounded operational contract, and H1 as the following corrections.

**Typed model:** S=(X,F,G,C,B,E): state space, transformations, interaction graph, constraints, boundaries/scope, evidence/provenance. This is a typed adapter to established physics and formal methods, not a new universal physical ontology.

**CGCD-001 executable contract:** Input=(source model, typed situation graph, frozen known-consequence ledger, target consequence class, budget). Output=(derived candidates, counterexamples, independent proof receipts, coverage gaps, rejections, unresolved). Every operator declares preconditions, deterministic or explicitly bounded algorithm, search ordering, candidate cap, time/memory/solver budget, failure status, and source/hash/assumption dependencies. No candidate may self-admit.

**Search:** normalize without unreported loss → enumerate admissible typed combinations → SAL checks → derive using established mathematical methods → compare to frozen coverage ledger → test equivalence/dependence → counterexample search → rank using declared utility and risk → independent check → record. Track pruned items, denominator, termination and `SEARCH_INCOMPLETE`. Do not claim completeness outside the frozen finite universe.

**H1 corrections:**
1. `LOSS_UNRESOLVED` blocks only derivation branches dependent on the missing/lossy semantics. Emit source-span-specific BLOCKED receipt; independent unaffected branches may continue.
2. Materiality must use an explicitly declared objective/utility, constraints and budget. High-impact actions still pass existing authority/human-effect gates; an AI-generated score alone cannot authorize an action.
3. Invalidated or revoked premises trigger dependency traversal. Downgrade exclusively dependent descendants to `UNKNOWN_PENDING_REVIEW`; preserve descendants with alternative valid proofs. Keep historical provenance and re-evaluate coverage.
4. Keep separate status axes: SPECIFIED, DERIVED, FORMALLY_PROVEN, EMPIRICALLY_VALIDATED, NOVELTY_SCREENED, USEFUL, ADMITTED; additionally INVALIDATED, REVOKED, BLOCKED and UNKNOWN_PENDING_REVIEW as appropriate. These are not a single automatic progression.
5. Independently construct/freeze reference obligations, planted omissions and decoys. Pre-register Garden heuristic, comparator, consequence type, budgets, stopping, contamination and proof checker. Distinguish *rediscovery recall* from scientific novelty.

**CGCD-BENCH-001:** For the first test, restrict to one consequence class (e.g., forward-invariant safety barriers). Arm A = strong domain specialist baseline; B = same checker with generic candidate ordering; C = same checker with GSL/typed-interface-coverage ordering. Match model, access, compute, certificate family and proof standard; disclose any structural heuristics also available to baselines. Primary endpoint = independently verified distinct missing consequences per fixed budget, with precision/recall, time, certified-region size and false-acceptance as secondary metrics. Run a separate interface/cross-domain test against *integrated* specialist baselines, not artificially siloed ones.

**Independence:** logical independence is relative to a declared model, domain and consequence language; algebraic restatements do not increase discovery count. Novelty and measured utility are separate from formal validity. Prior art includes bond graphs, port-Hamiltonian, Modelica/FMI, SOS/SMT/CEGIS, Lyapunov-Krasovskii, SINDy and symbolic regression.

## 11. Worked candidate — delayed thermal control interface (2026-10-11)

**Situation:** A heated physical component is regulated by a computational controller with delayed reaction. This is an *illustrative model-derived bound*, not an experimentally discovered physical law.

Let x(t)=T(t)-T_ambient be temperature rise. In a bounded operating regime, assume:
- While the controller has not reacted, the worst-case temperature rise rate is `dx/dt <= r_pre`, with `r_pre > 0`.
- A dangerous temperature threshold is `x_max`.
- Detection plus computation plus communication plus actuation take at most `tau` seconds.
- After reaction, a controller ensures `dx/dt <= 0` whenever at/above the intended safety region, under stated actuator authority and disturbances.
- Initial state `x(0) <= x_max - r_pre*tau`; no unmodeled heating or actuation saturation outside those assumptions.

**Derived interface safety margin:**

`h(x)=x_max-x-r_pre*tau`.

Before effective control, integration gives `x(t) <= x(0)+r_pre*t` for `0<=t<=tau`. Thus `x(t)<=x_max` during delay. After effective control, non-increase ensures `x(t)<=x_max` thereafter. Therefore the sufficient *initial* safety obligation is:

`x(0) + r_pre*tau <= x_max`.

This is **not** a time-invariant claim that `h(x(t))>=0` throughout delay; only the physical threshold `x(t)<=x_max` is guaranteed. For repeated delay episodes, the margin must be re-established at each episode, including controller state and queued actions.

**Counterexample:** If `x(0)=x_max-r_pre*tau+epsilon` and heating equals `r_pre` for the full delay, then `x(tau)=x_max+epsilon`; the safety condition fails. If delay exceeds `tau`, heating exceeds `r_pre`, or post-actuation nonincrease fails, the proof does not apply.

**Garden mapping:** THING=heated component/controller/sensor; TIME=latency; SPACE=physical location; EVENT=threshold detection; ACTION=command/cooling; AGENCY=operator/controller authority only when applicable; RULE=thermal bound and safety limit; VALUE=avoid overheating; CONTEXT=ambient/actuator limits; CLAIM=conditional safety guarantee. GSL relations `dependsOn`, `causes`, `controls`, `governs`, `derivedFrom`, `supports` track the physical-computational interface. No invented physical agency.

**Candidate gap:** A physical-only coverage ledger may contain `x<=x_max` and a cooling-rate limit but omit the cross-interface obligation `r_pre*tau <= x_max-x(0)`. CGCD could flag it through TIME × ACTION × RULE × CONTEXT coupling. This is an example of a *missing obligation relative to a particular ledger*, not evidence that specialists have overlooked the bound.

**Prior art:** delay margins, thermal safety and reachability bounds are well-established classes. No exhaustive technique/application literature search or independent domain validation has been performed; `NOVELTY_UNKNOWN`, `EMPIRICAL_UNKNOWN`, `GARDEN_ADVANTAGE_UNKNOWN`.

**Experiment:** compare A (delay-aware thermal/reachability baseline), B (generic consequence search), C (typed-interface CGCD) on independently prepared models with hidden latency constraints and decoys. Measure valid omissions recovered per equal compute budget and false positives. Do not use a delay-free baseline as the sole comparator.

**Status:** DERIVED under assumptions; analytically checked by integration, not machine-checked in this turn; no validated scientific novelty or measured practical benefit.


## 12. G15.10-GSH-001 — Frozen candidate search policy (2026-10-11)

**Status:** NONCANONICAL / SPECIFICATION FROZEN FOR INITIAL IMPLEMENTATION; not implemented, benchmarked or admitted. This is a search policy within CGCD-001, not a new core module or a substitute for domain solvers.

**Contract:** `GSH(S,K,L,W,B) -> ordered Candidate stream + PruningReceipts + SEARCH_INCOMPLETE/COMPLETE`. S=typed semantic/structural model, K=frozen known-consequence and coverage ledger, L=frozen mathematical template library and optional training-only motif records, W=declared objectives/normalized weights, B=hard budget (time, memory, candidate and solver-call limits). Deterministic under frozen versions/seeds. No proof, novelty or admission status can be emitted by ranking.

**Initial executable scope (three of seven Forms):**

| Form | Candidate template | Proof obligation | Applicability |
|---|---|---|---|
| STATE | `x_i >= 0` | For continuous locally Lipschitz dynamics and an appropriate domain, check inward-pointing vector field at `x_i=0` along the candidate boundary, with other active constraints accounted for | Declared real-valued state and positivity requirement |
| RULE | `a^T F(x)=0` for candidate constant vector a | Independently prove zero Lie derivative throughout declared domain; for polynomial F use coefficient matching or symbolic/SMT methods | Continuous dynamics and candidate linear conserved quantity |
| RELATION | `h_ij(x_i,x_j)>=0` across actual graph edge | Check boundary viability/derivative or applicable compositional barrier conditions for full coupled dynamics | Declared coupling edge, typed state and safety semantics |

CONSTRUCT, CONTRACT, PROCESS and PROJECTION remain mapped to *families* but have **no executable templates in this initial freeze**. Do not claim seven-family implementation.

**SAL / typing minimum:** Verify referenced state variables exist; units/dimensions match each expression; relation endpoints and actual coupling are present; physical THING is not assigned intentional AGENCY; assumptions and boundary semantics are declared. Reject only demonstrably invalid candidates, proven duplicates and out-of-scope templates. UNKNOWN and low-priority safety obligations are retained in a quarantine ledger, not silently discarded. Do not use arbitrary universal exclusions such as all CLAIM-to-CLAIM causal relations being invalid without source-supported semantics.

**Scoring (frozen baseline):** `H(c)=w_m*M+w_g*G+w_u*U+w_t*T-w_r*R-w_c*C`. Every feature is predeclared on [0,1]: M=declared objective relevance, G=actual interface/coupling relevance, U=gap in preexisting coverage ledger, T=availability of a known verification path, R=verified or likely dependence on known candidates, C=normalized estimated checker cost. Weights, tie-break order and normalization are frozen *before held-out evaluation*; scores rank attempts and do not estimate probability of truth. Any learned `P(success)*DeltaU/cost` score is a separately trained, preregistered future ablation, not a requirement for GSH-001.

**Execution:** Generate typed template instances from actual model variables and edges → SAL filter → remove provable duplicates → rank → allocate bounded best-first search with a reserved exploration quota for admissible low-ranked/safety-tagged candidates → cheap sampled falsification (rejection only when genuine counterexample is independently checked) → domain solver → independent proof checker → ledger update. Sampling alone cannot establish validity. Return `SEARCH_INCOMPLETE` when budget expires with unvisited candidates. Store pruned, deferred and failed candidates, reasons, scores, dependency and cost receipts.

**Verification and independence:** Checker, not heuristic, decides mathematical validity; use model-appropriate SOS/SMT/CEGIS/symbolic tools and declare proof semantics (including delta-complete caveats). Count distinct consequences only after classifying EQUIVALENT, DERIVED_FROM_KNOWN, INDEPENDENT_WITHIN_DECLARED_CLASS or DEPENDENCE_UNKNOWN relative to a frozen language/domain/known set. UNKNOWN is never counted as an independent finding.

**CGCD-BENCH-001 four-arm ablation:**

- A: strongest relevant specialist solver/search (including sparsity, cheap falsification and other standard optimizations).
- B: generic structural candidate ordering with the *same* solver/templates/structural inputs.
- C: Garden semantic typing and frozen coverage-aware ordering without historical retrieval.
- D: C plus frozen cross-situation typed-signature motif retrieval; an untyped-signature retrieval control is required.

Use independent held-out model families, leave-one-family-out evaluation for D, sealed planted obligations/decoys for *rediscovery recall* only, fixed hardware/time and solver budget, equal information access and independent checking. Primary: independently certified systems or distinct valid obligations per fixed budget, chosen before execution for each benchmark; secondary: time-to-certificate, precision/recall, certified-region volume and false-acceptance. Report uncertainty, contamination, and all null/negative results. A hidden known obligation is not evidence of novel science.

**Interpretation:** C>B supports a semantic-routing effect; D>C supports retrieval value; equality or reversal fails to show added value on tested families. None of these by itself establishes scientific novelty, real-world model fidelity, or universal capability.

**Freeze boundary:** No additional ontology, module, patch version, or architecture expansion is needed before the minimal templates, type predicates, ledger, ranker, solver/checker interfaces and benchmark are implemented and executed.
