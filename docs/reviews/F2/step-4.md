# Review � F2 step 4
Reviewed commit: ab7e45a2cc75ac42b1bb2a837e706e124fe73224
Verdict: HOLD
Tests: 242 passed, 0 failed, 0 skipped   (my run, `pytest -q`, 0.59s)

## Carried

**There is no previous review. `docs/reviews/F2/` was empty when this review
began — step 1, 2 and 3 were never gated, and the step gating kit was installed
today (`ddabd44`) with the reports for steps 1-4 backfilled at `6709db2`.** This
section therefore records an *absence of review*, which is a different statement
from "checked, nothing carried". No verdict has ever cleared the assembly, the
element, or the transformation this gate stands on.

The dependency list was reconstructed from the step reports instead.

- **AW3** (step 3, an explicit gate: "Proceed once AW3 is answered") — the AU3
  guard sat on `Section.circular_tube`, not on the type. **Answered.** Located in
  the diff, not only in the report: `floatfea/model/material.py`
  `Section.__post_init__` (`b2f7ae9`), with `test_an_incoherent_section_is_
  REFUSED_at_construction` and its meta-test `test_the_supported_section_still_
  constructs` in `tests/unit/test_transform_invariance.py`. Both resolve.
- **AW1** (tolerance form and counter quantity) — **answered in the report,
  refuted by measurement.** See R2. The `TRANSFORM_INVARIANCE` and counter-quantity
  half is correct and located in `floatfea/tolerances.py`; the claim made about
  `PATCH_TEST_EXACTNESS` is not.
- **AW2** (undeclared `rtol=1e-10` subdivision literal) — **answered.**
  `SUBDIVISION_INVARIANCE = 1e-11` with the three measured deviations recorded.
  I did not re-measure the subdivision sweep; taken as verified by the report's
  own numbers and the tolerance comment, both located.
- **Sequencing.** `b2f7ae9`, which answers all three, is an ancestor of `e1ea251`.
  So the fixes were in the tree before the patch test landed, and the failure was
  in the *report*, not the work — the step-4 report recorded them as OPEN and
  proceeded. The revision at `ab7e45a` closes the record. That distinction is
  worth keeping straight: the gate was not executed on top of broken code, it was
  executed on top of an unwritten answer.

## Findings

**R1. The patch test does not exercise the x-z bending plane at all, and the
locked plan requires it. This is the finding.**
`tests/verification/rung1/test_patch_test.py:72-91` (`_exact_local`). All four
states live in local DOF `{0}`, `{3}`, and `{1,5}`. Local DOF `{2,4,8,10}` — the
x-z bending block — is identically zero in every state, in both orientations,
because the skew direction rotates the *global* field without giving the *local*
field any x-z content.

Measured, by perturbing one interior element's local blocks by `1e-3` (a thousand
times the counter-case) and re-running all four states:

```
perturb axial block      -> axial 1.09e-04   others <= 5.5e-15
perturb torsion block    -> twist 1.09e-04   others <= 3.4e-15
perturb x-y bending      -> curvature 3.71e-05, shear 3.01e-05, others <= 2.0e-15
perturb x-z bending      -> axial 2.9e-15  curvature 5.5e-15  twist 6.4e-16  shear 6.7e-15
                            ^ NOTHING. Not one state above the 1e-12 ceiling.
```

`floatfea/element/beam.py:148-154` builds that block as `flip @ ky @ flip` with
`flip = diag(1,-1,1,-1)`, and its own comment says "this is the sign that planar
test cases cannot see". The patch test is a planar test case. `I_y == I_z` for the
circular tube, so a swapped inertia is invisible too.

`docs/milestones/F2.md` AV4 item 2 reads "**constant curvature** (in each bending
plane)". One plane was built. G2.2 is currently declared PASS on a test that
covers half the element's bending stiffness — the guard is assertion domain
blindness: the collection the assertion inspects cannot contain the failure.

I wrote the two missing states independently (`phi_y = c x`, `w = -c x^2/2`, and
the shear analogue with the sign flip) and ran them against the same model: they
reproduce the exact field at `9.36e-16` and `1.29e-15` on the clean element, and
they detect the `1e-3` x-z defect at `3.71e-05` and `3.02e-05` — the same
sensitivity the x-y states have. Two lines each in `_exact_local`.

