# Review — F2 step 5
Reviewed commit: 05390a59428978b84627ec0ff77b992c6c881534
Verdict: HOLD

**Reviewed commit: `ab698c0`.** Report revision 24, `Answers: verdict 49 @
ed67a7d`. The `Reviewed commit:` line stamped above by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus
commit `05390a5` -- not the commit judged. That is R373, still open; read
`ab698c0`.

Tests: **2537 passed, 0 failed, 0 skipped** at `ab698c0` (my run, clean tree,
`python -m pytest -q`, 563.14 s, Python 3.13.15 on Windows). Reconciles with
the report: at `1824b9a` the whole tree collects 2527 and the three excluded
files collect 358, so `2527 - 358 = 2169`, which is the report's line; the
report commit adds 10 tests, 5 of them in a fourth file (R431, below).

**Item 1b.** Revision 24 line 8810 reads `Answers: verdict 49 @ ed67a7d`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`ed67a7dec798be500806492bce7caed4b5a037a4`. It is the latest. **Passes.**

**Commits judged: `f5268ee`, `7a6d796`, `75c73ea`, `3cde01b` (plan,
RE-LOCKED), `7895944` (`process:`), `1824b9a`. Report `ab698c0`.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit ab698c0db344d07a3d0433c77b1ac426dcfc73eb
out  run 35548152088, event push, conclusion SUCCESS, status completed
cmd  gh run view 35548152088 --json jobs
out  "lint, unit and guards"        success, 14 steps, 00:34:57 -> 00:44:28
     "the verification ladder"      success, 13 steps, 00:34:57 -> 00:37:35
     "CI determinism -- leg"        skipped, 0 steps
     "CI determinism -- ten legs"   skipped, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I JUDGE. Not
     CK2: both ran real steps for minutes. The determinism pair is
     dispatch-only here and is recorded as an UNAVAILABLE check at this
     commit rather than skipped over.
cmd  gh run view 35545894507 --json jobs   -- this round's dispatch, at 7895944
out  ten "CI determinism -- leg (n)" success, "ten legs agree" success,
     "the verification ladder" success, "lint, unit and guards" FAILURE
cmd  gh run view 35545894507 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  13 rows, every one a report-or-figure staleness guard at a commit where
     revision 24 did not yet exist. Nothing in floatfea/, nothing in rung 1.
cmd  git diff --stat 7895944..HEAD -- tests/verification scripts .github
out  scripts/regen_figures.py | 16 +, 1 -   -- NOT empty this round. The ten
     executed legs describe the tree in `tests/verification` and `.github`
     exactly, and NOT `scripts/regen_figures.py`, which `1824b9a` moved
     after them. R383 is weaker than last round, where the diff was empty;
     recorded rather than glossed.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git log --oneline ed67a7d..HEAD -- .claude docs/SUPERVISOR.md
out  7895944 process: prose in the source tree does not claim things about
     the code (CW0, CW1)   -- ONE commit, and it is standalone
cmd  git show --stat 7895944
out  CLAUDE.md | 21 +++, docs/SUPERVISOR.md | 14 +++, 35 insertions(+), 0
     deletions. Nothing under floatfea/ or tests/ in it. The message cites
     CW0 and CW1 and quotes the rule it is obeying.
judge NO STOP-CLASS FINDING. Additive, zero deletions, no guard removed --
     I read all 35 lines. `.claude/` itself did not move.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff ed67a7d..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is being written by code in its own directory.
cmd  git diff ed67a7d..HEAD -- floatfea/tolerances.py | grep -E "^[+-][A-Z_]+.*Final"
out  (empty) -- NO CONSTANT MOVED. The 72 changed lines in that file are
     comments and two rewritten triples.
