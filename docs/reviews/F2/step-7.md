# Review — F2 step 7
Reviewed commit: 8b4b6879d45a690a04f358971175fcceedec4521
Verdict: PASS
Tests: 2931 passed, 2 failed, 0 skipped   (my own run at `d838d77`, `python -m pytest -q`, 1338.59s, one invocation, no split)

## Round of 2026-09-30 -- SEVENTY-THIRD verdict on F2/F3

**Reviewed commit: `d838d77`.**

**THIS IS THE THIRD ROUND OF THIS STEP AND IT CLOSES IT (CZ0).** The verdict letter is
PASS because the cap says so, and the substance of this round is a HOLD's: four blocking
findings, R596 to R599, carry by name into F3 step 1 and block there before any new work.
I am not softening them and I am not asking for a fourth round.

**WHAT THE ROUND GOT RIGHT, FIRST, because most of it is right.** DY0 to DY7 landed in
eight standalone commits, one path class each. R591 is genuinely and completely answered
-- the CoG assertion now names the deck's declared point instead of the body node, and the
10.3315 m error is gone. R592 is answered and the implementer found and reported a second
error of its own inside the fix, which is the behaviour this whole arrangement exists to
produce. R595 is answered. DY7's script is the best thing in the diff: it refuses twice to
produce a plausible number and says exactly why, which is worth more than a table would
have been. R594 is acknowledged and the eight commits obey DY8b.

**AND THE ONE THING THAT IS NOT.** R590 was that a gate could not fail. The repair
rebuilt the model well and moved the vacuity rather than removing it -- and it moved it
into a second quantity. The implementer asked me to rule on exactly this and reported the
mass half honestly; the finding is larger than the report says.

## The ruling asked for first: the two reds are a guard FAILING FALSE (R599)

**I rule with the implementer, and DR1's permitted repair is DELETION, not a name.**

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit d838d77 --json name,conclusion,workflowName,event
out  36696844153  CI  workflow_dispatch  completed  failure
out  2 failed, 1032 passed in the `lint, unit and guards` step; the verification
     ladder GREEN in every rung
cmd  gh run list --commit 6c09932 (the previous round's judged commit, dispatched)
out  36693879464  success
judge RED, and the two reds are the two I rule on in R599. The diagnosis in verdict
      72 -- that a docs-only push is path-ignored and `workflow_dispatch` is the one
      route left -- was right, the implementer took it, and C31 is closed by the
      measurement rather than by argument. The ladder being green at the judged commit
      on a machine neither of us controls is the thing I could not get last round.
cmd  python -m pytest -q            (mine, at `d838d77`)
out  2 failed, 2931 passed, 2 warnings in 1338.59s
judge my run and CI agree on the failure set exactly, which is the first time this
      step that they have been comparable at all.
```

**A note on the whole-suite figure.** The report's is `2621 passed, 1 failed` at
`56d6810`; mine is `2931 passed, 2 failed` at `d838d77`. The report names its commit so
nothing it says is false, but 310 tests separate the two, and several guards are
parametrised over the report's own rows -- so the count grows as the report is written and
a figure taken two commits early is not a figure about the tree under review. Closure item
C33; it is not why anything here blocks.

## Carried

Verdict 72 carried six blocking items -- R590 to R595 -- and closure items C12, C14,
C18 to C25, C26 to C32. The report's header reads `Answers: verdict 72 @ 5ef2e3d`, which
is my own verdict commit and the latest verdict, so instruction 1b is satisfied and DX2's
third ruling was followed.

```
cmd  python scripts/check_carried.py --verdict docs/reviews/F2/step-7.md --report docs/reports/F2/step-7.md
out  check_carried: all 10 findings carried        exit 0
```

**I re-measured all six rather than reading the report.**

* **R590 -- PARTIALLY ANSWERED, and the unanswered part is R596.** The mass half now has
  real content and I measured it: a ten percent error in the element axial mass block
  turns 12 tests red. That content is exactly what R590 said was the only non-trivial
  part of the old pair, now merged into one test. What R590's `Closed when` asked for --
  *"the mass half compares a quantity the deck constrains"* -- is not what landed, and the
  implementer says so in the report. Under DY0 every body is mass-sized by construction,
  so the hub-versus-platform distinction R590's condition rested on no longer exists; the
  condition was overtaken by a model change I accept. **The division the implementer asks
  me to rule on is SOUND for the mass and the section.** `test_the_section_is_F1s_RECORDED_section`
  really is what sees a wall error, and I confirmed both of the implementer's cells:
  `ARM_WALL` 0.180 -> 0.001 gives `5 failed, 38 passed`, all five in the section test and
  none in a mass-property assertion; `ARM_OUTER_DIAMETER` 2.5 -> 2.6, a four percent
  change, also gives 5 failed. **The vacuity was not removed, it was moved into the
  inertia and the CoG**, and that is R596. Open, renumbered.

* **R591 -- ANSWERED at `ecebd78` and `106ff69`. Closed.**

```
cmd  remainder_point + [0, 0, 5] applied after the placement rule, shipped tests re-run
out  11 failed, 32 passed -- CoG x5, inertia x5, and the first-moment placement test
judge the implementer's cell reproduces exactly. The CoG assertion names the offset and
      the point it is measured from. This is the finding I most wanted answered and it is.
```

* **R592 -- ANSWERED at `ecebd78`, and the implementer's self-report is correct.**
  `inertia_about` is a separate function from `rigid_properties` and the reference point
  is `G`. `test_J_mem_is_taken_ABOUT_G_and_not_about_the_member_centroid` asserts the
  parallel-axis difference and refuses to pass on a body whose shift is zero, which is a
  gate carrying its own failure. Closed. **But the figure quoted for it is not a
  measurement of accuracy** -- see R598.

* **R593 -- ANSWERED IN SUBSTANCE, NOT SITE BY SITE.** The `:468` comparison R593's
  condition named is gone: all three uses of `_NEGLIGIBLE_FRACTION` were deleted at
  `ecebd78`, which is better than moving the constant and is what the data supported.

```
cmd  grep -n "_NEGLIGIBLE_FRACTION" floatfea/model/platform.py
out  85:_NEGLIGIBLE_FRACTION: Final[float] = 1e-12      -- the declaration, and nothing else
cmd  git diff 5ef2e3d..HEAD -- floatfea/model/platform.py | grep NEGLIGIBLE
out  three deleted lines, no added line
judge the tolerance-shaped comparison is gone. The DECLARATION is still there, dead, with
      a docstring that describes a builder DY0 withdrew ("when a member is mass-sized"),
      and R593's condition also said "the :61-65 docstring stops saying the finding it
      gates is not a pass or a fail" -- that half was not done. A dead literal decides
      nothing, so this is not (b) and I am not holding on it: closure item C34.
```

  **And a second thing at the same site, which is a real code defect rather than prose.**
  `floatfea/model/platform.py:86-89` is `_NEGLIGIBLE_FRACTION`'s docstring and `:90-97` is
  a second bare string immediately after it -- the justification for
  `MIN_LENGTH_OVER_DIAMETER` and `MAX_LENGTH_OVER_GYRATION`, which now documents nothing
  at all because a module-level string only attaches to the assignment above it. The two
  builder limits have silently lost their recorded reason. Closure item C35, and deleting
  the dead constant closes both.

* **R594 -- ANSWERED. Closed, and verified rather than accepted.**

```
cmd  git diff 5ef2e3d..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git show --stat --format="" b8bca73
out  scripts/write_verdict.py     -- one file, a standalone `process:` commit
judge my own instructions are untouched this round. `write_verdict.py` is my tool and not
      my instructions, its change is additive, it removes no guard, and I read it line by
      line: earlier rounds are preserved verbatim, newest first, and both sides are
      explicit UTF-8. The latent cp1252 bug the implementer found would have silently
      discarded every earlier round on the first em dash, so that catch is the difference
      between DY6 working and DY6 looking like it worked. Closed.
```

* **R595 -- ANSWERED at `ecebd78`. Closed.** `buoy_joint_nodes` is keyed by
  `(body, node)` and `test_the_BUOY_NODE_MAP_names_its_body` reads it.

## Findings

**R596. (c, blocking) The CoG and INERTIA halves of G3.1a are algebraic identities of the
construction and cannot fail. The remainder position is solved to make the CoG comparison
close, and its rotary inertia is defined as the inertia comparison own deficit, so both
close. A 100 percent error in every element rotary inertia is undetectable at ANY
tolerance. `floatfea/model/platform.py:450` and `:486` against
`tests/verification/rung3/test_platform_skeleton.py:151` and `:172`; plan row
`docs/milestones/F3.md` G3.1a.**

This is R590 one level on. I am not repeating R590 reading; I ran the mutations.

```
rule   worst <= MASS_PROPERTY_AGREEMENT * max|deck_inertia|, per body
cmd    beam.bending_mass: rho_i -> 2.0 * rho_i, shipped tests re-run unmodified
out    43 passed
cmd    beam.local_mass: rho * (I_y + I_z) -> 3.0 * rho * (I_y + I_z), torsion block
out    43 passed
cmd    _build_body reads 2.0 * the deck inertia
out    43 passed
cmd    rigid_projection: the translation-rotation coupling block negated
out    43 passed
cmd    CONTROL -- remainder_inertia overwritten with zeros after the deficit is computed
out    5 failed, one per body
judge  the assertion is not inert. It is a consistency check of `body_mass_matrix`
       against the scalar arithmetic in `_build_body`, and that is ALL it is, because
       `remainder_inertia = deck_inertia - inertia_member - parallel` and
       `inertia_member` is read from the SAME assembled matrix the test then reads.
       The comparison reduces to deck_inertia == deck_inertia. There is no arrangement
       of the deck, the element or the section that breaks it.
```

**AND THE PUBLISHED RESIDUAL SAYS SO, WHICH IS WHY THIS IS NOT A READING.**

```
cmd    the gate own printed line, at `d838d77`, unmodified
out    platform  inertia residual 2.1092e-26 of 6.250000e+09 = 3.375e-36 relative
out    hub1..4                    2.98e-08 to 5.96e-08        = 9.5e-17 to 1.9e-16
cmd    numpy.spacing(6.25e9)
out    9.5367e-07
judge  the platform residual is NINETEEN ORDERS OF MAGNITUDE below one bit of the
       quantity being differenced. That is not round-off -- round-off on a 6.25e9
       subtraction is about 1e-06 absolute, which is what the hubs show. It is the
       arithmetic signature of the same floating-point numbers being subtracted and
       added back.
rule   INVERT THE DECISION RULE AND SOLVE, rather than sampling one side of it
cmd    MASS_PROPERTY_AGREEMENT 1e-13 -> 1e-30 WITH the bending rotary inertia doubled
out    9 failed -- and the platform inertia assertion PASSES, residual still 3.375e-36.
       The nine reds are the hubs and the CoG failing on their own round-off at 1e-17,
       not on the defect.
judge  NO value of this tolerance detects a 100 percent rotary-inertia error on the
       platform. There is no threshold to solve for, which is what a vacuous gate is.
```

**The CoG half is the same shape in a milder form.** `remainder_point` at `:450` is solved
from the first-moment equation, so the quantity the assertion inspects is identically zero
and carries neither a sign nor an operating point. That is why the negated coupling block
above passes: a comparison whose expected value is exactly zero has nothing for a sign
error to show against. The real content of the placement rule is asserted DIRECTLY and
well by `test_the_REMAINDER_is_placed_to_match_the_first_MOMENT` -- 11 red under the +5 m
cell -- so the CoG gate is not adding a check, it is restating one.

**Why this is (c) and not a closure item.** CZ0 third head is *what a gate claims, on which
quantity, at what threshold.* The G3.1a row in `docs/milestones/F3.md` was edited THIS STEP
to read *"All three are asserted since DY1/DY2; the narrowing that reported the inertia
rather than asserting it is withdrawn"*, and the same row concedes that the narrowing first
reason -- the deck superstructure inertias satisfy the lamina identity exactly and are
typed placeholders -- *"remains true"*. A narrowing that published an honest measurement
has been replaced by an assertion that cannot fail, against a placeholder the plan still
calls a placeholder. The narrowing was the better artifact.

**Why I am NOT escalating this to a STOP, on the record so the choice can be argued with.**
DY0c construction is not wrong. Building a model that reproduces the deck mass, CoG and
inertia is a legitimate and probably necessary thing to do, and the alternative is a model
that does not reproduce them. What is wrong is one row of the gate table calling the
reproduction a proof, and that is repairable without reopening DY0. The verification ladder
is green on CI at the judged commit. Nothing downstream is uninterpretable: the mass half
has measured content, the section gate has measured content, and the placement rule has a
direct test that reddens. A STOP would halt the project against 31 October over a claim
boundary. If the technical supervisor reads it the other way that is a decision above me,
and I have written down exactly what it turns on.

**Closed when** EITHER (i) the inertia comparison is against a quantity the deck constrains
independently of the remainder. I am describing the predicate and not writing it: a BOUND
rather than an identity is the honest form -- for instance that `J_r` is positive definite,
and that the members own contribution is a stated FRACTION of `J_b(G)`, published per body
and per component, with the direction of the inequality recorded. OR (ii) the site and the
plan row say in one sentence that mass, CoG and inertia are reproduced BY CONSTRUCTION,
name what the three tests actually check -- the consistency of `inertia_about` with
`rigid_properties` and of the assembled matrix with the scalars in `_build_body`, which is
real and worth keeping -- and G3.1a claim is re-scoped to that. Either is acceptable. What
is not acceptable is a published assertion that cannot fail. The tolerance sentence *"the
entry is known to be tight enough to see a real defect"* is corrected in the same commit,
per BP0.

**R597. (c, blocking) Nothing in the tree connects a built member node to the deck joint
point it came from, so the frame GEOMETRY is ungated -- and the rewrite lost a detection
the old CoG test had. `floatfea/model/platform.py:557` claims otherwise in prose, with no
test and no triple.**

```
cmd    every member whose label ends in "1" has its far end moved +3 m in x, inside the
       builder, AFTER the deck is read -- four arms 3 m too long
out    43 passed; and 1765 passed across tests/unit and tests/verification
cmd    the last member of each body re-pointed onto the FIRST member line -- the count
       stays 16, the labels stay unique, four arms are duplicated and four are gone
out    43 passed; and 1765 passed across tests/unit and tests/verification
cmd    the last member of each body REMOVED -- 11 members instead of 16
out    2 failed: `test_the_skeleton_is_FIVE_bodies_and_SIXTEEN_members` and
       `test_the_BUOY_NODE_MAP_names_its_body`. NEITHER IS G3.1a -- mass, CoG and
       inertia are green on all five bodies.
rule   `floatfea/model/platform.py:557` -- "Every coordinate comes from the deck own
       joint points. Nothing is typed, and no nominal radius is used -- DJ1 rule"
judge  a CW0 claim about the code, in a docstring, with no test and no triple beside it.
       And verdict 72 recorded that the PRE-DY1 CoG test caught a dropped member; the
       rewrite is better in every other respect and it lost that. The second cell is the
       one that matters: a materially wrong frame, counts and labels intact, and the
       whole unit and verification suite green at 1765 passed.
```

**Closed when** a shipped assertion compares each built member node to the deck joint point
it came from -- the deck is read in the same function and both are exact decimals, so this
is cheap -- OR the sentence at `:557` is deleted, DJ1 provenance is stated in the plan as
unasserted, and G3.1a reach is written without it. **Both halves, per the site-by-site
rule in CLAUDE.md.**

**R598. (b, blocking) `MASS_PROPERTY_AGREEMENT` names a counter that does not exist, and
its published worst measurement is 11.6x high. `floatfea/tolerances.py:1511` and `:1500`.**

```
rule   every citation resolves; a counter is a test
cmd    git grep -n "MISPLACED_remainder"
out    floatfea/tolerances.py:1511:# It carries a counter: `test_G3_1a_a_MISPLACED_remainder_reddens` moves the
out    one line, and it is the comment itself
judge  a phantom. `tests/test_counters_are_injected.py` cannot see it -- `REGISTERED` is
       a hand-written list and this entry is not on it, and that file own docstring says
       "a constant with no counter registered here is not covered at all" -- so the guard
       silence is not evidence. The sentence that follows, "so the entry is known to be
       tight enough to see a real defect and not merely loose enough to pass", is
       unsupported twice: the test is absent, AND R596 inversion cell shows that on the
       platform no value of this entry sees the defect.
rule   tolerances.py:1500 -- "Measured across the five bodies of F3 skeleton -- mass, CoG
       and the full inertia tensor, each relative to the quantity compared -- the worst
       residual is 2.2119e-15", and "about 45 over the worst measurement"
cmd    that same measurement reproduced at `d838d77`: rigid_properties(body_mass_matrix)
       against deck_mass, deck_cog and deck_inertia, per body, relative to each
out    platform  mass 0.0000e+00  cog 5.3218e-18  inertia 3.3747e-36
out    hub1      mass 0.0000e+00  cog 1.1642e-17  inertia 9.5367e-17
out    hub2      mass 1.5522e-16  cog 4.4238e-17  inertia 1.9073e-16
out    hub3      mass 0.0000e+00  cog 2.0955e-17  inertia 9.5367e-17
out    hub4      mass 1.5522e-16  cog 8.1491e-18  inertia 9.5367e-17
out    WORST = 1.9073e-16 at hub2 inertia; 1e-13 / worst = 524.29x
judge  the published figure is 11.6x high and the headroom is 524x, not 45x.
```

**What DOES hold, checked rather than assumed, because the entry is mostly right.**
`eps = 2.220446e-16` and `36 * eps = 7.993606e-15` exactly as written; `1e-13 / (36 eps) =
12.51x`, so the "factor of about 12" is right; `n_dof = 36` for a six-node body, correct;
`1.25e6 * 50 = 6.3e7` and `1.25e6 * 2500 = 3.1e9`, correct; `ROUNDOFF_IDENTITY = 1e-14` and
the reason for not reusing it is sound. **The CLASS line is right and the form is right** --
it is an exactness entry, dimensionless, relative to the quantity compared in every use, one
entry governing kilograms, metres and kilogram-metres-squared alike, and **setting it from
the derivation rather than from the measurement is the correct choice for the correct
reason.** I am not asking the value to move. What is wrong is the measurement published
beside the derivation, and that the entry offers the platform 3.375e-36 as evidence about
arithmetic when it is evidence about cancellation.

**Closed when** the counter exists at a path this entry names and reddens when the defect it
declares is injected -- OR the counter sentence is deleted and the entry states that it has
none and why, which for an exactness entry is defensible and is what I expect; **AND** the
`2.2119e-15` figure and the "about 45" that depends on it are regenerated by a committed
script at the commit that publishes them, or moved to the step report and replaced here by a
single number and a pointer (BI3).

**R599. (d, blocking -- RULED, and the permitted repair is DELETION) The two red
guard-states are the guard FAILING FALSE. `tests/test_report_guard_states.py:713-743`.**

The implementer is right, did not touch it, and was right not to. This is my call to make.

```
cmd    python -m pytest tests/test_report_guard_states.py -q -k "answers_header_names_an_older_verdict_commit or guard_state_declared_GREEN"
out    2 failed: "the guard failed through [test_the_answered_verdict_is_the_NEWEST_one,
       test_the_generator_would_catch_a_row_under_the_wrong_number,
       test_the_CI_section_is_about_the_REVIEWED_commit], none of which is a named
       reporter. A failure nobody can locate is half a report."
