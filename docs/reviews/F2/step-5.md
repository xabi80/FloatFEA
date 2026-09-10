# Review — F2 step 5
Reviewed commit: a7b0e23b164fce3a0ffdd45a9118df9bf6f859a9
Verdict: HOLD

Tests: **1759 passed, 0 failed, 0 skipped** (my run at `a949709`, `python -m pytest -q`,
274.49 s, Python 3.13.11 on Windows). Identical to the report's figure. With my
thirty-third-round corpus applied: `tests/test_ci_ladder_gating.py` gives **7 failed, 41
passed**; the two other files I wrote to have no runner and induce zero failures.

**Plan: `e4f1b45` (re-locked, standalone). Code: `bcaad88`. Report: `a949709`
(revision 7).** The verdict is stamped at my corpus commit.

**Item 1b.** The newest revision's header reads `Answers: verdict 32 @ 49c8449` and
`49c8449` is the thirty-second and latest verdict. **Passes** -- and R282 below is my
ruling on the machine that has now been asked to help with it.

**CI, item 3b, at the reviewed commit. RED, AND THE RED IS NEW.**

```
cmd  gh run list --commit a949709985ff3089d834d37fe720d1a9840015da
out  34440129351 (push) failure   34440131711 (pull_request) failure
cmd  gh run view 34440129351 --json jobs
out  lint and type-check   success   unit tests   success
     ladder 1 / 2 / 3      success
     guards and meta-tests FAILURE   ladder 4     failure
     ladder 5, ladder 6    skipped
     CI determinism (1..10)          FAILURE x10   <- ALL TEN
judge TWELVE RED JOBS. Two are routed items pending Q8. TEN ARE NEW AND THE
      REPORT DOES NOT MENTION THEM. R293.
cmd  gh run list --commit e4f1b45 ; gh run list --commit bcaad88
out  []  []  -- neither the plan commit nor the step commit ran on CI. The step
     commit's code is identical to a949709's, which did, so that is recorded
     rather than raised.
```

`git diff 49c8449..HEAD -- floatfea` is empty. `-- floatfea/tolerances.py` is empty.
`-- tests/regression` is empty. `-- docs/milestones/F2_figures.md` is empty. No commit in
the range touches `docs/reviews/`.

**PR #1 is open, `F2 -> master`, `gh pr view 1 --json comments` returns 0 comments.**
Step 5 still has no outside-witness comment. Recorded as an unavailable check, not as a
pass.

## Carried

Verdict 32 listed five numbered conditions over nine blocking items. **Three close. One
closes in its mechanical half with a stated clause unmet. Five do not close, and four of
those five are recorded in the report as answered.**

- **R282 -- CLOSED, and the ruling you asked for is: you are right.** The ancestry
  discriminator is the narrower claim, it is not item 1b restored, and I ran the boundary
  rather than reasoning about it.

```
cell a `git clone --local` at a949709; one commit appended touching ONLY
     docs/reviews/F2/step-5.md, exactly as a verdict does, report untouched:
out  174 passed, 0 failed        <- the closing condition, met
cell the same clone, one further commit touching ONLY the report, header left
     naming the older verdict -- the defect the check exists for:
out  1 failed, 173 passed
     "the report at `b53ea84` is newer than the verdict at `b48c28f` and names
      `49c8449`. Written with the newest verdict available, it must answer
      that one."
judge GREEN AT THE BOUNDARY, RED ON THE DEFECT. That is the gate carrying its
      own failure, and the shape that cost the meaning of the suite is gone.
judge AND THE REACH, STATED SO IT IS NOT TRUSTED PAST IT. The check cannot see
      a report that is never re-committed after a verdict lands: ancestry then
      says the report predates it and passes. That residue IS item 1b, it is
      still mine, and I did it by hand above.
judge ONE RESIDUE THAT IS NOT REACH. In a `--depth 1` clone the new test fails
      spuriously and the corpus state that models exactly that clone cannot
      see it. R300.
```

- **R283 -- CLOSED on the second branch.** Section 3 of revision 6 was withdrawn and
  replaced: revision 7's sections 1 and 2 state what the pin did and where the measurement
  lives. `grep -rn "34435454388\|34434995901" docs/` still matches only my own previous
  verdict, so the run ids remain traceable through `docs/reviews/` and nowhere else. I
  record that rather than raise it -- the hashes and the vendor split are now in the plan,
  which is what mattered.

