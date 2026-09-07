# Review — F2 step 4
Reviewed commit: b0bf8811c41758e506bb478dc5603bffa6d84d9b
Verdict: STOP
Tests: 830 passed, 0 failed, 0 skipped   (my run at `de32be3`, `python -m pytest -q`, 6.99s.
With my thirteenth-round corpus applied at `b0bf881`: **4 failed, 852 passed**.)

**Reviewed code commit: `de32be3`.** The header stamp is `b0bf881`, my own corpus
commit, made immediately before this verdict and touching no code.

Thirteenth pass. Range `2dda872..de32be3`, three commits: `88b2d5e` (plan,
re-lock), `a458662` (step) and `de32be3` (report).
`git diff 2dda872..de32be3 -- .claude docs/SUPERVISOR.md CLAUDE.md` is **empty** --
my own instructions were not touched, and I diffed them rather than inferring it
from a green suite that does not read them.

**The form is right and I could not break it, which is the first thing to say
after twelve rounds of the opposite.** BO0's move -- a `_COUNTER` is the injected
defect and the comparison is to the ceiling -- is correct, and I attacked it as
instructed. The plan's numbers reproduce: `wrong_dof_index` at `D=0.6 t=0.012
axis L=600` is `3.5433e-06`, `7.09e+08x` the ceiling, matching the quoted
`3.5e-06` at `L/r_min = 2885.5` to two digits; the three minima `5.150e+09x`,
`5.227e+09x`, `8.701e+06x` reproduce, the last at `slender_axis_L_r_189` exactly
as reported. **I could not construct a configuration at which any named defect
leaves the worst state at or below the ceiling.** The withdrawal of "structural
defects do not fall with slenderness" is right and was made before I asked for
it in those words. Section 0 -- the report opening on a false grep in its own
step commit's message, found by the author -- is the best thing in this round and
is credited without qualification.

**And the verdict is STOP, because the locked plan carries two measured
statements that the shipped runner refutes at this commit, and both are
load-bearing.** Not quantifiers this time; measurements.

```
claim   "the dropped shear parameter is undetectable on 22 of 63 entries"   F2.md:535
        (same sentence: test_corpus_configurations.py:795, report sec. 3)
cmd     Phi -> 0 in both planes, injected into system.local_stiffness, worst
        state per entry, compared to PATCH_TEST_EXACTNESS -- the comparison this
        round adopted; ablation: the same reconstruction with Phi intact returns
        the clean value on 8 of 8 entries checked
out     undetectable on 0 of 69 solved-admissible entries; minimum margin
        9.623e+04x the ceiling at lam1058_axis_counter_red

claim   "the red-on-defect check IS the sensitivity regression guard: a 5x loss
         of sensitivity turns the worst entry red"                          F2.md:544
cmd     inject 1e-6/5 instead of 1e-6, count entries that redden
out     2 of 69 redden, and BOTH are synthetic-anisotropy sections that
        `Section.__post_init__` refuses to construct. Over the 52
        legally-constructible solved entries a 5x loss is GREEN everywhere;
        the smallest legal margin is 5.979x.
