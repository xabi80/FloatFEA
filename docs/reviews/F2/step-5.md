# Review — F2 step 5
Reviewed commit: 40667c61286c357ed1095a23f9bbca009578bcc9
Verdict: HOLD

**Reviewed commit: `a93d505`.** Report revision 14, `Answers: verdict 39 @ 2b6435d`.

Tests: **2067 passed, 2 failed, 0 skipped** (my run at `a93d505` on a clean
tree, `python -m pytest -q`, 432.82 s, Python 3.13.15 on Windows).
`pytest --collect-only` gives **2069**, so nothing is skipped and nothing
silently uncollected. The two failures are the two section 7 names, both behind
the canonical re-render, both mine from earlier corpus rounds.

**Commits: code `2f21b54`, `d08a3e4`, `c6cf348`, `b8941b6`, `7ba1e9d`,
`8beb0e4`, `c92f3b3`, `ff6b61a`. Report `a93d505`.**

**Item 1b.** Header line 4652 reads `Answers: verdict 39 @ 2b6435d`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`2b6435d58390ea23ca627ea9aecadff55a1de7bb`. It is the latest. **Passes.**

**CI, item 3b, AT THE COMMIT I AM REVIEWING -- `a93d505`, NOT `389d416`:
`unavailable -- allowance exhausted`, the CK2 third state.**

```
cmd  gh run list --limit 8 --json headSha,conclusion,event,databaseId
out  34630780377  push  failure  @ a93d505   -- and no pull_request twin
cmd  gh api repos/.../actions/runs/34630780377/jobs
out  4 jobs. "lint, unit and guards" and "the verification ladder":
     conclusion failure, runner_name "", steps 0, started 17:59:44 and
     completed 17:59:46 -- two seconds.
     "CI determinism -- leg" and "-- ten legs agree": SKIPPED.
cmd  gh api .../check-runs/<id>/annotations  for both failures
out  "The job was not started because recent account payments have failed or
     your spending limit needs to be increased" -- both of them
judge CK2 THIRD STATE. Neither red nor green; nothing claimed from it in
     either direction, and it does not HOLD by itself.
cmd  gh api .../runs/34546580003/jobs   (the last run that EXECUTED, @ 8942cdc)
out  6 of 6 ladder jobs success; "guards and meta-tests" FAILURE; rest green
cmd  git diff --stat 8942cdc..a93d505 -- tests/verification scripts .github
out  NOT empty: 8 files, 717 insertions. ci.yml alone is 296 lines changed.
judge SO THAT RUN DOES NOT DESCRIBE THIS TREE. Recorded as unavailable.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
judge AND THE COMMIT THE REPORT SECTION 0 DESCRIBES IS NOT THE ONE UNDER
     REVIEW. That is R352, below, and it is the fourth round running.
```

**My own instructions (4b) and the conftest pathspec (4c).**

```
cmd  git diff 2b6435d..a93d505 -- .claude docs/SUPERVISOR.md
out  (empty) -- no commit in this range touches either. Nothing to read.
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 2b6435d..a93d505 -- tests/conftest.py 'tests/**/conftest.py'
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
cmd  git diff 2b6435d..a93d505 -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 2b6435d..a93d505 -- floatfea
out  (empty) -- fifteen rounds now
```

**What held, reproduced at my run**: `ruff check floatfea tests scripts` clean;
`black --check` clean over 87 files; `mypy floatfea` clean over 25 source files;
`sh scripts/run_rung.sh full:tests/verification/rung4` gives
`89 collected, 0 failed`, the report figure to the digit; the report guards
`tests/test_report_carried.py`, `test_report_numbers_are_sourced.py`,
`test_report_guard_states.py` are **260 passed** at `a93d505`, so sections 8
and 9 answer the guard rather than a second opinion; `scripts/suite_count.py`
at `a93d505` prints `1807 passed, 2 failed, excluding 260`, and
1807 + 2 + 260 = 2069 = my collection exactly.

