# Review — R2 step 1
Reviewed commit: e4e233c890d8f023f01f151e8f28d18d35af163e
**Reviewed commit: `e4e233c890d8f023f01f151e8f28d18d35af163e`.**
Verdict: HOLD
Scope: **R2 step 1, revision 1, judged at the tip `e4e233c890d8f023f01f151e8f28d18d35af163e`.**
Ruled under **FR1 as GJ5(b) narrows it for R2**: a finding blocks only if it can cause a
wrong tool output, a wrong published engineering number, or a wrong statement inside a
decision item addressed to Xabier -- and **for the one blocking finding I write the
silently wrong result it produces**, which is the test FR1 asks me to apply rather than a
courtesy. **One finding blocks. It is R1268 and it is in `floatfea/cli.py`, not in the
escalation.** Thirteen more do not: TWELVE ledger rows, each saying why the FR1 sentence
cannot be written for it, and ONE FF0 item in the gating apparatus, which is fixed in the
next commit rather than ledgered. **This is revision 1 of GJ5(a)'s three, so a HOLD costs one of them and
leaves two.** **GE3: `R835: unchanged, R2`. Not re-measured.**

**ITEM 1b -- THE HEADER NAMES THE NEWEST VERDICT, AND THAT IS THE ONE COMPARISON.** The
newest verdict is the first entry of `docs/reviews/R2/step-0.md`, committed by `ed5b859`,
`Reviewed commit: 8fe7fea`. The report's `Answers:` line names `ed5b859...` -- the VERDICT
commit -- and Â§11a derives the number 68 and says the sha is the half that decides. It is
the right sha, and 68 is the right number for the reason Â§11a gives: the file carries
ELEVEN `# Review` entries (`grep -c "^# Review"` is 11), the highest number mentioned
anywhere in it is 67, and the newest entry ANSWERS verdict 67's `R1256` and `R1261` -- so
the newest entry is one past 67.
```
cmd    grep -n "^Answers:" docs/reports/R2/step-1.md
out    3:Answers: verdict 68 @ ed5b859515fb54a0c00b851560bfdd0f221132e1
cmd    git log -1 --format=%H ed5b859 ; git log --oneline -1 ed5b859
out    ed5b859515fb54a0c00b851560bfdd0f221132e1
       ed5b859 review: R2 step 0 EQ0 FOLLOW-ON at 8fe7fea -- PASS, five ledger rows
judge  1b does not fire. The report answers the newest verdict and no earlier one.
```

**4 / 4b / 4c, each diffed separately against the newest verdict's commit `ed5b859`, and
every range below names `e4e233c` RATHER THAN `HEAD`** -- because my own two corpus commits
sit on my branch's HEAD, which is exactly the coincidence FV3 closed R1049 for: a range
anchored on `HEAD` is right only while the reviewer has committed nothing of its own.

`floatfea/tolerances.py` **0 lines**, so **nothing in "Tolerances touched" below is
inferred**; `.claude docs/SUPERVISOR.md` **0 lines, so NO STOP-CLASS FINDING ARISES**, and
I diffed it rather than treating the green guards as covering it, because nothing in the
suite reads those paths; `tests/conftest.py 'tests/**/conftest.py'` **0 lines**, and
`git ls-files` over that pathspec returns `tests/conftest.py` as it must -- no new
conftest, no new plugin, nothing under `tests/` that can rewrite a rung's own record, which
is the one channel no gate can close.
```
cmd    git diff ed5b859..e4e233c -- floatfea/tolerances.py | wc -l
out    0
cmd    git diff ed5b859..e4e233c -- .claude docs/SUPERVISOR.md | wc -l
out    0
cmd    git diff ed5b859..e4e233c -- tests/conftest.py 'tests/**/conftest.py' | wc -l
       git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    0   /   tests/conftest.py
cmd    git diff ed5b859..e4e233c | grep -cE '^[-+].*_COUNTER'
out    0        -- so EU1 does not arise, and I ran the adversarial case anyway (Corpus)
```
Tests: **MY OWN RUNS, in my own worktree and in two detached probe worktrees at the judged
sha, `-p no:randomly`. I took no count from the report.** I ran the WHOLE TREE, in CI's own
four disjoint partitions rather than as one `pytest -q`, and the four union to the tree:
```
cmd    pytest tests/unit tests/verification/rung4 -q -p no:randomly
out    1 failed, 872 passed, 1 skipped in 172.06s
       the one is test_the_npz_is_NOT_STALE_against_the_code_that_generated_it
       -- and 528 passed / 1 skipped of it is `tests/unit`, which is CI's own count at
          `1df2298` TO THE ID
cmd    pytest tests/verification --ignore=tests/verification/rung4 -q -p no:randomly
out    1758 passed, 0 failed in 138.25s        (rungs 1, 2, 3 and 5; rung 6 COLLECTS
       NOTHING, which is by design -- CI runs it as `empty:tests/verification/rung6`)
cmd    each directory collected separately, so the partition is a measurement
out    rung1 1276 | rung2 66 | rung3 329 | rung4 345 | rung5 87 | rung6 0
       unit 529   | regression 481   | guards 1619   -- and 2103 + 529 + 481 + 1619
       is the tree
cmd    pytest tests --ignore=tests/unit --ignore=tests/verification --ignore=tests/regression -q
out    8 failed, 1611 passed in 759.35s        (CI's `guards and meta-tests` step)
cmd    pytest tests/regression -q -p no:randomly
out    IN FLIGHT WHEN THIS WAS WRITTEN -- about 396 of the 481 ids run, with
       EXACTLY ONE `F` in the progress so far. **I AM NOT PUBLISHING A COUNT FROM A PARTIAL
       RUN** (Â§A3's own rule, and it is the right one), so the measurement for this
       partition is CI's concluded one, below. Each F6-deliverable test spawns a real FE
       solve as a child -- `scripts/measure/member_forces_table.py`, read out of the
       process tree -- which is why it is the slow partition locally and why FV1 assigns
       the whole of `tests/regression` to CI at the pushed sha
judge  AND THE SAME PARTITION, MEASURED BY CI AT `1df2298`, AGREES: the ladder's rung-6
       step reports `481 collected, 1 failed` with the id `test_R756...`. That run covers
       the judged tree for this partition, which I checked rather than assumed --
       `git diff --name-only 1df2298..e4e233c` is `docs/reports/R2/step-1.md` and
       `scripts/ci_section.py`, and `grep -rln "docs/reports\|ci_section" tests/regression`
       finds one file whose two matches are both PROSE mentions of "the step-1 gate". So
       no regression test reads either changed path.
cmd    the eight, by name
out    test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
       test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
                                                               [non_numeric_step_suffix]
                                                               [superscript_digit_step_number]
                                                               [draft_suffix_beside_a_step_report]
                                                               [step_number_is_the_empty_string]
                                                               [verdict_amended_after_the_commit_the_report_answers]
                                                               [zero_padded_step_number]
```
**WHOLE TREE: 9 failed and 4241 passed and 1 skipped across THREE partitions I ran to
completion, plus CI's concluded `481 collected, 1 failed` for the fourth = **TEN FAILED,
4721 PASSED, 1 SKIPPED, 4732 COLLECTED**. My own run of the fourth partition was at about
396 of 481 with one `F` when this was written, which agrees with CI and is
not published as a count.**

