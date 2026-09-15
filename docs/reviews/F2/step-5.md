# Review — F2 step 5
Reviewed commit: 224d57c84270aad2da22c501d01e3149c1016cbd
Verdict: HOLD

**Reviewed commit: `681c380`.** Report revision 21, `Answers: verdict 46 @
2058087`. The `Reviewed commit:` line stamped above this one by
`scripts/write_verdict.py` is HEAD at the moment of writing -- my corpus commit
`224d57c` -- not the commit judged. That is R373, still open; read `681c380`.

Tests: **2350 passed, 0 failed, 0 skipped** at `681c380` (my run, clean tree,
`python -m pytest -q`, 486.22 s, Python 3.13.15 on Windows). The report's
`2043` excludes 307 report-parametrised tests and reconciles exactly:
`2043 + 307 = 2350`.

**AT MY OWN CORPUS COMMIT `224d57c`: 1 failed**, and it is the figures guard
doing its job -- `rigid_mode_residual_worst_over_corpus` moves `1.0589e-16` to
`1.1410e-16`, `rigid_mode_corpus_frames` `82` to `114`,
`rigid_mode_corpus_refused` `21 of 82` to `29 of 114`. **None of my 32 new
frames reddens the gate.** Named below and in the next report.

**Commits: `a15502a`, `34ce4b3`, `8ded15a` (plan, RE-LOCKED), `4d8b583`,
`f079810`. Report `681c380`.**

**Item 1b.** Revision 21's header at line 7535 reads `Answers: verdict 46 @
2058087`; `git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`20580870b8a76744bbf8e2475e235f02fae530f3`. It is the latest. **Passes.**

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit 681c38001b8d4552eedc009fc0abd47121f1f37a
out  run 34927650922, event push, conclusion SUCCESS, status completed
cmd  gh run view 34927650922 --json jobs
out  "the verification ladder"      success, 13 steps, 04:08:23 -> 04:11:00
     "lint, unit and guards"        success, 14 steps, 04:08:23 -> 04:17:33
     "CI determinism -- leg"        skipped, 0 steps
     "CI determinism -- ten legs"   skipped, 0 steps
judge THE TWO JOBS THAT RAN ARE GREEN ON LINUX AT THE COMMIT I AM JUDGING,
     with the rewritten gate in the ladder. Not CK2: both ran real steps for
     minutes. The determinism pair is dispatch-only here and is recorded as an
     UNAVAILABLE check at this commit rather than skipped over.
cmd  gh run view 34925280557 --json headSha,conclusion   -- the dispatch the
     report's 0a and the invocation both name
out  headSha 8ded15a, event workflow_dispatch, conclusion **FAILURE**
     ten "CI determinism -- leg (n)" success, "ten legs agree" success,
     "the verification ladder" success, and "lint, unit and guards" FAILURE
cmd  gh run view 34925280557 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  22 rows, every one a report-or-figure staleness guard: test_plan_figures
     (the figures commit landed after), test_report_carried,
     test_report_guard_states, and one test_collected_set_golden citation row.
     Nothing in `floatfea/` and nothing in rung 1.
judge THE FAILURE IS EXPLICABLE AND THE OMISSION IS R412, SECOND ROUND. 0a
     names the run by id under "ten legs green, the verdict job green, the
     ladder green" and does not say its conclusion is `failure`. Every
     sentence in it is true. One line is missing and it is the line about the
     one machine neither of us controls. Still 4a, now with a repeat.
cmd  git diff --stat 8ded15a..HEAD -- tests/verification scripts .github
out  one file, tests/verification/rung1/test_rigid_body_corpus.py, 1 insertion
     1 deletion -- a test NAME inside a comment. R383 advanced; the executed
     legs describe the tree under review up to a comment.
