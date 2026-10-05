# F4 step 1 — EK4 PRELIMINARY member-force preview

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
| `platform:hub1_arm` | 1.2471e+07 | 1.8836e-02 | 2.7319e+06 | 5.9272e-06 | 1.4299e+08 | 1.3651e+00 |
| `platform:hub2_arm` | 3.8726e+05 | 9.9594e+06 | 3.0521e+06 | 4.0689e+02 | 1.5909e+08 | 4.9070e+08 |
| `platform:hub3_arm` | 1.1873e+07 | 1.3607e-02 | 3.0082e+06 | 5.9264e-06 | 1.5714e+08 | 7.4101e-01 |
| `platform:hub4_arm` | 3.8726e+05 | 9.9594e+06 | 3.0521e+06 | 4.0689e+02 | 1.5909e+08 | 4.9070e+08 |
| `hub1:buoy1_arm` | 5.0005e+06 | 2.1684e-02 | 4.8606e+06 | 5.9347e-05 | 1.2674e+08 | 8.0439e-01 |
| `hub1:buoy2_arm` | 2.9590e+06 | 5.2677e+06 | 4.8626e+06 | 9.9921e+02 | 1.2680e+08 | 1.3166e+08 |
| `hub1:buoy3_arm` | 2.9590e+06 | 5.2677e+06 | 4.8626e+06 | 9.9921e+02 | 1.2680e+08 | 1.3166e+08 |
| `hub2:buoy4_arm` | 5.6862e+06 | 1.4060e+05 | 5.0113e+06 | 1.2573e+02 | 1.3047e+08 | 3.6064e+06 |
| `hub2:buoy5_arm` | 2.7304e+06 | 4.9026e+06 | 5.0105e+06 | 8.5359e+02 | 1.3045e+08 | 1.2287e+08 |
| `hub2:buoy6_arm` | 2.8003e+06 | 5.2672e+06 | 5.0108e+06 | 7.8602e+02 | 1.3046e+08 | 1.3204e+08 |
| `hub3:buoy7_arm` | 5.7977e+06 | 1.7336e-02 | 5.1577e+06 | 5.6754e-05 | 1.3433e+08 | 6.4487e-01 |
| `hub3:buoy8_arm` | 2.9923e+06 | 5.1893e+06 | 5.1656e+06 | 1.1970e+03 | 1.3456e+08 | 1.2950e+08 |
| `hub3:buoy9_arm` | 2.9923e+06 | 5.1893e+06 | 5.1656e+06 | 1.1970e+03 | 1.3456e+08 | 1.2950e+08 |
| `hub4:buoy10_arm` | 5.6862e+06 | 1.4060e+05 | 5.0113e+06 | 1.2573e+02 | 1.3047e+08 | 3.6064e+06 |
| `hub4:buoy11_arm` | 2.8003e+06 | 5.2672e+06 | 5.0108e+06 | 7.8602e+02 | 1.3046e+08 | 1.3204e+08 |
| `hub4:buoy12_arm` | 2.7304e+06 | 4.9026e+06 | 5.0105e+06 | 8.5359e+02 | 1.3045e+08 | 1.2287e+08 |

## The static case alone, for comparison

| member | N | Vy | Vz | T | My | Mz |
|---|---|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 0.0000e+00 | 2.2992e+06 | 8.2718e-25 | 1.2135e+08 | 0.0000e+00 |
| `platform:hub2_arm` | 0.0000e+00 | 0.0000e+00 | 2.2992e+06 | 8.2718e-25 | 1.2135e+08 | 0.0000e+00 |
| `platform:hub3_arm` | 0.0000e+00 | 0.0000e+00 | 2.2992e+06 | 6.8905e-10 | 1.2135e+08 | 0.0000e+00 |
| `platform:hub4_arm` | 0.0000e+00 | 0.0000e+00 | 2.2992e+06 | 8.2718e-25 | 1.2135e+08 | 0.0000e+00 |
| `hub1:buoy1_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 0.0000e+00 | 1.2263e+08 | 0.0000e+00 |
| `hub1:buoy2_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 9.7511e-09 | 1.2263e+08 | 0.0000e+00 |
| `hub1:buoy3_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 9.4931e-09 | 1.2263e+08 | 0.0000e+00 |
| `hub2:buoy4_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 0.0000e+00 | 1.2263e+08 | 0.0000e+00 |
| `hub2:buoy5_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 5.0197e-09 | 1.2263e+08 | 0.0000e+00 |
| `hub2:buoy6_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 2.9580e-08 | 1.2263e+08 | 0.0000e+00 |
| `hub3:buoy7_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 0.0000e+00 | 1.2262e+08 | 0.0000e+00 |
| `hub3:buoy8_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 6.1345e-09 | 1.2262e+08 | 0.0000e+00 |
| `hub3:buoy9_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 2.4049e-08 | 1.2262e+08 | 0.0000e+00 |
| `hub4:buoy10_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 0.0000e+00 | 1.2262e+08 | 0.0000e+00 |
| `hub4:buoy11_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 1.6642e-09 | 1.2262e+08 | 0.0000e+00 |
| `hub4:buoy12_arm` | 0.0000e+00 | 0.0000e+00 | 4.7006e+06 | 1.1036e-08 | 1.2263e+08 | 0.0000e+00 |

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
