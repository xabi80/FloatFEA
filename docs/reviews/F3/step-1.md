# Review — F3 step 1
Reviewed commit: 008a8e98dd787e5ea4e1bca57dfbee8322655ce6
Verdict: HOLD
Tests: 2739 passed, 37 failed, 0 skipped   (my own run at `228bdfb`, `python -m pytest -q`, 1224.18s, one invocation, no split)

## Round of 2026-09-30 -- SEVENTY-FOURTH verdict, and the FIRST on F3 step 1

**Reviewed commit: `228bdfb`.**

**This is verdict 1 of 3 on this step.** The count restarted here, as verdict 73 said it
would.

**WHAT THE ROUND GOT RIGHT, AND IT IS MOST OF IT.** Eleven standalone commits, one path
class each. R596 is answered and answered well: the analytic path is real, it is
independent of the assembled matrix in the way it claims, and I broke it four different
ways to check. R598 is answered, its figure is re-measured rather than transcribed, and
the implementer was right to publish the number measured here instead of the one the
directive predicted -- I say so below because it asked. R599 is answered exactly as
ruled: deleted, not renamed. DZ5 is the best thing in the diff; its arithmetic
reproduces to the digit, including the hub figures nobody predicted. C34, C35, C38, C39,
C41 and C42 are closed and C42 is closed well enough that this verdict was written
through the repaired tool.

**AND THE ONE THING THAT IS NOT.** R597's repair has the same defect R596's repair had,
in the same shape: the new gate's reference is built from the thing it is checking. The
report says the endpoint-pair set is compared against the deck's joint coordinates. It
is compared against the built model. Every coordinate in the frame is compared only with
itself, and I have eight measured cells saying so.

## CI, for the commit under review (CA2)

```
cmd  gh run list --commit 228bdfb --json name,conclusion,workflowName
out  []  -- the commit touches only docs/, which ci.yml path-ignores
cmd  gh run view 36743819045 (workflow_dispatch AT 228bdfb, dispatched by the implementer)
out  headSha 228bdfb76e7944fe5d59603d043dc41109331280; status completed; conclusion FAILURE
out  the verification ladder            SUCCESS   (rungs 1, 2, 3, 6, 4, 5 all green)
out  CI determinism -- ten legs agree   SUCCESS   (all ten legs green)
out  lint, unit and guards              FAILURE   -- 37 failed, 835 passed in 581.86s
out  actionlint, ruff, black, mypy and the unit step all SUCCESS; the failure is
     entirely in the `guards and meta-tests` step
cmd  python -m pytest -q   (mine, at 228bdfb, one invocation)
out  37 failed, 2739 passed, 2 warnings in 1224.18s
judge RED. My run and CI agree on the failure set EXACTLY -- the same 37 names, 17 in
      tests/test_report_carried.py and all 24 parametrisations of
      test_the_guard_survives_the_state. Not `unavailable` and not `allowance
      exhausted`: every job started, every job ran, and one of them failed.
```

**The ladder being green on a machine neither of us controls is the thing that matters
most here**, and it is green: rung 3 -- the rung this whole step is about -- passes on
CI at the judged commit. The red is in the report-carry apparatus, which is why R601
below separates its two causes rather than calling it one boundary artifact.

## Carried

Verdict 73 carried four blocking items -- R596, R597, R598 and R599 -- and closure items
C12, C14, C18 to C32 and C33 to C42. **The report's header reads `Answers: verdict 73 @
52de940`, which is my own verdict commit and the latest verdict** (instruction 1b and
DX2's third ruling: satisfied, one comparison, and it is the right one).

**I re-measured all four rather than reading the report.** Every cell below is mine, run
in a `git worktree` at `228bdfb` outside this repository, restored between mutations.

* **R596 -- ANSWERED for the inertia half. Closed, with one piece of reach recorded
  below as C46.**

```
rule   (A) analytic == assembled at MASS_PROPERTY_AGREEMENT * M_b * l_b^2, per body
cmd    beam.py `rho_ip_l = rho * (I_y + I_z) * ll` scaled by 2.0
out    10 failed -- (A) and (B) on all five bodies. Platform absolute residual
       4.960883e-09 -> 4.230312e+05 kg.m^2, which is 1.5225e-18 -> 1.2983e-04 relative.
       The report's own figures reproduce to five digits.
