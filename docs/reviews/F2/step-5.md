# Review — F2 step 5
Reviewed commit: 1f389771f5f2af187b48ac169fa24a25c128906c
Verdict: HOLD

Tests: **1589 passed, 0 failed, 0 skipped** (my run at `5737fa6`, `python -m pytest -q`,
154.66 s, Python 3.13 on Windows). This equals the count the report states. With my
twenty-eighth-round corpus applied at `1f38977`: **9 additional failures**, which is the
coverage measurement and is a change of kind -- last round none of my 38 entries was
executed by anything in the suite; this round all of them are.

**Reviewed code commit: `5737fa6`.** The header stamp is `1f38977`, my own corpus
commit, made immediately before this verdict and touching no code.

**CI at the reviewed commit: RED (CA2).**

```
cmd  gh run list -R xabi80/FloatFEA --commit 5737fa67c892648cff440784bb0f0ba608189ef7
out  two runs (push 34382223222 + PR #1 34382227058), both "failure", both completed
cmd  gh run view -R xabi80/FloatFEA 34382223222 --json jobs
out  success  lint and type-check     success  ladder 2 (empty by design)
     success  unit tests              success  ladder 3
     success  ladder 1                FAILURE  ladder 4 -- 13 failed, 72 passed
                                      skipped  ladder 5, ladder 6
cmd  gh run view ... --log-failed | grep FAILED
out  the same 13, the same magnitudes: 1.110e-16 .. 4.441e-16 on the twelve
     kinematic channels, 3.469e-18 on rotation, plus joints/lam. Python 3.11.16.
     NOT ONE NUMBER MOVED from the twenty-seventh verdict table.
```

Third verdict on step 5. Range `8ffbd51..5737fa6`, two commits. **The two guards CB0 and
CB1 asked for are real work and I rule for both of them on their merits.** What holds the
step is one carried item that has not moved, one whose closing condition cannot yet be
met, and three sentences this diff publishes that measurement refutes -- one of which
stops `pytest` from collecting anything at the next step boundary.

## Carried

Step 5 is HOLD at `8ffbd51` (verdict 27). **Five items were listed under "Next step opens
when". Two close, one is answered in mechanism but not in its stated condition, and two
are untouched by declaration.**

- **R229 -- CLOSED, and I verified all three properties myself rather than reading
  them.** `tests/test_no_tolerance_literals.py:57-76` (tokenised markers), `:134-147`
  (header span), `:189-207` (one marker, one node).

```
cell  the three properties, each as the shape that must redden, through the
      SHIPPED offending() at 5737fa6 (marker = `# not-a-tolerance: ...`):
        assert residual < 1e-9, "not-a-tolerance: for context"
                                     -> [(8, 'comparison against 1e-09')] CAUGHT
                                        old line-keyed rule: exempt
        assert residual < 1e-9, f"not-a-tolerance: {residual}"
                                     -> CAUGHT.   old line-keyed rule: exempt
        a docstring carrying the marker, above the assert
                                     -> CAUGHT
        match kind:  # not-a-tolerance: ...
            case "a": assert residual < 1e-9
            case _:   assert other < 0.05
                                     -> BOTH caught, [(10,...), (12,...)]
        assert x < 0.05 and y < 0.05  # not-a-tolerance: only x
                                     -> CAUGHT.   old line-keyed rule: exempt
      (i), (ii) and (iii) all hold. On every shape I tried the new window is
      STRICTLY STRICTER than the line-keyed rule except where black had moved a
      marker off its node, which is the case it was written for.
cell  the corpus, measured through the shipped function, not read from the report:
        28 entries, 24 expect=caught / 4 expect=exempt
        misses 4 -- 19 at 3577930. All four are expect=caught.
        all four expect=exempt entries return []   (the hatch stays usable)
        measured miss set == KNOWN_MISSES: True
        the whole tests/ tree scans clean -- no false positive anywhere
