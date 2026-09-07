# Review — F2 step 4
Reviewed commit: 8a415e10884fe7e8a1dba5578c1dff8b709ff03d
Verdict: STOP
Tests: 741 passed, 0 failed, 0 skipped   (my run at `121a35a`, `python -m pytest -q`, 6.22s.
With my twelfth-round corpus applied at `8a415e1`: **7 failed, 760 passed**.)

**Reviewed code commit: `121a35a`.** The header stamp is `8a415e1`, my own corpus
commit, made immediately before this verdict and touching no code.

Twelfth pass. Range `fc3c9a8..121a35a`, three commits: `8834fba` (plan, re-lock),
`aa843ae` (step) and `121a35a` (report).
`git diff fc3c9a8..121a35a -- .claude docs/SUPERVISOR.md` is **empty** -- my own
instructions were not touched, and I diffed them rather than inferring it from a
green suite that does not read them.

**The eleventh verdict's two blocking items are answered, and the work is good.**
R94's withdrawals are real: `grep -n "dissolve" docs/milestones/F2.md` no longer
returns anything in sec. 5b Q6, and `0.13-0.49 eps` is withdrawn in the text that
supported it. R99's list is complete -- every item by number. R96 is fixed *and
locked*: I reverted `member_lambda` to the strong axis on my own copy and **six
entries go red** in the new band test, so the weak axis is asserted structurally
and not merely reported. R104 is fixed. The `I_y <-> I_z` refutation reproduces
**to the digit** (`8.247e-17` against a clean `2.191e-16` at
`aniso_weak_lam154_undetectable`), and recording a proposed control as refuted
rather than swapping it out quietly is the right instinct and is credited. The
defect harness carries its own ablation: I ran the reconstruction with **neither**
defect and it returns `2.56e-19 .. 2.26e-16`, i.e. round-off, so `5.8789e-05` and
`3.5991e-05` isolate the defect and are not the reconstruction's own error.

**And the verdict is STOP, on the same species the last one was, one level down.**
The plan no longer says the *ceiling* has no domain and means the whole gate; it
now says the *counter* and the *curve* have no domain, and both statements are
refuted by configurations inside the space they are asserted over. The gate makes
two claims; I measured both against shapes the corpus did not contain, and each
has an edge:

```
claim   "asserted on every entry with no exception and no domain"      F2.md:493
cmd     the shipped runner's own quantity, family D=0.6 t=0.012 axis, L swept
out     L/r_min    900     930    1058    1250    1443    1924    2885
        x counter  1.028   0.964  0.747   0.536   0.403   0.227   0.101
        wrong_dof_index crosses PATCH_TEST_EXACTNESS_COUNTER at L/r_min ~ 912

claim   "0.60 holds the measured scatter with 1.39x of margin"      tolerances:487
cmd     360 random admissible configurations, D 0.1-300 m, D/t 3-30,
        L/r_min 30-200, free direction, free roll, I_y/I_z 0.01-0.2
out     worst deviation 0.5937 against a band of 0.60 = 0.990 of it; a local
        search from there crosses at 0.6131 = 1.022x, L/r_min 92.9, L/D 8.3,
        ceiling still held at 0.053x
```

Neither is an element defect. Both are the plan describing a space from a list.

## Carried

Every item from the eleventh verdict (`STOP @ 36a3702`, committed `fc3c9a8`),
traced through `fc3c9a8..121a35a` and re-measured, plus the older carry.

- **R94 (STOP) -- ANSWERED in its letter, and the finding it named has moved
  rather than closed.** The three withdrawals are in the plan and I checked each:
  "dissolves" is gone from sec. 5b Q6 and D7 item 7, `0.13-0.49 eps` is withdrawn,
  the axis is `min(I_y, I_z)`, and the two reds are green without a skip, an
  `xfail`, a deleted line or a touched `expect` (`git diff fc3c9a8..121a35a --
  tests/corpus` is empty). **The proposed `lambda <= 300` bound was abandoned
  rather than defended, which is the right call and is credited.** What is not
  closed is the underlying item: a domain claim measured on the corpus and
  asserted over the space. It is re-opened as **R105** and **R107** against the
  new text.
