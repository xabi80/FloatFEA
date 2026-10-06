# F4 step 1 — EK4 PRELIMINARY member-force preview

**ISSUE 3.** Supersedes issue 2, which superseded issue 1. Issue 1's `Vz` and `My`
were all wrong (R663, the equivalent load omitted from the end forces). Issue 2 fixed
that. **Issue 3 changes no number**: it separates the static-only, dynamic-only and
total columns that issue 2 reported combined, and adds EK1's `f` sensitivity. EO2's
replacement of the driver's hand-rolled Froude arithmetic with the DS2 converter is in
this issue, and the measurement below is what it did to the numbers.

**Did issue 2's dynamic columns change?** Measured, not assumed:

```
worst relative move, DYNAMIC-only envelope:  0.000e+00
  (no component moved)
worst relative move, TOTAL envelope:         0.000e+00
  (no component moved)
```

**They did not change, by any digit.** Every component of every member is
bit-identical to issue 2. That is the expected result and it is worth saying why it
is not a tautology: the two Froude conversions the driver *had* — time `λ^0.5` and
length `λ¹` — were numerically identical to the converter's, so removing them moves
nothing. The defect EO2 names was a conversion that was **missing**, not one that was
wrong, and that one was already repaired before issue 2 ran.

**PRELIMINARY (EK4). Nothing here is gated.** Step 2 has not run, so DQ4, DQ5 and
DQ8's tolerances are unmeasured. What this *is*: EK0(d)'s static case with its three
checks passing, plus EK0(e)'s dynamic case over DQ6's window with the
equal-and-opposite duality asserted against FloatSim's own Jacobian, combined as
EK0(f) requires. Numbers can move when step 2 measures a tolerance; the shape will not.

Full scale. `N`, `Vy`, `Vz` in N; `T`, `My`, `Mz` in N·m. **One element per member at
F3's mesh (EK1), so two stations per member** — every value is the worse station, as a
magnitude. `static` is EK0(d)'s case alone; `dyn` is the envelope of the dynamic case
alone over the six design waves and DQ6's window; `total` is EK0(f)'s combination,
enveloped the same way. **`total` is not `static + dyn`**: each is the worst over
stations and cases independently, and the dynamic extremum of a component need not
fall at the station or the instant where the sum is worst.

## `N` (N)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.2505e+07 | 1.2505e+07 | — |
| `platform:hub2_arm` | 0.0000e+00 | 3.8726e+05 | 3.8726e+05 | — |
| `platform:hub3_arm` | 0.0000e+00 | 1.1910e+07 | 1.1910e+07 | — |
| `platform:hub4_arm` | 0.0000e+00 | 3.8726e+05 | 3.8726e+05 | — |
| `hub1:buoy1_arm` | 0.0000e+00 | 5.0568e+06 | 5.0568e+06 | — |
| `hub1:buoy2_arm` | 0.0000e+00 | 2.9711e+06 | 2.9711e+06 | — |
| `hub1:buoy3_arm` | 0.0000e+00 | 2.9711e+06 | 2.9711e+06 | — |
| `hub2:buoy4_arm` | 0.0000e+00 | 5.6962e+06 | 5.6962e+06 | — |
| `hub2:buoy5_arm` | 0.0000e+00 | 2.7600e+06 | 2.7600e+06 | — |
| `hub2:buoy6_arm` | 0.0000e+00 | 2.8292e+06 | 2.8292e+06 | — |
| `hub3:buoy7_arm` | 0.0000e+00 | 5.8326e+06 | 5.8326e+06 | — |
| `hub3:buoy8_arm` | 0.0000e+00 | 3.0282e+06 | 3.0282e+06 | — |
| `hub3:buoy9_arm` | 0.0000e+00 | 3.0282e+06 | 3.0282e+06 | — |
| `hub4:buoy10_arm` | 0.0000e+00 | 5.6962e+06 | 5.6962e+06 | — |
| `hub4:buoy11_arm` | 0.0000e+00 | 2.8292e+06 | 2.8292e+06 | — |
| `hub4:buoy12_arm` | 0.0000e+00 | 2.7600e+06 | 2.7600e+06 | — |

