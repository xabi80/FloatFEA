# Review — F2 step 5
Reviewed commit: 43e41cb357569e02f209a585b884b8f8f6809c66
Verdict: HOLD

Tests: **1686 passed, 0 failed, 0 skipped** (my run at `fa3b070`, `python -m pytest -q`,
223.39 s, Python 3.13 on Windows). Identical to the report's figure. With my
thirtieth-round corpus applied at `43e41cb`: **21 failed, 99 passed** across the three
harnesses that have a runner; the fourth corpus file has none, which is R259.

**AND THE LOCAL NUMBER IS NOT THE NUMBER THAT DECIDES THIS STEP.**

```
cmd  gh run list --limit 4 --json headSha,databaseId,conclusion
out  34408014924  fa3b070  failure   (push)
     34408020227  fa3b070  failure   (pull_request)
cmd  gh run view 34408014924 --json jobs
out  guards and meta-tests   FAILURE
     lint and type-check     success
     unit tests              success
     ladder 1 / 2 / 3        success
     ladder 4                failure     <- R231
     ladder 5, ladder 6      skipped     <- R230, still never run
cmd  gh run view 34408014924 --log-failed
out  4 failed, 386 passed in 119.26s
     FAILED test_counters_are_injected.py::...[exempt-response drift]      <- R244
     FAILED test_counters_are_injected.py::...[exempt-response drift]      <- R244
     FAILED test_plan_figures.py::test_the_generated_figures_are_not_stale <- R245
     FAILED test_report_guard_states.py::...[shallow_clone_depth_1]
            - TypeError: rmtree() got an unexpected keyword argument 'onexc'
```

**Three of the four are routed. The fourth is new, this commit made it, and it is in
the test that certifies this commit's answer to R243.** That is R253, and it is why CA2
is not a formality: `onexc` is Python 3.12+, `ci.yml` pins 3.11, the implementer runs
3.13, and the state that measures the shallow-clone repair therefore does not execute
on the machine the repair was written for.

`git diff 476f909..HEAD -- .claude docs/SUPERVISOR.md` is empty; `-- floatfea` is empty;
`-- floatfea/tolerances.py` is empty. No commit touches both code and `docs/reviews/`.
The header at `docs/reports/F2/step-5.md:663` reads `Answers: verdict 29 @ 476f909`,
and `476f909` is the fourth and latest step-5 verdict. Item 1b passes.

**PR #1 is open, `F2 -> master`, and `gh pr view 1 --json comments` returns none.**
Step 5 still has no outside-witness comment; recorded as an unavailable check, not as
a pass.

## Carried

Verdict 29 listed eight items under "Next step opens when". **Two close. Three are
answered in mechanism, and one of those does not hold where it matters. Three are open
by instruction.**

- **R242 -- CLOSED.** The false status is retracted by name, and the mechanism meant to
  make it impossible is real, if reachable (R259).

```
cmd  sed -n '788p' docs/reports/F2/step-5.md
out  "| R230 | **open** - REOPENED BY NAME. Revision 3 gave it a status only a
      verdict may give, against that verdict's own words; sec.0 |"
cmd  the report's own headline figure, reproduced at 37799aa by me
out  62 status cells parsed, 10 say closed -- exactly the published number
```

- **R246 -- CLOSED.** `tests/test_report_carried.py:66-85`. The pattern is `[0-9]+`,
  the docstring says what the two branches cover instead of "never raises", and I ran
  the state rather than reading about it.

```
cell a copy of the repository at fa3b070 with a superscript-one step report
     added and nothing else changed
out  123 passed. No collection error; the file is stepped over.
judge THE REPORT PUBLISHES 121, in sec.1 and in the commit message. It is 123 at
      the commit the report is committed at -- the four tests this same commit
      added to that file. That is R258.
cell 20 further filenames against the shipped `_steps`: Arabic-Indic digits,
     `step-5b`, `step-`, `step-6-draft`, `step-6.md.md`, `Step-6`, a trailing
     space, `step-1-2` -- all IGNORED, correctly. `step-01` and `step-0006` map
     onto step 1 and step 6 (R265, 4a).
```

- **R241 -- WITHDRAWN, AND I ACCEPT THE WITHDRAWAL.** The closing condition offered it.
  What I do not accept is the site row: lines `:651`-`:654` are recorded as "R241 quotes
  it as evidence, not as a site to change", and R241's closing condition names those
  exact lines as the site to change **or withdraw**. The withdrawal stands; the row
  describing it is wrong, and that is R266.

- **R243 -- ANSWERED IN MECHANISM, AND THE CERTIFICATE DOES NOT HOLD.** I verified every
  part of the mechanism, then measured what certifies it.

```
cmd  grep -c "fetch-depth: 0" .github/workflows/ci.yml
out  9 -- all nine checkouts, checked one by one against the nine
     `- uses: actions/checkout@v4` lines
cell git clone --depth 1 --no-local at fa3b070, my own clone, not the harness
out  2 failed, 121 passed. Both failures are named tests. Neither is a site
     parametrisation. The diff message names the remedy in its own text.
     Before: 23 failed, 99 passed. The repair is real and I reproduced it.
judge AND NOTHING IN THE REPOSITORY MEASURES IT -- R254 -- and the state does not
      run at all on CI -- R253.
```

