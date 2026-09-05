# Review — F2 step 4
Reviewed commit: ad2246afd2d160a85d319dadbf604a9e63796c84
Verdict: STOP
Tests: 502 passed, 0 failed, 0 skipped   (my run at ad2246a, `python -m pytest -q`, 1.78s)

Eighth pass. Reviewed range `25b2dcb..ad2246a`, nine commits, one of them a
standalone `process:` commit touching no code. My own corpus grew by **14
entries** this round (`tests/corpus/`, now 50), committed separately immediately
before this verdict; the coverage number is at the end. With the corpus applied
the suite is **5 failed, 520 passed**, and every one of the five reds is a
finding rather than a bad entry.

**This is a STOP, and it is the standing instruction's STOP.** The round was
asked to settle the tolerance FORM, which now claims three properties: a
unit-invariant floor, a bounded self-reference, and the constant cap. I tested
all three adversarially and two of the three are defective, one decisively:

* **A clean, admissible model that the constant accepts, the floor-aware term
  refuses.** `D = 0.6 mm, t = 6 um, L = 9.67 mm, skew, roll = -2.5` -- three
  fields already in this corpus, combined for the first time -- gives a worst
  field error of `4.4681e-13` against a floor-aware ceiling of `4.2034e-13`
  (**1.063x, red**) while sitting at `0.447` of `PATCH_TEST_EXACTNESS`. It is
  round-off and nothing else: the same configuration gives `0.174` under
  NATURAL, `0.112` under MMD_ATA and `0.195` under MMD_AT_PLUS_A. The gate
  reddens on a correct element, and the cheapest fix for that red is to widen
  the factor.
* **The new floor is not frame-invariant, and the old one was.** `cond(K_ff)` is
  `9.20958e+02` for *every* orientation of the same beam, exactly, because a
  rotation is an orthogonal congruence. `cond(K~)` is `1.0596e+02` axis-aligned,
  `3.8491e+02` skew, `6.3199e+02` at 45 deg -- **5.97x on the same physical
  model**, across the two orientations the gate is itself parametrised over.
* **And it does not track slenderness in one of those two orientations.** The
  entry publishes `121.7x` over `D = 0.6 .. 0.05`. That is the skew number. At
  axis-aligned the same sweep gives `105.96 -> 433.88`, **4.09x** -- flat, and
  below the constant throughout. "Not a constant wearing a floor's clothes" is
  true along one axis and false along the other.

Which is the seventh verdict's own closing question, one axis further out:
*for every ratio and every span in this diff, which axis was it measured along,
and what does it do along the other one?* The answer this round is **the frame**.
R55 moved the form off the unit axis and onto an axis nobody measured.

Per the standing instruction the form does not get elaborated again. **Return
`PATCH_TEST_EXACTNESS` to being the ceiling**, record `slender_L_r_79`, `_94`,
`_118` and `very_slender_L_r_189` as known round-off exceedances with the
permutation cell already at `tolerances.py:406-420` as their evidence, and take
the floor-aware criterion out of `F2.md` D7 item 5 -- which, separately, still
names the formula the code stopped using (**R74**).

**What is NOT the reason for the STOP, and should not be lost in it.** No
element defect was found, again. No existing accuracy ceiling moved: `git diff
-U0 25b2dcb..HEAD -- floatfea/tolerances.py` filtered to `Final[float]` gives one
addition and one modified pair. The strict parser (R57), the `residual`
docstring (R61), the `_COUNTER_DEFECT` numbers (R60) and the uniform-blindness
correction (R59) are real improvements, and three of them I verified by
re-running the mutation. The admission limit is a sound idea carried too far
(**R73**). Two of the four gated items are answered.

## Carried

Every item from the seventh verdict (`HOLD @ 83b2de2`, committed `25b2dcb`),
traced through `25b2dcb..ad2246a` and re-measured. The blocking four first.

- **1. R55 (gated) -- HALF ANSWERED, and the half that was done introduced
  R69/R70.** `977514f`. The floor is now `cond(equilibrate(K_ff))` and the unit
  invariance is real: I measured `3.84914e+02` at `S = 1e-3, 1, 1e3`, spread
  `1.000000x`, and it is exact rather than incidental -- a length-unit change is
  a diagonal congruence and `equilibrate` divides it out. The corpus runner now
  asserts `min(floor-aware, constant)` on `expect=hold`
  (`test_corpus_configurations.py:346`), which was the second half of the
  closing condition and is done. **The third half is not**: `F2.md` D7 item 5
  still reads "PATCH_TEST_COND_FACTOR * cond(K_ff) * eps" -- the unequilibrated
  form, which is the formula the code does NOT implement. One command:
  `grep -n "cond(K_ff)" docs/milestones/F2.md` gives line 946. A closing
  condition that names sites is closed site by site (CLAUDE.md, Step gating);
  this one named `tolerances.py`, the helper docstring and `F2.md`, and the
  third was left. **R74.**
