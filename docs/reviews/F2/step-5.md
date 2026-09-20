# Review � F2 step 5
Reviewed commit: 3ff6ceb41c85a055368aed07b811d9810216e8ed
Verdict: HOLD

**Reviewed commit: `d5d85ed`.** Report revision 23, `Answers: verdict 48 @
a0b2873`. The `Reviewed commit:` line stamped above by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus
commit -- not the commit judged. That is R373, still open; read `d5d85ed`.

Tests: **2516 passed, 0 failed, 0 skipped** at `d5d85ed` (my run, clean tree,
`python -m pytest -q`, 540.70 s, Python 3.13.15 on Windows). Reconciles with
the report: `python scripts/suite_count.py` at `d5d85ed` prints
`2172 passed ... excluding 344`, and `2172 + 344 = 2516`.

**Item 1b.** Revision 23 line 8383 reads `Answers: verdict 48 @ a0b2873`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`a0b2873e55660f004f3a56ab87467ee146ad9f82`. It is the latest. **Passes.**

**Commits judged: `c65b1bb`, `0e63448`, `1c94118` (plan, RE-LOCKED),
`4236848`, `e332f38`. Report `d5d85ed`.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit d5d85edc77bc73f2584e71bdfbc94148301470b3
out  run 35489487935, event push, conclusion SUCCESS, status completed
cmd  gh run view 35489487935 --json jobs
out  "the verification ladder"       success, 13 steps, 04:34:37 -> 04:37:27
     "lint, unit and guards"         success, 14 steps, 04:34:37 -> 04:44:27
     "CI determinism -- leg"         skipped, 0 steps
     "CI determinism -- ten legs"    skipped, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING.
     Not CK2: both ran real steps for minutes. The determinism pair is
     dispatch-only here and is recorded as an UNAVAILABLE check at this
     commit rather than skipped over.
cmd  gh run view 35487682884 --json jobs   -- this round's dispatch, at 4236848
out  ten "CI determinism -- leg (n)" success, "ten legs agree" success,
     "the verification ladder" success, "lint, unit and guards" FAILURE
cmd  gh run view 35487682884 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  13 rows, every one a report-or-figure staleness guard at a commit where
     revision 23 did not yet exist. Nothing in floatfea/, nothing in rung 1.
cmd  git diff --stat 4236848..HEAD -- tests/verification scripts .github
out  (empty) -- THE TEN EXECUTED LEGS DESCRIBE THE TREE UNDER REVIEW exactly.
     That is the strongest determinism evidence this step has had.
cmd  gh run list --limit 12, the two earlier pushes this round
out  35487290760 at 4236848 FAILURE, 35487102737 at 1c94118 FAILURE. Both are
     named with their conclusions in the report's 0a, as is the dispatch.
cmd  python -m black --check floatfea tests scripts ; python -m ruff check ...
out  90 files unchanged; all checks passed. `4236848` cleared it.
judge FOUR RUNS, FOUR CONCLUSIONS, ALL NAMED. R412's omission does not
     recur and the report leads with the conclusion rather than the table.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff a0b2873..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff a0b2873..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is being written by code in its own directory.
cmd  git diff a0b2873..d5d85ed -- floatfea/ | grep -E "^[+-][A-Z_]+.*Final"
out  (empty) -- NO CONSTANT MOVED. The 90/31 in tolerances.py is comments and
     two `# RETIRED-ALIAS:` declarations.
cmd  git show --stat on each of the five commits
out  `1c94118` touches docs/milestones/F2.md ALONE and says RE-LOCKED.
     `0e63448` and `e332f38` are the figure renders. `c65b1bb` is the code
     commit and carries the golden with a stated reason -- eight names added,
     none removed, and the rule is about removals. Clean separation.
