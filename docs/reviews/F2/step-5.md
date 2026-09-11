# Review � F2 step 5
Reviewed commit: 389d41601ca6560137824b2d4bed38e7261f2f01
Verdict: HOLD

**Reviewed commit: `389d416`.** Report revision 13, `Answers: verdict 38 @ 334f345`.

Tests: **2095 passed, 2 failed, 0 skipped** (my run at `389d416` on a clean tree,
`python -m pytest -q`, 440.92 s, Python 3.13.15 on Windows). `pytest --collect-only`
gives **2097**, so nothing is skipped and nothing silently uncollected. The two
failures are the two §7 names, and both are mine from earlier corpus rounds.

**Commits: code `fe321ee`, `d043f7a`, `5ff0e14`, `999b1e6`, `80e8bab`. Report
`389d416`.**

**Item 1b.** Header line 4243 reads `Answers: verdict 38 @ 334f345`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`334f3457b96b1ce98dc06f845f6fd2d926242156`. It is the latest. **Passes.**

**CI, item 3b, AT THE COMMIT I AM REVIEWING: `unavailable -- allowance
exhausted`, the CK2 third state.** I classified it myself rather than reading
§0, and §0 turns out to describe a different commit and a different shape --
R346.

```
cmd  gh run list --limit 10 --json headSha,conclusion,event,databaseId
out  34614405577  push  failure  @ 389d416   -- and no pull_request twin
cmd  gh api repos/xabi80/FloatFEA/actions/runs/34614405577/jobs
out  4 jobs. "the verification ladder" and "lint, unit and guards":
     conclusion failure, runner_name "", steps 0, started 15:09:07 and
     completed 15:09:08/09 -- two seconds.
     "CI determinism -- leg" and "-- ten legs agree": SKIPPED.
cmd  gh api .../check-runs/<id>/annotations  for the two failures
out  "The job was not started because recent account payments have failed or
     your spending limit needs to be increased" -- both of them
judge THIS IS EXACTLY CK2's THIRD STATE and it is NOT the shape the report
     publishes. `unavailable -- allowance exhausted`, neither red nor green.
     Nothing may be claimed from it in either direction.
judge AND IT IS ALSO THE MEASUREMENT THAT CLOSES R334's THIRD CLAUSE. Two
     real jobs and two skipped is `workflow_dispatch` gating working. Under
     the duplicate key the verdict job ran on every push; here it is skipped.
     "Expected cost per push is two jobs" is now a measured sentence.
cmd  python scripts/ci_section.py 389d416
out  "## 0. CI at the reviewed commit `389d416` -- **unavailable, allowance
     exhausted** ... not one of its 4 jobs started"
judge THE GENERATOR IS CORRECT AT THIS COMMIT. It crashed at `cbde0e4` and
     does not here; the new `if not jobs:` branch is guarded and right, and I
     read it. What is wrong is the sha the report fed it.
cmd  gh api .../runs/34546580003/jobs   (the last run that EXECUTED, @ 8942cdc)
out  6 of 6 ladder jobs success; "guards and meta-tests" FAILURE; rest green
cmd  git diff --stat 8942cdc..389d416 -- tests/verification scripts .github
out  NOT empty: 7 files, 580 insertions. ci.yml alone is 278 lines changed.
judge SO THAT RUN DOES NOT DESCRIBE THIS TREE and the report says so in §0a,
     correctly, and labels the local ladder result as local. Accepted.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

**My own instructions (4b) and the conftest pathspec (4c).**

```
cmd  git diff 334f345..389d416 -- .claude docs/SUPERVISOR.md
out  (empty) -- no commit in this range touches either. Nothing to read.
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 334f345..389d416 -- tests/conftest.py 'tests/**/conftest.py'
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
cmd  git diff 334f345..389d416 -- floatfea/tolerances.py
out  one hunk, three lines, all comment: R340's noun. Both `Final[float]`
     lines unchanged at 2.0 and 3.0.
