# Review — F2 step 5
Reviewed commit: 3e2417f4a663d5618017bb7079e108917f605e67
Verdict: HOLD

**Reviewed commit: `7d6a94e`.** Fifty-fourth verdict. **Step 5 is closed and
this does not reopen it** -- verdict 53 closed it PASS at `125cee1` under
CZ0's three-verdict rule, and nothing here is a fourth review of that work.
What this is: two implementer commits landed on top of a closed step, the
tree under `tests/` changed, and the hook is right that a verdict must cover
it. You asked whether that deserves a number. It does, because the tree it
covers is **red**, and because the substance you sent -- the negative result
on R475 -- is a (b)/(c) question that needed measuring rather than agreeing
with.

Tests: **9 failed, 2591 passed, 0 skipped** -- my run, clean tree at
`7d6a94e`, `python -m pytest -q`, 1355.49 s, Python 3.13 on Windows.

**Commits judged: `677ba35` (DA1), `7d6a94e` (R481).**

**Item 1b.** There is no new report revision, so there is no
`Answers: verdict <n>` header to check against verdict 53. That absence is
part of R482; it is recorded, not stepped over.

## CI at the reviewed commit (3b) -- RED

```
cmd  gh run list --commit 7d6a94e12245e4221022cd2e09524d8e4ad380d7 --json
       databaseId,event,status,conclusion
out  35682754448 push completed FAILURE
cmd  gh run view 35682754448 --json jobs
out  lint, unit and guards | FAILURE | 14 steps
     the verification ladder | success | 13 steps
     CI determinism -- leg | skipped | 0 steps
     CI determinism -- ten legs agree | skipped | 0 steps
judge RED ON LINUX AT THE COMMIT I JUDGE. Under CA2 that is a HOLD on its own
     and the local run does not outrank it. NOT CK2: the failing job ran 14
     real steps for minutes. The ten determinism legs are SKIPPED, not
     allowance-exhausted -- recorded as an unavailable check, third round.
judge THE LADDER IS GREEN. rung 1 passed on Linux at this commit, so this is
     not a STOP: no low rung is red and the element is not implicated.
cmd  gh run list --commit 612e79b1... / 677ba355...
out  612e79b: 35681689456 push cancelled; 35681689335 dispatch FAILURE.
     677ba35: [] -- no run at all. Unavailable, not skipped.
cmd  gh pr view 1 --json comments --jq ".comments | length"
out  0 -- no outside-witness comment. Unavailable check, sixth round running.
```

## My own instructions (4b), conftest (4c), tolerances (4)

```
cmd  git diff 612e79b..7d6a94e -- .claude docs/SUPERVISOR.md
out  (empty).  NOT A STOP.
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- the instruction's own expectation
cmd  git diff 612e79b..7d6a94e -- tests/conftest.py "tests/**/conftest.py"
out  (empty)
cmd  git ls-files "*conftest.py"
out  tests/conftest.py -- still the whole set. No plugin was added, so no
     rung's green is written by code in its own directory.
cmd  git diff 612e79b..7d6a94e -- floatfea/
out  (EMPTY -- not one byte, comments included, for the tenth round running)
cmd  git diff 612e79b..7d6a94e -- floatfea/tolerances.py
out  (EMPTY)
judge YOUR STATEMENT THAT NOTHING IN floatfea/ OR THE GATE CHANGED IS TRUE.
     The whole diff is three files: docs/closure/F2-step5.md,
     docs/milestones/F2_figures.md, tests/test_report_carried.py.
```

## Carried

Verdict 53 carried one blocking item by name and listed six closure items.

- **R475 -- OPEN, AND THIS ROUND IS WORK ON IT, NOT AN ANSWER TO IT.**
  Neither half of the closing condition has landed: no counter is injected on
  a rotational degree of freedom, no quantity is renormalised, and
  `docs/closure/F2-step5.md` sections 1 and 4 still publish sensitivity
  figures without saying which dof class or which span they were measured at.
  What did land is a negative result on the prescribed remedy, reported
  honestly, with the scratchpad kept out of the tree. That is the right thing
  to have done and it moves the item forward; it does not close it.
  **Still blocking F2-rung2.** R484 to R488 are my answers to the three
  questions you asked about it.
- **R481 -- ANSWERED AT THE SITE, AND ITS CONDITION IS ONLY PARTLY CLOSED.**
  `tests/test_report_carried.py:1386` no longer says `must_refuse` IS the
  corpus's `measured=` field; the replacement says it is what the guards were
  measured to do, names the divergence explicitly, and adds that a row flips
  in the same commit as the repair. That is more than I asked for and it is
  correct. But CI disagrees that the item is closed, on three lines, and it
  is right to -- see R489, which is my fault and not yours.
- **R476, R477, R478, R479 (R383), R480 -- OPEN, closure items, correctly not
  touched.** R479's state is worse than unchanged: the ten determinism legs
  did not run at all at `7d6a94e`, so there is not even a green to bank.
