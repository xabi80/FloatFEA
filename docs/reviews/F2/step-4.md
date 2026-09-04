# Review — F2 step 4
Reviewed commit: ec8b23705c2151e72a803fefa6052a1591241777
Verdict: HOLD
Tests: 260 passed, 0 failed, 0 skipped   (my run, `pytest -q`, 0.65s)

The x-z gap (R1) is genuinely closed and I verified it by mutation. The
unit-invariance property (R2) genuinely holds and I reproduced it independently.
But the *account* of R2 in `floatfea/tolerances.py` is refuted by measurement, R3's
refuted claim is still standing verbatim in the test file, R7's restoration adds a
mis-citation, and the commit that answers the HOLD re-introduces the undeclared
tolerance literal that AW2 was raised for. Three of those are the same species of
defect the HOLD was about, one iteration later.

## Carried

Every item from `docs/reviews/F2/step-4.md` (HOLD @ `ab7e45a`), traced into the
diff `ab7e45a..HEAD` rather than taken from the report.

- **R1 (blocking) - ANSWERED, and verified beyond the report.**
  `tests/verification/rung1/test_patch_test.py:104-116` adds `curvature_xz` and
  `shear_xz`; the parametrisations at :213, :311, :327 carry six states. I derived
  both fields independently rather than reading them: `curvature_xz` has
  `w' + phi_y = 0` (zero shear) and `phi_y' = c` (constant curvature);
  `shear_xz` has `w' + phi_y = P/(kappa G A)` constant and `M = EI_y phi_y'`
  linear. Confirmed against the discrete operator, not the continuum: imposing the
  exact field at every node and reading element end-forces gives, for
  `curvature_xz`, `Vz = 0` and `My = -4.0253e+04` identically on elements of
  length 3.27, 0.90 and 1.71 m - and `EI c = 210e9 * 9.5842e-4 * 2e-4 =
  4.0254e+04`. For `shear_xz`, `Vz = -1.0000e+05` on every element with
  `My(0) = 9.6700e+05 = P L` and `My(L) = 3.7e-09`. Correct, not merely
  self-consistent.

  **The states are load-bearing.** I mutated `beam.py:153` to drop the `flip`
  (`k[xz] = ky` instead of `flip @ ky @ flip`) and re-ran all six states:

  ```
  mutation          axial  curvature   twist    shear  curvature_xz  shear_xz
  flip omitted    1.4e-14   4.2e-15  3.0e-16  1.2e-14      1.33          1.79
  flip one-sided  5.9e-15   6.9e-15  7.1e-16  8.9e-15      1.33          1.79
  Phi:=0 in x-z   2.0e-14   1.2e-14  3.0e-15  1.6e-14      7.3e-15     6.20e-03
  ```

  Only the two new states see the sign error; only `shear_xz` sees an
  Euler-Bernoulli x-z block. The gap R1 named was real and is now covered.

  **The block-confined control does confine.** `local_stiffness` is exactly
  block-diagonal in local axes (max off-block entry `0.0` against a max entry of
  `1.42e+09`), so `pert` supported on `{2,4,8,10}` then rotated is a defect in one
  physical behaviour. Full response matrix to a `1e-3` block defect, skew:

  ```
  perturbed \ state   axial  curvature   twist    shear  curv_xz  shear_xz
  axial             1.09e-4   5.7e-15  3.0e-16  2.9e-15  4.3e-15   6.3e-15
  torsion           1.6e-14   3.8e-15  1.09e-4  9.0e-15  1.6e-15   2.9e-15
  bending_xy        1.4e-14   1.08e-4  2.5e-16  1.17e-4  3.0e-15   4.8e-15
  bending_xz        1.4e-14   2.9e-15  5.1e-16  6.9e-15  1.08e-4   1.17e-4
  ```

  Diagonal by block, four orders of separation. Answered.

- **R2 (blocking) - the PROPERTY is answered; the ACCOUNT of it is not.**
  I re-ran the unit-scaling table myself over `S = 1e-4 .. 1e+4`, all six states,
  skew, through the shipped `solve` and the shipped error measure: worst
  `3.19e-14`, no breach of `1e-12` anywhere. At `S = 1e-3..1e+3` the worst is
  `3.12e-14` - the exact figure `tolerances.py` records. The breach my previous
  verdict measured is gone. The property holds. What does not hold is the stated
  mechanism and the claim of verification - see **R8** and **R9**.