```

The first is this round's own diagnosis surviving as a live exclusion: `22 of 63`
is **my** twelfth-verdict figure, measured against `PATCH_TEST_EXACTNESS_COUNTER =
3.5e-05` -- the response floor this round deleted -- and my own verdict said in
the next sentence that the gate catches it everywhere against the ceiling. It was
carried across into a locked plan, a shipped test comment and the report as the
reason a third formulation defect stays out of `INJECTED_DEFECTS`.

## Carried

Every item from the twelfth verdict (`STOP @ 121a35a`, committed `2dda872`),
traced through `2dda872..de32be3` and re-measured, plus the older carry.

- **R105 (STOP) -- CLOSED, and closed at the right level.** The plan no longer
  bounds a domain; it changes the assertion. `grep -n "no exception and no domain"
  docs/milestones/F2.md` is empty, "`O(1)` ... do not fall with slenderness" is
  withdrawn at `F2.md`, `tolerances.py:446-452` and `admissibility.py:124-137`,
  and the `-1.99` exponent I measured is recorded as the reason. The `912` edge
  is gone because the number it was an edge of is gone. This is the fix, not a
  restatement of it.
- **R106 (STOP) -- CLOSED.** `grep -n "detects a 2.5x\|BAND_COUNTER = 3.0"
  docs/milestones/F2.md` is empty; the two surviving `BAND_COUNTER` lines (480,
  546) are withdrawal text. The stale docstring at `:877-881` went with the test.
  **And the report found and recorded a false grep in its own step commit's
  message before I did** -- see R121, which is a credit, not a finding.
- **R107 (blocking) -- ANSWERED BY REMOVAL, and the removal is right.**
  `PATCH_TEST_SENSITIVITY_BAND`, its counter, `SENSITIVITY_SCALE` and
  `SENSITIVITY_EXPONENT` are gone; `grep -rn "SENSITIVITY_BAND\|SENSITIVITY_SCALE"
  --include=*.py .` returns nothing. The `1.01x` margin is recorded as the reason
  rather than argued away. The replacement justification is what fails -- **R117**.
- **R108 (blocking) -- ANSWERED, and the assertion I asked for exists**
  (`test_EVERY_STATE_detects_the_small_defect`). Its worst margin has fallen from
  the `4.27x` I measured over 63 entries to `1.867x` over 69, and its domain is
  not stated: **R116**.
- **R109, R111 -- MOOT, correctly.** Both were about `PATCH_TEST_SENSITIVITY_BAND`
  and the curve's slack; both objects are deleted. Recording them as moot rather
  than closed is the honest word and I accept it.
- **R110 -- CLOSED.** `grep -rn "SENSITIVITY_CURVE" --include=*.py .` is empty.
- **R112 -- CLOSED, and well.** `admissibility.py:121-137` now says what is
  measured (`-1.99`, reporting axis, gates nothing) and drops the "which is why"
  that the plan had withdrawn. The stale three-row table went with it.
- **R113 -- carried, OPEN, correctly declared.** `grep -n "_section(entry"
  tests/verification/rung1/test_corpus_configurations.py` still returns `:634`
  inside `_inadmissible`. Still harmless, still a sentence its own grep contradicts.
- **R114 -- HALF CLOSED, and the half that was closed is not the invariant.**
  `I_y_over_I_z=0` and `=-1.0` now raise at the parser and my two entries go green
  by raising, which is what they asked for and is correctly reported. But the
  guard is a **sign test**, and the invariant `Section.__post_init__` actually
  enforces for a circular shape is `I_y == I_z`. Re-opened as **R119**.
- **R95 -- carried, OPEN, correctly declared.** `pytest.raises(ValueError)` with
  no `match` at `:699`.
- **R97 -- carried, OPEN, correctly declared.** `grep -n "never asserted at a
  constant" docs/milestones/F2.md` returns `:616` and `:1331`.
- **R98 -- carried, OPEN, correctly declared.** `INADMISSIBLE` assigned at `:640`,
  read by no assertion.
- **R100 -- carried, OPEN, correctly routed to step 4a, and the count went DOWN.**
  `ls scripts/` is still `write_verdict.py` alone, but the bracket table and the
  curve table both left `tolerances.py` with the band, and the margins table is
  now printed by the shipped runner. I checked the printed output against the
  entry's text: `8.701e+06x` at `L/r_min 558` matches `tolerances.py:459`.
- **R101 -- carried, OPEN, correctly declared.** `grep -n "revision 1"
  floatfea/tolerances.py` returns `:189` and `:585`, both "revision 10".
- **R102, R103 -- carried, OPEN, correctly declared** (both are about figures in
  earlier report revisions).
- **R63, R76, R79, R80 -- carried, unanswered, correctly declared open.**
- **R65 -- WITHDRAWN by me at the tenth verdict.** Correctly recorded.
- **R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36, R50, R52, R62 -- still
  open**, correctly declared, routed to step 4a or later.
- **R77, R78, R81-R94, R96, R99, R104 -- closed** at earlier verdicts, correctly
  recorded.
- **R68's standard -- HELD.** Seven rounds of six. The `Carried` table names every
  item by number and puts the round's own error first.

## Findings

