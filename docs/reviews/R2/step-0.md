# Review — R2 step 0
Reviewed commit: 5901738c3ace6884bf90a71c318e6c246b640ed8
**Reviewed commit: `5901738c3ace6884bf90a71c318e6c246b640ed8`.**
Verdict: HOLD
Scope: **the EQ0 REVIEW OF THE CLOSURE-COMMIT FOLLOW-ON `5901738`**, which answers verdict 66's two
blocking findings and changes two gates -- `tests/test_report_carried.py` and
`scripts/check_carried.py`. EQ0 puts it in scope because a gate moved; **EB4 makes it cost no
round**; **under DD1 step 0 remains CLOSED by verdict 65 (`Closes: R2/step-0`)**, and this HOLD is on
the follow-on commit and on nothing else. It closes nothing, so `--closes` is correctly absent (FK1).
Ruled under **FR1 with EZ0**: the one blocking finding is given the sentence FR1 asks for.
**GE3: `R835: unchanged, R2`. Not re-measured.**

**ITEM 1b.** `docs/reports/R2/step-0.md` is byte-identical to its final-verdict state and this is not
a report revision, so 1b does not fire. Stated rather than skipped.
```
cmd    git diff 0fb8c93 HEAD -- docs/reports/ | wc -l
out    0
cmd    sed -n '1516p' docs/reports/R2/step-0.md
out    Answers: verdict 64 @ a3a30d2      -- the header 1b passed on at 0fb8c93, sealed by EK3
```

**4 / 4b / 4c, each diffed separately against the previous verdict commit `492fc22`:**
`floatfea/tolerances.py` **0 lines**; `.claude docs/SUPERVISOR.md` **0 lines, so no STOP-class
finding**; `tests/conftest.py 'tests/**/conftest.py'` **0 lines**, and `git ls-files` over that
pathspec returns `tests/conftest.py` as it must -- no new conftest, no new plugin, nothing under
`tests/` that can rewrite a rung's own record. `git diff 492fc22..HEAD | grep -cE '^[-+].*_COUNTER'`
is **0**, so **EU1 does not arise**, and the whole diff is three paths: `docs/closure/R2-step0.md`,
`scripts/check_carried.py`, `tests/test_report_carried.py`.

Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`.**
* `tests/test_report_carried.py` + `test_report_numbers_are_sourced.py` +
  `test_report_guard_states.py` -> **489 passed, 0 failed in 157.22s.** **ALL TEN REDS OF THE
  PREVIOUS ROUND ARE GONE**, and 489 is 481 + the 8 that were red, to the id. 465 of those are your
  two-file figure and 24 the guard-state harness, which matches your `465 passed` exactly.
* `tests/test_ci_determinism_gate.py` + `test_ci_ladder_gating.py` + `test_ci_workflow_is_wellformed.py`
  + `test_ci_runs_the_whole_suite.py` + `rung3/test_closure_evidence_exists.py` +
  `test_collected_set_golden.py` + `test_tree_prose_consistent.py` + `test_no_tolerance_literals.py`
  + `test_one_gravity.py` -> **369 passed, 0 failed in 191.37s.**
* `tests/test_ci_determinism_gate.py` alone -> **13 passed**, your figure confirmed.
* `python scripts/check_carried.py` -> **exit 0**, `the step is CLOSED, so reading R2-step0.md` /
  `all 36 findings carried`. Verdict 66's `exit 1` is cleared.
* `ruff check floatfea tests` -> **All checks passed!**; `ruff check scripts` -> **All checks
  passed!**; `black --check floatfea tests` -> **129 files would be left unchanged**;
  `mypy floatfea` -> **Success: no issues found in 45 source files.**
* **WHAT I DID NOT RUN, SAID RATHER THAN IMPLIED: my own whole-suite `pytest -q` at this sha.** I
  declined it deliberately and the reason is CP3 on my own side: my corpus commit landed before this
  file, and this file changes a document three of the guards in such a run read, so a count taken
  across it would describe neither tree. What stands in for it is the concluded CI run at the judged
  commit's own sha, below, on a machine neither of us controls. **This is the one output of CZ1 (ii)
  still owed for `5901738`, and item 2 of "Next step opens when" says where it goes.**
CI: **THE JUDGED COMMIT HAS A CONCLUDED RUN. IT IS RED, AND IT HAS EXACTLY ONE RED, WHICH IS THE
ESCALATION. Under CA2 a red CI is a HOLD regardless of the local run, and this verdict is a HOLD --
but the single red is a carried, escalated, open blocking item recorded with its cause named, so it
is not an independent block on top of R1256.** I waited for the run rather than recording a pass from
one that had not finished; it ran 00:47:22Z to 01:38Z.
```
cmd    gh run list --commit 5901738c3ace6884bf90a71c318e6c246b640ed8 --json name,conclusion,
       workflowName,status,databaseId                                 (THE FULL 40, GF3 d)
out    [{"conclusion":"failure","databaseId":44210685970,"name":"CI","status":"completed",
         "workflowName":"CI"}]
cmd    gh api repos/:owner/:repo/actions/runs/44210685970/jobs --jq '.jobs[] |
       "\(.name) | \(.status) | \(.conclusion) | runner=[\(.runner_name)] | steps=\(.steps|length)"'
out    the verification ladder            | completed | failure | runner=[GitHub Actions 1000001938] | 13
       lint, unit and guards              | completed | SUCCESS | runner=[GitHub Actions 1000001939] | 14
       CI determinism -- leg              | completed | skipped | runner=[null] | 0
       CI determinism -- ten legs agree   | completed | skipped | runner=[null] | 0
```
**NOT CK2.** Both executing jobs were given runners, steps and work -- 13 and 14 steps, not the
two-second no-runner shape -- and the two determinism jobs are `skipped` by their own
`workflow_dispatch` condition, which is UNAVAILABLE and not passing, recorded as that rather than
counted as green.

**THE STEP LIST, WHICH IS THE MEASUREMENT CZ1 (iii) EXISTS FOR, AND THIS ROUND IT SAYS SOMETHING NEW.**
```
cmd    gh api .../44210685970/jobs --jq '.jobs[] | .name as $j | .steps[] |
       "\($j) :: \(.number) \(.name) -> \(.conclusion)"'
out    the verification ladder :: 5 ladder 1 -- the solver is a solver     -> success
                              :: 6 ladder 2 -- the element is the element -> success
                              :: 7 ladder 3 -- the model is the platform  -> success
                              :: 8 ladder 6 -- it stays fixed             -> FAILURE
                              :: 9 ladder 4 -- the loads are the loads    -> skipped
                              :: 10 ladder 5 -- independent confirmation  -> skipped
       lint, unit and guards  :: 5 actionlint -> success | 6 ruff -> success
                              :: 7 black --check -> success | 8 mypy -> success
                              :: 9 unit tests -> SUCCESS | 10 guards and meta-tests -> SUCCESS
cmd    gh run view 44210685970 --log | the two step totals
out    unit tests  480 passed in 154.70s   |  guards and meta-tests  1406 passed in 471.68s
```
**`guards and meta-tests` RAN and PASSED, which is the first time in this step it has.** It is seen
to have run rather than been skipped behind an earlier red step, which is the exact hiding CZ1 (iii)
was written for, and the arithmetic cross-checks the repair from CI's side rather than mine:
`ce5a84f`'s same step was **8 failed, 1398 passed**, and 1398 + 8 = **1406**. The eight cleared and
nothing else moved, measured on a machine neither of us controls -- a different operating system, a
different install -- which is what CA2 asks CI for and what my own `489 passed` could not establish
alone.

**EVERY RED TRACED PER ID (EG3 (i)) -- AND THERE IS ONE.**
```
cmd    gh run view 44210685970 --log | grep -iE "run_rung: *(OK|failure)|run_rung: [0-9]+ collected"
out    run_rung:  failure  tests.regression.test_f6_deliverable_agrees_with_itself::
                           test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
       1276 collected, 0 failed | 66 collected, 0 failed | 329 collected, 0 failed |
       477 collected, 1 failed                       -- 2148 collected, 1 failed across the ladder
```
`test_R756` is **R1223**, carried and escalated by verdicts 65 and 66 and by this one, red at this
commit and at every commit since the escalation opened, **with its cause named** rather than
classified. **I am not claiming a boundary state for it and it does not need one:** it is not a
step-boundary artefact, it is an open blocking finding that is red by design because the cheap wrong
repair -- regenerating the deliverable against a red gate -- has been correctly declined six rounds
running. It reaches no limb of the FS1/FT1 predicate and needs none; CZ1 (iv) is answered by the fact
that the red is a named, open, escalated item and not a new one. **Rung 4 did not execute, so the npz
staleness guard (R1225) did not run in CI**, which is R1239's second exit as the artifact records it
and R1243 carried, not a fresh fact.

**AND THE TWO SIDES AGREE, WHICH IS THE PART A SINGLE COUNT WOULD NOT HAVE GIVEN.** My own runs
produced **0 failed** over 489 + 369 + 13 ids; CI produced **0 failed** over 480 unit + 1406 guards +
1671 of the 2148 ladder ids, and **1 failed** in the 477 of `tests/regression`, which FV1 assigns to
CI and which I did not run locally. Neither list has a red the other lacks outside that one file, and
the one red in it is named.

Door (FV2 / GG2): `git worktree add -b review/5901738c3ace <a path outside the repository>
5901738c3ace6884bf90a71c318e6c246b640ed8` **succeeded on the first try, and
`git ls-remote --heads origin 'refs/heads/review/5901738*'` was empty, so no review of this commit
existed.** A second, DETACHED probe worktree at the same sha held every one of the twenty-seven
plants below, one variable at a time with a restore between, with `git status --porcelain` over `floatfea tests scripts .github` asserted empty inside the
harness before each measurement -- so a dirty tree would have aborted the run rather than
contaminated it. **And FV2 earned its keep this round rather than being hygiene:** one backgrounded
plant was interrupted mid-rename and left `docs/closure/R2-step0.md` DELETED in the probe tree. In a
shared checkout that is the `git checkout --` incident again, from my side of the loop.
`C:\dev\floatfea` was clean when I was invoked and I wrote nothing into it. This verdict is written
through `scripts/write_verdict.py`, which commits nothing
(`grep -nE '"(commit|add)"|check_call|\.run\(' scripts/write_verdict.py` is empty), committed on
`review/5901738c3ace` and pushed -- merge with `git merge --ff-only origin/review/5901738c3ace`.
**The corpus is committed separately, at the commit BEFORE this verdict**, which is the order
`require-verdict.sh` excludes `tests/corpus/` for.

## Carried

Verdict 66 and its addendum: two blocking findings, five ledger rows, and the carry list. **R1249 IS
CLOSED. R1250's CONDITION IS DISCHARGED -- I measured both of its directions myself -- AND THE
SIBLING CELL THE CONDITION DID NOT NAME IS OPEN AS R1256.** Three of the five ledger rows are
answered, one is half-answered, and two are routed to a place they are not in.

* **R1249 -- CLOSED, and I measured the replacement rather than reading it.** The five-row green
  table is gone and `<!-- cz1-closure-outputs -->` carries CZ1's record with its operating point in
  the heading (`at ce5a84f, the previous closure commit`). The ten reds are each a resolvable id on
  its own line, so the cascade-by-family collapse is gone too.
```
cmd    grep -c '^- \*\*failed\*\*' docs/closure/R2-step0.md
out    10     -- against the block's own `10 failed, 4456 passed`, which is the count your addendum
                 measured independently at ce5a84f
cmd    every `- **failed**` line in the artifact blanked, the step report left carrying its own
       two names, then the id that caught the collapse
out    1 failed    -- so the naming guard reads the record the COUNT came from, which is the
                      repair, confirmed from a direction your hand-back did not state
```
  **And the understatement you corrected is carried into the artifact correctly**: `:38-44` states
  that `468 + 24` was the COLLECTED ID COUNT published as a pass count -- green by construction --
  and keeps it apart from the ordinary staleness beside it. That is the sharper of the two defects and
  the artifact now says which is which.
* **R1250 -- THE CONDITION IS DISCHARGED. I RAN BOTH DIRECTIONS MYSELF AND DID NOT TAKE YOURS.**
```
cmd    six plants on the artifact, one at a time, against the three FC1 ids, in a detached probe
out    BASELINE (as shipped)                               3 passed
       A. block markers removed (artifact, no block)        2 failed, 1 skipped   <- the ""-branch
       B. whole-suite line deleted from the block           1 failed, 1 passed, 1 skipped
       E. one of the ten named ids removed                  1 failed
       C. sha replaced by `deadbee`, not a commit           3 passed    (DR0's recorded loss)
       F. passed 4456 -> 101, just over the `>100` floor    3 passed    (the floor, as written)
cmd    five plants on the ANCHORED `Closes:` line, against `scripts/check_carried.py`
out    Closes: R2/step-00   routes to R2-step0.md, exit 0   -- `int()` normalises, correct
       Closes: R2/step0     routes to R2-step0.md, exit 0   -- `step-?`, correct
       Closes: R2           CLOSURE=R2.md, absent, reads the report, exit 1
       Closes: R2/step-9    CLOSURE=R2-step9.md, absent, reads the report, exit 1
       no Closes: at all    reads the report, exit 1        -- the OPEN-step behaviour, unchanged
```
  The state the condition named reddens, the state it named as the pass routes to the artifact, and
  the mid-step behaviour is untouched. **A warning about my first attempt, because it is this step's
  own defect on my side:** my first plant replaced the first `Closes: R2/step-0` in the file, which is
  a PROSE mention inside verdict 66's body, and every cell came back green and meaningless. The
  anchored `(?m)^Closes: R2/step-0\r?$` is what the router reads, and the file is CRLF. A needle that
  could not see what it was looking for, in the measurement of a finding about needles that cannot
  see what they are looking for.
* **R1243 -- unchanged, and it is step 1's.** No workflow path is in this diff, the restored order is
  still green (13 passed), and **R1243 appears by name in step 1's `Carried` and stays blocking
  there.**
* **R1223 / R1225 -- OPEN, ESCALATED, UNCHANGED, CORRECTLY.** No `data/` or `results/` path is in
  this diff. **Sixth round in which the cheap wrong repair was available and not taken.** This is
  still the best thing in the step's record and it is what GI6 sends to Xabier.
* **R1244 -- answered; nothing further owed.** The rounds table is left as it shipped and the
  correction is in the artifact at `:298-303`.
* **R1245 -- MOVED TO THE ARTIFACT AND THE CORRECTION IS RIGHT. The paragraph around it is not, and
  that is R1259.** I re-derived the figure rather than accepting it:
```
cmd    python -c "import sys;sys.path.insert(0,'tests');import test_report_carried as t;
       print(len(t.EXPECTED), 'R1219' in t.EXPECTED,
             [i for i in ('R1212','R1217','R1218','R1224') if i in t.EXPECTED])"
out    35 False ['R1212', 'R1217', 'R1218', 'R1224']
judge  FOUR items, not five. The artifact's `:195-200` is correct to the id.
```
* **R1246 -- MOVED TO THE ARTIFACT, and this one's history IS what the artifact says.** Measured,
  because it is the clause R1259 is about: `git show e71ecd5:docs/reports/R2/step-0.md | grep -c
  "generated: scripts/untouched_sites"` is **1**, and at the judged commit it is **0**. So R1246's
  repair did exist in the file at `e71ecd5` and the EK3 restore did revert it.
* **The EK3 collision is recorded as the reusable part, and it is the right reading.**
  `docs/closure/R2-step0.md:210-217` states it as a collision between two instructions rather than as
  a complaint, and `:1616` / `:1629` are named declare-only. I agree; I created those two sites, and
  step 1's report recording them `**no change** -- EK3` is the one answer still available.
* **R1251 -- HALF-ANSWERED. R1257.** `:283` now says TWENTY-FIVE; `:371-372` still says eight.
* **R1252 -- ANSWERED, and the arithmetic now resolves.** Measured:
```
cmd    grep -c "^# Review" docs/reviews/R2/step-0.md, plus the per-entry census of kinds
out    9 entries = 3 reviewed revisions (4c19570, e87b2c0, 0fb8c93) + 4 interim ENTRIES over 3
       distinct interim commits (9e1092a, 3d24e1c x2, 91c2d2e) + 2 EQ0 entries at ce5a84f
cmd    grep -oE "R1[0-9]{3}\. \(BLOCKS\)" docs/reviews/R2/step-0.md | sort -u | wc -l
out    12   -- and 12 minus R1249 and R1250, which are the two EQ0 entries', is the artifact's TEN
judge  `:5-8`'s "six ... three interim checks plus three reviewed revisions" and `:358`'s "ten
       findings carrying the blocking marker" are both right, and `:358` carries the scope sentence
       that makes TEN right rather than TWELVE. Both figures hold.
```
* **R1253 -- ANSWERED, and I re-derived the table independently rather than checking the range.**
```
cmd    python -c "import math; [print(g, round(math.log(0.005/0.178)/math.log(g),2))
       for g in (0.767,0.732,0.673,0.535)]"
out    0.767 13.47 | 0.732 11.45 | 0.673 9.02 | 0.535 5.71
judge  `:17-19`'s "the PLATFORM needs 11-14 ... each HUB needs 5.7-9.0" is right to the digit and
       the group is now attached. The bare gain range 0.53-0.77 gives 5.63-13.67, which is the
       quantity that was being published without its group.
```
* **R1254, R1255 -- ROUTED IN THE ARTIFACT TO A PLACE THEY ARE NOT IN. R1258.**
* **R1247 -- reviewer-side, unchanged, and THIS COMMIT MADE IT LOAD-BEARING, which I state because
  it is in my own favour.** `_newest_verdict_closes()` searches the WHOLE accumulated file, so
  verdict 66, the addendum and this one all inherit verdict 65's `Closes:`. That is what sends the
  guards to the artifact at all, and it is the documented semantics in `docs/SUPERVISOR.md` ("the
  newest verdict carrying `Closes:`") while the function's own docstring says "the NEWEST entry". The
  behaviour is right here; the docstring is still wrong. Measured, not trusted, and in the corpus.
  **There is a THIRD reader and it is unaffected**: `.claude/hooks/require-verdict.sh:332` tests
  PRESENCE (`grep -qE '^Closes:'`), not value, so the repair neither reaches it nor needs to.
* **R1232 -- correctly held for the write run (step 2).** No write run was made:
  `git diff --name-only 492fc22..HEAD -- data results docs/F6_utilisation.csv scripts/measure` is
  empty.
* **R1248 -- step 2, unchanged. R1212, R1217, R1218, R1222, R1224, R1234, R1242 -- carried as
  routed; R1218 becomes blocking when step 2 writes the tolerance entry. R1186, R1188, R1189, R1190,
  R1191, R1193, R1196, R1197, R1198, R1199, R1200, R1201, R1203, R1204 -- open from verdict 58, to
  step 1, none a step-0 matter. R835 -- `unchanged, R2` (GE3), one line, not re-measured.**
* **YOUR QUESTION ABOUT THE "FIFTH INSTANCE" -- YES, THE DISTINCTION BELONGS IN THE RULE, AND I
  THINK YOU HAVE UNDERSTATED IT TWICE OVER.** You wrote that four of the five were predicates the
  repair failed to reach and the fifth one the repair itself created. **There is a sixth and it is in
  the repair as shipped**: R1261. So the rule the step produced is not "use the committed generator"
  alone; it is **the repair of a two-reader predicate is measured at BOTH readers, over the same
  state grid, AFTER the repair** -- which is what found R1256 and R1261, and which no amount of care
  at the first reader would have produced.

## Findings

**R1256. (BLOCKS) THE REPAIR CLOSES THE CELL ITS CONDITION NAMED AND LEAVES THE SIBLING CELL GREEN:
WHEN THE ROUTED-TO CLOSURE ARTIFACT DOES NOT EXIST, BOTH READERS FALL BACK TO THE STEP REPORT, AND AT
THE NEXT CLOSURE COMMIT THAT IS FULLY GREEN.**

```
claim  after the repair, a closure commit cannot publish CZ1's record nowhere and stay green
cmd    the state grid the decision rule guards, swept: {Closes: present / absent / another
       increment / another form} x {artifact present / absent} x {block present / absent / empty /
       duplicated}. 14 cells, one at a time, in a detached probe at 5901738, against
       `scripts/check_carried.py`, the five `test_FK2_*` ids, the three FC1 ids and the whole of
       `tests/verification/rung3/test_closure_evidence_exists.py`
out    artifact EXISTS, no block   -> cz1_record() == ""         -> 2 failed, 1 skipped    RED
       artifact ABSENT             -> cz1_record() == the STEP    -> 3 passed              GREEN
                                      REPORT's newest revision
cell   ONE VARIABLE, the presence of `docs/closure/R2-step0.md`. The `Closes:` line, the report and
       the code were untouched in both halves.
cmd    THE DECISIVE CELL, because the artifact-absent run above is red for an UNRELATED reason in
       THIS tree only -- `check_carried` exits 1 because EK3 seals this step's report and so it
       omits R1243. So I ran the state every FUTURE step will be in: artifact ABSENT and the
       report's `Carried` section COMPLETE.
out    check_carried                 exit 0, "all 36 findings carried"
       the three FC1 guards          3 passed
       _suite_line()                 ('a3a30d2', 3970, 2, 0)
rule   `cz1_record`'s own docstring -- "Returns `""` when this increment is closed and the artifact
       has no block, so the guards fail with their own messages rather than falling back to a step
       report whose older line would answer in their place. That fall-back is R803, and it failed
       GREEN." The absent-artifact branch IS that fall-back.
judge  Two readers, one predicate, and the repair reached one STATE of it.
       `tests/test_report_carried.py:3131` (`if not CLOSURE.exists(): return report`) and
       `scripts/check_carried.py:102` (`if artifact.is_file():` ... else `return report`).
```

**The silently wrong result.** At R2 step 1's closure commit -- the next one there will be -- a commit
that creates no `docs/closure/R2-step1.md` publishes **no CZ1 record at all** and the tree is green:
`check_carried` exits 0 against the step report, and `test_the_report_carries_a_WHOLE_SUITE_count`,
`test_a_RED_suite_is_named_in_the_report` and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` all
pass **while reading the step report's own whole-suite line and CI table**, measured several commits
earlier. At today's tree that line is `3970 passed, 2 failed, 0 skipped` at `a3a30d2`, four commits
before the closure commit, and the ten reds that actually existed at the closure commit are invisible.
That is R1250's own sentence, which I am quoting rather than re-deriving: *"a closure commit that
shipped CZ1's outputs nowhere at all would get exactly the same green."*

**And nothing else in the repository covers it, which I checked BEFORE blocking rather than after.**
`tests/verification/rung3/test_closure_evidence_exists.py:42` is
`CLOSURE = sorted((REPO / "docs" / "closure").glob("*.md"))` and every assertion in that module is
parametrised over it -- **so the collection the assertion inspects is the set of artifacts that
exist, and a missing one is invisible by construction.** That is the assertion-domain shape, in the
one module that exists to stop a closure artifact certifying rather than recording. The FK2 suite has
`test_FK2_a_CLOSED_increment_with_NO_BLOCK_reddens` and no sibling for a closed increment with no
artifact. And `tests/corpus/closure_artifact_published_as_green.txt:97`, written one verdict ago,
**names this state in so many words and was not measured by the commit that repaired its neighbour.**

*Closed when* the absent destination reaches the same branch as the present-but-empty one: when the
newest verdict's `Closes:` names THIS increment an artifact is OWED, so `not CLOSURE.exists()` is the
`""` branch and not the report, **in both readers** -- `check_carried.py`'s `_carrier` included, where
today the `is_file()` miss returns the report. With the inversion EH4 asks for in both directions, and
a row in the existing FK2 block for the state (a test row in a file that exists is not new apparatus).
**THE EXIT EXISTS AND I CHECKED IT BEFORE ASKING, because a repair with no green state is worse than
the hole:** the only commits in the window between a closing verdict and its closure commit are the
reviewer's own, and the two ids that would redden there are
`test_the_report_carries_a_WHOLE_SUITE_count` and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` --
**which are the two names FT1 adopted limb two FOR, by name** -- so those reds are boundary reds under
the predicate in force and the closure commit clears them.
`test_FK2_an_INTERIM_verdict_routes_to_the_REPORT` is untouched, because an interim verdict carries no
`Closes:` line at all.

**R1257. (ledger, FR1 -- figure wording in a deliverable, no wrong result follows) R1251 IS FIXED AT
ONE OF ITS TWO SITES IN THE SAME FILE, AND THE SURVIVING ONE IS 88 LINES BELOW THE CORRECTION.**
```
cmd    python -c "import re;print(re.findall(r'recorded eight\s+lines from the edit',
       open('docs/closure/R2-step0.md',encoding='utf-8').read()))"
out    ['recorded eight\n  lines from the edit']        -- docs/closure/R2-step0.md:371-372
cmd    grep -n "eight lines" docs/closure/R2-step0.md
out    (no match)
rule   verdict 66 R1251 -- the distance is 25 from CH3's last line and 31 from its first, and 8 at
       no commit in this step; `:283` now says TWENTY-FIVE and adds "getting it wrong twice in the
       same sentence is [the point]"
```
`:371-372` sits in "The honest account of the round", which is the section a later reader opens for
the step's own self-assessment, and it republishes the figure the paragraph four screens above has
just withdrawn -- BP0 inside one file. **`grep -n "eight lines"` finds nothing because the phrase
wraps a line**, so a line-anchored needle cannot see it: R1254's family, turned on the repair of
R1251. *Closed when* `:371-372` carries 25 or drops the distance, which `:283` already says is not
the point.

**R1258. (ledger) THE CARRIED TABLE ROUTES R1254 AND R1255 TO "THIS ARTIFACT, BELOW" AND NEITHER
APPEARS ANYWHERE IN THE REPOSITORY OUTSIDE THE VERDICT FILE.**
```
cmd    grep -rn "R1254\|R1255" --include=*.md --include=*.py --include=*.txt . | grep -v docs/reviews/
out    ./docs/closure/R2-step0.md:184:| R1251, R1252, R1253, R1254, R1255 | ledger | figure and
       needle corrections in this artifact, below |
cmd    grep -n "R12" docs/milestones/F2a.md
out    (no match)     -- and verdict 66 routed both to that frozen list "if it goes anywhere"
rule   `scripts/check_carried.py`'s own docstring -- "It does not check that the status written
       beside each one is true -- a report can carry `R142` and lie about it. That half is the
       reviewer's"
```
R1251, R1252 and R1253 are answered below, as the cell says. R1254 (rung 3's needle cannot see
`scripts/`, `data/`, `results/` or `.github/`) and R1255 (the ladder's step order is asserted for
rungs 3, 4 and 6 and for nothing else, so rung 1 can be moved to the end of the job and the tree
stays green) are the two with measurements attached, and those measurements are now in no file the
project keeps. **This is the third time in two rounds that a record has said an item was answered
where it was not** -- R1245 and R1246 were the first two, and both were in a hand-back; this one is in
the deliverable. *Closed when* the two rows exist in the artifact, or the cell reads "recorded in
verdict 66; not carried forward". Either is honest and one line.

**R1259. (ledger) THE R1245 PARAGRAPH ASSERTS A HISTORY AND REFUTES IT IN THE SAME SENTENCE, AND THE
CLAUSE IT BORROWED IS R1246's, WHERE IT IS TRUE.**
```
claim  docs/closure/R2-step0.md:202-205 -- "The correction was made in `e71ecd5` **and the
       byte-for-byte restore in `ce5a84f` reverted it** -- ... is `0`, so it never existed in a file
       at all."
cmd    git show e71ecd5:docs/reports/R2/step-0.md | grep -c "four items" ; ... "five items" ; ... R1219
out    0 ; 1 ; 7
cmd    git show e71ecd5:docs/reports/R2/step-0.md | grep -c "generated: scripts/untouched_sites"
out    1     -- R1246's repair DID exist in the file there, and is 0 at the judged commit
cell   ONE VARIABLE, which item. At `e71ecd5` R1245's correction was never in the file and R1246's
       was. The restore therefore reverted R1246's and had nothing of R1245's to revert.
rule   BG0 -- a causal sentence carries the cell that isolates it; CP2 -- a repair's prose carries
       its own numbers
```
The first clause is false, the third is true, and "and" joins them in one sentence. Nothing turns on
it today -- both items end in the same place for the same reason -- and it is CP2's exact species: the
care went to the fix and the prose written around it inherited none of it. *Closed when* `:202-205`
says of R1245 what the `grep` says: the correction existed only in `e71ecd5`'s commit message, and the
restore is why R1246's vanished.

**R1260. (ledger, FR1's second non-blocking class) THE ESCALATION CITES `requirements-lock.txt` AS
THOUGH IT WERE FLOATFEA-LOCAL, IT IS HSP's, AND VERDICT 66's "ALL TEN PATH CITATIONS RESOLVE" IS
REFUTED BY THE ELEVENTH.**
```
cmd    git ls-files '*lock*' '*requirement*'
out    (empty)
cmd    git grep -n "requirements-lock"
out    docs/closure/R2-step0.md:226   `requirements-lock.txt`                    <- unprefixed
       docs/reports/R2/step-0.md:584  `HSP-runs/requirements-lock.txt`           <- the report is right
       floatfea/hsp_pin.py:147        "Environment is requirements-lock.txt in the HSP repo"
rule   rung3/test_closure_evidence_exists.py -- "Cross-repo evidence is prefixed `HSP:` ... an
       unprefixed path is asserted to be FloatFEA-local", and its `_PATH` matches
       `(?:tests|floatfea|docs)/...` only, so a BARE filename is invisible to the very guard that
       enforces the prefix
cmd    a WIDER needle over every backticked file citation in the artifact
out    14 distinct; 13 resolve (five written as bare filenames that resolve under `scripts/`,
       `tests/regression/`, `tests/` and `docs/reports/`); 1 exists nowhere in this repository
```
The two version pairs beside it are right -- installed `numpy 2.5.4`, `scipy 1.18.1`, which is what
`:226` says -- so no number is wrong and nothing published is unconservative. **What is worth saying
is whose finding this is:** my predecessor wrote "I checked all ten path citations in the artifact one
by one and all ten resolve" in the same verdict that raised R1254 about needles too narrow to see
`scripts/`, and the census that produced the ten used the narrow needle. R755's shape, from the
reviewer's side of the loop, one round later. *Closed when* `:226` reads `HSP:requirements-lock.txt`
or `HSP-runs/requirements-lock.txt`, matching the report.

**R1261. (ledger) THE TWO READERS STILL DIVERGE ON THE MILESTONE CHECK, WHICH IS THE SIXTH INSTANCE
OF THIS STEP'S OWN RULE AND SITS INSIDE THE COMMIT THAT CLAIMS THE FIFTH.**
```
cmd    the anchored `Closes:` line replaced by `Closes: F2/step-4`, another milestone's EXISTING
       artifact, in a detached probe
out    scripts/check_carried.py    "the step is CLOSED, so reading F2-step4.md", exit 1
       test_report_carried.py      CLOSURE=F2-step4.md, and `cz1_record()` REFUSES it on
                                   `closes.split("/", 1)[0] != MILESTONE` and reads the report
rule   `cz1_record`'s docstring -- "a line naming another increment ... sends them to the step
       report"; and `scripts/write_verdict.py:_closes` resolves the milestone part through the plan
       but does NOT compare it against the plan stem carrying the step marker, so
       `--closes F2/step-4` is writable
```
`_carrier` has no milestone comparison. It is unreachable without an FK1 violation and, forced, it
fails in the SAFE direction here because R2's ids and F2's do not overlap -- which is why it is a
ledger row and not part of R1256. **It is still the same defect the commit message is about**, one
function below the one that was fixed, and it is why my carried note asks for the word BOTH in the
rule. *Closed when* `_carrier` applies the comparison `cz1_record` already applies, in the same commit
as R1256 and measured at the same cell.

**R1262. (ledger) THE BLOCK IS LABELLED "CZ1 (ii)-(iv)" AND CARRIES (ii) PLUS A RUN CENSUS; (iii)'s
EVIDENCE IS IN VERDICT 66 AND IS NOT POINTED AT.**
```
cmd    grep -niE "guards and meta-tests|job-level|skipped behind|actionlint" docs/closure/R2-step0.md
out    (no match)
rule   CZ1 (iii) -- "paste `gh run list --commit <sha>` with the job-level conclusions, **so that
       the lint job's `guards and meta-tests` step is seen to have RUN rather than been skipped
       behind an earlier red step**"
```
`:47` says "(ii)-(iv)". `:52-61` is (ii); `:69-142` is `ci_section.py`'s run census, which is
run-level conclusions plus per-test job attribution; `:144-156` serves (iv). The step list showing
`guards and meta-tests` RAN at `ce5a84f` exists -- in verdict 66's CI section -- and the artifact
neither carries it nor cites it, so the record an auditor reads cannot answer the one question
CZ1 (iii) was written for. *Closed when* `:47` cites verdict 66 for (iii), or the block carries the
step list. One sentence.

## Tolerances touched

**None, measured twice.** `git diff 492fc22..HEAD -- floatfea/tolerances.py` is **0 lines** and
`git diff 492fc22..HEAD | grep -cE '^[-+].*_COUNTER'` is **0**, so **EU1 does not arise** -- and I ran
the apparatus at twenty-seven configurations the diff did not choose anyway, which is where R1256 and
R1261 came from. The one tolerance-shaped thing still implicated has not moved: `--check`'s
`np.array_equal` with no threshold, by Q8's rule. **If any answer to the escalation introduces a
tolerance on that comparison, that is a widening and it is refused.** R1218's row-1 form question
becomes blocking at step 2.

## Corpus

**One batch, 42 entries, all new, committed separately at the commit BEFORE this verdict.** GC3 left
the pause expired, so the batch is my own call under GA3's length target.

`tests/corpus/closure_record_absent_rather_than_wrong.txt`. **14 measured; 2 of those are robustness
probes that should pass and do; of the 12 defect plants 8 reach a red and 4 reach a green tree.** The
axis is the one `tests/corpus/closure_artifact_published_as_green.txt` presupposes away: all 38 of its
entries assume the artifact EXISTS and the router READS it, and this file is the destination missing,
empty, duplicated or named differently. The four that reach green are the ids-moved-into-a-fenced-block
case and the three routing-cell cases of R1258. The headline entry is the decisive cell of R1256.

**The reason for a second file rather than more entries in the first is itself the measurement:** the
two halves BEHAVED IDENTICALLY before this commit and behave differently after it, so one entry of the
old file -- `:97`, "the same shape with the artifact ABSENT, which the router treats identically" --
now describes a state that is no longer identical and is still green. **A corpus entry that survived
its own repair** is exactly what a planted-shape count by the repair's author cannot produce, and this
is the first time in this milestone that one has.

**What I ran beside the batch is the recorded substitute, both halves, and both halves produced
findings.** A continuum grid over the parameter space a decision rule guards: the
`Closes:`/`CLOSURE`/artifact/block grid -- 14 cells, plus 5 on the `Closes:` value, plus 3 on the
naming guard -- which gave R1256 and R1261. A regeneration check on a published deliverable: the
closure artifact re-measured figure by figure at its own commit -- six figures checked, three hold
(the round arithmetic, the ten-findings scope, and the gain/iteration table, which I re-derived
independently to the digit) and three do not (R1257, R1260, R1262).

## Next step opens when

**STEP 0 STAYS CLOSED (DD1). THIS HOLD IS ON THE FOLLOW-ON COMMIT AND NOT ON THE STEP**, and it
consumes none of step 0's three ES0 revisions (EB4). Verdict 65's `Closes:` line is untouched and is
still the one the FC1 router reads; **this verdict carries no `Closes:` line, as FK1 requires of a
verdict that closes nothing.** Step 1 is held by GI6 until Xabier confirms or overrides D1-D4, and by
R1243, independently of anything here.

1. **R1256, in one commit, with R1261 folded into it** -- one condition in each of two readers, the
   inversion in both directions, and a row in the existing FK2 block. That is the repair of a guard
   that fails GREEN, which EK2 permits and FF0 puts ahead of everything else.
2. **CZ1 (ii)'s `pytest -q` AT `5901738`, AND THE ANSWER TO YOUR QUESTION IS: NOT HERE, AND NOT IN
   THE ARTIFACT'S BLOCK EITHER.** It goes in **step 1's report `Carried`** -- the place CZ1 names for
   a closed report, and the place verdict 66 already routed `ce5a84f`'s to. Two reasons, and the
   second decides it: the artifact's block is CZ1's record for the closure commit `ce5a84f`, and
   overwriting it with the follow-on's would delete the record R1249 was raised to produce; and a
   count taken at `5901738` cannot be written into `5901738`, which is CZ1's own reusable half.
   **Three of CZ1 (ii)'s four outputs and the whole of (iii) are measured at `5901738`'s own sha in
   my Tests and CI sections above and may be taken from there.** When you paste the suite run, the
   reds named above are what it should contain and nothing else -- anything more is CZ1 (iv).
3. **R1257, R1258, R1259, R1260, R1262 -- five lines in the artifact, fixed once as part of the list
   and not re-reviewed item by item.** Four are a sentence each; R1258 is two rows or one honest cell.
4. **R1243 appears by name in step 1's `Carried` and stays blocking there** until the chaining is
   fixed and that fix is reviewed.
5. **The escalation's conditions are unchanged.** Do not clear the staleness guard by regenerating the
   npz; do not clear R1223 by regenerating the deliverable against a red gate. Six rounds of declining
   the cheap wrong repair is still the best evidence this step has produced.
6. **`docs/reports/R2/step-0.md:1616` and `:1629` stay DECLARE-ONLY**, recorded `**no change** --
   EK3` in step 1's report, as the artifact already says.

**Nothing here is a STOP, and I considered it on the ladder.** No `floatfea/` file is in this diff; no
tolerance moved; the locked plan is untouched; `.claude/` and `docs/SUPERVISOR.md` are untouched, so
no STOP-class finding arises. Rungs 1, 2 and 3 are SUCCESS in CI at the judged commit's own run.

**And I disagree with nothing in the criterion.** FR1 did the work again: six of this round's seven
findings are single lines here instead of rounds, and the one that blocks is given the sentence FR1
asks for -- a closure commit that publishes no CZ1 record at all, green, with an auditor reading a
suite count from four commits earlier. **What I would say to Xabier if asked, in one sentence:** this
step has now produced, twice running, a repair that was exactly right at the state its condition named
and green at the state beside it, and the cheapest thing available from that is not another guard but
the habit of sweeping the grid rather than the cell.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0
Reviewed commit: ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5
**Reviewed commit: `ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5`.**
Verdict: HOLD
Scope: **ADDENDUM to the EQ0 review BELOW -- same reviewer, same branch, same judged commit,
accumulating under DX2. It counts against no round (EB4) and closes nothing, so `--closes` is
correctly absent (FK1), and the HOLD and both blocking findings are UNCHANGED.** It exists because
two measurements landed after I had written the entry below, and one of them contradicts what that
entry says about itself. **CP3 is the rule I was applying to the implementer four screens above --
"if an edit follows the paste, the paste is void" -- and the symmetrical case is a measurement that
arrives after the text.** Correcting it here is cheaper than leaving a reviewer's own figure wrong.

**(1) MY WHOLE-SUITE RUN DID FINISH, AND THE ENTRY BELOW SAYS I ABANDONED IT. THE ENTRY IS WRONG
ABOUT THAT AND THE RESULT IS THE TEN I PREDICTED, BY NAME.**
```
cmd    python -m pytest -q -p no:randomly          (my own worktree at ce5a84f)
out    10 failed, 4456 passed, 2 warnings in 3575.01s (0:59:35)
       FAILED tests/regression/test_f6_deliverable_agrees_with_itself.py::test_R756_...
       FAILED tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
       FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
       FAILED ... [non_numeric_step_suffix] [superscript_digit_step_number]
              ... [draft_suffix_beside_a_step_report] [step_number_is_the_empty_string]
              ... [verdict_amended_after_the_commit_the_report_answers] [zero_padded_step_number]
       FAILED tests/verification/rung4/test_f4_g41_dynamic.py::
              test_the_npz_is_NOT_STALE_against_the_code_that_generated_it
