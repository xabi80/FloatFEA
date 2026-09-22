# Review — F2 step 5
Reviewed commit: b49960fcb694fc54f56424f7ce807bbb259b4a0c
Verdict: PASS

**Reviewed commit: `125cee1`.** Report revision 27, `Answers: verdict 52 @
2d4f7fb`. The `Reviewed commit:` line `scripts/write_verdict.py` stamps above
is HEAD at the moment of writing -- my corpus commit `b49960f` -- not the
commit judged. R373, still open; read `125cee1`.

Tests: **2581 passed, 0 failed, 0 skipped** at `125cee1` (my run, clean tree,
`python -m pytest -q`, 566.88 s, Python 3.13 on Windows).

**Commits judged: `e45aae6` (process), `0e7e21f` (process), `db6d78e`,
`f9e24f5`, `c43f6e7`, `125cee1`.**

**Item 1b.** Revision 27 line 10021 reads `Answers: verdict 52 @ 2d4f7fb`;
`git log -1 --format=%H -- docs/reviews/F2/step-5.md` is
`2d4f7fb0d4c5aeb32403f7c732e3f53747f7ed9b`. It is the latest. **Passes.**

**PASS IS THE CZ0 DISPOSITION AND NOT AN ALL-CLEAR. This round found the
first (b)/(c) finding in fifty-three rounds** -- R475, on the gate's counter
and on what the closure artifact claims Claim A establishes. Under CZ0's
three-verdict rule the step closes and an open blocking item carries by name
into the next step and stays blocking there, which is what I have done.
Under the criterion this round replaced, R475 would be a HOLD. It is listed
first, it is blocking in F2-rung2, and it should be answered in that step's
first commit rather than at its end.

## CI, item 3b -- GREEN AT THE REVIEWED COMMIT

```
cmd  gh run list --commit 125cee1 --json databaseId,event,status,conclusion
out  35672582951 workflow_dispatch completed SUCCESS
     35672572925 push             completed cancelled  -- NO RESULT
cmd  gh run view 35672582951 --json jobs
out  13 jobs, ALL success: lint-unit-and-guards 14 steps 10m48s, the
     verification ladder 13 steps, ten CI determinism legs 13 steps each,
     and the ten-legs-agree job 4 steps
judge GREEN ON LINUX AT THE COMMIT I JUDGE. Not CK2: every job ran real
     steps for minutes. The ten determinism legs executed for the second
     consecutive round.
judge THE CANCELLED PUSH RUN IS NOT A RED BUILD. `125cee1` is report-only
     and `paths-ignore` skips it; the dispatch is the deliberate answer and
     it is the one that ran.
cmd  gh run list --commit c43f6e7 --json conclusion
out  failure -- run 35671331985
cmd  gh run view 35671331985 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  13 rows: test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph,
     test_the_whole_suite_line_is_about_a_commit_that_exists, three
     test_every_named_site_is_touched_or_declared parametrisations, and the
     eight test_report_guard_states cascade
judge THE ACCOUNT I WAS GIVEN IS TRUE AND INCOMPLETE IN MY FAVOUR. I was
     told the red was the report lagging the code; it is, and section 0a of
     revision 27 publishes all thirteen names, generated. Every one is
     answered at `125cee1`, which is why the revision is the last commit.
cmd  gh run list --commit e45aae6 / 0e7e21f / db6d78e / f9e24f5
out  [] for each -- paths-ignore. Recorded as unavailable, not skipped.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Recorded as an unavailable check.
```

**I re-ran all four CI generators at `125cee1` and compared, newline-
normalised.**

```
cmd  python scripts/ci_section.py with no flag, --rounds, --history, --commits
out  section 0. IDENTICAL.  0b. IDENTICAL.  0a. committed 25 lines, fresh 27
     -- the two extra are the runs at `125cee1` itself.  0c. committed 15,
     fresh 16 -- the extra is `125cee1` itself.
judge THE COMMITTED CI RECORD IS FAITHFUL. Every committed line is in the
     fresh render and the only additions post-date the report own commit,
     which is structural and is stated in each provenance line.
```

