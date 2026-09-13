# Review — F2 step 5
Reviewed commit: d195721580a5f24df9fc5258344c275a3323802e
Verdict: HOLD

**Reviewed commit: `d273acf`.** Report revision 18, `Answers: verdict 43 @
7fd7155`. The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`d195721` -- not the commit judged. That is R373, still open; read `d273acf`.

Tests: **2114 passed, 0 failed, 0 skipped** at `d273acf` (my run, clean tree,
`python -m pytest -q`, 483.73 s, Python 3.13.15 on Windows).

**AND 2131 PASSED, 0 FAILED AT MY OWN CORPUS COMMIT `d195721`**, which BE3
requires me to make. **That is R377, closed.** Last round the same commit gave
`1 failed`. I ran the ablation as well as the cell: restoring the pre-repair
`_report_anchor()` at that commit gives **8 failed, 18 passed** in
`tests/test_report_guard_states.py`, `two_digit_step_number` among them.

**Commits: `6d5f41a`, `3f0ff7f`, `ad7208f`, `1044a50`, `4e79873`; plan
`e642b12`. Report `d273acf`.**

**Item 1b.** Revision 18's header at line 6328 reads `Answers: verdict 43 @
7fd7155`; `git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`7fd7155da38de60ea04d075581c88a6f02cad3e8`. It is the latest. **Passes.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit d273acf
out  run 34774429589 -- event push, conclusion SUCCESS
cmd  gh api .../runs/34774429589/jobs
out  "lint, unit and guards"     success, runner "GitHub Actions 1000000951",
                                 14 steps
     "the verification ladder"   success, runner "GitHub Actions 1000000950",
                                 13 steps
     "CI determinism -- leg"          SKIPPED, runner null, 0 steps
     "CI determinism -- ten legs"     SKIPPED, runner null, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING.
     Not CK2: runners were assigned to the two that ran and steps executed,
     so the allowance is not the constraint. The determinism pair is an
     UNAVAILABLE check by design -- dispatch-only -- recorded as unavailable
     rather than skipped over, and R383 still holds: the last dispatch that
     executed them was at `9cec13e` and the tree has moved since.
cmd  failing_names(34774429589), the reader 3f0ff7f adds
out  {} -- and the same reader returns 4 names on run 34665512659 and 4 on
     34659275127, so it is a check that can fail. I ran the negative control
     rather than trusting the green.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff 7fd7155..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff 7fd7155..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set, and no plugin was added
cmd  git diff 7fd7155..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 7fd7155..HEAD -- floatfea
out  (empty) -- NINETEEN ROUNDS
cmd  git show --name-only on each of the six commits
out  `e642b12` touches docs/milestones/F2.md and docs/closure/F1.md only, is
     standalone, and says RE-LOCKED. No commit mixes process with code.
```

## Carried

Verdict 43 held on R375, R376, R377, R378, R379 and R380. **All six are
answered, and I reproduced five of them in a clean clone rather than reading
them.** This is the first round of this step where every gated item closed.

- **R375 -- ANSWERED AT BOTH LIMBS OF A CONDITION THAT OFFERED EITHER, and I
  re-ran my own evasion against the repair.**

```
cell clean clone at d273acf: (a) `ast.walk(inner)` to `ast.walk(inner.right)`,
     then thirteen lines under a CRLF comment repointing `CORPUS` at a temp
     copy with one entry rewritten -- byte for byte my own leaf-four edit
out  1 failed, 96 passed
     FAILED test_the_corpus_path_is_the_repository_file
judge THE LEAF IS SHUT AND THE SENTENCE IS GONE. A grep for "share nothing but
     the path" finds nothing; the paragraph is an enumeration of five leaves,
     each naming the test that closes it, and then a statement of where the
     reach ends.
```

- **R376 -- ANSWERED, and the cell is mine, not theirs.**

```
cell (a) as above, plus a three-line special case in `_planted_caught` that
     returns False for one id. Clean clone at d273acf.
out  3 failed, 94 passed
     FAILED test_the_partition_is_recomputed_from_the_file
     FAILED test_no_shape_that_was_CAUGHT_when_planted_escapes_now
     FAILED test_the_exemption_window_gives_the_required_verdict[...]
