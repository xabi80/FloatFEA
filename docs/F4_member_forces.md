# F4 step 3 — member forces, PRELIMINARY

**Every line below is preliminary until F4 closes.** The labels are the deliverable as much as the numbers are.

* PRELIMINARY until F4 closes.
* Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms (Xabier, 6 Oct); platform inertia scaled with mass (assumed). ER0.
* DZ5 / ER1(e): the four hub arms carry an equivalent density above steel (11433.5 kg/m^3 against 7850), which is a reported sizing finding -- the members are stiffness equivalents, so the hub's mass does not fit inside F1's section at f = 0.75.
* Hub line mass 15 t/m, against the platform arms' 10.3 t/m.
* Stand-in tube: the stiffness equivalent of a TRIANGULATED TRUSS of undecided depth (F1.md:390). Stresses are INDICATIVE, not a check on a real section.
* EX3 / R724: all six cases are heading 0 degrees. The heading dependence is UNTESTED.
* Stations: ROOT = the inboard end at the body's centre node, TIP = the far end. MID is closed-form for a uniform net body force (one element per member at F3's mesh).
* R730: all three stations are INTERNAL ACTIONS in one convention (as seen from the A end), so TIP is `-end_b` and not the raw element end force. An earlier version averaged the two raw ends for MID, which computes a LOAD -- exactly half the member's weight on Vz -- and understated the midspan stress by 46%.
* 'dynamic' is the DYNAMIC INCREMENT about static equilibrium, solved from FloatSim's multipliers with NO gravity -- FloatSim is linearised about equilibrium, so the static weight/buoyancy balance is already in the formulation. 'total' = static + dynamic.
* The load path is validated against FloatSim's own per-body accelerations: 1.55% on all five bodies, 2.78% worst over eighteen samples.
* No code check is applied. API RP 2A-WSD checks are F5 (EY4).
* SCALE: the npz holds FloatSim's MODEL-scale output; the FE model is FULL scale. The multipliers are converted through `floatfea.io.froude`'s declared `joint_multiplier_yaw_locked` composite (force x 125000, locked moment x 6250000).

## The ten most loaded member-stations, by indicative sigma

| # | body | member | station | governing case | sigma at the instant (MPa) | envelope upper bound (MPa) |
|---|---|---|---|---|---|---|
| 1 | platform | `platform:hub2_arm` | ROOT | T = 10 s | 742.6 | 762.2 |
| 2 | platform | `platform:hub4_arm` | ROOT | T = 10 s | 742.6 | 761.5 |
| 3 | platform | `platform:hub2_arm` | MID | T = 10 s | 384.6 | 396.7 |
| 4 | platform | `platform:hub4_arm` | MID | T = 10 s | 384.6 | 396.1 |
| 5 | platform | `platform:hub3_arm` | ROOT | T = 20 s | 337.3 | 338.2 |
| 6 | platform | `platform:hub1_arm` | ROOT | T = 12.5 s | 312.2 | 314.5 |
| 7 | hub1 | `hub1:buoy3_arm` | ROOT | T = 10 s | 262.5 | 263.0 |
| 8 | hub1 | `hub1:buoy2_arm` | ROOT | T = 10 s | 262.5 | 263.2 |
| 9 | hub4 | `hub4:buoy11_arm` | ROOT | T = 10 s | 261.7 | 265.2 |
| 10 | hub2 | `hub2:buoy6_arm` | ROOT | T = 10 s | 261.7 | 265.4 |

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