- **2. R56 (gated) -- NOT ANSWERED as measured.** `8217c65`. The bound mechanism
  is real, the published bound is wrong at this commit, and it does not hold on
  the branch where it matters most: **R71** and **R72**. The sentence "the
  ceiling moves by at most 1.13x under any defect" is correctly withdrawn and
  the uniform class is correctly named, which was the wording half.
- **3. R57 (gated) -- ANSWERED for field NAMES, not for field VALUES.**
  `7c66c35`. `typo_field_roll_rad` goes green by raising, seven malformed shapes
  each have a test, and per-line rather than per-file handling is the right call
  and better than what I asked for. But `_section` still reads only the `D` and
  `t` that follow the first comma: measured at `ad2246a`,
  `section=rectangle,D=0.600,t=0.01200` builds a **circular tube** and returns
  `1.251313e-14`, bit-identical to the reference -- and so do a stray key inside
  the section spec and a repeated `orient=` field. Three new corpus entries, all
  red. **R75.**
- **4. R58 (gated) -- ANSWERED IN THE HALF I DID NOT ASK FOR, AND NOT IN THE
  HALF I DID.** `5de8fd8`. The closing condition named two sites:
  `PATCH_TEST_EXACTNESS_COUNTER`'s entry stating the geometry it was measured at
  and the direction it degrades in, and `very_stubby_L_r_0p5` green or named.
  The second was achieved by refusing the configuration. **The first was not
  touched at all** -- the diff of `floatfea/tolerances.py` has no hunk between
  lines 488 and 509, and the entry still gives no D, no t, no L and no
  direction. That is not a wording point: the counter's domain fails on a
  **second axis the admission limit does not cover**. At `I_y/I_z = 500`, member
  `L/D = 16.12` and fully admissible, the weakest state responds to the 1e-6
  control at `8.6804e-08`, below `1.0e-07`. Corpus entry `aniso_I_y_500x`, red
  at `ad2246a`. **R73.**
- **5. R59 -- ANSWERED, and the narrowed claim is wrong in the other
  direction.** `cbb265f`. The independent-reference harness is the right fix and
  I reproduced both cells (`nu` caught at `5.5281e-04`, section at `7.3011e-03`).
  But "E is the only property in this model that scales K uniformly"
  (`test_patch_test.py:1063`) is false. **R76.**
- **6. R60 -- ANSWERED.** `beeb4f5`. The two cells now carry `2.5283e-07` and
  `1.0103e-14`, my own measured values to five digits, and the spread of 2.5e7
  is stated.
- **7. R61 -- ANSWERED.** `beeb4f5`. The `residual` docstring names
  `test_assembly_and_solve.py:133` and `:197` and routes the tolerance reuse to
  step 4a rather than contradicting itself.
- **8. R62 -- NOT ANSWERED.** The vacuous assertion was replaced by a different
  vacuous assertion: **R77**.
- **9. R63 -- NOT ANSWERED, and reported as answered.** The report's recordables
  read "R60, R62, R63 (beeb4f5)" and then describe three items that are R60, R61
  and R62. Re-measured, each mutation alone, whole suite at `ad2246a`:
  `MATRIX_SYMMETRY 1e-9 -> 1e-4` **502 passed**; `ROUNDOFF_IDENTITY 1e-14 ->
  1e-9` **502 passed**; `COND_UNIT_INVARIANCE 1e-6 -> 1e-4` **502 passed**. All
  three are still widenable in silence by 1e5x, 1e5x and 1e2x. Carried.
- **10. R64 -- ANSWERED in form, and the band it names is a round-off
  realisation.** `71f5919`. The published band reproduces exactly: `3.0` gives
  `1 failed`, `3.2` and `8.0` give `502 passed`, `8.2` gives `1 failed`. Moving
  to a centred value was right. See **R71** for the two numbers in that same
  paragraph that contradict each other, and **R69** for what the lower edge of
  that band actually is.
- **11. R65 -- still open**, unchanged and correctly so: the three
  `expect=breach` entries still pin round-off at 1.0% and 2.8% of margin. Mine
  to fix in the corpus, not the implementer's.
- **12. R66 -- TWO OF THREE HOOK HOLES CLOSED AND VERIFIED; THE THIRD IS
  REPORTED CLOSED AND IS NOT.** `7c60eed`, a standalone `process:` commit citing
  BH5 and touching only `.claude/`. Reading-order item 4b is **R78**.
- **13. R67 -- ANSWERED by behaviour.** Eight of nine commits carry one finding
  each; no bundling this round.
- **14. R68 -- ANSWERED.** Revision 8's "Still open" line lists R6, R16, R25,
  R30-R33, R36, R61, R65-R68. R30 was recorded answered in the seventh verdict
  and R63 is listed as answered when it is not -- but the list is complete and
  the regression the sixth verdict warned about did not repeat. Keep that.
