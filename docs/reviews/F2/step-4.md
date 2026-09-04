# Review � F2 step 4
Reviewed commit: 2b91340a23e9c450804eaf7c06c0d8c300ba20d9
Verdict: HOLD
Tests: 309 passed, 0 failed, 0 skipped   (my run, `pytest -q`, 0.68s)

Fourth pass. Four of the eight gated items are genuinely closed and I reproduced
the work behind each: the widening is reverted and this time I re-ran the
"no value loosened" check myself and it holds; `rel=0.05` is declared with a
margin I reproduce to five digits; R22's ratio test now reddens on the pre-R2
mixed measure, which is the first time that control has bitten; R23's two
sentences say what the ablation measured. Equilibration leaving `solve()` is
right, and I re-ran the nine-decade sweep on the new production path myself to
confirm the gate still holds without it.

Four gated items are not answered — R20 and R21 are untouched, R24 is now
contradicted rather than corrected — and the two artifacts built to close the
others do not do what they say. Every `_MEASURED` value is a hand-written
literal that no test recomputes, and three of the nine do not describe their
entry's sites; I located one of them exactly, on the code path BD2 deleted two
commits later. The AST scanner misses 23 of 25 shapes it has not been shown,
three of which the regex it replaced caught.

## Carried

Every item from `docs/reviews/F2/step-4.md` (HOLD @ `1acb5dc`), traced through
`64cf5c5..HEAD` rather than taken from the report.

- **1. R17 (gated) — ANSWERED.** `floatfea/tolerances.py:433` is back to
  `1e-14`. I re-ran the check rather than reading the pasted table: extracted
  every literal replaced by a declared name across `ec8b237..HEAD` and paired it
  with its successor. `ROUNDOFF_IDENTITY` absorbs literals of `1e-12` (x8) and
  `1e-14` (x3); `1e-14` is at or below all of them. `MATRIX_SYMMETRY = 1e-9`
  replaced `1e-9` x4. `COND_UNIT_INVARIANCE = 1e-6` replaced `1e-6`.
  `DETECTION_THRESHOLD_BAND = 0.05` replaced `0.05`. **No value loosened — the
  claim is true this time.** The entry's own comment records the episode, which
  is the right place for it. The closure-artifact clause is not yet due;
  `docs/closure/` has F0 and F1 only.

  Separately I checked the ~22 conversions from a *bare* `pytest.approx()`
  (default `rel=1e-6`) to `rel=ROUNDOFF_IDENTITY`, since those tighten by eight
  orders. I measured the residual at all fifteen: **every one is `0.0` exactly**.
  Nothing is now passing that should not, and nothing became flaky. What the
  conversions did *not* do is make the declared name decide — see **R33**.

- **2. R18 (gated) — ANSWERED, one residual.** `rel=0.05` at
  `test_patch_test.py:323` is now `DETECTION_THRESHOLD_BAND`, declared at
  `tolerances.py:493` with `_MEASURED = 9.9523e-03` and `_COUNTER = 0.25`. I
  reproduce the measured value **exactly**: perturbing by each recorded
  threshold gives per-state deviations `0.236 / 0.307 / 0.030 / 0.995 / 0.027 /
  0.044 %`, worst `9.9523e-03`. The per-line clearance hole is closed for
  tolerance *names* — the AST checks the argument node. It is **not** closed for
  the exemption: `test_no_tolerance_literals.py:86-88` still tests
  `EXEMPT in line` on raw source, and `EXEMPT` is now the bare substring
  `not-a-tolerance:` rather than the regex's `#\s*not-a-tolerance:`. So
  `assert err < 1e-9, "not-a-tolerance: sneaky"` is cleared by the new scanner
  and was **caught** by the old one. Recorded in **R32**.

- **3. R19 (gated) — PARTIALLY answered.** The four live sites carry a declared
  name: `test_beam_element.py:84, 105` -> `MATRIX_SYMMETRY`,
  `test_member_local_axes.py:70-72, 83` -> `ROUNDOFF_IDENTITY`. But at three of
  those four the declared name is in the slot that does not decide (**R33**),
  and the closed-when clause "its negative control carries shapes it has not
  already been shown" was not met: `PLANTED` at
  `test_no_tolerance_literals.py:136-152` is verbatim the fifteen shapes the
  previous verdict planted. I planted twenty-five it has not seen; twenty-three
  are missed (**R32**).