```

**What held, reproduced at my run**: `ruff check floatfea tests scripts` clean;
`black --check floatfea tests` clean over 76 files; `mypy floatfea` clean over
25 source files; `sh scripts/run_rung.sh full:tests/verification/rung4` gives
`89 collected, 0 failed`, which is the report's figure to the digit; the
collected golden matches the live collection exactly on all six roots
(305/73/50/46/37/4, zero missing and zero extra); `tests/test_ci_workflow_is_
wellformed.py` `8 passed` and three of its assertions ablated red; the
scanner reports **0** files over the whole of `tests/`.

## Carried

Verdict 38 listed six blocking items and five at 4a. **Three close outright
(R333, R336, R339/R340). Four close at some of the sites their conditions
named and not at others (R334, R335, R337, R338).** No item is untouched, and
the head one -- the three deleted tests -- is closed properly and with a
mechanism behind it.

- **R333 -- CLOSED, and the repair is better than the condition asked for.**

```
cell the three functions extracted by AST from `2e6276c` and from `389d416`
     and compared as text                                    (my run, 389d416)
out  test_channels_are_not_interchangeable          IDENTICAL
     test_a_validation_error_SURVIVES_propagation   IDENTICAL
     test_mu_is_present_and_not_all_zero            IDENTICAL
judge VERBATIM IS VERBATIM, checked rather than read off the commit message.
     The module function set is the old one plus the renamed sign-flip test
     plus one new test, and nothing else moved.
cmd  grep -n for the two citing sentences
out  :99 cites test_mu_is_present_and_not_all_zero, :200 cites
     test_channels_are_not_interchangeable -- both now resolve
cmd  sh scripts/run_rung.sh full:tests/verification/rung4
out  89 collected, 0 failed   -- the report figure to the digit, 85 reconciled
cell the deletion re-applied: the file truncated at the same function
out  tests/test_collected_set_golden.py  2 failed, 9 passed -- and it names
     all three by name under BOTH the `tests` and the `tests/verification/
     rung4` roots. THE GUARD CATCHES THE DELETION IT WAS WRITTEN FOR.
cell a rename: test_mu_is_present_and_not_all_zero -> ..._and_nonzero
out  2 failed -- A RENAME DOES ARRIVE AS A REMOVAL, as the docstring says
judge AND I CHECKED THE GOLDEN AGAINST THE TREE RATHER THAN AGAINST ITSELF:
     `GEN.collected(root)` run for all six roots gives 305/73/50/46/37/4,
     zero missing and zero extra. The `[tests]` root is a strict superset of
     the other five, so rung2/5/6 -- which hold no test functions at all --
     are not a hole in the ROOTS list; anything added there lands under
     `[tests]`.
judge AND IT CANNOT BE NEUTERED BY DELETING IT. An empty or missing golden
     parses to an empty map, the parametrisation collapses to `(none)` and
     fails, and `total > 300` means dropping the `tests` root from ROOTS
     leaves 210 and reddens. I traced each of those rather than assuming.
judge ONE THING IT DOES NOT SEE, measured, and it is recorded at 4a as R347
     rather than held against this item: parametrised ids are not recorded,
     by design and stated.
```

- **R334 -- CLOSED AT THREE OF THE FOUR THINGS ITS CONDITION NAMED. The
  fourth is answered by an assertion that passes on the hole and fails on the
  fix.** Carried as **R342**.

```
cmd  the workflow loaded with a duplicate-rejecting loader   (my run, 389d416)
out  clean. One `if:`, reading always() && github.event_name ==
     workflow_dispatch, and `needs: [determinism]` beside it.
cell the two keys planted back exactly as `83bffc1` had them
out  8 failed -- every assertion in the file, because every one of them
     parses the document. The named one reports the line number.
cell the gate removed, and separately `needs: [checks]` restored on ladder
out  2 failed / 2 failed, each naming the right property. BOTH ARE LIVE.
cmd  the run at 389d416, job by job
out  2 real jobs, 2 skipped -- "two jobs per push" is measured now, not
     predicted, and it is the third clause of the condition
judge FIVE OF CK0 SEVEN CLAIMS ARE ASSERTIONS. I checked each against the
     claim it is supposed to carry: the dispatch gate, the dropped
     pull_request trigger, cancel-in-progress, the wheel cache, and the doc
     paths. Two remain prose -- the three-jobs-in-one merge and the
     six-ladder-jobs merge -- and both are implied by assertions elsewhere
     that read the step list, which I ran.
judge THE DOC-PATHS ONE IS HALF AN ASSERTION AND HALF AN INVERSION. That is
     R342, and it is the fourth clause of this condition.
