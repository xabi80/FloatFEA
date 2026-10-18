# Review — R1 step 3
Reviewed commit: e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
**Reviewed commit: `e6a20e330fa1afc91fdc32b3d4eb3292f45898a2`.**
Verdict: PASS
Tests: 3547 passed, 78 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK, the second in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **Nothing
blocks.** Three of the four gate findings verdict 10 ledgered are repaired, and I verified each
by my own injections rather than by reading theirs; five findings below, none blocking.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1",
`docs/directives/FR.md`). For each finding I say the silently wrong result it would produce, or
that it produces none. **This file is HAND-WRITTEN because the one sanctioned path in refused it
again -- R856, second occurrence, measured below.**

```
cmd    git diff --name-status 0aa0c4a..HEAD
out    M  tests/regression/test_r1_example_regenerates.py
       -- one file, 68 insertions, 5 deletions, nothing else
cmd    git diff --stat 0aa0c4a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff 0aa0c4a..HEAD -- floatfea
out    (empty)                                   -- FR1 head (a) is unreachable from this diff
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
cmd    git diff 0aa0c4a..HEAD -- results scripts docs
out    (empty)                                   -- no published deliverable moved
cmd    printf <the four mandatory sections> | python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1                                    -- R856, unchanged and unchangeable here
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`), and two
verdicts are newer than it. That is EG3 state (2) by definition, and it is the whole of this
tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R850** (the wall-clock exclusion covered three of the five rows the generator writes; and no check reads a published wall-clock value) | **HALF ANSWERED. The five-stage half is repaired and I verified it in both EH4 directions. THE PROSE HALF IS UNTOUCHED AND STILL FALSE -- see R858.** My closing condition named two things, and "half of an item is not the item" is CLAUDE.md's own sentence. | Repaired: `_TIMING_STAGES` feeds both the regex and the pin, so those two cannot drift apart. Verified by me: `| load |` and `| code_check |` set to `999.99` are now green (both were inside the byte comparison before); a DUPLICATE `| total | 1234.00 |` row reddens the pin; a MISSING `| code_check |` row reddens the pin; a timing-shaped row reaching a CSV reddens `test_R845_the_CSVs_carry_NO_excluded_timing_row`. **So the widening is bounded in all three files, which is the question the implementer asked me.** Still open: the claim that both excluded classes "ARE CHECKED SEPARATELY", while nothing in the tree reads a published wall-clock value. |
| **R851** (`_provenance` returned a dict so a duplicate `# deck:` line collapsed; the key-set pin read `report.md` alone) | **ANSWERED, and I reproduced my own exact injection against the repair rather than taking its counter-cases** | `_provenance_lines` and `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the same file. My verdict-10 injection -- a second `# deck:` line with the SAME basename and a different directory, green before -- now reddens, in utilisation.csv and in report.md, **and reddens exactly one case** (the new one), which is the measurement that says the repair and not something else caught it. Two evasions I had not tried are caught as well, by different tests: `# Deck:` (capital, unmatched by the exclusion) falls into the byte comparison; `#deck:` with no space is caught by the new test AND by the basename test. The FRESH half of the new test is live -- injecting into the regenerated side alone reddens it. |
| **R853** (the published "102, 1289 and 73 comparable lines" did not reproduce) | **ANSWERED IN FORM, WRONG IN SUBSTANCE -- the corrected figure is correct against the rule the SAME COMMIT deleted. See R857.** | The commit took my 99/1286/70 and published it while widening the exclusion from three stage rows to five, which makes the report's comparable count 97. BP0 names this exactly: when a decision rule changes, every figure citing the old rule is regenerated in the same commit. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **relayed to Xabier by the implementer, correctly, and unchanged by this diff** | Mine, not the implementer's to repair in code. No new measurement this round. |
| **R856** (`write_verdict.py` refuses a step with no report) | **relayed to Xabier, and this is its SECOND measured occurrence** | the refusal is in my command block above. Under FF0 it is apparatus and not ledgered; the exit remains a clause, not a commit. |
| **R855** (the suite was not run at a pushed reviewed commit, and the tree's reds were not recorded with their cause named) | **STILL OPEN, third commit running. The implementer ran one file and asked whether the light scope requires the full run. IT DOES. I ran it: 78 failed, 3547 passed, 1 skipped in 966.33 s, every red traced below one id at a time.** | The offer to produce it rather than argue the scope is the right instinct and I am recording that; the answer is that ES0's light scope is the suite, and EG3(i) makes the waiver conditional on a trace that is pasted. **And the baseline I gave for that trace was wrong within one commit -- R861.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- C43, and there is no report revision in which it could be answered** | FR1's third class. Unchanged by this diff. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot and a padded dot) | **still open, untouched, correctly so** | `git diff 0aa0c4a..HEAD -- floatfea` is empty. Non-blocking, same class as R843. |
| **R849 with R854** (the caveat, disclaimer, provenance AND regeneration gates quantify over hard-coded three-file tuples, and step 3 publishes two more files) | **still open, both sites, and now with a second reason to be done before FL2 lands** | the two constants are `NAMES` in the regeneration gate and `ARTIFACTS` in the published-artifacts gate. Answered WHILE step 3 is built, as verdict 9 ruled. R860 below gives the same item its sharper reason. |
| **R835, R836** (EG3's enumeration; and R836) | **still open, still Xabier's; this commit is the ninth measurement of the enumeration** | and it over-lists again: of state (2)'s enumerated names, seven fire and two (`test_the_answered_verdict_is_the_NEWEST_one`, `test_a_carried_row_points_at_a_section_that_discusses_it`) are green. Relayed unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, locally AND on a machine neither of us controls** | mine: `ruff` `All checks passed!`; `black` `148 files would be left unchanged`; `mypy` `Success: no issues found in 43 source files`. CI run 39173178232, job `lint, unit and guards`, step level: `actionlint` SUCCESS, `ruff` SUCCESS, `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 164.24s`). Every one RAN rather than being skipped behind an earlier red. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired here. |
| **C43, C44, C45** | **C43 and C44 carry; C45 is unchanged and still unpayable before step 3's report exists** | see verdict 10's process note, which stands except for its baseline figure (R861). |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **The R850/R851/R853 ROUTING QUESTION the implementer asked me to check** | **ANSWERED: half right. EK2 governs the FORM of a repair and these repairs honour it; it is not a route that pre-empts the ledger, and FF0 does not reach this file.** | See the routing ruling below. No repair has to be undone. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files at e6a20e3: **78 failed, 165 passed, 1 skipped**, which is the same 78 as the whole suite's and the same 78 as CI's, id for id. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## The routing ruling

**The implementer asked for the classification to be checked as hard as the repairs, so it is
checked here and not glossed.** The answer is that it is half right, and nothing has to be
undone.

```
claim  EK2 is a constraint on the FORM of a repair, not a route that pre-empts the ledger
cmd    CLAUDE.md, the clause EK2 is cited from
out    "No new apparatus through F6. ... An existing guard that fails false is fixed or
        deleted, never extended."
       -- it says what a repair may be. It says nothing about when, or about the ledger.
claim  FF0's route does not reach this file
cmd    CLAUDE.md section "What blocks, and what is a closure item (CZ0)", the FF0 paragraph
out    "Anything that reads the gating record, or decides whether a green is believed -- the
        report guards, scripts/ci_section.py, scripts/suite_count.py, .claude/hooks/, the EG3
        lists -- is fixed in the next commit."
       -- tests/regression/test_r1_example_regenerates.py decides whether a PUBLISHED
          DELIVERABLE is believed. It reads no gating record and no green. Not FF0's class.
claim  the locked plan routes a non-blocking interim finding to the ledger, by name
cmd    docs/milestones/R1.md, step 3's paragraph
out    "Only FR1-blocking items from those checks are fixed in flight; everything else is
        ledgered. That ordering is the directive's answer to the measurement both reviewers
        reached independently -- the repairs were one line each and the rounds were the cost."
rule   FR1 -- R850, R851 and R853 were each ruled NON-blocking in verdict 10, so the plan's
       sentence routes all three to the ledger
judge  **the repairs are sound and I would rather have them than not; the route was the
       ledger.** Three consequences, and they are bookkeeping rather than rework. (i) EK2's
       form is honoured and conspicuously so: the set is NAMED rather than the comparison
       given slack, and the 0.02 tolerance I proposed against myself was declined -- that is
       the right call and it is the opposite of widening. (ii) R850, R851 and R853 stay on the
       R1 ledger as PAID EARLY, R850 as HALF paid, so the closure list does not lose them.
       (iii) The cost is the one the plan's sentence predicts: this is the second commit of
       step 3, and FL2 has five items with none of them built, against FR0's 5 November. The
       implementer says so plainly and claims none of it, which is the correct thing to have
       done; I am recording the arithmetic rather than a fault.
```

## Findings

**NOTHING BLOCKS.** The diff is one test file. No `floatfea/` line moved, no tolerance moved,
no published deliverable moved -- and I established the last of those by regenerating all three
artifacts twice rather than by reading the diff. Under FR1 none of the five findings below can
put a wrong number in front of anyone, and I say which for each.

**R857. (DOES NOT BLOCK -- ledgered) R853'S REPAIR REPUBLISHED R853'S DEFECT. The corrected
figure `99, 1286 and 70 COMPARABLE lines` in the exclusion comment was measured against the
THREE-stage exclusion that THIS COMMIT deleted. Under the shipped five-stage rule the report's
comparable count is 97. The two CSV figures are right.**

```
claim  the figure the file publishes as "the measurement that says the numbers are reproduced"
       is not a measurement of the rule the file now runs
cmd    the gate's own `_lines()` applied to the three shipped files, at this commit
out    report.md          total  105   comparable  97   timing-excluded 5   prov-excluded 3
       member_forces.csv  total 1289   comparable 1286  timing-excluded 0   prov-excluded 3
       utilisation.csv    total   73   comparable  70   timing-excluded 0   prov-excluded 3
cmd    the same three files under the regex this commit DELETED, (build|solve|total)
out    report.md 99, member_forces.csv 1286, utilisation.csv 70
       -- 99 is exactly the old rule's answer, which is where the published figure came from
cell   one variable moved and nothing else: the same `_PROVENANCE_PATH`, the same three files,
       the same `_lines`, the stage tuple three names versus five
out    99 -> 97 on report.md, 1286 -> 1286, 70 -> 70
cmd    what the gate's own failure message prints when it reddens, so the contradiction is
       inside the file rather than inferred
out    "report.md is not what this tree regenerates: 1 line(s) differ, shipped has 97
        comparable lines against 97"   -- from my injection of U = 0.99999
rule   BP0 -- when a decision rule changes, every figure citing the old rule is regenerated or
       withdrawn IN THE SAME COMMIT; CP2 -- a repair carries no new numeric claim outside a
       triple; and my own recorded guard that a reference is verified independently of the
       thing it measures
judge  **it does not block.** 97 against 99 is a claim about the gate's reach, not a number in
       a gate, a CSV, a report or a published deliverable: nothing asserts on it, and a reader
       of a RED is told 97 by the assertion message itself. No silently wrong result follows,
       so it is FR1's third class. **It is recorded because of what it is an instance of.**
       R853 was "a figure that is the total minus the wrong exclusion"; its repair is "a figure
       measured against the exclusion the same commit replaced". The attention went to the
       thing being fixed and the number written around the fix inherited none of the discipline
       being applied to it -- which is CP2's own sentence, and CZ0's: the highest-value finding
       in two of this project's rounds was a defect inside the repair of the previous finding.
```

**Closed when** the comparable counts in that comment are those of the rule the file actually
runs -- 97, 1286, 70 -- regenerated at the commit that publishes them (CP3), or the figure is
withdrawn and the claim left qualitative.

**R858. (DOES NOT BLOCK -- ledgered; it is the OPEN HALF of R850) THE FILE STILL ASSERTS THAT
BOTH EXCLUDED CLASSES "ARE CHECKED SEPARATELY", AND NOTHING IN THE TREE READS A PUBLISHED
WALL-CLOCK VALUE. The repair made that sentence LESS true, not more: the exclusion went from
three tolerated rows to five.**

```
claim  the file's own declared discipline is false for one of its two excluded classes
cmd    the header comment of tests/regression/test_r1_example_regenerates.py, first paragraph
out    "TWO DECLARED CLASSES OF LINE ARE EXCLUDED FROM THE BYTE COMPARISON, AND BOTH ARE
        CHECKED SEPARATELY. An excluded line is a line nothing checks unless something else
        checks it."
cell   my injections against the real gate's five test functions, the fresh side held fixed at
       my own 68.82 s regeneration, one edit each
out    CONTROL unmodified                                11 passed,  0 failed
       | load | 0.00 |       -> | load | 999.99 |        11 passed,  0 failed   <- GREEN
       | code_check | 0.00 | -> | code_check | 999.99 |  11 passed,  0 failed   <- GREEN
       -- before this commit both of these were COMPARED. The repair is right and the
          sentence describing it is now wrong about five rows instead of three.
cmd    whether anything anywhere reads a published wall-clock value
out    nothing. The provenance class has `test_R845_the_PROVENANCE_values_agree_by_BASENAME`
       and, since this commit, `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE`. The
       wall-clock class has no counterpart, by design and correctly -- I proposed the sum
       identity against myself in verdict 10 and withdrew it, and the commit records that
       withdrawal in the same comment, which is the right thing to have written down.
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; and the closing
       condition of R850, which named this site
judge  **it does not block**: a wall-clock second is not a number anyone sizes steel against,
       and FR1's third class covers the sentence. It carries because R850's closing condition
       named two things and one of them was done. The repair I asked for is five words -- the
       wall-clock VALUES are excluded and unchecked -- plus the observation that the pin and
       `test_R845_the_CSVs_carry_NO_excluded_timing_row` bound WHERE they may appear rather
       than WHAT they say. That is the honest description of a structure that is, in fact,
       honest, and I measured its bound in both directions.
```

**Closed when** that paragraph says of the wall-clock class what the two green rows above say,
and the commit message's "BOTH are checked elsewhere rather than merely dropped" is corrected
with it.

**R859. (DOES NOT BLOCK -- ledgered) THE NEW COMMENT NAMES THE WRONG ASSERTION. It says a sixth
stage row "reddens HERE rather than being absorbed", where HERE is the key-set pin. It reddens
the byte comparison; the pin stays green. The pin catches a DUPLICATE of a named stage and a
MISSING one -- which it does, and that is the stronger property.**

```
claim  the mechanism sentence attached to the repair is not the mechanism
cmd    the comment above the pin's `assert stages == sorted(_TIMING_STAGES)`
out    "ALL FIVE STAGES `cli.py` WRITES (R850), so a sixth reddens here rather than being
        absorbed, and so `load` and `code_check` stop sitting inside the byte comparison"
cell   one injection at a time into the shipped report, every other input held
out    | mesh | 3.00 | added                     10 passed, 1 failed
         FAILED REGENERATES[report.md]: "16 line(s) differ, shipped has 98 comparable lines
         against 97"                            -- the COMPARISON, and the pin is GREEN
       | total | 1.2e3 | added                   10 passed, 1 failed
         FAILED REGENERATES[report.md]          -- scientific notation is unmatched by the
                                                   digit-and-dot class, so it is compared,
                                                   which is the safe direction
       a DUPLICATE | total | 1234.00 | row       10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', [... 'total', 'total'])   <- THE PIN
       the | code_check | row DELETED            10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', ['build','load','solve','total'])
       | total | 5.00 | added to utilisation.csv 10 passed, 1 failed
         FAILED CSVs_NO_timing_row: "shipped utilisation.csv carries a timing row"
rule   BG0 -- a causal sentence carries the cell that isolates it; CW0; and my own recorded
       guard that a gate carries its own failure, asked of each of the five functions
judge  **it does not block** -- no number moves, and every one of those injections is red
       somewhere, so the gate is sound and only its description is wrong. The same error is in
       the report I was given ("a | mesh | row added -- a SIXTH row reddens the pin"), and the
       pre-existing docstring of that test has the same shape ("a fourth non-deterministic
       line ... reddens here"). **What the measurement shows is better than the claim**: a
       stage row can only be swallowed if it is one of exactly five names, in report.md,
       exactly once each -- a duplicate reddens the pin, a missing one reddens the pin, a sixth
       name reddens the comparison, and one in a CSV reddens the CSV test. That is the answer
       to "is the exclusion now too wide": **five tolerated rows, in one file, pinned by name
       and by count -- and the | mesh | case was not what bounded it.**
```

**Closed when** those two comments say which assertion fires for which class of intrusion, or
say nothing and let the five test functions speak.

**R860. (DOES NOT BLOCK -- ledgered, and it is the one of the five that step 3 is about to walk
into) `_TIMING_STAGES` IS A HAND COPY OF THE LITERAL TUPLE AT `floatfea/cli.py:297`, AND NOTHING
COMPARES THEM. R850 WAS THAT DRIFT. The repair removes the drift between the regex and the pin
and leaves the drift that caused it.**

```
claim  the repaired gate restates the generator's stage set in a second place instead of
       reading it from the one place it is defined
cmd    grep -rn "_TIMING_STAGES" --include=*.py .
out    tests/regression/test_r1_example_regenerates.py -- three hits: the tuple, the regex and
       the pin. All in the test file; nothing reads cli.py and nothing asserts equality.
cmd    the generator's own definition
out    floatfea/cli.py:297   for stage in ("build", "load", "solve", "code_check", "total"):
       -- a literal inside a function body; grep for a module-level STAGE constant in
          floatfea/ returns nothing
cmd    the sentence this leaves unchecked, which is a claim about the code in a comment
out    "floatfea/cli.py:297 writes build, load, solve, code_check, total."
       -- true today; nothing in the tree would notice it becoming false
cmd    whether the pin's new strictness can fail false instead, which is the direction that
       worried me more -- the generator guards its own loop with `if stage in result.timings`,
       so it contemplates a missing stage
out    floatfea/run/pipeline.py:605, 653, 664, 669, 672 -- all five assignments are
       unconditional on any run that returns a RunResult, and `_utilisations` is called
       unconditionally just above the code_check stamp. **So requiring all five rows cannot
       fail false on an admissible config today**, and I measured that rather than inferring it
       from the defensive guard.
rule   my own recorded guard -- provenance, not existence: that a value reaches the assertion
       through the thing that defines it is asserted structurally, not inferred from a passing
       test; EK2 -- a guard that fails false is fixed, and this is that fix one level up
judge  **it does not block.** The failure mode is a FALSE RED, which is loud, and the five
       names agree today -- CI's ladder 6 went 222 -> 225 collected with 0 failed, so the
       repair is green on a machine neither of us controls. **It carries because step 3 is the
       commit that makes it live.** FL2 adds `required_section` and `truss_sizing` to
       `floatfea run` with FM0's re-solve LOOP; a sizing loop that times itself adds a sixth
       stage to `result.timings` and a sixth row to that table, and the next sub-10-ms
       two-decimal row inside the byte comparison is R850 verbatim, in the step whose own gate
       is the thing that adds it. Two cheap closes, neither of them new apparatus: `cli.py`
       names the tuple as a module constant and the test imports it, or the pin asserts the
       gate's set against the generator's. The first also turns that comment sentence into a
       fact the tree holds.
```

**Closed when** the stage set reaches the regex and the pin from the one place the generator
defines it, or an assertion in the existing file compares the two sets.

**R861. (DOES NOT BLOCK -- it is a CORRECTION TO MY OWN VERDICT 10, and the implementer has
already relayed the wrong number) THE BASELINE OF NINE REDS WAS WRONG WITHIN ONE COMMIT OF MY
WRITING IT. The tree is at 78, and VERDICT 10 IS THE CAUSE: two of the report guards are
parametrised over the NEWEST VERDICT's findings and sites, so the baseline is a function of what
I write, not of what the implementer commits.**

```
claim  the number I told the implementer to trace against is not a constant
cmd    python -m pytest -q --tb=no -rf        (mine, at e6a20e3, tree clean)
out    78 failed, 3547 passed, 1 skipped in 966.33s (0:16:06)
cmd    verdict 10's own instruction, in this file below
out    "for the rest of step 3 the baseline is nine reds, every interim check traces against
        it one id at a time, and a tenth red is CZ1 (iv) unchanged"
cell   collection counted per file at both commits, in a worktree at e818375, nothing else
       moved
out    tests/regression/test_r1_example_regenerates.py     8 -> 11   (+3, the new test)
       tests/test_collected_set_golden.py                 77 -> 78   (+1, see below)
       tests/test_report_carried.py                      304 -> 221  (-83)
       tests/test_report_guard_states.py                  23 -> 23
       whole suite                                      3705 -> 3626  (-79, fully attributed)
       -- the -83 is `test_every_named_site_is_touched_or_declared` and
          `test_the_report_carries_the_finding`, parametrised over the newest verdict's sites
          and findings. Verdict 9 named a larger set and step 2's third revision ANSWERED it;
          verdict 10 names 12 findings and 51 sites and no report answers it, so 63 cases went
          from green to red while the parametrisation itself shrank.
cmd    the +1, so the delta is attributed and not rounded off
out    tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists gains the
       citation of `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the new helper's
       docstring, and it PASSES -- the "every citation resolves" guard working on this commit's
       own prose
cmd    the control that says nothing outside the two report-guard files is red
out    python -m pytest -q --tb=no tests/test_report_carried.py tests/test_report_guard_states.py
       78 failed, 165 passed, 1 skipped in 162.59s
       -- 78 in the whole suite and 78 in those two files is the same 78, so the other 3382
          collected cases are green. That is the statement that protects the trace, and it is a
          predicate rather than a count.
rule   EG3(i) -- every red traces BY NAME or it is CZ1 (iv) unchanged; EH1 -- the cascade is
       identified by the baseline being red and by each cascading state's own failure line; and
       C89's recorded lesson, that a tree red by design is a tree in which the next real red is
       harder to see
judge  **it does not block, and it is mine rather than the implementer's.** The operative
       correction, because the implementer will otherwise apply the wrong rule next commit:
       **"a tenth red is CZ1 (iv)" is WITHDRAWN.** The test is not a number. It is: every red
       is in `tests/test_report_carried.py` or `tests/test_report_guard_states.py`, and each
       either names a finding or a site of the newest verdict, or is a
       `test_the_guard_survives_the_state` case whose own inner FAILED list names those. A red
       that fails that predicate is CZ1 (iv) whether it is the tenth or the seventy-ninth.
       **And the count will move again at every verdict I write, including this one, because I
       am its input** -- which is the part worth keeping: a baseline whose value depends on the
       reviewer's own output cannot be handed to the implementer as a number.
```

**Closed when** nothing: it is a correction to a verdict, recorded so that the next commit
traces against the predicate rather than against nine.

## CI at the reviewed commit: RED, 78 reds, ALL 78 traced to EG3 state (2)

```
cmd    gh run list --commit e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
         --json conclusion,status,databaseId,workflowName
out    [{"conclusion":"failure","databaseId":39173178232,"status":"completed",
         "workflowName":"CI"}]
       -- the run was IN PROGRESS when I began and I waited six polls for it. An unfinished
          run is not a pass and I did not record one.
cmd    gh run view 39173178232 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  225 collected, 0 failed  (222 at e818375, so the THREE new cases ran and
                                             passed on a Linux runner) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 164.24s) / guards and meta-tests FAILURE
         (78 failed, 1050 passed, 1 skipped in 693.69s)
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39173178232 --log-failed, the unique ids, matched against state (2)'s list
out    51  test_every_named_site_is_touched_or_declared[R850..R856-<site>]   -> EG3 state (2)
       12  test_the_report_carries_the_finding[R845..R856]                   -> EG3 state (2)
        1  test_the_CI_section_is_about_the_REVIEWED_commit                  -> EG3 state (2)
        1  test_the_Carried_table_is_what_the_generator_produces             -> EG3 state (2)
        1  test_the_generator_would_catch_a_row_under_the_wrong_number       -> EG3 state (2)
        1  test_the_report_carries_a_WHOLE_SUITE_count                       -> FC1
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                    -> FC1
       10  test_the_guard_survives_the_state[baseline + 9]                   -> the cascade
       --- 51 + 12 + 1 + 1 + 1 + 1 + 1 + 10 = 78 exactly, with no remainder
cmd    the cascade identified by its own failure lines rather than by its names (EH1)
out    each inner run reads "66 failed, 154 passed, 1 skipped in 4.1-4.5s" and names
       test_the_report_carries_the_finding[R845] first; one reads 67 failed. The [baseline]
       state is red, which is EH1's other half.
cmd    the two state-(2) names that did NOT fire, so the enumeration is measured rather than
       assumed (R835)
out    test_the_answered_verdict_is_the_NEWEST_one                PASSED
       test_a_carried_row_points_at_a_section_that_discusses_it   all PASSED
       -- the enumeration over-lists here, for the ninth time
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with EH1, EJ2 and FC1 -- state (2) is the
       verdict-written-report-not-yet boundary and it is designed; EG3(i) -- the waiver is
       conditional on the trace and the trace is pasted
judge  **all 78 trace, and the waiver applies in full: CZ0 (d) does not stand and CA2's HOLD is
       not reached.** I measured that rather than classifying it, and the control that makes it
       a measurement is the one in R861: the whole suite's 78 and the two report-guard files'
       78 are the same 78, so no red sits outside the boundary set. Every step in the lint job
       RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to
       see, and mypy is green there, so the CI-only types-PyYAML red FP1 found has stayed
       fixed. **The judged commit had a run because it was pushed first (FP1).**
```

**Not CK2's exhausted-allowance state, and the usual discriminator does not work here.**
`runnerName` is null in this repository's API output for ALL FOUR jobs including the one that
SUCCEEDED, so an empty runner name cannot separate the states on this project and I did not use
it. What separates them: both real jobs carry per-step conclusions, real counts and fifteen-
and ten-minute durations (22:39:22Z -> 22:54:19Z, 22:39:23Z -> 22:49:04Z), and the two skipped
jobs are the determinism workflow's own event gate (CK0) with empty step lists at a zero-second
duration -- which arises from a designed `if:` and not from an unstarted runner.

## Try to break it -- what I ran, and what it found

* **Two full regenerations of all three deliverables from this tree into temporary
  directories**, with the fixture's own recipe: 68.82 s and 70.55 s, `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)` both times, and **0 differing
  comparable lines in all three files** at 97 / 1286 / 70. That is the control for everything
  below and the fifth and sixth independent machine states for the wall clock.
* **Eighteen injections against the five real test functions**, fresh side held fixed, one edit
  each, with the gate's `PUBLISHED` root redirected to a copy so the committed artifacts were
  never touched: baseline; a sixth `| mesh |` row; `| load |` and `| code_check |` at `999.99`;
  a duplicated `| total |` row carrying an engineering-sized number; a deleted `| code_check |`
  row; a timing-shaped row in a CSV; `| total | 1.2e3 |`; duplicate `# deck:` lines with a
  DIFFERENT basename in all three files; duplicate `# deck:` lines with the SAME basename in
  two (my own verdict-10 green, now red); the same duplicate on the FRESH side only; `# Deck:`
  with a capital; `#deck:` with no space; and the governing `U` control. **Every one of the five
  test functions was shown to carry its own failure by at least one red, and every injection
  was red somewhere except the two rows the exclusion now tolerates by design.**