## Carried

Verdict 39 listed six blocking items. **Five close (R341, R342, R343, R344,
R345). One does not (R346), and it is the same sentence, wrong in the same
way, for the fourth round running.** The five that close are the best-executed
set of repairs this step has produced: two of them I could not defeat, and the
one I did defeat I defeated through a door the condition did not name.

- **R341 -- CLOSED at everything its condition named, and the asymmetry is
  real. I measured it by exercising it rather than by reading the code.** The
  residue my break found is **R351**, a new finding, not a reopening.

```
cmd  grep -n "KNOWN_MISSES" tests/test_marker_exemption_corpus.py
out  two hits, both historical narration, no live claim. The map and its
     test are gone.
cell the scanner narrowed so a declared name on the LEFT of a BinOp is no
     longer read -- a plausible tightening               (my run, a93d505)
out  2 failed:
       test_the_exemption_window_gives_the_required_verdict
         [detect_declared_raised_to_a_literal]
       test_no_shape_that_was_CAUGHT_when_planted_escapes_now
     and the aggregate message names the shape with git blame commit.
cell the report own stated cell, the whole BinOp branch off
out  2 regressions, exactly the report figure. Reproduced.
judge AND THERE IS NO LONGER A LINE TO WRITE. PLANTED_ESCAPES is derived from
     `measured=`, which is in a file `.claude/hooks/protect-reviews.sh`
     refuses me -- I read the hook, and it covers shell redirects and `cd`,
     not just Edit. The three lines that cleared this last round clear
     nothing.
cell THE DECODE IS RIGHT AND I CHECKED IT AGAINST THE CORPUS OWN
     ARITHMETIC, not against the report. The batch header at :205-206 says
     "10 new entries, 2 agree with expect, 8 do not". That batch is 8
     `measured=clean`, 1 `caught`, 1 `caught_but_...`. For the header to
     reconcile, `clean` must mean "returned nothing" and `caught_but_` must
     mean "returned something" -- which is exactly `_did_catch()`.
     `clean` as a synonym for `exempt` is CONFIRMED, independently.
cell AND I EXERCISED THE ASYMMETRY WITH 22 SHAPES THE IMPLEMENTER HAS NEVER
     READ. 18 of them are misses. They arrive as DERIVED growth: no line
     written, no provenance typed, no ceremony.
out  tests/test_marker_exemption_corpus.py  56 passed  (52 before)
     Last round the identical act left that file 16 failed / 78 passed and
     demanded fifteen hand-written entries. THAT is the measurement.
cmd  the report section 5 "forty-one" attribution
out  "measured at forty-one files at revision 11" -- the round is named now
judge :50, :61 and :65 are withdrawn rather than restated, which BP0 allows
     and which is the better repair. All three clauses met.
```

- **R342 -- CLOSED, and it went further than the condition asked.** The
  predicate is the property, and the workflow no longer ignores the tree at
  all.

```
cmd  the two disjuncts, and the new `if`, against three ignore lists
out  shipped, milestones NOT ignored          -> passes
     the tree ignored wholesale               -> FAILS
     ignored plus the F2_figures carve-out    -> passes
cell the hole planted back in a sandbox copy of the shipped workflow
out  tests/test_ci_workflow_is_wellformed.py  1 failed, 7 passed,
     at :110, the new assertion. IT REDDENS ON THE HOLE NOW.
cmd  grep -n "F2_figures" .github/workflows/ci.yml
out  :177 `git diff --exit-code -- docs/milestones/F2_figures.md`
judge SO THE COMMENT CLAIM IS SUBSTANTIATED: the byte-identity comparison
     the carve-out exists for is a real step in the workflow, and I found it
     rather than took it.
judge AND THE FALSE ROW IS WITHDRAWN AS A FALSE ROW, not quietly replaced:
     "The sentence in revision 13 section 8 saying the ignore list had moved
     is withdrawn. It has moved now, in this round, which is a different
     statement and is made as one."
```

