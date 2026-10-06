# F4 step 2 — the dynamic case, the load mapping, and a new mass basis

Answers: verdict 96 @ 5786bed

# Revision 1 — EQ0, EQ2's basis-independent half, and ER1's premise check

Answers: verdict 96 @ 5786bed

**2026-10-06.**

## 0. CI at `84de436`, the commit verdict 96 judged — conclusion **SUCCESS**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 96 at `84de436` through the report's own `Answers:` line. Run `37424376028`, event `push`, conclusion **success**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 1892 | 0 | 0 |
| lint, unit and guards | 1042 | 0 | 0 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 0 not green.**

**Failing tests named in the log: 0.**

## 0a. Runs since the commit verdict 96 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 96 at `84de436` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that did not complete has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it (CX0, R449).

| run | event | head | outcome |
|---|---|---|---|
| `37424376028` | push | `84de436` | conclusion **success** |
| `37431234061` | push | `5786bed` | conclusion **success** |
| `37478402259` | push | `b979b68` | conclusion **failure** |

**Run `37478402259`, conclusion **failure**: 1 failing test name(s) in the log.**
- `tests/test_no_tolerance_literals.py::test_no_undeclared_tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]` (lint, unit and guards)

## 0b. The reds at this commit are EG3 state (1), traced by name (EG3(i))

**EIGHT reds, and every one traces to a single cause: step 2 has a report and no verdict
yet.** My first draft of this section claimed the guard-state baseline was green, and
quoted a count for it. That was false: the figure was taken before the step marker moved
from 1 to 2, and I had not re-run it at this content when I wrote the sentence. It is the
same shape as § 12a -- a count carried across a change that invalidated it. The corrected
measurement:

```
claim  the report-guard files give one red, and it is state (1)'s own named test
cmd    python -m pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py -q -rf
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    1 failed, 252 passed in 2.73s
```

```
claim  the guard-state file gives seven, and they are the cascade off a red baseline
cmd    python -m pytest tests/test_report_guard_states.py -q -rf
out    7 failed, 16 passed in 140.95s
out    FAILED ...[baseline]
out    FAILED ...[non_numeric_step_suffix]
out    FAILED ...[superscript_digit_step_number]
out    FAILED ...[draft_suffix_beside_a_step_report]
out    FAILED ...[step_number_is_the_empty_string]
out    FAILED ...[verdict_amended_after_the_commit_the_report_answers]
out    FAILED ...[zero_padded_step_number]
rule   EH1: the cascade is identified by the BASELINE being red and by each cascading
       state's own failure line, not by its name
```

```
claim  the baseline's nested run fails for that one reason and says so itself
cmd    python -m pytest "tests/test_report_guard_states.py::test_the_guard_survives_the_
       state[baseline]" -q --tb=long
out    AssertionError: step 2 has a report and no verdict yet. That is the legitimate
out    boundary -- the verdict is written after the report is committed -- and until it
out    lands this guard checks step 2, so step 2's carry list is UNCHECKED. Invoke the
out    gating-supervisor.
out    FAILED tests/test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
out    1 failed, 217 passed in 3.03s
judge  THIS IS STATE (1): report written, verdict not yet. The step marker moved from 1
       to 2 with this report, so `docs/reviews/F4/step-2.md` does not exist and every
       nested run inherits the same single failure. The reviewer measures it clearing at
       the verdict commit. ANY failure outside this trace would be CZ1 (iv) unchanged,
       and there is none -- the eight ids above are the whole list.
```

## 1. The reading

**This revision exists because the `Stop` hook required a verdict covering the tree, not
because step 2's work is done.** EQ3 says "one reviewer invocation, at the report", and
the report EQ3 means is the one at the end of step 2. Three commits of step-2 work landed
first — EQ0's rule, EQ2's basis-independent half, and ER1(c)'s premise check — and the
hook refuses a turn while `floatfea/` or `tests/` has moved past the newest verdict. I
cannot write a verdict and I will not revert verified work to silence a hook, so the
honest resolution is a real report of what has actually landed, early.

**I am asking the reviewer to rule on whether this round counts against step 2's three.**
My reading is that it should not: EB4 exempts a verdict whose occasion belongs to the
process rather than to the work, and the occasion here is a hook firing on a mid-step
commit. But that is a reading of EB4, not EB4, and it is the reviewer's call. If it does
count, step 2 has two rounds for ER1's remainder plus the whole of EQ3, and I would want
that said now rather than discovered at the third verdict.

**Measured against the dates, today, 6 October.**

| what | date | status today |
|---|---|---|
| F4 working target | 14 Oct | **at risk** — ER1 is a two-day item, see § 8 |
| member-force table | 17 Oct working, 23 Oct committed | on track |
| code check | 22 Oct working, 28 Oct committed | on track |
| F4 committed | 19 Oct | on track |

```
claim  the dates in that table are the ones the plan sets, not mine
cmd    grep -n '19 Oct\|23 Oct\|28 Oct' docs/milestones/F4.md | head -4
out    375:| F4 | 19 Oct | 14 Oct |
out    376:| member-force table | 23 Oct | 17 Oct |
out    377:| code check | 28 Oct | 22 Oct |
rule   CZ0: slippage is reported the day it is known
judge  ER1 arrived today and is two days of work (§ 8). The 14 Oct WORKING target is
       what absorbs it; the committed dates do not move and I am not asking them to.
```