```
**Exactly the nine CI produced plus the npz staleness guard, which CI could not reach because rung 4
was skipped.** So every red in the tree at the judged commit is now accounted for from BOTH sides:
eight boundary reds under the FS1/FT1 predicate, and the escalation's two, each named. **CZ1 (iv)
does not fire.**

**THE CAVEAT, STATED RATHER THAN BURIED, BECAUSE THE RUN OVERLAPPED TWO COMMITS OF MY OWN.** The
session ran 15:07 to 16:06:36; my corpus commit landed 15:56:49 and my verdict commit 16:06:10, so
the run finished 26 seconds after a commit that changes a file three of its tests read. Two
measurements say the result is nonetheless a measurement of `ce5a84f`:
```
claim  the corpus commit adds no collected id
cmd    pytest -q -p no:randomly tests/test_collected_set_golden.py   (with both new files present)
out    106 passed
claim  the eight report-guard ids ran BEFORE the verdict commit
cmd    pytest -q -p no:randomly <the three report-guard files>       (at 3e34953, the verdict commit)
out    489 passed, 0 failed
judge  at the verdict commit those eight PASS, so had they run after 16:06:10 they would have
       passed. They failed. Therefore they ran against `ce5a84f`'s tree, which is the only thing
       the count had to be about. I am not claiming more than that: a run whose session spans a
       commit is not a clean measurement, and the right fix is the ordering, which is why the
       entry below says what it says about CZ1's reusable half.
```

**(2) EG3 (ii), MEASURED AT MY OWN VERDICT COMMIT. ALL EIGHT BOUNDARY REDS CLEAR.**
```
cmd    git checkout --detach 3e34953 ; pytest -q -p no:randomly tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py tests/test_report_guard_states.py
out    489 passed in 114.81s     (481 passed + the 8 that were red = 489, to the id)
```
State (1)'s half is the reviewer's to measure and this is the third consecutive round in which it
has been. **It also settles the boundary-state reading in the entry below by measurement rather than
by argument:** the clearing event is the VERDICT COMMIT, not a new report revision, which is why I
filed it under limb two of FS1/FT1 rather than under EG3 state (1).

**(3) AND THE PASS-COUNT DIFFERENCE AGAINST YOUR OWN RUN IS R1249's CELL, INDEPENDENTLY.** You
measured `10 failed, 4459 passed` at `e71ecd5`; I measure `10 failed, 4456 passed` at `ce5a84f`.
Same ten, three fewer ids.
```
cmd    pytest -q -p no:randomly --collect-only, at BOTH commits, on the same three files
out    e71ecd5   test_report_carried + test_report_numbers_are_sourced  468 tests collected
                 test_report_guard_states                               24 tests collected
       ce5a84f   test_report_carried + test_report_numbers_are_sourced  465 tests collected
                 test_report_guard_states                               24 tests collected
cell   ONE VARIABLE, the report's content, from the two whole-suite runs and the two collections:
         e71ecd5   4469 ids total   three report-guard files: 492 ids
         ce5a84f   4466 ids total   three report-guard files: 489 ids
       -3 in both places, and the three are the parametrised ids the R1243 rows in e71ecd5's
       report created and the EK3 restore removed.
judge  **SO THE ARTIFACT'S `468 + 24 passed` IS NOT A STALE PASS COUNT -- IT IS THE COLLECTED ID
       COUNT PUBLISHED AS A PASS COUNT, AND I MEASURED IT RATHER THAN INFERRING IT.** `468` and
       `24` are exactly what `--collect-only` prints at `e71ecd5`, where the RESULT was 484 passed
       and 8 failed. A row that reports "collected" as "passed" is green by construction whatever
       the suite does, which is a sharper defect than staleness and it is the same row. R1249
       stands, with its mechanism now measured from a second direction.
```

## Carried

**Everything in the entry below stands unchanged**, and nothing here answers or withdraws any of it.
**R1249 and R1250 remain the two blocking findings**; R1243's condition remains discharged with its
forward item carried into step 1 by name and still blocking; R1245 and R1246 remain OPEN against a
hand-back that reports them answered; R1251-R1255 remain ledger rows; the escalation's R1225 and
R1223 remain open and escalated, and the whole-suite run above is the first measurement this step
has had of BOTH their reds in one place, since CI can only ever see one of the two while rung 4 is
skipped. **R835: unchanged, R2 (GE3).**

## Findings

**No new findings.** Three corrections, all to my own entry, all above: the whole-suite run finished
and the entry says it did not; EG3 (ii) is measured at `489 passed, 0 failed`; and the pass-count
difference against your run closes R1249's cell from a second direction rather than opening anything.

**One thing I will not dress up.** The defect in my own entry is the same shape as the one I blocked
you for -- a figure that was true when written and false when read, with nothing in the tree to say
so. Mine was cheap to catch because the measurement was still running and I was watching it. Yours
was cheap to catch too, which is the point of R1249 and not a complaint about the artifact.

## Tolerances touched

**None, and the measurement is unchanged from the entry below:** `git diff e511161..ce5a84f --
floatfea/tolerances.py` is 0 lines and `git diff e511161..ce5a84f | grep -cE '^[-+].*_COUNTER'` is 0,
so EU1 does not arise. No tolerance appears anywhere in the whole-suite failure list above.

## Next step opens when

**Unchanged from the entry below, items 1 to 6, except that item 2 is now smaller.** CZ1 (ii)'s
`pytest -q` at `ce5a84f` is in this addendum -- `10 failed, 4456 passed`, with the caveat stated and
every id named -- and CZ1 (iii)'s `gh run list` at that sha is in the entry below, concluded. **So
what step 1's report `Carried` owes for CZ1 is a pointer to those two measurements and your own
confirming run, not a fresh set.** Step 0 stays CLOSED (DD1); this remains a HOLD on the closure
commit and not on the step; R1249 and R1250 go in the CZ1 (iv) follow-on.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0
Reviewed commit: ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5
**Reviewed commit: `ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5`.**
Verdict: HOLD
Scope: **the EQ0 REVIEW OF R2 STEP 0's CLOSURE COMMIT**, two commits -- `e71ecd5`, which changes a
gate (`.github/workflows/ci.yml`), and `ce5a84f`, its EK3 correction. EQ0 puts it in scope because a
gate moved; **EB4 makes it cost no round**, and under **DD1 step 0 remains CLOSED by verdict 65
(`Closes: R2/step-0`)** -- this HOLD is on the CLOSURE COMMIT and on nothing else. It is not a
revision 4, it closes nothing, and `--closes` is correctly absent (FK1). Ruled under **FR1 with
EZ0**: each blocking finding names the silently wrong result it produces. **GE3: `R835: unchanged,
R2`. Not re-measured.**

**ITEM 1b, AND THE READING IT NEEDS HERE.** The report's header is `Answers: verdict 64 @ a3a30d2`
while the newest verdict is 65 @ `e511161`.
```
cmd    sed -n '1516p' docs/reports/R2/step-0.md
out    Answers: verdict 64 @ a3a30d2
cmd    git diff 0fb8c93 HEAD -- docs/reports/ | wc -l
out    0
```
**This is not a report revision and 1b does not fire.** Verdict 65 measured 1b PASSING at `0fb8c93`,
where `a3a30d2` WAS the newest verdict; EK3 then sealed the file, and the restore is byte-for-byte,
so the header is the one 1b has already passed on. I state it rather than skip it.

**4 / 4b / 4c, each diffed separately against the previous verdict commit `e511161`:**
`floatfea/tolerances.py` **0 lines**; `.claude docs/SUPERVISOR.md` **0 lines, so no STOP-class
finding**; `tests/conftest.py` **0 lines**, and `git ls-files -- tests/conftest.py
'tests/**/conftest.py'` returns `tests/conftest.py` as it must -- no new conftest, no new plugin.
`git diff e511161..ce5a84f | grep -cE '^[-+].*_COUNTER'` is **0**, so EU1 does not arise, and the
whole diff is two paths: `.github/workflows/ci.yml` and `docs/closure/R2-step0.md`.

Tests: **8 failed, 481 passed on the three report-guard files; 87 passed and 200 passed on the two
other gate selections; `ruff`, `black --check` and `mypy` clean -- MY OWN RUNS, in my own worktrees
at the judged sha, `-p no:randomly`.**
* `tests/test_report_carried.py` + `test_report_numbers_are_sourced.py` +
  `test_report_guard_states.py` -> **8 failed, 481 passed in 108.36s.** Every id traced below.
  **The artifact publishes this selection as `468 + 24 passed`; that is R1249.**
* `tests/test_ci_determinism_gate.py` + `test_ci_ladder_gating.py` +
  `test_ci_workflow_is_wellformed.py` -> **85 passed in 146.53s**, and 87 with
  `test_ci_runs_the_whole_suite.py` added. The reverted gate is green, and green on the assertion it
  was reverted to satisfy.
* `tests/verification/rung3/test_closure_evidence_exists.py` + `test_collected_set_golden.py` +
  `test_tree_prose_consistent.py` -> **200 passed in 41.99s** (the corpus baseline).
* `ruff check floatfea tests` -> **All checks passed!**; `black --check floatfea tests` -> **129
  files would be left unchanged**; `mypy floatfea` -> **Success: no issues found in 45 source
  files.** Three of CZ1 (ii)'s four outputs confirmed at `ce5a84f`'s own sha rather than accepted
  from the report, and your figures for these three match mine exactly.
* `python scripts/check_carried.py` -> **exit 1**, and that is R1249.
* **WHAT I DID NOT FINISH, SAID RATHER THAN IMPLIED: my own whole-suite `pytest -q`.** It was still
  running when I came to write this file, and writing this file changes a document three of the
  guards in that run read -- so I abandoned it rather than publish a count taken across a tree that
  moved underneath it. That is CZ1's reusable half on the reviewer's own side and it is the same
  ordering CP3 is about. **What stands in for it is better evidence, not worse: the CONCLUDED CI run
  at the judged commit's own sha**, below, which executed 1276 + 66 + 329 + 477 ladder tests, 480
  unit tests and 1406 guards and meta-tests on a machine neither of us controls, and whose eight
  guard reds are THE SAME EIGHT IDS, by name, that my own local run of those three files produced.
  Two independent measurements of the same eight is the cross-check a single whole-suite number
  would not have given.

CI: **THE JUDGED COMMIT HAS A CONCLUDED RUN AND IT IS RED. Under CA2 a red CI is a HOLD regardless of
the local run, and this verdict is a HOLD -- but every red traces, so the redness is not an
independent block on top of the two findings.**
```
cmd    gh run list --commit ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5 --json conclusion,status,databaseId
out    [{"conclusion":"failure","databaseId":44196001239,"status":"completed"}]
cmd    gh api repos/:owner/:repo/actions/runs/44196001239/jobs --jq '.jobs[] |
       "\(.name) | \(.status) | \(.conclusion) | runner=[\(.runner_name)] | steps=\(.steps|length)"'
out    the verification ladder            | completed | failure | runner=[GitHub Actions 1000001934] | 13
       lint, unit and guards              | completed | failure | runner=[GitHub Actions 1000001935] | 14
       CI determinism -- leg              | completed | skipped | runner=[null] | 0
       CI determinism -- ten legs agree   | completed | skipped | runner=[null] | 0
```
**NOT CK2** -- the two executing jobs were given runners, steps and work; the two determinism jobs
are `skipped` by their own `workflow_dispatch` condition, which is unavailable and not passing.
`e71ecd5`, the other commit in scope, also concluded FAILURE, at run `44187721362`.

**THE STEP LIST IS THE MEASUREMENT CZ1 (iii) EXISTS FOR, AND IT IS ALSO THE MEASUREMENT OF R1243's
REVERT.**
```
cmd    gh api .../44196001239/jobs --jq '.jobs[] | .name as $j | .steps[] |
       "\($j) :: \(.number) \(.name) -> \(.conclusion)"'
out    the verification ladder :: 5 ladder 1 -- the solver is a solver        -> success
                              :: 6 ladder 2 -- the element is the element    -> success
                              :: 7 ladder 3 -- the model is the platform     -> success
                              :: 8 ladder 6 -- it stays fixed                -> FAILURE
                              :: 9 ladder 4 -- the loads are the loads       -> skipped
                              :: 10 ladder 5 -- independent confirmation     -> skipped
       lint, unit and guards  :: 5 actionlint -> success | 6 ruff -> success
                              :: 7 black --check -> success | 8 mypy -> success
                              :: 9 unit tests -> success | 10 guards and meta-tests -> FAILURE
cmd    gh run view 44196001239 --log | grep -oE "run_rung: [0-9]+ collected, [0-9]+ failed[^\"]*"
out    1276 collected, 0 failed | 66 collected, 0 failed | 329 collected, 0 failed |
       477 collected, 1 failed
cmd    gh run view 44196001239 --log | grep -i "ladder 6.*run_rung: *failure"
out    tests.regression.test_f6_deliverable_agrees_with_itself::
       test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
cmd    the same log, the two step totals
out    unit tests  480 passed      |  guards and meta-tests  8 failed, 1398 passed
```
**CH3's order is in force in CI, measured from CI rather than from the file.** `guards and
meta-tests` is seen to have RUN rather than been skipped behind an earlier red -- which is the exact
hiding CZ1 (iii) was written for -- `ruff`, `black` and `mypy` are green on the canonical machine as
well as on mine, and the ladder's single red is named rather than classified: `test_R756`, the
escalation. **Rung 4 did not execute, so the npz staleness guard did not run in CI**, which is
R1239's second exit recorded as the artifact records it, not a new fact.

**EVERY RED TRACED PER ID AGAINST THE FS1/FT1 PREDICATE (EG3 (i)) -- THE PREDICATE CHECKED, NOT A
LIST.** **NINE REDS AT `ce5a84f` IN CI, AND THE EIGHT IN THE GUARDS JOB ARE THE SAME EIGHT MY OWN
RUN PRODUCED, BY NAME.** Both lists, matched id by id:
```
1   tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
      -> "the report at `e71ecd5` is newer than the verdict at `e511161` and names `a3a30d2`".
         LIMB TWO: its subject IS the commit carrying it -- it compares the newest commit touching
         the report with the newest touching the verdict, and the commit carrying it is the one
         that touched the report. It also reaches limb one, since `docs/reports/R2/step-0.md` is a
         site of verdict 65 (R1244 at `:813`, R1245 at sec.19 and sec.19c). Boundary red.
7   tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline |
    non_numeric_step_suffix | superscript_digit_step_number | draft_suffix_beside_a_step_report |
    step_number_is_the_empty_string | verdict_amended_after_the_commit_the_report_answers |
    zero_padded_step_number]
      -> the harness's own baseline leg prints `1 failed, 445 passed in 2.07s ... assert 1 == 0`,
         so all seven are the cascade of the one above, and they are the SAME seven verdict 65
         traced and measured clearing at `0fb8c93`. Limb one. Boundary reds.
