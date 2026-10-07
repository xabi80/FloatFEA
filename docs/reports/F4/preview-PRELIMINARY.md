# F4 step 2 — ER3 PRELIMINARY member-force preview

**ISSUE 4, ON A NEW MASS BASIS. Every number in issues 1–3 is superseded.**

## The label this basis carries (ER1(e))

> **platform 20 kg / hub 12 kg model scale; 75% of body mass on arms (Xabier, 6 Oct);
> platform inertia scaled with mass (assumed).**
>
> **The four hub arms carry an equivalent density above steel** — `11433.5 kg/m³`
> against `7850` — which is a reported sizing finding and **not** a refusal: the
> members are stiffness equivalents, so a density above steel means the hub's mass does
> not fit inside F1's section at `f = 0.75`, and the section or the fraction is the
> thing to look at. The platform is `7146.0 kg/m³`, below steel.
>
> **The hub reactions rise although the hub mass does not**, because the platform share
> handed down rises: `5.926875e+06 N` to `6.948750e+06 N` per hub support. Isolated
> (BG0), the mass alone accounts for all of it and `f` for none.

**PRELIMINARY (ER3). Nothing here is gated.** EQ3's work — G4.1 per body and per case,
DQ4's `M·a` vector test, DQ5's free fall, G4.5 — has not run. What this *is*: EK0(d)'s
static case on the new basis, plus the dynamic case over DQ6's window from six fresh
FloatSim runs with ER0's override applied in memory, combined as EK0(f) requires.

## What was measured on the new runs, and none of it stopped the work

```
EK0(a)  the per-body external hydrodynamic force on the five FE bodies,
        over EVERY step of all six cases -- 24611 steps
          0.000000e+00 N on every case and every body
EK0(e)  the equal-and-opposite duality, from FloatSim's OWN Jacobian
          0.000000e+00 on every case
EJ4     the per-body relief residual against the reaction scale, per case
          T_full  10.0    707 steps  7.850279e-13
          T_full  12.5    885 steps  4.042139e-13
          T_full  14.0    991 steps  2.271498e-13
          T_full  15.0   1061 steps  2.582255e-13
          T_full  16.2   1146 steps  1.075836e-13
          T_full  20.0   1415 steps  3.541988e-14
          worst over all six: 7.850279e-13
```

Full scale. `N`, `Vy`, `Vz` in N; `T`, `My`, `Mz` in N·m. One element per member, so
two stations — every value is the worse station, as a magnitude. **`total` is not
`static + dyn`**: each is the worst over stations and cases independently.

## `N` (N)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.2510e+07 | 1.2510e+07 | 1.000× |
| `platform:hub2_arm` | 0.0000e+00 | 3.8648e+05 | 3.8648e+05 | 0.998× |
| `platform:hub3_arm` | 0.0000e+00 | 1.1915e+07 | 1.1915e+07 | 1.000× |
| `platform:hub4_arm` | 0.0000e+00 | 3.8648e+05 | 3.8648e+05 | 0.998× |
| `hub1:buoy1_arm` | 0.0000e+00 | 5.0738e+06 | 5.0738e+06 | 1.003× |
| `hub1:buoy2_arm` | 0.0000e+00 | 2.9750e+06 | 2.9750e+06 | 1.001× |
| `hub1:buoy3_arm` | 0.0000e+00 | 2.9750e+06 | 2.9750e+06 | 1.001× |
| `hub2:buoy4_arm` | 0.0000e+00 | 5.7033e+06 | 5.7033e+06 | 1.001× |
| `hub2:buoy5_arm` | 0.0000e+00 | 2.7762e+06 | 2.7762e+06 | 1.006× |
| `hub2:buoy6_arm` | 0.0000e+00 | 2.8440e+06 | 2.8440e+06 | 1.005× |
| `hub3:buoy7_arm` | 0.0000e+00 | 5.8521e+06 | 5.8521e+06 | 1.003× |
| `hub3:buoy8_arm` | 0.0000e+00 | 3.0379e+06 | 3.0379e+06 | 1.003× |
| `hub3:buoy9_arm` | 0.0000e+00 | 3.0379e+06 | 3.0379e+06 | 1.003× |
| `hub4:buoy10_arm` | 0.0000e+00 | 5.7033e+06 | 5.7033e+06 | 1.001× |
| `hub4:buoy11_arm` | 0.0000e+00 | 2.8440e+06 | 2.8440e+06 | 1.005× |
| `hub4:buoy12_arm` | 0.0000e+00 | 2.7762e+06 | 2.7762e+06 | 1.006× |