judge ONE WEAKNESS WORTH NAMING AND NOT HOLDING ON (R348, 4a): the dispatch
     assertion is a substring test, so a negated condition passes it.
```

- **R335 -- CLOSED AT ITS FIRST CLAUSE, OPEN AT ITS SECOND.** Carried as
  **R343**. The `needs: [checks]` edge is gone, a shipped test asserts its
  absence and I ablated it red, and the comment records the measurement --
  run `34546580003`, guards red, six ladder jobs green -- rather than the
  interpretability argument. That is the whole first half and it is done
  well. What the condition also required was that the choice not be recorded
  with "the interpretability argument, which does not apply to lint", and
  `.github/workflows/ci.yml:277-279` still reads "The ORDER is the cheap-first
  order and it is not arbitrary: lint and type-check take seconds and catch
  the class of defect that makes the rest meaningless." The grep for
  `cheap-first` over the diff of that file is empty.

- **R336 -- CLOSED, and both halves of the condition are met.**

```
code assert drift == expected_drift          (the epsilon is gone entirely)
cmd  offending() over every *.py under tests/ and scripts/  (my run, 389d416)
out  0 files reported
judge SO THE SENTENCE AT :50-54 -- "None does -- the scanner is clean over
     every file in tests/, measured, not assumed" -- IS TRUE AGAIN AT THE
     COMMIT THAT PUBLISHES IT, which is what the condition asked for. I
     measured it rather than reading it.
judge AND THE CHOICE IS THE RIGHT ONE. Exact equality rather than a declared
     constant: the fourteen cells I ran last round land on the prediction to
     the bit, both sides are the same two subtractions in the same order, and
     an epsilon there was protecting against nothing measured. Removing the
     comparison is better than declaring it.
judge THE REST OF THAT COMMENT BLOCK IS NOW FALSE, and it was made false by
     the commit under review. That is R341 second half, not a reopening.
```

- **R337 -- CLOSED AT ONE OF ITS TWO CLAUSES.** Carried as **R344**. The
  figure is published: report §4 gives `1.062836e+16` ULP, band `2.0`, ratio
  `5.3142e+15`, `15.73` orders, and `74 of 75` values still exact. I
  re-measured `1.0628e+16` independently last round and `74 = want.size - 1`
  follows from the shipped assertion. The docstring no longer points at a
  figure that does not exist. The second clause -- "either the name matches
  what the test asserts, or the band comparison returns as its own
  assertion" -- is unanswered.

- **R338 -- CLOSED AT ONE AND A HALF OF ITS THREE CLAUSES.** Carried as
  **R345**. `scripts/measure_channel_drift.py` raises where it defaulted, the
  wording is right, and I confirmed the helper and the script now agree. The
  §8 generator false row is gone this round -- I checked every row in the
  table against `git diff --name-only` and **no row claims "the diff touches
  this file" for a file with no hunks** -- but by circumstance rather than by
  fix, and that is R349 at 4a. What is not done is the middle clause, "a test
  reddens when the raise is removed".

- **R339 -- CLOSED.** `scripts/suite_count.py:62-81` measures the exclusion
  and the line states it: "excluding 325 tests in 3 files". I checked the
  arithmetic rather than the sentence: at `389d416` the whole suite collects
  `2097`, the three excluded files collect `266`, and 2097 - 266 = 1831 =
  1829 passed + 2 failed. The line reconciles.

- **R340 -- CLOSED.** `floatfea/tolerances.py:1054-1055` now reads "AT LEAST
  one ULP by construction -- it is |clean| + 1, and one is its floor". That
  is the noun corrected and the measurement unchanged.

- **R330, R331, R332 -- OPEN at 4a, correctly listed in §5 and §6.** R332
  stands and I honoured it again: nothing reads `g21_rigid_body_frames.txt`,
  so I added nothing to it.

- **R231, R244, R245, R275 -- OPEN, and still correctly declared blocked** on
  the canonical re-render. I checked the block rather than accepting it. The
  two reds are `ck_length_thousand_km|dropped_flip` and `|wrong_dof_index`
  entering the exempt-and-detected set, and five exact-class figures moved by
  a corpus round -- `exempt_total` from `62 of 632` to `65 of 656`,
  `margin_dropped_flip` from `6.264e+05x` to `1217x`. Those five are staleness
  and not platform, by the shipped test own classification. But the same run
  puts `clean_worst_ratio` at `1.0784x` and `rigid_body_mode_ratio` at
  `1.3356x` of the committed values, and `regen_figures.py` writes the whole
  file, so a render here would fix five figures and corrupt nine. **The block
  is real and the right call is the one taken.**

- **R223, R224, R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.** R302 accepted at verdict 37, not reopened.

- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The §9 table status column reads `open` for R326-R329,
  including R327, which verdict 38 closed outright. Same species as the
  R318-R320 disagreement already at 4a; it has grown by four rows and stays
  there.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried, and
  correctly present in the generated table.**

## Findings

**R341. (BLOCKS -- the truth of a published sentence in a shipped guard and in
the report, and a control that cannot fail on the case it names) The escape
golden cannot tell a regression from growth. Three genuine regressions, one of
them on an entry whose own corpus line records `measured=caught`, go green by
adding three lines with a provenance string that is false.**
`tests/test_marker_exemption_corpus.py:90-92` and `:339-352`; report §5 and
§10.

```
code :90  "A SHAPE PREVIOUSLY CAUGHT THAT STARTS ESCAPING IS A REGRESSION and
     :91   fails. It arrives as a name in the measured set that this map does
     :92   not carry, and there is no way to record it without naming who
           planted it and when."
