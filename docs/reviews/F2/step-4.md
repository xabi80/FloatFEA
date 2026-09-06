# Review — F2 step 4
Reviewed commit: 0862f314bb75ab2fcffc966291e2a60d348e39e9
Verdict: HOLD
Tests: 562 passed, 0 failed, 0 skipped   (my run at `47d117e`, `python -m pytest -q`, 2.97s.
With my tenth-round corpus applied at `0862f31`: **2 failed, 580 passed**.)

**Reviewed code commit: `47d117e`.** The header stamp is `0862f31`, my own corpus
commit, made immediately before this verdict and touching no code.

Tenth pass. Range `620ec96..47d117e`, eight commits: one `plan:`, two `process:`,
four step commits, one `docs:`.

**The ordering is correct and it is the first thing this verdict checked.**
`git log --format="%h %ad %s" --date=iso 620ec96..HEAD --reverse` puts the plan
re-lock `e89a5a8` (08:17) before the step commit `fdade28` (08:32). No commit
touches both `.claude/` and code -- `git show --stat` on each of `c1662ff` and
`111cb2b` lists only `.claude/`. Neither touches `docs/reviews/` or
`tests/corpus/`. The STOP was answered through the plan, which is the only route
a STOP has.

**And the answer is the right one.** The ninth verdict's STOP said a domain claim
is a statement about a space and this envelope was sampled on two of its
coordinates. The response was not a bigger envelope: it was to stop asserting a
quantity that has a `cond` in it. G2.2 now asserts `max|K_hat w|_interior /
(max|K_hat| max|w|)` -- Irons' condition itself, no factorisation, no solve. **I
did not take that on the argument; I measured it.** My own harness, my own seed:

```
1500 random configurations, D in [1e-4,10] m, D/t in [2.1,400],
     member lambda in [3,3000], FREE direction, FREE roll
                                            worst clean 4.60e-16 = 0.092x ceiling
16 orders of length unit (S = 1e-8 .. 1e+8), posed section
                                            0.019x .. 0.035x, flat
mesh at fixed lambda, n = 2 .. 200          spread 3.6x - 5.3x, worst 0.05x
the ninth verdict's own counterexample      0.022x   (it was 7.58x of the old)
```

The axis that moved the old quantity `35-57x` moves this one `5x`. The unit axis
that moved it by decades moves this one by `1.8x`. **The ceiling's domain problem
is genuinely dissolved, and this is the first round in five where I could not
break the ceiling.** That is the finding of this round and it should not be lost
in what follows.

**What follows is that the domain did not disappear -- it moved to the counter,
and it is 11% of member lambda away.** The 1e-6 defect's residual falls as
`1/lambda^2`, so detection, not the ceiling, is what runs out with slenderness.
Measured at this HEAD, skew, the gate's own station ratios:

```
  member lambda   558 (corpus worst)   600     620     650     900    1600
  x counter             1.075x        1.088x  1.019x  0.927x  0.484x  0.153x
                                               ^ pin   ^ first red
```

Two of my new entries at member lambda 900 are **red**, in both frames. That red
is the guard working -- `test_the_corpus_entry_still_DETECTS_a_defect` refuses to
certify a configuration the gate cannot fail on, which is exactly what a gate
should do and is a real improvement on a silent pass. But `F2.md` sec. 5b Q6 says
the domain question is **"dissolved"** and there is **"no boundary"**, and no file
in this repository records that the boundary is at member lambda ~630 or that the
corpus's most slender entry sits 7.5% from it. **R94.**

## Carried

Every item from the ninth verdict (`STOP @ e9dd32f`, committed `620ec96`), traced
through `620ec96..47d117e` and re-measured. The gated four first.

- **1. R81 (STOP) -- ANSWERED, and answered at the right level.** Not by a bigger
  envelope and not by moving `60` until the counterexample stopped firing -- by
  removing the quantity the domain was drawn around. `G22_VALIDATED_MEMBER_LAMBDA`,
  `warn_outside_validated_domain` and `OutsideValidatedDomain` are gone;
  `grep -rn` finds them only in comments recording the removal. My own
  counterexample, the one that produced the STOP, is now green at `0.022x` and I
  have carried it into the corpus as `r81_counterexample` -- the third of R81's
  three closing conditions, taken. The envelope question I asked three rounds
  running is answered, and I re-ran it on axes nobody named: 1500 draws, 16 orders
  of unit, `n = 2..200`.