**EVERY RED TRACED PER ID (EG3 (i)), AGAINST THE FS1/FT1 PREDICATE, NEVER BY FAMILY.**
```
cmd    each of the seven planted states run ALONE, for its INNER failure
out    THREE of them read out in full (baseline, zero_padded_step_number,
       verdict_amended_after_the_commit_the_report_answers):
         `AssertionError: step 1 has a report and no verdict yet. That is the legitimate
          boundary -- the verdict is written after the report is committed`
         and one inner `FAILED tests/test_report_carried.py::
         test_the_guard_reads_the_step_being_worked_on`
       the other FOUR (non_numeric_step_suffix, superscript_digit_step_number,
       draft_suffix_beside_a_step_report, step_number_is_the_empty_string), counted for
       that same assertion string: 1, 1, 1, 1
       and all seven report `1 failed, 635 passed` -- ONE inner red each
cell   SEVEN SEPARATE RUNS, one id each. I did not rule them as a cascade: the
       eighty-third verdict's eighth planted state was a real defect (R629), which is why
       EG3 (i) demands the individual trace, and the report's own Â§9 makes the same point
       and then measures it the same way.
judge  **EIGHT BOUNDARY REDS, EG3 STATE (1), cleared by this verdict commit.** Each names
       the step boundary itself -- a report with no verdict -- which is FS1's first limb.
       **AND TWO REDS ARE NOT BOUNDARY REDS AND I AM NOT RULING THEM AWAY**:
       `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` (rung 4) and
       `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`
       (tests/regression). Neither names a finding or a site of verdict 68 and neither's
       subject is the commit carrying it, so **CZ1 (iv) applies to both unchanged and both
       are blocking reds** -- and both are ALREADY on the record as blocking, as R1225's
       family and as R1223, open and escalated to Xabier under FQ3 since before `8fe7fea`.
       Carried by name below. **The report's Â§9 enumerates NINE and the tree has TEN**: it
       omits `test_R756...`, which its own generated Â§0 names. The omission hides nothing
       -- R1223 is carried in Â§7 and in Â§11 -- so it is a ledger row (R1280) and not more.
```

CI: **THE JUDGED COMMIT HAS NO RUN, AND THAT IS RECORDED AS UNAVAILABLE RATHER THAN SKIPPED
OVER (CK2's third state is NOT what this is, and nor is CA2's red).**
```
cmd    gh run list --commit e4e233c890d8f023f01f151e8f28d18d35af163e --json name,conclusion,
       workflowName,status,databaseId                              (THE FULL 40, GF3 d)
out    []
cmd    git diff --name-only 1e8975b..e4e233c
out    docs/reports/R2/step-1.md          -- paths-ignored by ci.yml, so no run is possible
cmd    gh api .../runs/44470087130  (the nearest ancestor WITH a run, `1e8975b`)
out    status in_progress, conclusion null
judge  **GC2's condition on the diff listing is MET and its evidence is NOT YET AVAILABLE**:
       the judged commit is report-only, so FP1 is satisfied by the concluded run at its
       nearest ancestor that has one -- and that run has not concluded. A run that has not
       finished is not a pass and is not a failure. **NOT CK2**: every job in this series
       was given a runner and steps, 13 and 14 of them, not the two-second no-runner shape,
       so the allowance is not exhausted. **NOT A RED AT THE JUDGED COMMIT**, so CA2's
       automatic HOLD does not fire. I record it as what it is: unavailable.
```
**AND THE NEAREST CONCLUDED RUN IS TWO COMMITS BACK AND IT DESCRIBES THE JUDGED TREE, WHICH
I MEASURED RATHER THAN ASSUMED.**
```
cmd    gh api .../runs/44469942995  (at `1df2298`)   and   git diff --name-only 1df2298..e4e233c
out    completed, conclusion failure
       docs/reports/R2/step-1.md ; scripts/ci_section.py
cmd    git show 1e8975b -- scripts/ci_section.py
out    the only code change between that run and the judged tip is ONE PRINTED SENTENCE
       inside the skipped-step block -- a false clause about what a skip means, which the
       implementer found by RUNNING the generator. No gate, no threshold, no number.
cmd    the job and step conclusions at `1df2298`
out    lint, unit and guards     failure  -- 5 actionlint success | 6 ruff success
                                             7 black success | 8 mypy success
                                             9 unit tests SUCCESS | 10 guards FAILURE
       the verification ladder   failure  -- rungs 1,2,3 success | rung 6 FAILURE
                                             rung 4 FAILURE | rung 5 SUCCESS
       CI determinism (both)     skipped  -- workflow_dispatch only: UNAVAILABLE, not green
cmd    every run_rung verdict and every failing id in the ladder log
out    run_rung: OK x4, FAIL x2;  1276/0, 329/0, 87/0, 66/0, 345/1, 481/1
       failure  tests.verification.rung4.test_f4_g41_dynamic::test_the_npz_is_NOT_STALE...
       failure  tests.regression.test_f6_deliverable_agrees_with_itself::test_R756...
cmd    the guards step's 13 reds, each read from the log
out    the eight boundary ids above, plus test_the_report_carries_a_CI_SECTION,
       test_the_reported_CI_counts_are_not_all_zero,
       test_the_CI_section_is_about_the_REVIEWED_commit,
       test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph  (all four the
       absent CI section, which `4db742d` then added), and
       test_the_answered_verdict_is_the_NEWEST_one (the `Answers:` sha, which `1e8975b`
       then fixed -- a REAL defect, found and repaired inside the step)
judge  **EVERY CONCLUDED RED IN THIS SERIES IS EITHER THE ESCALATION, A BOUNDARY RED, OR
       WAS FIXED IN THE NEXT COMMIT UNDER FF0 -- and I checked the FF0 one rather than
       taking it.** `2a7ded8`'s `unit tests: failure` was
       `test_the_record_carries_the_path_and_the_lock_hash_GJ1_asks_for` asserting
       `endswith(("python.exe", "python"))`, which is a guess about an interpreter's NAME
       and false on a runner ending `/bin/python3`; `1df2298` replaced it with
       `== str(Path(sys.executable).resolve())`, which mentions no platform, and `unit
       tests` is SUCCESS there. That is FF0 applied correctly and promptly, and it is the
       first thing R1243's repair made visible.
```

Door (FV2 / GG2): `git worktree add -b review/e4e233c890d8 <a path outside the repository>
e4e233c890d8f023f01f151e8f28d18d35af163e` **succeeded on the first try**, which is the
detector, and I checked both sides of it before trusting that: `git branch --list
'review/e4e233c*'` returns only the branch I just made and `git ls-remote --heads origin
'refs/heads/review/e4e233c*'` is empty, so **no review of this commit already exists**. I
worked in that worktree and in two DETACHED probe worktrees at the same sha, so every
working-file read in this verdict is a read of the commit. **I wrote nothing into
`C:\dev\floatfea`'s working tree**: `git status --short` there was empty when I was invoked
and is empty now, every file I wrote is in my own worktree or under the scratchpad, and the
only things I touched in the shared repository are refs and `.git/worktrees` metadata --
`worktree add`, which is what the FV2 procedure prescribes. **No `checkout`, no `reset`, no
write of any kind in the implementer's working tree.** One stop-process: I killed MY OWN
whole-tree `pytest` in MY OWN worktree, by pid, after confirming its command line named my
worktree -- and that run is the reason `## Carried` carries a correction about buffered
progress dots rather than a figure.

This verdict is written through `scripts/write_verdict.py`, which commits nothing
(`grep -nE '"(commit|add)"|check_call|\.run\(' scripts/write_verdict.py` is empty),
committed on `review/e4e233c890d8` and pushed -- merge with
`git merge --ff-only origin/review/e4e233c890d8`, **which WILL fast-forward because I
judged the tip.** **The corpus is committed separately, at the two commits BEFORE this
verdict** (`fa688d3` and `efcfb20`), which is the order `require-verdict.sh` excludes
`tests/corpus/` for.
## Carried

Verdict 68 left **one blocking item carried in by GJ4 (R1243)**, **two open and escalated
(R1223, R1225)**, **five ledger rows it had just written (R1263-R1267)** and the long routed
list. **R1243 IS ANSWERED AND I HAVE CI EVIDENCE FOR BOTH HALVES OF IT THAT THE REPORT DID
NOT HAVE. R1223 and R1225 ARE OPEN, ESCALATED AND NOT CLEARED BY THIS VERDICT. ALL FIVE
LEDGER ROWS ARE UNANSWERED, WHICH IS CORRECT UNDER `CLAUDE.md`** -- they are fixed once in
the step's closure commit and are not re-reviewed item by item -- **and I list them under
`## Closure items` rather than holding on one.**