cmd  gh pr view 1 --json comments --jq '.comments | length'
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff 2058087..HEAD -- .claude docs/SUPERVISOR.md
out  (empty) -- no STOP-class finding. Nothing under `.claude/` moved.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py                  -- the instruction's own expectation
cmd  git diff 2058087..HEAD -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is being written by code in its own directory.
cmd  git diff --stat 2058087..HEAD -- floatfea
out  floatfea/tolerances.py | 176 +++++----- -- ONE FILE
cmd  git show --stat on each of the five commits
out  `8ded15a` touches docs/milestones/F2.md ALONE and says RE-LOCKED.
     `a15502a` touches docs/milestones/F2.md AND code: two rows of the
     tolerance-value table, which `tests/test_plan_matches_tolerances.py`
     forces to move with the values, and the figure-name list. Mechanical,
     not a plan change dressed as one; the argument moved in `8ded15a`. Noted,
     not a finding.
```

## Carried

Verdict 46 held on R403, R404, R405, R406, R407, R408, R409 and carried R399.
**R403, R407, R408 and R399 are answered. R413 is answered without being
claimed. R404 is answered except for the row it created. R405, R406 and R409
are recorded as answered by the report and are not.**

- **R403 -- ANSWERED, AND THIS IS THE STRONGEST THING IN THE ROUND.** I put my
  own instrument on the replacement and could not break it.


```
rule  lambda_7(K_hat) >= tau * 10**RIGID_MODE_GAP, tau = FLOOR*||K_hat||*eps
cell  THE SAME TECHNIQUE THAT KILLED BOTH PREDECESSORS: compose corpus entries
      that hold alone, and ladder one parameter through the transition.
out   rb_unit_millimetre x rb_span_x10000, R403's own composition: REFUSED.
      Over all 82 committed frames: 61 decided, 21 refused, and the number of
      eigenvalues below tau is EXACTLY SIX at every one of the 61. All 11
      non-six frames are refused.
cmd  440 further (unit, stretch) points, 11 unit systems from 1e-4 to 1e6,
     stretch 1 to 2e7, asking for margin >= 1.3 WITH below_tau != 6
out  ZERO. Plus my 32 new frames: zero. 554 configurations, no green with a
     seventh numerically-zero mode.
cell AND SOLVED RATHER THAN SAMPLED, one parameter at metre units:
out  stretch 1.90e6 margin  0.024 below_tau 6
             1.95e6 margin -0.003 below_tau 7
             2.00e6 margin -0.024 below_tau 8
judge THE COUNT LEAVES SIX EXACTLY WHERE THE MARGIN CROSSES ZERO, and the
     bound sits 1.3 orders on the safe side of it. That is what R403 said the
     old gap did not do, measured over 554 configurations. Closed.
cell AND THE OTHER DIRECTION -- a REAL mechanism, re-expressed 48 ways
out  the torsional release at 6 unit systems x 4 spans x 2 subdivisions:
     48 of 48 REFUSED, margins -1.09 to -9.60. Not one certified.
```

- **R404 -- ANSWERED ON THE ROW IT NAMED, OPEN ON THE ROW THE FIX CREATED.
  This carries as R418.** `10**abs(a-b)` and `10**(b-ceil)` are the right
  comparison and I reproduce the entry's `1.095` and `1.603x` exactly through
  the shipped `counter_response("gap")`. But `as_ratio = n.endswith("_orders")`
  dispatches on a NAME, and the same commit renamed the second log-valued row
  to `rigid_mode_seventh_orders_smallest_decided`, which does not end in
  `_orders`. Its spread is still computed as a ratio of logarithms. R404's
  condition said "the two gap-in-orders rows".

- **R405 -- NOT ANSWERED. The report's own named command refutes the report.**

```
code report section 3: "cmd grep for `sixteen` and for `twenty-eight frames`
                        out replaced by the rendered figure"
cmd  that grep, run at 681c380, over floatfea/ tests/verification docs/
out  floatfea/tolerances.py:295  "corpus of twenty-eight frames ... a large
                                  minority of them exceed its ceiling"
     floatfea/tolerances.py:438  "a large minority of the reviewer's
     floatfea/tolerances.py:439   fifty-six frames"
     test_rigid_body_modes.py:23  "exceeding its ceiling on a large minority"
     test_rigid_body_modes.py:468 "Sixteen of the
     test_rigid_body_modes.py:469  twenty-eight frames in the corpus"
     docs/milestones/F2.md:1823   "poses twenty-eight frames" ... "a large
                                   minority of those frames"
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt   (at 681c380)
out  82
cmd  grep retired_ratio_over_ceiling docs/milestones/F2_figures.md
out  | retired_ratio_over_ceiling_on_corpus | 60 of 82 |   -- I reproduce it
judge 60/82 IS 73 PER CENT. Not a large minority, and neither "twenty-eight"
     nor "fifty-six" is the size of the file. THREE of the five sites are the
     three R405 named; TWO ARE NEW THIS ROUND, written into the gate file's
     header and docstring by the commit that repaired R407 six lines above
     them. The carried table records this item as answered.
