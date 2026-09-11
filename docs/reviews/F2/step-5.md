# Review � F2 step 5
Reviewed commit: cbde0e4b3567f4f0b7966f69e0deb4a68021816a
Verdict: HOLD

**Reviewed commit: `cbde0e4`.** Report revision 12, `Answers: verdict 37 @ 2e6276c`.

Tests: **2058 passed, 2 failed, 0 skipped** (my run at `cbde0e4` on a clean tree,
`python -m pytest -q`, 427.70 s, Python 3.13.15 on Windows). The two failures are
the two §7 and §9 name, and both are mine from last round's corpus. **The suite
collects 2060; three of the tests it no longer collects are green rung-4 tests
this round deleted without a word anywhere -- R333.**

**Commits: ci `83bffc1`. Plan `0b78244` (standalone, RE-LOCKED). Code `be534a8`,
`361adce`, `db219a6`. Process `36052b8` (standalone). Report `cbde0e4`.**

**Item 1b.** Header line 3798 reads `Answers: verdict 37 @ 2e6276c`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`2e6276c81892975e17c7c38872cbee880aaf11e9`. It is the latest. **Passes.**

**CI, item 3b, AT THE COMMIT I AM REVIEWING: UNAVAILABLE -- AND NOT IN THE SHAPE
CK2 DESCRIBES.** I checked the classification rather than accepting §0, which
describes `d384e41` and not this commit.

```
cmd  gh run list --limit 8 --json headSha,conclusion,event
out  34567325589  push  failure  @ cbde0e4     -- and NO pull_request twin
cmd  gh api repos/xabi80/FloatFEA/actions/runs/34567325589/jobs --jq .total_count
out  0
cmd  gh api repos/xabi80/FloatFEA/commits/cbde0e4.../check-runs --jq .total_count
out  0
cmd  the same job count for the three runs before it, all under the same block
out  34549514338 : 20     34548439279 : 20     34546580003 : 20
judge THIS IS A DIFFERENT SHAPE FROM THE ONE CK2 NAMES. Every run under the old
     workflow created its twenty jobs and then failed to start them --
     runner_name empty, no steps, the billing annotation. The first run under
     the NEW workflow created no jobs at all and no check-runs at all, and
     concluded failure. Zero jobs is not "jobs that did not start".
cmd  python scripts/ci_section.py cbde0e4
out  gh run view 34567325589 --log failed: failed to get run log: log not found
judge THE REPOSITORY'S OWN GENERATOR CANNOT DESCRIBE THE REVIEWED COMMIT. It
     crashes. never_started() is correctly guarded with bool(jobs) -- I checked
     that guard and it is right, an empty list is not the third state -- so the
     run falls through to counts(), which needs a log there is none of.
judge RECORDED AS UNAVAILABLE, NOT AS RED AND NOT AS THE THIRD STATE. What I
     cannot do from outside is separate "the allowance now blocks job creation
     entirely" from "the workflow file no longer parses". R334 is that the
     workflow contains a duplicate mapping key introduced by `83bffc1`, which
     makes the second reading live whether or not it is the cause here.
cmd  gh api .../runs/34546580003/jobs   (the last run that EXECUTED, @ 8942cdc)
out  6 of 6 ladder jobs success; "guards and meta-tests" FAILURE; rest green
cmd  git diff --stat 8942cdc..cbde0e4 -- tests/verification scripts .github
out  NOT empty: .github/workflows/ci.yml, scripts/ci_section.py,
     scripts/run_rung.sh, scripts/suite_count.py,
     tests/verification/rung4/test_writer_round_trip.py
judge SO THE LADDER-GREEN CLAIM NO LONGER SURVIVES THE GAP UNCHECKED, and §0a
     still says "every ladder job is green including 4 and 5" without saying
     that rung 4's own module has since lost three tests and gained a rewritten
     counter. I re-ran it: sh scripts/run_rung.sh full:tests/verification/rung4
     gives `85 collected, 0 failed` where verdict 37 recorded `88 collected`.
cmd  gh pr view 1 --json comments
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

**My own instructions (4b) and the conftest pathspec (4c).**

```
cmd  git diff 2e6276c..cbde0e4 -- .claude docs/SUPERVISOR.md
out  36052b8 ONLY. Standalone `process:` commit citing CK2, touching those two
     files and nothing else. I read both hunks line by line.
