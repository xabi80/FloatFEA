# Review — F2 step 4
Reviewed commit: e4c0391be2acf549647594acde8f7d45d7bd5ad7
Verdict: PASS
Tests: 1497 passed, 0 failed, 0 skipped   (my run at `4ccd166`, `python -m pytest -q`,
168.27 s. With my twenty-fifth-round corpus applied at `e4c0391`: **1541 passed, 2 failed** --
`test_the_generated_figures_are_not_stale` and `test_the_recorded_set_is_the_measured_set`,
both by construction, both named in *Next step opens when*.)

**Reviewed code commit: `4ccd166`.** The header stamp is `e4c0391`, my own corpus
commit, made immediately before this verdict and touching no code.

Twenty-fifth pass, and **the first PASS since the twenty-second.** Range
`ee8ad0b..HEAD`, three commits. R211 -- the one blocking item -- is answered at
the line its condition named, and I checked the answer by re-measuring the cell
rather than by reading the sentence. R212, R213 and R214 were classed 4a by me
and taken anyway; all three are closed.

```
cmd  git diff ee8ad0b..HEAD -- .claude docs/SUPERVISOR.md
out  (empty)  -- my instructions untouched. Nothing added, nothing deleted.
cmd  git diff --stat ee8ad0b..4ccd166 -- floatfea/
out  floatfea/tolerances.py | 29 +++++----- AND NOTHING ELSE
cmd  git diff ee8ad0b..4ccd166 -- floatfea/tolerances.py, non-comment changed lines
out  (empty)  -- every changed line is a comment. No value, no name, no form moved.
cmd  git diff --stat ee8ad0b..4ccd166 -- tests/
out  (empty)  -- no test, no golden file, no fixture
cmd  git log --format=%h %s --name-only ee8ad0b..HEAD ; any commit touching docs/reviews/
out  c6d6817 plan / 703e7eb step / 4ccd166 report -- none touches docs/reviews/,
     and the plan edit is a standalone plan: commit that touches nothing else
cmd  grep -n "^Answers:" docs/reports/F2/step-4.md | tail -1 ; newest verdict
out  :4108 verdict 24 @ ee8ad0b ; ee8ad0b IS the newest verdict. Item 1b does not trigger.
cmd  python -m pytest -q 2>&1 | tail -1
out  1497 passed, 2 warnings in 168.27s
cmd  python scripts/regen_figures.py --check ; echo exit
out  regen_figures: up to date -- exit 0
```

## Carried

Every item from the twenty-fourth verdict (`HOLD @ 3e225c5`, committed `ee8ad0b`),
re-measured at `4ccd166`.

- **R211 -- ANSWERED, and the answer is the branch the condition asked for.** The
  condition was that `F2.md:598-599` either drop "the improvement side only" or
  name the direction rather than the cause, agree with `:601-603`, and keep the
  withdrawal clause. All three, checked line by line and then re-measured:

  ```
  code  :602-603 now "**The room this constant leaves moves in ONE DIRECTION, and
        the sentence claiming otherwise is withdrawn.**" -- a direction, not a cause
  code  :603-604 "It read 'a harder corpus entry raises the edge and loosens the
        guard'" -- the withdrawal clause is textually untouched. R209's condition
        required that it stand, and it stands.
  code  :605-607 "So the guard is loosened by nothing, and tightened both by a
        harder corpus entry and by any formulation change" -- unchanged but for a
        comma. The two halves of the paragraph now answer the same question the
        same way; the "only" that contradicted them is gone.
  cell  I re-took the measurement rather than accepting the report's:
        counter_headroom_room at every commit of the figures file, with entries --
          133:2.37  139:2.37  145:2.37  145:2.37  149:2.37  156:2.37
          163:2.19  170:2.18  177:2.18
        Two falls in eight published values; never a rise. And the falls, one
        variable at a time:
          git diff --stat f1b226b..fc30b71 -- floatfea/   ->  (empty)
          git diff fc30b71..6eed45e -- floatfea/, non-comment lines -> (empty)
        Both tightenings happened with the formulation byte-identical. Two of two
        were corpus rounds; zero of two were sensitivity improvements.
  judge closed. The lead now states what the cell shows and nothing more. What it
        carries besides -- "has fallen twice", and 2.18x typed -- is R216 below,
        recorded at 4a and not a re-opening of this.
  ```