- **R247 -- ANSWERED IN MECHANISM.** `tests/test_report_guard_states.py:190-245`. The
  junit reader is right, `collection_failed` and `everything_failed` are two separate
  assertions, and the substring grep with its `or "passed" in log` mirror is gone. Four
  of the six previously-red states are green on CI now. The residue is R254: for a state
  in `REQUIREMENT_CHANGED` the function returns at `:289`, before the named-reporter
  check at `:300-312` runs at all.

- **R240 -- OPEN.** The guards job is red at the reviewed commit. Three of its four
  failures are routed by name; the fourth is routed nowhere (R253). The closing
  condition also asked for "the run id and the count beside it", and revision 4 has no
  CI section at all -- section 3's counts are the reds at `476f909`, which is the
  corpus commit, not this one.

- **R244 -- OPEN by instruction (Q8), and the closing condition is one of three.** I
  asked for the constant, the site, and the fact that its gate is masked by a skipped
  ladder. `docs/milestones/F2.md` names the constant and the `2.6e9` figure. It does not
  name `tests/regression/test_exempt_pair_responses.py:109`, and it does not record that
  `test_every_recorded_pair_is_still_detected` has never run on CI -- which is the part
  that will surprise whoever writes the value.

```
cmd  gh run view 34408014924 --json jobs, the ladder 6 entry
out  conclusion: skipped -- as on every run this branch has produced
```

- **R245 -- OPEN by instruction (Q8).** `docs/milestones/F2_figures.md` untouched,
  correctly. I measured the half of Q8's route that nothing had measured: two separate
  processes rendering the figure file on this machine produce **byte-identical** output,
  2813 bytes each, so same-platform determinism is not what defeats the regeneration
  route. The cross-platform gap is unchanged: CI prints `3.5380e-14`, the committed file
  says `3.6275e-14`.

- **R230 -- OPEN, correctly, and it moved backwards this round.** `tests/regression` has
  still never executed on CI. And `82a4b33` removed rung 6's own declaration from the
  ladder without saying so, which is R256.

- **R231, R223, R224 -- OPEN by instruction.** Site by site, confirmed untouched:
  `floatfea/tolerances.py:293`, `:295-297`, `:300-308`;
  `tests/verification/rung1/test_rigid_body_modes.py:19`, `:175-177`;
  `docs/milestones/F2.md:51`, `:1477`, `:1491-1492`.
  `git diff 476f909..HEAD -- floatfea` is empty.

- **R248 -- HALF ANSWERED, and I re-ran all seven rather than reading about five.**

```
cell shipped scripts/run_rung.sh at fa3b070, scratch trees:
     (a) xfail-only rung whose test FAILS   -> exit 1, named           FIXED
     (b) no arguments                       -> exit 1, named           FIXED
     (c) argument with no kind prefix       -> exit 1, named           FIXED
     (d) capitalised `Empty:`               -> exit 1, named           FIXED
     (e) passing test printing "skipped"    -> exit 0, ran             FIXED
     (f) xfail-only rung whose test PASSES  -> exit 0, "run_rung: OK"  R260
     (g) a line printed AFTER the summary   -> exit 1, false alarm     R263
```

- **R249 -- carried, extended, and two of last round's misses are closed.** Both clauses
  of `CLAUDE.md` sec. Tolerances are caught in the two spellings I wrote, and go clean in
  six neighbours (R262). R237's left operand is read -- and the docstring twelve lines
  above still says it is not (R255).

- **R225-R228, R232, R233, R250, R251, R252** -- carried, unchanged, correctly
  classified in the report's section 6.

## Findings

**R253. (BLOCKS -- CA2) CI is RED at the reviewed commit, and the fourth failure is new,
is this commit's, and sits in the test that certifies this commit's answer to R243.**
`tests/test_report_guard_states.py:185`.

```
code :185  shutil.rmtree(work / ".git", onexc=_force_remove)
cmd  python -c "import inspect, shutil; print(inspect.signature(shutil.rmtree))"
out  (path, ignore_errors=False, onerror=None, *, onexc=None, dir_fd=None)
     -- `onexc` was added in Python 3.12. This machine is 3.13.11.
cmd  grep -n "python-version" .github/workflows/ci.yml
out  "3.11" nine times; the runner log reads
     pythonLocation: /opt/hostedtoolcache/Python/3.11.16/x64
out  CI, guards job, fa3b070, run 34408014924:
     FAILED ...[shallow_clone_depth_1] - TypeError: rmtree() got an unexpected
     keyword argument 'onexc'
judge THE HANDLER EXISTS FOR WINDOWS READ-ONLY PACK FILES and its comment says
      so. On Linux it is not needed and the keyword is fatal, so the ONE state
      that measures R243's repair is the one state that cannot run where R243
      was found. A try/except around the keyword, or `ignore_errors` plus a
      chmod walk, closes it.
judge AND THE REPORT IS SILENT ABOUT CI. Revision 3 carried a section 8;
      revision 4 carries none, and R240's closing condition asked for the run id
      and the counts.
```