- **R3 (blocking) - PARTIALLY answered.** The withdrawal is correct in direction
  and I reproduced every number in it (`A 7.7448e-08`, `B 6.5661e-08`, ratio
  `0.848`, and the `4.5x` spread across element index on a uniform mesh). But R3's
  "closed when" named three places and one of them still carries the refuted
  claim verbatim - see **R10**. The replacement figure is also over-stated as a
  measurement - see **R11**.

- **R7 (blocking) - PARTIALLY answered.** `d4c2fe5` restores the locked wording at
  `docs/milestones/F2.md:51` (byte-identical to `e353852:51`, the lock) and at
  :528, and rewrites :688. Committed alone, ahead of the work, as asked. But the
  restoration appends a sentence that is not the lock and is not AV4 - see **R12**.

- **R4 - still open**, as permitted. `docs/milestones/F2.md:775` still names
  `PATCH_TEST_STRAIN`, a tolerance that does not exist; the
  orientation-dependence of the transposed-transformation counter is still
  unrecorded. Deferred to step 5's `Carried`.

- **R5 - still open**, as permitted. `tests/verification/rung1/test_patch_test.py:225`
  still asserts `res.residual <= PATCH_TEST_EXACTNESS`. Note the equilibrated solve
  changed what this number is; I measure it at `1.55e-15` on the shear state. The
  objection is unchanged: it is a solver residual compared against a tolerance whose
  form, provenance and counter are all in a different quantity. Deferred.

- **R6 - still open**, as permitted. `grep` still finds `pin_threads` called only
  from `tests/verification/rung3/test_determinism_pins.py:24`. `tests/conftest.py`
  does not call it and there is no `tests/verification/conftest.py`. Deferred, and
  it should be recorded against step 3 as well.

## Findings

**R8. `floatfea/tolerances.py:309-324` states that unit invariance "required two
fixes". Measurement says it required one. The equilibrated solve - a change to the
production solve path - is justified in the permanent tolerance record by a
necessity claim that is false.**

I ran the 2x2. Worst relative error over all six states, `S = 1e-4 .. 1e+4`, and
the first breach of `1e-12` found by sweeping outward from `S = 1`:

```
equilibrate  weighted measure   worst error    first breach of 1e-12
   yes             yes            3.19e-14      none out to S = 1e12
   NO              yes            2.00e-13      none out to S = 1e12
   yes             NO             2.09e-11      S = 1e-3   (2.84e-12)
   NO              NO             2.07e-10      S = 1e+3   (1.82e-11)
```

The dimensionally homogeneous error measure **alone** carries the whole property,
out to twelve orders of length-unit change. Equilibration **alone** does not
achieve it at all - it still breaches in kilometres, at `2.84e-12`, which is the
same breach the previous verdict reported. Equilibration is worth a factor of
about 6 in the floor (`2.00e-13 -> 3.19e-14`); it is a real improvement and I am
not asking for its removal. What I am asking is that the record stop saying it was
required, because that is the exact move R3 was held for one commit earlier: a
plausible mechanism placed beside a real number without the controlled measurement
that would separate them. Here it is worse than in R3's case, because the false
necessity claim is what licenses a change to the solver every later gate runs
through.

I confirmed the solver change is otherwise inert: equilibrated and unequilibrated
`u` agree to `3.83e-15` relative on the shear state, `solve` is still bit-identical
across two factorisations in one process, and `cond(K~) = 3.8491e+02` at
`S = 1e-3, 1, 1e+3` exactly as claimed.

**Closed when** the comment says what measurement supports: the error measure is
necessary and sufficient over the tested range; equilibration is a ~6x improvement
in the floor and is justified on its own numerical merits (or is removed). If
equilibration stays, its justification is a solver-hygiene argument, not a
unit-invariance requirement, and it belongs in `system.py` and the closure
artifact rather than inside a tolerance's provenance.

**R9. The property R2 exists to establish has no executable guard. The three tests
added to hold it test something else, something insufficient, and a substring.**
`tests/verification/rung1/test_patch_test.py:414-465`.

