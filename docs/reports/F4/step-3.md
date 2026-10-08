# F4 step 3 — EV1's dynamic gate, the member-force table, and the closure

# Revision 1 — R711, EV1's counter families, and the two items step 2 closed carrying

Answers: verdict 104 @ 74c77d1

**2026-10-07.**

## 0. CI at `9de3e4e`, the commit verdict 104 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 104 at `9de3e4e` through the report's own `Answers:` line. Run `37711840143`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1979 | 0 | 0 |
| lint, unit and guards | 1177 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 104 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 104 at `9de3e4e` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37711840143` | push | `9de3e4e` | conclusion **success** |
| `37716501832` | push | `377bace` | conclusion **failure** |
| `37720993622` | push | `2564563` | conclusion **failure** |

**Run `37716501832`, conclusion **failure**: 52 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R709]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R710]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R712]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R713]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R714]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R715]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R716]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/README.md:1]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:234]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:180]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:181]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/report_joint_reactions.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:292]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:293]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-scripts/ci_section.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:183]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:184]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-scripts/measure/g41_dynamic.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)

**Run `37720993622`, conclusion **failure**: 51 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R709]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R710]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R711]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R712]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R713]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R714]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R715]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R716]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/README.md:1]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:180]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:181]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/report_joint_reactions.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:292]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:293]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-scripts/ci_section.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:183]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:184]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-scripts/measure/g41_dynamic.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)

## 0b. The reds, traced

```
claim  the tree is green at the reviewed commit, by the reviewer's own run
cmd    python -m pytest tests -q                      (the reviewer, at 9de3e4e)
out    3244 passed, 0 failed, 0 skipped in 697.69s
rule   EG3 state (2) is a verdict written with its answering report not yet committed
judge  the interim check was taken at a GREEN tree, which is why its finding is in
       `scripts/` and not in a red. This revision creates state (2) again and it clears
       at this revision's own commit; the closure section carries that measurement.
```

## 1. The schedule, and a sentence of mine the verdict refuted

**Step 3's working target is 14 October and it holds.** Today is 7 October. The verdict
answered was an ES0 interim check and counts against no round, so **this is round 1 of
three for step 3**. EV1's gate is measured but **no ceiling is declared yet** — the
six-case run is in flight and EV1 declares over the whole domain rather than the one
case measured here. EV2's items 2 to 5 — the member-force table, R638, R637(iii)/R648 and
`docs/closure/F4.md` — are not started.

**And the sentence EV0 told me to correct.** Step 2's revision 3 section 1 said "No step
has closed carrying a blocking item, so DZ7c does not fire." That is false:

```
claim  step 1 closed carrying four blocking items, and step 2 carried two
cmd    sed -n '/^## Carried for the next step -- THESE BLOCK AT STEP 2/,/^## /p'
       <step 1's verdict> | grep -cE "^[0-9]+\. \*\*R"
out    4
out    1. **R679   2. **R680   3. **R681   4. **R653
rule   CZ0: if two consecutive steps close carrying blocking items, that is escalated
       with the choice stated
judge  one `grep` refutes it, and the escalation fired. **It is corrected here and not
       in step 2's report**, because EK3 routes post-closure prose to the next report and
       the guard reads the commit graph — any commit touching a closed report before a
       newer verdict exists reddens it, whatever the content.
