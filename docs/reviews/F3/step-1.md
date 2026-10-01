# Review — F3 step 1
Reviewed commit: ec713d275b270ab499ccb04eb0a5277d00be02e5
Verdict: STOP
Tests: 2868 passed, 0 failed, 0 skipped   (my own run at the reviewed commit, `python -m pytest -q`, one invocation, no split, no exclusion, clean tree, 1326.42s, exit 0)

## Round of 2026-09-30 -- EIGHTIETH verdict. THE FOUR EA COMMITS ARE SOUND AND NOTHING IN THEM BLOCKS. THE STOP IS R616, UNCHANGED, AND IT IS STILL NOT THE IMPLEMENTER'S TO ANSWER.

**Reviewed commit: `df2c170`.**

**F3 step 1 remains CLOSED at PASS (DD1, verdict 76).** Nothing here reopens it. What is held
is the OPENING of step 2, and it is held on exactly one thing: `docs/milestones/F3.md`
section 5, which is R616. Nothing in the four EA commits touches section 5, so nothing in
them could have changed that, and nothing in them did.

**WHAT I RULED ON THIS ROUND.** Four commits, one path class each, after verdict 79's judged
commit. I read every line of the diff before the hand-back, ran the suite myself, took the
CI result from `gh` rather than from the paste, and measured the three things the hand-back
asked me to rule plus the one number it declined to assert a cause for. I also attacked
G3.1a with twelve planted defects, which is where the one new thing this round found came
from.

**MY ANSWER, IN ONE LINE EACH.** EA0: the implementer is right and the directive is wrong --
the detection is live and I proved the planted state depends on it. EA2's four remaining
sites: the implementer is right, and a ruling of mine already on the frozen list says so.
The dry run: the tree is clean of it, measured with `--untracked-files=all`. The delta: it
is EA4 and only EA4, two new citation cases, and the implementer's own suspicion is refuted.

## THE TREE AT df2c170, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    df2c170b598d5d93d050988ac24891199a36ca1b   both -- pushed, HEAD of F3
cmd    git status --porcelain --untracked-files=all
out    (no output, before any work of mine)
cmd    git log --oneline 7b44545..df2c170 --stat
out    ecf8e70  tests/test_report_numbers_are_sourced.py       30 +, 5 -
out    db6a099  scripts/carried_table.py, check_carried.py, ci_section.py   55 +, 5 -
out    3d818b6  floatfea/model/platform.py                     14 +, 1 -
out    df2c170  tests/verification/rung3/test_platform_skeleton.py   24 +, 0 -
judge  one path class per commit, as stated. No commit touches both floatfea/ and
       docs/reviews/, and no commit touches .claude/ or docs/SUPERVISOR.md.
cmd    python -m pytest -q
out    2868 passed, 2 warnings in 1326.42s (0:22:06)      exit 0
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!          (I added scripts/ to the pathspec myself)
cmd    python -m black --check floatfea tests
out    89 files would be left unchanged
cmd    python -m black --check scripts
out    21 files would be left unchanged           C75 is CLOSED, measured here
cmd    python -m mypy floatfea
out    Success: no issues found in 29 source files
```

**CI, AT THE REVIEWED COMMIT, FROM `gh` AND NOT FROM THE PASTE (CA2).**

```
cmd    gh run list --commit df2c170b598d5d93d050988ac24891199a36ca1b --json name,conclusion,status,workflowName,databaseId,event,headSha
out    CI  36801064334  push  completed  success   headSha df2c170...
cmd    gh run view 36801064334 --json jobs, every job and every step
out    the verification ladder     success   13 steps, all success
out    lint, unit and guards       success   14 steps: actionlint, ruff, black --check,
out                                          mypy, unit tests, guards and meta-tests --
out                                          ALL SUCCESS, none skipped
out    CI determinism -- leg              skipped   0 steps
out    CI determinism -- ten legs agree   skipped   0 steps
cmd    gh run view 36801064334 --log, the count lines
out    unit tests             88 passed in 0.68s
out    guards and meta-tests  959 passed, 1 warning in 584.93s (0:09:44)
out    ladder 1, 2, 3, 6, 4   run_rung: OK -- 1 directory ran, each
out    ladder 5               run_rung: OK -- 0 directories ran    empty by design
judge  GREEN on both machines. The two skipped jobs are the `workflow_dispatch` gate
       under CK0 -- unavailable BY DECLARATION, which is neither red nor CK2: no job
       here has an empty runner_name with a two-second duration and a spending
       annotation. Same state verdict 79 recorded, same reason.
```

## Carried

* **R616 -- STILL OPEN, STILL THE STOP, AND UNTOUCHED BY THIS ROUND.** `docs/milestones/F3.md`
  section 5 is byte-identical since verdict 79: `git diff 7b44545..df2c170 -- docs/` returns
  the verdict file and nothing else. It is not the implementer's and no verdict of mine can
  close it. It carries by name into step 2 the moment step 2 opens.
* **R612 -- closed at verdict 79.** Unchanged, and the lint path is green again at this commit
  including `scripts/`.
* **R611 -- item 1b applied, and the answer is the same as verdict 79's.** There is no new
  report revision this round, so there is no new `Answers:` claim to check. The newest
  revision still reads `Answers: verdict 75 @ 2f068c4`:

```
cmd    grep -n "^Answers:" docs/reports/F3/step-1.md | tail -1
out    618:Answers: verdict 75 @ 2f068c4        (Revision 3, the newest)
cmd    git log -1 --format=%h -- docs/reports/F3/step-1.md
out    8e4238d
cmd    git merge-base --is-ancestor 8e4238d 7e32070
out    YES -- the report commit precedes the verdict commits 77, 78 and 79
judge  the exemption at tests/test_report_carried.py:394-400 applies and the whole tree is
       0 failed. This is the legitimate boundary, not a report ignoring a verdict. Bumping
       the header was measured at 33 failed in verdict 78 and is still the wrong move. NOT a
       finding, recorded because item 1b says to compare and say so.
```

* **R613, R614, R617 -- as recorded at verdict 79.** R613 is R616. R617 stays withdrawn.
* **R615 and R610 -- closure items, unchanged.** This round is a third instance of R615's
  window and I am not spending a line on it beyond saying so.
* **C74 -- STILL OPEN.** The report was not revised in these four commits, so the generated CI
  section still anchors on verdict 74 at 228bdfb, a failed run. It closes when
  `scripts/ci_section.py` is re-run at the commit publishing the next revision.
* **C75 -- CLOSED.** `python -m black --check scripts` is `21 files would be left unchanged` at
  `df2c170`, measured above. `db6a099` reformatted `scripts/carried_table.py`, which the step's
  closure commit `8e4238d` had broken. **The PATHSPEC half is NOT closed and I am not asking for
  it again**: `ruff check floatfea tests`, `black --check floatfea tests`, `mypy floatfea` still
  leave `scripts/` outside CI. That stays a closure item (C75b below).
* **C76 -- STILL OPEN.** The marker-count-per-file clause is not in the tree.
  `tests/test_report_carried.py:471-483` still asserts one PLAN and not one MARKER, and
  `re.search` still returns the first. Unchanged and holding nothing.
* **C77 -- ANSWERED by `ecf8e70`, with one correction below (C79).** Verified: the module
  imports and reports instead of failing to collect.
* **C78 -- ledger line, unchanged.** No code change asked.
* **C58 to C64, C59/R605, C65 to C73, C40, C56(iii), C56(iv), C57** -- as ruled at verdicts 77
  and 79. Nothing in these four commits touches any of them.

## THE FOUR RULINGS THE HAND-BACK ASKED FOR

**1. EA0 -- THE IMPLEMENTER IS RIGHT AND THE DIRECTIVE IS WRONG. DO NOT DELETE THE STATE.**
I did not take this on the reading of the code. I ran the ablation, in a `git clone` under the
session scratch directory, and the state turns out to depend on the detection exactly as it
should:

```
claim  the `git cat-file -e` detection is live, and the planted state measures it
cmd    tests/test_report_carried.py:320, read at df2c170
out    out = subprocess.run(["git", "cat-file", "-e", ANSWERED], cwd=ROOT, capture_output=True)
out    assert out.returncode == 0, ...   -- live, three lines of message beneath it
cmd    python -m pytest "tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]" -q
out    1 passed in 10.18s
cell   THE ABLATION, one variable. In a clone at df2c170, plant the bad sha by hand
       (`Answers: verdict 28 @ deadbee`) and run the guard; then neuter the ONE assert
       above to `assert True` and run it again. Nothing else changed.
out    detection live:  154 failed, 192 passed -- and FAILED ... test_the_report_names_the_verdict_it_answers
out    detection inert: 153 failed, 193 passed -- and that name is NO LONGER among the failures
rule   `_assert_diagnosis` at tests/test_report_guard_states.py requires
       `test_the_report_names_the_verdict_it_answers` to be among the failed names and
       `test_the_diff_the_site_check_needs_is_available` NOT to be. The first clause goes red
       the moment the detection is removed.
judge  CONFIRMED, measured rather than argued. The state is a WORKING negative control whose
       green is a function of the detection. Deleting it under EA0 would have deleted the one
       thing in the tree that measures that this detection fires and fires by name. The
       implementer invoked the directive clause that my verdict governs where it differs, and
       that was the correct call. **EA0 is withdrawn on my authority; the premise it rests on
       is a diagnosis that was already refuted.**
```

**2. EA2's FOUR REMAINING SITES -- THE IMPLEMENTER IS RIGHT TO HAVE DECLINED, A RULING OF MINE
ALREADY SAYS SO, AND THE MEASUREMENT IS WORSE THAN THE READING CLAIMED.** Routing them does not
give two vacuous and two red. It gives FOUR RED, and two of those are collection errors:

```
claim  what each of the four does when its hardcoded F2 path is routed at F3
cell   one clone at df2c170, the F2.md and F2_figures.md literals replaced by F3 in each file
       in turn, nothing else touched, `pytest <that file> -q`
out    tests/test_plan_figures.py            ERROR during collection -- docs/milestones/F3_figures.md does not exist
out    tests/test_plan_matches_tolerances.py ERROR during collection -- "Empty parameter set in
                                            test_the_plan_and_the_code_agree at line 81"
out    tests/test_figure_local_check.py      1 failed, 21 passed
out    tests/test_ci_canonical_environment.py 1 failed, 3 passed -- test_the_plan_and_the_workflow_name_THE_SAME_kernel
cmd    grep -c "{{fig:" docs/milestones/F3.md docs/milestones/F2.md ; grep -c "Q8" on both
out    F3.md 0 and F2.md 60 for figures; F3.md 0 and F2.md 3 for Q8
judge  the reading is right in its conclusion and wrong in its words: NOTHING here would have
       gone vacuous, because this tree refuses an empty parameter set at COLLECTION. That is a
       guard working. Correction recorded as C82.
```

**AND THE AUTHORITY FOR LEAVING THEM IS ALREADY WRITTEN DOWN, which the hand-back did not cite:**

```
cmd    grep -n "hardcoded to a CLOSED milestone" docs/milestones/F2a.md
out    :230  "...`tests/test_plan_matches_tolerances.py:34`, which forced F3's
out          MASS_PROPERTY_AGREEMENT into a closed milestone's table ... **The reviewer ruled:
out          leave them alone** -- neither fails false, re-pointing is a guard edit DR1 forbids
out          ... **Return condition:** one `process:` commit re-pointing all three at the
out          active plan, when the freeze lifts."
cmd    grep -n "MASS_PROPERTY_AGREEMENT" docs/milestones/F2.md
out    :1398  "...so F3's `MASS_PROPERTY_AGREEMENT` has to be in a closed milestone's plan"
out    :1416  | `MASS_PROPERTY_AGREEMENT` | `MASS_PROPERTY_AGREEMENT = 1e-13` |
judge  so F3's one tolerance row lives in F2.md DELIBERATELY, and routing
       test_plan_matches_tolerances.py at F3.md would not merely redden it -- it would take
       away the guard's only live subject. The four are a different class from the four that
       broke at the marker move, exactly as the hand-back says. **Declining was right. DR1 and
       my own ruling on the frozen list both say so, and the return condition is a `process:`
       commit when the freeze lifts, not a step commit now.** The one site of the three in that
       F2a row that HAS since moved is the guard-state harness `_PLAN` (R601a), so that row is
       stale by one site; that is prose on the frozen list and I am not asking for it.
```

**3. THE F4 DRY RUN -- THE TREE IS CLEAN OF IT, AND I RE-RAN IT MYSELF OUTSIDE THE REPOSITORY.**

```
claim  nothing from the dry run survives in the repository
cmd    git ls-files docs/milestones/
out    F1.md  F2.md  F2_figures.md  F2a.md  F3.md          no F4.md is tracked
cmd    git status --porcelain --untracked-files=all
out    (no output)                                         no F4.md is untracked either
cmd    git diff 7b44545..df2c170 --stat -- docs/
out    docs/reviews/F3/step-1.md | 448 +      -- the verdict commit, and nothing else
cmd    grep -rn "step-under-execution" docs/milestones/
out    F2.md:10 moved to F3 at step 1 (DY8c)   -- non-numeric, so it does not resolve
out    F3.md:9  <!-- step-under-execution: 1 -->
judge  CLEAN. `docs/milestones/F3.md` is untouched since 7b44545 and exactly one plan carries a
       numeric marker.
```

```
claim  and the dry run's own conclusion holds, re-measured in MY clone rather than taken
cell   in a clone at df2c170: F3.md marker made non-numeric, a scratch F4.md created with
       `<!-- step-under-execution: 1 -->`, no docs/reports/F4 and no docs/reviews/F4
out    tests/test_report_numbers_are_sourced.py   1 failed, 2 passed -- NOT a collection error
out                                               the failure names the directory, at :175
out    python scripts/ci_section.py               refuses: "ci_section: no numbered verdict
out                                               under ...docs/reviews/F4 ... F4 carries the
out                                               step marker and has not been reviewed yet"
out    python scripts/check_carried.py (no flags) "check_carried: ...docs/reviews/F4/step-1.md
out                                               or ...docs/reports/F4/step-1.md missing"
out    tests/test_report_carried.py               20 failed, 84 passed, 1 skipped -- COLLECTED,
out                                               every failure carrying its own message
out    tests/test_report_guard_states.py          24 tests collected
judge  CONFIRMED on all five resolvers: each resolves to F4 or refuses by saying so, and none
       dies at import. The two fixes do what the commits claim. One correction to what the
       claim SAYS is recorded as C79.
```

**4. THE `2866 -> 2868` DELTA -- LOCALISED, AND THE IMPLEMENTER'S OWN SUSPICION IS REFUTED.**

```
claim  which commit adds the two, and what the two are
cmd    git checkout <each commit> ; python -m pytest --collect-only, in a clone
out    7b44545  2866 tests collected        9492a46  2866        7e32070  2866
out    ecf8e70  2866                        db6a099  2866        3d818b6  2866
out    df2c170  2868
cmd    diff of the collected id lists at ecf8e70 and df2c170
out    + tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists[tests/verification/rung3/test_platform_skeleton.py:test_C56_the_DECK_POINTS_really_come_from_the_DECK]
out    + tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists[tests/verification/rung3/test_platform_skeleton.py:test_the_chosen_FRACTION_is_asserted_not_inferred]
judge  ALL OF IT IS EA4 AND NONE OF IT IS THE VERDICT. The two new cases are the two test names
       the new `# expected:` comments CITE, picked up by the citation guard, and both are green
       because both names exist -- which is the guard doing its job on this very commit. The
       stated suspicion, that verdict 79's findings added parametrisations to
       `test_report_carried.py`, is refuted: 7e32070 collects 2866, the same as 7b44545.
       `test_collected_set_golden` stays green because it is ONE-DIRECTIONAL by design -- its
       own docstring says a new test is not the failure mode -- which is why no golden moved.
       The guards subset moves 957 -> 959 for the same two cases, and CI reports exactly that.
```

## WHAT I VERIFIED MECHANICALLY, BECAUSE THE HAND-BACK ASKED ME TO CHECK TWO CLAIMS

```
claim  EA4 is comments only -- no assertion, threshold or quantity changed
cmd    git diff 7b44545..df2c170 -- tests/verification/rung3/test_platform_skeleton.py | grep "^[-+]" | grep -v "^[-+][-+]" | grep -v "^+ *#"
out    (no output)
judge  CONFIRMED. Twenty-four inserted lines, every one of them a comment, zero deletions.
claim  EA3 changes no logic -- `admissible` is byte-identical below the docstring
cmd    `git show <sha>:floatfea/model/platform.py` at 7b44545 and at df2c170, the function body
       sliced from after the closing docstring quotes to the next top-level def, compared
out    identical below docstring: True   383 bytes at both commits
judge  CONFIRMED.
claim  and every file and field the six new comments name exists
cmd    the deck YAML parsed; the two cited test names grepped for their `def`
out    bodies[] carries mass, reference_point, inertia; joints[] carries body_a, body_b,
out    attach_a_body -- all present in data/platform/platform12_deck.yaml
out    test_the_chosen_FRACTION_is_asserted_not_inferred at :535 and
out    test_C56_the_DECK_POINTS_really_come_from_the_DECK at :383 both exist
judge  EVERY CITATION RESOLVES. And the independence each comment claims is true as stated: I
       followed `deck_mass`/`deck_cog`/`deck_inertia` back through `_full_scale_deck` to the
       YAML, `analytic_properties` through its own closed form with the remainder READ rather
       than recomputed, and `expected_pairs` to `deck_joint_points`/`deck_joint_owner`.
```

## Findings

**R618. (closure, `floatfea/model/platform.py:552`) THE NEW EA3 DOCSTRING SAYS THE SLACK IS
LINEAR IN `f`. IT IS NOT, ON THE ONE BODY WHERE IT MATTERS MOST.** The sentence is "the slack is
linear in `f` and reaches zero only at `f = 0`". The second half is true. The first is false on
the platform and true on the four hubs:

```
claim  the triangle-inequality slack of `J_r` against `f`, every body, every rung of the ladder
cmd    _build_body for each body at each f in MASS_FRACTION_LADDER, slack = a + b - c on the
       sorted eigenvalues of (J_r + J_r.T)/2
out    platform  f 0.5 -2.676969e+08   0.4 -1.785774e+08   0.3 -1.148723e+08
out              f 0.2 -6.705114e+07   0.1 -2.981931e+07   0.0  0.000000e+00
out    slack/f   -5.354e+08  -4.464e+08  -3.829e+08  -3.353e+08  -2.982e+08   a 1.80x spread
out    hub1..4   -2.030550e+06 per unit f at all five rungs, to six figures -- LINEAR
rule   the docstring sentence itself, read as a statement about the shipped ladder
judge  the platform is the body the figure `-2.6770e+08` in `assumptions` is quoted for, and it
       is the non-linear one. The RULING the sentence supports is unaffected and I measured it
       separately: slack is negative at all 25 rungs with f > 0 and exactly zero at f = 0 on all
       five bodies, so requiring realisability really would force `f = 0`. It is the word
       "linear" that is wrong, and it is wrong in a docstring that exists to be the recorded
       reason.
```

**Closed when** the word goes, or the sentence carries the sweep above as a `claim/cmd/out`
triple at the site. Either is one edit.

**R619. (closure, `floatfea/model/platform.py:558`) THE SAME DOCSTRING SENDS THE READER TO
`findings`, AND `findings` IS EMPTY.** "The slack is not hidden -- it is reported in `findings`
with both figures."

```
claim  which container holds the sentence with the two slack figures
cmd    build_superstructure(); print s.findings, each body.findings, and which tuple holds the
       substring "triangle"
out    Superstructure.findings = ()        every body.findings = ()   at the shipped f = 0.5
out    in findings: False     in assumptions: True     in label: False
judge  the sentence is the last entry of `assumptions`, not of `findings`, and `findings` is the
       empty tuple at the shipped configuration -- it fills only when the density exceeds steel
       or the ladder drops a rung, and neither happens. A reader who follows this docstring to
       the container it names finds nothing at all, which is the opposite of what the sentence
       promises. The EA3 commit message makes the same mistake in its own triple, where the
       `cmd` reads "read floatfea/model/platform.py, the body findings" -- a `cmd` that cannot
       be run and that names the wrong tuple.
```

**Closed when** the word `findings` becomes `assumptions` in that sentence, or the two figures
are also put in `findings`. One word, and I prefer the word.

**R620. (closure, `floatfea/model/platform.py:548-561`) THE EA3 DOCSTRING INTRODUCES THREE
QUANTITATIVE CLAIMS ABOUT THE WHOLE LADDER AND CARRIES NO CELL FOR ANY OF THEM.** "PSD at every
`f` on the ladder", "violates the triangle inequality at every `f > 0`", "linear in `f`". CW0 is
exactly this: a claim about this repository written in a docstring is a test, a triple, or
deleted. Two of the three are true, one is R618, and the commit that published them measured
none of them -- the commit's own triples measure what the docstring USED to say and what
`assumptions` contains. I took the sweep because it costs one loop; that it was not taken is the
finding, and under CZ0 it is a closure item rather than a hold.

**Closed when** the three sentences either carry the ladder sweep as a triple at the site, or
are reduced to the shipped configuration, which is the one `assumptions` already measures.

**R621. (closure, `tests/test_report_numbers_are_sourced.py:169-180` and `ecf8e70`'s message)
THE C77 REPAIR IS RIGHT AND ITS DESCRIPTION OVERSTATES IT BY TWENTY.** The commit says "the
twenty-two others are reported as what they are rather than buried in a collection error".

```
claim  what the module actually does in the state the repair is for
cell   the F4 state built in a clone: marker on a scratch F4.md, no docs/reports/F4
out    1 failed, 2 passed in 0.13s
judge  with no report, `TEXT` is "" and `_sections()` returns ONE entry, `(preamble)`, so the two
       parametrised tests run once each and PASS VACUOUSLY. Twenty-two checks are not reported;
       two are, and they are empty. What the repair genuinely buys is real and worth having --
       a NAMED failure carrying the directory instead of a collection error that runs nothing --
       and the suite is red either way, so no gate is weakened. The number is what is wrong.
```

**Closed when** the sentence says what the measurement says. I am not asking for a non-vacuity
assertion: that would be new apparatus, and DR1 is live.

**R622. (closure for F3, AND THE ONE THING IN THIS ROUND F4 HAS TO ANSWER) EA4's SIX COMMENTS
ARE TRUE, AND THE INDEPENDENCE THEY RECORD DOES NOT REACH A DEFECT IN THE DECK. I MEASURED
ELEVEN.** This is my adversarial case for the step and it is the corpus, batch 27.

```
claim  what the six annotated assertions see when the defect is in the deck INPUT
cell   one clone at df2c170, one field of data/platform/platform12_deck.yaml changed per run,
       `pytest tests/verification/rung3/test_platform_skeleton.py -q`, baseline 53 passed
out    every body mass x1.05                     53 passed     invisible
out    the platform mass x1.05 alone             53 passed     invisible
out    every inertia component x1.05             53 passed     invisible
out    the platform Izz halved                   53 passed     invisible
out    one joint attach point +3 m IN PLANE      53 passed     invisible
out    one joint attach point +3 m IN Z          2 passed, 51 errors   CAUGHT, by the builder
out    two buoy joint labels swapped IN THE DECK 53 passed     invisible
out    hub1 reference_point +3 m                 53 passed     invisible
out    element bending rotary inertia dropped    10 failed, 43 passed  CAUGHT, by G3.1a A and B
out    element torsion rho(I_y+I_z) -> rho J     53 passed     NULL: I_y+I_z == J == 1.775958412028696
out                                                            exactly for the tube, so no bit moved
out    MASS_EXPONENT 3.0 -> 2.0                  53 passed at rung 3; 4 failed at rung 4 + unit
rule   the six `# expected:` comments, read as EA4 asks: the named source must not be read from
       the object under test
judge  EVERY COMMENT IS TRUE AND THE GATE FAMILY IS STILL BLIND TO ALL EIGHT. The reason is one
       shape: the expected side and the measured side both DESCEND FROM THE DECK FILE, so a
       defect in the deck moves them together. That is a different circularity from the one EA4
       closes, and the module's own docstring already says the model is constructed to carry the
       deck's properties -- so this is REACH, declared, and not a defect. **I am not holding
       anything on it and I am not asking for a guard.**
judge  WHAT IT MEANS FOR F4, WHICH IS WHY IT IS WRITTEN DOWN. `buoy_joint_nodes` is keyed off the
       deck's `body_a` labels. R600's docstring says a label permutation is "the one that matters
       most, because F4 would have applied each buoy's reaction at its neighbour's node, and
       nothing would have said so". Measured: planted in the BUILDER it is caught; planted in the
       DECK EXPORT it is invisible, 53 passed. The only defence today is provenance -- the file
       is generated and its header forbids a hand edit -- and provenance is not a gate. The
       corpus carries two `plan` rows asking F4 for one expected side that does not descend from
       the deck label, the geometric cluster angle being the obvious candidate.
