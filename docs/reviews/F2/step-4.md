# Review — F2 step 4
Reviewed commit: 44f4e14d97f5e6b628691c812ae104ac24d76148
Verdict: HOLD
Tests: 301 passed, 0 failed, 0 skipped   (my run, `python -m pytest -q`, 0.76s)

Fifth pass, and the first in which the element rather than the instrumentation is
the main subject. **The narrowing is accepted** -- see the note below -- and
within the narrowed scope the four named corrections are real: I reproduced the
four-cell ablation through my own harness, re-measured every G2.2 figure the
report publishes, and verified by AST that no ceiling and no counter moved.

It is still a HOLD, and the first reason is the standing one. **R29 was a gated
item and half of it is untouched.** Its closing condition named
`tolerances.py:329-353` *and* `test_patch_test.py:423, 440, 446`; `70515f9` fixed
the first and `git diff e8c221a..HEAD -- tests/verification/rung1/test_patch_test.py`
is **empty**. All three strings still describe a solve that equilibrates. The
report records R29 as "answered" without distinguishing the half it did.

Three new findings are inside the narrowed scope and were found by measurement,
not by reading: the assertion that is G2.2's only guard against widening its own
ceiling admits a total loss of sensitivity (**R38**); the unit invariance the
narrowed step closes on is asserted by **no shipped test** (**R40**); and the
`1e-12` ceiling's "80x headroom" is breached at a slenderness the locked plan's
own tables discuss (**R43**).

## Carried

Every item from `docs/reviews/F2/step-4.md` (HOLD @ `2b91340`, committed
`e8c221a`), traced through `e8c221a..44f4e14` and re-measured, not taken from the
report.

- **1. R28 (gated) -- ANSWERED, by removal.** `ab23181` deletes all nine
  `_MEASURED` entries and the test that consumed them. I verified the "no ceiling
  or counter moved" claim independently of the pasted `grep`: parsing both
  revisions of `tolerances.py` with `ast` and diffing the name-to-value maps gives
  *nine* names only in the old file, all `_MEASURED`, **zero names only in the
  new**, and **zero moved values**. The replacement guard bites -- I appended
  `MATRIX_SYMMETRY_MEASURED: Final[float] = 3.7107e-17` to the file and got
  `2 failed, 22 passed`, then restored. The commit's own re-measurements check
  out: `PATCH_TEST_EXACTNESS` worst on the shipped path is `1.2513e-14` (my run,
  exactly) and both `MATRIX_SYMMETRY` sites are `0.0`. The diagnosis in the
  commit message -- that `TRANSFORM_INVARIANCE` has eight sites measuring six
  quantities, so no single number existed -- is the right reason and is stronger
  than the verdict's.

- **2. R29 (gated) -- HALF ANSWERED. Carried as R37a below and blocking.**
  `tolerances.py:308-360` is correct now and I re-derived every figure in it
  through my own harness: metre-scale worst `1.2513e-14` (file: `1.2513e-14`),
  nine-decade worst `2.004e-13` (file: `2.00e-13`), `cond(K_ff)` `9.210e+02` at
  `S = 1` and `5.983e+10` at `S = 1e-4` (file: `9.21e2`, `5.98e10`). The floor
  paragraph is rebuilt honestly: there is no single conditioning floor
  unequilibrated, and saying so rather than quoting one is the right call.
  **The three test strings the closing condition named are unchanged**:
  `test_patch_test.py:423` "the algebraic fact **the equilibrated solve rests
  on**"; `:440-441` "the solve is not unit-robust and every exactness ceiling
  above it is unit-dependent"; `:446` "if it did not, equilibration would be
  ceremony". None is true of the solve that ships. The file was not touched in
  this step at all.

- **3. R30, R31 (gated) -- MOVED to step 4a. Accepted.** Four dead counters and
  eleven `abs=` annotations, all attached to apparatus that gates nothing in
  G2.2. I re-checked that the four counters are still consumed by nothing outside
  `test_tolerance_counter_cases.py`, and that none of the eleven `abs=` sites is
  in `tests/verification/rung1/`. The move does not touch this gate.