## `Vy` (N)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.6921e-02 | 1.6921e-02 | 0.890× |
| `platform:hub2_arm` | 0.0000e+00 | 1.0164e+07 | 1.0164e+07 | 1.016× |
| `platform:hub3_arm` | 0.0000e+00 | 1.3083e-02 | 1.3083e-02 | 0.948× |
| `platform:hub4_arm` | 0.0000e+00 | 1.0164e+07 | 1.0164e+07 | 1.016× |
| `hub1:buoy1_arm` | 0.0000e+00 | 1.9831e-02 | 1.9831e-02 | 0.912× |
| `hub1:buoy2_arm` | 0.0000e+00 | 5.3030e+06 | 5.3030e+06 | 1.002× |
| `hub1:buoy3_arm` | 0.0000e+00 | 5.3030e+06 | 5.3030e+06 | 1.002× |
| `hub2:buoy4_arm` | 0.0000e+00 | 1.3961e+05 | 1.3961e+05 | 0.993× |
| `hub2:buoy5_arm` | 0.0000e+00 | 4.9843e+06 | 4.9843e+06 | 1.006× |
| `hub2:buoy6_arm` | 0.0000e+00 | 5.3494e+06 | 5.3494e+06 | 1.005× |
| `hub3:buoy7_arm` | 0.0000e+00 | 1.7155e-02 | 1.7155e-02 | 0.960× |
| `hub3:buoy8_arm` | 0.0000e+00 | 5.2704e+06 | 5.2704e+06 | 1.004× |
| `hub3:buoy9_arm` | 0.0000e+00 | 5.2704e+06 | 5.2704e+06 | 1.004× |
| `hub4:buoy10_arm` | 0.0000e+00 | 1.3961e+05 | 1.3961e+05 | 0.993× |
| `hub4:buoy11_arm` | 0.0000e+00 | 5.3494e+06 | 5.3494e+06 | 1.005× |
| `hub4:buoy12_arm` | 0.0000e+00 | 4.9843e+06 | 4.9843e+06 | 1.006× |

## `Vz` (N)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 6.1313e+06 | 6.5207e+05 | 6.6832e+06 | 1.910× |
| `platform:hub2_arm` | 6.1312e+06 | 7.7469e+05 | 6.9059e+06 | 1.803× |
| `platform:hub3_arm` | 6.1312e+06 | 1.0615e+06 | 7.1927e+06 | 1.884× |
| `platform:hub4_arm` | 6.1312e+06 | 7.7469e+05 | 6.9059e+06 | 1.803× |
| `hub1:buoy1_arm` | 6.9488e+06 | 3.4511e+05 | 7.1936e+06 | 1.176× |
| `hub1:buoy2_arm` | 6.9488e+06 | 3.4241e+05 | 7.1965e+06 | 1.176× |
| `hub1:buoy3_arm` | 6.9488e+06 | 3.4241e+05 | 7.1965e+06 | 1.176× |
| `hub2:buoy4_arm` | 6.9488e+06 | 4.8820e+05 | 7.3075e+06 | 1.168× |
| `hub2:buoy5_arm` | 6.9487e+06 | 4.6843e+05 | 7.3098e+06 | 1.169× |
| `hub2:buoy6_arm` | 6.9488e+06 | 4.6837e+05 | 7.3099e+06 | 1.169× |
| `hub3:buoy7_arm` | 6.9487e+06 | 6.0956e+05 | 7.5583e+06 | 1.172× |
| `hub3:buoy8_arm` | 6.9487e+06 | 6.2322e+05 | 7.5720e+06 | 1.171× |
| `hub3:buoy9_arm` | 6.9487e+06 | 6.2322e+05 | 7.5720e+06 | 1.171× |
| `hub4:buoy10_arm` | 6.9488e+06 | 4.8820e+05 | 7.3075e+06 | 1.168× |
| `hub4:buoy11_arm` | 6.9487e+06 | 4.6837e+05 | 7.3099e+06 | 1.169× |
| `hub4:buoy12_arm` | 6.9488e+06 | 4.6843e+05 | 7.3098e+06 | 1.169× |