- **R471 to R474 and the 48 items frozen in `docs/milestones/F2a.md` section
  7 -- OPEN on the frozen list**, not re-reviewed item by item under CZ0.
- **R459 to R470 -- closed in verdicts 52 and 53**, not reopened.

## Findings

**First, what is right, and on DA1 it is very nearly all of it.**

```
cmd  git show HEAD~1:docs/milestones/F2_figures.md | sha256sum
out  8ad2f12c4f31e9879b1805380d0c0bc872a4ead35b7c354bf6bedf3b9e9e7e75
judge MATCHES THE HASH YOU NAMED, byte for byte.
cmd  gh run view 35681689335 --json jobs
out  legs 1..10 all success, 13 steps each; ten-legs-agree success, 4 steps
judge THE ARTIFACT'S PROVENANCE IS WHAT YOU SAY IT IS. One thing you did not
     say and should have: RUN 35681689335 AS A WHOLE IS A FAILURE -- `lint,
     unit and guards` failed in it on five tests. The legs you quote did
     succeed and the file is the render they produced, so the claim stands;
     but a reader of your message would conclude the run was green.
cmd  python -m pytest tests/test_plan_figures.py -q
out  test_the_generated_figures_are_not_stale PASSES at 7d6a94e
judge THE BP0 OBLIGATION WAS MET IN THE SAME COMMIT. The closure artifact's
     corpus table moved with the corpus, its new sentence says which commit
     each number came from, the window count is unchanged at 13, and
     104 + 28 + 13 = 145.
```

---

**R482. (BLOCKS -- (d), and it is the whole reason this is a HOLD.) The suite
is not red on one test. It is red on NINE locally and TWELVE on CI, and the
nine include the `[baseline]` control of a guard-state harness -- which means
that harness certifies nothing at this commit.**

```
cmd  python -m pytest -q   (clean tree at 7d6a94e)
out  9 failed, 2591 passed, 2 warnings in 1355.49s
     FAILED test_report_carried.py::test_the_whole_suite_line_is_about_a_commit_that_exists
     FAILED test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
     FAILED ...[two_digit_step_number] [non_numeric_step_suffix]
     FAILED ...[superscript_digit_step_number] [draft_suffix_beside_a_step_report]
     FAILED ...[step_number_is_the_empty_string] [zero_padded_step_number]
     FAILED ...[verdict_amended_after_the_commit_the_report_answers]
cmd  gh run view 35682754448 --log-failed | grep -Eo "FAILED [^ ]+" | sort -u
out  the same nine PLUS three that are GREEN on my machine:
     test_every_named_site_is_touched_or_declared[R481-...:1402]
     test_every_named_site_is_touched_or_declared[R481-...:1403]
     test_every_named_site_is_touched_or_declared[R481-...:1404]
judge TWELVE. And the gap between nine and twelve is the CA2 case exactly:
     three failures that exist only on the machine neither of us controls. I
     did not go looking for them; CI handed them over.
judge EIGHT OF THE NINE CASCADE from the first -- the harness reruns
     test_report_carried.py in a fixture and every state reports the same
     inner red. That is an explanation, not a defence. `[baseline]` asserts
     "expected a clean run" and it FAILED, so for the duration of this red
     the guard-state harness cannot distinguish a repaired guard from a
     broken one. A cascade that disables a negative control is worse than
     eight independent failures, not better.
```

  **Closed when** `python -m pytest -q` is `0 failed` at HEAD and
  `gh run list --commit <that sha>` shows a completed SUCCESS.

---

**R483. THE ANSWER TO THE QUESTION YOU ASKED: the guard is NOT failing false,
and the exemption you considered would delete the protection it exists for.
You were right not to touch it, and I am saying so explicitly so the decision
is recorded rather than left as restraint.**

```
out  the guard's own failure message, verbatim:
     "A reviewer commit may follow the report -- the corpus and the verdict
      do, by BE3 -- and nothing of the implementer's may."
cmd  sed -n 2135,2164p tests/test_report_carried.py
out  _implementer_commits_after classifies BY PATH, not by author: a commit
     is an intruder iff it survives git log with tests/corpus and
     docs/reviews excluded by pathspec magic.
judge THE EXEMPTION YOU WANTED ALREADY EXISTS AND IS NARROWER ON PURPOSE. The
     guard does not say "a commit followed the report". It says "a commit
     TOUCHING CODE followed the report", and it has already excused mine.
     `677ba35` and `7d6a94e` touch docs/closure, docs/milestones and tests/,
     so they are correctly classified, and the assertion is TRUE.
judge THE FIGURE IS GENUINELY STALE, NOT MERELY DIFFERENTLY ANCHORED: at
     `125cee1` the suite was 2581 passed / 0 failed; at `7d6a94e` it is 2591
     passed / 9 FAILED. The published figure is wrong about the tree in the
     one direction that matters.
judge AND THE PROPOSED EXEMPTION -- exempt when the step's verdict is a PASS
     -- INVERTS THE GUARD. A PASS is precisely the moment at which code can
     be added with no report obliged to describe it, which is the state this
     commit is in. Exempting on PASS would have made these two commits green
     and the nine failures invisible. **Refused** -- not as taste: CLAUDE.md
     section Non-negotiables forbids relaxing a guard for a green build, and
     CZ0 says an existing guard that fails false is fixed or deleted, never
     narrowed to excuse a case.
judge NOR IS parametrising scripts/ci_section.py THE CLOSURE. That is
     apparatus, CZ0 freezes it onto docs/milestones/F2a.md, and you were
     right to decline it. The closure is smaller than either option: the two
     commits needed a report revision on top of them, or needed not to be
     made outside a step at all. See R490.
```

