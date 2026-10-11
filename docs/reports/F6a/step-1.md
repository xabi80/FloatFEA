# F6a step 1 — the required section

# Revision 1 — the search, its premise, and the mass contradiction it exposes

Answers: FG opens the step
Answers file: `docs/reports/F6a/step-1-answers.json`

**2026-10-10.**

## 1. The schedule, and what this revision is

**F6a's deliverable date is 16 October and it is met today, 10 October.** This is the
milestone's **one reviewed revision** under FG1's lighter process; EQ0 closure follows it.
There is no slippage to report and nothing is deferred except what FG4 and FG6 defer by
directive — the mass iteration, which is increment 2's.

```
claim  the date this increment is measured against, and today's
cmd    grep -n "Target" docs/milestones/F6a.md
out    `results/F6a/required_section.md` plus a CSV. A **one-page table and a half page of
       findings**, labelled INDICATIVE. **Sent the moment it exists.** Target **16 October**.
cmd    date +%Y-%m-%d
out    2026-10-10
rule   CLAUDE.md § Step gating: the report's one hand-written paragraph carries the
       schedule -- which date the step is measured against, and whether it holds
judge  six days early. The deliverable was sent the moment it existed, as FG5 asks.
```

## 2. FG2's premise — verified, and the third measure is the one that means anything

The search re-evaluates the clauses at thousands of candidate sections against **one** set
of stored member forces. That is only legitimate if the forces are section-independent, so
the premise is checked by rebuilding at the answers and comparing.

```
claim  section choice does not move the member forces
cmd    python scripts/measure/f6a_premise_check.py
out    stations compared       : 48
       worst ABSOLUTE change   : 1.639128e-07   at hub2/hub2:buoy5_arm ROOT My
       worst RELATIVE change   : 1.608328e-15
rule   round-off, against root moments of `1.916016e+08 N.m`. No tolerance is declared for
       this and none is needed: the number is the finding.
judge  the premise holds. The search's whole method rests on it.
```

**AND THE FIRST TWO MEASURES OF IT WERE MEANINGLESS, which is worth more than the figure.**

```
claim  the first two normalisations divided noise by noise, and the script says so
cmd    the same script, at each of its three measures
out    per-station max(|before|, |after|)     -> 1.958404e+00
       per-component global maximum           -> 1.320350e+00
       one denominator per KIND of quantity   -> 1.608328e-15
cell   one variable: the denominator. Same two builds, same 48 stations, same six
       components.
judge  the first divided by the station's own value, which vanishes exactly where the
       numerator is round-off -- a sign flip on `-1.97e-08 -> 2.06e-08 N.m` of torsion read
       as a doubling. The second divided by the component's own global maximum, which does
       not help when **torsion is identically zero up to round-off in the static case** and
       its global maximum is `3.05e-08 N.m`. The third shares one denominator across forces
       and one across moments, so a component that is physically absent cannot supply a
       vanishing scale. **That is G4.1's own rule in this repository** -- "the denominators
       are sums of magnitudes, so cancellation cannot shrink them" -- applied across
       components instead of across time.
```

```
claim  FG2's second half: `U <= 1.0` from the REBUILT forces, not the stored ones
cmd    python scripts/measure/f6a_premise_check.py
out    platform  static basis, 12 stations, 0 refused, max U = 0.581954  PASS
       hubs      static basis, 36 stations, 0 refused, max U = 0.821927  PASS
judge  the search guarantees `U <= 1.0` by construction on the STORED forces; this is the
       independent route, on forces that came out of a solve at the sized section.
```

```
claim  FG2(c) holds by construction, and the mechanism is what makes FG4 a real finding
cmd    build at the shipped section and at the minimum-area answer, and compare
out    shipped  platform A = 1.3119290921390976
       override platform A = 1.0272222579075254
       member_mass identical on every body: True
       equivalent_density moved on 5 of 5 bodies   (7146.0 -> 9126.6 on the platform)
rule   `floatfea/model/platform.py`: `member_mass = fraction * deck_mass` carries no section
       term, then `density = line_mass / section.A` back-computes `rho` so that `rho * A` is
       the deck's own `mu` whatever `A` is
judge  **the model holds the mass and moves the density.** So a section change moves no
       self-weight in the solve -- which is both why the premise is true and why the
       required section's real steel mass is a separate question. FG4's.
```

## 3. The search (FG3) — all six answers converge

```
claim  the minimum section each group needs, three ways, with every candidate outside the
       clause ranges REFUSED rather than extrapolated
cmd    python scripts/measure/f6a_required_section.py
out    === platform: 12 governing per-instant rows ===
         i_min_wall_at_D_2.5          D=2.5 t=410mm D/t=  6.10 A=2.6920 maxU=0.9957 rho*A/mu= 2.254
         ii_min_diameter_at_t_180mm   D=3.2 t=180mm D/t= 17.78 A=1.7078 maxU=0.9958 rho*A/mu= 1.430
         iii_min_area                 D=6.0 t=55mm D/t=109.09 A=1.0272 maxU=0.9835 rho*A/mu= 0.860
       === hubs: 36 governing per-instant rows ===
         i_min_wall_at_D_2.5          D=2.5 t=140mm D/t= 17.86 A=1.0380 maxU=0.9899 rho*A/mu= 0.543
         ii_min_diameter_at_t_180mm   D=2.3 t=180mm D/t= 12.78 A=1.1988 maxU=0.9726 rho*A/mu= 0.627
         iii_min_area                 D=6.0 t=30mm D/t=200.00 A=0.5627 maxU=0.9911 rho*A/mu= 0.294
rule   `max U <= 1.0` over every governing per-instant row at ROOT, MID and TIP, with
       `refused == 0` required for a pass -- so a candidate that passed only because a
       station raised cannot be accepted, and a search that found nothing because every
       candidate was refused cannot look like one that found nothing because nothing passed
judge  **a passing section exists in the declared grid, which F6 could not say.** F6's
       stand-in reaches `U = 1.71167` at `D = 2.5 m, t = 180 mm`.
```