judge LAST ROUND THE SAME EDIT GAVE 76 PASSED, 0 FAILED. Both sides of the
     partition are recomputed from `_entries_in_the_file()` now, so a special
     case disagrees with the file instead of with itself.
```

- **R377 -- ANSWERED, every limb of the condition, measured.** The anchor
  tells three states apart; the reviewer-commit cell is green in the clone and
  in the real repository; **2131 passed, 0 failed at my own corpus commit**
  against `1 failed` last round; and the ablation above names the repair as
  the cause. **What is not closed is the prose inside the repair: R387, R388.**

- **R378 -- ANSWERED in substance.** `git log --oneline 7fd7155..4e79873`
  prints six and section 10 now lists six, and `03e5f92`'s widening of
  `_CI_ROW` is described in section 4. The block is still not literally the
  command's output -- R391, recorded at 4a.

- **R379 -- ANSWERED at both named limbs.** Section 3 prints four sites and
  three rejection thresholds and the word "both" is gone; the guard's
  docstring at `:1-17` names its actual domain, names `reader.py:223` as a
  live instance of the literal its own first paragraph cites as closed, and
  points at the plan step. `git diff -- floatfea` is empty, which is what the
  finding asked for.

- **R380 -- ANSWERED, at the site.** `git show d273acf -- docs/reports/F2/step-5.md`
  puts a nine-line WITHDRAWN IN REVISION 18 block immediately above revision
  16 section 2, naming the wrong attribution and pointing at revision 17
  section 1. Editing a published revision in place was the right call and I
  want that recorded: it is the remedy R366 earned, applied where it was
  earned.

- **R381 and R384 -- CLOSED, and I measured it on my own data rather than on
  their cell.** `scripts/corpus_figures.py` reads `260 260 106 154 40` against
  `225 225 89 136 37` last round. Running the `7fd7155` scanner over the
  improvements as a control isolates exactly three entries that moved this
  round: `clean_float_of_the_string_infinity`,
  `fold_tightening_a_declared_name_by_an_integer`,
  `fold_widening_a_declared_name_by_an_integer`. Three asked, three moved,
  none of my new entries among them.

- **R382 -- DONE rather than carried, and the sentence is the right one.**
  `tests/test_report_carried.py:1160-1167` says the hook refuses any Bash
  command naming the verdict tree, that the split spelling is what lets the
  file be worked on at all, and that a grep over `tests/` will not find the
  line. Naming the cost is what the finding asked for.

- **R383 -- OPEN at 4a, correctly listed.** The determinism jobs were SKIPPED
  again at the reviewed commit, so CP3's predicate has still never executed.

- **R370, R371, R372, R373, R374 -- OPEN at 4a**, correctly listed in section
  6 and rowed in section 9. R373 bites again in this verdict's own header.

- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350's second
  half, R330, R331, R332 -- OPEN at 4a, correctly listed.** R332 honoured
  again: nothing reads `g21_rigid_body_frames.txt`, so I added nothing to it.

- **R231, R244, R245, R275 -- OPEN, unblocked, and the report correctly does
  not claim them.**

- **R223, R224 -- Q7 does not open.** CQ4 asks me to open it on a verdict
  without gate items. This verdict has gate items. Recorded so the ask is not
  lost rather than silently declined; the CI condition behind it has now been
  met at three consecutive reviewed commits.

- **R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged and
  stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** The
  generated table still expands a range by its endpoints only, so R250, R251,
  R226, R227, R264 and R266 have no row; R348 territory, unmoved.

- **R365, R366, R367, R368, R369 -- correctly moved from `answered` to
  `carried` in `step-5-answers.json`.** Checked the diff; the bookkeeping is
  right.

## Findings

**R385. (BLOCKS -- a RE-LOCKED plan row names a directory that is not in this
repository, and the directory it names belongs to the repository CLAUDE.md
says is never forked.)** `docs/milestones/F2.md:1951`, in `e642b12`.

```
code :1951 "`tests/test_no_tolerance_literals.py` scans `floatfea/` and
           `floatsim/io/` as well as `tests/`, and the build is RED on any
           undeclared tolerance in the package from then on."