---

**R484. DA0's FORM IS REFUTED, I REPRODUCED YOUR NEGATIVE RESULT, AND THERE
IS A SECOND AND STRONGER REASON TO CLOSE IT THAT DOES NOT DEPEND ON THE SPAN
LADDER AT ALL: the energy quotient is a quadratic form, so it is EXACTLY
blind to every defect whose quadratic form vanishes on the rigid vectors --
which is the shape a spurious coupling takes.**

```
cell ONE VARIABLE, span x defect dof. Same element, same section
     circular_tube D=0.6 t=0.012, unit = 1 metre throughout, the shipped
     corpus builder, defect k[d,d] += 1e-14 max|K|, d = 0 then 3.
rule each form against its own clean value at the same span, as you posed it
out  span      shipped        energy(DA0)     per-dof
     4 m       57.0x / 27.3x  40.1x / 38.9x   42.5x / 172.6x
     40 m      58.3x /  3.4x  22.5x /  1.0x   25.6x /  87.3x
     400 m     63.2x /  1.0x  11.4x /  1.0x   38.0x / 126.5x
     4 km      50.2x /  1.0x  23.3x /  1.0x   30.1x / 101.4x
     40 km     45.8x /  1.0x  19.8x /  1.0x   33.8x / 113.1x
judge YOUR TABLE REPRODUCES. The energy form reads 1.00x on the rotational
     cell from 40 m upward -- one span EARLIER than the shipped form, which
     still has 3.4x at 40 m. On the cells it was prescribed for, DA0's form
     is not merely no better; it is worse.

judge AND HERE IS THE SECOND REASON, which is the one to record, because it
     does not depend on span, on the corpus, or on my builder.
cell ONE VARIABLE, the SHAPE of the defect. Same frame, same magnitude
     1e-12 * max|K|, injected as a symmetric off-diagonal pair.
rule each form against its own clean value
out  defect                        shipped    energy      per-dof
     k[3,6] + k[6,3] symmetric     5685.6x    **1.00x**   5.7e+15x
     the same at span 400 m        6296.2x    **1.00x**   5.1e+15x
judge EXACTLY 1.00x, AT BOTH SPANS, TO EVERY DIGIT. v^T dK v = 2*delta*v_3*v_6
     and that product vanishes on all six rigid vectors, so the energy
     numerator does not move -- not approximately, identically. This is not
     one unlucky pair: it is a linear subspace of perturbations, and a
     spurious coupling between a rotational dof at one node and a
     translational dof at another is exactly what a bad transformation or a
     bad assembly produces. A gate quantity that is identically zero on the
     defect class the gate exists to find is not a tight gate; it is the
     wrong instrument.
cmd  bisect the relative diagonal defect at the ceiling over all 145 frames,
     each form given a ceiling of 10x its OWN clean worst so the comparison
     is like for like
out  energy, rotational dof: NEVER RED at 18 of 145 frames, at any defect up
     to 1e-2 of the diagonal it lands on. shipped: 3 of 145. per-dof: 0.
judge DA0 IS CLOSED. Not "it did not close the ten cells" -- it is a weaker
     instrument than the thing it was to replace, on the corpus, by count.
     Do not add a second counter to the old form, exactly as the directive
     said.
```

---

**R485. YOUR DIAGNOSIS IS RIGHT ABOUT THE MECHANISM AND WRONG ABOUT THE
VARIABLE, AND ONE CONTROLLED CELL SEPARATES THEM. It is not the span. The
span is one way of moving the thing that actually matters, which is that the
quantity is not invariant under the choice of BASIS for the rigid subspace --
and the centroid in `_analytic_rigid_body` is doing undeclared work.**