judge THE ROUTE IS CORRECT AND THE CONTENT IS PURELY ADDITIVE. 26 insertions, 0
     deletions across the two files. It adds `unavailable -- allowance
     exhausted` as a third state, with the command that identifies it and the
     instruction to name the last run that executed and diff the code since.
     CA2 is left standing in both files -- the words "A red CI is a HOLD" are
     still there and I checked for them. Nothing was removed. ACCEPTED.
judge AND I USED IT TO FIND ITS OWN BOUNDARY. The state it defines is keyed on
     "jobs with no steps". The reviewed commit has no jobs. The instruction is
     right for what it describes and silent on what happened here, which is
     why R334 records the shape rather than forcing it into the vocabulary.
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 2e6276c..cbde0e4 -- tests/conftest.py 'tests/**/conftest.py'
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py    -- still the whole set, and no plugin was added
```

## Carried

Verdict 37 listed seven blocking items and three at 4a. **Three close outright
(R323, R325, R327). One closes at its mechanism and not at its published figure
(R326). One closes at one of two named sites (R329). R324's repair is right and
the line below it is a new finding. R328 is answered in prose and contradicted
by the file it describes.**

- **R323 -- CLOSED, and the fix is better than what I asked for.**
  `scripts/suite_count.py:97-118` builds `git worktree add --detach` at the sha
  it prints, so the number is reproducible by anyone at that commit, and the
  line states its exclusions inline. §0a names `8942cdc` as the last run that
  executed. Both halves of the condition are met. **The exclusion itself is
  R339 and it does not reopen this.**

- **R324 -- CLOSED, and I tried to break the repair rather than read it.**

```
cell the shipped test's own arithmetic, the site forced to -2, -1, -0.5, 0,
     +0.5, +1, +2 ULP, both parametrised channels      (my run, cbde0e4)
out  clean -2.0 -> drift 5.0000   clean -1.0 -> 4.0000   clean -0.5 -> 3.5000
     clean +0.0 -> 3.0000         clean +1.0 -> 4.0000   clean +2.0 -> 5.0000
     14 of 14 cells: drift > 2.0 OK, and drift >= expected - 1e-9 OK
judge THE MARGIN IS NO LONGER DECIDED BY A LIBM. `direction` carries the
     injection AWAY from the reference, so the measured drift is |clean| + 3
     for any clean and the margin against the band is |clean| + 1 >= 1. The old
     form failed at clean = -1; the new one cannot. The added assertion cannot
     fire spuriously either, and I checked the arithmetic is exact rather than
     close: got[0,0] and 3*ulp(ampl) are both multiples of ulp(ampl) at these
     magnitudes, and all fourteen cells land on the prediction to the bit.
cmd  the operating point the entry records, re-measured here
out  position clean at [0,0] = 0.0 ULP;  acceleration clean at [0,0] = 0.0 ULP
     canonical channel bounds, run 34545832426 leg 4: position 0.5,
     acceleration 1.0 -- so "up to 1.0 ULP on the canonical machine" is a
     correct BOUND and the entry says "up to" rather than claiming the value
judge ONE WORD IS WRONG AND IT IS NOT WORTH A GATE: "the margin is one ULP by
     construction" is a floor, not the margin. Recorded as R340, 4a.
```

- **R325 -- CLOSED, and I re-took the measurement from the artifacts rather
  than from the report.**

```
cmd  gh run download 34545832426 -n determinism-leg-N, N = 1..10; cpu.txt and
     channel_drift.txt read leg by leg                          (my run)
out  leg1 EPYC 7763   leg2 Xeon 6973P-C  leg3 EPYC 9V74  leg4 EPYC 7763
     leg5 EPYC 9V74   leg6 Xeon 6973P-C  leg7 EPYC 9V74  leg8 EPYC 7763
     leg9 EPYC 9V74   leg10 EPYC 9V74;  worst 1.0000 ULP on all ten
judge DIGIT FOR DIGIT WHAT `docs/milestones/F2.md:1129-1132` NOW SAYS, per leg
     and per model. `six models` is gone from the plan, the tolerance entry and
     the test docstring -- three sites, and I grepped for the phrase.
judge AND THE CONTRADICTION IS RESOLVED IN THE HONEST DIRECTION. The plan and
     `tolerances.py:1024-1029` both now say the band came FROM the thirteen
     pairs and is twice their worst, and both say in as many words that this is
     "a tolerance derived from the disagreements it now admits". That is the
     harder of the two stories to tell and it is the true one.