- **4. R32 (gated) -- MOVED to step 4a. Accepted.** The scanner's coverage is not
  load-bearing on G2.2. I did not re-plant the twenty-five shapes; the report
  concedes 2 of 25 rather than disputing it, which is the right posture, and
  `F2a.md` sec. 2B replaces the design rather than patching the count.

- **5. R33 (gated) -- MOVED to step 4a, and one instance comes back.** The move is
  right for the ~30 sites outside this gate. It is **not** right for
  `test_patch_test.py:323`, which is inside G2.2 and is the only assertion that
  reddens when `PATCH_TEST_EXACTNESS` is widened. Measured and mutation-confirmed
  as **R38**. The narrowing's own carve-out applies: the apparatus does gate G2.2
  here.

- **6. R34 (gated) -- ANSWERED, and I reproduce all four cells.** I wrote my own
  sweep from the element up (assembly, equilibration switched at the
  factorisation, weighted and mixed measures) and got:

  ```
  cell         1e-4    1e-3    1e-2     0.1       1      10     100     1e3     1e4 | worst   breaches
  eq + wtd   2.0e-14 2.7e-14 2.0e-14 2.0e-14 7.9e-15 1.1e-14 3.1e-14 2.5e-14 3.2e-14| 3.19e-14  none
  -- + wtd   2.0e-13 1.6e-13 9.6e-14 1.3e-13 1.3e-14 1.2e-14 2.2e-14 6.0e-14 1.0e-13| 2.00e-13  none
  eq + mix   2.1e-11 2.8e-12 2.0e-13 2.0e-14 1.9e-15 9.9e-15 2.7e-14 6.3e-13 4.3e-12| 2.09e-11  1e-4,1e-3,1e4
  -- + mix   2.1e-10 1.7e-11 4.2e-13 1.3e-13 4.3e-15 4.2e-14 1.0e-13 2.3e-11 1.0e-10| 2.07e-10  1e-4,1e-3,1e3,1e4
  ```

  All four worsts agree to three digits with the shipped table, and the reversal
  the correction turns on is confirmed: at `S = 1e3` the mixed measure is
  `2.3e-11` unequilibrated and `6.3e-13` equilibrated, so **equilibration alone
  is what removes the kilometre breach**. `tolerances.py:339`'s breach column now
  reads `S = 1e-4, 1e-3, 1e4` for row 3, which is what I measure. The one
  sentence in the last diff that carried "alone" and "exactly" is withdrawn and
  replaced by the cells. This is the ablation guard applied correctly.

- **7. R35 (gated) -- ANSWERED.** `floatfea/assemble/system.py:9-12` now cites
  `docs/milestones/F2.md` sec. R8, and `## R8` exists at `F2.md:891`. Checked
  mechanically. The line also states that the earlier pointer resolved to
  nothing, which is the right way to leave a corrected citation. **But the same
  species is live one module over** -- `floatfea/testing.py:23-25`, **R39**.

- **8. R36 (recordable) -- carried to 4a. Accepted with one note.** The four
  literals are still there, verbatim: `io/reader.py:157, 208, 225`,
  `io/frames.py:358`. The reason given -- F1 code, and fixing it under a rule
  that is about to change would be a third pass -- is sound. It is now recorded
  in `F2a.md` sec. 5, so it has a home rather than a mention.

- **9. R37 (recordable) -- one bullet answered in the wrong place, two open.**
  `docs/instrumentation.md:727` still reads "to within **0.3%**". I re-measured
  the six deviations at the recorded thresholds -- `-0.24 / +0.31 / -0.03 / +1.00
  / -0.03 / +0.04 %`, worst `0.995%` -- so the document is wrong by 3x, and the
  `_MEASURED` entry that carried the right number has been deleted, which leaves
  the repository holding only the wrong one. The report answers this as though
  the finding were about its own AX1 revision; the finding named
  `instrumentation.md`. `:672` ("so only commensurability varies") is unchanged.
  `docs/milestones/F2.md:470` still says "DRAFT, awaiting review" after five
  rounds (R27). Permitted to carry, but the count is now two verdicts.