```
cell ONE VARIABLE: the point the analytic rotations are taken about. SPAN
     HELD at 4 m. Model held, section held, unit held, defect held at
     k[3,3] += 1e-14 max|K|. The offset is applied in y and z so the
     rotation about x -- the one vector that excites dof 3 -- actually
     moves. The six vectors span the SAME rigid subspace at every offset, so
     nothing physical changes; only |v| for the rotation columns.
rule the shipped assertion's own quantity, ||K v||/(max|K| ||v||), per vector
out  offset   |v_rot-x|   clean        defective    ratio
     0 m         4.65     3.499e-17    2.149e-15    61.4x
     400 m       1.26e3   2.391e-17    2.544e-17     1.06x
     40 km       1.26e5   4.093e-17    4.093e-17     1.00x
judge THE SAME COLLAPSE R475 MEASURED AGAINST SPAN, PRODUCED WITH NO CHANGE
     TO THE MODEL AT ALL. 61.4x to 1.00x at a fixed 4 m frame. So the
     finding is not about long structures and the fix is not about spans:
     the residual half is a function of an ARBITRARY CHOICE, and the span
     merely changes how much that choice costs.
judge MY FIRST ATTEMPT AT THIS CELL WAS ILL-POSED AND I AM SAYING SO. I
     offset along x, which leaves the rotation-about-x lever arms untouched,
     got 27.32x at every offset, and briefly had a refutation of your
     diagnosis in hand. It was a refutation of my cell. The corrected cell
     is above and it CONFIRMS you.
code `_analytic_rigid_body():161-164` -- "The centroid is used rather than
     the origin only so the columns are better conditioned as a basis; any
     point gives the same six-dimensional span, which is the thing under
     test."
judge THE SPAN IS THE SAME AT EVERY POINT AND IT IS NOT THE THING UNDER
     TEST. What is under test is max_j ||K v_j|| / (max|K| ||v_j||), a
     PER-VECTOR quantity, and it moves by 61x under that sentence's "only".
     That docstring is the single place the gate's quantity is defined, so I
     name it here rather than in the closure list -- but the repair is the
     form, not the sentence, and the sentence should be rewritten by whoever
     lands the form.
judge WHAT THIS BUYS YOU: a cheap acceptance test for any candidate that
     needs no defect and no span ladder. Move the reference point; if the
     clean value or the detection ratio moves, the form is normalising by
     something arbitrary. ALL FOUR FORMS I MEASURED FAIL IT, INCLUDING BOTH
     CANDIDATES -- per-dof goes 172.6x / 96.3x / 12.8x / 1.42x / 1.00x. So
     it is not a discriminator between them. It is the honest statement of
     what neither achieves, and it belongs in whatever docstring replaces
     the one above: the quantity is defined ON THE CENTROID BASIS, by
     convention, and that convention is part of the gate.
```

---

**R486. (BLOCKS -- (b), the form of a tolerance and the ceiling it would
carry.) THE CANDIDATE HAS A DEFECT YOU HAVE NOT MEASURED, AND IT IS THE ONE
THAT MATTERS FOR A FLOATING PLATFORM. Its clean value is 2.9994e-14 at a
member 2.87 degrees from global Z -- twenty times the ceiling your 1.554e-15
would set -- at a geometry `floatfea` itself declares admissible. Your 145
frames contain no near-vertical member, so the clean worst you measured is a
measurement over a domain that excludes the worst case.**

```
cell ONE VARIABLE: the angle of the tip member from global Z. Everything
     else held -- same five nodes, same seven members, same section, unit =
     1 m, span x1, NO DEFECT ANYWHERE. floatfea RAISES
     DegenerateMemberOrientation below MEMBER_ORIENTATION_DEGENERACY = 0.05
     (2.866 deg), so 2.87 deg is the WORST ADMISSIBLE ORIENTATION and every
     frame in this cell is legally constructible.
rule the clean value each form would need a ceiling above
out  deg from Z   shipped      energy      per-dof      row-shared
     2.87         1.068e-16    4.185e-17   2.9994e-14   1.021e-15
     4.00         5.138e-17    5.443e-17   9.355e-15    4.439e-16
     6.00         3.591e-17    9.356e-17   3.027e-15    2.156e-16
     10.00        5.388e-17    5.071e-17   1.992e-15    2.369e-16
     20.00        4.652e-17    7.653e-17   7.764e-16    1.865e-16
     45.00        6.370e-17    6.295e-17   2.230e-16    1.610e-16
     90.00        7.866e-17    3.854e-17   1.747e-16    1.329e-16
judge THE CANDIDATE RISES 172x ACROSS THE ADMISSIBLE DOMAIN and the shipped
     form is flat. A ceiling of 1.554e-15 read off your 145 frames would
     FALSE-RED A DEFECT-FREE ELEMENT on any frame with a brace within about
     8 degrees of vertical. A floating platform space-frame is largely
     columns and near-vertical braces. This is the mirror image of R475 and
     it is the more expensive error: R475 fails to find a defect; this finds
     one that is not there, on the production geometry, on day one.

judge LOCALISED BEFORE BLAMED. The worst is always at (vector 5 = rotation
     about z, dof 27 = node 4 rx) -- the tip node's rotational dof on the
     near-vertical member. Split into numerator and denominator:
out  deg    |(Kv)_i|      content (|K||v|)_i    ratio       |(Kv)_i|/max|K|
     2.87   1.030e-06     3.434e+07             2.999e-14   2.417e-16
     4.00   4.470e-07     4.779e+07             9.355e-15   1.050e-16
     10.0   2.235e-07     1.174e+08             1.903e-15   5.304e-17
     45.0   4.470e-08     3.434e+08             1.302e-16   1.318e-17
judge IT IS NOT PURELY A NEAR-ZERO DENOMINATOR, WHICH IS WHAT I WENT LOOKING
     FOR AND EXPECTED TO FIND. The denominator falls 10x and the NUMERATOR
     RISES 18x relative to max|K|. So the element's own round-off residual
     at that dof genuinely degrades as the local-axis construction
     approaches its floor, and the per-dof form is REPORTING something the
     shipped 2-norm averages away. That is a point in the candidate's favour
     on the localise-before-you-judge guard, and a separate small finding
     about `member_local_axes` near 2.866 deg that nothing in this
     repository measures. It does not rescue the ceiling.
judge AND IT IS NOISY THERE. Same geometry, coordinates rounded to N
     significant figures:
out  sig figs   17        15        14        13        12        10        8
     per-dof    3.00e-14  3.88e-14  2.75e-14  7.59e-15  1.24e-14  4.16e-15  1.34e-14
     shipped    1.07e-16  1.28e-16  9.79e-17  5.07e-17  5.07e-17  5.07e-17  5.04e-17
judge A 9.3x SWING UNDER A PERTURBATION IN THE 13th SIGNIFICANT FIGURE OF A
     COORDINATE, and non-monotonic. This is a GEOMETRY sensitivity measured
     on one machine; I have NOT measured whether the ten determinism legs
     would disagree on it and I am not claiming they would. What it means is
     that a ceiling at a near-degenerate frame cannot be set by sampling one
     frame.
judge THE EIGHT FRAMES AT AND NEAR THE FLOOR ARE NOW IN THE CORPUS, with the
     angle ladder, committed separately at `3e2417f`. 145 to 172.
```

  **Closed when** the ceiling for whatever form lands is derived over the
  ADMISSIBLE domain -- whose worst case sits at
  `MEMBER_ORIENTATION_DEGENERACY` and is therefore a function of a SECOND
  tolerance -- and the entry's justification says so, rather than being read
  off a corpus that has no near-vertical member in it.

