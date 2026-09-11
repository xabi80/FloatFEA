# Review — F2 step 5
Reviewed commit: 30de97a053d29ae9f58d07ed90fe01c170165230
Verdict: HOLD

**Reviewed commit: `b1cfceb`.** Report revision 15, `Answers: verdict 40 @ 8ee69b7`.

Tests: **2030 passed, 2 failed, 0 skipped** (my run at `b1cfceb` on a clean
tree, `python -m pytest -q`, 490.90 s, Python 3.13.15 on Windows).
`pytest --collect-only` gives **2032**, so nothing is skipped and nothing
silently uncollected. The two failures are the two section 7 names, both
behind the canonical re-render, both mine from earlier corpus rounds.

**Commits: code `ca57d8a`, `11e2606`, `0a6a608`; `process:` `52e956f`.
Report `b1cfceb`.**

**Item 1b.** The newest revision's header at line 5135 reads
`Answers: verdict 40 @ 8ee69b7`; the last commit touching the verdict file is
`8ee69b7e8b08fb89febb7db593b5e7336ce3090a`. It is the latest. **Passes.**

**CI, item 3b, AT THE COMMIT I AM REVIEWING -- `b1cfceb`, NOT `a93d505`:
`unavailable -- allowance exhausted`, the CK2 third state.**

```
cmd  gh run list --limit 10 --json headSha,conclusion,event,databaseId
out  34643760694  push  failure  @ b1cfceb   -- and no pull_request twin
cmd  gh api repos/.../actions/runs/34643760694/jobs
out  4 jobs. "lint, unit and guards" and "the verification ladder":
     conclusion failure, runner_name "", steps 0, started 20:21:15 and
     completed 20:21:17 -- two seconds.
     "CI determinism -- leg" and "-- ten legs agree": SKIPPED.
cmd  gh api .../check-runs/<id>/annotations  for both failures
out  "The job was not started because recent account payments have failed or
     your spending limit needs to be increased" -- both of them
judge CK2 THIRD STATE. Neither red nor green; nothing claimed from it in
     either direction, and it does not HOLD by itself.
cmd  gh api .../runs/34546580003/jobs   (the last run that EXECUTED, @ 8942cdc)
out  6 of 6 ladder jobs success; "guards and meta-tests" FAILURE
cmd  git diff --stat 8942cdc..b1cfceb -- tests/verification scripts .github
out  NOT empty. SO THAT RUN DOES NOT DESCRIBE THIS TREE. Recorded as
     unavailable.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

**AND paths-ignore BEHAVES AS CO3 CLAIMS, measured rather than read.**

```
cmd  gh api ".../actions/runs?head_sha=<40667c6>" --jq .total_count
out  0      -- my corpus commit created no run
cmd  the same for 2b6435d, last round's verdict commit
out  0
judge THE ONE THAT LOOKS LIKE A COUNTEREXAMPLE IS NOT ONE. `8ee69b7` touches
     only the verdict tree and DOES have a run (34635327297), because a push
     is evaluated over every commit it carries and that push carried
     `40667c6` too, at a commit where `tests/corpus/**` was not yet ignored.
     With CO3 in, the same push would be ignored entirely.
