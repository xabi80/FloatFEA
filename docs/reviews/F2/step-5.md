# Review — F2 step 5
Reviewed commit: aaaece2f0bbac7ce54ca8b21785467ac399c790a
Verdict: HOLD

**Reviewed commit: `bf00121`** (the verdict is stamped at my corpus commit `aaaece2`,
which touches `tests/corpus/` only).

Tests: **1889 passed, 0 failed, 0 skipped** (my run at `bf00121`, `python -m pytest -q`,
403.65 s, Python 3.13.11 on Windows). **The whole-suite line the report publishes
reproduces exactly on my machine, at the report's own commit** -- which is the first time
this step has had a whole-suite figure at all, and it is right.

**Commits: process `09b7db0` (standalone). Code `3f648e0`, `7440b81`, `7254dfc`. Plan
`3dd94b8` (standalone, re-locked). Report `bf00121` (revision 10).** `git diff
9cc7744..bf00121 -- floatfea` is `tolerances.py` and nothing else, for an eleventh round.
No value moved; one comment changed, and that comment is R316 below.

**Item 1b.** The newest revision's header (line 2945) reads `Answers: verdict 35 @ 9cc7744`
and `9cc7744` is `review: F2 step 5 -- thirty-fifth verdict`, the latest. **Passes.**

**CI, item 3b, at the reviewed commit. RED, and better than it has ever been.**

```
cmd  gh run list --commit bf00121cc295bb020e4b88710ed2e458f573c7ab
out  34523398136 (pull_request) failure   34523395377 (push) failure
cmd  gh run view 34523398136 --json jobs
out  lint / unit / ladder 1,2,3               success
     CI determinism -- leg (1..10)            success x10
     CI determinism -- ten legs agree         success
     ladder 6 -- it stays fixed               success
     guards and meta-tests                    SUCCESS   <- FIRST TIME ON THIS STEP
     ladder 4 -- the loads are the loads       failure  (13, routed under Q8)
     ladder 5 -- independent confirmation      skipped
cmd  the same run's log, the guards job
out  587 passed in 321.70s
cmd  the same run's log, ladder 4
out  run_rung: 85 collected, 13 failed, 0 errored, 0 skipped
     run_rung:   failure  tests.verification.rung4.test_writer_round_trip::
                 test_every_kinematic_channel_round_trips_BIT_EXACT[position-xi-0-bodyA-0]
     ... THIRTEEN NAMES, one per failure, plus test_joint_multipliers_round_trip_bit_exact
judge R309 IS CLOSED ON THE MACHINE THAT MATTERS: the guards job is green at
      the reviewed commit and my whole-suite run agrees with the report's line.
      R311(d) IS VISIBLE IN CI: last round ladder 4 printed thirteen failures
      and named none; this round it names all thirteen. What is left red is the
      Q8 rung, which is not this step's work and is not a new red.
```

**One red ladder rung means no PASS is available this round** whatever else is true
(CA2, and CLAUDE.md section Testing). It is **not** a STOP: Q8 is locked, it names these
thirteen `sin`/`cos` round-trips as the thing that forced it, and it routes the repair
through the canonical render rather than through this step. That is the reading every
verdict on this step has taken and I take it again -- deliberately, and not by inertia.

**PR #1 is open, `F2 -> master`, `gh pr view 1 --json comments` returns 0 comments.**
No outside-witness comment on step 5. Recorded as an unavailable check, not as a pass.

**My own instructions (item 4b) and the corrected item 4c.**

```
cmd  git diff 9cc7744..bf00121 -- .claude docs/SUPERVISOR.md
out  09b7db0 ONLY. Standalone `process:` commit citing CI0 and R310, touching
     nothing else. +22 / +30 lines, and I read both hunks line by line.
judge THE ROUTE IS CORRECT AND ONE SENTENCE IN IT IS NOT. Everything added is
     additive except one deliberate rewrite: "Review is the bound" became
     "Review is the LAST bound rather than the whole of it", justified by a
     claim about the new cross-check. That claim is refuted below (R315), so
     the guard was weakened on a measurement that does not hold. The route is
     right, the content is not, and it goes back the same way.
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py                          <- R310's condition, met
cmd  git diff 9cc7744..bf00121 -- tests/conftest.py 'tests/**/conftest.py'
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py                          <- and it is the whole set
```