- `test_the_equilibrated_conditioning_is_unit_INVARIANT` and
  `test_the_UNequilibrated_conditioning_DOES_move` assert conditioning. By the R8
  table, equilibrated conditioning is **neither necessary nor sufficient** for the
  error invariance: it is achieved without equilibration, and it is not achieved
  with equilibration alone. So both tests can be green while the gate's ceiling is
  again a function of the unit system.
- `test_the_error_measure_weights_rotations_by_a_length` asserts
  `"w[3:]" in src and "STATIONS[-1]" in src`. Writing `w[3:] = 0.0 * STATIONS[-1]`
  satisfies both substrings and destroys the measure. A structural provenance
  assertion is the right instinct here, but this one certifies the presence of two
  strings, not the presence of the property.

`tolerances.py:310` says the invariance is "VERIFIED ... across length-unit factors
S = 1e-3 .. 1e+3: worst error 3.12e-14". I reproduce that number exactly - and
nothing in the suite would notice if it stopped being true. This project already
holds the opposite standard one screen away: `DETECTION_THRESHOLD` is asserted
precisely so recorded numbers cannot go stale, and that assertion earned itself by
going red when the mesh changed.

**Closed when** the patch test is run at more than one length unit and the error is
asserted against `PATCH_TEST_EXACTNESS` at each - the same six states, the same
ceiling, the model posed in the scaled unit system rather than the conditioning
inspected as a proxy. `_scaled_model` already builds the scaled model; the missing
piece is a `_run` that takes a scale. If step 6 (V1.3 / G2.5) is the intended home
for that, then `tolerances.py` must say the invariance is *asserted at G2.5* rather
than *verified*, and step 6's plan must carry it.

**R10. R3's "closed when" named three places. One of them still carries the
withdrawn claim verbatim, and a fourth carries the superseded numbers.**
`tests/verification/rung1/test_patch_test.py:297-300`, unchanged in this diff:

```
# These numbers are FROM THE INCOMMENSURATE MESH. On the previous mesh -- which
# contained 0.9/0.6 = 3/2 exactly -- the weakest state's threshold was 1.51e-10,
# so removing the symmetry cancellation improved detection about FIVEFOLD.
```

That is the exact sentence R3 refuted, sitting ten lines below the corrected block
that says the fivefold claim is withdrawn. The module docstring at :69-73 was
corrected; this comment was not. `grep -rn fivefold` finds it.

Line :294 in the same block is stale for a second reason: "the patch test stops
seeing a single-element stiffness error below ~3.3e-11 relative" - `3.3e-11` is the
pre-R2 weakest threshold. The table eight lines above it now reads `9.29e-12`. The
block contradicts itself.

And `docs/instrumentation.md:705-711`, the corollary section that the withdrawal
sits directly above, still tabulates `curvature 3.7161e-02 / 2.69e-11` and
`shear 3.0170e-02 / 3.31e-11` - the sensitivities the report itself says were
understated by the incoherent measure. Superseded numbers left standing in the
permanent instrumentation record, in the section about not leaving recorded numbers
describing a gate that no longer exists.

**Closed when** the fivefold sentence is gone from the test file, :294 quotes the
current weakest threshold, and the `instrumentation.md` corollary table carries the
six re-measured rows.

**R11. `0.848` is one draw presented as a measured constant, and the comparison it
comes from still varies the variable the same paragraph identifies as dominant.**
`docs/instrumentation.md:673-682`, `floatfea/tolerances.py:348-352`, and the test
docstring at :71-72.

The comparison holds element 1's *length* at 2.0 m and the total at 10.0 m, but not
its *position*: element 1 occupies `[2.0, 4.0]` in mesh A and `[1.069, 3.069]` in
mesh B. The very next sentence says sensitivity is driven by which element is
perturbed and where it sits, and measures `4.5x` across element index. So position
is uncontrolled in a comparison labelled controlled - the second time in two
revisions at this spot.

Worse, it cannot be controlled as posed. If element 1 spans `[2.0, 4.0]` then
element 0 is 2.0 m, identical to element 1, and the mesh is commensurate by
construction. Position and commensurability are confounded for element index 1 in
a five-element mesh anchored at the origin.

I ran the distribution instead: for each mesh, perturb **every** element in turn by
`1e-6` and take the weakest state's response.

