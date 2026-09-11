# Review � F2 step 5
Reviewed commit: d384e41e3aedb80d90f1625a840e719dd4e83fa8
Verdict: HOLD

**Reviewed commit: `d384e41`.** Report revision 11, `Answers: verdict 36 @ 900fe88`.

Tests: **2067 passed, 0 failed, 0 skipped** (my run at `d384e41` on a clean tree,
`python -m pytest -q`, 465.68 s, Python 3.13.11 on Windows). The report's figure
`2067` is the number my run produces. **The commit it names is not the commit it
measures** -- R323.

**Commits: plan `05102f4`, `3f0c7e9`, `8f2d610` (standalone, RE-LOCKED). Process
`e6baa21` (standalone). Code `0cada85`, `8942cdc`, `d2bbcdd`, `265b32f`. Report
`d384e41`.** `git diff 900fe88..d384e41 -- floatfea` is `tolerances.py` and nothing
else, for a twelfth round -- but this time it is not only a comment: two new
constants land, and the step's own content moved.

**Item 1b.** Header line 3317 reads `Answers: verdict 36 @ 900fe88`;
`git log -1 900fe88` is `review: F2 step 5 -- thirty-sixth verdict`, and
`git log -1 -- docs/reviews/F2/step-5.md` is the same commit. It is the latest.
**Passes.**

**CI, item 3b, at the reviewed commit: UNAVAILABLE. Not red, not skipped over, and
I checked the classification rather than accepting it.**

```
cmd  gh run list --limit 12 --json headSha,conclusion,workflowName
out  34549514969 (pull_request) failure   34549514338 (push) failure   @ d384e41
cmd  gh api repos/xabi80/FloatFEA/actions/runs/34549514969/jobs
out  20 jobs. 13 conclusion=failure with runner_name="", steps=[], started
     01:09:30Z completed 01:09:32Z -- two seconds, nothing executed.
     7 conclusion=skipped, runner_name=null, steps=[].
cmd  gh api repos/xabi80/FloatFEA/check-runs/103109279774/annotations
out  failure  "The job was not started because recent account payments have
     failed or your spending limit needs to be increased."
judge A JOB THAT WAS NOT STARTED IS NOT A JOB THAT FAILED. Zero steps, no
     runner, two seconds, and a billing annotation on every one. `265b32f` is
     the same. Per `docs/SUPERVISOR.md` this is an UNAVAILABLE check for the
     reviewed commit, and nothing about the repository can be read from it --
     including, importantly, anything reassuring.
cmd  gh api .../runs/34546580003/jobs      (the last run that EXECUTED, @ 8942cdc)
out  every ladder job SUCCESS, ladder 4 and ladder 5 included. The only red is
     `guards and meta-tests`, on the report revision this round replaces.
cmd  git diff --stat 8942cdc..d384e41 -- tests/verification scripts .github
out  (empty)
judge SO THE LADDER-GREEN CLAIM SURVIVES THE GAP, and I checked it rather than
     taking it: nothing under `tests/verification`, `scripts/` or `.github/`
     has moved since the run that measured it. What does NOT survive is the
     sentence saying where that run was taken (R323b).
cmd  sh scripts/run_rung.sh full:tests/verification/rung4   (my run, d384e41)
out  run_rung: 88 collected, 0 failed, 0 errored, 0 skipped
     run_rung: OK -- 1 director(y|ies) ran
```

**One CI red inside the range that nothing in the repository records.** At
`d2bbcdd` the run DID execute and `lint and type-check` failed: `ruff` E501 at
`tests/test_report_carried.py:781`. `265b32f` repaired it -- `ruff check floatfea
tests` and `black --check floatfea tests` are both clean at my run of `d384e41` --
but its message says "three repairs" and makes four, and the fourth is the one CI
found rather than one "found by running them". R331.

**PR #1 is open, `F2 -> master`; `gh pr view 1 --json comments` returns `0`.** No
outside-witness comment. Recorded as an unavailable check, not as a pass.

**My own instructions (4b) and the conftest pathspec (4c).**

```
cmd  git diff 900fe88..d384e41 -- .claude docs/SUPERVISOR.md
out  e6baa21 ONLY. Standalone `process:` commit citing CJ0 and R315, touching
     those two files and nothing else. I read both hunks line by line.
judge THE ROUTE IS CORRECT AND SO IS THE CONTENT THIS TIME. The sentence I
     objected to last round -- "Review is the LAST bound rather than the whole
     of it" -- is gone from both files and "Review is the bound" is back, with
     the withdrawn claim named as withdrawn. The only addition beyond the
     withdrawal is "or any plugin the rung loads" in item 4c, which widens what
     I must read. Nothing was removed. R315 is closed HERE.
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 900fe88..d384e41 -- tests/conftest.py 'tests/**/conftest.py'
out  (empty -- no conftest changed this round)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py                      -- and it is still the whole set
```

## Carried