```

  **Closed when** all five sites carry the rendered figure or a quantifier the
  figure supports, and the corpus size is read from the file rather than typed.
  `{{fig:rigid_mode_corpus_frames}}` exists and now reads `114`.

- **R406 -- HALF ANSWERED. The counter paragraph is right; the section the
  last verdict called "worse" is untouched.**

```
cmd  git show 8ded15a -- docs/milestones/F2.md | grep "^@@"
out  ONE hunk, at -1774,29 +1774,50. The "G2.1's two quantities, added at
     step 5 (V1.1)" section at :1865-1900 is not in it.
code :1889 "Both are registered in `tests/test_counters_are_injected.py` and
           pass its two cells."
cmd  grep -n "RATIO PAIR IS GONE" tests/test_counters_are_injected.py
out  :128 "THE RATIO PAIR IS GONE FROM THIS REGISTRY (Q7)."
code :1884 the headroom table, `~83x` and `~18x`, against two ceilings that
           decide nothing, in the present tense
code :1878 "it is the assertion AP3 asks for, and without it G2.1 would be six
           numbers near zero with nothing said about what they are modes of"
code report section 4: "R406. ... The plan text is rewritten to CT0 in full."
judge "IN FULL" IS ONE HUNK. The verdict's condition named this section
     explicitly -- "either says at its head that everything in it is the
     retired form, or is cut" -- and BP0's "regenerated or withdrawn in the
     same commit" applies to `~83x`, `~18x` and "two cells" by name.
```

  **Closed when** :1865-1900 says at its head that it is the retired form, or
  is cut; and the false registry sentence goes either way.

- **R409 -- NOT ANSWERED. Section 5 answers a different window.**

```
cmd  git diff f19eef5..44f28e8 -- tests/goldens/collected_tests.txt | grep ^-
out  -test_a_RIGID_BODY_MODE_that_carries_ENERGY_is_caught
     -test_the_analytic_rigid_body_vectors_are_SPANNED    <- the two DELETIONS
code report section 5 heads its command `git diff 2058087..HEAD`, lists seven
     renames, and concludes "EVERY ONE IS A RENAME ... None is a deletion."
judge TRUE OF THIS ROUND'S WINDOW AND IRRELEVANT TO THE ITEM. R409 was about
     two assertions deleted in `7a5445a`, which is BEFORE `2058087`. Neither
     name appears anywhere in revision 21. It is a good golden-change section
     for the wrong diff.
cmd  grep -n "six numbers near zero" docs/milestones/F2.md
out  1878 -- the second half of R409's condition, verbatim, untouched. And
     :1662's D5 row and :1672 still say V1.1 asserts on the subspace.
judge The substance is still defensible and I said so last round: the residual
     is a stronger form of AP3's claim. What is missing is still anyone SAYING
     so where the golden rule and the plan need it.
