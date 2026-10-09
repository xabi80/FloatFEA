# F6 step 1 — API RP 2A-WSD utilisations, INDICATIVE

**A sizing screen, not a compliance calculation.** The labels below are the deliverable as much as the numbers are.

* INDICATIVE SIZING SCREEN -- NOT A CODE CASE. API RP 2A-WSD working-stress checks on a STAND-IN TUBE that is the stiffness equivalent of a triangulated truss of undecided depth (F1.md:390).
* Fy = 355 MPa (S355; ASSUMED). No one-third increase (EZ4 Q2, locked): section 3.1.2's increase is written for a declared extreme event and these are screening design waves with no return period.
* K = 2.0 for every arm, L = member length (EZ4 Q3): a cantilever from the body centre, the gimbal end on a floating body giving no reliable lateral restraint. A K = 1.0 column is reported beside it (FA2).
* C_m = 0.85 (section 3.3.1 case (a); members in frames subject to joint translation), consistent with K = 2.0's sidesway assumption. C_m MULTIPLIES the bending term, so C_m = 1.0 RAISES the compression utilisation and 0.85 is the LESS onerous of the two (R743). A C_m = 1.0 column is reported beside the K = 1.0 one (FB2).
* G6.1 is GREEN: every clause is verified against an independent hand calculation in tests/verification/rung5/, at two or more points per branch, either side of every boundary (FB0). R742: F_b is capped at 0.75 Fy -- the first reduced branch exceeded it to D/t = 30.60. R741: section 3.2.2(b) local buckling is implemented and D/t > 300 is refused rather than extrapolated.
* Governing basis: T = 12.5; 14; 15; 16.2 s (EZ2). T = 10 s and T = 20 s are outside the associated-period range for H = 24.2 m -- T = 10 s exceeds the breaking steepness -- and cannot govern.
* ROOT and TIP only (FA3). The MID column waits on R730's discharge: its closed form is a measured 4.0% approximation on bending, unverified against a refined mesh.
* Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms; platform inertia scaled with mass (assumed). ER0. Hub line mass 15 t/m against the platform arms' 10.3 t/m.
* DZ5 / ER1(e): the hub arms carry an equivalent density above steel (11433.5 against 7850 kg/m^3), so the mass does not fit inside F1's section at f = 0.75.
* EX3 / R724: all cases are heading 0 degrees. The heading dependence is UNTESTED, and the governing component on the transverse arms is entirely dynamic.
* R740: the utilisations are computed from F4's `total_instant` rows -- the six components AT the step where sigma peaks. The `total_max`/`total_min` envelope is a per-component upper bound whose values do not occur together, and it is NOT used here.
* R739: F4's N column is tension-positive (docs/conventions.md:320). It was published compression-positive, which put every over-unity station on section 3.3.1 instead of 3.3.2 and reported F_a = 213.00 MPa where the column allowable is 73.25 (platform, elastic) or 161.02 (hubs, inelastic).

## The ten most utilised member-stations

