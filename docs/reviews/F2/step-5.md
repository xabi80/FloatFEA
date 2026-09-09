# Review — F2 step 5
Reviewed commit: 964d1a5237eb5cbf6286653a6d05fcf677f04d56
Verdict: HOLD

Tests: 1578 passed, 0 failed, 0 skipped   (my run at `3577930`, `python -m pytest -q`,
139.88 s. With my twenty-seventh-round corpus applied at `964d1a5`: **1578 passed,
0 failed** -- unchanged, which is itself the coverage measurement: not one of my 38
new entries is executed by anything in the suite.)

**Reviewed code commit: `3577930`.** The header stamp is `964d1a5`, my own corpus
commit, made immediately before this verdict and touching no code.

**CI at the reviewed commit: RED** (item 3b / CA2, applied here for the first time).

```
cmd  gh run list -R xabi80/FloatFEA --commit 3577930 --json conclusion
out  two runs (push + PR #1), both "failure", both completed
cmd  gh run view -R xabi80/FloatFEA 34370454242 --json jobs
out  success  lint and type-check          success  ladder 2
     success  unit tests                   success  ladder 3
     success  ladder 1 (1013 passed)       FAILURE  ladder 4 -- 13 failed
                                           skipped  ladder 5, ladder 6
cmd  python -m pytest tests/verification/rung1 -q   (mine, local)
out  1013 passed -- IDENTICAL to CI. Step 5's own rung agrees on a machine
     neither the implementer nor I controls. That is new information and it is
     the first of its kind in this repository.
```

Second verdict on step 5. Range `5ade3a5..3577930`, three commits. **R223 and R224
are open and are not answered in this range; the implementer says so and is
correct.** What I rule on is what landed on top of them.

**The ruling asked for first is in the implementer's favour, narrowly and with a
measured cost.** What holds the step is three things I went looking for: a guard's
escape hatch was widened in the same commit that reddened it and now admits 19 of
my 28 planted violations; the new CI rung guard does not run tests/regression at
all and reports green; and CI is red at the reviewed commit.

## Carried

Step 5 is HOLD at `5ade3a5` (verdict 26). **Two items were blocking and neither is
answered.** The implementer declared both unanswered in advance, which is the
correct declaration and is not the same as answering them.

- **R223 -- STILL OPEN, BLOCKING, and its site citations have DRIFTED.** Untouched
  in substance: the invariance sentence is still at all five sites and my
  twenty-sixth-round measurement stands. **But `e5f6deb` moved three of the five
  line numbers the closing condition names**, and a closing condition that names
  sites is closed site by site, so I re-locate them here rather than leave the
  next report arguing about a stale number.

      cmd  git show caa2ec5:F | sed -n Np   vs   sed -n Np F, for each cited site
      out  tolerances.py:294        OLD "...invariant under all three."
                                    NEW "#"                          -> now :293
           test_rigid_body_modes.py:163  OLD "Dimensionless by construction..."
                                    NEW the docstring close             -> now :175
           test_rigid_body_modes.py:165  OLD "...ratio is invariant under..."
                                    NEW blank                           -> now :177
           test_rigid_body_modes.py:19   unchanged
           docs/milestones/F2.md:51, :1477  unchanged (F2.md untouched this range)

  **R223's five sites at `3577930` are: `floatfea/tolerances.py:293`,
  `tests/verification/rung1/test_rigid_body_modes.py:19` and `:175-177`,
  `docs/milestones/F2.md:51` and `:1477`.** The two published headroom figures at
  `F2.md:1491-1492` are unchanged and still carry no operating point.