```

- **R407 -- ANSWERED.** The header states the two halves, neither reads an
  eigenvector, AP3 is answered onto the residual rather than dropped, and the
  "TWO QUANTITIES, BOTH GATED" block is gone -- `grep -n "BOTH GATED"` is
  empty. **Closed.** The two count sentences six and 445 lines below it are
  R405, not a re-carry of this.

- **R408 -- ANSWERED, with the grep run.** `:437` now reads "referenced twice
  -- by `counter_response` ... and by the import that feeds it -- and by no
  assertion", and records the sentence that was refuted. I reran the grep:
  three hits, the definition plus the two the entry names. **Closed.**

- **R399 -- ANSWERED at both sites its condition named.** Both `_COUNTER_DEFECT`
  entries now open "RETIRED WITH ITS CEILING (R399)" and put the rest in the
  past tense, and `grep -n "rigid_body_counter" scripts/regen_figures.py` shows
  both rows plain, with no `_floor(...)` mark against a retired ceiling.
  **Closed.**

- **R413 -- ANSWERED, and not claimed.** `:353-356` now says `1.461` units at
  `rb_span_x1000` and `6.84x`, solved rather than sampled. I reproduce `1.4614`
  and `6.843x` over the same 82 frames, and the "a decade on each side"
  sentence is gone. **Closed.** What the solved bracket does not do is decide
  anything, and that is R415.

- **R410 -- DOES NOT RECUR IN ITS OWN SHAPE.** The generated table and the
  prose sections agree this round. They agree on three statuses that are
  wrong, which is R405, R406 and R409 above, not this item. Still 4a.

- **R411 -- OPEN, AND THE POINTER IS NOW BROKEN.** Revision 21's second line
  says "Commits since the forty-sixth verdict, listed in section 8"; section 8
  is "Sites named by findings and not touched" and lists no commit. There is no
  commit block in this revision at all. Fifth round for this row; 4a.

- **R412 -- OPEN, second round, same shape.** See the CI block.

- **R414 -- OPEN.** `test_ONE_PINNED_DOF_leaves_FIVE` and
  `test_a_PINNED_DOF_is_caught_by_the_RESIDUAL_half` still pin the same 30 DOFs
  by the same rule in two files, and the release pair does the same. 4a.

- **R383 -- ADVANCED, NOT CLOSED.** Ten legs executed and agreed at `8ded15a`;
  one comment line in the rung the legs run has moved since.

- **R400, R401, R402, R390, R391, R392, R393 -- OPEN at 4a**, correctly listed.
- **R370, R371, R372, R373, R374 -- OPEN at 4a.** R373 bites again in this
  verdict's own header.
- **R362, R363, R364, R354, R355, R356, R357, R347, R348, R349, R350's second
  half, R330, R331, R332 -- OPEN at 4a, correctly listed.**
- **R231, R244, R245, R275 -- OPEN, unblocked**, and the report correctly does
  not claim them. Step R has not run.
- **R230, R261 -- OPEN by instruction, correctly listed.**
- **R300, R291, R292, R281, R321, R322 -- OPEN, recordable at 4a.** R302
  accepted at verdict 37, not reopened.
- **R315-R320, R323-R329, R293, R303-R308 -- closed in earlier verdicts,
  carried.** The section 9 status-versus-subject disagreement stays at 4a.
- **R253, R254, R256, R257, R262-R274, R276, R277, the two R248 residues,
  R249-R252, R225-R228, R232, R233, R288, R289, R290 -- carried.** R250, R251,
  R226, R227, R264 and R266 still have no row; R348 territory, unmoved.
- **R365-R369, R375-R382, R384 -- carried in `step-5-answers.json`.**
- **R223, R224, R394, R395, R396, R397, R398, R388 -- closed earlier**, not
  reopened.

## Findings

**First, what is right, and it is the larger part of this round.**

**THE BOUND IS THE BEST FORM G2.1 HAS HAD AND I COULD NOT BREAK IT.** Three
attacks, all measured: 554 configurations with no green on a seventh zero mode;
48 re-expressions of a genuine mechanism, 48 refused; and the six-to-seven
transition solved on one parameter, landing exactly at margin zero with the
bound 1.3 orders clear of it. Dropping the count for a statement about
`lambda_7` alone is right, and refusing rather than answering is the honest
outcome of a conditioning limit. `pytest.skip` was tried and removed, the
residual is asserted at all 82 frames including all 21 refused, and the domain
is published rather than buried. R398's controls survive the rewrite: I ran
both cells of the meta-test for both spectral counters and all four fire.

**And my own corpus says so too.** Thirty-two new frames, none of them
breaching anything -- the first round in five in which the corpus found no hole
in the thing it was aimed at.

---

**R415. (BLOCKS -- `RIGID_MODE_FLOOR` and `RIGID_MODE_GAP` are one threshold
wearing two names. FLOOR can be moved to a value its own entry says is wrong,
with the entire gate, both counters, all four controls, both meta-cells and all
82 corpus frames green.)** `floatfea/tolerances.py:327-363` and `:388-411`,
`tests/verification/rung1/test_rigid_body_modes.py:247-286`.

```
code the decision, in full: lambda_7(K_hat) >= FLOOR * ||K_hat|| * eps * 10**GAP
cmd  grep -rn "RIGID_MODE_FLOOR" --include=*.py .
out  tolerances.py (definition and comments); test_rigid_body_modes.py:251
     inside `zero_mode_threshold`; :450 a print; test_counters_are_injected
     .py:160. `zero_mode_threshold` is called from `seventh_over_threshold`
     and from one print. NOTHING COUNTS EIGENVALUES BELOW TAU ANYWHERE.
