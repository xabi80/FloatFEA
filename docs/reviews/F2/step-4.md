# Review — F2 step 4
Reviewed commit: f435fed5b2d34273b5e047eded8575b7ada9cd5c
Verdict: STOP
Tests: 898 passed, 2 failed, 0 skipped   (my run at `7daffed`, `python -m pytest -q`,
79.88s. With my fifteenth-round corpus applied at `f435fed`: **5 failed, 935 passed**.)

**Reviewed code commit: `3830838`; report `7daffed`.** The header stamp is
`f435fed`, my own corpus commit, made immediately before this verdict and
touching no code.

Fifteenth pass. Range `baee1db..7daffed`, two commits. `git diff
baee1db..7daffed -- .claude docs/SUPERVISOR.md` is **empty** and `git log
--oneline baee1db..7daffed -- CLAUDE.md` returns nothing: my own instructions
were not touched, which I diffed rather than inferred from a suite that does not
read them. No commit touches both `floatfea/` and `docs/reviews/`.

**This is a STOP, and it is not a STOP about the element.** Fifteen rounds have
found no element defect and this round finds none either. It is a STOP for two
reasons that CLAUDE.md names by hand:

1. **A low rung is red.** `tests/verification/rung1` fails two cases at `7daffed`
   and five with my corpus. Everything above rung 1 is uninterpretable while it
   is red, and the resolution is a decision about *what G2.2 asserts*, which is
   plan territory.
2. **The locked plan was adapted silently while being implemented.**
   `docs/milestones/F2.md` is untouched in this range and now states a tolerance
   value the code does not carry (`PATCH_TEST_COUNTER_HEADROOM = 2.0e7` at
   `:558`; shipped `6.0e7`), together with four measured statements the shipped
   runner refutes. R124's closing condition named that plan site explicitly.
   "If execution reveals that the locked plan was wrong, stop and say so -- do
   not silently adapt the plan while implementing it."

**The refutation itself is correct and I reproduce it exactly**, which is the
first thing I checked and the thing I most wanted to break. `Phi` is an element
property falling as `1/L^2`; the gate's shortest element is `L/12.241` of the
member on every entry in the family; `Phi_max = 2.3807e-05` against the
member-level `59/lam^2 = 1.5943e-07`, which is the report's `149x` to three
digits. `injected_delta = 1.5 x Phi_max = 3.571067e-05` to seven digits -- the
`(2 - Phi)/(1 + Phi)` entry, which is the arithmetic I could not previously see.
`3.571e-05`, `2.480e-05`, `0.8806x` and `0.4247x` all reproduce. **My directive's
premise was wrong by 149x and the implementer was right to commit red rather
than narrow.** Section 5 stands.

## Carried

Every item from the fourteenth verdict (`HOLD @ f8df590`, committed `baee1db`),
traced through `baee1db..7daffed` and re-measured, plus the older carry.

- **R122 (blocking) -- CLOSED at all four named sites, site by site.** `:808`
  now enumerates three injected defects; `:819-822`'s uncorrected copy is gone;
  `:825-827`'s exclusion sentence survives only as an explicitly withdrawn
  quotation at `:803` and `:870`; `:904-909`'s four refuted minima are removed
  and replaced by a pointer. I checked the pointer resolves and prints: `python
  -m pytest -q -s ... -k REPORTED` emits `dropped_flip minimum 6.264e+05x`,
  `wrong_dof_index 2.838e+05x`, `dropped_shear_parameter 0.0006932x`,
  `one_element_scaled 8.701e+06x`, each with its entry and `L/r_min`. This is
  BI3's second option done properly and it is the cleanest thing in the range.
- **R123 (blocking) -- OPEN, and the directed answer is refuted by measurement,
  correctly.** See the headline above and **R130** for what the evidence
  supports instead. The implementer's refusal to decide this inside a HOLD is
  right.