**Closed when** the guards job is green at the reviewed commit, or every failure in it
is routed by name with the run id and the counts in the report -- and
`shallow_clone_depth_1` executes on the pinned interpreter instead of erroring in the
harness before the guard is ever run.

**R254. (BLOCKS -- the gate's own claim) The assertion that certifies R243 passes
whether or not R243 was fixed. Ablation: one machine, one commit, one variable.**
`tests/test_report_guard_states.py:276-289` and `:300-312`.

```
cell a `git clone --depth 1 --no-local` of the repository at fa3b070. The only
     thing varied is the return-code branch in `_changed_lines`, removed, and
     nothing else:
       shipped   2 failed, 121 passed   exit 1
       ablated  16 failed, 107 passed   exit 1
     `assert code != 0` at :285 is satisfied by both.
code :276-289  a state in REQUIREMENT_CHANGED asserts the direction and returns.
               The named-reporter check at :300-312 never runs for it.
judge AND FALLING THROUGH WOULD NOT CLOSE IT EITHER. The `named` tuple at
      :300-307 CONTAINS `test_every_named_site_is_touched_or_declared`, which is
      exactly what the sixteen ablated failures are. The check would pass on the
      broken guard too.
judge THIS IS THE WHOLE CONTENT OF R243 AND OF THE COMMIT MESSAGE: "the site
      tests defer to that one test so a single diagnosis does not become ninety
      identical failures". The deferral is real in the code at
      test_report_carried.py:479-484 -- I read it and I ran it. NOTHING ASSERTS
      IT. The file's own vocabulary says `named_fail` means "a NAMED test
      carries the message, with the rest of the file still collected and run",
      and the assertion checks the first word of that and nothing else.
judge SECOND SITE, SAME STATE, NOT FIXED AND NOT DECLARED. R243 named
      test_report_carried.py:186 as well as :282. At fa3b070 the message at
      :196-198 still reads "the report answers verdict `f354025`, which is not a
      commit in this repository". It is a commit; the clone does not have it.
      One of the two failures I measured above IS that sentence. The carry guard
      cannot see the site because the verdict wrote it as a bare `:186` and
      `_SITE` needs a filename -- a parser hole, not a defence.
```

**Closed when** the shallow-clone state distinguishes one named diagnosis from sixteen
site failures -- `tests/corpus/report_guard_states.txt` carries the requirement as
`forbid=` on `shallow_clone_depth_1_reports_one_diagnosis_not_sixteen` -- shown by
running the ablation rather than asserting it; and `:196-198` says what it means.

**R255. (BLOCKS -- head 3) The scanner's own "What is flagged" list states the opposite
of what the scanner does, twelve lines above the code this commit changed.**
`tests/test_no_tolerance_literals.py:29-33` against `:219`.

```
code :29-33  "**The left operand is not read** (R237): ``assert 0.05 > ratio``
             returns nothing ... Widening it to ``node.left`` is a change to the
             guard's reach and belongs to step 4a"
code :219    for comp in [node.left, *node.comparators]:
cell the shipped `offending()` on a file whose only content is
     `def test_x():` / `    assert 0.05 > r`
out  [(2, 'comparison against 0.05')]
judge R237 WAS CLOSED ONE ROUND AGO BY FIXING THIS SENTENCE TO MATCH THE CODE.
      This commit moved the code and left the sentence, so the same file carries
      the same species of falsehood pointing the other way. BP0 is the rule and
      the fix is one paragraph.
```

**Closed when** `:27-33` describes what `:218-254` does, or the code stops doing it.

**R256. (BLOCKS -- head 3) Rung 6's declaration was deleted from the ladder and from
the repository, and neither the commit message nor the report mentions it.**
`.github/workflows/ci.yml:235`; `tests/verification/rung6/.empty-by-design`, deleted.

```
cmd  git show 82a4b33 --stat -- tests/verification/rung6
out  tests/verification/rung6/.empty-by-design | 3 ---
cmd  git show 82a4b33 -- .github/workflows/ci.yml | grep "^[-+].*run_rung"
out  -  sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
     +  sh scripts/run_rung.sh full:tests/regression
cmd  git ls-files tests/verification/rung6
out  tests/verification/rung6/__init__.py -- still tracked, and now named by NO
     job in the workflow.
cmd  grep -rn "rung 6" tests/test_ci_ladder_gating.py .github/workflows/ci.yml
out  test_ci_ladder_gating.py:11-13  "ci_rung6_live, which is not a hypothesis
       but this repository as it stood: rung 6's own directory is empty by design"
     test_ci_ladder_gating.py:53-57  "Rung 6's own directory is declared
       `empty:`, so a test appearing in it now FAILS as a stale declaration
       rather than being run silently"      <- FALSE at fa3b070
     ci.yml:95-101  "the rung is declared `empty:` here and carries a
       `.empty-by-design` marker"           <- FALSE for rung 6 at fa3b070
     run_rung.sh:5  the usage line still shows the rung-6 invocation that is no
       longer shipped
code test_ci_ladder_gating.py:231-234 and :260 -- ARGS["rung6"] is still
     ["empty:tests/verification/rung6", "full:tests/regression"], and every
     `ci_rung6*` entry, six of them, is run against it. Nothing links ARGS to
     the workflow, so six corpus entries measure a job body that is not shipped,
     under a docstring at :303 that calls it "The shipped step body".
cell the SHIPPED rung-6 arguments against a tree where
     tests/verification/rung6 holds a passing test:
       sh run_rung.sh full:tests/regression  -> exit 0, "run_rung: OK"
     The populated rung is named by nothing and no declaration contradicts it.
judge I RECORD WHAT DOES STILL CATCH IT, because it matters:
      test_ci_runs_the_whole_suite.py would redden at the commit that adds a
      test there, and I verified that mechanism at R250 last round. What is gone
      is the ladder's own declaration -- the thing the marker file existed for,
      in its own words: "so a rung whose tests go missing is distinguishable
      from one nobody has written".
judge AND THE CHANGE IS NOWHERE IN THE COMMIT MESSAGE OR THE REPORT. A ladder
      declaration is exactly what this arrangement exists to make loud.
```

**Closed when** rung 6's directory is declared again, or it is deleted and every
sentence above is corrected in the same commit (BP0), with `ARGS["rung6"]` matching
`ci.yml` -- and either way the change is stated in the report.

**R257. (BLOCKS -- head 2, "never widen") The exemption window was loosened tree-wide,
in the same commit as the detection fix that would otherwise have reddened two files,
and the third option was neither offered nor measured.**
`tests/test_no_tolerance_literals.py:154-160` and `:264-277`.

```
code :155-159  "KEYED ON THE NODE, not on the value (CD2)" -- once a marker
               claims any candidate for a node, `claimed[node_id] = True` and
               every other candidate on that node is skipped.
judge THE TWO LIVE SITES WERE NOT RED BEFORE THIS COMMIT. `node.left` was not
      read, so `0.34 < r/0.9 < 0.3536` produced ONE candidate and one marker
      covered it. Reading `node.left` makes it two. The exemption rule was
      changed in the same commit as the change that would have reddened them,
      which is the shape CLAUDE.md sec. Tolerances forbids for a value and
      extends to "anything that functions as a tolerance under another name".
cell the two options, value-keyed against node-keyed, over every file in tests/
out  exactly two files disagree, and they are the two named:
       rung3/test_basis_constants.py:192        0.34 < r / 0.9 < 0.3536
       rung4/test_reference_provenance.py:30    0.3 < f < 0.7
     Both are genuine brackets and both markers are correct. The report's
     measurement is exact and I reproduced it.
cell THE THIRD OPTION, not offered: value-keyed exemption PLUS one extra
     `# not-a-tolerance:` comment inside each of those two statements, naming
     the lower bound of the same bracket.
out  offending() returns [] for both files. Cost: two comment lines.
cell what node-keying lets through, shipped scanner, measured:
out  `assert 1e-09 < r < 0.05  # not-a-tolerance: only the LOWER bound is
      deliberate`                                             -> clean
     `assert_allclose(a, b, rtol=2e-08, atol=1e-12)
      # not-a-tolerance: rtol only`                            -> clean
judge THIS IS CB0's HOLE ONE LEVEL DOWN, and CB0's own comment at :255-260 says
      so: "the statement window let a single marker cover every flaggable node
      in its span, so a two-clause assert needed one marker for two literals".
      A two-threshold comparison now needs one marker for two literals.
judge THE RULING, SINCE I WAS ASKED FOR IT. Between the two options offered,
      node-keying is the better one and the reasoning for it is sound. The
      ruling is that the option set was wrong: the third option keeps the rule
      at one marker per threshold, costs two comments in two files, and was not
      measured before the rule moved.
```

**Closed when** the exemption is keyed so that one marker covers one threshold, with
the two bracket statements carrying their second marker -- or the loosening carries a
written justification in `docs/milestones/F2.md` or the closure artifact naming why one
marker may cover two undeclared literals, per `CLAUDE.md` sec. Tolerances.

**R258. (BLOCKS -- head 3) Two published figures in revision 4 do not reproduce at the
commit that publishes them.** `docs/reports/F2/step-5.md:713` and `:745-746`.

```
code :713  "after:  `121 passed` -- the file is stepped over"
cell a copy of the repository at fa3b070, superscript-digit report file added
out  123 passed. The four tests this same commit adds to that file are the two.
     121 is a figure from a working state, carried across a change that moved
     the measure underneath it -- the sentence in CLAUDE.md sec. Step gating,
     verbatim.
code :745-746  "cmd  the reds at 476f909, by file
                out  12 marker shapes, 10 guard states, 9 ladder layouts, 1 site
                     declaration"
cmd  a clone at 476f909, `pytest tests --ignore=tests/unit
     --ignore=tests/verification --ignore=tests/regression -q`, by file
out  9  tests/test_ci_ladder_gating.py
     12 tests/test_marker_exemption_corpus.py
     13 tests/test_report_guard_states.py
     34 failed, 363 passed
judge THE TOTAL IS RIGHT AND THE BREAKDOWN IS NOT: 13 guard states, not 10, and
      there is no "site declaration" red -- test_report_carried.py was green at
      that commit. The `cmd` field is also a description rather than a command,
      which is what BF0 asks that field to be.
judge NEITHER FIGURE CHANGES A CONCLUSION. Both sit in a report a reader is
      asked to trust, and both are refuted by one command, which is the whole of
      head 3.
```

**Closed when** both figures are regenerated at the report's own commit, or withdrawn.

**R259. (BLOCKS -- head 3) "The word is gone" is not what the guard does. Four
formattings carry `closed` past both halves of CC1, measured end to end against the
shipped tests.** `tests/test_report_carried.py:288`, `:293`, `:296-322`.

```
code report sec.0  "Taking the strongest word away from the party that does not
     get to use it removes the failure mode instead of detecting it."
code :288  _ROW anchors on `^\|\s*(R\d+...)` -- the first cell must start with R
code :293  status = rest.rsplit("|", 1)[-1] -- the LAST column is the status
cell each row appended to the newest revision's Carried table in a copy of the
     repository at fa3b070, then
     `pytest tests/test_report_carried.py -k "CLOSED or report_words"`:
out  | R230 | **closed** at the third verdict |          -> 2 FAILED   caught
     | **R230** | **closed** at the third verdict |      -> 2 passed   MISSED
     | `R230` | **closed** at the third verdict |        -> 2 passed   MISSED
     | R230 | **closed** ... | still open |              -> 2 passed   MISSED
     | R230 | **resolved**, nothing open |               -> 2 passed   MISSED
judge FOUR OF FIVE. Three are not parsed as rows at all, so the SECOND half --
      the one that exists so "banning a word cannot become saying nothing" --
      does not see them either. The fourth reads the last column. And the row
      that made the rule is one keystroke from the first miss: the report's own
      adjacent table, "Sites named by findings and not touched", backticks every
      first cell, seventy times.
cell THE THIRD CHECK'S DOMAIN, measured over verdict 29 rather than reasoned:
out  test_no_status_claims_more_than_the_verdict_allows builds `carried_open`
     from the phrases "not closed" / "still carried" / "still open". Over
     verdict 29 that set is exactly {R230, R234, R242} of 21 findings. Every
     "(BLOCKS ...)" heading is outside it -- including R241, which is the ONE
     item revision 4 reports as `withdrawn`. The check cannot see the only
     withdrawal in the report it guards.
judge AND THE COVERAGE CLAIM RESTS ON ITS AUTHOR'S OWN ROWS (BE3). There was no
      corpus for this check. There is now:
      tests/corpus/report_status_vocabulary.txt, 12 rows, 4 of which the
      shipped guard gets right.
```

**Closed when** the four rows above are refused, and the contradiction check's domain
is the verdict's findings rather than three phrases -- with the corpus file given a
runner, so the next four formattings are measured rather than argued.

**R260. (BLOCKS -- head 3, and it is the ladder's own gate) The `*xpassed*` arm added
by this commit cannot fire on the shape it names.** `scripts/run_rung.sh:138-146`.

```
code :138-139  summary is built by grep -E '[0-9]+ (passed|failed|skipped|
               xfailed)' | tail -1