judge SO THE TWO CONSTANTS ENTER THE ONLY ASSERTION AS THE PRODUCT
     FLOOR * 10**GAP = 199.53, and no measurement in this repository can tell
     one from the other.
cell ONE VARIABLE MOVED IN COMPENSATED PAIRS, everything else held: FLOOR
     10.0 -> 1.0 and GAP 1.3 -> 2.3, product unchanged. Then: the gate, the
     retired-diagnostic test, both pin controls, both release controls, R403's
     composition, the finer-unit frame, all 82 corpus entries, and both cells
     of the meta-test for both spectral counters.
out  SHIPPED  FLOOR=10.0 GAP=1.3 : ALL GREEN
     MOVED    FLOOR=1.0  GAP=2.3 : ALL GREEN
judge AT FLOOR = 1.0, tau SITS BELOW THE LARGEST RIGID-BODY EIGENVALUE the
     entry itself measures -- `1.461` units of ||K_hat||*eps at `rb_span_x1000`
     -- so a genuine rigid mode is no longer numerically zero, which is the
     exact condition :353-356 says the floor must clear by `6.84x`. The entry's
     own bracket is a real measurement against a rule nothing applies. That is
     BP0 one level down: the rule beneath the figure moved when CT0 deleted the
     count, and the figure is correct and no longer load-bearing.
judge AND IT IS WHAT MAKES "EXACTLY SIX" TRUE RATHER THAN MERELY "NO SEVENTH".
     The file's own argument is Courant-Fischer: the residual half puts six
     eigenvalues under tau. That step needs RIGID_MODE_EXACTNESS <= FLOOR*eps
     -- `1e-15` against `2.22e-15`, a 2.2x margin -- which is stated nowhere,
     and empirically 1.461 against 10, which is stated and unenforced. The
     composition is TRUE at this commit: I measured below_tau == 6 at all 61
     decided frames of 82, at all 24 decided of my 32, and at 440 swept points.
     It is true and untested.
```

**Closed when** either the two constants are collapsed into the one number the
decision uses, or something asserts the composition that makes the second
constant observable -- "the below-tau count is six at every decided frame" is
one loop, it is already true everywhere I can measure it, and it turns the
`6.84x` bracket back into something that can fail. **I am not asking for a
third constant or a wider gate. I am asking that the entry's own window decide
something.**

**R416. (BLOCKS -- a sentence added THIS ROUND to justify a counter's size says
the meta-test checks a discrimination it does not check, and the cross cell
refutes the discrimination.)** `floatfea/tolerances.py:372-379`.

```
code :372 "SIZED BY THIS CONSTANT AND NOT BY THE OTHER ONE, which is what
     :373  `tests/test_counters_are_injected.py` widens to check."
cmd  tests/test_counters_are_injected.py, _ceiling_cell, run four ways
out  floor counter: fails when FLOOR widened = True   when GAP widened = True
     gap counter:   fails when FLOOR widened = True   when GAP widened = True
judge "SIZED BY THIS AND NOT THE OTHER" WOULD READ True/False AND False/True.
     Each counter responds to both, because there is one bound (R415). The
     meta-test runs one cell per row and never compares rows, so it cannot
     check the clause attributed to it -- its own docstring says so: "both
     cells are per-counter".
judge THE MEASURED HALF IS TRUE AND WORTH KEEPING: lowering FLOOR by a decade
     does take this margin to `1.396` and the cell does pass. I reproduce
     `0.3962`, `1.3962`, and `0.0151` at the retired `8.318e-15`. It is the
     "AND NOT BY THE OTHER ONE" that is a causal claim with no cell.
