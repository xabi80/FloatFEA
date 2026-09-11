# Review — F2 step 5
Reviewed commit: 23cfd7a150a4baf4cce98860c5626d78202e9a76
Verdict: HOLD

**Reviewed commit: `9cec13e`.** Report revision 16, `Answers: verdict 41 @ f04e3c5`.
**The `Reviewed commit:` line stamped above this one by `scripts/write_verdict.py`
is HEAD at the moment of writing -- my corpus commit `23cfd7a` -- not the commit
judged.** That is R373 below; read `9cec13e`.

Tests: **2045 passed, 0 failed, 0 skipped** (my run at `9cec13e` on a clean
tree, `python -m pytest -q`, 502.51 s, Python 3.13.15 on Windows).
`pytest --collect-only -q` gives **2045**, so nothing is skipped and nothing
silently uncollected. **Both standing reds are genuinely gone** -- the first
zero-failure whole-suite run of this milestone, reproduced rather than
accepted. Rung 1 is **1053 passed**.

**Commits: `46cf887`, `059cf5b`, `ea657dc`, `502e0de`; `process:` `8830041`.
Report `9cec13e`.**

**Item 1b.** Revision 16's header at line 5548 reads `Answers: verdict 41 @
f04e3c5`; the last commit touching the verdict file is
`f04e3c561cc783ae95d508a7a5a2a141f9f8a584`. It is the latest. **Passes.**

## CI, item 3b -- AND IT IS GREEN, AT THE COMMIT I AM REVIEWING

**The constraint is gone and I did not take that on report. I dispatched a run
at `9cec13e` myself and waited for it.**

```
cmd  gh run list --commit 9cec13e --json name,conclusion,workflowName
out  []       -- no run existed. `docs/reports/**` is in paths-ignore, so the
     report commit creates none, and the implementer's two runs are at
     `f04e3c5` and `502e0de`. Under CA2 that is an UNAVAILABLE check.
cmd  gh workflow run ci.yml --ref F2      (origin/F2 was at 9cec13e)
out  run 34658132995, workflow_dispatch, head_sha 9cec13e
cmd  gh api .../runs/34658132995 and .../jobs
out  conclusion SUCCESS. 13 of 13 jobs success: "the verification ladder",
     ten "CI determinism -- leg", "CI determinism -- ten legs agree",
     "lint, unit and guards".
     ladder 4  89 collected, 0 failed     ladder 6  4 collected, 0 failed
     unit tests 88 passed        guards and meta-tests 696 passed (445 s)
     ladder 5  "OK -- 0 director(y|ies) ran" -- the declared-empty rung; V5.1
               against CalculiX still has not run, and "not yet contradicted"
               still binds.
judge THE FIRST GREEN CI OF THIS MILESTONE, ON LINUX, AT THE REVIEWED COMMIT.
     Nothing in the local run and nothing in CI disagree. This is not why the
     step holds.
```

**And the ten-legs job is a gate now, which I checked by reading its output
rather than its status.**

```
cmd  gh run view --job <ten legs agree> --log      (run 34658132995)
out  ten rows, THREE DIFFERENT CPU MODELS -- AMD EPYC 7763, AMD EPYC 9V74,
     Intel Xeon 8370C -- core type Haswell on all ten, hash
     0415d1196b56a92ac63ba52ada55dcfbc53fbdd512c450548bf071db6560d9fe on all
     ten, and "4 collected, 0 failed" on all ten.
     "ten of ten identical: 0415d1196b56 core Haswell"
judge THE REGRESSION LINE IS READ NOW. `502e0de` is a real repair of a real
     hole the implementer found in their own gate by reading a run instead of
     the code, and it is the best piece of work in this round.
```

**The run the report calls "this round's head" is not this round's head, and
it is red.**

```
cmd  gh api .../runs/34655464372   -- the run section 4 describes twice
out  head_sha 502e0deff437..., the report's PARENT. HEAD is 9cec13e.
     "lint, unit and guards" FAILURE: guards and meta-tests, 12 failed,
     678 passed -- every failure a report-site guard (R358, R363) at a commit
     where revision 16 did not yet exist.