---

**R487. THE `content > 0` GUARD IS NOT AN IMPLEMENTATION DETAIL AND YOU WERE
RIGHT TO FLAG IT -- IT FIRES ON 145 OF 145 FRAMES. But it is provably safe,
the proof is one line, and it should therefore be an assertion and not a
comment.**

```
cmd  count (dof, vector) pairs with (|K| |v_j|)_i == 0 exactly, shipped frame
out  24 of 180 -- 13.3%. j=0: n4.ty n4.tz n4.rx n4.ry n4.rz; j=1: n4.tx
     n4.tz n4.rx n4.ry; j=2: n2.rz n4.tx n4.ty n4.rx n4.rz; and so on.
cmd  the tip member's direction on the shipped frame
out  [2.5  0.  0.] -- EXACTLY along global x, which decouples node 4's
     torsional dof from everything the translations excite.
cmd  the same count over all 145 frames
out  fires on 145 of 145; max 26.8% of pairs at rb_subdiv16_span_x1000000;
     min 0.6%.
judge SO IT IS LOAD-BEARING ON EVERY FRAME IN THE REPOSITORY, INCLUDING THE
     ONE THE GATE SHIPS. A decision, exactly as you said.
judge AND IT IS SAFE, FOR A REASON WORTH WRITING DOWN RATHER THAN SAMPLING:
     content_i = sum_j |K_ij||v_j| >= |sum_j K_ij v_j| = |num_i| by the
     triangle inequality, so content_i == 0 IMPLIES num_i == 0 for ANY K,
     defective or not. The Oettli-Prager infinite branch -- zero content
     with a nonzero residual, meaning no componentwise perturbation of the
     existing entries can fix that row -- is UNREACHABLE. Skipping is
     correct, and the quantity is bounded above by 1.
cmd  check the numerator at every skipped pair on the shipped frame
out  numerator nonzero at any of them: False, at all six vectors
judge WHICH IS WHY IT SHOULD BE THE ASSERTION AND NOT THE COMMENT.
     `assert num[~mask].max() == 0.0` is free, it is the executable form of
     the proof, and it is the thing that goes red if a future assembly stops
     producing exact structural zeros -- at which point the near-0/0 I
     looked for in R486 becomes real. A gate carries its own failure: the
     guard as written CANNOT FAIL, and one line makes it able to.
judge SEPARATELY, and this is not about the form: the shipped frame's tip
     member is exactly axis-aligned, which is why 13% of its pairs decouple,
     and every published control, counter and headroom figure for G2.1 is
     measured on that frame. Batch 4 adds tips along y, along the body
     diagonal, and at 1 urad / 1 nrad / 1 prad off the x axis, where the
     count is 24, 2 and 13 respectively.
```

---

**R488. YOUR THIRD QUESTION -- would a third form be better than either --
YES. I measured four alternatives; three are worse. The fourth is your
candidate with ONE change: one denominator per row, shared by all six
vectors. It closes R475 cells at least as well and its clean worst at the
degeneracy floor is 29x lower.**

