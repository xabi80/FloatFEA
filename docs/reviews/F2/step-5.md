# Review — F2 step 5
Reviewed commit: 8de404a8788f8801d0713304c0edc82085d942ca
Verdict: HOLD

**Reviewed commit: `55498f4`** (the verdict is stamped at my corpus commit `8de404a`,
which touches `tests/corpus/` only).

Tests: **1850 passed, 0 failed, 0 skipped** (my run at `55498f4`, `python -m pytest -q`,
285.33 s, Python 3.13.11 on Windows). The report publishes no whole-suite figure this
revision; the two subset figures its commit message carries both reproduce exactly --
`tests/test_report_carried.py` **231 passed**, the guards job body **554 passed**. With my
thirty-fourth-round corpus applied, `tests/test_ci_ladder_gating.py` gives **9 failed, 46
passed** and the vocabulary runner gives **7 failed, 25 passed**; the two files without a
runner induce zero failures.

**Plan: untouched. Code: `1be5606`, `05133c4`. Report: `55498f4` (revision 8).**

**Item 1b.** The newest revision's header reads `Answers: verdict 33 @ 35e7ddc` and
`35e7ddc` is the thirty-third and latest verdict. **Passes.**

**CI, item 3b, at the reviewed commit. RED -- and it is one test, and it is the right
one.**

```
cmd  gh run list --commit 55498f4
out  34461854122 (push) failure   34461858006 (pull_request) failure
cmd  gh run view 34461854122 --json jobs
out  lint / unit / ladder 1,2,3        success
     CI determinism -- leg (1..10)     SUCCESS x10      <- ten of ten
     CI determinism -- ten legs agree  SUCCESS          <- the job CG1 asked for
     guards and meta-tests             FAILURE
     ladder 4                          failure          <- 13, routed under Q8
     ladder 5, ladder 6                skipped
cmd  gh run view 34461854122 --log-failed | the guards job
out  FAILED tests/test_plan_figures.py::test_the_generated_figures_are_not_stale
     1 failed, 553 passed
judge THE GUARDS JOB WENT FROM 302 FAILURES AT 35e7ddc TO 16 AT 05133c4 TO ONE
      HERE, AND THE ONE IS R293'S OPEN HALF. That is the round working. It is
      still a red CI, CA2 is not discretionary, and it coincides with the
      implementer's own account: the canonical render is not committed.
cmd  gh run list --commit 1be5606 ; --commit 05133c4
out  34459537327 failure ; 34460382184 failure -- both ran, both with the same
     two reds (guards, ladder 4) and ten green legs.
```

`git diff 35e7ddc..HEAD -- floatfea` is empty, a **tenth** round. `-- floatfea/tolerances.py`
empty. `-- tests/regression` empty. `-- docs/milestones/F2_figures.md` empty.
`-- docs/milestones/F2.md` empty. No commit in the range touches `docs/reviews/`.

**PR #1 is open, `F2 -> master`, `gh pr view 1 --json comments` returns 0 comments.** Step
5 still has no outside-witness comment. Recorded as an unavailable check, not as a pass.

## Carried

Verdict 33 listed seven blocking items plus two at 4a. **Five close outright. One closes
in substance with its published command stale. One is half-closed by the implementer's own
statement, and I agree with the half.**

- **R293 -- HALF CLOSED, and the half that closed is the biggest thing in the range.**
  The job measures before it compares, the measurement cannot be suppressed, and a separate
  job asserts the ten legs against each other. I verified every leg myself rather than
  reading the table.

```
cmd  gh run view 34460382184 --log | the ten leg rows at 05133c4
out  2af0f7cbaee3... and Haswell on 10 of 10; 4 collected, 0 failed on 10 of 10
     AMD EPYC 7763 x4, 9V74 x1, 9V45 x1; INTEL 8573C x2, 8370C x1, 6973P-C x1
     "ten of ten identical: 2af0f7cbaee3 core Haswell"
judge SIX CPU MODELS ACROSS TWO VENDORS, ONE HASH. This is the first time this
      branch has had CG1, and it is a STRONGER result than the report publishes
      (R305). The regression rung ran on all ten and passed.
cmd  gh run download 34460382184 -n determinism-leg-1 ; sha256sum F2_figures.md
out  2af0f7cbaee3...  == the leg's own figures.sha256. CG2's artifact IS the
     file the legs agreed on, checked rather than assumed.
cmd  the downloaded render against the committed one, newline-normalised
out  9 of 47 lines differ, 38 identical
judge AND `COMMITTED-MATCHES-CI no` ON 10 OF 10. The corpus entry
      `determinism_all_ten_legs_render_bytes_equal_to_the_committed_file` is
      still NEVER OBSERVED at any commit on this branch.
```

  What remains of R293 is its own item, and the implementer says so plainly. My ruling on
  the question it ends with is at the foot of R303.