- **R284 -- CLOSED, and the repair is real. I ran your experiment against the new body.**

```
cell the two shipped step bodies verbatim, `git clone --local` at a949709:
out  F2_figures.md overwritten with one line of garbage
       -> regen_figures: F2_figures.md is not what this script produces at
          HEAD;  EXIT 1;  and the file still reads `GARBAGE` afterwards
     F2_figures.md deleted outright
       -> EXIT 1;  the file is NOT recreated
     unmodified tree
       -> regen_figures: up to date;  EXIT 0        CONTROL
judge THE HASH IS NO LONGER A PROPERTY OF THE RUNNER. `--check` compares the
      whole file and does not write, so the decoupling is gone. Comparing every
      leg against one committed reference is EQUIVALENT to comparing the legs
      with each other and I accept it as the "or equivalent" of my condition.
judge AND IT WENT RED ON ITS FIRST LIVE RUN, WHICH IS THE POINT. R293.
```

- **R285 -- MECHANICAL HALF CLOSED, SECOND CLAUSE UNMET AND RECORDED ANSWERED.** I checked
  the plan's numbers against the two runs myself, as asked, and they are exact.

```
cmd  gh run view 34434995901 --log | the ten legs at 291f096, UNPINNED
out  INTEL(R) XEON(R) PLATINUM 8573C  x3  -> FIGURES-SHA256 b0dc947f
     AMD EPYC 7763 x6 + AMD EPYC 9V74 x1  -> FIGURES-SHA256 2af0f7cb
cmd  the same log, which legs carry the 2612174795 ULP breach
out  legs 1, 2, 4 -- and legs 1, 2, 4 are EXACTLY the three Intel legs.
     "exists on Intel and nowhere else" is verified, not accepted.
cmd  gh run view 34435454388 --log | the ten legs at 73cf6ce, PINNED
out  2af0f7cb on all ten; AMD EPYC 7763 x7, INTEL 8573C x1, Intel 8370C x1,
     Intel Xeon 6973P-C x1. Four models, including the one that had failed.
judge EVERY FIGURE IN THE NEW PLAN SECTION CHECKS OUT. The re-lock route was
      taken, the standard is stated in the plan's own words -- "canonical
      status requires DEMONSTRATED run-to-run byte-identity" -- and it is the
      right standard.
cmd  grep -rn "OPENBLAS_CORETYPE\|Haswell" tests/ floatfea/ scripts/
out  (nothing)
cell the pin deleted from ci.yml, nothing else, guards job body at a949709:
out  463 passed, 0 failed
judge MY CONDITION HAD TWO CLAUSES AND THE SECOND IS WORD FOR WORD UNMET: "and
      a check exists that reddens when it is removed". The ablation I ran last
      round gives the same answer this round. R295, and the row says answered.
```

- **R286 -- NOT CLOSED, and the fifth shape you invited exists twice over.** The two named
  shapes do redden and I measured both. The sentence about the reach is false.

```
cell the shipped script, a scratch tree carrying the project's `addopts`:
out  xfail reason "1 passed on the reference build"
       73cf6ce script -> run_rung: OK   exit 0        MISSED
       a949709 script -> run_rung: FAIL exit 1        FIXED
     parametrize id "3 passed"
       73cf6ce script -> run_rung: OK   exit 0        MISSED
       a949709 script -> run_rung: FAIL exit 1        FIXED
cell the a949709 script, two channels neither -rN nor --no-header reaches:
out  warnings.warn("3 passed in 0.01s") inside an xpassing test
       -> "1 xpassed in 0.22s" on screen;  run_rung: OK   EXIT 0   MISSED
     conftest pytest_terminal_summary writing "5 passed in 0.01s"
       -> "1 xpassed in 0.25s" on screen;  run_rung: OK   EXIT 0   MISSED
     a CLEAN passing rung warning "1 xpassed in 0.01s"
       -> run_rung: FAIL, quoting the UserWarning       FALSE POSITIVE
     a module-level print at collection
       -> run_rung: FAIL                                CONTROL, closed
judge R272 CONDITION IS REACHED AGAIN, THROUGH A THIRD AND A FOURTH DOOR,
      and the mirror-image fault this file own comment records as fixed
      once already is back with it. R294.
cell AND THE SHIPPED LAYOUTS CANNOT FAIL. -rN --no-header deleted from
     run_rung.sh, the four layouts added at bcaad88 re-run:
out  shipped: 4 passed, 39 deselected
     ablated: 4 passed, 39 deselected      IDENTICAL
judge _run builds the layout in a bare tree with no pyproject.toml, so
      addopts = -ra -- the setting that makes the whole attack possible -- is
      absent, and the same forged reason is caught by pytest default. The
      repair is real and the evidence shipped for it certifies nothing.
```

