# Review � F2 step 4
Reviewed commit: 1acb5dcdbf8c5feeffa78d623cd4bb49c89b085b
Verdict: HOLD
Tests: 289 passed, 0 failed, 0 skipped   (my run, `pytest -q`, 0.67s)

R10, R11 and R14 are genuinely closed and I reproduced every number behind them.
R12 is closed in substance. R8 and R9 are not, and R13 is not — and in each case
the *shape* of the miss is the one the recorded guards name. R8's correction
reached `tolerances.py` and `F2.md` but not the two places the previous verdict
pointed at, and the retained justification for a production-path change is itself
an unablated causal claim: I removed equilibration from `solve()` and the suite
stayed at 289 green. R9's behavioural replacement passes when the pre-R2 mixed
measure is restored. R13's scanner reads the third literal it was written for as
clean, misses 13 of 15 planted shapes including two live in the two files this
commit edited, and its `# not-a-tolerance:` hatch stamps the category "not a
tolerance" onto eleven two-sided accuracy comparisons — one of which is the exact
expression the scanner's own docstring uses to define what IS a tolerance. And the
consolidation loosened three assertions by 100x while the report says none moved.

## Carried

Every item from `docs/reviews/F2/step-4.md` (HOLD @ `ec8b237`), traced into
`ec8b237..HEAD` rather than taken from the report.

- **R8 (blocking) — PARTIALLY answered.** `floatfea/tolerances.py:309-330` now
  carries the one-at-a-time table instead of the necessity claim, and
  `docs/milestones/F2.md:890-913` records it. I reproduced the table independently
  through my own harness — worst error over six states and `S = 1e-4 .. 1e+4`:
  `equil+weighted 3.194e-14` (0 breaches), `weighted only 2.004e-13` (0 breaches),
  `equil only 2.086e-11` (3 breaches, first at `S = 1e-4`), `neither 2.072e-10`
  (4 breaches). Every figure in the shipped table is correct to three digits. What
  is not answered: the refuted sentence still stands in two places (**R23**) and
  the replacement justification is unverified and un-operating-pointed (**R24**).

- **R9 (blocking) — NOT answered.** Neither branch of the "closed when" was taken.
  `_run` is still never called with a scale — the five call sites are all at
  `S = 1` — so no test poses the patch test in another unit system and asserts
  against `PATCH_TEST_EXACTNESS`. And `tolerances.py:308-310` still says
  **VERIFIED** invariant `S = 1e-4 .. 1e+4, worst error 3.19e-14`, not "asserted at
  G2.5". The number is right; I measure `3.194e-14`. It is unguarded, and the new
  guard written to guard it is vacuous — **R22**.

- **R10 (blocking) — ANSWERED, verified mechanically.** Grepping `fivefold`,
  `FIVEFOLD`, `0.848`, `3.7161e-02`, `3.0170e-02`, `2.69e-11` and `3.31e-11` across
  `floatfea tests docs` outside `docs/reviews/` returns only withdrawal contexts
  (`tolerances.py:357`, `test_patch_test.py:301`, `instrumentation.md:665,667,682,
  723`) plus the report's superseded revisions, which are history. The stale
  `~3.3e-11` sentence at the old :294 is gone. `instrumentation.md:712-720` carries
  six re-measured rows and I reproduce all six sensitivities and thresholds. One
  refuted sentence survives at :671-672 — recorded as **R26**, not blocking.

- **R11 (recordable) — ANSWERED.** `0.848` is replaced by a spread in all three
  places (`tolerances.py:357-360`, `instrumentation.md:675-685`,
  `test_patch_test.py:16-19` and :240-243) and the conclusion is stated without the
  precision. Residue in **R26**.

- **R12 (blocking) — ANSWERED in substance, one clause open.**
  `docs/milestones/F2.md:51` now says AV4 item 2 requires curvature in each plane
  (checked against AV4 at :726, "**constant curvature** (in each bending plane)"),
  says the shear-per-plane extension is "which AV4 does not require", and states
  **six** — which matches the shipped parametrisation at :222. The second clause —
  record the post-lock amendment where a later reader meets it — was not done; see
  **R27**.