```

**My own instructions (4b) and the conftest pathspec (4c).**

```
cmd  git diff 8ee69b7..b1cfceb -- .claude docs/SUPERVISOR.md
out  (empty) -- no commit in this range touches either. Nothing to read.
cmd  git ls-files -- tests/conftest.py and the double-star form
out  tests/conftest.py
cmd  git diff 8ee69b7..b1cfceb -- the same two pathspecs
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
cmd  git diff 8ee69b7..b1cfceb -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 8ee69b7..b1cfceb -- floatfea
out  (empty) -- sixteen rounds now
```

**What held, reproduced at my run**: `ruff check floatfea tests scripts`
clean; `black --check` clean over 88 files; `mypy floatfea` clean over 25
source files; `pytest -q tests/verification/rung1` is **1053 passed**;
`python scripts/corpus_figures.py` prints `147 147 51 96 30`, the report's
section 3 table to the digit; the three report guards collect **218** at
`b1cfceb` and **261** at `52e956f`, and 1812 + 2 + 218 = 2032 = my collection
exactly, so section 7's pair is my pair.

## Carried

Verdict 40 listed three blocking items. **All three close at the words of
their conditions, and I checked each by running it rather than reading it.**
Two of the three repairs then produced new findings of their own -- one
because the door it shut has a second leaf, one because the sentence that
justifies it is refuted by a four-line measurement. That is R359 and R361
below, and neither is a reopening.

- **R351 -- CLOSED at every clause of its condition.** The comparison exists,
  it is a second reader, the floor is gone, and the three sentences are
  withdrawn. I reproduced the closing cell in a clean clone.

```
cmd  clean clone at b1cfceb, pytest tests/test_marker_exemption_corpus.py
out  57 passed
cell (a) the scanner narrowed -- ast.walk(inner) to ast.walk(inner.right)
out  2 failed, 55 passed. `detect_declared_raised_to_a_literal` named, and
     the regression test names it with its blame commit.
cell (a) PLUS (b), the drop line the finding used verbatim
out  1 failed, 55 passed -- and it is `test_every_entry_reaches_the_
     assertions`, `assert 146 == 147`. LAST ROUND THIS PAIR LEFT THE WHOLE
     SUITE GREEN. It does not now.
cmd  grep -n "len(ENTRIES) >= 28" tests/test_marker_exemption_corpus.py
out  (nothing) -- the floor is deleted, not widened
judge AND THE PARTITION CLAUSE IS NOT CEREMONY, WHICH I CHECKED BY BREAKING
     IT: a filter added to `ASSERTED` -- the obvious next place to drop a
     shape from -- gives `1 failed` at the same assertion. It cannot fail for
     any state of the CORPUS, which is worth knowing and is not a defect: it
     is a guard against the edit one level down, and it fires on that edit.
judge THE THREE SENTENCES ARE WITHDRAWN RATHER THAN DEFENDED, which is the
     better half of the repair. The fourth sentence that replaced two of
     them is R359.
```

- **R352 -- CLOSED at both halves, after four rounds.** The generator and the
  label, and I attacked the generator rather than reading it.

```
cmd  python scripts/ci_section.py deadbeef
out  the docstring, exit 2 -- a sha is REFUSED, not ignored
cmd  python scripts/ci_section.py, diffed against the published section 0
out  identical, line for line, including the heading and the `Generated:`
     line. Section 0 IS generated.
cmd  every line of revision 15 containing "reviewed commit", with its shas
out  six lines, and not one of them carries a sha. Two are withdrawals, one
     is the Q7 sentence, one is the Carried table quoting verdict 40's own
     subject, one is the new test's name.
judge THE HEADING IS TRUE WHENEVER IT IS READ: "CI at `a93d505`, the commit
     verdict 40 judged", and `a93d505` is the commit verdict 40 judged. The
     condition asked for one line either way; the third form chosen is
     better than either I offered.
judge AND THE BYTE-IDENTITY CHANGE IS THE LOAD-BEARING HALF. `startswith` in
     both directions accepted a carried-forward heading, which is the shape
     that actually happened four times.
```

- **R353 -- CLOSED at both of its named sites.** The `declared` line is now
  `sum(1 for ... if _planted_caught(expect, measured))`, the same decode as
  the rest of the file; the two docstring counts are withdrawn to the report
  rather than restated, which is the disjunct BP0 and BI3 both allow.
  `scripts/corpus_figures.py` reproduces `147 147 51 96 30` at my run, and
  the report publishes exactly that.

- **R358 -- ANSWERED as a rule change, and EVERY FIGURE IN SECTION 4
  REPRODUCES.** I re-ran the cell in a real clone with only the CO3 hunk
  applied, which is the correction the report makes about its own first
  attempt, and the correction is right.

```
cell at 40667c6, before CO3
out  9 failed, 224 passed
cell at 40667c6, git apply of the CO3 hunk alone and nothing else
out  233 passed          -- the report says "9 failed -> 233 passed"
cell at 8ee69b7, before / after the same hunk
out  9 failed, 224 passed  ->  1 failed, 232 passed, and the residual is
     `two_digit_step_number`, which is what the report says it is
