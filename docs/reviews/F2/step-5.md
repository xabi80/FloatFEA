# Review — F2 step 5
Reviewed commit: 0dcdc2055ac52ed58db64760f21d456a2267c713
Verdict: HOLD

**Reviewed commit: `e3a3bd1`** (the verdict is stamped at my corpus commit `0dcdc20`,
which touches `tests/corpus/` only).

Tests: **1 failed, 1833 passed, 0 skipped** (my run at `e3a3bd1`, `python -m pytest -q`,
339.98 s, Python 3.13.11 on Windows). The failure is
`tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]`,
and it is the same one CI reports. **Every subset figure the report publishes reproduces
exactly** -- `test_figure_local_check` 17, `test_ci_ladder_gating` 56, `test_ci_determinism_gate`
13, `test_report_vocabulary_corpus` 32, the vocabulary corpus 31 entries, and rung 6 at
`ci.yml` 433 and 449. **None of the seven contains the red file**, and the report publishes
no whole-suite count.

**Plan: `897c3a4`, `1443fe9`, `095c6e1`, all standalone and re-locked. Process: `979933f`,
standalone. Code: `d713be4`, `1dc4d33`. Canonical file: `0def0dc`. Report: `e3a3bd1`
(revision 9).**

**Item 1b.** The newest revision's header (line 2404) reads `Answers: verdict 34 @ e6054b5`
and `e6054b5` is `review: F2 step 5 -- thirty-fourth verdict`, the latest. **Passes.**

**CI, item 3b, at the reviewed commit. RED.**

```
cmd  gh run list --commit e3a3bd1
out  []          <- the abbreviation matches nothing; the full sha is required,
                    which the implementer's own ci_section.py docstring says
cmd  gh run list --commit e3a3bd1d97e1e3bb1219ca24e2e95069a8b7ca37
out  34486215228 (push) failure   34486220416 (pull_request) failure
cmd  gh run view 34486215228 --json jobs
out  lint / unit / ladder 1,2,3          success
     CI determinism -- leg (1..10)       SUCCESS x10
     CI determinism -- ten legs agree    SUCCESS
     ladder 6 -- it stays fixed          SUCCESS   <- FIRST TIME ON THIS STEP
     guards and meta-tests               FAILURE
     ladder 4                            failure   (13, routed under Q8)
     ladder 5                            skipped
cmd  gh run view 34486215228 --log-failed
out  FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state
       [answers_header_names_an_older_verdict_commit]
     1 failed, 531 passed
     run_rung: 85 collected, 13 failed, 0 errored, 0 skipped     (ladder 4)
judge THE GUARDS JOB WENT FROM ONE FAILURE TO ONE FAILURE AND IT IS A DIFFERENT
      ONE. R293's open half is closed -- the figures test passes on the
      canonical machine. What is red is a declaration this round added, at the
      commit that added it. R309.
```

`git diff e6054b5..e3a3bd1 -- floatfea` is **not** empty for the first time in ten rounds:
it is `floatfea/tolerances.py` and nothing else. No element source moved.

**PR #1 is open, `F2 -> master`, `gh pr view 1 --json comments` returns 0 comments.** Step 5
still has no outside-witness comment. Recorded as an unavailable check, not as a pass.

**My own instructions (item 4b), and the new item 4c.**

```
cmd  git diff e6054b5..e3a3bd1 -- .claude docs/SUPERVISOR.md
out  979933f only: item 4c added to BOTH files, +12 and +13 lines, ADDITIVE.
     Standalone `process:` commit, citing CH2 and R302, touching nothing else.
     No guard removed -- I read both hunks line by line.
judge CLEAN, and the mechanism worked exactly as CLAUDE.md describes it.
cmd  git diff e6054b5..e3a3bd1 -- the conftest pathspec of my new item 4c
out  (empty)
cmd  git ls-files -- the same pathspec
out  (empty -- ZERO FILES)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py
judge THE PATHSPEC I WAS GIVEN MATCHES NO FILE IN THIS REPOSITORY. R310.
```

## Carried

Verdict 34 listed five blocking items plus two at 4a. **All seven are answered at their own
sites. Five close outright, two close and are replaced by a new claim in the same place.**

- **R293 -- CLOSED, and it is the largest thing in this step's history.** I checked it
  outside CI rather than reading the report.