* **Both EH4 directions on the thing I was asked to attack.** The weakening direction: the
  exclusion is two rows wider than it was and no check reads a tolerated value (R858). The
  strengthening direction: the pin now requires EXACTLY five rows, so a duplicate or a missing
  one reddens it -- and I checked that this new strictness cannot fail false by reading
  `pipeline.py` rather than trusting the generator's defensive `if stage in result.timings`.
* **The comparable-line counts recomputed under both rules**, which is what found R857, and the
  per-file collection delta recomputed in a worktree at `e818375`, which is what found R861 and
  attributed all 79 of it.
* **The 78 reds one id at a time**, with each cascading state's inner FAILED list read rather
  than inferred from its name, and the two enumerated state-(2) names that do NOT fire named.

**What I did not find, and it is the larger part.** The R851 repair closes my own injection
exactly, in all three files, on both sides, with precisely one new case firing -- and two
evasions I invented afterwards are caught as well, by two different tests. The R850 repair
removes a real machine-dependent false red, derives the regex and the pin from one tuple, and
**declines the tolerance I offered it**, recording the refusal in the comment so that a later
reader does not re-propose it; that paragraph is the best thing in the diff. `ruff`, `black`,
`mypy`, 186 unit tests and all six ladder rungs are green, locally and in CI, and the three new
cases ran and passed on a Linux runner. Nothing in `floatfea/` moved and no deliverable moved.
**All five of my findings are in a figure, a sentence or a structural provenance -- not one of
them is a number in a gate.**

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after I wrote this file.** Neither exception opens: this diff touches no part
of F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a published-artifact comparison. The last corpus commit
remains `ba1527e` (batch 47).