```

## Carried

Verdict 48 held on R421-R428 and recorded R429-R433. **R421 through R428 are
all answered at the sites their conditions named, and R429 and R430 are
answered better than asked. R419, R431, R432 and R433 are correctly left open
and said so. What holds this step is seven NEW findings, and five of them are
again sentences written in the commit that repaired the same species
elsewhere.**

- **R421 -- ANSWERED at all four named sites.** `:51` states the two halves;
  `:136` reads "a residual and a bound"; `:212` is past tense under a
  retirement note; `:1505` reads "(residual, and no seventh)". **Closed.** A
  FIFTH site, outside the condition and outside the new guard's roots, still
  says the retired thing: R437.
- **R422 -- ANSWERED.** `F2.md:1918-1927` names the uniform elastic
  foundation as the retired first attempt, "Both counters" is gone, and
  `tolerances.py:525-530` records it as an alias of the retired gap counter.
  **Closed.**
- **R423 -- ANSWERED at both named sites.** `grep -n "1\.248\|6\.237"
  docs/milestones/F2.md` returns nothing and the plan points at the entry
  that types them; `count(... "seventeen")` is 0 in the test file.
  **Closed.**
- **R424 -- ANSWERED.** `regen_figures.py:590-599` says what `grep -n
  "log=True"` prints, and carries the grep as a triple that runs. **Closed.**
- **R425 -- ANSWERED, and the distinction is the right one.** `:275-290`
  separates "the gate may not assert this" from "a control may", names
  `test_ONE_RELEASED_CONNECTION_gives_SEVEN`, and the plan says the same.
  **Closed.**
- **R426 -- ANSWERED by the better of the two branches.**
  `rigid_mode_mechanism_ceiling` is a figure, floor-class below the bound,
  rendered beside `rigid_mode_largest_rigid_eigenvalue`. **Closed.** And the
  implementer's correction is right and I confirm it: rendered together the
  six bind on both machines (`1.2727` vs `0.9606` canonical; `1.4614` vs
  `1.3750` here), and the reversal I reported came from my mixed comparison.
  **That is my error, corrected by a measurement, and it is recorded as
  mine.** What the shared render does NOT settle is R438.
- **R427 -- ANSWERED.** `rigid_mode_corpus_refused` is `derived`, and the
  partition ships as `88` decided-clear, `25` refused-clear, `13` in the
  window with all thirteen named. My six window frames are all in that list.
  **Closed.** The sentence sixteen lines below it is R439.
- **R428 -- ANSWERED.** `_floor("rigid_mode_seventh_orders", "derived",
  log=True)`. **Closed.** Four marks against retired ceilings that the
  condition did not name are R445.
- **R429 -- ANSWERED, and I re-measured rather than read it.** All seven of
  my shapes are refused by `runs_without_a_conclusion` at this commit and
  both allow-shapes are allowed. **7 of 7, up from 2 of 7. Closed.** The
  other half of the rewrite is R444.
- **R430 -- ANSWERED.** `a_green_table_under_a_failed_run` is a function with
  five states, one of them a failed run whose every job reads green. It can
  fail now. **Closed.**
- **R419 -- OPEN, correctly, and not claimed.** 4a.
- **R431, R432, R433 -- OPEN, correctly listed and not touched.** R431's
  arithmetic reconciles at this commit (`2172 + 344 = 2516`, my run), so what
  is left of it is the sentence about what the exclusion counts, which still
  names three files while a fourth grows with the revision. 4a.
- **R411 -- OPEN, SEVENTH ROUND.** Revision 23's second line reads "Commits
  since the forty-eighth verdict, listed in §10"; §10 is `Carried` and the
  commit list is in §11. Unchanged from last round. 4a.
- **R383 -- ADVANCED FURTHEST IT HAS.** Ten legs executed and agreed at
  `4236848`, and `git diff 4236848..HEAD -- tests/verification scripts
  .github` is empty, so their result describes the tree under review.
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
  carried.** The section 9 status-versus-subject disagreement stays at 4a.
- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250,
  R251, R226, R227, R264 and R266 still have no row; R348 territory, unmoved.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394-R399, R403-R409, R412, R415-R418, R420, R388 -- closed
  earlier**, not reopened.

## Findings

**First, what is right, and it is again the larger part.**

**THE GATE STILL HOLDS AND I ATTACKED THE NEW FIGURE HARD.** 858
configurations at `subdiv=1` over the corpus's own 22 unit strings and 39
span strings, one torsional release, nothing else moved: 350 of them are a
genuine seventh zero mode, and **0 of 350 escape the bound.** Rung 1 is green
on Linux and on Windows, `floatfea/` carries no executable change for the
fifth round, and the plan is RE-LOCKED in its own commit. `e332f38` is the
best commit in this round: it publishes a canonical render AND names the
sentence that render refuted on the way in, in the commit message, with both
numbers. That is the discipline working without a reviewer in the loop.

**And CV0 is the right instrument.** A guard that evaluates a prose triple is
a real advance, the `eval` surface is closed properly (parsed, four names,
string literals only), the annotation-strip bug was found by its own author,
and the cost is written down. Nothing below argues against the mechanism.
What is below is that **the first nine triples it certifies include two it
certifies falsely**, and that is worth saying precisely because the
mechanism is good.

---

**R434. (BLOCKS -- a `claim:` beside a `cmd:` that CANNOT FAIL. The claim is
false in both halves; the command searches for a string that does not occur
and cannot occur, so `out: none` is what it prints whatever the tree does. A
gate carries its own failure.)** `floatfea/tolerances.py:548-551`.

```
code :548 "claim: one test file mentions this ceiling, and it is the
     :549         diagnostic that prints it -- no assertion anywhere
     :550         compares against it"
     :550 "cmd:   files(tests/**/*.py, RIGID_BODY_MODE_RATIO<RPAREN>)"
     :551 "out:   none"