Verdict 36 listed three blocking items and five at 4a. **Two of the three close.
One closes at three of the four sites it named. All five 4a items are answered or
correctly declared. The round also moved the step's own content for the first time
in eleven rounds, and that is where this verdict's findings are.**

- **R315 -- CLOSED AT THREE OF FOUR NAMED SITES, AND THE FOURTH IS STILL THERE.**
  The condition named both instruction files, `scripts/run_rung.sh`,
  `scripts/rung_no_xpass.py` and the report. `docs/SUPERVISOR.md`,
  `.claude/agents/gating-supervisor.md` and `scripts/rung_no_xpass.py:91-100` all
  say what was measured now, and the plan states a boundary instead of a mechanism.
  `scripts/run_rung.sh:186` does not. Carried as **R327**.

```
judge THE BOUNDARY IS AN ANSWER, NOT AN EVASION, and I tried to read it as one.
     An evasion would declare the property out of scope and keep the
     mechanism's claim; this does the opposite -- it withdraws the claim in
     four files, keeps the cross-check with its reach stated at two of six
     measured channels, names the keyword argument that walks past it, and puts
     the defence where the defence actually is. `docs/milestones/F2.md:1223-1259`
     states it as a threat model, with the six channels in a cell rather than in
     a sentence. That is the shape I would have asked for.
cmd  python -m pytest tests/test_ci_ladder_gating.py -q         (my run)
out  64 passed -- all four of my layouts built, the DEFAULT_ORDER control
     caught, the three that walk past declared `pass` with the reason
judge AND THE DECLARATION IS TWO-SIDED. `REQUIREMENT_CHANGED[state][0] ==
     "pass"` asserts `code == 0`, so the day one of those channels starts being
     caught the file goes red and the declaration is revisited. A one-sided
     "out of scope" would have been an evasion; this is not one.
```

- **R316 -- CLOSED, and I re-measured the replacement rather than reading it.** The
  count leaves `floatfea/tolerances.py:1073-1080` and `docs/milestones/F2.md:1166-1175`,
  both of which now name the two historical mistakes as mistakes and point at the
  report; §2 carries the count with the stamp rows disclosed.

```
cmd  regen_figures.render() against docs/milestones/F2_figures.md, rows parsed
     with the generator's own `_ROW` pattern                  (my run, d384e41)
out  committed 44   local 44   shared 44   only-committed 0   only-local 0
     differ including the 5 stamp rows: 13
     differ excluding them:              8
     stamp_numpy, stamp_openblas_coretype, stamp_platform, stamp_python,
     stamp_scipy + clean_worst_ratio, counter_defect_boundary,
     counter_defect_over_edge, counter_headroom_room, detection_edge,
     rigid_body_counter_loss, rigid_body_mode_ratio, rigid_body_subspace_loss
judge 44 / 13 / 8, DIGIT FOR DIGIT WHAT §2 PUBLISHES. Third attempt, right.
cmd  grep -rn "thirty-eight\|forty-seven" docs/milestones/F2.md floatfea/tolerances.py
out  two hits, both inside the sentence that says both numbers were wrong
```

- **R317 -- CLOSED on all four, each re-run by me at this commit.**

```
cmd  python -m pytest tests/test_report_guard_states.py -q     (my run)
out  26 passed in 73.54s                      -- (a), matches §3
cmd  python -m pytest tests/test_report_carried.py -q -k WHOLE_SUITE
out  2 passed, 323 deselected                 -- (b), matches §3
cmd  the two renders, rows in common          -- (c), 44, above
cmd  §7's heading
out  "The whole suite, at the commit this revision is committed on top of"
judge (d) CORRECTED -- AND THE CORRECTION IS WHAT EXPOSED R323. The heading now
     states plainly what the line means, and what it means is false.
cmd  python scripts/ci_section.py bf00121                      (my run)
out  identical to §0, line for line, including "20 jobs, 1 not green"
```

- **R318 -- CLOSED.** `tests/test_report_carried.py:777-787` refuses a pointer at
  the Carried section, and
  `guard_state_every_Carried_pointer_names_the_Carried_SECTION_ITSELF` builds the
  state I made by hand last round; the file reddens through a named reporter.
  Revision 11's Carried section is §9 and no row points at it.

- **R319 -- CLOSED as specified, and the specification is now the finding.**
  `tests/test_report_carried.py:1018-1034` requires `rev-list --count sha..HEAD <= 1`.
  It does what I asked. What I asked for cannot distinguish "the count at that sha"
  from "the count at a tree that sha does not contain", and R323 is that gap made
  live.

- **R320 -- CLOSED.** The window is gone; `_inside_an_exempt_span()` requires the
  token to sit inside the exempt match, and I read both call sites. A new
  whole-line exemption arrived beside it -- R330, 4a.

- **R321, R322 -- OPEN, correctly declared "recorded, not done" at §5 and §8**, with
  reasons. Both remain at 4a.

- **R231, R244, R245, R275 -- OPEN.** I said last round these were due. One adjacent
  Q8 class landed instead and these four did not; I am not making that a gate,
  because the class that landed is the one that unblocked ladder 4 and ladder 5.
  **My corpus went into `g22_model_configurations.txt` and
  `g21_rigid_body_frames.txt` this round as I said it would**, and what it moved is
  at the foot of this verdict.