cmd    bending_mass called with 2.0 * rho * I in BOTH planes
out    10 failed
cmd    rho_a_l = 1.1 * rho * A * ll   (the translational block)
out    16 failed
judge  THE MUTATION THAT USED TO PASS 43 TESTS NOW REDDENS TEN. The old comparison was
       `deck == deck`; this one is a hand-computed rod-plus-section inertia against the
       assembled matrix, and the remainder is read off the lumped input rather than
       recomputed, so a defect in the element no longer cancels. This is the finding
       answered, not moved.
rule   the residuals are round-off and not cancellation, which is the OTHER half of R596
cmd    the raw residuals at 228bdfb, unmutated
out    platform (A) inertia 4.960883e-09 absolute on a 6.250000e+09 tensor
out    hub1-4   (A) inertia 5.96e-08 to 1.19e-07 absolute on 3.125000e+08
out    numpy.spacing(9.375e8) = 1.192093e-07
judge  these ARE round-off -- one ULP of the scale, where R596's `3.375e-36` was
       nineteen orders below one ULP. The signature is gone because the arithmetic
       changed, not because the print changed.
```

* **R597 -- NOT ANSWERED. Renumbered R600 and it blocks.** The new gate is real work and
  it catches two things it did not catch before (a duplicate line, and a chain instead
  of a star). It does not catch the cell R597 named, and it does not compare anything
  with the deck. See R600.

* **R598 -- ANSWERED at `1078698`. Closed, and I checked every number rather than the
  prose.**

```
cmd    git grep -n "MISPLACED_remainder"
out    (no output) -- the phantom is gone from the tree
cmd    the worst residual re-measured at 228bdfb over BOTH comparisons, five bodies,
       mass normalised by M_b, CoG by l_b, inertia by M_b l_b^2
out    platform  (A) mass 0.000e+00  CoG 3.648e-18  inertia 1.522e-18
out    hub1      (A) mass 0.000e+00  CoG 1.421e-16  inertia 6.358e-17
out    hub2      (A) mass 1.5522e-16 CoG 1.421e-16  inertia 1.272e-16
out    hub3/hub4 the same to within one ULP
out    WORST = 1.5522e-16, at hub2's MASS; 1e-13 / 1.5522e-16 = 644.1x
judge  the published `1.5522e-16` and `~644` are both correct at this commit. The
       claim that the old `2.2119e-15` came from dividing a CoG offset by 1.0 m
       instead of by l_b also holds: 2.2119e-15 / 1.9073e-16 is about 11.6, and
       11.6 is the ratio verdict 73 measured for the same figure.
```

  **AND ON THE DISAGREEMENT WITH THE DIRECTIVE'S FIGURE, WHICH THE INVOCATION ASKED ME
  TO RULE ON: publishing the figure measured here was RIGHT, and transcribing
  `1.9073e-16` would have been the defect.** BP0 is explicit -- when a decision rule
  changes, every figure citing the old rule is regenerated or withdrawn in the same
  commit. The rule changed twice over: the quantity moved from `assembled vs deck` to
  `analytic vs assembled and analytic vs deck`, and the normalisation moved from 1.0 m
  to `l_b`. `1.9073e-16` was measured against the pre-DZ1 gate and describes a
  comparison that no longer exists. Carrying it forward would have been exactly the
  species BP0 was written for, and the entry says which figure was measured where. Good.

* **R599 -- ANSWERED at `de6b1e0`. Closed as ruled, and I read the hunk line by line.**
  The `named` tuple and its assertion at `:713-743` are deleted, `assert code != 0` is
  kept, `_assert_diagnosis` is kept, neither state was deleted, `DIAGNOSIS` was not
  extended, and no name was added. The reason is recorded at the site naming R599 and
  DR1, including the R516 false-green direction. **Its closing condition also said
  `python -m pytest -q` reports `0 failed`, and that is not met -- for a reason that is
  not R599's and that R601 carries.**

## Findings

**R600. (c, blocking) DZ2's geometry gate builds its expected endpoint-pair set from the
BUILT MODEL, not from the deck, so the comparison is an identity. The whole frame can be
rotated, scaled, transposed, or have its member labels permuted onto each other's joint
points, and all 48 tests pass. R597 is not answered, and its named site is untouched.
`tests/verification/rung3/test_platform_skeleton.py:326-343`, `:374-377`, and
`floatfea/model/platform.py:551-553`.**

The mechanism first, because it is three lines and it decides the finding.

```
rule   tests/verification/rung3/test_platform_skeleton.py:327-333 -- "The undirected
       endpoint pairs this body must have, from the DECK's joints. Built from the deck's
       own joint coordinates and the body's centre node, so it is independent of what
       the builder actually made."
