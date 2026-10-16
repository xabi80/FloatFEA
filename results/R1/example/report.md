# FloatFEA run report

**INDICATIVE SIZING SCREEN -- NOT A CODE CASE. Produced by `floatfea run` from a declared configuration. The section is a stiffness stand-in for a truss of undecided depth (docs/milestones/F1.md:389-390).**

## What was configured

* **config** — platform12_placeholder.yaml
* **deck** — data/platform/platform12_deck.yaml
* **hsp_tag** — (pinned HSP state; see docs/hsp-coupling.md and floatfea/hsp_pin.py)
* **froude_lambda** — 50.0
* **mass_distribution** — {'hub1': 'f = 0.75', 'hub2': 'f = 0.75', 'hub3': 'f = 0.75', 'hub4': 'f = 0.75', 'platform': 'f = 0.75'}
* **sections** — {'hub1': 'D = 2.5 m, t = 0.18 m', 'hub2': 'D = 2.5 m, t = 0.18 m', 'hub3': 'D = 2.5 m, t = 0.18 m', 'hub4': 'D = 2.5 m, t = 0.18 m', 'platform': 'D = 2.5 m, t = 0.18 m'}
* **material** — E = 2.1e+11 Pa, G = 8.07692e+10 Pa, rho = 7850 kg/m^3, Fy = 3.55e+08 Pa
* **load_cases** — npz data/f4/dynamic_inputs.npz
* **governing_periods_s** — [12.5, 14.0, 15.0, 16.2]
* **window_rule** — the committed window per case; see data/f4/dynamic_inputs.provenance.json
* **study_only** — no
* **code_check_sensitivities** — K_sensitivity = 1, Cm_sensitivity = 1
* **code_check** — K = 2, Cm = 0.85, one-third increase OFF

## The wave basis these loads were exported at

* **heading** — 0.0 deg
* **wave height** — 24.2 m full scale (0.484 m model)
* **window** — DQ6: the last 5 whole periods, starting no earlier than ramp + 10

## What this run assumes, as the builder records it

* **build label** — buoy spar columns not assessed as members; buoy loads applied as joint reactions; platform mass properties as in FloatSim; see DZ5 finding
* the deck's `reference_point` IS the body's CoG. FloatSim's own `driver.py:203-209` states it -- "the deck's reference_point IS the body frame origin and the CoG (no explicit CoG-offset field in the deck)" -- so the referent is declared upstream rather than in the deck, and G3.1a compares against it on that basis.
* FROUDE-SCALED from model scale to full scale at lambda = 50 by floatfea.io.froude.
* the in-plane members are STIFFNESS equivalents of a truss with depth, not mass models (DY0). Steel density is not used for member mass: four 50 m platform arms at F1's section in steel weigh 2059.7 t against a 1250.0 t body. The mass splits by fraction instead, and the members carry it as a uniform line mass through an equivalent density.
* no buoy mass is in the model: each buoy's inertia reaches the arm tip through its gimbal reaction, and a lumped buoy mass beside it would double-count.
* the frame is a tree -- nothing joins adjacent hubs or adjacent buoy joints -- so each body is statically determinate and there is no redundancy. This is an observation about the platform.
* the deck's body inertias are kept AS FLOATSIM HAS THEM, because inertia-relief equilibrium with FloatSim's loads requires it, and they are physically inconsistent: every body's J_G satisfies the LAMINA identity exactly -- triangle-inequality slack 0.0000e+00 -- and the platform's is M * 50^2 * (1, 1, 2) exactly, giving a radius of gyration about z of 70.711 m against 50 m arms and a 51.056 m extent. The remainder inertia the split leaves is PSD but violates the triangle inequality by -2.6770e+08 kg.m^2 on the platform and -1.0153e+06 on each hub. See the DZ5 finding.

## Findings the build raised, per body

