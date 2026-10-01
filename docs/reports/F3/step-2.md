# F3 step 2 — G2.1 on real members, and G3.1b's coincidence

Answers: verdict 80 @ 7e5f3fb

**2026-10-01.**

```
rule   the gates this step is measured against, F3 section 5
out    G2.1   the element-local rigid residual and the seventh-mode bound,
out          asserted on every member of the real platform
out    G3.1b  the same mass properties against FloatSim's body definitions,
out          which on this model COINCIDE with G3.1a's (DV0)
```

## 0. CI at `df2c170`, the commit verdict 80 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 80 at `df2c170` through the report's own `Answers:` line. Run `36801064334`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1821 | 0 | 0 |
| lint, unit and guards | 959 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 80 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 80 at `df2c170` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `36801064334` | push | `df2c170` | conclusion **success** |
| `36806980881` | push | `7e5f3fb` | conclusion **success** |
| `36809861340` | push | `ccbd38b` | conclusion **success** |
| `36811916288` | push | `5d93e6c` | conclusion **success** |

## 1. The reading

**Schedule unchanged**, and the dates are in §7 rather than in this sentence. **F3
closes by 13 October: YES**, on the measurements below — G2.1's two halves hold on
the sixteen real members with margins of `2834.26x` and `4.70e+09x`, and the
builder refusal bites on all four injected shapes. One thing is held out of this
step and it is a decision rather than work: see §5.

```
claim  the two margins this answer rests on
out    residual     worst 3.5283e-19 against 1e-15      margin 2834.26x
out    seventh/eps  smallest 9.3791e+11 against 199.526 margin 4.70e+09x
rule   both are asserted per member in §2, which carries the commands
```

This is step 2's first report, so there is no verdict to answer and no `## 0.` CI
section — `scripts/ci_section.py` anchors on an `Answers:` line and there is none
yet. The CI run at this report's own commit is pasted in §8 under CZ1.

## 2. G2.1 on the sixteen real members

**Both halves, element-local, per member.** The gate is
`tests/verification/rung3/test_platform_rigid_modes.py`; the shipped quantities are
new in `floatfea/element/rigid.py`.

```
claim  the residual half, over every member of the real platform
cmd    pytest tests/verification/rung3/test_platform_rigid_modes.py -q, printed
out    worst element rigid residual 3.5283e-19 on hub2:buoy5_arm,
       ceiling 1e-15, margin 2834.26x
rule   element_rigid_residual(k_local, L) <= RIGID_MODE_EXACTNESS, per member

claim  the seventh-mode half, over the same members
out    smallest seventh/eps 9.3791e+11 on platform:hub1_arm, needing 199.526,
       margin 4.700e+09x
rule   seventh_over_epsilon(k_local, L) >= RIGID_MODE_BOUND, per member
judge  neither half is marginal here. What makes the second one a gate rather
       than arithmetic is that an UNRESOLVABLE seventh mode is refused, not
       passed: at that conditioning the question cannot be answered in double
       precision.
```

**The four distinct residuals are four distinct LENGTHS, and I nearly "corrected"
that into a falsehood.** EB0's § 5 text says "four distinct values over sixteen
members, for four distinct lengths". Rounding the lengths to six decimals shows
two, so I set out to withdraw the sentence — and at full precision there are four,
differing by one to three ULP, mapping one-to-one onto the four residuals:

```
claim  the lengths, at full precision, and the residual each one gives
cmd    repr(m.length) and element_rigid_residual, per member, grouped
out    L=50.0                 residual=8.721078e-20   n=4   e.g. platform:hub1_arm
out    L=25.0                 residual=9.673052e-20   n=7   e.g. hub1:buoy1_arm
out    L=25.000000000000004   residual=1.988390e-19   n=4   e.g. hub1:buoy3_arm
out    L=25.000000000000007   residual=3.528257e-19   n=1   hub2:buoy5_arm
cell   two members with the SAME length and the SAME section object give the SAME
       residual; two with lengths differing in the last bits do not --
       `a.section is c.section` is True, `a.length == c.length` is False, and
       `max|k_a - k_c|` is `3.814697e-06`
judge  the sentence is right and the bijection is why. The ULP differences come
       from `math.dist` on the deck coordinates. Recorded because the check I ran
       to refute it is the one that confirmed it, and a rounded print was what
       made it look false.
```

