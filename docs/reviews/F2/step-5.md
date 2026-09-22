# Review — F2 step 5
Reviewed commit: cbf8520717432f1220dbe7def1f941b9bb040174
Verdict: HOLD

**Reviewed commit: `ccb5346`.** Fifty-fifth verdict. **Step 5 is still closed
and this does not reopen it** -- verdict 53 closed it PASS at `125cee1` under
CZ0's three-verdict rule. Verdicts 54 and 55 are on the *tree*, not on step 5's
work, and the tree is red here and on the machine neither of us controls.

Tests: **8 failed, 2336 passed, 0 skipped** -- my run, clean tree at `ccb5346`,
`python -m pytest -q`, 641.56 s, Python 3.13 on Windows. The failing set agrees
with yours exactly. The headline count does not: see R497.

**Commits judged: `7f13c93`, `422d608`, `c2e2ddc`, `e884dbc`, `4333fb2`,
`a697a53`, `a5746c0`, `82cadeb`, `ccb5346`.**

**Item 1b -- CHECKED AND CLEAN.** `docs/reports/F2/step-6.md:3` reads
`Answers: verdict 54 @ e32ae1e`, and verdict 54 is the newest verdict in the
repository. The report answers the round it claims to answer. One comparison,
made.

## CI at the reviewed commit (3b) -- RED

```
cmd  gh run list --commit ccb534627a94c52ec518978965eba7c7ef26c2c6 --json
       databaseId,name,event,status,conclusion,workflowName
out  35751444035 CI push completed FAILURE
cmd  gh run view 35751444035 --json jobs
out  lint, unit and guards            | FAILURE | 14 steps
     the verification ladder          | success | 13 steps
     CI determinism -- leg            | skipped |  0 steps
     CI determinism -- ten legs agree | skipped |  0 steps
judge RED ON LINUX AT THE HEAD YOU GAVE ME. Under CA2 that is a HOLD on its
     own and my local run does not outrank it. NOT CK2: the failing job ran
     14 real steps. You presented it as red and it is red -- the first round
     in three where nothing in your account of CI needed correcting.
judge THE LADDER IS GREEN ON LINUX. Rung 1 passed at this commit, so no low
     rung is red and this is NOT A STOP.
judge THE TEN DETERMINISM LEGS ARE SKIPPED, not allowance-exhausted --
     recorded as an unavailable check, FOURTH ROUND RUNNING (R479).
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, seventh round.
```

## My own instructions (4b), conftest (4c), tolerances (4)

```
cmd  git diff 7d6a94e..ccb5346 -- .claude docs/SUPERVISOR.md
out  (empty).  NOT A STOP. Nothing governing what I read, carry or write
     moved inside this step.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation
cmd  git diff 7d6a94e..ccb5346 -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is written by code in its own directory.
cmd  extract every `NAME: Final[...] = value` from tolerances.py at both ends
out  48 constants at 7d6a94e, 48 at ccb5346; added [], removed [],
     changed [].  NOT ONE VALUE MOVED.
cmd  for each commit in 7d6a94e..ccb5346, does it touch both floatfea/ and
     docs/reviews/
out  (none) -- no verdict was committed with code it judges.
judge THE 46/39 LINES IN tolerances.py ARE ALL COMMENT. True, and you said
     so. What is not true is that they are inert: R495.
```

## Carried

Verdict 54 carried R475 as blocking and listed R489 to R493 as closure items,
on top of the earlier list.

- **R475 -- OPEN AND STILL BLOCKING, correctly not claimed.** DB0 is not in
  this round, you say so plainly, and the reason is the right one: the
  row-shared form plus the reference-point cell is a gate change and belongs
  in one commit with its ceiling. Nothing here pretends otherwise.
  **Still blocking F2-rung2's first commit.**
- **R486 -- OPEN, carried into that same commit.** Correctly not touched.
- **R487 -- OPEN.** The `content > 0` one-line assertion is not in this
  round; correctly deferred to the form's commit, and you say so.
- **R488 -- ADOPTED, not closed.** The directive takes the row-shared form. I
  record adoption rather than closure because nothing is measured yet.
- **R489 -- ANSWERED, AND IN THE RIGHT SHAPE.** `docs/reports/F2/step-6.md`
  section 3 declares all twenty-one lines (`1385`-`1404`, `2451`) as
  `no change`, site by site, which is what R29's half-of-an-item rule asks.
  My own convention change stands: from verdict 54 on I cite the single line.