## `Vy` (N)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.9021e-02 | 1.9021e-02 | — |
| `platform:hub2_arm` | 0.0000e+00 | 1.0004e+07 | 1.0004e+07 | — |
| `platform:hub3_arm` | 0.0000e+00 | 1.3798e-02 | 1.3798e-02 | — |
| `platform:hub4_arm` | 0.0000e+00 | 1.0004e+07 | 1.0004e+07 | — |
| `hub1:buoy1_arm` | 0.0000e+00 | 2.1738e-02 | 2.1738e-02 | — |
| `hub1:buoy2_arm` | 0.0000e+00 | 5.2944e+06 | 5.2944e+06 | — |
| `hub1:buoy3_arm` | 0.0000e+00 | 5.2944e+06 | 5.2944e+06 | — |
| `hub2:buoy4_arm` | 0.0000e+00 | 1.4060e+05 | 1.4060e+05 | — |
| `hub2:buoy5_arm` | 0.0000e+00 | 4.9555e+06 | 4.9555e+06 | — |
| `hub2:buoy6_arm` | 0.0000e+00 | 5.3215e+06 | 5.3215e+06 | — |
| `hub3:buoy7_arm` | 0.0000e+00 | 1.7876e-02 | 1.7876e-02 | — |
| `hub3:buoy8_arm` | 0.0000e+00 | 5.2509e+06 | 5.2509e+06 | — |
| `hub3:buoy9_arm` | 0.0000e+00 | 5.2509e+06 | 5.2509e+06 | — |
| `hub4:buoy10_arm` | 0.0000e+00 | 1.4060e+05 | 1.4060e+05 | — |
| `hub4:buoy11_arm` | 0.0000e+00 | 5.3215e+06 | 5.3215e+06 | — |
| `hub4:buoy12_arm` | 0.0000e+00 | 4.9555e+06 | 4.9555e+06 | — |

## `Vz` (N)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 3.0656e+06 | 6.7755e+05 | 3.4996e+06 | 0.221 |
| `platform:hub2_arm` | 3.0656e+06 | 7.6431e+05 | 3.8299e+06 | 0.249 |
| `platform:hub3_arm` | 3.0656e+06 | 7.7492e+05 | 3.8173e+06 | 0.253 |
| `platform:hub4_arm` | 3.0656e+06 | 7.6431e+05 | 3.8299e+06 | 0.249 |
| `hub1:buoy1_arm` | 5.9269e+06 | 3.6423e+05 | 6.1157e+06 | 0.061 |
| `hub1:buoy2_arm` | 5.9269e+06 | 3.5856e+05 | 6.1191e+06 | 0.060 |
| `hub1:buoy3_arm` | 5.9269e+06 | 3.5856e+05 | 6.1191e+06 | 0.060 |
| `hub2:buoy4_arm` | 5.9269e+06 | 4.5472e+05 | 6.2568e+06 | 0.077 |
| `hub2:buoy5_arm` | 5.9269e+06 | 4.3824e+05 | 6.2551e+06 | 0.074 |
| `hub2:buoy6_arm` | 5.9269e+06 | 4.3758e+05 | 6.2558e+06 | 0.074 |
| `hub3:buoy7_arm` | 5.9269e+06 | 5.2287e+05 | 6.4497e+06 | 0.088 |
| `hub3:buoy8_arm` | 5.9269e+06 | 5.3934e+05 | 6.4662e+06 | 0.091 |
| `hub3:buoy9_arm` | 5.9269e+06 | 5.3934e+05 | 6.4662e+06 | 0.091 |
| `hub4:buoy10_arm` | 5.9269e+06 | 4.5472e+05 | 6.2568e+06 | 0.077 |
| `hub4:buoy11_arm` | 5.9269e+06 | 4.3758e+05 | 6.2558e+06 | 0.074 |
| `hub4:buoy12_arm` | 5.9269e+06 | 4.3824e+05 | 6.2551e+06 | 0.074 |

