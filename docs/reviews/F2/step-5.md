# Review — F2 step 5
Reviewed commit: ec28446b257d5e90b4ce86682dd358779051f16d
Verdict: HOLD

Tests: **1722 passed, 0 failed, 0 skipped** (my run at `a59521e`, `python -m pytest -q`,
245.52 s, Python 3.13.11 on Windows). Identical to the report's figure. With my
thirty-first-round corpus applied: `tests/test_ci_ladder_gating.py` gives **5 failed,
34 passed**; the two new corpus files have no runner and induce zero failures.

**Code under review: `839b56b`. Report: `a59521e`.** The verdict is stamped at my
corpus commit, which is HEAD.

**CI, item 3b, at the reviewed commit.**

```
cmd  gh run list --commit a59521ec276ff8296ced03f38e258ee4796fc94f
out  34424766023 (push) failure   34424768066 (pull_request) failure
cmd  gh run view 34424766023 --json jobs
out  lint and type-check     success      unit tests            success
     ladder 1 / 2 / 3        success      guards and meta-tests FAILURE
     ladder 4                failure      ladder 5, ladder 6    skipped
cmd  gh run view 34424766023 --log-failed
out  guards:   1 failed, 425 passed -- test_plan_figures.py::
               test_the_generated_figures_are_not_stale            <- R245
     ladder 4: 13 failed, 72 passed -- test_writer_round_trip.py   <- R231
judge RED, AND BOTH REDS ARE ROUTED. Every failure at this commit is an item
      already open by instruction pending Q8. That is not a new finding and I do
      not raise one; it does mean CA2's condition is unmet and stays unmet until
      Q8 lands.
judge AND IT MOVED THE RIGHT WAY. 4 failed / 386 passed at `fa3b070` to
      1 failed / 425 passed here. `shallow_clone_depth_1` no longer raises
      `TypeError` on the runner: `onerror=` is the correct spelling for 3.11 and
      the handler ignores its third argument, so it fits either signature. R253's
      hard half is closed and CI is where I read it.
```

`git diff 1b93db0..a59521e -- .claude docs/SUPERVISOR.md` is empty -- not one byte. No
commit in the range touches `docs/reviews/`. `-- floatfea/tolerances.py` is empty,
`-- tests/regression` is empty, `-- docs/milestones/F2_figures.md` is empty. The one
`floatfea/` change is a return annotation in `determinism.py` with no runtime effect.
The header at `docs/reports/F2/step-5.md:898` reads `Answers: verdict 30 @ 1b93db0`
and `1b93db0` is the thirtieth and latest verdict. **Item 1b passes.**

**PR #1 is open, `F2 -> master`, and `gh pr view 1 --json comments` returns none.**
Step 5 still has no outside-witness comment; recorded as an unavailable check, not as
a pass.

## Carried

Verdict 30 listed eight numbered conditions. **Four close. One closes in substance with
a clause unmet. Three do not close, and one of those three was recorded in the report
as belonging to step 4a.** Six items are open by instruction.

- **R253 -- CLOSED.** `tests/test_report_guard_states.py:241-247`. `onerror=` for
  `onexc=`, and the state now executes on the runner: the failure is absent from run
  `34424766023`. The report carries CI per job in section 0 with the run id. I read the
  run rather than the table.

- **R254 -- ANSWERED IN MECHANISM, ONE CLAUSE UNMET.** I ran the ablation rather than
  reading about it.

```
cell a `git clone --local` at a59521e; the only thing varied is the
     return-code branch in `_changed_lines` (test_report_carried.py:486-496),
     removed, nothing else:
       shipped  2 passed  (both shallow states)
       ablated  1 failed, 1 passed
     The failure is `shallow_clone_depth_1_reports_one_diagnosis_not_sixteen`,
     and it names its cause: "the guard failed, but
     `test_the_diff_the_site_check_needs_is_available` ... is not among".
judge THE ABLATION IS REAL AND IT IS THE ONE I ASKED FOR. `assert code != 0` no
      longer decides it; the pair does.
judge THE OTHER STATE STILL DOES NOT SEE IT. `shallow_clone_depth_1` PASSED under
      the same ablation, because it is in `REQUIREMENT_CHANGED` and the function
      returns at :354 before the `DIAGNOSIS` block at :370 is reached. Its
      `DIAGNOSIS` entry is unreachable code. That is R276.
judge AND THE SECOND CLAUSE OF THE CLOSING CONDITION IS UNMET -- "and `:196-198`
      says what it means". `tests/test_report_carried.py:215` still reads "the
      report answers verdict `{ANSWERED}`, which is not a commit in this
      repository." It is a commit; the clone does not have it. That is R273.
```

