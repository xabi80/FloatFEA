# Review — F2 step 5
Reviewed commit: df00a01be0cbbf6201ba5f0615c302861c3f9e0f
Verdict: HOLD

**Reviewed commit: `6170263`.** Report revision 25, `Answers: verdict 50 @
f286a71`. The `Reviewed commit:` line stamped above by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus
commit `df00a01` -- not the commit judged. That is R373, still open; read
`6170263`.

Tests: **2559 passed, 0 failed, 0 skipped** at `6170263` (my run, clean tree,
`python -m pytest -q`, 538.76 s, Python 3.13 on Windows).

**Commits judged: `afc5b05`, `2a22543`, `651a524` (guard), `6170263`
(report).**

**Item 1b.** Revision 25 line 9210 reads `Answers: verdict 50 @ f286a71`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`f286a719674c4f1518fc222fb4f14b7da5287349`. It is the latest. **Passes.**

**The section 10 suite line reconciles exactly, and I measured it rather than
read it.**

```
cmd  git worktree add --detach <tmp> 651a524; pytest --collect-only -q
out  2589 tests collected
cmd  the same, for the three excluded files
out  386 tests collected
judge 2589 - 386 = 2203, which is the report's line to the unit. R339's
     "count what is excluded" is what made this checkable in one command.
cmd  pytest --collect-only -q, and the three files, at 6170263
out  2559 and 354 -- the revision-25 parametrisation is 32 smaller than
     revision 24's, which is why my whole-tree number is under 2589.
```

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT, AND ONE RED RUN NOBODY RECORDS

```
cmd  gh run list --commit 617026342249ffaf7d2aeff21a5624c966c978c3
out  run 35563850428, event push, conclusion SUCCESS, status completed
cmd  gh run view 35563850428 --json jobs
out  "lint, unit and guards"      success, 14 steps, 05:14:16 -> 05:21:13
     "the verification ladder"    success, 13 steps, 05:14:16 -> 05:17:03
     "CI determinism -- leg"      skipped, 0 steps
     "CI determinism -- ten legs" skipped, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I JUDGE. Not
     CK2: both ran real steps for minutes. The determinism pair is
     dispatch-only here and is recorded as an UNAVAILABLE check at this
     commit rather than skipped over.
cmd  python scripts/ci_section.py --rounds, re-run by me at this commit
out  the two committed rows reproduce BYTE FOR BYTE, plus a third for
     35563850428 that could not exist when the report was written. THE
     COMMITTED CI TABLE IS FAITHFUL. R449 is closed on its facts.
cmd  gh run list --limit 15 --json databaseId,headSha,conclusion,event
out  35561482997, event push, head 2bd9e897, conclusion FAILURE -- a fourth
     run this round, at the combined docs-plus-guard commit that was split.
cmd  gh run view 35561482997 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  9 rows, the first being
     test_a_docs_commit_does_not_also_edit_the_guard_that_judges_it
judge THE RULE FIRED IN CI AS WELL AS LOCALLY, and the split is its own
     remedy. THE REWRITE IS THE RIGHT ANSWER and I am saying so because I
     was asked: history stays linear, nothing but that one commit moved,
     --force-with-lease was used, and no verdict or report was rewritten.
     What is wrong is the silence -- see R461.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff --stat f286a71..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- NOTHING TOUCHED. No STOP-class finding.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation
cmd  git diff f286a71..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is being written by code in its own directory.
cmd  git diff f286a71..HEAD -- floatfea/tolerances.py | grep -E "^[+-][A-Z_]+.*Final"
out  (empty) -- NO CONSTANT MOVED. The 17 changed lines are comments.
```

## Carried

Verdict 50 held on R449-R454 and recorded R455-R458. **R449, R450, R451,
R452, R453 and R454 are answered at the sites their conditions named, and
R450 and R454 are answered better than asked. R455 and R456 are answered in
part and their residue is R464. R457 is answered. R458 is correctly left
open.** What holds this step is three new findings, and all three are the
same species the round was repairing: a sentence that one command refutes,
written in or around the repair.

- **R449 -- ANSWERED, and the repair is generation rather than care.**
  Section 0a is `scripts/ci_section.py --rounds`; a run whose status is not
  `completed` renders `**no result**` with no job lines, and the only reason
  a conclusion may carry is a failing test name from the same query.
  **Confirmed by re-running the generator: the two committed rows reproduce
  byte for byte, and `gh` agrees with both.** `scripts/review_invocation.py`
  imports `outcome()` rather than reimplementing it, and the invocation I was
  handed is that function's output -- the propagation path is closed at its
  source. **Closed on its facts.** What is not closed is that nothing
  compares the committed table with `gh`: R462.