- **R124 (blocking) -- CLOSED IN THE CODE, OPEN IN THE PLAN.** The selection no
  longer uses the constant it bounds: `_detection_edge` bisects on
  `defect_size=mid` and `_smallest_detection_edge` takes `min` over all 81
  solved entries, neither of which reads `PATCH_TEST_EXACTNESS_COUNTER_DEFECT`.
  I solved the boundary instead of sampling it -- `2.36e-6` passes, `2.38e-6`
  fails, against `6.0e7 x 3.9459e-14 = 2.3675e-6` -- so the published `2.37x` is
  now a solved quantity and correct. The plan's copy is **R129**.
- **R125 (recordable) -- CLOSED, and it now has data.** Ties are broken by name.
  At `7daffed` the minimum was unique, so the tie-break had nothing exercising
  it; my `aaa_band_edge_twin` bisects to `3.9459028621e-14`, bit-identical to
  `band_edge_isotropic_bracing`, and the guard's printed line moves to
  `detection edge 3.9459e-14 at aaa_band_edge_twin` with the ratio unchanged.
  The identical defect survives in the sibling entry -- **R136**.
- **R126 (blocking) -- CLOSED, and the control fires.** I broke it: replacing
  `classify`'s body with `return "live"` reddens
  `test_a_NO_OP_defect_classifies_below_resolution` in 0.60s. `no_op` is in
  `DEFECT_BUILDERS` and not in `INJECTED_DEFECTS` (`grep -n "no_op"`), so it
  cannot be reached as a defect. The unrecognised-name raise is **eager** --
  before `def build` -- which is why `pytest.raises` on the factory is a real
  check and not a deferred one. `delta > 0.0` is gone. What the new branch costs
  is **R139**.
- **R127 (recordable) -- CLOSED at the site it named**
  (`test_patch_test.py:970-980`), and the two entries are now separated by
  classification rather than generalised. The identical sentence stands in the
  plan at `F2.md:531`, 111 lines above `F2.md:642-645` which corrects it --
  **R129**.
- **R128 (recordable) -- CLOSED.** The range is now justified by purpose (R53's
  index mapping) with no floor argument, and it says so. The honest paragraph
  about the previous version's deleted quantity is kept.
- **R113 -- carried, OPEN, correctly declared.** `grep -n "_section(entry"` still
  returns `:673` inside `_inadmissible`.
- **R95 -- carried, OPEN, correctly declared.** `pytest.raises(ValueError)` with
  no `match` at `:738`. Note the two new raises tests do carry `match=`, so the
  pattern is being followed for new code.
- **R97 -- carried, OPEN.** `grep -n "never asserted at a constant"
  docs/milestones/F2.md` returns `:697` and `:1412`.
- **R98 -- carried, OPEN.** `INADMISSIBLE` still four occurrences, none an
  assertion.
- **R100 -- carried, OPEN, and it took on weight again.** `ls scripts/` is still
  `write_verdict.py` alone. Two figures in the re-derived
  `PATCH_TEST_COUNTER_HEADROOM` entry are wrong at the fourth digit against the
  file's own runner (**R132**), and a third in the sibling entry names an
  operating point the runner contradicts (**R136**). BI3 was written to stop
  exactly this and BI3's mechanism was deferred to F2a.
- **R101, R102, R103 -- carried, OPEN.** `grep -n "revision 1"
  floatfea/tolerances.py` returns `:189` and `:624`, both "revision 10".
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** The report omits it from the
  carry; it is withdrawn, so nothing turns on it.
- **R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 -- still
  open**, routed to step 4a or later. The report carries them as "the older set"
  rather than by number, which is a slip from the standard the last three reports
  held; I am not making it a finding.
- **R115-R121 -- closed at the fourteenth verdict**, correctly recorded.
- **R68's standard -- LAPSED this round.** Nine rounds of eight. Sections 1-5 are
  rule-carrying and good. What is missing is the section the last three reports
  carried first: the round's own errors. Revision 15 records none, in a round
  whose own commit message contains a stale entry count, an orders-of-magnitude
  figure wrong by two, and a causal claim its own module structure refutes
  (**R133-R135**). Not a finding on its own; recorded because the section was the
  thing that made the last three reports trustworthy.