## Carried

Verdict 35 listed three blocking items and three at 4a. **All six are answered at their own
sites. Five close. One does not, and two new claims arrive beside the ones that closed.**

- **R309 -- CLOSED, at both halves of its condition, and I checked both myself rather than
  reading them.**

```
cmd  python -m pytest -q                                     (my run, bf00121)
out  1889 passed, 2 warnings in 403.65s          NO FAILURES, NO SKIPS
cmd  the report's own line, section 7
out  "Whole suite at `7254dfc`: 1889 passed, 0 failed, 0 skipped"
judge THE NUMBER IS TRUE OF THE TREE THE REPORT IS COMMITTED FROM. 1889 at the
      parent and 1889 at the report commit; the only thing between them is the
      report file itself.
cmd  gh run view 34523398136 -- the guards job
out  SUCCESS, 587 passed. The state that went stale is committed by the
      harness now, so it no longer measures which of two files git saw last.
judge AND THE ORDERING RULE IS HONEST ABOUT ITSELF: "RUN IT LAST" is in
      `scripts/suite_count.py`'s docstring, stated as an ordering nothing can
      enforce from inside. The reach of the guard around the line is R319.
```

- **R310 -- CLOSED at every clause of the condition.** Both paths in both instruction
  files, in a standalone `process:` commit; `scripts/run_rung.sh:180-187` quotes what it
  became; `git ls-files` over it prints `tests/conftest.py`; and
  `tests/test_supervisor_conftest_pathspec.py` runs the instruction's own command.

```
cell the pathspec reverted to the double star alone, in a clone
out  FAILED test_the_instruction_pathspec_names_every_conftest[SUPERVISOR.md]
     "does not match ['tests/conftest.py']"       -- it reddens
cell a conftest tracked outside the pathspec (`floatfea/conftest.py`)
out  the same test names it                       -- the claim in SUPERVISOR.md
     that it "reddens when one appears outside it" is true
judge A NEGATIVE CONTROL FOR AN INSTRUCTION, WHICH IS NEW HERE AND RIGHT. The
     one clause I do not accept is the sentence written beside it: R315.
```

- **R311 -- CLOSED ON FOUR OF FIVE. (b) is not closed, and half of that is mine again.**

```
(a) cell the `state` and `where` of R309, R310 and R311 rotated among
        themselves, the table regenerated with the committed script, in a clone
    out FAILED ...points_at_a_section_that_discusses_it[R309->1], [R310->3],
        [R311->2] -- three rotations, three named failures, 3 failed 162 passed
    judge REFUSED BY A MACHINE, WHICH IS THE STRONGER OF THE TWO CLOSURES I
        OFFERED. The reach is R318.
(b) NOT CLOSED -- R316.
(c) cmd python scripts/regen_figures.py --check                 (this laptop)
    out nine floor-class rows, NINE spreads, counter_defect_boundary
        "2.183e-06 passes, 2.188e-06 fails" against the local pair, 1.0041x
    judge THE ROW THAT PRINTED NOTHING NOW PRINTS ITS SPREAD, and the plan's
        clause 3 is true of the code again.
(d) cmd sh scripts/run_rung.sh full:... over a rung with one good and one bad
    out run_rung: 2 collected, 1 failed, 0 errored, 0 skipped
        run_rung:   failure  tests.verification.rung1.test_a::test_bad
    cmd gh run view 34523398136 -- ladder 4                     (CI, this commit)
    out thirteen `run_rung:   failure` lines, one per failing case, NAMED
    judge CLOSED IN THE PLACE THE FINDING WAS MEASURED.
(e) cmd python scripts/ci_section.py e3a3bd1                    (my run)
    out identical to the report's section 0, line for line, "guards and
        meta-tests | 531 | 1 | 0"
    judge THE GENERATOR AND THE PUBLISHED TABLE AGREE, and the row is the job's
        own summary rather than the sum of its log. The 4056 is gone.
```