## `T` (N·m)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 8.2718e-25 | 1.1854e-05 | 1.1854e-05 | 14330942105330972672.000 |
| `platform:hub2_arm` | 8.2718e-25 | 8.1377e+02 | 8.1377e+02 | 983788717484182785925054464.000 |
| `platform:hub3_arm` | 6.8905e-10 | 1.1854e-05 | 1.1853e-05 | 17203.659 |
| `platform:hub4_arm` | 1.0340e-24 | 8.1377e+02 | 8.1377e+02 | 787030973990048470979837952.000 |
| `hub1:buoy1_arm` | 0.0000e+00 | 1.1869e-04 | 1.1869e-04 | — |
| `hub1:buoy2_arm` | 9.7511e-09 | 1.9984e+03 | 1.9984e+03 | 204943004016.980 |
| `hub1:buoy3_arm` | 9.9588e-09 | 1.9984e+03 | 1.9984e+03 | 200669706444.389 |
| `hub2:buoy4_arm` | 0.0000e+00 | 2.5145e+02 | 2.5145e+02 | — |
| `hub2:buoy5_arm` | 5.0197e-09 | 1.7072e+03 | 1.7072e+03 | 340097864383.570 |
| `hub2:buoy6_arm` | 2.9580e-08 | 1.5720e+03 | 1.5720e+03 | 53145554169.518 |
| `hub3:buoy7_arm` | 0.0000e+00 | 1.1351e-04 | 1.1351e-04 | — |
| `hub3:buoy8_arm` | 6.1345e-09 | 2.3941e+03 | 2.3941e+03 | 390266772410.166 |
| `hub3:buoy9_arm` | 2.4514e-08 | 2.3941e+03 | 2.3941e+03 | 97660425141.924 |
| `hub4:buoy10_arm` | 0.0000e+00 | 2.5145e+02 | 2.5145e+02 | — |
| `hub4:buoy11_arm` | 1.6642e-09 | 1.5720e+03 | 1.5720e+03 | 944636771851.844 |
| `hub4:buoy12_arm` | 1.1502e-08 | 1.7072e+03 | 1.7072e+03 | 148426671020.059 |

## `My` (N·m)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 1.1496e+08 | 3.3315e+07 | 1.3660e+08 | 0.290 |
| `platform:hub2_arm` | 1.1496e+08 | 3.7646e+07 | 1.5261e+08 | 0.327 |
| `platform:hub3_arm` | 1.1496e+08 | 3.8295e+07 | 1.5044e+08 | 0.333 |
| `platform:hub4_arm` | 1.1496e+08 | 3.7646e+07 | 1.5261e+08 | 0.327 |
| `hub1:buoy1_arm` | 1.1752e+08 | 6.8627e+06 | 1.2151e+08 | 0.058 |
| `hub1:buoy2_arm` | 1.1752e+08 | 6.7874e+06 | 1.2157e+08 | 0.058 |
| `hub1:buoy3_arm` | 1.1752e+08 | 6.7874e+06 | 1.2157e+08 | 0.058 |
| `hub2:buoy4_arm` | 1.1752e+08 | 9.3503e+06 | 1.2528e+08 | 0.080 |
| `hub2:buoy5_arm` | 1.1752e+08 | 9.1354e+06 | 1.2526e+08 | 0.078 |
| `hub2:buoy6_arm` | 1.1752e+08 | 9.1280e+06 | 1.2527e+08 | 0.078 |
| `hub3:buoy7_arm` | 1.1752e+08 | 1.1421e+07 | 1.2894e+08 | 0.097 |
| `hub3:buoy8_arm` | 1.1752e+08 | 1.1627e+07 | 1.2914e+08 | 0.099 |
| `hub3:buoy9_arm` | 1.1752e+08 | 1.1627e+07 | 1.2914e+08 | 0.099 |
| `hub4:buoy10_arm` | 1.1752e+08 | 9.3503e+06 | 1.2528e+08 | 0.080 |
| `hub4:buoy11_arm` | 1.1752e+08 | 9.1280e+06 | 1.2527e+08 | 0.078 |
| `hub4:buoy12_arm` | 1.1752e+08 | 9.1354e+06 | 1.2526e+08 | 0.078 |

## `Mz` (N·m)