out    the nested run inside the harness: 3 failed, 160 passed -- and one of the three
       prints "the CI section first commit is `6c09932` and the verdict judged `4708cc2`"
judge  the planted defect is detected THREE TIMES and every one of the three reporters
       names the commit and the file. The assertion own message -- "a failure nobody can
       locate" -- is FALSE about this state, and that is what failing false means. The
       criterion is written beside the tuple in the implementer own words: "the right
       answer for an anonymous collapse and the wrong one for a test that names the
       commit and the file." All three qualify.
```

**AND THE WHITELIST IS UNSOUND IN BOTH DIRECTIONS, which is why a name is the wrong
repair.** If the only reporter is unlisted, the state goes red with nothing wrong -- what
happened here. If a LISTED reporter fires for an unrelated reason, the state goes green
while the real reporter is absent -- which is R516, recorded in the comment three lines
above the failure, where a state "had been certifying nothing". A closed list of reporters
inside a suite that grows cannot be right in either direction, and adding a name has now
been the repair three times: R516, CI1 two, and this. **DR1 is absolute and specific about
exactly this shape: a guard that fails false is DELETED, with the reason recorded at the
site, not repaired.**

**What is deleted is the `named` tuple and the assertion at `:713-743`, not the two
states.** The states are good -- they plant a real defect and `assert code != 0` at `:712`
keeps the property that matters, that the guard reddens. Locatability survives where it is
done properly: `_assert_diagnosis` names the expected reporter PER STATE instead of
whitelisting a whole suite, and neither failing state is in `DIAGNOSIS`, so deleting the
whitelist costs them nothing they had.

**Closed when** `tests/test_report_guard_states.py:713-743` is gone, the reason is at the
site naming R599 and DR1, and `python -m pytest -q` reports `0 failed`. Do not add a name.
Do not delete the two states. Do not extend `DIAGNOSIS` to cover them -- that is an
extension and DR1 forbids it.

## Closure items

Named, with the file and what would close each. **Fixed once, in the closure commit for
this step, and not re-reviewed item by item.** C12, C14, C18 to C25 and C26 to C32 carry
forward except where noted.

**C31 is CLOSED by measurement.** Verdict 72 said CI could never, by construction, confirm
a fix for a red that a report revision causes. `workflow_dispatch` at `d838d77` did it. The
route is real and the implementer is the one who has it.

**C33. The whole-suite figure in the report is two commits early.**
`docs/reports/F2/step-7.md` publishes `2621 passed, 1 failed` at `56d6810`; my run at the
report own commit `d838d77` is `2931 passed, 2 failed`. The report names its commit so it
states nothing false, but 310 tests separate the two and several guards are parametrised
over the report own rows, so the number grows as the report is written. Closed when the
report either publishes a figure at its own commit or says in one line why it cannot and
what the gap is.

**C34. `_NEGLIGIBLE_FRACTION` is a dead literal with a false docstring.**
`floatfea/model/platform.py:85-89`. All three uses were deleted at `ecebd78`, which is the
right answer. The declaration remains, and its docstring describes a builder DY0 withdrew
(quote, when a member is mass-sized). The R593 condition also asked for that docstring to
stop saying the finding it gates is not a pass or a fail, and that half was not done.
Closed by deleting lines 85 to 89.

**C35. The two builder limits have lost their recorded reason, and it pre-dates this step.**
`floatfea/model/platform.py:90-97` is a bare string immediately after the
`_NEGLIGIBLE_FRACTION` docstring, so the justification for `MIN_LENGTH_OVER_DIAMETER` and
`MAX_LENGTH_OVER_GYRATION` now documents nothing -- a module-level string attaches only to
the assignment directly above it. Present at `5ef2e3d` too, so this round did not cause it.
Deleting C34 closes C35 as a side effect, which is why they are listed together.

**C36. The DY7 symmetry row pairs the wrong joints.** `docs/reports/F2/step-7.md`, the DY7
block. The report says joints 5/15, 6/14 and 7/13 mirror across y. I re-ran the script at
`--duration 30.0` and got the exact published figures for joints 2 and 3, so the numbers
are real; the pairing is not.

```
cmd  python scripts/report_joint_reactions.py --duration 30.0
out  5 buoy4  Fy -4.0503e-02 Fx -1.3037e-01   13 buoy10 Fy +4.0503e-02 Fx -1.3037e-01
out  6 buoy5  Fy -3.4939e-02 Fx +2.8571e-01   15 buoy12 Fy +3.4939e-02 Fx +2.8571e-01
out  7 buoy6  Fy +7.9455e-02 Fx +1.9953e-01   14 buoy11 Fy -7.9455e-02 Fx +1.9953e-01
judge the mirror pairs are (5,13), (6,15) and (7,14). Under the published pairing 5/15,
      Fy is -4.0503e-02 against +3.4939e-02 and Fx is -1.3037e-01 against +2.8571e-01,
      which is not a mirror in either component. THE CLAIM IS TRUE AND ITS EVIDENCE ROW
      IS WRONG -- the symmetry does hold, exactly, on the right pairs.
```

**C37. The DY7 command row does not produce the DY7 output row.** Same block. The `cmd` is
`python scripts/report_joint_reactions.py`, whose default is `--duration 40.0`, and the
`out` rows are at `t = 30.000 s`. I measured both: the default gives `t = 40.000 s` and a
different set of numbers. Closed by writing the invocation that was actually run.

**C38. The buoy Fz maximum in the reaction script is taken over the wrong joint set, and
the published number survives it by luck.** `scripts/report_joint_reactions.py`, the closing
block, `for i in range(12)`.

```
cmd  the deck joint order, read from platform12_deck.yaml
out  1-3 buoy/hub1, 4 hub1/platform, 5-7 buoy/hub2, 8 hub2/platform, 9-11 buoy/hub3,
     12 hub3/platform, 13-15 buoy/hub4, 16 hub4/platform
judge range(12) takes joints 1 to 12, which INCLUDES three hub-platform joints and
      EXCLUDES buoy10, buoy11 and buoy12. It is a maximum over a set that is not the set
      it is named for, which is the assertion-domain shape.
cmd  the same run, all sixteen joints inspected
out  the true buoy-joint maximum Fz at t = 30 s is 6.5806e-01 at joints 10 and 11, which
     ARE inside range(12); the three hub-platform Fz are 3.83e-01, 1.62e-01 and 4.85e-01,
     all below it; the three omitted buoy joints are 5.28e-01 and 5.32e-01 twice
judge the published 0.6581 N and the ratio 2.34e-03 are CORRECT at this operating point.
      The defect is latent rather than a wrong figure, and the conclusion it carries --
      that the reactions are perturbations about equilibrium, so a member-force table
      built from them alone understates every arm by three orders of magnitude -- stands.
      That conclusion is the most valuable thing in the round and I am not disturbing it.
```

Closed by selecting the buoy joints by name, which the builder already does elsewhere.

**C39. The buoy weight in the reaction script is typed.** Same file: `weight = 28.67 *
9.81`, while `deck.bodies` is in scope and `buoy1` carries `mass: 28.67`. The value is
right -- I read the deck -- but it is typed into a script whose whole argument is that
nothing in it is reconstructed. Closed by reading the mass from the deck and g from `basis`.

**C40. `tests/test_plan_matches_tolerances.py` is a THIRD guard hardcoded to a closed
milestone path, and my ruling is to LEAVE IT.** The implementer reported this against itself
and deferred it correctly: an F3 tolerance now sits in the closed F2 plan and the table
heading had to change to stay true. That heading change is honest and I accept it. The guard
does not fail false -- it passes, and what it checks, that every declared tolerance appears
in a plan table, is real. Re-pointing it is a guard edit, which DR1 forbids without a
directive, and deleting it would remove a real check to fix a cosmetic one. Recorded so the
debt stays visible and the F3 plan can carry the re-point when the freeze lifts. This is the
same shape as R564 and the second DX2 ruling, now in a third guard, and the PATTERN is worth
Xabier attention rather than another round of mine.

**C41. The G3.1a plan row and two test docstrings overstate what is checked.** Covered by
the R596 closing condition; listed here so the closure commit does not miss the prose half.

**C42. DY6 encoding fix is INCOMPLETE and it broke my own tool on this very verdict.**
`scripts/write_verdict.py:103`. The write side is explicit UTF-8 now; the read side is
too, and that is the problem -- the file already in the tree was written by the OLD
`write_text` and its header carries one cp1252 byte.

```
cmd  python scripts/write_verdict.py --milestone 2 --step 7 < the body of this verdict
out  UnicodeDecodeError: utf-8 codec can not decode byte 0x97 in position 9
cmd  the file bytes inspected
out  b"# Review  F2 step 7
..." -- byte 9 is a lone cp1252 em dash
out  14 non-ascii bytes in all: one 0x97, and 0xc2 0xa7 x5 and 0xe2 0x80 0x94, which
     are VALID UTF-8 and came from my verdict body
judge the file is MIXED -- a cp1252 header from the old tool and a UTF-8 body from me --
      so no single-encoding read can open it. This is precisely the failure the report
      says DY6 prevents, recurring on the transition file, and it stopped the verdict
      being written at all. I repaired it by replacing that ONE byte with U+2014 encoded
      as UTF-8, verified the result decodes and that both earlier rounds survive
      unchanged at 1550 lines, and then the tool ran and accumulated correctly.