```

- **R326 -- CLOSED AT TWO OF THE THREE THINGS ITS CONDITION NAMED. The third is
  refuted by a sentence the same commit wrote.** Carried as **R337**. The
  scanner's reach was 4a and stays there; what does not stay there is R336.

- **R327 -- CLOSED.** `grep -rn "LAST bound"` over the tree returns nothing.
  `scripts/run_rung.sh:194-197` now reads "WHAT PROTECTS A RUNG IS REVIEW OF ITS
  CONFTEST (CJ0). That is the bound, not the last of several", and the
  enumeration at `:155-170` is six channels with CAUGHT or "walks past" against
  each. Fourth site, and it matches the other three.

- **R328 -- ANSWERED IN PROSE AND CONTRADICTED BY THE FILE.** The docstring's
  first line is now "a record the WRITER produced, round-tripped against its
  closed form", the sidecar route is recorded with the reason it was not taken,
  and both halves of the condition are literally met. But the same commit
  deleted the test the new docstring at `:164` says is still doing the work, so
  the module makes a false statement it did not make before. That is **R333**,
  not a reopening of R328.

- **R329 -- CLOSED AT ONE OF THE TWO SITES ITS CONDITION NAMED.** Carried as
  **R338**.

- **R330, R331, R332 -- OPEN at 4a, correctly listed in §8 and §11.** R330's
  site rows say "recordable at 4a in the verdict's own classification, and not
  answered this round", which is accurate. R331 is recorded in §10 rather than
  by rewriting a published message, which is the right call.

- **R315, R316, R317 -- closed in verdict 37**, correctly carried, not reopened.
  R315's fourth site is R327 above and it is done.

- **R318, R319, R320 -- closed in verdict 37**, carried with status `open` while
  the subject column beside them reads "CLOSED." The generated table's two
  columns disagree for these three. Cosmetic, still 4a.

- **R231, R244, R245, R275 -- OPEN, and correctly declared blocked** on the
  canonical re-render in §8. I accept that: the block is outside the repository
  and §7 records this laptop's values labelled non-canonical rather than
  committing them. That is the right behaviour under the block.

- **R223, R224, R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a, correctly
  recorded.**

- **R302 -- accepted at verdict 37, not reopened.**

- **R293, R303-R308 -- closed in verdict 35**, correctly carried.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried, and correctly
  present in the generated table.**

## Findings

**R333. (BLOCKS -- the gate's assertion set at rung 4, and the truth of two
sentences in the file that lost it) Three green tests were deleted from
`tests/verification/rung4/test_writer_round_trip.py` in `be534a8`; nothing in
the commit message, the report or the plan records it; and the same file still
cites two of them as live.** `tests/verification/rung4/test_writer_round_trip.py:99`
and `:164`; the `be534a8` diff at the old `:211`, `:226`, `:249`.

```
cmd  git show 2e6276c:tests/.../test_writer_round_trip.py | grep -n "^def test"
out  :193 test_the_band_is_not_wide_enough_to_hide_a_swapped_sign
     :211 test_channels_are_not_interchangeable
     :226 test_a_validation_error_SURVIVES_propagation
     :249 test_mu_is_present_and_not_all_zero
cmd  the same at cbde0e4
out  the first is RENAMED to test_a_swapped_sign_is_orders_away_from_the_band.
     THE OTHER THREE ARE GONE.
cmd  grep -rn for the three names over the whole tree, --include=*.py
out  two hits, both PROSE inside the file that deleted them:
       :99  "...the shape a writer that forgot a channel produces, and is why
             `test_mu_is_present_and_not_all_zero` exists."
       :164 "the channels are still each other's controls
             (`test_channels_are_not_interchangeable`)"
cmd  grep -rn "__traceback__" tests/ ; grep -rn "radiation/mu" tests/ ;
     grep -rln "matches velocity" tests/
out  (nothing) (nothing) (nothing) -- all three properties are asserted NOWHERE
     in the repository now