* **R1243 -- ANSWERED, AND THE CONFIRMATION IS A CI RUN THAT CONCLUDED AFTER THE REPORT WAS
  WRITTEN.** Â§8 had the lint half only; the ladder had not concluded anywhere in this
  series when the report was pasted, so it could not show the half R1243's own words are
  about. It has now concluded at `1df2298`, which differs from the judged tip by the report
  and one printed sentence in `ci_section.py`:
```
cmd    gh api repos/:owner/:repo/actions/runs/44469942995/jobs --jq
       '.jobs[]|select(.name|test("ladder"))|.steps[]|"\(.number) \(.name) -> \(.conclusion)"'
out    5 ladder 1 -- the solver is a solver      -> success
       6 ladder 2 -- the element is the element  -> success
       7 ladder 3 -- the model is the platform   -> success
       8 ladder 6 -- it stays fixed              -> FAILURE
       9 ladder 4 -- the loads are the loads     -> FAILURE   <== IT RAN
      10 ladder 5 -- independent confirmation    -> success   <== IT RAN
cmd    the same api on the lint job at 2a7ded8 (run 44468004759)
out    9 unit tests -> failure   |   10 guards and meta-tests -> SUCCESS   <== IT RAN
cell   ONE VARIABLE against the previous reviewed commit: at `8fe7fea`, run
       44222328359, the same ladder read `8 ladder 6 -> failure`, `9 ladder 4 ->
       SKIPPED`, `10 ladder 5 -> SKIPPED`. The repair is the only thing between them.
rule   R1243's repair condition as `docs/closure/R2-step0.md` states it -- "stop the
       chaining: separate jobs, or `if: always()` per step, with a CI section that names
       skipped STEPS"
judge  **Both jobs, measured on a machine neither of us controls.** And it immediately
       bought what the un-chaining is for: rung 4 had been red and UNRUN in CI, so
       `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` -- part of the
       escalation, red since before `8fe7fea` -- was invisible to every CI run that
       reported "one red". Rung 5, independent confirmation, ran for the first time in
       this series and is 87 collected, 0 failed. The third part of the condition is done
       too and carries one defect of its own, R1276, which is FF0's and not a ledger row.
```
* **R1223 and R1225 -- OPEN, ESCALATED, AND THE ESCALATION HAS GENUINELY MOVED. I AM NOT
  RULING THE TWO REDS AWAY.** Â§1 is the best thing in this report. Under the FS1/FT1
  predicate neither red is a boundary red -- neither names a finding or a site of verdict
  68 and neither's subject is the commit carrying it -- so CZ1 (iv) applies to both and
  **they are blocking reds.** They are also **already recorded as blocking and already
  escalated**: `test_R756...` is R1223 and `test_the_npz_is_NOT_STALE...` is the R1225
  family, both red at `8fe7fea` and at every commit since the escalation opened, and
  verdict 65 recorded the second one by name. **Nothing in this diff caused either and
  nothing in this diff could clear either**: the only in-loop repair is the one FQ3 forbids
  in advance, and the implementer has now declined it for an eighth round. **I verified the
  declining rather than taking it:**
```
cmd    sha256sum data/f4/dynamic_inputs.npz   ;   git log --oneline -1 -- that path
out    dea555d933fb9fd088213896f9ad38fd891f71dd8fab1d8381aa47fa57797f86
       62a8281 R1 step 1 revision 3: the floor removed, the scale recorded ...
judge  Byte-for-byte Â§1's pasted hash, and the newest commit touching the golden is from
       R1 step 1 -- so nothing in R2 step 1 re-based it, and nothing in R2 step 0 did
       either. FQ3 honoured, measured.
```
  A HOLD on them would mean "answer these first", and nobody in this loop may. **The HOLD in
  this verdict is R1268's and it is answerable; these two stay on Xabier's desk.**
* **R1225's PUBLISHED DIAGNOSIS IS CORRECTED IN THE SOURCE TREE AND THE CORRECTION IS
  RIGHT.** The comment in `scripts/export_f4_dynamic_inputs.py` said "One variable moved";
  it now names two and says what pinning buys. I checked the arithmetic of the replacement
  rather than the prose: E -> F moves the five thread variables alone (6 differing arrays
  -> 0) and F -> G moves the numpy patch alone (0 -> 6), so "the committed file needs numpy
  2.4.0 AND an unfixed thread count, together" is exactly what two single-variable cells
  support. The one over-reach in the replacement is R1272 and it is a ledger row.
* **R1263 -- NOT ANSWERED. The figure verdict 68 named is still wrong and so is the stray
  `**`.**
```
cmd    grep -cE "^\*\*R[0-9]+\.? \(BLOCKS\)" docs/reviews/R2/step-0.md     (judged commit)
out    13
cmd    sed -n '438,444p' docs/closure/R2-step0.md
out    "produced **TWELVE findings carrying the `(BLOCKS)` marker** ... is 12, counted
       rather than recalled" , and ":443  without re-running the count.**"
cmd    git diff ed5b859..e4e233c --stat -- docs/closure
out    (empty)
judge  Correctly carried rather than quietly dropped -- Â§7 and Â§11 name it -- and under
       `CLAUDE.md` it belongs in this step's CLOSURE COMMIT, not in a round. Listed below.
```
* **R1264 -- NOT ANSWERED, AND IT IS THE ONE VERDICT 68 ASKED FOR FIRST.** "The one I would
  spend step 1's first ten minutes on." `grep -c "def test_FK2" tests/test_report_carried.py`
  is **5** at both commits and `git diff ed5b859..e4e233c -- tests/test_report_carried.py` is
  **empty**, so the two rows are not written and `scripts/check_carried.py` is still
  exercised by no test in this repository. **Closure item, not a HOLD** -- `CLAUDE.md` is
  explicit that the list is fixed once and not re-reviewed item by item, and I am applying
  that rather than re-arguing it. I will say only that it is the row whose absence cost the
  four preceding rounds their repairs-of-repairs, and that it is two lines.
* **R1265, R1266, R1267 -- NOT ANSWERED.** `_carrier` still has no milestone-level arm; the
  heading at `docs/closure/R2-step0.md:410` still precedes the three-row generator table
  while the six-row table sits at `:475`; `_SUITE` is still `.search` over the whole block.
  All three in the closure commit.
* **R1232 -- ANSWERED FOR THE CHILD, AND THAT IS A REAL ADVANCE.** R1232 is that
  `pin_threads()` cannot be wired above a process's own numpy import. `_child_env` assigns
  all five of `determinism.THREAD_ENV` in the environment of a process that has not started
  yet, which is the one place the pins land before any import. I verified the five
  assignments and the `setdefault` on the kernel; the kernel half is R1278.
* **R1248 -- open, step 2, correctly.** `scripts/export_buoy_centers_ref.py` is not in this
  diff and the export path does not use it.
* **CZ1 (ii)'s owed `pytest -q` at `5901738` -- STILL OWED, AND Â§A3's ACCOUNT IS HONEST AND
  I AM NOT CHARGING IT TO THIS ROUND.** Â§A3 reports a run stopped at 8% and refuses to
  publish a partial count, which is the right call: "I am not reporting a partial run as a
  count" is the sentence a report should contain when that is what happened. It also records
  the one thing the attempt did establish (the worktree is clean at the sha). **One
  correction to the reason given, from my own measurement**: Â§A3 and Â§9 both attribute the
  cost to guards that "each spawn a WHOLE NESTED SUITE", and the guards section is **759
  seconds** end to end on this machine -- `12:39`, not hours. My own whole-tree run looked
  stalled at 4% for twenty minutes and was not:
```
cmd    python -c "import sys; print('line_buffering', sys.stdout.line_buffering,
       'isatty', sys.stdout.isatty())"  > a file
out    line_buffering False isatty False
judge  so `pytest -q`'s progress dots are BLOCK-buffered when the output is redirected,
       which is how a run this long is actually taken. That is the same defect Â§6 records
       about `_cmd_export`'s banner, one tool over, and it is what made two of my own runs
       and probably two of Â§A3's look stalled when they were working.
```
  **The owed run is affordable.** It goes in the closure commit as
  Â§A3 says.