- **10. R4, R5, R6, R15, R16, R25, R26, R27 -- still open**, as verdict 1
  permitted. Two of them are no longer background: under the narrowing **R4 and
  R5 are G2.2's own items**, see **R41**. The report's `Carried` again lists
  R4/R5/R6 and omits R15, R16, R25, R26, R27 -- the same omission R37 recorded.

## Findings

**R37a. (blocking) R29's second half is untouched: three strings in G2.2's own
test file still assert a property of a solve path that was deleted.**
`tests/verification/rung1/test_patch_test.py` -- `git diff e8c221a..HEAD` on that
path is empty. `:423` says the conditioning identity is "the algebraic fact the
equilibrated solve rests on"; the solve rests on nothing of the kind, it
factorises `K_ff` directly. `:440-441`, the failure message of
`test_the_equilibrated_conditioning_is_unit_INVARIANT`, tells a future reader
that if that test fails "**the solve is not unit-robust and every exactness
ceiling above it is unit-dependent**" -- a false implication now, and in the
dangerous direction, because it would send someone to the solve when the test
measures a utility. `:446` calls the unequilibrated control the thing that stops
equilibration being "ceremony"; on the production path it *is* ceremony, and
`system.py:91` says so in the honest words ("retained as a utility").
**Closed when** the three read as statements about `equilibrate` the utility and
about the conditioning property, with no claim about `solve`.

**R38. (blocking) G2.2's only anti-widening guard admits a total loss of
sensitivity. Its declared 5% band is not the band in force.**
`tests/verification/rung1/test_patch_test.py:323`:

```python
assert err == pytest.approx(PATCH_TEST_EXACTNESS, rel=DETECTION_THRESHOLD_BAND)
```

`rel * |expected| = 0.05 * 1e-12 = 5e-14`; `pytest.approx`'s undeclared default
`abs = 1e-12` is twenty times larger, so the tolerance in force is `1e-12`.
Solved rather than sampled, by bisection on the shipped predicate:

```
band as declared would admit:  9.5000e-13 .. 1.0500e-12
band actually in force:        0.0        .. 2.0000e-12
err = 0.0 passes?  True
```

Per state the admissible sensitivity is `[0, ~2x]` against a measured
`~1.08e-01` -- i.e. **-100% to +100%**, not plus-or-minus 5%. Confirmed by
mutation rather than left as algebra: I replaced `if stiffness_scale != 1.0:` in
`_run` with `if False:` -- the perturbation silently dropped, the gate's
sensitivity exactly zero -- and **all six
`test_the_measured_detection_threshold_still_holds` nodes stayed green** (8
others failed; file restored). The docstring at `:316-319` says "If a formulation
change alters sensitivity, this fails."

Why this is G2.2's and not step 4a's: I mutated `PATCH_TEST_EXACTNESS` to
`1e-11`, `1e-10` and `1e-9` and in each case exactly six tests reddened -- these
six. It is the **only** widening guard on the gate's ceiling. Tightened to
`1e-13`, where `err ~ 1e-12` sits ten times above the ceiling, the whole suite
stays green, which is the same defect seen from the other side. The fourth
verdict reproduced `DETECTION_THRESHOLD_BAND_MEASURED = 9.9523e-03` and recorded
"margin 5x"; the margin is not 5x, because `0.05` does not decide.
**Closed when** the assertion's deciding tolerance is the declared one -- the
one-line form is `assert_close(err, PATCH_TEST_EXACTNESS,
DETECTION_THRESHOLD_BAND, floor=...)`, which has no defaults -- and the closing
number is the inverted one: the smallest sensitivity change the assertion
detects, measured, stated beside the `0.05`.

