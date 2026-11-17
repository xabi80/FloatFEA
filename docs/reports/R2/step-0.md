# R2 step 0 — measure only (GI3)

# Revision 1 — the plan lock answered, and the five measurements GI3 asks for

Answers: verdict 61 @ c931885
Answers file: `docs/reports/R2/step-0-answers.json`

*Three verdicts stand behind this report, accumulated newest-first in one file under DX2:
**61**, the addendum at `c931885` carrying R1223; **60**, the ES0 interim check at
`b2dc268` on commit `3d24e1c`; and **59**, the R2 plan-lock HOLD. This header names 61
because the newest verdict is the one the guard checks against and the one thing a machine
cannot check for itself — verdict 60's own closing note says so.*

*Verdicts 60 and 61 arrived by `git merge --ff-only origin/review/3d24e1c3808c`, as
SUPERVISOR.md asks. **Verdict 59 did not, and that was my error.** It reached this branch
by cherry-pick — byte-identical, which the reviewer verified independently
(`git diff review/91c2d2e05c7b adc6c3c -- <the verdict file>` empty) — because I committed
and pushed `8c0edce` while the review of its parent was in flight, leaving the branch
diverged with a force-push forbidden. The reviewer ruled the cherry-pick acceptable and
not an escalation, and named the unwritten rule it exposes: **do not commit to the
reviewed branch between invoking the reviewer and merging the verdict.** That rule is
worth Xabier's attention; it is not in CLAUDE.md or SUPERVISOR.md today.*

**2026-11-17. THE SCHEDULE: GI SETS NO DATE, and this report does not invent one.** R1
closed at the `R1` tag (`a780a9d`, unmoved) and GG4 parked the milestone; GI reopened work
as R2 on 17 November. Every previous milestone in this repository was measured against a
date a directive named — FL5's 28 October, FR0's 5 November, FW0's 10 November — and GI
names none, so what this paragraph carries instead is the one thing that *is* a schedule
fact: **GI6 stops the milestone here.** Step 0 is measure-only, this report is its output,
and no step-1 code is written until Xabier confirms or overrides D1–D4. Nothing has
slipped because nothing is due. **Two things are escalated under FZ (e) and they are in
§7**: R1206's apparatus repair, which needs a directive because one of its six sites is
`.claude/hooks/`, and the D1/step-2(iii) contradiction, which is GI's own and has no answer
inside the plan. This is the one hand-written paragraph CZ0 allows, and it carries the
schedule because that is what CZ0 says it carries.

## 1. What this commit is, and what it is not

It is the four conditions of the plan-lock verdict, the one code change GI3(e) permits, and
the five measurements of GI3. It is **not** step-1 code and it does not touch
`floatfea/export/`, `floatfea/cli.py` or any gate.

The plan-lock verdict was **HOLD** with four blocking findings. All four are answered in
§6. One of them — R1206 — is answered by **choosing an exit and escalating the one that
would close it**, which is not the same as closing it, and §6 says so rather than claiming
otherwise.

## 2. GI3(a) — inertial versus joint reaction, and what it says about mass sensitivity

**At the body the split is 1:1 BY CONSTRUCTION, so the question as posed has no other
answer.**

```
claim  |M xi_ddot| against |sum_j contrib_j|, per body, per case
cmd    per-body max over case<i>/m_xddot[:n] and the pair-summed case<i>/contrib,
       from data/f4/dynamic_inputs.npz
out    T=12.5  platform  |M a| 2.4144e+01  |react| 2.4143e+01  ratio 1.000
       T=12.5  hub1      |M a| 1.4537e+01  |react| 1.4534e+01  ratio 1.000
       T=12.5  hub2/3/4  ratio 1.000 on force, 1.000-1.001 on moment
       T=10.0  all five  ratio 1.000 on force, 1.000-1.001 on moment
rule   GI3(a): "the share of the governing load that is inertial ... versus joint reaction"
judge  The joint reactions are the ONLY external force on the five FE bodies -- C, mu, the
       external force and the added-mass contribution are identically zero on them
       (EK0(a)) -- so `M xi_ddot = sum_j reactions` IS the momentum balance. The two sides
       agree to round-off and a "share" between them is 1:1 wherever the balance holds.
       The 0.1% on the moment channel is R711's discrete-versus-continuous difference,
       not a physical split.
```