- **R450 -- ANSWERED, and the enumeration now resolves.** The carve-out is a
  parse on the assigned VALUE, and the docstring records that testing the
  node type alone would have reclassified every `cmd:` as code -- the same
  defect one turn later, written down. `out:` is `4`; I ran
  `grep -n "log=True" scripts/regen_figures.py` and got lines 118, 130, 266,
  656, which is exactly the claim's enumeration: two `_floor(...)` calls and
  two comment lines. **Closed.**
- **R451 -- ANSWERED.** `tolerances.py:427-431` names
  `rigid_mode_corpus_refused` and its class as `floor_class()` returns it
  (`words`), and says the window row is not floor-class at all. **Closed.**
- **R452 -- ANSWERED.** `:399-402` reads `{{fig:rigid_mode_corpus_frames}}`
  and records that `114` stood there. **Closed.**
- **R453 -- ANSWERED.** Section 5 names `rigid_body_mode_ratio` as the
  tightest floor-class row from the `--check` run and says the mechanism row
  got looser. R447 is restated on the row it is about. **Closed.**
- **R454 -- ANSWERED, and it is the best repair in the round.**
  `retired_loss_over_ceiling_on_corpus` is a `words` row at `99 of 126`
  canonical; all four citing sentences now carry the figure reference; the
  rung-1 triple that asserted its ABSENCE asserts its presence and
  `count("docs/milestones/F2_figures.md", "retired_loss_over")` returns `1`,
  which I ran. My own loop last round measured `101` here against the
  published canonical `99`, which is why `words` is the right class.
  **Closed.**
- **R455, R456 -- ANSWERED IN PART, residue is R464.** `control_defect()` is
  a function with the five shapes as controls, `no` counts as an absence, the
  control file is excluded by name as well as by glob, and the triplicated
  line is gone. All five of my shapes are refused. **Six more are not**, and
  four of those need no new control line either.
- **R457 -- ANSWERED.** The conclusion guard decides per run; all twenty
  shapes transcribed. Not re-measured by me this round: the guard those
  shapes test is no longer the one that rules on section 0a, which is R462's
  point.
- **R458 -- OPEN, correctly, and not claimed.** Section 6 names the five
  paths that are out of scope and not declared out. 4a.
- **R447 -- OPEN, restated correctly on `rigid_body_mode_ratio`.** 4a.
- **R419, R431, R432, R433 -- OPEN, correctly listed.** 4a.
- **R411 -- ANSWERED for revision 25.** Its second line reads "Commits since
  the fiftieth verdict, listed in section 9"; section 9 is `Commits`, so the
  pointer is right this round after eight rounds wrong. It stays on the 4a
  list only as a recurrence watch.
- **R383 -- OPEN and unchanged.** No determinism leg executed this round: the
  pair is `skipped` at every push commit and no dispatch at a commit in this
  round completed with leg rows. Recorded as an unavailable check, not green.
- **R410, R413, R414, R400, R401, R402, R390, R391, R392, R393 -- OPEN at
  4a**, correctly listed.
- **R370, R371, R372, R373, R374 -- OPEN at 4a.** R373 bites again in this
  verdict's header.
- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350 second
  half, R330, R331, R332 -- OPEN at 4a, correctly listed.**
- **R231, R244, R245, R275 -- OPEN, unblocked.** Step R has not run.
- **R230, R261 -- OPEN by instruction, correctly listed.**
- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a.**
- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 12 status-versus-subject disagreement stays at 4a.
- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250,
  R251, R226, R227, R264 and R266 still have no row; R348 territory.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394-R399, R403-R409, R412, R415-R418, R420, R421-R430,
  R434-R446, R448 -- closed earlier**, not reopened.

## Findings

**First, what is right, and it is the larger part again.**

**GENERATING THE CI RECORD IS THE CORRECT ANSWER TO R449, AND I VERIFIED IT
AGAINST `gh` RATHER THAN READING IT.** The two committed 0a rows reproduce
byte for byte from the generator, and both agree with `gh run view`. The
cancelled run renders as `**no result**` with no reason attributed. The
invocation I was handed is `review_invocation.paragraph()`'s output and
imports `outcome()`, so the propagation the fiftieth verdict recorded cannot
happen through that channel again. R454's publication of the loss count is
the best repair in the round: three refuted grounds are named, the class is
`words` because the two machines disagree, and the four sentences that needed
the number now cite it.

