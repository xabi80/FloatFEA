# F6b — TRUSS SIZING FROM THE BEAM FORCES (increment 1b)

<!-- CLOSED. The step marker moved to docs/milestones/R1.md with R1 step 1's report
     (FB4: "the marker moves in the commit that adds the step's report"). F6b closed
     at its closing verdict, which carries `Closes: F6b` (FK1). -->

Opened by **DIRECTIVE FI**. Lighter process as FG1: **one step, one reviewed report
revision, then EQ0 closure.** CZ0's blocking criterion is unchanged, including EZ0's
published deliverable. No new report guards and no new meta-tests. Corpus batches stay
paused. Review effort goes to the numbers: the reviewer recomputes the governing chord
force and its required area by hand.

**Target: 3 days (FI5).** Then STOP (FG6).

---

## 1. The directive, verbatim

**FI0 — PURPOSE:** convert F4's governing beam forces into chord and diagonal forces for a
space truss replacing each arm group's stand-in tube, and size it. Post-processing only: no
FloatSim, and the frame model is unchanged (FG2's premise: forces are independent of
section).

**FI1 — IDEALISATION** (declared, labelled INDICATIVE): pin-jointed parallel-chord truss,
no secondary bending. Two cross-sections:

* **(a) a BOX**, with 4 chords at `(±b/2, ±h/2)`:
  `chord force = N/4 ± My/(2h) ± Mz/(2b)`;
* **(b) a TRIANGLE**, with 3 chords (two bottom at `±b/2`, one top): forces from its own
  section properties, stated.

Shear `Vz` goes to the vertical faces and `Vy` to the horizontal faces; torsion `T` goes as
shear flow `T/(2·A_enclosed)`. Diagonals at 45° (panel length = the face dimension);
diagonal force = face shear / sin θ. Use per-instant forces at ROOT / MID / TIP over the
governing basis (EZ2 / FA0). Signs are preserved, so each chord's max tension and max
compression are found per instant.

**FI2 — SIZING** (API RP 2A-WSD, `Fy = 355 MPa`, as F6): chords and diagonals are tubes at
a declared `D/t = 24` (compact); tension `0.6·Fy`; compression § 3.2.2 with `K = 1.0` and
`L` = the panel length (the bracing restrains the chord), solved for the minimum area;
report each member's governing case and station. Truss line mass =
`(Σ chord A + diagonal A·length per panel / panel length)·ρ`, times a declared joint
allowance of `1.15`.

**FI3 — SWEEP:** `h ∈ {2, 3, 4, 5, 6, 8, 10} m` and `b ∈ {2, 3, 4, 5, 6, 8} m`, both
cross-sections, both arm groups (the platform arms, `L = 50 m`; the hub arms, `L = 25 m`).
For each `(h, b)`: required chord `A`, diagonal `A`, truss line mass, and the ratio to `μ`
(platform `9.375 t/m`, hubs `15.0 t/m`). **Headline: the SHALLOWEST mass-consistent truss
per group, and per width.**

**FI4 — ALSO REPORT**

* **(i)** the `My / Mz` split (static and dynamic) at the governing station, so the reader
  sees how much of the demand is horizontal bending;
* **(ii)** the truss's bending stiffness (`A_c·h²`, `A_c·b²`) against the stand-in's
  `I = 0.888 m⁴`. A note only: forces do not depend on it here;
* **(iii)** a check of the hand table (two chords, `σ = 213 MPa`, `M = 324 MN·m`):
  `A_c ≈ 0.51 / 0.38 / 0.30 / 0.25 m²` at `h = 3 / 4 / 5 / 6 m`. Confirm or correct it, and
  say how much compression buckling and the diagonals add.
* **(v)** a flag: FloatSim's platform CoG sits `10.33 m` above the joints, which is
  inconsistent with a shallow truss unless mass sits high. Quantify how much of the
  governing horizontal moment comes from the remainder's height (the remainder at `41 m`),
  as an input to increment 2.