- **R13 (blocking) — NOT answered.** Five sub-failures, each demonstrated:
  **R17** (the consolidation loosened three assertions), **R18** (`rel=0.05`, the
  third literal R13 named, is still bare and the scanner exempts it), **R19** (the
  scanner misses the shapes it polices, two of them live), **R20** (the annotation
  hatch mis-classifies eleven lines), **R21** (three dead counters).

- **R14 (recordable) — ANSWERED.** `instrumentation.md:712-724` and
  `test_patch_test.py:287-298` regenerated. Independently reproduced: block-confined
  `1e-3` defect gives `bending_xy -> curvature 1.0756e-04, shear 1.1734e-04` and
  `bending_xz -> curvature_xz 1.0756e-04, shear_xz 1.1734e-04`, matching the
  report's table. `CLAUDE.md:105-109` now requires regeneration. Good.

- **R15 (recordable) — still open**, as permitted. The 1000x margin on
  `test_a_defect_in_ONE_bending_plane_is_caught_by_THAT_plane`, the 7.6% margin on
  `PATCH_TEST_EXACTNESS_COUNTER`, and the stubby-configuration caveat are still
  unwritten. `test_the_four_constant_strain_states_are_EXACT` still says "four" and
  runs six (`:224`). Deferred to step 5.

- **R16 (note for step 12) — still open.** `assemble/system.py:55` unchanged.

- **R4, R5, R6 — still open**, as permitted. `docs/milestones/F2.md:775` still
  names `PATCH_TEST_STRAIN`; `test_patch_test.py:234` still asserts
  `res.residual <= PATCH_TEST_EXACTNESS`; `pin_threads` is still called only from
  `tests/verification/rung3/test_determinism_pins.py`. Deferred to step 5.

## Findings

**R17. The consolidation loosened three assertions by 100x, and the report says no
value moved.**
`docs/reports/F2/step-4.md:412` — "No value loosened: each declared entry sits at
or below every literal it replaced." Checked against the diff, it is false in three
places, all replacing `1e-14` with `ROUNDOFF_IDENTITY = 1e-12`:

```
tests/unit/test_beam_element.py:181         atol=1e-14*|flex|.max()  ->  1e-12*|flex|.max()
tests/unit/test_beam_element.py:185         rel=1e-14                ->  rel=1e-12
tests/unit/test_transform_invariance.py:65  atol=1e-14               ->  atol=1e-12
```

Nothing forced it. I measured all three sites: flexibility asymmetry `3.746e-17`,
`|flex[2,4]-flex[4,2]| / |flex[2,4]| = 1.894e-16`, and
`|SKEW @ SKEW.T - I|.max() = 4.816e-17`. The old `1e-14` had 53x to 267x headroom at
every one of them. A shared constant is the right idea; it had to be set at the
*tightest* literal it absorbs, not the loosest. `ROUNDOFF_IDENTITY`'s own comment
records the sites at `4.9e-15` without noticing that three of them were previously
asserted a hundred times tighter than the new value.

Two of the three are also now vacuous for a second reason. `pytest.approx` carries a
default `abs=1e-12`; at :185 the compared quantities are `1.4e-07`, so the effective
ceiling is `1e-12` absolute — a *relative* ceiling of `7.2e-06` on a Maxwell-Betti
check whose true residual is `1.9e-16`. The entry declares itself "Dimensionless in
every use"; at that site it acts as an absolute tolerance on a quantity in m/N.

**Closed when** `ROUNDOFF_IDENTITY` sits at or below the tightest literal it
replaces (or the three sites keep a separate, tighter declared entry), and CLAUDE.md
§ Tolerances' written justification for any value that did move is in the closure
artifact. No test is red; this is not a rescue, which is why it can be fixed
straight.

**R18. R13's third named literal is still bare, and the new scanner exempts it by
accident.**
`tests/verification/rung1/test_patch_test.py:322` —
`pytest.approx(PATCH_TEST_EXACTNESS, rel=0.05)`. R13 named it explicitly and the
"next step opens when" listed it. It is unchanged and unannotated, and
`_offending_lines` returns `[]` for the whole file.