```

**Closed when** F3 closes with this recorded in the closure artifact as the gate family's reach,
and F4's plan answers the two `plan` rows. Nothing is asked of the implementer inside this step.

**R623. (closure, `tests/verification/rung3/test_platform_skeleton.py:489-492`) THE DZ2 COMMENT
NAMES TWO SOURCES AND THE PLATFORM's CENTRE COMES FROM NEITHER.** The comment says the expected
side is built from `deck_joint_points` and `deck_joint_owner`. For the four hubs that is exactly
true. For the platform, `expected_pairs` uses the typed plan centre `(0.0, 0.0,
superstructure.joint_plane_z)`; the function's own docstring says so two lines above, and
`joint_plane_z` does come from the deck's joint elevations, so nothing is circular. The one-line
comment is what a reader checks against, and it omits the one point that is not a joint.

**Closed when** the comment says "and the typed plan centre for the platform", four words.

## Closure items

Named, not re-reviewed, none of them holding anything. They are the findings above plus what
carries. Fix the list once in the step's closure commit, and verify it AFTER it exists (CZ1).

* **C79 = R621.** `ecf8e70`'s "twenty-two others" is `1 failed, 2 passed`. Wording.
* **C80 = R618.** `floatfea/model/platform.py:552` -- "linear in `f`" is false on the platform.
* **C81 = R619.** `floatfea/model/platform.py:558` -- `findings` should read `assumptions`.
* **C82 = ruling 2 above.** The hand-back's "two vacuous and two red" is four red, two of them
  collection errors. Wording, in the next report.
* **C83 = R620.** The three ladder claims in the EA3 docstring carry no cell at the site.
* **C84 = R623.** The DZ2 comment omits the platform's typed plan centre.
* **C75b.** The `scripts/` LINT PATHSPEC, which `db6a099` explicitly declines and says so. CI
  still runs `ruff check floatfea tests`, `black --check floatfea tests`, `mypy floatfea`, so
  `run_rung.sh`, `check_carried.py`, `write_verdict.py` and `ci_section.py` are unlinted and
  untyped. **Closes when** either the pathspec covers `scripts/` or the exclusion is written down
  as deliberate with its reason. Not blocking: formatting is not a quantity and no gate claims it
  there. Second instance of the same ledger line.
* **C85.** `scripts/check_carried.py:62` and `scripts/ci_section.py:147` are the two
  resolvers in the tree that NOTHING collects. No test imports either module -- `_ci_section()`
  in `tests/test_report_carried.py:987` reads the report, not the script -- so the new
  `_active_step()` and the new `SystemExit` are measured only by a hand invocation. Both are
  correct today; I ran both. **Closes when** the closure artifact records that these two paths
  are reviewer-and-hook-only and are not under test, so nobody later mistakes the green suite for
  coverage of them. No new apparatus: a sentence, not a test.
* **C74, C76, C78, R610, R615** -- carried unchanged from verdict 79, see `## Carried`.

## Tolerances touched

```
cmd  git diff 7b44545..df2c170 -- floatfea/tolerances.py
out  no output
cmd  git diff 7b44545..df2c170 --stat -- floatfea
out  floatfea/model/platform.py | 15 +++++++++++++-  -- the docstring only, verified above
cmd  git diff 7b44545..df2c170 -- tests/conftest.py "tests/**/conftest.py"
out  no output
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py            one conftest in the tree; no rung carries its own
```

**None.** No tolerance, no golden, no parametrisation and no assertion value moved. No
`_COUNTER` moved. No conftest and no plugin changed, so nothing new can rewrite what
`scripts/run_rung.sh` reads and the CH2/CI0 reading has nothing to read this round.

## My own instructions (4b), and the commit classes

```
cmd  git diff 7b44545..df2c170 --stat -- .claude docs/SUPERVISOR.md
out  no output
cmd  git log --oneline 7b44545..df2c170 --name-only, every commit
out  ecf8e70 tests/ only; db6a099 scripts/ only; 3d818b6 floatfea/ only; df2c170 tests/ only
judge  my own instructions are untouched, no commit mixes a `process:` path into a step commit,
       and no commit touches both `floatfea/` and `docs/reviews/`. **There is no STOP-class
       process finding here.** The STOP is the plan, and only the plan.
```

## The adversarial corpus (BE3)

`tests/corpus/platform_deck_input_reach.txt`, batch 27, committed separately from this verdict.
**TWENTY entries, all twenty unseen -- a new file on a surface no corpus has touched.** In scope
under DE2: the platform model and the gate that proves it, not apparatus.

Eleven entries carry a mutation. **TWO CAUGHT, EIGHT INVISIBLE, ONE NULL BY AN EXACT
IDENTITY -- 2 + 8 + 1 = 11 -- and one of the eight is caught a rung higher than the gate under
review.** The eight are the R622 shape and they
are reach rather than misses -- `expect=uncaught` is the prediction written before each run, and
the row records what the shipped suite did. Against ten of eleven in batch 26, twelve of
thirteen in batch 25, six of eleven in batch 24.

Every mutation was applied in a `git clone` of this repository under the session scratch
directory and restored between entries. The working tree was never written to:
`git status --porcelain --untracked-files=all` is empty before and after, and the only path I
wrote in this repository is the corpus file and this verdict.

**AND THE CORPUS COMMIT REDDENS NOTHING, measured two ways.** Nothing globs
`tests/corpus/*.txt` -- each of the six corpus readers names one file by name -- and the
citation guard scans only `.py` prose inside backticks (`tests/test_collected_set_golden.py`
`_citations`, `rglob("*.py")` over `tests/` and `scripts/`), so a `.txt` file adds no
parametrised case. And it was measured rather than reasoned:

```
cmd  python -m pytest tests --ignore=tests/unit --ignore=tests/verification --ignore=tests/regression -q
     with tests/corpus/platform_deck_input_reach.txt present in the tree
out  959 passed, 1 warning in 1153.45s (0:19:13)      exit 0
judge the same 959 CI reports for `guards and meta-tests` at df2c170, so batch 27 moves no
      collected count and no assertion.
```

## On the criterion, and one thing above me

I was asked to rule under CZ0 and I did. **Nothing in these four commits is (a), (b), (c) or
(d).** No defect in `floatfea/` -- I attacked it twelve ways and the two detections that fired
fired correctly. No tolerance and no counter. No gate assertion: EA4 is comments, EA3 is
byte-identical below a docstring. No red test, locally or on CI. Seven findings, every one a
closure item, and I have put them in a list instead of spending a round on them.

**THE ONE THING I WANT RECORDED FOR XABIER, and I say it once.** This is the FIFTH verdict after
the step closed at PASS, and under `docs/SUPERVISOR.md` post-closure verdicts count against the
NEXT step's cap. So step 2 has arrived at its three-verdict cap already consumed, before its
first line is written, and every one of those five rounds has been about either the tree's colour
or a plan sentence the implementer is forbidden to edit. The mechanism is working exactly as
written and the arithmetic is still wrong: the cap exists to stop review consuming a step, and
here it is consuming a step that has not started, on a blocker whose addressee is not in the
loop. **The decision I would like from Xabier is one line: do post-closure rounds spent on a
STOP against the plan count against the next step, or against nothing?** I am not asking for a
fourth round, I am not softening the STOP, and this does not change anything I ruled above.

## Next step opens when

**F3 step 1 stays CLOSED at PASS (DD1, verdict 76). The four EA commits are SOUND: the tree is
green on both machines at `df2c170`, nothing in them blocks, and I have ruled every departure
from the directive in the implementer's favour.** What is stopped is the OPENING OF STEP 2, and
it is stopped on the plan.

1. **`docs/milestones/F3.md` section 5 is re-locked.** R616, unchanged and untouched by these
   four commits: the band sentence goes and G2.1's row says what it is measured on. The evidence
   for choosing the correction over a new gate is in verdict 79's R616 and I have not restated
   its figures here, because restating a measurement I am not re-taking is BP0 in miniature.
2. **Then step 2 opens and R616 carries into its `Carried` section by name**, and stays there
   until section 5 is edited. No verdict of mine can close it.
3. **Nothing else is required of the implementer, and specifically: do not spend a round on EA0,
   on the four hardcoded sites, or on any item in `## Closure items`.** EA0 is withdrawn.
   The four sites stay as they are until DR1 lifts, which is my own ruling on the frozen list and
   not a new one. The closure list is fixed once, in the closure commit, verified after it exists
   per CZ1.
4. **No re-review of this tree is needed to open step 2** once section 5 is edited: the plan edit
   is under `docs/milestones/`, and this verdict has recorded the colour of the code at
   `df2c170`. If `floatfea/`, `tests/` or `scripts/` moves again before step 2 opens, that
   condition lapses and the same reading applies to whatever moved.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the
code-check screen 28 October. **I have no measurement that contradicts any of them.** The one
item that could move them is still R616 answered as a new gate rather than as a correction. Five
post-closure rounds have now been spent, none of them on the platform model until this one, and
R622 is the first thing in those five that F4 will actually have to answer.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: 9492a460464e1313e4e683e283ef1c9ac56d81d6
Verdict: STOP
Tests: 2866 passed, 0 failed, 0 skipped   (my own run at the reviewed commit 7b44545, `python -m pytest -q`, one invocation, no split, no exclusion, clean tree, 1384.81s, exit 0)

## Round of 2026-09-30 -- SEVENTY-NINTH verdict. THE TREE IS GREEN ON BOTH MACHINES, R612 IS CLOSED, AND I AM CHANGING MY OWN LABEL ON R613 FROM HOLD TO STOP.

**F3 step 1 remains CLOSED at PASS (DD1, verdict 76).** Nothing here reopens it and the
STOP below is not about it. What is held is the OPENING of step 2, and the reason is that
`docs/milestones/F3.md` section 5 is wrong about the structure it instructs a gate to be
measured on. That is the definition of STOP in my own instructions -- the locked plan is
wrong; implementation halts and the plan reopens -- and I am told not to soften one.

**This is the verdict that records the tree's colour, which is what was asked for, and it
records it as GREEN.** The state the directive arrives into is now measured rather than
asserted.

## THE TREE AT 7b44545, MEASURED

```
cmd    git rev-parse HEAD && git rev-parse origin/F3
out    7b445451b3cfd4790248f632af570827c44975a2   both -- pushed, HEAD of F3
cmd    git diff 01e78c9..HEAD --stat
out    tests/verification/rung3/test_platform_skeleton.py | 7 ++++---
out    1 file changed, 4 insertions, 3 deletions
cmd    python -m pytest -q          mine, whole tree, clean, one invocation
out    2866 passed, 2 warnings in 1384.81s (0:23:04)      exit 0
cmd    python -m ruff check floatfea tests
out    All checks passed!
cmd    python -m black --check floatfea tests
out    All done!  89 files would be left unchanged.
cmd    python -m mypy floatfea
out    Success: no issues found in 29 source files
```

**CI, AT THE REVIEWED COMMIT, CONFIRMED FROM `gh` AND NOT FROM THE PASTE (CA2).**

```
cmd    gh run list --commit 7b445451b3cfd4790248f632af570827c44975a2 --json name,conclusion,status,workflowName,databaseId,event,headSha
out    CI  36789399558  push  completed  success   headSha 7b4454...
cmd    gh run view 36789399558 --json jobs, every job and every step
out    the verification ladder     success   13 steps, all success
out    lint, unit and guards       success   14 steps: actionlint, ruff, black --check,
out                                          mypy, unit tests, guards and meta-tests --
out                                          ALL SUCCESS, none skipped
out    CI determinism -- leg              skipped   0 steps
out    CI determinism -- ten legs agree   skipped   0 steps
cmd    gh run view 36789399558 --log, the count lines
out    unit tests             88 passed in 0.47s
out    guards and meta-tests  957 passed, 1 warning in 446.89s (0:07:26)
out    ladder 1  run_rung: 1276 collected, 0 failed, 0 errored, 0 skipped   run_rung: OK
out    ladder 2  run_rung:   66 collected, 0 failed, 0 errored, 0 skipped   run_rung: OK
out    ladder 3  run_rung:  218 collected, 0 failed, 0 errored, 0 skipped   run_rung: OK
out    ladder 6  run_rung:  134 collected, 0 failed, 0 errored, 0 skipped   run_rung: OK
out    ladder 4  run_rung:  127 collected, 0 failed, 0 errored, 0 skipped   run_rung: OK
out    ladder 5  run_rung: OK -- 0 directories ran        empty by design
judge  the two skipped jobs are gated on the workflow_dispatch event in
       .github/workflows/ci.yml under CK0. That is DECLARED-not-run, which is neither a red
       build nor CK2's allowance-exhausted state: no job here has an empty runner_name with
       a two-second duration and a spending annotation. I record them as **unavailable by
       declaration**, and the inputs that decide them -- the render, the kernel pin, the
       environment -- are untouched since the last dispatch.
```

**AND THE CAUSAL CLAIM IN THE COMMIT TITLE CARRIES ITS CELL (BG0), which I checked rather
than accepted.** "One line over the limit hid the whole guard suite from CI":

```
cell   the same workflow, the same job, two commits, and the only difference on the lint
       path is the wrap -- 359bda3, d305253 and 01e78c9 touch docs/reviews/ and
       tests/corpus/ only
cmd    gh run view 36781142834 --json jobs          at 8e4238d
out    lint, unit and guards  FAILURE: actionlint success, ruff FAILURE, then
out       black --check SKIPPED, mypy SKIPPED, unit tests SKIPPED,
out       guards and meta-tests SKIPPED
cmd    gh run view 36789399558 --json jobs          at 7b44545
out    lint, unit and guards  SUCCESS: all six, none skipped, guards 957 passed
judge  CONFIRMED, and the "for the first time" half too: the last run to EXECUTE the guards
       step before this one was 36777499936 at 78e9583, which predates C60's repoint
       entirely. So C60's repointed guard has now run on CI exactly once, green.
```

## WHY I AM CHANGING MY OWN LABEL, AND WHAT THE STOP IS AND IS NOT

Verdicts 77 and 78 both carried R613 as a blocking HOLD item. Two rounds have now been
spent with it on a list whose addressee cannot act on it, and the implementer has stated on
the record that it cannot -- correctly, under `CLAUDE.md` section Working agreement. **HOLD
names the implementer; STOP names the plan.** The item has only ever belonged to the second,
and calling it the first is what produced two rounds that moved nothing. That is the whole
reason for the change; no new defect was found in R613 this round.

**WHAT THE STOP IS.** `docs/milestones/F3.md` section 5, the G2.1 row and the paragraph
"What F3 must check that F2 could not", instructs a first measurement in a band that
contains none of the platform's members, on a stated premise that the same document
elsewhere measures to be false.

**WHAT IT IS NOT.** It is not a defect in `floatfea/`, not a red test, not a tolerance, and
not a statement that G2.1 is unsound -- I measured the opposite below. It does not make step
1's work uninterpretable and it does not touch the tree's green.

## Carried

* **R612 -- CLOSED.** Verified at the reviewed commit, both halves of the condition. The
  diff is one hunk in one file and `line-length` did not move:

```
cmd    git diff 01e78c9..HEAD -- tests/verification/rung3/test_platform_skeleton.py
out    line 414 dict comprehension wrapped across three lines; the f-string at 438-441
out    joined onto one. Four insertions, three deletions, nothing else in the tree.
cmd    git diff 01e78c9..HEAD -- pyproject.toml
out    no output -- tool.black line-length = 100 and tool.ruff line-length = 100 are
out    where they were
judge  both hunks are value-preserving, read: implicit f-string concatenation of
       f"a " and f"{x}." is the same string as f"a {x}.", and the comprehension is
       unchanged. And the line numbers BELOW 414 did not move, which is what the R600
       evidence rows in the report cite -- 326 to 343. Checked: no citation anywhere in
       tests/, scripts/ or docs/ names a line at or after 414 in that file.
cmd    ruff, black, mypy, pytest and gh -- all five above
judge  CLOSED. The guard suite reached CI and was green there, which is the half of the
       condition that had been unavailable since 1b3fb73.
```

* **R613 -- STILL OPEN, AND IT IS NOW THE STOP.** Not answered, not answerable by the
  implementer, and I confirmed the measurement independently rather than accepting it:

```
cmd    build_superstructure(), every member of every body, vector between its two nodes
out    16 members   the n_members property agrees: 16
out    max |dz| = 0.0   exactly, on all sixteen
out    angle from vertical: min 90.0000  max 90.0000 degrees
out    within 15 degrees of vertical: 0 of 16      at exactly 90.0000: 16 of 16
out    four at L = 50.0000 m centre-to-hub, twelve at L = 25.0000 m hub-to-buoy-joint
rule   docs/milestones/F3.md section 5: "A platform frame is mostly near-vertical members,
       so this gate is measured there first."
judge  the premise is false on this platform and the sentence is CAUSAL, so BG0 reaches it:
       the "so" makes the instruction a consequence of a fact that is not one. And section
       3.1 of the same document already measured z spread max minus min = 0.000e+00 m and
       calls the frame planar. The document contradicts itself.
```

* **R611 -- WITHDRAWN, and I did not touch the `Answers:` header.** Item 1b was applied and
  I record what it found rather than acting on it: the report's newest header reads
  `Answers: verdict 73 @ 52de940` while the latest verdict is 78. Under my own verdict 78
  that is not a finding here -- the report commit 8e4238d is an ancestor of the verdict
  commit 01e78c9, so the exemption at `tests/test_report_carried.py:394-400` applies and the
  boundary is the legitimate one. Measured: `git merge-base --is-ancestor 8e4238d 01e78c9`
  returns YES, and the whole tree is 0 failed. Bumping the header to 76 was measured at
  33 failed in verdict 78 and remains the wrong move.
* **R614 -- closed by verdict 78 being on the page.** Nothing here reopens it.
* **R615 -- still a closure item, unchanged, and this round is a second instance of the same
  window.** It carries beside R610 as a standing cost. No code change asked.
* **C59 (R605) -- closed at verdict 77.** Unchanged.
* **C58, C60, C61, C62, C63, C64 -- met, as ruled at verdict 77**, and C60 now has a CI
  result behind it for the first time, above.
* **C65 to C73 -- closure items, holding nothing.** **C72 is ruled below** at the
  implementer's request. **C40, C56(iii), C56(iv), C57** carry forward as recorded.

## Findings

**R616. (STOP-class, and it is R613 restated as what it actually is) `docs/milestones/F3.md`
section 5 instructs G2.1's first measurement in a band that is empty on the platform, on a
premise section 3.1 of the same document refutes.** The measurement is in `Carried` above.

**AND HERE IS THE THING THAT SHOULD DECIDE THE RE-LOCK, WHICH NOBODY HAD MEASURED.** The
choice put to Xabier is a correction against a new gate that moves the date. I took the
measurement that distinguishes them, using the shipped `element_rigid_residual` and the
shipped `local_stiffness`, on the sixteen members the platform actually has:

```
claim  G2.1's quantity on the real members, and whether the gate there is marginal
cmd    element_rigid_residual(local_stiffness(m.section, b.material, m.length), m.length)
       for every member of build_superstructure(), against RIGID_MODE_EXACTNESS = 1e-15
out    the 16 members collapse to 3 distinct classes by length and max|k_e|
out    worst residual over all sixteen = 3.5283e-19       margin to the ceiling 2.83e+03x
out    best                            = 8.7210e-20                             1.15e+04x
rule   element_rigid_residual(k_local, L) <= RIGID_MODE_EXACTNESS, per member, which is what
       section 5 says G2.1 asserts
judge  NOT MARGINAL. Three decades of headroom at the worst member.
```

```
claim  and the gate on those members CARRIES ITS OWN FAILURE -- all three registered
       counters reach every class, so it is not a gate that cannot fail
cmd    the `injected` function of scripts/rigid_counter_response.py at its own SIZE = 1e-8
       of max|k_e|, and again at 1e-4, into each of the three classes
out    dropped_flip      reddens 3 of 3 classes at both sizes; worst injected 3.656e-10
out    wrong_dof_index   reddens 3 of 3 classes at both sizes; worst injected 9.459e-09
out    rotational_block  reddens 3 of 3 classes at both sizes; worst injected 1.462e-11
out    the SMALLEST injected response anywhere is 3.784e-12, which is 3.8e+03x ABOVE the
       ceiling -- so the ceiling sits between the clean residual and the weakest detected
       defect with about three decades either side
rule   the same assertion, unchanged
```

```
claim  and the counters are DETECTION THRESHOLDS on these members, not one perturbation
cmd    invert the decision rule: bisect in log10 for the smallest injected fraction of
       max|k_e| at which element_rigid_residual exceeds 1e-15, per class per counter
out    dropped_flip      worst class threshold 5.286e-14 of max|k_e|   at L = 50 m
out    wrong_dof_index   worst class threshold 1.094e-15               at L = 25 m
out    rotational_block  worst class threshold 2.643e-12               at L = 50 m
out    the injection convention's SIZE = 1e-8 is four to seven decades past every one
judge  **SO THE CORRECTION IS SUFFICIENT AND A NEW GATE IS NOT NEEDED FOR SOUNDNESS.** G2.1
       on the members the platform has is neither vacuous nor marginal, measured three ways.
       What the band sentence was guarding against -- an element-local form that degrades
       near vertical -- cannot arise on a frame with no member within 15 degrees of
       vertical. I offer this as evidence for the re-lock; I am not making the decision and
       I have not touched the plan.
judge  WHAT IT DOES NOT SAY, so nobody promotes it. It is not the gate -- step 2 builds
       that. It is not a claim about members outside the planar frame, which do not exist on
       this model and would be a different measurement. And under "do not let right every
       time become a prior", four numbers taken by the reviewer with the implementation's
       own functions are an instrument reading, not an independent witness.
```

**Closed when** `docs/milestones/F3.md` section 5 no longer states that the frame is mostly
near-vertical and no longer instructs a first measurement in that band, and G2.1's row says
what it is measured on -- the sixteen members the platform has. One sentence and one row, in
a re-lock commit. Under DK0 that re-lock buys no fresh rounds.

**R617. (withdrawn by me, in the same round I found it, and the withdrawal is the record)** I
found that `_active_milestone` in `tests/test_report_numbers_are_sourced.py:53-72` falls back
to F2 -- a closed milestone -- whenever the marker resolution is ambiguous, and that
`_active_plan` in `tests/test_report_guard_states.py:44-74` does the same. That is a silent
default in the place C60 was repairing. **I then checked whether anything catches it before
publishing it, and something does:**

```
cmd    tests/test_report_carried.py:471-483, read, then driven directly against a scratch
       copy of docs/milestones with _MILESTONES, _PLAN and _PLAN_STEP_NUMBER rebound
out    real tree, one marker      -> PASSES
out    ZERO numeric markers       -> RED, "0 plans carry a step-under-execution line"
out    TWO numeric markers        -> RED, "2 plans carry it, F2a.md and F3.md"
judge  the assertion exists, it fires on both off-nominal states, and its own message already
       names the consequence I was about to report -- how a guard comes to read a closed
       milestone's last step and report green while checking nothing. WITHDRAWN. The residual
       is that the coverage is one assertion in one of the three files, so it holds only in an
       invocation that collects that file: the guards CI step does, the ladder job does not,
       and does not need to.
```

**Closed when** nothing. It is closed by being measured.

## Closure items

Named, not re-reviewed, and none of them holds anything. Fix the list once in the step's
closure commit -- and run the checks at that commit after it exists, per the wording
requested below.

* **C74.** `docs/reports/F3/step-1.md:264` and `:319` -- the generated CI section is anchored
  on verdict 74 at 228bdfb, run 36743792702, conclusion **failure**, while CI at the tree
  under review is run 36789399558, **success**. Every number in it was right when taken; the
  section a reader opens to learn CI's colour describes a commit five rounds back. BP0 in its
  plainest form. **Closes when** `scripts/ci_section.py` is re-run at the commit that
  publishes the next revision.
* **C75.** `python -m black --check scripts` is **red at this commit** --
  `scripts/carried_table.py` would be reformatted, and 8e4238d is the commit that touched it.
  Neither CI lint step covers `scripts/`: the pathspecs are `ruff check floatfea tests` and
  `black --check floatfea tests`, and `mypy floatfea` leaves the directory untyped entirely.
  That directory holds `run_rung.sh`, `check_carried.py`, `write_verdict.py`, `ci_section.py`
  and `regen_figures.py` -- the ladder gate's logic, the carry guard's logic, and the
  reviewer's own writer. This is R612's shape with the pathspec instead of the line length.
  **Closes when** either `scripts/` is inside the lint pathspec and the file is formatted, or
  the exclusion is written down as deliberate with its reason. Not blocking: formatting is not
  a quantity and no gate claims it there.