## 2. EQ0 — the rule adopted, in the reviewer's wording

Committed standalone at `9985bcd`, touching `CLAUDE.md` and `docs/SUPERVISOR.md` and
nothing else, as the rule about the reviewer's own instructions requires.

```
claim  the clause is in both files, at the same anchor, identical
cmd    git show --stat 9985bcd
out    CLAUDE.md          | 40 ++++++++++++++++++++++++++++++++++++++++
out    docs/SUPERVISOR.md | 40 ++++++++++++++++++++++++++++++++++++++++
out    2 files changed, 80 insertions(+)
judge  both files already carried the CZ1 section verbatim, so the clause appends at the
       same anchor and they stay identical rather than drifting -- which is the thing
       C131 keeps naming.
```

It records the rule — *a closure commit that changes a gate or a tolerance is reviewed;
one that changes only prose is not* — that the review counts against no step's rounds,
and **why a green suite was not enough**, which is the argument for it: a counter on the
wrong side of its own defect, a decision rule nothing holds in place, and four figures
whose rule the same commit deleted were all invisible to `pytest -q`, to the lint trio,
and to a green CI run at the commit's own sha. It also records EK3's mechanical reason
with the three-run measurement behind it.

## 3. ER1(c) — the STOP check on ER0's new mass basis, and it does NOT stop

ER1(c): "The admissibility check still applies; if any body is not PSD at 0.75, STOP and
report." Every body is PSD. The override is applied **in memory** to a copy of the deck,
so the generated file stays generator-only and nothing is hand-edited.

```
claim  the override is ER0's, at model scale, with the reference point untouched
cmd    python scratchpad/er1c_stop.py
out    platform mass    10.0 -> 20.0   (model scale)
out    platform Ixx/Iyy/Izz 10.0/10.0/20.0 -> 20.0/20.0/40.0
out    platform reference point [0.0, 0.0, 0.7]  (UNCHANGED, ER0(b))
rule   ER0(a) scales the inertia with the mass; ER0(b) leaves the CoG where it is
```

```
claim  every body is admissible at f = 0.75 on the new basis -- NO STOP
cmd    python scratchpad/er1c_stop.py
out    platform  f=0.75  admissible=True  m_member=1.875000e+06  m_remainder=6.250000e+05
out    hub1..4   f=0.75  admissible=True  m_member=1.125000e+06  m_remainder=3.750000e+05
rule   `admissible()`: `m_r >= 0` and no eigenvalue of `J_r` below `-tol` (DY0d)
judge  `admissible()` is CALLED, not re-implemented, so this is the shipped decision and
       not a second opinion about it.
```

**The three quantities ER0 asks to be reported, per body:**