- **2. R82 (blocking) -- ANSWERED by removal.** One tier. `PATCH_TEST_ROUNDOFF`
  and its counter are deleted; the eleven entries that never needed relief and the
  four marked `breach` are all held to `5e-15`. Verified against the shipped
  per-entry table: the four ex-breaches now read `0.011x`-`0.019x` of the ceiling.
- **3. R83 (blocking) -- ANSWERED.** `PATCH_TEST_EXACTNESS_COUNTER`'s entry is no
  longer byte-identical to anything: it states its operating point
  (`slender_axis_L_r_189`), the direction it degrades in (`1/lambda^2`, slope
  `-2.0`), and why the exemption it used to need is gone. The aniso exemption
  branch is deleted from the runner and I confirmed `aniso_I_y_500x` responds at
  `1.7605e-11` in the shipped output -- `164x` clear, as claimed.
- **4. R84 (blocking, reading-order item 4b) -- ANSWERED, and the fix is right.**
  `c1662ff`, standalone `process:`, `.claude/` only, citing the directive. I
  re-derived the clause rather than accepting the matrix: the exemption is now
  `>&` and a redirect whose target is stripped as `/dev/null|NUL`, so
  `echo x 1> tests/corpus/y` and `cmd 2> tests/corpus/y` both reach
  `re.search(r">{1,2}(?!&)", ...)` and are denied, while `pytest ... 2>&1` and
  `... 2>/dev/null` still clear. `2>>` is now caught by the rule rather than by
  accident. The commit message pastes both directions.
- **5. R78 hole 3 -- ANSWERED** (`111cb2b`, standalone `process:`). The hook reads
  `("file_path", "path", "notebook_path")`. The commit records the thing worth
  recording: it had been "fixed" once in `settings.json` and the hook then read an
  argument that was not there, which is a guard reporting success on a field it
  cannot see.
- **6. R85 (recordable) -- ANSWERED by removal, not by moving the number.**
  `grep -n "100.0 \* ceiling"` returns nothing. The separation is now asserted as
  `PATCH_TEST_EXACTNESS_COUNTER > PATCH_TEST_EXACTNESS`, a relation between two
  values `tolerances.py` already owns, with no third number. That is the better of
  the two closing conditions I offered.
- **7. R86 (recordable) -- ANSWERED by removal.** The paragraph claiming a deleted
  function's property "is real and asserted" went with the entry.
- **8. R87 (recordable) -- ANSWERED.** `grep -rn "conventions.md" floatfea/ tests/
  docs/milestones/F2.md | grep -i admission` returns nothing; the citation is one
  string, `_LIMIT_SOURCE`, in one place. The depth formula in `tolerances.py` now
  reads `D_o = 2 sqrt(2I/A + A/2pi)` and says why the old one was wrong, and the
  entry's status line says CONFIRMED rather than PENDING.
- **9. R88 (recordable) -- ANSWERED, with a meta-test.** `rotation_matrix` refuses
  a non-finite roll and the unit test also asserts a finite roll still builds, so
  the guard is not one that refuses everything. My `roll_field_nan` entry is green
  by raising.
- **10. R89 (recordable) -- ANSWERED, and at the right level.** `_inadmissible`
  cannot raise at import, and the two shapes I had to carry as comments are now
  committed entries plus four more. The closing condition asked for either the
  parser or laziness; both were done.
- **11. R90 (recordable) -- ANSWERED AT THE TWO SITES THE CONDITION NAMED, and the
  fix does not reach its only consumer.** `_outer_diameter` refuses a shape it has
  no inversion for; `member_lambda` takes `second_moment` and defaults to
  `min(I_y, I_z)`. Both named sites are fixed. But the one call site in the
  repository rebuilds the section from `entry["section"]` and discards
  `extra=I_y_over_I_z=`, so the shipped table still prints `46.5` for
  `aniso_I_y_twentieth` where the report's own row claims `208.0`, and no test
  anywhere exercises the new argument. **R96.**
- **12. R77 -- ANSWERED, and the replacement was mutation-checked.** The two routes
  (`_branch` and the `SOLVED` parametrisation) are genuinely independent and the
  partition is asserted non-degenerate in both directions. Sixth guard on that
  test, finally closed. A different vacuity took its place four hundred lines up:
  **R91.**