- **R294 -- CLOSED at all three clauses, and I ran every cell.** This is the first repair
  in this file's history aimed at the rule rather than at a producer, and the ablation
  column is honest.

```
cell the five scenarios of section 2, rebuilt from scratch outside the
     repository, each tree carrying the project's own pyproject.toml, each run
     twice (shipped, and `-p rung_no_xpass` deleted and nothing else):
out  xpass whose body warns "3 passed in 0.01s"     1 / 0     as published
     xpass + conftest pytest_terminal_summary       1 / 0     as published
     CLEAN rung warning "1 xpassed in 0.01s"        0 / 0     as published
     module-level print of a count phrase           0 / 0     as published
     a genuinely failing test                       1 / 1     as published
judge FIVE OF FIVE REPRODUCE. Both doors are shut and the mirror fault is gone.
cmd  pytest tests/test_ci_ladder_gating.py -q -k xpass            (shipped)
out  9 passed, 39 deselected
cmd  the same with `-p rung_no_xpass` deleted from scripts/run_rung.sh
out  8 failed, 1 passed, 39 deselected -- the one green is the false-positive
     control, which the repair is not what holds
judge THE EVIDENCE THAT CERTIFIED NOTHING NOW CERTIFIES SOMETHING. `_run`
      copies the project's pyproject.toml into every tree, so `-ra` is in
      effect and the layouts can produce the defect they were written for.
judge AND THE REACH SENTENCE THAT CAME WITH IT IS FALSE. R302.
```

- **R295 -- CLOSED, and the clause is met by a machine.** I ran the deletion rather than
  reading the section.

```
cmd  pytest tests/test_ci_canonical_environment.py -q
out  4 passed
cell the `OPENBLAS_CORETYPE: "Haswell"` line deleted from ci.yml, nothing else,
     the guards job body run whole:
out  3 failed, 551 passed
       test_the_workflow_pins_the_BLAS_kernel
       test_the_pin_is_set_once_for_EVERY_job
       test_the_plan_and_the_workflow_name_THE_SAME_kernel
judge MY OWN ABLATION GAVE `463 passed, 0 failed` TWICE. It now names three
      failures and one of them names the plan. The condition said "something in
      the suite goes red with OPENBLAS_CORETYPE removed -- shown as a run", and
      that is the run. CLOSED.
judge One residue, recordable: the third test raises `KeyError` at :92 rather
      than asserting, because `_workflow()["env"]` is subscripted before the
      key is known present. It fails, which is what matters; it fails without
      its message. R308.
```

- **R296 -- CLOSED at all three clauses.**

```
cmd  python scripts/carried_table.py docs/reviews/F2/step-5.md \
         docs/reports/F2/step-5-answers.json | diff against the report's S9
out  59 lines each, IDENTICAL. 57 rows. The command runs at this commit.
code the three rows, against verdict 32's own headings:
     R288 -> "answered at revision 7; the verdict ran the ablation" (R288's
             subject, and verdict 33 ruled R288 CLOSED)              CORRECT
     R289 -> "carried into R297" (R289's subject, ruled NOT CLOSED)  CORRECT
     R290 -> "carried into R298" (R290's subject, ruled NOT CLOSED)  CORRECT
cmd  the section reference in the paragraph beside the command
out  "the table in S9, verbatim" and the table is S9                 CORRECT
judge THE SHIFT IS GONE AND THE COMMAND IS RUNNABLE. Closed.
judge THE SENTENCE PUBLISHED FOR THE MECHANISM IS NOT MEASURED. R306.
```

- **R297 -- CLOSED, and the runner is a real detector. I ablated it three ways.**

```
cmd  pytest tests/test_report_vocabulary_corpus.py -q
out  23 passed, DISAGREEMENTS empty -- 22 corpus entries, all 22 agreeing
cell `_plain` reverted to the markup-only strip, nothing else:
out  3 failed -- soft_hyphen, html_comment, html_entity. Exactly the three.
cell `_ROW` reverted to the old anchor, nothing else:
out  2 failed -- indented_row, item_cell_written_R_space_230. Exactly the two.
cell "no longer open" deleted from VERDICT_ONLY, nothing else:
out  1 failed -- no_longer_open_as_the_whole_status. Exactly the one.
judge THE RUNNER BINDS TO THE REPAIRS, not to the fact that a file exists.
      Three rounds of "answered" with no runner are over.
judge THE COUNT BESIDE IT IS WRONG BY ONE. R305.
```

