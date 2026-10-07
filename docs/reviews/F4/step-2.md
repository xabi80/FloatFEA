# Review — F4 step 2
Reviewed commit: bac301796de7190f3bdf52a47a3c7dfe40a46669
Verdict: HOLD

**Reviewed commit: `bac3017`** (`bac301796de7190f3bdf52a47a3c7dfe40a46669`, HEAD of F3,
pushed, tree clean).
Tests: **3236 passed, 0 failed, 0 skipped** (MY OWN run, ONE invocation, no `--ignore`, no
`-k`, no deselection, in the repository itself, `654.90s`. Not the report's figure: the
report's `2855 passed` is `scripts/suite_count.py` at `b68f2f7` with the 381 report-guard
cases excluded, and `2855 + 381 = 3236` reconciles exactly.)

## Round of 2026-10-06 -- ROUND 2 OF THREE. ONE REVISION REMAINS.

**ES0's premise verified first, because the round count rests on it.**

```
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-2.md
out    bac3017 report: F4 step 2 revision 2 -- EQ3's DQ4/DQ5, R685, DQ8 per body, R704/R705
judge  a NEW report revision exists, so ES0's exemption does NOT apply. Verdict 97 was
       round 1; 98, 99, 100 and 101 were interim checks against none; this is ROUND 2.
       ONE REVISION REMAINS and the next one is the closer.
```

**Instruction 1b, checked mechanically rather than by reading.** The file's top line at
`docs/reports/F4/step-2.md:3` still says `Answers: verdict 96 @ 5786bed`; revision 2's own
header at `:719` says `Answers: verdict 101 @ 4b8f079`, which is the newest verdict and the
commit I judged last.

```
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
         tests/test_report_guard_states.py -q -p no:randomly
out    381 passed in 154.16s
judge  `test_the_answered_verdict_is_the_NEWEST_one` is inside that 381 and is green, so
       the guard reads `:719` and not `:3`. 1b does not fire. The stale `:3` line is C13.
```

**AND THE RANGE, COMPUTED RATHER THAN TAKEN.** The hand-back says `e76f165..HEAD` is three
commits and it is right this time.

```
cmd    git rev-list --count e76f165..HEAD
out    3
cmd    git log --oneline e76f165..HEAD
out    bac3017 / b68f2f7 / 36a5003
judge  36a5003 and b68f2f7 are the work; bac3017 is the revision. Nothing is scoped out of
       my reading, and I read the whole range.
```

**HOLD, TWO BLOCKING ITEMS, AND BOTH ARE INSIDE THIS ROUND'S OWN REPAIRS.**

* **R705 is CLOSED.** The signed comparison is right, the signs are independently derivable
  (I derived them from the construction's own `(L^2/12) e1 x w` rather than from
  `local_mass`), the shipped counter-case holds the rule, and I reproduced the ablation.
  This is the best-executed item in the range.
* **R704's repair carries a new blocking finding, R706.** The expected side is now the
  closed form at the body's own `f` and that half is correct. **The floor `0.04` is derived
  against the platform arm alone and sits ABOVE the defect on the twelve hub arms at
  `f = 0.1`** -- `0.03529411764705815` against a floor of `0.04` -- where the ceiling it
  brackets is asserted over all sixteen members with `assert checked == 16`. That is R682's
  and R694's finding verbatim, the fourth time in this block, and **the sentence refuting it
  is already in the entry eighteen lines above the value**: `floatfea/tolerances.py:1990`,
  "C149's correction stands -- the hub arms are the smaller figure".
* **R707 is mine, from EU1's adversarial case, and the implementer named the suspicion
  itself without measuring it.** DQ4(i)'s expected side reads `body.remainder_mass` and
  `body.remainder_node` -- the same two attributes `body_mass_matrix` reads -- so the gate
  cannot fail on either. A **doubled** remainder mass and the remainder lumped at **any of
  the six nodes** both read the clean value to every digit.

**No STOP.** The ladder is SUCCESS at every step in CI at the newest code-bearing commit, no
low rung is red, and `.claude`, `docs/SUPERVISOR.md` and `tests/conftest.py` are all
untouched in this range (section 1).

## 0. CI -- NO RUN AT `bac3017` BY DESIGN, AND THE RUN AT `b68f2f7` IS RED

```
cmd    gh run list --commit bac3017 --json name,conclusion,workflowName,status
out    []
cmd    grep -n paths-ignore -A 3 .github/workflows/ci.yml | head -6
out    paths-ignore:
out      - "docs/reports/**"
judge  a report-only commit runs nothing. This is NOT CK2 -- there is no exhausted-
       allowance job here, there is no job at all -- and it is the same situation I ruled
       on at `fa709df`. Recorded as what it is: NO RUN at the reviewed commit.
```

```
cmd    gh run list --commit b68f2f7 --json conclusion,databaseId,status
out    [{"conclusion":"failure","databaseId":37570657425,"status":"completed"}]
out    the verification ladder: SUCCESS, every step
out      ladder 1 the solver is a solver        success
out      ladder 2 the element is the element    success
out      ladder 3 the model is the platform     success
out      ladder 6 it stays fixed                success
out      ladder 4 the loads are the loads       success
out      ladder 5 independent confirmation      success
out    lint, unit and guards: FAILURE at `guards and meta-tests` ONLY
out      actionlint success / ruff success / black --check success / mypy success /
out      unit tests success / guards and meta-tests FAILURE
out    CI determinism -- leg / ten legs agree: skipped, no steps -- CK0's
out      workflow_dispatch condition, NOT CK2
```

**A red CI is a HOLD regardless of the local run (CA2) -- except where EG3 carves it out,
and this is that carve-out, traced rather than assumed.**

```
cmd    gh run view 37570657425 --log-failed, every FAILED id, parametrisation stripped,
       counted
out    154 tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
out     20 tests/test_report_carried.py::test_the_report_carries_the_finding
out      7 tests/test_report_guard_states.py::test_the_guard_survives_the_state
out      1 tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number
out      1 tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces
out      1 tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit
rule   EG3 state (2) as corrected by EH1 and R644: the five named, plus
       `test_the_answered_verdict_is_the_NEWEST_one`, plus
       `test_a_carried_row_points_at_a_section_that_discusses_it`, plus the cascade
       identified by a red baseline and each state's own failure line
judge  154 + 20 + 7 + 1 + 1 + 1 = 184, which is the whole list. FOUR of the five named ids
       are present; the seven `test_the_guard_survives_the_state` parametrisations are the
       cascade. NOTHING is red outside the state's own list, so CZ1 (iv) does not fire and
       this is NOT CZ0 (d). The HOLD comes from R706 and R707, not from the suite.
```

**AND EG3 CONDITION (ii), MEASURED BY ME AT THE REPORT'S OWN COMMIT.** State (2) is the half
this milestone kept owing:

```
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
         tests/test_report_guard_states.py -q -p no:randomly    (at bac3017, tree clean)
out    381 passed in 154.16s
cmd    python -m pytest -q -p no:randomly                        (at bac3017, tree clean)
out    3236 passed, 2 warnings in 654.90s
judge  the answering revision clears state (2) in full. The implementer's figure and mine
       agree to the id. This is measured, not inferred, and it is not owed again.
```

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat e76f165..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  NOT a STOP-class finding. Nothing in this range touches what I read or must carry.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py
cmd    git diff --stat e76f165..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (empty)
judge  the instruction's own CI0 check resolves to a real file, and it is unchanged. No new
       or changed conftest, and no plugin the rungs load, so CH2's channel is closed by
       reading rather than by assumption.
cmd    git diff --stat e76f165..HEAD -- floatfea tests docs scripts
out    docs/milestones/F4.md 4 | docs/reports/F4/step-2-answers.json 245 |
       docs/reports/F4/step-2.md 1496 | docs/reviews/F4/step-2.md 780 |
       floatfea/tolerances.py 29 | tests/verification/rung4/test_f4_static_and_mapping.py 142
judge  NOTHING under `floatfea/` moved except `tolerances.py`. There is no (a) in this range
       to find, which is why both my findings are (b) and (c).
```

## 2. R706 -- THE FLOOR IS THE PLATFORM ARM'S AND THE CEILING IS SIXTEEN MEMBERS'

The repair's expected side is right and I verified it at every rung with the shipped
assertion. The **floor** is the half that was derived at one member class.

**First, the domain. `F4_STATIC_REACTION_AGREEMENT` is asserted over all sixteen members.**

```
cmd    sed -n '182,215p' tests/verification/rung4/test_f4_static_and_mapping.py
out    def test_G4_the_tip_shear_equals_the_support_reaction(built: Superstructure) -> None:
out        ... for body in built.bodies: ... for member in body.members:
out            assert float(mf.end_b[2]) == pytest.approx(reaction,
out                                              rel=F4_STATIC_REACTION_AGREEMENT)
out    :210    assert checked == 16, (
judge  sixteen members, and the count is asserted so the domain cannot narrow silently.
       The counter-case injects into ONE of them -- `platform.members[0]`, `:371`.
```

**Then the defect, at every rung, over all sixteen rather than over the one the gate reads.**

```
cmd    python <scratch>/adv_r704b.py   (build_superstructure(measurement_fraction=f) at every
                                        rung; the SAME quantity the counter-case measures,
                                        on every member of every body)
rule   the shipped floor assertion, `:387` -- shortfall > F4_STATIC_REACTION_AGREEMENT_COUNTER
out      f  class      measured worst (min)   closed form         rel err   > floor 0.04?
out   0.75  platform   0.37499999999999983    f/2   = 0.375      4.44e-16   True
out   0.75  hub        0.2647058823529406     6f/17 = 0.2647058  2.10e-15   True
out    0.5  platform   0.2499999999999997     0.25              1.22e-15   True
out    0.5  hub        0.17647058823529396    0.17647058        9.44e-16   True
out    0.4  hub        0.14117647058823465    0.14117647        4.72e-15   True
out    0.3  hub        0.1058823529411758     0.10588235        6.16e-15   True
out    0.2  hub        0.07058823529411748    0.07058823        2.56e-15   True
out    0.1  platform   0.04999999999999985    0.05              7.91e-15   True
out    0.1  hub        0.03529411764705825    0.03529411        1.65e-14   **FALSE**
out
out   rungs/bodies where the declared floor 0.04 is ABOVE the defect it must bracket:
out      f=0.1 hub1: defect=0.03529411764705825   floor=0.04   ratio=0.8824
out      f=0.1 hub2: defect=0.03529411764705865   floor=0.04   ratio=0.8824
out      f=0.1 hub3: defect=0.035294117647058705  floor=0.04   ratio=0.8824
out      f=0.1 hub4: defect=0.03529411764705815   floor=0.04   ratio=0.8824
judge  TWELVE OF SIXTEEN MEMBERS at the ladder's bottom non-vacuous rung, every rung
       `admissible`. The hub closed form is `6f/17` -- the `(12f/17)/2` that
       `_defect_tip_ratio` already carries as `a = 12f/17` -- verified against the solve at
       six rungs, worst disagreement `1.65e-14`.
```

**The boundary, solved in BOTH directions (EH4).**

```
rule   the floor must sit below the defect at every rung, on every member the ceiling reads
out    strengthening side: 6f/17 = 0.04 at f = 17/150 = 0.11333333333333334, so EVERY
out      admissible rung below 0.1134 puts 12 of 16 members under the floor
out    weakening side: the floor may be no higher than 0.03529411764705883 and still
out      bracket f = 0.1's hub arms -- the published 0.04 is already past it, and the
out      honest margin on the twelve hub arms is 0.8824x, not 1.2500x
judge  the entry's "The smallest non-vacuous defect is 0.05 at f = 0.1 and 0.04 sits below
       it with margin 1.2500x" (`floatfea/tolerances.py:2005-2007`) is the PLATFORM ARM's
       figure published as the quantity's. EH4's "defect may shrink to 0.8000 of its size"
       inherits the same domain and is wrong by the same factor.
```

**And the entry contains its own refutation, eighteen lines above the value.**

```
cmd    sed -n '1990,1991p' floatfea/tolerances.py
out    # `0.5/2 = 0.25` and `0.75/2 = 0.375`. C149's correction stands -- the hub arms are
out    # the smaller figure and the platform value is declared because it is the member the
judge  C149 and R697 both say the hub arms are smaller, R697 measured them at 9/34, and the
       floor was derived anyway against the larger class. This is not a missed
       configuration -- it is a configuration named in the same comment block.
```

**What the right repair looks like, and it is already in the file.** `_defect_tip_ratio`
(`tests/verification/rung4/test_f4_static_and_mapping.py:572-597`) does exactly this for the
tip-moment counter: `a = f` on a platform arm, `a = 12f/17` on a hub arm, injected over all
sixteen with `assert checked == 16`. The reaction shortfall is `a/2` with the same `a`. I
checked that the tip-moment floor is NOT affected, which answers the hand-back's first
suspicion directly:

```
cmd    python <scratch>/adv_tip.py   (the SHIPPED `_defect_tip_ratio`, min over all bodies)
rule   the shipped floor assertion, F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.005
out    f=0.75  min 0.056603773584905655  margin 11.3208x
out    f=0.5   min 0.03448275862068966   margin  6.8966x
out    f=0.4   min 0.026666666666666672  margin  5.3333x
out    f=0.3   min 0.019354838709677417  margin  3.8710x
out    f=0.2   min 0.012500000000000004  margin  2.5000x
out    f=0.1   min 0.006060606060606062  margin  1.2121x
judge  **THE TWO FLOORS WERE NOT DERIVED THE SAME WAY AND ONLY ONE IS WRONG.** `0.005` is
       safe on all sixteen at every rung because R694 forced the member-class split into
       the expected side; `0.04` generalised over `f` and not over the member class, and
       those are the same generalisation. The hand-back's hypothesis of a shared systematic
       error is REFUTED -- which is itself the answer, because it means the thing to look
       at is not the arithmetic but which of the two repairs copied the whole shape.
```

## 3. R707 -- DQ4(i) CANNOT FAIL ON THE REMAINDER, AND THE ENTRY'S CLAIM IS THE REVERSE

The hand-back named this suspicion ("both read `body.remainder_mass` and
`body.remainder_node`, so a wrong remainder is on both sides and would cancel ... I have
not stated it anywhere") and did not measure it. It is real, and larger than suspected.

```
cmd    sed -n '1506,1507p' tests/verification/rung4/test_f4_static_and_mapping.py
out        dofs = node_dofs(body.remainder_node)
out        out[dofs[0:3]] += remainder_factor * body.remainder_mass * field
judge  the EXPECTED side reads the same two attributes `body_mass_matrix` reads
       (`floatfea/model/platform.py:718-724`). They cancel.
```

```
cmd    python <scratch>/adv_rem2.py  (the shipped `_dq4_i_departures`, remainder_mass x2)
rule   the shipped ceiling F4_DQ4_RIGID_VECTOR = 1.0e-12
out     f     rem frac   clean                   remainder DOUBLED       caught?
out    0.75   0.2500     (2.484e-16, 5.960e-16)  (1.863e-16, 5.960e-16)  False
out    0.5    0.5000     (9.313e-17, 3.576e-16)  (4.657e-17, 3.576e-16)  False
out    0.4    0.6000     (1.940e-17, 4.470e-16)  (9.701e-18, 4.470e-16)  False
out    0.3    0.7000     (8.315e-18, 5.960e-16)  (4.158e-18, 5.960e-16)  False
out    0.2    0.8000     (7.276e-18, 4.470e-16)  (3.638e-18, 4.470e-16)  False
out    0.1    0.9000     (3.234e-18, 4.470e-16)  (1.617e-18, 4.470e-16)  False
out    0.0    1.0000     RAISED ZeroDivisionError: float division by zero
judge  a mass error of 25% of the body at the shipped rung, and 90% at f = 0.1, reads the
       clean value. **THE BLIND FRACTION GROWS AS THE LADDER DESCENDS** -- the opposite
       direction from the `4i_no_remainder` counter-case, whose own entry says it "gets
       stronger as the ladder descends". That counter-case removes the remainder from `M`
       ALONE, which is an asymmetric injection; it measures that the two sides carry the
       SAME remainder, not that the remainder is right.
```

**And the node, which I did not expect to be blind as well:**

```
cmd    python <scratch>/adv_rem4.py  (remainder lumped at each of the six nodes in turn)
rule   the shipped ceiling, worst over all four `_DQ4_FIELDS`
out    remainder_node -> 0: 5.960464e-16   caught? False
out    remainder_node -> 1: 5.960464e-16   caught? False
out    remainder_node -> 2: 5.960464e-16   caught? False
out    remainder_node -> 3: 5.960464e-16   caught? False
out    remainder_node -> 4: 5.960464e-16   caught? False
out    remainder_node -> 5: 5.960464e-16   caught? False    <- the shipped node
judge  IDENTICAL to every digit at all six. Moving 25% of the body's mass to a different
       node is a wrong DISTRIBUTION, and `floatfea/tolerances.py:2311-2313` says "A mass
       matrix with the right rigid properties and the wrong DISTRIBUTION passes G3.1a and
       fails here." That sentence is the entry's ONLY statement of what this gate adds
       over G3.1a, it is the tolerance's reason for existing, and it is inverted on this
       half of the distribution: G3.1a's CoG comparison catches the node move and this
       gate does not.
```

**The repair is one expression and I measured that it works, so the closing condition is
not a wish.** `body.deck_mass` is on the body, and the construction already computes every
member's `rho A L`:

```
cmd    python <scratch>/adv_rem3.py  (remainder on the EXPECTED side taken as
                                      deck_mass - sum(rho A L), not body.remainder_mass)
rule   the shipped ceiling 1e-12 and the shipped F4_DQ4_RIGID_VECTOR_COUNTER = 5.0e-4
out    f=0.75 remainder x1.000: 2.483527e-16   caught? False   <- clean stays at round-off
out    f=0.75 remainder x1.001: 6.666667e-04   caught? True    <- above the declared counter
out    f=0.75 remainder x2.000: 6.666667e-01   caught? True
out    f=0.1  remainder x1.000: 3.233759e-18   caught? False
out    f=0.1  remainder x1.001: 1.000000e-03   caught? True
out    f=0.1  remainder x2.000: 1.000000e+00   caught? True
judge  the clean case is unaffected (four orders inside the ceiling at both rungs), a 0.1%
       remainder error reaches 6.7e-04 and 1.0e-03, and the ALREADY-DECLARED counter
       `5.0e-4` brackets both. No new apparatus, no new constant, no tolerance move.
```

**The element is fine.** A genuinely wrong `remainder_mass` breaks the body's total mass and
G3.1a's `MASS_PROPERTY_AGREEMENT` comparison against the deck YAML catches it -- the whole
suite is green and this is gate reach, exactly as R705 was. It is (c) and not (a).

## 4. R705 -- CLOSED, AND I REPRODUCED THE ABLATION RATHER THAN READING IT

```
cell   ONE VARIABLE: the two signed lines at `:1591-1592` reverted to
       `abs(abs(f[ra]) - want_m)` in a scratch copy of the tree; nothing else touched
cmd    python -m pytest tests/verification/rung4 -q -p no:randomly -k "DQ4 or DQ5"
out    FAILED ...::test_DQ4_ii_the_closed_form_gate_REDDENS[moment_sign_flipped]
out      Obtained: 5.960464477539063e-16   Expected: 2.0 +- 2.0e-12
out    1 failed, 66 passed, 160 deselected
cmd    python -m pytest tests/verification/rung4 -q -p no:randomly      (whole directory)
out    FAILED ...::test_DQ4_ii_the_closed_form_gate_REDDENS[moment_sign_flipped]
out    1 failed, 226 passed
judge  THE ROW HOLDS THE RULE. Exactly one id goes red under the reversion, it is the
       counter-case the commit added, and the obtained value is the clean one to every
       digit -- the same `5.9605e-16` I measured last round under three mutants of
       `local_mass`. The report's `1 failed, 99 passed` names the same single id under some
       other selection; the count has no stated selection (C11), the id is right in all
       three.
```

**The signs are not fitted, and I checked that independently of the element rather than
accepting the sentence.** The construction's own closed form is `M_A = (L^2/12) e1 x (mu a)`:
for the `xy` plane `e1 x w = x_hat x y_hat = +z_hat`, so `(rz_A, rz_B) = (+1, -1)`; for `xz`,
`x_hat x z_hat = -y_hat`, so `(ry_A, ry_B) = (-1, +1)`. That is `_DQ4_II_PLANES` exactly, and
it is derived from `_independent_nodal_force`'s formula, not read off `local_mass`.

**And the configuration the diff did not choose, since R705 taught that a rung is not the
only one:** the whole scale.

```
cmd    python <scratch>/adv_scale.py   (build_superstructure(froude_lambda=lam))
rule   the shipped ceilings and the shipped sign-flip counter
out    lambda= 50.0: DQ4ii=(2.484e-16,5.960e-16) DQ4i=(1.774e-16,5.109e-16) signflip=2.000000
out    lambda= 30.0: DQ4ii=(1.437e-16,3.449e-16) DQ4i=(5.133e-17,3.285e-16) signflip=2.000000
out    lambda=100.0: DQ4ii=(2.484e-16,8.345e-16) DQ4i=(1.774e-16,6.812e-16) signflip=2.000000
out    lambda=150.0: DQ4ii=(1.472e-16,3.768e-16) DQ4i=(2.102e-16,4.037e-16) signflip=2.000000
out    at lambda = 1 and lambda = 5000 the BUILDER REFUSES -- "L/D = 0.400 is below 2" and
out    "L/r = 607.7 exceeds 300, the slenderness ceiling. Refused rather than analysed."
judge  the clean gates are scale-invariant, the sign counter is exactly 2.0 at every scale,
       and the unsupported scales RAISE rather than defaulting. R705's repair survives the
       probe. The refusals are the right behaviour and I record them as such.
```

**The third named site is closed in its own commit (`b68f2f7`) and the self-correction is
honest.** The docstring now carries `2.796036563614433e-15` -> `3.140164140674671e-15`
instead of the word "unmoved", and I reproduce the second figure exactly: it is what my own
node-A-flip harness reads. The hand-back flagged its own first wording and the fix is in the
file rather than in the report.

## 5. THE HAND-BACK'S OTHER TWO SUSPICIONS, RULED

* **Section 11a's 154 `no change` rows: SORTED CORRECTLY, no mis-filed row found.** I read
  every non-bulk row. The four substantive ones are accurate: `tolerances.py:2239-2257` is
  genuinely the branch not taken and saying so is right; `tolerances.py:1988-1989` and
  `model/platform.py:116` were cited by me as already-correct and are; `test...py:355` and
  `:1511-1515` are unchanged context inside rewritten blocks, which is true of the file.
  The bulk rows for R686, R687 and R688 all resolve to verdict 98 and this range does not
  reach them. **The hatch is doing what it was built to do and I have nothing to add.**
* **DQ4(i) against a defect identical on every body: NOT a gap for DQ4(i).** Its expected
  side is per-node and independent of `M`, so a uniform `mass_scale` is caught --
  `1.0000000000005215e-03` at every rung, which is the shipped counter-case. The per-body
  `max` blindness I noted last round is the MAPPING gate's and is already on the 28 October
  corpus target list. **The real blindness on DQ4(i) is the remainder, which is R707**, and
  it is a different mechanism: not a max over bodies, but a shared value inside one body.

## Findings

**R706. (b, BLOCKING) `F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.04` IS THE PLATFORM ARM'S
FLOOR PUBLISHED AS THE QUANTITY'S, AND IT SITS ABOVE THE DEFECT ON 12 OF 16 MEMBERS AT
`f = 0.1`.** `floatfea/tolerances.py:2020` (the value) and `:2005-2007` (the "smallest
non-vacuous defect is 0.05 ... margin 1.2500x ... may shrink to 0.8000" justification);
`tests/verification/rung4/test_f4_static_and_mapping.py:387-391` (the floor assertion),
whose ceiling `F4_STATIC_REACTION_AGREEMENT` is asserted over all sixteen members at
`:182-215` with `assert checked == 16`. Measured in section 2: the hub-arm shortfall is
`6f/17` (verified against the solve at six rungs, worst disagreement `1.65e-14`) and reads
`0.03529411764705815` at `f = 0.1` against a floor of `0.04` -- ratio `0.8824`, on all
twelve hub arms, every rung `admissible`. Boundary solved both ways: `6f/17 = 0.04` at
`f = 17/150 = 0.11333333333333334`, and the floor may be no higher than
`0.03529411764705883` to bracket. The entry's own `:1990` already says "the hub arms are
the smaller figure". **This is R682's and R694's finding for the fourth time in this block,
and the tip-moment counter `0.005` is NOT affected** -- it is safe on all sixteen at every
rung, `1.2121x` at worst, because R694 forced the member-class split into its expected side.
**Closed when** the floor sits below the defect on all sixteen members at every admissible
rung, measured and pasted, **or** the counter-case injects over all sixteen against the
closed form at each body's own class -- `f/2` on a platform arm, `6f/17` on a hub arm, the
same `a` `_defect_tip_ratio` already computes -- in that helper's shape with
`assert checked == 16`, **or** the entry states that the declared figure is the platform
arm's alone, quotes the hub figure beside it, and names what brackets the twelve. No new
apparatus either way: `a = 12f/17` is already in the tree eighteen lines from the value.

**R707. (c, BLOCKING) DQ4(i) CANNOT FAIL ON THE REMAINDER MASS OR ON THE REMAINDER NODE,
AND THE ENTRY'S ONLY STATEMENT OF WHAT THE GATE ADDS OVER G3.1a IS INVERTED ON EXACTLY
THAT HALF.** `tests/verification/rung4/test_f4_static_and_mapping.py:1506-1507`
(`_independent_nodal_force` reading `body.remainder_node` and `body.remainder_mass`, the
two attributes `body_mass_matrix` reads at `floatfea/model/platform.py:718-724`), against
`floatfea/tolerances.py:2311-2313` ("A mass matrix with the right rigid properties and the
wrong DISTRIBUTION passes G3.1a and fails here") and `:2310` ("a route that never touches
`M`, `local_mass` or the element transform"), and `docs/milestones/F4.md:431` (the gate
row's `# expected:` source, "the construction (node coordinates and line mass only, never
`M`)"). Measured in section 3: a **doubled** remainder mass reads the clean value to every
digit at every rung, and the remainder lumped at **any of the six nodes** reads an identical
`5.960464e-16`. The unconstrained fraction of the body's mass is `0.25` at `f = 0.75` and
`0.90` at `f = 0.1`, growing as the ladder descends -- the opposite direction from the
`4i_no_remainder` counter-case, which removes the remainder from `M` alone and therefore
measures that the two sides agree rather than that either is right. **The element is fine**
(G3.1a's mass and CoG comparison catches a wrong remainder, the whole suite is green), so
this is the gate's reach and not a defect in `floatfea/`, exactly as R705 was.
**Closed when** the expected side's remainder comes from a source `M` does not read --
`body.deck_mass` minus the construction's own `sum(rho A L)` is one expression and I
measured it: clean stays at `2.483527e-16` / `3.233759e-18`, a 0.1% remainder error reaches
`6.666667e-04` and `1.000000e-03`, and the already-declared `F4_DQ4_RIGID_VECTOR_COUNTER =
5.0e-4` brackets both -- **or** `floatfea/tolerances.py:2310-2313` and
`docs/milestones/F4.md:431` state the unconstrained fraction per rung and name the gate
that covers it, with the "wrong DISTRIBUTION" sentence corrected or withdrawn. No new
apparatus either way.

## Closure items

Fixed once, in the step's closure commit. **Not re-reviewed item by item, and the step is
not held on one.** C1 to C7 from verdict 101 carry unchanged and are NOT re-adjudicated.

**C8. The direction argument in report section 12 is false of a floor.** "a counter moving
DOWN makes the gate demand more of the defect, not less" -- for `shortfall > floor`,
lowering the floor demands LESS. Both moves ARE net strengthenings, but because of the
closed-form equality that replaced a frozen constant, not because the constant went down.
**Closed when** the `rule` line says which assertion got harder and why.

**C9. `_dq4_i_departures` divides by `max|want[m_idx]|` with no guard.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1618`. At `f = 0` -- a rung of
`MASS_FRACTION_LADDER`, `admissible` -- it raises a bare `ZeroDivisionError`. It raises
rather than defaulting, which is the right half; the message says nothing. **Closed when**
the vacuous rung raises with its reason named, as the R704 repair's own skip does.

**C10. A published `f` label is wrong by rounding.**
`tests/verification/rung3/test_platform_skeleton.py:621` prints `f {mass_fraction:.1f}`, so
the shipped `0.75` prints as `f 0.8` beside every `rho_eq` row -- and ES1 asks for `rho_eq`
per body, so this print is the deliverable. Captured in my own run's output.
**Closed when** the format carries the value.

**C11. The ablation count has no stated selection.** Report section 3 and
`test_f4_static_and_mapping.py:1481-1484` say `1 failed, 99 passed`. I get `1 failed,
66 passed` under `-k "DQ4 or DQ5"` and `1 failed, 226 passed` over the whole rung4
directory. The FAILED id is identical in all three and the claim holds; the number does not
identify its run. **Closed when** the figure names the selection, or quotes a count I can
reproduce.

**C12. Three cited scripts are not in the tree.** Report sections 2 and 3 cite
`scratchpad/verify_r704_r705.py`, `scratchpad/r704_r705.py` and
`scratchpad/verify_r705_docstring.py`. Same reproducibility class as R700. **Closed when**
the figures are produced by something committed, or the citation says it is not.

**C13. `docs/reports/F4/step-2.md:3` still says `Answers: verdict 96 @ 5786bed`.** Revision
2's own header at `:719` is correct and is the one the guard reads -- verified mechanically,
section 0 -- so nothing is broken. A later reader opening the file sees the stale line
first. **Closed when** the top line tracks the newest revision, or says it is the first
revision's.

**C14. "Measured on every element of all five bodies, not assumed" is a measurement that
cannot vary.** `tests/verification/rung4/test_f4_static_and_mapping.py:1548-1551`.
`local_mass(section, material, length)` takes no orientation, so the sign pattern cannot
differ between elements -- the sweep varies `L` and `mu`, neither of which can move a sign.
Nothing false shipped: the signs ARE independently derivable and I derived them (section 4).
**Closed when** the sentence says what the sweep varied, or cites the derivation instead of
the sweep.

**C15. R697 is still open and R706 is now its consequence.**
`floatfea/tolerances.py:1988-1989` still generalises `f/2` to every member; the floor
derived from that generalisation is R706. Recorded so the closure commit fixes the sentence
and the gate in one place rather than twice.

## Tolerances touched

```
cmd    git diff e76f165..HEAD -- floatfea/tolerances.py, non-comment changed lines only
out    -F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.375
out    +F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.04
judge  ONE value moved in this range, and it is a counter. NO CEILING MOVED ANYWHERE IN THE
       TREE, and the value is not in the same commit as code it rescues -- `floatfea/`
       carries no change in this range except this file. The report's section 12 correctly
       reports TWO, because its own range reaches back to `30e4395`; mine is
       `e76f165..HEAD` and the tip-moment move is behind it, already ruled at verdict 101.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.375` | `0.04` | dimensionless, relative; form changed from a frozen constant compared by EQUALITY to (closed-form equality at the body's own `f`) + (a floor) | IS the counter; injected by `test_G4_the_defective_formula_misses_the_reaction_by_f_over_two` at `tests/.../test_f4_static_and_mapping.py:371`, ONE member of the sixteen the ceiling reads | `floatfea/tolerances.py:1996-2019`; plan row `docs/milestones/F4.md:473` | **THE EXPECTED SIDE IS CLOSED AND CORRECT. THE FLOOR IS R706 AND BLOCKS.** The `f/2` read from `body.mass_fraction` is right and EA4-clean (an input, not a response), and I reproduced all six rungs to within `7.9e-15` relative; the `f = 0` skip names its reason and the gate genuinely has no defect to inject there. **But the floor is the platform arm's and the ceiling is sixteen members'**: `0.03529411764705825` on the hub arms at `f = 0.1` against a declared `0.04`, ratio `0.8824`, boundary at `f = 17/150`. The published `1.2500x` and `0.8000` shrink are both the platform arm's figures. **This is the same generalisation the tip-moment repair made and this one did not** -- over `f` but not over the member class, which are one thing. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.005` | `0.005`, unmoved | dimensionless, relative; a floor under a closed form | `_defect_tip_ratio(body)`, `a = f` platform / `a = 12f/17` hub, over all 16 with `assert checked == 16` | `floatfea/tolerances.py:2016-2069` | **RE-VERIFIED AT THE HAND-BACK'S REQUEST AND SAFE.** It asked whether the two floors share a systematic error. They do not: measured over all bodies at every rung, the min runs `0.056603773584905655` down to `0.006060606060606062`, margin `11.3208x` to `1.2121x`, never below the floor. **Do not move it.** |
| `F4_DQ4_RIGID_VECTOR` / `_COUNTER` | `1.0e-12` / `5.0e-4` | unmoved | dimensionless, relative | the small injection (`mass_scale=1.001`) and `drop_remainder` | `floatfea/tolerances.py:2304-2344`; plan rows `docs/milestones/F4.md:431`, `:484-485` | **VALUE AND FORM STAND; THE QUANTITY'S REACH IS R707 AND BLOCKS.** The ceiling, the clean figure and the counter's `2.0000x` margin all reproduce and I accepted them last round. What I did not test then is the remainder: the gate reads an identical value with the remainder mass DOUBLED and with it lumped at any of the six nodes, and the entry's own "wrong DISTRIBUTION ... fails here" sentence is inverted on that half. **No value needs to move** -- the already-declared `5.0e-4` brackets a 0.1% remainder error once the expected side stops sharing it. |
| `F4_DQ4_ELEMENT_VECTOR` / `_COUNTER` | `1.0e-12` / `5.0e-4` | unmoved | dimensionless, relative; moment channel now SIGNED | three injections, the third R705's sign flip at exactly `2.0` on the moment channel with the force channel asserted at round-off | `floatfea/tolerances.py:2239-2301`; plan rows `docs/milestones/F4.md:432`, `:482-483` | **R705 CLOSED, AND THE COUNTER-CASE IS WHAT CLOSES IT.** The signed comparison is correct and the signs are independently derivable from `(L^2/12) e1 x w` -- I derived both planes rather than accepting the "measured on every element" sentence, which cannot vary (C14). The shipped `[moment_sign_flipped]` row holds the rule: reverting the two lines gives exactly one red, the right id, at the clean value `5.9605e-16`. Asserting the force channel stays at round-off under a sign-only injection is the right second half, because it distinguishes "the injection is the one R705 names" from "something moved". Scale-invariant at four values of `froude_lambda`. |
| `F4_DQ5_FREE_FALL` / `_COUNTER` | `1.0e-12` / `4.0e-4` | unmoved | dimensionless, relative | two injections reddening different channels | `floatfea/tolerances.py:2345-2383` | **UNCHANGED AND ACCEPTED**, as at verdict 101. C2 remains the one closure item on it. R707's remainder sharing reaches DQ5's applied load too -- the remainder is on both the load and `M` -- but DQ5's assertion is free fall (`a = g`, member forces zero), which a consistent wrong remainder genuinely does satisfy, so there is nothing to catch there and I do not extend R707 to it. |
| G4.1 dynamic (DQ8) | -- | **none declared** | -- | -- | `scripts/report_joint_reactions.py:217-247`; plan row `docs/milestones/F4.md:435` | **THE REFUSAL IS STILL CORRECT AND IS STILL NOT A BLOCKING OMISSION.** I ruled this at verdict 101 and nothing in this range changes the input. C1 is its closure item and lands before the quantity is chosen. The hand-back is right not to re-ask. |

## Carried

Verdict 101 (`4b8f079`, judging `e76f165`) left **two blocking findings, two items carried
by name, one deferred, and seven closure items plus C1 to C7.** Every one, with status.

* **R704 (blocking) -- ANSWERED IN FORM, AND ITS REPAIR CARRIES A NEW BLOCKING FINDING.**
  The expected side is now `f/2` at the body's own `f` read from `body.mass_fraction`, which
  is the first branch my condition offered and the right one; I reproduced all six rungs.
  **R704 itself does not carry further.** What carries is **R706**: the floor the repair
  declared is the platform arm's and the ceiling is sixteen members'. That is not the same
  item restated -- R704 was about `f`, R706 is about the member class -- but it is the same
  *shape*, and it is the fourth time in this block.
* **R705 (blocking) -- CLOSED, at all three named sites, and the ablation reproduces.**
  Section 4. The signed comparison, a shipped counter-case that goes red alone when the
  `abs` returns, and the docstring sentence withdrawn in its own commit with the
  self-correction (`2.796e-15` -> `3.140e-15`, not "unmoved") carried in the file. The third
  site being a separate commit rather than a line claimed covered by the first is the
  discipline the last six rounds have been asking for. **Does not carry.**
* **R682 -- CLOSED and does not carry**, as ruled at verdict 101.
* **R691 -- CLOSED at the fifth-missed site**, as ruled at verdict 101. Section 11a's rows
  declare the remaining declaration-only sites by name and they are accurate.
* **R685 -- CLOSED at verdict 101 and it stays closed.** No hunk in this range touches
  `F4_MAPPING_CONSERVATION`'s entry.
* **R695, R696, R698 -- CLOSED at verdict 101, unchanged in this range.**
* **R697, R699 to R703 (closure) -- carried unchanged as closure items and NOT
  re-adjudicated**, per verdict 101's own instruction. **R697 is now load-bearing**: the
  unqualified `f/2` sentence at `floatfea/tolerances.py:1988-1989` is the sentence the R706
  floor was derived from, so the closure commit fixes the prose and the gate in one place.
  Recorded as C15; **R706 is the blocking half and it is in Findings, not here.**
* **C1 to C7 (closure) -- carried unchanged.** C7's `136`/`108`-versus-`135`/`107`
  discrepancy: the report traces it to a working tree rather than a commit and that account
  is correct. My run and CI agree at this commit (184 ids, section 0), so the figure now
  comes from its own run and C7 is answered in substance; it stays on the closure list only
  as a record.
* **Verdict 101's "WHAT I WILL NOT ACCEPT" -- HONOURED on its own terms, and I say so.** The
  shape named was "a closing condition that names two entries, reported answered after one".
  Both of R705's three sites and R704's one are answered, section 11a declares every
  untouched site by name including the branch deliberately not taken, and the implementer
  reported three errors of its own before I found them. **The sixth repetition did not
  become a seventh.** R706 is a different failure -- a derivation whose domain was narrower
  than the ceiling's -- and I record that distinction rather than filing it under the old
  heading.
* **The `0.05` versus `0.005` suspicion the hand-back raised -- MEASURED AND REFUTED**,
  section 2. The two floors were not derived the same way and only one is wrong.

## The adversarial corpus (BE3)

**NO BATCH THIS ROUND, and it is EG4(e) rather than an omission.** Batches pause until
28 October except mutation work on **F4's load-mapping gate** and **EB6's label-provenance
gate**. This round's surfaces are the static reaction counter and the DQ4/DQ5 gates --
neither exception -- so the round went into mutation measurement instead of a file.

* **New entries in `tests/corpus/` this round: 0.** `tests/corpus/` is unchanged by me:
  nothing added, nothing carried. Previous batch: 36, at `4f99c7f`. **No coverage number**,
  and I will not publish one off a batch I did not run.
* **What the mutation work bought instead, stated so the spend is visible.** Both blocking
  findings came from running the model at a configuration the diff did not choose, and
  neither from reading the diff: **R706** from evaluating the counter-case's own quantity on
  the twelve members the gate does not read, at the rung the diff did not choose; **R707**
  from mutating two attributes nothing in the diff mentions. **That is the third round
  running where EU1's adversarial case is where the finding was, and the second where
  inverting EH4's direction -- solving for how far the DEFECT may shrink rather than how far
  the ceiling may rise -- is what exposed it.** Boundaries solved both ways this round:
  `6f/17 = 0.04` at `f = 17/150` (strengthening) and the floor's maximum admissible value
  `0.03529411764705883` (weakening); and the remainder-error detection threshold under the
  repaired expected side (`6.666667e-04` at `f = 0.75`, `1.000000e-03` at `f = 0.1`) against
  the declared `5.0e-4`.
* **Coverage, honestly.** Of the two blocking findings, **neither** is a shape a check in
  the tree looks for. R706 would be caught by one loop -- the counter-case's quantity over
  the ceiling's own member set at every rung -- and that loop is what `_defect_tip_ratio`'s
  gate already is for the other counter, so the tree contains the pattern and not the
  instance. R707 is a shared-value shape nothing here scans for.
* **The 28 October batch's targets, unchanged and still owed:** F4's load-mapping gate (a
  defect identical on all five bodies; a block moved between two nodes at the same position)
  and EB6's label-provenance gate per C5 (permutations that PRESERVE the count). **Added by
  this round:** a shared-attribute corpus for DQ4(i) -- every attribute both
  `_independent_nodal_force` and `body_mass_matrix` read, one entry each, which is the R707
  shape generalised.
* **Corpus hygiene note on my own files, carried from verdict 101 and still mine to fix:**
  `tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48, 49 and 50 carry
  `measured=` figures on the OLD mass basis. I will re-head that file at the 28 October
  batch.

## Next step opens when

**STEP 2 STAYS OPEN. THIS WAS ROUND 2 OF THREE; ONE REVISION REMAINS AND IT IS THE CLOSER.**
Step 3 does not begin. At the next revision the step closes under CZ0 whatever the verdict,
and any blocking item still open carries by name into step 3's `Carried` and blocks there.

**Answered before anything else, and only these two block:**

1. **R706** -- `floatfea/tolerances.py:2020` and `:2005-2007`, and
   `tests/verification/rung4/test_f4_static_and_mapping.py:387-391`. **My figures to beat:**
   hub-arm shortfall `6f/17`, verified against the solve at six rungs to `1.65e-14`;
   `0.03529411764705825` / `0.03529411764705865` / `0.035294117647058705` /
   `0.03529411764705815` on hub1 to hub4 at `f = 0.1`, every one `admissible`, ratio to the
   declared floor `0.8824`; boundary `f = 17/150 = 0.11333333333333334`; the floor's maximum
   admissible value `0.03529411764705883`. The closed form is `a/2` with the same `a`
   `_defect_tip_ratio` already computes.
2. **R707** -- `tests/verification/rung4/test_f4_static_and_mapping.py:1506-1507`, with
   `floatfea/tolerances.py:2310-2313` and `docs/milestones/F4.md:431`. **My figures to
   beat:** the remainder mass doubled reads the clean value to every digit at all six
   non-vacuous rungs; the remainder at any of the six nodes reads an identical
   `5.960464e-16`; the unconstrained fraction is `0.25` at `f = 0.75` and `0.90` at
   `f = 0.1`; with the remainder taken from `deck_mass - sum(rho A L)` the clean case is
   `2.483527e-16` / `3.233759e-18` and a 0.1% error reads `6.666667e-04` / `1.000000e-03`,
   inside the already-declared `5.0e-4`.

**Nothing else blocks.** R705, R682, R691, R685, R695, R696 and R698 are closed; no ceiling
moved; the one counter that moved is accepted in form and blocked only on its domain; the
refusal to declare a G4.1-dynamic tolerance is still correct. **C1 to C15 are closure
class** -- one list, one commit, do not spend a round on them and do not hold the step on
one -- **except that C1 is still answered before the G4.1-dynamic quantity is chosen**,
because that choice is (c) and C1 is its input, **and C15 travels with R706's repair**
because they are the same sentence.

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION, which is the last one.** A counter whose
domain is narrower than the domain of the ceiling it brackets, with the narrowness unstated.
R706 is the fourth instance in this one block -- R682, R694, R704, R706 -- and the first
where the narrow dimension was the MEMBER CLASS rather than the mass fraction. The command
that settles it is one loop: evaluate the counter-case's own quantity on **every member the
ceiling reads**, at **every admissible rung**, and paste the minimum. The repair for the
other counter in the same file is that loop already. And a gate whose expected side shares a
value with the measured side: R707's remainder is the second time this milestone that an
"independent" construction turned out to read an attribute from the object under test, and
the question that finds it is cheap -- for every attribute the expected side reads, mutate it
and see whether the gate moves.

## On the schedule

The report's one hand-written paragraph says the schedule holds and I see nothing in this
range to contradict it. Both my findings are one expression each in one file, and both closed
forms are already in the tree. **Working targets F4 14 Oct, table 17 Oct, code-check 22 Oct;
committed dates unchanged.** The thing I would watch is unchanged from verdict 101 and is not
these two findings: **G4.1 dynamic and G4.5 both wait on the six FloatSim re-runs and now
also on a plan decision about DQ8's quantity**, and the next revision is the last one in
which step 2's work gets read in full. If that decision needs the plan reopened rather than a
sentence, say so the day it is known under DZ7c -- reduce scope, do not slip. **Two
consecutive steps closing while carrying is the escalation CZ0 names**, and this step closing
with R706 or R707 open would be the first of those two, not the second.

## On the criterion -- I was asked, and I agree with it

Both blocking findings are (b) and (c), nothing prose went into Findings, and eight items
that would have been blocking heads six rounds ago went to the closure list without argument
-- including a false directional argument about a tolerance move (C8) and a published figure
label wrong by rounding (C10). **ES0 and EU1 earned themselves again.** Neither finding came
from reading the diff: the diff is clean, candid, self-correcting, and names three of its own
errors before I did. R706 came from evaluating a shipped assertion's quantity on members the
assertion does not read; R707 from mutating two attributes the diff never mentions.

**One note on the EU1 wording question, said once and not re-argued.** Verdict 101 observed
that EU1's "at least every admissible ladder rung" is narrower than its own first phrase,
"the model run at a configuration the diff did not choose", and recommended leaving the
wording and reading it the general way. This round is evidence for that reading rather than
against it: the configurations that found things were **a member class** (R706) and **two
attributes** (R707), and only R706 involved a rung at all. The hand-back asks whether it
should be written down. **My answer is still no, and the reason is a measurement rather than
a preference:** a clause enumerating configurations would have had to name "member class" and
"shared attribute" in advance, and whoever wrote it would have been the same person whose
corpus the enumeration came from -- which is the defect BE3 exists for. The general phrase is
the one that keeps working. That goes to Xabier through the implementer as a reading, not as
a round.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: e76f16507966e7404e7daec92fd2fe917af0b9ef
Verdict: HOLD

**Reviewed commit: `e76f165`** (HEAD of F3, pushed, tree clean).
Tests: **135 failed, 3057 passed, 0 skipped** (MY OWN run, ONE invocation, no `--ignore`,
no `-k`, no deselection, in the repository itself, 673.58s. All 135 are EG3 state (2) and
each is traced by name in section 2. **The hand-back's `136`/`108` is off by one: my run
and CI both say 135, with 107 on the named-site guard, and the id sets are IDENTICAL.**)

## Round of 2026-10-06 -- ES0 INTERIM CHECK + EU1. Counts against NO round.

**ES0's premise verified before anything else, because the exemption rests on it.**

```
claim  there is no new report revision -- the report is still the one verdict 97 judged
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-2.md
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), and a red
       I shipped