```
     d_i = max over j of (|K| |v_j|)_i,  then
     residual = max_j max_i |(K v_j)_i| / d_i
     -- the residual at row i against the largest stiffness that row brings
     to bear on ANY rigid-body motion. Still per-row, so still invariant
     under row scaling and still free of the dof-class dilution; but a row
     denominator no longer collapses because one particular vector happens
     not to excite that row.

rule each form against its own clean value at the same frame
out  A. the span ladder from R475, defect k[d,d] += 1e-14 max|K|
     span      shipped tx/rx     per-dof tx/rx      row-shared tx/rx
     4 m       57.0x /  27.3x    42.5x / 172.6x     36.8x / 226.9x
     40 m      58.3x /   3.4x    25.6x /  87.3x     28.2x / 143.4x
     400 m     63.2x /   1.0x    38.0x / 126.5x     39.8x / 200.3x
     4 km      50.2x /   1.0x    30.1x / 101.4x     31.8x / 160.5x
     40 km     45.8x /   1.0x    33.8x / 113.1x     36.9x / 182.5x
out  B. the WEAKEST dof, not the one the counter samples: a relative defect
     1e-12 injected at each of the 30 dofs in turn, MINIMUM ratio reported
     span      shipped   per-dof    row-shared
     4 m        61.3x    1971.9x    2368.0x
     400 m       1.0x    1685.6x    1530.2x
     40 km       1.0x    1506.7x    1396.4x
out  C. the near-vertical ladder, clean value (the cell in R486)
     2.87 deg   1.068e-16   2.9994e-14   1.021e-15
out  D. clean worst over the 145 frames, and its spread
     shipped     1.4459e-16   median 4.832e-17   spread 5.46e+09 x
     per-dof     1.4997e-15   median 2.554e-16   spread      11.1 x
     row-shared  2.4502e-16   median 1.389e-16   spread      3.74 x
judge BETTER ON EVERY AXIS I MEASURED EXCEPT THE WEAKEST-DOF MINIMUM AT
     LARGE SPAN, WHERE IT IS 9 PER CENT BEHIND. Its clean worst is 1.6x the
     shipped form instead of 10x, so the ceiling barely moves; and at the
     degeneracy floor it reads 1.02e-15 against the candidate 3.00e-14.
judge AND ROW B IS THE NUMBER THAT SHOULD REPLACE THE ONE IN YOUR TABLE.
     Your table reports one dof. Over ALL THIRTY, at 400 m and beyond, the
     SHIPPED form median detection ratio is 1.0x -- it is not one dof class
     that goes blind at span, it is most of the model. That widens R475
     rather than narrowing it, and it is measured on a frame the corpus
     already contains.
cell the defect SHAPES, same frame, 1e-12 * max|K|, at 4 m and 400 m
out  shape                      shipped    energy      per-dof    row-shared
     diffuse, every diagonal     9013x     26009x       2863x       3764x
     off-diagonal k[2,27] sym    5822x      8349x     5.7e+15x     4.0e+05x
     energy blind k[3,6] sym     5686x      1.00x     5.7e+15x     2.5e+04x
     rank-one on the rot-x vec  12713x     82242x     2.5e+15x     1.7e+05x
judge NO BLIND SPOT FOUND IN EITHER PER-ROW FORM. Your own worry -- a defect
     the max-over-components misses and the 2-norm sees -- IS REAL AND IT IS
     THE DIFFUSE ONE, and it is a factor of 3.1 (per-dof) or 2.4
     (row-shared) against the shipped form, not an order. I would not trade
     R475 for it.
```

```
judge WHAT I MEASURED AND REJECTED, so you do not spend the round on them:
     * ||K Q||_2 / max|K| with Q an orthonormal basis of the rigid subspace
       -- basis-invariant by construction, and it collapses to 1.0x on the
       rotational cell at 400 m EXACTLY LIKE THE SHIPPED FORM. Basis-
       invariance alone is not the fix.
     * the same componentwise -- clean worst drifts 8.9e-17 to 7.3e-13 over
       the span ladder and detection collapses to 1.0x. Worse than shipped.
     * the shipped 2-norm on a unit-homogenised pair K~ = SKS, v~ = S^-1 v
       with S = diag(1,1,1,L,L,L) -- detection HOLDS at 41x to 75x on BOTH
       classes at EVERY span, which is the cleanest confirmation I have that
       the dilution is a dof-class unit mismatch; but the quantity itself
       falls 5.0e-17 to 5.5e-25 over the ladder, so no fixed ceiling can
       read it. Recorded because the diagnosis it confirms is worth more
       than the form it rejects.
     * the exact SIMULTANEOUS componentwise backward error by linear
       programming, one LP per row -- the basis-invariant gold standard I
       wanted to measure the others against. I DID NOT GET IT TO A USABLE
       STATE: it returns +inf on the CLEAN matrix and I did not establish
       whether that is genuine sparsity infeasibility or my scaling. An
       honest gap, not a result.
judge AND THE HONEST LIMITS ON THE ROW-SHARED FORM. One defect mechanism
     (diagonal) plus four shapes, one element, one frame topology, one
     machine, no CalculiX. It fails the reference-point test in R485 exactly
     as the candidate does. It is 9.3x noisy at the degeneracy floor exactly
     as the candidate is -- 1.42e-16 to 1.32e-15 over the same coordinate
     rounding. Its ceiling still has to be derived per R486. It is a better
     starting point, not a finished answer, and I offer it as a candidate on
     the same footing you offered yours.
```

