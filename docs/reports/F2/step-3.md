# F2 step 3 — transformation, sparse assembly, direct solve

**Backfilled 2026-09-03** from the reports given at the time. Content unchanged.

**Commits:** `170cb52` (step 3), `b2f7ae9` (AW follow-up)

## Built

- `floatfea/element/transform.py` — 12x12 block-diagonal `T` from the member
  triad; `to_global` computes `T^T K T`.
- `floatfea/assemble/system.py` — `BeamElement`, sparse assembly (COO -> CSR), a
  dense scatter-add assembly for cross-checking, boundary conditions, and a
  direct solve carrying **per-case** diagnostics.

## AV0/AV1 — the local element is block-diagonal

The earlier claim that the 12x12 has "21 independent coupling entries to pin" was
**withdrawn**. In local axes a straight prismatic member has *no* couplings: four
blocks, eight independent free-block entries, all already pinned at step 2. The
correct local assertion is that the off-block entries are **identically zero**,
which catches an index-mapping error leaking a term into the wrong block — a
defect that leaves every in-plane response correct. Asserted exactly zero, with a
meta-test that every block is populated.

Reciprocity asserted on the measured flexibility, including `uz` per unit `My`
equalling `ry` per unit `Fz`.

## AV2 — three invariances

Against a deliberately skew 37 degree Rodrigues rotation, all six load DOF:
rotation invariance, spectrum invariance, and roll invariance for a circular
section. The roll test has a negative control showing it fails for `I_y != I_z`.

## AV3 — step-3 hygiene

- Per-case equilibrium residual on every solve; `SolveResult` carries no aggregate
  by construction.
- Reaction equilibrium asserted per case in three directions, with a negative
  control that zeroing one reaction component is detected.
- Sparse assembly checked **bit-exact** against the dense scatter-add, a
  deliberately different code path, with a meta-test that the two are not
  trivially equal.
- Subdivision invariance: fixed total length at 1, 2, 5 and 11 elements gives an
  identical tip response.

## Numbers

`214 passed` after `170cb52`; `222 passed` after `b2f7ae9`.

Subdivision deviation and the conditioning signature:

```
n= 2  dev 9.99e-15    solve resid 5.86e-14
n= 5  dev 1.16e-14    solve resid 1.08e-13
n=11  dev 4.58e-13    solve resid 8.79e-13
```

## Tolerances touched

| name | value | form | counter | justification |
|---|---|---|---|---|
| `TRANSFORM_INVARIANCE` | `1e-11` | relative, `/ ||u_loc||_inf` | `1.2e-7` | floor `3.836e-15`; counter is the residual from a `1e-8` rad non-orthogonality |
| `TRANSFORM_SPECTRUM_INVARIANCE` | `1e-11` | relative, `/ max eigenvalue` | `5.0e-7` | floor `2.71e-16`; counter is a 1 mrad `I + [theta x]` map |
| `SUBDIVISION_INVARIANCE` | `1e-11` | relative, `tip/tip_1 - 1` | `4.8e-8` | worst measured `4.58e-13`; counter is a `1e-7` stiffness error in one member |

`TRANSFORM_INVARIANCE` was first written as an **absolute** `atol` on a
displacement — a dimensional quantity, and what V1.3 exists to catch. The identity
`K_glo_ff == R6^T K_loc_ff R6` was verified exactly *before* the tolerance moved.
`SUBDIVISION_INVARIANCE` existed as an undeclared `rtol=1e-10` literal inside the
test before it was measured.

## AW follow-up, same step

**AW3 is a finding.** `basis.torsion_constant` guarded only
`Section.circular_tube`; the dataclass constructor accepted
`Section(A=1.0, I_y=1.0, I_z=3.0, J=99.0, shape="i_beam")` with no check. The
step-2 claim that a non-circular section fails loudly at construction was false
for any caller not using the classmethod. Fixed in `__post_init__`.

## Carried

From step 2, all answered in `170cb52` / `b2f7ae9`:

- **AV1** (coupling generalisation withdrawn) — answered, `test_beam_element.py`.
- **AV0** (reciprocity) — answered, `test_reciprocity_maxwell_betti`.
- **AW1** (tolerance form and counter quantity) — answered, `tolerances.py`.
- **AW2** (undeclared subdivision literal) — answered, measured and declared.
- **AW3** (guard on the classmethod, not the type) — answered, `material.py`
  `__post_init__`; sixteenth guard recorded.