* **`docs/reports/R2/step-0.md:1616` and `:1629` -- declare-only under EK3, and Â§10 records
  them as `no change`.** Correct: `git diff ed5b859..e4e233c -- docs/reports/R2/step-0.md` is
  empty, so EK3 is not breached.
* **R1247 -- reviewer-side, unchanged.** Verdict 65's `Closes:` still routes the FC1 guards;
  this verdict carries no `Closes:` line, as FK1 requires of a verdict that closes nothing.
* **R1212, R1217, R1218, R1222, R1224, R1234, R1242, R1254, R1255, and verdict 58's
  fourteen (R1186, R1188, R1189, R1190, R1191, R1193, R1196, R1197, R1198, R1199, R1200,
  R1201, R1203, R1204) -- carried as routed, none a step-1 matter, and Â§11's generated table
  is the per-item record.** R1218 becomes blocking when step 2 writes the tolerance entry.
  **R835 -- `unchanged, R2` (GE3), one line, not re-measured.**
* **Â§10 IS THE BEST PIECE OF BOOKKEEPING IN THIS REPORT AND I CHECKED IT RATHER THAN
  TRUSTING IT.** Every test name the report cites exists, and every path citation resolves
  except six, of which five are cross-repo or future-dated and the sixth is
  `scripts/untouched_sites_v2.py` -- which verdict 68's own text names, as a file that does
  not exist, so the table is faithfully echoing the verdict rather than inventing a path.
```
cmd    every `test_[A-Za-z0-9_]+` token in the report, against the collected suite
out    39 cited; 39 found; 0 phantoms
cmd    every backticked path-shaped token, against `git ls-files` with a bare-name fallback
out    106 distinct; 100 resolve; 6 do not -- HSP-runs/requirements-lock.txt,
       requirements-lock.txt, HSP-stable/studies/platform-12buoy/platform_common.py
       (all three cross-repo), docs/closure/R2-step1.md (not written yet),
       tmp_run_exported.yaml (the measurement's scratch file), and
       scripts/untouched_sites_v2.py (verdict 68's own phantom, quoted)
```
## Findings

**ONE BLOCKS. It is not in the escalation and it is not in the apparatus; it is in
`floatfea/cli.py`, on the command this step exists to build.** Twelve ledger rows and one
FF0 item follow it, and for each ledger row I say why the FR1 sentence cannot be written.

**R1268. (BLOCKS -- FR1's second head, and GJ5(b)'s "a wrong tool output") `floatfea export`
READS ONLY `T` OUT OF EACH DECLARED CASE. THE DECLARED WAVE HEIGHT IS PARSED,
RANGE-CHECKED AND THEN NEVER READ, AND THE ENGINE SOLVES AT A HARD-CODED SEA STATE.**

**The silently wrong result it produces, stated as FR1 requires.** A user who declares
`H: 40.0` in an export configuration -- any value in `WAVE_HEIGHT`'s `[0, 100]` domain
other than `24.2`, and `0.0` is admitted too -- gets a dynamic-inputs file computed at the engine's own `0.484 m`
model-scale design wave, `24.2 m` full scale. Nothing refuses, and the command's banner
prints the worktree, the interpreter, the heading and the periods and **not the height**.
Every member force, stress and utilisation `floatfea run` then publishes from that file is
for a sea state **39.5% smaller** than the one the configuration declares
(`24.2 / 40.0 = 0.605`, computed rather than rounded), and the only trace
is `run.wave_height_full_m` in the sidecar, which a reader has to compare by hand against a
configuration they wrote. That is the unconservative direction and it is the failure mode
`CLAUDE.md` opens with: *"A structure analysed under misinterpreted loads is the failure
mode this whole project is built to prevent."*

```
claim  the argv the engine is handed is IDENTICAL for H = 24.2 and H = 12.0
cmd    the shipped export configuration with `H: 24.2` -> `H: 12.0` on all six cases and
       nothing else, `cli._covered_headings` -> `(0.0,)`, `floatsim_env.interpreter`
       substituted, `subprocess.run` SPIED, in a detached worktree at the judged sha
out    H=24.2: exit 0; engine INVOKED; argv = [... --dt 0.01 --out <dir>
               --period 10.0 --period 12.5 --period 14.0 --period 15.0
               --period 16.2 --period 20.0]
       H=12.0: exit 0; engine INVOKED; argv = THE SAME BYTES
cell   ONE VARIABLE, the declared height. Same configuration, same substitutions, same
       spy; `git status --porcelain` empty before and after, the scratch config removed.
cmd    grep -rn "WAVE_HEIGHT_MODEL_M\|WAVE_HEADING_DEG" --include=*.py . |
         grep -v report_joint_reactions.py
out    scripts/export_f4_dynamic_inputs.py:817  "heading_deg": float(rjr.WAVE_HEADING_DEG)
       scripts/export_f4_dynamic_inputs.py:818  "wave_height_model_m": float(rjr.WAVE_HEIGHT_MODEL_M)
       scripts/export_f4_dynamic_inputs.py:819  "wave_height_full_m": ... * float(g41.LAMBDA)
       -- the three uses are all in the PROVENANCE WRITER. Nothing compares either
          constant with anything the configuration declared.
cmd    grep -c "\.height_m\|height_m=" floatfea/cli.py scripts/export_f4_dynamic_inputs.py
out    floatfea/cli.py:0  ;  scripts/export_f4_dynamic_inputs.py:0
       -- NEITHER the command NOR the engine ever reads the attribute. The needle is on
          `.height_m` and `height_m=` rather than on the word "height", which matches
          two prose lines in `cli.py` about the RECORDED basis and would have read as 2
cmd    the two fields `_cmd_export` DOES read out of `cfg.load_cases.cases`
out    `{c.heading_deg for c in ...}`  and  `{c.period_s for c in ...}`.  That is all.
rule   FR1's second head -- "an input accepted and used other than as declared"; and
       `floatfea export`'s OWN refusal for the heading, immediately above, which makes
       exactly this argument for exactly this reason: *"`export` runs the cases and labels
       the file with the heading, so the two cannot disagree -- one of them would be a
       false label on a published file."*
judge  The argument the command already makes for the heading is the argument for the
       height, and the height is the field with no reader. `T` IS honoured -- the argv
       carries one `--period` per distinct declared period -- so a user has every reason
       to believe the case block parametrises the run, and for two of its three fields it
       does not.
```

**AND THE SCHEMA'S OWN DOCSTRING SAYS WHAT A CASE IS, WHICH IS WHY THIS IS NOT A QUESTION
OF INTERPRETATION.** `floatfea/run/config.py`: `LoadCases` is *"Either committed npz files
of dynamic inputs, **or the FloatSim runs to produce them**"*, and `WaveCase` is *"One
regular wave: heading, height, period. Full scale, SI."* So a case IS a declaration of a run
to make, in three fields, at full scale -- and one of the three is discarded. There is no
reading of those two sentences under which `H` is decoration.

**AND THE SHIPPED CONFIGURATION'S OWN COMMENT STATES THE REQUIREMENT THE CODE DOES NOT
ENFORCE**, which is the second half of it. `examples/platform12_export.yaml`:
*"`periods_full_s` ... is `[10, 12.5, ...]` and `run.heading_deg` in its provenance sidecar
is `0.0`; `H = 24.2 m` full scale is `run.wave_height_full_m`. **Those three fields are
what this block has to agree with** for `--check` to be a meaningful comparison."* Three
fields named; two are checked (periods by being passed through, heading by the covered-set
query plus the two-key cross-check) and the third is not checked at all.