- **R95 -- carried, OPEN, correctly declared.** `expect == "raise"` at
  `test_corpus_configurations.py:703` still uses a bare `pytest.raises(ValueError)`
  with no `match`, where the inadmissible branch twenty lines above uses
  `match="admission limit"`. My two new refusal entries land in this branch and
  show the second half of it too -- see **R114**.
- **R96 -- CLOSED, and it is the best-executed fix of this round.** `member_lambda`
  reads `_entry_section`, `extra=` included. I checked every site an entry is
  characterised: `grep -n "_section(entry" ` gives two, `_build` (`:393`) and
  `_inadmissible` (`:639`); the second reads only the depth through
  `_outer_diameter`, which is `I_z` and `A`, and the only section-modifying extra
  moves `I_y`. So the strong axis is gone from every reading that could show it.
  One sentence overstates it -- **R113** -- and it is cosmetic.
- **R97 -- carried, OPEN, correctly declared, and the report's reading is fair.**
  `grep -rn "never asserted at a constant" docs/milestones/F2.md` still returns
  `:579` and `:1288`. The report's point that the sentence is about the forward
  *field* error while `RESULTANT_EXACTNESS` is a different quantity is correct;
  the plan still does not say so.
- **R98 -- carried, OPEN, correctly declared.** `INADMISSIBLE` is assigned at
  `:645` and read by no assertion.
- **R99 -- CLOSED.** The `Carried` table lists every item by number with a status,
  and the omission is recorded first rather than explained away. R68's standard is
  restored.
- **R100 -- carried, OPEN, correctly routed to step 4a -- and the count went up.**
  `ls scripts/` is still `write_verdict.py` alone. The bracket table added this
  round is a fourth table with no generator: see **R111**.
- **R101 -- carried, OPEN, correctly declared.** `grep -n "revision 1"
  floatfea/tolerances.py` still returns `:189` and `:623`, both "revision 10", and
  `:623` is `RESULTANT_EXACTNESS_COUNTER`'s pointer to the withdrawn claim.
- **R102 -- carried, OPEN, correctly declared.**
- **R103 -- carried, OPEN, correctly declared, and now moot in its second half**:
  the `lambda <= 300` framing it criticised is withdrawn with R94.
- **R104 -- CLOSED.** `_field` returns `AMBIGUOUS(raise|hold)` on a duplicate and
  the per-entry assertion reddens on it. I drove `_error_row` myself on both
  orderings; both now reach the assertion as a disagreement.
- **R63 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Correctly recorded.
- **R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 -- still
  open**, correctly declared, routed to step 4a or later.
- **R77, R78, R81-R93 -- closed** at the tenth and eleventh verdicts, correctly
  recorded.
- **R68's standard -- HELD.** Six rounds of five.

## Findings

**R105. (STOP) Claim 1's "no exception and no domain" is false at `L/r_min ~ 912`,
1.4% in its own axis from the corpus entry that already binds it -- and the
mechanism sentence that licenses the claim is refuted by the claim's own two
defects.** `docs/milestones/F2.md:472-493`, `:1277-1283`;
`floatfea/tolerances.py:425-445`;
`tests/verification/rung1/test_corpus_configurations.py:786-806`.

*The domain, solved rather than sampled.* Both injected defects fall with
slenderness at the measured exponent `-1.99`, on the family
`D=0.600 t=0.01200 orient=axis` that `lam900_axis_undetectable` belongs to:

```
  L/r_min       900      1058      1250      1443      1924      2885
  wrong_dof   3.599e-05 2.614e-05 1.876e-05 1.412e-05 7.960e-06 3.543e-06
  x counter     1.028     0.747     0.536     0.403     0.227     0.101
  flip        1.412e-04 1.025e-04 7.362e-05 5.539e-05 3.123e-05 1.390e-05
  1e-6 defect 4.132e-14 2.990e-14 2.140e-14 1.608e-14 9.044e-15 4.019e-15
```