- **R343 -- CLOSED at the second disjunct its condition offered.** The causal
  clause is gone and what replaces it is a measurement.

```
code "whether a lint failure PREDICTS a test failure is not measured here and
      is not asserted"
cmd  caches cleared, then ruff plus black plus mypy, then pytest tests/unit
out  3.74 s and 0.907 s      against the comment 4.0 s and 0.9 s
judge BOTH REPRODUCE. The ratio claim is two orders and is not a close call,
     and the comment says the runner numbers will differ, which is honest.
judge THE RE-TAKE IS THE POINT AND IT WAS DONE RIGHT: `ff6b61a` exists
     because the previous figures were warm-cache, and the comment says so.
     That is BP0 being obeyed without being asked twice.
judge WHAT I AM RECORDING AND NOT HOLDING ON (R354, 4a): the comment now says
     what a lint red COSTS IN SECONDS and still not what it costs in
     EVIDENCE -- 374 s of guards that do not run. The condition was
     disjunctive and this disjunct is met; I am not moving the goalpost.
```

- **R344 -- CLOSED at the second disjunct.** `tests/verification/rung4/
  test_writer_round_trip.py:355` now reads
  `assert drift > INTERCHANGE_CHANNEL_DRIFT_ULP`, inside the function the
  finding named, with both numbers in the message. The collected golden was
  regenerated in its own commit (`c6cf348`) for the rename in the same file,
  which is the route the condition asked for, working. The name still says
  "orders away" where the assertion says greater-than -- recorded as
  **R355**, 4a, because the docstring argues explicitly and correctly that an
  orders threshold would re-introduce the undeclared literal R326 removed.

- **R345 -- CLOSED at the second disjunct, and the first half got a control
  it did not have.**

```
cell the helper guard neutered, `if ampl == 0.0:` becomes `if False:`
out  1 failed -- "DID NOT RAISE ValueError" at :126
cell the SCRIPT guard neutered the same way, message intact
out  23 passed -- STILL GREEN, and the docstring now says so: "The script is
     READ ... Reading is weaker and saying so is the point."
cmd  grep -n "ampl\|def main\|h5py" scripts/measure_channel_drift.py
out  :66 `def main()`, :68 `import h5py`, :93-:94 the guard inside it
judge THE RE-ARGUMENT FACT IS TRUE, and I checked it rather than accepted
     it: the branch is inside `main()` behind h5py and the fixture. The
     condition allowed "the docstring says it is a source check and the
     condition is re-argued as one", and that is what was done, with the
     weakness named in the file rather than in a report.
judge THE NEW DISABLE-IT CONTROL IS NOT CEREMONY. It re-execs the helper own
     source with the guard removed and REQUIRES the defaulting to come back,
     so a future edit cannot make the raise unreachable and stay green.
```

- **R346 -- OPEN. Carried as R352.** The condition named two disjuncts and
  neither happened. Section 0 heading still reads "CI at the reviewed commit
  `389d416`"; the reviewed commit is `a93d505`. `scripts/ci_section.py` is
  untouched and still labels whatever sha it is handed "the reviewed commit".
  Report section 4 answers the duplication half of the finding and states
  "The script is unchanged; nothing was wrong with it" -- but the finding
  mechanism paragraph was about the script label, not only the prose.

- **R347, R348, R349, R350 second half -- OPEN at 4a, correctly listed in
  section 6.** R350 first half was done anyway and done correctly; section 5
  is accurate and I re-derived its claim from the corpus rather than from the
  report.

- **R330, R331, R332 -- OPEN at 4a, correctly listed.** R332 stands and I
  honoured it again: nothing reads `g21_rigid_body_frames.txt`, so I added
  nothing to it.

- **R231, R244, R245, R275 -- OPEN, still correctly declared blocked** on the
  canonical re-render. My run reproduces the block: `regen_figures` moves five
  exact-class figures that are staleness (`exempt_total` 62 of 632 becomes
  65 of 656, `margin_dropped_flip` 6.264e+05x becomes 1217x) and nine
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
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried, and
  correctly present in the generated table.**