cmd  git ls-files -- floatsim | wc -l
out  0
cmd  ls -d */
out  artifacts/ docs/ floatfea/ scripts/ tests/   -- there is no floatsim/
cmd  grep -rn "floatsim/io" --include=*.md .
out  docs/findings/G1.0-floatsim-output-audit.md:24 and docs/milestones/F1.md:38
     -- both about HSP's tree, which docs/hsp-coupling.md:45 puts in a
     SEPARATE worktree: `git worktree add ../HSP-stable <REFERENCE_TAG>`
judge A GLOB OVER A PATH THAT IS NOT HERE FINDS NOTHING AND READS GREEN, which
     is this repository's own "empty parameter set is an error, not a skip".
     Half of the widened domain in the locked plan is vacuous by construction.
     CLAUDE.md's Relationship to HSP forbids the other reading: FloatFEA does
     not vendor FloatSim, and a FloatFEA guard has no business reddening on
     HSP's tree.
judge AND THE TREE THE ROUND ACTUALLY SCANNED IS NOT IN THE ROW. `1044a50` ran
     `offending()` over `scripts/` and added a marker at
     `scripts/regen_figures.py:299-305` on the strength of it. `scripts/` is
     in neither the shipped domain nor the widened one, so that marker is
     inert today and will still be inert after step R.
```

**Closed when** the D5a row names the trees that exist here and that step R
will actually scan -- `floatfea/`, and `scripts/` if the round's own cell is
to mean anything -- and `floatsim/io/` is struck or given the sentence that
says it is HSP's and out of reach. One `git ls-files` is the check. A plan
edit in a standalone plan commit, not a code change.

**R386. (BLOCKS -- the gate on four tolerances that decide whether a FloatSim
record is REJECTED cannot fail. The invocation asked this directly and the
answer is cheaper now than after R1 runs.)** `docs/milestones/F2.md` section
D5a, "Step R1 -- the four move, and the decisions do not".

```
code R1 "each literal moves into `tolerances.py` at its IDENTICAL value"
code R1 "The gate for the step is decision-invariance, not equality of
        numbers. Every record ... keeps its accept/reject verdict and its
        `Fault`."
judge THOSE TWO SENTENCES CANNOT BOTH BE INFORMATIVE. A Python float bound to
     a name is the same float: `np.isclose(..., rtol=1e-10)` and
     `np.isclose(..., rtol=READER_INERTIA_SYMMETRY)` with the name equal to
     1e-10 are bit-identical on every input, so every record keeps its verdict
     and its `Fault` NECESSARILY. The gate passes before the step is written.
     Ask the question this repository asks of every check: if the thing it
     claims were false, would this go red? It cannot be false.
judge WHAT R1 NEEDS IS THE TWO THINGS D5a NAMES WITHOUT GATING.
     (i) PROVENANCE, NOT EXISTENCE. That the value reaches the comparison
     THROUGH `floatfea.tolerances` rather than as a literal is a STRUCTURAL
     assertion, and a pass/fail over records cannot show it. The widened
     scanner is that assertion and R1 ships before it, so R1 has none.
     (ii) THE `_COUNTER` IS THE GATE THAT BITES. D5a asks for one per D5 and
     then makes decision-invariance "the gate for the step". The counter is
     the smallest defect the same assertion detects in the same quantity --
     an injected asymmetry in the inertia tensor, an injected drift in the
     time base -- and it is what makes each of these four a check.
judge AND R2's INVARIANCE CAN PASS VACUOUSLY, a different defect in the same
     sentence. `atol=1e-9` on |g| becoming relative MOVES the accept
     boundary. "Every record keeps its verdict" is satisfied if no record in
     the F1 set lies near that boundary -- assertion domain blindness, over a
     small hand-made collection. The fix is a rule already written down here:
     INVERT THE DECISION RULE AND SOLVE. Report the |g| at which accept flips
     under each form and the nearest F1 record's margin to each, so the
     invariance is a measured distance and not a sample on one side.
