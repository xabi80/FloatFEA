# F3 step 1 — the platform superstructure

Answers: verdict 73 @ 52de940

**2026-09-30.**

F2 step 7 closed at verdict 73 carrying four items by name. This step opens with them,
and this is its first revision — the generated tables arrive with revision 2, once a
verdict exists in this milestone's review tree for the generators to read.

## 1. The reading

**Schedule: F3 13 October, F4 19 October, the member-force table 23 October, the
code-check screen 28 October — unchanged.** The 6–8 October figure was withdrawn last
round and is not reinstated. **All four carried items are answered** and the step
opens with nothing blocking: R599 first, for a green suite, then R596, R597 and R598
site by site, then the closure list, then this report and the marker move.

**DZ7c is recorded in the plan so the next escalation does not cost a round:** if this
step closes carrying, the answer is *reduce scope, do not slip* — carried items that
cannot change member forces or the G4.1 equilibrium check are ledgered; items that can
keep blocking, at F4's G4.1.

## 2. R596 — the gate was circular, and I published the signature of that as precision

```
claim  the platform's inertia comparison was `deck == deck`, by construction
cmd    the assembled tensor against the deck's, component by component
out    [0][0] +3.12500000000000000e+09 vs +3.12500000000000000e+09  identical: True
out    [1][1] +3.12500000000000000e+09 vs +3.12500000000000000e+09  identical: True
out    [2][2] +6.25000000000000000e+09 vs +6.25000000000000000e+09  identical: True
out    off-diagonals ~1e-26 against an exact 0
judge  the DIAGONAL -- the part carrying the physics -- differed by exactly nothing.
       The builder set `remainder = deck - member - parallel` and the gate added the
       same two terms back, from the same matrix.
```

**ERRATUM (DZ1d).** Revision 7 of `docs/reports/F2/step-7.md` published
`3.375e-36` as the platform's inertia residual and read it as an accuracy result. It
is withdrawn. `numpy.spacing(6.25e9) = 9.5367e-07`, so that figure is thirty orders
of magnitude below one bit of the quantity being differenced: it was the maximum over
the whole tensor normalised by `6.25e9`, and it came entirely from round-off on the
off-diagonal **zeros** while the diagonal was algebraically identical. A residual that
small is evidence that nothing was compared. **From now a residual below one ULP of
its scale is reported as `≤ 1 ULP`, never as a number.**

### What replaces it: an independent path (DZ1)

`analytic_properties` computes mass, CoG and inertia from node coordinates, the line
mass and the section. It never touches the assembled matrix, and it reads the
remainder off the model's lumped-mass input rather than recomputing it.

The rotary terms are **cited, not assumed**. `floatfea/element/beam.py:332-336,351`
says the torsional rotary inertia is `rho (I_y + I_z)` — the polar second moment — and
not `rho J`, with its reason; `bending_mass` carries `rho I`. So a member contributes,
about its own centre,

    J = m (L²/12) (1 − eeᵀ) + ρ_eq L [ J_p eeᵀ + I (1 − eeᵀ) ],   J_p = I_y + I_z

**If the element ever omits one of these, the residual is a finding and the reference
is not tuned to match.**

```
rule   (A) analytic == assembled, (B) analytic == deck, both at MASS_PROPERTY_AGREEMENT,
       mass normalised by M_b, CoG by l_b, inertia by M_b l_b^2 (DZ1c)
out    body       (A) mass     (A) CoG   (A) inertia   (B) inertia
out    platform  0.000e+00   3.648e-18     1.522e-18     1.522e-18
out    hub1      0.000e+00   1.421e-16     6.358e-17     6.358e-17
out    hub2      1.552e-16   1.421e-16     1.272e-16     6.358e-17
out    hub3      0.000e+00   1.421e-16     6.358e-17     6.358e-17
out    hub4      1.552e-16   1.421e-16     6.358e-17     6.358e-17
judge  worst 1.5522e-16 at hub2's mass, against a floor of 1e-13 -- 644x of headroom
```

## 3. DZ6 — four mutations, each with the code line, the red, and the restore

