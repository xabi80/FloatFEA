# Conventions — TEMPLATE, to be completed and locked at F0

**Status: NOT LOCKED.** This is a skeleton. Gate G0.2 is not satisfied until
every field below is filled with a specific answer and the document is reviewed
and merged.

This document is authoritative. Where any other file, comment, or docstring
disagrees with it, this file wins. Changing it after F0 requires reopening the
F0 gate, not an inline edit.

Fill it by reading FloatSim's `docs/multibody-conventions.md` and reconciling
against it explicitly. Where the two projects differ, the transformation is
written here, once, and referenced everywhere else. Do not resolve a difference
by silently adopting one side.

---

## Units

SI throughout, internally, with no exceptions: metres, kilograms, seconds,
newtons, radians. Conversion happens only at the I/O boundary. A conversion
found inside the numerics is a defect.

State here whether FloatSim's output matches, and if not, exactly where the
conversion happens.

- Length: m
- Mass: kg
- Time: s
- Force: N · Moment: N·m
- Angle: rad
- Stress: Pa
- **FloatSim agreement:** *[confirm or describe the conversion]*

## Global frame

- Origin: *[e.g. still-water level at the platform geometric centre — state it]*
- x axis: *[direction and physical meaning]*
- y axis:
- z axis: *[up positive? state it explicitly]*
- Handedness: *[right-handed — confirm]*
- Vertical datum: *[still-water level? seabed? state it]*
- **FloatSim agreement:** *[same frame, or the transformation]*

## Body frames

- Origin: *[body CoG, or a geometric reference point — state which]*
- Axis orientation relative to global at rest:
- **FloatSim agreement:**

## Rotations

- Representation: **rotation vector (axis-angle)**, matching FloatSim. Quaternion
  and Euler channels do not exist upstream and are not carried.
- Direction of the rotation (body←global, or global←body) must be stated; the
  representation alone is ambiguous.
- **Reconstruct rotations with Rodrigues, never with the linearised map.** A
  rotation vector is an *exact* parameterisation; only FloatSim's internal use
  of it is linearised. Applying `I + [θ×]` in FloatFEA yields a non-orthogonal
  matrix that stretches every transformed vector by `√(1+θ²)` — 1.5% at 10°,
  4.3% at 17° — which silently magnifies transformed loads. Rodrigues is
  orthogonal by construction and costs nothing.
- **FloatSim agreement:**

## Timestamps within a single RHS

FloatSim evaluates different force terms at different times inside the same
right-hand side: `state_force` from `(t[n], xi_n, xi_dot_n)` and
`external_force` at `t[n+1]`. Record here the index each exported channel is
aligned to. This is a trap that bites twice — once on export, once on any later
channel added by analogy to an existing one.

## Sign conventions

- Positive axial force: *[tension positive — confirm]*
- Positive bending moment: *[state the convention and the fibre it refers to]*
- Positive shear:
- Positive torque:
- Gravity vector: *[e.g. (0, 0, -9.80665) — state the value used, and confirm
  it matches FloatSim's exactly; a mismatch here is a silent mass error]*
- **FloatSim agreement:**

## Numbering and identifiers

- Node numbering scheme:
- Element numbering scheme:
- Body identifiers: *[must match FloatSim's exactly, or the mapping is stated]*
- Member identifiers: *[must be stable across model regeneration, because the
  envelope reports and golden files key on them]*
- Connector and mooring line identifiers:

## Machine-readable copy

Gate G0.2 requires the frame definitions above to also exist in a
machine-readable form that the interchange validator checks records against.
State here where that lives and confirm the two are generated from, or tested
against, each other — two hand-maintained copies of the same convention will
diverge.

## Reconciliation summary

A short table of every place FloatFEA and FloatSim differ, with the
transformation for each. If this table is empty, say so explicitly — "checked,
no differences" is a finding worth recording, and it is different from nobody
having looked.