```

**Closed when** D5a states each step's gate in a form that can fail: for R1, a
structural provenance assertion plus each entry's `_COUNTER` with the quantity
it is injected in; for R2, the two solved boundaries and the nearest record's
margin to each, with decision-invariance kept as the necessary condition it is
rather than as the gate. **If the judgement is that decision-invariance IS
sufficient, say so with the measurement showing a record near the boundary** --
that would refute me and it is one loop.

**R387. (BLOCKS -- a phantom citation, in the comment that explains why the
R377 repair is safe. "Every citation resolves" is the guard, and this is the
first phantom since it was written down.)** `tests/test_report_carried.py:1254`.

```
code :1253 "`test_the_report_this_guard_measures_HAS_history` is what
     :1254  stops this branch from ever being taken in this repository."
cmd  grep -rn "test_the_report_this_guard_measures_HAS_history" .
out  tests/test_report_carried.py:1254 -- the citation, and nothing else
cmd  grep -rn "def test_the_report_this_guard_measures" tests/
out  (nothing)
judge THE TEST DOES NOT EXIST. The one that does the job is
     `test_the_anchor_fallback_cannot_be_taken_in_this_repository` at :1342,
     and section 1 of the report cites THAT one correctly. The comment at the
     branch -- the place a reader checking the branch will look -- names a
     test nobody can run.
```

**Closed when** the comment names the test that exists. One line.

**R388. (BLOCKS -- the docstring enumerating the three anchor states is
refuted by its own function, in the state the harness constructs every round
and the one R377 was about.)** `tests/test_report_carried.py:1108-1117`,
`:1249-1252`.

```
code :1112 '""          the report path has NO HISTORY. Not the same thing as
     :1113  "not committed yet"...'
cell clean clone at d273acf, docs/reports/F2/step-5.md and step-10.md both
     present, step-10 untracked -- byte for byte the two_digit_step_number build
cmd  REPORT.name; ls-files --error-unmatch REPORT; _last_commit_touching(REPORT);
     _report_anchor()
out  REPORT        step-10.md
     tracked?      False
     log of REPORT ''          <- the report path HAS NO HISTORY
     anchor        'd273acf8'  <- AND THE FUNCTION RETURNS A SHA
judge SO THE THIRD ROW IS FALSE FOR THE STATE IT NAMES. `""` comes back only
     when the reports TREE has no history, or when `git status` itself fails.
     The commit message 6d5f41a states this correctly -- "no history for this
     path; the reports TREE is the anchor instead, and only when that has none
     either does rule 1 stand down" -- and the shipped docstring does not. The
     comment at :1249, "NO HISTORY FOR THIS REPORT PATH (R377). There is no
     commit to measure a distance to", labels a branch never taken for that
     reason.
judge THIS IS R380's SPECIES INSIDE THE ROUND THAT FIXED R380: the true
     sentence is eight lines below the false one, and a reader stops at the
     table.
```

**Closed when** the table's third row says what actually returns `""` -- the
reports tree having no history, or git failing -- and the comment at `:1249`
names the same condition, with the cell above run at the commit that publishes
the change. R387 and R388 are the same twenty lines and close together.

**R389. (BLOCKS -- CQ3's two stated rules are each refuted by a one-line
input, measured on entries the implementer has never read. The subject of
`1044a50` claims the species; fourteen spellings of the species are clean.)**
`tests/test_no_tolerance_literals.py:248-260`, `:290-295`.

```
code :248 "# WHAT LEAVES A DECLARED VALUE ALONE, per operator."
cmd  the shipped offending() at d273acf, one file per shape
out  clean   assert cond < 1 / ROUNDOFF_IDENTITY
     clean   assert cond < 1.0 / ROUNDOFF_IDENTITY
     clean   assert cond < 1 // ROUNDOFF_IDENTITY
     clean   assert err  < 1 ** ROUNDOFF_IDENTITY
     clean   assert err  < 0 - ROUNDOFF_IDENTITY
judge THE IDENTITY TABLE HAS NO SIDE, AND FOUR OF ITS EIGHT OPERATORS ARE NOT
     COMMUTATIVE. 1.0 is Div's identity on the RIGHT; on the left it is a
     RECIPROCAL, and `1 / ROUNDOFF_IDENTITY` is a bound fifteen orders of
     magnitude from the declared one. `1 ** DECLARED` is the constant 1.0 with
     the declared name decorative. `0 - DECLARED` is a sign flip.
     `_numbers_beside_a_declared_name` does `for side in (node.left,
     node.right)` and applies one table to both. A conditioning ceiling
     spelled `cond < 1 / DECLARED` is not an exotic line in this repository.