`wrong_dof_index / 1e-6 defect` is `8.71e+08` at `900` and `8.82e+08` at `2885` --
**constant to 1%.** The two claims are not two mechanisms. They are one curve at
two amplitudes, and claim 1 clears a fixed constant over a wider slenderness range
only because it starts `8.8e+08` higher. Its edge is `L/r_min ~ 912`.

*The mechanism sentence, checked.* "They are `O(1)` relative to the block they
corrupt and do not fall with slenderness" (`F2.md:475`; the same words at
`tolerances.py:432-437`). Measured, `dropped_flip` falls `178x` and
`wrong_dof_index` `475x` across the corpus's own slenderness range, at the same
exponent as the small defect the sentence contrasts them with. **A number that is
correct does not license the explanation attached to it (BG0).** The correct
statement is about amplitude, not about scaling, and it has a different
consequence: an amplitude ratio moves the edge, it does not remove it.

*A third formulation defect, and it is not O(1).* The directive asked me to
construct one. **Dropping the shear parameter** -- Timoshenko to Euler-Bernoulli,
`phi = 0`, one of the classic element formulation errors and one character in
`local_stiffness` -- measured on all 63 solved entries:

```
  L/r_min      5.9     46.5     139.5     328.8     900
  response  1.161e-02 1.390e-04 1.906e-06 4.937e-08 9.190e-10
  x counter   331.6     3.97      0.054     0.001     0.000
  below PATCH_TEST_EXACTNESS_COUNTER on 22 of 63 entries
```

It is a formulation defect, it changes the element's structure, and it is
`phi`-sized -- which falls as `1/lambda^2` itself, so the response falls as
`1/lambda^4`. **The gate still catches it**, everywhere, against the *ceiling*
(`9.190e-10` is `1.8e+05x` of `5e-15`), which is the honest form of the claim. The
class sentence is what fails.

*And the entry contradicts itself three paragraphs down.* `I_y <-> I_z` is a
formulation defect -- which inertia goes with which plane -- and its response is
**identically the clean value**, on every entry including the anisotropic ones. It
is recorded as refuted at `tolerances.py:446-452`, immediately below the sentence
saying structural defects do not behave that way. I verified the refutation and it
is correct; I also verified *why*, and the reason generalises: the interior
out-of-balance of a constant-strain field is insensitive to a **uniform** change of
section properties, because a uniform change keeps the field in the kernel. That is
the patch test's defining property, not an accident, and it is the boundary of what
this control can be claimed for.

*What the corpus does with it.* `lam930_axis_counter_edge` (`0.964x`),
`lam1058_axis_counter_red` (`0.747x`) and `flip_counter_edge_thickwall`
(`dropped_flip 0.736x`, `wrong_dof_index 15.0x`) are red at `8a415e1`. The third
is the one that matters for the shape of any fix: on a nearly solid wall
(`D/t = 2.07`) with a weak axis, **the other defect binds**, so the edge is not one
number in `L/r_min`.

**Closed when** sec. 5b Q6 and D7 item 7 say what was measured: both injected
defects fall as `(L/r_min)^-1.99`, the same exponent as the small defect; they
clear a fixed counter over a bounded range whose edge is `L/r_min ~ 912` for
`wrong_dof_index` and a different number on a different shape family; and the claim
that has no domain is the one against the **ceiling**, which is what the gate
decides on. "Do not fall with slenderness" is replaced by the amplitude statement
that is true, or by nothing.

**R106. (STOP) The locked plan ships a different constant from the code, in the
number this round is about.** `docs/milestones/F2.md:511-515` against
`floatfea/tolerances.py:503`, and
`tests/verification/rung1/test_corpus_configurations.py:877-881`.

```
cmd  grep -n "SENSITIVITY_BAND_COUNTER" docs/milestones/F2.md floatfea/tolerances.py
out  F2.md:514         PATCH_TEST_SENSITIVITY_BAND_COUNTER = 3.0 injected in both directions
     tolerances.py:503 PATCH_TEST_SENSITIVITY_BAND_COUNTER: Final[float] = 5.0

cmd  grep -n "2.5x" docs/milestones/F2.md floatfea/tolerances.py
out  F2.md:513         "it detects a 2.5x change in the gate's sensitivity and nothing finer"
     tolerances.py:499 "the derivation that said 2.5x ignored the scatter it sits on top of"
```

