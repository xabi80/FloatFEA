# Review — F2 step 5
Reviewed commit: f3540255ebc5f2e158af8404b2daba7dfa15f4d6
Verdict: HOLD

Tests: **1655 passed, 0 failed, 0 skipped** (my run at `37799aa`, `python -m pytest -q`,
189.54 s, Python 3.13 on Windows). The report states `1626 passed` at its own moment; the
difference is the 29 corpus rows the report itself added, and the two counts do not
disagree about anything. With my twenty-ninth-round corpus applied at `f354025`: **33
additional failures** across the three harnesses.

**AND THE LOCAL NUMBER IS NOT THE NUMBER THAT DECIDES THIS STEP.** CI at the reviewed
commit is red in the job this step created, with failures that are not R231's thirteen:

```
cmd  gh run list --commit 37799aa --json name,conclusion,workflowName
out  CI  failure  (completed)  + one in_progress run
cmd  gh run view 34388632233 --json jobs
out  guards and meta-tests  FAILURE          <- new in this range
     unit tests             success
     lint and type-check    success
     ladder 1 / 2 / 3       success
     ladder 4               failure          <- R231, 13 failed 72 passed
     ladder 5, ladder 6     skipped
cmd  the guards job's own summary line, both commits in this range
out  4a8d2a3   62 failed, 297 passed in 202.83s
     37799aa   30 failed, 329 passed in 127.99s
```

CA2 is not a preference: **a red CI is a HOLD regardless of what the local run says.**
The job R235 asked for exists and runs 359 tests, which is real work and I record it as
such. It is also red, and the report does not say so.

## Carried

Step 5 is HOLD at `8e7418f` (verdict 28). **Seven items were listed under "Next step
opens when". Two close. Two are answered in mechanism and refuted in their published
form. Three are untouched by declaration.** Plus one item the report records as closed
that the verdict it answers records as carried.

- **R236 -- CLOSED.** `.github/workflows/ci.yml:71-80` now states what adding the first
  test to an `empty:` rung costs.

```
cmd  git diff 8e7418f..HEAD -- .github/workflows/ci.yml
out  the sentence "adding a test to a rung is a matter of dropping a file into
     tests/verification/rungN/ -- not a CI edit" is DELETED and replaced by
     "the first test makes the declaration stale and the job FAILS. Delete the
     marker and change empty: to full: in the same commit. That is a CI edit".
cell my own layout, re-run at 37799aa in a scratch tree: rung2 declared empty:,
     marker present, one passing test dropped in -> EXIT=1, "declared empty and
     collects tests. The declaration is stale". The sentence now matches the rule.
```

- **R237 -- CLOSED, the sentence.** `tests/test_no_tolerance_literals.py:27-34` now says
  "**The left operand is not read** (R237): `assert 0.05 > ratio` returns nothing", names
  the two live sites, and routes the reach to 4a. That is one of the two branches I said
  would close it, and it is the honest one. The reach stays 4a and I have widened the
  corpus around it (R249).

- **R238 -- CLOSED as written, and I re-measured two of the four rather than reading
  them.** Three NEW residues in the same file are R248 below; the item as I wrote it is
  answered.

```
cell shipped scripts/run_rung.sh at 37799aa, scratch tree:
     (c) full:rung1 with one passing and one failing test
           -> EXIT=1, last line is the pytest summary. NO "OK" line.       FIXED
     (c) empty:rung2(marker) full:rung1(failing)
           -> EXIT=1, no "OK" line.                                        FIXED
     (a) full:rung1 whose only test is @pytest.mark.skip
           -> EXIT=1, "a test in ... was skipped. CLAUDE.md: never skip".  FIXED
     (b) full:rung1 populated AND carrying .empty-by-design
           -> EXIT=1, "declared full and still carries .empty-by-design".  FIXED
```

- **R239 -- CLOSED.** Section 3's `out` fields are pasted.