code :293 "Every nested BinOp is visited by the caller's own loop, so a
     :295  literal that really does modify the declared value is reached as
           somebody's operand."
cmd  the same scanner, the same way
out  clean   assert err < ROUNDOFF_IDENTITY * (1 + 1)
     clean   assert err < ROUNDOFF_IDENTITY * (10 - 8)
     clean   assert err < ROUNDOFF_IDENTITY * 2 ** 10
     clean   assert err < (1 + 1) * ROUNDOFF_IDENTITY
     clean   assert err < ROUNDOFF_IDENTITY / (2 * 5)
     clean   assert err < ROUNDOFF_IDENTITY * float(2)   (also int, abs, np.float64)
     CAUGHT  assert err < ROUNDOFF_IDENTITY * (1000)     -- the control
judge THE NESTED BinOp IS VISITED AND THEN SKIPPED. `_literal_thresholds_inside`
     requires a DECLARED NAME inside each BinOp it looks at; `(1 + 1)` holds
     none, so it continues, and the outer BinOp's operands are a Name and a
     BinOp, neither of which `_as_number` reads. The folding rule cannot pick
     it up either: it bounds itself under one, and 2.0 and 1024.0 are over. A
     declared tolerance DOUBLED by `* (1 + 1)` reaches the comparison with
     nothing looking at it, and that is the sentence's own counter-example.
cmd  the same scanner, on the two keyword forms
out  CAUGHT  assert a == pytest.approx(b, rel=ROUNDOFF_IDENTITY * 10)
     clean   assert np.isclose(a, b, atol=ROUNDOFF_IDENTITY * 10)
judge AND THE SPECIES DOES NOT REACH THE KEYWORD FORM IT MOST OFTEN TAKES.
     Recorded separately as R390 because that is a gap and not a sentence.
judge WHAT IS RIGHT, AND I WANT IT RECORDED. R384 IS GENUINELY CLOSED -- both
     entries I planted for it moved, with the old scanner as the control --
     the hatch reaches the new species on one line and split across five, and
     `<< 0` clean against `<< 1` caught pins the boundary from both sides. The
     rule is a real improvement. What blocks is two sentences claiming more
     than the rule does.