- **4. R20 (gated) — NOT answered.** All eleven `pytest.approx(..., abs=)`
  lines labelled "reference pin, not a ceiling" are unchanged, verbatim, at the
  same paths: `test_cantilever_closed_form.py:156, 164`;
  `test_basis_constants.py:27, 32, 33, 63, 98, 116`; `test_live_dof.py:80, 81`;
  `test_reference_provenance.py:34`. Nor were the three "wrong reason" labels
  repaired (`test_basis_constants.py:99`, `test_cantilever_closed_form.py:165`,
  `test_live_dof.py:80`). The one thing that did change is that the scanner's
  docstring no longer contains the sentence that contradicted the annotation on
  the same line — the contradiction was resolved by deleting the correct half.
  Carried as **R31**.

- **5. R21 (gated) — NOT answered.** `MATRIX_SYMMETRY_COUNTER`,
  `ROUNDOFF_IDENTITY_COUNTER` and `COND_UNIT_INVARIANCE_COUNTER` still appear
  nowhere outside `floatfea/tolerances.py` and
  `test_tolerance_counter_cases.py`'s three-literal comparison. A fourth,
  `DETECTION_THRESHOLD_BAND_COUNTER = 0.25`, was added in this step with the
  same defect. Carried as **R30**.

- **6. R22 (gated) — ANSWERED, verified by mutation.** This is the strongest
  thing in the diff. I substituted six weightings into `relative_error` and ran
  the shipped assertion at `test_patch_test.py:496`:

  ```
  w[3:] = char_length (shipped)   ratio 1.000000000                  PASS
  w[3:] = 1.0  (THE PRE-R2 MIXED MEASURE)  m=4.293e-13 mm=4.293e-16   RED
  w[3:] = char_length**2                                              RED
  w[3:] = sqrt(char_length)                                           RED
  w[3:] = 0.0 * char_length       m=mm=0   degenerate guard fires
  w[3:] = 1e-30 * char_length     ratio 1.000000000                  PASS
  ```

  The comparison is genuinely `O(1)`: `scale = max(|ratio|, 1.0) = 1.0`, so
  `1e-14` is what decides and pytest's `abs=1e-12` is out of the picture. The
  1000x drift that passed last time is red. The surviving `1e-30 * L` pass is
  correct — that weighting *is* unit-invariant, and blindness is caught by the
  six-state gate, which I confirmed reddens on `w[3:] = 0`.

  One note, not a finding: at the only production call site the operands are
  `ratio` and `1.0`, so `assert_close`'s floor check (`scale < 100 * floor`) can
  never fire. BD0's guard is structurally inert there; what closed R22 is the
  `O(1)` reframing, not the floor. The docstring at `:487-488` credits the floor.

- **7. R23 (gated) — ANSWERED.** `floatfea/assemble/system.py:40-73` no longer
  claims a relative tolerance is not unit-invariant without equilibration; it
  carries the per-scale table and states the change is reverted. `:167-171` is
  gone with the equilibrated solve. `test_patch_test.py:392-399` replaces "both
  had to be fixed" with the ablation result. Three of the four sentences are
  now right; the fourth is refuted (**R34**).

- **8. R24 (gated) — NOT answered, and now contradicted.**
  `floatfea/tolerances.py:346-349` still reads "**EQUILIBRATION IS RETAINED** ON
  A DIFFERENT JUSTIFICATION ... **Both are under test.** It would be removed if
  either stopped holding." Equilibration was removed from `solve()` at
  `d6f1ad3`. The paragraph describes the production path as it was two commits
  ago, "both under test" was already shown false, and the promise to remove it
  has been overtaken by its removal. Carried and widened into **R29**.

- **R4, R5, R6, R15, R16, R25, R26, R27 — still open**, as the previous verdict
  permits. `docs/milestones/F2.md:775` still names `PATCH_TEST_STRAIN`;
  `test_patch_test.py:235` still asserts `res.residual <= PATCH_TEST_EXACTNESS`;
  `pin_threads` still has one caller; `test_the_four_constant_strain_states_are_EXACT`
  still says four and runs six; `assemble/system.py` unchanged for R16;
  `docs/milestones/F2.md:470` still says "DRAFT, awaiting review";
  `docs/instrumentation.md:672, 727` unchanged. The report's `Carried` table
  lists only R4, R5, R6 and omits R15, R16, R25, R26 and R27 — the previous
  verdict named eight. See **R37**.

## Findings

**R28. (blocking) Three of the nine `_MEASURED` values do not describe their
entry's sites, and the guard written to make them meaningful cannot detect it.**

`floatfea/tolerances.py` — each accuracy entry now carries `X_MEASURED` under
the comment "WORST MEASURED at this entry's sites, from the shipped tests (BD1).
Asserted MEASURED < TOL < COUNTER, **so an entry whose sites drift toward its
ceiling fails** rather than quietly consuming its headroom."