- **R234 -- NOT CLOSED. Answered for the six states I wrote and refuted by the seventh.**
  The three changes are real and I verified each: `_read` returns `""` on `OSError`, the
  carry comparison runs against `max(REPORTED & REVIEWED)`, and the empty parametrise is
  a named placeholder rather than a collection error. Six of six states now collect and
  report by name on this machine. **But the closing condition was "the guard inputs are
  the states that actually occur", and two states that occur still do not report**: R246
  (the module still raises at import on an input the docstring says it never raises on,
  and the suite then runs zero tests) and R247 (the harness that certifies all of this is
  red on CI, including its own baseline, and its collection detector fires on the wrong
  condition). Condition (ii) -- "the same when `docs/reports/F2/` cannot be read" -- is
  GREEN here and RED on CI.

- **R235 -- ANSWERED IN MECHANISM, REFUTED IN ITS PUBLISHED FORM.** The `guards` job
  exists, it names every top-level `tests/*.py`, and `test_ci_runs_the_whole_suite.py` is
  not vacuous in the way its first version was -- I checked that myself rather than
  reading it (R250 records what I could and could not exhibit). The closing condition was
  "shown by a CI log line with a pass count covering them". There is a log line and it
  carries **30 failed, 329 passed**. A pass count that is also a fail count does not close
  an item whose whole content was that a claim about CI had never been measured.

- **R230 -- STILL CARRIED, AND THE REPORT RECORDS IT AS CLOSED.** This is R242 below.

- **R231 -- OPEN BY INSTRUCTION (Q8), and its number is now known to be an undercount.**
  Thirteen was the ladder-4 count. R244 adds two more of the same species in the guards
  job and one more masked behind a skipped ladder 6. Not offered as answered and not
  treated as such; what I record is that "the same 13" no longer bounds the set.

- **R223, R224 -- OPEN BY INSTRUCTION (Q7).** Site by site, unchanged in this range:
  `floatfea/tolerances.py:293`, `tests/verification/rung1/test_rigid_body_modes.py:19` and
  `:175-177`, `docs/milestones/F2.md:51`, `:1477`, `:1491-1492`; and
  `floatfea/tolerances.py:295-297`, `:300-308`. Confirmed untouched:
  `git diff 8e7418f..HEAD -- floatfea` is empty.

- **R225-R228, the R232 residue, the remaining half of R233, and everything already at
  4a** -- carried, unchanged, correctly classified in the report's section 5.

## Findings

**R240. (BLOCKS -- CA2) CI is RED at the reviewed commit, in the job this step added, and
the failures are not R231's.** `.github/workflows/ci.yml:34-53`, run `34388632233`.

```
out  guards and meta-tests: 30 failed, 329 passed in 127.99s at 37799aa
     by file:  test_report_carried.py            25
               test_report_guard_states.py        4  (including `baseline`)
               test_counters_are_injected.py      2
               test_plan_figures.py               1
judge R231 is ladder 4 and it is 13 failed / 72 passed on this same run. None of
      these 30 is one of those 13, and none of them is offered as open by
      instruction anywhere in the report.
judge THE JOB IS THE RIGHT WORK. 359 guard tests now execute on a machine neither
      of us controls, for the first time in this milestone, and four separate
      defects fell out of that on the first attempt. That is exactly what CA2
      predicts and it is the strongest thing in this range. It is also why the
      step cannot close on it: the measurement was taken and it came back red.
```

**Closed when** the `guards` job is green at the reviewed commit, or every failure in it
is routed by name -- to Q8, to 4a, or to a fix -- and the routing is in the report with
the run id and the count beside it.

**R241. (BLOCKS -- head 3) The report's CI section is not what CI says.**
`docs/reports/F2/step-5.md:651-655`.

```
code :655  "The `guards` job is new and runs for the first time on this commit."
cmd  gh run list --limit 10 --json headSha,conclusion,createdAt
out  4a8d2a3  failure  2026-09-09T18:14:38Z   <- the guards job ran HERE
     37799aa  failure  2026-09-09T18:22:48Z   <- the report commit
cmd  the guards job's summary line in the 4a8d2a3 run
out  62 failed, 297 passed in 202.83s; last log line at 18:18:24Z
judge The job first ran on 4a8d2a3, which is "the previous commit" the same
      paragraph reports rungs 1-4 for, and it finished RED four minutes before
      the report was committed. The paragraph enumerates every other job's
      outcome at that commit and omits the one this revision introduced.
judge I am not ruling on intent and I do not need to. BF0: every sentence that
      states a fact about the code carries the command that would refute it. One
      `gh run view` refutes this one, and the fact it withholds is the fact the
      step turns on.
```

