# Review — F2 step 4
Reviewed commit: 83b2de2d935c484564750bb3126259b853f3f448
Verdict: HOLD
Tests: 459 passed, 0 failed, 0 skipped   (my run at 83b2de2, `python -m pytest -q`, 1.70s)

Seventh pass. Reviewed range `d426e48..83b2de2`, nine commits, four of them
`process:`/`plan:` commits touching no code. My own corpus grew by **19 entries**
this round (`tests/corpus/`, now 36), committed separately immediately before
this verdict; the coverage number is at the end.

**The BG6 hook works.** `agent_type == "gating-supervisor"` is the right string --
I was not denied, and I exercised the hook from both sides before relying on it
(R66 below). The report's item 3 of "what I want looked at hardest" is answered:
the assumption held.

**All four gated items are answered and I verified each by re-running it, not by
reading it.** R45: `backward_error` replaces the load-normalised residual, runs
at all three scales, worst clean cell `1.0343e-16 = 0.466 eps` -- the entry's
figure to five digits. R46: the `L/r = 119` boundary is gone from `tolerances.py`
and from `F2.md`; **I reproduced the permutation cell independently and the
inference is sound** -- COLAMD/NATURAL/MMD_ATA/MMD_AT_PLUS_A move the worst error
2.27x-3.51x and swap which component is worst, on a change that provably cannot
move the exact solution, so the three breaches are round-off and there is no
element defect down the slenderness axis. R47: both sites now carry the inverted
thresholds. R48: `RESULTANT_EXACTNESS 1e-9 -> 1e-8` now gives **6 failed**, and
`-> 1e-7` gives 6 failed where last round it gave `366 passed`. **I widened every
ACCURACY ceiling in the file**; the four in this step's scope all redden.

It is a HOLD because **the floor-aware ceiling is presented as the more robust
form on a measurement taken along one axis, and along the other axis the gate is
actually parametrised over -- the unit system -- it is five to six orders looser
than the constant it is offered in place of**; because the self-reference
measurement that licenses it was taken against three defects its own author
chose, and the defect class this same step declares invisible inflates the
ceiling 65x; because the corpus runner states an anti-vacuity property it does
not have; and because a stubby configuration inside the claimed domain makes a
shipped negative control fail, which reverses a withdrawal I made last round.

**Not a STOP, and I want the reason on the record.** No rung is red, no element
defect was found, no existing value moved (four `+` and two `-` `Final[float]`
lines, no modifications), and **nothing the repository previously rejected is now
accepted**: `test_the_six_constant_strain_states_are_EXACT` asserts the constant
`PATCH_TEST_EXACTNESS` *and* the floor-aware ceiling, and at the posed geometry
the floor-aware one is the tighter of the two (`8.1797e-13` against `1e-12`), so
it binds rather than relaxes. The loosening is potential, not realised: it lives
in the corpus module, where only the floor-aware ceiling is asserted, and in
`F2.md` D7 item 5, which now hands F3 that criterion. That is a HOLD-sized
finding, and I am not inflating it into a STOP.

## Carried

Every item from the sixth verdict (`HOLD @ 15bbc3b`, committed `d426e48`), traced
through `d426e48..83b2de2` and re-measured.

- **1. R45 (gated) -- ANSWERED, and I re-ran both halves.** `10b62fd`.
  `SolveResult` gains `backward_error` (`system.py:216-224`);
  `test_the_solve_is_BACKWARD_STABLE` is parametrised over `GATE_UNIT_SCALES`
  (36 nodes). My own run over all 18 cells: worst clean backward error
  **`1.0343e-16` = `0.466 eps`**, matching the entry. The conditioning story is
  withdrawn at both sites and replaced by the cell. The claim that the new
  counter is **weaker** than the old one is stated (`test_patch_test.py:800-806`,
  `tolerances.py:591-599`) rather than hidden, and I measured how much weaker by
  inverting the shipped predicate per cell -- see **R60**, where the number is
  missing from the entry that promises it.
- **2. R46 (gated) -- ANSWERED in the half that was wrong, and the inference is
  verified.** `c43e12a`, `9dbfcb4`, `0fe14c3`. The boundary sentence is gone; the
  block now says "THERE IS NO BOUNDARY". The permutation cell reproduces through
  my own harness (my NATURAL at `D = 0.600` is `8.237e-15` against the entry's
  `7.97e-15`, 3%; every other cell to three digits) and the conclusion is right:
  at `D = 0.12` only COLAMD breaches, at `D = 0.080` only COLAMD and NATURAL. The
  member-vs-element `lambda` conflation is fixed, and the 4.4x cross-source
  discrepancy at element `L/r = 46.40` is **recorded rather than averaged**,
  which is the right handling. The replacement form is **R55/R56/R64**.
- **3. R47 (gated) -- ANSWERED.** `9dbfcb4`. "6.4x the more sensitive" is deleted
  from `tolerances.py` and from `F2.md` D5; both now carry the inverted table and
  the words "~150x WEAKER". The table reproduces: I re-measured
  `via field 8.45e-12 .. 9.30e-12` against `via resultants 1.25e-09 .. 1.45e-09`.
  The reason for keeping the channel is now the one the measurements support, and
  it carries R53's caveat against itself.
