# Review — F2 step 5
Reviewed commit: 99fae70abc8a100eefb76f0bd25ecfc39e324df3
Verdict: HOLD

**Reviewed commit: `17bd759`.** Report revision 17, `Answers: verdict 42 @
c85511b`. **The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`99fae70` -- not the commit judged.** That is R373, still open; read `17bd759`.

Tests: **2073 passed, 0 failed, 0 skipped** at `17bd759` (my run, clean tree,
`python -m pytest -q`, 465.90 s, Python 3.13.15 on Windows).
`pytest --collect-only -q` gives **2073**, so nothing is skipped and nothing
silently uncollected. Rung 1 and the whole tree are green at the implementer's
head.

**AND 1 FAILED AT MY OWN CORPUS COMMIT `99fae70`**, which BE3 requires me to
make: `tests/test_report_guard_states.py::test_the_guard_survives_the_state
[two_digit_step_number]`. That is R377, and it is not an artefact of my file --
it reproduces on a one-line corpus commit in a clean clone, and it was red in
CI at `c85511b`, in the run this round mined for `03e5f92`.

**Commits: `286343b`, `3a125f2`, `c28be03`, `03e5f92`; `process:` `ce2071d`
and `a4621c3`. Report `17bd759`.**

**Item 1b.** Revision 17's header at line 5954 reads `Answers: verdict 42 @
c85511b`; `git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`c85511bfff2d281072d6825a8dc7b3d3b94b367f`. It is the latest. **Passes.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT, AND ONE JOB DID NOT RUN

```
cmd  gh run list --commit 17bd759 --json name,conclusion,workflowName
out  run 34663480634 -- event push, conclusion SUCCESS, head_sha
     17bd759bcfb6e23d8dbd774c13c709589298bb46
cmd  gh api .../runs/34663480634/jobs
out  "lint, unit and guards"      success, runner 1000000946, 14 steps
     "the verification ladder"    success, runner 1000000947, 13 steps
     "CI determinism -- leg"      SKIPPED, runner null, 0 steps
     "CI determinism -- ten legs agree"  SKIPPED, runner null, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING.
     This is not why the step holds. Not CK2 either: runners were assigned
     and steps ran, so the allowance is not the constraint this round.
judge THE DETERMINISM JOBS ARE AN UNAVAILABLE CHECK HERE, by design --
     `workflow_dispatch` only. Recorded as unavailable rather than skipped
     over, and with the thing CK2 asks for:
cmd  git diff --stat 9cec13e..17bd759 -- tests/verification scripts .github
out  .github/workflows/ci.yml | 38 +++++++++---------
judge SO THE LAST EXECUTED DETERMINISM RUN (34658132995, at `9cec13e`) NO
     LONGER DESCRIBES THE TREE UNDER REVIEW. `3a125f2` rewrote the ten-legs
     aggregation and that code has never executed anywhere. R383.
cmd  gh api .../runs/34659275127/jobs  (at `c85511b`, verdict 42 own commit)
out  FAILURE. "lint, unit and guards": 1 failed, 708 passed. The failure is
     `test_report_guard_states.py::...[two_digit_step_number]`, NOT a
     report-site guard -- those 70 are inside the replay and ARE explained by
     the report predating the verdict. This one is not. R377.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff c85511b..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- nothing in this range touches either. No STOP-class finding.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                     -- the instruction own expectation
cmd  git diff c85511b..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
cmd  git diff c85511b..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat c85511b..HEAD -- floatfea
out  (empty) -- eighteen rounds
cmd  git show --name-only on each of the seven commits
out  `ce2071d` touches tests/test_report_carried.py only; `a4621c3` touches
     CLAUDE.md only. Both are standalone and both cite their directive (CP1,
     CP2) in the subject. No commit mixes process with code, and nothing
     under `.claude/` moved at all.
```

## Carried

Verdict 42 held on R365, R366, R367 and R368. **Two close cleanly and I
reproduced both. One closes at the leaf it named, and the property its
docstring claims is refuted by a one-line edit. One does not close.** I ran
every closing condition rather than reading it.

- **R365 -- ANSWERED AT THE LEAF IT NAMED, and section 1 reproduces to the
  digit. The door is not shut: R375 and R376.**