- **R224 -- STILL OPEN, BLOCKING, sites re-located.** The two self-refuting
  sentences are untouched and now sit two lines up: `floatfea/tolerances.py`
  **`:295-297`** (the clean ratio 1.601e-14, then "is not retyped here") and
  **`:300-308`** (the sweep table, then "it is not tabulated here (BI3)").

      cmd  grep -n for the four strings in floatfea/tolerances.py
      out  295, 297, 304, 308 -- and :596, the file's own rule, still says a
           generated number is cited by name or it is not written.
      cmd  git diff 5ade3a5..HEAD -- floatfea/tolerances.py
      out  -12 lines, +0. Every one a blank line removed by black. NOT ONE VALUE,
           NAME, FORM, COUNTER OR JUSTIFICATION SENTENCE MOVED.

- **R225, R226, R227, R228 -- OPEN at 4a**, untouched, as the previous verdict
  routed them. R226's species recurs this round as R233.
- **Everything at 4a from step 4** -- R216--R222, R200--R215, R198, R199, R181,
  R189, R190, the R170/R171 remainder, R172, R159, R162, R151, R152, R134--R139,
  R148, R129, R131, R132, R113, R95, R97, R98, R100--R103, R124, R63, R76, R79,
  R80, R6, R16, R25, R30--R33, R36, R50, R52, R62 -- **unchanged and untouched.**
  R65 remains withdrawn by me and recorded as a disagreement. R68 standard met.
- **The witness -- STILL NO COMMENT, and now it is an unavailable check with a
  name.** PR #1 is open, refs/pull/1/head = `3577930`, and there is no
  `[witness F2 step 5]` comment. **This is the twenty-seventh consecutive review
  by the same reader.** `docs/SUPERVISOR.md:35-40` still records the gap
  correctly. Not a pass; an unavailable check -- and the CI machine is the first
  independent reader this project has ever had.

## Findings

**Three block. Two are recorded at 4a.**

**R229. (BLOCKS -- head 2, a tolerance rule's enforcement, and head 3, the truth
of a published sentence) The `# not-a-tolerance:` exemption window was widened in
the same commit that reddened it, and the new window admits 19 of my 28 planted
violations -- every one of which the old window caught.**
`tests/test_no_tolerance_literals.py:107-117`, and the docstring at `:16-18`.