**I ran the recorded substitute, and both halves paid:**

* **A regeneration check on a published deliverable, in both directions** -- two independent
  full regenerations of all three R1 artifacts, diffed line for line, then eighteen injections
  against the gate that guards them. It produced **R857, R858 and R859**.
* **A continuum grid over the parameter space a decision rule guards** -- the exclusion's own
  space this time: the stage-name axis (three names, five names, a sixth name, a duplicate, a
  deletion), the value axis (`0.00`, `0.01`, `999.99`, `1234.00`, `1.2e3`), the file axis (all
  three artifacts), and the provenance axis (basename, directory, duplicate, capital, no space,
  fresh side). It produced **R860**, from the one axis the diff did not vary: WHERE the stage
  set comes from.

**This is the sixth consecutive round in which the regeneration check's weakening direction
produced the round's findings.**

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance|slack"
out    "tolerance because the rows are two-decimal, and that is a threshold this gate has no
        business introducing. The reviewer proposed it against itself and withdrew it; I am
        recording that so the next reader does not re-propose it."
       -- a comment RECORDING A DECLINED threshold. No value is introduced.
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves, and the one threshold this step invited was declined by the implementer
       after I declined to ask for it. **EU1 does not attach** -- no value and no declared
       counter moves -- and I ran the adversarial configuration anyway, eighteen injections and
       two full model runs, because R694's lesson is that a value which does not move is the
       worst case and not the safest.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line).** Step 3 remains open with all three reviewed revisions available. Nothing blocks, so