- **R312 -- CLOSED, and the shape is better than the item asked for.** Membership is
  marked at the `rows.append` that builds each row and read back through `floor_class()`;
  a figure added without a mark is exact-compared, which is the safe direction. `20 passed`
  in `tests/test_figure_local_check.py`, my run.

- **R313 -- CLOSED.** A whole-word `findall` replaces the substitution over the character
  class that ate the letter `e`; `passees` no longer equals `passes`, and the pair that
  matters is unaffected. Read line by line and exercised through the `--check` run above.

- **R314 -- CLOSED**, by the same machine as R311(a), with the reach recorded as R318.

- **R302, R303, R304, R305, R306, R307, R308, R293 -- closed in verdict 35**, correctly
  carried and not reopened. R302's analysis stands; the sentence built on top of it is
  R315.

- **R231, R244, R245, R275 -- OPEN, and now due.** The canonical render has stood one clean
  round on its own, which is exactly what I said it needed. Next round these are the work,
  and my corpus goes back into `g22_model_configurations.txt` and
  `g21_rigid_body_frames.txt` with the re-render as part of the answer.

- **R230, R223, R224, R261 -- OPEN by instruction, correctly listed.** No Q8 value written.

- **R300, R291, R292 -- OPEN, recordable at 4a, correctly recorded.**

- **R281 -- OPEN, and one file longer.** `ci_determinism.txt` and `carried_row_subject.txt`
  still have no runner. My new `report_numbers_sourced.txt` has none either, and I say so
  rather than leaving it to be found.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues, R249-R252,
  R225-R228, R232, R233, R288, R289, R290** -- carried, and correctly present in the
  generated table.

## Findings

**R315. (BLOCKS -- the reach of the ladder's gate, and one sentence in four files, one of
them mine) One conftest hookwrapper, in one file, still reaches `run_rung: OK` and exit 0
on a rung whose test fails -- and both records agree, because the attacker sits INSIDE the
hook the second record is taken from.** `docs/SUPERVISOR.md` item 4c;
`.claude/agents/gating-supervisor.md` item 4c; `scripts/run_rung.sh:172-178`;
`scripts/rung_no_xpass.py:98-113`; `docs/reports/F2/step-5.md` section 1 and section 10.

```
code SUPERVISOR.md: "a single hook that rewrites one of them reddens the rung
     ... what that buys is that forgery must be consistent across two places
     rather than done in one"
code run_rung.sh:176: "A conftest that drops a failing item now has to defeat
     both records consistently instead of one."
code S1: "TWO OF FOUR ... THE OTHER TWO CANNOT BE CAUGHT FROM INSIDE THE
     SESSION"
cell the shipped script, a scratch rung holding test_ok and test_bad, the
     project's own pyproject.toml, ONE conftest, at BOTH depths:
out  makereport wrapper flipping the report        exit 1  CAUGHT  (as claimed)
     sessionfinish rewriting the XML               exit 1  CAUGHT  (as claimed)
     collection_modifyitems dropping the item      exit 0  missed  (as claimed)
     no conftest, two tests, one failing           exit 1  CONTROL
     runtest_call wrapper, force_result, trylast   exit 0  MISSED  <- NEW
       run_rung: 2 collected, 0 failed, 0 errored, 0 skipped
       run_rung: OK -- 1 director(y|ies) ran
     the SAME body without `trylast=True`          exit 1  caught  CONTROL
       run_rung: FAIL -- the two records of this run disagree. junit says
       (2, 0, 0) and the plugin tallied (2, 1, 0)
judge ONE KEYWORD ARGUMENT IS THE WHOLE DIFFERENCE. `rung_no_xpass` takes its
     tally inside `pytest_runtest_call`; a hookwrapper on the same hook ordered
     INNERMOST runs inside that, so the exception is gone before the tally
     looks and both records are honest accounts of a passing test. Nothing had
     to be written twice, nothing had to be kept consistent, and the forgery is
     in one file at either depth.
judge THE HEDGE EXISTS AND IT IS IN THE WRONG REGISTER. `rung_no_xpass.py:100`
     says "a conftest that swallows it there has changed what the test DID
     rather than what was written about it". From the gate's side those are the
     same event: a red rung reporting `run_rung: OK`, which is the whole of
     what CH2 is about.
cell two further shapes, same harness, both depths:
out  pytest_runtest_protocol returning True for the failing item   exit 0
     pytest_deselected plus items[:] = keep                        exit 0
judge SO THE MEASURED SET IS SIX CHANNELS AND THE CROSS-CHECK CLOSES TWO. The
     report's "two of four" is true of the four it inherited and is not the
     reach of the mechanism.
cmd  tests/corpus/ci_ladder_gating.txt, the 4 entries added at aaaece2
```