- **R256 -- ANSWERED IN SUBSTANCE, ONE CLAUSE UNMET.** `.github/workflows/ci.yml:235`
  carries `empty:tests/verification/rung6 full:tests/regression` again;
  `tests/verification/rung6/.empty-by-design` is restored with a five-line reason;
  `ARGS["rung6"]` matches. The four sentences R256 measured as false are true again by
  restoration rather than by edit, which is the better of the two routes the condition
  offered. **The clause "and either way the change is stated in the report" is unmet:**
  `grep -n "rung 6" docs/reports/F2/step-5.md` finds the change nowhere in revision 5,
  only in the commit message and in a Carried row that reads `open ... 4a`.

- **R257 -- CLOSED, and the ruling was taken in full.** `tests/test_no_tolerance_literals.py:263-280`:
  `claimed` is gone, the loop discards `node_id`, and the two bracket statements carry a
  second `# not-a-tolerance:` marker naming the lower bound. One marker, one threshold.
  I re-measured both files and both are clean, and I re-measured the hole node-keying
  had opened -- `assert 1e-09 < r < 0.05` with one marker -- and it is flagged again.

- **R255 -- NOT ANSWERED.** R269.
- **R258 -- NOT ANSWERED.** R270.
- **R259 -- NOT ANSWERED.** R271. One of the four named rows is refused.
- **R260 -- ANSWERED FOR THE SHAPE, NOT FOR THE CONDITION.** R272.

- **R261 -- OPEN, correctly, and the report states both clauses.** Section 5 records
  that there is no lockfile and that the basis for `2` is not published in the rule's
  own quantity. No Q8 value was written. That is right and I say so again.

- **R231, R244, R245, R230, R223, R224 -- OPEN by instruction.** Site by site, confirmed
  untouched: `floatfea/tolerances.py:293`, `:295-297`, `:300-308`;
  `tests/verification/rung1/test_rigid_body_modes.py:19`, `:175-177`;
  `docs/milestones/F2.md:51`, `:1477`, `:1491-1492`. `tests/regression` has still never
  executed on CI -- ladder 6 skipped again at this commit. **R244 has moved and not in a
  good direction: R275.**

- **R262-R266, R248's two residues, R249, R250, R251, R252, R225-R228, R232, R233** --
  carried. R263 and R265 are now fixed in the code (I re-ran both) though the report
  files them at 4a; R264 and R266 are not, and R266 has recurred as R269.

## Findings

**R267. (BLOCKS -- head 3, and it is the dependency list itself) The report's Carried
table attaches this step's work to the wrong finding numbers, and routes four of
verdict 30's eight blocking items to step 4a.** `docs/reports/F2/step-5.md:1043-1062`.

```
cmd  grep -n "^\*\*R2[0-9][0-9]\." docs/reviews/F2/step-5.md
out  the thirtieth verdict's findings are R253..R266. R253 = CI is red / the
     `onexc` interpreter split. R254 = the shallow-clone certificate.
     R255 = the scanner's "What is flagged" list. R257 = the exemption window.
     R259 = the vocabulary. R260 = the `xpassed` arm.
code report :1051  | R248 | **answered** - S1, the interpreter is pinned |
     report :1052  | R249 | **answered** - S2, the ablation asserts the diagnosis |
     report :1054  | R251 | **answered** - S3, the vocabulary reads stripped text |
     report :1055  | R252 | **answered** - S3, the contradiction domain |
     report :1056  | R253 | **answered** - S3, value-keying plus two markers |
     report :1057  | R254 | **answered** - S3, the `xpassed` arm can be fed |
     report :1058  | R255 | **answered** - S0, the report carries CI per job |
judge SIX ROWS, SIX WRONG NUMBERS. R248, R249, R251 and R252 are the TWENTY-NINTH
      verdict's findings -- run_rung residues, the scanner's misses, the
      step-6-draft read, regen_figures --check. R253 is the red CI, not
      value-keying. R254 is the certificate, not `xpassed`. R255 is the scanner
      docstring, not the CI table.
code report :1060-1063  | R257 | **open** - 4a |  | R258 | **open** - 4a |
                        | R259 | **open** - 4a |  | R260 | **open** - 4a |
judge AND THE OTHER HALF IS THE SAME ERROR RUNNING BACKWARDS. R257, R259 and R260
      are recorded as deferred to 4a and this commit CLOSES two of them and moves
      the third. R258 is recorded as deferred to 4a and is genuinely unanswered.
      A step report may not route a verdict's blocking item to 4a; the criterion
      in `.claude/agents/gating-supervisor.md` sec. "What blocks this step" is
      the verdict's to apply, and it applied it.
cmd  pytest tests/test_report_carried.py -k "carries_the_finding" -q
out  all green. The guard checks that each number APPEARS with a report word. It
     cannot see which work is attached to which number, and that is the whole of
     what a Carried table is for.
judge THIS IS THE FAILURE `CLAUDE.md` sec. Step gating exists for, in its own
      words: "the dependency list -- the open items from the last review -- is
      part of what gets re-read at every step". Six of the entries in this one
      point at the wrong dependency, and three real gaps are hidden behind a
      routing the report was not entitled to make.
```