cmd    read :341-343
out    centre = body.model.nodes[body.centre_node].xyz
out    tips   = [body.model.nodes[m.node_b].xyz for m in body.members]
out    return {frozenset({cell(centre), cell(tip)}) for tip in tips}
judge  every one of those is the BUILT model. The function takes `superstructure` as its
       first argument and never reads it. So the assertion at :374 is
       {(node_a, node_b)} == {(centre, node_b)} over the same member list -- which is
       true iff every member's node_a is the centre, and that is asserted again three
       lines below at :381. The set comparison adds nothing the star check does not
       already do, and it adds no deck.
cmd    git grep -n "platform12_deck\|DECK_YAML\|_full_scale_deck" on the test module
out    one hit, at :29, inside the module docstring
judge  the module does not read the deck at all.
```

**EIGHT CELLS, ONE VARIABLE EACH, ALL AT `228bdfb`, baseline `48 passed`.**

```
cell   every member end point +3 m in x, in `_member_geometry` BEFORE `math.dist`, so
       lengths and first moments follow -- R597's own cell, made self-consistent
out    48 passed. Widened to tests/verification/rung3: 213 passed.
cell   the platform's plan centre moved from (0,0,z) to (3,0,z) -- four hub arms at
       53 m and 47 m instead of 50 m
out    48 passed
cell   every in-plane coordinate scaled by 1.02 -- what a typed nominal radius instead
       of the deck's joint point looks like, which is the case DJ1's "no coordinate is
       typed into this repository" exists for
out    48 passed
cell   the four platform arm labels reversed against their tips, so `platform:hub1_arm`
       ends at hub4's joint
out    48 passed
cell   inside each hub, every cluster-arm label rotated onto the NEXT buoy's joint, so
       `hub2:buoy4_arm` ends at buoy5's point
out    48 passed -- and `buoy_joint_nodes` is keyed off exactly those labels, so F4
       would apply each buoy's reaction at its neighbour's node
cell   the whole frame rotated 30 degrees about z
out    DZ2 GREEN on all five bodies. 4 failed, and all four are
       `test_the_chosen_FRACTION_is_asserted_not_inferred`, because the f ladder
       descended to 0.1 on the hubs. The only detector of a rotated frame reports it as
       a SIZING FINDING and its message says "update it with the reason."
cell   x and y transposed on every node
out    DZ2 GREEN. 4 failed, the same f-ladder test, at f = 0.
cell   CONTROL -- the last member of each body re-pointed onto the first member's line,
       count and labels preserved
out    5 failed, one per body, on the DUPLICATE-PAIR assertion
cell   CONTROL -- member i starts at member i-1's tip: a chain, not a star
out    5 failed
judge  the duplicate check and the star check are real and I am not asking for them
       back. What is absent is any comparison against the deck, and six of the eight
       cells above are exactly the defect DJ1's rule and `platform.py:551-553` claim
       cannot happen.
```

**AND THE REPORT'S OWN CELL (ii) DOES NOT MEASURE WHAT IT SAYS IT MEASURES.** This is
the part I would most want read, because the figure in it is correct.

```
rule   docs/reports/F3/step-1.md section 3, cell (ii): "a member TIP moved +3 m -> DZ2
       reddens ... out 20 failed, 28 passed"
cmd    the same edit, `b = node((end[0] + 3.0, end[1], end[2]), f"{label}_tip")`
out    20 failed, 28 passed -- the published count reproduces EXACTLY
out    the 20 are MASS x5, (A) x5, (B) x5 and MEMBER_ONLY_fraction x5.
       `test_DZ2_the_bodys_MEMBER_GEOMETRY_is_what_the_deck_implies` is NOT one of them.
judge  the edit sits AFTER `length = math.dist(start, end)`, so it leaves `member.length`
       saying 50 m while the coordinates say 53 m. What reddens is the mass gate reacting
       to a member whose length disagrees with its own end points -- a real detection, and
       a different one. Move the same 3 m one function earlier, where everything stays
       self-consistent, and the count is 48 passed. The number was right and the sentence
       attached to it was not, which is BG0 in its usual form.