judge THE DIAGNOSIS IN SECTION 4 IS RIGHT AND THE LABEL IS WRONG. Nothing
     turns on it now because I ran the real head. R372.
cmd  gh api .../runs/34643760694/jobs         (at b1cfceb, verdict 41's commit)
out  unchanged: 4 jobs, runner_name "", steps [], the billing annotation.
     Still CK2 `unavailable -- allowance exhausted`, as section 0a says.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff f04e3c5..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- nothing in this range touches either. No STOP-class finding.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                     -- the instruction's own expectation
cmd  git diff f04e3c5..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
cmd  git diff f04e3c5..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat f04e3c5..HEAD -- floatfea
out  (empty) -- seventeen rounds
cmd  git show --stat on each of the six commits
out  `8830041` is standalone and cites R361 in its subject; it touches
     `.github/workflows/ci.yml` and `tests/test_report_carried.py` and nothing
     else. No commit mixes process with code.
```

## Carried

Verdict 41 held on R359, R360 and R361. **One closes. One closes at its
load-bearing half and republishes four figures I cannot reproduce. One closes
at one of its two named sites and the replacement opens a hole of its own.** I
ran every closing condition rather than reading it.

- **R359 -- ANSWERED at the words of its condition, and the mechanism works.**
  `_triples_in_the_file()` exists, it is one regex over the bytes, and the
  parsed set is compared field for field. My targeted re-scope from verdict 41
  now fails by name, reproduced in a clean clone:

```
cell reviewer's ablation (a) `ast.walk(inner)` -> `ast.walk(inner.right)`,
     then each parser edit in turn, clean clone, restored between rows
out  at 9cec13e:  CLEAN 64 passed / (a) 2 failed 62 passed /
     (a)+R351 drop 1 failed / (a)+R359 re-scope 1 failed / RESTORED 64 passed
     at ca57d8a:  CLEAN 57 / (a) 2 failed 55 / (a)+drop 1 failed 55 /
     (a)+re-scope 56 PASSED  -- green before the repair, red after it
judge EVERY ROW OF SECTION 1 REPRODUCES TO THE DIGIT, at both commits. The
     door R359 named is shut.
judge AND THE DOCSTRING IS HONEST ABOUT WHAT IT DOES NOT PROVE -- the third
     attempt, and the first I cannot fault on its own terms, except that it
     is still one field short. R365.
```

- **R360 -- ANSWERED at its load-bearing half, NOT at the half the report
  chose to add.** Section 1's rows are re-run and correct (above). Section 2
  then publishes four MORE figures for an ablation named only in prose, and
  the attribution is refuted by the verdict it cites. That is R368, and it is
  the direct answer to the implementer's question: **yes, publishing both is
  worse than withdrawing to the one sufficient sentence.**

- **R361 -- ANSWERED at one of its two named sites, and the replacement is
  looser in the one direction the old rule's own docstring calls the point.**

```
cmd  the collected-set claim, re-taken at my own corpus commit
out  tests/test_marker_exemption_corpus.py 64 passed -> 77 passed. The corpus
     tree IS parametrisation data; the measurement half of R361 reproduces.
cmd  git show 8830041 -- .github/workflows/ci.yml
out  `tests/corpus/**` is out of paths-ignore. The trade is taken, not hidden.
judge THE FIRST NAMED SITE IS REPAIRED. `:1079-1085` is gone; what stands in
     its place quotes CO3's sentence and refutes it with the number.
judge THE SECOND NAMED SITE IS BYTE-IDENTICAL. R366.
judge AND THE NEW ANCHOR LETS THROUGH THE CASE THE OLD ONE CAUGHT. R367.
```

- **R362, R363, R364 -- OPEN at 4a, correctly listed in section 5** and rowed
  in section 8. R364 stands and strengthens: see the corpus measurement below,
  the fifth consecutive batch to miss two thirds of the detection axes.

- **R354, R355, R356, R357 -- OPEN at 4a, correctly listed.** R356 is R351's
  species in four more readers; R365 makes that family larger again.

- **R347, R348, R349, R350's second half -- OPEN at 4a, correctly listed.**
  R348 is no longer only loud: the site parser's gap is load-bearing now, and
  R366 is the demonstration.

- **R330, R331, R332 -- OPEN at 4a, correctly listed.** R332 honoured again:
  nothing reads `g21_rigid_body_frames.txt`, so I added nothing to it.

- **R231, R244, R245, R275 -- OPEN, and the block they were declared behind is
  LIFTED.** I verified the render's provenance independently:

```
cmd  sha256 of docs/milestones/F2_figures.md at HEAD
out  0415d1196b56a92a..., 2857 bytes, LF
cmd  gh api .../artifacts/10285307984/zip  (run 34654570891, leg 1), unzip,
     sha256 the F2_figures.md inside it
out  0415d1196b56a92a..., 2857 bytes -- IDENTICAL, its figures.sha256 claims
     the same, and its regression.txt says "4 collected, 1 failed"
judge THE BYTE-FOR-BYTE CLAIM IS TRUE AND I CHECKED IT FROM THE ARTIFACT, not
     from the leg's own number. Re-confirmed at run 34658132995 by ten legs on
     three CPU models. CG2 is done.
cmd  python -m pytest tests/test_plan_figures.py -q
out  104 passed
```

- **R223, R224 -- Q7 is not claimed by the report and I am not opening it, but
  the condition it waits on is now MET and measured**: green CI at a reviewed
  commit, run `34658132995` at `9cec13e`. Recorded so the next round need not
  re-establish it. Opening Q7 is the plan's business, not a verdict's.

- **R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement is unchanged and
  stays at 4a.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** The
  generated table still expands a range by its endpoints only, so R250, R251,
  R226, R227, R264 and R266 have no row; R348's territory, unmoved.

## Findings

**R365. (BLOCKS -- my adversarial case passed when it should have failed. The
second reader reads three of the four fields, and the one it does not read is
the one the gate's assertion actually runs on.)**
`tests/test_marker_exemption_corpus.py:42-47`, `:157-168`, `:169`, `:315-323`,
`:337-355`.

```
code :42  "So the file is read TWICE, by readers that share nothing but the
     :44   path, and every field the decision reads is compared: the ids, the
           `expect` and the `measured`."
judge THE DECISION READS FOUR FIELDS. `test_the_exemption_window_gives_the_
     required_verdict` writes `src` to a file and hands it to `offending()`,
     and `_measured_misses()` does the same. `src` is THE INPUT THE SCANNER
     RUNS ON, and `_TRIPLE` captures `id`, `expect` and `measured` only.
cell TWO EDITS, BOTH IN FILES THE IMPLEMENTER OWNS, clean clone at 9cec13e:
     (a) `ast.walk(inner)` -> `ast.walk(inner.right)` in
         `_literal_thresholds_inside` -- the same genuine, plausible
         tightening verdicts 40 and 41 both used
     (e) TWO LINES in `_entries()`, right after `src = fields[3]...`:
             if "raised_to_a_literal" in got["id"]:  # normalise operand order
                 src = src.replace("ROUNDOFF_IDENTITY ** 2.0",
                                   "2.0 ** ROUNDOFF_IDENTITY")
out  after (a) alone
       pytest tests/test_marker_exemption_corpus.py    2 failed, 62 passed
       named: detect_declared_raised_to_a_literal, and the regression test
       names it with its blame commit
     after (a) and (e)
       pytest tests/test_marker_exemption_corpus.py    64 passed
       python -m pytest -q   (the WHOLE SUITE, 443.89 s)
                                                       2045 passed, 0 failed
       WHICH IS THE CLEAN TREE NUMBER EXACTLY (2045 passed, 0 failed).
judge NO CORPUS EDIT. NO FIELD REWRITTEN. `_triples_in_the_file()` agrees
     field for field, the count agrees, the partition holds, and
     `PLANTED_ESCAPES` is unchanged -- because nothing about `id`, `expect` or
     `measured` moved. The shape is still ASSERTED; it is asserted against a
     module that is no longer the reviewer own text.
judge THIS IS THE THIRD LEAF OF THE SAME DOOR AND THE PATTERN IS THE FINDING.
     R351 removed the entry. R359 rewrote the classification field. R365
     rewrites the artefact under test. Each repair closed the leaf it was
     shown and published a sentence claiming the door; the sentence has been
     wrong three times, and the code one field short three times.
judge WHAT IS NOT WRONG, AND I CHECKED IT: a GENERIC version is caught. A
     blanket `src = "assert err < 1e-09"` for every entry reddens the exempt
     controls at once. It is the TARGETED rewrite that is invisible, which is
     the one an adversary writes.
judge AND IT COSTS NOTHING THIS TIME. R351 and R359 each moved the pass count
     by exactly one; this moves it by zero, because the entry stays in the
     parametrisation and passes there.
```

**Closed when** either (i) the second reader reads the source as well -- the
regex extended to capture `src=` to end of line, the decoded module compared
byte for byte against what `_entries()` hands to `offending()`, with a cell
showing it red on a one-entry source rewrite and green on the clean tree -- or
(ii) the docstring at `:42-47` stops saying "every field the decision reads is
compared" and says what is true: three of the four fields are read twice, the
fourth is the module the scanner is actually run on, and a targeted rewrite of
it in `_entries()` is not detected. If (ii) is chosen, say it at `:157-168`
too, which makes the same claim in other words. **Either closes it; what may
not stand is the sentence and the code disagreeing for a third round.**

**R366. (BLOCKS -- R361's condition named two sites and one of them is
byte-identical. The refuted sentence is still shipped, asserted, fifteen lines
below its own withdrawal.)** `tests/test_report_carried.py:1142-1157`.

```
cmd  git show b1cfceb:tests/test_report_carried.py | sed -n "1132,1146p"
     against the same block at HEAD (now :1142-1156)
out  IDENTICAL. Not a word changed.
code :1154 "A reviewer commit carries no code and changes nothing the count
     :1155  describes, so the count stays true across it."
judge THAT IS THE SENTENCE R361 REFUTED, in the file R361 named. A reader who
     reaches the assertion reads the withdrawn justification, not the
     withdrawal.
code :1142 "CO3, R358: REVIEWER COMMITS DO NOT COUNT TOWARD THE DISTANCE"
judge AND THAT ONE IS NOW FALSE ABOUT THE CODE BENEATH IT. `_report_anchor()`
     counts every commit between the named sha and the report commit, the
     reviewer own ones included, and the commit message for `8830041` says so.
     The comment describes the rule it replaced.
cmd  import test_report_carried, print every SITES row whose finding is R361
out  CLAUDE.md:0, tests/corpus/...txt:0, tests/test_marker_exemption_corpus.py:0,
     tests/test_report_carried.py:1079 .. :1085 -- and nothing at 1132-1146
judge SO THE GUARD NEVER ASKED. `_SITE` at :138 requires a filename before a
     line range, and verdict 41 wrote the second site as a bare `:1132-1146`
     continuation. The site is absent from `SITES`, absent from section 7,
     and it is the one that was left. R348 species with a consequence: the
     site check domain came from a parser that cannot see half of what the
     verdict wrote.
```

**Closed when** `:1154-1157` says what was measured -- that a corpus-only
commit moves the collected suite (4 at `40667c6`, 7 at the round that
followed, 13 at mine this round), and that this is why the trees are no longer
exempt -- **and** `:1142-1151` either describes the rule now in the file or is
deleted as history. The parser gap is 4a and goes with R348; the two comment
blocks are this step.

**R367. (BLOCKS -- a causal sentence in a `process:` commit, refuted by one
controlled cell. The new anchor is stricter in the direction R361 named and
LOOSER in the direction the rule exists for.)**
`tests/test_report_carried.py:1095-1115`, `:1158-1175`; the commit message of
`8830041`; report section 3.

```
code msg  "THE REPLACEMENT IS STRICTER WHERE IT MATTERS and quieter where it
           does not"
code :1156 "What still fails is an implementer commit after the measurement,
     :1157  which is the thing R319 was written to catch."
cell ONE VARIABLE: a code commit landing AFTER the report commit, everything
     else held. Clean clone, branch off 9cec13e, one new test file with two
     collected tests, committed.
cmd  pytest --collect-only -q   before / after
out  2045 -> 2048. The report line still names `502e0de`, now TWO commits
     back, and still says 1821 with 218 excluded.
cmd  pytest tests/test_report_carried.py -k whole_suite   under the NEW rule
out  2 passed
cmd  the same with only tests/test_report_carried.py checked out at 8830041^
     -- the OLD rule, one variable, nothing else touched
out  1 failed:  "names `502e0de`, which is 2 implementer commit(s) behind
     HEAD"    assert 2 <= 1
judge THE OLD RULE CAUGHT IT AND THE NEW ONE DOES NOT. `_report_anchor()`
     freezes at the last commit touching the report, so nothing committed
     after the report can raise the distance -- including an implementer
     commit, which is the case `:1156` says is still caught and which R319
     was written for. The exemption R361 removed for the corpus has been
     replaced by a blanket exemption for everything after the report.
judge THE FIX IS NOT A REVERT AND I AM NOT ASKING FOR ONE. Anchoring the
     SENTENCE on the report commit is right; what is missing is that the tree
     under review is HEAD. Both can hold: distance from the named sha to the
     anchor <= 1, AND the anchor is HEAD or the parent of HEAD.
judge AND THE CELL THAT WOULD HAVE ISOLATED IT IS THE ONE THE ROUND DID NOT
     RUN. Section 3 measures green at the report, corpus and verdict commits
     -- three cases in the direction that was loosened -- and none in the
     direction the claim is about.
```

**Closed when** the rule also bounds the anchor against HEAD -- one extra
`rev-list --count anchor..HEAD` with its own threshold and message -- with the
cell above run both ways at the commit that publishes it, **or** "stricter
where it matters" is withdrawn and the file states plainly that a commit
landing after the report is not counted, so the suite line describes the
report tree rather than the reviewed one. Four lines, or a sentence.

**R368. (BLOCKS -- R360's repair republished four figures I cannot reproduce,
attached to an attribution the cited verdict contradicts.)** Report section 2.

```
code s2 "verdict 39's `or True` on the `isinstance` line, which is what
         produced the published threes"
code s2 "cmd the same four rows with `or True`, at `ca57d8a`
         out 57 passed / 3 failed 54 passed / 3 failed 53 passed / 57 passed"
cmd  git show 2b6435d:docs/reviews/F2/step-5.md | sed -n "263,268p"
out  verdict 39 own cell: "`_literal_thresholds_inside` narrowed by one line
     so a declared name on the LEFT of a BinOp is no longer read ...
     3 entries regress ... tests/test_marker_exemption_corpus.py ->
     4 failed, 70 passed."
judge VERDICT 39 DESCRIBES NO `or True` AND PUBLISHES NO 3/54. Its cell is a
     narrowing of the same function the reviewer ablation narrows, and its
     own outcome is "4 failed, 70 passed".
cmd  the only literal reading I can construct -- `or True` on the
     `isinstance(n, ast.Name)` line at :174 -- run at ca57d8a, four rows
out  57 passed / 5 failed 52 passed / 5 failed 51 passed / 4 failed 52 passed
cmd  git diff --stat 389d416..ca57d8a -- tests/test_no_tolerance_literals.py
out  (empty) -- the scanner did not move between the two commits, and the
     corpus only GREW, so a shape that regressed at 389d416 must still
     regress at ca57d8a. Three regressions and one regression are not one
     edit.
judge SO THE ROUND REPLACED FOUR UNREPRODUCIBLE FIGURES WITH FOUR MORE. They
     are honestly labelled as archaeology and the load-bearing cell beside
     them is now exact -- but BF0 has no archaeology exemption, and the one
     thing a reader wants from section 2 is the diff line that produced the
     threes.
judge THE IMPLEMENTER ASKED DIRECTLY AND THE ANSWER IS YES: publishing both
     is worse. Section 1 is sufficient.
```

**Closed when** section 2's four rows and the "verdict 39's `or True`"
sentence are deleted, leaving the statement R360's condition called true and
sufficient -- the pair is red at `test_every_entry_reaches_the_assertions` and
was green before CO0, with section 1's rows as the evidence -- **or** the exact
diff hunk that produces 3 failed / 54 passed at `ca57d8a` is pasted so a
reader can run it. Deleting is cheaper and, I think, right.

**R369. (recordable, 4a) The determinism verdict job's new red-check reads
`failed` and not `collected`, so "0 collected, 0 failed" is green there.**
`.github/workflows/ci.yml:277-279`. The predicate is
`not line.startswith("0 failed") and ", 0 failed" not in line`, and a leg that
collected nothing writes `0 collected, 0 failed` before exiting. The leg own
step does refuse zero collection at `:144-145`, so the RUN still goes red --
but the job named "ten legs agree" would again report success under ten red
legs, which is the exact shape `502e0de` was written to remove, one notch
over. "Empty parameter set is an error, not a skip" applies to a gate own
input. One extra clause.

**R370. (recordable, 4a) A published gate row stopped describing the
repository when the canonical render landed, and nothing in the suite reads
it.** `docs/closure/F2-step4.md:22` says the dropped-shear-parameter defect is
"below the declared resolution on 7 of 158". `059cf5b` moved
`below_ceiling_dropped_shear_parameter` to `8 of 164`.
`tests/test_plan_figures.py` checks `docs/milestones/F2.md` against the render
and does not reach `docs/closure/`. BP0 asks that every figure citing a rule
that moved be regenerated or withdrawn in the same commit; the commit message
lists four figures that moved and this is a fifth it does not mention, with
`exempt_total`, `exempt_by_defect`, `boundary_margin_bases`,
`boundary_margin_refused` and `calibration_ulp_histogram` alongside it. All are
correct in the render. The closure artifact is what now disagrees.

**R371. (recordable, 4a) The golden was re-indented from one space to two in
the same commit that added two pairs, so the diff reads 57 insertions and 55
deletions for a change the message calls additive.** `ea657dc`,
`tests/regression/g22_exempt_pair_responses.json`. **The claim is true** -- I
parsed both revisions: 55 keys to 57, none removed, no recorded value moved by
a single bit -- but a reader cannot see that in the diff, which is the one
place a golden change is audited. Reformat separately from content, or the
audit is "take my word for it".

**R372. (recordable, 4a) "The dispatch run at this round's head" names a run
at the report parent.** Report section 4, twice. `34655464372` is at
`502e0de`; HEAD is `9cec13e`; and that run's `lint, unit and guards` job is a
FAILURE. Moot now because I dispatched and read the real one, but as written
it tells a reader CI was exercised at the commit they are holding.

**R373. (recordable, 4a) `scripts/write_verdict.py:29,55` stamps
`git rev-parse HEAD` as "Reviewed commit", and BE3 requires the corpus to be
committed before the verdict.** So the machine-readable header of every
verdict in this milestone names the reviewer corpus commit, not the commit
judged: verdict 41 says `30de97a` on line 2 and `b1cfceb` on line 5. Two
answers in one file to the question CA2 turns on. The script is not a path I
may write; recorded so 4a can give it `--reviewed <sha>`.

**R374. (recordable, 4a) The scanner coverage is two thirds unseen axes for
the fifth consecutive batch, and the shape of the miss has not changed.** My
27 entries are 13 correct and 14 missed; restricted to the 21 detection
entries it is 7 correct and 14 missed, the same two thirds the last four
batches measured. The misses are not exotic: a number inside a string (`exec`,
`eval`), a number spelled as an integer (`Fraction(1, 1000000000)`,
`maxulp=4`, `decimal=9`), and four more places a default lives. R364 stands;
this is the fifth data point, and it is evidence that the planted-list
approach has a ceiling.

## Tolerances touched

**None.** `git diff f04e3c5..HEAD -- floatfea/tolerances.py` is empty, and so
is the diff over all of `floatfea/`.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| everything in `tolerances.py` | unchanged | -- | -- | the diff over the file is empty |
| `EXEMPT_RESPONSE_DRIFT_ULP` | unchanged | dimensionless, ULP of the recorded response | the golden set grew by two pairs and no recorded value moved by one bit | `tests/regression/g22_exempt_pair_responses.json`, verified by parsing both revisions |
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (unchanged) | dimensionless, ULP of the channel own amplitude | `3.0`, injected beyond the site clean deviation | `docs/milestones/F2.md:1116-1152`, `tolerances.py:1024-1035` |

```
cmd  the golden, old and new, parsed and compared key by key
out  55 -> 57 keys, removed [], added the two ck_length_thousand_km pairs,
     values moved {}    -- ADDITIVE, exactly as the commit message claims
judge NO NUMBER IN ANY OF THE SIX COMMITS FUNCTIONS AS A TOLERANCE. The
     workflow predicate `", 0 failed" not in line` is a string test, not a
     threshold; `distance <= 1` is unchanged in value and changed in DOMAIN,
     which is R367.
cmd  my whole-suite run includes the shipped literal scanner over tests/ and
     scripts/
out  2045 passed -- no undeclared literal entered the tree this round
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

What moved this round is real and I want it recorded before the holds: the
whole suite is **zero failures for the first time in this milestone**, both
standing reds are genuinely closed, the canonical render byte-for-byte
provenance checks out against the artifact I downloaded myself, and **CI is
green at the reviewed commit** -- run `34658132995`, thirteen of thirteen
jobs, ten legs on three CPU models agreeing on one hash with the goldens
passing on every one. The implementer also found a hole in their own gate by
reading a run instead of the code, and fixed it. `floatfea/` is unchanged for
the seventeenth round and rung 1 is **1053 passed**.

**What holds is one door on its third leaf and three sentences a command
refutes.**

1. **R365 -- the corpus gate decision runs on a field the second reader does
   not read.** Genuine scanner regression plus two lines in `_entries()` that
   rewrite the module under test for one entry: whole suite **2045 passed, 0
   failed**, identical to the clean tree, corpus untouched, every compared
   field agreeing. The docstring says every field the decision reads is
   compared. It reads four and compares three.
2. **R366 -- R361's second named site is byte-identical**, and the refuted
   sentence is still shipped fifteen lines below its own withdrawal. The site
   check never asked, because `_SITE` cannot parse the bare `:1132-1146` form
   verdict 41 wrote.
3. **R367 -- the new anchor does not count anything committed after the
   report, including an implementer commit.** One controlled cell: a code
   commit on top of `9cec13e` adding two collected tests takes the suite from
   2045 to 2048; the old rule goes **1 failed**, the new rule **2 passed**.
   "Stricter where it matters" is the sentence.
4. **R368 -- section 2's four `or True` rows do not reproduce and the verdict
   they are attributed to describes a different edit with a different
   outcome.** Answering the question asked: withdraw them.

R365 is the one that matters. Three rounds have each shut the leaf they were
shown and published a sentence claiming the door, and the sentence has been
wrong every time. **I would rather see repair (ii) -- the docstring reduced to
what the code does -- than a fourth field comparison followed by a fourth
claim.** If the source is compared too, then say only that four of four fields
are compared, and that `_planted_caught`, `_did_catch` and the partition
remain the implementer to edit.

**Not gates on step 5, into the next report Carried section:** R369, R370,
R371, R372, R373, R374, R362, R363, R364, R354, R355, R356, R357, R347, R348,
R349, R350's second half, R330, R331, R332, the section 9
status-versus-subject disagreement, R321, R322, R300, R291, R292, R281, R231,
R244, R245, R275 (now unblocked -- the render is canonical and CI is green, so
the Q8 values can be taken), R223, R224 (Q7's condition is met and measured;
opening it is the plan call), R230, R261, the underlying gap in R276, R277,
R262, R264, R266, the two R248 residues, R249-R252, R225-R228, R232, R233, and
everything already at 4a.

**Adversarial corpus (BE3): 27 new entries in one file, all unseen by the
implementer, every `measured=` taken at `9cec13e` by running the shipped
`offending()` before the `expect=` beside it was written, and every line
round-tripped through the corpus escape before it was measured** -- a first
attempt at this batch was silently truncated at the first newline escape and
would have planted twenty-seven one-line modules that scan clean for the wrong
reason. The generator asserts the round-trip now.

**The coverage measurement, stated plainly: of my 27 new entries the shipped
scanner does what the entry requires on 13, and 14 are misses. Of the 21
entries that ask for DETECTION, 7 are correct and 14 are missed.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+27 (169 to 196), 13
  correct.** `python scripts/corpus_figures.py` reads `196 196 71 125 30`, and
  `tests/test_marker_exemption_corpus.py` is **77 passed** at my corpus commit
  against 64 at `9cec13e`.
* **The largest axis is a tolerance that is not a float node at all.**
  `exec("TOL = 1e-09")` and `eval("1e-09")` carry it inside a string;
  `float(Fraction(1, 1000000000))`, `assert_array_max_ulp(maxulp=4)` and
  `assert_almost_equal(a, b, 9)` spell it with integers. Five of five missed.
* **The machine constants that are not `eps`**: `math.ulp(1.0) * 1e07` and
  `np.finfo(np.float64).tiny * 1e300`, the recorded `eps` species in two
  spellings nobody scanned. Two of two missed.
* **Four more places a default lives**: a
  `dataclasses.field(default_factory=...)`, a `typing.Annotated` metadata
  slot, an `argparse` default, and `pytest.fixture(params=[1e-09])`. Four of
  four missed.
* **Three name resolutions that cross a statement**: an inherited class
  attribute, a starred tuple unpacked into a call, and a literal in a `match`
  MAPPING PATTERN rather than in an expression. Three of three missed.
* **What IS caught, and it matters as much**: an undeclared `atol=` beside a
  DECLARED `rtol=` in one call, a plain `assert` inside a `unittest.TestCase`,
  an `async def` test, a backslash-continued comparison, and a boolean mask
  index. Five of five.
* **Both marker-direction controls pass**: a marker with no colon and a marker
  spelled with underscores do NOT exempt.
* **All six hatch controls pass, and they matter most**: the marker still
  works on a `for` header, on an `assert` nested in a `with` block, on a
  backslash-continued statement, on a dict comprehension, on the closing line
  of an `or` chain, and on a `global` rebinding. A hatch that stops working is
  worse than any miss.
* **My corpus commit is green everywhere I checked it**, which is R361 own
  claim tested from the outside: `tests/test_report_carried.py` and
  `tests/test_report_numbers_are_sourced.py` **198 passed**,
  `tests/regression` **4 passed**, `tests/test_plan_figures.py` **104
  passed**, all at `23cfd7a`.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands.

**Forty-two rounds have found no element defect, and this round does not
either.** The difference is that for the first time that sentence rests on
something other than the author own machine: ladder 4 is
`89 collected, 0 failed` and ladder 6 is `4 collected, 0 failed` on Linux, at
the reviewed commit, on a runner nobody here controls. It still means "not yet
contradicted" -- ladder 5 printed `OK -- 0 director(y|ies) ran`, and V5.1
against CalculiX is the witness that has not spoken.
