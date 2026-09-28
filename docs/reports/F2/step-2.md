# F2 step 2 — Timoshenko beam element, local stiffness

**Backfilled 2026-09-03** from the reports given at the time. Content unchanged.

**Commits:** `dfb5808` (element), `8a02930` (AU follow-up)

## Built

`floatfea/element/beam.py` — axial, torsion, and shear-flexible bending in both
planes. Przemieniecki 1968 with equation numbers (§5.2, §5.3, §5.6), cross-checked
against Cook et al. 4th ed.

## Checkpoint 1 — `Phi -> 0` recovers Euler-Bernoulli: PASSED

Asserted **entry-wise and bit-exact** (`np.array_equal`), not as a deflection at a
tolerance.

Made falsifiable: in a `1/(1+Phi)` formulation the comparison passes *by
construction*, so `euler_bernoulli_bending_stiffness` is transcribed independently
from Przemieniecki eq. 5.20 rather than being `bending_stiffness(..., phi=0)`, and
`test_the_phi_zero_check_CAN_FAIL` perturbs one shear-coupling term by 1 part in
1e9 and confirms the assertion goes red.

## Checkpoint 2 — nodal exactness at N = 1

One-element cantilever against the closed form, end force and end moment:

```
slender  L/D=25  Phi=0.0112   force rel 1.11e-16   moment rel 1.11e-16
stubby   L/D=3   Phi=0.7769   force rel 0.00e+00   moment rel 3.33e-16
```

## AU follow-up, same step

- **AU1** — the `Phi = 0` check pins the *limit* but not the *placement*: any
  `K_EB * f(Phi)` with `f(0) = I` passes it. The cantilever tests are now
  **over-determined** — deflection *and* rotation, under end force *and* end
  moment, at both `Phi` values: four equations for the three independent entries
  of the symmetric 2x2 free block. All pass at `rel 1e-13`.
- **AU2** — the `diag(1,-1,1,-1)` flip measured now rather than at V2.4. The x-z
  plane is asserted against its own closed form, **signed**: `force_z -> uz
  +7.026e-03, ry -3.677e-03`; `moment_y -> uz -3.677e-03, ry +3.064e-03`. A
  negative control shows a magnitude-only assertion passes on a block built with
  the flip omitted.
- **AU3** — `basis.torsion_constant` added, raising for non-circular shapes.
  **This was later found to be misplaced — see step 3 and the step-4 revision.**
- **AU4** — V2.2's tolerance provenance recorded: nodal exactness is exact, so the
  tolerance is a ULP multiple justified by the four measured values, with a
  counter-case of 16.3% (an Euler-Bernoulli element mislabelled as Timoshenko).

## Numbers

`174 passed` after `dfb5808`; `184 passed` after `8a02930`.

## Tolerances touched

None in this step. `AS3`'s bound was restated as an inequality in `basis.py`
(`shear_geometric_bound`), which is a derived quantity, not a tolerance.

## Carried

From step 1: nothing was left open — step 1 and step 2 landed in one commit.

From the AS/AT review blocks, all answered in this step's commits: AS1 (`kappa`
computed, never stored), AS2 (`sections.py` -> `basis.py`), AS3/AT1 (the bound as
an inequality, with material scaling), AS4 (nodally exact rather than
locking-free), AS5 (slenderness as the discriminating axis).