cmd  pytest --collect-only -q on the three guard files at 52e956f
out  261 tests collected  -- section 7's exclusion count, exact
judge THE SELF-CORRECTION IS THE BEST THING IN THIS ROUND. A first cell that
     measured twelve against twelve and would have reported "nothing
     changed" was caught by its author, named in the report, and replaced.
     That is the ablation discipline working without being asked.
judge WHAT IS WRONG IS NOT THE NUMBERS. It is the sentence the numbers are
     attached to -- R361.
```

- **R354, R355, R356, R357 -- OPEN at 4a, correctly listed in section 5** and
  correctly rowed in section 8 with `no change`. R356 is R351's species in
  four more readers and R359 makes it larger, not smaller.

- **R347, R348, R349, R350 second half -- OPEN at 4a, correctly listed.**
  R349's other half is visible again: section 8 spends twenty-five identical
  rows on one finding. Loud rather than wrong, as recorded.

- **R330, R331, R332 -- OPEN at 4a, correctly listed.** R332 stands and I
  honoured it again: nothing reads `g21_rigid_body_frames.txt`, so I added
  nothing to it.

- **R231, R244, R245, R275 -- OPEN, still correctly declared blocked** on the
  canonical re-render. My run reproduces the block exactly: `regen_figures`
  moves five exact-class figures that are staleness (`exempt_total` 62 of 632
  becomes 65 of 656, `margin_dropped_flip` 6.264e+05x becomes 1217x) and nine
  floor-class figures that are this machine (`rigid_body_mode_ratio` 1.3356x,
  `clean_worst_ratio` 1.0784x). A render here fixes five and corrupts nine.
  **The block is real and the right call is the one taken.**

- **R223, R224, R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged
  and stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** The
  generated table still expands a range by its endpoints only, so R250, R251,
  R226, R227, R264 and R266 have no row; that is R348's territory and it has
  not moved.

## Findings

**R359. (BLOCKS -- my adversarial case passed when it should have failed, and
it refutes the sentence written to replace the one R351 withdrew) CO0 shut the
door on the DOMAIN and the same species walks in through the CLASSIFICATION
INPUT. `expect=` is supplied by `_entries()` exactly as `measured=` is, and
the second reader counts headers without reading either.**
`tests/test_marker_exemption_corpus.py:35-42`, `:111-132`, `:138-160`,
`:203-219`.

```
code :36  "The CLASSIFICATION of an entry -- growth or regression -- is
     :38   derived from a field the implementer cannot write, and that holds."
code s1   "The CLASSIFICATION -- growth or regression -- is derived from a
           field only the reviewer writes, and that holds."
judge IT IS DERIVED FROM TWO FIELDS, NOT ONE. `_planted_caught(expect,
     measured)` is `_did_catch(measured) == (expect == "caught")`. Both
     arguments are handed over by `_entries()`, which is the implementer's.
     The reviewer writes them in the file; the parser decides what they are
     by the time anything compares them.
cell TWO EDITS, BOTH IN FILES THE IMPLEMENTER OWNS, IN A CLEAN CLONE AT
     b1cfceb:                                          (my run, b1cfceb)
     (a) ast.walk(inner) becomes ast.walk(inner.right) -- the same genuine,
         plausible tightening verdict 40 used
     (d) THREE LINES in `_entries()`, phrased as a re-scoping:
             if "raised_to_a_literal" in got["id"]:  # re-scoped
                 got["expect"] = "exempt"