- **15. R50, R52 -- still open**, correctly declared. R52's second half became
  R73, which is where the substance went.
- **16. R6, R16, R25, R31, R32, R33 (outside G2.2), R36 -- still open**, in step
  4a and step 5, unchanged and correctly unchanged. `pin_threads` still has one
  caller. `equilibrate` still takes `abs()` of the diagonal, and that note stops
  being cosmetic the moment a ceiling is computed from that diagonal.

## Findings

**R69. (STOP) The floor-aware ceiling REJECTS A CLEAN, ADMISSIBLE MODEL that the
constant accepts, and which of the two happens is decided by the pinned
fill-reducing permutation.** `floatfea/tolerances.py:513-606`,
`tests/verification/rung1/test_patch_test.py:361-375`,
`tests/verification/rung1/test_corpus_configurations.py:346`.

Measured at `ad2246a` through the shipped `test_corpus_configurations` helpers,
on `D = 6.0e-4 m, t = 6.0e-6 m, L = 9.67e-3 m, skew, roll = -2.5 rad`:

```
state           err        err/ceiling   err/constant
axial        4.4681e-13      1.0630        0.4468     <-- red
curvature    6.2181e-14      0.1479        0.0622
twist        1.0861e-15      0.0026        0.0011
shear        2.6183e-14      0.0623        0.0262
curvature_xz 4.9740e-14      0.1183        0.0497
shear_xz     4.7002e-14      0.1118        0.0470

cond(K~) 3.78607e+02   ceiling 4.2034e-13   constant 1.0e-12
L/D = 16.12 (admissible)   1e-6 control fires at 1.0763e-07 >= 1.0e-07
```

The model is clean. Nothing is defective. The failure is entirely round-off in
the axial state's rotational component -- the signature `tolerances.py:422-426`
already describes -- and moving only the fill-reducing permutation, which
provably cannot change the exact solution, moves it right off the cliff:

```
COLAMD (shipped)  4.4681e-13   err/ceiling 1.0630   RED
NATURAL           7.3320e-14   err/ceiling 0.1744
MMD_ATA           4.7053e-14   err/ceiling 0.1119
MMD_AT_PLUS_A     8.1740e-14   err/ceiling 0.1945
```

**6.1x of permutation spread against 1.6x of margin.** The same file documents
that spread as 2.3x-3.5x and calls it round-off; the factor `5.0` sits `1.56x`
above the lower edge of its own live band (`3.2`), and that lower edge is itself
a COLAMD realisation -- rerunning my whole-corpus scan under the other three
permutations puts the smallest admissible factor at `1.668`, `1.519` and `0.939`.
The form's operating margin against a false positive is smaller than the scatter
of the quantity it bounds. The constant does not have this failure: over the
same scan the worst clean ratio to `PATCH_TEST_EXACTNESS` is `0.447`.

That is what makes it a STOP rather than a HOLD. A rung-1 gate that reddens on a
correct element is not a conservative gate: the cheapest response to that red is
to widen the factor, and CLAUDE.md's first non-negotiable exists because that
response is the one that gets taken.
**Closed when** the floor-aware term is out of the assertion and
`PATCH_TEST_EXACTNESS` is the ceiling again, with the four breach entries
recorded as known round-off exceedances against the permutation cell -- or, if
the form is defended instead, when a clean configuration breaching it is
impossible by a stated argument and `unit_mm_D_t_100_roll_neg` is green.

**R70. (STOP-class, same form) `cond(equilibrate(K_ff))` moves 5.97x with the
FRAME, where `cond(K_ff)` is exactly frame-invariant, and it stops tracking
slenderness in one of the two orientations the gate runs.**
`floatfea/assemble/system.py:42-105`,
`tests/verification/rung1/test_patch_test.py:326-349`,
`floatfea/tolerances.py:522-545`.

Same physical beam, same section, `S = 1`, only the direction of the member in
the global frame moved:

```
orientation    cond(K_ff)      cond(K~)    ratio to axis-aligned
axis          9.20958e+02   1.05962e+02         1.000
global y      9.20958e+02   1.05962e+02         1.000
skew          9.20958e+02   3.84914e+02         3.633
45 deg xy     9.20958e+02   6.31992e+02         5.964
(1,1,1)/sq3   9.20958e+02   6.32722e+02         5.971
```

`cond(K_ff)` is identical to six digits because rotating the model is an
orthogonal congruence on the DOF and cannot move a spectrum. The equilibrated
version is not invariant under it, because the diagonal it divides by is
frame-dependent. So the property R55 bought -- invariance under a DIAGONAL change
of variables -- was paid for with the loss of invariance under an ORTHOGONAL one,
and CLAUDE.md is explicit that a frame is never assumed. Both orientations are
inside the shipped parametrisation, so this is not an exotic case.

