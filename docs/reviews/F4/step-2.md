# Review — F4 step 2
Reviewed commit: 46154986ac3b129d9bb9d1cf8c0bd6d05f7582a6
Verdict: HOLD

**Reviewed commit: `4615498`.** (`46154986ac3b129d9bb9d1cf8c0bd6d05f7582a6`, HEAD of F3,
pushed.) Range `488f2d8..HEAD` -- two commits.
Tests: 2988 passed, 32 failed, 0 skipped (MY OWN run, one invocation, no `--ignore`, no
`-k`, no deselection, in the repository itself, 639.53s. **All 32 are EG3 state (2) and
each is traced by name in section 2.**)
**CI at the reviewed commit: run `37492421362` at `4615498`, conclusion FAILURE.**
`the verification ladder: success` at EVERY step -- `ladder 1`, `2`, `3`, `6`, `4`, `5`.
`lint, unit and guards: failure` at `guards and meta-tests` ONLY; `actionlint`, `ruff`,
`black --check`, `mypy` and `unit tests` all success. `32 failed, 998 passed in 328.27s`
-- the same 32, same ids. NOT CK2: `runner_name` is `GitHub Actions 1000001531`, the steps
ran, the durations are real.

## Round of 2026-10-06 -- ES0 INTERIM CHECK. Counts against NO round.

**ES0's premise verified before anything else, because the exemption rests on it.**

```
claim  there is no new report revision -- the report is the one verdict 97 judged
cmd    git log --format='%h %s' -1 -- docs/reports/F4/step-2.md
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), ...
judge  7cee09f is the commit verdict 97 judged. The report has not moved. This is an
       interim check, it counts against no round, verdict 97 stands as round 1 of 3,
       and TWO REVISIONS REMAIN.
```

**Instruction 1b does not fire, and I say so rather than leaving it silent.** The report's
header reads `Answers: verdict 96 @ 5786bed` and the newest verdict is 97. Under 1b that
comparison is a HOLD. It is not one here: 1b guards against a report that answers a
superseded round, and a report that PREDATES the newest verdict with no revision between
them is EG3 state (2) -- designed, self-clearing, and the exact state ES0 exists to
permit. The distinction is the same one DD1 draws between an open step and a step file.

**I accept ES0's scope and I have held to it:** the suite, CI, and a CZ0 (a)-(d) scan of
`488f2d8..HEAD`. No corpus batch. No closure list -- section 6 records the three
closure-class things I found so they are not lost, as single lines, explicitly not as a
list to work through.

**HOLD, on three items, two of which are repairs that stopped one site short of their own
closing condition.** R686 is ANSWERED and I reproduced it in both directions plus a third
the condition did not ask for. R687 and R688 are answered on the branches they took.
**R689 is HALF answered and R682 is not answered on the branch the hand-back says it
took** -- and both are the same shape, the shape `CLAUDE.md` records under *A closing
condition that names sites is closed site by site*. That rule was earned by R29. This is
its third instantiation in four verdicts.

**No STOP.** The ladder is green at every rung in CI. `4615498` is the permitted form for
touching my own instructions and I confirm it in section 1 as I was asked.

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 488f2d8..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 31 +++++++++++++++++++++++++++++++
out    (.claude/ -- nothing)
cmd    git log --format='%h %s' 488f2d8..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    4615498 process: ES0 -- rounds are counted per report revision; an interim check
out            counts against none
```

**`4615498` IS THE PERMITTED FORM. NOT A STOP-CLASS FINDING.** Four conditions, each
checked rather than inferred:

```
claim  standalone -- it touches nothing but the two instruction files
cmd    git show --stat 4615498
out    CLAUDE.md | 31 +++ ; docs/SUPERVISOR.md | 31 +++ ; 2 files changed, 62 insertions(+)
claim  zero deletions, so no guard was removed
out    62 insertions(+), 0 deletions -- and I read the 31 lines; they are additive
claim  it cites the directive asking for the change, in its first line
out    "process: ES0 -- rounds are counted per report revision ..."
claim  the two inserted regions are byte-identical, which the commit message asserts
cmd    git diff 488f2d8..HEAD -- <file> | grep '^+' | grep -v '^+++' | sed 's/^+//' ; md5sum
out    8a6ad471294c2c4cfc1886bb3ed6ee14  (CLAUDE.md)
out    8a6ad471294c2c4cfc1886bb3ed6ee14  (docs/SUPERVISOR.md)
out    diff: no output. BYTE-IDENTICAL.
```

Same ruling as `9985bcd`, on the same four grounds, and I checked it the same way rather
than carrying the earlier ruling across.

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                   <- non-empty, so the pathspec is the CI0 one
cmd    git diff 488f2d8..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty). No conftest changed. No new plugin. CH2 clear.
```

## 2. THE 32 REDS, EACH TRACED BY NAME (EG3(i), CA2)

EG3(i) is explicit that a family is not a trace. Each id, matched against EH1's and EJ2's
corrected **state (2)** list:

| count | id | on the list as |
|---|---|---|
| 17 | `test_every_named_site_is_touched_or_declared[R686/R687/R688/R690-...]` | named, state (2) |
| 5 | `test_the_report_carries_the_finding[R686..R690]` | named, state (2) |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | named, state (2) |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | named, state (2) |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | named, state (2) |
| 1 | `test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` | the red baseline |
| 6 | the six planted states | the cascade, by failure line |

**The cascade is identified by each state's OWN failure line and not by its name**, which
is the R629 discipline:

```
out  [baseline] AssertionError: baseline: expected a clean run.
out  [verdict_amended_after_the_commit_the_report_answers] ... expected a clean run.
out  [non_numeric_step_suffix]           ... must be stepped over, not reacted to.
out  [superscript_digit_step_number]     ... must be stepped over, not reacted to.
out  [draft_suffix_beside_a_step_report] ... must be stepped over, not reacted to.
out  [step_number_is_the_empty_string]   ... must be stepped over, not reacted to.
out  [zero_padded_step_number]           ... must be stepped over, not reacted to.
```

Every one of the six asserts against a clean baseline and the baseline is dirty.
17+5+3+1+6 = 32. **Nothing is outside the list, so CZ1 (iv) does not fire and this is not
a (d).**

**EG3(ii), the half no verdict has measured -- state (1) DID clear at my verdict commit.**
`test_the_guard_reads_the_step_being_worked_on` was the cause of all eight reds at
`7cee09f` and it is absent from the 32 above. `488f2d8..4615498` touches neither the report
nor the verdict, so the measurement at `4615498` is the measurement at `488f2d8`:

```
cmd    git diff 488f2d8..HEAD --stat -- docs/reports docs/reviews
out    (empty)
out    test_the_guard_reads_the_step_being_worked_on: NOT in the FAILED list. CLEARED.
```

## 3. WHAT I REPRODUCED RATHER THAN READ

**R686 -- ANSWERED, and the repair is bidirectional, which is more than the condition
asked.** I ran the ablation myself, in both directions and in a third:

```
cmd    python <scratch>/r686.py  (pytest rung4 + tests/test_no_tolerance_literals.py)
out    as shipped (deck 0.8)              88 passed
out    deck key -> 0.9                    1 failed  RED test_R653_the_DECK_and_the_DECLARATION_agree...
out    deck key -> 0.85                   1 failed  RED (same)
out    deck key -> 0.8000001              1 failed  RED (same)   <- `==`, no slack
out    declaration -> 0.9, deck untouched 2 failed  RED (same) + RED ..._FloatSims_DEFAULT_reddens...
out    deck key DELETED                   1 failed  RED (same)   <- raises, never defaults
out    deck restored: True
rule   editing EITHER side must redden; a missing key must raise, not default
```

That is the EB6 shape and it is the real one. The literal left the comparison entirely
rather than being re-marked, which is the right fix and not the cheap one. **R686 closed.**

**R687 -- ANSWERED on the branch it took, and I note what that branch costs.** Branch A of
the three I offered: the ranges the scheme actually attains, with both closed forms and
both crossover values pasted, and the false sentence gone from both sites (the marker
comment is deleted; the assertion message is rewritten). `rho_inf = 0.2` is now walked, so
the value my finding was about is exercised. **Closed as offered.** The measurement of what
the branch buys is in section 6; it is not a reopening.

**R688 -- ANSWERED on the branch it took.** The window is declared, with a counter, with
two plan rows in the same commit, and the word "exact" is gone from the docstring. The
reference resolves:

```
cmd    sed -n '255,263p' docs/load-interchange-v1.md
out    line 259: alpha_m = 0.42105     alpha_f = 0.47368     difference 0.05263
judge  `_DOC_DIFFERENCE = 0.05263` and its "at line 259" both resolve. Citation good.
```

The per-channel figures the hand-back pastes are correct, and they are **a different
quantity from the four in my R688** -- mine were the drift `round(x,5)` still ACCEPTED
(distance to the quantisation edge, governing `7.895e-07` on `alpha_f`); these are
`|exact - published|` (governing `4.210526e-06`, also on `alpha_f`). Both right. The
hand-back's sentence "Per-channel drifts reproduce yours" is false -- they are not the same
numbers and could not be -- and it is section 6's third line, not a blocking item. What IS
blocking is the bracket figure: R693.

## 4. R689 -- HALF ANSWERED. I SOLVED THE THRESHOLD AND THE VACUITY IS STILL THERE.

The all-zero row is closed and I reproduced it. The COUNT is not, and `compared > 0` is a
nonzero-check wearing a count's name. Inverting the decision rule rather than sampling one
side of it:

```
cmd    python <scratch>/r689.py  (the production gate's own helpers, built fixture, real mapper)
rule   the shipped pair: `_channels_compared(...) > 0` and
       `max(per_body) < F4_MAPPING_CONSERVATION`
out    dense in all 16 blocks  blocks 16/16  compared 10/10  err 2.196e-16  GREEN  <- control
out    zeros everywhere        blocks  0/16  compared  0/10  err 0.000e+00  RED    <- R689, closed
out    only block  0 (buoy1)   blocks  1/16  compared  2/10  err 0.000e+00  GREEN
out    ... every one of blocks 0-11 (the twelve buoys)  compared 2/10  GREEN
out    ... every one of blocks 12-15 (the four hubs)    compared 4/10  GREEN
out    ALL SIXTEEN single-block rows read GREEN. The minimum is 2 of 10 channels.
out
out    `compared >  0`: 16 of 16 degraded rows still GREEN
out    `compared >  1`: 16 of 16 still GREEN
out    `compared >  2`:  4 of 16 still GREEN
out    `compared >  3`:  4 of 16 still GREEN
out    `compared >  4`:  0 of 16 -- EVERY degraded row reddens       <- the boundary
```