```

## Carried

Verdict 49 held on R434-R440 and recorded R441-R448. **R434, R435, R436,
R437, R440 and R444 are answered at the sites their conditions named. R438
is answered better than asked and I re-measured it independently. R439 is
answered as asked and its own repair reopens as R454. R447 is correctly left
open, and the SENTENCE the report uses to leave it open is false in both
halves (R453) -- and half of R447 as I wrote it was wrong, recorded below as
mine.** What holds this step is six new findings, and five of them are again
sentences written in the commit that repaired the same species elsewhere.

- **R434 -- ANSWERED, and the repair is the right one.** `tolerances.py:554`
  now says three files name the ceiling and names
  `test_the_RETIRED_ratio_is_why_the_form_changed` as the one that asserts;
  `cmd` is the bare name and returns exactly the three files, which I ran.
  The assertion at `test_rigid_body_corpus.py:269` is declared as the
  retirement's own evidence in the entry AND in both docstrings that denied
  it. **Closed.**
- **R435 -- ANSWERED.** `tolerances.py:639`: two files, neither asserts, and
  the entry adds the honest half -- nothing would notice if the evidence
  disappeared, unlike the ratio. `cmd` returns the two. **Closed.**
- **R436 -- ANSWERED at both sites.** `modes.py:566` now says the quantity is
  asserted FINITE thirty lines below and names the refutation;
  `corpus.py:236` moved into the function docstring and says the assert is
  twenty-three lines below it. **Closed.**
- **R437 -- ANSWERED.** `docs/verification/README.md:16-24` states the two
  halves, the undecidable outcome, and quotes the ratio as retired with a
  pointer to F2.md. `ROOTS` now includes `docs/verification/` and
  `EXTRA_FILES` includes `CLAUDE.md`. **Closed.**
- **R438 -- ANSWERED, AND I RE-MEASURED IT RATHER THAN READ IT.** The cell is
  now every distinct `unit` crossed with every distinct `stretch` in the
  corpus, 22 x 39 = 858 -- the same set my own sweep used last round -- and
  it renders `1.5243` here, matching my independent figure to four digits.
  `subdiv=1` is pinned WITH its reason at the cell and in the entry. Both
  machines now put the mechanism above the six (`1.6519` vs `1.2727`
  canonical; `1.5243` vs `1.4614` here), so the reversal is real and the
  plan records it. **Closed.** See my widening attack in Findings.
- **R439 -- ANSWERED as asked, and the repair reopens one level up.**
  `:278-280` is gone; the rule is written once and both published counts are
  `words`. The ground for withholding the loss count changed from a refuted
  reason to a new one, and the new one is refuted too: **R454**.
- **R440 -- ANSWERED, and the mechanism works.**
  `test_every_corpus_shape_is_transcribed` reads `^id=` from the corpus and
  fails on anything not transcribed. **Confirmed by measurement: my 20 new
  entries turn it red.** **Closed.**
- **R444 -- ANSWERED, and measured.** 15 of my 20 unseen shapes ruled
  correctly, against 3 of 12 last round; all four R412-one-level-up shapes
  are refused. What survives is **R457**.
- **R441, R442 -- ANSWERED BY DELETION, and I endorse it.** See the first
  paragraph of Findings.
- **R443 -- ANSWERED on (a); (b) is the cause of R450.** The empty glob
  raises and has its own shipped test. The annotation fix is right for an
  annotated assignment and wrong for a needle containing `=`.
- **R445 -- ANSWERED.** All four rows are `derived`; no `_floor` call in
  `scripts/` names a retired ceiling. **Closed.**
- **R446 -- ANSWERED by deletion.** The `_ABSENCE_EXEMPT` table went with the
  detector. **Closed.**
- **R447 -- OPEN, correctly not claimed, and HALF OF IT WAS MY ERROR.** See
  R453: the item stands only as "a floor-class row sits close to
  `FIGURE_FLOOR_CLASS_SPREAD` and no entry says so", and the row is
  `rigid_body_mode_ratio`, not `rigid_mode_mechanism_ceiling`.
- **R448 -- ANSWERED.** `words` compares the word sequence and every number
  beside it, so `33 of 126` has both numbers checked. **Closed.**
- **R419 -- OPEN, correctly, and not claimed.** 4a.
- **R431 -- OPEN, and I can now name the fourth file.** The suite line says
  it excludes "3 files parametrised over this report"; a fourth is
  `tests/test_plan_figures.py`, whose
  `test_every_figure_reference_anywhere_resolves` gains one parameter per
  `{{fig:}}` reference in the report. Measured: 5 of the 10 tests the report
  commit adds are in that file. The arithmetic in the line is right; the
  sentence about what it counts is not. 4a.
- **R432, R433 -- OPEN, correctly listed and not touched.** 4a.
- **R411 -- OPEN, EIGHTH ROUND.** Revision 24's second line reads "Commits
  since the forty-ninth verdict, listed in section 10"; section 10 is
  `Carried` and the commit list is section 11. Unchanged. 4a.
- **R383 -- WEAKER THAN LAST ROUND, and the report does not say so.** Ten
  legs executed at `7895944`, then `1824b9a` changed
  `scripts/regen_figures.py`. Recorded, not blocking: the ladder at
  `ab698c0` is green and the change is to a generator, not to a rung.
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
  R251, R226, R227, R264 and R266 still have no row; R348 territory.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394-R399, R403-R409, R412, R415-R418, R420, R421-R430 --
  closed earlier**, not reopened.

## Findings

**First, what is right, and it is the larger part again.**

**THE CW1 DELETION IS THE CORRECT CALL AND I WANT THAT ON THE RECORD.** The
measurement that killed the detectors was mine and the implementer acted on
it rather than arguing with it. A keyword list that rules on a sixth of its
domain while reading as complete is worse than a prohibition, because the
green suite is the thing that lies. Both halves landed in a standalone
`process:` commit citing the directive, additive, zero deletions. The honest
cost -- a sentence of the species can now land with the suite green -- is
written down in three places and is real: six landed this round. That is an
argument for running the reading every round, which `docs/SUPERVISOR.md`
item 6 now requires, and not an argument for the list.

**AND THE GATE HOLDS UNDER AN ATTACK THE CELL DOES NOT MAKE.** I widened the
R438 cell along the one axis it still pins: which member is released. Over
all seven members x 22 units x 39 spans at `subdiv=1`, 392 configurations
pass `zero_modes_under_the_bound == 7` and **0 escape the bound**. The
worst, `199.5206` against `199.5262`, is not a mechanism at all -- every one
of the twelve worst sits at `stretch = 4.371037e5`, the corpus stretch
placed exactly where the CLEAN frame first flexible mode crosses the bound,
so the seventh eigenvalue counted there is that flexible mode. Excluding
bases whose clean `lambda_7` is inside `1.5x` of the bound leaves 329 and
**only released member 6 produces a mechanism at all**, worst `1.5243` --
the shipped figure, to four digits, from a sweep the implementer did not
write. The cell picks the right member and the figure is right. The `== 7`
filter is confounded at that one stretch and it does not reach the published
figure, because at member 6 those bases have EIGHT under the bound and are
dropped.

---

**R449. (BLOCKS, and it is the head. A cmd/out pair in the report CI section
where running the command gives a different answer in both halves. This is
the R412 subject -- a CI run reported as something it was not -- in the
round that repaired the CI-section guard.)** `docs/reports/F2/step-5.md`
section 0a.

```
code 0a "cmd   gh run view 35545894471 --json conclusion -- this round push
         out   conclusion **FAILURE**, same reason, ladder green"