judge  7cee09f is the commit verdict 97 judged. The report has not moved across verdicts
       98, 99, 100 or this one. This counts against no round, verdict 97 remains round 1
       of three, and TWO REVISIONS REMAIN.
```

Instruction 1b does not fire, on the same ground verdicts 98, 99 and 100 gave and
unchanged: the report's `Answers: verdict 96 @ 5786bed` names the verdict the report was
written to answer, and a report that PREDATES the newest verdict with no revision between
them is EG3 state (2), not a report answering a superseded round.

**AND THE HAND-BACK'S RANGE IS WRONG, WHICH MATTERS BECAUSE OF WHAT IT EXCLUDES.** It says
`fa709df..HEAD` is four commits and that `30e4395` -- the commit answering verdict 100's
three blocking items -- is outside it.

```
cmd    git rev-list --count fa709df..HEAD
out    6
cmd    git log --oneline fa709df..HEAD
out    e76f165 / 1297804 / da7c25b / ad77a69 / 30e4395 / 6703575
cmd    git merge-base --is-ancestor 30e4395 fa709df && echo yes || echo NO
out    NO    <- so 30e4395 IS in fa709df..HEAD
cmd    git log --oneline -1 -- docs/reviews/F4/step-2.md
out    6703575 review: ... HOLD @ fa709df
judge  30e4395 is INSIDE my range and NO verdict has ever read it. Verdict 100 judged
       fa709df; 30e4395 came after it. So R694, R695 and R696 are not "already answered"
       -- this check is the FIRST reading of their repair, and the first thing I check is
       the previous verdict's gated items. I reviewed 30e4395 in full.
```

**HOLD, TWO BLOCKING ITEMS.** The larger is a carried one: **R694 was answered on one of
its two entries.** The tip-moment half got a real repair -- the closed form in the gate,
the constant demoted to a floor -- and I reproduced it at every rung. The reaction half did
not: `F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375` is still asserted by EQUALITY against a
frozen constant, and verdict 100's own closing condition said "both entries" and "the gate
no longer compares a frozen constant to a quantity that moves with a model parameter the
model may change by itself". Measured: false at every rung below `0.75`. Sixth appearance
of the half-of-an-item shape and the first on a carried gate rather than a sentence.

The second is mine, from EU1's adversarial case applied to the new gates: **DQ4(ii)'s
moment channel cannot fail on a sign**, and the plan declares its quantity with the sign in
two places.

**No STOP.** The ladder is SUCCESS at every step in CI at the reviewed commit, no low rung
is red, and `.claude`/`docs/SUPERVISOR.md`/`CLAUDE.md` moved only in a standalone
`process:` commit. Sections 0 and 1.

## 0. CI AT THE REVIEWED COMMIT -- RED, AND THE RED IS THE STEP'S OWN BOUNDARY

```
cmd    gh run list --commit e76f16507966e7404e7daec92fd2fe917af0b9ef --json
         name,conclusion,workflowName,status
out    [{"conclusion":"failure","databaseId":37566586915,"status":"completed",
         "workflowName":"CI"}]
judge  completed, so it is not "a run that has not finished". NOT CK2: both real jobs have
       13 steps with real durations and ran 3 and 6 minutes; runner_name reads null
       through this gh version for every job including the two that plainly ran, so I used
       the steps and the durations as the discriminator and not that field. No payment or
       spending-limit annotation. The two `CI determinism` jobs are skipped with no steps
       -- CK0's workflow_dispatch condition, not CK2.
```

```
the verification ladder: SUCCESS, every step
  ladder 1 the solver is a solver        success
  ladder 2 the element is the element    success
  ladder 3 the model is the platform     success
  ladder 6 it stays fixed                success
  ladder 4 the loads are the loads       success
  ladder 5 independent confirmation      success
lint, unit and guards: FAILURE at `guards and meta-tests` ONLY
  actionlint success / ruff success / black --check success / mypy success /
  unit tests success / guards and meta-tests FAILURE
  135 failed, 992 passed, 1 warning in 369.98s
```

**A red CI is a HOLD regardless of the local run (CA2) -- except where EG3 carves it out,
and this is that carve-out, measured rather than assumed.** Section 2 traces all 135 by
name to EG3 state (2). Nothing is red outside the state's own list, so CZ1 (iv) does not
fire and **this is NOT CZ0 (d)**. The HOLD comes from R704 and R705, not from the suite.

I ran the lint gates myself at `e76f165`, tree clean:

```
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests
out    All done! 98 files would be left unchanged.
cmd    python -m mypy floatfea
out    Success: no issues found in 36 source files
```

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat fa709df..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    CLAUDE.md 33 +++ / docs/SUPERVISOR.md 33 +++   (66 insertions, 0 deletions)
cmd    git log --oneline fa709df..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    ad77a69 process: EU1 -- an interim check that moves a tolerance value gets the
       adversarial case
cmd    git show --name-only --format= ad77a69
out    CLAUDE.md
out    docs/SUPERVISOR.md
judge  ONE commit, standalone, `process:` prefix, cites EU1 in its first line, touches
       NEITHER floatfea/ NOR tests/. Purely additive -- I read both hunks line by line and
       NO GUARD IS REMOVED OR WEAKENED. The inserted clause is byte-identical to the EU1
       text in my own invocation. No STOP-class finding here.
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py            <- non-empty, so the pathspec is the CI0 one
cmd    git diff fa709df..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty). No conftest changed, no new plugin, no hookwrapper. CH2 clear, so the
       rung greens in section 0 are believable.
cmd    git diff --stat fa709df..HEAD -- tests/
out    tests/verification/rung4/test_f4_static_and_mapping.py | 569 ++++--
       ONE test file. Nothing under tests/ outside it.
```

## 2. THE 135 REDS, EACH TRACED BY NAME (EG3(i), CA2, R644)

| count | id | on EH1/EJ2's **state (2)** list as |
|---|---|---|
| 107 | `test_every_named_site_is_touched_or_declared[...]` | named, state (2) |
| 18 | `test_the_report_carries_the_finding[...]` | named, state (2) |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | named, state (2) |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | named, state (2) |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | named, state (2) |
| 1 | `test_the_guard_survives_the_state[baseline]` | the red baseline |
| 6 | the six planted states | the cascade, by failure line |

107+18+1+1+1+1+6 = 135.

**CI's 135 and my 135 are the SAME IDS, not the same count** -- the only form of that claim
worth making on a different OS and a different libm:

```
cmd    gh run view 37566586915 --log-failed | grep -oE "FAILED tests/[^ ]+" | sort -u > ci
cmd    python -m pytest -q -rf | grep -oE "^FAILED tests/[^ ]+" | sort -u > local
cmd    diff ci local
out    (empty). IDENTICAL, 135 lines each.
```

**The cascade is identified by each state's OWN failure line, individually (R644):**

```
cmd    python -m pytest tests/test_report_guard_states.py -q -p no:randomly
         | grep -E "^E +AssertionError" | sort | uniq -c
out    1 baseline: expected a clean run.
out    1 draft_suffix_beside_a_step_report: ... must be stepped over, not reacted to.
out    1 non_numeric_step_suffix:           ... must be stepped over, not reacted to.
out    1 step_number_is_the_empty_string:   ... must be stepped over, not reacted to.
out    1 superscript_digit_step_number:     ... must be stepped over, not reacted to.
out    1 verdict_amended_after_the_commit_the_report_answers: expected a clean run.
out    1 zero_padded_step_number:           ... must be stepped over, not reacted to.
judge  seven distinct lines, the same seven verdicts 99 and 100 recorded. Each nested run
       pastes a dirty baseline carrying the state (2) ids; six states assert against a
       clean baseline and the baseline is dirty.
cmd    grep -c "test_the_guard_reads_the_step_being_worked_on" local
out    0    <- ABSENT, so state (1) is clear and this is unambiguously state (2)
```

**`test_the_answered_verdict_is_the_NEWEST_one` and
`test_a_carried_row_points_at_a_section_that_discusses_it` are both GREEN**, which EJ2 put
on state (2)'s list. I record that rather than assuming they must be red: the state's list
is the set a red is ALLOWED to be in, not a set that must be full.

## 3. R704 -- THE BLOCKING ONE. R694 WAS CLOSED ON ONE OF ITS TWO ENTRIES

Verdict 100's R694 named two counters and its `Closed when` said **both**. I ran the
ladder, which is what EU1 exists for, with the SHIPPED assertions and nothing of my own:

```
cmd    python <scratch>/adv1.py   (build_superstructure(measurement_fraction=f) at every
                                   rung of MASS_FRACTION_LADDER; the two shipped
                                   assertions evaluated by their own rule)
rule   the shipped assertions. (i) test_f4_static_and_mapping.py:350-356 --
       shortfall == approx(F4_STATIC_REACTION_AGREEMENT_COUNTER, rel=1e-12);
       (ii) :640-651 -- ratio == approx(_defect_tip_ratio(body), rel=1e-12) AND
       ratio > F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER, over all 16 members
out      f  adm   shortfall(plat[0])     ==0.375?   min tip/root         >floor?  cf ok?
out   0.75 True   0.37500000000000006    True       0.0566037735849053   True     True
out    0.5 True   0.25000000000000017    FALSE      0.03448275862068926  True     True
out    0.4 True   0.2000000000000001     FALSE      0.02666666666666618  True     True
out    0.3 True   0.15000000000000022    FALSE      0.01935483870967727  True     True
out    0.2 True   0.10000000000000019    FALSE      0.01249999999999982  True     True
out    0.1 True   0.0500000000000004     FALSE      0.006060606060605793 True     True
out    0.0 True   6.075906704932774e-16  FALSE      (vacuous; the gate skips it)
```

**THE TIP-MOMENT HALF IS CLOSED AND THE REPAIR IS THE RIGHT SHAPE.** `_defect_tip_ratio`
(`tests/verification/rung4/test_f4_static_and_mapping.py:572-597`) puts the closed form
`a/(12-5a)` with `a = f` on a platform arm and `a = 12f/17` on a hub arm on the EXPECTED
side, at each body's OWN `f`, and `0.005` is a floor under every rung. I verified the closed
form against the solve on all 16 members at all six non-vacuous rungs (`cf ok? True`
throughout, `rel=1e-12`) and the floor at every one. `f = 0` is genuinely vacuous --
`_defect_tip_ratio` returns exactly `0.0`, and the gate's `continue` sits BEFORE the
assertions and AFTER `checked += 1`, so `assert checked == 16` still binds and an empty
collection is still an error, not a silent skip. This is precisely the shape EU1's last
paragraph prescribes, and it is what I asked for.

**THE REACTION HALF IS NOT.** `tests/verification/rung4/test_f4_static_and_mapping.py:350-356`
still reads

```
assert shortfall == pytest.approx(
    F4_STATIC_REACTION_AGREEMENT_COUNTER, rel=F4_STATIC_REACTION_AGREEMENT
)
```

-- a frozen `0.375`, by equality, inside a `1e-12` window, on a quantity whose own entry
says in two places that it is `f/2`. **At `f = 0.5` the measured shortfall is
`0.25000000000000017` and the gate goes RED on a build the ladder is designed to produce.**
Every rung is `admissible` at the current basis, so none is unreachable, and
`floatfea/model/platform.py:801-807` descends PER BODY -- the platform can sit at `0.5`
while the hubs stay at `0.75`.

**The boundary, solved rather than sampled.** There is nothing to solve: the assertion is an
equality inside `rel=1e-12`, so its domain of validity is the single point `f = 0.75`. The
closed form the repair needs is already in the tree -- `floatfea/tolerances.py:1988-1989`
states `shortfall = f/2` -- and the table above confirms it at six values of `f`, each
within `2.2e-16` relative of `f/2`. One expression, the same shape `_defect_tip_ratio`
already gives the other half.

## 4. R705 -- DQ4(ii)'s MOMENT CHANNEL CANNOT FAIL ON A SIGN

The plan declares the quantity with the sign, twice: `docs/milestones/F4.md:72` and `:432`,
both "`Î¼L/2` forces, `Â±Î¼LÂ²/12` moments". The gate's quantity is `_dq4_ii_departures`
(`tests/verification/rung4/test_f4_static_and_mapping.py:1511-1515`):

```
worst_m = max(worst_m, abs(abs(f[ra]) - want_m) / want_m,
                       abs(abs(f[rb]) - want_m) / want_m)
```

The inner `abs()` throws the sign away, so the `Â±` is not in the assertion. I broke the
property and ran it -- three mutants of `local_mass`, all leaving the MAGNITUDES exactly
right, patched at the real assembly call site `floatfea/assemble/system.py:102`:

```
cmd    python <scratch>/adv4.py
rule   the shipped ceilings F4_DQ4_ELEMENT_VECTOR and F4_DQ4_RIGID_VECTOR, both 1e-12
out    mutant       DQ4ii                DQ4i
out    none         1.9372e-15 green     2.7960e-15 green
out    flip_both    1.9372e-15 green     2.0000e+00 RED     (M_A and M_B both negated)
out    flip_A       1.9372e-15 green     3.1402e-15 green   (M_A only -- so M_A = M_B)
out    swap_ends    1.9372e-15 green     2.0000e+00 RED
judge  DQ4(ii) reads the IDENTICAL value, to every digit, under all three. It cannot fail
       on any sign error in the rotational rows -- that is the abs() and not luck. And
       flip_A escapes DQ4(i) too, because the geometry is a star: every element shares
       node A, the four arms (and the hubs' three) are symmetric, so the consistent
       moments at the centre sum to zero for ANY field and negating zero is zero.
cmd    PYTHONPATH=<scratch> python -m pytest tests/verification/rung4 -q -p mutplug
         -p no:randomly -k "DQ4 or DQ5"
out    66 passed, 160 deselected    <- the WHOLE new gate set is blind to flip_A
```

**What this is NOT.** The defect shape IS caught -- 63 reds at rungs 2 and 3 under the same
mutant, including `test_the_six_RIGID_BODY_inertias_of_ONE_ELEMENT_are_exact` and
`test_G3_1a_A/B`. So there is no uncovered defect in the tree today and the element is
fine. This is (c) and not (a): **what the gate claims, on which quantity.** It claims
`Â±Î¼LÂ²/12` and asserts `|Î¼LÂ²/12|`.

**And it makes one sentence in the diff false.** `_independent_nodal_force`'s docstring at
`:1426-1431`: "Had the convention disagreed the gate would have reddened, and the
disagreement would have been the finding." For a GLOBAL flip against DQ4(i), true --
`flip_both` reads `2.0`. For a node-A-only disagreement, false in all 66 parametrisations.

**The fix is in the tree already.** `_DQ4_II_PLANES` (`:1485`) carries the plane label, and
the same docstring states both expected signs (`+wLÂ²/12` about local z for a y-load,
`-wLÂ²/12` about local y for a z-load). Comparing signed, or asserting `f[ra] == -f[rb]`,
closes it.

## 5. THE EU1 ADVERSARIAL CASE ON THE SIX NEW VALUES -- WHAT I REPRODUCED

Every new ceiling and counter, at every rung, through the shipped helpers:

```
cmd    python <scratch>/adv2.py
rule   the shipped assertions in test_DQ4_ii_*, test_DQ4_i_*, test_DQ5_*
out     f   DQ4ii clean  lump   m1.001  | DQ4i clean  norem   m1.001 | DQ5 clean norem m1.01
out  0.75   1.9372e-15  1.0e0  1.00e-3 | 2.7960e-15  6.67e-1 1.00e-3| 3.7795e-16 .25 8.33e-4
out   0.5   1.8999e-15  1.0e0  1.00e-3 | 2.5164e-15  1.00e0  1.00e-3| 3.7946e-16 .50 8.33e-4
out   0.4   1.8161e-15  1.0e0  1.00e-3 | 2.6616e-15  1.00e0  1.00e-3| 4.2182e-16 .60 8.33e-4
out   0.3   1.8626e-15  1.0e0  1.00e-3 | 2.5272e-15  1.00e0  1.00e-3| 4.8866e-16 .70 8.33e-4
out   0.2   1.8161e-15  1.0e0  1.00e-3 | 2.6616e-15  1.00e0  1.00e-3| 7.1712e-16 .80 8.33e-4
out   0.1   1.8161e-15  1.0e0  1.00e-3 | 2.6616e-15  1.00e0  1.00e-3| 1.3414e-15 .90 8.33e-4
out   0.0   ZeroDivisionError -- VACUOUS, and ONLY this rung
out  DQ4ii worst clean 1.9371509552001953e-15 at f=0.75, ceiling above it 516.2x
out  DQ4i  worst clean 2.796036563614433e-15  at f=0.75, ceiling above it 357.6x
out  DQ5   worst clean 1.3414143963362381e-15 at f=0.1,  ceiling above it 745.5x
out  all three counters below BOTH injections at EVERY non-vacuous rung: True
```

**ACCEPTED, and the figures reproduce to the last digit except one.** DQ4(ii)'s
`1.9371509552001953e-15` and `516.2x`; DQ4(i)'s `2.796036563614433e-15` and `357.6x`; the
rotational half's `1.241763e-16`; all three injection measurements
(`0.001000000000000745`, `0.0010000000000005215`, `0.0008333333333333215`); all three
margins (`2.0000x`, `2.0000x`, `2.0833x`); all three EH4 shrink factors
(`5e-4/0.001000000000000745 = 0.5000`, `0.5000`, `4e-4/0.0008333333333333215 = 0.4800`);
and `4i_no_remainder` getting STRONGER as the ladder descends (`6.667e-01` at `0.75`,
exactly `1.0` below) -- every one of them is mine as well as yours.

**The one that is not: DQ5's worst clean. Published `1.3335849658769691e-15` / `749.9x`;
measured `1.3414143963362381e-15` / `745.5x`, and the sweep that produced it missed a
direction.** Localised:

```
cmd    python <scratch>/adv3.py   (per body x per direction x per channel, f = 0.1)
out    platform minus_z 1.316061e-15  platform x 1.333585e-15  platform y 1.341414e-15
out    WORST: 1.3414143963362381e-15  ('platform', 'y', 'moment')
out    three repeats of the worst cell: identical to every digit
judge  1.333585e-15 IS the platform's `x` cell exactly, so the ladder-wide sweep covered
       minus_z and x and not y. The GATE parametrises over sorted(_DQ5_DIRECTIONS) = all
       three, so the gate is unaffected; only the published figure is understated.
       Closure item (C2), and I say so loudly because the discipline it misses is EU1's.
```

**`f = 0` is the only vacuous rung and skipping it is right.** `mu = 0` makes `want_f` and
`want_m` exactly zero, the measurement raises `ZeroDivisionError` rather than reporting a
small number, and that is the better failure. I checked the other six: none is vacuous, all
six are `admissible`, and all three gates have a denominator at each.

**THE INDEPENDENCE CLAIM HOLDS, and it is the one I most wanted to break.**

```
cmd    (read _independent_nodal_force, :1436-1453, every attribute it touches)
out    body.model.nodes.coords / body.elements / e.material / e.section / e.node_a /
       e.node_b / element_length / node_dofs / body.remainder_mass / body.remainder_node
       / np.cross
judge  no local_mass, no body_mass_matrix, no rotation_matrix, no to_global. The cross
       product annihilates the axial term on its own, so no local decomposition is needed
       and the element transform is genuinely off the path. EA4 is satisfied and
       gravity_load's docstring is the right precedent. The signs: flip_both reddens
       DQ4(i) at 2.0, so they are checked and not fitted -- for a GLOBAL convention.
       R705 is where that stops.
```

**The oblique field adds no discrimination, measured.** Both sides are exactly linear in
`field`, so the oblique case is a linear combination of the three axis cases and vanishes
exactly when they do:

```
cmd    python <scratch>/adv5.py
out    platform  |r(oblique) - sum_k ob_k r(e_k)| = 3.307e-10   |r(oblique)| = 6.985e-10
out    hub1      |r(oblique) - sum_k ob_k r(e_k)| = 9.094e-11   |r(oblique)| = 1.266e-09
judge  equal to round-off on a near-cancelling residual. The parametrisation is harmless
       and costs nothing; the COMMENT at :1480-1482 claiming it catches a sign error the
       axis cases would hide is what is false. C4.
```

## 6. THE TWO RULINGS THE HAND-BACK ASKED FOR

**RULING 1 -- DQ4(i)'s resultant half (hand-back item 2). I AGREE WITH YOUR REASONING, and
the measurement makes it stronger than you put it. NOT a blocking finding.** You said the
rotational gate "adds no discrimination over G3.1a". I measured that it reaches NINE of
G3.1a B's ten entries, not ten:

```
cmd    python <scratch>/adv11.py
rule   the shipped assertions in test_DQ4_i_ROTATIONS_resultant_and_moment_match_the_DECK
out    clean              rotational-half worst 1.241763e-16  GREEN
out    deck_mass x 1.001  rotational-half worst 1.240523e-16  GREEN
out    deck_mass x 2.0    rotational-half worst 6.208817e-17  GREEN
judge  the expected rotational columns are the skew first moment and `J_G alpha`, and
       NEITHER contains the total mass -- `m` enters only through the normaliser. A 100%
       total-mass error leaves this gate green, and G3.1a B catches it. So it is a strict
       SUBSET of G3.1a B, missing exactly the mass. Your conclusion stands and is if
       anything understated. 1.241763e-16 reproduces the declared 1.2417634328206378e-16.
```

Whether a gate that adds no discrimination should ship at all is a criterion question and
you routed it correctly. **It goes to Xabier, not into a round**, and I have nothing to add
beyond the measurement: labelling it is honest, and the docstring does label it.

**RULING 2 -- DQ8's normalisation (hand-back item 7). YOUR DIMENSIONAL REASONING IS RIGHT
IN KIND AND ITS PREMISE IS WRONG ON 6 OF 17 BODIES, WHICH MAKES THE REFUSAL MORE RIGHT
RATHER THAN LESS. Declining to declare is the CORRECT refusal and is NOT a blocking
omission.**

I reproduced the breakdown first, exactly:

```
cmd    python scripts/report_joint_reactions.py --period 10.0 --duration 40.0
out    force rel  : 2.3281e-16 (hub2, hub4) to 1.0012e-14 (buoy6)
out    moment rel : 1.0941e-10 (hub3) to 2.7915e-09 (platform)
out    rel        : identical to moment rel on every one of the seventeen
out    WORST BODY platform at 2.791541e-09 relative, over 17 of 17 bodies
out    aggregate 3.328367e-09 N; reaction scales 5.2845e-01 to 1.5061e+00
judge  every figure in e76f165's message is mine too, on a different machine.
```

Then I checked the premise, because "`max |Sum reactions|` is a FORCE scale" is a claim
about a 6-vector's largest component and nothing in the tree had split it:

```
cmd    python <scratch>/dq8split.py   (the same window, the same g_mid.T @ lam, with the
                                       scale's force rows and moment rows reported apart)
rule   DQ8: "normalised by that body's `max |Sum reactions|` over the window"
out    body     |R force| N   |R moment| N.m   dominates
out    buoy1     6.1175e-01     1.0237e+00     MOMENT
out    buoy2     5.8728e-01     6.1175e-01     MOMENT
out    buoy3     5.8728e-01     6.1175e-01     MOMENT
out    buoy7     6.5402e-01     7.5496e-01     MOMENT
out    buoy8     8.9309e-01     1.5061e+00     MOMENT
out    buoy9     8.9309e-01     1.5061e+00     MOMENT
out    hub1      1.3756e+00     2.1991e-03     FORCE
out    platform  1.1923e+00     4.5699e-02     FORCE
out    (the other nine FORCE)
out    the scalar is the FORCE half on 11 of 17 bodies
judge  the normaliser's OWN UNITS switch between bodies. On the eleven force-dominated
       bodies your account holds: moment_rel is a LENGTH and force_rel is dimensionless.
       On the six moment-dominated ones it INVERTS -- the scale is in N.m, so force_rel
       carries 1/length and moment_rel is the dimensionless one.
```

**So `judge2` in your commit message -- "`force rel` IS dimensionless and reads round-off on
all seventeen, which is the real result" -- is false on six of the seventeen.** It is
dimensionless on eleven. And the defect in DQ8's wording is worse than "a moment divided by
a force scale": **which of the two channels is dimensionless depends on which component
happens to be larger at that body, in that window, in that case, and it can switch between
any of them.** A ceiling on `<body>_rel` would mean a different physical thing on `buoy1`
than on `hub1`, and could change meaning between cases on one body.

That is the strongest available argument for your refusal, so I record it as support and
not as a reversal. **Declining to declare is what `CLAUDE.md` requires** -- "If execution
reveals that the locked plan was wrong, stop and say so" -- and the "Tolerance form" guard
makes a dimensionless ceiling on a dimensional quantity a defect outright. Reporting all
three forms under `<body>_rel`, `<body>_force_rel` and `<body>_moment_rel` so a ruling can
be made against numbers is the right call. **Not blocking, and do not declare one until the
quantity is chosen.** The still-unmeasured part, which you said: what the moment half
closes to against a MOMENT scale. Nothing in the tree has divided it by one. That is the
measurement the plan decision needs, and it is one patched run of the script you have.

## 7. R685 -- REPRODUCED IN FULL AND CLOSED

```
cmd    python <scratch>/adv7.py   (the shipped _mapping_error and _body_errors, all three
                                   shipped injections, at every rung)
rule   _mapping_error IS max(_body_errors(...).values()) -- read at :821-827, so the gate
       and its counter DO measure the same quantity, which is what I was asked
out    per body clean: hub1 2.1962235947826024e-16  hub2 1.7952712519813278e-16
out                    hub3 2.092543223926032e-16   hub4 1.634659231730534e-16
out                    platform 0.0
out    ceiling 1.0e-12 / worst clean = 4553.3x
out    wrong_node 0.9597085787263796  sign 3.5569621874567385  dropped 1.7784810937283693
out    smallest injection 0.9597085787263796 ; counter 0.2 ; margin 4.7985x
out    counter/ceiling = 2.000e+11      (ELEVEN decades, not twelve -- your correction)
out    BIT-IDENTICAL at all seven rungs f = 0.75 ... 0.0, every figure
judge  every one of R685's replacements is mine too, to the last digit, and the ladder
       invariance is measured rather than argued.
```

**And the force channel going to EXACTLY 0.0 is the per-body rule's signature, as you
claimed. I split the channels to check it rather than taking the max:**

```
cmd    python <scratch>/adv9.py
out    CLEAN                          force                     moment
out      platform                     0.0                       0.0
out      hub3                         2.092543223926032e-16     8.907844524080589e-17
out    wrong_node_same_body INJECTED
out      platform                     0.0                       0.9597085787263796
out      hub1..hub4                   bit-identical to clean
judge  the injection moves a block between two nodes of ONE body, so that body's force
       resultant is bit-identical -- and it is EXACTLY 0.0 both before and after. Not a
       tightening. floatfea/tolerances.py:2178 is right.
```

The parametrize list is three (`:961-963`), so "of the three" is now true of the mapping
entry. I also swept the whole file for phantom injectors, which is R695's lesson:

```
cmd    grep -nE "Injected by|injections are run by" floatfea/tolerances.py
         | grep -oE 'test_[A-Za-z0-9_]+' | sort -u | <resolve each against tests/>
out    ok test_DQ4_i_the_PER_NODE_gate_REDDENS / test_DQ4_ii_the_closed_form_gate_REDDENS
out    ok test_DQ5_the_free_fall_gate_REDDENS / test_EB6_a_PERMUTED_export_reddens_the_gate
out    ok test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula
out    ok test_G4_the_defective_formula_misses_the_reaction_by_f_over_two
out    ok test_R653_a_COEFFICIENT_WRONG_IN_THE_LAST_PRINTED_PLACE_reddens_the_gate
judge  seven live citations, seven resolve, ZERO phantoms. R695 is CLOSED, verified
       mechanically and not by reading the one line that was named.
```

## 8. R696 -- CLOSED, MEASURED

```
cmd    python <scratch>/adv12.py
rule   F4_STATIC_REACTION_AGREEMENT's entry: the full-scale magnitudes its 1e-12 ceiling
       is a round-off ceiling at
out    support reaction magnitudes 6.13e+06 to 6.95e+06 N
       (exact 6131249.999999998 .. 6948750.0000000065)
cmd    grep -n "25.0000%\|3.07e+06\|5.93e+06" floatfea/tolerances.py
out    1950-1951  (inside the paragraph LABELLED `R696:` as the old basis)
out    1983-1984  (inside the ER1(d) four-corner cell, where "25.0000% at f = 0.5" is the
                   CORRECT reading of the held-f corners)
judge  the live sentences carry 37.5000% and 6.13e+06 to 6.95e+06 N; the old figures
       survive only where they are labelled as the old figures or are correct for the
       corner they describe. R696 is CLOSED.
```

## Findings

**R704. (b and c, BLOCKING) `F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375` IS STILL A
FROZEN EQUALITY PINNED TO `f = 0.75`, AND IT IS THE HALF OF R694 THAT WAS NOT ANSWERED.**
`tests/verification/rung4/test_f4_static_and_mapping.py:350-356` and
`floatfea/tolerances.py:1995`, against `floatfea/model/platform.py:116` and `:801-807`.
Measured at every rung in section 3: the assertion is FALSE at `f = 0.5, 0.4, 0.3, 0.2,
0.1` and `0.0`, with shortfall `0.25000000000000017` at the ladder's own next rung, and
every rung is `admissible` so none is unreachable. The assertion is an equality inside
`rel=1e-12`, so its domain of validity is one point.
**Closed when** the expected side is the closed form at the body's own `f` -- `f/2`, which
the entry already states at `floatfea/tolerances.py:1988-1989` and which I confirmed at six
values of `f` to within `2.2e-16` relative -- in the same shape `_defect_tip_ratio` gives
the tip-moment half, **or** the entry records the inequality, its direction and what it
scales with per "State bounds, not identities", and the declared constant becomes a bound
rather than a value true at one rung. No new apparatus either way: the closed form is
already in the tree.

**R705. (c, BLOCKING) DQ4(ii)'s MOMENT CHANNEL CANNOT FAIL ON A SIGN, AND THE PLAN DECLARES
ITS QUANTITY AS `Â±Î¼LÂ²/12` IN TWO PLACES.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1511-1515`
(`abs(abs(f[ra]) - want_m)`), against `docs/milestones/F4.md:72` and `:432`. Measured in
section 4: three sign mutants of the element's rotational rows, magnitudes exactly
preserved, all three leave `_dq4_ii_departures` at `1.9372e-15` -- the clean value, to every
digit -- and all 66 DQ4/DQ5 parametrisations pass under the node-A-only flip, which also
escapes DQ4(i) because the star geometry sums the centre-node moments to zero for any
field. It makes `:1426-1431`'s "Had the convention disagreed the gate would have reddened"
false for that disagreement. **The element is fine and the shape IS caught at rungs 2 and
3** (63 reds under the same mutant), so this is the gate's reach and not a defect in
`floatfea/`.
**Closed when** the moment channel compares the SIGNED value -- `_DQ4_II_PLANES` at `:1485`
already carries the plane label and `_independent_nodal_force`'s docstring already states
both expected signs -- or asserts `f[ra] == -f[rb]` so the antisymmetry the `Â±` means is in
the assertion, **or** the entry at `floatfea/tolerances.py:2239-2257` states that the sign
is out of DQ4(ii)'s scope and names the rung-2 test that covers it, and the docstring
sentence at `:1426-1431` is withdrawn.

## Closure items

Fixed once, in the step's closure commit. **Not re-reviewed item by item, and the step is
not held on one.** The first is listed first because it gates a plan decision.

**C1. `scripts/report_joint_reactions.py:238` has the dimensional direction backwards** --
"gives a number with units of 1/length". `NÂ·m / N` is LENGTH; the commit message has it
right and the docstring has it inverted. **And both are incomplete**: ruling 2 measured the
scale to be the FORCE half on only 11 of 17 bodies, so on `buoy1`, `buoy2`, `buoy3`,
`buoy7`, `buoy8` and `buoy9` it is `force_rel` that carries `1/length` and `moment_rel`
that is dimensionless. The sentence "`force rel` IS dimensionless ... on all seventeen" is
false on six. **Closed when** `:217-247` says which channel is dimensionless on which
bodies and that it is a property of the window rather than of the body. **This one is
answered BEFORE the G4.1-dynamic quantity is chosen**, because that choice is (c) and this
is its input.

**C2. `F4_DQ5_FREE_FALL`'s published worst clean is understated and the sweep missed a
direction.** `floatfea/tolerances.py:2329-2331`, `docs/milestones/F4.md:433` and `:486`:
`1.3335849658769691e-15` / `749.9x`; measured `1.3414143963362381e-15` on
`platform / y / moment` at `f = 0.1`, `745.5x`, deterministic over three repeats. The
published figure is the platform's `x` cell exactly, so `y` was not in the sweep. The gate
parametrises all three and is unaffected. **Closed when** all three sites carry the figure
from a run over all three directions, taken after the last edit (CP3).

**C3. A figure without its body.** `tests/verification/rung4/test_f4_static_and_mapping.py:971`:
the wrong-node injection "leaves the force at `2.092543e-16`". That is `hub3`'s CLEAN
round-off, on a body the injection never touches; the INJECTED body's force channel is
exactly `0.0`, which is what `floatfea/tolerances.py:2178` says. The two sites disagree and
the entry is the right one. **Closed when** the docstring names the body, or quotes `0.0`.

**C4. The oblique field's comment claims discrimination it cannot have.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1480-1482`: "because three
axis-aligned ones leave every cross product with a zero component and a sign error in one
term can hide in it." Both sides of the residual are exactly linear in `field`, so the
oblique case is a linear combination of the three axis cases and vanishes exactly when they
do -- measured in section 5. The parametrisation is harmless and costs nothing. **Closed
when** the comment is withdrawn, or restated as "a fourth case at no cost" with the
linearity named.

**C5. The per-body label map is validated by COUNT only.**
`scripts/report_joint_reactions.py:289-295` raises on `len(names) != n_bodies` and says "a
per-body breakdown keyed by the wrong names is worse than none" -- but nothing asserts that
state block `k` IS `deck.bodies[k]`. The convention is inherited from the pre-existing block
at `:400-408` and is not introduced here, and the output corroborates it: `hub2`/`hub4`,
`buoy8`/`buoy9` and `buoy2`/`buoy3` are bit-identical symmetric pairs, which a misalignment
would break. **Closed when** the ordering is asserted rather than assumed, or the comment
says it is inherited and names where. **It becomes (c) the moment a tolerance is declared
on a per-body key**, which is EB6's label-provenance surface.

**C6. R697 to R703 from verdict 100, carried unchanged as closure items** and NOT
re-adjudicated, per verdict 100's own instruction. Spot-checked: R697 is still open --
`floatfea/tolerances.py:1988-1989` still generalises `f/2` to every member, and verdict 100
measured the twelve hub arms at `9/34`.

**C7.** The hand-back's red decomposition says `136` with `108` on the named-site guard. My
run and CI both say `135` with `107`, and the id sets are identical. **Closed when** the
next revision's figure comes from its own run.

## Tolerances touched

```
cmd    git diff fa709df..HEAD -- floatfea/tolerances.py | grep -E '^[+-]'
         | grep -v '^[+-][+-]' | grep -vE '^[+-]\s*#' | grep -vE '^[+-]\s*$'
out    -F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER: Final[float] = 0.05
out    +F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER: Final[float] = 0.005
out    +F4_DQ4_ELEMENT_VECTOR: Final[float] = 1.0e-12
out    +F4_DQ4_ELEMENT_VECTOR_COUNTER: Final[float] = 5.0e-4
out    +F4_DQ4_RIGID_VECTOR: Final[float] = 1.0e-12
out    +F4_DQ4_RIGID_VECTOR_COUNTER: Final[float] = 5.0e-4
out    +F4_DQ5_FREE_FALL: Final[float] = 1.0e-12
out    +F4_DQ5_FREE_FALL_COUNTER: Final[float] = 4.0e-4
judge  ONE value moved and it moved DOWN -- a counter TIGHTENED to answer a blocking
       finding, which is the opposite of the shape "Never widen" exists for. SIX new
       declarations. NO CEILING WAS WIDENED ANYWHERE IN THE TREE, and no value moved in
       the same commit as code it rescues.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.005` | dimensionless, relative; now a FLOOR under a closed form rather than a value at one rung | IS the counter; injected over all 16 members by `test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula` (`:599-656`) against `_defect_tip_ratio(body)` (`:572-597`) at each body's own `f` | `floatfea/tolerances.py:2016-2069`; plan row `docs/milestones/F4.md:477` | **R694's TIP-MOMENT HALF CLOSED. VALUE AND FORM ACCEPTED.** I verified the closed form `a/(12-5a)` against the solve on all 16 members at all six non-vacuous rungs, `rel=1e-12`, and the floor `0.005` under every one -- smallest `0.006060606060605793` at `f = 0.1`, margin `1.2121x`. `f = 0` is vacuous and the `continue` sits AFTER `checked += 1`, so `assert checked == 16` still binds and an empty collection is still an error. This is EU1's own prescribed repair: a constant right at one configuration replaced by the closed form the quantity actually has, with the constant demoted to a floor beneath every configuration. |
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.375` | `0.375`, unmoved | dimensionless, relative; **a frozen constant compared by EQUALITY inside `rel=1e-12`** | IS the counter; injected by `test_G4_the_defective_formula_misses_the_reaction_by_f_over_two` (`:325-359`) -- the citation now resolves, R695 closed | `floatfea/tolerances.py:1941-1995`; plan row `docs/milestones/F4.md:473` | **R704, BLOCKING. THE VALUE DID NOT MOVE AND THAT IS THE FINDING.** This is the entry R694 named alongside the one above, and verdict 100's `Closed when` said "both entries". Measured FALSE at every rung below `0.75`; `0.25000000000000017` at `f = 0.5`. EU1 is explicit that a value which does not move is the WORST case for an adversarial case, not the safest -- and the same commit that applied that lesson to one entry did not apply it to the entry thirty lines above it in the same file. R696's and R698's repairs to this entry's PROSE are both correct and measured; the ASSERTION is unchanged. |
| `F4_DQ4_ELEMENT_VECTOR` | -- | `1.0e-12` | dimensionless, relative | `F4_DQ4_ELEMENT_VECTOR_COUNTER = 5.0e-4`, from the SMALL injection (`moment_scale=1.001`, measures `0.001000000000000745`), run by `test_DQ4_ii_the_closed_form_gate_REDDENS` (`:1619-1643`) | `floatfea/tolerances.py:2239-2277`; plan rows `docs/milestones/F4.md:432`, `:482-483` | **CEILING AND COUNTER VALUE ACCEPTED; THE MOMENT CHANNEL'S QUANTITY IS R705.** Worst clean `1.9371509552001953e-15` at `f = 0.75` and `516.2x` reproduce exactly, at every rung. Taking the counter from the small injection rather than from `lumped`'s exact `1.0` is the right instinct, and the `2.0000x` margin is a real 0.1% detection threshold rather than one arbitrary perturbation. EH4's shrink factor `0.5000` verified. Turning the shear sweep into a shipped parametrisation instead of a docstring figure is CW0 applied correctly, and `phi = 9.9e+02` is a configuration the shipped model does not choose. **But the channel compares `abs(abs(f[ra]) - want_m)` and the plan row says the moments are `+-mu L^2/12`** -- section 4. |
| `F4_DQ4_RIGID_VECTOR` | -- | `1.0e-12` | dimensionless, relative; force and moment normalised separately, and the rotational half by `m l_b` / `m l_b^2` rather than by one newton | `F4_DQ4_RIGID_VECTOR_COUNTER = 5.0e-4`, from the SMALL injection (`mass_scale=1.001`, measures `0.0010000000000005215` at every rung), run by `test_DQ4_i_the_PER_NODE_gate_REDDENS` (`:1671-1696`) | `floatfea/tolerances.py:2278-2318`; plan rows `docs/milestones/F4.md:431`, `:484-485` | **ACCEPTED.** `2.796036563614433e-15` at `f = 0.75`, `357.6x`, margin `2.0000x`, shrink `0.5000`, and the rotational half's `1.241763e-16` all reproduce to the last digit. The INDEPENDENCE of the expected side is real and I checked it attribute by attribute rather than taking the docstring (section 5): no `local_mass`, no `body_mass_matrix`, no `rotation_matrix`. Replacing the `max(|want|, 1.0)` floor with `m l_b` and `m l_b^2` is C158 and R598 applied correctly -- `4.66e-09` really was newtons over one newton. And reading that `4i_no_remainder` STRENGTHENS as the ladder descends, rather than averaging it, is the right treatment of a per-rung diagnostic. |
| `F4_DQ5_FREE_FALL` | -- | `1.0e-12` | dimensionless, relative; four channels, each on its own stated scale | `F4_DQ5_FREE_FALL_COUNTER = 4.0e-4`, from the SMALL injection (`moment_factor=1.01`, measures `0.0008333333333333215`), run by `test_DQ5_the_free_fall_gate_REDDENS` (`:1832-1862`) | `floatfea/tolerances.py:2319-2357`; plan rows `docs/milestones/F4.md:433`, `:486-487` | **CEILING AND COUNTER ACCEPTED; ONE FIGURE IS UNDERSTATED (C2).** Margin `2.0833x` and shrink `0.4800` verified; the ladder dependence is REAL and I reproduced the whole sweep -- `3.7795e-16` at `0.75` rising to `1.3414e-15` at `0.1`. **Deriving the ceiling ladder-wide rather than at the shipped rung is exactly right, and it is the first time in this milestone that a ceiling was derived that way without being told to.** Two injections reddening DIFFERENT channels, with which-channel-which stated, is a real improvement on a single max. The worst clean is `1.3414143963362381e-15`, not `1.3335849658769691e-15`: the sweep covered `minus_z` and `x`, not `y`. **Your own BG0 call stands -- the "because less member mass conditions the relief solve differently" sentence has no cell and I treat it as unmeasured. Do not isolate it this round: it is not blocking and the rung-wide ceiling is correct either way.** |
| `F4_MAPPING_CONSERVATION` / `_COUNTER` | `1.0e-12` / `0.2` | unmoved | dimensionless, relative; `max` over bodies, not a sum | the wrong-node injection, smallest of THREE, run by `test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node` (`:961-1020`) | `floatfea/tolerances.py:2170-2238`; plan row `docs/milestones/F4.md:481` | **R685 CLOSED.** Section 7: `_mapping_error` IS `max(_body_errors(...).values())`, so the gate and its counter measure one quantity; every per-body replacement reproduces to the last digit and is bit-identical at all seven rungs; the force channel going to exactly `0.0` is the per-body rule's signature and I split the channels to confirm it rather than taking the max; "eleven decades" is right and "twelve" was not. Restating the weakening window as a 79% tolerated loss where the entry had implied 18% is EH4 done properly. |
| G4.1 dynamic (DQ8) | -- | **none declared** | -- | -- | `scripts/report_joint_reactions.py:217-247`; plan row `docs/milestones/F4.md:435` | **DECLINING TO DECLARE IS CORRECT AND IS NOT A BLOCKING OMISSION.** Ruling 2. DQ8's quantity is dimensional, and worse than the commit argued: the normaliser's own units switch between bodies, so NEITHER channel is reliably dimensionless. A dimensionless ceiling on it would be exactly the defect the "Tolerance form" guard names. Reporting all three forms so the ruling can be made against numbers is right. C1 is its closure item and lands before the quantity is chosen. |

## Carried

Verdict 100 (`6703575`, judging `fa709df`) left **three blocking findings, two items
carried by name, one deferred, and seven closure items.** Every one, with status. **Note
that `30e4395` -- the commit answering the three -- is inside this range and had never been
read by a verdict**, so this is their first review and not a re-check.

* **R694 (blocking) -- ANSWERED ON ONE OF ITS TWO ENTRIES. The tip-moment half is CLOSED;
  the reaction half is STILL OPEN and carries as R704, blocking.**
  `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` got the closed form in the gate and the constant
  as a floor, verified by me at every rung (section 3, Tolerances row 1).
  `F4_STATIC_REACTION_AGREEMENT_COUNTER` did not: still a frozen `0.375` by equality,
  measured false at every rung below `0.75`. Verdict 100's condition named **both** entries
  and the words "the gate no longer compares a frozen constant to a quantity that moves
  with a model parameter the model may change by itself". **Half of an item is not the
  item, and this is the sixth appearance of that shape in this milestone.**
* **R695 (blocking) -- CLOSED.** `floatfea/tolerances.py:1993` now names
  `test_G4_the_defective_formula_misses_the_reaction_by_f_over_two`, and I did not take
  that one line on trust: all seven live `Injected by` / `run by` citations in the file
  resolve to a `def` under `tests/`, zero phantoms (section 7).
* **R696 (blocking) -- CLOSED.** The three lines carry `37.5000%` and
  `6.13e+06 to 6.95e+06 N`; I measured `6131249.999999998 .. 6948750.0000000065` myself.
  The old figures survive only inside the paragraph labelled `R696:` as the old figures,
  and inside the ER1(d) four-corner cell where `25.0000% at f = 0.5` is the correct
  reading (section 8).
* **R685 (deferred under ER2) -- CLOSED, and I reproduced every replacement figure rather
  than accepting the account.** Section 7: the `max`-versus-sum rule, the five per-body
  clean values, `4553.3x`, all three injections, the `4.7985x` margin, the seven-rung
  bit-identity, the eleven-decades correction, and the exactly-`0.0` force channel.
* **R682 -- carried by name by verdict 100. Its basis-independent half stays closed, and
  its VALUE half is now closed too**, by the closed form in `_defect_tip_ratio`. R682 does
  not carry further.
* **R691 -- carried by name by verdict 100. CLOSED at the fifth-missed site.**
  `tests/verification/rung4/test_f4_static_and_mapping.py:553-558` now carries
  `f/(12-5f)` and `a/(12-5a)` with `a = 12f/17` rather than a basis-specific pair, so the
  next basis change cannot strand it again. That is the right repair and not the minimum
  one.
* **R698 (closure) -- CLOSED.** `floatfea/tolerances.py:1969-1977` now says the equality is
  held by the `rel=1e-12` window against a `4.4e-16` spread, not by exact arithmetic, and
  quotes the four arms' spread `0.37499999999999983` to `0.37500000000000006`, which
  refutes the old reason. Correct, and the candour about it having been a BG0 failure
  inside a tolerance comment is the right register.
* **R697 and R699 to R703 (closure) -- carried as closure items and NOT re-adjudicated**,
  per verdict 100's own instruction. C6 records the one I spot-checked: R697 is still open.

## The adversarial corpus (BE3)

**NO BATCH THIS ROUND, and that is a rule rather than an omission.** ES0's light scope says
"no corpus batch", and EG4(e) pauses batches until 28 October except mutation work on F4's
load-mapping gate and EB6's label-provenance gate. `tests/corpus/` is unchanged by me:
**nothing added, nothing carried.** Coverage measurement this round: **0 new entries, so
no coverage number** -- I will not publish one off a batch I did not run.

Two surfaces are now owed one, named so the 28 October batch has a target rather than a
theme:

* **F4's load-mapping gate.** The adversarial work I did do (section 7: the `max` rule,
  three injections, seven rungs, the channel split) found nothing, which is the first clean
  reading that gate has had. The next batch should press the two shapes a per-body `max`
  still cannot see: a defect identical on all five bodies, and a defect inside one body
  that moves a block between two nodes at the SAME position. `:971`'s force channel is
  exactly `0.0` for a reason, and that reason is also a blind spot.
* **EB6's label-provenance gate**, per C5. The DQ8 breakdown's `names` list is validated by
  count and corroborated only by symmetry. A corpus of permutations that PRESERVE the count
  is the shape, and `test_EB6_a_PERMUTED_export_reddens_the_gate` is the existing hook.

## Next step opens when

**STEP 2 STAYS OPEN. This check counts against NO round** -- there is no new report
revision, verified at the top -- **so verdict 97 remains round 1 of three and TWO REVISIONS
REMAIN.** Step 3 does not begin. Per EU1 this check still rules under CZ0 (a)-(d) and its
findings still block; what it does not do is consume one of the three revisions in which
the step's work is read in full.

**Answered before anything else, and only these two block:**

1. **R704** -- `tests/verification/rung4/test_f4_static_and_mapping.py:350-356`: the
   expected side at the body's own `f`, or the entry restated as a bound with its
   direction and what it scales with. **My figures to beat:** `0.37500000000000006` at
   `f = 0.75`, `0.25000000000000017` at `0.5`, `0.2000000000000001` at `0.4`,
   `0.15000000000000022` at `0.3`, `0.10000000000000019` at `0.2`, `0.0500000000000004`
   at `0.1` -- each within `2.2e-16` relative of `f/2`, every rung `admissible`. The
   closed form is already in the tree at `floatfea/tolerances.py:1988-1989`.
2. **R705** -- `tests/verification/rung4/test_f4_static_and_mapping.py:1511-1515`: the
   moment channel signed, or the antisymmetry asserted, or the scope stated and the
   docstring sentence at `:1426-1431` withdrawn. **My figures to beat:** all three sign
   mutants read `1.9372e-15`, identical to clean to every digit; 66 of 66 DQ4/DQ5
   parametrisations pass under the node-A flip; the same mutant gives 63 reds at rungs 2
   and 3, so the element is fine and the gap is the gate's.

**Nothing else blocks.** The six new declarations are accepted on value and form; R685,
R695, R696, R698, R682 and R691 are closed; and both rulings the hand-back asked for went
your way. **C1 to C7 are closure class** -- one list, one commit, do not spend a round on
them and do not hold the step on one -- **except that C1 is answered before the
G4.1-dynamic quantity is chosen**, because that choice is (c) and C1 is its input.

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION.** A closing condition that names two
entries, reported answered after one. R704 is the sixth appearance of that shape in this
milestone and the first on a carried gate rather than a sentence, and the command that
settles it is the one in section 3 -- run the ASSERTION, not the entry, at a configuration
the diff did not choose. The repair to R694 is the best piece of work in this range, and it
was applied to one of the two places the finding named; the entry thirty lines above it, in
the same file and in the same commit, got its prose re-derived and its assertion left
alone.

## On the schedule

The hand-back reports no slippage and I see none to add from this range: R704 and R705 are
each one expression in one file, and both closed forms are already in the tree. **Working
targets F4 14 Oct, table 17 Oct, code-check 22 Oct; committed dates unchanged.** The thing
I would watch is not these two findings. It is that G4.1 dynamic and G4.5 both wait on the
FloatSim runs and now also wait on a plan decision about DQ8's quantity (C1, ruling 2). If
that decision needs the plan reopened rather than a sentence, say so the day it is known
under DZ7c -- reduce scope, do not slip.

## On the criterion -- I was asked, and I agree with it

Both my blocking findings are (b)/(c), and everything else went to the closure list without
argument, including two sentences I would have blocked on six rounds ago. **ES0 and EU1
both earned themselves in this round and I want that on the record.** The light scope kept
me out of seven prose findings. EU1's adversarial case is what found R704 and R705, and
neither came from reading the diff: R704 came from running a shipped assertion at
`f = 0.5`, and R705 from negating a sign the gate's own `abs()` discards. In both cases the
diff reads clean, the entries are candid, the margins are stated, and every published
figure at the chosen configuration is correct.

One observation for Xabier, not a reopening, and nothing above depends on it: **EU1 says
"at least every admissible ladder rung", and a rung is not the only configuration a diff
does not choose.** R705 is not at a rung -- it is at a sign. The reusable form of the clause
is its own first phrase, "the model run at a configuration the diff did not choose", and
the ladder is one cheap instance of that rather than the definition. I would leave the
wording alone and read it the general way.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: fa709df70dca5821cda738b5bf951d65f4d68db0
Verdict: HOLD

**Reviewed commit: `fa709df`** (`fa709df70dca5821cda738b5bf951d65f4d68db0`, HEAD of F3,
pushed). Range `dc20d97..HEAD` -- two commits, `e2fa88a` and `fa709df`.
Tests: **92 failed, 2945 passed, 0 skipped** (MY OWN run, one invocation, no `--ignore`,
no `-k`, no deselection, in the repository itself, 654.26s. **All 92 are EG3 state (2) and
each is traced by name in section 2.**)

## Round of 2026-10-06 -- ES0 INTERIM CHECK. Counts against NO round.

**ES0's premise verified before anything else, because the exemption rests on it.**

```
claim  there is no new report revision -- the report is still the one verdict 97 judged
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-2.md
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), and a red
       I shipped