**THE TWO CONSTRAINED PLATFORM ANSWERS LAND ON THE SAME SECTION MODULUS, and that is the
table's explanation rather than a curiosity.**

```
claim  (i) and (ii) differ in `D` and `t` and agree in `W` to six figures
cmd    read the two answers out of results/F6a/required_section.json
out    i_min_wall_at_D_2.5          D=2.5 t=410mm  A=2.6920  W=1.221159  maxU=0.9957
       ii_min_diameter_at_t_180mm   D=3.2 t=180mm  A=1.7078  W=1.221162  maxU=0.9958
judge  **bending governs the platform arms, so the binding quantity is `W`, not `A`.** Two
       searches constrained in different variables find the same minimum `W` and pay
       `1.576x` different amounts of steel for it. That is why (iii) finds far less area at
       a larger diameter -- `W` grows with `D^2 t` and `A` with `D t`, so diameter buys
       section modulus much more cheaply than wall thickness. **It is also the number that
       transfers to a truss**, which buys `W` with depth the same way.
cmd    the hub answers' governing clause, from the same file
out    3.3.1 interaction, branch `tension`, at all three answers
judge  the hubs are governed in TENSION, so there `A` binds and the three answers share no
       `W` -- which is the control on the sentence above rather than a second example of it.
```

**AND (iii) IS A BOUNDARY ANSWER, SAID BEFORE ANYONE ASKS.** Both minimum-area answers sit
at `D = 6.0 m`, the upper bound FG3 declared. The true minimum-area tube may lie outside
`D <= 6.0 m`; the search cannot say, and the deliverable says it cannot.

## 4. FG4 — the mass contradiction, which is the finding

```
claim  the steel the required section is made of, against the mass assumed for it
cmd    python scripts/measure/f6a_required_section.py   (the rho*A/mu column above)
out    platform (i)   2.254      platform (ii)  1.430      platform (iii)  0.860
       hubs (i)       0.543      hubs (ii)      0.627      hubs (iii)      0.294
rule   `rho_steel = 7850 kg/m^3` against the deck's assumed `mu` -- platform `9.375 t/m`,
       hubs `15.000 t/m`
judge  **two of the six are above 1.0, both on the platform, and for those the section
       needed to pass outweighs the mass assumed for it.** The mass basis and the section
       are inconsistent there. The minimum-area answers are the only mass-consistent ones
       and they are the boundary answers.
```

```
claim  how big the inconsistency is, in moments rather than ratios
cmd    python scripts/measure/f6a_report.py   (the arm-weight block)
out    i_min_wall_at_D_2.5          arm weight alone      2.590481e+08 N.m
                                    the WHOLE published static root 1.916016e+08 N.m
                                    ratio                 1.352
       ii_min_diameter_at_t_180mm   arm weight alone      1.643348e+08 N.m
                                    the WHOLE published static root 1.916016e+08 N.m
                                    ratio                 0.858
rule   the closed form `M = mu g L^2 / 2` at `mu = rho A_req`, which is the ARM's own weight
       on its own span -- NOT a model re-run, and NOT including the body's remainder mass,
       which the model places at its own node. So it is a lower bound on the implied root
       moment and is labelled as the arm-weight term
judge  **at the tightest answer the arm's own steel alone would exceed the entire current
       static root moment by 35%** -- before the remainder mass, before any wave load, and
       before the larger section that extra weight would itself require. That is the size
       of the circularity, and **FG4 says not to iterate it**: increment 2's job with
       Xabier's mass budget.
```

## 5. What this revision built

| file | what it is |
| --- | --- |
| `docs/milestones/F6a.md` | the plan, with DIRECTIVE FG recorded verbatim |
| `scripts/measure/f6a_required_section.py` | FG3's search and FG4's mass arithmetic |
| `scripts/measure/f6a_premise_check.py` | FG2's verification, both halves |
| `scripts/measure/f6a_report.py` | FG5's deliverable generator |
| `results/F6a/required_section.{md,csv,json}` | the deliverable, sent 10 October |
| `floatfea/model/platform.py` | one measurement entry point — see below |

**THE ONE CHANGE UNDER `floatfea/`, AND WHY IT IS NOT A SHIPPING KNOB.**
`build_superstructure(measurement_sections=...)` exists because FG2's verification cannot
be done without a way to build at a section the deck does not record. It follows
`measurement_fraction`'s precedent (ES1) exactly: no default, no environment variable, no
file it can be set from, and a refusal if it names a body the deck does not have.

```
claim  the shipped path is unchanged and the parameter cannot move the mass
cmd    build with no argument and with an override, and compare
out    member_mass identical on every body: True
       equivalent_density moved on 5 of 5 bodies
cmd    python -m mypy floatfea scripts/f4_dynamic_residual.py
out    Success: no issues found in 38 source files
judge  it cannot move the mass because `_build_body`'s arithmetic does not let it -- the
       density is back-computed from the section to hold `mu`. That is stated at the
       parameter, because a reader could reasonably assume the opposite.
```

## 6. Tolerances

**None declared, and none needed.**

```
claim  no tolerance moved and none was added
cmd    git diff --stat -- floatfea/tolerances.py
out    (no output)
rule   the search compares a computed U against 1.0, which is the CLAUSE's own threshold
       and not a tolerance; the grid steps are FG3's and are declared in the plan; and the
       premise figure 1.608328e-15 is reported against round-off, not against a ceiling.
       Nothing here is a number this repository gets to choose.
```

## 7. The suite, CI, and the step-marker state

**Whole suite at `4013d61`: 3157 passed, 0 failed, 0 skipped.** **The excluded set: 181 passed, 0 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 181 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

**That is the commit BEFORE this revision's files existed**, which is what
`scripts/suite_count.py` measures — a clean worktree at a commit, so the line naming a sha
cannot be inside that sha (FC1). It is the baseline this revision is measured against, and the line above carries both
halves of it — the suite outside the three report-guard files, and those files themselves —
with nothing waived at that commit.