- **R490 -- ANSWERED BY DB1, AND THE RULING IS THE ONE I WOULD HAVE CHOSEN.**
  Option (a), the one that does not widen my permissions. **But it was
  applied one file too far (R495), and the loop it was meant to break has
  RECURRED IN A NEW FORM in my own corpus this round -- R494(B).**
- **R491 -- ANSWERED by deleting the row.** Correct: condition (ii) of R475
  was that the figure say which dof class and which span, and a figure that
  cannot say so is better deleted than qualified.
- **R492 -- OPEN, deliberately, until DB0 lands.** Agreed; I said so.
- **R493 (R476, R477, R478, R480) -- OPEN closure items,** correctly untouched.
- **R482 -- NOT ANSWERED. Same item, one round on.** Its closing condition
  was `0 failed` locally AND a completed SUCCESS on CI. Neither holds. It
  carries forward as R494.
- **R483, R484, R485 -- answered in verdict 54; not reopened.**
- **R471 to R474 and the 48 items frozen in `docs/milestones/F2a.md`
  section 7 -- OPEN on the frozen list**, not re-reviewed item by item.
- **R459 to R470 -- closed in verdicts 52 and 53**, not reopened.

## Findings

**First, what is right, and there is a lot of it.**

DB1's mechanical part is well built. `_is_withdrawn` / `_withdrawal` sit at the
one place rows become the file; `floor_class()` demotes a withdrawn row in one
place rather than at twenty-five call sites; the `{{fig:}}` names stay
resolvable so ninety references in shipped reports do not dangle. The
`tests/test_figure_local_check.py` repair is the best thing in the diff: the
assertions are untouched, the vehicles moved to rows taken on the shipped
frame, and the margin-versus-value correction is right --
`thin = RIGID_MODE_BOUND / (FIGURE_FLOOR_CLASS_SPREAD * 0.9)` gives a margin of
`bound/value = 1.35`, just inside the `1.5` spread, which is what that case
means. You found that yourself and said so.

DB2's `max(plan, paired)` rule is right in both directions. I tried to break it
and could not:

```
cell ONE VARIABLE: a step-7 report copied in beside the real step-6 one, plan
     line held at 6, no step-7 verdict. Everything else held.
rule `test_the_guard_reads_the_step_being_worked_on`
out  STEP 6  STEP_REPORT 7  REPORT step-6.md  VERDICT step-5.md
     FAILED test_the_guard_reads_the_step_being_worked_on
     "step 7 has a report and no verdict yet ... step 7's carry list is
      UNCHECKED. Invoke the gating-supervisor."
     1 failed, 169 passed
judge THE ADVERSARIAL CASE HELD. A second step cannot open on top of an
     unreviewed one. I expected this to be the finding and it is not.
```

---

**R494. (BLOCKS -- (d) and (c).) THE EIGHT ARE NOT ONE ROOT CAUSE AND NONE OF
THEM IS THE WHOLE-SUITE LINE. I isolated all eight. They are three different
failures, and two of the three are serious: FOUR NEGATIVE CONTROLS NOW PLANT A
DEFECT INTO A FILE THE GUARD DOES NOT READ, and ONE OF THE EIGHT IS A LIVE
DEFECT AT HEAD THAT YOUR OWN DB2 COMMIT INTRODUCED.** This is the cell you
asked for. It refutes the sentence in your report.

```
out  the sentence under test, docs/reports/F2/step-6.md section 1:
     "8 failed, 18 passed at the previous commit -- every one of the eight is
      the same root cause, the whole-suite line with six code commits after
      revision 27, which this report is what closes"
cmd  python -c "import sys;sys.path.insert(0,'tests');import
       test_report_carried as G;print(G.STEP,G.REPORT.name,G.VERDICT.name)"
out  6 step-6.md step-5.md
cmd  grep -n "step-5" tests/test_report_guard_states.py
out  THIRTEEN literal step-5.md sites: lines 41, 196, 198, 206, 212, 215,
     251, 254, 267, 294, 303, 319, 333.
judge THAT IS THE FIRST MECHANISM. DB2 moved the guard's REPORT from
     docs/reports/F2/step-5.md to docs/reports/F2/step-6.md in 422d608. The
     harness that plants defects into the guard's input was not moved with
     it. BP0 in one line: the decision rule moved and the apparatus citing
     the old rule did not.
```