cell  AND THE STATED REASON FOR STOPPING AT FOUR IS A CAUSAL CLAIM (BG0), so I ran
      its ablation rather than accept it. test_marker_exemption_corpus.py:61-67
      says the tightening that would close them is what CA0 abandoned. One
      variable moved -- exemption keyed to the FLAGGED NODE own lineno..end_lineno
      instead of the statement span, everything else held:
        corpus misses     4 -> 5, and two of the new ones are expect=exempt
                          entries that the variant falsely reddens
        false positives   0 -> 14 sites across 8 real test files, none of which
                          the shipped rule flags: test_cantilever_closed_form,
                          test_transform_invariance, test_corpus_configurations,
                          test_patch_test, test_basis_constants (5 sites),
                          test_conventions_are_generated, test_live_dof,
                          test_reference_provenance
judge THE CELL REPRODUCES AND THE TRADE-OFF IS REAL. It closes one of the four and
      opens two, at a cost of fourteen false positives. That sentence is now
      measured rather than argued, and I record it as VERIFIED -- which is not
      something the last three rounds have been able to say about a "because".
judge KNOWN_MISSES IS NOT xfail WEARING A REASON, and I checked the domain rather
      than the wording. `_misses()` runs ALL 28 entries including the four;
      `test_the_known_misses_are_exactly_these` asserts set equality in BOTH
      directions; the parametrised test excludes exactly those four. A miss that
      gets fixed and a miss that appears are both build failures. The collection
      the assertion inspects can contain the failure.
```

- **R230 -- MECHANISM VERIFIED, CLOSING CONDITION NOT MET. Carried, not closed, and it
  closes when R231 does.** `scripts/run_rung.sh`, `.github/workflows/ci.yml:83-147`.

```
cell  the shipped script at the REAL repository layout, run by me:
      cmd  sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
      out  run_rung: tests/verification/rung6 -- empty by design, nothing to run
           4 passed in 2.62s        EXIT=0
judge THE R230 DEFECT IS GONE. `tests/regression` executes; at 3577930 it could
      not. `ls A B` is replaced by a declaration per directory, and a rung that is
      renamed, emptied, or renamed off the test_ prefix now contradicts its
      declaration instead of matching no glob.
judge BUT THE CONDITION I WROTE WAS "shown by a CI log line carrying a non-zero
      pass count from that path, NOT by reading the YAML". Ladder 6 is `skipped`
      at 5737fa6 because ladder 4 is red. I am not going to quietly relax my own
      condition to a local run -- that is the sentence CA2 exists to refuse. The
      item is answered in substance and unmet in its stated form, and it becomes
      satisfiable the moment R231 does.
```

- **R231 -- STILL OPEN, BLOCKING, AND LEAVING IT UNTOUCHED WAS RIGHT. Both halves of
  that, said separately.** `tests/verification/rung4/test_writer_round_trip.py:92-103`.

```
judge THE RULING ASKED FOR: leaving it open was correct, and I would have found
      against the alternative. Both available fixes change what a gate F1 CLOSED
      asserts, and CLAUDE.md routes that through the plan, not through a step
      commit. Touching it inside step 5 would have been the finding. The report
      site table declares all twelve lines :92--:103 as "no change, and
      deliberately", which is the site-by-site form a naming condition needs.
judge AND IT IS STILL A HOLD, which is not a contradiction. CA2 says a red CI is a
      HOLD regardless of the local run, and I wrote that into my own reading order
      two commits before this range. "1589 passed locally" is exactly the defence
      CA2 refuses. Correct conduct and an open gate are different facts.
judge WHY NOT STOP. Rungs 1, 2 and 3 are green on CI, so step 5 own rung is
      interpretable. No product code is implicated: `git diff 8ffbd51..HEAD --
      floatfea` is EMPTY across this whole range.
```

- **R232 -- CLOSED on substance.** The revision covers all five commits
  (`docs/reports/F2/step-5.md:184-185`).

```
cmd   grep -rn CA0/CA1/CB0/CB1/CB2 over docs/, excluding docs/reviews/
out   4 hits, all in docs/reports/F2/step-5.md: CB0/CB1 at :185, CA0 at :229,
      CB1 at :268, CB0-CB2 at :423. CA0 and CA1 are NAMED, but what they ASKED
      FOR is still only in their commit bodies.