```

EV0 answered the escalation: no slip and no cut to the six cases, with step 3's scope
fixed to EV2's five items and nothing else entering F4.

## 2. R711 — the numerator was the CONTINUOUS balance

```
claim  the two forms differ by thirteen decades on the force channel
cmd    python scripts/measure/g41_dynamic.py --period 14.0
out    BEFORE (continuous): force worst 2.393343e-03   (the reviewer's figure)
out    AFTER (discrete, locked): force worst 1.6159118708143226e-16 at hub3/T14
out    AFTER: moment worst 1.4480755718208573e-06 at platform/T14
rule   `docs/milestones/F4.md` locks the discrete form twice and names
       `newmark.py:414-437` as the `# expected:` source
judge  the force channel CLOSES TO ROUND-OFF under the locked form. A ceiling declared by
       the window rule from my figures would have been thirteen decades loose on a
       channel with no slack at all.
```

**Why it survived a reading, which is the part worth keeping.** The missing terms were the
generalized-alpha weights, `C`, `mu`, the external force and the MIDPOINT Jacobian — and
`ext`, `C`, `mu` and the added-mass contribution are **identically zero on the five FE
bodies** (EK0(a), which ER1 verified). So the whole cost was `alpha_m M_eff xi_ddot_{n-1}`
and `(g_mid - g_now)^T lam`. **A form that is wrong only in the terms that happen to be
nonzero looks right term by term**, which is how it passed my own reading of it.

```
claim  my repaired figures reproduce the reviewer's independently
out    reviewer, 200 steps at T=14: force 1.086249e-16, moment 1.453396e-06
out    mine, DQ6's own 990-step window: force 1.6159e-16, moment 1.448076e-06
judge  same order on force and the same number to three figures on moment, from different
       windows. The difference is the window: the reviewer used `t = 10.010 .. 12.000`
       for speed and DQ6's is `t = 29.810 .. 39.700`.
```

**Two controls exist now where there were none.**

```
claim  the per-joint decomposition reproduces the locked form's own reaction term
cmd    python scripts/measure/g41_dynamic.py --period 14.0
out    control: the per-joint decomposition reproduces `g_mid.T lam` to 2.015e-16
       relative, worst over the window
judge  this replaced a comparison of maxima, which was weaker. The reviewer measured the
       same decomposition exact to 2.869e-18 and that is what cleared the worry I had
       raised about it — the decomposition was right and the thing beside it was not.
claim  the whole-state aggregate is printed and LABELLED as what DQ8 forbids
out    control: whole-state discrete residual worst 1.107530e-04 (all 102 DOF)
judge  1.1e-04 over 102 DOF against 1.6e-16 on the FE bodies' force channel: the
       aggregate is dominated by the twelve buoys, which is why DQ8 says per body and why
       EV1 takes the buoys out of the gate.
```

**And the denominators now read the same Jacobian as the numerator.** The numerator is
formed at the step midpoint; a denominator from `jacobian(xi[n])` would describe a
different configuration. `per_joint_contributions_from(g_mid, ...)` takes the matrix the
caller already has.

## 3. EV1's counter families — two findings about the counter-cases as specified

**Finding 1: two of the twenty (body, joint) pairs are vacuous on the moment channel.**

```
claim  hub1/3 and hub3/11 carry essentially no moment to their own hub
cmd    python scripts/measure/g41_dynamic.py --period 14.0
out    hub1/3   |F| max 6.6066e+01   |M| max 5.0420e-08   drop moment 9.2111e-07
out    hub3/11  |F| max 6.6996e+01   |M| max 7.8975e-08   drop moment 6.0211e-07
out    every other pair: |M| max 3.4120e-01 .. 3.1728e+01
out    hub1 and hub3 own CLEAN moment: 9.211029e-07 and 6.021058e-07
rule   a counter-case member must move its channel ABOVE the clean value
judge  seven orders below the rest, and the drop response IS the clean value to seven
       figures. R689's shape. The cause is geometric: those two joints sit AT their hubs'
       reference points, so there is no lever and the locked-axis moment is carried on
       the platform side (`platform/3` reads `|M| 1.6475e+01`). **Only two of the four
       hubs** — hub2's and hub4's platform joints read `6.4214e-01` — so the asymmetry is
       in the geometry, not in the gate.
```

**Finding 2: EV1's `M x (1 + 1e-6)` brackets the force channel and fails the moment one.**

```
claim  the mass injection does not clear the moment channel's clean value at 2x
cmd    python scripts/measure/g41_dynamic.py --period 14.0
out    mass x(1+1e-6) on force : weakest 1.386550e-07 vs clean 1.615912e-16 -- brackets;
       the scale for a 2x edge is 1 + 2.331e-15
out    mass x(1+1e-6) on moment: weakest 6.013115e-07 vs clean 1.448076e-06 -- DOES NOT
       BRACKET at 2x; the scale for a 2x edge is 1 + 4.816e-06
rule   EV1's window rule requires both edges at least 2x
judge  the force channel closes to round-off, so almost any scale brackets it. The moment
       channel sits at 1.4e-06 and a 1e-6 mass perturbation produces 6.0e-07 — BELOW the
       thing it must bracket. The response is linear in the scale, so the smallest usable
       one is reported rather than guessed. **EV1 specifies `1 + 1e-6`, so this is a plan
       question and not mine to change.** The joint-drop injection brackets both channels
       (weakest force 1.630619e-01, weakest moment 1.816033e-02) and the window rule
       closes on it alone.
```

**Three defects of my own in that script, all found by running it.** The docstring claimed
a cross-check whose implementation was a placeholder returning zero; the check that
replaced it compared a `cog` attribute the deck does not have, so it refused all
seventeen bodies; and the family filter decided membership **per step**, so it printed the
correct exclusion set and a family of twenty at the same time — a filter disagreeing with
its own report. The family test is now the property the window rule needs: does the drop
exceed the clean worst.

## 4. R709 and R710 — the items step 2 closed carrying, and I reproduced both closures

Answered in `4b64eaf`, before the interim check, which is why that check closed them. The
ablations are here because a closure I did not reproduce myself is one I am taking on
trust.

```
cell   R709: ONE VARIABLE, a force-channel error on the four hubs only, under the sign flip
cmd    python -c "...hub-only force error, min vs max over bodies..."
out    min over bodies : 2.483526865641276e-16   <- the OLD reduction
out    max over bodies : 0.001                   <- the offender
out    old form (min < ceiling) would PASS : True
out    per-body form catches it on         : ['hub1','hub2','hub3','hub4']
judge  `min` is right for `error > counter`, where the weakest body must clear it, and
       exactly wrong for `worst_f < ceiling`, where the worst OFFENDER is the max. I
       wrote one reduction and used it for both directions, in the commit that widened
       the counter-case to fix that very class of narrowness.
cell   R710: ONE VARIABLE, the counter set to 0.5 — inside the family's spread
cmd    python -m pytest tests/verification/rung4/test_f4_static_and_mapping.py -q
       -k "mapping_gate_REDDENS"
out    AssertionError: the weakest wrong-node pair reads 0.2179893030274107, which does
       not reach the declared counter 0.5. The family: {'1->2': '0.9597', ...,
       '3->4': '0.2180', ...}
judge  the family loop catches a counter the single-pair form would have passed, because
       0.9597 > 0.5. `len(family) == 12` means the loop cannot be narrowed back silently.
```

## 5. EW0 — the CI state for a report-only judged commit

The gap I reported in step 2 revision 3, repaired in `4ed4399` under EW0 and EK2.

```
claim  the new state's premise is measured, not taken from the commit subject
cmd    python -c "...import scripts/ci_section.py; print(ci.paths_ignored()); then
       report_only on four commits..."
out    paths_ignored() : ['docs/reports/**', 'docs/reviews/**']
out    report_only(d4e2136) : True    report_only(bac3017) : True
out    report_only(77d4a6b) : False   report_only(4b64eaf) : False
rule   a commit called `report:` that also edits a test is NOT report-only
judge  the reviewer constructed eight mutations of that parser and found every misread
       errs SHORT, which is safe twice over. R714 records that `fnmatch` is wider than
       GitHub's glob and that wider is the unsafe direction — closure class, and no
       tracked path outside the two report directories matches at this tree.
claim  the verification EW0 asked for
cmd    git worktree add --detach <scratch> HEAD ; marker 2 there ; regenerate §0 ; swap
out    replaced 91 hand-carried lines with 212 generated ones
cmd    python -m pytest tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py -q -p no:randomly   (in the scratch tree)
out    365 passed
judge  and the generated figures are the ones I had assembled by hand: `981/184/0`,
       `1978/0/0`, full sha `b68f2f73dd37ad3093fd4f569fa37365fd97771a`. The hand-assembly
       was right; it should not have had to exist.
```

## 5a. R717 and R718 — the anchor line, and a fallback that could certify the wrong commit

I asked the reviewer for one line and got two findings, one of which **inverts my own
reading**. I had offered the guards' fallback as the guards resolving what the generator
cannot. It is the other way round: the generator's refusal is correct and the fallback was
the defect.

```
claim  the plain `Reviewed commit:` header is NOT the judged commit, in most states
cmd    python -c "...over the newest 60 commits touching the verdict directory, compare
       the plain header with the bold judged line..."
out    states carrying BOTH lines           : 53
out    plain header == bold judged (prefix) : 13
out    plain header DIFFERS from bold judged: 40
out    states with NO bold line at all      :  7
out      DIFFERS  488f2d8  F4/step-2  plain 4f99c7f  judged 7cee09f
out      DIFFERS  5786bed  F4/step-1  plain 6e39151  judged 84de436
rule   `scripts/write_verdict.py:36-41` says in its own words that the plain stamp is
       "structurally NOT the reviewed commit whenever the reviewer commits its corpus
       first -- as it is instructed to"
judge  so in **40 of 53** states the fallback would have resolved to a different commit
       than the one judged, and `test_the_CI_section_is_about_the_REVIEWED_commit` would
       then certify a CI table as being about a commit that is not the one reviewed. My
       sample is larger than the reviewer's and the conclusion is worse: it measured 23
       of 35. R352 was four consecutive rounds of a SECTION naming the wrong commit;
       this is the same defect with the CHECK at fault.
```

```
claim  the fallback is removed and the guard now refuses as the generator does
cmd    grep -n "return m.group(1) if m else" tests/test_report_carried.py
out    (the `_reviewed_commit` fallback is gone; the function returns "" instead)
rule   `_anchor()`'s own docstring: "CO1: one chain, no argument, no fallback that
       guesses"
judge  the existing `assert judged` already names the bold, backticked form in its
       message, so the assertion was written for this shape before the fallback was
       added. **It is latent, not live** -- all seven no-bold states happen to have the
       plain header equal to the judged commit's parent -- and I am not treating that as
       a reason to leave it: the two conditions that make it fire are a hand-written
       verdict and a corpus commit before it, which is this round minus ES0's light
       scope.
```

**R717 is the producer half and is closure class.** `write_verdict.py` emits the plain
stamp and `ci_section.py` anchors on the bold one, so the generator's input depends on a
line its own producer does not write — and the reviewer measured that the line has been
omitted **four times before** this verdict, in `F3/step-3.md` and three states of
`F2/step-7.md`. The repair belongs at the producer: emit the bold line from the body's own
statement of the judged commit, and refuse when the body states none. **Not done here**,
because it is closure class and this commit is the blocking half.

## 6. EV1's DQ8 amendment, and what it answers

`4f0acfd`, standalone, re-locking DQ8 only (DK0 applies). It answers C1: the superseded
clause normalised a 6-component residual — newtons on three rows, newton-metres on three
— by **one scalar**, and the round-2 verdict measured that scalar as the force half on
only 11 of 17 bodies. **The two channels measured separately are ten decades apart**,
which is the amendment earning itself:

```
claim  the two channels are ten decades apart over the 30 body-cases
cmd    python scripts/measure/g41_dynamic.py        (the six-case run, discrete form)
out    force  worst 1.8556070086831165e-16  at hub2/T20
out    moment worst 2.3243458955783927e-06  at platform/T15
out    force spread 2.83x ; moment spread 22.58x ; ratio between channels 1.253e+10x
rule   EV1: two dimensionless numbers, each gated, never combined
judge  a single ceiling over both would be set by the moment channel and would accept
       anything the force channel could do. **These figures are from the PREVIOUS six-case
       run and the counter families were added after it**; the declaration waits for the
       run now in flight, which produces clean and counters together.
```

## 7. R715 — my conventions escalation was overstated, and the verdict is right

I raised EV1's "moments about the body's `G`" against `docs/conventions.md`, which says
the reference point and not the CoG. The conflict is real; **my evidence for "not
coincident on this platform" was not.**

```
claim  the +37.0 mm offset I cited is the BUOY's, and buoys are out of this gate
cmd    sed -n '182,184p' docs/conventions.md
out    | Body reference point | `Z_BUOY_REF = -1.1956674` m | `platform_common.py:101` |
out    | CoG, global | `-1.0163 - 0.21638 = -1.23268` m | `cluster_common.py:33` ... |
rule   DQ7: buoys are loads, with no FE mass, so they are out of EV1's gate
judge  the deck exposes `reference_point` and NO CoG field at all, so **no FE body in
       this gate has a declared offset**. The escalation stands as a wording conflict and
       is less urgent than I framed it. The branch I took — form the moment about the
       reference point, which is the point the Jacobian's rows are already about — the
       verdict ruled right and also the better construction, since no lever arm is
       reconstructed.
```

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R709 | **answered** — §4 | (blocking) -- CLOSED, at the first branch of my condition. Answered at 4b64eaf, |
| R710 | **answered** — §4 | (blocking) -- CLOSED, at both branches of my condition. Answered at 4b64eaf, |
| R711 | **answered** — §2 | and (c) through the generator-is-the-gate carve-out) scripts/measure/g41_dynamic.py MEASURES... |
| R712 | **carried** — §9 | declaration) ER0's BASIS IS WIRED IN THE NEW CALLER AND NOT AT THE SITE, AND THE OVERRIDE'S... |
| R713 | **carried** — §9 | run_for() AND code_identical_run() APPLY NO STATUS OR CONCLUSION FILTER, SO EW0's STATE CAN... |
| R714 | **carried** — §9 | fnmatch IS WIDER THAN GITHUB'S GLOB AND WIDER IS THE UNSAFE DIRECTION.... |
| R715 | **answered** — §7 | THE DOCSTRING'S EVIDENCE FOR "NOT COINCIDENT ON THIS PLATFORM" IS A BUOY FIGURE, AND NO BODY IN... |
| R716 | **carried** — §9 | scripts/write_verdict.py CANNOT WRITE AN ES0 INTERIM CHECK ON A STEP WHOSE REPORT DOES NOT... |
| R717 | **carried** — §9 | scripts/ci_section.py's ANCHOR PATTERN AND scripts/write_verdict.py's OUTPUT DISAGREE, SO THE... |
| R718 | **answered** — §5a | : a gate assertion on WHICH QUANTITY. Latent, and I say so.)... |

## 8a. Every named site this round's diff does not touch, declared by name

```
claim  every site below is named by a verdict and untouched by this round's diff
cmd    python -m pytest tests/test_report_carried.py::test_every_named_site_is_touched_or_declared -q
out    sixty-one sites before this table existed, across eight findings
rule   a site is TOUCHED by the diff or DECLARED `no change` beside its exact token
judge  the two findings this round answers are R711 and R718, and both were answered
       by REWRITING an expression rather than by editing every line a condition
       cited -- so most rows here are lines inside the files the rewrites landed in.
       R715 is answered by withdrawing my own claim, which is why its sites are
       cited as evidence and not edited.
```

| finding | site | this round | why |
|---|---|---|---|
| R711 | `docs/milestones/F4.md:131` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `docs/milestones/F4.md:486` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `report_joint_reactions.py` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/README.md:1` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:222` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:227` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:228` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:229` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:230` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:231` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:232` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:233` | **no change** | answered in `377bace` (§2). The sites the condition names are in `scripts/measure/g41_dynamic.py`, which that commit rewrote; the rows here are lines the rewrite did not land on. |
| R712 | `report_joint_reactions.py` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/measure/g41_dynamic.py:131` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/measure/g41_dynamic.py:179` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/measure/g41_dynamic.py:180` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/measure/g41_dynamic.py:181` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/measure/g41_dynamic.py:182` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R712 | `scripts/report_joint_reactions.py:120` | **no change** | closure item (§9). ER0's basis is wired in the caller; the site fix waits for the closure commit. |
| R713 | `docs/SUPERVISOR.md` | **no change** | closure item (§9). No status/conclusion filter on EW0's state. |
| R713 | `scripts/ci_section.py:292` | **no change** | closure item (§9). No status/conclusion filter on EW0's state. |
| R713 | `scripts/ci_section.py:293` | **no change** | closure item (§9). No status/conclusion filter on EW0's state. |
| R714 | `docs/closure/F4.md` | **no change** | closure item (§9). `fnmatch` wider than GitHub's glob; no tracked path outside the two report directories matches at this tree. |
| R714 | `scripts/ci_section.py:316` | **no change** | closure item (§9). `fnmatch` wider than GitHub's glob; no tracked path outside the two report directories matches at this tree. |
| R715 | `docs/conventions.md:182` | **no change** | answered in §7 by WITHDRAWING my own overstatement, so the sites are cited as evidence and not edited. |
| R715 | `docs/conventions.md:183` | **no change** | answered in §7 by WITHDRAWING my own overstatement, so the sites are cited as evidence and not edited. |
| R715 | `docs/conventions.md:184` | **no change** | answered in §7 by WITHDRAWING my own overstatement, so the sites are cited as evidence and not edited. |
| R715 | `scripts/measure/g41_dynamic.py:36` | **no change** | answered in §7 by WITHDRAWING my own overstatement, so the sites are cited as evidence and not edited. |
| R716 | `CLAUDE.md` | **no change** | a mechanical note needing a directive, not a change to these sites (§9). |
| R716 | `docs/SUPERVISOR.md` | **no change** | a mechanical note needing a directive, not a change to these sites (§9). |
| R716 | `docs/reports/F4/step-2.md` | **no change** | a mechanical note needing a directive, not a change to these sites (§9). |
| R716 | `scripts/write_verdict.py` | **no change** | a mechanical note needing a directive, not a change to these sites (§9). |
| R716 | `write_verdict.py` | **no change** | a mechanical note needing a directive, not a change to these sites (§9). |
| R717 | `docs/reviews/F2/step-7.md` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `docs/reviews/F3/step-3.md` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `docs/reviews/F4/step-3.md` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:172` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:192` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:193` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:194` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:195` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:196` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:197` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:198` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/ci_section.py:199` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/write_verdict.py` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `scripts/write_verdict.py:82` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R717 | `write_verdict.py` | **no change** | closure item (§9), and the repair belongs at the PRODUCER (`scripts/write_verdict.py`), not at these sites. |
| R718 | `docs/closure/F4.md` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `docs/reviews/F3/step-2.md` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `docs/reviews/F3/step-3.md` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `docs/reviews/F4/step-1.md` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `docs/reviews/F4/step-2.md` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:36` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:37` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:38` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:39` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:40` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `scripts/write_verdict.py:41` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |
| R718 | `write_verdict.py` | **no change** | answered in §5a. The fallback is removed from `_judged_commit()`; the rows here are lines in the same files the removal did not land on. |

## 9. Closure items — C1 to C15, and R712, R713, R714, R716, R717

Per CZ0, fixed once in the step's closure commit, not re-reviewed item by item, and the
step is not held on one.

```
claim  the list is the two verdicts' own
out    C1 the dimensional direction (**and its condition is now LIVE** — verdict 102
       required it answered before the G4.1-dynamic quantity is chosen, and R711 is that
       choice arriving; they are one piece of work)
out    C2 answered early in c78918c   C3 the :971 figure   C4 the oblique field
out    C5 the label map   C6 R697/R699-R703 carried   C7 the 135/107 count
out    C8 the direction argument   C9 a bare ZeroDivisionError   C10 an f label
out    C11 an ablation count   C12 answered by EV3   C13 the stale :3 header
out    C14 "every element"   C15 R697 pairs with R706
out    R712 ER0's basis wired in the caller not the site
out    R713 no status/conclusion filter, so EW0's state can offer an in_progress run
out    R714 fnmatch wider than GitHub's glob
out    R716 write_verdict.py cannot write a first interim check -- needs a directive
```

**Two file-count figures of mine were wrong in commit messages**, which is CP3's ordering
in the one place CP3 does not reach — a commit message. Both are pushed and force-push is
forbidden, so they are recorded here rather than amended:

```
claim  two counts I pasted are not what the command prints
cmd    python -m black --check floatfea tests scripts
out    120 files would be left unchanged.          (I pasted 116, in 4ed4399)
cmd    python -m black --check scripts
out    23 files would be left unchanged.           (I pasted 22, in 9de3e4e)
judge  the shape is that I write a count from a previous run and then add a file. CP3's
       ordering -- generate, edit, re-run, paste -- is exactly the rule, and a commit
       message is the one artifact no guard re-reads.
```

**R717 is listed above and is the producer half of R718's mechanism**; section 5a carries
both.

## 10. Tolerances touched

**None.** No value and no declared counter moved in this range:

```
claim  no tolerance declaration changed since the step-2 close
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+][A-Z0-9_]+:"
out    (no output)
rule   EU1 fires on an interim check whose diff moves a value or a declared counter
judge  53 lines of that file changed and all are comments — R710's figure corrections.
       **EV1's two ceilings are not declared yet**, which is section 1's point.
```

## 11. Lint, types, and the whole suite

```
claim  lint, formatting and types are green at this commit
cmd    python -m ruff check floatfea tests scripts && python -m black --check floatfea
       tests scripts && python -m mypy floatfea
out    All checks passed!
out    120 files would be left unchanged.
out    Success: no issues found in 36 source files
judge  `pytest` runs none of the three, which is CZ1's reason for pasting each.
```

**The first count is the result: `2856 passed, 0 failed, 0 skipped`** over the whole suite
outside the three files parametrised over this report.

```
cmd    python scripts/suite_count.py
out    Whole suite at 74c77d1 : 2856 passed, 0 failed, 0 skipped
out    The excluded set       : 166 passed, 83 failed, 0 skipped
cmd    python -m pytest tests/test_report_carried.py
       tests/test_report_numbers_are_sourced.py tests/test_tree_prose_consistent.py -q
out    1 failed, 260 passed   (the one was test_the_report_carries_a_WHOLE_SUITE_count,
out                            which this paste answers)
rule   EG3 state (2): a verdict written, its answering report not yet committed
```

**The 83, traced by id and not by family (EG3(i)).** `test_every_named_site_is_touched_or_declared`
60, `test_the_report_carries_the_finding` 10, `test_the_guard_survives_the_state` 10 (the
cascade off a red baseline), and one each of
`test_the_generator_would_catch_a_row_under_the_wrong_number`,
`test_the_Carried_table_is_what_the_generator_produces` and
`test_the_CI_section_is_about_the_REVIEWED_commit`. **60 + 10 + 10 + 1 + 1 + 1 = 83**, the
whole count, and every id is on EG3 state (2)'s list as corrected by EH1 and R644. It
clears at this revision's own commit, not by time, and the closure section carries that
measurement.

**The count is taken at `74c77d1`, which is the VERDICT's commit and not this report's** --
`suite_count.py` runs in a clean worktree at the last commit, so its answer is independent
of this uncommitted revision and re-running it would print the same two numbers.

**Whole suite at `74c77d1`: 2856 passed, 0 failed, 0 skipped.** **The excluded set: 166 passed, 83 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 249 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R709]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R710]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R711]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R712]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R713]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R714]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R715]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R716]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R717]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_the_finding[R718]`
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_carried::test_the_generator_would_catch_a_row_under_the_wrong_number`
- **failed, in the excluded set** `tests.test_report_carried::test_the_CI_section_is_about_the_REVIEWED_commit`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:131]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:486]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/README.md:1]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:222]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:227]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:228]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:229]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:230]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:231]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:232]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:233]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:131]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:179]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:180]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:181]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:182]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R712-scripts/report_joint_reactions.py:120]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:292]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:293]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R713-tests/test_report_carried.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R714-docs/closure/F4.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R714-scripts/ci_section.py:316]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:182]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:183]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:184]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R715-scripts/measure/g41_dynamic.py:36]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R716-docs/reports/F4/step-2.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R716-scripts/write_verdict.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R716-write_verdict.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F2/step-7.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F3/step-3.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F4/step-3.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:172]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:192]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:193]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:194]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:195]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:196]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:197]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:198]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:199]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py:82]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R717-write_verdict.py]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-docs/closure/F4.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-2.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-3.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-1.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-2.md]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:36]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:37]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:38]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:39]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:40]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:41]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2084]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2085]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2086]`
- **failed, in the excluded set** `tests.test_report_carried::test_every_named_site_is_touched_or_declared[R718-write_verdict.py]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[report_file_is_a_directory]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]`
```