**At the member, the split that exists is static against dynamic**, because
`forces_table.py:808-817` maps `lam` to the FE joint nodes and then calls
`solve_inertia_relief`, so the inertial field is computed FROM the reaction.

```
claim  static vs dynamic share of the stress each utilisation is formed from
cmd    static and total_instant rows of results/R1/example/member_forces.csv, joined to
       results/R1/example/utilisation.csv on (body, member, station)
out    body      member      stn   T_s        U  sig_stat  sig_tot  STATIC%  dyn%
       platform  hub2_arm    ROOT 12.5  1.71167    269.72   455.72   59.2%  40.8%
       platform  hub4_arm    ROOT 12.5  1.71167    269.72   455.72   59.2%  40.8%
       platform  hub3_arm    ROOT 16.2  1.18223    269.72   314.67   85.7%  14.3%
       platform  hub1_arm    ROOT 12.5  1.17709    269.72   312.17   86.4%  13.6%
       hub3      buoy8_arm   ROOT 12.5  0.80821    179.81   214.83   83.7%  16.3%
       hub1      buoy2_arm   ROOT 12.5  0.79049    179.81   210.14   85.6%  14.4%
       (sigma in MPa; ROOT stations with a utilisation only)
rule   GI3(a): "This says how sensitive sizing is to mass."
judge  At the governing station the stress is 59.2% static. The COMPONENT breakdown is
       what matters and it is not one ratio:
         My  static +1.916016e+08   dynamic -1.141810e+07   the dynamic term REDUCES My
         Mz  static  0.000000e+00   dynamic +2.689043e+08   entirely dynamic, and LARGER
                                                            than the static My
         Vy  static  0.000000e+00   dynamic +5.190609e+06   entirely dynamic
       The governing station carries gravity bending about one axis and a purely dynamic
       bending about the other, and the dynamic one is the bigger moment. BOTH scale with
       mass -- static as m*g directly, dynamic because FloatSim computed `lam` with those
       masses -- so sizing is first-order sensitive to mass through two channels.
```

### 2a. The loop gain, and why D3's cap is the number to look at

Treating `sigma ~ m_body / Z` and, for a tube at fixed diameter, `Z ~ A`, the iteration
`A_{n+1} = (m_nonstruct + k*rho*L*A_n)/c` has gain `g = k * m_steel / m_body`.

```
claim  the loop gain and the iterations it implies at D1's basis
       (k = 1.0, m_nonstruct = 625 t platform / 375 t per hub)
cmd    A = pi*(D-t)*t; steel = A*L*7850; g = steel/(m_nonstruct+steel);
       n = ln(0.005/e0)/ln(g) with e0 = 0.178; L = 200 m star, 75 m per hub
out    group       section      A m2   L m  steel t  m_body t  gain g  iters to 0.5%
       platform    2.5 / 0.18  1.3119  200     2060      2685   0.767          13.5
       platform    3.0 / 0.12  1.0857  200     1705      2330   0.732          11.4
       hub (each)  2.5 / 0.18  1.3119   75      772      1147   0.673           9.0
       hub (each)  3.0 / 0.08  0.7339   75      432       807   0.535           5.7
       control: A(2.5,0.18)*200*7850 = 2059.7 t, which is the pre-R2 acceptance
       report's own figure for the four 50 m platform arms, to the digit
rule   D3: "every body's mass changes by < 0.5% between iterations ... At most 8
       iterations. If it oscillates (2-cycle), apply 0.5 under-relaxation"
judge  ESTIMATE, NOT A MEASUREMENT, under three named first-order assumptions:
       sigma ~ m/Z; Z ~ A at fixed D; reaction ~ m_body. Each is checkable once step 2
       exists and none is checkable now. What it says is worth saying before step 2 is
       built:
       * g is 0.53-0.77, so the loop CONVERGES and converges MONOTONICALLY. It is not
         predicted to oscillate -- so D3's 2-cycle detector and its 0.5 UNDER-relaxation
         address a failure mode this loop is not predicted to have.
       * The platform needs 11-14 iterations to reach 0.5%. D3'S CAP IS 8. On this
         estimate the cap, not oscillation, is the binding constraint, and D3's own rule
         then applies: stop and report, never report a non-converged result as a design.
       * The remedy matching a monotone gain is OVER-relaxation by about 1/(1-g) ~ 4, or
         solving the fixed point in closed form -- which is the shape of the R694 repair
         CLAUDE.md records: a constant right at one configuration replaced by the closed
         form the quantity actually has.
       This is a GI6 question for Xabier, not a change made here.
```