| body | remainder position (full scale) | link | eig(J_r) | triangle slack | rho_eq |
|---|---|---|---|---|---|
| platform | `[3.4e-15, -3.0e-15, 65.995]` | `41.326086` m | `4.666294e+09`, `4.666294e+09`, `1.093623e+10` | `-1.603643e+09` | `7146.0` |
| hub1 | `[50, 0, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |
| hub2 | `[0, 50, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522912e+06` | `11433.5` |
| hub3 | `[-50, 0, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |
| hub4 | `[0, -50, 24.6685]` | `0.000000` m | `3.792032e+07`, `3.792032e+07`, `7.736354e+07` | `-1.522913e+06` | `11433.5` |

**ER0(b)'s prediction is confirmed and the reason it holds is worth stating.** The
remainder sits `41.326086 m` above the joint plane, which is the "≈ 41 m" ER0(b) expected
— and that link length is **unchanged from the old basis**, because the remainder's
position is fixed by matching the deck's CoG and that constraint is linear in mass.
Doubling the mass doubles `m_remainder` and moves the lever not at all.

```
claim  the link length does not move when the mass doubles
cmd    python scratchpad/er1c_stop.py   (the NEW BASIS and OLD BASIS blocks, both f=0.75)
out    new basis: |link| = 41.326086 m, m_remainder = 6.250000e+05
out    old basis: |link| = 41.326086 m, m_remainder = 3.125000e+05
cell   only the platform's mass and inertia moved; the geometry, the reference point,
       the joints and f are all held
```

**The negative triangle slack is inherited, not created**, which DZ5 recorded and EA3
ruled on: the deck's own `J_G` sits on the lamina boundary, `admissible()` tests PSD and
deliberately not realisability, and the slack is negative at every `f > 0` on either
basis.

**And the sizing problem has moved to the hubs.**

```
claim  the platform's equivalent density is now BELOW steel and the hubs' is above it
cmd    python scratchpad/er1c_stop.py   (the rho_eq lines of all three blocks)
out    new basis, f=0.75:  platform rho_eq = 7146.0   hub1..4 rho_eq = 11433.5
out    old basis, f=0.75:  platform rho_eq = 3573.0   hub1..4 rho_eq = 11433.5
out    new basis, ladder:  platform rho_eq = 4764.0   hub1..4 rho_eq = 7622.4
rule   `basis.RHO_STEEL` = 7850 kg/m^3, which is the value `_build_body` reports a
       finding against
cell   between the two f=0.75 rows only the platform's mass and inertia moved, so the
       platform figure doubles and the hub figure does not move at all
judge  the platform doubled from 3573.0 to 7146.0 and is still under steel; the hubs
       are unchanged because their mass is unchanged and only `f` moved. On this basis
       the density finding is a hub-section question and not a platform one.
```

## 3a. ER1(d) — Xabier's static arithmetic, confirmed

All eight figures reproduce exactly. Nothing to correct.

| | R | w·L | root Vz | root My |
|---|---|---|---|---|
| platform arm | `6,131,250` N | `4,598,437.5` N | `1,532,812.5` N | `191,601,562.5` N·m |
| hub arm | `6,948,750` N | `3,678,750` N | `3,270,000` N | `127,734,375` N·m |

```
claim  each of the eight follows from ER0's inputs and the Froude table, by hand
cmd    20.0 kg * 125000 = 2.5e6 kg ; * 9.81 = 24,525,000 N ; / 4 arms = 6,131,250 N
       0.75 * 2.5e6 / 4 = 468,750 kg ; * 9.81 = 4,598,437.5 N
       6,131,250 - 4,598,437.5 = 1,532,812.5 N
       6,131,250 * 50 - 4,598,437.5 * 25 = 191,601,562.5 N.m
       12.0 kg * 125000 * 9.81 = 14,715,000 N ; + 6,131,250 handed down = 20,846,250 N
       / 3 arms = 6,948,750 N ; 0.75 * 1.5e6 / 3 * 9.81 = 3,678,750 N
       6,948,750 - 3,678,750 = 3,270,000 N
       6,948,750 * 25 - 3,678,750 * 12.5 = 127,734,375 N.m
out    every line above evaluates to the figure ER1(d) states
rule   mass and force scale as lambda^3 = 125000; length as lambda = 50
judge  these are the EXPECTED values the static analytic gate will assert against once
       ER1 lands. They are not asserted yet, and § 7 is why.
```

## 4. R683 — the counter-case that holds R679's rule in place exists now

```
claim  the parametrisation carries `internal_joint_dropped`
cmd    grep -rn internal_joint_dropped tests/verification/rung4/test_f4_static_and_mapping.py
out    861: "injection", ["sign_not_flipped", "wrong_node_same_body", "internal_joint_dropped"]
out    872: the docstring sentence that says what it is for
out    906: the comment that records why the claim was false before
rule   EQ2(b): a claim that a test exists is pasted from grep or `pytest -k`, never from
       memory
```

```
claim  reverting R679's per-body rule to the aggregate reddens it, and nothing else
cmd    python scratchpad/eq2_ablate.py
out    as shipped (per body)        28 passed in 0.56s
out    REVERTED to the aggregate    1 failed, 27 passed in 0.78s
out    RED  test_G4_4_the_mapping_gate_REDDENS_on_a_wrong_sign_and_on_a_wrong_node[internal_joint_dropped]
cell   only the aggregation moved -- `_mapping_error` sums over bodies on both sides,
       exactly as it did before `ecace4a`. Every injection is untouched.
judge  ONE test reddens and it is the right one. Before this row both shipped
       counter-cases were red under the aggregate too, so reverting the rule left the
       whole suite green and nothing held it in place -- which is what R683 was.
```

**Why the closure commit's claim was false.** The patch that added the row raised before
writing, I read a stale `git diff --stat` as evidence it had applied, and then edited that
patch script in a way that removed the row entirely. The refutation was one `grep` and I
did not run it. EQ2(b)'s wording is the rule that would have caught it.

## 5. R684 — a legal sparse row no longer raises, and the zero case has its own answer

```
claim  a row with only `buoy1`'s block nonzero is legal and leaves four bodies at zero
cmd    python scratchpad/eq2_measure.py
out    joint_order[0] = ('buoy1', 'buoy1', 'hub1')
out    ||lam|| = 1.912540e+06   nonzero rows: 4 of 64
out    hub2, hub3, hub4, platform: expected resultant array([0., 0., 0., 0., 0., 0.])
out    the SHIPPED gate RAISES: AssertionError: hub2's expected resultants are
out    array([0., 0., 0., 0., 0., 0.]), so there is no scale to normalise by
judge  C158's replacement assertion said no body can have a zero resultant for a nonzero
       row. It can. The premise was the reviewer's and verdict 96 withdrew it; my
       implementation of it was faithful, which is the part worth saying -- a faithful
       implementation of a wrong premise is still a wrong gate.
```

```
claim  the mapper puts EXACTLY zero on a body with no applied load, so that case is
       asserted absolutely rather than normalised
cmd    python scratchpad/eq2_measure.py
out    hub2, hub3, hub4, platform: mapped max|.| = 0.0
out    hub1 (the one body that does carry load): 1.4085799532319176e+08
rule   EQ2(c): for a body whose applied load is exactly zero, assert that its mapped load
       is exactly zero (absolute); otherwise use the relative form
```

```
claim  restoring C158's assertion reddens the new counter-case, and nothing else
cmd    python scratchpad/eq2_ablate.py
out    as shipped (zero scale handled)  28 passed in 0.56s
out    C158's assertion restored        1 failed, 27 passed in 0.81s
out    RED  test_G4_4_a_LEGAL_SPARSE_row_does_not_raise_and_is_still_checked
```

## 6. R653 — answered by name, because step 2 is the condition it was waiting for

Verdict 92 carried R653 on the condition that it becomes blocking "if a G4.x gate ever
cites this residual as evidence that FloatSim's scheme is reproduced". F4 step 2's G4.1
does exactly that, per body and per case, so it is answered rather than carried a fifth
time.

```
claim  the grep the driver's own comment recorded as empty now returns two files
cmd    grep -rln RHO_INF floatfea/ tests/
out    floatfea/io/integrator.py
out    tests/verification/rung4/test_f4_static_and_mapping.py
judge  the driver's comment said, in its own `cmd:`/`out:` pair, "(no output) -- nothing
       asserts this value". That was true and it is no longer.
```

```
claim  the closed form reproduces the interchange specification's own published
       coefficients, which are not derived from this code (EA4)
cmd    python -m pytest tests/verification/rung4 -q -k R653
out    2 passed, 155 deselected in 0.47s
rule   docs/load-interchange-v1.md SECTION 4, lines 259-260: at rho_inf = 0.9,
       alpha_m = 0.42105, alpha_f = 0.47368, difference 0.05263, gamma = 0.55263,
       beta = 0.27701 -- compared at five decimal places, which is exact
judge  NO TOLERANCE IS DECLARED and none is wanted: the specification publishes five
       places and the comparison is against the value rounded to five places. A ceiling
       here would be a number with nothing behind it.
```

`FLOATSIM_RHO_INF` and `generalized_alpha_coefficients` live in
`floatfea/io/integrator.py`; `scripts/report_joint_reactions.py` imports both and keeps no
copy of either, so the two-copies shape cannot return.

```
claim  the driver holds no copy of the constant or the derivation
cmd    grep -n 'RHO_INF\|alpha_m =' scripts/report_joint_reactions.py
out    RHO_INF = FLOATSIM_RHO_INF
out    alpha_m, alpha_f, beta, _gamma = generalized_alpha_coefficients(RHO_INF)
rule   C131: a rule written twice drifts, and an earlier version of this driver held two
       copies of this number whose 0.05 disagreement made the residual "429x louder"

claim  my first citation of the specification was false
cmd    grep -n '^## ' docs/load-interchange-v1.md | awk -F: '$1<=259' | tail -1
out    211:## 4. Time alignment is a required field
judge  I wrote "sec.6". Section 6 is `## 6. Two-pass generation`, which begins at line
       571 and is about something else entirely. A false citation in a docstring is the
       CW0 shape and it was mine; one grep settles it.
```

## 7. R682 and R685 — OPEN, held by ER2, and what is already measured

**These are not answered and I am not claiming they are.** ER2 puts ER1's new mass basis
before any step-2 tolerance work "so nothing is calibrated twice", and both items are
figures derived from `mu`, `M` and `f` — all three of which ER0 changes. Answering them on
the old basis and again on the new one is the double calibration ER2 exists to prevent.

**What is already measured, so the reviewer can see the work is done and only its basis is
waiting.** On the OLD basis, in the gate's own denominator:

```
claim  the counter 0.05 sits ABOVE the defect on 12 of the 16 members
cmd    python scratchpad/eq2_measure.py
out    platform:hub1_arm   defective root 1.2134765625000013e+08  tip/root 5.2631578947368425e-02  = 1/19
out    hub3:buoy9_arm      defective root 1.2262499999999999e+08  tip/root 4.1666666666666269e-02  = 1/24
out    SMALLEST over the 16: 0.04166666666666627 = 1/24 on hub3:buoy9_arm
out    LARGEST  over the 16: 0.05263157894736891 = 1/19
out    counter 0.05  below EVERY defect: False   members whose defect is below it: 12
out    counter 0.04  below EVERY defect: True    members whose defect is below it: 0
rule   the counter is the smallest defect the gate must still fail
judge  my published 5.555556e-02 divided by the CORRECT root moment; the gate divides by
       the DEFECTIVE one, which is larger by exactly the tip moment being tested. No
       member reads 5.555556e-02 on either basis.
```

The test-side half of R682 — the counter-case running over all 16 members instead of the
platform's first — is written and was reverted with the value, because a counter-case over
16 members and a counter declared for one are not a consistent pair. Both land together on
the new basis.

R685's four figures are re-measured under the per-body rule and are in hand:

```
claim  the mapping entry's four figures, under the rule that replaced the aggregate
cmd    python scratchpad/eq2_measure.py
out    clean, per body                       : 2.1962235947826024e-16
out    ceiling 1.0e-12 is above it by        : 4553.3x
out    wrong node, same body: force 2.092543223926032e-16
out                           moment 0.9597085787263796
out    sign not flipped     : worst  3.5569621874567385
rule   relative, force and moment normalised separately, worst over the five bodies
judge  the `0.2` counter does NOT move: under the aggregate the wrong-node injection
       measured 0.24374825705420716 and 0.2 was the round bound below it; per body the
       same injection is about four times larger, so 0.2 is further below the defect
       than it was declared to be. It errs safe and the ordering it depends on survives.
```

They are held with R682 so that `floatfea/tolerances.py` changes once.

## 8. ER1's cost, said the day I know it

**ER1 is a two-day item, not a one-day item.** ER1 asks me to say so the day I know, and I
know today.

* **ER1(b) is the long pole.** Six FloatSim design-wave re-runs in `../HSP-runs` with the
  override applied in memory by the run script, a fresh `res.lam` export, then EK0(a)
  repeated over all 24,006 steps and the EJ4 per-body residual on the new runs. The
  REPLAY alone was about 25 minutes of solve time this session; full runs with export are
  longer, and the in-memory override is new code written against HSP-stable's API, which
  stays read-only at `floatfea-ref-1`.
* **ER1(d) is the wide one.** BP0 requires every figure and counter that depends on `mu`,
  `M` or `f` re-derived in the SAME commit: the static analytic gate's four expected
  values, the tip-moment counter, `F4_STATIC_REACTION_AGREEMENT_COUNTER`, the symmetry
  counter, the conservation counter, and ER0 into both `F3.md` § 0 and `F4.md` § 0.
* **(a), (c) and (e)** are a few hours each. (c) is now a one-line default change plus the
  findings it reports, because § 3 has already measured that it is admissible.

**A suggestion rather than a request:** ER3's preview issue 4 needs the new runs only for
its dynamic columns. The static-only columns and the `f = 0.5` / `f = 1.0` sensitivity need
only ER1(c), which is done — so a static-only issue 4 is available inside a day if that is
worth having before the dynamic half.

<!-- generated: scripts/answered_table.py -->

| item | class | state | where | site | the verdict's own subject |
|---|---|---|---|---|---|
| R622 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R626 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R631 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R635 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R638 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R653 | carried | **answered** | §6 | `` | carried from an earlier verdict |
| R656 | carried | **carried** | §9b | `` | carried from an earlier verdict |
| R663 | recorded | **NOT ANSWERED** |  | `` | , A DEFECT IN `floatfea/`.) `floatfea/post/member_forces.py:78` |
| R664 | recorded | **NOT ANSWERED** |  | `` | , A GATE ASSERTION THAT CANNOT FAIL.) |
| R665 | recorded | **NOT ANSWERED** |  | `` | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS |
| R666 | recorded | **NOT ANSWERED** |  | `` | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS |
| R667 | recorded | **NOT ANSWERED** |  | `` | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND |
| R668 | recorded | **NOT ANSWERED** |  | `` | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE |
| R669 | recorded | **NOT ANSWERED** |  | `` | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" |
| R670 | recorded | **NOT ANSWERED** |  | `` | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.) |
| R671 | recorded | **NOT ANSWERED** |  | `` | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) |
| R672 | recorded | **NOT ANSWERED** |  | `` | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT |
| R673 | recorded | **NOT ANSWERED** |  | `` | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY |
| R674 | recorded | **NOT ANSWERED** |  | `` | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND |
| R675 | recorded | **NOT ANSWERED** |  | `` | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF |
| R676 | recorded | **NOT ANSWERED** |  | `` | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE |
| R677 | recorded | **NOT ANSWERED** |  | `` | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT |
| R678 | recorded | **NOT ANSWERED** |  | `` | , R668 SECOND CLAUSE, UNTOUCHED.) `duality_residual` STILL RETURNS |
| R679 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) G4.4's GATE SUMS ITS |
| R680 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) R675's BODY AVERAGE IS |
| R681 | recorded | **answered** | §9a | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) `F4_STATIC_TIP_MOMENT_N_M = |
| R682 | recorded | **open** | §7 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) |
| R683 | recorded | **answered** | §4 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) NOTHING IN THE TREE HOLDS |
| R684 | recorded | **answered** | §5 | `` | , AND IT CARRIES INTO STEP 2 BY NAME. THE PREMISE IT RESTS ON WAS |
| R685 | recorded | **open** | §7 | `` | , AND IT CARRIES INTO STEP 2 BY NAME.) THE `F4_MAPPING_CONSERVATION` |