# Revision 2 — EX0's committed inputs, EX1's re-derivation, and four findings of my own

Answers: verdict 106 @ 0949047

**2026-10-08.**

## 0. CI at `f07bcb8`, the commit verdict 106 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 106 at `f07bcb8` through the report's own `Answers:` line. Run `37733553932`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1987 | 124 | 0 |
| lint, unit and guards | 1054 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- the verification ladder (failure)

**Failing tests named in the log: 124.**

- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_joint_drop_family_covers_the_whole_domain` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_every_joint_drop_reddens_the_force_gate` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_every_NON_VACUOUS_joint_drop_reddens_the_moment_gate` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_VACUOUS_moment_members_are_exactly_the_two_declared_pairs` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T20]` (the verification ladder)

## 0a. Runs since the commit verdict 106 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 106 at `f07bcb8` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37733553932` | push | `f07bcb8` | conclusion **failure** |
| `37790839814` | push | `8ae9acc` | conclusion **failure** |
| `37794940102` | push | `380184e` | conclusion **failure** |
| `37796814444` | push | `d16a46b` | conclusion **failure** |

**Run `37733553932`, conclusion **failure**: 124 failing test name(s) in the log.**
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_force_residual_is_inside_its_ceiling[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_moment_residual_is_inside_its_ceiling[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_joint_drop_family_covers_the_whole_domain` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_every_joint_drop_reddens_the_force_gate` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_every_NON_VACUOUS_joint_drop_reddens_the_moment_gate` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_VACUOUS_moment_members_are_exactly_the_two_declared_pairs` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_reddens_the_force_gate[hub4-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T10]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T12.5]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T14]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T15]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T16.2]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[platform-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub1-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub2-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub3-T20]` (the verification ladder)
- `tests.verification.rung4.test_f4_g41_dynamic::test_the_mass_scale_is_VACUOUS_on_the_moment_channel[hub4-T20]` (the verification ladder)

**Run `37790839814`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_no_tolerance_literals.py::test_no_undeclared_tolerance_reaches_a_comparison[test_f4_g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `37794940102`, conclusion **failure**: 9 failing test name(s) in the log.**
- `tests/test_plan_matches_tolerances.py::test_every_declared_tolerance_appears_in_the_plan[F4_WINDOW_RULE_MIN_EDGE]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `37796814444`, conclusion **failure**: 8 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. The reds, traced

```
claim  verdict 106 judged a tree whose rung 4 was RED, and the red was the finding
cmd    gh run view 37733553932 --json conclusion,jobs --jq '.conclusion,
       (.jobs[] | "\(.name): \(.conclusion)")'
out    conclusion **failure**
out    lint, unit and guards: success
out    the verification ladder: failure
rule   EG3: a boundary red traces by name to the step boundary; anything else is CZ1 (iv)
judge  **this was not a boundary state and I am not claiming it was.** 124 of 126 cases
       errored because the gate reached `HSP-runs`, which is CZ1 (iv) unchanged, and it is
       answered in §2. The tree at THIS revision's commit is measured in §12.
```

## 0c. CI at THIS revision's own commit, which cannot be measured yet (CZ1)

```
claim  the authoritative green for this revision is a pushed CI run at its own sha, and
       that run does not exist while this sentence is being written
cmd    gh run list --commit <this revision's sha>
out    (nothing -- the commit does not exist yet)
rule   CZ1: a check whose input is the commit itself cannot be measured before the commit
       exists, and "I ran it before committing" is not a measurement for that class
judge  **this is the one section of this report that cannot be complete when it ships.**
       The two preceding commits are measured: `8ae9acc`'s ladder went GREEN (section 2,
       which is R721 closed) and its guards job went red on two items, one of which was
       the bare `2.0` fixed in `380184e` and one of which was the answers file shipped
       ahead of this report. `380184e`'s own run and this revision's are read after they
       exist and carried in the next revision's section 0, which is where CZ1 (iv) puts
       them. I am not claiming a green I have not read.
```

## 1. The schedule, and what the STOP cost

**Step 3's working target is now 16 October (EX4, was 14) and it holds.** Today is 8 October.
**This is round 2 of three and one revision remains.** EX0's data path, EX1's re-derivation,
EX2 and EX3 are built and green; EV2's items 2 to 5 — the member-force table, R638,
R637(iii)/R648 and `docs/closure/F4.md` — are not started. The table may start now that the
npz exists (EX5) and is the next thing.

**Verdict 106's STOP was right and I verified all four findings before accepting them.**
R721, R722, R723 and R724 each reproduced. The plan re-locked in `c8cb5f6`, a standalone
`plan:` commit (DK0: a re-lock inside a step does not restart the round count).

## 1a. R719 and R720, closed before this revision

Verdict 105 held on both. They were answered in `becf47c`, `7799482` and `801796e`, and
verdict 106 — an ES0 interim check — did not re-raise either.

```
claim  both counters measure the SIGNAL, the difference from the clean residual, and the
       shipped module still does
cmd    grep -c "the DIFFERENCE from the clean residual" scripts/f4_dynamic_residual.py
out    1
cmd    python scripts/f4_dynamic_residual.py
out    weakest     : 0.017528231438113724  at ('drop', 'hub3/8', 10.0)
rule   R719/R720: a counter's response is `|resid_injected - resid|`, never the absolute
       residual, which includes the clean floor
judge  R719 refuted my round-1 headline — the window rule IS satisfiable on the moment
       channel — and R720 refuted "the response is linear in the scale". Both corrections
       survive into EX0's recompute: the drop signal is `contrib_p` exactly, and the mass
       signal is the closed form, so neither can pick the floor back up.
```

## 2. R721 — the gate was green on one machine, and the number that says so

```
claim  the HSP-dependent gate passed locally and errored on 124 of 126 cases in CI
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q -p no:randomly
out    126 passed, 1 warning in 1539.78s (0:25:39)
cmd    gh run view 37733553932 --log-failed | grep -oE "run_rung: [0-9]+ collected.*"
out    run_rung: 354 collected, 0 failed, 124 errored, 0 skipped
out    conclusion **failure** -- the ladder job's, with the guards job green
cmd    git ls-files | grep -c "HSP-runs\|platform_rao_pilot"
out    0
rule   a rung-4 gate must run without an HSP worktree
cell   one variable: becf47c ladder 4 SUCCESS; f07bcb8 ladder 4 FAILURE; the gate file
judge  R670 for the second time in this directory, and `test_f4_static_and_mapping.py:848`
       and `:1028` already said so in their own words. I read neither before writing it.
```

**EX0's answer, and the number that matters:**

```
claim  the gate now runs from committed inputs, with no HSP on its path
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q -p no:randomly
out    112 passed in 1.22s
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q --collect-only
out    112 tests collected in 0.10s
rule   EX0(b): recompute LIVE from `data/f4/dynamic_inputs.npz`; refuse on absence or a sha
       mismatch; never skip
judge  **1539.78 s to 1.22 s**, and the 25 minutes did not move to CI -- they moved to an
       on-demand script. Collection reads no npz, so a missing file is a reported refusal
       rather than a collection error that takes the rung down with it.
```

**The refusal is exercised on four paths, none of them conditional:**

```
claim  absence, a sha mismatch, a provenance with no digest, and an absent provenance all
       raise `InputsMissing`
cmd    python -m pytest "tests/verification/rung4/test_f4_g41_dynamic.py::test_the_inputs_REFUSE_rather_than_skip" -q
out    1 passed
rule   EX0(b): refuse, never skip -- a skipped gate reports green
judge  the first version guarded the sha half behind `if NPZ.exists()`, so on a machine
       without inputs it would have passed having checked ONE of two refusals. `load()`
       verifies the digest before it reads the archive, so none of it needs a real npz.
```

**And R721 is now a check rather than a sentence (CW0):**

```
claim  the module the gate imports reaches nothing but numpy and the stdlib, asserted from
       the AST
cmd    python -m pytest "tests/verification/rung4/test_f4_g41_dynamic.py::test_the_module_the_gate_IMPORTS_reaches_nothing_but_numpy_and_the_stdlib" -q
out    1 passed
rule   CW0: prose in the source tree is a test, a triple, or deleted
judge  the docstring claimed it; nothing checked it. The AST and not the runtime, because
       `sys.modules` would see whatever else the session had already loaded.
```

## 3. R722 — I declared the force ceiling over one of EV1's two counter-cases

```
claim  the mass injection binds five decades below the joint-drop family, and the force
       ceiling, its counter and its EH4 bound were all derived without it
cmd    python scripts/f4_dynamic_residual.py
out    clean worst : 2.112671361106528e-16  at platform/T20
out    family      : 150 live, 0 vacuous
out    weakest     : 3.385828903353713e-08  at ('mass', 'hub3', 10.0)
rule   EV1's window rule over the WHOLE counter family, both edges at least 2x
judge  published against true, at the old `5.0e-9`:
judge      upper edge      2.82742e+07x   ->  6.77166x
judge      EH4 rise bound  7.068550e-02   ->  1.692914e-08   (out by 4.17537e+06x)
judge  and `F4_G41_DYNAMIC_FORCE_COUNTER = 0.1` sat **2.95349e+06x ABOVE** a defect the
       gate asserts it must fail, with the suite green. The measuring script printed the
       word "brackets" one line above the minimum it was excluding from. EH4's weakening
       direction is what caught it, which is what EH4 is for.
```

**Re-declared over both injections:**

```
claim  the new values, and that only the force channel moved
cmd    python -c "from floatfea.tolerances import *; print(F4_G41_DYNAMIC_FORCE,
       F4_G41_DYNAMIC_FORCE_COUNTER, F4_G41_DYNAMIC_MOMENT, F4_G41_DYNAMIC_MOMENT_COUNTER)"
out    2.5e-12 3e-08 0.0002 0.01
cmd    python scripts/f4_dynamic_residual.py
out    force  centre 2.674536e-12, edges at the declared value 11833.4x / 13543.3x
out    moment centre 2.018457e-04, edges 86.0457x / 87.6412x, 42 of 150 vacuous
rule   EV1's window rule; BR0/EV1: a plan row in the same commit
judge  **the moment channel did not move, and that is itself the finding**: there the whole
       mass family is vacuous, so the joint-drop family still binds. Six plan rows in
       section 5a moved with the six values.
```

## 4. The force channel measures round-off, and the entry now says so

This was not asked for. It came out of answering R722 and it changes how one of the
published figures should be read.

```
claim  re-forming the reaction the second way moves the force clean worst by 1.139x and
       onto a different body, while the moment channel is unaffected
cmd    python scripts/f4_dynamic_residual.py   (the npz path)
out    force clean worst 2.112671361106528e-16 at platform/T20
out    moment clean worst 2.324345895610256e-06 at platform/T15
cmd    python scripts/measure/g41_dynamic.py   (the one-matvec path)
out    force clean worst 1.8556070086831165e-16 at hub2/T20
out    moment clean worst 2.3243458955783927e-06 at platform/T15
cell   one variable: the reaction as ONE matvec `g_mid.T @ lam`, or as the SUM over the
       twenty (body, joint) pairs. Algebraically identical. Same npz inputs, same window,
       same solve.
rule   the two forms must agree, which is now `F4_G41_DECOMPOSITION_AGREEMENT`
judge  factor 1.139 and a different body on the force channel; 1.371e-11 relative on the
       moment channel.
```

```
claim  the measured gap IS the force residual, to three digits
cmd    python -c "import sys; sys.path.insert(0,'scripts'); import f4_dynamic_residual as m;
       inp=m.load(); print(max(m.decomposition_gap(inp,i) for i in range(6)))"
out    2.111298e-16
rule   the force clean worst is 2.112671361106528e-16
judge  **the same number.** So the force channel's residual is indistinguishable from
       summation-order round-off: the balance closes to machine precision and there is no
       physical error to measure. **`11833.4x` is the distance from noise to the ceiling,
       not a margin**, and the entry and the plan row now say so. The UPPER edge is the one
       that carries information. The moment channel's figure is a measurement and both of
       its edges carry information -- the asymmetry is recorded in both entries.
```

Two constants hold the two forms together rather than a paragraph asserting they agree:

| constant | value | why |
|---|---|---|
| `F4_G41_DECOMPOSITION_AGREEMENT` | `1.0e-12` | the value the export has enforced since written; `4736x` above the measured worst gap `2.111298e-16` |
| `F4_G41_DECOMPOSITION_AGREEMENT_COUNTER` | `0.1` | drop ONE pair and the two forms differ by that pair's own contribution, so the gap IS the joint-drop signal; weakest over all 120 members `0.14137099995337896`, margin `1.4137x` |

## 5. EX2 and EX3

```
claim  the vacuity assertion's threshold is 2x the global clean worst, not the ceiling
cmd    git diff c8cb5f6..HEAD -- tests/verification/rung4/test_f4_g41_dynamic.py | grep -c "2.0 \* worst"
out    1
rule   EX2: the threshold is where the CLAIM flips. No slack.
judge  it asserted `signal < 2.0e-4` where the claim flips at `4.648692e-06`: `43.0229x` of
       slack, inside which the entry's sentence is false and the test is green (R723).
```

```
claim  the published cause of the 12 vacuous moment members is false in both halves
cmd    (the deck's joints 3, 7, 11, 15)
out    hub1/platform attach_a_body [0.0, 0.0, 0.0]   platform side [ 1,  0, -0.20663]
out    hub2/platform attach_a_body [0.0, 0.0, 0.0]   platform side [ 0,  1, -0.20663]
out    hub3/platform attach_a_body [0.0, 0.0, 0.0]   platform side [-1,  0, -0.20663]
out    hub4/platform attach_a_body [0.0, 0.0, 0.0]   platform side [ 0, -1, -0.20663]
cmd    ls ../HSP-runs/studies/platform-12buoy/floatfea_design_waves/
out    case_T10s_full_H24.2m_head0.csv ... case_T20s_full_H24.2m_head0.csv  (all six head0)
rule   EX3 / R724: the record becomes the x-axis observation plus the untested-heading
       limitation
judge  ALL FOUR hub-platform joints are at their hub's own reference point, so "hub2's and
       hub4's are not" was false. The two vacuous hubs are the two on the **x axis**, which
       is the wave axis, and **the heading never varies across the six cases**, so the
       dependence is untested. Withdrawn in the entry, in the gate's own docstring, and in
       the results label (§ 5b of the plan).
```