## 3. GI3(b) — wall time of one FloatSim run, and the cost of one D4 iteration

*Measured through `report_joint_reactions.solve_one`, which is the call
`export_f4_dynamic_inputs.py:190` uses to produce the reference npz, with
`PLATFORM_MASS_OVERRIDE` set to ER0's basis as that script sets it at `:185`, durations
from `g41_dynamic.window_duration` = `RAMP_S + 15*T_model`, `dt = 0.01`. Read-only on HSP
(GI1): `solve_one` solves in memory and writes no file, and nothing was written into
either worktree.*

```
claim  wall time of one FloatSim run at the R1 config, and of one D4 iteration
cmd    scripts/export_f4_dynamic_inputs.py --check, all six periods through
       report_joint_reactions.solve_one with ER0's override, dt = 0.01, durations
       g41.window_duration = RAMP_S + 15*T_model; THREADS PINNED to 1 on all five of
       determinism.THREAD_ENV
out    --check exit 1, wall 25 min 56 s      <- six cases, one heading = ONE D4 ITERATION
       per-case boundaries from the same run, UNPINNED (a separate, slower run):
         T_full 10     9.4 min
         T_full 12.5  10.7 min
         T_full 14    12.6 min
         T_full 15    12.1 min
rule   GI3(b): "Wall time of ONE FloatSim run at the R1 config, and the projected cost
       of one loop iteration over all headings and sea states."
judge  **ONE D4 ITERATION IS 26 MINUTES, NOT 74.** The 74 was my own projection from the
       UNPINNED run, scaled linearly from its first case, and it was wrong by 2.9x --
       because pinning the threads makes the solve FASTER here, not slower. Four cores
       contending on an 884-step convolution lose more to synchronisation than they gain.
       The projection's arithmetic was right and its operating point was wrong, which is
       what CP3 is about.
         D3's cap of 8 iterations          ~ 3.5 h
         the 11-14 that (a) estimates      ~ 4.8-6.0 h
       So D4's "every heading and sea state" is affordable in full and needs no working
       set, and the cap, while still probably too small on (a)'s gain estimate, is a
       3.5-hour run rather than a 10-hour one. **The number to fix before relying on
       either figure is the toolchain (§7).**
```

## 4. GI3(c) — how mass and inertia enter HSP's deck builder, and the override path

**They do not enter it. The builder is a function over literals, and the Deck object is
the only override point that exists.**

```
claim  what input HSP's deck builder takes for mass and inertia
cmd    read platform_rao_pilot._deck_with_drag and platform_common.py in the pinned
       HSP-runs worktree at floatfea-ref-1
out    _deck_with_drag() takes NO arguments and reads NO file. All 17 bodies are
       constructed in Python from literals:
         platform_common.py:41       PLATFORM_MASS = 10.0
         platform_common.py:158      mass = cc.ARM_MASS_TOTAL           (the hubs)
         platform_common.py:159      Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)
         platform_common.py:177-178  mass=PLATFORM_MASS,
                                     Inertia(Ixx=10.0, Iyy=10.0, Izz=20.0)
rule   GI3(c): "How mass and inertia enter HSP's deck builder, and whether an override
       path exists without editing FloatSim source. If none does, escalate per GI1."
judge  There is NO file input, so the returned Deck OBJECT is the only override point and
       the alternative to mutating it WOULD BE an edit to FloatSim source -- which GI1
       forbids. The override is therefore not merely sufficient, it is the only
       admissible mechanism. **GI3(c) RAISES NO ESCALATION.**
```