```

**Closed when** :372 claims what the cell measures, or a cell that measures the
discrimination exists. The first is one sentence.

**R417. (BLOCKS -- both descriptions of the gap counter's size are wrong by a
factor of three, in the tolerance entry and in the test that injects it.)**
`floatfea/tolerances.py:413-414` and
`tests/verification/rung1/test_rigid_body_modes.py:679`.

```
code tolerances.py:413 "Reason for 1.0e-13: the same nearly-released
     :414              connection, one and a half decades stiffer"
code test_rigid_body_modes.py:679 "The same defect a decade and a half stiffer"
cmd  RIGID_MODE_GAP_COUNTER_DEFECT / RIGID_MODE_FLOOR_COUNTER_DEFECT
out  1.0e-13 / 2.0e-14 = 5.0  ->  log10(5.0) = 0.699 decades
judge NOT ONE AND A HALF DECADES. Not against the retired `8.318e-15` either,
     which is 1.08. The numbers `0.396` and `1.095` that flank the sentence are
     both exactly right and I reproduce both; the arithmetic relating them is
     the thing nobody ran. That is CP2's species precisely -- the prose written
     around a repair inheriting none of the discipline applied to the repair.
```

**Closed when** both sentences say `5x`, or `0.7 of a decade`, or nothing.

**R418. (BLOCKS -- R404's fix dispatches on a name suffix, and the same commit
created a log-valued row the suffix does not match.)**
`scripts/regen_figures.py:636`.

```
code as_ratio = n.endswith("_orders")
cmd  the figure names this commit publishes
out  rigid_mode_seventh_orders                    -- matches, compared right
     rigid_mode_seventh_orders_smallest_decided   -- DOES NOT MATCH
judge THE SECOND ROW IS log10 OF A RATIO AND ITS SPREAD IS STILL COMPUTED AS
     max(a,b)/min(a,b) ON LOGARITHMS. At `1.312` a platform factor of 1.5 on
     the underlying ratio shifts it by 0.176 and the guard would read
     `1.488/1.312 = 1.134x` where the declared spread is `1.5x` on the ratio.
     Nothing tripped; the guard's sensitivity on that row is reduced by roughly
     the row's own magnitude, which is the sentence I wrote in R404 about the
     row this one replaced. R404's condition said "the two gap-in-orders rows".
judge AND THE MECHANISM IS THE FINDING, not the row: a name-suffix test means
     the next log-valued figure is compared wrongly by default and silently.