* `platform` — platform: the mass fraction is 0.75, handed in by the caller rather than taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for it. This body is a MEASUREMENT, not one to ship.
* `hub1` — hub1: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850. The members are stiffness equivalents so a density above steel is not impossible, but it means this body's mass does not fit inside F1's section at the chosen fraction and the section or the fraction is the thing to look at.
* `hub1` — hub1: the mass fraction is 0.75, handed in by the caller rather than taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for it. This body is a MEASUREMENT, not one to ship.
* `hub2` — hub2: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850. The members are stiffness equivalents so a density above steel is not impossible, but it means this body's mass does not fit inside F1's section at the chosen fraction and the section or the fraction is the thing to look at.
* `hub2` — hub2: the mass fraction is 0.75, handed in by the caller rather than taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for it. This body is a MEASUREMENT, not one to ship.
* `hub3` — hub3: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850. The members are stiffness equivalents so a density above steel is not impossible, but it means this body's mass does not fit inside F1's section at the chosen fraction and the section or the fraction is the thing to look at.
* `hub3` — hub3: the mass fraction is 0.75, handed in by the caller rather than taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for it. This body is a MEASUREMENT, not one to ship.
* `hub4` — hub4: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850. The members are stiffness equivalents so a density above steel is not impossible, but it means this body's mass does not fit inside F1's section at the chosen fraction and the section or the fraction is the thing to look at.
* `hub4` — hub4: the mass fraction is 0.75, handed in by the caller rather than taken from (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for it. This body is a MEASUREMENT, not one to ship.

## What the columns mean

* R739: the N column is TENSION-POSITIVE (docs/conventions.md:320). Published compression-positive it put every over-unity station on section 3.3.1 instead of 3.3.2.
* R740: a utilisation must be read from the `total_instant` rows -- the six components AT the step where sigma peaks. `total_max` / `total_min` max each component INDEPENDENTLY over the window, so their six values do not occur together and a stress formed from them is an UPPER BOUND, not a stress at any instant.
* FA3: ROOT and TIP are the element's two ends and are exact. MID is a closed form whose bending term is a measured 4.0% approximation, unverified against a refined mesh (R730).
* EZ2: only the declared governing periods may set the envelope. Cases outside the associated-period range for this wave height -- and any exceeding the deep-water breaking steepness -- are reported as SENSITIVITY ONLY and cannot govern.
* EX3 / R724: the heading these loads were exported at is in the provenance above. Where a run covers a SINGLE heading the heading dependence is UNTESTED, and no column here is evidence about any other heading.
* FA0: a governing period sitting just below the associated-period band's lower bound is admitted by FA0's ruling rather than by rounding. Which period governs is a RESULT of this run and is in the period column; it is not a property of the band.
* FA1: a generic 0.6*Fy reference stress is NOT the API bending allowable and is SUPERSEDED by the clause results in these columns. Section 3.2.3's branches decide the bending allowable from D/t, not from 0.6*Fy.
* R741 / R742: section 3.2.2(b) local buckling is implemented, and the D/t ceiling is 300000/Fy[MPa] -- 845.1 at Fy = 355 MPa -- above which the section is refused rather than extrapolated. F_b = 0.75*Fy IS the compact allowable; section 3.2.3's reductions apply above the compact limit, not below it. Every clause is verified against an independent hand calculation in tests/verification/rung5/.
* R743: C_m MULTIPLIES the bending term in section 3.3.1's interaction, so a LARGER C_m RAISES the compression utilisation. The value used is in the provenance above, and the run reports a one-variable sensitivity beside it.

## The governing utilisation

**U = 1.71167** at `platform:hub4_arm` ROOT, `T_full = 12.5 s`, basis `total_instant`, governing clause 3.3.2 interaction.

Checked stations: 32. Over unity: 4.

## Mass, per body

Body totals, centre of gravity and inertia come FROM THE DECK. The residual below
is `deck - member - remainder`, formed from its own terms (G4.1) and reported per
body rather than summed, because two bodies out in opposite directions would cancel.

| body | f | deck mass (kg) | member (kg) | remainder (kg) | residual (kg) | rho_eq (kg/m^3) | PSD |
|---|---|---|---|---|---|---|---|
| `platform` | 0.75 | 2.500000e+06 | 1.875000e+06 | 6.250000e+05 | +0.000e+00 | 7146.0 | OK |
| `hub1` | 0.75 | 1.500000e+06 | 1.125000e+06 | 3.750000e+05 | +0.000e+00 | 11433.5 | OK |
| `hub2` | 0.75 | 1.500000e+06 | 1.125000e+06 | 3.750000e+05 | +0.000e+00 | 11433.5 | OK |
| `hub3` | 0.75 | 1.500000e+06 | 1.125000e+06 | 3.750000e+05 | +0.000e+00 | 11433.5 | OK |
| `hub4` | 0.75 | 1.500000e+06 | 1.125000e+06 | 3.750000e+05 | +0.000e+00 | 11433.5 | OK |

## Wall time

| stage | seconds |
|---|---|
| build | 0.12 |
| load | 0.00 |
| solve | 66.49 |
| code_check | 0.00 |
| total | 66.62 |

## Declared, and what became of it

* G = 80769230769.23077 Pa is DERIVED by the model from E and nu = 0.3; the declared value was checked for exact agreement, not injected.
* rho was declared as 7850 kg/m^3 (nominal) and is BACK-COMPUTED per body so that rho * A is the deck's own line mass whatever the section is. Equivalent densities: hub1 11433.5, hub2 11433.5, hub3 11433.5, hub4 11433.5, platform 7146.0.
* DZ5 / ER1(e): hub1, hub2, hub3, hub4 carry an equivalent density ABOVE the declared nominal, so the deck's mass does not fit inside the declared section at this fraction. This is a recorded finding about the configuration, not an error.

## Limitations this run does not escape

* The section is a **stiffness stand-in** for a triangulated truss of undecided
  depth (`docs/milestones/F1.md:389-390`), so these are indicative sizes.
* **Linear Airy waves** and a **rigid-body** FloatSim; the superstructure only.
* The grade is **assumed** (S355), not certified.
* **No joint or connection checks**, no fatigue, no shell sub-models.
* API RP 2A-WSD is applied as a **working-stress screen**, with no one-third
  increase (EZ4 Q2, locked).
