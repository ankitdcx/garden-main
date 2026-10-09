#!/usr/bin/env python3
"""Ten physically mapped industrial candidates: bounded post-freeze replays.
NONCANONICAL RESEARCH. Ten investigations, NOT ten novel discoveries.
All monetary inputs and physical effect targets are assumed scenarios. No field
savings, current price quotation, global extrapolation or full SAL admission.
Run: python industrial_ten_cases.py [--details]. Standard library only.
Four scoped branches are isolated in functions to preserve their individual
contracts. Adapted source equations and targeted tests are retained below; see the
consolidated scientific register section 4.12 for graphs, sources and falsifiers.
"""
import argparse
from contextlib import redirect_stdout
import io


# Research-role source ten_heat_material_calc.py; original SHA256 416dbcfea2976d135c97cef0807e4c1dcda363ef1b026158bf9ba150c1438c55
def heat_material():
    """Bounded, illustrative material/energy contracts; no plant data or novelty proof.
    Python 3 standard library. Inputs are assumed scenario values unless noted.
    """
    import json
    import math


    def crf(rate=0.08, years=10):
        if not (rate >= 0 and years > 0):
            raise ValueError('rate and life outside economic domain')
        return 1 / years if rate == 0 else rate * (1 + rate)**years / ((1 + rate)**years - 1)


    def yield_value(throughput_t_y, incremental_saleable_t_t, price_usd_t,
                    added_kwh_t, electricity_usd_kwh, fixed_usd_y, capex_usd):
        if min(throughput_t_y, price_usd_t, added_kwh_t,
               electricity_usd_kwh, fixed_usd_y, capex_usd) < 0:
            raise ValueError('negative physical/economic parameter')
        gross = throughput_t_y * incremental_saleable_t_t * price_usd_t
        cost = throughput_t_y * added_kwh_t * electricity_usd_kwh + fixed_usd_y + capex_usd * crf()
        return dict(gross_usd_y=gross, cost_usd_y=cost, net_usd_y=gross - cost,
                    break_even_incremental_t_t=cost / (throughput_t_y * price_usd_t))


    def two_zone(t_s, fraction_surface=0.05, initial_core_c=950,
                 initial_surface_c=550, relaxation_s=60):
        """Closed two-lump thermal model, common constant cp; no phase kinetics.
        tau=(Cs*Cc)/(K*(Cs+Cc)); surface and core temperatures in degrees C.
        """
        f = fraction_surface
        if not (0 < f < 1 and relaxation_s > 0 and t_s >= 0):
            raise ValueError('thermal model domain')
        mean = f * initial_surface_c + (1 - f) * initial_core_c
        difference = (initial_core_c - initial_surface_c) * math.exp(-t_s / relaxation_s)
        return mean - (1-f)*difference, mean + f*difference


    def run():
        h1 = yield_value(100_000, .005, 2000, 10, .10, 100_000, 1_000_000)
        h1r = yield_value(100_000, .002 * (.8 - 0), 2000, 2, .10, 40_000, 500_000)
        h1r_comparator = yield_value(100_000, .002 * (.8 - .5), 2000, 2, .10, 40_000, 500_000)
        q_mj_t = (1 - .05) * 1000 * .7 * 400 / 1000
        fuel_gj_t = q_mj_t / 1000 / .6
        h2_cost = 5_000_000 * crf() + 250_000
        h2_gross = 1_000_000 * fuel_gj_t * 10
        h2 = dict(ideal_incremental_heat_MJ_t=q_mj_t, ideal_fuel_GJ_t=fuel_gj_t,
                  gross_usd_y=h2_gross, cost_usd_y=h2_cost, net_usd_y=h2_gross-h2_cost,
                  break_even_incremental_heat_MJ_t=h2_cost / (1_000_000*10) * .6 * 1000)
        cross_time_s = -60 * math.log((930-750) / (930-550))
        h2.update(surface_750C_time_s=cross_time_s,
                  temperatures_at_crossing_C=two_zone(cross_time_s))
        recovered_t_t = 20 / 1000 * .7
        heat_mj_t = recovered_t_t * 1000 * 1 * 800 / 1000
        h3_heat_gross = 1_000_000 * heat_mj_t / 1000 / .6 * 10
        h3_material_gross = 1_000_000 * recovered_t_t * 20
        h3_cost = 1_000_000 * crf() + 80_000
        h3 = dict(recovered_mineral_t_t=recovered_t_t, retained_heat_MJ_t=heat_mj_t,
                  heat_gross_usd_y=h3_heat_gross, material_gross_usd_y=h3_material_gross,
                  cost_usd_y=h3_cost,
                  net_usd_y=h3_heat_gross+h3_material_gross-h3_cost,
                  break_even_clean_recovery_fraction=h3_cost / ((h3_heat_gross+h3_material_gross)/.7))
        # Checks protect real physical/economic risks, not claims of empirical validation.
        checks = 0
        for t in (0, 1, 30, 60, 300, 10000):
            ts, tc = two_zone(t)
            assert math.isclose(.05*ts + .95*tc, 930, abs_tol=1e-10)
            assert 550 <= ts <= tc <= 950
            checks += 2
        assert math.isclose(two_zone(cross_time_s)[0], 750, abs_tol=1e-10); checks += 1
        assert yield_value(100_000, 0, 2000, 10, .10, 100_000, 1_000_000)['net_usd_y'] < 0; checks += 1
        assert h1r_comparator['net_usd_y'] < 0 < h1r['net_usd_y']; checks += 1
        assert 0 < h3['break_even_clean_recovery_fraction'] < 1; checks += 1
        assert math.isclose(crf(0,10), .1); checks += 1
        # A unchanged strong baseline permits no physical savings credit.
        return dict(status='ILLUSTRATIVE_ONLY_NO_MEASURED_GARDEN_SAVINGS', crf_per_y=crf(),
                    H1=h1, H1R_no_existing_recovery=h1r,
                    H1R_existing_50pct_recovery=h1r_comparator, H2=h2, H3=h3,
                    contract_checks=checks)

    return run()