## 6. Seven findings of my own, from building EX0

Seven, lettered (a) to (g). Five of them are rule violations I committed while repairing
other people's findings, which is the pattern worth more than any of the counts: the
attention goes to the thing being fixed and the work done *around* the fix inherits none of
the discipline being applied *to* it. That is CP2's subject, and CP2 was written about
prose; these are code.

**(a) `tolerances.py` held the same constant twice and the toolchain did not see it.**

```
claim  two definitions of F4_G41_DYNAMIC_FORCE_COUNTER, the later silently winning, with
       ruff, black and mypy all clean
cmd    grep -c "^F4_G41_DYNAMIC_FORCE_COUNTER: Final" floatfea/tolerances.py
out    1                              (after the repair; it was 2)
cmd    python -m mypy floatfea
out    Success: no issues found in 36 source files      (WITH the duplicate present)
rule   CLAUDE.md: every tolerance lives in this file, once
judge  **`mypy` does not catch a redefined `Final`.** My edit replaced the span from the
       force comment to the next CLASS comment, and the decomposition entry had been
       inserted BETWEEN the force ceiling and its counter -- so the old `0.1` survived
       below the new `3.0e-8` and shadowed it. I found it only by printing the value back
       instead of trusting the edit. A duplicate-definition check would be a meta-test,
       which CZ0 forbids through F6, so it is reported rather than built.
```

**(b) the export shipped a tolerance literal.**

```
claim  the decomposition control was `1.0e-12` written into the script, and the comparison
       now reads the constant
cmd    grep -c "gap > 1.0e-12" scripts/export_f4_dynamic_inputs.py
out    0
cmd    grep -c "gap > F4_G41_DECOMPOSITION_AGREEMENT" scripts/export_f4_dynamic_inputs.py
out    1
cmd    grep -cE "gap > [0-9]" scripts/export_f4_dynamic_inputs.py
out    0
rule   CLAUDE.md: no local literals, no exceptions
judge  **and a bare `grep -c "1.0e-12"` on that file prints 1, not 0** -- the hit is my own
       comment quoting the value in order to document its removal. I drafted this triple
       with `out 0` and the check refuted it. That is the same trap as C1's
       `grep -c "1/length"`, for the third time: a needle that cannot distinguish an
       assertion from a quotation of it proves nothing, so the needle here is the
       COMPARISON and not the number. Found while writing the gate that reads the same
       quantity out of the npz.
```

**(c) the provenance's required HSP tag read `UNKNOWN`.**

```
claim  a field EX0(a) requires was filled with a sentence about the field being unavailable
out    "hsp_tag": "UNKNOWN -- no HSP checkout beside this one"
cmd    for d in ../*/; do git -C "$d" describe --tags --always --dirty; done
out    ../HSP-runs     floatfea-ref-1
out    ../HSP-stable   floatfea-ref-1
out    ../HSP_code     floatfea-ref-1-99-gc2fe24f-dirty
cmd    python -c "...; import floatsim; print(floatsim.__file__)"
out    C:\\Users\\xlama\\OneDrive\\Documents\\buoy\\HSP-runs\\floatsim\\__init__.py
rule   EX0(a): the provenance carries the HSP tag
judge  I guessed `../HSP`, which does not exist. **Three checkouts sit beside this tree at
       two different states**, so guessing a directory name was the wrong method:
       `_hsp_tag()` now asks the imported module where it came from, which cannot name the
       wrong one. I rejected a `--provenance-only` mode to avoid the re-run, because it
       would let an edited measurement path claim it produced an old npz -- which is what
       the staleness gate exists to refuse.
```

**(d) the gate compared edges against a bare `2.0`, and CI found it, not me.**

```
claim  a tolerance literal reached a comparison in the gate I had just written
cmd    python -m pytest "tests/test_no_tolerance_literals.py::test_no_undeclared_tolerance_reaches_a_comparison" -q
out    test_f4_g41_dynamic.py:
out        line 435: comparison against 2.0
out        line 439: comparison against 2.0
rule   CLAUDE.md: every numerical tolerance lives in `floatfea/tolerances.py`. No local
       literals, no exceptions
judge  **the same rule I had caught myself breaking in the export script two hours earlier,
       broken again in the same change, two files away.** I did not run this guard locally
       -- I ran rung 3, rung 4, unit and the prose guard, and this one is in `tests/` root.
       CI ran it. Every red in this stretch was found by a check I had not run, which is
       CZ1's reusable half arriving at a non-closure commit for the third time.
```

The repair is not an annotation. EV1's "both edges at least 2x" is the window rule's own
shape, so it is `F4_WINDOW_RULE_MIN_EDGE`, declared **STRUCTURAL** -- it fires by design,
and an invented counter-case for it would be an invented number (AO2).

```
claim  one constant now serves all three places, because they are one rule
cmd    grep -c "F4_WINDOW_RULE_MIN_EDGE" tests/verification/rung4/test_f4_g41_dynamic.py
       scripts/f4_dynamic_residual.py
out    tests/verification/rung4/test_f4_g41_dynamic.py:4
out    scripts/f4_dynamic_residual.py:5
cmd    python -m pytest tests/test_no_tolerance_literals.py tests/verification/rung4
       tests/verification/rung3/test_tolerance_counter_cases.py -q -p no:randomly
out    512 passed in 3.15s
rule   AO2: a STRUCTURAL entry fires by design and carries NO counter-case
judge  both edge comparisons, EH4's two bounds and EX2's vacuity threshold read it. That
       they are one rule is the whole of R723: asserting vacuity against the CEILING
       instead of against this factor left 43.0229x of slack.
```

**(e) my own import-surface test caught the repair, and the allowance it forced is verified
rather than asserted.**

```
claim  moving the literal into `tolerances.py` made the module import `floatfea`, which the
       test refused
cmd    python -m pytest "tests/verification/rung4/test_f4_g41_dynamic.py::test_the_module_the_gate_IMPORTS_reaches_nothing_but_numpy_and_the_stdlib" -q
out    1 failed    (before the allowance; 1 passed after)
cmd    grep -rEc "^\s*(import|from)\s+(floatsim|platform_rao_pilot)" floatfea/ --include=*.py | grep -v ":0" | wc -l
out    0
rule   CW0: the claim is a test, not a docstring
judge  `floatfea` is now allowed, and **what makes that safe is asserted over the whole
       package rather than assumed**: the test walks every `.py` under `floatfea/` and
       fails if any imports FloatSim or the study pilot, so the allowance cannot become a
       back door to `HSP-runs` through a future edit to some other module. The package's
       only two mentions of FloatSim are prose citations.
```

**(f) I shipped the answers file ahead of the report it describes.**

```
claim  `8ae9acc` staged `docs/reports/F4/step-3-answers.json` without revision 2
cmd    git show --stat 8ae9acc | grep answers
out     docs/reports/F4/step-3-answers.json  | ...
rule   the Carried table is generated FROM the answers file INTO the report; they ship
       together
judge  so `test_the_Carried_table_is_what_the_generator_produces` went red at that commit,
       and the `test_the_guard_survives_the_state` cascade followed off the red baseline.
       **This is not EG3 state (2) and I am not filing it as one** -- state (2) is a verdict
       with no answering report, which is also true here, but this red is mine and would
       have fired regardless. It clears at this revision's commit.
```

**(g) and the repair for (d) shipped without its plan row.**

```
claim  `380184e` declared F4_WINDOW_RULE_MIN_EDGE and gave it no plan row
cmd    python scripts/suite_count.py          (at `380184e`, the commit before the row)
out    2993 passed, 1 failed, 0 skipped -- the one failure being
out    `tests.test_plan_matches_tolerances::test_every_declared_tolerance_appears_in_the_plan[F4_WINDOW_RULE_MIN_EDGE]`
cmd    python -m pytest tests/test_plan_matches_tolerances.py
       tests/verification/rung3/test_tolerance_counter_cases.py
       tests/test_counters_are_injected.py tests/test_no_tolerance_literals.py -q
out    358 passed, 1 warning in 44.77s
rule   BR0/EV1: the plan row goes in the same commit as the value it describes
judge  **in the commit whose entire subject was not breaking the tolerance rule**, and
       immediately after I had moved six plan rows with six values in `8ae9acc` precisely
       so none of them shipped undeclared. I put the seventh value in alone. Added in
       `d16a46b`, a standalone `plan:` commit.
```

**The pattern, which is the part worth keeping.** Five of these seven are rule violations I
committed *while repairing* a finding — (b) the literal in the export while answering R721,
(d) the literal in the gate in the same change, (g) the missing row while answering (d),
(a) the duplicate while re-declaring under R722, (c) the `UNKNOWN` tag while building
EX0(a). CP2 says a repair's *prose* inherits none of the discipline being applied to the
thing it repairs. **These are code, and the same thing is true of it.** Each was caught by
a guard or a pasted command and not by care, which is the argument for the guards and
against relying on me to be careful at the end of a long change.

## 6a. EX0(c)'s determinism comparison, which came out stronger than the rule asks

```
claim  two independent six-case exports produce a BIT-IDENTICAL npz
cmd    python scripts/export_f4_dynamic_inputs.py        (twice, hours apart)
out    run 1  wrote data/f4/dynamic_inputs.npz  sha256 f6961553cf285181...
out    run 3  wrote data/f4/dynamic_inputs.npz  sha256 f6961553cf285181...
out    (full digests compared byte-for-byte; the truncation is the form the script prints,
out     because a 64-character digest contains 10-digit runs that the CI-run guard reads as
out     run numbers -- a false positive on my own data)
rule   EX0(c): fail if the regeneration differs beyond the Q8 golden-file rule
judge  **not "within tolerance" -- byte for byte.** The re-run was forced by the `hsp_tag`
       repair rather than planned as a determinism check, so this is the comparison EX0(c)
       asks for, taken for free. 9.47 MiB, 81 arrays, six cases, two runs.
```

```
claim  the provenance now names the HSP state, and the staleness gate agrees with the tree
out    "hsp_tag": "floatfea-ref-1  (HSP-runs)"
out    "generating_script": {"blob_sha": "927b19571908..."}
cmd    git hash-object scripts/export_f4_dynamic_inputs.py | cut -c1-12
out    927b19571908
rule   EX0(a): the provenance carries the HSP tag; the gate refuses on a generator mismatch
judge  the two shas match, which is the state the staleness test asserts. It was mismatched
       for as long as the `_hsp_tag` repair sat in the tree unexported -- and the test was
       red for exactly that window, which is the test working.
```

## 7. Where EX's letter was not implementable, stated rather than substituted

Three places. None of them changes what is gated; each is recorded because a directive
followed to the letter in these three would have produced a gate that measures the wrong
thing, cannot run, or is unchecked.

**(a) EX0(a)'s array list cannot reproduce the residual the plan locks.**

```
claim  reactions and `M a` alone give the CONTINUOUS balance, not the discrete one
cmd    grep -n "2.393343e-03" scripts/measure/g41_dynamic.py
out    27:force channel read `2.393343e-03` where the locked form reads `1.086249e-16` -- a factor
rule   R711: the plan locks the DISCRETE balance (`newmark.py:414-437`)
judge  thirteen decades. So `base` and `m_xddot` -- the discrete balance's own non-reaction
       terms -- are stored beside EX0(a)'s four. The gated quantity and both ceilings are
       unchanged; this is the minimum state that measures them without a solve.
```

**(b) EX0(c)'s determinism leg has no HSP worktree.**

```
claim  the determinism job runs on a plain runner, so it cannot regenerate the npz
cmd    sed -n '86,90p' .github/workflows/ci.yml
out        runs-on: ubuntu-latest
out        # CK0: BY HAND ONLY. Ten legs are twenty-two minutes of the ninety
out        # this workflow was costing, and they answer a question that moves with
out        # the render, the kernel pin and the environment rather than with a test.
out        if: github.event_name == 'workflow_dispatch'
rule   EX0(c): the leg regenerates and fails beyond the Q8 golden-file rule
judge  the regeneration needs FloatSim, which is why the npz exists at all. So the re-solve
       stays local and on demand; its comparison is in section 6a and came out
       bit-identical. What CI gates instead is the half that actually goes stale -- the
       provenance's recorded blob shas against `git hash-object`, which caught its own
       author (section 6a).
```

**(c) EX0(e)'s "two scripts" is one in this design.**

```
claim  the gate imports one module, and the export is deliberately outside the type check
cmd    grep -c "f4_dynamic_residual" tests/verification/rung4/test_f4_g41_dynamic.py
out    6
cmd    grep -n "export_f4_dynamic_inputs" tests/verification/rung4/test_f4_g41_dynamic.py
out    208:    (`python scripts/export_f4_dynamic_inputs.py --check`) and is pasted in the step
out    242:            "`python scripts/export_f4_dynamic_inputs.py` -- it needs an HSP worktree."
cmd    grep -cE "^\s*(import|from) .*export_f4_dynamic_inputs" tests/verification/rung4/test_f4_g41_dynamic.py
out    0
rule   EX0(e): the scripts the gate IMPORTS must be mypy-clean
judge  the export's two hits are its NAME in a docstring and in a refusal message, and the
       third command is the one that matters: **the gate never imports it, 0 times.** I
       first wrote this triple with `2`, `3` and `30:` from memory and all three were
       wrong -- which is the fourth time in this session, and the reason the counts are
       pasted from the run rather than recalled. It is excluded from `mypy` because its
       FloatSim and `platform_rao_pilot` imports have no stubs and are absent on a runner,
       **which is precisely why it must not be on a gate's path.** That asymmetry is the
       whole repair for R721, so making both files mypy-clean would have meant putting the
       HSP-dependent one somewhere a gate could reach it.
```