code report §10  "The asymmetry is the point: growth is allowed and named, a
     regression cannot be filed as growth."
cell ONE VARIABLE MOVED, EVERYTHING ELSE HELD. `_literal_thresholds_inside`
     narrowed by one line so a declared name on the LEFT of a BinOp is no
     longer read -- a plausible tightening, not sabotage.  (my run, 389d416)
out  3 entries regress: detect_declared_divided_by_literal,
     detect_literal_added_to_declared, detect_declared_raised_to_a_literal.
     The last one corpus line carries measured=caught.
     tests/test_marker_exemption_corpus.py -> 4 failed, 70 passed. GOOD.
cell then the three names added to KNOWN_MISSES with the provenance string
     "34bce16, the thirty-eighth round" -- which is a lie -- and nothing else
out  tests/test_marker_exemption_corpus.py  71 passed
     tests/test_no_tolerance_literals.py    44 passed
judge THE DECISION HAS TWO INPUTS AND NEITHER CARRIES HISTORY:
     `_measured_misses()`, which is what the scanner does now, and
     `set(KNOWN_MISSES)`, which is a map of names. A regression and a newly
     planted shape are the SAME INPUT. The provenance string is compared to
     nothing -- not to git, not to the corpus. "There is no way to record it"
     is three lines and a sentence, and it is what growth needs too.
judge THE RECORD THAT WOULD MAKE THE ASYMMETRY REAL IS ALREADY IN THE FILE
     AND IS THROWN AWAY. `tests/corpus/tolerance_marker_exemptions.txt`
     carries `measured=` per entry -- what the shipped scanner returned when
     the reviewer planted it -- and `_entries()` at :247 parses it into `got`
     and never reads it. An entry with `measured=caught` that now escapes is
     a regression BY CONSTRUCTION and is mechanically separable from a new
     plant. The asymmetry the docstring describes is one comparison away.
judge WHAT IS NOT WRONG, and I checked it rather than assuming: the thirteen
     ARE recorded with the right provenance. 20 entries added by `34bce16`
     against `34bce16^`, 13 of them missed, exactly the 13 attributed to it;
     20 attributed to CD2 and none of those added by `34bce16`; and
     `set(KNOWN_MISSES) == _measured_misses()`. The bookkeeping is accurate.
     The mechanism is what does not hold the claim up.
judge AND THE COMMENT BLOCK IMMEDIATELY ABOVE THE MAP WAS MADE FALSE BY THE
     COMMIT THAT PUBLISHES IT (BP0). `:50` reads "measured at CD2 over 66
     shapes" against a corpus of 105; `:61` repeats it; `:65` reads "ALL FOUR
     ARE ONE SPECIES" above a map of 33 entries in at least two species by
     the file own new text. Every one of those was true when written. CM4
     rewrote the map twenty-nine lines below them and left them.
judge AND ONE MORE IN THE SAME PARAGRAPH OF THE REPORT. §5 reads "that number
     was measured at forty-one this round". It was measured at revision 11
     (report line 3901), the scanner is byte-unchanged this round, and the
     file it is quoting says "measured at forty-one of them, ONCE" at :88.