```
cmd  gh run download 34482015314 -n determinism-leg-1 ; sha256sum F2_figures.md
out  40b8828fb3f57b64... == the leg's own figures.sha256
cmd  cmp <the downloaded artifact> docs/milestones/F2_figures.md
out  IDENTICAL, byte for byte
cmd  gh run view 34486215228 --log | grep -c "COMMITTED-MATCHES-CI yes"
out  10
cmd  the same log, the verdict job
out  ten of ten identical: 40b8828fb3f5 core Haswell
     10 x "4 collected, 0 failed"    (the regression rung, on every leg)
judge THE COMMITTED FILE IS THE CI ARTIFACT, HASH-VERIFIED, AND TEN LEGS AGREE
      WITH IT. The corpus entry
      `determinism_all_ten_legs_render_bytes_equal_to_the_committed_file` was
      NEVER OBSERVED at any commit on this branch for four rounds. It is
      observed. The stamp is inside the file, five rows, and it names the
      kernel.
```

- **R303 -- CLOSED at all three clauses, and I reproduced both columns of the table.**

```
cmd  python scripts/localise_clean_worst.py                       (this laptop)
out  curvature_xz 1.38250081892969870e-15 <- wins ; ratio 0.2765x
cmd  gh run download 34482015314 -n determinism-leg-1 ; cat clean_worst.txt
out  curvature_xz 1.28195530482572000e-15 <- wins ; ratio 0.2564x
judge SIX ROWS, BOTH MACHINES, EVERY DIGIT AS PUBLISHED. The same state wins on
      both; there is no argmax anywhere in this figure that moved; the largest
      per-state disagreement is 1.643x on `curvature`, which never surfaces
      because it never wins; one state agrees to sixteen digits.
judge AND THE CAUSE IS NOT CLAIMED. Four variables move between the two renders
      and the report names none of them as the cause. That is BG0 applied
      against the reporter's own interest, and it is the first time.
judge THE TOLERANCE IS SIZED ABOVE THIS ROW. 1.078x here, 1.336x at
      `rigid_body_mode_ratio`, bound 1.5. My condition said "sized against this
      row rather than against the 0.4% ones" and it is sized against a larger
      one still.
```

- **R304 -- CLOSED, and the shape of the repair is right.** The two gate bodies are
  **lifted out of the workflow at import time**, not copied into the test.

```
cmd  python -m pytest tests/test_ci_determinism_gate.py -q
out  13 passed
code _body() reads the heredoc out of .github/workflows/ci.yml -- "a copy would
     pass for ever while the workflow drifted"
cell (4 cases, 3 failing) -> must_fail True ; (4, 0) -> must_fail False, control
cell a leg lying about its own hash, and a leg with no artifact -> both refused
cmd  gh run view 34486215228 --json jobs | ladder 6
out  SUCCESS
judge FIVE LEG CASES AND SIX VERDICT CASES, CONTROLS IN BOTH DIRECTIONS. The
      goldens are gated on the machine that produces them, ladder 6 is off the
      chain with a reason I accept, and the shipped test asserts both halves --
      not rung4, not rung5, and not nothing.
```

- **R305 -- CLOSED ON FOUR OF FIVE. One re-taken figure is still wrong, and half of that
  is mine.**

```
cmd  python -m pytest tests/test_report_vocabulary_corpus.py -q ; count the corpus
out  32 passed ; 31            -> "31 of 31 agree"                  CORRECT
cmd  grep -n rung6 .github/workflows/ci.yml
out  433: and 449:             -> the report says 433 and 449       CORRECT
cmd  the ten-leg table, now generated by ci_section.py --legs from the run it
     cites                     -> 10 legs, 6 CPU models, 1 hash     CORRECT
code the module-level print row: withdrawn, with the reason         CORRECT
cmd  the delta row: "9 of 47"
out  THE FILE HAS 38 ROWS BEFORE AND 44 AFTER. 47 IS A LINE COUNT. R311(b).
judge FOUR OF FIVE RE-TAKEN AND TWO OF THEM NOW GENERATED, WHICH IS THE POINT
      OF THE ITEM. The fifth is a denominator that came out of my own verdict,
      where I wrote "9 of 47 differ, 38 identical" about LINES and the report
      read it as rows -- so I name it as a finding and name my share.
```