FR3's instruction stands and it is the only thing that matters this week: **build the rest of
FL2.**

1. **FL2, complete, before step 3's first reviewed revision (FR3).** Five items, none built:
   member topology from the config with the star as the default; `required_section` and
   `truss_sizing` in `floatfea run` with FM0's re-solve loop; the optional analyses off by
   default; headings as a list with the BEM refusal; the band check per case. The commit says
   so and claims none of it, which is correct. **This is the second commit of step 3 and both
   have been spent on ledgered gate items.** The locked plan routes those to the ledger by
   name, and FR0's date is 5 November.
2. **R860 before FL2 lands, not after.** It is the one of my five that FL2 itself makes live: a
   sizing loop that times itself puts a sixth sub-10-ms row in that table, and the hand copy of
   the stage tuple will not know. One import or one assertion.
3. **R849 with R854, over TWO files, still answered WHILE step 3 is built.** Two new
   deliverables are coming and both constants are hard-coded three-name tuples.
4. **R857, R858, R859 in the first reviewed revision**, with every figure regenerated at that
   commit (CP3) -- 97 rather than 99, the wall-clock sentence corrected, the mechanism sentences
   naming the assertion that actually fires. R847 and R848 unchanged; R850 is half paid, and
   R851 and R853 are paid.
5. **R852 and R856 remain with Xabier**, relayed correctly and verbatim this turn. Neither is
   the implementer's to repair in code.
6. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855, third
   occurrence), **against the PREDICATE in R861 and not against nine.** Every red in
   `tests/test_report_carried.py` or `tests/test_report_guard_states.py` naming a finding or a
   site of the newest verdict, or a `survives_the_state` case whose inner list names those;
   anything else is CZ1 (iv).
7. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 78
   reds matching mine id for id, and the three new cases green inside ladder 6 on a machine
   neither of us controls. I waited for the run rather than recording an unfinished one.
8. **The schedule.** FR0's 5 November stands. Step 3 opened on 18 October; two commits in, FL2
   is unbuilt by design under FR3, and nothing has slipped against a date yet. **I am not
   re-opening the escalation FR0 answered, and I am recording one number rather than a warning:
   five items, eighteen days, two commits spent on the ledger.** The next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right.** It repaired a guard of its own that failed false, in the one way
EK2 permits -- by naming the real set rather than by giving the comparison slack -- and it wrote
down the tolerance it declined so that the next reader cannot re-propose it. It found the
dict-collapse in `_provenance` by reading the code I pointed at rather than taking my word,
extended the new check to all three artifacts and to both sides, and recorded the wrong figure
it was replacing instead of quietly substituting the right one. It accepted the two greens I had
reasoned were unreachable and did not pad the diff with them. **And it asked for its own
classification to be checked, which is how R861 got found: I went looking for the baseline I had
given it, and the baseline was wrong.**

---

<!-- EARLIER ROUNDS, VERBATIM. Hand-appended in the form
     scripts/write_verdict.py uses, under DX2: each round is added and no prior
     round is rewritten or removed. The tool refused this step (R856). -->