- **R223, R224, R230, R261 -- OPEN by instruction, correctly listed.**

- **R300, R291, R292 -- OPEN, recordable at 4a, correctly recorded.**

- **R281 -- OPEN, and my own count of it was wrong.** See R332: seven corpus files
  have no runner, not three.

- **R302 -- answered by the boundary rather than by the mechanism claimed for it**,
  which §1 says in as many words. Accepted.

- **R293, R303-R308 -- closed in verdict 35**, correctly carried and not reopened.

- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues, R249-R252,
  R225-R228, R232, R233, R288, R289, R290 -- carried, and correctly present in the
  generated table.**

## Findings

**R323. (BLOCKS -- the truth of the round's headline figure, twice) Two provenance
claims each name a commit that is not the one measured. Each is one command.**
`docs/reports/F2/step-5.md:3502` and `:3356`; `scripts/suite_count.py:69`.

```
(a) code S7 "**Whole suite at `265b32f`: 2067 passed, 0 failed, 0 skipped.**"
    cmd  clone to a scratch dir, checkout 265b32f, pytest --collect-only -q
    out  1907 tests collected
    cmd  the same clone at d384e41
    out  2067 tests collected
    cmd  the same clone at 265b32f with d384e41's step-5.md and
         step-5-answers.json copied in, nothing else changed
    out  2067 tests collected
    judge THE NUMBER IS RIGHT AND THE SHA IS WRONG. 2067 is the suite of the
        tree that CONTAINS revision 11 -- the tree of `d384e41` -- and revision
        11's own §8 site table is most of those 160 cases. At the commit the
        sentence names, the suite is 1907 tests and 160 of the ones counted do
        not exist. My own clean run at `d384e41` is 2067 passed, 0 failed, 0
        skipped, so nothing is wrong with the measurement.
    judge AND THE GENERATOR PRINTS THE CONTRADICTION. `suite_count.py`'s
        docstring says "the count is a measurement of the tree the report is
        committed from"; `main()` prints "at <_sha()>" where `_sha()` is
        `rev-parse HEAD`, which at the moment it runs is the PARENT of that
        tree. The script states the right thing and prints the wrong one.
(b) code S0a "§4 is where they stop being red, and the run that shows it is at
        this round's own head"
    cmd  gh api repos/xabi80/FloatFEA/actions/runs/34546580003 --jq .head_sha
    out  8942cdc32f9380a18719dbefba483ae33a69a51d
    judge THAT IS THE FIFTH OF EIGHT COMMITS, three before the head, and two
        commits touching `tests/` landed after it. The ladder claim survives --
        `git diff 8942cdc..d384e41 -- tests/verification scripts .github` is
        empty, and I ran that -- but a reader is told the head has CI evidence
        and it has none, which matters more than usual in the round where CI
        became unavailable.
```

**Closed when** §7's line says which tree it measured -- the honest form is the
parent sha plus "and this file", or no sha and the tree described in words -- and
`suite_count.py` prints that form rather than "at HEAD"; and §0a names `8942cdc`.
If the count AT the named sha is what is wanted instead then it is `1907`, and the
line would have to be taken before the report is written, which is the opposite of
"run it last".

**R324. (BLOCKS -- a counter and how it is injected) The counter's margin against
the band is exactly the drift the band exists to admit, so the counter test can go
red on the machine the band was measured on.**
`tests/verification/rung4/test_writer_round_trip.py:168-190`.

```
code got[0, 0] += INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER * math.ulp(ampl)
     assert drift > INTERCHANGE_CHANNEL_DRIFT_ULP
     with COUNTER = 3.0 and the band = 2.0
cell the shipped `_drift_ulp` and the shipped fixture, three states of the
     element the injection lands on                        (my run, d384e41)
out  position     base drift 0.0000  injected 3.0000  PASSES
     acceleration base drift 0.0000  injected 3.0000  PASSES
     position, on a machine where got[0,0] - want[0,0] = -1 ULP of the
     amplitude:  injected 2.0000   assert 2.0 > 2.0  ->  FAILS
     acceleration, same state:
                 injected 2.0000   assert 2.0 > 2.0  ->  FAILS
cmd  the canonical measurement this band was set from (run 34545832426, leg 4)
out  kinematics/bodyA/acceleration  1.0000 ULP, 73/75 exact
     kinematics/bodyB/*             1.0000 ULP
judge THE STATE IS NOT HYPOTHETICAL. The canonical machine already puts a full
     -1 or +1 ULP at two of the seventy-five values of that channel, and which
     two is a property of a libm. The counter is "one ULP past the band" and
     the noise the band admits is one ULP, so the margin is ZERO in the worst
     case and the outcome is decided by which way the last bit fell. Invert the
     rule and solve: this counter is safe only while element [0,0] happens to
     be one of the exact ones.
judge AND IT IS NOT MEASURING WHAT THE ENTRY SAYS. Injecting into `got`, which
     already carries the drift, measures `drift(got + delta)` rather than
     `delta`; the smallest defect this assertion detects is 3.0 ULP on this
     machine and 2.0 on another, so "the smallest injection unambiguously
     outside the band" is not what the shipped cell computes.
```

**Closed when** the injection is on a clean array -- as
`test_the_band_is_not_wide_enough_to_hide_a_swapped_sign` already does -- or the
counter is separated from the observed drift so its measured value is the same on
every machine, and the `tolerances.py` entry says which. A counter whose value
depends on the libm under it is not a detection threshold.

**R325. (BLOCKS -- the stated basis of a new tolerance) The basis contradicts
itself inside one locked file, and two of its numbers are refuted by the run they
cite.** `docs/milestones/F2.md:1101-1103` against `:1133` and `:1137-1140`;
`floatfea/tolerances.py:1022-1031`;
`tests/verification/rung4/test_writer_round_trip.py:124-127`; report §4.

```
(a) code F2.md:1101 "The basis for `2` is the thirteen CI-versus-local pairs
        ALREADY MEASURED, every one of which is 0.5 or 1.0 ULP of its
        channel's amplitude."
    code F2.md:1138 "the band Q8 fixed for this class BEFORE ANY OF IT WAS
        MEASURED is two. The measurement did not set the number."
    code tolerances.py:1029 "it is the number Q8 already fixed for this class
        before any of it was measured"
    cmd  git log -S'ULP of the channel' -- docs/milestones/F2.md
    out  5697b2a, 2026-09-09, and the "already measured" sentence entered in
         THAT SAME COMMIT
    judge ONE OF THE TWO IS FALSE AND THEY ARE FORTY LINES APART. Either the
        band came from those thirteen pairs -- in which case it is a number
        derived from the failures it now admits, which is legitimate at twice
        the worst but has to be said that way -- or it did not, in which case
        the sentence that has stood since 5697b2a is wrong. The round's whole
        claim not to be fitting a tolerance to a red test rests on which.
(b) code tolerances.py:1029 "The same `1.0` is reported by every determinism
        leg, across SIX CPU models."; the test docstring repeats it
    cmd  gh run view 34545832426 --log | grep -E "EPYC|Xeon" | sort -u
    out  AMD EPYC 7763 64-Core Processor
         AMD EPYC 9V74 80-Core Processor
         Intel(R) Xeon(R) 6973P-C
    judge THREE, over ten legs. "Every determinism leg" is true: all ten
        printed 1.0000 and I read all ten.
(c) code F2.md:1133 "the same, on legs 4, 7 and 10 of the same run, three CPU
        models"
    out  leg 4 EPYC 7763, leg 7 EPYC 9V74, leg 10 EPYC 9V74 -- TWO models. A
        three-model set exists; it is one of {1,4,8} + one of {3,5,7,9,10} +
        one of {2,6}.
```

**Closed when** the plan and the tolerance entry tell one story about where `2` came
from, and the CPU-model counts are the ones the run prints. The measurement itself is
sound and I reproduced it from the CI log leg by leg; what is wrong is every sentence
about its provenance.

**R326. (BLOCKS -- an undeclared threshold in a comparison, and the one condition
under which the repository said this would stop being a 4a item) `1e12` reaches a
comparison in a shipped test, the scanner cannot see it, and the figure published
beside it is 15.7 orders rather than fourteen.**
`tests/verification/rung4/test_writer_round_trip.py:193-208`;
`tests/test_no_tolerance_literals.py:224-260`;
`tests/test_marker_exemption_corpus.py:51-54`; report section 4 line 3456.

```
code assert drift > 1e12 * INTERCHANGE_CHANNEL_DRIFT_ULP
cmd  offending(Path("tests/verification/rung4/test_writer_round_trip.py"))
out  []                                                    (my run, d384e41)
cmd  the same scanner on `assert d > 1e12` alone
out  [(3, 'comparison against 1000000000000.0')]
judge THE COMPARATOR IS A `BinOp`, and the `Compare` branch reads only
     `Constant` and a negated `Constant`. CLAUDE.md sec. Tolerances is
     explicit -- "no exceptions, no local literals" -- and this is the only
     such literal in `tests/`: a grep for a big literal times a name over
     `tests/` returns this one line.
judge AND THIS IS THE ESCALATION THE REPOSITORY ITSELF WROTE DOWN.
     `tests/test_marker_exemption_corpus.py:51-54` bounds the known misses --
     `detect_literal_times_scale` among them -- with "they go to 4a by name
     unless one exposes a false pass on a real file in the tree. None does --
     the scanner is clean over every file in tests/, measured, not assumed."
     At this commit one does. The bound's own condition has fired, so this is
     not a 4a item this round.
cell the control's own headroom, solved rather than sampled
out  a sign flip on `xi[:, 3:6]` measures 1.0628e+16 ULP of the amplitude
     against the band (2.0):               15.73 orders
     against the shipped threshold (2e12):  3.73 orders, a factor of 5313
     the assertion is satisfied for any band below 1.06e+04 ULP
judge SO "FOURTEEN ORDERS" IS IN NO READING I CAN CONSTRUCT, and what the
     control certifies is "the band is under ten thousand ULP" while the
     sentence beside it says it certifies fourteen orders. It also never reads
     the fixture -- `got` is built from `want` -- so it cannot fail for any
     defect in the repository, only for a band change. That is a legitimate
     scale statement and it should say so.
cmd  tests/corpus/tolerance_marker_exemptions.txt, the 9 entries added this round
```

**Closed when** the `1e12` is a declared constant in `floatfea/tolerances.py` with
its own basis, or the assertion is rewritten against a quantity that is not a
threshold; the published figure is the one the run prints; and the docstring says
what the control does and does not read. The scanner's reach is 4a and stays there.

**R327. (BLOCKS -- R315 is closed at three of the four sites its condition named)
`scripts/run_rung.sh:186` still carries the withdrawn sentence, and the channel list
eighteen lines above it still enumerates four.** `scripts/run_rung.sh:157-166` and
`:186-187`.

```
cmd  grep -rn "LAST bound" over the tree
out  ./scripts/run_rung.sh:186  "WHAT PROTECTS A RUNG IS THEN REVIEW OF ITS
     CONFTEST -- the LAST bound, not the whole of the answer."
judge THAT IS THE EXACT PHRASE THE CONDITION ASKED TO BE CORRECTED, in one of
     the four files it named, twenty lines below a new paragraph that withdraws
     the claim it rested on. The file now says both things.
code run_rung.sh:157-160 "the reviewer measured FOUR channels and three were
     unlisted", followed by a four-row list
judge SIX ARE MEASURED AND THE LIST NAMES FOUR. The new paragraph says six in
     prose; the enumeration a reader will actually use omits
     `pytest_runtest_call` with `trylast`, `pytest_runtest_protocol` and
     `pytest_deselected`.
judge AND SECTION 8 CANNOT CATCH THIS, which is worth recording on its own:
     the site table works at file granularity, so a finding naming a line in a
     file the diff touches is reported as "the block moved" whether or not that
     line was addressed. Eighteen `rung_no_xpass.py` rows and thirty-odd
     `test_report_carried.py` rows carry that same sentence this round.
```

**Closed when** `run_rung.sh:186` says what the other three files say, and the
enumeration at `:157-166` is the measured six with the two the cross-check catches
marked as such. This one is a script comment, not an instruction file, so it does
not need a `process:` commit.

**R328. (BLOCKS -- BP0: a sentence citing the rule that changed, in the file that
changed it) The module's title and its stated reason for shipping no sidecar both
describe the assertion this commit removed, and the sidecar the generator already
writes was never weighed.** `tests/verification/rung4/test_writer_round_trip.py:1-23`;
`artifacts/make_fixture_flr.py:61-63`.

```
code line 1  "G1.1 -- bit-exact round-trip of a record the WRITER actually
     produced (V2)."
cmd  grep -n "array_equal" tests/verification/rung4/test_writer_round_trip.py
out  153, 221-223 -- `time/t` and the interchangeability control. The twelve
     kinematic pairs and `joints/lam` are a band now.
judge THE TITLE OF THE FILE STATES THE RULE THE COMMIT DELETED. BP0 asks for
     that in the same commit, not the next one.
code lines 20-22 "recomputed here from the same closed forms the generator
     used, RATHER THAN SHIPPED IN A SIDECAR -- so what is asserted is readable"
cmd  sed -n '61,63p' artifacts/make_fixture_flr.py
out  np.savez(OUT.with_suffix(".expected.npz"), t=t, xi=xi, ...)
     print("wrote expected-values sidecar")
cmd  git ls-files tests/fixtures
out  panel_reconstruction.npz   writer_output.flr    -- the sidecar is written
     by the generator and is not committed
judge THE ROUTE THE ROUND DID NOT TAKE EXISTS AND IS ONE `git add`. Fixture
     against a committed sidecar is bit-exact on EVERY machine, because both
     sides are stored data: it keeps G1.1's title true and confines the band to
     the one comparison that genuinely varies, closed form against libm. I am
     not requiring it -- the readability reason is real, and a text sidecar is
     a different argument -- but a round that relaxes an exactness assertion
     has to say why the machine-independent form was rejected, and nothing
     does.
judge WHAT IS NOT LOST, and I checked rather than assuming: the container is
     still asserted exactly, by `time/t` through the same file, 25/25 on the
     canonical machine. I also measured HDF5 float64 round-tripping `xi`
     bit-exactly in a scratch file. The diagnosis in section 4 is correct.
```

**Closed when** the module docstring's first line and its sidecar paragraph describe
what the file now asserts, and the sidecar alternative is recorded with the reason it
was not taken.

**R329. (BLOCKS -- the form of the new tolerance, in its denominator) A channel with
no amplitude defaults to a scale of `1.0` instead of raising.**
`tests/verification/rung4/test_writer_round_trip.py:72`;
`scripts/measure_channel_drift.py:93`.

```
code ampl = float(np.max(np.abs(want))) or 1.0
cell an all-zero `want` against a `got` of 4e-16          (my run, d384e41)
out  _drift_ulp -> (1.8014, 0)  -- 1.8 ULP, INSIDE the band, and zero of the
     nine values agree bit for bit
judge A CHANNEL THAT SHOULD BE IDENTICALLY ZERO AND IS NOT WOULD PASS, at up
     to 4.4e-16 absolute, with the band's denominator silently invented. No
     channel in this fixture is all-zero, so it is latent -- but the recorded
     rule is that an unsupported case raises and never defaults, and `1.0` is
     a scale for a dimensional quantity chosen inside a test file.
     `test_mu_is_present_and_not_all_zero`, in this same module, exists
     precisely because an all-zero channel is the shape a writer that forgot a
     channel produces.
```

**Closed when** an amplitude of zero raises, naming the channel, in both the test
helper and the script.

**R330. (recordable, 4a) R320's repair added a whole-line exemption on a weaker
predicate than the one it replaced.**
`tests/test_report_numbers_are_sourced.py:135-141`. A prose line matching
"python scripts/<name>.py" in backticks is skipped entirely, so **every** number on
it is exempt whether or not that script produced it. Last round `1889` was exempt
because a sha sat ten characters to its left; this round `2067` is exempt because
`suite_count.py` is named later on the same line. The intent is right -- a line
carrying its own command satisfies BF0 -- and the predicate wanted is "this line's
command produced this token", not "this line mentions a script".

**R331. (recordable, 4a) A commit message's count, and an unrecorded CI red inside
the range.** `265b32f`'s subject says "three repairs the new guards needed, found by
running them"; the diff makes four changes, and the fourth is a rewrap of
`tests/test_report_carried.py:781` repairing the `ruff` E501 that made
`lint and type-check` RED at `d2bbcdd` (run `34547887983`). Lint is clean at my run
of `d384e41`. Nothing in the report or in any message records that the range
contained a red CI job, and section 0 by construction only ever describes the
previously reviewed commit.

**R332. (recordable, 4a -- and it corrects my own figure) R281 is seven files, not
three, and the largest is the corpus for this step's own gate.**

```
cmd  every tests/corpus/*.txt name grepped for across tests/ and scripts/
out  UNREAD: carried_item_routing.txt  carried_row_subject.txt
     ci_determinism.txt  g21_rigid_body_frames.txt  pinned_interpreter.txt
     report_ci_section.txt  report_numbers_sourced.txt
cmd  grep -rn "rigid_body_frames" --include=*.py .
out  (nothing)
judge g21_rigid_body_frames.txt IS THE CORPUS FOR G2.1, THE GATE THIS STEP IS
     ABOUT, and nothing in the repository reads it. Twenty-one recorded frames
     -- four unit systems, four spans, four sections, four meshes, eleven of
     them recorded as breaching a shipped ceiling -- and the suite executes
     none of them. They were measured by an instrument that no longer exists,
     which is this item's other half: my own attempt to re-measure failed its
     control, and the corpus note below says so rather than publishing numbers
     as though it had not.
```

## Tolerances touched

**Two new constants, and they arrived by the right route.** `3f0c7e9` is a
standalone plan + `tolerances.py` commit; the test that reads them is `8942cdc`, the
next commit. **No tolerance and no counter is in the same commit as the code it
rescues**, and the report says so and it is true.

| name | value | form | counter | basis located |
|---|---|---|---|---|
| `INTERCHANGE_CHANNEL_DRIFT_ULP` | `2.0` (NEW) | dimensionless, ULP of the channel's own amplitude -- relative to a stated response scale, which is the right form | `3.0`, injected into one value of one channel -- **R324** | F2.md Q8 second class + `scripts/measure_channel_drift.py` on run `34545832426`; **the provenance sentences are R325**, the denominator's fallback is **R329** |
| `INTERCHANGE_CHANNEL_DRIFT_ULP_COUNTER` | `3.0` (NEW) | dimensionless, one ULP past the band | itself | same run; its margin against the noise the band admits is **zero** (R324) |
| `FIGURE_FLOOR_CLASS_SPREAD` | `1.5` (unchanged) | dimensionless, max over min of two renders | `1.6` | comment rewritten for R316; bracket re-measured below |
| `FIGURE_ARGMIN_TIE_WINDOW` | `1.01` (unchanged) | dimensionless factor on an extremum | `1.0216` | unchanged |

```
cmd  the canonical drift measurement, read off the CI log myself rather than
     from the report                      (run 34545832426, legs 2, 4, 9, 10)
out  time/t                             0.0000 ULP   25/25 exact
     joints/lam                         0.5000 ULP   97/100
     kinematics/bodyA/position          0.5000 ULP   72/75
     kinematics/bodyA/rotation          1.0000 ULP   72/75
     kinematics/bodyA/velocity          0.5000 ULP   69/75
     kinematics/bodyA/angular_velocity  0.5000 ULP   74/75
     kinematics/bodyA/acceleration      1.0000 ULP   73/75
     kinematics/bodyA/angular_accel.    1.0000 ULP   74/75
     kinematics/bodyB/*                 1.0000 ULP
     worst channel drift 1.0000 ULP, identical on all ten legs
judge THE BAND IS TWICE THE MEASURED WORST, AND IT IS NOT THE LOOSEST THING
     THAT WOULD HAVE MADE LADDER 4 GREEN. The tightest is 1.0, which is the
     measurement itself and leaves no room for a fourth libm; 2.0 is the same
     factor EXEMPT_RESPONSE_DRIFT_ULP took (tolerances.py:724, "twice that
     maximum -- room for a platform whose last bit rounds differently, and
     nothing wider"); the loosest that would have worked is unbounded. It is
     the second-tightest defensible number and I accept the value.
judge RELAXING BIT-EXACTNESS IS THE RIGHT CALL HERE, AND I TRIED TO ARGUE
     OTHERWISE. Regenerating the fixture on the canonical machine does not fix
     it -- it moves the red from CI to every other machine, because the
     comparison is against `np.sin` re-evaluated at test time and not against
     the file. I verified the reference: `artifacts/make_fixture_flr.py:37-41`
     and `_expected()` are the same five closed forms, term for term. The one
     route that would have kept a machine-independent exactness claim is a
     committed sidecar, and that is R328.
cmd  the floor-class bracket, re-measured at this commit
out  largest measured spread 1.3356 (rigid_body_mode_ratio)
     smallest floor-class margin 2.18 (counter_headroom_room)
     1.336 < 1.5 < 2.18                          UNCHANGED and still bracketed
cmd  git diff 900fe88..d384e41 -- floatfea/tolerances.py, value lines only
out  the two new constants and nothing else -- no existing value moved
```

**What held**, reproduced at my run rather than read: the whole suite, 2067 passed
with no failures and no skips; rung 4 green through the shipped gate script, 88
collected and 0 failed; the canonical drift table, read off the CI log leg by leg;
the 44/13/8 render comparison; `26 passed`, `2 passed`, `64 passed`, and
`ci_section.py bf00121` verbatim; `ruff` and `black` clean; the reference behind
`_expected()`; HDF5 float64 round-tripping bit-exactly; the withdrawal present and
correct in both of my own instruction files, by the right route, removing nothing;
and no conftest changed.

**These did not**: the sha on the whole-suite line and the sha under section 0a
(R323), the counter's margin (R324), the provenance of `2` and two CPU-model counts
(R325), an undeclared `1e12` and the fourteen orders beside it (R326), one of
R315's four sites (R327), the module's own title (R328), and a denominator that
defaults (R329).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** This is the best round this step has
had: the boundary in place of a mechanism is the right answer to R315 and it is
argued from measurement, R316 is finally right at the third attempt, all four parts
of R317 reproduce on my machine, and ladder 4 and ladder 5 are green on the
canonical machine for the first time -- the step's own content moving after eleven
rounds of apparatus. **None of that is undone by what follows, and all of what
follows is small.**

1. **R323 -- the headline figure names the wrong tree, twice.** `2067` is the suite
   of `d384e41`; at `265b32f` it is `1907`. And the run that shows ladder 4 green is
   at `8942cdc`, not at the head.
2. **R324 -- the counter has zero margin.** On a machine where the injected element
   already carries the one ULP the band admits,
   `test_a_drift_PAST_the_band_is_refused` measures exactly `2.0` and asserts
   `2.0 > 2.0`.
3. **R325 -- the tolerance's basis contradicts itself.** `F2.md:1101` and `:1138`
   cannot both be true; "six CPU models" is three; "legs 4, 7 and 10, three CPU
   models" is two.
4. **R326 -- `1e12` reaches a comparison and the scanner cannot see it**, which is
   the exact condition `test_marker_exemption_corpus.py` set for this to stop being
   a 4a item; and the "fourteen orders" beside it is 15.7.
5. **R327 -- R315 at its fourth site.** `run_rung.sh:186` still says "the LAST
   bound".
6. **R328, R329** -- the module's own title, and a denominator that defaults.

**CI is UNAVAILABLE, not red, and that bounds what the next round may claim.** No
further Q8 value should be written from a measurement CI has not reproduced while
CI cannot run; `INTERCHANGE_CHANNEL_DRIFT_ULP` was measured before the block and is
safe. The canonical re-render that R231, R244, R245, R275 and my own corpus all need
is blocked outside the repository, and a round that cannot re-render should say so
in its report rather than leave the staleness looking like a defect.

**Not gates on step 5, into the next report's Carried section:** R330, R331, R332,
the reach of R318 and R319, R321, R322, R300, R291, R292, R281, the underlying gap
in R276, R277, R262, R264, R266, the two R248 residues, R249-R252, R225-R228, R232,
R233, and everything already at 4a.

**Adversarial corpus (BE3): 33 new entries across three files, all unseen by the
implementer; every `measured=` and every `expect=` taken at `d384e41` by running the
shipped check before the requirement beside it was written -- except two, which I
name.**

**The coverage measurement, stated plainly: of my 33 new entries the shipped checks
do what the entry requires on 17, of which 15 are entries whose requirement I wrote
before the run.**

* `tests/corpus/g22_model_configurations.txt` -- **+16 (187 -> 203), 16 correct.**
  Six carried from my previous session (the downward vertical with and without an
  orientation node, a near-vertical at `-1e-17`, roll at `+pi`, at `-pi`, and at
  `-0.0`) and ten new: the orientation node ON the member axis and AT node 1,
  `t = D/2` and `t > D/2`, `D = t`, a zero-length member, a one-micron member, a
  thousand-kilometre member, `I_y/I_z = 1.0` exactly, and a subnormal orientation
  component. **The runner refuses every one it should.** It is the hardest corpus in
  this repository to get past and it earned that. **Two of the ten I first wrote as
  `hold` and re-recorded as `raise` after the run** -- `ck_t_equals_half_D`, refused
  as "the wall must be positive and thinner than the radius", and
  `ck_orient_subnormal_component`, refused as degenerate against global Z. In both
  the code is right and I was wrong; those two are not independent evidence and the
  file says so.
* `tests/corpus/tolerance_marker_exemptions.txt` -- **+9 (66 -> 75), 1 correct, and
  the one is the control.** Eight shapes in which an undeclared literal travels
  attached to a declared tolerance name: `1e12 * NAME` on either side,
  `NAME / 100.0`, `NAME + 1e-09`, `rel=0.99 * NAME`, a tuple subscript,
  `min(1e-09, scale)`, and a negated factor. All eight are exempt. The ninth,
  `assert r < ROUNDOFF_IDENTITY` alone, is correctly exempt and shows the guard is
  still usable.
* `tests/corpus/g21_rigid_body_frames.txt` -- **+8 (21 -> 29), 0 measurable, and
  that is the measurement (R332).** Nothing in the repository reads this file. The
  eight are boundary-locating: `unit=20/32/50` between the file's holding `10` and
  breaching `100`, `stretch=3/5` between its holding `1` and breaching `10`,
  `D=0.3` between holding `0.6` and breaching `0.15`, a mirrored tip, and a tip at
  `x=40`. **They are marked `provisional=yes` because my scratch instrument failed
  its own control**: on `rb_shipped_frame` it gives ratio `2.0906e-14` and loss
  `7.2695e-15` against the `1.6009e-14` and `5.3061e-15` that this file and
  `F2_figures.md` both carry -- 1.31x and 1.37x. I will not publish numbers from an
  instrument that cannot reproduce the row above them, so the file says so, and
  `rb_span_x5`'s breach (1.36x over the ceiling) sits inside that error and is
  flagged as the first row to re-measure.

**WHAT MY CORPUS DOES TO THE SUITE, SAID UP FRONT SO IT IS NOT MISTAKEN FOR A
DEFECT.** At my corpus commit the whole suite is **11 failed, 2105 passed, 0
skipped** (my run), against 2067 passed and nothing failing at `d384e41`. All eleven
are named and all eleven are mine:

```
out  tests/test_plan_figures.py::test_the_generated_figures_are_not_stale
       corpus_entries 187 -> 203, corpus_solved 158 -> 172,
       exempt_total "62 of 632" -> "62 of 680",
       calibration_ulp_histogram 0 ULP x141 -> x149,
       boundary_margin_refused 5 entries -> 11
     tests/regression/test_exempt_pair_responses.py::test_the_recorded_set_is_the_measured_set
       'ck_length_thousand_km|dropped_flip' and '|wrong_dof_index' are exempt
       and detected and not in the golden -- the thousand-kilometre member
       reaches the exempt-pair classification
     tests/test_marker_exemption_corpus.py -- the 8 new species, each named,
       plus test_the_known_misses_are_exactly_these
judge THE FIRST TWO NEED THE CANONICAL RE-RENDER, WHICH CI CANNOT PRODUCE
     WHILE THE BILLING BLOCK STANDS, AND I AM ADDING THEM ANYWAY. Withholding
     data to keep a number green is the inverse of this repository's rule; the
     route is R231/R244/R245/R275, which were already due; and a red that is
     named, explained and attributable beats a green that is green because
     nobody measured. The nine marker failures need `KNOWN_MISSES` to grow by
     eight and `1e12` to leave `tests/` (R326).
```

**Thirty-seven consecutive rounds have found no element defect, and this round does
not either.** What blocks is a sha, a counter's margin, a self-contradicting
paragraph, one undeclared literal, one sentence in one of four files, a docstring
title, and a denominator that defaults. The element has now been right for twelve
rounds against corpora it did not choose -- and by the rule I am bound by that still
means "not yet contradicted", because V5.1 against CalculiX has not run.