**Closed when** `:651-655` states the guards job's result at the commit the report is
committed at, with the run id and the counts, or is withdrawn.

**R242. (BLOCKS -- head 3) The report records R230 as closed at the third verdict. The
third verdict records it as carried, in the sentence that names it.**
`docs/reports/F2/step-5.md:442` and `:601`; `docs/reviews/F2/step-5.md:95-96`.

```
code report :442  "R229 and R230 closed at the third verdict."
code report :601  "| R230 | **closed** at the third verdict |"
cmd  grep -n "R230" docs/reviews/F2/step-5.md
out  :95  "**R230 -- MECHANISM VERIFIED, CLOSING CONDITION NOT MET. Carried, not
           closed, and it closes when R231 does.**"
     :477 item 4 of "Next step opens when": "R230 -- tests/regression
           demonstrably executed by ladder 6 on CI, a log line with a pass count
           from that path."
cmd  the ladder 6 job's conclusion on every CI run this branch has produced
out  skipped, on all of them. `tests/regression` has never executed on CI.
judge THE CONDITION IS UNMET AND THE FACT IS UNCHANGED SINCE I WROTE IT. What
      moved is the record of it. This is the exact failure the arrangement exists
      to prevent -- an open dependency recorded as discharged -- and it is the one
      species running the suite cannot catch, because test_report_carried checks
      that R230 is MENTIONED in Carried, never that the status beside it is true.
      Its own docstring says so at :48-50.
```

**Closed when** the report's Carried row for R230 says carried-not-closed, and section 0
stops saying it closed at the third verdict.

**R243. (BLOCKS -- head 3, and it is the machinery R235 installed) The carry guard cannot
run in the checkout CI gives it. 23 false accusations, and the cause is fetch depth, not
platform.** `tests/test_report_carried.py:282` and `:186`.

```
cell ONE MACHINE, ONE COMMIT, ONE INTERPRETER, one variable moved:
       git clone           file://<repo> full     -> 122 passed
       git clone --depth 1 file://<repo> shallow  -> 23 failed, 99 passed
     `actions/checkout@v4` with no `fetch-depth:` is the shallow one.
code :282  out = subprocess.run(["git","diff","-U0",reviewed], ...)
           out.returncode is NEVER READ; on failure stdout is empty and
           _changed_lines() returns {}, which is indistinguishable from "the step
           touched nothing". Every named site then falls through to the
           `no change` scan and fails.
code :186  subprocess.run(["git","cat-file","-e",ANSWERED]) -> 128,
           "fatal: Not a valid object name 8e7418f", so
           test_the_report_names_the_verdict_it_answers accuses the report of
           answering a verdict that is not a commit. It is a commit. The clone
           does not have it.
judge THIS IS HEAD 3 AND I AM NOT SPLITTING IT TO 4a. The guard's whole purpose is
      to make the dependency re-read mechanical; R235's whole content was that it
      had never run where it matters; and the answer put it somewhere it cannot
      run. This repository has already recorded once what happens when `pytest` is
      red by construction -- green stops meaning anything exactly where it is
      needed -- and 23 of 122 is that, on the only machine neither of us controls.
judge AND THE FAILURE DIRECTION IS SAFE, WHICH IS WHY IT IS CHEAP: an empty
      touched-set makes the check STRICTER, never looser, so nothing is hidden.
      What is broken is that the check cannot tell "git could not answer" from
      "the answer is no", and one return-code test separates them.
```

**Closed when** the guard either fetches the depth it needs, or detects that it cannot
compute the diff and says so through a named test instead of through every site -- shown
as a run in a `--depth 1` clone, not asserted. `tests/corpus/report_guard_states.txt`
carries the state as `shallow_clone_depth_1`.

**R244. (BLOCKS -- head 2, a tolerance and its form) `EXEMPT_RESPONSE_DRIFT_ULP = 4.0` is
a bit-exactness ceiling on a quantity that is not bit-reproducible across platforms.**
`floatfea/tolerances.py:713`, asserted at
`tests/regression/test_exempt_pair_responses.py:109`.