out  after (a) alone            2 failed  -- the mechanism works
     after (a) and (d), pytest tests/test_marker_exemption_corpus.py
                                 56 passed, NOTHING RED
     after (a) and (d), python -m pytest -q  (the whole suite, 471.93 s)
                                 2 failed, 2029 passed
                                 THE SAME TWO PRE-EXISTING FAILURES AS THE
                                 CLEAN TREE (2 failed, 2030 passed).
judge NO CORPUS EDIT. NO PROVENANCE STRING. The shape moves from `ASSERTED`
     into `PLANTED_ESCAPES` and is filed as allowed growth, which is the
     exact outcome R341 and R351 were each written to prevent.
judge AND THE NEW GUARD IS GREEN THROUGHOUT. `test_every_entry_reaches_the_
     assertions` compares 147 to 147 -- true, because no entry was dropped --
     and the partition holds, because the shape IS covered, on the wrong
     side. The second reader reads `^id=` and nothing else; it has no opinion
     about what the parser decided the other three fields were.
judge THE PASS COUNT DROPS BY EXACTLY ONE AGAIN, 2030 to 2029, and nothing
     looks at it -- the same signature R351 recorded, one round later.
judge THE SAME EDIT AGAINST `measured=` DOES THE SAME THING. Either field
     alone is enough; there is nothing special about `expect`.
judge WHAT IS NOT WRONG, AND I CHECKED IT: a GENERIC version of this edit is
     caught. Deriving `expect` from `measured` for every entry empties
     `PLANTED_ESCAPES`, and `test_the_growth_rule_reads_a_field_the_
     implementer_cannot_write` and `test_improvement_is_visible_and_needs_no_
     ceremony` both redden. It is the TARGETED flip that is invisible, which
     is also the one an adversary would write.
judge THIS IS NOT R351 REOPENED. R351's condition named the count comparison
     and the count comparison is there, correct, and red on the edit it was
     written for -- see Carried. This is the leaf of the door that condition
     did not name, and the sentence published as the remaining guarantee is
     what makes it a finding rather than a note.
```

**Closed when** the second reader reads the fields as well as the headers --
one regex over the same bytes yielding `(id, expect, measured)` per line, and
the parsed triples compared to it -- with a cell showing it red on a
one-field flip and green on the clean tree; **or** the two sentences are
reduced to what is true: that the classification is derived from two fields,
both of which the parser re-supplies, and that a targeted flip of either is
not detected. Either repair closes it, and which one is the implementer's
call; the sentences and the mechanism must agree.

**R360. (BLOCKS -- the figures in the cell that demonstrates R351's repair do
not reproduce at any commit in this round) Report section 1, and the same
block in `ca57d8a`'s commit message.**

```
code s1  "(a) scanner narrowed   3 failed -- the mechanism works, two shapes
          named, each blamed to the commit that planted it"
code s1  "(a) and (b) the drop   3 failed, and one of them is
          test_every_entry_reaches_the_assertions"
cmd  clean clone, (a) alone, pytest tests/test_marker_exemption_corpus.py,
     run at ca57d8a, 11e2606, 0a6a608, 52e956f and b1cfceb
out  2 failed, 55 passed  AT ALL FIVE, one shape named
     (detect_declared_raised_to_a_literal), not two
cmd  the same with ast.walk(inner.left) instead, in case the edit differed
out  2 failed, 55 passed
cmd  clean clone, (a) and (b) together, at b1cfceb
out  1 failed, 55 passed -- `test_every_entry_reaches_the_assertions`,
     `assert 146 == 147`
judge CLEAN 57 AND RESTORED 57 DO REPRODUCE, and so does the CONCLUSION: the
     pair that was green last round is red now, at the new assertion, by
     name. The repair works. The numbers published beside it are not the
     numbers the commands print.
judge WHY THIS IS NOT PEDANTRY, AND IT IS THE SAME REASON BF0 EXISTS. This
     cell is the whole evidence that the head item was repaired, in the round
     whose subject is a check whose domain was its own. A reader who runs it
     gets a different answer from the one printed, and the first thing they
     will doubt is the repair.