**AND THE GATE HAS NOT MOVED.** `floatfea/` carries no executable change for
the seventh consecutive round; rung 1 is green in my run and in CI at the
commit I judge.

---

**R459. (BLOCKS, and it is the head. Two sentences in `floatfea/tolerances.py`
that a one-line `grep` refutes -- made false by THIS round's `afc5b05`, which
blinded the guard that would have seen it in the same commit. BP0 exactly:
the rule beneath a figure moved and the figures citing it were not
regenerated.)** `floatfea/tolerances.py:455-459` and `:556-562`.

```
code :455 "claim: two test files still name `RIGID_MODE_FLOOR` -- the gate
     file ... and the counter meta-test"
cmd  grep -rl "RIGID_MODE_FLOOR" tests/ --include=*.py
out  tests/test_counters_are_injected.py
     tests/test_tree_prose_consistent.py
     tests/verification/rung1/test_rigid_body_modes.py
judge THREE, NOT TWO, and the enumeration names two of the three.
code :556 "claim: three test files name this ceiling, and ONE OF THEM
     ASSERTS ON IT ... The other two are the literal scanner and the
     diagnostic."
cmd  grep -rl "RIGID_BODY_MODE_RATIO" tests/ --include=*.py
out  tests/test_no_tolerance_literals.py
     tests/test_tree_prose_consistent.py
     tests/verification/rung1/test_rigid_body_corpus.py
     tests/verification/rung1/test_rigid_body_modes.py
judge FOUR, NOT THREE.
cell ONE VARIABLE, THE COMMIT. git log -1 -S RIGID_MODE_FLOOR over
     tests/test_tree_prose_consistent.py returns afc5b05, this round. The
     constants entered that file as test data in _CONTROL_SHAPES. Both
     sentences were written at c65b1bb and were TRUE then.
cmd  the shipped vocabulary at this commit, files over tests globstar py
     for the needle RIGID_MODE_FLOOR
out  tests/test_counters_are_injected.py,
     tests/verification/rung1/test_rigid_body_modes.py     -- TWO
judge SO THE TRIPLE IS GREEN AND THE SENTENCE IS FALSE, and the reason is
     that _paths() now drops SELF from every glob. files() and count() no
     longer mean what a reader running the same search gets. The module
     states the cost as "no triple can make a claim about those two files";
     the ACTUAL cost is larger and was not stated -- every existing triple
     whose glob CONTAINS those files silently changed answer, and two
     published claims in floatfea/tolerances.py went stale in the same
     commit that narrowed the rule.
judge THIS IS R450 ONE LEVEL UP: a claim that is not what its command
     measures, created by the commit that redefined the command, inside the
     mechanism built to stop exactly that.
```

  **Closed when** `:455` and `:556` state counts that
  `grep -rl <needle> tests/ --include=*.py` returns, or the claims say
  explicitly that the vocabulary excludes the guard module and the controls
  file and the enumeration names the excluded file. Whichever is chosen, the
  commit that narrows a vocabulary word regenerates every `out:` and every
  claim sentence that word appears in -- one pass over nine triples.

**R460. (BLOCKS -- CP2. The repair for "figures go stale" publishes its own
figure twice, in the report and in the module, and no command at this commit
produces it.)** `docs/reports/F2/step-5.md` section 6 and
`scripts/precommit_stale.py:37-48`.

```
code s6  "cmd python scripts/precommit_stale.py, on this round's own diff"
     s6  "out 12 numbers, 0 renamed rows, 0 changed classes; 5 survivors,
          1 TRUE and 4 false"
code :38 the same figures in the module docstring, under "MEASURED ON ITS
     OWN ROUND, because a checker that has never been run on a real diff is
     a script"
cmd  python scripts/precommit_stale.py           (clean tree; the report's
     own command, which reads the STAGED diff)
out  precommit_stale: no figure class, row name or measured number removed
cmd  python scripts/precommit_stale.py f286a71..HEAD      (the round's diff)
out  looking for 41, no rows, no classes / no survivor
cmd  python scripts/precommit_stale.py afc5b05^..afc5b05  (the CX commit)
out  11 numbers, 0 rows, 0 classes; 14 SURVIVORS
judge NO SPEC AT THIS COMMIT PRINTS 12 AND 5. The nearest is 11 and 14.
cell ONE VARIABLE, the range: f286a71..2a22543 and f286a71..651a524 both
     print "no survivor", so the 14 are the canonical-versus-local render
     that 2a22543 resolved -- which is the report's own explanation of three
     of its four falses, at a count of 14 rather than 4.
judge AND I CLASSIFIED ALL 14: every one is an F2.md or F2_figures.md row
     holding a canonical value against a local render. ZERO TRUE, not one.
     The "1 TRUE" in both texts is a survivor that no longer survives --
     the marker was added in the same commit -- so the figure describes a
     tree that existed for the length of one git add.
```

  **Closed when** section 6 and the docstring carry a figure that a named
  command reproduces at the commit publishing it, or the docstring carries a
  pointer to section 6 and section 6 carries the spec -- BI3's own remedy,
  applied to `scripts/` rather than to `tolerances.py`.