cmd  the SAME call with the trailing right-paren removed from the needle
out  tests/test_no_tolerance_literals.py,
     tests/verification/rung1/test_rigid_body_corpus.py,
     tests/verification/rung1/test_rigid_body_modes.py
     -- THREE FILES, not one. The needle as written matches nothing in the
     repository, because no site spells the name followed by a right paren.
code tests/verification/rung1/test_rigid_body_corpus.py:247
     `if ratio > RIGID_BODY_MODE_RATIO:` ... :259 `assert over, (...)`
cell MY OWN ABLATION, one variable moved: over all 126 corpus frames the
     largest `mode_ratio` is `0.9141` and the ceiling is `1e-12`, so 91
     frames populate `over`. Raise the ceiling past `0.9141` and `over` is
     empty and `:259` goes RED. THE ASSERTION'S TRUTH IS A FUNCTION OF THE
     RETIRED CONSTANT. "no assertion anywhere compares against it" is false.
judge AND THIS SENTENCE REPLACED "nothing asserts against it", which the new
     guard WOULD have flagged. The rewrite moved an absence claim into a
     `claim:` field where it is checked by a command that returns `none` for
     a needle that cannot occur. The entry now reads as certified and is
     wrong in both halves. My own verdict-48 grep missed the assert because
     I piped through `grep assert` and the assert is twelve lines below the
     comparison -- assertion domain blindness, and it is recorded as mine.
```

  **Closed when** the `cmd:` is a call whose result could differ if the claim
  were false -- the bare name, not the name plus a paren -- and the `claim:`
  says what that call prints, including that `test_rigid_body_corpus.py:259`
  asserts on a list built by comparing against this constant.

**R435. (BLOCKS -- the same shape, the same commit, one entry down.)**
`floatfea/tolerances.py:621-624`.

```
code :621 "claim: the retired subspace loss is named by one test file, which
     :622         prints it as a diagnostic, and by no assertion"
     :623 "cmd:   files(tests/**/*.py, RIGID_BODY_SUBSPACE_LOSS<RPAREN>)"
     :624 "out:   none"