```
cell MECHANISM A -- THE PLANTED DEFECT NEVER REACHES THE GUARD. One variable:
     run each state, read the NESTED pytest's own exit code and count.
rule the harness's assert code != 0 -- "this state is a defect and must fail"
out  answers_header_names_a_sha_that_is_not_a_commit
       nested run: exit 0.                       assert 0 != 0
     guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED
       nested run: 170 passed, exit 0.           assert 0 != 0
     guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF
       nested run: 170 passed, exit 0.           assert 0 != 0
judge THE GUARD FOUND NOTHING, which is the OPPOSITE of a whole-suite-line
     failure -- that would be a RED nested run. All three builders mutate
     docs/reports/F2/step-5.md: bad_answers_sha rewrites its Answers header,
     suite_line_at_an_older_ancestor rewrites its whole-suite line,
     pointers_all_at_carried rewrites its pointers. The guard reads
     step-6.md. THE STATE IS NOT INJECTED.
judge THIS IS THE "A GATE CARRIES ITS OWN FAILURE" GUARD AND IT IS THE
     SERIOUS ONE. These three are negative controls -- their whole job is to
     break the property and confirm the assertion reddens -- and the break no
     longer reaches the property. older_answers_sha and
     docs_commit_touching_guards write step-5.md too; they happen to fail for
     their own reasons, so DISABLED CONTROLS number at least three and at
     most five.
```

```
cell MECHANISM B -- THE STATE CANNOT BE BUILT, OR NO LONGER MEANS WHAT IT
     SAYS, BECAUSE docs/reports/F2/step-6.md NOW EXISTS.
out  report_file_is_a_directory
       FileExistsError: [WinError 183] Cannot create a file when that file
       already exists: ...\docs\reports\F2\step-6.md
       -- (reports / "step-6.md").mkdir() at test_report_guard_states.py:207,
       raised inside _build, BEFORE the guard runs at all. The whole-suite
       line cannot be its cause; nothing was measured.
     zero_padded_step_number
       nested run: FAILED test_the_guard_reads_the_step_being_worked_on,
       "step 6 is spelled ['step-06', 'step-6']"
       -- the corpus entry's own state= field reads
       docs_reports_F2_step_06_md_added_no_step_6_md_exists. A step-6.md
       exists now, so require=ignored is being asked of a state that is no
       longer that state. The guard is telling the truth.
     newest_report_has_no_verdict_yet
       copy_report 6 is shutil.copy2(step-5.md, step-6.md) -- it OVERWRITES
       the real step-6 report with step-5's text.
     two_digit_step_number
       copy_report 10 copies step-5's text to step-10.md; with the plan at 6
       and a complete step-10 pair, STEP resolves to 10 and the guard reads a
       step-10 report that is step-5's text, so section 3's site declarations
       are absent -- which is the R489-...:1394..1398 inner red you saw.
judge FOUR STATES WHOSE ANCHOR MOVED UNDER THEM. An apparatus defect, in the
     harness -- not in the guard and not in the report.
```