code :141      case "$summary" in *skipped*|*xfailed*|*xpassed*)
cell shipped script, scratch trees, one variable moved:
out  rung1 full, only test is @pytest.mark.xfail and its body FAILS
       -> "1 xfailed in 0.2s"       exit 1, named           caught
     rung1 full, only test is @pytest.mark.xfail and its body PASSES
       -> "1 xpassed in 0.22s"      exit 0, "run_rung: OK -- 1 director(y|ies)
                                    ran"                    MISSED
     the same rung plus one plain passing test
       -> "1 xpassed, 1 passed"     exit 1, named           caught
judge `xpassed` IS IN THE CASE ARM AND NOT IN THE ALTERNATION THAT BUILDS THE
      LINE, so `$summary` is empty and the arm is dead for the minimal shape.
      Detection depends on whether an unrelated test happens to share the
      summary line, which is not a property of the rung.
judge THE COMMENT DIRECTLY ABOVE IT IS WHAT MAKES THIS HEAD 3: "pytest exits 0
      for a run that did either to everything -- so without this the ladder
      reports green on a rung that asserted nothing." With this, it still does.
      The commit message counts the xfail defect among five and says "All five
      fixed". One word in the alternation closes it.
```

**Closed when** `run_rung.sh` reddens on `1 xpassed` alone, shown as a run.
`tests/corpus/ci_ladder_gating.txt` carries it as
`ci_rung_full_every_test_is_xfail_and_PASSES`.

**R261. (recordable, and it is a condition on the Q8 measurements rather than on this
diff) The canonical environment Q8 defines does not exist, and the sequence does not
create it before the values are measured.** `docs/milestones/F2.md`, Q8.

```
code plan  "**CI is canonical** -- Linux, with Python, `numpy` and `scipy`
           pinned in a lockfile"