```

**Closed when** log-valuedness is carried by the row rather than inferred from
its name, or the second row is renamed so the existing rule reaches it.

**R419. (recordable, 4a) The corpus test's spectral half asserts almost nothing
per entry, and the domain can drift without a red.**
`tests/verification/rung1/test_rigid_body_corpus.py:189-230`. Per entry only
`np.isfinite(margin)` is asserted; the split is asserted only as "both sides
non-empty". The gate could refuse 80 of 82 frames and this file would stay
green. What actually guards the number is `{{fig:rigid_mode_corpus_refused}}`
through the figures staleness check on the canonical machine -- a real guard,
and not where a reader of this file would look. The docstring says the reviewer
will mark entries `expect=undecidable`; I have not, and I say so here rather
than leaving it implied. My new block carries `outcome=` for every entry, so
the next round can assert against it.

**R420. (recordable, 4a) `test_ONE_RELEASED_CONNECTION_gives_SEVEN` computes
its own answer from the thing it is testing.**
`tests/verification/rung1/test_rigid_body_modes.py:589`:
`dim = RIGID + 1 if margin < RIGID_MODE_GAP else RIGID`, then
`assert dim == RIGID + 1` five lines after `assert margin < RIGID_MODE_GAP`.
The second assertion cannot fail while the first passes. The control is sound
-- the first assertion does the work and I confirmed it fires -- but "a gate
carries its own failure", and this half cannot.

## Tolerances touched

**One file, `floatfea/tolerances.py`, `+98 -78`, all in `a15502a` and
`34ce4b3`. Two values moved, both of them counters; no ceiling moved.**

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| `RIGID_MODE_FLOOR` | `10.0` | `10.0` | unchanged in value; **the rule it serves changed** -- it no longer thresholds a count, only `tau` in one bound | `RIGID_MODE_FLOOR_COUNTER_DEFECT`, now the nearly-released connection at `2.0e-14`, injected through `assembled`, decided by the shipped bound, pinned by `match="UNDECIDABLE"` | `:339-362`. Bracket re-measured and solved; I reproduce `1.4614` units and `6.843x` over 82 frames. **R413 closed. R415: nothing makes this bracket decide anything.** |
| `RIGID_MODE_FLOOR_COUNTER_DEFECT` | `1.0e-12` | `2.0e-14` | relative stiffness given back on the released twist DOF | n/a | `:365-380`. **Margin `0.3962` reproduced exactly, `1.3962` under the meta-test's own widening, `0.0151` at the retired value. The move is right and the meta-test forced it, which is that file working. R416 is the sentence beside it.** |
| `RIGID_MODE_GAP` | `1.3` | `1.3` | unchanged in value; **the quantity it bounds changed** -- from the separation after the last eigenvalue below `tau` to `log10(lambda_7 / tau)` at the sixth-seventh boundary | `RIGID_MODE_GAP_COUNTER_DEFECT` at `1.0e-13`, same injection one size up, pinned by `match="UNDECIDABLE"` | `:388-410`. **Both margins now in the same quantity (R404): `1.095` orders, `1.603x` as a ratio against a declared `1.5x`. I reproduce both. The `below` half is the counter's placement rather than a reachable minimum -- the smallest non-negative margin this injection reaches is `0.029` on my 200-point scan -- and the entry no longer claims otherwise.** |
| `RIGID_MODE_GAP_COUNTER_DEFECT` | `8.318e-15` | `1.0e-13` | relative, same site | n/a | `:412-417`. **R417: "one and a half decades stiffer" is `5x`.** |
| `RIGID_BODY_MODE_RATIO` and its counter | `1e-12` / `1.0e-12` | unchanged (**retired**) | nothing asserts against either | -- | `:419-473`. R399 and R408 closed. **R405 on "a large minority of the reviewer's fifty-six frames".** |
| `RIGID_BODY_SUBSPACE_LOSS` and its counter | `1e-13` / `1.0e-12` | unchanged (**retired**) | nothing asserts against either | -- | `:475-531`. R399 closed. |

```
judge NO VALUE WAS WIDENED TO RESCUE A TEST. No test was failing before either
     counter moved; the floor's counter moved because the meta-test refused it
     for reddening on the other constant's account, which is that guard doing
     its job, and the move makes the counter a FIFTY TIMES SMALLER defect. No
     ceiling moved at all this round.
judge NO OTHER NUMBER IN THE FIVE COMMITS FUNCTIONS AS A TOLERANCE. `RIGID` is
     still a kinematic constant with a not-a-tolerance docstring; `EPS` is
     `np.finfo(float).eps`; `WIDEN` is a declared not-a-tolerance; the
     `-1.0e-3` ARPACK shift carries its own not-a-tolerance comment.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2350 passed at 681c380 -- no undeclared literal entered tests/ this round
     and nothing was added to `tolerance_marker_exemptions.txt`.