**R461. (BLOCKS -- a `cmd`/`out` pair in the report whose command, run at the
report's own commit, returns four lines where the report shows three; the
missing line is the commit that records the history rewrite, and the rewrite
itself is nowhere in the report.)** `docs/reports/F2/step-5.md` section 9.

```
code s9 "cmd  git log --oneline f286a71..HEAD"
     s9 "out  afc5b05 ... / 2a22543 ... / (this revision's own commit
         follows)"
cmd  git log --oneline f286a71..HEAD                      (at 6170263)
out  6170263 docs: step-5 revision 25 ...
     651a524 CX0: the generated sections are split from the prose BY INDEX
     2a22543 CG2: the canonical render, with the loss count published
     afc5b05 CX0-CX3: CI facts are generated, and a control that can ...
judge FOUR COMMITS, AND 651a524 IS NOT IN THE LIST. The parenthetical
     accounts for one commit and two followed. Section 10 names 651a524 by
     sha, so the report knows it exists; section 9 was not re-run after the
     split.
judge WHAT IS MISSING IS NOT AN ARBITRARY COMMIT. 651a524 is the guard
     change to tests/test_report_carried.py -- the file that judges this
     report -- and its message is the only place in the repository that
     records the rewrite. A reader of the report cannot reach it.
cmd  a case-insensitive grep over revision 25 for force, rewrit, split,
     2bd9e89 and 651a524
out  one hit, section 10's suite sha. NOTHING SAYS A COMMIT WAS REWRITTEN.
cmd  gh run list --limit 15 --json databaseId,headSha,conclusion,event
out  35561482997, push, head 2bd9e897, conclusion FAILURE
cmd  git merge-base --is-ancestor 2bd9e897 HEAD
out  NOT-ANCESTOR -- and rounds_runs() filters on
     git log --format=%H judged..HEAD, so this run drops out of section 0a
     AND out of the generated invocation, identically and silently.
judge SO A RED PUSH RUN IN THIS ROUND IS INVISIBLE IN A SECTION TITLED
     "Runs since the commit verdict 50 judged", and the report does not say
     a commit was rewritten. That is CE1's species -- the CI record in the
     report is not the CI record -- reached by a route the generator cannot
     see. I am not classing it as apparatus for the same reason I did not
     class R449 as apparatus.
judge THE REWRITE ITSELF IS THE RIGHT CALL and I want that on the record:
     linear history preserved, one commit split, force-with-lease, no
     verdict and no report rewritten, and the rule that caught it is the
     rule working. The finding is the silence, not the rebase.
```

  **Closed when** section 9's `out` is what `git log --oneline f286a71..HEAD`
  prints at the report's own commit, and the report states in one sentence
  that the `docs:` commit was split after
  `test_a_docs_commit_does_not_also_edit_the_guard_that_judges_it` refused
  it, naming run `35561482997` at `2bd9e89` as a run of this round that
  section 0a cannot show, and why.

---

**Recorded, and lock items for step 4a (BU0). None of these touches the gate
assertion, a tolerance, or the truth of a published figure.**

**R462. Nothing compares a generated CI section with `gh`, so R449's exact
content is re-admissible by editing the table.** Measured at `6170263` by
applying each edit to the revision text and calling the three predicates in
`tests/test_report_carried.py` directly. (a) The cancelled row rewritten to
`conclusion **success**` -- all three pass. (b) The dispatch failure rewritten
to `success` with its fifteen failing-test bullets left underneath it -- all
three pass, and nothing cross-checks a row against the block generated from
the same run. (c) A row for run `99999999999` at head `deadbee` -- all three
pass. (d) **Every row deleted and the header kept** -- all three pass, because
the header-present assertion is satisfied by the header line alone, so a
whole round of runs can be suppressed. (e) The `Generated:` provenance line
is a string the guard asserts is present; nothing re-runs the generator.
Deleting section 0a outright IS caught, which is the control. The guard's own
docstring says "structural rather than byte-for-byte" and gives a true
reason -- the generator's newest row is not in the committed text -- but the
answer to that is to require the committed rows to be a SUBSET of a fresh
render, not to compare nothing. Six entries in
`tests/corpus/report_ci_section.txt`.