The mechanism does not exist. `test_measured_below_ceiling_below_counter`
(`test_tolerance_counter_cases.py:123-145`) reads all three values with
`getattr(tolerances, ...)` and compares them to each other. Nothing in the repo
recomputes `X_MEASURED`: `grep -rn "_MEASURED" tests/ floatfea/` outside
`tolerances.py` returns only that one test and unrelated names in
`test_live_dof.py`. A site can drift by nine orders and the test stays green.
This is an unablated causal claim, repeated on nine entries.

I recomputed all nine against the shipped assertion sites. Five reproduce or are
plausible (`COND_UNIT_INVARIANCE` 1.7278e-14 vs 1.7319e-14;
`DETECTION_THRESHOLD_BAND` 9.9523e-03 exactly; `ROUNDOFF_IDENTITY` and
`TRANSFORM_SPECTRUM_INVARIANCE` at ULP; `PANEL_RECONSTRUCTION_RESIDUAL` not
re-derived). Four do not:

```
entry                     declared     my measurement at its sites   where
PATCH_TEST_EXACTNESS      8.2144e-15   1.3881e-14   blind bending_xz/shear (:383)
MATRIX_SYMMETRY           3.7107e-17   0.0 exactly  test_beam_element.py:83, 103
TRANSFORM_INVARIANCE      3.8357e-15   1.5623e-12   test_assembly_and_solve.py:155
SUBDIVISION_INVARIANCE    6.0130e-13   8.4821e-14   test_assembly_and_solve.py:158
```

Each has a locatable cause, and two of them are the same cause:

- `PATCH_TEST_EXACTNESS_MEASURED = 8.2144e-15` is `gate axis_aligned/shear_xz`
  measured **with equilibration in `solve()`** — I restored the pre-`d6f1ad3`
  solve and got `8.2144e-15` to five digits. `SUBDIVISION_INVARIANCE_MEASURED =
  6.0130e-13` likewise: on the equilibrated path I get `6.0130e-13` exactly, on
  the shipped path `8.4821e-14`. Both were recorded at `49a3acc` and not
  regenerated when `d6f1ad3` removed equilibration two commits later. This is
  precisely what `CLAUDE.md:105-109` — added at R14, by this implementer —
  requires: every figure regenerated by running the shipped tests at the
  report's own commit.
- Even at its own commit, `8.2144e-15` was not the worst at the entry's sites:
  `blind bending_xy/axial` was `1.4066e-14`. The `err <= PATCH_TEST_EXACTNESS`
  assertions inside `test_the_OTHER_plane_is_blind_to_it` (`:383`) were not in
  the sample.
- `MATRIX_SYMMETRY_MEASURED = 3.7107e-17` is **another entry's site**. I get
  `max|K - K^T| / max|K| = 3.7107e-17` for the assembled frame at
  `test_assembly_and_solve.py:82` — which is a `TRANSFORM_INVARIANCE` site. Both
  actual `MATRIX_SYMMETRY` sites measure `0.0` exactly, and the two rank sites
  give `3.49e-17` and `1.36e-16`.
- `TRANSFORM_INVARIANCE_MEASURED = 3.8357e-15` is 400x below the worst at its
  sites on *either* path: `r.residual = 1.5623e-12` at `n_el=11`
  (`test_assembly_and_solve.py:155`), `2.565e-12` equilibrated. The entry's true
  headroom against `1e-11` is 6.4x, not 2600x.

The direction matters. Three of the four understate, and the whole point of the
number is to tell a later reader how much headroom is left before the ceiling is
consumed. `TRANSFORM_INVARIANCE` is at 16% of its ceiling and reads as 0.04%.

**Closed when** each `X_MEASURED` is produced by the shipped tests rather than
written down — the cheapest form is a fixture that records the worst value each
assertion actually saw and a session-end check against the declared number, so
that a drift or a solve-path change reddens — and the four values above are
regenerated at HEAD, over *all* of the entry's assertion sites. Until the value
is computed, `MEASURED` is prose with a float type, and the comment must not say
that drift fails.

**R29. (blocking) The justification for the load-bearing rung-1 tolerance still
describes the solve path this step deleted.**
`floatfea/tolerances.py:329-353`, three consecutive paragraphs:

- `:329-331` — "VERIFIED invariant across length-unit factors S = 1e-4 .. 1e+4:
  **worst error 3.19e-14**, no breach at any scale." I re-ran the sweep on the
  shipped path through my own harness (E proportional to S^-2, dimensions to S,
  translations of the exact field to S), six states, nine decades. **Worst is
  `2.0036e-13`** at `S = 1e-4`; the `3.19e-14` figure is the equilibrated one,
  which my harness also reproduces to three digits (`3.1967e-14`, `S = 1e4`) —
  so the harness is calibrated against their own published row. The good news is
  that there are still **zero breaches**: BD2 is safe and the gate holds without
  equilibration. The bad news is the recorded headroom is 5x, not 31x, and the
  number in the file is 6.3x optimistic about the code that ships.