- **13. R65 -- WITHDRAWN by me.** The three `expect=breach` entries pinned
  round-off against a quantity nothing asserts. They are re-recorded as ordinary
  `hold` entries by the reporting test and I have no pin left to carry; the tenth
  round's `lam620_counter_pin` replaces it on the axis that now matters.
- **14. R63 -- carried, unanswered, declared.** `MATRIX_SYMMETRY` and
  `ROUNDOFF_IDENTITY` remain widenable in silence.
- **15. R76, R79, R80 -- NOT ANSWERED, correctly declared open.** R80's third
  instance closed with R85; the finding stands.
- **16. R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 --
  still open**, correctly declared in the report's section 7, routed to step 4a or
  later steps.
- **17. R68's standard held, fourth round.** Section 7 lists every open item by
  number and I found none open that it omits.

## Findings

**R91. (blocking) `_parse` throws away the reviewer's `expect` on any line it
cannot execute and writes `"raise"` in its place, and the per-entry test then
asserts that value equals `"raise"`. The assertion compares a variable with the
constant assigned to it eighty lines earlier and cannot fail.**
`tests/verification/rung1/test_corpus_configurations.py:244` and `:575`.

```python
rows.append({"id": ident, "expect": "raise", "_error": str(exc), "_line": line})
...
expect = entry["expect"]
if "_error" in entry:
    assert expect == "raise", (
        f"{entry['id']}: the corpus expects {expect!r} but the line cannot "
        f"be executed at all -- {entry['_error']}")
```

Executed, on a line whose recorded expectation is `hold`:

```
row as _parse builds it:   {'id': 'probe_hold_unparseable', 'expect': 'raise'}
the reviewer wrote expect=hold; the module records expect= raise
PER-ENTRY TEST: PASSED on a line the reviewer said must HOLD
```

`_parse`'s own docstring says "a malformed line the corpus expected to WORK is a
failure", and the failure message is written to name a disagreement it can never
see. This is R77's species -- a predicate compared with the thing that defines it
-- in the same file, in the commit after R77 was closed, and it lands on the one
instrument in this repository that is not the implementer's. The effect is not
hypothetical: my new `roll_and_aniso_together` asks for roll and anisotropy on one
member, `extra=` takes one key, and the entry reads **green while measuring
nothing**.

**Closed when** the reviewer's `expect` survives the parse failure and a line
recorded `hold` that cannot be executed produces a **red** naming the field the
module cannot build -- demonstrated on `roll_and_aniso_together`, which either
parses or reddens.

**R92. (blocking) A six-column table of scratch measurements was added to
`floatfea/tolerances.py` two commits after `CLAUDE.md` BI3 forbade exactly that,
and the report's own provenance header names it as scratch.**
`floatfea/tolerances.py:192-198`, commit `fdade28`.

```
#   L/D           0.50       1.00       1.50 |     2.00       8.00      48.00
#   response   8.80e-09   4.55e-09   2.02e-09| 1.14e-09   7.12e-11   2.02e-12
#   x counter    88000      45478      20213 |    11371        712         20
```

The numbers are **correct** -- I reproduced all six independently
(`8.7999e-09, 4.5478e-09, 2.0213e-09, 1.1371e-09, 7.1212e-11, 2.0222e-12`) -- and
that is not the point BI3 makes. `ls scripts/` returns `write_verdict.py` and
nothing else; no committed script produces this table at this commit, and
`grep -rn "L/D" scripts/` is empty. BI3 gives two routes and this takes neither:
"either a committed script produces the table at the commit that publishes it, or
the table belongs in the step report -- which is regenerated by rule -- and the
entry carries the single number it needs and a pointer." The report's section 4
already carries the table; the entry needs the sentence and the pointer.

The rule was earned by two tables left stale by `8/5`. This one was written the
same day the quantity moved, and the paragraph immediately above it in the same
entry explains that the PREVIOUS table there went stale for precisely this reason.

**Closed when** the table is in the step report only and the entry carries the one
number it needs with a pointer, or `scripts/` gains the generator and the commit
that publishes the table runs it.