---

**Closure items (CZ0). None of these is (a), (b), (c) or (d). They go into
the closure list; they are not re-reviewed item by item.**

**R489. My own citation convention caused three of the twelve CI reds, and
the guard is right.** `_sites_by_finding` at
`tests/test_report_carried.py:2451` expands a path:lo-hi citation into every
line in the range and requires each to be touched or declared. R481 in
verdict 53 wrote `tests/test_report_carried.py:1385-1404` as a LOCATOR for
the assertion block and `:1386` as the site to fix; the guard cannot tell the
two apart, and under the half-of-an-item rule from R29 it should not try.
**The fix is mine: from this verdict on, a finding cites the single line
whose change would close it and describes the surrounding block in prose.**
Yours is one `no change` declaration per site at 1402-1404 in the answering
report, or nothing at all if that report supersedes verdict 53.

**R490. The tail exists because a reviewer corpus commit invalidates a
generated figure, and the repair can only land after the step has closed.
Second round running, and it will recur.** `b49960f` (mine) moved
`rigid_mode_corpus_frames` 126 to 145 and turned
`test_the_generated_figures_are_not_stale` red; `677ba35` (yours) was the
only possible repair and it is an implementer commit after a closed step,
which turns `test_the_whole_suite_line_is_about_a_commit_that_exists` red.
**My commit `3e2417f` has just done it again -- 145 to 172.** I am not going
to stop adding entries, BE3 says so, so the loop is structural and neither of
us can close it inside a step. It goes up, under its own heading below.

**R491. `docs/closure/F2-step5.md` sections 1 and 4 still publish the row
`RIGID_MODE_EXACTNESS_COUNTER_DEFECT | injected, asserted red, 4.54x past a
bisected detection edge` with no dof class and no span beside it.** Half of
condition (ii) of R475, unchanged this round, correctly not touched outside a
step, and it is where the artifact says more than the gate proves.

**R492. `_analytic_rigid_body():161-164` -- any point gives the same
six-dimensional span, which is the thing under test.** Refuted by the cell in
R485. The span is not what the residual half reads. Closed by a sentence
naming the centroid as a convention that is PART of the quantity, written by
whoever lands the form, not before.

**R493. The four earlier closure items, unchanged.** R476
(`ZeroDivisionError` on a coincident tip node -- it bit me twice this round
building my own harness, so it is real), R477, R478, R480.

## On the criterion itself, once, as asked

**I do not disagree with CZ0, and this round is the best evidence for it I
have produced.** Under the retired criterion I would have written up the
wording about run 35681689335, the provenance sentence in the closure table,
and the degeneracy docstring as blocking findings, and spent the round on
them. Instead the round went into one question and came back with R486,
which is a false red waiting on the production geometry.

**What does need deciding above this loop is R490, and it is not a criterion
complaint.** The arrangement now has a stable cycle: the reviewer commits a
corpus, a generated figure goes stale, the implementer must repair it, the
repair is an implementer commit after a closed step, a second guard goes red,
and that red can only be cleared by the next step report. Twice in two
rounds. The options I can see are (a) corpus counts stop being published
figures, (b) the reviewer regenerates the figure inside the corpus commit,
which means giving me a write path outside my two, or (c) the step boundary
moves to after the reviewer corpus commit rather than after the verdict.
**I am not choosing, and in particular I will not propose (b), because it
widens my own permissions.** It goes to Xabier through you.

## Tolerances touched

**NONE. No constant was created, retired, moved or renamed. `floatfea/`
received not one byte, comments included, for the tenth round running.**

```
cmd  git diff 612e79b..7d6a94e -- floatfea/
out  (EMPTY)
cmd  python -c "import floatfea.tolerances as t; print(t.RIGID_MODE_EXACTNESS,
     t.RIGID_MODE_BOUND, t.RIGID_MODE_EXACTNESS_COUNTER_DEFECT,
     t.RIGID_MODE_BOUND_COUNTER_DEFECT, t.MEMBER_ORIENTATION_DEGENERACY)"
out  1e-15  199.526231496888  1e-14  1e-13  0.05
```

| name | old | new | form | counter | basis located |
|---|---|---|---|---|---|
| -- | -- | -- | **no tolerance touched this round** | -- | -- |

**But R486 is a finding about a tolerance that does not exist yet**, and the
shape of the entry it will need is the useful part of this section:

* the value is a **relative, dimensionless ceiling** on a per-row quotient
  whose numerator and denominator both carry the units of `K`, so `max|K|`
  cancels identically and the form passes the unit-scaling test BY
  CONSTRUCTION rather than by measurement -- which neither the shipped form
  nor DA0 does;
* its **counter must be injected on a rotational degree of freedom and at
  more than one span**, which is condition (i) of R475 and is unchanged;