## Findings

**R351. (BLOCKS -- my adversarial case passed when it should have failed, and
it refutes three published sentences) A regression can still be filed as
growth, without touching my file. The growth rule CLASSIFICATION is derived
from the corpus; its DOMAIN is one function in the implementer own test file,
and nothing ties that function output to the corpus it parses.**
`tests/test_marker_exemption_corpus.py:103-127` and `:220-232`.

```
code :33  "The set of allowed escapes is therefore DERIVED, and a regression
     :35   has no field to hide in."
code :281 "There is nothing to declare and nowhere to declare it -- the field
     :282  that decides is in a file the implementer does not write."
code s1   "THE ONLY WAY TO FILE A REGRESSION AS GROWTH IS TO EDIT THE
           REVIEWER FILE, and the hook refuses that to me in a shell
           command as well as in an edit."
cell TWO EDITS, BOTH IN FILES THE IMPLEMENTER OWNS, IN A CLEAN CLONE AT
     a93d505:                                             (my run, a93d505)
     (a) `ast.walk(inner)` becomes `ast.walk(inner.right)` in
         `_literal_thresholds_inside` -- a genuine, plausible tightening
     (b) ONE LINE in `_entries()`, phrased as housekeeping:
             if "raised_to_a_literal" in line:  # shape superseded
                 continue
out  after (a) alone   2 failed -- the mechanism works, it names the shape
                       and blames the commit. This is not in dispute.
     after (a) and (b) python -m pytest -q
                       2 failed, 2066 passed
                       THE SAME TWO PRE-EXISTING FAILURES AS THE CLEAN TREE.
                       No corpus edit. No provenance string. Nothing red.
judge THE HOOK IS NOT THE BOUND. It protects the DATA and it does that well
     -- I read it and it covers redirects and `cd`. What it cannot protect is
     whether the data is read. `ENTRIES` is the domain of every assertion in
     the file: the parametrisation, `PLANTED_ESCAPES`, `_measured_misses()`,
     `test_no_shape_that_was_CAUGHT_when_planted_escapes_now`. Remove a line
     from `ENTRIES` and all four lose it together.
judge AND THE META-TEST WRITTEN FOR EXACTLY THIS IS CALIBRATED 4.5x TOO
     LOOSE. `:223` reads `assert len(ENTRIES) >= 28` with the message "a
     parser that silently drops most of them is the failure this guards" --
     against a file of 125 entries. It defends against dropping 78 per cent
     and nothing else. That is the assertion-domain-blindness guard: the
     collection the assertion inspects is built by the code that would
     contain the fault.
judge THE PASS COUNT DROPS BY EXACTLY ONE, 2067 to 2066, AND NOTHING LOOKS AT
     IT. The collected golden records function names, not parametrised ids
     (R347), so a vanished case is invisible there too.
cell THE FIX IS ONE ASSERTION AND I RAN IT BOTH WAYS:
         on_file = sum(1 for l in CORPUS.read_text(...).splitlines()
                       if l.startswith("id="))
         assert len(ENTRIES) == on_file
out  with (a) and (b) planted   1 failed -- test_the_corpus_is_not_empty
     on the clean tree          52 passed
judge IT CONVERTS AN INVISIBLE EDIT INTO A LOUD ONE, which is the whole
     arrangement. I am not claiming a test can be made un-editable; I am
     saying the count is a fact about a file I write and it is currently
     compared to nothing.
judge THIS IS NOT R341 REOPENED. What R341 named was done, and done well --
     see Carried. This is a door that condition did not name, and I found it
     by trying to break the thing rather than by reading it.
judge AND THE SAME SHAPE IS IN FOUR MORE READERS, recorded at 4a as R356.
```