```

Closed by `errors="replace"` or a cp1252 fallback on the read at `:103`, so the next
reviewer does not have to hand-patch a file to write a verdict. It will not recur on this
file, which is why it is a closure item and not a hold -- but it would recur on
`docs/reviews/F3/step-1.md` if any pre-DY6 verdict is ever appended to.

## Tolerances touched

```
cmd  git diff 5ef2e3d..HEAD -- floatfea/tolerances.py
out  one entry ADDED, nothing changed, nothing removed, nothing widened
```

| | |
|---|---|
| constant | `MASS_PROPERTY_AGREEMENT` |
| old | did not exist; the section read "(no entries yet -- F3)" |
| new | `1e-13` |
| form | EXACTNESS. Dimensionless, relative to the quantity compared in every use, one entry over kilograms, metres and kilogram-metres-squared. Correct form, and I checked it is not an absolute tolerance on a dimensional quantity. |
| derivation | `36 * eps = 7.993606e-15`, verified; `1e-13` is `12.51x` it, verified; `n_dof = 36` for a six-node body, verified. Set from the derivation rather than from the measurement, with the reason stated, and I agree with that choice. |
| counter | **NAMED AND ABSENT.** `test_G3_1a_a_MISPLACED_remainder_reddens` does not exist. R598. |
| justification | the `docs/milestones/F2.md:1383` table row, present and matching, plus the entry own comment. That comment measurement figure is 11.6x high. R598. |
| widened? | No. Nothing in this file was loosened. `_NEGLIGIBLE_FRACTION` moved the other way: three uses deleted and no replacement threshold. |

**And the entry is the RIGHT decision.** R593 asked for a comparison epsilon to be either
deleted or promoted properly. Both happened: the epsilon went, and the quantity that does
need a threshold got a declared entry with a class line and a derivation. The two defects in
it are a phantom citation and a stale figure, not the value.

## Carried for the next step

**R596, R597, R598 and R599 carry BY NAME into `docs/reports/F3/step-1.md` and stay
BLOCKING there.** They are answered before any new F3 step-1 work and the answers go in that
report Carried section. Closure items C12, C14, C18 to C25, C26 to C30 and C32 to C41 go
into this step closure commit as one list.

**Schedule, and the escalation the rule asks for.** F3 closes 13 October. The platform
skeleton is the first executable thing in it and it builds, which is the good news. This
step closes carrying four blocking items. If F3 step 1 also closes carrying blocking items,
`CLAUDE.md` requires the choice to be stated to Xabier -- slip the date or reduce scope --
and I am flagging now that R596 is the item most likely to force it, because its honest
repair is a decision about what G3.1a is FOR rather than a code change.

## Next step opens when

**It opens now, and it opens with a debt.** PASS is the cap ruling. The conditions, in this
order:

1. **R599 first, in its own commit, because everything else is measured against a green
   suite.** Delete `tests/test_report_guard_states.py:713-743`. Do not add a name.
2. **R596, R597 and R598 before any new F3 step-1 work.** Each answered site by site with
   its diff hunk, or the site named and the reason it was left given.
3. **The closure list once, in one commit.**
4. Then DY8c: `docs/reports/F3/step-1.md`, the step-marker move, and the F3 skeleton.

**And yes, my next verdict is on the F3 tree, at `docs/reviews/F3/step-1.md`**, and the
three-verdict count restarts there. The four carried items are already in F3 territory --
`floatfea/model/platform.py`, `tests/verification/rung3/` and `floatfea/tolerances.py` --
so the carry is natural rather than a straddle. `docs/reviews/F2/step-7.md` is CLOSED at
this verdict, and under DD1 nothing later written about the tree reopens it.

## The adversarial corpus (BE3)

`tests/corpus/platform_mass_property_gate.txt`, batch 21, committed separately at
`8b4b687`. **24 entries, all new this round. Sixteen carry a mutation; the shipped suite
caught 7 and MISSED 9.** The nine misses are the measurements behind R596, R597 and R598.
The other eight are `expect=explain` entries about published figures and claims.

The number that matters: **9 of 16 unseen mutation shapes are green under the shipped
suite**, against 23 of 31 missed in batch 20. Fewer are missed than last round, and the ones
still missed have moved inward -- they are in the gate now rather than around it, which is
why three of them are blocking findings rather than corpus rows.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F2 step 7
Reviewed commit: e5e2015e18dd27034197b56cadd404662514ddbf
Verdict: HOLD

## Round of 2026-09-29 -- SEVENTY-SECOND verdict on F2/F3

**Reviewed commit: `6c09932`.**
Tests: 2812 passed, 0 failed, 0 skipped   (my own run at `6c09932`, `python -m pytest -q`, 1358.62s, one invocation, no split)

**This is the SECOND round of this step. The next one closes it (CZ0).**

**WHY HOLD, AND IT IS NOT ABOUT CI THIS TIME.** All four of verdict 71's findings are
genuinely answered and I re-measured each rather than reading the report. The suite is
green at the judged commit on my machine, in one run, including the two the report
reports red -- the interval closed, measured rather than predicted. **What holds this
round is the skeleton itself.** `floatfea/model/platform.py` builds five bodies and
sixteen members correctly partitioned, and its gate cannot fail on the quantity the plan
locked it to. I set the one designed section in the model -- the 25 m cluster arm,
2.5 m x 180 mm, the only member with a recorded basis -- to a **1 mm wall**, a section
wrong by a factor of 180, and `test_platform_skeleton.py` printed `32 passed`. Six
findings follow from that reading and from two arithmetic errors it uncovered in the
remainder inertia. They are four sites in two files.

**Do not read this HOLD as a judgement on the round's work.** The plan re-lock is right,
the buoy ruling is right, R586 was deleted rather than loosened, and the implementer found
and reported a rounding bug of its own before I got here. The builder is the first thing in
this milestone that is the actual platform, and it is close.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 6c099323715277e6c487dbf67dcf8d1d22218991 --json databaseId
out  []
cmd  gh run list --limit 4 --json headSha,databaseId,status,conclusion,event
out  36654231979  863c1aa  push  completed  failure
     36523001390  4708cc2  push  completed  failure
     36462874787  2e24459  push  completed  success
cmd  git show --stat --format="" 6c09932
out  docs/reports/F2/step-7-answers.json | docs/reports/F2/step-7.md  -- nothing else
cmd  git show 6c09932:.github/workflows/ci.yml   (the on: block)
out  push: branches ["**"]  paths-ignore: "docs/reports/**", "docs/reviews/**"
judge UNAVAILABLE -- PATH-IGNORED BY DESIGN. Not red, not green, and not CK2 either:
      no job was started because no workflow was triggered, and there is no billing
      annotation to read. Polled three times over the review; the filter stays empty.
```

**THE INVOCATION'S EXPECTATION IS WRONG AND THE REASON IS CHECKABLE.** `4708cc2` touched
the identical file set and did get a run, but not because the filter let it through:

```
cmd  git show --stat --format="" 475c224      (4708cc2's parent, same push)
out  tests/test_report_guard_states.py | ...   -- code, so the push was not ignored
rule GitHub evaluates paths-ignore over ALL commits in a push, not over the head commit
out  863c1aa's run exists for the same reason: f14fad2 and de67ba5 rode with it
out  6c09932 was pushed ALONE, a docs/reports-only push, so nothing triggered
judge it will never run at this commit on a push. `gh workflow run CI --ref F3` is the
      one route left and it is the implementer's to take, not mine to spend.
```

**THE LAST RUN THAT EXECUTED, per CK2's procedure.** `36654231979` at `863c1aa`,
conclusion `failure`: the verification ladder green in every rung, three reds in
`lint, unit and guards`, all three report-guard states.

```
cmd  git diff 863c1aa..6c09932 -- tests/verification scripts .github
out  (no output)
judge the LADDER result still describes the tree under review and I am relying on it.
      The GUARDS result does NOT, and this is the one thing worth writing down: its
      three reds were guards reading the REPORT, the report is the only thing that
      moved, and the directory it lives in is the one CI is configured never to run
      on. CI CANNOT, BY CONSTRUCTION, EVER CONFIRM THE FIX FOR A RED THAT A REPORT
      REVISION CAUSES. My own run at the judged commit is the only measurement of
      it that exists, and it is green. Recorded as C31; it is not why this is a HOLD.
```

## Carried

Verdict 71 carried four blocking items -- R586, R587, R588, R589 -- and closure items
C12, C14, C17 to C25.

```
cmd  python scripts/check_carried.py --verdict docs/reviews/F2/step-7.md --report docs/reports/F2/step-7.md
out  check_carried: all 4 findings carried        exit 0
cmd  the report's revision-6 header
out  Answers: verdict 71 @ 7bd86e8
judge 7bd86e8 IS verdict 71's own commit and 71 IS the latest verdict, so instruction
      1b is satisfied and DX2's third ruling was followed. Not holding on it.
```

**I re-measured all four. Every one is answered.**

* **R586 -- ANSWERED at `f14fad2`, and it is a DELETION, which is what I ruled.**

```
cmd  git show f14fad2 -- tests/test_report_carried.py
out  the four-line `assert len(EXPECTED) >= 5, (...)` statement is GONE, replaced by
     a 16-line comment naming R586, R546, the two verdicts with no satisfiable state,
     and the eight reds it caused
out  the two assertions above it -- `_FINDING.findall(VERDICT_TEXT)` non-empty and
     `CARRIED.strip()` non-empty -- are byte-identical
cmd  python -m pytest -q          (mine, at 6c09932)
out  2812 passed, 0 failed, 0 skipped
judge deleted, not loosened; no smaller floor, no parametrisation; reason at the site.
      Closed.
```

* **R587 -- ANSWERED at `8b14de3`, a standalone `plan:` commit, AND MY PROPOSED FIX WAS
  WRONG. I am recording that in my own words because it is my error.** I wrote that the
  buoys are 85.6% of the deck mass and that omitting them checks the one designed section
  against loads it was not sized for. The first half stands. The fix I named -- twelve
  lumped buoy masses -- would have double-counted every buoy, and DX0 is right: each buoy
  is its own FloatSim body on a gimbal, so its weight, buoyancy, wave force and inertia
  already arrive at the cluster-arm tip as the transmitted force and the locked-axis
  moment, which is what FloatSim computes. A mass beside the reaction counts it twice.

```
cmd  sed -n on docs/milestones/F3.md sections 3.2, 3.3 and 3.4
out  :305  attach each MODELLED body's remainder mass by rigid link
out  :306  apply the twelve buoy-joint reactions as the loads at the cluster-arm tips
out  :318  "Each modelled body" is the platform and the four hubs
out  :335  THE BUOYS' LOADS ARE NOT DEFERRED
out  :353  Label: buoy spar columns not assessed as members; buoy loads applied as
           joint reactions
cmd  the built model, bodies dict lookups
out  bodies["platform"] and bodies[hub] only; no buoy mass and no buoy inertia
     reaches any BodyModel   -- corpus entry topo_no_buoy_mass_entered
judge the contradiction is gone, the scope section and the executable list agree, the
      label is on the Superstructure, and the double-count I would have introduced is
      not present. Closed, and the ruling is better than my finding was.
```

* **R588 -- ANSWERED at `f14fad2`.** `_IMPORT_DIRS` sits beside the preflight and the
  refusal is scoped to `.py` on the three directories `build_deck` puts on `sys.path`. The
  false sentence is gone. I did not plant a file in `../HSP-runs` to re-demonstrate it --
  the mechanism is two `sys.path.insert(0, ...)` calls and two bare-name imports, both
  unchanged.

* **R589 -- ANSWERED at `f14fad2`.** Renamed
  `test_G3_2_the_file_matches_its_RECORDED_TEXT_digest`, the docstring states the CRLF
  limitation and why it is deliberate, the message says text. **The behaviour is
  unchanged, which is what I asked for.**

* **C17 -- CLOSED at `f14fad2`.** `docs/verification/README.md:91-107` now names the three
  digests, the coplanarity assertion, the twelve-mutation counter, and says in terms that
  the parse-and-re-emit comparison is not the gate and no longer carries the id.

* **DX2's three process rulings -- LANDED at `de67ba5`, and that commit is R594 below.**
  The rulings themselves are right and I am not disputing any of them.

## Withdrawn in earlier rounds, recorded here so the record survives the round

* **R567 -- WITHDRAWN by verdict 69.** Its site, the `two_digit_step_number` guard state,
  was deleted under DT2. `docs/milestones/F2a.md:228` records the same withdrawal. A report
  may write `withdrawn` for R567 without the guard reddening, and `carried` remains correct
  and weaker. Carried forward in every verdict from here.

**AND FROM THIS ROUND THE FILE ACCUMULATES (DX2).** Verdict 71's round is appended below
mine, verbatim. **Verdict 70's round is NOT re-imported and that is a decision, not an
oversight:** it exists in git at `1b895db`, it was a PASS, and
`.claude/hooks/require-verdict.sh` treats any `^Verdict: *PASS` anywhere in the file as
closing the step. Importing it would release the gate while six blocking items are open.
The disposition of step 7 under DD1 is unchanged -- it closed at verdict 70 and these
rounds are about the tree -- and `docs/reviews/` is where that is written down, not the
hook.

## Findings

**R590. (c, blocking) G3.1a's mass half cannot fail. The remainder is DEFINED as the
residual, so the assertion reduces to an identity, and the one designed section in the
model can be wrong by a factor of 180 with the gate green.
`tests/verification/rung3/test_platform_skeleton.py:112-124` against
`floatfea/model/platform.py:417`.**

This is the finding that outranks everything in the report and it is not adversarial in
any clever way: I changed one number.

```
cmd    floatfea.model.platform.CLUSTER_ARM_WALL rebound, the SHIPPED module re-run
out    0.180 m (recorded) -> 32 passed
out    0.090 m            -> 32 passed
out    0.045 m            -> 32 passed
out    0.001 m            -> 32 passed
out    0.400 m            -> 32 passed
rule   from_matrix + body.remainder_mass == approx(body.deck_mass, rel=ROUNDOFF_IDENTITY)
out    at 1 mm: member mass per hub falls 7.723983e+05 -> 4.622182e+03 kg and the
       remainder rises 7.276017e+05 -> 1.495378e+06 kg, exactly compensating
judge  platform.py:417 is `remainder = deck_mass - member_mass`, with no clamp, so
       member_mass + remainder == deck_mass is an identity in float arithmetic. The
       only non-trivial content left in the assertion -- the assembled matrix against
       A*L*rho -- is the SEPARATE test immediately below it at :128-140.
```

**AND THE DOCSTRING IS WHY THIS IS (c) RATHER THAN A CLOSURE ITEM.** `:115` reads *"This is
the half of G3.1a that rests on real design figures"*, and `:17-18` reads *"mass and CoG
are ASSERTED. They come from real design figures -- F1's 1250 t truss and the hub's 3 rods
x 4 kg."* One grep refutes both. `docs/milestones/F3.md:309` and `:323` say **"G3.1a is the
gate that proves the sizing"** and **"per body, never on the sum"** -- the per-body part is
honoured and the sizing part is not asserted at all. Under CZ0 this is *what a gate claims,
on which quantity*.

**Two more cells, because the shape has a second consequence F3 section 3.3 names by
name.**

```
cmd    every hub body mass 12.0 -> 4.0 model scale, so three 257 t arms outweigh a
       500 t hub by 54.5 percent
out    32 passed; four NEGATIVE remainder findings emitted; no test reads them
cmd    every hub body mass 12.0 -> 60.0, so the lumped remainder is 85 percent of the body
out    32 passed
rule   F3 section 3.3: "clamping would make G3.1a pass on a body whose steel does not
       fit inside its own mass"
judge  nothing clamps, so the letter of the rule holds -- and the gate passes on exactly
       that body anyway, by a different route. The sizing finding the plan requires IS
       emitted at platform.py:420-427 and NO shipped test asserts that it fires; the two
       finding shapes that are asserted are the lamina identity and the rotary inertia.
```

**Closed when** the mass half compares a quantity the deck constrains. I am describing the
predicate and not writing it: for a body whose members carry a RECORDED section (the four
hubs) the deck mass and the member mass are independent, so `0 <= remainder <= deck_mass`
is a real assertion and the fraction it lands at is a number worth publishing; for a body
whose members are MASS-SIZED (the platform) the identity is unavoidable and the honest move
is to say so at the site and assert the sizing round-trip instead. **And the
negative-remainder finding is asserted**, the way the lamina finding already is, so F3
section 3.3's own hazard has a test. The two docstring sentences quoted above are corrected
in the same commit, per BP0.

**R591. (a, blocking) The built platform body's centre of gravity is 10.3315 m below the
one the deck declares, and G3.1a's CoG half cannot see it -- it reads the MEMBERS' centroid
about the body's own node and never compares anything to the deck.
`floatfea/model/platform.py:339` and `:454`, gate at
`tests/verification/rung3/test_platform_skeleton.py:144-162`.**

First the referent, because F3 section 3.1 records this as a forced assumption and the
producer states it outright:

```
cmd    grep -n "reference_point" ../HSP-runs/floatsim/driver.py
out    :207-209  "M7-Foundation PR4 assumes the deck's reference_point IS the body
       frame origin and the CoG (no explicit CoG-offset field in the deck)."
out    :219-223  rigid_body_mass_matrix(mass=..., inertia_at_reference=...,
       cog_offset_body=None)
judge  the deck DOES declare a CoG per body -- it is the reference point -- and
       docs/milestones/F3.md:271-275 is right for a STRONGER reason than it gives.
       So G3.1a's CoG row has a referent, and DV0's "G3.1a checks against the deck's
       body mass, CoG and inertia" is well defined rather than ambiguous.
```

Then the miss:

```
cmd    the built model, whole-body CoG = (m_members * members' centroid
       + m_remainder * deck reference) / total, per body
out    platform  members' centroid (0, 0, 24.6685) m, deck reference (0, 0, 35.0) m,
       remainder mass 9.313226e-10 kg, whole-body CoG (0, 0, 24.6685) m
out    dz = -10.3315 m, on the heaviest modelled body, 1250 t
out    hub1..4   dz = 0.0000 m -- the hubs are fine, their link is zero-length
rule   G3.1a: per-body CoG from the FE mesh against the model definition
cell   ONE VARIABLE: the deck's platform reference_point z, 0.7 -> 2.0 model, which
       moves the declared CoG from 35.0 m to 100.0 m full scale. Nothing else touched.
out    32 passed. link_length becomes 75.3315 m and no assertion reads it.
cell   ONE VARIABLE: the same reference_point x, 0.0 -> 1.0 model -- 50 m IN PLAN,
       which is the component the gate does look at
out    32 passed, because the offset is measured from the body NODE.
```

**The assertion is not vacuous -- it is about a different quantity, and I measured that
too, so this is not a claim that the test is worthless.** Removing one of hub1's three
cluster arms gives an offset of `5.4127e+00` m against a threshold of `2.5e-13`, so it does
bite on a dropped member or a mislocated node. What it cannot contain is the failure: the
collection it inspects is the members about their own node, and the deck is not in it. That
is the recorded *assertion domain blindness* guard exactly.

**Why this is (a) and not only (c).** The 1250 t is 10.33 m lower than the definition says,
and F4 reads this model for inertia relief. A body whose mass sits 10 m below where the body
definition puts it produces the wrong rigid-body accelerations and therefore the wrong
member forces, and no gate in the tree says so.

**Closed when** two things, and the first is the model: either the platform's remainder
carries enough mass to put the body CoG where the deck declares it, or the plan records that
it cannot and why -- DJ1's mass-sizing rule and this requirement pull in opposite directions
for this body and the choice is above the implementer, so a `plan:` commit is an acceptable
answer to the first half. The second is the gate: G3.1a's CoG half compares the WHOLE body's
CoG, all three components, against the deck's reference point per body, and the sibling
docstring stops claiming the present check rests on design figures.

**R592. (a, blocking) `remainder_inertia` subtracts the members' contribution from `Izz`
alone, so the built bodies carry 20.9% (platform) and 51.5% (each hub) more `Ixx` than the
deck; and the `Izz` it does subtract uses a rod formula that disagrees with the assembled
matrix, so the gate publishes a figure labelled `deck` that is not the deck's.
`floatfea/model/platform.py:438-439`, gate at
`tests/verification/rung3/test_platform_skeleton.py:165-189`.**

```
cmd    remainder_inertia against the deck tensor, Froude-scaled at lambda = 50
out    platform  remainder Ixx 3.125000e+09 = the deck's Ixx, unchanged
out    hub1      remainder Ixx 1.562500e+08 = the deck's Ixx, unchanged
cmd    the members' own Ixx about the deck reference point, 20001-point quadrature
       along each member
out    platform  6.542588e+08 kg.m^2  = 20.9% of the deck Ixx, double-counted
out    hub1      8.045815e+07 kg.m^2  = 51.5% of the deck Ixx, double-counted
rule   F3 section 3.3: "the remaining inertia about that point"
cmd    sed -n on floatfea/model/platform.py lines 438-439
out    remaining = body["inertia"].copy()
out    remaining[2][2] -= member_izz
judge  Ixx, Iyy and every off-diagonal keep the full deck value. Nothing at the site
       says this is partial, so a reader of remainder_inertia gets a tensor that is
       the deck's with one entry adjusted.
cell   ONE VARIABLE: the deck's platform Ixy 0.0 -> 3.0 model, a product of inertia no
       symmetric lamina has. Nothing else touched.
out    32 passed -- the lamina predicate reads only the three diagonals and the
       remainder carries Ixy through unchanged.
```

**And the gate that was supposed to catch this cannot fail, in the strongest possible
sense.**

```
cmd    sed -n on tests/verification/rung3/test_platform_skeleton.py lines 178-189
out    member_izz = float(m6[5, 5]); remaining = float(body.remainder_inertia[2][2])
out    deck_izz = member_izz + remaining
out    assert member_izz + remaining == pytest.approx(deck_izz, rel=ROUNDOFF_IDENTITY)
judge  deck_izz is DEFINED two lines above as the sum it is then compared against.
       The assertion is x == approx(x). It cannot fail for any deck, any section or
       any geometry, and `assert deck_izz > 0.0` beside it is equally free.
cmd    the same three numbers against the COMMITTED deck's Izz
out    platform  printed "deck" 6.250897e+09   committed deck 6.250000e+09  ratio 1.000144
out    hub1..4   printed "deck" 3.130228e+08   committed deck 3.125000e+08  ratio 1.001673
out    the cause: `remaining` was formed by subtracting the builder's rod formula
       sum(m L^2 / 3) = 1.041667e+09, and the test adds back the ASSEMBLED matrix's
       m6[5,5] = 1.042564e+09. 8.97e+05 kg.m^2 invented for the platform, 5.23e+05
       per hub.
rule   the docstring at :187 -- "what IS asserted: the split is exact, so no inertia
       is invented or lost"
judge  the split is not exact and the sentence is the only statement of what the gate
       measures, which is the reading my own instructions name for (c).
```

**NOW THE RULING THE INVOCATION ASKED FOR, AND IT IS THE ONE PLACE I DISAGREE WITH THE
NARROWING WHILE AGREEING WITH ITS REASON.**

**The reason is TRUE and I verified it independently.** From the committed YAML: platform
`10, 10, 20`, every hub `0.5, 0.5, 1.0`, so `Ixx + Iyy - Izz` is `0.0` **exactly** on all
five modelled bodies, while every buoy in the same deck reads `47.886`, a relative `420`.
They are typed round numbers. Asserting an FE model against a placeholder would make a gate
turn on a number nobody derived, and that is `CLAUDE.md`'s fudge factor. **So measuring
rather than asserting is the right call and it is not a weakening to avoid a red.**

**What is wrong is that it is not the ONLY reason the assertion would be red, and the other
reason is a defect.**

```
cell   would a DERIVED deck inertia make the assertion pass?
out    NO, for any value. The remainder never decrements Ixx, so the FE total exceeds
       the deck Ixx by the members' contribution whatever the deck says -- 20.9% for
       the platform, 51.5% for a hub -- and the shortfall is a property of
       platform.py:438-439, not of the deck.
judge  a narrowing justified by reason A, taken while reason B would have reddened the
       same assertion, is the shape of a tolerance changed to make a red test green, in
       a different costume. The narrowing is SOUND and it is INCOMPLETE, and the part it
       is silent about is the part that is a bug.
```

**Two procedural notes on the narrowing, and neither is the finding.** It changed what a
gate the plan locks asserts, and it landed at `863c1aa` in a commit with the code, not in a
`plan:` commit; `docs/milestones/F3.md:465` still reads *"Per-body mass, CoG and inertia
tensor ... Reported and asserted PER BODY"*. That is BP0: the decision rule moved and the
document locking it did not move with it.

**Closed when** `_finish` subtracts the members' full inertia tensor about the point the
remainder attaches to -- all six components, from the same source the gate reads, so the
split is exact by construction rather than by two agreeing approximations -- and the inertia
test asserts `assembled + remainder == approx(the DECK's tensor)` on the components the deck
constrains, with the lamina narrowing kept and restated as what it is: the reason the tensor
is not asserted **component by component against a derived figure**, not a reason to assert
nothing. `F3.md:465`'s row is amended in a `plan:` commit in the same round, and the printed
`deck` label names what it prints.

**R593. (b, blocking) `_NEGLIGIBLE_FRACTION = 1e-12` is a comparison epsilon in `floatfea/`
outside `floatfea/tolerances.py`, its `not-a-tolerance:` reason is refuted by one grep, and
it has no measured margin and no counter. `floatfea/model/platform.py:61-65`, used at `:454`
and `:468`.**

```
cmd    sed -n on floatfea/model/platform.py lines 61-65
out    _NEGLIGIBLE_FRACTION: Final[float] = 1e-12
out    """not-a-tolerance: ... It is a REPORTING threshold on a quantity that is zero
       by construction ... and the finding it gates is a sentence, not a pass or a fail."""
cmd    sed -n on the same file line 468
out    if ixx > 0.0 and abs(ixx + iyy - deck_izz) <= _NEGLIGIBLE_FRACTION * deck_izz:
cmd    grep -n "LAMINA" tests/verification/rung3/test_platform_skeleton.py
out    :200  lamina = [f for f in superstructure.findings if "LAMINA" in f]
out    :201  assert len(lamina) == BODIES
judge  the sentence IS a pass or a fail. A shipped test asserts on the predicate this
       epsilon decides, and it is the test that carries the G3.1a narrowing -- so the
       exemption's own stated reason is false at the site, which is CLAUDE.md's
       "anything that functions as a tolerance under another name: comparison epsilons".
```

**And inverting the rule, which is the check the entry never gets.** The identity holds to
`0.0` exactly on all five bodies, so `1e-12` is never exercised: the margin is not large, it
is undefined. What the value actually decides is the smallest lamina deviation that still
reads as a placeholder, `1e-12` relative -- unmeasured, unstated, and the number a later
reader will reach for when a deck arrives whose inertia is derived but nearly planar.

**I am not asking for the value to move and I do not think the behaviour is wrong.** The
second use at `:454` is genuinely a reporting threshold and I would leave it. **Closed when**
the `:468` comparison is either an exact `== 0.0` -- which is what the data supports and
which needs no threshold at all -- or the constant moves to `floatfea/tolerances.py` with
the form, the counter (the smallest lamina deviation the same predicate detects, in the same
quantity) and the justification an entry there requires; and the `:61-65` docstring stops
saying the finding it gates is not a pass or a fail.

**R594. (process, blocking -- STOP-class, and I record why I am NOT escalating it to a STOP
verdict) `de67ba5` changes `docs/SUPERVISOR.md` in a commit that also touches `tests/`.**

```
cmd    git log --format="%h %s" 7bd86e8..6c09932 -- .claude docs/SUPERVISOR.md
out    de67ba5 process: report paths follow the plan; the verdict file accumulates (DX2)
cmd    git show --stat --format="" de67ba5
out    docs/SUPERVISOR.md           | 43 ++
out    tests/test_report_carried.py | 102 +++++++-----
rule   CLAUDE.md "The reviewer's own instructions are not edited inside a step": they
       change "only in a standalone `process:` commit ... never in a commit that also
       touches floatfea/ or tests/", and such a change "is a STOP-class finding". My
       own instruction 4b says the same, "regardless of its content".
judge  the commit's own message says it touches "no tests/ assertion about the code",
       which is a narrowing of the rule that the rule does not contain -- and it does
       add a tests/ assertion, `assert len(carrying) == 1`.
```

**WHY I AM NOT WRITING STOP, said once and available to be overruled.** My instructions
distinguish the two halves of that sentence: a mixed commit "is a STOP-class finding", and
"a change that removes a guard is a STOP". I read the diff line by line, which is the whole
point of the guard:

```
cmd    git show de67ba5 -- docs/SUPERVISOR.md | grep -c "^-[^-]"
out    0        -- purely additive, two new sections, nothing removed or reworded
cmd    git show de67ba5 -- tests/test_report_carried.py | grep "^-" | grep -c assert
out    0        -- no assertion deleted; two path constants re-homed, one added
cmd    git log --format="%h" 7bd86e8..6c09932 -- docs/reviews
out    (no output) -- no commit this round touches docs/reviews/ at all
```

A STOP means the locked plan is wrong or a low rung is red, and means everything after it is
uninterpretable. Neither is true here: the ladder is green, the plan is not what is wrong,
and the round's work is interpretable -- I interpreted it above. **So this is a blocking
process finding at STOP class, not a STOP verdict, and it is the second round running in
which a DR1-frozen guard was edited under a cited direction** (verdict 71 recorded the same
for C10/R585 and declined to escalate for the same reason). **Two is a pattern and three
would be a habit.** The next occurrence I will write as a STOP without reading the content,
because a rule whose enforcement depends on the reviewer liking the diff is not a rule.

**Closed when** the `tests/test_report_carried.py` half of `de67ba5` is separated from the
`docs/SUPERVISOR.md` half in the record -- a note in the closure artifact naming the commit,
the rule and the two hunks is enough; I am not asking for history to be rewritten -- and the
standing convention is restated: a commit that touches `docs/SUPERVISOR.md`,
`.claude/agents/` or `.claude/hooks/` touches nothing else, even when the directive asking
for the change also asks for a guard edit. Two commits, always.

**R595. (a, blocking) `Superstructure.buoy_joint_nodes` maps a buoy name to a node index
that is only meaningful inside one of five separate models, and nothing in the type or the
docstring says which. `floatfea/model/platform.py:146` and `:357`.**

```
cmd    the built model's buoy_joint_nodes
out    {buoy1: 1, buoy2: 2, buoy3: 3, buoy4: 1, buoy5: 2, buoy6: 3, buoy7: 1, ...}
out    value histogram: {1: 4, 2: 4, 3: 4}
cmd    each body's node list
out    hub1: 0 hub1_node, 1 buoy1_joint, 2 buoy2_joint, 3 buoy3_joint
out    hub2: 0 hub2_node, 1 buoy4_joint, 2 buoy5_joint, 3 buoy6_joint
rule   F3 section 3.2 item 6: "apply the twelve buoy-joint reactions as the loads at
       the cluster-arm tips"
judge  dict[str, int] with four different buoys mapped to node 1 in four different
       Model objects. A consumer cannot resolve the pair from the mapping, and the
       consumer is F4 applying the loads. CLAUDE.md section Non-negotiables: "a
       structure analysed under misinterpreted loads is the failure mode this whole
       project is built to prevent."
```

**Closed when** the mapping carries the body -- `dict[str, tuple[str, int]]`, or a keyed
pair, or the node ids made global -- so that a reaction cannot be applied to the wrong model
without a type error. One line and a docstring; it is listed as blocking because it is (a),
not because it is expensive.

## The rulings the invocation asked for

**1. THE SKELETON: DO THE MEMBERS PARTITION, HAS BUOY MASS CREPT IN, IS THE HUB ARM'S MARK
WHAT DJ1 REQUIRES? Yes, no, and yes. All three checked independently.**

```
cmd    the sixteen labels and the five bodies
out    platform 4 (platform:hubN_arm), hub1..4 3 each (hubN:buoyM_arm)
out    len(labels) == len(set(labels)) == 16; no member in two bodies
cmd    which deck bodies the builder reads
out    bodies["platform"] and bodies[hub] only; the twelve buoy entries are read for
       GEOMETRY and their mass and inertia are never touched
cmd    sed -n on docs/milestones/F1.md lines 385-392
out    :389  Cluster arm (hub->buoy) | 25 m span, 2.5 m x 180 mm tubular
out    :390  Platform cross-truss arm | 50 m span, triangulated, depth undecided
judge  F1 records no tubular section for the hub arm, so DJ1's "sized to reproduce its
       body's deck mass and marked preliminary" is the rule that applies, and the
       builder applies it: preliminary=True on all four hub arms, False on all twelve
       cluster arms, with the basis string naming F1.md:390. That is the requirement
       and not a convenience.
```

**What I will say beside that ruling, because the mark is doing more work than the tree
knows.** The sized tube stands in for a **triangulated truss**: a 2.5 m tube of equal mass
has an `EI` and an `Izz` about the platform centre that are properties of the substitution.
`HUB_ARM_OUTER_DIAMETER` is an assumed 2.5 m carried over from the cluster arm, and I
measured that moving it to 6.0 m leaves all 32 green while moving the platform arm's bending
stiffness by more than an order of magnitude. The mark is correct; nothing asserts it (no
test reads `BodyModel.preliminary`) and no output table exists yet to carry it. That is C35,
not blocking, because the requirement DV0 states lands on the member-force table.