# Research-role source ten_utilities_calc.py; original SHA256 cb352c767c4b6009248c865a537d4b00a4c877c7ecd2cc2b4e2d33d908463e4b
def utilities():
    """Bounded utilities research calculations; synthetic assumptions, no field validation.
    Run: python ten_utilities_calc.py. Standard library only. No network or writes.
    """
    from math import exp, isclose

    GRAPHS = {
        "U1": [(1,2),(2,3),(3,4),(4,5),(4,6),(5,7),(6,7),(7,8),
               (7,9),(7,10),(8,11),(9,10),(10,12),(12,11),(11,1),(2,7)],
        "U2": [(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),
               (9,10),(10,11),(11,12),(7,4),(2,4),(4,6),(9,6),(6,3)],
        "U3": [(1,2),(2,3),(3,6),(4,7),(5,7),(6,7),(7,8),(7,9),
               (8,10),(9,10),(10,11),(11,1),(3,7),(2,9),(1,8),(11,12),(9,12)],
    }
    LAW_BINDINGS = {
        "U1": [[2,3,4,5,6,8,9,10,11,12],[1,3,4,8,11,12],[4,5,6],
               [3,4,8,11],[5,6,7,8,9],[2,5,6,7],[7,8,11,12],[1,8,9,10,11,12]],
        "U2": [[2,3,4,7,8,9],[3,4,7,8,9,11],[2,4,6,7],[9,10,11],
               [7,8,9],[1,2,4,6],[4,6,7],[4,7,8,9,10],[6,9,12]],
        "U3": [[1,2,8,9,10,11],[2,3,4,5,6,7,8,9],[7,8,9,10],[2,9,10],
               [4,7,8],[1,8,11],[1,2,11],[2,3,6,7],[1,7,8,9,11,12]],
    }


    def crf(rate=0.08, years=10):
        return rate * (1 + rate) ** years / ((1 + rate) ** years - 1)


    def partition(cin, flash, coefficient):
        if cin < 0 or not 0 <= flash < 1 or coefficient < 0:
            raise ValueError("Outside dilute single-stage equilibrium domain")
        liquid = cin / (1 - flash + flash * coefficient)
        return liquid, coefficient * liquid


    def u1():
        cl, cv = partition(10, 0.1, 50)
        recovered_kg = 30000 * 8000 * 0.1 * 0.9
        thermal = recovered_kg * 4.18 * 80 / 3600
        fuel = thermal / 0.8
        water = recovered_kg / 1000
        gross = fuel * 0.04 + water * 2
        # Added financial scenario after physical freeze; not vendor quotes.
        capital, annual_om = 300000, 15000
        net = gross - capital * crf() - annual_om
        return dict(liquid_mg_kg=cl, vapor_mg_kg=cv, liquid_kg_y=recovered_kg,
                    recovered_kWh_th_y=thermal, saved_kWh_fuel_y=fuel,
                    gross_usd_y=gross, net_usd_y=net,
                    max_capital_usd=(gross-annual_om)/crf())


    V, E, CM, PULSE_B, PERIOD, PULSE_H = 600., 30., 1000., 72., 12., 1.


    def tower_c(t, phase=0.0, continuous=False):
        """Exact periodic solution; starts each phase with a one-hour blowdown."""
        if continuous:
            b = PULSE_B * PULSE_H / PERIOD
            return b, (E+b)*CM/b
        a = exp(-PULSE_B * PULSE_H / V)
        eq = (E+PULSE_B)*CM/PULSE_B
        rise = E*CM/V*(PERIOD-PULSE_H)
        maximum = eq + rise/(1-a)
        minimum = eq + (maximum-eq)*a
        tau = (t-phase) % PERIOD
        if tau < PULSE_H:
            return PULSE_B, eq + (maximum-eq)*exp(-PULSE_B*tau/V)
        return 0., minimum+E*CM/V*(tau-PULSE_H)


    def receiving_trial(phases, continuous=False, dt=1/600):
        """Receiver CSTR240m3; conservative salt only, NO biological kinetics.
        Midpoint input and exact constant-input CSTR integration on each step.
        First 29 cycles equilibrate; report the last 12 hours. Starts are grid aligned.
        """
        volume, q_bg, c_bg = 240., 120., 300.
        c = c_bg
        n = round(PERIOD/dt)
        p_in = p_out = 0.
        tower_min, tower_max = float("inf"), 0.
        blown_volume = blown_salt = 0.
        for i in range(30*n):
            t = (i+0.5)*dt
            pairs = [tower_c(t, phase, continuous) for phase in phases]
            b_total = sum(b for b, _ in pairs)
            salt_rate = sum(b*x for b, x in pairs)  # mg/L*m3/h; convert /1000 tokg/h
            q = q_bg+b_total
            cin = (q_bg*c_bg+salt_rate)/q
            c = cin+(c-cin)*exp(-q*dt/volume)
            if i >= 29*n:
                p_in = max(p_in, cin)
                p_out = max(p_out, c)
                tower_min = min(tower_min, *(x for _, x in pairs))
                tower_max = max(tower_max, *(x for _, x in pairs))
                blown_volume += b_total*dt
                blown_salt += salt_rate*dt/1000
        return dict(inlet_peak_mg_L=p_in, reactor_peak_mg_L=p_out,
                    tower_min_mg_L=tower_min, tower_max_mg_L=tower_max,
                    blowdown_m3_per_12h=blown_volume,
                    salt_kg_per_12h=blown_salt)


    def u2():
        result = {"synchronous": receiving_trial([0,0,0]),
                  "staggered": receiving_trial([0,4,8]),
                  "continuous_baseline": receiving_trial([0,0,0],True)}
        result["conditional_avoided_tank_net_usd_y"]=(400000-60000)*crf()-5000
        result["attributable_increment_vs_continuous_usd_y"] = 0.0
        result["attribution_status"]="Tank avoidance already achieved by continuous baseline; no demonstrated candidate increment"
        return result


    def tes_value(volume=4000, cycles=200, t_layer=12, t_return=18,
                  price_peak=.20, price_off=.08, cop_peak=5, cop_off=6, eta=.95):
        if not (volume >= 0 and cycles >= 0 and t_return >= t_layer and 0 < eta <= 1):
            raise ValueError("Outside sensible-storage domain")
        e = 1000*volume*4.18*(t_return-t_layer)/3600
        avoided = e*cycles/cop_peak
        charge = e*cycles/(cop_off*eta)
        gross = avoided*price_peak-charge*price_off
        return e, avoided, charge, gross


    def u3():
        e, avoided, charge, gross = tes_value()
        capital, om = 500000, 20000
        return dict(kWh_th_cycle=e, peak_kWh_e_y=avoided,
                    offpeak_kWh_e_y=charge, gross_usd_y=gross,
                    net_usd_y=gross-capital*crf()-om,
                    max_capital_usd=(gross-om)/crf(),
                    incremental_vs_equivalent_modern_controller_usd_y=0.0)


    def checks():
        n = 0
        for f in (0, .01, .1, .3, .9):
            for k in (0, .1, 1, 10, 50, 100):
                cl, cv = partition(10, f, k)
                assert isclose((1-f)*cl+f*cv,10,abs_tol=1e-10)
                n += 1
        assert partition(10,.1,1)==(10,10); n+=1
        assert partition(10,0,50)[0]==10; n+=1
        assert partition(10,.1,0)[1]==0; n+=1
        for phase in (0,4,8):
            assert isclose(tower_c(0,phase)[1],tower_c(12,phase)[1]); n+=1
        results = u2()
        for key in ("synchronous","staggered","continuous_baseline"):
            r=results[key]
            assert isclose(r["blowdown_m3_per_12h"],216,abs_tol=1e-7);n+=1
            assert isclose(r["salt_kg_per_12h"],1296,abs_tol=1e-4);n+=1
        assert results["continuous_baseline"]["reactor_peak_mg_L"] < results["staggered"]["reactor_peak_mg_L"] < results["synchronous"]["reactor_peak_mg_L"]; n+=1
        assert tes_value(volume=0)[3]==0; n+=1
        assert tes_value(t_layer=18,t_return=18)[3]==0; n+=1
        assert tes_value(price_peak=.1,price_off=.1,cop_peak=5,cop_off=5,eta=.9)[3]<0;n+=1
        assert isclose(tes_value()[3],2*tes_value(volume=2000)[3]);n+=1
        return n

    return dict(U1=u1(), U2=u2(), U3=u3(), contract_checks=checks())