cmd  the same call without the trailing right-paren
out  tests/verification/rung1/test_rigid_body_corpus.py,
     tests/verification/rung1/test_rigid_body_modes.py   -- TWO files
judge "by no assertion" is true here -- `loss_over` is printed only, and I
     checked. "named by one test file" is false, and the command beside it
     prints `none`, which is neither one nor two. A triple whose `out`
     denies its own `claim` is worse than a bare sentence: the bare sentence
     does not look checked.
```

  **Closed when** the `cmd:` is the bare name and the `claim:` says what it
  prints.

**R436. (BLOCKS -- two absence sentences refuted by their OWN function
bodies, both invisible to the guard this round added, both in docstrings the
round rewrote.)** `tests/verification/rung1/test_rigid_body_modes.py:566` and
`tests/verification/rung1/test_rigid_body_corpus.py:236-237`.

```
code modes.py:566  "Nothing is asserted against it."
code modes.py:596  `assert math.isfinite(ratio), (...)`  -- SAME FUNCTION,
     30 lines below, asserting on the very quantity the sentence is about
code corpus.py:236 "It is not asserted against anything -- that is what
                    retired means"
code corpus.py:259 `assert over, (...)`  -- SAME FUNCTION, 23 lines below,
     and `over` is built by `ratio > RIGID_BODY_MODE_RATIO` at :247
cmd  both paragraphs through the shipped `_ABSENCE` pattern
out  NEITHER MATCHES. The pattern knows `nothing asserts` and not `nothing
     is asserted`; it knows `referenced by nothing` and not `is not asserted
     against anything`.
judge THE ROUND EDITED BOTH FILES AND BOTH DOCSTRINGS. `c65b1bb` rewrote the
     docstring at modes.py:566's own function and left the sentence; it
     rewrote corpus.py's module docstring and left :236. CP2 exactly, for
     the third round running: the prose around the repair inherits none of
     the discipline applied to it.
```

  **Closed when** both sentences say what a grep prints -- or are deleted --
  and the two phrasings are in `_ABSENCE`.

**R437. (BLOCKS -- the VERIFICATION LADDER document, which `CLAUDE.md` §
Testing names as the ordering authority, still defines V1.1 and G2.1 as the
retired eigenvalue ratio, in the present tense. R421 fixed the plan's four
sites; this is the fifth, and it is outside the new guard's roots.)**
`docs/verification/README.md:16-18`.

```
code :16 "**V1.1 Rigid-body modes.** An unconstrained model has exactly six
     :17  zero-energy modes. Test the eigenvalue ratio against the first
     :18  flexible mode, not an absolute value, so the test is mesh- and
          unit-independent. *Gate G2.1.*"
cmd  the shipped RETIRED-ALIAS predicate, applied to this file
out  MATCHES the declared alias `eigenvalue ratio`, and the paragraph does
     not say retired -- it WOULD FAIL the guard. The guard never opens the
     file: ROOTS is ("floatfea", "tests", "scripts", "docs/milestones").
cmd  grep -rn "eigenvalue ratio" docs/verification/
out  one hit, this one
judge A READER FOLLOWING `CLAUDE.md` TO THE LADDER IS TOLD G2.1 IS A RATIO.
     This is not prose precision and it is not 4a: it is the same sentence
     R421 blocked on, in the one document the ladder's ordering is defined
     in. The round declared the alias, built the detector, and pointed it at
     four roots that exclude the document.