**2. IS THE G3.1a NARROWING SOUND, OR A WEAKENING TO AVOID A RED?** Ruled in full inside
R592. The short form: **the reason is true, I verified it independently, and it is not a
weakening -- and it is incomplete, because the same assertion would be red for any deck
inertia on account of `platform.py:438-439`, and that half is a bug rather than a
placeholder.** Narrow it if you like; say both reasons.

**3. THE ZERO REMAINDER CARRYING ROTARY INERTIA: IS REPORTING ENOUGH, OR MUST IT REFUSE?
Reporting is enough for THAT, and it is not enough for what is beside it. Ruled.**

A zero-mass point with `5.208333e+09 kg.m^2` of `Izz` is representable in a mass matrix and
is not a point mass; the builder saying so, with the factor `deck_izz / member_izz` beside
it, is the right shape, and a refusal would be wrong -- it would refuse the model DJ1's own
sizing rule produces. **What is not enough is that the same construction moves the body's CoG
10.33 m and nothing reports THAT** (R591), and that the finding F3 section 3.3 does require
-- the negative remainder -- is emitted and asserted on by nothing (R590). So: keep
reporting, add the CoG consequence to what is reported, and assert the findings the plan
names.

**4. R486 ON REAL MEMBERS: IS THE MEASUREMENT RIGHT, AND IS MEASURING WITHOUT SHIPPING
ACCEPTABLE THIS ROUND? The measurement is right to the digit, and yes.**

```
cmd    element_rigid_residual(local_stiffness(section, S355, L), L) over all 16 shipped
       members, the rung-1 function called directly
out    16 members; worst 3.5283e-19 on hub2:buoy5_arm; RIGID_MODE_EXACTNESS 1e-15;
       headroom 2834.3x
out    four distinct values: 7.18521e-20, 9.67305e-20, 1.98839e-19, 3.528257e-19
judge  reproduced exactly, on my own harness, from the shipped members. Not taken from
       the report.
```

**Measuring here without shipping is acceptable and I am not holding on it:** F3's step 1 has
not opened, F3 section 5 is where the assertion and the three counters belong, and a number
measured and published is strictly better than a number not taken. **One thing about that
gate needs saying now rather than after it ships.** F3 section 5 says *"A platform frame is
mostly near-vertical members, so this gate is measured there first"* and DW1 measured every
one of the 16 members horizontal. **The near-vertical band R486 was found in cannot arise on
this frame at all**, so the F3 gate as locked is narrower than the sentence that motivates
it, and the honest form is that R486's original band is left uncovered by this model rather
than covered by it. C29.

**5. `tests/verification/rung3/test_platform_skeleton.py` AS THE GATE FOR EVERYTHING
DOWNSTREAM.** Read line by line. It defines no `pytest_` hook of any kind; its only pytest
surfaces are `@pytest.fixture(scope="module")` and `@pytest.mark.parametrize`, so none of
CH2's six forgery channels is present. Its structure is right -- parametrised per body,
deliberately no test that sums the five, `rigid_mass_matrix` reduced from the ASSEMBLED
matrix rather than trusted from a summary, which is the correct instinct and is what let me
measure R592. **Three of its five G3.1a assertions cannot fail** (mass, inertia, and the
planar check, whose nodes are all constructed from the same `z` literal), **one can and does**
(CoG, on a dropped member or a rotated tripod), **and the two refusal tests and the sizing
test are good**: I confirmed `L/D` and `L/r` redden either side of their boundaries and that
`size_to_mass` refuses rather than going solid.

## Closure items

None of these blocks. Fix the list once, in the closure commit, and do not re-review them
item by item (CZ0). **C17 is CLOSED at `f14fad2`** and I re-read the README bullet.
**C12, C14, C18 to C25 carry forward unchanged** -- nothing in this round touched any of
them, and `git diff 7bd86e8..6c09932 -- docs/verification/README.md` shows only C17's hunk.

* **C26. `floatfea/model/platform.py:66-73` is an orphan string literal.** The builder
  limits' docstring -- *"F3 section 2's builder limits, verbatim, and neither is a
  tolerance"* -- sits after `_NEGLIGIBLE_FRACTION`'s docstring and therefore attaches to
  nothing; the two constants it documents are eight lines above it. **Closed when** it sits
  under `MAX_LENGTH_OVER_GYRATION` where it belongs.
* **C27. `floatfea/model/platform.py:26-28` claims what another module asserts, with no
  triple.** *"test_platform_deck_export.py asserts the coplanarity, so if it ever stops
  being true this module's premise fails loudly."* True -- I checked -- and CW0 says a claim
  about this repository in a docstring is a test, a triple, or deleted. **Closed when** it
  carries `claim:`/`cmd:`/`out:` or names the test id and nothing more.
* **C28. `docs/reports/F2/step-7.md:1641-1643` reads "every F3 gate is measured green:
  G3.1a, G3.1b ..., G3.2, G3.3, and R486", and the 6-8 October date rests on that
  sentence.** G3.1a's inertia half is not asserted, its mass half cannot fail, and R486 is
  measured rather than asserted. **Closed when** the sentence says which gates are asserted,
  which are measured and which are narrowed -- the date may well survive it, and it should
  be computed from the honest list.
* **C29. `docs/milestones/F3.md:496-500` says a platform frame is mostly near-vertical
  members and that R486's gate is measured there first.** Every member of this frame is
  horizontal (DW1, `dz = 0.000e+00`). **Closed when** the paragraph records that the band is
  unreachable on this platform and therefore uncovered, rather than implying it is where the
  measurement starts.
* **C30. `docs/milestones/F3.md:183-184` says "If a joint turns out not to be a gimbal,
  F3's builder refuses the model rather than idealising it", and the builder never reads
  `joint["type"]`.** Measured: every joint type changed `yaw_locked` to `ball` in the deck
  the builder reads, `32 passed`. The property IS asserted, at
  `test_platform_deck_export.py:206` on the committed file, so nothing is unguarded -- the
  plan names the wrong mechanism. **Closed when** the plan names the assertion that exists,
  or the builder refuses.
* **C31. CI is configured never to run on a commit that changes only `docs/reports/`, and
  the guards that read a report are exactly what such a commit changes.**
  `.github/workflows/ci.yml`'s comment says "a report revision ... change[s] no code; the
  guards that read them run on the next code push and locally, every time" -- and this
  round's three CI reds were report-guard reds whose fix can never be confirmed by any push.
  **Closed when** the comment says that, or `docs/reports/**` leaves `paths-ignore`, or the
  convention becomes `gh workflow run CI --ref F3` after a report-only push. Apparatus, so a
  closure item; it is also why I could not corroborate my green.
* **C32. `floatfea/model/platform.py:315` sizes the four hub arms from `min()` over the four
  hub radii while each member's mass uses its own length.** Identical here (all four are
  exactly 50 m) and silently inconsistent on any deck where they are not: I measured
  `3 failed` when one arm is 40 m, so it is caught, but by the planar and CoG reads rather
  than by anything that knows the sizing basis moved. **Closed when** the sizing refuses
  unequal radii or sizes per member.
* **C33. `DX0`, `DX1`, `DX2` and `DX3` are directive ids nothing in the repository
  defines**, exactly C25's shape one letter later: `DX2` appears only in
  `docs/SUPERVISOR.md`'s two new headings and `DX3` only in a report sentence and a commit
  subject. **Closed with C25**, by transcribing the DW and DX directives into F3 section 0
  verbatim beside DJ and DV.
* **C34. The report's section 1 is four hand-written paragraphs where CZ0 allows one**, and
  the schedule paragraph is the first of them. **Closed when** section 1 is one paragraph
  carrying the date and whether it holds.
* **C35. Nothing asserts the `preliminary` mark.** `BodyModel.preliminary` returns the four
  hub arms and no test reads it; DV0 makes the mark a requirement on the member-force table.
  **Closed when** the table exists and carries it, or a test asserts the four-and-twelve
  split now.

## Tolerances touched

**One value added, outside `floatfea/tolerances.py`, and it is R593.**

```
cmd  git diff 7bd86e8..6c09932 -- floatfea/tolerances.py
out  (no output)
cmd  git diff 7bd86e8..6c09932 -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py            -- CI0: the pathspec resolves; the instruction holds
cmd  git diff 7bd86e8..6c09932 -- .github
out  (no output)
cmd  git diff 7bd86e8..6c09932 --name-status
out  12 files: SUPERVISOR.md, F2a, F3, the report and its answers json, the ladder
     README, floatfea/model/platform.py, the export script, two goldens, the carry
     guard, the rung-3 export module, and the new rung-3 skeleton module
```

**No conftest and no plugin was added or changed**, so CH2 has nothing new to read, and the
one existing conftest is byte-identical across the round. I read the new rung-3 module by
hand anyway, because its green is what I am relying on: no `pytest_` hook of any kind.

**The new module reads `ROUNDOFF_IDENTITY` at five sites** (`:105`, `:120`, `:140`, `:158`,
`:188`). Four are relative and dimensionless and that is the entry's declared form:
`|z - z_plane| / |z_plane|`, two `pytest.approx(rel=...)` on masses, and
`max|offset| / span`. **The fifth, `:188`, sits on an identity and is therefore not a
comparison at all** -- see R592. **Margins measured:** the planar read is `0.000e+00` against
`2.467e-13` and cannot fail as written; the mass reads are exact identities (R590); the CoG
read is the only one with a real margin and it is a good one -- `5.5879e-16` worst against
`5.0e-13` on the platform and `4.2201e-15` against `2.5e-13` on hub2, and a dropped member
puts it at `5.4127e+00`, which is `2.2e+13` times the threshold. **No tolerance value was
widened and none was moved.**

**`BODIES = 5` and `MEMBERS = 16`** are object counts and the `not-a-tolerance:` marker on
them is correct. **`_NEGLIGIBLE_FRACTION = 1e-12` is not**, and that is R593.

## What I built to break it

Everything ran from `/tmp`, outside the repository. Nothing was written into the tree except
this verdict and the corpus.

1. **The section sweep.** `CLUSTER_ARM_WALL` rebound to 0.090, 0.045, 0.001 and 0.400 m and
   the shipped module re-run at each: `32 passed` five times out of five, clean control
   first. **This is the adversarial case that passed when it should have failed**, and it is
   R590.
2. **A sixteen-mutation deck harness**, each mutation applied to a copy of the committed YAML
   and the shipped module run against it through a `-p` plugin that repoints `DECK_YAML`.
   Eight caught, five not, three refused. The two that matter are the platform reference
   point moved 65 m up and 50 m across, both `32 passed`.
3. **An independent inertia probe**: the members' `Ixx` about each deck reference point by
   20001-point quadrature along every member, against `remainder_inertia` and against the
   deck tensor. That is where 20.9% and 51.5% come from, and neither number is in the report.
4. **The R486 residual, recomputed** from `local_stiffness` and the rung-1 function over all
   16 members. `3.5283e-19`, `2834.3x`, four distinct values.
5. **The CoG reduction done twice**, once as the shipped gate does it (members about the body
   node) and once as G3.1a's row reads it (whole body against the deck reference), to be sure
   the gap was in the gate and not in my reading.
6. **FloatSim's own convention, read rather than assumed.**
   `../HSP-runs/floatsim/driver.py:207-209` and the `cog_offset_body=None` call beside it.
   This is the measurement that turned R591 from an ambiguity into a defect, and it took one
   grep.
7. **Six refusal cells**: a non-coplanar joint, a thirteenth cluster joint, a hub reference
   off the plane, `lambda` scaled by a thousand, and two hub-arm diameters that need a solid
   rod. All six refuse, loudly, with the reason in the message. **The builder's refusals are
   the best part of this commit** and I want that on the record beside the findings.

## Corpus this round (BE3)

**`tests/corpus/platform_skeleton_builder.txt`, batch 20, committed separately at `e5e2015`,
before this verdict.** Fifty-five entries, none seen by the implementer, in seven sections:
the section, the body mass, the CoG, the inertia tensor, geometry and topology, scale and
R486, and six questions.

**In scope under DE2** -- "from F3, the platform model" -- so it is not an apparatus corpus,
DR1 does not defer it to `docs/milestones/F2a.md`, and nothing is transcribed. It is a
separate file from batch 19 because batch 19 was written BEFORE the frame existed and asked
the plan questions; every entry in batch 20 is run against shipped code.

**THE COVERAGE MEASUREMENT: 31 of the 55 entries assert that a defect must be caught by
something shipped. 8 are caught. 23 are not.** Seven more are refusals and all seven are
measured REFUSED.

```
cmd  the eight caught
out  a dropped member; a 40 m arm among three 50 m arms; a 100-degree tripod;
     platform Izz halved, Izz x100, Ixx zeroed; a derived platform Izz; a derived hub Izz
judge every one of the eight is caught by the CoG symmetry read or by the lamina
     predicate. NOTHING in the shipped module catches a wrong SECTION, a wrong deck
     MASS, a moved deck CoG, an off-diagonal inertia, or the Izz double-count.
cmd  the module's own evidence for G3.1a
out  32 tests, one deck, one set of sections; no entry perturbs either
judge that is the shape BE3 exists for. The published figure "32 passed" is a statement
     about the input the gate's author designed.
```

**The 23 missed reduce to five shapes and four of them are this verdict's blocking
findings:** the mass identity (R590, 7 entries), the CoG blindness (R591, 4), the inertia
tensor (R592, 6), the epsilon (R593, 2), and the ambiguous node map (R595, 1). Three more are
C30, C32 and the un-asserted `preliminary` mark. **That the corpus and the findings agree
this closely is itself the measurement:** the shapes were found by perturbing inputs, not by
reading prose.

**The standing measurement.** `cmd grep -h "^id=" tests/corpus/*.txt | wc -l`; `out` 1308
entries across 21 files. The apparatus corpus's untranscribed count stays where DR1 put it
and is reported by the corpus-agreement test rather than written down here.

## My own instructions (4b)

```
cmd  git log --format="%h %s" 7bd86e8..6c09932 -- .claude docs/SUPERVISOR.md
out  de67ba5 process: report paths follow the plan; the verdict file accumulates (DX2)
cmd  git diff 7bd86e8..6c09932 -- .claude
out  (no output)
cmd  git diff 7bd86e8..6c09932 -- docs/SUPERVISOR.md | grep -c "^-[^-]"
out  0
cmd  git log --format="%h" 7bd86e8..6c09932 -- docs/reviews
out  (no output)
```

**One commit touched them, it is additive in every line, and it also touched `tests/`, which
is R594.** I read all 43 added lines: two new sections, on the `Answers:` sha and on the
verdict file accumulating, both of which record rulings I gave last round. Nothing was
removed, nothing was reworded, and no guard in that file is weaker than it was. **I read the
five commits' file lists individually rather than the aggregate:** `f14fad2` is the README,
the export script, the rung-3 export module, the carry guard and one golden; `8b14de3` is the
plan and the ledger; `de67ba5` is SUPERVISOR.md and the carry guard; `863c1aa` is
`floatfea/model/platform.py`, the new rung-3 module and one golden; `6c09932` is the report
and its answers json. **No commit touches both `floatfea/` (or `tests/`) and
`docs/reviews/`.**

**I have complied with both DU1 rules:** the judged commit is restated bolded and backticked
at the top, and every blocking finding heads `**R<n>. (<class>, blocking) ...**` with
`blocking` inside the parentheses, which is what `scripts/check_carried.py`'s `^\*\*(R\d+)\.`
and `test_report_carried.py`'s `_blocking()` both parse.