The plan states as settled the value and the buy-claim that `tolerances.py`, one
commit later in the same round, records as **refuted by injection**. I reproduced
the refutation exactly -- `3x` up leaves four entries inside the band at
`2.362-2.464` -- so the plan is not merely stale, it states a number the shipped
suite would fail on. The test module's docstring at `:877-881` is stale the same
way: it describes a `3.0x` injection and a `1.2x` clearance while the code injects
`PATCH_TEST_SENSITIVITY_BAND_COUNTER = 5.0`.

This is R94's shape at one-tenth the scale and it arrived in the round that fixed
R94: a figure corrected in `tolerances.py` and left standing in the plan that
decides and in the test that runs. Three files, one number, two of them wrong.

**Closed when** `F2.md:511-515` and the docstring at `:877-881` carry `5.0` and
the measured `5x`, each with the bracket that produced it.

**R107. (blocking) The band's stated `1.39x` of margin is a property of the 63
entries it was fitted on; over the admissible space the margin is `1.01x` and an
ordinary member crosses.** `floatfea/tolerances.py:485-489`;
`tests/verification/rung1/test_corpus_configurations.py:840-872`.

The acceptance window of `assert_close(ratio, 1.0, 0.60)` is
`ratio in (0.400, 2.500)`, which I solved rather than read. The corpus's clean
scatter is `0.787 .. 1.761`, so the entry-wise margin is `1.42x` up and `1.97x`
down -- the entry's `1.39x` is right about the corpus. Over 360 random admissible
configurations (`D` 0.1-300 m, `D/t` 3-30, `L/r_min` 30-200, free direction, free
roll, `I_y/I_z` 0.01-0.2) the worst deviation is **`0.5937`, `0.990` of the band**,
and a local search from there crosses:

```
  band_edge_thickwall_aniso   D 2.888  t 0.5471  L 24.11  I_y/I_z 0.0932
      L/r_min 92.9   L/D 8.3   ratio 2.5847   deviation 0.6131 = 1.022x the band
      clean out-of-balance 2.661e-16 = 0.053x the ceiling
```

**This is not a slender member and not a degenerate one.** `L/D 8.3`, a thick wall,
a free direction and a roll -- a shape a platform carries. The element is fine
there; the *curve* is not. Two more entries bracket it,
`band_edge_thickwall_free_dir` at `0.990` of the band and -- the one that removes
the "synthetic anisotropy" reply -- `band_edge_isotropic_bracing`, a plain circular
tube the shipped model builds today (`D/t 4.5`, `L/D 111`), at `2.3505`, `0.958` of
the band.

A consequence I did not predict and the suite found for me: with those three
entries present, `test_a_SENSITIVITY_CHANGE_breaks_the_band[down]` **fails** --
`5.0` no longer catches a `1/5` change, because the required downward factor is
`max_ratio / 0.400 = 2.5847 / 0.4 = 6.46`. **The band's counter is a property of
the list too.**

**Closed when** the band and its counter are stated over the sample they were
measured on, or re-measured over the admissible space and set from that -- and the
`1.39x` margin sentence says which of the two it is.

**R108. (blocking) The only per-entry claim that a small defect is detectable at
all was removed and not replaced, and the replacement is free.**
`tests/verification/rung1/test_corpus_configurations.py:786-872`.

Before this round, every corpus entry had to respond to a 1e-6 single-element
defect above a counter. That claim is gone: claim 1 injects *structural* defects,
and claim 2 asserts only that the small-defect response tracks a curve -- a curve
that passes **below the ceiling** at `L/r_min ~ 2978`, where the response is
undetectable and the ratio is still `1.0` and green. So nothing in the suite now
says any configuration can fail on a small defect.

The replacement needs no new number, and it is the pattern this round adopted at
the posed geometry (`assert err > PATCH_TEST_EXACTNESS`, `test_patch_test.py:735`):
assert the small-defect response against the **ceiling**, per entry. Measured over
all 63 entries at this commit it holds, worst first:

```
  aniso_weak_lam154_undetectable  L/r_min 1539  2.1370e-14 =  4.27x the ceiling
  lam900_axis_undetectable        L/r_min  900  4.1317e-14 =  8.26x
  lam900_skew_undetectable        L/r_min  900  4.8362e-14 =  9.67x
  lam620_counter_pin              L/r_min  620  1.0187e-13 = 20.37x
```

`4.27x` on the entry the last two rounds were fought over. The claim that was red
at `1e-13` is true at the ceiling, on every entry, with no new constant and no
domain -- and it is the claim a reader of a patch test expects to find.

**Closed when** either that assertion exists, or the plan records that the gate no
longer claims small-defect detectability per entry and says where the claim went.

**R109. (recordable) "The only number in the claim that decides a pass is the
band" is refuted by measurement: `SENSITIVITY_SCALE` decides passes and has
untested slack of `x1.5` up and `x0.8` down.** `floatfea/tolerances.py:461-470`;
`tests/verification/rung1/test_corpus_configurations.py:809-831`;
`docs/reports/F2/step-4.md` sec. 4.

**The placement is defensible and I endorse it** -- `DETECTION_THRESHOLD` sets the
precedent, `test_no_entry_carries_a_hand_written_MEASURED_value` positively
requires measured values to live outside `tolerances.py`, and the meta-tests did
reject the first attempt for a real reason. What did not come across with the
precedent is the guard that makes it safe. `DETECTION_THRESHOLD_BAND_COUNTER` is
injected by perturbing **the recorded threshold itself**
(`test_patch_test.py:1008`, `eps = DETECTION_THRESHOLD[state] * factor`), so the
recorded numbers cannot be tuned by more than the counter without going red. The
new counter perturbs the **physical response** instead, so nothing constrains the
curve. Measured by moving the constant with everything else held:

```
  SENSITIVITY_SCALE  x1.2 x1.4 x1.5  ALL GREEN     x2.0  1 entry red
  SENSITIVITY_SCALE  x0.8            ALL GREEN     x0.6  2 entries red
  SENSITIVITY_EXPONENT  +-0.05       ALL GREEN     +-0.10  1-2 entries red
```

A `x1.5` knob that no test constrains, sitting in front of the number that decides
the ratio, is "a factor introduced to make two numbers agree" (`CLAUDE.md`
sec. Tolerances) -- and the scatter is not centred on it: the geometric centre of
`0.787 .. 1.761` is `1.178`, so moving `SCALE` up by that factor would buy margin
on both sides. Nothing did that. But nothing would notice.

**Closed when** either the band's counter is also injected on the recorded curve --
the precedent's own form -- or the claim in sec. 4 is narrowed to what is true: the
band is the only number in `tolerances.py`, and the curve is a recorded value with
`x1.5 / x0.8` of unconstrained slack.

**R110. (recordable) A phantom citation in `tolerances.py`.** `:467`.

```
cmd  grep -rn "SENSITIVITY_CURVE" --include=*.py .
out  floatfea/tolerances.py:467 only -- nothing under tests/
```

The entry names the curve "as `SENSITIVITY_CURVE` in
`tests/verification/rung1/test_corpus_configurations.py`". No such symbol exists;
the file defines `SENSITIVITY_SCALE`, `SENSITIVITY_EXPONENT` and
`sensitivity_curve()`. **Closed when** the entry names a symbol that resolves.

**R111. (recordable) The bracket table is a fourth generatorless table in
`tolerances.py`, added one commit after BI3 was adopted against exactly that.**
`floatfea/tolerances.py:479-484`; `8d6ba7d`.

The shipped reporting test regenerates the ceiling, the two formulation controls
and the curve's residual range -- that part of the BI3 claim is true and I checked
it prints them. It does **not** produce the `3x / 4x / 5x` escape bracket; the
shipped test injects `5.0` only. I reproduced every cell of the bracket by hand and
it is exactly right today, which is why this is recordable rather than blocking.
BI3's point is the mechanism: the table is a report that nothing regenerates.

Second, smaller: the entry brackets where it could solve. The exact edges are
`3.175x` up (binding entry `lam900_axis_undetectable` at ratio `0.787`) and
`4.403x` down (`aniso_free_dir_weak` at `1.761`), so the smallest two-sided factor
is `4.403` and the margin `5.0` carries is `1.14x`. "Invert the decision rule and
solve" gives a number; the bracket gives an interval.