- **R287 -- MECHANICAL HALF CLOSED, AND THE HAND-WRITTEN HALF IS SHIFTED BY ONE.**
  `scripts/carried_table.py` is committed and its class logic is correct -- I ran it and
  reproduced the generated rows. The rows that matter are the hand-written ones. R296.

- **R288 -- CLOSED, and I ran the ablation rather than counting call sites.**

```
cmd  grep -n "_assert_diagnosis" tests/test_report_guard_states.py
out  310 def, 363 call (the REQUIREMENT_CHANGED branch), 394 call
cell DIAGNOSIS["shallow_clone_depth_1"] must-name replaced with a name that
     exists nowhere, one variable, at a949709:
out  FAILED test_the_guard_survives_the_state[shallow_clone_depth_1]
     "the guard failed, but ... is not among [...]"
judge THE ENTRY IS REACHABLE AND IT REDDENS. Answered.
judge ITS ROW, HOWEVER, IS NUMBERED R289. R296.
```

- **R289 -- NOT CLOSED. You asked me to check and you were right to.**

```
cmd  grep -rn "report_status_vocabulary" --include=*.py --include=*.yml
     --include=*.sh --include=*.toml .
out  (nothing outside tests/corpus/)
judge NO RUNNER. Word for word the state of the last two rounds. R297.
cmd  for f in tests/corpus/*.txt; do (search the tree for a reader); done
out  11 files; 4 have a runner. That is R281, grown by two -- both of the two
     are mine, this round, and I record that against myself.
```

- **R290 -- NOT ANSWERED, THIRD ROUND RUNNING, and recorded answered.**

```
cmd  sed -n 1449,1712p docs/reports/F2/step-5.md | grep -in "rung 6|rung6"
out  (nothing)
cmd  grep -n "rung6" .github/workflows/ci.yml ; ls -a tests/verification/rung6
out  312: sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
     .empty-by-design present
judge THE SUBSTANCE IS DONE AND HAS BEEN FOR THREE ROUNDS. What is asked is one
      sentence, and this is the third revision in which the row says it was
      written and it was not. R298.
```

- **R291, R292 -- OPEN, recordable at 4a, correctly recorded.**

- **R231, R244, R245, R275, R230, R223, R224 -- OPEN by instruction, and correctly listed
  as open in the report section 5.** Site by site, confirmed untouched:
  `floatfea/tolerances.py:293`, `:295-297`, `:300-308`;
  `tests/verification/rung1/test_rigid_body_modes.py:19`, `:175-177`;
  `docs/milestones/F2.md:51`, `:1477`, `:1491-1492`. **R275 re-measurement is now blocked
  by R293 rather than by R285** -- the pin exists and the demonstration it was supposed to
  enable does not complete on any leg.

- **R261 -- OPEN, correctly.** No Q8 value was written. Said again, and it remains the
  right call.

- **R253, R254, R256, R257, R262, R263, R264, R265, R266, R267, R268, R269, R270, R271,
  R272, R273, R274, R276, R277, R281, the two R248 residues, R249, R250, R251, R252,
  R225-R228, R232, R233** -- carried. R271 mechanical half and R272 remain fixed in
  the code; R271 runner clause is R297 and R272 shape is R294.

## Findings

**R293. (BLOCKS -- head 2, the Q8 basis, and CA2) The determinism job first live run
under the new body failed on all ten legs, the goldens now execute on no CI job at all,
and the only cross-runner quantity the job has is printed on zero legs. The report CI
section describes a different commit and says the only reds are two.**
`.github/workflows/ci.yml:99-116`; `docs/reports/F2/step-5.md`, section 0.