```
out  CI, guards job, 37799aa:
     bt_boundary_rolled_aniso_below_L513p206|dropped_shear_parameter: the response
     moved from 1.099531e-10 to 1.099531e-10, 2612174795.0 ULP of the recorded
     ratio, above 4.
     assert 2612174795.0 <= 4.0
     -- twice: test_the_counter_fails_when_its_gate_is_neutered[exempt-response
     drift] and ...its_ceiling_is_widened[exempt-response drift].
judge THE RECORDED VALUE AND THE MEASURED ONE AGREE TO SEVEN DIGITS AND DISAGREE
      IN THE LOW BITS. 2.6e9 ULP of a ratio near 1e-14/1e-14 is a relative move of
      order 1e-7 -- ordinary cross-libm drift, and the reason written beside the
      constant says the admissible move is round-off. On one platform. The form is
      right (ULP, dimensionless, counter 10.0 at :720); what does not hold is that
      the recorded measurements cover the machines the assertion runs on.
judge AND THE GATE ITSELF IS MASKED. test_every_recorded_pair_is_still_detected
      lives in tests/regression, ladder 6 is skipped on every CI run, so the gate
      has never run on CI -- only the meta-test that calls it has, in the new job.
      When R230 is finally satisfied this becomes a third failure at the same site.
judge SAME SPECIES AS R231, DIFFERENT FILE, AND I NAME IT SEPARATELY ON PURPOSE.
      R231 is scoped to ladder 4 thirteen failures and is with the technical
      supervisor as Q8. Folded into "the same 13" it will be answered by a change
      that does not reach it.
```

**Closed when** this is on Q8 list by name -- the constant, the site, and the fact that
its gate is currently masked by a skipped ladder -- or the CI failure is gone. **Not by
raising `4.0`** inside a step commit: that is the widening the rule forbids, and the
counter ordering asserted at `tests/test_counters_are_injected.py:170` means it cannot be
raised far without breaking the registry, which is that guard working.

**R245. (BLOCKS -- head 3, a published figure) `docs/milestones/F2_figures.md` does not
reproduce on CI. The generated file the locked plan cites by name is machine-specific.**
`docs/milestones/F2_figures.md:34-38`, `scripts/regen_figures.py:113-147`,
`tests/test_plan_figures.py:73`.

```
out  CI, guards job, 37799aa:
     "regen_figures: F2_figures.md is not what this script produces at HEAD"
     and the boundary probes it prints on the way:
       detection edge 3.5380e-14 at ci_plateau_D0p0689_roll1p017_aniso9p6e5
       shipped defect 2.12065e-06 is 5.994e+07x it  (passes)
       shipped defect 2.12489e-06 is 6.006e+07x it  (fails)
cmd  the committed file, this machine
out  | detection_edge | 3.6275e-14 |
     | counter_defect_over_edge | 2.757e+07x |
     | counter_headroom_room | 2.18x |
     | counter_defect_boundary | 2.174e-06 passes, 2.179e-06 fails |
judge FOUR PUBLISHED FIGURES MOVE. The edge differs by 2.5% between the machines,
      so counter_defect_over_edge becomes about 2.83e+07x, the room about 2.12x,
      and the solved boundary moves to 2.121e-06 / 2.125e-06, both printed in the
      CI log. All four are referenced from the plan as fig names, and the
      justification entry for PATCH_TEST_COUNTER_HEADROOM cites three of them by
      name precisely so they would not be typed.
judge THE MECHANISM IS THE FINDING, NOT THE 2.5%. The premise of BT0 is that a
      generated file is reproducible, and --check compares the whole file byte for
      byte. A bisected detection edge over a 158-entry corpus is not a
      bit-reproducible quantity, so test_the_generated_figures_are_not_stale is red
      on Linux by construction, and the only reason nobody had seen it is that this
      file had never run in CI. The answer to R235 is what exposed it.
judge I RECORD THE DIRECTION AS WELL AS THE FACT, because the tolerance entry
      claims one: the room fell 2.37x -> 2.19x -> 2.18x here and reads about 2.12x
      there, so the monotone-tightening argument survives. The published NUMBER
      does not describe the repository on the reference machine.
```

**Closed when** either the file contents are reproducible across the platforms CI runs, or
--check compares what is actually invariant and the machine-dependent rows say which
machine they were taken on -- with the four rows above regenerated or annotated in the
same commit as the rule that changes (BP0).