cmd  gh run view 35545894471 --json conclusion,jobs
out  conclusion: cancelled
     jobs: the verification ladder      -> cancelled
           lint, unit and guards        -> cancelled
           CI determinism -- leg        -> skipped
           CI determinism -- ten legs   -> skipped
cmd  gh run list --limit 12 --json databaseId,headSha,conclusion
out  35545894471 at 7895944: cancelled. The only FAILURE at that head is the
     dispatch 35545894507, which 0a names separately and correctly.
judge BOTH HALVES ARE WRONG. The conclusion is cancelled, not failure, and
     the ladder was CANCELLED, not green -- it completed none of its steps.
     A cancelled run is not a result at all, and reporting it as a failure
     "for the same reason" attributes to it a reason it never reached.
cell ONE VARIABLE: the same command against the sibling run. gh run view
     35545894507 --json conclusion returns failure, which 0a reports
     correctly. So the tool works and the run id is right; what is wrong is
     that the output beside the command is not the output.
judge AND IT PROPAGATED. The directive I was handed repeated the report
     wording, so this would have entered my own verdict unchecked.
```

  **Closed when** section 0a states cancelled for `35545894471`, drops "same
  reason, ladder green", and says what a cancelled run does and does not
  license -- pasted from the command, not from the neighbouring run.

**R450. (BLOCKS -- a triple counts its own `claim:` and `cmd:` lines, so
`out: 6` is the tree 4 plus 2 of itself, and the claim enumeration names two
lines that do not exist. The R443b fix opened this in the same round.)**
`scripts/regen_figures.py:660-665` and
`tests/test_tree_prose_consistent.py:94-103`.

```
code test_tree_prose_consistent.py:94 "AN ANNOTATION LINE IS NOT PART OF THE
     TREE IT MEASURES: every `cmd:` contains the needle it searches for, so
     the first four triples written here counted themselves."