So the threshold that closes the item is `compared > 4`, equivalently `compared == 10`, and
`> 0` sits four below it. My condition read "asserts the COUNT of bodies compared
relatively -- equivalently that the lam row is nonzero in all sixteen blocks", and I named
the pattern: "that is the `checked == 16` pattern this file already uses twice". A floor of
one channel out of ten is not the count. The coverage still degrades invisibly, which is
the sentence the condition was written against.

## 5. R682 -- NOT ANSWERED. THE FALSE ARITHMETIC SURVIVES AT TWO OF THREE NAMED SITES.

```
cmd    grep -rn '1/18\|5\.555556e-02\|1\.0550e+14\|114960937\|6386718' --include=*.py --include=*.md .
out    floatfea/tolerances.py:1990-1991  -- DELETED as false. Site 1 of 3. DONE.
out    docs/milestones/F4.md:348         -- STILL THERE. Site 2 of 3.
out    tests/verification/rung4/test_f4_static_and_mapping.py:549 -- STILL THERE. Site 3 of 3.
out    tests/verification/rung4/test_f4_static_and_mapping.py:520 -- a fourth, same arithmetic.
out    (CLAUDE.md:274 and docs/SUPERVISOR.md:438 quote the figure AS WRONG. Correct.)
```

R682's closing condition named three sites and I said so again in verdict 97 ("R682's
condition names three sites"). One was answered. This is R691.

## Findings

**R691. (b, blocking) R682's FALSE ARITHMETIC IS DELETED FROM `tolerances.py` AND LEFT
STANDING IN THE PLAN ROW THAT IS THE SAME COUNTER'S LOCATED JUSTIFICATION -- BY THE SAME
COMMIT, IN A TABLE THAT COMMIT EDITED TWO LINES ABOVE.**
`docs/milestones/F4.md:348` and `tests/verification/rung4/test_f4_static_and_mapping.py:549`
(and `:520`). The plan row reads `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 | ... R663's
mu L^2 / 12 over the root moment -- exactly 1/18 on a platform arm, measured 5.555556e-02,
bracket 1.0550e+14x`. `floatfea/tolerances.py:1990` now says of that exact sentence:
"**Both halves are false and they are deleted rather than left standing while the repair
waits (ES2)**", and gives `1/19` and `1/24` as the ratios in the gate's own denominator.
**The two authoritative locations for this counter's justification now contradict each
other inside one commit**, and `docs/SUPERVISOR.md` item 4 is the reason that is (b) rather
than prose: a tolerance change needs "a justification located in `docs/milestones/F<n>.md`
or the closure artifact", and a justification known by the same commit to be false is a
missing one. I checked the arithmetic rather than taking either side: if the correct root
moment is `M` and the defect adds `M/18`, then `(M/18)/(M*19/18) = 1/19` exactly --
`tolerances.py` is right, the plan row is wrong, and `1/18` is the ratio against the
CORRECT root moment, which is not the quantity the assertion divides by. The plan row's
`1.0550e+14x` bracket is the same figure verdict 96 measured as `9.9950e+13` against the
injected member and `7.9127e+13` against the worst. `test_f4_static_and_mapping.py:549` is
worse than stale, because it names the right denominator and the wrong number: "against the
DEFECTIVE root moment this ratio uses is 1/18 of the root moment on a platform arm."
Nothing caught this: `tests/test_plan_matches_tolerances.py` compares the row's VALUE
against the declared constant and never reads the row's prose.
**Closed when** `docs/milestones/F4.md:348`, `test_f4_static_and_mapping.py:549` and `:520`
each carry the `1/19` / `1/24` figures or no figure at all, and the `1.0550e+14x` bracket is
re-measured or withdrawn. This is basis-INDEPENDENT -- the deleted claim does not depend on
`f`, only the VALUE does, and the hold on the value stays accepted. **OR** each of the three
sites is named in the next revision with the sentence saying it was left and why, which is
the branch `CLAUDE.md` section *A closing condition that names sites* offers. What I will
not accept a third time is R682 reported as answered on its prose branch while two sites
carry the sentence.

**R692. (c, blocking) `compared > 0` IS R689's CLOSING CONDITION MINUS ITS COUNT. ALL
SIXTEEN DEGRADED ROWS STILL READ GREEN AND I SOLVED THE THRESHOLD.**
`tests/verification/rung4/test_f4_static_and_mapping.py`, the `assert compared > 0` at
`:865-871` inside `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`. Measurements in
section 4: the all-zero row now reddens (the half verdict 96 asked for, and it is real --
I reproduced the control green and the injection red), and every one of the sixteen
single-block rows reads GREEN at **2 of 10 channels compared** for the twelve buoy joints
and **4 of 10** for the four hub joints. Solving the rule rather than sampling it,
`compared > 4` is the smallest threshold at which every degraded row reddens; the shipped
`> 0` sits four below it, and `> 1` buys nothing at all. The gate's coverage therefore
still rests entirely on `_synthetic_lam` being dense in all sixteen blocks -- the
`:769`-class sentence my R689 named as the CW0 shape -- and that premise is still asserted
in prose and checked nowhere.
**Closed when** the assertion is `compared == 10` (or the equivalent all-sixteen-blocks
density check) with the `2 of 10` / `4 of 10` figures and the `compared > 4` boundary
pasted as what it prevents. One character of the assertion, and it makes the `:769`
sentence true by assertion in the same edit, which is what I asked for the first time.