# Review — R1 step 3
Reviewed commit: e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
**Reviewed commit: `e818375beb4198f853d5c6427b0ea2c7bbbfe8c6`.**
Verdict: PASS
Tests: 3695 passed, 9 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK.** No report revision exists for step 3, so this counts against
no round and all three reviewed revisions remain available. **Nothing blocks.** Both
blocking items step 2 carried are ANSWERED, measured by me rather than read; six findings
are ledgered and one is an apparatus item that FF0 routes to the next commit.

**I RULED UNDER FR1 WITH EZ0** (`docs/directives/FR.md:14-26`, `CLAUDE.md` section "What
blocks for the rest of R1"). No finding below can cause a silently wrong result, and I say
so for each rather than leaving the classification implicit. **This file is HAND-WRITTEN
because the one sanctioned path in refuses it -- R856.**

```
cmd    git diff --stat e93becf..HEAD
out    tests/regression/test_r1_example_regenerates.py  | 201 +
       tests/regression/test_r1_published_artifacts.py  |  16 +
       -- two files, both tests, nothing else
cmd    git diff --stat e93becf..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers:` header to compare. The newest revision in the tree is step 2's
third, `Answers: verdict 8 @ a7b2f62` (`docs/reports/R1/step-2.md:1302`), and verdict 9 is
newer -- which is EG3 state (2) by definition and is designed, not a defect.
`test_the_guard_reads_the_step_being_worked_on` is **green** in my run, which says
mechanically that state (1) is not in play.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R845** (not one number in the three published R1 deliverables is compared against anything) | **ANSWERED IN CODE, and I verified the repair by my own regeneration rather than by reading its counter-cases. The REPORT half of the condition is owed, correctly, at step 3's first reviewed revision.** | `tests/regression/test_r1_example_regenerates.py`, 8 cases. I ran `floatfea run` on the shipped example into a temp directory with the fixture's own recipe (68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`) and compared every line: **report.md 99 comparable lines, 0 differing; member_forces.csv 1286, 0 differing; utilisation.csv 70, 0 differing.** Then I injected: the governing `**U = 1.71167 -> 0.99999` reddens `REGENERATES[report.md]`; the **last digit of member_forces.csv line 701** and of **utilisation.csv line 60** each redden their own file's case, so the comparison reaches the middle of a 1289-line CSV and not only row 1. The condition asked for the wall clock excluded BY NAME rather than by tolerance, and it is a regex over stage names. **Closed in code.** Owed: the report pasting both directions, every figure regenerated at the report's own commit (CP3) -- three of the figures the new file already publishes are wrong, see R853. |
| **R846** (the R838 repair is green on three injections one step above the one it was built for) | **ANSWERED, and I reproduced all three injections and the restore** | `tests/regression/test_r1_published_artifacts.py:112-117` (nine distinct non-blank), `:139` (`LABEL.strip()`), `:171` (`caveat.strip()`). My own harness, 31 cases over the three artifacts: baseline **31 passed**; caveat 8 = a duplicate of caveat 4 -> **1 failed** (`NINE_caveats`, naming `9 entries and 8 distinct non-blank ones`); caveat 8 = `""` -> **4 failed** (three membership cases by file, plus the count); `LABEL = ""` -> **3 failed**, one per artifact; restored -> **31 passed**. The three doors verdict 9 measured open are shut. **The next injection up is still green -- R852 -- and it is not the implementer's to fix.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- ledgered, and there is no report revision in which it could be answered** | FR1's third class. It is C43 on the closure list. |
| **R848** (the empty-directory refusal admits `.`, `./`, `..`, `" . "`) | **still open, untouched by this diff, and correctly so** | `git diff e93becf..HEAD -- floatfea` is empty. Non-blocking, same class as R843, ruled twice. |
| **R849** (the caveat, disclaimer and provenance gates quantify over a hard-coded three-file tuple, and step 3 publishes two more files) | **still open, and it now has a SECOND site -- R854** | `ARTIFACTS` at `tests/regression/test_r1_published_artifacts.py:69` and now `NAMES` at `tests/regression/test_r1_example_regenerates.py:48`. Verdict 9 said R849 is answered WHILE step 3 is built; that is unchanged, and the condition now names two files. |
| **R835** (EG3's enumeration) | **still open, still Xabier's; this commit is its eighth measurement** | of state (2)'s enumerated names, **two fire and the rest are green**, and both that fire do so for FC1's reason. It over-lists here as it under-listed at EH1, FN2 and EJ2. Relayed unchanged. |
| **R836** | **recorded, no change in this diff** | unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, on a machine neither of us controls** | CI run 39169784204, job `lint, unit and guards`, read at step level: `actionlint` SUCCESS, `ruff` SUCCESS (`All checks passed!`), `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 67.62s`). Every one RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired in this verdict; repaired by the rounds that touch the files. |
| **C43, C44, C45** | **C43 and C44 carry; C45's ROUTING WAS MINE AND IT WAS WRONG** | verdict 9 ledgered C45. **FF0 says a closure item in the gating apparatus is NOT ledgered** -- `scripts/ci_section.py` reads the gating record -- so C45 belonged in the next commit, not on the list. I am correcting my own routing. See the process note: it cannot in fact be fixed before step 3's report exists, and that is the thing worth recording rather than the misfiling. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed, and now STRUCTURALLY UNPAYABLE until step 3's report exists** | see the process note. Not a finding against the implementer. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files: **9 failed, 320 passed, 1 skipped**, the same nine ids as verdict 9's and the same nine as CI's, traced one at a time under R855. |

## Findings

**NOTHING BLOCKS.** The diff is two test files, no `floatfea/` change, no tolerance, and the
three published deliverables are byte-unchanged -- which I established by regenerating them,
not by reading the diff. Both carried blocking items are answered at the layer they were
about. The seven findings below are the weakening directions I could still reach, and under
FR1 none of them can put a wrong number in front of anyone; I say which, for each.

**The implementer asked for the EXCLUSION to be attacked, and that is where four of the
seven are.** Two classes of line are dropped from the byte comparison and the commit message
claims "**BOTH are checked elsewhere rather than merely dropped**". For the provenance class
that is true in part and I measured its reach. **For the wall-clock class it is false:
nothing in the tree reads any published wall-clock value.**

**R850. (DOES NOT BLOCK -- ledgered) THE WALL-CLOCK EXCLUSION COVERS THREE OF THE FIVE ROWS
THE GENERATOR WRITES, SO TWO WALL-CLOCK ROWS SIT INSIDE A BYTE COMPARISON -- and in the other
direction no check anywhere reads a published wall-clock VALUE: `| total | 97.27 |` edited to
`| total | 999.99 |` and `| solve | 97.08 |` edited to `| solve | 0.01 |` are both green on
all 8 cases.**

```
claim  the exclusion's declared class and the generator's actual output are not the same set
cmd    floatfea/cli.py:296-299, the row loop
out    for stage in ("build", "load", "solve", "code_check", "total"):
           lines.append(f"| {stage} | {result.timings[stage]:.2f} |")
       -- FIVE stages, every one a time.perf_counter() delta (floatfea/run/pipeline.py:605,
          653, 664, 669, 672)
cmd    the exclusion regex, tests/regression/test_r1_example_regenerates.py:56
out    r"^\|\s*(build|solve|total)\s*\|\s*[0-9.]+\s*\|\s*$"       -- THREE
cmd    the file's own declared class, :54-55
out    "the report carries a `| stage | seconds |` table whose THREE rows cannot agree
        between two runs"
cell   my own injections against the real gate's four test functions, one edit each, the
       fresh side held fixed at my own 68.95 s run of the shipped example
out    CONTROL unmodified                        8 passed, 0 failed
       | total | 97.27 | -> | 999.99 |           8 passed, 0 failed   <- GREEN
       | solve | 97.08 | -> | 0.01 |             8 passed, 0 failed   <- GREEN
       | load | 0.00 | -> | 0.01 |               7 passed, 1 failed   <- COMPARED
       | code_check | 0.00 | -> | 0.01 |         7 passed, 1 failed   <- COMPARED
cell   the margin on the two compared rows, solved rather than sampled: the printed row
       flips at 5 ms, and the load stage is np.load + exported_froude_lambda + the period
       check
out    first pass 1.6 ms, then 0.7 ms (12.8 MB npz, lazy open)  -> margin 3.1x on the
       coldest sample I could take
cmd    the same two rows on a Linux runner with a different filesystem
out    ladder 6 (empty:tests/verification/rung6 full:tests/regression):
       214 collected at 8542d79 -> 222 collected here, 0 failed, 0 errored -- the 8 new
       cases RAN and passed there, so both compared rows printed 0.00 on that machine too
rule   my own recorded guard -- an excluded line is a line nothing checks unless something
       else checks it, which the file itself says at :50-51; EH4 -- the boundary is solved in
       the direction that weakens the gate
judge  **two statements in opposite directions, and neither is a silently wrong result.**
       (i) `load` and `code_check` are inside the comparison with a 3.1x margin to a FALSE
       RED. A false red is loud, so it does not block -- but the pressure a false red creates
       is to widen the exclusion, at the worst possible moment to be deciding what the
       exclusion means. (ii) No published wall-clock value is checked by anything, so the
       commit message's "both are checked elsewhere" is false for this class. That is prose
       (FR1's third class) and the number is a wall clock nobody sizes steel against, so it
       does not block either. **And I checked the obvious repair and WITHDREW it:**
       `timings["total"]` is the exact sum of the four at full precision
       (floatfea/run/pipeline.py:672), but the published rows are rounded to 2 dp, so
       `total == build + load + solve + code_check` on the PRINTED values needs up to 0.02
       of slack -- which is a tolerance, in `tolerances.py`, for a wall clock. I am not
       asking for it.
       What I would accept: the exclusion covers all five stages the generator writes, the
       pin at :172-175 lists all five, and the docstring says the wall-clock VALUES are
       excluded and unchecked instead of saying they are checked elsewhere.
```

**Closed when** the exclusion and its pin cover the same five stage names
`floatfea/cli.py:297` writes, and the two prose claims -- at
`tests/regression/test_r1_example_regenerates.py:54-55` and in the commit message -- are
corrected to what was measured.

**R851. (DOES NOT BLOCK -- ledgered) THE PROVENANCE EXCLUSION IS CHECKED BY BASENAME ONLY,
AND THE KEY-SET PIN READS `report.md` ALONE. Three injections measured green: the deck path's
DIRECTORY swapped in all three files, the `load_cases` MODE word changed, and a second
contradictory `# deck:` line inserted into a CSV.**

```
claim  the reach of the exclusion the implementer asked me to attack, solved from the side
       that weakens it (EH4)
cell   the real gate's four test functions, fresh side held fixed, one class of edit each
out    CONTROL unmodified                                            8 passed, 0 failed
       deck DIRECTORY swapped, basename kept, all three files        8 passed, 0 failed  <- GREEN
         data/platform/platform12_deck.yaml -> /home/someone-else/junk/platform12_deck.yaml
       CONTROL deck BASENAME changed, all three files                5 passed, 3 failed
         -> "the deck provenance names 'OTHER_deck.yaml' in the committed file and
             'platform12_deck.yaml' in a fresh run of this tree"   -- the basename half WORKS
       load_cases MODE word npz -> static, all three files           8 passed, 0 failed  <- GREEN
       a SECOND "# deck: /home/someone-else/junk/platform12_deck.yaml" line
         inserted into utilisation.csv                               8 passed, 0 failed  <- GREEN
       CONTROL an extra "| solve | 3.00 |" row in report.md          6 passed, 2 failed
         -> EXCLUSION pin: ('the SHIPPED report', ['build','solve','solve','total'])
       CONTROL the three provenance lines DELETED from report.md     6 passed, 2 failed
       CONTROL the three timing rows DELETED from report.md          7 passed, 1 failed
cmd    why the duplicate is invisible, read rather than guessed
out    tests/regression/test_r1_example_regenerates.py:105-112 -- _provenance returns a
         DICT keyed on config|deck|load_cases, so two lines with one key COLLAPSE and the
         last wins; :168-177 -- the pin iterates over report.md and the fresh report ONLY,
         so for the two CSVs the excluded set is pinned by nothing
rule   EH4; and my own recorded guard -- check that the collection the assertion inspects can
       contain the failure
judge  **it does not block, and I want the reason on the record rather than the ruling.** No
       number moves in any of the three. None of the three is a string this tool can emit:
       the directory component is a FUNCTION OF THE CONFIG'S OWN LOCATION
       (floatfea/run/config.py:507-523 -- anchored on source.parent, then its parent, then
       absolute), which is exactly why the exclusion exists and why the fixture's copy in a
       temp directory differs at all. So a wrong directory in a shipped artifact is reachable
       only by a hand-edit, and a hand-edited provenance path puts no wrong engineering
       number in front of anyone. Under FR1 that is not a silently wrong result, and under
       its second head nothing is accepted and used other than as declared -- the deck that
       was USED is the right one in every green row above.
       **What I would accept, if it is cheap:** the pin loop at :168 runs over all three
       files rather than over the report, which is the same loop already written; and the
       shipped path is compared by resolving it against the two anchors _relative uses
       instead of by rsplit("/", 1)[-1].
```

**Closed when** the excluded key set is pinned in all three artifacts rather than in the
report alone -- or the report states that the two CSVs' excluded set is pinned by nothing and
why that is acceptable.

**R852. (DOES NOT BLOCK -- ledgered, AND IT IS THE ONE I MOST WANT READ, because no repair the
implementer can write will close it) A CAVEAT TRUNCATED TO ITS OWN MARKER IS GREEN ON 31 OF
31 CASES. TABLE_CAVEATS[8] reduced from R743's sentence to the string "R743:" passes the new
distinct-and-non-blank count, passes all 27 membership cases, and passes after the artifacts
are regenerated. So does LABEL = "a". This is R831 returning in a new shape: R831 was "the
needle is the MARKER and the marker survives a rewording", and truncating the text to the
marker turns the needle back into a marker.**

```
claim  the repaired gate's boundary, one injection above the three it was built for
cell   floatfea.cli.TABLE_CAVEATS / LABEL rebound and the gate re-imported so it reads the
       mutated value, the three committed artifacts untouched, 31 cases (9 caveats x 3 files
       + 3 disclaimer + the count)
out    BASELINE                                              31 passed,  0 failed
       caveat 8 = DUPLICATE of caveat 4                      30 passed,  1 failed
       caveat 8 = ""                                         27 passed,  4 failed
       LABEL = ""                                            28 passed,  3 failed
       caveat 8 truncated to its first word, "R743:"         31 passed,  0 failed  <- GREEN
       caveat 8 = "C_m"                                      31 passed,  0 failed  <- GREEN
       LABEL = "a"                                           31 passed,  0 failed  <- GREEN
       RESTORED                                              31 passed,  0 failed
cmd    what the published caveat says, so the loss is stated rather than implied
out    floatfea/cli.py, TABLE_CAVEATS[8]:
       "R743: C_m MULTIPLIES the bending term in section 3.3.1's interaction, ..."
       -- the sentence that delegates the C_m DIRECTION to a published sensitivity column
cmd    whether the new R845 gate catches it instead
out    no. The regeneration gate compares the shipped files against a fresh run, so once the
       artifacts are regenerated BOTH sides carry the stub and both are green. The two gates
       compose against a stub that was never regenerated, and neither covers a regenerated
       one.
cmd    whether any record of the nine caveat TEXTS exists to compare against
out    grep -n "caveat" docs/directives/FO.md
       :20-22  "all nine caveats in the header; a test that reads the published .md and .csv
                files, not a stub. Each must redden when one caveat is removed"
       -- FO2 records the COUNT and the mechanism. It records no caveat text.
rule   my own recorded guard -- a gate carries its own failure, and "R743:" in text cannot
       fail against a file that contains R743's real caveat; EH4 -- the injection rises until
       a clean case trips
judge  **it does not block, for a reason that is not about severity.** The published outcome
       is the one verdict 9 stated for R846 -- a utilisation column whose C_m direction is a
       stub while the gate certifies nine of nine -- so by severity it IS R846. But **no
       comparison between the code and the files can detect it**, because both halves carry
       the stub; the only check that could is a comparison against an independent record of
       what the nine caveats SAY, and this repository has none. The cheap alternative is a
       minimum length or word count, which is a threshold for a sentence and belongs in
       tolerances.py if anywhere, and I am not asking for that. **So this is not the
       implementer's to repair in code.** It is a question for Xabier about FO2: if the nine
       caveats are load-bearing enough that their absence is a wrong result, their TEXTS
       belong in the directive record, and then one list comparison closes the class
       permanently. Recorded, measured and relayed -- not a round.
```

**Closed when** FO2's nine caveat texts exist in a record the gate can compare against -- or
the report states, with the three green rows above, that the caveat gate cannot distinguish a
caveat from its own marker and that this is accepted.

**R853. (DOES NOT BLOCK -- ledgered, FR1's third class) "102, 1289 AND 73 COMPARABLE LINES"
DOES NOT REPRODUCE. The comparable counts are 99, 1286 and 70. The published figures are the
report's total minus its three provenance lines, and the two CSVs' TOTAL line counts -- so the
timing exclusion was subtracted nowhere and the provenance exclusion was subtracted only for
the report.**

```
claim  the figure the new file offers as "the measurement that says the numbers are
       reproduced" (tests/regression/test_r1_example_regenerates.py:62-64)
cmd    the gate's own _lines() applied to the three shipped files and to my own fresh run
out    report.md          total 105   comparable 99    differing 0
       member_forces.csv  total 1289  comparable 1286  differing 0
       utilisation.csv    total 73    comparable 70    differing 0
cmd    where the published numbers come from
out    102 = 105 - 3   (the provenance lines only)
       1289, 73        = the TOTAL line counts, with nothing excluded
rule   BF0 with CP3 -- the figure is pasted from the run that produced the artifact and the
       paste is the last edit; BP0 -- a figure carries the rule it was measured against
judge  the substantive claim -- that nothing but the two declared classes differs -- is TRUE,
       and I verified it independently on a fourth machine state: 0 differing comparable
       lines in all three files. Only the three counts are wrong, and they are wrong in the
       direction that makes the gate sound wider than it is. FR1's third class; no number in
       a gate or a deliverable moves. **It is recorded because it is the figure the step's own
       repair is measured by**, which is exactly what R847 was two rounds ago.
```

**R854. (DOES NOT BLOCK -- ledgered; it joins R849) R849 NOW HAS A SECOND SITE. The new gate
repeats the hard-coded three-file tuple, so FR3's two further deliverables would arrive
UNCOMPARED as well as uncaveated.**

```
claim  the artifact set is fixed in the source in two files now, not one
cmd    the two constants
out    tests/regression/test_r1_published_artifacts.py:69  ARTIFACTS = (REPORT, FORCES,
                                                                        UTILISATION)
       tests/regression/test_r1_example_regenerates.py:48  NAMES = ("report.md",
                                                                    "member_forces.csv",
                                                                    "utilisation.csv")
cmd    what step 3 publishes, from the plan
out    docs/milestones/R1.md step 3 -- required_section and truss_sizing in `floatfea run`,
       both OFF in the shipped example today
rule   my own recorded guard -- check that the collection the assertion inspects can contain
       the failure
judge  not a defect today: the two outputs are off, the files do not exist, and the gate is
       green because main() writes exactly these three. Verdict 9 ruled R849 answered WHILE
       step 3 is built; the only change is that its closing condition now names two files,
       and the second is the one that compares NUMBERS. A fourth deliverable that arrives
       with no numeric comparison is R845 with a different file name, and that is the one of
       my seven findings that could later put a wrong number in front of someone.
```

**R855. (DOES NOT BLOCK -- ledgered, and it is the SECOND occurrence) THE SUITE WAS NOT RUN AT
A PUSHED, REVIEWED COMMIT, AND THE TREE'S NINE REDS WERE NOT RECORDED WITH THEIR CAUSE NAMED.
The implementer ran `tests/regression tests/unit` (408 passed) and asked whether the light
scope requires the full run. It does, and EG3(i) requires the FAILED list pasted with the
state named. I did both; nothing was hiding this time.**

```
claim  ES0's light scope is the suite, and EG3's waiver is conditional on a trace that was
       not written
cmd    python -m pytest -q --tb=no -rf        (mine, at the reviewed commit, tree clean)
out    9 failed, 3695 passed, 1 skipped in 957.64s (0:15:57)
cmd    the implementer's two figures, cross-checked against CI's own numbers rather than
       re-run
out    unit tests 186 passed + ladder 6 222 collected = 408   (this commit, run 39169784204)
       unit tests 186 passed + ladder 6 214 collected = 400   (8542d79, run 39164110433)
       -- both reported counts are exactly right, and the +8 is this gate
cmd    the nine reds, traced ONE ID AT A TIME per EG3(i), not as a family
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
         "run 39162423263: the table says no result (status in_progress), gh says failure"
                                                                      -> FC1, and C45
       test_the_report_carries_a_WHOLE_SUITE_count
         "the newest revision carries no whole-suite line ... Generate it with
          python scripts/suite_count.py"                              -> FC1
       test_the_guard_survives_the_state[baseline] and six others
         each inner run read individually: 2 failed, 301 passed, 1 skipped, and the two
         FAILED ids inside each are the two above                     -> the cascade
       test_the_guard_reads_the_step_being_worked_on                  -> PASSED
rule   ES0 -- an interim check is the suite and CI at the commit plus a CZ0 (a)-(d) scan;
       EG3(i) -- the waiver is conditional on the trace and the trace is pasted; CA2, which I
       keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD regardless of
       the local run; EH1 -- the cascade is identified by the baseline being red and by each
       cascading state's own failure line, not by its name
judge  **all nine trace, to two names rather than to a family, and the waiver applies in full
       -- so CZ0 (d) does not stand and CA2's HOLD is not reached.** I measured that rather
       than classifying it. The finding is that the record did not say so at a pushed commit,
       for the second time in three commits: verdict 8's R841 was a NINTH red that an
       eight-file subset could not contain, and the subset is the same shape of choice. It
       does not block under FR1 -- no wrong number follows, and in fact nothing was hiding --
       but a tree whose reds are not traced is the tree in which the next real one is not
       seen, and R629 is this project's own measured instance of that.
```

**Closed when** the next commit in step 3 records the whole-suite run and names the EG3 state
with its FAILED list, as every revision in step 2 did.

**R856. (DOES NOT BLOCK -- APPARATUS, and under FF0 it is NOT LEDGERED: it is fixed in the next
commit) `scripts/write_verdict.py` REFUSES TO WRITE A VERDICT FOR A STEP THAT HAS NO REPORT,
AND FR3 PLUS ES0 MAKE THAT THE NORMAL STATE OF AN INTERIM CHECK. This verdict is hand-written
because the one sanctioned path into `docs/reviews/` refused it.**

```
claim  the sanctioned path cannot write the verdict the Stop hook requires
cmd    printf the four mandatory sections with a PASS header |
         python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1
cmd    the refusal site
out    scripts/write_verdict.py:179-181
         report = root / f"docs/reports/{args.milestone}/step-{args.step}.md"
         if not report.exists(): sys.exit(f"refused: no step report at {report}")
cmd    whether the state is exceptional
out    docs/directives/FR.md:28-33 (FR3) -- "Build ALL of it before the first reviewed
       revision. Interim checks run as the hook requires and count against no round."
       CLAUDE.md (ES0) -- "a verdict the hook forces at a turn boundary mid-step, on a tree
       with NO new report revision, is an INTERIM CHECK"
rule   FF0 -- anything that reads the gating record, or decides whether a green is believed,
       is fixed in the next commit under EK2's repair-not-extend rule; and the file's own
       docstring already records the precedent: "the reviewer could not write an R1 verdict
       through the one sanctioned path in, and hand-wrote it instead"
judge  the refusal was right when every step's first reviewed artifact was its report. FR3
       inverted that: step 3's report comes after all of FL2, so every interim check in step 3
       is a verdict on a step with no report, and the only path in refuses all of them. The
       check that is wanted is "a step with no report AND no diff to judge"; here the diff is
       217 lines. **I am recording it rather than widening it** -- EK2 says a guard that fails
       false is fixed or deleted, never extended, and which of those this is, is Xabier's
       call, because it is the reviewer's own tooling and the file says so itself at :44-48.
       Until then the hand-written file IS the verdict, as it was for R1 step 1.
```

## The process note this tree is about to need, said once

**FR3 + FC1 + EK3 means the tree is RED BY TWO FOR THE WHOLE OF STEP 3, by construction, and
no file says so.** `test_the_report_carries_a_WHOLE_SUITE_count` wants a line inside the
newest report revision; `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` wants that revision's
CI table regenerated (C45). The newest revision is step 2's third, and **EK3 forbids any
commit touching a closed step report**, so neither can be written until step 3's first
revision exists -- which FR3 places after all five of FL2's items. FC1 says both are designed
and self-clearing "in the next commit"; FF0 says an apparatus item is "fixed in the next
commit". **Neither is available here, and that is neither the implementer's fault nor mine.**
The consequence is operational and I will act on it: for the rest of step 3 the baseline is
nine reds, every interim check traces against it one id at a time, and a tenth red is CZ1 (iv)
unchanged. This is C89's shape -- "a tree that is red by design is a tree in which the next
real red is harder to see" -- and it goes to Xabier with R856, because the exit is a clause
and not a commit.

## Try to break it -- what I ran, and what it found

* **A full regeneration of all three deliverables from this tree into a temp directory, with
  the fixture's own recipe.** 68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`,
  **0 differing comparable lines in all three files** (99, 1286, 70). That is the control for
  everything below, and the fourth independent machine state for the wall clock.
* **Thirteen injections against the new gate**, each run against the real test functions with
  the fresh side held fixed: the governing U; the last digit of member_forces.csv line 701;
  the last digit of utilisation.csv line 60; five wall-clock edits; three provenance edits; a
  duplicated provenance line in a CSV; an extra timing-shaped row; and two deletion controls.
  **Three classes came back green -- R850, R851 -- and each of the gate's four test functions
  was shown to carry its own failure by at least one red.**
* **Seven injections against the repaired caveat gate**, including the three verdict 9
  measured (all three redden, 1 / 4 / 3 cases, and restore) and **three one step above
  (R852)**. My first pass of that harness had a bug -- three cases ran with the unmutated
  tuple and printed `31 passed`, which would have read as the repair not working. I found it
  because `R846 b` should have reddened and did not, fixed the harness and re-ran. Recorded
  because an instrument that silently fails to inject is the shape of every finding in this
  section.
* **The boundary on the two compared wall-clock rows, solved rather than sampled:** the
  printed row flips at 5 ms, and the load stage measures 1.6 ms cold and 0.7 ms warm --
  margin 3.1x.
* **CI read at the step level, both jobs**, including the ladder's rung-6 collected count
  before and after, which is what says the new gate RAN on a machine neither of us controls
  rather than being collected and skipped.
* **The nine reds one id at a time**, with each cascading state's inner FAILED list read
  rather than inferred from its name.

**What I did not find, and it is the larger part.** R845's repair does what verdict 9 asked
and it is stronger than the condition required: it reaches the last digit of any line in any
of the three files, it is redirected so it cannot overwrite the evidence it checks, and it
arrives green on a Linux runner as well as here. R846's three doors are shut. No `floatfea/`
line moved, no tolerance moved, the three deliverables are byte-unchanged, and `ruff`,
`black`, `mypy`, 186 unit tests and all six ladder rungs are green in CI. **The exclusion --
the thing I was asked to attack -- is honest in its structure: it is declared, it is pinned
for the report, and its deletion direction is backstopped. Where it leaks, it leaks on paths
and on a wall clock, and not on one engineering number.**

## CI at the reviewed commit: RED, nine reds, ALL NINE traced to FC1's designed pair

```
cmd    gh run list --commit e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
         --json conclusion,status,databaseId
out    [{"conclusion":"failure","databaseId":39169784204,"status":"completed"}]
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The SHORT sha returns an empty list; the flag
          needs the full sha, as verdict 9 recorded.
cmd    gh run view 39169784204 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  222 collected, 0 failed  (empty:rung6 full:tests/regression; 214 at
                                             8542d79, so the 8 new cases ran and passed) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 67.62s) / guards and meta-tests FAILURE
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39169784204 --log-failed, the ids
out    identical to my own nine, id for id, and each cascading state's inner run reads
       "2 failed, 301 passed, 1 skipped" naming the two FC1 ids
rule   CA2 -- a red CI is a HOLD regardless of the local run; EG3 with FC1 -- the two
       CZ1-class names are state (2)'s and neither can pass in the commit it describes;
       EG3(i) -- EVERY red traces by name or it is CZ1 (iv) unchanged
judge  **all nine trace, and the waiver applies in full: CZ0 (d) does not stand.** Both FC1
       reds are designed and neither is clearable before step 3's report exists -- see the
       process note. Every step in the lint job RAN rather than being skipped behind an
       earlier red, which is what CZ1 (iii) exists to see, and mypy is green there, so the
       CI-only types-PyYAML red FP1 found has stayed fixed.
```

**Not CK2's exhausted-allowance state.** Both real jobs have per-step conclusions, real counts
and eight- and nine-minute durations; the two skipped jobs are the determinism workflow's own
event gate and not an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree
was clean before I wrote this file.** Neither exception opens: this diff touches no part of
F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a caveat tuple or a published-artifact comparison. The
last corpus commit remains `ba1527e` (batch 47).

**I ran the recorded substitute, and the half that paid is the one this step is about:**

* **A regeneration check on a published deliverable, taken in BOTH directions** -- all three
  R1 artifacts regenerated from this tree and diffed line for line (0 differing), then
  thirteen injections against the gate that now guards them. It produced R850, R851 and R853.
  **This is the fifth consecutive round in which the regeneration check's weakening direction
  produced the round's findings.**
* **A continuum grid over the parameter space a decision rule guards** -- the caveat gate's
  mutation space rather than the config's this time: duplicate, blank, whitespace-only,
  truncated-to-first-word, degenerate-substring, and the same five on LABEL. It produced
  **R852**, the one finding here that no code in this repository can close.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- floatfea tests scripts | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"
out    (no match)
cmd    the same, widened to any literal comparison the diff adds
out    93:+   assert main(["run", str(cfg)]) == 0        -- an exit code
       210:+  assert len({c.strip() for c in TABLE_CAVEATS if c.strip()}) == 9
       -- FO2's own declared count, annotated at :204-209; ruled a declared quantity and not
          a threshold at verdict 9, and that ruling is unchanged by the new form
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves. **EU1 does not attach** -- no value and no declared counter moves --
       and I ran adversarial configurations anyway, twenty of them, because R694's lesson is
       that a value which does not move is the worst case and not the safest. And I declined
       to ask for the one new threshold this step invited: a slack on the published
       wall-clock sum (R850).
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1).** Step 3
remains open with all three reviewed revisions available. Nothing blocks, so FR3's instruction
stands: build the rest of FL2.

1. **FL2, complete, before step 3's first reviewed revision (FR3):** member topology from the
   config with the star as the default; `required_section` and `truss_sizing` in `floatfea
   run` with FM0's re-solve loop; headings as a list with the BEM refusal; the period-band
   check. None of it is in this commit, as the commit says.
2. **R849 with R854 -- answered WHILE step 3 is built, over TWO files now.** The caveat,
   disclaimer, provenance AND regeneration gates are written over the artifact set the config
   declares, not over two hard-coded three-name tuples. A fifth deliverable arriving with no
   numeric comparison is R845 with a different file name.
3. **R850's two prose corrections and the five-stage exclusion**, R851's pin over three files,
   R853's three counts -- all in the first reviewed revision, with every figure regenerated at
   that commit (CP3). R847 and R848 unchanged.
4. **R852 and R856 go to Xabier, not into a round.** R852 needs FO2's caveat texts recorded
   before any gate can see the defect; R856 needs a clause about the reviewer's own tooling.
   Both are relayed with their measurements and neither is the implementer's to repair in code.
5. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855),
   against a baseline of nine, with a tenth red treated as CZ1 (iv).
6. **The push (FP1) continued.** It gave this round a completed CI run at the judged commit,
   nine reds matching mine id for id, and the new gate's 8 cases green inside the ladder's
   rung 6 on a machine neither of us controls. I waited for the run rather than recording an
   unfinished one.
7. **The schedule.** FR0's 5 November is the target. Step 3 opened on 18 October carrying two
   blocking items, both answered in its first commit, with FL2 unbuilt by design. Nothing has
   slipped and I am not re-opening the escalation FR0 answered; the next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right, and it is much the larger part.** Two blocking items were
answered first, at the layer each was about, in one commit, with counter-cases in both EH4
directions and a redirected fixture so the gate cannot overwrite its own evidence. The
implementer reproduced my R845 finding independently instead of taking it, flagged the one
lint choice that reads like an omission (`strict=False`, and the reasoning is right -- the
length mismatch is reported with both counts, which I confirmed by injecting one), and found
the provenance exclusion by RUNNING the gate rather than by anticipating it, which is the only
way that class is ever found. **Every one of my seven findings is in the reach of a check, not
in a number: nothing in `floatfea/` moved, no deliverable moved, and the gate that now guards
them reaches the last digit of every line in all three files.**