judge  7cee09f is the commit verdict 97 judged. The report has not moved across verdicts
       98, 99 or this one. This counts against no round, **verdict 97 remains round 1 of
       three, and TWO REVISIONS REMAIN.**
```

Instruction 1b does not fire, for the reason given in verdicts 98 and 99 and unchanged: a
report that PREDATES the newest verdict with no revision between them is EG3 state (2),
not a report answering a superseded round.

**HOLD, with THREE NEW BLOCKING ITEMS, all (b), all in `floatfea/tolerances.py`.** The
largest is not a margin and not prose: **R694 -- the repair to R682 is valid at exactly
one rung of a seven-rung ladder, and the ladder exists so that a body can descend.** At
`f = 0.5`, `MASS_FRACTION_LADDER`'s own next rung, the counter sits above the defect on
12 of 16 members -- bit for bit the R682 defect this commit reports closed.

**No STOP, and I ruled on ET2's three conditions.** The ladder is green at every rung in
CI at `e2fa88a`; all five bodies are PSD at `f = 0.75` on my own `admissible()` run, so
ER1(c)'s STOP does not fire. Section 6.

**Reading note for the hand-back, since it asked.** Having the figures in it again paid
for itself: every number in sections 3, 4 and 5 I reproduced rather than constructed, and
the time that bought went into section 3, which is the finding. That is the trade working
as intended.

## 0. CI AT THE REVIEWED COMMIT -- AND WHY THERE IS NO RUN AT IT

```
cmd    gh run list --commit fa709df70dca5821cda738b5bf951d65f4d68db0 --json name,conclusion,workflowName
out    []
judge  NOT CK2 and NOT unavailable-by-accident. `fa709df` touches only
       docs/reports/F4/preview-PRELIMINARY.md, and `.github/workflows/ci.yml` carries
       `paths-ignore: docs/reports/**` under CK0. A report revision changes no code and
       by design costs no run.
cmd    git diff --stat e2fa88a..HEAD -- floatfea tests scripts data .github
out    (empty). The code has not moved since the last commit that DID run.
judge  so run 37551431148 at `e2fa88a` describes the tree under review exactly.
```

**Run `37551431148` at `e2fa88a`, conclusion FAILURE. NOT CK2.** Both real jobs have 13
steps with real durations and the job ran 11 minutes; `runner_name` reads `null` through
this `gh` version's JSON for every job including the two that plainly ran, so I did not
use it as the CK2 discriminator -- I used the steps and the durations. No payment or
spending-limit annotation. The two `CI determinism` jobs are `skipped` with no steps, and
that is CK0's own `workflow_dispatch` condition, not CK2.

```
the verification ladder: SUCCESS at every step
  ladder 1 -- the solver is a solver        success
  ladder 2 -- the element is the element    success
  ladder 3 -- the model is the platform     success
  ladder 6 -- it stays fixed                success
  ladder 4 -- the loads are the loads       success
  ladder 5 -- independent confirmation      success
lint, unit and guards: FAILURE at `guards and meta-tests` ONLY
  actionlint success / ruff success / black --check success / mypy success /
  unit tests success / guards and meta-tests FAILURE
  92 failed, 955 passed, 1 warning in 666.31s
```

**No low rung is red, so no STOP is available on that ground.** I also ran the lint gates
myself at `fa709df`:

```
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests
out    All done! 98 files would be left unchanged.
cmd    python -m mypy floatfea
out    Success: no issues found in 36 source files
judge  `mypy`'s 36 reproduces the hand-back's figure; `black` reports 98 over
       `floatfea tests`, and the hand-back's 120 is presumably with `scripts` added. Not
       a finding, and I record the number I measured rather than adopting the one I was
       handed.
```

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat dc20d97..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty). None of the three moved. No STOP-class finding available here.
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py            <- non-empty, so the pathspec is the CI0 one
cmd    git diff dc20d97..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty). No conftest changed. No new plugin. CH2 clear, and the rung greens in
       section 0 are therefore believable.
```

## 2. THE 92 REDS, EACH TRACED BY NAME (EG3(i), CA2, R644)

| count | id | on EH1/EJ2's **state (2)** list as |
|---|---|---|
| 74 | `test_every_named_site_is_touched_or_declared[R686..R691-...]` | named, state (2) |
| 8 | `test_the_report_carries_the_finding[R686..R693]` | named, state (2) |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | named, state (2) |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | named, state (2) |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | named, state (2) |
| 1 | `test_the_guard_survives_the_state[baseline]` | the red baseline |
| 6 | the six planted states | the cascade, by failure line |

74+8+1+1+1+1+6 = 92, and the whole suite's 92 is this subset's 92 -- nothing is red
anywhere else in the tree:

```
cmd    python -m pytest -q                    (whole suite, ONE invocation)
out    92 failed, 2945 passed, 2 warnings in 654.26s
cmd    python -m pytest tests/test_report_carried.py tests/test_report_guard_states.py -q -rf
out    92 failed, 146 passed in 172.65s
judge  identical count, so every red in the tree is in those two files.
```

**CI's 92 and my 92 are the SAME IDS, not the same count** -- the only form of that claim
worth making on a different OS and a different libm:

```
cmd    gh run view 37551431148 --log-failed | grep -oE "FAILED tests/[^ ]+" | sort -u > ci
cmd    python -m pytest <the two files> -q -rf | grep -oE "FAILED tests/[^ ]+" | sort -u > local
cmd    diff ci local
out    (empty). IDENTICAL, 92 lines each.
```

**The cascade is identified by each state's OWN failure line, individually (R644):**

```
cmd    python -m pytest tests/test_report_guard_states.py -q
         | grep -E "^E +AssertionError" | sort | uniq -c
out    1 baseline: expected a clean run.
out    1 draft_suffix_beside_a_step_report: ... must be stepped over, not reacted to.
out    1 non_numeric_step_suffix:           ... must be stepped over, not reacted to.
out    1 step_number_is_the_empty_string:   ... must be stepped over, not reacted to.
out    1 superscript_digit_step_number:     ... must be stepped over, not reacted to.
out    1 verdict_amended_after_the_commit_the_report_answers: expected a clean run.
out    1 zero_padded_step_number:           ... must be stepped over, not reacted to.
judge  seven distinct lines, the same seven verdict 99 recorded. Each nested run pastes a
       dirty baseline carrying the state (2) ids; six states assert against a clean
       baseline and the baseline is dirty. Nothing is outside the list, so CZ1 (iv) does
       NOT fire and **this is not CZ0 (d)**.
```

`test_the_guard_reads_the_step_being_worked_on` is absent from the 92, so state (1) is
clear and this is unambiguously state (2). **Why 84 grew to 92:** verdict 99 added no
finding, so `test_the_report_carries_the_finding` stayed at 8; the named-site guard went
66 -> 74 because verdict 99 named eight more sites while measuring. The composition is
the tell that the growth is the boundary and not a defect.

**One thing the machine noticed before I did, and it is the `Carried` section's finding:**
the parametrisation
`test_every_named_site_is_touched_or_declared[R691-tests/verification/rung4/test_f4_static_and_mapping.py:549]`
is red. It is red for the state (2) reason -- the report predates verdict 99 -- but the
site it names is the one site of R691's closing condition that was not touched, and whose
figure this commit made false.

## 3. R694 -- THE BLOCKING ONE. THE COUNTER IS PINNED TO ONE RUNG OF A SEVEN-RUNG LADDER

I was asked to attack the `1.1321x` margin. **The margin is not the problem.** I first
reproduced the entry's figures on all sixteen members, in the gate's own denominator:

```
cmd    python <scratch>/m1.py   (build_superstructure + solve_superstructure_static +
                                 member_forces with the R663 formula on every member)
rule   ratio = |end_b[4]| / |end_a[4]| with the equivalent load deleted, which is the
       quantity `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` is compared against
out    platform:hub1..4_arm   0.09090909090909094 .. 0.09090909090909136  = 1/11, 4 members
out    hub1..4:buoy1..12_arm  0.0566037735849053  .. 0.056603773584906036 = 3/53, 12 members
out    SMALLEST 0.0566037735849053   LARGEST 0.09090909090909136
out    counter 0.05 below EVERY defect: True   margin 1.1320754716981059
judge  every figure in the entry and in `F4.md:477` reproduces to the last digit --
       `1/(53/3)`, the smallest, and the `1.1321x`. And both rationals are STRUCTURAL,
       not coincidental: ratio = a/(12-5a) with a = wL/R, which is `f` on the platform
       (R = W/4, wL = fW/4) and `12f/17` on the hubs. f=0.75 gives 0.75/8.25 = 1/11 and
       (9/17)/(12-45/17) = 3/53.
```

**Then I built the case the gate should fail and ran it: the ladder's own next rung.**

```
cmd    python <scratch>/m5.py   (every rung of MASS_FRACTION_LADDER, all 16 members, all
                                 three moved/held counters evaluated by their own rule)
rule   the shipped assertions: ratio > 0.05 on all 16; shortfall == 0.375 within
       rel=F4_STATIC_REACTION_AGREEMENT; spread(100x soften) > 1.3
out      f      min tip/root    >0.05?   plat shortfall  ==0.375?   spread@100x  >1.3?
out    0.75   0.0566037735849053   True   0.37500000000000006  True   1.3814612408854223  True
out     0.5   0.03448275862068926  FALSE  0.25000000000000017  FALSE  1.5616518375226505  True
out     0.4   0.02666666666666618  FALSE  0.2000000000000001   FALSE  1.6337280761775415  True
out     0.3   0.01935483870967727  FALSE  0.15000000000000022  FALSE  1.7058043148324336  True
out     0.2   0.01249999999999982  FALSE  0.10000000000000019  FALSE  1.7778805534873248  True
out     0.1   0.006060606060605793 FALSE  0.0500000000000004   FALSE  1.8499567921422175  True
out    members below the counter: 0/16 at f=0.75, **12/16 at f=0.5**, 16/16 at 0.4 and below
```

**At `f = 0.5` the counter sits above the defect on 12 of 16 members. That is R682, to the
member count, resurrected by one rung of descent.** And the reaction counter is an
EQUALITY, so it goes red at every rung but one.

**The boundary, solved rather than sampled (Invert the decision rule and solve):**

```
cmd    python <scratch>/m5.py   (brentq on the closed form a/(12-5a) - 0.05, a = 12f/17)
out    f=0.75 hub ratio 0.05660377 >0.05 True    f=0.69 0.05092251 True
out    f=0.68 hub ratio 0.05000000 >0.05 FALSE   f=0.67 0.04908425 FALSE
out    BOUNDARY: the hub ratio crosses the counter 0.05 at f = 0.6800000000003912
judge  the live domain of `0.05` is f >= 0.68. The shipped f is 0.75 -- 9.3% of f above
       the edge -- and `MASS_FRACTION_LADDER`'s next rung is 0.5, a third below it.
```

**Why this is (b) and not a hypothetical.** `MASS_FRACTION_LADDER` exists for exactly one
purpose, stated in its own docstring at `floatfea/model/platform.py:130-133`: "The ladder
is descended per body when `f` is inadmissible". `admissible()` is consulted at every
rung -- the commit's own headline claim -- and ER0 has just moved the deck's mass basis,
which is the input `admissible()` reads. The first time any body fails PSD at 0.75 it
descends to 0.5, and then `test_EO1_the_analytic_gate_REDDENS_on_the_R663_formula` goes
red on twelve members with its own message, *"the counter is on the wrong side of the
defect for that member"* -- which would be **true**, and would be a false alarm about the
counter rather than a finding about the code. The entry's candour ("the value did not move
-- which is not the same as having been right") is the right instinct applied to the past
tense; the same sentence is due about the future.

**This is "State bounds, not identities", and the inequality is already derivable.** The
closed form `ratio = a/(12-5a)` reproduces both exact rationals above and is monotone in
`f`, so a counter expressed as a function of `f`, or an assertion that compares against
the derived ratio rather than a frozen constant, covers the whole ladder and needs no new
apparatus.

**And I solved the direction that WEAKENS, so this is not a blanket objection (EH4).**
`F4_STATIC_SYMMETRY_SPREAD_COUNTER = 1.3` is **safe** across the entire ladder: the spread
rises monotonically as `f` falls -- 1.3814, 1.5616, 1.6337, 1.7058, 1.7779, 1.8500 -- so
descending makes that gate easier to trip, never harder. The 1.3 move is sound and I say
so. The other weakening edge on it, which the entry does not state and which the deleted
sentence used to:

```
cmd    python <scratch>/m2.py   (bisect the softening factor at which spread == 1.3)
out    factor 0.01 -> 1.3814612408854223 ; factor 0.05 -> 1.1866786371824025 (RED at 1.3)
out    BOUNDARY: the injection may weaken from 100x to 38.9687x and still trip 1.3
judge  the spread-side margin 1.0627x IS in the entry, so the deleted "admits a 4%
       weakening" sentence has an equivalent and nothing false was published. The
       injection-side figure (100x -> 39x) is not there, and it is the one a reader
       changing the injection would need. Closure class (R703).
```

## 4. R695 AND R696 -- TWO (b)s INSIDE THE ENTRIES THIS COMMIT EDITED

**R695. The counter's `Injected by` names a test that does not exist, and the same commit
is what deleted it.** CZ0 (b) is explicit that it covers "a counter **and how it is
injected**", and the `Injected by` line is the only statement of that.

```
cmd    grep -oE 'Injected by `[A-Za-z0-9_]+`' floatfea/tolerances.py
         | sed 's/.*`\(.*\)`/\1/' | sort -u
         | while read t; do grep -rqF "def $t" tests/ || echo "PHANTOM: $t"; done
out    PHANTOM: test_G4_the_defective_formula_misses_the_reaction_by_a_quarter
judge  the ONLY phantom among every `Injected by` citation in the file -- every other one
       resolves. `floatfea/tolerances.py:1979` names it; `e2fa88a` renamed the function to
       `test_G4_the_defective_formula_misses_the_reaction_by_f_over_two`
       (`tests/verification/rung4/test_f4_static_and_mapping.py:315`) and left the
       citation behind. "Every citation resolves" -- and this one was broken by the commit
       that cites it.
```

**R696. The ceiling entry that brackets the moved counter still publishes the old basis,
and it is the only statement of what that counter-case is.**

```
cmd    sed -n '1940,1981p' floatfea/tolerances.py
out    :1942  "...which puts the tip shear 25.0000% below the reaction -- eleven decades
              outside this, and exercised by the conservation gate..."
out    :1948  "...at full-scale magnitudes of 3.07e+06 to 5.93e+06 N..."
out    :1950  "# COUNTER-CASE: R663's defective formula puts the tip shear 25.0000% below
              the reaction, which is eleven decades outside this."
out    :1981  F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.375
cmd    python <scratch>/m1.py
out    measured shortfall, four platform arms: 0.37500000000000006 .. 0.37499999999999983
out                                            -> 37.5%, not 25.0000%
out    measured reaction magnitudes: 6.13e+06 (platform) to 6.95e+06 (hub) N,
out                                  not 3.07e+06 to 5.93e+06
judge  `floatfea/tolerances.py` now states, 31 lines apart and in the same commit, that
       the defect is 25.0000% and that the declared counter for it is 0.375.
       `:1950-1951` is the ONLY sentence in `F4_STATIC_REACTION_AGREEMENT`'s entry saying
       what its counter-case is and how far outside the ceiling it sits -- which is
       precisely the carve-out the criterion names, "a docstring that is the only
       statement of what a tolerance means". BP0's "in the same commit, not the next one"
       is the rule, and these three lines are inside the two entries the commit edited.
```

## 5. WHAT I REPRODUCED AND ACCEPT -- AND THE TWO RULINGS THE HAND-BACK ASKED FOR

**Every ER1(d) figure in the commit reproduces.** Nothing below is taken from the
hand-back; all of it is my own run at `fa709df`.

```
cmd    python <scratch>/m1.py
out    platform arm  L=50.0  R=6131250.000000004  wL=4598437.5
out                  root Vz=1532812.5000000014   root My=191601562.5000002
out    hub arm       L=25.0  R=6948750.000000002  wL=3678750.0
out                  root Vz=3270000.000000003    root My=127734375.00000006
judge  all eight of ER1(d)'s declared figures (`F4.md:215-219`) reproduce exactly, and so
       does the reconstruction verdict 99 predicted them from. The hub reaction rising
       while the hub mass does not is confirmed STRUCTURALLY, not just numerically:
       R = (W_hub + R_plat_arm)/3 = (14715000 + 6131250)/3 = 6948750, and with the OLD
       platform arm reaction (14715000 + 3065625)/3 = 5926875. **Section 5b's cell is
       right** -- M accounts for all of it and f for none.
cmd    python <scratch>/m2.py  (admissible() on all five bodies at the shipped build)
out    platform True  hub1 True  hub2 True  hub3 True  hub4 True
out    clean symmetry spread 9.113860057399177e-16 against a 1e-12 ceiling (1097x of room)
out    100x-softened spread 1.3814612408854223, margin 1.0627x over the declared 1.3
judge  ER1(c)'s STOP does not fire. The symmetry figures reproduce to the last digit.
```

**RULING 1 -- `measurement_fraction` STAYS. ES1 does not require it deleted, and I
measured the distinction rather than reading the comment that asserts it.**

```
cmd    python <scratch>/m4.py  (build_superstructure(), then at 0.5 and at 1.0)
out    no argument  -> f = [0.75]*5, 4 findings (the four hubs' above-steel density)
out    0.5          -> 5 findings, one per body: "the mass fraction is 0.5, handed in by
                       the caller rather than taken from (0.75, 0.5, ...), so
                       `admissible()` was never consulted for it. This body is a
                       MEASUREMENT, not one to ship."
out    1.0          -> 10 findings: the same five plus five above-steel densities
                       (platform 9528.0, hubs 15244.7 kg/m^3)
cmd    grep -rn 'mass_fraction=' --include=*.py floatfea tests scripts
out    floatfea/model/platform.py:578 and :632 only -- the BodyModel field, not a caller.
       No caller passes the old name; the rename is complete.
judge  ES1's sentence is about the SHIPPED path, and `build_superstructure()` with no
       argument descends the ladder with `admissible()` consulted at every rung. A
       measurement entry point that labels every body it builds as not-to-ship is not an
       override on that path. **And ER3 asks for `f = 1.0`, which is on no ladder and
       which ES1 does not put on one** -- so the parameter is what makes ER3 satisfiable
       at all, and deleting it would make the plan self-contradictory. **NO FINDING.**
       The preview's "5 findings at f = 0.5 and 10 at f = 1.0" reproduces exactly.
```

**RULING 2 -- THE EQUALITY ON `0.375` STANDS, AND THE REASON GIVEN FOR IT DOES NOT.** This
is the one judgement the hand-back explicitly asked me to try to break, and it half breaks.

```
claim  (floatfea/tolerances.py:1960-1962) "`f/2` is exact arithmetic on exactly-
       representable values (0.75/2 = 3/8), NOT a solve-derived number, so the
       portability objection to a bit-exact counter does not apply here"
cmd    python <scratch>/m1.py   (the shortfall on each of the four platform arms)
out    0.37500000000000006  0.37500000000000017  0.37499999999999983  0.37499999999999983
judge  REFUTED by the entry's own measurement. A quantity that were not solve-derived
       would be bit-exact 0.375; this one spreads over four members to 4.4e-16 relative,
       because the shortfall is `(R - tipVz)/R` and BOTH terms come out of the solve.
rule   the shipped assertion is `shortfall == pytest.approx(0.375,
       rel=F4_STATIC_REACTION_AGREEMENT)`, i.e. rel=1e-12 -- NOT bit-exact
out    measured worst solve spread 4.4e-16 against a 1e-12 window = **2.3e+03x of room**
judge  so the equality is SAFE, and that is the portability answer the hand-back wanted --
       three decades of headroom measured ACROSS the members, not an exactness argument.
       The value and the form are right. The sentence explaining them is a BG0 defect: a
       correct number with an unmeasured cause attached, and one loop refutes the cause.
       Recorded as R698, closure class, because the value and the form are unaffected.
```

## 6. ET2 / NO STOP, AND THE FIGURES I COULD NOT CHECK

The ladder is green at every rung in CI (section 0) and all five bodies are PSD at 0.75 on
my own run (section 5), so neither ET2's ground nor ER1(c)'s fires. **No STOP.**

**Recorded as UNVERIFIED BY ME, not as accepted:** EK0(a)'s `0.000000e+00 N` over 24611
steps, EK0(e)'s duality, and EJ4's six per-case residuals (worst `7.850279e-13`). They
come from `scratchpad/er1b_runs.py` and `scratchpad/er1_combine.py` against six FloatSim
runs in `../HSP-runs` -- neither script is in the tree and neither worktree is available
to me. I checked what I could: the six step counts sum to 24611 exactly, and EJ4 is
reported per body and per case rather than averaged, which is what Â§ Non-negotiables
requires. **This is why R700 matters more than its class suggests** -- the committed driver
cannot reproduce those runs, because it ships with the override switched off.

## Findings

**R694. (b, BLOCKING) `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05` AND
`F4_STATIC_REACTION_AGREEMENT_COUNTER = 0.375` ARE VALID AT `f = 0.75` ALONE, ON A LADDER
WHOSE PURPOSE IS TO DESCEND.** `floatfea/tolerances.py:2027` and `:1981`, against
`floatfea/model/platform.py:116`. Measured at every rung in section 3: at `f = 0.5` the
tip-moment counter sits above the defect on **12 of 16** members and the reaction counter's
equality goes red; at 0.4 and below, 16 of 16. Boundary solved: the hub ratio crosses 0.05
at **`f = 0.6800000000003912`**. `admissible()` is consulted at every rung by design, and
ER0 has just moved the input it reads.
**Closed when** both entries state the bound over the whole ladder rather than the value at
one rung -- the closed form `ratio = a/(12-5a)` with `a = f` (platform) and `a = 12f/17`
(hubs) reproduces both exact rationals and is derived in section 3 -- **or** the entries
record the inequality, its direction and what it scales with, per "State bounds, not
identities", and the gate no longer compares a frozen constant to a quantity that moves
with a model parameter the model may change by itself. No new apparatus either way.

**R695. (b, BLOCKING) `floatfea/tolerances.py:1979` NAMES AN INJECTOR THAT DOES NOT
EXIST**, and `e2fa88a` is the commit that renamed it. The only phantom among every
`Injected by` citation in the file, checked mechanically in section 4. CZ0 (b) covers "a
counter and how it is injected".
**Closed when** `floatfea/tolerances.py:1979` names
`test_G4_the_defective_formula_misses_the_reaction_by_f_over_two`, with the one-line loop
from section 4 pasted showing no phantom remains.

**R696. (b, BLOCKING) THE CEILING ENTRY BRACKETING THE MOVED COUNTER STILL PUBLISHES THE
OLD BASIS.** `floatfea/tolerances.py:1942`, `:1948` and `:1950-1951` state the defect as
`25.0000%` and the reaction magnitudes as `3.07e+06 to 5.93e+06 N`; measured 37.5% and
`6.13e+06 to 6.95e+06 N`. `:1950-1951` is the only sentence in the
`F4_STATIC_REACTION_AGREEMENT` entry saying what its counter-case is and how far outside it
sits, so it is the criterion's own carve-out rather than ordinary prose. BP0 requires it in
this commit, not the next.
**Closed when** all three lines carry the measured basis, with a `claim/cmd/out` from a run
taken after the last edit (CP3), and the `# COUNTER-CASE` and `# Injected by` lines in both
entries agree with the declared `1e-12` and `0.375`.

**R697. (closure) THE `f/2` MECHANISM IS FALSE OF 12 OF THE 16 MEMBERS.**
`floatfea/tolerances.py:1974-1975` ("The shortfall is `f/2` exactly ... so the tip shear is
short by `f/2` of the reaction"), `docs/milestones/F4.md:473`, and
`tests/verification/rung4/test_f4_static_and_mapping.py:320-323`.
Measured: the hub arms read **0.2647058823529411 = 9/34** on all twelve, not 0.375. The
platform identity IS confirmed, at six values of `f` (0.375 / 0.25 / 0.2 / 0.15 / 0.1 /
0.05 at f = 0.75 / 0.5 / 0.4 / 0.3 / 0.2 / 0.1), so the declared value and the injected
member are right -- it is the unqualified generalisation that is refuted. The cause: the
platform's four rollers carry exactly its own weight (`R = W/4`, `wL = fW/4`, so
`wL/2R = f/2`) while the hubs carry the platform's handed-down share
(`R = (W_hub + R_plat)/3`), which `F4.md` Â§ 5b gets right thirty lines away. **Closed when**
the sentence is qualified to the platform arms, or restated as `(wL/2)/R` with the hub
figure beside it.

**R698. (closure) THE EQUALITY'S JUSTIFICATION IS REFUTED BY ITS OWN MEASUREMENT.**
`floatfea/tolerances.py:1960-1962`. Ruling 2, section 5. **Closed when** the entry says
what actually protects the equality -- `rel=F4_STATIC_REACTION_AGREEMENT = 1e-12` against a
measured solve spread of `4.4e-16`, `2.3e+03x` of room -- instead of claiming the quantity
is not solve-derived.

**R699. (closure) THE BP0 SWEEP MISSED FIVE MORE `f`/`M`-DEPENDENT FIGURES, AND ONE IS THE
SITE R691's CLOSING CONDITION NAMED.** Each with its measurement at `fa709df`:

| site | published | measured |
|---|---|---|
| `tests/.../rung4/test_f4_static_and_mapping.py:555-556` | "1/19 on a platform arm and 1/24 on a hub arm" | **1/11** and **3/53** |
| `tests/.../rung4/test_f4_static_and_mapping.py:526-527` | "platform `114960937.5 N*m`, hub `117515625 N*m`, both reproduced to every digit" | **191601562.5** and **127734375.0** |
| `tests/.../rung4/test_f4_static_and_mapping.py:95` | "every platform-arm shear 25.0000% low" | **37.5%** |
| `floatfea/post/member_forces.py:10` | "every shear 25.0000% low, every root moment 5.56% high" | **37.5%** and **10.0%** |
| `floatfea/post/member_forces.py:12-13` | "the tip shear is `3065625.000000 N` ... the member's weight `1532812.5 N`" | **6131250.0** and **4598437.5** |

`:555-556` is contradicted by this commit's OWN new comment twenty-six lines below at
`:581-582`, which says 1/11 and 3/53. `:526-527` is the site I withdrew at verdict 99
*because it was true*; it is now false. **Closed when** each of the five carries the
measured basis or is withdrawn.

**R700. (closure) THE REPLAY DRIVER SHIPS WITH THE OVERRIDE OFF, AND ONE SENTENCE CLAIMS
OTHERWISE.**
```
cmd    grep -n 'PLATFORM_MASS_OVERRIDE' scripts/report_joint_reactions.py | head -2
out    120:PLATFORM_MASS_OVERRIDE: dict[str, object] | None = None
cmd    sed -n '153,156p' scripts/export_platform_deck.py
out    "The replay driver applies the same override in memory
       (`scripts/report_joint_reactions.py`), so the FE side and the FloatSim runs see one
       basis."
cmd    grep -rn 'PLATFORM_MASS_OVERRIDE\|PLATFORM_OVERRIDE\|apply_override' --include=*.py floatfea tests
out    (empty). Nothing imports or tests either override, and nothing compares them.
judge  as committed, the FE side is on 20 kg and the replay driver is on 10 kg. The
       sentence is refuted by one grep -- CW0. Two sources of truth for one physical
       input, and the only thing holding them equal is that someone edits both. The six
       ER1(b) runs were driven by `scratchpad/er1b_runs.py`, which is not in the tree, so
       nothing committed reproduces section 6's figures.
```
It is not silent -- `_apply_platform_override` prints "deck as exported, no override" --
which is why this is a reproducibility finding and not a wrong-answer one. **Closed when**
the two overrides have one source, or the `export_platform_deck.py` sentence states what
is true of the committed default.

**R701. (closure) "`Vz` does not move with `f` at all" IS TRUE ONLY OF THE STATION THE
TABLE REPORTS.** `docs/reports/F4/preview-PRELIMINARY.md:200-206`.
```
cmd    python <scratch>/m3.py   (both stations, all 16 members, f = 0.5 / 0.75 / 1.0)
rule   worst relative move over f, against the f = 0.75 value
out    worst-station Vz (what the table reports) : 1.206246184067538e-15
out    ROOT-station  Vz                          : **1.0000000000000002**
out    platform:hub1_arm root Vz  3065625.0 -> 1532812.5 -> **0.0** exactly
out    hub arms         root Vz   4496250.0 -> 3270000.0 -> 2043750.0
```
So "worst relative move `0.000000`, which is exactly zero and not merely small" is wrong
even inside its own domain (it is 1.2e-15), and the ROOT shear moves by 100% -- at
`f = 1.0` a platform arm's root shear is exactly zero, which is a result worth publishing
in its own right. The stated mechanism, "the TOTAL weight each member carries is conserved
exactly, and the root shear is that total whatever the split", is refuted in both halves:
the member's own weight is `f`-proportional and doubles from 0.5 to 1.0, and the root shear
is precisely what moves. The figure is `f`-independent because it is the TIP shear, which
equals the support reaction, which is `f`-independent because the total body weight is.
**This is assertion domain blindness in a published figure** -- a max-over-stations
reduction cannot contain the dependence -- and the draft sentence the report says the
measurement refuted was right about the root station. **Closed when** the sentence names
the station, or the table carries both.

**R702. (closure) "`My` runs from `1.1200x` to `0.8800x`" IS THE HUB'S RANGE PUBLISHED AS
THE WHOLE RANGE.** `docs/reports/F4/preview-PRELIMINARY.md:208-210`. Measured per member:
platform arms **1.200000 / 0.800000**, hub arms 1.120000 / 0.880000. The worst is 20%, not
12%. A ratio without its operating point. **Closed when** the figure names which members
it is of, or quotes the worst.