- **R306 -- CLOSED at the condition, and the sentence that replaced it is the finding.**
  The condition was "section 4's claim states the measured reach ... or the check is
  strengthened". Section 6 states it: *one row in eight*, with the counterfactual. **That
  is met.** What is added beside it is not. R311(a).

- **R307 -- CLOSED.** The verdict job opens `F2_figures.md`, hashes it, and compares against
  the leg's own claim; a lying leg and a leg with no artifact are both refused in a run I
  made. Provenance, not existence.

- **R308 -- CLOSED.** `tests/test_ci_canonical_environment.py` is `4 passed` and the third
  test asserts membership before subscripting.

- **R302 -- CLOSED, and it is the honest answer of the two I offered.** Both sentences are
  withdrawn by name and replaced with the property: everything the gate reads is writable
  from a rung's own `conftest.py`, no gate in this position changes that, and the bound is
  review. The four channels are built as layouts and **declared with their direction**, so
  the day one starts reddening the file says the declaration is stale rather than agreeing
  with it. I ran the file: `56 passed`, all 53 corpus entries have a layout.

  **The bound named is a pathspec that matches no file. R310.**

- **R231, R244, R245, R275 -- OPEN, and now UNBLOCKED for the first time.** The report says
  so and declines to write them in the commit that lands the render they would be measured
  from. **That is the correct reading of CLAUDE.md and I endorse it.** They are the next
  round's.

- **R230, R223, R224, R261 -- OPEN by instruction, correctly listed.** No Q8 value written.

- **R300, R291, R292 -- OPEN, recordable at 4a, correctly recorded.**

- **R281 -- OPEN.** Of the eleven corpus files, six now have a runner that names my new
  entries. `ci_determinism.txt` and `carried_row_subject.txt` still have none, and both
  carry six and four new entries this round that nothing will read.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues, R249-R252,
  R225-R228, R232, R233, R288, R289, R290** -- carried, and correctly present in the
  generated table.

## Findings