**Closed when** every row of the Carried table names the finding verdict 30 gives that
number, and no item verdict 30 headed `(BLOCKS ...)` carries a `4a` status.

**R268. (BLOCKS -- head 3) The interpreter guard is inert exactly where the pin is
honoured, which is all nine CI jobs and, once CE0 succeeds, everywhere.**
`tests/test_the_pinned_interpreter.py:110-113`, against `:14-26` and report section 1.

```
code :110-113  if pinned == running: return
cell ONE VARIABLE MOVED, everything else held. A `git clone --local` at
     a59521e with `onexc=` reinstated at test_report_guard_states.py:247:
       requires-python ">=3.11,<3.12", running 3.13  -> 1 failed, and the
         message is `Unexpected keyword argument "onexc"` at the pinned 3.11
       requires-python ">=3.13,<3.14", running 3.13  -> 1 passed in 0.01s
     Same defect, same file, same line. The only thing that changed is whether
     the pin equals the interpreter.
cmd  grep -c "python-version" .github/workflows/ci.yml ; the runner log
out  9 of 9 jobs at "3.11"; pythonLocation .../Python/3.11.16/x64
judge SO ON CI, `pinned == running` AND THE GUARD RETURNS AT LINE 113. It ran in
      the guards job at this commit and asserted nothing. The one machine CA2
      exists to consult is the one machine where CE0's central check is a no-op.
judge AND THE STEADY STATE IS WORSE THAN THE PRESENT ONE. The guard measures
      something only while the implementer's interpreter DISAGREES with the pin
      -- that is, only while CE0's own goal is unmet. The moment 3.11 is
      installed locally, as CE0 asks, the check evaporates in silence.
code :24-26  "WHAT IT DOES NOT PIN, said so it is not trusted past its reach: the
     patch version, and the libraries."
code report S1  "The difference-guard is what covers the gap, and it covers the
     class rather than the instance."
judge A PARAGRAPH WHOSE ENTIRE PURPOSE IS TO STATE THE REACH omits the condition
      under which the reach is nil, and the report's sentence is refuted by the
      cell above. It covers the class on one machine and no class on the other.
judge WHAT WOULD NOT HAVE THIS PROPERTY, described rather than written: compare
      mypy at the pin against mypy at a FIXED newer reference version recorded in
      the file -- the highest version the project expects to meet -- rather than
      against `sys.version_info`. That difference is the same measurement, it is
      identical on every machine, and it does not vanish when the environment
      becomes correct. `mypy --python-version` takes both, so neither has to be
      installed.
judge AND `return` IS NOT "SAY SO". The comment at :111-112 reads "Say so rather
      than passing silently" and the branch prints nothing, warns nothing and
      reports a pass. AM5 in `pyproject.toml:45` -- an empty parameter set is an
      ERROR, not a skip -- is the same rule one level up.
```

**Closed when** the check measures the same thing on a machine whose interpreter equals
the pin, shown by a run at `pinned == running` that reddens on the `onexc` call; or the
docstring's reach paragraph and the report's sentence say that it does not, in the same
commit.

**R269. (BLOCKS -- head 3) R255 is not answered: the scanner's "What is flagged" list
still states the opposite of what the scanner does, and the site table declares its five
lines "evidence, not a site to change" against R255's own closing condition.**
`tests/test_no_tolerance_literals.py:29-33`; `docs/reports/F2/step-5.md:1104-1108`.