## 8. Every named site this round's diff does not touch, declared by name

```
claim  every site a verdict names is either touched by this round's diff or declared
cmd    python scripts/untouched_sites.py
out    71 rows
rule   a site is TOUCHED by the diff or DECLARED `no change` beside its exact token
judge  R721's own sites are mostly declared rather than edited, and that is the shape
       of its repair: the gate's DATA PATH was replaced, so the lines the condition
       named are superseded by a file that did not exist when it was written. The
       generator reads the guard's own site set, so this table cannot enumerate a
       different set than the check does.
```

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R711 | `docs/milestones/F4.md:131` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/README.md:1` | the file is untouched | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:218` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:219` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:220` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:221` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:222` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:223` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:224` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:225` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:226` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:227` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:228` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:229` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:230` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:231` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:232` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:233` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R711 | `scripts/measure/g41_dynamic.py:234` | the file is touched and this line number is the old one | **no change** - closed in revision 1 at `377bace`, and EX0's module carries the same discrete form (S2). These rows are lines in files the rewrite did not land on. |
| R712 | `scripts/measure/g41_dynamic.py:131` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R712 | `scripts/measure/g41_dynamic.py:179` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R712 | `scripts/measure/g41_dynamic.py:180` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R712 | `scripts/measure/g41_dynamic.py:181` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R712 | `scripts/measure/g41_dynamic.py:182` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R712 | `scripts/report_joint_reactions.py:120` | the file is touched and this line number is the old one | **no change** - closure item (S9), and EX0(e) answered the half that mattered: `PLATFORM_MASS_OVERRIDE` is off the gate's path. |
| R713 | `docs/SUPERVISOR.md` | the file is untouched | **no change** - closure item (S9). EW0's state takes no status or conclusion filter. |
| R713 | `scripts/ci_section.py:292` | the file is untouched | **no change** - closure item (S9). EW0's state takes no status or conclusion filter. |
| R713 | `scripts/ci_section.py:293` | the file is untouched | **no change** - closure item (S9). EW0's state takes no status or conclusion filter. |
| R713 | `tests/test_report_carried.py` | the file is untouched | **no change** - closure item (S9). EW0's state takes no status or conclusion filter. |
| R714 | `docs/closure/F4.md` | the file is untouched | **no change** - closure item (S9). `fnmatch` is wider than GitHub's glob, and no tracked path outside the two report directories matches at this tree. |
| R714 | `scripts/ci_section.py:316` | the file is untouched | **no change** - closure item (S9). `fnmatch` is wider than GitHub's glob, and no tracked path outside the two report directories matches at this tree. |
| R715 | `docs/conventions.md:182` | the file is untouched | **no change** - withdrawn in revision 1; these sites are cited as evidence, not edited. |
| R715 | `docs/conventions.md:183` | the file is untouched | **no change** - withdrawn in revision 1; these sites are cited as evidence, not edited. |
| R715 | `docs/conventions.md:184` | the file is untouched | **no change** - withdrawn in revision 1; these sites are cited as evidence, not edited. |
| R715 | `scripts/measure/g41_dynamic.py:36` | the file is touched and this line number is the old one | **no change** - withdrawn in revision 1; these sites are cited as evidence, not edited. |
| R716 | `CLAUDE.md` | the file is untouched | **no change** - a mechanical note needing a directive (S9), not a change to these sites. |
| R716 | `docs/SUPERVISOR.md` | the file is untouched | **no change** - a mechanical note needing a directive (S9), not a change to these sites. |
| R716 | `docs/reports/F4/step-2.md` | the file is untouched | **no change** - a mechanical note needing a directive (S9), not a change to these sites. |
| R716 | `scripts/write_verdict.py` | the file is untouched | **no change** - a mechanical note needing a directive (S9), not a change to these sites. |
| R716 | `write_verdict.py` | the file is untouched | **no change** - a mechanical note needing a directive (S9), not a change to these sites. |
| R717 | `docs/reviews/F2/step-7.md` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `docs/reviews/F3/step-3.md` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `docs/reviews/F4/step-3.md` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:172` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:192` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:193` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:194` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:195` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:196` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:197` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:198` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/ci_section.py:199` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/write_verdict.py` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `scripts/write_verdict.py:82` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R717 | `write_verdict.py` | the file is untouched | **no change** - closure item (S9), and the repair belongs at the PRODUCER, not at these sites. |
| R718 | `docs/closure/F4.md` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `docs/reviews/F3/step-2.md` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `docs/reviews/F3/step-3.md` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `docs/reviews/F4/step-1.md` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `docs/reviews/F4/step-2.md` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:36` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:37` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:38` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:39` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:40` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `scripts/write_verdict.py:41` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `tests/test_report_carried.py:2084` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `tests/test_report_carried.py:2085` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `tests/test_report_carried.py:2086` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |
| R718 | `write_verdict.py` | the file is untouched | **no change** - the fallback was removed in revision 1; these rows are lines the removal did not land on. |

## 9. Closure items, and what earlier rounds closed

**Closed in earlier rounds of this step**, recorded here because the Carried table points
at this section and a pointer that resolves nowhere is worse than none:

```
out    R709  the per-body loop's two assertion directions -- closed at 4b64eaf, accepted
out          by EV0, reproduced in revision 1
out    R710  the wrong-node injection site as a domain coordinate -- closed at 4b64eaf
out    R711  the numerator was the CONTINUOUS balance -- closed in revision 1 at 377bace,
out          and EX0's module now carries the same discrete form (§2)
out    R715  my conventions escalation was overstated -- withdrawn in revision 1
out    R718  the guards' `_judged_commit()` fallback could certify the wrong commit --
out          removed in revision 1
```

**Still carried as closure items**, per CZ0 — fixed once in the step's closure commit, not
re-reviewed item by item, and the step is not held on one:

```
out    R712  ER0's basis is wired in the caller and not at the site. **EX0(e) answers the
out          half that mattered**: `PLATFORM_MASS_OVERRIDE` is no longer a module global
out          the gate's fixture writes -- the export passes it explicitly
out    R713  `run_for()` and `code_identical_run()` apply no status or conclusion filter
out    R714  `fnmatch` is wider than GitHub's glob, and wider is the unsafe direction
out    R716  `scripts/write_verdict.py` cannot write an ES0 interim check on a step whose
out          report does not yet exist
out    R717  `ci_section.py`'s anchor pattern and `write_verdict.py`'s output disagree
out    C2 to C15, C24 to C27  carried from revision 1
```

**And one blocking item carries by name**, because it is (c) — a gate assertion the locked
plan required and nothing makes:

```
out    EV1's THIRD ASSERTION -- FE inertia-relief acceleration against FloatSim's per body
out    -- IS DEFERRED TO F5 BY EX4, with its declarations removed and the deferral recorded
out    in `F4.md` section 8. It is no longer blocking in F4. EX4 settled it.
```

## 10. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R709 | **answered** — §9 | (blocking) -- CLOSED, at the first branch of my condition. Answered at 4b64eaf, |
| R710 | **answered** — §9 | (blocking) -- CLOSED, at both branches of my condition. Answered at 4b64eaf, |
| R711 | **answered** — §9 | and (c) through the generator-is-the-gate carve-out) scripts/measure/g41_dynamic.py MEASURES... |
| R712 | **carried** — §9 | declaration) ER0's BASIS IS WIRED IN THE NEW CALLER AND NOT AT THE SITE, AND THE OVERRIDE'S... |
| R713 | **carried** — §9 | run_for() AND code_identical_run() APPLY NO STATUS OR CONCLUSION FILTER, SO EW0's STATE CAN... |
| R714 | **carried** — §9 | fnmatch IS WIDER THAN GITHUB'S GLOB AND WIDER IS THE UNSAFE DIRECTION.... |
| R715 | **answered** — §9 | THE DOCSTRING'S EVIDENCE FOR "NOT COINCIDENT ON THIS PLATFORM" IS A BUOY FIGURE, AND NO BODY IN... |
| R716 | **carried** — §9 | scripts/write_verdict.py CANNOT WRITE AN ES0 INTERIM CHECK ON A STEP WHOSE REPORT DOES NOT... |
| R717 | **carried** — §9 | scripts/ci_section.py's ANCHOR PATTERN AND scripts/write_verdict.py's OUTPUT DISAGREE, SO THE... |
| R718 | **answered** — §9 | : a gate assertion on WHICH QUANTITY. Latent, and I say so.)... |
| R719 | **answered** — §1a | : a counter and how it is injected, through the generator-is-the-gate carve-out) THE JOINT-DROP... |
| R720 | **answered** — §1a | : how the counter is injected, and the size it has to be) "THE RESPONSE IS LINEAR IN THE SCALE"... |
| R721 | **answered** — §2 | , AND THE STOP) THE WHOLE OF LADDER RUNG 4 IS RED IN CI AT THE REVIEWED COMMIT BECAUSE THE GATE... |
| R722 | **answered** — §3 | : a tolerance value, its counter, and how the counter is injected) THE FORCE CHANNEL CEILING,... |
| R723 | **answered** — §5 | : a gate assertion, on the right quantity at the wrong threshold)... |
| R724 | **answered** — §5 | : the warrant for excluding 12 of 120 counter-family members) THE PUBLISHED CAUSE OF THE MOMENT... |

## 11. Tolerances touched

```
claim  two values moved, two were declared, two were unmoved, and nothing was widened
cmd    git diff 0e4188a..HEAD -- floatfea/tolerances.py | grep -E "^[-+]F4_G41"
out    -F4_G41_DYNAMIC_FORCE: Final[float] = 5.0e-9
out    +F4_G41_DYNAMIC_FORCE: Final[float] = 2.5e-12
out    -F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 0.1
out    +F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 3.0e-8
out    +F4_G41_DECOMPOSITION_AGREEMENT: Final[float] = 1.0e-12
out    +F4_G41_DECOMPOSITION_AGREEMENT_COUNTER: Final[float] = 0.1
rule   EX1: re-derive the force window over BOTH counter families
judge  the force ceiling TIGHTENED by three decades and its counter by six -- both in the
       strengthening direction, because the family they are declared over got larger. The
       moment channel's two values are unmoved. Six plan rows moved with the six values.
cmd    grep -c "^F4_G41_DYNAMIC_FORCE_COUNTER: Final" floatfea/tolerances.py
out    1
judge  and that count is here because it was 2 (§6a).
```

| constant | value | why |
|---|---|---|
| `F4_G41_DYNAMIC_FORCE` | `2.5e-12` | centre `2.674536e-12` over all 150 family members; edges `11833.4x` / `13543.3x` |
| `F4_G41_DYNAMIC_FORCE_COUNTER` | `3.0e-8` | below the weakest live `3.385828903353713e-08`; margin `1.12861x` |
| `F4_G41_DYNAMIC_MOMENT` | `2.0e-4` | unmoved — its mass family is wholly vacuous, so the drop family still binds |
| `F4_G41_DYNAMIC_MOMENT_COUNTER` | `0.01` | unmoved; vacuity now asserted at `2 ×` the clean worst (EX2) |
| `F4_G41_DECOMPOSITION_AGREEMENT` | `1.0e-12` | `4736x` above the measured worst gap `2.111298e-16` |
| `F4_G41_DECOMPOSITION_AGREEMENT_COUNTER` | `0.1` | below the weakest drop-one-pair gap `0.14137099995337896` |

## 12. Lint, types, and the whole suite

```
claim  lint, formatting and types are green at this commit, including the module the gate
       imports
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    124 files would be left unchanged.
cmd    python -m mypy floatfea scripts/f4_dynamic_residual.py
out    Success: no issues found in 37 source files
rule   EX0(e): the scripts the gate imports must be mypy-clean; `ci.yml`'s step now names
       the module, where it was `mypy floatfea`
judge  36 source files to 37 -- the one added file is the module the gate reads. **And
       `mypy` passing is not sufficient for this file**: it reported Success with
       `F4_G41_DYNAMIC_FORCE_COUNTER` declared TWICE in `tolerances.py` (section 6).
```

**And the measurements this revision rests on, each from the shipped path:**

```
claim  the gate, the directory it lives in, and the two data checks
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q -p no:randomly
out    112 passed in 1.22s
cmd    python -m pytest tests/verification/rung4 -q -p no:randomly
out    340 passed in 2.39s
cmd    python -m pytest tests/verification/rung3/test_tolerance_counter_cases.py -q
out    115 passed in 0.33s
cmd    python -m pytest tests/unit -q
out    88 passed in 0.35s
cmd    python -m pytest tests/test_tree_prose_consistent.py -q
out    30 passed in 0.46s
rule   CZ1's reusable half: a check whose input is the commit itself cannot be measured
       before the commit exists
judge  1539.78 s to 1.22 s on the gate, and the 25 minutes moved to an on-demand script
       rather than to CI.
```


**Whole suite at `d16a46b`: 2995 passed, 0 failed, 0 skipped.** **The excluded set: 247 passed, 8 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 255 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_Carried_table_is_what_the_generator_produces`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```

**The eight in the excluded set are EG3 state (2) and they trace by name.** The newest
verdict exists and this revision is its answering report; until this revision is committed,
`test_the_guard_reads_the_step_being_worked_on`'s companions read a report older than the
newest verdict. The list is `test_the_Carried_table_is_what_the_generator_produces` plus
the seven planted states that cascade off its red baseline, which is EH1's state (2) set
and the cascade identified by the baseline being red rather than by name. **They clear at
this revision's commit, and that is measured in the next revision's section 0 (CZ1).**

**One of the eight is mine and not the boundary's**, and I am separating it rather than
filing it under the state: `test_the_Carried_table_is_what_the_generator_produces` went red
at `8ae9acc` because I staged `docs/reports/F4/step-3-answers.json` in that commit without
the report revision it generates into. It would have fired at a non-boundary commit too.
See section 6(f).