cmd  ls *.lock requirements*.txt constraints*.txt poetry.lock uv.lock
out  (none)
cmd  grep -n "numpy\|scipy" pyproject.toml
out  "numpy>=1.26", "scipy>=1.11" -- floors, not pins
cmd  grep -n "python-version" .github/workflows/ci.yml
out  "3.11" nine times; the runner resolved it to 3.11.16 on this run
judge A VALUE MEASURED ON AN UNPINNED RUNNER IS ONE RUNNER IMAGE'S NUMBER, which
      is the same defect as one laptop's number on a different machine. The
      plan's own argument -- "A number that can only be produced in one place
      cannot drift between places" -- needs the place to be fixed, and the
      sequence at the end of Q8 does not put the lockfile anywhere in it.
judge THE OTHER CLAUSE I COULD NOT LOCATE: "the thirteen CI-versus-local pairs
      already measured, every one of which is 0.5 or 1.0 ULP of its channel's
      amplitude" is the stated basis for the number 2. The assertion that
      produced those thirteen prints an ABSOLUTE max-diff --
      tests/verification/rung4/test_writer_round_trip.py:100, "max |diff| =
      1.110e-16" on the runner -- not ULP of amplitude, and only for the
      channels that failed. The translation is not in the repository.
judge WHAT I DO NOT FIND WRONG, said plainly: the diagnosis, the choice of CI,
      the per-class split, the stamp-inside-the-file mechanism and the
      regenerate-and-compare route are all right, and the form of the local rule
      -- ULP of the channel's own amplitude -- is dimensionless and survives a
      unit scaling, which an absolute epsilon would not. Amplitude rather than
      value is the correct normaliser for a channel that crosses zero, and a
      sine does.