judge The defect was three commits with no report. That is fixed. The residue --
      a reader in docs/ cannot recover the text of CA0 and CA1 -- rolls into 4a
      with R220 list, and I am not holding the step on it.
```

- **R233 -- STILL OPEN, 4a. Its condition had two halves and one is met.**

```
cmd   python -m ruff check floatfea tests --statistics, at e5f6deb~1   (mine)
out   43 E501, 8 E702, 8 SIM300, 7 I001, 6 NPY002, 4 SIM117, 4 UP037, 3 F401,
      2 B905, 2 E741, 2 F821, 1 B007, 1 F841, 1 SIM102, 1 UP035
      -- Found 93 errors.
judge REPRODUCES CHARACTER FOR CHARACTER against report section 3. The
      enumeration is produced, not typed. That half CLOSES.
cmd   grep -n NPY002 tests/verification/rung3/test_determinism_pins.py, at HEAD
out   46 53 55 69 70 71 72 -- SEVEN lines. Report section 3 out field says
      ":53 :55 :69 :70 :71 :72". Line 46 is the docstring sentence, not a
      suppression.
judge The six SUPPRESSION sites are right. The out field is a filtered result
      presented as what the command prints -- the species R233 named, in the
      paragraph answering R233. Recorded as R239, still 4a, not blocking.
```

- **R223 -- STILL OPEN, BLOCKING, untouched and declared.** The five sites re-located at
  `8ffbd51` are unmoved: `floatfea/tolerances.py:293`,
  `tests/verification/rung1/test_rigid_body_modes.py:19` and `:175-177`,
  `docs/milestones/F2.md:51` and `:1477`; `F2.md:1491-1492` still carries no operating
  point. `git diff 8ffbd51..HEAD -- floatfea/tolerances.py` is EMPTY.
- **R224 -- STILL OPEN, BLOCKING, untouched and declared.** `floatfea/tolerances.py`
  `:295-297` and `:300-308`, both sites, unchanged.
- **R225, R226, R227, R228 -- OPEN at 4a**, untouched.
- **Everything at 4a from step 4** -- R216--R222, R200--R215, R198, R199, R181, R189,
  R190, the R170/R171 remainder, R172, R159, R162, R151, R152, R134--R139, R148, R129,
  R131, R132, R113, R95, R97, R98, R100--R103, R124, R63, R76, R79, R80, R6, R16, R25,
  R30--R33, R36, R50, R52, R62 -- **unchanged and untouched.** R65 remains withdrawn by
  me and recorded as a disagreement. R68 standard met.
- **Item 1b -- SATISFIED.** The report newest revision header is
  `Answers: verdict 27 @ 8ffbd51`, and `8ffbd51` is the latest verdict. One comparison,
  and it passes.
- **The witness -- STILL NO COMMENT.** PR #1 open, `refs/pull/1/head = 5737fa6`, no
  `[witness F2 step 5]` comment. **Twenty-eighth consecutive review by one reader.**
  An unavailable check, not a pass.

## Findings

**Four block. Two are recorded at 4a.**

**R234. (BLOCKS -- head 3, and it is the only finding here that stops the suite from
running at all) The carry guard now reads a pair of files that `CLAUDE.md` guarantees
will not both exist at every step boundary, and at that commit `python -m pytest -q`
collects NOTHING.** `tests/test_report_carried.py:62-84` and `:149-151`, and the
sentence at `docs/reports/F2/step-5.md:314-316`.

```
code  :62-81  STEP = max step number with a report under docs/reports/F2/
      :82-84  VERDICT = docs/reviews/F2/step-<STEP>.md; REPORT = same for reports
      :149    REPORT_TEXT  = _read(REPORT)            <- MODULE SCOPE
      :151    VERDICT_TEXT = _verdict_text_at(...) -> _read(VERDICT) on fallback
