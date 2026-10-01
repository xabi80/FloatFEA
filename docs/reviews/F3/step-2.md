# Review — F3 step 2
Reviewed commit: 5a2ff21b7ba611f453716bc987ba58ba113c01c3
Verdict: PASS
Judged commit: b105de1b8efb976d5c225aaee7426ea2a095794d  (HEAD of F3 and pushed; the stamp above is HEAD at write time, which is corpus batch 30 at 5a2ff21 -- the tool records that limitation in its own docstring)
Tests: 2939 passed, 1 failed, 0 skipped   (my own run, ONE invocation, clean tree, no exclusion, 619.12s -- not the report's 2650 and not its excluded-set split)

## Round of 2026-10-01 -- EIGHTY-THIRD verdict, ROUND 3 OF 3 ON STEP 2. THE STEP CLOSES AND FOUR ITEMS CARRY.

**This is the third verdict in this file and the cap closes the step (CZ0, DK0).** I write PASS because that is what the third round does, not because the tree is clean. **It is not clean: one test is red at the judged commit, on my machine and on CI, and it is NOT the step-boundary class two verdicts have been ruling it as.** Were a round left I would HOLD on it. The cap says the item carries by name and stays blocking, and CZ1(iv) says a closure commit is not finished until a pushed run is green -- between them the red has the teeth a HOLD would give it, one round cheaper.

**WHAT THE WORK OF THE ROUND IS WORTH, FIRST, BECAUSE IT IS GOOD.** `test_the_REFUSAL_rejects_a_SUNK_seventh_mode` is the best cell this step has produced and I could not break it. The edge it hardcodes reproduces on my machine to seven figures; both sides reproduce exactly; the shape leaves the other two clauses satisfied and asserts that it does; the two assertions bracket the decision quantity, so a moved edge reddens one of them rather than degrading into a pass; and it needs no separate negative control, because with the seventh clause removed nothing raises and the `pytest.raises` fails. That is four recorded guards satisfied in nine lines.

**AND THE ADVERSARIAL ROUND FOUND THE ACCUSATION AGAINST THE LOCKED PLAN TO BE FALSE.** I bisected the three counter edges myself, per member. The plan is RIGHT to the digit; the three figures published in the test file and in the report are the BEST of the sixteen members. C89 is withdrawn and R630 replaces it, pointing the other way.

## THE TREE AT b105de1, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    b105de1b8efb976d5c225aaee7426ea2a095794d   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 86e161b..HEAD --name-only
out    8ed0fd4  floatfea/tolerances.py
out             tests/verification/rung3/test_platform_rigid_modes.py
out    b105de1  docs/reports/F3/step-2.md and step-2-answers.json
judge  TWO COMMITS, one path class each, and the report is separate from the code
       it reports. Neither touches the verdict tree, .claude/, docs/SUPERVISOR.md
       or CLAUDE.md, so there is NO STOP-class process finding this round.
cmd    git diff 86e161b..HEAD --stat -- floatfea tests docs scripts
out    tolerances.py 26 +, the rung-3 gate 54 +, the report 572 +, answers.json
cmd    python -m pytest -q
out    1 failed, 2939 passed, 2 warnings in 619.12s (0:10:19)
out    FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state
out            [guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF]
cmd    python -m pytest tests/verification/rung3/test_platform_rigid_modes.py -q -s
out    12 passed in 1.02s, and every printed figure is in R626 below
cmd    the two Answers headers in the report, and the one the guards read
out    line 3    Answers: verdict 80 at 7e5f3fb    revision 1, left as the record
out    line 734  Answers: verdict 82 at 86e161b    revision 2, the NEWEST
out    tests/test_report_carried.py:257-264 reads the header of the NEWEST
out    revision, so that is the live one
cmd    the newest verdict commit
out    86e161b  the EIGHTY-SECOND verdict
judge  ITEM 1b PASSES. The newest revision names verdict 82 by verdict 82's own
       commit (DX2). One comparison; it passes; R628 is answered and the whole
       report-guard family it was holding is cleared.
```

Lint and types: not re-run by me, because CI ran them at this exact commit and that is the stronger witness -- `actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` are five SUCCESS steps in run 36875204695, none skipped.

## CI, AT THE JUDGED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit b105de1... --json name,conclusion,status,databaseId
out    CI  36875204695  push  completed  FAILURE
cmd    gh run view 36875204695 --json jobs, job by job
out    the verification ladder            success   13 steps   2m55s
out    lint, unit and guards              FAILURE   14 steps  11m08s
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
judge  NOT CK2: no two-second duration and no spending annotation. The two
       skipped jobs are the workflow_dispatch gate under CK0, unavailable BY
       DECLARATION, as at verdicts 79, 80, 81 and 82. THE LADDER IS GREEN on a
       machine neither party controls, which is the CA2 measurement that matters
       for the element work: the twelve rung-3 cells, including the new one with
       its hardcoded edge, pass on Linux.
cmd    gh run view 36875204695 --log-failed
out    ONE failing test, and it is the one my own run names:
out    test_the_guard_survives_the_state[guard_state_every_Carried_pointer_names
out            _the_Carried_SECTION_ITSELF] -- "this state is a defect and must
out            fail", with the nested run reading `235 passed in 1.82s`
out    1 failed, 1018 passed in 625.33s
judge  CI AND MY RUN AGREE, BY NAME, ON EXACTLY ONE FAILURE. CI is RED at the
       reviewed commit and I record it as red (CA2), not as a local curiosity.
```

**AND THIS RED IS NOT THE CLASS I HAVE BEEN RULING IT AS, WHICH IS A FINDING AGAINST MY OWN TWO PREVIOUS VERDICTS.** At `29570e1` and at `c4d4817` eight `test_the_guard_survives_the_state` failures were present and I attributed all eight to the cascade off a red `baseline` -- the step-boundary circularity. **Seven of the eight cleared the moment the answering revision landed. This one did not, and `baseline` is GREEN here**, so there is no cascade left to attribute it to. It is an independent red that sat inside a group I ruled on by class rather than by state, for two rounds. R629.

## Carried

* **R624 -- OPEN, BLOCKING, WITH XABIER, AND NOT STEP-2 WORK (EB4).** Nothing in these two commits moves it: `RIGID_MODE_EXACTNESS` stands at `1e-15` and the `tolerances.py` diff changes no `NAME = value`. **One measurement this round sharpens the ruling and costs nothing**, because every round so far has argued the COUNTER side and nobody had swept the CLEAN side of the band the refusal applies to:

```
cmd    the worst clean element_rigid_residual over 60000 random admissible points
       plus 200 Nelder-Mead restarts, D_o 0.05..20 m, t/D_o 0.0005..0.49, L
       constrained to L/D >= 2 and L/r <= 300, S355
out    1.956747e-17  at D_o 0.2286, t/D_o 0.00383, L 0.4743
rule   element_rigid_residual(k_local, L) <= RIGID_MODE_EXACTNESS
judge  51.1x INSIDE the inherited ceiling. SO THE INHERITED 1e-15 DOES NOT FALSE
       REFUSE ANYWHERE I CAN REACH, and R624 is not a defect waiting to fire --
       it is exactly and only the question of whether a ceiling measured on a
       different quantity may host three counters. That narrows what Xabier is
       being asked to rule.
cmd    the smallest clean seventh_over_epsilon over the same band
out    3.850549e+10  at D_o 0.3056, t/D_o 0.3823, L 23.54, L/r 299.9
rule   seventh_over_epsilon(k_local, L) >= RIGID_MODE_BOUND
judge  1.93e+08x above the floor. That clause had never been swept over anything
       but the sixteen members; it is clean over the whole band too.
```

* **R625 -- CLOSED at verdict 82 and still closed.** My eight-mutation probe this round adds one reading worth keeping: the residual clause alone sees a NON-SYMMETRIC stiffness, because both spectral clauses take `(k + k.T)/2` before they look.
* **R626 -- ANSWERED IN ITS HEADLINE at `8ed0fd4`, verified rather than accepted. THE REST OF ITS CONDITION IS OPEN AND CARRIES.**

```
cmd    the shipped cell, run, with its own prints
out    the edge, bisected independently by me   2.1273422e-10
out    the committed hardcoded edge             2.127342e-10    ratio 1.0000001
out    half the edge   7th/eps 9.9762e+01   residual 8.721e-20
out    twice the edge  7th/eps 3.9905e+02   residual 8.721e-20
out    the two ratios to the bound              0.5000 and 2.0000
judge  (i) IS DONE AND DONE WELL. The seventh clause raises, at a SOLVED edge,
       from both sides, with the other two ceilings asserted satisfied on both --
       so the refusal is the position of the mode. The quantity is linear in the
       retained fraction, so a two-fold bracket in the DECISION quantity is a
       bracket and not a sample. And the cell cannot rot into a vacuous pass:
       both inequalities are asserted across the bound.
cmd    and for the OTHER TWO clauses, how far past their thresholds do the
       committed inputs still sit?
out    the three INDEFINITE cells     4.70e+09x past the floor, unchanged
out    the LIFTED rigid-mode cell     3.78e+03x past the ceiling, unchanged
judge  (ii) IS DONE FOR ONE CLAUSE OF THREE. The condition read "for each of the
       three clauses an input just inside and one just outside its own solved
       boundary". Half an item is not the item (CLAUDE.md), so this is open --
       AND it belongs where it is going: those two boundaries ARE the counter
       registration, which is step 3's work beside R624. Every edge is measured
       and written here; nothing is re-derived.
out    the signed clause, torsion site    2.127350e-10 of the block's magnitude
out    the signed clause, axial site      9.599513e-16
out    the residual clause, rotational_block, worst over the sixteen  2.642868e-12
```

* **R627 -- ANSWERED at `8ed0fd4` in both its halves, with one residue that becomes R631 and one closure item.** I read the entry line by line. `floatfea/tolerances.py:407-431` declares the third reading as `lambda_min(k_hat) >= -RIGID_MODE_BOUND * ||k_hat|| * eps` on the element-local homogenisation, says why it is still ONE constant, carries TWO margins labelled by subject, points at the report for the derivation rather than carrying a table (BI3), and says in its own words that a sampled worst is not a proven bound. **That is more than I asked for and the hedge is the right instinct.** `floatfea/element/rigid.py:135-139` now labels its published range as the real platform's members, which is the first half of condition (ii).
* **THE TWO RULINGS THE HAND-BACK ASKED FOR, SO THEY ARE ON THE PAGE.** **(1) Yes -- a sampled quantity may be written into `tolerances.py` that way**, and this entry is how: the sentence says it is the worst on the grids tried, it says the margin is two decades rather than a theorem, and it does not promise a bound. What it must not do is offer coordinates that cannot reproduce it, which is R631. **(2) Three readings under one name is NOT one too many.** I re-read the entry asking exactly that and the answer is no: all three are statements about where the round-off band ends on one homogenised matrix, the paragraph says so, and the alternative -- a fourth constant whose value nothing measures independently -- is worse. The thing that would make it two decisions is a quantity change, and the entry names the quantity for each reading.
* **C89 -- WITHDRAWN. I MEASURED IT AND IT IS WRONG.** See R630. The locked plan's three bisected edges are right to the digit.
* **C88 -- STILL OPEN, CLOSURE, AND HERE IS THE RULING THE HAND-BACK ASKED FOR.** **It waits for the closure commit.** It is a citation defect in a locked plan and not a gate assertion: every figure in that plan block that is a MEASUREMENT reproduces exactly (R630), and what fails is the sentence attributing them to a command that prints something else -- 1851 corpus elements and a per-frame `lambda_6` split, not one of the sixteen-member figures. **One condition on the wait:** it lands BEFORE step 3 chooses an injection size, because step 3 reads those rows. A wrong number in a locked plan is worse than one in a report, and the answer to that is the order of the fixes rather than another round.
* **C86, C90, C91, C92, C93, C94, C95, C96 -- STILL OPEN, closure, not re-reviewed.** Four new ones below. **Nothing on that list has become blocking in my reading since verdict 82** -- the hand-back asked, and the answer is that the three items I am blocking on are new measurements of this round, not promotions from the list.
* **C74, C76, C78, C82, C85, R610, R615 -- carried unchanged, no work asked, one line each.**
* **C75, C75b -- closed and still closed.** `ruff`, `black --check` and `mypy` all SUCCEEDED on CI at this commit.
* **R611, R617 withdrawn and staying withdrawn. R616, R613, R612, R614, R618 to R621, R623 closed as ruled at 79, 81 and 82. R622 is F4. R628 ANSWERED -- the newest revision's header names verdict 82 at its own commit.**
* **C58 to C64, C65 to C73, C40, C56(iii), C56(iv), C57 -- as ruled at verdicts 77, 79, 80, 81 and 82.** These two commits touch none of them.

## Findings

**R629. (d, BLOCKING, CARRIES) ONE TEST IS RED AT THE JUDGED COMMIT ON BOTH MACHINES, IT IS NOT THE STEP-BOUNDARY CLASS, AND WHAT IT IS REPORTING IS THAT THE POINTER CHECK CERTIFIES NOTHING.** The negative control plants "every Carried pointer names the Carried section itself" and requires the guard to report. The guard does not report: the nested run reads `235 passed`, exit 0.

```
cmd    the harness's own action, read: tests/test_report_guard_states.py:539-547
out    it rewrites every section pointer in the NEWEST REVISION to section 9
cmd    apply that substitution myself and ask whether the text changes
out    IT CHANGES -- the section 7, 5, 4, 3, 2 and 1 occurrences are rewritten,
out    so the state IS built. The harness is not the defect.
cmd    count the pointers in the newest revision BEFORE any planting
out    52 of them are ALREADY section 9 -- every row of the generated Carried
out    table and of the answered table
cmd    what is section 9 of the newest revision?
out    "Where each carried item stands" -- a bulleted list naming EVERY item
cmd    docs/reports/F3/step-2-answers.json, the `where` field per item
out    R610 through R628: every one of them is section 9
rule   a gate carries its own failure -- break the claimed property and confirm
       the assertion goes red
judge  THE SHIPPED REPORT IS ALREADY IN THE PLANTED STATE, so the planted copy
       and the healthy copy are indistinguishable to a resolution that asks only
       that the named section exist and mention the item. The control cannot fail
       because there is nothing left to break. This is the recorded
       assertion-domain-blindness shape: the collection the assertion inspects
       cannot contain the failure.
```

**Closed when** one of two things, and both are inside CZ0's "an existing guard that fails false is fixed or deleted, never extended" -- a guard that passes a planted defect is failing false: **(i)** the pointer resolution in `tests/test_report_carried.py` stops resolving against a section that mentions every item, so a pointer has to discriminate; or **(ii)** the state is deleted under DR1 and the vacuity is recorded in the closure artifact, standing in my corpus row as what was measured. **And in either case** `docs/reports/F3/step-2-answers.json` should carry the section that actually answers each item -- the newest revision's own section 9 already says R628 is section 1, R627 section 2, R626 section 3, R625 section 4 and R624 section 5 -- because a `where` column that is one constant for nineteen items is not a pointer. **No new apparatus is asked for. This red must be green before the closure commit is finished (CZ1 iv), and it is the first thing step 3 touches.**

**R630. (b, BLOCKING, CARRIES) THE THREE DETECTION EDGES PUBLISHED IN THE SOURCE TREE AS "THE DETECTION EDGES" ARE THE BEST OF SIXTEEN MEMBERS. THE LOCKED PLAN'S ARE THE WORST, AND THE PLAN IS RIGHT. IT IS THE R627 SHAPE ONE QUANTITY OVER, AND STEP 3 WILL CHOOSE AN INJECTION SIZE FROM IT.** Bisected per member, with the injection shapes taken from `scripts/rigid_counter_response.py`'s own `injected`, against `RIGID_MODE_EXACTNESS`:

```
cmd    per member, bisect the size at which the residual crosses 1e-15; report
       the LARGEST over the sixteen (what a counter must exceed to redden EVERY
       member) and the SMALLEST (the easiest member)
out    dropped_flip      worst 5.285599e-14   best 2.735459e-14
out    wrong_dof_index   worst 1.094071e-15   best 1.057143e-15
out    rotational_block  worst 2.642868e-12   best 6.837686e-13
cmd    docs/milestones/F3.md section 5's bisected rows
out    5.286e-14 / 1.094e-15 / 2.643e-12   -- THE WORST. THE PLAN IS RIGHT.
cmd    tests/verification/rung3/test_platform_rigid_modes.py:370 and report s.5
out    2.735459e-14 / 1.057143e-15 / 6.837686e-13  -- THE BEST, verbatim.
rule   a margin is quoted at the worst case of the subject asserted, and a ratio
       carries its operating point
judge  A SIZE CHOSEN JUST ABOVE 2.735459e-14 FOR dropped_flip REDDENS ONE MEMBER
       OF SIXTEEN AND NOT THE WORST, which needs 1.93x more. That is a counter
       registered under a size that cannot see the defect on fifteen members --
       the precise thing the implementer was right to refuse last round, reached
       by arithmetic instead of by choice. And the sentence attached to the
       figures ("the inherited size sits BELOW two of them") is true of BOTH
       sets, so nothing in the tree would catch the substitution.
cmd    the other rows of the same plan block, for completeness
out    weakest response at SIZE = 1e-8:  1.891891e-10 / 9.140177e-09 /
out                                      3.783782e-12  -- the plan, exactly
out    reddened at the declared 1e-14:   0/16, 16/16, 0/16, with worst responses
out                                      3.656327e-16 / 9.459456e-15 /
out                                      1.464442e-17 -- the test comment, exactly
judge  so every MEASUREMENT in both places reproduces, except which end of the
       sixteen the three edges are taken from.
```

**Closed when** `tests/verification/rung3/test_platform_rigid_modes.py:368-371` names the end it quotes -- either the worst-over-sixteen figures above, or the same three labelled "the easiest member of sixteen; the worst needs `5.285599e-14`, `1.094071e-15` and `2.642868e-12`" -- and step 3's injection size, when it is chosen, is chosen against the WORST. **It is (b) and not prose:** the figure is the input to a counter-size decision and nothing else in the tree states that edge.

**R631. (b, BLOCKING, CARRIES) THE `RIGID_MODE_BOUND` ENTRY'S NEW MARGIN IS PUBLISHED WITH AN OPERATING POINT THAT DOES NOT PRODUCE IT. THE FIGURE IS RIGHT -- I FOUND WORSE -- AND AS WRITTEN NOBODY CAN CHECK IT.** This is the CP2 shape: the round's fix was a margin quoted at the wrong end of the wrong subject, and the correction publishes a point that is not the point.

```
cmd    element_lambda_min_over_epsilon at EXACTLY the entry's own point --
       D_o = 1.468 m, t/D_o = 0.3864, L = 4.634 m, S355
out    -5.207773e-02      margin 3831.3x
cmd    what the entry publishes beside those coordinates
out    "worst clean found -1.332560e+00, margin 149.7x"
cmd    1331 points in a +-5e-4 RELATIVE box around that point
out    the values span -1.077133e+00 to EXACTLY 0.000000e+00
judge  IT IS A ROUND-OFF-SCATTER FUNCTIONAL AND FOUR SIGNIFICANT FIGURES CANNOT
       LOCATE IT. The number is not wrong; the coordinates are unusable, and they
       are the only route a later reader has to the one figure that justifies
       reading this constant in a third direction.
cmd    my own searches, independent of both published grids
out    nu free over the band, 400 restarts   -1.353920e+00   147.4x
out    refined near the entry's own region   -1.372438e+00   145.4x at
out                                          D_o 1.48121, t/D_o 0.351624, L 4.35596
rule   lambda_min(k_hat) >= -RIGID_MODE_BOUND * ||k_hat|| * eps, over the
       admissible band the REFUSAL applies to
judge  THREE INDEPENDENT SEARCHES NOW AGREE: the band worst is of order -1.4 and
       the margin of order 145x. MINE IS THE WORST OF THE THREE, which is the
       second round running that a published band worst has been beaten by the
       next grid -- so "the worst on the grids tried" is the right way to write
       it. NO FALSE REFUSAL EXISTS ANYWHERE I COULD REACH, including with an
       unphysical Poisson ratio, so this is about the record and not the code.
```

**Closed when**, site by site: **(i)** the entry's refusal-side row either drops the operating point and names the command that regenerates the sweep, or gives the coordinates at full `repr` precision and the figure reproduces from them; **(ii)** the worst is re-taken including the two figures above, so the published number is the worst of every grid tried rather than of one; **(iii)** the one element of verdict 82's R627(i) that did not land goes in with it -- that the outcome is unchanged for any floor between the band worst and the weakest defect (`9.3791e+11`), which is the measurement that says the VALUE is not load-bearing in this direction and is the strongest sentence available for the reuse. **No value moves.**

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step closure commit and verify it AFTER it exists (CZ1).

* **C97.** `docs/reports/F3/step-2.md` section 3 publishes `lam_min/eps -1.579e-03` at half the edge; the shipped cell prints `-2.331e-04` at this commit, a factor of 6.8. The other five fields of that block reproduce exactly, including `-1.680e-03` at twice the edge. The margin on that field is `1e+05x`, so no assertion moves -- but it is the sixth field of the block that corrects a figure, and it came from a cell that is not the shipped test. **Closes when** the row is taken from the test's own output.
* **C98.** `floatfea/element/rigid.py:141-144` still carries "NO NEW CONSTANT. `RIGID_MODE_BOUND` already says ..." -- the justification R627(ii) asked to move into the entry. The entry now carries it too, so this is a duplicate rather than the only home, which is why it is here and not above. **Closes when** the docstring points at the entry.
* **C99.** The CZ1 sharpening is NOT in the repository as a clause. Report section 11 carries the measurement -- "the 103 go green as this revision lands, not with time" -- and no proposal text and no Xabier-facing paragraph; the one `CZ1` line in the report is about the reusable half. **My wording, restated here so the channel is a verdict and not an agent message:** *the first-report carve-out should say that state (2) is cleared BY THE ANSWERING REPORT and not by time -- if no answering report is written the state does not clear, and a tree red with no revision in sight must read as what it is.* That is the sentence, it is four lines, and it narrows nothing. **Closes when** it is in `CLAUDE.md` by directive, or recorded as declined.
* **C100.** Report section 6a's generated column reads "the file is untouched" for `floatfea/element/rigid.py:135-139` while the prose in the same row reads "TOUCHED in this round at `c4d4817` and `8ed0fd4`". Both are defensible -- the column is this round's diff, the prose is the step's -- and a reader cannot tell which. **Closes when** the column says which range it is over.
* **C88** -- still open, ruled in `## Carried`: the plan's figures are right, the cited command prints none of them, it waits for the closure commit, and it lands before step 3 picks a size.
* **C86, C90, C91, C92, C93, C94, C95, C96, C74, C76, C78, C82, C85, R610, R615** -- carried unchanged, see `## Carried`.
* **C89** -- WITHDRAWN, measured wrong. See R630.

## Tolerances touched

```
cmd  git diff 86e161b..HEAD --numstat -- floatfea/tolerances.py
out  26  0
cmd  the same diff grepped for a changed `NAME = value` line
out  (no output)
cmd  git diff 86e161b..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  no output
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py        one conftest in the tree; no rung carries its own
cmd  tests/conftest.py, read line by line (CH2), unchanged this round and read anyway
out  it registers a hypothesis profile, adds a rung marker from the directory and
out  SORTS items by rung. It removes no item, rewrites no report, sets no outcome.
judge  NO VALUE MOVED, NO GOLDEN, NO PARAMETRISATION, NO `_COUNTER` AND NO
       ASSERTION WAS LOOSENED. One entry's COMMENT grew by 26 lines and one test
       function was added.
```

| constant | value | what changed | justification located |
|---|---|---|---|
| `RIGID_MODE_BOUND` | `199.526231496888`, unchanged | its entry now declares the THIRD reading -- a signed floor on `lambda_min` of the element-local S-homogenised matrix -- as the lower edge of the window it already declared, with the sign kept, and carries a margin for each of the two sites | `floatfea/tolerances.py:407-431`, which is where `CLAUDE.md` requires it. **R627 is answered.** The residue is **R631**: the refusal-side margin's operating point does not produce its figure, and the insensitivity window is not there. |
| `RIGID_MODE_EXACTNESS` | `1e-15`, unchanged | nothing | unchanged, and still what **R624** is held on -- narrowed this round by the band sweep in `## Carried`, which puts the clean side `51.1x` inside it. |

## My own instructions (4b), read line by line

```
cmd  git diff 86e161b..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  (no output)
cmd  git log --oneline 86e161b..HEAD --name-only
out  two commits, four files, all under floatfea/, tests/ and docs/reports/
judge  NOTHING IN MY OWN INSTRUCTIONS CHANGED, and neither commit mixes a process
       path with a code path. No STOP-class process finding. Verified by the diff
       being empty rather than by the commit subjects.
```

## THE EXCLUSION: DID IT HIDE ANYTHING? YES -- ONE THING, AND IT IS R629

The hand-back asked me to check this and it is the right question to have asked.

```
cmd    the report's own post-revision re-run, section 11
out    "python -m pytest tests/test_report_carried.py
out      tests/test_report_numbers_are_sourced.py -q, in place" -> 1 failed, 263 passed
judge  TWO OF THE THREE EXCLUDED FILES. `tests/test_report_guard_states.py` is the
       third member of REPORT_PARAMETRISED and it was not in that command -- and it
       is the one that CANNOT be run in place, because it clones the repository and
       so cannot see an uncommitted revision. The one file whose answer needs the
       commit to exist is the one the in-place check could not cover.
cmd    my own whole-suite run, no exclusion, at the committed revision
out    1 failed, 2939 passed -- and the one is in that third file
cmd    scripts/suite_count.py:52-59, read
out    the exclusion is a fixed three-file list, both halves are measured, and every
       failing id of both halves is printed into the report
judge  SO THE MECHANISM IS HONEST AND THE CLAIM AROUND IT IS NOT QUITE TRUE. "The
       103 are state (2)" is right for 102 of them. "Nothing outside the excluded
       set is red" is TRUE. What is false is the implication that the excluded set
       goes green as the revision lands: 102 did, one did not, and no in-place run
       could have told the implementer which. That is CZ1's reusable half doing
       exactly what it says, and it is why the reviewer runs the suite at the
       committed revision.
```

**The report's 2650 and my 2939 are not comparable and neither is wrong.** Mine is the whole tree at the committed revision with no exclusion; the report's is the tree minus three files at the commit before the revision existed. The number that decides anything is mine, and it is `1 failed`.

## The adversarial corpus (BE3)

`tests/corpus/element_g21_triple_reach_and_record.txt`, batch 30, committed separately from this verdict at `5a2ff21`. **TWENTY-EIGHT ENTRIES, ALL TWENTY-EIGHT UNSEEN.** In scope under DE2: the element, the gates, the platform model; section E is the one report-guard shape, in scope because it is the only red in the tree.

**TEN ROWS PREDICT `caught`. FIVE READ CAUGHT.** That is worse than batch 29's eight of thirteen, and the shape of the miss is the finding: **not one of the five is the element.** All five are figures -- a printed diagnostic in a report (C97), an operating point in a tolerance entry (R631), a detection edge taken at the best of sixteen (R630), a command cited for figures it does not print (C88), and a pointer column that makes its own guard vacuous (R629). **Five mutation rows predicted caught and five were caught, which is the first clean sweep of a mutation section this milestone.**

**Three rows are `expect=blind`, and they are reach boundaries measured rather than failures**, recorded so no later reader takes this triple for a general element check: a dropped shear parameter, an axial `EA` doubled, and the same member expressed in millimetres all pass all three clauses and build the platform. The second is new and worth having written down -- **a pure magnitude error in one stiffness term is invisible to G2.1**, which is correct, because the triple checks rigid modes, mode position and sign and not the value of any stiffness. The third says the clean reading moves by `24x` under a thousand-fold change of length unit, which spends a sixth of the band margin R631 is about; internal SI is a `CLAUDE.md` non-negotiable, so it is a property of the figure and not a live defect.

```
cmd  grep -c "^id=" tests/corpus/element_g21_triple_reach_and_record.txt
out  28
cmd  grep -rn "element_g21_triple_reach_and_record" tests/ scripts/ --include=*.py
out  (no output) -- named by no .py, so it adds no parametrised case
cmd  python -m pytest tests/test_collected_set_golden.py tests/test_marker_exemption_corpus.py
       tests/test_report_vocabulary_corpus.py tests/test_tree_prose_consistent.py
       tests/test_ci_ladder_gating.py -q        with batch 30 in the tree
out  298 passed in 131.97s        exit 0
judge  THE CORPUS COMMIT REDDENS NOTHING, measured and not reasoned -- the same 298
       as batch 29.
```

Every mutation was applied in a scratch harness under the session scratch directory, importing the shipped functions; nothing in the working tree was written. `git status --porcelain --untracked-files=all` was empty before I began, and the only paths I have written in this repository are that corpus file and this verdict.

## On the criterion

**I ruled under CZ0 and I have one sharpening to offer, not a complaint, and I say it once.** Three of this round's four substantive findings are FIGURES, which CZ0 retires as a blocking head -- and I am blocking on two of them anyway, on the ground my own instructions give me: a figure that a pending (b) decision will be read from is (b). R630 is the clearest case that has arisen: three numbers in a test comment, no assertion attached, and step 3 will pick a counter injection size from them; picked from the published end, the counter reddens one member of sixteen. **The sharpening, in one sentence: a figure becomes blocking when a decision already scheduled in the plan will be taken from it, and the test is whether moving the figure moves the decision.** That is narrow, it is checkable, and it would have classed all six of the retired rounds' findings as closure items, which is the point of CZ0 and I am not trying to unwind it. R629 needs no such argument -- it is (d), measured on two machines.

**And CZ0 worked this round.** I did not re-review ten closure items, no round was spent on prose, and the two reds I care about are a red test and a number that feeds a scheduled decision.

## Carried for the next step

**These block in step 3 and stay blocking there (CZ0, DK0, `CLAUDE.md` section Step gating). Step 3 opens for them FIRST, before the counter registration and before F3's closure artifact.**

1. **R629 -- the red.** The pointer-resolution negative control, red on both machines. First thing touched, and green before the closure commit is finished (CZ1 iv).
2. **R630 -- the three detection edges are the best of sixteen.** Fix the published end, and choose step 3's injection size against the WORST: `5.285599e-14`, `1.094071e-15`, `2.642868e-12`.
3. **R631 -- the entry's refusal-side operating point does not produce its figure**, plus the insensitivity-window element of R627(i) that did not land. No value moves.
4. **R626's residue -- a solved boundary from both sides for the residual clause and for the signed clause.** Both edges are in `## Carried` above; this is the same work as the counter registration and should be done with it.
5. **R624 -- OPEN, BLOCKING, WITH XABIER. Not step-3 work either until it is ruled**, and the round that rules it costs step 3 nothing under EB4. Narrowed this round: the clean side of the band sits `51.1x` inside `1e-15`, so no false refusal is waiting; the question is only whether that ceiling may host three counters.

And the closure list, which the closure commit absorbs in one go: **C86, C88, C90, C91, C92, C93, C94, C95, C96, C97, C98, C99, C100**, plus the ledger lines **C74, C76, C78, C82, C85, R610, R615**. **C89 is withdrawn.** C88 lands before step 3 picks a size.

## Next step opens when

**Step 2 is CLOSED at PASS, on the third round, and its disposition is this verdict (DD1).** The next step opens immediately -- and its first three commits are the carried list above, in the order given, not the counter registration.

**The specific conditions, so that "address the above" is not what this says:**

1. `python -m pytest -q` at the step-3 commit reads `0 failed`, and a pushed CI run at that sha is green. Today it is `1 failed` on both machines and that is R629.
2. `tests/verification/rung3/test_platform_rigid_modes.py:368-371` names which end of the sixteen its three edges are, and no injection size is registered against the best member.
3. The `RIGID_MODE_BOUND` entry's refusal-side row reproduces from what it publishes, by full-precision coordinates or by a command.
4. The residual and signed clauses each carry an input just inside and one just outside their own solved boundary, as the seventh clause now does.
5. R624 is ruled by Xabier, either way, and the ruling is written where the next reader finds it.

**Schedule.** F3 closes **13 October**; F4 19 October; the member-force table 23 October; the code-check screen 28 October. **I have no measurement that contradicts any of them.** The ladder is green on CI at this commit, which is the one that would. The four carried items are one guard decision, one comment correction, one entry edit and two test cells -- none is a day of work. **DZ7c IS triggered in its letter**, because this is the second consecutive step to close carrying blocking items, so the choice is stated as DZ7c requires and the standing answer applies: **reduce scope, do not slip.** Nothing carried can change a member force or the G4.1 equilibrium check except R624, which keeps blocking at G4.1 as DZ7c says; the rest is the record. **I am not asking for a slip and I see nothing to cut.**

**One sentence for the implementer, since this closes the step.** The element is sound, the refusal is on the production path, the new boundary cell is the best thing in the step, and every one of my four carried items is about a NUMBER THAT WAS WRITTEN DOWN rather than about the code. That has been the shape of the whole step, and it is worth knowing before step 3 writes anything.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 2
Reviewed commit: 6b3642a599b78c5d867869f041bc2801cbda1acc
Verdict: HOLD
Judged commit: c4d48173792770066c9f525f08930a7a5bbc428c  (HEAD of F3 and pushed when I read it; the stamp above is HEAD at write time, which is corpus batch 29 at 6b3642a -- the tool records that limitation in its own docstring)
Tests: 2843 passed, 68 failed, 0 skipped   (my own run, ONE invocation, clean tree, 651.91s -- not the 317-test subset the hand-back quotes)

## Round of 2026-10-01 -- EIGHTY-SECOND verdict, ROUND 2 OF 3 ON STEP 2, AND IT COUNTS

**The hand-back asked which side of EB4 this round falls on, so I rule it first.** EB4 exempts "a verdict spent on a STOP or blocker whose resolution belongs to the supervisor or to the user", and counts a verdict "when it judges implementer work done for that step". This round judges one commit of implementer work for step 2; R624 consumed one paragraph and the rest went to the code. **It counts. Round 2 of 3. One round remains.**

**R625 IS ANSWERED AND THE FIX IS BETTER THAN THE ONE I MEASURED.** I accepted no row of it. I re-ran the cell, added two negation shapes the committed test does not carry, swept 20400 clean admissible points for a false refusal, solved the detection boundary at two sites, took the negative control, and drove the refusal from `build_superstructure` rather than from a test. Every one of those says the clause is right.

**R626 IS ANSWERED IN PART, AND WHAT IS MISSING IS THE CLAUSE THAT NEVER HAD EVIDENCE.** Two of the three clauses now have a committed cell showing them raise. The SEVENTH-MODE clause still has none, and it is the clause whose only published shape is the one I refuted last round. No boundary in the new cells is solved; all five sit decades from the threshold they are about.

**AND THE REPORT IN THE TREE ANSWERS VERDICT 80.** That is item 1b of my own instructions and it is not a formality this time: 68 tests are red at the judged commit, on CI and on my machine, and every one of them says the newest verdict is unanswered.

## THE THREE RULINGS THE HAND-BACK ASKED FOR

**1. `-RIGID_MODE_BOUND` IS THE RIGHT COMPARAND AND IT IS NOT A SECOND DECISION WEARING ONE NAME. MEASURED, IN FOUR CELLS, NOT ARGUED.**

The constant is already declared two-sided in its own entry. `floatfea/tolerances.py:390-405` says "THIS CONSTANT IS READ IN TWO DIRECTIONS" -- a floor on `lambda_7`, a ceiling on `lambda_6` -- and calls them "the two sides of the same window", the window being where an eigenvalue of the homogenised matrix stops being round-off. A signed floor on `lambda_min` is the lower edge of that same window with the sign kept. One decision, not two, and I would have ruled the same way.

```
cmd    can a CLEAN admissible member fall below the floor? D_o 0.05..20 m,
       t/D_o 0.0005..0.49, L constrained to L/D >= 2 and L/r <= 300, S355,
       20400 points, then a refined grid around the worst corner
out    worst clean   -1.170315e+00   at D_o 4.4  t 0.88    L 58.19   L/r 45.4
out    refined       -1.202245e+00   at D_o 4.0  t 0.2607  L 266.34  L/r 201
out    clean points that would be REFUSED                            0
rule   element_lambda_min_over_epsilon(k_local, L) >= -RIGID_MODE_BOUND
judge  NO FALSE REFUSAL ANYWHERE IN THE BAND. The margin at the worst
       admissible point is 166x.
cmd    does it degrade with slenderness? hold the section, sweep L/r from 1 to
       1e7 -- seven decades past the admissible edge -- then L/D from 2 to 1e-4
out    L/r sweep   stays within -6.1292e-01 .. -5.6999e-07, no trend
out    L/D sweep   stays within -7.3380e-01
judge  the S-homogenisation removes the length scaling, so this quantity has no
       runaway direction. That is WHY the reuse is safe, and it is the cell.
cmd    for which floors F is the outcome unchanged on every clean point and on
       every sign shape?
out    ANY F in (1.2023, 9.3791e+11) -- 11.9 decades. The shipped 199.526 sits
out    166x above the clean worst and 4.701e+09x below the weakest defect.
judge  THE VALUE IS NOT LOAD-BEARING HERE. That is the strongest argument for
       the reuse, and it is why R627 below is about the RECORD and not the
       number: nothing in this assertion asks for 199.526 specifically, so
       nothing is gained by minting a constant and nothing is lost if the
       lambda_7 side ever moves this one.
cmd    how small a SIGN error does it read? bisect, worst over the sixteen
out    torsional block scaled by -a    a = 2.127350e-10 of its own magnitude
out    axial block scaled by -a        a = 9.599513e-16
judge  so it is not only a catcher of whole negations: a torsional stiffness
       negative at two ten-billionths of its own size is already refused.
```

**What I do not accept is the record as it stands, and that is R627.** The entry enumerates its readings and names R540 as the finding for a reading that shipped without being written there. A third reading now ships in two places and the entry still says two.

**2. "STILL PASSES" RATHER THAN BIT-IDENTICAL IS RIGHT, AND I REPRODUCED THE DOUBLES THAT REFUTE THE STRONGER FORM.**

```
cmd    repr(seventh_over_epsilon(k, L)) clean and under each shape, hub1_arm
out    clean                        937911510493.6768
out    torsion sub-block negated    937911510493.6768
out    axial sub-block negated      937911510493.677
out    THE WHOLE matrix negated     937911510493.677
out    bending-z negated            937911510493.6768
out    bending-y negated            937911510493.6768
out    the residual is identical to the last bit in all six, 8.721077547984348e-20
rule   what the cell has to carry is that the shape PASSES THE OTHER TWO
       CEILINGS, so a refusal can only have come from the signed clause
judge  CONFIRMED on exactly the two shapes the hand-back names. A bit-identity
       assertion would have been a claim about the eigensolver inside a cell
       whose subject is detection -- and it would have been FALSE. The weakening
       is the correct reading and I would have made the same one.
```

**3. YES -- PUBLISH THE CORRECTION IMMEDIATELY, IN ITS OWN REVISION, AND DO NOT WAIT FOR R624.** The revision is owed for three independent reasons and none of them depends on R624: item 1b of my instructions, `CLAUDE.md` section Step gating, and the 68 red tests whose single cause is its absence. A revision can say "R624 is with Xabier, unanswered" in one line, and for the dependency list that IS the answer -- the guard asks for each site to be touched or DECLARED, which is what declaring it does. **Withholding the revision did the opposite of protecting section 5: it left every figure of this round outside the repository, in an agent message, which is the one place BF0 says a number may not live.** The four rows I was asked to accept are now reproduced above; they are good; and had I not reproduced them, nothing in the tree would carry them.

## THE TREE AT c4d4817, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    c4d48173792770066c9f525f08930a7a5bbc428c   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 4add9d5..HEAD --name-only
out    c4d4817  floatfea/element/rigid.py
out             floatfea/model/platform.py
out             tests/verification/rung3/test_platform_rigid_modes.py
judge  ONE COMMIT, three files, one path class. It touches neither docs/reviews/
       nor .claude/ nor docs/SUPERVISOR.md nor CLAUDE.md, so there is NO
       STOP-class process finding this round.
cmd    git diff 4add9d5..HEAD --stat
out    rigid.py 40 +, platform.py 26 +, the rung-3 gate 109 +   169 +, 6 -
cmd    python -m pytest -q
out    68 failed, 2843 passed, 2 warnings in 651.91s (0:10:51)
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    112 files would be left unchanged
cmd    python -m mypy floatfea
out    Success: no issues found in 30 source files
cmd    python -m pytest tests/verification/rung3/test_platform_rigid_modes.py -q
out    11 passed in 1.12s
cmd    grep -n "Answers:" docs/reports/F3/step-2.md
out    3:Answers: verdict 80 @ 7e5f3fb
cmd    git log --oneline -1 -- docs/reviews/F3/
out    4add9d5  the EIGHTY-FIRST verdict -- the newest verdict commit
judge  ITEM 1b FAILS. The header names verdict 80; the newest is 81. R628.
```

**AND THE COLLECTED TOTAL IS NOT COMPARABLE ACROSS A VERDICT BOUNDARY, recorded so that 3100 -> 2843 is not read as tests disappearing.**

```
cmd    python -m pytest --collect-only -q | tail -1
out    2911 tests collected          (verdict 81 measured 3109 at 29570e1)
cmd    python -m pytest tests/test_report_carried.py --collect-only -q | tail -1
out    205 tests collected
cmd    the site parametrisation, called directly: len(_sites_by_finding())
out    59, over findings R610..R626 read from the NEWEST verdict file
judge  that guard parametrises over the newest verdict -- it read step-1.md with
       twenty-four findings before and reads step-2.md now -- so the collected
       count is a function of the verdict. A total compared across that boundary
       is not like-for-like; 2911 is the number at this commit.
```

## CI, AT THE JUDGED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit c4d4817... --json conclusion,status,workflowName,databaseId,event,headSha
out    CI  36867957796  push  completed  FAILURE   headSha c4d4817...
cmd    gh run view 36867957796 --json jobs, job by job with runner and duration
out    the verification ladder            success   13 steps   3m08s
out    lint, unit and guards              FAILURE   14 steps   12m02s
out    CI determinism -- leg              skipped    0 steps
out    CI determinism -- ten legs agree   skipped    0 steps
judge  THE JOBS RAN. Not CK2: no empty runner with a two-second duration and a
       spending annotation. The two skipped jobs are the workflow_dispatch gate
       under CK0, unavailable BY DECLARATION, as at verdicts 79, 80 and 81.
cmd    the step list of the failing job
out    actionlint, ruff, black --check, mypy and unit tests ALL SUCCESS, none
out    skipped; step 10 "guards and meta-tests" FAILURE
cmd    gh run view 36867957796 --log-failed, grouped by test function
out    test_every_named_site_is_touched_or_declared[R616..R626-<site>]  most of it
out    3 x test_the_report_carries_the_finding
out    1 x test_the_CI_section_is_about_the_REVIEWED_commit
out    1 x test_the_Carried_table_is_what_the_generator_produces
out    1 x test_the_generator_would_catch_a_row_under_the_wrong_number
out    8 x test_the_guard_survives_the_state[baseline and seven planted states]
out    68 failed, 923 passed in 684.23s
cmd    my own whole-suite run at the same commit
out    THE SAME SET, BY NAME. 68 failed, 2843 passed.
judge  LADDER GREEN. The ladder job is the one that would say a rung is red, and
       rung 3 -- including the five new cells -- passed on a machine neither
       party controls. That is the CA2 measurement that matters here.
```

**THE RED IS NOT (d), AND I RULE IT BY HAND FOR THE SECOND VERDICT RUNNING.** Every one of the 68 is the state verdict 81 enumerated as "verdict written, answering report not yet": each names a finding or a site of the newest verdict and asserts the report answers it. Reading that as (d) makes every step boundary permanently red -- the no-exit `CLAUDE.md` records at DD1 as costing two verdicts, neither about the work. **But the premise of that ruling is that the ANSWERING REPORT clears them, and no answering report was written** -- so this red is not self-clearing, it is the measured cost of R628, and the one action that turns 68 red into green is the revision.

## Carried

* **R624 -- OPEN, BLOCKING, AND WITH XABIER. RECORDED AS AWAITING A RULING, NOT AS IGNORED.** I agree with the routing: both closes I offered are decisions rather than work -- (i) a ceiling derived for the quantity it bounds, or (ii) a written separation of the subject of the gate from the subject of the refusal, which is a scope statement about F3 section 5. Nothing in `c4d4817` moves it: `git diff 4add9d5..HEAD -- floatfea/tolerances.py` is EMPTY and `RIGID_MODE_EXACTNESS` stands at `1e-15`. **Under EB4 the round that resolves it costs step 2 nothing; this round was not that round.**
* **R625 -- ANSWERED at `c4d4817`, verified independently rather than accepted.** Seven cells, all mine, at this commit:

```
cmd    each shape alone into k_local on platform:hub1_arm, L = 50 m, then
       floatfea.model.platform.check_rigid_modes
out    clean                        lambda_min/eps -2.1425e-03   accepted
out    torsion sub-block negated    lambda_min/eps -9.3791e+11   REFUSED
out    axial sub-block negated      lambda_min/eps -4.5035e+15   REFUSED
out    THE WHOLE matrix negated     lambda_min/eps -4.5035e+15   REFUSED
out    bending-z sub-block negated  lambda_min/eps -1.8003e+13   REFUSED
out    bending-y sub-block negated  lambda_min/eps -1.8003e+13   REFUSED
judge  the last two are NOT in the committed set and are refused anyway. The
       residual reads 8.7211e-20 and seventh/eps reads 9.379115e+11 on all six,
       so in every case the refusal came from the new clause alone.
cmd    Material(E = -2.1e+11) -- which Material does NOT refuse at construction
       -- through local_stiffness for a real member
out    residual 8.7211e-20 PASSES, seventh/eps 9.3791e+11 PASSES,
out    lambda_min/eps -4.5035e+15 REFUSED
judge  SO THE CLAUSE CLOSES A CONSTRUCTIBLE INPUT CLASS, not only a hand-negated
       matrix. Before c4d4817 that material built the platform.
cmd    replace floatfea.model.platform.local_stiffness with a negating wrapper
       and call build_superstructure()
out    whole negated    -> ValueError, platform:hub1_arm, -4.503527e+15
out    torsion negated  -> ValueError, platform:hub1_arm, -9.379115e+11
out    restored         -> builds
judge  THE REFUSAL IS ON THE PRODUCTION PATH and not only in a test, which is
       the half F3 section 5 actually asks for.
cmd    the negative control: reimplement the check WITHOUT the third clause and
       run the three committed shapes through it
out    NO RAISE on any of the three
judge  so all three pytest.raises(INDEFINITE) cells FAIL if the clause goes.
       THE CELL CARRIES ITS OWN FAILURE -- which is what makes the three new
       tests evidence rather than decoration.
```

  **R625 closes here and carries no further.** The refuted sentence is gone by deletion, so **C87 closes with it.**
* **R626 -- ANSWERED IN PART. STILL OPEN AND STILL BLOCKING on two of the sites its condition named.** What landed is real and I checked it site by site: `check_rigid_modes` is imported, called and asserted to raise at `tests/verification/rung3/test_platform_rigid_modes.py:242` and `:261`; `test_the_REFUSAL_accepts_every_real_member` is the other side; and the `rotational_block` claim at `:257-259` holds -- `scripts/rigid_counter_response.py:88-89` is `out[3, 3] += size * big`, the identical shape. What did not land is in Findings.
* **R627 is NEW and is the only new blocking item.** See Findings.
* **C86 -- STILL OPEN, now in two halves.** The sentence still does not name the quantity the agreement test covers, and the module docstring opens "Two quantities about one 12x12 local stiffness matrix" while three ship.
* **C87 -- CLOSED at `c4d4817`**, by deletion, which is the route I named.
* **C88, C89 -- STILL OPEN against my own section 5, and I am not re-reviewing them.** The hand-back restates the bisected-edge figures; I did not re-measure them this round and they stay on the closure list as the previous round left them.
* **C90, C91 -- STILL OPEN, closure.** Nothing this round touches either.
* **C74, C76, C78, C82, C85, R610, R615 -- carried unchanged, no work asked, one line each.**
* **C75 and C75b -- closed at verdict 81 and still closed.** `ruff`, `black --check` and `mypy floatfea` are clean here, and the first two SUCCEEDED on CI at this commit.
* **R611, R617 withdrawn and staying withdrawn. R616 and R613 closed at 81. R612 closed at 79. R614, R618, R619, R620, R621, R623 closed. R622 is F4.**
* **C58 to C64, C65 to C73, C40, C56(iii), C56(iv), C57 -- as ruled at verdicts 77, 79, 80 and 81.** This commit touches none of them.

## Findings

**R626. (c, STILL OPEN) TWO OF THE THREE CLAUSES CAN NOW BE SEEN TO FAIL. THE THIRD STILL CANNOT, AND NO BOUNDARY IS SOLVED.** The condition read: "for each half, one input just inside and one just outside, with the boundary solved rather than sampled". Site by site:

```
cmd    grep -n "pytest.raises" tests/verification/rung3/test_platform_rigid_modes.py
out    :242   match="INDEFINITE"        the signed clause        DONE
out    :261   match="rigid residual"    the residual clause      DONE
out    nothing for the SEVENTH clause
cmd    grep -rn "first flexible mode" tests/ --include=*.py
out    tests/verification/rung3/test_platform_rigid_modes.py:131  the GATE print
out    no raise, no match, no cell anywhere in tests/ for the rung-3 refusal
rule   a gate carries its own failure -- break the claimed property and confirm
       the assertion goes red
judge  ONE OF THE THREE CLAUSES OF A SHIPPED REFUSAL STILL HAS NO COMMITTED
       DEMONSTRATION THAT IT CAN FIRE, and it is the clause whose only ever
       published shape is the one I refuted last round.
cmd    how far past its threshold does each committed input sit?
out    the three negation cells      4.70e+09x or more past the floor
out    the LIFTED rigid mode cell    3.78e+03x past the ceiling (3.7838e-12
out                                  against 1e-15)
out    the acceptance cell           2.79e+03x inside the floor
judge  so NO cell is just inside or just outside anything. The committed evidence
       says the clauses fire on a gross defect; it does not say what they detect.
       A counter that is one arbitrary perturbation and not a detection threshold
       is incomplete, and all three of these are the former.
```

**I have solved two of the three boundaries so no round is spent measuring them:** the torsional block scaled by `-a` crosses the floor at `a = 2.127350e-10` of its own magnitude, worst over the sixteen (`5.319381e-11` best), and the axial block at `a = 9.599513e-16`. For the seventh clause the boundary is already published -- the retained-torsion fraction `2.127342e-10` from verdict 81 -- and a shape that fires it is the torsional block scaled by `1e-12`, which reads `seventh/eps 9.3750e-01` against `199.526` and raises. **A reading worth having beside them:** on the TORSION site the signed clause and the seventh clause cross at the same `a` to six figures, because for a negated torsion block the seventh eigenvalue IS the minimum one; the reach the signed clause ADDS is on the axial and the two bending sites, where `seventh/eps` never moves off `9.3791e+11`.

**Closed when** `tests/verification/rung3/test_platform_rigid_modes.py` carries (i) a cell that makes the SEVENTH clause raise, and (ii) for each of the three clauses an input just inside and one just outside its own solved boundary -- 0.9x and 1.1x of the edge is enough, and the edges are in the paragraph above. **Not new apparatus:** it is a verification test of shipped `floatfea/` behaviour in the file class that already holds exactly this, and DR1 freezes guards and meta-tests, not rung tests.

**R627. (b, blocking) A THIRD READING OF `RIGID_MODE_BOUND` SHIPS IN TWO ASSERTIONS AND ITS OWN ENTRY STILL SAYS TWO -- WHICH IS THE R540 SHAPE, IN THE SAME CONSTANT, NAMED IN THE SAME ENTRY. AND THE MARGIN PUBLISHED FOR IT IS TAKEN AT THE WRONG END OF THE WRONG SUBJECT.** This is not a complaint about the reuse; ruling 1 above says the reuse is right. It is that `CLAUDE.md` makes `tolerances.py` the sole home of every tolerance and its justification, and the justification for this reading lives in a `rigid.py` docstring instead.

```
cmd    sed -n 390,405p floatfea/tolerances.py
out    "THIS CONSTANT IS READ IN TWO DIRECTIONS, and until R540 only one of them
out     was written down in the file CLAUDE.md makes the sole home of every
out     tolerance" -- then the lambda_7 floor and the lambda_6 ceiling
cmd    grep -n "RIGID_MODE_BOUND" floatfea/ tests/verification/rung3/ -r
out    floatfea/model/platform.py:328   the seventh clause          direction 1
out    floatfea/model/platform.py:344   the SIGNED floor            direction 3
out    test_platform_rigid_modes.py:~186 the signed gate cell       direction 3
out    git diff 4add9d5..HEAD -- floatfea/tolerances.py             EMPTY
judge  THE THIRD DIRECTION IS NOWHERE IN THE ENTRY. The quantity also differs
       from the one the entry declares -- the entry is on `K / max|K|` assembled,
       this is the element-local S-homogenised matrix over its Frobenius norm --
       and nothing in the suite can see either difference.
cmd    would any guard notice? read tests/test_plan_matches_tolerances.py
out    both directions check NAMES and VALUES; neither reads how many assertions
out    a constant has, or in which quantity
judge  so the entry and a reader are the whole mechanism, which is exactly what
       R540 established and what this repeats.
```

**And the margin that justifies the form is quoted at the best member of the narrowest subject:**

```
cmd    element_lambda_min_over_epsilon over the sixteen, both ends
out    worst  -7.1459e-02 on hub1:buoy3_arm   margin 2792x
out    best   -2.1425e-03 on platform:hub4_arm  margin 9.313e+04x
cmd    the same over the admissible band the REFUSAL applies to
out    worst  -1.202245e+00                   margin 166x
rule   a margin is quoted at the worst case of the subject asserted, and a ratio
       carries its operating point
judge  THE COMMIT MESSAGE PUBLISHES "93000x of clean margin on the near side",
       which is the BEST member -- 560x optimistic against the refusal subject.
       The gate cell prints 2.792e+03x, which is right for the GATE. The number
       that justifies a REFUSAL over every deck is 166x, and it appears nowhere.
```

**Closed when**, site by site: **(i)** the `RIGID_MODE_BOUND` entry at `floatfea/tolerances.py:389-405` records the third direction -- a signed floor on `lambda_min` of the element-local homogenised matrix, as the lower edge of the window it already declares -- with TWO NUMBERS and a pointer, not a table (BI3): the clean worst over the admissible band, `-1.202245e+00`, `166x`, and that the outcome is unchanged for any floor in `(1.2023, 9.3791e+11)`, so the value is not load-bearing for this direction; **(ii)** `floatfea/element/rigid.py:135-139` either labels its published range as the sixteen members or carries the band figure, and points at the entry for the justification rather than being it. **No value moves and nothing is widened.** Registering a counter in the new quantity is NOT required here -- the detection edges in R626 are that counter, and registering them is step 3 work alongside R624.

**R628. (ITEM 1b, AND I AM NOT DRESSING IT AS A CZ0 HEAD) THE REPORT IN THE TREE ANSWERS VERDICT 80. THIS ROUND HAD NO REPORT, AND ITS FIGURES LIVED IN AN AGENT MESSAGE.** Item 1b of my instructions is one comparison and it fails: `docs/reports/F3/step-2.md:3` reads `Answers: verdict 80 @ 7e5f3fb`; the newest verdict is 81 at `4add9d5`. The item exists because every `Carried` claim in a report answering a superseded round is about the wrong list -- and here the `Carried` section is literally about verdict 80, while the work in `c4d4817` answers verdict 81.

```
cmd    the 68 failures, by what each asserts
out    test_every_named_site_is_touched_or_declared[R624-..., R625-..., R626-...]
out            every site the NEWEST verdict names, unanswered
out    test_the_report_carries_the_finding   R624, R625, R626 -- three, by name
out    test_the_CI_section_is_about_the_REVIEWED_commit
out    test_the_Carried_table_is_what_the_generator_produces
out    test_the_generator_would_catch_a_row_under_the_wrong_number
out    8 x test_the_guard_survives_the_state   cascading off the same baseline
rule   CLAUDE.md section Step gating: the report carries a Carried section
       answering each open item from the previous review, or declaring it
judge  THE GUARDS ASK FOR EXACTLY WHAT THE HAND-BACK CONTAINS. "Site touched or
       DECLARED" is satisfied by a declaration, so R624 being with Xabier is not
       what blocked the revision -- one line declaring it would have cleared the
       site and most of the 68 with it.
```

**This is not (a), (b), (c) or (d) and I am not calling it one.** It is the precondition on reading the report at all, and it is why the verdict below also records what I could NOT check: whether the report would have stated these figures correctly, with their rules and their operating points, is unmeasurable on an absent revision -- and the one figure of this round that IS in the repository, the commit message, got its margin from the best member of the wrong subject (R627).

**Closed when** `docs/reports/F3/step-2.md` carries `Answers: verdict 81 @ 4add9d5`, a `Carried` section naming R624 (declared, with Xabier), R625 and R626 with the sites each touched, and the section 3 fourth row corrected or withdrawn. **It is one revision and it does not wait on R624.**

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step closure commit and verify it AFTER it exists (CZ1).

* **C92.** `floatfea/element/rigid.py:110` -- "seven negative eigenvalues" is a measurement in the source tree that does not reproduce. Measured with the SHIPPED homogeniser on `platform:hub1_arm`: clean 1, torsion negated 3, axial negated 3, whole negated 9. The commit message says 2 / 5 / 5 / 7 and verdict 81 said 0 / 1 / 1 / 6. Three triples for one quantity, because it counts eigenvalues that scatter about zero at round-off -- it is not a decision quantity and nothing asserts on it. **Closes when** the sentence says the matrix is indefinite, or gives the count with the command that produces it (CW0).
* **C93.** `floatfea/element/rigid.py:3-9` -- "Two quantities about one 12x12 local stiffness matrix" while three ship. Same file, one line. Folded with C86.
* **C94.** `tests/verification/rung3/test_platform_rigid_modes.py:195-198` -- "NO COMMITTED TEST SHOWED IT RAISING -- a grep over `tests/` returned two comment lines, no import and no `pytest.raises`" is refuted by its own grep at this commit, in the file that contains it. Written as history, read as present. **Closes when** it says "before this commit" or goes.
* **C95.** `floatfea/element/rigid.py:81-95` and the two ratios -- a NON-FINITE `k_local` passes all three clauses, and `element_rigid_residual` returns EXACTLY `0.000000e+00` on it, because `max(0.0, nan)` is `0.0` and every comparison against `nan` is `False`; the zero matrix and `k * 1e-300` raise `ZeroDivisionError` rather than refusing; `check_limits` ACCEPTS a `nan` length while `check_rigid_modes` crashes on one. **I measured the reachability before listing it and that is why it is here and not above:** `Section(A=nan, ...)` is refused by the `J = I_y + I_z` check, `Section.circular_tube(nan, t)` by the `I_y != I_z` check (a `nan` fails every equality), a `nan` length raises `LinAlgError` -- which subclasses `ValueError`, so it is refused, by a crash rather than a message -- and the shipped deck YAML carries no `nan` or `inf` token. **Latent, not live.** No new apparatus is asked for under CZ0; it is recorded so the next person to touch these three functions knows.
* **C96.** `floatfea/model/material.py` -- `Material(E=-2.1e+11)` constructs without complaint and `Material(E=0.0)` raises `ZeroDivisionError` from the shear modulus rather than a validation error. The new clause catches both at the element, which is a second line of defence standing in for a first.
* **C86, C88, C89, C90, C91, C74, C76, C78, C82, C85, R610, R615** -- carried unchanged, see `## Carried`.

## Tolerances touched

```
cmd  git diff 4add9d5..HEAD -- floatfea/tolerances.py
out  no output
cmd  git diff 4add9d5..HEAD --stat -- floatfea
out  floatfea/element/rigid.py     40 +      one new function
out  floatfea/model/platform.py    26 +      one new clause
cmd  git diff 4add9d5..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  no output
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py             CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py             one conftest in the tree; no rung carries its own
cmd  grep -rn "pytest_runtest_makereport\|pytest_ignore_collect\|pytest_collection_modifyitems" tests/
out  no output
judge  NO CONFTEST AND NO PLUGIN CHANGED, so nothing new can rewrite what
       scripts/run_rung.sh reads, and the CH2/CI0 reading has nothing to read.
```

**NO VALUE MOVED. NO GOLDEN, NO PARAMETRISATION, NO `_COUNTER` AND NO ASSERTION WAS LOOSENED, and one assertion was ADDED** -- which is the direction this section rarely gets to record.

| constant | value | what asserted it before | what asserts it now | justification located |
|---|---|---|---|---|
| `RIGID_MODE_BOUND` | `199.526231496888`, unchanged | the rung-3 gate at `:125`, `platform.py:328`, rung 1 on the assembled `K / max abs K` | **and now a THIRD reading**: a SIGNED floor on `lambda_min` of the element-local S-homogenised matrix, at `platform.py:344` and in the new gate cell | `floatfea/element/rigid.py:135-144` -- a docstring, which `CLAUDE.md` does not allow to be the home of a tolerance justification, publishing a range taken over the sixteen while the clause is a refusal over every deck. **R627.** My own measurements for the entry: clean worst over the band `-1.202245e+00`, `166x`; outcome invariant for any floor in `(1.2023, 9.3791e+11)`; detection edges `2.127350e-10` torsion and `9.599513e-16` axial. |
| `RIGID_MODE_EXACTNESS` | `1e-15`, unchanged | the rung-3 gate at `:99` and `platform.py:319` | the same, plus the new `rejects_a_LIFTED_rigid_mode` cell | unchanged, and still what **R624** is held on. |

## My own instructions (4b), read line by line

```
cmd  git diff 4add9d5..HEAD --stat -- .claude docs/SUPERVISOR.md CLAUDE.md
out  (no output)
cmd  git log --oneline 4add9d5..HEAD --name-only
out  one commit, three files, all under floatfea/ and tests/
judge  NOTHING IN MY OWN INSTRUCTIONS CHANGED THIS ROUND, and the one commit does
       not mix a process path with a code path. No STOP-class process finding.
       Verified by the diff being empty rather than by the commit subject.
```

## The adversarial corpus (BE3)

`tests/corpus/element_psd_half_reach.txt`, batch 29, committed separately from this verdict at `6b3642a`. **THIRTY-TWO ENTRIES, ALL THIRTY-TWO UNSEEN.** In scope under DE2: the element, the gates and the platform model.

**THIRTEEN ROWS PREDICT `caught`. EIGHT READ CAUGHT, FIVE NOT CAUGHT -- and all seven sign-mutation rows in section A are among the caught.** That is the first batch this milestone whose headline section goes entirely the right way; batch 28 was four of eleven, 27 was four of eleven, 26 ten of eleven. Four of the seven are shapes the committed test does not carry: the two bending blocks negated, a `Material` with `E = -2.1e+11`, and `local_stiffness` itself replaced by a negating wrapper so `build_superstructure` is the thing asked to refuse.

**The five not caught are the honest remainder and each is routed:** two are NaN shapes whose UNREACHABILITY from the shipped path I measured rather than assumed (C95); two are the missing record of the third reading (R627); one is the seventh clause with no committed failure cell (R626).

```
cmd  grep -c "^id=" tests/corpus/element_psd_half_reach.txt
out  32
cmd  grep -rn "element_psd_half_reach" tests/ scripts/ --include=*.py
out  (no output) -- named by no .py, so it adds no parametrised case
cmd  python -m pytest tests/test_collected_set_golden.py tests/test_marker_exemption_corpus.py
       tests/test_report_vocabulary_corpus.py tests/test_tree_prose_consistent.py
       tests/test_ci_ladder_gating.py -q        with batch 29 in the tree
out  298 passed in 138.81s          exit 0
judge  THE CORPUS COMMIT REDDENS NOTHING, measured and not reasoned -- the same
       298 as batch 28.
```

Every mutation was applied in a scratch harness under the session scratch directory, importing the shipped functions; nothing in the working tree was written. `git status --porcelain --untracked-files=all` was empty before I began, and the only paths I have written in this repository are that corpus file and this verdict.

## On the criterion

**I was asked to rule under CZ0 and I did, and I have no complaint about the criterion this round.** Two blocking findings, each squarely inside a head: R627 is the form of a tolerance and where its justification lives; R626 is what a gate clause claims and whether it can fail. R628 is item 1b of my own instructions and I have said so rather than borrowing a CZ0 head for it. Five closure items are a list, including one against a docstring count and one against a latent NaN path I measured myself before deciding it does not block -- which is the discipline CZ0 asks for, applied to my own findings.

**The one thing I want recorded for Xabier, and this is the second verdict running that it has cost a ruling: CZ1 needs the first-report carve-out in verdict 81 ruling 4.** I have now applied it by hand twice. It is four lines, it narrows nothing, and without it the red at every step boundary has to be adjudicated in prose by whoever happens to be reading. **And one sharpening from this round:** the carve-out as I wrote it assumes state (2) clears itself at the answering report. If no answering report is written, it does not clear, and the clause should say that the state is cleared BY THE REPORT and not by time -- so that 68 red with no revision in sight is read as what it is.

## Next step opens when

**Step 2 stays OPEN. R625 is answered and answered well; the element is sound and the refusal is on the production path.** Three items, and two of them are small.

1. **R628 FIRST, and on its own, because everything else is read through it.** `docs/reports/F3/step-2.md` revised to `Answers: verdict 81 @ 4add9d5`, with R624 DECLARED as with Xabier, R625 and R626 answered site by site, and section 3 fourth row corrected or withdrawn. **It does not wait on R624 and it clears 68 red tests.** Do that one first, as the hand-back offered.
2. **R627 -- the third reading goes into the entry that already enumerates its readings**, with the band figure and the insensitivity window, two numbers and a pointer rather than a table. No value moves. The docstring stops being the home of the justification.
3. **R626 -- the seventh clause gets a cell that shows it raising, and each of the three clauses gets its own solved boundary from both sides.** Every edge is measured and written above; nothing has to be re-derived.

**R624 remains with Xabier and is not step 2 work.** If it is answered by deriving `RIGID_MODE_EXACTNESS` for the element-local quantity, the window is the one I published last round; if by separating the two subjects in writing, the empty-window measurement goes beside the refusal. **Either way, say which the day it is decided**, because R627 lands in the same file and the two edits are cheaper together than apart -- though R627 does not depend on it and must not wait for it.

**Do NOT spend a round on anything under `## Closure items`.** Fix the list once in the closure commit. **I will not re-review it item by item**, and under CZ0 I have not re-reviewed C88 or C89 against my own section 5 this round either.

**CZ1, as verdict 81 ruled it and as I apply it again.** Verify the closure commit after it exists. If the only red at that commit is the step-pairing class and the states cascading off it, record it with the `FAILED` list pasted and proceed; any other red is CZ1 (iv) unchanged.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the code-check screen 28 October. **I have no measurement that contradicts any of them**, and the ladder job is green on CI at this commit, which is the one that would. The three items above are a revision, a paragraph and one test function; none is a day of work. **DZ7c is not triggered and I am not asking for a slip.** The thing that would move the date is R624 waiting on a round rather than on a ruling -- so route it, and do not hold step 2 shut behind it.

**This is round 2 of 3 on step 2 (EB4).** One round remains. **At the third verdict step 2 closes**, and anything still blocking carries by name into step 3 and blocks there -- which for R624 is where it was always going to land.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 2
Reviewed commit: cb03e0a14f5a6d57b0289778c46cfcff16a5020c
Verdict: HOLD
Tests: 3100 passed, 9 failed, 0 skipped   (my own run at the reviewed commit, `python -m pytest -q`, ONE invocation, no split, no exclusion, clean tree, 629.76s -- and NOT the report's subset count)

## Round of 2026-10-01 -- EIGHTY-FIRST verdict, and the FIRST on step 2 (EB4). THE PLAN STOP IS CLEARED. THE GATE IS WHERE THE WORK IS.

**Reviewed commit: `29570e1`.**

**R616 IS ANSWERED AND THE STOP IS LIFTED.** `docs/milestones/F3.md` section 5 is re-locked at `3709cc6`: the near-vertical band sentence is struck in place with the measurement that empties it, and the G2.1 row says what it is measured on. That was the one thing holding step 2 shut and it is shut no longer. Under EB4 the five post-closure rounds count against nothing and step 2 opens with three. **This is round 1 of 3.**

**WHAT I RULED THIS ROUND.** Eight commits, one path class each. I read every line of the diff before opening the report, ran the whole suite myself in one invocation, took CI from `gh` rather than from the paste, reproduced every figure in sections 2, 3, 4 and 5 of the report independently, and then attacked the new gate and the new refusal twenty-two ways. **The report is ACCURATE: every number in it that I re-took, I got.** The findings below are not corrections to its arithmetic. They are what the arithmetic it stopped short of says.

**THE ONE-LINE ANSWER TO THE HAND-BACK'S FIVE.** (1) Holding section 5 was RIGHT, and all three of its options move the wrong variable -- the CEILING is the variable and I have solved for it. (2) The second implementation is the right trade and the agreement test is sound, but it ties ONE of the two quantities and the untied one is where the defect is. (3) Four shapes is not the right set; the placement is correct and I measured it, `0.000000e+00`. (4) CZ1 needs a carve-out for a first report and my wording is below; the red is my own absence and it holds nothing. (5) You have item 5 the right way round -- the four lengths are real at full precision and I confirmed the bijection.

## THE TREE AT 29570e1, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    29570e121d129ee9b0dadfb5ea748e7695ffa678   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 7e5f3fb..HEAD --name-only
out    3709cc6  docs/milestones/F3.md                EB0, the re-lock
out    9c26ffe  CLAUDE.md + docs/SUPERVISOR.md       EB1/EB4, process:
out    6246fbd  scripts/write_verdict.py             EB2, process:
out    ccbd38b  .github/workflows/ci.yml             EB3
out    5d93e6c  .claude/hooks/require-verdict.sh     EC0, process:
out    d0fb2a6  floatfea/ + tests/                   the gate and the refusal
out    d8ea3a3  docs/milestones/F3.md                the step marker
out    a772128  tests/ + docs/reports/               the cited test name
out    29570e1  docs/reports/                        this report
judge  one path class per commit, as stated. No commit touches both floatfea/ and
       docs/reviews/. The three commits touching my own instructions are each a
       standalone process: commit citing its directive -- read line by line below.
cmd    python -m pytest -q
out    9 failed, 3100 passed, 2 warnings in 629.76s (0:10:29)
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    112 files would be left unchanged
cmd    python -m mypy floatfea
out    Success: no issues found in 30 source files
cmd    python -m mypy scripts
out    Found 56 errors in 16 files (checked 21 source files)
judge  the ledgered count in ccbd38b's comment is RIGHT at this commit.
cmd    python scripts/check_carried.py --verdict docs/reviews/F3/step-1.md
         --report docs/reports/F3/step-2.md
out    check_carried: all 24 findings carried          exit 0
judge  ED1(c) confirmed by MY run, not accepted from the paste.
cmd    grep -n "'Answers:" docs/reports/F3/step-2.md
out    3:Answers: verdict 80 @ 7e5f3fb
cmd    git log --oneline -1 7e5f3fb ; git log --oneline -3 -- docs/reviews/F3/
out    7e5f3fb IS the eightieth verdict's own commit AND the newest verdict commit
judge  ITEM 1b SATISFIED. The header names the latest verdict, by the verdict's own
       commit rather than the commit it judged (DX2, C13). One comparison; it passes.
```

## CI, AT THE REVIEWED COMMIT, FROM gh AND NOT FROM THE PASTE (CA2)

```
cmd    gh run list --commit 29570e121d129ee9b0dadfb5ea748e7695ffa678 --json name,conclusion,status,workflowName,databaseId,event,headSha
out    CI  36861000264  push  completed  FAILURE   headSha 29570e1...
cmd    gh run view 36861000264 --json jobs, every job and every step
out    the verification ladder     success   13 steps, all success
out    lint, unit and guards       FAILURE   14 steps: actionlint, ruff,
out                                black --check, mypy and unit tests all SUCCESS,
out                                none skipped; "guards and meta-tests" FAILURE
out    CI determinism -- leg              skipped   0 steps
out    CI determinism -- ten legs agree   skipped   0 steps
judge  THE JOBS RAN -- runner present, 14 steps, 11m40s. NOT CK2: no job here has
       an empty runner_name with a two-second duration and a spending annotation.
       The two skipped jobs are the workflow_dispatch gate under CK0, unavailable
       BY DECLARATION, the same state verdicts 79 and 80 recorded.
cmd    gh run view 36861000264 --log-failed, the FAILED names
out    tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
out    ... and seven more planted states, each carrying either "baseline: expected
out    a clean run" or "a file that is not a numbered step must be stepped over"
cmd    my own whole-suite run at the same commit, one invocation
out    THE SAME NINE, BY NAME. 9 failed, 3100 passed.
```

**AND IT IS ONE CAUSE, WHICH IS MY OWN ABSENCE.** `tests/test_report_carried.py:450-456` asserts `STEP_REPORT == _PAIRED` and fails with "step 2 has a report and no verdict yet ... Invoke the gating-supervisor." Its own docstring at :418-422 names the state: "CB2 made it follow the newest report and that took the suite down whenever a report had no verdict yet, **which is every legitimate boundary**." The eight planted states cascade off it because the harness plants into a tree whose baseline is already red -- the cascade verdict 78 already ruled on.

**SO THE RED IS NOT THE HOLD, AND I SAY SO EXPLICITLY RATHER THAN LETTING CA2 DO IT SILENTLY.** CA2 exists because CI runs on a machine neither party controls and can contradict a local green. Here CI and my own run AGREE, by name, on nine failures whose assertion is that the verdict for this report does not exist. Reading that as (d) makes every step's first report unreviewable -- the no-exit the DD1 entry in `CLAUDE.md` records as costing two verdicts, neither about the work. **The HOLD below rests on three findings that are (a), (b) and (c), and a green CI would change none of them.**

**AND I MEASURED WHAT THIS VERDICT DOES TO THE SUITE, which is not what I expected and is worth more than the ruling.** Taken with `docs/reviews/F3/step-2.md` written into the tree, before it was committed:

```
cmd    python -m pytest "tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on" -q
out    1 passed in 0.15s
judge  CONFIRMED -- the verdict is what clears the nine. The summons is answered.
cmd    python -m pytest tests/test_report_carried.py -q, same tree
out    63 failed, 142 passed in 4.77s
out    57 x test_every_named_site_is_touched_or_declared[R616..R626-<site>]
out     3 x test_the_report_carries_the_finding
out     1 x test_the_CI_section_is_about_the_REVIEWED_commit
out     1 x test_the_Carried_table_is_what_the_generator_produces
out     1 x test_the_generator_would_catch_a_row_under_the_wrong_number
judge  THE PAIRING GUARD CLEARS AND SIXTY-THREE OTHERS OPEN. The suite is red on
       BOTH SIDES of a step boundary: before the verdict because the verdict does
       not exist, after it because the report answering it does not. The green
       window is only after the ANSWERING report lands.
judge  AND THE SECOND HALF HAS NEVER APPEARED IN A VERDICT, because the reviewer
       runs the suite at the JUDGED commit, before writing -- verdict 80's
       `2868 passed, 0 failed` was taken at `ec713d2`, which precedes `7e5f3fb`. So
       this state has existed at every step boundary in this milestone and nobody
       has measured it. It is the other half of R615's window, and it is why my
       ruling-4 clause below covers both sides rather than only the first.
```

The planted-state half needs the commit -- `tests/test_report_guard_states.py` clones the repository, so it cannot see an uncommitted verdict. That one measurement, and only that one, is taken after this file exists and goes in the hand-back.

## Carried

* **R616 / R613 -- ANSWERED at `3709cc6`, and the STOP IS LIFTED.** Verified line by line rather than taken from the report: section 5 now carries "WHAT THIS GATE IS MEASURED ON -- RE-LOCKED (EB0)", the band sentence is struck in place with `max abs dz = 0.0` and `within 15 deg of vertical  0` beside it, the gate row reads "Those orientations are all one orientation (EB0)", and the rigid link is named as outside the gate's subject. That is exactly verdict 80's condition 1. **R616 closes here and carries no further.**
* **R612 -- closed at verdict 79, still closed.** `ruff`, `black --check` and `mypy floatfea` clean at this commit, and CI's `ruff` and `black --check` steps both SUCCEEDED in run 36861000264.
* **R611, R617 -- withdrawn, and they stay withdrawn.** Nothing this round reopens either.
* **R614 -- closed by being on the page.**
* **R610, R615 -- ledger lines, unchanged, no work asked.** Third and second instance; I spend no more than this line on either.
* **R618 / C80 -- ANSWERED at `d0fb2a6`.** The word "linear" is gone from `floatfea/model/platform.py` and the entry reads "IT IS NOT LINEAR IN f ON THE PLATFORM (C80, R618)" with the `slack/f` row and the `1.80x` spread, naming the hubs as the exactly-linear case. The ruling it supports is untouched, as I said it would be.
* **R619 / C81 -- ANSWERED at `d0fb2a6`.** The sentence reads "THE SLACK IS REPORTED IN assumptions, NOT findings (C81, R619)" and says both tuples are empty at the shipped configuration.
* **R620 / C83 -- ANSWERED at `d0fb2a6`**, by the route BI3 prescribes: the docstring carries the numbers it needs and points at the report section rule regenerates, instead of carrying a table nothing regenerates.
* **R623 / C84 -- ANSWERED at `d0fb2a6`.** `tests/verification/rung3/test_platform_skeleton.py:488-497`: the DZ2 comment names the typed plan centre as the third source and says `joint_plane_z` is the deck's own joint elevation. More than the four words I asked for, and correctly more.
* **R621 / C79 -- ANSWERED in prose at `29570e1`**, section 9: `1 failed, 2 passed` replaces "twenty-two others".
* **R622 -- LATER, and correctly so.** It was written as F4's to answer and the report routes it there. Nothing owed inside this step.
* **C75 -- CLOSED. C75b -- ANSWERED at `ccbd38b`, both halves measured.** The workflow runs `ruff check floatfea tests scripts` and `black --check floatfea tests scripts` and both steps succeeded on CI at the reviewed commit. The `mypy` half is ledgered AT THE SITE WITH ITS REASON AND ITS COUNT, and the count is right: `Found 56 errors in 16 files`. `run_rung.sh` ledgered too. **That is the right shape -- the item asked for the pathspec or the exclusion written down with its reason, and this is the second.**
* **C74 -- STILL OPEN, closure.** Step 1's generated CI section stays anchored on verdict 74 at a failed run, by CO1's design, and step 1 is closed at PASS so its report is not edited. Ledgered.
* **C76 -- STILL OPEN, closure.** The marker-count clause counts plans, not markers per plan. Unchanged, holding nothing.
* **C77 answered with C79 as its correction. C78 ledger line. C82 wording, recorded in section 9. C85 recorded as asked** -- and I re-ran both uncollected resolvers by hand this round; `scripts/check_carried.py` is the one I used for ED1(c) above.
* **C58 to C64, C65 to C73, C40, C56(iii), C56(iv), C57** -- as ruled at verdicts 77, 79 and 80. Nothing in these eight commits touches any of them.

## THE FIVE RULINGS THE HAND-BACK ASKED FOR

**1. SECTION 5 -- HOLDING IT WAS RIGHT, AND ALL THREE OPTIONS MOVE THE WRONG VARIABLE.** Holding was right twice over: a tolerance decision is not the implementer's to take mid-step, and declining to register a counter under a size that cannot see the defect is exactly the restraint `CLAUDE.md` asks for. But all three options assume the INJECTION SIZE is the variable and the ceiling is fixed. It is the other way round, and the constant's own entry says so:

```
cmd    sed -n 347,353p floatfea/tolerances.py
out    "It is left rather than retired-with-a-marker because F3 asserts the
out     element-local check on every real platform member, and that gate needs a
out     ceiling of this shape -- which will be DERIVED FROM THAT QUANTITY'S OWN
out     MEASUREMENTS, NOT INHERITED FROM HERE."
judge  it was inherited. 1e-15 was measured under the PER-ROW ASSEMBLED form at
       R475, over the corpus of assembled frames. The gate and the refusal shipped
       at d0fb2a6 assert the GLOBAL-NORM ELEMENT-LOCAL form against it. Different
       quantity, same number, no new measurement taken.
```

**And the solve all three options skip. One loop each, at this commit:**

```
cmd    over the SIXTEEN members: solve for the ceilings C that pass the
       defect-free case AND redden all three counters at the declared 1e-14
out    clean worst            3.528257e-19    (C must be ABOVE)
out    dropped_flip           3.656327e-16    (C must be BELOW)
out    wrong_dof_index        9.459456e-15    (C must be BELOW)
out    rotational_block       1.464442e-17    (C must be BELOW)
out    => A WINDOW EXISTS: (3.5283e-19, 1.4644e-17), 41.51x wide
judge  SO NO NEW CONSTANT AND NO NEW INJECTION SIZE IS NEEDED. Option (a)'s row in
       a closed plan and option (b)'s new table in F3.md both answer a question
       nobody has to ask: the declared 1e-14 registers all three counters as soon
       as the ceiling sits inside that window.
cmd    the same solve over the WHOLE admissible band, L/D >= 2 to L/r <= 300, on
       F1:389's recorded section, 194 points
out    worst clean                        5.287607e-18   (C must be ABOVE)
out    weakest rotational_block response  1.571633e-19   (C must be BELOW)
out    => THE WINDOW IS EMPTY
judge  AND THIS IS WHAT SECTION 5 HAS TO SAY. The GATE'S subject is the sixteen
       members (EB0 narrowed it); the REFUSAL'S subject is every deck. One constant
       cannot carry a counter guarantee on the second, because the clean response
       and the counter response move in OPPOSITE directions with slenderness. That
       is a statement about scope, not a number to tune.
```

**Option (c) is the one I would refuse on its face.** An injection size derived at runtime from the bisected edge is a counter sized by the very ceiling it is supposed to be independent of. `tests/test_counters_are_injected.py` cell two exists to require the opposite -- "the counter must be SIZED BY the constant it defends" -- and a runtime-derived size passes that cell vacuously. `WIDEN = 10.0` is not a precedent: `WIDEN` is a fixed factor nothing compares against, not a quantity read back out of the measurement it governs.

**2. THE SECOND IMPLEMENTATION IS THE RIGHT TRADE, AND THE TIE COVERS ONE OF THE TWO QUANTITIES.** Shipping `floatfea/element/rigid.py` rather than re-pointing frozen rung-1 apparatus is correct under DR1 and I would have ruled the same way. The agreement test is sound and the `0.000e+00` is real -- I reproduced it on all sixteen. But:

```
cmd    compare the four function bodies in the two files, name by name, docstrings
       stripped
out    element_rigid_vectors    NOT textually identical -- a different loop form
out    element_homogeniser      NOT textually identical -- a different loop form
out    element_rigid_residual   identical below the docstring
out    seventh_over_epsilon     A DIFFERENT FUNCTION. rung 1 takes (k) and
out                             homogenises by max|K|; the shipped one takes
out                             (k_local, length) and homogenises by S
cmd    read what the gate compares
out    test_G2_1_the_SHIPPED_residual_agrees_with_RUNG_ONEs compares
       element_rigid_residual ONLY
judge  so the module docstring's "rung 1 keeps its own copy ... what ties the two is
       [that test]" is true of the residual and false of the spectral half, and the
       UNTIED half is the one R625 below is about. The trade is right; the tie is
       half a tie; and the half that is loose is the half that is new.
```

**3. FOUR SHAPES IS NOT THE RIGHT SET. THE PLACEMENT IS CORRECT AND I MEASURED IT.**

```
claim  the refusal would land identically in the member loop
cmd    max |local_stiffness(section, body.material, L) - local_stiffness(section,
       S355, L)| over the sixteen members
out    0.000000e+00
cmd    read floatfea/element/beam.py:127-152 for what local_stiffness consumes
out    E, G, A, J, I_z, I_y and kappa. rho appears nowhere in the function.
judge  CONFIRMED, and the placement chosen is the better of the two for the reason
       the comment gives: what is checked is what is shipped. No finding here.
```

The SET is where it falls short, and the missing class is SIGN -- R625. Four shapes that all perturb a magnitude cannot reach a defect that preserves every magnitude.

**4. CZ1 NEEDS A CARVE-OUT FOR A FIRST REPORT. HERE IS MY WORDING, TO CARRY AS THE ORIGINAL WAS CARRIED.** The circularity is real and measured above: step (iii) asks for a green pushed run before the invocation, and at a step's first report the guard that is red is the one asserting that this verdict does not exist.

> **CZ1 step (iii) does not apply to the boundary red a step's own report creates, on EITHER side of the verdict.** Two states, both designed, both self-clearing, and neither is a defect:
>
> **(1) Report written, verdict not yet.** The only failures are `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` and the planted states that cascade off its baseline. The verdict clears them.
>
> **(2) Verdict written, answering report not yet.** The only failures are `test_every_named_site_is_touched_or_declared`, `test_the_report_carries_the_finding`, `test_the_CI_section_is_about_the_REVIEWED_commit`, `test_the_Carried_table_is_what_the_generator_produces` and `test_the_generator_would_catch_a_row_under_the_wrong_number`, each naming a finding or a site of the newest verdict. The answering report clears them.
>
> In either state the run is recorded as RED WITH ITS CAUSE NAMED -- the full `FAILED` list pasted, and the sentence saying which of the two states it is -- and work proceeds. **Any failure outside the state's own list is CZ1 (iv) unchanged**, and "only those" is a claim that carries the `FAILED` list as its command. The reviewer measures state (1) clearing at its verdict commit; the implementer measures state (2) clearing at the report commit.

I have done the reviewer half this round. **I am not editing CZ1 and this is not a HOLD on it** -- it is the disagreement-with-the-criterion channel, said once, leaving the loop.

**5. ITEM 5 IS THE RIGHT WAY ROUND AND I CONFIRMED THE BIJECTION.**

```
cmd    repr(length) and element_rigid_residual, per member, grouped
out    L=50.0                 8.721078e-20   n=4
out    L=25.0                 9.673052e-20   n=7
out    L=25.000000000000004   1.988390e-19   n=4
out    L=25.000000000000007   3.528257e-19   n=1
judge  four lengths, four residuals, one to one, counts 4+7+4+1 = 16. EB0's sentence
       is TRUE at full precision and withdrawing it would have been the error. You
       caught yourself; recorded because the check that looked like a refutation is
       the one that confirmed it.
```

## Findings

**R624. (b, blocking) THE CEILING THE NEW GATE AND THE NEW REFUSAL ASSERT AGAINST IS INHERITED FROM A DIFFERENT QUANTITY, AND THAT CONSTANT'S OWN ENTRY FORBIDS IT. THE CONSEQUENCE IS MEASURED, NOT PREDICTED.** `tests/verification/rung3/test_platform_rigid_modes.py:99` and `floatfea/model/platform.py:311-319` both compare the element-local global-norm residual with `RIGID_MODE_EXACTNESS = 1e-15`, whose "Reason for 1e-15" at `floatfea/tolerances.py:316-328` is measured under the per-ROW assembled form (R475), over assembled corpus frames. `tolerances.py:347-352` pre-registered that F3's gate "needs a ceiling of this shape -- which will be derived from THAT quantity's own measurements, not inherited from here."

```
cmd    the whole admissible section-and-length space: D_o 0.2..6 m, t/D_o
       0.005..0.2, L constrained to L/D >= 2 and L/r <= 300; 1680 points
out    WORST clean residual   1.620063e-17   at D_o 0.20, t 0.0010, L 0.400
out    the ceiling            1e-15          => 61.73x headroom EVERYWHERE
out    SMALLEST seventh/eps   3.849230e+10   at D_o 0.50, t 0.0250, L/r 300.0
out    the bound              199.526        => 1.929e+08x inside
rule   the two shipped assertions, read as refusals over every member a deck can
       describe
judge  so NEITHER HALF OF THE REFUSAL CAN FIRE ON ANY ADMISSIBLE DECK. The only
       thing that can move the residual is a CODE defect in local_stiffness -- which
       makes the counter sizes the whole specification of what this gate is for, and
       two of the three declared ones are blind:
out    dropped_flip      at 1e-14  3.656327e-16 = 0.3656x the ceiling    BLIND
out    rotational_block  at 1e-14  1.464442e-17 = 0.01464x               BLIND
out    wrong_dof_index   at 1e-14  9.459456e-15 = 9.459x                 reddens
cmd    invert and bisect each edge, worst over the sixteen
out    2.735459e-14   1.057143e-15   6.837686e-13
judge  I reproduced the report's figures exactly. What it did not take is the solve in
       ruling 1: over the SIXTEEN the ceiling window is (3.5283e-19, 1.4644e-17),
       41.51x wide; over the ADMISSIBLE BAND it is EMPTY.
```

**Closed when** one of two things, and either is a decision rather than work: **(i)** `RIGID_MODE_EXACTNESS` is derived from the element-local quantity's own measurements and lands inside the 41.51x window, at which point all three counters register at the declared `1e-14` with no new constant and no new table -- the value moves in an existing `F2.md` row, not a new one; or **(ii)** the gate's subject and the refusal's subject are separated in writing, the gate keeping a derived ceiling and the refusal declaring that it carries no counter guarantee across the admissible band with the EMPTY-window measurement beside it. **Either way the three counters F3 section 5 asks for are registered or section 5 is amended to say they cannot be** -- what may not stand is an assertion whose declared counters are two-thirds blind and whose ceiling nobody measured for it.

**R625. (a and c, blocking) THE SHIPPED REFUSAL ACCEPTS AN INDEFINITE ELEMENT STIFFNESS. THREE SIGN ERRORS, EACH INJECTED ALONE, EACH PASSING BOTH HALVES.** `floatfea/element/rigid.py:106-119`: `seventh_over_epsilon` sorts `np.abs(np.linalg.eigvalsh(khat))`, so a large NEGATIVE seventh eigenvalue reads as a large positive one. And a symmetric sub-block negated still annihilates every rigid motion -- a rigid rotation has `theta_A == theta_B`, so the torsion block cancels whatever its sign -- so the residual half does not see it either.

```
cell   one shape at a time into k_local for platform:hub1_arm, L = 50 m, nothing
       else touched, then floatfea.model.platform.check_rigid_modes called
out    clean                        residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    torsion sub-block negated    residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    axial sub-block negated      residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    whole matrix negated         residual 8.721e-20  seventh/eps 9.3791e+11  ACCEPTED
out    torsion DIAGONALS only       residual 2.083e-04                          REFUSED
out    signed eigenvalues, homogenised: clean has 0 negatives; the three accepted
out    cases have 1, 1 and 6, the largest at -2.2951e+06 on a matrix of norm 1.1e10
rule   the two shipped assertions, and the check_rigid_modes docstring's claim that
       "no OTHER deck can produce a member that is not [sound]"
judge  an element with negative axial or torsional stiffness RELEASES energy under
       deformation. "The whole matrix negated" is the sign-convention inversion
       CLAUDE.md non-negotiables name by name. Three of four pass, and the one that
       is caught is caught by the residual, not by the half that exists for this.
cmd    does anything else in the repository reject an indefinite element stiffness
out    NO. Every spectral read in rung 1 and rung 3 takes np.abs; rung 2's
       test_consistent_mass.py:497 and :747 use np.clip(..., 0.0, None), which
       DISCARDS the sign; the only eigenvalue sign test in floatfea/ is on INERTIA,
       at io/reader.py:314.
judge  AND THE DOCSTRING SENTENCE THAT WOULD HAVE REASSURED A READER IS THE ONE THIS
       REFUTES: "why the residual half is the thing that catches a structural sign
       flip, is in rung 1's copy" (rigid.py:100-103). It does not catch these three.
```

**Closed when** the refusal rejects an indefinite element, and the measurement below says it needs NO new constant -- `RIGID_MODE_BOUND` read as a floor on the SIGNED minimum separates clean from defect by twelve to fifteen decades:

```
cmd    lambda_min(k_hat) / (||k_hat|| * eps), the same unit the bound is already in
out    the sixteen members          -0.0715 .. -0.0021
out    the whole admissible band    -0.7908 .. +0.0001     (194 points)
out    torsion sub-block negated    -9.379115e+11
out    axial sub-block negated      -4.503527e+15
out    whole matrix negated         -4.503527e+15
rule   lambda_min / (||k_hat|| * eps) >= -RIGID_MODE_BOUND
judge  every clean case passes by 252x; all three defects are refused by 4.70e+09x
       or more. One comparison, inside the assertion that is already there, on the
       constant that is already there. NOT a new gate and NOT new apparatus.
```

The alternative close is narrower and I will take it: the two docstring sentences are reduced to what was measured and the gate's own comment says the pair is blind to sign. **What may not stand is a shipped refusal that accepts negative stiffness while its docstring says no other deck can produce an unsound member.**

**R626. (c, blocking) THE REFUSAL IS A GATE HALF AND NOTHING COMMITTED SHOWS IT EVER REFUSES. ITS SIBLING IN THE SAME MODULE IS TESTED ON BOTH SIDES OF BOTH BOUNDARIES.** F3 section 5 makes "the builder refuses a platform that fails it" half of what G2.1 asserts, so this is a gate assertion and not apparatus.

```
cmd    grep -rn "check_rigid_modes" tests/
out    tests/verification/rung3/test_platform_rigid_modes.py:26   a docstring line
out    tests/verification/rung3/test_platform_rigid_modes.py:224  a comment line
out    no import, no call, no pytest.raises, anywhere in tests/
cmd    grep -rn "check_limits" tests/
out    test_platform_skeleton.py:696  check_limits("just inside", 2.0 * D)
out    test_platform_skeleton.py:698  pytest.raises ... ("stubby", 1.99 * D)
out    test_platform_skeleton.py:705  check_limits("just inside", 300 * r)
out    test_platform_skeleton.py:707  pytest.raises ... ("slender", 1.01 * 300 * r)
rule   a gate carries its own failure -- break the claimed property and confirm the
       assertion goes red
judge  check_limits, the refusal shipped in the SAME module for F3 section 2, is
       solved at both boundaries from both sides. check_rigid_modes, shipped in the
       same step, has nothing. The only evidence the refusal fires is the report's
       section 3 cell, and that cell is a scratch measurement no committed code
       reproduces.
cmd    and one row of that cell does not reproduce: the fourth shape, "seventh_mode
       REFUSED, injected alone at 1e-8 of max|k_e|"
out    NO SUCH SHAPE EXISTS IN THE REPOSITORY -- scripts/rigid_counter_response.py
out    injected() raises SystemExit on anything but the three
out    AND NO 1e-8-of-max|k_e| PERTURBATION AT THE TORSIONAL BLOCK CAN REACH THE
out    BOUND: rotational_block at 1e-8 reads 9.3791e+11 against 199.526, green, and
out    the retained-torsion fraction at the boundary, bisected, is 2.127342e-10 --
out    9.67 DECADES below 1e-8
judge  so the one row offered as evidence that the SEVENTH-MODE half of the refusal
       fires is UNVERIFIED, and the size attached to it is refuted. The half does
       fire -- I made it, by removing the torsion entirely, 4.8647e-02 -- but that is
       my measurement and not the report's.
```

**Closed when** `tests/verification/rung3/` carries a cell that calls `check_rigid_modes` and asserts it RAISES, in the shape `check_limits` already uses beside it: for each half, one input just inside and one just outside, with the boundary solved rather than sampled. **Not new apparatus** -- it is a verification test of shipped `floatfea/` behaviour, in the file class that already holds exactly this, and DR1 freezes guards and meta-tests, not rung tests. And the `seventh_mode` row either names a shape that exists in the tree with its real size, or goes.

## Closure items

Named, not re-reviewed, none of them holding anything. Fix the list once in the step's closure commit and verify it AFTER it exists (CZ1), with my ruling-4 carve-out applied to the pairing guard if it is the only red.

* **C86.** `floatfea/element/rigid.py:18-23` -- the module docstring says rung 1 "keeps its own copy" and that the agreement test "ties the two". It ties `element_rigid_residual` and not `seventh_over_epsilon`, which is a different function in the two files. **Closes when** the sentence names the quantity it covers.
* **C87.** `floatfea/element/rigid.py:100-103` -- "why the residual half is the thing that catches a structural sign flip, is in rung 1's copy". Refuted by R625's three shapes. Folded into R625's close; listed here so the wording is not forgotten if R625 is closed by the signed read alone.
* **C88.** `docs/milestones/F3.md` section 5, mine under EB0, two provenance defects I am recording against myself. **(i)** "Every figure below is produced by `PYTHONPATH=. python scripts/rigid_counter_response.py` and the geometry and residual sweep in `tests/verification/rung3/`" -- that script reads the rigid-body CORPUS and prints counts at `SIZE = 1e-8`; it never builds the platform, and no sweep in `tests/verification/rung3/` prints the per-member table. **(ii)** the bisected edges published there, `5.286e-14 / 1.094e-15 / 2.643e-12`, are not reproducible as "worst over the sixteen members": at this commit that solve gives `2.735459e-14 / 1.057143e-15 / 6.837686e-13`, which is what the report prints and what I measured. The published triple looks like the WEAKEST member's edge rather than the worst. **Closes when** section 5 either names the command that produces its table or carries the figures the report's own run gives. Not the implementer's file; recorded for whoever next edits it.
* **C89.** `docs/milestones/F3.md` section 5's judgement "SIZE sits four to seven decades past every boundary" is measured at `1e-8`, which is `scripts/rigid_counter_response.py`'s not-a-tolerance probe size and NOT `RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1e-14`, the repository's declared counter size. At the declared size two of three are blind. The sentence that follows -- "what make a correction sufficient here and a new gate unnecessary" -- is the conclusion R624 holds on. Same file, same owner.
* **C90.** `tests/verification/rung3/test_platform_rigid_modes.py:94-96` and `:122-124` -- "a pure number because the residual is dimensionless and relative to the quantity compared". Dimensionless, yes; unit-INVARIANT, no. The same member in millimetres, consistently scaled, moves the residual by `1.1110x`, `3.9264x` and `2.5417x` at `L = 50`, `25` and `5` m. `seventh_over_epsilon` is exactly invariant, `1.000000`. It passes the unit-scaling test vacuously today on a `2834x` margin; inside R624's `41.51x` window a `3.93x` sensitivity is a tenth of the room. **Closes when** the comment says dimensionless rather than implying invariant, and R624's derivation accounts for it.
* **C91.** `tests/verification/rung3/test_platform_rigid_modes.py:217-218` -- "`tests/test_report_carried.py`'s sibling `test_every_declared_tolerance_appears_in_the_plan`". That test is in `tests/test_plan_matches_tolerances.py:98`. Same directory, different file; a reader following the name goes to the wrong one.
* **C74, C76, C78, C82, C85, R610, R615** -- carried unchanged, see `## Carried`.

## Tolerances touched

```
cmd  git diff 7e5f3fb..HEAD -- floatfea/tolerances.py
out  no output
cmd  git diff 7e5f3fb..HEAD --stat -- floatfea
out  floatfea/element/rigid.py     115 +     a new module
out  floatfea/model/platform.py     91 +, 8 -
cmd  git diff 7e5f3fb..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  no output
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py            one conftest in the tree; no rung carries its own
```

**NO VALUE MOVED, AND THAT IS THE FINDING RATHER THAN THE CLEARANCE.** No tolerance, no golden, no parametrisation and no `_COUNTER` changed, and no counter was registered -- which is correct restraint and is why R624 is a HOLD on a DECISION rather than on an edit. No conftest and no plugin changed, so nothing new can rewrite what `scripts/run_rung.sh` reads and the CH2/CI0 reading has nothing to read this round.

**TWO CONSTANTS CHANGED THEIR SUBJECT WITHOUT CHANGING THEIR VALUE**, which is the case this section exists to notice and the one a diff of the file cannot show:

| constant | value | what asserted it before | what asserts it now | justification located |
|---|---|---|---|---|
| `RIGID_MODE_EXACTNESS` | `1e-15`, unchanged | nothing -- a diagnostic since DI0/R530 | the rung-3 gate at :99 AND the shipped refusal at platform.py:312 | `F3.md` section 5's residual sweep -- a measurement of the clean response, NOT a derivation of the ceiling, and `tolerances.py:347-352` asks for the derivation. **R624.** |
| `RIGID_MODE_BOUND` | `199.526231496888`, unchanged | rung 1, on the ASSEMBLED `K / max abs K` | the rung-3 gate at :125 AND platform.py:325, on the ELEMENT-LOCAL `S`-homogenised quantity | `F3.md` section 5 gives the margin `4.70e+09x` and no counter in the new quantity. The registered `rigid-body seventh under the bound` counter in `tests/test_counters_are_injected.py` defends rung 1's gate, not this one -- and I measured that no perturbation at the three counter sites, at any size up to `1.0`, can redden the new half. **R624, and the signed read in R625 is what gives this constant a sensitive direction.** |

## My own instructions (4b), read line by line

```
cmd  git diff 7e5f3fb..HEAD --stat -- .claude docs/SUPERVISOR.md
out  .claude/hooks/require-verdict.sh | 40 +++++++++++++++++++++++++++++++++++----
out  docs/SUPERVISOR.md               | 41 ++++++++++++++++++++++++++++++++++++++++
cmd  git log --oneline 7e5f3fb..HEAD --name-only, the two commits that touch them
out  9c26ffe  CLAUDE.md + docs/SUPERVISOR.md only      process:, cites EB1 and EB4
out  5d93e6c  .claude/hooks/require-verdict.sh only    process:, cites EC0
judge  BOTH ARE STANDALONE process: COMMITS CITING THEIR DIRECTIVE, and neither also
       touches floatfea/ or tests/. NO STOP-CLASS PROCESS FINDING.
judge  CONTENT, read line by line rather than by stat. docs/SUPERVISOR.md gains CZ1
       and EB4 and loses nothing -- 41 inserted, 0 deleted, and the CZ1 text is the
       wording I proposed, unparaphrased. require-verdict.sh changes the milestone
       field from $2 to $3 and makes a path it cannot read a milestone from BLOCK
       rather than rank at zero. That is STRICTER, not looser: before, every report
       ranked at milestone 000 and docs/reports/F2/step-7.md beat
       docs/reports/F3/step-1.md on 7 > 1, so the hook read none of F3's seven
       verdicts. NO GUARD IS REMOVED BY EITHER COMMIT. Verified by reading both
       diffs in full, not by counting lines.
cmd  and the byte-identity EB1 claims between the two copies of the CZ1 text:
     slice each file from the CZ1 heading to the next heading and compare
out  CLAUDE.md 1817 bytes ; docs/SUPERVISOR.md 1817 bytes ; identical True
judge  CONFIRMED. The hand-back says 1527, which is a different slice of the same
       block -- my boundaries include the heading line and the italic attribution.
       Identity is what EB1 claimed and identity is what I measured.
```

## The adversarial corpus (BE3)

`tests/corpus/element_local_g21_refusal_reach.txt`, batch 28, committed separately from this verdict at `cb03e0a`. **THIRTY ENTRIES, ALL THIRTY UNSEEN -- a new file on a surface no corpus has touched.** In scope under DE2: the element, the gates and the platform model, and nothing about apparatus.

**Ten entries carry a mutation. FOUR CAUGHT, SIX NOT CAUGHT.** The six are not reach -- they are the subject the gate names: three sign errors that leave the element indefinite, one torsion loss of nine decades, and two of the three counters F3 section 5 asks for at the size this repository declares. `expect=` is the prediction written before each run; `measured=` is what the shipped pair did. Against four of eleven caught in batch 27, ten of eleven in batch 26, twelve of thirteen in batch 25.

**This is the first corpus round in five whose misses are inside the gate's own stated subject rather than outside it**, and that is why R625 and R624 block where batch 27's eight invisible deck mutations did not.

Every mutation was applied in a scratch harness under the session scratch directory, importing the shipped functions; nothing in the working tree was written. `git status --porcelain --untracked-files=all` was empty before I began and the only paths I have written in this repository are the two corpus files and this verdict.

**AND THE CORPUS COMMIT REDDENS NOTHING, measured rather than reasoned.**

```
cmd  grep -rn for a glob over tests/corpus in tests/ and scripts/
out  none -- every corpus reader names one file by name, as verdict 80 recorded
cmd  grep -rn "element_local_g21_refusal_reach" tests/ scripts/ --include=*.py
out  named by no .py
cmd  python -m pytest tests/test_collected_set_golden.py tests/test_marker_exemption_corpus.py
       tests/test_report_vocabulary_corpus.py tests/test_tree_prose_consistent.py
       tests/test_ci_ladder_gating.py -q        with batch 28 in the tree
out  298 passed in 131.28s          exit 0
judge  a .txt file adds no parametrised case -- the citation guard scans .py prose
       inside backticks only -- so batch 28 moves no collected count and no assertion.
```

**EC4 IS DONE, in the same commit.** `tests/corpus/platform_skeleton_builder.txt:136` recorded the smallest of the four distinct residuals as `7.18521e-20`; re-measured at this commit it is `8.721078e-20`, the other three and the worst agree exactly, and the `2834.26x` margin is set by the worst and is unaffected. The row now carries the corrected figure and says it was corrected here and why. The file is mine under DE2 and DR1; the request was the right way to raise it.

## On the criterion, and the one thing above me

I was asked to rule under CZ0 and I did. **Three findings are blocking and each is squarely inside (a), (b) or (c):** R624 is a tolerance value and the form of one, including a counter and how it is injected; R625 is a defect in `floatfea/` and a gate assertion's quantity; R626 is what a gate half claims and whether it can fail. Six more findings are closure items and I have put them in a list instead of spending a round on them -- including two against my OWN section 5, which I am recording rather than re-litigating.

**NOTHING HERE IS A COMPLAINT ABOUT THE CRITERION.** CZ0 worked this round exactly as intended: six prose findings that would have consumed a round under the old head are a list, and the round went to the element instead. That is the first time this milestone it has paid out that way, and it is worth saying so.

**The one thing I want recorded for Xabier, and I say it once: CZ1 needs the first-report carve-out in ruling 4.** It is a four-line clause, it narrows nothing, and without it every step's first report arrives with an unsatisfiable precondition -- which is the species of defect DR1's own record says produced a finding against itself in four consecutive rounds. I have not edited CZ1; it is the implementer's to carry, as the original was.

## Next step opens when

**Step 2 stays OPEN. R616 is answered, the STOP is lifted, and the plan is no longer what blocks -- the gate is.** Three items, and two of them are decisions rather than code.

1. **R624 -- the ceiling is derived for the quantity it bounds, or the two subjects are separated in writing.** Either close is acceptable and both are measured above. If the derivation route is taken, the 41.51x window `(3.5283e-19, 1.4644e-17)` is where the value lands and the declared `1e-14` then registers all three counters with no new constant and no new plan table -- **which retires all three of section 5's options, so do not spend a round choosing between them.** If the separation route is taken, the EMPTY-window measurement goes beside the refusal. **Either way, F3 section 5's request for three registered counters is satisfied or section 5 says why it cannot be.**
2. **R625 -- the refusal rejects an indefinite element stiffness.** The signed `lambda_min / (||k_hat|| * eps) >= -RIGID_MODE_BOUND` read is measured, needs no new constant and no new gate, and separates clean from defect by twelve to fifteen decades. Whatever form is chosen, the three shapes in R625's cell are the acceptance test and the two docstring sentences are reduced to what holds.
3. **R626 -- `check_rigid_modes` gets a committed cell that shows it RAISING**, in the shape `check_limits` already uses eight lines away, with each boundary solved rather than sampled; and the report's `seventh_mode` row names a shape that exists with its real size, or goes.

**Do NOT spend a round on anything under `## Closure items`**, including C88 and C89 which are against my own section 5. Fix the list once in the closure commit.

**CZ1, as I have ruled it.** Verify the closure commit after it exists. If the only red at that commit is the step-pairing guard and the states that cascade off it, record it with the `FAILED` list pasted and proceed -- that is ruling 4 and it applies to you now, not after Xabier answers. Any other red is CZ1 (iv) unchanged.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the code-check screen 28 October. **I have no measurement that contradicts any of them.** The report says step 3 is "the counter registration and F3's closure artifact, 7 October" and that is where R624 and R625 land naturally; what I have added to that step is the derivation and one assertion, not a new gate, and R626 is a test in a file that already has its template. **DZ7c is not triggered and I am not asking for a slip.** The one thing that could move the date is R624 answered by inventing a new constant and a new plan table instead of deriving the one that exists -- and if that is the choice, say so the day it is made.

**This is round 1 of 3 on step 2 (EB4).** Two rounds remain. I would rather spend the second on R625's acceptance cell than on anything in the closure list, and I will not re-review the closure list item by item.