**R463. The exemption is keyed on a heading the implementer writes, and
`651a524` extended it to two sections whose columns are hand-written prose.**
The pattern is `^##+ (?:0[a-z]?|1[12])\.`. Measured: a paragraph under
`## 0b. What the runs mean`, naming a real run with a false story and an
invented run id beside it, passes all three guards, because `0b` through `0z`
are read as generated. Sections 11 and 12 were added this round; section 11's
"why it was left" column is hand-written by the implementer, which the report
itself states, and a row whose reason cell reads
"run 35559285688 concluded success, ladder green" passes all three. The
reason for adding 11 and 12 is sound -- they quote the verdict, and a verdict
naming a run id would otherwise redden the report -- but the unit of
exemption should be the quoted text, not the section.

**R464. `control_defect()` constrains the EDGES of a needle and not its
interior, so every substring of every planted control line is an acceptable
needle.** Measured by calling the shipped function; entries in
`tests/corpus/prose_triple_shapes.txt`. Four shapes are ALLOWED with `out: 0`
or `out: none` under needles that occur nowhere in the tree, and **none of
the four adds a control line** -- each uses one already shipped and planted
for a different triple: `RIGID_MODE_FLOOR * norm` (floor_constant_name),
`RIGID_BODY_MODE_RATIO_COUNTER_DEFECT * scale` (ratio_counter_name),
`= last_below(spectrum, tau)` (last_below_needle), and the `files()` variant
of the first. The trailing-space rule from R455(a) is a fix for one instance;
the class is that a 30-to-50 character planted line has hundreds of
substrings. **And the uniqueness rule points the wrong way**:
`RIGID_BODY_MODE_RATIO`, which has nine real hits in `tests/`, is refused for
matching two controls, while `> RIGID_BODY_MODE_RATIO:`, which has one, is
allowed -- the narrower needle is the one more likely to be malformed.
R455(c) is **withdrawn in substance**: `0 of 12` and a bolded `none` do
escape `control_defect()`, but `test_a_prose_triple_still_says_what_the_tree_
says` compares on equality and refuses both, so the shape cannot ship.

**R465. `scripts/precommit_stale.py` is wired to nothing.** A grep for
`precommit_stale` over `.github/`, `.claude/` and every `*.sh`, `*.yml`,
`*.json` and `*.py` outside the script itself finds only
`tests/test_precommit_stale.py`. It is a pre-commit checker that no
pre-commit runs, so whether it fires depends on the implementer remembering,
which is the failure mode CX1 was written to close. **The recorded miss IS
honestly recorded and I endorse that half**: R454's four sentences name
neither a number nor a row, the docstring says so, and the test asserts the
miss rather than a success. On the value question -- a four-in-five false
rate is acceptable for a checker that runs, because each false costs one
look; unwired, the rate is moot. And it did not catch this round's own
staleness: R459 is a WORD, not a number, and `tests/` is outside
`MEASURED_PROSE`.

**R466. `_paths()` reports a false reason for the two excluded files.** A
count over `tests/test_tree_prose_consistent.py` raises `ValueError: the
pattern 'tests/test_tree_prose_consistent.py' matches no file under the
repository root`, about a file that exists and is tracked. The same for
`tests/prose_triple_controls.txt`. Raising is right (R443a); the message is a
claim about the repository that is false.

## Tolerances touched

**NONE. No constant was created, retired, or moved.**