**Closed when** the bracket moves to the report (which is regenerated by rule) with
a pointer here, or `scripts/` gains the generator.

**R112. (recordable) The withdrawn framing survives in a production module, on the
function this round changed.** `floatfea/model/admissibility.py:129-137`.

```
"The value is still worth carrying, because it is the axis along which the
 counter-case's sensitivity falls -- as 1/lambda^2, which is why
 PATCH_TEST_EXACTNESS_COUNTER is recorded at the most slender configuration
 in the corpus."
```

At this commit `PATCH_TEST_EXACTNESS_COUNTER` is the formulation control, it is not
recorded at the most slender configuration (`1539`) but at `900`, and the causal
"which is why" is the sentence the plan withdrew. Three test-file docstrings were
regenerated this round and the production module was not. The docstring also
carries a three-row table with no generator (R100's family).

**Closed when** the docstring describes the constant that exists.

**R113. (recordable) "Everything characterising an entry now goes through one
`_entry_section`" is refuted by a one-line grep, and is currently harmless.**
`docs/reports/F2/step-4.md` sec. 3;
`tests/verification/rung1/test_corpus_configurations.py:639`.

`_inadmissible` still calls `_section(entry["section"])`. I measured that it does
not matter today -- `member_l_over_d` reads `_outer_diameter`, which is `I_z` and
`A`, and the only section-modifying extra moves `I_y` -- so the L/D branch is
unaffected. It matters the day an extra touches `D`, `t` or `I_z`. The finding is
the sentence, not the code: it states a fact about the repository that its own grep
contradicts (BF0).

**Closed when** the sentence says "everything that reads the weak axis", or
`_inadmissible` reads `_entry_section`.

**R114. (recordable, new subject) The synthetic anisotropy route validates nothing:
`I_y_over_I_z=0` builds a member with zero bending stiffness in one plane and
`=-1.0` builds one with negative bending stiffness, both silently.**
`tests/verification/rung1/test_corpus_configurations.py:325-343` (`_extras`) and
`:405-407` (`_build`).

`_extras` checks that the value is finite and stops. Driven directly at this
commit:

```
  I_y_over_I_z=0     _build ACCEPTS,  I_y = 0.0000e+00   I_z = 9.5842e-04
  I_y_over_I_z=-1.0  _build ACCEPTS,  I_y = -9.5842e-04  I_z = 9.5842e-04
```

A mechanism and an indefinite element, assembled without complaint. The refusal
belongs where the value is parsed; today the first symptom is a `ValueError` from
`member_lambda` inside a diagnostic, which is a crash in the reporting path rather
than a refusal of the configuration. `aniso_zero_I_y_must_refuse` and
`aniso_negative_I_y_must_refuse` are in the corpus at `expect=raise` and both are
red. This is a different subject from BN1-BN3 and it is **not** part of the STOP;
it is the next round's item.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS_COUNTER` | `1.0e-13` | `3.5e-05` | dimensionless residual, the same quantity as the ceiling | it *is* the counter; ceiling `5e-15` sits `7.0e+09x` below it | `tolerances.py:425-453`, `F2.md:472-493`, report sec. 2 |
| `PATCH_TEST_SENSITIVITY_BAND` | -- | `0.60` | relative to the larger operand, dimensionless | `PATCH_TEST_SENSITIVITY_BAND_COUNTER = 5.0`, injected two-sided | `tolerances.py:455-500` |
| `PATCH_TEST_SENSITIVITY_BAND_COUNTER` | -- | `5.0` | multiplicative factor | it is a counter | `tolerances.py:496-503` -- **and `F2.md:514` says `3.0` (R106)** |

**The move that matters is the first, and it is not a widening -- it is a
replacement of the claim, and it must be read as one.** Raising a counter weakens
the assertion attached to it, and this one rose by eight orders. It is defensible
because the assertion changed with it: the old one ("every entry detects a 1e-6
defect at `1e-13`") is a universal that is false, which is what the last two rounds
established, and deleting a false universal is right. What is not defensible is
deleting it and leaving nothing behind, because the true form of the claim holds on
every entry with `4.27x` to spare -- **R108**.

I re-derived the new value independently: `dropped_flip 5.8789e-05` at
`L/r_min 1539` and `wrong_dof_index 3.5991e-05` at `900` reproduce **to the
digit**, the clean reconstruction is round-off, and the `I_y <-> I_z` refutation
reproduces to the digit. The bracket behind `5.0` reproduces cell for cell.
Nothing here is mis-measured; the findings are about what the measurements are said
to mean.

No golden file moved -- `git diff --stat fc3c9a8..121a35a -- tests/regression` is
empty. `grep -rn "xfail\|pytest.skip" tests/` returns nothing. No `expect` on any
corpus line was touched: `git diff fc3c9a8..121a35a -- tests/corpus` is empty.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin, and **neither does another step
commit**. This is a STOP: `docs/milestones/F2.md` reopens. **The suite at `121a35a`
is green and the element is not implicated in anything here** -- every red at
`8a415e1` is mine, and every one of them is a sentence in the plan meeting a
configuration it did not sample.

1. **R106 -- the plan against the code.** `3.0` versus `5.0`, `2.5x` versus `5x`,
   in the plan and in a test docstring. One line each, needs nobody, and it is the
   cheapest of the three to close.
2. **R105 -- claim 1's edge.** The plan says what was measured: both structural
   defects fall at the small defect's own exponent; the counter is cleared over a
   bounded range whose edge is `L/r_min ~ 912` on one family and a different number
   on another; the claim with no domain is the one against the ceiling. Whether the
   corpus entries past the edge are configurations this project intends to admit is
   a separate question and a legitimate answer -- but it is an **admission**
   answer, and BN4 has just ruled that no admission limit enters G2.2, so the two
   cannot both stand as written.
3. **R107 -- claim 2's band over the space, not the list.** `1.39x` is `1.01x` off
   the corpus, and `band_edge_thickwall_aniso` is an ordinary member. The band's
   own counter fails downward once the three new entries are present.
4. **R108 -- the detectability claim, free to restore**, and the one thing in this
   round I would call a loss rather than a change.
5. **R109-R114 -- recordable**, answerable in the next report's `Carried` section.
   R114 is a new subject and not part of the STOP.

**Adversarial corpus (BE3): 8 new entries committed, all unseen by the
implementer; 2 of 8 scored as the implementer's checks would predict, 6 red.**
`tests/corpus/g22_model_configurations.txt`, now **90**, committed separately at
`8a415e1` immediately before this verdict and touching no code. Full suite with the
corpus applied: **7 failed, 760 passed** -- six from the new entries plus
`test_a_SENSITIVITY_CHANGE_breaks_the_band[down]`, which the new entries broke
without being aimed at it.

The coverage measurement, stated plainly: **three configurations break claim 1, one
breaks claim 2, two build a mechanism silently, and two are green witnesses that
pin the margin from inside.** The implementer's own count -- 63 entries, two
planted defects -- is what it is: the entries and the defects came from the same
head as the claims, and the claims are what the entries cannot test.

**Twelve consecutive rounds have found no element defect**, and the guard's reading
is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side.
This round sharpens the pattern the eleventh named. It is no longer "the sentences
around the element are wrong" -- the sentences this round are careful, and three of
them were withdrawn by their own author before I read them. It is narrower:
**every remaining error is a quantifier.** "Every entry", "no domain", "do not fall
with slenderness", "the only pass-deciding number", "1.39x of margin" -- five
claims, five measurements over a list, five statements about a space. The
measurements are right. The quantifiers are what nobody measures, because measuring
a quantifier means leaving the list.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Twelve
consecutive reviews by one reader, and the standing consequence is unchanged.

**The standing question for the next round**, sharper than the eleventh's: **for
every quantifier in this diff -- "every", "any", "no", "always" -- what is the
sample it was measured on, and what is the cheapest configuration outside that
sample?** If the answer is "the corpus", the quantifier is a claim about 90 lines
written by one reader, and the next round will find the ninety-first.