```

**Why this is (c) and not a closure item.** CZ0's third head is *what a gate claims, on
which quantity, at what threshold*. DZ2 is a new gate assertion, introduced this step,
whose claimed quantity -- agreement with the deck's joint points -- is not the quantity
compared. And its threshold is `MASS_PROPERTY_AGREEMENT * l_b` used as a coordinate
ROUNDING GRID, which the invocation asked me to size: **the grid cannot reject round-off
and cannot admit a real displacement, because both sides of the comparison read the same
float and round identically. Its size is currently unobservable.** That is not a
criticism of the number chosen; it is that no number is being tested.

**Why this is not a STOP.** The builder is not wrong. The frame it produces is, as far
as I can measure, correct -- I read the deck's hub points and the built nodes side by
side and they agree. What is wrong is that nothing in the tree says so, and DJ1's rule
is the one the plan leans on hardest. That is repairable inside the step.

**Closed when ALL THREE, site by site per CLAUDE.md:**
1. `expected_pairs` reads the DECK's joint points -- `build_superstructure` already has
   `joints` in scope and the test module can call `_full_scale_deck` the same way the
   builder does; the unused `superstructure` argument is where it was meant to come from.
2. The cell "every member tip +3 m, applied before `math.dist`" reddens it, and the
   report publishes that cell in place of cell (ii). Cell (ii) is withdrawn or
   re-labelled as what it measures -- `member.length` against the coordinates -- per BP0.
3. `floatfea/model/platform.py:551-553` -- "Every coordinate comes from the deck's own
   joint points. Nothing is typed, and no nominal radius is used" -- is either backed by
   that assertion or deleted (CW0). Verdict 73 asked for this site and it was not
   touched. **And the docstring at `:327-333` and the message at `:375` stop saying
   "deck" until they mean it.**

**R601. (d, blocking) CI is RED at the reviewed commit -- `37 failed, 835 passed` in
`lint, unit and guards` -- and it has TWO causes, only one of which is the step
boundary. `tests/test_report_guard_states.py:42` is the other, and it FAILS FALSE.**

```
cmd  gh run view 36743819045 --log-failed, failure names grouped
out  24 of 37: every parametrisation of test_the_guard_survives_the_state
out  13 of 37: tests/test_report_carried.py
cmd  the same, locally at 228bdfb
out  the same 37 names
```

**Cause (a), and it is the one that is not the boundary.**

```
rule   tests/test_report_guard_states.py:42 -- `_PLAN = ROOT / "docs" / "milestones" /
       "F2.md"`, with `_STEP_LINE` requiring `<!-- step-under-execution: (\d+) -->`
cmd    the marker as this step leaves it in F2.md
out    <!-- step-under-execution: moved to F3 at step 1 (DY8c) -->
judge  no digits, so the regex misses, `_step()` returns 0, `REPORT_NAME` becomes
       `step-0.md`, and `_build` raises
       `FileNotFoundError: docs/reports/F2/step-0.md` before a single state is planted.
       All 24 parametrisations die in the harness, including `baseline`.
judge  THE HARNESS IS REPORTING THE STATE OF ITS OWN INPUTS, which is the exact thing
       its own assertion at :296 refuses to let the nested run do. This is a guard
       failing FALSE, and DR1's permitted repair is DELETION, or the one-file
       `process:` re-point that C40 already names as its return condition.
