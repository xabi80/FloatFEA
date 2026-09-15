# F2 step 1 — nodes, DOF numbering, containers

**Backfilled 2026-09-03** from the report given at the time, to give the step gate
something to stand on. Content unchanged; no work is described here that is not in
the diff.

**Commit:** `dfb5808` (covers steps 1 and 2)

## Built

- `floatfea/model/nodes.py` — `Node`, `NodeSet`, `Model`, with DOF numbering
  structural (`node_dofs`, `element_dofs`) rather than `6*i+3` written by hand at
  call sites.
- `floatfea/model/material.py` — `Material` and `Section` containers that declare
  no constants; every value comes from `basis.py`.

## Numbers

`174 passed` (whole suite, at the end of step 2).

## Decisions carried into the code

- Numbering follows **insertion order**, never set or dict iteration, per
  `floatfea/determinism.py`: `PYTHONHASHSEED` permutes set iteration and an
  assembly ordering built that way silently permutes the matrix.
- A self-connected element is refused — zero length means no axis and no triad.
- `Material.G` is a **property**, derived from `E` and `nu`, so the three cannot
  drift apart. A `G` field would let a caller construct a material whose three
  values disagree with nothing downstream noticing.
- `Section` carries a **shape name**, not a `kappa`. `kappa` depends on both
  section geometry and `nu`, so it belongs to neither container alone
  (AS1). A test asserts structurally that neither container has a `kappa` field.

## Tolerances touched

None.

## Carried

No previous step. Open items inherited from the lock Q&A and the AS/AT review
blocks were addressed in the same commit and are reported under step 2.