**16 finding(s) with no row in the answers file: ['R663', 'R664', 'R665', 'R666', 'R667', 'R668', 'R669', 'R670', 'R671', 'R672', 'R673', 'R674', 'R675', 'R676', 'R677', 'R678'].**

<!-- generated: scripts/untouched_sites.py -->

| item | site | what the diff says | why it was left |
|---|---|---|---|
| R663 | `docs/reports/F4/preview-PRELIMINARY.md` | the file is untouched | **no change** — answered at step 1 (R677, the required argument). Step 2's range does not touch this site. |
| R663 | `floatfea/post/member_forces.py:78` | the file is untouched | **no change** — answered at step 1 (R677, the required argument). Step 2's range does not touch this site. |
| R664 | `floatfea/solve/static.py:92` | the file is untouched | **no change** — answered at step 1 (R674, the signed comparison). Step 2's range does not touch this site. |
| R665 | `floatfea/loads/selfweight.py:86` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:21` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:22` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R665 | `floatfea/solve/static.py:23` | the file is untouched | **no change** — answered at step 1 by WITHDRAWING the claim (R672), which is why the site is untouched rather than edited. |
| R667 | `docs/closure/F3.md:179` | the file is untouched | **no change** — answered at step 1 (R670's pinned snapshot and R676's hub side). |
| R667 | `tests/verification/rung3/test_platform_skeleton.py:711` | the file is untouched | **no change** — answered at step 1 (R670's pinned snapshot and R676's hub side). |
| R668 | `joint_reactions.py:89` | the file is touched and this line number is the old one | **no change** — answered at step 1 (R678, `duality_residual` raises). |
| R670 | `scripts/run_rung.sh:274` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `scripts/run_rung.sh:275` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `scripts/run_rung.sh:276` | the file is untouched | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:265` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:266` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:267` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:268` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:269` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:270` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:271` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R670 | `tests/verification/rung4/test_f4_static_and_mapping.py:272` | the file is touched and this line number is the old one | **no change** — answered at step 1; `ladder 4` is green in CI and the rung runs with 0 skipped. `scripts/run_rung.sh` was never the thing at fault. |
| R671 | `floatfea/tolerances.py:1888` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:89` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:90` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:91` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:92` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:93` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R671 | `tests/verification/rung3/test_tolerance_counter_cases.py:94` | the file is untouched | **no change** — answered at step 1; the `_COUNTER` suffix was the whole repair and verdict 94 said not to extend this guard. |
| R672 | `floatfea/loads/selfweight.py` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `floatfea/solve/static.py` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:21` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:22` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R672 | `static.py:23` | the file is untouched | **no change** — answered at step 1 by withdrawal, at both named sites. |
| R673 | `scripts/suite_count.py` | the file is untouched | **no change** — answered at step 1; `scripts/suite_count.py` was correct and simply had not been run. |
| R674 | `static.py:86` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:87` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:88` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:89` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:90` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `static.py:91` | the file is untouched | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R674 | `tests/verification/rung4/test_f4_static_and_mapping.py:161` | the file is touched and this line number is the old one | **no change** — answered at step 1; `sum_error` was already signed and the `abs()` was in the test, which is where it was fixed. |
| R677 | `floatfea/post/member_forces.py:95` | the file is untouched | **no change** — answered at step 1; `f_eq_global` is a required argument. |
| R678 | `floatfea/loads/joint_reactions.py` | the file is untouched | **no change** — answered at step 1; the both-zero case raises. |
| R679 | `docs/milestones/F4.md:310` | the file is touched and this line number is the old one | **no change** — answered in step 1's closure commit, per body, and verified by verdict 96 (§ 9a). |
| R681 | `floatfea/tolerances.py:1966` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1967` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1968` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1969` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1970` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1971` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1972` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `floatfea/tolerances.py:1973` | the file is untouched | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R681 | `test_f4_static_and_mapping.py:504` | the file is touched and this line number is the old one | **no change** — answered in step 1's closure commit, relative form (§ 9a). |
| R682 | `F4.md:346` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `docs/milestones/F4.md:346` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `floatfea/tolerances.py` | the file is untouched | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R682 | `test_f4_static_and_mapping.py:552` | the file is touched and this line number is the old one | **no change** — OPEN and HELD by ER2 until the new mass basis lands; the measurement is in § 7 and only its basis is waiting. |
| R685 | `floatfea/tolerances.py` | the file is untouched | **no change** — OPEN and HELD by ER2 with R682, so `tolerances.py` changes once (§ 7). |

