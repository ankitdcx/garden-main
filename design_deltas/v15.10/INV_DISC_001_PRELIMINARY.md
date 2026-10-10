# INV-DISC-001 — Within-System Invariant Discovery

**Status:** NONCANONICAL RESEARCH / PRELIMINARY CONTROL ONLY  
**Date:** 2026-10-10  
**Related:** [PHY-XFER-003](G15_10_PHY_XFER_003_CONSOLIDATED_CANDIDATE.md)

## Question

Can Garden-guided structural search derive valid, useful, previously unrecognized system-specific invariants more efficiently than matched established methods? Distinguish fundamental conservation laws, derived invariants of a model, and empirical regularities. This experiment addresses derived nonlinear invariant inequalities; cross-domain transfer is separate.

## Correct sign convention

System: dx/dt = -x+y², dy/dt=-y. Safe set: g=x²+y²-1 <= 0. Then dg/dt = -2x²+2xy²-2y², and on the boundary dg/dt = -2(1-xy²) < 0. Equivalently for h=1-x²-y² >=0, dh/dt = +2(1-xy²)>0. The earlier summary conflated g and h. The conclusion (forward invariance of the unit disk) is correct, but the original derivative sign was incorrect for g. No machine-checked SOS/SMT certificate was produced.

## Three-stage evaluation

A. Linear stoichiometric conservation: calibrate against exact left null-space (expect tie; no novelty).  
B. Polynomial first integrals: compare against appropriate Darboux/Lie/symbolic methods.  
C. Nonlinear inequalities (primary): compare Garden-guided synthesis against matched SOS/semidefinite and CEGIS/SMT-based methods, where available.

Hold out independently generated systems (including planted invariants and decoys). Freeze candidate generator, training data, scoring, time/memory budgets, solver configurations, acceptance thresholds and stopping rules *before* scored tests. Primary metrics: independently verified certificate rate and time-to-certificate; secondary: certified-region size, false certificates (zero accepted), coverage, compute. Same model/solver/time budget for baseline and Garden arm. A structural heuristic must be specified and ablated; do not count ordinary symbolic search relabeled as Garden.

## Preliminary executed control

The companion `inv_disc_001_control.py` uses SymPy to instantiate 20 cases of dx/dt=-a*x+b*y², dy/dt=-c*y, with positive a,c and bounded b. It checks the **sufficient** condition for the unit disk g<=0:

On x²+y²=1, |x*y²| <= 2/(3√3), so dg/dt <= -2 min(a,c) + 4|b|/(3√3). If this bound is strictly negative, the unit disk is forward-invariant.

**Observed:** 20/20 chosen cases satisfy this sufficient inequality. This is a parameterized positive control, not 20 independent discoveries or a benchmark against an established solver. It does not measure the Garden search heuristic. Output is in `INV_DISC_001_preliminary_receipts.json`. No SOS/SMT verifier, blinded test, independent evaluator or novel scientific result has been run.

## Historical contamination / provenance

A source-date cutoff, temporal tags and hashes cannot remove memorized knowledge from a pretrained model. Do not claim cryptographically guaranteed blindness. Model-free algorithms reduce but do not eliminate designer contamination; maintain separate frozen source/answer keys, decoys, leakage audits, and explicit limitations. Legacy K-INT IDs and v10.25 provenance/temporal controls are UNVERIFIED BINDINGS unless pinned to actual source spans.

## Research gate

No admission, scientific discovery or economic benefit from this control. Next: implement an explicit Garden-guided certificate proposal heuristic, establish a strong baseline and an independent verifier, and run held-out paired trials. Failure to beat baseline is an informative negative result. Do not revise architecture merely to avoid reporting a tie or loss.