```
cell clean clone at 17bd759: (a) `ast.walk(inner)` -> `ast.walk(inner.right)`,
     then the R365 `src` rewrite in `_entries()`, restored between rows
out  CLEAN                      77 passed
     (a) alone                   2 failed, 75 passed -- real regressions, and
                                 detect_declared_raised_to_a_literal is named
     (a) + rewrite `src`         1 failed, 76 passed
                                 test_every_entry_reaches_the_assertions
judge EVERY ROW OF SECTION 1 REPRODUCES. The round trip is sound for the
     field it reads: `unicode_escape` encoding is injective, so the parsed
     `src` is pinned to exactly what the bytes decode to, and a field added
     later really is covered the day it is added. This is a better repair
     than the two before it and I want that recorded.
```

- **R366 -- ANSWERED at both named sites, checked at each.**

```
cmd  grep -n "carries no code" tests/test_report_carried.py
out  1203 -- one hit, inside the paragraph that withdraws it
judge THE SENTENCE IS GONE FROM WHERE IT WAS ASSERTED and survives only as a
     quotation in its own withdrawal. The first named site, the
     `CO3, R358: REVIEWER COMMITS DO NOT COUNT` block, now states CP1 two
     halves and they are the rule in the file beneath it. Both sites, not
     one. Closed.
```

- **R367 -- ANSWERED, and I ran the cell in both directions on the real
  repository rather than on the synthetic history.**

```
cell ONE VARIABLE: a commit on top of `17bd759`, everything else held.
cmd  clean clone at 17bd759, pytest tests/test_report_carried.py -k whole_suite
out  2 passed
cmd  add tests/unit/test_zz.py with two collected tests, commit, rerun
out  1 failed: "1 commit(s) touching code follow the report own commit
     `17bd759` ... f08d144 a code change after the count"
cmd  reset, append one line to tests/corpus/..., commit, rerun
out  2 passed
judge THE CASE VERDICT 42 DEMONSTRATED IS CAUGHT NOW, and the corpus
     direction is still exempt. The repair is not the one I named -- it
     bounds what may FOLLOW the anchor by pathspec rather than bounding the
     anchor against HEAD -- and in the implementer direction it is stricter:
     zero, not a distance. Closed on its merits, and the shape is right: the
     cell is a test on a synthetic history, so the next version of the rule
     has to survive it before it ships.
judge WHAT IS NOT CLOSED IS THE ANCHOR OWN FALLBACK. R377.
```

- **R368 -- NOT ANSWERED. The four rows are still in the file and section 3
  says they are gone.** R380.

- **R369 -- ANSWERED (`3a125f2`), and I exercised the predicate rather than
  reading it.** The five rows in the commit message reproduce exactly. Two
  edges it does not cover, and the fact that it has never executed anywhere,
  are R383.

- **R370, R371, R372, R373, R374 -- OPEN at 4a, correctly listed in section 6
  and rowed in section 8.** R372 is withdrawn by the report at its own site,
  which is the right disposal. R374 is re-measured below and it MOVED, for
  the first time in five batches.

- **R362, R363, R364 -- OPEN at 4a, correctly listed.** R364 is answered in
  part this round: CP4 is the first species closure of this milestone that
  held on shapes its author had not seen. The ceiling argument stands.

- **R354, R355, R356, R357 -- OPEN at 4a, correctly listed.** R356 is R351
  species in four more readers; R375 and R376 make that family larger again.

- **R347, R348, R349, R350 second half -- OPEN at 4a, correctly listed.**
  R348 site-parser gap is why R366 second site went unasked; still 4a.

- **R330, R331, R332 -- OPEN at 4a, correctly listed.** R332 honoured again:
  nothing reads `g21_rigid_body_frames.txt`, so I added nothing to it.

- **R231, R244, R245, R275 -- OPEN, unblocked, and the report correctly does
  not claim them.** The render is canonical and CI is green; taking the Q8
  values is the plan business.

- **R223, R224 -- Q7 condition is met and measured** (green CI at a reviewed
  commit, twice now). CP5 asks that I open Q7 on this verdict "without gate
  items". I cannot: this verdict has gate items. Recorded so the ask is not
  lost rather than silently declined.