## 9. Carried

Generated: `python scripts/carried_table.py <the verdict> <the answers file>`.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R622 | **carried** — §9b | F4's own, not yet reached. |
| R626 | **carried** — §9b | 's residue, R635 and the long closed |
| R631 | **carried** — §9b | 's residue, R635 and the long closed |
| R635 | **carried** — §9b | no clause this generator can cut -- see the verdict's Carried section |
| R637 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R638 | **carried** — §9b | OPEN, unchanged, EJ1 governs, closed before F4 closes. floatfea/tolerances.py |
| R653 | **answered** — §6 | OPEN, carried, and about to become (c). A grep for RHO_INF over tests and |
| R654 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R655 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R656 | **carried** — §9b | OPEN WITH XABIER, unchanged, correctly not repaired. scripts/ci_section.py is |
| R657 | **not classified in this verdict** — carried in from an earlier one | ANSWERED AND CLOSED at e505f28. The word is mine. Section 8 carries the |
| R658 | **not classified in this verdict** — carried in from an earlier one | ANSWERED AND CLOSED at e505f28, same constant, same commit, same reading. |
| R659 | **not classified in this verdict** — carried in from an earlier one | CLOSED, not reopened, nothing in this range touches their sites. |
| R660 | **not classified in this verdict** — carried in from an earlier one | ANSWERED at 0c490bf, the standalone closure commit verdict 92 said was worth |
| R661 | **not classified in this verdict** — carried in from an earlier one | ANSWERED in report section 8, where EK3 puts it, and the cause is correctly |
| R662 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R663 | **open** — blocking, and not answered in this round | , A DEFECT IN floatfea/.) floatfea/post/member_forces.py:78 RETURNS THE ELEMENT NODAL FORCE AND... |
| R664 | **open** — blocking, and not answered in this round | , A GATE ASSERTION THAT CANNOT FAIL.) floatfea/solve/static.py:92: StaticCase.sum_error IS AN... |
| R665 | **open** — blocking, and not answered in this round | .) THE EK0(d) SUPPORT-SCHEME CHECK CANNOT FAIL, AND NO THRESHOLD IS DECLARED FOR IT.... |
| R666 | **open** — blocking, and not answered in this round | , THREE RED TESTS THAT ARE NOT THE MILESTONE BOUNDARY, AND CI IS RED AT THE REVIEWED COMMIT.)... |
| R667 | **open** — blocking, and not answered in this round | .) EB6's GATE DOES NOT EXIST, AND REPORT SECTION 7 REPORTS A SECOND SIDE TO A FIRST SIDE THAT... |
| R668 | **open** — blocking, and not answered in this round | .) THE EK0(e) DUALITY FIGURE IS ZERO BY CONSTRUCTION, AND THE STATE THE DOCSTRING NAMES IS... |
| R669 | **open** — blocking, and not answered in this round | .) FOUR GATE ROWS THE LOCKED PLAN MARKS "TO BE MEASURED AT STEP 1" HAVE NO ASSERTION ANYWHERE,... |
| R670 | **open** — blocking, and not answered in this round | , CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4.)... |
| R671 | **open** — blocking, and not answered in this round | , A TOLERANCE WHOSE CEILING NOTHING BOUNDS ABOVE.) floatfea/tolerances.py:1888... |
| R672 | **open** — blocking, and not answered in this round | , CARRIED FROM VERDICT 93 AND UNANSWERED.) R665 IS UNTOUCHED AT EVERY SITE ITS CLOSING... |
| R673 | **open** — blocking, and not answered in this round | , 39 RED TESTS AT THE REVIEWED COMMIT AND NOT ONE IS A BOUNDARY RED.) Section 8 traces all 39... |
| R674 | **open** — blocking, and not answered in this round | and (c), THE COUNTER-CASE DOES NOT RUN THE INJECTION IT NAMES, AND THE GATE IS SIGN-BLIND ON... |
| R675 | **open** — blocking, and not answered in this round | , TWO GATES WHOSE REACH IS NARROWER THAN THE TABLE CLAIMS, ONE OF THEM VACUOUSLY PASSABLE.)... |
| R676 | **open** — blocking, and not answered in this round | , CARRIED FROM VERDICT 93 AND ANSWERED FOR ONE ROW OF FOUR.) THREE OF R669 FOUR GATE ROWS STILL... |
| R677 | **open** — blocking, and not answered in this round | and (b), R663 CLOSING CONDITION SECOND BRANCH IS NOT MET: IT DEFAULTS.)... |
| R678 | **open** — blocking, and not answered in this round | , R668 SECOND CLAUSE, UNTOUCHED.) duality_residual STILL RETURNS 0.0 FOR A BOTH-ZERO SHARE,... |
| R679 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) G4.4's GATE SUMS ITS RESIDUAL OVER ALL FIVE BODIES, SO... |
| R680 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) R675's BODY AVERAGE IS STILL LIVE IN... |
| R681 | **answered** — §9a | , AND IT CARRIES INTO STEP 2 BY NAME.) F4_STATIC_TIP_MOMENT_N_M = 1.0 IS AN ABSOLUTE TOLERANCE... |
| R682 | **open** — §7 | , AND IT CARRIES INTO STEP 2 BY NAME.) F4_STATIC_TIP_MOMENT_RELATIVE_COUNTER = 0.05 IS DECLARED... |
| R683 | **answered** — §4 | , AND IT CARRIES INTO STEP 2 BY NAME.) NOTHING IN THE TREE HOLDS R679'S PER-BODY RESIDUAL IN... |
| R684 | **answered** — §5 | , AND IT CARRIES INTO STEP 2 BY NAME. THE PREMISE IT RESTS ON WAS MINE AND I WITHDRAW IT.)... |
| R685 | **open** — §7 | , AND IT CARRIES INTO STEP 2 BY NAME.) THE F4_MAPPING_CONSERVATION ENTRIES REPUBLISH FOUR... |