# Revision 3 — verdict 107's five, and EY0's table first

Answers: verdict 107 @ fbac279

**2026-10-08.**

## 0. CI at `d09a237`, the commit verdict 107 judged — **report-only; no run by design** — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 107 at `d09a237` through the report's own `Answers:` line. The judged commit touches only paths the workflow ignores (`docs/reports/**`, `docs/reviews/**`), so no run was created for it. **Code-identical run at `d16a46b65122e9f00bdeaf05f31b49c6120188d6`**: run `37796814444`, event `push`, conclusion **failure**.

```
cmd  gh run list --commit d09a2370a258c30e540b3bdf1df15696e83b2e2c
out  (no output)
cmd  git diff --name-only d16a46b d09a237
out  only paths under the workflow's paths-ignore
judge NO RUN BY DESIGN, not CK2 and not a red. The run below measures the same
     code, because every path that differs is one the workflow ignores.
```

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 1053 | 8 | 0 |
| the verification ladder | 2101 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 8.**

- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0a. Runs since the commit verdict 107 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 107 at `d09a237` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37824279365` | push | `4ace816` | conclusion **failure** |
| `37828612962` | push | `af093ae` | **no result** (`cancelled`) |
| `37828831692` | push | `005c6fc` | **no result** (`cancelled`) |
| `37829211436` | push | `7312f2c` | conclusion **failure** |

**Run `37824279365`, conclusion **failure**: 351 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R726->3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R727->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R728->5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R729->6]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_CI_RUN_the_report_names_carries_its_conclusion` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/README.md:1]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:218]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:219]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:220]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:221]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:223]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:224]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:225]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:226]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:234]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:180]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:181]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/report_joint_reactions.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:292]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:293]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-scripts/ci_section.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:183]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:184]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-scripts/measure/g41_dynamic.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F2/step-7.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F3/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F4/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:172]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:192]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:193]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:194]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:195]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:196]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:197]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:198]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:199]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py:82]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:37]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:38]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:39]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:40]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:41]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2084]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2085]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2086]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:439]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:440]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:441]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:442]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:443]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:444]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:445]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:446]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:447]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:448]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R720-scripts/measure/g41_dynamic.py:462]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R720-scripts/measure/g41_dynamic.py:463]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/hsp-coupling.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:745]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:746]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:747]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:748]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:749]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:750]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:751]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:752]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:753]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:754]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:755]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:756]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:757]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:758]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:759]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:760]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:761]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:762]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:763]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:764]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:765]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:766]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:767]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:768]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:769]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:770]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/export_buoy_centers_ref.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:202]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:203]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:204]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/report_joint_reactions.py:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:235]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:236]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:237]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:238]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:239]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:240]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:241]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:242]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:243]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:244]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:245]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:246]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:247]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:248]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:249]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:89]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:90]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:91]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:93]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:94]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:97]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_static_and_mapping.py:848]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:145]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:154]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:155]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:539]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:540]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-floatfea/tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:519]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:520]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:521]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:522]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:312]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:313]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:324]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:325]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:326]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:327]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:328]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:329]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:330]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:331]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:332]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:333]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:334]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:335]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:336]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:337]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:338]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:339]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:340]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:341]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:342]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:343]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-docs/milestones/F4.md:541]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-floatfea/tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-scripts/run_floatsim_design_waves.py:177]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:266]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:267]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:268]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:269]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:266]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:267]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:268]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:269]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-docs/reviews/F4/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:415]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:416]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:417]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:418]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:419]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:420]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:421]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:422]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:423]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:424]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:425]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:427]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:428]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:429]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:430]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:14]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:16]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:17]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:18]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-floatfea/io/integrator.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:154]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:155]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:156]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:157]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:158]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:159]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:224]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:225]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:226]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:234]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:235]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:236]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:237]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:238]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:239]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:240]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:241]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:242]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:243]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:244]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:245]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:246]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:247]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:248]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:249]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:250]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:251]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:252]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:253]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:254]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:255]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:256]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:257]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:258]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:259]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:260]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:261]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:262]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:263]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:264]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:265]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:266]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:267]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-floatfea/tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:527]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:528]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:529]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:530]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:531]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:532]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:533]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:534]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:535]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:536]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-docs/milestones/F4.md:600]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-floatfea/tolerances.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:145]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-tests/verification/rung4/test_f4_g41_dynamic.py:519]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-data/f4/dynamic_inputs.provenance.json:33]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-scripts/f4_dynamic_residual.py:206]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:270]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:271]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:272]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:273]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:274]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:275]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:276]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:277]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:278]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:279]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:280]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:281]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:282]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:283]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:520]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

**Run `37829211436`, conclusion **failure**: 322 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R726->3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R727->4]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R728->5]` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[R729->6]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_CI_RUN_the_report_names_carries_its_conclusion` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_RUN_CONCLUSION_guard_rules_on_the_reviewer_shapes[run_id_as_part_of_a_longer_token]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/README.md:1]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:218]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:219]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:220]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:221]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:223]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:224]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:225]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:226]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R711-scripts/measure/g41_dynamic.py:234]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:131]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:179]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:180]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:181]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/measure/g41_dynamic.py:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R712-scripts/report_joint_reactions.py:120]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:292]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R713-scripts/ci_section.py:293]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R714-scripts/ci_section.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:182]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:183]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-docs/conventions.md:184]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R715-scripts/measure/g41_dynamic.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/SUPERVISOR.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-docs/reports/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R716-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F2/step-7.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F3/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-docs/reviews/F4/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:172]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:192]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:193]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:194]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:195]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:196]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:197]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:198]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/ci_section.py:199]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-scripts/write_verdict.py:82]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R717-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/closure/F4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F3/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-docs/reviews/F4/step-2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:36]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:37]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:38]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:39]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:40]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-scripts/write_verdict.py:41]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2084]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2085]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-tests/test_report_carried.py:2086]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R718-write_verdict.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:439]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:440]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:441]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:442]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:443]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:444]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:445]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:446]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:447]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R719-scripts/measure/g41_dynamic.py:448]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R720-scripts/measure/g41_dynamic.py:462]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R720-scripts/measure/g41_dynamic.py:463]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/hsp-coupling.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/milestones/F4.md:486]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:745]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:746]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:747]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:748]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:749]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:750]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:751]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:752]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:753]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:754]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:755]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:756]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:757]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:758]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:759]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:760]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:761]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:762]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:763]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:764]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:765]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:766]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:767]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:768]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:769]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-docs/reports/F4/step-1.md:770]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/export_buoy_centers_ref.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:202]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:203]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/measure/g41_dynamic.py:204]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/report_joint_reactions.py:81]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:235]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:236]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:237]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:238]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:239]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:240]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:241]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:242]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:243]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:244]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:245]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:246]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:247]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:248]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-scripts/run_rung.sh:249]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:89]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:90]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:91]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:93]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:94]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_g41_dynamic.py:97]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R721-tests/verification/rung4/test_f4_static_and_mapping.py:848]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:145]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:154]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:155]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:539]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-docs/milestones/F4.md:540]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:519]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:520]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:521]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R722-scripts/measure/g41_dynamic.py:522]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:312]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:313]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:314]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:315]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:316]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:317]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:318]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:319]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:320]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:322]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:323]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:324]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:325]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:326]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:327]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:328]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:329]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:330]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:331]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:332]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:333]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:334]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:335]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:336]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:337]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:338]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:339]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:340]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:341]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:342]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R723-tests/verification/rung4/test_f4_g41_dynamic.py:343]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-docs/milestones/F4.md:541]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-scripts/run_floatsim_design_waves.py:177]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:268]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-test_f4_g41_dynamic.py:269]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:268]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R724-tests/verification/rung4/test_f4_g41_dynamic.py:269]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-docs/reviews/F4/step-3.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:415]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:416]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:417]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:418]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:419]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:420]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:421]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:422]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:423]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:424]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:425]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:427]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:428]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:429]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_carried.py:430]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R725-tests/test_report_guard_states.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:13]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:14]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:16]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:17]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:18]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-data/f4/dynamic_inputs.provenance.json:19]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-floatfea/io/integrator.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:150]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:151]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:152]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:153]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:154]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:155]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:156]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:157]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:158]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/export_f4_dynamic_inputs.py:159]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-scripts/measure/g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:224]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:225]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:226]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:227]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:228]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:229]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:230]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:231]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:232]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:233]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:234]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:235]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:236]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:237]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:238]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:239]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:240]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:241]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:242]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:243]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:244]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:245]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:246]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:247]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:248]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:251]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:254]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:255]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:256]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:257]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:258]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:259]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R726-tests/verification/rung4/test_f4_g41_dynamic.py:260]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:529]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R727-tests/verification/rung4/test_f4_g41_dynamic.py:534]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-docs/milestones/F4.md:600]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:145]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:146]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:147]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:148]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R728-scripts/f4_dynamic_residual.py:149]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-data/f4/dynamic_inputs.provenance.json:33]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-scripts/f4_dynamic_residual.py:206]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:270]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:271]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:272]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:273]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:274]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:275]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:276]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:277]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:278]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:279]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:280]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:281]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:282]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:283]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R729-tests/verification/rung4/test_f4_g41_dynamic.py:520]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)

## 0b. The reds, traced

```
claim  the eight reds at the code-identical commit section 0 names are the report-guard
       boundary
cmd    gh run view "$(gh run list --commit d16a46b --json databaseId --jq '.[0].databaseId')"
       --log-failed | grep -oE "FAILED [^ ]+" | sort -u
out    the eight report-guard tests, and nothing else
rule   EG3 state (2): a verdict exists and its answering report does not
judge  **and one of the eight was NOT the boundary, which is R725 and section 2.**
       `test_the_answered_verdict_is_the_NEWEST_one` fired through the guard's
       later-of-the-two branch on a wrong `Answers:` token, not through its ancestry
       carve-out. Revision 2's section 12 called all eight state (2); seven were.
```

## 1. What this revision is, and why its Carried table arrived before its answers

**Step 3's working target is 16 October (EX4) and it holds.** This is **round 3 of three
and the last reviewed revision for this step.** EY3 has pre-decided the outcome: if this
revision's verdict closes step 3 carrying anything, F4 closes and the carried items go to
F5's ledger. **That is a cut, not a slip**, and the committed dates are unchanged.

**EY0 put the member-force table before any further revision-3 work, and it is first.** The
table is sent separately; `scripts/measure/member_forces_table.py` is its script, outside
the gate, reading `data/f4/dynamic_inputs.npz` (EX0(d)).

**This section exists because BS0 is a build failure and not a review finding.** The
moment verdict 107 was committed, the newest report's Carried table was required to list
every open item, and revision 2 — which answers verdict 106 and has its own final verdict
— must not be edited after it (EK3). So revision 3 opens with its Carried table and its
substantive answers follow. The ordering is the hook's, not a choice, and it is recorded
rather than left to look like an answer that is missing.

## 2. R725 — the `Answers:` line named the wrong commit, and a generator published a green table for a red one

```
claim  revision 2's `Answers:` line named the commit verdict 106 REVIEWED, not the one it
       was WRITTEN at, and the CI section anchors through that token
cmd    git log --oneline -1 0949047
out    0949047 review: F4 step 3 -- INTERIM CHECK, STOP. Rung 4 is red in CI
cmd    git log --oneline -1 f07bcb8
out    f07bcb8 F4 step 3: the gate EV1's declaration cannot exist without
cmd    grep -n "^Answers:" docs/reports/F4/step-3.md
out    5:Answers: verdict 104 @ 74c77d1
out    710:Answers: verdict 106 @ 0949047
rule   the `Answers:` line names the VERDICT's own commit; revision 1 got this right, and
       `74c77d1` is a `review:` commit
judge  **what the wrong token produced is the finding, not the token.** `ci_section.py`
       says in its own output that it is "anchored on verdict 106 ... through the report's
       own `Answers:` line", so revision 2 §0 published **"CI at `45e5242` — conclusion
       SUCCESS"** for a verdict that judged `f07bcb8`, where the run reached conclusion
       **failure** with 124 errors. Regenerated against the corrected token it reads
       **"CI at `f07bcb8` — conclusion FAILURE"**, which §0 above now does.
judge2 the two runs are named by COMMIT here and not by id. C29 narrowed the run-id guard
       this round and it immediately caught this paragraph: a bare id belongs in the
       GENERATED sections, which carry it with its conclusion by construction, and §0 does
       exactly that. Anchoring on the commit is also the better citation -- it is the thing
       the verdict and the report both already name.
```

**And I mis-filed the red it caused.** `test_the_answered_verdict_is_the_NEWEST_one` was
among revision 2's eight excluded-set failures, and §12 of that revision called all eight
EG3 state (2). They WERE state (2) at `d16a46b`, where the report was older than the
verdict. At `d09a237` this one fires on the wrong token, through the guard's later-of-the-two
branch rather than its boundary carve-out. **The guard worked and I explained its output
away.** That is R718's class one step further out: removing the fallback closed the
generator trusting a MISSING token, and this is it trusting a PRESENT and wrong one.

## 3. R726 — the committed input could be stale, and recording the closure did not fix it

```
claim  the provenance blob-shaed two files and the npz is a function of twelve
cmd    python -c "import json,pathlib; d=json.loads(pathlib.Path(
       'data/f4/dynamic_inputs.provenance.json').read_text()); print(len(d['import_closure']))"
out    12
rule   EX0(a)/R726: the provenance records every input the npz is a function of
judge  the reviewer constructed the stale-but-accepted state rather than arguing it:
       `scripts/report_joint_reactions.py`'s `heading_deg` from `0.0` to `90.0` — **the one
       variable EX3/R724 declares untested** — left the gate at `112 passed` and the
       staleness test green, because that file was not one of the two.
```

**And my first repair did not work, which is the part worth recording.**

```
claim  adding `import_closure` to the provenance left the heading edit passing
cmd    (first repair in the tree: WAVE_HEADING_DEG 0.0 -> 90.0, staleness test alone)
out    1 passed in 0.15s
cmd    (after asserting the closure, the same edit)
out    1 failed in 0.56s
rule   a defence is what is CHECKED, not what is recorded
judge  **a field nothing reads is not a defence.** I recorded the closure and went on
       asserting the two named entries, so the measurement that had found the defect still
       passed. The gate now walks every entry and compares it against `git hash-object`.
```