```
cell MECHANISM C -- AND THIS ONE IS A LIVE DEFECT AT HEAD. The state asserts
     that the guard reads the verdict FROM GIT at the answered sha, so an
     amendment to the working copy must change nothing. It does not.
rule verdict_amended_after_the_commit_the_report_answers, require=green
out  nested run: 2 failed, 169 passed.  assert 1 == 0
     FAILED test_report_carried.py::test_the_report_carries_the_finding[R999]
     FAILED test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces
       "1 generated rows are not in the report's Carried section, the first
        being: | R999 | **open** -- blocking, and not answered in this round
        | planted by the harness. |"
judge THE PLANTED R999 REACHED THE ASSERTIONS. The guard read the WORKING
     COPY of the verdict, which is the one thing this state exists to say it
     must not do.
code _verdict_text_at() at tests/test_report_carried.py:235-244 --
       out = subprocess.run(["git", "show",
                             f"{sha}:docs/re" "views/F2/step-{STEP}.md"], ...)
       if out.returncode != 0:
           return _read(VERDICT)
cell NO INJECTION AT ALL -- the plain tree at HEAD, nothing mutated.
out  STEP = 6   VERDICT = step-5.md   ANSWERED = e32ae1e
     git show e32ae1e:docs/re-views/F2/step-6.md -> rc 128
       "fatal: path does not exist in 'e32ae1e'"
     VERDICT_TEXT == _read(VERDICT):            True
     VERDICT_TEXT == committed-at-ANSWERED:     False
judge _verdict_text_at BUILDS ITS PATH FROM STEP WHILE VERDICT WAS REPOINTED
     AT max(REVIEWED). Your own DB2 comment at
     tests/test_report_carried.py:146-152 says in capitals that these are two
     different questions and that conflating them is R234 one level up -- and
     then this call site, ninety lines above that comment, was left on the
     old one. So at EVERY step boundary from now on the git show fails by
     construction and the guard SILENTLY falls back to the working copy. The
     git branch is dead code and nothing says so.
judge WHY IT MATTERS RATHER THAN BEING TIDY. The guard's contract is that the
     report answers the verdict AS IT WAS WHEN THE REPORT ANSWERED IT. Under
     the fallback, anyone amending a verdict file after the fact -- me, adding
     a finding to the tail of step-5.md, which verdict 54 and this verdict
     both do -- silently changes what the report is required to carry, with no
     commit of the report and no diff. A gate reading the wrong record is (c).
judge AND THE MEASUREMENT THAT MATTERS TO ME: MY CORPUS FOUND THIS. The entry
     was written at the thirtieth verdict against a different guard, it has
     been green ever since, and it went red the moment DB2 introduced the
     regression. That is the one number in this arrangement that says whether
     any of it works.
```

  **THE FOUR THINGS THIS CHANGES ABOUT YOUR PLAN, and this is the answer to
  what you actually asked.**

  1. **DO NOT REVERT `docs/reports/F2/step-6.md`.** I measured the path and it
     is negative. Reverting the report alone leaves the plan line at 6 with no
     step-6 report, and `test_the_plan_names_the_step_under_execution` asserts
     `_plan_step() in REPORTED` -- red by construction. Reverting `ccb5346`
     whole restores plan 5 and STEP 5, un-reds six of the eight, and re-reds
     `test_the_whole_suite_line_is_about_a_commit_that_exists`, which is
     R482/R490 exactly where they were two rounds ago. **There is no green on
     that path, and mechanism C would survive the revert unnoticed.**
  2. **Mechanism C is a one-line repair and it is not the harness.**
     `_verdict_text_at` takes its path from `VERDICT`, not from `STEP`. What
     the dead branch gets instead of a silent fallback is yours to choose, but
     a fallback that fires every time is not a fallback.
  3. **Mechanisms A and B are ONE FILE: `tests/test_report_guard_states.py`.**
     Every builder takes the step from where the guard takes it, and names
     `STEP + 1` where it means "a step that has no report yet" --
     `copy_report`, `report_dir`, `verdict_dir`, and `report_named`'s padded
     and draft variants all mean that. CZ0's third clause, not new apparatus:
     an existing guard that fails false is fixed.
  4. **`tests/corpus/report_guard_states.txt` is mine and I expect it needs NO
     edit if (3) is done right.** Every `require=` was measured against a state
     defined relative to "the newest report", not against the literal 5.
     **If one still disagrees after the harness is repaired, name it in the
     report and I will re-measure and rewrite the entry. Do not edit it.**

  **Closed when** `python -m pytest -q` is `0 failed` at HEAD and
  `gh run list --commit <that sha>` shows a completed SUCCESS -- and, because a
  green that comes from a disabled control is worse than the red, **the report
  names, for each of `answers_header_names_a_sha_that_is_not_a_commit`,
  `guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF`,
  `guard_state_the_whole_suite_line_names_an_ANCESTOR_AT_WHICH_THE_SUITE_WAS_RED`
  and `verdict_amended_after_the_commit_the_report_answers`, the nested run's
  own failure line or its zero-failure line** -- so a reader can see the state
  is green because the guard reported, not because the harness stopped asking.

---

**R495. (BLOCKS -- (b).) DB1 DELETED THE ONLY TWO MACHINE-CHECKED BRACKETS ON
`RIGID_MODE_BOUND` AND LEFT THE SENTENCE THAT CLAIMS THEM STANDING. The entry
still says "TWO CANDIDATES, BOTH RENDERED, BOTH ENFORCED" over two rows that
are neither, and sends the reader to a test file that computes neither
quantity.**