The second claimed property goes with it. The entry publishes "it still tracks
slenderness, 121.7x over D = 0.6 .. 0.05". That is the skew column:

```
D       cond(K_ff)   cond(K~) skew   cond(K~) axis   ceiling axis
0.600   9.2096e+02     3.8491e+02     1.0596e+02     1.1764e-13
0.200   7.6312e+03     2.8587e+03     3.1768e+02     3.5270e-13
0.100   3.0283e+04     1.1480e+04     4.0386e+02     4.4837e-13
0.050   1.2090e+05     4.6838e+04     4.3388e+02     4.8171e-13
0.030   2.1200e+05     1.3102e+05     4.4092e+02     4.8952e-13
```

**4.09x over the range the entry claims 121.7x for**, and the whole axis-aligned
column is a flat number below the constant. On that half of the gate the
floor-aware term is a constant -- a tighter one -- and delivers none of the
slenderness relief it was introduced for (R46). Three new corpus entries sit on
this axis; all three hold, and that is the point.
**Closed when** the form is withdrawn per R69, or the entry states that the
floor is frame-dependent, carries this table, and says which frame each of its
published figures was taken in.

**R71. (blocking) Two of the three tables inside `PATCH_TEST_COND_FACTOR`'s
entry were measured at a factor of 8.0 and were not re-measured when commit
`71f5919` moved the factor to 5.0. Every figure in them is wrong by exactly
8/5.** `floatfea/tolerances.py:513-606` (the bound table) and `:608-624` (the
counter table). The report says "Every figure regenerated at this commit";
`git show 8217c65:floatfea/tolerances.py | grep 5.313` shows where they came
from, and the same file at that commit carries `PATCH_TEST_COND_FACTOR = 8.0`.

Published against measured at `ad2246a`:

```
                                        published    measured    ratio
worst bound over the admitted corpus      5.313x      8.500x     1.600
the posed geometry                        1.463x      2.340x     1.600
counter table, ceiling at D = 0.600     6.838e-13   4.2734e-13   0.625
counter table, worst cell               2.983e-10   1.8661e-10   0.625
```

`5.313 = 1e-12 / (8.0 * 105.96 * eps)` reproduces the old value exactly, so the
provenance is not in doubt. The consequences are not cosmetic. The bound the
entry offers as the defence of the whole form is **8.500x**, not 5.313x, and it
is reached on five admitted corpus entries -- `posed_axis`, `vertical_onode`,
`in_plane_y`, `onode_just_outside`, `vertical_onode_y` -- every one of them
axis-aligned, which is R70 arriving through a second door. And "the counter is
set just above the worst cell" is `1.61x` above it.

A third number in the same entry contradicts its own neighbour: "it sits 2.7x
above the worst measured clean ratio, 1.8754" cannot stand beside "3.0 ->
FAILED ... [unit_mm_similar]", which requires a clean ratio above 3.0. Measured,
the worst clean ratio over the corpus is **3.130**, and 5.0 sits `1.60x` above
it. `1.8754` is the gate's own `S = 1e-3` cell; the corpus is worse, and the
entry publishes the smaller of the two numbers it has.
**Closed when** the form is withdrawn per R69, or every figure in the entry is
regenerated at the shipped factor and the clean ratio quoted is the worst one
measured rather than the worst one in the gate.

**R72. (blocking) The cap that bounds the self-reference is not asserted on the
`expect=breach` branch, which is where the floor-aware ceiling is loosest. A
single-element defect of `4.4e-10` passes there.**
`tests/verification/rung1/test_corpus_configurations.py:329-339`.

The `hold` branch asserts `min(floor-aware, constant)`, so `constant /
binding_clean` bounds it and that argument is sound. The `breach` branch asserts
`worst > PATCH_TEST_EXACTNESS` **and** `worst <= _ceiling(entry)` -- the
floor-aware value alone, with nothing above it. Bisecting the largest
single-element relative stiffness defect that still passes the shipped
assertion:

```
entry                  branch   largest surviving defect   error at it
very_slender_L_r_189   breach          4.4020e-10          5.1961e-11   52x the constant
slender_L_r_118        breach          1.7165e-10          1.9960e-11   20x
slender_L_r_94         breach          1.0840e-10          1.2739e-11
posed_metre            hold            3.5669e-12          4.2726e-13
posed_axis             hold            9.7877e-13          1.1732e-13
```

**450x between the two branches**, and the entry's bound table records those
same entries as "1.000x -- no loosening at all", because it applies the min()
formula to entries whose assertion is not a min(). The bound is computed for the
branch that does not need it.
**Closed when** the form is withdrawn per R69, or the breach branch carries an
upper cap a defect cannot move and the bound table is recomputed over the branch
it describes.

