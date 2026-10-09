#!/usr/bin/env python3
"""Deterministic, synthetic transformer-interface audit, stdlib only.

NONCANONICAL research. Known harmonic-loss physics; no discovery/deployment claim.
Run: python electricity_experiment.py
The fixed local prediction memo SHA-256 is included in every result. This does
not establish independent preregistration. All numerical parameters are synthetic.
"""
from dataclasses import dataclass, replace
import json
import math
import random

PROTOCOL_SHA256 = "19984e724c2453b83f78694c0c65333e629c2da0cfd976fee2bde84122a1fa71"
SOURCE = "https://strathprints.strath.ac.uk/92564/1/Senol-etal-IEEE-TECE-2025-Transformer-aging-under-harmonic-emissions-from-electric-vehicle.pdf"


@dataclass(frozen=True)
class Contract:
    """Fixed synthetic whole-transformer coefficients and proxy constraints."""
    iref_a: float = 1000.0
    voltage_ll_v: float = 400.0
    core_w: float = 1000.0
    dc_w: float = 3000.0
    eddy_w: float = 300.0
    stray_w: float = 150.0
    conductance_w_per_k: float = 80.0
    ambient_c: float = 40.0
    limit_c: float = 105.0
    rms_limit_a: float = 1200.0
    highest_harmonic: int = 13

    def validate(self):
        vals = list(self.__dict__.values())
        if not all(isinstance(x, (float, int)) and not isinstance(x, bool)
                   and math.isfinite(x) for x in vals):
            raise ValueError("Nonfinite parameter")
        if min(self.iref_a, self.voltage_ll_v, self.conductance_w_per_k,
               self.rms_limit_a) <= 0:
            raise ValueError("Positive scales required")
        if min(self.core_w, self.dc_w, self.eddy_w, self.stray_w) < 0:
            raise ValueError("Negative loss coefficient")
        if (not isinstance(self.highest_harmonic, int) or
                self.highest_harmonic < 1 or self.limit_c <= self.ambient_c):
            raise ValueError("Empty declared operating domain")


def validate_spectrum(spectrum, c):
    """RMS amplitudes AFTER phasor aggregation, finite declared harmonic band."""
    c.validate()
    for h, amps in spectrum.items():
        if isinstance(h, bool) or not isinstance(h, int) or h < 1 or h > c.highest_harmonic:
            raise ValueError("Outside declared harmonic domain")
        if not math.isfinite(amps) or amps < 0:
            raise ValueError("Invalid RMS amplitude")


def spectrum_at(i1_a, h, thd=0.20):
    if not isinstance(h, int) or isinstance(h, bool) or h < 2:
        raise ValueError("Specify a nonfundamental integer harmonic")
    if not all(math.isfinite(x) and x >= 0 for x in (i1_a, thd)):
        raise ValueError("Nonnegative finite current and THD required")
    return {1: float(i1_a), h: float(i1_a * thd)}


def moments(spectrum, c):
    validate_spectrum(spectrum, c)
    return tuple(math.fsum((amps / c.iref_a) ** 2 * h ** p
                          for h, amps in spectrum.items())
                 for p in (0.0, 2.0, 0.8))


def full_loss(spectrum, c):
    """Full-spectrum established baseline; no call through compressed moments."""
    validate_spectrum(spectrum, c)
    return c.core_w + math.fsum(
        (amps / c.iref_a) ** 2 *
        (c.dc_w + c.eddy_w * h * h + c.stray_w * h ** 0.8)
        for h, amps in spectrum.items())


def moment_loss(spectrum, c):
    m0, m2, m08 = moments(spectrum, c)
    return c.core_w + c.dc_w * m0 + c.eddy_w * m2 + c.stray_w * m08


