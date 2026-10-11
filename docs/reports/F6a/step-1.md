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

**THE EIGHTEENTH IS NOT THE SAME THING AND I CHECKED IT ON ITS OWN**, because a group this
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