**R73. (blocking) The beam admission limit refuses two configurations where the
gate's own control demonstrably fires, and the site R58 named --
`PATCH_TEST_EXACTNESS_COUNTER`'s own entry -- was left untouched, so the
counter's domain still fails on an axis the limit does not cover.**
`floatfea/tolerances.py:152-186` and `:488-509`, `docs/conventions.md` section
"Beam admission limit",
`tests/verification/rung1/test_corpus_configurations.py:186-191`.

The justification reproduces exactly. I re-ran the whole sweep with the limit
bypassed and every published figure is right to three digits:

```
L/D     0.50      1.00      1.20      1.30      1.50      2.00      3.00     16.10
resp  9.5011e-8 8.8011e-8 1.0758e-7 1.0853e-7 1.0839e-7 1.0805e-7 1.0748e-7 1.0764e-7
       FAILS     FAILS    ------------------ control fires ------------------
scale-free in D at L/D = 2: 1.0805e-07 at D = 0.1, 0.3, 1.0, 2.0 and 4.0
```

The measured boundary is between `L/D = 1.0` and `1.2`; the limit is set at
`2.0`, 1.7x above it. The report says so itself, honestly, as item 2 of what it
wants looked at hardest, and the value is declared a judgement pending Xabier.
**My adjudication: refusing the other two is not right, and the way the limit
was introduced is the recorded failure mode.** A new threshold in
`tolerances.py`, wired into the parametrisation of the failing test, in the same
commit as the red it turns green, is a parametrisation changed to make a red
test green; CLAUDE.md extends the tolerance rule to tier cutoffs in screening by
name. `stubby_thin` and `stubby_thick` at `L/D = 1.5` pass the control with 8%
of margin, and my new `stubby_L_over_D_1p3` passes with 8.5%. Only
`very_stubby_L_r_0p5` fails.

Refusing them did not close the hole R58 was about. The counter's domain fails
on **anisotropy** as well as on stubbiness: at `I_y/I_z = 500`, member
`L/D = 16.12` and fully admissible, the weakest state responds at `8.6804e-08`
against `1.0e-07` -- `aniso_I_y_500x`, red at `ad2246a`, and non-monotone, since
1000x gives `9.4675e-08`. The ratio is extreme and no real section reaches it;
the entry is evidence about an undeclared domain, not about the element. The
declared domain is what was asked for and what would have covered both axes.

Two smaller things belong here. `docs/conventions.md` is **locked at F0** and
CLAUDE.md says changing it requires reopening that gate rather than an inline
edit; the section was added inline, in a commit that also touches `floatfea/`
and `tests/`. The text anticipates the objection and offers to move, which is
the right instinct, but that is not the implementer's decision to take by
writing it down. And `member_l_over_d` derives the depth from `I_z` alone with
no shape guard: the inversion `D_o = 2 sqrt(2 I/A + A/2pi)` is exact for a
circular annulus of any wall -- I verified it to `2.2e-16` at five thicknesses
and at the solid limit -- and silently wrong for the first non-circular section,
which is the raises-never-defaults rule this repository applies to `basis.kappa`
twenty lines away.
**Closed when** the limit sits where its own measurement puts it, with
`stubby_thin`, `stubby_thick` and `stubby_L_over_D_1p3` running, or Xabier
confirms `2.0` in writing; **and** `PATCH_TEST_EXACTNESS_COUNTER`'s entry states
the geometry it was measured at, the direction it degrades in, and both
configurations now known to leave its domain; **and** `member_l_over_d` raises
for a shape it has no inversion for.

**R74. (blocking) The locked plan states a formula the code does not implement,
at the site R55 named.** `docs/milestones/F2.md:946`: "The ceiling itself is now
floor-aware -- PATCH_TEST_COND_FACTOR * cond(K_ff) * eps". The code computes
`cond(equilibrate(K_ff))`. One command:
`grep -n "cond(K_ff)" docs/milestones/F2.md`. F3 inherits D7 item 5 as a named
dependency, so a builder written from the plan would implement the form this
round replaced -- the one that moves six orders with the unit system.
**Closed when** D7 item 5 says what ships. If R69 is taken up, that is the same
edit.

**R75. (recordable) The corpus parser validates field NAMES and not field
VALUES, and the value it does not validate is the section shape.**
`tests/verification/rung1/test_corpus_configurations.py:160-162`. `_section`
splits on the first comma and reads `D` and `t`; the shape token is never looked
at, and neither is any further key. Measured at `ad2246a`, all three
bit-identical to the reference at `1.251313e-14`:

```
section=rectangle,D=0.600,t=0.01200               builds a CIRCULAR TUBE
section=circular_tube,D=0.600,t=0.01200,b=0.300   the b is dropped
a repeated `orient=` field                        silently takes the last one
```