**R246. (BLOCKS -- head 3) `tests/test_report_carried.py:67-68` says `_steps` "Never
raises". It raises, and the suite then runs zero tests.**

```
code :66-68  def _steps(where): docstring reads "Step numbers with a file under
             `where`. Never raises: a directory that cannot be read is a state
             this guard REPORTS, not one it dies on."
code :69-76  try: {int(q.stem.split("-")[1]) ... if ....isdigit()}
             except OSError: return set()
cell one file added to a copy of the repository at 37799aa, nothing else changed:
       docs/reports/F2/step-[U+00B9].md          (superscript one)
       python -m pytest tests/test_report_carried.py -q
       -> ERROR tests/test_report_carried.py - ValueError: invalid literal for
          int() with base 10
          Interrupted: 1 error during collection
          1 error in 0.14s
     ZERO tests execute. That is the failure mode of R234, at HEAD, after the
     repair.
judge THE MECHANISM IS GENERAL, NOT THE CHARACTER. str.isdigit() is true for a
      strictly larger set than int() accepts -- superscripts, subscripts, circled
      digits -- so the admission test and the parse disagree, and the repair caught
      OSError because OSError was the exception it had seen.
judge I RATE THIS AS THE SENTENCE, NOT THE STATE. A superscript step number is not
      a state that occurs, and had the docstring said "never raises on a directory
      it cannot read" I would have recorded it at 4a. It says "Never raises", full
      stop, in a diff whose entire subject is a guard that took the suite down by
      raising.
```

**Closed when** `:67-68` says what it does, or `_steps` catches what it can raise. One
`except (OSError, ValueError)`, or one stricter admission test, closes it either way.

**R247. (BLOCKS -- head 3, and it is the gate on R234) The collection detector in the
R234 harness fires on the wrong condition, and its own `baseline` is red on CI.**
`tests/test_report_guard_states.py:132-135` and `:78-91`.

```
code :132  assert "error" not in log.split("=====")[-1].lower() or "passed" in log,
           with the message "the guard did not COLLECT -- it errored during import"
out  CI, 37799aa, state reports_directory_renamed_away:
     the nested run printed "FFFFF [100%]" and "5 failed in 0.05s" -- it COLLECTED
     and it named five failures -- and the harness reported "the guard did not
     COLLECT -- it errored during import, so nothing in the file ran and nothing
     was reported."
judge THE DETECTOR CANNOT DISTINGUISH A COLLECTION ERROR FROM A RUN IN WHICH EVERY
      TEST FAILED. Any AssertionError in the short summary contains the substring
      "error"; the escape hatch "or passed in log" is satisfied only if something
      passed, and in an all-red run nothing does. So the one assertion in this file
      that names the failure mode of R234 reports it on a state that is not it --
      and the mirror is worse: that same disjunct DISABLES the collection check
      entirely whenever any test in the nested run passes, which is most states.
out  CI, same run: baseline FAILED -- "expected a clean run", carrying the 23
     shallow-clone failures of R243 inside it. _build copies .git from the outer
     checkout on purpose (:82-84), so the harness inherits the history of the outer
     clone and its control cannot say whether the harness works there.
judge FOUR OF SIX STATES RED ON CI, INCLUDING THE CONTROL. On this machine the file
      is 7 passed, and section 1 of the report publishes that as the closure of
      R234 -- "7 passed -- all six of the reviewer states, none a collection error,
      every failing state reported by a named test". On the machine CA2 exists for
      it is four failures, and one of them says the opposite.
```

**Closed when** the collection check asks pytest rather than the log -- an exit code of 2,
or the word Interrupted, or a `--collect-only` probe -- and `baseline` is green wherever
the harness runs, shown in a `--depth 1` clone.

**R248. (recordable, 4a) Three new residues in `scripts/run_rung.sh`, each measured, and
one of them is the rule the fix itself cites.**