```

  **Closed when** `:16-18` states the residual-and-bound form, and the
  guard's roots either include `docs/verification/` or the file says at its
  head why it is out of scope.

**R438. (BLOCKS -- `rigid_mode_mechanism_ceiling` is published, enforced and
quoted as one of the two lower candidates for `RIGID_MODE_BOUND` under a
sentence claiming a coverage the cell does not have; over the set the
sentence names the figure is not the maximum, and the round's own conclusion
about which candidate binds reverses.)** `floatfea/tolerances.py:369-371`
and `scripts/regen_figures.py:127-129`.

```
code tolerances.py:369 "a genuine seventh zero mode: one torsional release
     :370                re-expressed over EVERY UNIT SYSTEM AND SPAN THE
     :371                CORPUS USES, refused at all of them, reaching
                         {{fig:rigid_mode_mechanism_ceiling}} units at the
                         highest"
code regen_figures.py:127 "The cell is one torsional release re-expressed:
                           every unit system and span the corpus uses,
                           nothing else moved."
code the cell as shipped: 7 units x 5 spans, `subdiv` forced to "1"
cmd  the corpus's own distinct values
out  19 distinct unit VALUES (22 strings) and 31 distinct span VALUES (39
     strings), and 10 distinct subdivisions. The cell covers 6 of the 19
     units and 5 of the 31 spans, and one of its seven units -- `1e-2` --
     IS NOT A UNIT THE CORPUS USES.
cell MY SWEEP, over the set the sentence names: 22 unit strings x 39 span
     strings at subdiv=1, one torsional release, nothing else moved. 858
     configurations, 350 of them a genuine seventh zero mode
     (`zero_modes_under_the_bound == 7`).
out  0 of 350 escape the bound -- THE GATE HOLDS, and that is the important
     half. But the HIGHEST `lambda_7` among them is **1.5243** units, at
     unit `1.0` with span `3600.0`, both of which the corpus uses. The cell
     renders **1.3750** on this same machine. The published figure is not
     the maximum of the set its own sentence names, and it is low by 1.109x.
judge AND THE CONSEQUENCE IS THE QUESTION CV1 WAS ASKED TO SETTLE.
     `rigid_mode_largest_rigid_eigenvalue` is 1.4614 here. Against the cell
     (1.3750) the six bind, which is what the entry and `e332f38`'s message
     conclude. Against the set the sentence claims (1.5243) THE MECHANISM
     BINDS. The correction to R426 is right about the cell, and the cell is
     not what the sentence says it is.
judge I ALSO CHECKED WHY subdiv IS PINNED, because the sentence does not say
     it is: at every `subdiv > 1` I tried,
     `_assemble_with_torsional_release(..., released=6)` leaves SIX under
     the bound, not seven -- the injection stops being a mechanism. Pinning
     it is CORRECT. Not saying so, in a sentence that claims the corpus's
     coverage, is not.
```

  **Closed when** the two sentences say what the cell is -- 7 units, 5 spans,
  `subdiv=1`, and why -- or the cell is widened to the set they claim and the
  figure is re-rendered. If it is widened, the entry's statement about which
  candidate binds is re-taken with it (BP0).

**R439. (BLOCKS -- one generator, THREE policies for a count in twenty
lines, and the sentence stating the rule is refuted by the row above it,
added in the same commit.)** `scripts/regen_figures.py:253-280`.

```
code :262 `_floor("rigid_mode_corpus_refused", "derived")`  -- a count,
          floor-class, published                                    (NEW)
code :273 `("retired_ratio_over_ceiling_on_corpus", "{ratio_over} of ...")`
          -- a count, EXACT row, published, untouched
code :278 "An exact row that disagrees between machines is staleness by Q8's
     :279  rule, and IT IS NOT FLOOR-CLASS EITHER -- A COUNT IS NOT A
     :280  MEASUREMENT AGAINST A TOLERANCE. It is left out"
judge THE STATED GROUND FOR WITHHOLDING THE LOSS COUNT IS REFUTED BY THE ROW
     SIXTEEN LINES ABOVE IT, written in the same commit. R427 was "one
     generator, two policies, six lines apart"; the repair made one of the
     two counts floor-class, left the sentence saying that cannot be done,
     and left the third count exact. If `derived` is right for the refusal
     count -- and I think it is -- then the reason the loss count is
     withheld has to be restated, and the same question has to be asked of
     `retired_ratio_over_ceiling_on_corpus`.