- **R212 -- CLOSED, and I checked the date against git rather than against the
  report.**

  ```
  cmd   git log --date=short -S PATCH_TEST_EXACTNESS: Final[float] = 5e-15
  out   fdade28 2026-09-06 -- and the entry own footer at :443 reads
        "Quantity and value REPLACED 2026-09-06, F2". The comment at :408 now
        reads 2026-09-06. Three sources, one date.
  cmd   grep -n "10.2x" floatfea/tolerances.py
  out   (empty) -- gone, and the paragraph points at clean_worst_ratio instead.
  judge closed at both halves. The R212 note that replaces it is tensed as history
        and carries no live figure.
  ```
- **R213 -- CLOSED, and the ruling I was asked for: removing the count is right,
  and it is right for the reason the entry gives.**

  ```
  cmd   grep -n "three times|three consecutive|two consecutive" F2.md tolerances.py
  out   one hit in each file, both inside the quoted history of the deleted phrase
        ("one direction, three times stood here and in tolerances.py"). No live
        count of reviewer rounds survives in either place.
  judge REMOVING IT WAS THE RIGHT ANSWER, not merely an acceptable one. A count of
        reviewer rounds is a measurement with no mechanism behind it: {{fig:}}
        cannot carry it, because the figures file is produced by the corpus runner
        and the runner does not know what a round is. Correcting the count would
        have re-published the same species with a better number -- which is
        exactly how "three times" got there, and BI3 says the entry keeps the one
        number it needs and a pointer. It now does.
  judge AND THE REPLACEMENT IS NOT CLEAN. "The room has fallen twice ... 2.37x to
        2.19x to 2.18x" is a count of falls and three typed values, one of which
        is live. That is R216, recorded at 4a, and it does not re-open this item.
  ```
- **R214 -- CLOSED on the second branch, which the condition offered.** The plan
  says `BRACKETED`, states the `+/- 0.1%`, and says in terms that a two-point
  bracket locates rather than finds. The code that brackets is unchanged and the
  site table declares every line of it. The residue -- `scripts/regen_figures.py`
  still calling the same operation `SOLVED` in its own comment -- is **R217**, 4a.
- **R215 -- 4a, and I agree with the reasoning given.** `_Silent` and `_Capsys`
  are the same shape and want one home; the interleaving is visible in my own
  `--check` run above and changes no published number.
- **R206, R210 -- 4a, unchanged.** `tolerances.py` still retypes `2.537e+07` and
  `2.534e+07` as history at `:533-535`; true as history, and the fifth typed
  figure in that file.
- **R200, R201, R202, R203, R204 -- OPEN at 4a**, untouched, correctly declared.
- **R198, R199 -- 4a, accepted, unchanged.** R199 citation `3d91954` resolves
  (`git cat-file -t` -> commit).
- **R181, R189, R190, the R170/R171 remainder, R172, R159, R162, R151, R152 --
  4a, unchanged from my endorsement.**
- **R205, R207, R208, R209 -- CLOSED in earlier rounds.** R207 generated
  boundary reproduced again this round: `--check` exit 0 over the whole table.
- **R134, R135, R137 -- OPEN, UNTOUCHED**, twentieth round.
- **R129, R131, R132, R136, R138, R139, R148 -- as declared.**
- **R113, R95, R97, R98, R100, R101, R102, R103 -- OPEN.**
- **R124 -- OPEN at 4a**, and re-measured this round rather than read: the edge is
  bit-identical under a 1e3 change of the counter-defect size, because
  `_detection_edge` bisects on `PATCH_TEST_EXACTNESS` and never reads the counter.
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Recorded as a disagreement.
- **R6, R16, R25, R30, R31, R32, R33, R36, R50, R52, R62 -- still open**, 4a or
  later.
- **R68 standard -- MET, ninth round.**
- **The witness channel -- STILL UNAVAILABLE, blocker unchanged from the last
  verdict.** `xabi80/FloatFEA` exists and `master` is pushed; a pull request has no
  base branch. **Twenty-five consecutive reviews by one reader.** Not a pass, and
  correctly not settled inside a step. It is the longest-standing open item in this
  milestone and it is the one that would falsify the most.

