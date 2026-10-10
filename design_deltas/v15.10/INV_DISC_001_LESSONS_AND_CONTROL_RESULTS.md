# INV-DISC-001 — Lessons, scope and initial test receipt

**Status:** NONCANONICAL RESEARCH; CONTROL TEST RUN, NO DISCOVERY VALIDATED
**Date:** 2026-10-10

## What changed

The physical-discovery program distinguishes:
1. Fundamental laws (usually established).
2. System-specific derived invariants from dynamics, topology and constraints.
3. Empirical regularities that require calibrated observations.

Cross-domain analogy generation (PHY-XFER) is not the same as within-system invariant discovery (INV-DISC). The latter is the active benchmark direction. Previous lists of ten or more engineering 'invariants' often restated mature state-estimation, barrier, and monitoring methods. Idea generation is not novelty or proof. No generator self-rating is evidence of novelty.

## Testable Garden contribution

A Garden-guided candidate generator must explicitly convert models into typed objects, relations, admissible situation combinations and constraint motifs, and must produce a logged candidate ordering that differs from a generic-search arm. Without an executable generator, there is no Garden-vs-baseline experiment.

A: strong specialist baseline (SOS/SMT/CEGIS, appropriate to system).
B: same verification stack + generic candidate generation.
C: same verification stack + Garden-guided structural candidate generation.
Match information, CPU/solver time, parameter/template degrees, and evaluation data. Independently check every candidate certificate. Pre-register primary valid-certificate rate and secondary time, certified-region size, compute and false-acceptance rate; false certificates must never be accepted. Include held-out structured systems and decoys; disclose any training contamination. A known benchmark such as BarrierBench may be evaluated after confirming its exact contents, license, and contamination exposure.

## Correct positive control

Dynamics: xdot=-x+y^2, ydot=-y.
For h=x^2+y^2-1<=0, Lie(h)=-2(x^2+y^2)+2*x*y^2=-2(1-x*y^2) on the boundary.
Thus Lie(h)<0 because max_{x^2+y^2=1} x*y^2=2/(3*sqrt(3))<1.
For the opposite convention g=1-x^2-y^2>=0, Lie(g)>0. Mixing the sign conventions was an error in the prior summary. This analytic proof is a mathematical positive control, not a novel finding or an SMT proof.

## Executed preliminary control (2026-10-10)

Executable: [inv_disc_001_100_controls.py](inv_disc_001_100_controls.py).
100 parameterized systems xdot=-a*x+b*y^2, ydot=-c*y, candidate ellipses x^2/A^2+y^2/B^2<=1.
For u=x/A,v=y/B on the ellipse boundary, Lie(h)<=-2*a*u^2-2*(c-|b|*B^2/A)*v^2.
Under a>0 and c>|b|B^2/A the candidate ellipse is forward invariant.
Actual local SymPy run: **100 tested; 99 certified by this sufficient condition; 1 INCONCLUSIVE**. The inconclusive case is not a disproved invariant. This is a narrow related family with constructed certificates, not 100 independent discoveries or an empirical validation. No baseline/Garden comparison was run.

## Candidate portfolio

[INV-DISC-100](INV_DISC_100_CANDIDATE_PORTFOLIO.md) contains 100 distinct domain × motif research questions with a named comparator, all NOVELTY_UNKNOWN and UNTESTED. They are not 'almost certainly novel'—such a probability cannot be justified without rigorous prior-art and external validation.

## Hard boundaries

- Existing physics/control methods are not Garden inventions.
- Temporal masking and provenance filtering cannot erase facts encoded in pretrained model weights; no guarantee of historical blindness.
- Simulation with identical generator/detector equations risks inverse crime; use independent perturbations or field data.
- Verify source-bound legacy identifiers before citing as controlling.
- Negative, inconclusive and null results remain in the ledger.
- No self-admission or changes to canonical v15.5.

## Next experiment

Implement actual typed Garden generator and generic generator, freeze held-out nonlinear systems, and compare both against a matched SOS/SMT/CEGIS baseline. A gain requires independently validated, reproducible held-out advantage. Otherwise report no added value in that class.