```

  **Closed when** `:278-280` states the rule the file actually follows, and
  `retired_ratio_over_ceiling_on_corpus` is classed by that rule.

**R440. (BLOCKS -- a sentence added this round says a change to the
reviewer's corpus "shows up as a disagreement". Nothing in the repository
reads that file.)** `tests/test_report_carried.py:1033-1039`.

```
code :1037 "The corpus is the reviewer's and is not imported -- these are the
     :1038  paragraphs it specifies, written out, SO A CHANGE TO EITHER ONE
     :1039  SHOWS UP AS A DISAGREEMENT."
cmd  grep -rn "report_ci_section" tests/ --include=*.py
out  three hits, all comments: :919, :1034, :1081. NO READ.
judge THE SHAPES ARE TRANSCRIBED, NOT LINKED. `tests/test_marker_exemption_
     corpus.py` and `tests/verification/rung1/test_corpus_configurations.py`
     both read their corpus file; this one does not, and the sentence claims
     the property those two have. Same species as R424 -- a correct
     mechanism described by a sentence one grep refutes -- in the file this
     round rewrote.
```

  **Closed when** the sentence says the shapes are transcribed and unlinked,
  or the ids are read from the corpus file so the disagreement it promises
  can occur.

---

**Recorded, and lock items for step 4a (BU0). None of these touches the gate
assertion, a tolerance, or the truth of a published figure.**

**R441. The CV0 absence detector catches 0 of 20 unseen phrasings, and seven
of the twenty are sentences already in the tree.** Measured against the
shipped `_ABSENCE` predicate; the entries are in
`tests/corpus/tree_prose_claims.txt`. The three controls -- the author's own
phrasings -- are all caught. The misses include `nothing is asserted`,
`asserted nowhere`, `never asserted`, `no assertion anywhere`, `read by
nothing`, `not registered anywhere`, `is unused`, and `no such injection
exists` (written this round at `F2.md:1920`). A probe over the guard's own
roots finds **21 absence-shaped paragraphs it does not match, against the 13
it does**.

**R442. The RETIRED-ALIAS detector is 3 of 8, and its domain has four
holes.** A fenced block in markdown, an assertion message in Python, a
hyphenated alias, a blank line inside the phrase, and the word `retired`
about a different quantity in the same paragraph all pass. Scope: `.py` and
`.md` only; `ROOTS` excludes `docs/verification/` (R437) and everything
outside those four; and `floatfea/tolerances.py` is skipped WHOLESALE rather
than only at its retirement entries, so a present-tense alias anywhere in the
1400-line file that declares the aliases is invisible.

**R443. Two vocabulary holes, both measured.** (a) A glob that matches no
file returns `none` from `files()` and `0` from `count()`, silently -- so a
triple can certify an absence with a pattern that reaches nothing. AM5 says
an empty parameter set is an error and not a skip, and this is that rule
inside the new guard. (b) The annotation strip removes any line matching
`^\s*(?:#\s*)?(?:claim|cmd|out):`, which includes a Python variable
annotation named `out`: `count("tests/test_tree_prose_consistent.py",
"list[tuple[int, str]]")` returns **5** where the file has **6**.

**R444. CV3 closed one hole in `_CONCLUSION` and opened another; 3 of 12
unseen shapes refused.** `tests/corpus/report_ci_section.txt`, twelve new
entries. The regex now matches a bare conclusion VALUE anywhere in the
paragraph, so a value inside a `--jq 'select(.conclusion=="success")'`,
inside `grep -c failure`, inside "was not a failure", or in an unrelated "the
legs were skipped" all satisfy it. One false positive in the other
direction: `100,200,300,400` is joined by the thousands strip into a
twelve-digit run id and the paragraph is then required to carry a conclusion.

**R445. Four `_floor(...)` marks still decide a figure against a RETIRED
ceiling.** `scripts/regen_figures.py:77, 83, 291, 297` --
`rigid_body_mode_ratio` and `rigid_body_counter_ratio` against
`RIGID_BODY_MODE_RATIO`, `rigid_body_subspace_loss` and
`rigid_body_counter_loss` against `RIGID_BODY_SUBSPACE_LOSS`, both retired at
Q7/CS2. R428's species at four sites its condition did not name, and R399
asked for the general form two rounds ago.

**R446. One `_ABSENCE_EXEMPT` row describes its own sentence wrongly.**
`("tests/verification/rung1/test_corpus_configurations.py", "nothing
asserts")`, reason "the sentence says the curve may not be asserted on, not
that no assertion exists". The sentence at `:1590` reads "The fitted curve is
a DIAGNOSTIC and nothing asserts it" -- descriptive, not prescriptive, and it
is the exact conflation R425 was a finding about. The claim is TRUE today (I
checked: `fit` is printed and the function ends `assert True`) and nothing
would notice if it stopped being. The other six rows are honest policy
statements and I read all seven.

**R447. `rigid_mode_mechanism_ceiling` is the tightest floor-class row in the
file and the entry does not say so.** `scripts/regen_figures.py --check`
here prints `0.9606` committed against `1.3750` local, **spread 1.4314x**
against `FIGURE_FLOOR_CLASS_SPREAD = 1.5` -- `1.048x` of margin. Every other
floor-class row on this machine is at or under `1.1483x`. A fourth machine
reddens the build on this row before it reddens on anything else.

**R448. `derived` drops the denominator.** `rigid_mode_corpus_refused`
renders `"33 of 126"`, and `compare()`'s numeric branch reads only the
LEADING number for a floor-class row. Off the canonical machine the `126` is
compared by nothing. `counter_defect_boundary` uses kind `words` for exactly
this reason.

## Tolerances touched

**NONE. No constant was created, retired, or moved.**

```
cmd  git diff a0b2873..d5d85ed -- floatfea/ | grep -E "^[+-][A-Z_]+.*Final"
out  (empty)
cmd  git diff --stat a0b2873..d5d85ed -- floatfea/
out  floatfea/tolerances.py | 90 insertions, 31 deletions -- ONE FILE, and
     every line of it a comment or a `# RETIRED-ALIAS:` declaration
judge NO VALUE WAS WIDENED AND NO VALUE MOVED. What changed in that file is
     prose: R416's clause, R423's numbers, R426's two candidates, R427's
     window, and two aliases. Two of those prose changes are R434 and R435
     and one is R438, which is why this step holds -- but not one of them
     moves a threshold or a decision.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2516 passed at d5d85ed -- no undeclared literal entered tests/ this
     round and nothing was added to `tolerance_marker_exemptions.txt`.
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**CV0 is the right answer to the forty-eighth verdict and I want that on the
record before the list.** A guard that runs a prose triple is worth more than
eight repairs; the `eval` surface is closed properly; the annotation-strip
defect was found by its own author; and `e332f38` shows the discipline
working unprompted -- a canonical render that refuted a sentence two commits
old, with the refutation in the commit message and both numbers beside it.
Three of the implementer's own claims were refuted by running them this round
and all three are in the report. **The fourth is R434, and it is inside the
sentence the new guard certifies.**

**What holds is seven items.**

1. **R434 -- a triple whose command cannot fail**, beside a claim that is
   false in both halves. `tolerances.py:548`. The needle carries a right
   paren that occurs nowhere, so `out: none` is printed whatever the tree
   does, and `assert over` at `test_rigid_body_corpus.py:259` compares
   against the constant the claim says nothing compares against. My own
   verdict-48 grep missed that assert; the ablation is in the finding.
2. **R435 -- the same shape one entry down**, `tolerances.py:621`.
3. **R436 -- two absence sentences refuted by their own function bodies**,
   `modes.py:566` against `:596` and `corpus.py:236` against `:259`, both in
   docstrings this round rewrote, both invisible to the new pattern.
4. **R437 -- the ladder document still defines V1.1 and G2.1 as the retired
   eigenvalue ratio**, `docs/verification/README.md:16-18`, outside the
   guard's roots and inside what `CLAUDE.md` § Testing points at.
5. **R438 -- "every unit system and span the corpus uses" is 6 of 19 units
   and 5 of 31 spans**, and over the set the sentence names the mechanism
   reaches `1.5243` here against the cell's `1.3750` -- which puts it ABOVE
   the six (`1.4614`) and reverses the round's own conclusion about which
   candidate binds. The gate is NOT breached: 0 of 350 mechanisms escape.
6. **R439 -- three policies for a count in twenty lines**, with the sentence
   stating the rule refuted by the row sixteen lines above it.
7. **R440 -- "a change to either one shows up as a disagreement"**, with
   nothing in the repository reading the file.

**The finding behind the findings, third round running.** Five of these seven
are sentences written in the commit that repaired the same species elsewhere,
and two of the five are inside the mechanism built to stop it. CP2 named the
species and CV0 now enforces it for three phrasings; **the species survives
because the enforcement is a keyword list and the defect is not.** R441-R443
are the measurement of that. The answer is not a longer list -- it is that a
`claim:` is read by a human against its `cmd:` before either is believed,
exactly as the guard's own docstring already says. Two of the first nine
triples in this repository fail that reading, and both were written by the
hand that wrote the rule.

**Adversarial corpus (BE3): 51 new entries across two files, all unseen by
the implementer, committed separately.**

**`tests/corpus/tree_prose_claims.txt`, NEW, 39 entries. The shipped guard
rules correctly on 6, and all six are controls written in the author's own
phrasing.** Twenty unseen absence phrasings: **0 of 20**. Eight alias
shapes: **3 of 8**. Five vocabulary shapes and three scope shapes: **0 of
8**. Seven of the twenty absence phrasings are sentences already in the
tree, and three of those became R436, R440 and R441.

**`tests/corpus/report_ci_section.txt`, 11 to 23. Twelve entries, and the
implementer's check caught 3 -- one of which is a false positive.** The seven
shapes from last round are re-measured here at **7 of 7 refused**, which is
the CV3 claim and it holds. The twelve new ones measure the other half of the
rewrite: four of them are the R412 shape surviving one level up, inside a jq
filter, a grep needle, a negation, or an unrelated `skipped`.

```
cmd  python -m pytest tests/ -q --ignore=tests/verification   (after my adds)
out  1113 passed -- the corpus files are data and break nothing
```

**Not gates on step 5, into the next report's Carried section:** R441, R442,
R443, R444, R445, R446, R447, R448, R419, R431, R432, R433, R410, R411, R413,
R414, R400, R401, R402, R390, R391, R392, R393, R383, R370, R371, R372, R373,
R374, R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350 second
half, R330, R331, R332, the section 9 status-versus-subject disagreement,
R321, R322, R300, R291, R292, R281, R231, R244, R245, R275, R230, R261, the
underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a. **R421, R422,
R423, R424, R425, R426, R427, R428, R429 and R430 are closed.** R411 is
unchanged and stays open. R426 closed and reopens in substance as R438; R427
closed and reopens as R439; R428 closed and reopens at four unnamed sites as
R445.

**Forty-nine rounds have found no element defect and this round found none
either.** 858 mechanism configurations, 350 genuine seventh zero modes, zero
escapes; 126 corpus frames with the residual green at all of them; ten
determinism legs executed on a tree byte-identical to the one under review in
`tests/verification`, `scripts` and `.github`. It still means "not yet
contradicted": ladder 5 has printed `OK -- 0 directories ran` every time it
has run, and V5.1 against CalculiX is the witness that has not spoken.
