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