judge THE DIAGNOSIS IS RIGHT AND I VERIFIED THE FIGURE IT RESTS ON. The guard did
      name step-4.md in two places while step 5 was open.
      cmd  worktree at 76c186a, tests/test_report_carried.py replaced by HEAD one
      out  80 failed, 13 passed in 0.59s
      EXACTLY the report number, reproduced independently. Every one of the 80 is
      a step-5 finding the report did not carry. That is not what blocks.
judge WHAT BLOCKS IS THE STATE THE FIX CANNOT SURVIVE. CLAUDE.md, Step gating,
      step 1: "Write docs/reports/F<n>/step-<k>.md ... Commit." Step 2: "Invoke
      the gating-supervisor subagent ... Commit the verdict SEPARATELY." So there
      is a commit, at EVERY boundary, where the newest report has no verdict.
cell  one variable moved -- the presence of docs/reports/F2/step-6.md -- in a
      worktree at 5737fa6, nothing else changed:
        WITHOUT it   pytest tests/test_report_carried.py -q
                     -> 93 passed in 0.13s
        WITH it      -> E FileNotFoundError: ...docs\reviews\F2\step-6.md
                        ERROR collecting tests/test_report_carried.py
                        Interrupted: 1 error during collection
        WITH it      python -m pytest -q            (the WHOLE suite)
                     -> 2 warnings, 1 error in 0.84s
                        ZERO of 1589 tests execute.
judge NOT "one test goes red". The module raises at IMPORT, pytest interrupts
      collection, and the run reports nothing. The step report that must state
      "the test counts from your own run" at that commit has no counts to state.
judge AND THE PUBLISHED SENTENCE IS REFUTED. step-5.md:314-316 says "It follows
      the newest report now, and `test_the_guard_reads_the_step_being_worked_on`
      fails if the verdict beside it is missing."
        cmd  pytest that node id, in exactly that state
        out  ERROR collecting ... FileNotFoundError. 1 error in 0.13s.
      It does not fail. It is never collected. The meta-test written for this
      state is dominated by a module-scope read of the same file, so the one
      assertion that would name the problem cannot fire in the only state it was
      written for -- "a gate carries its own failure", inverted.
judge THIS IS ITEM 1b, ONE LEVEL DOWN, AND THE REPOSITORY ALREADY PAID FOR IT. My
      own instructions record that comparing against the newest verdict made the
      boundary permanently red, pytest was `34 failed` BY CONSTRUCTION, and "green
      stopped meaning anything exactly where it is needed". The `Answers:` header
      fixed that for the verdict CONTENT. CB2 has reintroduced it for the verdict
      FILE, and the new failure is worse: 34 failed still tells you 1555 passed.
cell  AND R235 COMPOUNDS IT: this module is one of the 293 tests no CI job
      collects, so CI would stay green through the whole event.