The mechanism is `tests/test_no_tolerance_literals.py:72`:
`if not any(n in line for n in names)` — a line is cleared if *any* uppercase name
from `floatfea.tolerances` appears anywhere on it, including inside the failure
message. Planted and run against the shipped scanner:

```
assert err == pytest.approx(PATCH_TEST_EXACTNESS, rel=0.05)   MISSED
assert err == pytest.approx(PATCH_TEST_EXACTNESS, rel=0.99)   MISSED
assert err < 1e-3, f"above {PATCH_TEST_EXACTNESS}"            MISSED
assert err < 1e-3, "msg"                                      CAUGHT
```

Of the eight lines in the repo currently cleared by that heuristic, seven are the
benign `rtol=0` beside a declared `atol=`, and the eighth is precisely the one R13
named. The heuristic exists to avoid flagging the declared name; it must clear only
the literal that *is* that name's value, not the line.

**Closed when** the check is per-literal rather than per-line, and `rel=0.05` at
:322 is a declared entry — it is a real accuracy tolerance: 5% agreement between the
recorded detection threshold's predicted and measured error, worst measured 0.67%.

**R19. The scanner misses the shapes it is written to police, and two of the misses
are live in the two files this commit edited.**
`tests/test_no_tolerance_literals.py:59-77`. I planted fifteen shapes; thirteen were
missed:

```
MISSED  np.testing.assert_allclose(a, b, atol=1e-12)     line does not start "assert "
MISSED  assert_allclose(a, b, rtol=1e-9)                 same
MISSED  assert math.isclose(a, b, rel_tol=1e-9)          "rel_tol"/"abs_tol" not in the keyword set
MISSED  assert math.isclose(a, b, abs_tol=1e-9)
MISSED  assert np.allclose(a, b)                         numpy default rtol=1e-5
MISSED  assert a == pytest.approx(b)                     pytest defaults rel=1e-6, abs=1e-12
MISSED  TOL = 1e-9 ... assert err < TOL                  literal hoisted one line
MISSED  assert spread > 10000                            integer form of the flagged "> 1e4"
MISSED  assert (\n err\n < 1e-9\n)                       continuation heuristic drops out
MISSED  assert np.linalg.matrix_rank(k, tol=...) == 2    "tol=" not in the keyword set
MISSED  self.assertAlmostEqual(a, b, delta=1e-9)
MISSED  if abs(a-b) > 1e-9: raise AssertionError
CAUGHT  assert d["x"] == pytest.approx(1.0, abs=1e-9)
CAUGHT  assert err < 5e-3 * scale
```

Two are not hypothetical:

- `tests/unit/test_beam_element.py:84` and `:105` —
  `np.linalg.matrix_rank(k, tol=1e-9 * abs(k).max()) == 2` / `== 6`. A rank
  threshold that decides a pass, sitting one line below `atol=1e-9 * abs(k).max()`
  on the same matrix, which *this commit* declared as `MATRIX_SYMMETRY`. The same
  number, the same expression, one line apart; one declared, one invisible.
- `tests/unit/test_member_local_axes.py:70, 71, 72, 83` —
  `np.testing.assert_allclose(..., atol=1e-12)`. Line :83 sits immediately under
  :80-82, which this commit converted to `ROUNDOFF_IDENTITY`. Identical assertion,
  identical value, never scanned because the statement does not begin with
  `assert `.

The `> 10000` / `> 1e4` split is worth naming on its own: the file flags
`test_patch_test.py:447`'s `> 1e4` (annotated) and would not flag the identical
threshold written `> 10000`. A check whose coverage depends on notation invites the
notation.

**Closed when** the scan is over the parsed AST of the whole assertion statement —
or at minimum covers the `assert_*`/`isclose`/`allclose` call families, the
`tol=`/`rel_tol=`/`abs_tol=`/`delta=` keywords, and library defaults for `approx`
and `allclose` — the four live sites above are declared or annotated, and
`test_the_scanner_detects_a_known_violation` carries at least the `assert_allclose`,
`tol=` and multi-line shapes rather than only the two shapes R13 already found. A
control drawn from the defects already met is a test of those defects;
`docs/instrumentation.md:657-658` says exactly this about the mesh check.