- **R298 -- CLOSED IN SUBSTANCE, third round, and its published command is stale.**
  The sentence is written, in the report, where the condition asked for it. The `cmd/out`
  triple beside it prints something else at this commit, and part of that is my fault --
  my condition named `:312`, which was the line before the workflow grew by 85 lines at
  `1be5606`.

```
code the report S5: "`.github/workflows/ci.yml:312` carries ..." and
     cmd grep -n "rung6" .github/workflows/ci.yml
     out 312:  run: sh scripts/run_rung.sh empty:...rung6 full:tests/regression
cmd  grep -n "rung6" .github/workflows/ci.yml            (at 55498f4)
out  381:  rung6:
     397:      - run: sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
cmd  ls -a tests/verification/rung6
out  .  ..  .empty-by-design  __init__.py      (the report's `out` omits the
     fourth entry)
judge THE SUBSTANCE IS RIGHT AND I HAVE NOW VERIFIED IT FOUR TIMES: the rung is
      declared `empty:`, carries its marker, and `tests/regression` is declared
      `full:` in the same invocation. The item is CLOSED.
judge THE TRIPLE IS NOT A RUN. BF0 says the command carries the check; a
      command whose published output is not what it prints is worse than no
      command, because a reader stops there. Re-take it. R305.
```

- **R299 -- CLOSED.** `python -m pytest tests/test_report_carried.py -q` at `55498f4`
  gives **231 passed**, which is what S6 publishes, measured at the report's own commit.

- **R300 -- OPEN, correctly recorded at 4a**, and one of its named sites moved:
  `tests/test_report_guard_states.py:105-108` lost the
  `answers_header_names_an_older_verdict_commit` entry at `55498f4`, and the whole file is
  `22 passed`. The removal is in the right direction -- the state now reports rather than
  needing a declared exception -- but the diagnosis entry that cannot see a third failure
  is untouched. Still 4a.

- **R301 -- CLOSED.** `test_the_Carried_table_is_what_the_generator_produces` executes the
  script and compares; `test_the_generator_would_catch_a_row_under_the_wrong_number` is a
  real ablation and I ran it. The generator is no longer a comment.

- **R231, R244, R245, R275, R230, R223, R224 -- OPEN by instruction, correctly listed.**
  Site by site, confirmed untouched: `floatfea/tolerances.py:293`, `:295-297`, `:300-308`;
  `tests/verification/rung1/test_rigid_body_modes.py`; `docs/milestones/F2.md`. **R275,
  R231, R244 and R245 still wait on R293's open half**, which is the right dependency.

- **R261 -- OPEN, correctly.** No Q8 value was written.

- **R291, R292 -- OPEN, recordable at 4a, correctly recorded.**

- **R281 -- OPEN and grown by two.** Of the eleven corpus files, five now have a runner
  (`report_status_vocabulary.txt` gained one this round, which is R297).
  `ci_determinism.txt` and `carried_row_subject.txt` still have none, and both carry
  entries this round that nothing will read. I record that against myself as much as
  anyone.

- **R253, R254, R256, R257, R262, R263, R264, R265, R266, R267, R268, R269, R270, R271,
  R272, R273, R274, R276, R277, the two R248 residues, R249, R250, R251, R252, R225-R228,
  R232, R233** -- carried. R271's runner clause is now met (R297); R272's shape is met at
  the rule (R294) and reopened one level down at R302.

## Findings