- **4. R48 (gated) -- ANSWERED, and I re-ran the mutation that found it.**
  `9dbfcb4`. The guard is `test_the_RESULTANT_detection_threshold_still_holds`,
  the form the sixth verdict named, with the inverted numbers in the entry.
  **680x of free travel is now about 5%.** The `X_COUNTER_DEFECT` protocol is a
  real addition; see **R63** for the four entries it does not reach.
- **5. R49 (recordable) -- ANSWERED by removal.** The `SOLVE_RESIDUAL` pair is
  gone with the quantity, so the perturbation-size-as-counter contract went with
  it, and the new `_COUNTER_DEFECT` suffix says what it is. Superseded by R60.
- **6. R50 (recordable) -- NOT ANSWERED, correctly declared.** The report says so
  in one line. The three stale figures are in revision 6's prose, which is now
  historical text in an append-only file. Carried; low value.
- **7. R51 (recordable) -- ANSWERED** at `73f4edc`, last round.
  `test_patch_test.py:1` now reads "SIX constant-strain states".
- **8. R52 (recordable) -- NOT ANSWERED, and it got worse.** The stale opening
  paragraph at `tolerances.py:409-414` is unchanged, and the missing operating
  point is now a measured failure rather than a wording point: see **R58**.
- **9. R53 (recordable) -- ANSWERED, and I re-ran the mutation.** `aead308`.
  `section.I_y -> section.I_z` at `beam.py:73` now gives **2 failed**
  (the corpus node `aniso_I_y_2x` and one transform node); at `:152`, **1
  failed** (`test_the_xz_bending_block_uses_I_y_and_the_xy_block_uses_I_z`); both
  at once, 2 failed. Last round all three mutations gave `366 passed`. The
  expectation is computed from Przemieniecki 5.36 rather than from
  `shear_parameter`, which the report records as the correction that made the
  second site redden -- I confirmed the `:152` site is caught only by that test.
  The AW3 bypass is labelled, fenced by a test that the type still refuses the
  object, and carries its own deletion condition.
- **10. R54 (recordable) -- ANSWERED, and it produced the round's best process
  result.** `aead308`. The corpus runs. The report's own note is the valuable
  part: `vertical_no_onode` did not raise on the first attempt because the
  builder never reached `rotation_matrix`, so `expect=raise` was passing by not
  looking -- the tenth guard caught inside the step. `_build` now calls the guard
  explicitly (`test_corpus_configurations.py:109-110`). I verified the runner can
  fail: flipping `slender_L_r_86` from `hold` to `breach` in my own file gives
  `1 failed, 34 passed` at `:191`.
- **11. R6 -- still open.** `pin_threads` is called only from
  `tests/verification/rung3/test_determinism_pins.py`. Unchanged. Step 5's.
- **12. R16 -- still open**, correctly unchanged. `equilibrate` takes `abs()` of
  the diagonal; a note for step 12.
- **13. R30 -- ANSWERED.** Its four dead counters were surfaced by
  `test_every_accuracy_entry_has_a_counter_that_something_INJECTS` and all four
  now have injections. Two of the four injections **refuted the entry they were
  written for**, which is the strongest thing in this diff.
- **14. R25, R31, R32, R33 (outside G2.2), R36 -- still open**, in step 4a,
  unchanged, and correctly unchanged: nothing in `F2a.md` is built.
  **Revision 7's `Carried` section does not list R6, R16, R25, R31, R32, R33 or
  R36 at all** -- a `grep` for each over the revision-7 text returns 0. The sixth
  verdict put that obligation on step 5's report, so it is not yet late; it is
  recorded here as **R68** so it is not lost.

## Findings

**R55. (blocking) The floor-aware ceiling is not unit-invariant. `cond(K_ff)`
moves by 6.5 orders across the three unit systems the gate is itself
parametrised over, and the ceiling and its detection threshold move with it -- so
the form offered as "scaling with the problem posed" scales with the choice of
units by more than it scales with anything physical. The unit-invariant version
of the same quantity is already in this repository.**
`floatfea/tolerances.py:477-523`, `tests/verification/rung1/test_patch_test.py:344-353`.

The entry's case for the new form is measured along slenderness at metre scale:
`err/1e-12` spans 141x and crosses 1 three times, `err/(cond*eps)` spans 8x and
never reaches 1. Both halves of that are true and I reproduced them. The gate
runs over *two* axes, though, and the second one was not measured. Holding the
geometry fixed and moving only the unit scale:

```
scale  cond(K_ff)   cond(equilibrate(K_ff))  ceiling=4*cond*eps  worst err   err/ceiling
1e-3   5.9831e+08         3.8491e+02             5.3140e-07      1.6029e-13   3.02e-07
1      9.2096e+02         3.8491e+02             8.1797e-13      1.2513e-14   1.53e-02
1e+3   4.0490e+07         3.8491e+02             3.5962e-08      4.9240e-14   1.37e-06
```

`err/(cond*eps)` therefore spans **five orders** along the unit axis, against the
8x the entry publishes along the slenderness axis. Inverting each shipped
predicate -- the smallest single-element relative stiffness defect each one
detects, per scale:

```
scale     floor-aware detects     the constant detects
1e-3          4.5254e-06               8.3237e-12
1             6.8611e-12               8.4405e-12
1e+3          3.0625e-07               8.3867e-12
```

**As a gate the floor-aware form is 5.4e5x weaker at millimetres and 3.6e4x
weaker at kilometres**, while the constant it is offered as an improvement on is
unit-invariant to 1.4% across the same three scales. This is the ninth guard, and
it is the same failure R45 has just finished correcting -- a ratio against a
denominator that varies by orders -- reappearing in the ceiling written in the
same commit range to answer R46.

Nothing is hidden by it today, because the gate asserts both and the constant
binds. Two places make it matter anyway: `test_corpus_configurations.py:203`
asserts **only** the floor-aware ceiling on `expect=hold` entries, and `F2.md`
D7 item 5 now writes it into the locked plan as F3's criterion -- "a slender
configuration is judged against the accuracy its own conditioning permits rather
than against a constant".

The fix is one call and it is already in `floatfea/assemble/system.py`.
`cond(equilibrate(K_ff))` is `3.8491e+02` **at all three scales to five digits**
-- `COND_UNIT_INVARIANCE` is the tolerance that asserts exactly this property --
and it still carries the slenderness dependence the new form was introduced for:

```
 D      L/r     cond(K_ff)   cond(K~)   err/(4*cond*eps)  err/(4*cond~*eps)
0.600   15.7    9.2096e+02   3.8491e+02     0.0153             0.0366
0.200   47.2    7.6312e+03   2.8587e+03     0.0232             0.0619
0.120   78.6    2.1054e+04   7.9293e+03     0.0540             0.1435
0.100   94.4    3.0283e+04   1.1480e+04     0.0655             0.1728
0.080  117.9    4.7272e+04   1.8070e+04     0.0245             0.0640
```

`cond(K~)` moves 47x over the same range and the ratio spans the same 8x, so the
equilibrated form has **both** properties: it scales with slenderness and it does
not scale with the unit system. At the posed geometry it gives
`4*384.91*eps = 3.42e-13`, tighter than both the current `8.18e-13` and the
constant, so it would bind everywhere rather than at one scale.
**Closed when** either (a) the entry, the helper docstring and `F2.md` D7 item 5
state the domain -- metre scale, and the constant asserted beside it wherever the
floor-aware form is asserted -- with the three-scale table above written down; or
(b) the ceiling moves to `cond(equilibrate(K_ff))` and `PATCH_TEST_COND_FACTOR`
is re-derived against it. Either way `test_corpus_configurations.py` asserts the
constant too on the entries where it holds, which is **all thirteen** current
`expect=hold` entries -- worst ratio `0.4638` (`slender_L_r_99`), eleven of the
thirteen below `0.24`. Asserting only the looser of two available ceilings on
configurations where the tighter one demonstrably holds is a weakening with no
measurement behind it.

**R56. (blocking) "The ceiling moves by at most 1.13x under any defect the gate
must catch" is measured against three defects its own author chose, and the
defect class this same step declares invisible moves it 65x.**
`floatfea/tolerances.py:511-521`.

The entry raises the right question -- the ceiling is computed from the same
matrix the gate tests, so a defect could raise its own ceiling -- and then answers
it with `1e-6 defect`, `2x defect`, `transposed R`: three non-uniform defects,
all of which barely touch `cond`. That is BE3's failure in one paragraph, and the
corpus had nothing on it because I did not know to write it.

The lever on `cond(K_ff)` is the **uniform** property error, which is exactly the
class `test_a_UNIFORM_property_error_is_invisible_to_this_gate` and the new
"BLIND to" docstring assert the gate cannot see. Holding everything else fixed
and scaling the torsion constant uniformly:

```
J factor  cond(K_ff)   ceiling      clean err   floor-aware detects  constant detects
1         9.2096e+02   8.1797e-13   1.251e-14      6.8611e-12           8.4405e-12
1e-2      5.9831e+04   5.3140e-11   2.874e-13      4.5240e-10           8.3195e-12
```

A uniform torsional error of a factor 100 -- the size of the difference between
the open- and closed-section torsion constants for a thin tube, i.e. a plausible
real defect -- leaves the clean error at `2.874e-13`, **invisible to both
ceilings**, while raising the floor-aware ceiling 65x and weakening its detection
of an *unrelated* single-element defect from `6.86e-12` to `4.52e-10`, **66x**.
The constant's threshold moves by 1.4%.

`J` itself is fenced: `Section.__post_init__` requires `J == I_y + I_z`, so that
exact route is closed -- good, and I checked it. The **reachable** version is the
area, which `__post_init__` checks only for positivity: `A x 1e-3` gives
`cond 4.2496e+03` (4.6x), ceiling `3.7744e-12`, clean error `1.544e-15`
(invisible), and the floor-aware detection threshold `3.4592e-11` -- 5.0x weaker.
Smaller than the `J` figure, in the same direction, from a defect the type system
permits.