## 3. The builder refuses, which is the half a gate cannot do

`floatfea.model.platform.check_rigid_modes`, called per member after the body's
equivalent material exists. The gate says the sixteen members this deck produces
are sound; the refusal says no other deck can produce one that is not.

```
cell   ONE COUNTER AT A TIME into `local_stiffness`, at 1e-8 of max|k_e|, nothing
       else touched; the builder is asked to build
out    baseline, unmutated                 builds: yes
out    dropped_flip        REFUSED -- platform:hub1_arm: the element-local rigid residual is ...
out    wrong_dof_index     REFUSED -- platform:hub1_arm: the element-local rigid residual is ...
out    rotational_block    REFUSED -- platform:hub1_arm: the element-local rigid residual is ...
out    seventh_mode        REFUSED -- platform:hub1_arm: the first flexible mode sits at ...
out    restored                            builds: yes
rule   F3 § 5: "the builder refuses a platform that fails it"
judge  all four bite, and the fourth is the one that matters for coverage: a
       NEARLY-RELEASED mode is a different injection from a lifted rigid one, so
       the seventh-mode half is exercised by something the residual half cannot
       see.
```

## 4. Two implementations of one formula, and nothing had compared them

`floatfea/element/rigid.py` exists because a refusal in `floatfea/` cannot import
from `tests/`. Rung 1 keeps its own copy — it is F2 apparatus, frozen under DR1,
and is not re-pointed.

```
claim  the shipped residual and rung 1's agree on the real platform's members
cmd    max |shipped - rung1| over the sixteen
out    0.000e+00
rule   one formula, two implementations, and `test_G2_1_the_SHIPPED_residual_
       agrees_with_RUNG_ONEs` is what stops them drifting
judge  bit-identical, which is what it should be: the two bodies are the same
       arithmetic in the same order. The test is there for the commit where that
       stops being true.
```

## 5. WHAT IS HELD OUT, AND IT NEEDS A DIRECTIVE

**F3 § 5 asks for the three counters registered against this gate. Two of the
three cannot see the defect at the size the F2 constant declares.**

```
claim  each counter's worst response over the sixteen members, at the declared size
cmd    inject at RIGID_MODE_EXACTNESS_COUNTER_DEFECT = 1e-14 of max|k_e|,
       take element_rigid_residual, worst over the members
out    dropped_flip      3.6563e-16  = 0.366x the ceiling    NO
out    wrong_dof_index   9.4595e-15  = 9.459x the ceiling    yes
out    rotational_block  1.4644e-17  = 0.0146x the ceiling   NO
cmd    invert the rule and bisect each one for its detection edge
out    dropped_flip      2.735459e-14
out    wrong_dof_index   1.057143e-15
out    rotational_block  6.837686e-13
rule   a counter must redden the gate it defends, and
       `tests/test_counters_are_injected.py`'s two cells both require that
judge  THE DECLARED SIZE SITS BELOW TWO OF THE THREE EDGES. This is not a
       surprise and it is not a contradiction: that constant's own entry
       pre-registered it -- "that counter's size will be bisected against THAT
       gate rather than assumed from this one" -- and `RIGID_MODE_EXACTNESS`'s
       entry says the same. The bisection is above; the choice is below.
```

**Why I did not just declare one.** `CLAUDE.md` puts every numerical tolerance in
`floatfea/tolerances.py`, and `test_plan_matches_tolerances.py::test_every_declared_tolerance_appears_in_the_plan`
then requires a row stating its value in **`docs/milestones/F2.md`** — a closed
milestone's locked plan. So the cheapest-looking path writes an F3 tolerance into
F2's table, which is exactly the cost C40 ledgers and C60 found a fifth instance
of. The options, none of them mine:

* **(a)** declare the size in `tolerances.py` and add the row to `F2.md`'s table,
  accepting that an F3 tolerance lives in a closed plan;
* **(b)** give `F3.md` a tolerance table and re-point that guard at the active
  plan — which EA2 measured as currently red, because F3.md has no table;
* **(c)** derive the injection size from the bisected edge at runtime and mark it
  `not-a-tolerance` in the manner of `WIDEN = 10.0`, which nothing accepts or
  rejects by comparison with.