## `T` (N·m)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 2.4539e-05 | 2.4539e-05 | 2.070× |
| `platform:hub2_arm` | 3.5155e-24 | 2.3469e+03 | 2.3469e+03 | 2.884× |
| `platform:hub3_arm` | 9.5131e-10 | 2.4538e-05 | 2.4537e-05 | 2.070× |
| `platform:hub4_arm` | 2.0680e-24 | 2.3469e+03 | 2.3469e+03 | 2.884× |
| `hub1:buoy1_arm` | 0.0000e+00 | 1.2093e-04 | 1.2093e-04 | 1.019× |
| `hub1:buoy2_arm` | 5.8263e-09 | 2.9158e+03 | 2.9158e+03 | 1.459× |
| `hub1:buoy3_arm` | 9.9251e-09 | 2.9158e+03 | 2.9158e+03 | 1.459× |
| `hub2:buoy4_arm` | 0.0000e+00 | 3.8008e+02 | 3.8008e+02 | 1.512× |
| `hub2:buoy5_arm` | 1.1156e-09 | 2.6440e+03 | 2.6440e+03 | 1.549× |
| `hub2:buoy6_arm` | 3.0510e-08 | 2.6414e+03 | 2.6414e+03 | 1.680× |
| `hub3:buoy7_arm` | 0.0000e+00 | 1.1194e-04 | 1.1194e-04 | 0.986× |
| `hub3:buoy8_arm` | 2.9983e-09 | 3.7505e+03 | 3.7505e+03 | 1.567× |
| `hub3:buoy9_arm` | 1.9714e-08 | 3.7505e+03 | 3.7505e+03 | 1.567× |
| `hub4:buoy10_arm` | 0.0000e+00 | 3.8008e+02 | 3.8008e+02 | 1.512× |
| `hub4:buoy11_arm` | 2.8489e-09 | 2.6414e+03 | 2.6414e+03 | 1.680× |
| `hub4:buoy12_arm` | 9.1187e-09 | 2.6440e+03 | 2.6440e+03 | 1.549× |

## `My` (N·m)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 1.9160e+08 | 3.0081e+07 | 2.1880e+08 | 1.602× |
| `platform:hub2_arm` | 1.9160e+08 | 3.6451e+07 | 2.2805e+08 | 1.494× |
| `platform:hub3_arm` | 1.9160e+08 | 4.7390e+07 | 2.3899e+08 | 1.589× |
| `platform:hub4_arm` | 1.9160e+08 | 3.6451e+07 | 2.2805e+08 | 1.494× |
| `hub1:buoy1_arm` | 1.2773e+08 | 5.7159e+06 | 1.3298e+08 | 1.094× |
| `hub1:buoy2_arm` | 1.2773e+08 | 5.6740e+06 | 1.3300e+08 | 1.094× |
| `hub1:buoy3_arm` | 1.2773e+08 | 5.6740e+06 | 1.3300e+08 | 1.094× |
| `hub2:buoy4_arm` | 1.2773e+08 | 9.4693e+06 | 1.3576e+08 | 1.084× |
| `hub2:buoy5_arm` | 1.2773e+08 | 9.3383e+06 | 1.3577e+08 | 1.084× |
| `hub2:buoy6_arm` | 1.2773e+08 | 9.3384e+06 | 1.3577e+08 | 1.084× |
| `hub3:buoy7_arm` | 1.2773e+08 | 1.2905e+07 | 1.4064e+08 | 1.091× |
| `hub3:buoy8_arm` | 1.2773e+08 | 1.2990e+07 | 1.4072e+08 | 1.090× |
| `hub3:buoy9_arm` | 1.2773e+08 | 1.2990e+07 | 1.4072e+08 | 1.090× |
| `hub4:buoy10_arm` | 1.2773e+08 | 9.4693e+06 | 1.3576e+08 | 1.084× |
| `hub4:buoy11_arm` | 1.2773e+08 | 9.3384e+06 | 1.3577e+08 | 1.084× |
| `hub4:buoy12_arm` | 1.2773e+08 | 9.3383e+06 | 1.3577e+08 | 1.084× |

## `Mz` (N·m)