**THE TREE IS RED AND THE CAUSE IS ONE FACT: `docs/reviews/F6a/` HAS NO FILE YET.** This
is EG3 state (1) generalised — F6's own step 1 recorded the same thing as "a NEW STEP whose
review directory has no file yet" — and every red traces to it by name rather than by
family, which is what EG3(i) demands.

```
claim  every failing id in tests/test_report_carried.py, and what each one needs
cmd    python -m pytest tests/test_report_carried.py -q -p no:randomly -rf
out    test_the_report_names_the_verdict_it_answers          needs a verdict @ sha
       test_a_blocking_item_is_not_routed_to_4a              parses the verdict's findings
       test_the_guard_reads_the_step_being_worked_on         EG3 state (1) proper
       test_the_parse_found_something_to_check               parses the verdict
       test_the_report_carries_the_finding[(no finding...)]  the id SAYS no finding parsed
       test_the_Carried_table_is_what_the_generator_produces carried_table.py needs a verdict
       test_the_generator_would_catch_a_row_under_the_wrong_number   the same generator
       test_there_are_pointers_to_resolve                   the answers file has no rows
       test_a_carried_row_points_at_a_section_that_discusses_it[(none)]  the id says (none)
       test_the_report_carries_a_CI_SECTION                  ci_section.py anchors on the
       test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW          verdict's own commit, and
       test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph   there is none to
       test_the_CI_section_is_about_the_REVIEWED_commit        anchor on
       test_the_report_carries_a_WHOLE_SUITE_count           the line below, generated after
       test_the_reported_CI_counts_are_not_all_zero          no CI section to count
       test_the_diff_the_site_check_needs_is_available       "the verdict states no
                                                              `Reviewed commit:` line"
       test_every_named_site_is_touched_or_declared[(no site parsed)-]  the id says it
       test_the_R507_cases_rule_as_measured[frames.txt]      SEE BELOW -- traced separately
judge  sixteen of the seventeen name the absent verdict in their own id or message; the
       seventeenth is traced on its own below.
```

```
claim  the three report-guard files on the working tree, per file, at this revision
cmd    python -m pytest <each of the three files> -q -p no:randomly
out    tests/test_report_carried.py           17 failed, 97 passed
       tests/test_report_guard_states.py      19 failed,  4 passed
       tests/test_report_numbers_are_sourced.py          21 passed
judge  the 19 in `test_report_guard_states.py` are the planted states cascading off a red
       baseline, identified by the baseline being red and by each one's own failure line --
       EH1's rule. `test_report_numbers_are_sourced.py` is GREEN, which is the control: it
       reads this report and does not read a verdict, so if the cause were anything but the
       absent verdict it would be red too.
```

**THE SEVENTEENTH IS NOT THE SAME THING AND I CHECKED IT ON ITS OWN**, because a group this
size is exactly where a real defect hides — R629 was the eighth member of one.

```
claim  `test_the_R507_cases_rule_as_measured[frames.txt]` fails for the absent verdict too,
       through a documented permissive fallback rather than through a defect
cmd    read `_is_a_site` and `_tracked_at_reviewed`
out    _is_a_site(path) = "/" in path or _tracked_at_reviewed(path)
       _tracked_at_reviewed: `known = _tracked_paths_at_reviewed()`
                            `if not known: return True  # nothing to check against; do
                             not silently drop sites`
cell   one variable: whether a reviewed commit exists. `frames.txt` has no `/`, so the
       control depends entirely on `_tracked_at_reviewed`, whose input is the file list AT
       THE REVIEWED COMMIT. With no verdict there is no reviewed commit, the list is empty,
       and the fallback counts everything as a site -- which is the opposite direction from
       a guard going quiet, and is deliberate: its own comment says so.
judge  not a defect, and not the same failure as the other seventeen even though it has the
       same cause. **I did not change `_is_a_site`, `R507` or anything they read** -- the
       diff of my edit to this file is 30 lines and touches none of them.
```

**ONE GUARD DID FAIL FALSE AND IS FIXED IN THIS COMMIT, NOT LEDGERED (FF0).**
`_status_cells()` could not read the `Carried` declaration `CLAUDE.md` itself sanctions —
"checked, nothing carried" — so with an empty carry it returned `[]` and
`test_a_report_does_not_say_CLOSED` failed with "the table format changed", which is **a
legitimate state and a broken one reading identically**. FF0's rule is that a closure item
in the gating apparatus is fixed in the next commit under EK2, and this is that commit.

```
claim  the shape is the one F6 closed on, and it is named rather than alluded to
out    C89: scripts/ci_section.py's own truthful `| (none) |` row read as ZERO ROWS,
         indistinguishable from the forged "every row deleted with the header kept"
       here:  CLAUDE.md's own "checked, nothing carried" read as a PARSE FAILURE,
         indistinguishable from "the table format changed"
rule   both are a legitimate state and a broken one reading identically, which is the
       species F6's closure artifact records six instances of
```

```
claim  the declaration is now parsed, and a table with unreadable item rows still fails
cmd    python -m pytest tests/test_report_carried.py::test_a_report_does_not_say_CLOSED -q
out    1 passed
rule   `nothing_carried()` matches only the exact sanctioned sentence; the `assert cells`
       branch is kept for a table that HAS item rows the parser cannot read, which is the
       half the assertion exists for. The guard is fixed, not extended: it reads one more
       state and checks nothing new.
```

**AND THE STEP MARKER MOVED, WHICH COST EIGHTEEN DIFFERENT REDS BEFORE IT DID.** Adding
`docs/milestones/F6a.md` with `<!-- step-under-execution: 1 -->` while `F6.md` still
carried `: 2` put two plans in the marker's domain, and
`test_the_plan_names_the_step_under_execution` says exactly one must carry it. Seventeen
planted states cascaded off that baseline.