**Three probes, all reddening, one per class of input:**

```
claim  a wave parameter, a solver input and an unrelated closure file each redden
cmd    (WAVE_HEADING_DEG 0.0 -> 90.0)
out    1 failed in 0.56s
cmd    (WAVE_HEIGHT_MODEL_M 0.484 -> 0.5)
out    1 failed in 0.54s
cmd    (a comment appended to floatfea/io/integrator.py, which produces the stored alpha_m)
out    1 failed in 0.55s
cmd    (clean tree)
out    1 passed in 0.41s
rule   EX0(b): absence or staleness is a REFUSAL, never a skip
judge  the wave parameters are single-source constants in `report_joint_reactions.py` now
       and the export READS them, so there is no mirror to diverge — and that file is in
       the closure, which is why the heading edit reddens at all.
```

**Asserting the closure found a fault of my own, in the opposite direction.**

```
claim  `floatfea/tolerances.py` was on the closure, so every tolerance edit demanded a
       regeneration of a 12 MiB golden file
cmd    python -c "import json,pathlib; d=json.loads(pathlib.Path(
       'data/f4/dynamic_inputs.provenance.json').read_text()); print(
       any('tolerances' in k for k in d['import_closure']))"
out    False
cmd    (the npz digest, before and after the dependency was removed)
out    8f17fd40573f3ae5...  /  8f17fd40573f3ae5...
rule   a golden file is regenerated under the Q8 rule, with a written reason — not because
       an unrelated constant moved
judge  **the digest is unchanged across the edit, which proves the dependency was inert for
       the output.** The export imported one tolerance for its own control check; that
       ceiling already lives in the consumer, where `resid_control` is stored precisely so
       `test_the_two_WAYS_of_forming_the_reaction_agree` can make the comparison on the
       arrays that ship. A ceiling in two places is one too many. What stays in the export
       is the structural question it alone can answer — that the shapes match.
```

## 4. R727 — the verdict's mechanism is wrong about the repository and its finding is right

```
claim  a ceiling edited above its counter DOES redden, in rung 3, which is parametrised
       over every ACCURACY entry
cmd    (F4_G41_DECOMPOSITION_AGREEMENT 1.0e-12 -> 0.1413, rung 3 alone)
out    FAILED tests/verification/rung3/test_tolerance_counter_cases.py::
       test_the_ceiling_sits_below_its_counter_case[F4_G41_DECOMPOSITION_AGREEMENT]
out    1 failed, 115 passed in 0.42s
cmd    (the same edit, the gate file alone)
out    112 passed in 1.28s
rule   CZ0 (b): a tolerance value, or the form of one
judge  the verdict says the ceiling exceeds its counter "with nothing red". The GATE FILE
       named two pairs and omitted this one, and the verdict measured the gate file —
       which is a fair thing to measure and an incomplete account of the repository. I am
       not claiming the omission did not matter: the file should be self-sufficient and it
       now discovers every pair.
```

**The finding underneath is larger than its stated mechanism, and that is what I fixed.**

```
claim  the ceiling widens eleven decades with everything green, because it is the one F4
       value outside the window rule and nothing tied it to its measurement
cmd    (the reviewer's ladder: 1e-8, 1e-4, 1e-2, 0.1, 0.1413 -> each 112 passed)
out    1.413e+11x of room, bounded only by the counter-case
cmd    python scripts/f4_dynamic_residual.py   (the worst decomposition gap)
out    2.111298e-16
cmd    (ceiling 1.0e-12 -> 1.0e-11, after the repair)
out    1 failed, 113 passed in 1.48s
rule   a ceiling outside the window rule is justified by its MEASUREMENT or it is not
       justified
judge  `F4_G41_DECOMPOSITION_HEADROOM = 1.0e4` pins it to the measured gap, which the
       declared `1.0e-12` sits `4736x` above. Eleven decades becomes a third of one. **The
       tightening itself stands and the reviewer endorsed it** — the window rule's own
       centre would LOOSEN this ceiling by seven decades on a quantity whose clean value is
       round-off, which is the asymmetry §4 of revision 2 measured.
```

## 5. R728 — one constant, two opposite senses, and my first pin bounded it at 86

```
claim  the factor was read as a floor on a ratio in three places and as a ceiling on a
       signal in one, so every change strengthened one test and weakened the other
cmd    (F4_WINDOW_RULE_MIN_EDGE 2.0 -> 86.0, before the split)
out    112 passed  — and the vacuity assertion back at 1.999e-04
rule   EX2/R723: the vacuity threshold is 2x the global clean worst, where the claim flips
judge  **the direction is what makes this bad.** Raising the edge floor is a STRENGTHENING
       move for the window rule, and it reinstated the whole of R723's `43.0229x` of slack
       somewhere else. The reviewer is correcting its own prior condition here, not the
       work, and it says so.
```

**And my first repair was not enough.**

```
claim  pinning only `factor * clean_worst < ceiling` bounds the factor at 86, not at 2
cmd    (86.0 x 2.324345895610256e-06, against the declared 2.0e-4)
out    1.9989e-04 < 2.0e-4 — passes
cmd    (the reviewer's own measurement)
out    86.0 green, 87.0 red
rule   a pin that admits 43x of the slack it was written to remove has not removed it
judge  I wrote one pin, measured it against the defect, and it passed. Three now, all
       DERIVED and none invented: the factor equals the edge floor by derivation (separate
       constants so a change is loud, equal so neither drifts), the threshold stays below
       the weakest LIVE member, and below the ceiling.
```

```
claim  both constants now redden in BOTH directions, including the strengthening one
cmd    (F4_G41_VACUITY_FACTOR 2.0 -> 86.0 / 3.0 / 1.0)
out    30 failed, 84 passed   (each)
cmd    (F4_WINDOW_RULE_MIN_EDGE 2.0 -> 86.0 / 3.0)
out    30 failed, 84 passed   (each)
cmd    (restored)
out    114 passed in 1.27s
rule   EH4: every boundary is solved in BOTH directions, including the two that weaken a
       gate
judge  the strengthening direction is the one the defect was found in, which is the whole
       argument for EH4 and the reason both probes are here rather than just the loosening
       pair.
```

## 6. R729 — the locked injection size was a literal nothing asserted

```
claim  `mass_eps` reached `tests/` once, inside an f-string in a failure message, and both
       force values are functions of it
cmd    grep -n "mass_eps" tests/verification/rung4/test_f4_g41_dynamic.py
out    586:        f"scaling {body}'s mass by 1 + {inputs.mass_eps:g} at T_full = ..."
out    646:    """R729: `mass_eps` was a literal nothing asserted, and both force values ...
out    653:    assert inputs.mass_eps == F4_G41_MASS_INJECTION_EPS, (
out    654:        f"the committed inputs were made with eps = {inputs.mass_eps!r} and "
out    (four hits AFTER the repair; 586 is the original f-string and the other three are
out     the repair itself. I first wrote `grep -c` expecting 2 and it printed 4 -- the
out     needle counts the fix along with the defect, which is the `1/length` trap again)
cmd    (the reviewer's band over which the suite stays green)
out    [8.8605e-07, 2.8385e-05], across which the window centre moves 5.66x
rule   CZ0 (b): a counter and how it is injected, including its size
judge  the mass response is exactly linear in it and IS the binding member of the force
       family, so the ceiling and the counter both move with it. A number that two declared
       values depend on, mentioned once in a message string, is not declared.
```

```
claim  the declaration is compared against the value the npz was MADE with, not another
       literal
cmd    (F4_G41_MASS_INJECTION_EPS 1.0e-6 -> 2.0e-6)
out    1 failed, 113 passed in 1.47s
rule   EA4: no gate assertion reads its expected value from the object under test
judge  the npz records `mass_eps` from the export's own run, so this compares a declaration
       against a measurement rather than two literals against each other — which is the
       shape BG1's original subject had and the reason `_MEASURED` values are forbidden in
       `tolerances.py` (BE2).
```

**Three plan rows moved with the three values** (BR0/EV1), in section 5a of the plan.

## 7. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R709 | **answered** — §8 | (blocking) -- CLOSED, at the first branch of my condition. Answered at 4b64eaf, |
| R710 | **answered** — §8 | (blocking) -- CLOSED, at both branches of my condition. Answered at 4b64eaf, |
| R711 | **answered** — §8 | and (c) through the generator-is-the-gate carve-out) scripts/measure/g41_dynamic.py MEASURES... |
| R712 | **carried** — §8 | declaration) ER0's BASIS IS WIRED IN THE NEW CALLER AND NOT AT THE SITE, AND THE OVERRIDE'S... |
| R713 | **carried** — §8 | run_for() AND code_identical_run() APPLY NO STATUS OR CONCLUSION FILTER, SO EW0's STATE CAN... |
| R714 | **carried** — §8 | fnmatch IS WIDER THAN GITHUB'S GLOB AND WIDER IS THE UNSAFE DIRECTION.... |
| R715 | **answered** — §8 | THE DOCSTRING'S EVIDENCE FOR "NOT COINCIDENT ON THIS PLATFORM" IS A BUOY FIGURE, AND NO BODY IN... |
| R716 | **carried** — §8 | scripts/write_verdict.py CANNOT WRITE AN ES0 INTERIM CHECK ON A STEP WHOSE REPORT DOES NOT... |
| R717 | **carried** — §8 | scripts/ci_section.py's ANCHOR PATTERN AND scripts/write_verdict.py's OUTPUT DISAGREE, SO THE... |
| R718 | **answered** — §8 | : a gate assertion on WHICH QUANTITY. Latent, and I say so.)... |
| R719 | **answered** — §8 | : a counter and how it is injected, through the generator-is-the-gate carve-out) THE JOINT-DROP... |
| R720 | **answered** — §8 | : how the counter is injected, and the size it has to be) "THE RESPONSE IS LINEAR IN THE SCALE"... |
| R721 | **answered** — §8 | , AND THE STOP) THE WHOLE OF LADDER RUNG 4 IS RED IN CI AT THE REVIEWED COMMIT BECAUSE THE GATE... |
| R722 | **answered** — §8 | : a tolerance value, its counter, and how the counter is injected) THE FORCE CHANNEL CEILING,... |
| R723 | **answered** — §8 | : a gate assertion, on the right quantity at the wrong threshold)... |
| R724 | **answered** — §8 | : the warrant for excluding 12 of 120 counter-family members) THE PUBLISHED CAUSE OF THE MOMENT... |
| R725 | **answered** — §2 | : A RED TEST AT THE REVIEWED COMMIT) REVISION 2 ANSWERS LINE NAMES THE COMMIT VERDICT 106... |
| R726 | **open** — §3 | : a gate assertion, on which quantity) THE STALENESS CHECK READS TWO FILES AND THE NPZ IS A... |
| R727 | **open** — §4 | : a tolerance value and the form of one; and (c): the assertion that would bound it)... |
| R728 | **open** — §5 | : the FORM of a tolerance) F4_WINDOW_RULE_MIN_EDGE = 2.0 IS A FLOOR ON A RATIO IN THREE OF ITS... |
| R729 | **open** — §6 | : a gate assertion that the plan requires and nothing makes; and (b): the size the counter is... |

## 9. Lint, types, and the measurements this revision rests on

```
claim  lint, formatting and types are green, and the gates the repairs touch pass
cmd    python -m ruff check floatfea tests scripts
out    All checks passed!
cmd    python -m black --check floatfea tests scripts
out    126 files would be left unchanged.
cmd    python -m mypy floatfea scripts/f4_dynamic_residual.py
out    Success: no issues found in 37 source files
cmd    python -m pytest tests/verification/rung4 tests/verification/rung3
       tests/test_no_duplicate_tolerance_names.py tests/test_plan_matches_tolerances.py
       -q -p no:randomly
out    812 passed in 10.79s
rule   CZ1's reusable half: a check whose input is the commit itself cannot be measured
       before the commit exists, so the authoritative run is CI at this revision's own sha
judge  126 files to black's 124 of the previous round -- the two added are EY0's table
       script and EY2's meta-test. `mypy`'s 37 is unchanged: neither new file is on a
       gate's import path, and the export deliberately is not.
```

**EY2's exception, and EY0's deliverable, measured:**

```
claim  the duplicate-name check reddens on the actual R722 defect, and EY0's table runs
cmd    (the duplicate line appended to tolerances.py)
out    FAILED tests/test_no_duplicate_tolerance_names.py::
       test_no_name_in_tolerances_is_assigned_twice
cmd    python -m pytest tests/test_no_duplicate_tolerance_names.py -q
out    8 passed in 0.03s
cmd    python scripts/measure/member_forces_table.py
out    wrote docs/F4_member_forces.csv (1200 rows); wrote docs/F4_member_forces.md
rule   R430: a guard that cannot be shown to fail certifies nothing
judge  and EY2's own counter-case caught my parser -- `X, Y = 1.0, 2.0` is an `Assign` with
       a `Tuple` target and the first version read only `ast.Name`, so it saw no binding at
       all. No entry in `tolerances.py` is written that way today, which is why the
       omission would have sat there.
```

## 9a. The whole suite

**Whole suite at `264c7e5`: 3016 passed, 0 failed, 0 skipped.** **The excluded set: 527 passed, 9 failed, 1 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 537 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
out    the nine, traced
out      test_the_report_carries_a_WHOLE_SUITE_count            -- this line, which did not
out        exist when the run was taken. Self-clearing and it is the reason the run is
out        taken LAST (R309).
out      test_the_guard_survives_the_state[baseline] + 6 planted states
out        -- EG3 state (2)'s cascade off a red baseline, identified by the baseline being
out        red rather than by name (EH1). They clear at this revision's commit.
out      test_the_RUN_CONCLUSION_guard_rules_on_the_reviewer_shapes
out        [run_id_as_part_of_a_longer_token]
out        -- NOT a boundary state and NOT self-clearing. C29 narrowed the run-id guard to
out        standalone tokens as EY1 directs; corpus entry 178 expects a letter-prefixed
out        token to COUNT as a run id, and its own `measured` field names the old
out        lookbehind as the reason. The corpus tree is the reviewer's to write, so the
out        entry is left alone and the disagreement is raised. RED UNTIL RE-RULED.
rule   EG3 (i): the waiver is conditional on the trace, and a red that does not match the
       state's own list is CZ1 (iv) unchanged