**R20. The `# not-a-tolerance:` hatch stamps a false category onto eleven accuracy
comparisons, including the one the scanner's own docstring uses to define a
tolerance.**

The direction test is the whole of it: a tolerance is a threshold that hides a
discrepancy when widened. Applied to the 28 annotated lines:

- **Correct, 15 lines.** Every "discrimination floor" (`> 0.05`, `> 1e-4`, `> 1e4`,
  `> 0.15`, `> 1e-3`) and every "negative control" (`assert not np.allclose(...)`,
  `!= pytest.approx(...)`, `mm < m/100`) is red-when-widened. These are sound and
  the annotation earns its keep.
- **False, 11 lines.** Every `x == pytest.approx(v, abs=e)` labelled "reference pin,
  not a ceiling": `test_cantilever_closed_form.py:156, 164`;
  `test_basis_constants.py:27, 32, 33, 63, 98, 116`; `test_live_dof.py:80, 81`;
  `test_reference_provenance.py:34`. Each is a two-sided accuracy comparison; each
  hides a discrepancy when `abs=` grows. `abs=5e-4` on
  `kappa("thin_tube", 0.3) == 0.5305` is the tolerance against Cowper (1966)
  Table 1 — the one number that decides whether the shear coefficient is right.

  `test_reference_provenance.py:34` is `pytest.approx(0.486, abs=5e-3)`, and
  `tests/test_no_tolerance_literals.py:29-32` says of that exact expression:
  "`5e-3` is a COMPARISON EPSILON, which `CLAUDE.md` names explicitly as a
  tolerance. Only the second is in scope." The scanner's definition and the
  annotation contradict each other on the same line of the same commit.

- **Wrong reason, 3 more.** `test_basis_constants.py:99` and
  `test_cantilever_closed_form.py:165` are labelled "fixture property — bounds an
  input"; both bound a value computed by production code
  (`sec.shear_geometric_bound(fy)`, `shear_parameter(...)`), not an input.
  `test_live_dof.py:80` is labelled "the recorded contaminated values" but compares
  two statistics both computed at runtime (`naive` against the parametrised
  `contaminated`).

This is the predictable failure of an annotation escape hatch, and the classifier
was crude enough that four annotations already needed hand repair; the eleven above
are the ones that were not repaired.