**Closed when** the sentence is bounded to what was measured ("under the three
counter-cases below") and the entry names the class that moves it -- a uniform
property error, which is the class the gate beside it is blind to -- with one of
the two cells above. The two facts were established in the same step, in the same
file, and were never put next to each other.

**R57. (blocking) The corpus runner states the anti-vacuity property it does not
have. An entry naming a field it cannot build is silently ignored, and the result
is bit-identical to the entry without it.**
`tests/verification/rung1/test_corpus_configurations.py:26-28` -- "An entry naming
a field this module cannot build is a FAILURE, not a skip: a corpus entry that
silently does nothing is the vacuous-parameter failure AM5 named." Measured at
`83b2de2`, through the module's own helpers:

```
extra=none                     1.251313e-14   (reference)
extra=roll=1.0                 2.463560e-14   honoured
extra=orientation_node=5,0,0   1.287764e-14   honoured
extra=roll_rad=1.0             1.251313e-14   BIT-IDENTICAL to the reference
extra=nonsense=3.0             1.251313e-14   BIT-IDENTICAL
extra=temperature=300          1.251313e-14   BIT-IDENTICAL
unit_scale=0.001 (top level)   1.251313e-14   BIT-IDENTICAL
```

`_build`'s if/elif chain at `:91-99` has no `else: raise`, and `_parse` accepts
any key. This matters more here than in an ordinary module: the corpus and the
runner have **different authors by construction**, so a field-name mismatch is
not an exotic failure, it is the expected one -- and it reads green while the
entry checks nothing. It is the tenth guard, failing in the code written to
honour it. `tests/corpus/g22_model_configurations.txt` now carries
`typo_field_roll_rad` (`extra=roll_rad=1.0`, `expect=raise`), which is **red at
83b2de2** and is the executable form of this finding.
**Closed when** `_build` raises on any `extra=` prefix and any top-level key it
does not honour, and `typo_field_roll_rad` goes green by raising.

**R58. (blocking) A shipped negative control FAILS on a stubby configuration
inside the domain `PATCH_TEST_EXACTNESS_COUNTER` is claimed over -- and my own
withdrawal of R15 last round was premature.**
`floatfea/tolerances.py:409-431`, `test_corpus_configurations.py:216`.

R15 recorded that on a stubby configuration the six responses to the `1e-6`
single-element control fall below `PATCH_TEST_EXACTNESS_COUNTER = 1.0e-7`. The
sixth verdict -- mine -- withdrew it **on measurement**: at `D = 2.0 m`,
`t = 0.040`, `L = 3.0 m` the responses are `1.0839e-07 .. 1.4062e-07`, all above
the counter. That measurement was right and the withdrawal was wrong, because it
sampled one point on the stubby axis. At the **same section** with `L = 1.0 m`
the weakest state's response is `9.5011e-08`, against `1.0e-7`.

**The control does not fire.** `test_the_corpus_entry_still_DETECTS_a_defect
[very_stubby_L_r_0p5]` is red at `83b2de2`, and it is red for the reason R15
gave: the counter is a property of the posed mesh and the posed section, and its
entry says so nowhere. This is R52's second half -- the operating point -- turned
from a wording note into a measured failure of a shipped assertion. The counter
value itself is fine; what is missing is the domain it is a counter over.
**Closed when** `PATCH_TEST_EXACTNESS_COUNTER`'s entry states the geometry it was
measured at and the direction it degrades in (stockier members respond less), and
`very_stubby_L_r_0p5` is either green or named in that entry as a known-uncovered
configuration. I withdraw the sixth verdict's withdrawal of R15; the finding
stands and was mine to get wrong.

**R59. (recordable) The uniform-blindness docstring gives the wrong cause for two
of the three cases it parametrises, and the cause it gives is the more alarming
of the two.** `tests/verification/rung1/test_patch_test.py:57-84` and
`:1000-1013`; the report calls it "the round's most useful finding". The stated
mechanism is "the interior nodes depend on the RATIOS of element stiffnesses and
a uniform factor cancels exactly", strengthened to "even an independent reference
would not change the conclusion, because `E` and the section are drawn
independently and are equally invisible."

Two cells. First, is each change a uniform scalar factor on `K`? Entrywise
`K1/K0` over the assembled matrix:

```
E x 2               2.0000 .. 2.0000     UNIFORM
nu 0.30 -> 0.45     0.6667 .. 1.1420     NOT uniform
section x 1.5      -0.7380 .. 10.8553    NOT uniform
```

Second, hold the exact-field reference at the original properties -- one variable
moved, the element's properties; everything else held:

```
uniform change      reference MOVES (shipped)   reference HELD
E x 2                     1.2513e-14              1.2513e-14
nu 0.30 -> 0.45           3.3044e-14              5.5281e-04
section x 1.5             9.7418e-15              7.3011e-03
```

Only `E` is invisible for the stated reason. `nu` and the section are invisible
because `_exact_local` draws them from the same objects the element does
(`_section_material` returns the module's own `SEC`/`S355`), which is precisely
the mechanism R44 identified for `kappa` and which this docstring says is not
needed. Held independent, both are caught eight and nine orders above the
ceiling. **The docstring generalises the blindness wider than it is, in the
unsafe direction**: a reader concludes G2.2 says nothing about any property,
whereas a code defect that computes `G` or a section property wrongly -- a defect
that does *not* move the test's reference -- is caught at `5.5e-04`. Asserting a
blindness is the right call; asserting it with the wrong cause is what makes it
grow.
**Closed when** the docstring separates the two mechanisms: a uniform scalar
multiple of `K` is invisible unconditionally (`E`), and a non-scalar uniform
property error is invisible only because the reference shares the source, with
the held-reference numbers above. This is BG0 applied to the sentence BG0 was
written for.

**R60. (recordable) `SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT`'s entry promises
a per-cell bisection and prints no numbers. Its table's two rows say "see below",
and below is a sentence.** `floatfea/tolerances.py:587-600`. The entry says the
counter is "measured by bisection on the shipped predicate, per cell -- and it is
strongly configuration-dependent, which is the cost of this normalisation and is
recorded rather than buried", then gives two rows naming the worst and best cell
with no value against either, and "see below" resolves to nothing. Inverting the
shipped predicate myself, per cell -- smallest relative solution error detected:

```
state         S=1e-3      S=1         S=1e3
axial         1.033e-14   1.010e-14   6.701e-10
curvature     2.226e-11   6.073e-14   6.502e-12
twist         2.528e-07   2.539e-13   2.254e-14
shear         2.015e-11   6.473e-14   7.173e-12
curvature_xz  2.226e-11   6.029e-14   6.502e-12
shear_xz      2.014e-11   6.428e-14   7.173e-12
```

Worst `2.528e-07` (twist at `S = 1e-3`, exactly the cell named), best
`1.010e-14` (axial at `S = 1`, also as named) -- a spread of **seven orders**,
and the counter `1.0e-6` sits `4.0x` above the worst, which is tight and correct.
The qualitative statement is right; the numbers that would let a reader check it
are absent. The measure it replaces detected at `~1e-12`, so "the cost" is a
factor of `2.5e5` at the worst cell and the entry never says so.
**Closed when** the two named cells carry their measured values.

**R61. (recordable) `residual` is documented "Reported, not gated" and is gated in
two places, against a tolerance belonging to a different quantity.**
`floatfea/assemble/system.py:110-114` -- added this step -- says "Reported, not
gated. Its denominator is a property of the LOAD ... so a ceiling on it is a
ceiling on the load case rather than on the solve (R45)." One command:
`grep -rn '\.residual' tests/` gives `tests/unit/test_assembly_and_solve.py:133`
(`assert r.residual < TRANSFORM_INVARIANCE`) and `:197` (the same). It is gated,
and against `TRANSFORM_INVARIANCE = 1e-11`, the transform-invariance ceiling
rather than a solve ceiling. Both sites predate this step; the sentence does not.
**Closed when** the docstring says where it is still asserted, or those two sites
move to `backward_error`.

**R62. (recordable) `test_the_corpus_coverage_is_reported`'s assertion cannot
fail.** `tests/verification/rung1/test_corpus_configurations.py:231`:
`assert runs > recorded or recorded == runs`. `recorded` counts entries of the
same list carrying `runs_in_suite=yes`, so `recorded <= runs` identically and the
disjunction reduces to `runs >= recorded` -- true for every possible corpus,
including an empty one. The printed number is genuinely useful; the assertion
beside it certifies nothing. Fifth guard.
**Closed when** it asserts something that can be false -- that every id the
reviewer recorded as `runs_in_suite=yes` is among the ids this module
parametrised, which is set membership rather than a count comparison.

**R63. (recordable) Four ACCURACY ceilings can still be widened in silence. The
new rung-3 test checks that a counter is NAMED, which is not the property R48 was
about.** Measured, each mutation alone, whole suite:

```
PANEL_RECONSTRUCTION_RESIDUAL  1e-12 -> 1e-6   459 passed   (1e6 x)
MATRIX_SYMMETRY                1e-9  -> 1e-4   459 passed   (1e5 x)
ROUNDOFF_IDENTITY              1e-14 -> 1e-9   459 passed   (1e5 x)
COND_UNIT_INVARIANCE           1e-6  -> 1e-4   459 passed   (1e2 x)
```

Each still satisfies `ceiling < counter`, and each now has an injection test --
but the injections assert the *counter is reachable* (`asym >= COUNTER`,
`deviation >= COUNTER`, `drift >= COUNTER`), which is a statement about the
defect, not about the ceiling's magnitude. That is a real and useful addition and
it corrected two false bases; it is not the guard R48 named. The two entries that
did get that guard redden at 5% and 10%.
**Closed when** the three in this step's scope carry a detection-threshold test in
the shape of `test_the_RESULTANT_detection_threshold_still_holds`, or
`tolerances.py` records which ACCURACY entries are unguarded and why, so the next
reader is not told the protocol is complete. `PANEL_RECONSTRUCTION_RESIDUAL` is
F1's and is listed for completeness only.

**R64. (recordable) `PATCH_TEST_COND_FACTOR = 4.0` sits at 91% of the top of its
own live band, and the measurements support 1.0.** Inverting the decision rule on
the shipped suite:

```
4.0 -> 4.4   1 failed (counter test, D=0.08)          upper bound ~4.4
4.0 -> 3.5   459 passed
4.0 -> 1.0   459 passed
4.0 -> 0.3   459 passed
4.0 -> 0.2   4 failed (counter test, D=0.12, D=0.1)   lower bound ~0.3
```

Live band `[0.3, 4.4]`, 15x wide, with `4.0` at the loosest end. The entry's two
stated reasons are both about the *upper* end -- it must stay under `4.89`, where
it would equal the constant, and it sits 15x above the worst measured ratio.
Neither is an argument for `4.0` over `1.0`, which would give a 4x tighter
ceiling, a 4x sharper detection threshold, and still 3.8x of margin over the
worst measured clean ratio (`0.262`). The report flags this itself as item 4 of
"what I want looked at hardest"; this is the measurement it asked for.
**Closed when** the entry records the band and says why the value sits at its top,
or moves.

**R65. (recordable) Two `expect=breach` assertions pin round-off with 1% and 3% of
margin, on a quantity the same file documents as scattering 2.3x-3.5x under a
permutation change.** `tests/verification/rung1/test_corpus_configurations.py:191`.
Measured at `83b2de2`: `slender_L_r_79` `1.0104e-12` (margin **+1.0%**),
`slender_L_r_118` `1.0275e-12` (**+2.8%**), `slender_L_r_94` `1.7620e-12` (+76%).
The permutation cell says two of those three are breaches under COLAMD and not
under MMD_ATA. The design intent -- keeping my measurement under test rather than
deleting it -- is right, and the failure message even says "Either the entry or
the code moved". But an assertion that a numerical error is *large enough* goes
red when the code gets better, and at 1% of margin it will also go red on a
different BLAS. These are entries I wrote; recorded so the fragility is scored
rather than discovered by a red build.
**Closed when** the breach half is expressed as a range the recorded value sits
inside with room, or those two entries are demoted to the floor-aware assertion
alone with the constant's ratio printed rather than asserted.

**R66. (recordable) Reading-order item 4b -- the diff of my own instructions.
Additive on balance and accepted; three holes measured and stated, because the
hook's own comment understates one of them.**
`git diff d426e48..HEAD -- .claude docs/SUPERVISOR.md` touches
`protect-reviews.sh`, `require-verdict.sh` and `settings.json`, in **two
standalone `process:` commits** (`7b6b9b3`, `8448517`) that touch no `floatfea/`
or `tests/`, each citing its directive (BE3 and BG6). `docs/SUPERVISOR.md` is
unchanged. **No commit in the range touches both `.claude/` and `floatfea/` or
`tests/`; none touches both `floatfea/` and `docs/reviews/`.** Checked
mechanically, both ways, over all nine commits.

The change is a net strengthening: the matcher gains `Bash`, the
interpreter-missing path fails closed, and the hook keys on `agent_type`. I
exercised it on twelve synthetic inputs. Denied as they must be: main-session
`Write` to `docs/reviews/` and to `tests/corpus/`, forward- and back-slash
absolute paths, `echo > tests/corpus/x`, `awk ... > tests/corpus/y`, a heredoc
with a redirect, and a `general-purpose` subagent writing `docs/reviews/`.
Allowed as they must be: `cat`, `grep` and `git log` on those paths, and
everything from `gating-supervisor`. Three gaps:

- `cd tests/corpus && echo x > y.txt` is **allowed**. The path never appears in
  the redirecting segment. The hook's stated limitation is "a path assembled at
  runtime from pieces, nor a verb outside that list", and this is neither -- it
  is the most ordinary way anyone would write into a directory. The note
  understates the hole by naming two exotic cases and not the plain one.
- Malformed stdin JSON **fails open**: the python runs under `2>/dev/null`, an
  exception leaves `agent` and `hit` empty, no `case` arm matches, `exit 0`. The
  header says the hooks "FAIL CLOSED", scoped to a missing interpreter; a reader
  will carry the stronger reading.
- `NotebookEdit` is not in the matcher and carries `notebook_path`, so neither
  the matcher nor the path extraction sees it.

`require-verdict.sh`'s exclusion of `tests/corpus` is the one relaxation and it
is correct -- it stopped the Stop hook demanding that I re-review my own corpus
commit. Its safety rests on `protect-reviews.sh` denying the implementer that
directory, which the first gap partially undermines. **Accepted, not blocking**:
no guard was removed, both commits are standalone and cited, and the
commit-separation check that depends on no hook is clean this round.
**Closed when** the header's limitation note names the `cd`-then-redirect case,
or the rule matches on the resolved working directory.

**R67. (recordable) Two commits bundle several findings, against BD6, and say so.**
`9dbfcb4` answers BG1/BG3/BG4 across five files; `aead308` answers BG5/R53/R54
across three. The report declares both and gives the reason -- splitting after the
fact would mean reconstructing states that never ran. I accept that for a round
whose findings are mostly one-line corrections in one file, and record it so it
is not read as precedent. The cost was real and visible: `9dbfcb4` is the commit
in which `MATRIX_SYMMETRY_COUNTER`'s and `ROUNDOFF_IDENTITY_COUNTER`'s bases were
both found wrong, and neither correction has a commit of its own to be cited by.

**R68. (recordable) Revision 7's `Carried` section lists ten of seventeen open
items.** A `grep` for each of `R6`, `R16`, `R25`, `R31`, `R32`, `R33`, `R36` over
the revision-7 text (`docs/reports/F2/step-4.md` from line 938) returns **0**.
The sixth verdict placed that obligation on step 5's report, so this is not yet a
breach -- but the complete list appeared for the first time in revision 6 and
disappeared again in revision 7, which is the exact regression the sixth verdict
wrote "Keep that" against. Recorded so step 5 has no room to read the requirement
as satisfied.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COND_FACTOR` | -- | `4.0` | dimensionless multiplier on `cond(K_ff)*eps`; the ceiling it forms is relative and dimensionless | `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT = 4.0e-10`, a defect size, **injected** by `test_the_floor_aware_ceiling_CATCHES_its_counter_defect` over four sections | `tolerances.py:477-523`, `F2.md` D7 item 5. **The form is the finding.** `4*9.2096e2*eps = 8.1797e-13` reproduces exactly and is tighter than the `1e-12` beside it -- *at metre scale only*; at `S=1e-3` the same expression is `5.3140e-07` and at `S=1e3` `3.5962e-08` (**R55**). Guarded in both directions and tightly: +10% reddens, -93% reddens; band `[0.3, 4.4]` with the value at the top (**R64**). The self-reference measurement's domain excludes the class that moves `cond` most (**R56**). Nothing was loosened by it: the gate asserts the constant alongside and at the posed geometry the new one binds. |
| `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT` | -- | `4.0e-10` | defect size, relative, dimensionless | -- | `tolerances.py:525-548`. **This is the model the protocol should follow.** Measured by inverting the shipped predicate per state on four sections; set 2.4% above the worst cell (`3.906e-10`), and the report records that a first draft at `3.7e-10` went red on `D = 0.080` -- the counter test working on its own author. I confirmed the tightness independently: `PATCH_TEST_COND_FACTOR 4.0 -> 4.4` reddens `[D=0.08]`. |
| `SOLVE_BACKWARD_ERROR_FACTOR` | -- | `8.0` | dimensionless multiplier on `eps`; the quantity is the standard backward error, dimensionless and unit-invariant | `SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT = 1.0e-6`, a defect size, **injected** at all 18 cells, with the clean cell asserted not already tripped so the counter cannot be vacuous | `tolerances.py:551-585`. Correct replacement for `SOLVE_RESIDUAL` and the right answer to R45. Worst clean cell `1.0343e-16 = 0.466 eps`, so `8.0` sits 17x above it -- reproduces exactly. Live band `[~0.5, ~35]`: `-> 30.0` silent, `-> 40.0` reddens, `-> 1.0` silent, `-> 0.4` reddens. 3.75x of silent widening remains and the entry does not say so. The `||K||_max` norm choice is named in the docstring, which is the right level of explicitness. |
| `SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT` | -- | `1.0e-6` | defect size, relative, dimensionless | -- | `tolerances.py:587-601`. 4.0x above the worst cell I measured (`2.528e-07`, twist at `S=1e-3`) -- correct and tight. The entry's table carries **no numbers** (**R60**). |
| `SOLVE_RESIDUAL`, `SOLVE_RESIDUAL_COUNTER` | `1e-13`, `9.9e-13` | **removed** | -- | -- | Removed with the quantity, which is the honest way to answer R45 and R49 together. `residual` survives on `SolveResult` as a reported number -- and is still gated in two unit tests (**R61**). |
| `MATRIX_SYMMETRY_COUNTER` | `1.0e-2` | `1.0e-2` (unchanged) | relative, dimensionless | -- | `tolerances.py:684-702`. **Basis corrected, value unmoved.** The correction is real and I confirmed it: an element contribution is symmetric, so the previously named "transposed element block" defect was a no-op that nothing had ever run. The new basis (mis-indexed scatter, `7.902e-02`) is injected. The *ceiling* remains widenable 1e5x (**R63**). |
| `ROUNDOFF_IDENTITY_COUNTER` | `1.0e-8` | `1.0e-8` (unchanged) | relative, dimensionless | -- | `tolerances.py:723-741`. Basis corrected from `theta = 1e-8` to `theta = 1e-4`; the O(theta^2) reason is right -- `I + [theta x]` is orthogonal to first order. The table reproduces. Ceiling widenable 1e5x (**R63**). |
| `DETECTION_THRESHOLD_BAND_COUNTER` | `0.25` | `0.25` (unchanged) | relative, dimensionless | -- | Now **consumed**, by `test_a_SENSITIVITY_CHANGE_breaks_the_threshold_band`, in both directions. `DETECTION_THRESHOLD_BAND 0.05 -> 0.20` reddens it. One of R30's four dead counters. |
| `COND_UNIT_INVARIANCE_COUNTER` | `1.0e-3` | `1.0e-3` (unchanged) | relative, dimensionless | -- | Now consumed by `test_a_STIFFNESS_DEFECT_moves_the_equilibrated_conditioning`. The injection is a stiffness defect where the assertion is about a unit change -- a different *driver* in the same *quantity*, which the docstring states and justifies (a unit change cannot move this quantity; that is the property under test). Accepted. The recorded non-monotonicity (10% moves it `7.05e-03`, 100% moves it `5.05e-03`) is the right handling. Ceiling widenable 100x (**R63**). |
| everything else | -- | unchanged | -- | -- | `git diff -U0 d426e48..HEAD -- floatfea/tolerances.py` filtered to `Final[float]` declarations gives four `+` and two `-` lines and **no modification**: no existing value moved in either direction. |

No tolerance was widened. No golden file moved. No test is skipped or `xfail`ed;
the suite has zero skips. Both new ACCURACY entries collect under
`test_accuracy_tolerances_have_a_counter_case`, so the empty-parameter-set guard
holds -- and the `_COUNTER_DEFECT` early return at
`test_tolerance_counter_cases.py:96` is a documented exemption carrying its
reason, not a silent skip.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R55** -- the floor-aware ceiling states its domain or moves to
   `cond(equilibrate(K_ff))`. Either way `test_corpus_configurations.py` asserts
   `PATCH_TEST_EXACTNESS` as well as the floor-aware ceiling on `expect=hold`
   entries, where it holds on all thirteen, and `F2.md` D7 item 5 stops handing
   F3 a criterion that moves 6.5 orders with the unit system.
2. **R56** -- "under any defect the gate must catch" is bounded to the three
   defects measured, and the entry names the uniform property error as the class
   that inflates the ceiling, with one of the two cells recorded.
3. **R57** -- `_build` raises on an `extra=` prefix or a top-level key it does not
   honour, and `typo_field_roll_rad` in the corpus goes green by raising.
4. **R58** -- `PATCH_TEST_EXACTNESS_COUNTER`'s entry carries the geometry it was
   measured at and the direction it degrades in, and `very_stubby_L_r_0p5` is
   either green or named in that entry as a known-uncovered configuration. The
   sixth verdict's withdrawal of R15 is **withdrawn**; treat R15's content as
   live.

R59 through R68 -- together with R6, R16, R25, R31, R32, R33 (outside G2.2), R36,
R50 and R52 -- may be answered in step 5's `Carried` section, **and that section
must list every one of them, open or answered.** Revision 6 listed all fifteen;
revision 7 listed ten of seventeen. That is R68, and it is the one item where
this project's own recorded history says the regression matters more than the
content.

**Adversarial corpus (BE3): 19 new entries, all unseen by the implementer; 17
caught, 2 not.** `tests/corpus/g22_model_configurations.txt`, now 36 entries,
committed separately in the commit immediately before this verdict, touching no
code. The 19 are the axes the file had none of: the **unit axis**
(`unit_km_similar`, `unit_mm_similar` -- geometrically similar models at 1000x
and 1/1000x, which is how R55 is expressible in the schema that exists), **wall
thickness, held out of every sweep so far** (`D/t = 5` and `D/t = 200`), **both
ends past the slenderness range the factor was fitted over** (`L/r = 189`, a
fourth measured breach at `4.4147e-12`, and `L/r = 0.5`), **the orientation guard
at its own boundary** (collinear and 0.003 degrees must raise and do; 0.0501 rad
must not and is exact at `3.8831e-15` with its control at `1.0764e-07`), **roll
past the recorded values** (pi/2, -2.5), **the `I_y/I_z` pin from the other
side** (0.5x, 10x), and **the corpus interface itself**.

**Scored against the implementer's checks at `83b2de2`: 17 of 19 pass, 2 are red,
and both reds are findings rather than bad entries** --
`test_the_corpus_entry_still_DETECTS_a_defect[very_stubby_L_r_0p5]` (**R58**) and
`test_the_corpus_entry_behaves_as_the_reviewer_recorded[typo_field_roll_rad]`
(**R57**). Full suite with the corpus applied: `2 failed, 492 passed`. That
17-of-19 is the coverage measurement for this round, and it is a good number: the
runner built at `aead308` handled fourteen configuration shapes it had never
seen, including two that must raise, without a change. What it did not handle is
the one shape that tests the runner rather than the element.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Seven
consecutive reviews by one reader. `459 passed` still means "not yet
contradicted" until V5.1 puts CalculiX on the other side.

**The pattern, seventh round.** Last round it was "the numbers are right and the
sentences explaining them are the reasoning that was never measured", and BG0 was
adopted for exactly that. It worked: three causal sentences were withdrawn on
cells this round, and the cells are correct -- I re-ran the permutation cell and
the conditioning cell and both hold. What replaced it is one level further out.
**The measurement is correct, the reasoning attached to it is now correct, and
the axis it was taken along was chosen by the same person who wanted the answer.**
`err/(cond*eps)` spans 8x -- along slenderness, and five orders along units. The
ceiling moves 1.13x under a defect -- under the three defects the author picked,
and 65x under the class the neighbouring test declares invisible. A uniform
property error cancels out of the stiffness ratios -- for the one case of three
where the change is actually a scalar multiple. Each is refuted by a cell that
holds the *published* variable fixed and moves a different one. The standing
question for step 5: *for every ratio and every span in this diff, which axis was
it measured along, and what does it do along the other one?*