## My own instructions (4b), the conftest pathspec (4c), tolerances (4)

```
cmd  git diff --stat 2d4f7fb..125cee1 -- .claude docs/SUPERVISOR.md
out  .claude/agents/gating-supervisor.md | 74 ++-
     .claude/hooks/stale-before-commit.sh | 15 ++-
     docs/SUPERVISOR.md                   | 12 +-
cmd  git show --stat --format= e45aae6
out  .claude/agents/gating-supervisor.md, CLAUDE.md, docs/SUPERVISOR.md
cmd  git show --stat --format= 0e7e21f
out  .claude/hooks/stale-before-commit.sh
judge TWO STANDALONE process: COMMITS, each citing its directive, neither
     touching floatfea/ or tests/. NOT A STOP. I read both diffs line by
     line. `e45aae6` replaces the BU0 section with CZ0 and KEEPS the escape
     hatch -- if something classed as a closure item does touch (a), (b) or
     (c), block on it -- and keeps BE3 intact and named. `0e7e21f` REMOVES A
     WITHDRAWN FIGURE and adds no permission; the hook still decides ask,
     never deny, and the reviews/corpus PreToolUse hook beside it is
     untouched. NO GUARD DELETED.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction own expectation
cmd  git diff 2d4f7fb..125cee1 -- the same two pathspecs
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung green is written by code in its own directory.
cmd  git diff 2d4f7fb..125cee1 -- floatfea/
out  (EMPTY -- not one byte, comments included, for the ninth round running)
cmd  git diff --stat 2d4f7fb..125cee1 -- docs/verification PLAN.md
out  (empty) -- the ladder own plan was not touched.
```

## Carried

Verdict 52 held on R467, R468, R469 and R470, and recorded R471-R474. **All
four held items are answered, three of them cleanly and one by the
alternative route the condition named.** R471-R474 are on the frozen list.

- **R467 -- ANSWERED, by the BI3 remedy the condition named.**
  `.claude/hooks/stale-before-commit.sh:35-46` now carries no figure at all
  and points at the docstring of `scripts/precommit_stale.py`. I ran
  `python scripts/precommit_stale.py afc5b05^..afc5b05` and got
  `14 survivor(s)`; the docstring names that command and prints 14/0. The
  sentence that justified ask is restated without resting on a count, which
  is correct -- it never did. **Closed.**
- **R468 -- ANSWERED, at both sites its condition named.** I ran the four
  invocations myself: with no flag, --rounds, --history and --commits each
  emit their own `Generated: python scripts/ci_section.py <its own flag>`
  line, four distinct strings. And `tests/test_report_carried.py` now
  asserts the `--rounds` provenance line is in the 0a block -- the guard
  requires the string the generator writes instead of the false one.
  **Closed.**
- **R469 -- ANSWERED, and the docstring says the harder thing.**
  `tests/test_tree_prose_consistent.py:42-72` now reads REGISTRATION IS NOT
  FINDABILITY, and the earlier wording here claimed it was, and `:459-470`
  rewrites rule 3 as THE NEEDLE IS REGISTERED EXACTLY ONCE with an explicit
  WHAT THIS FUNCTION DOES NOT DECIDE paragraph saying most unseen defect
  shapes pass it. No figure is repeated in the tree; the measurement is left
  in the verdict, which is the BI3 answer. **Closed.**
- **R470 -- ANSWERED by a third route, and I accept it.** Revision 27 section
  1 carries the split sentence, names `651a524` and `2bd9e89`, and states
  that the rewrite left a red push run at a commit unreachable from HEAD. It
  does not type the run id, and the argument is that the report own guard
  refuses a run id in hand-written prose. **I verified that guard bites:**
  `test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` requires
  every run id in hand-written text to be in a generated form, and
  `control_a_naked_run_id_in_a_plain_paragraph_outside_any_marked_section` is
  a shipped shape asserting exactly that refusal. So the condition first
  branch was not merely skipped -- it is **unsatisfiable** against the
  apparatus the same item built, which is a fact my own condition did not
  know. The structural route -- section 0a prints the row labelled *head not
  in current history* when anchored on that round -- is the one verdict 52
  called a good one. **Closed.**