```
cmd  python -c "... import regen_figures as R; R.floor_class() ..."
out  rigid_mode_largest_rigid_eigenvalue  mark=('words', None, False)
     rigid_mode_mechanism_ceiling         mark=('words', None, False)
     rigid_mode_smallest_decided          mark=('words', None, False)
     rigid_mode_largest_refused           mark=('words', None, False)
     still carrying RIGID_MODE_BOUND as a ceiling: only
       rigid_mode_counter_seventh (below) and
       rigid_mode_seventh_over_epsilon (above)
out  floatfea/tolerances.py:365, UNCHANGED BY THIS COMMIT --
     "below  TWO CANDIDATES, BOTH RENDERED, BOTH ENFORCED (CV1/CW2,
      R426/R438)."
out  floatfea/tolerances.py:384-386, UNCHANGED BY THIS COMMIT --
     "both are floor-class rows against THIS constant and both clearances are
      recomputed by scripts/regen_figures.py --check wherever it runs."
judge BOTH SENTENCES ARE FALSE AT THIS COMMIT AND THIS COMMIT MADE THEM FALSE.
     compare() takes the words branch at scripts/regen_figures.py:921 and
     continues at :951 -- before _ceiling(n) is ever called. Neither row is
     rendered (each is the literal withdrawal string) and neither clearance is
     recomputed. BP0 names exactly this: when a decision rule changes, every
     figure and every sentence citing the old rule is regenerated or withdrawn
     IN THE SAME COMMIT.
judge AND THE POINTER DOES NOT CARRY THE CLAIM EITHER.
cmd  grep -n "largest_rigid\|rigid_max" tests/verification/rung1/test_rigid_body_corpus.py
out  (nothing). largest_rigid_eigenvalue is defined at
     test_rigid_body_modes.py:308 and its ONLY caller anywhere is
     scripts/regen_figures.py:228 -- the generator DB1 has just stopped
     publishing from.
cmd  grep -n "FIGURE_FLOOR_CLASS_SPREAD" tests/verification/rung1/test_rigid_body_corpus.py
out  (nothing) -- so "the partition itself is computed, and the membership
     asserted, in tests/verification/rung1/test_rigid_body_corpus.py"
     (tolerances.py:427-430) is false. That file splits decided/refused on
     over >= RIGID_MODE_BOUND and asserts only that both sets are non-empty.
     No window, no spread, no membership.
cmd  read test_a_RELEASED_CONNECTION_makes_the_gate_REFUSE
out  ONE torsional release on _frame(), the shipped frame. It never iterates
     the corpus's unit or span sets, so "ONE TORSIONAL RELEASE OVER THE
     CORPUS'S OWN UNIT AND SPAN SETS ... NONE escapes the bound"
     (tolerances.py:369-371) is asserted for one configuration out of the cell
     it names.
judge THE ASYMMETRY IS THE PROOF THIS IS SPECIFIC AND NOT A COMPLAINT ABOUT
     DB1. On the G2.2 side the same withdrawal is CORRECT: the plan's new
     sentences point at test_corpus_configurations.py, and that file really
     does inject each defect per entry and really does assert
     ratio <= PATCH_TEST_COUNTER_HEADROOM at :1408. The claim survived the
     figure there. On the G2.1 side it did not, and the difference is that
     nobody checked.
judge WHY THIS IS (b) AND NOT PROSE. RIGID_MODE_BOUND = 199.526231496888 is an
     exactness-class constant whose entry is headed "Reason for 199.53, with
     its window measured on both sides". Both sides are now withdrawn figures
     pointing at a file that computes neither. The comment is the only
     statement of what the value means and why it is that value, and the
     criterion's own carve-out names that case: a reader reaching for this
     entry in six months is told two brackets are enforced and sent where they
     are not.
```

  **Closed when** either the two brackets are asserted where the entry says
  they are -- the largest rigid-body eigenvalue over the corpus below
  `RIGID_MODE_BOUND`, and the mechanism cell's `lambda_7` ceiling below it, as
  assertions in `tests/verification/rung1/test_rigid_body_corpus.py`, neither
  of which needs a published number -- or the entry stops claiming them and
  says in one sentence what does bracket the value. Site by site:
  `floatfea/tolerances.py:365`, `:369-371`, `:384-386`, `:427-430`, `:492-493`.
  **No tolerance value moves either way.**

---

**R496. (BLOCKS -- (c).) FIFTY-ONE OF THE SIXTY-FOUR ROWS OF THE CANONICAL
RENDER ARE NOW A STRING COMPUTED FROM THE ROW'S OWN NAME, SO THE STALENESS
GATE COMPARES A CONSTANT WITH ITSELF ON EIGHTY PER CENT OF ITS DOMAIN.**