**Closed when** the x-z plane's constant-curvature and constant-shear states are
in the parametrisation, passing at ULP scale, with a measured per-state detection
threshold and a negative control confined to the x-z block — not a whole-element
scaling, which every state already sees.

**R2. `PATCH_TEST_EXACTNESS` is not unit-invariant. AW1's answer that it is, is an
argument the measurement contradicts — and AW1 was one of the three items this
step's revision closed today.**
`docs/reports/F2/step-4.md` (Revision, AW1) states: "None is an absolute tolerance
on a dimensional quantity, so V1.3's rescaling passes through all three: posing
the same problem in millimetres scales numerator and denominator together."

Posed in millimetres (`E` in N/mm², lengths x1000, `c` and `tau` /1000, `P`
unchanged), the same four states give:

```
scale S      axial      curvature      twist        shear     cond(K_ff)
    1     3.65e-15      3.19e-15    1.41e-15     4.19e-15      9.21e+02
   10     1.26e-15      1.26e-15    4.24e-14     1.61e-15      4.06e+03
  100     5.98e-15      1.10e-14    1.55e-13     1.24e-14      4.05e+05
 1000     1.12e-14      2.97e-14  * 1.88e-11 *   2.19e-14      4.05e+07   <- mm
0.001     1.66e-11 *    3.29e-14    1.67e-15     4.23e-14      5.98e+08   <- km
```

The twist state breaches the `1e-12` ceiling by **19x** in millimetres; the axial
state breaches it in kilometres. Its measured detection threshold in mm collapses
below `1e-14` — i.e. the assertion is red at zero perturbation, so the recorded
thresholds are not unit-invariant either.

I checked this is conditioning and not an error in my rescaling: the exact field
scales exactly (translations x1000.000000, rotations x1.000000 in every state),
and `cond(K_ff)` climbs from `9.2e2` to `4.0e7` because the translational and
rotational stiffness blocks separate by `L^2` under a length-unit change
(`EA/L` and `12EI/L^3` move in opposite directions). **Being relative makes the
numerator and denominator scale together; it does not make the round-off floor
scale with them.** That is the whole content of AW1's answer, and it does not
hold for an exactness tolerance sitting three orders above the floor.

This matters now rather than at step 6: V1.3 / G2.5 is the next-but-one step, and
it will land on exactly this. The response must not be to widen
`PATCH_TEST_EXACTNESS` — under this measurement the ceiling is a function of the
unit system, and the fix is to state what unit system it is declared in, or to
scale it with the measured conditioning, before V1.3 exerts pressure on it.

**Closed when** the unit system `PATCH_TEST_EXACTNESS` is declared against is
written into `floatfea/tolerances.py`, and V1.3's own plan says what it does with
a tolerance whose floor moves with the length unit. If the answer is that G2.5
poses the rescaled problem and asserts the *ratio* of results rather than
re-running the patch test, say so — that is a fine answer, but it must be written
before the test is.

**R3. The seventeenth guard's central claim — that removing commensurability
bought a fivefold improvement — is refuted. A UNIFORM mesh outperforms the
"irregular" mesh it replaced.**
`docs/instrumentation.md` § Seventeenth, `tests/verification/rung1/test_patch_test.py:53-57`
and `:206-209`, and `floatfea/tolerances.py` (the `_COUNTER` comment). All four
say the `1.51e-10 -> 3.31e-11` gain came from removing symmetry cancellation.

Measured in the counter-case's own quantity — interior-field error from a `1e-6`
single-element stiffness defect, weakest state:

```
old mesh   [1.7 0.6 2.8 0.9 3.1]  (contains 3/2 exactly)   6.60e-09
UNIFORM    [1.934 x 5]  (every ratio exactly 1/1)          1.90e-08   2.9x better
current    [3.27 3.00 0.90 0.79 1.71]  (incommensurate)    3.02e-08   1.6x better
                                                                      than uniform
```

The maximally commensurate mesh recovers 2.9 of the 4.6x. Detection thresholds
agree: uniform `5.27e-11` weakest, current `3.30e-11` — and on the axial and twist
states the uniform mesh is *better* (`8.33e-12` vs `9.17e-12`). The uniform mesh
also reproduces all four states at `<= 8.8e-16`, four orders inside the ceiling.