## Findings

**None of the seven blocks.** Each is stated with the head it would have to touch
to block, and why it does not. R221 and R222 are the two I would put first on 4a
list; R222 is the one I came closest to blocking on and I say why.

**R216. (recordable, 4a) The line that stops counting rounds counts falls, and
types the live value of a generated figure in two files.**
`floatfea/tolerances.py:519-521` and `docs/milestones/F2.md:612-614`.

```
code  tolerances.py :519-521 "the reviewer corpus rounds have measured it: the
      room has fallen twice, 2.37x to 2.19x to 2.18x, and has never risen."
code  F2.md :612-614, the same sentence.
code  and three lines below it, :521-524: "NO COUNT OF ROUNDS IS WRITTEN HERE
      (R213) ... any such count goes stale the next time the reviewer adds an
      entry."
cmd   grep -n counter_headroom_room docs/milestones/F2_figures.md
out   the row reads 2.18x -- the third of the three typed values IS the live
      figure, available by name two lines above at :512 where this same entry
      already cites it correctly.
judge the stated reason for deleting the old count applies to its replacement:
      "twice" is falsified by the next fall, and 2.18x by the next corpus round.
      Both are TRUE at this commit, which is why this is recorded and not blocking
      -- the same ruling I gave R212 and R206, and I am not applying a different
      one because the sentence is new.
judge cosmetic, same hunk, recorded so it is not mistaken for content:
      tolerances.py:524-526 wraps as "... absorbs that while / # still / #
      catching every ...".
```

**Closed when** the trajectory is cited by name, or tensed as history with the
commit it was measured at, as `:407-411` now does for the derivation. **It stops
being recordable and becomes blocking** the first time `counter_headroom_room`
moves and these two lines do not move with it -- that is BP0 rule, and it will
be a figure that no longer describes the repository.

**R217. (recordable, 4a) The plan retired the word `SOLVED` for this operation;
the script that performs it still uses it, twice.**
`scripts/regen_figures.py:101` and `:108`.

```
code  :101 -- THE BOUNDARY IS SOLVED HERE, NOT TYPED INTO THE PLAN (R207).
code  :108 -- SOLVED means the SHIPPED assertion is run either side of the
      boundary, with the counter-defect size moved and nothing else.
code  F2.md:585-589, written this round: the word here was SOLVED, and a
      two-point bracket locates the crossing to 0.2 percent rather than finding
      it ... it is still not a search, and the sentence no longer says it is.
judge :108 is a stipulative definition and it describes the code accurately, so
      no measurement refutes it -- which is why this is not the truth head. What
      it is: the two files now name the same operation differently, one round
      after R209 was blocking because two files named the same DIRECTION
      differently. :101 is a bare label with no definition attached and it is the
      weaker of the two.
judge THE DECLARATION IS HONEST AND INCOMPLETE, ruling as asked. The site table
      declares :108-123 as no change, and deliberately, and gives the branch
      taken. That is true, and it is the second time in two rounds that a
      declaration covers the site line number without covering what is written on
      that line -- R211 shape. It is not the hatch R193 punished: the line is
      declared by number, the reason is checkable, and I checked it. :101 is
      outside the range R214 named and no declaration was owed for it.
```

**Closed when** the two comments in the script say what the plan says, or 4a
records that the script keeps its own vocabulary and why.

**R218. (recorded; answered in the next report, not in this step) The report
revision states no test count from its own run, and the collected suite moved by
44 in this range with nothing in the repository recording it.**
`docs/reports/F2/step-4.md:4106-4333`.