```
cmd  git diff f286a71..HEAD -- floatfea/ | grep -E "^[+-][A-Z_]+.*Final"
out  (empty)
cmd  git diff --stat f286a71..HEAD -- floatfea/
out  floatfea/tolerances.py | 17 ++-   -- ONE FILE, every line a comment
judge NO VALUE WAS WIDENED AND NO VALUE MOVED. What changed is prose: the
     R451 class sentence, the R452 figure reference, and the R454 loss-count
     references. Two OTHER comment neighbourhoods in the same file carry
     R459, which this file did not cause -- it was caused by a commit in
     tests/ narrowing the vocabulary underneath them.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2559 passed at 6170263 -- no undeclared literal entered tests/ this
     round and nothing was added to tolerance_marker_exemptions.txt.
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**CX4 asked for PASS with the 4a list carried, or HOLD naming the head. The
head is R459** -- two sentences in `floatfea/tolerances.py` that
`grep -rl <needle> tests/ --include=*.py` refutes, made false by `afc5b05`,
the commit that narrowed the vocabulary and excluded the guard module in the
same breath. I am not classing that as apparatus: it is a claim in the file
CLAUDE.md singles out, it is false as written, and the mechanism that would
have caught it is the one that commit disabled.

**Three items hold.**

1. **R459 -- "two test files still name `RIGID_MODE_FLOOR`" where three do,
   and "three test files name this ceiling" where four do.** The
   vocabulary's glob stopped meaning what a reader's grep means, in the
   commit that made both sentences false.
2. **R460 -- "12 numbers ... 5 survivors, 1 TRUE and 4 false"**, published
   in the report and again in the module, where the nearest command at this
   commit prints 11 numbers and 14 survivors, all fourteen false.
3. **R461 -- section 9's commit list is missing `651a524`**, and the report
   nowhere records that a pushed commit was rewritten or that run
   `35561482997` at `2bd9e89` concluded `failure` this round.

**The finding behind the findings, fifth round running, and it has narrowed
again.** Last round I wrote that the attention goes to the thing being fixed
and the prose around the fix inherits none of the discipline. This round the
generated things are RIGHT -- I checked section 0a against `gh` and it
reproduces byte for byte, and the invocation is the same function's output.
All three holds are in the hand-written residue around generated work: two
sentences a redefined glob left behind, a figure in one of the few sections
that is not generated, and a commit list that was not re-run after the
history underneath it moved. **Each of the three is fixed by re-running a
command the repository already has.** Six of revision 25's thirteen sections
are generated and not one of the six carried a finding this round; three of
the seven hand-written ones did. That is the argument for generating section
9 too, and it is an argument about this arrangement rather than about
attention.

**Adversarial corpus (BE3): 24 new entries across two files, all unseen by
the implementer, committed separately at `df00a01`.**

**`tests/corpus/prose_triple_shapes.txt`, 22 to 35. Thirteen entries: twelve
defect shapes and one allow-control. The shipped code refuses 2 of the 12 --
both by `test_a_prose_triple_still_says_what_the_tree_says` on equality, NOT
by `control_defect()`, which is the function CX2 built.** All five of my
previous shapes are refused, which is the repair working; four of the new
ones re-admit R434 using control lines already in the file.

**`tests/corpus/report_ci_section.txt`, 43 to 54. Eleven entries: ten defect
shapes and one control. The shipped guards refuse 0 of the 10; the control --
section 0a deleted outright -- is caught.**

**Coverage measurement: 2 of the 22 new defect shapes are caught, and neither
by the check written for its class.** The implementer's own count -- five
re-admission shapes, all refused -- is the count of the shapes I handed over
last round, which is exactly what BE3 exists to separate from coverage.

```
cmd  python -m pytest tests/test_report_carried.py -q     (after my adds)
out  test_every_corpus_shape_is_transcribed goes red on my 11 new ids, which
     is the R440 mechanism working. The 2559-pass run above is at 6170263,
     before my corpus commit.
```

**Not gates on step 5, into the next report's Carried section:** R462, R463,
R464, R465, R466, R458, R447 (restated), R419, R431, R432, R433, R410, R411
(answered for revision 25, kept as a recurrence watch), R413, R414, R400,
R401, R402, R390, R391, R392, R393, R383, R370, R371, R372, R373, R374,
R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350 second
half, R330, R331, R332, the section 12 status-versus-subject disagreement,
R321, R322, R300, R291, R292, R281, R231, R244, R245, R275, R230, R261, the
underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a.
**R449, R450, R451, R452, R453, R454 and R457 are closed.** R455 and R456
close in part and reopen as R464; R455(c) is withdrawn in substance.

**Fifty-one rounds have found no element defect and this round found none
either.** Rung 1 green in my run and in CI at the commit I judge; two CI jobs
with real steps on Linux at `6170263`; the loss count now published at
`99 of 126` canonical against the `101` I measured independently last round,
which is why `words` is the right class for it. It still means "not yet
contradicted": ladder 5 has printed `OK -- 0 directories ran` every time it
has run, no determinism leg executed at any commit in this round, and V5.1
against CalculiX is the witness that has not spoken.