- **R471, R472, R473, R474 -- OPEN, on the frozen list, correctly.** I
  re-verified the list is exactly the open set: `docs/milestones/F2a.md` has
  48 rows matching the item pattern, `docs/reports/F2/step-5-answers.json`
  has 48 entries in state open, and the two sets are **equal** -- no item in
  the list that is not open, none open that is not in the list. That is a
  stronger statement than the commit message 44 + 4 and it is the one that
  matters.
- **R383 -- STATE UNCHANGED FROM LAST ROUND AND STILL NOT BANKED.** The ten
  determinism legs ran green again at `125cee1`, 13 steps each. No leg table
  is published. Closure item; `python scripts/ci_section.py --legs`.
- **R458, R447, R419, R431-R433, R410-R414, R400-R402, R390-R393, R370-R374,
  R362-R364, R354-R357, R347-R350, R330-R332, R321, R322, R300, R291, R292,
  R281, R275, R261, R244, R245, R231, R230, R223, R224 and everything else
  the answers file carries -- OPEN on the frozen 4a list**, correctly listed,
  not re-reviewed item by item under CZ0.
- **R459, R460, R461-mechanism, R462-R466 -- closed in verdict 52**, not
  reopened.

## Findings

**First, what is right, and it is the larger part again.**

**THE STEP RECORD IS NOW GENERATED AND IT IS FAITHFUL.** Four CI sections
reproduce from their own named invocations; the 4a list is exactly the open
set, checked both ways; the report is append-only -- the diff over
`docs/reports/F2/step-5.md` removes exactly one line and it is the `---`
diff header, so revision 26 is untouched as claimed; and section 5 suite
line reconciles to the unit at its own commit. I collected 2586 tests at
`f9e24f5` in a clean worktree and 381 in the three excluded files, and
2586 - 381 = 2205, the report figure exactly.

**AND THE THREE THINGS I WAS TOLD RATHER THAN LEFT TO FIND ARE ALL TRUE.**
The suite was red at `2d4f7fb` before the round began; the CZ0 commit message
does carry the refutation of its own first command, in capitals, with the
corrected command beside it; and the revision-26 corruption left no trace in
history. Telling me was the right call and it cost the round nothing.

---

**R475. (BLOCKS -- (b) the counter and how it is injected, AND (c) what the
gate first claim establishes. The gate detection threshold degrades linearly
with the model span on rotational degrees of freedom, the shipped counter is
injected on the one class where it does not, and nothing in the suite can
see this.)** `tests/verification/rung1/test_rigid_body_modes.py`
`_analytic_rigid_body():159-181`, `residual_exactness():229-253`, the
injection at `:454-459`, and `docs/closure/F2-step5.md` sections 1 and 4.