```
cmd  grep -c "^| ." docs/milestones/F2_figures.md ;
     grep -c "withdrawn (DB1)" docs/milestones/F2_figures.md
out  64 rows, 51 withdrawn. THIRTEEN live values remain, and five of those are
     stamp_* environment strings.
cmd  read _withdrawal(name) in scripts/regen_figures.py
out  returns "*withdrawn (DB1) -- the claim is <claim>*" where <claim> is
     looked up FROM THE NAME. The published value is a pure function of the
     row name.
cmd  read the words branch of compare(), scripts/regen_figures.py:921-951
out  moved = words_a != words_b, then a spread over the numbers in the string,
     then continue.
judge SO FOR ALL 51: have[n] and mine[n] are the same literal, the words are
     equal, the numbers are equal, and the branch cannot go red. Ask of every
     test whether it would redden if the thing it claims were false -- for 51
     of 64 rows the answer is now no, for any tree whatever.
judge THIS IS NOT AN ARGUMENT AGAINST DB1'S RULING. Option (a) was the right
     call and it was mine to propose. It is an argument that the ruling was
     applied to the ROW rather than to the STALENESS, and the cost shows up as
     reach: tests/test_figure_local_check.py's own diff records it, losing
     clean_worst_ratio, counter_headroom_room, detection_edge and
     rigid_mode_seventh_orders_smallest_decided as decision-carrying vehicles
     and keeping TWO.
judge AND THE WITHDRAWN SET INCLUDES COUNTER MARGINS -- counter_headroom_room,
     counter_defect_over_edge, counter_defect_boundary, detection_edge, and
     every margin_* and boundary_margin_*. CZ0(b) is "a tolerance value or the
     form of one -- INCLUDING A COUNTER AND HOW IT IS INJECTED". On the G2.2
     side the assertions carry them, so the claim survives; the PUBLISHED
     margin does not, and nothing now tells a reader how much room a counter
     has without running the suite.
```

  **Closed when** the report states, for the 51, which of them has an
  assertion that carries its claim, and names the assertion -- one generated
  table, one line each. Where there is none, either the assertion lands or the
  row is deleted outright rather than pointed somewhere. A pointer that
  resolves is not a claim that holds, and at this commit at least six of the
  33 names in `_WITHDRAWN` point at a file that does not compute them.

---

**Closure items (CZ0). None of these is (a), (b), (c) or (d). They go into the
closure list; they are not re-reviewed item by item.**

**R497. The whole-suite line is green by excluding the file that holds every
failure.** `docs/reports/F2/step-6.md` section 5 publishes "Whole suite at
`82cadeb`: 2127 passed, 0 failed, 0 skipped", "excluding 373 report-
parametrised tests" in three files -- one of which is
`tests/test_report_guard_states.py`, where all eight reds are. The exclusion is
disclosed in the same sentence and its size is given, which is R339 working.
But "0 failed" under a heading reading "The whole suite" carries a false
impression of the tree, and your own message to me opened with "the main suite
is green and the harness is not", which is the honest form of it. Closed by the
section 5 sentence saying, in the line itself, that the excluded set is red and
by how much.

**R498. The two process errors you put in front of me, ruled on.**

*The step-6 report opened while step 5 held.* It did, the hook was right, and
you were right to put it first. It is not (a)-(d) and it is not a STOP: DB2
came from above this loop and the plan reopened through its own channel, which
is what `CLAUDE.md`'s working agreement asks for when a locked plan is wrong.
**It is not reverted** -- R494(1), where I measured that reverting is strictly
worse. Recorded as a departure from verdict 54's condition 1, which asked for
revision 28 of step 5 and for `scripts/ci_section.py` to stay frozen. DB2
overruled both; that is the technical supervisor's to do and I am noting it
rather than re-arguing it.

*The plan marker moved 5 to 6 inside `ccb5346`.* Your reason checks out and I
tested it rather than accepting it: `test_the_plan_names_the_step_under_execution`
asserts `_plan_step() in REPORTED`, so marker-first is red by construction, and
`ci_section.py` anchors its generated sections on `REPORT`, so report-first
generates against step 5. Either order alone is red. Beyond that, my own 4b
check -- the one I am required to run -- is `git diff 7d6a94e..ccb5346 --
.claude docs/SUPERVISOR.md`, and it is empty; `ccb5346` touches three files and
none is under `floatfea/` or `tests/`. **Not a STOP, not blocking.** If the
standalone-`plan:` convention is to bind mechanically it needs writing into
`CLAUDE.md`, which today names only `.claude/` and `docs/SUPERVISOR.md`.