| member | static | dyn | total | dyn/static |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.3625e+00 | 1.3625e+00 | — |
| `platform:hub2_arm` | 0.0000e+00 | 4.9033e+08 | 4.9033e+08 | — |
| `platform:hub3_arm` | 0.0000e+00 | 7.3506e-01 | 7.3506e-01 | — |
| `platform:hub4_arm` | 0.0000e+00 | 4.9033e+08 | 4.9033e+08 | — |
| `hub1:buoy1_arm` | 0.0000e+00 | 8.0385e-01 | 8.0385e-01 | — |
| `hub1:buoy2_arm` | 0.0000e+00 | 1.3176e+08 | 1.3176e+08 | — |
| `hub1:buoy3_arm` | 0.0000e+00 | 1.3176e+08 | 1.3176e+08 | — |
| `hub2:buoy4_arm` | 0.0000e+00 | 3.6064e+06 | 3.6064e+06 | — |
| `hub2:buoy5_arm` | 0.0000e+00 | 1.2265e+08 | 1.2265e+08 | — |
| `hub2:buoy6_arm` | 0.0000e+00 | 1.3181e+08 | 1.3181e+08 | — |
| `hub3:buoy7_arm` | 0.0000e+00 | 6.4939e-01 | 6.4939e-01 | — |
| `hub3:buoy8_arm` | 0.0000e+00 | 1.2976e+08 | 1.2976e+08 | — |
| `hub3:buoy9_arm` | 0.0000e+00 | 1.2976e+08 | 1.2976e+08 | — |
| `hub4:buoy10_arm` | 0.0000e+00 | 3.6064e+06 | 3.6064e+06 | — |
| `hub4:buoy11_arm` | 0.0000e+00 | 1.3181e+08 | 1.3181e+08 | — |
| `hub4:buoy12_arm` | 0.0000e+00 | 1.2265e+08 | 1.2265e+08 | — |

## EK1's `f` sensitivity — static case at `f` = 0.25, 0.50, 0.75

`f` is DY0's mass fraction: the share of a body's deck mass carried by its members,
the remainder lumped at the remainder node on a rigid link. It is a **modelling
choice**, which is why EK1 asks what the member forces do when it moves.

The shipped build takes the first admissible rung of `MASS_FRACTION_LADDER =
(0.5, 0.4, 0.3, 0.2, 0.1, 0.0)` and reaches `f = 0.50` on every body. **Neither 0.25
nor 0.75 is on that ladder, and 0.75 is above its first rung**, so both are reached
through a new optional `build_superstructure(mass_fraction=...)`, which bypasses the
ladder, does not consult `admissible()`, and reports a finding on every body saying
so. Whether `f = 0.75` is admissible is therefore a question and not an assumption:

```
f0.25  platform  admissible=True  rho_eq=   1191.0  m_member=3.1250e+05  m_remainder=9.3750e+05  min eig(J_r)=2.9500e+09
f0.25  hub1      admissible=True  rho_eq=   3811.2  m_member=3.7500e+05  m_remainder=1.1250e+06  min eig(J_r)=1.1681e+08
f0.25  hub2      admissible=True  rho_eq=   3811.2  m_member=3.7500e+05  m_remainder=1.1250e+06  min eig(J_r)=1.1681e+08
f0.25  hub3      admissible=True  rho_eq=   3811.2  m_member=3.7500e+05  m_remainder=1.1250e+06  min eig(J_r)=1.1681e+08
f0.25  hub4      admissible=True  rho_eq=   3811.2  m_member=3.7500e+05  m_remainder=1.1250e+06  min eig(J_r)=1.1681e+08
f0.50  platform  admissible=True  rho_eq=   2382.0  m_member=6.2500e+05  m_remainder=6.2500e+05  min eig(J_r)=2.7305e+09
f0.50  hub1      admissible=True  rho_eq=   7622.4  m_member=7.5000e+05  m_remainder=7.5000e+05  min eig(J_r)=7.7364e+07
f0.50  hub2      admissible=True  rho_eq=   7622.4  m_member=7.5000e+05  m_remainder=7.5000e+05  min eig(J_r)=7.7364e+07
f0.50  hub3      admissible=True  rho_eq=   7622.4  m_member=7.5000e+05  m_remainder=7.5000e+05  min eig(J_r)=7.7364e+07
f0.50  hub4      admissible=True  rho_eq=   7622.4  m_member=7.5000e+05  m_remainder=7.5000e+05  min eig(J_r)=7.7364e+07
f0.75  platform  admissible=True  rho_eq=   3573.0  m_member=9.3750e+05  m_remainder=3.1250e+05  min eig(J_r)=2.3331e+09
f0.75  hub1      admissible=True  rho_eq=  11433.5  m_member=1.1250e+06  m_remainder=3.7500e+05  min eig(J_r)=3.7920e+07
f0.75  hub2      admissible=True  rho_eq=  11433.5  m_member=1.1250e+06  m_remainder=3.7500e+05  min eig(J_r)=3.7920e+07
f0.75  hub3      admissible=True  rho_eq=  11433.5  m_member=1.1250e+06  m_remainder=3.7500e+05  min eig(J_r)=3.7920e+07
f0.75  hub4      admissible=True  rho_eq=  11433.5  m_member=1.1250e+06  m_remainder=3.7500e+05  min eig(J_r)=3.7920e+07
```