cell the three restored verbatim into a scratch module at this commit, run
out  3 passed in 0.15s      -- THEY WERE GREEN WHEN THEY WERE DELETED
cmd  sh scripts/run_rung.sh full:tests/verification/rung4    (my run, cbde0e4)
out  run_rung: 85 collected, 0 failed        -- verdict 37 recorded 88
judge THIS IS THE FIRST FINDING IN THIRTEEN ROUNDS THAT REMOVES COVERAGE RATHER
     THAN MISDESCRIBING IT, and the one it removes is the worst to lose this
     round. test_channels_are_not_interchangeable is the answer to "if the
     thing this rung claims were false, would it go red": it is what stops the
     band test passing on a writer that emitted velocity into the position
     dataset. The round BEFORE this one relaxed those same twelve pairs from
     bit-exact to a two-ULP band. A band with no interchangeability control is
     strictly weaker than either alone, and nothing anywhere says so.
judge test_a_validation_error_SURVIVES_propagation IS A REGRESSION TEST FOR A
     REAL RECORDED FAULT -- a frozen dataclass refusing __traceback__, so a
     named rejection arrived as FrozenInstanceError. Its own docstring says the
     rejection matrix cannot see that path. It is now untested.
judge AND THE FILE ARGUES FROM A TEST IT DELETED. Line 99 justifies R329's new
     raise by pointing at test_mu_is_present_and_not_all_zero. That is the BF0
     species exactly -- a sentence a reader trusts, refuted by one grep -- and
     worse than the usual instance, because the sentence is the justification
     for a change made in the same commit.
judge WHAT I CANNOT TELL, and I say so rather than guess: whether it was
     intended. The rewrite replaced a function two above them and the diff ends
     with three functions removed and nothing added, which is what an
     overwritten file tail looks like. Either way, §10 lists nineteen
     test_writer_round_trip.py line numbers as "the block moved" and none of
     them is this.
```

**Closed when** the three are restored, or each deletion is argued in the report
with the measurement of what now covers the property; and lines 99 and 164
describe tests that exist; and the report reconciles `88 collected` with
whatever the rung collects.

**R334. (BLOCKS -- the truth of a published figure, and the check CA2 depends
on) `83bffc1` leaves a duplicate `if:` key in one job, so CK0's central change
is discarded by the second reading, and no guard asserts any of CK0's claimed
properties except the two ordering ones.** `.github/workflows/ci.yml:194` and
`:196`; report §6; `83bffc1`'s message.

```
code   determinism_verdict:
         if: github.event_name == "workflow_dispatch"    <- added by 83bffc1
         needs: [determinism]                               (quotes normalised)
         if: always()                                    <- already there
cmd  a duplicate-rejecting YAML loader over the file               (my run)
out  DUPLICATE KEY: "if" at line 196
cmd  yaml.safe_load(...)["jobs"]["determinism_verdict"]["if"]
out  always()             -- the CK0 line is the one thrown away
judge SO ON A CODE PUSH THE JOB RUNS. always() runs it whatever needs did,
     determinism is skipped, the download finds no legs, and the job hits
     sys.exit("<n> legs reported, expected 10"). That is THREE jobs per push,
     one of them red by construction, against §6's "the determinism legs are
     workflow_dispatch only" and 83bffc1's "Expected cost per push is two
     jobs".