```
code :252  worst = max(worst, ||k @ v|| / (scale * ||v||))
code :177-180  a rotation column carries LEVER ARMS on translational dofs
           and 1.0 on rotational dofs
judge SO ||v_j|| FOR A ROTATION COLUMN GROWS WITH THE SPAN OF THE MODEL, and
     the quantity it divides shrinks by the same factor. The three
     translation columns carry 1.0 and do not move.
code :458  k[0, 0] += size * scale        -- the residual counter injection
judge k[0,0] IS A TRANSLATIONAL DOF. The counter samples the one class whose
     threshold is span-invariant.

cell ONE VARIABLE, WHICH DOF THE SAME DEFECT LANDS ON. Everything else held:
     same element, same section circular_tube D=0.6 t=0.012, unit=1 metres
     THROUGHOUT -- no unit change anywhere, so this is not the conditioning
     story the corpus already tells. Defect = the shipped counter own
     mechanism, k[d,d] += 1e-14 * max|K|, d=0 then d=3.
rule the shipped assertion: residual_exactness(k, model) > RIGID_MODE_
     EXACTNESS = 1e-15, or seventh_over_epsilon(k) < RIGID_MODE_BOUND
cmd  the two shipped functions over a span ladder built by the shipped
     builder test_rigid_body_corpus._build, stretch = 1, 10, 100, 1e3, 1e4
out  span    k[0,0] 1e-14                k[3,3] 1e-14
     4 m     4.484e-15 (4.48x)  RED      2.149e-15 (2.15x)  RED
     40 m    4.416e-15 (4.42x)  RED      2.541e-16 (0.25x)  GREEN -- MISSED
     400 m   4.487e-15 (4.49x)  RED      7.103e-17 (0.07x)  GREEN -- MISSED
     4 km    4.432e-15 (4.43x)  RED      8.834e-17 (0.09x)  GREEN -- MISSED
     40 km   4.462e-15 (4.46x)  RED      9.742e-17 (0.10x)  GREEN -- MISSED
judge AT 400 m THE DEFECTIVE FRAME READS 7.103e-17 AND THE CLEAN ONE READS
     7.103e-17. The gate cannot distinguish them at all.

judge AND THE SECOND HALF DOES NOT CATCH IT EITHER, which is the thing that
     turns a weakness into a finding.
cmd  seventh_over_epsilon and zero_modes_under_the_bound on every cell above
out  l7/eps unchanged to four figures at every span, below_bound = 6 at all
     ten cells, largest_rigid_eigenvalue 0.40 at the 400 m rotational cell
     against 7.61 at the translational one. CLAIM B GREEN EVERYWHERE.
cmd  the same at 400 m, walking the defect size up
out  1e-14 -> GATE GREEN   1e-13 -> GATE GREEN   4e-13 -> GATE GREEN
     1e-12 -> GATE RED
judge A DEFECT 40x THE SHIPPED COUNTER PASSES THE WHOLE OF G2.1 GREEN at a
     span the repository own corpus already contains.

judge I CHECKED MY OWN INJECTION FOR THE OPERATING-POINT DEFECT before
     writing this. size * max|K| adds the same ABSOLUTE stiffness to dofs
     with different units and different natural magnitudes, so the cell
     above is not yet like-for-like. Re-measured as a fraction of the
     diagonal the defect lands on, bisected, either half red:
cmd  bisected edge of k[d,d] += f * k[d,d], f solved to the gate boundary
out  span     k[0,0]      k[3,3]      edge tx (rel)  edge rx (rel)  rot/tx
     4 m      1.863e+09   3.527e+08     3.2629e-15     3.6420e-14   11.2x
     40 m     1.801e+08   3.925e+07     3.3930e-15     2.7590e-13   81.3x
     400 m    1.800e+07   3.930e+06     3.2082e-15     2.7548e-12    859x
     4 km     1.800e+06   3.930e+05     3.4281e-15     2.7517e-11   8.0e3
     40 km    1.800e+05   3.930e+04     3.3149e-15     2.7506e-10   8.3e4
judge THE FINDING SURVIVES THE FAIR MEASURE AND SHARPENS. The translational
     edge is 3.3e-15 at every span -- flat over four decades, which is the
     gate working. The rotational edge is 11x worse at the shipped frame and
     859x worse at 400 m, and it scales exactly with the span.
out  the absolute view: the rotational edge is about 1.08e-05 N.m/rad at
     4 m, at 400 m and at 40 km -- a CONSTANT absolute stiffness. The
     translational edge scales with the structure: 6.1e-06, 5.8e-08 and
     6.0e-10 N/m.
judge SO THE GATE CARRIES AN ABSOLUTE THRESHOLD ON A DIMENSIONAL QUANTITY in
     the rotational direction, which is the tolerance-form defect the
     recorded guards name, hidden inside a quantity whose clean value IS
     span-invariant -- 6.7e-17 to 9.7e-17 over the same ladder -- and which
     therefore looks correct from every angle the suite has.

judge WHY THIS IS (b) AND NOT ONLY PROSE. CZ0 makes a tolerance value or the
     form of one, INCLUDING A COUNTER AND HOW IT IS INJECTED, blocking. The
     counter injection site is the whole of the finding: move it from k[0,0]
     to k[3,3] and the same constant measures a threshold three orders of
     magnitude different at the platform own scale.
judge AND WHY IT IS (c). docs/closure/F2-step5.md:42-45 reads "Claim A is
     exact and unconditional, and it is the one that would catch a defective
     element. Claim B is conditional on the frame conditioning and is the one
     that goes undecidable." Claim A POWER is conditional on the span,
     measured above, and Claim B does not cover the gap. The section 4 row
     "RIGID_MODE_EXACTNESS_COUNTER_DEFECT | injected, asserted red, 4.54x
     past a bisected detection edge" is a figure for one dof class at one
     span, published without either.
judge WHAT THIS IS NOT. IT IS NOT AN ELEMENT DEFECT. I ran 42 configurations
     -- rigid translation of the whole frame out to 1e8 m, wall thickness
     from 1e-6 m to D/2, subdivision to 64, coplanar node sets,
     near-collinear braces, nu from 0 to 0.49999, E over twelve decades,
     span over eight -- and the clean residual never once exceeded 1.5e-16,
     a seventh of the ceiling. Fifty-three rounds have found no element
     defect and this round found none either. What it found is that the gate
     proves less than the closure artifact says it proves, in a direction
     nobody had looked.
```

  **Closed when** (i) the residual half carries a counter injected on a
  ROTATIONAL degree of freedom as well as a translational one, with its
  detection edge measured at more than one span, or the quantity is
  renormalised so the two classes share a threshold; and (ii)
  `docs/closure/F2-step5.md` sections 1 and 4 say which dof class and which
  span every published sensitivity figure was measured at. **Carried by name
  into F2-rung2 and blocking there.** Until (i) lands, a rung-2 result is
  interpretable with the limit stated, not without it -- G2.1 is green and
  the element is sound; what is unproven is the rotational direction at span.