**FI5 — DELIVERABLE:** `results/F6b/truss_sizing.md` plus a CSV, generated (EV3, EZ0). A
one-page table, a half-page of findings, and the label (INDICATIVE: idealised pin-jointed
truss, no joint or connection checks, placeholder masses, heading 0°, `Fy` assumed). The
reviewer recomputes the governing chord force and its required area by hand. Target 3 days.
Then STOP (FG6).

*(FI4 has no (iv). The directive's numbering is reproduced as received.)*

---

## 2. What was measured before planning, because the plan depends on it

### 2a. The local axes, pinned rather than assumed

`docs/conventions.md` § "Member local axes" gives `local x = unit(B − A)`,
`local z = unit(r − (r·x)x)`, `local y = z × x`. For every platform arm the triad computes
to:

```
claim  all four platform arms are horizontal with local z VERTICAL, so My is vertical
       bending and Mz is horizontal bending -- which is what FI1's `My/(2h)` and
       `Mz/(2b)` pairing assumes
cmd    build_superstructure(), then member_local_axes on each platform member
out    platform:hub1_arm  x=[1. 0. 0.]  y=[0. 1. 0.]  z=[0. 0. 1.]
       platform:hub2_arm  x=[0. 1. 0.]  y=[-1. 0. 0.] z=[0. 0. 1.]
       platform:hub3_arm  x=[-1. 0. 0.] y=[-0. -1. 0.] z=[0. 0. 1.]
       platform:hub4_arm  x=[-0. -1. 0.] y=[1. -0. 0.] z=[0. 0. 1.]
rule   `h` is the vertical dimension and `b` the horizontal one, which is also what
       "Vz goes to the vertical faces and Vy to the horizontal faces" requires
judge  the pairing in FI1 is correct for this model and is not being assumed here.
```

### 2b. The `My`/`Mz` structure, which decides what FI3's headline can say

```
claim  the governing envelope per group, and the per-arm split
cmd    the total_instant rows at the four governing periods, enveloped
out    PLATFORM  max|My| = 2.2324e+08   max|Mz| = 2.6890e+08
                 max|N|  = 9.1925e+06   max|Vy| = 5.7485e+06  max|Vz| = 5.9134e+06
                 max|T|  = 2.4832e+02
         platform:hub1_arm  max|My|=2.183e+08  max|Mz|=2.851e-01
         platform:hub2_arm  max|My|=1.802e+08  max|Mz|=2.689e+08
         platform:hub3_arm  max|My|=2.232e+08  max|Mz|=3.249e-01
         platform:hub4_arm  max|My|=1.802e+08  max|Mz|=2.689e+08
       HUBS      max|My| = 1.3449e+08   max|Mz| = 7.5994e+07
                 max|T|  = 1.1175e+03
rule   EZ2/FA0's governing basis: `total_instant` at T in {12.5, 14.0, 15.0, 16.2}
judge  **the split is the arm's ORIENTATION, not the physics.** At heading 0° the arms
       along the wave direction take the demand as `My` and the transverse arms take it as
       `Mz`; the arms are geometrically identical and `My = 1.916016e+08` on all four at
       ROOT static, to the digit (verdict 122's (a) ruling).
```

**THE CONSEQUENCE, AND IT IS THE PLAN'S ONE REAL DECISION.** A tube is axisymmetric, so F6a
only ever needed the resultant `M_res`. A truss with `h ≠ b` is not. Sizing *one* section
per arm group — which is FG2's two groups, unchanged here — means the group's requirement is
the envelope over its members, so:

> **`b` may not be made small on the grounds that `Mz ≈ 0`**, because `Mz ≈ 0` is true of
> two platform arms and `2.689e+08` is true of the other two. Both dimensions have to carry
> `2.2`–`2.7e+08` somewhere in the group.

This is decided rather than asked, because the alternative — sizing each arm for its own
orientation — would deliver four different platform arms at one heading and is void the
moment increment 3 changes the heading. **It is stated in the deliverable as a finding, not
buried as an assumption.**

### 2c. Torsion is retained and is negligible, which is a result rather than a reason to drop it

`max|T|` is `248 N·m` on the platform and `1118 N·m` on the hubs, against moments of
`10⁸ N·m`. FI1's shear-flow term `T/(2·A_enclosed)` is implemented as specified and will
contribute ~`10⁻⁵` of the face shear. **Reported as measured, not assumed away** — a term
dropped because someone expected it to be small is the shape BP0 exists for.

### 2d. FI4(v)'s two heights, confirmed from the model

```
claim  the two heights FI4(v) cites are the model's own
cmd    build_superstructure(): the platform body's nodes, deck_cog and remainder_point
out    node 0: platform_centre      [ 0.    0.   24.67]
       node 5: platform_remainder   [ 0.   -0.   65.99]
       deck_cog                     [ 0.    0.   35.  ]
       remainder_mass 6.2500e+05    link_length 41.326086404053946
judge  the joints are at `z = 24.67`; the deck CoG is `35.0`, i.e. **`10.33 m` above the
       joints**, and the remainder is at `65.995`, i.e. **`41.33 m` above them**. Both
       figures in FI4(v) are confirmed.
```

### 2e. FI1(b)'s triangle, derived — the properties the directive asks to be stated

Three chords of equal area `A_c`: two at `(y, z) = (±b/2, 0)` and one at `(0, h)`.
Centroid `z̄ = h/3`.

```
I_yy = A_c[2(h/3)² + (2h/3)²] = (2/3)A_c h²        I_zz = A_c·2(b/2)² = A_c b²/2
```

Chord force from `F_i = A_c · M · z_i / I`:

| chord | from `N` | from `My` | from `Mz` |
|---|---|---|---|
| top `(0, h)` | `N/3` | `+My/h` | `0` |
| bottom `(+b/2, 0)` | `N/3` | `−My/(2h)` | `+Mz/b` |
| bottom `(−b/2, 0)` | `N/3` | `−My/(2h)` | `−Mz/b` |

Equilibrium checks, both exact: `ΣF = My/h − 2·My/(2h) = 0`, and
`ΣM = (My/h)(2h/3) + 2(My/(2h))(h/3) = My`.

**The asymmetry is the point and it is reported:** the apex carries twice the `My` force of
either bottom chord, and **the top chord carries no `Mz` at all** — so a triangle resists
horizontal bending on its bottom pair alone, with lever `b` rather than the box's `2·(b/2)`
doubled pair. Apex-up is declared; both moment signs are evaluated per instant, so hogging
(apex in tension) and sagging (apex in compression) are both found.

`A_enclosed = b·h/2` for the triangle and `b·h` for the box.

---

## 3. Steps

**One step (FG1).** `docs/reports/F6b/step-1.md`, one reviewed revision, then EQ0 closure.

1. `scripts/measure/f6b_truss_sizing.py` — the resolution, the sizing and the sweep,
   reusing `floatfea/checks/api_wsd.py`'s clause functions rather than transcribing them a
   second time.
2. `scripts/measure/f6b_report.py` — FI5's deliverable, generated end to end, no typed
   measured figure (R781).
3. `results/F6b/truss_sizing.md` + `.csv`.

## 4. Tolerances

**None expected.** `D/t = 24`, the joint allowance `1.15`, the 45° diagonals, the sweep
grids and `Fy = 355 MPa` are all FI's declared inputs, not tolerances — they are reported as
declared and carried in the deliverable's label. If anything in execution needs a value
chosen to make two numbers agree, that is a tolerance and it stops and asks.

## 5. What this increment does NOT do

No joint or connection design, no secondary bending, no buckling of the diagonals as a
system, no heading other than 0°, no mass iteration (increment 2), and no change to the
frame model or to FloatSim.