```

**Closed when** either a regression is separable from growth by something the
implementer cannot write freely -- the corpus own `measured=` field is the
obvious one and is already in the file -- or the two sentences say what the
code does, which is that both directions are recorded by hand and the record
is a convention rather than a check; and `:50`, `:61` and `:65` describe the
map they sit above; and §5 "this round" names the round that took the figure.

**R342. (BLOCKS -- a gate that passes on the hole and fails on the fix, and a
false sentence answering the condition that asked for it) The `paths-ignore`
assertion is inverted: `docs/milestones/**` is still ignored, the canonical
render is still under it, and the test written to catch that is satisfied by
exactly that configuration.** `tests/test_ci_workflow_is_wellformed.py:99-101`;
`.github/workflows/ci.yml:24-27`; report §8, the `docs/milestones/F2_figures.md`
row.

```
code assert "docs/milestones/**" not in ignored or all(
         "F2_figures" not in x for x in ignored
     ), "the canonical render ... must not be ignored blindly"
cmd  the two disjuncts evaluated against the shipped workflow  (my run)
out  ignored = ['docs/reports/**', 'docs/reviews/**', 'docs/milestones/**']
     A ("milestones not ignored")        = False
     B ("no entry mentions F2_figures")  = True
     A or B -> True     THE ASSERTION PASSES ON THE HOLE
cell the carve-out the message asks for added: !docs/milestones/F2_figures.md
out  A or B -> False    THE FIX REDDENS IT
judge `all(... not in ...)` where `any(... in ...)` was meant. The predicate
     is the complement of the property. It is not wholly vacuous -- the loop
     above it over `docs/reports/**` and `docs/reviews/**` is real, and I
     confirmed that half reddens -- but the clause that exists for R334
     fourth condition certifies the opposite of it.
cmd  git diff 334f345..389d416 -- .github/workflows/ci.yml, grep paths-ignore
out  (empty) -- the ignore list did not move
code report §8  "| docs/milestones/F2_figures.md | no change -- ... The
     render is UNCHANGED ... and the ignore list is what moved |"
judge THE IGNORE LIST DID NOT MOVE. That row is the answer to the fourth
     clause of R334 and it states as fact something the diff refutes in one
     command. A commit landing the canonical render and nothing else still
     runs no CI -- the one commit in this milestone that most needs to.
```

**Closed when** the predicate is the property (`any`, not `all`), with a cell
showing it red on the shipped ignore list and green on the carve-out; and
either the carve-out is in the workflow or §8 says the hole is open and why,
instead of saying the list moved.

**R343. (BLOCKS -- R335 second named site, and a causal sentence whose cell
the repository holds) The `needs:` edge is gone and the cheap-first
justification is not.** `.github/workflows/ci.yml:277-279`.

```
code "The ORDER is the cheap-first order and it is not arbitrary: lint and
      type-check take seconds and catch the class of defect that makes the
      rest meaningless."
cmd  the diff of that file grepped for cheap-first
out  (empty) -- unchanged
cell the cell is in the repository and was taken last round: at `d2bbcdd` the
     red was a ruff E501, and rung 4 was green in the same run
judge AN OVER-LONG LINE DID NOT MAKE ANYTHING MEANINGLESS. Inside `checks`,
     lint still precedes `unit tests` and `guards and meta-tests`, steps stop
     at the first failure, so an E501 still costs the unit tests and every
     guard in the suite on a machine nobody controls. The ladder is rescued;
     the rest of the evidence is not, and the sentence that justifies the
     order is the one BG0 asks for a cell for. The condition named this and
     the repair took the first half.
judge WHAT I AM NOT SAYING: that the order must change. Putting lint last, or
     `continue-on-error` on it with a final gate, or leaving it first and
     deleting the causal claim, all close this. It is the uncelled "because"
     that is the finding.
```

**Closed when** either the ordering no longer converts a lint red into the
loss of the unit tests and the guards, or the sentence at `:277-279` is
reduced to what was measured -- lint is cheap -- with the causal clause
removed.

**R344. (BLOCKS -- R337 second named clause) The test still claims a property
nothing in its body asserts.**
`tests/verification/rung4/test_writer_round_trip.py:289-327`.

```
code def test_a_swapped_sign_is_orders_away_from_the_band() -> None:
         ...
         assert drift == predicted
         assert exact == want.size - 1
cmd  grep -n INTERCHANGE_CHANNEL_DRIFT_ULP over that function
out  (nothing) -- the band does not appear in the body at all
judge THE CONDITION READ: "either the name matches what the test asserts, or
     the band comparison returns as its own assertion." Neither happened. The
     figure was published, which is the first clause, and the name was left
     saying the thing the docstring spends four lines explaining it no longer
     does. A reader scanning function names in a rung-4 module reads a band
     guarantee that is not there.
judge THIS IS CHEAP AND IT IS NOT COSMETIC. A rename closes it, and the
     golden this round makes a rename a build failure -- which is the route
     working, not an obstacle.
```

**Closed when** the name states what the two assertions assert, or the band
comparison is back as an assertion of its own; and if it is the rename, the
collected golden is regenerated in the same commit, as `CLAUDE.md` § Testing
requires.

**R345. (BLOCKS -- R338 middle clause, and a false sentence in the guard
written for it) "A test reddens when the raise is removed" is a grep over the
script source, and the docstring says it is an import. Removing the raise
while leaving the words is green.**
`tests/verification/rung4/test_writer_round_trip.py:109-143`.

```
code """... which is why this one asserts BOTH, by importing the script
        rather than by reading it."""
code     spec.loader.exec_module(module)          <- `module` is never used
         source = (...).read_text(encoding="utf-8")
         assert "or 1.0" not in source
         assert "identically zero" in source
cell the old default restored in the script                 (my run, 389d416)
out  1 failed -- the literal reversion IS caught, and that is worth having
cell the raise neutered and the message left: `if ampl == 0.0:` -> `if False:`
out  23 passed                                       THE SUITE STAYS GREEN
judge IT READS THE SCRIPT. The import executes the module and the module
     object is discarded; nothing calls the code path. So the assertion is
     over two substrings, and any change that keeps the substrings and moves
     the condition passes. A guard whose own docstring says the opposite of
     what it does is the species this milestone has recorded five times.
judge WHAT WOULD MAKE IT AN ASSERTION RATHER THAN A GREP: call the function.
     The script loop is inside `main()`, so it needs a seam -- factor the
     per-row amplitude out and call it with a zero array, which is three
     lines and the same shape as the helper own arm two lines above.
```

**Closed when** the script zero-amplitude path is EXECUTED by a test that
reddens when the raise is removed with its message intact, or the docstring
says it is a source check and the condition is re-argued as one.

**R346. (BLOCKS -- the truth of the report own CI section) §0 calls `cbde0e4`
"the reviewed commit" and publishes the wrong one of CK2 two shapes for the
commit under review.** Report §0 and §0a.

```
code §0  "## 0. CI at the reviewed commit `cbde0e4` -- **unavailable, no jobs
         created**"
cmd  gh api .../runs/34614405577/jobs      (the run at 389d416)
out  4 jobs, runner_name "", steps 0, two seconds, billing annotation
judge THE REVIEWED COMMIT IS `389d416` AND ITS STATE IS `allowance
     exhausted`, not `no jobs created`. `cbde0e4` is the commit the PREVIOUS
     verdict reviewed, and its run does still have zero jobs -- I re-checked
     -- so §0 is true about a commit and false about which commit that is.
judge §10 SAYS THE OTHER ONE. "CI is `unavailable -- allowance exhausted`"
     appears in the report closing section, a different state from its own
     §0. One report naming both shapes for one commit.
judge THE MECHANISM, because this recurred: `scripts/ci_section.py <sha>`
     labels whatever sha it is handed "the reviewed commit", and nothing ties
     that argument to the report own head. Verdict 37 found §0 describing
     `d384e41`; verdict 38 found it describing `cbde0e4`; this one finds the
     same. A report cannot describe the run its own push creates -- that is a
     real constraint -- and the honest form is to say which commit it does
     describe.
judge NOTHING TURNS ON IT FOR THE VERDICT. Both shapes are `unavailable` and
     I classified the reviewed commit myself. It is a sentence a reader
     trusts, and it is wrong.
```

**Closed when** §0 names the commit it actually describes and does not call it
the reviewed commit, or the generator takes the head and says so when no run
exists there.

**R347. (recordable, 4a) The collected golden records functions, not cases, so
a parametrisation can collapse under it -- and the thing that catches that is
elsewhere.** `tests/test_collected_set_golden.py:144-152`; report §1.

```
cell tests/corpus/g22_model_configurations.txt cut from 203 entries to 2
out  pytest tests --collect-only:  2097 -> 1248    (849 cases gone)
     tests/test_collected_set_golden.py:  11 passed
judge THE GOLDEN CANNOT SEE IT, and the docstring names only the emptied body
     as its limit. The decision to record functions is right and the churn
     argument is real; the consequence is one sentence longer than it says.
judge AND I WENT AND FOUND WHAT DOES CATCH IT rather than filing this as a
     hole: under the same ablation `tests/regression/test_exempt_pair_
     responses.py::test_every_recorded_pair_is_still_detected` reddens with
     55 named pairs. The gate own corpus is defended. That is why this is 4a
     and not a gate, and naming the covering guard in the docstring is the
     whole fix.
```

**R348. (recordable, 4a) The dispatch assertion is a substring test.**
`tests/test_ci_workflow_is_wellformed.py:78` asserts that the literal
`workflow_dispatch` appears in the condition, so a NEGATED condition mentioning
the same event passes it. Parse the expression or pin it.

**R349. (recordable, 4a) The §8 generator still reasons at file granularity.**
No row is false this round -- I checked every one against `git diff
--name-only` -- but only because the four files it says "the block moved"
about really were touched. `scripts/measure_channel_drift.py` dropped off the
table because the diff now touches it, not because the generator learned to
tell an untouched file from a moved block. R338 third clause is closed by
circumstance.

**R350. (recordable, 4a) Two small things, one of them mine.**
`tests/corpus/tolerance_marker_exemptions.txt:215` carries `measured=clean`,
outside the two-value vocabulary the file own header declares -- that entry is
mine and I am recording it against myself, and it matters more now that R341
proposes reading that field. And `tests/test_collected_set_golden.py:68`
asserts a bare integer floor on the golden size: a vacuity backstop, fine as
one, and it should say so rather than look like a threshold.

## Tolerances touched

**No tolerance VALUE moved this round.** The diff over `floatfea/tolerances.py`
is one hunk of three comment lines.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (unchanged) | dimensionless, ULP of the channel own amplitude -- the right form | `3.0`, injected beyond the site clean deviation | `docs/milestones/F2.md:1116-1152` and `tolerances.py:1024-1035`, one story, re-measured from the ten leg artifacts at verdict 38 |
| `INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER` | `3.0` (unchanged) | dimensionless, three ULP beyond whatever the site already carries | itself; the assertion is now `drift == expected_drift`, exact | same run; the noun corrected at `:1054-1055` -- **R340 closed** |
| everything else | unchanged | -- | -- | the diff over value lines is empty |

```
cmd  the diff over floatfea/tolerances.py filtered to lines with Final
out  (empty)
cmd  offending() over every *.py in tests/ and scripts/       (my run, 389d416)
out  0 files reported -- no new undeclared literal entered the tree, and the
     one R336 named is gone rather than declared
judge THE EPSILON IS REMOVED, NOT RELOCATED, which is the better of the two
     repairs the condition allowed: the comparison is exact and I confirmed
     last round that it is exact to the bit in all fourteen forced cells.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** This is the first round in
fourteen where the ladder GAINED coverage rather than losing or re-describing
it: three green tests are back verbatim, a new guard makes the next silent
deletion a build failure and I could get neither a deletion nor a rename past
it, the workflow discarded gate is repaired and the run at this very commit
measures the repair, and the undeclared epsilon is gone rather than declared.
R333 -- the worst finding this milestone has produced -- is properly closed.

**What holds is not new work. It is four closing conditions answered at some
of the sites they named and not at others, and two guards that certify the
opposite of what they say.**

1. **R341 -- the escape golden asymmetry is a convention, not a check.**
   Three real regressions filed as growth with a false provenance string and
   the suite green. The field that would make it real -- `measured=` -- is in
   the corpus and is parsed and discarded. The stale header above the map
   goes with it.
2. **R342 -- `test_a_documentation_commit_runs_no_job`** passes on the
   `paths-ignore` hole and fails on its fix, and §8 says the ignore list
   moved when the diff says it did not.
3. **R343 -- R335 second site.** The `needs:` edge is gone; the cheap-first
   "because" it was recorded with is unchanged and the cell refuting it is in
   the repository.
4. **R344 -- R337 second clause.** `test_a_swapped_sign_is_orders_away_from_
   the_band` measures no distance from the band.
5. **R345 -- R338 middle clause.** Neutering the raise and keeping its
   message is green; the docstring says the script is imported and it is read.
6. **R346 -- §0 names the wrong commit** and publishes the wrong one of CK2
   two shapes for the one under review.

**CI at `389d416` is `unavailable -- allowance exhausted`**, the CK2 third
state: four jobs, none started, the billing annotation, two seconds. Neither
red nor green, and nothing is claimed from it in either direction. The last
run that executed, `34546580003` at `8942cdc`, no longer describes this tree
-- 580 lines across seven files since -- and the report says so. Two of the
six items above are in the workflow, and they are cheaper to fix before
minutes return than after.

**Not gates on step 5, into the next report Carried section:** R347, R348,
R349, R350, R330, R331, R332, the §9 table status-versus-subject disagreement
now covering R318-R320 and R326-R329, R321, R322, R300, R291, R292, R281,
R231/R244/R245/R275 behind the canonical render, R223, R224, R230, R261, the
underlying gap in R276, R277, R262, R264, R266, the two R248 residues,
R249-R252, R225-R228, R232, R233, and everything already at 4a.

**Adversarial corpus (BE3): 20 new entries in one file, all unseen by the
implementer, every `measured=` taken at `389d416` by running the shipped
`offending()` before the `expect=` beside it was written.**

**The coverage measurement, stated plainly: of my 20 new entries the shipped
scanner does what the entry requires on 5, and 15 are misses.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+20 (105 -> 125), 5
  correct.** The last two rounds asked whether a literal is seen where it
  sits. These ask a different question: whether a tolerance reaches the
  comparison through a NAME BINDING the scanner never reads -- a class
  attribute, an annotated ClassVar, a dataclass field default, an `Enum`
  member, a `parametrize` argument, a loop variable drawn from a literal
  list, a `getattr` default, a `**kwargs` dict, a `SimpleNamespace`
  attribute, a `try/except` fallback -- and through constructions with no
  `Compare` node at all: `operator.lt`, `np.clip`, `float("1e-09")`,
  `decimal.Decimal`, `np.array([...])`. **Three of the eighteen
  `expect=caught` are caught** -- `functools.partial(atol=)`, a bare
  `while err > 1e-09` convergence loop, and a `match`/`case` guard -- and
  **both `expect=exempt` controls pass**, so the guard remains usable, which
  matters more than any single miss.
* **None of the fifteen is an exotic construction.** A class attribute and a
  dataclass field default are how a tolerance is ordinarily written by
  someone not trying to hide one. That is the difference between these and a
  puzzle-box corpus, and it is why the reach is worth more at 4a than the
  ratio alone suggests.
* **What they measure THIS round is not the scanner but R341.** Fifteen new
  names arrive in the measured set, `test_the_known_misses_are_exactly_these`
  goes red, and the only way back to green is fifteen lines each carrying a
  provenance string nothing checks -- the same keystroke a genuine regression
  needs. The corpus is the demonstration; the finding is the mechanism.
* **No entry was added to `g21_rigid_body_frames.txt`.** R332 stands: nothing
  reads it, and adding to a corpus no runner executes measures nothing.

**WHAT MY CORPUS DOES TO THE SUITE, SAID UP FRONT SO IT IS NOT MISTAKEN FOR A
DEFECT.** At my corpus commit `tests/test_marker_exemption_corpus.py` is **16
failed, 78 passed** (my run) against `94 passed` at `389d416`. All sixteen are
mine: the fifteen misses, plus `test_the_known_misses_are_exactly_these`,
which is that file working as designed. Closing R341 does not close these; the
scanner reach is 4a and the entries are there to size it.

**Thirty-nine rounds have found no element defect, and this round does not
either.** `floatfea/` has been comment-only for fourteen rounds. By the rule I
am bound by that still means "not yet contradicted", because V5.1 against
CalculiX has not run. Last round the instruments lost ground; this round they
gained it back and more, and what remains is six conditions to finish rather
than anything to rebuild.