**R309. (BLOCKS -- CA2, and the truth of the report's own account) The suite is red at the
reviewed commit, on a declaration this round wrote in the commit that publishes it, and no
figure in the report would show it.** `tests/test_report_guard_states.py:108-121`;
`docs/reports/F2/step-5.md`, section 11.

```
cmd  python -m pytest -q                                        (my run, e3a3bd1)
out  1 failed, 1833 passed, 2 warnings in 339.98s
     FAILED test_the_guard_survives_the_state[answers_header_names_an_older...]
cmd  gh run view 34486215228 --log-failed                       (CI, same commit)
out  1 failed, 531 passed -- THE SAME TEST. Two machines, one failure.
code the failure text: "the repaired guard is expected to be GREEN here and it
     failed" -> "the report at e3a3bd1 is newer than the verdict at e6054b5 and
     names d713be4"
code S11: "One declared disagreement with a corpus ... It is declared green in
     tests/test_report_guard_states.py with the reason"
judge THE DECLARATION WAS TRUE WHEN IT WAS MEASURED AND FALSE WHEN IT SHIPPED.
      While `docs/reports/F2/step-5.md` was still at 55498f4 it was older than
      the verdict, the guard returned early, and the state was green. The
      commit that ADDED the declaration is the commit that re-committed the
      report -- so the report became newer than the verdict in the same breath,
      the guard fired, and the declaration was stale before it was pushed. This
      is BP0 in its purest form, and the declared-direction machinery this
      round built is what caught it.
judge AND THE REPORT'S OWN EVIDENCE CANNOT SEE IT. Revision 9 publishes seven
      subset counts and every one is correct. `tests/test_report_guard_states.py`
      is in none of them, and no whole-suite figure is published, which
      CLAUDE.md's step-gating list requires ("the test counts from your own
      run"). Assertion domain blindness, applied to a report rather than to a
      test: the collection the evidence inspects cannot contain the failure.
cmd  tests/corpus/report_guard_states.txt, the CONTROL entry added at 0dcdc20
```

**Closed when** the suite is green at the report's own commit -- either the declaration is
corrected to the direction measured there, or the state is made green -- **and** the report
publishes a whole-suite count from its own run. If the honest answer is that the state
genuinely must redden and the corpus is right, say that and let the entry go back to
`require=fail`.

**R310. (BLOCKS -- the bound is the whole of R302's answer, and it inspects nothing) The
conftest pathspec matches zero files in this repository. The one conftest that exists,
`tests/conftest.py`, is outside it -- and that file already implements
`pytest_collection_modifyitems`, which is R302's third channel, for every rung at once.**
`docs/SUPERVISOR.md` item 4c; `.claude/agents/gating-supervisor.md` item 4c;
`scripts/run_rung.sh:172-176`.

```
cmd  git ls-files -- the pathspec as written in both instruction files
out  (nothing)
cmd  git ls-files with the same pattern under :(glob) magic ; git ls-files "*conftest.py"
out  tests/conftest.py                                  ;   tests/conftest.py
judge GIT'S DEFAULT PATHSPEC GLOB WILL NOT LET A DOUBLE STAR STAND FOR ZERO
      DIRECTORIES. The instruction reads as "every conftest under tests/" and
      means "every conftest at depth two or more under tests/". The repository
      has exactly one conftest and it is at depth one.
code tests/conftest.py:  def pytest_collection_modifyitems(items): ...
                         items.sort(key=...)
judge THAT IS THE HOOK. It sorts today. Replacing the sort with a filter is the
      same line with a different body, it applies to EVERY rung rather than to
      one, and the diff command that is supposed to surface it prints nothing.
cell two rung trees, the shipped script, the project's pyproject.toml, one
     conftest each, nothing else:
out  conftest at tests/conftest.py, dropping the failing item
       -> run_rung: 1 collected, 0 failed ; run_rung: OK          EXIT 0
     conftest at tests/verification/conftest.py, the same body
       -> run_rung: 1 collected, 0 failed ; run_rung: OK          EXIT 0
     no conftest, same two tests                      CONTROL
       -> run_rung: 2 collected, 1 failed ; FAIL                  EXIT 1
judge SO THE CHANNEL IS NOT A PROPERTY OF THE RUNG DIRECTORY. It is a property
      of every conftest on the collection path, and all four declarations in
      `REQUIREMENT_CHANGED` name the rung's own directory.
judge WHAT I AM NOT SAYING. The analysis behind R302's answer is right and the
      answer is the one I would have chosen. A gate cannot outrank code that
      writes the record it reads, and review IS the bound. This is that bound
      written as a command that returns the empty set -- "an empty parameter
      set is an error, not a skip", landed in my own instructions.
cmd  tests/corpus/ci_ladder_gating.txt, the 4 entries added at 0dcdc20
```

**Closed when** the pathspec in both instruction files names the files it means -- shown as
a run of `git ls-files` over it printing `tests/conftest.py` -- and `scripts/run_rung.sh:172-176`
quotes whatever it becomes. A standalone `process:` commit, per CLAUDE.md; and since it is
my instruction, I will take the correction as written and diff it under 4b next round.

**R311. (BLOCKS -- head 3) Five published sentences and figures do not describe the
repository. Each is refuted by one command, and every one of them sits beside a repair that
works.** `scripts/carried_table.py:36-40`; `floatfea/tolerances.py:1033`;
`docs/milestones/F2.md:1129`; `scripts/regen_figures.py:344`; `scripts/run_rung.sh:181-183`;
`docs/reports/F2/step-5.md`, sections 0, 2, 5 and 6.

```
(a) code carried_table.py:38 and S6: "a rotation is not detected -- it is
        impossible to write" / "ROTATION IS NOT DETECTED, IT IS UNWRITABLE"
    cell the `state` and `where` fields of R302, R303 and R304 rotated among
        themselves, each row's `site` LEFT CORRECT:
    out THE GENERATOR PRINTS ALL FIFTY-NINE ROWS.
        | R302 | answered - S4 | The gate reads pytest's record ... |
        | R303 | answered - S3 | One of the nine differing rows ... |
        | R304 | answered - S1 | The goldens now execute on ten CI legs ... |
    judge THE SUBJECT IS UNROTATABLE AND THE STATUS IS NOT. What CH4 removed is
        the prose; what is left to rotate is a state and a section number, and
        `check_sites` passes because every site is still its own. The true
        sentence is one word shorter: the SUBJECT cannot be attached to the
        wrong number. Two further shapes print as well -- a pointer at `S99`,
        which no section is, and `state: withdrawn` on a blocking finding.
    judge AND THE CONTROLS ARE REAL: `state: closed` and a sixty-character
        `where` are both refused by name, in runs I made. This is a good
        repair with one word too many on it.

(b) code tolerances.py:1033 "over the nine rows of forty-seven that move at
        all"; F2.md:1129 and regen_figures.py:344 "Nine rows of forty-seven"
    cmd the two renders, rows parsed with the script's own row pattern
    out 38 rows before, 44 after, 38 in common, 9 of the 38 differ. `47` is the
        old FILE's line count, including the title and the prose. My own
        verdict wrote "9 of 47 differ, 38 identical" about lines, and this is
        where it went.
    judge THE 9 IS RIGHT AND THE DENOMINATOR IS A DIFFERENT QUANTITY. It is in
        `tolerances.py` as the stated basis of a new constant, which is why it
        is here rather than filed as tidiness.

(c) code F2.md Q8 clause 3: "the local value is within FIGURE_FLOOR_CLASS_SPREAD
        of the committed canonical one, and the spread is PRINTED BESIDE THE
        VALUE either way"; S2: "with the spread printed beside all nine"
    cmd python scripts/regen_figures.py --check                (this laptop)
    out spreads printed beside EIGHT rows. `counter_defect_boundary` gets none:
        the `words` branch continues before any number is read.
    cell the committed row 2.183e-06/2.188e-06 against a local render reading
        "1e-99 passes, 1e+99 fails"
    out EXIT 0. Nine orders of magnitude, no spread, no complaint.
    judge THE CODE'S OWN COMMENT DECLARES THIS ("words: the decision is the
        pass/fail words, not the numbers") AND THE PLAN CONTRADICTS IT. One of
        the two is wrong and the plan is the locked one. Nor is "all nine" the
        set: the ninth mover is `detection_edge_at`, which is not floor-class.

(d) code 1dc4d33 subject "a red rung says which test failed";
        run_rung.sh:182 "what was lost was everything that says WHICH test
        failed"
    cmd gh run view 34486215228 --log | ladder 4              (the reviewed run)
    out run_rung: 85 collected, 13 failed, 0 errored, 0 skipped
        run_rung: FAIL -- tests/verification/rung4 is red.
    judge THIRTEEN FAILURES AND NOT ONE NAME. The repair restored the COUNT and
        the REASON, which is real and is what the shipped test asserts. It did
        not restore a name, and the junit report it already parses carries
        them.

(e) code S0, the second table: guards and meta-tests | 4056 | 123 | 0
    cmd gh run view 34483519085 --log-failed | the guards job summary
    out 9 failed, 604 passed in 364.03s
    judge `ci_section.py` sums EVERY pytest summary line in the log, and this
        job's failures echo dozens of nested subprocess summaries inside their
        assertion text. The row overstates the job by 13x. It errs loud rather
        than quiet, and it is still a published measurement of CI that CI
        refutes.
```

**Closed when** each of (a) to (e) is re-taken or withdrawn at the commit that publishes it.
(a) may instead be closed by refusing a rotation, (d) by printing the names the junit report
already holds, (e) by counting the job rather than the log -- but none of those is required;
the sentence matching the code is.

**R312. (recordable, 4a) `FLOOR_CLASS` membership is hand-granted and nothing measures
whether a member needs the licence.** `scripts/regen_figures.py:346-356`.
`rigid_body_counter_ratio` reads `3.0612e-11` on both machines -- byte-identical -- and is
in the class, so it may drift by up to `1.5x` on a non-canonical machine without a word.
Conversely `detection_edge_at`, one of the nine rows that DID move, is not in the class at
all, correctly, because it is a name. The class has nine members and the movers are nine,
and they are not the same nine. Nothing asserts the membership against the measured set,
which is the one thing this round has the data for.

**R313. (recordable, 4a) The decision-word comparator strips the letter `e` out of the
words.** `scripts/regen_figures.py:483-484`. The substitution over the character class
`[-+0-9.eE]` turns `passes` into `passs`, so `passes` and `passees` compare equal. The pair
that matters, `passes` against `fails`, survives it, and both sides get the same
transformation -- so this is latent rather than live. It is in the only comparator in the
file that decides on words.

**R314. (recordable, 4a) A `Carried` pointer is not resolved against the report it points
into.** `scripts/carried_table.py:154-166`. `where` is bounded at forty characters and the
state at five spellings, both of which I ran and both of which refuse. Nothing asks whether
`S99` is a section, or whether the section named discusses that item. That is the half of
(a) above that a machine could take.

## Tolerances touched

**Two constants added, both new, neither rescuing a failing test. I verified the basis of
both against the live corpus rather than reading the plan.**

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `FIGURE_FLOOR_CLASS_SPREAD` | `1.5` | dimensionless factor, max over min of two renders | `1.6` | `F2.md` Q8 third-class table; asserted from two files by `test_figure_local_check.py` |
| `FIGURE_ARGMIN_TIE_WINDOW` | `1.01` | dimensionless factor on an extremum | `1.0216` | `F2.md` Q8, and re-measured below |

```
cmd  git show 1443fe9 --stat
out  docs/milestones/F2.md, floatfea/tolerances.py -- STANDALONE, re-locked,
     ahead of every reader. A grep for either name at that commit finds
     tolerances.py and F2.md and nothing else.
judge THE ORDER IS THE ONE CLAUDE.md ASKS FOR and it has not been used on this
     branch before: the value is declared with its basis in a plan commit, and
     the code that reads it lands afterwards.
cell the tie window's basis, re-measured from the corpus rather than read:
out  3.627517e-14  1.000000  ci_plateau_D0p0689_roll1p017_aniso9p6e5
     3.642482e-14  1.004125  ch_edgemin_D0p0758_roll1p05_aniso9p4e5
     3.705745e-14  1.021565  ci_plateau_D0p0743_roll1p075_anisocap
judge 1.0041 < 1.01 < 1.0216, EXACTLY AS PUBLISHED, to the digits published.
     The counter IS the third entry's position, so it is a detection threshold
     and not one arbitrary perturbation. Bracketed on both sides by
     measurements. This is the best-founded tolerance pair in this file.
cell the spread bound's bracket, re-measured from the committed figures:
out  floor-class margins 83.4, 18.2, 30.6, 74.7, 3.90, 2.19 -> min 2.19
     largest measured spread 1.336 -> 1.336 < 1.5 < 2.19
judge AND BOTH INEQUALITIES ARE ASSERTED FROM FILES, not restated in the test.
     The shipped bracket test parses the plan's table and the committed
     figures; when either side moves the bracket closes and the build reddens.
     That is BI3's remedy applied properly.
cell the two counters, run:
out  a figure moved by 1.6x -> refused ; by 1.336x -> allowed ; by 3.0x ->
     refused. An entry at 1.0216x -> not named in the tie set.
judge THE COUNTERS ARE IN THE ASSERTION'S OWN QUANTITY. 1.6 fails through the
     spread branch, not through the margin branch -- I checked which one fires.
```

**The `CLASS:` label moved from `PLATFORM` to `ACCURACY` at `1dc4d33`, in the same commit
as a `scripts/run_rung.sh` change, and I am recording it rather than finding on it.** Rung 3
requires a class from `{ACCURACY, STRUCTURAL}`; `PLATFORM` is not in that vocabulary; the
`set -e` repair is what made the red visible. The choice taken was to conform the entry to
the gate rather than to widen the gate's vocabulary, which is the direction CLAUDE.md
requires, and the commit says so in as many words. **No value moved.** The hygiene note --
the commit that exposed a red and the change that answers it are one commit -- is worth
avoiding next time; both runs are pasted, so nothing is hidden.

**Two figures in `tolerances.py` comments were re-taken and one trend withdrawn (BP0),
correctly, in the commit whose file made them stale.** `62x -> 83x` on
`RIGID_BODY_MODE_RATIO`: `1e-12 / 1.1986e-14 = 83.4`, checked. The `2.37 -> 2.19 -> 2.18`
series: the second step is `1.0046x` and this figure's measured cross-machine spread is
`1.0046x`, so withdrawing it as a trend is what the measurement says. **The direction
argument survives and is stated as surviving.** The plan's `~62x` and `~19x` cells moved to
`~83x` and `~18x` in the standalone plan commit that follows -- `1e-13 / 5.5095e-15 = 18.15`,
checked.

**What held**, reproduced at my run rather than read: the committed figures file against the
CI artifact, downloaded, hashed and compared byte for byte; ten legs printing
`COMMITTED-MATCHES-CI yes` at the reviewed commit; both columns of the `clean_worst_ratio`
localisation, every digit; the tie window's three entries and the spread bound's two
brackets, re-measured from the corpus and from the committed file; the two gate bodies
lifted from the workflow and run against injected junit and injected legs, controls in both
directions; six of the report's subset figures; `--check` on this laptop, exit 0 with nine
floor rows listed; and no element source touched for a tenth round.

**These did not**: the suite and CI at the reviewed commit (R309), the reach of the bound
named for R302 (R310), and five published sentences (R311).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** This is the strongest round this step has had
-- all five blocking items and both 4a items answered at their own sites, the first
canonical file in the repository's history, and the first tolerance pair whose basis I could
re-measure end to end and find exact. It is still a HOLD, and two of the three reasons are
one line each.

1. **R309 -- the suite is red at the reviewed commit.** CA2 is not discretionary, and this
   is not a stale routing: it is a declaration written in the commit that falsifies it.
   Correct it in the direction measured there, and publish a whole-suite count so that the
   next one cannot hide between seven green subsets.
2. **R310 -- the bound named for R302 matches no file.** The conftest pathspec returns the
   empty set; `tests/conftest.py` is the only conftest and already runs the hook. A
   standalone `process:` commit, in both instruction files, and the quote in
   `run_rung.sh:172-176` with it.
3. **R311 -- five sentences.** (a) rotation, (b) the denominator in `tolerances.py`, (c) the
   spread that is not printed beside all nine, (d) the red rung that names no test, (e) the
   generated guards row.
4. **R231, R244, R245, R275 -- unblocked and correctly deferred.** The canonical render must
   stand one round on its own; a Q8 value written in the commit that lands the render it is
   measured from is the shape this file rejects. Next round, not this one.

**Not gates on step 5, into the next report's Carried section:** R312, R313, R314, R300,
R291, R292, R281, the underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 16 new entries at `0dcdc20`, across four files, all unseen by the
implementer; every `measured=` taken at `e3a3bd1` -- or against CI runs `34482015314` and
`34486215228` -- before the `require=` beside it was written.**

**The coverage measurement, stated plainly: of my 16 new entries the shipped checks do what
the entry requires on 5, and four of the five are controls I wrote to show the checks are not
vacuous.** All four behaved.

* `tests/corpus/ci_ladder_gating.txt` -- **+4 (53 -> 57), 1 correct**, the control. The two
  conftest-placement entries and the no-test-name entry get through. With the corpus applied
  the file gives **6 failed, 54 passed** and names all four new entries as having no layout,
  which is the runner working.
* `tests/corpus/ci_determinism.txt` -- **+6 (20 -> 26), 2 correct.** One is the
  COMMITTED-MATCHES-CI control and it is the best result this branch has produced. One is
  the declared licence of Q8's third class, recorded so the dependency on the canonical
  byte-comparison is on the page. **This file still has no runner.**
* `tests/corpus/carried_row_subject.txt` -- **+4 (13 -> 17), 1 correct**, the control. The
  three rotations print. **This file still has no runner.**
* `tests/corpus/report_guard_states.txt` -- **+2 (21 -> 23), 1 correct**, the control, which
  is the live failure. With the corpus applied the file gives **4 failed, 20 passed**.

**I am deliberately not adding to `g22_model_configurations.txt` or `g21_rigid_body_frames.txt`
this round, and saying so rather than leaving a gap.** A corpus entry there changes
`corpus_entries` and can change `detection_edge_at`, which makes the canonical render stale
the moment it is committed -- and the canonical render can now only be produced on CI. The
byte-identity claim has stood exactly one run. It gets one clean round to stand on its own;
the next verdict adds to both files and the re-render is part of the answer.

**Thirty-five consecutive rounds have found no element defect, and this round does not
either.** `git diff e6054b5..e3a3bd1 -- floatfea` is `tolerances.py` and nothing else.

**What is different about this round.** The thing this step has been for since revision 1 is
now true and checkable by a stranger: `docs/milestones/F2_figures.md` is the byte-for-byte
artifact of a CI run, stamped with the environment that produced it, agreed on by ten runners
across six CPU models and two vendors, and re-asserted by the next run. I downloaded it and
compared it myself. And the round's own repair caught the round's own stale declaration,
which is the first time a mechanism built here has fired on its author within one commit.
Everything blocking above is a sentence or a pathspec.