- **R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged
  and stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** The
  generated table still expands a range by its endpoints only, so R250, R251,
  R226, R227, R264 and R266 have no row; R348 territory, unmoved.

## Findings

**R375. (BLOCKS -- the fourth leaf. My adversarial case passed when it should
have failed, at whole-suite scale, and the edit is ONE LINE in the one thing
the docstring names as shared between the two readers.)**
`tests/test_marker_exemption_corpus.py:42-43`, `:49-52`, `:68`, `:148-150`,
`:180-195`.

```
code :42  "So the file is read TWICE, by readers that share nothing but the
     :43   path"
code :49  "an edit in the parser has to be made identically in two places to
     :50   stay invisible"
judge THE PATH IS A MODULE CONSTANT AND IT IS ONE PLACE. `_entries()` reads
     `CORPUS`; `_entries_in_the_file()` reads it; `_headers_in_the_file()`
     reads it; `test_the_growth_rule...` reads it. Move `CORPUS` and all four
     move together, in agreement, byte for byte.
cell TWO EDITS, BOTH IN FILES THE IMPLEMENTER OWNS, clean clone at 17bd759:
     (a) `ast.walk(inner)` -> `ast.walk(inner.right)` in
         `_literal_thresholds_inside` -- the same genuine, plausible
         tightening verdicts 40, 41 and 42 all used
     (f) THIRTEEN LINES after `CORPUS = ...`, under a comment about CRLF:
             _NORMALISED = Path(tempfile.gettempdir()) / "ffea_corpus_lf.txt"
             _NORMALISED.write_bytes(
                 CORPUS.read_bytes()
                 .replace(bytes([13, 10]), bytes([10]))
                 .replace(b"ROUNDOFF_IDENTITY ** 2.0",
                          b"2.0 ** ROUNDOFF_IDENTITY")
             )
             CORPUS = _NORMALISED
out  after (a) alone
       pytest tests/test_marker_exemption_corpus.py   2 failed, 75 passed
     after (a) and (f)
       pytest tests/test_marker_exemption_corpus.py   77 passed
       python -m pytest -q   (THE WHOLE SUITE, 471.65 s)
                                                      2073 passed, 0 failed
       WHICH IS THE CLEAN TREE NUMBER EXACTLY (2073 passed, 0 failed).
judge NO CORPUS EDIT. NO FIELD REWRITTEN. THE ROUND TRIP IS INTACT -- it
     compares the parser output to the bytes of the file the parser read, and
     both readers read the substituted file. The count agrees, the partition
     holds, PLANTED_ESCAPES is unchanged, and the pass count does not move by
     one the way R351 and R359 did. It moves by zero.
judge THIS IS THE DOCUMENTED EVASION SHAPE, and the hook says so about
     itself: `.claude/hooks/protect-reviews.sh:80-84`, "a path assembled at
     runtime from pieces is not caught". The corpus FILE is protected; which
     file is called the corpus is not.
judge THE COVER STORY IS NOT EXOTIC EITHER. Normalising CRLF before handing
     bytes to a regex is a plausible Windows repair in this repository, and
     the second `.replace` is one line inside it.
```

**Closed when** the bytes the parser actually read are compared against
something the implementer cannot write in a working tree -- the tracked blob,
`git -C ROOT cat-file blob HEAD:tests/corpus/tolerance_marker_exemptions.txt`
against `CORPUS.read_bytes()`, which costs one subprocess in a file that
already shells out to `git blame` at `:268-275` -- with a cell showing it RED
under the redirect above and green on the clean tree; **or** `:42-52` stops
saying "two places" and says what is true: the two readers share one path, the
path is a module constant, and one line that moves it moves both. **Either
closes it. What may not stand for a fourth round is the sentence and the code
disagreeing.**

**R376. (BLOCKS -- the fifth leaf, in the code verdict 42 named when it said
the classification remains yours to edit. Measured rather than argued.)**
`tests/test_marker_exemption_corpus.py:243-259`.