## Findings

**R129. (STOP) The locked plan is not the shipped code. `F2.md` states
`PATCH_TEST_COUNTER_HEADROOM = 2.0e7` where `6.0e7` ships, and carries four
statements the runner refutes -- one of which the report says has been removed.**
`docs/milestones/F2.md:531`, `:542`, `:557-560`, `:564`; `git diff --stat
baee1db..7daffed -- docs/milestones/F2.md` is empty.

```
claim  "The 'any raise of 2.31x' sentence is gone with the selection that
        produced it."                                   -- report sec. 1
cmd    grep -rn "2.31x" docs/milestones/F2.md
out    :559  shipped value has `2.30x` of room and **any raise of 2.31x or more
             fails the build
```

Four further sites, each refuted by one command at this commit:

```
:558   "PATCH_TEST_COUNTER_HEADROOM = 2.0e7"
       cmd  grep -n "COUNTER_HEADROOM: Final" floatfea/tolerances.py
       out  PATCH_TEST_COUNTER_HEADROOM: Final[float] = 6.0e7

:557-9 "the edge is 1.1513e-13 at slender_axis_L_r_189 ... 8.686e+06x ... 2.30x"
       cmd  python -m pytest -q -s <runner> -k counter_DEFECT_SIZE
       out  detection edge 3.9459e-14 at aaa_band_edge_twin; 2.534e+07x it,
            against a headroom of 6e+07 (2.37x of room)

:564   "A corpus entry that is harder to detect raises the edge and *loosens*
        the guard"
       cell  the selection is now min-over-entries; nine entries added at
             dac209e, five of them the most slender in the corpus
       out   min edge with them 3.945903e-14; without them 3.945903e-14 -- 0%.
             A harder entry CANNOT raise a minimum. The sentence was true under
             the max-selection R124 refuted and moved with nothing.

:542   "Phi ~ 1/lambda^2 does shrink the defect on a slender member; it does not
        take it below the ceiling anywhere in the corpus"
       cmd   python -m pytest -q
       out   5 entries at or below it

:531   "On 2 further near-axis entries the injected difference leaves the
        interior balance below the ceiling"
       -- the sentence R120 found and R127 corrected in test_patch_test.py,
       still standing 111 lines above F2.md:642-645, which corrects it in the
       same document.
```

The value change is *justified*: under the corrected selection the old `2.0e7`
genuinely fails, the justification is written at the site, and the direction is
forced by a code correction I directed. That is not the finding. The finding is
that a locked plan now specifies a different number from the one that ships, and
was neither reopened nor amended, in a milestone whose working agreement makes
that the one thing you stop for. **Closed when** `F2.md` is reopened and the five
sites are answered site by site, or each is stated as left with a reason.

**R130. (STOP) Rung 1 is red, and the evidence says the missing thing is not a
slenderness domain but the block the defect lands in -- with a measured
coefficient. The gate's declared resolution is a whole-element resolution, and
the counter-defect that certifies it is injected in the one block where the gate
is `8.7e6x` more sensitive than in the block every shipped formulation defect
lives in.** `tests/verification/rung1/test_corpus_configurations.py:919-940`
(`classify`), `:1015-1040`; `floatfea/tolerances.py:449-455`.

You asked what the evidence supports. It supports the third option, and the
block-dependence has a constant:

```
rule  worst state against PATCH_TEST_EXACTNESS, defect size held at 1e-6,
      injected on element 1 only; ONE variable moved -- the local block
cell  R(lam) = (bending-block response) / (whole-element response)
out   lam      389    2676    2886   14428   19237   23084     sections: four
      R    1.40e-5 2.79e-7 2.40e-7 9.61e-9 5.41e-9 3.75e-9
      lam^2 R  2.12    2.00    2.00    2.00    2.00    2.00
      => R = 2.00 / lam^2 to +/-6% over 59x in lam and four section families
```