| # | body | member | station | case | governing clause | U (K=2) | U (K=1) | U (C_m=1) |
|---|---|---|---|---|---|---|---|---|
| 1 | platform | `platform:hub2_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 1.712 | 1.712 | 1.714 |
| 2 | platform | `platform:hub4_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 1.712 | 1.712 | 1.714 |
| 3 | platform | `platform:hub3_arm` | ROOT | T = 16.2 s | 3.3.1 interaction | 1.182 | 1.182 | 1.182 |
| 4 | platform | `platform:hub1_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 1.177 | 1.177 | 1.177 |
| 5 | hub3 | `hub3:buoy8_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.808 | 0.808 | 0.808 |
| 6 | hub3 | `hub3:buoy9_arm` | ROOT | T = 12.5 s | 3.3.1 interaction | 0.808 | 0.808 | 0.808 |
| 7 | hub1 | `hub1:buoy2_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 0.790 | 0.790 | 0.796 |
| 8 | hub1 | `hub1:buoy3_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 0.790 | 0.790 | 0.796 |
| 9 | hub2 | `hub2:buoy6_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 0.788 | 0.788 | 0.793 |
| 10 | hub4 | `hub4:buoy11_arm` | ROOT | T = 12.5 s | 3.3.2 interaction | 0.788 | 0.788 | 0.793 |

## FA2: how little the axial term contributes

| # | member | station | f_a (MPa) | F_a (MPa) | u_axial | f_b (MPa) | F_b (MPa) | u_bending | axial branch |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `platform:hub2_arm` | ROOT | 0.06 | 73.19 | 0.0008 | 455.7 | 266.2 | 1.711 | elastic |
| 2 | `platform:hub4_arm` | ROOT | 0.06 | 73.19 | 0.0008 | 455.7 | 266.2 | 1.711 | elastic |
| 3 | `platform:hub3_arm` | ROOT | 0.41 | 213.00 | 0.0019 | 314.3 | 266.2 | 1.180 | tension |
| 4 | `platform:hub1_arm` | ROOT | 4.92 | 213.00 | 0.0231 | 307.2 | 266.2 | 1.154 | tension |
| 5 | `hub3:buoy8_arm` | ROOT | 1.43 | 213.00 | 0.0067 | 213.4 | 266.2 | 0.801 | tension |
| 6 | `hub3:buoy9_arm` | ROOT | 1.43 | 213.00 | 0.0067 | 213.4 | 266.2 | 0.801 | tension |
| 7 | `hub1:buoy2_arm` | ROOT | 1.32 | 161.08 | 0.0082 | 208.8 | 266.2 | 0.784 | inelastic |
| 8 | `hub1:buoy3_arm` | ROOT | 1.32 | 161.08 | 0.0082 | 208.8 | 266.2 | 0.784 | inelastic |
| 9 | `hub2:buoy6_arm` | ROOT | 1.16 | 161.08 | 0.0072 | 208.4 | 266.2 | 0.783 | inelastic |
| 10 | `hub4:buoy11_arm` | ROOT | 1.16 | 161.08 | 0.0072 | 208.4 | 266.2 | 0.783 | inelastic |

## The section and the slenderness

* `D = 2.5000 m`, `t = 0.18000 m`, `D/t = 13.9` — **compact**, so § 3.2.3 gives `F_b = 0.75 F_y = 266.25 MPa`.
* `A = 1.3119 m²`, `W = 0.7104 m³`, `W_t = 1.4208 m³`.
* `C_m = 0.85` (§ 3.3.1 case (a), members in frames subject to joint translation — consistent with `K = 2.0`'s sidesway assumption). `C_m` multiplies the bending term, so the `C_m = 1.0` column is the HIGHER of the two (R743).

| body | L (m) | KL/r at K=2 | KL/r at K=1 | branch at K=2 |
|---|---|---|---|---|
| hub1 | 25 | 60.8 | 30.4 | **inelastic** |
| hub2 | 25 | 60.8 | 30.4 | **inelastic** |
| hub3 | 25 | 60.8 | 30.4 | **inelastic** |
| hub4 | 25 | 60.8 | 30.4 | **inelastic** |
| platform | 50 | 121.5 | 60.8 | **elastic** |

**The `K = 2.0` lock moves the platform arms onto a different formula** — at `K = 1.0` every arm is inelastic and at `K = 2.0` the 50 m platform arms cross `C_c = 108.06` into § 3.2.2's elastic branch. How much it moves a utilisation, and how much `C_m` does, are the two numbers FA2 and FB2 ask for:

```
axial branch over 32 rows : elastic 4; inelastic 13; tension 15
largest |U(K=2) - U(K=1)|      : 0.034238  at platform:hub1_arm TIP (elastic)
largest |U(C_m=1) - U(C_m=0.85)| : 0.009245  at hub4:buoy10_arm ROOT (inelastic)
worst compression station      : U = 1.71167
section 3.3.2 over 17 compression rows: AMPLIFIED governs on 7, SIMPLE on 10  (read from interaction_form, not inferred -- R752)
C_m visibly moves U on 10 of 17 -- a DIFFERENT question, and its answer is the bending-dominated ROOTs
worst station platform:hub2_arm ROOT: u_axial = 0.000833  u_bending = 1.71138  (3.3.2 interaction, elastic)
```

**Bending governs and the axial term is three orders smaller** — the ratio is in the block above, at the worst station, read from the row the table publishes. Neither modelling lever moves the governing number much, and the reason is the clause rather than the structure: § 3.3.2 takes the larger of its amplified and simple forms, the simple form carries no `F_a` and no `C_m`, and it is the one that governs wherever bending dominates.

**4 of 32 member-stations exceed `U = 1.0`**, the worst at `1.712`. They are on platform, at ROOT, and the governing clause is 3.3.1 interaction on 2; 3.3.2 interaction on 2.

## What this does NOT do

* **No MID station** (FA3) — it waits on R730's discharge.
* **No circumferential stress recovery**, no CalculiX cross-check, no VTK. Those are G6.2 and F7.
* **No one-third increase** (EZ4 Q2).
* **No hydrostatic or shell-buckling check.** The buoy cans are DNV-RP-C202 and F7.