# Research-role source ten_food_cold_replay.py; original SHA256 6e2fa5f68042dff51ffbcbba920566feaec5658d256c6416ab08180165227f75
def food_cold():
    """Arithmetic and explicitly synthetic identifiability screen, no field evidence."""
    import math
    import random


    def crf(rate, years):
        return rate*(1+rate)**years/((1+rate)**years-1)


    def solve(a, b):
        a = [list(row)+[rhs] for row,rhs in zip(a,b)]
        for j in range(len(a)):
            pivot=max(range(j,len(a)), key=lambda i:abs(a[i][j]))
            a[j],a[pivot]=a[pivot],a[j]
            div=a[j][j]
            if abs(div)<1e-15: raise ValueError('rank deficient')
            a[j]=[v/div for v in a[j]]
            for i in range(len(a)):
                if i != j:
                    factor=a[i][j]
                    a[i]=[v-factor*w for v,w in zip(a[i],a[j])]
        return [row[-1] for row in a]


    def regress(rows, y):
        p=len(rows[0]);n=len(rows)
        gram=[[sum(row[j]*row[k] for row in rows) for k in range(p)] for j in range(p)]
        cross=[sum(row[j]*yi for row,yi in zip(rows,y)) for j in range(p)]
        beta=solve(gram,cross)
        residual=[yi-sum(a*b for a,b in zip(row,beta)) for row,yi in zip(rows,y)]
        sigma2=sum(x*x for x in residual)/(n-p)
        covariance_first=solve(gram,[1.0]+[0.0]*(p-1))[0]*sigma2
        return beta,math.sqrt(covariance_first)


    def synthetic(leak, seed=20261009):
        # Known transfer/phase frozen; four sinusoidal periods; uncorrelated Gaussian noise.
        # Concentration readout in uS/cm under a locally linear, temperature-compensated adapter.
        # Flow is not inferred from cross-side pressure because plate compliance can imitate it.
        rng=random.Random(seed)
        n=240
        period_s=60.0; dt_s=1.0; tau_s=8.0; delay_s=3.0
        omega=2*math.pi/period_s
        q0_ml_min=.5 if leak else 0.0
        dp0_pa=50_000.0; dp_hat_pa=5_000.0
        q_hat_ml_min=q0_ml_min*dp_hat_pa/(2*dp0_pa)
        receiver_ml_min=100.0; delta_kappa_us_cm=1_000.0
        transfer=1/math.sqrt(1+(omega*tau_s)**2)
        phase=math.atan(omega*tau_s)+omega*delay_s
        amplitude=delta_kappa_us_cm*q_hat_ml_min/receiver_ml_min*transfer
        rows=[];y=[]
        for i in range(n):
            t=i*dt_s
            carrier=math.sin(omega*t-phase)
            # Quadrature handles small phase errors; bias and slow drift separately fitted.
            rows.append([carrier,math.cos(omega*t-phase),1.0,(t-(n-1)/2)/n])
            y.append(amplitude*carrier+.4+.2*(t-(n-1)/2)/n+rng.gauss(0,.2))
        beta,se=regress(rows,y)
        return {'amplitude_predicted_us_cm':amplitude,'amplitude_fit_us_cm':beta[0],
                'standard_error_us_cm':se,'five_sigma_threshold_us_cm':5*se,
                'detected':beta[0]>5*se,'qhat_ml_min':q_hat_ml_min,
                'transfer':transfer,'count':n}


    def main():
        factor=crf(.08,10)
        print('CRF per year',factor)
        cycles=100*2*330
        f1_gross=cycles*3*.6*2500/(3600*1.5)*.12
        f1_net=f1_gross-5000-factor*200_000
        f1_break_mass=(5000+factor*200_000)/(f1_gross/3)
        print('F1 cycles/year',cycles,'condensation refrigeration component gross USD/y',f1_gross,
              'cooling-only net USD/y',f1_net,'break-even escaped kg/cycle',f1_break_mass)
        f1_additional_heat=cycles*3*.6*2500/3600*.12
        print('F1 plus purchased electric defrost heat scenario gross,net',f1_gross+f1_additional_heat,f1_net+f1_additional_heat)
        # Narrow incremental protocol compared with an existing integrated daily test.
        cost=40_000*factor+12_000+.1*5_000
        print('F2 required incremental avoided loss USD/y',cost)
        print('F2 required additional preventions/year at USD250k avoidable cost/event',cost/250_000)
        print('F2 iff incremental avoided loss USD75k/y: net',75_000-cost)
        signal=synthetic(True);null=synthetic(False)
        print('F2 SIGNAL',signal)
        print('F2 NULL',null)
        assert abs(signal['amplitude_fit_us_cm']-signal['amplitude_predicted_us_cm'])<3*signal['standard_error_us_cm']
        assert signal['detected'] and not null['detected']
        # No certificate of empirical detector performance: simulated white noise and known lag.
        fp=sum(synthetic(False,seed)['detected'] for seed in range(100))
        tp=sum(synthetic(True,seed)['detected'] for seed in range(100))
        print('F2 synthetic seeds 0..99 only: false positives',fp,'detections',tp)
        # Pressure-only counterexample: intact compliance creates a correlated response.
        compliance_ml_pa=1e-6
        dp_hat_pa=5000.0
        omega=2*math.pi/60
        apparent_ml_min=omega*compliance_ml_pa*dp_hat_pa*60
        print('F2 intact compliance apparent oscillatory volume-flow amplitude ml/min',apparent_ml_min)
        assert apparent_ml_min>signal['qhat_ml_min']
        # For white noise, correctly characterized DC hot test is stronger, so no superiority.
        dc_se=.2/math.sqrt(240)
        dc_leak_signal=1000*.5/100
        print('F2 ideal known-background constant-pressure comparator signal,se',dc_leak_signal,dc_se)


    buffer = io.StringIO()
    with redirect_stdout(buffer):
        main()
    factor = crf(.08,10)
    f1_cooling = 100*2*330*3*.6*2500/(3600*1.5)*.12
    f1_separate_electric_heat = 100*2*330*3*.6*2500/3600*.12
    f1_cost=5000+factor*200000
    f2_cost = 40000*factor+12000+.1*5000
    return dict(transcript=buffer.getvalue(), F1=dict(cooling_gross_usd_y=f1_cooling,
        separate_electric_heating_credit_if_metered=f1_separate_electric_heat,
        net_single_channel_usd_y=f1_cooling-f1_cost,
        net_two_distinct_bills_usd_y=f1_cooling+f1_separate_electric_heat-f1_cost,
        break_even_escaped_kg_cycle_single_channel=f1_cost/(f1_cooling/3)),
        F2=dict(incremental_avoided_loss_needed_usd_y=f2_cost,
        field_net_usd_y=None, signal=synthetic(True), null=synthetic(False)))