* **C76.** The one miss in corpus batch 26. `tests/test_report_carried.py:471-483` asserts
  that exactly one PLAN carries the marker; it does not assert exactly one MARKER per plan,
  and `re.search` returns the first. A stale marker line left ABOVE a live one resolves to the
  stale number, silently, in all three files, and every report guard then reads the wrong
  step's report -- green. Measured: the value 1 above the value 7 in F3.md gives step 1 from
  all three resolvers and the assertion GREEN. The same edit in the other order is red only
  because step-7.md does not exist yet. **Closes when** that existing assertion also counts
  markers per file, in the same clause. No new file and no new guard -- a clause added to an
  assertion written for exactly this class.
* **C77.** `tests/test_report_numbers_are_sourced.py:81` -- `_newest_report`'s `assert steps`
  runs at module import through the module-level `REPORT`, so a plan whose reports directory
  does not yet exist makes the module fail to COLLECT rather than fail a test. That is the
  R234 shape the same module's `_active_milestone` docstring says it avoids, two functions
  apart. Measured: AssertionError "no numbered step report under ..." at import. **Closes
  when** the check is a test, or the docstring stops claiming the module avoids it.
* **C78.** A ledger line beside R610 and R615, no code change. CK0's cheap-first step order in
  `.github/workflows/ci.yml` is deliberate and its ratio is measured in the file. Its realised
  cost is now one round in which the guard suite's result was UNAVAILABLE behind a
  one-character lint error, at the commit where that result mattered most. The workflow's own
  comment already declines to claim that lint predicts test failure. Recorded as the price of
  the trade, not as a request to change it -- changing it is apparatus and DR1 is live.

## THE TWO RULINGS ASKED FOR

**1. THE CLOSURE-COMMIT RULE. YES, I WANT IT WORDED AS A RULE, AND HERE IS THE WORDING.**
Carry this to Xabier verbatim rather than paraphrasing it. It asks for no new apparatus: every
command in it already exists and already runs somewhere.

> **A closure commit is verified AFTER it exists (proposed CZ1).** A closure commit is written
> after the last reviewed round and is not reviewed by rule, so nothing between it and the
> next step's report measures it. Two classes of red shipped in 8e4238d for that reason: the
> lint gate, which `pytest` does not run, and the report guards, whose answer is a function of
> the commit graph and therefore cannot be taken before the commit exists.
>
> So, for every closure commit, in this order: **(i)** make the commit; **(ii)** at that
> commit, tree clean, run and paste `ruff check floatfea tests`, `black --check floatfea
> tests`, `mypy floatfea` and `pytest -q`; **(iii)** push it and paste `gh run list --commit
> <sha>` with the job-level conclusions, so that the lint job's `guards and meta-tests` step
> is seen to have RUN rather than been skipped behind an earlier red step; **(iv)** any red is
> answered in a follow-on commit that repeats (ii) and (iii). A closure commit is not finished
> until a pushed CI run at its own sha, or at the follow-on's, is green.
>
> The four outputs are `claim / cmd / out` triples (BF0, CP2) in the step report's closure
> section, or -- where that report is already closed -- in the next report's `Carried`.
>
> **The reusable half of it:** a check whose input is the commit itself cannot be measured
> before the commit exists. That class includes `tests/test_report_carried.py`,
> `tests/test_report_guard_states.py`, and anything reading `git log`, `git diff` or
> `git merge-base`. For those, "I ran it before committing" is not a measurement.

**2. C72 -- `scripts/write_verdict.py`'s CRLF doubling. NOTHING IS CORRUPTED AT THIS COMMIT.
IT WILL BE, ON THE FIRST UNMITIGATED INVOCATION.** The directive can say "only will be":

```
claim  the committed bytes of both files are clean at 7b44545
cmd    git show HEAD:scripts/write_verdict.py | count CRLF, lone CR, LF
out    7090 bytes   CRLF 0   lone CR 0   LF 150        pure LF
cmd    git show HEAD:docs/reviews/F3/step-1.md | count CRLF, lone CR, LF, CR CR LF
out    147473 bytes   CRLF 0   lone CR 0   LF 2412   CR CR LF 0     pure LF
cmd    the same counts on the WORKING COPY of docs/reviews/F3/step-1.md
out    149885 bytes   CRLF 2412   lone CR 0   CR CR LF 0
cmd    git config --get core.autocrlf
out    true        so the working copy being all-CRLF is a normal checkout, not damage
judge  CLEAN, both on the page and in the index. No stray carriage return exists anywhere in
       either file at this commit.
```

```
claim  and the mechanism is real, reproduced on a two-line file outside the repository
cmd    write b"line one\r\n line two\r\n"; read_bytes; decode; then line 140's
       out.write_text(rounds, encoding="utf-8") -- text mode, platform newline
out    b'new round\r\n\r\n\r\n---\r\n\r\nline one\r\r\nline two\r\n'    CR CR LF: 1
cmd    the same call with newline="\n" added
out    CRLF 1, CR CR LF 0
judge  one CR CR LF per preserved line, so the live file's next unmitigated round would
       produce about 2411 of them, and `core.autocrlf` on commit would turn each into a LONE
       CARRIAGE RETURN in the blob. The fix is the keyword argument and nothing else. I am
       not making it: my writable paths are docs/reviews/ and tests/corpus/, and the file is
       the reviewer's tool, which the closure commit already declined to touch from the other
       side. **My ruling: the one-keyword change alters nothing the tool asserts or reads, so
       it is a closure item and not a directive -- but since both sides have now declined it
       on DR1 grounds, put it in the same directive as CZ1 and let Xabier settle it in one
       move.** Until then the mitigation is mine and it is manual: normalise the file to LF
       before every invocation, which is what I did for this round.
```

## THE CORPUS (BE3)

`tests/corpus/plan_step_marker_resolution.txt`, batch 26, committed separately from this
verdict. **EIGHTEEN entries, all eighteen unseen -- this is a new file on a surface no corpus
had touched.** Eleven carry a state that misdirects or blinds a report guard; **TEN CAUGHT,
ONE MISS**, and the miss is C76 above. Seven are controls or reach rows and are counted
neither way. Against twelve of thirteen in batch 25, six of eleven in batch 24, eleven of
sixteen in batch 23.

The surface is the one input the three report guards share after C60, R601a and DX2 replaced
five hardcoded milestone constants with one regex over `docs/milestones/F*.md`. Nothing had
measured that resolution off its nominal input. Every `measured=` was taken against a scratch
copy of the plan directory with the shipped modules' own path globals rebound; no file in the
repository was written and the tree was clean at every row. **The header records that the
reviewer's own first pass got shape 12 wrong** -- rebinding only `_MILESTONES` leaves the step
number reading the real F3 marker -- because that is the mistake the next reader would repeat.

**AND THE CORPUS COMMIT DOES NOT REDDEN THE SUITE**, which CO3 earned the hard way:

```
cmd  python -m pytest tests --ignore=tests/unit --ignore=tests/verification --ignore=tests/regression -q
     with tests/corpus/plan_step_marker_resolution.txt present in the tree
out  957 passed, 1 warning in 1089.23s (0:18:09)      exit 0
judge the same 957 CI's `guards and meta-tests` step reports at 7b44545, so batch 26 moves no
      collected count and no assertion. Nothing globs tests/corpus/*.txt, and the two scanners
      that walk tests/ read only .py and .md.
```

## Tolerances touched

```
cmd  git diff 01e78c9..HEAD --stat -- floatfea/tolerances.py
out  no output
cmd  git diff 01e78c9..HEAD --stat -- floatfea
out  no output
cmd  git diff 01e78c9..HEAD --stat -- tests/conftest.py 'tests/**/conftest.py'
out  no output
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py            CI0: the pathspec resolves to a real file, as it must
cmd  git ls-files | grep conftest
out  tests/conftest.py            one conftest in the tree; no rung carries its own
cmd  git diff 01e78c9..HEAD --stat -- .claude docs/SUPERVISOR.md
out  no output
cmd  git diff 01e78c9..HEAD --stat
out  tests/verification/rung3/test_platform_skeleton.py | 7 ++++---
```

**None.** No tolerance, no golden, no parametrisation and no assertion moved. No conftest and
no plugin changed, so nothing new can rewrite what `scripts/run_rung.sh` reads and the CH2/CI0
reading has nothing to read this round. My own instructions are untouched, and the one commit
under review touches neither `floatfea/` nor `.claude/` -- so there is no STOP-class
process-commit finding here.

## ON THE CRITERION

I was asked to rule under CZ0 and to say so if I disagree with the criterion rather than with
the work. **I do not disagree, and I applied it against myself twice this round:** R617 was
withdrawn before publication once I measured that an existing assertion covers it, and five
findings that are real -- a published CI table describing a red run at a five-round-old
commit, a red `black --check scripts`, a marker-count gap, an import-time assert, a step-order
cost -- are listed as closure items and are not holding anything. The STOP is not a CZ0
promotion: a locked plan that is wrong is its own head in my instructions and always was.

## Next step opens when

**F3 step 1 stays CLOSED at PASS (DD1, verdict 76). The TREE IS GREEN, locally and on CI, and
that is now on the record. What is stopped is the OPENING OF STEP 2, and it is stopped on the
plan rather than on the implementer.**

1. **`docs/milestones/F3.md` section 5 is re-locked.** The band sentence goes and G2.1's row
   says what it is measured on. The evidence for choosing the correction over a new gate is in
   R616: on the sixteen real members the worst residual is `3.5283e-19` against a `1e-15`
   ceiling, and all three registered counters redden all three element classes with the
   weakest detected response still `3.8e+03x` above the ceiling. **If the choice is the new
   gate instead, the date moves and that is said the day it is made.**
2. **Then step 2 opens and R616 carries into its `Carried` section by name**, as R613 did,
   and stays there until section 5 is edited. No verdict of mine can close it.
3. **Nothing else is required of the implementer.** R612 is closed. C74 to C78 are closure
   items for the closure commit and none of them gates step 2. Do not spend a round on them
   and do not spend a line on R611.
4. **No re-review of this tree is needed to open step 2** once section 5 is edited: the plan
   edit is under `docs/milestones/`, the code is untouched, and this verdict has recorded the
   colour.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the