My reimplementation of the injection is bit-identical to the shipped
`one_element_scaled` route (`rel 0.00e+00` at `plan_headline_lam2885`), so this
is the operator the gate runs, not a textbook one. Two consequences, both solved
rather than sampled:

```
cmd   bisect L for a BENDING-ONLY defect of exactly the DECLARED size 1e-6,
      D=0.600 t=0.01200 axis, L the only variable moved
out   L = 867.42, lam = 4171.7 -- above this the gate does NOT redden on a
      defect of exactly the size it declares it resolves
      (and lam = 4172 is what R = 2/lam^2 predicts, from the other direction)

out   the same 1e-6 as a WHOLE-element defect at lam = 23084: 8.701e+06x
      the ceiling. The counter-defect is 8.7e6x flattered by where it lands.
```

`classify` compares a block-agnostic `injected_delta` against a constant
calibrated on a whole-element defect. The shear defect is not anomalous; it is
the first shipped defect small enough for the block to matter. `dropped_flip`
(delta `2.0`) and `wrong_dof_index` (delta `inf`) live in the same blocks and
clear the bending edge by `10^5`.

**And this was already in the repository before the rule was built.**
`floatfea/tolerances.py:449-452` -- "the residual normalises by the largest
stiffness -- the axial one -- so any defect in a bending block falls as
`1/lambda_weak^2`. Measured, both structural defects fall at exponent `-1.99`" --
`git blame` dates it to `a458662`, 2026-09-06, **two step commits before** BQ0.
My directive and the implementer's premise were both refutable from the file the
constant lives in. That is my error more than anyone's.

What I do not recommend is a per-entry *measured* resolution: `classify`'s own
docstring is right that a gate which coarsens its own resolution exempts what it
stopped seeing (R56). A declared constant times `lam^2` is not that -- it is a
stated scaling law with one measured coefficient, it reddens if sensitivity
moves, and it is falsifiable. **Closed when** the plan reopens and states which
of the three it takes, with the block-dependence measured or explicitly declined.

**R131. (blocking) The commit created a two-line path in `tolerances.py` out of a
red gate that did not exist before it, and the guard that blocks it is a single
test whose own constant has `422x` of room.**
`tests/verification/rung1/test_corpus_configurations.py:919-940`, `:990-1000`.

```
cell  both constants moved, nothing else, full suite each time
out   CD 1e-6 -> 1e-4, HEADROOM 6.0e7             1 failed  (the guard fires)
      CD 1e-6 -> 1e-4, HEADROOM 6.0e7 -> 3.0e9    900 passed
```

**900 passed.** Both reds go green by exemption, not by detection.
`test_every_entry_carries_at_least_one_LIVE_defect` cannot see it -- the entries
still carry three live defects each. Before `classify`, a defect that failed to
redden was a hard failure with no constant to move.

I am not alleging this was done; the implementer committed red and said the
decision was not theirs, which is the right call and I credit it. The finding is
that the surface now exists, on the one gate whose whole purpose is that a
formulation defect cannot be tolerated into silence. **Closed when** the
exemption is bounded by something that is not the same constant family the
sensitivity claim rests on -- or the plan records the surface and why it is
accepted.

**R132. (blocking) The re-derived tolerance entry's two headline figures do not
match the file's own runner at the same commit, at the fourth digit. This is
BI3's failure mode inside the entry re-derived under BI3.**
`floatfea/tolerances.py:496-497`; report sec. 1.

```
published  smallest edge 3.9413e-14 ... shipped 1e-6 sits 2.537e+07x above it
cmd        python -m pytest -q -s <runner> -k counter_DEFECT_SIZE
out        detection edge 3.9459e-14 ... 2.534e+07x it
```

`0.12%`, in the safe direction, and nothing turns on it numerically -- the guard
fires at `2.5e7` and passes at `2.6e7` either way. It matters because the number
was published in the commit that also published "RE-DERIVED 2026-09-07 with the
selection rule", and it was not taken from the runner that prints it four lines
of output away. The report repeats both figures in sec. 1. **Closed when** both
sites carry the runner's figures or point at the line that prints them.