```
claim  the override path exists, is shipped, and is what produced the reference npz
cmd    git grep -n "PLATFORM_MASS_OVERRIDE" -- scripts
out    scripts/report_joint_reactions.py:137      the module global, default None
       scripts/report_joint_reactions.py:158-163  mutates body.mass and body.inertia
                                                  in place, before build_system
       scripts/export_f4_dynamic_inputs.py:185    rjr.PLATFORM_MASS_OVERRIDE = ER0_OVERRIDE
       scripts/measure/g41_dynamic.py:213         the gate sets it too
cmd    python -c "print(list(np.load(NPZ)['case0/body_mass']))"
out    [20.0, 12.0, 12.0, 12.0, 12.0]
rule   GI5 step 2's zero-change test: "feeding today's masses reproduces the reference run"
judge  "Today's masses" are ER0's, not HSP's own `PLATFORM_MASS = 10.0`. The override
       defaults to `None`, which is a DIFFERENT run, so step 2 states which it feeds.
       Corroboration from GI itself: D1's 625 t and 375 t are (1-0.75) x 2500 t and
       (1-0.75) x 1500 t -- ER0's platform at lambda = 50, not HSP's 1250 t -- so GI4 is
       already reckoning from the overridden basis.
```

**What step 2 must generalise, measured rather than assumed.**
`_apply_platform_override` selects `b.name == "platform"` and writes `Ixx`, `Iyy`, `Izz`
only, while `_inertia_matrix` reads all six components. **One body of five, three
components of six.** `export_platform_deck.apply_override`'s generic dict walk is the
better shape to generalise from. And GI1 asks for a *declared override file*: ER0 did both
halves — mutate the object **and** serialise to `data/platform/platform12_deck.yaml`, with
the provenance json recording the dict. Only the in-memory half exists on the solve path.

## 5. GI3(d) — buoyancy, ballast, and the sign of the correction

```
claim  which deck bodies carry buoyancy, and which bodies R2 changes the mass of
cmd    per body in data/platform/platform12_deck.yaml: hydro_body_label, structural,
       len(drag_elements), reference_point z
out    12 buoys   hydro_body_label buoy1..buoy12  structural False
                  10 morison members + 1 heave plate each
                  z_ref -1.1957 (submerged)       mass 28.67 kg
       4 hubs     hydro_body_label None           structural True
                  drag_elements []                z_ref +0.4934  mass 12.00 kg
       platform   hydro_body_label None           structural True
                  drag_elements []                z_ref +0.7000  mass 20.00 kg
rule   D2: "Every floating body (or the buoy carrying a changed body) gets compensating
       ballast, so its equilibrium draft and trim stay at the BEM reference."
judge  THE FIVE BODIES R2 RESIZES ARE NOT FLOATING BODIES. Platform and hubs have no
       hydro database, no drag elements and reference points ABOVE the waterline; they
       have no draft of their own and no waterplane, and are held up entirely by the 12
       buoys through the 16 joints. So D2's parenthetical is not a special case, it is
       the ONLY case: ballast sits in the buoys and the draft check is on the BUOYS.
       "The draft is held" is a condition on TOTAL WEIGHT AND ITS DISTRIBUTION, measured
       per buoy, not a per-body draft check.
```

```
claim  which way the first iteration moves the mass, and so which way ballast goes
cmd    D1 at k = 1.0 over the shipped deck and builder, full scale
out    platform      2500.0 -> 2684.7 t   +7.39 %
       each hub      1500.0 -> 1147.4 t  -23.51 %
       five bodies   8500.0 -> 7274.3 t  -1225.7 t,  -14.42 %
       the 12 buoys  43005 t             so the change is 2.85 % of buoy mass
rule   GI3(d): "where ballast could sit, so draft can be held (GI4 D2)"
judge  THE SYSTEM GETS LIGHTER ON ITERATION ONE, SO BALLAST IS ADDED, NOT REMOVED. The
       hubs dominate and they lose 23.5% each. **This corrects the direction I gave
       before the measurement**, which reasoned from the platform's +7.39% alone and
       concluded that ballast would have to be removed. The platform does get heavier;
       the system does not.
       D2 needs a BALLAST BUDGET PER BUOY in both directions -- a buoy at zero ballast
       cannot compensate a mass increase, and a buoy at full ballast cannot compensate a
       decrease -- and the refusal fires when the budget is exhausted rather than when a
       drift exceeds a tolerance. **How much removable ballast a buoy carries is not in
       the deck.** That is a physical input and it is Xabier's under FZ.
       And every figure above is one to two decades outside D3's 0.5% band, so iteration
       one cannot converge by construction.
```

## 6. The four blocking findings of the plan-lock verdict

**R1205 — two live markers. ANSWERED.** `docs/milestones/R1.md:3` now reads
`<!-- step-under-execution: moved to R2 at step 0 (GI) -->`, the form `F2.md:10`,
`F3.md:9` and `F6a.md:3` use, as the condition words it.