---

**Closure items (CZ0). None of these is (a), (b), (c) or (d). They go into
the step closure list; they are not re-reviewed item by item.**

**R476. A coincident tip node raises `ZeroDivisionError`, where every other
invalid geometry raises a validated `ValueError`.** Measured through the
shipped builder: tip = 1.9,1.1,2.8 -- node 4 on top of node 3, a zero-length
member -- gives `ZeroDivisionError: float division by zero` out of the
length computation, while `Section.circular_tube(0.6, 0.3)` gives
`ValueError: invalid tube: D_outer=0.6, t=0.3. The wall must be positive`.
It raises rather than defaulting, which is the non-negotiable, and the class
of error is the finding, not the fact of it. Closed by a validated refusal
naming the two nodes.

**R477. G2.1 applies no admission check, and G2.2 does.**
`tests/verification/rung1/test_corpus_configurations.py` overrides `expect`
for any member below `BEAM_ADMISSION_L_OVER_D` because no beam element
describes it; `test_rigid_body_corpus._build` never calls
`assert_beam_admissible`. Measured: tip = 1.900000001,1.1,2.8 is a member at
L/D = 2.5e-9 and G2.1 reports decided, residual 4.64e-17. The gate claim is
still true there -- the finding is that the two rungs disagree about what a
member is, and only one of them says so.

**R478. Two coincident, unconnected nodes are certified.** tip = 0,0,0 puts
node 4 exactly on node 0 with no element between them; G2.1 reads decided,
l7/eps = 1.0e13, residual 5.52e-17. That is a modelling error a reader would
want refused at the model, not at the gate. Both shapes are in the corpus now.

**R479. R383, still.** Ten determinism legs green at `125cee1` for the second
round running, 13 steps each, and no table in the repository carries the
result. `python scripts/ci_section.py --legs`.

**R480. The `.git/worktrees/` administrative directory holds about 70 stale
entries** -- tree1..tree51, wt..wt15, wt651, wt1824 -- from earlier rounds
scratch worktrees, and `git worktree prune` cannot remove them under
OneDrive. Nothing in the working tree is affected and `git status` is clean.
Recorded so it is not rediscovered as a mystery.