**R703. (closure) THE SYMMETRY ENTRY LOST ITS INJECTION-SIDE EDGE (EH4).**
`floatfea/tolerances.py:2104-2118`. The deleted "admits a 4% weakening of the injection"
sentence has a spread-side equivalent in the new `1.0627x`, so nothing false was
published. The injection-side figure is absent: measured, the injection may weaken from
`100x` to **`38.9687x`** and still trip 1.3. **Closed when** the entry carries it, or
points at the report section that does.

**One line for Xabier, not a finding.** ES1 records the hub density finding as "hub arms
15 t/m against the stand-in tube's 10.3 t/m as steel". The measured value at the shipped
`f = 0.75` is **11433.5 kg/m^3**; `15244.7 kg/m^3` is the value at `f = 1.0`. The results
label publishes the measured 11433.5, which is right, so nothing in the tree is wrong --
but ES1's own figure appears to be the `f = 1.0` number and he may want to know that the
finding at his own chosen fraction is 1.33x smaller than the one he was told about.

## Tolerances touched

```
cmd    git diff dc20d97..HEAD -- floatfea/tolerances.py | grep -E '^[+-]'
         | grep -v '^[+-][+-]' | grep -vE '^[+-]\s*#'
out    -F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.25
out    +F4_STATIC_REACTION_AGREEMENT_COUNTER: Final[float] = 0.375
out    -F4_STATIC_SYMMETRY_SPREAD_COUNTER: Final[float] = 1.5
out    +F4_STATIC_SYMMETRY_SPREAD_COUNTER: Final[float] = 1.3
judge  TWO values moved. Both are counters, both move with ER0's basis, and both are in
       the same commit as the basis change -- which is what BP0 requires, and is NOT the
       same commit as code they rescue. NO CEILING MOVED anywhere in the tree.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_STATIC_REACTION_AGREEMENT_COUNTER` | `0.25` | `0.375` | dimensionless, relative | IS the counter; injected by `test_G4_the_defective_formula_misses_the_reaction_by_f_over_two` at `tests/verification/rung4/test_f4_static_and_mapping.py:315` | `floatfea/tolerances.py:1955-1980`; plan row `docs/milestones/F4.md:473` | **VALUE AND FORM ACCEPTED, FOUR FINDINGS.** I measured `0.37500000000000006` on the injected member and reproduced the four-corner cell structurally (`R = W/4` and `wL = fW/4` on the platform, so `wL/2R = f/2`; `f` moves it and `M` does not). The equality is safe with `2.3e+03x` of room (Ruling 2). **R694**: it is an equality pinned to `f = 0.75` and goes red at every other ladder rung. **R695**: its `Injected by` names the deleted name. **R696**: the paired ceiling entry still says `25.0000%`. **R697/R698**: the `f/2` generalisation and the exactness reason are each refuted by measurement. |
| `F4_STATIC_SYMMETRY_SPREAD_COUNTER` | `1.5` | `1.3` | dimensionless, relative | IS the counter; injected into the MODEL by `test_EK0d_the_symmetry_gate_REDDENS_on_an_unsymmetric_frame` (`:664-680`), which softens and re-solves rather than perturbing the expected side -- verified by reading `_soften_one_arm` | `floatfea/tolerances.py:2104-2126`; plan row `docs/milestones/F4.md:479` | **ACCEPTED.** `1.3814612408854223` and the `1.0627x` margin reproduce to the last digit; the clean case is `9.11e-16` against a `1e-12` ceiling, `1097x` of room. The BG0 cell is sound: `A` is held so the body's mass is identical and only the stiffness moved. **And I solved the weakening direction, which is the one that matters here: this counter is SAFE across the entire ladder** -- the spread rises monotonically as `f` falls, 1.3814 to 1.8500, so descending makes it easier to trip. R703 is the one gap and it is closure class. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.05`, unmoved | dimensionless, relative | IS the counter; now injected over **all sixteen** members at `tests/.../test_f4_static_and_mapping.py:583-603`, with `assert checked == 16` so an empty collection is an error and not a silent skip -- verified | `floatfea/tolerances.py:2002-2027`; plan row `docs/milestones/F4.md:477` | **R682's BASIS-INDEPENDENT HALF CLOSED; THE VALUE IS R694 AND BLOCKS.** The sixteen-member loop is a real repair and I reproduced `1/11`, `3/53`, the smallest `0.0566037735849053` and the `1.1321x` on all sixteen, deriving both rationals independently from `a/(12-5a)`. The entry's candour about a survived number is the right instinct. But the value holds only for `f >= 0.68`, and the ladder's next rung is `0.5`, where it sits above the defect on 12 of 16 -- the same count as the defect it reports closing. |
| `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | `1.0e-5` | `1.0e-5`, unmoved | dimensionless | unchanged | `floatfea/tolerances.py:2070-2086` | **ET3's withdrawal of the `86.4%` label ACCEPTED**, and it is exactly what verdict 99's Ruling 2 asked for: the label went, the number went with it, and the `50.0%` and the band `[4.210526e-06, 5.789474e-06]` stayed. No value moved. |

## Carried

Verdict 99 left **two open findings, one closed-and-now-reopened item, and five numbered
conditions.** Every one, with status:

* **R682 -- reported CLOSED. I CLOSE ITS BASIS-INDEPENDENT HALF AND REOPEN THE VALUE AS
  R694.** The sixteen-member loop and the per-member derivation are done, and I reproduced
  every figure in them. The VALUE is wrong one rung down the ladder -- 12 of 16 at
  `f = 0.5`, boundary at `f = 0.68`, section 3. **R694 carries it and blocks.**
* **R685 -- STILL OPEN, hold accepted without reservation.** The mapping entry's four
  figures are untouched in this range: the `tolerances.py` diff has no hunk inside
  `F4_MAPPING_CONSERVATION`'s entry. ER2's ordering puts it after ER1 and that ordering is
  right. Not held against this diff.
* **R691 -- reported closed at three sites. TWO OF THE THREE WERE EDITED, AND THE THIRD IS
  NOW FALSE.** Fifth appearance of the shape, and the first time the tree is not clean
  underneath it.
  ```
  claim  (hand-back) "`tolerances.py` and `F4.md:348` and `test...py:549` are all three
         edited in `e2fa88a`"
  cmd    git diff dc20d97..HEAD -U0 -- tests/verification/rung4/test_f4_static_and_mapping.py
           | grep '^@@'
  out    @@ -315 +315 @@   @@ -320,4 +320,10 @@   @@ -567 +573,5 @@   @@ -569,13 +579,25 @@
  judge  **`:549` is in none of the four hunks.** At `dc20d97`, line 549 is
         `"the DEFECTIVE root moment this ratio uses is 1/19 on a platform arm "` -- the
         exact site verdict 98's `Closed when` named. It is now line 555, still says 1/19
         and 1/24, and this commit's own new comment at `:581-582` contradicts it.
  cmd    git show dc20d97:docs/milestones/F4.md | sed -n '348p' ; sed -n '348p' docs/milestones/F4.md
  out    "**In the FIRST commit:**"   (both). Unchanged, and in no F4.md hunk either.
  cmd    git diff dc20d97..HEAD -U0 -- docs/milestones/F4.md | grep '^@@'
  out    @@ -439,0 +440,20 @@   @@ -453 +473 @@   @@ -457 +477 @@   @@ -459 +479 @@
  judge  the row that WAS edited is `F4.md:477`, which is the right site with the right
         content -- so the WORK is two of three, correctly done, and the REPORT of it
         names a set that does not match. `:520`, which I withdrew at verdict 99 *because
         it was true*, is false as well now (R699).
  ```
  **R699 carries the figures; it is closure class and it is the fifth time, so I record
  the shape here and spend no round on it.** The discipline that would have caught it is
  mechanical and already available: a closing condition that names a line gets
  `git diff -U0 | grep '^@@'` run against it, not a recollection of having been there.
* **R690 -- CLOSED at verdict 99, and it stays closed.** All thirteen directives are
  readable in `docs/milestones/F4.md` Â§ 0, and `dc20d97` is a clean `plan:` commit (118
  insertions, 0 deletions, no code) saying what verdict 99 asked it to say -- the authority
  is Â§ 0's own shape, not EH2.
* **Verdict 99's `86.4%` withdrawal -- ANSWERED** at `floatfea/tolerances.py:2079-2083`
  under ET3. Tolerances table.
* **Verdict 99's condition 1 (ER1(a)-(e), BP0)** -- (a) DONE: deck, header and golden move
  together and the override is stated on the deck's own face. (b) DONE but not reproducible
  from the tree (R700). (c) DONE and all five bodies PSD at 0.75, measured by me. (d) DONE
  for the two counters and the three plan rows, **INCOMPLETE for five figures (R699) and
  three lines inside the tolerance entries themselves (R696)**. (e) DONE, Â§ 5b, and the
  hub-reaction cell is correct and I verified it structurally.
* **Verdict 99's condition 2 (R682's value on the new basis)** -- the per-member table is
  there and every figure reproduces. **The value is R694 and blocks.**
* **Verdict 99's condition 3 (R685)** -- correctly deferred by ER2.
* **Verdict 99's condition 4 (R691's declaration-only sites)** --
  `tests/test_plan_matches_tolerances.py`, `floatfea/tolerances.py:1990`, `CLAUDE.md`,
  `docs/SUPERVISOR.md`. Still owed, and they are part of the 92 that only a report revision
  clears. Not held against this diff.
* **Verdict 99's condition 5 (EG3(ii))** -- **MEASURED HERE SO IT IS NOT OWED AGAIN.**
  State (2) at `fa709df`: `92 failed, 2945 passed, 0 skipped` whole-suite; `92 failed,
  146 passed` on the two guard files; the same 92 ids in CI run `37551431148`, diffed
  rather than counted. Every id traced in section 2. State (1) absent, so this is
  unambiguously state (2).
* **BR0** -- satisfied and checked: three plan rows moved plus a new Â§ 5b, in the same
  commit as the values. `git diff -U0 -- docs/milestones/F4.md` gives hunks at `+440,20`
  (Â§ 5b) and at `473`, `477`, `479` (the three rows).

## The adversarial corpus (BE3)

**No new corpus file this round, and the number is still reported.** EG4(e) pauses batches
until 28 October except mutation work on F4's **load-mapping** gate and EB6's
label-provenance gate, and ES0 excludes a batch from an interim check. Neither exception
covers the gates in front of me -- these are the static and symmetry counters -- so the
round went into measurement instead of a file, and EH4 is where it went.

* **New entries in `tests/corpus/` this round: 0.** Previous batch: 36, at `4f99c7f`.
* **Boundaries solved in BOTH directions, which is what EH4 bought:** six ladder rungs x
  16 members x 3 counters evaluated by their own rules, the tip-moment counter's
  `f`-boundary solved by `brentq` rather than sampled, the symmetry injection's weakening
  edge bisected to `38.9687x`, and the symmetry counter confirmed safe across the whole
  ladder. **Two of the three blocking findings came from inverting the direction and from
  nothing else** -- R694 entirely, and R696 from reading the entry that BRACKETS the
  edited one rather than the edited one. That is the second round running where EH4's
  inversion is where the finding was.
* **Coverage, honestly:** of the three blocking findings, **one** (R695) is a shape a
  check in the tree could catch mechanically -- one loop over `Injected by`. The other two
  are shapes nothing in the tree looks for. The implementer's own planted-shape counts are
  not the measurement; this is.
* **One corpus hygiene note on my own files, for me and not for the implementer:**
  `tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48, 49, 50 carry
  `measured=` figures on the OLD mass basis (`2.299219e+06`, `3065625`, `1532812.5`,
  `5926875`). Corpus entries record what was measured when they were written, so they are
  not stale in the way a tolerance comment is -- but a later reader will compare them with
  a tree on ER0's basis. I will re-head that file at the next batch.

## Next step opens when

**STEP 2 STAYS OPEN. This check counts against NO round, so verdict 97 remains round 1 of
three and TWO REVISIONS REMAIN.** Step 3 does not begin.

**Answered before anything else, and only these three block:**

1. **R694** -- the two counters bounded over the ladder, or the ladder's reach stated as
   an inequality with its direction and what it scales with. **My figures to beat:** at
   `f = 0.5`, 12 of 16 members below `0.05` and `shortfall = 0.25000000000000017`; at
   `f = 0.4`, 16 of 16; boundary `f = 0.6800000000003912`; `ratio = a/(12-5a)` with `a = f`
   and `a = 12f/17` reproducing `1/11` and `3/53` exactly. The symmetry counter is safe
   across the ladder and needs nothing -- do not move it.
2. **R695** -- `floatfea/tolerances.py:1979`, with the phantom loop from section 4 pasted
   at the repair commit.
3. **R696** -- `floatfea/tolerances.py:1942`, `:1948` and `:1950-1951`, each at the
   measured basis: `37.5%`, and `6.13e+06 to 6.95e+06 N`.

**R682 and R691 carry by name into the next revision's `Carried`, and R682 blocks there as
R694.** R685 stays deferred under ER2. **R697 to R703 are closure class** and are a list
the step's closure commit absorbs -- do not spend a round on them, and do not hold the step
on one.

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION.** A counter whose domain of validity is
narrower than the model's own configuration space with the narrowness unstated -- R694 is
the second time a counter in this entry has been right about one configuration and wrong
about the rest, and the first time the configuration was chosen by the CODE rather than by
a directive. A closing condition reported answered at a site that
`git diff -U0 | grep '^@@'` says is in no hunk: fifth appearance, and the command that
settles it is one line. And a BP0 sweep that covers the entries it edited but not the
entries that BRACKET them -- R696 is three lines in the paired ceiling, thirty lines above
a value the same commit moved.

## On the schedule

The hand-back reports no slippage and I see none to add. ER1 landed; R694, R695 and R696
are all inside one file, and R694's closed form is already derived in section 3, so the
repair is small even though the finding is not. **Working targets F4 14 Oct, table 17 Oct,
code-check 22 Oct; committed dates unchanged.** If R694's repair turns out to need the
gate's assertion restructured rather than the entry reworded, that is the day to say so
under DZ7c -- reduce scope, do not slip.

## On ES0's scope -- I was asked, and this is an observation, not a reopening

**I agree with ES0 and I am not relitigating it.** The hand-back asked whether the light
scope was wrong for a diff this size. My answer: **the rule held and the scope did not.**

ES0's scope is "the suite and CI, plus a CZ0 (a)-(d) scan of the diff". All three blocking
findings are (b), so the rule caught the right class. But the thing that FOUND R694 was not
a scan of the diff -- it was building the model at a configuration the diff did not choose
and running it. Nothing in `e2fa88a` looks wrong when you read it; `0.05` is unchanged, the
entry is candid, the margin is stated, and the gate grew from one member to sixteen. The
defect is only visible from outside the diff.

So, for Xabier and not for this loop: **ES0's light scope should say that a diff moving a
tolerance VALUE gets the adversarial case regardless of the round's class**, because a
value is the one thing a scan of a diff cannot judge. You have to run the model somewhere
the diff did not look. That is one measurement, not new apparatus, and this round is the
evidence for it.

It goes to Xabier through the implementer. It is not a HOLD, and nothing above depends on
it.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: dc60ee9a42530407ad9a687478861b092beaf732
Verdict: HOLD

**Reviewed commit: `dc60ee9`.** (`dc60ee9a42530407ad9a687478861b092beaf732`, HEAD of F3,
pushed.) Range `4615498..HEAD` -- two commits, `7a40758` and `dc60ee9`.
Tests: 2951 passed, 84 failed, 0 skipped (MY OWN run, one invocation, no `--ignore`, no
`-k`, no deselection, in the repository itself, 645.25s. **All 84 are EG3 state (2) and
each is traced by name in section 2.**)
**CI at the reviewed commit: run `37497138919` at `dc60ee9`, conclusion FAILURE.**
`the verification ladder: success` at EVERY step -- `ladder 1`, `2`, `3`, `6`, `4`, `5`.
`lint, unit and guards: failure` at `guards and meta-tests` ONLY; `actionlint`, `ruff`,
`black --check`, `mypy` and `unit tests` all success. `84 failed, 961 passed in 663.08s`.
NOT CK2 for the two jobs that ran: `runner_name` is `GitHub Actions 1000001534` and
`...1535`, the steps ran, the durations are real. The two `CI determinism` jobs are
`skipped` with `runner_name: null`, no steps and a one-second span -- **and that is CK0's
own `if: github.event_name == 'workflow_dispatch'`, not CK2**: `.github/workflows/ci.yml:90`
makes them by-hand-only, the annotations list is empty, and there is no payment or
spending-limit annotation. A conditional skip is a check that was not asked for, which is
a third thing again from unavailable and from red.

## Round of 2026-10-06 -- ES0 INTERIM CHECK. Counts against NO round.

**ES0's premise verified before anything else, because the exemption rests on it.**

```
claim  there is no new report revision -- the report is the one verdict 97 judged
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-2.md
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), ...
judge  7cee09f is the commit verdict 97 judged. The report has not moved across verdict
       98 and across this one. This counts against no round, verdict 97 remains round 1
       of three, and TWO REVISIONS REMAIN.
```

Instruction 1b does not fire, for the reason given in verdict 98 and unchanged: a report
that PREDATES the newest verdict with no revision between them is EG3 state (2), not a
report answering a superseded round.

**HOLD, and there is no new blocking item. All three of verdict 98's items are CLOSED and
I reproduced every figure in all three repairs rather than reading them.** The HOLD is the
step's own state: step 2's work -- ER1, EQ2's remainder, EQ3 -- has not been done, R682 and
R685 are open and legitimately held by ER2's ordering, and step 3 does not begin. Nothing
in this diff needs fixing before ER1 starts.

**No STOP, and I was asked to rule on that specifically.** Section 5 rules on ER0 as a
recorded input change. The ladder is green at every rung in CI.

**The whole executable surface of this diff is four comment lines.**

```
claim  nothing under floatfea/ changed except comments
cmd    git diff 4615498..HEAD -- floatfea/ | grep -E '^[+-]' | grep -v '^[+-][+-]' \
         | grep -vE '^[+-]\s*#'
out    (empty)
cmd    git diff --stat 4615498..HEAD -- floatfea/
out    floatfea/tolerances.py | 31 +++++++++++++++++++++++++++----
judge  so a CZ0 (a) finding is not available in this range by construction. The one
       executable change anywhere is `compared > 0` -> `compared == _CHANNELS` in rung 4,
       which is (c), and it is section 4.
```

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 4615498..HEAD -- .claude docs/SUPERVISOR.md
out    (empty). Neither file moved. No STOP-class finding available here.
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                   <- non-empty, so the pathspec is the CI0 one
cmd    git diff 4615498..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty). No conftest changed. No new plugin. CH2 clear.
cmd    git log --format='%h %an %s' 4615498..HEAD -- docs/reviews tests/corpus
out    7f822ba gating-supervisor review: F4 step 2 -- ES0 INTERIM CHECK ...
judge  the only commit touching docs/reviews/ in this range is my own verdict 98. The
       implementer wrote neither a verdict nor a corpus entry.
```

**`dc60ee9` is a clean `plan:` commit and I checked the form rather than the subject
line.**

```
cmd    git show --stat dc60ee9
out    docs/milestones/F3.md | 19 ++ ; docs/milestones/F4.md | 99 ++ ; 118 insertions(+)
claim  it touches no code and deletes nothing
out    118 insertions(+), 0 deletions. No floatfea/, no tests/, no .claude/.
claim  it cites the finding that asked for it
out    "plan: the EQ, ER and ES directives recorded in F4.md and F3.md section 0 (R690)"
```

## 2. THE 84 REDS, EACH TRACED BY NAME (EG3(i), CA2)

EG3(i) is explicit that a family is not a trace, and R644 is why each id gets run on its
own. Every id, matched against EH1's and EJ2's corrected **state (2)** list:

| count | id | on the list as |
|---|---|---|
| 66 | `test_every_named_site_is_touched_or_declared[R686/R687/R688/R689/R690/R691-...]` | named, state (2) |
| 8 | `test_the_report_carries_the_finding[R686..R693]` | named, state (2) |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | named, state (2) |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | named, state (2) |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | named, state (2) |
| 1 | `test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` | the red baseline |
| 6 | the six planted states | the cascade, by failure line |

66+8+1+1+1+1+6 = 84, and the whole-suite run's 84 is this subset's 84 -- nothing is red
anywhere else in the tree:

```
cmd    python -m pytest -q                 (whole suite, one invocation)
out    84 failed, 2951 passed, 2 warnings in 645.25s
cmd    python -m pytest tests/test_report_carried.py tests/test_report_guard_states.py
         tests/test_report_numbers_are_sourced.py -q -rf
out    84 failed, 187 passed in 181.68s
judge  identical count, so every red in the tree is in the three report-guard files.
```

**The cascade is identified by each state's OWN failure line, individually, not by its
name** -- the R644 discipline, and the seven lines are distinct:

```
cmd    python -m pytest tests/test_report_guard_states.py -q
         | grep -E "^E +AssertionError" | sort | uniq -c
out    1 baseline: expected a clean run.
out    1 draft_suffix_beside_a_step_report: ... must be stepped over, not reacted to.
out    1 non_numeric_step_suffix:           ... must be stepped over, not reacted to.
out    1 step_number_is_the_empty_string:   ... must be stepped over, not reacted to.
out    1 superscript_digit_step_number:     ... must be stepped over, not reacted to.
out    1 verdict_amended_after_the_commit_the_report_answers: expected a clean run.
out    1 zero_padded_step_number:           ... must be stepped over, not reacted to.
judge  each nested run pastes the same dirty baseline (74 failed, 139 passed) carrying
       the state (2) ids. Six states assert against a clean baseline and the baseline is
       dirty. Nothing is outside the list, so CZ1 (iv) does not fire and this is not (d).
```

**CI's 84 and my 84 are the SAME IDS, not the same count**, which is the only form of that
claim worth making on a different OS and a different libm:

```
cmd    gh run view 37497138919 --log-failed | grep -oE "FAILED tests/[^ ]+" | sort -u > ci
cmd    diff ci local
out    (empty). IDENTICAL, 84 lines each.
```

**EG3(ii) -- state (1) cleared at verdict 98's own commit.**
`test_the_guard_reads_the_step_being_worked_on` is absent from the 84 and
`4615498..7f822ba` is the verdict alone, so the measurement at `7f822ba` is the
measurement here.

**Why the red grew from 32 to 84, since a growing red deserves a sentence:** verdict 98
added three findings naming many sites, and `test_every_named_site_is_touched_or_declared`
is one parametrisation per site. The composition is the tell that the growth is the
boundary and not a defect -- R692 and R693 contribute **zero** named-site failures, because
`7a40758` touched their sites, and R691 contributes four, all of them sites my own finding
named as already correct (`CLAUDE.md`, `docs/SUPERVISOR.md`, `floatfea/tolerances.py:1990`)
or as a guard that cannot see the shape (`tests/test_plan_matches_tolerances.py`). Those
four are declarations the next revision writes, which the hand-back says it will.

## 3. R691 -- CLOSED, AND I WITHDRAW ONE SITE OF MY OWN CONDITION WITH THE MEASUREMENT

I built the frame, ran the solve, and computed the defect's ratio on all sixteen members
rather than checking the arithmetic on paper:

```
cmd    python <scratch>/p1.py   (build_superstructure + solve_superstructure_static,
                                 member_forces with the R663 formula on every member)
rule   tip_ratio = |end_b[4]| / |end_a[4]| with the equivalent load deleted, which is
       the quantity `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` is compared against
out    platform:hub1..4_arm   tip_ratio 0.0526315789473684..  -> 1/19 EXACTLY, 4 members
out    hub1..4:buoy1..12_arm  tip_ratio 0.0416666666666662..  -> 1/24 EXACTLY, 12 members
out    min 0.04166666666666627   max 0.05263157894736891
out    counter 0.05 sits ABOVE the defect on 12 of 16 members
judge  `tolerances.py` was right and the plan row and the assertion string were wrong.
       `1/19` and `1/24` are confirmed in the gate's own denominator; the F4.md row's
       `smallest measured 0.04166666666666627` is `hub3:buoy9_arm` to the last digit;
       and "sits above the defect on 12 of the 16 members" is 12 of 16 measured.
```

So `docs/milestones/F4.md:447` and `test_f4_static_and_mapping.py:549` are both correct
now, and the `1/18`, `5.555556e-02` and `1.0550e+14x` figures survive nowhere outside the
files that quote them AS WRONG:

```
cmd    grep -rn '1/18\|5\.555556e-02\|1\.0550e+14' --include=*.py --include=*.md .
         | grep -v '^\./docs/reviews/'
out    CLAUDE.md:274, docs/SUPERVISOR.md:438   -- quote the figure as wrong. Correct.
out    docs/milestones/F4.md:230               -- ES2's record of the deletion. Correct.
out    floatfea/tolerances.py:1990-1991        -- quotes it as the deleted claim. Correct.
out    test_f4_static_and_mapping.py:550       -- "never 1/18 (R691)". Correct.
out    docs/reports/F4/step-2.md:382-384       -- the report's own account. Correct.
```

**AND I WITHDRAW THE `:520` CLAUSE OF MY OWN CLOSING CONDITION, with the measurement that
withdraws it.** My R691 named `test_f4_static_and_mapping.py:520` as a fourth site "same
arithmetic", on a grep hit for `114960937`. It is not the same arithmetic: `:520` states
the two CORRECT root moments and claims they reproduce, and they do.

```
cmd    python <scratch>/p1.py   (analytic_My vs solve_My, all 16 members)
out    platform arms: analytic 114960937.500000  solve 114960937.500000
out    hub arms:      analytic 117515625.000000  solve 117515625.000000
judge  `:520`'s "both reproduced to every digit" is TRUE at this commit. The site needed
       nothing, so it satisfies my condition's "or no figure at all" branch. Withdrawn.
```

**The discipline point stands even though the tree is clean, and I record it rather than
blocking on it.** The hand-back reports R691 answered at "three sites" and the three it
names are `tolerances.py`, `F4.md` and `test:549` -- which is not the set my condition
named (`F4.md:348`, `test:549`, `test:520`). `:520` went unmentioned in either branch the
site-by-site rule offers. It happens to be clean, and it is clean because **I** measured
it, not because the answer said so. That is the fourth appearance of this shape in five
verdicts. It is not blocking: there is nothing false in the tree, and CZ0 gives me no head
for "the answer counted a different three".

## 4. R692 -- CLOSED, REPRODUCED IN BOTH DIRECTIONS, AND THE WEAKENING EDGE SOLVED TOO

Not read: run, with the production gate's own helpers, the real mapper and the real
fixture, and with the old predicate evaluated beside the new one on every row.

```
cmd    python <scratch>/p2.py  (_joint_wiring, _synthetic_lam, map_joint_reactions,
                                _channels_compared, _body_errors -- the shipped helpers)
rule   the shipped pair: `_channels_compared(...) == _CHANNELS` and
       `max(per_body) < F4_MAPPING_CONSERVATION`
out    _CHANNELS = 10
out    dense (control)        compared=10/10  err=2.196e-16  ==10: GREEN   >0: GREEN
out    all zero               compared= 0/10  err=0.000e+00  ==10: RED     >0: RED
out    only block 0 (buoy1)   compared= 2/10  err=0.000e+00  ==10: RED     >0: GREEN
out    ... all twelve buoy blocks          compared= 2/10    ==10: RED     >0: GREEN
out    ... all four hub blocks             compared= 4/10    ==10: RED     >0: GREEN
out    SIXTEEN of sixteen degraded rows move from GREEN to RED. The control stays GREEN.
judge  my figures to beat were 16 of 16 green at 2 of 10 and 4 of 10 channels. All
       sixteen now redden, and the gate's own dense row is unaffected.
```

**EH4's weakening direction, which nothing asked for and which is the one that matters
here: how degraded may a row be and still read green?** Solved by exhaustion rather than
sampled, over every keep-set of the sixteen blocks:

```
cmd    python <scratch>/p6.py  (all C(16,k) keep-sets for k = 1..4, 2516 rows)
rule   a row "passes" if compared == 10 AND max(per_body) < 1e-12
out    k=1:   0 of   16 pass        k=2:   0 of  120 pass
out    k=3:   0 of  560 pass        k=4: 175 of 1820 pass
out    example: blocks (0, 1, 6, 14) = buoy1, buoy10, buoy4, hub3
judge  the boundary is k = 4: twelve of sixteen blocks may be zero and the gate still
       reads green. I rule that CORRECT rather than vacuous, and the distinction is the
       one R684 and R689 are both about: on a four-block row every one of the five bodies
       has a nonzero expected resultant and is compared RELATIVELY, and the mapping
       genuinely is right on it. On a single-block row three of five bodies were never
       compared at all. `== 10` closes exactly the second thing and nothing is hiding in
       the first -- a defect at a zeroed joint is a no-op, and a dropped block inside a
       body that still has load is what `internal_joint_dropped` reddens at 1.778.
```

**Two structural rulings, so they are not left ambiguous for the next reader.**

* `compared` reads the EXPECTED side (`_one_body_error` takes `f_scale` from `want`), so
  `compared == 10` is an assertion about the FIXTURE's premise, not about the mapper's
  output. That is what makes it the density check verdict 98 offered as the alternative,
  and it is why it cannot mask the error assertion: a mapper that puts nothing on a body
  leaves `compared` at 10 and is caught by `max(per_body)`.
* `_CHANNELS = 10` as a literal int is right here for the same reason `len(joint_order)
  == 16` two lines above is right: on a model with a sixth body this gate SHOULD go red
  and force a re-derivation rather than silently re-scale. I say so rather than leaving
  the hard-coded count to be read as an oversight. It is a count, not a tolerance, and
  `tests/test_no_tolerance_literals.py` is green on the file.

## 5. ER0 -- A RECORDED INPUT CHANGE, NOT A RE-LOCK. NO STOP.

I was asked to rule on this specifically and before ER1's six re-runs. **ER0 does not
reopen EK's lock.** The ground is not EH2, and I read Â§ 0 line by line rather than
accepting the citation:

```
claim  Â§ 0 (EK0, DQ4-DQ9, EK2-EK4) states no mass and no `f` ANYWHERE
cmd    sed -n '28,140p' docs/milestones/F4.md   (the whole locked block, read)
out    DQ4 "# expected: deck YAML mass, J_G"   <- the deck BY REFERENCE
out    DQ5 "the deck's mass with DY0's split"  <- DY0 BY REFERENCE
out    DQ7 "No buoy FE mass"                   <- a scope statement, not a value
out    EK0(d) "self-weight from the FE mass (the DY0 distribution)"
judge  Â§ 0 locks METHOD, SUBJECT and NORMALISATION, and names the mass only by reference
       to the deck and to DY0. A deck value is an input to the locked method, not one of
       the locked answers, so changing it changes what the method is applied to and
       leaves every Â§ 0 sentence true. That is a recorded input change. NOT a STOP.
```

**One correction to the plan's own reasoning, recorded and not blocking:** `F4.md:150`
cites EH2 as the clause that permits this. EH2 is at `docs/milestones/F3.md:678` and it
governs **when `PLATFORM_RIGID_MODE_EXACTNESS` may move** -- (a) never on fixed inputs,
(b) a re-derivation on changed inputs in a `plan:` commit, (c) both edges at `2x`. It is a
tolerance-movement rule, and the thing it licenses here (ER1(d) re-deriving every
dependent figure in the `plan:` commit) is right by EH2(b) by analogy, but EH2 is not a
lock-scope clause and should not be cited as the authority for not re-locking. The
authority is the paragraph above.

**ER1(d)'s eight static figures are published in the plan AHEAD OF THE CODE, so I
checked all eight.** The new basis is not in the tree -- `MASS_FRACTION_LADDER` is still
`(0.5, 0.4, 0.3, 0.2, 0.1, 0.0)` -- so I reconstructed them from the measured old basis by
the linearity of statics, and validated the reconstruction against a measured quantity it
did not use:

```
cmd    python <scratch>/p5.py  (measured L, wL and R on the shipped basis, then
                                platform mass x2 and f 0.5 -> 0.75 by linearity)
out    measured now: platform L=50.0  wL=1532812.5  R=3065625.0
out    measured now: hub      L=25.0  wL=2452500.0  R=5926875.0
out    PLATFORM NEW: R=6131250.0000  wL=4598437.5000  Vz=1532812.5000  My=191601562.5000
out    HUB NEW:      R=6948750.0000  wL=3678750.0000  Vz=3270000.0000  My=127734375.0000
out    CONTROL for the hub formula R = (hub weight + platform share)/3, evaluated on the
out    OLD platform share: 5926875.0 against the MEASURED 5926874.999999998
judge  all eight of the plan's figures reproduce exactly, and the control says the
       formula that produced the hub pair is the right formula -- the hub reaction rises
       although the hub mass does not, because it carries the platform's share, and that
       is the one figure in the eight a reader would wrongly call inconsistent.