## The two mechanism questions, answered as asked

**ONE: DO I WRITE THE NEXT VERDICT INTO F3's TREE NOW, IN THE ROUND THE MARKER ADVANCES?
NO, AND THE ORDER IS FORCED RATHER THAN CHOSEN.**

```
cmd  sed -n on scripts/write_verdict.py lines 70-73
out  report = root / f"docs/reports/F{args.milestone}/step-{args.step}.md"
out  if not report.exists(): sys.exit(f"refused: no step report at {report}")
judge I CANNOT write docs/reviews/F3/step-1.md today: the tool refuses a step with no
      report, and there is no docs/reports/F3/step-1.md. So "the same round the marker
      advances" cannot be MY round -- it has to be the round after the implementer's.
```

**The sequence, stated so nobody has to guess.** (1) This round's blocking items are answered
and this step reaches PASS in `docs/reviews/F2/step-7.md`, where verdicts 70, 71 and 72
already live. (2) The implementer's next commit adds `docs/reports/F3/step-1.md` and moves
`<!-- step-under-execution: N -->` from `F2.md` to `F3.md` **in that one commit**, which is
what `tests/test_report_carried.py` already requires and what DX2's mechanism now makes
visible. (3) I am then invoked on F3 step 1 and `write_verdict.py --milestone 3 --step 1`
succeeds, because the report it refuses on exists. **The interim ruling from verdict 71 --
keep writing into step 7's files -- stands for exactly one more round and then retires.**

**TWO: `scripts/write_verdict.py` STILL OVERWRITES, AND I AM NOT CHANGING IT. This is the one
place I disagree with a directive rather than with the work, and it leaves the loop.** DX2
says the mechanical cause "is the reviewer's tool to change". My own instructions name **two**
writable paths -- `docs/reviews/` and `tests/corpus/` -- and say that every harness I build
goes under `/tmp`, "never the repository root". `scripts/` is not one of the two, and a
reviewer that edits the generator of its own verdicts is the hazard `CLAUDE.md` records two
sections earlier. **So I have satisfied DX2 by construction instead: this round is written
above verdict 71's, which is preserved verbatim below, by feeding the accumulated body through
the unchanged tool.** That works and it will keep working. The durable fix is one line in
`write_verdict.py` and it needs either a directive that adds that path to my write set, or one
implementer `process:` commit that touches nothing else. **Choose either; I am not asking for
a ruling and this does not become another round.**

## On the criterion

**CZ0 held and I did not have to stretch it this time.** Five of six findings are literally
(a), (b) or (c), and the sixth is the process class `CLAUDE.md` names itself; eleven closure
items are listed and none consumed a paragraph of argument. **What is worth saying is where
the round's value came from.** Verdict 71 spent itself on a meta-test floor, a plan
contradiction, a preflight flag and two docstrings -- all correct, all closed, none of them
about the platform. This round every blocking finding is about the platform, and four of six
came from changing one number in a shipped constant and re-running a shipped test. **That is
the cheapest review this milestone has had and the first one where the apparatus was not the
subject.** I record it because DR1's bet -- freeze the apparatus, spend the rounds on physics
-- just paid, measurably.

**The escalation condition fires for the fourth consecutive round and the choice has not
changed.** F3's computed date of 6-8 October is not credible while G3.1a does not assert the
sizing, because the repair is `_finish` plus one gate rewrite and then the gate has to be
re-measured against the deck -- call it one round, not one day. **13 October still holds** and
I would not cut scope for this. What I will not do is let the schedule paragraph rest on
"every F3 gate is measured green" (C28).

## Carried for the next step

Nothing carries yet -- **this is a HOLD, not a close.** R590 to R595 are answered before
anything else. **The next verdict on this step is the third and it closes the step (CZ0)**, so
any of these still open then carries into F3 step 1's `Carried` section by name and blocks
there.

## Next step opens when

**Seven things, and the code is four sites in two files.**

1. **R590: G3.1a's mass half compares something the deck constrains**, and the two docstring
   sentences that say it already does are corrected in the same commit (BP0). The
   negative-remainder finding gets an assertion, the way the lamina finding has one.
2. **R591: the platform body's CoG.** Either the model puts it where the deck declares it, or
   a `plan:` commit records that DJ1's sizing rule and G3.1a's CoG row cannot both hold for
   this body and which gives. **Either way the gate compares the WHOLE body's CoG, all three
   components, against the deck.**
3. **R592: `_finish` subtracts the members' full inertia tensor about the attachment point,
   from the same source the gate reads**, so the split is exact by construction; the inertia
   test asserts against the DECK's tensor rather than against its own sum; the lamina
   narrowing is kept and restated with BOTH of its reasons; `F3.md:465`'s row moves in a
   `plan:` commit in the same round.
4. **R593: `_NEGLIGIBLE_FRACTION`'s `:468` use** becomes an exact comparison or an entry in
   `floatfea/tolerances.py` with form, counter and justification. The `:61-65` docstring stops
   saying the finding it gates is not a pass or a fail.
5. **R595: `buoy_joint_nodes` carries its body.** One line and a docstring.
6. **R594: one note in the closure artifact**, and the convention restated: a commit that
   touches `docs/SUPERVISOR.md` or `.claude/` touches nothing else, ever, even when the
   directive asks for a guard edit in the same breath. **C26 to C35 plus C12, C14 and C18 to
   C25 land in one closure commit** and are not re-reviewed individually.
7. **CI.** A push that changes only `docs/reports/` triggers nothing (C31), so after the
   answering push **run `gh workflow run CI --ref F3` and wait for it to complete** before
   asking for the verdict. A run that has not finished is not a pass, and this round I had no
   second machine at all.


---

# PREVIOUS ROUND, PRESERVED VERBATIM (DX2)

## Round of 2026-09-28 -- SEVENTY-FIRST verdict on F2/F3, judged commit `4708cc2`

Verdict: HOLD

**Reviewed commit: `4708cc2`.**
Tests: 2768 passed, 8 failed, 0 skipped   (my own run at `4708cc2`, `python -m pytest -q`, 591.03s)

**SEVENTY-FIRST verdict on F2/F3, and the FIRST of the new step. The count starts at one;
verdict 70 spent step 7's cap and closed it, and step 7 stays closed (DD1).** This verdict
is about the tree and about a plan, exactly as 70 was, and it is written into step 7's file
because that is the only report file every guard can see -- the reason is in R590 below and
the ruling is mine to give, not the implementer's.

**WHY HOLD AND NOT PASS.** All four carried items are genuinely answered and I re-measured
every one of them myself rather than reading the report -- DW1's six geometry figures
reproduce to the digit, the twelve-mutation ablation reproduces exactly, `--check` passes on
my reading of the tree. That is the best round of work this milestone has produced on the
platform. **But CI at `4708cc2` has conclusion `failure` and my own run is 8 red.** CA2 says
a red CI is a HOLD regardless of what a local run says, CZ0(d) says a red test at the
reviewed commit blocks, and verdict 70's own closing condition 4 pre-declared this exact
outcome as (d). The cause is one arbitrary floor in one meta-test and the fix is a deletion I
rule for below. Do not read this HOLD as a judgement on the work; read it as the one line in
the ladder that cannot be waived.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 4708cc2 --json name,conclusion,status,workflowName
out  []       -- the --commit filter still returns nothing while a run is in flight
cmd  gh run list --limit 6 --json headSha,databaseId,status,conclusion,event
out  36523001390  4708cc2  push  in_progress   -- the run EXISTS at the judged commit
cmd  gh run view 36523001390 --json status,conclusion   (polled to completion, 14 polls)
out  completed  FAILURE
cmd  gh run view 36523001390 --json jobs
out  the verification ladder            success  13 steps
     lint, unit and guards              FAILURE  14 steps  -- step "guards and meta-tests"
     CI determinism -- leg              skipped, 0 steps
     CI determinism -- ten legs agree   skipped, 0 steps
cmd  gh run view 36523001390 --log | grep run_rung
out  rung1 1276 / rung2 66 / rung3 164 / rung6 134 / rung4 127 collected, 0 failed,
     0 errored, 0 skipped in every rung; rung5 0 directories
cmd  gh run view 36523001390 --log-failed | grep -E "FAILED|failed,"
out  8 failed, 913 passed, 1 warning in 570.41s
     FAILED tests/test_report_carried.py::test_the_parse_found_something_to_check
     FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[7 states]
```

**THE LADDER IS GREEN AND THAT IS WHY THIS IS A HOLD AND NOT A STOP.** Every rung collected
and none failed, at the judged commit, on a machine neither of us controls. rung3 collected
164 including the rewritten G3.2 module. Nothing about the platform, the element or the deck
is red anywhere.

**CK2 DOES NOT APPLY AND I CHECKED RATHER THAN ASSUMED.** The failing job ran 14 steps for
ten minutes; it is a real failure, not an unstarted job. The two determinism jobs are
`skipped` with zero steps -- neither red nor green, and not CK2's allowance state either,
since every other job in the run executed and there is no billing annotation. Recorded as
unavailable on this run. The last run that executed them is `36455024518` at `2dc6a99`, and
`git diff 2dc6a99..HEAD -- .github` is empty, so nothing about the determinism configuration
has moved since.

**My own run agrees with CI on both the count and the names**, which is worth saying because
it is the first time this round that the two machines have been compared on a red rather than
on a green: 8 failed, 2768 passed at `4708cc2`, same eight test ids.

## Carried

Verdict 70 carried three blocking items -- R582, R583, R584 -- and closure items C10 to C16.
**The report's header is `Answers: verdict 70 @ 1b895db`, which names the LATEST verdict, so
instruction 1b is satisfied and I am not holding on it (see the ruling on C13 below).**
`python scripts/check_carried.py --verdict docs/reviews/F2/step-7.md --report
docs/reports/F2/step-7.md` prints `all 4 findings carried`, exit 0.

**I re-measured all four rather than reading the report on them. Every one is answered.**

* **R582 -- ANSWERED at `63046e5`, a standalone `plan:` commit, and DW1's condition holds on
  my own measurement.** I resolved every joint attach point through its body reference from
  the exported deck and got the plan's figures to the digit:

```
cmd    joint attach points resolved through each body reference, lambda = 50
out    16 of 16 joints: |a - b| = 0.000e+00; z spread max - min = 0.0 exactly
out    joint plane z = 0.4933695679797303 model = 24.668478398986515 m full = 24.6685
out    platform reference z = 0.7 model = 35.0 m full, 10.331521601013483 m above = 10.3315
out    hub1..4 reference z minus joint z = 0.0 exactly, all four
out    centre -> hub node: 50.000000 m full, dz 0.000e+00, on all four
out    hub node -> buoy joint: 25.000000 m full, dz 0.000e+00, on all twelve
out    platform MASS reference -> hub1 joint: 51.0562 m, 11.6747 deg
rule   a planar frame requires ONE joint elevation exactly, not approximately
judge  the frame IS planar at joint elevation, the 51.056 m inclined vector IS the
       platform end alone, and the hubs DO need no rigid link. All three of the
       implementer's readings are correct and I did not take any of them on trust.
```

  **And the two findings beyond the ruling are both correct.** Each hub carries exactly three
  cluster arms with angular gaps of `120.0, 120.0, 120.0` degrees on all four hubs -- four
  tripods, twelve cluster arms. `L/r` is `60.774830` and `30.387415`, so `60.77` and `30.39`
  as printed; the `60.78` is gone. Each buoy reference is `84.45185` m below its joint point,
  so the F2a return condition's `84.45 m` is right.

* **R583 -- ANSWERED at `b5602d6`, and the published ablation reproduces EXACTLY.** This is
  the invocation's question 1 and it deserves the detail.

```
cell   ONE VARIABLE: remove the CONTENT and BYTE digest gates from the check list,
       run the module's own twelve mutations through the SHIPPED functions
out    2 of 12 missed: every_mass_times_ten, re_emitted_with_sort_keys_True
judge  exactly the published figure, reproduced independently on my own harness.
       The counter is measuring those gates and not a copy of them. R583 is closed.
cell   the same twelve with ALL of the shipped checks
out    0 of 12 missed -- every one of the eleven the old gate missed now reddens
cell   the same twelve with all THREE digests removed, which the report does not run
out    3 of 12 missed -- two_bodies_swapped_in_order joins them
```

  **Then I ran thirty-three mutations the twelve-entry table does not contain, and that is
  where the coverage number moves.** Two are caught by nothing shipped -- see R589 and C18 --
  and the ablation goes from 2 of 12 to **17 of 33**. Both numbers are correct. One of them is
  about the gate and the other is about the table.

* **R584 -- ANSWERED at `b5602d6`, and I ran the procedure myself on a second reading of the
  tree rather than accepting a pasted output.**

```
cmd    python scripts/export_platform_deck.py --check
out    HSP floatfea-ref-1 @ 25de7ce / bodies 17 joints 16 /
       round trip: re-validated dump equals the source dump (9 top-level keys) /
       tests/goldens/platform_deck_digest.txt matches the deck /
       data/platform/platform12_deck.yaml matches the deck, HEADER INCLUDED   exit 0
cmd    git -C ../HSP-runs describe --tags --always ; rev-parse --short HEAD ;
       status --porcelain --untracked-files=no
out    floatfea-ref-1 / 25de7ce / (empty)
judge  both halves of R584 landed. The preflight refuses a dirty worktree at :89-97, and
       `comparable()` at :227-228 now excludes only `#   exported` by name rather than
       slicing the whole header. The committed YAML and the committed digest both
       reproduce a deck built from HSP at the pin, today, here. That is the strongest
       statement available about this file and it holds.
```

* **C10 / R585 -- ANSWERED at `475c224`**, and the fix is the one-line `is_dir()` branch the
  technical supervisor directed. The commit cites the direction and touches nothing else in
  the harness; the diff is 16 lines of which 12 are the reason. **It is a guard repair where
  DR1 permits only deletion, and it stands only on that direction** -- I record that rather
  than ruling it a STOP-class process breach, because the direction is named in the commit
  message and the change is confined to `tests/`. C11 is closed too, in passing: the
  `BODIES * 6 - JOINTS * JOINT_ROWS == 38` line is gone from the module.

* **R567 -- CARRIED, and the implementer is right about the mechanism.** See the ruling below.
  I have recorded the withdrawal in this verdict so the guard can do its job.

## Withdrawn in earlier rounds, recorded here so the record survives the round

**This file is OVERWRITTEN each round** -- `scripts/write_verdict.py:78` is
`out.write_text(header + body)`, not an append -- so it holds one round and every earlier
verdict exists only in git history. `test_no_status_claims_more_than_the_verdict_allows`
states its premise on its face as "the WHOLE review file, every round of it, because a
withdrawal ruled two verdicts ago is still a withdrawal", and that premise is false of a file
I replace. The implementer measured it: `83c7ba5` 397 lines / R567 x3, `4314118` 508 / x2,
`4ff1008` 508 / x2, `1b895db` 538 / **x0**. I reproduced the line counts.

**The guard is right about the rule and the defect is in MY output, not in the guard.** I am
not asking for the guard to change and the implementer was right not to touch it. The fix is
one standing section in the file I write, and this is it:

* **R567 -- WITHDRAWN by verdict 69.** Its site, the `two_digit_step_number` guard state, was
  deleted under DT2, which was one of the two DR1-compliant moves verdict 68 itself named.
  `docs/milestones/F2a.md:228` records the same withdrawal.

**A report may now write `withdrawn` for R567 without the guard reddening, and reporting
`carried` -- which is what revision 5 did -- remains correct and weaker.** This section will
be carried forward in every verdict from here.

## Findings

**R586. (d, blocking) Eight tests are red at the judged commit and CI at the judged commit
has conclusion `failure`. `tests/test_report_carried.py:454`.**

One cause, and the implementer named it correctly before I got here. I am ruling it rather
than leaving it open a second round.

```
cmd    python -m pytest -q          (mine, at 4708cc2)
out    8 failed, 2768 passed, 0 skipped in 591.03s
cmd    gh run view 36523001390 --json conclusion     (the push run AT 4708cc2)
out    failure -- job "lint, unit and guards", step "guards and meta-tests", 8 failed
rule   `assert len(EXPECTED) >= 5` -- a FLOOR on how many findings a verdict must carry
out    AssertionError: only ['R582','R583','R584','R585'] expected; assert 4 >= 5
judge  the parse did not fail. It found all four findings verdict 70 wrote, and four is
       the true count. Seven of the eight reds are guard states whose nested run includes
       this test, so eight reds are one assertion.