def coarse_loss(spectrum, c, assumed_h=1):
    """Counterfactual lossy interface, explicit assumed harmonic allocation."""
    validate_spectrum(spectrum, c)
    if (not isinstance(assumed_h, int) or isinstance(assumed_h, bool) or
            not 1 <= assumed_h <= c.highest_harmonic):
        raise ValueError("Assumed harmonic outside declared domain")
    i1_sq = (spectrum.get(1, 0) / c.iref_a) ** 2
    harmonic_sq = math.fsum((v / c.iref_a) ** 2
                           for h, v in spectrum.items() if h > 1)
    k1 = c.dc_w + c.eddy_w + c.stray_w
    kh = c.dc_w + c.eddy_w * assumed_h ** 2 + c.stray_w * assumed_h ** .8
    return c.core_w + k1 * i1_sq + kh * harmonic_sq


def thermal_proxy(loss_w, c):
    c.validate()
    if not math.isfinite(loss_w) or loss_w < 0:
        raise ValueError("Nonnegative finite heat loss required")
    return c.ambient_c + loss_w / c.conductance_w_per_k


def feasible(spectrum, loss_w, c):
    # Reject invalid physical input even when a current limit would short-circuit.
    temperature = thermal_proxy(loss_w, c)
    m0 = moments(spectrum, c)[0]
    return (math.sqrt(m0) * c.iref_a <= c.rms_limit_a + 1e-10 and
            temperature <= c.limit_c + 1e-10)


def capacity_oracle(h, thd, c):
    """Analytic isolated-harmonic oracle, independent of full_loss/moments.

    Return None if even an energized zero-current state exceeds the heat budget.
    """
    c.validate()
    if (not isinstance(h, int) or isinstance(h, bool) or
            not 2 <= h <= c.highest_harmonic or
            not math.isfinite(thd) or thd < 0):
        raise ValueError("Invalid harmonic or THD")
    k = (c.dc_w * (1 + thd ** 2) +
         c.eddy_w * (1 + thd ** 2 * h ** 2) +
         c.stray_w * (1 + thd ** 2 * h ** .8))
    budget = c.conductance_w_per_k * (c.limit_c - c.ambient_c) - c.core_w
    if budget < 0:
        return None
    if k == 0:
        return c.rms_limit_a / math.sqrt(1 + thd ** 2)
    return min(c.rms_limit_a / math.sqrt(1 + thd ** 2),
               c.iref_a * math.sqrt(budget / k))


def choose_mode(i1_a, c, estimator):
    """Identical delivered service and hard proxy constraints for both modes.

    The lower-order mode's 200W auxiliary draw is external to the transformer.
    Real feasibility of controlling these waveforms is UNKNOWN.
    """
    actions = []
    for label, h, aux_w in (("h13", 13, 0.0), ("h5", 5, 200.0)):
        s = spectrum_at(i1_a, h)
        predicted_w = estimator(s, c)
        if feasible(s, predicted_w, c):
            actions.append((predicted_w + aux_w, label, s, aux_w))
    if not actions:
        return {"mode": "NONE", "evaluated_feasible": False}
    _, label, spectrum, aux = min(actions)
    true_w = full_loss(spectrum, c)
    useful_w = math.sqrt(3.0) * c.voltage_ll_v * i1_a
    source_w = useful_w + true_w + aux
    return {"mode": label,
            "evaluated_feasible": feasible(spectrum, true_w, c),
            "actual_transformer_loss_w": true_w,
            "auxiliary_w": aux,
            "actual_temperature_proxy_c": thermal_proxy(true_w, c),
            "useful_power_w": useful_w,
            "source_power_w": source_w,
            "energy_balance_residual_w": source_w - useful_w - true_w - aux}


def determinant3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def matched_moment_pair(c):
    """Positive spectra from explicit nullspace cofactors, no fitted targets."""
    hs = (5, 7, 11, 13)
    a = [[h ** p for h in hs] for p in (0, 2, .8)]
    v = [(-1) ** j * determinant3([[row[k] for k in range(4) if k != j]
                                   for row in a]) for j in range(4)]
    positive = [max(x, 0) for x in v]
    negative = [max(-x, 0) for x in v]
    pair = []
    for signs in (positive, negative):
        scale = .04 / math.fsum(signs)
        s = {1: c.iref_a}
        s.update({h: c.iref_a * math.sqrt(weight * scale)
                  for h, weight in zip(hs, signs)})
        pair.append(s)
    return pair