### 9a. Answered in step 1's closure commit and verified by verdict 96

* **R679, R680, R681** — fixed in `ecace4a` and reproduced by the reviewer at
  `84de436`: R679's per-body rule (`1.778481e+00` and `1.635665e+00` against the
  aggregate's `1.872582e-16` and `9.362910e-17`), R680's `rho A L`, R681's relative
  tip-moment form. This revision did no work on them, which is why they point here.

### 9b. Open elsewhere, not answered in this round

* **R638** — open under EJ1, which requires it answered before F4 ends.
* **R656** — open with Xabier.
* **R622, R626, R631, R635** — on the EJ3 ledger at `docs/closure/F3.md` § 8, unchanged
  and not re-reviewed (CZ0).

### 9c. Closure items

**C161 to C166 and C137/C141/C144/C145/C147/C148/C151 are open and go into step 2's
closure commit, not re-reviewed item by item (CZ0).** One of them is answered early
because it is housekeeping the directive asked for by name: **C166** is § 10.

## 10. Housekeeping — the stale worktree registrations (EQ4)

EQ4 asks for the paths so they can be deleted by hand. `git worktree prune` cannot remove
them on this machine: it exits `Permission denied` on the pack files inside each
registration.

```
claim  nine registrations, of which eight are stale
cmd    git worktree list
out    C:/Users/xlama/OneDrive/Documents/buoy/FLOATFEA  b979b68 [F3]   <- the real one
out    C:/Users/xlama/AppData/Local/Temp/claude/C--Users-xlama-OneDrive-Documents-buoy-
out      FLOATFEA/ec986bd8-d1bc-48a2-918b-168c4b1be465/scratchpad/wt84  8368c51
out    C:/Users/xlama/AppData/Local/Temp/suite-count-6_es7sst/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-6mfeb05h/tree      f839dd8
out    C:/Users/xlama/AppData/Local/Temp/suite-count-f78bb4m4/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-f_sfu9l2/tree      8beb0e4
out    C:/Users/xlama/AppData/Local/Temp/suite-count-qcfoceyc/tree      3fdfc79
out    C:/Users/xlama/AppData/Local/Temp/suite-count-qj9dnjl4/tree      24e8bb2
out    C:/Users/xlama/AppData/Local/Temp/suite-count-woj9990l/tree      8beb0e4
judge  the `wt84` one is a reviewer worktree from F3 step 3's eighty-fourth verdict and
       the seven others are `scripts/suite_count.py`'s. Since C154, `_real_git_dir_into`
       copies the whole common directory into every scratch build of the guard-state
       harness, and these registrations go with it -- harmless, and a reason to clear
       them rather than leave them accumulating.
```