```

**AND IT WILL STILL BE RED AFTER THIS VERDICT, WHICH IS WHAT DECIDES IT. I MEASURED THAT
RATHER THAN ASSUMING EITHER WAY.**

```
cmd    EXPECTED, recomputed against THIS verdict as `test_report_carried.py:270-273`
       computes it -- findings, union the R-numbers in the LAST `Carried` heading
out    ['R586', 'R587', 'R588', 'R589']   -- 4, so `assert 4 >= 5` again
judge  the last heading matching "Carried" in this file is `## Carried for the next
       step`, which names no item because this is a HOLD. There is no state of this
       verdict that satisfies the floor except padding it with findings I do not have.
```

R546 is the same shape and it is already on the record: *no satisfiable state at a milestone
close*. A guard that reddens because I wrote four findings and would green because I wrote six
is measuring the reviewer's verbosity. It has never measured a parse failure: the two assertions above it, `_FINDING.findall(VERDICT_TEXT)` non-empty and
`CARRIED.strip()` non-empty, are what stop a parse failure reading as a clean bill, and those
two are correct and must stay.

**Closed when** the single statement `assert len(EXPECTED) >= 5, (...)` at
`tests/test_report_carried.py:454-457` is **deleted**, with the reason recorded at the site
-- that a verdict is permitted to carry fewer than five findings, and that verdict 70 carried
four correctly. **This is a DELETION under DR1 and not a repair: do not replace the floor with
a smaller floor, and do not parametrise it.** The two assertions above it stay untouched. Then
CI at the answering commit is green. Nothing else in this HOLD depends on anything but that.

**R587. (plan, blocking) The re-locked plan says both that the twelve buoy bodies are in the
model and that they are out, and the difference is 85.6% of the deck mass.
`docs/milestones/F3.md:302` against `:323-324`.**

This is the invocation's question 4, and the answer is that scope was not widened -- it was
reduced, and the reduction is under-determined at the one number that decides what the first
result means.

```
claim  the plan says the remainder mass of EVERY body is attached
cmd    sed -n '302p;310,313p' docs/milestones/F3.md
out    :302  5. **attach each body's remainder mass by rigid link** (DW2, section 3.3)
out    :311  * **Remainder:** each body's remaining mass -- deck mass minus member mass
              -- goes on a lumped mass at the deck's reference point
claim  and the plan says the first result contains five of the seventeen bodies
cmd    sed -n '323,324p' docs/milestones/F3.md
out    The first result is **the platform body and the 4 hub bodies, 16 members.** The 12
       buoy spar columns are **deferred until after the member-force table**
cmd    the exported deck, body masses summed by class
out    12 buoys 344.04 kg model / 4 hubs 48.00 / platform 10.00 / total 402.04
rule   G3.1a asserts FE body mass, CoG and inertia against the deck PER BODY
judge  under one reading the model carries 402.04 kg and twelve 84.45 m rigid links nobody
       has mentioned; under the other it carries 58.00 kg, which is 14.4% of the deck, and
       G3.1a passes on 5 of 17 bodies while 85.6% of the mass is absent. The plan's
       executable list says the first; its scope section says the second.
```

**AND THE TWO READINGS GIVE MEMBER FORCES THAT DIFFER BY ORDERS OF MAGNITUDE IN THE ONE
MEMBER WHOSE SECTION IS A RECORDED NUMBER.** `docs/milestones/F3.md:101` sources the 25 m
cluster arm's `2.5 m x 180 mm` wall from `docs/milestones/F1.md:425-433`, where the demand is
`5.93 MN` at the rod tip over 25 m, `M = 148.2 MN.m`. If the buoy body is out, that tip
carries nothing but the arm's own steel, and the member-force table for the only member in the
model with a designed section is computed without the load that designed it. A utilisation
computed that way is not conservative and not unconservative -- it is about a different
structure.

**And a third thing follows from whichever reading is taken.** Sixteen members, four hub arms
and twelve cluster arms, with nothing joining adjacent hubs or adjacent buoy joints: in plan
the frame is a **tree**, four tripods on four radial spokes. Every joint plane member is
horizontal, z spread `0.000e+00` m, so a vertical load at a buoy joint has **no axial path at
all** and is carried entirely by bending and torsion of the cluster and hub arms. That may be
the right model. It is not a conclusion the plan states, and DW5 is written from this list.

**Closed when** section 3.2 item 5 and section 3.4 agree, in words, on whether the twelve buoy
bodies' mass and inertia are in the first result; if they are, the twelve `84.4519 m` rigid
links are named beside the platform's `10.3315 m` and the hubs' zero-length one; if they are
not, section 3.4 says so in those terms and G3.1a's row says which bodies it covers. A `plan:`
commit; DK0 applies and it buys no fresh three.

**R588. (c, blocking) The preflight that makes G3.2's "at the pin" true ignores untracked
files, and the comment beside it asserts that untracked files cannot matter.
`scripts/export_platform_deck.py:89` and `:95-96`, against `:103-104`.**

R584's first half landed and the tracked-file gap is closed. This is the residue, and it is a
finding because the code chose the narrower refusal and wrote a reason for the choice that one
reading refutes.

```
claim  untracked files cannot change what the study imports
cmd    the sentence at :95-96 -- "Untracked files are ignored -- they cannot change
       what the study imports."
cmd    the three lines at :103-104 --
         for path in (HSP_RUNS, STUDY, STUDY.parent / "cluster-3buoy-rigid"):
             sys.path.insert(0, str(path))
cmd    grep -nE "^(import|from) " ../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py
out    :62  import cluster_common as cc
out    :63  import platform_common as pc
judge  both are BARE-NAME imports resolved off sys.path, and `insert(0, ...)` in a loop
       puts `cluster-3buoy-rigid` FIRST. An untracked `platform_common.py` dropped into
       that directory is imported in preference to the tracked one in
       `platform-12buoy`, and `git status --porcelain --untracked-files=no` reports
       nothing. The preflight passes, the header names the pin, and the deck is built
       from a file no commit contains -- which is the exact outcome the docstring at
       :62-64 says the pin exists to prevent.
rule   "a model exported today and a model exported next month are the same model"
```

**This is (c) and not prose because the flag IS the threshold.** `--untracked-files=no` versus
`all` is a decision about *which files a gate requires to match HEAD*, and `docs/verification/
README.md:97` makes this script half of G3.2. The false sentence is what makes it a finding
rather than an acceptable narrowing: a reader of the site is told the gap does not exist.

**Closed when** either the preflight refuses untracked files in the three directories it puts
on `sys.path` -- `--untracked-files=all` restricted to those paths, or a check that no
untracked `.py` exists in them -- **or** the sentence at `:95-96` is deleted and replaced by
the residual stated as a residual, in which case the gate's claim shrinks to match what it
checks. Either direction closes it; I am describing the predicate, not writing it.

**R589. (c, blocking) The digest that now carries G3.2 is named for the file's bytes and is not
over the file's bytes, and a line-ending rewrite passes all nine checks.
`tests/verification/rung3/test_platform_deck_export.py:221-247` and `:80`.**

This is the invocation's question 1, second half, and it is the one adversarial case that
passed when it should have failed.

```
cell   ONE VARIABLE: the committed YAML rewritten with CRLF, nothing else changed
out    all nine shipped checks GREEN -- CONTENT, ORDER, HEADER, FINITE, TOPOLOGY,
       AXIAL, COPLANAR, BYTE and REEMIT
cmd    the reader at :80 -- `DECK_YAML.read_text(encoding="utf-8")`
judge  `Path.read_text` opens in text mode with `newline=None`, so universal-newline
       translation turns every CRLF into LF before the hash sees it. The digest is over
       the newline-normalised decoded body, not over the bytes.
rule   the docstring at :221 -- "The file as emitted, hashed" -- and the failure message
       at :242-246 -- "the deck YAML's BYTES do not match the recorded digest"
```

**I am NOT asking for the behaviour to change and I want that on the record**, because the
normalisation is what makes the gate portable: with `core.autocrlf` on Windows the same commit
checks out with different bytes on two machines, and a true byte digest would redden in CI or
here depending on nobody's decision. The quantity it compares is the right quantity.

**What blocks is that the gate's own statement of which quantity it compares is wrong, and
that statement is now the only one there is.** `docs/verification/README.md` does not mention
the digests at all (C17), so these two sentences are the whole published description of what
G3.2 asserts, and they describe a stricter gate than the one that runs. Under CZ0 this is (c)
-- "what a gate claims, on which quantity" -- by the same reading my own instructions name: a
docstring that is the only statement of what a gate measures is the gate's assertion.

**Closed when** `:221` and `:242-246` say what is hashed -- the newline-normalised document
body as decoded, header excluded -- and say why, in one sentence, so a later reader does not
reach for `read_bytes()` and make the gate environment-dependent. One docstring and one
message. No behaviour change, no new apparatus.

## The rulings the invocation asked for

**IS A COMMITTED DIGEST A LEGITIMATE GATE, OR A GOLDEN THAT WILL SIMPLY BE REGENERATED?
It is a legitimate gate for exactly one property, and the property is the one DJ1 asked for.
Ruled, not left standing.**

The digest cannot detect a deck that changed *because HSP changed*: `main()` writes
`platform12_deck.yaml` and `platform_deck_digest.txt` in one invocation, so one re-run moves
both and the module goes green again. What it CAN detect, without a second repository and
therefore in CI, is that the committed file was written by something other than the generator
-- a hand edit, a merge resolution, an editor reformat, a partial revert. That is precisely
*"no coordinate is typed into this repository"*, and before this commit nothing in the tree
checked it at all.

**The defence against regenerate-to-match is the `git diff` and the reviewer, not a test, and
that is what a golden IS under `CLAUDE.md` § Testing.** It is the same boundary CJ0 draws for
conftest forgery: a gate that reads a record cannot outrank code that writes the record. The
digest docstring at `scripts/export_platform_deck.py:160-162` says this in the right words and
points at the rule. **So the split is coherent and I am ruling it sound:** the digest gates the
file against the tree, `--check` gates the tree against HSP, and neither pretends to be the
other. The residual I will name once: **a commit that moves the digest and the YAML together is
the one thing in this arrangement that only a reader can catch**, and it should be read as
carefully as a `tolerances.py` diff. That is not a new guard; it is a line in my own reading
list and I am putting it there.

**WHAT ELSE I WENT LOOKING FOR AND DID NOT FIND: A FOURTH GAP IN `--check`.** Three candidate
holes, measured:

```
cell   the header rewritten with `bodies 99` / `joints 99`
out    the suite half reddens (HEADER); `--check` reddens on the comparable lines. FIXED.
cell   a tracked file in ../HSP-runs modified while the worktree sits at the pin
out    the preflight refuses with the diff printed. FIXED.
cell   an untracked module on the import path
out    NOT refused -- that is R588, and it is the only one of the three still open.
cell   a line beginning `#   exported` carrying arbitrary text
out    invisible to `--check` (filtered by `comparable`) AND to the header test.
       A blind channel, recorded as C21 rather than blocking: nothing reads that line
       and the model cannot be changed through it.
judge  the fourth gap you asked about is R588. The `exported` channel is a fifth and it
       is cosmetic. I found no path by which a WRONG MODEL reaches the file with
       `--check` green on a clean pinned worktree.
```

**THE `Answers:` SHA NAMES THE COMMIT THE VERDICT TEXT IS FINAL AT, NOT THE COMMIT JUDGED.
Ruled, and C13 is closed by this ruling.** `VERDICT_TEXT = _verdict_text_at(ANSWERED)` reads
the verdict file *at that commit*, and this file is overwritten each round, so naming the
judged commit makes every generator read the PREVIOUS round's verdict. That cost three rebuilds
and it will cost three more every time. **My last two hand-backs proposed the judged commit and
they were wrong.** The convention from here: `Answers: verdict <n> @ <the commit that verdict
was committed at>`, and the judged commit is stated in prose in the report's own §1. This
verdict's closing instructions say it as a command.

**THE THIRD PASTED UNRUN NUMBER -- RECORDED, NOT A FINDING, AND THE PROCEDURAL CHANGE IS THE
FIRST ONE THAT IS A PROCEDURE.** `902301b` (three counts), `b958083` (one), `b5602d6` (108
where it is 107). All three amended before pushing; nothing in the tree reads a commit message,
so no guard could have caught any of them and none reached a reader. **What is different this
time is that the fix is not a resolution.** The lint line is now produced by capturing the
command's output into the message text, which removes the hand from the loop instead of asking
it to be more careful -- and the `L/r = 60.78` slip in the plan was fixed by computing the
table in place rather than by re-typing it. That is the right shape and it is the first time in
three occurrences that the answer has been mechanical. I verified the number it lands on:
`L/r` is `60.774830`, so `60.77`.

**`measure_platform_joints.py` and `export_platform_deck.py` are still not apparatus under the
freeze**, unchanged from verdict 70's ruling. Nothing was added to either class this round.

## Closure items

None of these blocks. Fix the list once, in the closure commit, and do not re-review them
item by item (CZ0). **C10, C11, C13, C15 and C16 from verdict 70 are closed** -- C10 at
`475c224`, C11 by the rewrite, C13 by the ruling above, C15 and C16 by the plan rewrite at
`63046e5`, both of which I re-measured. **C12 and C14 are still open and carry forward.**

* **C17. `docs/verification/README.md:93-96` still describes the RETIRED assertion as gate
  G3.2's always-run half, and does not mention the digests at all.** It reads "*asserts,
  everywhere and always, that the committed file round-trips through a parse-and-re-emit
  cycle*" -- which is the assertion R583 ruled vacuous, which no longer carries the gate id,
  and which is now named `test_the_file_PARSES_and_re_emits_stably`. `git diff 1b895db..HEAD --
  docs/verification/README.md` is empty. This is BP0 exactly: the decision rule moved and the
  document citing it did not move in the same commit. **It is the first item on this list and
  it is the one I would fix first**, because the ladder document is where a reader who is not
  the author goes to find out what G3.2 claims. **Closed when** the bullet names the three
  digest lines and the four structural assertions, and the parse-and-re-emit sentence is gone
  or is labelled as the assertion that does not carry the gate.
* **C18. `tests/verification/rung3/test_platform_deck_export.py:320-322` says the twelve
  mutations are "the reviewer's eleven, plus the coplanarity case".** They are eight of the
  eleven plus four new ones. Absent: every body z negated, a buoy moved onto the diagonal, a
  duplicated `name` key. I measured all three and all three are caught by the digests, so the
  table is weaker than it says and the gate is not. **Closed when** the docstring counts what
  is there, or the three are added.
* **C19. `tests/test_report_guard_states.py:507-510` asserts "CI is unaffected ... guards were
  1000 passed at the reviewed commit", with no triple, and it is already stale.** At `4708cc2`
  the same job is 8 failed / 913 passed. CW0: a claim about this repository written in a
  comment is a test, a triple, or deleted. **Closed when** the sentence states the mechanism
  (`actions/checkout` produces a directory) without the count, or carries the count as a
  triple that something regenerates.
* **C20. The header's `source` line is unguarded by the always-run half of G3.2.** Measured:
  `platform_rao_pilot.py` changed to `other_thing.py`, all nine checks green. `--check` does
  compare it, so R584's condition is met and this is the residue. **Closed when** the header
  test asserts the source line, or the docstring's "declares its provenance" is narrowed to
  the four things it actually reads.
* **C21. Any line beginning `#   exported` is invisible to both halves of G3.2.**
  `scripts/export_platform_deck.py:227-228` filters the prefix from both sides, and the header
  test does not read it. Arbitrary text can live there. **Closed when** the filter matches the
  generated line's full shape rather than its prefix, or the blind channel is named at the site.