cell the half of the route nobody had measured: two separate processes
     rendering F2_figures.md on this machine
out  byte-identical, 2813 bytes each. Same-platform determinism holds, so
     "regenerate on the runner and assert byte-identity" is not defeated before
     it starts.
```

**Closed when** the lockfile lands and the thirteen pairs are published in the quantity
the tolerance is stated in -- both before any Q8 value is written, not after.

**R262. (recordable, 4a) The scanner misses 8 of 10 new shapes, and six of the eight
are the two clauses of `CLAUDE.md` sec. Tolerances in other spellings.** Measured at
`fa3b070` against the shipped `offending()`; the ten are at
`tests/corpus/tolerance_marker_exemptions.txt`.

```
out  clean  TOL: float = 1e-09         <- ast.AnnAssign; only ast.Assign is
                                          read, and this is the form CLAUDE.md
                                          sec. Style prescribes
     clean  a function-local tol = 1e-09   <- only tree.body is scanned
     clean  def check(r, *, tol=1e-09)     <- kwonlyargs / kw_defaults not read
     clean  lambda r, tol=1e-09: ...       <- ast.Lambda not in the isinstance
                                              tuple
     clean  FLOOR = -1e-09                 <- UnaryOp, so not in local_floats
     clean  TOL = 1e-09 * 2                <- the value is not an ast.Constant
     caught a marker written in a MESSAGE STRING rather than a comment
     caught TOL = 1e-09 then TOL = 3   (the message names 1e-09; the value is 3)
judge Detection reach, which BU0 routes to 4a and where R237 and R249 already
      sent it. I am consistent and I do not block on it. I record it because the
      commit's own claim is that "a guard that misses the rule it quotes is a
      hole in the claim" -- and the rule it quotes has more than two spellings.
```

**Closed when** 4a rules on the candidate set.

**R263. (recordable, 4a) The skip alarm's `tail -1` heuristic reinstates the false alarm
for anything printed after pytest's summary.** `scripts/run_rung.sh:138-139`. Measured:
a rung whose only test PASSES, in a module registering an `atexit` hook that prints
`1 skipped in 0.01s`, gives exit 1 and a false skip alarm. Corpus entry
`ci_rung_full_prints_a_counter_line_AFTER_pytests_summary`.

**R264. (recordable, 4a) `tests/test_ci_ladder_gating.py:326` asserts a phrase the
script never prints, and nothing reaches it.** The only `require=pass` entry is in
`REQUIREMENT_CHANGED` and returns at `:314`, so `assert "empty by design" in log` is
unreachable, and `grep -rn "empty by design" scripts/` is empty. Measured: the live
rung-2 and rung-5 shape -- `empty:` with its marker and nothing in it -- gives exit 0
and `run_rung: OK -- 0 director(y|ies) ran`, with the phrase absent. Corpus entry
`ci_rung_declared_empty_with_its_marker_and_nothing_in_it` reaches it.

**R265. (recordable, 4a) `_steps` is not injective on the filenames it admits.**
`tests/test_report_carried.py:85`. `step-01.md` maps to 1 and `step-0006.md` to 6.
Measured at `fa3b070`: `step-06.md` alone gives `1 failed, 122 passed`, naming a step
whose file does not exist; `step-06.md` and `step-6.md` together, with a step-6 verdict,
give **123 passed, green**, with one of the two report files invisible. Corpus entries
`zero_padded_step_number` and `zero_padded_step_number_beside_the_unpadded_one`.

**R266. (recordable, 4a) The site table calls four lines "evidence, not a site to
change" when the finding's closing condition named them as the site.**
`docs/reports/F2/step-5.md:820-823` against verdict 29's R241: "Closed when `:651-655`
states the guards job's result ... **or is withdrawn**". The withdrawal is recorded and
I accept it; the row describing the site is wrong. `test_report_carried.py` cannot catch
it -- a `no change` declaration is accepted for any named site.

## Tolerances touched

**None by this diff.**

```
cmd  git diff 476f909..HEAD -- floatfea/tolerances.py
out  (empty)
cmd  git diff --stat 476f909..HEAD -- floatfea
out  (empty) -- floatfea/ is UNTOUCHED across this entire range, as it has been
     for six consecutive rounds.