1   tests/regression/test_f6_deliverable_agrees_with_itself.py::test_R756_the_SHIPPED_report_IS_a_
    regeneration_of_the_current_tree   (CI's ladder, rung 6)
      -> names R1223, carried and escalated by verdict 65 at the site it named, and red at this
         commit WITH ITS CAUSE NAMED as EG3 (i) requires. Limb one. Correctly not cleared.
```
**Not one of the nine fails the predicate, so CZ1 (iv) does not fire on the suite or on CI.** The
eight-way agreement between CI and my own run is the part I would not have had from a single
whole-suite count, and it is measured rather than eyeballed:
```
cmd    comm -12 <(CI's 8, sorted) <(my own 8, sorted) | wc -l
out    8
cmd    comm -23 ... (CI only)  ;  comm -13 ... (local only)
out    (empty)                 ;  (empty)
```
Neither list has a member the other lacks, so the eight are the same eight on two different
operating systems and two different installs, which is what CA2 asks CI for. I do not assert
the clearing. **EG3 (ii) IS MEASURED AT MY OWN VERDICT COMMIT, AFTER THIS FILE IS WRITTEN, AND THE
COUNT GOES TO THE IMPLEMENTER IN MY HAND-BACK** -- a verdict cannot contain a measurement taken at
the commit that creates it, which is CZ1's reusable half applied to the reviewer's own side of the
loop, and it is why state (1)'s half had never been measured before this step. Third consecutive
round in which it has been.

**AND I REACH A DIFFERENT READING OF THE BOUNDARY STATE THAN THE ONE YOU CLAIMED, WITH THE SAME
OUTCOME.** You claimed EG3 state (1). State (1) is *report written, verdict not yet*; state (2) is
*verdict written, answering report not yet*. **This is neither.** A verdict IS written, no answering
report is due because the step is closed, and the red exists because a commit written AFTER the
verdict touched the report. That is not a step boundary at all -- it is EK3's own consequence -- and
it reaches the waiver through **limb two of FS1/FT1**, not through either of EG3's named states. The
outcome is identical; the label matters for the round after this one, because a reader told "state
(1)" looks for a new report revision to clear it and there is none. My verdict commit is what
clears it, which is why I MEASURE that rather than predict it and send you the count. You asked because you had claimed a boundary
state wrongly twice: this is a third reading, and it is the cheapest of the three to get right,
because the predicate is two reasons and neither is a list of names.

Door (FV2 / GG2): `git worktree add -b review/ce5a84fefe1f <a path outside the repository>
ce5a84fefe1f00cf98124b8ab2bb5a97fd0ef3d5` **succeeded on the first try, so no review of this commit
existed.** A second, detached probe worktree at the same sha held every plant. **Fifteen plants of
my own, one variable at a time, with `git status --porcelain` asserted empty inside the harness after
each**, so a dirty tree would have aborted the measurement rather than contaminated it.
`C:\dev\floatfea` was clean when I was invoked and I wrote nothing into it. This verdict is written
through `scripts/write_verdict.py`, committed on `review/ce5a84fefe1f` and pushed -- merge with
`git merge --ff-only origin/review/ce5a84fefe1f`. **The corpus is committed separately, at `d2d95b6`,
BEFORE this verdict**, which is the order `require-verdict.sh` excludes `tests/corpus/` for.

## Carried

Verdict 65's one blocking finding, its five closure items and its carry list. **R1243's CONDITION IS
DISCHARGED WITH ONE HALF OF IT WITHDRAWN BY ME; TWO CLOSURE ITEMS ARE OPEN AGAINST A HAND-BACK THAT
REPORTS THEM ANSWERED, AND ONE OF THOSE WAS REPAIRED AND THEN REVERTED BY THE NEXT COMMIT.**

* **R1243 -- THE CONDITION IS ANSWERED, AND THE REVERT IS CH3's ORDER RATHER THAN MERELY A DIFFERENT
  ONE. That is the one thing you asked me to confirm, and it is measured three ways, two of them
  outside the file.**
```
cmd    git diff 2e08766..ce5a84f -- .github/workflows/ci.yml
out    one hunk, additions only: a 21-line comment block between `ladder 3` and `ladder 6`. NO
       `- name:` or `run:` line is added, removed or moved, so the STEP SEQUENCE at the judged
       commit is byte-identical to the pre-reorder commit's, which is CH3's.
cmd    git show 2e08766:.github/workflows/ci.yml | grep -n 'name: "ladder'
out    525 ladder 3 | 527 ladder 6 | 529 ladder 4        (pre-reorder)
cmd    grep -n 'name: "ladder' .github/workflows/ci.yml
out    525 ladder 3 | 548 ladder 6 | 550 ladder 4        (at ce5a84f -- same sequence, shifted by
                                                          the comment block)
cmd    the CI step list above, at e71ecd5's own run
out    ladder 1,2,3 success | ladder 6 FAILURE | ladder 4, 5 skipped
```
  **So it is CH3's order and not a third ordering that happens to satisfy the gate.** I checked the
  gate rather than assuming it: `tests/test_ci_determinism_gate.py:199` and `:204` assert **both**
  `where["rung6"] < where["rung4"]` **and** `where["rung3"] < where["rung6"]`, which is CH3's whole
  sentence -- behind rungs 1 to 3, out from behind rung 4 -- and both are green.
  **The record R1239's second exit asked for is present**, in the artifact's "What was deferred and
  why": *"Rungs 4 and 5 are unmeasurable in CI while the escalation stands. Rung 6 is red, so the
  rungs after it do not execute."* CI's step list above is the measurement of that sentence rather
  than a restatement of it.
  **And the stale comment is gone in the sense that mattered**: `ci.yml:496-502` (CH3) and `:527-547`
  (the new block) now assert the SAME order, the reorder's own comment is removed in full, and no two
  comments in that file contradict each other. My condition's wording was loose -- under exit 1 the
  comment that had gone stale was the REORDER's, not CH3's -- and the right thing happened anyway.
  **THE HALF OF MY CONDITION I WITHDRAW, AND THE REASON IS STRUCTURAL.** I wrote *"sec.19's 'ONE red
  to TWO' is replaced by the measurement above"*. `docs/reports/R2/step-0.md:1616` still reads
  *"Expect CI's ladder job to go from ONE red to TWO"* and **cannot be changed by this commit**,
  because EK3 forbids a closure commit from touching a step report after that report's final verdict.
  The measurement is published in the artifact's R1243 cell instead, which discharges the substance.
  **A closing verdict must not name a site inside the report it closes.** Mine did it twice -- this
  and R1244's `docs/reports/R2/step-0.md:813` -- and both were unfulfillable by construction, under a
  rule written three sections above the one I was applying. That is a reviewer-side instance of this
  step's own recurring defect: a condition specified from reading rather than from running.
  **The FORWARD item stands exactly as verdict 65 left it.** Chaining rungs in one job hides every
  rung after a red one whichever order they sit in; the fix is to stop the chaining, which is step
  1's. **R1243 carries into step 1's `Carried` by name and stays blocking there.**
* **R1244 -- YOUR CHOICE IS CORRECT AND I RULE IT SO, in your own terms.** Revision 2's rounds table
  stays as it shipped. Rewriting a reviewed generated record so it no longer shows what was published
  removes the evidence of the finding, and the same rule already governs one file over: DX2 keeps
  every verdict round verbatim for exactly that reason, and `scripts/write_verdict.py` carries the
  measurement that forced it -- a file that went 397 -> 508 -> 508 -> 538 lines while mentions of one
  withdrawn item went 3 -> 2 -> 2 -> 0. **Nothing further is owed on R1244.**
* **R1245 -- OPEN, AND THE HAND-BACK'S CLAIM THAT IT IS ANSWERED IS REFUTED.** You wrote "THE FIGURE
  CORRECTIONS from your verdict 65 are in `0fb8c93`'s report".
```
cmd    grep -n "five items" docs/reports/R2/step-0.md
out    1629:out    GAINS R1212, R1217, R1218, R1219, R1224 -- five items the newest verdict carries
cmd    grep -o "GAINS[^\"]*" docs/reports/R2/step-0-answers.json
out    GAINS R1212, R1217, R1218, R1219, R1224 -- five items the
cmd    python -c "import sys;sys.path.insert(0,'tests');import test_report_carried as t;
       print('R1219' in t.EXPECTED, [i in t.EXPECTED for i in ('R1212','R1217','R1218','R1224')])"
out    False [True, True, True, True]
cmd    git show e71ecd5:docs/reports/R2/step-0.md | grep -c "four items"
out    0
cmd    grep -c "four items\|R1219" docs/closure/R2-step0.md
out    0
```
  The figure is wrong in the report and in the answers JSON; it was **not** corrected at `e71ecd5`
  either; and the correction exists only in `e71ecd5`'s commit message, which BF0 and CZ1 both put
  outside the record. **I am not holding on it** -- verdict 65 classed R1245 a closure item, and
  `CLAUDE.md` forbids me to re-review one item by item or to hold a step on one. It is recorded as
  OPEN against a claim that it is answered, and EK3 now leaves the artifact as its only home.
* **R1246 -- REPAIRED AT `e71ecd5` AND REVERTED BY `ce5a84f`, AND NOTHING SAYS SO.** This is the
  collateral of the EK3 restore, and it is the one thing I think should also have moved.
```
cmd    git show e71ecd5:docs/reports/R2/step-0.md | grep -n "generated: scripts/untouched_sites"
out    1800:<!-- generated: scripts/untouched_sites.py -->
cmd    grep -c "generated: scripts/untouched_sites" docs/reports/R2/step-0.md
out    0
```
  Your hand-back says "Â§15/Â§19c now come from `scripts/untouched_sites.py`, the committed generator".
  **True at `e71ecd5`; false at the commit I am judging.** The byte-for-byte restore necessarily
  reverted every closure-item repair that lived in the report, and the hand-back describes the tree
  one commit back. **The general fact worth carrying: EK3 and "the implementer fixes the whole
  closure list once, in the step's closure commit" are in direct collision for any closure item whose
  site is the closed report.** Both of my predecessor's report-sited closure items hit it. Not
  blocking, for the same reason as R1245; `docs/closure/R2-step0.md` is where they can still be
  answered.
* **R1247 -- reviewer-side, unchanged, nothing asked of you -- and I added a fourth hole to it this
  round.** `tests/test_report_carried.py:3063-3076`'s `_newest_verdict_closes()` is documented as
  "the `Closes:` line of the NEWEST entry" and implemented as a search over the WHOLE file, so under
  DX2 accumulation every verdict written after a closing one inherits the closing one's routing.
  Benign here, and in my own favour, which is why I measured it rather than trusting it. Every FK2
  test is synthetic and single-entry, so the accumulated case is exercised by none of them. It is in
  the corpus.
* **R1248 -- correctly routed to step 2, and I checked the routing against the plan rather than
  accepting it.** `docs/milestones/R2.md:313-330` is the row where the override file and its
  provenance get written, and R1248 is a provenance-regeneration gap on a committed snapshot.
  Accepted.
* **R1232 -- correctly held for the write run**, which is step 2 (i). No write run was made:
  `git diff --name-only e511161..ce5a84f -- data results docs/F6_utilisation.csv scripts/measure` is
  empty.
* **R1225 / R1223 -- OPEN, ESCALATED AND UNCHANGED, CORRECTLY.** Rung 4 is skipped in CI, so the
  staleness guard did not run there; rung 6's single red is `test_R756...`, named in CI's own log
  above. No `data/` or `results/` path is in this diff. **Fifth round in which the cheap wrong repair
  was available and not taken.** This is still the good part of the step and it is what GI6 sends to
  Xabier.
* **R1217, R1218 -- open, not answerable here.** R1218 becomes blocking when step 2 writes the
  tolerance entry. **R1212, R1203, R1204, R1222, R1224 -- reviewer-side or Xabier's; no action asked
  of you. R1234, and R1239's first exit -- WITHDRAWN, both mine, both stay withdrawn. R835 --
  `unchanged, R2` (GE3), one line, not re-measured.**
* **R1230 -- your fourth instance is real and I confirm it.** What I would add is that the first
  three and this one are not the same defect: the first three were a HEADER that trailed, which an
  edit fixes, and this one is a COMMIT TIME, which no edit of the report's bytes can fix. That is the
  measurement `CLAUDE.md` already records under EK3, and you quoted it correctly.

## Findings

**R1249. (BLOCKS) THE CLOSURE ARTIFACT'S "WHICH GATES PASS" TABLE PUBLISHES TWO OF ITS FIVE ROWS AS
GREEN WHERE THE GATE IS RED AT THE COMMIT THAT PUBLISHES THEM, AND ONE OF THE TWO IS RED ABOUT
R1243.**

```
claim  docs/closure/R2-step0.md:24-32 "Which gates pass" -- five rows, all green
cmd    python scripts/check_carried.py ; echo "exit=$?"            (at ce5a84f, tree clean)
out    check_carried: the newest report's Carried section omits R1243
         verdict declares 29 findings; 28 are carried
       exit=1
cmd    python -m pytest -q -p no:randomly tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py tests/test_report_guard_states.py
out    8 failed, 481 passed in 108.36s
cmd    gh run view 44187721362 --log-failed | grep -c "^FAILED"    (e71ecd5's own run)
out    8
cell   ONE VARIABLE, the report's content. Nothing in `floatfea/`, `tests/` or `scripts/` moves
       between the two commits -- `git diff --name-only e71ecd5 ce5a84f` is two docs paths:
         at e71ecd5   git show e71ecd5:docs/reports/R2/step-0.md | grep -c R1243   ->  4
                      check_carried  ->  29 of 29, exit 0
         at ce5a84f   grep -c R1243 docs/reports/R2/step-0.md                      ->  0
                      check_carried  ->  28 of 29, exit 1
rule   CP3 -- "a figure is pasted from the run that produced the artifact it is pasted into, and
       the pasting is the LAST edit ... if an edit follows the paste, the paste is void"; CZ1 (ii),
       which requires the outputs AT the closure commit's own sha; EG3 (i), which requires a
       boundary red to be recorded RED WITH ITS CAUSE NAMED rather than reported as a pass
judge  Row `:30` was TRUE at `e71ecd5` and the next commit voided it. Row `:29` was true at
       NEITHER -- `468 + 24 passed` means 492 passed and 0 failed, and `e71ecd5`'s own CI run lists
       eight reds in those same three files, so that figure was taken before the commit it
       describes existed, which is CZ1's reusable half verbatim. Rows `:31` and `:32` I measured
       and they are TRUE at ce5a84f (85 passed; ruff, black and mypy clean). Row `:28` carries its
       own sha and is honest about being `a3a30d2`'s.
```

**The silently wrong result.** `docs/closure/R2-step0.md` is the one file written to answer "which
gates passed when step 0 closed" -- `CLAUDE.md`'s working agreement mandates the artifact for exactly
that -- and an auditor asking that question is told five gates were green. Two were red at the commit
publishing the answer: the three report-guard files at `8 failed, 481 passed`, and the carry gate at
`exit 1`, failing about **R1243, the step's only open blocking item, which is to say the one item the
carry mechanism exists to stop anyone dropping.** Nothing else in the artifact and nothing in the
tree says so: `docs/closure/**` is outside `tests/test_tree_prose_consistent.py:99`'s `ROOTS`,
outside the number-sourcing guard's domain, and the only automated reader of a closure artifact
checks path existence. **This is CZ1's own failure mode with the artifact substituted for the
report** -- "two classes of red shipped in `8e4238d` ... nothing between it and the next step's
report measures it". The sentence at `:34-36` sits inside the same
blind spot and I state its status precisely rather than lumping it in: *"The two failures are the
whole of the FQ3 escalation ... neither is clearable by any edit of the implementer's"* is TRUE of
`a3a30d2`, which the row above it names, and false of the commit publishing it, where the failures
are ten and eight of them clear -- at a verdict. It is the row's operating point doing the work, and
only one of the five rows carries one.

*Closed when* every row of that table either states the commit it was measured at and its true result
there, with the two boundary reds recorded red and traced per id as EG3 (i) requires, or is removed
in favour of a pointer to where CZ1's outputs actually live. Measured after the last edit to the
artifact rather than before it (CP3). One table, in the CZ1 (iv) follow-on that is owed anyway.

**R1250. (BLOCKS) `tests/test_report_carried.py:3054` CANNOT SEE A STEP CLOSURE ARTIFACT, SO AT THIS
CLOSING COMMIT THE TWO FC1 GUARDS PASS WHILE READING A WHOLE-SUITE FIGURE MEASURED THREE COMMITS
EARLIER.**

```
claim  `Closes: R2/step-0` routes the CZ1 guards to the closure artifact's block (FK2)
cmd    python -c "import sys;sys.path.insert(0,'tests');import test_report_carried as t;
       print(t.MILESTONE, t.CLOSURE.name, t.CLOSURE.exists(), t._newest_verdict_closes());
       print(t.cz1_record()==t._newest_revision(t.REPORT_TEXT), t._suite_line())"
out    R2  R2.md  False  R2/step-0
       True  ('a3a30d2', 3970, 2, 0)
cmd    ls docs/closure/
out    F2-step4.md F2-step5.md F2-step6.md F2-step7.md ... R1.md R2-step0.md
       -- five artifacts named `<MILESTONE>-step<k>.md`, which is this repository's own convention
cmd    grep -rn '"-step\|}-step\|-step{' tests/*.py scripts/*.py
out    (no match)
rule   `cz1_record`'s own docstring -- "Returns `""` when this increment is closed and the artifact
       has no block, so the guards fail with their own messages rather than falling back to a step
       report whose older line would answer in their place. That fall-back is R803, and it failed
       GREEN."
judge  The increment IS recorded closed and the artifact DOES exist -- under the step name, which
       `f"{MILESTONE}.md"` cannot produce. So `CLOSURE.exists()` is False, the router takes its "no
       artifact" branch, and the guards read the step report. **The collection the check inspects
       cannot contain the artifact it is looking for**, which is a fourth instance of the family the
       comment eighteen lines above that constant enumerates three instances of.
```

**The silently wrong result.** At the closing commit `test_the_report_carries_a_WHOLE_SUITE_count` is
GREEN on `Whole suite at a3a30d2: 3970 passed, 2 failed, 0 skipped` -- `a3a30d2` is verdict 64's
commit, three commits before the artifact -- and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` is
GREEN on the report's CI table, which describes `e87b2c0`'s run. Both guards exist to hold a CLOSURE
COMMIT's CZ1 record in place. At a closure commit they report green about a commit that is not the
one they are supposed to be measuring, and **a closure commit that shipped CZ1's outputs nowhere at
all would get exactly the same green.** It is also the mechanical reason this closure commit had
nowhere legal to put CZ1 (ii)-(iv): the artifact is invisible to the router, the report is sealed by
EK3, and so the outputs went into a commit message, which no guard and no reader of the record reads.

*Closed when* `CLOSURE` is resolved from the `Closes:` value -- `R2/step-0` giving
`docs/closure/R2-step0.md`, falling back to `docs/closure/<MILESTONE>.md` -- so that an existing step
artifact WITHOUT a `<!-- cz1-closure-outputs -->` block reaches the `""` branch the docstring already
describes instead of the report. **Solved in both directions as EH4 requires**, one measurement each:
a step artifact WITH a block routes to it and the suite line is read from there, and one WITHOUT a
block turns those two guards RED rather than green. This is the repair of a guard that passes false,
not an extension and not new apparatus (EK2), and FF0 puts it in the next commit.

**R1251. (ledger, FR1 -- no wrong result follows) THE "EIGHT LINES" FIGURE IS WRONG AT EVERY COMMIT IN
PLAY, AND IT SITS IN THE TWO PLACES CW0's ENFORCEMENT CANNOT REACH.**
```
cmd    grep -n "AND RUNG 6 RUNS BEFORE RUNG 4 (CH3)\|asserts that position\|R1243 REVERTS\|
       the comment eight lines above" .github/workflows/ci.yml
out    496 (CH3 begins) | 502 (CH3's last line) | 527 (the new block begins)
       528: "# comment eight lines above this one says so, and I reordered the steps without"
cmd    git show 2e08766:.github/workflows/ci.yml | grep -n 'name: "ladder 6'
out    527    -- the step the reorder moved, so the distance from CH3's last line (502) is 25 and
              from its first (496) is 31. It is 8 at no commit in this step.
rule   CW0 -- a claim about this repository in a comment is a test, a triple, or deleted
```
`docs/closure/R2-step0.md:98` carries the same figure ("recorded eight lines from the edit"), and my
own verdict 65 wrote "four lines above the line I edited", which is also not 25. **Nobody measured it
and three documents repeat it.** The reason nothing caught it is worth the line:
`tests/test_tree_prose_consistent.py:99`'s `ROOTS` is
`("floatfea","tests","scripts","docs/milestones","docs/verification")`, so `.github/` and
`docs/closure/` are both outside the one guard that enforces CW0 -- and those two files carry some of
the densest claim-prose in the repository. **Recorded, and explicitly NOT an apparatus request:** it
goes on `docs/milestones/F2a.md`'s frozen list if it goes anywhere.

**R1252. (ledger) THE ARTIFACT'S ROUND ARITHMETIC DOES NOT ADD UP, AND ITS "NINETEEN" IS A DIFFERENT
QUANTITY.**
```
cmd    sed -n '5,6p' docs/closure/R2-step0.md
out    "It consumed all three ES0 revisions and five reviewer rounds (three interim checks, which
        count against none, plus three reviewed revisions)."             -- 3 + 3 = 6
cmd    grep -c "^# Review" docs/reviews/R2/step-0.md ;
       grep -c "^# Review â€” R2 step 0 â€” ES0 INTERIM CHECK" docs/reviews/R2/step-0.md
out    7   4    -- 3 revision entries plus 4 interim entries over 3 distinct interim commits
                  (`3d24e1c` carries two, the second an addendum to the first)
cmd    grep -oE "R1[0-9]{3}\. \(BLOCKS\)" docs/reviews/R2/step-0.md | sort -u | wc -l
out    10   -- against `:168`'s "nineteen blocking findings"
```
`19` does occur in that file, as the count of RED REPORT-GUARD IDS at `91c2d2e` -- "19 failed, 320
passed", with CI's identical selection giving the same nineteen. A count of red ids and a count of
blocking findings are different quantities. I state the measurement and attach no cause to it.

**R1253. (ledger) THE ARTIFACT DROPS THE SCOPE ON THE ITERATION FIGURE, AND IT ERRS IN THE SAFE
DIRECTION.** `docs/closure/R2-step0.md:17-19` reads "Loop gain `g = kÂ·m_steel/m_body` is 0.53-0.77,
so the loop converges **monotonically** and 11-14 iterations are needed to reach D3's 0.5 % band."
The report's own table is per group and scopes it correctly.
```
rule   docs/reports/R2/step-0.md:109-113 -- n = ln(0.005/e0)/ln(g), e0 = 0.178
out    platform 2.5/0.18  g 0.767  13.5 | platform 3.0/0.12  g 0.732  11.4
       hub 2.5/0.18       g 0.673   9.0 | hub 3.0/0.08       g 0.535   5.7
cmd    re-derived independently from the four gains: ln(0.005/0.178)/ln(g)
out    13.47, 11.45, 9.01, 5.71      -- the report's table is right to the digit
```
`11-14` is the PLATFORM range; the artifact attaches it to the whole gain range, where two of four
rows are 5.7 and 9.0. It over-states iterations for the hubs, so the error is conservative, and that
is why it is a ledger row and not a block.

**R1254. (ledger, FR1's second non-blocking class -- a needle too narrow where no wrong result
follows) RUNG 3's PHANTOM-CITATION GUARD CANNOT SEE `scripts/`, WHICH IS WHERE THIS ARTIFACT'S
CITATIONS MOSTLY ARE.** `tests/verification/rung3/test_closure_evidence_exists.py:45`'s `_PATH`
matches `(?:tests|floatfea|docs)/...\.(?:py|md)` only. Measured on a plant: replacing the cited
`scripts/untouched_sites.py` with `scripts/untouched_sites_v2.py`, which does not exist, leaves **200
passed, 0 failed** -- so the G1.1 failure that file's own docstring names ("a gate recorded PASS
against a phantom test") is invisible for `scripts/`, `data/`, `results/` and `.github/`. No wrong
result follows today: I checked all ten path citations in the artifact one by one and all ten
resolve. **Widening the needle would be an EXTENSION of an existing guard, which EK2 forbids, so this
is recorded and routed to `docs/milestones/F2a.md` rather than requested.**

**R1255. (ledger, same class) THE LADDER's STEP ORDER IS ASSERTED FOR RUNGS 3, 4 AND 6 AND FOR
NOTHING ELSE, SO RUNG 1 CAN BE MOVED TO THE END OF THE JOB AND THE TREE STAYS GREEN.** This is the
adversarial case on this commit's own subject: the diff chose rungs 4 and 6, so I moved the rungs it
did not choose.
```
rule   tests/test_ci_determinism_gate.py:197 --
       where = {n: i for i, step in enumerate(order) for n in ("rung3","rung4","rung6") if n in step}
       -- and the two assertions beneath it, at :199 and :204, are the only position claims there are
cmd    five plants, one at a time, against tests/test_ci_determinism_gate.py +
       test_ci_ladder_gating.py + test_ci_workflow_is_wellformed.py + test_ci_runs_the_whole_suite.py
out    BASELINE                                  87 passed, 0 failed
       rungs 1 and 3 swapped                     87 passed   NOT CAUGHT
       rung 1 moved to the END, after rung 5     87 passed   NOT CAUGHT
       rung 2 moved after rung 6                 87 passed   NOT CAUGHT
       `full:tests/regression` moved onto rung 4 87 passed   NOT CAUGHT
       rung 5's step deleted                     2 failed    CAUGHT -- and by
         `assert len(order) >= 6` at :196 plus the naming check, not by anything about position
```
`CLAUDE.md` section Testing says "a failure at a low rung makes higher rungs uninterpretable", and
CK0's comment says the step order IS that rule now that six jobs are six steps -- so the rule is
asserted for half the ladder. **The fourth plant is the one worth naming: moving
`full:tests/regression` onto rung 4's step is R1243's own silently-wrong-result mechanism, reproduced
in a single line, reaching a green tree.** **Not blocking: no step in this diff moves, every rung's
position at the judged commit is CH3's, and no wrong result follows today.** Recorded with the batch
and routed rather than requested.

## The four rulings you asked for

1. **Is R1243 closed?** The CONDITION is discharged -- exit 1 taken; the order verified to be CH3's
   by byte diff, by line numbers at the pre-reorder commit and by CI's own step list; the record
   present in the artifact; the two contradicting comments reconciled; and the half of my condition
   that named a sealed report site WITHDRAWN by me. **The FORWARD item is not closed and was never
   going to be closed here:** chaining hides a rung in either order, and it carries into step 1 by
   name, still blocking.
2. **Is the EK3 correction the right shape?** Yes, and the restore is exact -- `git diff 0fb8c93 HEAD
   -- docs/reports/` is 0 lines, which I ran rather than accepted, and `step-0-answers.json` is
   restored with it. **One thing should also have moved and did not:** R1245's and R1246's repairs
   lived in the report, the restore reverted them, and the hand-back still reports them done. The
   artifact is now their only legal home. Nothing else should have moved: touching the report was
   unavoidable once `e71ecd5` existed, and the red it leaves is the commit-time comparison, which no
   arrangement of bytes could have avoided.
3. **Is anything in `docs/closure/R2-step0.md` wrong?** Yes -- R1249, which blocks, and the ledger
   rows R1251-R1253. What is RIGHT, because a list of defects is not an answer: all ten of its path
   citations resolve, measured one by one; every engineering figure in it traces to the reviewed
   report, and three I re-derived independently -- the gain/iteration table to the digit,
   8 x 25.93 min = 3.46 h against its "â‰ˆ 3.5 h", and 11-14 x 25.93 min = 4.75-6.05 h against the
   report's "4.8-6.0 h"; the two ladder rows in it and in `ci.yml` are confirmed from the CI logs
   themselves (1276+66+325+477 = 2144 collected, 1 failed, so 2143 passed; 1276+66+325+345 = 2012,
   so 2011 passed; -477/+345 = -132 with the same `1 failed`); the `untouched_sites.py` docstring
   quotation is verbatim and that script predates the step (`git log --diff-filter=A` gives
   `8beb0e4`); and (d)'s direction is right -- a lighter system needs ballast ADDED to hold draft.
4. **Is the carried list right?** R1243 to step 1 and R1232 to the write run: correct. R1248 to step
   2: correct, and checked against `docs/milestones/R2.md:313-330` rather than accepted. R1245 and
   R1246: **misrouted in the one way that mattered -- they were routed to the report, which EK3
   seals.** They go to the artifact. R1247: reviewer-side, and I added a fourth hole to it myself.

## Tolerances touched

**None, measured twice.** `git diff e511161..ce5a84f -- floatfea/tolerances.py` is **0 lines** and
`git diff e511161..ce5a84f | grep -cE '^[-+].*_COUNTER'` is **0**, so **EU1 does not arise** -- and I
ran the apparatus at configurations the diff did not choose anyway, which is where R1255's five
ladder plants came from. The one tolerance-shaped thing still implicated has not moved: `--check`'s
`np.array_equal` with no threshold, by Q8's rule. **If any answer to the escalation introduces a
tolerance on that comparison, that is a widening and it is refused.** R1218's row-1 form question
becomes blocking at step 2.

## Corpus

**Two batches, committed separately from this verdict.** GC3 left the pause expired, so the batches
are my own call under GA3's length target.

**(1) `tests/corpus/closure_artifact_published_as_green.txt` -- 38 entries, all new. 10 measured this
round, 1 CAUGHT, 9 reach a green tree.** It is the axis none of the existing corpora has.
`tests/corpus/report_record_freshness_and_completeness.txt` is the right family -- "a GENERATED record
that was TRUE WHEN GENERATED and is FALSE WHEN READ" -- and `grep -c "docs/closure"` over it is **0**;
all 26 of its entries are about a step report, as are those of `report_ci_section.txt`,
`report_numbers_sourced.txt` and `report_guard_states.txt`. The closure artifact is the weaker half of
that pair: the report has three guard files parametrised over it and the artifact has none. Baseline
for the selection used (`rung3/test_closure_evidence_exists.py` + `test_collected_set_golden.py` +
`test_tree_prose_consistent.py`): **200 passed, 0 failed.** The nine that reach a green tree are a
wrong number in a gate row, a gate row inverted while still reading as a pass, a row naming a gate
that does not exist, the whole-suite row deleted, a sha that is not a commit, an engineering figure
moved by an order of magnitude, a false `claim:/cmd:/out:` triple appended to the artifact, a row
attributed to a different commit, and a cited `scripts/` path that does not exist. **The one catch**
is removing every path citation, which `test_the_artifact_cites_evidence_at_all[R2-step0]` sees,
because it is an existence check.

**(2) `tests/corpus/ladder_step_order_the_gate_does_not_assert.txt` -- 13 entries, all new. 5 measured,
1 CAUGHT, 4 reach a green tree.** The counts are in R1255. **The baseline subtraction is part of the
measurement and this time it is clean**: unlike last round, `test_ladder_6_is_not_gated_behind_a_rung_
that_is_red_under_Q8` is green at the judged commit because of the revert, so a plant that reddens is
unambiguously caught and a plant that does not is unambiguously missed. That is the one thing the
revert bought the corpus, and it is worth saying, because last round four workflow plants "looked
caught" against an already-red tree.

**What I ran beside the batches** is the recorded substitute, both halves, and **both of this round's
blocking findings came out of them rather than out of reading the diff.** A continuum over the
parameter space a decision rule guards: the `Closes:`/`CLOSURE` router, swept over the four states its
own comment enumerates plus the fifth nobody had -- an artifact that exists under the step's name --
which is R1250. And a regeneration check on a published deliverable: the closure artifact itself,
re-measured gate by gate at its own commit, which is R1249.

## Next step opens when

**STEP 0 STAYS CLOSED (DD1). THIS HOLD IS ON THE CLOSURE COMMIT AND NOT ON THE STEP**, and it consumes
none of step 0's three ES0 revisions (EB4). Verdict 65's `Closes:` line is untouched and is still the
one the FC1 router reads; **this verdict carries no `Closes:` line, as FK1 requires of a verdict that
closes nothing.** Step 1 is held by GI6 until Xabier confirms or overrides D1-D4, and by R1243,
independently of anything here.

1. **R1249 and R1250, in the CZ1 (iv) follow-on commit that is already owed** -- one table and one
   path resolution, each with the inversion EH4 asks for. CZ1 (iv) says a closure commit is not
   finished until a pushed run at its own sha, or at the follow-on's, is green or has every red
   traced. **`ce5a84f`'s run at `44196001239` has concluded FAILURE and I have traced all nine of
   its reds above, so (iv) is satisfied on the CI half by this verdict rather than by a follow-on**
   -- what the follow-on owes is the two findings and a run of its own.
2. **CZ1 (ii)-(iv) at `ce5a84f`'s own sha, in the place CZ1 names for a closed report: step 1's
   report `Carried`** -- "where that report is already closed, in the next report's Carried" -- and
   not in a commit message. **Three of the four outputs, and the `gh run list` of CZ1 (iii), are
   already measured at that sha in my Tests and CI sections above and may be taken from there; the
   one still owed is your own `pytest -q` at `ce5a84f`, which you said was running.** When you paste
   it, the nine reds above are what it should contain and nothing else -- a tenth is CZ1 (iv).
3. **R1245 and R1246 move to `docs/closure/R2-step0.md`**, the only home EK3 leaves them. Two lines,
   fixed once as part of the list and not re-reviewed item by item.
4. **R1243 appears by name in step 1's `Carried` and stays blocking there** until the chaining is
   fixed and that fix is reviewed.
5. **The escalation's conditions are unchanged.** Do not clear the staleness guard by regenerating the
   npz; do not clear R1223 by regenerating the deliverable against a red gate. Five rounds of
   declining the cheap wrong repair is still the best evidence this step has produced.
6. **Two report sites are DECLARE-ONLY, and I name the constraint because I created the sites.**
   `docs/reports/R2/step-0.md:1616` and `:1629` are named in this verdict and EK3 forbids touching
   them, so step 1's report declares them `**no change** -- EK3` rather than reaching for an edit it
   is not allowed to make.

**Nothing here is a STOP, and I considered it on the ladder.** No `floatfea/` file is in this diff; no
tolerance moved; rungs 1, 2 and 3 are SUCCESS in CI at `e71ecd5`'s own run over code byte-identical to
the judged commit's in every path the ladder reads; the locked plan is untouched and faithful to GI.
Rung 4's red is the provenance comparison that is escalated, and rungs 4 and 5 did not execute, which
is R1243 carried rather than a rung failure.

**And I disagree with nothing in the criterion.** FR1 did the work again: five of this round's seven
findings are single lines here instead of rounds, and the two that block are each given the sentence
FR1 asks for -- a closure record that answers "which gates passed" with two gates it cannot have seen
pass, and a pair of gates reporting green about a commit three earlier than the one they exist to
measure. **What I would say to Xabier if asked, in one sentence, is not a criterion complaint:** the
honest account section of the artifact is the best thing in this step's record, and the table four
screens above it is the worst, and they are the same document.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0
Reviewed commit: 0fb8c936e2043d954d6661140b03fbdabcb27273
**Reviewed commit: `0fb8c936e2043d954d6661140b03fbdabcb27273`.**
Closes: R2/step-0
Verdict: PASS
Scope: **R2 step 0, REVISION 3 -- the THIRD AND LAST reviewed revision ES0 allows, so this
verdict CLOSES the step** (`--closes R2/step-0`, FK1). Ruled under **FR1 with EZ0**: each
blocking finding names the silently wrong result it produces, and the narrowing is this
milestone's own -- `docs/milestones/R2.md:32` carries *"Blocking stays FR1 -- a silently
wrong result"*. **GE3: `R835: unchanged, R2`. Not re-measured.**

**ITEM 1b PASSES.** One comparison, made:
```
cmd    sed -n '1516p' docs/reports/R2/step-0.md ; git log --oneline -1 -- docs/reviews/R2/step-0.md
out    Answers: verdict 64 @ a3a30d2
       a3a30d2 review: R2 step 0 REVISION 2 at e87b2c0 -- HOLD, two blocking findings
cmd    python -c "import test_report_carried as t; print(t.ANSWERED, len(t.EXPECTED))"
out    a3a30d2 35      -- and the generated table at sec.19b has 35 rows, counted
```
The newest revision's header names the newest verdict. Lines 5 and 704 still read 61 and 63;
both are correct as the record of their own rounds and the guard reads `_newest_revision()`.

**4 / 4b / 4c, each diffed separately against `a3a30d2`:** `floatfea/tolerances.py` **0
lines**; `.claude docs/SUPERVISOR.md` **0 lines, so no STOP-class finding**;
`tests/conftest.py` **0 lines**, and `git ls-files -- tests/conftest.py 'tests/**/conftest.py'`
returns `tests/conftest.py` as it must -- no new conftest, no new plugin. **EU1 does not
arise, measured not taken:** `git diff a3a30d2..HEAD | grep -cE '^[-+].*_COUNTER'` is `0`.
`git diff --name-only a3a30d2..HEAD -- floatfea data results docs/F6_utilisation.csv scripts/measure`
is **empty** -- no tool change, no write run, no re-based npz, no regenerated deliverable.
The step's whole `floatfea/` diff since the plan lock is still one file, `hsp_pin.py`, which
is what the plan allows.

Tests: **1646 passed, 3 failed, 0 skipped -- MY OWN RUNS, in my own worktree at the judged
sha, `-p no:randomly`.** Two of the three reds are the escalation; **the third is new and it
is R1243.**
* `tests/test_report_numbers_are_sourced.py` + `tests/test_report_carried.py` -> **465
  passed** (446 + 19). `tests/test_report_guard_states.py` -> **24 passed in 89.59s**. Those
  are your figures exactly, and **all three report-guard files are green for the first time
  in this step.**
* FV1 selection -- `tests/unit`, the four root guards, `tests/verification/rung4`,
  `tests/regression/test_f6_deliverable_agrees_with_itself.py` -> **2 failed, 1071 passed in
  321.89s**, the two being `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`. The escalation, by
  name, and nothing else.
* **`tests/test_ci_determinism_gate.py` -> 1 failed, 12 passed.** The file the diff's own
  change is about, and it is not in your stated FV1 selection. See R1243.
* `tests/test_ci_ladder_gating.py` + `test_ci_runs_the_whole_suite.py` +
  `test_ci_workflow_is_wellformed.py` -> **74 passed.**
* `python scripts/check_carried.py` -> **all 28 findings carried, exit 0.** `ruff`,
  `black --check`, `mypy floatfea` -> clean (163 files unchanged, 45 source files).
* **NOT RUN LOCALLY, and I say which rather than implying coverage:** rungs 1, 2, 3, 5, 6 and
  the rest of `tests/regression`, and the whole suite. `git diff --name-only a3a30d2..HEAD --
  floatfea` is empty, so FV1 puts them on CI; CI ran rungs 1-4 at `772f616` and rungs 1, 2, 3
  are SUCCESS there. **Rungs 5 and 6 did not run in CI either, and that is R1243.**

CI: **the judged commit `0fb8c93` HAS NO RUN AND CANNOT HAVE ONE. GC2's case, both conditions
measured.**
```
cmd    gh run list --commit 0fb8c936e2043d954d6661140b03fbdabcb27273 --json name,conclusion,workflowName
out    []
cmd    git diff --name-only 772f616..0fb8c93
out    docs/reports/R2/step-0.md     -- the only path, and `docs/reports/**` is in ci.yml's
                                       paths-ignore (CK0)
```
So the evidence is the nearest ancestor with a run: **run `44180156206` at
`772f616bfac3e20455c04764be3666d04b9f5fdf`, `completed`, conclusion FAILURE.** **NOT CK2** --
both executing jobs were given work and ran. The two determinism jobs are `skipped` by their
own `workflow_dispatch` condition: unavailable, not passing.
```
the verification ladder   failure   rungs 1,2,3 SUCCESS | rung 4 FAILURE | rungs 5,6 SKIPPED
lint, unit and guards     failure   17 FAILED ids
```
**EVERY CI RED TRACED PER ID FROM ITS OWN MESSAGE (EG3 (i)), AGAINST THE FS1/FT1 PREDICATE,
AND SIXTEEN OF SEVENTEEN CLEAR AT THE JUDGED COMMIT -- MEASURED, NOT ASSUMED.**
```
8   test_every_named_site_is_touched_or_declared[R1221|R1242-tests/test_report_carried.py:387..390]
      -> names a FINDING and a SITE of verdict 64. Limb one. GREEN at 0fb8c93 (465 passed).
7   test_the_guard_survives_the_state[baseline | non_numeric_step_suffix |
    superscript_digit_step_number | draft_suffix_beside_a_step_report |
    step_number_is_the_empty_string | verdict_amended_after_the_commit_the_report_answers |
    zero_padded_step_number]
      -> EG3 state (2). Limb one. GREEN at 0fb8c93 (24 passed).
1   test_every_number_in_prose_is_sourced_in_its_own_section[19. ...]
      -> section 19 IS verdict 64's answer section. Limb one. GREEN at 0fb8c93.
1   rung4 ... test_the_npz_is_NOT_STALE_against_the_code_that_generated_it
      -> names R1225/R1223, carried by verdict 64, at the site it named. Limb one. The
         escalation; red at 0fb8c93 with its cause named, and correctly not cleared.
1   test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8
      -> FAILS BOTH LIMBS. Names no finding and no site of verdict 64; its subject is the
         workflow's step order, not the commit carrying it. STILL RED at 0fb8c93.
         CZ1 (iv) applies unchanged. This is R1243.
```
**The test I used to separate "boundary" from "introduced": a boundary red is SELF-CLEARING
-- EG3's own word for both of its states. The sixteen above cleared, and I measured them
clearing. This one does not clear at any future commit until the order is settled.**

Door (FV2 / GG2): `git worktree add -b review/0fb8c936e204 <a path outside the repository>
0fb8c936e2043d954d6661140b03fbdabcb27273` **succeeded on the first try, so no review of this
commit existed.** Every measurement was taken there; the corpus is committed separately at
`30e3c56` and this verdict is written through `scripts/write_verdict.py`, committed on that
branch and pushed -- merge with `git merge --ff-only origin/review/0fb8c936e204`. **My own
writes, all in my own worktree, all reverted before committing:** one Carried row removed, one
`no change` row planted, four `ci.yml` plants, two `data/platform/buoy_centers_ref.json`
regenerations, with `git status --porcelain` empty after each. `C:\dev\floatfea` was clean when
I was invoked and I wrote nothing into it. **And one of my own measurements was wrong and I
caught it before writing it down:** my first "empty directory named `HSP-stable`" probe ran
against a POPULATED fake a previous round of mine had left in the same scratch directory, so
`mkdir -p` was a no-op and the fixture was not what I believed. Re-run on a genuinely empty
directory the code refuses correctly. The entry in the Corpus section is the controlled plant,
not that first probe.

## Carried

Verdict 64's five numbered conditions and its carry list. **FOUR ANSWERED, ONE ANSWERED INTO A
NEW BLOCKING FINDING, TWO CORRECTLY UNCHANGED, AND TWO OF MY OWN CLAIMS WITHDRAWN.**

* **R1238 -- ANSWERED AND CLOSED, and this is the cleanest answer of the round.** Sec.20's
  fenced block is the generator's output with **10 bullets = 2 + 8**, equal to the two counts
  in its own line, counted by me. `splice3.py` now exits non-zero on a bullet/line mismatch, on
  a file that would shrink, and on a vanished site row -- three defects of this step turned
  into preconditions on the script that caused them, which is the right place for them.
* **R1240 -- ANSWERED AND CLOSED, at both sites, and the repair carries its own failure.**
  `tests/test_report_carried.py:380` and `scripts/carried_table.py:160` both scope to the
  newest `# Review` entry. **I measured the repair rather than reading it:** deleting the
  R1217 row -- one of the ids the repair brings into scope -- gives `2 failed` at
  `test_the_report_carries_the_finding[R1217]` and
  `test_the_Carried_table_is_what_the_generator_produces`, so the newly-covered ids are
  genuinely inside the gate's domain and the generator/gate pair agrees. **And your correction
  to my reason for the third site is right and I verified it line by line:**
  `scripts/check_carried.py:80`'s `heads[-1]` is on the REPORT path, scoped at `:73-80`, where
  the last heading IS correct; what makes it immune is that `:145` is
  `set(_FINDING.findall(...))` and extracts no Carried section from accumulated text at all.
  Recording the distinction rather than the conclusion is what tells the next reader whether a
  fourth site would be a site, and you wrote it that way.
* **R1241 -- ANSWERED at both named sites**, and the rewrite into a `claim/cmd/out/rule/judge`
  block rather than prose was the right call: the number-sourcing guard was red on the two
  figures inside the first correction, which is CP2 exactly -- a repair's own numbers carrying
  no triple. One site of the same class is left: sec.15's judge still reads *"this reads the
  SAME `SITES` the gate reads rather than reimplementing the pattern and getting a different
  answer from the thing it has to satisfy"*, and the eight reds of `772f616` are the
  measurement that it reimplemented the TOUCHED half. Closure item.
* **R1242 -- correctly a ledger row, unchanged.**
* **R1237 -- THE MECHANISM IS ANSWERED AND DEMONSTRATED; THE NAMED SITE IS NOT, AND I NARROW MY
  OWN CONDITION RATHER THAN HOLD YOU TO IT.** The ordering is real -- all four runs concluded
  first, then each generator to its own file, then the paste, then the commit -- and sec.20 is
  the proof: I verified its nine failing ids against `gh run view 44164723945 --log-failed` and
  the eight lint ids match exactly, with `test_R756` the ninth from the ladder. GC2 was handled
  correctly for `e87b2c0`, with both shas, the diff listing and the run id printed. **But the
  site my condition named is unchanged:** `docs/reports/R2/step-0.md:813` still reads
  `| 44145793006 | push | 0c5c864 | **no result** (status in_progress) |` and `gh` says
  `conclusion=failure, updated 18:58:00Z`; `44149168617` has no row in that table. Your
  hand-back says "the rounds table now reads `conclusion **failure**` for the run it had
  published as 'no result'" -- **that is true of sec.20's table and of a different run, and it
  is not true of the run and the row the finding named.** I am not holding on it, for a reason
  I can state: **it is no longer silent.** Sec.17 declares, in the report's own words, that the
  row said no result where `gh` says failure and that the table was incomplete, and sec.19b's
  generated row points R1237 at sec.17. Under FR1 that makes it a ledger item, not a blocking
  one. And leaving the row is defensible on the ground verdict 64 itself used for revision 1's
  `Answers:` header -- a revision is the record of its round. What is missing is the pointer AT
  the site: sec.17 never names run `44145793006`, so a reader at line 813 has nothing to
  follow. One line, in the closure artifact. **R1244.**
* **R1239 -- ANSWERED IN FORM, AND THE FORM OF THE ANSWER IS A NEW BLOCKING FINDING. R1243,
  AND THE FIRST EXIT OF MY OWN CONDITION IS WITHDRAWN.** I offered "either the two existing
  steps move ahead of rung 6 -- a reorder of steps that already exist, so no new apparatus is
  created -- or the report records that rungs 4 and 5 are unmeasurable in CI". **The first exit
  is not available and I did not know it when I wrote it**: `ci.yml:496-503` carries CH3, which
  put rung 6 ahead of rung 4 deliberately and for a measured reason, and names
  `tests/test_ci_determinism_gate.py` as the gate that asserts the position. You took the exit
  I named, which was the right thing to do with a reviewer's condition; the condition was
  wrong. **And I withdraw a second claim of my own from the same finding:** R1239's judge said
  *"Nothing is published wrongly -- a skipped step is recorded as skipped"*. Measured at
  `scripts/ci_section.py:473-505` and `:628-653`: the counts come from `run_rung:` log lines
  and the SKIPPED notice is keyed on `job["conclusion"]`. **A skipped STEP emits no log line
  and is named nowhere.** I asserted it and did not run it; that is the pattern this step has
  been about all month and this instance is mine.
* **Conditions 4 and 6 (R1225, R1223) -- OPEN, UNCHANGED, AND CORRECTLY SO.** Both red in my
  own run with the cause named; `git diff --name-only a3a30d2..HEAD -- data results` is empty.
  **Fourth round running in which the cheap wrong repair was available and not taken.** Sec.7
  states both options with both costs and leaves the choice where it belongs. This is the part
  of the step that is actually good, and it is what GI6 sends to Xabier.
* **Condition 5 (R1232) -- NOTHING TO DO, and nothing was done.** No write run was made.
* **R1217, R1218 -- still open and not answerable here**; R1218 becomes a blocking item when
  step 2 writes the tolerance entry. **R1212, R1203, R1204, R1222, R1224 -- reviewer-side or
  Xabier's; no action asked of you. R1234 -- withdrawn by me last round, stays withdrawn.
  R835 -- `unchanged, R2` (GE3), one line.** The R1213 message assertion stays a ledger row.
* **Verdict 58's twelve and verdict 59's four -- ROUTED, and now held in place by a gate that
  reads the right round**, which is what R1240's repair bought.
* **THE THREE-INSTANCES LESSON: YES, IT BELONGS IN THE CLOSURE ARTIFACT, and it is stronger
  than you put it.** R1221 (filter), R1240 (scoping) and `772f616`'s eight reds (the
  touched-line predicate) are three instances of one shape, each found by running the pair
  rather than reading either. **The fourth fact sharpens it into a rule:**
  `scripts/untouched_sites.py` is a COMMITTED generator for exactly the sec.19c table, it
  already reads `SITES` and `TOUCHED` from the gate, and it already REFUSES when the diff is
  unavailable (`TOUCHED_ERROR`, `:77-79`) -- and sec.15 and sec.19c were produced by an ad-hoc
  script instead, with no `<!-- generated: -->` mark on either section. So the rule is not
  "take the gate's value" but **"use the committed generator; where one exists, a second
  implementation is the defect, and the one you write will be the lenient one."** Both halves
  of that sentence are measured: lenient (`range(380, 405)` against `{379, 380}`) and
  already-solved (the committed script). Put it in the closure artifact in those terms.

## Findings

**R1243. (BLOCKS) THE RUNG REORDER BREAKS THE GATE THAT EXISTS TO PREVENT IT, AND IT TAKES THE
WHOLE OF `tests/regression` OUT OF CI. THE PREDICTION IT SHIPPED WITH IS REFUTED BY ITS OWN
RUN.**

```
claim  the rungs now run in the ladder's own order, and CI's ladder job goes from one red
       to two -- the second being the escalation becoming visible
cmd    python -m pytest -q -p no:randomly tests/test_ci_determinism_gate.py
out    1 failed, 12 passed
       test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8
       AssertionError: the goldens run after ladder 4, so a red ladder 4 stops them --
       which is where they were for eleven rounds, gated nowhere while running on ten
       determinism legs.   assert 5 < 3
cmd    sed -n '496,503p' .github/workflows/ci.yml     (UNCHANGED by this diff, four lines
                                                       above the comment that reorders it)
out    "AND RUNG 6 RUNS BEFORE RUNG 4 (CH3). The goldens ask whether today's bytes equal
        yesterday's, which stays interpretable whatever ladder 4 says; chained behind it
        they were skipped for eleven rounds while running on ten determinism legs ...
        `tests/test_ci_determinism_gate.py` asserts that position."
cmd    gh api repos/:owner/:repo/actions/runs/44180156206/jobs --jq '.jobs[] |
       select(.name=="the verification ladder") | .steps[] | "\(.name) -> \(.conclusion)"'
out    ladder 1,2,3 -> success ; ladder 4 -> FAILURE ; ladder 5 -> skipped ;
       ladder 6 -> skipped
cell   ONE VARIABLE, the step order, measured from the two runs rather than reasoned:
         44149168617  rungs 1,2,3,6   ladder row  2143 passed, 1 failed, 0 skipped
         44180156206  rungs 1,2,3,4   ladder row  2011 passed, 1 failed, 0 skipped
       -477 (rung 6 AND all of tests/regression), +345 (rung 4), net -132, SAME `1 failed`.
rule   FS1 with FT1 -- a red is a boundary red if it names a finding or a site of the newest
       verdict, OR if its SUBJECT IS THE COMMIT CARRYING IT
judge  **IT FAILS BOTH LIMBS, and it is not self-clearing, which is EG3's defining property
       of both of its states.** CZ1 (iv) applies unchanged. **And the prediction is refuted
       by the commit's own run: ONE red, not two.** Rung 4 fails, so rungs 5 and 6 skip --
       which is the very mechanism R1239 identified, applied to the repair for R1239. The
       escalation did not become visible; it MOVED, from the rung-6 deliverable red to the
       rung-4 staleness red, and the rung-6 one is now invisible in CI.
```

**The silently wrong result.** `scripts/ci_section.py` reads `job["conclusion"]` and parses
`run_rung:` lines out of the log. **A skipped STEP emits no `run_rung:` line, and the "N job(s)
SKIPPED, so unavailable rather than passing" notice is keyed on a JOB's conclusion** -- so the
next report publishes `the verification ladder | 2011 | 1 | 0` and nothing anywhere says that
477 tests did not execute. Among them is the whole of `tests/regression`, which FV1 assigns to
CI at the pushed sha in so many words, and
`tests/regression/test_f6_deliverable_agrees_with_itself.py`, **the only automated check that a
published deliverable still regenerates.** Under the previous order that check ran and reported
its red; under this one it cannot run while the escalation stands, and the figure that would
have told a reader so is a smaller number beside an unchanged `1 failed`. The gate that held
the property is the one now red, so the tree cannot say it either.

**And one thing it is NOT.** This is not a new-apparatus request and it is not an extension:
`tests/test_ci_determinism_gate.py` is not failing false. It is reporting, correctly, that the
order it asserts is gone.

*Closed when* **either** the CH3 order is restored and R1239's SECOND exit is taken -- the
report, or the closure artifact, records that rungs 4 and 5 are unmeasurable in CI while the
escalation stands -- **or**, if the new order is kept, `ci.yml:496-503`'s CH3 paragraph and
`tests/test_ci_determinism_gate.py:199`'s assertion are changed in the same commit with CH3's
own measurement answered, and the CI section names every skipped ladder step rather than only
skipped jobs. **Either way the stale CH3 comment goes** -- two adjacent comments in one file
currently assert opposite orderings -- **and sec.19's "ONE red to TWO" is replaced by the
measurement above.** This is FF0-class apparatus, so it is the NEXT COMMIT, which is the step's
closure commit; under EQ0 that commit changes a gate and I review it, and under EB4 that review
costs no round.

## Closure items

1. **R1244 -- `docs/reports/R2/step-0.md:813`.** The `44145793006` row stays as the record of
   its round; it needs one sentence AT the site naming the run and pointing at sec.17, because
   sec.17 never names the run id. And `44149168617`'s conclusion appears only inside sec.20's
   GC2 preamble, not as a row of the round it belonged to.
2. **R1245 -- two stale figures, both inherited from me, both one line.** (i) Sec.19's cell and
   `step-0-answers.json`'s preamble both read *"GAINS R1212, R1217, R1218, R1219, R1224 -- five
   items"*; **`R1219` is not in `EXPECTED` (35 ids) and has no row in sec.19b.** The figure is
   four, and it is four because **my verdict-64 cell measured the gain against verdict 63 while
   the repair landed against verdict 64** -- BP0, the rule moving under the figure, and the
   rule was my own newest-verdict pointer. (ii) Sec.19c's `out` reads `16 touched` and its
   `judge` reads *"among the 24 touched"*; measured, `len(SITES) - 229 = 16`. Both reach a
   green tree -- the number-sourcing guard is green with `24` in the judge line and with
   `R1219` in the prose, on the shipped artifact and not on a plant.
3. **R1246 -- sec.15 and sec.19c carry no `<!-- generated: -->` mark and were produced by an
   uncommitted script, while `scripts/untouched_sites.py` is the committed generator for that
   table.** BI3's rule is that a table is regenerated by a script at the commit it describes or
   it does not belong in that file. Sec.15's judge claim is the R1241-class sentence left over.
4. **R1247 -- three measured holes in the newest-entry scoper, all reachable from MY OWN
   wording, none caught by anything.** A newest entry with no `## Carried` heading empties the
   mention half of `EXPECTED`; a heading written `#Review` without the space makes the scoper
   read the SECOND-newest entry, which is R1240 re-entering through a typo; and a line reading
   `# Review` quoted inside a fenced `out` block truncates the entry before its real Carried
   section. The third is live for me -- I quote verdict text in `out` lines every round. Noted
   for the record, not as a repair request: the constrained party here is the reviewer.
5. **R1248 -- `scripts/export_buoy_centers_ref.py` checks the stable tree's NAME and never its
   TAG.** Measured on a controlled plant: a git tree at commit `8dfdc6c` with no tags, merely
   named `HSP-stable`, regenerates `data/platform/buoy_centers_ref.json` -- EB6's
   label-provenance input -- and the written file declares `hsp_tag: floatfea-ref-1` beside a
   `blob_sha` from that tree. `hsp_pin.worktree`'s docstring scopes itself out of tag checking
   deliberately and R1226 gave this file a NAME refusal, so the gap is documented rather than
   hidden, and the committed snapshot is untouched this round (`b8b8123904af`). It does not
   block -- no artifact in the tree was produced that way and the realistic error, pointing the
   stable key at `HSP-runs`, is refused loudly. **It belongs in step 2**, which is where the
   override file and its provenance get written, and it is FR1's second head the moment someone
   regenerates on a machine with a stale stable worktree.

## Tolerances touched

**None, measured twice.** `git diff a3a30d2..HEAD -- floatfea/tolerances.py` is **0 lines** and
`git diff a3a30d2..HEAD | grep -cE '^[-+].*_COUNTER'` is **0**, so **EU1 does not arise** -- and
I ran the apparatus at configurations the diff did not choose anyway, which is where R1243's
cell and R1240's both-direction measurement came from. The one tolerance-shaped thing still
implicated is not a tolerance and has not moved: `--check`'s `np.array_equal` with no threshold,
by Q8's rule. **If any answer to the escalation introduces a tolerance on that comparison, that
is a widening and it is refused.** R1218's row-1 form question becomes blocking at step 2.

## Corpus

**One batch, committed separately at `30e3c56`:
`tests/corpus/ci_step_skipped_inside_a_job_that_ran.txt`, 32 entries, all new.** GC3 left the
pause expired, so this is my own call under GA3's length target. It is the axis none of the
three existing CI corpora has: every entry in `report_ci_section.txt`, `ci_ladder_gating.txt`
and `ci_workflow_job_gating_shapes.txt` is about a JOB, and this round's blocking finding is
about a **step inside a job that ran.**

**10 of the 32 measured this round, one variable at a time in my own worktree, reverted after
each. 1 CAUGHT, 9 reach a green tree.** The one catch is dropping `full:tests/regression` from
rung 6's `run:` line, which `test_every_test_in_the_suite_is_run_by_some_ci_job` sees because it
is a NAMING check. The three that do not: `continue-on-error: true` on rung 4 (step fails, job
concludes success), `if: ${{ !cancelled() }}` on rungs 5 and 6 (CK0's own premise that "steps
stop at the first failure, so the chain is the order" silently falsified), and splitting
`tests/regression` into its own step behind rung 6 (still named, still gated on a rung that can
be red). Plus three on the verdict scoper and two taken on the SHIPPED artifact rather than a
plant -- the `24`/`16` judge line and the `R1219` prose row, both green.

**AND THE BASELINE SUBTRACTION IS PART OF THE MEASUREMENT, NOT BOOKKEEPING.** At this commit
`test_ladder_6_...` is already red, so all four workflow plants "look caught" if the `FAILED`
list is read without comparing it against the unplanted tree. Subtracting the baseline -- 1
failed, 86 passed -- leaves exactly one catch out of four. A corpus measured against a tree
that is already red over-reports its own coverage, which is a shape worth naming for the next
round.

**What I ran beside the batch** is the recorded substitute: a continuum over the parameter space
the carry gate's decision rule guards, solved in both directions (EH4) -- the weakening
direction found that a TOUCHED site declared `**no change**` leaves `test_report_carried.py` at
`446 passed`, which is the escape hatch working as designed and is why the reviewer reading the
table is the bound; and a regeneration check on a published-deliverable producer, which is
R1248.

## Next step opens when

**STEP 0 IS CLOSED BY THIS VERDICT (DD1, `--closes R2/step-0`). STEP 1 DOES NOT BEGIN: GI6
holds it until Xabier confirms or overrides D1-D4, and R1243 holds it independently.** Rounds:
this consumed **revision 3 of 3 under ES0 and the cap is reached**, so nothing here is a request
for a revision 4. R1238, R1240 and R1241 are **DISCHARGED**; R1237 is discharged in its
mechanism and ledgered at its site; condition 7 and R1234 stay **WITHDRAWN**, and the first exit
of R1239's condition plus R1239's own skipped-step parenthetical are **WITHDRAWN TOO**, both
mine, both with the measurement that forced it.

1. **R1243 in the closure commit, before anything else (FF0).** One of the two exits above, with
   the stale CH3 paragraph removed either way and sec.19's prediction replaced by the two ladder
   rows. **Under EQ0 I review that commit because it changes a gate; under EB4 the review counts
   against no step's rounds.** R1243 also carries by name into step 1's `Carried` and stays
   blocking there until that review passes.
2. **The closure artifact carries CZ1's four outputs at the closure commit's own sha** --
   `ruff`, `black --check`, `mypy`, `pytest -q`, then the pushed `gh run list`, with any red
   answered in a follow-on that repeats both. **And EG3 (ii): the report-guard files run AT the
   verdict commit and the counts recorded**, which is the half no verdict in this milestone had
   measured and which this step has now measured twice.
3. **The closure list above, items 1-5, fixed once as a list** -- not re-reviewed item by item.
   R1248 is the one to route forward rather than fix: it belongs to step 2's provenance work.
4. **Conditions 4 and 6 stay open and stay escalated.** Do not clear the staleness guard by
   regenerating the npz and do not clear R1223 by regenerating the deliverable against a red
   gate. Four rounds of not doing the cheap wrong thing is the best evidence this step produced.
5. **No write run until R1232's pin is above `import numpy` or in the invocation's
   environment**, with the provenance recording the pinned values.

**Why PASS and not HOLD, stated so it is not read as a caveat.** ES0's cap and CZ1 (iv) collide
here, and CLAUDE.md resolves the collision itself: *"A blocking item still open at that point
carries by name into the next step's `Carried` section and stays blocking there."* That sentence
presupposes a step closing with a blocking item open, which is this. A HOLD would demand a
revision the cap forbids and would rebuild DD1's deadlock, which this project has already paid
two verdicts for. And the honest part: **R1243 exists because the first exit of my own condition
was wrong** -- I named a reorder as safe without reading the comment four lines above the step I
was asking to move. Holding you for a round on a defect my own condition specified would be the
exact failure I named last round -- relaying a condition no action of yours can meet --
inverted. So: the step closes, the report goes to Xabier, and the two-line repair plus its
review happen in the closure commit where FF0 puts them.

**Nothing here is a STOP, and I considered it on the ladder.** Rungs 1, 2 and 3 are SUCCESS in
CI at `772f616` over code byte-identical to the judged commit's; no `floatfea/` file is in this
diff; and the escalation's two reds are a provenance comparison and a regeneration comparison,
not a numerical disagreement at a rung. Rung 4's red is that same provenance comparison and rung
5 has not run -- which is R1243, not a rung failure. The locked plan is faithful to GI and needs
no reopening, and section 6 item 2 of that plan is still the one clause I rule must NOT be
triggered yet.

**And I disagree with nothing in the criterion this round.** FR1 did the work again: R1244-R1248
would each have been a blocking round under the unamended CZ0 and each is a line here instead,
and the one that blocks is given the sentence FR1 asks for -- a published CI figure that
conceals 477 tests, including the only check that a deliverable still regenerates, never having
run.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0
Reviewed commit: e87b2c00a7cab740f27841f66e9362ac5248283e
**Reviewed commit: `e87b2c00a7cab740f27841f66e9362ac5248283e`.**
Verdict: HOLD
Scope: **R2 step 0, REVISION 2 -- a REVIEWED REVISION, not an interim check.** A new report
revision exists at `fa8d59c`, so under ES0 this is **2 of step 0's 3 revisions and ONE
remains.** It closes nothing, so `--closes` is correctly absent (FK1). **Ruled under FR1
with EZ0**, and each blocking finding names the silently wrong result it produces -- and the
narrowing is this milestone's own rather than an import from R1: `docs/milestones/R2.md:32`
carries *"Blocking stays FR1 -- a silently wrong result"* in the locked plan. **GE3: `R835:
unchanged, R2`. Not re-measured.**

**ITEM 1b PASSES, AND IT IS THE ONE THAT FAILED LAST ROUND.**
```
cmd    sed -n '698p' docs/reports/R2/step-0.md ; git log --oneline -1 -- docs/reviews/R2/step-0.md
out    Answers: verdict 63 @ 0c5c864
       0c5c864 review: R2 step 0 REVISION 1 at 4c19570 -- HOLD, two blocking findings
cmd    python -c "import test_report_carried as t; print(t.ANSWERED, len(t.EXPECTED))"
out    0c5c864 38      -- and the generated table at sec.12 has 38 rows, counted
```
One comparison, made, and it is right. Line 5 still reads `Answers: verdict 61 @ c931885`
and **that is correct**: it is revision 1's own header, left as the record of the finding,
with sec.11 saying so, and the guard reads `_newest_revision()`.

**4 / 4b / 4c, each diffed separately against `0c5c864`:** `floatfea/tolerances.py` **0
lines**; `.claude docs/SUPERVISOR.md` **0 lines, so no STOP-class finding**;
`tests/conftest.py` **0 lines**, and `git ls-files -- tests/conftest.py 'tests/**/conftest.py'`
returns `tests/conftest.py` as it must -- no new conftest, no new plugin. **EU1 does not
arise, measured not taken:** `git diff 0c5c864..HEAD | grep -cE '^[-+].*_COUNTER'` is `0`.
`git diff --name-only 0c5c864..HEAD -- floatfea data results` is **empty**, which is the
measurement behind "no write run, no re-base, no regenerated deliverable".

Tests: **MY OWN RUNS, in my own worktrees at the judged shas, `-p no:randomly`. Ten reds at
`e87b2c0`: the two of the escalation, and eight with one cause.**
* **FV1 selection plus both escalation tests and the vocabulary corpus: 2 failed, 873 passed
  in 335.73s.** `tests/unit`, the four root guards, `tests/test_report_vocabulary_corpus.py`,
  rung 4's `test_f4_g41_dynamic.py`, `tests/regression/test_f6_deliverable_agrees_with_itself.py`.
  The two are `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` -- the escalation, by
  name, and nothing else.
* **The three report-parametrised files at `fa8d59c`, the commit your whole-suite line
  measures: 9 failed, 464 passed, 1 skipped in 129.76s.** That is your `464 passed, 9 failed,
  1 skipped` **exactly** -- and the nine ids are not the nine you pasted. R1238.
* **At `e87b2c0`:** `test_report_guard_states.py` **7 failed, 17 passed in 139.82s**;
  `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` **1 failed**; and the inner run inside
  each planted state reports `1 failed, 430 passed` for the whole of
  `test_report_carried.py`, which is your 1 + 7 and matches.
* `python scripts/check_carried.py` -> **all 22 findings carried, exit 0.**
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`,
  `mypy floatfea`: **all clean, my own runs** -- 163 files unchanged, 45 source files.
* **NOT RUN LOCALLY, and I say which rather than implying coverage:** rungs 1, 2, 3, 5, 6 and
  the rest of `tests/regression`. `git diff --name-only 0c5c864..HEAD -- floatfea` is
  **empty**, so FV1 puts them on CI and CI ran rungs 1-3 and rung 6 at `fa8d59c`. I started a
  whole-suite run at `e87b2c0` and it was at 8% after ninety minutes; I am not reporting a
  partial count as a whole one.

CI: **the judged commit `e87b2c0` HAS NO RUN AND CANNOT HAVE ONE.** This is GC2's case and
both of its conditions hold:
```
cmd    gh run list --commit e87b2c00a7cab740f27841f66e9362ac5248283e --json name,conclusion
out    []
cmd    git diff --name-only fa8d59c..e87b2c0
out    docs/reports/R2/step-0.md     -- the only path, and `docs/reports/**` is in ci.yml's
                                       paths-ignore (CK0)
```
So the evidence is the nearest ancestor with a run, and **it concluded while I was ruling.
Run `44149168617` at `fa8d59c7a7bd5ae17ae70b60abc08da25554ca66`: `completed`, conclusion
FAILURE.** **NOT CK2** -- both executing jobs were given work and ran for 18 and 66 minutes.
```
the verification ladder   failure   rungs 1,2,3 SUCCESS | rung 6 FAILURE | rungs 4,5 SKIPPED
lint, unit and guards     failure   8 failed, 1381 passed, 1 skipped in 679.34s
CI determinism x 2        skipped   by their own workflow_dispatch condition -- unavailable
```
**EVERY CI RED THERE IS A BOUNDARY RED, TRACED PER ID FROM ITS OWN MESSAGE RATHER THAN BY
FAMILY (EG3 (i)), AND THE TRACE IS A COUNT AND NOT A RESEMBLANCE.**
`grep -oE "FAILED tests/[^ ]+"` over `gh run view --job 134272415170 --log-failed` gives
**15 occurrences of `...::test_the_report_carries_a_WHOLE_SUITE_count` and NO other inner
test id anywhere inside the eight.** That test is FT1 limb two by its own reason --
`suite_count.py` measures a clean worktree AT a sha, so the line naming that sha cannot be
inside it -- and `e87b2c0` is the commit that supplies it. The ladder's single red is
`test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`, which names R1223, a
finding the newest verdict carries, at the site that verdict named: limb one. **So CA2 is not
reached through CI's own reds.** The HOLD is on two local reds that fail the predicate in
both limbs, and on what the report publishes about these very runs.

Door (FV2 / GG2): `git worktree add -b review/e87b2c00a7ca <a path outside the repository>
e87b2c00a7cab740f27841f66e9362ac5248283e` **succeeded on the first try, so no review of this
commit existed.** Every measurement was taken there or in two throwaway detached worktrees at
`fa8d59c` and `e87b2c0` under my scratch directory; this verdict is written through
`scripts/write_verdict.py`, committed on that branch and pushed -- merge with
`git merge --ff-only origin/review/e87b2c00a7ca`. **My own writes, all in my own worktree and
all reverted before committing:** one `0a` outcome cell, one head-sha cell, one whole-suite
line, and a planted `docs/milestones/R1230.md`, with `git status --porcelain` empty after
each. `C:\dev\floatfea` was clean when I was invoked and I wrote nothing into it. **And you
did not commit to F3 between the invocation and the merge** -- it is the first round in which
no read of mine could have shown me work that is not in the judged commit.

## Carried

Verdict 63's six numbered conditions and its carry list. **FIVE ANSWERED AND CLOSED, TWO
CORRECTLY UNCHANGED, TWO WITHDRAWN BY ME.**

* **R1230 -- ANSWERED AND CLOSED, both halves.** The header names `0c5c864`; `EXPECTED` is 38
  ids computed from it; sec.12 carries 38 rows; `check_carried` is green;
  `test_the_answered_verdict_is_the_NEWEST_one` is red at neither commit. You were asked for
  the header **and** the carry list in the same commit and both are here. **The self-report is
  worth more than the fix**: sec.11 records that you told me the header read 62 without
  running `sed -n '5p'`, and names the pattern -- asserting from reading rather than running
  -- for the fourth time in this step, found by you and not by me.
* **R1231 -- THE MECHANISM IS ANSWERED; THE RECORD IT PRODUCED IS WRONG, AND THAT IS R1237.**
  All four guards that were red on the placeholders pass (`CI_SECTION`,
  `CI_section_is_about_the_REVIEWED_commit`, `counts_are_not_all_zero`, `ROUNDS_SECTION`), the
  order was the one I asked for, and three generators now stand where three paragraphs did.
  The CI table they produced says a run that failed reached no result.
* **R1233 -- ANSWERED AND CLOSED.** Sec.7 now reads "ROUND-OFF, ON THE ONE CASE MEASURED",
  states the band the accumulation sits in, and makes all six periods a **condition of
  choosing** option 2 rather than a claim already made. The over-reaching sentence is quoted
  rather than quietly replaced.
* **R1235 -- ANSWERED AND CLOSED, and the second site was a real find.** R1221's filter is in
  both `tests/test_report_carried.py` `_mentions()` and `scripts/carried_table.py`
  `MILESTONE_LABELS`, which it had to be: the guard compares the table against the
  generator's output, so a filter in one of the two makes the pair unsatisfiable. **I measured
  the filter in both directions.** It removes exactly one id -- 39 to 38, the one dropped
  being the phantom -- and nothing real: with `docs/milestones/R1230.md` planted in my own
  worktree, `R1230` STAYS in `EXPECTED`, because declared findings arrive through the
  unfiltered `_FINDING` path. Its blast radius is mention-only ids, and names rather than a
  digit count is the right choice. R1228's quotation now matches the code it quotes.
* **R1236 -- ANSWERED AND CLOSED.** The `_active_step()` output corrected with the reason it
  was wrong (BP0, named), and sec.9 rewritten: it no longer predicts a red that passes, it
  names the two that block, and it says in its own words that a trace wrong at both ends is
  worse than no trace.
* **R1232 -- CORRECTLY NOT WIRED; the condition stands unchanged for the write run.** You read
  the finding as I meant it. `pin_threads()` below `import numpy` would write a pinned thread
  count into the provenance of a run whose BLAS had already initialised at the ambient one,
  and a false provenance field is worse than the null it replaces. Nothing to do here.
* **Conditions 4 and 6 (R1225, R1223) -- OPEN, UNCHANGED, AND CORRECTLY SO.** Both red in my
  own runs at both commits, both recorded red with the cause named, neither cleared by a
  regeneration: `git diff --name-only 0c5c864..HEAD -- data results` is empty. Third round
  running in which the cheap wrong repair was available and not taken.
* **Condition 7 (a concluded GREEN ladder in CI) -- I WITHDRAW IT, because I have measured
  that you cannot satisfy it. R1239.** CI runs rung 6 BEFORE rungs 4 and 5, so the
  escalation's rung-6 red skips them -- identically at both reviewed commits. Relaying a
  condition no action of yours can meet is the mechanism this file warns about, and it was
  mine for three rounds.
* **R1234 -- WITHDRAWN, and the re-measurement is mine.** Measured at this commit:
  `tests/test_report_vocabulary_corpus.py` is inside my 873-passed selection and **neither id
  is in my failure list**, so the two reds are gone. They are gone because sec.12's generated
  table no longer carries the two row shapes, **not** because the guard was ruled on -- so
  the disagreement I recorded is unobservable rather than answered, and asking you to change a
  guard that is not failing would be the extend-not-repair line EK2 draws. My two corpus
  entries' `measured=` fields are the stale thing here, and they are mine.
* **R1217, R1218 -- still open and not answerable here**; R1218 becomes a blocking item when
  step 2 writes the tolerance entry. **R1212, R1203, R1204, R1224 -- reviewer-side or
  Xabier's; no action asked of you. R835 -- `unchanged, R2` (GE3), one line.** The R1213
  message assertion stays a ledger row.
* **Verdict 58's twelve and verdict 59's four -- ROUTED, and now in two places that agree**
  (sec.12's generated table and sec.16's prose). Accepted as a disposition -- **but see
  R1240: the gate meant to hold that list in place is reading the wrong round's Carried
  section, so the routing rests on your bookkeeping and not on the guard.**

## Findings

**R1237. (BLOCKS) THE GENERATED `0a` TABLE PUBLISHES A RUN THAT CONCLUDED FAILURE AS "no
result", AND OMITS A RUN OF THIS ROUND ALTOGETHER. IT IS NOT FT1 LIMB TWO, AND THAT IS
MEASURED RATHER THAN RULED ON THE TEST'S NAME.**

```
claim  the 0a table agrees with gh for every row
cmd    pytest -q tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
out    AssertionError: run 44145793006: the table says `**no result** (status
       `in_progress`)`, gh says `failure`
cmd    gh run view 44145793006 --json conclusion,status,headSha,createdAt,updatedAt
out    conclusion failure, completed, head 0c5c864..., created 18:15:04Z, updated 18:58:00Z
cmd    git log -1 --format=%cI e87b2c0     (the commit that carries the table's file)
out    2026-11-17T11:28:58-08:00 = 19:28:58Z -- THIRTY MINUTES after that run concluded
cell   ONE VARIABLE, that row's outcome cell, in my own worktree, reverted after:
         `**no result** (status in_progress)`  ->  1 failed
         `conclusion **failure**`              ->  1 passed
rule   FS1 with FT1 -- a red is a boundary red if it names a finding or a site of the newest
       verdict, OR if its SUBJECT IS THE COMMIT CARRYING IT
judge  **IT FAILS BOTH LIMBS.** It names no finding and no site of verdict 63. Its subject is
       run `44145793006` at `0c5c864`, an ANCESTOR pushed three commits ago whose run
       concluded half an hour before the carrying commit was written. FT1 names this test --
       and FT1's own sentence is that "both limbs are reasons and neither is a list of
       names". The reason it gives, *no run exists for a commit before it is pushed*, is not
       this red's reason, and the cell above is how I know rather than a reading of the
       docstring. **CZ1 (iv) applies unchanged.**
```

**The silently wrong result.** Sec.13 is the only part of this report that says anything about
CI at the commits of this round, and what it says is that the run at the verdict commit
**reached no conclusion**. It concluded FAILURE: eight reds in `lint, unit and guards` and a
red rung 6. A reader of the report GI6 sends to Xabier -- who does not have `gh` in his hands
-- learns that this round has no CI result where the truth is two red runs, and a CI table
looks identical whichever state it describes. That is CE1's own subject. **The table is also
incomplete**: run `44149168617` at `fa8d59c`, a commit of this round, has no row at all, and I
measured that nothing catches it -- with the one row corrected the gate is `1 passed` while
the missing run stays missing. **CP3 is the mechanism**: the paste was true when taken, an
edit followed it, so the paste was void at `e87b2c0`, where regenerating would have printed
`conclusion failure` and the second run's row.

*Closed when* sec.13 and sec.14 are **regenerated as the LAST edit before committing, after
every run of the round has CONCLUDED**: the `44145793006` row reads `conclusion **failure**`,
a row exists for `44149168617`, and the gate is pasted green at the commit that carries the
table. **Eight of my ten local reds clear with it, and I measured that too**: all 21 reported
inner failures inside `test_report_guard_states.py` at `e87b2c0` name this one test, three per
state, and no other test anywhere.

**R1238. (BLOCKS) THE WHOLE-SUITE RED LIST IS TWO REDS SHORT OF THE COUNT IN ITS OWN LINE,
AND THE GENERATOR CANNOT PRODUCE THAT.**

```
claim  the fenced block under the whole-suite line is that run's failing ids
cmd    sed -n '1135,1154p' docs/reports/R2/step-0.md
out    "**The excluded set: 464 passed, 9 failed, 1 skipped.**" above a fenced block of NINE
       bullets -- 2 `failed` and SEVEN `failed, in the excluded set`
cmd    grep -n "verdict_amended_after_the_commit_the_report_answers\|zero_padded_step_number"
       docs/reports/R2/step-0.md
out    947, 948, 1119, 1120 -- all four inside the CI lists for run 44140076843 at 4c19570.
       NEITHER APPEARS IN THAT BLOCK.
cmd    my own run of the three files in a detached worktree at fa8d59c
out    9 failed, 464 passed, 1 skipped -- the nine being the seven you list plus
       test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
       and test_the_guard_survives_the_state[zero_padded_step_number]
rule   scripts/suite_count.py:282-287 prints every id in `failing` and then every id in
       `ex_failing`, and `:120` returns the count as `len()` OF THAT SAME LIST
judge  **THE LINE AND THE LIST CANNOT DISAGREE IN THE GENERATOR'S OUTPUT**, so the block in
       the report is not the generator's output: either an edit followed the paste, or the
       two halves came from two runs. CP3, in the commit whose whole purpose is a figure
       taken last. Your commit message declares the other defect of that same splice script
       -- the one that deleted sec.15 and sec.16 -- and this is the one it did not catch.
```

**The silently wrong result.** The block is the step's **red trace**, which is what the next
boundary-red waiver is decided from. As published it says the excluded half's reds are seven
named tests when they are nine, so `verdict_amended_after_the_commit_the_report_answers` and
`zero_padded_step_number` are published as green while they are red. **Those two are not
arbitrary members of a cascade: they are two of the exactly eight reds CI reports at
`fa8d59c`**, and EG3 (i) exists because eight planted states were once ruled as one cascade
by class and the eighth was a real defect. A trace that drops two of its own nine is the
state that rule was written against.

*Closed when* the fenced block is `scripts/suite_count.py`'s output verbatim at the commit
that carries it, re-run as the last edit, with the number of `failed` bullets equal to the two
counts in the line above it, and the command pasted beside it.

**R1239. (DOES NOT BLOCK -- FF0, next commit, and it is not new apparatus) CI RUNS RUNG 6
BEFORE RUNGS 4 AND 5, SO THE HIGHEST RUNG SKIPS THE TWO THIS STEP NEEDS.**

```
claim  the ladder in CI is ordered by dependency
cmd    gh api repos/:owner/:repo/actions/jobs/<the ladder job> --jq '.steps[] | "\(.number) \(.name) -> \(.conclusion)"'
out    at BOTH reviewed commits, 4c19570 and fa8d59c, identically:
         ladder 1, 2, 3 -> success ; ladder 6 -> failure ; ladder 4 -> skipped ;
         ladder 5 -> skipped
cmd    grep -n "ladder [0-9]" .github/workflows/ci.yml
out    :521 one, :523 two, :525 three, :527 SIX, :529 four, :531 five
rule   CLAUDE.md, Testing: "The verification ladder is ordered by dependency. A failure at a
       low rung makes higher rungs uninterpretable"
judge  The ordering inverts the rule it implements. Rung 6 is the HIGHEST rung and it gates
       two below it, so while the escalation holds `test_R756` red, **rungs 4 and 5 cannot
       run in CI at any commit** -- and rung 4 is where the other escalation red,
       `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it`, lives, so CI has
       never measured it. Nothing is published wrongly -- a skipped step is recorded as
       skipped and the generator calls skipped jobs unavailable -- so FR1 does not block it;
       it is gating apparatus, so FF0 rather than the ledger.
```
*Closed when* either the two existing steps move ahead of rung 6 -- a reorder of steps that
already exist, so no new apparatus is created -- or the report records that rungs 4 and 5 are
unmeasurable in CI while the escalation stands. **Condition 7 is withdrawn either way.**

**R1240. (DOES NOT BLOCK -- FF0, next commit) THE CARRY GATE READS THE OLDEST ROUND'S
`Carried` SECTION, SO FIVE ITEMS THE NEWEST VERDICT CARRIES ARE OUTSIDE ITS DOMAIN AND FOUR
IT DOES NOT CARRY ARE INSIDE IT.**

```
claim  EXPECTED is the newest verdict's findings plus the items it carries forward
cmd    python -c "import test_report_carried as t;
       print(repr(t._section(t.VERDICT_TEXT,'Carried')[:70]))"
out    "\n\nThe newest verdict is `63affd1`'s entry on `602bce8` (verdict 58), and its ope"
       -- that is VERDICT 59's Carried section, the OLDEST round in the file
rule   tests/test_report_carried.py:366, `_section` takes `heads[-1]`, the LAST matching
       heading -- and DX2 appends earlier rounds BELOW the newest, so the last `## Carried`
       in an accumulated verdict file is the first round's. The report path is immune
       because its callers slice `_newest_revision(...)` first; the verdict path has no
       such slice.
cell   ONE VARIABLE, the slice, on the same text: the newest round's Carried gives 31
       mentions against today's 16, and the symmetric difference is the finding --
         GAINED: R1212, R1217, R1218, R1219, R1224   (five open items verdict 63 carries BY
                 NAME for which no parametrised case exists today)
         LOST:   R835, R1198, R1199, R1202           (required only because it is reading
                 verdict 59)
judge  Wrong in BOTH directions (EH4), and the weakening direction is the one that matters: a
       revision may drop any of those five from its Carried table and the gate stays green.
       That is assertion domain blindness on the gate whose domain IS the dependency list --
       R1230's shape one level down, this time in the apparatus rather than in a header. No
       wrong number reaches an artifact, so FR1 does not block it; it decides whether a green
       is believed, so FF0 puts it in the next commit rather than the ledger.
```
*Closed when* the verdict text is sliced to its newest round before the Carried section is
extracted, **at BOTH sites in the same commit** -- `tests/test_report_carried.py` and
`scripts/carried_table.py:158`, whose `_carried_section` is a copy of the same four lines --
because the guard compares the table against the generator and a repair in one makes the pair
unsatisfiable. That is R1235's lesson applied before it bites. **Expect the five new ids to
need rows in the same revision; that is the repair working, not a new finding.** One ledger
note from the same measurement: `_FINDING` scans the WHOLE accumulated file, so every finding
ever declared in this step's verdict file is required forever -- over-broad, loud, and not
worth a round.

**R1241. (DOES NOT BLOCK -- ledger, FR1 report prose) TWO SENTENCES THAT ONE COMMAND EACH
REFUTES.** Sec.14 reads *"the verification ladder at `4c19570` ran 2143 passed, 1 failed --
that one failure is the staleness guard"*; the report's own generated list twenty lines above
names it, and it is `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`
(R1223). The staleness guard is in rung 4, which was **skipped** at that commit and has never
run in CI during this step. And `docs/reports/R2/step-0-answers.json`'s preamble reads
*"REVISION 1 answers verdict 62 (0901933)"*, while `sed -n '5p'` on the report gives
`Answers: verdict 61 @ c931885` -- which is R1230's whole point, so the json asserts the
repair that was deliberately not made. Both are prose; both are one line.

**R1242. (DOES NOT BLOCK -- ledger, and it constrains MY wording more than yours) THE
`_FINDING` PATH IS UNFILTERED, SO A MILESTONE LABEL CAN STILL ENTER THE PARAMETRISED SET.**
Measured on a synthetic string rather than asserted: `_FINDING.findall` of a bold line
beginning with the plan's own file name returns the plan label as a finding id. R1221's
filter covers `_MENTION` only. The consequence is a demanded carry row for a phantom, which
is **loud**, so no wrong result follows; and the party who can trigger it is me, by starting a
bold line with a plan name. I have not, in this verdict.

**WHAT THIS COMMIT GOT RIGHT, AND IT IS MOST OF IT.** Both blocking findings of verdict 63 are
answered at their roots rather than at their symptoms, and four generators now do work that
four hand-written passages used to do: sec.12's 38 rows are `carried_table.py`'s output and
the guard that compares them is green; sec.15's 211 declarations are read from the gate's own
`SITES` and **all 224 of its parametrised cases pass, which is the first time this step has
had that**; `check_carried` is green and caught the section short twice on the way. I
spot-checked the declarations against the commit rather than trusting them --
`tests/test_report_carried.py:387-390` at `0c5c864` is docstring prose inside
`_verdict_text_at`, so "no change" is true of the lines and not merely of the diff. **Both
self-inflicted defects were declared by you before I looked**, and I verified the cp1252
repair at the byte level: **0** occurrences of `EF BF BD` in either file, against 79 and 46
proper `C2 A7`. **And R1232 is the round's best answer**: a one-line fix was available, it
would have written a false provenance field, and you declined it and said why.

## Tolerances touched

**None, measured twice.** `git diff 0c5c864..HEAD -- floatfea/tolerances.py` is **0 lines**
and `git diff 0c5c864..HEAD | grep -cE '^[-+].*_COUNTER'` is **0**, so **EU1 does not arise**
-- and I ran the apparatus at configurations the diff did not choose anyway, which is where
R1237's cell and R1240's both-direction measurement came from. The one tolerance-shaped thing
still implicated is not a tolerance and has not moved: `--check`'s `np.array_equal` with no
threshold, by Q8's rule. **If any answer to the escalation introduces a tolerance on that
comparison, that is a widening and it is refused.** R1218's row-1 form question is still
unwritten and becomes a blocking item at step 2.

## Corpus

**One batch, committed separately at `cbfa0a2`:
`tests/corpus/report_record_freshness_and_completeness.txt`, 26 entries, all new.** GC3 left
the pause expired, so this is my own call under GA3's length target. **It is the other axis of
`tests/corpus/report_ci_section.txt`:** every entry in that file has an author who changed a
byte, and this round's blocking finding had none -- the generator printed what was true, a run
concluded, and the published status became wrong with nobody touching it.

**10 of the 26 measured this round, one row or one line at a time in my own worktree,
reverted after each. 2 caught by a shipped guard, 1 partly, 5 reach a green gate, and 2 were
caught by my own measurement and by no guard at all.** The ones that get through: a `0a` table
missing an entire run of the round (with the stale row corrected, `1 passed` while
`44149168617` is absent); a head-sha column never compared with `gh` (a nonexistent commit in
that cell gives `1 passed`); the whole-suite line re-pointed at an unrelated older sha with an
older green count (`1 passed` -- and DR0 declares that hole deliberately, which is why it is
recorded rather than asked for); and the truncated fenced list, which is R1238 and which I
measured on the shipped artifact rather than on a plant. **The gate does carry its own failure
in the direction that matters most**: with `gh` unable to answer at all, the tree that is
`1 passed` goes `1 failed` with *"no such run"* for both rows, so it fails loudly rather than
going quiet. **What I ran beside the batch** is the recorded substitute, and it is where R1240
came from: a continuum over the parameter space the carry gate's own decision rule guards --
which round's Carried section it reads -- solved in both directions.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN** -- GI6 holds it anyway, so this HOLD costs no
schedule. **Rounds: this consumed revision 2 of 3 under ES0. ONE REMAINS**, and I would rather
it closed the step than spent itself on bookkeeping, so the list is short and ordered. R1230,
R1231's mechanism, R1233, R1235 and R1236 are **DISCHARGED and are not re-measured**;
condition 7 and R1234 are **WITHDRAWN** by me, each with the measurement that forced it.

1. **R1237 -- regenerate sec.13 and sec.14 after every run of this round has CONCLUDED, as
   the last edit before committing.** The `44145793006` row says `failure`, a row exists for
   `44149168617`, and the gate is pasted green at the carrying commit. Eight of my ten local
   reds go with it.
2. **R1238 -- the fenced red list is the generator's output verbatim and its length matches
   its own counts.** Same commit, same ordering: generate, edit, re-run, paste, commit.
3. **R1240 in the next commit (FF0, not the ledger), at BOTH of its sites.** R1239 is a
   two-line reorder or one sentence, your choice; R1241's two sentences are one line each.
4. **Conditions 4 and 6 -- unchanged, still subordinate to the escalation, still red with
   their cause named.** Do not clear the staleness guard by regenerating the npz and do not
   clear R1223 by regenerating the deliverable against a red gate. Three rounds of not doing
   the cheap wrong thing is the best evidence this step has produced.
5. **No write run until R1232's pin is above `import numpy` or in the invocation's
   environment**, with the provenance recording the pinned values.

**Nothing here is a STOP, and I considered it on the ladder.** Rungs 1, 2 and 3 are SUCCESS in
CI at `fa8d59c`, over code byte-identical to the judged commit's
(`git diff --name-only fa8d59c..e87b2c0` is one report file); no `floatfea/` file is in this
diff at all; and the two escalation reds are a provenance comparison and a regeneration
comparison rather than a numerical disagreement at a rung. The locked plan is faithful to GI
and needs no reopening, and section 6 item 2 of that plan is still the one clause I rule must
NOT be triggered yet.

**And I disagree with nothing in the criterion this round.** FR1 did the work it was adopted
for: R1239, R1241 and R1242 would each have been a blocking round under the unamended CZ0 and
each is a line here instead, and FF0 took R1240 out of the ledger without taking a round for
it. The two that block are both "a wrong record in the report GI6 sends to Xabier, silently",
with the sentence written out, which is the test FR1 asks for.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0
Reviewed commit: 4c19570907a3f3f300222f9e95ffd79d95e26556
**Reviewed commit: `4c19570907a3f3f300222f9e95ffd79d95e26556`.**
Verdict: HOLD
Scope: **R2 step 0, REVISION 1 -- a REVIEWED REVISION, not an interim check.**
`docs/reports/R2/step-0.md` exists at this commit, so under ES0 this is **1 of step 0's
3 revisions** and **2 remain**. It closes nothing, so `--closes` is correctly absent (FK1).
**Ruled under FR1 with EZ0**, and each blocking finding names the silently wrong result it
produces. **GE3: `R835: unchanged, R2`. Not re-measured.**

**ITEM 1b IS THE FINDING, AND IT IS THE ONE COMPARISON A MACHINE WAS NOT GIVEN.** The
report's header reads `Answers: verdict 61 @ c931885`. The newest verdict is **62**, at
reviewed commit `9e1092a`, written by commit `0901933`. **The invocation told me the header
names verdict 62 and `0901933`; it does not, and `grep` over the whole report finds
`verdict 62`, `0901933` and `9e1092a` zero times.** R1230 below, with the consequence
measured rather than asserted.

**4 / 4b / 4c, each diffed separately against `0901933`:** `floatfea/tolerances.py` 0 lines;
`.claude docs/SUPERVISOR.md` 0 lines, so **no STOP-class finding**; `tests/conftest.py`
0 lines, and `git ls-files -- tests/conftest.py 'tests/**/conftest.py'` returns
`tests/conftest.py` as it must. No new conftest, no new plugin.
**EU1 does not arise, measured not taken:** `git diff 0901933..HEAD | grep -cE '^[-+].*_COUNTER'`
is `0`. I ran the adversarial cases anyway and they are where R1226's closure came from.
**One correction to my own instructions, stated rather than worked around:** step 2 says
`git diff -- floatfea tests docs`, which **misses `scripts/`** -- where two of the three
repairs under review live. I diffed the whole commit.

Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`.**
* FV1 selection plus the deliverable regression test (`tests/unit`, the four root guards,
  rung 3 deck export, rung 4 G4.1, `tests/regression/test_f6_deliverable_agrees_with_itself.py`):
  **2 failed, 862 passed in 341.01s.** The two are conditions 4 and 6 by name --
  `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`. Both still open and
  correctly so. The report's `1 failed, 839 passed` is the same tree over a narrower
  selection: 862 - 839 = 23 is the deliverable file it did not include.
* **The six report-guard files, which the report did not run and left to me.** CI's wide
  selection, `pytest tests --ignore=tests/unit --ignore=tests/verification --ignore=tests/regression`:
  **146 failed, 1103 passed, 1 skipped in 595.04s.** Verdict 61 gave 187 and verdict 62 gave
  172 at `9e1092a`; **the answering report moved 172 -> 146.** Per file: `test_report_carried`
  151 -> 129, `test_report_guard_states` 20 -> 7, `test_report_numbers_are_sourced` 1 -> 8,
  `test_report_vocabulary_corpus` 0 -> 2. **EG3 (ii) is measured on my side; it is still
  owed on the report's.**
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`, `mypy floatfea`:
  **all clean, my own runs** -- 163 files unchanged, 45 source files.
* **NOT RUN LOCALLY, and I say which rather than implying coverage:** rungs 1, 2, 5, 6 and
  `tests/regression` beyond the one deliverable test. **No `floatfea/` file is in this diff at
  all** (`git diff --stat 0901933..HEAD -- floatfea` is empty), so FV1 puts the rest on CI.

CI: **run `44140076843` at the FULL sha `4c19570907a3f3f300222f9e95ffd79d95e26556` EXISTS,
so FP1 held.** `lint, unit and guards` **CONCLUDED FAILURE at step 10 `guards and
meta-tests`**, with `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all
**success** before it -- so the guards step is seen to have RUN rather than been skipped
behind an earlier red (CZ1 iii). **`the verification ladder` had NOT finished when I ruled**
(`in_progress` at 18:14:29Z, started 17:43:22Z -- 31 minutes): **rungs 1, 2 and 3 SUCCESS**, rung 6 running,
**rungs 4 and 5 unmeasured.** A run that has not finished is not a pass. Both determinism
jobs `skipped` by their own `workflow_dispatch` condition. **NOT CK2** -- runners
`1000001920` and `1000001921` were assigned and both jobs executed for minutes.
**CA2 IS REACHED: CI IS RED AT THE JUDGED COMMIT.** CI's per-id list is **unavailable, not
skipped over**: `gh run view --job 134240156555 --log-failed` answers *"run 44140076843 is
still in progress; logs will be available when it is complete"* -- but my own wide run IS
that job's selection, so nothing hides inside CI's aggregate that I have not measured.
GC2 does not arise: the diff touches `scripts/` and `tests/`.

Door (FV2 / GG2): `git worktree add -b review/4c19570907a3 <a path outside the repository>
4c19570907a3f3f300222f9e95ffd79d95e26556` **succeeded on the first try, so no review of
this commit existed.** Every measurement above was taken in that worktree; this verdict is
written there through `scripts/write_verdict.py` (`grep -nE '"(commit|add)"|check_call|\.run\('`
over it: no match), committed on that branch and pushed -- merge with `git merge --ff-only
origin/review/4c19570907a3`. **My own writes, all in my own worktree and all reverted before
committing:** the verdict file moved aside and back (cell A), a planted
`docs/reports/R2/step-1.md` with the plan marker at 0 and 1 and back (cell B), the report
moved aside and back (the vocabulary cell). `git status --porcelain` in my worktree is empty
but for the corpus file, which is committed separately at `91f083d`.
**Outside the repository, read-only:** `git -C <HSP-stable|HSP-runs>
hash-object/rev-parse/status/check-attr/config`, and three throwaway `git init` trees under
my scratch directory for the R1226 cells. Nothing wrote a byte into either HSP worktree or
into `C:\dev\floatfea`.

**AND A DISCLOSURE, BECAUSE IT IS THE HAZARD FV2 EXISTS FOR AND IT WAS LIVE WHILE I RULED.**
`C:\dev\floatfea` was clean when I was invoked and is **dirty now** -- `git status --porcelain`
there shows `docs/reports/R2/step-0.md`, `docs/reports/R2/step-0-answers.json`,
`tests/test_report_carried.py` and `tests/test_report_guard_states.py` modified. Those are
four of the five files I judged. **Every read I took was of the commit, in my own worktree,
so the addendum-29 defect did not arise** -- but in a shared checkout it would have, on
exactly these files, and the reading would have been of work that is not in `4c19570`.
I judged `4c19570` and nothing else.

## Carried

Verdict 62's five numbered conditions, plus the header requirement and the EG3 (ii) paste it
closed on. **TWO ANSWERED AND CLOSED, ONE HALF-ANSWERED, THREE OPEN, AND THE HEADER
REQUIREMENT FAILED.**

* **R1226 (the stable key, R1213 one key over) -- ANSWERED AND CLOSED, both limbs, and I ran
  the control and the direction the commit did not.** The refusal is inside `_source()`, not
  at module level, so it cannot take a rung down in collection. Six values through `--check`,
  with exit codes measured separately because a pipe to `tail` hides them:
  ```
  cmd  FLOATFEA_HSP_STABLE=<...>/HSP-runs    export_buoy_centers_ref.py --check
  out  REFUSED: the STABLE key resolves to ...\HSP-runs, which is not an HSP-stable
       worktree ... records a source it did not read (R1226)            exit 1
  cmd  FLOATFEA_HSP_STABLE=<...>/HSP-stable  (the control)
  out  EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1    exit 0
  cmd  <...>/HSP-stable/../HSP-runs
  out  REFUSED ... resolves to ...\HSP-runs   -- `resolve()` normalises the hop, so the
                                                 classic bypass is closed
  cmd  a REAL directory named HSP-stable-copy, source present and committed
  out  REFUSED by the name predicate          -- measured with the existence refusal cleared,
                                                 so the predicate is what fired
  cmd  C:/nope/HSP-stable  and  C:/nope/not/a/tree
  out  R1214's "declared and is not a directory" refusal, which fires first
  cmd  <...>/hsp-stable  (case-folded, existing)
  out  current  -- correct: `resolve()` restores the on-disk case, so it IS the tree
  ```
* **R1226's SECOND LIMB -- THE CHOICE IS RIGHT, AND THE REASON IS STRONGER THAN THE ONE THE
  DOCSTRING GIVES.** You asked me to rule on hashing the working file against `--dirty`.
  **Hashing is correct**, and measurements say so rather than the argument:
  ```
  cmd  git -C HSP-stable hash-object <rel> ; git -C HSP-stable rev-parse HEAD:<rel>
  out  b8b8123904af...   b8b8123904af...      -- IDENTICAL on a clean tree
  cmd  git -C HSP-stable config core.autocrlf ; git check-attr text eol -- <rel>
  out  true ; text: unspecified, eol: unspecified
  rule `git hash-object <path>` applies the attribute filters, so CRLF working bytes hash to
       the LF blob. Had it not, `data/platform/buoy_centers_ref.json` would have STOPPED
       REGENERATING at this commit -- R1223's shape -- and `--check` would be a third red.
  cell ONE VARIABLE, the working file's bytes, in a throwaway git tree named HSP-stable:
         clean                              -> "current"
         comment-only edit, no value moves  -> "the VALUES match but the source blob moved,
                                                b8b8123904af -> 48391dd3de42"
         Z_HUB_REF edited                   -> "STALE -- hub_positions_xyz_m differs"
       and the OLD code on that same dirty tree: `rev-parse HEAD:<rel>` still returns
       `b8b8123904af`, so `--check` would have printed `current`.
  judge `--dirty` would have said "something here is uncommitted" while publishing
       `b8b8123904af` beside numbers that did not come from it. The hash makes `check()`'s
       own `blob_sha` comparison (`:172-180`) the thing that catches it, and that comparison
       already ships. Your docstring's reason is right; this is the measurement of it.
  ```
  **The residual, stated rather than left:** a real directory *named* `HSP-stable` holding
  other content still prints `current` (measured). A name predicate is defeated by a name and
  always will be; what covers the rest is the blob sha, which catches any tree whose bytes
  differ. The pair is sound. The shapes nothing catches are in my corpus below.
* **R1227 (R1206's fourth site) -- ANSWERED, AND I WITHDRAW THE `_PAIRED` HALF OF MY OWN
  CONDITION.** `assert REPORTED & REVIEWED` is the right predicate and `:217` does **not**
  need to move. You asked for this explicitly; here is the cell.
  ```
  cell ONE VARIABLE -- the verdict file present or absent, at this commit:
         both present        -> REPORTED [0] REVIEWED [0] _PAIRED 0 STEP 0 STEP_REPORT 0,
                                test green
         verdict moved aside -> 1 failed at tests/test_report_carried.py:585,
                                "reports exist for steps [0] and verdicts for []; no step
                                 has both"
  rule `STEP_REPORT == _PAIRED` at `:606`, the assertion I said would go silently vacuous
  judge IT IS UNREACHABLE IN THAT STATE. `_PAIRED`'s `else 0` arm is taken exactly when
       `REPORTED & REVIEWED` is empty, which is exactly when the NEW first assertion fires --
       and it fires with a message that is TRUE. `grep -rn _PAIRED tests/ scripts/ .claude/`
       gives three code sites, all in this one file (`:217`, `:237`, `:606`), and `:237`'s
       use is sound in every state I constructed. The sequencing closes it, so my "treat
       `:229` in the same commit" was wrong: it asked you to change a line that is
       load-bearing for nothing.
  ```
* **AND THE MARKER MEASUREMENT IS WITHDRAWN TOO -- IT IS MINE, AND YOU WERE RIGHT TO ASK FOR
  IT RULED EXPLICITLY RATHER THAN LET IT STAND.** Verdict 62 recorded `marker 0 -> STEP 0` and
  `marker 3 -> STEP 0` and attached the cause *"the `else 0` arm is doing the work"*. The
  figures were right; the cause was not.
  ```
  cell ONE VARIABLE -- the marker, with a step-1 report planted beside the step-0 one:
         marker 0 -> _PLAN_STEP 0 _PAIRED 0 STEP 0 REPORT step-0.md
         marker 1 -> _PLAN_STEP 1 _PAIRED 0 STEP 1 REPORT step-1.md
  judge THE MARKER DOES CONTROL WHICH REPORT THE GUARD READS. It had no effect at `9e1092a`
       because `3 not in REPORTED` -- only step 0 has a report -- not because the resolver
       ignores it. A measurement over one value of the other axis with a causal sentence
       attached: BG0, on my side of the loop. **Nothing to fix; the claim is withdrawn.**
  ```
* **"One, and this is it" -- ANSWERED, and the replacement is not decorative.**
  `assert not Path(relative).is_absolute(), "the probe value must be relative to mean
  anything"` is what stops the R1219 test passing on an absolute value, which is the shape
  R1229 was. The probe directory is out of the repository root, and `git status --porcelain`
  was empty after every run I made. **R1229 discharged.** One ledger note: `os.path.relpath`
  raises `ValueError` when `tmp_path` and the repo root are on different drives -- loud, not
  silent, so it is a note and not a finding.
* **R1225 (ii) -- THE RECORDING HALF IS ANSWERED; THE HOLDING HALF IS NOT, AND THE OBVIOUS
  REPAIR IS NOT A ONE-LINER. R1232 below.** The `environment` block is only built on a write
  run, which nothing covers, so I exercised it: it builds and serialises, and it is already
  informative -- `numpy 2.5.4 / scipy 1.18.1 / xarray 2026.4.0` against
  `BASELINE_CONDITIONS`' `2.4.4 / 1.17.1 / 2026.7.0`, three libraries off the artifact's
  basis, with `threads` all `null` and `openblas_coretype` `null`.
* **R1225 (i) -- ANSWERED FOR THE DECISION, NOT FOR THE CLAIM IT IS USED TO SUPPORT. R1233.**
* **R1225 (iii) -- ANSWERED.** Section 7 escalates under **FQ3** by name, does **not** trigger
  `R2.md` section 6 item 2, and says so. The implementer's tree shows no `data/` entry:
  **no write run was made.** This was the one decision in the step that could have
  republished a dozen figures in a file sent to Xabier, and it was taken correctly for the
  second round running.
* **Conditions 4 and 6 -- OPEN, UNCHANGED, AND CORRECTLY SO.** Both red in my own run, both
  recorded red with their cause named, neither cleared by writing a provenance. The staleness
  message now names three blobs rather than two because this commit touched
  `export_f4_dynamic_inputs.py`; that is the diff, not a new defect.
* **Condition 7 (a concluded GREEN ladder in CI at the follow-on sha) -- NOT MET.** Rungs 1-3
  are SUCCESS in CI at this sha, which is new and worth having. **Rungs 4 and 5 are still
  unmeasured in CI at any commit of this step.**
* **The header requirement -- FAILED. R1230.** **EG3 (ii)'s paste -- NOT DONE**: the report
  carries no report-guard count, because `<!-- WHOLE_SUITE -->` was never filled.
* **R1221 and R1228 -- STILL OPEN, and FF0 said "next commit". R1235.** **R1217, R1218 --
  still open**, unchanged and not answerable here; R1218 becomes CZ0 (b) when step 2 writes
  the entry. **The R1213 message assertion -- ledger, and the answer to your question is no:**
  `:209` asserts the two keys differ, so the identity path cannot fire and the assertion is
  not vacuous. It stays a ledger row and I am not asking you to narrow it in a round.
  **R1212, R1203, R1204 -- reviewer-side or Xabier's. R1224 -- mine, no action.**
* **Verdict 58's twelve items and verdict 59's four report items -- PARTLY ROUTED.** Section 8
  routes R1196-R1201 and R1186/R1188/R1189(c)/R1190/R1191/R1193 to step 1, which is a
  disposition and acceptable. Four of them (R1197-R1200) are nonetheless red as missing carry
  rows, which is R1230's consequence rather than a separate item.

## Findings

**R1230. (BLOCKS) THE `Answers:` HEADER NAMES VERDICT 61 WHILE THE NEWEST IS 62, AND THE
GATE'S FINDING SET IS COMPUTED FROM THE VERDICT THE HEADER NAMES. ITEM 1b.**

```
claim  the report answers the newest verdict
cmd    git show HEAD:docs/reports/R2/step-0.md | sed -n '5p'
out    Answers: verdict 61 @ c931885
cmd    sed -n '1,4p' docs/reviews/R2/step-0.md ; git log --oneline -1 -- docs/reviews/R2/step-0.md
out    # Review -- R2 step 0 -- ES0 INTERIM CHECK ... Reviewed commit: 9e1092a...
       0901933 review: R2 step 0 ES0 INTERIM CHECK at 9e1092a -- HOLD, two blocking findings
cmd    grep -n "verdict 62\|0901933\|9e1092a" docs/reports/R2/step-0.md
out    (nothing -- three needles, zero hits)
cmd    tests/test_report_carried.py:406-412 -- ANSWERED = _answered_verdict(REPORT_TEXT);
       VERDICT_TEXT = _verdict_text_at(ANSWERED); EXPECTED = _FINDING.findall(VERDICT_TEXT) | ...
out    ANSWERED = c931885, EXPECTED = 27 ids, and
         R1225 in EXPECTED: False  R1226: False  R1227: False  R1228: False  R1229: False
cell   ONE VARIABLE -- the sha in the header. `_verdict_text_at('0901933')` gives EXPECTED =
       32, and the five it adds are EXACTLY ['R1225','R1226','R1227','R1228','R1229'].
rule   tests/test_report_carried.py:514 test_the_answered_verdict_is_the_NEWEST_one, whose own
       docstring reads "Item 1b, mechanically ... A header naming a real but older verdict
       commit passed every check: the sha resolves, the findings parse, and the carry table
       is complete about a list that has been superseded."
out    FAILED -- "the report at `4c19570` is newer than the verdict at `0901933` and names
       `c931885`. Written with the newest verdict available, it must answer that one."
judge  That red names no finding and no site of the newest verdict, and its SUBJECT is not
       the commit carrying it -- it is measurable at this commit and it was. It fails the
       FS1/FT1 predicate in both limbs, so **CZ1 (iv) applies unchanged and it blocks.**
```

**The silently wrong result, in the form FR1 asks for -- two of them.** First: `EXPECTED` is
the domain of `test_the_report_carries_the_finding`, so **neither of verdict 62's blocking
findings is a parametrised case at this commit.** A revision that had answered nothing about
R1225 or R1226 would read green on the one gate CLAUDE.md says the whole arrangement exists
for -- *"the dependency list is part of what gets re-read at every step"* -- and the list it
re-read is the superseded one. That is assertion domain blindness on the gate whose domain
IS the dependency list. Second: `scripts/ci_section.py:203 _anchor()` reads **this same
header** (`_ANSWERS` at `:178`), so generating section 10 now produces a CI table anchored on
`c931885` and publishes it under the heading *"CI at the judged commit"* -- a wrong commit,
and therefore wrong pass/fail counts, in the mandatory section of the report GI6 sends to
Xabier, and silent because a CI table looks identical whichever commit it describes.

**And the report is split between two verdicts rather than simply stale.** Section 7 and all
three code comments answer verdict 62 (R1225, R1226, R1227 by name). The header, section 8's
table, `step-0-answers.json` and section 9's red trace answer verdict 61. The prose at
lines 8-12 asserts the opposite of what line 5 does -- *"This header names 61 because the
newest verdict is the one the guard checks against"* -- and its parenthetical enumerates
"61, 60, 59" with 62 absent. BP0 at the scale of a whole document: the body moved and the
header did not.

*Closed when* the header names `0901933` **and section 8 plus `step-0-answers.json` carry the
32-id list in the same commit.** Fixing the header alone makes it worse by five: the table has
no row for any of R1225-R1229, and it is also missing R1213, R1214, R1215, R1221, R1222,
R1223 and `R2`, which the verdict it *names* already demanded --
`test_the_report_carries_the_finding` is red on exactly those ten ids today. The 107
`test_every_named_site_is_touched_or_declared[...]` reds and the seven
`test_the_guard_survives_the_state[...]` reds are the same item: the harness copies the real
report into every planted tree, so `baseline` reports *"expected a clean run"* with 122 of
these inside it, and **the harness that holds the resolver in place is certifying nothing
while the carry list is short.**

**R1231. (BLOCKS) ALL THREE GENERATED SECTIONS ARE UNFILLED PLACEHOLDERS, AND CI IS RED AT
THIS COMMIT, WHICH IS THE EXACT STATE CE1 WAS ADOPTED FOR.**

```
cmd    tail -6 docs/reports/R2/step-0.md
out    <!-- WHOLE_SUITE -->   ## 10. CI at the judged commit   <!-- CI_SECTION -->
cmd    pytest -q tests/test_report_carried.py -k "CI_SECTION or REVIEWED_commit or
       counts_are_not_all_zero or ROUNDS_SECTION"
out    test_the_report_carries_a_CI_SECTION  "the newest report revision has no
         `## ... CI ...` section"  assert '' -- the section body is EMPTY, not a placeholder
         that parses
       test_the_CI_section_is_about_the_REVIEWED_commit  "the CI section names no commit"
       test_the_reported_CI_counts_are_not_all_zero      "the shape without the measurement"
       test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph  "no `## 0a` table"
rule   CLAUDE.md section Step gating: "A report is its generated sections plus at most one
       hand-written paragraph." This report is the hand-written paragraphs and none of the
       generated sections.
judge  Four reds, none naming a finding or a site of the newest verdict, and none whose
       SUBJECT is this commit: a run exists at this sha (`44140076843`), FP1's push happened,
       so `python scripts/ci_section.py` and `--rounds` were both runnable here. They fail
       the FS1/FT1 predicate in both limbs, so **CZ1 (iv) applies unchanged.**
```

**The silently wrong result.** CI is **red at the judged commit** -- `lint, unit and guards`
concluded `failure` -- and no revision of the report says so. CE1 was adopted because CI had
been red at three consecutive reviewed commits with no revision saying so; this is the fourth,
and the report GI6 sends to Xabier carries no CI status at all. **Order matters and it is the
operative instruction: fix R1230 first.** Generating the section against the present header
anchors it on `c931885`, which replaces "no CI status" with "a CI status about the wrong
commit", and the second is worse than the first.

**R1232. (DOES NOT BLOCK -- the condition stands for the write run) R1225 (ii) IS RECORDED AND
NOT HELD, AND `pin_threads()` CANNOT BE WIRED AT THE CALL SITE THE DIFF CREATED.**

```
claim  the generation environment is "recorded in the provenance and held at the point of
       generation", which is what verdict 62's condition (ii) says
cmd    grep -n "pin_threads\|determinism\." scripts/export_f4_dynamic_inputs.py
out    :554  **determinism.report(),     -- and no other hit. `report()` only.
cmd    sed -n '64p;72p' scripts/export_f4_dynamic_inputs.py ;
       grep -n "Call before importing numpy" floatfea/determinism.py
out    64  import numpy as np
       72  from floatfea import determinism, hsp_pin  # noqa: E402
       floatfea/determinism.py:96  """Fix every BLAS/OpenMP thread count. Call before
                                      importing numpy."""
judge  **THE RECORDING HALF IS DONE AND IS THE RIGHT HALF TO DO FIRST.** An unpinned run now
       records `threads: {all null}` and `openblas_coretype: null`, which is a TRUE statement
       about the run, so an unpinned write run is loud rather than silent -- which is why
       this does not block under FR1. **The holding half is open, and the one-line repair is
       not available at `:72`:** the only import site the diff created is eight lines AFTER
       `import numpy as np`, and `pin_threads`'s own documented precondition is the opposite.
       Wiring it there would write `threads: {"OMP_NUM_THREADS": "1", ...}` into the
       provenance of a run whose BLAS had already initialised at the ambient count -- a
       provenance field that is false, which is strictly worse than the null it replaces.
       I did NOT measure a thread count and I assert none: there is no `threadpoolctl` here.
       What I assert is the documented precondition and the two line numbers.
```
*Closed when* either the pin is set before `import numpy` and the provenance records the
pinned values, or the write run is launched with the five `THREAD_ENV` variables set in its
environment and the report says that is the mechanism. **Either way: no write run before it.**
One ledger note on the same block: `baseline_conditions` is a tuple of prose sentences while
`versions` is a dict, so nothing can compare the two without a parse. Recorded, not asserted,
is what was asked for, so this is a note.

**R1233. (DOES NOT BLOCK) R1225 (i) IS SATISFIED FOR THE RULING AND NOT FOR THE SENTENCE IT IS
USED TO SUPPORT. ~200 eps IS CONSISTENT WITH THE PIN -- HERE IS WHY, SINCE YOU ASKED.**

The three rows are arithmetically right -- I recomputed every ratio and every eps count from
the pasted maxima (`4.3670e-14 / 196.7`, `8.5350e-15 / 38.4`, `5.4106e-15 / 24.4`) -- and the
answer is **yes, and the bound is two lines rather than a feeling**: a sequential convolution
over `N = 884` steps accumulates round-off between `sqrt(N) * eps` and `N * eps`, i.e.
**30 eps to 884 eps**, and 196.7 eps sits inside that band. `4.37e-14` relative is **twelve
decades** below the `1e-3` I named as "a different and larger finding" and ten below the six
figures `U = 1.71167` is published to. **It is round-off. Your reading is correct, and the
self-correction of the `1.210e-01` probe -- an elementwise ratio anchored on near-zero
entries, which measures the entry and not the array -- is the right diagnosis of the right
error.**

**What one case does not support is the sentence attached to it.** `--check` names **36 of
100** arrays across **six** cases; section 7 measures **three arrays of one case**. The
conclusion *"no published number can move"* is a claim over all six periods taken from one,
and `results/R1/example/member_forces.csv` publishes `G4.1` rows at every period. The
mechanism is period-independent and I expect the other five to look the same -- which is the
point: an expectation is what a measurement is for. **This does not block and is not a
condition of step 0**, because option 2 is not being taken and nothing is republished. It
**is** a condition of choosing option 2: the other five cases are measured before any
re-base, or the sentence is reduced to "at the governing period".

**R1234. (DOES NOT BLOCK -- FF0, next commit) `tests/test_report_vocabulary_corpus.py` HAS TWO
NEW REDS AND THEY ARE MINE, NOT YOURS.**

```
cmd    pytest -q tests/test_report_vocabulary_corpus.py, report present vs report moved aside
out    report present -> 2 failed: legitimate_open_row, two_spaces_before_the_item_number
       report absent  -> 32 passed
cmd    grep -n "legitimate_open_row\|two_spaces" tests/corpus/report_status_vocabulary.txt
out    :58  expect=allowed measured=allowed     row=| R231 | **open** - Q8 is locked; ... |
       :97  expect=allowed measured=allowed...  row=|  R230 | **answered** in section 1 |
judge  **BOTH `measured=` FIELDS WERE RECORDED IN A TREE WITH NO REPORT, WHERE THE GUARD
       COULD NOT RULE AT ALL.** `allowed` there meant "never evaluated", not "allowed" -- a
       baseline taken in a vacuous state, which is this project's own recorded guard applied
       to my own directory. The moment a report exists the shipped guard refuses two row
       shapes the corpus declares legitimate. Under FR1 the outcome is a refusal and so is
       loud, which is why it does not block; it is gating apparatus, so FF0 rather than the
       ledger. **I have NOT edited the corpus to match the guard** -- that is widening by
       another name -- and the test's own message names the two exits: repair the guard so a
       two-space indent and a hyphenated open row are ruled on, or declare the disagreement
       with a reason. The first is yours under EK2; if the guard turns out to be right, the
       re-measurement is mine and I will take it next round.
```

**R1235. (DOES NOT BLOCK -- FF0, and it was due in THIS commit) R1221 AND R1228 ARE
UNCHANGED.** Verdict 62's item 5 read *"R1227 and R1228 in the next commit (FF0, not the
ledger) ... R1221 is in the same file and belongs in the same commit."* This is that commit;
R1227 and R1229 are in it, these two are not, and the commit does not say they were left.
Measured: `tests/test_report_guard_states.py:117` still quotes
`max(_PLAN_STEP if _PLAN_STEP in REPORTED else 0, _PAIRED)` against the code's
`_PLAN_STEP is not None and _PLAN_STEP in REPORTED` at `:236`; and `EXPECTED` at this commit
**literally contains `'R2'`** -- the phantom id is the first element of the 27 printed under
R1230. **Both in the next commit.**

**R1236. (DOES NOT BLOCK -- ledger) TWO FIGURES IN THE REPORT THAT ONE COMMAND EACH REFUTES.**
Section 6's R1205 block pastes `out  ('R2', 1) R2.md`; the command it names prints
**`('R2', 0)`**. Section 9 predicts `test_the_plan_names_the_step_under_execution` "stays red
on the sentinel collision"; it **passes** (`1 passed`, measured), as verdict 62 and `R2.md:15`
both already recorded. The second is the more useful of the two, because section 9 is the
report's red trace and it predicts a red that does not exist while omitting the one that
blocks. Report prose, so FR1 does not block it -- but EG3 (i) asks for every red traced by
name, and the trace that exists is wrong in both directions. Also ledger:
`test_every_number_in_prose_is_sourced_in_its_own_section` is red on the preamble and on
sections 2, 3, 6, 7, 8 and 9, plus `test_a_table_of_numbers_shows_where_it_came_from[8.
Carried]`.

**WHAT THIS COMMIT GOT RIGHT, AND IT IS THE LARGER PART OF IT.** GI3 (a) is the measurement I
most expected to have to re-derive, and it reproduces exactly: I rebuilt the momentum balance
from `case1/m_xddot`, `case1/contrib` and `case1/pair_body` myself and got `2.414413e+01`
against `2.414287e+01` on the platform and `1.4537e+01 / 1.4534e+01` on hub1, ratio 1.0001 --
the report's own table -- and the judgement that a "share" between the two sides is 1:1 by
construction is right, and is the honest answer to a question GI asked in a form the model
cannot answer. The static/dynamic decomposition is exact: `269.72` and `455.72 MPa`,
`My static 1.916016e+08`, `Mz dynamic 2.689043e+08`, and the dynamic `My` of `-1.141810e+07`
is `total_instant - static` to the digit, all read out of the published CSVs. All six
utilisations check (`1.71167` twice, `1.18223`, `1.17709`, `0.808211`, `0.790493`). Section
2a's loop-gain table is internally consistent at every one of its 24 cells and its control
`2059.7 t` reproduces; section 5's deck census is exact on all 17 bodies and `43 005 t` is
`344.04 kg x 50^3` to the tonne. **And three figures were corrected against the author's own
earlier statements before anyone asked** -- 74 minutes to 26, the ballast sign, and the
`1.210e-01` probe -- each with the reason the first version was wrong. The
`(1 - 0.75) x 2500` corroboration in section 4 is the kind of cross-check that catches a
basis error, and it is the second time this step has found one that way.

## Tolerances touched

**None, measured twice.** `git diff 0901933..HEAD -- floatfea/tolerances.py` is 0 lines, and
`git diff 0901933..HEAD | grep -cE "^[-+].*_COUNTER"` is `0`. **EU1 therefore does not
arise**, and I ran the model at configurations the diff did not choose anyway -- which is
where R1226's closure and R1234 came from. One tolerance-shaped thing remains implicated and
is not a tolerance: `--check`'s comparison is `np.array_equal` with no threshold, by Q8's
rule. **If any answer to R1225 introduces a tolerance on that comparison, that is a widening
and it is refused.** R1218's row-1 form question is still unwritten and becomes CZ0 (b) at
step 2.

## Corpus

**One batch, committed separately at `91f083d`: `tests/corpus/hsp_worktree_key_provenance.txt`,
28 entries, all new.** GC3 left the pause expired, so this is my own call under GA3's length
target. The surface is the one this step's only code change touches: GI3(e) turned a wrong
path from a MISSING directory into a RESOLVING one, so the question became whether the tree
that was read is the tree the artifact declares.

**12 of the 28 measured this round. 6 caught, 3 reach a green `--check`, 1 correctly needs no
refusal, 1 is not live on this tree, 16 carried unmeasured.** The three that get through:
a real directory *named* `HSP-stable` holding other content (`current`, exit 0); the stable
key set to the **empty string**, which falls through as unset and exits **0** with *"HSP-stable
absent, so the snapshot cannot be re-derived here"* -- a gate that could not compare returning
0, which is *empty parameter set is an error, not a skip*, and which is pre-existing rather
than in this diff; and a stable tree at another tag with byte-identical source, where nothing
is wrong because `hsp_tag` is a literal on both sides. Both entries verdict 62 said it would
write are in it, and `declared_tag_is_a_literal` is still live. **What I ran beside the batch**
is the recorded substitute, and it is where R1230 came from: a regeneration check on a
published deliverable (the EB6 snapshot, in a throwaway tree, in both directions) and a
continuum over the parameter space the new resolver guards.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN** -- which GI6 holds anyway, so this HOLD costs
no schedule, and you are right that it does not. **Rounds: this consumed revision 1 of 3
under ES0. Two remain.** R1226, R1227, R1229 and R1225 (iii) are **DISCHARGED and are not
re-measured**, and two conditions of my own are **WITHDRAWN** (the `_PAIRED` half of R1227,
and the marker's cause). What remains, in this order, because the order is load-bearing:

1. **R1230 -- the header to `0901933`, AND the 32-id carry list in the same commit.** Not the
   header alone: section 8, `step-0-answers.json` and the generated Carried table move
   together, or the next revision is red by five more than this one.
2. **R1231 -- `python scripts/ci_section.py`, `--rounds`, and the whole-suite line, AFTER
   item 1.** CI is red at this sha and the report has to say so.
3. **R1232 -- no write run until the pin is above `import numpy` or in the invocation's
   environment, and the provenance records the pinned values.** The recording half is done.
4. **Conditions 4 and 6 -- unchanged, still subordinate to R1225, still red with their cause
   named.** Do not clear the staleness guard by writing a provenance whose npz moved for an
   unrecorded reason.
5. **Condition 7 -- a concluded, GREEN ladder in CI.** Rungs 1-3 are green at this sha; 4 and
   5 have still never run in CI during this step.
6. **R1234 and R1235 in the next commit (FF0, not the ledger).** R1233's five remaining cases
   only if option 2 goes on the table.

**Nothing here is a STOP, and I considered it on the ladder.** Rungs 1, 2 and 3 are SUCCESS in
CI at this commit, which is the first time this step has had that; the two local reds are a
provenance comparison and a regeneration comparison rather than numerical disagreements at a
rung, and R1225 established that what moved is the committed golden and not the code. No
`floatfea/` file is in this diff. The locked plan is faithful to GI and needs no reopening,
and `R2.md` section 6 item 2 is still the one clause I rule must NOT be triggered yet.

**And I disagree with nothing in the criterion this round.** FR1 did the work it was adopted
for: R1233, R1234 and R1236 would each have been a blocking round under the unamended CZ0,
and each is a line here instead. The two findings that block are both "a wrong number in a
report, silently" with the sentence written out, which is the test FR1 asks for and the
reason it is cheap to apply.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 9e1092a35eed45ee5351789778a3c50752af1bb1
**Reviewed commit: `9e1092a35eed45ee5351789778a3c50752af1bb1`.**
Verdict: HOLD
Scope: **ES0 INTERIM CHECK on the OPEN step, the third.** `git ls-files docs/reports/R2` is
EMPTY, so no new report revision exists and this **counts against none of step 0's three
revisions** and closes nothing; `--closes` is correctly absent (FK1). Light per ES0: the
suite, CI at the commit, a CZ0 (a)-(d) scan of the diff. **Ruled under FR1 with EZ0**, and
each blocking finding names the silently wrong result it produces. **GE3: `R835: unchanged,
R2`. Not re-measured.** 1b does not arise -- there is no report, so there is no `Answers:`
header to compare against the newest verdict.
**EU1 does not arise, measured not taken:** `git diff 3d24e1c..HEAD -- floatfea/tolerances.py`
is 0 lines, so is `git diff 91c2d2e..HEAD`, and `git diff 3d24e1c..HEAD | grep -cE '^[-+].*_COUNTER'`
is `0`. I ran the adversarial case anyway and it is where both blocking findings came from.
**CH2/CI0: `git ls-files -- tests/conftest.py 'tests/**/conftest.py'` returns `tests/conftest.py`,
and `git diff 3d24e1c..HEAD` over it is 0 lines. No new conftest, no new plugin.**
**4b: `git diff 3d24e1c..HEAD -- .claude docs/SUPERVISOR.md` is 0 lines. No STOP-class finding.**
Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`.**
* `tests/unit` + the four root guards: **703 passed in 196.31s.** That is verdict 60's 692 at
  `3d24e1c` plus the new file's 10 plus one parametrised root-guard case over the new file.
* `tests/verification/rung4/test_f4_g41_dynamic.py` + `tests/regression/test_f6_deliverable_agrees_with_itself.py`:
  **2 failed, 138 passed in 146.11s.** The two are conditions 4 and 6 BY NAME --
  `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` and
  `test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree`. Both still open.
* the new file's revert-red-restore cycles, **run by me rather than taken**: R1214's `raise`
  reverted to `tried.append(...); continue` gives **2 failed, 8 passed**; R1213's name test
  disabled with `if False and ...` gives **1 failed, 9 passed**; **R1219's anchor removed
  gives 1 failed, 9 passed, a cycle the commit did not report**; all restored gives
  **10 passed**, with `git status --porcelain` empty.
* **CI's own wide guards selection**, `pytest tests --ignore=tests/unit
  --ignore=tests/verification --ignore=tests/regression`, in my worktree: **172 failed, 1057
  passed, 1 skipped in 555.85s**, and the reds are confined to THREE files --
  `test_report_carried.py` 151, `test_report_guard_states.py` 20,
  `test_report_numbers_are_sourced.py` 1. **No root test outside the report guards is red at
  this commit.** Per-id ruling under FS1/FT1 below.
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`, `mypy floatfea`:
  **all clean, my own runs** -- 163 files unchanged, 45 source files.
* **NOT RUN LOCALLY and I say which rather than implying coverage:** rungs 1, 2, 5, 6 and
  `tests/regression` beyond the one deliverable test. The diff's only `floatfea/` file is
  `hsp_pin.py` (32 lines) and the only rung tests reaching it are rung 3's deck export and
  rung 4's G4.1, both run above; FV1 puts the rest on CI.
CI: **run `44133344180` at the FULL sha `9e1092a35eed45ee5351789778a3c50752af1bb1` EXISTS, so
FP1 held.** `lint, unit and guards` **CONCLUDED FAILURE at step 10 `guards and meta-tests`**,
with `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all **success** before it
-- so the guards step is seen to have RUN rather than been skipped behind an earlier red
(CZ1 iii), and CI's `mypy` passes at the pinned toolchain this time. **`the verification
ladder` had NOT finished when I ruled** (`in_progress`, runner `GitHub Actions 1000001919`,
started 17:06:50Z); a run that has not finished is not a pass. Both determinism jobs
`skipped` by their own `workflow_dispatch` condition. **NOT CK2** -- runners `1000001918` and
`1000001919` were assigned and both jobs executed for minutes. **CA2 IS REACHED: CI is red at
the judged commit.** CI's per-id list is **UNAVAILABLE, not skipped over**: `gh run view --job
<id> --log-failed` answers *"run 44133344180 is still in progress; logs will be available when
it is complete"* while the ladder runs, so the id-for-id agreement with my local 172 is
deferred -- but my local run IS that selection, so nothing is hiding inside CI's aggregate
that I have not measured. GC2 does not arise: the diff touches `floatfea/` and `tests/`.
Door (FV2 / GG2): `git worktree add -b review/9e1092a35eed <a path outside the repository>
9e1092a35eed45ee5351789778a3c50752af1bb1` **succeeded on the first try, so no review of this
commit existed.** Every measurement above was taken in that worktree; this verdict is written
there through `scripts/write_verdict.py` (`grep -nE '"(commit|add)"|check_call|\.run\(' ` over
it: no match), committed on that branch and pushed -- merge with `git merge --ff-only
origin/review/9e1092a35eed`. **Writes of my own, all in my own worktree and all reverted
before committing:** the three revert cycles, a planted `docs/reports/R2/step-0.md` for the
R1227 cell, and the plan marker moved to `3` and back for the provenance cell.
`git status --porcelain` in my worktree is empty. In `C:\dev\floatfea` I ran only read-only
`git` and `gh`. **Two read-only things I ran outside the repository and disclose rather than
leave for you to find:** `git -C <HSP-runs> describe/rev-parse/status --porcelain`, and
`export_buoy_centers_ref.py --check` under two values of `FLOATFEA_HSP_STABLE` -- `--check`
compares and writes nothing (`:188`). Neither wrote a byte anywhere.

## Carried

Verdict 60's five conditions and verdict 61's two. **FIVE ANSWERED, TWO OPEN, and one of the
five answered its condition without closing its finding.**

* **R1213 (the DS0 refusal that did not fire) -- ANSWERED, verified three ways.** The name
  test is at `run_floatsim_design_waves.py:112-119`, **beside** the identity test at `:120`
  and not replacing it (EK2), and `test_the_DS0_refusal_fires_when_the_RUNS_key_names_the_STABLE_tree`
  drives `preflight()` rather than reading its source. Revert cycle: **1 failed**. And the
  adversarial case the commit did not run -- a **case-folded** value:
  ```
  cmd  Path('C:/users/xlama/onedrive/documents/buoy/hsp-stable').resolve().parts
  out  ('C:\','Users','xlama','OneDrive','Documents','buoy','HSP-stable')
       NAME TEST ("HSP-stable" in parts): True
  rule run_floatsim_design_waves.py:112; Windows `resolve()` restores the on-disk case for an
       existing path, so the predicate is not defeated by the casing of the declaration
  ```
* **R1214 (set-but-wrong silently discarded) -- ANSWERED AS WRITTEN, and the finding is not
  closed: see R1226.** The condition was *"a source that is set and not a directory is a
  refusal and only an unset source falls through"*, and that is exactly what shipped
  (`hsp_pin.py:120-126`, with the legacy sibling moved outside the loop at `:128-130`). Both
  directions (EH4): revert gives **2 failed**; unset still resolves through. **And the
  direction the condition did not ask for, measured because R670 is the reason
  `require=False` exists:** a set-and-wrong key now raises `SystemExit` from a module-level
  constant in six scripts, so I checked it cannot take a rung down in collection --
  `FLOATFEA_HSP_RUNS=C:/nope/not/a/worktree python -m pytest --collect-only
  tests/verification/rung4 tests/verification/rung3` gives **670 tests collected in 0.75s, no
  errors.** R670 is not resurrected.
* **R1206 (`0` is both a legal step number and the resolvers' sentinel) -- THE CONDITION'S
  THREE LINES ARE FIXED AND THE FINDING IS NOT CLOSED. R1227 below, with the cell.** Exit
  (iii) was the right exit and the escalation was rightly withdrawn; `_plan_step() is not
  None` is green, `check_carried._active_step()` is `('R2', 0)`, `ci_section` is `R2 0`, and
  `test_R887_the_plant_base_is_the_step_the_GUARD_reads` passes its `STEP == guard.STEP`
  assertion. A **fourth** site of the same `> 0` collision is live.
* **R1215 (the marker comment said the opposite of the marker) -- ANSWERED.** `R2.md:5-25`
  now reads `IT READS 0, WHICH IS WHAT IS UNDER EXECUTION`, with the withdrawn escalation and
  its refuting grep recorded. Read against the diff, not inferred.
* **R1216 (the census described the pre-change tree in the commit that changed it) --
  ANSWERED.** `R2.md:208-223` states BOTH counts and names why they differ. **R1219 --
  ANSWERED** (`hsp_pin.py:106-111`), and I measured the revert cycle the report did not.
  **R1220 -- ANSWERED**, with one defect in the new file: R1229.
* **CZ1 (iv), the rung-4 staleness red (condition 4) -- OPEN.** Confirmed red in my own run.
  **The diagnosis offered for it is refuted by a measurement already in this repository:
  R1225.**
* **R1223 (the published deliverable stops regenerating, condition 6) -- OPEN.** Confirmed
  red in my own run; the four differing lines are the same `pass` to `FAIL` and `116 passed`
  to `1 failed, 115 passed` cells verdict 61 named. **Not touched, which is right.**
* **Condition 7 (the follow-on commit's own CI run GREEN on the LADDER) -- NOT MET.** The
  ladder job at this sha is still `in_progress`, so **rungs 4 and 5 remain unmeasured in CI
  at any commit of this step.** That is the hiding CZ1 (iii) exists for; the condition stands.
* **R1222 -- ANSWERED, and the prediction verdict 60 recorded before measuring is
  CONFIRMED.** `test_a_blocking_item_is_not_routed_to_4a` is **green** at this commit, because
  the newest verdict writes dispositions in the parenthesised form the parser needs: that id
  plus `test_the_plan_names_the_step_under_execution` give **2 passed**. Withdrawn.
* **R1217, R1218, R1221 -- STILL OPEN**, unchanged and not answerable by this commit (R1218
  becomes CZ0 (b) when step 2 writes the entry; R1221 is FF0 and belongs with R1227 in the
  same file). **`declared` is still a config key no config declares.** **Verdict 58's twelve
  items and verdict 59's four report items -- STILL OPEN, due in R2's first report.**
  **R1212, R1203, R1204 -- reviewer-side or Xabier's. R1224 -- mine, recorded, no action.**

## Findings

**R1225. (BLOCKS) THE `--check` REFUSAL IS NOT THREAD COUNT. The npz golden moved when THIS
REPOSITORY'S OWN numpy/scipy PIN moved, and the ablation cell is already in the git history:
`--check` was GREEN before the pin and refuses after it, with the thread count unpinned on
BOTH sides.**

```
claim  `--check` ran with no thread pins, and the six named arrays are what multi-threaded
       BLAS would perturb  (the commit message's diagnosis)
cmd    git log --oneline -1 -- data/f4/dynamic_inputs.npz
out    62a8281  R1 step 1 revision 3
cmd    git show cfb76ff   (R1 step 2, first commit -- AFTER 62a8281, npz untouched since)
out    cmd  python scripts/export_f4_dynamic_inputs.py --check   (on the shipped npz)
       out  100 arrays reproduce the committed file EXACTLY      (exit 0, no stray file)
cmd    git log --oneline -S "numpy==2.5.4" -- constraints-dev.txt
out    09d5bc9  R1 step 2, revision 1: FQ0-FQ3, and a refusal site nobody had named
cmd    git merge-base --is-ancestor cfb76ff 09d5bc9 ; echo $?
out    0        -- the GREEN --check PRECEDES the pin move
cmd    constraints-dev.txt, the FQ3 block's own measured table
out    numpy  local 2.4.0   CI 2.5.4        scipy  local 1.17.1   CI 1.18.1
       "a minor bump in either can move the last bits of a linear solve. The verification
        ladder asserts at ULP scale, so 'can move a number' is not hypothetical here"
       "FQ3: if the golden moves under these pins, STOP and report rather than re-baselining."
cmd    python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
out    2.5.4 1.18.1          -- i.e. AT the pin, which is the value that moved
cmd    git grep -ln "pin_threads\|OMP_NUM_THREADS" -- scripts floatfea pyproject.toml
out    floatfea/determinism.py   floatfea/hsp_pin.py
       -- nothing in the export path pins threads, and nothing did at cfb76ff either
cell   ONE VARIABLE ACROSS THE GREEN/RED BOUNDARY. Thread count: unpinned at cfb76ff
       (green, 100 arrays EXACT) and unpinned today (red, 36 of 100 differ). numpy and
       scipy: moved, by the named commit, between the two.
rule   scripts/export_f4_dynamic_inputs.py:476-500 -- np.array_equal, Q8's golden rule,
       "there is no tolerance on this comparison"
judge  **THE THREAD COUNT IS HELD CONSTANT ACROSS THE BOUNDARY, SO IT IS NOT THE CAUSE.**
       The diagnosis cites `ci.yml:67-69`; three lines BELOW that citation the same file
       says *"THE BLAS KERNEL, PINNED (CF1). Thread count alone was not enough."*
       `OPENBLAS_CORETYPE` is unset locally. And 36 of 100 arrays differ while all 64 input
       arrays are bit-identical -- the signature of a solver-bit move, not of inputs that
       moved. Measured: HSP-runs is at `floatfea-ref-1` / `25de7ce`, clean but for the
       untracked `floatfea_design_waves/` export, so no input moved either.
```

**The silently wrong result, in the form FR1 asks for.** Condition 4 as verdict 60 wrote it
says *"then a full **write** run, which is the only thing that rewrites `import_closure`"*.
Executed on this machine that overwrites `data/f4/dynamic_inputs.npz` with arrays computed at
numpy 2.5.4 / scipy 1.18.1 / an unpinned OpenBLAS kernel, writes a fresh provenance **that
records none of those three** -- there is no `threads`, no `coretype` and no library version
in `dynamic_inputs.provenance.json`, I read every key -- and moves every `G4.1 force` and
`G4.1 moment` figure in `results/F6/floatfea_results_report.md`, a file sent to Xabier, for a
toolchain reason, **with the staleness guard and R1223's deliverable test both going GREEN to
confirm it.** That is CLAUDE.md's golden-file rule verbatim: *"Regenerating a golden file to
match new output, without that explanation, is the same error as widening a tolerance."* The
npz is the one canonical artifact that **cannot** be produced in the canonical environment --
CI checks out no HSP worktree, which is EX0's whole reason -- so Q8's "CI is canonical" does
not reach it, and `tests/test_ci_canonical_environment.py` reads the workflow, not this file.

*Closed when* three things are true. **(i)** The **magnitude** is measured and reported per
array -- max |fresh - committed| and its ratio to the array's own scale, with the operating
point. `--check` prints names only, correctly, because FP2/C20 made it a gate and not a
report; so this is a one-off probe under `/tmp`, not apparatus. A last-bits move (relative
`~1e-16`) is consistent with the pin; `1e-3` is a different and larger finding. *A residual
destroys information* -- 36 names cannot tell a wrong sign from a wrong magnitude. **(ii)** No
write run until the environment the regeneration runs under is recorded in the provenance and
held at the point of generation. `floatfea/determinism.py` already has `pin_threads` and
`report()` and nothing in the export path calls either, so this is wiring and not new
apparatus. **This answers your question directly: FF0-class, next commit, not a ledger row** --
`--check` is the thing that decides whether the committed npz is believed and whether `R2.md`
section 6 item 2 fires, it reported REFUSED with no defect established, and EK2 says a guard
that fails false is fixed. **(iii)** The escalation is raised under **FQ3**, not under `R2.md`
section 6 item 2. *"If it refuses again with the pins set, I read that as section 6 item 2's
escalation"* -- **no.** That item asks whether a **zero-change FloatSim re-run** is
bit-identical, and the premise is untested while numpy, scipy and the BLAS kernel all sit off
the values the artifact was built under; reopening the R2 plan on it attributes to FloatSim an
effect this repository has already measured twice, CF1 by CPU vendor and FQ3 by library minor.
FQ3's ruling already covers it: **STOP and report rather than re-baselining.** *A causal claim
carries its ablation*, and this one cost three `git log` commands. **If the pinned re-run in
flight comes back GREEN, R1225 still stands:** a bit-exactness gate whose answer depends on
unrecorded ambient conditions is the finding, and a pass does not record them either.

**R1226. (BLOCKS) R1213 ONE KEY OVER: NOTHING TIES THE TREE THE STABLE KEY NAMES TO THE TREE
THE SNAPSHOT DECLARES, AND I RAN IT WITH A CONTROL.**

```
claim  the two-key split makes a stable key pointed at the runs tree safe
cmd    FLOATFEA_HSP_STABLE=.../buoy/HSP-runs    python scripts/export_buoy_centers_ref.py --check
out    EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1, 12 buoys and 4 hubs.
       exit=0
cmd    FLOATFEA_HSP_STABLE=.../buoy/HSP-stable  python scripts/export_buoy_centers_ref.py --check
out    EB6 reference: current. blob b8b8123904af, tag floatfea-ref-1, 12 buoys and 4 hubs.
       exit=0      (the control)
cell   ONE VARIABLE -- the tree the key names. The two outputs are BYTE-IDENTICAL and both
       exit 0, so the gate that certifies the EB6 reference cannot tell which worktree it
       was derived from.
rule   scripts/export_buoy_centers_ref.py:172  "source": f"HSP-stable/{SOURCE_REL}"  <- a LITERAL
                                         :176  "hsp_tag": hsp_pin.HSP_TAG            <- a MODULE CONSTANT
                                         :180  "blob_sha": _blob_sha(source)         <- from WHICHEVER tree
cmd    grep -n SystemExit scripts/export_buoy_centers_ref.py
out    :75 "is not a file"  :93 "could not read the blob sha"  :111 :135 :146 :167 (parse/shape)
       -- no DS0 name refusal, no tag refusal, no dirtiness refusal, on any line
```

**The silently wrong result.** `data/platform/buoy_centers_ref.json` -- a committed data file
and the input to EB6's label-provenance gate -- regenerated from the **runs** worktree while
its own `provenance.source` declares `HSP-stable/studies/platform-12buoy/platform_common.py`
and its `provenance.hsp_tag` declares `floatfea-ref-1`, **because both are literals that
cannot be wrong**, with `blob_sha` taken from the other tree's index so both sides move
together and `--check` prints `current`. That is FR1's second head verbatim, and CLAUDE.md's
own note on that head covers this case word for word: *"No number was wrong in any artifact at
the time, and the input was used other than as declared."* **Both worktrees are at the same
tag today -- `blob b8b8123904af` from either -- so nothing in the tree as it stands is wrong,
and I say so rather than overstating it.** `hsp_pin.py:36-46` states this hazard in prose and
names this file as the reason there are two keys; what it does not do is refuse it, and
GI3(e) is what made a key able to name the wrong tree at all, exactly as it did for R1213.
**A second limb, same file, from reading rather than running:** `:153` reads the constants
from the WORKING file (`source.read_text()`) while `:88-93` takes `blob_sha` from
`git rev-parse HEAD:<rel>`, so a dirty stable worktree records a sha for a version of the file
the numbers did not come from.

*Closed when* `export_buoy_centers_ref.py` refuses a stable key whose resolved path is not
`HSP-stable` -- the one-line predicate this commit just wrote at
`run_floatsim_design_waves.py:112`, inverted -- or declares the tree it actually read instead
of the literal; with both runs pasted and the control beside them (EH4). The dirtiness limb
closes with `--dirty` on the describe, or by taking the sha from the working file; **say which
and why**, not both.

**R1227. (DOES NOT BLOCK -- FF0, next commit, not the ledger) R1206's FOURTH SITE:
`tests/test_report_carried.py:579` still reads `assert STEP > 0`, and it goes red with a FALSE
message the moment the step-0 report lands -- which is your next commit.**

```
cmd    plant a minimal docs/reports/R2/step-0.md in my own worktree, then
       pytest -q tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    E  AssertionError: reports exist for steps [0] and verdicts for [0]; no step has
          both. There is no carry list to check.
       E  assert 0 > 0
       tests\test_report_carried.py:579
       1 failed   (and test_the_plan_names_the_step_under_execution: 1 passed)
rule   tests/test_report_carried.py:579, inside test_the_guard_reads_the_step_being_worked_on
judge  step 0 HAS both, so the message is FALSE -- `0` is the sentinel AND the value, which
       is R1206 verbatim at a site its three line numbers did not name. The condition asked
       for `:100`, `:111` and `:617`; those three are fixed and the finding is not.
```

Three things make this more than one line. **The assert is FIRST in its test, so three further
assertions in the same function are dead for the whole of step 0** -- the spelling check,
`STEP_REPORT == _PAIRED`, and `STEP_REPORT - STEP <= 1`, which is the one that forbids opening
step k+1 over an unreviewed step k. **The obvious repair makes one of them silently vacuous:**
`_PAIRED` at `:229` is `max(REPORTED & REVIEWED) if ... else 0`, so at step 0 the sentinel
equals the value there too -- fix `:579` alone and `STEP_REPORT == _PAIRED` passes at step 0
whether a verdict exists or not, which is loud today only because `:579` fires first.
**Treat `:229` in the same commit.** And it changes the class of one red next revision:
`test_the_guard_reads_the_step_being_worked_on` is state (2) today (`assert REPORTED`, no
report directory) and becomes **CZ1 (iv)** the moment the report exists, because the answering
report does not clear it. A third measurement, on provenance rather than existence:
`marker 0 -> STEP 0, REPORT step-0.md` and `marker 3 -> STEP 0, REPORT step-0.md`, so the plan
marker currently has **no effect** on which report the guard reads -- the `else 0` arm is doing
the work, and the repair's claim that the resolver follows the plan is not demonstrated by
this tree.

**R1228. (DOES NOT BLOCK -- FF0, next commit) `tests/test_report_guard_states.py:117` quotes
the expression this commit changed.** It reads *"The guard resolves `max(_PLAN_STEP if
_PLAN_STEP in REPORTED else 0, _PAIRED)`"*, while `test_report_carried.py:236` now reads
`max(_PLAN_STEP if _PLAN_STEP is not None and _PLAN_STEP in REPORTED else 0, _PAIRED)`. BP0 at
the smallest scale, inside the gating apparatus, and the same shape as R1215 which this commit
fixed one file over: a figure whose rule moved underneath it, in the file that exists to hold
the other guard's resolution.

**R1229. (DOES NOT BLOCK -- ledger, and the direct answer to your question)
`tests/unit/test_hsp_worktree_resolution.py:123` IS AN ASSERTION THAT CANNOT FAIL, and it is
the ONLY other one of that shape in the file.**

```
cmd    sed -n '121,123p' tests/unit/test_hsp_worktree_resolution.py
out        got = hsp_pin.worktree("runs")
           assert got.name == "HSP-runs"
           assert not got.is_absolute() or True  # the value is a path, existing or not
rule   `X or True` is True for every X -- in the file whose own docstring says "A check that
       cannot fail is not a check (CW0)", eleven lines above it
judge  Delete it; `:122` is the real check and it does fail if `worktree()` refuses or
       returns another name. I checked the other nine individually: four are held by the
       revert cycles I ran (R1213, R1214 twice, R1219), and the remaining five -- the
       precedence pair, key independence, `require=True`, the unknown key -- each drive
       `worktree()` or `preflight()` and assert on the returned value or the raised message,
       so each can fail. **One, and this is it.**
```

Two smaller notes against the same file, both ledger. The R1213 test's message assertion is
`"HSP-stable" in message and "DS0" in message`, and the **identity** refusal's message
(`"the runs worktree is HSP-stable, which is read-only from here (DS0)"`) satisfies both
clauses -- so the assertion cannot tell which of the two refusals fired, which is R1213's whole
content. It is not vacuous here, because `:209` asserts the two keys differ and the identity
path therefore cannot fire; a match on `R1213` or `by NAME` would make it say what it means.
And `:148-161` creates and `rmdir`s `HSP-runs-r1219-probe` **in the repository root**, outside
`tmp_path`, in the file whose docstring says *"NOTHING HERE TOUCHES A REAL WORKTREE"*: an
interrupted run leaves it behind, and `mkdir(exist_ok=True)` with an unconditional `rmdir`
deletes a pre-existing directory of that name. It cleaned up correctly in my run --
`git status --porcelain` empty.

**FS1/FT1 PER-ID RULING ON THE 172 REDS, checked against each id's own failure rather than by
family name (EG3 (i)).** State **(2)** throughout: a verdict exists, the answering report does
not, `git ls-files docs/reports/R2` is empty. **Limb one** -- names a finding or a site of the
newest verdict -- takes the 110 `test_every_named_site_is_touched_or_declared[R12xx-<path>:<line>]`
and the 27 `test_the_report_carries_the_finding[R12xx]`, each of which carries a verdict-60 or
verdict-61 finding id **in its own parameter**; that is the whole of R835, the count being a
function of what the reviewer wrote. The 19
`test_report_guard_states.py::test_the_guard_survives_the_state[...]`,
`test_R887_the_plant_base_is_the_step_the_GUARD_reads` (*"the harness copies FROM step-0.md,
which does not exist"*, with its `STEP == guard.STEP` assertion PASSING),
`test_report_numbers_are_sourced.py::test_the_report_parsed_into_sections`, and the 12
`test_report_carried.py` singletons about the absent report --
`the_report_names_the_verdict_it_answers`, `carries_a_CI_SECTION`,
`reported_CI_counts_are_not_all_zero`, `the_Carried_table_is_what_the_generator_produces`,
`the_ROUNDS_SECTION...`, `a_carried_row_points_at_a_section_that_discusses_it`,
`a_report_does_not_say_CLOSED`, `there_are_pointers_to_resolve`,
`the_parse_found_something_to_check`, `the_generator_would_catch_a_row_under_the_wrong_number`,
`the_CI_section_is_about_the_REVIEWED_commit`, `the_guard_reads_the_step_being_worked_on` --
are each about the report that answers this verdict and clear when it is written (EG3 state
(2), cleared BY THE ANSWERING REPORT and not by time). **Limb two** -- subject IS the commit
carrying it -- takes the remaining two, as FT1 names them:
`test_the_report_carries_a_WHOLE_SUITE_count` and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`. **No id fails the predicate, so no red here
is CZ1 (iv)** -- with the single exception R1227 records, whose class changes next revision.
**R835: unchanged, R2 (GE3).** Not re-measured further.

## Tolerances touched

**None, measured twice.** `git diff 3d24e1c..HEAD -- floatfea/tolerances.py` is 0 lines and so
is `git diff 91c2d2e..HEAD -- floatfea/tolerances.py`. No declared counter moves:
`git diff 3d24e1c..HEAD | grep -cE "^[-+].*_COUNTER"` is `0`. **EU1 therefore does not arise**,
and I ran the model at configurations the diff did not choose anyway -- which is where R1225
and R1226 came from. One tolerance-shaped thing is implicated by R1225 and is NOT a tolerance:
`--check`'s comparison is `np.array_equal` with no threshold, by Q8's rule, and nothing in
R1225 asks for one. **If any answer to condition 4 introduces a tolerance on that comparison,
that is a widening and it is refused.**

## Corpus

**No batch, and ES0 is why, not GC3.** An interim check is light by rule: *"No corpus batch,
no closure list."* My own instructions say "add unseen entries at every review"; where the two
differ CLAUDE.md governs and I say so rather than quietly following the looser one.
**What I ran instead is the recorded substitute, and it produced both blocking findings:** a
continuum over the parameter space the new resolver guards (the stable key at the runs tree
with a control, a case-folded value, a set-and-wrong key through collection of two rungs, the
plan marker at 0 and at 3, three revert-red-restore cycles) plus a **regeneration check on a
published deliverable** -- the F6 results report and the npz, which is where R1225 lives.
Nothing in `tests/corpus/` covers worktree-key *provenance* as against resolution;
`stable_key_names_the_runs_tree` and `declared_tag_is_a_literal` are the entries I would write
next round if R1226 is not closed by then.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN** -- which GI6 holds anyway, so this HOLD costs
no schedule. Step 0's remaining work (the FloatSim run, GI3(b)'s wall time, (a) and (d)) is
the right work to continue with. **Conditions 1, 2, 3-as-written, 5, and R1216/R1219/R1220 are
DISCHARGED and are not re-measured.** What remains:

1. **R1225 -- the magnitude, then the decision, then the escalation under FQ3.** (i) the
   per-array magnitude and its ratio to that array's own scale, pasted, with the operating
   point; (ii) **no write run** until the generation environment is recorded in the provenance
   and held at the point of generation, through the existing `floatfea/determinism.py` (FF0,
   next commit); (iii) if it is a last-bits move, the escalation is **FQ3** -- *STOP and
   report, do not re-baseline* -- and **NOT** `R2.md` section 6 item 2, whose premise is
   untested while the pin sits off the artifact's basis. A green pinned re-run does not close
   this; it only changes which sentence is written.
2. **Condition 4 (the staleness red) and condition 6 (R1223) -- UNCHANGED and now subordinate
   to R1225.** Verdict 60's ordering was right and is what saved the npz; what has changed is
   that the second half of it is not available yet. **Do not clear the staleness guard by
   writing a provenance whose npz moved for an unrecorded reason** -- that turns both reds
   green and publishes the move. If answering R1225 means the figures legitimately move, that
   is a golden-file change and it carries a written explanation naming the pin commit
   `09d5bc9`, per CLAUDE.md section Testing.
3. **Condition 7 -- a concluded, GREEN ladder in CI at the follow-on sha.** Rungs 4 and 5 have
   not been measured in CI at any commit of this step.
4. **R1226 -- the stable key refuses a tree that is not `HSP-stable`, or the snapshot declares
   the tree it read.** Both runs pasted, control beside them (EH4), and the dirtiness limb
   answered or declared left with its reason.
5. **R1227 and R1228 in the next commit (FF0, not the ledger), and R1227 covers `:229` as well
   as `:579`.** R1221 is in the same file and belongs in the same commit. **R1229 is a ledger
   row: delete the line.**

**And for the step-0 report itself, so the next revision is a revision and not a round:** its
`Answers:` header names **THIS verdict and this sha** (`9e1092a35eed45ee5351789778a3c50752af1bb1`),
not verdict 60 or 61 -- the newest verdict is the one the guard checks against and the one
thing a machine cannot check. EG3 (ii): paste the report-guard files run AT my verdict commit;
verdict 61 asked for that figure at `b2dc268` and gave 187 to compare against, and at this
commit the wide guards selection is **172 failed, 1057 passed, 1 skipped**, of which
`tests/test_report_carried.py` is 151. Verdict 58's twelve open items and verdict 59's four
report items are due in it.

**Rounds: step 0 has consumed NONE of its three ES0 revisions.** Verdict 59 was the plan lock;
60, 61 and this are interim checks. The next report revision is the first.

**Nothing here is a STOP, and I considered it twice.** Rung 4 is red and one `tests/regression`
test is red, which read like low-rung failures -- but both are provenance and regeneration
comparisons rather than numerical disagreements at a rung, and R1225 establishes that what
moved is the committed golden and not the code: `git diff --stat 3d24e1c..HEAD -- floatfea` is
`hsp_pin.py` alone, 32 lines, and rungs 1, 2 and 3 were SUCCESS in CI at the previous sha over
byte-identical rung code. The locked plan is faithful to GI and needs no reopening; **`R2.md`
section 6 item 2 is the one clause I am ruling must NOT be triggered yet**, which is the
opposite of reopening it. If Xabier's answer under FQ3 is that the npz is re-baselined at the
pin, that is a golden-file change with a written explanation, not a plan change.

**What this commit got right, and it is the larger part.** Five conditions answered in one
commit with no re-measurement asked for. Each repair is held by a test that reddens when the
repair is reverted, and I ran all three cycles myself rather than taking them -- plus a fourth,
R1219's, that the report did not claim. **The commit found and fixed a check of its own that
could not fail, and said so**; that is the most useful sentence in the diff, and the only other
instance in the file is one decorative line. The escalation was withdrawn on a measurement
rather than defended, with its own wrong premise named as BF0's shape applied to an escalation.
And **condition 4 was stopped at the refusal rather than pushed through it** -- the one decision
in this step that could have republished a dozen figures in a file sent to Xabier, taken
correctly, with the bit-identity prediction admitted wrong before anyone asked for it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 3d24e1c3808cd6be35490eab76b43f5ccf9d175b
**Reviewed commit: `3d24e1c3808cd6be35490eab76b43f5ccf9d175b`.**
Verdict: HOLD
Scope: **ADDENDUM to the interim check above, same reviewer, same branch, same judged
commit, accumulating under DX2.** It exists because **CI's verification ladder concluded
AFTER I ruled** and it found a red I had not measured -- in `tests/regression`, which I
declined to run locally and gave a reason for that THIS REFUTES. Still an ES0 interim check:
it counts against none of step 0's three revisions and closes nothing. One new blocking
finding, one correction to my own Tests line, and two measurements that arrived late.

## Carried

Everything carried in the entry below stands unchanged -- R1206 open and blocking, R1213,
R1214, R1215, R1221, R1222, the ledger, and the rung-4 staleness red under CZ1 (iv).
**R1223 below is a consequence of that staleness red reaching a published deliverable**, so
it is answered by the same follow-on commit and adds no separate work. Nothing is withdrawn.

## Findings

**R1223. (BLOCKS) A PUBLISHED DELIVERABLE no longer regenerates from this tree, and the two
rows that moved are gate STATUSES: the shipped report says `G4.1 force ... pass` where this
tree produces `FAIL`.**

```
claim  CI's ladder is a pass, or its red is the staleness guard I already ruled
cmd    gh api .../actions/runs/44118920983/jobs  (after the run CONCLUDED, 16:25Z)
out    the verification ladder: CONCLUDED FAILURE
       ladder 1 success, ladder 2 success, ladder 3 success,
       ladder 6 -- it stays fixed  FAILURE,  ladder 4 SKIPPED, ladder 5 SKIPPED
cmd    gh run view --job <the ladder job> --log-failed
out    run_rung: FAIL -- tests/regression is red.
       run_rung: 477 collected, 1 failed, 0 errored, 0 skipped
       run_rung:   failure  tests.regression.test_f6_deliverable_agrees_with_itself::
                            test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
cmd    the same test, my own run, in my own worktree at the judged sha
out    1 failed in 56.14s -- "the committed deliverable is not what this tree regenerates:
       4 line(s) differ, shipped has 470 lines against 470.
         line 154: shipped `| G4.1 force | ... | F4_G41_DYNAMIC_FORCE | pass |`
                   vs fresh `| ... | F4_G41_DYNAMIC_FORCE | FAIL |`
         line 155: shipped `| G4.1 moment | ... | pass |` vs fresh `| ... | FAIL |`
         line 165: shipped `  G4.1 force       116 passed`
                   vs fresh `  G4.1 force       1 failed, 115 passed`"
cell   ONE VARIABLE -- the same test at `91c2d2e`'s code, in the worktree at `8d40843`
       (which adds only verdict 59's file to that tree)
out    1 passed in 74.74s
rule   tests/regression/test_f6_deliverable_agrees_with_itself.py:317; EZ0 -- a published
       deliverable is anything under `results/` or `scripts/measure/` that produces one
judge  **THIS COMMIT CAUSED IT.** Green at 91c2d2e, red at 3d24e1c, code the only variable.
       It is downstream of the rung-4 staleness guard -- the G4.1 gate's 116 cases include
       it, so `116 passed` became `1 failed, 115 passed` and the generator wrote `FAIL` --
       but it is a STRICTLY LARGER claim than the staleness red, and FS1's predicate does
       not reach it: it names no finding and no site of verdict 59, and its subject is a
       shipped deliverable rather than the commit carrying it. CZ1 (iv).
```

**The silently wrong result, in the form FR1 asks for:** the shipped F6 results report --
a file sent to Xabier -- states that gates `G4.1 force` and `G4.1 moment` **pass**, with
`116 passed` beside them, while the tree at this commit regenerates the same report with
`FAIL` and `1 failed, 115 passed`. A reader of the deliverable is told a dynamic-equilibrium
gate holds; the tree says it does not. That is FR1's first head verbatim -- a wrong value in
a published deliverable -- and it is invisible to `pytest tests/unit`, to the four root
guards, to `ruff`, `black` and `mypy`, and to the selection either of us ran before CI.

**And the correction, which is mine (R1224, DOES NOT BLOCK -- a reasoning error of my own,
recorded so the next round does not inherit it).** My Tests line argued that rungs 1, 2, 5,
6 and `tests/regression` could not be reached, because `git diff --stat ... -- floatfea` is
`hsp_pin.py` alone and only two test files import it. **The argument is refuted by the
measurement:** `tests/regression` reaches the changed lines INDIRECTLY, through a gated run
of the G4.1 gate inside the deliverable generator. An import census over `tests/` cannot see
a test that shells out to a generator that runs another gate. **FV1's own clause said so and
I read past it:** *"any regression test that reads a deliverable the diff regenerates"* runs
locally. This diff regenerates one. Convert arguments into measurements -- the measurement
was 56 seconds and I reasoned instead.

## Tolerances touched

**None.** Unchanged from the entry below and re-checked against this red: the four differing
lines are STATUS and COUNT cells, not thresholds -- `2.5e-12` / `F4_G41_DYNAMIC_FORCE` and
`0.0002` / `F4_G41_DYNAMIC_MOMENT` are byte-identical on both sides of the comparison, so no
tolerance moved and none is implicated. EU1 still does not arise.

## Next step opens when

The five conditions below stand, with one addition and one sharpening.

6. **R1223 -- the deliverable regenerates.** It should fall out of condition 4 (the
   provenance refresh) with no separate work, and the check is one command:
   `pytest -q tests/regression/test_f6_deliverable_agrees_with_itself.py` green at the
   follow-on commit, pasted. **If it does NOT go green once the provenance is refreshed,
   stop and say so** -- that would mean the G4.1 gate's `116 passed` is not restored by the
   refresh, which is a different and larger finding than anything in this file.
   **Do not regenerate the deliverable to match a red gate.** Re-running
   `scripts/measure/f6_results_report.py` now would write `FAIL` into the shipped report and
   turn this test green while publishing a failing gate; that is the golden-file error
   CLAUDE.md names, one artifact over.
7. **Condition 4 is sharpened: the follow-on commit's own CI run must be GREEN on the
   LADDER, not only on lint** (CZ1 (iii), (iv)). Rungs 4 and 5 were SKIPPED behind this red,
   so **nothing at this commit has measured rung 4 or rung 5 in CI at all** -- including the
   staleness guard's companions and the whole of rung 5. That is the hiding CZ1 (iii) exists
   for, and it is why a concluded, green ladder at the follow-on sha is the condition rather
   than a local run.

**Two measurements that arrived after I ruled, recorded here so the next revision does not
have to take them.** CI at the judged commit is now fully concluded: `lint, unit and guards`
FAILURE (the 108, as traced), `the verification ladder` FAILURE at `ladder 6` with rungs 4
and 5 skipped, both determinism jobs skipped by their own condition -- so **CA2 is reached
on both jobs**, and rungs 1, 2 and 3 are measured SUCCESS in CI at this sha, which is the
half of my STOP paragraph that survives. And EG3 (ii), measured at MY verdict commit
`b2dc268` on the two report-guard files: **187 failed, 120 passed, 1 skipped in 111.90s**,
up from the 107 those two files carried at `3d24e1c` -- because
`test_every_named_site_is_touched_or_declared` is parametrised over the newest verdict's
sites and this verdict names many more. That is R835 in one line, not re-measured further
(GE3). Paste that count in the next revision; the number to compare against is 187.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 3d24e1c3808cd6be35490eab76b43f5ccf9d175b
**Reviewed commit: `3d24e1c3808cd6be35490eab76b43f5ccf9d175b`.**
Verdict: HOLD
Scope: **ES0 INTERIM CHECK on the OPEN step** -- no new report revision exists
(`git ls-files docs/reports/R2` is empty; `docs/reports/R2/step-0.md` is untracked), so this
**counts against none of step 0's three revisions** and closes nothing, and `--closes` is
correctly absent (FK1). Light scope per ES0: the suite, CI at the commit, and a CZ0 (a)-(d)
scan of the diff. **Ruled under FR1 with EZ0**, and each blocking finding names the silently
wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.**
**EU1 DOES NOT ARISE, MEASURED RATHER THAN TAKEN:** `git diff adc6c3c..3d24e1c --
floatfea/tolerances.py` is empty, so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`,
and no declared counter moves anywhere in the diff. **I took the diff from `91c2d2e`, the last
JUDGED commit, not from `adc6c3c`**, so `8c0edce` is inside it and is judged below.
**GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the
overrun is the per-id trace of 108 reds with its one-variable control (EG3 (i) forbids ruling
a cascade by family), two blocking findings with their cells, and the four rulings you asked
for by name.
Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`, and the first
reproduces your figure exactly rather than taking it.**
* your stated selection -- `tests/unit` + the four root guards +
  `rung3/test_platform_deck_export.py` + `rung4/test_f4_g41_dynamic.py`:
  **1 failed, 828 passed in 365.65s**, and the one failure is the staleness guard.
* the six report-guard files: **108 failed, 557 passed, 1 skipped in 442.68s**, traced per
  id below. Your selection excludes all six, so your report's "1 failed" is true of what it
  ran and silent about the file where the marker decision lands.
* CI's own guards selection, `pytest tests --ignore=tests/unit --ignore=tests/verification
  --ignore=tests/regression`, in a second worktree: **108 failed, 1047 passed, 1 skipped in
  903.77s -- THE SAME 108, id for id.** `comm -23` and `comm -13` over the two sorted FAILED
  lists are BOTH EMPTY, so **no root test outside the six report-guard files is red at this
  commit** and nothing is hiding inside CI's aggregate.
* the one-variable control (marker back on R1 step 4, this commit's code unchanged):
  **8 failed, 849 passed in 607.41s** -- see the trace.
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`,
  `mypy floatfea`: **all clean, my own runs.**
* **NOT RUN LOCALLY and I say which rather than implying coverage**: rungs 1, 2, 5, 6 and
  `tests/regression`. The reason is measured, not assumed:
  `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` alone, and
  `git grep -ln hsp_pin -- tests` outside the corpus returns only
  `rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py`, so no test in
  those rungs reaches a changed line. FV1 puts the whole of `tests/regression` on CI.
CI: **run `44118920983` at the FULL sha `3d24e1c3808cd6be35490eab76b43f5ccf9d175b` EXISTS
and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with
`actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all **success** before it --
so the guards step is seen to have RUN rather than been skipped behind an earlier red
(CZ1 iii). **`the verification ladder` had NOT finished when I ruled** (`in_progress`, both
runners assigned, started 15:50:31Z); a run that has not finished is not a pass. Expect it
to redden at `ladder 4` on the same staleness guard -- and note CI orders `ladder 6 --
tests/regression` BEFORE `ladder 4`, so that rung is not hidden behind it. Both determinism
jobs `skipped` by their own `workflow_dispatch` condition. **This is NOT CK2**: runners
`GitHub Actions 1000001916` and `1000001917` were assigned and the jobs executed for
minutes. **CA2 IS REACHED -- CI is red at the judged commit** -- and the per-id list is
**unavailable, not skipped over**: `gh run view --log` refuses while any job is in progress
(*"logs will be available when it is complete"*), so the id-for-id agreement between my 108
and CI's list is deferred to the next revision. FP1 held: the commit was pushed before I was
invoked. GC2 does not arise -- `git diff --name-only 91c2d2e..HEAD` touches `floatfea/` and
`scripts/`, so the push triggered a run of its own. **One throughput observation, not a
finding:** the runs at `91c2d2e` and `8c0edce` are STILL `in_progress` after 1h18 and 1h00,
their ladders unfinished, because GG3's per-commit group no longer cancels them -- three
ladders now run in parallel and CI's answer arrives long after the commit.
Door (FV2 / GG2): `git worktree add -b review/3d24e1c3808c <a path outside the repository>
3d24e1c3808cd6be35490eab76b43f5ccf9d175b` **succeeded on the first try, so no review of this
commit existed**; `git push origin review/3d24e1c3808c` likewise. Every measurement above was
taken in that worktree, and this verdict is written there through `scripts/write_verdict.py`,
committed on that branch and pushed -- merge it with `git merge --ff-only
origin/review/3d24e1c3808c`. **Three writes of my own, all in my own worktree and all
reverted before committing** -- the marker-1 cell, the marker control, and a second DETACHED
worktree for CI's wide selection, which I removed with `rm -rf` followed by `git worktree
prune` -- the one `.git`-metadata write I made in `C:\dev\floatfea`, which touches no file
in the working tree and which I disclose rather than leave for you to find. `git status --porcelain` there is empty
and both marker lines read as committed. In `C:\dev\floatfea` I ran only read-only `git` and
`gh`, and the one write-shaped thing I did touch -- `preflight()` against the real
`HSP-stable` -- reads only (`git describe`, `git hash-object` without `-w`) and wrote nothing.

## Carried

Verdict 59's four blocking findings, its four closing conditions, and verdict 58's items
routed to R2's first report. **Three of four answered; two halves open.**

* **R1205 (two live markers; the `Carried` gate reporting on F2 step 4) -- ANSWERED, and I
  re-ran both checks the condition asked for rather than reading them.**
  `docs/milestones/R1.md:3` now reads `<!-- step-under-execution: moved to R2 at step 0
  (GI) -->`, the `F2.md:10` form.
  ```
  cmd  grep -rnE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
  out  docs/milestones/R2.md:3   (one plan, not two)
  cmd  python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
  out  ('R2', 0)
  cmd  python scripts/check_carried.py ; echo exit=$?
  out  check_carried: .../docs/reviews/R2/step-0.md or .../docs/reports/R2/step-0.md missing
       exit=1
  cmd  python -c "import sys; sys.path.insert(0,'.'); import scripts.ci_section as c; print(c.MILESTONE, c.STEP)"
  out  R2 0
  ```
  The gate that was green about the wrong milestone is now red about the right one, naming
  the file the next revision adds. That is the repair.

* **R1206 (`0` is both a legal step number and the resolvers' sentinel) -- STILL OPEN,
  still blocking, and it carries by name into step 0's list.** You do not claim it
  answered; what shipped is verdict 59's **cell 2**, not exit (ii) -- see R1215 and
  ruling (1), where I withdraw the escalation by measurement.

* **R1207 (step 2's gates (ii) and (iii) both passable by a no-op) -- ANSWERED in the
  plan, at `docs/milestones/R2.md:317-332`.** (ii) is now a pair with the inverted half
  stated as the gate ("a run at a PERTURBED mass does *not* [reproduce], differing in
  `case<i>/body_mass`, `m_xddot` and `accel`"), and (iii) closes against
  `case<i>/body_mass` read back from the npz. Both citations resolve in substance; one
  line number is off by three (R1217).

* **R1208 (one key is silent in one direction) -- HALF ANSWERED. The two keys are
  written and routed correctly; the half that says "the three DS0 refusals shown firing
  after the change" FAILS BY MEASUREMENT.** The routing I checked site by site, as you
  asked:
  ```
  cmd  git grep -n "hsp_pin.worktree(" -- scripts
  out  export_buoy_centers_ref.py:42   "stable"     <- correct, the no-refusal site
       export_platform_deck.py:45      "runs"
       measure_platform_joints.py:52   "runs"
       report_joint_reactions.py:96    "runs"
       run_floatsim_design_waves.py:55 "runs"   :56 "stable"   <- both, correct
  cmd  for each touched script: import it with NO worktree present and NO env var set
  out  OK export_buoy_centers_ref / export_platform_deck / measure_platform_joints /
       report_joint_reactions / run_floatsim_design_waves / f4_dynamic_residual /
       export_f4_dynamic_inputs      (7 of 7 -- `require=False` does what its docstring
       claims and R670's import-time ImportError is avoided, measured not argued)
  ```
  The refusals are **R1213**: two of the three fire on the adversarial input, one does not.

* **Verdict 59's ledger -- R1209, R1210, R1211, the Â§4 row-1 form, the CP3 header, the
  triple grammar, and Â§5's DO-NOT-HAND-EDIT line: all SIX addressed in the plan diff.**
  I read each against its site. R1209's census is rewritten with a needle that finds all
  seven (`git grep -nE '(ROOT|parents?\[[0-9]\])...'`) and now splits runs from stable;
  R1210's false `out` line is replaced by what the command returns, with the consequence
  for D4 stated; R1211 gains the one-body/three-component limit and the GI1 declared-file
  distinction; Â§5 gains the deck bullet; the CP3 header names its two carried figures; the
  triple-grammar paragraph is accurate -- `grep -c "^cmd:" docs/milestones/R2.md` is `0`
  and the file says so rather than pretending otherwise. **The Â§4 row-1 form is half
  right and I re-open that half as a ledger item (R1218).**

* **R1212 -- unchanged, mine, Xabier's.** The verdict is at `step-0.md` and not `plan.md`
  for the reason recorded there; this entry accumulates into the same file under DX2.

* **Verdict 58's items -- R1196 to R1201, R1186, R1188, R1189 (c), R1190, R1191, R1193 --
  STILL OPEN, due in R2's first report**, which is in flight. None is answerable by this
  commit and none is a plan matter. **R1193 stays discharged from my side** (I am
  operating under the post-`2e08766` text). **R1203, R1204 -- reviewer-side or Xabier's.**

* **Verdict 59's four "things for step 0's report" -- not yet due**, and three of the four
  are the report that is in flight. The `--check` determinism run is ruling (4) below,
  where I correct what it can and cannot clear.

## The 108, per id, at this commit -- traced from each id's own message (EG3 (i))

```
cmd    python -m pytest -q -p no:randomly <the six report-guard files>, my own run in my
       own worktree at the judged sha
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    grep "^FAILED" | strip the parameter | sort | uniq -c
out    50  test_every_named_site_is_touched_or_declared[...]
       21  test_the_report_carries_the_finding[...]
       19  test_the_guard_survives_the_state[...]
       18  singletons in test_report_carried / test_report_guard_states /
             test_report_numbers_are_sourced
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST verdict
       (verdict 59, `adc6c3c`, whose entry is in this same file). Limb two: its SUBJECT is
       the commit carrying it.
```

**The 50 and the 21 are parametrised over verdict 59's OWN findings and sites**, so limb one
holds by construction, and their messages say what clears them: *"...the step's diff does not
touch it, and the newest report revision does not say..."* and *"the report does not carry
..."*. EG3 state (2), cleared by the answering report. **Three of the 50 are worth naming
rather than waiving silently, because their content IS R1213:**
`[R1208-run_floatsim_design_waves.py:98]`, `[R1208-report_joint_reactions.py:106]` and
`[R1208-export_platform_deck.py:75]` -- the three DS0 refusals -- are red because *the diff
does not touch them*. The guard is enforcing CLAUDE.md's *a closing condition that names
sites is closed site by site*, mechanically, and it is right: two of the three needed no
change and one did.

**The 19 share ONE cause with the singleton `test_R887_...`, and the harness names it
itself** rather than being ruled by class: R887 reports *"the harness copies FROM step-0.md,
which does not exist. Every state built by a `copy2` dies in `_build` before planting
anything."* State (2). Two of the 19 additionally report `<state>: expected a clean run`,
which is the same absence seen from inside the inner run.

**The 18 singletons, each read individually. SIXTEEN are state (2) in their own words** --
*"the newest report revision has no `Answers:` header"*, *"...no Carried section"*, *"...no
`## ... CI ...` section"*, *"the CI section names no commit"*, *"no step report found
under docs/reports/R2"*, *"step-0-answers.json is not committed ... That is EG3 state (2)"*.
That sixteen includes the two names FC1 put under limb two,
`test_the_report_carries_a_WHOLE_SUITE_count` and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -- **and limb two is not needed for either
here**, because at this commit they fail on report absence like the rest (*"the newest
revision carries no whole-suite line"*, *"the 0a table has neither a run row nor the
generator's zero-run row"*). Measured, not assumed from the name. **And two are neither,
and they are the two that matter:**

* **`test_the_plan_names_the_step_under_execution` is R1206 ITSELF.** The marker count is
  now 1, so the first assertion passes; it dies at `assert _plan_step() > 0`. It is not a
  boundary red and it needs no waiver -- it is the true, loud symptom of an open blocking
  finding carried from verdict 59, and it clears when exit (iii) is taken and not when a
  report is written.

* **`test_a_blocking_item_is_not_routed_to_4a` IS MINE, AND NO REPORT CAN CLEAR IT --
  R1222 under Findings.** It is red on verdict 59's heading FORMAT, not on anything the
  implementer did or can do.

**So: of 108, ONE HUNDRED AND SIX are EG3 state (2) and the waiver covers them --
50 + 21 + 19 + 16, which sums exactly; ONE is R1206, already blocking and already carried;
ONE is mine (R1222). The 109th red, `test_the_npz_is_NOT_STALE...` in the separate rung-4
run, fails the predicate and is CZ1 (iv) unchanged.**

**THE CONTROL, ONE VARIABLE, AND IT IS THE MEASUREMENT THAT SETTLES OWNERSHIP OF ALL 108.**
A list of names cannot be checked against a failure message and a family cannot be ruled as a
cascade (EG3 (i)), so I moved the marker back to `8c0edce`'s state **with this commit's CODE
DIFF LEFT IN PLACE** -- R1 at step 4, R2's retired -- and re-ran the identical selection in my
own worktree, then reverted (`git status --porcelain` empty, both marker lines back):

```
cmd    the judged tree (R1 retired, R2 at step 0), six report-guard files
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    ONE VARIABLE MOVED -- the marker back on R1 step 4, R2's retired, same code
out      8 failed, 849 passed in 607.41s
cmd    the eight, by name
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       test_the_guard_survives_the_state[baseline, non_numeric_step_suffix,
         superscript_digit_step_number, draft_suffix_beside_a_step_report,
         step_number_is_the_empty_string,
         verdict_amended_after_the_commit_the_report_answers, zero_padded_step_number]
rule   FS1/FT1 per id, and `8c0edce`'s own trace of the same eight
judge  **THE EIGHT ARE EXACTLY THE SET `8c0edce` TRACED BY NAME, id for id**, including the
       one it showed red at `251af69` before this turn began. So **not one of the 108 is
       caused by the code in this commit** -- the hundred extra are a function of the
       marker/no-report state alone, and the collection total moves with it (666 vs 857)
       because both guards are parametrised over the active report's verdict (R861).
```

That is the control R1 step 1's report got wrong by comparing two instances of the SAME state:
here the two cells differ in one variable and the code is held fixed, so it separates "red
because no report exists" from "red because of this diff". The answer is all of the first.

## Findings

**R1213. (BLOCKS) The DS0 refusal in `run_floatsim_design_waves.py` DOES NOT FIRE on the
input this diff newly admits, and I ran it against the real production worktree rather than
reasoning about it.**

```
claim  verdict 59's condition 4 -- "the three DS0 refusals shown still firing" -- holds
       after the change
cmd    FLOATFEA_HSP_RUNS=C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable, the stable key
       UNSET and its legacy sibling absent (the state measured at C:\dev\floatfea);
       import scripts/run_floatsim_design_waves and call preflight() -- preflight only,
       nothing written
out    RUNS   = C:\Users\xlama\OneDrive\Documents\buoy\HSP-stable
       STABLE = ...\scratchpad\HSP-stable            (the legacy candidate, absent)
       worktree  HSP-stable at floatfea-ref-1
       database  blob f26501001916, sha256 3dca8b131b4a028b -- matches the commit
       output    ...\HSP-stable\studies\platform-12buoy\floatfea_design_waves
       >>> preflight() RETURNED. DS0 did not fire.
cmd    the same input, through the OTHER two refusals' predicate
out    "HSP-stable" in RUNS.resolve().parts  ->  True     (they DO fire)
       RUNS.resolve() == STABLE.resolve()    ->  False    (this one does not)
rule   scripts/run_floatsim_design_waves.py:102 -- the refusal is an IDENTITY test against
       the other key, not a NAME test. report_joint_reactions.py:109 and
       export_platform_deck.py:77 test the name and are unaffected.
cell   one variable: at `91c2d2e`, `RUNS = Path(__file__).resolve().parents[2] /
       "HSP-runs"` reads no config and no environment, so no input could reach this state.
       The diff is what makes it reachable; the refusal is what was supposed to hold it.
```

**The silently wrong result.** `main()` calls `preflight()` and then, at
`run_floatsim_design_waves.py:138`, `OUT.mkdir(parents=True, exist_ok=True)` and writes six
`case_*.csv` solve-state windows **inside the tree `RUNS` names** -- so six FloatSim
design-wave solves run and write into `HSP-stable`, the read-only production worktree GI1,
`R2.md:366` and `docs/hsp-coupling.md:121` (*"`HSP-stable` is read-only from FloatFEA
(DS0)"*) forbid writing to, with the one refusal that exists to prevent exactly that
printing nothing. The module's own docstring records the precedent: *"this repository wrote
into it once: a `platform_bem.py` run regenerated `platform12_bem.nc` and overwrote the
version commit `e1010fe` had corrected, after which FloatSim's own restoring-PSD gate
refused the database."* And the export is read back by `report_joint_reactions.py:121`
(`EXPORT.glob("case_*.csv")`) through **its own** runs key, so a case set written into one
tree is described from the other -- the September case set is still sitting in `HSP-runs`.
That is FR1's second head: an input accepted and used other than as declared, with DS0's
declaration silent.

*Closed when* `preflight()` refuses on the measured input -- the one-line name test the
other two sites already carry, kept **beside** the identity test rather than replacing it
(EK2: repair, not a new mechanism) -- and the run above is pasted showing the refusal, which
is also what `R2.md:253` and `:291` promise and what verdict 59's condition 4 asked for.

**R1214. (BLOCKS) A key that is SET BUT WRONG is silently discarded and a different
worktree is used.**

```
claim  what happens to a declared value that is not a directory
cmd    FLOATFEA_HSP_STABLE=C:/typo/HSP-stable-oops (set, not a directory), with a legacy
       sibling of the repo root that EXISTS; then hsp_pin.worktree("stable")
out    legacy sibling exists?  True
       worktree('stable') -> ...\scratchpad\HSP-stable
       the declared value was DISCARDED with no message and no refusal
cmd    the same shape through `declared`, which is the config half GI3(e) asks for
out    declared=<nonexistent>, env set to another existing tree -> the ENV tree is
       returned; the declared value is discarded silently
rule   floatfea/hsp_pin.py:90-101 -- the loop appends `f"{source}: {path} is not a
       directory"` to `tried` and then CONTINUES. `tried` is read only under
       `require=True`, which NO caller passes (`git grep -n "require=" -- scripts` is
       empty), so the distinction between NOT SET and SET-AND-WRONG is computed and
       thrown away.
```

**The silently wrong result.** `data/platform/buoy_centers_ref.json` -- a committed data
file and the input to EB6's label-provenance gate -- regenerated from a worktree nobody
declared, with its `"source"` field naming `HSP-stable/...` and `_blob_sha` recording that
other tree's sha, so both sides move together and `--check` stays green. That is C155's
shape and it is the **same defect R1208 was**, surviving one level up inside the resolver
written to fix it: `export_buoy_centers_ref.py` is the one site with no tag, name, commit or
dirtiness refusal -- I checked, its only `SystemExit` on the tree is "the source file is not
a file" (`:74-76`) -- which is precisely why you gave it the stable key. A typo'd or stale
`FLOATFEA_HSP_STABLE` on a checkout that satisfies the legacy convention reaches it today,
and that convention is the DOCUMENTED one: `docs/hsp-coupling.md:45` and `:141-142`
prescribe `git worktree add ../HSP-stable` and `../HSP-runs` as the scheme, so a conforming
checkout HAS the sibling this falls through to.

*Closed when* a source that is **set and not a directory** is a refusal and only an **unset**
source falls through -- the information is already in `tried`, so this is a two-line change
in `hsp_pin.worktree` and no new apparatus. CLAUDE.md's own line is the rule here: *never
let a validation failure degrade to a warning*; this one degrades to silence. FZ rule 2 says
refuse rather than silently adjust.

**R1215. (DOES NOT BLOCK -- FF0, next commit, not the ledger) `docs/milestones/R2.md:5`
says the marker reads `1` while `:3` reads `0`, and calls the shipped state "exit (ii)",
which it is not.** No wrong number follows, so FR1 does not block it; FF0 keeps it out of
the ledger because it is the gating apparatus's own record.

```
cmd    sed -n '3p;5p' docs/milestones/R2.md
out    3: <!-- step-under-execution: 0 -->
       5: <!-- IT READS 1 WHILE STEP 0 IS BEING WORKED, AND THAT IS R1206'S EXIT (ii)
          CHOSEN DELIBERATELY ...
cmd    the same comment, 29 lines down
out    "SO THE MARKER READS 0 AND NOT 1"
rule   verdict 59's exit (ii) is "keep the marker at the NEXT step and record step 0
       another way". The marker is at the CURRENT step, so what shipped is the judged
       tree's cell 2 -- no exit taken. You say R1206 is open, which is right; the plan
       file says the opposite twice.
```

This is BP0 on the smallest possible scale: the first sentence was written for the marker-1
attempt and the decision moved underneath it. It is in the file four resolvers read, beside
the value they read, and it says the opposite of the value. One paragraph, next commit.

**THE RED. I REACH YOUR CONCLUSION AND NOT YOUR REASONING, AND THE REASONING MATTERS
BECAUSE IT IS FS1's FIRST LIVE FAILURE IN THE OTHER DIRECTION.**

`tests/verification/rung4/test_f4_g41_dynamic.py::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it`
is **CZ1 (iv), unwaived**. You wrote that it "names no finding or site of verdict 59". It
names three:

```
cmd    the assertion message, from my own run
out    floatfea/hsp_pin.py: tree 1d18d35e24c7 vs provenance d2e055b9fdc0;
       scripts/export_f4_dynamic_inputs.py: tree e5b4b012a56a vs provenance 3127f6ffe524;
       scripts/report_joint_reactions.py: tree 7166c5ef0a5f vs provenance 006af3e1d622
rule   FS1 limb one -- "names a finding or a site of the newest verdict". All three files
       are sites of verdict 59 (R1208 names `hsp_pin.py:20` and
       `report_joint_reactions.py:96`; R1207 names `export_f4_dynamic_inputs.py:467-479`
       and `:390`), and `test_every_named_site_is_touched_or_declared` is parametrised
       over two of them BY NAME in this very run.
judge  **LIMB ONE IS SATISFIED IN LETTER AND FAILS IN SUBSTANCE, so the red blocks.**
       Both limbs are REASONS, not names (FS1), and the reason behind limb one is EG3's
       two states -- *designed, and SELF-CLEARING*. This red does not clear when the
       answering report is written, and it did not exist because a verdict exists: it
       exists because committed data went stale against committed code. Limb two is not
       reached either -- its subject is the npz, not this commit. CZ1 (iv) stands.
```

That is worth one sentence of record and no more (GE3: `R835: unchanged, R2`): the predicate
has now been short in **both** directions in one tree -- too narrow for the no-report reds
below, too wide for this one -- and in both cases what settled it was the failure message,
not the name.

**And your stated answer does not clear it, which is the part that would have cost a
commit.** `--check` measures the right thing and cannot discharge the guard:

```
claim  `scripts/export_f4_dynamic_inputs.py --check` clears the staleness red
cmd    read the --check path: scripts/export_f4_dynamic_inputs.py:435, :444-:504
out    `--check` writes `dynamic_inputs.check.npz`, compares arrays with
       `np.array_equal`, unlinks, and `return`s -- it never reaches
       `PROVENANCE.write_text` at :540. The guard compares the provenance's
       `import_closure` blob shas against the tree's, so only a provenance REWRITE
       clears it.
cmd    whether a full regeneration churns the 12 MiB npz as well -- measured, because I
       assumed it would and I was wrong
out    np.savez_compressed of identical arrays, twice, two seconds apart:
       file bytes identical? True   (arrays equal? True)
rule   the guard at tests/verification/rung4/test_f4_g41_dynamic.py:321
judge  so the sequence that clears it is `--check` FIRST (your determinism and GI3(b)
       wall-time measurement, and if it differs, that is R2.md Â§6 item 2's escalation and
       the provenance must NOT be refreshed), then a full WRITE run, whose git diff should
       be the provenance json alone. If `dynamic_inputs.npz` moves in that diff, the
       arrays moved and Â§6 item 2 is live.
```

**R1221. (DOES NOT BLOCK -- FF0, next commit) The `Carried` gate is parametrised over
PHANTOM finding ids -- `R2`, and `R1` too -- and no wording on my side can avoid them.**
FR1 does not block it; FF0 keeps it out of the ledger, because this is the gate R1205
exists to protect.
```
claim  the ids `test_the_report_carries_the_finding` demands of the step-0 report are
       findings
cmd    tests/test_report_carried.py:387-390 -- EXPECTED = _FINDING.findall(VERDICT_TEXT)
       | _MENTION.findall(_section(VERDICT_TEXT, "Carried")); _MENTION is
       re.compile(r"\bR\d+\b") at :238
out    the parametrised ids at this commit include [R2] and [R835] beside [R1205..R1208]
       and verdict 58's R1186..R1204
cmd    where `R2` comes from -- the Carried section of verdict 59, six times
out    "routed to **R2's first report**", "due in R2's first report", "routed to R2",
       "R835 is R2's under GE3", "It asks R2's first report", "docs/milestones/R2.md:12"
cmd    whether a reviewer can write a Carried section without it
out    grep -o "\bR2\b" <this verdict's Carried section> | wc -l  ->  10, and
       grep -o "\bR1\b" -> 1, so THIS entry injects TWO phantoms. All eleven are either
       the milestone label or a path -- `docs/milestones/R2.md`, `('R2', 0)` and
       `docs/milestones/R1.md:3`, which is R1205's OWN site and therefore mandatory in a
       Carried section that answers it.
rule   `\bR\d+\b` cannot distinguish a finding id from a milestone label in a repository
       whose milestones are `R1` and `R2`. In the F-era it could not fire -- `F6` is not
       `R\d+` -- so this is FF0's `F*.md` glob defect one needle over.
judge  the guard then requires the report to "carry R2" as a Carried row, which it will
       satisfy BY ACCIDENT, since every report mentions its own milestone. A gate that
       goes green for the wrong reason on the one gate CLAUDE.md says the whole
       arrangement exists for. EK2: fixed, not extended -- the `_MENTION` needle needs to
       exclude the active milestone's own label, or `EXPECTED` needs to take ids only
       from `_FINDING`-shaped lines.
```

**R1222. (DOES NOT BLOCK -- MINE, and no report can clear it)
`test_a_blocking_item_is_not_routed_to_4a` is red because verdict 59 wrote its dispositions
as PROSE and the gate parses them from PARENTHESES.**

```
cmd    the id's own message, from my run
out    "no `**R<n>. (<disposition>)` heading parsed from step-0.md at all. The heading
        format changed and this check passes on anything."
rule   tests/test_report_carried.py:423-428 -- `_findings()` matches
       r"^(?:\*\*|#{2,4}\s+)(R\d+)\.?\s*\(([^)]*)\)", so the disposition must sit in
       parentheses immediately after the id. Verdict 59 wrote `**R1205. TWO plans carry a
       live ... BLOCKS.**` -- the disposition is in the prose -- so `_findings()` is EMPTY
       and the guard's own non-vacuity check fires.
judge  **the answering report cannot fix a verdict's heading format**, so this red is
       neither state (2) nor limb two; it is the R861 shape, a guard parametrised over what
       the reviewer itself wrote. Every finding in THIS entry uses the parenthesised form.
       **Prediction, recorded before the measurement (EG3 (ii) measures state (1) at the
       verdict commit): this id is GREEN at my verdict commit.** Paste that run in the next
       revision; if it is still red, the parser wants something else and that is a finding
       against the guard, not against the verdict.
```

## The four rulings you asked for

**(1) THE ESCALATION IS WITHDRAWN -- NOT BECAUSE EK2 AND FF0 AUTHORISE A HOOK CHANGE, BUT
BECAUSE NO HOOK CHANGE IS NEEDED. R1206's exit (iii) is three lines in `tests/`.** You
asked me to rule on whether EK2 plus FF0 authorise the `.claude/hooks/` edit without a
directive. They do not, and CLAUDE.md is unambiguous: `.claude/hooks/` changes only in a
standalone `process:` commit citing the directive asking for it, and mixed into a commit
touching `floatfea/` or `tests/` it is a **STOP-class finding**. You were right to refuse
that door. **But the premise -- "one of its six sites is
`.claude/hooks/require-verdict.sh:81,110`" -- is wrong, and I measured it rather than
reading the two line numbers you named:**

```
claim  the hook needs the sentinel separated from the value
cmd    sed -n '81p;110p;134p' .claude/hooks/require-verdict.sh
out    81   marker_re='<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->'
       110  step=$(grep -oE "$marker_re" "$plans" | head -1 | grep -oE '[0-9]+')
       134  if [ -z "$step" ]; then        <- THE HOOK'S SENTINEL IS THE EMPTY STRING
cmd    grep -n '"0"\|-eq 0\|step -gt\|step == 0' .claude/hooks/require-verdict.sh
out    (no match)
cmd    where the collision actually is
out    tests/test_report_carried.py:100   return None, 0
       tests/test_report_carried.py:111   return None, 0
       tests/test_report_carried.py:617   assert _plan_step() > 0
rule   `0` is READABLE at :110 and distinct from unreadable at :134, so the hook resolves
       `report=docs/reports/R2/step-0.md` correctly at marker 0. `check_carried` falls back
       to `("F2", 4)` and `ci_section` to `F2.md` -- neither uses `0` as a sentinel, and I
       ran both at marker 0 above: `('R2', 0)` and `R2 0`.
judge  **exit (iii) is: give `_active_plan` a sentinel that is not `0` (`-1` or `None`), and
       make :617 assert on THAT rather than on `> 0`.** One file, in `tests/`, where EK2's
       "a guard that fails false is fixed, not extended" applies directly and no directive
       is required. Take it; it is cheaper than the state you shipped and it ends the red.
```

**And one correction to the discriminator you chose it on.** Your third measurement --
"at marker 1, `ci_section.py` raises `FileNotFoundError` on `docs/reports/R2/step-1.md`" --
is true, and it is **not a discriminator at this commit**, because marker 0 raises the same
error one filename over:

```
cmd    marker 0, as judged, in a worktree at the commit:  python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-0.md
cmd    marker 1 (one variable moved, reverted after):     python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-1.md
cmd    and at marker 1 the IMPORT you cited succeeds
out    imported, MILESTONE= R2 STEP= 1
judge  the difference appears only once `docs/reports/R2/step-0.md` EXISTS, which at this
       commit it does not -- it is untracked. The right reason for 0 over 1 is simpler and
       does not need the generator: step 0 is the step being worked, so 0 is the only value
       that makes every resolver name the file the next revision adds. Marker 1 would point
       them at a report that will never be written during step 0.
```

**(2) The FS1/FT1 predicate on the staleness red: I reach your conclusion, by the other
route.** See THE RED under Findings. It blocks; CZ1 (iv) stands; `--check` alone will not
clear it.

**(3) The cherry-pick of verdict 59: ACCEPTABLE HERE, AND I VERIFIED THE BYTES MYSELF
RATHER THAN TAKING THEM. The procedure item is not the cherry-pick.**

```
cmd    git rev-parse review/91c2d2e05c7b ; git diff review/91c2d2e05c7b adc6c3c -- docs/reviews/R2/step-0.md
out    8d40843a353ad580f1faba5c9babeadcc61c5b6b
       (empty)
cmd    git show --stat adc6c3c
out    docs/reviews/R2/step-0.md | 246 +++++  -- one file, 246 insertions, nothing else
rule   CLAUDE.md's escalation head is "a write to `docs/reviews/` outside
       `write_verdict.py`". The content was written by `write_verdict.py` on my branch and
       is byte-identical here, so nothing was written to that tree by any other hand.
       SUPERVISOR.md's `--ff-only` exists so that the move "cannot alter a byte"; that
       property held, and it held as a MEASUREMENT instead of as a structural guarantee.
```

So: not an escalation, and the verdict commit is clean and separate from the code it judges,
which is what step gating actually requires. **What I would record for Xabier is the cause
you named, not the cherry-pick**: the `--ff-only` door presumes the branch does not move
while a review is in flight, and once `8c0edce` landed on `F3` a linear-history merge of my
branch was impossible -- rebase-then-ff and cherry-pick are the same operation. The rule
that would have prevented it is "do not commit to the reviewed branch between invoking the
reviewer and merging the verdict", and that is not written anywhere. One line for Xabier; I
am not asking for a round on it.

**(4) `8c0edce`, which you flagged as unjudged: JUDGED, AND IT IS SOUND -- but note that
this commit reverses it.** Its diff is one file, `docs/milestones/R2.md`, retiring R2's
marker; its three-row control (`19 failed` / `54 failed` / `8 failed`, one variable each)
is the right shape and its EG3 (i) trace of the remaining eight runs each id individually
with a counted inner site, which is the discipline the eighty-third verdict asked for. **Two
observations rather than findings.** First, `3d24e1c` puts the live marker back on R2 at
step 0 and retires R1's -- i.e. it ships the middle row of `8c0edce`'s own control, the one
that commit measured at `54 failed, 103 passed` and rejected. My measurement of that state
now is **108 failed**, higher because verdict 59 exists and two guards are parametrised over
its findings and sites. That is not a contradiction -- the marker had to move for R1205 --
but `8c0edce`'s comment, which said "R1's marker stays live until R2 has a report to gate",
is the sentence `3d24e1c` overrode without withdrawing (it is gone from the file, so this is
an observation and not R1215). Second, `8c0edce`'s eighth red,
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, is in my 108 as well and its exit is now
the ordinary one: it is FT1 limb two, and FP1's push is what clears it.

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1216 -- Â§2c's census and Â§3's step-0 gate describe the PRE-change tree, in the commit
  that changed it (CP3/BP0).** Â§2 is headed *"What exists today, measured"* and Â§2c's `out`
  block lists all seven assignments in their old form with `-> MISSING`
  (`export_platform_deck.py:45 ROOT.parent/"HSP-runs"`), while the same commit rewrote :45
  to `hsp_pin.worktree("runs")`. The paste is void the moment an edit follows it. And Â§3's
  gate routes **"`export_buoy_centers_ref.py` and `hsp_pin` on `worktree_stable`"** while
  the commit DELETED `hsp_pin`'s own assignment rather than routing it -- so the shipped
  state is **six assignments in five files**, not the seven in six the gate names.
  `git grep -n "hsp_pin.worktree(" -- scripts` returns six lines; `git grep -n HSP_WORKTREE`
  returns no code site anywhere.
* **R1217 -- two citations land three lines short.** `export_f4_dynamic_inputs.py:390` is
  `"joint_body_b"`; `body_mass` is `:393` -- the substantive claim ("taken from the deck the
  solve used", `float(body[n].mass)`) is correct. `report_joint_reactions.py:106` is the
  `is_dir` check; the DS0 name refusal is `:109-110`. The second is inherited from verdict
  59's own text, so it is mine as much as yours.
* **R1218 -- Â§4 row 1's FORM is half right, and the justification is attached to the wrong
  quantity.** Trim in absolute radians is sound (an angle is already dimensionless). Draft
  in absolute **metres** is the form my own standing rule calls a defect -- it either fails
  the unit-scaling test or passes it vacuously -- and the reason given, *"a relative
  tolerance on a draft that passes through zero trim is unbounded"*, is trim's reason
  wearing draft's label: draft does not pass through zero. Verdict 59 named the response
  scale it should be relative to (the BEM reference draft, or the buoy radius). Nothing is
  compared yet, so no number can be wrong today; it becomes CZ0 (b) the moment step 2
  writes the entry.
* **R1219 -- a RELATIVE value in either key makes the resolution CWD-dependent, which is
  the defect GI3(e) exists to remove.** Measured, one variable (the cwd):
  `FLOATFEA_HSP_RUNS=HSP-runs` gives `...\scratchpad\fake\HSP-runs` from one directory and
  `...\scratchpad\HSP-runs` from another. `is_dir()` is tested before `resolve()`, so which
  tree is found depends on where the script was invoked. One line: resolve a relative value
  against `_repo_root()`, or refuse it.
* **R1220 -- NOTHING EXERCISES `hsp_pin.worktree`, and that is how R1213 and R1214 stayed
  invisible.** `git diff --stat 91c2d2e..HEAD -- tests` is empty while the commit adds ~95
  lines to `floatfea/`; `git grep -n "hsp_pin.worktree\|worktree(\"" -- tests` returns
  nothing. Both blocking findings above are one assertion each in a test that does not
  exist, and the DS0 refusal has never been run with the property it claims broken. *A gate
  carries its own failure* -- the repair of R1213 is the place to put it, not new apparatus.
* **The `declared` parameter is a config key no config declares.** The docstring calls it
  "a config key, `floatsim.worktree_runs` / `floatsim.worktree_stable`"; those names exist
  only in `R2.md:249-250` and in that docstring, no caller passes `declared`, and no schema
  mentions them. True of a half-built mechanism and fine as such -- it is named here so the
  revision that wires it closes R1214 in the same breath (CW0: prose in the source tree
  does not claim things about the code).

## Tolerances touched

**None, measured twice.** `git diff adc6c3c..3d24e1c -- floatfea/tolerances.py` is empty and
so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`. No declared counter moves: the
only tolerance-shaped values in the diff are `R2.md` Â§4's five FUTURE declarations, three of
which are to be written and two of which are correctly classified as not-tolerances -- I
re-checked both classifications and both still hold, and the iteration cap's "nothing
mechanical will hold it" note is true (`tests/test_no_tolerance_literals.py:39`: *"integers
are counts and are never flagged"*). **EU1 therefore does not arise**, and I still ran the
model at configurations the diff did not choose -- which is where R1213, R1214 and R1219
came from.

## Corpus

**No batch, and ES0 is why, not GC3.** An interim check is light by rule: *"No corpus batch,
no closure list."* My own instructions say "add unseen entries at every review"; where the
two differ, CLAUDE.md governs and I am saying so rather than quietly following the looser
one. **What I ran instead is the recorded substitute, and it produced both blocking
findings**: a sweep of the new resolver at seven configurations the diff did not choose
(declared-wrong + env-right, declared-wrong + nothing, `require=True`, the runs key pointed
at the real `HSP-stable`, the stable key set-but-wrong over an existing legacy sibling, a
relative value from two cwds, and all seven touched scripts imported with no worktree and no
env at all), plus a one-variable control on the marker state and a regeneration check on the
plan's own citations. **Batch 26 had already predicted the marker half**
(`tests/corpus/plan_step_marker_resolution.txt`, `id=step_number_is_zero`); nothing in
`tests/corpus/` covers worktree-key resolution, and the R1213/R1214 shapes are the entries
I would write next round if the repair has not already closed them.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN -- which GI6 holds anyway, so this HOLD costs
no schedule.** It is not a stop-work order: step 0's remaining items (the FloatSim run,
GI3(b)'s wall time, (a) and (d)) are exactly the right work to continue with. What must not
happen is step 0 CLOSING with the five conditions below unanswered, and **all five of them
fit in the follow-on commit CZ1 (iv) already requires.** No re-measurement of anything the
plan already settled.

1. **R1213 -- `run_floatsim_design_waves.preflight()` refuses on the measured input.** The
   name test the other two sites already carry, added **beside** the identity test rather
   than replacing it, and the run pasted: `FLOATFEA_HSP_RUNS` pointed at the stable
   worktree, `FLOATFEA_HSP_STABLE` unset, `preflight()` called. That is also `R2.md:253`'s
   and `:291`'s own promise.
2. **R1214 -- a key that is SET and not a directory REFUSES; only an UNSET key falls
   through.** `tried` already distinguishes them. Show both directions (EH4): the set-wrong
   case refuses, and the unset case still resolves through to the legacy sibling so a
   conforming checkout keeps working.
3. **R1206 -- one exit taken, and ruling (1) says it needs no directive and no hook edit.**
   `tests/test_report_carried.py:100`, `:111`, `:617`. Then
   `test_the_plan_names_the_step_under_execution` is green with R2 step 0 under execution,
   and the three-cell table re-run. If you choose a different exit, say which and why; what
   is not available is leaving the tree red by design, which is C89's measured cost.
4. **CZ1 (iv) -- the staleness red answered, in this order, with both outputs pasted:**
   `python scripts/export_f4_dynamic_inputs.py --check` **first** (your determinism
   prediction, GI3(b)'s wall time, and `R2.md` Â§6 item 2's premise, in one run -- and if it
   reports a difference, STOP: that is the escalation, and the provenance is not refreshed);
   then a full **write** run, which is the only thing that rewrites `import_closure`. Expect
   the git diff to be `dynamic_inputs.provenance.json` alone -- `savez_compressed` is
   byte-reproducible, measured above -- and if `dynamic_inputs.npz` moves in that diff, the
   arrays moved and Â§6 item 2 is live. Then the guard green at the follow-on commit.
5. **R1215 -- the marker comment says what the marker says** (FF0, next commit, not the
   ledger).

**And for the step-0 report itself, so the next revision is a revision and not a round:**
its `Answers:` header names **THIS verdict and this sha**, not verdict 59 -- the newest
verdict is the one the guard checks against and the one thing a machine cannot check; the
`Carried` section answers R1206, R1213, R1214 and the ledger above **by hand**, since
`check_carried.py` now correctly reports R2 and will name every finding in this file; and
verdict 58's twelve open items plus verdict 59's four report items are due in it.

**Rounds: step 0 has consumed NONE of its three ES0 revisions.** Verdict 59 was the plan
lock and this is an interim check; both count against none. The next report revision is the
first.

**Nothing here is a STOP, and I considered it.** Rung 4 is red, which is the one thing that
reads like a low-rung failure -- but the red is a provenance-digest comparison, not a
numerical disagreement at a rung, and the low rungs cannot be reached by this diff. Measured
rather than assumed: `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` ALONE, and
`git grep -ln hsp_pin -- tests` (excluding the corpus) returns exactly
`rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py` -- so rungs 1, 2, 5
and 6 contain no test that reaches a changed line. Rung 3's deck-export test and the rest of
rung 4's G4.1 gate are green in my own run at this commit. I did NOT run rungs 1, 2, 5, 6 or
`tests/regression` locally, and CI's ladder job at this sha had not concluded when I ruled;
CI runs rung 6 and `tests/regression` BEFORE rung 4, so the staleness red will not hide
them. The plan is faithful to GI and nothing in it needs reopening.

**What this commit got right, and it is the larger part.** It answered three of four
blocking findings in one commit with no re-measurement asked for, which is what verdict 59
said the HOLD should cost. The two-key routing is correct at every one of the six sites, and
`require=False` is the right default for the right reason -- R670's import-time failure --
which I measured by importing all seven touched scripts with no worktree and no environment
at all. It deleted `HSP_WORKTREE` rather than wiring a constant nothing reads. It raised two
procedure items against itself before I could find them, and the escalation it refused to
take was refused on the correct rule even though the premise turned out to be wrong. And it
said plainly that the red blocks and that R1206 is open, which is the behaviour that makes a
report worth reading last.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 91c2d2e05c7b89a6169c359bc144a1438b6540a1
**Reviewed commit: `91c2d2e05c7b89a6169c359bc144a1438b6540a1`.**
Verdict: HOLD
Scope: **the PLAN-LOCK round GI2 asks for** -- `docs/milestones/R2.md`, added at `91c2d2e`, judged against `docs/directives/GI.md` recorded verbatim at `de04131`. It consumes **none of step 0's three ES0 revisions** and closes nothing, so `--closes` is correctly absent (FK1). Ruled under **FR1 with EZ0**, and every blocking finding below names the silently wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.** EU1 does not arise -- `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file -- and I ran the model at configurations the diff did not choose anyway. **GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the overrun is four blocking findings with their controlled cells, an independent re-derivation of sec.2's five blocks, a read of HSP's own deck builder, and a procedure finding of my own.
Tests: **692 passed, 0 failed, 0 skipped** on `tests/unit` plus the four root guards, my own run in my own worktree at the judged sha, `-p no:randomly`: `692 passed in 194.86s`. That is **470 + 222 and it matches your two runs exactly.** The three report-guard files: **19 failed, 320 passed in 110.41s.** CI's identical guards selection at the judged commit: **19 failed, 1235 passed in 588.62s -- the SAME nineteen ids**, so the two measurements agree and nineteen is the whole of it. I did not re-run `tests/verification` or `tests/regression`, and the reason is measured: `git diff --stat 251af69..91c2d2e -- floatfea tests scripts .github` is **EMPTY**, and the last concluded run's ladder was SUCCESS on all six rungs over that byte-identical code.
CI: **run `44107452079` at the full sha `91c2d2e05c7b89a6169c359bc144a1438b6540a1` EXISTS and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with actionlint, ruff, black, mypy and the unit tests all `success` **before** it -- so the guards step is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii). `the verification ladder` had **NOT finished when I ruled** (`in_progress`); a run that has not finished is not a pass, and no rung is red, so nothing here is a STOP. Both determinism jobs `skipped` by their own `workflow_dispatch` condition. **This is not CK2** -- runners were assigned and the jobs executed for ten minutes. **CA2 IS REACHED: the job is red at the judged commit and twelve of its nineteen reds FAIL the FS1/FT1 predicate**, so the EG3 waiver does not cover them and CZ1 (iv) stands. FP1 held -- the commit was pushed before I was invoked, which is also why `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` is GREEN here and was red at `251af69`.
Door (FV2 / GG2): `git worktree add -b review/91c2d2e05c7b <a path outside the repository> 91c2d2e05c7b89a6169c359bc144a1438b6540a1` **succeeded on the first try, so no review of this commit existed.** Every measurement below taken in that worktree; this verdict written there through `scripts/write_verdict.py`, committed on that branch and pushed. **Two writes of my own, both in my worktree and both reverted before committing** -- the marker cells in R1206 -- and `git status --porcelain` there is empty. In `C:\dev\floatfea` I ran only read-only `git` and `gh`.

**THE FILENAME I WAS ASKED FOR DOES NOT EXIST AND COULD NOT, SO THIS IS `step-0.md` -- R1212.** `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door into `docs/reviews/`, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")` -- so a verdict at `plan.md` would have left R2's CI-section anchor missing and the report guards red with nothing in the loop able to clear them, which is the FP1 failure mode `CLAUDE.md` already records.

## The nineteen, per id, at this commit -- traced from CI's own messages, not classified by family (EG3 (i))

```
cmd    the FAILED list from CI's completed `guards and meta-tests` step, read from
       the job log rather than inferred
out    1   test_the_plan_names_the_step_under_execution
             "2 plans carry a `<!-- step-under-execution: N -->` line
              (['R1.md', 'R2.md']); exactly one must ... which is how a guard comes
              to read a closed milestone's last step and report green while checking
              nothing."
       11  test_the_FAILED_reader_takes_an_id_WITH_A_SPACE[...] -- ALL ELEVEN
             "SystemExit: .../docs/milestones/F2.md carries no
              `<!-- step-under-execution: N -->` line" (scripts/ci_section.py:135)
       7   test_the_guard_survives_the_state[...] -- 2 "expected a clean run",
             5 "a file that is not a numbered step must be stepped over"
cmd    the inner run inside each of the seven, from its own output
out    "12 failed, 284 passed" in all seven, and the twelve ARE the twelve above
cmd    the control -- CI's FAILED list at 251af69, where only R1.md carried a marker
out    7  test_the_guard_survives_the_state[...]   <- the SAME seven
       1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  <- GREEN here
       and NEITHER test_the_plan_names... NOR any FAILED_reader id
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST
       verdict (63affd1's entry on 602bce8). Limb two: its SUBJECT is the commit
       carrying it.
judge  **THE SEVEN are EG3 state (2) and the waiver holds** -- a verdict exists and
       no answering report revision does; they are red in both trees and R2's first
       report clears them. **THE TWELVE ARE NEW AT THIS COMMIT AND FAIL BOTH LIMBS.**
       `docs/milestones/R2.md` did not exist when the newest verdict was written and
       is not among its sites, and none of the twelve is about the commit carrying
       it -- their subject is the marker state of two plan files. **So CZ1 (iv) is
       unchanged for the twelve, and that is R1205 and R1206.**
```

The seven's inner list has gone from **one** id at the previous verdict's trace to **twelve** here, which is the control that the cascade follows its cause rather than being a fixed family -- and the cause it is now following is the one this commit introduced.

## Carried

The newest verdict is `63affd1`'s entry on `602bce8` (verdict 58), and its open items are routed to **R2's first report**, which does not exist yet -- this commit is the plan commit GI2 makes the first of the milestone, so it predates the report that answers them. None of them is answerable by a plan file and none holds this lock. Status, one line each:

* **R1202 (FF0, the base-case sha at five sites) -- ANSWERED before this commit**, at `bb952e7` (`closure: R1202 (FF0) at FIVE sites, not the four named`). Not carried.
* **R1196, R1197, R1198, R1199, R1200, R1201 -- still open, due in R2's first report**, as verdict 58 item 2 routes them. Six prose/one-line items in two files; none blocks under FR1 and none is a plan matter.
* **R1186, R1188, R1189 (c), R1190, R1191, R1193 -- still open, routed to R2** by verdict 58 item 3. R1193 (the dead corpus-pause clause in my own instructions) is **DISCHARGED from my side**: `2e08766` replaced it and I am operating under the post-`2e08766` text -- `grep -c "the corpus pause is \*\*EXPIRED\*\*" .claude/agents/gating-supervisor.md` is 1. R1188's concurrency lever is **answered by GG3**: the group is now per-commit and run `44107452079` started 3 s after creation rather than queueing 71 minutes.
* **R1203, R1204, R835 -- reviewer-side or Xabier's.** R835 is R2's under GE3 and I did not re-measure it.
* **Verdict 58 item 4 -- the one I check here.** It asks R2's first report to answer the newest verdict's commit and carry verdicts 55 through 58. `docs/milestones/R2.md:12` carries that instruction by sha (`63affd1` or later) and by number (verdicts 55 onward), faithfully to GI2. Nothing to answer yet.

## Findings

**R1205. TWO plans carry a live `step-under-execution` marker, and the gate that enforces the `Carried` section now reports on F2 step 4. BLOCKS.**

```
claim  how many plans declare a step under execution at this commit
cmd    grep -rlE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
out    docs/milestones/R1.md      (line 3: `<!-- step-under-execution: 4 -->`)
       docs/milestones/R2.md      (line 3: `<!-- step-under-execution: 0 -->`)
cmd    python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
out    ('F2', 4)
cmd    python scripts/check_carried.py ; echo exit=$?
out    check_carried: the newest report's Carried section omits R216, R217, R218,
         R219, R220, R221, R222
       verdict declares 7 findings; 0 are carried
       exit=0
cmd    python -c "import scripts.ci_section as c; print(c.MILESTONE)"
out    SystemExit: docs\milestones\F2.md carries no `<!-- step-under-execution: N -->`
       line, so there is no step to generate a section for.
rule   scripts/check_carried.py:126-130 and scripts/ci_section.py:98-106 -- both fall
       back to F2 when the count is not exactly one; .claude/hooks/require-verdict.sh:105
       blocks a turn on it; tests/test_report_carried.py:608 asserts against it
judge  **New at this commit** -- at `251af69` only R1.md carried a marker and
       `test_the_plan_names_the_step_under_execution` was green in CI there.
```

**The silently wrong result:** `scripts/check_carried.py` -- the gate that enforces the one thing `CLAUDE.md` says the whole arrangement exists for, that the previous review's open items get re-read -- reports on `docs/reports/F2/step-4.md` against `docs/reviews/F2/step-4.md`, names seven F2 findings nobody has to answer, and **exits 0**. R2 step 0's report can ship with an absent or wrong `Carried` section and nothing is red. Its own comment is the sentence: *"a guard reporting green about the wrong milestone."* Second consequence: `scripts/ci_section.py` cannot import, so R2's report cannot generate the CI section CE1 makes mandatory, and **11 report-guard ids die on that import** (`SystemExit` at `scripts/ci_section.py:135`). *Closed when* `docs/milestones/R1.md:3` retires its marker the way `F2.md:10`, `F3.md:9` and `F6a.md:3` retire theirs -- `<!-- step-under-execution: moved to R2 at step 0 (GI) -->` -- in a commit that also answers R1206.

**R1206. `step 0` is not representable: `0` is both a legal step number (GI3) and the resolvers' sentinel for "unclear". BLOCKS (CZ1 (iv)); apparatus, so FF0 and not the ledger.**

```
cmd    cell 1 -- the judged tree (R1=4, R2=0), test_the_plan_names_the_step_under_execution
out    RED: "2 plans carry a `<!-- step-under-execution: N -->` line"
cmd    cell 2 -- R1's marker retired, R2's left at 0. ONE VARIABLE MOVED
out    RED: "docs/milestones/R2.md carries no readable step number, so the guards fell
       back to the newest complete report/verdict pair ... it makes the step boundary
       permanently red."   assert 0 > 0   where 0 = _plan_step()
cmd    cell 3 -- R1 retired AND R2's marker set to 1
out    RED at tests/test_report_carried.py:639 instead -- the expected "no report yet"
       state, which R2's first report clears
rule   tests/test_report_carried.py:617; _active_plan returns the sentinel `(None, 0)`
       at :110, so a real step 0 and "no marker" are the same value
judge  Retiring R1's marker does NOT clear this. My own corpus predicted it:
       tests/corpus/plan_step_marker_resolution.txt, `id=step_number_is_zero`,
       `expect=caught measured=RED_the_plan_carries_no_readable_step_number`, batch 26.
```

On its own this red is TRUE and loud, so it misleads nobody once R1205 is fixed -- but it cannot be left, because a tree red by design is a tree in which the next real red is harder to see, which is C89's measured cost, and FF0 puts an item in the gating apparatus in the next commit rather than the ledger. Three exits and **the choice is yours, not mine**: renumber R2's steps 1..5 (which breaks GI's own numbering and GI2's "before any step-1 code"); keep the marker at the NEXT step and record step 0 another way; or separate the sentinel from the value in the three resolver copies and the two scripts -- a repair of an existing guard, which EK2 permits and FK2's "no new apparatus" does not forbid. *Closed when* one is chosen, the cell above is re-run, and `test_the_plan_names_the_step_under_execution` is green with R2 under execution.

**R1207. Step 2's gates (ii) and (iii) are both passed by a build in which the mass never reaches FloatSim. BLOCKS.**

```
claim  what the zero-change test's own input is
cmd    python -c "import yaml; d=yaml.safe_load(open('data/platform/platform12_deck.yaml'));
         print([(b['name'],b['mass']) for b in d['bodies'] if b['name'] in ('platform','hub1')])"
out    [('buoy1', 28.67)... ('hub1', 12.0), ('platform', 20.0)]
cmd    python -c "import numpy as np; z=np.load('data/f4/dynamic_inputs.npz');
         print(list(z['case0/body_mass']))"
out    [20.0, 12.0, 12.0, 12.0, 12.0]
rule   GI5 step 2: "feeding today's masses reproduces the reference run ... bit-identical"
judge  the committed deck's masses ARE today's masses, so a build whose override
       plumbing is a NO-OP reproduces the reference run EXACTLY. (ii) is green on code
       that ignores its mass input entirely.
claim  whether (iii) can fail
rule   D1: `body mass = m_nonstruct + k x m_steel`; GI5 step 2: "member steel +
       non-structural + ballast = body mass, exactly"
judge  D1 DEFINES body mass as that sum, so the identity is over FloatFEA's own
       arithmetic and cannot fail on anything but an addition bug.
```

**The silently wrong result:** the converged design step 3 publishes -- its sections, member forces, utilisations, the iteration table, and everything it writes under `results/` -- computed from FloatSim runs that used the deck's own masses rather than the sized ones, with gates (ii) and (iii), `pytest`, `ruff`, `black`, `mypy` and all six ladder rungs green. That is the loop still open at exactly the end GI0 exists to close, and no gate in the locked set would say so.

**The repair needs no new apparatus, because the mechanism already ships, inverted.** `scripts/export_f4_dynamic_inputs.py:467-479` is already Q8's rule -- `np.array_equal` over every array, *"there is no tolerance on this comparison"*, non-finite failing in its own right. So **(ii) becomes a pair**: the zero-change run reproduces bit-identically **and** a run at a perturbed mass does NOT, differing in `case<i>/body_mass`, `m_xddot` and `accel`. And **(iii) closes against the run's own record** -- `case<i>/body_mass`, which `export_f4_dynamic_inputs.py:390` takes from the deck the solve actually used -- rather than against the tool's variables. Provenance, not existence. *Closed when* sec.3's step-2 gate carries the inverted half of (ii) and (iii) reads back from the npz.

**R1208. sec.2c specifies ONE config key routed to all six sites, and the six sites are not one worktree. BLOCKS.**

```
cmd    for each: test -d and git describe --tags
out    C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable  EXISTS  floatfea-ref-1
       C:/Users/xlama/OneDrive/Documents/buoy/HSP-runs    EXISTS  floatfea-ref-1
       ../HSP-stable and ../HSP-runs from C:\dev\floatfea  BOTH MISSING
cmd    git grep -nE '(ROOT|parents?\[[0-9]\])\s*(\.parent)?\s*/\s*"HSP-' -- '*.py'
out    scripts/export_buoy_centers_ref.py:42    HSP_STABLE -> HSP-stable
       scripts/export_platform_deck.py:45       HSP_RUNS   -> HSP-runs
       scripts/measure_platform_joints.py:48    HSP_RUNS   -> HSP-runs
       scripts/report_joint_reactions.py:96     HSP_RUNS   -> HSP-runs
       scripts/run_floatsim_design_waves.py:50  RUNS       -> HSP-runs
       scripts/run_floatsim_design_waves.py:51  STABLE     -> HSP-stable
rule   DS0, enforced by three refusals keyed on the NAME `HSP-stable`:
       report_joint_reactions.py:106, export_platform_deck.py:75,
       run_floatsim_design_waves.py:98
judge  five of the six sites want HSP-runs, one wants HSP-stable, and the three
       refusals make a single key pointed at HSP-stable loud. **The remaining
       direction is silent**: a single key pointed at HSP-runs sends
       `export_buoy_centers_ref` there, and that script has no DS0 refusal of its own.
```

**The silently wrong result:** `data/platform/buoy_centers_ref.json` -- a shipped data file, the input to EB6's label-provenance gate -- regenerated from `HSP-runs` while its `"source"` field declares `HSP-stable/studies/platform-12buoy/platform_common.py` and `_blob_sha` records that tree's sha. `--check` stays green because both sides move together, which is C155's shape, recorded in that file's own docstring. Both worktrees are at `floatfea-ref-1` today, so the bytes match and nothing shows -- and R2 is about to start running FloatSim in one of them. That is FR1's second head verbatim: an input accepted and used other than as declared. **FZ rule 7 would probably reach the right answer on its own**, and I block anyway because the plan's own words specify the wrong thing and GI2 gives no review between this one and step 0's close. *Closed when* sec.2c and sec.3's step-0 gate say TWO keys, name which sites take which, keep `export_buoy_centers_ref` on the stable key, and show the three DS0 refusals still firing.

## The four rulings you asked for

**(1) Is the plan faithful to GI? YES on every gate, with two departures you should state.** GI5 step 2's four sub-gates are all present at `R2.md:173-180` and GI5 step 3's acceptance at `:182-187`, none softened. Five additions are all STRICTER and each traces to GI's own text: read-only-on-HSP and the run folder on (i) (GI1), "not warned" on (iv), the refusal-by-name for a non-converged design on step 3 (D3's last sentence, which GI5 step 3 did not itself carry), the heading refusal on step 1 (FL2(c)), and "never the witness" on step 4. The departures:

* **GI5 step 1's input is "a FloatSim npz"; `R2.md:168` makes it "a FloatSim solve".** sec.2d's reading is right and I measured it: `scripts/export_f4_dynamic_inputs.py:187-196` calls `solve_one`, and the npz is that run's OUTPUT -- there is no FloatSim-written npz in this repository to read. But the consequence is that **step 1 performs the FloatSim invocation GI5 assigns to step 2**, which GI6 gates, and the plan does not say so. State which, and which part of GI6's hold it crosses.
* **`R2.md:165` drops GI3(d)'s purpose clause** "so draft can be held (GI4 D2)". One clause; sec.4 row 1 carries the tie. Prose.

And one addition I checked rather than accepted: step 1's `U = 1.71167` **"at `platform:hub4_arm` ROOT"** is right as the TOOL's own line, and it is a **tie at six figures** -- `docs/F6_utilisation.csv:40` and `:44` give `hub2_arm` and `hub4_arm` the same `1.71167`, and `docs/USER_GUIDE.md:966-975` records the full-precision split. An acceptance that asserts the member NAME must read the tool's line, never a `max()` over the rounded CSV.

**(2) Are sec.2's five measured blocks true? Four yes, one wrong in its `out` line, and the census in sec.2c wrong three ways.**

* **sec.2a -- TRUE, and the "no escalation" conclusion is RIGHT.** The census reproduces line for line (four sites, the numbers as printed), and the mechanism reproduces by reading: `solve_one` builds the deck from `prp._deck_with_drag()`, mutates it at `report_joint_reactions.py:158-163`, and runs `integrate_cummins` -- a FloatSim **time-domain** integration, in-process, HSP source untouched. `case0/body_mass = [20.0, 12.0, 12.0, 12.0, 12.0]` reproduces too. **I went one step further than the plan and read HSP's own builder, which settles GI3(c) harder than sec.2a does:** `platform_rao_pilot._deck_with_drag()` **takes no arguments and reads no file** -- it constructs all 17 bodies in Python from `platform_common.py:41` (`PLATFORM_MASS = 10.0`), `:158` (`mass=cc.ARM_MASS_TOTAL`), `:159` (`Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)`, the hubs) and `:177-178` (the platform). So there is **no file input to HSP's builder at all**, the returned object is the only override point, and the escalation GI1 contemplates is not merely unnecessary -- it is the ONLY alternative, and it would be an edit to FloatSim source. **Your reading is right; raise no escalation.** And an independent corroboration the plan does not give: GI4 D1's own `625 t` and `375 t` are `(1 - 0.75) x 2500 t` and `(1 - 0.75) x 1500 t`, i.e. ER0's platform at lambda = 50, not HSP's 1250 t -- **GI4's numbers confirm sec.2a's reading of "today's masses"**. Caveats are R1207 and R1211.
* **sec.2b -- the conclusion is TRUE and reproduces; one `out` line is FALSE.** `periods_full_s = [10, 12.5, 14, 15, 16.2, 20]`, six cases in the npz, one heading => **six FloatSim cases per iteration** YES, and D4 needs no working-set escalation on heading count YES. But "config declares ONE heading" is not what the command returns: `grep -n heading examples/platform12_placeholder.yaml` returns exactly one line and it is **a comment at line 8**. The config declares **no heading key at all**; heading 0 lives in `report_joint_reactions.WAVE_HEADING_DEG` and in `data/f4/dynamic_inputs.provenance.json`'s `run.heading_deg: 0.0`. **That matters forward**: D4's "every heading in the R1 config" is *unrepresentable* today, and that absent key is what step 1's heading refusal has to grow into. **The 3.66 h / 40.6 GB figures ARE good enough for a plan row, and the reason is specific**: the second heading is excluded by GI1's ban on `platform_bem.py`, not by its cost, so the figures could be wrong by a decade and sec.2b's conclusion would not move. The plan attributes them to the docstring, which is what BP0 needs. One wording point -- sec.2b bolds them as "**measured**" when they are *recorded as measured elsewhere*; if any decision ever rests on them, they get re-taken.
* **sec.2c -- the diagnosis is RIGHT, the WIDER READING IS AUTHORISED, and the census is wrong three ways.** See the ruling below and R1208/R1209.
* **sec.2d -- TRUE and measured.** `cli.py:1279` is the FL2(c) comment, `:1291-1297` the refusal, and the command validates its config and the declared cases before refusing.
* **sec.2e -- TRUE, and I reproduced the consequence rather than reading it.** `rho_eq = f.M_b/(L_b.A)` by construction (`floatfea/model/platform.py:47-48`), so at the shipped config the builder gives platform `rho_eq = 7146.0` / member mass `1875.0 t` and each hub `11433.5` / `1125.0 t` -- **independent of the section, exactly as claimed**. `cli.py:830-833` ships the same sentence to every reader. The second sentence (three configurations, identical densities) carries no triple and I did not reproduce it; the mechanism half is enough to carry sec.2e.

**THE RULING ON THE SIX-SITE READING, WHICH YOU ASKED FOR DIRECTLY: YOUR READING IS RIGHT AND I WOULD GO FURTHER.** GI3(e) names `hsp_pin.HSP_WORKTREE` as the symptom -- *"It does not resolve from `C:\dev\floatfea`"* -- and prescribes a mechanism (*"a config key with an env-var fallback"*). Fixing only that constant fixes **nothing**, and that is measured: `git grep -n HSP_WORKTREE` over the whole tree returns the definition at `floatfea/hsp_pin.py:20` and three documentation hits, and **no consumer**. GI3(e) exists so that step 0's own items (b) and (d) can open the worktree, so routing the sites that actually open it through the new key is the **same item**, not new scope. It is authorised; write it. **R1208 is the one condition on it**: two keys, not one.

**(3) The two "not a tolerance" classifications -- BOTH CORRECT, and one has a shipped precedent.**

* **The iteration cap `8` -- correctly not a tolerance.** Nothing is compared against `8` to decide a result is good; exceeding it produces a **refusal** (D3's "stop and report", `R2.md:186`'s "refused by name"), not an accepted number. That is this repository's own test, stated in `PLATFORM_MASS_OVERRIDE`'s docstring: *"not-a-tolerance: ... Nothing is compared against them."* **But the classification is only as safe as that refusal, and nothing mechanical will hold the value**: `tests/test_no_tolerance_literals.py`'s own docstring says *"integers are counts and are never flagged"*, so `8` becoming `80` is invisible to the one guard that would look. Declare it as a named module constant with a `not-a-tolerance:` justification -- the convention `PLATFORM_OVERRIDE` and `hsp_pin.BASELINE` already use -- so raising it is a visible act. And `R2.md:195` says "**Every** value below goes in `floatfea/tolerances.py`" while two rows say they are not tolerances: say where those two live.
* **The determinism bound -- correctly not a tolerance, and row 5 is not a declaration to write at all.** The comparison already exists in exactly the right form at `scripts/export_f4_dynamic_inputs.py:467-479`: `np.array_equal` on the raw arrays, *"A regeneration either reproduces it exactly or it does not (Q8); there is no tolerance on this comparison"*, with non-finite values failing in their own right rather than comparing equal to zero. Step 2 reuses it rather than re-deriving it. **And that makes sec.6 item 2 measurable today -- see (4).**

**(4) What sec.6 should settle now. Three things, and the first is nearly free.**

**(a) sec.6 item 2's premise is measurable TODAY, and the whole of step 2's (ii) rests on it.** `python scripts/export_f4_dynamic_inputs.py --check` re-runs all six cases through `solve_one` and compares bit-exactly against the committed npz. That single command **is** GI3(b)'s wall-time measurement *and* the determinism measurement; running it twice costs one more pass. Nothing in this repository has published a measurement of FloatSim's determinism on this path, and Q8's premise is the thing step 2's bit-identical gate is built on. Convert the argument into a measurement.

**(b) sec.6 does not carry the contradiction between D1 and the step-2 bookkeeping identity, and GI6 is the only scheduled point where D1-D4 can be corrected.** D1: `body mass = m_nonstruct + k x m_steel`. GI5 step 2 (iii): `member steel + non-structural + ballast = body mass, exactly`. **The two are consistent only if ballast == 0** -- and if ballast is identically zero then D2's draft can never be held when `m_steel` moves, so (iv)'s refusal fires on the design rather than on a test. One of the two has to gain a ballast term and Xabier is the one who says which. This is loud rather than silent when it bites, so it does not block; it belongs in step 0's report because that is where it can still be cheap.

**(c) sec.6 item 3 is not a contingency -- it is a number, available today, and step 0 (d) should publish it.** Measured at this commit from the shipped deck and the shipped builder:

```
cmd    which bodies carry a hydro label
out    buoy1..buoy12  hydro_body_label = 'buoy1'...   platform, hub1..hub4  None
cmd    the builder's own member geometry and D1 at k = 1.0, lambda = 50
out    platform  steel 2059.7 t vs 1875.0 t allocated   steel/alloc = 1.0985
       each hub  steel  772.4 t vs 1125.0 t allocated   steel/alloc = 0.6866
       D1: platform 2500 -> 2684.7 t (+7.39%), each hub 1500 -> 1147.4 t (-23.51%)
       the five bodies 8500 -> 7274.3 t = -1225.7 t (-14.42%)
       the 12 buoys carry 43005 t, so the deficit is 2.85% of them
rule   D3's convergence band is 0.5% per body between iterations
judge  **the bodies whose mass D1 changes carry NO buoyancy, and the bodies that
       carry buoyancy are not changed by sizing.** So D2's "every floating body (or
       the buoy carrying a changed body) gets compensating ballast" is written for a
       picture this deck does not have: ballast has to sit on the NON-wetted bodies,
       and "the draft is held" becomes a condition on total weight and its
       distribution, measured per BUOY. And iteration one moves every mass one to two
       decades outside D3's band, so the loop certainly iterates -- what nobody has
       measured is whether the BEM reference survives the ballast it implies.
```

This also reproduces both near ends of `R2.md:31`'s range (`+10%` -> `+9.85%`, `-31%` -> `-31.34%`) at this commit, which is the re-measurement sec.0 routes to step 0 (a).

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1209 -- sec.2c's census is wrong three ways, in the R755/R1147 shape: an `out` block that reports more than its own `cmd` returns.** The heading says "five sites" and the body says "SIX sites in five files"; it is **six files**, not five; counting assignments it is **seven**, because `run_floatsim_design_waves.py` has two (`RUNS` at `:50`, `STABLE` at `:51`) at line numbers the plan prints as `49-50`; and **the quoted needle cannot see either of them** -- `grep -rn "HSP_RUNS\s*[:=]\|HSP_STABLE\s*[:=]\|HSP_WORKTREE" --include=*.py .` returns **five** lines, not the six printed. The needle that finds all seven is in R1208's block. The plan's `HSP_WORKTREE`-has-no-consumer claim is **TRUE** -- I ran it over the whole tree, not just `*.py`.
* **R1210 -- sec.2b's "config declares ONE heading" is false as measured** (see ruling 2). The conclusion is unaffected.
* **R1211 -- sec.2a and sec.3 use one word for two mechanisms, GI3(c)'s first half is unanswered, and four of the five bodies have never been overridden by anything.** GI1 requires mass changes to go *"through HSP's deck builder with a declared override file, as ER0 did"*; `R2.md:174` says FloatFEA "writes the override file" YES, while sec.2a's judge says step 2 must "move it out of a script global into the tool", which is the **in-memory** path where nothing on disk declares what was applied. ER0 did BOTH -- `export_platform_deck.apply_override` mutates in memory **and serialises to `data/platform/platform12_deck.yaml`**, and `export_f4_dynamic_inputs` records the dict in `dynamic_inputs.provenance.json`'s `"override"` block. Step 2 says which, and the declared-on-disk half is what makes the override auditable. GI3(c)'s first half -- *how* mass and inertia enter the builder -- has the precise answer in ruling 2 and the plan does not state it. And **the existing helper is the wrong shape to generalise**: `_apply_platform_override` selects `b.name == "platform"` and sets three inertia components, while `_inertia_matrix` reads six and *"the off-diagonals are read rather than assumed zero"*; the four hubs sit at `cc.ARM_MASS_TOTAL` and the literal `Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)` with **no override anywhere in this repository**. One body -> five, three components -> six, and `export_platform_deck.apply_override`'s generic dict walk is the better shape.
* **sec.4 row 1 does not declare the FORM of the equilibrium-drift tolerance, and draft is a LENGTH.** An absolute tolerance on a dimensional quantity either fails the unit-scaling test or passes it vacuously, so the entry has to be relative to a stated response scale -- the BEM reference draft, or the buoy radius -- and dimensionless, with trim against a stated angle scale. sec.4's stated purpose is to be reviewable before the value exists, so the form belongs there now.
* **sec.2's CP3 header overclaims.** It says "Figures taken at this commit, after the last edit", and two are not: sec.0's `+10% to +29% / -31% to -55%` (attributed to pre-R2 work and correctly routed to step 0 (a) -- both near ends reproduce, ruling 4c) and sec.2e's "three configurations" (no triple at all, and a causal "so" with no cell, BG0). Say which figures are this commit's and which are carried.
* **sec.2's five triples are not machine-checked and two are not runnable.** `tests/test_tree_prose_consistent.py` reads `^claim:` / `^cmd:` / `^out:`; `grep -c "^cmd:" docs/milestones/*.md` is 0 everywhere, so the space-aligned form R1.md and R2.md both use is invisible to the guard that scans `docs/milestones`. And `python -c "...np.load(NPZ)..."` has no `NPZ`, while sec.2b's is an ellipsis. R1.md uses the same form, so this is the house convention and not a new deviation -- but a `cmd` a reader cannot run is not a check.
* **sec.5 does not carry GI1's "the deck stays DO-NOT-HAND-EDIT".** One line; it belongs beside the three prohibitions.
* **R1212 -- MINE, and it goes to Xabier, not into a round.** I was asked to write `docs/reviews/R2/plan.md`. That path does not exist and cannot: `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")`, so a file named `plan.md` would not be found and R2's CI-section anchor would stay missing -- the FP1 failure mode `CLAUDE.md` already records. I used `--step 0 --interim`: no report revision exists, it consumes none of step 0's three ES0 revisions, and it closes nothing. **The `--interim` header the tool stamps says "ES0 INTERIM CHECK", which is accurate about rounds and mislabels the round's nature** -- this is GI2's plan lock. If a separate plan-lock artifact is wanted, that is an edit to `write_verdict.py` and to `ci_section.py`'s glob, and it is Xabier's to authorise.

## Tolerances touched

**None.** `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file. sec.4 declares five future entries and I ruled on their classification above; **"None of them exists yet" is true** -- the only convergence entry in the file is `BOUNDARY_BISECTION_CONVERGENCE` at `:1290`, which is a solver-internal bisection and not D3's loop. EU1 does not arise.

## Corpus

**No new batch, and GC3 leaves that to me.** What I ran instead is the substitute GG1 records, and it is where three of the four blocking findings came from: a **continuum grid over the parameter space D1's rule guards** (all five bodies, steel against allocated mass, through the shipped builder -- ruling 4c), a **regeneration check on the published figures** (sec.0's two ranges, sec.2a's npz block, sec.2e's densities, all re-derived at this commit), and **three controlled cells on the marker state**, one variable each. A batch would have bought none of them on a commit that contains no code.

**And batch 26 had already predicted both halves of R1205 and R1206.** `tests/corpus/plan_step_marker_resolution.txt` carries `id=two_plans_carry_it_F3_and_a_new_F4 ... expect=caught measured=RED_2_plans_carry_it` and `id=step_number_is_zero ... expect=caught measured=RED_the_plan_carries_no_readable_step_number`. **The tree is now in both states at once**, eleven batches later, and that is the corpus doing the job it exists for -- which is the reason I am not spending this round writing another one.

## Next step opens when

**STEP 0 DOES NOT OPEN YET, AND THE REASON IS CHEAP: one commit touching `docs/milestones/R1.md` and `docs/milestones/R2.md`, with no re-measurement of anything.** GI2 asks for one round and I am not asking for a second review before step 0's code -- **PASS follows automatically from the four conditions below being visible in the diff**, and I have written them so that the implementer can satisfy them without another invocation. What they must not do is start step 0's code with the gating apparatus in the state R1205 measures.

1. **R1205 -- `docs/milestones/R1.md:3`'s marker retired**, in the form `F2.md:10`, `F3.md:9` and `F6a.md:3` use. Then `python scripts/check_carried.py` names **R2**, not F2 step 4, and `python -c "import scripts.ci_section"` stops raising. Paste both.
2. **R1206 -- one of the three exits chosen for step 0's number**, with `test_the_plan_names_the_step_under_execution` green at R2 under execution, and the cell re-run. If the exit is renumbering, say what happens to GI2's "before any step-1 code".
3. **R1207 -- sec.3's step-2 gate carries the inverted half of (ii)**, and **(iii) reads `case<i>/body_mass` back from the npz the solve wrote.** Both are amendments to `R2.md`, not code: GI6 holds step-2 code regardless, and this is the only moment at which the gate is still free.
4. **R1208 -- sec.2c and sec.3's step-0 gate say TWO keys**, which sites take which, `export_buoy_centers_ref` on the stable key, and the three DS0 refusals shown still firing.

**Then step 0 opens and nothing else does.** GI6 holds step 2 regardless, and step 1's code waits on Xabier's answer to D1-D4 as well -- because ruling (1)'s first departure means step 1 as written performs the FloatSim invocation GI5 assigns to step 2. Say which in the amendment.

**And four things for step 0's report, none of which blocks and all of which are cheap now:** the `--check` determinism run (ruling 4a, one command, answers GI3(b) too); the D1/(iii) ballast contradiction put in front of Xabier (4b); GI3(d) answered with the wetted/non-wetted split and the `-1225.7 t` first iteration (4c); and GI3(c) answered in BOTH halves, with HSP's zero-argument builder named, because that is what tells Xabier the escalation is not merely unnecessary but impossible without an edit to FloatSim source.

**On the schedule.** GI sets no date and `R2.md:14-16` says so rather than inventing one, which is the right handling. This HOLD costs one commit and no measurement. **Nothing here is a STOP**: the plan is faithful to GI, the ladder was green on all six rungs at the last concluded run over code byte-identical to this tree, and no low rung is red.

**What the plan got right, and it is much the larger part.** It went and measured the five things the steps rest on instead of asserting them, and four of the five hold exactly as written. It found the override path GI3(c) asks about and read it correctly enough to withdraw an escalation -- which is the single most consequential call in the document, and it is right for a reason stronger than the one it gives. It noticed that "today's masses" is ambiguous and that `None` is a different run, which is the distinction the zero-change test lives or dies on. It read GI3(e) wider than GI wrote it and said why, on the half-an-item rule, rather than doing the literal minimum. And it declared two of its five tolerance rows as **not** tolerances with the reasoning attached, which is the step at which a tolerance usually ships without a counter.