```
judge THE ROUND TRIP PINS THE FOUR FIELDS AND NOTHING DOWNSTREAM OF THEM.
     `_planted_caught()` turns (expect, measured) into the partition, and
     PLANTED_ESCAPES is the set the regression test SUBTRACTS.
cell (a) as above, plus a three-line special case in `_planted_caught` that
     returns False for one id -- moving that entry out of ASSERTED and into
     the allowed escapes. Clean clone at 17bd759.
out  pytest tests/test_marker_exemption_corpus.py    76 passed, 0 failed
judge GREEN, WITH THE SAME GENUINE REGRESSION PLANTED. The round trip passes;
     `covered == names` passes, because both sides of the partition come from
     the same function and it cannot see a move between them; and the
     `_did_catch` vocabulary test passes, because it asserts the four values
     and not the derivation. The entry simply stops being asserted. The pass
     count drops by one, which is what R351 and R359 also did, and which
     nothing in the file reads.
```

**Closed when** the two sides of the partition are each pinned to the corpus
rather than to a function -- the simplest form being that the asserted set is
recomputed from `_entries_in_the_file()` and compared, so a special case in
`_planted_caught` disagrees with itself -- with a cell showing it red under a
one-id special case; **or** the docstring at `:35-52` states that the split
between asserted and escaping is made by implementer code that no second
reader checks, so a reader knows where the reach ends. **I would take the
sentence.** R375 and R376 together say the honest answer is one paragraph,
not a fourth mechanism.

**R377. (BLOCKS -- a RED test in the shipped suite at the commit BE3 requires
me to make, isolated by a one-variable cell, in the rule this round changed.
`_report_anchor()` degrades silently to the form R361 refuted, and switches
CP1 rule 2 off entirely while it does.)**
`tests/test_report_carried.py:1112-1125`, `:1141-1143`.

```
code :1124 return last.stdout.strip() or "HEAD"
code :1141 if anchor == "HEAD": return []   -- "not committed yet"
judge THE FALLBACK IS NOT ONLY "NOT COMMITTED YET". Any state in which
     `git log -1 -- REPORT` comes back empty -- a report path with no
     history, which is what several of the harness own states construct --
     takes it. In that state rule 1 measures the distance to HEAD, which is
     exactly the pre-CP1 rule R361 refuted, and rule 2 returns the empty
     list, so the half that makes the claim true is switched off.
cell ONE VARIABLE: one corpus-only commit on top of 17bd759, nothing else
     touched, clean clone.
cmd  pytest tests/test_report_guard_states.py -k two_digit_step_number -q
out  BEFORE   1 passed
cmd  append one line to tests/corpus/tolerance_marker_exemptions.txt, commit,
     rerun the same test
out  AFTER    1 failed
     "the whole-suite line names 03e5f92, which is 2 commit(s) behind HEAD"
     assert 2 <= 1
judge SO THE HARNESS GOES RED ON A REVIEWER COMMIT, one level of indirection
     out from the contradiction CO3 exempted the trees for and CP1 claims to
     have resolved by pathspec. At my own corpus commit 99fae70 the whole
     suite is 1 failed; at 17bd759 it is 2073 passed, 0 failed.
judge AND IT WAS ALREADY RED IN CI, AT c85511b, IN THE RUN THIS ROUND MINED.
     Run 34659275127, job "lint, unit and guards": 1 failed, 708 passed, and
     the one failure is this test -- outside the 70-failure report-site block
     that the report legitimately predates. 03e5f92 came out of that run;
     this did not, and nothing in revision 17 names it.
     `test_a_RED_suite_is_named_in_the_report` exists for this.
```

**Closed when** `_report_anchor()` distinguishes "the report is dirty and not
yet committed" from "this report path has no history", and the second raises
or is carried into the rule rather than becoming HEAD -- with the
one-variable cell above run in both directions at the commit that publishes
the change, **and** the `two_digit_step_number` state green at a commit that
has a reviewer-only commit on top of the report. If the harness expectation
is what is wrong rather than the anchor, say so with the measurement. What
may not stand is a test that is red every round at a commit the process
requires.

**R378. (BLOCKS -- an `out` block that is not what its `cmd` prints, in the
revision that records CP2. The omitted line is a commit that changed a guard
matcher, and it is described nowhere in the report.)**
Report section 10, lines 6288-6295.