```

**Closed when** either the rule reaches these -- the identity excused only in
the position where it IS an identity, and a compound operand descended into --
with the false-positive control `RIGID_BODY_MODE_RATIO * w[RIGID - 1]` still
clean; **or** `:248` and `:290-295` say what is true: that a literal is excused
whenever it equals its operator's identity on EITHER side, that an operand
which is itself an expression or a call is not read, and that both are known
gaps with `tests/corpus/tolerance_marker_exemptions.txt` recording them. **I
would take the sentences.** Fourteen of my eighteen misses are these two axes,
and a reader who trusts `:293` will write `DECLARED * 2 ** 10` and believe the
guard looked.

**R390. (recordable, 4a) The CQ3 species does not reach a tolerance keyword.**
`assert np.isclose(a, b, atol=ROUNDOFF_IDENTITY * 10)` is clean while
`pytest.approx(b, rel=ROUNDOFF_IDENTITY * 10)` is caught: the first has no
`ast.Compare` for `_literal_thresholds_inside` to be called on, and the keyword
rule looks for a `Constant`. `atol=` and `rtol=` are where a tolerance most
often travels in this tree. Corpus entry `cq3_scaled_name_as_an_isclose_keyword`.

**R391. (recordable, 4a) Section 10's `out` is still not the command's
output.** `git log --oneline 7fd7155..4e79873` prints newest-first; section 10
lists the six oldest-first with subjects truncated mid-word, dropping
RE-LOCKED from `e642b12`'s. R378's substance is answered -- all six are there
and `03e5f92` is described -- so this does not block; a block labelled `out`
that is not the output is nevertheless the shape R378 was.

**R392. (recordable, 4a) `failing_names()` has no shipped test, and nothing in
the suite reads the line it produces.** `scripts/ci_section.py:178-226`; a grep
for `ci_section` or `failing_names` under `tests/` finds only `_ci_section()`,
which reads the report's own table. I ran the negative control myself and it
passes -- 4 names on each of two red runs, 0 on the green one -- which is
exactly why it should be a test rather than something a reviewer happens to
check. Second item this round in the R383 family: a repair to the CI apparatus
shipping with no executable check.

**R393. (recordable, 4a) Rule 2's message names the wrong commit while a new
report is being drafted.** Cell: clean clone at `d273acf`, one code commit,
`docs/reports/F2/step-6.md` copied in and left untracked -- the state every
step boundary passes through. The anchor falls back to the reports tree and
the failure reads "1 commit(s) touching code follow the report's own commit
d273acf", where `d273acf` is step FIVE's report commit and the report being
measured is uncommitted. The ablation says the state was red before the repair
too, by rule 1, so nothing new is broken; what changed is that the diagnosis
is now wrong. CE2's own lesson, one file over.

## Tolerances touched

**None in `floatfea/tolerances.py`.** `git diff 7fd7155..HEAD -- floatfea` is
empty over the whole package, for the nineteenth consecutive round.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| everything in `tolerances.py` | unchanged | -- | -- | the diff over the file is empty |
| `floatfea/io/reader.py:155` `atol=1e-9` | unchanged, UNDECLARED | **absolute on a dimensional quantity** (m/s^2), `rtol=0.0` | none exists | **now planned**: F2.md D5a step R2. R386 is about that gate |
| `floatfea/io/reader.py:206` `rtol=1e-9` | unchanged, UNDECLARED | dimensionless, on the time base | none exists | D5a step R1. R386 |
| `floatfea/io/reader.py:223` `rtol=1e-10` | unchanged, UNDECLARED | dimensionless, on the inertia tensor | none exists | D5a step R1. R386 |
| `floatfea/io/frames.py:358` `atol=1e-12` | unchanged, UNDECLARED | absolute, on omega in rad/s | none exists | D5a step R1. R386 |
| `scripts/regen_figures.py:303` `1.0` | unchanged, newly EXEMPTED | `hi / lo < 1.0 + BOUNDARY_BISECTION_CONVERGENCE` | n/a | the 1.0 is unity, the reference a ratio is compared to; the bound is the declared name beside it. **The marker is correct and it is also inert** -- nothing scans `scripts/`. R385 |

```
judge NO NUMBER IN ANY OF THE SIX COMMITS FUNCTIONS AS A TOLERANCE. CQ3's
     `_IDENTITY` table is a CLASSIFICATION BOUNDARY inside a scanner, not a
     threshold on a measured quantity, and I pinned it from both sides in the
     corpus rather than taking the docstring's word: `DECLARED << 0` clean and
     `DECLARED << 1` caught; `* 1`, `/ 1`, `+ 0`, `** 1` clean and `* 1_000`,
     `* 0x10` caught. R381's `math.isfinite` clause removes a report; it does
     not move a bound.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2114 passed at d273acf -- no undeclared literal entered tests/ this round
     and no `not-a-tolerance:` marker was added to any test file. The four in
     `floatfea/` remain outside that scan.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin, and Q7 does not open on this
verdict** -- CQ4 asks for a verdict without gate items and this is not one.
The CI condition behind Q7 has now been met at three consecutive reviewed
commits, and I record that rather than let the ask lapse.

**What moved this round is the most that has moved in this step, and it goes
before the holds.** All six gated items closed, five of them reproduced in a
clean clone. **R377 was mine twice over and it is gone**: 2131 passed, 0 failed
at my own corpus commit against 1 failed last round, with an ablation naming
the repair as the cause. **R375 and R376 were each closed at BOTH limbs of a
condition that offered either.** **R381 and R384 are closed and I proved it on
my own data** with the old scanner as the control: exactly three corpus
entries moved, and they are exactly the three those findings named. **The
withdrawal at revision 16's own site is the right shape** and it should become
the standard for this log. CI is green on Linux at the reviewed commit.
`floatfea/` is byte-identical for the nineteenth round.

**What holds is five items, and not one of them is in the work that closed a
finding. All five are in prose or plan written AROUND the repairs.** That is
CP2's exact pattern, and it is the fourth round running that it has decided
the verdict.

1. **R385 -- a RE-LOCKED plan row names `floatsim/io/`, which is not in this
   repository.** One `git ls-files` refutes it, and the tree the round's own
   cell actually scanned, `scripts/`, is not in the row.