```
cmd  gh run view 34440129351 --log | the ten legs at a949709
out  COMMITTED-SHA256 545f74b6...  on all ten -- identical BY CONSTRUCTION,
     since every leg hashes the same git checkout. It carries no information.
     regen_figures: F2_figures.md is not what this script produces at HEAD
       on ALL TEN, exit 1, on four CPU models, WITH the kernel pinned.
     FIGURES-SHA256  printed on 0 of 10 legs.
     the regression rung step  SKIPPED on 10 of 10.
judge THE COMMITTED FIGURES FILE IS A LAPTOP RENDER, and the new comparison is
      what says so. CI prints ch_edgemin_D0p0758_roll1p05_aniso9p4e5 at
      detection edge 3.6425e-14 where the committed file and my local run give
      ci_plateau_D0p0689_roll1p017_aniso9p6e5 at 3.6275e-14. Different corpus
      entry, different edge -- not a last-bit disagreement.
judge THIS IS THE COUPLING WORKING AND IT IS ALSO A RED CI. CA2 is not
      discretionary and the red is not a routed item.
judge TWO MEASUREMENTS WERE LOST WITH IT. --check and the FIGURES-SHA256 print
      share one run: block under bash -e, so a failing comparison suppresses
      the render hash on every leg; and pytest tests/regression is the step
      after it. tests/regression executed TEN times on CI at 73cf6ce and ZERO
      times at a949709. Ladder 6 is still skipped behind a red ladder 4, so the
      goldens now run nowhere on the machine Q8 makes canonical for them.
judge AND A VENDOR SPLIT WOULD NOW BE INVISIBLE. Two legs rendering different
      bytes, with the committed file matching neither, produces exactly the log
      this run produced: ten identical failure messages and no hash.
code report section 0 publishes a CI table for 73cf6ce and states "Both reds
     are the sine and cosine round-trip comparisons, open under Q8."
judge AT THE COMMIT THE REPORT IS WRITTEN AT THERE ARE TWELVE RED JOBS AND TEN
      OF THEM ARE NEITHER SINE NOR COSINE. The report cannot have known -- the
      run started after it -- and that is exactly why the sentence should not
      have been written in the present tense about a commit it does not name.
judge THE PLAN ALREADY NAMES THE MECHANISM THAT WOULD HAVE PREVENTED THE STATE.
      docs/milestones/F2.md:1039-1043: "a golden or figure whose stamp is not
      CI pinned environment fails the build, so no canonical file can be
      produced on a laptop again." docs/milestones/F2_figures.md carries no
      stamp -- head -6 is a title, a provenance sentence and a table header.
cmd  tests/corpus/ci_determinism.txt, entries
     determinism_committed_figures_were_produced_on_a_NON_canonical_machine,
     determinism_the_goldens_execute_on_no_CI_job_at_all,
     determinism_a_vendor_split_in_the_RENDER_hiding_behind_a_stale_committed_file
```

**Closed when** the determinism job reaches green on all ten legs -- the canonical figures
regenerated on CI and committed from there, with the explanation the golden-file rule
requires -- **or** the job is restructured so that a stale committed file and a vendor
split are distinguishable in the log and `tests/regression` still executes; and the
report CI section names the commit it describes.

**R294. (BLOCKS -- head 3, and it is the ladder own gate) `-rN --no-header` closes two
doors and the sentence claims it closed the corridor. Two more streams put text the test
tree controls ahead of pytest count line, the same channel reddens a rung that skipped
nothing, and the four layouts shipped as evidence pass with the repair deleted.**
`scripts/run_rung.sh:130-136`, `:148-157`; `tests/test_ci_ladder_gating.py:133-172`,
`:306-318`; `docs/reports/F2/step-5.md`, section 4.