```

**AND MY OWN RULING ON C40 IS WITHDRAWN.** Verdict 73 wrote, of these three guards:
*"The guard does not fail false -- it passes, and what it checks ... is real."* That was
true when I wrote it and it was true of the wrong event: the guard passes while the
marker sits on F2 and fails false the moment the marker moves, which is the single event
C40 was ledgered for. I ruled "leave it" on a guard whose only failure mode was the
transition I knew was next. Recorded here rather than softened, because the pattern --
three guards hardcoded to a closed milestone -- is the thing I said should go to Xabier,
and this is the measurement that says why.

**Cause (b), which IS the boundary.** The 13 `test_report_carried.py` reds are
`docs/reviews/F3/` being empty: `REVIEWED = _steps(REVIEWS)` is the empty set, `VERDICT`
resolves to a file that does not exist, and the parse yields
`test_the_report_carries_the_finding[(no finding parsed from the verdict)]`. The
implementer states this on the report's face and the forced order is real -- the tool
refuses a step with no report, so the report must land first. **It is not fully cured by
this verdict either:** `_verdict_text_at("52de940")` finds no F3 verdict at that sha and
falls back to the working copy, so once this file exists the guard will compare the
report against *this* verdict, which the report predates. That is BU1's boundary
reopened by the milestone change, and it closes at revision 2.

**Closed when** `python -m pytest -q` and a `workflow_dispatch` run at the commit the
next verdict judges both report `0 failed`. Cause (b) closes by revision 2 of the report
with its generated sections. Cause (a) needs a decision, and the two DR1-compliant ones
are: delete the states the hardcoded `_PLAN` breaks, with the reason at the site; or one
standalone `process:` commit re-pointing `tests/test_report_guard_states.py:42` and
`tests/test_plan_matches_tolerances.py:34` at the plan carrying the marker, citing C40.
**I am not choosing between them -- that is a directive, not a review finding.** What I
am ruling is that "leave it" is no longer available, because it is red.

## The four rulings the invocation asked for

**1. Is the analytic path independent, or has the vacuity moved a second time? IT IS
INDEPENDENT, and the answer is stronger than the report claims.** Three element
mutations redden it (torsion x2, bending x2, axial x1.1) and so does a wrong equivalent
density. It is blind to exactly one class, and the class is named correctly in its own
docstring: anything the remainder absorbs. What the report does not say, and what I
measured, is that comparison (B) covers precisely that class -- see ruling 2.

There is one thing it is blind to that nobody has named:

```
cell   ONE VARIABLE: `rigid_properties`'s translation-rotation coupling block negated
       after the projection -- the sign of every CoG this function reports, inverted
out    48 passed
judge  R596's fourth mutation, and it still passes. The reason is domain blindness, not
       reach: the full-body CoG offset is IDENTICALLY ZERO on all five bodies, so there
       is nothing for a sign error to show against. R596's sentence -- "a comparison
       whose expected value is exactly zero has nothing for a sign error to show
       against" -- survives DZ1 unchanged for the CoG half. This is not a blocking
       finding, because (B) demonstrably reddens on a DISPLACED remainder (below) and
       the model contains no body with a nonzero offset to measure a sign on. It is
       C46, and the honest form of it is a sentence saying so at the site.
```

**2. Is asserting (B) honest, or a second circular assertion wearing a label? HONEST,
and I can prove it with a cell the report does not carry.**

```
cell   remainder_inertia += 1e7 * I, AFTER the deficit is computed
out    5 failed -- ALL FIVE ARE (B). (A) is GREEN on every body.
cell   remainder_point += [0, 0, 5], after the placement rule
out    6 failed -- five (B), plus the first-moment placement test. (A) GREEN.
cell   remainder_mass = 1.05 * (1 - f) * deck_mass
out    10 failed -- MASS x5 and (B) x5
judge  (A) and (B) are COMPLEMENTARY, not redundant. (A) sees the element, the section
       and the assembly and is blind to the remainder; (B) sees the remainder and is
       blind to nothing the construction closes. The report's own defence of (B) -- "the
       placement rule could be wrong and this is where that shows" -- is correct and
       understated. Assert it. The sentence to change is "largely closed by
       construction", which is true of the inertia identity and false of the three cells
       above.
```

**3. DZ2's grid. It cannot admit a real displacement or reject round-off, and the reason
is not its size.** Both sides of the comparison read the same `float` out of the same
`Node`, so `cell()` maps them to the same tuple for any grid whatever. Set the grid to
1e-30 m or to 1 m and the assertion still passes on every frame the builder can build.
The grid is only a threshold once there is a second, independently obtained coordinate
to compare with, and there is none. **So I am NOT asking for the grid to change: I am
saying it is untested, and it becomes testable the moment R600 is closed.** At that
point `1e-13 * 51.056 m = 5.1e-12 m` against coordinates that are exact decimals in the
deck and pass through one Froude scaling is a reasonable size, and the number to publish
beside it is the worst |built - deck| over the 16 members.

**4. DZ5's arithmetic. It reproduces exactly, including the hubs.**

```
cmd    eigenvalues of J_G and of J_r per body, triangle slack = w0 + w1 - w2
out    platform  deck [3.125e+09 3.125e+09 6.250e+09]  slack +0.0000e+00
out    platform  J_r  [2.7305e+09 2.7305e+09 5.7287e+09]  slack -2.6770e+08  min +2.73e+09
out    hub1..4   deck [1.5625e+08 1.5625e+08 3.1250e+08]  slack +0.0000e+00
out    hub1..4   J_r  [7.7364e+07 7.7364e+07 1.5574e+08]  slack -1.0153e+06  min +7.74e+07
out    k_z = sqrt(6.25e9 / 1.25e6) = 70.711 m; extent 51.056 m; arms 50 m
judge  every published figure holds, PSD holds on all five, and the hub figure the
       directive did not predict is -1.0153e+06 on each of the four, identical to five
       digits. The label and the assumptions block are the right response and I am not
       asking for a model change.