```
mesh                                  min over elem   median   spread across index
uniform [2 x 5], total 10               1.906e-08   7.745e-08      4.5x
report's B, total 10                    6.519e-09   6.566e-08     14.3x
six random incommensurate, total 10   1.15-2.41e-08  4.67-7.86e-08  3.5-9.2x
current test mesh, total 9.67            1.565e-08   2.645e-08      6.9x
```

Median-of-medians for the random incommensurate meshes is `7.015e-08` against the
uniform mesh's `7.745e-08`: ratio `0.906`, with the single reported `0.848` sitting
comfortably inside a scatter that runs `0.60 .. 1.01`. **The conclusion survives** -
commensurability buys nothing, and if anything costs a little. The number does not:
`0.848` is one sample of a quantity whose between-mesh scatter is larger than the
effect and whose within-mesh scatter across element index is 4.5x larger again.

**Closed when** the three places state the conclusion without the spurious
precision - no measurable benefit, the effect smaller than the scatter across which
element is perturbed (4.5x) and across mesh draws - or `0.848` is replaced by a
range over several meshes. The lesson quoted at :696-697, to report the result as
unattributed, is the right one; it is not the one the number above it follows.

**R12. The restored scope is the locked scope plus a paraphrase, and the paraphrase
mis-cites AV4 and states a count that matches neither AV4 nor the test.**
`docs/milestones/F2.md:51`. Everything up to "...below every accuracy comparison" is
byte-identical to `e353852:51`, the lock. What follows is new:

> "Per AV4 this is **four** states ... and per AV4 item 2 curvature and shear are
> required **in each bending plane**, so eight state/plane combinations in total"

AV4 item 2 reads "**constant curvature** (in each bending plane)". Item 4 reads
"**constant shear**, with its accompanying *linear* moment" - with no plane
qualifier. The requirement that shear be run in each plane is mine, from R1, not
AV4, and attributing it to AV4 item 2 makes a review finding look like a locked
requirement.

And "eight" is wrong under every reading. Four states with two of them
plane-doubled is six: axial, twist, curvature x2, shear x2. The shipped
parametrisation is six. So the gate cell now demands more than AV4 asks and more
than the test delivers, and any closure row citing it will not reconcile. R7 was
about a gate cell quietly changing meaning; this is the same cell changing meaning
again, in the commit that fixes it.

Separately, and not blocking: AV4 itself entered `docs/milestones/F2.md` at
`170cb52` - during step 3, after the 2026-08-30 lock - and the detailed plan still
reads "**Status:** DRAFT, awaiting review" at :470. The plan is being amended while
it is executed. AV4 is a strengthening and I am not asking for it to be undone, but
the lock's own rule is that execution revealing a plan gap stops and says so.
Record it.

**Closed when** the cell states AV4's requirement as AV4 writes it, marks the
extension to shear as a step-4 review finding rather than as AV4, and gives the
count the test actually runs.

**R13. The commit that answers the HOLD re-introduces the undeclared tolerance
literal that AW2 was raised for, in the same file, two commits after AW2 was
closed.**
`tests/verification/rung1/test_patch_test.py:431` - `pytest.approx(..., rel=1e-6)`;
:445 - `assert max(conds) / min(conds) > 1e4`. Both are new in `ba8c3c4`. Both are
numerical thresholds that decide a pass. CLAUDE.md section Tolerances: every
numerical tolerance in this repository lives in `floatfea/tolerances.py`, no
exceptions and no local literals - and it explicitly extends the rule to comparison
epsilons and small-number guards. AW2 was exactly this (`rtol=1e-10` in the
subdivision test) and was fixed by creating `SUBDIVISION_INVARIANCE` with its
measurement.

`rel=0.05` at :320 is the same violation and pre-dates this step; I did not raise
it last time and I am raising it now so it is not carried silently a third time.

**Closed when** the three literals are named entries in `tolerances.py` with their
class and, where they are accuracy claims, a measured counter - or the tests that
carry them are restructured so no literal decides a pass.

**R14. (recordable, not blocking) The report's block-confined numbers are from the
superseded error measure.**
`docs/reports/F2/step-4.md:226-228` quotes `curvature_xz 3.714e-05`,
`shear_xz 3.015e-05` for the `1e-3` `bending_xz` defect and says they match my
independent figures. Under the shipped code they are `1.076e-04` and `1.174e-04`; I
reproduce `3.714e-05 / 3.015e-05` only by turning the rotation weight off. So the
revision that introduces the coherent measure reports its new control in the old
measure, and reads as corroborated because the old measure is what my pre-fix
verdict used. The agreement is an artifact. Not a defect in the code; a claim I
could not locate in the shipped behaviour, recorded as unverified.