# Research-role source ten_manufacturing_replay.py; original SHA256 f8a1975475d1afdbe94a8fbf361a1923e5ab320c967bea33c1ea626a78a4d470
def manufacturing():
    """Bounded, synthetic manufacturing equation checks; no empirical savings/novelty claim."""
    import math

    M1_NODES = {
     'm1.01':'Receive characterized blank', 'm1.02':'Locate and support blank',
     'm1.03':'Apply cutting preload', 'm1.04':'Rough machine',
     'm1.05':'Redistribute heat and residual stress', 'm1.06':'Establish finish allowance',
     'm1.07':'Stop spindle and probe at preload F1', 'm1.08':'Perturb preload safely to F2',
     'm1.09':'Probe at F2', 'm1.10':'Estimate free shape and uncertainty',
     'm1.11':'Choose final cut / wait / stop', 'm1.12':'Restore validated cutting preload and finish',
     'm1.13':'Unclamp and thermally equilibrate', 'm1.14':'Independent coordinate measurement',
     'm1.15':'Release, rework or scrap',
    }
    M1_EDGES = [(f'm1.{i:02d}',f'm1.{i+1:02d}','SEQUENCE') for i in range(1,15)] + [
     ('m1.01','m1.10','dependsOn'),('m1.02','m1.10','dependsOn'),('m1.05','m1.10','dependsOn'),
     ('m1.06','m1.11','dependsOn'),('m1.03','m1.12','dependsOn'),
     ('m1.11','m1.05','BRANCH wait'),('m1.11','m1.15','BRANCH stop'),('m1.15','m1.06','RETRY rework bounded1'),
    ]
    M2_NODES = {
     'm2.01':'Final old-color shot','m2.02':'Clean feed path and barrel','m2.03':'Melt new resin',
     'm2.04':'Displace common manifold','m2.05':'Partition branch flows','m2.06':'Open purge gates',
     'm2.07':'Take branch-specific samples','m2.08':'Close cleared branch',
     'm2.09':'Purge uncleared branch at original permitted flow','m2.10':'Reopen production gate pattern',
     'm2.11':'Validate resumed production per cavity','m2.12':'Accept product or restart purge',
     'm2.13':'Segregate purge stream for allowed recovery',
    }
    M2_EDGES = [(f'm2.{i:02d}',f'm2.{i+1:02d}','SEQUENCE') for i in range(1,12)] + [
     ('m2.01','m2.04','dependsOn old identity'),('m2.03','m2.09','dependsOn rheology'),
     ('m2.04','m2.07','dependsOn retained contamination'),('m2.05','m2.09','dependsOn pressure/flow'),
     ('m2.06','m2.13','material transfer'),('m2.09','m2.13','material transfer'),
     ('m2.07','m2.09','BRANCH not clear'),('m2.12','m2.06','RETRY bounded qualified recipe'),
    ]

    def free_shape(y1,y2,f1,f2):
     if f1 == f2: raise ValueError('identical preload is unidentifiable')
     return (f2*y1-f1*y2)/(f2-f1)

    def crf(r,n):
     return r*(1+r)**n/((1+r)**n-1)

    def washout(masses, flows, threshold):
     if not 0 < threshold < 1 or any(x<=0 for x in masses+flows): raise ValueError('domain')
     required=[m/q*math.log(1/threshold) for m,q in zip(masses,flows)]
     finish=max(required)
     all_open=sum(flows)*finish
     close_cleared=sum(q*t for q,t in zip(flows,required))
     c_all=[math.exp(-q*finish/m) for m,q in zip(masses,flows)]
     c_route=[threshold]*len(masses)
     return finish,required,all_open,close_cleared,c_all,c_route

    def main():
     checks=0
     for g in [-100,0,10,100]:
      for c in [0,.001,.04,.2]:
       for f1,f2 in [(1000,500),(1000,100),(500,100)]:
        assert math.isclose(free_shape(g+c*f1,g+c*f2,f1,f2),g,abs_tol=1e-10)
        checks+=1
     try: free_shape(10,10,500,500)
     except ValueError: checks+=1
     else: raise AssertionError('unidentifiable state accepted')
     g,c,d=10,.04,.00001
     y1,y2=g+c*1000+d*1000**2,g+c*500+d*500**2
     wrong=free_shape(y1,y2,1000,500)
     assert math.isclose(wrong,5) # Actual g0=10: curvature gives -d*f1*f2 bias.
     checks+=1
     sigma0=.5*math.sqrt(1000**2+500**2)/500
     assert math.isclose(sigma0,math.sqrt(5)/2); checks+=1
     finish,required,all_open,routed,c_all,c_route=washout([1.,1.],[.9,.1],.001)
     old_initial=2.
     old_out_all=sum(1-c for c in c_all)
     old_out_route=sum(1-c for c in c_route)
     assert math.isclose(old_out_all+sum(c_all),old_initial);checks+=1
     assert math.isclose(old_out_route+sum(c_route),old_initial);checks+=1
     assert all(c<=.001+1e-15 for c in c_all+c_route);checks+=1
     conventional_optimal=sum(m*math.log(1/.001) for m in [1.,1.])
     assert math.isclose(routed,conventional_optimal);checks+=1
     balanced=washout([1.,1.],[.5,.5],.001)
     assert math.isclose(balanced[2],balanced[3]);checks+=1
     annual_cost=100000*crf(.08,10)+5000
     probe_cost=100000*5/3600*60
     gross_m1=100000*.01*120
     gross_m2=500*(all_open-routed)*(4-1)
     print('SYNTHETIC EQUATION REPLAY; NO FIELD VALIDATION; NO NOVELTY CLAIM')
     print('M1 graph',len(M1_NODES),'situations',len(M1_EDGES),'edges')
     print('M2 graph',len(M2_NODES),'situations',len(M2_EDGES),'edges')
     print('checks',checks)
     print('M1: inferred free shape',free_shape(50,30,1000,500),'um; independent noise sd',sigma0,'um')
     print('M1 curvature falsifier: inferred',wrong,'um vs true10um')
     print('M1 gross/annualizednetUSD',gross_m1,gross_m1-probe_cost-annual_cost)
     print('M2 finish minutes',finish,'branch close minutes',required)
     print('M2 all-open/routed/conventional-optimal purge kg',all_open,routed,conventional_optimal)
     print('M2 terminal old species kg all-open/routed',sum(c_all),sum(c_route))
     print('M2 gross/annualizednetUSD',gross_m2,gross_m2-annual_cost)
     print('M2 Garden increment over known optimal gating=0 in this model')
     print('M1/M2 field increment and novel status remain UNKNOWN/KNOWN respectively')
     print('Shared assumed K=100000USD,O=5000USD/y,r=.08,n=10; annualized cost',annual_cost)

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        main()
    finish, required, all_open, routed, c_all, c_route=washout([1.,1.],[.9,.1],.001)
    fixed=100000*crf(.08,10)+5000
    m1_gross=100000*.01*120
    m1_time=100000*5/3600*60
    m2_gross=500*(all_open-routed)*3
    return dict(transcript=buffer.getvalue(), M1=dict(gross_usd_y=m1_gross,
        net_usd_y=m1_gross-m1_time-fixed,
        break_even_scrap_fraction=(m1_time+fixed)/(100000*120)),
        M2=dict(gross_usd_y=m2_gross,net_usd_y=m2_gross-fixed,
        break_even_purge_kg_change=fixed/(500*3),
        incremental_vs_known_optimal_usd_y=0.,
        terminal_old_species_kg_all_open=sum(c_all),terminal_old_species_kg_routed=sum(c_route)),
        graph_counts=dict(M1_nodes=len(M1_NODES),M1_edges=len(M1_EDGES),
                          M2_nodes=len(M2_NODES),M2_edges=len(M2_EDGES)))


