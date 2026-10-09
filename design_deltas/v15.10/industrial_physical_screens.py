"""Reproduce two rejected/known physical leads; not novel science or field savings.

Standard-library-only post-freeze checks, 2026-10-09. Drying equations are adapted
from the drying-mapper branch's drying_screen.py; its SciPy solvers are replaced
by bounded scalar solvers here. Carbonate equations replay membrane M-01.
Neither screen establishes measurement accuracy, industrial applicability,
novelty, Garden superiority, or economic benefit over the strongest comparator.
"""
from math import exp, sqrt


def bisect(function, low, high, tolerance=1e-12):
    """Bracketed scalar root; finite budget, no convergence-to-PASS fallback."""
    fl, fh = function(low), function(high)
    if fl == 0:
        return low
    if fh == 0:
        return high
    if fl * fh > 0:
        raise ValueError("Root is not bracketed")
    for _ in range(200):
        middle = (low + high) / 2
        fm = function(middle)
        if fm == 0 or high - low <= tolerance:
            return middle
        if fl * fm > 0:
            low, fl = middle, fm
        else:
            high = middle
    raise RuntimeError("Root iteration budget exhausted")


def bounded_minimum(function, low, high):
    """Golden-section minimum for this smooth, assumed-unimodal screen only.

    Includes both endpoints. It is not a certificate for arbitrary objectives.
    """
    left, right = low, high
    fraction = (sqrt(5) - 1) / 2
    a, b = right - fraction * (right - left), left + fraction * (right - left)
    fa, fb = function(a), function(b)
    for _ in range(120):
        if right - left < 1e-10:
            break
        if fa < fb:
            right, b, fb = b, a, fa
            a = right - fraction * (right - left)
            fa = function(a)
        else:
            left, a, fa = a, b, fb
            b = left + fraction * (right - left)
            fb = function(b)
    return min((low, high, (left + right) / 2), key=function)


def psat(t):
    """Assumed Buck-style saturation fit: Celsius -> kPa, liquid-water scope."""
    return .61121 * exp((18.678 - t / 234.5) * t / (257.14 + t))


def wsat(t):
    """Saturation humidity ratio kg water/kg dry air at assumed 101.325 kPa."""
    pressure = psat(t)
    return .62198 * pressure / (101.325 - pressure)


def h(t, w):
    """Moist-air enthalpy kJ/kg dry air; Celsius and kg water/kg dry air."""
    return 1.006 * t + w * (2501 + 1.86 * t)


def cop(t):
    """Assumed cooling COP: 45% of Carnot, condenser 65 C, evaporator t C.

    This is a synthetic performance model, not a measured heat-pump curve.
    """
    return .45 * (t + 273.15) / (65 - t)


def drying_screen():
    """Known split-return benefit against optimized mixed-return/bypass screen.

    Two return streams each carry 1 kg/s dry air. A:40C,w=.016;
    B:55C,w=.008. Required supply60C,w=.008. Same .008 kg/s water removal.
    Condensate sensible enthalpy uses 4.186 kJ/(kg K), relative to 0C.
    Excludes fans, pressure losses, installation, transients and product effects.
    Established selective-return engineering already supplies the candidate;
    the positive comparison here is not Garden-specific incremental savings.
    """
    ta, wa, tb, wb, ws, ts = 40, .016, 55, .008, .008, 60
    wm, hm = (wa + wb) / 2, (h(ta, wa) + h(tb, wb)) / 2
    td = bisect(lambda t: wsat(t) - ws, 0, 40)

    def baseline(t):
        wc = wsat(t)
        alpha = (wm - ws) / (wm - wc)
        qe = 2 * alpha * (hm - h(t, wc) - (wm - wc) * 4.186 * t)
        power = qe / cop(t)
        hp = (1 - alpha) * hm + alpha * h(t, wc)
        reheat = 2 * (h(ts, ws) - hp)
        return dict(t=t, alpha=alpha, qe=qe, w=power, qreheat=reheat,
                    qreject=qe + power - reheat, water=2 * alpha * (wm - wc))

    optimum = bounded_minimum(lambda t: baseline(t)["w"], 0, td)
    mixed = baseline(optimum)
    qe = h(ta, wa) - h(td, ws) - (wa - ws) * 4.186 * td
    power = qe / cop(td)
    reheat = 2 * h(ts, ws) - h(td, ws) - h(tb, wb)
    split = dict(t=td, qe=qe, w=power, qreheat=reheat,
                 qreject=qe + power - reheat, water=wa - ws)
    delta = mixed["w"] - split["w"]
    return dict(baseline=mixed, selective=split, delta_kw=delta,
                chamberA_available_heat_kw=h(ts, ws) + (wa-ws)*4.186*ta-h(ta, wa),
                chamberB_available_heat_kw=h(ts, ws)-h(tb, wb))