**Closed when** the sentence in both instruction files, in `run_rung.sh`, in
`rung_no_xpass.py` and in the report says what was measured -- that the second record
raises the cost for a hook written OUTSIDE the tally and does nothing against one written
inside it, so **review remains the bound and not merely the last one** -- and the
`trylast` shape is in the layout map with its direction declared, like the other channels
that escape. The instruction files go back through a standalone `process:` commit, per
CLAUDE.md; the wording is the implementer's to propose and mine to check. Making the
channel actually redden would close it too and is not required.

**R316. (BLOCKS -- the stated basis of a tolerance, and R311(b) is not closed) The
denominator was corrected from a line count of a superseded render to a ROW count of the
same superseded render. At this commit the two renders share forty-four rows, not
thirty-eight, and eight of them differ here, not nine.** `floatfea/tolerances.py:1033-1037`;
`docs/milestones/F2.md:1129-1132`; `docs/reports/F2/step-5.md` section 3; the commit
message of `3dd94b8`.

```
code tolerances.py:1033 "The two renders share thirty-eight rows and nine of
     the thirty-eight differ"; F2.md:1129 the same; 3dd94b8's own cmd/out block
     "38 rows in common, 9 of the 38 differ"
cmd  regen_figures.render() against docs/milestones/F2_figures.md, rows parsed
     with the generator's own row pattern                       (this laptop)
out  committed rows 44   local rows 44   shared 44   only-committed 0   only-local 0
     differing INCLUDING the five stamp rows: 13
     differing EXCLUDING them:                8
       clean_worst_ratio        0.2564x     -> 0.2765x
       counter_defect_boundary  2.183e-06.. -> 2.174e-06..
       counter_defect_over_edge 2.745e+07x  -> 2.757e+07x
       counter_headroom_room    2.19x       -> 2.18x
       detection_edge           3.6425e-14  -> 3.6275e-14
       rigid_body_counter_loss  7.4709e-12  -> 7.4708e-12
       rigid_body_mode_ratio    1.1986e-14  -> 1.6009e-14
       rigid_body_subspace_loss 5.5095e-15  -> 5.3061e-15
     `rigid_body_counter_ratio` 3.0612e-11 identical; `detection_edge_at`
     IDENTICAL HERE -- the argmin name does not move on this machine, and it is
     the ninth of the claimed nine
judge 38 IS THE OLD FILE'S ROW COUNT. The comparison the sentence describes is
     "the canonical CI render and a laptop render OF THE SAME COMMIT"; at this
     commit that is 44 shared rows. The 38/9 pair came from comparing the
     SUPERSEDED committed file against a current render, which is a different
     measurement -- and it is the one I made in verdict 35 and handed over. My
     share, again, and this is the second round the same number has travelled.
judge AND THE TABLE ABOVE IT IS FINE. Every value in the plan's seven-row
     spread table reproduces on my machine to the digits published, and
     FIGURE_FLOOR_CLASS_SPREAD's bracket -- 1.336 < 1.5 < 2.19 -- is
     unaffected. What is wrong is the summary sentence that states the basis.
```