```
baseline  48 passed

(i) the element ROTARY-MASS term scaled -> (A) reddens
    file  floatfea/element/beam.py
    -     rho_ip_l = rho * (section.I_y + section.I_z) * ll
    +     rho_ip_l = rho * (section.I_y + section.I_z) * ll * 2.0
    out   10 failed, 38 passed
    out   AssertionError: platform: the analytic inertia and the assembled one
          disagree by 4.230312e+05 kg.m^2
    restored  48 passed

(ii) a member TIP moved +3 m -> DZ2 reddens
    file  floatfea/model/platform.py
    -     b = node(end, f"{label}_tip")
    +     b = node((end[0] + 3.0, end[1], end[2]), f"{label}_tip")
    out   20 failed, 28 passed
    restored  48 passed

(iii) a DUPLICATED member, COUNT PRESERVED -> DZ2 reddens
    file  floatfea/model/platform.py
    -     total_length = sum(m.length for m in members)
    +     members[-1] = <a copy of members[0]'s endpoints, keeping its own label>
    out   5 failed, 43 passed
    out   AssertionError: platform has duplicate members: 4 members occupy 3 distinct
          endpoint pairs, so at least one line is drawn twice and its mass is counted
          twice
    restored  48 passed

(iv) a 180x WALL error -> the section gate reddens
    file  floatfea/model/platform.py
    -     ARM_WALL: Final[float] = 0.180
    +     ARM_WALL: Final[float] = 0.001
    out   5 failed, 43 passed
    out   AssertionError: the builder uses t = 0.001; F1:389 records 0.18 m
    restored  48 passed
```

**The previous round's cell hit a docstring and measured nothing.** These mutate the
code line and each shows its diff, which is what DZ6 asked for.

## 4. R597 — the geometry was not gated at all

The reviewer measured four tips moved +3 m and four of sixteen members duplicated,
both **1765 passed**. A dropped member was caught by the count alone — a detection the
pre-DY1 CoG test had and my rewrite lost. DZ2 asserts the member count, the undirected
endpoint-pair set against the **deck's own** joint coordinates, no duplicate pairs,
and that each body is a star from its centre. Cells (ii) and (iii) above are the
evidence.

## 5. R598 — a phantom counter and two wrong figures

The entry cited `test_G3_1a_a_MISPLACED_remainder_reddens`. `git grep` found that name
in exactly one place: the comment itself. **I named a test I never wrote, in the file
whose purpose is that a value is not taken on trust.** It is deleted and replaced by a
pointer to §3 above, per DZ3 — demonstrations live in the report.

And the entry's own figures were wrong. It claimed a worst residual of `2.2119e-15`
and ~45× headroom; that divided a CoG offset by `1.0 m` instead of the body's extent.
Under `l_b` normalisation the worst at this commit is **`1.5522e-16`**, giving 644×.
The directive's correction, `1.9073e-16`, was measured against the pre-DZ1 gate; the
figure above is re-measured here, on the path that replaced it.

**`MASS_PROPERTY_AGREEMENT = 1e-13` is unchanged**, set from `36·eps = 7.993606e-15`
rather than from any measurement.

## 6. R599 — a guard that failed false, deleted rather than extended

The `named` whitelist required the nested failure to arrive through one of eleven
listed test names. The planted defect was detected three times over, by reporters that
name the commit and the file, and the assertion's message was false about those
states. **The list was unsound in both directions** — an unlisted reporter gives a
false red, a listed one firing for an unrelated reason gives a false green, which is
R516 recorded three lines below it. Adding a name had been the repair three times.
Deleted; `assert code != 0` and `_assert_diagnosis` are kept.

## 7. DZ5 — the deck's body inertias are physically inconsistent

**Report only. The FE keeps FloatSim's values, because inertia-relief equilibrium with
FloatSim's loads requires it.**

```
claim  the platform's deck inertia is M * 50^2 * (1, 1, 2) exactly
out    np.diag(J_G) = [3.125e+09 3.125e+09 6.250e+09]; M*2500*(1,1,2) identical: True
rule   a rigid body's principal moments satisfy I_i + I_j >= I_k

out    body        M t    k_z m   extent m   deck J_G slack     J_r slack
out    platform 1250.0   70.711     51.056       0.0000e+00   -2.6770e+08
out    hub1     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub2     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub3     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
out    hub4     1500.0   14.434     25.000       0.0000e+00   -1.0153e+06
judge  every body's J_G is planar at G -- the lamina identity, slack exactly zero --
       which no real three-dimensional body satisfies, and the buoys in the same deck
       do not. The platform's radius of gyration about z is 70.711 m against 50 m arms
       and a 51.056 m extent: the mass gyrates beyond the structure carrying it.
judge  J_r is PSD for every body and violates the triangle inequality for every body.
       The directive predicted about -2.67e8 for the platform; it is -2.6770e+08. The
       hubs were not predicted and are -1.0153e+06 each.

cmd    grep -rn "Inertia(Ixx=10.0\|Inertia(Ixx=0.5" ../HSP-stable/studies/platform-12buoy/
out    platform_common.py:159   inertia=Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)
out    platform_common.py:178   inertia=Inertia(Ixx=10.0, Iyy=10.0, Izz=20.0)
out    platform_rao_pilot.py:172 and :191 carry the same two literals
judge  typed into the study, not derived. HSP's `docs/platform-geometry.md:46` flags
       the hub value as Q2.
```