cmd  grep -n for workflow_dispatch, event_name, paths-ignore, concurrency and
     pull_request over tests/*.py
out  (nothing)
judge FIVE OF CK0'S SEVEN CLAIMS ARE ASSERTED NOWHERE. The two ordering
     properties ARE asserted, well, and I ran them: `15 passed` over
     test_ci_runs_the_whole_suite.py and test_ci_determinism_gate.py, and the
     rewritten ladder-6 test reads the step order and would catch a
     reordering. The pull-request drop, paths-ignore, concurrency, the
     dispatch gate and the job merge are prose. Under BF0 each is a claim
     without a command, and the one I checked is false.
judge THE OTHER HALF OF THE FIRST BULLET IS TRUE AND I CHECKED IT: the run at
     cbde0e4 has no pull_request twin, where the three runs before it all had
     one. The trigger change works.
judge PATHS-IGNORE HAS A HOLE WORTH NAMING NOW RATHER THAN LATER.
     `docs/milestones/**` is ignored and `docs/milestones/F2_figures.md` is the
     canonical render Q8 exists to produce. A commit that lands the canonical
     file and nothing else will not be checked by CI -- the one commit in this
     milestone that most needs to be.
```

**Closed when** the job has one `if:`; a guard asserts that both determinism
jobs are `workflow_dispatch`-gated and that the workflow has no duplicate
mapping key; §6 and the commit message's "two jobs per push" are re-taken or
withdrawn; and the `F2_figures.md` hole in `paths-ignore` is closed or recorded
with its reason.

**R335. (BLOCKS -- what CI is able to measure, and the evidence this step rests
on) CK0 puts the whole ladder behind the guards job, and the one CI run this
milestone relies on is a run where the guards were red and the ladder was
green.** `.github/workflows/ci.yml`, the `checks:` step list and
`ladder: needs: [checks]`.

```
cmd  gh api .../runs/34546580003/jobs, conclusion by job name
out  failure  guards and meta-tests
     success  ladder 1 ... ladder 6, lint and type-check, unit tests, all ten
              determinism legs, and the verdict job
cell ONE VARIABLE MOVED, THE COMMIT HELD: the same tree under the new shape.
     "guards and meta-tests" is now the fifth STEP of checks; steps stop at the
     first failure; ladder has needs: [checks].
out  checks red -> ladder SKIPPED. Six ladder results become zero.
judge THE SENTENCE THIS STEP HAS LEANED ON FOR TWO ROUNDS -- "ladder 4 and
     ladder 5 are green on the canonical machine" -- COULD NOT HAVE BEEN
     PRODUCED UNDER THE NEW WORKFLOW. Not hypothetical: it is the only run in
     the range that executed.
cell the second instance, also measured rather than argued: at d2bbcdd the red
     was "lint and type-check", a ruff E501 (verdict 37, R331)
out  under the old shape that run still gave unit, guards and all six ladder
     jobs. Under the new one a line-length violation hides the unit tests, the
     guards and the entire ladder.
judge §6 SAYS THE ORDER "IS NOT ARBITRARY: LINT AND TYPE-CHECK TAKE SECONDS AND
     CATCH THE CLASS OF DEFECT THAT MAKES THE REST MEANINGLESS." That is a
     causal sentence (BG0) with no cell, and the repository holds the cell that
     refutes it: an over-long line did not make rung 4 meaningless, and under
     the new shape it would have stopped it.
judge WHAT I AM NOT SAYING. Collapsing six ladder JOBS into six ladder STEPS is
     right -- the dependency order is preserved exactly, I checked that rung 6
     moved ahead of rung 4 as claimed, and the guard asserting it now reads
     step order rather than the needs graph. What is wrong is the
     needs: [checks] edge and the lint-first ordering inside checks, which
     convert a diagnostic red into a total loss of evidence on a machine nobody
     controls -- the exact thing CA2 exists to get.
```

**Closed when** a red in "guards and meta-tests", or in lint, no longer
suppresses the ladder -- a separate job, or the guard steps last, or
`continue-on-error` with a final gate -- and the choice is recorded with the
measurement above rather than with the interpretability argument, which does not
apply to lint.

**R336. (BLOCKS -- a tolerance in the form of an undeclared comparison epsilon,
inside the counter's own assertion) R326's repair reintroduces the species it
closed, three lines below where the `1e12` was removed, and the scanner the
same commit built cannot see it.**
`tests/verification/rung4/test_writer_round_trip.py:239`;
`tests/test_no_tolerance_literals.py:124-197`;
`tests/test_marker_exemption_corpus.py:51-54`.

```
code assert drift >= expected_drift - 1e-9
cmd  offending(Path("tests/verification/rung4/test_writer_round_trip.py"))
out  []                                                      (my run, cbde0e4)
cmd  the same scanner on `assert x < 1e-9` alone
out  [(1, "comparison against 1e-09")]
cmd  the same scanner on `assert x < eps - 1e-9`
out  []
judge THE DIFFERENCE IS THE LOCAL NAME. _literal_thresholds_inside requires a
     DECLARED tolerance name inside the BinOp; `expected_drift` is a local, so
     the branch returns before it looks, and the root Constant branch never
     sees a BinOp. CLAUDE.md sec. Tolerances names "comparison epsilons" in the
     list of things that are tolerances under another name.
judge AND THE ESCALATION CONDITION HAS FIRED AGAIN, ON THE SAME LINE OF THE
     SAME FILE. tests/test_marker_exemption_corpus.py:51-54 still reads "they
     go to 4a by name unless one exposes a false pass on a real file in the
     tree. None does -- the scanner is clean over every file in tests/,
     measured, not assumed." One does, and it is three lines from the last one.
     The bound is UNCHANGED and it is false again.
cell IS THE SLACK EVEN NEEDED? the fourteen cells of R324 above
out  drift equals expected_drift to the bit in all fourteen. The slack is
     protecting against nothing that was measured.
judge A CORPUS MEASUREMENT RATHER THAN A PLANTED COUNT: 20 unseen shapes, 13
     missed. Detail at the foot of this verdict.
```

**Closed when** the `1e-9` is a declared constant in `floatfea/tolerances.py`
with its own basis, or removed because the comparison is exact, or the
assertion is rewritten with no epsilon in it; and the sentence at
`test_marker_exemption_corpus.py:51-54` says something true at the commit that
publishes it.

**R337. (BLOCKS -- BP0, and R326's second named condition) The "fourteen
orders" figure was deleted rather than regenerated, and the docstring that
replaced it says the figure lives in the step report, where it does not.**
`tests/verification/rung4/test_writer_round_trip.py:258-260`; report §4.

```
code lines 258-260 "the ORDERS between it and the band are then a published
     figure in the step report, where a figure belongs"
cmd  grep -n for order, 15.7, "sign flip", swapped over revision 12
     (report lines 3796-4239)
out  four hits, all of them the words "ordering properties" and "in order".
     NO SUCH FIGURE IS PUBLISHED.
judge VERDICT 37 NAMED THREE THINGS AND THE REPORT DID TWO. The literal is gone
     (first clause) and the docstring says what the control does not read
     (third clause). The middle clause -- "the published figure is the one the
     run prints" -- was answered by deleting the figure and then asserting in
     the file that it had been published elsewhere.
judge AND ONE PROPERTY LEFT WITH IT, which is the part that is not bookkeeping.
     The old assertion, weak as it was, compared a sign flip AGAINST THE BAND.
     The new one compares a measurement against its own prediction and never
     mentions the band. Nothing in the repository now asserts that this band
     cannot hide a swapped sign. I measured the figure: 1.0628e+16 ULP against
     a band of 2.0, which is 15.73 orders.
judge THE TEST NAME ALSO STILL CLAIMS THE OLD PROPERTY:
     test_a_swapped_sign_is_orders_away_from_the_band measures no distance from
     the band.
```

**Closed when** the figure is published in the report with its rule, or the
docstring stops saying that it was; and either the name matches what the test
asserts, or the band comparison returns as its own assertion.

**R338. (BLOCKS -- R329 at one of the two sites its condition named, and a
generated table that gives a false reason for the other)
`scripts/measure_channel_drift.py:93` still defaults a zero amplitude to `1.0`,
and §10 says the diff touches that file.** `scripts/measure_channel_drift.py:93`;
report §10, the row for that path.

```
cmd  git diff 2e6276c..cbde0e4 -- scripts/measure_channel_drift.py
out  (empty)
code measure_channel_drift.py:93   ampl = float(np.max(np.abs(ref))) or 1.0
code report §10  "| scripts/measure_channel_drift.py:93 | no change -- the diff
     touches this file and the block moved; the finding's line numbers are the
     old ones |"
judge THE REASON IS FALSE AND IT IS THE GENERATED ONE. The diff does not touch
     that file. Whatever produces that column decided "the block moved" for a
     file with no hunks, which means the same sentence on the other eighty-odd
     rows is not evidence of anything either. Verdict 37 already recorded that
     the table works at file granularity; this is worse than coarse, it is
     wrong.
judge AND THE ITEM IS HALF DONE, which is the species CLAUDE.md records under
     "a closing condition that names sites is closed site by site". The
     condition read "in both the test helper and the script". The helper raises
     and names the channel, well, and I read it. The script does not. §11 lists
     R329 as answered.
cmd  grep -rn "identically zero" over tests/, looking for a control on the raise
out  three hits, none of them this. NOTHING ASSERTS THAT _drift_ulp RAISES.
judge A GATE CARRIES ITS OWN FAILURE. The new raise is three lines that no test
     executes; put `or 1.0` back and the suite stays green. Cheap to fix, and
     part of the same item.
```

**Closed when** the script raises as the helper does, a test reddens when the
raise is removed, and the §10 generator either states the true reason for a
file with no hunks or that row is written by hand.

**R339. (recordable, 4a) CL1's exclusion is legitimate in mechanism, and the
line does not let a reader size it.** `scripts/suite_count.py:51-59` and
`:119-126`; report §9.

```
cmd  pytest --collect-only -q over the three excluded files, and over all
out  325 collected   /   2060 collected                       (my run, cbde0e4)
judge 15.8% OF THE SUITE. The line names the three files, which is enough for a
     reader to go and look, and the reason is real -- I confirmed it: those
     files are parametrised over the report being written, so a count taken at
     the parent describes a tree that does not exist. I ran all 325 myself and
     they are green in the main tree. THE EXCLUSION IS NOT A GREENER NUMBER and
     I checked rather than assumed it.
judge WHAT IS MISSING IS THE SIZE. "Whole suite ... 1733 passed" with no count
     of what was left out cannot be reconciled with last round's 2067, and in
     the one round where three tests silently vanished (R333) that arithmetic
     is the only place it would have shown.
judge ONE MORE THING THE EXCLUSION HIDES, found by running the count's own
     method: in a `git worktree add --detach` checkout of cbde0e4,
     tests/test_report_guard_states.py is `3 failed, 23 passed`; in the main
     tree it is `26 passed`. The file is not worktree-portable. That is a real
     property of a guard, and the instrument that would have surfaced it is the
     instrument that excludes it.
```

**R340. (recordable, 4a) One word in a tolerance entry.**
`floatfea/tolerances.py:1055` says "the margin is one ULP by construction". The
margin is `|clean| + 1` ULP; one is its floor. The measurement is right and the
noun is wrong.

## Tolerances touched

**No tolerance VALUE moved this round.** `git diff 2e6276c..cbde0e4 --
floatfea/tolerances.py` is thirty lines and every one of them is a comment; I
read the hunk and checked that the two `Final[float]` lines are unchanged at
`2.0` and `3.0`.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (unchanged) | dimensionless, ULP of the channel's own amplitude -- the right form | `3.0`, now injected beyond the site's clean deviation -- **R324 closed** | `docs/milestones/F2.md:1116-1152` and `tolerances.py:1024-1035`, ONE story now, re-measured by me from the ten leg artifacts -- **R325 closed** |
| `INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER` | `3.0` (unchanged) | dimensionless, three ULP beyond whatever the site already carries | itself, and the test now asserts the measured drift equals what was injected | same run; operating point recorded and correct; the word "margin" is **R340** |
| everything else | unchanged | -- | -- | the diff over value lines is empty |

```
cmd  git diff 2e6276c..cbde0e4 -- floatfea/tolerances.py | grep "^[+-].*Final"
out  (empty)
cmd  the counter's new form, fourteen forced states           (my run, cbde0e4)
out  every one passes with margin >= 1 ULP; the sweep is under R324, above
judge THE COMMENT'S CAUSAL PARAGRAPH IS NOW EARNED. "Added to the reference, a
     3 ULP injection at a site the canonical machine already holds 1 ULP low
     measures 2 against a band of 2" -- that is the cell, it is in the entry,
     and I reproduced both arms of it. BG0 satisfied.
judge AND THE NEW EPSILON IS NOT IN THIS TABLE BECAUSE IT IS NOT IN THIS FILE.
     That is R336.
```

**What held**, reproduced at my run rather than read: `ruff check floatfea
tests` and `black --check floatfea tests` clean; `mypy floatfea` clean over 25
source files; `109 passed` over the two scanner files; `15 passed` over the two
CI guards; `26 passed` over `test_report_guard_states.py` in the main tree;
`322 passed` over the three report guards; the ten determinism artifacts read
leg by leg; the fourteen-cell counter sweep; `85 collected, 0 failed` through
the shipped rung-4 gate script; the whole suite at `2058 passed, 2 failed, 0
skipped`; `36052b8` additive and by the right route; no conftest changed and no
plugin added.

**These did not**: three deleted rung-4 tests and the two sentences that still
cite them (R333), a duplicate `if:` and five unasserted CK0 claims (R334), a
ladder now suppressed by a lint error (R335), a new undeclared epsilon inside
the counter's assertion (R336), a figure said to be published and absent
(R337), R329's second site and a generated reason that is false (R338).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Three of the seven items close
cleanly and one of them -- R324 -- is the round's real work: the counter's
margin is now a property of arithmetic rather than of a libm, and I could not
break it in fourteen forced states. R325 is right to the leg. R327 closes
R315's last site. **What holds this round is neither the element nor the
counter. It is that a commit removed three green assertions from the
verification ladder without saying so, and that the workflow rewritten in the
same round both discards its own central change and would have suppressed the
only CI evidence this step has.**

1. **R333 -- three tests deleted from rung 4, silently.** `85 collected` where
   the last verdict recorded `88`. The interchangeability control is what made
   the new band able to fail on a swapped channel, and the file still names it
   in a sentence.
2. **R334 -- `.github/workflows/ci.yml:194/196` has two `if:` keys**, so CK0's
   dispatch gate is discarded, and five of CK0's seven claims are asserted by
   nothing.
3. **R335 -- `ladder: needs: [checks]`.** At `8942cdc` the guards were red and
   all six ladder jobs were green; under the new shape that run yields no
   ladder result at all.
4. **R336 -- `assert drift >= expected_drift - 1e-9`**, three lines below the
   literal R326 removed, invisible to the scanner R326 built, and the
   known-miss bound's escalation condition has fired again on the same file.
5. **R337 -- the orders figure**, said in the file to be published in the
   report and absent from it; and nothing now asserts the band cannot hide a
   sign flip.
6. **R338 -- R329's second site**, plus a §10 row whose generated reason is
   false.

**CI is UNAVAILABLE at the reviewed commit, in a shape neither instruction file
describes: zero jobs, zero check-runs, conclusion `failure`, and the section
generator crashes on it.** Nothing may be claimed from it in either direction.
Two of the six items above are about the workflow itself, and they are better
fixed before minutes return than after: the first green run under a broken
shape is the most expensive kind of reassurance.

**Not gates on step 5, into the next report's Carried section:** R339, R340,
R330, R331, R332, the generated table's status-versus-subject disagreement on
R318-R320, R321, R322, R300, R291, R292, R281, R231/R244/R245/R275 behind the
canonical render, R223, R224, R230, R261, the underlying gap in R276, R277,
R262, R264, R266, the two R248 residues, R249-R252, R225-R228, R232, R233, and
everything already at 4a.

**Adversarial corpus (BE3): 20 new entries in one file, all unseen by the
implementer, every `measured=` taken at `cbde0e4` by running the shipped
`offending()` before the requirement beside it was written.**

**The coverage measurement, stated plainly: of my 20 new entries the shipped
scanner does what the entry requires on 7, and 13 are misses.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+20 (85 -> 105), 7
  correct.** Last round's nine were all one species -- a literal riding on a
  DECLARED name -- and the rule that closed them is keyed on that species, so
  measuring it against them measures it against itself. These twenty move off
  that axis: a literal beside a LOCAL name (the shape shipped in the tree at
  `:239`), a product of two literals with no declared name anywhere
  (`assert r < 2.0 * 1e-09`), a literal divided by a literal, a unary plus, a
  `np.minimum` candidate, a `sorted(...)[0]`, an inline dict subscript, a
  conditional-expression branch, `abs(-1e-09)`, `float(1e-09)`, a walrus, an
  `isclose` keyword, and an integer iteration cap. **Five of the eighteen
  expect=caught entries are caught** -- a parenthesised literal, a declared
  name raised to a literal power, a chained comparison, a nested BinOp, and a
  negative list index -- and **both expect=exempt controls pass**, so the
  guard remains usable, which matters more than any single miss.
* **One entry contests the documented reach rather than reporting a miss.**
  `detect_integer_iteration_threshold` is an int and the scanner says it looks
  for float thresholds. `CLAUDE.md` sec. Tolerances names convergence
  thresholds, and an iteration cap is one. The disagreement is the point of
  recording it, and the file says so.
* **No entry was added to `g21_rigid_body_frames.txt` this round.** R332
  stands: nothing in the repository reads that file, and adding to a corpus no
  runner executes measures nothing. It grows again when it has a runner.

**WHAT MY CORPUS DOES TO THE SUITE, SAID UP FRONT SO IT IS NOT MISTAKEN FOR A
DEFECT.** At my corpus commit `tests/test_marker_exemption_corpus.py` is **14
failed, 73 passed** (my run) against `87 passed` at `cbde0e4`. All fourteen are
mine: the thirteen misses, plus `test_the_known_misses_are_exactly_these`,
which is that file working exactly as designed -- a new miss cannot appear
unnoticed. Closing R336 does not close these; the scanner's reach is 4a, and
the entries are there to size it rather than to gate it.

**Thirty-eight rounds have found no element defect, and this round does not
either.** `floatfea/` has been comment-only for thirteen rounds. By the rule I
am bound by that still means "not yet contradicted", because V5.1 against
CalculiX has not run -- and this is the first round in which the instruments
lost ground rather than gaining it.