code :103 _ANNOTATION carries a trailing negative lookahead for an equals
     sign, added to spare `out: list[tuple[int, str]] = []` (R443b)
judge THE LOOKAHEAD EXEMPTS ANY ANNOTATION LINE WHOSE REST CONTAINS AN
     EQUALS SIGN -- including every `cmd:` whose NEEDLE contains one, which
     is the one shipped triple that has one.
cmd  the shipped _ANNOTATION applied to every line of scripts/regen_figures.py
     containing the needle log=True
out  118: comment, AND THEY ARE WHY log=True IS NOT A DEAD FLAG ...
     130: _floor("rigid_mode_seventh_orders", "derived", log=True),
     265: log=True,
     647: comment, AND log=True SAYS THE VALUE IS log10 OF A RATIO ...
     660: the triple OWN claim line
     663: the triple OWN cmd line
cell ONE VARIABLE, the regex: with the PREVIOUS annotation pattern (at
     ed67a7d, no equals carve-out) the same needle counts **4**. The tree
     content is 4; the shipped answer is 6; the difference is the triple.
code the claim at :660-662 enumerates the six as two _floor calls plus
     "this comment block, the one above it, and the two in the class
     vocabulary"
cmd  grep -n "log=True" over the class-vocabulary block, lines 640-646
out  no hit. THERE ARE NO TWO IN THE CLASS VOCABULARY. The two unaccounted
     hits are :660 and :663 themselves.
judge SO out:4 -> out:6 WAS A DEFECT IN THE GUARD, and the claim was
     rewritten to justify the new number with an enumeration naming lines
     that do not exist. R434 exactly -- a claim that is not what its command
     measures -- inside the mechanism built to close R434.
```

  **Closed when** the annotation strip excludes an annotated ASSIGNMENT
  rather than any line containing an equals sign, `out:` returns to what the
  tree contains, and the claim enumerates lines a reader can find.
  `tests/corpus/prose_triple_shapes.txt` carries three entries for this.

**R451. (BLOCKS -- the BP0 case. A figure row CLASS changed in `1824b9a` and
the sentence in `floatfea/tolerances.py` naming the old class was
republished unchanged in the same round.)** `floatfea/tolerances.py:424-426`.

```
code :420 "{{fig:rigid_mode_corpus_in_the_window}} frames are inside the
     :424  spread ... NOTHING IN CI CHECKS WHICH SIDE THEY FALL ON ... The
     :425  check that would see it is --check on a non-canonical runner,
     :426  and there this row is `derived` rather than exact."
cmd  floor_class() from scripts/regen_figures.py, at this commit
out  rigid_mode_corpus_refused         -> kind words
     rigid_mode_corpus_in_the_window   -> NOT PRESENT, it is a plain row
judge FALSE UNDER BOTH READINGS. If "this row" is rigid_mode_corpus_refused
     -- the row that counts which side they fall on -- it is `words` now,
     changed by R448 in `1824b9a`, in this round. If it is
     rigid_mode_corpus_in_the_window, it is not floor-class at all, so
     --check requires it to agree EXACTLY and would call a difference
     staleness rather than "seeing it".
cmd  git show --stat 1824b9a
out  floatfea/tolerances.py and scripts/regen_figures.py in the same commit.
     The class moved and the sentence naming it did not.
```

  **Closed when** `:426` names the row and its class as `floor_class()`
  returns them, or the sentence is deleted.

**R452. (BLOCKS -- a number in `floatfea/tolerances.py` that does not
describe the repository, in the entry this round edited, five lines above
the generated figure that contradicts it.)** `floatfea/tolerances.py:400`.

```
code :399 "That is measured, not argued: over all 114 corpus frames
     :400  below_bound == 6 and lambda_7 > bound and rigid_max < bound
     :401  disagree on ZERO."
cmd  grep "rigid_mode_corpus_frames" docs/milestones/F2_figures.md
out  | rigid_mode_corpus_frames | 126 |
cell MY OWN RE-RUN of the claim at 126 frames, one variable moved (the
     corpus, not the predicate): 126 frames, 0 disagreements. THE CLAIM IS
     STILL TRUE. The number beside it is stale by 12 frames.