```
claim  exactly one plan carries a live marker, and the resolvers reach R2
cmd    grep -rlE '<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->' docs/milestones/
out    docs/milestones/R2.md          (count: 1)
cmd    python -c "import check_carried, ci_section; print(check_carried._active_step(), ci_section._PLAN.name)"
out    ('R2', 1) R2.md
rule   R1205 *Closed when* R1.md:3 retires its marker ... in a commit that also answers R1206
judge  Answered. The two symptoms the verdict measured are gone: `_active_step()` no
       longer returns ('F2', 4), and `ci_section` imports instead of raising SystemExit,
       so the 11 report-guard ids that died on that import no longer do.
```

**R1206 — `step 0` is not representable. EXIT (ii) CHOSEN; THE EXIT THAT WOULD CLOSE IT IS
ESCALATED, AND I SAY SO RATHER THAN CLAIMING CLOSURE.**

```
claim  what each of the three marker states does, same three report-guard files
cmd    pytest -q tests/test_report_carried.py tests/test_report_guard_states.py
       tests/test_report_numbers_are_sourced.py, one marker state per run
out    marker 0 on R2   114 failed, 126 passed, 1 skipped
       marker 1 on R2   114 failed, 126 passed, 1 skipped
       and the discriminating message, which is NOT the count:
         marker 0 -> "R2.md carries no readable step number, so the guards fell back to
                      the newest complete report/verdict pair. That is the behaviour DB2
                      replaced, and it makes the step boundary permanently red."
                      (test_report_carried.py:617, assert 0 = _plan_step())
         marker 1 -> "the plan says step 1 is under execution and there is NEITHER a
                      step-1.md under docs/reports/R2 nor one under docs/reviews/R2"
                      (test_report_carried.py:639)
rule   R1206 *Closed when* one exit is chosen, the cell re-run, and
       `test_the_plan_names_the_step_under_execution` is green with R2 under execution
judge  THE COUNT DOES NOT DISCRIMINATE, AND NEITHER DOES THE MESSAGE. Both states give
       114, because R2 had no report at all and every guard reading the active report
       fails -- EG3 state (2), which this report clears. I first read the two messages
       and chose marker 1, on the ground that its failure is loud and true while
       marker 0's is a silent fallback. **That was wrong, and the thing that settles it
       is a third measurement neither message mentions:**
         marker 1  ->  scripts/ci_section.py: FileNotFoundError
                       docs/reports/R2/step-1.md -- THE CI SECTION CANNOT GENERATE
         marker 0  ->  generates, anchored on verdict 59 at 91c2d2e through this
                       report's own `Answers:` line
       CE1 makes that section MANDATORY. The sentinel collision is in
       `check_carried._active_step` and `test_report_carried._plan_step`.
       **So: marker 0 -- which is also simply what is under execution.**
```

**AND EXIT (iii) WAS TAKEN, SO R1206 IS CLOSED. My escalation of it was withdrawn
because its premise was wrong and I had not measured it.**

```
claim  exit (iii)'s scope, and whether it needs a directive
cmd    sed -n '81p;110p;134p' .claude/hooks/require-verdict.sh
out    81   marker_re='...step-under-execution:[[:space:]]*[0-9]+...'
       110  step=$(grep -oE "$marker_re" "$plans" | head -1 | grep -oE '[0-9]+')
       134  if [ -z "$step" ]; then          <- THE HOOK'S SENTINEL IS THE EMPTY STRING
cmd    grep -n '"0"\|-eq 0\|step -gt\|step == 0' .claude/hooks/require-verdict.sh
out    (no match)
rule   R1206 *Closed when* one exit is chosen, the cell re-run, and
       `test_the_plan_names_the_step_under_execution` is green with R2 under execution
judge  **THE HOOK HAS NO COLLISION AND NEEDS NO CHANGE.** `0` is readable at `:110` and
       distinct from unreadable at `:134`, so the hook resolved `step-0.md` correctly
       throughout. I claimed `.claude/hooks/require-verdict.sh:81,110` was one of the six
       sites and escalated on that basis -- CLAUDE.md would indeed have required a
       standalone `process:` commit citing a directive, and refusing that door was right.
       **The premise was not.** I read two line numbers instead of running them, which is
       the BF0 failure in its own shape: a claim about this repository with no command
       under it. The collision is three lines in `tests/`, where EK2's "a guard that fails
       false is fixed, not extended" applies directly and no directive is needed:
         tests/test_report_carried.py:100,111   return None, 0   ->  return None, None
         tests/test_report_carried.py:617       _plan_step() > 0 ->  is not None
       plus `_plan_step`'s return type and the one `STEP` expression that tested
       membership on it.
cmd    the three-cell table re-run, one variable moved
out    marker 0  ->  1 passed in 0.27s
       marker 1  ->  1 failed in 0.24s   (step 1 has not started, which is TRUE)
```