**AND THE REPAIR HAS TWO PRECEDENTS IN THIS REPOSITORY, BOTH EXACT AND BOTH REFUSING, WHICH
IS WHAT TAKES THIS PAST A JUDGEMENT CALL.** The recorded basis of a dynamic-inputs file is
four fields -- `heading_deg`, `wave_height_full_m`, `wave_height_model_m`, `lambda` -- and
three of the four already have a declared-versus-actual check somewhere:
```
cmd    grep -n "froude_lambda" floatfea/run/pipeline.py
out    766  exported, where = exported_froude_lambda(npz)
       775  if exported != cfg.floatsim.froude_lambda:
       777      "scale mismatch. floatsim.froude_lambda = ... in <the config> ..."
       783      "... larger/smaller by a factor of N, which is N**3 x on every force"
cmd    the heading's equivalent, same file
out    703-716  each file's RECORDED heading against `load_cases.headings`, modulo 360,
                refusing by name and naming every missing heading
cmd    the wave height's equivalent, anywhere
out    `RECORDED_BOUNDS["wave_height_full_m"] = WAVE_HEIGHT`, a DOMAIN check (R881), and
       `_recorded_height` for the EZ2 band -- and nothing that compares it with a declared
       value, on either side
rule   `pipeline.py`'s own Î» refusal is the pattern: the file's recorded value against the
       configuration's declared value, EXACT, refusing, with the consequence spelled out
judge  `lambda` is protected at run time, `heading_deg` is protected at run time and
       (between the two config keys) at export time, and `wave_height_full_m` is protected
       nowhere. On the run side that is defensible -- `cases` may not be declared beside
       `npz:`, so there is no declared height to compare -- which is precisely why the
       check belongs at EXPORT time, where the declared height exists and is discarded.
```

**Three more cells on the same axis, measured, because the shape is wider than one field.**
```
out    two cases at ONE period with different H (T = 20 s at 24.2 and at 11.0)
         -> SEVEN declared cases become SIX `--period` flags. One declared case produces
            nothing and nothing says so: `periods` is a set over `period_s` alone, so two
            cases that differ only in a field nobody reads are one case
       H = 0.0, the domain's lower edge          -> accepted, exported at 24.2 m
       H = 99.0, just inside the ceiling         -> accepted, exported at 24.2 m
       and the heading half of the same shape, unreachable TODAY and only by accident:
         `headings: [45.0]` with cases at 45 deg, against a BEM database covering
         [0.0, 45.0], passes BOTH config checks and the engine still solves at
         `WAVE_HEADING_DEG = 0.0`. It is unreachable because the pinned database is
         single-heading, which is a property of the dataset and not of the code
cell   one candidate per cell, same harness, same substitutions
```

***Closed when*** `floatfea export` refuses unless every declared case's `H` is the height
the engine will actually solve at and write -- which is the engine's own expression,
`float(rjr.WAVE_HEIGHT_MODEL_M) * float(g41.LAMBDA)` at
`scripts/export_f4_dynamic_inputs.py:819`, taken from there rather than copied -- or the
height is passed to the engine so the declaration is honoured; **and** the same comparison is made
for `heading_deg` against `WAVE_HEADING_DEG`, so the heading does not depend on the dataset
happening to carry one entry; **and** two cases that differ in any field the export reads
are not collapsed, or are refused by name. **With a test row per direction** -- the
engine's own height proceeds, any other height refuses -- in
`tests/unit/test_cli_export_refusals.py`, which exists and is therefore not new apparatus.
The refusal for the two heading keys is the shape to copy; it is sixteen lines away.

**AND THE CHEAPEST HALF OF THE REPAIR IS ALREADY WRITTEN FOR THE PERIODS, IN A TEST THAT
PARSES THE SAME LINES.** `tests/regression/test_export_config_matches_the_placeholder.py::
test_the_export_config_declares_the_SIX_PERIODS_THE_NPZ_CARRIES` reads every
`- {heading: ..., H: ..., T: ...}` line, extracts `T`, and compares the set against
`periods_full_s` INSIDE the committed npz -- "not against a list retyped here" -- and its
docstring makes the argument for me: *"a period moved ... would refuse after 26 minutes,
and this refuses in milliseconds."* The same loop already has `H` in hand on the same line,
and the committed sidecar carries `run.wave_height_full_m`. **One more assertion in that
test holds the SHIPPED configuration; the refusal in `_cmd_export` is what holds a user's
own. The blocking condition is the refusal -- the regression row is the ten-second
companion.** That file is also the model for the rest of this: it carries its own vacuity
control (`test_the_SHARED_SET_IS_NOT_EMPTY_AND_NAMES_THE_BLOCKS_IT_HOLDS`) and an inverted
half, which is the standard the new refusal rows should meet.

**AND THE COMPARISON IS EXACT, WITH NO TOLERANCE, WHICH I CHECKED BEFORE ASKING FOR IT** --
because a check that needed an epsilon would be a tolerance, and a tolerance introduced to
make two numbers agree is what `CLAUDE.md` calls a fudge factor:
```
cmd    python -c "h=0.484; lam=50.0; print(repr(h*lam), h*lam==24.2)"
out    24.2 True          -- and 24.2/50.0 == 0.484 is True as well
judge  The shipped configuration's `H: 24.2` and the engine's `0.484 * 50.0` are the SAME
       double, so `==` admits the shipped file and refuses everything else. The heading
       check beside it is exact for the same reason and says so: "a heading is a declared
       input". No entry in `tolerances.py` is needed or wanted here.

**THE TWELVE LEDGER ROWS AND THE ONE FF0 ITEM, each with its command and its closing
condition. None of them can
be given FR1's sentence, and I say the reason in one line rather than a paragraph.**

**R1269. (ledger) THE R1243 GUARD'S NEW ASSERTION IS SATISFIED BY A CONDITION THAT DISABLES
THE RUNG: IT TESTS THAT EACH RUNG'S `if:` CONTAINS THE SUBSTRING `cancelled()`, NOT THAT NO
RUNG GATES ANY OTHER -- AND THE WEAKENING DIRECTION WAS NOT MEASURED.**
```
claim  Â§8: "the guard asserts the un-chaining rather than a proxy for it, and it inverts"
cmd    ladder 5's `if: ${{ !cancelled() && steps.deps.outcome == 'success' }}` replaced by
       `if: ${{ cancelled() }}` -- the rung then runs ONLY in a cancelled run, i.e. never
       -- then pytest tests/test_ci_determinism_gate.py tests/test_ci_workflow_is_wellformed.py
out    BASELINE (the three CI guard files)   85 passed
       the mutation                          21 passed, 0 failed     <== GREEN
       restored, git status --porcelain       (clean)
cell   ONE VARIABLE, ladder 5's `if:` expression; nothing else in the workflow moved.
rule   the assertion itself: `[... if "cancelled()" not in str(s.get("if", ""))]`, a
       substring test, so any expression carrying the token passes -- including the
       negation of the intended one, and including one gated on another rung's outcome
judge  Â§8's inversion DELETED the `if:`, which is the strengthening direction; EH4 asks for
       both, and the weakening boundary is a condition that keeps the token and changes the
       meaning. The positional assertion beside it still passes, so the file is not without
       content -- what over-reaches is "carries the property this test is named for".
```
*Not blocking:* a rung that does not run is named by `ci_section.py`'s skipped-step line, so
no wrong number follows. ***Closed when*** the assertion compares each rung's `if:` against
the condition the job uses, or checks that it names no step id but `deps`, with the mutation
above as its counter-case.

**R1270. (ledger) THE REFUSAL TO OVERWRITE A COMMITTED GOLDEN FIRES AFTER THE
TWENTY-SIX-MINUTE SOLVE -- IN THE STEP THAT MAKES "THE REFUSAL IS TIMED, NOT JUST PRESENT"
A PRINCIPLE.**
```
cmd    scripts/export_f4_dynamic_inputs.py main(), in source order
out    cases = [export_case(p, args.dt) for p in periods]        <- the six solves
       ... then: if not args.check and not args.allow_regenerate and _is_tracked(...)
rule   Â§4 on the heading refusal -- "a heading check that fired after the solve would charge
       most of an hour for a typo" -- and
       test_the_heading_refusal_fires_BEFORE_the_engine_is_invoked
judge  Same command, same 26 minutes, and this is the branch the SHIPPED configuration hits:
       `outputs.directory` is the committed location by design, so
       `floatfea export examples/platform12_export.yaml` with no flag is 26 minutes and
       then a refusal. The write is correctly never reached.