This matters more than `typo_field_roll_rad` did. The corpus header says
`circular_tube` is "the only shape basis.kappa knows", and the `aniso_I_y` block
is explicitly waiting for a non-circular shape -- so the natural way for the next
reviewer to write that entry is `section=rectangle,...`, and it would be scored
green as a circular tube. Three new entries, all red.
**Closed when** `_parse_line` validates the shape token against the shapes
`Section` can build, refuses an unknown key inside the section spec, refuses a
repeated field, and the three entries go green by raising.

**R76. (recordable) "E is the only property in this model that scales K
uniformly" is false, and the second one is a SECTION defect -- the class this
same docstring now says the gate can see.**
`tests/verification/rung1/test_patch_test.py:57-84` and `:1052-1068`. Entrywise
`K1/K0` over the assembled matrix, with the reference held independent:

```
defect                      K1/K0 range           uniform?  held-ref worst
E x 1.5                    1.500000 .. 1.500000     YES     1.4002e-14  invisible
A, I_y, I_z, J ALL x 1.5   1.500000 .. 1.500000     YES     9.8106e-15  INVISIBLE
I_y, I_z, J x 1.5 (A held) 0.61798  .. 2.46969      no      2.9777e-03  caught
A x 1.5 (I held)           0.20452  .. 1.82738      no      2.0293e-03  caught
rho x 10                   1.000000 .. 1.000000     YES     1.2513e-14  invisible
fy x 2                     1.000000 .. 1.000000     YES     1.2513e-14  invisible
```

Scaling every stored section property by one factor is an exact scalar multiple
of K -- the shear parameter is invariant because I and A move together -- and
such a `Section` passes `__post_init__` unchanged, since `J = I_y + I_z`
survives the scaling. So a consistent scale error on a section table is
invisible to G2.2, and the docstring now tells a reader the opposite. `rho` and
`fy` are the trivial other direction: "a uniform scalar factor on K, and nothing
wider" is also wrong about every property that does not enter K at all.
**Closed when** the sentence names the class rather than the property -- any
defect that multiplies K by a scalar, of which a uniform E error and a uniform
scaling of all section properties are two -- with the entrywise cell beside it.

**R77. (recordable) `test_the_corpus_coverage_is_reported`'s replacement
assertion is a tautology, like the one it replaced. Fifth guard, same test, two
rounds running.**
`tests/verification/rung1/test_corpus_configurations.py:386-398`. `solved` is
`A and B and C`; `refused` is `(not A) or (not B) or (not C)`. They are exact
complements, so `solved & refused` is empty and `solved | refused` is everything,
for every possible corpus including an empty one. I enumerated all eight
combinations of the three predicates: **0 of 8** put an entry in both sets or in
neither. R62's closing condition named a different property -- that every id the
reviewer recorded `runs_in_suite=yes` is among the ids this module parametrised
-- which compares two independently sourced sets and can fail.
**Closed when** the assertion compares the reviewer's recorded set against the
parametrised set, and a deliberately wrong `runs_in_suite` in my file reddens it.

**R78. (recordable) Reading-order item 4b. Two of the three hook holes are
closed and I verified both by exercising them; the third is reported closed and
is open.** `git diff 25b2dcb..HEAD -- .claude docs/SUPERVISOR.md` touches
`protect-reviews.sh` and `settings.json` in **one standalone `process:` commit**
(`7c60eed`) citing BH5 and touching no `floatfea/` and no `tests/`.
`docs/SUPERVISOR.md` is unchanged. Checked mechanically over all nine commits:
**no commit touches both `.claude/` and code; none touches `docs/reviews/` or
`tests/corpus/` at all.** No guard was removed -- the diff is additive plus one
per-segment rule replaced by a whole-command rule, which is strictly stricter.
Exercised on ten synthetic inputs at `ad2246a`:

```
implementer `cd tests/corpus && echo x > y.txt`      DENIED   (hole 1 closed)
malformed stdin JSON                                 DENIED   (hole 2 closed)
NotebookEdit, notebook_path under tests/corpus/      ALLOWED  (hole 3 OPEN)
implementer Write to docs/reviews/                   DENIED
supervisor Write to docs/reviews/                    allowed
supervisor `cd tests/corpus && echo x > y.txt`       allowed
implementer cat / git diff on those paths            allowed
implementer python -c open(...,'w') on tests/corpus  ALLOWED  (declared limit)
```

`NotebookEdit` was added to the matcher in `settings.json`, and the path
extraction reads `file_path` or `path` -- never `notebook_path`. The hook now
runs for that tool and sees no path. The header says "3. NotebookEdit was not in
the matcher. Closed in settings.json." That is a claim about the code with no
command behind it (BF0), on the one file whose failure mode is that nobody
checks it. Accepted as non-blocking: the exposure is one exotic tool, my verdict
path is intact, and I confirmed I can still write both `docs/reviews/` and
`tests/corpus/`.
**Closed when** the extractor reads `notebook_path`, demonstrated on the input
above.