**R1207 — step 2's gates (ii) and (iii) are passed by a no-op. ANSWERED.**
`docs/milestones/R2.md` §3 step 2 now carries both halves: (ii) is a **pair** — the
zero-change run reproduces bit-identically **and** a perturbed-mass run does not,
differing in `case<i>/body_mass`, `m_xddot` and `accel` — reusing
`export_f4_dynamic_inputs.py:467-479`, which is already Q8's rule with "there is no
tolerance on this comparison"; and (iii) closes against `case<i>/body_mass` **read back
from the npz the solve wrote**, which `:390` takes from the deck the solve actually used,
rather than against the tool's own variables. Provenance, not existence.

**R1208 — one key for two worktrees. ANSWERED, and the code is in this commit.**

```
claim  no sibling-of-the-repo guess remains, and the two keys resolve
cmd    git grep -nE '(ROOT|parents?\[[0-9]\])\s*(\.parent)?\s*/\s*"HSP-' -- scripts floatfea
out    three hits, all PROSE in docstrings, two of which this commit corrected under
       BP0 because they described code this commit changed
       (export_f4_dynamic_inputs.py:8, f4_dynamic_residual.py:8); the third is
       hsp_pin.py:80 describing what it replaced. No assignment remains.
cmd    FLOATFEA_HSP_RUNS=... FLOATFEA_HSP_STABLE=... python -c "hsp_pin.worktree(...)"
out    worktree('runs')   -> C:\Users\xlama\OneDrive\Documents\buoy\HSP-runs
       worktree('stable') -> C:\Users\xlama\OneDrive\Documents\buoy\HSP-stable
       with no env set, require=False: C:\dev\HSP-runs, C:\dev\HSP-stable, NO refusal
       with no env set, require=True:
         REFUSED: cannot locate the pinned HSP runs worktree (tag floatfea-ref-1).
           tried declared (floatsim.worktree_runs): not set
           tried $FLOATFEA_HSP_RUNS: not set
           tried legacy sibling of the repo root: C:\dev\HSP-runs is not a directory
rule   R1208 *Closed when* sec.2c and sec.3's step-0 gate say TWO keys, name which sites
       take which, keep `export_buoy_centers_ref` on the stable key, and show the three
       DS0 refusals still firing
judge  Seven assignments in six files, routed: the four runs sites on `worktree("runs")`,
       `export_buoy_centers_ref.py` and `hsp_pin` on `worktree("stable")`,
       `run_floatsim_design_waves.py` on BOTH -- which is why its two assignments count
       separately: it runs in RUNS and asserts it is not STABLE, so one key would make
       that comparison compare a path with itself.
       **`require=False` IS THE DEFAULT AND THAT IS THE POINT.** These are module-level
       constants imported by `tests/` and by `export_f4_dynamic_inputs.py`; refusing at
       import would turn "this machine has no worktree" -- true of CI by design -- into
       an ImportError taking the whole module with it, which is R670's shape exactly.
       So the default returns the best candidate as the bare expressions did, and each
       caller's own preflight still refuses with its own message.
```

```
claim  the three DS0 refusals still fire after the change
cmd    git grep -n "HSP-stable, which is read-only\|refusing to run against HSP-stable\|is at .*not the pinned" -- scripts
out    scripts/run_floatsim_design_waves.py   the runs-worktree-is-HSP-stable refusal
       scripts/report_joint_reactions.py      the same check in _preflight
       scripts/export_platform_deck.py        the tag/commit refusal on HSP_RUNS
rule   R1208's closing condition names the refusals explicitly
judge  All three are untouched by this commit -- the resolver returns a path and checks
       nothing else, deliberately, because replacing three loud differently-worded
       refusals with one is the extend-not-repair line EK2 draws.
```