| member | static | dyn | total | vs issue 3 total |
|---|---|---|---|---|
| `platform:hub1_arm` | 0.0000e+00 | 1.1485e+00 | 1.1485e+00 | 0.843× |
| `platform:hub2_arm` | 0.0000e+00 | 4.9417e+08 | 4.9417e+08 | 1.008× |
| `platform:hub3_arm` | 0.0000e+00 | 6.6035e-01 | 6.6035e-01 | 0.898× |
| `platform:hub4_arm` | 0.0000e+00 | 4.9417e+08 | 4.9417e+08 | 1.008× |
| `hub1:buoy1_arm` | 0.0000e+00 | 6.9452e-01 | 6.9452e-01 | 0.864× |
| `hub1:buoy2_arm` | 0.0000e+00 | 1.3170e+08 | 1.3170e+08 | 0.999× |
| `hub1:buoy3_arm` | 0.0000e+00 | 1.3170e+08 | 1.3170e+08 | 0.999× |
| `hub2:buoy4_arm` | 0.0000e+00 | 3.5740e+06 | 3.5740e+06 | 0.991× |
| `hub2:buoy5_arm` | 0.0000e+00 | 1.2281e+08 | 1.2281e+08 | 1.001× |
| `hub2:buoy6_arm` | 0.0000e+00 | 1.3192e+08 | 1.3192e+08 | 1.001× |
| `hub3:buoy7_arm` | 0.0000e+00 | 5.8054e-01 | 5.8054e-01 | 0.894× |
| `hub3:buoy8_arm` | 0.0000e+00 | 1.2959e+08 | 1.2959e+08 | 0.999× |
| `hub3:buoy9_arm` | 0.0000e+00 | 1.2959e+08 | 1.2959e+08 | 0.999× |
| `hub4:buoy10_arm` | 0.0000e+00 | 3.5740e+06 | 3.5740e+06 | 0.991× |
| `hub4:buoy11_arm` | 0.0000e+00 | 1.3192e+08 | 1.3192e+08 | 1.001× |
| `hub4:buoy12_arm` | 0.0000e+00 | 1.2281e+08 | 1.2281e+08 | 1.001× |

## ER3's `f` sensitivity — static case at `f` = 0.5, 0.75, 1.0

`f = 0.75` is the shipped build and reaches that value **through the ladder**, with
`admissible()` consulted (ES1). `f = 0.5` and `f = 1.0` are measurement-only builds:
they bypass the ladder, do not consult `admissible()`, and report a finding on every
body saying so — 5 findings at `f = 0.5` and 10 at `f = 1.0`. **`f = 1.0` puts the
entire body mass on the members and will never be on a ladder.**

| member | Vz @ 0.5 | Vz @ 0.75 | Vz @ 1.0 | My @ 0.5 | My @ 0.75 | My @ 1.0 |
|---|---|---|---|---|---|---|
| `platform:hub1_arm` | 6.1313e+06 | 6.1313e+06 | 6.1313e+06 | 2.2992e+08 | 1.9160e+08 | 1.5328e+08 |
| `platform:hub2_arm` | 6.1312e+06 | 6.1312e+06 | 6.1312e+06 | 2.2992e+08 | 1.9160e+08 | 1.5328e+08 |
| `platform:hub3_arm` | 6.1313e+06 | 6.1312e+06 | 6.1312e+06 | 2.2992e+08 | 1.9160e+08 | 1.5328e+08 |
| `platform:hub4_arm` | 6.1312e+06 | 6.1312e+06 | 6.1313e+06 | 2.2992e+08 | 1.9160e+08 | 1.5328e+08 |
| `hub1:buoy1_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub1:buoy2_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub1:buoy3_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub2:buoy4_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub2:buoy5_arm` | 6.9487e+06 | 6.9487e+06 | 6.9487e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub2:buoy6_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub3:buoy7_arm` | 6.9488e+06 | 6.9487e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub3:buoy8_arm` | 6.9487e+06 | 6.9487e+06 | 6.9487e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub3:buoy9_arm` | 6.9487e+06 | 6.9487e+06 | 6.9487e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub4:buoy10_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub4:buoy11_arm` | 6.9487e+06 | 6.9487e+06 | 6.9487e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |
| `hub4:buoy12_arm` | 6.9488e+06 | 6.9488e+06 | 6.9488e+06 | 1.4306e+08 | 1.2773e+08 | 1.1241e+08 |

**`Vz` does not move with `f` at all** — worst relative move `0.000000`, which
is exactly zero and not merely small. I drafted the opposite sentence for this section
and the measurement refuted it before it was sent: I expected the handed-down platform
share to break the independence `Vz` had in issue 3, and it does not. `f` moves mass
between two places that both lie inside the member's span, so the TOTAL weight each
member carries is conserved exactly, and the root shear is that total whatever the
split — on either basis, and with or without a share handed down from above.

`My` runs from `1.1200×` at `f = 0.5` to `0.8800×` at `f = 1.0` against the
shipped `f = 0.75`. Moving mass outboard raises the root moment; the lever is what `f`
changes.