**R481. `tests/test_report_carried.py:1385-1404` asserts ten times that a
defect is NOT caught, and I am asked whether that certifies it. It does not,
and the construction is right.** I checked all twelve transcriptions against
my own corpus `shape=` descriptions line by line and all twelve are faithful
-- including `the_two_non_green_rows_deleted_and_the_green_one_kept`, which
correctly strips the failing-test blocks along with the rows, and
`a_0a_table_copied_forward_from_the_previous_round_unchanged`, which is
`_BASE` under a later verdict number and is the hardest of the twelve to
transcribe honestly. The equality assertion `refused == must_refuse` makes a
False row a CHANGE DETECTOR, not a certificate: closing the hole turns the
row red and the fix is a deliberate False-to-True edit, which is a
tightening and not a widening. What it costs is that the ten rows must be
edited in the same commit as any repair, so a reader of that commit sees ten
assertions flip -- which is the loud outcome, not the quiet one. **The one
thing I would change** is the wording at `:1386`, "`must_refuse` is the
corpus own `measured=` field": it is the reviewer recorded measurement, and a
future round that fixes a guard without updating the corpus would make that
sentence false while the suite stayed green. Say "the outcome measured at
this commit" instead.

## On the criterion itself (CZ0), once, as asked

**I do not disagree with it.** Six rounds of correct prose findings against a
falling coverage number is a real measurement and the response is
proportionate. Retiring the truth of a published figure or sentence as a
blocking head is the right call: it was earned, it stopped paying, and the
findings it produced are still written down.

**One qualification, and it is the only one.** The three-verdict clock counts
rounds, not scrutiny. R475 was found at the third verdict, so it has had zero
rounds of anybody attention but mine, and it closes a step whose closure
artifact publishes two sentences it refutes. The mechanism CZ0 gives for this
-- carry it by name, blocking, into the next step -- is adequate **if the
answering commit is the next step first and not its last.** If the rule ever
produces a step that closes carrying a (b) or (c) item that is then answered
at the end of the following step, the clock has bought throughput by
deferring the one class of finding it was written to keep.

Nothing here needs another round. It needs R475 answered early in F2-rung2.

## Tolerances touched

**NONE. No constant was created, retired, or moved. `floatfea/` received not
one byte, comments included.**

```
cmd  git diff 2d4f7fb..125cee1 -- floatfea/
out  (EMPTY)
cmd  git diff 2d4f7fb..125cee1 -- floatfea/tolerances.py
out  (EMPTY)
cmd  python -c "import floatfea.tolerances as t; print(t.RIGID_MODE_EXACTNESS,
     t.RIGID_MODE_BOUND, t.RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
     t.RIGID_MODE_BOUND_COUNTER_DEFECT)"
out  1e-15  199.526231496888  1e-14  1e-13
judge ALL FOUR MATCH docs/closure/F2-step5.md section 1 TO THE DIGIT. The
     retired RIGID_MODE_FLOOR and RIGID_MODE_GAP are still importable and
     marked rather than deleted, as section 8 says, and a grep over
     floatfea/ outside tolerances.py finds NO use of either -- the gate
     reads RIGID_MODE_BOUND.
cmd  my whole-suite run includes the shipped literal scanner over tests/
out  2581 passed at 125cee1 -- no undeclared literal entered tests/ and
     nothing was added to tolerance_marker_exemptions.txt.
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

**But R475 is a tolerance finding without a tolerance change**, and that is
worth saying in this section rather than only above: the value 1e-15 is not
what is wrong. Its counter injection site is, and the counter is the part of
a tolerance entry CZ0 names explicitly.

## Adversarial corpus (BE3)

**19 new entries, all unseen by the implementer, committed separately at
`b49960f`. `tests/corpus/g21_rigid_body_frames.txt`, 126 to 145.**

Every field is measured through the shipped builder,
`test_rigid_body_corpus._build`, so the consuming test poses the frame the
line describes and nothing was transcribed by hand. Four are the span ladder
R475 rests on and carry a new field, `rot_dof_detection_edge`, read by
nothing.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
     tests/verification/rung1/test_rigid_body_modes.py -q   (at b49960f)
out  161 passed -- all 19 new frames pass both halves of G2.1
cmd  python -m pytest tests/ -q -k "figure or figures or stale or corpus"
out  1 failed, 1490 passed -- test_the_generated_figures_are_not_stale,
     because rigid_mode_corpus_frames moves 126 to 145 and
     docs/milestones/F2_figures.md is canonical-on-CI
judge THAT RED IS THE GUARD WORKING and the closing path is a CI
     regeneration. It is at MY commit, not at the reviewed one.
```