**Closed when** the sentence in `tolerances.py`, in `F2.md` and in the report carries a
count taken from the two renders it names, at the commit that publishes it, saying whether
the stamp rows are in the denominator. If the honest answer is that the numerator moves
with the machine, say which machine and drop the fixed nine.

**R317. (BLOCKS -- head 3) Three published outputs are not what the published command
prints, and a fourth sentence names the wrong commit. Each is one command.**
`docs/reports/F2/step-5.md` sections 2, 3 and 7.

```
(a) code S2: "cmd python -m pytest tests/test_report_guard_states.py -q /
        out 23 passed"
    cmd the same command                                        (my run)
    out 24 passed in 55.00s
    cmd the collected count at 3f648e0, 7440b81, 7254dfc and bf00121
    out 24, 24, 24, 24 -- it is not stale, it is wrong at every commit of this
        round. 23 is the number of entries in my corpus; the file is 23
        parametrised states plus test_the_corpus_and_the_states_agree.
(b) code S2: "cmd python -m pytest tests/test_report_carried.py -q -k
        WHOLE_SUITE / out 1 passed"
    cmd the same command                                        (my run)
    out 2 passed, 163 deselected -- `-k` matches case-insensitively, so
        test_the_whole_suite_line_is_about_a_commit_that_exists is in it too
(c) code S3: "cmd the two renders ... out 38 rows in common, 9 differ"
    out R316. 44 in common; 13 differ with stamps, 8 without.
(d) code S7's heading: "The whole suite, at this revision's own commit"
    cmd git log -1 --format=%h -- docs/reports/F2/step-5.md
    out bf00121, and the line names 7254dfc, its parent
    judge THE LINE IS RIGHT AND THE HEADING IS NOT, and the report's own guard
        says so: test_the_whole_suite_line_is_about_a_commit_that_exists
        documents "not the report's own commit -- that sha does not exist while
        the report is being written -- but an ancestor of it". One word.
judge FOUR OF THE REPORT'S OTHER PUBLISHED COMMANDS I RAN AND THEY ARE EXACT:
     ci_ladder_gating 60 passed, supervisor_conftest_pathspec 4 passed,
     figure_local_check 20 passed, and ci_section.py e3a3bd1 identical to
     section 0. This is not a report that stopped measuring; it is three
     figures in a revision whose whole subject is figures that were not
     re-taken.
```

**Closed when** each of (a) to (d) is re-taken or reworded at the commit that publishes it.

**R318. (recordable, 4a) The Carried pointer resolves against a section that mentions the
item, and the Carried section itself mentions every item.**
`tests/test_report_carried.py:766-781`.

```
cell every answered row's `where` set to the Carried section, table regenerated
     with the committed script, in a clone at bf00121
out  165 passed. Six pointers, none of them pointing at a discussion, all six
     resolved.
judge THE ROTATION IS GENUINELY REFUSED -- I ran that and it reddens three
     times by name -- and a self-pointer is not a rotation. Excluding the
     Carried section's own number from the resolvable set is two lines.
cmd  tests/corpus/report_guard_states.txt, entry 1 of the 2 added at aaaece2
```

**R319. (recordable, 4a) The whole-suite line is bound to an ancestor and to nothing
else.** `tests/test_report_carried.py:958-1027`. A line reading "Whole suite at 9cc7744:
1833 passed, 0 failed, 0 skipped" -- the previous verdict's commit, last round's count, at
a commit where the suite was in fact `1 failed` -- gives `165 passed` in a clone. The three
shipped assertions are: the line exists, `passed > 100`, the sha is an ancestor of HEAD.
The report did the right thing voluntarily and my run confirms its number; the guard would
not have noticed if it had not. Second corpus entry at `aaaece2`.

**R320. (recordable, 4a) `tests/test_report_numbers_are_sourced.py` exempts a
24-character WINDOW rather than a token, so a figure standing beside an item number, a
sha, a run id, a rung number or a directive code is exempt with it.**
`tests/test_report_numbers_are_sourced.py:62-142`.