```
*Not blocking:* the refusal is right and the golden is untouched. ***Closed when*** the
`_is_tracked` question precedes `export_case`, with a row asserting the engine is not
invoked.

**R1271. (ledger) `--check`'s REFUSAL SAYS "is not committed" WHERE THE QUESTION IT ASKED IS
`.exists()`, SO AN UNTRACKED FILE IS COMPARED AGAINST AND CALLED COMMITTED.**
```
out    if not npz_path.exists():
           print(f"  REFUSED: {npz_path} is not committed; nothing to compare")
judge  The engine HAS `_is_tracked` and does not use it here. With `--out <scratch>` and a
       previous export sitting there, `--check` reports a bit-exact verdict against an
       untracked file as though against the golden.
```
*Not blocking:* FR1's first named class -- the outcome is right, the message is not.
***Closed when*** the message says `does not exist`, or the branch asks `_is_tracked`.

**R1272. (ledger) CELL H MOVES NUMPY AND SCIPY TOGETHER, SO "PINNING BUYS AGREEMENT ACROSS A
NUMPY PATCH RELEASE AND NOT ACROSS A MINOR ONE" IS A TWO-VARIABLE CELL READ AS ONE.**
```
claim  Â§1: "numpy 2.5.4 PINNED differs from all three. Pinning buys agreement across a
       numpy PATCH release and not across a minor one"
cmd    the report's own Â§A2 table, cells A and H; and grep -niE "^(numpy|scipy)" constraints-dev.txt
out    A   numpy 2.4.4 / scipy 1.17.1  pinned   accel 8.774756e-14
       H   numpy 2.5.4 / scipy 1.18.1  pinned   accel 6.367170e-14
       constraints-dev.txt:  numpy==2.5.4 ; scipy==1.18.1    -- BOTH pins moved
rule   BG0 -- a causal sentence carries the cell that isolates it
judge  The conclusion the decision rests on survives and is the conservative one: pinning
       does not make the comparison version-independent, whichever library moved it. What
       is unmeasured is that NUMPY's minor release is the mover -- scipy is in the solve
       path too, and `determinism.py`'s own SuperLU note is about a scipy version. E -> F
       and F -> G are each one variable and correctly labelled, which is what makes the one
       two-variable cell worth naming.
```
*Not blocking:* no wrong number, and no option's cost changes. ***Closed when*** the
sentence says "a library minor release", or a cell at numpy 2.5.4 with scipy held at 1.17.1
exists.

**R1273. (ledger, and the one I came closest to blocking on) "THE DIFFERENCE DOES NOT REACH A
PUBLISHED NUMBER" IS MEASURED ON THE GOVERNING UTILISATION AND WRITTEN OVER EVERY PUBLISHED
NUMBER -- IN THE DECISION ITEM AND AGAIN IN THE DIGEST.**
```
claim  Â§1's one-screen row and option 1's cost column ("nothing a reader sees"), and the
       same sentence in docs/digests/2026-11-18.md
cmd    what Â§A4 actually compares
out    sha256 of both npz; np.array_equal over 100 arrays (64 exact, 36 differ, worst
       1.109519e-09 on case0/resid_control); and ONE line of `floatfea run` -- the
       governing U, member, station, period and clause
judge  That run also published 1248 member-force rows and 32 checked stations, and
       `CLAUDE.md` requires the equilibrium residual PER CASE -- `resid_control` being the
       array that differs most. None of those was compared. The claim is very probably
       true at published precision and I do not assert it is false; it is a generalisation
       from one line to a directory, inside the paragraph Xabier is asked to rule on, and
       the measurement is a byte-diff of two output directories Â§A4 already had in hand.