```

**ER1(c)'s no-STOP, independently again, and the two densities F3.md now publishes:**

```
cmd    python <scratch>/p4.py  (build_superstructure(mass_fraction=0.75) + admissible())
out    platform PSD=True  hub1..4 PSD=True          <- all five, so ER1(c) does not STOP
out    hub rho_eq = 11433.544762348803             <- F3.md publishes 11433.5. Confirmed.
out    platform rho_eq at the OLD 10 kg = 3572.982738234001
judge  the platform's figure doubles with the mass to 7145.965476468, which is F3.md's
       `7146.0`. Both recorded densities check out, and the hubs' above-steel equivalent
       density is a reported finding per ES1 and not a STOP -- I agree with that ruling.
```

**R690 CLOSED.** Every directive I have been judging commits against is now readable:

```
cmd    for d in EQ0..EQ4 ER0..ER3 ES0..ES3; do grep -c "\*\*$d" docs/milestones/F4.md; done
out    all thirteen return >= 1. ER0 and ES1 also appear in docs/milestones/F3.md.
judge  the hand-back is right that this was about my ability to do the job, and it is
       fixed. F3.md recording ER0 rather than editing DY0's rows is the right call for
       the reason it gives: F3 is closed and its figures describe the basis it was
       verified on.
```

## Findings

**No new blocking finding this round.** Verdict 98's three items are closed, nothing in
the diff is a CZ0 (a), (b), (c) or (d), and I am not inventing a head to fill this
section. The three rulings I was asked for, numbered so they can be cited:

**Ruling 1 -- ER0 is a recorded input change and needs no re-lock. NO STOP.** Section 5.
The ground is that Â§ 0 names the mass only by reference to the deck and DY0; the EH2
citation at `F4.md:150` is the wrong authority, and that is prose, not a gate.

**Ruling 2 -- of the two percentages, `50.0%` is the one that belongs, and the
mislabelling was MINE.** Both are arithmetic on the same band and both reproduce:

```
cmd    python <scratch>/p3.py
out    band [4.210526e-06, 5.789474e-06], ratio 1.3750
out    linear position of 5.0e-6 in that band:            50.0%
out    (counter - ceiling)/(counter - max|d|):            86.4%
judge  `86.4%` is the ceiling's position in `[max|d|, counter]`, which is a DIFFERENT
       interval from the pinned band. Verdict 98 wrote it as "86.4% of the way up its
       own legal band" and that label is false of it; I withdraw the label, not the
       number. The entry carrying both with their formulas is truthful and I accept it
       as shipped; at the next edit of that entry the `86.4%` should go, because a
       reader who needs one number needs the position in the band that pins the value.
```

**Ruling 3 -- the counter's missing upper pin is structural, not a defect.** Verdict 98's
tolerance table listed "the absence of any upper pin (direction B2: it may rise to `1e6`
with nothing red)" under R693, and the new entry does not address it. I rule it closed
without an edit, and the reason is general enough to be worth writing down: a counter-case
is never pinned from above by its own assertion, because a larger injected defect is
always detected. What pins it from above is its DERIVATION -- "one whole unit in the fifth
decimal place" is the smallest error that changes what the specification prints, so the
value is a definition and not a sample. The measured room between the boundary and that
definition is `1.0857x`, which is the tightest such margin in the table. Nothing to fix.

## Tolerances touched

```
cmd    git diff 4615498..HEAD -- floatfea/tolerances.py | grep -E '^[+-]'
         | grep -v '^[+-][+-]' | grep -vE '^[+-]\s*#'
out    (empty). Every changed line is a comment. NO VALUE MOVED, in this file or anywhere.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | `1.0e-5` | `1.0e-5`, unmoved | dimensionless, one unit in the fifth printed place | is the counter; injected by `test_R653_a_COEFFICIENT_WRONG_IN_THE_LAST_PRINTED_PLACE_reddens_the_gate` | `docs/milestones/F4.md:446`; entry at `floatfea/tolerances.py:2031-2062` | **R693 CLOSED.** All four ratios reproduce exactly on my instrument: `counter/ceiling 2.0000`, `ceiling/max|d| 1.1875`, `(max|d|+ceiling)/ceiling 1.8421`, `counter/(max|d|+ceiling) 1.0857`, with `C* = max|d| + ceiling = 9.2105263e-06`. The invariance sentence is gone and what replaced it is true of the ratio it is true of. "Thin by construction" is corrected to the measured `inf / 1.1250x / 1.1875x` across `rho_inf`. Both EH4 edges are in the entry and the band `[4.210526e-06, 5.789474e-06]` is `1.3750x`, which I re-solved. `C*` is named as the expression `max|d| + ceiling` with both terms pasted rather than as the digits; that determines it, and I accept it as satisfied rather than spending a round on the form. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.05`, unmoved | dimensionless | is the counter, still injected on one member | `docs/milestones/F4.md:447` -- **now candid: "R682 OPEN: this value sits above the defect on 12 of the 16 members"** | **R691 CLOSED.** The row's three false figures are withdrawn and replaced by `1/19`, `1/24` and `smallest measured 0.04166666666666627`, all three of which I reproduced on all sixteen members to the last digit, including the `12 of 16`. The VALUE stays held by ER2, and that hold stays accepted. |

## Carried

Verdict 98 left **three findings and three carried items** open. Every one, with status:

* **R691 -- ANSWERED. CLOSED.** Section 3. `docs/milestones/F4.md:447` and
  `test_f4_static_and_mapping.py:549-551` both carry `1/19` and `1/24`; I measured both on
  all sixteen members, and the plan row's `0.04166666666666627` and `12 of 16` as well.
  **One site of my own condition WITHDRAWN with its measurement:** `:520` states the two
  correct root moments, both reproduce to every digit, and it never carried the false
  ratio. The site-by-site miss is recorded at the end of section 3 and does not block.
* **R692 -- ANSWERED. CLOSED.** Section 4. `compared == _CHANNELS` with `_CHANNELS = 10`
  declared and derived. All sixteen single-block rows move GREEN -> RED, the dense control
  stays GREEN, and I solved the weakening edge as well: k = 4 blocks is the boundary, 175
  of 1820 four-block rows still pass, and I rule those correct passes with the reason.
* **R693 -- ANSWERED. CLOSED.** The tolerances table above. Four ratios named individually
  and every one reproduced; the invariance sentence restated as the definition it is; both
  EH4 edges and the `1.3750x` band pasted; "thin by construction" corrected. The `50.0%`
  vs `86.4%` question is ruled in Ruling 2 and the mislabelling was mine.
* **R690 -- ANSWERED. CLOSED.** Section 5. All thirteen of EQ0-EQ4, ER0-ER3 and ES0-ES3
  are now readable in `docs/milestones/F4.md` Â§ 0, with ER0 and ES1 also in `F3.md`. I was
  judging commits against three directives I could not read; I can read all of them now.
* **R682 -- STILL OPEN, hold accepted, unchanged in substance.** The basis-INDEPENDENT
  half is now done at every site. The VALUE is held by ER2's ordering, which is right:
  `1/19` and `1/24` both move with `f` and with `M`, and ER0 moves both. Not held against
  this diff.
* **R685 -- STILL OPEN, hold accepted without reservation.** `tolerances.py` carries no
  change for it in this range and nothing about it has moved. Not held.
* **EG3(ii)** -- state (1) cleared at `7f822ba`, measured in section 2. State (2) is the
  implementer's to measure at the next report commit, and my figure for it to beat is in
  "Next step opens when".

Closure items C161 to C173 and the earlier C-items: **not reviewed this round.** ES0
excludes the closure list from an interim check and I did not look at them. The one
closure-class thing I found while measuring is the EH2 citation in section 5; it is one
line, it is recorded there, and it is explicitly not a list to work through.

## The adversarial corpus (BE3)

**No new corpus file this round, and the number is still reported.** EG4(e) pauses batches
until 28 October except for mutation work on F4's load-mapping gate, and ES0's scope for an
interim check excludes a batch. The exception covers exactly the gate in front of me, so I
spent it on measurement rather than on a file: 16 single-block multiplier rows and 1820
four-block rows, generated by exhaustion rather than by choosing shapes.

* **16 new mutation rows against G4.4, 16 of 16 now caught** (they were 0 of 16 before
  `7a40758`, and that is the whole content of R692).
* **1820 four-block rows, 0 caught, and 0 SHOULD be caught** -- section 4 gives the
  reason, and the measurement is what turns "the gate is fine on sparse rows" from a
  belief into a boundary at k = 4.

Entries new to `tests/corpus/`: none. Previous batch: 36, at `4f99c7f`.

## Next step opens when

**STEP 2 STAYS OPEN, and nothing in it is blocked on me.** This check counts against NO
round, so **verdict 97 remains round 1 of three and TWO REVISIONS REMAIN**. Step 3 does not
begin. **ER1 should start now** -- all three of verdict 98's items are closed, ER0 needs no
re-lock, and there is no item of mine for ER1 to wait behind.

The next report revision is round 2, and these are what I will read it for:

1. **ER1 (a)-(e) and then EQ2's remainder, in ES3's order.** ER1(d) is the commit BP0
   governs: every figure and declared counter depending on `mu`, `M` or `f` re-derived in
   that commit, not the next. **My figures to beat, measured at `dc60ee9`:** platform
   `R = 6131250.0`, `wL = 4598437.5`, `Vz = 1532812.5`, `My = 191601562.5`; hub
   `R = 6948750.0`, `wL = 3678750.0`, `Vz = 3270000.0`, `My = 127734375.0`; all five bodies
   PSD at `f = 0.75`; `rho_eq` hub `11433.544762348803`, platform `7145.965476468` at
   20 kg.
2. **R682's VALUE, on the new basis**, with the per-member table that derives it. My
   figures on the OLD basis, which the new ones must supersede rather than contradict:
   `1/19` on 4 platform arms, `1/24` on 12 hub arms, smallest `0.04166666666666627`,
   counter above the defect on 12 of 16.
3. **R685**, as ER2 orders it.
4. **The sites of R691 that are declarations rather than edits** --
   `tests/test_plan_matches_tolerances.py`, `floatfea/tolerances.py:1990`, `CLAUDE.md` and
   `docs/SUPERVISOR.md` -- each named with the sentence saying it was left and why, which
   is what `test_every_named_site_is_touched_or_declared` is red on and the one half of
   this round's 84 that the revision itself clears.
5. **EG3(ii)** -- the report-guard files run AT `dc60ee9` and the counts pasted. **My
   figures: 84 failed, 2951 passed, 0 skipped whole-suite; 84 failed, 187 passed on the
   three guard files; the same 84 ids in CI run `37497138919`.** Any red outside EH1's and
   EJ2's state (2) list is CZ1 (iv) unchanged.

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION.** A closing condition answered at a
different set of sites than the one it named, reported as the same number of sites --
section 3 is the fourth appearance of that shape in five verdicts, and this time the tree
was clean only because I measured the site myself. A figure from ER1(d) taken before the
final edit to the artifact that carries it; CP3 is the rule, and six FloatSim re-runs is
exactly the shape that invites a remembered number. And an ER1(d) figure without the cell
that isolates it (BG0) wherever the sentence says the new basis *caused* something to
move: the basis moves two inputs at once -- `M` and `f` -- and a figure credited to one of
them needs the one-at-a-time pair.

## On the schedule

The hand-back reports ER1 at two days and the working targets as F4 14 Oct, table 17 Oct,
code-check 22 Oct, committed dates unchanged. Nothing in this verdict adds to that: there
are no blocking items to answer, so ER1's two days start today rather than after a repair.
**I see no slippage to report that the hand-back has not already reported.** If ER1(b)'s
six re-runs overrun, that is reported the day it is known, per Â§ Step gating.

## On ES0's scope -- I was asked, and this is not a second round of the same argument

I agree with ES0 and said so once in verdict 98; I do not reopen it. Its scope was right
for THIS diff in particular, and the reason is measurable: the entire executable surface of
two commits is one assertion operator and four comment lines, and a full round against that
would have spent a third of this step's allowance on a diff with no code in it.

One observation to add to the one already recorded, not a request. This hand-back DID carry
`claim/cmd/out` triples for its repairs and both EH4 directions for R693, which is the
thing verdict 98 said would recover the reading cost -- and it worked. Three of five
judgements last round came out of measurements the hand-back did not contain; this round
every figure I needed was in it, and my job was to reproduce rather than to construct.
That is the version of an interim check that is cheaper for both sides.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: 46154986ac3b129d9bb9d1cf8c0bd6d05f7582a6
Verdict: HOLD

**Reviewed commit: `4615498`.** (`46154986ac3b129d9bb9d1cf8c0bd6d05f7582a6`, HEAD of F3,
pushed.) Range `488f2d8..HEAD` -- two commits.
Tests: 2988 passed, 32 failed, 0 skipped (MY OWN run, one invocation, no `--ignore`, no
`-k`, no deselection, in the repository itself, 639.53s. **All 32 are EG3 state (2) and
each is traced by name in section 2.**)
**CI at the reviewed commit: run `37492421362` at `4615498`, conclusion FAILURE.**
`the verification ladder: success` at EVERY step -- `ladder 1`, `2`, `3`, `6`, `4`, `5`.
`lint, unit and guards: failure` at `guards and meta-tests` ONLY; `actionlint`, `ruff`,
`black --check`, `mypy` and `unit tests` all success. `32 failed, 998 passed in 328.27s`
-- the same 32, same ids. NOT CK2: `runner_name` is `GitHub Actions 1000001531`, the steps
ran, the durations are real.

## Round of 2026-10-06 -- ES0 INTERIM CHECK. Counts against NO round.

**ES0's premise verified before anything else, because the exemption rests on it.**

```
claim  there is no new report revision -- the report is the one verdict 97 judged
cmd    git log --format='%h %s' -1 -- docs/reports/F4/step-2.md
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), ...
judge  7cee09f is the commit verdict 97 judged. The report has not moved. This is an
       interim check, it counts against no round, verdict 97 stands as round 1 of 3,
       and TWO REVISIONS REMAIN.
```

**Instruction 1b does not fire, and I say so rather than leaving it silent.** The report's
header reads `Answers: verdict 96 @ 5786bed` and the newest verdict is 97. Under 1b that
comparison is a HOLD. It is not one here: 1b guards against a report that answers a
superseded round, and a report that PREDATES the newest verdict with no revision between
them is EG3 state (2) -- designed, self-clearing, and the exact state ES0 exists to
permit. The distinction is the same one DD1 draws between an open step and a step file.

**I accept ES0's scope and I have held to it:** the suite, CI, and a CZ0 (a)-(d) scan of
`488f2d8..HEAD`. No corpus batch. No closure list -- section 6 records the three
closure-class things I found so they are not lost, as single lines, explicitly not as a
list to work through.

**HOLD, on three items, two of which are repairs that stopped one site short of their own
closing condition.** R686 is ANSWERED and I reproduced it in both directions plus a third
the condition did not ask for. R687 and R688 are answered on the branches they took.
**R689 is HALF answered and R682 is not answered on the branch the hand-back says it
took** -- and both are the same shape, the shape `CLAUDE.md` records under *A closing
condition that names sites is closed site by site*. That rule was earned by R29. This is
its third instantiation in four verdicts.

**No STOP.** The ladder is green at every rung in CI. `4615498` is the permitted form for
touching my own instructions and I confirm it in section 1 as I was asked.

## 1. MY OWN INSTRUCTIONS, AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 488f2d8..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 31 +++++++++++++++++++++++++++++++
out    (.claude/ -- nothing)
cmd    git log --format='%h %s' 488f2d8..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    4615498 process: ES0 -- rounds are counted per report revision; an interim check
out            counts against none
```

**`4615498` IS THE PERMITTED FORM. NOT A STOP-CLASS FINDING.** Four conditions, each
checked rather than inferred:

```
claim  standalone -- it touches nothing but the two instruction files
cmd    git show --stat 4615498
out    CLAUDE.md | 31 +++ ; docs/SUPERVISOR.md | 31 +++ ; 2 files changed, 62 insertions(+)
claim  zero deletions, so no guard was removed
out    62 insertions(+), 0 deletions -- and I read the 31 lines; they are additive
claim  it cites the directive asking for the change, in its first line
out    "process: ES0 -- rounds are counted per report revision ..."
claim  the two inserted regions are byte-identical, which the commit message asserts
cmd    git diff 488f2d8..HEAD -- <file> | grep '^+' | grep -v '^+++' | sed 's/^+//' ; md5sum
out    8a6ad471294c2c4cfc1886bb3ed6ee14  (CLAUDE.md)
out    8a6ad471294c2c4cfc1886bb3ed6ee14  (docs/SUPERVISOR.md)
out    diff: no output. BYTE-IDENTICAL.
```

Same ruling as `9985bcd`, on the same four grounds, and I checked it the same way rather
than carrying the earlier ruling across.

```
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                   <- non-empty, so the pathspec is the CI0 one
cmd    git diff 488f2d8..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty). No conftest changed. No new plugin. CH2 clear.
```

## 2. THE 32 REDS, EACH TRACED BY NAME (EG3(i), CA2)

EG3(i) is explicit that a family is not a trace. Each id, matched against EH1's and EJ2's
corrected **state (2)** list:

| count | id | on the list as |
|---|---|---|
| 17 | `test_every_named_site_is_touched_or_declared[R686/R687/R688/R690-...]` | named, state (2) |
| 5 | `test_the_report_carries_the_finding[R686..R690]` | named, state (2) |
| 1 | `test_the_CI_section_is_about_the_REVIEWED_commit` | named, state (2) |
| 1 | `test_the_Carried_table_is_what_the_generator_produces` | named, state (2) |
| 1 | `test_the_generator_would_catch_a_row_under_the_wrong_number` | named, state (2) |
| 1 | `test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` | the red baseline |
| 6 | the six planted states | the cascade, by failure line |

**The cascade is identified by each state's OWN failure line and not by its name**, which
is the R629 discipline:

```
out  [baseline] AssertionError: baseline: expected a clean run.
out  [verdict_amended_after_the_commit_the_report_answers] ... expected a clean run.
out  [non_numeric_step_suffix]           ... must be stepped over, not reacted to.
out  [superscript_digit_step_number]     ... must be stepped over, not reacted to.
out  [draft_suffix_beside_a_step_report] ... must be stepped over, not reacted to.
out  [step_number_is_the_empty_string]   ... must be stepped over, not reacted to.
out  [zero_padded_step_number]           ... must be stepped over, not reacted to.
```

Every one of the six asserts against a clean baseline and the baseline is dirty.
17+5+3+1+6 = 32. **Nothing is outside the list, so CZ1 (iv) does not fire and this is not
a (d).**

**EG3(ii), the half no verdict has measured -- state (1) DID clear at my verdict commit.**
`test_the_guard_reads_the_step_being_worked_on` was the cause of all eight reds at
`7cee09f` and it is absent from the 32 above. `488f2d8..4615498` touches neither the report
nor the verdict, so the measurement at `4615498` is the measurement at `488f2d8`:

```
cmd    git diff 488f2d8..HEAD --stat -- docs/reports docs/reviews
out    (empty)
out    test_the_guard_reads_the_step_being_worked_on: NOT in the FAILED list. CLEARED.
```

## 3. WHAT I REPRODUCED RATHER THAN READ

**R686 -- ANSWERED, and the repair is bidirectional, which is more than the condition
asked.** I ran the ablation myself, in both directions and in a third:

```
cmd    python <scratch>/r686.py  (pytest rung4 + tests/test_no_tolerance_literals.py)
out    as shipped (deck 0.8)              88 passed
out    deck key -> 0.9                    1 failed  RED test_R653_the_DECK_and_the_DECLARATION_agree...
out    deck key -> 0.85                   1 failed  RED (same)
out    deck key -> 0.8000001              1 failed  RED (same)   <- `==`, no slack
out    declaration -> 0.9, deck untouched 2 failed  RED (same) + RED ..._FloatSims_DEFAULT_reddens...
out    deck key DELETED                   1 failed  RED (same)   <- raises, never defaults
out    deck restored: True
rule   editing EITHER side must redden; a missing key must raise, not default
```

That is the EB6 shape and it is the real one. The literal left the comparison entirely
rather than being re-marked, which is the right fix and not the cheap one. **R686 closed.**

**R687 -- ANSWERED on the branch it took, and I note what that branch costs.** Branch A of
the three I offered: the ranges the scheme actually attains, with both closed forms and
both crossover values pasted, and the false sentence gone from both sites (the marker
comment is deleted; the assertion message is rewritten). `rho_inf = 0.2` is now walked, so
the value my finding was about is exercised. **Closed as offered.** The measurement of what
the branch buys is in section 6; it is not a reopening.

**R688 -- ANSWERED on the branch it took.** The window is declared, with a counter, with
two plan rows in the same commit, and the word "exact" is gone from the docstring. The
reference resolves:

```
cmd    sed -n '255,263p' docs/load-interchange-v1.md
out    line 259: alpha_m = 0.42105     alpha_f = 0.47368     difference 0.05263
judge  `_DOC_DIFFERENCE = 0.05263` and its "at line 259" both resolve. Citation good.
```

The per-channel figures the hand-back pastes are correct, and they are **a different
quantity from the four in my R688** -- mine were the drift `round(x,5)` still ACCEPTED
(distance to the quantisation edge, governing `7.895e-07` on `alpha_f`); these are
`|exact - published|` (governing `4.210526e-06`, also on `alpha_f`). Both right. The
hand-back's sentence "Per-channel drifts reproduce yours" is false -- they are not the same
numbers and could not be -- and it is section 6's third line, not a blocking item. What IS
blocking is the bracket figure: R693.

## 4. R689 -- HALF ANSWERED. I SOLVED THE THRESHOLD AND THE VACUITY IS STILL THERE.

The all-zero row is closed and I reproduced it. The COUNT is not, and `compared > 0` is a
nonzero-check wearing a count's name. Inverting the decision rule rather than sampling one
side of it:

```
cmd    python <scratch>/r689.py  (the production gate's own helpers, built fixture, real mapper)
rule   the shipped pair: `_channels_compared(...) > 0` and
       `max(per_body) < F4_MAPPING_CONSERVATION`
out    dense in all 16 blocks  blocks 16/16  compared 10/10  err 2.196e-16  GREEN  <- control
out    zeros everywhere        blocks  0/16  compared  0/10  err 0.000e+00  RED    <- R689, closed
out    only block  0 (buoy1)   blocks  1/16  compared  2/10  err 0.000e+00  GREEN
out    ... every one of blocks 0-11 (the twelve buoys)  compared 2/10  GREEN
out    ... every one of blocks 12-15 (the four hubs)    compared 4/10  GREEN
out    ALL SIXTEEN single-block rows read GREEN. The minimum is 2 of 10 channels.
out
out    `compared >  0`: 16 of 16 degraded rows still GREEN
out    `compared >  1`: 16 of 16 still GREEN
out    `compared >  2`:  4 of 16 still GREEN
out    `compared >  3`:  4 of 16 still GREEN
out    `compared >  4`:  0 of 16 -- EVERY degraded row reddens       <- the boundary
```

So the threshold that closes the item is `compared > 4`, equivalently `compared == 10`, and
`> 0` sits four below it. My condition read "asserts the COUNT of bodies compared
relatively -- equivalently that the lam row is nonzero in all sixteen blocks", and I named
the pattern: "that is the `checked == 16` pattern this file already uses twice". A floor of
one channel out of ten is not the count. The coverage still degrades invisibly, which is
the sentence the condition was written against.

## 5. R682 -- NOT ANSWERED. THE FALSE ARITHMETIC SURVIVES AT TWO OF THREE NAMED SITES.

```
cmd    grep -rn '1/18\|5\.555556e-02\|1\.0550e+14\|114960937\|6386718' --include=*.py --include=*.md .
out    floatfea/tolerances.py:1990-1991  -- DELETED as false. Site 1 of 3. DONE.
out    docs/milestones/F4.md:348         -- STILL THERE. Site 2 of 3.
out    tests/verification/rung4/test_f4_static_and_mapping.py:549 -- STILL THERE. Site 3 of 3.
out    tests/verification/rung4/test_f4_static_and_mapping.py:520 -- a fourth, same arithmetic.
out    (CLAUDE.md:274 and docs/SUPERVISOR.md:438 quote the figure AS WRONG. Correct.)
```

R682's closing condition named three sites and I said so again in verdict 97 ("R682's
condition names three sites"). One was answered. This is R691.

## Findings

**R691. (b, blocking) R682's FALSE ARITHMETIC IS DELETED FROM `tolerances.py` AND LEFT
STANDING IN THE PLAN ROW THAT IS THE SAME COUNTER'S LOCATED JUSTIFICATION -- BY THE SAME
COMMIT, IN A TABLE THAT COMMIT EDITED TWO LINES ABOVE.**
`docs/milestones/F4.md:348` and `tests/verification/rung4/test_f4_static_and_mapping.py:549`
(and `:520`). The plan row reads `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 | ... R663's
mu L^2 / 12 over the root moment -- exactly 1/18 on a platform arm, measured 5.555556e-02,
bracket 1.0550e+14x`. `floatfea/tolerances.py:1990` now says of that exact sentence:
"**Both halves are false and they are deleted rather than left standing while the repair
waits (ES2)**", and gives `1/19` and `1/24` as the ratios in the gate's own denominator.
**The two authoritative locations for this counter's justification now contradict each
other inside one commit**, and `docs/SUPERVISOR.md` item 4 is the reason that is (b) rather
than prose: a tolerance change needs "a justification located in `docs/milestones/F<n>.md`
or the closure artifact", and a justification known by the same commit to be false is a
missing one. I checked the arithmetic rather than taking either side: if the correct root
moment is `M` and the defect adds `M/18`, then `(M/18)/(M*19/18) = 1/19` exactly --
`tolerances.py` is right, the plan row is wrong, and `1/18` is the ratio against the
CORRECT root moment, which is not the quantity the assertion divides by. The plan row's
`1.0550e+14x` bracket is the same figure verdict 96 measured as `9.9950e+13` against the
injected member and `7.9127e+13` against the worst. `test_f4_static_and_mapping.py:549` is
worse than stale, because it names the right denominator and the wrong number: "against the
DEFECTIVE root moment this ratio uses is 1/18 of the root moment on a platform arm."
Nothing caught this: `tests/test_plan_matches_tolerances.py` compares the row's VALUE
against the declared constant and never reads the row's prose.
**Closed when** `docs/milestones/F4.md:348`, `test_f4_static_and_mapping.py:549` and `:520`
each carry the `1/19` / `1/24` figures or no figure at all, and the `1.0550e+14x` bracket is
re-measured or withdrawn. This is basis-INDEPENDENT -- the deleted claim does not depend on
`f`, only the VALUE does, and the hold on the value stays accepted. **OR** each of the three
sites is named in the next revision with the sentence saying it was left and why, which is
the branch `CLAUDE.md` section *A closing condition that names sites* offers. What I will
not accept a third time is R682 reported as answered on its prose branch while two sites
carry the sentence.

**R692. (c, blocking) `compared > 0` IS R689's CLOSING CONDITION MINUS ITS COUNT. ALL
SIXTEEN DEGRADED ROWS STILL READ GREEN AND I SOLVED THE THRESHOLD.**
`tests/verification/rung4/test_f4_static_and_mapping.py`, the `assert compared > 0` at
`:865-871` inside `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`. Measurements in
section 4: the all-zero row now reddens (the half verdict 96 asked for, and it is real --
I reproduced the control green and the injection red), and every one of the sixteen
single-block rows reads GREEN at **2 of 10 channels compared** for the twelve buoy joints
and **4 of 10** for the four hub joints. Solving the rule rather than sampling it,
`compared > 4` is the smallest threshold at which every degraded row reddens; the shipped
`> 0` sits four below it, and `> 1` buys nothing at all. The gate's coverage therefore
still rests entirely on `_synthetic_lam` being dense in all sixteen blocks -- the
`:769`-class sentence my R689 named as the CW0 shape -- and that premise is still asserted
in prose and checked nowhere.
**Closed when** the assertion is `compared == 10` (or the equivalent all-sixteen-blocks
density check) with the `2 of 10` / `4 of 10` figures and the `compared > 4` boundary
pasted as what it prevents. One character of the assertion, and it makes the `:769`
sentence true by assertion in the same edit, which is what I asked for the first time.