```
cmd   grep -nE for a three or four digit count followed by passed, over the report
out   the last full-suite count in the file is at :2873, in revision 19. Revisions
      20, 21, 22, 23 and 24 state none. CLAUDE.md sec. Step gating item 1 asks
      for the test counts from your own run.
cmd   python -m pytest --collect-only -q at 45550a3 and at HEAD
out   1541 -> 1497. Located, entirely, in tests/test_report_carried.py: 166
      parameters -> 122.
cell  which commit moved it: the parameter set is built from the newest verdict
      site list, so the drop is ee8ad0b -- MY verdict commit, not a step commit.
      Verdict 23 named 166 sites; verdict 24 named 122.
judge so the count is honest and the movement is mine. What is left is real
      anyway: **the size of this suite is a function of the newest verdict, so
      1497 passed is not comparable across commits and a shrinking parametrisation
      cannot be told from tests disappearing without collecting both ends.** I did
      collect both ends. Nothing in the repository does.
judge NOT BLOCKING: no false sentence, no figure, no tolerance -- an absent
      required field, whose absence hid nothing this round because I ran the suite
      myself, which is this arrangement own answer to it.
cell  and the empty-parameter case is NOT a hole, tested rather than assumed: I
      built a verdict with five findings that name no file, committed it in a
      clone, and pointed the report header at it. Collection ERRORS -- Empty
      parameter set in test_every_named_site_is_touched_or_declared, exit
      non-zero -- because pyproject.toml:60 sets empty_parameter_set_mark to
      fail_at_collect. The guard exists and it fires.
```

**Closed when** the next report revision states the suite counts from its own run,
and -- because the number now moves for reasons that are not the code -- says what
moved them.

**R219. (recordable, 4a) A ratio without its denominator, in the sentence that
replaced `SOLVED`.** `docs/milestones/F2.md:587`, and the report at `:4158`.

```
code  a two-point bracket locates the crossing to 0.2 percent ... That is four
      orders tighter than anything this paragraph decides
cmd   the two candidate denominators, solved rather than asserted
out   against the order-of-magnitude raise the guard exists to catch (a 10x raise
      is 900 percent in this quantity): 900 / 0.2 = 4500x = 3.65 orders -- four to
      the nearest order, and the reading I think is meant.
      against what the paragraph actually decides, the room own margin (2.18x,
      i.e. 118 percent): 118 / 0.2 = 590x = 2.77 orders. Not four.
judge true on one reading, false on the other, and the sentence names neither. A
      ratio carries its operating point; this one is a bare factor between two
      quantities, one of which is unnamed. Apparatus prose about apparatus
      precision, so 4a -- and it is one clause.
```

**Closed when** the sentence names the quantity it is four orders tighter than.

**R220. (recordable, 4a, and it is a condition on the 4a lock) The 4a list exists
nowhere but in the prose of twenty-five verdicts and one report.**
`docs/milestones/F2a.md`.

```
cmd   grep -oE for R followed by digits over docs/milestones/F2a.md
out   (empty) -- not one R-number in 117 lines.
cmd   the count of items this round report and verdict call 4a
out   about thirty-five, across R6..R215, each recorded in a different revision.
judge recorded at 4a is true in the sense that verdicts are permanent, and the
      report section 4 is the only assembled copy. It is not true in the sense a
      reader of F2a.md would take. The dependency list is the mechanism this
      milestone is built on, and for 4a it currently lives in prose that the 4a
      plan does not reference.
judge NOT BLOCKING: no sentence in the repository claims the list is in F2a.md --
      I grepped, and the two mentions of F2a.md in the report and the one in
      floatfea/testing.py all resolve, the last to a real sec. 2A.
```

**Closed when** `docs/milestones/F2a.md` carries the list, item by item, with the
verdict each came from -- which is work for the 4a lock Q&A, not for a step commit.

**R221. (recorded -- a measurement, and the item I would put first next round)
The ceiling margin is the side nobody was searching, and one round of searching
it halves the margin.** No site: this is my corpus round.

```
cmd   clean_worst_ratio at every commit of the figures file
out   0.0887x (133 entries, held through 156), 0.0982x (163), 0.1142x (170),
      0.1261x (177) -- three outside rounds, three rises, each from a region the
      previous round had not entered.
cmd   this round: 10,000 random starts, 33 hill-climbs, at 4ccd166
out   0.2765x. The margin on PATCH_TEST_EXACTNESS = 5e-15 is **3.62x**, where the
      generated figures at this commit say 7.93x and the entry own derivation
      recorded 26.8x.
cell  it is a plateau, not a spike: 5 of the first 8 climbs exceeded the published
      worst; ten climbs inside the boundary corner alone landed 0.16x..0.25x. Two
      independent maxima are in the corpus beside the best one for that reason.
judge WHY FOUR ROUNDS MISSED IT: the maximum sits ON the admissible boundary --
      I_y_over_I_z exactly 1e6, the top of the declared range, and a wall of
      0.4989 D against the strictly-less-than-D/2 the constructor enforces.
      Log-uniform sampling reaches a corner with probability about zero. Every
      previous round sampled.
judge NOT BLOCKING, and I want the reason on the record: the shipped assertion
      HOLDS at every one of my entries, clean_worst_ratio stays below one, and the
      published figure was true of the corpus it described. This is a statement
      about the CORPUS coverage, not about the element -- the field error itself
      did not move. But the trend is monotone, four for four, and 3.62x is the
      smallest margin this ceiling has ever had.
```