```
code run_rung.sh:135  "With the short summary off, THE FIRST COUNT LINE IS
                       PYTEST OWN."
code the report section 4, the same sentence, and "all four of the reviewer
     shapes now redden"
cell the a949709 script, project addopts present, one variable moved:
out  an xpassing test whose body calls warnings.warn("3 passed in 0.01s")
       -> the warnings summary prints BEFORE the count line
       -> "1 xpassed in 0.22s" on screen;  run_rung: OK   EXIT 0
     a conftest pytest_terminal_summary writing "5 passed in 0.01s"
       -> "1 xpassed in 0.25s" on screen;  run_rung: OK   EXIT 0
judge NEITHER IS A SHORT SUMMARY AND NEITHER IS A HEADER, so neither flag
      touches them. -ra was one producer of pre-summary text; it was not the
      only one, and the fix was aimed at the producer rather than at the rule.
cell the mirror image, same channel:
out  an ordinary PASSING test warning "1 xpassed in 0.01s", nothing skipped,
     nothing xfailed
       -> run_rung: FAIL, quoting the UserWarning line.   EXIT 1
judge THIS FILE OWN COMMENT AT :143-145 RECORDS THIS EXACT FAULT AS FIXED:
      "Grepping the whole output matched a PASSING test whose own diagnostic
      contained the word, and reddened a rung that had skipped nothing." It is
      back, in the direction that turns a green rung red.
cell the evidence, ablated -- -rN --no-header deleted, nothing else:
out  pytest tests/test_ci_ladder_gating.py -k xpass
       shipped: 4 passed, 39 deselected
       ablated: 4 passed, 39 deselected      IDENTICAL
judge _run writes the layout into a bare tmp_path with no pyproject.toml, so
      the project addopts = -ra is absent and pytest prints no short summary
      with or without the flag. The four new layouts pass whether or not the
      thing they were added to prove is present. Ask the standing question of
      them: if the repair were absent, would they go red? No. Measured.
judge THE PREVIOUS VERDICT NAMED THE SHAPE OF THE ANSWER AND IT IS STILL THE
      ANSWER: pytest own machine-readable count of unexpected passes, from a
      terminal-summary or session-finish hook reading the reporter xpassed
      stat. Every repair aimed at the TEXT has held for exactly one round.
cmd  tests/corpus/ci_ladder_gating.txt, the five entries added at a7b0e23
```

**Closed when** neither the warning channel nor a terminal-summary hook reaches exit 0,
and a clean rung whose warning text contains `xpassed` stays green -- all three shown as
runs; the layouts that carry the claim run under the project `addopts`, demonstrated by
the repair removal turning them red; and the sentence at `run_rung.sh:135` says what the
reach is.

**R295. (BLOCKS -- head 2, a tolerance basis) The plan half of R285 is done and verified.
The clause "and a check exists that reddens when it is removed" is untouched, unmentioned,
and the row says answered.** `docs/milestones/F2.md:1047-1076`;
`.github/workflows/ci.yml:25`; `docs/reports/F2/step-5.md`, section 2 and its Carried row.

```
code verdict 32, R285 Closed when: "the kernel pin is written into Q8 as a
     condition of canonicity ... AND A CHECK EXISTS THAT REDDENS WHEN IT IS
     REMOVED -- before any Q8 value is written"
code the report Carried row: R285  answered -- section 2, the pin and its
     measurement are in the plan
code the report section 2: the plan, the measurement, the re-lock. No sentence
     about a check.
cmd  grep -rn "OPENBLAS_CORETYPE|Haswell" tests/ floatfea/ scripts/
out  (nothing)
cell the env line deleted from ci.yml, nothing else, guards job body:
out  463 passed, 0 failed
judge CLAUDE.md sec. Step gating names this shape by its own history: "Half of
      an item is not the item ... the first was fixed, the second was untouched,
      and the report recorded the item as answered." The plan now states a
      condition three canonical artifacts depend on, and that condition can
      still be deleted in silence.
judge AND THE PLAN OWN SENTENCE IS THE CLAIM THIS BEARS ON. F2.md:1073-1076
      says "The determinism job ... IS THAT DEMONSTRATION." At a949709 the
      demonstration does not complete on any leg (R293), so the plan newly
      locked sufficient condition is unmet at the commit that locked it. The
      condition is right. It is not yet satisfied, and no Q8 value may be
      written until it is -- which is the plan working, not the plan wrong.
```

**Closed when** something in the suite goes red with `OPENBLAS_CORETYPE` removed from
`ci.yml` -- shown as a run of the deletion -- or R285 row states the clause is open.

**R296. (BLOCKS -- head 3) The generator is committed and correct about class. The
hand-written rows are shifted by one: R288 carries R287 subject, R289 carries R288,
R290 carries R289. And the command published beside them cannot be run at this commit.**
`docs/reports/F2/step-5.md`, section 4 and the Carried table; `scripts/carried_table.py`.