**R693. (b, blocking) THE NEW COUNTER'S BRACKET IS PUBLISHED AS `2x` AND MEASURES
`1.0857x`, AND THE SENTENCE SAYING NO MEASUREMENT CAN CHANGE THAT RATIO IS REFUTED BY
ONE.**
`floatfea/tolerances.py`, the `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` entry: "**Twice the
ceiling, which is the most a printing-precision window can ever be bracketed by**: the
ceiling is half a unit and the counter is one unit, and **no measurement can change that
ratio**." The counter-to-ceiling ratio IS 2.000000 and that arithmetic is right. It is not
the bracket. This repository's own usage of "bracket" is the margin by which the gate
DETECTS the counter -- the deleted sentence four entries above used it that way ("The
bracket is 1.0550e+14x"), and so does every other entry in the table. Solved, not sampled:

```
cmd    python <scratch>/tol_boundary.py
rule   the counter-case asserts, for all four channels,
       abs(exact - (published + C)) > F4_INTEGRATOR_SPEC_AGREEMENT
out    clean abs(exact - published): alpha_f 4.210526e-06   alpha_m 2.631579e-06
out                                  beta  -1.689751e-06    gamma  1.578947e-06
out    bisected boundary C* = 9.2105263e-06  ( = max|d| + ceiling; closed form confirms)
out    shipped counter 1.0e-5 clears C* by 1.085714x    <- THE DETECTION BRACKET
out    the entry claims the bracket is "twice the ceiling" = 2.0x
```

And the invariance claim, refuted by one measurement because `C* = max|d| + ceiling` and
`max|d|` is a property of the four exact values, not of the print precision:

```
out    rho_inf 0.90: max abs(exact - its own 5dp print) 4.210526e-06 -> bracket 1.0857x
out    rho_inf 0.20: 4.444444e-06 -> C* 9.444444e-06 -> bracket 1.0588x
out    rho_inf 0.00 and 1.00: max|d| = 0 -> C* = 5.0e-06 -> bracket 2.0000x
judge  a measurement does change that ratio, and the same table shows it ranging
       1.0588x to 2.0000x over the scheme's own parameter.
```

**EH4, both directions, which the hand-back's sweep took only one of.** It reported
`7.0e-6, 9.9e-6` reddening the counter-case; the BOUNDARY is `5.789474e-06`:

```
out    DIRECTION A (strengthening): the ceiling FALLS -> the clean gate trips below
out                    4.210526e-06 (4.2105264e-6 passes, 4.21e-6 RED)
out    DIRECTION B (the WEAKENING one): the ceiling RISES -> the counter-case stops
out                    detecting at 5.789474e-06 (5.7894e-6 detects, 5.79e-6 does not)
out    => the ceiling is PINNED into [4.210526e-06, 5.789474e-06], a band of 1.3750x,
out       and the shipped 5.0e-6 sits 86.4% of the way up its own legal band.
out    DIRECTION B2 (the injection RISES): counter 1e-5, 2e-5, 1e-4, 1e-2, 1.0, 1e6
out       -- all still "detected", NOTHING reddens. The counter is pinned only FROM BELOW.
```

**The ceiling's VALUE is right and I am not asking for it to move.** `5.0e-6` is the
principled half-unit, it is absolute on a genuinely dimensionless quantity so the absolute
form is correct and the entry says why, the two plan rows landed in the same commit, and
the band `[4.210526e-06, 5.789474e-06]` is the tightest bracket in this table. **What is
wrong is the arithmetic published about it**, and the entry is the only statement a reader
has of what that counter bounds.
**Closed when** the entry gives the detection bracket `1.0857x` with `C* = 9.2105263e-06`
named as the boundary, the invariance sentence is deleted or restated as the thing that IS
invariant (the counter/ceiling ratio of exactly 2, which is a definition and not a
bracket), and the ceiling's band `[4.210526e-06, 5.789474e-06]` is pasted so a later
reader sees it pinned from both sides instead of sampled from one. Section 6's third line
notes the separate sentence "That margin is thin BY CONSTRUCTION"; fold it into this edit.

## 6. RECORDED, NOT A CLOSURE LIST -- ES0 PUTS THE LIST OUTSIDE THIS CHECK

Three lines so they are not lost. **None of these holds the step and none is to be worked
through this round.** CZ0 classes them as closure items; I agree with the classification,
and I give the reasoning for the first because I was asked to rule on it.

1. **The dict is LEGITIMATE as to its four numbers, and it escapes the guard rather than
   being exempted by it.** `_COEFFICIENT_RANGES` at
   `test_f4_static_and_mapping.py:1017-1036`. Verdict 97 already ruled the numbers are not
   tolerances -- they bound a computed quantity, there is no slack -- so the FORM is right
   and the derivation in the docstring is correct and complete. **It is not a dodge.** The
   part the hand-back did not ask about is what I measured, with the flat literal and the
   module-level float NAME as controls so the probe carries its own failure:
   ```
   cmd  python <scratch>/probe_dict.py   (tests/test_no_tolerance_literals.py::offending)
   out  CAUGHT  bare literal                               <- control
   out  CAUGHT  module-level float NAME (the :497 clause)  <- control
   out  MISSED  module-level DICT of floats, unpacked
   out  MISSED  assert residual < RANGES["r"]              <- a REAL tolerance, subscripted
   out  MISSED  module-level TUPLE, indexed
   out  MISSED  LO, HI = 3.7e-9, 2.2e-3   then   LO <= v <= HI
   out  MISSED  the SHIPPED shape, verbatim
   ```
   So it is invisible to the guard, which is a different and larger thing than a dodge: the
   `:497` clause exists because "a module-level `NAME = <float>` used as a threshold is a
   local literal wearing a name; the indirection is the point of the clause", and a
   container is the same indirection one level down. The docstring routes unread species to
   `tests/test_marker_exemption_corpus.py`; grepping that file for dict, tuple, container
   or subscript returns nothing, so the routing claim does not cover this form. **DR1
   forbids extending the guard and I am not asking for that.** The repair that costs one
   line and no apparatus: a `not-a-tolerance:` marker on the dict assignment, which
   restores the audit trail a reader greps for. It is free -- there is no unused-marker
   guard, so an unconsumed marker is simply ignored.
2. **`test_R653_the_coefficients_are_the_CLOSED_FORM_at_the_declared_radius` does not check
   a closed form and checks nothing AT the declared radius.** `:1114`. R687's condition is
   MET and this is not it reopened. Measured against nine wrong closed forms: the range
   gate catches 6 and is blind to 3 -- `beta = 1/(1+r)` with the square dropped, the
   Newmark trapezoid `beta=0.25, gamma=0.5`, and `alpha_m = (r-1)/(r+1)`. The spec pin
   above it catches all nine, so the pair's reach is the pin's reach. The name states a
   property the test cannot fail on, which is the shape R686 was, one finding earlier.
   Renaming it to what it asserts costs one line.
3. **Two sentences, and one claim I could not reproduce.** "Per-channel drifts reproduce
   yours" in the hand-back -- a different quantity from my four, and both sets are right
   (section 3). And `tolerances.py`: "That margin is thin BY CONSTRUCTION" of the
   `1.1875x` -- the margin is `ceiling / max|d|` and `max|d|` is measured, giving `inf` at
   `rho_inf` 0 and 1, `1.1250x` at 0.2/0.5/0.8, `1.1875x` at 0.9. It is thin by
   measurement. BG0; fold into R693. **Not reproduced:** the `black`-moves-the-marker
   fragility the hand-back flagged. I built a marked assertion long enough to force a
   reflow; `black -l 100` left the marker on the comparison's line and `offending()` read
   CLEAN before and after. Recorded as unverified, not as refuted -- a different shape may
   do it.

## Carried

Verdict 97 left **five findings and two carried items** open. Every one, with status:

* **R686 -- ANSWERED.** Section 3, reproduced in both directions plus the deleted-key case.
  `integrator.py:rho_inf_from_deck`, `scripts/report_joint_reactions.py:77`,
  `test_f4_static_and_mapping.py:1058-1112`. My figure to beat was `212 passed` with the
  deck at `0.9`; it now reddens. **Closed.**
* **R687 -- ANSWERED on branch A, as offered.** Both false sentences out of both sites; the
  ranges `[0.25, 1.0]` and `[0.5, 1.5]`, the two closed forms and the crossovers
  `sqrt(2)-1` and `1/3` all pasted; `rho_inf = 0.2` walked. **Closed.** The name is
  section 6 item 2 and is not this item.
* **R688 -- ANSWERED on the branch it took.** `F4_INTEGRATOR_SPEC_AGREEMENT = 5.0e-6`
  declared, counter declared, two plan rows in the same commit, "exact" gone. **Closed**,
  and the bracket arithmetic inside the answer is **R693**.
* **R689 -- HALF ANSWERED. STILL OPEN as R692.** The all-zero vacuity is closed and
  reproduced; the COUNT conjunct is not, and I solved the threshold.
* **R690 -- STILL OPEN, NOT HELD** (it never was). Grepping
  `docs/milestones/F4.md` for ER0, ER1, ER2, EQ2, EQ3 and EQ4 still returns nothing, and
  the only plan change in this range is the two section 5a rows. ES0 and ES2 have now
  joined the list of directives I can read only through a hand-back -- ES0 is in the
  repository, which is why I could verify it in section 1; **ES2 is not.** Unchanged in
  substance: the text goes in before ER1(d) derives anything from the new basis.
* **R682 -- STILL OPEN, AND NOW ALSO R691.** The hold on the VALUE stays accepted
  (basis-dependent through `f`, ER0 moves `f`, ER2's ordering is right). The
  basis-INDEPENDENT half was taken at one of three named sites. Section 5.
* **R685 -- STILL OPEN, hold accepted without reservation.** `tolerances.py` is untouched
  for it in this range and nothing about it has moved. Not held.

Closure items C161 to C173 and the earlier C-items: **not reviewed this round.** ES0
excludes the closure list from an interim check, and I did not look at them.

## Tolerances touched

```
cmd    git diff 488f2d8..HEAD -- floatfea/tolerances.py
out    two new entries, one deleted justification paragraph, and nothing else.
out    No existing VALUE moved -- the diff contains no changed `Final[float] =` line.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_INTEGRATOR_SPEC_AGREEMENT` | none | `5.0e-6` | absolute, dimensionless -- correct here; the quantity is a pure number and the entry says there is nothing to be relative to | `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | `docs/milestones/F4.md:346`, same commit; entry at `tolerances.py:2007-2026` | **VALUE ACCEPTED.** Band `[4.210526e-06, 5.789474e-06]` solved in both directions, `1.3750x`, the tightest in this table. Passes the unit-scaling question non-vacuously because the quantity is genuinely dimensionless. The published bracket is **R693**. |
| `F4_INTEGRATOR_SPEC_AGREEMENT_COUNTER` | none | `1.0e-5` | dimensionless, one unit in the fifth printed place | is the counter; injected by `test_R653_a_COEFFICIENT_WRONG_IN_THE_LAST_PRINTED_PLACE_reddens_the_gate` | `docs/milestones/F4.md:347`, same commit | **VALUE ACCEPTED** -- principled, not arbitrary, and it clears the boundary `C* = 9.2105263e-06`. **R693** on the bracket, the invariance sentence, and the absence of any upper pin (direction B2: it may rise to `1e6` with nothing red). |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `0.05` | `0.05`, unmoved | dimensionless | is the counter, still injected on one member | `docs/milestones/F4.md:348` -- **and that row is the false arithmetic the same commit deleted from `tolerances.py`** | **R691, blocking.** The `tolerances.py` paragraph is now correct and candid, and I say so: deleting a false sentence rather than leaving it standing while the repair waits is the right call and it is what I asked for. It was done at one site of three. |

## Next step opens when

**STEP 2 STAYS OPEN. This check counts against NO round, so verdict 97 remains round 1 of
three and TWO REVISIONS REMAIN.** Step 3 does not begin. ER1's six FloatSim re-runs may
proceed -- that is the whole point of ES0 and I am not obstructing it -- but these three
are answered in the same revision that carries ER1, before its own work is read:

1. **R691** -- `docs/milestones/F4.md:348`, `test_f4_static_and_mapping.py:549` and
   `:520`, **each named with its hunk or with the sentence saying it was left and why**.
   Basis independent; three edits. **My figures: `1/19` on a platform arm and `1/24` on a
   hub, in the gate's own denominator; `1/18` is against the correct one; the
   `1.0550e+14x` bracket measured `9.9950e+13` and `7.9127e+13`.**
2. **R692** -- `compared == 10` (or the all-sixteen-blocks density check) in
   `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`, **not** in the sparse test,
   which already has one. **My figures to beat: 16 of 16 single-block rows GREEN, minimum
   2 of 10 channels compared, boundary at `compared > 4`.**
3. **R693** -- the detection bracket `1.0857x`, the boundary `C* = 9.2105263e-06`, the
   ceiling's band `[4.210526e-06, 5.789474e-06]`, and the invariance sentence deleted or
   restated. Fold section 6 item 3's "thin BY CONSTRUCTION" into the same edit, because
   BP0 says a figure whose rule moved is regenerated in the commit that moves it, not the
   next.
4. **R682, R685, R690** -- carried, unchanged in substance. R690's text in the repository
   before ER1(d) derives anything from the new basis; **and ES2 with it**, since I have
   now judged two commits citing a directive that exists nowhere I can read.
5. **EG3(ii)** -- the report-guard files run AT my verdict commit and the counts pasted.
   The expected reds are EH1's state (2) list and nothing else; any red outside it is CZ1
   (iv) unchanged. **My figure at `4615498`: 32 failed, 2988 passed, 0 skipped, all 32
   traced in section 2.**

**WHAT I WILL NOT ACCEPT AT THE NEXT REVISION.** R691 reported answered with one or two of
the three sites touched -- the rule is site by site and this is its third instantiation in
four verdicts, so the next revision lists all three by path and line whatever their
disposition. A count assertion for R692 that is a floor rather than the count: `> 1`
through `> 4` are all still vacuous on 4 of 16 rows or more, and I have pasted the table.
And for R693, a replacement bracket figure taken before the final edit to the entry -- CP3
is the rule, and this round's one blocking tolerance finding is a bracket arithmetic
inside a repair, which is CP2's recorded shape for the fourth round running.

## On ES0's scope -- said once, and it leaves the loop

**I agree with ES0 and this is the once I say so.** The exemption keys on whether a new
report revision exists, which is a fact a machine can check and which distinguishes "the
work reached a reviewable state" from "a turn ended". That is a better discriminator than
the one I was applying in verdict 97, and the revision count answers DK0 cleanly.

One limit, recorded as an observation and not as a HOLD or a request. An interim check
reads a tree that **no report describes**, so every claim about it is one I had to
construct a command for rather than check against a written one, and three of this round's
five judgements came out of measurements the hand-back did not contain -- R691's third
site, R692's threshold, R693's boundary. That is more reviewer work per unit of code, not
less. If interim checks become frequent, the honest accounting is that the saving is in
the ROUND COUNT and not in the reading, and the thing that would recover it is cheap: a
hand-back for an interim check could carry the `claim/cmd/out` triples for the repairs it
describes, which this one largely did, and the boundary solved in both directions, which
it did not. Nothing follows from this; it goes to Xabier through the implementer if it is
worth anything.

## On the schedule

The three blocking items are, between them, one assertion operator, three prose edits and
one re-measured bracket -- a few hours, and none of them touches ER1. **ER1's two days are
not threatened by this verdict and should start now, in parallel.** I see no slippage to
report that the hand-back has not already reported.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 2
Reviewed commit: 4f99c7f6a3e446bc183b67bf0c77b91596e367c5
Verdict: HOLD
**Reviewed commit: `7cee09f`.** (`7cee09fdaac615519fe0da08c09d018f7438d0de`, HEAD of F3
at invocation, pushed.) My corpus commit `4f99c7f` lands first, so the script's
`Reviewed commit:` stamp and the judged commit differ; DU1 says restate the judged one
and this is it. The range is `5786bed..7cee09f` -- three commits.
Tests: 3022 passed, 8 failed, 0 skipped   (MY OWN run, ONE invocation, no `--ignore`,
no deselection, no `-k`, in the repository itself, 636.92s. I did not accept a count
from the report. **All eight are EG3 state (1) and traced by name in section 3.**)
**CI at the reviewed commit: run `37482781971` at `7cee09f`, conclusion FAILURE --
`the verification ladder: success` at every step including `ladder 4` and `ladder 5`;
`lint, unit and guards: failure` at `guards and meta-tests` ONLY, with `8 failed, 1038
passed`, and the eight are the same eight. `actionlint`, `ruff`, `black --check`,
`mypy` and `unit tests` all success.**

## Round of 2026-10-06 -- NINETY-SEVENTH verdict. F4 step 2, FIRST round of three.

**HOLD, and the first thing in it is the answer to the question I was asked, because the
implementer asked for it now rather than at the third verdict.**

**THIS ROUND COUNTS. It is step 2's first of three.** EB4's exemption is written for "a
verdict spent on a STOP or blocker whose resolution belongs to the supervisor or to the
user", and its second sentence limits the carry to POST-CLOSURE verdicts that judge
implementer work. Neither clause fits. This verdict judges three commits of step-2
implementer work -- `9985bcd`, `b979b68`, `7cee09f` -- and every finding in it is the
implementer's to fix. The OCCASION was a hook; the SUBJECT is the work, and EB4 keys on
the subject. Reading it the other way is the shape DK0 already rejected for plan
re-locks: if a mid-step commit bought a free round, every mid-step commit would buy one
and the cap would mean nothing.

**I think the mechanism that forced this round is wrong, and that is a separate
statement, made once, under its own heading at the end.** It goes to Xabier through the
implementer. It is not a HOLD on anything and the count above stands until he rules.

**R683 and R684 are substantively ANSWERED and I reproduced each by ablation rather than
accepting it** -- one red each, the right one, over the whole of rung 4. R653's FORMULA
half is answered and I checked the reference's own derivation independently. **The four
blocking items are all inside the new work, three of them inside R653's own answer**,
which is CP2's recorded shape for the third round running: the attention goes to the
thing being fixed and the apparatus built around the fix inherits none of the discipline
being applied to it.

**No STOP.** ER1(c)'s STOP condition does not fire -- I reproduced all five bodies PSD
at `f = 0.75` with `admissible()` itself (section 5). The ladder is green at every rung
in CI. And `9985bcd` is the permitted form for touching my own instructions, which I say
plainly because I was asked: section 2.

## 1. THE DIFFS, EACH ONE SEPARATELY, AS MY INSTRUCTIONS ORDER THEM

```
cmd    git log --format='%h %s' 5786bed..HEAD
out    7cee09f F4 step 2 revision 1: EQ0, EQ2's basis-independent half, ER1(c), ...
out    b979b68 F4 step 2: R683, R684 and R653 -- EQ2's basis-independent half
out    9985bcd process: EQ0 -- a closure commit that changes a gate or a tolerance ...
cmd    git diff --stat 5786bed..HEAD
out    CLAUDE.md 40, docs/SUPERVISOR.md 40, docs/milestones/F4.md 2,
out    docs/reports/F4/step-2-answers.json 81, docs/reports/F4/step-2.md 715,
out    floatfea/io/integrator.py 72, scripts/report_joint_reactions.py 37,
out    tests/verification/rung4/test_f4_static_and_mapping.py 228.
out    EIGHT files, 1171 insertions, 44 deletions.
cmd    git diff 5786bed..HEAD -- floatfea/tolerances.py          [instruction 4]
out    (no output) -- NO TOLERANCE MOVED. The implementer's section 11 is confirmed at
out    the level that matters, and I diffed it separately because that is where the
out    cheapest wrong fix lands.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"  [instruction 4c]
out    tests/conftest.py                             -- the instruction is intact
cmd    git diff 5786bed..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (no output). And I read all 228 changed lines of the rung-4 file: NO
out    `pytest_runtest_makereport`, no `pytest_ignore_collect`, no
out    `pytest_collection_modifyitems`, no hookwrapper, no plugin. Nothing the
out    ladder's gate reads was rewritten from inside a rung.
cmd    git diff --stat 5786bed..HEAD -- .claude docs/SUPERVISOR.md   [instruction 4b]
out    docs/SUPERVISOR.md | 40 ++++ -- and the whole of it is in `9985bcd`. Section 2.
cmd    git diff --name-only 5786bed..HEAD -- docs/reviews
out    (no output) -- no commit in this range touches a verdict.
```

**INSTRUCTION 1b, THE ONE COMPARISON.** The report header reads
`Answers: verdict 96 @ 5786bed`. `5786bed` IS verdict 96's own commit -- `git log
--oneline -1 5786bed` gives `review: F4 step 1 CLOSURE COMMIT -- ninety-sixth verdict`
-- and verdict 96 is the newest verdict in the repository. **The header names the LATEST
verdict and it names the verdict's own commit, not the commit it judged (DX2/C13). No
HOLD on 1b.**

## 2. MY OWN INSTRUCTIONS -- `9985bcd` IS THE PERMITTED FORM. NOT A STOP-CLASS FINDING.

I was asked to confirm this and the answer is yes, with the reading rather than the
assurance. I read the whole 80-line diff line by line.

```
cmd    git show --stat 9985bcd
out    CLAUDE.md 40 +, docs/SUPERVISOR.md 40 + -- 2 files, 80 insertions, 0 deletions
rule   CLAUDE.md "the reviewer's own instructions are not edited inside a step": a
       standalone `process:` commit that CITES the directive asking for the change, and
       never a commit that also touches `floatfea/` or `tests/`
judge  STANDALONE: two files, nothing in `floatfea/`, nothing in `tests/`. CITES: the
       message names EQ0 in its first line and quotes the directive's wording.
       PURELY ADDITIVE: zero deletions -- so NO GUARD WAS REMOVED, which is the one
       thing this rule exists to catch and the one thing a green suite cannot see,
       because nothing in the suite reads either file. The inserted text is the
       ninety-sixth verdict's own proposal, unparaphrased, at the same anchor in both
       files. **PERMITTED FORM. Not a STOP.**
```

One observation and not a finding: the clause I proposed was adopted in my wording, and
it is now the rule that this very round is NOT an instance of. EQ0 is about closure
commits. `b979b68` is a step commit.

## 3. THE EIGHT REDS AND THE RED CI, TRACED BY NAME (EG3(i), CA2)

**CI IS RED AT THE REVIEWED COMMIT AND IT IS NOT A HOLD, because every red traces by
name to EG3 state (1).** I matched each `FAILED` id to the state's own list rather than
ruling them as a family, which is the discipline EG3(i) exists to force.

```
cmd    gh run list --commit 7cee09f...  ; gh run view 37482781971 --json jobs
out    JOB the verification ladder: SUCCESS -- ladder 1,2,3,6,4,5 all success
out    JOB lint, unit and guards: FAILURE -- actionlint, ruff, black --check, mypy and
out        unit tests ALL SUCCESS; `guards and meta-tests` FAILURE
out    JOB CI determinism -- leg: skipped       (workflow_dispatch only)
out    JOB CI determinism -- ten legs agree: skipped   (workflow_dispatch only)
cmd    gh run view 37482781971 --log-failed | grep FAILED
out    8 failed, 1038 passed -- and the eight ids are the eight below
cmd    python -m pytest -q      [my own run, one invocation]
out    8 failed, 3022 passed, 2 warnings in 636.92s
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    FAILED tests/test_report_guard_states.py::...[baseline]
out    FAILED ...[non_numeric_step_suffix]
out    FAILED ...[superscript_digit_step_number]
out    FAILED ...[draft_suffix_beside_a_step_report]
out    FAILED ...[step_number_is_the_empty_string]
out    FAILED ...[verdict_amended_after_the_commit_the_report_answers]
out    FAILED ...[zero_padded_step_number]
rule   EH1: state (1) is `test_the_guard_reads_the_step_being_worked_on` plus the
       planted states that cascade off a red baseline, identified by the baseline being
       red and by each cascading state's OWN failure line
judge  ONE is the named test. The other SEVEN each print, inside their own nested run,
       `FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked
       _on -- AssertionError: step 2 has a report and no verdict yet` and
       `1 failed, 217 passed`. `[baseline]` is red, so the cascade is identified the way
       EH1 says. **NOT ONE RED IS OUTSIDE THE LIST.** The literal-guard red that
       `b979b68` shipped is GONE at this commit, confirmed by CI and by my own run:
       `tests/test_no_tolerance_literals.py` appears in neither failure list, and
       `pytest tests/test_no_tolerance_literals.py tests/verification/rung4 -q` gives
       `212 passed in 1.21s`.
```

**The three states, kept distinct (CK2).** The two determinism jobs are `skipped`, and
they are `if: github.event_name == 'workflow_dispatch'` in `.github/workflows/ci.yml:90`
and `:213` -- so they are skipped BY DESIGN on a push and not by an exhausted allowance.
That makes them **unmeasured at this commit**, which I record rather than step over.
Nothing in this range touches `.github`, so the last dispatch result still describes the
tree.

**EG3(ii) -- I measure state (1) clearing at MY verdict commit and the next revision
pastes it.** That is the half no verdict in this milestone had measured until verdict 96
asked for it, and this is the second time it is being taken.

## 4. THE RED `b979b68` SHIPPED, AND THE EXEMPTIONS I WAS ASKED TO RULE ON

**The mechanism the implementer reports is correct and the self-diagnosis is the right
one** -- a count taken over `tests/verification/rung4` cannot speak for a guard that is
not in that directory, and the revert that removed R682's edits is what put the literals
back. I confirm CI found the same three, to the line number, at the same commit.

**NOW THE RULING, because three exemptions were asked about and the answer is not the
same for all three.**

**`0.05263` -- LEGITIMATE.** It is the EXPECTED side of a comparison, read out of
`docs/load-interchange-v1.md:259`, which publishes it. An expected value is not a
tolerance: there is no slack in it to widen. Marker accepted.

**`0.8` -- LEGITIMATE AS AN EXEMPTION.** It is an INPUT to the integrator and the
quantity the assertion pins, not a bound on one. Marker accepted. **The assertion it
sits in is R686 for a different reason.**

**`0.5` and `1.0` -- THE LITERALS ARE NOT TOLERANCES AND THE REASON GIVEN FOR THEM IS
FALSE.** That is R687, and it is blocking.

**AND THE ONE REAL TOLERANCE IN THIS GATE IS THE ONE NOBODY MARKED.**
`round(getattr(got, name), 5) == published` is a comparison epsilon written as a
rounding, and `CLAUDE.md` names "comparison epsilons" explicitly. The report says "NO
TOLERANCE IS DECLARED and none is wanted ... compared at five decimal places, which is
exact". **It is not exact. I solved it.** That is R688.

## 5. ER1(c) -- NO STOP, AND I REPRODUCED IT WITH `admissible()` RATHER THAN READING IT

The report's figures are generated by `scratchpad/er1c_stop.py`, which is not in the
tree, so no figure in its section 3 is regenerable at this commit. **So I took every one
of them myself**, from the deck YAML with ER0's override applied to an in-memory copy,
through `build_superstructure(mass_fraction=0.75)` and `admissible()`.

```
cmd    my own probe: deck platform mass 10.0 -> 20.0, Ixx/Iyy/Izz 10/10/20 -> 20/20/40,
       reference_point untouched; build_superstructure(path=..., mass_fraction=0.75)
out    platform  admissible=True  m_rem=6.250000e+05
out       eig = 4.666294e+09, 4.666294e+09, 1.093623e+10   slack = -1.603643e+09
out       link = 41.326086   rem_pos = [3.4e-15, -3.0e-15, 65.9946]
out    hub1..4   admissible=True  m_rem=3.750000e+05
out       eig = 3.792032e+07, 3.792032e+07, 7.736354e+07   slack = -1.522913e+06
out       link = 0.000000    rem_pos = [+-50, 0, 24.6685]
rule   ER1(c): if any body is not PSD at 0.75, STOP and report
judge  **NO STOP. Every figure the report publishes reproduces to every digit it
       prints**, and I called `admissible()` itself rather than re-implementing the
       test, so this is the shipped decision and not a second opinion about it.
```

**THE LINK-LENGTH CLAIM IS CORRECT AND SO IS THE REASON GIVEN FOR IT**, which I checked
rather than accepting, because a causal sentence carries its cell (BG0).

```
cmd    the same probe on BOTH decks, f = 0.75, only the platform mass and inertia moved
out    new basis: |link| = 41.326086 m, m_remainder = 6.250000e+05
out    old basis: |link| = 41.326086 m, m_remainder = 3.125000e+05
cell   geometry, reference point, joints and f all held; mass and inertia alone moved
judge  CORRECT, and the algebra says why: the remainder position solves
       `M x_cog = f M x_member + (1-f) M x_rem`, so `x_rem = (x_cog - f x_member)/(1-f)`
       and `M` cancels. The position is independent of the TOTAL mass at fixed `f`, which
       is a stronger statement than "linear in mass" and is the one that holds.
```

**The equivalent densities reproduce exactly too**: platform `7145.965` (`7146.0`), hubs
`11433.545` (`11433.5`), old basis platform `3572.983` (`3573.0`), new basis at the
ladder default `4763.977` (`4764.0`) with hubs `7622.363` (`7622.4`). The report's
reading -- the sizing question has moved to the hubs -- is confirmed.

**AND ONE THING THE REPORT DOES NOT SAY, which will decide whether ER0 can ship at
`f = 0.75` at all.** `f = 0.75` is OFF `MASS_FRACTION_LADDER`, whose largest rung is
`0.5`, so the builder itself records a finding at every body:

```
cmd    my own probe: build_superstructure(mass_fraction=0.75).findings, both decks
out    NEW basis, f=0.75: 9 superstructure findings
out      platform x1: "the mass fraction is 0.75, handed in by the caller rather than
out        taken from (0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never
out        consulted for it. This body is a MEASUREMENT, not one to ship."
out      hub1..4 x2 each: the same, PLUS "the equivalent density is 11433.5 kg/m^3,
out        ABOVE steel at 7850"
out    NEW basis, ladder (f=0.5): 0 findings, platform 4763.977, hubs 7622.363
out    OLD basis, f=0.75: the same 9 findings
judge  `admissible()` returning True and the SHIPPED builder admitting the fraction are
       two different statements, and the builder's own words for `f = 0.75` are "not one
       to ship". ER0 at `f = 0.75` therefore needs either a ladder that contains 0.75 or
       an explicit decision to ship a configuration carrying nine findings, and the hub
       section is the thing the density finding points at. NOT a blocking finding at this
       commit -- nothing is implemented -- and recorded now because it is cheaper to
       settle before ER1(d) derives eight expected values on top of it.
```

**ER1(d)'s eight static figures: all eight confirmed by hand, independently.**
`20.0*125000*9.81/4 = 6,131,250`; `0.75*2.5e6/4*9.81 = 4,598,437.5`; difference
`1,532,812.5`; `6,131,250*50 - 4,598,437.5*25 = 191,601,562.5`. Hub side:
`12.0*125000*9.81 = 14,715,000`, `+6,131,250 = 20,846,250`, `/3 = 6,948,750`;
`0.75*1.5e6/3*9.81 = 3,678,750`; difference `3,270,000`;
`6,948,750*25 - 3,678,750*12.5 = 127,734,375`. And the INPUTS are the deck's own:
`platform mass 10.0`, `hub mass 12.0` at model scale, read out of
`data/platform/platform12_deck.yaml`. Nothing to correct.

## 6. R683 AND R684 -- BOTH ABLATIONS RUN BY ME, ONE RED EACH, THE RIGHT ONE

I did not accept either ablation. I made each change in the tree myself, ran the WHOLE of
rung 4 rather than a `-k` subset, and restored the file.

```
cmd    `_body_errors` replaced by the AGGREGATE form (sum got and want over the five
       bodies, then normalise), every injection and the lam row held; pytest
       tests/verification/rung4 -q -rf
out    1 failed, 156 passed in 1.05s
out    FAILED ...REDDENS_on_a_wrong_sign_and_on_a_wrong_node[internal_joint_dropped]
out    AssertionError: the `internal_joint_dropped` injection reads 2.082021e-16, which
out    the ceiling ACCEPTS
cell   ONE VARIABLE MOVED -- the normalisation scope. Nothing else touched.
judge  **R683 IS ANSWERED.** The row exists, it is the only one that distinguishes the
       two forms, and the per-body rule is now held in place by something in the tree.
       The gate carries its own failure.
```

```
cmd    `assert f_scale > 0.0 and m_scale > 0.0` reinstated at the head of
       `_one_body_error` -- the form C158 shipped; pytest tests/verification/rung4 -q -rf
out    1 failed, 156 passed in 1.08s
out    FAILED test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked
judge  **R684 IS ANSWERED ON ITS FIRST HALF**, and the false sentence is deleted rather
       than rephrased, which was the second conjunct of its closing condition. The COUNT
       conjunct is not done and that is R689.
```

**AND THE ABSOLUTE BRANCH IS THE RIGHT FORM, which I say explicitly because I asked for
it and it would be easy to get wrong.** I attacked it four ways:

```
cmd    my own probe: leak eps onto `hub2`'s force, buoy1-only row (hub2 expected == 0)
out    eps = 5e-324 (one denormal) -> RAISES.  1e-300 -> RAISES.  1e-12 -> RAISES.
out    1.0 -> RAISES.  pure MOMENT leak 1e6 N.m -> RAISES on the moment branch.
out    equal-and-opposite force pair on two different nodes -> RAISES on the moment
out    branch, because cross(x, F) does not cancel when the points differ.
rule   `np.all(got == 0.0)`: the smallest detectable defect is one ULP
judge  **the strongest counter in this file, and the two channels are branched
       SEPARATELY** so a moment-only leak is not hidden behind a zero force check. The
       only miss is a signed `-0.0`, which carries no load; recorded in the corpus so a
       later tightening is a decision rather than a surprise.
```

## 7. R653 -- THE FORMULA HALF IS ANSWERED. THE CONSTANT HALF IS A TAUTOLOGY.

**First, the placement question I was asked: `floatfea/io/integrator.py` IS ACCEPTABLE
and DR1 does not reach it.** DR1 freezes "guards, scanners, meta-tests, detectors and
report generators". This module is neither -- it is a closed-form coefficient derivation
and the scheme parameter, on the FE side's read path, and `floatfea/io/reader.py:50`
already requires the same five fields from every record. It is production code in the
right package. Accepted, and I would not have accepted it in `tests/`.

**Second, the reference, verified independently of the implementation (my recorded guard
is that the reference has been wrong more often than the thing measured).**

```
cmd    my own evaluation of Chung & Hulbert (1993) eqs (25)-(27) at rho_inf = 0.9, and
       the closed forms beta = 1/(1+rho)^2 and gamma = 1/2 + (1-rho)/(1+rho)
out    alpha_m 0.4210526315789474  alpha_f 0.4736842105263158
out    beta    0.2770083102493076  gamma   0.5526315789473684
out    rounded to five places: 0.42105, 0.47368, 0.27701, 0.55263
rule   docs/load-interchange-v1.md:259-260 publishes exactly those four, and line 52 of
       the same file points at sec.4.1 for the block
judge  **THE REFERENCE IS RIGHT, THE FORMULA IS RIGHT, AND THE TWO AGREE.** The
       difference `alpha_f - alpha_m = (1-rho)/(1+rho)` gives `0.0526315...` -> `0.05263`,
       the figure the specification singles out. The report's section 4 citation is
       correct (SECTION 4, lines 259-260); the two in-tree citations are not, see
       Closure items.
```

**Third, and this is R686: the constant half asserts a literal against a copy of
itself, and the artifact that carries FloatSim's own value is in this repository,
unread.**

```
cmd    grep -rn "spectral_radius_inf" over the whole repository
out    data/platform/platform12_deck.yaml:26:  spectral_radius_inf: 0.8
out    -- ONE occurrence. Nothing reads it.
cmd    grep -rn "rho_inf" HSP-stable --include=*.py | grep "= *0\."
out    HSP-stable/floatsim/solver/newmark.py:222:    rho_inf: float = 0.9   <- DEFAULT
out    HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291:  rho_inf=0.8
judge  `0.8` IS the right number for this study and I verified it two independent ways.
       What nothing verifies is that the FE side's copy still equals it.
```

```
claim  the new gate cannot fail on the property its own name states
cmd    set data/platform/platform12_deck.yaml:26 to `spectral_radius_inf: 0.9` -- the
       exact disagreement C131's "429x louder" was about -- then
       python -m pytest tests/verification/rung4 tests/test_no_tolerance_literals.py -q
out    212 passed in 1.41s
rule   "A gate carries its own failure": break the claimed property and confirm the
       assertion goes red
judge  **GREEN. The deck, generated from HSP at the pinned tag and never hand-edited,
       may disagree with `FLOATSIM_RHO_INF` by any amount and nothing reddens.** The
       gate is a change-detector on its own literal, which is worth having and is not
       what its name, its docstring or the report claim for it.
```

## 8. TRY TO BREAK IT -- THE MAPPING GATE READS PERFECT ON A ROW IT MEASURES NOTHING IN

The adversarial case for this step is the one R684's repair created and nothing in the
step looks at: a lam row that sends bodies into the ZERO-SCALE branch. The new
`test_G4_4_a_LEGAL_SPARSE_row...` asserts `len(silent) == 4` and `norm(lam_row) > 0.0`,
so it is safe. **The PRODUCTION gate is not.**

```
cmd    my own probe: `_body_errors` over the buoy1-only row, per body
out    hub1 0.000e+00  hub2 0.000e+00  hub3 0.000e+00  hub4 0.000e+00
out    platform 0.000e+00     ->  error 0.000e+00, well inside 1.0e-12, GREEN
out    bodies compared RELATIVELY: 0 of 5
cmd    the same over an ALL-ZERO lam row
out    error 0.0 -> GREEN. The gate passes on a multiplier row that certifies nothing.
rule   "assertion domain blindness": check that the collection the assertion inspects
       can actually contain the failure
judge  **R689.** `_one_body_error` returns `0.0` for "compared and perfect" AND for
       "nothing to compare", and `max()` over the five cannot tell them apart. Four
       bodies took the absolute branch; `hub1`'s relative error is also exactly `0.0`.
       The production gate's coverage rests entirely on `_synthetic_lam` being dense,
       which a comment at `:769` claims and nothing asserts. This is the COUNT conjunct
       of R684's closing condition -- "so a sparse row reduces coverage visibly rather
       than erroring" -- and it is the half that is not done.
```

**Both directions on the boundary (EH4), including the two that weaken the gate.**

```
cmd    uniform gain (1+eps) on every mapped body, expected side held
out    eps 1e-13 -> 1.002e-13 GREEN ;  eps 1e-12 -> 1.001e-12 RED
cmd    the `internal_joint_dropped` share scaled by s -- the INJECTION falling
out    s = 5.7e-13 -> 1.013828e-12 RED ;  s = 5.6e-13 -> 9.959214e-13 GREEN
out    full strength 1.778481e+00, so the row survives a 1.8e+12x weakening
cmd    a single-component defect on the platform's SMALLEST force component
out    want force = [-636113.848, -1157231.570, -431368.634] N; the normaliser is the
out    component-wise MAX 1.157e6, not the 4.314e5 being tested, so +1e-6 N on Fz reads
out    8.641e-13 GREEN and detection starts near 1.16e-6 N -- a 2.68x dilution
judge  the ceiling is sound and its operating point is now stated. The dilution is not a
       defect; it is what "relative to the largest component" means, and it is recorded
       so the ratio is not read as a per-component bound.
```

**And the localisation R683's closing condition asked for, which the report does not
paste. I took it.**

```
cmd    the shipped `internal_joint_dropped` injection, per body
out    platform 1.778481e+00   hub1 3.896589e-01
out    hub2 1.795271e-16   hub3 2.092543e-16   hub4 1.634659e-16
judge  the residual localises to EXACTLY the two bodies the dropped joint touches and
       the other three sit at round-off -- matching the `1.795e-16 / 2.093e-16 /
       1.635e-16` I measured at verdict 96 to four digits. This is the evidence, and it
       is a closure item that it is in my file rather than in the report's.
```

## The adversarial corpus (BE3)

`tests/corpus/f4_mapping_zero_scale_and_coverage.txt`, batch 36, committed separately at
`4f99c7f`. **Fourteen entries, all unseen.** Under EG4(e) this is the F4 load-mapping
gate, which is one of the two standing exceptions to the corpus pause; the R653
integrator gate is outside that exception, so its measurements are in section 7 and not
in the corpus.

**COVERAGE: 8 of the 14 caught, 4 missed, 2 explanatory.** The eight caught include the
one-denormal leak on both channels, the equal-and-opposite pair, both solved boundaries
and both of my ablations. The four misses are the sparse row, the all-zero row, the
extra-body-absent-from-`want` route through `_mapping_error`, and a signed `-0.0`. The
first two are R689, the third is scoped to the three counter-cases and the new sparse
test (the production gate catches it at `set(loads) == set(n_dof_of)`), and the fourth is
harmless and recorded as such.

Batch 34 moved the WIRING and batch 33 the THRESHOLDS; this batch exists because R684's
repair created a third surface -- `_one_body_error` now has two branches and the LAM ROW
decides which one a body takes -- that neither earlier batch could have reached.
`python -m pytest tests/ -q -k corpus` gives `1361 passed, 1669 deselected` with the new
file in the tree.

## Findings

**R686. (c, blocking) `test_R653_the_value_the_DRIVER_reconstructs_with_is_the_declared_one`
CANNOT FAIL ON THE PROPERTY ITS NAME STATES, AND THE GENERATED ARTIFACT THAT CARRIES
FLOATSIM'S OWN `rho_inf` IS IN THIS REPOSITORY, UNREAD.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1016-1046` and
`floatfea/io/integrator.py:27`. The driver reads `RHO_INF = FLOATSIM_RHO_INF`
(`scripts/report_joint_reactions.py:77`), so "the value the driver reconstructs with IS
the declared one" is true by assignment and has no failure mode; the only thing the test
detects is an edit to `FLOATSIM_RHO_INF` that does not also edit the test literal.
Measured: `data/platform/platform12_deck.yaml:26` carries `spectral_radius_inf: 0.8`, it
is the ONLY occurrence of that key in the repository, nothing reads it, and setting it to
`0.9` -- the exact disagreement C131's "429x louder" figure was about -- leaves
`pytest tests/verification/rung4 tests/test_no_tolerance_literals.py` at `212 passed`.
The deck is generated by `scripts/export_platform_deck.py` from HSP at the pinned tag, is
round-trip-validated by its own generator, and its header says "DO NOT HAND-EDIT" -- it is
the one copy of this number with provenance and it is the one not compared.
`HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291` confirms `rho_inf=0.8` for
the study the driver replays, while `floatsim/solver/newmark.py:222` shows FloatSim's
DEFAULT is `0.9`, so "It is FloatSim's value, not a choice made here" is also imprecise:
it is this STUDY's value. The number now exists in three places -- the deck,
`integrator.py`, and the test literal -- and the two that are compared are the two the
same hand typed, which is C131's own finding re-instantiated by the commit that cites it.
**Closed when** `FLOATSIM_RHO_INF` is compared against a value READ from
`data/platform/platform12_deck.yaml` (`simulation.spectral_radius_inf`) instead of against
a literal, with the deck-at-`0.9` ablation re-run and pasted to show the gate now reddens;
the deck is already a shipped data file this rung reads, so this needs no HSP worktree and
no new apparatus. **OR**, equally acceptable to me: the literal stays, the test is RENAMED
to say it is a change-detector on the declared constant, its docstring drops the claim
that it pins what the driver reconstructs with, and the provenance becomes a
`claim/cmd/out` triple naming the deck line and the study line -- but then R653 is
answered by disclosure and the entry says which claim it is making.

**R687. (c, blocking) THE RANGE ASSERTION CLAIMS A PROPERTY GENERALIZED-ALPHA DOES NOT
HAVE, AND THAT FALSE SENTENCE IS WHAT EXEMPTS TWO LITERALS FROM `tolerances.py`.**
`tests/verification/rung4/test_f4_static_and_mapping.py:1037-1046`:
`assert 0.0 < coefficients.beta < 0.5 and 0.0 < coefficients.gamma < 1.0`, with the marker
comment "0.5 and 1.0 are the mathematical ranges `beta` and `gamma` have for a dissipative
generalized-alpha step, which is a property of the scheme and not an agreement between two
measurements", and the message "which are outside the ranges a dissipative
generalized-alpha step has". Measured over the scheme's own parameter range `rho_inf` in
`[0, 1]`, from the closed forms `beta = 1/(1+rho)^2` and `gamma = 1/2 + (1-rho)/(1+rho)`
which I derived and then checked against the code at twelve values:
**`beta` in `[0.25, 1.0]` and `gamma` in `[0.5, 1.5]`.** `beta < 0.5` holds only for
`rho_inf > sqrt(2)-1 = 0.4142136`, and `gamma < 1.0` only for `rho_inf > 1/3`. At
`rho_inf = 0.2` -- a valid, more strongly dissipative step -- the shipped assertion calls
`beta = 0.694444` and `gamma = 1.166667` "outside the ranges a dissipative
generalized-alpha step has", which is false of both numbers. The two literals are NOT
tolerances and do not belong in `floatfea/tolerances.py`: they bound a computed quantity
rather than a window of agreement, so the exemption's FORM is right. Its REASON is false,
and the reason is the whole of what the marker offers a reader. The assertion also adds
nothing beside the exact pin above it, passing at `0.5`, `0.9` and `1.0` as readily as at
`0.8`.
**Closed when** either the assertion states the ranges the scheme actually has
(`0.25 <= beta <= 1.0`, `0.5 <= gamma <= 1.5`) with the two closed forms and the two
crossover values `sqrt(2)-1` and `1/3` pasted; **OR** it is replaced by the invariant that
holds for every `rho_inf` and would catch a wrong formula -- `beta` exactly
`0.25*(1 - alpha_m + alpha_f)**2`, `gamma` exactly `0.5 - alpha_m + alpha_f`, with
`alpha_m <= alpha_f <= 0.5` -- which is a stronger gate than the one shipped and needs no
literal at all; **OR** it is deleted with the reason recorded at the site. In every case
the false sentence goes from BOTH sites, the marker comment and the assertion message.

**R688. (b, blocking) `round(x, 5) == published` IS A COMPARISON EPSILON, THE TEST AND THE
REPORT BOTH CALL IT EXACT, AND I SOLVED IT.**
`tests/verification/rung4/test_f4_static_and_mapping.py:999-1013` ("the comparison is
against the value ROUNDED to five places, which is exact. A ceiling here would be a number
with nothing behind it") and `docs/reports/F4/step-2.md` section 6 ("NO TOLERANCE IS
DECLARED and none is wanted ... compared at five decimal places, which is exact").
`CLAUDE.md` names "comparison epsilons" among the things that are a tolerance under
another name, and a rounding comparison is one: it admits any drift that does not cross a
quantisation edge. Measured, per coefficient, the drift this assertion still accepts:
**`alpha_f` 7.895e-07** (exact `0.4736842105263158`, edge at `0.473685`), `alpha_m`
`2.368e-06`, `beta` `3.310e-06`, `gamma` `3.421e-06`; `5.0e-06` is the half-step and the
GOVERNING figure is the smallest of the four, not the nominal half-step, because a gate is
as sensitive as its weakest channel. On `alpha_f` that is `1.67e-06` relative. The gate is
strong and I am not asking it to be stronger; "exact" is false by six orders of magnitude,
and the four numbers that make it a measurement are nowhere in the tree.
**Closed when** either the half-width `5.0e-06` is declared in `floatfea/tolerances.py` as
a dimensionless tolerance justified by the specification's five-place print precision, with
the counter being the smallest coefficient drift the same assertion detects in the same
quantity -- `7.895e-07` on `alpha_f`, with all four per-coefficient figures pasted;
**OR** `round(..., 5)` stays and the word "exact" is deleted from the test docstring and
from the report, replaced by the measured per-coefficient window with `7.895e-07` named as
the governing one. Either is fine. What is not is a sentence saying there is no tolerance
here when there is one and nobody has measured it.

**R689. (c, blocking) THE PRODUCTION MAPPING GATE READS `0.000e+00` ON A ROW IT COMPARES
NOTHING IN, AND PASSES ON AN ALL-ZERO MULTIPLIER ROW. THIS IS THE COUNT CONJUNCT OF
R684's CLOSING CONDITION.**
`tests/verification/rung4/test_f4_static_and_mapping.py`, `_one_body_error` at `:760-791`,
`_body_errors` at `:749-757`, and
`test_G4_4_the_mapping_CONSERVES_the_joint_resultants` at `:807-847`. `_one_body_error`
returns `0.0` both for "compared relatively and perfect" and for "nothing to compare", and
`max()` over the five bodies cannot distinguish them. Measured: handed the buoy1-only row,
the production gate reads `error 0.000e+00` against `1.0e-12`, GREEN, with **0 of 5 bodies
compared relatively**; handed `np.zeros_like(lam_row)` it reads `0.0` and PASSES on a
multiplier row that certifies nothing. The new
`test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked` has both guards --
`assert float(np.linalg.norm(lam_row)) > 0.0, "the row is zero, so it tests nothing"` and
`assert len(silent) == 4` -- and the gate the plan's G4.4 row points at has neither. Its
coverage rests entirely on `_synthetic_lam` being dense in all sixteen blocks, which the
comment at `:769` asserts in prose ("It was latent only because `_synthetic_lam` is dense
in all 16 joints"), which I measured true today at 16 of 16, and which nothing in the file
checks -- so the premise that makes the gate meaningful is exactly the kind of sentence
CW0 asks to be a test or a triple. Verdict 96's condition read "an absolute comparison
against zero for that body PLUS an assertion on the COUNT of bodies compared ... so a
sparse row reduces coverage visibly rather than erroring". The first conjunct is done and
reproduced; this is the second, and half of an item is not the item.
**Closed when** `test_G4_4_the_mapping_CONSERVES_the_joint_resultants` asserts the COUNT
of bodies compared relatively -- equivalently that the lam row is nonzero in all sixteen
blocks -- with the measured `0 of 5` on the sparse row and the `0.0` on the all-zero row
pasted as what the assertion exists to prevent. That is the `checked == 16` pattern this
file already uses twice, and it makes the `:769` sentence true by assertion in the same
edit.

**R690. (closure-class, not (a) to (d), and I say so rather than dressing it as more.)
ER0, ER1, ER2, EQ2, EQ3 AND EQ4 EXIST NOWHERE IN THIS REPOSITORY, AND ER0 CHANGES THE
LOCKED PLAN'S SECTION 0.**
`grep -n "ER0\|ER1\|ER2\|EQ2\|EQ3\|EQ4" docs/milestones/F4.md` returns nothing, and the
only plan change in this range is the step marker `1 -> 2`. So this round judged a report
structured around six directives I can read only through the report's own account of them,
which my instructions name as a finding in itself. The work is correctly PAUSED -- the
report holds R682 and R685, and section 3a's eight figures are explicitly not asserted --
so nothing is silently adapted and this is not a STOP today. `docs/milestones/F4.md:5`
reads "LOCKED by directive EK. The section 0 answers are the directive's words,
unparaphrased. Changing them reopens the lock; it is not an inline edit", and ER0 changes
the platform mass and inertia that section 0 fixes.
**Closed when** ER0's and ER1's text is in the repository -- the plan's section 0 under a
re-lock, with ER2's ordering and EQ2/EQ3/EQ4 recorded wherever they belong -- BEFORE any
figure is derived on the new basis. Recorded now, and not held, because ER1(d) will derive
eight expected values and five counters from section 0, and a re-lock after that is a
second calibration of exactly the kind ER2 exists to prevent. The off-ladder consequence
in section 5 belongs to this item: `f = 0.75` produces nine builder findings on either
basis, one of them "This body is a MEASUREMENT, not one to ship".

## Closure items

Not re-reviewed item by item (CZ0). **C161 to C166 and C137/C141/C144/C145/C147/C148/C151
are STILL OPEN** -- the report says so in its section 9c and routes them to step 2's
closure commit, which is the right place. C161 I checked and it is unchanged: the dead
`error = _mapping_error(built, loads, want)` at `:838` is still overwritten two lines
later at `:840`. C166 is partly discharged -- the report lists the paths, which is what
EQ4 asked for -- and `git worktree list` still shows my own `wt84` plus seven
`suite-count-*`. New this round:

* **C167.** `scripts/report_joint_reactions.py:71` -- the false specification citation
  the report says it fixed is still here: "`docs/load-interchange-v1.md` sec.6's own
  published coefficients". `sec.6` is `## 6. Two-pass generation` at line 571. The fix
  landed at the other site and this one was left, which is the "closed site by site"
  shape. Closes when it reads sec.4.1 (or SECTION 4, lines 259-260, as the test file's
  own comment correctly does).
* **C168.** `floatfea/io/integrator.py:63` -- "`docs/load-interchange-v1.md` sec.2 is
  where the field is specified". Section 2 LISTS the field, at line 52, as
  `integrator REQUIRED -- v1.2, see sec.4.1`; section 4.1 at line 222 is where it is
  SPECIFIED, and the spec's own line points there. Defensible and still not the right
  pointer. Closes when it reads sec.4.1.
* **C169.** `floatfea/io/integrator.py:28-37` -- three sentences asserting facts with no
  triple and no cell: "It is FloatSim's value, not a choice made here", "the driver
  imports it from this module so that there is exactly one copy", and "Varying the single
  value moves the residual by about `1.0005x`". The first is imprecise (R686: it is this
  study's value; FloatSim's default is `0.9`), the second is checkable in one grep and
  measured true, the third is a causal figure with no cell in this file. CW0/BG0. Closes
  when each is a triple, a test, or deleted. **Note the module docstring at `:9-10`
  already does this correctly**, which is why this is a closure item and not a pattern.
* **C170.** `test_f4_static_and_mapping.py:862-864` -- the counter-case docstring's
  "`1.872582e-16` aggregated" carries no command and is not regenerated by anything. My
  own aggregate revert measured `2.082021e-16`. Both are round-off and nothing turns on
  the digits; the point is that it is an `out` line with no `cmd`. BI3's second permitted
  form applies: the entry keeps the number it needs and a pointer to the report.
* **C171.** R683's closing condition asked for the per-body breakdown to be pasted,
  because that is the evidence the residual localises. The report's section 4 pastes the
  pass/fail counts only. I took it (section 8) and it confirms localisation to exactly the
  two bodies the joint touches. Closes when the report or the closure artifact carries
  `platform 1.778481e+00, hub1 3.896589e-01, hub2 1.795271e-16, hub3 2.092543e-16,
  hub4 1.634659e-16`.
* **C172.** `docs/reports/F4/step-2.md` sections 3, 3a and 7 are generated by
  `scratchpad/er1c_stop.py` and `scratchpad/eq2_measure.py`, which are not in the tree, so
  no figure in them is regenerable at this commit -- the same shape as verdict 93's R, and
  the reason I re-took every one of them myself. All reproduce exactly, so this is a
  provenance item and not a correctness one. Closes when the figures come from something
  committed, or the report says plainly that these three sections are reviewer-reproduced
  rather than regenerated.
* **C173.** The two `CI determinism` jobs are `workflow_dispatch`-only
  (`.github/workflows/ci.yml:90`, `:213`) and were skipped at this commit, so determinism
  is **unmeasured** here. Recorded rather than stepped over (CK2's discipline, applied to
  a by-design skip rather than to an exhausted allowance). Nothing in this range touches
  `.github`. Closes when a dispatch run at a step-2 commit is cited, or the report states
  that determinism is measured per milestone and not per step.

## Carried

Verdict 96 carried **six items into step 2 by name -- R682, R683, R684, R685, R653 and
R679's remainder (R683 IS that remainder, so five distinct)** -- plus C161 to C166 and the
seven deferred C-items. Every one, with its status and where.

* **R683 -- ANSWERED, AND I REPRODUCED IT RATHER THAN ACCEPTING IT.** Report section 4;
  the row is at `test_f4_static_and_mapping.py:848-850` and `:886-901`. My own aggregate
  revert over the whole of rung 4 gives `1 failed, 156 passed` and the one red is
  `...[internal_joint_dropped]`, so the per-body rule is now held in place by something in
  the tree -- which is the whole of what R683 was. **Remainder: the per-body breakdown was
  not pasted; that is C171 and I took the measurement myself.** The closure commit's claim
  having been false is correctly owned in the report and in the comment at `:894-901`.
* **R684 -- ANSWERED ON THE FIRST CONJUNCT AND ON THE SECOND; THE COUNT CONJUNCT CARRIES
  AS R689.** Report section 5; `_one_body_error:760-791` and the new
  `test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked:918-949`. A legal
  sparse row no longer raises, I reproduced the C158 restoration reddening exactly that one
  test (`1 failed, 156 passed`), and the false sentence is DELETED rather than rephrased.
  **The premise was mine and the implementer is right that a faithful implementation of a
  wrong premise is still a wrong gate** -- I accept that answer in those words, as verdict
  96 said I would. What is not done is "an assertion on the COUNT of bodies compared", and
  the production gate reading `0.000e+00` with `0 of 5` compared is the measurement of why
  that conjunct was in the condition. **R689.**
* **R653 -- ANSWERED ON THE FORMULA HALF, NOT ON THE CONSTANT HALF, AND ITS COMPARISON
  FORM IS R688.** Report section 6; `floatfea/io/integrator.py` and
  `test_f4_static_and_mapping.py:960-1046`. The closed form is correct, I verified it
  against Chung & Hulbert independently and against the specification's own published
  block, and the module placement is accepted. **R686** is the constant half: the pin
  cannot fail on the property its name states, and the generated deck carries
  `spectral_radius_inf: 0.8` unread. **R688** is the comparison epsilon. Both are new
  findings inside R653's own answer rather than R653 re-opened, and I say which is which so
  the next round is not asked to re-answer what is done.
* **R682 -- OPEN, AND ER2's HOLD ON THE VALUE IS ACCEPTED.** Report section 7. I checked
  the premise rather than taking it: the tip/root ratio is independent of the total mass
  (numerator `mu L^2/12` and denominator `R L - w L^2/2` both scale with `M`) but it is NOT
  independent of `f`, and ER0 moves `f` from the ladder's `0.5` to `0.75`. So the `1/19`
  and `1/24` figures WILL move and calibrating now would be calibrating twice. **The hold
  is right.** What I do not accept for a second round is the other half: R682's condition
  offered a branch -- "the entry says that it is a bound about that one member and not
  about the sixteen" -- which is basis-INDEPENDENT, costs one sentence, and would remove a
  false claim from `floatfea/tolerances.py` today. `tolerances.py` is untouched, so the
  entry still reads "the measured worst over all 16 members is 5.555556e-02", a figure no
  member reads on either basis and which the implementer's own section 7 shows is wrong.
  R682 stays blocking and carries.
* **R685 -- OPEN, AND ER2's HOLD IS ACCEPTED WITHOUT RESERVATION.** Report section 7. The
  four figures are re-measured and in hand, the ordering the counter depends on survives,
  and the `0.2` value does not move. Nothing here is urgent and nothing is wrong except
  that the entry has not been rewritten yet. Carries.
* **R679's remainder** -- IS R683. Answered, see above.
* **C161 to C166 and C137/C141/C144/C145/C147/C148/C151** -- OPEN, routed to step 2's
  closure commit by the report's section 9c, not re-reviewed item by item, and none of them
  holds step 2. C166 is partly discharged by section 10.
* **CZ1 (ii) / EG3(ii)** -- the report measured state (1) at its own commit and traced all
  eight by name, which is what verdict 96 asked for and it is correct. I measure state (1)
  CLEARING at my verdict commit and the next revision pastes it.

## Tolerances touched

**NONE IN `floatfea/tolerances.py`, AND I DIFFED IT SEPARATELY (instruction 4) RATHER THAN
READING THE REPORT'S CLAIM.**

```
cmd    git diff 5786bed..HEAD -- floatfea/tolerances.py
out    (no output)
cmd    git diff 5786bed..HEAD -- docs/milestones/F4.md
out    one hunk: `<!-- step-under-execution: 1 -->` -> `2`. Nothing in section 5a.
rule   every numerical tolerance lives in floatfea/tolerances.py and moves with a plan
       edit; a tolerance change in the same commit as the code it rescues is a finding
judge  NO VALUE, FORM, COUNTER OR INJECTION MOVED. The report's section 11 is confirmed.
```

**BUT TWO NUMBERS THAT FUNCTION AS TOLERANCES ENTERED THE TREE OUTSIDE THAT FILE, AND
THAT IS WHY THIS SECTION IS NOT ONE LINE.**

| what | where | value | form | counter | my judgement |
|---|---|---|---|---|---|
| the five-place rounding comparison | `test_f4_static_and_mapping.py:1001`, `:1032` | half-width `5.0e-06`, undeclared | written as `round(x, 5) == published`, so dimensioned like the coefficient -- dimensionless here only because the coefficients are | none | **R688. A comparison epsilon under another name, and the test and the report both call it exact.** Solved per channel: `alpha_f` `7.895e-07`, `alpha_m` `2.368e-06`, `beta` `3.310e-06`, `gamma` `3.421e-06`. The governing figure is the smallest, `7.895e-07` on `alpha_f`. |
| `0.0 < beta < 0.5` and `0.0 < gamma < 1.0` | `test_f4_static_and_mapping.py:1041-1042` | `0.5`, `1.0` | NOT a tolerance -- a bound on a computed quantity, so `tolerances.py` is correctly not its home | n/a | **R687. The exemption's FORM is right and its REASON is false.** Measured `beta` in `[0.25, 1.0]`, `gamma` in `[0.5, 1.5]` over `rho_inf` in `[0, 1]`. |
| `0.05263` | `test_f4_static_and_mapping.py:1017` | expected value | reference figure read from `docs/load-interchange-v1.md:259` | n/a | **EXEMPTION ACCEPTED.** An expected value has no slack to widen. |
| `0.8` | `test_f4_static_and_mapping.py:1030` | input constant | the quantity pinned, not a bound on one | n/a | **EXEMPTION ACCEPTED as a non-tolerance.** The assertion is R686 for an unrelated reason. |
| `F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER` | `floatfea/tolerances.py` | `0.05`, unmoved | dimensionless | is the counter | **R682, OPEN.** Hold on the value accepted (the ratio depends on `f`, which ER0 moves). The entry's "worst over all 16 members is 5.555556e-02" is still there and is still false. |
| `F4_MAPPING_CONSERVATION` / `_COUNTER` | `floatfea/tolerances.py` | `1.0e-12` / `0.2`, unmoved | dimensionless, relative, per body | each other | **R685, OPEN, hold accepted.** I re-measured the ceiling's room myself at `4553x` on the clean per-body value `2.196224e-16`, and solved both EH4 directions in section 8. |

## On the criterion -- said once, and it leaves the loop

I was asked to say if I disagree with the criterion rather than with the work. **On CZ0 I
do not.** All four blocking findings are (b) or (c), everything else is a closure item, and
I have not held the step on a sentence.

**On the mechanism that forced THIS round, I do disagree, and this is the once.** EQ3 says
one invocation at the report; the `Stop` hook refuses a turn while `floatfea/` or `tests/`
has moved past the newest verdict. Those two rules cannot both be satisfied by a step that
takes more than one commit, and step 2 is a multi-commit step by design -- ER1(b) alone is
six FloatSim re-runs. The implementer's resolution was the honest one available: a real
report of what had landed, early, rather than a reverted commit or a silenced hook. **But
the cost is a round, and the cost falls on the step rather than on the mechanism.** I have
ruled that it counts because EB4 does not say otherwise, and I think that ruling is wrong
in substance and right in procedure.

**What I would ask Xabier for, as a question and not a round:** either EQ3 gains a clause
saying that a mid-step commit may be covered by a verdict that does not consume a round --
in which case EB4 is where it is written, so the next reviewer reads it rather than
reasoning about it -- or the `Stop` hook's condition changes to the one it is actually
trying to enforce, which is "no LATER step is worked while an earlier one is open", not
"no commit exists past the newest verdict". I have no preference between them. I am not
asking for new apparatus and the hook is not mine to edit. What I will not do is read EB4
as covering a case it does not mention, because the three-verdict cap is the only thing
standing between this project and the six-round rounds it already measured as worthless.

## On the schedule

The report's one hand-written paragraph carries the dates and reports slippage the day it
is known, which is what CZ0 asks: **F4's 14 Oct WORKING target is at risk, ER1 is a
two-day item, and the committed dates do not move.** I checked the dates against the plan
(`F4.md:375-377`) and they are the plan's. I have nothing to add except the exposure, which
has not improved: **step 2 now carries R682, R685, R686, R687, R688 and R689 -- six
blocking items, four of them new this round and three of them inside R653's own answer.**
Step 1 closed carrying three. CZ0's clause is "if two consecutive steps close carrying
blocking items, that is escalated with the choice stated -- slip the date, or reduce
scope." **If step 2 closes carrying any, that clause has now fired twice in a row**, and
the report paragraph is where the choice gets stated.

One observation for that paragraph, offered because it is cheap: the four findings this
round are all one-or-two-line edits in one file, and none of them needs ER1, the new mass
basis, or a decision from anyone. They can land before ER1(b)'s six re-runs start rather
than after.

## Next step opens when

**STEP 2 STAYS OPEN. This is its FIRST round of three, so two remain.** Step 3 does not
begin. What the next revision answers, before its own work is read, and each is specific:

1. **R686** -- `FLOATSIM_RHO_INF` compared against `simulation.spectral_radius_inf` read
   out of `data/platform/platform12_deck.yaml`, with the deck-at-`0.9` ablation re-run and
   pasted to show the gate reddens; OR the test renamed and its claim reduced to what it
   measures, with the provenance as a triple naming `platform12_deck.yaml:26` and
   `HSP-stable/studies/platform-12buoy/platform_rao_pilot.py:291`. **My figure to beat:
   `212 passed` with the deck at `0.9`.**
2. **R687** -- the range assertion stating the ranges the scheme has, or replaced by the
   exact `beta`/`gamma` identities, or deleted. The false sentence out of BOTH sites: the
   marker comment and the assertion message. **My figures to beat: `beta` in
   `[0.25, 1.0]`, `gamma` in `[0.5, 1.5]`, crossovers `sqrt(2)-1` and `1/3`.**
3. **R688** -- the five-place window declared with a counter, or `round(..., 5)` kept and
   "exact" deleted from the docstring and the report with the measured window published.
   **My figure to beat: `7.895e-07` on `alpha_f`, which is the governing channel.**
4. **R689** -- the production gate asserting the count of bodies compared relatively (or
   the row's density), with `0 of 5` and the all-zero row's `0.0` pasted as what it
   prevents.
5. **R682 and R685** -- the hold on their VALUES is accepted and I will not ask for them on
   the old basis. **R682's basis-independent half is a different matter**: either the
   `tolerances.py` entry says it is a bound about one platform arm rather than about
   sixteen, or the report names the site and says why it was left for a second round. A
   false figure in a tolerance comment is the only statement a reader has of what that
   counter bounds.
6. **R690** -- not held. ER0/ER1's text into the repository before ER1(d) derives anything
   from it, and the `f = 0.75` off-ladder question settled: nine builder findings, one of
   them "not one to ship", on either basis.
7. **C167 to C173, plus C161 to C166 and the seven deferred C-items** -- step 2's closure
   list, absorbed once, not re-reviewed item by item, and none of them holds the step.
8. **EG3(ii)** -- state (1) measured CLEARING at my verdict commit `4f99c7f`+1, and state
   (2) measured at that commit and pasted in the next revision. The expected reds there are
   the EH1 state (2) list and nothing else; any red outside it is CZ1 (iv) unchanged.

**WHAT I WILL NOT ACCEPT AT THE SECOND ROUND.** "The deck and the constant agree today"
offered as R686's answer: that is the measurement, not the gate, and R653 has been carried
four times on exactly that sentence. A range assertion for R687 whose bounds are chosen to
pass at `0.8` and justified by a new claim about the scheme that is not derived -- if the
bounds are arbitrary, say they are arbitrary and say what they are for. "A rounding is not
a tolerance" for R688 without the four numbers; the numbers are the finding and they are
measured. And for R689, a count assertion added to the SPARSE test, which already has one
-- the gate that needs it is `test_G4_4_the_mapping_CONSERVES_the_joint_resultants`,
because that is the one the plan's G4.4 row points at and the one a reader will believe.

**And the thing I would most like the second round NOT to contain**: a new figure outside a
`claim/cmd/out` triple taken after the final edit. Four of this round's five findings are
sentences that were each written in good faith, three of them inside a repair, and CP2 and
CP3 are the two rules that would have caught all three.