So the docstring's stated mechanism — "a uniform mesh cannot distinguish an
element that is exact from one that is merely consistent, because the errors
cancel by symmetry" — is false as written, and the gain the guard claims for
incommensurability is mostly attributable to something else (the old mesh's
`0.6 m` element and its shorter total length). The *guard itself* — write the
check from the property, not from the defects you met — is sound and I am not
asking for it to be withdrawn. Its supporting measurement is the problem, and it
now sits in the project's permanent instrumentation record, where it will be
cited.

**Closed when** the fivefold figure in `docs/instrumentation.md`, the test
docstring and the `_COUNTER` comment is either re-attributed to the variable that
actually carries it, or replaced by the three-mesh comparison above with the
honest conclusion that commensurability is worth ~1.6x. `test_the_mesh_is_actually
_irregular` may stay; its rationale may not stay as written.

**R4. The counter-case the plan named for this gate was never executed, and half
the parametrisation is blind to it.**
`docs/milestones/F2.md` D5 names `PATCH_TEST_STRAIN` with counter-case "one
element's transformation transposed". The entry shipped as `PATCH_TEST_EXACTNESS`
with a different counter (a uniform element-stiffness scaling). I ran the named
one — `to_global(k_loc, R.T)` on element 1:

```
skew          axial 4.60e-01  curvature 1.01e-01  twist 2.91e-01  shear 1.10e-01
axis-aligned  axial 5.61e-17  curvature 8.35e-16  twist 1.87e-16  shear 8.28e-16
```

Detected, but **only by the skew orientation** — the axis-aligned half of the
parametrisation cannot see a transposed transformation at all. That is fine as
long as it is known; it is not currently written anywhere, and the D5 row still
names a tolerance that does not exist.

**Closed when** D5's row is reconciled with the shipped name, and the
orientation-dependence of the transformation counter-case is recorded.

**R5. `assert res.residual <= PATCH_TEST_EXACTNESS` (line 147) is a green
assertion that cannot fail for anything this test targets.**
`res.residual` is `||K_ff u_f - f_f|| / ||f_f||`, a linear-solve residual.
Measured: `5.93e-16` clean, `4.70e-16` with a `1e-3` element defect — it goes
*down* under the defect. It also compares a solver residual against a tolerance
whose recorded form, provenance and counter are all in a different quantity
(displacement-field deviation), which is the AW1 discipline running the other way.
Harmless, but it reads as a second check and is not one.

**Closed when** it is either removed or given its own named tolerance with its own
measurement.

**R6. D6 is not discharged: `determinism.pin_threads(1)` is never called.**
D6 says "`determinism.pin_threads(1)` before numpy import in the verification
conftest". `grep` finds it defined at `floatfea/determinism.py:90` and called only
from `tests/verification/rung3/test_determinism_pins.py:24`, which tests the
function rather than applying it. `tests/conftest.py` does not call it.
`SPARSE_PERMC_SPEC` *is* used in `solve`. Carried from step 3, never gated.

**Closed when** the conftest pins threads, or D6 records why it does not.