```
code s10 "cmd  git log --oneline c85511b..HEAD"
code s10 the pasted output: FIVE commits, 286343b through a4621c3, then
         "(this revision own commit follows)"
cmd  git log --oneline c85511b..03e5f92   -- HEAD when that block was written
out  03e5f92 The CI-row reader stopped at the first comma, so a complete
             table read short
     a4621c3   c28be03   3a125f2   ce2071d   286343b        -- SIX, not five
judge THE COMMAND PRINTS SIX LINES AND THE REPORT PASTES FIVE. The missing
     one is not a formatting detail: 03e5f92 widened `_CI_ROW` from
     `[\w .\-]` to `[^|`]`, the matcher a guard uses to read the CI table.
     It appears in the revision only as a sha inside section 7 suite line.
     A reader building the review list from section 10 never reads it.
cmd  grep -n "CI-row\|_CI_ROW\|first comma" docs/reports/F2/step-5.md
out  no hit anywhere in revision 17
```

**Closed when** section 10 `out` is the command actual output, and the change
03e5f92 makes is described somewhere in the revision that ships it. One
triple is enough and the commit message already has the material.

**R379. (BLOCKS -- section 5 `out` lists two of the four sites its own `cmd`
reports, and calls them "both". And the guard module docstring cites, as a
CLOSED breach, a literal that stands undeclared in the package today.)**
Report section 5, lines 6109-6124; `tests/test_no_tolerance_literals.py:1`,
`:3-6`, `:492`; `floatfea/io/reader.py:155`, `:206`, `:223`;
`floatfea/io/frames.py:358`.

```
code s5  "out   2 files reported, both in the package:
            floatfea/io/frames.py:358   isclose(..., atol=1e-12)
            floatfea/io/reader.py:155   isclose(..., atol=1e-9)"
cmd  offending() over every *.py in floatfea/ and scripts/, at 17bd759
out  floatfea\io\frames.py [(358, isclose(atol=<literal>))]
     floatfea\io\reader.py [(155, isclose(atol=<literal>)),
                            (206, allclose(rtol=<literal>)),
                            (223, allclose(rtol=<literal>))]
judge FOUR SITES, NOT TWO, AND "BOTH" IS FOUR. `:206` is rtol=1e-9 on the
     time-base uniformity check and `:223` is rtol=1e-10 on the inertia
     symmetry check. ALL THREE READER SITES DECIDE WHETHER A RECORD IS
     REJECTED, which is the one thing CLAUDE.md Non-negotiables say may never
     be soft.
code guard docstring :3-6 "every numerical tolerance lives in
     floatfea/tolerances.py. That was a rule, and it was broken three times
     -- an undeclared rtol=1e-10 (AW2) ..."
judge AN UNDECLARED rtol=1e-10 IS AT reader.py:223 RIGHT NOW, in the tree the
     guard first line says nothing may reach. The module title is "No
     undeclared tolerance may reach a comparison"; its domain at `:492` is
     TESTS.rglob("test_*.py").
cmd  git log -S "rtol=1e-10, atol=0.0" -- floatfea/io/reader.py
out  a90d060 2026-08-13 "F1: reader + validator with the G1.2 rejection
     matrix" -- one commit, the original. All four have been there since F1
     and no round of this milestone has seen them.
judge reader.py:155 IS ALSO THE TOLERANCE-FORM DEFECT VERBATIM: rtol=0.0 with
     atol=1e-9 on |g| in m/s^2 is an absolute tolerance on a dimensional
     quantity. Under a unit system scaled by a thousand it is a different
     test, which is the thing the form rule exists to forbid.
judge THE IMPLEMENTER IS RIGHT THAT DECLARING THEM IS NOT A REPAIR COMMIT.
     Two things are separable and only one of them is step 5.
```

**Closed when** (i) section 5 `out` is what the command prints -- four sites,
three of them rejection thresholds -- and the sentence stops saying "both";
and (ii) the guard docstring stops asserting a repository scope it does not
have, at `:1` and `:3-6`, names its actual domain, and names reader.py:223 as
a live instance of the very literal it cites as closed. **Declaring the four
values is NOT asked for here**: that is a tolerance change with a written
justification plus a domain widening that reddens the build, it needs a plan
row, and it should get one at 4a or in a step of its own. What blocks is the
published sentence, not the literal.

**R380. (BLOCKS -- R368 condition is not met. The four rows still stand in the
file, unmarked, and section 3 says they are gone.)**
Report lines 5617-5618 and 5623-5627; section 3, line 6068.

```
cmd  grep -n "or True" docs/reports/F2/step-5.md
out  5618 and 5624 -- plus 4710, a different and properly sourced use
code :5618 "verdict 39 `or True` on the `isinstance` line, which is what
            produced the published threes"
code :5625 "out   57 passed / 3 failed 54 passed / 3 failed 53 passed / 57
            passed"
code s3    "so the comparison table is gone rather than corrected a third
            time"
cmd  git diff --stat c85511b..HEAD -- docs/reports/F2/step-5.md
out  365 insertions(+), 0 deletions(-) -- purely additive, so revision 16
     section 2 is byte-identical
judge "GONE" IS REFUTED BY ONE GREP. What is true is that revision 17 does
     not republish them. A reader at line 5618 reads an attribution verdict
     42 refuted -- verdict 39 own cell describes a narrowing of
     `_literal_thresholds_inside` and reports "4 failed, 70 passed" -- with
     nothing at the site to say so.
judge THIS IS R366 SPECIES, IN THE ROUND THAT FIXED R366, and by the
     implementer own standard: a withdrawn sentence surviving at its site is
     the finding, and the remedy they chose there was a marker AT the site.
```

**Closed when** the four rows and the "verdict 39 `or True`" sentence carry a
withdrawal at their own lines -- a marker inside revision 16 section 2 that
names the verdict which withdrew them and points at revision 17 section 1 --
**or** they are deleted. I said "deleted" last round; a marker is the better
answer for an append-only log and either closes it. What may not stand is
section 3 saying "gone".

**R381. (recordable, 4a) CP4 second species has no magnitude bound, so
`float("inf")` is reported as a tolerance.** `_float_of_a_string` in
`tests/test_no_tolerance_literals.py`. Measured on a corpus entry I planted
this round, `clean_float_of_the_string_infinity`: `assert cost < float("inf")`
returns "comparison against float(<string>) = inf". The folding species bounds
itself at one with a written justification; the string species excuses 0.0 and
1.0 and nothing else, so infinity and NaN are tolerances to it -- and unlike
every other shape this file flags, `float("inf")` has no bare-literal spelling
for the older rules to be consistent with. One `math.isfinite` clause. Nothing
in the tree hits it today, which is why this is 4a and not a gate item.

**R382. (recordable, 4a, and loudly) A load-bearing pathspec is assembled from
pieces, which is this repository own documented evasion shape, with no comment
saying why.** `tests/test_report_carried.py:1130`:
`REVIEWER_TREES = ("tests/corpus", "docs/" + "re" + "views")`. The value is
correct and the rule built on it works -- I ran it both ways under R367. The
objection is legibility with consequences: `grep -rn "docs/reviews" tests/`
does not find the one place in `tests/` that decides which commits are the
reviewer own, and `.claude/hooks/protect-reviews.sh:80-84` names "a path
assembled at runtime from pieces" as the limitation that makes that hook worth
less than it looks. If the concatenation exists to get an edit past that hook
whole-command scan, then that sentence is what the line needs beside it.

**R383. (recordable, 4a) CP3 predicate has no shipped test and has never
executed anywhere.** `.github/workflows/ci.yml:279-290`;
`tests/test_ci_workflow_is_wellformed.py` has eight tests and none of them
reads `leg_is_red`. The determinism jobs are `workflow_dispatch` only and were
SKIPPED at 17bd759; the last dispatch that ran them was at 9cec13e, before
3a125f2 rewrote them. I lifted the predicate out and ran it: the five rows in
the commit message reproduce exactly, and two edges do not hold --
"4 collected, 0 failed, 2 errors" reads GREEN, because errors are not in its
vocabulary, and a line carrying two `failed` counts takes the LAST, so
"4 collected, 10 failed, 0 failed" reads green. Neither is reachable from the
leg own writer today, which is why this is 4a. That a gate own predicate is
exercised only by a paste in a commit message is the finding, and it is the
second repair to this job in three rounds that shipped unexecuted.

**R384. (recordable, 4a) A declared tolerance scaled by an INTEGER factor
falls between two rules and is invisible.** Measured on two corpus entries I
planted this round: `assert err < ROUNDOFF_IDENTITY / 1000` and
`assert err < ROUNDOFF_IDENTITY * 1000` are both clean. The folding rule
refuses any expression containing a name, for a stated and correct reason; the
BinOp rule wants a FLOAT literal beside the name. An integer between them is
neither. CLAUDE.md names this shape in its own words -- "any factor introduced
to make two numbers agree" -- and tightening or widening a declared tolerance
is the form it takes here.

## Tolerances touched

**None in `floatfea/tolerances.py`.** `git diff c85511b..HEAD -- floatfea` is
empty over the whole package.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| everything in `tolerances.py` | unchanged | -- | -- | the diff over the file is empty |
| `floatfea/io/reader.py:155` `atol=1e-9` | unchanged, UNDECLARED | **absolute on a dimensional quantity** (m/s^2), `rtol=0.0` | none exists | nowhere -- it is not in `tolerances.py`. R379 |
| `floatfea/io/reader.py:206` `rtol=1e-9` | unchanged, UNDECLARED | dimensionless, on the time step | none exists | nowhere. R379 |
| `floatfea/io/reader.py:223` `rtol=1e-10` | unchanged, UNDECLARED | dimensionless, on the inertia tensor | none exists | nowhere. R379 |
| `floatfea/io/frames.py:358` `atol=1e-12` | unchanged, UNDECLARED | absolute, on omega in rad/s | none exists | nowhere. R379 |

```
judge NO NUMBER IN ANY OF THE SEVEN COMMITS FUNCTIONS AS A TOLERANCE. CP4
     "under one, and not zero" is a CLASSIFICATION BOUNDARY inside a scanner,
     not a threshold on a measured quantity -- and I pinned it from both
     sides in the corpus rather than taking the docstring word for it:
     `1 / 2` folds to 0.5 and is caught, `1000 / 1000` folds to 1.0 and is
     clean. The workflow predicate is an integer comparison. `distance <= 1`
     is unchanged in value.
cmd  my whole-suite run includes the shipped literal scanner over tests/ and
     scripts/
out  2073 passed at 17bd759 -- no undeclared literal entered tests/ this
     round. The four in `floatfea/` are outside that scan and always were.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin, and Q7 does not open on this
verdict** -- CP5 asks for a verdict without gate items and this is not one.

What moved this round is real and I want it recorded before the holds.
**R366 and R367 are closed, and I reproduced both in a clean clone, in both
directions.** CP1 is the first version of that rule whose justification I
could not refute with a command, and the reason is structural rather than
lucky: the cell is a test on a synthetic history, so the next version has to
survive it before it ships. That is the right shape and it should be the
template for everything here. **R365 repair is the best of the three
attempts** -- a round trip really does cover a field nobody has added yet, and
because `unicode_escape` encoding is injective, `src` is genuinely pinned to
the bytes. **CP4 closed a species and the closure HELD on nine spellings its
author had not seen**, which is the first time in five batches that has
happened. CI is green at the reviewed commit. `floatfea/` is byte-identical
for the eighteenth round.

**What holds is one door with two more leaves, one red test, and three
published sentences a command refutes.**

1. **R375 -- the fourth leaf, and it costs nothing.** Thirteen lines under a
   CRLF comment redirect `CORPUS`; both readers follow it; the whole suite is
   **2073 passed, 0 failed**, the clean tree own number, with a real scanner
   regression planted and the corpus file untouched. "Readers that share
   nothing but the path" is the sentence, and the path is one line.
2. **R376 -- the fifth leaf, in the code verdict 42 already named.** A
   three-line special case in `_planted_caught` moves an entry out of the
   asserted set: **76 passed**, same regression planted.
3. **R377 -- a red test at the commit BE3 requires me to make**, isolated by
   one variable, red in CI at `c85511b` in the run this round mined, and named
   nowhere. `_report_anchor()` falls back to HEAD and takes rule 2 with it.
4. **R378, R379, R380 -- three `out` blocks that are not what their commands
   print**: five commits pasted where six print, two sites pasted where four
   print, and "the comparison table is gone" where one grep finds it. All
   three are in the revision that records CP2, and CP2 is the rule they break.

**On R375 and R376 I would take the paragraph over the mechanism.** Four
rounds have each shut the leaf they were shown and published a sentence
claiming the door. A fifth mechanism will have a sixth leaf. What has not been
tried is a docstring that says where the reach ends and stops there. If a
mechanism is preferred for R375, the tracked blob is the one anchor in this
repository the implementer cannot write from a working tree, and the file
already shells out to git eight lines below.

**And one thing that is not step 5 and should not be lost.** Four undeclared
tolerances sit in `floatfea/io/`, three of them deciding whether a load record
is rejected, one of them absolute on a dimensional quantity, all four there
since F1 and all four invisible to the guard whose first line forbids them.
R379 blocks on the published sentence only. The values need a plan row -- 4a
or a step of their own -- and somebody should write it before the milestone
closes, because "a wrong answer that looks right" is what that reader exists
to prevent.

**Not gates on step 5, into the next report Carried section:** R381, R382,
R383, R384, R370, R371, R372, R373, R374, R362, R363, R364, R354, R355, R356,
R357, R347, R348, R349, R350 second half, R330, R331, R332, the section 9
status-versus-subject disagreement, R321, R322, R300, R291, R292, R281, R231,
R244, R245, R275, R223, R224, R230, R261, the underlying gap in R276, R277,
R262, R264, R266, the two R248 residues, R249-R252, R225-R228, R232, R233,
and everything already at 4a.

**Adversarial corpus (BE3): 29 new entries in one file, all unseen by the
implementer, every `measured=` taken at `17bd759` by running the shipped
`offending()` BEFORE the `expect=` beside it was written, and every line
round-tripped through the corpus escape AND through the guard own
re-serialisation before it was measured.**

**The coverage measurement, stated plainly: of my 29 new entries the shipped
scanner does what the entry requires on 18, and 11 are misses. Of the 21
entries that ask for DETECTION, 11 are correct and 10 are missed.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+29 (196 to 225), 18
  correct.** `python scripts/corpus_figures.py` reads `225 225 89 136 37`, and
  `tests/test_marker_exemption_corpus.py` is **95 passed** at my corpus commit
  against 77 at `17bd759`.
* **THE RATIO MOVED, AND CP4 IS WHY.** Four batches running it sat at one
  third. It is 11 of 21 now, and the nine entries that moved it are all one
  species: `10 ** -9`, `1e-3 / 1e6`, `1 - 0.9999999999`,
  `(1 + 1) / 2000000000`, inside `abs()`, mid chained-compare, in
  `approx(abs=)`, in `isclose(atol=)`, and in a `while` header. **A species
  closed between rounds and the closure held on shapes its author had not
  seen.** That is the first evidence this milestone that the scanner is
  growing rather than being patched, and it is worth more than the misses.
* **THE STRING SPECIES IS `float(<constant>)` AND NOTHING ELSE.** Six
  spellings are clean: `float("1e-09".strip())`, `float(f"1e-09")`,
  `np.float64("1e-09")`, `float.fromhex("0x1p-30")`, `atol=float("1e-09")` as
  a keyword rather than a comparator, and `tol = float("1e-09")` bound to a
  name one line before use.
* **Two more axes**: a declared name scaled by an integer (R384), and a
  threshold reaching the comparison through a container, in both new species.
* **THE BOUNDARY IS PINNED FROM BOTH SIDES rather than sampled on one.**
  `fraction_of_span < 1 / 2` folds to 0.5 and is caught; `err < 1000 / 1000`
  folds to 1.0 and is clean. The decision rule own threshold is written down
  in data now, so a change that moves it cannot move it quietly.
* **One entry asks the scanner to report LESS**, and it is the only one of its
  kind in the file: `assert cost < float("inf")`. R381.
* **All three hatch controls pass, and they matter most**: the marker works on
  a folded constant, on a `float("...")`, and on a folded constant after
  `black` has split the call across five lines. A new rule the escape hatch
  does not reach makes a correct file unfixable, which is worse than any miss.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands.

**Forty-three rounds have found no element defect, and this round does not
either.** `floatfea/` is byte-identical for the eighteenth consecutive round
and its two CI jobs are green on a machine nobody here controls. It still
means "not yet contradicted": the determinism legs did not run at this commit,
ladder 5 has printed `OK -- 0 director(y|ies) ran` every time it has run, and
V5.1 against CalculiX is the witness that has not spoken.