judge The entry references {{fig:rigid_mode_corpus_frames}} five lines later
     and types 114 here. BI3 inside the file BI3 is about, and a different
     species from R433, which named seven MACHINE-DEPENDENT values: 114 is
     machine-independent and simply old.
```

  **Closed when** `:400` reads the figure reference or the sentence drops
  the count.

**R453. (BLOCKS -- the report sentence for leaving R447 open is false in
both halves, and one command the implementer ran this round prints the
refutation. It also refutes half of R447 as I wrote it, which is mine.)**
`docs/reports/F2/step-5.md` section 5.

```
code s5 "**R447 stands and I am not claiming it**: rigid_mode_mechanism_
     ceiling is the tightest floor-class row in the file and the entry does
     not say so. It got tighter this round, not looser."
cmd  python scripts/regen_figures.py --check     (this machine, at ab698c0)
out  rigid_body_mode_ratio                1.1986e-14  1.6009e-14   1.3356x
     rigid_mode_largest_rigid_eigenvalue  1.2727      1.4614       1.1483x
     rigid_mode_mechanism_ceiling         1.6519      1.5243       1.0837x
     clean_worst_ratio                    0.2564x     0.2765x      1.0784x
     -- every other row at or under 1.0086x
judge (a) THE TIGHTEST ROW IS rigid_body_mode_ratio AT 1.3356x, with 1.123x
     of margin against FIGURE_FLOOR_CLASS_SPREAD = 1.5. The mechanism
     ceiling is fourth.
     (b) IT GOT LOOSER, NOT TIGHTER: 1.4314x last round (0.9606 against
     1.3750) against 1.0837x now, so the margin went from 1.048x to 1.384x.
     The widened cell raised the canonical value more than the local one and
     closed the gap.
judge AND HALF OF R447 WAS MY OWN ERROR. I wrote "every other floor-class
     row on this machine is at or under 1.1483x"; rigid_body_mode_ratio was
     `below`-class then with the same two values, so it printed 1.3356x in
     the same table I was reading. A `below`-class row prints its spread
     exactly as a `derived` one does. **Recorded as mine.**
```

  **Closed when** section 5 says which row is tightest and in which
  direction the mechanism row moved, both from the --check run, and R447 is
  restated on the row it is actually about.

**R454. (BLOCKS -- the R439 repair replaced a refuted reason with another
refuted reason. The ground for withholding the loss count is now "nothing
cites it", and four sentences in the tree cite it.)**
`scripts/regen_figures.py:337-343`.

```
code :341 "What keeps it out is that no sentence anywhere needs it -- the
     :342  contrast the reports draw is with the ratio"
cmd  grep -rn "breached at more|indicted harder" floatfea/ tests/ scripts/ docs/milestones/
out  floatfea/tolerances.py:650                    (the loss entry itself)
     tests/test_counters_are_injected.py:164
     tests/verification/rung1/test_rigid_body_modes.py:575
     docs/milestones/F2.md:1784
     -- four sentences, each of the form "it breached at MORE of the
     reviewer clean frames THAN THE RATIO DID". Every one is a comparison
     whose truth IS the loss count against the published one.
cell MY OWN MEASUREMENT, one loop over the corpus: 126 frames, ratio_over
     91, loss_over 101. THE SENTENCE IS TRUE. It is also uncheckable by any
     reader, because 91 is a published figure and 101 is withheld on the
     ground that nothing needs it.
judge R439 was "the stated ground for withholding the loss count is refuted
     by the row sixteen lines above it". This is the same shape one round
     later: the new ground is refuted by four sentences, one of them in the
     same file, and the round that wrote it also rewrote that entry.