**R133. (blocking) The `_measure` comment's causal chain is structurally
impossible in the shipped code, and the fix it justifies is guarded by nothing.**
`tests/verification/rung1/test_corpus_configurations.py:522-528`, `:1015-1040`;
report sec. 3.

```
claim  "(1+size)-1 ... and classify, comparing the measured size against the
        declared one, put the gate's OWN counter-defect below its own resolution
        on every entry. The arithmetic was deciding a classification."
rule   classify -> injected_delta -> _build, system.local_stiffness,
       _defective_stiffness.  It never calls _measure.
cell   revert :529 to ((1.0 + defect_size) - 1.0) * element_global_stiffness(...),
       nothing else moved, whole module
out    2 failed, 481 passed -- IDENTICAL to the shipped result, and
       test_the_delta_measure_is_CALIBRATED is GREEN
```

So (a) the classification consequence attributed to `_measure`'s arithmetic
cannot arise, because `injected_delta` computes `bad = clean + CD*clean` in its
own body; and (b) **nothing in the suite would catch the re-introduction of the
old form.** `test_the_delta_measure_is_CALIBRATED` is credited with finding it
and does not test it.

The fix is right and the stated magnitude is wrong in the place it mattered. At
`size = 1e-6` the loss is `4.5e-11` relative and harmless. At the *edge* scale
`_detection_edge` bisects over, `(1+x)-1` quantises the injected size to
multiples of `ulp(1) = 2.22e-16`:

```
cmd   x = 1.152090e-13; (1+x)-1
out   1.1524115e-13 -- 2.79e-04 relative, and the quantisation step is 1.93e-03
      of x. The published edge moved 1.1513e-13 -> 1.15209e-13 for exactly this
      reason: the old bisection was searching a staircase.
```

Seven orders larger than the `2e-10` the comment states, and it is the reason a
published boundary moved. **Closed when** the comment states the consequence it
can have (a quantised bisection at `1e-13`, not a classification), and either a
check exists that reddens on the old form or the report says plainly that none
does. BG0: the cell, or the bare measurement with no cause attached.

**R134. (recordable) "nine orders smaller" is 6.99 orders.** report sec. 5;
`3830838` commit message.

```
cmd   4.3507e-08 / 4.4030e-15
out   9.881e+06  -- 6.99 orders
```

Both operands are the report's own and both reproduce on my run; the subtraction
does not. "Nine orders" is the phrase attached to a different comparison at
`tolerances.py:444-446`. **Closed when** the figure is the one the two numbers
give.

**R135. (recordable) "on all 74 solved entries" -- `SOLVED` is 81 at this
commit, and the report's own next sentence says so.** report sec. 3.

```
cmd   len(SOLVED)
out   81         (and 324 pairs = 81 x 4, which the same paragraph quotes)
```

The corpus went to 81 solved at `dac209e`, before this range opened. BP0's own
case, in the paragraph about a measure being in the same units as its claim.

**R136. (recordable) R125's defect survives in the sibling entry, and the runner
now contradicts the operating point it names.** `floatfea/tolerances.py:459`.

```
published  "the gate still reddens on it at every entry in the corpus, minimum
            8.701e+06x the ceiling at L/r_min = 558"
cmd        python -m pytest -q -s <runner> -k REPORTED
out        one_element_scaled  minimum 8.701e+06x  at posed_axis (L/r_min 46.5)
```

The value holds; the operating point is a tie label, and the tie is now broken
somewhere else. Same species as R125, one entry above it, unfixed. **Closed
when** the sentence points at the line the runner prints, per BI3.

**R137. (recordable) The assertion inside the exemption branch is a tautology of
the predicate that reached it and cannot fail.**
`tests/verification/rung1/test_corpus_configurations.py:997`.