```

## The measurement DZ5 is missing, and it changes what the finding means (BG0)

DZ5 states the violation and attributes nothing. One loop over the ladder isolates it,
one variable moved and everything else held:

```
cell   the J_r triangle slack recomputed at every f in MASS_FRACTION_LADDER
out    platform  f=0.5 -2.6770e+08   f=0.4 -1.7858e+08   f=0.3 -1.1487e+08
out    platform  f=0.2 -6.7051e+07   f=0.1 -2.9819e+07   f=0.0 +0.0000e+00 EXACTLY
out    hub1      f=0.5 -1.0153e+06   f=0.4 -8.1222e+05   f=0.3 -6.0917e+05
out    hub1      f=0.2 -4.0611e+05   f=0.1 -2.0306e+05   f=0.0 +0.0000e+00 EXACTLY
out    `admissible(body)` is True at every f, for every body
judge  THE SPLIT DOES NOT CREATE THE VIOLATION, IT INHERITS IT. The deck's own J_G sits
       exactly ON the lamina boundary, so subtracting any planar member set drives the
       remainder off it, and the slack is linear in f with a single zero at f = 0 --
       where the members carry no mass at all. **No admissible f removes it.** That
       turns "the deck is physically inconsistent and Xabier decides on FloatSim" into a
       decision with two options rather than a sensitivity to explore, and it is worth
       the four lines it costs.
judge  AND DY0d's admissibility test is PSD, not realisability. It passes a remainder
       whose minimum eigenvalue is +2.7305e+09 and which is not the inertia tensor of
       any real mass distribution. That is representable in a mass matrix and the solve
       is well posed, so it is not a defect -- but the plan's word for it is
       "admissible", and a reader will take that to mean more than PSD.