**R693. (b, blocking) THE NEW COUNTER'S BRACKET IS PUBLISHED AS `2x` AND MEASURES
`1.0857x`, AND THE SENTENCE SAYING NO MEASUREMENT CAN CHANGE THAT RATIO IS REFUTED BY
ONE.**
`floatfea/tolerances.py`, the `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` entry: "**Twice the
ceiling, which is the most a printing-precision window can ever be bracketed by**: the
ceiling is half a unit and the counter is one unit, and **no measurement can change that
ratio**." The counter-to-ceiling ratio IS 2.000000 and that arithmetic is right. It is not
the bracket. This repository's own usage of "bracket" is the margin by which the gate
DETECTS the counter -- the deleted sentence four entries above used it that way ("The
bracket is 1.0550e+14x"), and so does every other entry in the table. Solved, not sampled:

```
cmd    python <scratch>/tol_boundary.py
rule   the counter-case asserts, for all four channels,
       abs(exact - (published + C)) > F4_INTEGRATOR_SPEC_AGREEMENT
out    clean abs(exact - published): alpha_f 4.210526e-06   alpha_m 2.631579e-06
out                                  beta  -1.689751e-06    gamma  1.578947e-06
out    bisected boundary C* = 9.2105263e-06  ( = max|d| + ceiling; closed form confirms)
out    shipped counter 1.0e-5 clears C* by 1.085714x    <- THE DETECTION BRACKET
out    the entry claims the bracket is "twice the ceiling" = 2.0x
```

And the invariance claim, refuted by one measurement because `C* = max|d| + ceiling` and
`max|d|` is a property of the four exact values, not of the print precision:

```
out    rho_inf 0.90: max abs(exact - its own 5dp print) 4.210526e-06 -> bracket 1.0857x
out    rho_inf 0.20: 4.444444e-06 -> C* 9.444444e-06 -> bracket 1.0588x
out    rho_inf 0.00 and 1.00: max|d| = 0 -> C* = 5.0e-06 -> bracket 2.0000x
judge  a measurement does change that ratio, and the same table shows it ranging
       1.0588x to 2.0000x over the scheme's own parameter.
```

**EH4, both directions, which the hand-back's sweep took only one of.** It reported
`7.0e-6, 9.9e-6` reddening the counter-case; the BOUNDARY is `5.789474e-06`:

```
out    DIRECTION A (strengthening): the ceiling FALLS -> the clean gate trips below
out                    4.210526e-06 (4.2105264e-6 passes, 4.21e-6 RED)
out    DIRECTION B (the WEAKENING one): the ceiling RISES -> the counter-case stops
out                    detecting at 5.789474e-06 (5.7894e-6 detects, 5.79e-6 does not)
out    => the ceiling is PINNED into [4.210526e-06, 5.789474e-06], a band of 1.3750x,
out       and the shipped 5.0e-6 sits 86.4% of the way up its own legal band.
out    DIRECTION B2 (the injection RISES): counter 1e-5, 2e-5, 1e-4, 1e-2, 1.0, 1e6
out       -- all still "detected", NOTHING reddens. The counter is pinned only FROM BELOW.
```

**The ceiling's VALUE is right and I am not asking for it to move.** `5.0e-6` is the
principled half-unit, it is absolute on a genuinely dimensionless quantity so the absolute
form is correct and the entry says why, the two plan rows landed in the same commit, and
the band `[4.210526e-06, 5.789474e-06]` is the tightest bracket in this table. **What is
wrong is the arithmetic published about it**, and the entry is the only statement a reader
has of what that counter bounds.
**Closed when** the entry gives the detection bracket `1.0857x` with `C* = 9.2105263e-06`
named as the boundary, the invariance sentence is deleted or restated as the thing that IS
invariant (the counter/ceiling ratio of exactly 2, which is a definition and not a
bracket), and the ceiling's band `[4.210526e-06, 5.789474e-06]` is pasted so a later
reader sees it pinned from both sides instead of sampled from one. Section 6's third line
notes the separate sentence "That margin is thin BY CONSTRUCTION"; fold it into this edit.

## 6. RECORDED, NOT A CLOSURE LIST -- ES0 PUTS THE LIST OUTSIDE THIS CHECK

Three lines so they are not lost. **None of these holds the step and none is to be worked
through this round.** CZ0 classes them as closure items; I agree with the classification,
and I give the reasoning for the first because I was asked to rule on it.

1. **The dict is LEGITIMATE as to its four numbers, and it escapes the guard rather than
   being exempted by it.** `_COEFFICIENT_RANGES` at
   `test_f4_static_and_mapping.py:1017-1036`. Verdict 97 already ruled the numbers are not
   tolerances -- they bound a computed quantity, there is no slack -- so the FORM is right
   and the derivation in the docstring is correct and complete. **It is not a dodge.** The
   part the hand-back did not ask about is what I measured, with the flat literal and the
   module-level float NAME as controls so the probe carries its own failure:
   ```
   cmd  python <scratch>/probe_dict.py   (tests/test_no_tolerance_literals.py::offending)
   out  CAUGHT  bare literal                               <- control
   out  CAUGHT  module-level float NAME (the :497 clause)  <- control
   out  MISSED  module-level DICT of floats, unpacked
   out  MISSED  assert residual < RANGES["r"]              <- a REAL tolerance, subscripted
   out  MISSED  module-level TUPLE, indexed
   out  MISSED  LO, HI = 3.7e-9, 2.2e-3   then   LO <= v <= HI
   out  MISSED  the SHIPPED shape, verbatim
   ```
   So it is invisible to the guard, which is a different and larger thing than a dodge: the
   `:497` clause exists because "a module-level `NAME = <float>` used as a threshold is a
   local literal wearing a name; the indirection is the point of the clause", and a
   container is the same indirection one level down. The docstring routes unread species to
   `tests/test_marker_exemption_corpus.py`; grepping that file for dict, tuple, container
   or subscript returns nothing, so the routing claim does not cover this form. **DR1
   forbids extending the guard and I am not asking for that.** The repair that costs one
   line and no apparatus: a `not-a-tolerance:` marker on the dict assignment, which
   restores the audit trail a reader greps for. It is free -- there is no unused-marker
   guard, so an unconsumed marker is simply ignored.
2. **`test_R653_the_coefficients_are_the_CLOSED_FORM_at_the_declared_radius` does not check
   a closed form and checks nothing AT the declared radius.** `:1114`. R687's condition is
   MET and this is not it reopened. Measured against nine wrong closed forms: the range
   gate catches 6 and is blind to 3 -- `beta = 1/(1+r)` with the square dropped, the
   Newmark trapezoid `beta=0.25, gamma=0.5`, and `alpha_m = (r-1)/(r+1)`. The spec pin
   above it catches all nine, so the pair's reach is the pin's reach. The name states a
   property the test cannot fail on, which is the shape R686 was, one finding earlier.
   Renaming it to what it asserts costs one line.
3. **Two sentences, and one claim I could not reproduce.** "Per-channel drifts reproduce
   yours" in the hand-back -- a different quantity from my four, and both sets are right
   (section 3). And `tolerances.py`: "That margin is thin BY CONSTRUCTION" of the
   `1.1875x` -- the margin is `ceiling / max|d|` and `max|d|` is measured, giving `inf` at
   `rho_inf` 0 and 1, `1.1250x` at 0.2/0.5/0.8, `1.1875x` at 0.9. It is thin by
   measurement. BG0; fold into R693. **Not reproduced:** the `black`-moves-the-marker
   fragility the hand-back flagged. I built a marked assertion long enough to force a
   reflow; `black -l 100` left the marker on the comparison's line and `offending()` read
   CLEAN before and after. Recorded as unverified, not as refuted -- a different shape may
   do it.

## Carried

Verdict 97 left **five findings and two carried items** open. Every one, with status:

* **R686 -- ANSWERED.** Section 3, reproduced in both directions plus the deleted-key case.
  `integrator.py:rho_inf_from_deck`, `scripts/report_joint_reactions.py:77`,
  `test_f4_static_and_mapping.py:1058-1112`. My figure to beat was `212 passed` with the
  deck at `0.9`; it now reddens. **Closed.**
* **R687 -- ANSWERED on branch A, as offered.** Both false sentences out of both sites; the
  ranges `[0.25, 1.0]` and `[0.5, 1.5]`, the two closed forms and the crossovers
  `sqrt(2)-1` and `1/3` all pasted; `rho_inf = 0.2` walked. **Closed.** The name is
  section 6 item 2 and is not this item.
* **R688 -- ANSWERED on the branch it took.** `F4_INTEGRATOR_SPEC_AGREEMENT = 5.0e-6`
  declared, counter declared, two plan rows in the same commit, "exact" gone. **Closed**,
  and the bracket arithmetic inside the answer is **R693**.
* **R689 -- HALF ANSWERED. STILL OPEN as R692.** The all-zero vacuity is closed and
  reproduced; the COUNT conjunct is not, and I solved the threshold.
* **R690 -- STILL OPEN, NOT HELD** (it never was). Grepping
  `docs/milestones/F4.md` for ER0, ER1, ER2, EQ2, EQ3 and EQ4 still returns nothing, and
  the only plan change in this range is the two section 5a rows. ES0 and ES2 have now
  joined the list of directives I can read only through a hand-back -- ES0 is in the
  repository, which is why I could verify it in section 1; **ES2 is not.** Unchanged in
  substance: the text goes in before ER1(d) derives anything from the new basis.
* **R682 -- STILL OPEN, AND NOW ALSO R691.** The hold on the VALUE stays accepted
  (basis-dependent through `f`, ER0 moves `f`, ER2's ordering is right). The
  basis-INDEPENDENT half was taken at one of three named sites. Section 5.
* **R685 -- STILL OPEN, hold accepted without reservation.** `tolerances.py` is untouched
  for it in this range and nothing about it has moved. Not held.

Closure items C161 to C173 and the earlier C-items: **not reviewed this round.** ES0
excludes the closure list from an interim check, and I did not look at them.

## Tolerances touched

```
cmd    git diff 488f2d8..HEAD -- floatfea/tolerances.py
out    two new entries, one deleted justification paragraph, and nothing else.
out    No existing VALUE moved -- the diff contains no changed `Final[float] =` line.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_INTEGRATOR_SPEC_AGREEMENT` | none | `5.0e-6` | absolute, dimensionless -- correct here; the quantity is a pure number and the entry says there is nothing to be relative to | `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | `docs/milestones/F4.md:346`, same commit; entry at `tolerances.py:2007-2026` | **VALUE ACCEPTED.** Band `[4.210526e-06, 5.789474e-06]` solved in both directions, `1.3750x`, the tightest in this table. Passes the unit-scaling question non-vacuously because the quantity is genuinely dimensionless. The published bracket is **R693**. |
| `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | none | `1.0e-5` | dimensionless, one unit in the fifth printed place | is the counter; injected by `test_R653_a_COEFFICIENT_WRONG_IN_THE_LAST_PRINTED_PLACE_reddens_the_gate` | `docs/milestones/F4.md:347`, same commit | **VALUE ACCEPTED** -- principled, not arbitrary, and it clears the boundary `C* = 9.2105263e-06`. **R693** on the bracket, the invariance sentence, and the absence of any upper pin (direction B2: it may rise to `1e6` with nothing red). |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.05`, unmoved | dimensionless | is the counter, still injected on one member | `docs/milestones/F4.md:348` -- **and that row is the false arithmetic the same commit deleted from `tolerances.py`** | **R691, blocking.** The `tolerances.py` paragraph is now correct and candid, and I say so: deleting a false sentence rather than leaving it standing while the repair waits is the right call and it is what I asked for. It was done at one site of three. |

## Next step opens when

**STEP 2 STAYS OPEN. This check counts against NO round, so verdict 97 remains round 1 of
three and TWO REVISIONS REMAIN.** Step 3 does not begin. ER1's six FloatSim re-runs may
proceed -- that is the whole point of ES0 and I am not obstructing it -- but these three
are answered in the same revision that carries ER1, before its own work is read:

1. **R691** -- `docs/milestones/F4.md:348`, `test_f4_static_and_mapping.py:549` and
   `:520`, **each named with its hunk or with the sentence saying it was left and why**.
   Basis independent; three edits. **My figures: `1/19` on a platform arm and `1/24` on a
   hub, in the gate's own denominator; `1/18` is against the correct one; the
   `1.0550e+14x` bracket measured `9.9950e+13` and `7.9127e+13`.**
2. **R692** -- `compared == 10` (or the all-sixteen-blocks density check) in
   `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`, **not** in the sparse test,
   which already has one. **My figures to beat: 16 of 16 single-block rows GREEN, minimum
   2 of 10 channels compared, boundary at `compared > 4`.**
3. **R693** -- the detection bracket `1.0857x`, the boundary `C* = 9.2105263e-06`, the
   ceiling's band `[4.210526e-06, 5.789474e-06]`, and the invariance sentence deleted or
   restated. Fold section 6 item 3's "thin BY CONSTRUCTION" into the same edit, because
   BP0 says a figure whose rule moved is regenerated in the commit that moves it, not the
   next.
4. **R682, R685, R690** -- carried, unchanged in substance. R690's text in the repository
   before ER1(d) derives anything from the new basis; **and ES2 with it**, since I have
   now judged two commits citing a directive that exists nowhere I can read.
5. **EG3(ii)** -- the report-guard files run AT my verdict commit and the counts pasted.
   The expected reds are EH1's state (2) list and nothing else; any red outside it is CZ1
   (iv) unchanged. **My figure at `4615498`: 32 failed, 2988 passed, 0 skipped, all 32
   traced in section 2.**

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION.** R691 reported answered with one or two of
the three sites touched -- the rule is site by site and this is its third instantiation in
four verdicts, so the next revision lists all three by path and line whatever their
disposition. A count assertion for R692 that is a floor rather than the count: `> 1`
through `> 4` are all still vacuous on 4 of 16 rows or more, and I have pasted the table.
And for R693, a replacement bracket figure taken before the final edit to the entry -- CP3
is the rule, and this round's one blocking tolerance finding is a bracket arithmetic
inside a repair, which is CP2's recorded shape for the fourth round running.

## On ES0's scope -- said once, and it leaves the loop

**I agree with ES0 and this is the once I say so.** The exemption keys on whether a new
report revision exists, which is a fact a machine can check and which distinguishes "the
work reached a reviewable state" from "a turn ended". That is a better discriminator than
the one I was applying in verdict 97, and the revision count answers DK0 cleanly.

One limit, recorded as an observation and not as a HOLD or a request. An interim check
reads a tree that **no report describes**, so every claim about it is one I had to
construct a command for rather than check against a written one, and three of this round's
five judgements came out of measurements the hand-back did not contain -- R691's third
site, R692's threshold, R693's boundary. That is more reviewer work per unit of code, not
less. If interim checks become frequent, the honest accounting is that the saving is in
the ROUND COUNT and not in the reading, and the thing that would recover it is cheap: a
hand-back for an interim check could carry the `claim/cmd/out` triples for the repairs it
describes, which this one largely did, and the boundary solved in both directions, which
it did not. Nothing follows from this; it goes to Xabier through the implementer if it is
worth anything.

## On the schedule

The three blocking items are, between them, one assertion operator, three prose edits and
one re-measured bracket -- a few hours, and none of them touches ER1. **ER1's two days are
not threatened by this verdict and should start now, in parallel.** I see no slippage to
report that the hand-back has not already reported.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: 4f99c7f6a3e446bc183b67bf0c77b91596e367c5
Verdict: HOLD
**Reviewed commit: `7cee09f`.** (`7cee09fdaac615519fe0da08c09d018f7438d0de`, HEAD of F3
at invocation, pushed.) My corpus commit `4f99c7f` lands first, so the script's
`Reviewed commit:` stamp and the judged commit differ; DU1 says restate the judged one
and this is it. The range is `5786bed..7cee09f` -- three commits.
Tests: 3022 passed, 8 failed, 0 skipped   (MY OWN run, ONE invocation, no `--ignore`,
no deselection, no `-k`, in the repository itself, 636.92s. I did not accept a count
from the report. **All eight are EG3 state (1) and traced by name in section 3.**)
**CI at the reviewed commit: run `37482781971` at `7cee09f`, conclusion FAILURE --
`the verification ladder: success` at every step including `ladder 4` and `ladder 5`;
`lint, unit and guards: failure` at `guards and meta-tests` ONLY, with `8 failed, 1038
passed`, and the eight are the same eight. `actionlint`, `ruff`, `black --check`,
`mypy` and `unit tests` all success.**

## Round of 2026-10-06 -- NINETY-SEVENTH verdict. F4 step 2, FIRST round of three.

**HOLD, and the first thing in it is the answer to the question I was asked, because the
implementer asked for it now rather than at the third verdict.**

**THIS ROUND COUNTS. It is step 2's first of three.** EB4's exemption is written for "a
verdict spent on a STOP or blocker whose resolution belongs to the supervisor or to the
user", and its second sentence limits the carry to POST-CLOSURE verdicts that judge
implementer work. Neither clause fits. This verdict judges three commits of step-2
implementer work -- `9985bcd`, `b979b68`, `7cee09f` -- and every finding in it is the
implementer's to fix. The OCCASION was a hook; the SUBJECT is the work, and EB4 keys on
the subject. Reading it the other way is the shape DK0 already rejected for plan
re-locks: if a mid-step commit bought a free round, every mid-step commit would buy one
and the cap would mean nothing.

**I think the mechanism that forced this round is wrong, and that is a separate
statement, made once, under its own heading at the end.** It goes to Xabier through the
implementer. It is not a HOLD on anything and the count above stands until he rules.

**R683 and R684 are substantively ANSWERED and I reproduced each by ablation rather than
accepting it** -- one red each, the right one, over the whole of rung 4. R653's FORMULA
half is answered and I checked the reference's own derivation independently. **The four
blocking items are all inside the new work, three of them inside R653's own answer**,
which is CP2's recorded shape for the third round running: the attention goes to the
thing being fixed and the apparatus built around the fix inherits none of the discipline
being applied to it.

**No STOP.** ER1(c)'s STOP condition does not fire -- I reproduced all five bodies PSD
at `f = 0.75` with `admissible()` itself (section 5). The ladder is green at every rung
in CI. And `9985bcd` is the permitted form for touching my own instructions, which I say
plainly because I was asked: section 2.

## 1. THE DIFFS, EACH ONE SEPARATELY, AS MY INSTRUCTIONS ORDER THEM

```
cmd    git log --format='%h %s' 5786bed..HEAD
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), ...
out    b979b68 F4 step 2: R683, R684 and R653 -- EQ2's basis-independent half
out    9985bcd process: EQ0 -- a closure commit that changes a gate or a tolerance ...
cmd    git diff --stat 5786bed..HEAD
out    CLAUDE.md 40, docs/SUPERVISOR.md 40, docs/milestones/F4.md 2,
out    docs/reports/F4/step-2-answers.json 81, docs/reports/F4/step-2.md 715,
out    floatfea/io/integrator.py 72, scripts/report_joint_reactions.py 37,
out    tests/verification/rung4/test_f4_static_and_mapping.py 228.
out    EIGHT files, 1171 insertions, 44 deletions.
cmd    git diff 5786bed..HEAD -- floatfea/tolerances.py          [instruction 4]
out    (no output) -- NO TOLERANCE MOVED. The implementer's section 11 is confirmed at
out    the level that matters, and I diffed it separately because that is where the
out    cheapest wrong fix lands.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"  [instruction 4c]
out    tests/conftest.py                             -- the instruction is intact
cmd    git diff 5786bed..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (no output). And I read all 228 changed lines of the rung-4 file: NO
out    `pytest_runtest_makereport`, no `pytest_ignore_collect`, no
out    `pytest_collection_modifyitems`, no hookwrapper, no plugin. Nothing the
out    ladder's gate reads was rewritten from inside a rung.
cmd    git diff --stat 5786bed..HEAD -- .claude docs/SUPERVISOR.md   [instruction 4b]
out    docs/SUPERVISOR.md | 40 ++++ -- and the whole of it is in `9985bcd`. Section 2.
cmd    git diff --name-only 5786bed..HEAD -- docs/reviews
out    (no output) -- no commit in this range touches a verdict.
```

**INSTRUCTION 1b, THE ONE COMPARISON.** The report header reads
`Answers: verdict 96 @ 5786bed`. `5786bed` IS verdict 96's own commit -- `git log
--oneline -1 5786bed` gives `review: F4 step 1 CLOSURE COMMIT -- ninety-sixth verdict`
-- and verdict 96 is the newest verdict in the repository. **The header names the LATEST
verdict and it names the verdict's own commit, not the commit it judged (DX2/C13). No
HOLD on 1b.**

## 2. MY OWN INSTRUCTIONS -- `9985bcd` IS THE PERMITTED FORM. NOT A STOP-CLASS FINDING.

I was asked to confirm this and the answer is yes, with the reading rather than the
assurance. I read the whole 80-line diff line by line.

```
cmd    git show --stat 9985bcd
out    CLAUDE.md 40 +, docs/SUPERVISOR.md 40 + -- 2 files, 80 insertions, 0 deletions
rule   CLAUDE.md "the reviewer's own instructions are not edited inside a step": a
       standalone `process:` commit that CITES the directive asking for the change, and
       never a commit that also touches `floatfea/` or `tests/`
judge  STANDALONE: two files, nothing in `floatfea/`, nothing in `tests/`. CITES: the
       message names EQ0 in its first line and quotes the directive's wording.
       PURELY ADDITIVE: zero deletions -- so NO GUARD WAS REMOVED, which is the one
       thing this rule exists to catch and the one thing a green suite cannot see,
       because nothing in the suite reads either file. The inserted text is the
       ninety-sixth verdict's own proposal, unparaphrased, at the same anchor in both
       files. **PERMITTED FORM. Not a STOP.**
```

One observation and not a finding: the clause I proposed was adopted in my wording, and
it is now the rule that this very round is NOT an instance of. EQ0 is about closure
commits. `b979b68` is a step commit.

## 3. THE EIGHT REDS AND THE RED CI, TRACED BY NAME (EG3(i), CA2)

**CI IS RED AT THE REVIEWED COMMIT AND IT IS NOT A HOLD, because every red traces by
name to EG3 state (1).** I matched each `FAILED` id to the state's own list rather than
ruling them as a family, which is the discipline EG3(i) exists to force.

```
cmd    gh run list --commit 7cee09f...  ; gh run view 37482781971 --json jobs
out    JOB the verification ladder: SUCCESS -- ladder 1,2,3,6,4,5 all success
out    JOB lint, unit and guards: FAILURE -- actionlint, ruff, black --check, mypy and
out        unit tests ALL SUCCESS; `guards and meta-tests` FAILURE
out    JOB CI determinism -- leg: skipped       (workflow_dispatch only)
out    JOB CI determinism -- ten legs agree: skipped   (workflow_dispatch only)
cmd    gh run view 37482781971 --log-failed | grep FAILED
out    8 failed, 1038 passed -- and the eight ids are the eight below
cmd    python -m pytest -q      [my own run, one invocation]
out    8 failed, 3022 passed, 2 warnings in 636.92s
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    FAILED tests/test_report_guard_states.py::...[baseline]
out    FAILED ...[non_numeric_step_suffix]
out    FAILED ...[superscript_digit_step_number]
out    FAILED ...[draft_suffix_beside_a_step_report]
out    FAILED ...[step_number_is_the_empty_string]
out    FAILED ...[verdict_amended_after_the_commit_the_report_answers]
out    FAILED ...[zero_padded_step_number]
rule   EH1: state (1) is `test_the_guard_reads_the_step_being_worked_on` plus the
       planted states that cascade off a red baseline, identified by the baseline being
       red and by each cascading state's OWN failure line
judge  ONE is the named test. The other SEVEN each print, inside their own nested run,
       `FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked
       _on -- AssertionError: step 2 has a report and no verdict yet` and
       `1 failed, 217 passed`. `[baseline]` is red, so the cascade is identified the way
       EH1 says. **NOT ONE RED IS OUTSIDE THE LIST.** The literal-guard red that
       `b979b68` shipped is GONE at this commit, confirmed by CI and by my own run:
       `tests/test_no_tolerance_literals.py` appears in neither failure list, and
       `pytest tests/test_no_tolerance_literals.py tests/verification/rung4 -q` gives
       `212 passed in 1.21s`.
```

**The three states, kept distinct (CK2).** The two determinism jobs are `skipped`, and
they are `if: github.event_name == 'workflow_dispatch'` in `.github/workflows/ci.yml:90`
and `:213` -- so they are skipped BY DESIGN on a push and not by an exhausted allowance.
That makes them **unmeasured at this commit**, which I record rather than step over.
Nothing in this range touches `.github`, so the last dispatch result still describes the
tree.

**EG3(ii) -- I measure state (1) clearing at MY verdict commit and the next revision
pastes it.** That is the half no verdict in this milestone had measured until verdict 96
asked for it, and this is the second time it is being taken.

## 4. THE RED `b979b68` SHIPPED, AND THE EXEMPTIONS I WAS ASKED TO RULE ON

**The mechanism the implementer reports is correct and the self-diagnosis is the right
one** -- a count taken over `tests/verification/rung4` cannot speak for a guard that is
not in that directory, and the revert that removed R682's edits is what put the literals
back. I confirm CI found the same three, to the line number, at the same commit.

**NOW THE RULING, because three exemptions were asked about and the answer is not the
same for all three.**

**`0.05263` -- LEGITIMATE.** It is the EXPECTED side of a comparison, read out of
`docs/load-interchange-v1.md:259`, which publishes it. An expected value is not a
tolerance: there is no slack in it to widen. Marker accepted.

**`0.8` -- LEGITIMATE AS AN EXEMPTION.** It is an INPUT to the integrator and the
quantity the assertion pins, not a bound on one. Marker accepted. **The assertion it
sits in is R686 for a different reason.**

**`0.5` and `1.0` -- THE LITERALS ARE NOT TOLERANCES AND THE REASON GIVEN FOR THEM IS
FALSE.** That is R687, and it is blocking.

**AND THE ONE REAL TOLERANCE IN THIS GATE IS THE ONE NOBODY MARKED.**
`round(getattr(got, name), 5) == published` is a comparison epsilon written as a
rounding, and `CLAUDE.md` names "comparison epsilons" explicitly. The report says "NO
TOLERANCE IS DECLARED and none is wanted ... compared at five decimal places, which is
exact". **It is not exact. I solved it.** That is R688.

## 5. ER1(c) -- NO STOP, AND I REPRODUCED IT WITH `admissible()` RATHER THAN READING IT

The report's figures are generated by `scratchpad/er1c_stop.py`, which is not in the
tree, so no figure in its section 3 is regenerable at this commit. **So I took every one
of them myself**, from the deck YAML with ER0's override applied to an in-memory copy,
through `build_superstructure(mass_fraction=0.75)` and `admissible()`.

```
cmd    my own probe: deck platform mass 10.0 -> 20.0, Ixx/Iyy/Izz 10/10/20 -> 20/20/40,
       reference_point untouched; build_superstructure(path=..., mass_fraction=0.75)
out    platform  admissible=True  m_rem=6.250000e+05
out       eig = 4.666294e+09, 4.666294e+09, 1.093623e+10   slack = -1.603643e+09
out       link = 41.326086   rem_pos = [3.4e-15, -3.0e-15, 65.9946]
out    hub1..4   admissible=True  m_rem=3.750000e+05
out       eig = 3.792032e+07, 3.792032e+07, 7.736354e+07   slack = -1.522913e+06
out       link = 0.000000    rem_pos = [+-50, 0, 24.6685]
rule   ER1(c): if any body is not PSD at 0.75, STOP and report
judge  **NO STOP. Every figure the report publishes reproduces to every digit it
       prints**, and I called `admissible()` itself rather than re-implementing the
       test, so this is the shipped decision and not a second opinion about it.
```

**THE LINK-LENGTH CLAIM IS CORRECT AND SO IS THE REASON GIVEN FOR IT**, which I checked
rather than accepting, because a causal sentence carries its cell (BG0).

```
cmd    the same probe on BOTH decks, f = 0.75, only the platform mass and inertia moved
out    new basis: |link| = 41.326086 m, m_remainder = 6.250000e+05
out    old basis: |link| = 41.326086 m, m_remainder = 3.125000e+05
cell   geometry, reference point, joints and f all held; mass and inertia alone moved
judge  CORRECT, and the algebra says why: the remainder position solves
       `M x_cog = f M x_member + (1-f) M x_rem`, so `x_rem = (x_cog - f x_member)/(1-f)`
       and `M` cancels. The position is independent of the TOTAL mass at fixed `f`, which
       is a stronger statement than "linear in mass" and is the one that holds.
```

**The equivalent densities reproduce exactly too**: platform `7145.965` (`7146.0`), hubs
`11433.545` (`11433.5`), old basis platform `3572.983` (`3573.0`), new basis at the
ladder default `4763.977` (`4764.0`) with hubs `7622.363` (`7622.4`). The report's
reading -- the sizing question has moved to the hubs -- is confirmed.

**AND ONE THING THE REPORT DOES NOT SAY, which will decide whether ER0 can ship at
`f = 0.75` at all.** `f = 0.75` is OFF `MASS_FRACTION_LADDER`, whose largest rung is
`0.5`, so the builder itself records a finding at every body:

```
cmd    my own probe: build_superstructure(mass_fraction=0.75).findings, both decks
out    NEW basis, f=0.75: 9 superstructure findings
out      platform x1: "the mass fraction is 0.75, handed in by the caller rather than
out        taken from (0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never
out        consulted for it. This body is a MEASUREMENT, not one to ship."
out      hub1..4 x2 each: the same, PLUS "the equivalent density is 11433.5 kg/m^3,
out        ABOVE steel at 7850"
out    NEW basis, ladder (f=0.5): 0 findings, platform 4763.977, hubs 7622.363
out    OLD basis, f=0.75: the same 9 findings
judge  `admissible()` returning True and the SHIPPED builder admitting the fraction are
       two different statements, and the builder's own words for `f = 0.75` are "not one
       to ship". ER0 at `f = 0.75` therefore needs either a ladder that contains 0.75 or
       an explicit decision to ship a configuration carrying nine findings, and the hub
       section is the thing the density finding points at. NOT a blocking finding at this
       commit -- nothing is implemented -- and recorded now because it is cheaper to
       settle before ER1(d) derives eight expected values on top of it.
```

**ER1(d)'s eight static figures: all eight confirmed by hand, independently.**
`20.0*125000*9.81/4 = 6,131,250`; `0.75*2.5e6/4*9.81 = 4,598,437.5`; difference
`1,532,812.5`; `6,131,250*50 - 4,598,437.5*25 = 191,601,562.5`. Hub side:
`12.0*125000*9.81 = 14,715,000`, `+6,131,250 = 20,846,250`, `/3 = 6,948,750`;
`0.75*1.5e6/3*9.81 = 3,678,750`; difference `3,270,000`;
`6,948,750*25 - 3,678,750*12.5 = 127,734,375`. And the INPUTS are the deck's own:
`platform mass 10.0`, `hub mass 12.0` at model scale, read out of
`data/platform/platform12_deck.yaml`. Nothing to correct.

## 6. R683 AND R684 -- BOTH ABLATIONS RUN BY ME, ONE RED EACH, THE RIGHT ONE

I did not accept either ablation. I made each change in the tree myself, ran the WHOLE of
rung 4 rather than a `-k` subset, and restored the file.

```
cmd    `_body_errors` replaced by the AGGREGATE form (sum got and want over the five
       bodies, then normalise), every injection and the lam row held; pytest
       tests/verification/rung4 -q -rf
out    1 failed, 156 passed in 1.05s
out    FAILED ...REDDENS_on_a_wrong_sign_and_on_a_wrong_node[internal_joint_dropped]
out    AssertionError: the `internal_joint_dropped` injection reads 2.082021e-16, which
out    the ceiling ACCEPTS
cell   ONE VARIABLE MOVED -- the normalisation scope. Nothing else touched.
judge  **R683 IS ANSWERED.** The row exists, it is the only one that distinguishes the
       two forms, and the per-body rule is now held in place by something in the tree.
       The gate carries its own failure.
```

```
cmd    `assert f_scale > 0.0 and m_scale > 0.0` reinstated at the head of
       `_one_body_error` -- the form C158 shipped; pytest tests/verification/rung4 -q -rf
out    1 failed, 156 passed in 1.08s
out    FAILED test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked
judge  **R684 IS ANSWERED ON ITS FIRST HALF**, and the false sentence is deleted rather
       than rephrased, which was the second conjunct of its closing condition. The COUNT
       conjunct is not done and that is R689.
```

**AND THE ABSOLUTE BRANCH IS THE RIGHT FORM, which I say explicitly because I asked for
it and it would be easy to get wrong.** I attacked it four ways:

```
cmd    my own probe: leak eps onto `hub2`'s force, buoy1-only row (hub2 expected == 0)
out    eps = 5e-324 (one denormal) -> RAISES.  1e-300 -> RAISES.  1e-12 -> RAISES.
out    1.0 -> RAISES.  pure MOMENT leak 1e6 N.m -> RAISES on the moment branch.
out    equal-and-opposite force pair on two different nodes -> RAISES on the moment
out    branch, because cross(x, F) does not cancel when the points differ.
rule   `np.all(got == 0.0)`: the smallest detectable defect is one ULP
judge  **the strongest counter in this file, and the two channels are branched
       SEPARATELY** so a moment-only leak is not hidden behind a zero force check. The
       only miss is a signed `-0.0`, which carries no load; recorded in the corpus so a
       later tightening is a decision rather than a surprise.
```

## 7. R653 -- THE FORMULA HALF IS ANSWERED. THE CONSTANT HALF IS A TAUTOLOGY.

**First, the placement question I was asked: `floatfea/io/integrator.py` IS ACCEPTABLE
and DR1 does not reach it.** DR1 freezes "guards, scanners, meta-tests, detectors and
report generators". This module is neither -- it is a closed-form coefficient derivation
and the scheme parameter, on the FE side's read path, and `floatfea/io/reader.py:50`
already requires the same five fields from every record. It is production code in the
right package. Accepted, and I would not have accepted it in `tests/`.

**Second, the reference, verified independently of the implementation (my recorded guard
is that the reference has been wrong more often than the thing measured).**

```
cmd    my own evaluation of Chung & Hulbert (1993) eqs (25)-(27) at rho_inf = 0.9, and
       the closed forms beta = 1/(1+rho)^2 and gamma = 1/2 + (1-rho)/(1+rho)
out    alpha_m 0.4210526315789474  alpha_f 0.4736842105263158
out    beta    0.2770083102493076  gamma   0.5526315789473684
out    rounded to five places: 0.42105, 0.47368, 0.27701, 0.55263
rule   docs/load-interchange-v1.md:259-260 publishes exactly those four, and line 52 of
       the same file points at sec.4.1 for the block
judge  **THE REFERENCE IS RIGHT, THE FORMULA IS RIGHT, AND THE TWO AGREE.** The
       difference `alpha_f - alpha_m = (1-rho)/(1+rho)` gives `0.0526315...` -> `0.05263`,
       the figure the specification singles out. The report's section 4 citation is
       correct (SECTION 4, lines 259-260); the two in-tree citations are not, see
       Closure items.
```

**Third, and this is R686: the constant half asserts a literal against a copy of
itself, and the artifact that carries FloatSim's own value is in this repository,
unread.**

```
cmd    grep -rn "spectral_radius_inf" over the whole repository
out    data/platform/platform12_deck.yaml:26:  spectral_radius_inf: 0.8
out    -- ONE occurrence. Nothing reads it.
cmd    grep -rn "rho_inf" HSP-stable --include=*.py | grep "= *0\."
out    HSP-stable/floatsim/solver/newmark.py:222:    rho_inf: float = 0.9   <- DEFAULT
out    HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291:  rho_inf=0.8
judge  `0.8` IS the right number for this study and I verified it two independent ways.
       What nothing verifies is that the FE side's copy still equals it.
```

```
claim  the new gate cannot fail on the property its own name states
cmd    set data/platform/platform12_deck.yaml:26 to `spectral_radius_inf: 0.9` -- the
       exact disagreement C131's "429x louder" was about -- then
       python -m pytest tests/verification/rung4 tests/test_no_tolerance_literals.py -q
out    212 passed in 1.41s
rule   "A gate carries its own failure": break the claimed property and confirm the
       assertion goes red
judge  **GREEN. The deck, generated from HSP at the pinned tag and never hand-edited,
       may disagree with `FLOATSIM_RHO_INF` by any amount and nothing reddens.** The
       gate is a change-detector on its own literal, which is worth having and is not
       what its name, its docstring or the report claim for it.
```

## 8. TRY TO BREAK IT -- THE MAPPING GATE READS PERFECT ON A ROW IT MEASURES NOTHING IN

The adversarial case for this step is the one R684's repair created and nothing in the
step looks at: a lam row that sends bodies into the ZERO-SCALE branch. The new
`test_G4_4_a_LEGAL_SPARSE_row...` asserts `len(silent) == 4` and `norm(lam_row) > 0.0`,
so it is safe. **The PRODUCTION gate is not.**

```
cmd    my own probe: `_body_errors` over the buoy1-only row, per body
out    hub1 0.000e+00  hub2 0.000e+00  hub3 0.000e+00  hub4 0.000e+00
out    platform 0.000e+00     ->  error 0.000e+00, well inside 1.0e-12, GREEN
out    bodies compared RELATIVELY: 0 of 5
cmd    the same over an ALL-ZERO lam row
out    error 0.0 -> GREEN. The gate passes on a multiplier row that certifies nothing.
rule   "assertion domain blindness": check that the collection the assertion inspects
       can actually contain the failure
judge  **R689.** `_one_body_error` returns `0.0` for "compared and perfect" AND for
       "nothing to compare", and `max()` over the five cannot tell them apart. Four
       bodies took the absolute branch; `hub1`'s relative error is also exactly `0.0`.
       The production gate's coverage rests entirely on `_synthetic_lam` being dense,
       which a comment at `:769` claims and nothing asserts. This is the COUNT conjunct
       of R684's closing condition -- "so a sparse row reduces coverage visibly rather
       than erroring" -- and it is the half that is not done.
```

**Both directions on the boundary (EH4), including the two that weaken the gate.**

```
cmd    uniform gain (1+eps) on every mapped body, expected side held
out    eps 1e-13 -> 1.002e-13 GREEN ;  eps 1e-12 -> 1.001e-12 RED
cmd    the `internal_joint_dropped` share scaled by s -- the INJECTION falling
out    s = 5.7e-13 -> 1.013828e-12 RED ;  s = 5.6e-13 -> 9.959214e-13 GREEN
out    full strength 1.778481e+00, so the row survives a 1.8e+12x weakening
cmd    a single-component defect on the platform's SMALLEST force component
out    want force = [-636113.848, -1157231.570, -431368.634] N; the normaliser is the
out    component-wise MAX 1.157e6, not the 4.314e5 being tested, so +1e-6 N on Fz reads
out    8.641e-13 GREEN and detection starts near 1.16e-6 N -- a 2.68x dilution
judge  the ceiling is sound and its operating point is now stated. The dilution is not a
       defect; it is what "relative to the largest component" means, and it is recorded
       so the ratio is not read as a per-component bound.
```

**And the localisation R683's closing condition asked for, which the report does not
paste. I took it.**

```
cmd    the shipped `internal_joint_dropped` injection, per body
out    platform 1.778481e+00   hub1 3.896589e-01
out    hub2 1.795271e-16   hub3 2.092543e-16   hub4 1.634659e-16
judge  the residual localises to EXACTLY the two bodies the dropped joint touches and
       the other three sit at round-off -- matching the `1.795e-16 / 2.093e-16 /
       1.635e-16` I measured at verdict 96 to four digits. This is the evidence, and it
       is a closure item that it is in my file rather than in the report's.
```

## The adversarial corpus (BE3)

`tests/corpus/f4_mapping_zero_scale_and_coverage.txt`, batch 36, committed separately at
`4f99c7f`. **Fourteen entries, all unseen.** Under EG4(e) this is the F4 load-mapping
gate, which is one of the two standing exceptions to the corpus pause; the R653
integrator gate is outside that exception, so its measurements are in section 7 and not
in the corpus.

**COVERAGE: 8 of the 14 caught, 4 missed, 2 explanatory.** The eight caught include the
one-denormal leak on both channels, the equal-and-opposite pair, both solved boundaries
and both of my ablations. The four misses are the sparse row, the all-zero row, the
extra-body-absent-from-`want` route through `_mapping_error`, and a signed `-0.0`. The
first two are R689, the third is scoped to the three counter-cases and the new sparse
test (the production gate catches it at `set(loads) == set(n_dof_of)`), and the fourth is
harmless and recorded as such.

Batch 34 moved the WIRING and batch 33 the THRESHOLDS; this batch exists because R684's
repair created a third surface -- `_one_body_error` now has two branches and the LAM ROW
decides which one a body takes -- that neither earlier batch could have reached.
`python -m pytest tests/ -q -k corpus` gives `1361 passed, 1669 deselected` with the new
file in the tree.

## Findings

**R686. (c, blocking) `test_R653_the_value_the_DRIVER_reconstructs_with_is_the_declared_one`
CANNOT FAIL ON THE PROPERTY ITS NAME STATES, AND THE GENERATED ARTIFACT THAT CARRIES
FLOATSIM'S OWN `rho_inf` IS IN THIS REPOSITORY, UNREAD.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1016-1046` and
`floatfea/io/integrator.py:27`. The driver reads `RHO_INF = FLOATSIM_RHO_INF`
(`scripts/report_joint_reactions.py:77`), so "the value the driver reconstructs with IS
the declared one" is true by assignment and has no failure mode; the only thing the test
detects is an edit to `FLOATSIM_RHO_INF` that does not also edit the test literal.
Measured: `data/platform/platform12_deck.yaml:26` carries `spectral_radius_inf: 0.8`, it
is the ONLY occurrence of that key in the repository, nothing reads it, and setting it to
`0.9` -- the exact disagreement C131's "429x louder" figure was about -- leaves
`pytest tests/verification/rung4 tests/test_no_tolerance_literals.py` at `212 passed`.
The deck is generated by `scripts/export_platform_deck.py` from HSP at the pinned tag, is
round-trip-validated by its own generator, and its header says "DO NOT HAND-EDIT" -- it is
the one copy of this number with provenance and it is the one not compared.
`HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291` confirms `rho_inf=0.8` for
the study the driver replays, while `floatsim/solver/newmark.py:222` shows FloatSim's
DEFAULT is `0.9`, so "It is FloatSim's value, not a choice made here" is also imprecise:
it is this STUDY's value. The number now exists in three places -- the deck,
`integrator.py`, and the test literal -- and the two that are compared are the two the
same hand typed, which is C131's own finding re-instantiated by the commit that cites it.
**Closed when** `FLOATSIM_RHO_INF` is compared against a value READ from
`data/platform/platform12_deck.yaml` (`simulation.spectral_radius_inf`) instead of against
a literal, with the deck-at-`0.9` ablation re-run and pasted to show the gate now reddens;
the deck is already a shipped data file this rung reads, so this needs no HSP worktree and
no new apparatus. **OR**, equally acceptable to me: the literal stays, the test is RENAMED
to say it is a change-detector on the declared constant, its docstring drops the claim
that it pins what the driver reconstructs with, and the provenance becomes a
`claim/cmd/out` triple naming the deck line and the study line -- but then R653 is
answered by disclosure and the entry says which claim it is making.

**R687. (c, blocking) THE RANGE ASSERTION CLAIMS A PROPERTY GENERALIZED-ALPHA DOES NOT
HAVE, AND THAT FALSE SENTENCE IS WHAT EXEMPTS TWO LITERALS FROM `tolerances.py`.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1037-1046`:
`assert 0.0 < coefficients.beta < 0.5 and 0.0 < coefficients.gamma < 1.0`, with the marker
comment "0.5 and 1.0 are the mathematical ranges `beta` and `gamma` have for a dissipative
generalized-alpha step, which is a property of the scheme and not an agreement between two
measurements", and the message "which are outside the ranges a dissipative
generalized-alpha step has". Measured over the scheme's own parameter range `rho_inf` in
`[0, 1]`, from the closed forms `beta = 1/(1+rho)^2` and `gamma = 1/2 + (1-rho)/(1+rho)`
which I derived and then checked against the code at twelve values:
**`beta` in `[0.25, 1.0]` and `gamma` in `[0.5, 1.5]`.** `beta < 0.5` holds only for
`rho_inf > sqrt(2)-1 = 0.4142136`, and `gamma < 1.0` only for `rho_inf > 1/3`. At
`rho_inf = 0.2` -- a valid, more strongly dissipative step -- the shipped assertion calls
`beta = 0.694444` and `gamma = 1.166667` "outside the ranges a dissipative
generalized-alpha step has", which is false of both numbers. The two literals are NOT
tolerances and do not belong in `floatfea/tolerances.py`: they bound a computed quantity
rather than a window of agreement, so the exemption's FORM is right. Its REASON is false,
and the reason is the whole of what the marker offers a reader. The assertion also adds
nothing beside the exact pin above it, passing at `0.5`, `0.9` and `1.0` as readily as at
`0.8`.
**Closed when** either the assertion states the ranges the scheme actually has
(`0.25 <= beta <= 1.0`, `0.5 <= gamma <= 1.5`) with the two closed forms and the two
crossover values `sqrt(2)-1` and `1/3` pasted; **OR** it is replaced by the invariant that
holds for every `rho_inf` and would catch a wrong formula -- `beta` exactly
`0.25*(1 - alpha_m + alpha_f)**2`, `gamma` exactly `0.5 - alpha_m + alpha_f`, with
`alpha_m <= alpha_f <= 0.5` -- which is a stronger gate than the one shipped and needs no
literal at all; **OR** it is deleted with the reason recorded at the site. In every case
the false sentence goes from BOTH sites, the marker comment and the assertion message.

**R688. (b, blocking) `round(x, 5) == published` IS A COMPARISON EPSILON, THE TEST AND THE
REPORT BOTH CALL IT EXACT, AND I SOLVED IT.**
`tests/verification/rung4/test_f4_static_and_mapping.py:999-1013` ("the comparison is
against the value ROUNDED to five places, which is exact. A ceiling here would be a number
with nothing behind it") and `docs/reports/F4/step-2.md` section 6 ("NO TOLERANCE IS
DECLARED and none is wanted ... compared at five decimal places, which is exact").
`CLAUDE.md` names "comparison epsilons" among the things that are a tolerance under
another name, and a rounding comparison is one: it admits any drift that does not cross a
quantisation edge. Measured, per coefficient, the drift this assertion still accepts:
**`alpha_f` 7.895e-07** (exact `0.4736842105263158`, edge at `0.473685`), `alpha_m`
`2.368e-06`, `beta` `3.310e-06`, `gamma` `3.421e-06`; `5.0e-06` is the half-step and the
GOVERNING figure is the smallest of the four, not the nominal half-step, because a gate is
as sensitive as its weakest channel. On `alpha_f` that is `1.67e-06` relative. The gate is
strong and I am not asking it to be stronger; "exact" is false by six orders of magnitude,
and the four numbers that make it a measurement are nowhere in the tree.
**Closed when** either the half-width `5.0e-06` is declared in `floatfea/tolerances.py` as
a dimensionless tolerance justified by the specification's five-place print precision, with
the counter being the smallest coefficient drift the same assertion detects in the same
quantity -- `7.895e-07` on `alpha_f`, with all four per-coefficient figures pasted;
**OR** `round(..., 5)` stays and the word "exact" is deleted from the test docstring and
from the report, replaced by the measured per-coefficient window with `7.895e-07` named as
the governing one. Either is fine. What is not is a sentence saying there is no tolerance
here when there is one and nobody has measured it.

**R689. (c, blocking) THE PRODUCTION MAPPING GATE READS `0.000e+00` ON A ROW IT COMPARES
NOTHING IN, AND PASSES ON AN ALL-ZERO MULTIPLIER ROW. THIS IS THE COUNT CONJUNCT OF
R684's CLOSING CONDITION.**
`tests/verification/rung4/test_f4_static_and_mapping.py`, `_one_body_error` at `:760-791`,
`_body_errors` at `:749-757`, and
`test_G4_4_the_mapping_CONSERVES_the_joint_resultants` at `:807-847`. `_one_body_error`
returns `0.0` both for "compared relatively and perfect" and for "nothing to compare", and
`max()` over the five bodies cannot distinguish them. Measured: handed the buoy1-only row,
the production gate reads `error 0.000e+00` against `1.0e-12`, GREEN, with **0 of 5 bodies
compared relatively**; handed `np.zeros_like(lam_row)` it reads `0.0` and PASSES on a
multiplier row that certifies nothing. The new
`test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked` has both guards --
`assert float(np.linalg.norm(lam_row)) > 0.0, "the row is zero, so it tests nothing"` and
`assert len(silent) == 4` -- and the gate the plan's G4.4 row points at has neither. Its
coverage rests entirely on `_synthetic_lam` being dense in all sixteen blocks, which the
comment at `:769` asserts in prose ("It was latent only because `_synthetic_lam` is dense
in all 16 joints"), which I measured true today at 16 of 16, and which nothing in the file
checks -- so the premise that makes the gate meaningful is exactly the kind of sentence
CW0 asks to be a test or a triple. Verdict 96's condition read "an absolute comparison
against zero for that body PLUS an assertion on the COUNT of bodies compared ... so a
sparse row reduces coverage visibly rather than erroring". The first conjunct is done and
reproduced; this is the second, and half of an item is not the item.
**Closed when** `test_G4_4_the_mapping_CONSERVES_the_joint_resultants` asserts the COUNT
of bodies compared relatively -- equivalently that the lam row is nonzero in all sixteen
blocks -- with the measured `0 of 5` on the sparse row and the `0.0` on the all-zero row
pasted as what the assertion exists to prevent. That is the `checked == 16` pattern this
file already uses twice, and it makes the `:769` sentence true by assertion in the same
edit.

**R690. (closure-class, not (a) to (d), and I say so rather than dressing it as more.)
ER0, ER1, ER2, EQ2, EQ3 AND EQ4 EXIST NOWHERE IN THIS REPOSITORY, AND ER0 CHANGES THE
LOCKED PLAN'S SECTION 0.**
`grep -n "ER0\|ER1\|ER2\|EQ2\|EQ3\|EQ4" docs/milestones/F4.md` returns nothing, and the
only plan change in this range is the step marker `1 -> 2`. So this round judged a report
structured around six directives I can read only through the report's own account of them,
which my instructions name as a finding in itself. The work is correctly PAUSED -- the
report holds R682 and R685, and section 3a's eight figures are explicitly not asserted --
so nothing is silently adapted and this is not a STOP today. `docs/milestones/F4.md:5`
reads "LOCKED by directive EK. The section 0 answers are the directive's words,
unparaphrased. Changing them reopens the lock; it is not an inline edit", and ER0 changes
the platform mass and inertia that section 0 fixes.
**Closed when** ER0's and ER1's text is in the repository -- the plan's section 0 under a
re-lock, with ER2's ordering and EQ2/EQ3/EQ4 recorded wherever they belong -- BEFORE any
figure is derived on the new basis. Recorded now, and not held, because ER1(d) will derive
eight expected values and five counters from section 0, and a re-lock after that is a
second calibration of exactly the kind ER2 exists to prevent. The off-ladder consequence
in section 5 belongs to this item: `f = 0.75` produces nine builder findings on either
basis, one of them "This body is a MEASUREMENT, not one to ship".

## Closure items

Not re-reviewed item by item (CZ0). **C161 to C166 and C137/C141/C144/C145/C147/C148/C151
are STILL OPEN** -- the report says so in its section 9c and routes them to step 2's
closure commit, which is the right place. C161 I checked and it is unchanged: the dead
`error = _mapping_error(built, loads, want)` at `:838` is still overwritten two lines
later at `:840`. C166 is partly discharged -- the report lists the paths, which is what
EQ4 asked for -- and `git worktree list` still shows my own `wt84` plus seven
`suite-count-*`. New this round:

* **C167.** `scripts/report_joint_reactions.py:71` -- the false specification citation
  the report says it fixed is still here: "`docs/load-interchange-v1.md` sec.6's own
  published coefficients". `sec.6` is `## 6. Two-pass generation` at line 571. The fix
  landed at the other site and this one was left, which is the "closed site by site"
  shape. Closes when it reads sec.4.1 (or SECTION 4, lines 259-260, as the test file's
  own comment correctly does).
* **C168.** `floatfea/io/integrator.py:63` -- "`docs/load-interchange-v1.md` sec.2 is
  where the field is specified". Section 2 LISTS the field, at line 52, as
  `integrator REQUIRED -- v1.2, see sec.4.1`; section 4.1 at line 222 is where it is
  SPECIFIED, and the spec's own line points there. Defensible and still not the right
  pointer. Closes when it reads sec.4.1.
* **C169.** `floatfea/io/integrator.py:28-37` -- three sentences asserting facts with no
  triple and no cell: "It is FloatSim's value, not a choice made here", "the driver
  imports it from this module so that there is exactly one copy", and "Varying the single
  value moves the residual by about `1.0005x`". The first is imprecise (R686: it is this
  study's value; FloatSim's default is `0.9`), the second is checkable in one grep and
  measured true, the third is a causal figure with no cell in this file. CW0/BG0. Closes
  when each is a triple, a test, or deleted. **Note the module docstring at `:9-10`
  already does this correctly**, which is why this is a closure item and not a pattern.
* **C170.** `test_f4_static_and_mapping.py:862-864` -- the counter-case docstring's
  "`1.872582e-16` aggregated" carries no command and is not regenerated by anything. My
  own aggregate revert measured `2.082021e-16`. Both are round-off and nothing turns on
  the digits; the point is that it is an `out` line with no `cmd`. BI3's second permitted
  form applies: the entry keeps the number it needs and a pointer to the report.
* **C171.** R683's closing condition asked for the per-body breakdown to be pasted,
  because that is the evidence the residual localises. The report's section 4 pastes the
  pass/fail counts only. I took it (section 8) and it confirms localisation to exactly the
  two bodies the joint touches. Closes when the report or the closure artifact carries
  `platform 1.778481e+00, hub1 3.896589e-01, hub2 1.795271e-16, hub3 2.092543e-16,
  hub4 1.634659e-16`.
* **C172.** `docs/reports/F4/step-2.md` sections 3, 3a and 7 are generated by
  `scratchpad/er1c_stop.py` and `scratchpad/eq2_measure.py`, which are not in the tree, so
  no figure in them is regenerable at this commit -- the same shape as verdict 93's R, and
  the reason I re-took every one of them myself. All reproduce exactly, so this is a
  provenance item and not a correctness one. Closes when the figures come from something
  committed, or the report says plainly that these three sections are reviewer-reproduced
  rather than regenerated.
* **C173.** The two `CI determinism` jobs are `workflow_dispatch`-only
  (`.github/workflows/ci.yml:90`, `:213`) and were skipped at this commit, so determinism
  is **unmeasured** here. Recorded rather than stepped over (CK2's discipline, applied to
  a by-design skip rather than to an exhausted allowance). Nothing in this range touches
  `.github`. Closes when a dispatch run at a step-2 commit is cited, or the report states
  that determinism is measured per milestone and not per step.

## Carried

Verdict 96 carried **six items into step 2 by name -- R682, R683, R684, R685, R653 and
R679's remainder (R683 IS that remainder, so five distinct)** -- plus C161 to C166 and the
seven deferred C-items. Every one, with its status and where.

* **R683 -- ANSWERED, AND I REPRODUCED IT RATHER THAN ACCEPTING IT.** Report section 4;
  the row is at `test_f4_static_and_mapping.py:848-850` and `:886-901`. My own aggregate
  revert over the whole of rung 4 gives `1 failed, 156 passed` and the one red is
  `...[internal_joint_dropped]`, so the per-body rule is now held in place by something in
  the tree -- which is the whole of what R683 was. **Remainder: the per-body breakdown was
  not pasted; that is C171 and I took the measurement myself.** The closure commit's claim
  having been false is correctly owned in the report and in the comment at `:894-901`.
* **R684 -- ANSWERED ON THE FIRST CONJUNCT AND ON THE SECOND; THE COUNT CONJUNCT CARRIES
  AS R689.** Report section 5; `_one_body_error:760-791` and the new
  `test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked:918-949`. A legal
  sparse row no longer raises, I reproduced the C158 restoration reddening exactly that one
  test (`1 failed, 156 passed`), and the false sentence is DELETED rather than rephrased.
  **The premise was mine and the implementer is right that a faithful implementation of a
  wrong premise is still a wrong gate** -- I accept that answer in those words, as verdict
  96 said I would. What is not done is "an assertion on the COUNT of bodies compared", and
  the production gate reading `0.000e+00` with `0 of 5` compared is the measurement of why
  that conjunct was in the condition. **R689.**
* **R653 -- ANSWERED ON THE FORMULA HALF, NOT ON THE CONSTANT HALF, AND ITS COMPARISON
  FORM IS R688.** Report section 6; `floatfea/io/integrator.py` and
  `test_f4_static_and_mapping.py:960-1046`. The closed form is correct, I verified it
  against Chung & Hulbert independently and against the specification's own published
  block, and the module placement is accepted. **R686** is the constant half: the pin
  cannot fail on the property its name states, and the generated deck carries
  `spectral_radius_inf: 0.8` unread. **R688** is the comparison epsilon. Both are new
  findings inside R653's own answer rather than R653 re-opened, and I say which is which so
  the next round is not asked to re-answer what is done.
* **R682 -- OPEN, AND ER2's HOLD ON THE VALUE IS ACCEPTED.** Report section 7. I checked
  the premise rather than taking it: the tip/root ratio is independent of the total mass
  (numerator `mu L^2/12` and denominator `R L - w L^2/2` both scale with `M`) but it is NOT
  independent of `f`, and ER0 moves `f` from the ladder's `0.5` to `0.75`. So the `1/19`
  and `1/24` figures WILL move and calibrating now would be calibrating twice. **The hold
  is right.** What I do not accept for a second round is the other half: R682's condition
  offered a branch -- "the entry says that it is a bound about that one member and not
  about the sixteen" -- which is basis-INDEPENDENT, costs one sentence, and would remove a
  false claim from `floatfea/tolerances.py` today. `tolerances.py` is untouched, so the
  entry still reads "the measured worst over all 16 members is 5.555556e-02", a figure no
  member reads on either basis and which the implementer's own section 7 shows is wrong.
  R682 stays blocking and carries.
* **R685 -- OPEN, AND ER2's HOLD IS ACCEPTED WITHOUT RESERVATION.** Report section 7. The
  four figures are re-measured and in hand, the ordering the counter depends on survives,
  and the `0.2` value does not move. Nothing here is urgent and nothing is wrong except
  that the entry has not been rewritten yet. Carries.
* **R679's remainder** -- IS R683. Answered, see above.
* **C161 to C166 and C137/C141/C144/C145/C147/C148/C151** -- OPEN, routed to step 2's
  closure commit by the report's section 9c, not re-reviewed item by item, and none of them
  holds step 2. C166 is partly discharged by section 10.
* **CZ1 (ii) / EG3(ii)** -- the report measured state (1) at its own commit and traced all
  eight by name, which is what verdict 96 asked for and it is correct. I measure state (1)
  CLEARING at my verdict commit and the next revision pastes it.

## Tolerances touched

**NONE IN `floatfea/tolerances.py`, AND I DIFFED IT SEPARATELY (instruction 4) RATHER THAN
READING THE REPORT'S CLAIM.**

```
cmd    git diff 5786bed..HEAD -- floatfea/tolerances.py
out    (no output)
cmd    git diff 5786bed..HEAD -- docs/milestones/F4.md
out    one hunk: `<!-- step-under-execution: 1 -->` -> `2`. Nothing in section 5a.
rule   every numerical tolerance lives in floatfea/tolerances.py and moves with a plan
       edit; a tolerance change in the same commit as the code it rescues is a finding
judge  NO VALUE, FORM, COUNTER OR INJECTION MOVED. The report's section 11 is confirmed.
```

**BUT TWO NUMBERS THAT FUNCTION AS TOLERANCES ENTERED THE TREE OUTSIDE THAT FILE, AND
THAT IS WHY THIS SECTION IS NOT ONE LINE.**

| what | where | value | form | counter | my judgement |
|---|---|---|---|---|---|
| the five-place rounding comparison | `test_f4_static_and_mapping.py:1001`, `:1032` | half-width `5.0e-06`, undeclared | written as `round(x, 5) == published`, so dimensioned like the coefficient -- dimensionless here only because the coefficients are | none | **R688. A comparison epsilon under another name, and the test and the report both call it exact.** Solved per channel: `alpha_f` `7.895e-07`, `alpha_m` `2.368e-06`, `beta` `3.310e-06`, `gamma` `3.421e-06`. The governing figure is the smallest, `7.895e-07` on `alpha_f`. |
| `0.0 < beta < 0.5` and `0.0 < gamma < 1.0` | `test_f4_static_and_mapping.py:1041-1042` | `0.5`, `1.0` | NOT a tolerance -- a bound on a computed quantity, so `tolerances.py` is correctly not its home | n/a | **R687. The exemption's FORM is right and its REASON is false.** Measured `beta` in `[0.25, 1.0]`, `gamma` in `[0.5, 1.5]` over `rho_inf` in `[0, 1]`. |
| `0.05263` | `test_f4_static_and_mapping.py:1017` | expected value | reference figure read from `docs/load-interchange-v1.md:259` | n/a | **EXEMPTION ACCEPTED.** An expected value has no slack to widen. |
| `0.8` | `test_f4_static_and_mapping.py:1030` | input constant | the quantity pinned, not a bound on one | n/a | **EXEMPTION ACCEPTED as a non-tolerance.** The assertion is R686 for an unrelated reason. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `floatfea/tolerances.py` | `0.05`, unmoved | dimensionless | is the counter | **R682, OPEN.** Hold on the value accepted (the ratio depends on `f`, which ER0 moves). The entry's "worst over all 16 members is 5.555556e-02" is still there and is still false. |
| `F4_MAPPING_CONSERVATION` / `_COUNTER` | `floatfea/tolerances.py` | `1.0e-12` / `0.2`, unmoved | dimensionless, relative, per body | each other | **R685, OPEN, hold accepted.** I re-measured the ceiling's room myself at `4553x` on the clean per-body value `2.196224e-16`, and solved both EH4 directions in section 8. |

## On the criterion -- said once, and it leaves the loop

I was asked to say if I disagree with the criterion rather than with the work. **On CZ0 I
do not.** All four blocking findings are (b) or (c), everything else is a closure item, and
I have not held the step on a sentence.

**On the mechanism that forced THIS round, I do disagree, and this is the once.** EQ3 says
one invocation at the report; the `Stop` hook refuses a turn while `floatfea/` or `tests/`
has moved past the newest verdict. Those two rules cannot both be satisfied by a step that
takes more than one commit, and step 2 is a multi-commit step by design -- ER1(b) alone is
six FloatSim re-runs. The implementer's resolution was the honest one available: a real
report of what had landed, early, rather than a reverted commit or a silenced hook. **But
the cost is a round, and the cost falls on the step rather than on the mechanism.** I have
ruled that it counts because EB4 does not say otherwise, and I think that ruling is wrong
in substance and right in procedure.

**What I would ask Xabier for, as a question and not a round:** either EQ3 gains a clause
saying that a mid-step commit may be covered by a verdict that does not consume a round --
in which case EB4 is where it is written, so the next reviewer reads it rather than
reasoning about it -- or the `Stop` hook's condition changes to the one it is actually
trying to enforce, which is "no LATER step is worked while an earlier one is open", not
"no commit exists past the newest verdict". I have no preference between them. I am not
asking for new apparatus and the hook is not mine to edit. What I will not do is read EB4
as covering a case it does not mention, because the three-verdict cap is the only thing
standing between this project and the six-round rounds it already measured as worthless.

## On the schedule

The report's one hand-written paragraph carries the dates and reports slippage the day it
is known, which is what CZ0 asks: **F4's 14 Oct WORKING target is at risk, ER1 is a
two-day item, and the committed dates do not move.** I checked the dates against the plan
(`F4.md:375-377`) and they are the plan's. I have nothing to add except the exposure, which
has not improved: **step 2 now carries R682, R685, R686, R687, R688 and R689 -- six
blocking items, four of them new this round and three of them inside R653's own answer.**
Step 1 closed carrying three. CZ0's clause is "if two consecutive steps close carrying
blocking items, that is escalated with the choice stated -- slip the date, or reduce
scope." **If step 2 closes carrying any, that clause has now fired twice in a row**, and
the report paragraph is where the choice gets stated.

One observation for that paragraph, offered because it is cheap: the four findings this
round are all one-or-two-line edits in one file, and none of them needs ER1, the new mass
basis, or a decision from anyone. They can land before ER1(b)'s six re-runs start rather
than after.

## Next step opens when

**STEP 2 STAYS OPEN. This is its FIRST round of three, so two remain.** Step 3 does not
begin. What the next revision answers, before its own work is read, and each is specific:

1. **R686** -- `FLOATSIM_RHO_INF` compared against `simulation.spectral_radius_inf` read
   out of `data/platform/platform12_deck.yaml`, with the deck-at-`0.9` ablation re-run and
   pasted to show the gate reddens; OR the test renamed and its claim reduced to what it
   measures, with the provenance as a triple naming `platform12_deck.yaml:26` and
   `HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291`. **My figure to beat:
   `212 passed` with the deck at `0.9`.**
2. **R687** -- the range assertion stating the ranges the scheme has, or replaced by the
   exact `beta`/`gamma` identities, or deleted. The false sentence out of BOTH sites: the
   marker comment and the assertion message. **My figures to beat: `beta` in
   `[0.25, 1.0]`, `gamma` in `[0.5, 1.5]`, crossovers `sqrt(2)-1` and `1/3`.**
3. **R688** -- the five-place window declared with a counter, or `round(..., 5)` kept and
   "exact" deleted from the docstring and the report with the measured window published.
   **My figure to beat: `7.895e-07` on `alpha_f`, which is the governing channel.**
4. **R689** -- the production gate asserting the count of bodies compared relatively (or
   the row's density), with `0 of 5` and the all-zero row's `0.0` pasted as what it
   prevents.
5. **R682 and R685** -- the hold on their VALUES is accepted and I will not ask for them on
   the old basis. **R682's basis-independent half is a different matter**: either the
   `tolerances.py` entry says it is a bound about one platform arm rather than about
   sixteen, or the report names the site and says why it was left for a second round. A
   false figure in a tolerance comment is the only statement a reader has of what that
   counter bounds.
6. **R690** -- not held. ER0/ER1's text into the repository before ER1(d) derives anything
   from it, and the `f = 0.75` off-ladder question settled: nine builder findings, one of
   them "not one to ship", on either basis.
7. **C167 to C173, plus C161 to C166 and the seven deferred C-items** -- step 2's closure
   list, absorbed once, not re-reviewed item by item, and none of them holds the step.
8. **EG3(ii)** -- state (1) measured CLEARING at my verdict commit `4f99c7f`+1, and state
   (2) measured at that commit and pasted in the next revision. The expected reds there are
   the EH1 state (2) list and nothing else; any red outside it is CZ1 (iv) unchanged.

**WHAT I WILL NOT ACCEPT AT THE SECOND ROUND.** "The deck and the constant agree today"
offered as R686's answer: that is the measurement, not the gate, and R653 has been carried
four times on exactly that sentence. A range assertion for R687 whose bounds are chosen to
pass at `0.8` and justified by a new claim about the scheme that is not derived -- if the
bounds are arbitrary, say they are arbitrary and say what they are for. "A rounding is not
a tolerance" for R688 without the four numbers; the numbers are the finding and they are
measured. And for R689, a count assertion added to the SPARSE test, which already has one
-- the gate that needs it is `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`,
because that is the one the plan's G4.4 row points at and the one a reader will believe.

**And the thing I would most like the second round NOT to contain**: a new figure outside a
`claim/cmd/out` triple taken after the final edit. Four of this round's five findings are
sentences that were each written in good faith, three of them inside a repair, and CP2 and
CP3 are the two rules that would have caught all three.
