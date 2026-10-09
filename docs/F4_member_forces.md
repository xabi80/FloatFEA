# F4 step 3 — member forces, PRELIMINARY

**Every line below is preliminary until F4 closes.** The labels are the deliverable as much as the numbers are.

* PRELIMINARY until F4 closes.
* Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms (Xabier, 6 Oct); platform inertia scaled with mass (assumed). ER0.
* DZ5 / ER1(e): the four hub arms carry an equivalent density above steel (11433.5 kg/m^3 against 7850), which is a reported sizing finding -- the members are stiffness equivalents, so the hub's mass does not fit inside F1's section at f = 0.75.
* Hub line mass 15 t/m, against the platform arms' 10.3 t/m.
* Stand-in tube: the stiffness equivalent of a TRIANGULATED TRUSS of undecided depth (F1.md:390). Stresses are INDICATIVE, not a check on a real section.
* EX3 / R724: all six cases are heading 0 degrees. The heading dependence is UNTESTED.
* R739: the N column is TENSION POSITIVE (docs/conventions.md:320). It was published compression-positive -- a 1 mm stretch gave a negative N -- which put every over-unity station on API section 3.3.1 instead of 3.3.2.
* R740: `total_instant` rows carry the six components AT the step where sigma peaks. `total_max` / `total_min` are the PER-COMPONENT envelope; their six values do not occur together and a utilisation from them is an UPPER BOUND.
* FA1: the 213.0 MPa figure this table compares against is a GENERIC 0.6*Fy REFERENCE; it is SUPERSEDED by F6's API RP 2A-WSD clauses and it is NOT the API bending allowable. For D/t = 13.9 (below 10340/Fy = 29.13) API gives Fb = 0.75*Fy = 266.25 MPa; the generic reference is 1.25x conservative on bending.
* FA0: T = 12.5 s STAYS in the governing set. It is 0.3% below sqrt(6.5*H) = 12.542 s -- within the guidance's precision -- and it was CHOSEN as the band's lower edge. The response rises as T falls across the band, so the lower edge governs and 12.5 s represents it. No new FloatSim run.
* EZ2: the GOVERNING envelope is T = 12.5; 14; 15 and 16.2 s only. T = 10 s and T = 20 s are outside the associated-period range for H = 24.2 m -- and T = 10 s exceeds the deep-water breaking steepness -- so they are reported as SENSITIVITY ONLY and cannot govern. T = 12.5 s sits 0.042 s below the band's lower bound; see the wave-basis table.
* Stations: ROOT = the inboard end at the body's centre node, TIP = the far end. MID is closed-form for a uniform net body force (one element per member at F3's mesh).
* R730: all three stations are INTERNAL ACTIONS in one convention (as seen from the A end), so TIP is `-end_b` and not the raw element end force. An earlier version averaged the two raw ends for MID, which computes a LOAD -- exactly half the member's weight on Vz -- and understated the midspan stress by 46%.
* 'dynamic' is the DYNAMIC INCREMENT about static equilibrium, solved from FloatSim's multipliers with NO gravity -- FloatSim is linearised about equilibrium, so the static weight/buoyancy balance is already in the formulation. 'total' = static + dynamic.
* The load path is validated against FloatSim's own per-body accelerations: 1.55% on all five bodies, 2.78% worst over eighteen samples.
* No code check is applied. API RP 2A-WSD checks are F5 (EY4).
* SCALE: the npz holds FloatSim's MODEL-scale output; the FE model is FULL scale. The multipliers are converted through `floatfea.io.froude`'s declared `joint_multiplier_yaw_locked` composite (force x 125000, locked moment x 6250000).

## The ten most loaded member-stations, by indicative sigma

| # | body | member | station | governing case | sigma at the instant (MPa) | envelope upper bound (MPa) |
|---|---|---|---|---|---|---|
| 1 | platform | `platform:hub4_arm` | ROOT | T = 12.5 s | 455.7 | 482.9 |
| 2 | platform | `platform:hub2_arm` | ROOT | T = 12.5 s | 455.7 | 483.2 |
| 3 | platform | `platform:hub3_arm` | ROOT | T = 16.2 s | 314.7 | 318.9 |
| 4 | platform | `platform:hub1_arm` | ROOT | T = 12.5 s | 312.2 | 314.5 |
| 5 | platform | `platform:hub4_arm` | MID | T = 12.5 s | 253.9 | 269.4 |
| 6 | platform | `platform:hub2_arm` | MID | T = 12.5 s | 253.9 | 269.7 |
| 7 | hub3 | `hub3:buoy9_arm` | ROOT | T = 12.5 s | 214.8 | 216.8 |
| 8 | hub3 | `hub3:buoy8_arm` | ROOT | T = 12.5 s | 214.8 | 216.7 |
| 9 | hub1 | `hub1:buoy3_arm` | ROOT | T = 12.5 s | 210.1 | 216.3 |
| 10 | hub1 | `hub1:buoy2_arm` | ROOT | T = 12.5 s | 210.1 | 216.4 |

## The two cases OUTSIDE the associated-period range (sensitivity only)

**EZ2(b): these do not govern and are not in the table above.** `T = 10 s` exceeds the deep-water breaking steepness and `T = 20 s` is too long for this height, so neither can set a design envelope. They are reported because the response at `T = 10 s` is the largest in the whole sweep and a reader who saw only the governing block would not know that.