- `:346-349` — "EQUILIBRATION IS RETAINED ... Both are under test. It would be
  removed if either stopped holding." It was removed, in this step. R24, verbatim.
- `:351-353` — "Floor, as a multiple of the equilibrated conditioning:
  cond(K~) * eps = 3.85e2 * 2.22e-16 = 8.5e-14. The worst measured error is
  **0.37x** that floor and this ceiling is ~12x it." There is no equilibrated
  conditioning on the solve path; `cond(K_ff)` runs `9.2e2 .. 6.0e8` over these
  scales. Against the same stated floor the measured worst is now `2.36x`, not
  `0.37x` — the recorded ratio is on the wrong side of the floor it cites.

The same staleness reaches the tests. `test_patch_test.py:423` — "the algebraic
fact **the equilibrated solve rests on**"; `:440`, the failure message — "the
solve is not unit-robust and every exactness ceiling above it is unit-dependent";
`:446` — "if it did not, equilibration would be ceremony". All three describe a
solve that equilibrates.

**Closed when** `:329-331` states the measured worst on the shipped path with
its scale (`2.00e-13` at `S = 1e-4`, no breach), `:346-353` is rewritten for a
solve that does not equilibrate — including the floor paragraph, which now has
to be built on `cond(K_ff)` or dropped — and the three test strings stop
asserting a property of the production solve that the two conditioning tests do
not test.

**R30. (blocking) R21 is unanswered and the step added a fourth dead counter.**
`MATRIX_SYMMETRY_COUNTER`, `ROUNDOFF_IDENTITY_COUNTER`,
`COND_UNIT_INVARIANCE_COUNTER` and now `DETECTION_THRESHOLD_BAND_COUNTER` appear
in no assertion. Checked mechanically: zero occurrences under `tests/` outside
`test_tolerance_counter_cases.py`. The five older counters
(`PATCH_TEST_EXACTNESS`, `SUBDIVISION_INVARIANCE`, `TRANSFORM_INVARIANCE`,
`TRANSFORM_SPECTRUM_INVARIANCE`, `PANEL_RECONSTRUCTION_RESIDUAL`) are all
consumed by a test. `DETECTION_THRESHOLD_BAND_COUNTER = 0.25` is justified as
"if a formulation change moved any state's sensitivity by 25% ... this must catch
it" — an executable claim that nothing executes, and a round number rather than a
measured detection threshold. The gated wording was: the argument of an assertion
that reddens on it, in the tolerance's own quantity, at a measured threshold.
**Closed when** that holds for all four.

**R31. (blocking) R20 is unanswered; the eleven annotations stand verbatim.**
Direction test, unchanged from the previous verdict: widening `abs=5e-4` on
`sec.kappa("thin_tube", 0.3) == pytest.approx(0.5305, abs=5e-4)`
(`test_basis_constants.py:32`) hides a wrong shear coefficient. That is a
ceiling, whatever the comment calls it. Eleven such lines, three more with a
category that does not survive inspection. **Closed when** the eleven epsilons
are declared entries — a single quantisation entry with a stated rule would cover
most, but then the rule has to hold: `abs=5e-6` on `0.006043`, `abs=0.1` on
`59.6`, `abs=1e-4` on `1.1111` are 5, 2 and 1 units in the last place, not half —
or the "reference pin" category is retired.

**R32. (blocking) The AST scanner misses 23 of 25 shapes it has not been shown,
three of which the regex it replaced caught.**
`tests/test_no_tolerance_literals.py`. Its docstring says the regex's three holes
are closed "by construction". I planted twenty-five shapes outside its own corpus
and ran the shipped `offending()`:

```
MISSED  assert_close(a, b, 1e-9, floor=1e-16)          SAFE_CALLS skips the whole call
MISSED  assert_differs(a, b, by=0.5, floor=1e-16)      same
MISSED  assert math.isclose(a, b, rel_tol=1e-9)        rel_tol/abs_tol not in TOL_KEYWORDS
MISSED  assert math.isclose(a, b, abs_tol=1e-9)
MISSED  self.assertAlmostEqual(a, b, delta=1e-9)       delta/places not in TOL_KEYWORDS
MISSED  assert np.allclose(a, b)                       bare-default rule is `approx`-only
MISSED  assert np.isclose(a, b)
MISSED  np.testing.assert_allclose(a, b)
MISSED  np.testing.assert_allclose(a, b, 1e-7)         positional rtol
MISSED  TOL = 1e-9 ... assert err < TOL                comparator is a Name
MISSED  eps = 1e-9; assert a == approx(b, rel=eps)     kw value carries no Constant
MISSED  assert err < 5e-3 * scale                      <- OLD REGEX CAUGHT THIS
MISSED  assert err <= 1e-13 * abs(k).max()             <- OLD REGEX CAUGHT THIS
MISSED  assert err < 1e-9, "not-a-tolerance: sneaky"   <- OLD REGEX CAUGHT THIS
MISSED  assert spread > 10000                          integer form, documented choice
MISSED  self.assertLess(abs(a-b), 1e-9)
MISSED  assert err < 10**-9
CAUGHT  assert (\n err\n < 1e-9\n)                     genuine improvement over the regex
CAUGHT  assert err < 0.000000001
```