judge  eight of the nine are the boundary. **The ninth is a directive and a corpus entry
       disagreeing, which is not mine to resolve** -- C29's instruction and entry 178's
       expectation cannot both hold, and the sha256 false positive is the evidence that
       the entry's reading is a false positive on figures this repository publishes rather
       than a caught obfuscation.
```

**The main suite is green**, and the growth is accounted for rather than noted:

```
claim  the added tests are EY2's exception plus the pins R727 to R729 required
cmd    python -m pytest tests/test_no_duplicate_tolerance_names.py -q
out    8 passed in 0.03s
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q --collect-only
out    114 tests collected        (112 before this round)
rule   the whole-suite line above is the measurement; this is what moved under it
judge  EY2's eight, the gate's two new tests (the decomposition headroom pin and the
       injection-size check), and the rest are parametrisations of the two-sided probes
       R728 needed. No test was removed.
```

## 10. Every named site this round's diff does not touch, declared by name

```
claim  every site a verdict names is touched by this round's diff or declared
cmd    python scripts/untouched_sites.py
out    302 rows, across nineteen findings -- R711 to R729
rule   a site is TOUCHED by the diff or DECLARED `no change` beside its exact token
judge  the list is long because this is the THIRD revision of one step and the
       generator reads the guard's own site set, which does not shrink when a finding
       closes. Four of this round's five findings were answered by replacing a
       MECHANISM rather than by editing the lines a condition cited -- the data path
       (R726), the pin (R727), the split (R728), the declaration (R729) -- so most
       rows are superseded rather than untouched, and each says which.
```

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R711 | `docs/milestones/F4.md:131` | the file is touched and this line number is the old one | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `docs/milestones/F4.md:486` | the file is touched and this line number is the old one | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/README.md:1` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:218` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:219` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:220` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:221` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:222` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:223` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:224` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:225` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:226` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:227` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:228` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:229` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:230` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:231` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:232` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:233` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R711 | `scripts/measure/g41_dynamic.py:234` | the file is untouched | **no change** - closed in revision 1; EX0's module carries the same discrete form. |
| R712 | `scripts/measure/g41_dynamic.py:131` | the file is untouched | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R712 | `scripts/measure/g41_dynamic.py:179` | the file is untouched | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R712 | `scripts/measure/g41_dynamic.py:180` | the file is untouched | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R712 | `scripts/measure/g41_dynamic.py:181` | the file is untouched | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R712 | `scripts/measure/g41_dynamic.py:182` | the file is untouched | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R712 | `scripts/report_joint_reactions.py:120` | the file is touched and this line number is the old one | **no change** - closure item (S8); EX0(e) answered the `PLATFORM_MASS_OVERRIDE` half. |
| R713 | `docs/SUPERVISOR.md` | the file is untouched | **no change** - closure item (S8). EW0's state takes no status or conclusion filter. |
| R713 | `scripts/ci_section.py:292` | the file is untouched | **no change** - closure item (S8). EW0's state takes no status or conclusion filter. |
| R713 | `scripts/ci_section.py:293` | the file is untouched | **no change** - closure item (S8). EW0's state takes no status or conclusion filter. |
| R714 | `docs/closure/F4.md` | the file is untouched | **no change** - closure item (S8). No tracked path outside the report directories matches. |
| R714 | `scripts/ci_section.py:316` | the file is untouched | **no change** - closure item (S8). No tracked path outside the report directories matches. |
| R715 | `docs/conventions.md:182` | the file is untouched | **no change** - withdrawn in revision 1; cited as evidence, not edited. |
| R715 | `docs/conventions.md:183` | the file is untouched | **no change** - withdrawn in revision 1; cited as evidence, not edited. |
| R715 | `docs/conventions.md:184` | the file is untouched | **no change** - withdrawn in revision 1; cited as evidence, not edited. |
| R715 | `scripts/measure/g41_dynamic.py:36` | the file is untouched | **no change** - withdrawn in revision 1; cited as evidence, not edited. |
| R716 | `CLAUDE.md` | the file is untouched | **no change** - a mechanical note needing a directive (S8). |
| R716 | `docs/SUPERVISOR.md` | the file is untouched | **no change** - a mechanical note needing a directive (S8). |
| R716 | `docs/reports/F4/step-2.md` | the file is untouched | **no change** - a mechanical note needing a directive (S8). |
| R716 | `scripts/write_verdict.py` | the file is untouched | **no change** - a mechanical note needing a directive (S8). |
| R716 | `write_verdict.py` | the file is untouched | **no change** - a mechanical note needing a directive (S8). |
| R717 | `docs/reviews/F2/step-7.md` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `docs/reviews/F3/step-3.md` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `docs/reviews/F4/step-3.md` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:172` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:192` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:193` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:194` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:195` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:196` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:197` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:198` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/ci_section.py:199` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/write_verdict.py` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `scripts/write_verdict.py:82` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R717 | `write_verdict.py` | the file is untouched | **no change** - closure item (S8); the repair belongs at the PRODUCER. |
| R718 | `docs/closure/F4.md` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `docs/reviews/F3/step-2.md` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `docs/reviews/F3/step-3.md` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `docs/reviews/F4/step-1.md` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `docs/reviews/F4/step-2.md` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:36` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:37` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:38` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:39` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:40` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `scripts/write_verdict.py:41` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R718 | `tests/test_report_carried.py:2084` | the file is touched and this line number is the old one | **no change** - the fallback was removed in revision 1. |
| R718 | `tests/test_report_carried.py:2085` | the file is touched and this line number is the old one | **no change** - the fallback was removed in revision 1. |
| R718 | `tests/test_report_carried.py:2086` | the file is touched and this line number is the old one | **no change** - the fallback was removed in revision 1. |
| R718 | `write_verdict.py` | the file is untouched | **no change** - the fallback was removed in revision 1. |
| R719 | `scripts/measure/g41_dynamic.py:426` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:439` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:440` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:441` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:442` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:443` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:444` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:445` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:446` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:447` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R719 | `scripts/measure/g41_dynamic.py:448` | the file is untouched | **no change** - closed before revision 2; the shipped module carries the correction. |
| R720 | `scripts/measure/g41_dynamic.py:462` | the file is untouched | **no change** - closed before revision 2. |
| R720 | `scripts/measure/g41_dynamic.py:463` | the file is untouched | **no change** - closed before revision 2. |
| R721 | `../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `CLAUDE.md` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `data/platform/buoy_centers_ref.json` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/hsp-coupling.md` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/milestones/F4.md:486` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:745` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:746` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:747` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:748` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:749` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:750` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:751` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:752` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:753` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:754` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:755` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:756` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:757` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:758` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:759` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:760` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:761` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:762` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:763` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:764` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:765` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:766` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:767` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:768` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:769` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `docs/reports/F4/step-1.md:770` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/export_buoy_centers_ref.py` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/measure/g41_dynamic.py` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/measure/g41_dynamic.py:202` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/measure/g41_dynamic.py:203` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/measure/g41_dynamic.py:204` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/report_joint_reactions.py:81` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:235` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:236` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:237` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:238` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:239` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:240` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:241` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:242` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:243` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:244` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:245` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:246` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:247` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:248` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `scripts/run_rung.sh:249` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:89` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:90` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:91` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:92` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:93` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:94` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:95` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:96` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_g41_dynamic.py:97` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R721 | `tests/verification/rung4/test_f4_static_and_mapping.py:848` | the file is untouched | **no change** - answered in revision 2 by REPLACING the gate's data path, so these sites are superseded rather than edited. |
| R722 | `docs/milestones/F4.md:145` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:146` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:147` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:148` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:149` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:150` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:151` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:152` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:153` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:154` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:155` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:539` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `docs/milestones/F4.md:540` | the file is touched and this line number is the old one | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `scripts/measure/g41_dynamic.py:519` | the file is untouched | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `scripts/measure/g41_dynamic.py:520` | the file is untouched | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `scripts/measure/g41_dynamic.py:521` | the file is untouched | **no change** - answered in revision 2; the repair is the value and the family. |
| R722 | `scripts/measure/g41_dynamic.py:522` | the file is untouched | **no change** - answered in revision 2; the repair is the value and the family. |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:312` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:313` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:314` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:315` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:316` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:317` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:318` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:319` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:320` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:321` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:322` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:323` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:324` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:325` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:326` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:327` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:328` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:329` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:330` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:331` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:332` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:333` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:334` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:335` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:336` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:337` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:338` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:339` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:340` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:341` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:342` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R723 | `tests/verification/rung4/test_f4_g41_dynamic.py:343` | the file is touched and this line number is the old one | **no change** - answered in revision 2 at the threshold, and again here under R728 (S5). |
| R724 | `docs/milestones/F4.md:541` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R724 | `scripts/run_floatsim_design_waves.py:177` | the file is untouched | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R724 | `test_f4_g41_dynamic.py:268` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R724 | `test_f4_g41_dynamic.py:269` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R724 | `tests/verification/rung4/test_f4_g41_dynamic.py:268` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R724 | `tests/verification/rung4/test_f4_g41_dynamic.py:269` | the file is touched and this line number is the old one | **no change** - answered in revision 2 by WITHDRAWING the claim; cited as evidence. |
| R725 | `docs/reviews/F4/step-3.md` | the file is untouched | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `scripts/ci_section.py` | the file is untouched | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:415` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:416` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:417` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:418` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:419` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:420` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:421` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:422` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:423` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:424` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:425` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:426` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:427` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:428` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:429` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_carried.py:430` | the file is touched and this line number is the old one | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R725 | `tests/test_report_guard_states.py` | the file is untouched | **no change** - answered in S2 at the `Answers:` line; these rows are lines the one-token edit did not land on. |
| R726 | `CLAUDE.md` | the file is untouched | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:13` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:14` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:16` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:17` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:18` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `data/f4/dynamic_inputs.provenance.json:19` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `floatfea/io/integrator.py` | the file is untouched | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:148` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:149` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:150` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:151` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:152` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:153` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:154` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:155` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:156` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:157` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:158` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/export_f4_dynamic_inputs.py:159` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `scripts/measure/g41_dynamic.py` | the file is untouched | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:224` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:225` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:226` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:227` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:228` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:229` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:230` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:231` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:232` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:233` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:234` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:235` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:236` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:237` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:238` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:239` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:240` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:241` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:242` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:243` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:244` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:245` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:246` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:247` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:248` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:251` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:254` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:255` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:256` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:257` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:258` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:259` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R726 | `tests/verification/rung4/test_f4_g41_dynamic.py:260` | the file is touched and this line number is the old one | **no change** - answered in S3 by asserting the whole import closure, so the sites the condition names are superseded by a check over all twelve. |
| R727 | `tests/verification/rung4/test_f4_g41_dynamic.py:529` | the file is touched and this line number is the old one | **no change** - answered in S4 by pinning the ceiling to its measurement; the bracket test now DISCOVERS pairs, so a named site is no longer the unit. |
| R727 | `tests/verification/rung4/test_f4_g41_dynamic.py:534` | the file is touched and this line number is the old one | **no change** - answered in S4 by pinning the ceiling to its measurement; the bracket test now DISCOVERS pairs, so a named site is no longer the unit. |
| R728 | `docs/milestones/F4.md:600` | the file is touched and this line number is the old one | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py:145` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py:146` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py:147` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py:148` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R728 | `scripts/f4_dynamic_residual.py:149` | the file is untouched | **no change** - answered in S5 by splitting the constant; these rows are lines the split did not land on. |
| R729 | `data/f4/dynamic_inputs.provenance.json:33` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `scripts/f4_dynamic_residual.py:206` | the file is untouched | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:270` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:271` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:272` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:273` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:274` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:275` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:276` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:277` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:278` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:279` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:280` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:281` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:282` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:283` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
| R729 | `tests/verification/rung4/test_f4_g41_dynamic.py:520` | the file is touched and this line number is the old one | **no change** - answered in S6 by declaring the constant; the gate reads it from the npz. |
## 8. The items earlier rounds closed, and the closure list

R709, R710, R711, R715 and R718 were closed in revision 1; R719 and R720 before revision 2;
R721, R722, R723 and R724 in revision 2 and accepted by verdict 107. R712, R713, R714, R716
and R717 remain closure items, R712's `PLATFORM_MASS_OVERRIDE` half answered by EX0(e).

```
out    carried closure items   C2 to C15, and C24 to C27
out    added by verdict 107    C28  the force lower edge as a DETECTION THRESHOLD rather
out                                 than a ratio to noise -- the reviewer measured the
out                                 smallest common contrib error that breaches the
out                                 ceiling and it is a real number, so the ratio is the
out                                 wrong thing to publish
out                            C29  the run-id guard narrowed to standalone tokens --
out                                 DONE, in its own process commit, and one corpus
out                                 expectation now disagrees with the directive
out                            C30  `body_mass`, `body_J_G` and `accel` are loaded and
out                                 read by nothing in the gate
out                            C31  a docstring figure one ulp stale against the shipped
out                                 value
out                            C32  revision 2 section 4's cell moves two variables -- it
out                                 compares two SCRIPTS, and inside the npz the effect is
out                                 smaller and on a different body
out                            C33  the mypy ledger states a rule against an instance
rule   CZ0: a closure item is fixed once in the step's closure commit, not re-reviewed
       item by item, and the step is not held on one
judge  C29 is done early because EY1 routed it to its own commit and it was cheap. The rest
       go in the closure commit, which EQ0 makes reviewable because R727 and R728's repairs
       move gates.
```

**Sections 3 to 6 — R726, R727, R728 and R729 — follow the table.**
