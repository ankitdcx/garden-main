# Garden v15.10 scientific discovery — gap-closure evidence

Date: 2026-10-09
Status: NONCANONICAL / SCIENTIFIC RESEARCH / NOT DISCOVERY

## Scope and limitations
This addendum does NOT claim to fix all 100 scientific candidates. The 100 proposals remain largely un-derived; novelty is unverified. The current evidence repairs one important benchmark comparator weakness for Candidate 026.

## Candidate 026: noise-aware output-error comparator
- Synthetic source: `garden_candidate026_harness.py` (unchanged reference generator).
- New comparator: `garden_candidate026_strong_comparator.py`.
- Fits one-body and two-body thermal RC state-space models to noisy observed temperature using least squares of **simulation output**, not regression on noisy lagged outputs.
- Zero-order-hold discretization, positive capacities and conductances via log parameters, fitted initial temperatures, one fixed starting point per model, SciPy `least_squares` with parameter bounds.
- Selection rule: training BIC(two-body) <= training BIC(one-body)-10. Held-out MSE reported separately and not used to select model.
- Noise sigma=0.012, 20 null + 20 hidden-state synthetic cases: 0/20 false selections; 20/20 detections.
- Noise sigma=0.024, 12 null + 12 hidden-state synthetic cases: 0/12 false selections; 12/12 detections.
- These counts are finite-sample results, not guarantees; comparator is given both candidate model families, so it is not a blind scientific discovery benchmark.
- The earlier ARX result (3/100 null false positives after calibration) remains as a historical diagnostic; it is no longer presented as the best baseline.

## Corrections to prior claims
- Keyword-based mechanism hints are NOT residual-driven discoveries.
- '100 distinct diagnostics' is false. 100 entries are research prompts; only ten contain worked mathematics.
- Candidate 017: positive Arrhenius log-rate curvature under constant positive prefactors and fixed barriers.
- Candidate 041: information-theoretic conditioning inequality does not supply an implementable closure without a forecast of the conditioning variable.
- Candidate 072: infection-age model is established, not unresolved as a mathematical mechanism.
- Candidate 026: two-body RC physics is established. No claim of scientific novelty.

## Explicit pending gates
1. Global literature novelty search for 100/100: NOT DONE.
2. Strongest current domain-specific baselines for 100/100: NOT DONE.
3. Full dimensioned TheoryEquationContracts for remaining 99: NOT DONE.
4. Blind residual-driven mechanism identification on unseen problems: NOT DONE.
5. Real-world held-out experiments: NOT DONE.
6. TREE_CORE build integrity, CRC, schema and deterministic compilation repairs: NOT DONE.
7. Multiplicity-adjusted registered primary endpoints for a shortlisted candidate set: NOT DONE.

## Proposed acceptance gates
- G0: Pin current baseline theory and strongest alternatives.
- G1: Define projection and find independent physical states with same projected state but different futures.
- G2: Diagnose residual without title or mechanism leakage; report UNKNOWN when insufficient.
- G3: Derive typed equations with units, limits, identifiability, conservation and positivity checks.
- G4: Compare against noise-aware state-space and domain-specific baselines, with held-out forcing and matched budget.
- G5: Search literature for novelty; downgrade rediscovered results to known mechanisms.
- G6: Pre-register signed/magnitude predictions, multiple-comparison controls and independent replication.
- G7: Human-reviewed scientific status; no self-admission or overwrite of controlling Garden sources.

## Reproduction
From this directory with NumPy and SciPy installed:
`python garden_candidate026_strong_comparator.py --n 20 --output garden_candidate026_strong_results.json`
`python garden_candidate026_strong_comparator.py --n 12 --noise 0.024 --seed 20000 --output garden_candidate026_strong_results_high_noise.json`

The harness imports `garden_candidate026_harness.py` for synthetic trajectory generation. Numerical results may vary with dependency versions; reproducible pinned environments are a future gate.