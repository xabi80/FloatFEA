# F4 step 1 — EK4 PRELIMINARY member-force preview

**ISSUE 2. THIS SUPERSEDES THE FIRST ISSUE, WHOSE `Vz` AND `My` WERE ALL WRONG.**
The ninety-third verdict found R663: `member_forces` returned `k u` with the
element's equivalent load omitted, so every shear was 25.0000% low on the platform
arms and 20.69% on the hub arms, every root moment 5.56% / 4.35% high, and the tip
moment sat at exactly `-mu L^2 / 12` where a roller support carries none. The
decisive symptom: `Vz_A + Vz_B` was identically zero, so each member's own weight
appeared nowhere in its end forces.

Fixed, and now gated by CONSERVATION rather than by a hand-computed end value —
because the check I had written, `reaction - weight/2`, was the defective formula's
own identity: it agreed with the bug and would have reddened on the fix. After the
fix `Vz_A + Vz_B` equals each member's weight to `5.7e-16` and every tip shear
equals its support reaction to every digit.

**PRELIMINARY (EK4). Nothing here is gated.** Step 2 has not run, so DQ4, DQ5 and
DQ8's tolerances are unmeasured. What this *is*: EK0(d)'s static case with its three
checks passing, plus EK0(e)'s dynamic case over DQ6's window with the
equal-and-opposite duality asserted against FloatSim's own Jacobian, combined as
EK0(f) requires. Numbers can move when step 2 measures a tolerance; the shape will not.

Full scale. `N`, `Vy`, `Vz` in N; `T`, `My`, `Mz` in N·m. **One element per member at
F3's mesh (EK1), so two stations per member** — the value shown is the worse station.

## Envelope over the six design-wave cases

| member | N | Vy | Vz | T | My | Mz |
|---|---|---|---|---|---|---|
| `platform:hub1_arm` | 1.2505e+07 | 1.9021e-02 | 3.4996e+06 | 1.1854e-05 | 1.3660e+08 | 1.3625e+00 |
| `platform:hub2_arm` | 3.8726e+05 | 1.0004e+07 | 3.8299e+06 | 8.1377e+02 | 1.5261e+08 | 4.9033e+08 |
| `platform:hub3_arm` | 1.1910e+07 | 1.3798e-02 | 3.8173e+06 | 1.1853e-05 | 1.5044e+08 | 7.3506e-01 |
| `platform:hub4_arm` | 3.8726e+05 | 1.0004e+07 | 3.8299e+06 | 8.1377e+02 | 1.5261e+08 | 4.9033e+08 |
| `hub1:buoy1_arm` | 5.0568e+06 | 2.1738e-02 | 6.1157e+06 | 1.1869e-04 | 1.2151e+08 | 8.0385e-01 |
| `hub1:buoy2_arm` | 2.9711e+06 | 5.2944e+06 | 6.1191e+06 | 1.9984e+03 | 1.2157e+08 | 1.3176e+08 |
| `hub1:buoy3_arm` | 2.9711e+06 | 5.2944e+06 | 6.1191e+06 | 1.9984e+03 | 1.2157e+08 | 1.3176e+08 |
| `hub2:buoy4_arm` | 5.6962e+06 | 1.4060e+05 | 6.2568e+06 | 2.5145e+02 | 1.2528e+08 | 3.6064e+06 |
| `hub2:buoy5_arm` | 2.7600e+06 | 4.9555e+06 | 6.2551e+06 | 1.7072e+03 | 1.2526e+08 | 1.2265e+08 |
| `hub2:buoy6_arm` | 2.8292e+06 | 5.3215e+06 | 6.2558e+06 | 1.5720e+03 | 1.2527e+08 | 1.3181e+08 |
| `hub3:buoy7_arm` | 5.8326e+06 | 1.7876e-02 | 6.4497e+06 | 1.1351e-04 | 1.2894e+08 | 6.4939e-01 |
| `hub3:buoy8_arm` | 3.0282e+06 | 5.2509e+06 | 6.4662e+06 | 2.3941e+03 | 1.2914e+08 | 1.2976e+08 |
| `hub3:buoy9_arm` | 3.0282e+06 | 5.2509e+06 | 6.4662e+06 | 2.3941e+03 | 1.2914e+08 | 1.2976e+08 |
| `hub4:buoy10_arm` | 5.6962e+06 | 1.4060e+05 | 6.2568e+06 | 2.5145e+02 | 1.2528e+08 | 3.6064e+06 |
| `hub4:buoy11_arm` | 2.8292e+06 | 5.3215e+06 | 6.2558e+06 | 1.5720e+03 | 1.2527e+08 | 1.3181e+08 |
| `hub4:buoy12_arm` | 2.7600e+06 | 4.9555e+06 | 6.2551e+06 | 1.7072e+03 | 1.2526e+08 | 1.2265e+08 |

## The static case alone, for comparison