**R7. The locked gate description was rewritten in the same commit as the work it
describes.** `e1ea251` edits `docs/milestones/F2.md:51`, replacing G2.2's statement
of what it proves ("a constant strain state recovered exactly. Catches assembly,
transformation and connectivity errors") with its outcome ("all four
constant-strain states ... **PASS**: `2.88e-17 .. 4.21e-15`"). Recording a result
is legitimate; overwriting the gate's scope with it is how a gate quietly narrows,
and here it matters — the replacement wording is what makes R1 look satisfied.

**Closed when** the gate's statement of what it proves is restored alongside the
result, and the result line is reconciled with R1.

---

**What I verified positively**, so the above is not read as the whole picture:

- I re-derived all four exact fields independently of `_exact_local` and got the
  same pass. Stronger, I checked the patch-test property directly and by a
  different route: assembling `K`, imposing the exact field at **every** node, and
  measuring the out-of-balance force at the interior DOF. Relative to `|K|·|u|` it
  is `4.5e-18 .. 4.7e-17` across the four states and both orientations. The
  element genuinely reproduces these states; nothing in R1-R7 disputes that.
- **The form is genuinely displacement-driven.** `f = -(k @ u_pres)` with
  `u_pres` supported only on the end DOF is the standard static-condensation
  elimination term: `f_f = -K_fp u_p`, so `u_f = -K_ff^{-1} K_fp u_p`. The only
  free DOF where `f` is non-zero are node 1's, and they are non-zero because node 1
  is adjacent to a prescribed node — not because a load was applied. External load
  on the interior is zero, as claimed. This was the thing I was asked to look at
  hardest and it holds.
- **State 4 does the job claimed for it.** Substituting an Euler-Bernoulli element
  (`Phi := 0`): axial `5.13e-15`, curvature `5.41e-15`, twist `1.11e-15` — all pass
  — and shear `9.91e-04`, four orders wrong. Only state 4 discriminates. The shear
  content of state 4 is `6.75e-03` of the tip response against the meta-test's
  `1e-4` bar, so that bar is 67x conservative but not vacuous.
- **The counter-case reproduces exactly.** My independent measurement of the `1e-6`
  responses: `1.09e-07`, `1.09e-07`, `3.72e-08`, `3.02e-08`. The comment in
  `tolerances.py` says `1.09e-07`, `1.09e-07`, `3.72e-08`, `3.02e-08`. Counter set
  at the smallest. That number is real.
- Every test named in the report and the revision resolves to a real test at the
  path given, checked mechanically. No phantoms.
- No commit in this range touches both `floatfea/` and `docs/reviews/`.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS` | — | `1e-12` | relative, `max abs deviation / max abs exact field` — dimensionless | `3.0e-8` | `floatfea/tolerances.py:292-314`, with the eight measured values. New entry for a new test, **not** a widening. |
| `PATCH_TEST_EXACTNESS_COUNTER` | `6.0e-9` | `3.0e-8` | same quantity as the assertion | — | `floatfea/tolerances.py:316-329`. **Tightened**, not widened: the assertion is `err >= COUNTER`, so raising it makes the negative control stricter. I reproduced all four underlying measurements independently. |

Both changes are in the same commits as the code they describe (`e1ea251`,
`eba50cf`). For a *new* tolerance on a *new* test that is unavoidable and not the
pattern the rule targets — nothing red was made green. **But** `PATCH_TEST_EXACTNESS`'s
recorded form is where R2 lands: it is dimensionless, and it is still not
unit-invariant, and the tolerance comment does not say so.

The counter's re-measurement justification ("removing that symmetry improved the
weakest state's sensitivity about fivefold") is the claim R3 refutes. The *value*
`3.0e-8` is correct and independently reproduced; only its stated cause is wrong.

No other tolerance moved in `170cb52..HEAD`.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R1** — the x-z bending plane is in the patch test: constant curvature and
   constant shear in that plane, exact at ULP scale, with a negative control
   confined to the x-z block and a measured detection threshold per new state.
   G2.2 stays open until then; the gate as locked asks for each bending plane.
2. **R2** — `PATCH_TEST_EXACTNESS` carries the unit system it was measured in, and
   the AW1 answer in `docs/reports/F2/step-4.md` is corrected to say that a
   relative tolerance is not thereby unit-invariant. V1.3's approach to it is
   stated before V1.3 is written. **Do not widen the tolerance to absorb this.**
3. **R3** — the fivefold commensurability claim in `docs/instrumentation.md`, the
   test docstring and the `_COUNTER` comment is corrected against the three-mesh
   measurement, or re-attributed to whatever actually carries it.
4. **R7** — G2.2's row in `docs/milestones/F2.md` states what the gate proves as
   well as its result, consistent with (1).

R4, R5 and R6 may be answered in the step-5 report's `Carried` section rather than
before step 5 opens. R6 (`pin_threads`) is inherited from an ungated step 3 and
should be recorded there too.

**Not a STOP.** The locked plan is not wrong, no lower rung is red, and the element
survived every adversarial case I could pose inside the plane it is tested in. The
gate is incompletely executed and two written claims are refuted by measurement —
that is a HOLD.

One standing caveat, per the recorded guard: every instrument here was written by
the same hand as the element, against closed forms they share assumptions with.
Until V5.1 puts CalculiX on the other side, a run of passes means "not yet
contradicted". This step produced three contradictions in one afternoon of looking,
which is the argument for looking.

**Witness channel unavailable.** No git remote is configured, so there is no PR and
no `[witness ...]` comment. Per `docs/SUPERVISOR.md`, that is an unavailable check,
not a pass. The class of failure the outside witness exists to catch — a step
executed on top of an unanswered gate — is precisely what the `Carried` section
above records for steps 1-3, and no second reader has seen any of it.
