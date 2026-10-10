# INV-DISC-100 — Computational screening receipts (2026-10-10)

**Status: PRELIMINARY SYNTHETIC FEASIBILITY ONLY. No original idea has passed empirical testing, prior-art verification, or Garden-vs-baseline comparison.**

## Method and result

Each of the 100 domain × motif entries was subjected to a *generic two-state linear surrogate*, not a domain-calibrated physical model. A reproducible script and results table are linked below. The surrogate matrix is A=[[-a,b],[-b,-c]], a,c>0; the symmetric part is negative definite. Many passes are **true by construction** and cannot be interpreted as independent evidence. This deliberately weak screening is useful chiefly for checking implementation, recording inapplicability, and exposing how little the original 100 questions specify.

- 70/100 PASS_TOY (seven elementary synthetic mathematical checks per domain)
- 10/100 FAIL_TOY (illustrative 3× timescale-separation requirement not met)
- 20/100 NOT_TESTABLE (no rare-event process or actuator constraints specified)
- **0/100 SCIENTIFIC_PASS; 0/100 NOVELTY_PASS; 0/100 GARDEN_ADVANTAGE_PASS**.

## Per-candidate results

| Candidate | Domain | Motif | Toy check | Original claim | Novelty |
|---|---|---|---|---|---|
| INV-001 | Battery cell | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-002 | Battery cell | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-003 | Battery cell | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-004 | Battery cell | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-005 | Battery cell | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-006 | Battery cell | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-007 | Battery cell | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-008 | Battery cell | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-009 | Battery cell | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-010 | Battery cell | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-011 | Water distribution | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-012 | Water distribution | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-013 | Water distribution | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-014 | Water distribution | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-015 | Water distribution | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-016 | Water distribution | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-017 | Water distribution | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-018 | Water distribution | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-019 | Water distribution | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-020 | Water distribution | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-021 | Heat exchanger | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-022 | Heat exchanger | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-023 | Heat exchanger | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-024 | Heat exchanger | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-025 | Heat exchanger | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-026 | Heat exchanger | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-027 | Heat exchanger | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-028 | Heat exchanger | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-029 | Heat exchanger | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-030 | Heat exchanger | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-031 | Grid inverter network | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-032 | Grid inverter network | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-033 | Grid inverter network | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-034 | Grid inverter network | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-035 | Grid inverter network | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-036 | Grid inverter network | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-037 | Grid inverter network | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-038 | Grid inverter network | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-039 | Grid inverter network | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-040 | Grid inverter network | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-041 | Robot actuator | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-042 | Robot actuator | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-043 | Robot actuator | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-044 | Robot actuator | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-045 | Robot actuator | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-046 | Robot actuator | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-047 | Robot actuator | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-048 | Robot actuator | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-049 | Robot actuator | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-050 | Robot actuator | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-051 | PFAS adsorption column | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-052 | PFAS adsorption column | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-053 | PFAS adsorption column | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-054 | PFAS adsorption column | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-055 | PFAS adsorption column | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-056 | PFAS adsorption column | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-057 | PFAS adsorption column | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-058 | PFAS adsorption column | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-059 | PFAS adsorption column | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-060 | PFAS adsorption column | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-061 | Bioreactor | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-062 | Bioreactor | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-063 | Bioreactor | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-064 | Bioreactor | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-065 | Bioreactor | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-066 | Bioreactor | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-067 | Bioreactor | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-068 | Bioreactor | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-069 | Bioreactor | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-070 | Bioreactor | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-071 | Crop-soil system | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-072 | Crop-soil system | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-073 | Crop-soil system | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-074 | Crop-soil system | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-075 | Crop-soil system | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-076 | Crop-soil system | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-077 | Crop-soil system | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-078 | Crop-soil system | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-079 | Crop-soil system | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-080 | Crop-soil system | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-081 | PV array | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-082 | PV array | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-083 | PV array | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-084 | PV array | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-085 | PV array | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-086 | PV array | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-087 | PV array | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-088 | PV array | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-089 | PV array | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-090 | PV array | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |
| INV-091 | Bearing drivetrain | boundary-history | PASS_TOY | UNTESTED | UNKNOWN |
| INV-092 | Bearing drivetrain | sensor-loss | PASS_TOY | UNTESTED | UNKNOWN |
| INV-093 | Bearing drivetrain | coupling-cross-term | PASS_TOY | UNTESTED | UNKNOWN |
| INV-094 | Bearing drivetrain | switching-dwell | PASS_TOY | UNTESTED | UNKNOWN |
| INV-095 | Bearing drivetrain | delayed-feedback | PASS_TOY | UNTESTED | UNKNOWN |
| INV-096 | Bearing drivetrain | uncertainty-budget | PASS_TOY | UNTESTED | UNKNOWN |
| INV-097 | Bearing drivetrain | spatial-decomposition | PASS_TOY | UNTESTED | UNKNOWN |
| INV-098 | Bearing drivetrain | rare-transition | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-099 | Bearing drivetrain | actuator-budget | NOT_TESTABLE | UNTESTED | UNKNOWN |
| INV-100 | Bearing drivetrain | multi-timescale | FAIL_TOY | UNTESTED | UNKNOWN |

## Important limitations

1. Toy pass means only the chosen elementary necessary/sufficient surrogate property held; it does not validate the idea in its domain.
2. The toy system lacks fluid network topology, chemical kinetics, inverter control delays, PFAS adsorption physics, and other real domain details.
3. The linearized toy system is deliberately stable; most PASS_TOY outcomes are constructed, not discovered.
4. No public/real datasets, independent reviewers, domain-specific baselines, matched search budget or prior-art screens were used.
5. FAIL_TOY means an *illustrative* timescale criterion failed, not that the real idea is physically impossible.
6. NOT_TESTABLE is not FAIL and not PASS.
7. A generated 10×10 grid is not 100 independent scientific ideas; some combinations may be inapplicable.

## Next valid experiments

Select a well-posed candidate with source equations, named specialist comparator and quantitative primary endpoint. Build a Garden-guided search algorithm and generic search baseline, then perform held-out, independently verified comparison. Do not promote any of these 70 toy passes to the active discoveries register.