2. **R386 -- the gate on four record-rejection tolerances cannot fail.** The
   values move unchanged, so decision-invariance holds before the step is
   written; and R2's half needs the solved boundary rather than a sample on
   one side of it.
3. **R387 -- a phantom test name** in the comment explaining why the R377
   branch is safe. One line.
4. **R388 -- the three-state table is refuted by its own function** in the
   state the harness builds every round. The commit message has it right and
   the shipped docstring does not.
5. **R389 -- CQ3's two stated rules are each refuted by a one-line input.**
   `1 / DECLARED` is excused by an identity that is only an identity on the
   other side; `DECLARED * (1 + 1)` and `DECLARED * 2 ** 10` are reached by
   nothing. **I would take the sentences over a sixth mechanism**, and the
   corpus now records both axes from outside.

**On the three questions the invocation asked.** *Amending an unpushed commit
whose figure was false is the right call* -- a withdrawal is owed to a reader
and nobody could have read it; what is owed is what section 4 does, naming
both instances in the published revision. *Editing revision 16 in place was
also right*, and better than deleting: the mark is at the site, names the
verdict that withdrew it, and points at the live account. *The decision-
invariance gate is the wrong one for R1 and insufficient for R2* -- R386.

**Not gates on step 5, into the next report's Carried section:** R390, R391,
R392, R393, R383, R370, R371, R372, R373, R374, R362, R363, R364, R354, R355,
R356, R357, R347, R348, R349, R350's second half, R330, R331, R332, the
section 9 status-versus-subject disagreement, R321, R322, R300, R291, R292,
R281, R231, R244, R245, R275, R223, R224, R230, R261, the underlying gap in
R276, R277, R262, R264, R266, the two R248 residues, R249-R252, R225-R228,
R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 35 new entries in one file, all unseen by the
implementer, every `measured=` taken at `d273acf` by running the shipped
`offending()` BEFORE the `expect=` beside it was written.**

**The coverage measurement, stated plainly: of my 35 new entries the shipped
scanner does what the entry requires on 17, and 18 are misses. Of the 25
entries that ask for DETECTION, 7 are correct and 18 are missed.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+35 (225 to 260), 17
  correct.** `python scripts/corpus_figures.py` reads `260 260 106 154 40`;
  `tests/test_marker_exemption_corpus.py` is **114 passed** at my corpus commit
  against 97 at `d273acf`, and the whole suite there is **2131 passed, 0
  failed, 0 skipped**.
* **FOURTEEN OF THE EIGHTEEN MISSES ARE TWO AXES OF ONE RULE**, the rule this
  round shipped: an identity table with no side, and an operand reach of one
  level. R389.
* **BOTH BOUNDARIES ARE PINNED FROM BOTH SIDES rather than sampled on one.**
  `DECLARED << 0` clean against `DECLARED << 1` caught; `* 1`, `/ 1`, `+ 0`,
  `** 1` clean against `* 1_000` and `* 0x10` caught. The new decision rule's
  own threshold is written down in data now, so a change that moves it cannot
  move it quietly.
* **THE HATCH CONTROLS PASS AND THEY MATTER MOST.** The `# not-a-tolerance:`
  marker reaches the new CQ3 species on one line and split across five lines,
  and R381's `isfinite` clause leaves `float("nan")`, `-float("inf")` and
  `float("1e400")` clean. A new rule the hatch cannot reach makes a correct
  file unfixable, which is worse than any miss.
* **THREE OLD ENTRIES MOVED FROM ESCAPING TO CORRECT**, isolated by running
  the `7fd7155` scanner over the improvements as a control: exactly R381's one
  and R384's two. Three findings named three entries, and three moved.
* **One new axis nobody has looked at**: the bound chosen by a conditional
  expression, `err < (DECLARED if strict else 1e-09)`, clean.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands.

**Forty-four rounds have found no element defect, and this round does not
either.** `floatfea/` is byte-identical for the nineteenth consecutive round
and its two CI jobs are green on a machine nobody here controls. It still
means "not yet contradicted": the determinism legs did not run at this commit
either, ladder 5 has printed `OK -- 0 director(y|ies) ran` every time it has
run, and V5.1 against CalculiX is the witness that has not spoken.