**R93. (blocking) `test_patch_test.py`'s module docstring states "Every figure
below this line was re-measured on the shipped quantity at this commit." Three
blocks below that line were not, and two of them are refuted by measurements
inside the same file at the same commit.**
`tests/verification/rung1/test_patch_test.py:17`, `:657-672`, `:757-767`, `:924-926`.

*(i) The resultant-comparison table, `:757-763`.* Its "via field" column is the
retired quantity's decision thresholds. I bisected both predicates at this HEAD:

```
state          table "via field"   old quantity (fwd > 1e-12)   SHIPPED (oob > 5e-15)
axial              9.1808e-12            9.1850e-12                  1.0136e-13
twist              9.1708e-12            9.1663e-12                  2.8348e-10
shear              8.4540e-12            8.4278e-12                  1.1298e-10
```

The table's column is the middle one to three digits. `DETECTION_THRESHOLD`, 130
lines above it in the same file, carries the right-hand one. The file contradicts
itself. The sentence the table exists to support -- **"As a GATE the resultant
channel is ~150x weaker"** -- is refuted with it: on the shipped quantity the
ratio is `14304x` in axial and `5.1x` in twist, a span of three orders where a
single number is written.

*(ii) `test_a_TRANSPOSED_TRANSFORM_on_one_element_breaks_every_state`, `:924-926`.*
"axial 1.53e+00, curvature 2.01e-01, twist 1.57e-01, shear 3.02e-01,
curvature_xz 1.01e-01, shear_xz 1.49e-01 -- every state, at O(1)." Measured on the
quantity the test now asserts:

```
axial 2.8565e-02  curvature 1.4356e-02  twist 7.1889e-04
shear 2.1497e-02  curvature_xz 8.2813e-03  shear_xz 1.2401e-02
```

None is O(1); the smallest is `2000x` below the docstring's smallest. **The plan
quotes the correct `7.1889e-04` for this case**, so the number existed and the
docstring was not updated with it.

*(iii) `WHAT THE BAND BUYS`, `:657-672`.* `git show
620ec96:tests/verification/rung1/test_patch_test.py` gives this block
byte-identical. Its first column does not reproduce: it records `axial 0.997640,
curvature 1.003067, shear 1.009952`; the shipped predicate gives `0.996385,
0.999760, 0.999578`, and two of the six cross 1.000 in the old table where none
does now. The plus/minus columns are unregenerated with it.

*(iv) minor, same block class.* The comment above `GATE_UNIT_SCALES` says the
clean value "spans 3.8x (0.13-0.49 eps)" across six orders of length unit. The
thirty-six cells that parametrisation actually runs span `0.0001` to `0.665 eps`
at this commit, and the per-scale worst is `0.665 / 0.392 = 1.7x`.

Four of the five findings in the fifth verdict on this step were sentences in
files a reader trusts, and that is why BF0 exists. A blanket "every figure was
re-measured" is the strongest form of that claim and the cheapest to refute.

**Closed when** each of the four blocks is regenerated at its commit or deleted,
and the module docstring's blanket sentence is either true or replaced by a
per-block statement. `(i)` is the one that matters most: it is the number a reader
uses to decide what the resultant channel is for.

**R94. (blocking) The domain moved from the ceiling to the counter and is recorded
nowhere. The plan says it is "dissolved" and that there is "no boundary"; the
boundary is at member lambda ~630 and the corpus's most slender entry sits 7.5%
from it.** `docs/milestones/F2.md` sec. 5b Q6 and sec. D7 item 7,
`floatfea/tolerances.py` `PATCH_TEST_EXACTNESS_COUNTER`.

The ceiling's domain is dissolved and I verified it hard (header). The counter's
is not, and the same `1/lambda^2` the entry records is why:

```
  member lambda   558 (corpus worst)   600     620     650     900    1600
  x counter             1.075x        1.088x  1.019x  0.927x  0.484x  0.153x
  x ceiling (clean)     0.020x        0.017x  0.030x  0.009x  0.033x  0.022x
```

At member lambda 650 the gate holds and cannot fail. My two entries at 900 are red
in both frames (`0.484x` skew, `0.413x` axis-aligned), so it is not a skew
artefact. Beyond ~2800 the 1e-6 defect does not reach the ceiling at all.