```
cell nine prose lines through the shipped `_unsourced()`      (my run, bf00121)
out  "The headroom is 47x."                        FLAGGED   CONTROL
     "The count is 4056."                          FLAGGED   CONTROL
     "At R311 the headroom is 47x."                exempt
     "At 7254dfc the suite is 1889 passed."        exempt
     "Run 34523398136 published 4056 passed..."    exempt
     "Ladder 4 lost 4056 passed rows."             exempt
     "BP0 moved the figure to 4056 rows."          exempt
     a figure that is a substring of a longer fenced number    exempt
cell the report's own revision 10, with the sha pattern removed from the tuple
out  three tokens appear, and one of them is 1889 -- the headline figure of
     the round, exempt only because 7254dfc sits ten characters to its left
judge THE CHECK IS REAL AND IT WORKS ON THE SHAPE IT WAS WRITTEN FOR. Its own
     definition is "a number in prose is sourced when the same number appears
     inside a fenced block in the same section", and the number this round is
     about does not meet it. Nothing is wrong with the figure -- I ran the
     suite and got 1889 -- and the sentence does carry its command inline, so
     BF0 is satisfied where the mechanism is not.
cmd  tests/corpus/report_numbers_sourced.txt, NEW at aaaece2, 9 entries
```

**R321. (recordable, 4a) A protected directory's name split across a concatenation, with
no comment saying why.** `tests/test_report_guard_states.py:40`. The same file spells that
path in full elsewhere. The only mechanism the split defeats is `protect-reviews.sh`'s
refusal of a Bash write whose command text mentions the directory, and what the constant
is used for is a read of the verdict's history in a scratch clone -- so nothing bad
happened here. It is recorded because an obfuscated protected path with no reason beside
it is indistinguishable, to the next reader, from one written to get past the hook.

**R322. (recordable, 4a) The docs-commit guard matches `tests/test_report_*.py` only.**
`tests/test_report_carried.py:908`. A `docs:` commit that edited
`tests/test_ci_ladder_gating.py`, `tests/test_figure_local_check.py` or any of the
`scripts/` that generate the report's own tables is not caught. The state the harness
builds is real and it reddens; the file set is narrower than the rule the docstring states
("a change to the machine that measures a report is not part of the report").

## Tolerances touched

**No value moved.** `git diff 9cc7744..bf00121 -- floatfea/tolerances.py` is one comment
hunk on `FIGURE_FLOOR_CLASS_SPREAD`, replacing "over the nine rows of forty-seven that
move" with "over the nine rows that move ... The two renders share thirty-eight rows and
nine of the thirty-eight differ". **That new sentence is R316.**
`FIGURE_FLOOR_CLASS_SPREAD` is `1.5` and `FIGURE_ARGMIN_TIE_WINDOW` is `1.01`, both
unchanged, both with the counters and the brackets I re-measured last round.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `FIGURE_FLOOR_CLASS_SPREAD` | `1.5` (unchanged) | dimensionless, max over min of two renders | `1.6` | F2.md Q8 third-class table; asserted from two files by `test_figure_local_check.py` -- and the SENTENCE stating how the table was counted is R316 |
| `FIGURE_ARGMIN_TIE_WINDOW` | `1.01` (unchanged) | dimensionless factor on an extremum | `1.0216` | F2.md Q8, re-measured from the corpus in verdict 35 |

```
cmd  grep for either constant across the whole range
out  tolerances.py, F2.md, regen_figures.py, test_figure_local_check.py --
     no new numeric literal anywhere in the diff
cell the bracket, re-checked against the two files at THIS commit:
out  largest measured spread 1.336 (rigid_body_mode_ratio, reproduced above)
     smallest floor-class margin 2.19 (counter_headroom_room)
     1.336 < 1.5 < 2.19          UNCHANGED, and both sides are still asserted
                                 from files rather than retyped
cmd  python scripts/regen_figures.py --check                    (this laptop)
out  exit 0, nine floor rows, nine spreads, every exact row agrees
judge THE CONSTANT IS FINE. What is wrong is one sentence about how its basis
     was counted, which is why R316 is a finding and not a tolerance change.
```