# Illustrative ideal dilute 25 C constants; no activity/complexation correction.
# Concentrations mol/L, partial pressure atm. K1,K2 concentration-form constants;
# KH mol/(L atm), Ksp concentration-form mol^2/L^2, Kw mol^2/L^2.
K1, K2, KH, KSP, KW = 4.45e-7, 4.69e-11, .034, 3.3e-9, 1e-14


def carbonate_state(alkalinity, partial_pressure):
    """Solve alkalinity exactly within the assumed ideal carbonate-water model.

    No precipitation, kinetics, biological reactions or industrial activity model.
    CO2 partial pressure is dissolved-gas equilibrium equivalent, not hydraulic
    pressure. Gas contact is required to approach an imposed external gas value.
    Ca may be balanced by spectator counterions; their activities are ignored.
    """
    if alkalinity <= 0 or partial_pressure <= 0:
        raise ValueError("This bounded screen requires positive alkalinity/CO2")
    co2 = KH * partial_pressure

    def charge_residual(log_h):
        hydrogen = 10 ** log_h
        return (K1 * co2 / hydrogen + 2 * K1 * K2 * co2 / hydrogen**2
                + KW / hydrogen - hydrogen - alkalinity)

    log_h = bisect(charge_residual, -12, -3)
    hydrogen = 10 ** log_h
    bicarbonate = K1 * co2 / hydrogen
    carbonate = K1 * K2 * co2 / hydrogen**2
    return dict(pH=-log_h, hydrogen=hydrogen, co2=co2,
                bicarbonate=bicarbonate, carbonate=carbonate,
                total_carbon=co2 + bicarbonate + carbonate,
                charge_residual=charge_residual(log_h))


def carbonate_screen():
    initial = carbonate_state(.002, .02)
    calcium = .8 * KSP / initial["carbonate"]
    final = carbonate_state(.001, .0004)
    final_omega = .5 * calcium * final["carbonate"] / KSP
    approximate = .8 * .5**3 * .02 / .0004
    # M-02 negative control: fixed alkalinity+pH fixes dissolved CO2 uniquely.
    hydrogen = initial["hydrogen"]
    co2_from_fixed_ph = (.002 - KW/hydrogen + hydrogen) / (
        K1/hydrogen + 2*K1*K2/hydrogen**2)
    return dict(initial=initial, final=final, calcium_initial_M=calcium,
                initial_omega=.8, final_omega=final_omega,
                approximate_final_omega=approximate,
                approximation_relative_error=approximate/final_omega-1,
                matching_gas_fraction=initial["co2"]/(KH*1),
                co2_from_fixed_ph=co2_from_fixed_ph)


def verify(drying, carbonate):
    """Regression to separately frozen branch numbers, plus balance/null checks.

    These checks verify implementation/model accounting, not independent physics.
    """
    assert abs(drying["delta_kw"] - 13.522193830056892) < 1e-7
    assert abs(drying["baseline"]["water"] - drying["selective"]["water"]) < 1e-12
    assert abs(drying["selective"]["water"] - .008) < 1e-12
    assert drying["baseline"]["qreject"] >= 0
    assert drying["selective"]["qreject"] >= 0
    assert abs(carbonate["final_omega"] - 4.840887281137874) < 1e-9
    assert abs(carbonate["initial"]["charge_residual"]) < 1e-12
    assert abs(carbonate["final"]["charge_residual"]) < 1e-12
    assert abs(carbonate["matching_gas_fraction"] - .02) < 1e-14
    assert abs(carbonate["co2_from_fixed_ph"] - carbonate["initial"]["co2"]) < 1e-12


def main():
    drying, carbonate = drying_screen(), carbonate_screen()
    verify(drying, carbonate)
    print("POST-FREEZE NEGATIVE CONTROLS; known/overlapping mechanisms, no novelty.")
    print(f"Drying: mixed {drying['baseline']['w']:.9f} kW; "
          f"selective {drying['selective']['w']:.9f} kW; "
          f"difference {drying['delta_kw']:.9f} kW; equal water removal .008 kg/s.")
    print(f"Carbonate: saturation .8 -> {carbonate['final_omega']:.9f}; "
          f"bicarbonate approximation {carbonate['approximate_final_omega']:.9f}.")
    print("M-02: 2% CO2 matches assumed initial potential at 1 atm; "
          "existing fixed-pH/fixed-alkalinity control gives the same carbon state.")
    print("Checks passed; field benefit, novelty and Garden-specific gain unproven.")


if __name__ == "__main__":
    main()