```
cmd  git diff 1b93db0..a59521e -- tests/test_no_tolerance_literals.py
out  the only hunks are at :263-280. Lines 27-33 are untouched.
code :29-33  "**The left operand is not read** (R237): ``assert 0.05 > ratio``
             returns nothing ... the sentence is what was false and it is fixed
             here."
cell the shipped `offending()` on a file whose only body is
     `assert 0.05 > ratio`
out  [(3, "comparison against 0.05")]
code :218-224  "BOTH SIDES (R237, closed at CD2)" / for comp in [node.left, ...]
judge THE FILE CARRIES BOTH SENTENCES, TWELVE LINES APART, SAYING OPPOSITE THINGS,
      and the false one ends by asserting it has been fixed.
code verdict 30, R255: "**Closed when** `:27-33` describes what `:218-254` does,
     or the code stops doing it."
code report :1104-1108, five rows: "`tests/test_no_tolerance_literals.py:29`
     ... **no change** -- R255 quotes it as evidence, not as a site to change"
judge THIS IS R266 A SECOND TIME, IN THE SAME TABLE, ONE ROUND LATER. R266 was
      recorded because four lines a closing condition named as the site to change
      were declared evidence. Five more are, and this time the finding they
      belong to is entirely unaddressed. `test_report_carried.py` accepts a
      `no change` declaration for any named site, so the table's own guard cannot
      tell a site left deliberately from a finding not read.
```

**Closed when** `:27-33` describes what `:218-254` does, and the five rows say so.

**R270. (BLOCKS -- head 3) R258 is not answered: two figures that do not reproduce are
still published and are not withdrawn.** `docs/reports/F2/step-5.md:713`, `:745-746`.

```
cmd  git show --stat a59521e -- docs/reports/F2/step-5.md
out  258 insertions(+), 0 deletions(-) -- revision 5 appends and changes nothing
cmd  grep -n "121 passed" docs/reports/F2/step-5.md
out  713: after:  `121 passed` -- the file is stepped over
     746: 12 marker shapes, 10 guard states, 9 ladder layouts, 1 site declaration
judge BOTH REFUTED LAST ROUND AND BOTH STILL STANDING: 123, not 121; and 12 / 9 /
      13 / 0, not 12 / 10 / 9 / 1. Verdict 30: "Closed when both figures are
      regenerated at the report's own commit, or withdrawn." Neither happened,
      and revision 5 does not mention them.
cmd  grep -n "step-5.md:74" docs/reports/F2/step-5.md
out  (nothing) -- only `:713` reaches the site table, because verdict 30 wrote
     the second site as a bare `:745-746` and `_SITE` needs a filename. The
     parser hole is R254's, not a defence.
```

**Closed when** both figures are regenerated at the commit that publishes them, or
withdrawn in the text where they stand.

**R271. (BLOCKS -- head 3) One of the four formattings verdict 30 named is refused. The
report's account of the fix is refuted by the shipped code, and the corpus file still
has no runner.** `tests/test_report_carried.py:325`, `:328-334`; report section 3.

```
cell each row appended to the newest revision's Carried table in a `git clone
     --local` at a59521e, then
     pytest tests/test_report_carried.py -k "CLOSED or report_words or
     status_claims". The four verdict 30 named, plus the control:
out  | R230 | **closed** ... |                  -> 1 failed   caught (control)
     | **R230** | **closed** ... |              -> 3 passed   STILL MISSED
     | `R230` | **closed** ... |                -> 3 passed   STILL MISSED
     | R230 | **closed** ... | still open |     -> 3 passed   STILL MISSED
     | R230 | **resolved**, nothing open |      -> 1 failed   caught
code report S3  "It reads markdown-stripped text across every cell now"
code :328-334  status = rest.rsplit("|", 1)[-1] -- THE LAST CELL, unchanged
code :325      _ROW anchors on ^\|\s*(R\d+ -- unchanged, so a first cell wearing
               any markup is not parsed as a row at all
judge THE SYNONYM CLAUSE IS TRUE AND THE CELL CLAUSE IS NOT. `_plain` strips
      markup from the status cell, which is real; nothing strips it from the
      item cell, and nothing reads any cell but the last. One of four.
cell the contradiction domain, which IS better: | R253 | **withdrawn** |
out  1 failed -- caught. The domain is every finding the verdict names.
     | **R253** | **withdrawn** | -> 1 passed. The same bolding defeats it.
cmd  grep -rn "report_status_vocabulary" tests/ scripts/ .github/
out  (nothing outside tests/corpus/). Verdict 30: "with the corpus file given a
     runner, so the next four formattings are measured rather than argued." The
     file induces zero failures and measures nothing.
code test_a_report_does_not_say_CLOSED docstring: "Taking the word away removes
     the failure mode rather than detecting it."
judge STILL THERE. Verdict 30's alternative was explicit -- route the reach to 4a
      AND withdraw that sentence in the same commit. Neither branch was taken:
      the sentence stands, the row says 4a, and section 3 claims a reach the code
      does not have.
```

**Closed when** the three remaining formattings are refused, or the sentence at
`test_a_report_does_not_say_CLOSED` and report section 3 are withdrawn in the same
commit -- and `tests/corpus/report_status_vocabulary.txt` has a runner either way.