**To clear them:** delete the eight folders listed above, then
`git worktree prune` in the repository.

## 11. Tolerances touched

**NONE.** No value, form, counter or injection changed in this revision.

```
claim  floatfea/tolerances.py is untouched across this revision's range
cmd    git diff --stat 5786bed..HEAD -- floatfea/tolerances.py
out    (no output)
rule   BR0: a tolerance moves with a plan edit, and no tolerance moved
judge  R682 and R685 are the two items that would have moved it, and § 7 is why they did
       not. `docs/milestones/F4.md` changed only in its step marker, 1 -> 2.
```

## 12. The whole suite

Generated by `python scripts/suite_count.py`, run AFTER every other edit (CP3).

**Whole suite at `b979b68`: 2753 passed, 1 failed, 0 skipped.** **The excluded set: 271 passed, 0 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 271 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed** `tests.test_no_tolerance_literals::test_no_undeclared_tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]`
```

### 12a. The one red at `b979b68` was mine, and it is fixed in this revision's commit

```
claim  `b979b68` shipped a red that rung 4 could not see
cmd    python -m pytest "tests/test_no_tolerance_literals.py::test_no_undeclared_
       tolerance_reaches_a_comparison[test_f4_static_and_mapping.py]" -q
out    line 1008: comparison against 0.05263
out    line 1021: comparison against 0.8
out    line 1028: comparison against 0.5
judge  all three are in MY R653 gate, and none of them is a tolerance: `0.05263` is a
       value the interchange specification PUBLISHES and is compared exactly after
       rounding to the five places it prints; `0.8` is FloatSim's spectral radius, the
       input R653 exists to pin; `0.5` and `1.0` are the mathematical ranges `beta` and
       `gamma` have for a dissipative step. The guard offers
       `# not-a-tolerance: <why it is an input>` for exactly this, and that is what they
       carry now.