**Three things distinguish this from R81 and they are all improvements.** The
failure is loud, not silent -- an assertion refuses to certify. It is on the
counter, where a red means "this gate cannot fail here" rather than "this clean
member is wrong". And the members concerned are `L/D` 215 to 312, far from the
platform's braces, where R81's counterexample was an ordinary `L/D = 20`. What it
is not is dissolved.

**Closed when** one of: the entry states the member slenderness at which the
counter stops clearing, measured, so a later reader is not told the domain
question is gone; or the plan's sec. 5b Q6 sentence is narrowed from "dissolved"
to what was measured (the ceiling's domain is dissolved, the counter's runs out at
`1/lambda^2`), with the number; or the corpus schema gains a way to record "the
ceiling holds and the gate cannot fail here", which is the state my two entries
are in and for which `expect` has no value.

**R95. (recordable) `_direction` returns the zero vector its own docstring says it
refuses, whenever the input direction's norm overflows.**
`tests/verification/rung1/test_corpus_configurations.py:206-211`.

```
$ _direction(0, "1e308,1e308,0")
RuntimeWarning: overflow encountered in dot   numpy/linalg/_linalg.py:2767
-> array([0., 0., 0.])   norm 0.0
```

`norm = np.linalg.norm(v)` is `inf`, `norm == 0.0` is False, and `v / inf` is the
zero vector. The guard tests the input norm and the failure is in the result. It
is caught downstream, by `Node`'s "node_a and node_b must be distinct", for a
different reason -- so `expect=raise` passes and certifies the wrong refusal.
`test_orient_takes_any_direction_and_NORMALISES_it` asserts `|got| == 1` over four
parametrised directions and its collection cannot contain this one: assertion
domain blindness in the recorded form. My `orient_norm_overflow` entry is green
and its RuntimeWarning is visible in the suite output.

**Closed when** `_direction` refuses a non-finite norm and a zero result, and the
normalisation test's parametrisation contains an overflowing input.

**R96. (recordable) `member_lambda`'s weak-axis default is unreachable from its
only consumer and untested anywhere.**
`tests/verification/rung1/test_corpus_configurations.py:410-419`.

```python
def member_lambda(entry) -> float:
    return _member_lambda(float(entry["stations"]), _section(entry["section"]))
```

`_section` rebuilds a circular tube from the spec string; the
`extra=I_y_over_I_z=` modification that `_build` applies is not applied here. So
the shipped table prints

```
  aniso_I_y_twentieth   member lam 46.5      (I_y/I_z = 0.05)
```

where the report's R90 row states "`I_y/I_z = 0.05` reads 46.5 on `I_z`, **208.0**
on the weak axis". The function does; the repository never asks it to.
`grep -rn "second_moment" tests/` returns nothing, so the new argument and the
`min(I_y, I_z)` default have no negative control at all -- a code change whose
property is asserted by no test, twenty lines from a docstring explaining that
this is exactly how `_outer_diameter`'s circular inversion came to be called
general.

**Closed when** the corpus's `member_lambda` reads the section the entry actually
builds, and one test constructs `I_y != I_z` and asserts both readings.

**R97. (recordable) "The forward field error is reported per corpus entry and
never asserted at a constant" is not true at the gate's own geometry, and the true
statement is better.** `docs/reports/F2/step-4.md` rev 10 section 2, `F2.md`
sec. D7 item 7, `tests/verification/rung1/test_patch_test.py:525-531`.

`test_the_six_constant_strain_states_are_EXACT` still asserts `res_err <=
RESULTANT_EXACTNESS` on resultants recovered from the **solved** field, at all 36
cells. Bisected on the shipped predicate, holding everything else:

```
  state    clean res_err    u_free x (1+d) -> res_err        d that reddens 1e-9
  axial      1.75e-15       1e-10 -> 4.65e-10                      2.15e-9
  twist      4.24e-15       1e-10 -> 4.65e-10                      2.15e-9
  shear      3.92e-13       1e-10 -> 1.97e-08                      5.1e-11
```

So the solved interior field is bounded at `2.15e-9` relative at the gate's
geometry -- four orders looser than the retired `1e-12`, and not "nowhere". For
corpus entries it genuinely is unasserted, because `_measure` computes no
resultant error. Saying which is which costs a sentence and removes a claim a
grep refutes.

**Closed when** the sentence distinguishes the gate's geometry (bounded through
the resultant channel, at the measured `2.15e-9`) from the corpus (reported only).