**R302. (BLOCKS -- the ladder's own gate) The gate reads pytest's record instead of
pytest's output, which is right, and a rung's own `conftest.py` can write that record. A
genuinely red rung reports `run_rung: OK`, exit 0, through the same hook the repair itself
uses -- and three of the four channels are outside the reach the script states.**
`scripts/rung_no_xpass.py:21-22`; `scripts/run_rung.sh:148-157`;
`docs/reports/F2/step-5.md`, section 2.

```
code rung_no_xpass.py:21  "A test cannot write another test's report element,
                           so there is nothing to forge."
code run_rung.sh:152      "What is still outside the gate is anything that can
                           write the junit file itself: a conftest replacing
                           --junit-xml through addopts, a plugin implementing
                           pytest_sessionfinish to rewrite the XML, or a rung
                           run with -p no:junitxml. Those are edits to the
                           harness rather than to a test."
cell four rung trees, each with the project's pyproject.toml, the shipped
     script, one conftest.py inside the rung directory, nothing else:
out  pytest_runtest_makereport hookwrapper, rep.outcome = passed on a failing
     call report; the rung's only test asserts False
       -> run_rung: 1 collected, 0 failed, 0 errored, 0 skipped
       -> run_rung: OK -- 1 director(y|ies) ran        EXIT 0    MISSED
     pytest_ignore_collect returning True for test_bad.py, test_ok.py left
       -> run_rung: 1 collected, 0 failed;  OK          EXIT 0    MISSED
     pytest_collection_modifyitems dropping only the failing item
       -> run_rung: 1 collected, 0 failed;  OK          EXIT 0    MISSED
     pytest_sessionfinish parsing config.option.xmlpath, removing every
     failure element, writing it back
       -> run_rung: 1 collected, 0 failed;  OK          EXIT 0    MISSED,
                                                        and DECLARED
cell the two controls, same harness:
out  a conftest deselecting EVERY item -> run_rung: FAIL, "collects nothing"
     an xfail marker on a test that genuinely fails -> run_rung: FAIL,
       "1 skipped ... never skip a test to get a green build"
```

```
judge THE FIRST ONE IS THE FINDING. `rung_no_xpass.py` works by mutating a
      report inside `pytest_runtest_makereport`; the sentence two lines above
      it says a test cannot do that. A rung conftest can, to every report, in
      the opposite direction, and the junit writer records what it is handed.
judge THE SECOND AND THIRD ARE A DIFFERENT CLASS AND WORSE. They forge nothing.
      They remove the failing test from the collection BEFORE anything records
      it, and nothing in this repository states how many tests a rung is
      supposed to contain -- which is the `.empty-by-design` argument, one
      level down. Assertion domain blindness: the collection the gate inspects
      cannot contain the failure.
judge A CONFTEST IS NOT THE HARNESS BY THIS ROUND'S OWN STANDARD. Scenario 2 of
      section 2 is a conftest `pytest_terminal_summary`, counted as a live
      attack and shut. The reach sentence cannot classify a conftest as a test
      when it is caught and as the harness when it is not.
judge WHAT I AM NOT SAYING. The migration to junit is the right move and it is
      the first repair here that survived my whole battery: four text channels
      are dead and stay dead. This is not "the fix lasted one round again". It
      is that the sentence written beside it enumerates producers instead of
      stating the property, which is the fifth time in this file's history.
cmd  tests/corpus/ci_ladder_gating.txt, the 7 entries added at 8de404a
```

**Closed when** neither the `makereport` wrapper nor the two collection channels reaches
exit 0 -- each shown as a run -- **or** the reach sentence at `run_rung.sh:148-157` and the
sentence at `rung_no_xpass.py:21-22` are rewritten to what is true: that everything the
gate reads is writable from a rung's own `conftest.py`, and that what protects a rung is
review of its conftest rather than the gate. Either answer is acceptable; the present pair
of sentences is not.

**R303. (BLOCKS -- R293's open half, and the Q8 tolerance basis) One of the nine differing
rows is not what the report says it is. `clean_worst_ratio` moves 7.3% between the two
renders while `clean_worst_entry` is BYTE-IDENTICAL on both -- no argmax flipped, and it is
the headroom quantity the gate is about.** `docs/reports/F2/step-5.md`, section 1;
`scripts/regen_figures.py:77-79`.

```
code the report S1: "detection_edge_at and clean_worst_ratio are a MINIMUM OVER
     A CORPUS: two entries 0.4% apart, and which one wins flips. The value
     beside a flipped argmin is a different entry's value, not the same number
     computed twice."
cmd  the two renders, the clean_worst rows
out  CI    | clean_worst_ratio | 0.2564x |
           | clean_worst_entry | ck_cleanmax_D18p8_tw0p499_aniso1e6 |
     repo  | clean_worst_ratio | 0.2765x |
           | clean_worst_entry | ck_cleanmax_D18p8_tw0p499_aniso1e6 |
judge SAME ENTRY. NO FLIP. 7.3%. It IS the same number computed twice, which is
      the thing the sentence says it is not. BG0: a causal sentence carries the
      cell that isolates it, and the cell is the adjacent line of the same file.
cmd  the full localisation, which the report stops one row short of
out  3 rows last-bit at 1e-14   rigid_body_mode_ratio, _subspace_loss,
                                _counter_loss
     1 row an argmin NAME       detection_edge_at
     4 rows DOWNSTREAM of it    detection_edge and the three counter_* rows,
                                all computed from that edge, all 0.4-0.5%
     1 row UNEXPLAINED          clean_worst_ratio, 7.3%, same entry
     every margin_* and boundary_* row IDENTICAL
judge SO IT IS NOT SCATTER. Eight of nine rows have a mechanism and one does
      not, and the one that does not is a MAXIMUM OVER STATES at a fixed entry
      (regen_figures.py:77), which can move its winner without moving
      clean_worst_entry. That is a one-loop cell and nobody ran it.
judge AND THIS IS WHY IT BLOCKS RATHER THAN BEING TIDINESS. Q8's declared local
      classes are "arithmetic only: exact" and "through sin, cos or a
      factorisation: <= 2 ULP of the channel's own amplitude". 7.3% is neither,
      and the row was classified out of the tolerance question by a sentence
      instead of by a measurement. The per-figure relative tolerance the next
      commit is supposed to write has to cover this row, and its basis is
      currently a cause that measurement refutes.
cmd  tests/corpus/ci_determinism.txt, entry
     determinism_clean_worst_ratio_moves_7_3_percent_at_an_IDENTICAL_winning_entry
```

**Closed when** the 7.3% row is localised -- which state wins on each machine, or what else
moves it -- and section 1's classification is rewritten from that measurement; and the
per-figure tolerance that lands with the render is sized against this row rather than
against the 0.4% ones.

**MY RULING ON THE QUESTION AT THE END OF SECTION 1, because you asked and because a
reviewer who will not rule leaves the step stuck.**

**The decision not to commit is a correct reading of Q8 and it is not an evasion.** Q8's
Sequence line puts "the platform-dependent drift tolerance and the four moving figures
measured on CI under this Q&A **before their values are written**" -- tolerance first and
values after is the plan's own order, not a detour around it. Refusing to write the
tolerance in the same commit as the render is `CLAUDE.md` applied correctly. And the argmin
residue is real: I checked, `detection_edge_at` is a corpus entry NAME, and a relative
tolerance on a value cannot express which name is admissible.

**Of the two shapes you offer, take the second, and one of the two is not really a
choice.** Shape 1 -- publish the value and drop the entry name -- destroys the location of
an extremum, which is the recorded guard "a residual destroys information; report sign and
location alongside a norm" applied to exactly this case. Shape 2 -- the render names every
entry within the declared tolerance of the extremum -- keeps the location, is stable under
a flip, and makes a change in the SET a loud finding rather than a silent one. Take it.

**And the stop is one step further back than it needs to be.** Two things in section 1's
own way are unblocked by the ruling and were not done. The environment stamp Q8 names as
the enforcing mechanism -- "a golden or figure whose stamp is not CI's pinned environment
fails the build, so no canonical file can be produced on a laptop again" -- is absent from
the committed file **and from the CI artifact**: `head -9` of the downloaded
`F2_figures.md` is a title, a provenance sentence and a table header, byte-identical to the
repository's. Committing that artifact today would land a canonical file that says nothing
about where it came from. And R303's row needs measuring whatever the ruling is. Neither
waits on me.

**R304. (BLOCKS -- R293's open half) The goldens now execute on ten CI legs and their
failure is fatal on none of them. `bad` is computed, written into `regression.txt`,
printed by the verdict job, and asserted nowhere -- while ladder 6, the job that does gate
them, is skipped behind a red ladder 4.** `.github/workflows/ci.yml:119-140`, `:172-201`.

```
code ci.yml:124  pytest tests/regression -q --junit-xml=leg/regression.xml || true
code ci.yml:133  bad = [c for c in cases if any(k.tag in ("failure","error") ...)]
code ci.yml:138  if not cases: sys.exit("zero cases collected ...")
judge THAT IS THE ONLY EXIT. A leg whose golden comparison fails is not one.
cell the shipped step body verbatim, over a leg/regression.xml recording four
     testcases of which three carry a failure element:
out  "4 collected, 3 failed" written to leg/regression.txt
     EXIT 0
code ci.yml:186-189  determinism_verdict reads regression.txt into a row and
     PRINTS it. It asserts on the hashes and on the core types. Not on this.
judge SO THE ROW "4 collected, 3 failed" WOULD APPEAR IN A GREEN JOB'S LOG, ten
      times, and the run would be green. The comparison against the committed
      file is continue-on-error for a good reason and this is a different
      value: how many goldens failed is not a report about staleness, it is the
      golden gate.
judge MY OWN CONDITION SAID "and tests/regression still executes", and it does
      -- I wrote the weaker clause and this is me saying so. The purpose was
      that the goldens be gated on the machine Q8 makes canonical for them, and
      at this commit they are gated nowhere: ladder 6 is skipped behind ladder
      4, which is red under Q8 and stays red until R293 lands.
judge IT IS ONE LINE. `if bad: sys.exit(...)`, or one assertion in the verdict
      job over the ten regression.txt rows.
cmd  tests/corpus/ci_determinism.txt, entry
     determinism_a_leg_whose_REGRESSION_RUNG_FAILS
```

**Closed when** a leg whose regression rung reports a non-zero failure count turns
something red -- the leg, or `determinism_verdict` -- shown as a run of the injected XML.

**R305. (BLOCKS -- head 3) Five published figures do not describe the repository. Each is
refuted by one command and each is a one-line fix.** `docs/reports/F2/step-5.md`, sections
1, 2, 4 and 5.

```
code S1  "the ten legs, measured on CI at this round's code commit 05133c4"
         and, three lines down, "cmd gh run view 34459537327 --log (the push
         run at the code commit)"
cmd  gh run view 34459537327 --json headSha
out  1be5606. The published table -- AMD 9V74 on legs 2,3,4,7,9, three CPU
     models -- is that run's. At 05133c4 (34460382184) the ten legs drew SIX
     models: AMD 7763, 9V74, 9V45; Intel 8573C, 8370C, 6973P-C. The label and
     the data name different commits, and the commit named has the STRONGER
     result. CG3 is the rule this round added: "a table for another commit is a
     measurement of another state."

code S1  "11 of 47 rows differ; the other 36 are identical"
cmd  the two files, newline-normalised, line by line
out  9 of 47 differ, 38 identical. The published table has 9 rows and is
     complete; the count above it is wrong by two, and the judge line's
     "3 round-off and 3 argmin" accounts for 6 of 9.

code S4  "23 passed -- 23 of 23 entries agree" and the Carried row "23 of 23
         entries agreeing"
cmd  the corpus, entries parsed
out  22. `23` is the pytest count with test_the_corpus_was_parsed in it, and
     that test exists so that a runner reading nothing cannot agree with
     everything. The runner's own docstring says twenty-two.

code S2  "THE MODULE-LEVEL PRINT IS NO LONGER CAUGHT ... The reviewer recorded
         that entry as closed under the old rule, so this is a behaviour change
         and I state it rather than let it read as a pass."
cmd  pytest tests/test_ci_ladder_gating.py -q -k MODULE_LEVEL
out  2 passed. The reviewer's entry is
     ci_rung_full_xpass_with_a_MODULE_LEVEL_print...; its layout carries an
     xpass as well as the print, so it still reddens, require=fail is still
     met, and REQUIREMENT_CHANGED still has exactly two members, neither of
     them this one. No behaviour change occurred on that entry. The report's
     row describes a different layout under the same name.

code S5  cmd grep -n "rung6" .github/workflows/ci.yml / out 312: ...
     and  cmd ls -a tests/verification/rung6 / out . .. .empty-by-design
cmd  both, at 55498f4
out  381: and 397:, not 312: -- the workflow grew 85 lines at 1be5606, and my
     own R298 condition named the stale number, so half of this one is mine
     .  ..  .empty-by-design  __init__.py
judge FIVE FIGURES, FIVE ONE-LINE FIXES, AND EVERY ONE WAS CORRECT WHEN IT WAS
      TAKEN OR IN A NEIGHBOURING FILE. That is BP0's whole subject: this
      repository re-takes nothing when the thing beneath it moves, and a green
      suite never says so. Three of the five point at a BETTER result than the
      one published, which is why they are worth a fix rather than an argument.
```

**Closed when** each of the five is re-taken at the report's own commit, or withdrawn.

**R306. (BLOCKS -- head 3) The site check is real and its reach is a fraction of the
sentence published for it. Seven of eight answered rows this round declare a site another
finding's block also names, and rotating three statuses among them prints the table.**
`scripts/carried_table.py:91-105`; `docs/reports/F2/step-5.md`, section 4.

```
code S4  "THE THREE SHIFTED ROWS OF LAST ROUND WOULD HAVE BEEN CAUGHT BY THIS,
         each of them, because each cited a site from a different block."
cmd  the sites verdict 32's four relevant blocks name
out  R287 -> check_carried.py, docs/reports/F2/step-5.md, regen_figures.py,
             run_rung.sh, write_verdict.py   (NOT carried_table.py -- the
             verdict's own words were "a generator that does not exist")
     R288 -> docs/reports/F2/step-5.md, tests/test_report_guard_states.py
     R289 -> CLAUDE.md, docs/reports/F2/step-5.md,
             tests/corpus/report_status_vocabulary.txt
     R290 -> CLAUDE.md, ci.yml, docs/reports/F2/step-5.md
judge docs/reports/F2/step-5.md IS IN ALL FOUR. A shifted row declaring it -- a
      legal declaration, and the one this round's R230, R283 and R299 rows use
      -- passes in all three cases. Whether the shift is caught depends on
      which of its block's sites the author writes down, and the author is the
      one who shifted them. The counterfactual is unmeasured.
cmd  over this round's own answers file, for each answered row with a block,
     how many OTHER blocks name its declared site
out  R293 .github/workflows/ci.yml   also R295, R298
     R295 .github/workflows/ci.yml   also R293, R298
     R298 .github/workflows/ci.yml   also R293, R295
     R296 scripts/carried_table.py   also R301
     R301 scripts/carried_table.py   also R296
     R294 scripts/run_rung.sh        also R298
     R299 docs/reports/F2/step-5.md  also all seven others
     R297 tests/corpus/report_status_vocabulary.txt   UNIQUE
     7 of 8.
cell the status text of R293, R295 and R298 rotated among themselves, each
     row's site left alone -- the exact defect of R296:
out  the generator PRINTS all 57 rows. No SystemExit.
     | R293 | **answered** -- S3: tests/test_ci_canonical_environment.py ... |
     | R295 | **answered** -- S5, the sentence, written |
     | R298 | **answered** in the half that is mine -- S1: the job measures ...|
judge AND THE COMPARISON TEST WOULD PASS TOO, because the report would carry
      the rotated table and the generator produces it.
judge SIXTEEN OF THE TWENTY-FOUR ROWS IN THE ANSWERS FILE ARE NOT CHECKED AT
      ALL -- check_sites continues past any item the CURRENT verdict gives no
      block, by design. R267's shift was across carried items. It would be
      invisible here.
judge NONE OF THIS MAKES THE CHECK BAD. It catches a real class, its ablation
      test is genuine, and R296 is closed. It makes the SENTENCE wrong, and the
      sentence is what a later reader will trust instead of re-measuring.
cmd  tests/corpus/carried_row_subject.txt, the 4 entries added at 8de404a
```

**Closed when** section 4's claim states the measured reach -- that the check discriminates
only where the declared site is unique to its block, with this round's 7 of 8 -- or the
check is strengthened so a rotation among same-site findings is refused.

**R307. (recordable, 4a) `determinism_verdict` never re-hashes the uploaded
`F2_figures.md`.** `.github/workflows/ci.yml:112-117`, `:172-201`. CG2's stated claim is
that "the bytes uploaded are the bytes ten legs agreed on"; the verdict job reads
`cpu.txt`, `coretype.txt`, `figures.sha256` and `regression.txt`, and never opens
`F2_figures.md`. I downloaded leg 1 of `34460382184` and the file does hash to
`2af0f7cb...`, so the claim HELD when measured -- which is existence, not provenance, and
provenance is what a file about to be committed as canonical needs. One line in the verdict
job closes it.

**R308. (recordable, 4a) `test_the_plan_and_the_workflow_name_THE_SAME_kernel` raises
`KeyError` where it means to assert.** `tests/test_ci_canonical_environment.py:92`.
`env = _workflow()["env"]` is subscripted before the key is known present, so with the
whole `env:` block removed the test errors instead of reporting. It goes red either way and
the first test carries the message, so this is cosmetic -- and it is the one place in that
file where the reach is stated better than it is enforced.

## Tolerances touched

**None by this diff. A tenth round.**

```
cmd  git diff 35e7ddc..55498f4 -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 35e7ddc..55498f4 -- floatfea tests/regression
     docs/milestones/F2_figures.md docs/milestones/F2.md
out  (empty) -- not one line of floatfea/, no golden, no figure, no plan
judge THE PATIENCE IS PAYING A THIRD TIME. EXEMPT_RESPONSE_DRIFT_ULP = 4.0 has
      had a red CI in front of it for ten rounds. Widened at round one it would
      have been widened to one vendor's number; at round eight, from a laptop
      render; and this round we learn that one of the nine rows the canonical
      render moves is 7.3% at a fixed entry with no mechanism attached to it.
      The number to write is still not knowable.
```

**The tolerance finding this round is R303**, and it is a basis rather than a value: the
row that the per-figure relative tolerance will have to cover is the one the report
classified out of the question with a cause that measurement refutes.

**My own instructions (item 4b).**

```
cmd  git diff 35e7ddc..55498f4 -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" 35e7ddc..55498f4 with per-commit file lists
out  1be5606  ci.yml, 4 scripts, 5 tests files  -- no docs/reviews/, no .claude/
     05133c4  ci.yml                            -- the same
     55498f4  the report, answers.json, 2 scripts, 2 tests -- the same
judge No commit touches both code and docs/reviews/. No commit touches .claude/
      or docs/SUPERVISOR.md at all, so the STOP-class condition is not in play.
      CLEAN. One note, not a finding: 55498f4 is messaged `docs:` and also
      changes tests/test_report_carried.py and removes a REQUIREMENT_CHANGED
      entry from tests/test_report_guard_states.py. Both changes are correct
      and both are declared in the message body; the subject line is not what
      they are.
```

**What held**, reproduced at my run rather than read: the ten legs leg by leg on two CI
runs, including six CPU models at `05133c4`; the uploaded artifact hashing to the value the
legs agreed on, downloaded and checked; the five rung scenarios rebuilt from scratch, five
of five; the `-p rung_no_xpass` ablation at 9 versus 8-of-9; the kernel-pin deletion naming
three failures where it named none twice; the vocabulary runner reddening under three
separate repair ablations; the generated Carried table byte-identical to the published one
over 59 lines; the generated CI section byte-identical to section 0; `231 passed` at this
commit; the rung-6 declaration and its marker; and `floatfea/` untouched for a tenth round.

**These did not**: the reach of the rung gate against a rung's own conftest (R302), the
cause published for the 7.3% row (R303), the goldens' failure being fatal anywhere (R304),
five published figures (R305), and the reach published for the site check (R306).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Five blocking items, and none of them is a
repeat of an unanswered gate -- **all seven of last round's blocking items were answered at
their own sites, five of them outright.** That has not happened before on this step.

1. **R302 -- the rung gate, against the rung's own tree.** Either the three collection and
   report channels stop reaching exit 0, shown as runs, or the two sentences that say they
   cannot are rewritten to what is true. This is the only one that touches a gate's
   assertion.
2. **R303 -- the 7.3% row, and my ruling is written above.** Localise
   `clean_worst_ratio`; rewrite section 1's classification from that measurement; take
   shape 2 for the argmin figures; and the environment stamp waits on none of it.
3. **R304 -- one line.** A leg whose regression rung fails turns something red.
4. **R305, R306 -- six sentences.** Five figures re-taken at this commit, and the site
   check's reach stated as measured.
5. **R231, R244, R245, R275, R230, R223, R224 -- unchanged and open by instruction**,
   still behind R293's open half.

**Not gates on step 5, into the next report's Carried section:** R307, R308, R300, R291,
R292, R281, the underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 26 new entries at `8de404a`, across four files, all unseen by
the implementer; every `measured=` field taken at `55498f4` -- or against CI runs
`34459537327` and `34460382184` -- before the `require=` beside it was written.**

**The coverage measurement, stated plainly: of my 26 new entries the shipped checks do what
the entry requires on 8.** Four of those eight are controls I wrote to prove the checks are
not vacuous, and all four behaved.

* `tests/corpus/ci_ladder_gating.txt` -- **+7 (46 -> 53), 3 correct**, and all three are
  controls. The four that get through are the conftest channels of R302. With the corpus
  applied the file gives **9 failed, 46 passed**: the seven new entries have no layout yet
  and `test_the_corpus_and_the_layouts_agree` names them, which is the runner working.
* `tests/corpus/ci_determinism.txt` -- **+6 (14 -> 20), 2 correct.** One is the CG1 control
  and it is the best result on this branch. Four are open: the fatal-nowhere regression
  rung, the un-rehashed artifact, the missing stamp on the CI render, and the 7.3% row.
  **This file still has no runner** and induces zero failures.
* `tests/corpus/report_status_vocabulary.txt` -- **+9 (22 -> 31), 2 correct.** The file
  finally has a runner and I ablated it three ways; seven new spellings get past the
  repaired guard, four of them by producing no status cell at all, which is the half of the
  pair that exists so that banning a word cannot become saying nothing.
* `tests/corpus/carried_row_subject.txt` -- **+4 (9 -> 13), 1 correct**, the control being
  the shipped ablation. **This file still has no runner.**

**Thirty-four consecutive rounds have found no element defect, and this round does not
either.** `git diff 35e7ddc..55498f4 -- floatfea` is empty for the tenth time.

**What is different about this round, said plainly, because it has not been true before.**
Every blocking item was answered where it was raised. The gate that had been repaired at
the string four times was repaired at the rule, and the ablation column beside it is real
-- I deleted the plugin and eight of nine layouts went red. A corpus that had sat unread
for three rounds got a runner that binds to the code rather than to the file's existence.
And a determinism job that had produced no usable measurement in two attempts produced one:
ten runners, six CPU models, two vendors, one hash, and an artifact I downloaded and hashed
myself.

**And the thing that gate bought is a number nobody has explained.** The canonical machine
and this one disagree by 7.3% on the worst clean entry's headroom, at the same entry, with
every neighbouring row identical. The report has a sentence for it and the sentence is
refuted by the line underneath it in the same file. That is not a criticism of the round --
the row is only visible BECAUSE the artifact was finally downloaded and compared. It is the
next measurement, and it is the one the tolerance will be written from.