```
code  :107-117  exempt_lines = set(marked); for each ast.stmt, span = header-only
      if it has a `body`, else lineno..end_lineno; if ANY line of the span is
      marked, THE WHOLE SPAN becomes exempt.
code  :121  flag() suppresses a node whose lineno is in exempt_lines.
judge THE DIAGNOSIS IS RIGHT AND I VERIFIED IT. black did void twenty
      correctly-placed markers; keying an exemption to a line number is a guard a
      formatter rewrites. The commit body's cell reproduces. That is not what
      blocks.
judge WHAT BLOCKS IS THE SIZE OF THE REPLACEMENT. A statement can hold MORE THAN
      ONE flaggable node. One marker anywhere in its span now exempts all of them.

cell  28 shapes written by me and passed to the SHIPPED offending() at 3577930 --
      24 that must be caught, 4 legitimate exemptions that must not be:
        shipped rule   9 of 28 correct   -- 19 planted violations EXEMPTED
        the line-keyed rule CA0 replaced, same 28, re-run:
                       every one of those 19 CAUGHT
      All 4 expect=exempt entries pass under both, so the guard stays usable
      either way. Five representative misses, through the shipped function:
        assert ( station > 0.15  # not-a-tolerance: ...
                 and residual < 1e-9 )                      -> [] EXEMPT
        assert_allclose(a, b, rtol=0.5,  # not-a-tolerance: ...
                        atol=1e-12)                         -> [] EXEMPT
        assert_allclose(  # not-a-tolerance: ...
                        a, b, atol=1e-12)                   -> [] EXEMPT
        assert ( residual < 1e-9 ), ( "not-a-tolerance: for context" )
                                                            -> [] EXEMPT
        match kind:  # not-a-tolerance: ...
            case "a": assert residual < 1e-9                -> [] EXEMPT

judge THREE SPECIES, each measured rather than argued:
      (a) MULTIPLE NODES, ONE MARKER -- most of the nineteen. The comment at
          :102-106 identifies exactly this hazard for COMPOUND statements and
          closes it there; the same hazard in a SIMPLE statement is not named.
      (b) ast.Match HAS NO `body` ATTRIBUTE.
            cmd  ast.parse of a two-line match/case; hasattr(node, "body")
            out  False -- so a match takes the WHOLE-STATEMENT branch, and one
                 marker exempts every comparison in every case body. That is
                 precisely the "far larger hole" :102-106 says was deliberately
                 avoided, present in the one compound statement the comment does
                 not name. CI runs Python 3.11; match parses.
      (c) THE MARKER IS MATCHED AGAINST RAW TEXT, so a marker inside an assertion
          MESSAGE STRING exempts the statement. This file's docstring at :10-18
          says the regex it replaced failed because it "cleared a whole LINE if a
          tolerance name appeared anywhere on it -- including inside the f-string
          message", and that walking the AST closes this "by construction ...
          message strings are not on that path". **At this commit message strings
          ARE on the exemption path**, at statement scope, which is where black
          puts them. The sentence at :16-18 is refuted by measurement. That is
          head 3, and it is why this is not 4a.

cell  AND A NARROWER RULE EXISTS -- solved rather than asserted, because "the
      minimal fix was taken" is a causal claim and needs its cell. Three changes
      applied one at a time to a reimplementation, scored on my 28 and on false
      positives across the whole real tests/ tree:
        baseline (union of spans, text markers, any count)  17/28 miss   0 FP
        + markers counted in COMMENT TOKENS only            15/28 miss   0 FP
        + at most one exempted node per marker               4/28 miss   0 FP
      **Zero false positives anywhere in tests/ at every step**, and all four
      legitimate exemptions survive throughout. The shipped window is not the
      narrowest window that fixes the formatter problem, and the difference is
      fifteen admitted violations.
judge THE GUARD THIS SITS ON IS THE ONE THAT KEEPS EVERY TOLERANCE IN
      tolerances.py. CLAUDE.md extends the tolerance rule to "anything that
      functions as a tolerance under another name"; an exemption marker is the
      escape hatch on that rule, and it was enlarged to turn twenty red offences
      green. The default hypothesis for a red guard is not that its exemption is
      too narrow.
```

**Closed when** the exemption cannot exempt a flaggable node that no marker
annotates -- stated as a test that FAILS if it were false, not as a comment.
Concretely: (i) a marker occurring inside a string literal exempts nothing, and
the docstring sentence at `:16-18` is either true or withdrawn; (ii) `ast.Match`
does not take the whole-statement branch; (iii) a statement carrying one marker
and two flaggable nodes reddens. The 28 shapes are on disk at
`tests/corpus/tolerance_marker_exemptions.txt`, each with a `measured` field
recording what the shipped scanner returned at `3577930`; how they are caught, or
whether they are, is the implementer's.