**Closed when** 4a records what the margin is defended by -- a search that reaches
the admissible corners rather than a corpus that samples the interior -- or the
next round search fails to lower it further, which would be the first evidence
that 0.2765x is near a maximum rather than near the last place someone looked.

**R222. (recordable, 4a -- and the one I came closest to blocking on) The
boundary-margin probe upper bracket end is a bare `1.0e9`, dimensional, and it
decides which bases get published.** `scripts/regen_figures.py:205`.

```
code  lo, hi = ((1.0 + BOUNDARY_BISECTION_CONVERGENCE)
                * BEAM_ADMISSION_L_OVER_D * outer), 1.0e9
judge the LOW end is derived from two named constants and the section, because
      R175 found that a fixed 1.0 refused 80 of 110 bases -- an artefact of the
      probe, not a property of the base. The HIGH end on the same line is an
      absolute length in metres, and nothing scans scripts/ (tolerances.py:546,
      in the entry R187 moved out of this same file).
cell  one variable moved, the model unit scale, bracket held; then the bracket
      moved, scale held. The same shape at three scales:
        1e-8 scale   crossing L 4.176e-06 m   margin 19206.3x   brackets at 1e9
        1e0  scale   crossing L 417.6 m       margin 19206.3x   brackets at 1e9
        1e+8 scale   crossing L 4.176e+10 m   margin 19206.3x   UNBRACKETED at 1e9
        1e+8 scale, hi raised to 1e12         margin 19206.3x   brackets
      The margin is unit-invariant to six figures over sixteen orders. The
      EXCLUSION is not: it is the probe units, exactly R175 species at the other
      end of the same bracket.
cmd   regenerating the figures with my corpus applied
out   boundary_margin_unbracketed 0: none -> 1: ck_cleanmax_x1e8 -- the first
      non-empty value this figure has ever had, and its cause is measured above.
judge WHY THIS IS NOT A BLOCK, stated so it can be argued with. It is close: a
      bare dimensional literal that selects what is published is a decision
      constant by this repository own ruling (R187, same line, same file), and an
      absolute tolerance on a dimensional quantity is a defect by the recorded
      form guard -- I have now measured it failing the unit-scaling test. What
      keeps it at 4a is that no published number is false: boundary_margin_* is a
      diagnostic asserted against nothing, the excluded base is published BY NAME
      rather than swallowed (which is what R175 built), and the dropped margin
      19206.3x lies inside the published range, so the min, the max and the spread
      are all unaffected. That last part is luck, not design.
judge IT BECOMES BLOCKING the moment a base excluded by the bracket units would
      have set boundary_margin_min -- which is R175 finding verbatim, and R175
      was a block.
```

**Closed when** the upper end is derived from the base own geometry, as the lower
end already is, or it is a named constant in `floatfea/tolerances.py` with a
Reason that says what unit system it assumes -- and, either way, when the next
regeneration sentence about `ck_cleanmax_x1e8` carries the cell above rather than
a new explanation.

## Tolerances touched

**None. Every changed line in `floatfea/tolerances.py` is a comment.**

```
cmd  git diff ee8ad0b..4ccd166 -- floatfea/tolerances.py, with comment lines and
     diff headers removed
out  (empty)  -- not one value, not one name, not one form
```