judge AND IT IS THE THIRD FIGURE THIS MILESTONE THAT WAS CORRECT SOMEWHERE
     AND PUBLISHED SOMEWHERE ELSE. R353 was two counts made stale by the next
     commit; this is a count that matches no commit in the range.
```

**Closed when** the four rows of that cell are re-run at the commit that
publishes them and carry what the command printed, in the report and in the
commit message's own quoted block -- or the rows are withdrawn and replaced
by the one statement that is true and sufficient: the pair is red at
`test_every_entry_reaches_the_assertions` and was green before CO0.

**R361. (BLOCKS -- a causal sentence in a shipped guard, refuted by one
command, and it is the sentence that licenses the exemption) CO3 exempts the
corpus tree from the distance rule on the ground that it changes nothing a
suite count describes. A corpus-only commit changes the collected suite by
four.** `tests/test_report_carried.py:1079-1085` and `:1132-1146`; report
section 4; commit message `52e956f`.

```
code :1080 "Neither carries code, so neither changes what a suite count
     :1081  describes."
code :1143 "A reviewer commit carries no code and changes nothing the count
     :1144  describes, so the count stays true across it."
cell ONE VARIABLE: the corpus commit `40667c6`, everything else held.
cmd  git show --name-only --format="" 40667c6
out  tests/corpus/tolerance_marker_exemptions.txt          -- and nothing else
cmd  pytest --collect-only -q, at a93d505 and at 40667c6   (my run, 2 clones)
out  2069 tests collected    ->    2073 tests collected
cmd  the same, on tests/test_marker_exemption_corpus.py alone
out  52 tests collected      ->    56 tests collected
judge THE CORPUS IS PARAMETRISATION DATA, NOT PROSE. `ASSERTED` is the
     parametrisation of `test_the_exemption_window_gives_the_required_
     verdict`, and it is built from the corpus file. Adding entries adds
     tests. My commit this round adds seven more.
judge SO THE RULE NOW ACCEPTS A WHOLE-SUITE LINE THAT IS STALE BY EXACTLY THE
     NUMBER OF CASES THE CORPUS ADDED, and the amount is unbounded: it is
     whatever I write next round. R319 exists to stop a count describing a
     tree nobody is reading, and this is a tree nobody is reading.
judge THE EXEMPTION IS RIGHT FOR THE OTHER TREE AND I CHECKED THAT TOO: the
     verdict tree is read by the report guards as TEXT, and those three files
     are excluded from the count line anyway, so a verdict commit genuinely
     moves nothing the line reports.
judge THE PROCESS CONTRADICTION CO3 FIXES IS REAL AND THE FIX IS THE RIGHT
     SHAPE. What is wrong is that the justification was reasoned rather than
     measured, and the measurement is one command. CLAUDE.md BG0: a causal
     sentence carries the cell that isolates it.
judge AND IT MEETS THE OTHER HALF OF ITS OWN COMMIT FROM THE OTHER SIDE.
     `tests/corpus/**` is now in `paths-ignore`, so the one class of commit
     that provably changes what CI collects is the class CI will not see. I
     wrote at verdict 40 that the distance-rule fix was the better of the
     two and that the corpus is the one thing a run should see; this
     measurement is why. The report says the tension was recorded -- it is
     not: the only mention of the change is section 4 announcing it, and
     nothing weighs it.
