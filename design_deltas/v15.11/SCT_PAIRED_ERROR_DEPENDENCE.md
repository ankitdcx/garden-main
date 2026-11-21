# SCT paired-error dependence correction

**Status** Proposed v15.11 theory correction. Canonical owner: v15.5 Theories, TH-SCT §3. The TheoryEquationContract, Evidence, Compare and REP independence owners apply. This candidate changes the reference estimator used when combining reviewer signals.

The canonical reference uses empirical co-error frequency as a latent correlation and compares it to observed correlation with a maximum. Their scales answer different questions. Identical joint error frequencies can arise from independent reviewers or reviewers with identical failures.

## Paired observations

Freeze the question family, pair of reviewers, scoring oracle, inclusion rules, treatment of abstentions, aggregation unit, collection window and dependence profile before evaluation. Count n11 (both wrong), n10 (only the first wrong), n01 (only the second wrong), and n00 (both correct). Retain excluded, unscorable and abstained cases as separate counts. Preserve shared-source and shared-representation information. Use a separate profile for deployment data and each probe population.

For N equal to the sum of the four counts, joint risk is n11/N. Marginal error rates are (n11+n10)/N and (n11+n01)/N. Estimate association of the paired error indicators using

    phi = (n11*n00 - n10*n01) /
          sqrt((n11+n10)*(n01+n00)*(n11+n01)*(n10+n00))

Empty samples have undefined rates. Constant indicators have undefined phi even when joint risk is known. Below the profile's predeclared adequate independent sampling-unit count, keep descriptive counts and label inferential dependence UNKNOWN. Item repetition, related questions, missing outcomes and selection on agreement require explicit treatment.

## Use in evidence weighting

Use joint risk for the chance of the pair failing together on the evaluated population. For a dependence discount, compare estimates on the same association scale over qualified populations. Bind any operational weight to the selected population, sampling-unit definition, uncertainty method, interval level, minimum support and validity window. A profile may conservatively use the larger upper bound across qualified, relevant strata. Pooling or transferring estimates needs a justified population mapping. Domain shift, constant indicators, missing uncertainty qualification or evidence of a material shared loss leaves independent corroboration unestablished.

For a qualified binary-error profile using the existing SCT discount, omit the diagonal, use a conservative discount coefficient in [0,1] for each other reviewer, and keep unresolved pairs grouped for corroboration until requalified. A negative point estimate alone gives no extra independence credit. Perfectly co-failing equal-weight reviewers may collectively contribute at most one equal-weight signal for the affected property. Pairwise results alone cannot certify group independence. No change to consent, authority or proof admission follows from this arithmetic.

| Counts (n11, n10, n01, n00) | Joint risk | Phi | Expected interpretation |
|---|---:|---:|---|
| 1, 9, 9, 81 | 0.01 | 0 | Empirically zero association on this fixture |
| 1, 0, 0, 99 | 0.01 | 1 | Identical failures |
| 0, 0, 10, 90 | 0 | undefined | Constant first indicator |
| 0, 0, 0, 0 | undefined | undefined | No paired outcomes |

The [reference cases](../../verification/test_design_cases.py) check the arithmetic and weight cap on synthetic tables. Re-estimating assessor reliability and demonstrating improvement over a simpler shared-lineage grouping require independent held-out paired outcomes.