**R98. (recordable) Two smaller ones, together.**
`tests/verification/rung1/test_corpus_configurations.py:533`;
`docs/reports/F2/step-4.md` rev 10 header.

* `INADMISSIBLE = [...]` is built at import and never read: `grep -rn
  "INADMISSIBLE"` finds the assignment and three comments. Harmless, but it is the
  variable R89 was about and a reader will assume it is load-bearing.
* The report's provenance header says the four scratch groups are "labelled where
  they appear". None of the four carries an inline label; the header's list is the
  only labelling. Naming them centrally is honest and I credit it -- the sentence
  describing it is not what the file shows.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS` | `1e-12` | `5e-15` | dimensionless: a relative residual, numerator and denominator both carrying the largest stiffness. **Correct form, and the best form this gate has had** -- I could not make it move: 1500 random configurations over D, D/t, member lambda, free direction and free roll give a worst clean value of `4.60e-16`; 16 orders of length unit give `0.019x-0.035x`; `n = 2..200` gives `0.05x` | `PATCH_TEST_EXACTNESS_COUNTER`, below | `tolerances.py` entry + `F2.md` sec. 5b Q6 + report sec. 1. **The judgement to move the number is right and the directive text does not reach it**: `1e-12` was derived for the forward error of a solve, and on this quantity it puts the counter at `0.11x` of the ceiling -- a gate that holds and cannot fail. Keeping it would have been R41 species. **It is a tightening of 200x**, the direction `CLAUDE.md` permits. Both ends are named and I re-derived both: `26.8x` above the corpus floor as claimed, but **`10.9x` above the floor of my wider envelope**, which is the honest headroom and is not in the entry. `21.5x` below the counter, confirmed. |
| `PATCH_TEST_EXACTNESS_COUNTER` | `1.0e-7` | `1.0e-13` | same quantity as the ceiling, dimensionless | n/a (it is the counter) | `tolerances.py` entry. **The "not comparable" argument is right and I tested it adversarially rather than accepting it.** The two numbers are responses of different quantities to the same defect, so the comparable figure is the SMALLEST DEFECT THE GATE STILL DETECTS, and I bisected both predicates at the same geometry: new `1.01e-13` axial (91x **stronger** than the old `9.19e-12`) and `1.13e-10` to `2.83e-10` in the other five (12x-31x weaker). At the corpus slender end the loss is larger: `4.7e-8` against the old constant `8.7e-12` and the retired tier `1.7e-10`. **So the change is not uniformly a strengthening and the entry does not say so.** What redeems it is that the old gate could not be run at those configurations without false reds, and that a 1e-6 defect is four orders below anything a real defect produces -- the transposed transform sits at `7.19e-04`. The 7.5% margin does carry over and is stated with its operating point, which is the part R83 asked for. |
| `G22_VALIDATED_MEMBER_LAMBDA` | `60.0` | **removed** | -- | -- | with the quantity. `grep -rn` finds it only in comments recording the removal. The right answer to my STOP. |
| `PATCH_TEST_ROUNDOFF` | `2e-11` | **removed** | -- | -- | R82 dissolved rather than answered; the second tier existed to relieve entries this quantity does not strain. |
| `PATCH_TEST_ROUNDOFF_COUNTER` | `1.0e-7` | **removed** | -- | -- | with its ceiling. |
| `NON_SCALAR_ERRORS` floors | `1e-4`, `1e-3` | `1e-7`, `1e-6` | discrimination floors, asserted from BELOW | n/a | `test_patch_test.py:1034-1038`. **Lowering these is a weakening in form**, and the comment says so explicitly and correctly ("setting them low weakens the claim rather than propping it up"). Each sits `21.6x` / `28.9x` below its own re-measured response. Correctly handled. |
| `DETECTION_THRESHOLD`, six states | `~9e-12` flat | `1.01e-13 .. 2.83e-10` | not a tolerance; a recorded property, asserted by its own test | `DETECTION_THRESHOLD_BAND_COUNTER` | **Independently reproduced by bisection, all six, to three digits.** The `2800x` spread is real and recording six numbers rather than one is right: a flat threshold would have described the axial state and nothing else. |
| `BEAM_ADMISSION_L_OVER_D` | `2.0` | `2.0` | unchanged | none, correctly (structural) | **The withdrawal is the best thing in this round.** The sweep that supported it was a property of the retired quantity; re-measured, the control is STRONGER below the limit, and the entry says so -- "the limit keeps its physical justification and loses its numerical one". I reproduced all six columns exactly. That is what the eighth verdict R70 asked for, done unprompted. The table PLACEMENT is **R92**. |
| everything else | -- | unchanged | -- | -- | the `Final[float]` lines of `git diff 620ec96..HEAD -U0 -- floatfea/tolerances.py` are **two additions and five deletions, no third value moved**. No accuracy ceiling was widened in place and none was loosened to rescue a red. |

No golden file moved. No test is skipped or `xfail`ed; a grep for `xfail` and
`pytest.skip` over `tests/` returns nothing.

**One claim in the report the diff does not support**, beyond those already
numbered: section 7 R90 row states the weak-axis reading as a fact about the
repository, and the shipped table prints the strong-axis number for the same entry
at the same commit (**R96**).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a **HOLD, not a STOP**:
the plan was reopened and re-locked in the right order, the quantity is the right
quantity, no element defect was found for the eleventh consecutive round, and
nothing is red at the reviewed commit. Two things are red with my corpus applied
and they are the subject of R94.

1. **R91 -- the corpus own expectation is overwritten before it is checked.**
   First, because it is the mechanism by which everything else in this section is
   measured, and because a check that cannot fail is the failure this project keeps
   finding. `roll_and_aniso_together` either parses or reddens.
2. **R94 -- the domain of the counter.** The number, in the entry or in the plan.
   Do not answer it by lowering `PATCH_TEST_EXACTNESS_COUNTER`: the assertion is
   `smallest >= COUNTER`, so lowering it weakens the control, and my two red
   entries would go green having certified nothing.
3. **R92 -- the table in `tolerances.py`**, moved or generated, per the two routes
   BI3 gives.
4. **R93 -- the four unregenerated blocks**, and the blanket sentence above them.

R95 through R98, together with R63, R76, R79, R80, R6, R16, R25, R30, R31, R32,
R33 (outside G2.2), R36, R50, R52 and R62, may be answered in the next report
`Carried` section, **and that section must list every one of them, open or
answered.** Four rounds of a complete list now; keep it.

**Adversarial corpus (BE3): 12 new entries committed, all unseen by the
implementer; 9 scored exactly as recorded, 2 red, 1 absorbed.**
`tests/corpus/g22_model_configurations.txt`, now **74**, committed separately at
`0862f31` immediately before this verdict and touching no code. Full suite with the
corpus applied: **2 failed, 580 passed**.

The twelve are the axes this round created. The **domain of the counter** -- a pin
at member lambda 620 (`1.019x`, so a 2% loss of sensitivity reddens it) and two
undetectable entries at 900 in both frames. The **counterexample from the ninth
verdict**, carried as an entry at last because `orient=` takes a free direction:
`0.022x` where it was `7.58x`. The **degeneracy threshold taken from both sides**,
`0.0501` admitted and `0.0499` refused, because a threshold sampled on one side is
a threshold nobody has measured. The **free direction reaching sections the four
names cannot** -- a near-solid wall and an anisotropic section off every axis. And
the **remaining value-shaped holes in the parser**: an overflowing norm, a
subnormal component, a roll of `1e300`, and the one entry that reads green while
measuring nothing (**R91**).

**Eleven consecutive rounds have found no element defect.** Per the guard that
still means "not yet contradicted", and it stays that way until V5.1 puts CalculiX
on the other side. It is worth saying plainly what changed this round: for the
first time in five rounds I could not break the ceiling, and I tried on five axes
with my own harness and my own seed.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Ten
consecutive reviews by one reader.

**The pattern, tenth round.** Nine rounds asked which axis every ratio was
measured along, and each round produced a better envelope. This round stopped
answering the question and removed the quantity that made it unanswerable -- the
move that was available from the third round onward, and finding it is the real
result of this milestone. What did not change is the smaller thing underneath:
**every one of the four blocking findings in this round is a sentence or a check
that describes the repository as it was one commit ago.** A stale table, a stale
docstring, a stale blanket claim, a plan word that outran its measurement, and an
assertion holding a value it assigned itself. The standing question for the next
round is narrower than any I have asked: **for every figure in this diff, what ran
it, and at which commit?**