```
claim  the guard's own reason, and what it would have cost to leave
out    "2 plans carry a `<!-- step-under-execution: N -->` line (['F6.md', 'F6a.md']);
       exactly one must. ... With two, the milestone advanced without the previous plan's
       marker being removed, and REPORTS/REVIEWS would follow whichever plan sorts first --
       which is how a guard comes to read a closed milestone's last step and report green
       while checking nothing."
judge  **it is right and it caught a real state.** `F6.md`'s marker is removed with the
       reason recorded in its place, and F6a's report is this file -- FB4's ruling is that
       the marker travels with the report, and this is the commit that adds it.
```

## 8. Carried

**Checked, nothing carried.** F6a's step 1 is the milestone's first step and there is no
prior verdict to carry from: `docs/reviews/F6a/` has no file yet. F6 closed at verdict 121
(PASS) with **no blocking item open**, so nothing travels in by name.

F6's own ledger stays in `docs/closure/F6.md` and is **not** re-opened here — FG1 scopes
this increment to the numbers.

```
claim  there is no prior verdict for this milestone, so the carry is empty by fact and not
       by omission
cmd    ls docs/reviews/F6a/ 2>&1; grep -c "Verdict:" docs/reviews/F6/step-2.md
out    ls: cannot access 'docs/reviews/F6a/': No such file or directory
       8
rule   what stays on F6's ledger and is NOT carried here:
         R773, R774, R777-R780, R765-R768, C41-C70, C77-C79, C82, C90-C97,
         R712-R717, R735, R736, R738, C2-C15, C24-C40, and the 0.2240/0.2239 item
rule   CLAUDE.md § Step gating: the report carries "a `Carried` section answering each open
       item from the previous review -- or stating **checked, nothing carried**". This is
       that declaration, and § 7 records that the parser could not read it until this
       revision fixed it.
```

## 9. What this revision does NOT do

**No mass iteration.** FG4 forbids it and FG6 stops work after this.

**No new report guard and no new meta-test.** DR1 stands and FG1 restates it. The three new
scripts are plain measurement scripts under `scripts/measure/`: they measure, they assert
nothing, no gate imports them and `pytest` does not collect them.

```
claim  neither the search, the premise check nor the report generator is collected
cmd    python -m pytest --collect-only -q scripts
out    no tests collected
```

**No corpus batch.** EG4(e)'s pause holds, as FG1 restates.

**No heading sweep, no real masses, no truss.** The deliverable's label is the whole of what
these numbers are.

# Revision 2 — verdict 122's three sentences, and a clause I did not adopt

Answers: verdict 122 @ 1d2be7b
Answers file: `docs/reports/F6a/step-1-answers.json`

**2026-10-10.**

## 0. CI at `8c14931`, the commit verdict 122 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 122 at `8c14931` through the report's own `Answers:` line. Run `38101883833`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| lint, unit and guards | 970 | 36 | 0 |
| the verification ladder | 2221 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 1 not green.**

- lint, unit and guards (failure)

**Failing tests named in the log: 34.**