## 7. ESCALATION — TWO items, Xabier's

**(1) THE COMMITTED `dynamic_inputs.npz` DOES NOT REGENERATE FROM THIS TREE, AND FQ3
ALREADY RULED ON IT: STOP AND REPORT RATHER THAN RE-BASELINING.**

```
claim  why --check refuses, with the one variable that moved
cmd    git log -1 -- data/f4/dynamic_inputs.npz
out    62a8281   written at R1 step 1 revision 3, untouched since
cmd    git show cfb76ff   (R1 step 2's first commit, AFTER 62a8281)
out    "100 arrays reproduce the committed file EXACTLY"   -- GREEN, threads unpinned
cmd    git log -S "numpy==2.5.4" -- constraints-dev.txt
out    09d5bc9   R1 step 2 revision 1
cmd    git merge-base --is-ancestor cfb76ff 09d5bc9 ; echo $?
out    0         -- the GREEN --check PRECEDES the pin move
cmd    python -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"
out    2.5.4 1.18.1          against BASELINE_CONDITIONS' 2.4.4 / 1.17.1
cell   ONE VARIABLE ACROSS THE GREEN/RED BOUNDARY. Threads: UNPINNED on both sides.
       numpy and scipy: moved by 09d5bc9 between them. HSP-runs at floatfea-ref-1 /
       25de7ce, and all 64 INPUT arrays bit-identical -- a solver-bit move, not an
       input move.
rule   constraints-dev.txt's FQ3 block: "if the golden moves under these pins, STOP and
       report rather than re-baselining."
judge  **MY TWO DIAGNOSES WERE BOTH WRONG AND THE ABLATION WAS IN THE GIT HISTORY ALL
       ALONG.** I said bit-identity; it refused. I said thread count; the threads were
       unpinned on BOTH sides of the boundary, so the count cannot be the cause -- and
       `ci.yml` says why it never could be, three lines below the lines I cited: "THE
       BLAS KERNEL, PINNED (CF1). Thread count alone was not enough." I cited 67-69 and
       stopped reading. The cause is this repository's own numpy/scipy pin, moved by a
       commit this repository can name.
```

**And the magnitude, which is what the decision turns on:**

```
claim  how big the difference is, relative to each array's own scale
cmd    one case regenerated at T_full = 12.5 s (the GOVERNING period), compared against
       the committed case1 arrays; scale = max|committed|
out    array        shape          max|a|      max|diff|   diff/scale    in eps
       accel    (884, 5, 6)  1.211464e+00     5.2905e-14    4.367e-14     196.7
       base     (884, 5, 6)  2.414287e+01     2.0606e-13    8.535e-15      38.4
       contrib (884, 20, 6)  7.354023e+01     3.9790e-13    5.411e-15      24.4
       WORST relative to its own array scale: 4.3670e-14  =  196.7 eps
rule   R1225 (i): "~1e-16 is consistent with the pin; 1e-3 is a larger finding"
judge  **ROUND-OFF.** ~200 eps accumulated over 884 timesteps of a Cummins convolution
       is what a reduction-order change from a library minor bump looks like. It is TEN
       ORDERS OF MAGNITUDE below the six figures `U = 1.71167` is published to, so no
       published number can move. The committed npz is physically right; its last bits
       belong to a toolchain this machine no longer has.
       **A CORRECTION TO MY OWN FIRST MEASUREMENT OF THIS.** The first probe reported
       `max rel 1.210e-01` -- 12% -- for the same 5.29e-14, because it divided
       ELEMENTWISE by `max(|a|,|b|)`, so entries where both are near zero dominated. A
       relative measure anchored on a near-zero element measures the element, not the
       array. It also died converting a string array and lost every row after
       `joint_body_a`. The table above is the ratio to the array's own SCALE, which is
       what R1225 (i) asked for and what I did not compute the first time.
```

**THE DECISION IS YOURS, and the two options are not equivalent:**

* **Restore the baseline toolchain** from `HSP-runs/requirements-lock.txt` (`numpy==2.4.4`,
  `scipy==1.17.1`, `xarray==2026.7.0`) and re-run. `--check` should then pass and the
  provenance refresh becomes a sha-only change. Cost: an environment rebuild.