```

**Closed when** every place that sentence is written says what was measured:
that a corpus commit changes the collected suite by N (N = 4 at `40667c6`,
7 at mine) and that the exemption therefore accepts a count stale by N, with
the number on the record -- **and** the exemption is narrowed or the staleness
is bounded, either by restricting `_REVIEWER_TREES` to the verdict tree and
solving the corpus collision another way, or by counting distance in commits
that change the COLLECTED SET rather than in commits that touch files. The
`paths-ignore` half is closed by recording the trade in the report with this
measurement beside it, or by taking `tests/corpus/**` back out; leaving both
in with the ground now refuted is the one option that is not available.

**R362. (recordable, 4a) Two shipped files assemble the protected verdict
path from pieces, and neither says why.** `scripts/ci_section.py:71` and
`tests/test_report_carried.py:1082` both build the string by concatenating
three fragments. The same test file writes the plain literal at `:66` and at
`:189`, so this is new and local to this round's two commits.
`.claude/hooks/protect-reviews.sh` names exactly this shape in its own
LIMITATION paragraph -- a path assembled at runtime from pieces is not
caught. Nothing is dodged in effect: both uses are `git show` reads, and the
hook's comments are explicit that over-blocking a read is the expensive
direction, so a legitimate motive exists. It is unwritten, and an unexplained
split literal in front of a guard that matches on that literal is the kind of
thing a later reader has to guess at. One comment, or the plain string.

**R363. (recordable, 4a) Section 0 anchors on the previous verdict's judged
commit even when a newer run exists, and the docstring justifies a different
thing.** `scripts/ci_section.py:74-110`. The reason given is that a report
cannot describe the run its own push creates, which is true of HEAD and not
of `8ee69b7`: run `34635327297` at the verdict commit existed before revision
15 was written, and section 0 reports `34630780377` at `a93d505`. Both are
CK2, so nothing turns on it this round, and anchoring on the judged commit is
a defensible choice -- it is the commit the verdict is about. The docstring
should say that is the choice, rather than implying no later run is
available.

**R364. (recordable, 4a) The scanner's coverage is still two thirds unseen
axes, four batches running.** My 22 entries this round are 15 misses and 7
correct; the 15 arrive as derived growth with no line written, and CO0's
count check agrees at 169. That is the asymmetry working as designed. It is
also the fourth consecutive batch where a two-thirds miss rate came from axes
nobody had thought of, while the scanner's own planted list has not grown.
Not a defect in this step; recorded so 4a can decide whether a guard that
misses two thirds of every unseen batch is a guard or a sample.

## Tolerances touched

**None.** `git diff 8ee69b7..b1cfceb -- floatfea/tolerances.py` is empty, and
so is the diff over all of `floatfea/`.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| everything in `tolerances.py` | unchanged | -- | -- | the diff over the file is empty |
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (unchanged) | dimensionless, ULP of the channel's own amplitude | `3.0`, injected beyond the site's clean deviation | `docs/milestones/F2.md:1116-1152`, `tolerances.py:1024-1035` |

```
cmd  offending() over every *.py in tests/ and scripts/   (my run, b1cfceb)
out  0 files reported -- no undeclared literal entered the tree this round,
     and `scripts/corpus_figures.py` is new this round
judge NO NUMBER IN ANY OF THE FOUR COMMITS FUNCTIONS AS A TOLERANCE. The
     deleted `>= 28` was a floor on a count, not on a quantity, and deleting
     a floor is the opposite of widening one. `distance <= 1` is unchanged;
     what moved is the set of commits counted, which is R361.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** All three of verdict 40's
conditions close at their own words, and I verified each by running it: the
drop that was invisible last round is `1 failed` at a named assertion, the
generator refuses a sha and regenerates section 0 line for line, and the
superseded equality is gone. Section 4's numbers reproduce to the digit in a
real clone with only the CO3 hunk applied, including the residual, and the
report's correction of its own first measurement is the best piece of work in
the round. `floatfea/` is unchanged for the sixteenth round and rung 1 is
**1053 passed**.

**What holds is one door with a second leaf and two sentences that a command
refutes.**

1. **R359 -- the classification is derived from TWO fields and the parser
   supplies both.** Genuine scanner regression plus three lines in
   `_entries()`: whole suite `2 failed, 2029 passed`, the same two failures
   as the clean tree, the corpus untouched, the new count check green at
   147 == 147. The sentence written to replace the one R351 withdrew says
   this cannot happen.
2. **R360 -- the cell that demonstrates R351's repair prints 2 and 1 where
   the report publishes 3 and 3**, at all five commits of the round and for
   both spellings of the edit. The conclusion is right; the figures are not
   the ones the commands give.
3. **R361 -- "a reviewer commit changes nothing a suite count describes" is
   false for the corpus tree.** `40667c6` touches one data file and moves the
   collected suite from 2069 to 2073. The rule that exempts it, and the
   `paths-ignore` entry that hides it from CI, both rest on that sentence.

**CI at `b1cfceb` is `unavailable -- allowance exhausted`**, the CK2 third
state: four jobs, two never started with the billing annotation, two skipped.
Neither red nor green, nothing claimed from it, and it does not hold this step
by itself. The last run that executed, `34546580003` at `8942cdc`, no longer
describes this tree. None of the three items above waits on a runner.

**Not gates on step 5, into the next report's Carried section:** R362, R363,
R364, R354, R355, R356, R357, R347, R348, R349, R350's second half, R330,
R331, R332, the section 9 status-versus-subject disagreement, R321, R322,
R300, R291, R292, R281, R231/R244/R245/R275 behind the canonical render,
R223, R224, R230, R261, the underlying gap in R276, R277, R262, R264, R266,
the two R248 residues, R249-R252, R225-R228, R232, R233, and everything
already at 4a.

**Adversarial corpus (BE3): 22 new entries in one file, all unseen by the
implementer, every `measured=` taken at `b1cfceb` by running the shipped
`offending()` before the `expect=` beside it was written.**

**The coverage measurement, stated plainly: of my 22 new entries the shipped
scanner does what the entry requires on 7, and 15 are misses.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+22 (147 to 169), 7
  correct.** The largest axis is **the other test framework**: `unittest`'s
  assertion vocabulary carries no `Compare` node at all, and
  `assertAlmostEqual(places=9)`, `assertAlmostEqual(delta=1e-09)` and
  `assertLess(err, 1e-09)` are three of three misses. The same shape in
  numpy's testing API: `assert_allclose(a, b, 1e-09)` is a positional rtol,
  `assert_array_less(err, 1e-09)` is the bound itself, and
  `assert_approx_equal(significant=9)` spells a tolerance as an integer.
  `pytest.approx(want, 1e-09)` IS caught -- the same one-library asymmetry
  the last batch measured, now in a second library.
* **A convergence threshold is a tolerance by another name** per CLAUDE.md,
  and `root_scalar(f, x0=1.0, xtol=1e-09)` scans clean.
* **Four entries carry no float constant where the comparison is**:
  `float.fromhex("0x1p-30")`, `np.float64(1e-09)`, `10.0 * np.spacing(1.0)`
  and `err * 1_000_000_000 < 1`, which has no float literal anywhere.
* **Four more ways a number reaches a name**: a `@property`, a `defaultdict`
  factory, a class built by `type(...)`, and a `global` rebound in a setup
  function.
* **Both marker-direction controls pass and all three `expect=exempt`
  controls pass.** An upper-case marker does not exempt, a marker on the line
  below the statement does not exempt, and the hatch still works on an
  annotated local assignment, on the closing bracket of a chained method call
  and inside a parenthesised `and` clause. A hatch that stops working is
  worse than any miss, so the green on those three matters most.
* **WHAT MY CORPUS DOES TO THE SUITE THIS ROUND: it grows it, and that is the
  point of R361.** `tests/test_marker_exemption_corpus.py` is **64 passed** at
  my corpus commit against 57 at `b1cfceb`, and
  `python scripts/corpus_figures.py` reads `169 169 58 111 30`. Seven new
  collected cases, from a commit the distance rule now treats as changing
  nothing a suite count describes.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands: nothing
  reads it.

**Forty-one rounds have found no element defect, and this round does not
either.** `floatfea/` has been comment-only for sixteen. By the rule I am
bound by that still means "not yet contradicted", because V5.1 against
CalculiX has not run. What moved this round is that two doors shut properly
and one of them turned out to have two leaves -- which is what happens when a
finding is repaired at the site it named rather than at the species it
belongs to, and R356 already says the species is in four more readers.