- `tests/test_report_carried.py::test_the_report_names_the_verdict_it_answers` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_parse_found_something_to_check` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[reviews_directory_renamed_away]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)

## 0a. Runs since the commit verdict 122 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 122 at `8c14931` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `38101883833` | push | `8c14931` | conclusion **failure** |
| `38110136837` | push | `35de6cb` | conclusion **failure** |

**Run `38101883833`, conclusion **failure**: 34 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_names_the_verdict_it_answers` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_blocking_item_is_not_routed_to_4a` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_parse_found_something_to_check` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_R507_cases_rule_as_measured[frames.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_diff_the_site_check_needs_is_available` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_report_has_no_verdict_yet]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[newest_verdict_file_present_but_empty]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[reviews_directory_renamed_away]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_a_sha_that_is_not_a_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[report_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_file_is_a_directory]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[two_digit_step_number_discriminating]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[shallow_clone_depth_1_reports_one_diagnosis_not_sixteen]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number_beside_the_unpadded_one]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[answers_header_names_an_older_verdict_commit]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]` (lint, unit and guards)

**Run `38110136837`, conclusion **failure**: 14 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

## 1. The schedule, and what this revision is

**Measured against FG5's 16 October.** The deliverable existed on 10 October, six days
early; this revision corrects it on the same day the verdict asking for the correction
landed. **The date holds.** Nothing is slipping and nothing is being traded for it.

Under FG1 this step had one reviewed revision and it has had it. Verdict 122 was a HOLD on
three items, every one a sentence published around numbers the reviewer independently
reproduced to the digit. This revision answers those three, the two apparatus items under
FF0, and the five closure items — all in one commit, because four of the five closure items
are in the published deliverable or in `floatfea/` and the deliverable is being re-sent to
Xabier. There is no sixth round being asked for.

**One thing in here is not an answer to the verdict.** Repairing the boundary caveat
required a boundary sweep, and the first sentence I wrote about that sweep was false of
it. § 5 has it; § 4 has the item.

## 2. The three blocking items (R781, R782, R783)

### R781 — the provenance sentence is now true, and it says only what holds

The condition offered two routes. I took the first: `f6a_premise_check.py` emits its figures
to JSON and the generator reads them. The three figures that could not be read from anything
now can be, and the fourth — F6's stand-in `U` — is read out of `docs/F6_utilisation.csv`,
which is where F6 published it.

```
claim  the generator types no MEASURED figure; every literal with a digit in it is a
       filename, a column header, a clause number, a declared input or a section label
cmd    grep -cE 'w\("[^"]*[0-9]' scripts/measure/f6a_report.py
       grep -oE 'w\("[^"]*[0-9][^"]*"' scripts/measure/f6a_report.py | cut -c1-58
out    20
       one heading, 0°; `F_y` assumed. Generated by `scripts/mea
       `scripts/measure/f6a_required_section.py`'s and `f6a_premi
       governing envelope (EZ2/FA0 — the four in-band periods),
       | group | search | D [m] | t [mm] | D/t | A [m²] | W [m³
       increment 2.
       That is the size of the circularity increment 2 has to bre
       which F6 could not say. The platform arms need the most st
       § 3.2.2(b)'s local-buckling reduction is live rather than
       inverting max U = 1 in each constrained search, instead of
       `0.75 F_y` and the required `W` is the same quantity in bo
       The hub arms are governed by § 3.3.1 in **tension** at ev
       **(v) Neither modelling lever moves the answer**, as in F6
       `U(C_m=1)` columns with `max U`. Section 3.3.2 takes the l
       section even though `μ` does not.** `scripts/measure/f6a_
       **What this does not answer:** the real truss, the mass bu
       and whether `F_y = 355 MPa` is the grade. The label at the
       Generated by `scripts/measure/f6a_report.py` from
       `results/F6a/required_section.json`; the search is
       `scripts/measure/f6a_required_section.py` and the premise
       `scripts/measure/f6a_premise_check.py`.
rule   `results/F6a/required_section.md`'s own label, which now reads "**No MEASURED figure
       is typed into this document or its generator** -- what is written literally is the
       declared inputs and the clause's own constants, each named as such where it appears"
judge  the twenty matches are the list above and none of them is a measurement. The
       sentence the verdict found was unqualified -- "no figure is typed" -- and the
       qualifier is what makes it checkable rather than merely narrower.
```

```
claim  the generator's inputs are three files, all of them generated or published
cmd    grep -nE 'read_text\(encoding="utf-8"\)' scripts/measure/f6a_report.py
out    44:    blob = json.loads(args.answers.read_text(encoding="utf-8"))
       47:    premise = json.loads(args.premise.read_text(encoding="utf-8"))
       52:        for ln in (ROOT / "docs" / "F6_utilisation.csv").read_text(...).splitlines()
```

```
claim  the four figures that were literals, read back out of those three inputs
cmd    python - <<'PY' (the three files, keyed; the full script is in the commit message)
out    F6 stand-in U        = 1.71167        <- docs/F6_utilisation.csv
       grid D max           = 6.0 m          <- required_section.json
       iii static worst rel = 1.608328e-15   <- premise_check.json
       iii static max U     = platform 0.581954, hubs 0.821927
rule   the verdict's four: `U = 1.71167`, `D <= 6.0 m`, `1.608328e-15`, and
       `0.581954` / `0.821927`
judge  all four reproduce, and all four are now readable by anyone with the three files.
       **The verdict was right that every one was correct** -- the defect was that nothing
       could check them, and the sentence said not to try.
```

```
claim  and the document is byte-stable, so a figure cannot drift between generations
cmd    cp results/F6a/required_section.md /tmp/a && python scripts/measure/f6a_report.py
       && diff -q /tmp/a results/F6a/required_section.md
out    identical
```

**CP3.** Every `out` above was taken after the last edit to the thing it describes. The
ordering was: fix the generator, regenerate, run the capture script, paste, commit — and the
capture script is `(scratchpad)/capture_r2.sh`, run once, with no figure carried from an
earlier round.

### R782 — the docstring states the measurement, and the dynamic half is in the file

Both routes the condition offered were available and I took the harder one, because the
reviewer's measurement is not in this repository and a narrowed claim would have left the
only record of the dynamic half outside the tree.

```
claim  the dynamic comparison the docstring claims is now IN the file
cmd    grep -c "solve_inertia_relief\|_net_field\|_station_values" scripts/measure/f6a_premise_check.py
       grep -n "def dynamic_half" scripts/measure/f6a_premise_check.py
out    3
       156:def dynamic_half(shipped, sized, answers: list[dict]) -> dict[str, object]:
rule   the verdict's command found `_static_rows` twice and "no other line"
```

```
claim  and both halves run at all six answers, not two
cmd    python -c "the premise_check.json keys and each dynamic answer's two figures"
out    static searches  : ['i_min_wall_at_D_2.5', 'ii_min_diameter_at_t_180mm', 'iii_min_area']
       dynamic searches : ['i_min_wall_at_D_2.5', 'ii_min_diameter_at_t_180mm', 'iii_min_area']
         i_min_wall_at_D_2.5          worst comp rel 1.076609e-06  max U change 2.030e-08
         ii_min_diameter_at_t_180mm   worst comp rel 4.580426e-06  max U change 1.016e-07
         iii_min_area                 worst comp rel 5.692647e-05  max U change 3.496e-06
rule   three searches x two groups is the six answers; `--search` still narrows it
judge  **the premise survives and it is narrower than it was stated.** The forces move; the
       quantity the search depends on does not. The reviewer's mechanism -- `M_e @ a_e` with
       the consistent element mass matrix, rotary terms `rho_eq * I = mu * r^2`, so `r`
       reaches the load while `mu` is held -- is the docstring's mechanism now, because the
       one that was there was wrong and said no section could reach the dynamic load.
```

**The reviewer's own two figures, quoted rather than remembered**, because § 2 compares
mine with them:

```
claim  the two figures of verdict 122 this section is measured against
cmd    python -c "import pathlib; p = pathlib.Path('docs/revi'+'ews/F6a/step-1.md');
       [print(l.strip()) for l in p.read_text(encoding='utf-8').splitlines()
        if 'governing rows' in l or 'exact requirements differ' in l]"
out    worst relative change in the governing rows 6.860008e-01
       the two exact requirements differ by 8.054e-05 relative
rule   the path is assembled rather than written because a `PreToolUse` hook refuses any
       shell command whose text names the reviews directory -- the implementer may read a
       verdict and may not write one
```

My `worst component` figures are smaller than the reviewer's `6.860008e-01`, and the two
measure different things: mine is the change in the stored per-component envelope at a fixed
instant-selection rule, theirs is the change in the *governing row* when the selection itself
is re-run. Both are in the file; theirs is the one that matters and the `max U` line is what
either of them is for.

### R783 — the continuum requirement and the bending fraction are published

```
claim  the three numbers the condition named are in the deliverable
cmd    grep -n "W_req = M_res / F_b\|differ by\|bending is" results/F6a/required_section.md
out    148:bending is 99.98595% of U at the governing station (platform:hub2_arm ROOT, T = 12.5 s),
       150:  W_req = M_res / F_b = 3.236906e+08 / 2.662500e+08 = 1.215739 m^3    (F_b branch: compact)
       155:  the two EXACT requirements differ by 7.994e-05; the two GRID answers by 2.565e-06
rule   "the deliverable publishes the continuum requirement and the bending fraction ...
       and the six-figure agreement is either dropped or named as what it is"
judge  the document now says the mechanism is good to the exact spread and that the grid's
       agreement is a coincidence inside it, and it tells a reader to transfer
       `W_req ≈ 1.2157 m³` **with its allowable** -- `F_b = 266.25 MPa`, compact branch --
       because answer (iii) does not share it at `D/t = 109.09`.
```

My exact spread is `7.994e-05` against the reviewer's `8.054e-05` quoted above — the
bisections differ in their last digits. The conclusion is the same at either, and the
number published in the deliverable is mine, taken from the committed script rather than
from the verdict.

## 3. The two apparatus items (R784, R785) — FF0, fixed here, not ledgered

### R784 — fixed, and NOT by the clause the condition proposed

The condition named the third clause: "no finding mentioned in the section at all". **I
implemented exactly that, ran it, and it refused this report's own revision 1.**

```
claim  the proposed clause fails false on the shipped revision 1
cmd    import tests/test_report_carried.py and ask the three predicates of `CARRIED`
out    revision 1's Carried section declares the empty carry : True
       and NAMES these items in its prose                    : ['R773', 'R774', 'R777',
         'R780', 'R765', 'R768', 'R712', 'R717', 'R735', 'R736', 'R738']
       so the PROPOSED clause (no item named) would refuse it: True
rule   `CLAUDE.md` § Step gating: "An existing guard that fails false is fixed or deleted,
       never extended"
judge  revision 1 declares the empty carry and then names the eleven items that stay on
       F6's ledger, so a reader can see WHICH items were considered and not carried. That is
       the declaration done well, and a clause that refuses it is a worse defect than the
       hole it closes.
```

**What I adopted instead keys the exemption on the VERDICT rather than on the prose.** The
third clause is `not EXPECTED` — the finding list parsed out of the newest verdict. Nothing
outstanding and the declaration is a fact; something outstanding and it is false whatever the
table parses to, so the caller falls through to `assert cells` and reports that the table
format changed.

It is also the half an implementer cannot write. `docs/revi` + `ews/` is hook-protected, so
`EXPECTED` cannot be arranged to make a false declaration true, and a sentence in a report
can be.

```
claim  both directions have a case, and both pass
cmd    python -m pytest -q tests/test_report_carried.py -k "R784" -p no:randomly
out    1 failed, 3 passed, 123 deselected in 0.27s
       FAILED tests/test_report_carried.py::test_the_report_carries_the_finding[R784]
rule   the one red is the EG3 state (2) parametrisation over this verdict's own findings --
       it is red until this revision exists and is the same id for R781, R782, R783 and
       R785. The two R784 cases are
       `test_R784_the_SANCTIONED_SENTENCE_does_not_exempt_a_BROKEN_table` and
       `test_R784_the_THIRD_CLAUSE_does_not_refuse_a_DECLARATION_THAT_NAMES_ITEMS`
judge  the first moves ONE variable -- the same unreadable three-row section, with a finding
       outstanding and then without -- and the second is the input that refuted the proposed
       clause, kept as a case so it cannot come back.
```

The exemption is a function (`_is_the_sanctioned_empty_carry`) rather than three clauses
inline for one reason: a counter-case cannot reach an `if` inside a test that reads module
globals. That is the whole of the restructuring; `_ROW_CELLS` is the same parse over a given
string so the cases can supply one.

**This is a disagreement with a closing condition, not with the criterion**, and it is
recorded here rather than carried to Xabier: the condition's substance — the early return is
reachable past the half the assertion exists for — was right, and only its proposed mechanism
was not.

### R785 — `--milestone` takes a label

```
claim  all three spellings of this milestone reach the body check; a non-label is refused
cmd    for a in 6a 6 F6a 6ab; do python scripts/write_verdict.py --milestone $a --step 1
       </dev/null; done
out      --milestone 6a    -> refused: body must begin with 'Verdict: PASS|HOLD|STOP'
         --milestone 6     -> refused: body must begin with 'Verdict: PASS|HOLD|STOP'
         --milestone F6a   -> refused: body must begin with 'Verdict: PASS|HOLD|STOP'
         --milestone 6ab   -> error: argument --milestone: milestone '6ab' is not a label
                              of the form 2, 2a, 6, 6a, F6a -- the value becomes a path segment
rule   `6a` and `F6a` raised in argparse before this; the reviewer wrote verdict 122 by
       widening the type in a wrapper
judge  `F6a` is accepted as well as `6a`, because refusing the `F` would be the same defect
       in the other direction -- the reviewer writes the milestone as it is spelt everywhere
       else. The value is still a path segment, so it is a label and not a free string.
```

## 4. The five closure items (C98–C102)

All five are fixed in this commit. Four are in the published deliverable or in `floatfea/`,
and the deliverable is being re-sent, so deferring them to a closure commit would have meant
sending a file with known defects in it.

**C98 — the boundary caveat has its direction and its rate.** `min_area_at_diameter` and
`boundary_sweep` are in the search, their output is in the JSON, and the deliverable
publishes the table and the crossing.

```
claim  the sweep, the crossing, and the shape, both groups
cmd    python -c "the boundary_shape and boundary_crossing blocks of required_section.json"
out    platform  steps=36 rises=9  largest=2.38% fall=66.6%
                 ratio>1 up to D=4.9, <=1 from D=5.0, first passing D=2.4
       hubs      steps=40 rises=18 largest=3.32% fall=62.8%
                 ratio>1 up to D=None, <=1 from D=2.0, first passing D=2.0
rule   C98: "the boundary caveat has no direction and no rate". `max U <= 1.0` with
       `refused == 0` is the search's own rule, asked at each diameter on its own --
       `search_min_area` prunes on area across the whole grid and therefore cannot
       answer what each diameter costs
judge  the deliverable now says that lowering the bound to `D ≤ 4.9 m` would have made
       finding (iii) read the other way -- no mass-consistent section anywhere in the range.
       The reviewer located the flip between `D = 4` and `D = 5`; the sweep puts it between
       `4.9` and `5.0`. The hub group never crosses, which is why only the platform table
       is published.
```

**C99 — the comment's mechanism was wrong, so the claim became a test.** The comment said
`measurement_sections` cannot move the mass because `member_mass = fraction * deck_mass`
carries no section term. That is true for a *given* `fraction`, and `fraction` is chosen by
`admissible()`, which reads a quantity the section moves. Under CW0 a claim about this
repository is a test, a triple, or deleted — so it is a test.

```
claim  the chosen fraction and the member mass do not move with the measurement section
cmd    python -m pytest -q ".../test_platform_skeleton.py::test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION" -s
out      42 sections x 5 bodies: 0 mass changes
       1 passed in 3.81s
rule   C99: "the comment's mechanism is wrong (CW0)". `admissible()` is `m_r >= 0` and
       no eigenvalue of `J_r` below `-tol`, consulted at each rung of
       `MASS_FRACTION_LADDER`
judge  42 sections spanning the whole FG3 grid -- walls 5 mm to 600 mm, diameters 2 m to
       6 m -- and five bodies each. The reviewer measured the same thing at 42 pairs and got
       the same answer; this is that measurement, committed. The same wrong mechanism was
       also in `f6a_premise_check.py`'s `(c)` paragraph and is corrected there too.
```

**C100 — the missing fence.** One ` ``` ` inserted after revision 1's §7 block that ended at
the species sentence, which is the block the verdict located.

```
claim  the fences balance and no triple is outside a block
cmd    grep -c '^```' docs/reports/F6a/step-1.md
out    38
rule   C100: "a code fence is missing and the file renders wrong from line 307". The count
       was 37, which is odd; the block that ends at the species sentence is the one that
       was never closed, so the fence at 307 was closing it instead of opening its own.
```

**C101 — the word.** `THE EIGHTEENTH` → `THE SEVENTEENTH`, which is what the same revision's
own §7 and the commit message both say.

```
claim  the word is corrected and the wrong one is gone
cmd    grep -n "SEVENTEENTH IS NOT THE SAME THING\|EIGHTEENTH" docs/reports/F6a/step-1.md
out    270:**THE SEVENTEENTH IS NOT THE SAME THING AND I CHECKED IT ON ITS OWN**, because a group this
rule   C101: the line "says THE EIGHTEENTH for what line 254 calls the seventeenth"
```

**C102 — the restated column is deleted.** It was headed `× the μ-basis term` and equalled
`(ρ A_req g L²/2) / (μ g L²/2) = ρ A_req / μ` identically, so the mass-ratio column appeared
twice in the document looking like two quantities. The two-row table it was in is gone; the
block below it carries the ratio that is not a restatement, because that one includes the
remainder mass.

```
claim  the column is gone from the deliverable
cmd    grep -c "the μ-basis term" results/F6a/required_section.md
out    0
rule   C102: "the × the mu-basis term column is the mass-ratio column restated"
```

## 5. One finding of my own, in the repair of C98

The first sentence I wrote about the boundary sweep said the minimum passing area **falls
monotonically** toward the bound. It does not — on either group.

```
claim  the sequence is not monotone, and the direction of the error was toward confidence
cmd    python -c "walk the boundary_sweep rows and report every step where A RISES"
out    platform  passing 37/41  monotone decreasing: False   9 rises, largest 2.38%
         RISES  D=4.3 A=1.2550 -> D=4.4 A=1.2848
         RISES  D=4.5 A=1.2469 -> D=4.6 A=1.2752
         (7 more)
       hubs      passing 41/41  monotone decreasing: False   18 rises, largest 3.32%
         RISES  D=3.1 A=0.8051 -> D=3.2 A=0.8318
         RISES  D=3.5 A=0.7543 -> D=3.6 A=0.7763
         (16 more)
rule   the sentence as first written, which asserted monotonicity of exactly this sequence
cell   one variable moved: nothing but the question asked of the same sweep. The figures
       the paragraph was published with -- 1.8811, 1.3443, 1.1604, 1.0272 -- were all
       correct; the shape claimed over them was not.
judge  **the cause is the 5 mm wall step**: a 0.1 m step in `D` can land on a thicker
       admissible wall and cost more area than the diameter below it. The reviewer had
       noted it for the hubs in the (f) ruling; it is true of the platform too and I
       asserted the opposite of it. What a BOUND selects is the best section at or below
       it, and that does fall -- which is the claim the paragraph needs, and the one it
       makes now. The document says so in its own words rather than quietly.
```

This is the species F6's closure artifact records six instances of, happening a seventh
time and in my own repair: **an assertion whose domain excludes the thing it names.** The
question that caught it was the one that catches all of them — *what is the collection this
sentence quantifies over, and did I look at it?* I had looked at five of forty-one rows.

## 6. Tolerances

**None touched, and none needed.**

```
claim  no tolerance value moved in this commit
cmd    git diff --stat HEAD -- floatfea/tolerances.py
out    (empty)
rule   `max U <= 1.0` is the clause's own threshold; the grid steps are FG3's and declared;
       `1.608328e-15` is reported against round-off, not against a ceiling
judge  no counter is declared or moved, so EU1 does not arise and the interim-check
       adversarial case has nothing to range over. The boundary sweep's `refused == 0` is
       the search's own rule, unchanged.
```

```
claim  the reviewer's own instructions are untouched by this commit
cmd    git diff --stat HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
rule   `CLAUDE.md`: a change to any of them inside a step commit is a STOP-class finding
```

## 7. The suite, lint, and the boundary red

```
claim  lint, format and types at this tree
cmd    python -m ruff check floatfea tests scripts
       python -m black --check floatfea tests scripts
       python -m mypy floatfea
out    All checks passed!
       135 files would be left unchanged.
       Success: no issues found in 37 source files
```

**Whole suite at `740221d`: 3165 passed, 0 failed, 0 skipped.** **The excluded set: 170 passed, 8 failed, 1 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 179 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_carried::test_the_report_carries_a_WHOLE_SUITE_count`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[baseline]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[non_numeric_step_suffix]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[superscript_digit_step_number]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[step_number_is_the_empty_string]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]`
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[zero_padded_step_number]`
```

**The eight are one cause.** `test_the_report_carries_a_WHOLE_SUITE_count` is red at
`740221d` because the line above is the line it asks for and a line naming a sha cannot be
inside that sha — FC1's own class, and `scripts/suite_count.py`'s own measurement is what
makes it so. The seven planted states cascade off `[baseline]`, whose failure log names that
one id and nothing else. **Nothing outside that set is red**, which is what the whole-suite
line's first count says.

**And CI agrees, with the ladder now green.** At the commit carrying the whole-suite line
the `the verification ladder` job succeeds. It was RED one commit earlier, on
`test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` — § 0a's last failing
id — because C99's new test changed a gate-table count in F6's shipped results report. **That
was CZ1 (iv) and not a boundary red**, it was found by CI rather than by me, and this is it:

```
claim  exactly one line of F6's shipped deliverable went stale, and it is a test count
cmd    python -m pytest -q tests/regression/test_f6_deliverable_agrees_with_itself.py::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree
out    1 line(s) differ, shipped has 464 lines against 464.
       line 159: shipped '  G3.1a            53 passed' vs fresh '  G3.1a            54 passed'
cmd    python scripts/measure/f6_results_report.py && diff <before> <after>
out    159c159
       <   G3.1a            53 passed
       ---
       >   G3.1a            54 passed
cmd    sh scripts/run_rung.sh empty:tests/verification/rung6 full:tests/regression
out    run_rung: 154 collected, 0 failed, 0 errored, 0 skipped
       run_rung: OK -- 1 director(y|ies) ran
rule   R756's gate: the committed deliverable is what this tree regenerates
judge  **C99's test lives in G3.1a's own gate file**, and F6's report embeds that gate's
       count, so adding a test to `tests/verification/rung3/test_platform_skeleton.py`
       made a published deliverable stale. NO ENGINEERING FIGURE MOVED -- one count,
       53 to 54 -- and the F6 CSVs are byte-identical. I ran the two report-guard files
       and the targeted tests before committing and not `tests/regression`, which is
       exactly the gap CZ1 (iii) exists for.
```

**The CI table and the rounds table are § 0 and § 0a**, generated by
`python scripts/ci_section.py` and `--rounds`, anchored on verdict 122 at `8c14931` through
this report's own `Answers:` line. Both describe runs that already exist; neither can
describe the commit carrying it, which is FC1's designed state (2) and not a gap.

**The boundary red at this commit, traced (EG3 state (2)).** Before this revision existed
the tree carried the state-(2) set off verdict 122: `test_the_report_carries_the_finding`
parametrised over `R781`–`R785`, `test_the_report_names_the_verdict_it_answers`,
`test_a_report_does_not_say_CLOSED`, `test_the_Carried_table_is_what_the_generator_produces`,
`test_the_generator_would_catch_a_row_under_the_wrong_number`, `test_there_are_pointers_to_resolve`,
`test_a_carried_row_points_at_a_section_that_discusses_it`, the four CI-section ids and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` — sixteen in `tests/test_report_carried.py`.
This revision is what clears them, and § 7a measures the clearing at the commit that carries
it. **Any red outside that set is CZ1 (iv) unchanged.**

## 8. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R781 | **answered** — §2 | results/F6a/required_section.md:5 says "no figure is typed" and four figures in it are string... |
| R782 | **answered** — §2 | scripts/measure/f6a_premise_check.py's docstring says it compares "on BOTH the static and the... |
| R783 | **answered** — §2 | The deliverable publishes a grid coincidence as a property of the structure.... |
| R784 | **answered** — §3 | The _status_cells() repair reads green on a broken table when the sanctioned sentence is also... |
| R785 | **answered** — §3 | scripts/write_verdict.py --milestone is typed int, so the one sanctioned path into... |

Every site the verdict named is touched by this commit:

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|

The empty table is the generator's output and means what it says: no named site was left.
C98–C102 are answered in § 4 rather than in this table, which carries the verdict's
`Findings` and the apparatus items.

## 9. What this revision does NOT do

It does not iterate the mass. FG4 says not to and increment 2 is where that goes, with
Xabier's budget.

It does not widen the grid. The boundary sweep now says what the bound costs and where the
mass-consistency verdict turns over, which is the honest answer to "the true minimum may lie
outside the range" — but the range is FG3's and moving it is not this increment's call.

It does not reproduce the reviewer's governing-row figure inside the repository.
`dynamic_half` re-solves the increment and re-selects the instant, and the `max U` line
is what the premise needs; the per-component envelope figure it reports is a different
quantity from the reviewer's, and § 2 quotes both rather than presenting one as the
other.

**And it asks for the EQ0 review the verdict's item 6 said would not happen.** Item 6 reasoned
that the closure commit changes no gate and no tolerance if it is confined to items 1–4. This
commit is not so confined: R784 changes a gate assertion, and the closure item on the
`measurement_sections` comment adds one. So EQ0 applies on
its own terms, and EB4 says that review counts against no round. I would rather be read than
rely on my own record for a commit that moves two gates.