| member | N | Vy | Vz | T | My | Mz |
|---|---|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 0.0000e+00 | 3.0656e+06 | 8.2718e-25 | 1.1496e+08 | 0.0000e+00 |
| `platform:hub2_arm` | 0.0000e+00 | 0.0000e+00 | 3.0656e+06 | 8.2718e-25 | 1.1496e+08 | 0.0000e+00 |
| `platform:hub3_arm` | 0.0000e+00 | 0.0000e+00 | 3.0656e+06 | 6.8905e-10 | 1.1496e+08 | 0.0000e+00 |
| `platform:hub4_arm` | 0.0000e+00 | 0.0000e+00 | 3.0656e+06 | 1.0340e-24 | 1.1496e+08 | 0.0000e+00 |
| `hub1:buoy1_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 0.0000e+00 | 1.1752e+08 | 0.0000e+00 |
| `hub1:buoy2_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 9.7511e-09 | 1.1752e+08 | 0.0000e+00 |
| `hub1:buoy3_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 9.9588e-09 | 1.1752e+08 | 0.0000e+00 |
| `hub2:buoy4_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 0.0000e+00 | 1.1752e+08 | 0.0000e+00 |
| `hub2:buoy5_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 5.0197e-09 | 1.1752e+08 | 0.0000e+00 |
| `hub2:buoy6_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 2.9580e-08 | 1.1752e+08 | 0.0000e+00 |
| `hub3:buoy7_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 0.0000e+00 | 1.1752e+08 | 0.0000e+00 |
| `hub3:buoy8_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 6.1345e-09 | 1.1752e+08 | 0.0000e+00 |
| `hub3:buoy9_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 2.4514e-08 | 1.1752e+08 | 0.0000e+00 |
| `hub4:buoy10_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 0.0000e+00 | 1.1752e+08 | 0.0000e+00 |
| `hub4:buoy11_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 1.6642e-09 | 1.1752e+08 | 0.0000e+00 |
| `hub4:buoy12_arm` | 0.0000e+00 | 0.0000e+00 | 5.9269e+06 | 1.1502e-08 | 1.1752e+08 | 0.0000e+00 |

## Per-case checks (EN2's STOP conditions, none tripped)

| T full | duration | window | steps | duality | relief residual / scale |
|---|---|---|---|---|---|
| 10.0 s | 31.21 s | from 24.15 s | 707 | 0.000e+00 | 4.371e-13 |
| 12.5 s | 36.52 s | from 27.68 s | 885 | 0.000e+00 | 3.539e-13 |
| 14.0 s | 39.70 s | from 29.80 s | 991 | 0.000e+00 | 1.772e-13 |
| 15.0 s | 41.82 s | from 31.22 s | 1061 | 0.000e+00 | 3.311e-13 |
| 16.2 s | 44.37 s | from 32.92 s | 1146 | 0.000e+00 | 2.699e-13 |
| 20.0 s | 52.43 s | from 38.29 s | 1415 | 0.000e+00 | 1.203e-13 |

## What is worth reading in it

**The heading shows up in the load path, and nothing arranged that.** The waves run
along `x` at heading 0. The two arms lying along `x` — `hub1` at `+x`, `hub3` at `-x` —
carry the load as AXIAL (`N` ≈ `1.2e7`) with essentially no transverse shear. The two
along `y` carry it as transverse shear (`Vy` ≈ `1.0e7`) with an order less axial. A
mapping that had lost the force direction could not produce that split.

**`Mz` on the `y` arms reconciles by hand:** `9.9594e6 N` × the `50 m` arm = `4.98e8`,
against a computed `4.9070e8`.

**The mirror pairs agree to every digit shown.** `hub1:buoy2_arm` and `hub1:buoy3_arm`
are identical; so are `hub2:buoy5` and `hub4:buoy12`, and `hub2:buoy6` and
`hub4:buoy11`. That is the `y → -y` symmetry — the one global isometry this geometry
admits, which R650 identified while settling DQ9's second side.

**The joint reactions fall with period**, `|F|max` from `1.2437e7 N` at `T = 10 s` to
`3.3105e6 N` at `T = 20 s`: longer waves, less relative motion between buoy and hub.

## One defect this table had in its first run

The first run made the dynamic contribution ~`1e-5` of the static, which is not
possible for a design wave, and that is how it announced itself.
`build_superstructure` converts the deck by `lambda`, so the static case is FULL scale
while `res.lam` comes out of a MODEL-scale run, and I was adding the two.

`floatfea/io/froude.py` had already anticipated it:
`COMPOSITE_BLOCKS["joint_multiplier_yaw_locked"] = ((0,3,"force"), (3,4,"moment"))`,
with R579's note that scaling the block as pure force *leaves the moment columns short
by exactly lambda* and as pure moment *leaves the force columns long by the same
factor* — *"Neither raised. Both results look like numbers."* Force scales `x125000`,
moment `x6250000`.

**The conversion sits in the driver, not in `floatfea/`,** which is correct —
`docs/conventions.md` puts unit conversion at the I/O boundary and the library modules
rightly take whatever load vector they are handed. The consequence for the reviewer:
the guard against a repeat has to be a test on the driver, and there is none yet.