```
code verdict 32 headings, verbatim: R287 = the table and its generator;
     R288 = R276 row and _assert_diagnosis; R289 = R271 runner clause;
     R290 = verdict 31 condition 8, the rung-6 restoration.
code the report table:
     | R288 | answered -- the four rows are generated from the headings |
                                            <- that is R287 subject
     | R289 | answered -- _assert_diagnosis has two call sites |
                                            <- that is R288 subject
     | R290 | answered -- the vocabulary corpus runner |
                                            <- that is R289 subject, and it
                                               does not exist (R297)
judge R267 WAS SIX ROWS ATTACHED TO THE WRONG FINDINGS. R287 WAS FOUR ROWS
      ATTACHED TO THE WRONG STATUS. THIS IS THREE ROWS ATTACHED TO THE WRONG
      SUBJECT, and the item that falls off the end of the shift is R290 --
      which is the one that has now gone unanswered for three rounds. The
      table is not untidy; it is doing damage.
cmd  python scripts/carried_table.py docs/reviews/F2/step-5.md (empty json)
out  11 rows, R282..R292, classes correct -- the GENERATED half is right and
     I reproduced it. answered.json is what carries the three wrong rows.
code the report section 4:
     cmd python scripts/carried_table.py docs/reviews/F2/step-5.md answered.json
     out "the table in section 7, verbatim"
cmd  ls answered.json ; git ls-files | grep answered
out  No such file; nothing tracked.
judge THE PUBLISHED COMMAND CANNOT BE RUN. answered.json is not committed and
      neither is the third argument the 49-row order needs, so the command as
      written prints 11 rows against a committed 49 -- and the table it points
      at is in section 6, not section 7. R287 was "a generator that does not
      exist"; this is a generator whose inputs do not exist. BF0: a claim
      without a command that refutes it is not written, and a command that
      cannot be run is the same thing one level in.
cmd  grep -rn "carried_table" --include=*.py --include=*.yml --include=*.sh .
out  only the script own docstring. Nothing runs it. R301.
cmd  tests/corpus/carried_row_subject.txt, 9 entries, 2 correct
```

**Closed when** each of the three rows states what verdict 32 ruled for that number, the
inputs the published command needs are committed or the command is replaced by one that
runs, and the section reference is right.

**R297. (BLOCKS -- head 3) R271 unconditional clause is unmet for a third round and the
row says answered.** `docs/reports/F2/step-5.md`, the Carried row;
`tests/corpus/report_status_vocabulary.txt`.

```
cmd  grep -rn "report_status_vocabulary" --include=*.py --include=*.yml
     --include=*.sh --include=*.toml .
out  (nothing outside tests/corpus/)
code verdict 31, R271: "-- and tests/corpus/report_status_vocabulary.txt has a
     runner EITHER WAY."
judge YOU ASKED ME TO CHECK BECAUSE YOU BELIEVED IT DID NOT EXIST. It does not.
      That is the right instinct and it is also the reason the row should not
      have said answered before the grep was run.
```

**Closed when** `tests/corpus/report_status_vocabulary.txt` induces a failure when an entry
disagrees with the guard, shown as a run -- or the row says the clause is open.

**R298. (BLOCKS -- head 3, and it is an unanswered gated item for the third consecutive
round) Verdict 31 condition 8, carried as verdict 32 R290, is still one unwritten
sentence, and the table says it is written.** `docs/reports/F2/step-5.md`, the Carried
row; `.github/workflows/ci.yml:312`.

```
cmd  sed -n 1449,1712p docs/reports/F2/step-5.md | grep -in "rung 6|rung6"
out  (nothing)
cmd  grep -n "rung6" .github/workflows/ci.yml ; ls -a tests/verification/rung6
out  312:  sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
     .empty-by-design present
judge THE SUBSTANCE IS DONE. I have now verified it three times. What is being
      asked for is a sentence in the report, it has been asked for three times,
      and three times the row has recorded it as given. This is the failure the
      whole arrangement exists for, in CLAUDE.md words: the dependency list is
      part of what gets re-read.
judge AND IT IS THE ITEM AT THE END OF R296 SHIFT. The two are one defect.
```

**Closed when** the report states that `ci.yml:312` carries
`empty:tests/verification/rung6 full:tests/regression` and that
`tests/verification/rung6/.empty-by-design` is present -- or says why it will not.

**R299. (BLOCKS -- head 3) A published figure is the previous commit number.**
`docs/reports/F2/step-5.md`, section 3.