**Closed when** `len(ENTRIES)` is compared to the corpus file own `id=`
count, with a cell showing it red on a dropped entry and green on the clean
tree; and the three sentences above either say what the code does or the
domain is closed so they become true. Either repair closes it; the sentences
and the mechanism must agree, and which way is the implementer call.

**R352. (BLOCKS -- R346 unmet at both of its disjuncts, fourth round running)
Section 0 heading names a commit that is not the reviewed commit and calls it
the reviewed commit.** Report section 0; `scripts/ci_section.py`.

```
code s0  "## 0. CI at the reviewed commit 389d416 -- unavailable,
         allowance exhausted"
cmd  git rev-parse HEAD
out  a93d505000e14a2288be18638a011ddef526ceb6
cmd  git diff --stat 2b6435d..a93d505 -- scripts/ci_section.py
out  (empty) -- the generator is untouched and still labels its argument
judge R346 CONDITION HAD TWO DISJUNCTS AND NEITHER HAPPENED. The first was
     "section 0 names the commit it actually describes AND DOES NOT CALL IT
     THE REVIEWED COMMIT" -- it names 389d416, which it does describe, and
     it does call it the reviewed commit. The second was "the generator takes
     the head and says so when no run exists there" -- unchanged.
judge SECTION 4 ANSWERS THE OTHER HALF AND SAYS THE SCRIPT IS FINE. The
     duplication IS fixed and section 0a is a genuine improvement -- it now
     carries only what section 0 cannot know. But R346 mechanism paragraph
     was about the LABEL: ci_section.py labels whatever sha it is handed
     "the reviewed commit", and nothing ties that argument to the report
     own head.
judge THE SERIES: verdict 37 found section 0 describing d384e41; 38 found
     cbde0e4; 39 found cbde0e4 while reviewing 389d416; this one finds
     389d416 while reviewing a93d505. Same off-by-one-round, four times.
     A report cannot describe the run its own push creates -- that is a real
     constraint, stated in the finding, and it is why the fix is a label and
     not a measurement.
judge AND IT PROPAGATED. The task handing me this step repeated "CI at the
     reviewed commit 389d416" as fact. It is the sentence, not the reader.
judge NOTHING TURNS ON IT FOR THE VERDICT -- I classified a93d505 myself
     and both states are unavailable. It is a sentence a reader trusts and
     it is wrong, in the one section whose entire job is to say what a
     machine nobody controls did to this commit.
```

**Closed when** the string "the reviewed commit" does not appear beside a sha
that is not `git rev-parse HEAD` -- either the generator takes the head and
reports "no run at this commit; the nearest ancestor with a run is X", or the
heading reads "the last commit with a run, followed by the sha". One line
either way.

**R353. (BLOCKS -- two figures in a shipped guard made false by the commit
that publishes them, and the check beside them left on the rule that was
replaced) 7ba1e9d moved one entry across the boundary and did not re-take
the two numbers that count it, in the same file.**
`tests/test_marker_exemption_corpus.py:299` and `:363-373`.

```
code :299  "The first version of this asserted the other direction and
            reddened on thirty-one shapes"
code :371  "reddened at 46 against 79 ... and it is the forty-six the scanner
     :373   was right about at plant time"
cell ONE VARIABLE MOVED: 7ba1e9d, which made _did_catch() read
     caught_but_... as caught.  Everything else held; the corpus is
     byte-identical across the pair.                      (my run)
out  at 2f21b54, the commit that WROTE both sentences:
        PLANTED_ESCAPES 79   ASSERTED 46   improved 31   declared 46
     at a93d505, the commit that PUBLISHES them:
        PLANTED_ESCAPES 78   ASSERTED 47   improved 30   declared 46
judge SO "thirty-one" IS 30 AND "forty-six" IS 47, at the commit that ships
     them. Both were true when written. Neither was re-taken when the rule
     beneath them moved one commit later -- which is BP0, and which is the
     same species as R341 second half, recurring in the same file, in the
     round that repaired it.
judge AND declared IS 46 ONLY BECAUSE :363 STILL USES THE SUPERSEDED RULE.
       declared = sum(1 for _, expect, measured, _ in ENTRIES
                      if measured == expect)
     That is the bare string comparison 7ba1e9d replaced, and it is the
     one place in the file that still uses it. The entry it disagrees about
     is exactly the one 7ba1e9d was written to rescue:
       detect_module_float_shadowed_by_a_later_int
     So the assertion "the regression domain is not empty" measures a
     46-entry domain while the domain it guards is 47. It is a non-emptiness
     check, so nothing fails today. It is the wrong rule sitting under the
     right sentence, and it is one token: _planted_caught(expect, measured).
judge WHY THIS IS NOT PEDANTRY. R350 first half exists BECAUSE a bare
     measured != expect filed a caught shape as growth. The fix landed and
     left the same comparison in the test that certifies the fix.
```