def artificial_residual(spectrum, c, epsilon_w=5000.0):
    """Deliberate domain challenge; not claimed as measured constitutive law."""
    return math.fsum(epsilon_w * (h / 13.0) ** 1.5 * (amps / c.iref_a) ** 2
                     for h, amps in spectrum.items() if h > 1)


def run():
    c = Contract()
    estimators = {
        "rms_only": lambda s, p: coarse_loss(s, p, 1),
        "rms_thd_assume_h5": lambda s, p: coarse_loss(s, p, 5),
        "rms_thd_worst_h13": lambda s, p: coarse_loss(s, p, 13),
        "repaired_moments": moment_loss,
        "full_spectrum": full_loss,
    }
    rows = {}
    for h in (5, 13):
        s = spectrum_at(950, h)
        cap = capacity_oracle(h, .20, c)
        boundary_loss = full_loss(spectrum_at(cap, h), c)
        assert abs(thermal_proxy(boundary_loss, c) - c.limit_c) < 1e-10
        assert not feasible(spectrum_at(cap * 1.000001, h),
                            full_loss(spectrum_at(cap * 1.000001, h), c), c)
        rows[str(h)] = {
            "rms_a": c.iref_a * math.sqrt(moments(s, c)[0]),
            "thd": .2,
            "loss_w": full_loss(s, c),
            "temperature_proxy_c": thermal_proxy(full_loss(s, c), c),
            "permissible_i1_a": cap,
        }
    analytical_gap = (.95 ** 2 * .04 *
                      (c.eddy_w * (13 ** 2 - 5 ** 2) +
                       c.stray_w * (13 ** .8 - 5 ** .8)))
    observed_gap = rows["13"]["loss_w"] - rows["5"]["loss_w"]
    assert abs(observed_gap - analytical_gap) < 1e-10
    assert observed_gap > 1500
    assert rows["5"]["temperature_proxy_c"] < 105 < rows["13"]["temperature_proxy_c"]
    assert rows["5"]["permissible_i1_a"] - rows["13"]["permissible_i1_a"] > 150

    at950 = {name: choose_mode(950, c, f) for name, f in estimators.items()}
    assert not at950["rms_only"]["evaluated_feasible"]
    assert not at950["rms_thd_assume_h5"]["evaluated_feasible"]
    assert at950["repaired_moments"] == at950["full_spectrum"]
    assert at950["full_spectrum"]["mode"] == "h5"

    rng = random.Random(20261009)
    max_loss_error = 0.0
    max_electrical_residual = 0.0
    max_thermal_residual = 0.0
    decisions_same = 0
    for _ in range(200):
        i1 = rng.uniform(500, 1100)
        energy = rng.uniform(0, .09)
        weights = [rng.expovariate(1) for _ in range(4)]
        s = {1: i1}
        s.update({h: i1 * math.sqrt(energy * w / math.fsum(weights))
                  for h, w in zip((5, 7, 11, 13), weights)})
        lfull, lmom = full_loss(s, c), moment_loss(s, c)
        max_loss_error = max(max_loss_error, abs(lfull - lmom))
        assert abs(lfull - lmom) < 1e-9
        assert abs(coarse_loss(s, c, 13) - c.core_w) >= lfull - c.core_w - 1e-9
        assert lfull >= 0
        max_thermal_residual = max(max_thermal_residual, abs(
            c.conductance_w_per_k * (thermal_proxy(lfull, c) - c.ambient_c) - lfull))
        mf = choose_mode(i1, c, full_loss)
        mr = choose_mode(i1, c, moment_loss)
        assert mf == mr
        decisions_same += 1
        if mf["mode"] != "NONE":
            max_electrical_residual = max(max_electrical_residual,
                                         abs(mf["energy_balance_residual_w"]))

    # Fourier orthogonality provides an independently integrated RMS oracle.
    sample_s = spectrum_at(950, 13)
    sample_n = 4096
    rms2_quadrature = math.fsum(
        math.fsum(math.sqrt(2) * amps * math.sin(2 * math.pi * h * j / sample_n)
                  for h, amps in sample_s.items()) ** 2
        for j in range(sample_n)) / sample_n
    rms2_parseval = math.fsum(v * v for v in sample_s.values())
    assert abs(rms2_quadrature - rms2_parseval) < 1e-7

    nulls = {}
    no_harmonic = {1: 800.0}
    vals = [f(no_harmonic, c) for f in estimators.values()]
    nulls["zero_harmonics_all_models_equal"] = max(vals) - min(vals) < 1e-10
    ohmic = replace(c, eddy_w=0.0, stray_w=0.0)
    nulls["ohmic_only_rms_sufficient"] = all(
        abs(full_loss(spectrum_at(950, h), ohmic) -
            coarse_loss(spectrum_at(950, h), ohmic)) < 1e-10 for h in (5, 13))
    nulls["zero_current_core_loss_only"] = full_loss({1: 0.0}, c) == c.core_w
    rejected = 0
    for invalid_s in ({0: 10.0}, {15: 1.0}, {1: float("nan")}, {1: -1.0}):
        try:
            full_loss(invalid_s, c)
        except ValueError:
            rejected += 1
    nulls["invalid_and_out_of_band_rejected"] = rejected == 4
    bad_calls = (
        lambda: feasible({1: 950}, -5000, c),
        lambda: spectrum_at(1000, 1),
        lambda: capacity_oracle(99, .2, c),
        lambda: coarse_loss({1: 950}, c, assumed_h=-3),
        lambda: replace(c, highest_harmonic=13.5).validate(),
    )
    invalid_rejected = 0
    for call in bad_calls:
        try:
            call()
        except ValueError:
            invalid_rejected += 1
    nulls["adversarial_invalid_arguments_rejected"] = invalid_rejected == len(bad_calls)
    zero_load_loss = replace(c, dc_w=0, eddy_w=0, stray_w=0)
    nulls["zero_load_coefficient_capacity_is_current_limit"] = (
        capacity_oracle(5, .2, zero_load_loss) == c.rms_limit_a / math.sqrt(1.04))
    nulls["core_alone_over_limit_returns_no_feasible_state"] = (
        capacity_oracle(5, .2, replace(c, core_w=6000)) is None)
    assert all(nulls.values())

    # Both hypothetical modes deliver the same useful service and satisfy gates.
    low_s, high_s = spectrum_at(800, 5), spectrum_at(800, 13)
    low_w, high_w = full_loss(low_s, c), full_loss(high_s, c)
    assert feasible(low_s, low_w, c) and feasible(high_s, high_w, c)
    net_saving_w = high_w - low_w - 200
    energy_saved_kwh = net_saving_w * 8000 / 1000
    annual_gross = energy_saved_kwh * .10
    annual_net = annual_gross - 1200 / 5 - 50
    assert net_saving_w > 900 and annual_net > 400
    assert choose_mode(800, c, full_loss) == choose_mode(800, c, moment_loss)

    # Second-cycle failure: moments are only sufficient for the declared law.
    pair = matched_moment_pair(c)
    mm = [moments(s, c) for s in pair]
    moment_gap = max(abs(x - y) for x, y in zip(*mm))
    assert moment_gap < 1e-10
    base_gap = abs(full_loss(pair[0], c) - full_loss(pair[1], c))
    residuals = [artificial_residual(s, c) for s in pair]
    bound = 5000 * .04
    assert base_gap < 1e-8
    assert 0 < abs(residuals[0] - residuals[1])
    assert all(0 <= r <= bound + 1e-9 for r in residuals)
    assert max_electrical_residual < 1e-8
    assert max_thermal_residual < 1e-8

    # Temporal/phasor aggregation domain check: source moments are not additive.
    # Two 100 A h5 phasors sum to 0 or 200 A depending on relative phase.
    harmonic_loss_inphase = (200 / c.iref_a) ** 2 * (
        c.dc_w + c.eddy_w * 25 + c.stray_w * 5 ** .8)
    harmonic_loss_antiphase = 0.0

    def round_floats(x):
        if isinstance(x, float):
            return float(f"{x:.12g}")
        if isinstance(x, dict):
            return {k: round_floats(v) for k, v in x.items()}
        if isinstance(x, (tuple, list)):
            return [round_floats(v) for v in x]
        return x

    return round_floats({
        "experiment": "E1 transformer spectrum-to-loss interface",
        "status": "SYNTHETIC_KNOWN_PHYSICS_NO_NOVELTY_OR_EMPIRICAL_VALUE_CLAIM",
        "protocol_sha256": PROTOCOL_SHA256,
        "baseline_source": SOURCE,
        "parameters": c.__dict__,
        "same_rms_thd_witness_at_950a": rows,
        "loss_gap_w": observed_gap,
        "analytic_oracle_error_w": observed_gap - analytical_gap,
        "decision_audit_at_950a": at950,
        "full_baseline_equality": {
            "random_spectra": 200,
            "max_loss_error_w": max_loss_error,
            "fixed_pair_decisions_equal": decisions_same,
            "incremental_garden_operating_value_before_extra_cost": 0.0,
            "max_electrical_balance_residual_w": max_electrical_residual,
            "max_thermal_balance_residual_w": max_thermal_residual,
            "balance_check_scope": "Constructed bookkeeping identities only, not independent physical conservation validation",
            "parseval_relative_error": abs(rms2_quadrature - rms2_parseval) / rms2_parseval,
        },
        "null_checks": nulls,
        "conditional_economics_at_800a": {
            "currency": "hypothetical currency units; not market quotes",
            "same_useful_power_w": math.sqrt(3) * c.voltage_ll_v * 800,
            "both_modes_proxy_feasible": True,
            "baseline_high_order_loss_w": high_w,
            "low_order_loss_w": low_w,
            "extra_auxiliary_w": 200,
            "net_energy_saving_w": net_saving_w,
            "annual_saved_kwh": energy_saved_kwh,
            "annual_gross_energy_value": annual_gross,
            "annualized_capex_and_maintenance": 290,
            "annual_net_value": annual_net,
            "five_year_undiscounted_break_even_upfront_cost": 5 * (annual_gross - 50),
            "incremental_garden_value_vs_full_spectrum_baseline": 0,
            "measured_real_economic_value": "UNKNOWN",
        },
        "second_cycle_domain_challenge": {
            "status": "ARTIFICIAL_RESIDUAL_NOT_PHYSICAL_LAW",
            "spectra_rms_a": pair,
            "retained_moment_max_difference": moment_gap,
            "declared_model_loss_difference_w": base_gap,
            "artificial_true_loss_difference_w": abs(residuals[0] - residuals[1]),
            "individual_omitted_losses_w": residuals,
            "loss_error_bound_w": bound,
            "temperature_error_bound_k": bound / c.conductance_w_per_k,
            "robust_controller": "BOUND_DERIVED_CONTROLLER_NOT_IMPLEMENTED_OR_TESTED",
            "domain_response": "INVALIDATE exact sufficiency; use independently justified residual bound or full revised model",
        },
        "phasor_aggregation_counterexample": {
            "per_source_h5_rms_a": 100,
            "in_phase_aggregate_h5_loss_w": harmonic_loss_inphase,
            "opposed_phase_aggregate_h5_loss_w": harmonic_loss_antiphase,
            "conclusion": "Aggregate harmonic phasors before computing moments; phase-free source summaries are insufficient",
        },
        "gates": {
            "local_model_mathematics": "VERIFIED_UNDER_ASSUMPTIONS",
            "implementation_synthetic_checks": "PASS",
            "independent_code_review": "PARTIAL_SCOPED_SAME_MODEL_ROLE_REVIEW_REPORTED_COUNTEREXAMPLES_REPAIRED",
            "full_transformer_safety_standard": "NOT_IMPLEMENTED",
            "empirical_validation": "NOT_RUN",
            "frontier_novelty": "NOT_ESTABLISHED",
            "blind_discovery_advantage": "NOT_TESTED",
            "canonical_admission": "NOT_REQUESTED_OR_GRANTED",
        },
    })


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