```
code the report section 3:  out "at HEAD: 197 passed"
cmd  python -m pytest tests/test_report_carried.py -q      (at a949709)
out  174 passed
cmd  the same, at 73cf6ce
out  197 passed
judge THE FIGURE IS EXACT AND IT IS THE PREVIOUS COMMIT ONE. The count is
      parametrised over the sites the verdict names, so it moves with every
      verdict; nothing re-takes it. CLAUDE.md sec. Step gating: "Every figure
      is regenerated by running the shipped tests at the report own commit;
      no number is carried across from working notes, because a measure that
      changed underneath it makes the figure quietly stale." This is BP0
      exactly, and the number was correct when it was taken.
```

**Closed when** the figure carries the count at the report own commit.

**R300. (recordable, 4a) The new ancestry check adds a third failure to the shallow-clone
state, and the corpus state that models that clone cannot observe it.**
`tests/test_report_carried.py:264-303`; `tests/test_report_guard_states.py:101-108`,
`:310-323`. In a `--depth 1` clone at a949709, `tests/test_report_carried.py` gives
**3 failed, 171 passed**: the two designed reporters plus
`test_the_answered_verdict_is_the_NEWEST_one`, because `git log -1 -- path` returns the
same single commit for report and verdict, the `head_report != head_verdict` guard is
false, and the assertion is reached. `DIAGNOSIS["shallow_clone_depth_1"]` asserts one
must-name present and one must-not-name absent; a third, unrelated failure satisfies both.
The state the repository explicitly models has changed under it and the model says
nothing. CI sets `fetch-depth: 0` on every job, so this is not live -- which is why it is
recordable and not a block.

**R301. (recordable, 4a) `scripts/carried_table.py` is executed by nothing.**
`grep -rn "carried_table" --include=*.py --include=*.yml --include=*.sh .` matches only
the script own docstring. It is not imported by a test, not named by a CI job, and its
output is never compared with the committed table. `tests/test_ci_runs_the_whole_suite.py`
constrains `tests/`, not `scripts/`, so a generator that stops matching what it generates
is a silent state. The script is good and its docstring is honest about what it does; the
gap is that nothing holds the table to it.

## Tolerances touched

**None by this diff.**

```
cmd  git diff 49c8449..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 49c8449..HEAD -- floatfea tests/regression
     docs/milestones/F2_figures.md
out  (empty) -- not one line of floatfea/, no golden, no figure
judge A NINTH ROUND. EXEMPT_RESPONSE_DRIFT_ULP = 4.0 has had a red CI and an
      obvious one-character fix in front of it for nine rounds and has not been
      touched, and this is the round in which that patience is vindicated
      twice over: the number would have been one vendor, and the file it would
      have been measured from turns out not to be what CI produces at all.
```

**The tolerance findings this round are R295 and R293**, and neither is a value. R295 is
Q8 stated condition still lacking the machine that holds it. R293 is the basis itself:
`docs/milestones/F2_figures.md` as committed is not what the canonical machine renders, so
every platform-dependent tolerance that would be written from it would be written from a
laptop.

**The plan change, checked.** `e4f1b45` touches `docs/milestones/F2.md` and nothing else,
carries RE-LOCKED and the directive (R285) in its message, and lands before the step
commit. The addition is 32 lines, entirely additive, and every number in it I verified
against the two CI runs above. **This is the best-supported paragraph in the plan.**

**My own instructions (item 4b).**

```
cmd  git diff 49c8449..HEAD -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" 49c8449..HEAD with per-commit file lists
out  e4f1b45  docs/milestones/F2.md            -- no docs/reviews/, no .claude/
     bcaad88  ci.yml, 3 scripts, 3 tests files -- the same
     a949709  docs/reports/F2/step-5.md        -- the same
judge No commit touches both code and docs/reviews/. No commit touches .claude/
      or docs/SUPERVISOR.md at all, so the STOP-class condition is not in play.
      CLEAN.
```

**What held**, reproduced at my run rather than read: the ancestry check green at the
boundary and red on the defect, both as runs; `--check` refusing a garbage file and a
deleted file without overwriting either; the two forged-summary shapes reddening under the
project own `addopts`, with the pre-fix script as the control; `_assert_diagnosis`
reachable from the `REQUIREMENT_CHANGED` branch and reddening under ablation; the
generator class logic reproduced by running it; the plan ten-leg measurement verified leg
by leg, including that the ULP breach appears on legs 1, 2 and 4 and those are exactly the
three Intel legs; the re-lock route taken in a standalone commit; and
`floatfea/tolerances.py` untouched for a ninth round.