**Closed when** the eleven `pytest.approx(..., abs=)` epsilons are declared entries
— a single quantisation entry with its rule ("half the last quoted digit of the
cited value") would cover most of them, but then the rule has to hold: `abs=5e-6` on
`0.006043`, `abs=0.1` on `59.6` and `abs=1e-4` on `1.1111` are 5, 2 and 1 units in
the last place, not half — or the "reference pin" category is retired and each line
justifies its own epsilon in `tolerances.py`.

**R21. Three of the three new counters are dead values.**
`MATRIX_SYMMETRY_COUNTER`, `ROUNDOFF_IDENTITY_COUNTER` and
`COND_UNIT_INVARIANCE_COUNTER` appear nowhere outside `floatfea/tolerances.py` —
checked with `grep -rn` across `floatfea` and `tests`. The three counters that
pre-date this step (`PATCH_TEST_EXACTNESS_COUNTER`, `SUBDIVISION_INVARIANCE_COUNTER`,
`TRANSFORM_INVARIANCE_COUNTER`) are all asserted. The guard is "the counter-case is
an executable value, not a sentence"; these are sentences.

`COND_UNIT_INVARIANCE_COUNTER`'s own comment says so: "the assertion must catch
anything at or above that ratio; the counter is set far below it". A value set far
below what must be caught is not the smallest detected defect — it is unmeasured.
`ROUNDOFF_IDENTITY_COUNTER = 1.0e-8` cites "the non-orthogonal `I + [theta x]` map
at theta = 1e-8", but no assertion in the repo applies `ROUNDOFF_IDENTITY` to that
quantity; the site that does (`test_transform_invariance.py:137`) uses a bare
`atol=1e-6` and is annotated as a negative control.

**Closed when** each of the three counters is the argument of an assertion that
reddens on it, in the same quantity as the tolerance it controls, and the measured
detection threshold — not a round number below it — is what is recorded.

**R22. R9's behavioural replacement passes when the pre-R2 mixed measure is
restored. It cannot detect the defect it exists for.**
`tests/verification/rung1/test_patch_test.py:472-486`.

`m` and `mm` are both `4.1509e-12`. The assertion is
`m == pytest.approx(mm, rel=ROUNDOFF_IDENTITY)`, i.e. `rel = 1e-12`, giving a
relative allowance of `4e-24` — but `pytest.approx` applies
`max(rel*|expected|, abs)` with an undeclared default `abs = 1e-12`, which is
*larger than the quantities being compared*. I substituted weightings into
`relative_error` and re-ran the assertion:

```
w[3:] = char_length      (shipped)   m=4.1509e-12  mm=4.1509e-12   PASS
w[3:] = 1.0     (THE PRE-R2 MIXED MEASURE)
                                     m=4.2926e-13  mm=4.2926e-16   PASS  <- 1000x unit drift, undetected
w[3:] = 0.0*char_length  (the sabotage the docstring names)
                                     m=0.0         mm=0.0          PASS
w[3:] = 1e-30*char_length            m=4.15e-42    mm=4.15e-42     PASS
w[3:] = char_length**2                                             FAIL
w[3:] = sqrt(char_length)                                          FAIL
w[3:] = 9.67  (hardcoded)                                          FAIL
```

The structural test this replaced could be satisfied by `w[3:] = 0.0 * STATIONS[-1]`.
So can this one. And worse: the mixed measure — metres and radians under one
`max()`, which is the entire subject of R2 — drifts by a factor of 1000 between the
two unit systems and the assertion does not notice, because both numbers sit under
the hidden absolute floor. The pass is decided by an undeclared `abs=1e-12` that
pytest supplies, in the same step whose companion commit made undeclared tolerances
a test.

Two smaller points in the same block. `test_a_MIXED_unit_measure_would_FAIL_that`
(:489-499) defines `mixed` locally, so it exercises a function no production or test
path can regress — it demonstrates the concept and guards nothing. And
`w[3:] = 0.0*L` *does* redden the six-state gate, through the twist state's
zero-translation denominator going to `inf`, so the suite catches that particular
mutation elsewhere; the docstring's claim that this test covers it is still wrong.

**Closed when** the assertion is posed on a quantity of order one — the ratio
`m/mm` against 1, or `m` and `mm` normalised — so the declared relative tolerance is
what decides it, and `w[3:] = 1.0` is confirmed to turn it red. R9's original
"closed when" also still stands: either the patch test runs at more than one length
unit with its error asserted against `PATCH_TEST_EXACTNESS` at each, or
`tolerances.py:308` stops saying VERIFIED and says asserted at G2.5, with step 6's
plan naming it.

**R23. R8's correction did not reach the two places the previous verdict named, and
the refuted sentence still stands verbatim in both.**
The diff `ec8b237..HEAD -- floatfea/` touches `tolerances.py` only.

- `floatfea/assemble/system.py:50-53`, the docstring of `equilibrate` on the
  production path: "Without it an exactness tolerance is **not unit-invariant** even
  when it is relative -- being relative scales numerator and denominator together,
  but it does not scale the round-off floor with them." Row 2 of the ablation, which
  I reproduced (equilibrate NO, weighted measure: worst `2.004e-13`, zero breaches
  of `1e-12` anywhere in `S = 1e-4 .. 1e+4`), refutes it directly. `:153-155`
  repeats it: "This makes the conditioning -- and therefore **the achievable
  accuracy** -- independent of the length unit." R8's "closed when" said the honest
  justification "belongs in `system.py` and the closure artifact". `system.py` was
  not opened.
- `tests/verification/rung1/test_patch_test.py:392-393`: "**Both had to be fixed for
  that to hold**, and neither fix was a tolerance change." That is the "required two
  fixes" claim, unchanged, in the file the R8/R9 commit rewrote, ten lines above the
  tests it introduces. This is R10's shape exactly -- a corrected claim surviving in
  a comment a few lines from its correction -- one commit after R10.

**Closed when** both sentences say what the ablation measured, and the closure
artifact carries equilibration's justification.

**R24. The retained justification for equilibration is not under test, and the "6x"
has no operating point. The new guard applied to the answer to R8.**
`floatfea/tolerances.py:326-330`: "EQUILIBRATION IS RETAINED ON A DIFFERENT
JUSTIFICATION ...: a measured 6x reduction in worst error (3.19e-14 against
2.00e-13) and cond(K~) = 3.85e2 at every unit system ... **Both are under test.** It
would be removed if either stopped holding." The report repeats "both under test".

The ablation for that claim: I copied the tree, deleted the three equilibration
lines from `solve()` (`system.py:156-158`) so the solver factorises `kff` directly,
and ran the suite. **`289 passed`.** Nothing reddens. The two conditioning tests call
`equilibrate()` directly, so they pass whether or not the solve uses it; the 6x floor
improvement is asserted nowhere. So neither half of the retained justification is
under test, and the promise to remove it if either stopped holding has no mechanism.
This is the "provenance, not existence" guard: a pass cannot show that equilibration
reaches the solve.

And the 6x is a ratio between two worst-over-nine-decades values taken at different
scales. Per unit system, worst over six states, unequilibrated over equilibrated:

```
S       1e-4   1e-3   1e-2   1e-1     1      10    100    1e3    1e4
ratio   9.93   5.84   3.87   5.10   1.58   1.08   0.77   1.97   1.69
```

At `S = 1`, the unit system the model is actually posed in, equilibration buys
`1.58x`. At `S = 100` it is `0.77x` -- the equilibrated error is 30% *larger*. "A
ratio carries its operating point": `6x` is neither the typical nor the production
figure, it is the ratio of two extremes. The qualitative statement the numbers
support is that the floor improves by roughly 4x-10x in the extreme unit systems and
by about 1.6x at `S = 1`, and that it is not monotone.

**Closed when** the comment states the range with its operating point rather than a
single `6x`, and either the "under test" claim is removed or an assertion exists that
reddens when `solve()` stops equilibrating -- a per-scale floor assertion would do
both jobs and would also close R9.

**R25. (recordable) Report counts do not reconcile.** The report cites "27 lines
annotated" and "14 literals replaced"; I count 28 `# not-a-tolerance:` lines under
`tests/` -- 26 of which suppress an actual regex match, two being decorative -- and
15 literal-to-name substitutions in `f8a99d1`. Small, but the counts are the
evidence that the sweep was exhaustive.

**R26. (recordable) Two stale numbers in `docs/instrumentation.md`.**
- `:727` -- "perturbing by the threshold lands the error on the declared ceiling to
  within **0.3%**". Measured, per state: `0.56 / 0.67 / 0.04 / 0.54 / 0.17 / 0.11 %`.
  The worst is 0.67%. Same sentence, same section, that the previous verdict already
  had to correct once for the old `3.3e-11`.
- `:671-672` -- "element 1 exactly `2.0 m` and total exactly `10.0 m` in **both**
  meshes, **so only commensurability varies**". That is the sentence R11 refuted:
  element 1's *position* differs between the two meshes, and at index 1 in a
  five-element mesh anchored at the origin it cannot be held fixed without making the
  mesh commensurate. It sits directly above the block that now correctly reports the
  spread.

**R27. (recordable) The detailed plan is still marked DRAFT and the post-lock
amendment is still unrecorded.**
`docs/milestones/F2.md:470` -- "**Status:** DRAFT, awaiting review." Four steps have
been executed against it, and AV4 -- cited as a locked requirement by the G2.2 scope
cell -- entered the file at `170cb52`, during step 3, after the 2026-08-30 lock. A
grep for "post-lock", "after the lock" and "amended" finds nothing. This is R12's
second clause. Not a STOP: the gates and the lock Q&A above :465 are unchanged and
AV4 is a strengthening. But a plan that says "awaiting review" while it is being
executed is the state CLAUDE.md section Working agreement forbids, and a later
reader has nothing to tell them which parts arrived when.

---

**What I verified positively**, so the above is not read as the whole picture:

- All 289 tests pass in my run. Six states, two orientations, worst clean error at
  `S = 1` is `7.937e-15` (axial, skew) against `1e-12` -- matches the report exactly.
- The R8 ablation table in `tolerances.py:316-320` reproduces to three digits under
  my own harness, including the breach location (`S = 1e-4`, axial). The physics
  claim it makes -- the error measure alone is necessary and sufficient -- is
  correct, and it is the single most valuable thing in this diff.
- All six detection thresholds reproduce (`9.17 / 9.29 / 9.17 / 8.52 / 9.29 /
  8.52e-12`), and perturbing by each lands the error on `1e-12` to within 0.67%.
- All six block-confined `1e-3` responses reproduce (`1.0756e-04` / `1.1734e-04` in
  plane, `1.4e-14` / `2.5e-16` out of plane) -- R14's correction is right and the
  control separates by ten orders.
- `relative_error` is well-behaved at both degenerate ends: for a field with zero
  rotational content (axial) the denominator is the translational scale; for zero
  translational content (twist) it is the rotation magnitude times `char_length`,
  and both scale with `S`, so the measure stays invariant. An all-zero field gives
  `nan`, which fails the assertion loudly rather than passing. No finding.
- The 15 discrimination-floor and negative-control annotations are sound -- I
  checked each for red-when-widened.
- `MATRIX_SYMMETRY = 1e-9` is not a widening: it replaced two `1e-9` literals
  exactly, and the measured element asymmetry is `0.0`.
- `COND_UNIT_INVARIANCE = 1e-6` replaced R13's bare `rel=1e-6` at the same value.
- Every test cited in the report and in `tolerances.py` resolves to a real test at
  the path given, checked mechanically. No phantoms.
- No commit in `ec8b237..HEAD` touches both `floatfea/` and `docs/reviews/`, and
  `f8a99d1` (R13) precedes `f53a420` (R8-R14).
- Adversarial cases that did **not** produce a finding: the full six-state gate at
  `S = 1e-4 .. 1e+4` through an independently written harness (no breach, worst
  `3.19e-14`); the axis-aligned orientation; the all-zero field; the stubby
  configuration re-run from the previous verdict.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` (unchanged) | relative, dimensionless | `1.0e-7` | `floatfea/tolerances.py:309-337`. **Value unmoved.** The refuted "two fixes" mechanism is replaced by the ablation table, which I reproduce exactly. Still says **VERIFIED** with nothing that can falsify it (**R9**, **R22**); the retained justification for equilibration is untested and un-operating-pointed (**R24**). |
| `MATRIX_SYMMETRY` | -- | `1e-9` | relative to the largest entry, dimensionless | `1.0e-2`, **unused** (**R21**) | `floatfea/tolerances.py:369-380`. Replaces the `1e-9` factor at `test_beam_element.py:83, 103` at the identical value. Not a widening. Measured element asymmetry `0.0`, assembled `2.4e-16` -- reproduced. |
| `ROUNDOFF_IDENTITY` | -- | `1e-12` | declared relative and dimensionless; acts as an absolute at three sites | `1.0e-8`, **unused** (**R21**) | `floatfea/tolerances.py:383-401`. Replaces ten literals. Seven were `1e-12` -- no change. **Three were `1e-14`** (`test_beam_element.py:181, 185`; `test_transform_invariance.py:65`) -- a **100x widening** (**R17**), with 53x to 267x headroom already available at those sites. Not a rescue of a red test, but the report claim "no value loosened" is false and the CLAUDE.md written justification does not exist. |
| `COND_UNIT_INVARIANCE` | -- | `1e-6` | relative on a condition number, dimensionless | `1.0e-3`, **unused**, and its own comment says it is set far below what must be caught (**R21**) | `floatfea/tolerances.py:404-417`. Replaces the bare `rel=1e-6` R13 named, at the same value. Not a widening. |

Undeclared thresholds still deciding a pass, outside `tolerances.py`:
`test_patch_test.py:322` `rel=0.05` (**R18**); `test_beam_element.py:84, 105`
`tol=1e-9 * abs(k).max()` (**R19**); `test_member_local_axes.py:70, 71, 72, 83`
`atol=1e-12` (**R19**); and the `pytest.approx` default `abs=1e-12`, which is what
actually decides `test_patch_test.py:483` and `test_beam_element.py:185`
(**R22**, **R17**).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R17** -- `ROUNDOFF_IDENTITY` sits at or below the tightest literal it absorbs,
   or the three `1e-14` sites carry their own tighter declared entry, and the report
   claim "no value loosened" is corrected. **Do not resolve this by re-checking that
   the tests still pass** -- they pass either way; the question is what the assertion
   can still catch.
2. **R18** -- the scan clears a *literal* that equals a declared tolerance, not a
   *line* on which a tolerance name appears; and `rel=0.05` at
   `test_patch_test.py:322` is a declared entry with its measured margin (worst
   0.67% of a 5% allowance).
3. **R19** -- the four live sites (`test_beam_element.py:84, 105`;
   `test_member_local_axes.py:70-72, 83`) are declared or annotated, and the scanner
   sees at minimum the `assert_*` call families, the `tol=`, `rel_tol=`, `abs_tol=`
   and `delta=` keywords, and the black-wrapped multi-line assert. Its negative
   control carries shapes it has not already been shown.
4. **R20** -- the eleven `pytest.approx` absolute epsilons are declared entries or
   carry an annotation whose stated category survives the direction test, and
   `tests/test_no_tolerance_literals.py:29-32` and `test_reference_provenance.py:34`
   stop contradicting each other.
5. **R21** -- the three new counters are the argument of an assertion that reddens on
   them, in the tolerance's own quantity, at a measured detection threshold.
6. **R22** -- `test_the_error_measure_is_UNIT_INVARIANT` is posed so the declared
   tolerance decides it, and setting the rotational weight to 1.0 is confirmed to
   turn it red.
7. **R23** -- `floatfea/assemble/system.py:50-53` and `:153-155`, and
   `tests/verification/rung1/test_patch_test.py:392-393`, say what the ablation
   measured.
8. **R24** -- the 6x is stated with its operating point (or as the measured range
   `0.77x .. 9.9x`, `1.58x` at `S = 1`), and "both under test" is either made true or
   removed. An assertion that reddens when `solve()` stops equilibrating would close
   this and R9 together.

R4, R5, R6, R15, R16, R25, R26 and R27 may be answered in step 5's `Carried` section
rather than before step 5 opens. R6 (`pin_threads`) remains inherited from an
ungated step 3.

**Not a STOP.** No lower rung is red, the locked gates are unchanged, and the element
survived every adversarial case I could construct -- the six-state gate holds at
`3.19e-14` across nine decades of unit change through a harness I wrote myself, and
the block-confined controls separate by ten orders. The substance of G2.2 has been
met since the previous verdict. What is not met is the record and the instruments
around it, and this is the third consecutive iteration in which the commit answering
the HOLD introduces a new instance of the species it was answering: R10's stale
sentence has a twin at `test_patch_test.py:392`, R13's undeclared literal has twins
in the `pytest.approx` default and in `tol=`, and R8's unablated causal claim has a
twin in "both are under test". That pattern is itself the finding, and it is why
this is a HOLD rather than a PASS with caveats.

**Witness channel unavailable.** No git remote is configured, so there is no PR and
no `[witness ...]` comment. Per `docs/SUPERVISOR.md` that is an unavailable check,
not a pass. Three consecutive reviews of this step have now been produced by a
single reader; the standing caveat is unchanged -- every instrument here was written
by the same hand as the element, against fields they share Timoshenko kinematics
with, and until V5.1 puts CalculiX on the other side a run of passes means "not yet
contradicted."