**R39. (blocking, cheap) A false claim about the repository, in a production
module, of exactly the species `c737358` fixed one module over.**
`floatfea/testing.py:23-25`: "`pytest.approx`, `np.allclose` and friends are
**not called directly under `tests/`**; the scanner enforces that." Counted at
HEAD, excluding the scanner's own corpus: **45** `approx` call sites and **28**
`assert_allclose`/`allclose`/`isclose`/`assert_array_almost_equal` call sites
under `tests/`. Two of the 45 are in the patch test itself (`:323`, `:439`), and
`:323` is R38. The scanner does not enforce it and never claimed to. This is not
a scanner finding -- it is a sentence in `floatfea/` asserting a fact about the
tree that a one-line `grep` refutes, in the module BD0 created.
**Closed when** the sentence states what is true (`assert_close` exists and is
used at two sites; the ban is step 4a's proposal, not the present state) or is
deleted.

**R40. (blocking) "Unit invariance on the shipped solve path" is one of the four
things the narrowed step closes on, and no shipped test asserts it.**
`_scaled_model` (`test_patch_test.py:404`) is consumed only by the two
conditioning tests at `:419` and `:445`. `_run` is never called at any scale but
`1.0`. So the nine-decade sweep exists only in a scratch harness -- the
implementer's, and mine. The consequence is in `tolerances.py:317-321`, which
justifies the ceiling with "VERIFIED invariant across length-unit factors
`S = 1e-4 .. 1e+4` ON THE PATH THAT SHIPS: worst error `2.00e-13` ... **5.0x of
headroom at the worst scale**, against 80x at the metre scale". `5.0x` is the
binding number and nothing in the suite measures at the scale it belongs to.

The claim itself is **true** -- I reproduce `2.004e-13` and, extending past the
recorded range, there is no breach anywhere from `S = 1e-8` to `S = 1e+8`
(worst `2.404e-13` at `S = 1e-7`, where `cond(K_ff) = 5.7e16`). So this is not a
correctness finding. It is that the number which decides whether `1e-12` is
defensible has exactly the epistemic status `_MEASURED` had, and `ab23181`
deleted `_MEASURED` for that reason: *"a hand-written literal ... is a check
whose subject the check itself supplies"*. Moving it from a `Final[float]` to a
comment line one screen up does not change what a run can falsify.
**Closed when** `test_the_four_constant_strain_states_are_EXACT` is parametrised
over scales as well as states and orientations -- `_run` already takes everything
needed and `_scaled_model` exists -- so that the `5.0x` figure is an execution
result. If nine decades is too slow, three (`1e-4, 1, 1e4`) covers the worst cell
and is 18 more nodes.

**R41. (blocking under the narrowing) R4 and R5 are G2.2's items, and the
narrowing is what makes them due.**
They were allowed to carry when step 4 was large. Step 4 now closes on G2.2
alone, so the locked plan's obligations *for this gate* are the whole of what is
left, and two are open.

- **R4.** `docs/milestones/F2.md:775` still names the entry `PATCH_TEST_STRAIN`,
  which does not exist, and gives its counter-case as "one element's
  transformation transposed", which no test runs. I ran it -- `rotation_matrix`
  returning `R.T` for element 1 only -- and every state detects it:
  `axial 1.53e+00, curvature 2.01e-01, twist 1.57e-01, shear 3.02e-01,
  curvature_xz 1.01e-01, shear_xz 1.49e-01`. So the gate is not weak; the plan's
  named counter-case is prose. The guard is that a counter-case is an executable
  value, not a sentence.
- **R5.** `test_patch_test.py:235`, `assert res.residual <= PATCH_TEST_EXACTNESS`,
  inside the gate assertion itself. Re-measured at HEAD, and further than the
  first verdict went -- with a **2x** element-stiffness defect, which puts the
  displacement error at 6.5%:

  ```
  state         clean      1e-3 defect   2x defect   (field err at 2x)
  axial       5.931e-16     4.700e-16    3.356e-16      6.46e-02
  curvature   1.056e-15     1.258e-15    1.490e-15      6.37e-02
  shear       1.729e-15     1.418e-15    1.162e-15      6.89e-02
  ```

  The residual does not move; for two of the three it moves *down*. A defect that
  fails the line above by eleven orders leaves this line green. It is a
  linear-solve residual compared against a displacement-field exactness
  tolerance -- the wrong quantity as well as a vacuous assertion.

**Closed when** `F2.md:775` names the shipped entry and its shipped counter-case,
the transposed-transform case is a test or is withdrawn from the plan with a
reason, and `:235` either compares the residual against a tolerance in its own
quantity or is removed. A `SOLVE_RESIDUAL` entry with its own counter is the
honest form; reusing this one is what made the line unfalsifiable.

**R42. (recordable) The implementer edits the reviewer's own instructions, and
nothing gates that.**
`8ba62d3` modifies `.claude/agents/gating-supervisor.md` -- the file that defines
what I read, what I must carry, and what I may write. I diffed it line by line:
this change is purely additive (the BE3 section, the description line, the "What
you write" clause) and **deletes no guard**, so there is nothing wrong with the
change itself. The mechanism is the finding.
`.claude/hooks/protect-reviews.sh` denies `docs/reviews/` and now
`tests/corpus/`; the agent definition that governs both is freely editable by the
implementer, and the only thing that would catch a quietly deleted guard is a
reviewer diffing their own instructions -- which is not in the instructions.
**Closed when** either the hook covers `.claude/agents/gating-supervisor.md`, or
the review protocol names it as a file to diff at every step. I did diff it this
round; that was discretionary.

**R43. (recordable, and the one a later reader will need) `1e-12`'s "80x
headroom" carries no operating point, and the ceiling is breached inside the
slenderness range the locked plan's own tables discuss.**
The gate is posed at one geometry: `Section.circular_tube(0.6, 0.012)` with
element lengths `0.79..3.27 m`, i.e. longest-element `L/r ~ 16`. Sweeping the
section and re-running all six states in both orientations:

```
  D (m)   elem L/r   worst err    x ceiling
   0.60       15.7   1.251e-14      0.013
   0.40       23.6   3.807e-14      0.038
   0.20       47.2   1.571e-13      0.157
   0.10       94.4   1.762e-12      1.762   BREACH
   0.05      188.7   4.415e-12      4.415   BREACH
   0.02      471.8   1.844e-11     18.440   BREACH
```

Bisected, the boundary is `D = 0.078 m`, longest-element `L/r ~ 121`. `F2.md`
sec. D3's own table runs `lambda = 20 .. 100`, and sec. 5's corrected Q1 table
puts the governing brace at `lambda = 46.4` -- comfortably inside the safe region
(`~4e-14`, 25x of margin), so **F3's expected sections are covered and this is
not a defect**. It is a missing operating point on the headroom figure this
revision leads with, and the guard is "a ratio carries its operating point".

Localised before being reported, per the second guard. The breach is entirely on
the **skew** orientation, in the **axial** state, in the **rotational** DOF:

```
  D=0.60  err 1.251e-14 at node 3 rz   translational part 3.66e-15   cond 9.21e2
  D=0.10  err 1.762e-12 at node 4 rz   translational part 4.13e-13   cond 3.03e4
```

The axial state's exact rotations are identically zero, so its error is a pure
spurious-rotation-over-translation ratio through the transform chain -- the same
structure that produced the kilometre breach in R2/R8, arriving down the
slenderness axis instead of the unit axis. Axis-aligned stays at `1e-16`
throughout. **Closed when** `tolerances.py` states the geometry the `80x` belongs
to, and either the measured `L/r` boundary or the range the ceiling is claimed
over. One sentence; no value needs to move.

**R44. (recordable) The gate is blind to `kappa`, correctly, and does not say so.**
I set `Section.kappa` to `0.5` -- the simple thin-tube value against the shipped
Cowper `0.5305`, the 6% gap Q1b was written about -- and re-ran all six states on
the skew orientation. **All six green**, worst `8.6e-15`. That is right: the
reference field at `_exact_local:92` consumes `SEC.kappa(S355)`, the same source
the element uses, which is exactly what Q1b pinned. But it means G2.2 certifies
formulation *self-consistency*, not any section constant, and the module
docstring does not say which way that runs. Recorded because the counter-case it
should be read against is V2.2's, not this gate's. Positively: the discrimination
AV4 claims for state 4 **does** work -- substituting
`euler_bernoulli_bending_stiffness` for the shear-flexible block reddens `shear`
and `shear_xz` at `6.2e-03` while the other four states stay at `1e-14`, which is
the state-4 argument measured rather than asserted.

---

**On the narrowing itself -- accepted, and here is the test I applied.**

The question is whether the scope was cut to route around open items. I do not
think it was, for three reasons I could check:

1. **It returns step 4 to the locked plan rather than departing from it.**
   `F2.md` sec. D2 row 4 is "V1.2 patch test / proves assembly, transformation,
   connectivity / G2.2". The scanner, `testing.py`, the exemption scheme and the
   `_MEASURED` registry were never in that row. The narrowing is the plan being
   re-read, which is the opposite of the failure this loop exists to catch.
2. **Nothing that gates G2.2 left with them.** I tested this rather than
   accepting it. Of the moved items, R30, R31, R32 and R36 touch no assertion in
   `tests/verification/rung1/`. R33 does, at one site, and I have brought that
   one back as R38 rather than letting the move carry it.
3. **`F2a.md` is a real skeleton, not a parking space.** It carries the diagnosis
   (sec. 2A: the scanner failed because it reasoned about precedence, so remove
   the question), six questions that are genuinely open, and an exit criterion
   that the reviewer's corpus must have caught shapes the implementer did not
   see. A plan written to bury something does not pre-register that its coverage
   number will be supplied by someone else.

**What the narrowing does not do is remove the apparatus from the tree.**
`tests/test_no_tolerance_literals.py` still runs in CI, still nominally enforces
`CLAUDE.md` sec. Tolerances -- the rule the whole file exists for -- and reads
green at a measured 2-of-25 on unseen shapes. The report states this honestly;
the *tree* does not. That is not blocking on G2.2, but a green suite is the
signal a later reader gets, and right now it overstates one thing. The cheapest
fix is a sentence in the scanner's own docstring recording its measured coverage
and that it is unplanned pending 4a -- the same move `system.py:91` makes for
`equilibrate`.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| nine `X_MEASURED` entries | various | **deleted** | -- | -- | `tolerances.py:50-57` and `test_tolerance_counter_cases.py:119-133`. Verified by `ast` diff of both revisions: nine names removed, none added, **no value moved**. The right direction -- the class was unfalsifiable by construction. |
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` (unchanged) | relative, dimensionless | `1.0e-7`, asserted at `:339` | `tolerances.py:305-360`, rewritten for the shipped path; every figure in it reproduces through my own harness. Two gaps: the `5.0x` worst-scale headroom is asserted by no run (**R40**), and the `80x` metre-scale headroom has no operating point and does not survive `L/r ~ 94` (**R43**). |
| `PATCH_TEST_EXACTNESS_COUNTER` | `1.0e-7` | `1.0e-7` (unchanged) | relative, dimensionless | -- | `test_a_perturbed_element_BREAKS_the_patch_test`. Measured margin at HEAD `1.076e-07 .. 1.174e-07` against `1.0e-7`: **7.6% at the weakest state**. Thin, but on the right side and failing in the safe direction. Worth one sentence recording that it is calibrated against a `1e-6` perturbation at a measured sensitivity of `1.08e-01`, so a reader knows why it is not round. |
| `DETECTION_THRESHOLD_BAND` | `0.05` | `0.05` (unchanged) | relative, dimensionless | `0.25`, unused (4a) | `tolerances.py:461-489`. Value unmoved, **but it does not decide its only assertion** -- the band in force is `0 .. 2x` (**R38**). The previous verdict's "margin 5x" should be read as withdrawn. |
| everything else | -- | unchanged | -- | -- | No other declared value moved anywhere in `e8c221a..44f4e14`, verified by parsing both revisions rather than by reading the diff. |

No tolerance was widened. No golden file moved. No test was skipped or `xfail`ed;
the suite has zero skips and the ACCURACY parametrisation still resolves to real
entries rather than the sentinel.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R37a** -- `test_patch_test.py:423, 440-441, 446` stop asserting a property
   of `solve`. Gated at the fourth verdict as the second half of R29, and the
   only item here that is a repeat.
2. **R38** -- the deciding tolerance at `test_patch_test.py:323` is the declared
   one, and the smallest sensitivity change the assertion detects is measured and
   recorded beside `DETECTION_THRESHOLD_BAND`. The mutation that closes it is the
   one I ran: drop the perturbation in `_run` and confirm those six nodes go red.
3. **R39** -- `floatfea/testing.py:23-25` says something true about `tests/`.
4. **R40** -- a shipped test runs the six states through the solve at more than
   one length unit, so that `2.00e-13` and the `5.0x` headroom are execution
   results rather than scratch-harness figures.
5. **R41** -- `F2.md:775` names the entry that exists with a counter-case that
   runs, and `test_patch_test.py:235` compares a residual against a tolerance in
   its own quantity or is removed.

R42, R43 and R44 -- together with R4's plan-text half, R6, R15, R16, R25, R26,
R27 and R37's two open bullets -- may be answered in step 5's `Carried` section,
**and that section must list every one of them, open or answered.** That
instruction was given at the fourth verdict and this step's report again lists
three of eight.

**Not a STOP.** No rung is red, and the element is in better shape than any
document in the repository claims. Everything I could think to break, I ran: the
six states are exact at `1.25e-14` in both orientations at the posed geometry
(80x); the Euler-Bernoulli substitution reddens exactly the two shear states and
nothing else, which is AV4's state-4 argument measured; a transposed
transformation on one element is caught by all six states at `1e-01` and above; a
defect confined to one bending block is seen by that plane at `1.08e-04` and by
the other at `1.4e-14`, ten orders apart; and the shipped, unequilibrated solve
holds the ceiling across **seventeen** decades of length unit, at conditioning up
to `5e19`, worst `2.4e-13`. The four corrections in this step are all genuine,
and the ablation behind R34 is the best-executed piece of work in the milestone
-- I rebuilt it independently and it reproduces to three digits, including the
cell that refutes the sentence.

What the findings have in common is narrower than in the last four rounds, and
worth naming because it is now the *only* pattern left: **five of the seven are
sentences and numbers that describe the repository, in files a reader trusts,
that a one-line check refutes** -- three test strings about a deleted solve path,
a `floatfea/` docstring about what `tests/` contains, a headroom figure with no
operating point, a plan row naming an entry that does not exist. Not one of them
is an element defect. The standing question for the next round is the one that
would have caught all five: *for every sentence in this diff that states a fact
about the code, what is the command that checks it?* `c737358` asked exactly
that about citations and found one; the same sweep over claims rather than
citations finds four more.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Five
consecutive reviews by one reader. Until V5.1 puts CalculiX on the other side,
301 green means "not yet contradicted" -- and this round it means slightly less
than that, because R38 and R41 are two assertions inside the green count that
cannot fail.

**Adversarial corpus (BE3): `tests/corpus/` holds ZERO entries, and I did not
create it this round.** The reason, stated so it is a decision rather than an
omission: the check it scores is 4a's, and 4a's Q3 and Q5 leave the checker's
*rule* open -- a corpus written against an undesigned checker fixes the design
from the reviewer's side, which is the same error BE3 identifies, mirrored. The
shapes I would seed it with are already measured and public: the three
regressions from the regex (`err < 5e-3 * scale`, `err <= 1e-13 * abs(k).max()`,
the in-message exemption), the `SAFE_CALLS` blind spot, `rel_tol`/`abs_tol`/
`delta`, positional `rtol`, library defaults for the whole `APPROX_NAMES` set,
and the name-indirection form `TOL = 1e-9; assert err < TOL`. **The corpus opens
when `F2a.md` is locked**, and its first count will be reported in the verdict on
4a's build, not before.