`classify` returns "below resolution" **iff** `injected_delta(entry, kind) <
PATCH_TEST_EXACTNESS_COUNTER_DEFECT`; the branch then asserts exactly that, with
`delta` from the same call. If the thing it claims were false the branch would
not have been entered. It costs nothing and certifies nothing, in the module
whose previous section title was "controls that cannot be vacuous". **Closed
when** it is removed or replaced by something the branch does not already know.

**R138. (recordable) Eight call sites still apply the perturbation as
`(1 + size) - 1`, in the module the detection thresholds are measured in.**
`tests/verification/rung1/test_patch_test.py:454`, `:462`, reached from `:694`,
`:729`, `:831`, `:852`, `:1037`, `:1175`, `:1199`.

The report's sec. 3 says "The size is now applied directly" with no scope.
Measured, the harm there is bounded and small -- the worst case is
`DETECTION_THRESHOLD["axial"] = 1.01e-13`, where the quantisation is `2.2e-03`
relative against a `5%` band -- so this is a wording finding, not a numerical
one. It is listed because it is the same form the commit message calls "a real
defect in the injection", left standing in the module the constants it moved were
measured in.

**R139. (blocking) An exempted pair is printed indistinguishably from an
asserted one, so the exemption the new branch introduces is invisible in the
output that is supposed to make it visible.**
`tests/verification/rung1/test_corpus_configurations.py:991-999`, `:1231`.

The branch's comment says the pair "is classified, every classified pair is
printed by `test_the_forward_error_is_REPORTED_and_the_floor_is_too`". It is
printed. It is not marked:

```
cmd   python -m pytest -q -s <runner> -k REPORTED   (with my corpus)
out   shear_defect_live_thin_L1990   ...  dropped_shear_pa  0.0006932   ASSERTED
      shear_defect_exempt_L2500      ...  dropped_shear_pa  0.002448    EXEMPT
```