**R115. (STOP-class, and it is the round's own subject) The constant this round
is about can be raised by twelve orders with the entire suite green.**
`floatfea/tolerances.py:465`; `tests/verification/rung3/test_tolerance_counter_cases.py:96-101`.

`PATCH_TEST_EXACTNESS_COUNTER_DEFECT` was moved and the suite re-run each time,
nothing else touched:

```
  1.0e-9    28 failed, 802 passed
  5.36e-7   the solved edge (below)
  1.0e-6    830 passed   <- shipped
  1.0e-2    830 passed
  1.0e-1    830 passed
  1.0e+3    830 passed
  1.0e+6    830 passed        a defect that multiplies one element by a MILLION
```

**Raising a `_COUNTER_DEFECT` weakens the claim** -- "the gate reddens on a
sixth-digit slip" is strictly stronger than "the gate reddens on a 100x element"
-- and nothing in the repository notices the weakening. The ablation that makes
this a finding rather than an observation: the same move on a response-quantity
counter is caught. `RESULTANT_EXACTNESS_COUNTER` x1e3, everything else held,
gives **12 failed, 818 passed**. The old form was bounded in both directions --
below by `ceiling < counter`, above by the measurement itself. The
`_COUNTER_DEFECT` exemption at `:96-101` removes the first (correctly: the
quantities differ) and the change of assertion removes the second, and nothing
replaced either.

*Invert the decision rule and solve*, which the entry does not:

```
  smallest defect the assertion still detects, per entry
    flip_counter_edge_thickwall  L/r_min 2332   5.3555e-07   -> 1.867x of room
    band_edge_isotropic_bracing  L/r_min  389   7.7898e-09   -> 128x of room
```

So `1.0e-6` is one arbitrary perturbation, not a detection threshold -- which is
the incompleteness the standing guard names, and which now has **no** mechanical
guard at all. This matters beyond bookkeeping: **R116 puts four entries red on
the assertion that binds this constant from below, and the cheapest green is to
raise the constant.** Nothing would go red if someone did.

**Closed when** the value is either set to the solved detection threshold and
bracketed (a test that reddens when it is raised, in the defect quantity, not the
response quantity), or the entry states in one line that the number is unbounded
above and names what would catch a widening.
`SOLVE_BACKWARD_ERROR_FACTOR_COUNTER_DEFECT` and
`PATCH_TEST_COND_FACTOR_COUNTER_DEFECT` are the same class and inherit the answer.

**R116. (STOP) `test_EVERY_STATE_detects_the_small_defect` is asserted over every
entry with no domain, and its edge is inside the configuration this round's own
plan, tolerances entry and report all cite as their headline.**
`tests/verification/rung1/test_corpus_configurations.py:860-885`;
`floatfea/tolerances.py:420`, `:444`; `docs/reports/F2/step-4.md` sec. 1 and 4.

The plan's example is `L/r_min = 2885`, quoted three times as the proof that
detection is nine orders wide. I built it -- `D=0.600 t=0.01200 axis L=600`, a
plain circular tube, no extras, no synthetic anisotropy -- and both halves are
true at once:

```
  wrong_dof_index      3.5433e-06  = 7.087e+08x the ceiling   the plan's claim, CONFIRMED
  weakest state, 1e-6  4.0195e-15  = 0.804x the ceiling       the SHIPPED assertion, RED
  clean field          8.7e-17     = 0.017x the ceiling       the element is fine here
```

Solved rather than sampled, on the family `D=0.100 t=0.00500 axis` with `L` the
only variable moved:

```
  L      85      90      100     110     120
  L/r  2527    2676     2973    3271    3568
  x     1.048   0.935    0.757   0.626   0.526     edge at L/r_min ~ 2580
```

`2580` is **1.11x** past `flip_counter_edge_thickwall`, the entry that binds the
reported `1.867x`. The report calls that margin "thin, and it is the honest
number", which it is -- but a margin in the response quantity is not the domain,
and the domain is what six rounds of this milestone have been about. The same
edge is reached at `L/D 83` rather than `1000` by moving `L` alone from `35` to
`50` on the binding entry's own family (`0.916x`, clean `0.028x`).

This is not the R105 species relabelled. R105 was a false universal in the
*plan*; this is a true-so-far universal in the *shipped suite*, whose failure
mode is a red test on a correct element, whose cheapest green is R115's
unguarded constant, and whose margin **halved** (`4.27x` -> `1.867x`) when the
corpus grew from 63 entries to 69 without anyone aiming at it.

**Closed when** the per-state claim states the sample it is asserted over and the
solved edge (`L/r_min ~ 2580` on a legal section, lower on the thick-wall
anisotropic family), or the assertion is restricted to a stated domain. Either is
fine. Silence is what is not, because the next corpus round reaches it.

**R117. (STOP) The plan's replacement justification for dropping the band is
false over every legally-constructible entry.** `docs/milestones/F2.md:543-545`.

"**The red-on-defect check is the sensitivity regression guard**: a `5x` loss of
sensitivity turns the worst entry red." Injected -- `1e-6/5` instead of `1e-6`,
everything else held:

```
  loss 5.0x   2 of 69 redden   aniso_weak_lam154_undetectable [synthetic]
                               flip_counter_edge_thickwall    [synthetic]
  loss 4.0x   1 of 69          flip_counter_edge_thickwall    [synthetic]
  loss 2.0x   1 of 69          flip_counter_edge_thickwall    [synthetic]
```

Both are `extra=I_y_over_I_z=` sections -- objects `Section.__post_init__`
explicitly refuses (R119). Over the **52** solved entries the model can actually
build, the smallest margin is `5.979x` (`lam1058_axis_counter_red`), so a `5x`
loss is green everywhere and the sentence is false on the whole legal corpus.

I endorse dropping the band; R107 was mine. What cannot stand is the sentence
that replaced it, because it is the entire recorded reason the gate is still
claimed to guard sensitivity, and it rests on two entries that are not members.

**Closed when** `F2.md:543-545` states the factor measured over the legal corpus
(`5.98x`, one entry), or states that the sensitivity guard now rests on the
synthetic-anisotropy entries and why that is acceptable.

**R118. (STOP) "The dropped shear parameter is undetectable on 22 of 63 entries"
is `0 of 69` at this commit, and it is the live reason a third formulation defect
is not asserted.** `docs/milestones/F2.md:535`;
`tests/verification/rung1/test_corpus_configurations.py:794-797`;
`docs/reports/F2/step-4.md:2109`.

```
cmd   Phi -> 0 in both planes, injected into system.local_stiffness, worst state
      per entry, compared to PATCH_TEST_EXACTNESS
out   undetectable on 0 of 69; smallest margins
        9.623e+04x  L/r_min 1058   lam1058_axis_counter_red
        1.611e+05x  L/r_min  930   lam930_axis_counter_edge
        1.838e+05x  L/r_min  900   lam900_axis_undetectable
abl   the same reconstruction with Phi INTACT returns the clean value on 8 of 8
      entries checked, so the numbers isolate the defect
```

`22 of 63` is my own twelfth-verdict figure and it was measured against
`PATCH_TEST_EXACTNESS_COUNTER = 3.5e-05` -- the response floor this round
deleted. My verdict said so in the adjacent sentence: "**The gate still catches
it**, everywhere, against the *ceiling*." The figure was carried into the locked
plan, into a shipped test comment and into the report, at a commit where the
comparison is to the ceiling, and it is the stated reason `dropped_shear` is not
in `INJECTED_DEFECTS`. **This is the exact artefact BO0 was written to remove,
surviving as the justification for an exclusion.**

The causal sentence attached to it -- "`Phi ~ 1/lambda^2` makes the *defect
itself* vanish on a slender member: there is nothing left to corrupt" -- is a
correct statement about `Phi` whose consequence is refuted: the residual
normalises by the axial stiffness, so a vanishing defect is still `9.6e+04x` the
ceiling. It is also the same reasoning shape the round withdrew for structural
defects, left standing for this one.

**Closed when** the count is re-measured against the ceiling at the commit that
publishes it, in all three places, and the exclusion is either withdrawn (the
defect joins `INJECTED_DEFECTS`) or re-justified on something that is true.
Section 3 of the report is regenerated by rule and this figure was not; that is
`CLAUDE.md` sec. Step gating, not a new rule.

**R119. (blocking) R114 is closed as a sign test; the invariant
`Section.__post_init__` enforces for a circular shape is `I_y == I_z`, it is
still bypassed, and 14 solved entries -- including the one that binds this
round's thinnest margin -- are objects the model refuses to construct.**
`tests/verification/rung1/test_corpus_configurations.py:334-352`, `:426`, `:526`;
`floatfea/model/material.py:95-102`; `tests/unit/test_beam_element.py:194-210`.

```
cmd   dataclasses.replace(Section.circular_tube(0.6, 0.29), I_y=0.01*I_z)
out   ValueError: shape 'thin_tube' is circular but I_y != I_z. ... this object
      would draw the circular kappa and the circular J for a section that is
      neither.

cmd   corpus entries carrying extra=I_y_over_I_z=, solved
out   14, every one shape='thin_tube' with I_y != I_z
```

`tests/unit/test_beam_element.py:194-210` builds the same object by the same
route, labels it honestly, and states the contract: "**it is never solved with**".
This module solves with it 14 times. The new guard at `:334-352` restores the
positivity half of `__post_init__` and not the half that names this route.

Executable, not argued: `extra=I_y_over_I_z=1e-300` passes the new sign test,
builds a member with `L/r_min = 4.8e+152`, passes the exactness ceiling at
`0.0045x`, and its weakest-state response to a `1e-6` defect is **exactly `0.0`**.
`aniso_denormal_I_y_must_refuse` is in the corpus at `expect=raise` and is red.

This is load-bearing, not hygiene: the two thinnest per-state margins in the
corpus (`1.867x`, `4.274x`) are both on these objects, R117's entire sensitivity
guard is these objects, and the twelfth round's `I_y <-> I_z` refutation was
measured on them.

**Closed when** each named site is answered: `:426` and `:526` construct the
section by a route the type admits or the guard states which invariant it is
standing in for; the comment at `:339` stops naming `Section.__post_init__` as
"the only guard" while restoring half of it; and the report says whether a
`thin_tube` with `I_y != I_z` is a configuration G2.2 claims anything about,
given that `test_beam_element.py` says it is never solved with.

**R120. (recordable) The transposed transform's "2 further near-axis entries" is
right in its count and wrong in its mechanism, on all three copies.**
`docs/milestones/F2.md:529-532`;
`tests/verification/rung1/test_corpus_configurations.py:788-794`;
`tests/verification/rung1/test_patch_test.py:961-968`; report sec. 3.

The `8` reproduces exactly -- `|R - R.T| = 0` on `lam1058_axis_counter_red`,
`lam900_axis_undetectable`, `lam930_axis_counter_edge`, `posed_axis`,
`slender_axis_L_r_118`, `slender_axis_L_r_189`, `tier2_axis_lam65_metre`,
`vertical_onode`, and nowhere else. The `2` reproduces as a count. The mechanism
does not:

```
  onode_just_outside         |R - R.T| = 2.000   |to_global(k,R.T) - to_global(k,R)| = 0.0 EXACTLY
  straddle_above_lam61_axis  |R - R.T| = 1.197   relative delta 3.09e-18  (round-off)
  both: response identical to the clean value in ALL SIX states
```

Neither is "near-axis" -- `2.000` is as far from symmetric as a rotation matrix
gets -- and the difference is not "below the ceiling", it is *absent*. The true
statement is stronger and cheap: on `10` entries the transposed transform changes
the assembled matrix by nothing, and `R`'s symmetry is not the criterion; for an
isotropic section `to_global(k, R)` is invariant under a relabelling that acts as
a roll, which is why a member with `R.T != R` can still see nothing. **A number
that is correct does not license the explanation attached to it (BG0)** -- and
this is the third round in three where the ratio was right and the mechanism was
not.

**Closed when** the sentence describes what was measured (the injected
`to_global` difference, not `|R - R.T|`) in all three copies, or says `10`
entries with the criterion left as measured rather than named.

**R121. (credit, not a finding) Section 0.** I verified both halves. `a458662`'s
message says `grep -n "2.5x\|BAND_COUNTER" F2.md` is empty; it returns `:480` and
`:546`, both withdrawal text. The correction the report gives is true: `grep -n
"detects a 2.5x\|BAND_COUNTER = 3.0" docs/milestones/F2.md` returns nothing.
Recording a false claim in one's own commit message, first, in the round that
cites BF0, is the standard this project has been trying to reach, and it is
recorded so the next reader can see it was not extracted.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_EXACTNESS_COUNTER` | `3.5e-05` | **removed** | -- | -- | `tolerances.py:428-465`, `F2.md:469-500`, report sec. 1 |
| `PATCH_TEST_EXACTNESS_COUNTER_DEFECT` | -- | `1.0e-6` **new** | relative, dimensionless defect size | it *is* the counter; margin to ceiling `8.701e+06x` at `L/r_min 558`, reproduced | `tolerances.py:430-465` -- **and it is unbounded above (R115)** |
| `PATCH_TEST_SENSITIVITY_BAND` | `0.60` | **removed** | -- | -- | `F2.md:541-548` (R107) |
| `PATCH_TEST_SENSITIVITY_BAND_COUNTER` | `5.0` | **removed** | -- | -- | same |
| `PATCH_TEST_EXACTNESS` | `5e-15` | `5e-15` unchanged | -- | -- | comment rewritten only |

**Three removals and one addition, and the ceiling did not move.** That is the
right shape for this round and I want it on the record: the failing assertions of
the last two rounds were answered by deleting the numbers that were wrong, not by
moving them. `grep -rn "xfail\|pytest.skip" tests/` returns nothing.
`git diff --stat 2dda872..de32be3 -- tests/regression tests/corpus` is empty --
no golden file moved and no `expect` on any corpus line was touched.

I re-derived every published figure independently. `8.701e+06x` at
`slender_axis_L_r_189`, `5.150e+09x`, `5.227e+09x`, `0.0887x` worst clean,
`1.867x` worst per-state, `3.5433e-06` at `L/r_min 2885`, `|R - R.T| = 0` on 8
entries -- all reproduce. **Every number in this round is right.** Two of the
sentences built on them are not, and one constant has no guard.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin, and **neither does another step
commit**. This is a STOP: `docs/milestones/F2.md` reopens. The suite at `de32be3`
is green, the element is not implicated in anything here, and every red at
`b0bf881` is mine.

1. **R118 -- the plan states `22 of 63` where the runner says `0 of 69`.** One
   measurement, three files, and it is the reason a real formulation defect is
   excluded. Cheapest of the four and the least defensible to leave.
2. **R117 -- the band's replacement justification.** `5x` is caught by two
   entries the model refuses to build; `5.98x` is the legal number.
3. **R115 -- the counter has no guard in the direction that weakens it.**
   `1.0e+6` leaves the suite green. Answer this before R116, because R116's
   reds make raising it the cheapest fix.
4. **R116 -- the per-state claim's domain.** State the sample and the solved edge
   (`L/r_min ~ 2580`), or restrict the assertion. The plan's own headline
   configuration is past it.
5. **R119 -- R114's other half**, site by site. `expect=raise` is answered for
   `0` and `-1.0`; `1e-300` and `I_y != I_z` on a circular shape are not.
6. **R120 -- recordable**, three copies of one sentence.
7. **R113, R95, R97, R98, R100-R103 -- carried, unchanged**, answerable in the
   next report's `Carried` section.

**Adversarial corpus (BE3): 6 new entries committed, all unseen by the
implementer; 4 red at `de32be3`, 2 green as predicted.**
`tests/corpus/g22_model_configurations.txt`, now **96**, committed separately at
`b0bf881` immediately before this verdict and touching no code. Full suite with
the corpus applied: **4 failed, 852 passed**. Every outcome was predicted from a
measurement before the line was written, and the two green entries are there so
the four reds mean something: `every_state_edge_iso_L85` brackets the edge from
inside at `1.048x`, and `aniso_ratio_one_is_a_noop` shows the synthetic route at
ratio `1.0` changes nothing, so R119's reds are about the ratio and not the
route.

The coverage measurement, stated plainly: **three configurations cross a shipped
assertion's undeclared edge -- one of them the plan's own worked example -- one
shows the new admission guard is a sign test, and two are witnesses that pin the
brackets.** The implementer's own count -- 69 solved entries, three injected
defects -- is what it is.

**Thirteen consecutive rounds have found no element defect**, and the guard's
reading is unchanged: not yet contradicted, until V5.1 puts CalculiX on the other
side. What changed this round is worth naming. The twelfth verdict said every
remaining error was a quantifier. That is no longer the whole of it: BO0 fixed
the quantifier problem at the level it lived at, and what is left underneath is
narrower and older -- **a number measured under one decision rule, republished
under another.** `22 of 63` was measured against a floor that no longer exists.
`5x` was measured over a corpus that includes objects the type refuses. `1.867x`
is a margin in a quantity, quoted where a domain was needed. In each case the
measurement was correct when it was taken and false when it was read, and nothing
in the repository re-takes a measurement when the rule beneath it moves. BI3
named this for tables in `tolerances.py`; it is not a tables problem.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass.
Thirteen consecutive reviews by one reader, and the standing consequence is
unchanged.

**The standing question for the next round:** for every figure republished in
this diff, **under which decision rule was it measured, and is that rule still
the one in force?** If the rule moved, the figure is stale even though nobody
edited it, and a green suite will never say so.