```

```
claim  the marker has to sit on the comparison's OWN line, and my first attempt put it
       above
cmd    python -m pytest tests/test_no_tolerance_literals.py tests/verification/rung4 -q
out    first attempt (explanation above the assert): 1 failed, 211 passed
out    marker on the comparison line:                212 passed in 1.22s
rule   `_marker_lines` tokenises and collects the line of each COMMENT token carrying
       the marker, so a comment on the preceding line is not on the comparison's line
judge  the explanation stays above, where it is readable, and a short
       `# not-a-tolerance: see above` sits on the line the guard reads.
```

```
claim  CI caught the same three literals at the same commit, independently of me
cmd    gh run view <the b979b68 run in section 0a> --json conclusion,jobs ; then
       gh run view <it> --log-failed | grep 'comparison against'
out    conclusion: failure
out    JOB the verification ladder: success
out    JOB lint, unit and guards: failure
out        STEP guards and meta-tests: failure
out    E           line 1008: comparison against 0.05263
out    E           line 1021: comparison against 0.8
out    E           line 1028: comparison against 0.5
judge  the same three lines, to the line number, from a machine that did not know what
       I had run. The ladder job was GREEN there -- which is exactly why rung 4 could
       not see this and why "rung 4 is green" was not the claim I needed.
```

**HOW I SHIPPED IT, because the mechanism is the one CZ1 names.** I ran
`tests/verification/rung4` after reverting R682, and rung 4 was green:

```
claim  rung 4 was green at the commit that shipped the red
cmd    python -m pytest tests/verification/rung4 -q   [at b979b68]
out    157 passed in 1.01s
rule   `tests/test_no_tolerance_literals.py` is NOT under `tests/verification/rung4`,
       so no count from that directory can speak for it
```

The guard that reads that file is not in rung 4 -- it is `tests/test_no_tolerance_literals.py`
-- and I had run it earlier, against the version WITH R682, where the literals did not
exist because R682's own edits were in the file. The revert changed the file and I
re-measured only the directory I had been watching. "I ran the tests" is not a
measurement of the tests I did not run.
