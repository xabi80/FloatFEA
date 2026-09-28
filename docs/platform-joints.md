# The platform's 16 joints, measured

**DQ2 / DJ0. Verified 2026-09-28** against the assembled deck at the pinned HSP
tag, not against the prose.

`docs/milestones/F3.md` § 1 records DJ0's second half — *"all 16 joints are
two-rotation gimbals"* — as **a claim to verify, not a fact to assume**, and
defers the verification to F5-prep. This file is that verification. It is here
early because F3's joint work consumes the result: DJ0's own rule is that if a
joint is not a gimbal, F3's builder refuses the model rather than idealising it.

Every table below is produced by `python scripts/measure_platform_joints.py` at
the commit that publishes it (BI3). **No figure in this file is typed.**

---

## 1. What was measured, and why it is not the joint's name

DJ0, verbatim: *"A two-rotation gimbal is modelled as a release of the two free
moments with the locked-axis moment transmitted."*

That is a statement about the **reaction**, not about a label. So the measurement
takes an arbitrary multiplier vector, forms the generalised constraint force
`Gᵀλ`, and shifts body A's moment to the joint point:

```
M_joint = M_reference − arm × F
```

and requires the two components perpendicular to the locked axis to be absent.

```
claim  every joint transmits three forces and exactly one moment
cmd    python scripts/measure_platform_joints.py
out    two-rotation gimbals: 16 of 16
out    worst released-moment leak at the joint point : 2.753e-15
rule   |M_released| / |M_at the joint point| must be zero; the two perpendicular
       moments are absent by construction, not small
```

The leak is machine zero **structurally**: the Jacobian has one rotational row per
joint, so there is no row that could generate a perpendicular moment at any
operating point. A figure this size is not a number that could grow elsewhere.

## 2. The joints

| # | body A | body B | kind | rows | translations locked | moments locked | moments released | `\|attach_a\|` |
|---|---|---|---|---|---|---|---|---|
| 1–3 | buoy1–3 | hub1 | `yaw_locked` | 4 | 3 | 1 | 2 | 1.6890 m |
| 4 | hub1 | platform | `yaw_locked` | 4 | 3 | 1 | 2 | 0.0000 m |
| 5–7 | buoy4–6 | hub2 | `yaw_locked` | 4 | 3 | 1 | 2 | 1.6890 m |
| 8 | hub2 | platform | `yaw_locked` | 4 | 3 | 1 | 2 | 0.0000 m |
| 9–11 | buoy7–9 | hub3 | `yaw_locked` | 4 | 3 | 1 | 2 | 1.6890 m |
| 12 | hub3 | platform | `yaw_locked` | 4 | 3 | 1 | 2 | 0.0000 m |
| 13–15 | buoy10–12 | hub4 | `yaw_locked` | 4 | 3 | 1 | 2 | 1.6890 m |
| 16 | hub4 | platform | `yaw_locked` | 4 | 3 | 1 | 2 | 0.0000 m |

64 constraint rows over 102 DOF, which reproduces
`../HSP-runs/docs/platform-geometry.md:67` — *"Joints = 16 IDENTICAL `yaw_locked`
… m = 16 × 4 = 64 constraints"* — from the assembly rather than from the sentence.

## 3. THE CELL, and it is here because the first measurement of this was wrong

**A first measurement took the rank of all four constraint rows in body A's
rotational columns and read rank 3 on the twelve buoy↔hub joints**, which says
they are not gimbals. That rank is real. It is not a joint moment.

Rows 0:3 are the **translational** lock, and their entries in the rotational
columns are `−skew(arm_a)` — the moment of the constraint **force** about body A's
reference point. Row 3 is the **rotational** lock, and it is the only row carrying
a joint moment.

The variable that separates them is the attach offset, and the platform holds it
at two values with the joint kind, the axis and the code path all unchanged:

```
cell   ONE VARIABLE: |attach_a|. Same kind, same axis, same Jacobian assembly.
cmd    python scripts/measure_platform_joints.py
out    |attach_a| = 0.0000 m  ( 4 joints)  rank over all 4 rows = 1   lock row = 1
out    |attach_a| = 1.6890 m  (12 joints)  rank over all 4 rows = 3   lock row = 1
judge  the rank over all four rows MOVES with the offset; the rank over the lock
       row does not. That is what identifies the first as the force's moment
       about the reference point rather than as a transmitted joint moment.
```

Without this cell the wrong rank is the one a reader re-derives, because it is the
one an obvious measurement produces.

## 4. Two properties F3's builder must carry

**The locked axis is body-A-fixed, not world-fixed.** `axis_world = R_A · ẑ`:

```
claim  the locked axis follows body A, and equals world z only at the reference
cmd    python scripts/measure_platform_joints.py
out    worst locked axis vs R_A z            : 2.220e-16
out    worst locked axis vs world z at xi = 0: 0.000e+00
```

So the released moments are about the two axes perpendicular to **body A's local
z**, and body A is the buoy on twelve joints and the hub on four. A linear model
at the reference configuration sees world `ẑ`, which is why the distinction has to
be written into the joint interface rather than discovered later.

**The reaction is equal and opposite**, worst asymmetry `0.000e+00` over 16 joints
— so a release applied at one end and not the other would be visible, and is not
present.

## 5. Where the joints are

All 16 lie in one horizontal plane and the two attach points coincide exactly
(worst gap `0.00e+00` m at the reference configuration). Hub joints at radius
1.0 m model scale on ±x and ±y; each cluster's three buoy joints at radius 0.5 m
from its hub.

**The arms are AXIAL, not diagonal.** `CLUSTER_ANGLES_DEG = [0, 90, 180, 270]`
in `../HSP-runs/studies/platform-12buoy/platform_common.py:34`, so the two
crossing arms run along ±x and ±y. It is therefore the **0° heading** that travels
along an arm, not 45°. This is recorded here because the opposite was published in
`docs/reports/F2/step-7.md` and is also written into `docs/milestones/F3.md:25`
("two diagonal arms"), which is one of R576's three strands.

Which heading governs the arms has **not** been measured and no claim about it is
made here.