```

This is a closure item, not a block: it does not change a member force and it does not
move a gate. It is written here because the four numbers are cheap and the conclusion
they support is the one Xabier needs.

## Closure items

Named, with the file and what would close each. **Fixed once, in this step's closure
commit, and not re-reviewed item by item.** C12, C14, C18 to C32 and the unclosed part
of C33 to C42 carry forward except where noted.

**CLOSED THIS ROUND, verified rather than accepted:** C34 and C35 (the dead
`_NEGLIGIBLE_FRACTION` and the docstring it orphaned -- both gone, and the builder-limit
string now attaches to `MAX_LENGTH_OVER_GYRATION`); C36 and C37 (corrected in the
report's section 8); C38 and C39 (`buoy_rows` selected by name with an `assert len ==
12`, and the weight read from the deck and `GRAVITY_MAGNITUDE`); C41 (the module
docstring and the plan row now state what G3.1a is FOR); C42 (the `latin-1` fallback at
`scripts/write_verdict.py:103` -- this verdict was written through it).

**C40 is REOPENED and it is now R601(a).** My ruling that it does not fail false is
withdrawn.

**C43. C33 recurs inside its own repair.** `docs/reports/F3/step-1.md` section 8 says
"the line in section 10 is taken at this report's own commit"; section 10 says `Whole
suite at 9cba81c`. The report's commit is `228bdfb`. The one change between the two is
the marker move, which is what turns `0 failed` into `37 failed` -- so the published
figure is not merely early, it is the opposite of the tree under review. Section 10's
last paragraph explains the mechanism honestly, which is why this is a closure item and
not a finding about a hidden red. Closed by publishing the figure at the report's own
commit, or by section 8 not claiming it was.

**C44. The assumptions block carries five hardcoded measurements that nothing
regenerates.** `floatfea/model/platform.py:645-654`: `0.0000e+00`, `-2.6770e+08`,
`-1.0153e+06`, `70.711 m`, `51.056 m`. All five verify at this commit -- I checked every
one. BI3's reasoning applies exactly: a string in `floatfea/` that carries measurements
is a report nothing regenerates, and this one is surfaced in the run log where a reader
will trust it most. Closed by computing the slack at build time, or by carrying one
number and a pointer to the step report.

**C45. `MASS_PROPERTY_AGREEMENT`'s comment describes one use and the constant now governs
three decisions.** A comparison floor (`tolerances.py:1531`, described); a PSD
admissibility threshold at `floatfea/model/platform.py:529`, where the margin is 22
orders and the ladder therefore never descends; and a coordinate rounding grid at
`tests/verification/rung3/test_platform_skeleton.py:336` and `:361`. The third goes with
R600. Closed by the entry naming all three, or by the third not being this constant.

**C46. The CoG comparison's expected value is identically zero on all five bodies, so it
carries no sign.** Measured above: the projection's coupling block negated, 48 passed.
Not blocking -- (B) reddens on a displaced remainder and no body in this model has a
nonzero offset -- but the site should say it, because the next reader will take a green
CoG assertion for a checked sign.

**C47. The analytic reference applies `section.I_y` to both across directions.**
`tests/verification/rung3/test_platform_skeleton.py:162-164`, while the element applies
`I_z` in one bending plane and `I_y` in the other. Identical on every circular tube and
wrong on the first section with `I_y != I_z` -- which would read as an element defect
rather than a reference defect. Two corpus entries measure how invisible this is today:
swapping the element's two bending second moments, and replacing the reference's
`I_y + I_z` with `section.J`, both give 48 passed, because `Section.__post_init__`
requires `J == I_y + I_z` for a circular shape. Closed by using `I_z` for the
corresponding plane, which is a two-token change and costs nothing today.

**C48. `expected_pairs(superstructure, body)` never reads `superstructure`.** Goes with
R600; named separately so the closure commit does not leave a dead argument behind if
R600 is answered another way.

**C49. DZ5 has no ablation.** The `f`-ladder cell above. Closed by the four rows going
into the report, or into the closure artifact.

## Tolerances touched

```
cmd  git diff 52de940..HEAD -- floatfea/tolerances.py
out  one entry's COMMENT rewritten; no value added, changed, removed or widened
cmd  grep -n "MASS_PROPERTY_AGREEMENT: Final" floatfea/tolerances.py
out  1531:MASS_PROPERTY_AGREEMENT: Final[float] = 1e-13      -- unchanged
```

| | |
|---|---|
| constant | `MASS_PROPERTY_AGREEMENT` |
| old | `1e-13` |
| new | `1e-13` -- **unchanged**, and the entry says so |
| form | EXACTNESS, unchanged and still correct: dimensionless, relative to the quantity compared in every use, one entry over kilograms, metres and kilogram-metres-squared. The DZ1c normalisation makes the form MORE honest than it was -- the CoG is now relative to `l_b` rather than to a bare metre, which is what R598 turned on. |
| counter | **the phantom is deleted and the entry states what it has instead.** The binding cell is the element's torsional rotary term scaled by 2, which I reproduced: `1.5225e-18 -> 1.2983e-04` relative, fourteen orders above the floor. Verdict 73's condition allowed "the counter sentence is deleted and the entry states that it has none and why"; this is that, with the measurement named. **Accepted.** For an exactness entry a registered `_COUNTER` is not required and `test_counters_are_injected`'s registry is hand-written, which the entry now says in its own words. |
| justification | `docs/milestones/F2.md`'s table row, plus the entry's own comment. `36 * eps = 7.993606e-15` and `1e-13 / (36 eps) = 12.51` both re-verified. The worst-measurement figure `1.5522e-16` and the `~644` headroom re-verified at this commit. |
| widened? | **No.** Nothing in this file was loosened this step, and nothing anywhere else acquired a tolerance-shaped literal -- `tests/test_no_tolerance_literals.py` and `tests/test_plan_matches_tolerances.py` are both green in my run. |

**A note on the one place a tolerance moved into a new KIND of use.** `expected_pairs`
uses `MASS_PROPERTY_AGREEMENT * l_b` as a coordinate rounding grid. That is a different
form from a comparison floor and the entry does not cover it. It is inside R600 and is
answered there.

## My own instructions (4b)

```
cmd  git diff 52de940..HEAD -- .claude docs/SUPERVISOR.md
out  (no output)
cmd  git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out  tests/conftest.py
cmd  git diff 52de940..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out  (no output)
```

Untouched, both. No new conftest appeared anywhere under `tests/`, and no plugin was
added to the rung runs. `scripts/write_verdict.py` changed and it is my tool rather than
my instructions: I read the hunk line by line, it is additive, it removes no guard, and
the `latin-1` fallback is correct -- it cannot raise, and it rewrites UTF-8 so a mixed
file repairs itself. The commit that made it is standalone and `process:`-messaged.

## The adversarial corpus (BE3)

`tests/corpus/platform_geometry_gate.txt`, batch 22, committed separately at `008a8e9`.
**29 entries, all new this round.** Twenty-one carry a mutation. **Four of those are
numerically vacuous on this model** -- a circular tube has `I_y == I_z`, and
`Section.__post_init__` requires `J == I_y + I_z` for a circular shape, so two of the
substitutions `beam.py`'s own docstring warns about cannot be told apart here -- and
they are marked `expect=vacuous` rather than counted, because a vacuous mutation counted
as a catch is how a coverage number becomes a lie.

**Of the seventeen that are not vacuous, the shipped suite caught 9 and MISSED 8.**

Against 9 of 16 missed in batch 21 and 23 of 31 in batch 20. The proportion has not
improved, and the reason it has not is that the eight misses are one shape rather than
eight: every coordinate in the frame is compared only with itself. Close R600 and seven
of the eight go green in one commit. That is the most useful thing the number says this
round -- the misses have concentrated, which is what they did before R596 landed too.

## On the criterion, said once

I do not disagree with CZ0 and I am not asking for a fourth round or a wider blocking
head. Both findings here are inside (a)-(d): R600 is a gate assertion, R601 is a red
test at the reviewed commit. Everything else is in the closure list and I have not held
on any of it -- including four sentences I would have blocked on a year of rounds ago.

One observation about the mechanism rather than the criterion, and it leaves the loop
rather than becoming a round. **CZ0(d) and the milestone boundary are in tension, and
this step is the first place it bites.** The report cannot name a verdict in its own
milestone's review tree because none exists; the verdict cannot exist before the report;
and the guards that read both are parametrised over the pair. BU1 closed this for a step
boundary and the milestone boundary reopened it, because `_verdict_text_at` falls back
to the working copy when the named sha predates the tree. The state is legible -- the
implementer wrote it down in advance and the counts agree everywhere -- but "green means
green" does not hold here, and it is the one place my instructions say it must. That is
for Xabier, and the cheap answer is probably that the first report of a milestone names
the previous milestone's last verdict and its path, which is what it is actually
answering.

## Carried for the next step

**R600 and R601 carry BY NAME into the next round of `docs/reports/F3/step-1.md` and stay
BLOCKING.** R596, R598 and R599 are closed. Closure items C12, C14, C18 to C32, the open
part of C33 to C39 and C42, and C43 to C49 go into this step's closure commit as one list.

**Schedule.** F3 closes 13 October; the step report states the date and states that it
holds; I have no measurement that contradicts it. This is round 1 of 3, so nothing about
DZ7c is triggered yet. If this step reaches round 3 still carrying R600, DZ7c's rule
applies and **R600 is NOT ledgerable under it**: a frame whose geometry is unchecked can
change every member force in the table, which is exactly the test DZ7c sets.

## Next step opens when

**It does not open. This step stays open and these are the conditions, in this order:**

1. **R601 first, because everything else is measured against a green suite**, and
   because cause (a) is currently hiding whether R599's repair is green. The two
   DR1-compliant moves are named in the finding; choose one and say which.
2. **R600, all three sites, each with its diff hunk or the site named and the reason it
   was left.** The cell that closes it is "every member tip +3 m, applied in
   `_member_geometry` before `math.dist`", and it must go red.
3. **The closure list once, in one commit.**
4. Then the report's revision 2, with the generated sections, and the `Answers:` header
   naming THIS verdict at its own commit.

`python -m pytest -q` at `0 failed`, and a `workflow_dispatch` run at that commit with
`lint, unit and guards` green, are what I will check first.