```
*Not blocking:* I cannot write FR1's sentence -- no number is wrong, and the number anybody
sizes steel against IS measured and does hold. ***Closed when*** the sentence is scoped to
the governing utilisation, member, station, period and clause, or the two output directories
are diffed and the result pasted.

**R1274. (ledger) `tests/unit/test_export_sensitivity_note.py` IS TEN IDS AND IS PUBLISHED AS
NINE, SO "52 new rows" IS 53 AND THE `62 passed` DECOMPOSITION ADDS UP ONLY BECAUSE OF THE
ERROR. THIRD WRONG SELF-COUNT IN THIS REPORT, AND IT RECORDS THE OTHER TWO.**
```
cmd    python -m pytest tests/unit/test_export_sensitivity_note.py --collect-only -q |
         grep -c "::"                                     (the report's OWN command)
out    10          -- the report's Â§6 table and Â§2 decomposition both say 9
cmd    the five files of Â§2, collected, then run
out    23 + 16 + 4 + 10 + 10 = 63 collected ; 62 passed, 1 skipped in 0.95s
rule   CP3 -- the figure is pasted from the run that produced the artifact
judge  Two errors that cancel: "16 + 23 + 4 + 9 + 10" sums to 62 and the run says
       `62 passed`, so the line READS consistent -- but 63 are collected and the missing
       one is a SKIP in a different file (`test_floatsim_env.py:113`), which the `out` line
       does not mention. New rows are 53. The report already records `57` and `78` as
       earlier self-count corrections in this same step; this is the third.
```
*Not blocking:* report prose, GJ5(b)'s own ledger class, and no gate reads either figure --
`test_report_numbers_are_sourced.py` is satisfied because the 9 sits in its own section's
command block, which is that guard's documented limit. ***Closed when*** the row reads 10,
the two totals read 53, and the `out` line names the skip.

**R1275. (ledger) THE R1219 REGRESSION TEST SKIPS WHEREVER THE LOCKED VENV IS NOT BUILT --
CI AND EVERY FRESH CLONE -- SO THE PROPERTY IT EXISTS FOR IS VERIFIED ON ONE MACHINE.**
```
out    tests/unit/test_floatsim_env.py:106-114
         monkeypatch.setenv(fse.VENV_ENV, ".venv-floatsim"); monkeypatch.chdir(tmp_path)
         if not (ROOT / fse.DEFAULT_VENV).is_dir(): pytest.skip(...)
cmd    the CI log at 1df2298, the `unit tests` step
out    SKIPPED [1] tests/unit/test_floatsim_env.py:113 ... ; 528 passed, 1 skipped
rule   "Empty parameter set is an error, not a skip" -- a check that cannot run where it
       matters certifies nothing there, and R1219 is a MEASURED defect (one declaration
       naming two worktrees depending on the cwd)
judge  Honest, and recorded by the implementer in `1df2298`'s own message rather than
       hidden. Also avoidable: the test two below it monkeypatches `fse._repo_root` to
       `tmp_path`, and the same move with a `.venv-floatsim` directory created there tests
       the anchoring rule with no real venv. `hsp_pin`'s equivalent needs no skip.
```
*Not blocking:* no wrong number, and the `require=True` refusal rows beside it do run.
***Closed when*** the test builds its own directory under `tmp_path` with `_repo_root`
pointed at it and the skip is deleted.

**R1276. (FF0 -- NOT A LEDGER ROW. It is in the gating apparatus, so it is fixed in the next
commit.) THE SKIPPED-STEP BLOCK COUNTS POST-RUN HOUSEKEEPING AS A CHECK, SO Â§0 PUBLISHES
"3 STEP(S) SKIPPED" OF WHICH ONE IS `Post Run actions/setup-python@v5`.**
```
claim  R1243's third part: "a CI section that names skipped STEPS"
out    Â§0, generated: "**3 STEP(S) SKIPPED inside a job that ran:** `ladder 4 ...`,
       `ladder 5 ...`, `the verification ladder / Post Run actions/setup-python@v5`"
cmd    the new comprehension in scripts/ci_section.py
out    if step.get("conclusion") == "skipped"       -- every step of every job, unfiltered
cmd    gh api .../jobs at 1df2298, both jobs
out    19 Post Run actions/setup-python@v5 -> skipped    (in EVERY job of EVERY run)
rule   FF0 -- anything that reads the gating record "is FIXED IN THE NEXT COMMIT", and
       `scripts/ci_section.py` is named in it; EK2 -- repaired or deleted, never extended
judge  Two of the three are R1243's defect; the third is skipped in every run of every job
       and says nothing, so the figure that answers R1243's repair condition is inflated by
       one per job, permanently. `1e8975b` fixed this block's SENTENCE after running it;
       the DOMAIN it counts over was not revisited. The fix is a filter, not a new check.
```

**R1277. (ledger) ONE PREDICATE, TWO RULES, SIXTEEN LINES APART: THE TWO-KEY HEADING CHECK
COMPARES EXACTLY WHILE THE COVERED-SET CHECK BESIDE IT IS MODULO 360 -- R1100's DEFECT ONE
READER OVER, IN THE LOUD DIRECTION.**
```
cmd    three cells, covered set (0.0,), one variable each
out    cases 360.0 / headings [0.0]   CAUGHT  "headings is [0.0] deg but the declared
                                               cases sit at [360.0] deg"
       both keys 360.0                GREEN   `uncovered_headings` calls 360 and 0 one
                                               heading, and the two keys agree exactly
       cases -0.0 / headings [0.0]    GREEN   `-0.0 == 0.0`, so the exact test passes
rule   R1100's ruling, quoted in pipeline.py: "the modulo is the correct rule and the
       duplicate was the defect: two checks of one question is the shape where one of them
       quietly stops being the one that runs"
judge  The new check is `sorted(set(...)) != sorted(set(...))` on raw degrees -- STRICTER
       than the modulo rule in every cell I measured, so it refuses where the other reader
       accepts and never the reverse. Loud, not silent, which is why it is not R1268's
       second half.
```
*Not blocking:* it refuses; nothing is published under it. ***Closed when*** the two-key
check asks `uncovered_headings` in both directions.

**R1278. (ledger) `_child_env`'s `setdefault` ON `OPENBLAS_CORETYPE` IS JUSTIFIED BY A CELL
IN WHICH `setdefault` AND ASSIGNMENT ARE THE SAME THING.**
```
claim  "`OPENBLAS_CORETYPE` is `setdefault` and the thread counts are assigned: CI sets the
       kernel deliberately for every job"
cmd    the value CI sets, against the default this code would assign
out    ci.yml  OPENBLAS_CORETYPE: Haswell   ;   determinism.CANONICAL_CORETYPE "Haswell"
rule   BG0 -- the cell that isolates the causal claim
judge  Same string, so on CI the two behaviours are indistinguishable and the reason given
       does not reach the only cell where they differ: an inherited kernel that is NOT
       canonical -- the state CF1 was adopted for, "an EPYC run produced a DIFFERENT file
       and PASSED". There `setdefault` lets the non-canonical value win in the child doing
       the bit-exact comparison. Small because the sidecar's `environment` block records
       `openblas_coretype` from `os.environ`, so the file says which kernel made it.
```
*Not blocking:* the file self-describes, so the result is not silent. ***Closed when*** the
justification names that cell and says which way it is decided, or the kernel is assigned
like the thread counts.

**R1279. (ledger) Â§A4's `U = 1.71167` WAS TAKEN FROM A RUN ON A FILE WITH NO PROVENANCE
SIDECAR, WHICH IS A DIFFERENT SCREENING PATH FROM THE ONE THE REPAIRED TOOL PRODUCES.**
```
claim  GI5 step 1's second half: "`floatfea run` gives U = 1.71167 -- HOLDS on the exported
       file too"
out    Â§A4's own block, in order: "export wall 26 min 39 s, exit 1" / "the PROVENANCE was
       never written" / "governing U = 1.71167 ..." / published "wave basis: NOT RECORDED"
rule   CP3 -- if an edit follows the paste, the paste is void
judge  With no sidecar there is no recorded height, and `pipeline`'s own comment says such
       a file has NO associated-period band -- so the EZ2 screening that decides which
       cases may govern ran in a mode a repaired export does not produce. The value is
       almost certainly unchanged (the golden with its sidecar gives it, and 64 arrays are
       bit-identical) and the report states both facts in the same block; what it does not
       say is that the acceptance figure was taken in the state the repair removed. I am
       not asking for a 26-minute re-run: step 2's zero-change test re-exports anyway.
```
*Not blocking:* the number is the golden's and the gate it answers is met. ***Closed when***
the block says which state the run was made in, or the figure is re-taken at step 2.

**R1280. (ledger -- FR1's own "a census, needle or grep that is too narrow where no wrong
result follows") Â§9's EG3 TRACE ENUMERATES NINE REDS AND THE TREE HAS TEN. THE TENTH IS
`test_R756...`, WHICH THE REPORT'S OWN GENERATED Â§0 NAMES.**
```
claim  Â§9: "THE EIGHT THAT REMAIN ARE ONE CAUSE ... THE NINTH RED IS NOT IN THAT SET"
cmd    the whole tree at the judged sha, in CI's four partitions -- three of them my own
       completed runs, the fourth CI's concluded one, exactly as the Tests block records
out    8 (boundary, mine) + 1 (rung 4, the staleness gate, mine)
       + 1 (tests/regression, R756, CI's at `1df2298` and 1 `F` in my own in-flight run)
       = TEN
cmd    the report's own Â§0, generated
out    "Failing tests named in the log: 1. - ...::test_R756_the_SHIPPED_report_IS_a_
       regeneration_of_the_current_tree"
cmd    the ladder at 1df2298, which concluded after the report was pasted
out    rung 4 FAILURE (the staleness gate) AND rung 6 FAILURE (R756) -- two, not one
rule   EG3 (i) -- the waiver is conditional on EVERY red tracing by name
judge  Â§9 scopes itself to the FV1 selection and says in terms that "the whole of
       `tests/regression` is CI's job at the pushed sha", so this is a scope the section
       states rather than a red it hides, and R1223 is carried by name in Â§7 and Â§11. What
       it means is that Â§9's trace is not a trace of the TREE -- and EG3 (i) exists because
       eight states were once ruled as one cascade and the eighth was real.
```
*Not blocking:* both reds are already on the record as blocking and escalated, in the same
report. ***Closed when*** Â§9's count is ten and `test_R756...` is in its list beside the
staleness gate.

**R1281. (ledger) `parse_lock` DROPS A LINE IT DOES NOT RECOGNISE, SILENTLY. THE ZERO CASE IS
GUARDED AND THE PARTIAL CASE IS NOT -- AND I MEASURED THAT TODAY'S LOCK LOSES NOTHING, WHICH
IS WHY THIS IS A ROW AND NOT A FINDING.**
```
claim  `refuse_unless_locked` compares every pin in the lock
cmd    floatsim_env.parse_lock / editables / _PIN over the real
       HSP-runs/requirements-lock.txt, counting lines that are none of pin, editable,
       comment or blank
out    lines 40  pins 39  editables 1  UNRECOGNISED 0
rule   the module's own guard -- "an empty lock would make this check pass on any
       environment at all, which is worse than no check" -- and `_PIN`, which is anchored
       `^name==version\s*$` with `[^\s;#]+` for the version, so a PEP 508 environment
       marker (`numpy==2.4.4 ; python_version < "3.14"`) matches neither `_PIN` nor
       `_EDITABLE` and is dropped with nothing printed
judge  Nothing is lost today: 39 + 1 = 40 and the plan's Â§7a `diff` of lock-minus-editable
       against `pip freeze` is empty, so the parse is complete. The shape is that the check
       guarding the FQ3 environment gets WEAKER, not louder, if HSP re-locks with markers
       -- and `record()["lock"]["pins"]` is the only trace, a number a reader would have to
       notice falling.
```
*Not blocking:* measured complete on the lock in use, so no wrong result is reachable today.
***Closed when*** a line that is neither pin, editable, comment nor blank raises, by the
same argument the zero-pin case already raises under.
## Closure items

Not re-reviewed item by item and not held on, per `CLAUDE.md`. **The implementer fixes the
whole list once, in step 1's closure commit.** R1263-R1267 are verdict 68's and are
unanswered; R1269-R1275 and R1277-R1281 are mine; R1276 is **not** on this list because
FF0 puts a defect in the gating apparatus in the next commit instead.

* **R1263** -- `docs/closure/R2-step0.md:440-441`, `TWELVE` where its own command returns
  `13`; and the stray `**` at `:443`. Fix with the commit that adds R1263-R1267 and this
  verdict's ids to the artifact's `Carried` table, which verdict 68 already asked for.
* **R1264** -- two rows in `tests/test_report_carried.py` beside the five `test_FK2`
  cases, so `cz1_record`'s and `_carrier`'s repaired branches are held by something.
  Verdict 68's first ask; still two lines.
* **R1265** -- `_carrier`'s missing milestone-level arm, or a `docs/SUPERVISOR.md` line
  saying `--closes <milestone>` is unused (a `process:` commit and Xabier's).
* **R1266** -- the heading at `docs/closure/R2-step0.md:410` moved above the six-row table
  at `:475`, or deleted.
* **R1267** -- `_SUITE` anchored to the last match or to a marked line.
* **R1269-R1275, R1277-R1281** -- each with its `Closed when` in `## Findings`.
* **CZ1 (ii)'s owed `pytest -q` at `5901738`**, per Â§A3, with nothing else running. My own
  measurement says the guards section is 759 s and the whole tree is well inside an hour.

## Tolerances touched

**None, measured rather than asserted.** `git diff ed5b859..e4e233c -- floatfea/tolerances.py`
is **0 lines** and `git diff ed5b859..e4e233c | grep -cE '^[-+].*_COUNTER'` is **0**, so
**EU1 does not arise** -- and I ran the adversarial case anyway, at thirteen configurations
of the export command's input that the diff did not choose, which is where R1268 came from.

**One tolerance-shaped thing is implicated and has not moved, and it is the one to watch.**
`--check`'s comparison is `np.array_equal` with no threshold, by Q8's rule, and Â§1's option
3 is explicitly *"retire the bit-exact comparison in favour of a declared tolerance"*. The
report costs that option as needing a written physical or numerical justification and names
`CLAUDE.md`'s prohibition on a tolerance in the same commit as the code it rescues. **I
agree with that costing and I will say the sharper thing: if the answer to the escalation
introduces a tolerance on that comparison, it is a widening and it is refused here.** The
golden either regenerates or it does not; a number that makes two files agree is the
definition of a fudge factor.

## Corpus

**One batch, 30 entries, all new, committed separately at the two commits BEFORE this
verdict** (`fa688d3`, and `efcfb20` which corrects one of my own lines --
`tests/corpus/export_config_fields_not_read.txt`). **The correction is worth naming because
it is my own BF0 failure in the same round in which I charge two to the report:** entry B3
said a pair "is REFUSED by `pipeline`'s signed-heading rule (FY1) on the run side", which I
had not run. FY1 refuses a signed RECORDED heading such as `-10.0`; `-0.0` is a different
cell, `HEADING`'s domain is `("deg", 0.0, 360.0)` and `-0.0 >= 0.0` is True, so the schema
admits it and nothing distinguishes it from `0.0` anywhere. The row now says what was
measured. GC3 left the pause expired,
so the batch is my own call under GA3's length target.

**13 of the 30 carry a measurement: 4 CAUGHT and 9 reach a GREEN tree** -- meaning the
engine was invoked with the declared configuration accepted. The axis is the one
`floatfea export` creates by construction and the one the implementer's own 16 refusal rows
do not sweep: the command builds the engine's argv out of the configuration, the argv
carries `--dt`, `--out`, `--period` and `--check` and nothing else, and the engine
hard-codes the sea state it solves at. So **every field of a declared case except `T` is a
candidate by construction**, and the two cross-checks the command does carry are between
two CONFIG KEYS rather than between a config key and the engine. **That measurement is
R1268.** Two cells are marked `reach=unmeasured` and excluded from the ratio because my own
substitution defeats the check they are about -- the operating point, stated, rather than a
ratio over cells of different kinds.

**And what I ran beside the batch, both halves of the recorded substitute, because both
produced something.** *A continuum grid over the parameter space a decision rule guards*:
the declared-height axis at five values and the declared-heading axis at four, times the
two config keys, which is R1268 and R1277. *A regeneration check on a published
deliverable*: every test name and every path citation in the report re-resolved at its own
commit (39 of 39 names, 100 of 106 paths, the six accounted for in `## Carried`), the five
export test files re-collected (which is R1274), the SR log re-counted (`82` lines,
highest id `SR-78` -- the report's figure, confirmed), and `pip download numpy==2.4.0`
re-run, which prints `Reason for being yanked: Backward compatibility bug` exactly as Â§1
says. **Â§1's load-bearing external fact is independently confirmed.**

**The inversion EH4 asks for, in the direction that WEAKENS a gate, is R1269** -- the
`cancelled()` substring mutation, which is green. The strengthening direction was the one
the report measured.

## Next step opens when

**STEP 1 STAYS OPEN. The condition is R1268 and nothing else.**

1. **R1268 is answered**: the declared sea state is compared with the one the engine will
   actually solve at, or is passed to it, with a test row per direction in
   `tests/unit/test_cli_export_refusals.py` -- the engine's own height proceeds, any other
   height refuses -- and the heading given the same treatment so it does not depend on the
   pinned database carrying one entry. **The refusal for the two heading keys is the shape
   and it is sixteen lines away from the gap**, and
   `test_the_export_config_declares_the_SIX_PERIODS_THE_NPZ_CARRIES` is the ten-second
   companion -- it already parses the `H` it discards. EH4: solve it in both directions,
   including the one that weakens it -- a configuration at the engine's height must still
   proceed, which is the control the new rows need.
2. **R1276 is fixed in the next commit** (FF0, not the closure commit): the skipped-STEP
   count stops including post-run actions.
3. **The closure list above is fixed once, in the closure commit**, and `R1263`'s figure
   and `R1264`'s two rows are in it. I am not re-reviewing them item by item.
4. **The two escalated reds stay red and stay named.** Do not clear
   `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` by regenerating the npz
   and do not clear `test_R756...` by regenerating the deliverable against a red gate. **An
   eighth round of declining the cheap wrong repair is still the strongest thing in this
   step's record, and Â§1 is what GJ1's successor ruling has to answer.**
5. **EG3 (ii), the half no verdict in R2 had measured until verdict 68 and now mine: the
   report-guard files are run AT THIS VERDICT'S COMMIT and the counts pasted in the next
   revision.** My prediction, so that it is a measurement and not a reassurance: the eight
   boundary reds above go to **zero** when this verdict lands, and
   `python scripts/check_carried.py` then refuses until step 1's report `Carried` section
   names **R1268-R1281**. That refusal is the state-(2) boundary red and it clears at the
   answering revision.
6. **The next revision's Â§9 enumerates TEN reds, not nine** (R1280: the whole-tree count
   is ten and `test_R756...` is the tenth). And the
   first concluded ladder run is now in hand -- `1df2298`, two reds across the whole
   ladder, both the escalation -- so the next CI section has a concluded ladder to point at
   for the first time in this series.

**GJ5(a): this is revision 1 of three. Two remain.** A HOLD here costs one round and buys a
refusal on the input that decides which sea state a published utilisation describes; the
twelve ledger rows cost one line each instead of a second one.

**Nothing here is a STOP and I considered it on the ladder.** Rungs 1, 2, 3 and 5 are
`1758 passed, 0 failed` in my own run, so no low rung is red; the locked plan is amended by
GJ and the amendment is in its own `plan:` commit; `.claude/` and `docs/SUPERVISOR.md` are
**0 lines**, so no STOP-class finding arises. The one red rung is rung 4, and it is the
escalation.

**And I disagree with nothing in the criterion.** FR1 as GJ5(b) narrows it did the work
again: fourteen findings, and the sentence "here is the silently wrong result this produces"
could be written for exactly one of them. That one is a wrong published engineering number
and it is worth the round; the other thirteen are single lines here instead of a second
revision. **GJ5(d) is also met and worth saying so**: the one-screen table at the top of
the report gave me the dispositions and every figure in it was measured in the section it
named. The one place that discipline slipped is R1273, where a sentence in that very table
is wider than the measurement behind it -- which is the cost of putting the conclusions
first, and is why it is the ledger row I came closest to blocking on.