`APPROX_NAMES` at `:42-45` is defined and never referenced — the six call names
it lists (`assert_allclose`, `allclose`, `isclose`,
`assert_array_almost_equal`, ...) are only ever reached through their keywords.

Three of these are live and were not caught by either scanner:

- `tests/unit/test_beam_element.py:76` —
  `assert np.linalg.eigvalsh(stiff - soft).min() >= -1e-6 * abs(stiff[0, 0])`.
  A negative-eigenvalue floor deciding a physical-direction test, seven lines
  above a site this step declared.
- `tests/verification/rung3/test_basis_constants.py:85` —
  `assert actual <= bound + 1e-15`.
- `tests/unit/test_member_local_axes.py:60, 61, 62, 79` —
  `np.isclose(np.linalg.norm(x), 1.0)`, numpy defaults `rtol=1e-5, atol=1e-8`,
  in the file this commit edited, ten lines above the sites it declared.

And the `SAFE_CALLS` blanket is the regex's line-clearance re-created at call
granularity: `tests/unit/test_testing_helpers.py` — introduced in this step —
carries sixteen bare literals (`tol=1e-12` x6, `floor=1e-16` x6, `floor=1e-12`
x2, `by=0.5` x3) that the scanner cannot see, and `test_patch_test.py:535`
carries `by=0.5` on a live negative control. The new preferred helper is the one
call form exempt from the check.

**Closed when** the check descends into `assert_close`/`assert_differs`
arguments rather than skipping the call; `TOL_KEYWORDS` covers
`rel_tol`/`abs_tol`/`delta`, positional tolerance arguments, and library defaults
for the whole `APPROX_NAMES` set it already declares; a comparator that is a
`BinOp` containing a float is flagged (the regression); the exemption is a
comment token, not a substring anywhere on the line; the three live sites above
are declared or annotated; and `PLANTED` carries shapes drawn from somewhere
other than the previous verdict's list. `docs/instrumentation.md:657-658` states
this principle about the mesh check: a control drawn from the defects already met
is a test of those defects.

**R33. (blocking) At about seventeen sites the declared name is in the slot that
does not decide, and the scanner's own stated reason says so.**

`tests/test_no_tolerance_literals.py:25-26` flags a bare `pytest.approx(x)`
because "it defaults to `rel=1e-6, abs=1e-12`". `pytest.approx(x, rel=NAME)`
keeps `abs=1e-12` and is not flagged. `approx` applies
`max(rel*|expected|, abs)`, so wherever `|expected| < abs/rel = 100`, the
undeclared absolute is what decides. Measured at
`tests/unit/test_beam_element.py:185`:

```
flex[2,4] = -1.397e-07, flex[4,2] = -1.397e-07, true residual 1.894e-16
rel * |expected| = 1.397e-21   vs   pytest default abs = 1e-12
injected relative defect 1e-14 .. 7e-6  ->  assertion PASSES
injected relative defect 1e-5           ->  assertion fails
```

The declared ceiling is `1e-14`; the ceiling in force is `7.2e-6`, a factor of
7e8. That is the Maxwell-Betti reciprocity check — the one assertion a
transcription error in the flexibility cannot survive. At least thirteen of the
~30 `ROUNDOFF_IDENTITY` sites are in this regime (`kappa` 0.53, `tube_area`
0.0222 / 1.31 / 0.0417, `J` 1.9e-3, `torsion_constant` 7.0 x2,
`chs_class_limits` 59.6, `radius_of_gyration` 0.313, `basis:68` 0.006, `flex`
1.4e-7, `transform:238`).

The same shape with numpy. `np.testing.assert_allclose` defaults to `rtol=1e-7`,
so at `test_member_local_axes.py:70, 71, 72, 83` — three of R19's four live
sites, declared in this step — the declared `atol=1e-14` is inert:

```
np.testing.assert_allclose([0,0,1+d], [0,0,1], atol=ROUNDOFF_IDENTITY)
  d = 1e-14 .. 1e-7  ->  PASSES        d = 5e-7  ->  fails
```

A local-axis unit vector wrong in the seventh digit passes a check declared at
the fourteenth. (`:80-82` use `np.isclose(x, 0.0, atol=...)`, where the desired
value is zero and the declared `atol` correctly decides — those are sound.)

This is not a pre-existing defect the step merely failed to fix. The step's own
BD0 module docstring names it: "`pytest.approx(mm, rel=1e-12)` carries an
**undeclared default** `abs=1e-12`". `assert_close` was written to remove it, and
was then applied at exactly one site while ~30 comparisons were given a declared
`rel` and left with an undeclared `abs`.

**Closed when** each site either passes `abs=` explicitly from a declared entry,
or uses `assert_close`, or is shown by measurement to be in the regime where the
declared value decides. The check is one line: assert `rel*|expected|` exceeds
the default `abs` at the site, or invert it — solve for the smallest defect the
assertion detects and compare it to the declared number. The guard is "invert the
decision rule and solve"; here the two differ by eight orders.

**R34. (blocking) A causal claim on the production path, refuted by its own
ablation, in the commit written to answer that guard.**
`floatfea/assemble/system.py:57-58` — "the error measure alone is necessary and
sufficient, and **equilibration alone leaves the kilometre breach exactly where
it was**."

I ran the four-cell ablation. My harness reproduces all four shipped worsts
(`3.1967e-14 / 2.0036e-13 / 2.0859e-11 / 2.0720e-10` against the file's
`3.19e-14 / 2.00e-13 / 2.09e-11 / 2.07e-10`), so it is calibrated against their
numbers. Per scale, under the mixed measure:

```
S            1e-4     1e-3     1e-2     1e-1      1       10      100     1e3      1e4
equil NO   2.07e-10 1.66e-11 5.12e-13 7.24e-14 4.19e-15 4.55e-14 1.52e-13 2.30e-11 1.07e-10
equil YES  2.09e-11 2.84e-12 2.26e-13 2.20e-14 1.91e-15 1.11e-14 3.85e-14 5.75e-13 7.80e-12
```

At `S = 1e3` — kilometres, the scale the sentence names — the breach of `1e-12`
is present without equilibration (`2.30e-11`) and **absent with it**
(`5.75e-13`). Equilibration alone removes the kilometre breach; it leaves the
ones at `1e-4`, `1e-3` and `1e4`. The sentence is backwards on the single scale
it cites.

The *decision* is not affected — rows 1 and 2 both have zero breaches, so the
error measure alone is sufficient and BD2 stands. What is affected is that the
one sentence in the diff carrying "alone" and "exactly" is the one the ablation
contradicts. **Closed when** the sentence states what the cells measured: the
error measure alone is necessary and sufficient; equilibration alone reduces
every scale's error by roughly 3-9x but still breaches at `1e-4`, `1e-3` and
`1e4` under the mixed measure.

While there: `tolerances.py:339` records the row-3 first breach as `S = 1e-3`; I
measure `S = 1e-4` (`2.09e-11`), which is also the row's own worst. Same
correction, one line up.