```

## Next step opens when

**Step 5 stays OPEN. Step 6 does not begin.**

**The gate's claim is in the best shape it has been in, and that goes first.**
R403 is answered by measurement rather than by argument: 554 configurations, 48
re-expressions of a real mechanism, and the transition solved on one parameter
with the bound 1.3 orders clear of it. No count, one bound, and a refusal that
is a red rather than a skip is the right answer to a conditioning limit. R407,
R408, R399 and R413 are closed at the lines their conditions named, CI is green
on Linux at the reviewed commit, the local suite is 2350 green, and nothing
went near `.claude/` or a conftest.

**What holds is six items. Two are about the gate's own constants, one is a
counter's size described wrongly, and three are closing conditions the report
records as met that measurement says are not.**

1. **R415 -- two constants, one threshold.** `FLOOR 10 -> 1` with
   `GAP 1.3 -> 2.3` leaves everything green while `tau` falls under the `1.461`
   the entry says it must clear by `6.84x`.
2. **R416 -- "sized by this constant and not by the other one"**, refuted by
   the cross cell: both counters fail under both widenings.
3. **R417 -- "one and a half decades stiffer" is `5x`,** in the tolerance entry
   and in the test that injects it.
4. **R418 -- R404's fix misses the row R404 named,** because it dispatches on
   the suffix `_orders` and that row was renamed to end in `_decided`.
5. **R405 -- five sites still say twenty-eight, fifty-six, sixteen and "a large
   minority"** against a rendered `60 of 82`; two of the five were written this
   round, and section 3's own grep is the command that refutes section 3.
6. **R406 and R409 -- the plan section the last verdict called "worse" is
   untouched** (`~83x`, `~18x`, "registered ... and pass its two cells", "six
   numbers near zero"), and section 5's golden-change section documents this
   round's seven renames instead of the two deletions R409 named.

**Adversarial corpus (BE3): 32 new entries in
`tests/corpus/g21_rigid_body_frames.txt`, all unseen by the implementer,
committed separately at `224d57c`.** The file goes 82 -> 114.

**The coverage measurement, stated plainly: of my 32 new frames the shipped
gate reddens at NONE.** Twenty-four decided, eight refused, and a refusal is
the declared domain rather than a breach. The residual half holds at all 32,
worst `1.1410e-16` against `1e-15`. Last round it was 13 breaches of 26; the
rule changed underneath and the same technique no longer finds a hole.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
       tests/test_plan_figures.py -q        (at 224d57c)
out  1 failed, 363 passed
     tests/test_plan_figures.py::test_the_generated_figures_are_not_stale
```

* **The one red at my commit is the figures guard and it is correct.**
  `rigid_mode_residual_worst_over_corpus` `1.0589e-16` -> `1.1410e-16`,
  `rigid_mode_corpus_frames` `82` -> `114`, `rigid_mode_corpus_refused`
  `21 of 82` -> `29 of 114`. **The next report regenerates them and names
  them.**
* **What is new, and the first item is the one that mattered.** The `tip` field
  has existed in this format since the twenty-sixth verdict and no entry ever
  moved it: all 82 are `4.4,1.1,2.8`. The shipped release control asserts that
  member is parallel to global x, so the one piece of geometry the gate leans
  on is the one the corpus never varied. Eight entries move it -- skewed,
  reversed, nearly coincident with node 3, ten times further out -- and all
  eight are decided with `below_tau = 6`.
* **Also unseen:** near-solid and `1e-6 m`-wall sections; `D=4.0` and `D=8.0`
  on a four-metre frame; `stretch < 1`, which shrinks the frame where every
  composed entry above stretches it; `subdiv` 32 and 48; and unit and span
  pulling in OPPOSITE directions, where every composed entry above pushes both
  the same way.
* **Six entries ladder the decision boundary on one parameter** so the margin
  crosses `RIGID_MODE_GAP` with nothing else moving, and the block's header
  records the solved crossing: the margin reaches zero at `stretch ~1.95e6`,
  which is exactly where `below_tau` leaves six.
* **The block carries `below_tau=` as the control on the bound**, and its
  header names the shape to watch for: `outcome=decided` with `below_tau` not
  six. There is none, in 114 entries or 440 swept points.

**Not gates on step 5, into the next report's Carried section:** R419, R420,
R410, R411, R412, R414, R400, R401, R402, R390, R391, R392, R393, R383, R370,
R371, R372, R373, R374, R362, R363, R364, R354, R355, R356, R357, R347, R348,
R349, R350's second half, R330, R331, R332, the section 9 status-versus-subject
disagreement, R321, R322, R300, R291, R292, R281, R231, R244, R245, R275, R230,
R261, the underlying gap in R276, R277, R262, R264, R266, the two R248
residues, R249-R252, R225-R228, R232, R233, and everything already at 4a.
R403, R407, R408, R399 and R413 are closed. R404 is closed on its own row and
reopens as R418. R405, R406 and R409 carry.

**Forty-seven rounds have found no element defect, and this round found none
either -- for the first time including my own corpus.** Every one of the 114
frames is the same defect-free element and the residual half holds at all of
them. It still means "not yet contradicted": ladder 5 has printed
`OK -- 0 directories ran` every time it has run, and V5.1 against CalculiX is
the witness that has not spoken.