cmd  git diff 476f909..HEAD -- tests/regression/ docs/milestones/F2_figures.md
out  (empty) -- no golden file and no figure moved.
```

**AND THAT IS THE STRONGEST THING IN THIS RANGE, so I say it before the findings are
read.** `EXEMPT_RESPONSE_DRIFT_ULP = 4.0` was measured at `2.6e9` ULP on the runner and
was not raised. `F2_figures.md` has four rows that do not reproduce there and was not
regenerated. Both are recorded as deliberate, site by site, at
`docs/reports/F2/step-5.md:826-871`. Under a red CI, with a locked Q&A in hand and an
obvious one-character fix available, nothing was widened. That is the rule working, and
it is why this is a HOLD on apparatus rather than a STOP on the plan.

**What IS a tolerance finding this round is R257**, and it is about a decision rule
rather than a number: the exemption window of the guard that keeps every tolerance in
`floatfea/tolerances.py` was loosened tree-wide, in the same commit as the detection fix
that would otherwise have reddened two files. `CLAUDE.md` sec. Tolerances extends the
never-widen rule to "anything that functions as a tolerance under another name", and an
exemption window is one. The alternative is measured at two comment lines.

**My own instructions (item 4b).**

```
cmd  git diff 476f909..HEAD -- .claude docs/SUPERVISOR.md
out  (empty). Not one byte.
cmd  git log --format="%h %s" 476f909..HEAD with per-commit file lists
out  5697b2a  docs/milestones/F2.md                       -- plan only
     82a4b33  ci.yml, run_rung.sh, test_ci_ladder_gating.py,
              test_marker_exemption_corpus.py, test_no_tolerance_literals.py,
              test_report_carried.py, test_report_guard_states.py,
              tests/verification/rung6/.empty-by-design   -- no docs/reviews/
     fa3b070  docs/reports/F2/step-5.md                   -- no docs/reviews/
judge No commit touches both code and docs/reviews/. No commit touches .claude/
      or docs/SUPERVISOR.md at all, so the STOP-class condition is not in play.
      CLEAN. The plan edit is a standalone `plan:` commit, which is the right
      shape for a re-lock.