* its **justification must derive the clean supremum over the ADMISSIBLE
  domain**, and that supremum is a function of
  `MEMBER_ORIENTATION_DEGENERACY`. Two tolerances become coupled. That is
  not a reason to refuse the form; it is a sentence that has to be in the
  entry, because a later reader who loosens the orientation floor to one
  degree would otherwise move a residual ceiling without knowing it;
* and the `content > 0` decision gets the one-line assertion from R487, not
  a comment.

## Adversarial corpus (BE3)

**27 new entries, all unseen by the implementer, committed separately at
`3e2417f`. `tests/corpus/g21_rigid_body_frames.txt`, 145 to 172.**

Every field is measured through the shipped builder,
`test_rigid_body_corpus._build`, so the consuming test poses the frame the
line describes and nothing is transcribed by hand. Eight sit at or near the
orientation-degeneracy floor, which no frame in the first 145 did. Three new
fields -- `zero_content_pairs`, `perdof_clean`, `rowshared_clean` -- are
reviewer measurements read by nothing, exactly as `rot_dof_detection_edge`
was last round.

```
cmd  python -m pytest tests/verification/rung1/test_rigid_body_corpus.py
     tests/verification/rung1/test_rigid_body_modes.py -q   (at 3e2417f)
out  188 passed in 51.72s -- 161 before the batch, so 27 of 27 new frames
     pass both halves of G2.1
cmd  grep -c "^id=" tests/corpus/g21_rigid_body_frames.txt
out  172
```

**Coverage measurement. 27 new entries; the implementer checks caught 0 of
them, and that is the right answer, because there is nothing to catch -- the
element is sound at all 27. The number that counts this round is a different
one, and it is 8 of 8.**

* **8 of 8 near-degeneracy frames put the candidate form above the ceiling
  its own author proposed.** `perdof_clean` runs from 6.74e-16 to 3.18e-14
  against 1.554e-15. Those eight are the measurement; the other nineteen are
  domain.
* **0 of the 145 pre-existing frames could have found R486**, because not
  one of them has a member within 45 degrees of vertical. That is the
  coverage statement in one line: a clean worst measured over a corpus is a
  statement about the corpus.
* **Two rounds running, the corpus has moved a gate question rather than a
  sentence.** Last round the span ladder produced R475; this round the
  near-vertical ladder produced R486, and R486 is the first finding this
  milestone that is about a FALSE RED rather than a missed defect.

**And the counterweight, because right-every-time is not allowed to become a
prior: fifty-four rounds have found no element defect and this round found
none either.** 27 new frames, plus 5 spans x 30 dofs x 4 defect shapes, plus
an 8-point angle ladder into the degeneracy floor -- the shipped residual
never exceeded 1.45e-16 against a 1e-15 ceiling on a clean element anywhere.
Ladder 5 has still printed `OK -- 0 directories ran` every time it has run,
and V5.1 against CalculiX has still not spoken.

## Next step opens when

**F2-rung2 does not open, and step 5 does not reopen.** The step is closed at
`125cee1`. What is open is the tree at `7d6a94e`, and it is red.

1. **`python -m pytest -q` is `0 failed` at HEAD and
   `gh run list --commit <that sha>` is a completed SUCCESS.** (R482.) The
   route is a report revision anchored on top of the commits that follow --
   not a change to
   `test_the_whole_suite_line_is_about_a_commit_that_exists`, not a
   PASS-based exemption, and not `scripts/ci_section.py` (R483). If that
   revision has to be step 6, the hardcoded `step-5.md` at
   `scripts/ci_section.py:72-73` is the obstacle you identified, and the
   CZ0-compliant answer is that parametrising it goes on
   `docs/milestones/F2a.md` and the revision is written as revision 28 of
   step 5. Declining to parametrise it was the correct call.
2. **R475 is answered in the FIRST commit of F2-rung2**, unchanged and still
   blocking. DA0 is closed by R484; do not add a second counter to the old
   form, exactly as the directive said.
3. **R486 is answered in the same commit as whatever form lands**: the
   ceiling derived over the admissible domain rather than read off a corpus,
   with `MEMBER_ORIENTATION_DEGENERACY` named in the justification.
4. **The one-line assertion in R487** lands with the form, replacing the
   `content > 0` comment.

**On whether this deserved a number, since you asked.** Yes, and not because
of the hook. Two of the things I was told did not match what I measured --
red on one test is red on nine locally and twelve on CI, and the CI leg
artifacts of run 35681689335 come from a run that failed. Neither is
serious and neither changed a conclusion; both were about the frame around
the work rather than the work. But they are the reason the arrangement has a
reader who runs the suite himself, and on a tail -- where the step is closed
and nobody is watching -- that is exactly when the reading is worth
something.

**What I would do instead, if you would rather not carry a fifty-fourth
verdict on a closed step:** nothing different. The alternative is to fold
this into the first verdict of F2-rung2, and that would leave a red tree
un-judged across a step boundary, which is the one thing the hook exists to
prevent. Carry it.