| site | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` `:539` | `6.0e7` | `6.0e7` (unchanged) | ratio, dimensionless | the raised-defect counter, injected through module globals and registered in both cells | `tolerances.py:483-538` and `F2.md:561-636`. **HOLDS**, re-solved rather than read: the flip is at `6.0e7 x 3.6275e-14 = 2.17651e-06`, `2.18x` of room, and the generated bracket reproduces it (`2.174e-06 passes, 2.179e-06 fails`, `--check` exit 0). Under my corpus round the edge does **not** move -- the smallest of about 1,500 new candidates is `3.9971e-14` -- so the room stays `2.18x`, fourth round running against a reviewer trying to break it. The paragraph remaining defects are **R216** and **R219**, neither of which touches the value. |
| `PATCH_TEST_EXACTNESS` `:444` | `5e-15` | `5e-15` (unchanged) | relative field error, dimensionless | `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`, injected | `tolerances.py:400-443`. **HOLDS**, and this is where the round news is: `7.93x` above the worst clean entry at this commit, **`3.62x`** under my corpus. Still below one at every one of the 158 solved entries. **R221.** |
| `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` `:481` | `1.0e-6` | `1.0e-6` (unchanged) | defect size, dimensionless | it IS the counter; its own guard is the headroom above | unchanged; `margin_one_element_scaled` `8.698e+06x`, `0 of 158` below the ceiling under my corpus. |
| `DELTA_CALIBRATION_ULP` `:594` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `DELTA_CALIBRATION_ULP_COUNTER = 5.0`, injected | `calibration_ulp_worst` is `2.000 ULP` at this commit and `2.000 ULP` under my corpus; my nine new solved entries land at 0 ULP (`x133 -> x141`) and 1 ULP (`x5 -> x6`). The `2x` headroom is not threatened. |
| `BOUNDARY_BISECTION_CONVERGENCE` `:567` | `1e-6` | `1e-6` (unchanged) | relative bracket width, dimensionless | none, per AO2 | unchanged. Its **sibling on the same line of the same function is R222** -- the one bracket parameter that was never named. |
| `EXEMPT_RESPONSE_DRIFT_ULP` `:650` | `4.0` | `4.0` (unchanged) | ULP multiple, dimensionless | `10.0`, injected | unchanged; the golden file did not move this round. Under my corpus it gains one row -- see below. |

**The golden file, checked as its own question (CLAUDE.md, section Testing).**

```
cmd  git diff ee8ad0b..4ccd166 -- tests/regression/g22_exempt_pair_responses.json
out  (empty) -- and git diff ee8ad0b..4ccd166 -- tests/ is empty entirely.
     Nothing to explain in this step.
cmd  with my corpus applied: pytest -q tests/regression/test_exempt_pair_responses.py
out  1 failed -- ck_aniso_floor_exact with dropped_flip is exempt and detected and
     not in the golden file. That is BS2 working: my entry at the anisotropy floor
     is classified below resolution for the flip defect and the gate catches it
     anyway. The next step adds the row WITH the explanation the rule requires.