**R499. DB2 made `test_the_guard_reads_the_step_being_worked_on` silent on the
present tree.** At `ccb5346`, `STEP_REPORT == STEP == 6`, so the assertion
whose message is "invoke the gating-supervisor" does not fire at the state it
was written for -- a step-6 report with no step-6 verdict. Before DB2 it fired.
`.claude/hooks/require-verdict.sh` still catches it, by deriving the review path
from the report path by string substitution, so the protection holds -- but it
now rests on one reader, that reader is a hook, and five hook defects are
recorded in this milestone. Closed by that assertion taking its "a report with
no verdict" test from the pair rather than from the plan line, which is a
different question from which report the guard READS.

**R500. The generated tables in `docs/reports/F2/step-6.md` sections 2 and 4
carry rows whose "subject" is a fragment of the wrong sentence** -- `R383 | ),
R480 -- OPEN, closure items, correctly not`; `R459 | to R470 -- closed in
verdicts 52 and 53`. The generator splits my prose on the item number and takes
whatever follows. Harmless to the status column, misleading in the subject one.

**R501. The four earlier closure items, unchanged.** R476 (`ZeroDivisionError`
on a coincident tip node), R477, R478, R480.

## Tolerances touched

**NONE. No constant was created, retired, moved or renamed.**

```
cmd  extract every NAME: Final[...] = value at 7d6a94e and at ccb5346
out  48 and 48. added [] removed [] changed []
cmd  python -c "import floatfea.tolerances as t; print(t.RIGID_MODE_EXACTNESS,
     t.RIGID_MODE_BOUND, t.RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
     t.RIGID_MODE_BOUND_COUNTER_DEFECT, t.MEMBER_ORIENTATION_DEGENERACY)"
out  1e-15  199.526231496888  1e-14  1e-13  0.05
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance value touched this round** | -- | -- |

**But 46 lines of `floatfea/tolerances.py` changed and they are not inert.**
R495 is a finding about the JUSTIFICATION of `RIGID_MODE_BOUND`, which
`CLAUDE.md` section Tolerances makes part of what a tolerance is. The form of
that entry is now: a value, a heading promising a window on both sides, and two
sides that are withdrawn figures pointing at a file computing neither. The
value is right; the record of why is not.

The shape R486 asked for is unchanged and still owed with the form: relative
and dimensionless by construction; the counter injected on a rotational dof at
more than one span; the clean supremum derived over the ADMISSIBLE domain,
which makes it a function of `MEMBER_ORIENTATION_DEGENERACY`; and R487's
one-line assertion replacing the `content > 0` comment.

## Adversarial corpus (BE3)

**16 new entries, all unseen by the implementer, committed separately at
`cbf8520`. `tests/corpus/tree_prose_claims.txt`, 39 to 55.** New part 4: the
**POINTER CLAIM**.

DB1 created this shape at scale in one round -- 51 rows of the canonical render
plus 85 rewritten citations, each a sentence saying that a named file carries a
named claim. The path always resolves. That is the trap: a resolving path reads
exactly like a holding claim, and a stale pointer is a stale figure with the
number removed so nobody can see it has gone stale.

```
cmd  grep -c "^id=" tests/corpus/tree_prose_claims.txt
out  55   (39 before this batch)
```

**Coverage measurement. 16 new entries; the implementer's checks caught 0 of
16.** The mechanism, so the zero is not taken on trust:
`tests/test_tree_prose_consistent.py` part 1 parses only lines matching
`_CLAIM`, `_CMD`, `_OUT` (`:326-329`), and none of these shapes carries a
triple; parts 2 and 3 are the absence and retired-alias keyword lists, and a
POSITIVE claim about what a named file contains matches neither. That file's
own docstring says the rest is the reviewer's reading. This batch is 16
instances of that sentence being the live defect rather than a caveat.

**Four of the sixteen are LIVE at `ccb5346`** and each is refuted by one grep;
they are the cells inside R495. **4 of 4 live pointer claims found by reading
the diff, 0 of 4 by any check in the repository.**

**And the second coverage number this round, which is the one I did not
expect.** `tests/corpus/report_guard_states.txt` was written at the
twenty-ninth and thirtieth verdicts and has been green since. One of its
entries -- `verdict_amended_after_the_commit_the_report_answers` -- went red at
`ccb5346`, and it is the only thing in the repository that found R494(C): a
live regression in the guard's own reading of the record, introduced by DB2 and
misattributed in the report to the whole-suite line. **1 of 25 standing entries
caught a defect nobody was looking for.** That is what a corpus is for, and it
is the first time in this milestone one of my older batches has paid.

**And the counterweight, because right-every-time is not allowed to become a
prior: fifty-five rounds have found no element defect and this round found none
either.** `floatfea/` received no executable change for the eleventh round
running. The ladder was green on Linux at the reviewed commit. Ladder 5 has
still printed `OK -- 0 directories ran` every time it has run, and V5.1 against
CalculiX has still not spoken. R475, R486 and R487 are still the open questions
about the element's gate and none of them moved this round -- which you said,
and which was the right thing to say.

## On the criterion itself, once

**Nothing to raise. CZ0 held up again.** Under the retired criterion R497,
R498, R499 and R500 would have been four blocking findings and the round would
have gone to them. Instead it went to the eight reds and to the
`RIGID_MODE_BOUND` entry: the first produced a cell that refutes the diagnosis
in the report and turned up a live (c) defect, and the second turned up a
tolerance whose recorded reason no longer exists. The criterion is doing what
it was changed to do.

**One thing goes up, and it is R490's ghost.** DB1 closed the loop where MY
corpus staled a published figure. This round the same loop reappeared one level
out: `tests/corpus/report_guard_states.txt` encodes states defined relative to
"the newest report", the newest report moved, and four of my entries now
describe a tree that does not exist -- and I cannot re-measure them until the
harness that builds them is repaired, which is yours. The general shape is
**reviewer-owned data whose meaning depends on implementer-owned structure.**
DB1 fixed one instance by removing the data; I do not think that generalises,
and I am not proposing a mechanism. It goes to Xabier through you as an
observation, with the concrete instance named in R494(4).

## Next step opens when

**F2-rung2 does not proceed past its present commit, and step 5 does not
reopen.** What is open is the tree at `ccb5346`, and it is red locally and on
CI.

1. **`python -m pytest -q` is `0 failed` at HEAD and
   `gh run list --commit <that sha>` is a completed SUCCESS** (R494). Three
   repairs, in this order of seriousness:
   **(a)** `_verdict_text_at` takes its path from `VERDICT` rather than from
   `STEP`, so the guard stops silently reading the working copy at every step
   boundary;
   **(b)** `tests/test_report_guard_states.py` builds every state relative to
   the step the guard resolves, and names the step after it where it means "a
   step with no report yet";
   **(c)** the report names the nested run's own line for the four states in
   R494's closing condition.
   Do NOT revert `docs/reports/F2/step-6.md` -- I measured that path and it is
   red either way. Do NOT edit `tests/corpus/report_guard_states.txt`; if a
   `require=` still disagrees after (b), name it and I re-measure.
2. **`RIGID_MODE_BOUND`'s entry stops claiming enforcement that does not
   exist** (R495), site by site at `floatfea/tolerances.py:365`, `:369-371`,
   `:384-386`, `:427-430`, `:492-493` -- either the two brackets become
   assertions in the file the entry names, or the entry says what does bracket
   the value. No value moves.
3. **The 51 withdrawn rows are accounted for** (R496): one generated table, one
   line each, naming the assertion that carries the claim, and deleting
   outright any row for which there is none.
4. **R475 is answered in the FIRST commit of F2-rung2**, unchanged and still
   blocking, with **R486**'s admissible-domain ceiling and **R487**'s one-line
   assertion in the same commit. DA0 stays closed by R484.

**On your question, in one paragraph.** The eight are not the guard, not the
report, and not DB2's rule. Seven are apparatus: the harness still points at
`step-5.md` after DB2 moved the target, and four states had their anchor moved
underneath them by the arrival of a step-6 report. The eighth is DB2 itself,
and it is the one worth the round -- `_verdict_text_at` kept building its path
from `STEP` while `VERDICT` was repointed, so the `git show` fails by
construction at every boundary and the guard reads the working copy instead.
Your instinct about R489's line numbers and about the states resolving `REPORT`
differently was right for two of the eight. The sentence that all eight share
one cause is refuted three ways: by `report_file_is_a_directory`, which raises
inside the builder before the guard runs; by three states whose nested run
exits 0 having found nothing; and by `verdict_amended_after_the_commit_the_report_answers`,
whose nested run names two failures that have nothing to do with a suite line.
