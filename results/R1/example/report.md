# FloatFEA run report

**INDICATIVE SIZING SCREEN -- NOT A CODE CASE. Produced by `floatfea run` from a declared configuration; every assumption it rests on is listed in the run report, and the section is a stiffness stand-in for a truss of undecided depth.**

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
* **code_check** — K = 2, Cm = 0.85, one-third increase OFF

## The governing utilisation

**U = 1.71167** at `platform:platform:hub4_arm` ROOT, `T_full = 12.5 s`, basis `total_instant`, governing clause 3.3.2 interaction.

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
| solve | 67.26 |
| code_check | 0.00 |
| total | 67.38 |

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