* **Accept a re-base** under the current toolchain. Cost: every figure downstream of the
  npz is regenerated and re-reviewed, the `G4.1 force` / `G4.1 moment` rows in
  `results/F6/floatfea_results_report.md` move, and the R1 closure artifacts need marking
  — for a last-bits reason, which is precisely what CLAUDE.md's golden-file rule forbids
  doing silently.

**I have done neither, and the staleness red and R1223 therefore stay red with their
cause named.** `--check` wrote nothing (`git status --porcelain data/` empty) and no write
run was made. Note also that this blocks step 2's gate (ii) from ever being meaningful
until the toolchain is pinned at the point of generation: `dynamic_inputs.provenance.json`
recorded no thread count, no BLAS coretype and no library versions, so nothing in the
artifact said which environment produced it. **That half is fixed in this commit** —
`scripts/export_f4_dynamic_inputs.py` now records `determinism.report()`, the coretype and
the six library versions, which the reviewer ruled FF0-class rather than a ledger row.

**(2) GI's D1 and GI5 step 2 (iii) contradict each other, and only Xabier can pick.**

**R1206's escalation is WITHDRAWN**, not because a hook change was authorised but because
no hook change was needed. See §6. The thing I had written here — a six-site diff with
`.claude/hooks/require-verdict.sh` named as the blocker — was wrong at its premise, and
the record keeps that rather than deleting it, because the error is the instructive part:
**I named two line numbers in a file I had not run.** BF0 exists for exactly that, and it
applies to an escalation as much as to a figure. The repair was three lines in `tests/`.

**GI's D1 and GI5 step 2 (iii) contradict each other, and only Xabier can pick.**
D1: `body mass = m_nonstruct + k*m_steel`. Step 2 (iii):
`member steel + non-structural + ballast = body mass, exactly`. **Consistent only if
ballast is identically zero** — and if ballast is zero, D2's draft cannot be held when
`m_steel` moves, so gate (iv) fires on the design rather than on a test. One of the two
needs a ballast term. §5 above measures the size of the problem: the five bodies lose
1225.7 t on iteration one, which is 2.85 % of the buoys' 43 005 t and must go somewhere.

## 8. Carried

Pointers only (CH4). Every row points at the section that discusses it.

| id | state | where |
|---|---|---|
| R1205 | **answered** | §6 |
| R1206 | **open — exit chosen, closure escalated** | §6, §7(1) |
| R1207 | **answered** | §6 |
| R1208 | **answered** | §6 |
| R1209 | answered | `docs/milestones/R2.md` §2c — the census is now seven assignments in six files, with the needle that finds all seven |
| R1210 | answered | `docs/milestones/R2.md` §2b — the config declares NO heading key; the false `out` line is replaced |
| R1211 | answered | §4 — one body of five, three inertia components of six, and the declared-override-file half |
| R1212 | **Xabier's** | the verdict's own filename finding; no action here |
| R1196–R1201 | **open, routed here by verdict 58 item 2** | six prose/one-line items in two files; none blocks under FR1 and none is a step-0 matter. Carried to step 1. |
| R1186, R1188, R1189(c), R1190, R1191, R1193 | **open, routed here by verdict 58 item 3** | R1193 and R1188 are discharged from the reviewer's side (`2e08766`, GG3); the rest carry to step 1 |
| R1202 | answered before this milestone | `bb952e7` |
| R1203, R1204 | reviewer-side or Xabier's | no action here |
| R835 | R2's under GE3, not re-measured | carried to step 1 |

**Verdict 58 item 4 is satisfied by this report's header**, which answers the newest
verdict by sha (`adc6c3c`) and carries verdicts 55 onward in the rows above.

## 9. The marker, and the two reds this report is expected to leave

Stated in advance rather than discovered: at marker `0`, with this report present,
`test_the_plan_names_the_step_under_execution` stays red on the sentinel collision
(`test_report_carried.py:617`, `assert 0 = _plan_step()`), which is R1206 itself, and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` was **already red at `251af69`, before
this turn began** — measured in a detached worktree at that commit, `1 failed in 0.34s`.
The first names R1206, a finding of the newest verdict, so it is a boundary red under the
FS1 limb-one predicate. The second's subject is its own commit's CI run, which is FT1
limb two. Every other red is traced by id in §10.

<!-- WHOLE_SUITE -->

## 10. CI at the judged commit

<!-- CI_SECTION -->