```
cell shipped script at 37799aa, scratch tree, arguments as ci.yml gives them:
     (a) full:rung1 whose only test is @pytest.mark.xfail
           -> "1 xfailed", "run_rung: OK -- 1 director(y|ies) ran", EXIT=0.
              The skip guard is a shell case on the substring "skipped", and
              "xfailed" does not contain it. CLAUDE.md forbids xfail in the same
              sentence as skip, and the comment above the guard cites that
              sentence.
     (b) no arguments at all
           -> "run_rung: OK -- 0 director(y|ies) ran", EXIT=0. A ladder step whose
              arguments are lost reports green.
     (c) tests/verification/rung1 with no full: or empty: prefix
           -> ran as full, EXIT=0. With no colon the kind becomes the whole path,
              which is not "empty", so an argument that declares NOTHING defaults
              instead of raising. The opening line of the script is "Run one rung
              of the verification ladder, with its expectation DECLARED."
     (d) a rung that skips nothing but whose PASSING test prints the word
           -> EXIT=1, false skip alarm. Live shape, not a contrivance: rung 1
              prints diagnostics through capsys.disabled() today.
     Correct on: a capitalised Empty: (treated as full, marker contradiction,
     EXIT=1), and both no-OK-line-after-failure cases from R238.
```

**Closed when** 4a rules on them. The seven layouts are at
`tests/corpus/ci_ladder_gating.txt`.

**R249. (recordable, 4a) The tolerance scanner misses 11 of 20 new shapes, and two of the
misses are the two clauses of `CLAUDE.md` Tolerances written out.**

```
cell each shape written to a file and passed to the SHIPPED offending() at 37799aa:
     CLEAN   TOL = 1e-9  ...  assert r < TOL          <- "no local literals"
     CLEAN   def check(r, tol=1e-9): assert r < tol   <- "no default arguments
                                                          carrying a tolerance"
     CLEAN   assert r > -1e-09        (UnaryOp, not Constant)
     CLEAN   float("1e-9") / 10**-9 / 1e-09 * scale / (t := 1e-09)
     CLEAN   T = {"a": 1e-09}; assert r < T["a"]      and tuple unpacking
     CLEAN   np.isclose(a, b, 1e-09)  (third POSITIONAL; only the second
                                       positional of approx is read)
     CLEAN   assert round(a - b, 9) == 0              (a tolerance as an integer)
     CAUGHT  .05, 1_000.5, a generator expression, an if ... raise AssertionError
             that never writes the word assert, a conditional expression, the right
             half of a chain, assert_allclose(rtol=), approx(abs=), and a marker
             parked on a neighbouring statement.
judge 9 of 20. This is detection reach, which BU0 names as 4a and where R237
      already routed it, so I am consistent and I do not block on it. I record it
      here rather than only in the corpus because two of the eleven are not reach
      at the margin: they are the sentence the guard exists to enforce.
judge AND THE COVERAGE CLAIM IS STILL THE AUTHOR OWN LIST. Fifteen planted shapes
      catch fifteen shapes their author thought of; 46 corpus entries before this
      round and 66 after is the number that measures anything.
```

**Closed when** 4a rules on the candidate set. The 20 shapes are at
`tests/corpus/tolerance_marker_exemptions.txt` with `measured` taken at `37799aa`.

**R250. (recordable, 4a) `tests/test_ci_runs_the_whole_suite.py` is not vacuous in the way
its first version was; its reference set is still unasserted.** `:91`.

```
cell I checked the fix rather than reading the note about it:
     a passing test dropped into tests/verification/rung5 -- a directory the guards
     job ignores and ladder 5 declares empty: --
     -> FAILED test_every_test_in_the_suite_is_run_by_some_ci_job,
        assert not ["tests/verification/rung5/test_uncovered.py::test_x"].
     The gate carries its own failure. The --ignore flags are replayed, the
     full:-only rule is right, and every mis-parse I could construct SHRINKS the
     covered set, which is the strict direction.
judge ONE HOLE REMAINS AND I COULD NOT EXHIBIT IT, WHICH I RECORD AS THAT AND NOT
      AS A FINDING. everything = _collected(["tests"]) ignores the subprocess
      return code, so if the reference collection ever returned empty, missing
      would be empty and the assertion would pass on nothing. I tried two states to
      empty it -- a module raising at import, and a conftest raising -- and the
      first still collects 1656 while the second kills the outer run too. So:
      reasoned, not measured. One line, assert everything, closes it for free.
judge AND THE DOCSTRING IS HONEST ABOUT THE REST: it does not check that the jobs
      RUN. That matters here, because ladders 5 and 6 are skipped on every run this
      branch has produced, so the union-covers-the-suite property is true while
      tests/regression has never executed. That is R230, not this file.
```