**R272. (BLOCKS -- head 3, and it is the ladder's own gate) A summary reading exactly
`1 xpassed` at exit 0 is still producible. One keyword restores R260.**
`scripts/run_rung.sh:125-131`.

```
cell shipped scripts/run_rung.sh at a59521e, scratch trees, one variable moved:
out  rung1 full, only test is @pytest.mark.xfail, body PASSES
       -> "1 failed", "[XPASS(strict)]"     exit 1, named          FIXED
     rung1 full, only test is @pytest.mark.xfail(strict=False), body PASSES
       -> "1 xpassed in 0.21s"              exit 0, "run_rung: OK" MISSED
     rung1 full, a genuinely skipped test   exit 1, named          control ok
     rung1 full, an atexit hook printing a skip line after the summary
       -> exit 0                            R263 FIXED, re-run by me
judge -o xfail_strict=true IS AN INI OVERRIDE AND THE MARKER OWN ARGUMENT BEATS
      IT. The junit report then records the xpass as a pass -- skipped="0" -- so
      the (skipped|xfail)="[1-9] grep sees nothing either. The rung reports OK
      having asserted the opposite of what its test says.
code verdict 30, R260: "**Closed when** `run_rung.sh` reddens on `1 xpassed`
     alone, shown as a run."
judge THE CONDITION IS LITERAL AND IT IS UNMET. What the fix reddens on is a
      strict XPASS, which pytest reports as a FAILURE, not as an xpass. The
      script still has no path that reddens on the word the condition names.
      `tests/corpus/ci_ladder_gating.txt` carries it as
      ci_rung_full_xfail_marker_carries_strict_False_and_the_body_PASSES.
```

**Closed when** a rung whose summary reads `1 xpassed` exits non-zero, shown as a run.

**R273. (BLOCKS -- head 3) The second clause of R254's closing condition is untouched:
a test still tells its reader that a commit in this repository is not one.**
`tests/test_report_carried.py:215`.

```
cmd  git show fa3b070:tests/test_report_carried.py | grep -n "is not a commit"
out  197: ... which is not a commit in "this repository."
cmd  grep -n "is not a commit" tests/test_report_carried.py
out  215: ... which is not a commit in "this repository."
judge THE LINE MOVED BY EIGHTEEN AND THE SENTENCE DID NOT CHANGE. In the state
      that produces it -- a shallow clone -- the commit exists; the clone does
      not have it. That is the diagnosis a reader needs and the opposite of the
      one they are given. Verdict 30: "and `:196-198` says what it means."
```

**Closed when** the message distinguishes "no such commit" from "this clone does not
contain it".

**R274. (BLOCKS -- head 3) The sentence that replaces the withdrawn ratio names a test
that cannot observe the thing it is said to assert.**
`tests/test_marker_exemption_corpus.py:209-221` against
`tests/test_no_tolerance_literals.py:362-370`.

```
code :215-218  "NO FALSE PASS ON A REAL FILE.
               `test_no_undeclared_tolerance_reaches_a_comparison` runs the
               scanner over every file under `tests/` at every commit."
code test_no_tolerance_literals.py:362-364
       def test_no_undeclared_tolerance_reaches_a_comparison(path):
           bad = offending(path)
           assert not bad
judge A FALSE PASS IS A FILE THE SCANNER MISSES. `offending()` returns [] for
      exactly those files, and the assertion is satisfied. The named test cannot
      go red on a miss under any circumstance -- it is the assumption the miss
      list exists to qualify, not a check on it. Every one of the eleven entries
      in KNOWN_MISSES is a shape this test is green on today.
code :219-221  the assertion that replaces the ratio:
       speciesless = [k for k, v in KNOWN_MISSES.items() if not v.strip()]
judge AND THAT ONE CANNOT FAIL EITHER without somebody typing an empty string on
      purpose. Eleven non-empty literals; nothing generates a value.
judge THE RULING, SINCE I WAS ASKED FOR IT, IN TWO PARTS.
      (1) WITHDRAWING THE RATIO IS CORRECT AND I DO NOT ASK FOR IT BACK. The
      denominator was len(ENTRIES), a corpus I write, so growing it LOOSENED the
      rule and only entries the scanner missed tightened it: a threshold that
      moves with an outside party effort is not a bound on the guard. That is
      "a ratio carries its operating point", and the operating point was mine.
      The seven correct files reddened by the broad fix are the measured cost of
      obeying it, and rejecting that fix was right.
      (2) THE REPLACEMENT IS NOT A RELAXATION -- IT IS AN ABSENCE, described as a
      presence. Nothing now bounds the miss list at all, in either direction, and
      the sentence saying otherwise is refuted by four lines of the file it
      names. Say that plainly and the position is defensible: the miss list is
      unbounded on purpose, each miss carries its species, and the bound is 4a to
      set. Say it as written and a reader believes a check exists.
```

**Closed when** `:215-218` states what is and is not asserted, or a check that can
observe a false pass is named and runs.

**R275. (BLOCKS -- head 2, a tolerance basis) The CI measurement that R244's Q8 value is
to be written from does not reproduce. Four runs, two outcomes, deciding files
untouched.** `tests/test_counters_are_injected.py` [exempt-response drift].

```
cmd  gh run view <id> --log-failed, guards job, four consecutive runs
out  4a8d2a3  34387814070  62 failed / 297 passed  -- drift PASSED
     37799aa  34388632233  30 failed / 329 passed  -- drift FAILED x2
     fa3b070  34408014924   4 failed / 386 passed  -- drift FAILED x2
     a59521e  34424766023   1 failed / 425 passed  -- drift PASSED
cmd  git diff --stat 4a8d2a3..a59521e -- tests/regression floatfea/tolerances.py
     tests/test_counters_are_injected.py
out  (empty)
judge THE OUTCOME CHANGED TWICE ACROSS FOUR RUNS WITH NOTHING THAT DECIDES IT
      CHANGED. I do not attach a cause: the runner CPU and BLAS, the thread
      count, and collection order are all candidates and I have discriminated
      none of them. What is measured is the instability itself.
judge AND IT IS MY OWN FIGURE THAT THIS RETRACTS. Verdict 30 recorded
      "EXEMPT_RESPONSE_DRIFT_ULP = 4.0 ... measured at 2.6e9 ULP on the runner"
      and routed the value to Q8 on that basis. 2.6e9 was printed by run
      34408014924 and the same assertion printed nothing at all one run later. A
      number present in half the runs at commits that cannot differ is not yet a
      measurement of the runner, and Q8 exists precisely to make the runner
      canonical.
judge THIS IS WHY IT BLOCKS RATHER THAN BEING RECORDED. The next act of Q8 is to
      write a tolerance from this number. Under `CLAUDE.md` sec. Tolerances the
      justification has to name the numerical reason, and "2.6e9 ULP on the
      runner" is not yet a fact about the runner.
```

**Closed when** the drift assertion outcome is reproduced -- the same commit run twice
on CI, both times the same way -- and the variable that moves it is named, before any
Q8 value is written for `EXEMPT_RESPONSE_DRIFT_ULP`.

**R276. (recordable, 4a) The DIAGNOSIS entry for `shallow_clone_depth_1` is
unreachable.** `tests/test_report_guard_states.py:132-135` against `:350-355`. The state
is in `REQUIREMENT_CHANGED`, so `test_the_guard_survives_the_state` returns at `:354`
before the DIAGNOSIS block at `:370`. Measured: with the return-code branch ablated,
that state PASSED while the new one failed. The map presents four ablation-asserted
states and three are.

**R277. (recordable, 4a) The CE1 guard catches an absent CI record and not a false
one.** `tests/test_report_carried.py:436-465`. New corpus file
`tests/corpus/report_ci_section.txt`, 4 entries, 1 agrees. Measured at `a59521e` in a
scratch clone: the guards and ladder-4 rows rewritten green, contradicting run
34408014924 on both -> 2 passed; the run id deleted -> 2 passed; the job table replaced
by three rows of an unrelated table -> 2 passed. The docstring at `:437-439` says the
shape is "taken from `gh run view` at the commit the report is written on"; nothing
reads a sha, a run id, or a job name.

**R278. (recordable, 4a) Three more reach holes in the interpreter guard, plus an
instrument that cannot report its own failure.** `tests/test_the_pinned_interpreter.py`.
Measured, corpus file `tests/corpus/pinned_interpreter.txt`, 9 entries, 4 agree: a tenth
CI job with no `setup-python` step at all -> 2 passed; a `python-version` supplied by a
matrix expression -> 2 passed; `[tool.mypy] python_version` set to 3.9 against a
`requires-python` of 3.11 -> 2 passed, a third site naming a version that nothing
reconciles. And `_mypy_errors` never reads the subprocess return code: called with a
version mypy refuses outright it returns an empty set, so "mypy did not run" and "the
tree is clean" are the same value.

**R279. (recordable, 4a) A conftest with `collect_ignore` removes a test from a rung
silently.** Measured at `a59521e`: rung 1 declared `full`, holding a FAILING
`test_a.py` and a passing `test_b.py`, with `collect_ignore` naming the first -> exit 0,
`1 passed`, `run_rung: OK`. Corpus entry
ci_rung_full_conftest_collect_ignore_silently_drops_a_test_file.

**R280. (recordable, 4a) SPECIAL_ARGS is still not linked to `ci.yml`, and the rung-6
corpus entry now measures arguments its own `layout=` field says it does not.**
`tests/test_ci_ladder_gating.py:255-263`. The R256 closing condition asked for the
rung-6 arguments to match `ci.yml`, and they do -- by two literals agreeing, not by
construction. The entry ci_rung6_job_as_shipped_leaves_its_own_rung_undeclared states
its layout as the arguments `ci.yml` actually carried at `fa3b070`, namely
`full:tests/regression` alone, and SPECIAL_ARGS now runs the restored pair. The entry
passes because `ci.yml` was fixed, which is the right outcome reached through a field
that is now false about what runs.

**R281. (recordable, 4a) Nothing requires a corpus file to have a runner.**
`tests/corpus/` holds seven files; three are read by a test. A corpus with no runner
reports no coverage and no absence of coverage, and two of the three files added in the
last two rounds are in that state. `test_the_corpus_and_the_states_agree` and
`test_the_corpus_and_the_layouts_agree` are the right shape and exist per-harness; there
is no check that every file in the directory reaches one.

## Tolerances touched

**None by this diff.**

```
cmd  git diff 1b93db0..a59521e -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 1b93db0..a59521e -- tests/regression docs/milestones/F2_figures.md
out  (empty) -- no golden file and no figure moved.
cmd  git diff --stat 1b93db0..a59521e -- floatfea
out  floatfea/determinism.py | 16 +++++++++---
     the ONLY change: a return type of `object` becomes NDArray[np.float64],
     with numpy still deferred behind TYPE_CHECKING. Runtime identical: the
     expression is bound to a local and returned.
```

**AND THAT IS AGAIN THE STRONGEST THING IN THE RANGE.** `EXEMPT_RESPONSE_DRIFT_ULP = 4.0`
had a red CI, a locked Q&A and an obvious one-character fix in front of it for a seventh
round and was not touched. `F2_figures.md` has four rows that do not reproduce on the
runner and was not regenerated. Both are recorded as deliberate. Nothing was widened.

**What IS a tolerance finding this round is R275**, and it is not a value: the CI
measurement Q8 will write `EXEMPT_RESPONSE_DRIFT_ULP` from flipped twice across four
runs at commits where nothing that decides it changed -- and the figure verdict 30
published, 2.6e9 ULP, came from one of the two runs that produced it.

**R274 is the second**, under the extension in `CLAUDE.md` sec. Tolerances to "anything
that functions as a tolerance under another name": the quantitative bound on the
tolerance scanner's known-miss list was removed, correctly, and the sentence describing
what replaced it names a test that cannot fail on a miss.

**My own instructions (item 4b).**

```
cmd  git diff 1b93db0..a59521e -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" 1b93db0..a59521e with per-commit file lists
out  839b56b  ci.yml, pyproject.toml, run_rung.sh, floatfea/determinism.py,
              six tests/, tests/verification/rung6/.empty-by-design -- no
              docs/reviews/, no .claude/
     a59521e  docs/reports/F2/step-5.md -- the same
judge No commit touches both code and docs/reviews/. No commit touches .claude/
      or docs/SUPERVISOR.md at all, so the STOP-class condition is not in play.
      CLEAN.
```

**What held**, reproduced at my run rather than read: 1722 passed / 0 failed / 0
skipped, matching the report exactly; the guards job at 1 failed / 425 passed with the
`onexc` state gone from CI; the CE2 ablation, which reddens the new state and names its
cause; `onerror=` fitting both signatures; value-keying with one marker per threshold,
both files clean and the node-keying hole re-flagged; rung 6 declared again with its
arguments matching; xfail_strict reddening the strict XPASS; the junit read defeating
the atexit forgery (R263); `step-06.md` no longer read as step 6 (R265); the
contradiction domain widened to every finding the verdict names; the synonym clause of
the vocabulary; the report carrying CI per job with its run id at all; and
`floatfea/tolerances.py` untouched for a seventh round. **These did not**: the Carried
table numbering (R267), the interpreter guard where the pin is honoured (R268), R255
(R269), R258 (R270), R259 (R271), the R260 condition (R272), the second clause of R254
(R273), the replacement for the withdrawn ratio (R274), and the reproducibility of the
runner measurement Q8 depends on (R275).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Nine blocking items. R267 is first,
because until the dependency list points at the right dependencies none of the others
can be tracked -- three of them are currently recorded in the report as belonging to a
different milestone step.

1. **R267 -- the Carried table.** Every row names the finding verdict 30 gives that
   number. No item verdict 30 headed `(BLOCKS ...)` carries a `4a` status. If an item
   genuinely belongs at 4a, the argument goes in the report and the verdict rules on it;
   the report does not route it.
2. **R268 -- the interpreter guard where the pin is honoured.** A run at
   `pinned == running` that reddens on the `onexc` call, or the docstring reach
   paragraph and report section 1 saying it cannot, in the same commit. This is the one
   I most want answered on its merits rather than by editing the sentence: CE0 is a good
   mechanism aimed at the right defect and it is switched off on the only machine
   neither of us controls.
3. **R275 -- before any Q8 value is written.** Two CI runs at one commit, the same
   outcome both times, and the variable that moves the drift assertion named. The 2.6e9
   figure from verdict 30 is withdrawn as a basis until then; it is mine and I withdraw
   it.
4. **R269, R270, R273 -- three sentences, each in the same commit as what it
   describes:** the "What is flagged" list and its five site rows; the 121 and the
   by-file breakdown, regenerated or withdrawn where they stand; the "is not a commit in
   this repository" message.
5. **R271 -- the vocabulary, and the choice is yours.** Refuse the three remaining
   formattings, or withdraw both the docstring sentence and the report section 3 claim
   in the same commit. Either way `tests/corpus/report_status_vocabulary.txt` gets a
   runner: as it stands, the file is cited as coverage and induces zero failures.
6. **R272 -- one keyword.** A rung whose summary reads `1 xpassed` exits non-zero.
7. **R274 -- the replacement for the ratio**, stated as what it is.
8. **The last clause of R256** -- the rung-6 restoration stated in the report, not only
   in the commit message. The substance is done and I record that.
9. **R231, R230, R244, R245, R223, R224 -- unchanged and open by instruction.** R244 now
   also carries R275.

**Not gates on step 5, into the next report Carried section:** R276-R281, R262, R264,
R266, the two R248 residues, R249, R250, R251, R252, R225-R228, R232, R233, and
everything already at 4a. R263 and R265 are fixed in the code and I re-ran both.

**Adversarial corpus (BE3): 26 new entries at `ec28446`, across four files, two of them
new, all unseen by the implementer; every `measured` field taken at `a59521e` before the
`expect` or `require` beside it was written.**

**The coverage measurement, stated plainly: of my 26 new entries the shipped checks do
what the entry requires on 9.** With the corpus applied, `tests/test_ci_ladder_gating.py`
gives **5 failed, 34 passed**; the two new files have no runner and induce zero
failures, which is R281.

* `tests/corpus/pinned_interpreter.txt` -- **NEW, 9 entries, 4 correct.** The CE0 guard
  had a corpus of one: the `onexc` call its author had already seen. The entry that
  matters is pin_equals_running_with_a_3_12_only_keyword_present, which is R268.
* `tests/corpus/report_ci_section.txt` -- **NEW, 4 entries, 1 correct.** An absent CI
  record is caught; a false one is not.
* `tests/corpus/report_status_vocabulary.txt` -- **+10 (12 -> 22), 3 correct.** Five more
  spellings of closure, two ways to break the word itself, and one legitimate row that
  must pass. The three rows from last round that are still allowed are re-measured here
  rather than carried across.
* `tests/corpus/ci_ladder_gating.txt` -- **+3 (34 -> 37), 1 correct.** The
  `strict=False` xpass, a `collect_ignore` that drops a test, and a module-level skip
  that is correctly caught.

**Thirty-one consecutive rounds have found no element defect, and this round does not
either.** `git diff 1b93db0..a59521e -- floatfea` is a return annotation. What this
round found is, again, one thing in several places: **a check verified against inputs
its own author designed.** The interpreter guard was written against the one call it had
already seen, and it is inert in the configuration it is aimed at. The CI-table guard
was written against the absence it had just lived through, and cannot see a falsehood.
The vocabulary guard was fixed against two of the four rows it was given. And R275 is
the other species and the harder one: a measurement taken once on a machine nobody
controls, published as a property of that machine, that turns out not to reproduce on
it.

**And the best thing in the range is still that nothing was widened.** Seven rounds of a
red CI, a locked Q&A, and a one-character fix, and `floatfea/tolerances.py` has not
moved. R275 is the vindication of that patience rather than an argument against it: had
the value been written when the figure was first taken, it would have been written from
a run that the next run contradicts.