**What held**, reproduced at my run rather than read: the whole suite, 1889 passed and no
skips, agreeing with the report's own line; the guards job green on CI at the reviewed
commit; thirteen named failures under ladder 4 where last round there were none; `--check`
with nine spreads including the words row; the rotation of three Carried pointers refused
three times by name; the instruction pathspec reverted and the new test reddening; the
regenerated CI section identical to the published one; the makereport and sessionfinish
channels caught at both conftest depths, with the no-conftest control red; and no element
source touched for an eleventh round.

**These did not**: the sentence about what a second record buys (R315), the denominator in
`tolerances.py` and in the plan (R316), and three published command outputs plus one
heading (R317).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** This round closed five of six carried items,
including the two largest: the suite is green at the reviewed commit with a whole-suite
line I reproduced digit for digit, and the guards job is green on CI for the first time in
this step. Three things are in the way and two of them are sentences.

1. **R315 -- one hook still walks past both records.** A `pytest_runtest_call` hookwrapper
   with `trylast=True` reaches `run_rung: OK` on a red rung, at both conftest depths, with
   the two records agreeing; the identical body without that one keyword is caught. The
   claim that forgery must now be consistent across two places is refuted by one keyword
   argument, and it is written into my own instruction file. Correct it there (standalone
   `process:` commit), in `run_rung.sh`, in `rung_no_xpass.py` and in the report, and put
   the shape in the layout map with its direction declared.
2. **R316 -- the denominator is still not the repository's.** 44 shared rows, 13 differing
   with the stamps and 8 without, measured at this commit; "thirty-eight" and "nine"
   describe a render that no longer exists. It is the stated basis of a constant, in three
   files.
3. **R317 -- three outputs and a heading.** 23 passed is 24, 1 passed is 2, 38 rows in
   common is 44, and section 7's heading names a commit the line does not.
4. **Ladder 4 is red.** Not this step's work, routed under Q8, and no PASS is available
   while it is. R231, R244, R245 and R275 are due next round and the canonical re-render
   is part of that answer.

**Not gates on step 5, into the next report's Carried section:** R318, R319, R320, R321,
R322, R300, R291, R292, R281, the underlying gap in R276, R277, R262, R264, R266, the two
R248 residues, R249-R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 15 new entries at `aaaece2`, across three files, one of them
new, all unseen by the implementer; every `measured=` taken at `bf00121` by running the
shipped script or the shipped check before the `require=` beside it was written.**

**The coverage measurement, stated plainly: of my 15 new entries the shipped checks do what
the entry requires on 4, and all four are controls I wrote to show the checks are not
vacuous.** All four behaved.

* `tests/corpus/ci_ladder_gating.txt` -- **+4 (57 -> 61), 1 correct**, the control. The
  `trylast` swallow, the protocol channel and the deselect channel all reach exit 0.
* `tests/corpus/report_guard_states.txt` -- **+2 (23 -> 25), 0 correct.** Both new states
  give `165 passed` in a clone.
* `tests/corpus/report_numbers_sourced.txt` -- **NEW, 9 entries, 3 correct** (two flags and
  one exempt, all three controls). **This file has no runner**, which makes R281's list one
  entry longer, and I say so rather than leaving it to be found.

With the corpus applied the two runners that have one give **9 failed, 81 passed** and name
every new entry, which is the mechanism working.

**I am still not adding to `g22_model_configurations.txt` or `g21_rigid_body_frames.txt`,
and this is the last round I will say it.** The canonical render has now stood its clean
round; the next verdict adds to both and the re-render is part of the answer, together
with R231, R244, R245 and R275.

**Thirty-six consecutive rounds have found no element defect, and this round does not
either.** Everything blocking above is a sentence, a denominator, or a hook ordering flag.