**These did not**: CI at the reviewed commit (R293), the rung count line (R294), Q8
enforcement clause (R295), three Carried rows and the command beside them (R296), R271
runner (R297), the rung-6 sentence for the third time (R298), and a figure from the
previous commit (R299).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Seven blocking items. **R293 is the head and
it is not a criticism -- it is what the round bought.** The comparison you built went red
on its first live run and said something nothing in this repository could previously say:
the canonical figures file was never produced on the canonical machine.

1. **R293 -- the goldens and the figures, on CI.** The canonical `F2_figures.md`
   regenerated on the runner and committed from there, with the written explanation the
   golden-file rule requires; the determinism job green on all ten legs, or restructured
   so a stale file and a vendor split are distinguishable and `tests/regression` still
   executes; and the report CI section naming the commit it describes. **No Q8 value is
   written before this**, which is what the plan you just locked says.
2. **R295 -- Q8 condition, held by a machine.** Deleting `OPENBLAS_CORETYPE` from
   `ci.yml` turns something red, shown as a run. Three lines, and it is the last clause of
   the item the round was about.
3. **R294 -- the ladder gate, at the rule rather than at the text.** The warning channel
   and the terminal-summary hook do not reach exit 0; a clean rung warning `1 xpassed`
   stays green; the layouts run under the project `addopts` and are shown to go red with
   the repair removed. Every fix aimed at the string has lasted one round; the reporter
   `xpassed` stat has not been tried.
4. **R296, R297, R298, R299 -- the dependency list and one figure, four sites.** Three
   rows restated against verdict 32 own headings; the generator inputs committed or the
   command replaced; the vocabulary runner met or declared open; the rung-6 sentence
   written; the 197 re-measured at the report own commit.
5. **R231, R244, R245, R275, R230, R223, R224 -- unchanged and open by instruction.** R275
   now waits on item 1 rather than on R285.

**Not gates on step 5, into the next report Carried section:** R300, R301, R291, R292,
the underlying gap in R276, R277-R281, R262, R264, R266, the two R248 residues, R249,
R250, R251, R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 21 new entries at `a7b0e23`, across three files, one of them
new, all unseen by the implementer; every measured field taken at `a949709` before the
require beside it was written.**

**The coverage measurement, stated plainly: of my 21 new entries the shipped checks do
what the entry requires on 7.** With the corpus applied,
`tests/test_ci_ladder_gating.py` gives **7 failed, 41 passed**; the two files without a
runner induce zero failures, which is R281 -- and it has grown by two, both of them mine.

* `tests/corpus/ci_ladder_gating.txt` -- **+5 (41 -> 46), 2 correct.** The module-level
  print stays closed and the reason shape reddens under the project `addopts`. The warning
  channel and the terminal-summary hook do not, and the same channel reddens a clean rung.
* `tests/corpus/ci_determinism.txt` -- **+8 (6 -> 14), 3 correct.** The garbage file, the
  deleted file and the laptop render are all caught now, which is R284 repair working. The
  pin deletion, the lost render hash, the goldens running nowhere and the missing
  environment stamp are not.
* `tests/corpus/carried_row_subject.txt` -- **NEW, 9 entries, 2 correct.** Both correct
  ones are controls. Nothing in the suite compares a row text with what the verdict said
  about that number -- the sentence I wrote for R267, then for R287, and now for R296.

**Thirty-three consecutive rounds have found no element defect, and this round does not
either.** `git diff 49c8449..HEAD -- floatfea` is empty. What this round found is one
thing wearing three faces, and it is the same one as last round: **a check verified
against inputs its own author designed.** The four xpass layouts were built in a tree that
cannot produce the defect they were written for, and they pass with the repair deleted.
The forged-count-line rule was repaired at the producer it had just seen, and two other
producers were never enumerated. The Carried table gained a generator, and the rows the
generator does not write are shifted by one.

**And the best thing in the range is not a guard either -- it is a red build.** A reviewer
asked for a comparison, the comparison was built, it ran on ten machines, and it
immediately contradicted something everyone had been assuming: that the file in git was
the file CI produces. Nobody had to argue for that; the machine said it. That is the
arrangement working, and it is why this is a HOLD and not a STOP -- the plan answer to Q8
is intact and newly better evidenced, ladder 1 is green, `floatfea/` is untouched, and
what is red is red about the right thing for the first time.
