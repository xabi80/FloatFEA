# F2 step 4 — the patch test (V1.2 / G2.2)

**Backfilled 2026-09-03** from the report given at the time. Content unchanged,
**including its omission** — see `Carried`.

**Commits:** `e1ea251` (patch test), `eba50cf` (AX follow-up)

## Built

`tests/verification/rung1/test_patch_test.py` — displacement-driven patch test per
Irons. The exact field is imposed on the two end nodes; the interior nodes are
free and carry **zero load**; the interior response must reproduce the exact
field. The load-driven form is an equilibrium test wearing the patch test's name
and does not exercise connectivity, which is why V1.2 sits at rung 1.

Straight member, irregular mesh, both axis-aligned and skew-but-straight
orientations so the transform is in the loop without this becoming a frame test.
A non-collinear assembly stays at V2.4.

## Numbers — all four constant-strain states, relative to the exact field

```
axis-aligned   axial 2.88e-17  curvature 1.35e-16  twist 4.81e-17  shear 2.00e-16
skew straight  axial 4.21e-15  curvature 1.51e-15  twist 6.24e-16  shear 2.12e-15
```

Ceiling `1e-12`. Exact, not converged.

## AX follow-up, same step

**The commensurability check was written from the defects already met, and was
hiding a live one.** "No length an integer multiple of another" passed a mesh
containing `0.9/0.6 = 3/2` exactly and `2.8/1.7` within 0.02 of `5/3`. Rewritten
to sweep `p/q` for `p,q <= 5`; mesh replaced by search, closest approach `0.0877`.

Not cosmetic: removing the symmetry improved the weakest state's detection
threshold about **fivefold**, `1.51e-10 -> 3.31e-11`.

**Detection thresholds** measured, verified (perturbing by the threshold lands on
the ceiling to within 0.3%), and asserted:

```
axial 9.17e-12   curvature 2.69e-11   twist 9.17e-12   shear 3.31e-11
```

That assertion went red the moment the mesh changed, which is how the stale
counter-case was found.

Final: `242 passed`.

## Tolerances touched

| name | value | form | counter | justification |
|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS` | `1e-12` | relative, `/ max abs exact field` | `3.0e-8` | ~240x above the worst measured `4.19e-15`; exactness, not convergence |
| `PATCH_TEST_EXACTNESS_COUNTER` | `3.0e-8` | same quantity | — | smallest of the four states' responses to a `1e-6` single-element stiffness error; re-measured after the mesh change (was `6.0e-9`, stale) |

## Carried

**Three items from step 3 were NOT carried into this report, and were open when it
was written:**

- **AW1** — the form of `TRANSFORM_INVARIANCE`, the subdivision figure, and (new
  at this step) `PATCH_TEST_EXACTNESS`: relative to what scale? **OPEN.**
- **AW2** — was the subdivision agreement measured or asserted? **OPEN.**
- **AW3** — how did the `I_y != I_z` roll-invariance control obtain a `J` past
  `basis.torsion_constant`? **OPEN**, and it was an explicit gate: the step-3
  block ended "Proceed once AW3 is answered."

This omission is the failure `CLAUDE.md` § Step gating exists to prevent: a report
accurate about what it covers, with a stated condition sitting unaddressed
underneath it. It is recorded here rather than silently repaired, because the
backfill is meant to show the gate what actually happened.

**Answered in the revision below.**