```
rule   the three options, and what each one costs
out    (a) a row in F2.md's table      -- the cost C40 ledgers
out    (b) a table in F3.md           -- C60 found the fifth instance of the
out                                      hardcoding this would unwind
out    (c) a derived not-a-tolerance  -- the WIDEN = 10.0 precedent
judge  (c) needs no plan edit; whether a derived factor is a tolerance under
       another name is the part that is not mine to decide.
```

Nothing is registered under a size that cannot see the defect, and no tolerance
moved. `tests/test_counters_are_injected.py` is untouched, so its
`len(REGISTERED) >= 4` still holds on the four it already has.

**What is not in doubt:** the gate reddens under all three shapes at a size it can
see (§3's refusal cell is the same three shapes), and the gate itself is green with
the margins in §2.

## 6. G3.1b, and the duplicate I nearly shipped

```
claim  the file the MODEL reads is the file G3.2 gates
cmd    compare floatfea.model.platform.DECK_YAML with
       test_platform_deck_export.DECK_YAML, resolved
out    equal
rule   G3.1b's properties are FloatSim's body definitions only if the deck the
       model reads is the exported one
judge  G3.1b and G3.1a COINCIDE on this model (DV0) and the row is kept with the
       coincidence stated, not left to imply a second witness. A FIRST VERSION
       RE-HASHED THE DECK and was two defects in one: it duplicated
       `test_G3_2_the_committed_deck_matches_its_CONTENT_digest`, which already asserts
       `content_sha(raw) == golden["content_sha256"]`, and it hashed RAW BYTES
       where that test hashes canonical JSON -- so it failed on a correct tree,
       because the committed file is CRLF here and the digest is deliberately
       blind to that. What nothing had asserted is the path identity above: two
       modules each held their own `data/platform/platform12_deck.yaml`.
```

## 7. The remaining F3 steps, with dates

```
rule   the dates this milestone is measured against, DZ7c, unchanged
out    step 2  G2.1 on real members, G3.1b          1 October   -- this report
out    step 3  the counter registration (§5's ruling) and F3's closure artifact
out                                                  7 October
out    F3 closed                                     13 October
out    F4                                            19 October
out    the member-force table                        23 October
out    the code-check screen                         28 October
judge  **F3 closes by 13 October: YES.** Step 2 is the milestone's substantive
       gate and it is green. What remains is §5's ruling, the closure artifact,
       and the closure list -- none of which is a measurement that could fail.
       DZ7c is NOT triggered: nothing is slipping and nothing is being cut. If
       §5's ruling takes option (b), F3.md gains a tolerance table and that is a
       plan edit rather than new work, so the date still holds.
```

## 8. Findings answered

Generated: `python scripts/answered_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R596 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R598 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R599 | carried | **answered** | §9 | `` | carried from an earlier verdict |
| R600 | recorded | **answered** | §9 | `` | DZ2's geometry gate builds its expected endpoint-pair set from the |
| R601 | recorded | **answered** | §9 | `` | CI is RED at the reviewed commit -- `37 failed, 835 passed` in |
| R602 | recorded | **answered** | §9 | `` | `answers_header_names_a_sha_that_is_not_a_commit` is red, and the |
| R603 | recorded | **answered** | §9 | `` | `_seed_older_verdict` runs `git commit` with no author identity while |
| R604 | recorded | **answered** | §9 | `` | The new test's docstring publishes `52 passed` in the very commit that |
| R605 | recorded | **answered** | §9 | `` | C56(i)'s fresh read is |
| R606 | recorded | **answered** | §9 | `` | A FIFTH file hardcoded to F2, and it is the one that enforces BF0. |
| R607 | recorded | **answered** | §9 | `` | The section 8 ordering argument -- THE RULING THE HAND-BACK ASKED FOR. |
| R608 | recorded | **answered** | §9 | `` | `expected_pairs`'s docstring still |
| R609 | recorded | **answered** | §9 | `` | C51's residual: the status stopped over-claiming and the subject beside it |
| R610 | recorded | **carried** | §9 | `` | The harness's anchors are positional |
| R611 | recorded | **withdrawn** | §9 | `` | ) Eight tests are red at the reviewed commit, and the cause is one |
| R612 | recorded | **answered** | §9 | `` | ) CI is red at the reviewed commit, on a line the C59 repair |
| R613 | recorded | **answered** | §9 | `` | , and STOP-class ON THE PLAN -- it carries by name into step 2, and |
| R614 | recorded | **answered** | §9 | `` | Verdict 77's R611 published a closing |
| R615 | recorded | **carried** | §9 | `` | The guard that caught the closure commit can only catch it inside one |
| R616 | recorded | **answered** | §9 | `` | `docs/milestones/F3.md` |
| R617 | recorded | **withdrawn** | §9 | `` | I |
| R618 | recorded | **answered** | §9 | `` | THE NEW EA3 DOCSTRING SAYS THE SLACK IS |
| R619 | recorded | **answered** | §9 | `` | THE SAME DOCSTRING SENDS THE READER TO |
| R620 | recorded | **answered** | §9 | `` | THE EA3 DOCSTRING INTRODUCES THREE |
| R621 | recorded | **answered** | §9 | `` | THE C77 REPAIR IS RIGHT AND ITS DESCRIPTION OVERSTATES IT BY TWENTY.** The commit says "the |
| R622 | recorded | **later** | §9 | `` | EA4's SIX COMMENTS |
| R623 | recorded | **answered** | §9 | `` | THE DZ2 COMMENT |

## 8a. Sites named by findings and not touched

Generated: `python scripts/untouched_sites.py`, which reads the guard's own `SITES` and `TOUCHED` rather than re-deriving them.

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R600 | `docs/reports/F3/step-1.md` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R600 | `floatfea/model/platform.py:551` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R600 | `platform.py:551` | the file is touched and this line number is the old one | **no change** -- the same site as `floatfea/model/platform.py`, cited by bare name in a verdict's prose. See that row. |
| R600 | `tests/test_report_carried.py:320` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:326` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:327` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:328` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:329` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:330` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:331` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:332` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:333` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:334` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:335` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:336` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:337` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:338` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:339` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:340` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:341` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:342` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R600 | `tests/verification/rung3/test_platform_skeleton.py:343` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R601 | `F2.md` | the file is untouched | **no change.** A closed milestone's locked plan. §5 is where this step says what would be needed to add a row to its tolerance table and why that is not the implementer's call. |
| R601 | `docs/reports/F2/step-0.md` | the file is untouched | **no change -- this file has never existed.** It is the path the broken harness constructed when `_step()` returned 0, and the `FileNotFoundError` it raised is the symptom R601 names, not a file to create. |
| R601 | `test_report_carried.py` | the file is untouched | **no change** -- the same site as `tests/test_report_carried.py`, cited by bare name. See that row. |
| R601 | `tests/test_plan_matches_tolerances.py:34` | the file is untouched | **no change, deliberately.** It is the one of the family that does not fail false -- it reads `docs/milestones/F2.md` for a table that is really there -- and it is ledgered as C40. §5 explains why this step did not move it: doing so is one of the three options a new tolerance would force. |
| R601 | `tests/test_report_carried.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R601 | `tests/test_report_guard_states.py:42` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `docs/reports/F3/step-1.md` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R602 | `docs/reports/F3/step-1.md:589` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R602 | `scripts/ci_section.py` | the file is untouched | **no change in step 2.** Re-pointed and given its refusal in `db6a099` under EA2; the line a step-1 finding named predates that hunk. |
| R602 | `tests/test_report_carried.py:309` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:310` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:311` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:312` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:313` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:314` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:315` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:316` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:317` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:318` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:319` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:320` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:321` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:322` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:323` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:324` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:325` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:326` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:2259` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_carried.py:2260` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:392` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:393` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:394` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:395` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:396` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:397` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:398` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R602 | `tests/test_report_guard_states.py:399` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:329` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:330` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:331` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:332` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:333` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:334` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:335` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R603 | `tests/test_report_guard_states.py:336` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R604 | `tests/verification/rung3/test_platform_skeleton.py:372` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R604 | `tests/verification/rung3/test_platform_skeleton.py:373` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R605 | `tests/verification/rung3/test_platform_skeleton.py:383` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R606 | `F2.md` | the file is untouched | **no change.** A closed milestone's locked plan. §5 is where this step says what would be needed to add a row to its tolerance table and why that is not the implementer's call. |
| R606 | `test_plan_matches_tolerances.py` | the file is untouched | **no change** -- the same site as `tests/test_plan_matches_tolerances.py`, cited by bare name. See that row. |
| R606 | `test_report_guard_states.py` | the file is untouched | **no change** -- the same site as `tests/test_report_guard_states.py`, cited by bare name. See that row. |
| R606 | `tests/test_report_numbers_are_sourced.py` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R606 | `tests/test_report_numbers_are_sourced.py:42` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R607 | `docs/reports/F3/step-1.md:990` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R607 | `docs/reports/F3/step-1.md:991` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R607 | `docs/reports/F3/step-1.md:992` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R607 | `docs/reports/F3/step-1.md:993` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R607 | `docs/reports/F3/step-1.md:994` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R607 | `test_ci_workflow_is_wellformed.py:97` | the file is untouched | **no change** -- the same site as `tests/test_ci_workflow_is_wellformed.py`, cited by bare name in a verdict's prose. See that row. |
| R607 | `test_tree_prose_consistent.py:4` | the file is untouched | **no change** -- the same site as `tests/test_tree_prose_consistent.py`, cited by bare name. See that row. |
| R607 | `tests/test_ci_workflow_is_wellformed.py` | the file is untouched | **no change in step 2.** It asserts `docs/reports/**` is in the workflow's `paths-ignore` and reads `.github/workflows`, never a report. The workflow itself moved in `ccbd38b` for EB3, and this file was green at that commit. |
| R607 | `tests/test_report_carried.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R607 | `tests/test_report_guard_states.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R607 | `tests/test_tree_prose_consistent.py` | the file is untouched | **no change.** It states that `docs/reports/` is NOT in its scope, which is what verdict 80 confirmed when it read all four files naming that path. |
| R607 | `tests/verification/rung3/test_tolerance_counter_cases.py` | the file is untouched | **no change.** Named as a file that mentions `docs/reports` in a docstring, which verdict 80 read and found does not read the report's contents. |
| R607 | `tests/verification/rung4/test_writer_round_trip.py` | the file is untouched | **no change.** The same docstring-mention class as the rung-3 hit above. |
| R608 | `floatfea/model/platform.py:343` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R608 | `floatfea/model/platform.py:344` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R609 | `docs/reports/F3/step-1.md:964` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R609 | `docs/reports/F3/step-1.md:965` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R609 | `docs/reports/F3/step-1.md:966` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R610 | `docs/milestones/F2a.md` | the file is untouched | **no change.** The apparatus plan is frozen as a list under DR1, and verdict 80 cited its line 230 as already recording the ruling to leave the hardcoded guards alone until the freeze lifts. |
| R611 | `docs/reports/F3/step-1.md` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R611 | `docs/reports/F3/step-1.md:618` | the file is untouched | **no change, and it may not have one.** Step 1 is CLOSED at PASS (DD1) and its report is the record of what was answered there. Step 2 writes its own report rather than editing a closed step's. |
| R611 | `docs/reviews/F3/step-1.md` | the file is untouched | **no change, and the implementer may not write it.** The verdict file is the reviewer's, through `scripts/write_verdict.py`, and a `PreToolUse` hook refuses edits under that directory. |
| R611 | `tests/test_report_carried.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:380` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:381` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:382` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:383` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:384` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:385` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:386` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:387` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:388` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:389` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:390` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:391` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:392` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:393` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:394` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:395` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:396` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:397` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:398` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:399` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:400` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:401` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:402` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:403` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:404` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:405` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:406` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:407` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:408` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:409` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_carried.py:410` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R611 | `tests/test_report_guard_states.py` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R612 | `tests/verification/rung3/test_platform_skeleton.py:414` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R614 | `docs/reviews/F3/step-1.md` | the file is untouched | **no change, and the implementer may not write it.** The verdict file is the reviewer's, through `scripts/write_verdict.py`, and a `PreToolUse` hook refuses edits under that directory. |
| R615 | `docs/milestones/F2a.md` | the file is untouched | **no change.** The apparatus plan is frozen as a list under DR1, and verdict 80 cited its line 230 as already recording the ruling to leave the hardcoded guards alone until the freeze lifts. |
| R615 | `tests/test_report_carried.py:394` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:395` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:396` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:397` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:398` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:399` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R615 | `tests/test_report_carried.py:400` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R616 | `scripts/rigid_counter_response.py` | the file is untouched | **no change.** It is the script §5's injection sites are taken from, and it measures rather than asserts -- this step reads it and does not edit it. |
| R617 | `F2a.md` | the file is untouched | **no change.** Cited by bare name; the apparatus plan is frozen as a list under DR1. See the `docs/milestones/F2a.md` row. |
| R617 | `tests/test_report_carried.py:471` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:472` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:473` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:474` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:475` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:476` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:477` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:478` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:479` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:480` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:481` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:482` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_carried.py:483` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:44` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:45` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:46` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:47` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:48` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:49` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:50` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:51` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:52` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:53` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:54` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:55` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:56` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:57` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:58` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:59` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:60` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:61` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:62` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:63` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:64` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:65` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:66` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:67` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:68` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:69` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:70` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:71` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:72` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:73` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_guard_states.py:74` | the file is untouched | **no change, and nothing is owed here.** This site was named by a finding ANSWERED IN STEP 1 and the verdicts closed it there; step 2's diff is the G2.1 gate and the closure corrections, which do not reach it. |
| R617 | `tests/test_report_numbers_are_sourced.py:53` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:54` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:55` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:56` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:57` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:58` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:59` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:60` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:61` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:62` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:63` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:64` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:65` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:66` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:67` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:68` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:69` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:70` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:71` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R617 | `tests/test_report_numbers_are_sourced.py:72` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R620 | `floatfea/model/platform.py:548` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:549` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:550` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:551` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:555` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:556` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R620 | `floatfea/model/platform.py:557` | the file is touched and this line number is the old one | TOUCHED in this step -- the G2.1 refusal `check_rigid_modes`, and C80, C81 and C83 in `admissible`'s docstring -- and **no change at that exact line**: the numbers a step-1 finding named are from before those hunks. |
| R621 | `tests/test_report_numbers_are_sourced.py:169` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:170` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:171` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:172` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:173` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:174` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:175` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:176` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:177` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:178` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:179` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R621 | `tests/test_report_numbers_are_sourced.py:180` | the file is untouched | **no change in step 2.** Re-pointed at the active milestone in `ecf8e70` under EA2/C60 and again for C77's import-time assert; the line numbers a step-1 finding named are from before those commits. |
| R623 | `tests/verification/rung3/test_platform_skeleton.py:489` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |
| R623 | `tests/verification/rung3/test_platform_skeleton.py:490` | the file is touched and this line number is the old one | TOUCHED in this step, for C84, and **no change at that exact line**: the DZ2 `# expected:` comment now names the typed plan centre as well as the two deck fields. The line numbers a step-1 finding named are from before that hunk. |

## 8b. Carried

Generated: `python scripts/carried_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R596 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R598 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R599 | **answered** — §9 | no clause this generator can cut -- see the verdict's Carried section |
| R600 | **answered** — §9 | DZ2's geometry gate builds its expected endpoint-pair set from the BUILT MODEL, not from the... |
| R601 | **answered** — §9 | CI is RED at the reviewed commit -- 37 failed, 835 passed in lint, unit and guards -- and it... |
| R602 | **answered** — §9 | answers_header_names_a_sha_that_is_not_a_commit is red, and the stated diagnosis is refuted:... |
| R603 | **answered** — §9 | _seed_older_verdict runs git commit with no author identity while the other two commit sites in... |
| R604 | **answered** — §9 | The new test's docstring publishes 52 passed in the very commit that made the baseline 53.... |
| R605 | **answered** — §9 | C56(i)'s fresh read is fresh only because nothing caches it, and the shape it was built to... |
| R606 | **answered** — §9 | A FIFTH file hardcoded to F2, and it is the one that enforces BF0.... |
| R607 | **answered** — §9 | The section 8 ordering argument -- THE RULING THE HAND-BACK ASKED FOR.... |
| R608 | **answered** — §9 | expected_pairs's docstring still claims more than the tree supports.... |
| R609 | **answered** — §9 | C51's residual: the status stopped over-claiming and the subject beside it did not.... |
| R610 | **carried** — §9 | The harness's anchors are positional and unguarded, by a decision I agree with. Three states... |
| R611 | **withdrawn** — §9 | ) Eight tests are red at the reviewed commit, and the cause is one thing: this commit edited... |
| R612 | **answered** — §9 | ) CI is red at the reviewed commit, on a line the C59 repair introduced, and the failure gated... |
| R613 | **answered** — §9 | , and STOP-class ON THE PLAN -- it carries by name into step 2, and docs/milestones/F3.md Â§ 5... |
| R614 | **answered** — §9 | Verdict 77's R611 published a closing condition it had already refuted in its own cell, and... |
| R615 | **carried** — §9 | The guard that caught the closure commit can only catch it inside one window, and that window... |
| R616 | **answered** — §9 | docs/milestones/F3.md section 5 instructs G2.1's first measurement in a band that is empty on... |
| R617 | **withdrawn** — §9 | I found that _active_milestone in tests/test_report_numbers_are_sourced.py:53-72 falls back to... |
| R618 | **answered** — §9 | THE NEW EA3 DOCSTRING SAYS THE SLACK IS LINEAR IN f. IT IS NOT, ON THE ONE BODY WHERE IT... |
| R619 | **answered** — §9 | THE SAME DOCSTRING SENDS THE READER TO findings, AND findings IS EMPTY. "The slack is not... |
| R620 | **answered** — §9 | THE EA3 DOCSTRING INTRODUCES THREE QUANTITATIVE CLAIMS ABOUT THE WHOLE LADDER AND CARRIES NO... |
| R621 | **answered** — §9 | THE C77 REPAIR IS RIGHT AND ITS DESCRIPTION OVERSTATES IT BY TWENTY. The commit says "the... |
| R622 | **later** — §9 | EA4's SIX COMMENTS ARE TRUE, AND THE INDEPENDENCE THEY RECORD DOES NOT REACH A DEFECT IN THE... |
| R623 | **answered** — §9 | THE DZ2 COMMENT NAMES TWO SOURCES AND THE PLATFORM's CENTRE COMES FROM NEITHER. The comment... |

## 9. Where each carried item stands

```
rule   the shas and sites this section's dispositions cite
out    G3.1a's inertia half      106ff69, 88fc1d3
out    C56's provenance re-read  8e4238d
out    R612's 101-character line 7b44545
out    R617's covering check     tests/test_report_carried.py:471-483
out    C84's DZ2 comment         tests/verification/rung3/test_platform_skeleton.py
judge  each one is the commit or line the verdict named, re-read at this
       commit rather than carried from a working note.
```

Every row of §8b points here. The word beside each item is the REPORT's word -- answered, open, withdrawn, carried, later -- and where an item stands is the verdict's to say (CC1).

* **R596** — verdict 76 closed it; the inertia half of G3.1a, answered at `106ff69` and `88fc1d3`
* **R598** — verdict 76 closed it; the phantom counter and two figures, at `1078698`
* **R599** — verdict 76 closed it; the `named` whitelist deleted at `de6b1e0`
* **R600** — the geometry gate reads the deck, `1c0785e` and `8df625a`
* **R601** — the harness reads the active plan, `8df625a` and `b2e59b0`
* **R602** — my own report prose broke the anchor, `eb8e165`
* **R603** — the seeding commit's git identity, `1d623c1`
* **R604** — the docstring's stale `52 passed`, `8e4238d`
* **R605** — C56 re-reads the deck FILE, `8e4238d`; verdict 80 ruled it closed
* **R606** — the fifth hardcoded milestone, `ecf8e70`
* **R607** — § 8's over-stated sentence reduced to the grep, `8e4238d`
* **R608** — `expected_pairs`'s docstring, `8e4238d`
* **R609** — the Carried subject the generator cannot cut, `8e4238d`
* **R610** — the harness's anchors are positional and unguarded; verdict 79 recorded it as a ledger line with no work
* **R611** — verdict 78 withdrew it; writing verdict 77 cleared the state it named
* **R612** — the 101-character line that hid the guard suite, `7b44545`
* **R613** — § 5 re-locked, `3709cc6`. Raised as a STOP against the plan; EB0 ruled a correction
* **R614** — verdict 78's own defect, recorded by the reviewer against itself
* **R615** — the guard's standing cost, R610's class, no work
* **R616** — § 5's re-lock, `3709cc6`. This is R613's carry under its later number
* **R617** — the reviewer withdrew it before publishing: `test_report_carried.py:471-483` already covers it
* **R618** — the slack is NOT linear in `f` on the platform; corrected in this step's commit, with the sweep in §9
* **R619** — the slack is in `assumptions`, not `findings`; corrected in this step's commit
* **R620** — the EA3 docstring's figures now point at §9, which rule regenerates
* **R621** — "the twenty-two others are reported" is wrong; the measured figure is in §9
* **R622** — a buoy-label permutation in the DECK EXPORT is invisible; EB6 records the gate F4 adds
* **R623** — the DZ2 comment omitted the typed plan centre; corrected in this step's commit

### The closure items worked in this step

```
claim  C80 / R618: the slack against `f`, re-measured through `_build_body`
cmd    rebuild each body at each rung of MASS_FRACTION_LADDER, slack of
       remainder_inertia, then divide by f
out    f      platform        hub1
out    0.5    -5.3539e+08     -2.030550e+06
out    0.4    -4.4644e+08     -2.030550e+06
out    0.3    -3.8291e+08     -2.030550e+06
out    0.2    -3.3526e+08     -2.030550e+06
out    0.1    -2.9819e+08     -2.030550e+06
out    platform spread 1.795x        hub spread 1.000000x
out    slack at f = 0, all five bodies: 0.0
rule   a rigid body's principal moments satisfy I_i + I_j >= I_k
judge  NOT LINEAR ON THE PLATFORM, exactly linear on the hubs -- which is where
       the claim came from. EA3's ruling is untouched: slack is negative at every
       rung with `f > 0` and exactly zero at `f = 0`, which is all that
       "requiring realisability would force f = 0" needs.

claim  C81 / R619: where the slack is actually reported
cmd    read Superstructure.findings and every body's findings
out    findings: ()   every body: ()
out    the entry with both figures is the last in `assumptions`
judge  the docstring pointed a reader at an empty tuple. One word.

claim  C79 / R621: "the twenty-two others are reported" was wrong
cmd    the F4 state, after ecf8e70: pytest tests/test_report_numbers_are_sourced.py
out    1 failed, 2 passed
judge  with no report `SECTIONS` collapses to one `(preamble)` entry, so the two
       parametrised tests run once each and pass vacuously. The repair is still
       right -- a named failure beats a collection error -- and the figure in its
       commit message is not. Corrected here; the message is immutable.
```

**C84 / R623** the DZ2 `# expected:` comment now names the typed plan centre as
well as the two deck fields, and says that `joint_plane_z` is the deck's own joint
elevation so nothing is circular. **C83 / R620** the EA3 docstring points here for
its derivation. The rest are recorded rather than worked:

```
rule   the closure items this step records and does not fix, with why
out    C85   scripts/check_carried.py:62 and scripts/ci_section.py:147 are
out          collected by nothing -- no test imports either module, so
out          `_active_step()` and the new `SystemExit` are measured by hand only
out    C74   step 1's CI section stays anchored on the verdict it answered, by
out          the generator's design (CO1); step 1 is closed and is not edited
out    C76   the marker-count guard counts plans, not markers per plan
out    C78   a ledger line for the cheap-first CI ordering, no change asked
out    C75b  the scripts/ lint pathspec -- ANSWERED at ccbd38b under EB3, and the
out          mypy half ledgered there with its 56-error count
judge  none of these is (a) to (d) under CZ0, and none is load-bearing for G2.1.
```

**EC4 — a request to the reviewer, not a work item.** One corpus row records a
residual this step re-measures differently:

```
claim  the smallest of the four distinct residuals, recorded against measured
cmd    read the corpus row the reviewer wrote at line 136
out    recorded   7.18521e-20
cmd    element_rigid_residual over the sixteen members, grouped, at this commit
out    measured   8.721078e-20
out    the other three, and the worst, agree exactly: 9.673052e-20,
out    1.988390e-19, 3.528257e-19
rule   a figure is produced by a command at the commit that publishes it
judge  the 2834.26x margin is unaffected, because it is set by the WORST and
       the worst agrees. That file is the reviewer's under DE2 and DR1, so the
       row is not edited here -- this is the request to correct it, citing
       EB0's re-run at 3709cc6 and this one.
```

## 10. Tolerances touched

**None.** No value in `floatfea/tolerances.py` moved, and none was added — §5 is the
reason, and it is a decision held open rather than a change made.

```
cmd    git diff 5d93e6c..HEAD -- floatfea/tolerances.py
out    (no output)
```

## 11. The whole suite

SUITE_LINE_PLACEHOLDER