**Closed when** 4a rules on it.

**R251. (recordable, 4a) `docs/reports/F2/step-6-draft.md` is read as a step-6 report.**
`tests/test_report_carried.py:69-74`. Measured at 37799aa: the guard fails with "step 6
has a report and no verdict yet". A draft is not a step. Corpus entry
`draft_suffix_beside_a_step_report`.

**R252. (recordable, 4a) `regen_figures.py --check` says the file is stale without saying
which row moved.** `scripts/regen_figures.py:327-332`. On CI this produced a bare
`AssertionError:` and the four moved rows had to be reconstructed from two unrelated
diagnostic prints. A unified diff of the two renderings costs three lines.

## Tolerances touched

**None by this diff. One is refuted by measurement.**

```
cmd  git diff 8e7418f..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 8e7418f..HEAD -- floatfea
out  (empty) -- floatfea/ is UNTOUCHED across this entire range, as it has been for
     five consecutive rounds.
cmd  git diff 8e7418f..HEAD -- tests/regression/
out  (empty) -- no golden file moved.
```

**What IS a tolerance finding this round is R244**, and it is about a value nobody
changed. `EXEMPT_RESPONSE_DRIFT_ULP = 4.0` at `floatfea/tolerances.py:713` is an exactness
ceiling whose recorded measurements were taken on one machine, and the first CI run that
ever reached it measured `2.6e9` ULP. Form: ULP, dimensionless, counter `10.0` at `:720`
-- all correct. What does not hold is the record: the measurements the entry rests on do
not cover the machines the assertion runs on. **It must not be raised in a step commit**,
and the counter ordering at `tests/test_counters_are_injected.py:170` means it cannot be
raised far without breaking the registry, which is that guard doing its job.

**My own instructions (item 4b).**

```
cmd  git diff 8e7418f..HEAD -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" 8e7418f..HEAD with per-commit file lists
out  4a8d2a3  ci.yml, check_carried.py, regen_figures.py, run_rung.sh,
              test_ci_ladder_gating.py, test_ci_runs_the_whole_suite.py,
              test_marker_exemption_corpus.py, test_no_tolerance_literals.py,
              test_report_carried.py, test_report_guard_states.py
                                                     -- no docs/reviews/
     37799aa  docs/reports/F2/step-5.md, test_report_guard_states.py
                                                     -- no docs/reviews/
judge No commit touches both code and docs/reviews/. No commit touches .claude/ or
      docs/SUPERVISOR.md at all, so the STOP-class condition is not in play. CLEAN.
cmd  the report header, item 1b
out  "Answers: verdict 28 @ 8e7418f", and 8e7418f is the third step-5 verdict,
     which is the latest. CORRECT -- one comparison, and it passes.
```

**What held**, reproduced at my run rather than read: `1655 passed, 0 failed, 0 skipped`;
ruff, black and mypy clean; the guards job existing and reaching 359 tests; the negative
control on the coverage check; all four R238 residues fixed; `ci.yml:71-80` true against
the rule it describes; the flagging contract of the scanner now honest about `node.left`;
the six guard states green on this machine; and the two-digit ruling, which I accept and
have given a discriminator. **These did not**: the CI result (R240), the CI sentence
(R241), the status of R230 (R242), the carry guard in the checkout CI gives it (R243), an
exactness ceiling on a platform-dependent quantity (R244), four generated figures (R245),
"never raises" (R246), and the harness that certifies R234 (R247).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Eight items. R240 is first and most of this
list sits inside it: until the `guards` job is green or every failure in it is routed by
name, the machine CA2 exists for is telling you something, and nothing below can be
measured anywhere else.

1. **R240 -- the `guards` job at the reviewed commit.** Green, or every one of the 30
   failures routed by name with the run id and the count beside it. A job that runs and is
   red is not the closure of an item whose content was that a claim about CI had never
   been run.