**R230. (BLOCKS -- head 3, and it is the ladder's own gate) `ci.yml`'s rung-6 job
never runs `tests/regression` and reports green, and the comment above it names a
defect class the new guard lets through.** `.github/workflows/ci.yml:63-67` and
`:165-169`.

```
code  :165  if ! ls tests/verification/rung6/test_*.py tests/regression/test_*.py
              >/dev/null 2>&1; then echo "empty rung"; exit 0; fi
code  :63-67 "a rung that HAS test files and collects none of them fails. The
      second is a real defect -- A RENAMED DIRECTORY, a broken import, a
      collection error -- and blanket-accepting exit 5 would hide it."
cmd   ls tests/verification/rung6/  ;  ls tests/regression/
out   rung6: __init__.py ONLY.   regression: test_exempt_pair_responses.py
cell  ten layouts built in a scratch tree, the step body copied from ci.yml
      unchanged, bash + pytest:
        rung6 EMPTY + regression POPULATED  (THE REPO AT 3577930)
                                       guard fires -> exit 0, PYTEST NEVER RUNS
        rung6 populated + regression gone  guard fires -> exit 0
        both populated                     runs, 2 passed, exit 0
        rung1 DIRECTORY RENAMED AWAY       guard fires -> exit 0
                                           (the line CA1 replaced: EXIT 4, RED)
        rung1 files renamed off test_*.py  guard fires -> exit 0
                                           (the line CA1 replaced: EXIT 5, RED)
        rung1 tests moved into a SUBDIR,
          containing a FAILING test        guard fires -> exit 0, REPORTED GREEN
        rung1 genuinely empty              exit 0   correct
        file present, collects nothing     exit 5   correct
        file present, broken import        exit 2   correct
        file present, test fails           exit 1   correct
      5 of 10 do what the entry requires. 5 do not.
judge MECHANISM, stated as the measurement: ls A B exits non-zero when EITHER
      glob fails, so a two-glob guard runs its rung only when BOTH halves are
      populated. rung6 is empty BY DESIGN, so tests/regression -- the golden file
      for G2.2 exempt pairs, the one artefact CLAUDE.md ties to a written
      explanation -- can never run in CI under this guard.
judge AND THE PUBLISHED SENTENCE IS REFUTED. "A renamed directory" is named at
      :65 as a defect the arrangement catches. Measured, a renamed rung directory
      goes from exit 4 to exit 0: CA1 made that case STRICTLY WORSE than the line
      it replaced. So did a rename off the test_ prefix, and so did moving tests
      one directory down, which now hides a genuinely failing test.
judge WHY THIS IS NOT 4a. This is not apparatus around the gate; it IS the gate
      that item 3b was added in this same range to make binding. A verdict that
      reads gh run list and finds green is now reading a rung that can be green
      while running nothing -- "empty parameter set is an error, not a skip",
      applied to the job that decides whether a verdict may say PASS. It has not
      bitten yet only because rungs 5 and 6 have never executed.
```

**Closed when** rung 6 runs `tests/regression` at the current layout -- shown by a
CI log line carrying a non-zero pass count from that path, not by reading the YAML
-- and each rung distinguishes "the directory holds no test file" from "the
directory is not there", "the files are not named test_*" and "the tests are one
level down". The ten layouts are on disk at `tests/corpus/ci_ladder_gating.txt`
with the measured outcome per entry.

**R231. (BLOCKS -- CA2, and head 3 against a gate F1 CLOSED) CI is red at the
reviewed commit. Ladder 4 fails 13 tests, and the failure is a defect in the
assertion, not in the data: G1.1's bit-exact round-trip conflates a container
claim it does not test with a libm claim that is false across platforms.**
`tests/verification/rung4/test_writer_round_trip.py:92-103`, comment at `:98-99`.

```
code  :95-97  want is RECOMPUTED at test time from np.sin / np.cos; got is read
      from the committed fixture.
code  :98-99  "Bit-exact, not approximate: HDF5 float64 is a lossless container,
      so any difference at all is a defect rather than a rounding artifact."
judge THE CONTAINER CLAIM IS TRUE AND THE TEST DOES NOT TEST IT. Nothing here
      compares stored bytes with stored bytes. What is compared is a stored value
      against a fresh transcendental evaluation, so the assertion ALSO claims that
      np.sin and np.cos are bit-reproducible across machines. They are not: IEEE
      754 does not require correctly-rounded transcendentals.
cell  THE CONTROLLED CELL IS ALREADY IN THE FAILURE LIST, and it is free. Of the
      15 bit-exact assertions in this file, 13 fail on CI and 2 pass:
        FAIL  12 kinematic channels  -- every one computed through sin or cos
        FAIL  joints/lam             -- computed through cos
        PASS  time/t                 -- np.arange(N+1) * DT, ARITHMETIC ONLY
      One variable moved: whether the channel passes through libm. That is the
      cause, measured, not asserted.
cell  AND THE MAGNITUDE IS ONE LAST BIT, which I measured rather than accepted
      from the report figure of 1--2 ULP:
        channel                max|v|      1 ULP there   CI max|diff|   in ULP
        position               1.099863    2.2204e-16    1.1100e-16     0.50
        rotation               0.024995    3.4694e-18    3.4690e-18     1.00
        velocity               2.059974    4.4409e-16    2.2200e-16     0.50
        angular_velocity       2.147823    4.4409e-16    2.2200e-16     0.50
        acceleration           2.999351    4.4409e-16    4.4410e-16     1.00
        angular_acceleration   2.934568    4.4409e-16    4.4410e-16     1.00
      Never above one ULP of the channel own amplitude, at any channel. NO
      FIXTURE VALUE IS WRONG AND NO PRODUCT CODE IS IMPLICATED.
judge THE RESTRAINT WAS RIGHT AND I RULE FOR IT WITHOUT QUALIFICATION. The two
      available fixes are to split the two claims or to declare a ULP tolerance,
      and both change what a gate F1 closed asserts. CLAUDE.md: "If execution
      reveals that the locked plan was wrong, stop and say so -- do not silently
      adapt the plan while implementing it", and "Never widen a tolerance ...
      Report the failure instead." Touching it inside step 5 would have been the
      finding. Leaving it red and naming it is the correct output.
judge WHY HOLD AND NOT STOP, said so it can be argued with. STOP is for a wrong
      locked plan or a red LOW rung. Rungs 1, 2 and 3 are green on CI, so step 5
      own rung is interpretable and agrees bit-for-bit with my local run
      (1013 = 1013). No product code is implicated: 21 of the 42 changed .py files
      carry an AST change and not one is in the failing path. What is wrong is one
      test assertion, in a milestone that is closed, and the route for changing a
      gate asserted quantity already exists and is a lock Q&A. **If the answer is
      that G1.1 must assert a different quantity, that is a plan change and it
      comes back before code lands** -- the same ruling I gave R223, applied to
      the same species.
judge AND CA2 IS BINDING ON ME REGARDLESS. I wrote it into my own reading order in
      this range; a red CI is a HOLD whatever the local run says. "1578 passed
      locally" is not a defence, and it is exactly the sentence CA2 exists to
      refuse.
```

**Closed when** ladder 4 is green on CI at a reviewed commit, by an assertion that
tests one claim at a time: a stored-vs-stored comparison for the container claim,
and -- if a recomputed reference is kept at all -- a declared, counter-carrying
tolerance for it whose value comes back through the gate-change route rather than
into a step commit. Until then ladders 5 and 6 are an unavailable check, not a
pass.

**R232. (recordable, 4a) No step report covers this range, and the directives CA0
and CA1 appear nowhere in `docs/`.** `docs/reports/F2/step-5.md` unchanged.

```
cmd   git diff --name-only 5ade3a5..HEAD -- docs/reports
out   (empty) -- three code and CI commits, no report revision.
cmd   grep -n for the Answers header in docs/reports/F2/step-5.md
out   "verdict 25 @ aae355a" -- correct for the report it is, which predates
      verdict 26. Item 1b does NOT trigger: the report legitimately predates the
      findings, and tests/test_report_carried.py is green for the same reason.
cmd   grep -rn for CA0, CA1, CA2 over docs/
out   ONE hit: docs/SUPERVISOR.md:63, CA2. CA0 and CA1 are recorded only in their
      own commit bodies.
judge Not blocking, and I say why rather than assert it: the two commit bodies are
      the best in this repository -- both carry claim/command/output triples, and
      every one I checked reproduced. Nothing is hidden. What is missing is that a
      reader coming to docs/ cannot find the directive that asked for either
      change, and the Stop hook cannot see the gap, because the newest REPORT has
      a verdict while three commits sit after it. Recorded so that the mechanism
      is on the list, not the diligence.
```

**Closed when** the answering report covers `e5f6deb`, `99d0565` and `3577930`
with their directives named, or 4a records that a `process:` or `ci:` commit body
is the artifact of record and the hook condition is amended to match.

**R233. (recordable, 4a) Two `out` fields in the `e5f6deb` commit body do not
describe the commit they ship with.** `git log -1 e5f6deb`.

```
code  body: "SIX SITES SUPPRESSED ... each named here one per line:
      :45 :47 :62 :63 :64 :65"
cmd   git grep -n NPY002 at e5f6deb in tests/verification/rung3/test_determinism_pins.py
out   :53 :55 :69 :70 :71 :72. The six sites EXIST, are the right six, and each
      reason is correct; the numbers are the pre-commit ones for two of them and
      neither pre nor post for four. Same species as R226.
code  body: "F841 + B007 + SIM102 + E741 x2 ... B905 x2"
cmd   ruff check, repo config, on the pre-commit file content
out   also SIM300 (yoda-condition) and I001. SIM300 rewrote the operand order of
      at least three assertions: assert s.A < math.pi*d*t became
      assert math.pi*d*t > s.A, and x == pytest.approx(y) became
      pytest.approx(y) == x.
judge SEMANTICALLY INERT and I checked rather than assumed: both operands are
      unchanged, the operator is reflected, and pytest.approx compares
      symmetrically. Not a widening. Recorded because the enumeration is presented
      as complete and is not, in a commit whose whole claim is that nothing else
      changed.
```

**Closed when** an `out` field says what its command prints at the commit that
publishes it, and a rule enumeration is produced by `ruff --statistics` rather
than typed.

## Rulings I was asked for

**1. Was it legitimate to land `e5f6deb` over an open HOLD? YES, narrowly -- and
the criterion is written down here so it can be argued with, because "answered
before anything else" says otherwise on its face.**

```
judge The plain reading of a HOLD is that the listed items come first. e5f6deb
      answered neither R223 nor R224 and landed before both. I take that
      seriously: this project has already had a step executed cleanly on top of
      unanswered items, and that is the failure the re-read guard exists for.
judge I RULE FOR IT ON THREE CONDITIONS, ALL VERIFIED MECHANICALLY, NOT READ:
  (a) IT CANNOT MOVE A GATED QUANTITY.
      cmd  git diff 5ade3a5..HEAD -- floatfea/tolerances.py
      out  -12 +0, every one a blank line. No value, name, form or counter moved.
      cmd  git diff --name-only 5ade3a5..HEAD, filtered to paths outside
           floatfea/ tests/ docs/ .claude/ .github/
      out  (empty) -- pyproject.toml UNTOUCHED. No rule disabled, no file
           excluded, no per-file ignore added.
      cmd  ast.dump of every changed .py file, before vs after
      out  42 changed; 21 AST-IDENTICAL. Of the 21 that differ, the COMPLETE set
           of changes to numeric constants, comparison operators and call keywords
           across the whole diff is: +2 zip.strict, +1 float(), -1 .items() and
           +1 .values(), one Lt->Gt (SIM300, reflected), one int 0 removed (F841),
           and the exemption window. NOT ONE NUMERIC TOLERANCE VALUE CHANGED
           ANYWHERE IN THE RANGE.
  (b) THE VERIFICATION IS MECHANICAL, not a reading. It is, above.
  (c) IT UNBLOCKS AN INDEPENDENT CHECK, measured rather than argued: CI had never
      executed the ladder, and executing it produced 13 failures in a rung green
      locally for weeks, plus 1013 = 1013 agreement on rung 1. The closing
      paragraph of the twenty-sixth verdict asked for exactly this -- an
      independent reader. Getting one before answering a finding about a stated
      invariance is a defensible ordering and I endorse it.
judge THE COST IS REAL AND I RECORD IT RATHER THAN WAIVE IT. Three of the five
      sites R223 names moved (see Carried). A closing condition that names sites
      got harder to check. The drift was not deliberate; re-locating it is still
      owed by the answering report.
judge AND THE COUNTER-ARGUMENT IS IN THIS VERDICT. Condition (a) is FALSE in one
      respect: e5f6deb widened the escape hatch on the rule that keeps tolerances
      in tolerances.py (R229). A commit framed as lint and formatting contained
      the one change in the range that a purely cosmetic commit could not have
      contained. **That is the argument against landing large work over an open
      HOLD, and it is not rhetorical -- it is the finding.** The ruling stands;
      the precedent does not extend past the three conditions.
```

**2. The six per-line `# noqa: NPY002` suppressions. WITHIN THE DIRECTIVE. Ruled
for.**

```
cmd   git grep -n noqa at 5ade3a5 over floatfea tests, and the same at HEAD
out   15 pre-existing (E402 x14, BLE001 x1) before, THE SAME 15 after, plus
      exactly SIX new, all NPY002, all in test_determinism_pins.py, each with its
      reason at the site. NOTHING ELSE SUPPRESSED, and pyproject.toml untouched.
judge "fixed, or the report names it with the reason it cannot be" is met: the
      reason is at the site AND in the commit body, one per line. And the reason
      is correct rather than plausible -- np.random.Generator cannot perturb the
      legacy global state, so the modern call would leave both assertions in
      deterministic_v0 true BY CONSTRUCTION. That is the vacuous-gate failure
      mode, and writing the modern call would itself have been the finding. The
      rule stays active everywhere else and no file is excluded.
judge The line numbers in the body are stale -- R233, recorded, not blocking.
```

**3. The two real defects. Both fixes are right, and one of them is a guard.**

```
code  floatfea/io/frames.py:37-40 -- import numpy as np now at module level, three
      in-body imports removed, and the two annotations at :228 and :285 are no
      longer string-quoted. The name was undefined at the scope that used it.
judge Correct, and the module-level comment states the reason. mypy floatfea is
      green on CI, which is the first time that has been true.
code  zip(..., strict=True) x2, the second one in
      tests/verification/rung4/test_live_dof.py, over DOF_NAME and mask.
judge THAT IS AN ASSERTION-DOMAIN FIX, not a style fix. A mask shorter than
      DOF_NAME would silently reduce the collection the assertion inspects --
      "check that the collection the assertion inspects can actually contain the
      failure", verbatim. Ruled for.
```

## Tolerances touched

**None. No value, no name, no form, no counter, no justification sentence.**

```
cmd  git diff 5ade3a5..HEAD -- floatfea/tolerances.py
out  -12 +0, all blank lines removed by black. Diffed line by line.
cmd  AST feature scan over all 42 changed .py files -- numeric constants,
     comparison operators, call keywords -- before vs after
out  no numeric literal changed value anywhere in floatfea/ or tests/.
cmd  git diff 5ade3a5..HEAD -- tests/regression/g22_exempt_pair_responses.json
out  (empty) -- no golden file moved.
```

**What DID move is the ENFORCEMENT of the tolerance rule**, and that is R229: the
exemption window on `tests/test_no_tolerance_literals.py` was enlarged in the same
commit as the reformatting that reddened it. Under the CLAUDE.md extension of the
tolerance rule to "anything that functions as a tolerance under another name",
that belongs in this section and not only under Findings.

**My own instructions (item 4b).** `3577930` is a **standalone `process:` commit**
touching only `.claude/agents/gating-supervisor.md` (+15) and `docs/SUPERVISOR.md`
(+8), citing directive CA2, with no `floatfea/` and no `tests/` change. **Purely
additive: 23 lines added, none removed, no guard weakened.** Reviewed line by
line. `.claude/hooks/` and `.claude/settings*.json` are untouched across the whole
range. No commit in the range touches both code and `docs/reviews/`. CLEAN.

**What held**, reproduced at my run: `1578 passed, 0 failed, 0 skipped`; rung 1
`1013 passed` locally and `1013 passed` on CI; `pyproject.toml` untouched; every
one of the 42 changed files AST-compared and no tolerance value moved; the six
NPY002 sites and their reasons; both `strict=True` fixes; the `frames.py` F821
fix; the `process:` commit standalone and additive; the hooks untouched. **These
did not**: the exemption window (R229), the rung-6 guard (R230), ladder 4 on CI
(R231), the report gap (R232), two `out` fields (R233) -- and R223 and R224, which
are unchanged and which nobody claimed otherwise.

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Five items. The first three are new
and come before the two carried, because two of them are the machinery that
decides whether any later verdict means anything.

1. **R231 -- CI green through ladder 4**, or the finding routed as a plan change
   through the gate-change route the technical supervisor already owns. Until
   ladders 5 and 6 run once, they are recorded as unavailable, never as passing.
   **Do not close this by widening np.array_equal into a tolerance inside a step
   commit.**
2. **R230 -- `tests/regression` demonstrably executed by ladder 6 on CI**, shown
   by a log line with a pass count from that path. The ten layouts in
   `tests/corpus/ci_ladder_gating.txt` are the shapes; five of them currently do
   the wrong thing and one of the five is the repository as it stands.
3. **R229 -- the exemption window**, closed on the three properties named in the
   finding, each as a test that reddens if the property is false. A narrower rule
   with zero false positives across the whole `tests/` tree exists and I measured
   it: 4 of 28 remaining, down from 19.
4. **R223** -- the five sites, **re-located above at `3577930`**:
   `floatfea/tolerances.py:293`, `tests/verification/rung1/test_rigid_body_modes.py:19`
   and `:175-177`, `docs/milestones/F2.md:51` and `:1477`. Site by site. The
   invariance in `E` HOLDS over fifteen decades and should be kept; the section,
   the mesh and the length unit do not. `F2.md:1491-1492` carries its operating
   point or is withdrawn, in the same commit (BP0).
5. **R224** -- `floatfea/tolerances.py:295-297` and `:300-308`, both sites, one
   branch each.

**Not gates on step 5, into the next report Carried section:** R232, R233,
R225--R228, and everything already at 4a.

**And the witness.** PR #1 is open at `3577930` and there is still no
`[witness F2 step 5]` comment. This is the twenty-seventh consecutive review by
one reader. **CI is the first thing in the history of this project that read the
code without sharing my assumptions, and the first time it reached the ladder it
contradicted twenty-six rounds of green.** A witness HOLD is answered exactly like
this one; where we disagree the stricter verdict stands and the disagreement goes
in the report.

**Adversarial corpus (BE3): 38 new entries committed at `964d1a5`, in two new
files, all unseen by the implementer; every `measured` field taken at `3577930`
before the line was written.**

**The coverage measurement, stated plainly: of my 38 new entries the shipped
checks did what the entry requires on 14.**

* `tests/corpus/tolerance_marker_exemptions.txt` -- **28 entries, 9 correct, 19
  misses.** All 19 misses are planted violations the new window exempts and the
  old window caught. All 4 legitimate exemptions survive, so the guard stays
  usable. A NEW FILE, because the coverage claim of that scanner rested on fifteen
  shapes its own author wrote, and not one of the fifteen exercises the exemption
  at all.
* `tests/corpus/ci_ladder_gating.txt` -- **10 entries, 5 correct, 5 misses.** One
  of the five is not hypothetical: it is the repository at `3577930`.
* `pytest -q` is **1578 passed with both files on disk, unchanged** -- zero of the
  38 is executed by anything in the shipped suite.

**Twenty-seven consecutive rounds have found no element defect, and this round
does not either.** `floatfea/` gained one module-level import and lost three
in-body ones; nothing else in it moved. What moved this round is the instruments
around it -- and for the first time the instruments were read by a machine that
did not write them, which is how thirteen failures surfaced in a rung that had
been green here for weeks.