| body | member | station | case | sigma at the instant (MPa) |
|---|---|---|---|---|
| platform | `platform:hub2_arm` | ROOT | T = 10 s | 742.6 |
| platform | `platform:hub4_arm` | ROOT | T = 10 s | 742.6 |
| platform | `platform:hub2_arm` | MID | T = 10 s | 384.6 |
| platform | `platform:hub4_arm` | MID | T = 10 s | 384.6 |
| platform | `platform:hub3_arm` | ROOT | T = 20 s | 337.3 |
| platform | `platform:hub1_arm` | ROOT | T = 10 s | 302.6 |
| hub1 | `hub1:buoy3_arm` | ROOT | T = 10 s | 262.5 |
| hub1 | `hub1:buoy2_arm` | ROOT | T = 10 s | 262.5 |
| hub4 | `hub4:buoy11_arm` | ROOT | T = 10 s | 261.7 |
| hub2 | `hub2:buoy6_arm` | ROOT | T = 10 s | 261.7 |

## The wave basis, per case (EZ2(d))

`H = 24.2 m` full scale. Deep-water `lambda = g T^2 / (2 pi)`; the associated-period band is `sqrt(6.5 H) .. sqrt(11 H)`; the breaking limit is `H/lambda = 1/7 = 0.1429`.

| T (s) | lambda (m) | H/lambda | position | basis |
|---|---|---|---|---|
| 10 | 156.1 | 0.1550 | BREAKING (H/L 0.1550 > 1/7); and below the band 12.542-16.316 s | sensitivity only |
| 12.5 | 244.0 | 0.0992 | below the band 12.542-16.316 s by 0.042 s | **governing** |
| 14 | 306.0 | 0.0791 | in the band 12.542-16.316 s | **governing** |
| 15 | 351.3 | 0.0689 | in the band 12.542-16.316 s | **governing** |
| 16.2 | 409.8 | 0.0591 | in the band 12.542-16.316 s | **governing** |
| 20 | 624.5 | 0.0387 | above the band 12.542-16.316 s by 3.684 s | sensitivity only |

**`T = 12.5 s` sits `0.042 s` below `sqrt(6.5 x 24.2) = 12.542 s`, and FA0 RULES THAT IT STAYS.** `0.3%` below the bound is within the guidance's own precision, and the case was CHOSEN as the band's lower edge. The reason it matters is the direction: **the response rises as `T` falls across the band**, so the lower edge is what governs and `12.5 s` is what represents it -- which is also why it carries 8 of the governing top ten. No new FloatSim run.

## The section these stresses are computed on

* `D = 2.5000 m`, `t = 0.18000 m`, `D/t = 13.9` (EN 1993-1-1 class limits 33.1, 46.3, 59.6)
* `A = 1.3119 m^2`, `W = 2I/D = 0.7104 m^3`, `J = 1.7760 m^4`, `W_t = 2J/D = 1.4208 m^3`, `A_shear = kappa A = 0.6961 m^2`
* `docs/milestones/F1.md:389 for the SECTION (stiffness); F1.md:390 records this arm as a TRIANGULATED truss of undecided depth, so the tube is a stiffness equivalent and the member is marked preliminary`


## The `f` sensitivity at the ROOT (static only)

`f` is DY0's fraction of body mass carried on the members; the remainder is lumped at the centre node on a rigid link. **`f = 0.75` is the basis (Xabier, 6 Oct)** and the other two bracket it. The last column is the spread of sigma across a body's own members, which is round-off where the body is symmetric under self-weight.

| f | body | worst root moment (N·m) | sigma (MPa) | spread across members |
|---|---|---|---|---|
| 0.5 | platform | 2.2992e+08 | 323.7 | 3.68e-16 |
| 0.5 | hub1 | 1.4306e+08 | 201.4 | 8.88e-16 |
| 0.5 | hub2 | 1.4306e+08 | 201.4 | 4.44e-16 |
| 0.5 | hub3 | 1.4306e+08 | 201.4 | 4.44e-16 |
| 0.5 | hub4 | 1.4306e+08 | 201.4 | 1.04e-15 |
| 0.75 | platform | 1.9160e+08 | 269.7 | 4.42e-16 |
| 0.75 | hub1 | 1.2773e+08 | 179.8 | 8.29e-16 |
| 0.75 | hub2 | 1.2773e+08 | 179.8 | 1.66e-16 |
| 0.75 | hub3 | 1.2773e+08 | 179.8 | 3.31e-16 |
| 0.75 | hub4 | 1.2773e+08 | 179.8 | 8.29e-16 |
| 1 | platform | 1.5328e+08 | 215.8 | 4.14e-16 |
| 1 | hub1 | 1.1241e+08 | 158.2 | 3.77e-16 |
| 1 | hub2 | 1.1241e+08 | 158.2 | 5.65e-16 |
| 1 | hub3 | 1.1241e+08 | 158.2 | 5.65e-16 |
| 1 | hub4 | 1.1241e+08 | 158.2 | 7.53e-16 |
## What is exact and what is not

* ROOT and TIP are the element's own end nodes: **exact** at F3's mesh.
* MID is **closed-form** for a uniform net body force -- the chord mean plus `w L^2 / 8` on the two bending components. A refined mesh would give it directly.
* `dynamic` is **solved**, not subtracted: the dynamic joint increments with no gravity. `total = static + dynamic`.
* The load path is **validated** against FloatSim's own accelerations -- 1.55% on all five bodies, 2.78% worst over eighteen (case, step, body) samples.
* sigma and tau are **indicative**: `sigma = |N|/A + sqrt(My^2+Mz^2)/W` and `tau = |T|/(2W_t) + sqrt(Vy^2+Vz^2)/A_shear`. No von Mises combination is formed, because the two peak at different points of the section.
* **No code check is applied.** API RP 2A-WSD is F5.