**Closed when** `:363` uses `_planted_caught()` like the rest of the file, and
`:299` and `:371-373` carry the numbers measured at the commit that publishes
them -- or the numbers are withdrawn to the step report, which BP0 and BI3
both allow and which the same round already did for the block at `:52-59`.

**R354. (recordable, 4a) The cheap-first comment prices a lint red in seconds
and not in evidence.** `.github/workflows/ci.yml:281-297`. The causal claim is
gone and the timings reproduce (3.74 s and 0.907 s against 4.0 and 0.9), which
closes R343. What is still unsaid: steps stop at the first failure, so a ruff
E501 costs the 374 s of guards on a machine nobody controls. The cell is in
the repository -- d2bbcdd, where the red was an E501 and rung 4 was green in
the same run. A `continue-on-error` on lint with a final gate is one line.

**R355. (recordable, 4a) test_a_swapped_sign_is_orders_away_from_the_band
asserts greater-than, not orders.**
`tests/verification/rung4/test_writer_round_trip.py:311, 355`. R344 is closed
at its second disjunct and this is the residue of the first. The docstring
argues -- correctly -- that an orders threshold would re-introduce the
undeclared literal R326 removed, and that the orders belong in the report. It
also states its own limit: "IT READS NO FIXTURE ... this cannot fail for any
defect in the repository." A test that declares its own vacuity is not the
species this milestone keeps finding; the NAME is what a reader scanning a
rung-4 module sees, and it still promises more than the body delivers.

**R356. (recordable, 4a) Every reviewer-owned corpus is read by a parser the
implementer owns, and none of the five readers compares the parsed count to
the file.** `tests/test_marker_exemption_corpus.py:223` (28 against 125),
`tests/verification/rung1/test_corpus_configurations.py:671` (10 against 203),
`tests/test_report_vocabulary_corpus.py:117` (20 against 31),
`tests/test_ci_ladder_gating.py:133` and `tests/test_report_guard_states.py:105`
(no count assertion at all). R351 is the one instance where I could show the
hole doing damage; the other four are the same construction and the fix is the
same line. R347 already names one covering guard for the g22 corpus; the rest
have none that I could find.

**R357. (recordable, 4a) `scripts/untouched_sites.py:59` matches sites by path
suffix.** The expression is a list comprehension over TOUCHED keeping any path
that ends with the site path, so a verdict naming `golden.py` would match
`tests/test_collected_set_golden.py`. The import of the guard own SITES and
TOUCHED is the RIGHT call and I want it on the record as such: a second regex
drifted 68 against 87, and a generator that disagrees with the check it feeds
is worse than an unusual import direction. The suffix match is the one place
the script still decides something on its own. Separately, the line-granularity
expansion produced 41 identical rows for one finding this round; that is R349
other half and it is loud rather than wrong.

**R358. (recordable, 4a -- and it is mine to have caused and nobody to have
noticed for two rounds) A shipped guard is RED BY CONSTRUCTION at every corpus
commit and every verdict commit on this branch, and no report has ever said
so, because the only commits anyone measures at are the ones where it is
green.** `tests/test_report_carried.py:1043-1061` (R319 distance rule).