```

**What held**, reproduced at my run rather than read: `1686 passed, 0 failed, 0
skipped`, matching the report exactly; `fetch-depth: 0` on all nine checkouts; the
return code read and reported through a named test, with 23 false accusations down to 2
in a real `--depth 1` clone; `[0-9]+` against twenty filenames; the junit reader and its
two separated assertions; five of the seven `run_rung.sh` defects, each re-run; both
clauses of `CLAUDE.md` sec. Tolerances caught in the spellings I wrote; `node.left`
read; the four requirement disagreements carrying their direction explicitly, including
the one this commit found in its own map; R230 reopened by name; `62 status cells, 10
say closed` reproducing exactly at `37799aa`; and `floatfea/` untouched for a sixth
round. **These did not**: CI at the reviewed commit (R253), the certificate on the
shallow clone (R254), the scanner's own docstring (R255), rung 6's declaration (R256),
the exemption window (R257), two published figures (R258), CC1's reach (R259), and the
`xpassed` arm (R260).

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.** Eight blocking items. R253 is first,
because it is the machine neither of us controls saying that the answer to R243 has
never run where R243 was found.

1. **R253 -- the guards job at the reviewed commit.** Green, or every failure routed by
   name with the run id and the counts in the report; and `shallow_clone_depth_1`
   running on Python 3.11 rather than raising `TypeError` inside the harness. Three of
   the four are already routed and I record that; the fourth is this commit's own.
2. **R254 -- the shallow-clone certificate.** Shown by running the ablation: with the
   return-code branch removed, the state must go red. Do not close it by asserting the
   count -- `assert code != 0` is what the finding is about. And `:196-198` stops saying
   a commit is not a commit.
3. **R256 -- rung 6's declaration**, restored, or removed with every sentence corrected
   in the same commit, `ARGS["rung6"]` matching `ci.yml`, and the change stated in the
   report. A ladder declaration is not a silent edit.
4. **R257 -- the exemption window.** One marker, one threshold, with the two bracket
   statements carrying their second marker; or a written justification in the plan or
   the closure artifact for why one marker may cover two undeclared literals.
5. **R255, R258, R260 -- three sentences and one word**, each in the same commit as what
   it describes: the "What is flagged" list; the `121` and the by-file breakdown;
   `xpassed` in the alternation.
6. **R259 -- CC1's reach.** The four formattings refused, the contradiction domain taken
   from the verdict's findings rather than three phrases, and
   `tests/corpus/report_status_vocabulary.txt` given a runner. If the answer is that the
   reach belongs to 4a, say so -- but then the sentence "removes the failure mode
   instead of detecting it" is withdrawn in the same commit, because it is the claim the
   reach was supposed to support.
7. **R261 -- before any Q8 value is written**, not after: the lockfile, and the thirteen
   pairs published in the quantity the tolerance is stated in.
8. **R231, R230, R244, R245, R223, R224 -- unchanged and open by instruction.** R244's
   closing condition is one of three; the site and the masked ladder are still not on
   the Q8 list.

**Not gates on step 5, into the next report's Carried section:** R262, R263, R264, R265,
R266, R248's two residues, R249, R250, R251, R252, R225-R228, the R232 residue, the
remaining half of R233, and everything already at 4a.

**On Q8, since I was asked to rule on it directly.** The plan text states the answer
correctly. The diagnosis is right -- `sin` and `cos` are not correctly rounded and a
gate cannot assert a property the arithmetic does not have -- the choice of CI as the
canonical machine is the only defensible one available, the stamp-inside-the-file
mechanism puts the mismatch where the number is read, the per-class split is the right
shape, and the local rule's form (ULP of the channel's own amplitude) is dimensionless
and survives a unit scaling, which an absolute epsilon would not. The
regenerate-and-compare route removes the category of error instead of widening a
threshold, and I measured the half of it nobody had: same-platform rendering is
byte-identical here. Two clauses are not yet true of the repository, both are
load-bearing, and they are R261.

**And leaving the values unwritten was right.** It is the single best decision in this
range. `EXEMPT_RESPONSE_DRIFT_ULP` had a red CI, a locked Q&A and a one-character fix
sitting in front of it, and it was not touched; the four figure rows were not
regenerated on the machine that produces the wrong ones. `git diff 476f909..HEAD --
floatfea` is empty and `-- docs/milestones/F2_figures.md` is empty. A value written
before its measurement would have been a number describing a laptop, published under
the one plan that exists to stop exactly that.

**Adversarial corpus (BE3): 31 new entries committed at `43e41cb`, across four files,
one of them new, all unseen by the implementer; every `measured` field taken at
`fa3b070` before the `require` or `expect` beside it was written. One existing entry is
RULED ON rather than added to.**

**The coverage measurement, stated plainly: of my 31 new entries the shipped checks do
what the entry requires on 9.** With the corpus applied, the three harnesses that have a
runner give **21 failed, 99 passed**.

* `tests/corpus/report_status_vocabulary.txt` -- **NEW, 12 rows, 4 correct, 8 misses.**
  CC1 had no corpus and its claim is a claim about reach. Four rows carry `closed` past
  both halves end to end; one carries `withdrawn` past the check written to stop it.
  **This file has no runner, so it induces zero failures**, which is the honest state of
  the measurement and is item 6 above.
* `tests/corpus/report_guard_states.txt` -- **+4 (17 -> 21), 2 correct.** The two misses
  are the zero-padded step number in both its shapes, one of which is green while a
  report file is invisible.
* `tests/corpus/ci_ladder_gating.txt` -- **+5 (29 -> 34), 1 correct.** The xpassed-only
  rung, the live empty-rung shape that reaches an unreachable assertion, rung 6's
  shipped job, and the post-summary print.
* `tests/corpus/tolerance_marker_exemptions.txt` -- **+10 (66 -> 76), 2 correct.** Six
  of the eight misses are the two clauses this commit closed, in other spellings.

**The ruling you asked for.** `shallow_clone_depth_1`, `require=green`: **the direction
change is ACCEPTED and my `require` is withdrawn, in the corpus rather than overridden
in test code.** `green` was measured against a guard that produced 23 false accusations,
and what I was recording was those accusations, not a claim that silence is correct. A
guard that cannot compute its input must say so, and `fetch-depth: 0` removes the state
from CI without making it harmless where it occurs -- both halves of the report's
argument are right, and I ran the state myself to check the second: 2 failed, 121
passed, both named, no site parametrisation among them.

**But the requirement as the harness reads it is not measured, and that is R254.** The
ablation says `assert code != 0` passes on the broken guard too, so accepting the word
`named_fail` accepts nothing. The corpus now carries the discriminating form as
`shallow_clone_depth_1_reports_one_diagnosis_not_sixteen`, with the requirement in a
`forbid=` field: no `test_every_named_site_is_touched_or_declared` parametrisation may
fail in that state. The ruling stands because a cell says so, not because the reasoning
was good -- and the same is true of the sixteen.

**Thirty consecutive rounds have found no element defect, and this round does not
either.** `git diff 476f909..HEAD -- floatfea` is empty for the sixth round running.
What this round found is one thing, in four places: **a check verified against inputs
its own author designed.** The `xpassed` arm was written for a shape the author's own
xfail case did not contain. The vocabulary guard was written against the table that
prompted it. The shallow-clone certificate was written against the failure it had
already seen. Both clauses of `CLAUDE.md` were closed in the two spellings I sent last
round. Every one of them is correct about the input it was given; every one was green
here and, where it ran, on CI; and each took one cell to break. That is what BE3
predicts, and it is why the corpus is not the implementer's to write.

**And it is also why R253 is first.** No corpus could have found it. Only a different
machine could, and the reason there was a different machine to find it on is that the
last two rounds did the work of putting one there. The step did the right thing again,
and the right thing found the problem again.