**The results label now reads** `buoy spar columns not assessed as members; buoy loads
applied as joint reactions; platform mass properties as in FloatSim; see DZ5 finding`,
and the assumptions block carries the figures. Xabier decides on FloatSim.

## 8. Corrections to the previous report (C33, C36, C37)

**C36 — the DY7 symmetry pairing was wrong.** I wrote that joints 5/15, 6/14 and 7/13
mirror. They do not: the pairs are **(5, 13), (6, 15), (7, 14)**. The reviewer
re-measured and got my exact figures for joints 2 and 3, so the observation that the
reactions are symmetric stands; the pairing I published for it does not.

**C37 — the command row did not produce the output row.** It read `--duration 30.0`
while the printed snapshot was at the script's default. The command is stated with its
arguments in §9.

**C33 — the whole-suite figure was two commits early**, published before the commits
it described. The line in §10 is taken at this report's own commit.

**C38 and C39, found in the same reading, were code and are fixed** (`3621b35`):
`range(12)` is not the twelve buoy joints — the joint order interleaves three buoy
joints with a hub-platform joint, so it took in joints 3, 7 and 11 and left out
buoy10–12 — and the buoy weight was typed rather than read from the deck. **The
published `0.6581 N` and `2.34e-03` do not move**; what is fixed is a latent error.

## 9. DY7 — the joint reactions, restated with the command that produced them

```
cmd    python scripts/report_joint_reactions.py --period 10.0 --duration 30.0
out    6 case files, 21 columns; columns naming a multiplier, reaction or joint: 0
out    buoys represented: 3 of 12 -- ['buoy1', 'buoy4', 'buoy7']
out    16 joints x 4 rows = 64 multipliers, read from res.lam
out    the largest buoy-joint Fz is 0.6581 N against a buoy weight of
       28.67 * 9.81 = 281.3 N, a ratio of 2.34e-03
rule   the study builds with `solve_equilibrium=False` and `xi` is displacement from
       the reference, so `lam` is the reaction ABOUT the equilibrium state
judge  a member-force table built from these alone would understate every arm by three
       orders of magnitude. F4's export must carry the equilibrium reaction as well as
       the history, and it is an ADDITIVE writer on the HSP side rather than a
       reconstruction.
```

The equilibrium identity does not close from what is exported: the inertia term is the
Cummins operator, and neither the per-body added mass nor the memory state is in the
file. That is DX1's gap one level deeper, and the script prints `|R + A|` labelled as
the part that is available rather than a residual that would look like the answer.

## 10. The whole suite

**Whole suite at `9cba81c`: 2628 passed, 0 failed, 0 skipped.** **The excluded set: 309 passed, 1 failed, 0 skipped.** Generated by `python scripts/suite_count.py`, run after every other edit to this revision, in a clean worktree at that commit. The first count excludes 310 tests in 3 files parametrised over this report (tests/test_report_carried.py, tests/test_report_numbers_are_sourced.py, tests/test_report_guard_states.py); the second is those same files, run at the same commit. R339: the count of what is excluded is part of the line. R497: so is its result, because a reader cannot otherwise tell a green tree from a green subset.

```
- **failed, in the excluded set** `tests.test_report_guard_states::test_the_guard_survives_the_state[guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL]`
```

**Zero failed and zero skipped in the main set.** The excluded set is one, down from
two: `test_the_answered_verdict_is_the_NEWEST_one` through the nested harness, which is
the ordinary interval red while this report waits for the verdict that judges it. The
other one cleared when R599's whitelist went.

**THE STEP MARKER MOVES IN THIS COMMIT (DY8c), and the consequence is stated rather
than discovered.** `REPORTS` and `REVIEWS` follow the plan carrying
`<!-- step-under-execution -->` since DX2, so from this commit they resolve to
`docs/reports/F3` and `docs/reviews/F3`. **There is no verdict in that tree yet** --
`scripts/write_verdict.py` refuses a step with no report, so this report has to exist
before the reviewer can write one. The report-parametrised guards are therefore red
between this commit and that verdict, and the generated tables arrive with revision 2.
The forced order is the reviewer's own: report and marker first, verdict second.