```

**Closed when** the guard inputs are the states that actually occur, shown as
measurements and not as a comment: (i) at a commit whose newest report has no verdict
beside it, `python -m pytest -q` COLLECTS and reports a count, and a NAMED test carries
the message; (ii) the same when `docs/reports/F2/` cannot be read; (iii)
`test_the_guard_reads_the_step_being_worked_on` is shown firing in state (i) rather than
asserted to. The six states are on disk at `tests/corpus/report_guard_states.txt`, each
with what `pytest` did at `5737fa6`.

**R235. (BLOCKS -- head 3) "in the suite, so in CI" is false. No CI job collects any
top-level `tests/*.py`, so 293 of 1589 tests -- every process guard in this repository,
including both guards this step added -- have never run on CI and cannot.**
`docs/reports/F2/step-5.md:243`, and `.github/workflows/ci.yml:71-74`.

```
code  report section 2, :243  "12 passed -- all ten of the reviewer layouts, in
      the suite, so in CI"
code  ci.yml:72-74   "`tests/test_ci_ladder_gating.py` runs it against all ten
      layouts in this suite -- WHICH MEANS IN CI."
cmd   grep -rn "pytest|run_rung" .github/workflows/          (the complete list)
out   :43   pytest tests/unit -q
      :92   run_rung.sh full:tests/verification/rung1
      :103  run_rung.sh empty:tests/verification/rung2
      :114  run_rung.sh full:tests/verification/rung3
      :125  run_rung.sh full:tests/verification/rung4
      :136  run_rung.sh empty:tests/verification/rung5
      :147  run_rung.sh empty:tests/verification/rung6 full:tests/regression
      -- and `ls .github/workflows/` is ci.yml alone. No job names tests/ itself.
cmd   pytest --collect-only -q over exactly those eight paths
out   1296 tests collected
cmd   pytest --collect-only -q                        (the whole suite)
out   1589 tests collected
cmd   pytest --collect-only -q tests/test_*.py
out   293 tests collected                     1296 + 293 = 1589, exactly.
judge THE SENTENCE IS REFUTED BY MEASUREMENT and it is load-bearing, not
      decorative. R230 whole content was that a claim about what CI catches had a
      corpus of zero. The answer builds the corpus, runs it, and publishes that it
      runs in CI -- and it does not. test_ci_ladder_gating, test_marker_exemption_
      corpus, test_no_tolerance_literals, test_report_carried,
      test_counters_are_injected, test_plan_figures, test_plan_matches_tolerances:
      not one is reachable from any job. The tolerance-literal scanner -- the
      guard that enforces the central rule of CLAUDE.md -- has never executed on a
      machine neither the implementer nor I controls.
judge AND IT IS THE SAME SPECIES AS R234, WHICH IS WHY I AM NOT SPLITTING THEM
      APART: the machine that would have caught a suite that collects nothing is
      the machine that does not run the file that stops it collecting.
```

**Closed when** either every top-level `tests/*.py` is executed by a named CI job --
shown by a CI log line with a pass count covering them, not by reading the YAML -- or
both sentences are withdrawn and replaced by what is true, in the same commit (BP0). A
count is the honest form: say how many of the 1589 CI runs.

**R236. (BLOCKS -- head 3 and BP0) `ci.yml:54-55` says adding a test to a rung is not a
CI edit. Under the rule this same commit installs, adding a test to rung 2, 5 or 6
reddens CI until `ci.yml` is edited -- and the implementer own `REQUIREMENT_CHANGED`
entry says so.** `.github/workflows/ci.yml:54-55`, unchanged in this range.

```
code  ci.yml:54-55  "Each rung is wired now, while empty, so that adding a test to
      a rung is a matter of dropping a file into tests/verification/rungN/ -- NOT
      A CI EDIT."
code  tests/test_ci_ladder_gating.py:53-57  REQUIREMENT_CHANGED for
      ci_rung6_both_populated: "Rung 6 own directory is declared `empty:`, so a
      test appearing in it now FAILS as a stale declaration"
cell  measured, not inferred, in a scratch tree with the shipped script:
        rung6: .empty-by-design + __init__.py + a PASSING test_r6.py,
               tests/regression populated, args exactly as ci.yml gives them
        -> run_rung: FAIL -- ...rung6 is declared empty and collects tests.
           EXIT=1
        rung2: .empty-by-design + a FAILING test  -> EXIT=1, same message
      Dropping a file into rung 2, 5 or 6 reddens the ladder. Recovering needs TWO
      edits outside that directory: `empty:` -> `full:` in ci.yml, and deleting
      the marker.
cmd   git diff 8ffbd51..HEAD -- .github/workflows/ci.yml, grepped for the sentence
out   (no hunk) -- the sentence is untouched while the rule under it moved.
judge THIS IS BP0 EXACTLY: "when a decision rule changes, every figure citing the
      old rule is regenerated or withdrawn IN THE SAME COMMIT. Not the next one,
      and not when someone notices." The commit withdrew the "renamed directory"
      sentence four lines below and left this one, in the same comment block.
judge AND I RULE FOR THE RULE ITSELF, so this is a sentence finding and not a
      design one. Both REQUIREMENT_CHANGED entries are stricter and both are
      right, and they are mine to rule on, so: ci_rung_genuinely_empty --
      ACCEPTED, rung 1 declares itself full and a rung 1 holding only __init__.py
      must redden; my require=pass was written against a rule that could not tell
      an emptied directory from an unwritten one. ci_rung6_both_populated --
      ACCEPTED, a stale declaration should be loud. The cost of accepting them is
      that :54-55 is now false, and the cost is cheap to pay in words.
```

**Closed when** `ci.yml:54-55` states what the declared rule actually requires of
someone adding the first test to an empty rung, or is withdrawn.

**R237. (BLOCKS -- head 3, the sentence only) The scanner own "What is flagged" list says
it flags a comparison against any float threshold other than 0.0 or 1.0. It never
inspects the LEFT operand of a comparison, so `assert 0.05 > ratio` returns clean.**
`tests/test_no_tolerance_literals.py:27-28`, and `:176-187`.

```
code  :176  for comp in node.comparators:     <- ast.Compare.left is never read
code  :27-28 "a comparison against ANY float threshold other than 0.0 or 1.0"
cell  through the shipped offending() at 5737fa6:
        assert 0.05 > ratio                      -> []   CLEAN
        assert 1e-9 > residual > 0.0             -> []   CLEAN
        assert (0.34 < ratio < 0.3536)  # marker -> []   CLEAN
      The old line-keyed rule missed all three too: this is NOT a CB0 regression.
judge THE COLLECTION THE ASSERTION INSPECTS CANNOT CONTAIN THE FAULT -- assertion
      domain blindness, verbatim. And it interacts with the property CB0 was built
      to establish: "one marker exempts at most one node" is satisfied on
      `0.34 < r < 0.3536` by ONE marker and ONE invisible literal, so the bound
      holds by counting a candidate set that is short.
cmd   AST scan of tests/ and floatfea/ for Compare nodes with a float left operand
out   2 live sites: tests/verification/rung3/test_basis_constants.py:192
      (0.34 < r/0.9 < 0.3536) and
      tests/verification/rung4/test_reference_provenance.py:30 (0.3 < f < 0.7).
      BOTH ARE LEGITIMATE fixture-range assertions and both already carry a marker
      for their right operand, so NO undeclared tolerance is hiding in the tree
      today. The cost of closing the reach is two extra markers.
judge I AM SPLITTING THIS DELIBERATELY, per BU0. The REACH -- whether `left` joins
      the candidate set -- is parser reach and is 4a, the example BU0 names. The
      SENTENCE at :27-28 is head 3: it is the guard stated contract and it is
      wrong. Either branch closes it, and I am not choosing for the implementer.
```

**Closed when** `:27-28` describes what the scanner does, or the scanner does what
`:27-28` says. Four shapes are on disk at `tests/corpus/tolerance_marker_exemptions.txt`
with `measured` taken at `5737fa6`.

**R238. (recordable, 4a) Four residues in `scripts/run_rung.sh`, each measured.**

```
cell  layouts I built that the ten do not cover, shipped script, scratch tree:
      (a) rung1 full, its only test is @pytest.mark.skip
            -> EXIT=0, "1 skipped". A rung reports green having executed nothing.
               CLAUDE.md forbids a skip taken to get a green build; the ladder
               cannot presently tell that state from a real pass.
      (b) rung1 declared `full:`, populated, AND carrying a stale
          `.empty-by-design`   -> EXIT=0. The marker is read only in the `empty:`
               branch, so the state left by a forgotten half of the
               `empty:`->`full:` transition is silent.
      (c) an `empty:` rung that collects tests -> EXIT=1, correct, but the run
               still prints "run_rung: <dir> -- empty by design, nothing to run"
               AFTER the FAIL line, because :65-68 fails without `continue`. A log
               reader sees the reassuring sentence on the failing run.
      (d) a rung path containing a space -> EXIT=4. `$RUN_DIRS` at :85 is unquoted
               and word-splits. It fails loudly rather than silently, so it is
               robustness, not a hole.
      Correct on everything else I threw at it: symlinked rung directory (runs),
      missing __init__.py (runs), conftest that raises (EXIT=1), rung path that is
      a file (EXIT=1), declared-empty directory absent (EXIT=1), second `full:`
      directory that collects nothing (EXIT=1).
```

**Closed when** 4a rules on (a) and (b) -- both are declaration-versus-reality states,
which is the distinction CB1 exists to make -- and (c) does not print a success line on a
failed rung. The twelve layouts are at `tests/corpus/ci_ladder_gating.txt`.

**R239. (recordable, 4a) Report section 3 `out` field is a filtered result presented as
what its command prints.** `docs/reports/F2/step-5.md:279-280`. Measured above under
R233. Same species as R226 and R233 and the third recurrence; the substance is right
each time and the `out` field is not what the `cmd` prints.

**Closed when** an `out` field is pasted rather than summarised, or the `cmd` includes
the filter that produces it.

## Tolerances touched

**None. No value, no name, no form, no counter, no justification sentence.**

```
cmd  git diff 8ffbd51..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 8ffbd51..HEAD -- floatfea
out  (empty) -- floatfea/ is UNTOUCHED across this entire range.
cmd  git diff 8ffbd51..HEAD -- tests/regression/
out  (empty) -- no golden file moved.
```

**What DID move is the ENFORCEMENT of the tolerance rule**, and it moved in the right
direction: the `# not-a-tolerance:` window is narrower at `5737fa6` than at `3577930` on
every shape I could construct, and narrower than the pre-CA0 line rule except where
`black` had voided a correctly-placed marker. Fifteen of nineteen admitted violations are
closed. Under the CLAUDE.md extension of the tolerance rule to "anything that functions as
a tolerance under another name", that belongs in this section and it is the one thing in
this range I would have been sorry to lose. R237 is a hole in the same guard DETECTION
and predates CA0.

**My own instructions (item 4b).**

```
cmd  git diff 8ffbd51..HEAD -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format=%h %s 8ffbd51..HEAD, with per-commit file lists
out  76c186a  ci.yml, run_rung.sh, test_ci_ladder_gating.py,
              test_marker_exemption_corpus.py, test_no_tolerance_literals.py,
              three .empty-by-design markers          -- no docs/reviews/
     5737fa6  docs/reports/F2/step-5.md, test_report_carried.py
                                                      -- no docs/reviews/
judge No commit touches both code and docs/reviews/. No commit touches .claude/ or
     docs/SUPERVISOR.md at all, so the STOP-class condition is not in play. CLEAN.
```

**What held**, reproduced at my run: `1589 passed, 0 failed, 0 skipped`, equal to the
report figure; `80 failed, 13 passed` for the CB2 cell, reproduced independently in a
worktree; the `ruff --statistics` table, character for character; `26 passed` and
`12 passed` for the two new modules; the three R229 properties, each as a shape that
reddens; the R229 ablation cell; `4 passed` from `tests/regression` through the shipped
rung-6 arguments; `floatfea/` and `tolerances.py` untouched; `.claude/` untouched; no
verdict committed with code. **These did not**: the carry guard at a step-opening commit
(R234), "so in CI" (R235), `ci.yml:54-55` (R236), the scanner own flagging contract
(R237), four ladder residues (R238), one `out` field (R239) -- and R223, R224 and R231,
which are unchanged and which nobody claimed otherwise.

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Seven items. R234 is first because until it
is fixed the next boundary has no test counts at all, and every item below it is measured
by a suite that would not collect.

1. **R234 -- the carry guard survives the step-opening commit.** At a commit whose newest
   report has no verdict beside it, `python -m pytest -q` COLLECTS and prints a count, and
   a named test carries the message. Shown as a run in that state, not as a comment. The
   six states are in `tests/corpus/report_guard_states.txt`; two of them currently
   interrupt collection and one of the two is the state `CLAUDE.md` Step gating creates at
   every boundary. **Do not close this by deleting
   `test_the_guard_reads_the_step_being_worked_on` -- the diagnosis behind CB2 is correct
   and the guard should keep following the newest step.**
2. **R235 -- the 293.** Either a CI job runs the top-level `tests/*.py` and a log line
   proves it, or both sentences (`step-5.md:243`, `ci.yml:72-74`) are withdrawn in the
   same commit and replaced by the count. This is the machinery that decides whether any
   later verdict means anything: it is the reason R230 existed.
3. **R231 -- CI green through ladder 4**, or the finding routed as a plan change through
   the gate-change route (Q8). Until ladders 5 and 6 run once they are an unavailable
   check, never a pass. **Do not close this by widening `np.array_equal` into a tolerance
   inside a step commit.**
4. **R230 -- `tests/regression` demonstrably executed by ladder 6 on CI**, a log line with
   a pass count from that path. The mechanism is verified and this is now waiting on
   item 3.
5. **R236 -- `ci.yml:54-55`**, true or withdrawn, in one commit with the rule it
   describes.
6. **R237 -- `tests/test_no_tolerance_literals.py:27-28`**, true or withdrawn. The reach
   itself is 4a; the sentence is not.
7. **R223 and R224 -- unchanged from the twenty-seventh verdict**, site by site. R223:
   `floatfea/tolerances.py:293`, `tests/verification/rung1/test_rigid_body_modes.py:19`
   and `:175-177`, `docs/milestones/F2.md:51`, `:1477`, and `:1491-1492` carrying its
   operating point or withdrawn. R224: `floatfea/tolerances.py:295-297` and `:300-308`,
   one branch each.

**Not gates on step 5, into the next report Carried section:** R238, R239, the remaining
half of R233, the R232 residue (CA0 and CA1 have no statement in `docs/` of what they
asked for), R225--R228, and everything already at 4a.

**Adversarial corpus (BE3): 36 new entries committed at `1f38977`, across three files,
one of them new, all unseen by the implementer; every `measured` field taken at `5737fa6`
before the `expect`/`require` field beside it was written.**

**The coverage measurement, stated plainly: of my 36 new entries the shipped checks did
what the entry requires on 27.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **+18 entries (28 -> 46), 14 correct,
  4 misses.** Three of the four are the left-operand species (R237); the fourth is a
  de-duplication collapse -- two identical literal comparators on one `Compare` node
  reduce to one candidate, so one marker exempts both. The exemption window itself
  survived everything else I aimed at it. This is a different region from the
  twenty-seventh round on purpose: CB0 closed 15 of that round 19, so I moved from the
  hatch to the candidate set behind it.
* `tests/corpus/ci_ladder_gating.txt` -- **+12 entries (10 -> 22), 9 correct, 3 misses**
  -- a rung whose every test is skipped, a stale `full:`-side marker, and a path with a
  space. Measured by me through `sh scripts/run_rung.sh` directly; the shipped harness
  cannot yet execute them, because `LAYOUTS` has no entry for a corpus line it has not
  seen -- which is `test_the_corpus_and_the_layouts_agree` doing its job, and it fires.
* `tests/corpus/report_guard_states.txt` -- **NEW, 6 entries, 4 correct, 2 misses.** Both
  misses interrupt collection instead of failing a named test, and one of them is not
  hypothetical: it is the commit the step-gating protocol produces at every boundary.
* **`pytest` is no longer indifferent to this directory.** Last round all 38 entries sat
  on disk and the suite was unchanged at 1578; this round the corpus is wired in and adds
  9 failures. That is CB0 and CB1 delivering the thing BE3 asked for, and I record it as
  the clearest single improvement in this range.

**Twenty-eight consecutive rounds have found no element defect, and this round does not
either.** `git diff 8ffbd51..HEAD -- floatfea` is empty. What is under review now is
entirely the apparatus, and this round it got materially better in two places and
acquired one new way to report nothing at all. The pattern across R234, R235 and R236 is
one thing said three ways: **a guard was strengthened, and the sentence describing where
it runs was not re-measured against the change.** That is BP0, and it is the same finding
the twenty-fifth verdict on step 4 turned on.