def situation_graphs():
    """Finite process/dependency adjacency; full typed node contracts in section 4.12.

    IDs are case-local situation numbers, not new Garden object or relation types.
    Sequence edges and dependencies are distinguished. Neither coverage counts nor
    graph connectivity establish empirical validity or completeness of the domain.
    """
    def chain(n):
        return [(i, i + 1) for i in range(1, n)]

    graphs = {
        'H1': (9, chain(8), [(4,9),(7,9),(9,8)]),
        'H2': (8, chain(8), [(1,4)]),
        'H3': (9, [(9,1),(1,2),(2,3),(3,8),(2,4),(4,5),(5,6),(5,7),(6,8)], []),
        'U1': (12, [(1,2),(2,3),(3,4),(4,5),(4,6),(7,8),(7,9),(7,10),
                    (8,11),(9,10),(10,12),(12,11),(11,1)], [(5,7),(6,7),(2,7)]),
        'U2': (12, chain(12), [(7,4),(2,4),(4,6),(9,6),(6,3)]),
        'U3': (12, [(1,2),(2,3),(3,6),(6,7),(7,8),(7,9),(8,10),(9,10),
                    (10,11),(11,1)], [(4,7),(5,7),(3,7),(2,9),(1,8),(11,12),(9,12)]),
        'F1': (13, chain(13), [(1,3),(2,4),(4,6),(5,7),(5,8),(6,9),
                              (7,9),(8,10),(9,11),(12,3),(13,1)]),
        'F2': (15, chain(15), [(1,5),(1,6),(3,7),(5,9),(5,11),(6,9),
                              (7,11),(8,12),(9,12),(10,12),(12,14),(13,15)]),
        'M1': (15, chain(15), [(1,10),(2,10),(5,10),(6,11),(3,12),(11,5),(11,15),(15,6)]),
        'M2': (13, chain(12), [(1,4),(3,9),(4,7),(5,9),(6,13),(9,13),(7,9),(12,6)]),
    }
    result = {}
    for ident, (nodes, process, dependency) in graphs.items():
        edges = process + dependency
        if len(set(edges)) != len(edges):
            raise ValueError(f'duplicate graph edge: {ident}')
        if any(not (1 <= a <= nodes and 1 <= b <= nodes) for a,b in edges):
            raise ValueError(f'graph references missing situation: {ident}')
        if {v for edge in edges for v in edge} != set(range(1, nodes + 1)):
            raise ValueError(f'unconnected declared situation: {ident}')
        result[ident] = dict(situations=nodes, edges=len(edges),
            process_edges=process, dependencies_or_feedback=dependency)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--details',action='store_true')
    args=parser.parse_args()
    h,u,f,m=heat_material(),utilities(),food_cold(),manufacturing()
    graphs=situation_graphs()
    rows=[
      ('H1','Hot aluminium ash separation',h['H1']['net_usd_y'],'ASSUMED yield; known mechanism'),
      ('H2','Selective slab cooling/core heat retention',h['H2']['net_usd_y'],'IDEAL upper scenario vs full cooling; known sequence'),
      ('H3','Cement mineral return with chloride purge',h['H3']['net_usd_y'],'ASSUMED additional clean recovery; known family'),
      ('U1','Phase-qualified condensate return',u['U1']['net_usd_y'],'ASSUMED qualifying events; known separation'),
      ('U2','Staggered tower blowdown',None,'DEFEATED by ordinary continuous blowdown'),
      ('U3','Temperature-matched thermal storage',u['U3']['net_usd_y'],'CONDITIONAL vs early cutoff; modern comparator ties'),
      ('F1','Defrost moisture capture on frozen section',f['F1']['net_two_distinct_bills_usd_y'],'NEGATIVE generous two-bill scenario; hot-gas case cannot assume purchased electric heat'),
      ('F2','Hot pressure-coded tracer leak test',None,'NO demonstrated sensitivity advantage; field value UNKNOWN'),
      ('M1','Two-preload released-shape estimation',m['M1']['net_usd_y'],'ASSUMED scrap improvement; known compensation family'),
      ('M2','Branch-resolved resin purge',m['M2']['net_usd_y'],'CONDITIONAL vs all-open purge; known optimal gating ties')]
    print('USD per facility per year; hypothetical after OPEX and annualized CAPEX.')
    print('No row establishes novel or measured Garden incremental savings.')
    for ident,title,net,status in rows:
        print(f"{ident} | {title} | {'UNKNOWN/REJECTED' if net is None else f'{net:,.2f}'} | {status}")
    print('F2 break-even incremental avoided loss/year:',round(f['F2']['incremental_avoided_loss_needed_usd_y'],2))
    print('U2 receiver peaks mg/L:',{k:round(u['U2'][k]['reactor_peak_mg_L'],3)
        for k in ('synchronous','staggered','continuous_baseline')})
    print('H1 repair net with existing 50% fines recovery:',round(h['H1R_existing_50pct_recovery']['net_usd_y'],2))
    print('Checked branches:',h['contract_checks'],'heat/material checks;',u['contract_checks'],'utility checks; manufacturing and food/null checks executed.')
    print('Bounded graph inventory:',sum(g['situations'] for g in graphs.values()),
          'situations;',sum(g['edges'] for g in graphs.values()),
          'process/dependency edges. No exhaustive denominator or validation percentage.')
    if args.details:
        print('GRAPHS',graphs)
        for label,result in [('HEAT',h),('UTILITIES',u),('FOOD',f),('MANUFACTURING',m)]:
            print(label,result)
    print('Novelty unresolved or rejected as described; no global sum or operational permission.')


if __name__=='__main__':
    main()