code-check screen 28 October. **I have no measurement that contradicts any of them**, and the
one item that could move them is R616 answered as a new gate rather than as a correction --
which R616's three cells argue against on soundness grounds. The two rounds spent carrying
R613 as a HOLD are the cost already paid for mislabelling it, and this verdict is the
correction.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: 359bda33c33c88544ebe9552c23c093234856531
Verdict: HOLD
Tests: 2866 passed, 0 failed, 0 skipped   (my own run at `359bda3`, `python -m pytest -q`, 1415.93s, one invocation, no split, no exclusion, exit 0 -- and `8 failed, 2858 passed` at the reviewed commit `8e4238d`; BOTH are true and the reason is this round's subject)

## Round of 2026-09-30 -- SEVENTY-EIGHTH verdict. A CORRECTION TO MY OWN VERDICT 77, AND NO NEW COMMIT IS REVIEWED.

**This round reviews nothing the implementer wrote.** It exists because verdict 77's R611
carried a closing condition that is both unnecessary and harmful, and I am the one who wrote
it. `CLAUDE.md` Â§ "Every claim carries its command" applies to a verdict as much as to a
report, and "a wrong reason in the tree outlives the red" is the sentence I used on the
implementer two rounds ago. So this is a page, not a round: **nothing new is asked of the
implementer here and the work list gets SHORTER.**

**F3 step 1 remains CLOSED at PASS (DD1, verdict 76).** The verdict remains **HOLD**, on
R612 and R613 alone.

## What verdict 77 got wrong

**Writing verdict 77 cleared the red verdict 77 was about.** I measured the eight failures at
`8e4238d` twice and they were real. What I did not check before publishing a closing
condition is what my own commit would do to them.

```
cmd    for each commit, the guard's three inputs, taken without moving HEAD:
       git log -1 --format=%h <commit> -- docs/reviews/F3/step-1.md
       git log -1 --format=%h <commit> -- docs/reports/F3/step-1.md
       git merge-base --is-ancestor <report> <verdict>
out    at 8e4238d : verdict 78e9583 | report 8e4238d | report is ancestor: NO
out    at d305253 : verdict 78e9583 | report 8e4238d | report is ancestor: NO
out    at 359bda3 : verdict 359bda3 | report 8e4238d | report is ancestor: YES
rule   tests/test_report_carried.py:394-400 -- if the newest verdict commit DESCENDS from
       the newest report commit, the guard returns early and the report legitimately
       predates the verdict
cmd    python -m pytest tests/test_report_carried.py tests/test_report_guard_states.py -q
out    at 8e4238d (twice, in isolation, tree clean)   8 failed, 202 passed
out    at 359bda3, after verdict 77 was committed     0 failed, and 256 passed across the
                                                      four files that read docs/reviews/
cmd    python -m pytest -q      (mine, WHOLE TREE, at 359bda3, clean, one invocation)
out    2866 passed, 2 warnings in 1415.93s (0:23:35), exit 0 -- 0 failed, 0 skipped
judge  **THE RED IS SELF-CLEARING AND MY OWN COMMIT IS WHAT CLEARS IT.** It was red at the
       reviewed commit and at my corpus commit; the moment a newer verdict exists the
       ancestry exemption re-applies, and the report is once again allowed to name an older
       verdict because that is the legitimate step boundary. Nothing the implementer does is
       required, and nothing it does could be verified against those eight tests now.
judge  AND MY CLOSING CONDITION WOULD HAVE MADE THINGS WORSE. Verdict 77 asked for the
       newest `Answers:` line to name verdict 76. I measured that state myself in the same
       verdict -- `33 failed, 214 passed` -- and then wrote it into the condition anyway.
       The two halves of R611 contradict each other, and the cell is the half that is right.
```

## Carried

* **R611 -- WITHDRAWN AS A BLOCKING ITEM, and its closing condition is withdrawn with it.**
  The red was real at `8e4238d` and it justified the HOLD at that commit; it is gone at
  `359bda3` for a reason that has nothing to do with a repair. **Do not bump the `Answers:`
  header to verdict 76** -- measured, that state is `33 failed`. What survives is not
  mechanical and is not a work item on its own: the closure commit edited
  `docs/reports/F3/step-1.md` and no header in that file declares which verdict its edits
  answer. The next report or revision names the newest verdict at the time it is written, as
  it always must, and that discharges it.
* **R612 -- STILL OPEN, STILL BLOCKING.** Unchanged and confirmed at `359bda3`:

```
cmd  python -m ruff check floatfea tests
out  Found 1 error.        (E501, tests/verification/rung3/test_platform_skeleton.py:414)
cmd  python -m black --check floatfea tests
out  1 file would be reformatted, 88 files would be left unchanged.
judge the two commits since 8e4238d touch only `tests/corpus/*.txt` and `docs/reviews/`, so
      neither lint gate could have moved and neither did. **CI has no run at `359bda3`, which
      is not pushed, so the newest CI result is still the red one at `8e4238d`** -- where
      `lint, unit and guards` died at step 6 of 14 and never reached the guard suite. That is
      unavailable-at-HEAD plus red-at-the-last-run, and neither of those is green.
```

* **R613 -- STILL OPEN, STILL BLOCKING, and it carries by name into step 2.** Nothing in this
  round touches `docs/milestones/F3.md`, so Â§ 5 still instructs a first measurement in a band
  that contains none of the sixteen real members (`max |dz| = 0.0` exactly, 90.0 degrees from
  vertical on every one) while Â§ 3.1 of the same document measures the frame planar.
* **C59 (R605) -- closed in verdict 77 and nothing here reopens it.** The path is independent,
  the duplication is exercised and load-bearing, and the one shared surface is digest-pinned.
  That ruling stands unchanged.
* **C58, C60, C61, C62, C63, C64 -- met, as ruled in verdict 77.** **C65 to C73** are closure
  items and hold nothing. **C40, C56(iii), C56(iv), C57** carry forward as recorded.

## Findings

**R614. (closure, and it is against MY OWN verdict) Verdict 77's R611 published a closing
condition it had already refuted in its own cell, and this round is the correction.**
`docs/reviews/F3/step-1.md`, verdict 77's R611 block.

```
judge  the defect is CP2's, in the place CP2 was written for: the attention went to the thing
       being measured, and the prose written AROUND it inherited none of the discipline. The
       measurement was right twice over -- `8 failed` at the commit, `33 failed` under the
       obvious repair -- and the sentence that turned them into an instruction was checked
       against neither.
judge  AND THE GENERAL FORM IS WORTH MORE THAN THE INSTANCE: **a reviewer's closing condition
       is a claim about the repository and it should carry the command that would refute it.**
       Verdict 77's other two conditions do -- R612 names two commands, R613 names a plan
       section and a measurement. R611's did not, and it is the one that was wrong.
```

**Closed when** nothing; it is closed by this round being on the page.

**R615. (closure) The guard that caught the closure commit can only catch it inside one
window, and that window is shut by the next verdict.** `tests/test_report_carried.py:394-400`.

```
rule   the exemption: the report commit is an ancestor of the newest verdict commit
judge  so the state "the report was edited AFTER the newest verdict and its header was not
       moved" is visible only between that edit and the next verdict commit. After it, the
       same tree reads green. The exemption is CORRECT -- it is the legitimate boundary DX2
       and item 1b exist for, and `33 failed` is what removing it would cost -- but it means
       **a report edited by a closure commit is checked for at most as long as it takes a
       reviewer to answer, and never again.** The eight reds this round is correcting are the
       only time the mechanism will ever have said so.
judge  DR1 FORBIDS EXTENDING IT AND I AM NOT ASKING. Recorded as a standing cost in the same
       class as R610, and the mitigation available under the freeze is a reviewer reading the
       commit -- which is how it was found.
```

**Closed when** it is ledgered alongside R610 as a standing cost, or `docs/milestones/F2a.md`
carries it as a frozen list entry. No code change either way.

## Tolerances touched

```
cmd  git diff 8e4238d..359bda3 --stat -- floatfea
out  (no output)
cmd  git diff 8e4238d..359bda3 --stat
out  docs/reviews/F3/step-1.md                                       | 581
out  tests/corpus/platform_geometry_provenance_independent_read.txt  |  87
```

**None.** Nothing under `floatfea/` has changed since `8e4238d`, and the only two files
touched since are my own verdict and my own corpus batch. No tolerance, no golden, no
parametrisation and no assertion moved in this round, by me or by anyone.

## Next step opens when

**Step 2 does not open yet. F3 step 1 remains CLOSED at PASS (DD1, verdict 76); what is held
is the TREE.** The list is now TWO items and R611 is not one of them.

1. **R612 closed** -- `ruff check floatfea tests` and `black --check floatfea tests` clean, by
   reformatting `tests/verification/rung3/test_platform_skeleton.py:414` and not by moving
   `line-length`; and CI's `lint, unit and guards` job reaches `guards and meta-tests` and
   succeeds at the commit that ships it. **Paste the `gh run list` line.** The guard suite
   has not run on CI since `1b3fb73`.
2. **R613 closed** -- `docs/milestones/F3.md` Â§ 5 no longer instructs a first measurement
   whose subject is empty on the real platform, and no longer says the frame is mostly
   near-vertical. One sentence; under DK0 it buys no rounds. **R613 carries by name into
   step 2's `Carried` section and stays blocking there until Â§ 5 is edited.**
3. **R611 is withdrawn.** Do not spend a line on it and do not touch the `Answers:` header
   for its sake. The next report names the newest verdict when it is written, which by then
   is this one.
4. **Then one verdict** recording the tree green. That verdict opens step 2.

**Schedule unchanged.** F3 closes 13 October; F4 19 October; the member-force table
23 October; the code-check screen 28 October. Two items, one a line wrap and one a sentence,
and I have no measurement that contradicts the dates. R613 is the only one that could move
them, and only if it is answered with a new gate instead of a correction; **if that is the
choice, say so the day it is made.**


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: 8e4238d654c2fbf9ebc5ab401cfe08d04b44d3a3
Verdict: HOLD
Tests: 2858 passed, 8 failed, 0 skipped   (my own run at `8e4238d`, `python -m pytest -q`, 1304.15s, one invocation, no split, no exclusion; 2866 collected)

## Round of 2026-09-30 -- SEVENTY-SEVENTH verdict. A verdict about the TREE at the closure commit, not a fourth round on step 1's work.

**Reviewed commit: `8e4238d`, the closure commit.**

**F3 step 1 IS CLOSED AND STAYS CLOSED (DD1).** Its disposition is PASS at the
seventy-sixth verdict and this verdict does not reopen it. The closure list was fixed
once, in one commit, and I have not re-reviewed it item by item. I was asked to rule on
one item that changed what a gate asserts -- C59, which is CZ0(c) -- and that ruling is
below and it is favourable.

**THE VERDICT IS HOLD BECAUSE THE TREE IS RED AT THIS COMMIT, on both machines, and
neither red was known when the commit was written.** Eight tests fail in my own run and
CI fails in a job whose failure gated out the entire guard suite. Both are CZ0(d). Both
were introduced by this commit. The step's work is sound; the commit that closes it is
not shippable.

**THE EXIT IS TWO EDITS AND ONE VERDICT, AND I AM WRITING IT DOWN SO NO ROUND IS LOST TO
THE DD1 TRAP.** This file's header will now read HOLD and the `Stop` hook reads the last
line, so the hook and DD1 will disagree exactly as `CLAUDE.md` Â§ Step gating records.
When they do, DD1 is what the disagreement is resolved against: **step 1's disposition is
PASS at verdict 76.** What is held is the TREE. Fix R611 and R612, commit, re-invoke; the
next verdict on this file records the tree green and step 2 opens. Do not write a step-2
report first, and do not read this HOLD as reopening step 1's three-round cap -- no
further round on step 1's WORK is available and I am not offering one.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 8e4238d654c2fbf9ebc5ab401cfe08d04b44d3a3 --json name,conclusion,status,event
out  [{"conclusion":"failure","databaseId":36781142834,"event":"push","name":"CI","status":"completed"}]
cmd  gh api repos/xabi80/FloatFEA/actions/runs/36781142834/jobs
out  the verification ladder            success   runner 1000001448  13 steps  21:42:37 -> 21:46:02
out  lint, unit and guards              FAILURE   runner 1000001449  14 steps  21:42:36 -> 21:42:59
out  CI determinism -- leg              skipped   runner null  0 steps
out  CI determinism -- ten legs agree   skipped   runner null  0 steps
judge RED. **Not CK2 and not unavailable**: the failing job got a real runner, ran its
      steps and returned a non-zero conclusion in 23 s. There is no billing annotation
      and no two-second started job. The two skipped determinism jobs are the same
      workflow condition as last round (`if: github.event_name == 'workflow_dispatch'`,
      and this was a push), so they are unavailable by design and not CK2 either.
      **A red CI is a HOLD regardless of what the local run says. Here the local run is
      red too.**
```

**AND THE SHAPE OF THE RED MATTERS MORE THAN THE RED.**

```
cmd  gh api .../jobs, the failing job's fourteen steps
out  1-5  success (setup, checkout, python, pip install, actionlint)
out  6    FAILURE  ruff
out  7    skipped  black --check
out  8    skipped  mypy
out  9    skipped  unit tests
out  10   skipped  guards and meta-tests
judge STEPS IN A JOB STOP AT THE FIRST FAILURE, so one line-length error meant that
      **black, mypy, the unit tests and the entire guards-and-meta-tests suite never ran
      on CI at this commit** -- including the guard C60 repointed, which is the whole
      subject of that closure item and which has therefore still never been exercised on
      the machine neither of us controls. It is the exact cost `.github/workflows/ci.yml`
      anticipates in its own comment at the ladder job: "A `ruff` line-length error would
      have hidden the whole ladder in the same way." It does not hide the ladder, because
      R335 and CM2 took the `needs:` out. It hides everything in its own job.
cmd  gh run view 36781142834 --log | grep run_rung
out  ladder 1  1276 collected, 0 failed, 0 errored, 0 skipped
out  ladder 2    66 collected, 0 failed, 0 errored, 0 skipped
out  ladder 3   218 collected, 0 failed, 0 errored, 0 skipped
out  ladder 4   127 collected, 0 failed, 0 errored, 0 skipped
out  ladder 6   134 collected, 0 failed, 0 errored, 0 skipped
judge **THE LADDER IS GREEN ON CI AT THIS COMMIT, RUNG 3 INCLUDED**, so the C59 repair
      itself is proven on the independent machine. That is why R611 and R612 are repairs
      rather than a STOP.
```

## Carried

Verdict 76 carried **no blocking item** -- it closed the step with "nothing carries by
name" -- and a closure list. **The report's own `Answers:` header is the subject of R611
below and it is WRONG at this commit (instruction 1b, DX2): its newest line reads
`Answers: verdict 75 @ 2f068c4` while the latest verdict is 76 at `78e9583`, and the
report was edited by a commit that descends from it.** I did the one comparison and it
failed; that is R611, and it is not a bookkeeping note, because the machine that normally
checks it is red for the same reason.

**Every cell below is mine.** Mutations were taken in `git worktree`s at `8e4238d` outside
this repository and restored between entries; the report-header ablation had to be taken in
this repository, because a linked worktree is not a valid environment for the report
harness -- measured, `121 failed` at an unmutated worktree baseline against `8 failed`
here. Both worktrees are removed and `git status` is clean.

* **C59 (R605) -- ANSWERED, AND THE PATH IS GENUINELY INDEPENDENT. This is the ruling the
  hand-back asked for.** The circularity was removed, not moved. Thirteen mutations,
  twelve red, and the one green is green because it moves no value.

```
rule   condition: the re-read goes to the FILE rather than through the builder's function
cmd    git show 8e4238d -- tests/verification/rung3/test_platform_skeleton.py
out    `from floatfea.model.platform import DECK_YAML` alone; `_full_scale_deck` is gone
       from the import and from the body. The only other floatfea import is
       `to_full_scale`, used once, in the basis assertion, and not in the arithmetic.
judge  SO THE SHARED SURFACE IS THE CONSTANT `DECK_YAML` AND THE `yaml` LIBRARY. The
       reader is no longer shared and the arithmetic is duplicated rather than called.
cell   R605's own cell, reproduced: `_full_scale_deck` given a module-level cache keyed on
       path and lambda, every cached joint point +3 m in x inside the cached object
out    1 failed, 52 passed  -- test_C56_the_DECK_POINTS_really_come_from_the_DECK
cell   the same cache, setdefault, NOTHING shifted
out    53 passed
judge  the implementer's four rows reproduce exactly. Batch 24 measured `53 passed` on the
       third row; it is `1 failed` now. **AND C56 IS THE SINGLE DETECTION, which I confirm
       is the right shape rather than a thin one**: DZ2's expected side is built from
       `deck_joint_points`, so under that mutation both of its sides move together and it
       is silent by construction. I read that the same way the report does.
```

**AND I ATTACKED THE DUPLICATION, WHICH IS THE PART THE HAND-BACK WAS RIGHT TO WORRY
ABOUT.** A duplicated formula fails by agreeing with the original. It does not here.

```
cell   the builder composes `to_full_scale(r) + a` instead of `to_full_scale(r + a)`
out    2 passed, 51 errors -- ValueError: the joint points span 2 elevations; this builder
       makes a PLANAR frame
cell   the builder uses `r - a`
out    2 passed, 51 errors  -- the same coplanarity refusal
cell   the joint point scaled by lambda a second time
out    2 passed, 51 errors  -- the same coplanarity refusal
cell   the builder zips `attach_b_body` instead of `attach_a_body`; the deck carries both
       and joint 0's is [0.5, 0.0, 0.0], so it is a key a reader could reach for
out    2 passed, 51 errors, and C56 is among the named errors
cell   `raw_reference` returns x and y exchanged -- IN PLANE, z untouched, no refusal
out    5 failed, 48 passed: C56 plus the four FRACTION-is-asserted-not-inferred
       parametrisations. NEITHER DZ2 TEST REDDENS.
cell   `deck_joint_owner` built from the next joint's `body_b`; no coordinate moves
out    9 failed, 44 passed -- C56 and both DZ2 families
judge  **THE DUPLICATION IS EXERCISED AND LOAD-BEARING.** Twelve of the sixteen joints
       carry a nonzero `attach_a_body` ([0.0, 0.0, 1.689037]), so the `+ a` term is not
       vacuous; the x/y row matters most, because it is in-plane, the builder accepts it,
       DZ2 is blind to it and **C56 is a detection DZ2 is not.** Four composition errors
       are caught upstream by the builder's own coplanarity refusal rather than by C56 --
       recorded as detections with the mechanism named, because folding them into C56's
       credit would over-state what this gate reaches.
```

**AND THE ONE SURFACE STILL SHARED IS PINNED, WHICH IS WHAT MAKES THE ANSWER "YES".**

```
cell   every body `reference_point` in the committed deck YAML moved +0.06 m in x, which is
       3 m at full scale. NO CODE TOUCHED. Both paths read the same wrong file.
out    the module: 53 passed. C56 is blind to this, by construction, and must be.
out    THE RUNG: 4 failed, 214 passed --
         test_G3_2_the_committed_deck_matches_its_CONTENT_digest
         test_G3_2_the_file_matches_its_RECORDED_TEXT_digest
         test_the_HEADER_agrees_with_what_the_file_CONTAINS
         test_the_arms_are_AXIAL_which_is_what_R576_turned_on
out    restored: 218 passed
judge  **THE CIRCULARITY IS NOT MOVED, IT IS CLOSED BY TWO LINKS.** `DECK_YAML` names a
       file that a content digest in `test_platform_deck_export.py` pins, and C56 pins the
       carried points to an independent read of that file. Neither link on its own is
       enough and both are shipped. This is the measurement the question deserved and I
       could not have given it from the diff.
cell   the length basis: LENGTH_EXPONENT 1.0 -> 2.0, the mutation the new comment names
out    2 passed, 51 errors -- ValueError: platform:hub1_arm L/r = 3038.7 exceeds 300. The
       builder refuses first and THE BASIS ASSERTION NEVER RUNS.
cell   LENGTH_EXPONENT 1.0 -> 1.0000001, small enough that L/r moves by a factor 1.0000009
       and the builder still accepts the platform -- the rule perturbed, not broken
out    1 failed, 52 passed, at test_platform_skeleton.py:411,
       AssertionError: assert 50.000019560118865 == 50.0
judge  **THE BRIDGE ASSERTION CARRIES ITS OWN FAILURE AND IS THE SOLE DETECTION THERE**, so
       the docstring's claim that it stops this path scaling by the wrong power is measured
       rather than asserted. At the exponent the comment names it is not the detection; at a
       perturbation the builder accepts, it is. Both rows are in the corpus.
```

**C59 IS CLOSED. It does not carry into step 2.**

* **C58 (R604) -- met.** No live count in the C56 docstring; the two mentions of `52` and
  `53` are the sentence explaining the retired figure, and the baseline is pointed at the
  step report. That is one of the two forms the condition named.
* **C60 (R606) -- met, and the three-state cell reproduces in kind.**
  `tests/test_report_numbers_are_sourced.py:72` now derives the milestone from the plan
  carrying `<!-- step-under-execution: -->`, and `docs/milestones/F3.md:9` is the only file
  carrying it, so `REPORTS` resolves to `docs/reports/F3`. **On the duplication question
  the hand-back asked me to rule: the implementer is right and I agree.** The helper is the
  twin of `tests/test_report_guard_states.py:45` including the fallback and its stated
  reason; a shared module would be new apparatus under DR1, and DR1 has no exception for a
  good one. Duplicate it. The fallback's DESTINATION is a separate closure item, C67.
* **C61 (R607) -- met.** The sentence "no test outside those three reads `docs/reports/`"
  is gone, and what replaces it is the grep, all six hits, and the reading of the four
  outside the three. The conclusion it now states is the one I verified independently.
* **C62 (R608) -- met.** `expected_pairs`'s docstring says what C56 asserts and names the
  conditionality. **My verdict-76 citation of the site was wrong** -- I wrote
  `floatfea/model/platform.py:343-344` and the function is at
  `tests/verification/rung3/test_platform_skeleton.py:344`. The implementer fixed the real
  site. My error, recorded.
* **C63 (R609) -- met, and the implementer's reasoning beats the option I offered.** The
  three rows print a pointer instead of a fragment. I offered a line number as the
  alternative and it is the wrong option for the reason given: the same line of the same
  file numbered `1637` from one reader and `1703` from another, because line numbering
  depends on newline decoding. I withdraw that half of the condition.
* **C64 (R610) -- ledger, no work, correct.** R610 was recorded as a standing cost and not
  a work item. Nothing was owed and nothing was done.
* **C40, C56(iii), C56(iv), C57 -- carried forward as recorded.** C56(iv) is named for the
  step that ships the member-force table; that step still has no number.

## My own run (instruction 3)

```
cmd  python -m pytest -q       (mine, at 8e4238d, clean tree, ONE invocation, no split, no
                                exclusion, no deselect)
out  8 failed, 2858 passed, 2 warnings in 1304.15s (0:21:44)
out  2866 collected
judge **8 failed, 2858 passed, 0 skipped.** I do not take the report's `2866 passed`, and it
      is wrong -- see R611 for why it was true when measured and false at the commit it was
      published for. My total agrees with the report's total: 2858 + 8 = 2866.
cmd  the first run overlapped my own worktree operations, so I RETOOK the eight alone,
     nothing else running, tree clean
out  8 failed, 202 passed in 203.97s -- the same eight, by name
judge NOT MY CONTAMINATION. Reproduced in isolation.
```

## Findings

**R611. (BLOCKING, CZ0(d)) Eight tests are red at the reviewed commit, and the cause is one
thing: this commit edited the step report and left the `Answers:` header naming the verdict
before last.** `docs/reports/F3/step-1.md:618`.

```
cmd    grep -n "Answers: verdict" docs/reports/F3/step-1.md
out    3:Answers: verdict 73 @ 52de940
out    256:Answers: verdict 74 @ 8ac9ce8
out    618:Answers: verdict 75 @ 2f068c4
cmd    git log --format="%h %cI" -3
out    8e4238d 2026-09-30T14:42:29  (touches docs/reports/F3/step-1.md)
out    78e9583 2026-09-30T14:07:30  (verdict 76, touches docs/reviews/F3/step-1.md)
rule   tests/test_report_carried.py:380-410. The guard returns early at the legitimate step
       boundary -- if the newest verdict commit DESCENDS from the newest report commit, the
       report predates it honestly. Here the report commit is the descendant, so the report
       was written with verdict 76 available and must name it.
out    FAILED test_the_answered_verdict_is_the_NEWEST_one
out      AssertionError: the report at `8e4238d` is newer than the verdict at `78e9583` and
       names `2f068c4`. Written with the newest verdict available, it must answer that one.
cmd    the other seven, and whether they are separate defects
out    FAILED test_the_guard_survives_the_state[baseline]
out    FAILED test_the_guard_survives_the_state[non_numeric_step_suffix]
out    FAILED test_the_guard_survives_the_state[superscript_digit_step_number]
out    FAILED test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]
out    FAILED test_the_guard_survives_the_state[step_number_is_the_empty_string]
out    FAILED test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]
out    FAILED test_the_guard_survives_the_state[zero_padded_step_number]
out    the [baseline] failure is `assert 1 == 0`, and the guard's own output inside it is
       `1 failed, 185 passed` naming `test_the_answered_verdict_is_the_NEWEST_one`
judge  ONE CAUSE, SEVEN DOWNSTREAM. The seven states seed a defect and assert what the guard
       does; with the guard already red in the unmutated baseline, every state expecting a
       pass or a specific named failure is broken. Do not chase eight items.
```

**AND THE HEADER ALONE IS NOT THE FIX. I solved for it rather than assuming.**

```
cell   ONE VARIABLE: line 618 changed to `Answers: verdict 76 @ 78e9583`, nothing else, in
       this repository, then restored
out    33 failed, 214 passed in 212.31s
judge  WORSE, AND INFORMATIVELY SO. Naming verdict 76 makes the guard check revision 3's
       `Carried` section against verdict 76's items, which revision 3 does not answer, so
       twenty-five more reds appear. **The header is necessary and not sufficient**: the
       revision that names verdict 76 has to be a revision that answers it. Under this
       guard, a closure commit that edits the report IS a revision of the report.
```

**AND THIS IS WHY THE REPORT'S `2866 passed` WAS TRUE WHEN TAKEN AND FALSE WHEN PUBLISHED**,
which is the figures-at-the-commit rule in its exact form and the second time C43 has
ledgered this shape.

```
judge  the guard's answer is a function of the COMMIT GRAPH. Run with the report edits
       uncommitted, `git log -1 -- docs/reports/F3/step-1.md` returns 1b3fb73, which IS an
       ancestor of 78e9583, so the guard returns early and the eight are green. The commit
       is what makes them red. A whole-tree count taken before the commit it describes
       cannot see this class of red at all, and this is the class the count exists for.
```

**Closed when** the newest `Answers:` line in `docs/reports/F3/step-1.md` names verdict 76
at `78e9583` **and** the revision carrying it answers verdict 76's items, and `python -m
pytest tests/test_report_carried.py tests/test_report_guard_states.py -q` is `0 failed` at
the commit that ships it -- measured at that commit, not before it.

**R612. (BLOCKING, CZ0(d)) CI is red at the reviewed commit, on a line the C59 repair
introduced, and the failure gated out the whole guard suite.**
`tests/verification/rung3/test_platform_skeleton.py:414`.

```
cmd    python -m ruff check floatfea tests          (ruff 0.15.12, line-length = 100)
out    E501 Line too long (101 > 100)
out      --> tests/verification/rung3/test_platform_skeleton.py:414:101
out      414 | reference = {body["name"]: [float(c) for c in body["reference_point"]] for body in raw["bodies"]}
out    Found 1 error.
cmd    awk 'NR==414{print length($0)}' tests/verification/rung3/test_platform_skeleton.py
out    101
cmd    python -m black --check floatfea tests
out    would reformat tests/verification/rung3/test_platform_skeleton.py
out    1 file would be reformatted, 88 files would be left unchanged.
cmd    python -m mypy floatfea
out    Success: no issues found in 29 source files
rule   .github/workflows/ci.yml:370-388 -- ruff, then black, then mypy, then the unit tests,
       then the guards, as steps of ONE job; steps stop at the first failure
judge  TWO of the three lint gates are red and both are the same line. `pytest` runs neither,
       so the report's whole-tree run could not have seen this and did not claim to -- but
       the commit shipped with the lint gate red and nothing in the implementer's own loop
       reads it. One finding with two commands, because it is one line. mypy is clean, so
       there is nothing behind the gate but the formatting and the suite R611 covers.
```

**Closed when** `ruff check floatfea tests` and `black --check floatfea tests` are both
clean, and CI's `lint, unit and guards` job reaches `guards and meta-tests` and succeeds at
the commit that ships the fix. **Reformat the line; do not raise `line-length`.** A
threshold moved to make a red check green is the same error under another name, and
`pyproject.toml:89` and `:93` both carry it.

**R613. (BLOCKING, CZ0(c), and STOP-class ON THE PLAN -- it carries by name into step 2, and
`docs/milestones/F3.md` Â§ 5 reopens for one sentence before step 2's G2.1 row is written.)
The near-vertical band step 2 must measure first is EMPTY on the real platform, and the plan
contradicts its own measurement two sections earlier.** `docs/milestones/F3.md` Â§ 5, "What
F3 must check that F2 could not".

```
claim  the plan's sentence: "A platform frame is mostly near-vertical members, so this gate
       is measured there first."
cmd    build_superstructure(), every member of every body, direction cosine, angle from
       vertical
out    16 members. max |dz| over all sixteen = 0.0 EXACTLY.
out    angle from vertical = 90.0 degrees for every one of the sixteen.
out    platform:hub1_arm .. platform:hub4_arm   L = 50.0 m, dz = 0.0
out    hubN:buoyM_arm, twelve of them           L = 25.0 m, dz = 0.0
rule   the gate F3 Â§ 5 asserts: element_rigid_residual(k_local, L) <= RIGID_MODE_EXACTNESS
       on every member of the real platform at its real orientation, measured in the
       near-vertical band FIRST
cell   the plan's own Â§ 3.1, which measured the premise and got the opposite answer:
       "z spread max - min = 0.000e+00 m", "dz = 0.000e+00", "The frame is planar."
judge  **THE REAL-MEMBER SET CONTAINS NO NEAR-VERTICAL MEMBER AND CANNOT, BECAUSE DW1 LOCKED
       THE FRAME PLANAR.** Every member is exactly horizontal. The instruction "this gate is
       measured there first" has an empty subject on this model, and the causal sentence
       attached to it is false for the platform this milestone builds -- BG0's shape in the
       locked plan, with the refuting cell already inside the same document.
judge  WHY THIS IS (c) AND NOT PROSE. Written as specified, step 2's band check is a
       parametrisation over real members within some angle of vertical, and that glob finds
       nothing: **an empty parameter set reads green while checking nothing**, which is a
       recorded guard and the cheapest way for this gate to certify nothing. The alternative
       -- inventing near-vertical members to fill the band -- makes the row a statement
       about structures in general, which DD0 explicitly moved out of F2. Either way what
       the gate asserts has to change, and that is CZ0(c).
```

**Closed when** `docs/milestones/F3.md` Â§ 5 says which of the two it means -- the ceiling
asserted on the sixteen real horizontal members with the near-vertical band recorded as
**not reachable on this model** (naming any orientation sweep as a separate, non-real-member
check if it is wanted at all), or the band redefined against a quantity the real member set
contains -- and the "mostly near-vertical" sentence is deleted or replaced by what Â§ 3.1
measured. **I am not issuing a bare STOP because the tree is already held by R611 and R612
and because the gate's own assertion is executable on the sixteen members; I am naming the
plan-reopen consequence explicitly rather than letting a HOLD swallow it.** If Â§ 5 is read
as binding as written, treat this as the STOP it is and reopen the plan before anything else.

## Tolerances touched

```
cmd  git diff 78e9583..8e4238d -- floatfea/tolerances.py
out  (no output)
cmd  git diff 78e9583..8e4238d --stat -- floatfea
out  (no output)
cmd  git show --stat 8e4238d
out  docs/reports/F3/step-1.md                          | 72
out  scripts/carried_table.py                           | 24
out  tests/test_report_numbers_are_sourced.py           | 32
out  tests/verification/rung3/test_platform_skeleton.py | 77
cmd  grep -n "MASS_PROPERTY_AGREEMENT: Final" floatfea/tolerances.py
out  1531:MASS_PROPERTY_AGREEMENT: Final[float] = 1e-13      -- unchanged
```

**None.** No value added, changed, removed or widened; no comment in that file touched; and
**no file under `floatfea/` changed at all in this commit**, so there is no code for a
tolerance to have rescued. The one numeric constant this commit could have reached for is
`pyproject.toml`'s `line-length = 100`, and it did not -- see R612, which must stay that way.

## The corpus round (BE3, scope DE2)

`tests/corpus/platform_geometry_provenance_independent_read.txt`, **batch 25, committed
separately.** A new file rather than rows appended to batch 24, because C59 changed the rule
-- what the expected side is derived from -- and a corpus row kept across a rule change is
BP0 in corpus form.

**17 entries, all 17 new this round and none of them read by the implementer before this
verdict. Thirteen carry a mutation. TWELVE CAUGHT, ONE GREEN -- and the one green is green
CORRECTLY, because the mutation moves no value. ZERO REAL MISSES.** Against 6 of 11 with
three real misses in batch 24, 11 of 16 in batch 23, 9 of 17 in batch 22.

**I state what the zero rests on, so nobody reads it as the gate being complete.** Three
independent links, each measured in the file: the deck file is digest-pinned; C56 pins the
carried points to an independent read of it; the builder refuses a non-planar,
mis-topologised or over-slender deck. Remove any one and rows go green. **And six of the
twelve detections are builder refusals rather than gate assertions** -- recorded as
detections with the refusal named, because folding them into C56's credit would over-state
what the gate under review reaches. That distinction is why the number is worth reading.

**The three rows worth more than the ratio.**

```
cell   a 17th joint duplicating the first joint's `body_a`, attach +7 m in x
out    2 passed, 51 errors -- ValueError: expected 4 hub-platform joints and 12 buoy-hub
       joints; got 4 and 13. The topology is not the platform this builder describes.
judge  THE REPAIR DID WEAKEN ONE ASSERTION AND THE WEAKENING IS UNREACHABLE. The old test
       asserted `len(carried) == len(fresh["joints"]) == 16` -- a JOINT count. The new one
       asserts `len(carried) == len(fresh) == 16`, and `fresh` is keyed by `body_a`, so a
       duplicate key collapses on BOTH sides identically and 17 joints read as 16. The
       builder's topology refusal catches it first, so this is reach and not (c) and I am
       not blocking on it -- but it is written down against the day that refusal moves.
cell   the deck FILE shifted, no code touched
out    module 53 passed; RUNG 4 failed
judge  the answer to the hand-back's question, and the reason it is "independent" rather
       than "moved".
cell   LENGTH_EXPONENT perturbed by 1e-7 rather than doubled
out    1 failed at test_platform_skeleton.py:411 -- the basis assertion, alone
judge  the decision rule inverted rather than sampled. At the exponent the comment names,
       the builder refuses first and the assertion never runs; at a perturbation the builder
       accepts, the assertion IS the gate. Both rows are in the file so the next reader does
       not have to re-take either.
```

Per DE2 this batch is the platform model and the gate that proves it, not apparatus. **No
apparatus corpus was written or grown.**

```
cmd  python -m pytest <the ten files under tests/ that read tests/corpus> -q, with batch 25 in
out  405 passed in 452.02s
judge adding the file reddens nothing. It does NOT clear R611: the two report-harness files
      are red for their own reason and were measured separately, above.
```

## Process checks (4, 4b, 4c, and the commit classes)

```
cmd  git diff 4b0ad7a..8e4238d -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git show 8e4238d -- .claude docs/SUPERVISOR.md docs/reviews
out  (no output)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 4b0ad7a..8e4238d -- tests/conftest.py 'tests/**/conftest.py'
out  (no output)
judge my own instructions untouched; the pathspec returns the file that exists rather than
      the empty set; NO conftest changed and no plugin added to any rung run, so there is no
      report-rewriting hookwrapper and no collection filter to read line by line this round.
      The closure commit touches `docs/reviews/` not at all. The 2836-line change to
      `docs/reviews/F3/step-1.md` in the wider range is verdict 76, my own commit 78e9583.
cmd  the two commits in range, by path class
out  78e9583 docs/reviews/ only (mine) | 8e4238d docs/reports/ + scripts/ + tests/
judge ONE commit for the closure list, as CZ0 asks, and it touches neither `floatfea/` nor
      `docs/reviews/`. No commit touches both `floatfea/` and my own instructions.
```

## Closure items

**Fixed once, in the next closure commit, and not re-reviewed item by item.** None blocks.

* **C65.** `docs/reports/F3/step-1.md:809` -- the new C40 block's `rule` line says C60 fixed
  the fifth file "because it fails false -- it measures a closed milestone". Verdict 76 said
  the opposite in as many words: "this one does not fail false either, it simply measures a
  closed milestone". Those are two different defects and the report attributes mine to the
  wrong one. **Closed when** the line says what the verdict said, or says it disagrees and
  why.
* **C66.** `docs/reports/F3/step-1.md:813` -- the line after that fenced block begins with a
  space and runs onto the fence (" It is the one of the five..."), so the paragraph reads as
  one broken sentence. **Closed when** the block and the paragraph are separated.
* **C67.** `tests/test_report_numbers_are_sourced.py:66` and its twin
  `tests/test_report_guard_states.py:74` -- the milestone helper returns `"F2"` when the
  marker is found in zero plans or in more than one. The failure mode R606 named is "green
  forever on a closed milestone's report", and the fallback is a path straight back to it:
  delete the marker at F4 and both guards go quiet rather than red. The import-time reasoning
  (R234) is sound; the destination is not. **Closed when** the fallback is a state the suite
  reports rather than a silent reversion. Ledgered as one item because the two must stay
  identical under DR1.
* **C68.** `tests/test_report_guard_states.py` leaves `tests/test_report_carried.py` and
  `docs/reports/F3/step-1.md` MODIFIED in the working tree when a state fails -- measured,
  `M tests/test_report_carried.py` and `M docs/reports/F3/step-1.md` after a failing run, and
  a second run in that state reports `121 failed` on its own debris. **Closed when** the
  mutation is restored in a `finally`, or the tree state is asserted after the run.
  Apparatus, so it is a closure item; recorded because it cost me a round of measurement to
  tell debris from a real red.
* **C69.** `.git/worktrees/` holds 119 entries, and three `suite-count-*` worktrees dated
  11 September are still registered at commits that are not HEAD. `git worktree remove` now
  fails with `Permission denied` on unrelated entries. **Closed when** the stale metadata is
  pruned. Housekeeping, but it is now interfering with the harness's own tool.
* **C70.** The basis assertion at `tests/verification/rung3/test_platform_skeleton.py:411` is
  vacuous at `lambda = 1`: measured, the comparison holds with the exponent at 1.0 and still
  holds with it at 7.0 when lambda is 1.0, while at lambda 50.0 with exponent 7.0 it is
  False. The fixture builds at 50.0, so it is not vacuous today and nothing says it depends
  on that. **Closed when** the dependence is stated at the site, or the assertion is written
  in a form with no fixed point at lambda = 1.
* **C71.** `Superstructure` carries eight fields and none is the deck path it was built from,
  while `build_superstructure` accepts any path. C56 therefore asserts provenance for the
  DEFAULT build and cannot in principle check one built from another deck. **Closed when**
  the object records its source, or C56's docstring says the claim is about the default build.
* **C72.** `scripts/write_verdict.py` -- the CRLF defect the implementer reported is real and
  I reproduced it on a scratch copy rather than on the file: reading the current 1661-line
  verdict file and writing it back the way that script does gives `CRLF 1663, CRCRLF 1660`,
  so 1660 of 1661 preserved lines gain a stray carriage return per round. **I agree with the
  implementer that neither of us should patch it and I have not.** It is apparatus under DR1,
  `docs/SUPERVISOR.md` names it as mine, and a reviewer editing its own tooling inside a step
  is the shape `CLAUDE.md` makes STOP-class. It needs a directive and the implementer has
  raised it. **For this round I normalised my own file's line endings to LF before invoking
  the script**, so the single translation produces clean CRLF; that is a mechanical repair of
  the one file I own and it is recorded here so it is not mistaken for a fix.
* **C73. (plan note, for the reopen R613 already requires, not a separate round)** The locked
  plan still does not say whether a provenance assertion may re-read through the code under
  test. CJ0 says it for the harness; nothing says it for the model, and R605 existed because
  the answer was assumed. The duplication C59 creates is the other half: the deck-to-point
  mapping is now written twice, and a legitimate change to it must be made in both places,
  where the natural second edit is a copy of the first. Measured to be load-bearing today;
  unstated as a rule.

## On the criterion, said once

**I do not disagree with CZ0 and this verdict spends no round on prose.** R611, R612 and
R613 are (d), (d) and (c). Everything else is in the closure list above and I have held
nothing on it. The one item I was asked to rule -- C59 -- is closed, and I said so first
rather than burying it under the reds.

**What I want on the record, once, is that the closure commit is the weakest point in this
mechanism and nothing measures it.** A step's three rounds are reviewed; its closure commit
is written after the last one and is not reviewed by rule, and this one shipped two reds --
one of them in the guard `CLAUDE.md` names as the mechanical half of BF0, red for the
mechanical reason that the commit exists. Both were invisible to the implementer's own loop
by construction: `pytest` does not run `ruff`, and the report guard's answer depends on the
commit graph, so a pre-commit run cannot see it. **I am not asking for apparatus** -- DR1
forbids it and the corpus rounds are not it. I am recording that "the closure commit is not
re-reviewed item by item" was read, reasonably, as "the closure commit is not reviewed at
all", and that the cheapest available correction is the one already required of a report: run
the checks at the commit, after it exists. That goes to Xabier as a note about CZ0's wording,
not as a round, and it does not change my verdict here.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the
code-check screen 28 October. **Step 1 closed on 30 September carrying no blocking item, so
DZ7c's reduce-scope branch is not triggered** -- but step 2 has not opened, and R611, R612
and R613 stand between it and opening. R611 is a header and a revision, R612 is a line wrap,
R613 is a sentence in the plan. None is days of work and the dates stand, on the condition
that R613 is resolved as a plan edit rather than as a new gate. **If R613 turns into a new
orientation gate, the 13 October date should be re-stated the day that is decided, not when
step 2 closes.**

## Next step opens when

**Step 2 does not open yet. F3 step 1 remains CLOSED at PASS (DD1, verdict 76); what is held
is the TREE at the closure commit.**

1. **R611 closed** -- the newest `Answers:` line names verdict 76 at `78e9583`, the revision
   carrying it answers verdict 76's items, and `python -m pytest tests/test_report_carried.py
   tests/test_report_guard_states.py -q` is `0 failed` **at the commit that ships it**. The
   header alone is measured insufficient (`33 failed`); do not stop there.
2. **R612 closed** -- `ruff check floatfea tests` and `black --check floatfea tests` clean,
   by reformatting line 414 and not by moving `line-length`; and CI's `lint, unit and guards`
   job reaches `guards and meta-tests` and succeeds at that commit. **Paste the `gh run list`
   line, not a local green** -- the guard suite has not run on CI since `1b3fb73`.
3. **R613 closed** -- `docs/milestones/F3.md` Â§ 5 no longer instructs a measurement whose
   subject is empty, and no longer says the platform frame is mostly near-vertical. This
   reopens the plan for one sentence; under DK0 that buys no rounds and I am not offering
   any. **R613 carries by name into step 2's `Carried` section and stays blocking there until
   Â§ 5 is edited**, because it is the first thing step 2's G2.1 row has to be written against.
4. **Then one verdict on this file**, recording the tree green. That verdict, not this one,
   opens step 2.

**Nothing else carries.** C59 is closed and does not carry. C58, C60, C61, C62, C63 and C64
are met. C65 to C73 are closure items and hold nothing.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: 4b0ad7a2c24ce53191f7883fa35c5cd919d3d7bd
Verdict: PASS
Tests: 2862 passed, 0 failed, 0 skipped   (my own run at `1b3fb73`, `python -m pytest -q`, 1401.74s, one invocation, no split, no exclusion, exit 0)

## Round of 2026-09-30 -- SEVENTY-SIXTH verdict, round 3 of 3 on F3 step 1. THE STEP CLOSES.

**Reviewed commit: `1b3fb73`.**

**Both blocking items are answered and I verified each by the cheapest check that could
refute it.** R602 and R603 are closed. My own whole-tree run is `0 failed` and CI at the
reviewed commit is **green in every job that ran, including the verification ladder and
including rung 3, which is the rung this step is about.** That is the pair verdict 75 named
as the closing condition, and it is met.

**Nothing found this round is blocking.** Under CZ0 the step closes with PASS, nothing
carries by name, and the closure items below go into the step's closure artifact as one
list. The corpus round found one shape worth more than the rest of this verdict and it is
R605; it is reach rather than defect, so it does not hold the step, and I say plainly that
it is the item I would spend the next commit on.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 1b3fb7344686b8545faf5c53a55272d3b8424a24 --json conclusion,status,databaseId
out  [{"conclusion":"success","databaseId":36768565948,"status":"completed"}]
cmd  gh run view 36768565948 --json headSha,status,conclusion,event
out  headSha 1b3fb7344686b8545faf5c53a55272d3b8424a24; push; completed; conclusion SUCCESS
cmd  gh api repos/xabi80/FloatFEA/actions/runs/36768565948/jobs
out  the verification ladder            success   runner 1000001444  13 steps  19:51:31 -> 19:54:58
out  lint, unit and guards              success   runner 1000001445  14 steps  19:52:06 -> 20:03:03
out  CI determinism -- leg              skipped   runner null  0 steps
out  CI determinism -- ten legs agree   skipped   runner null  0 steps
cmd  gh run view 36768565948 --log, the rung tallies and the two pytest summaries
out  ladder 1 -- the solver is a solver      run_rung: 1276 collected, 0 failed, 0 errored, 0 skipped
out  ladder 2 -- the element is the element  run_rung:   66 collected, 0 failed, 0 errored, 0 skipped
out  ladder 3 -- the model is the platform   run_rung:  218 collected, 0 failed, 0 errored, 0 skipped
out  ladder 4 -- the loads are the loads     run_rung:  127 collected, 0 failed, 0 errored, 0 skipped
out  ladder 6 -- it stays fixed              run_rung:  134 collected, 0 failed, 0 errored, 0 skipped
out  unit tests             88 passed in 0.53s
out  guards and meta-tests  953 passed, 1 warning in 618.64s
judge GREEN. Not `unavailable` and not `allowance exhausted`: both scheduled jobs got a
      runner, ran their steps and succeeded.
```

**THE TWO SKIPPED JOBS ARE A WORKFLOW CONDITION AND NOT CK2, AND I CHECKED WHICH.**

```
cmd  grep -n "determinism" -A 6 .github/workflows/*.yml
out  :85  name: "CI determinism -- leg"
out  :90  if: github.event_name == 'workflow_dispatch'
judge this was a `push`, so the two jobs were gated off by design. `runner_name: null` and
      `steps: []` here are the CONDITIONAL-SKIP shape, not CK2's -- there is no billing
      annotation and no two-second started job. So: not red, not exhausted, and not green
      either. **The determinism check is UNAVAILABLE at this commit by workflow design**,
      as it has been at every push-triggered commit, and rung 3 does not depend on it.
```

**And the disagreement that made verdict 75 a HOLD is gone in the direction that matters.**
Last round CI had three reds and I had one; the two extra were exactly the two
`_seed_older_verdict` states. This round both machines agree at zero. That is R603's
ablation completed by the only machine that could complete it.

## Carried

Verdict 75 carried two blocking items, R602 and R603, and closure items C12, C14, C18 to
C32, the open part of C33 to C39 and C42, C43 to C47, and C50 to C57. **The report's header
reads `Answers: verdict 75 @ 2f068c4`, which is my own verdict commit and the LATEST
verdict (instruction 1b and DX2: satisfied, one comparison, and it is the right one).**

**Every cell below is mine**, run in a `git worktree` at `1b3fb73` outside this repository
and restored between mutations. The worktree is removed and `git status` is clean.

* **R602 -- ANSWERED, and answered in the form I measured and named.**

```
rule   condition: the newest revision no longer carries the anchor literal in a position
       preceding the real header, and the state passes
cmd    grep -n "Answers: verdict" docs/reports/F3/step-1.md
out    3:Answers: verdict 73 @ 52de940
out    256:Answers: verdict 74 @ 8ac9ce8
out    618:Answers: verdict 75 @ 2f068c4
cmd    grep -c "Answers: verdict" docs/reports/F3/step-1.md
out    3
judge  EXACTLY THREE, each one a revision header, none in prose. `rindex` lands on 618,
       which is revision 3's own header. The hand-back asked me to check this hardest and
       it holds.
cmd    the fix, at eb8e165
out    the quoted generator message is replaced by a DESCRIPTION, with the reason at the
       site. `docs/` only, no apparatus touched -- the cheapest form, which is the one
       I named.
judge  and the record is corrected. `b2e59b0`'s message said the state "expects a check the
       repository decided to give up"; `eb8e165` says that is false and that the check at
       `tests/test_report_carried.py:320` is live. A wrong reason in the tree outlives the
       red, and this one did not.
```

**AND I CHECKED THE OTHER ANCHOR, WHICH NOBODY ASKED ABOUT.** `bad_answers_sha` is not the
only positional anchor in that harness.

```
cmd    grep -n "rindex" tests/test_report_guard_states.py
out    413  head = text.rindex("Answers: verdict")      (bad_answers_sha)
out    472  head = text.rindex("Answers: verdict")      (older_answers_sha)
out    545  head = text.rindex("# Revision ")           (pointers_all_at_carried)
cmd    grep -n "# Revision " docs/reports/F3/step-1.md
out    254:# Revision 2 -- verdict 74's two findings
out    616:# Revision 3 -- verdict 75's two findings, and the provenance check
judge  two occurrences, the last is revision 3's own heading, so the THIRD anchor is sound
       too. Three anchors checked, three correct. No prose anywhere in that file puts a
       harness anchor after the line it anchors on.
```

* **R603 -- ANSWERED. The move is named, it is the one that changes nothing about what any
  guard checks, and CI is where it was proved.**

```
cmd    git show 1d623c1 -- tests/test_report_guard_states.py
out    the `git commit` argv in `_seed_older_verdict` gains `-c user.name=harness` and
       `-c user.email=harness@localhost`, verbatim as the two adjacent sites in `_build`
       already carry them, with the reason at the site. `tests/` only.
cmd    git show 1d623c1 --numstat -- tests/test_report_guard_states.py
out    20  1
judge  ONE deletion, and it is that argv. No hook of any kind was added -- I read the hunk
       line by line as 4c requires: no `pytest_runtest_makereport`, no
       `pytest_ignore_collect`, no `pytest_collection_modifyitems`, no `pytest_runtest_call`,
       no `force_result`, and no assertion weakened. `assert code != 0` is untouched.
cmd    the three states named by R602 and R603, on CI at 1b3fb73
out    0 failed. The exit-128 / CalledProcessError signature is gone from the run.
judge  ANSWERED, and by the machine that had to answer it. The defect was invisible here by
       construction, so a local green would not have closed it.
```

* **R600, R601 -- closed in verdict 75, not carried, and nothing this round reopens either.**

## My own run (instruction 3)

```
cmd  python -m pytest -q      (mine, at 1b3fb73, clean worktree, ONE invocation, no split,
                               no exclusion, no deselect)
out  2862 passed, 2 warnings in 1401.74s (0:23:21)
out  exit 0
judge 2862 passed, 0 failed, 0 skipped. I do not take the report's counts and I did not
      need to: this supersedes the report's section 8 line entirely, and it is a
      measurement of the COMMITTED tree at the reviewed commit rather than an argument
      about one. See R607 for the ruling the hand-back asked for.
```

## Findings

**R604. (closure) The new test's docstring publishes `52 passed` in the very commit that
made the baseline `53`.** `tests/verification/rung3/test_platform_skeleton.py:372-373`:
"with `deck_joint_points` overwritten from the built nodes, the whole module gives
`52 passed`."

```
cmd    python -m pytest tests/verification/rung3/test_platform_skeleton.py -q, at 1b3fb73
out    53 passed in 0.52s
cmd    the same after overwriting `deck_joint_points` from the built nodes, one variable
out    53 passed
judge  the figure was correct when I measured it at b2e59b0 and 086a2c7 is the commit that
       falsified it, by adding the test whose docstring quotes it. BP0 in its exact form --
       a figure republished across the change that moved it -- landing in a docstring, in
       the commit answering a finding about unbacked prose. Nothing regenerates a docstring.
```

**Closed when** the docstring says `53 passed` or names no count and points at the step
report, which is regenerated by rule.

**R605. (closure, and it is the one I would spend the commit on) C56(i)'s fresh read is
fresh only because nothing caches it, and the shape it was built to close survives one
level up.** `tests/verification/rung3/test_platform_skeleton.py:383` reads the deck through
`_full_scale_deck`, the same function the builder used.

```
cell   ONE VARIABLE: `_full_scale_deck` given a module-level cache keyed on path and lambda,
       so C56's "fresh" read returns the very object the builder used. Nothing else touched.
out    53 passed   -- correct, no value moved
cell   the same cache AND every deck joint point shifted +3 m in x inside the cached object
out    53 passed
judge  THE WHOLE FRAME IS 3 M WRONG AND THE MODULE IS GREEN -- C56, both DZ2 tests and the
       buoy-node test. A provenance check that re-reads through the builder's own function
       is circular the moment that function returns a shared object, which is R600's shape
       at the assertion built to close R600.
cmd    grep -n "lru_cache\|_DECK_CACHE\|cache" floatfea/model/platform.py
out    (no output)
judge  REACH, NOT DEFECT: nothing memoises that function at this commit, so CZ0(a) is not
       engaged and I am not blocking. It is also not a moved goalpost -- verdict 75's own
       closing condition specified re-reading THROUGH `_full_scale_deck`, so the
       implementer built exactly what I asked for and the hole is in what I asked for.
```

**Closed when** the re-read goes to the file rather than through the builder's function --
`Deck.model_validate` on `DECK_YAML` inside the test, or a hash of the YAML bytes compared
against one the builder records -- or the plan states that in-tree memoisation of the deck
read is out of scope, the way CJ0 states the forgery boundary.

**R606. (closure) A FIFTH file hardcoded to F2, and it is the one that enforces BF0.**
`tests/test_report_numbers_are_sourced.py:42` reads `REPORTS = ROOT / "docs" / "reports" / "F2"`.

```
cmd    grep -n '"reports"' tests/test_report_numbers_are_sourced.py
out    42:REPORTS = ROOT / "docs" / "reports" / "F2"
judge  so the guard `CLAUDE.md` names as what "enforces most of this mechanically" -- a
       number in prose must appear in a command block of its own section -- has never read
       an F3 report and never will. It is green, on F2's newest step report, forever.
       C40 was ledgered on the reading that the hardcoded ones do not fail false; this one
       does not fail false either, it simply measures a closed milestone, which is the same
       cost R601a found in three other files and a different one from
       `test_plan_matches_tolerances.py` (that reads F2.md for a table that is really there).
judge  CZ0 puts guards in the closure list explicitly, so this is not blocking. Recording it
       because C40's ledger currently reads as four files and the family is five.
```

**Closed when** C40's ledger names this file too, or the constant follows the plan marker
the way `test_report_guard_states.py` now does.

**R607. (closure) The section 8 ordering argument -- THE RULING THE HAND-BACK ASKED FOR.**
`docs/reports/F3/step-1.md:990-994`.

**The conclusion is right and I verified it independently. The sentence carrying it is
false, and it is false to one grep.**

```
claim  the report's load-bearing premise: "no test outside those three reads `docs/reports/`"
cmd    grep -rln 'docs/reports' tests/ --include=*.py
out    tests/test_ci_workflow_is_wellformed.py
out    tests/test_report_carried.py
out    tests/test_report_guard_states.py
out    tests/test_tree_prose_consistent.py
out    tests/verification/rung3/test_tolerance_counter_cases.py
out    tests/verification/rung4/test_writer_round_trip.py
judge  four files outside the three, one of them in LIVE CODE at
       `test_ci_workflow_is_wellformed.py:97`. The needle-changed check moves the answer, so
       the grep can fail.
cmd    read each of the four
out    :97 asserts `docs/reports/**` is in the workflow's `paths-ignore` -- it reads
       `.github/workflows`, never the report
out    test_tree_prose_consistent.py:4 and :102 say `docs/reports/` is NOT in scope
out    the rung3 and rung4 hits are docstring mentions
judge  SO THE CONCLUSION HOLDS: no test outside those three reads the report's CONTENTS, and
       an edit to it cannot move the 2633. The sentence overstates that into something a
       grep refutes, which is BF0's own species inside a paragraph that correctly labels
       itself an argument.
```

**And on whether the line must be retaken: no, because I retook it.** `2862 passed, 0
failed, 0 skipped` at `1b3fb73`, one invocation over the whole tree with nothing excluded,
is in this verdict and supersedes both the 2633 and the excluded-set pair. An argument is
not a measurement and the rule asks for the measurement -- but the reviewer's own run is
where the gate actually reads the number, and it is taken at the reviewed commit. **Closed
when** the sentence is reduced to what the grep supports, or when the line is generated
after the last edit; and the count itself needs nothing, it is above.

**R608. (closure, carried prose, not touched this round) `expected_pairs`'s docstring still
claims more than the tree supports.** `floatfea/model/platform.py:343-344`: "both filled
from the deck's joints, neither of which any part of the model construction can influence."

```
cell   ONE VARIABLE: `deck_joint_points` rebuilt in the constructor from the BUILT nodes,
       same sixteen keys
out    53 passed
judge  model construction CAN influence them. With C56 shipped the claim is now backed as
       a test -- CW0's first permitted form -- but only CONDITIONALLY: C56 sees it when a
       value also moves and is silent when nothing moves (and silent altogether under
       R605). The sentence is an absolute where the tree supports a conditional.
```

**Closed when** the clause reads what C56 asserts -- that the carried points equal a fresh
read of the deck -- rather than that construction cannot reach them.

**R609. (closure) C51's residual: the status stopped over-claiming and the subject beside it
did not.** `docs/reports/F3/step-1.md:964-966`.

```
out    | R596 | **not classified in this verdict** -- carried in from an earlier one |
         are closed. Closure items C12, C14, C18 to C32, the open |
judge  the status is honest now, which is exactly the half of C51 I named as acceptable, so
       C51 IS MET. What remains is the subject: a mid-sentence fragment beginning "are
       closed." beside a row that declines to say whether it is closed. `127c7b1`'s own
       check -- no subject BEGINS with a finding number -- passes and was the wrong needle
       for this half.
```

**Closed when** the subject is dropped where the generator cannot find a sentence start, or
the row prints the verdict line number instead of a fragment of it.

**R610. (ledger to `docs/milestones/F2a.md`, no work) The harness's anchors are positional
and unguarded, by a decision I agree with.** Three states depend on the literal
`Answers: verdict` and the string `# Revision ` being LAST in a file the implementer writes
freely every round. This round it broke once and was caught by the implementer before
committing; last round it broke and was not. DR1 forbids repairing it and deletion would
cost three working negative controls. **Recorded as a standing cost, not a work item**, and
the note `eb8e165` left at the site is the whole mitigation available under the freeze.

## Tolerances touched

```
cmd  git diff 2f068c4..1b3fb73 -- floatfea/tolerances.py
out  (no output)
cmd  git diff 2f068c4..1b3fb73 --stat -- floatfea
out  (no output)
cmd  grep -n "MASS_PROPERTY_AGREEMENT: Final" floatfea/tolerances.py
out  1531:MASS_PROPERTY_AGREEMENT: Final[float] = 1e-13      -- unchanged
```

**None.** No value added, changed, removed or widened; no comment in that file touched; and
**no file under `floatfea/` changed at all this round**, so there is no code for a tolerance
to have rescued.

**AND C55 IS ANSWERED BY CORRECTING MY OWN FIGURE, WHICH IS THE RULING THE HAND-BACK ASKED
FOR. The implementer's reading is right and mine was wrong.**

```
cmd    MASS_PROPERTY_AGREEMENT * body_extent(body), five bodies, mine
out    platform  extent 51.056247 m  grid 5.1056e-12 m
out    hub1..4   extent 25.000000 m  grid 2.5000e-12 m
cmd    max |built tip - its own deck point|_inf over sixteen tips and five bodies, mine
out    0.0000e+00 m EXACTLY
cmd    the distance from each platform-body hub-tip coordinate to its OWN cell boundary,
       solved as (0.5 - |frac(p/g) - 0.5|) * g rather than sampled -- the rule inverted
out    hub1 x = 50.0                  7.7781e-13 m
out    hub1 y = 0.0                   0.0000e+00 m        <- ON a boundary
out    hub2 x = 3.0616e-15            3.0616e-15 m        <- ON a boundary
out    hub2 y = 50.0                  7.7781e-13 m
out    hub3 x = -50.0                 7.7781e-13 m
out    hub4 y = -50.0                 7.7781e-13 m
out    the shared z = 24.668478...    1.4360e-12 m
judge  **THE DETECTION THRESHOLD IS NOT A PROPERTY OF THE GATE AND MY `+7.1054e-13 m` WAS
       NOT ONE.** It is a coordinate's distance to its own cell boundary. Over the platform
       body it runs from 0.0000e+00 m to 1.4360e-12 m -- so the implementer's caveat that it
       "can be arbitrarily small for a coordinate that happens to sit on a boundary" is not
       hypothetical, two of these coordinates ARE on one. My figure is also not the exact
       boundary distance at hub1 x: that is 7.7781e-13 m and my ULP walk stopped nine ULPs
       short. Their published range 1.7728e-12 to 3.3218e-12 m is a THIRD quantity -- a deck
       hub joint shifted, which moves the platform's tip and the hub's centre at two
       different grids -- correct for what it measures and understating the spread.
rule   set(pairs) == expected_pairs(...), both sides rounded to
       MASS_PROPERTY_AGREEMENT * body_extent
judge  AND THE VALUE AND FORM ARE BOTH RIGHT, so there is nothing here to change. The grid
       is relative and dimensionless, the baseline offset is exactly zero, so the entire
       grid is headroom and the worst discrepancy the rounding can hide is just under
       5.1056e-12 m -- twelve orders below anything physical. A 3 m tip shift reddens 9. The
       gate carries its own failure and the threshold cannot hide a real defect.
```

## The corpus round (BE3, scope DE2)

`tests/corpus/platform_geometry_provenance.txt`, batch 24, committed separately at
`4b0ad7a`. **16 entries, all new this round.** Eleven carry a mutation; five are deck facts,
solved boundaries or questions for the plan and are not counted either way.

**Of the eleven mutations, the shipped suite CAUGHT 6 and was GREEN on 5 -- and of those
five, TWO are green correctly because the mutation moves no value, so THREE ARE REAL
MISSES.** I state the carve-out rather than folding it into the numerator: a row green
because nothing moved is not a detection the suite made, and it is not a defect it let
through either. Against 11 of 16 in batch 23, 9 of 17 in batch 22, 9 of 16 in batch 21.

**The two rows that are worth more than the ratio.**

```
cell   each hub's three cluster tips rotated EXACTLY 120 degrees about that hub's own node --
       drawn from the tripod's own symmetry, so the tip SET maps onto itself by construction
out    4 failed, 49 passed, and all four are test_DZ2_each_BUOY_lands_on_the_node_the_DECK...
judge  the pair-set comparison is BLIND to this and must be. The buoy-node test added at
       8df625a is the SINGLE detection, and this is the measurement that says what that
       test is load-bearing for rather than that it happens to redden.
cell   the four platform arm LABELS reversed against their tips -- tip coordinate set
       bit-identical, only the assignment moved
out    53 passed
judge  C56(iv) in its sharpest form. No coordinate changes at all, so NO set-valued
       comparison can see it, and the buoy-node test is parametrised over `range(1, BODIES)`
       and never looks at the platform. The implementer is right to carry this by name.
```

Per DE2 this batch is the platform model and the gate that proves it, not apparatus. **No
apparatus corpus was written or grown**, and `tests/corpus/report_guard_states.txt` was not
edited even where C57 leaves one row unreproducible.

```
cmd  python -m pytest <every file under tests/ whose text mentions a corpus> -q
out  829 passed
cmd  python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
       tests/test_collected_set_golden.py tests/test_tree_prose_consistent.py
       tests/test_report_guard_states.py -q      (at my verdict commit, with the corpus in)
out  313 passed in 231.40s
judge adding the file reddens nothing, and the three harness anchors are green with the
      verdict and the corpus both committed.
```

## On the criterion, said once

**I do not disagree with CZ0 and I am closing on the third round as instructed.** Nothing I
found is (a), (b), (c) or (d), so PASS is the honest verdict rather than a softened one.

**The disagreement I flagged in verdict 75 about DR1's repair rule is answered by events and
I withdraw it.** I said the delete-not-repair reading would have forced deleting a working
control. Both items were closed without touching a guard's assertion at all -- one report
sentence and two `-c` flags -- so the rule never bit, and my worry was about a case that did
not arise. It does not need to go to Xabier.

**What I do want on the record for the plan, once, is R605's boundary rather than R605.**
CJ0 says in-tree code is trusted under review and resistance to forgery by in-tree code is
out of scope. R605 is the same question in the MODEL rather than in the harness: a provenance
assertion that re-reads through the code under test is trusted for the same reason, and the
plan does not say so where the ladder can see it. One sentence in `docs/milestones/F3.md`
would make the next reviewer's job a reading rather than a rediscovery. **That is a plan
note, not a round, and not a condition on this PASS.**

## Closure items

**Fixed once, in this step's closure commit, and not re-reviewed item by item.**

C12, C14, C18 to C32, the open part of C33 to C39 and C42, C43 to C47, and C52, C56(ii),
C56(iii), C57 carry forward, plus **C58 = R604, C59 = R605, C60 = R606, C61 = R607,
C62 = R608, C63 = R609**, and **C64 = R610 which is a ledger line and no work.**

**CLOSED THIS ROUND, verified rather than accepted.**

* **C50 -- closed, and my numbers were the right ones.** Both disputed cells measure
  `9 failed, 44 passed` in my own worktree, the same two test functions, and the mutation
  the report describes -- applied in `_member_geometry`, before the node is built and before
  `length = math.dist(start, end)` -- **is the mutation I ran.** `9 = 5 + 4` is those two
  functions, as the report says.
* **C51, C53, C54 -- repaired at `127c7b1`.** C51's status half is met (R609 is the
  residual); C53's stub heading is gone; C54's line naming run `36756429195` at `b2e59b0` is
  present.
* **C55 -- closed by the correction above.** Grid and baseline offset reproduce exactly. The
  third number was never a gate property and the report is right that it is not; my figure
  is withdrawn and the boundary distances are published here so nobody re-takes them.
* **C56(i) -- BUILT, and it does what it was asked to do.** With the provenance broken and a
  tip 3 m out, both DZ2 tests go green and C56 is the only red left (`1 failed, 52 passed` in
  my cell; the report says `2 failed` for a differently-constructed break -- a count
  difference in a closure cell, not a claim difference). Its two clauses both carry weight:
  keys rotated gives `10 failed`, owners rotated `9 failed`. Its limit is R605 and it is a
  new item rather than C56(i) reopened.
* **C40 -- reasoning accepted, and the family is five files not four (R606).**
* **The golden.** `tests/goldens/collected_tests.txt` 418 -> 420 is correct and additive, and
  the golden catches deletions only by design (`test_every_recorded_test_is_still_collected`),
  so its being one test stale at `b2e59b0` was not a missed red.

## Process checks (4b, 4c, and the commit classes)

```
cmd  git diff 2f068c4..1b3fb73 -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 2f068c4..1b3fb73 -- tests/conftest.py 'tests/**/conftest.py'
out  (no output)
cmd  the five commits, by path class
out  1d623c1 tests/ only | eb8e165 docs/ only | 086a2c7 tests/ only
out  127c7b1 scripts/ + docs/ | 1b3fb73 docs/ only
judge my own instructions untouched, the pathspec returns the file that exists rather than
      the empty set, no new conftest and no plugin added to any rung run, and NO COMMIT
      touches both `floatfea/` and `docs/reviews/` -- none touches either. `floatfea/` is
      untouched for the whole round.
```

## Next step opens when

**It opens now. F3 step 1 is CLOSED at PASS and step 2 may begin.**

1. **Nothing carries by name.** R602 and R603 are answered and closed; no blocking item
   remains, so step 2's `Carried` section says "checked, nothing carried" unless the closure
   commit finds something.
2. **The closure list above goes into the closure artifact as ONE commit**, not re-reviewed
   item by item. C58 (R604) and C63 (R609) are one-line edits; C59 (R605) is the one worth
   real thought and it may legitimately be answered by a sentence in the plan rather than by
   a test.
3. **Step 2's first report states whether 13 October still holds**, per DZ7c and `CLAUDE.md`
   -- and since this step closes carrying NO blocking item, DZ7c's reduce-scope branch is not
   triggered and the dates stand as written.

**Schedule.** F3 closes 13 October; F4 19 October; the member-force table 23 October; the
code-check screen 28 October. The report's hand-written paragraph states the date and states
that it holds, and I have no measurement that contradicts it: the whole tree is green on two
machines, the ladder is green on the one neither of us controls, and rung 3 -- the rung this
step is about -- is `218 collected, 0 failed`.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: f204977e06b029e2035b2b6ce333bfe28d390603
Verdict: HOLD
Tests: 2815 passed, 1 failed, 0 skipped   (my own run at `b2e59b0`, `python -m pytest -q`, 1351.45s, one invocation, no split)

## Round of 2026-09-30 -- SEVENTY-FIFTH verdict, round 2 of 3 on F3 step 1

**Reviewed commit: `b2e59b0`.**

**R600 IS ANSWERED AND IT IS ANSWERED PROPERLY.** I ran sixteen one-variable mutations of
my own against the new gate, baseline `52 passed`, and eleven of them redden it -- including
the frame rotation and the x/y transposition the hand-back said produced no clean result, and
including one detection the design gained that nobody claimed. The expected side really does
come from the deck now, and the two cells that were vacuous before are not.

**AND THE ONE RULING THE HAND-BACK ASKED FOR IS THE ONE I HAVE TO REFUSE.** The remaining
red is NOT "a state requiring a detection DR0 retired". The sha-exists check exists, at
`tests/test_report_carried.py:320`, and it works -- I proved it by ablation. What is broken
is the harness's planting anchor, and what broke it is a sentence this commit added to the
report. Deleting the state, or withdrawing the corpus row, would remove a working control
on a false premise. That is R602 and it blocks.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit b2e59b05e74174b8935ad8adc8991ea59cc13c32 --json name,conclusion,databaseId,event
out  [{"conclusion":"failure","databaseId":36756429195,"event":"push","name":"CI"}]
cmd  gh run view 36756429195 --json headSha,status,conclusion,event,jobs
out  headSha b2e59b05e74174b8935ad8adc8991ea59cc13c32; status completed; conclusion FAILURE
out  the verification ladder            SUCCESS   (18:08:26 -> 18:11:30)
out  lint, unit and guards              FAILURE   (18:08:27 -> 18:16:52)
out  CI determinism -- leg              SKIPPED
out  CI determinism -- ten legs agree   SKIPPED
cmd  gh run view 36756429195 --log-failed
out  3 failed, 905 passed, 1 warning in 449.12s
out  FAILED ...[answers_header_names_a_sha_that_is_not_a_commit] -- this state is a defect
     and must fail
out  FAILED ...[answers_header_names_an_older_verdict_commit] -- CalledProcessError: git
     commit ... returned non-zero exit status 128
out  FAILED ...[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_..._REDDENS_CONTROL] -- same
cmd  python -m pytest -q   (mine, at b2e59b0, one invocation, clean worktree)
out  1 failed, 2815 passed, 2 warnings in 1351.45s
judge RED, and I am not softening it. Not `unavailable` and not `allowance exhausted`:
      every job that was scheduled started and one of them failed.
judge AND THE DISAGREEMENT BETWEEN THE TWO RUNS IS THE FINDING, NOT NOISE. CI has three,
      I have one, and the two extra are exactly the two `_seed_older_verdict` states. That
      is CA2's own species measured on this commit -- a claim that holds only where it was
      written. See R603.
```

**`gh run list --commit b2e59b0` with the ABBREVIATED sha returns `[]`, and the full sha
returns the run.** Recorded because it is how a reviewer comes to report as unavailable a
run that is merely red.

**The ladder is green on a machine neither of us controls, and rung 3 is the rung this step
is about.** That is the most important line in this block and it is why this is HOLD and not
STOP.

## Carried

Verdict 74 carried two blocking items, R600 and R601, and closure items C12, C14, C18 to
C32, the open part of C33 to C39 and C42, and C43 to C49. **The report's header reads
`Answers: verdict 74 @ 8ac9ce8`, which is my own verdict commit and the latest verdict
(instruction 1b and DX2: satisfied, one comparison, and it is the right one).**

**I re-measured both rather than reading the report.** Every cell below is mine, run in a
`git worktree` at `b2e59b0` outside this repository, restored between mutations.

* **R600 -- ANSWERED. Closed, site by site, and the closing cell goes red.**

```
rule   condition 1: `expected_pairs` reads the DECK's joint points
cmd    read tests/verification/rung3/test_platform_skeleton.py:350-365
out    deck = superstructure.deck_joint_points
out    platform: centre = (0.0, 0.0, superstructure.joint_plane_z);
       tips = [deck[n] for n in sorted(deck) if n.startswith("hub")]
out    hubs:     centre = deck[body.name];
       tips = [deck[n] for n in sorted(deck) if owner[n] == body.name]
cmd    read floatfea/model/platform.py:647-650 and 343-358
out    both maps are comprehensions over `joints`, which is `_full_scale_deck`'s output.
       Neither `_member_geometry` nor `_build_body` can reach them.
judge  the argument is used, the quantity compared has changed, and the docstring's claim --
       "neither of which any part of the model construction can influence" -- is exactly as
       strong as what I could measure. It is narrower than "from the deck" and it is TRUE;
       I tried to break it and could only do so from the READER (C56(ii)).

rule   condition 2: "every member tip +3 m, applied before `math.dist`" must go RED
cmd    the platform arms' end point +3 m in x in `_member_geometry`   (baseline 52 passed)
out    1 failed -- test_DZ2_the_bodys_MEMBER_GEOMETRY_is_what_the_deck_implies
cmd    the twelve cluster arms' end points +3 m in x, same place
out    8 failed -- 4x DZ2 pair set, 4x the new buoy-node test
cmd    both together
out    9 failed -- 5x DZ2 pair set, 4x buoy-node test
cmd    the same +3 m inside `_build_body` with `length` recomputed from the moved end
out    9 failed -- the same nine. The consistent form and the inconsistent form now redden
       the SAME test, which is what verdict 74 asked for.
judge  the condition is met. Cell (ii) is withdrawn in the report and re-stated as what it
       measured, in the implementer's own words.

rule   condition 3: `platform.py:551-553`'s DJ1 claim is backed by an assertion or deleted
cmd    git diff 8ac9ce8..b2e59b0 -- floatfea/model/platform.py | grep -c "^-[^-]"
out    0  -- nothing was removed; the docstring (now at :578-579) is untouched
judge  ACCEPTED AS BACKED. CW0 gives three permitted forms and "a test" is one of them.
       "Every coordinate comes from the deck's own joint points. Nothing is typed, and no
       nominal radius is used" is now asserted by DZ2 over all sixteen tips and the four hub
       centres -- and my `x1.02` cell, which is precisely the typed-nominal-radius case,
       reddens 9. **The one clause still unbacked is the platform's own CENTRE**, which IS
       typed as `(0, 0, joint_plane_z)`: C56(iii). Closure item, because the gate does not
       claim otherwise and its docstring names the exception explicitly.

rule   and the docstring at :327-333 and the message stop saying "deck" until they mean it
cmd    read :341-352 and the assertion message at :398-401
out    the docstring now describes what R600 found, names the five measured cells, and says
       which point is not from the deck. The message reads "do not join the points the deck's
       joints imply" and that sentence is now true of the comparison.
judge  met.
```

* **R601 -- BOTH NAMED CAUSES ANSWERED AND VERIFIED. Its closing CONDITION is not met, and
  the residue is two DIFFERENT causes, R602 and R603. Not double-counted.**

```
rule   cause (a): `_PLAN` hardcoded to a closed milestone, failing false the moment the
       marker moved
cmd    read tests/test_report_guard_states.py:44-90 and 123-146
out    `_active_plan()` globs `docs/milestones/F*.md` for the marker; `MILESTONE = _PLAN.stem`;
       `_verdict_step()`, `REVIEW_PATH`, `reports`, `reviews` and both `git add` paths all
       derive from it. Six sites, one name.
cmd    the fallback when the glob finds zero or two plans
out    `carrying[0] if len(carrying) == 1 else milestones / "F2.md"`, with `try/except OSError`
       and the reason at the site (a raise at import is R234)
judge  and the fallback is BACKED rather than silent: `tests/test_report_carried.py:471-484`
       asserts exactly one plan carries the marker and its message says what two would do.
       I looked for that assertion before accepting the fallback.
cmd    the state count at the two commits, mine
out    228bdfb  24 states dying in the harness before planting anything
out    b2e59b0  1 failed, 23 passed locally
judge  ANSWERED. The second half -- thirteen states coming back CLEAN because the harness
       planted into F2 while the guard read F3 -- is real, and `assert code != 0` is what
       caught it. That is the assertion R599's deletion left behind, doing the job it was
       kept for, which is worth recording because I ruled on that deletion last round.

rule   cause (b): the milestone-boundary interval, 13 reds in tests/test_report_carried.py
cmd    python -m pytest tests/test_report_carried.py -q  (inside my whole-suite run)
out    0 failed. None of the thirteen remains, and the 47-red excluded set at `8df625a` is
       gone: one invocation over the whole tree is `1 failed, 2815 passed`.
judge  ANSWERED. Revision 2 closed it exactly as the implementer predicted it would.

rule   R601's own closing condition: `0 failed` locally AND on a run at the judged commit
out    NOT MET. 1 failed locally, 3 failed on CI.
judge  the two causes R601 NAMED are closed. The condition is not, for two causes that did
       not exist when it was written. They are R602 and R603 and they block on their own
       merits rather than as R601 carried -- carrying R601 forward would attribute reds to a
       hardcoded path that is now fixed.
```

## Findings

**R602. (d, blocking) `answers_header_names_a_sha_that_is_not_a_commit` is red, and the
stated diagnosis is refuted: the sha-exists check EXISTS and WORKS. What is broken is the
harness's planting anchor, and what broke it is a line of prose this commit added to the
report. `tests/test_report_guard_states.py:392-399` against `docs/reports/F3/step-1.md:589`.**

The mechanism first, because it decides the finding and it is four lines.

```
rule   tests/test_report_guard_states.py:392-399 -- `bad_answers_sha` locates the header with
       `text.rindex("Answers: verdict")` and overwrites to end of line
cmd    grep -n "Answers: verdict" docs/reports/F3/step-1.md
out    3:Answers: verdict 73 @ 52de940
out    256:Answers: verdict 74 @ 8ac9ce8          <- the real header, revision 2's
out    589:out    the newest revision of the report has no `Answers: verdict N @ <sha>` line
cmd    the same string surgery, replayed
out    rindex lands on LINE 589. Replaced segment: 'Answers: verdict N @ <sha>` line'
out    planted line: 'out    the newest revision of the report has no `Answers: verdict 28 @ deadbee'
out    remaining count of "Answers: verdict 74 @ 8ac9ce8": 1
judge  the state mangles a sentence inside revision 2's `out` block and leaves the real header
       intact. `ANSWERED` resolves to `8ac9ce8`, `git cat-file -e` succeeds, and the nested run
       is `141 passed` -- CORRECTLY, because no defect was planted.
```

**THE ABLATION. One variable, in a worktree at `b2e59b0`.**

```
cell   the literal `Answers: verdict N @ <sha>` at docs/reports/F3/step-1.md:589 replaced by
       `A-n-s-w-e-r-s line`. Nothing else touched -- not the harness, not the guard.
out    1 passed
cell   restored
out    1 failed
judge  the red is caused by the report's own prose, in the commit that reports the state as
       unfixable. The line quotes `scripts/ci_section.py`'s error message, and that message
       contains the literal the harness anchors on.
```

**AND THE DETECTION IS NOT RETIRED.** This is the half of the hand-back I have to refuse.

```
cmd    read tests/test_report_carried.py:309-326
out    test_the_report_names_the_verdict_it_answers:
out        out = subprocess.run(["git", "cat-file", "-e", ANSWERED], cwd=ROOT, ...)
out        assert out.returncode == 0, "the report answers verdict `{ANSWERED}`, which
           `git cat-file -e` cannot resolve ..."
cmd    git cat-file -e deadbee; echo $?
out    fatal: Not a valid object name deadbee
out    128
judge  the check is there, it is IN the very test the corpus row names as `require=named_fail`,
       and the ablation above shows it firing. The retirement note at
       `tests/test_report_carried.py:2259-2260` is about a DIFFERENT quantity -- the WHOLE-SUITE
       LINE's sha, in the deleted distance-and-pathspec test -- not the `Answers:` header's.
       Two sha-exists checks, one retired and one live, and the diagnosis crossed them.
judge  so "leave it or delete it, and the corpus entry is yours" is not the choice on offer.
       Deleting the state would delete a control that works, and my corpus row's
       `measured=named_fail_1_failed_121_passed` is still correct ABOUT THE GUARD. I am not
       withdrawing it.
```

**Why this is (d) and not a closure item.** It is a red test at the reviewed commit, on CI and
in my own run. It is also the only one of the three reds that a reader of revision 2 would have
taken for a settled loss.

**Closed when** the report's newest revision no longer carries the anchor literal in a position
preceding the real header -- the cheapest form is to break the quoted string in that `out` row,
which is a REPORT edit and touches no apparatus at all, and I have measured that it works -- and
`python -m pytest tests/test_report_guard_states.py -q` reports this state passing. If the state
is deleted instead, the reason recorded at the site must say that the guard's check is LIVE and
that the harness's anchor was what failed; `b2e59b0`'s commit message currently records the
opposite, and a wrong reason in the tree outlives the red.

**R603. (d, blocking) `_seed_older_verdict` runs `git commit` with no author identity while
the other two commit sites in the same file pass one, so two states are red on CI and green
here. `tests/test_report_guard_states.py:332-336`.**

```
cmd    read tests/test_report_guard_states.py:329-336
out    subprocess.run(["git", "-C", str(work), "add", REVIEW_PATH], check=True)
out    subprocess.run(["git", "-C", str(work), "commit", "-q", "--no-verify", "-m", message],
                      check=True)
cmd    read the two other commit sites in `_build`
out    both carry ["-c", "user.name=harness", "-c", "user.email=...", "commit", ...]
judge  one of three sites lacks the identity. That is the whole defect.
cell   git init in an empty directory, add a file, commit with
       GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null GIT_CONFIG_NOSYSTEM=1
out    fatal: unable to auto-detect email address ...; exit=128
judge  exit 128 on `git commit` is a missing identity, as the hand-back says.
cmd    git config --local --get user.email; git config --global --get user.email
out    xlamaeso@outlook.com
out    (empty)
cmd    grep the user section out of .git/config
out    [user] name = gating-supervisor, email = xlamaeso@outlook.com
judge  AND THIS IS WHY IT IS GREEN HERE. `_build` copies `.git` into the scratch repo, so the
       harness inherits the identity from THIS repository's own local config.
       `actions/checkout` writes no user section, so CI's copy has none. The two states have
       never passed on a machine that did not happen to carry an identity in the repository --
       and before R601a they never ran on CI at all, so nothing said so. The hand-back's
       reading is correct and I am recording it with the measurement, because this is exactly
       the species CA2 exists for.
```

**Closed when** `python -m pytest -q` and a run at the judged commit both report `0 failed` for
these two names. Two moves are available and I am not choosing: add the two `-c` flags so the
third commit site matches the two that already have them -- which changes nothing about what
any guard checks -- or delete the two states with the reason at the site. Say which and why.

**On the third red, which is not a third finding.** The two `CalledProcessError` states are one
defect at one line: the CONTROL twin
(`guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_..._REDDENS_CONTROL`) is the same build
under another name, by design and by its own comment. Three reds, two causes, and neither is a
retired requirement. That is the direct answer to the question the hand-back asked.

## The rulings the hand-back asked for

**1. The label-permutation reasoning. IT IS RIGHT, AND I CHECKED THE ALTERNATIVE RATHER THAN
THE ARGUMENT.**

```
cmd    grep -rn "member.label" floatfea/ --include=*.py
out    platform.py:179  a tuple of `m.label` for every preliminary member
out    platform.py:639  `buoy = member.label.split(":")[1].removesuffix("_arm")`
judge  `buoy_joint_nodes` is built FROM the member labels, at :639. Selecting the expected tips
       through it would put the label on both sides of the comparison -- R600's shape one level
       down. `deck_joint_owner` comes from the deck's `body_b`, which the builder never writes.
       The reasoning is correct and the choice is the right one.
cell   ONE VARIABLE: inside each hub, every cluster-arm label rotated onto the NEXT buoy's
       joint. Pair set and count unchanged.
out    4 failed, 48 passed -- all four test_DZ2_each_BUOY_lands_on_the_node_the_DECK_puts_it_at
cell   ONE VARIABLE: each hub takes the NEXT hub's three buoy joints -- labels right,
       coordinates from another tripod
out    12 failed -- 4x buoy-node test, 4x DZ2 pair set, 4x the f ladder
judge  both halves of the new assertion carry weight: the coordinate clause catches the
       within-hub rotation, the owner clause is there for the cross-hub case. This is the test
       I was asked to check hardest and it holds.
cell   can it go VACUOUS? It iterates the map and skips every entry whose owner is not this
       body, so an empty or short map would read green.
out    `test_the_BUOY_NODE_MAP_names_its_body` asserts `len(mapping) == 12` in the same file.
       The domain cannot empty silently. Assertion domain blindness checked and clear.
```

**2. The mechanical check for "the expected side is built out of whatever is nearest". THERE IS
ONE, IT IS PROVENANCE RATHER THAN DETECTION, AND I MEASURED THAT THE SHAPE IS STILL REACHABLE.**

```
cell   ONE VARIABLE: `deck_joint_points` overwritten in the `Superstructure` constructor with
       the coordinates of the BUILT nodes. R600's exact shape at a new site.
out    52 passed
judge  nothing in the tree ties that map to the file it claims to come from. The check that
       would: `expected_pairs` re-reads the deck through `_full_scale_deck(DECK_YAML, lam)` and
       asserts `superstructure.deck_joint_points` equals it. That is ONE rung-3 assertion about
       the model -- the ladder, not a guard, not a scanner, not a report generator -- so DR1's
       freeze does not reach it, and it turns the three-round pattern from a matter of attention
       into a matter of provenance, which is the form my own instructions ask for
       ("Provenance, not existence").
judge  I am NOT blocking on it, because the tree as it stands carries no such defect and CZ0(a)
       is about defects rather than about reach. It is C56(i), and it is the one closure item I
       would spend the commit on first.
```

**3. DZ7a. THE CITATION DOES NOT RESOLVE, AND ON THE SUBSTANCE THE ORDERING WAS RIGHT.**

```
cmd    grep -rn "DZ7a" --include=*.md --include=*.py .
out    (no output -- nowhere in the repository, including docs/reports and the locked plan)
cmd    grep -rn "DY8b" --include=*.md docs/milestones docs/reviews CLAUDE.md
out    docs/reviews/F2/step-7.md:22 only
cmd    grep -n "DZ7" docs/milestones/F3.md
out    206:### DZ7c. If F3 step 1 closes carrying: REDUCE SCOPE, DO NOT SLIP
judge  there is no DZ7a to have violated. The one-path-class discipline exists as DY8b and it
       appears once, in an F2 verdict -- not in `docs/milestones/F3.md` and not in `CLAUDE.md`.
       `b2e59b0`'s message cites a rule by a label that resolves nowhere, which is the "every
       citation resolves" guard in its cheapest form. Closure item C52.
judge  AND ON THE SUBSTANCE: the ordering was right and I would not have split it. The report is
       produced by `scripts/ci_section.py`, the generator was broken, and it was only found
       broken by trying to build the report. Committing the report first would have committed a
       file the generator refused to produce; committing the generator first would have been a
       commit whose only justification was a report that did not exist yet. What the discipline
       is FOR -- a reviewer able to read one class of change at a time -- was not damaged:
       `floatfea/` is in its own commit (`1c0785e`), the gate is in its own commit (`8df625a`),
       and the three-class commit contains no `floatfea/` change at all. That is the line that
       matters and it was held.
```

**4. C43 and the suite line at `8df625a`.** Confirmed, unchanged, still a closure item. My own
figure supersedes it for this round: `1 failed, 2815 passed, 0 skipped` at `b2e59b0`, one
invocation, no split, no exclusion. Section 6's own closing paragraph is what stops this being a
hidden red rather than a stale figure, and that is why it is not a finding.

**5. The slack-against-`f` table and `admissible`.** Verified in round 1 and re-confirmed by the
implementer to the digit. I am not asking for a model change, and DY0d's PSD-versus-
realisability gap stays where verdict 74 put it: recorded, for Xabier. Nothing new this round.

## The counter DZ2 now has, which it did not have last round

Verdict 74 ruled the rounding grid untestable because both sides read the same float. It is
testable now, so I inverted the rule and solved for the boundary rather than sampling one side.

```
cmd    the worst max abs(built - deck) over all sixteen member tips and the four hub centres
out    0.0 m, EXACTLY. Both sides trace to the same float, so the pair check is bit-exact in
       practice. **This is the number verdict 74's ruling 3 asked to be published beside the
       grid, and revision 2 does not carry it.**
cmd    extents and grids
out    platform  extent 51.056247 m   grid 5.1056e-12 m
out    hub1..4   extent 25.000000 m   grid 2.5000e-12 m
cmd    the smallest positive displacement that moves a tip into a different grid cell, solved
       by walking ULPs from the deck's own coordinate
out    platform:hub1_arm  x = 50.0                 +7.1054e-13 m   (100 ULPs)
out    hub1:buoy1_arm     x = 75.0                 +1.2648e-12 m   ( 89 ULPs)
out    hub1:buoy2_arm     x = 37.50000000000001    +1.2506e-12 m   (176 ULPs)
rule   set(pairs) == expected_pairs(...), both sides rounded to
       MASS_PROPERTY_AGREEMENT * body_extent
judge  the grid IS a threshold now: baseline offset exactly zero, detection at sub-picometre,
       which is 1.4e-14 relative on a 51 m frame -- two orders above one ULP of the coordinate
       and twelve orders below any displacement that means anything physically. The size is
       right and I am not asking for it to change.
cell   ONE VARIABLE: the grid multiplied by 1e12, so the cells are 5.1 m wide
out    52 passed
judge  and its SIZE is unasserted -- it can be inflated twelve orders with nothing saying so.
       Not blocking: the value is correct and now measured. C55, with the numbers supplied so
       nobody has to re-take them.
```

## Closure items

Named, with the file and what would close each. **Fixed once, in this step's closure commit, and
not re-reviewed item by item.** C12, C14, C18 to C32 and the unclosed part of C33 to C49 carry
forward except where noted.

**CLOSED THIS ROUND, verified rather than accepted:** C48 -- `expected_pairs` uses its
`superstructure` argument, `deck = superstructure.deck_joint_points` at :352, and both branches
read it. C49 -- the four `f`-ladder rows are in revision 2 section 2. **C40 is answered for
three of its five files**: `test_report_guard_states.py` and `scripts/ci_section.py` are
re-pointed and `test_report_carried.py` never needed it. `tests/test_plan_matches_tolerances.py:34`
stays ledgered and I accept the reasoning -- it reads F2.md for a table that really is there --
with the F3 tolerance sitting in a closed milestone's table as the visible cost.

**C50. Two of the four published cell counts in section 1 do not reproduce from their own
descriptions.** `docs/reports/F3/step-1.md:421-427`. "every tip +3 m, the node moved WITH the
length -> 5 failed" measures `9 failed` under both edit sites I could construct -- 5x DZ2 plus 4x
the new buoy-node test -- so `5 failed` is one test function's parametrisations rather than the
run. "every in-plane coordinate x1.02, a typed radius -> 1 failed" measures `9 failed`
whole-frame, or `25 failed` if `member.length` follows the scale; `1 failed` is reproducible only
if the edit was the platform's four arms alone, which is not "every in-plane coordinate". The
other two rows -- the plan centre and the label permutation -- reproduce EXACTLY, `1 failed` and
`4 failed`, including which test. Both discrepancies UNDERSTATE the detection, which is the safe
direction, and R600 is answered on my own cells regardless. Closed by re-measuring the two rows
or by restating what was mutated.

**C51. The generated Carried table states three CLOSED findings as open, with subjects that are
fragments of the sentence saying they are closed.** `docs/reports/F3/step-1.md:512-518`: R596,
R598 and R599 each read "open -- carried from an earlier verdict" with the subject "and R599 are
closed. Closure items C12, C14, C18 to C32, the open". Verdict 74 closed all three explicitly and
said so in its own `Carried for the next step` section. The generator is reading the mention
rather than the disposition. Over-reporting, so not blocking. Closed by the table reading the
disposition, or by it not claiming a status it cannot read.

**C52. `DZ7a` resolves nowhere.** Ruling 3 above. Closed by citing a label that resolves, or by
the rule being written into `docs/milestones/F3.md`.

**C53. Two consecutive `## 0.` headings**, `docs/reports/F3/step-1.md:260` and `:262`, the first
with no body.

**C54. Revision 2 reports CI for `228bdfb` and there is no line anywhere in it about `b2e59b0`'s
own run `36756429195`.** The generator anchors on the `Answers:` sha by design, so this is
structural rather than a slip, and it is the same machinery as C43 -- but the consequence is that
a reader of revision 2 cannot see that the tree they are handed is red. Closed by one line naming
the run at the report's own commit, which does not need the generator.

**C55. The DZ2 grid's size is unasserted, and the three numbers that pin it are in this verdict
and not in the report.** `tests/verification/rung3/test_platform_skeleton.py:352-356` and
`:387-391`. Closed by the report or by `MASS_PROPERTY_AGREEMENT`'s entry carrying the baseline
offset (`0.0 m`), the detection threshold (`+7.1054e-13 m`) and the grid (`5.1056e-12 m`). Goes
with C45, which already ledgers that this constant governs three decisions.

**C56. Four shapes DZ2 still cannot see, each one edit, each `52 passed`.** All four are reach
rather than defect, and the gate's docstring claims none of them.

  (i) `deck_joint_points` overwritten from the BUILT nodes -- R600's shape at a new site. Closed
  by the provenance re-read named in ruling 2. **This is the one to spend the commit on.**

  (ii) the deck READER scaling every joint point by 1.02 -- both sides move together. DZ2 tests
  the builder against the reader and cannot test the reader. Verdict 74's own closing condition
  accepted reading through `_full_scale_deck`, so this is recorded and not asked for.

  (iii) the deck's four hub joints all shifted +3 m in x, so the plan centre is no longer their
  centroid while the builder keeps the typed `(0, 0, joint_plane_z)`. The CoG gate cannot supply
  this because the remainder is placed to make the first moment match -- I checked that rather
  than assuming it. Closed by asserting the centre against a deck fact (the centroid of the four
  hub-platform joints, or the platform body's own reference point projected to the joint plane),
  or by the plan saying which fact pins the origin.

  (iv) the four platform arm LABELS reversed against their tips. The new buoy-node test is
  parametrised over `range(1, BODIES)` and never looks at the platform, and nothing ties a
  platform arm label to a deck hub joint. Nothing load-bearing reads those labels today -- the
  two `member.label` readers in `floatfea/` are the preliminary-member list and the buoy map,
  and the buoy map is built off the HUB bodies -- so the cost is a member-force row named for
  the wrong arm. **Carried to the step where that table ships**, whichever it turns out to be.

**C57. My own corpus row `tests/corpus/report_guard_states.txt:99` is still correct about the
guard and no longer reproducible through the harness.** Recorded here rather than edited, because
the apparatus corpora are frozen under DE2 and DR1. Not a work item, and it is not the row's
fault -- see R602.

## Tolerances touched

```
cmd  git diff 8ac9ce8..b2e59b0 -- floatfea/tolerances.py
out  (no output)
cmd  git diff 8ac9ce8..b2e59b0 --stat
out  docs/reports/F3/step-1-answers.json 23 +; docs/reports/F3/step-1.md 346 +;
     floatfea/model/platform.py 30 +; scripts/ci_section.py 45 +-;
     tests/test_report_guard_states.py 63 +-;
     tests/verification/rung3/test_platform_skeleton.py 75 +-
cmd  grep -n "MASS_PROPERTY_AGREEMENT: Final" floatfea/tolerances.py
out  1531:MASS_PROPERTY_AGREEMENT: Final[float] = 1e-13      -- unchanged
```

**None.** No value added, changed, removed or widened, and no comment in that file touched. Every
use of `MASS_PROPERTY_AGREEMENT` this step is a use that already existed. The one thing worth
saying is that its THIRD use -- the coordinate rounding grid -- has become a real threshold rather
than a no-op, and the measurement that pins it is in this verdict and is C55. That is a
strengthening of the entry's reach, not a change to its value, so it is not a tolerance touched.

## My own instructions (4b) and the conftest (4c)

```
cmd  git diff 8ac9ce8..b2e59b0 -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 8ac9ce8..b2e59b0 -- tests/conftest.py 'tests/**/conftest.py'
out  (no output)
```

Both untouched, and the pathspec returns the file that exists rather than the empty set.
No new conftest appeared anywhere under `tests/` and no plugin was added to any rung run.

**`tests/test_report_guard_states.py` DID change and it runs a nested pytest, so I read that
hunk line by line as instruction 4c requires.** Every change is a path derivation from one
`MILESTONE` name. No hook of any kind was added: no `pytest_runtest_makereport`, no
`pytest_ignore_collect`, no `pytest_collection_modifyitems`, no `pytest_runtest_call`, no
`force_result`, nowhere in the file. No assertion was weakened -- `assert code != 0` is what
caught the implementer's own incomplete fix, and the `collection_failed` and `everything_failed`
assertions are untouched. `scripts/ci_section.py` changed and it is a report generator that no
gate reads for a pass; the change is additive, and its new fallback is backed by an assertion in
another file that I located rather than assumed.

## The adversarial corpus (BE3)

`tests/corpus/platform_geometry_gate_r600.txt`, batch 23, committed separately at `f204977`.
**23 entries, all new this round.** Sixteen carry a mutation; five are solved boundaries or deck
facts and two are questions for the plan, and those seven are not counted either way.

**Of the sixteen mutations, the shipped suite caught 11 and MISSED 5.**

Against 9 of 17 in batch 22 on the same surface before R600, 9 of 16 in batch 21, and 23 of 31
in batch 20. **This is the first batch this milestone where the proportion moved for a reason I
can name**, and the reason is R600: batch 22's eight misses were one shape, the shape is gone,
and seven of those eight entries are caught here. A new file rather than rows added to batch 22,
because R600 changed the quantity compared and a row kept across a rule change is BP0 in corpus
form; batch 22 stays as the record of what the circular gate did.

The five misses are four shapes -- the reader, the expected side rebuilt at a new site, a label
with no deck anchor, and the threshold's own size -- and they are C56 and C55. None of them is
"the expected side is the built model", which is what batch 22 was entirely about.

Per DE2 this batch is the platform model and the gate that proves it, not apparatus. No apparatus
corpus was written or grown this round, and `tests/corpus/report_guard_states.txt` was not edited
even where R602 makes one of its rows unreproducible.

## On the criterion, said once

I do not disagree with CZ0 and I am not asking for a fourth round. Both findings are inside
(a)-(d) -- both are (d) -- and everything else is in the closure list, including two figures and
four sentences I have not held on.

**What I do disagree with is DR1's repair rule as it lands on R602 and R603, and this goes to
Xabier rather than becoming a round.** DR1 says a guard that fails false is DELETED, not
repaired. `docs/SUPERVISOR.md` says that; my own agent definition says "fixed or deleted". On this
commit the two readings give opposite answers, and the deletion reading is the worse one:

* R602's underlying check is LIVE and I proved it fires. Deleting the state deletes a working
  control in order to clear a red that a sentence in a report caused.
* R603 is one line missing two `-c` flags that the two adjacent commit sites already carry.
  Deleting two states -- one of which is the CONTROL for the other -- rather than supplying a
  git identity is not a proportionate trade.

Neither is "repairing a guard that fails false" in DR1's sense: neither changes what any guard
checks, on which quantity, at what threshold. If the rule is meant to cover the harness's
ENVIRONMENT and its ANCHORS as well as its assertions, then it is buying a reduction in
negative-control coverage at a price nobody has measured, and that is the decision I am flagging.
I will accept either move and I am not holding on the choice.

## Carried for the next step

**R602 and R603 carry BY NAME into round 3 of `docs/reports/F3/step-1.md` and stay BLOCKING.**
R600 is closed. R601's two named causes are closed and it does not carry. Closure items C12, C14,
C18 to C32, the open part of C33 to C39 and C42, C43 to C47, and C50 to C57 go into this step's
closure commit as one list; C48 and C49 are closed.

**ROUND 3 IS THE LAST.** Verdict 74 was round 1, this is round 2, and the next verdict closes the
step whatever it finds. If R602 or R603 is still open then, DZ7c applies and the hand-back has
already recorded the answer: **reduce scope, do not slip.** My reading on how that would land, so
it is on the record before it is needed: **R602 and R603 are BOTH ledgerable under DZ7c** -- they
are two lines in a meta-test harness and neither can change a member force -- and the item I
would NOT ledger is C56(i), because a gate whose expected side can be rebuilt from the thing
under test is the defect this step has now produced three times.

**Schedule.** F3 closes 13 October. The report's one hand-written paragraph states the date and
states that it holds, and I have no measurement that contradicts it. The ladder is green on CI at
this commit and rung 3 is the rung this step is about; what is red is two lines in a harness.

## Next step opens when

**It does not open. This step stays open and these are the conditions, in this order:**

1. **R603 first, because it is one line and because it is the whole reason my run and CI
   disagree.** Name the move -- the two `-c` flags at `tests/test_report_guard_states.py:333-336`,
   or deletion of the two states with the reason at the site -- and say which.
2. **R602, and its recorded reason must match what is measured.** The cheapest close is a REPORT
   edit breaking the anchor literal at `docs/reports/F3/step-1.md:589`, which touches no
   apparatus; I have measured that it takes the state from red to green with one variable moved.
   If the state is deleted instead, the site must record that the `Answers:` sha-exists check at
   `tests/test_report_carried.py:320` is LIVE and that the harness's `rindex` anchor was what
   failed -- because `b2e59b0`'s commit message currently records the opposite, and a wrong reason
   in the tree outlives the red.
3. **The closure list once, in one commit.**
4. Then the report's revision 3, with the generated sections and the `Answers:` header naming
   THIS verdict at its own commit.

`python -m pytest -q` at `0 failed`, and a run at the commit round 3 offers with `lint, unit and
guards` green, are what I will check first. **And I will check them in that order and then close
the step**, per the three-verdict cap.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F3 step 1
Reviewed commit: 008a8e98dd787e5ea4e1bca57dfbee8322655ce6
Verdict: HOLD
Tests: 2739 passed, 37 failed, 0 skipped   (my own run at `228bdfb`, `python -m pytest -q`, 1224.18s, one invocation, no split)

## Round of 2026-09-30 -- SEVENTY-FOURTH verdict, and the FIRST on F3 step 1

**Reviewed commit: `228bdfb`.**

**This is verdict 1 of 3 on this step.** The count restarted here, as verdict 73 said it
would.

**WHAT THE ROUND GOT RIGHT, AND IT IS MOST OF IT.** Eleven standalone commits, one path
class each. R596 is answered and answered well: the analytic path is real, it is
independent of the assembled matrix in the way it claims, and I broke it four different
ways to check. R598 is answered, its figure is re-measured rather than transcribed, and
the implementer was right to publish the number measured here instead of the one the
directive predicted -- I say so below because it asked. R599 is answered exactly as
ruled: deleted, not renamed. DZ5 is the best thing in the diff; its arithmetic
reproduces to the digit, including the hub figures nobody predicted. C34, C35, C38, C39,
C41 and C42 are closed and C42 is closed well enough that this verdict was written
through the repaired tool.

**AND THE ONE THING THAT IS NOT.** R597's repair has the same defect R596's repair had,
in the same shape: the new gate's reference is built from the thing it is checking. The
report says the endpoint-pair set is compared against the deck's joint coordinates. It
is compared against the built model. Every coordinate in the frame is compared only with
itself, and I have eight measured cells saying so.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 228bdfb --json name,conclusion,workflowName
out  []  -- the commit touches only docs/, which ci.yml path-ignores
cmd  gh run view 36743819045 (workflow_dispatch AT 228bdfb, dispatched by the implementer)
out  headSha 228bdfb76e7944fe5d59603d043dc41109331280; status completed; conclusion FAILURE
out  the verification ladder            SUCCESS   (rungs 1, 2, 3, 6, 4, 5 all green)
out  CI determinism -- ten legs agree   SUCCESS   (all ten legs green)
out  lint, unit and guards              FAILURE   -- 37 failed, 835 passed in 581.86s
out  actionlint, ruff, black, mypy and the unit step all SUCCESS; the failure is
     entirely in the `guards and meta-tests` step
cmd  python -m pytest -q   (mine, at 228bdfb, one invocation)
out  37 failed, 2739 passed, 2 warnings in 1224.18s
judge RED. My run and CI agree on the failure set EXACTLY -- the same 37 names, 17 in
      tests/test_report_carried.py and all 24 parametrisations of
      test_the_guard_survives_the_state. Not `unavailable` and not `allowance
      exhausted`: every job started, every job ran, and one of them failed.
```

**The ladder being green on a machine neither of us controls is the thing that matters
most here**, and it is green: rung 3 -- the rung this whole step is about -- passes on
CI at the judged commit. The red is in the report-carry apparatus, which is why R601
below separates its two causes rather than calling it one boundary artifact.

## Carried

Verdict 73 carried four blocking items -- R596, R597, R598 and R599 -- and closure items
C12, C14, C18 to C32 and C33 to C42. **The report's header reads `Answers: verdict 73 @
52de940`, which is my own verdict commit and the latest verdict** (instruction 1b and
DX2's third ruling: satisfied, one comparison, and it is the right one).

**I re-measured all four rather than reading the report.** Every cell below is mine, run
in a `git worktree` at `228bdfb` outside this repository, restored between mutations.

* **R596 -- ANSWERED for the inertia half. Closed, with one piece of reach recorded
  below as C46.**

```
rule   (A) analytic == assembled at MASS_PROPERTY_AGREEMENT * M_b * l_b^2, per body
cmd    beam.py `rho_ip_l = rho * (I_y + I_z) * ll` scaled by 2.0
out    10 failed -- (A) and (B) on all five bodies. Platform absolute residual
       4.960883e-09 -> 4.230312e+05 kg.m^2, which is 1.5225e-18 -> 1.2983e-04 relative.
       The report's own figures reproduce to five digits.
cmd    bending_mass called with 2.0 * rho * I in BOTH planes
out    10 failed
cmd    rho_a_l = 1.1 * rho * A * ll   (the translational block)
out    16 failed
judge  THE MUTATION THAT USED TO PASS 43 TESTS NOW REDDENS TEN. The old comparison was
       `deck == deck`; this one is a hand-computed rod-plus-section inertia against the
       assembled matrix, and the remainder is read off the lumped input rather than
       recomputed, so a defect in the element no longer cancels. This is the finding
       answered, not moved.
rule   the residuals are round-off and not cancellation, which is the OTHER half of R596
cmd    the raw residuals at 228bdfb, unmutated
out    platform (A) inertia 4.960883e-09 absolute on a 6.250000e+09 tensor
out    hub1-4   (A) inertia 5.96e-08 to 1.19e-07 absolute on 3.125000e+08
out    numpy.spacing(9.375e8) = 1.192093e-07
judge  these ARE round-off -- one ULP of the scale, where R596's `3.375e-36` was
       nineteen orders below one ULP. The signature is gone because the arithmetic
       changed, not because the print changed.
```

* **R597 -- NOT ANSWERED. Renumbered R600 and it blocks.** The new gate is real work and
  it catches two things it did not catch before (a duplicate line, and a chain instead
  of a star). It does not catch the cell R597 named, and it does not compare anything
  with the deck. See R600.

* **R598 -- ANSWERED at `1078698`. Closed, and I checked every number rather than the
  prose.**

```
cmd    git grep -n "MISPLACED_remainder"
out    (no output) -- the phantom is gone from the tree
cmd    the worst residual re-measured at 228bdfb over BOTH comparisons, five bodies,
       mass normalised by M_b, CoG by l_b, inertia by M_b l_b^2
out    platform  (A) mass 0.000e+00  CoG 3.648e-18  inertia 1.522e-18
out    hub1      (A) mass 0.000e+00  CoG 1.421e-16  inertia 6.358e-17
out    hub2      (A) mass 1.5522e-16 CoG 1.421e-16  inertia 1.272e-16
out    hub3/hub4 the same to within one ULP
out    WORST = 1.5522e-16, at hub2's MASS; 1e-13 / 1.5522e-16 = 644.1x
judge  the published `1.5522e-16` and `~644` are both correct at this commit. The
       claim that the old `2.2119e-15` came from dividing a CoG offset by 1.0 m
       instead of by l_b also holds: 2.2119e-15 / 1.9073e-16 is about 11.6, and
       11.6 is the ratio verdict 73 measured for the same figure.
```

  **AND ON THE DISAGREEMENT WITH THE DIRECTIVE'S FIGURE, WHICH THE INVOCATION ASKED ME
  TO RULE ON: publishing the figure measured here was RIGHT, and transcribing
  `1.9073e-16` would have been the defect.** BP0 is explicit -- when a decision rule
  changes, every figure citing the old rule is regenerated or withdrawn in the same
  commit. The rule changed twice over: the quantity moved from `assembled vs deck` to
  `analytic vs assembled and analytic vs deck`, and the normalisation moved from 1.0 m
  to `l_b`. `1.9073e-16` was measured against the pre-DZ1 gate and describes a
  comparison that no longer exists. Carrying it forward would have been exactly the
  species BP0 was written for, and the entry says which figure was measured where. Good.

* **R599 -- ANSWERED at `de6b1e0`. Closed as ruled, and I read the hunk line by line.**
  The `named` tuple and its assertion at `:713-743` are deleted, `assert code != 0` is
  kept, `_assert_diagnosis` is kept, neither state was deleted, `DIAGNOSIS` was not
  extended, and no name was added. The reason is recorded at the site naming R599 and
  DR1, including the R516 false-green direction. **Its closing condition also said
  `python -m pytest -q` reports `0 failed`, and that is not met -- for a reason that is
  not R599's and that R601 carries.**

## Findings

**R600. (c, blocking) DZ2's geometry gate builds its expected endpoint-pair set from the
BUILT MODEL, not from the deck, so the comparison is an identity. The whole frame can be
rotated, scaled, transposed, or have its member labels permuted onto each other's joint
points, and all 48 tests pass. R597 is not answered, and its named site is untouched.
`tests/verification/rung3/test_platform_skeleton.py:326-343`, `:374-377`, and
`floatfea/model/platform.py:551-553`.**

The mechanism first, because it is three lines and it decides the finding.

```
rule   tests/verification/rung3/test_platform_skeleton.py:327-333 -- "The undirected
       endpoint pairs this body must have, from the DECK's joints. Built from the deck's
       own joint coordinates and the body's centre node, so it is independent of what
       the builder actually made."
cmd    read :341-343
out    centre = body.model.nodes[body.centre_node].xyz
out    tips   = [body.model.nodes[m.node_b].xyz for m in body.members]
out    return {frozenset({cell(centre), cell(tip)}) for tip in tips}
judge  every one of those is the BUILT model. The function takes `superstructure` as its
       first argument and never reads it. So the assertion at :374 is
       {(node_a, node_b)} == {(centre, node_b)} over the same member list -- which is
       true iff every member's node_a is the centre, and that is asserted again three
       lines below at :381. The set comparison adds nothing the star check does not
       already do, and it adds no deck.
cmd    git grep -n "platform12_deck\|DECK_YAML\|_full_scale_deck" on the test module
out    one hit, at :29, inside the module docstring
judge  the module does not read the deck at all.
```

**EIGHT CELLS, ONE VARIABLE EACH, ALL AT `228bdfb`, baseline `48 passed`.**

```
cell   every member end point +3 m in x, in `_member_geometry` BEFORE `math.dist`, so
       lengths and first moments follow -- R597's own cell, made self-consistent
out    48 passed. Widened to tests/verification/rung3: 213 passed.
cell   the platform's plan centre moved from (0,0,z) to (3,0,z) -- four hub arms at
       53 m and 47 m instead of 50 m
out    48 passed
cell   every in-plane coordinate scaled by 1.02 -- what a typed nominal radius instead
       of the deck's joint point looks like, which is the case DJ1's "no coordinate is
       typed into this repository" exists for
out    48 passed
cell   the four platform arm labels reversed against their tips, so `platform:hub1_arm`
       ends at hub4's joint
out    48 passed
cell   inside each hub, every cluster-arm label rotated onto the NEXT buoy's joint, so
       `hub2:buoy4_arm` ends at buoy5's point
out    48 passed -- and `buoy_joint_nodes` is keyed off exactly those labels, so F4
       would apply each buoy's reaction at its neighbour's node
cell   the whole frame rotated 30 degrees about z
out    DZ2 GREEN on all five bodies. 4 failed, and all four are
       `test_the_chosen_FRACTION_is_asserted_not_inferred`, because the f ladder
       descended to 0.1 on the hubs. The only detector of a rotated frame reports it as
       a SIZING FINDING and its message says "update it with the reason."
cell   x and y transposed on every node
out    DZ2 GREEN. 4 failed, the same f-ladder test, at f = 0.
cell   CONTROL -- the last member of each body re-pointed onto the first member's line,
       count and labels preserved
out    5 failed, one per body, on the DUPLICATE-PAIR assertion
cell   CONTROL -- member i starts at member i-1's tip: a chain, not a star
out    5 failed
judge  the duplicate check and the star check are real and I am not asking for them
       back. What is absent is any comparison against the deck, and six of the eight
       cells above are exactly the defect DJ1's rule and `platform.py:551-553` claim
       cannot happen.
```

**AND THE REPORT'S OWN CELL (ii) DOES NOT MEASURE WHAT IT SAYS IT MEASURES.** This is
the part I would most want read, because the figure in it is correct.

```
rule   docs/reports/F3/step-1.md section 3, cell (ii): "a member TIP moved +3 m -> DZ2
       reddens ... out 20 failed, 28 passed"
cmd    the same edit, `b = node((end[0] + 3.0, end[1], end[2]), f"{label}_tip")`
out    20 failed, 28 passed -- the published count reproduces EXACTLY
out    the 20 are MASS x5, (A) x5, (B) x5 and MEMBER_ONLY_fraction x5.
       `test_DZ2_the_bodys_MEMBER_GEOMETRY_is_what_the_deck_implies` is NOT one of them.
judge  the edit sits AFTER `length = math.dist(start, end)`, so it leaves `member.length`
       saying 50 m while the coordinates say 53 m. What reddens is the mass gate reacting
       to a member whose length disagrees with its own end points -- a real detection, and
       a different one. Move the same 3 m one function earlier, where everything stays
       self-consistent, and the count is 48 passed. The number was right and the sentence
       attached to it was not, which is BG0 in its usual form.
```

**Why this is (c) and not a closure item.** CZ0's third head is *what a gate claims, on
which quantity, at what threshold*. DZ2 is a new gate assertion, introduced this step,
whose claimed quantity -- agreement with the deck's joint points -- is not the quantity
compared. And its threshold is `MASS_PROPERTY_AGREEMENT * l_b` used as a coordinate
ROUNDING GRID, which the invocation asked me to size: **the grid cannot reject round-off
and cannot admit a real displacement, because both sides of the comparison read the same
float and round identically. Its size is currently unobservable.** That is not a
criticism of the number chosen; it is that no number is being tested.

**Why this is not a STOP.** The builder is not wrong. The frame it produces is, as far
as I can measure, correct -- I read the deck's hub points and the built nodes side by
side and they agree. What is wrong is that nothing in the tree says so, and DJ1's rule
is the one the plan leans on hardest. That is repairable inside the step.

**Closed when ALL THREE, site by site per CLAUDE.md:**
1. `expected_pairs` reads the DECK's joint points -- `build_superstructure` already has
   `joints` in scope and the test module can call `_full_scale_deck` the same way the
   builder does; the unused `superstructure` argument is where it was meant to come from.
2. The cell "every member tip +3 m, applied before `math.dist`" reddens it, and the
   report publishes that cell in place of cell (ii). Cell (ii) is withdrawn or
   re-labelled as what it measures -- `member.length` against the coordinates -- per BP0.
3. `floatfea/model/platform.py:551-553` -- "Every coordinate comes from the deck's own
   joint points. Nothing is typed, and no nominal radius is used" -- is either backed by
   that assertion or deleted (CW0). Verdict 73 asked for this site and it was not
   touched. **And the docstring at `:327-333` and the message at `:375` stop saying
   "deck" until they mean it.**

**R601. (d, blocking) CI is RED at the reviewed commit -- `37 failed, 835 passed` in
`lint, unit and guards` -- and it has TWO causes, only one of which is the step
boundary. `tests/test_report_guard_states.py:42` is the other, and it FAILS FALSE.**

```
cmd  gh run view 36743819045 --log-failed, failure names grouped
out  24 of 37: every parametrisation of test_the_guard_survives_the_state
out  13 of 37: tests/test_report_carried.py
cmd  the same, locally at 228bdfb
out  the same 37 names
```

**Cause (a), and it is the one that is not the boundary.**

```
rule   tests/test_report_guard_states.py:42 -- `_PLAN = ROOT / "docs" / "milestones" /
       "F2.md"`, with `_STEP_LINE` requiring `<!-- step-under-execution: (\d+) -->`
cmd    the marker as this step leaves it in F2.md
out    <!-- step-under-execution: moved to F3 at step 1 (DY8c) -->
judge  no digits, so the regex misses, `_step()` returns 0, `REPORT_NAME` becomes
       `step-0.md`, and `_build` raises
       `FileNotFoundError: docs/reports/F2/step-0.md` before a single state is planted.
       All 24 parametrisations die in the harness, including `baseline`.
judge  THE HARNESS IS REPORTING THE STATE OF ITS OWN INPUTS, which is the exact thing
       its own assertion at :296 refuses to let the nested run do. This is a guard
       failing FALSE, and DR1's permitted repair is DELETION, or the one-file
       `process:` re-point that C40 already names as its return condition.
```

**AND MY OWN RULING ON C40 IS WITHDRAWN.** Verdict 73 wrote, of these three guards:
*"The guard does not fail false -- it passes, and what it checks ... is real."* That was
true when I wrote it and it was true of the wrong event: the guard passes while the
marker sits on F2 and fails false the moment the marker moves, which is the single event
C40 was ledgered for. I ruled "leave it" on a guard whose only failure mode was the
transition I knew was next. Recorded here rather than softened, because the pattern --
three guards hardcoded to a closed milestone -- is the thing I said should go to Xabier,
and this is the measurement that says why.

**Cause (b), which IS the boundary.** The 13 `test_report_carried.py` reds are
`docs/reviews/F3/` being empty: `REVIEWED = _steps(REVIEWS)` is the empty set, `VERDICT`
resolves to a file that does not exist, and the parse yields
`test_the_report_carries_the_finding[(no finding parsed from the verdict)]`. The
implementer states this on the report's face and the forced order is real -- the tool
refuses a step with no report, so the report must land first. **It is not fully cured by
this verdict either:** `_verdict_text_at("52de940")` finds no F3 verdict at that sha and
falls back to the working copy, so once this file exists the guard will compare the
report against *this* verdict, which the report predates. That is BU1's boundary
reopened by the milestone change, and it closes at revision 2.

**Closed when** `python -m pytest -q` and a `workflow_dispatch` run at the commit the
next verdict judges both report `0 failed`. Cause (b) closes by revision 2 of the report
with its generated sections. Cause (a) needs a decision, and the two DR1-compliant ones
are: delete the states the hardcoded `_PLAN` breaks, with the reason at the site; or one
standalone `process:` commit re-pointing `tests/test_report_guard_states.py:42` and
`tests/test_plan_matches_tolerances.py:34` at the plan carrying the marker, citing C40.
**I am not choosing between them -- that is a directive, not a review finding.** What I
am ruling is that "leave it" is no longer available, because it is red.

## The four rulings the invocation asked for

**1. Is the analytic path independent, or has the vacuity moved a second time? IT IS
INDEPENDENT, and the answer is stronger than the report claims.** Three element
mutations redden it (torsion x2, bending x2, axial x1.1) and so does a wrong equivalent
density. It is blind to exactly one class, and the class is named correctly in its own
docstring: anything the remainder absorbs. What the report does not say, and what I
measured, is that comparison (B) covers precisely that class -- see ruling 2.

There is one thing it is blind to that nobody has named:

```
cell   ONE VARIABLE: `rigid_properties`'s translation-rotation coupling block negated
       after the projection -- the sign of every CoG this function reports, inverted
out    48 passed
judge  R596's fourth mutation, and it still passes. The reason is domain blindness, not
       reach: the full-body CoG offset is IDENTICALLY ZERO on all five bodies, so there
       is nothing for a sign error to show against. R596's sentence -- "a comparison
       whose expected value is exactly zero has nothing for a sign error to show
       against" -- survives DZ1 unchanged for the CoG half. This is not a blocking
       finding, because (B) demonstrably reddens on a DISPLACED remainder (below) and
       the model contains no body with a nonzero offset to measure a sign on. It is
       C46, and the honest form of it is a sentence saying so at the site.
```

**2. Is asserting (B) honest, or a second circular assertion wearing a label? HONEST,
and I can prove it with a cell the report does not carry.**

```
cell   remainder_inertia += 1e7 * I, AFTER the deficit is computed
out    5 failed -- ALL FIVE ARE (B). (A) is GREEN on every body.
cell   remainder_point += [0, 0, 5], after the placement rule
out    6 failed -- five (B), plus the first-moment placement test. (A) GREEN.
cell   remainder_mass = 1.05 * (1 - f) * deck_mass
out    10 failed -- MASS x5 and (B) x5
judge  (A) and (B) are COMPLEMENTARY, not redundant. (A) sees the element, the section
       and the assembly and is blind to the remainder; (B) sees the remainder and is
       blind to nothing the construction closes. The report's own defence of (B) -- "the
       placement rule could be wrong and this is where that shows" -- is correct and
       understated. Assert it. The sentence to change is "largely closed by
       construction", which is true of the inertia identity and false of the three cells
       above.
```

**3. DZ2's grid. It cannot admit a real displacement or reject round-off, and the reason
is not its size.** Both sides of the comparison read the same `float` out of the same
`Node`, so `cell()` maps them to the same tuple for any grid whatever. Set the grid to
1e-30 m or to 1 m and the assertion still passes on every frame the builder can build.
The grid is only a threshold once there is a second, independently obtained coordinate
to compare with, and there is none. **So I am NOT asking for the grid to change: I am
saying it is untested, and it becomes testable the moment R600 is closed.** At that
point `1e-13 * 51.056 m = 5.1e-12 m` against coordinates that are exact decimals in the
deck and pass through one Froude scaling is a reasonable size, and the number to publish
beside it is the worst |built - deck| over the 16 members.

**4. DZ5's arithmetic. It reproduces exactly, including the hubs.**

```
cmd    eigenvalues of J_G and of J_r per body, triangle slack = w0 + w1 - w2
out    platform  deck [3.125e+09 3.125e+09 6.250e+09]  slack +0.0000e+00
out    platform  J_r  [2.7305e+09 2.7305e+09 5.7287e+09]  slack -2.6770e+08  min +2.73e+09
out    hub1..4   deck [1.5625e+08 1.5625e+08 3.1250e+08]  slack +0.0000e+00
out    hub1..4   J_r  [7.7364e+07 7.7364e+07 1.5574e+08]  slack -1.0153e+06  min +7.74e+07
out    k_z = sqrt(6.25e9 / 1.25e6) = 70.711 m; extent 51.056 m; arms 50 m
judge  every published figure holds, PSD holds on all five, and the hub figure the
       directive did not predict is -1.0153e+06 on each of the four, identical to five
       digits. The label and the assumptions block are the right response and I am not
       asking for a model change.
```

## The measurement DZ5 is missing, and it changes what the finding means (BG0)

DZ5 states the violation and attributes nothing. One loop over the ladder isolates it,
one variable moved and everything else held:

```
cell   the J_r triangle slack recomputed at every f in MASS_FRACTION_LADDER
out    platform  f=0.5 -2.6770e+08   f=0.4 -1.7858e+08   f=0.3 -1.1487e+08
out    platform  f=0.2 -6.7051e+07   f=0.1 -2.9819e+07   f=0.0 +0.0000e+00 EXACTLY
out    hub1      f=0.5 -1.0153e+06   f=0.4 -8.1222e+05   f=0.3 -6.0917e+05
out    hub1      f=0.2 -4.0611e+05   f=0.1 -2.0306e+05   f=0.0 +0.0000e+00 EXACTLY
out    `admissible(body)` is True at every f, for every body
judge  THE SPLIT DOES NOT CREATE THE VIOLATION, IT INHERITS IT. The deck's own J_G sits
       exactly ON the lamina boundary, so subtracting any planar member set drives the
       remainder off it, and the slack is linear in f with a single zero at f = 0 --
       where the members carry no mass at all. **No admissible f removes it.** That
       turns "the deck is physically inconsistent and Xabier decides on FloatSim" into a
       decision with two options rather than a sensitivity to explore, and it is worth
       the four lines it costs.
judge  AND DY0d's admissibility test is PSD, not realisability. It passes a remainder
       whose minimum eigenvalue is +2.7305e+09 and which is not the inertia tensor of
       any real mass distribution. That is representable in a mass matrix and the solve
       is well posed, so it is not a defect -- but the plan's word for it is
       "admissible", and a reader will take that to mean more than PSD.
```

This is a closure item, not a block: it does not change a member force and it does not
move a gate. It is written here because the four numbers are cheap and the conclusion
they support is the one Xabier needs.

## Closure items

Named, with the file and what would close each. **Fixed once, in this step's closure
commit, and not re-reviewed item by item.** C12, C14, C18 to C32 and the unclosed part
of C33 to C42 carry forward except where noted.

**CLOSED THIS ROUND, verified rather than accepted:** C34 and C35 (the dead
`_NEGLIGIBLE_FRACTION` and the docstring it orphaned -- both gone, and the builder-limit
string now attaches to `MAX_LENGTH_OVER_GYRATION`); C36 and C37 (corrected in the
report's section 8); C38 and C39 (`buoy_rows` selected by name with an `assert len ==
12`, and the weight read from the deck and `GRAVITY_MAGNITUDE`); C41 (the module
docstring and the plan row now state what G3.1a is FOR); C42 (the `latin-1` fallback at
`scripts/write_verdict.py:103` -- this verdict was written through it).

**C40 is REOPENED and it is now R601(a).** My ruling that it does not fail false is
withdrawn.

**C43. C33 recurs inside its own repair.** `docs/reports/F3/step-1.md` section 8 says
"the line in section 10 is taken at this report's own commit"; section 10 says `Whole
suite at 9cba81c`. The report's commit is `228bdfb`. The one change between the two is
the marker move, which is what turns `0 failed` into `37 failed` -- so the published
figure is not merely early, it is the opposite of the tree under review. Section 10's
last paragraph explains the mechanism honestly, which is why this is a closure item and
not a finding about a hidden red. Closed by publishing the figure at the report's own
commit, or by section 8 not claiming it was.

**C44. The assumptions block carries five hardcoded measurements that nothing
regenerates.** `floatfea/model/platform.py:645-654`: `0.0000e+00`, `-2.6770e+08`,
`-1.0153e+06`, `70.711 m`, `51.056 m`. All five verify at this commit -- I checked every
one. BI3's reasoning applies exactly: a string in `floatfea/` that carries measurements
is a report nothing regenerates, and this one is surfaced in the run log where a reader
will trust it most. Closed by computing the slack at build time, or by carrying one
number and a pointer to the step report.

**C45. `MASS_PROPERTY_AGREEMENT`'s comment describes one use and the constant now governs
three decisions.** A comparison floor (`tolerances.py:1531`, described); a PSD
admissibility threshold at `floatfea/model/platform.py:529`, where the margin is 22
orders and the ladder therefore never descends; and a coordinate rounding grid at
`tests/verification/rung3/test_platform_skeleton.py:336` and `:361`. The third goes with
R600. Closed by the entry naming all three, or by the third not being this constant.

**C46. The CoG comparison's expected value is identically zero on all five bodies, so it
carries no sign.** Measured above: the projection's coupling block negated, 48 passed.
Not blocking -- (B) reddens on a displaced remainder and no body in this model has a
nonzero offset -- but the site should say it, because the next reader will take a green
CoG assertion for a checked sign.

**C47. The analytic reference applies `section.I_y` to both across directions.**
`tests/verification/rung3/test_platform_skeleton.py:162-164`, while the element applies
`I_z` in one bending plane and `I_y` in the other. Identical on every circular tube and
wrong on the first section with `I_y != I_z` -- which would read as an element defect
rather than a reference defect. Two corpus entries measure how invisible this is today:
swapping the element's two bending second moments, and replacing the reference's
`I_y + I_z` with `section.J`, both give 48 passed, because `Section.__post_init__`
requires `J == I_y + I_z` for a circular shape. Closed by using `I_z` for the
corresponding plane, which is a two-token change and costs nothing today.

**C48. `expected_pairs(superstructure, body)` never reads `superstructure`.** Goes with
R600; named separately so the closure commit does not leave a dead argument behind if
R600 is answered another way.

**C49. DZ5 has no ablation.** The `f`-ladder cell above. Closed by the four rows going
into the report, or into the closure artifact.

## Tolerances touched

```
cmd  git diff 52de940..HEAD -- floatfea/tolerances.py
out  one entry's COMMENT rewritten; no value added, changed, removed or widened
cmd  grep -n "MASS_PROPERTY_AGREEMENT: Final" floatfea/tolerances.py
out  1531:MASS_PROPERTY_AGREEMENT: Final[float] = 1e-13      -- unchanged
```

| | |
|---|---|
| constant | `MASS_PROPERTY_AGREEMENT` |
| old | `1e-13` |
| new | `1e-13` -- **unchanged**, and the entry says so |
| form | EXACTNESS, unchanged and still correct: dimensionless, relative to the quantity compared in every use, one entry over kilograms, metres and kilogram-metres-squared. The DZ1c normalisation makes the form MORE honest than it was -- the CoG is now relative to `l_b` rather than to a bare metre, which is what R598 turned on. |
| counter | **the phantom is deleted and the entry states what it has instead.** The binding cell is the element's torsional rotary term scaled by 2, which I reproduced: `1.5225e-18 -> 1.2983e-04` relative, fourteen orders above the floor. Verdict 73's condition allowed "the counter sentence is deleted and the entry states that it has none and why"; this is that, with the measurement named. **Accepted.** For an exactness entry a registered `_COUNTER` is not required and `test_counters_are_injected`'s registry is hand-written, which the entry now says in its own words. |
| justification | `docs/milestones/F2.md`'s table row, plus the entry's own comment. `36 * eps = 7.993606e-15` and `1e-13 / (36 eps) = 12.51` both re-verified. The worst-measurement figure `1.5522e-16` and the `~644` headroom re-verified at this commit. |
| widened? | **No.** Nothing in this file was loosened this step, and nothing anywhere else acquired a tolerance-shaped literal -- `tests/test_no_tolerance_literals.py` and `tests/test_plan_matches_tolerances.py` are both green in my run. |

**A note on the one place a tolerance moved into a new KIND of use.** `expected_pairs`
uses `MASS_PROPERTY_AGREEMENT * l_b` as a coordinate rounding grid. That is a different
form from a comparison floor and the entry does not cover it. It is inside R600 and is
answered there.

## My own instructions (4b)

```
cmd  git diff 52de940..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 52de940..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out  (no output)
```

Untouched, both. No new conftest appeared anywhere under `tests/`, and no plugin was
added to the rung runs. `scripts/write_verdict.py` changed and it is my tool rather than
my instructions: I read the hunk line by line, it is additive, it removes no guard, and
the `latin-1` fallback is correct -- it cannot raise, and it rewrites UTF-8 so a mixed
file repairs itself. The commit that made it is standalone and `process:`-messaged.

## The adversarial corpus (BE3)

`tests/corpus/platform_geometry_gate.txt`, batch 22, committed separately at `008a8e9`.
**29 entries, all new this round.** Twenty-one carry a mutation. **Four of those are
numerically vacuous on this model** -- a circular tube has `I_y == I_z`, and
`Section.__post_init__` requires `J == I_y + I_z` for a circular shape, so two of the
substitutions `beam.py`'s own docstring warns about cannot be told apart here -- and
they are marked `expect=vacuous` rather than counted, because a vacuous mutation counted
as a catch is how a coverage number becomes a lie.

**Of the seventeen that are not vacuous, the shipped suite caught 9 and MISSED 8.**

Against 9 of 16 missed in batch 21 and 23 of 31 in batch 20. The proportion has not
improved, and the reason it has not is that the eight misses are one shape rather than
eight: every coordinate in the frame is compared only with itself. Close R600 and seven
of the eight go green in one commit. That is the most useful thing the number says this
round -- the misses have concentrated, which is what they did before R596 landed too.

## On the criterion, said once

I do not disagree with CZ0 and I am not asking for a fourth round or a wider blocking
head. Both findings here are inside (a)-(d): R600 is a gate assertion, R601 is a red
test at the reviewed commit. Everything else is in the closure list and I have not held
on any of it -- including four sentences I would have blocked on a year of rounds ago.

One observation about the mechanism rather than the criterion, and it leaves the loop
rather than becoming a round. **CZ0(d) and the milestone boundary are in tension, and
this step is the first place it bites.** The report cannot name a verdict in its own
milestone's review tree because none exists; the verdict cannot exist before the report;
and the guards that read both are parametrised over the pair. BU1 closed this for a step
boundary and the milestone boundary reopened it, because `_verdict_text_at` falls back
to the working copy when the named sha predates the tree. The state is legible -- the
implementer wrote it down in advance and the counts agree everywhere -- but "green means
green" does not hold here, and it is the one place my instructions say it must. That is
for Xabier, and the cheap answer is probably that the first report of a milestone names
the previous milestone's last verdict and its path, which is what it is actually
answering.

## Carried for the next step

**R600 and R601 carry BY NAME into the next round of `docs/reports/F3/step-1.md` and stay
BLOCKING.** R596, R598 and R599 are closed. Closure items C12, C14, C18 to C32, the open
part of C33 to C39 and C42, and C43 to C49 go into this step's closure commit as one list.

**Schedule.** F3 closes 13 October; the step report states the date and states that it
holds; I have no measurement that contradicts it. This is round 1 of 3, so nothing about
DZ7c is triggered yet. If this step reaches round 3 still carrying R600, DZ7c's rule
applies and **R600 is NOT ledgerable under it**: a frame whose geometry is unchecked can
change every member force in the table, which is exactly the test DZ7c sets.

## Next step opens when

**It does not open. This step stays open and these are the conditions, in this order:**

1. **R601 first, because everything else is measured against a green suite**, and
   because cause (a) is currently hiding whether R599's repair is green. The two
   DR1-compliant moves are named in the finding; choose one and say which.
2. **R600, all three sites, each with its diff hunk or the site named and the reason it
   was left.** The cell that closes it is "every member tip +3 m, applied in
   `_member_geometry` before `math.dist`", and it must go red.
3. **The closure list once, in one commit.**
4. Then the report's revision 2, with the generated sections, and the `Answers:` header
   naming THIS verdict at its own commit.

`python -m pytest -q` at `0 failed`, and a `workflow_dispatch` run at that commit with
`lint, unit and guards` green, are what I will check first.