```
code assert distance <= 1  -- the whole-suite line must name HEAD or HEAD^
cmd  pytest tests/test_report_carried.py::test_the_whole_suite_line_is_
     about_a_commit_that_exists, at three commits    (my run, clean clone)
out  at a93d505, the report commit            PASSES  (distance 1)
     at 9848630, LAST round corpus commit     FAILS
     at 2b6435d, LAST round verdict commit    FAILS
     at 40667c6, THIS round corpus commit     FAILS   (distance 2)
judge BE3 REQUIRES THE CORPUS TO BE COMMITTED SEPARATELY, BETWEEN THE REPORT
     AND THE VERDICT. R319 requires the whole-suite line to name HEAD or its
     parent. The two rules collide on every round, and the collision has been
     there for at least two rounds, unrecorded.
judge WHY NOBODY SAW IT. The supervisor runs the suite at the REPORT commit,
     where it is green. The implementer runs it at the report commit too. The
     two commits where it is red carry no code, so nobody runs anything there
     -- and `scripts/suite_count.py` excludes this very file from the count
     line, for an unrelated and good reason.
judge WHY IT WILL MATTER WHEN MINUTES RETURN, and this is the part that is
     not cosmetic. `paths-ignore` covers `docs/reports/**` and
     `docs/reviews/**`; it does NOT cover `tests/corpus/**`. So a push
     carrying my corpus commit runs the whole CI and goes RED on this guard,
     for no defect. R223, R224 and Q7 open on "green CI at a reviewed
     commit", and this stands between them and that.
judge IT IS ELEVEN OF THE ELEVEN FAILURES I SEE AT MY OWN CORPUS COMMIT: one
     direct, ten through `test_report_guard_states.py`, which replays the
     guard under each state and inherits the same red.
```

This is why the eleven reds at `40667c6` are named here in full rather than
left for the next report to explain. They are mine, they are one assertion,
and the fix is either a corpus-commit exemption in the distance rule or
`tests/corpus/**` in `paths-ignore` -- the first is better, because the corpus
is the one thing a run should see.

## Tolerances touched

**None.** `git diff 2b6435d..a93d505 -- floatfea/tolerances.py` is empty, and
so is the diff over all of `floatfea/`.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (unchanged) | dimensionless, ULP of the channel own amplitude | `3.0`, injected beyond the site clean deviation | `docs/milestones/F2.md:1116-1152`, `tolerances.py:1024-1035` |
| `INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER` | `3.0` (unchanged) | dimensionless | itself; the assertion is `drift == expected_drift`, exact | same, `:1054-1055` |
| everything else | unchanged | -- | -- | the diff over the file is empty |

```
cmd  offending() over every *.py in tests/ and scripts/    (my run, a93d505)
out  0 files reported -- no undeclared literal entered the tree this round
judge AND THE NEW ASSERTION IN rung4 USES THE DECLARED NAME: the band is
     imported, not a literal. That is R344 repair obeying R326 rather than
     undoing it, and I checked it because the cheapest wrong fix here was a
     literal multiple of the band coming back.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** This is the strongest round the
step has had. Five of six conditions close, and two of them close against
attacks I built rather than against the words of the condition: the
`paths-ignore` predicate reddens on the hole I planted in a sandbox, and the
all-zero control reddens when I neuter the guard it defends. The escape
golden asymmetry is real -- I measured it by writing 22 shapes the implementer
has never seen and watching 18 misses arrive as derived growth with no line
written, where the identical act last round produced 16 failures and demanded
fifteen hand-typed entries. `floatfea/` is unchanged for the fifteenth round
and the ladder is green.

**What holds is one thing I broke and two sentences that do not describe the
repository.**

1. **R351 -- the growth rule domain is a function I write, and one line in it
   files a regression as growth.** Full suite, clean clone, genuine scanner
   regression plus one housekeeping line: `2 failed, 2066 passed`, the same
   two failures as the clean tree. Three published sentences say this is
   impossible. The fix is one assertion and I ran it red and green.
2. **R352 -- section 0 calls 389d416 the reviewed commit and the reviewed
   commit is a93d505.** R346 condition is unmet at both disjuncts; this is the
   fourth verdict finding the same off-by-one-round in the same heading, and
   it propagated into the task that briefed me.
3. **R353 -- "thirty-one" is 30 and "forty-six" is 47** at the commit that
   publishes them, and `:363` still uses the string comparison 7ba1e9d
   replaced -- in the test that certifies 7ba1e9d.

**CI at `a93d505` is `unavailable -- allowance exhausted`**, the CK2 third
state: four jobs, two never started with the billing annotation, two skipped.
Neither red nor green, nothing claimed from it, and it does not hold this step
by itself. The last run that executed, `34546580003` at `8942cdc`, no longer
describes this tree -- 717 lines across eight files since. None of the three
items above waits on a runner.

**THE ELEVEN REDS AT MY CORPUS COMMIT `40667c6` ARE MINE AND ARE NOT A
DEFECT IN THIS ROUND, AND THEY ARE ALSO NOT NEW.** All eleven are one
assertion -- R319 distance rule, one direct and ten replayed through
`test_report_guard_states.py` -- and the same assertion was red at last
round corpus and verdict commits too. At the commit I judged, `a93d505`, it
passes. R358 records it and measures it at four commits.

**Not gates on step 5, into the next report Carried section:** R354, R355,
R356, R357, R358, R347, R348, R349, R350 second half, R330, R331, R332, the section
9 status-versus-subject disagreement, R321, R322, R300, R291, R292, R281,
R231/R244/R245/R275 behind the canonical render, R223, R224, R230, R261, the
underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 22 new entries in one file, all unseen by the
implementer, every `measured=` taken at `a93d505` by running the shipped
`offending()` before the `expect=` beside it was written.**

**The coverage measurement, stated plainly: of my 22 new entries the shipped
scanner does what the entry requires on 4, and 18 are misses.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+22 (125 to 147), 4
  correct.** Two axes the last three rounds did not reach. **First: a library
  DEFAULT is a tolerance and there is nothing to grep for.** The scanner knows
  this for one library and not the other -- `pytest.approx(want)` with no
  `abs=` or `rel=` is reported by name with its defaults spelled out in the
  message; `np.isclose(a, b)`, which carries `rtol=1e-05`, scans clean. The
  rule exists, it is correct, and it was written for one call site. **Second:
  three entries carry no float constant at all** -- one divided by a billion,
  ten to the minus ninth, and `decimal=9` -- because `_floats_in()` reads
  float constants and an integer spelling of the same number is invisible.
* **The remaining fifteen are how a tolerance ordinarily arrives somewhere**:
  a pytest fixture, an instance attribute set in `__init__`, a namedtuple
  field, `dict.get` default, `os.environ.get` default, a JSON blob, a helper
  that returns it, machine epsilon scaled by a chosen number, and the
  `cfg.tol or 1e-09` shape -- which is exactly what R338 found shipped in
  `scripts/measure_channel_drift.py` and which the scanner still does not see.
* **Both `expect=exempt` controls pass**, so the hatch remains usable, which
  matters more than any single miss.
* **WHAT MY CORPUS DOES TO THE SUITE THIS ROUND: nothing.**
  `tests/test_marker_exemption_corpus.py` is **56 passed** at my corpus commit
  against 52 at `a93d505`. Eighteen misses arrive as derived growth. That is
  CN0 working, and it is the reason R341 closes.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands: nothing
  reads it.

**Forty rounds have found no element defect, and this round does not either.**
`floatfea/` has been comment-only for fifteen. By the rule I am bound by that
still means "not yet contradicted", because V5.1 against CalculiX has not run.
What this round changed is that the instruments got harder to fool: two of my
three attacks failed against guards that were written before I ran them. The
one that succeeded went through a door nobody had thought to shut, and it
shuts with one line.