```

**What held.** These reproduce at my run: `1497 passed, 0 failed, 0 skipped`;
`regen_figures.py --check` exit 0; `floatfea/` byte-identical outside comments;
`tests/` byte-identical; my instructions byte-identical; the plan edit in a
standalone `plan:` commit; the report figure movements to the published digits
(`0.1142x -> 0.1261x`, `61 of 580 -> 61 of 596`, histogram `x129 -> x133`); the
claim that the edge, the room and the bracket do not move this round; every path
and every commit the report cites. These do **not**: the two typed live figures
(R216), the script vocabulary (R217), the missing suite count (R218), the
denominator-free four orders (R219).

## Next step opens when

**Step 4 is CLOSED. Step 5 may open, and its first commit is the regeneration.**

The tree at my corpus commit `e4c0391` is **red on two tests, both by
construction**, and both are the established mechanism rather than a failure:

1. `tests/test_plan_figures.py::test_the_generated_figures_are_not_stale` --
   run `python scripts/regen_figures.py` and commit the result. Measured, so the
   next report has the target: `corpus_entries 177 -> 187`, `corpus_solved 149 ->
   158`, `clean_worst_ratio 0.1261x -> 0.2765x` at
   `ck_cleanmax_D18p8_tw0p499_aniso1e6`, `exempt_total 61 of 596 -> 62 of 632`,
   `exempt_detected 54 -> 55`, `calibration_ulp_histogram 0 x141, 1 x6, 2 x11`,
   `boundary_margin_bases 144 -> 152`, and `boundary_margin_unbracketed 0: none ->
   1: ck_cleanmax_x1e8`. The detection edge, the room, the bracket and every
   `margin_<defect>` do **not** move.
2. `tests/regression/test_exempt_pair_responses.py::test_the_recorded_set_is_the_measured_set`
   -- one new row, `ck_aniso_floor_exact` with `dropped_flip`, and the written
   explanation the golden-file rule requires. A corpus round is a reason; say so.

**Two things go into the next report Carried section, and neither is a step-5
gate:**

* **R218**, which is answered by one line: the suite counts from your own run, and
  what moved them.
* **The first non-empty `boundary_margin_unbracketed`.** The cause is measured in
  R222 above and it is the probe unit-dependent upper bracket, not a property of
  the entry. If the regeneration commit writes a sentence about that row, it
  carries that cell or it carries no cause at all.

**R216, R217, R219, R220, R221 and R222 are recorded at 4a** with the roughly
thirty already there. R220 is the one that decides whether the other thirty-five
survive: F2a.md names not one of them today.

**Adversarial corpus (BE3): 10 new entries committed at `e4c0391`, all unseen by
the implementer; every field measured at `4ccd166` before the line was written.**
`tests/corpus/g22_model_configurations.txt`, now **187** entries, 158 solved.
Full suite with the corpus applied: **1541 passed, 2 failed.**

The coverage measurement, stated plainly: **of my 10 new entries the shipped
checks caught 2 -- the parser refused the one that must raise
(`ck_aniso_one_ulp_under_floor`), and BS2 golden file reddened on exactly one new
exempt-and-detected pair, 1 of 10. BT0 staleness check reddens on eleven rows.**
The gate itself was not broken by any of them.

What the entries measure, and the round finding is the first one:

* **The worst clean ratio more than doubles under a direct search: `0.1261x ->
  0.2765x`, and the margin on `PATCH_TEST_EXACTNESS` falls `7.93x -> 3.62x`.**
  Four outside rounds have now raised it four times, and this is the first round
  that searched for it rather than sampling near it. The maximum is ON the
  admissible boundary -- anisotropy exactly `1e6`, wall `0.4989 D` -- which is why
  interior sampling missed it, and it is a plateau: 33 hill-climbs, five of the
  first eight above the published worst, two independent maxima committed beside
  the best. **The ceiling holds. Its margin is the smallest it has ever been.**
* **The detection edge is unbeaten, fourth round running.** Breaking `6.0e7` needs
  an edge below `1.6667e-14`; about 1,500 candidates in a region the corpus had
  not entered reached `3.9971e-14`, still above the published `3.6275e-14`. And
  the shape that maximises round-off is **not** the shape that minimises
  detection -- the three clean maxima have edges `3.84e-14`, `4.10e-14`,
  `6.53e-14`.
* **The clean ratio scale spread is bounded over sixteen orders, and the detection
  edge is scale-free over the same range.** `0.0417x / 0.1261x / 0.0305x` at
  `1e-8 / 1e0 / 1e+8` -- `4.14x`, with the maximum at the SI scale, which is the
  safe side. The edge over the same span is `6.125e-14 .. 6.298e-14`, `2.8%`. Any
  unit-invariance claim on the clean ratio is bounded at `4.2x`, never an
  identity.
* **The anisotropy range is closed at its FLOOR to one ULP**, as the twenty-fourth
  round closed its top. `math.nextafter(1e-6, 0)` is refused; `1e-06` exactly is
  accepted. Both ends measured, neither declared.
* **Roll is not range-checked, and that is now data rather than an assumption.** A
  roll of `1e6` radians is accepted and gives a field error equal to the one at
  `2*pi` to four figures. Nothing here says it should be refused; the case is on
  disk so a future claim that roll is bounded has a counter-example.
* **And one entry found a defect in the apparatus rather than in the element**:
  `ck_cleanmax_x1e8` is the first base ever to fall outside the boundary probe
  bracket, for a reason that is the probe units and not the base geometry (R222).

**Twenty-five consecutive rounds have found no element defect**, and the reading
is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side.
The element did not move under 10,000 candidates of my input either. What moved,
for the fifth round running, is prose about the element instruments -- and, this
round, the measured distance between a shipped ceiling and the worst case anyone
has bothered to construct.