**Every body is admissible at all three fractions** — `m_r >= 0` and `J_r` PSD
throughout. At `f = 0.75` the four hubs carry a second finding: the equivalent density
reaches 11433.5 kg/m³, above steel at 7850, which is the sizing statement that a hub's
mass does not fit inside F1's section once three quarters of it is on the members. The
platform stays below steel at every fraction.

| member | Vz @ 0.25 | Vz @ 0.50 | Vz @ 0.75 | My @ 0.25 | My @ 0.50 | My @ 0.75 | My .25/.50 | My .75/.50 |
|---|---|---|---|---|---|---|---|---|
| `platform:hub1_arm` | 3.0656e+06 | 3.0656e+06 | 3.0656e+06 | 1.3412e+08 | 1.1496e+08 | 9.5801e+07 | 1.1667 | 0.8333 |
| `platform:hub2_arm` | 3.0656e+06 | 3.0656e+06 | 3.0656e+06 | 1.3412e+08 | 1.1496e+08 | 9.5801e+07 | 1.1667 | 0.8333 |
| `platform:hub3_arm` | 3.0656e+06 | 3.0656e+06 | 3.0656e+06 | 1.3412e+08 | 1.1496e+08 | 9.5801e+07 | 1.1667 | 0.8333 |
| `platform:hub4_arm` | 3.0656e+06 | 3.0656e+06 | 3.0656e+06 | 1.3412e+08 | 1.1496e+08 | 9.5801e+07 | 1.1667 | 0.8333 |
| `hub1:buoy1_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub1:buoy2_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub1:buoy3_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub2:buoy4_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub2:buoy5_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub2:buoy6_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub3:buoy7_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub3:buoy8_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub3:buoy9_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub4:buoy10_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub4:buoy11_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |
| `hub4:buoy12_arm` | 5.9269e+06 | 5.9269e+06 | 5.9269e+06 | 1.3284e+08 | 1.1752e+08 | 1.0219e+08 | 1.1304 | 0.8696 |

**`Vz` does not move at all; only `My` does.** The worst relative move of any `Vz` in
the table is `8.882e-16`, which is round-off. `My` rises by at most
`1.1667x` at `f = 0.25` and falls to `0.8333x` at `f = 0.75`.

That asymmetry is the shape of the split, not an accident. `f` moves mass between two
places that both lie inside the member's span, so the **total** carried weight is
conserved exactly — which fixes the root shear, the quantity `Vz` reports at its worst
station, independently of `f`. What `f` changes is where that weight acts: a uniform
line load has its resultant at mid-span, the lumped remainder hangs at the remainder
node, and the root moment is the weighted lever of the two. Moving mass outboard raises
`My`, inboard lowers it, and the shear never notices.

The practical reading: **the static root moment carries a modelling band of about
±17% from `f` alone**, while the shear carries none. Any
utilisation driven by `My` inherits that band, and it is a band on a choice rather than
an uncertainty in a measurement — F5's section checks should be read against it.