**R35. (recordable) A citation that does not resolve, in a production module.**
`floatfea/assemble/system.py:8-10` — "`equilibrate` is a tested utility and is
**not** on the solve path -- see its docstring, and **BD2 in
`docs/milestones/F2.md`**." `grep -n "BD0\|BD1\|BD2\|BD3\|BD4\|BD5"
docs/milestones/F2.md` returns nothing. The BD items exist only in
`docs/reports/F2/step-4.md`. The guard is "every citation resolves"; this is the
first phantom I have found pointing out of `floatfea/`.

**R36. (recordable) The scanner's domain cannot contain a production violation,
and there are four.**
`test_no_tolerance_literals.py:40` sets `TESTS = Path(__file__).parent` and
`:129` globs `TESTS.rglob("test_*.py")`. `floatfea/` is never scanned, while
`CLAUDE.md` section Tolerances binds it — "no local literals, no default
arguments carrying a tolerance" — and binds it hardest, because three of these
decide whether a record is rejected:

```
floatfea/io/reader.py:157   np.isclose(abs(gravity[2]), GRAVITY_MAGNITUDE, rtol=0.0, atol=1e-9)
floatfea/io/reader.py:208   np.allclose(dt, dt[0], rtol=1e-9, atol=0.0)
floatfea/io/reader.py:225   np.allclose(inertia, inertia.T, rtol=1e-10, atol=0.0)
floatfea/io/frames.py:358   np.isclose(g, omega, rtol=0.0, atol=1e-12)
```

"Assertion domain blindness": the collection the assertion inspects cannot
contain the failure. The report's "repo sweep 0 remaining" is true of `tests/`
and reads as true of the repo.

**R37. (recordable) Stale and divergent figures.**
- `docs/instrumentation.md:727` — "perturbing by the threshold lands the error on
  the declared ceiling to within **0.3%**". Measured: worst `0.995%`. This step
  declared the correct figure as `DETECTION_THRESHOLD_BAND_MEASURED =
  9.9523e-03` in `tolerances.py`, so the repo now carries two different numbers
  for the same measurement. R26 was recordable; it is now a contradiction
  introduced by this step's own correct half.
- `docs/instrumentation.md:672` — "so only commensurability varies", the sentence
  R11 refuted. Unchanged.
- The report's `Carried` table lists three of the eight items the previous
  verdict permitted to be carried; R15, R16, R25, R26 and R27 are absent rather
  than marked open.
- `docs/milestones/F2.md:470` still says "DRAFT, awaiting review" after four
  executed steps (R27).

---

**What I verified positively.**

- 309 tests pass in my run. No `xfail`, no skips, no empty parametrisation: the
  ACCURACY set parses to nine entries and the `["<none>"]` sentinel is asserted,
  so `test_tolerance_counter_cases.py`'s 32 nodes are all real.
- The "no value loosened" claim is **true this time**, checked by my own
  extraction of every replaced literal rather than from the pasted table.
- BD2 is right on the merits. Nine-decade sweep on the shipped path: worst
  `2.0036e-13`, **zero breaches** of `1e-12`. The six-state gate at `S = 1`
  worsens from `7.94e-15` to `1.25e-14`, which is nothing. Nothing in the repo
  consumed the equilibrated solve; the two conditioning tests call `equilibrate`
  directly and are unaffected.
- BD3 closes R22. The mutation table above is the ablation R22 asked for, and
  `w[3:] = 1.0` is red.
- `DETECTION_THRESHOLD_BAND` is a real accuracy tolerance, correctly declared,
  with a measured value I reproduce to five digits and 5x of margin.
- All fifteen bare-`approx` conversions measure `0.0` residual — the tightening
  from `rel=1e-6` to `rel=1e-14` changed no verdict and introduced no flake.
- `COND_UNIT_INVARIANCE_MEASURED` reproduces (`1.7278e-14` against `1.7319e-14`);
  `cond(K~) = 3.849144e+02` at all four scales, identical to seven digits.
- Commit hygiene is clean: no commit touches `docs/reviews/`; no tolerance value
  moves in the same commit as code it would rescue; `407e5ad` (the helper)
  precedes its uses.
- The AST walk is a genuine improvement on two shapes the regex could not reach —
  the black-wrapped multi-line assert, and a threshold inside an `if ... raise`
  rather than an `assert`.
- Adversarial cases that produced **no** finding: the axis-aligned orientation;
  the all-zero field; `w[3:] = 1e-30 * L` (passes, and correctly — that weighting
  is unit-invariant, and the six-state gate catches the blindness); the
  degenerate zero-over-zero branch, which asserts rather than returning silently.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `ROUNDOFF_IDENTITY` | `1e-12` | `1e-14` | relative, dimensionless | `1.0e-8`, **unused** (**R30**) | `floatfea/tolerances.py:416-443`. **Tightening**, back to the tightest literal it absorbs. Re-verified against all eleven replaced literals: `1e-12` x8, `1e-14` x3 — at or below every one. R17 closed. `_MEASURED = 2.2204e-16` is machine epsilon written as a measurement; my worst at its reachable sites is `1.894e-16`. The comment still says "its **nine** sites"; `3f9ff25` took it to about 30 and the figure was not re-measured. At 13 or more of those sites the value is inert (**R33**). |
| `DETECTION_THRESHOLD_BAND` | — (bare `rel=0.05`) | `0.05` | relative, dimensionless | `0.25`, **unused** (**R30**) | `floatfea/tolerances.py:473-499`. Same value as the literal — not a widening. `_MEASURED = 9.9523e-03` reproduces exactly; margin 5x. R18's declaration clause closed. The counter is a round number, not a measured detection threshold. |
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` (unchanged) | relative, dimensionless | `1.0e-7`, asserted | `floatfea/tolerances.py:312-388`. Value unmoved. Its justification block now describes a deleted code path (**R29**); `_MEASURED = 8.2144e-15` is a pre-BD2 figure and was not the worst even then (**R28**). |
| `MATRIX_SYMMETRY` | `1e-9` | `1e-9` (unchanged) | relative to largest entry | `1.0e-2`, **unused** | `_MEASURED = 3.7107e-17` is another entry's site (**R28**). |
| the other five accuracy entries | — | unchanged | — | unchanged | `_MEASURED` added to each. `TRANSFORM_INVARIANCE` and `SUBDIVISION_INVARIANCE` are wrong (**R28**). |