**R15. (recordable, not blocking) Three margins that are not written down.**

- `test_a_defect_in_ONE_bending_plane_is_caught_by_THAT_plane` perturbs by `1e-3`
  and asserts against a counter measured from a `1e-6` defect. Measured margin
  1000x. It certifies that the plane is not blind, which is what R1 asked for, but
  it would stay green if that plane's sensitivity fell by three orders. The
  whole-element control at :335 uses the matching `1e-6`.
- `PATCH_TEST_EXACTNESS_COUNTER = 1.0e-7` against a measured minimum response of
  `1.0764e-07`: margin 7.6%. That is deliberate and defensible - the point is that
  sensitivity erosion reddens - but the margin is the number a later reader needs
  and it is not in the comment. For contrast, the same six states on a stubby
  configuration (D = 2.0 m tube, 3.0 m total, `Phi = 184`) respond at
  `8.898e-08 .. 1.018e-07`, i.e. below the counter, so the counter is a property of
  this mesh and this section and should say so.
- `test_the_four_constant_strain_states_are_EXACT` runs six states. Rename before a
  closure evidence row cites it.

**R16. (note for step 12, not a defect now) `equilibrate` takes `abs()` of the
diagonal.**
`floatfea/assemble/system.py:57`. The solve stays algebraically exact for any
non-zero diagonal scaling, so this is not wrong. But the guard beneath it only
catches an exactly-zero diagonal, and its message asserts that the caller has an
unconstrained mechanism. When `k_g` arrives at step 12 a diagonal can go negative
under compression, and it will pass this guard silently. Worth a line in step 12's
plan.

---

**What I verified positively**, so the above is not read as the whole picture:

- All six states clean, both orientations, through the shipped code: worst
  `8.214e-15` (axis-aligned `shear_xz`) against `1e-12`. Matches the report.
- Independent route, not through the solver: impose the exact field at every node
  and read the interior out-of-balance relative to `|K| |u|` -
  `1.8e-17 .. 4.7e-17` across all six states. The element reproduces these states.
- Every recorded detection threshold reproduces to three digits under my own
  harness: `axial 9.168e-12`, `curvature 9.291e-12`, `twist 9.168e-12`,
  `shear 8.516e-12`, `curvature_xz 9.291e-12`, `shear_xz 8.516e-12` against the
  recorded `9.17 / 9.29 / 9.17 / 8.52 / 9.29 / 8.52e-12`. Perturbing by each lands
  the error on `1e-12` to within 0.7%.
- The counter `1.0e-7` is the smallest of six independently measured responses
  (`1.0764e-07`), and the direction is right: the assertion is `err >= COUNTER`, so
  raising it is a tightening. Verified, not accepted.
- `cond(K~) = 3.8491e+02` at `S = 1e-3, 1, 1e+3`; `cond(K_ff)` runs
  `5.98e+08 -> 9.21e+02 -> 4.05e+07` over the same range. Both claims exact.
- Equilibration changes the shear-state solution by `3.83e-15` relative and leaves
  the two-factorisation comparison bit-identical.
- Adversarial cases I ran that did **not** produce a finding: a stubby
  configuration with `Phi = 184` (all six states at `2.2e-16 .. 5.7e-16`); skew and
  axis-aligned orientations, which give identical block-confined responses; the
  non-circular section, which `Section.__post_init__` still refuses.
- Every test cited in the report and in `tolerances.py` resolves to a real test at
  the path given, checked mechanically. No phantoms.