Same column, same format, no marker, and no line anywhere in the output giving
the number of exempted pairs. A reader of that table cannot tell which pairs the
gate held to the ceiling. At `7daffed` this is latent -- **0 of 324 pairs
classify below resolution**, so the branch is dead except for the `no_op`
control, which is itself worth saying: the new rule exempted nothing and
reddened two entries. My corpus makes it live. **Closed when** the classification
appears in the printed table and the count of exempted pairs is printed, so an
exemption cannot arrive unremarked.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COUNTER_HEADROOM` | `2.0e7` | `6.0e7` | relative, dimensionless -- a bound on the ratio of a defect size to the smallest solved detection edge over the corpus | `test_a_RAISED_counter_defect_breaks_that`, in the defect quantity. Verified by moving the constant: `2.5e7` fails, `2.6e7` passes, `2.0e10` passes, `3.0e10` fails -- bounded below at `2.534e+07` and above at `2.534e+10`, `422.4x` of room | `tolerances.py:489-505`; **NOT in `F2.md`, which still says `2.0e7` (R129)**; two of its figures refuted by its own runner (R132) |
| `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` | `1.0e-6` | `1.0e-6` unchanged | -- | -- | boundary now **solved**, not derived: `2.36e-6` passes, `2.38e-6` fails, against `6.0e7 x 3.9459e-14 = 2.3675e-6`. R124's substance closed |
| `PATCH_TEST_EXACTNESS` | `5e-15` | `5e-15` unchanged | -- | -- | untouched |

`git diff baee1db..7daffed -- floatfea/tolerances.py` is `+22 -8`: one value, one
rewritten reason, no constant added or removed. `grep -rn "xfail|pytest.skip"
tests/` returns nothing. `git diff --stat baee1db..7daffed -- tests/regression`
is empty -- no golden file moved, and no `expect` field on any corpus line was
touched.

On the standing rule: this **is** a tolerance change in the same commit as the
code that forces it. I do not record it as a "never widen" violation, because
the code change is a correction I directed, the old value provably fails under
it, and the direction is not chosen -- `2.0e7` is arithmetically impossible once
the minimum edge replaces the largest. The effective loosening is
`2.30e-6 -> 2.37e-6` on the quantity that matters, `+2.9%`. What is wrong is that
the locked plan still publishes the superseded value (R129).

I re-derived every published figure independently. `3.571067e-05`,
`2.479899e-05`, `0.8806x`, `0.4247x`, `Phi 1.39e-06 .. 2.38e-05`, `149x`,
`L/12.241`, `2.37x`, `422.4x`, `1.83e-12`, `324 pairs`, `0 below resolution`,
and the tie at `3.9459028621e-14` -- **all reproduce**, except `3.9413e-14`,
`2.537e+07`, `74 entries` and `nine orders`, which do not.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin, and neither does any further
step-4 work until the plan reopens. This is a STOP and I will not soften it: the
rung is red, and the fix is a decision about what the gate asserts, not a code
change inside the step.

1. **`docs/milestones/F2.md` reopens (R129).** Five sites, answered site by site:
   the value at `:558`, the edge and boundary at `:557-560`, the refuted "harder
   entry loosens" mechanism at `:564`, the shear claim at `:542`, and the
   `near-axis` sentence at `:531` that the same document corrects at `:642-645`.
2. **The scope decision (R130), in the reopened plan.** Slenderness domain,
   corrected numbers, or block-dependence. My evidence: `R = 2.00/lam^2` to
   `+/-6%` over `59x` in `lam` and four section families; the declared `1e-6` is
   a whole-element resolution and fails for a bending-only defect above
   `lam = 4172` (solved, `L = 867.42`, one variable moved); the counter-defect is
   `8.7e6x` flattered by where it lands; and `tolerances.py:449-452` recorded the
   mechanism two commits before the rule was built.
3. **R131 -- the exemption surface**, bounded or accepted in writing.
4. **R139 -- the exemption is printed unmarked.** My corpus makes it live.
5. **R132, R133 -- two figures and one causal chain**, both in files nobody
   regenerates.
6. **R134, R135, R136, R137, R138 -- recordable**, answerable in prose or one
   line each.
7. **R113, R95, R97, R98, R100-R103 -- carried, unchanged.**

**Adversarial corpus (BE3): 8 new entries committed, all unseen by the
implementer; 3 red at `7daffed`, 5 green, every outcome measured before the line
was written.** `tests/corpus/g22_model_configurations.txt`, now **113**,
committed separately at `f435fed` immediately before this verdict and touching no
code. Full suite with the corpus applied: **5 failed, 935 passed.**

The coverage measurement, stated plainly: **the implementer's check is a
classification rule, and 0 of its 324 shipped pairs exercise the branch that does
the classifying.** Two of my entries put a shipped defect on both sides of it --
`delta = 1.002e-06` live and `1400x` short of reddening, `delta = 6.348e-07`
exempt and green -- so the exemption is measured at its own operating point
rather than argued. A third section family reaches the shear edge, which the
implementer had on two. One entry refutes `L/r_min` as the variable, and refutes
**my own** fourteenth-round `lam^-4` fit while it does so: at fixed geometry with
`I_y/I_z = 0.01`, `L/r_min` moves `19237 -> 192370` and the margin does not move
at all. One forces the exact tie R125's fix has no data for. Two put the same
member in a `10^6` range of length unit and find all four defect margins
identical to four digits -- the strongest positive result of the round, and the
only unit-invariance measurement in the corpus.

**Fifteen consecutive rounds have found no element defect**, and the reading is
unchanged: not yet contradicted, until V5.1 puts CalculiX on the other side. Four
of the four defective instruments this milestone were tests, and the two failures
in front of us are a *rule* that is wrong, on an element that is fine at
`0.0000x` and `0.0098x` of the ceiling on both failing entries.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Fifteen consecutive reviews by one reader.

**The standing question for the next round, and it is the one that decided this
verdict:** the plan is the only document in this repository that is *locked* and
therefore never regenerated, and it is the one nobody diffs. BP0 reached the
report. BI3 reached the tolerance entry, imperfectly. Nothing has reached
`F2.md`, which now states a constant the code does not carry. **For every number
in the locked plan, what is the command that checks it, and what happens to the
plan when the command's answer changes?**