**R79. (recordable) `Section.circular_tube` labels every wall thickness
`thin_tube` and therefore draws the thin-wall-limit shear coefficient for a
section of any thickness. At `D/t = 5` -- a configuration already in this corpus
-- `kappa` is 8.9% wrong; at the constructor's own admissible limit it is 40%
wrong.** `floatfea/model/material.py:120-140`, `floatfea/basis.py:102-118`.
Cowper's hollow-circle coefficient, verified against this repository's own two
endpoints (it returns `0.530612` as `Ri/Ro -> 1` and `0.886364` at `Ri/Ro = 0`,
both to the last digit of `basis.kappa`):

```
D/t      200      50      20      10       5       3      2.07
Cowper 0.53063 0.53097 0.53297 0.54108 0.58238 0.71402 0.88366
shipped 0.53061 at every one
error  -0.00%  -0.07%  -0.44%  -1.93%  -8.89% -25.69% -39.95%
```

`basis.kappa` refuses an unknown shape rather than defaulting, and the reason
given there is that a wrong kappa makes an element and its verification
reference two different beams -- but the constructor upstream of it assigns the
shape from nothing, so the guard never sees the case. G2.2 is documented blind
to a uniform kappa error, so nothing in rung 1 can catch this; V2.2 could.
Pre-existing, not introduced this step, and outside G2.2's own claim -- recorded
because my corpus now contains two entries (`thick_wall_D_t_5`,
`nearly_solid_D_t_2p1`) that run it.
**Closed when** `circular_tube` either refuses a wall outside the thin-wall
range or selects the shape from the radius ratio, or `basis.py` records the ratio
at which the thin-wall coefficient stops being defensible and
`docs/verification/` carries it as a limitation.

**R80. (recordable) Two decision thresholds were added OUTSIDE
`floatfea/tolerances.py` and both can be weakened to nothing in silence.**
`tests/verification/rung1/test_patch_test.py:1082-1085` --
`NON_SCALAR_ERRORS = [("nu ...", "nu", 0.45, 1.0e-4), ("section x 1.5",
"section", 1.5, 1.0e-3)]`. These are discrimination floors on a shipped negative
control, the same species as `PATCH_TEST_EXACTNESS_COUNTER`, which lives in
`tolerances.py`. Measured: set both to `1.0e-30` and the suite is **426 passed**
(the corpus module excluded, since my own file was uncommitted at that moment)
with the tolerance-literal scanner silent, because the scanner reads `assert`
lines and these values sit in a module-level table. CLAUDE.md: "no exceptions, no
local literals". The `# not-a-tolerance:` marker sits on the assert line; the
number it excuses is thirty lines away.
**Closed when** both move to `tolerances.py` as counters with their measured
bases, or the scanner reaches parametrisation tables and the marker sits on the
value it excuses.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `BEAM_ADMISSION_L_OVER_D` | -- | `2.0` | dimensionless: member length over a derived outer diameter. STRUCTURAL, so no counter-case is required (AO2) | none, correctly | `tolerances.py:152-186` and `docs/conventions.md` "Beam admission limit". The measurement reproduces exactly -- I re-ran the whole `L/D` sweep with the limit bypassed and every published figure is right to three digits, including the scale-freeness in `D`. **The value is 1.7x above what that measurement supports** (the control fails only below `L/D ~ 1.2`); it is declared a judgement pending Xabier; and it was introduced in the same commit as the red it turns green, while refusing two configurations that pass. **R73.** The depth inversion is exact for a circular annulus (`2.2e-16` at five wall thicknesses and at the solid limit) and unguarded for anything else. |
| `PATCH_TEST_COND_FACTOR` | `4.0` on `cond(K_ff)` | `5.0` on `cond(equilibrate(K_ff))` | dimensionless multiplier on a conditioning estimate times `eps`; the ceiling it forms is relative and dimensionless | `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT = 3.0e-10`, injected by `test_the_floor_aware_ceiling_CATCHES_its_counter_defect` over four sections | `tolerances.py:513-606`. **The form is the STOP.** The quantity changed rather than the value, so this is not a widening of the old entry, and the unit invariance is real and exact (`3.84914e+02` at all three scales, spread `1.000000x`). But a clean admissible model breaches it at `1.063x` (**R69**); it moves `5.97x` with the frame and its slenderness tracking is `4.09x` rather than the published `121.7x` in the axis-aligned half of the gate (**R70**); and two of its three tables are stale by exactly `8/5` (**R71**). The band reproduces: `3.0` reddens, `3.2`-`8.0` pass, `8.2` reddens -- and that lower edge is a COLAMD realisation that moves to `0.94` under MMD_AT_PLUS_A. |
| `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT` | `4.0e-10` | `3.0e-10` | defect size, relative, dimensionless | -- | `tolerances.py:608-624`. **Tightened, not loosened** -- the assertion is that the defect is caught, so a smaller counter is a stricter control, and I confirmed the guard bites: `PATCH_TEST_COND_FACTOR -> 8.2` reddens `[D=0.08]`. The per-state table is stale at every cell: measured at `ad2246a` the worst cell is `1.8661e-10`, not `2.983e-10`, so the counter sits `1.61x` above the worst cell rather than just above it (**R71**). |
| everything else | -- | unchanged | -- | -- | `git diff -U0 25b2dcb..HEAD -- floatfea/tolerances.py` filtered to `Final[float]` gives one addition and one modified pair, and nothing else. **No accuracy ceiling was widened in either direction.** I re-ran the R63 mutations to confirm the three unguarded ceilings are unguarded for the same reason as last round rather than a new one. |