```

  **Closed when** `retired_loss_over_ceiling_on_corpus` is published as a
  `words` row like its two siblings and the four sentences reference it, or
  the four sentences are reduced to what the published figures support.
  Note that `tests/verification/rung1/test_rigid_body_modes.py:37` asserts
  that figure is ABSENT, so publishing it moves that triple too.

---

**Recorded, and lock items for step 4a (BU0). None of these touches the gate
assertion, a tolerance, or the truth of a published figure.**

**R455. The negative control is satisfiable by writing the needle down, and
R434 is re-admissible verbatim -- one shape of it without adding a control
line at all.** Measured against the shipped module; the entries are in
`tests/corpus/prose_triple_shapes.txt`. (a) `files("tests/**/*.py",
"RIGID_MODE_FLOOR ")` -- the name plus a trailing space -- returns `none`,
and the SHIPPED control `tau = RIGID_MODE_FLOOR * norm * EPS` contains that
substring, so `ctl: floor_constant_name` passes and an absence claim is
certified by a needle that matches nothing in `tests/`. (b)
`defined("RIGID_MODE_BONUD")` returns `no`, which is neither `none` nor a
bare count, so `_BARE_COUNT` does not fire and **no control is required at
all** -- R434 in the one vocabulary word the control requirement does not
reach. (c) The requirement is written on the shape of the ANSWER, so an
absence spelled `0 of 12` escapes it. 0 of the 17 defect shapes in the new
corpus are caught; the 5 that agree are allow-controls and declared design
decisions. The module docstring already says a triple does not prove the
claim is what the command measures, which is honest; what it also says at
:50 is "A needle that cannot match fails its control", and that is the
sentence these three refute.

**R456. `tests/prose_triple_controls.txt` says it is excluded from the
vocabulary own searches and it is not, and three of its eleven lines are a
silently collapsed duplicate.** `_paths()` excludes CONTROLS in the GLOB
branch only, so `count("tests/prose_triple_controls.txt",
"RIGID_BODY_MODE_RATIO")` returns **5**. `ratio_counter_name` is planted
three times identically; `_CONTROL_LINES` is a dict comprehension, so 11
lines parse to 9 ids and the LAST wins -- a bad duplicate placed first is
invisible, and `test_every_control_line_is_used_by_a_triple` compares sets
and cannot see it.

**R457. CV3 rules correctly on 15 of 20 unseen shapes, up from 3 of 12, and
the substantive miss is that it decides per PARAGRAPH and not per RUN.**
`tests/corpus/report_ci_section.txt`, twenty new entries. One conclusion
anywhere in a paragraph satisfies every run id in it, so "Run 35489487935
had conclusion success. Run 35545894507 is also named here." is allowed --
the R412 shape with a neighbour, and the shape section 0a would have had if
two of its three runs had been left bare. `_joined` strips commas, spaces,
hyphens and en-dashes after the word `run` but not underscores. Two false
positives: a conclusion whose value wraps to the next line, and a genuine
result pasted on the same line as the gh command that produced it, which
`_COMMANDISH` discards.

**R458. The CW1 reading is the whole enforcement now, and its declared scope
is five roots plus one file, `.py` and `.md` only.** Out of scope and not
declared out: `PLAN.md`, `docs/conventions.md` (locked and authoritative for
frames and signs), `docs/hsp-coupling.md`, `docs/closure/`,
`.github/workflows/*.yml`, and every `tests/corpus/*.txt` header -- including
the two I write. And a claim/cmd/out written inside a markdown fenced block
is parsed by nothing: `_markdown_prose` blanks fenced lines, so a fenced
triple reads as checked and is checked by no one. Measured: 0 triples found
in a fenced block.

## Tolerances touched

**NONE. No constant was created, retired, or moved.**

```
cmd  git diff ed67a7d..HEAD -- floatfea/ | grep -E "^[+-][A-Z_]+.*Final"
out  (empty)
cmd  git diff --stat ed67a7d..HEAD -- floatfea/
out  floatfea/tolerances.py | 72 ++-   -- ONE FILE, every line a comment
judge NO VALUE WAS WIDENED AND NO VALUE MOVED. What changed is prose: the
     R434 and R435 triples, the R438 two candidates and the subdiv reason.
     Two of those prose neighbourhoods carry R451 and R452, which is part of
     why this step holds -- but not one of them moves a threshold or a
     decision.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2537 passed at ab698c0 -- no undeclared literal entered tests/ this
     round and nothing was added to tolerance_marker_exemptions.txt.
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**CW4 asked for PASS or a named head. The head is R449** -- a CI run
reported as a failure that was cancelled, with its ladder reported green
when the ladder was cancelled, beside the command that says so. I am not
classing that as apparatus. CE1 exists because CI was red at three
consecutive reviewed commits and no report said so; R412 was a run named
with no result; the species is "the CI record in the report is not the CI
record", and this is that species with a cmd line in front of it. It also
propagated: the directive I was handed repeated the wording, and I would
have published it unchecked.

**Six items hold.**

1. **R449 -- gh run view 35545894471 returns cancelled, not FAILURE, and its
   ladder job was cancelled, not green.** Report section 0a.
2. **R450 -- a triple counts its own claim and cmd lines**, because the
   R443b fix exempts any annotation line whose needle contains an equals
   sign. out:6 is the tree 4 plus 2 of itself, and the claim names "the two
   in the class vocabulary", where there are none.
3. **R451 -- "this row is derived rather than exact"**, in the file whose
   sibling commit made it words. BP0.
4. **R452 -- "over all 114 corpus frames"**, where the corpus is 126 and the
   generated figure saying so is referenced five lines away. The claim
   itself I re-measured and it holds at 126.
5. **R453 -- the sentence leaving R447 open is false in both halves**: the
   tightest floor-class row is rigid_body_mode_ratio at 1.3356x, and the
   mechanism row went from 1.4314x to 1.0837x, which is looser.
6. **R454 -- "no sentence anywhere needs it"**, with four sentences in four
   files needing it, one of them in tolerances.py.

**The finding behind the findings, fourth round running, and it has changed
shape.** Last round I wrote that the species survives because the
enforcement is a keyword list and the defect is not. The list is gone and
the species is unchanged: five of these six are sentences written in the
commit that repaired the same species elsewhere. What CP2 names is not a
detection problem at all -- it is that the attention goes to the thing being
fixed and the prose written AROUND the fix inherits none of the discipline
applied TO it. R450 is the sharpest instance this project has produced: the
guard built to stop a claim that is not what its command measures shipped a
claim that is not what its command measures, and the command was made wrong
by the same commit other fix. **The reading is the right answer and the
reading has to cover the repair own prose**, which is the one place four
rounds of this have landed. The cheapest mechanical help available is not
another pattern: it is that any commit changing a figure CLASS, a regex or
a generator runs `grep -rn` for the old class name and the old number before
it is committed, which is BP0 with a command attached.

**Adversarial corpus (BE3): 42 new entries across two files, all unseen by
the implementer, committed separately at `05390a5`.**

**`tests/corpus/prose_triple_shapes.txt`, NEW, 22 entries. The shipped code
agrees with 5, and all five are allow-controls or design decisions the
module declares. 0 of the 17 defect shapes.** Four of the seventeen are
R434 re-admissible; one of those four needs no new control line, because a
shipped one already contains the malformed needle. Three are R450 and were
found by running the shipped `_ANNOTATION` over the tree rather than reading
it.

**`tests/corpus/report_ci_section.txt`, 23 to 43. Twenty entries, 15 ruled
correctly.** Against 3 of 12 last round, and all four of the R412-one-level-
up shapes from last round are refused now. CV3 is the best-measured repair
in this round and I want that said next to R449, which is in the same
section of the same report.

```
cmd  python -m pytest tests/ -q --ignore=tests/verification   (after my adds)
out  9 failed, 1125 passed -- test_every_corpus_shape_is_transcribed and
     eight cascades in test_report_guard_states.py. THAT IS THE R440 REPAIR
     WORKING: my 20 new ids are not transcribed and the guard says so. It is
     not a regression, and the 2537-pass run above is at ab698c0, before my
     commit.
```

**Not gates on step 5, into the next report Carried section:** R455, R456,
R457, R458, R447 (restated), R419, R431, R432, R433, R410, R411, R413, R414,
R400, R401, R402, R390, R391, R392, R393, R383, R370, R371, R372, R373,
R374, R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350
second half, R330, R331, R332, the section 9 status-versus-subject
disagreement, R321, R322, R300, R291, R292, R281, R231, R244, R245, R275,
R230, R261, the underlying gap in R276, R277, R262, R264, R266, the two R248
residues, R249-R252, R225-R228, R232, R233, and everything already at 4a.
**R434, R435, R436, R437, R438, R440, R444, R445, R446 and R448 are closed.**
R439 closed and reopens in substance as R454; R443b closed and reopens as
R450; R447 stands, restated, with half of it withdrawn as my error.

**Fifty rounds have found no element defect and this round found none
either.** 392 mechanism configurations over all seven released members, 22
units and 39 spans, zero escapes, and the shipped figure reproduced to four
digits by a sweep the implementer did not write; 126 corpus frames with the
residual green at every one; ten determinism legs executed on a tree
identical in `tests/verification` and `.github` to the one under review. It
still means "not yet contradicted": ladder 5 has printed `OK -- 0
directories ran` every time it has run, and V5.1 against CalculiX is the
witness that has not spoken.