* **C22. Revision 5 carries no `--check` triple, and the README says the procedure's output
  goes in the step report.** The cells are in the commit message at `b5602d6` instead. **I ran
  it myself and it passes -- the output is in the Carried section above -- so nothing about the
  deck is in doubt; what is missing is the record at the commit.** Closed when the report
  carries the `--check` output at its own commit, per `docs/verification/README.md:97-99`.
* **C23. The report's own suite figure does not describe the commit it is published at.**
  §5 reads "*Whole suite at `475c224`: 2573 passed, 2 failed*" plus 10 in the excluded set; at
  `4708cc2` my run is 2768 passed / 8 failed and neither of the two vocabulary-corpus reds it
  names still exists. The measurement is structurally taken one commit early because the report
  is inside what it measures, which is a known seam -- but the line as written asserts a state
  the judged tree is not in. **Closed when** the line names the commit it was taken at *and*
  says that the report commit that follows it may move the count, or the figure moves to the
  closure artifact.
* **C24. Revision 5 has a duplicated heading and a duplicated clause.** `## 0. CI, for the
  commit under review` immediately above `## 0. CI at 2e24459 ...`, and "*The escalation was
  answered by scope, not by slipping the date — and the escalation was answered by scope, not
  by slipping the date (DW0)*". Generator seams, not content. **Closed when** each appears once.
* **C25. `DW0`, `DW4` and `DW5` are directive ids that nothing in the repository defines.**
  `grep -rn "DW5" docs/` is empty; `DW0` appears only as a parenthesis on `docs/milestones/
  F3.md:321` and a row in `F2a.md:229`; `DW4` appears nowhere. DW5 is described to me as "the
  whole of" the next work and the plan's §3.2 list is what it will be written from. **Closed
  when** the DW directives are transcribed into F3 §0 beside DJ and DV, verbatim, in the way
  DV0-DV2 already are -- a plan whose executable list cites an id no reader can look up is the
  condition R576 and R582 were both about.
* **C12 (carried).** `floatfea/io/froude.py::_refuse_uncovered` refuses a genuinely scalar 2-D
  array of trailing width 4, 5 or 6; the docstring documents the 1-D residual and not this.
* **C14 (carried).** `docs/reports/F2/step-7.md:1087` still says F3 closes 10 October, in
  revision 4's paragraph; the plan has said 13 October since `772f01e`. Revisions are
  append-only, so BP0's "regenerated or withdrawn in the same commit" needs the withdrawal
  written in place.

## Tolerances touched

**None.**

```
cmd  git diff 1b895db..HEAD -- floatfea/tolerances.py
out  (no output)
cmd  git diff 1b895db..HEAD -- floatfea
out  (no output)   -- nothing under floatfea/ moved at all this round
cmd  git diff 1b895db..HEAD -- tests/conftest.py "tests/**/conftest.py"
out  (no output)
cmd  git ls-files -- tests/conftest.py "tests/**/conftest.py"
out  tests/conftest.py        -- CI0: the pathspec resolves; the instruction is not broken
cmd  git diff 1b895db..HEAD -- .github
out  (no output)
cmd  git diff 1b895db..HEAD --name-status
out  10 files: the plan, F2a, the report and its answers json, the deck YAML (one date
     line), the export script, two goldens, the guard-state harness, the rung-3 module
```

**No conftest and no plugin was added or changed, so CH2's reading has nothing new to read**,
and the one existing conftest is byte-identical across this round. I checked the rung-3 module
for the six forgery channels by hand anyway, because it is the module whose green I am relying
on: it defines no `pytest_` hook of any kind, and its only pytest surface is one
`@pytest.mark.parametrize` and one `importorskip`.

**The rung-3 module reads `ROUNDOFF_IDENTITY` at FOUR sites now (`:268`, `:275`, `:291`,
`:296`), two more than last round.** All four are relative and dimensionless --
`min(|x|,|y|)/radius`, `(max-min)/max` over the four arm radii, `dist(a,b)/max(1,|a|)` on the
joint coincidence, and `(max z - min z)/max|z|` on the joint plane -- which is the entry's
declared form. **I measured the margin on the two new ones:** every joint gap is `0.000e+00`
against a threshold of `1e-14`, and the defect it exists to catch, a 1 mm offset at model
scale, reads `1e-3` relative -- `1e11` times the threshold. The `z`-spread assertion is the
one to watch: it is `(max - min) <= ROUNDOFF_IDENTITY * max|z|`, measured `0.000e+00` against
`4.934e-15`, and **its counter-case is an assertion-domain hole rather than a margin** -- see
the `named` rows in the corpus, where a uniformly lifted plane is coplanar and invisible to it.
No value was added, none was changed, nothing was widened.

**`tests/goldens/platform_deck_digest.txt` is new and it is a golden, not a tolerance.** Three
hashes, two counts, two order strings; no threshold, exact comparison. It is the right shape
for what it is and the ruling above says why.

## What I built to break it

Everything ran from the session scratch directory outside the repository. Nothing was written
into the tree except this verdict and the corpus.

1. **An independent geometry probe over the exported deck**, resolving all 16 joint attach
   points through both bodies. It reproduced every one of DW1's six figures to the digit, plus
   the 120-degree tripod, the `84.45185` m buoy offset, and the `51.0562 m / 11.6747 deg`
   platform-reference vector. This is the measurement DW1 made the plan conditional on and I
   did not take it from the report.
2. **Thirty-three mutations of the committed YAML against the SHIPPED check functions**, called
   directly with `DECK_YAML` repointed, which is the same mechanism the module's own counter
   uses. **Two are caught by nothing: a CRLF rewrite (R589) and a falsified `source` header line
   (C20).** A clean-file control ran first and all nine checks passed on it, so the harness can
   tell green from red.
3. **The published ablation, reproduced, and then run three more ways.** 2 of 12 with
   CONTENT+BYTE removed -- exactly the figure. 3 of 12 with all three digests removed. 17 of 33
   and 20 of 33 on the unseen set. 6 of 33 with only the digests, all six header edits.
4. **`--check` on my own reading of the tree**, with `../HSP-runs` at `floatfea-ref-1` @
   `25de7ce` and `git status --porcelain --untracked-files=no` empty. Exit 0, header included.
5. **The untracked-shadow reading on the preflight** (R588), traced through
   `sys.path.insert(0, ...)` and the study's two bare-name imports. I did not write into
   `../HSP-runs` to demonstrate it; the mechanism is the two lines and the two imports.
6. **The CI run at the judged commit, polled to completion**, which is what turned a PASS into
   a HOLD. Fourteen polls over seven minutes.

**The adversarial case that passed when it should have failed is the CRLF rewrite** -- all nine
checks green on a file whose every line ending changed -- and the reason it is R589 rather than
a demand to change the behaviour is that the normalisation is correct and only the words are
wrong. **The finding that outranks everything in the report is R587**, which is not adversarial
at all: I added the body masses up.

## Corpus this round (BE3)

**`tests/corpus/platform_model_skeleton.txt`, batch 19, committed separately at `02407b5`,
before this verdict.** Fifty-five entries, none seen by the implementer, in four sections: the
twenty-nine mutations the module's twelve-entry table does not contain, the ablation run four
ways, the model F3 section 3 now describes, and the generator after R584.

**In scope under DE2** -- "from F3 -- the platform model" -- so it is not an apparatus corpus,
DR1 does not defer it to `docs/milestones/F2a.md`, and nothing is transcribed. It is a separate
file from batch 18 because batch 18 is about the committed FILE and this is about the MODEL.

**THE COVERAGE MEASUREMENT: 33 of the 55 entries assert that a defect must be caught by
something shipped. 26 are caught. 7 are not.** That number replaces the module's own, and the
comparison is the point of the round:

```
cmd  the module's own twelve, all shipped checks
out  0 of 12 missed
cmd  thirty-three mutations the module's table does not contain, all shipped checks
out  2 missed -- CRLF line endings, and a falsified `source` header line
cmd  the same thirty-three with the CONTENT and BYTE digests ablated
out  17 of 33 missed, against 2 of 12 on the author's own table
judge  the gate is much stronger than it was and the PUBLISHED COVERAGE FIGURE IS STILL A
       PROPERTY OF THE TWELVE-ENTRY TABLE. Nothing is wrong with the ablation; it is that
       "exactly two" is a statement about what twelve mutations happen to contain.
```

**The seven missed, named, because a count without its members is not a measurement:** the CRLF
rewrite (R589); the falsified `source` line (C20); a uniformly lifted joint plane, invisible to
every *named* assertion because the coplanarity test asserts a spread and not a datum; an
untracked module on the study's import path (R588); the `#   exported` blind channel (C21); the
absence of a `--check` record at the judged commit (C22); and the README still describing the
retired gate (C17).

**Thirteen entries are questions rather than mutations** (`expect=explain`) and they are the
half I would read first, because the frame has not been built: whether the buoy mass is in the
model, what is at the tip of a twelve-cantilever tripod, whether the one designed section in the
model is loaded by what designed it, the three rigid-link lengths, and the fact that a planar
frame gives a vertical load at a buoy joint no axial path at all. **Two of them became R587.**

**The standing measurement.** `cmd grep -h "^id=" tests/corpus/*.txt | wc -l`; `out` 1253
entries across 20 files. Of the apparatus corpus, the untranscribed count stays where DR1 put
it and is reported by the corpus-agreement test rather than written down here.

## My own instructions (4b)

```
cmd  git diff 1b895db..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git log --format="%h %s" 1b895db..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git log --format="%h" 1b895db..HEAD -- docs/reviews
out  (no output)
```

**Nothing touched them this round, and no commit in this round touches both `floatfea/` (or
`tests/`) and `docs/reviews/`.** I read the four commits' file lists individually rather than
taking the aggregate: `63046e5` is plan and ledger only, `b5602d6` is the script, the module and
two goldens, `475c224` is the harness alone, `4708cc2` is the report and the deck's date line.
**I have complied with both DU1 rules:** the judged commit is restated bolded and backticked at
the top, and every blocking finding heads `**R<n>. (<class>, blocking) ...**` with the status
inside the parentheses, which is the shape `scripts/check_carried.py`'s `^\*\*(R\d+)\.` and
`test_report_carried.py`'s `_blocking()` both parse.

## On the criterion, and two things that leave the loop

**CZ0 is right and it paid again.** Nine closure items from verdict 70 landed in one commit, five
of them are closed, and the round went to the deck, the gate and the plan. Three of my four
findings are one deletion, one plan paragraph and two docstrings between them.

**WHERE I AM STRETCHING CZ0, SAID ONCE AND NOT ARGUED.** R587 is a plan finding and R582 was.
Neither is literally one of (a)-(d). I am classing it `(plan, blocking)` on verdict 70's
precedent and for its reason: a plan that says two different things about 85.6% of the model's
mass makes DW5's first instruction ambiguous, and DW5 is the whole of the next work. **I am not
asking for a ruling and this does not become another round.** If the technical supervisor
prefers it as a closure item, say so and it becomes one.

**TWO THINGS THAT GO TO XABIER THROUGH THE IMPLEMENTER, not into another round.**

**One: F3's step reports have nowhere to go that any guard can see, and the interim answer is
ugly.** `tests/test_report_carried.py:67-68` hardcodes `docs/reviews/F2` and
`docs/reports/F2`; `scripts/write_verdict.py` refuses a step with no report under the milestone
it is given; `docs/milestones/F2.md:10` carries the only `step-under-execution` marker. **Nothing
goes RED when F3 opens -- the guards simply go on reading F2 step 7 forever, which is the
assertion-domain failure in its purest form: green while checking nothing.** DR1 permits only
deletion, and R564 already named this exact shape as one of the four findings the carry rule
produced against itself. **My interim ruling, so the implementer is not blocked: keep writing
into `docs/reports/F2/step-7.md` and `docs/reviews/F2/step-7.md` as revisions, exactly as
revisions 5 and verdicts 54, 55, 70 and this one do, with DD1 as the precedent.** It is wrong and
it works. The durable choice -- re-point two path constants, or delete the carry apparatus and
let `tests/test_collected_set_golden.py` carry what remains -- is above me and above the
implementer, and I would take the deletion.

**Two: the escalation condition fired again and the answer has already been given once.** DW0
answered the last one by reducing scope and holding 13 October, and the reduction is real work.
This round ends carrying blocking items for the third consecutive time. **I am not asking for
another scope cut** -- the remaining three items are a deletion, a plan paragraph and two
docstrings, and none of them costs a day. What I will say plainly is that **nothing has yet
touched the platform MODEL.** The deck is exported, measured and gated; that is the input. The
frame, the sections, the rigid links and G3.1a are all still ahead of 13 October, and R587 is
the reason the first line of that work cannot be written today.

## Carried for the next step

Nothing carries yet -- **this is a HOLD, not a close.** The four findings above are answered
before anything else and the step does not advance. If a third verdict on this step arrives with
any of them open, they carry by name then.

## Next step opens when

**This step stays open. Four things, and three of them are small.**

1. **R586: delete `assert len(EXPECTED) >= 5, (...)` at `tests/test_report_carried.py:454-457`**,
   with the reason at the site -- a verdict may carry fewer than five findings and verdict 70
   carried four correctly. A DELETION under DR1: no smaller floor, no parametrisation. The two
   assertions above it stay. **Then CI at the answering commit is green**, and 8 failed / 913
   passed becomes 0. Anything less than green CI at the answering commit is (d) again.
2. **R587: one `plan:` commit** making section 3.2 item 5 and section 3.4 agree on whether the
   twelve buoy bodies' mass is in the first result, and naming the rigid-link lengths that
   follow. DK0 applies: it buys no fresh three.
3. **R588 and R589: one predicate and two docstrings.** R588 either refuses untracked files on
   the three `sys.path` directories or deletes the sentence that says they cannot matter. R589
   says what the digest hashes. Neither needs new apparatus and neither changes behaviour.
4. **C17 to C25 plus C12 and C14 land in one closure commit** and are not re-reviewed
   individually. C17 first: the ladder document still describes G3.2 as the assertion R583
   retired.
5. **The next report's header is `Answers: verdict 71 @ <the commit THIS verdict is committed
   at>`** -- not `4708cc2`, not `02407b5`. The generators read `VERDICT_TEXT` at the commit the
   header names and this file is overwritten each round, so naming the judged commit makes every
   generator read verdict 70. That is C13's ruling and this is it as a command. State the judged
   commit in the report's own prose instead.
6. **Push, wait for the run to complete, then ask for the verdict.** The run at `4708cc2` was
   `in_progress` when this review began and it is the reason this is a HOLD rather than a PASS
   written on a local green. A run that has not finished is not a pass.