New undeclared thresholds introduced by this step:
`tests/unit/test_testing_helpers.py` sixteen literals inside `assert_close` and
`assert_differs` calls, and `test_patch_test.py:535` `by=0.5` — all invisible to
the scanner by the `SAFE_CALLS` exemption (**R32**).

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin until:

1. **R28** — `X_MEASURED` is produced by running the shipped tests rather than
   written down, so that a site drifting toward its ceiling reddens; and
   `PATCH_TEST_EXACTNESS_MEASURED`, `MATRIX_SYMMETRY_MEASURED`,
   `TRANSFORM_INVARIANCE_MEASURED` and `SUBDIVISION_INVARIANCE_MEASURED` are
   regenerated at HEAD over every one of their entry's assertion sites. Until the
   value is computed, the nine comments must stop claiming that drift fails.
2. **R29** — `tolerances.py:329-353` describes the solve that ships: the sweep
   figure is `2.00e-13` at `S = 1e-4` with no breach, "equilibration is retained
   ... both are under test" is gone, and the floor paragraph is rebuilt on
   `cond(K_ff)` or dropped. `test_patch_test.py:423, 440, 446` likewise.
3. **R30** — the four dead counters are each the argument of an assertion that
   reddens on them, in the tolerance's own quantity, at a measured threshold.
   Third consecutive verdict for the first three.
4. **R31** — the eleven `pytest.approx(..., abs=)` epsilons are declared entries,
   or the "reference pin" category is retired. Third consecutive verdict.
5. **R32** — the scanner descends into `assert_close` and `assert_differs`,
   covers `rel_tol`, `abs_tol`, `delta` and positional tolerance arguments and
   the library defaults for the `APPROX_NAMES` set it already declares, flags a
   `BinOp` comparator containing a float (the three regressions from the regex),
   and keys the exemption on a comment token; the three live sites
   (`test_beam_element.py:76`, `test_basis_constants.py:85`,
   `test_member_local_axes.py:60-62, 79`) are declared or annotated; and
   `PLANTED` carries shapes not taken from a previous verdict.
6. **R33** — at every site where a declared name shares a call with an undeclared
   library default, either the default is declared too or the site is shown by
   measurement to be in the regime where the declared value decides. The two
   demonstrated sites (`test_beam_element.py:185`,
   `test_member_local_axes.py:70-72, 83`) are the minimum.
7. **R34** — the kilometre sentence in `floatfea/assemble/system.py:57-58` says
   what the cells measured, and `tolerances.py:339`'s first-breach column reads
   `S = 1e-4`.

R35, R36 and R37 — together with R4, R5, R6, R15, R16, R25, R26 and R27 — may be
answered in step 5's `Carried` section rather than before step 5 opens, and that
section must list all of them, open or answered.

**Not a STOP.** No rung is red. The element itself survived every adversarial
case I could build: the patch test holds at `2.00e-13` across nine decades of
unit change on the shipped, unequilibrated path, through a harness I wrote and
then calibrated against the implementer's own published ablation row; the
six-state gate is exact at both orientations; the block-confined controls
separate by ten orders; and removing equilibration cost the `S = 1` error a
factor of 1.6. The physics and the formulation are in good shape and have been
since `e1ea251`.

What is not in good shape is the instrumentation, and the pattern from the last
three verdicts repeats a fourth time in a sharper form. Each of the six commits
answers its finding and creates a new instance of the species it answers: BD1
introduces nine "worst measured" values, four of which are not measurements of
what they name, guarded by a test that compares three literals to each other;
BD2 corrects an unablated causal claim and writes a new one that its own ablation
refutes on the scale it names; BD4 replaces a scanner that missed thirteen shapes
with one that misses twenty-three, three of them regressions, and exempts
wholesale the helper family BD0 had just created. The report is accurate about
what it covers, as every report in this step has been. What it does not cover is
whether the new instrument can fail.

Two of those — the `_MEASURED` literal and the `SAFE_CALLS` exemption — are the
same mistake in different clothes: a check whose subject is a value the check
itself supplies. Before step 5 I would want the standing question asked of each
new artifact in the commit that introduces it: if the thing this claims were
false, would this go red? For `test_measured_below_ceiling_below_counter` the
answer is no, and one perturbation finds that out.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Four
consecutive reviews of this step have now been produced by a single reader, and
every instrument in it was written by the same hand as the element, against
fields they share Timoshenko kinematics with. Until V5.1 puts CalculiX on the
other side, 309 green means "not yet contradicted".