- No commit in `ab7e45a..HEAD` touches both `floatfea/` and `docs/reviews/`.
- `d4c2fe5` carries R7 alone and precedes `ba8c3c4`, as the previous verdict asked.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` (unchanged) | relative, dimensionless; rotations now enter through a characteristic length | `1.0e-7` | `floatfea/tolerances.py:309-324`. **Value unmoved.** Comment gains the unit system (SI metres) and a `cond(K~)*eps = 8.5e-14` bound. The unit-system declaration is what R2 asked for and it is there. The mechanism beside it is refuted (**R8**) and the VERIFIED claim has no guard (**R9**). |
| `PATCH_TEST_EXACTNESS_COUNTER` | `3.0e-8` | `1.0e-7` | same quantity as the assertion it controls | - | `floatfea/tolerances.py:341-355`. **A genuine tightening**, confirmed: the assertion is `err >= COUNTER`, and I re-measured all six responses to a `1e-6` defect independently - `1.0764e-07 .. 1.1743e-07`, smallest `1.0764e-07`. Margin 7.6%, unstated (**R15**). The withdrawal note beside it is right in direction, over-precise in value (**R11**). |

The counter moved in the same commit (`ba8c3c4`) as the error measure that changed
it. That is the shape the rule targets, so I checked it directly: nothing red was
made green - the change makes the negative control **stricter**, and the
measurement that sets it reproduces independently under my own harness. Not a
widening.

No other tolerance moved in `ab7e45a..HEAD`. Two *undeclared* thresholds were added
outside `tolerances.py` - see **R13**.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R8** - `tolerances.py` stops claiming unit invariance required two fixes. The
   record states what the 2x2 shows: the dimensionally homogeneous error measure is
   necessary and sufficient over `S = 1e-4 .. 1e+4`; equilibration is a ~6x floor
   improvement, justified on its own terms in `system.py` and in the closure
   artifact, or removed. **Do not change a tolerance to settle this** - no
   tolerance is implicated.
2. **R9** - the patch test is executed at more than one length unit with its error
   asserted against `PATCH_TEST_EXACTNESS` at each, so the property `tolerances.py`
   calls VERIFIED can fail. If that assertion is deliberately deferred to step 6,
   `tolerances.py` says asserted at G2.5 rather than verified, and step 6's plan
   names it before step 6 is written. The conditioning tests may stay; they are not
   a substitute, and the source-substring test is replaced by something a broken
   measure cannot satisfy.
3. **R10** - the fivefold sentence is gone from
   `tests/verification/rung1/test_patch_test.py:297-300`, line :294 quotes the
   current weakest threshold, and `docs/instrumentation.md:705-711` carries the six
   re-measured rows. `grep -rn fivefold floatfea tests docs/instrumentation.md`
   returns only the withdrawal.
4. **R12** - `docs/milestones/F2.md:51` cites AV4 as AV4 is written, marks the
   extension of each-bending-plane to the shear state as a step-4 review finding
   rather than as a locked requirement, and states the count the test runs. The
   post-lock amendment of the detailed plan is recorded somewhere a later reader
   will meet it.
5. **R13** - `rel=1e-6` (:431), `1e4` (:445) and `rel=0.05` (:320) are named
   entries in `floatfea/tolerances.py` with a class, or the tests are restructured
   so no literal decides a pass.

R4, R5, R6, R11, R14, R15 and R16 may be answered in step 5's `Carried` section
rather than before step 5 opens. R6 (`pin_threads`) remains inherited from an
ungated step 3 and should be recorded there too.

**Not a STOP.** The locked plan is not wrong, no lower rung is red, and the element
survived every adversarial case I could construct - including the two mutations that
the previous verdict's missing states were needed to catch. G2.2's *substance* is
now met: six states, two orientations, exact at `<= 8.3e-15`, with a per-plane
negative control that separates by four orders and a whole-element control at a
measured `1.08e-07`. What is not met is the record around it, in the one file the
project has singled out as needing the most discipline, and one hard rule that was
re-broken in the commit that answered the HOLD. That is a HOLD.

One standing caveat, unchanged: every instrument here was written by the same hand
as the element, against fields they share assumptions with. My own independent
derivation of `curvature_xz` and `shear_xz` shares Timoshenko kinematics with the
element it checks. Until V5.1 puts CalculiX on the other side, a run of passes means
not yet contradicted - and this step's real evidence is not the passes but the two
mutations that reddened only the new states.

**Witness channel unavailable.** No git remote is configured, so there is no PR and
no `[witness ...]` comment. Per `docs/SUPERVISOR.md` that is an unavailable check,
not a pass. Both the HOLD and this re-review were produced by a single reader; the
class of defect an outside witness exists to catch is the one where the reviewer's
own framing carries forward, and R14 - a report number that agreed with my previous
verdict only because both used the superseded measure - is a small live instance
of it.