Two decision thresholds were added **outside** the file, in a parametrisation
table, and are weakenable to `1e-30` in silence: **R80**. No golden file moved.
No test is skipped or `xfail`ed; the suite has zero skips.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin, **and neither does another
revision of step 4 that keeps the present form.** This is a STOP: the plan
reopens at `F2.md` D7 item 5 and the form is settled there, not inside another
step commit.

1. **R69, R70, R71, R72 -- the form.** The instruction for this round was that a
   defect in the form ends the elaboration. Return the assertion to
   `PATCH_TEST_EXACTNESS` alone; record `slender_L_r_79`, `_94`, `_118` and
   `very_slender_L_r_189` as known round-off exceedances, with the permutation
   cell at `tolerances.py:406-420` as the evidence and the four measured values
   written down; delete `PATCH_TEST_COND_FACTOR` and its counter, or demote them
   to a REPORTED diagnostic that nothing asserts. If the form is defended
   instead, it is defended against R69 first -- a clean model it refuses -- and
   nothing else in step 4 is worth reading until that is answered.
2. **R73 -- the admission limit and the counter's domain.** Both halves, at the
   two sites named, or the limit moves to where its own measurement puts it.
3. **R74 -- `F2.md` D7 item 5 states the ceiling the code implements.** That is
   the plan edit this STOP reopens; make it there, not in a step commit.
4. **R75 -- the parser validates the section spec**, and the three new corpus
   entries go green by raising.

R76 through R80, together with R6, R16, R25, R30 (recorded answered), R31, R32,
R33 (outside G2.2), R36, R50, R52, R62 and R63 (carried unanswered as R77 and as
item 9 of Carried), and R65, may be answered in the next report's `Carried`
section, **and that section must list every one of them, open or answered.**
Revision 8 listed all of them, and that is the standard now.

**Adversarial corpus (BE3): 14 new entries, all unseen by the implementer; 9
caught, 5 red.** `tests/corpus/g22_model_configurations.txt`, now 50 entries,
committed separately in the commit immediately before this verdict, touching no
code. The 14 are the axes this round created or left open: the **frame axis** --
three slender entries in the axis-aligned and `in_plane_y` orientations, which is
how R70 is expressible in the schema that exists; the **unit-times-roll corner**
where the floor-aware ceiling refuses a clean model (R69, one red and two near
misses at `0.53` of their ceilings); the **section spec's own value** (three red,
R75); the **admission limit at both sides of its boundary**, plus one entry at
`L/D = 1.3` where the control demonstrably fires and the member is refused
anyway (R73); and **two entries on section physics nothing checks** (R79, and
`aniso_I_y_500x` red on the negative control, R73). Full suite with the corpus
applied: **5 failed, 520 passed**.

That 9-of-14 is the coverage measurement for this round, and it is a worse number
than last round's 17-of-19 for a reason worth stating: the six entries that
exercise machinery written *this* round -- the parser's section spec and the
admission limit's boundary -- found four defects, while the eight that exercise
the element found one, and that one is a defect in the ceiling rather than in the
element. **Nine consecutive rounds have found no element defect.** Every finding
in this verdict is in a check, a comment, a threshold or a plan line. Per the
guard, that means "not yet contradicted", and it stays that way until V5.1 puts
CalculiX on the other side.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Eight
consecutive reviews by one reader.

**The pattern, eighth round.** The seventh verdict asked: for every ratio and
every span in this diff, which axis was it measured along, and what does it do
along the other one? The answer is that the form was moved off the unit axis onto
the frame axis, where nobody had looked, and that the numbers describing it were
carried across a change in the very factor they were computed from. Both are the
failure the last four rounds have found. The reason to stop elaborating is not
that the implementer keeps missing an axis -- the work each round has been
careful and the corrections have been real. It is that **a ceiling computed from
the matrix under test has one more axis than anyone can enumerate**, and the
constant it replaced has none. The standing question for whatever comes next:
*if this check went red tomorrow, what is the cheapest way to make it green, and
is that thing a tolerance?*