2. **R243 -- the carry guard in a `--depth 1` clone.** Shown as a run in that state with a
   count, not asserted. The failing direction is safe and the fix is one return-code test;
   what must not happen is `fetch-depth: 0` being added while the return code stays
   unread, because the next unavailable object is then silent again.
3. **R247 -- the R234 harness.** `baseline` green wherever it runs, and the collection
   check asking pytest instead of grepping the log for the substring "error". **Do not
   close this by deleting the collection assertion** -- it is the only assertion in the
   file about the failure the file exists for.
4. **R241 and R242 -- two sentences, in the same commit as what they describe.** Section 8
   stating the guards job result at the commit the report is committed at, with the run id
   and the counts; and the Carried row plus section 0 saying R230 is carried, not closed.
5. **R246 -- "never raises", true or withdrawn.**
6. **R244 -- on the Q8 list by name**, with its site and the fact that its gate is masked
   behind a skipped ladder 6. **Not by raising `4.0`** in a step commit.
7. **R245 -- the reproducibility of the figure file.** Either it reproduces on the
   platforms CI runs, or the rows that do not say so, with the four affected rows
   regenerated or annotated in the same commit (BP0).
8. **R231, R230, R223, R224 -- unchanged and open by instruction**, site by site as listed
   in Carried. R230 now waits on R231 and on R244, since ladder 6 is where both land.

**Not gates on step 5, into the next report Carried section:** R248, R249, R250, R251,
R252, R225-R228, the R232 residue, the remaining half of R233, and everything already at
4a.

**Adversarial corpus (BE3): 38 new entries committed at `f354025`, across the three files,
all unseen by the implementer; every `measured` field taken at `37799aa` before the
`require` or `expect` beside it was written. One existing entry is RULED ON rather than
added to.**

**The coverage measurement, stated plainly: of my 38 new entries the shipped checks did
what the entry requires on 20.**

* `tests/corpus/report_guard_states.txt` -- **+11 entries (6 -> 17), 8 correct, 3 misses.**
  The three are `superscript_digit_step_number` (a collection error, R246),
  `shallow_clone_depth_1` (23 false accusations, R243) and
  `draft_suffix_beside_a_step_report`. Eight states that were untested last round now
  report by name, which is the repair working.
* `tests/corpus/ci_ladder_gating.txt` -- **+7 entries (22 -> 29), 3 correct, 4 misses** --
  xfail, no arguments, an undeclared argument, and the substring skip alarm (R248).
* `tests/corpus/tolerance_marker_exemptions.txt` -- **+20 entries (46 -> 66), 9 correct,
  11 misses.** A different region again: the R237 sentence is closed, so this round
  attacks the candidate set rather than the exemption window, and two of the eleven are
  the two clauses of `CLAUDE.md` Tolerances verbatim.
* **The corpus bites harder than last round: 33 additional failures at `f354025` against
  9 last time.** That is what BE3 asks for -- the implementer own harnesses reporting on
  data they have not seen.

**The ruling you asked for.** `two_digit_step_number`: **ACCEPTED**, and the `require`
field is changed in the corpus rather than overridden in test code. But not on the
argument. `green` is also exactly what a guard comparing step numbers as STRINGS would
print, because 10 sorts below 5 lexically and such a guard would silently check step 5
while reporting nothing; the two outcomes are indistinguishable on that state, which is
why it was written `named_fail`. So the property was measured instead: with a step-10
report and a step-10 verdict where the VERDICT carries `R999` and the report does not, the
guard at `37799aa` goes **red naming R999**, so `int()` is parsing ten. The ruling stands
because a cell says so, not because the reasoning was good, and the discriminator is
committed as `two_digit_step_number_discriminating`.

**Twenty-nine consecutive rounds have found no element defect, and this round does not
either.** `git diff 8e7418f..HEAD -- floatfea` is empty. What changed this round is where
the review is standing: for the first time in this milestone the guards ran on a machine
neither of us controls, and four of them came back broken, one exactness ceiling came back
unreproducible, and one generated figure file came back machine-specific. **Not one of
those six was visible to a green local suite, and five of the six had been green here for
rounds.** That is the argument for CA2, measured rather than asserted, and it is the best
thing in this range -- which is exactly why the honest verdict is HOLD and not a PASS with
a caveat. The step did the right work, and the right work found the problems.
