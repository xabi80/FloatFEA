# F6 step 1 — API RP 2A-WSD utilisations, INDICATIVE

**A sizing screen, not a compliance calculation.** The labels below are the deliverable as much as the numbers are.

* INDICATIVE SIZING SCREEN -- NOT A CODE CASE. API RP 2A-WSD working-stress checks on a STAND-IN TUBE that is the stiffness equivalent of a triangulated truss of undecided depth (F1.md:390).
* Fy = 355 MPa (S355; ASSUMED). No one-third increase (EZ4 Q2, locked): section 3.1.2's increase is written for a declared extreme event and these are screening design waves with no return period.
* K = 2.0 for every arm, L = member length (EZ4 Q3): a cantilever from the body centre, the gimbal end on a floating body giving no reliable lateral restraint. A K = 1.0 column is reported beside it (FA2).
* Governing basis: T = 12.5; 14; 15; 16.2 s (EZ2). T = 10 s and T = 20 s are outside the associated-period range for H = 24.2 m -- T = 10 s exceeds the breaking steepness -- and cannot govern.
* ROOT and TIP only (FA3). The MID column waits on R730's discharge: its closed form is a measured 4.0% approximation on bending, unverified against a refined mesh.
* Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms; platform inertia scaled with mass (assumed). ER0. Hub line mass 15 t/m against the platform arms' 10.3 t/m.
* DZ5 / ER1(e): the hub arms carry an equivalent density above steel (11433.5 against 7850 kg/m^3), so the mass does not fit inside F1's section at f = 0.75.
* EX3 / R724: all cases are heading 0 degrees. The heading dependence is UNTESTED, and the governing component on the transverse arms is entirely dynamic.
* The utilisations are computed from F4's PER-INSTANT stresses where available; the per-component envelope is an upper bound and is reported separately in F4's table.

## The ten most utilised member-stations

| # | body | member | station | case | governing clause | U (K=2) | U (K=1) |
|---|---|---|---|---|---|---|---|
| 1 | platform | `platform:hub2_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 1.815 | 1.815 |
| 2 | platform | `platform:hub4_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 1.814 | 1.814 |
| 3 | platform | `platform:hub3_arm` | ROOT | T = 16.2 s | 3.3.1 interaction | 1.202 | 1.202 |
| 4 | platform | `platform:hub1_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 1.188 | 1.188 |
| 5 | hub3 | `hub3:buoy9_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.816 | 0.816 |
| 6 | hub3 | `hub3:buoy8_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.815 | 0.815 |
| 7 | hub1 | `hub1:buoy2_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.814 | 0.814 |
| 8 | hub1 | `hub1:buoy3_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.814 | 0.814 |
| 9 | hub2 | `hub2:buoy6_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.806 | 0.806 |
| 10 | hub4 | `hub4:buoy11_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.804 | 0.804 |

## FA2: how little the axial term contributes

| # | member | station | f_a (MPa) | F_a (MPa) | u_axial | f_b (MPa) | F_b (MPa) | u_bending | axial branch |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `platform:hub2_arm` | ROOT | 0.08 | 213.00 | 0.0004 | 483.1 | 266.2 | 1.815 | tension |
| 2 | `platform:hub4_arm` | ROOT | 0.08 | 213.00 | 0.0004 | 482.8 | 266.2 | 1.813 | tension |
| 3 | `platform:hub3_arm` | ROOT | 4.58 | 213.00 | 0.0215 | 314.3 | 266.2 | 1.181 | tension |
| 4 | `platform:hub1_arm` | ROOT | 7.23 | 213.00 | 0.0340 | 307.3 | 266.2 | 1.154 | tension |
| 5 | `hub3:buoy9_arm` | ROOT | 1.43 | 213.00 | 0.0067 | 215.4 | 266.2 | 0.809 | tension |
| 6 | `hub3:buoy8_arm` | ROOT | 1.43 | 213.00 | 0.0067 | 215.2 | 266.2 | 0.808 | tension |
| 7 | `hub1:buoy2_arm` | ROOT | 1.34 | 213.00 | 0.0063 | 215.0 | 266.2 | 0.808 | tension |
| 8 | `hub1:buoy3_arm` | ROOT | 1.34 | 213.00 | 0.0063 | 215.0 | 266.2 | 0.807 | tension |
| 9 | `hub2:buoy6_arm` | ROOT | 1.16 | 213.00 | 0.0055 | 213.0 | 266.2 | 0.800 | tension |
| 10 | `hub4:buoy11_arm` | ROOT | 1.16 | 213.00 | 0.0055 | 212.7 | 266.2 | 0.799 | tension |

## The section and the slenderness

* `D = 2.5000 m`, `t = 0.18000 m`, `D/t = 13.9` — **compact**, so § 3.2.3 gives `F_b = 0.75 F_y = 266.25 MPa`.
* `A = 1.3119 m²`, `W = 0.7104 m³`, `W_t = 1.4208 m³`.
* `C_m = 0.85` (§ 3.3.2, no transverse load — a declared input).

| body | L (m) | KL/r at K=2 | KL/r at K=1 | branch at K=2 |
|---|---|---|---|---|
| hub1 | 25 | 60.8 | 30.4 | **inelastic** |
| hub2 | 25 | 60.8 | 30.4 | **inelastic** |
| hub3 | 25 | 60.8 | 30.4 | **inelastic** |
| hub4 | 25 | 60.8 | 30.4 | **inelastic** |
| platform | 50 | 121.5 | 60.8 | **elastic** |

**The `K = 2.0` lock moves the platform arms onto a different formula** — at `K = 1.0` every arm is inelastic and at `K = 2.0` the 50 m platform arms cross `C_c = 108.06` into § 3.2.2's elastic branch — **but it barely moves a utilisation**, and that is the quantitative answer to FA2:

```
axial branch over 256 rows : elastic 32; inelastic 96; tension 128
largest |U(K=2) - U(K=1)|      : 0.024114  at platform:hub1_arm TIP (elastic)
worst compression station      : U = 1.70984  with U(K=1) identical
```

**Bending governs everywhere and the axial term is three orders smaller.** At the worst station `u_axial = 0.0004` against `u_bending = 1.815`, so § 3.3's interaction is bending plus a rounding error, the `C_m / (1 - f_a/F_e')` amplification never bites, and on the compression rows the simple `0.6 F_y` form of § 3.3.2 governs over the amplified one — which has no `K` in it at all. **The `K` question, which looked like the biggest modelling choice in the check, changes the governing number by at most `0.024`.** It would matter on a member carrying real axial load; none of these does.

**4 of 32 member-stations exceed `U = 1.0`**, the worst at `1.815`. All four are platform arm ROOTs, all governed by § 3.3.1, and all on bending.

## What this does NOT do

* **No MID station** (FA3) — it waits on R730's discharge.
* **No circumferential stress recovery**, no CalculiX cross-check, no VTK. Those are G6.2 and F7.
* **No one-third increase** (EZ4 Q2).
* **No hydrostatic or shell-buckling check.** The buoy cans are DNV-RP-C202 and F7.