**Coverage measurement, and this round it is not a count of shapes -- it is
the gate own counter against the cell that separates the two dof classes.**

* **The shipped residual counter detects 5 of 5 translational cells and
  1 of 5 rotational cells** across the span ladder, at its own size. The one
  it detects is the shipped 4 m frame, the only configuration the counter
  was ever measured at.
* **0 of 5 rotational cells are detected by the second half of the gate**,
  which is what makes the miss a miss rather than a division of labour.
* **19 of 19 new frames pass**, which is the right answer and is the
  measurement that says the element is sound over a domain 15 per cent
  larger than the one it had.

**LAST ROUND THE NUMBER WAS 1 OF 19 AND I WAS ASKED TO SAY IF IT MOVED. IT
MOVED, AND NOT BY THE APPARATUS IMPROVING.** It moved because I stopped
measuring the report guards and measured the gate. CZ0 froze the apparatus
the previous two rounds corpora were aimed at, so a third batch of report
shapes would have measured a frozen target and returned a foregone zero at
the cost of a transcription round. I added none, deliberately, and say so
here rather than letting an absent number read as a clean one.

**That redirection is the strongest argument for CZ0 in this verdict.** Two
rounds of corpus work against parsers found 3 of 41 shapes and no defect.
One round against the gate found R475.

## Next step opens when

**Step 5 CLOSES at `125cee1`.** Third verdict under CZ0. Rung 1 is green in
my run -- 2581 passed, 0 failed, 0 skipped -- and on Linux at the commit I
judge, 13 jobs including ten determinism legs. Every item verdict 52 held is
answered. `floatfea/` carries no change for the ninth round.

**F2-rung2 opens, and it opens carrying one BLOCKING item by name:**

1. **R475** -- the residual counter is injected on a translational degree of
   freedom, the gate rotational sensitivity degrades linearly with span
   (859x at 400 m, measured, on the dimensionally fair measure), Claim B
   does not cover it, and `docs/closure/F2-step5.md` sections 1 and 4
   publish the opposite. **Class (b) and (c).** It blocks F2-rung2 and it
   should be answered in that step FIRST commit -- before a rung-2 number is
   interpreted, not after.

**Closure items into step 5 closure list, fixed once, not re-reviewed:**
R476 (ZeroDivisionError on a coincident node), R477 (G2.1 has no admission
check while G2.2 does), R478 (coincident unconnected nodes certified), R479
(the determinism legs are green twice and banked nowhere), R480 (about 70
stale worktree entries), R481 (one sentence at
`tests/test_report_carried.py:1386`), and the 48 items frozen in
`docs/milestones/F2a.md` section 7.

**One thing the closure artifact should gain before F2 closes**, and it is
not a new measurement: section 5 records where the apparatus stopped and is
right to. It should also record where the apparatus WORKED -- the span
ladder in `tests/corpus/g21_rigid_body_frames.txt` is the first reviewer
artefact this milestone that moved a gate finding rather than a sentence.

**Fifty-three rounds have found no element defect and this round found none
either** -- 42 adversarial configurations, clean residual never above
1.5e-16 against a 1e-15 ceiling. It still means not yet contradicted:
ladder 5 has printed `OK -- 0 directories ran` every time it has run, and
V5.1 against CalculiX is the witness that has not spoken. What changed this
round is that the gate own power was measured for the first time in a
direction its counter does not sample, and it is smaller than published.
