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
out    ('R2', 0) R2.md
       (R1236: this read `('R2', 1)` in revision 1. It was taken while the marker was
       still at 1 and was not regenerated when the marker moved to 0 -- BP0, in the
       report whose own section 7 cites BP0.)
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

## 6a. Verdicts 60, 61 and 62's findings

**R1213 — the DS0 refusal that did not fire.** `run_floatsim_design_waves.py` tested
`RUNS.resolve() == STABLE.resolve()`, an identity test against the other key. Unreachable
while both were literals; GI3(e) made it reachable, and a runs key pointed at the real
production `HSP-stable` then passed it while `main()` went on to write six case CSVs into
the read-only worktree. The name test is added **beside** the identity test (EK2).

```
cmd    FLOATFEA_HSP_RUNS=.../buoy/HSP-stable, stable key unset, preflight() called
out    name test     : True
       identity test : False      <- what the old check saw, and why it passed
       REFUSED: the runs worktree resolves to ...\HSP-stable, which is HSP-stable --
                read-only from here (DS0). ... refuses by NAME and not only by identity
                with the stable key (R1213).
```

**R1214 — a key set but wrong was silently discarded**, so a caller opened a different
tree from the one declared. Now a refusal naming the source and the value; only an
**unset** key falls through, because the six call sites are module-level constants and
refusing at import would turn "this machine has no worktree" — true of CI by design —
into an ImportError taking the module with it, which is R670's shape.

```
cmd    FLOATFEA_HSP_RUNS=C:/nope/not/a/worktree
out    REFUSED: the HSP runs worktree was declared and is not a directory.
         $FLOATFEA_HSP_RUNS = C:\nope\not\a\worktree
cmd    unset, require=False   /   unset, require=True
out    C:\dev\HSP-runs, no refusal   /   REFUSED, naming all three candidates
```

**R1219 — a relative value resolved against the process cwd**, so one declaration named
different worktrees depending on where it was started. It now anchors to the repository
root, which is a property of the declaration rather than of the caller's shell.

**R1220 — nothing exercised `hsp_pin.worktree`, which is why R1213, R1214 and R1219 were
all invisible.** `tests/unit/test_hsp_worktree_resolution.py`, 10 cases over the decision
table, every one on `tmp_path` so the file is green with no HSP checkout. Each repair is
held by the cycle FT2 asks for:

```
cmd    revert each repair in turn, run the file, restore
out    R1214's raise reverted          ->  2 failed, 8 passed
       R1213's name test disabled      ->  1 failed, 9 passed
       R1219's anchor removed          ->  1 failed, 9 passed   (the reviewer's cycle)
       restored                        ->  10 passed
```

**R1229 — and the first version of the R1213 test was a check that could not fail.** It
asserted the predicate's *source line* was present, so `if False and ...` left it passing
with the repair reverted. It now drives `preflight()`. The reviewer then found a second in
the same file — `assert not got.is_absolute() or True`, true for every input, eleven lines
below a docstring saying exactly that — which is deleted rather than repaired, because the
line above it is the real check. **Three of this shape in one session**: that one, the
source-text assertion, and a wait condition using `pgrep -f` that could not see a Windows
process and so reported success the moment it was armed. The common cause is asserting
from reading rather than running.

**R1226 — R1213 one key over.** `export_buoy_centers_ref.py` had no DS0 refusal at all, so
the stable key pointed at the **runs** tree regenerated `buoy_centers_ref.json` — EB6's
label-provenance input — while `provenance.source` declares `HSP-stable/...` as a literal
and `hsp_tag` is a module constant, neither of which can be wrong.

```
cmd    the reviewer's control, rerun with the predicate added
out    stable key -> HSP-runs    REFUSED: the STABLE key resolves to ...\HSP-runs, which
                                 is not an HSP-stable worktree ... records a source it
                                 did not read (R1226)
       stable key -> HSP-stable  EB6 reference: current. blob b8b8123904af, tag
                                 floatfea-ref-1, 12 buoys and 4 hubs.
```

Its second limb asked for one of two fixes and for the reason. **Chosen: hash the working
file** (`git hash-object`) rather than add `--dirty` to a describe. `build()` reads the
numbers from `source.read_text()`, so the recorded sha should describe the bytes the
snapshot came from; a `--dirty` marker would make the mismatch visible while still
publishing the wrong sha beside it.

**R1227 — R1206's fourth and fifth sites.** `assert STEP > 0` fired at step 0 with a
message asserting "no step has both" when step 0 has both, and being first in its test it
killed three later assertions — among them `STEP_REPORT - STEP <= 1`, the one that forbids
opening step k+1 over an unreviewed step k. It now tests `REPORTED & REVIEWED`, which is
the condition rather than a proxy for it. **`_PAIRED`'s own `else 0` is raised with the
reviewer rather than silently changed**, together with its measurement that `marker 0` and
`marker 3` both give `STEP 0` — i.e. the plan marker currently has no effect on which
report the guard reads. That is a larger claim than R1227 and I have not acted on it.

**R1221 — the Carried gate was parametrised over phantom ids.** `\bR\d+\b` cannot tell a
finding id from a milestone label in a repository whose milestones are `R1` and `R2`; in
the F-era it could not fire, because `F6` does not match. Eleven matches in one verdict's
Carried section were the label or a path, and one of those paths is R1205's own site, so
no wording on the reviewer's side could avoid them. `_mentions()` filters the milestone
names themselves rather than imposing a digit count, which would silently drop a real
two-digit finding — CLAUDE.md cites R29.

**R1228 — a quotation whose rule moved underneath it.**
`tests/test_report_guard_states.py:117` quoted the `STEP` expression that R1206 changed one
file over. Regenerated in the same commit as the change, which is what BP0 requires.

**R1225 (ii) — the environment is now recorded in the provenance**:
`determinism.report()`, `OPENBLAS_CORETYPE`, the six library versions, and
`BASELINE_CONDITIONS` beside them. Both halves already existed in
`floatfea/determinism.py` and nothing in the export path called either. Recorded, **not
asserted** — a refusal against a differing environment is FQ3's case, not a gate failure.

**R1222 and R1224 are the reviewer's own** — a prediction it confirmed green, and a
correction it made to its own reasoning. Recorded; no action here.

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
judge  **ROUND-OFF, ON THE ONE CASE MEASURED.** ~200 eps over 884 timesteps of a
       sequential convolution sits inside the `sqrt(N)*eps = 30` to `N*eps = 884` band
       such an accumulation is bounded by, and twelve decades below the `1e-3` R1225 (i)
       named as the threshold for a larger finding. On this case nothing published can
       move: the governing utilisation is quoted to six figures and the perturbation is
       at the fourteenth.
       **AND THE SCOPE OF THAT SENTENCE IS NARROWER THAN REVISION 1 CLAIMED (R1233).**
       `--check` names 36 arrays across SIX cases; this measures three arrays of ONE.
       Revision 1 wrote "so no published number can move", which is a claim over six
       periods supported by one. It is not a condition of step 0, because option 2 is
       not being taken -- but it IS a condition of CHOOSING option 2, and whoever takes
       that option measures all six first.
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

*`scripts/check_carried.py` caught this section short by eleven ids on its first pass —
R1213, R1214, R1215, R1221, R1222, R1223, R1225, R1226, R1227, R1228, R1229 — because it
listed verdict 59's findings and not those of verdicts 60, 61 and 62. **That the gate
could catch it is the measurement that R1205's repair landed**: before it, the same gate
reported on `docs/reports/F2/step-4.md` and exited 0 about a milestone closed a year ago.*

| id | state | where |
|---|---|---|
| R1213 | **answered** | §6a — the DS0 name test beside the identity test, with the refusal pasted |
| R1214 | **answered** | §6a — set-and-wrong refuses, unset falls through, both directions |
| R1215 | **answered** | the marker comment in `docs/milestones/R2.md` now says what the marker says |
| R1216 | **answered** | `docs/milestones/R2.md` §2c — the census before *and* after |
| R1219 | **answered** | §6a — a relative key anchors to the repo root, not the cwd |
| R1220 | **answered** | §6a — `tests/unit/test_hsp_worktree_resolution.py`, with the revert-red-restore cycles |
| R1221 | **answered** | §6a — `_mentions()` filters milestone labels; the gate's own defect, FF0 |
| R1222 | reviewer-side, confirmed green | the reviewer's own prediction; no action here |
| R1223 | **open — escalated with R1225** | §7(1). Downstream of the staleness red; clears when the npz question is decided. NOT repaired by regenerating the deliverable to match a red gate |
| R1224 | reviewer-side correction | the reviewer's own; recorded, no action here |
| R1225 | **open — ESCALATED UNDER FQ3** | §7(1). (i) the magnitude is measured: 197 eps. (ii) the environment is now in the provenance. (iii) the frame is FQ3, not §6 item 2 |
| R1226 | **answered** | §6a — the stable key refuses a non-`HSP-stable` tree; sha from the bytes read |
| R1227 | **answered** | §6a — `STEP > 0` → `REPORTED & REVIEWED`; `_PAIRED` raised for the reviewer to rule |
| R1228 | **answered** | §6a — the quoted expression regenerated with the rule that moved (BP0) |
| R1229 | **answered** | §6a — the assertion that could not fail is deleted |
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

**THIS SECTION WAS WRONG IN BOTH DIRECTIONS IN REVISION 1 AND R1236 IS THE FINDING.** It
predicted that `test_the_plan_names_the_step_under_execution` would "stay red on the
sentinel collision" — it **passes** (`1 passed`, measured), because R1206's exit (iii)
landed in the same commit and the prediction was written before that and never
regenerated. And it omitted the reds that actually block. A red trace that predicts a red
which does not exist, while leaving out the ones that do, is worse than no trace: EG3 (i)
asks for every red traced by name, and this one was wrong at both ends.

The reds at this revision, traced rather than predicted:

* `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` — the FQ3 escalation in
  §7(1). Recorded red with its cause named; it does not clear until the toolchain
  question is decided, and no edit of mine can clear it.
* `tests/regression/test_f6_deliverable_agrees_with_itself.py` (R1223) — downstream of
  the same cause, and **not** to be cleared by regenerating the deliverable against a
  red gate.
* `test_the_answered_verdict_is_the_NEWEST_one` (R1230) and the four generated-section
  guards (R1231) — **both blocking, both CZ1 (iv), and both answered in revision 2
  below.** They fail the FS1/FT1 predicate in both limbs, which is why they are repairs
  and not waivers.
* `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` was already red at `251af69`, before
  this turn began — measured in a detached worktree at that commit, `1 failed in 0.34s`.
  Its subject is its own commit's CI run, which is FT1 limb two.

<!-- WHOLE_SUITE -->

## 10. CI at the judged commit

*Revision 1 left this a placeholder, which is R1231. The generated sections are in
revision 2's §13 and §14, anchored on the header that revision corrects.*

# Revision 2 — R1230 and R1231, and the generated sections this report owed

Answers: verdict 63 @ 0c5c864
Answers file: `docs/reports/R2/step-0-answers.json`

**2026-11-17. THE SCHEDULE is unchanged: GI sets no date, and GI6 stops the milestone at
step 0's report.** This revision exists because revision 1 shipped a header naming the
wrong verdict and three unfilled generated sections. Step 0 stands at **2 of 3** under
ES0 after it. This is the one hand-written paragraph the revision gets.

## 11. R1230 — the `Answers:` header named verdict 61 while the newest was 62

```
claim  revision 1's header named the newest verdict
cmd    git show 4c19570:docs/reports/R2/step-0.md | sed -n '5p'
out    Answers: verdict 61 @ c931885
cmd    grep -c "verdict 62\|0901933\|9e1092a" <that file>
out    0
rule   tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one, and
       scripts/ci_section.py:203 _anchor(), which read the same line
judge  **AND I TOLD THE REVIEWER THE OPPOSITE.** My invocation said "The report's
       `Answers:` header names verdict 62 and `0901933`, as your closing note required."
       It did not. I asserted it from memory without running `sed -n '5p'` -- the same
       failure as the thread-count diagnosis in §7 and the three checks that could not
       fail in §6a. Fourth time in one step: asserting from reading rather than running.
       IT IS NOT COSMETIC. `EXPECTED`, the domain of
       `test_the_report_carries_the_finding`, is computed from the verdict the header
       NAMES, and `_verdict_text_at` reads that file as it stood at that sha:
         ANSWERED = c931885  ->  EXPECTED = 27 ids, and R1225, R1226, R1227, R1228 and
                                 R1229 are NONE of them
         ANSWERED = 0901933  ->  EXPECTED = 32, the five added being exactly those
       So a revision answering nothing about either of verdict 62's blocking findings
       would have read GREEN on the gate whose only job is the dependency list. This
       revision's header names verdict 63 at `0c5c864`, the newest, and §12 carries it.
```

## 12. Carried — verdict 63

*`check_carried.py` reads the NEWEST revision's Carried section, so this table is
self-contained rather than a delta on §8. It caught this section short twice — once in
revision 1 and once here — and both times the omission was real.*

```
claim  this table carries every finding the newest verdict declares
cmd    python scripts/check_carried.py
out    check_carried: all 22 findings carried        (exit 0)
       before the rows below were completed, the same command printed:
         omits R1205, R1206, R1207, R1208, R1213, R1214, R1215, R1222, R1223, R1225,
         R1226, R1227, R1229 -- verdict declares 22 findings; 9 are carried
rule   BS0 -- CLAUDE.md requires the next report's Carried section to list every open
       item, and BS0 makes that a build failure rather than a review finding
judge  **THAT THIS GATE CAN CATCH ANYTHING IS THE MEASUREMENT THAT R1205'S REPAIR
       LANDED.** Before it, the same command resolved to `docs/reports/F2/step-4.md`,
       named seven findings from a milestone closed a year ago, and exited 0 -- green
       about the wrong milestone. It is now correct about R2, and the first two things
       it did were catch this section short.
```

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R835 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1186 | **later** — §16 | (c), R1190, R1191, R1193 -- still open, routed to R2 by verdict 58 item 3. R1193 (the dead... |
| R1188 | **later** — §16 | (c), R1190, R1191, R1193 -- still open, routed to R2 by verdict 58 item 3. R1193 (the dead... |
| R1189 | **later** — §16 | (c), R1190, R1191, R1193 -- still open, routed to R2 by verdict 58 item 3. R1193 (the dead... |
| R1190 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1191 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1193 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1196 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1197 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1198 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1199 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1200 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1201 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1202 | **answered** — §16 | (FF0, the base-case sha at five sites) -- ANSWERED before this commit, at bb952e7 (closure:... |
| R1203 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1204 | **later** — §16 | no clause this generator can cut -- see the verdict's Carried section |
| R1205 | **answered** — §16 | carried, and the verdict says nothing further about it here |
| R1206 | **open** — §16 | carried, and the verdict says nothing further about it here |
| R1207 | **answered** — §16 | carried, and the verdict says nothing further about it here |
| R1208 | **answered** — §16 | carried, and the verdict says nothing further about it here |
| R1213 | **answered** — §16 | The DS0 refusal in run_floatsim_design_waves.py DOES NOT FIRE on the input this diff newly... |
| R1214 | **answered** — §16 | A key that is SET BUT WRONG is silently discarded and a different worktree is used. claim what... |
| R1215 | **answered** — §16 | docs/milestones/R2.md:5 says the marker reads 1 while :3 reads 0, and calls the shipped state... |
| R1221 | **answered** — §16 | The Carried gate is parametrised over PHANTOM finding ids -- R2, and R1 too -- and no wording... |
| R1222 | **later** — §16 | test_a_blocking_item_is_not_routed_to_4a is red because verdict 59 wrote its dispositions as... |
| R1223 | **open** — §16 | A PUBLISHED DELIVERABLE no longer regenerates from this tree, and the two rows that moved are... |
| R1225 | **open** — §16 | THE --check REFUSAL IS NOT THREAD COUNT. The npz golden moved when THIS REPOSITORY'S OWN... |
| R1226 | **answered** — §16 | R1213 ONE KEY OVER: NOTHING TIES THE TREE THE STABLE KEY NAMES TO THE TREE THE SNAPSHOT... |
| R1227 | **answered** — §16 | R1206's FOURTH SITE: tests/test_report_carried.py:579 still reads assert STEP > 0, and it goes... |
| R1228 | **answered** — §16 | tests/test_report_guard_states.py:117 quotes the expression this commit changed. It reads "The... |
| R1229 | **answered** — §16 | tests/unit/test_hsp_worktree_resolution.py:123 IS AN ASSERTION THAT CANNOT FAIL, and it is the... |
| R1230 | **answered** — §11 | THE Answers: HEADER NAMES VERDICT 61 WHILE THE NEWEST IS 62, AND THE GATE'S FINDING SET IS... |
| R1231 | **answered** — §13 | ALL THREE GENERATED SECTIONS ARE UNFILLED PLACEHOLDERS, AND CI IS RED AT THIS COMMIT, WHICH IS... |
| R1232 | **open** — §16 | R1225 (ii) IS RECORDED AND NOT HELD, AND pin_threads() CANNOT BE WIRED AT THE CALL SITE THE... |
| R1233 | **answered** — §16 | R1225 (i) IS SATISFIED FOR THE RULING AND NOT FOR THE SENTENCE IT IS USED TO SUPPORT. ~200 eps... |
| R1234 | **later** — §16 | tests/test_report_vocabulary_corpus.py HAS TWO NEW REDS AND THEY ARE MINE, NOT YOURS. cmd... |
| R1235 | **answered** — §16 | R1221 AND R1228 ARE UNCHANGED. Verdict 62's item 5 read "R1227 and R1228 in the next commit... |
| R1236 | **answered** — §16 | TWO FIGURES IN THE REPORT THAT ONE COMMAND EACH REFUTES. Section 6's R1205 block pastes out... |

## 13. Runs since the commit verdict 63 judged

*R1231: revision 1 left this a placeholder. Generated, not written.*

## 0a. Runs since the commit verdict 63 judged

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py --rounds`, anchored on verdict 63 at `4c19570` through the report's own `Answers:` line. Every run whose head is a commit in this round, from `gh run list --json databaseId,event,conclusion,status,headSha`. A run that reached no conclusion ABOUT THE CODE -- cancelled, or still running -- has **no result** and no job lines: it reached no verdict on anything, so no reason is attributed to it. A cancelled run IS `completed`, which is why the test is the conclusion and not the status (CX0, R449, R1130).

| run | event | head | outcome |
|---|---|---|---|
| `44140076843` | push | `4c19570` | conclusion **failure** |
| `44145793006` | push | `0c5c864` | **no result** (status `in_progress`) |

**Run `44140076843`, conclusion **failure**: 147 failing test name(s) in the log.**
- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1197]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1198]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1199]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1200]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1213]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1214]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1215]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1221]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1223]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_carried_item_carries_one_of_the_report_words` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-.claude/hooks/require-verdict.sh:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F2.md:10]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F3.md:9]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F6a.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-R1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/milestones/R1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/milestones/R1.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/reports/F2/step-4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/reviews/F2/step-4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:98]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:99]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:100]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:101]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:102]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:135]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-tests/test_report_carried.py:608]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1206-tests/corpus/plan_step_marker_resolution.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1206-tests/test_report_carried.py:639]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-data/f4/dynamic_inputs.npz]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-data/platform/platform12_deck.yaml]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-export_f4_dynamic_inputs.py:390]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:467]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:468]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:469]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:470]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:471]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:472]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:474]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:475]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:476]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:477]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:478]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-HSP-stable/studies/platform-12buoy/platform_common.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-export_platform_deck.py:75]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-report_joint_reactions.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-run_floatsim_design_waves.py:98]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/export_buoy_centers_ref.py:42]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/export_platform_deck.py:45]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/measure_platform_joints.py:48]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/report_joint_reactions.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/run_floatsim_design_waves.py:50]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/run_floatsim_design_waves.py:51]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-R2.md:253]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-R2.md:366]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-docs/hsp-coupling.md:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-export_platform_deck.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-report_joint_reactions.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-report_joint_reactions.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-run_floatsim_design_waves.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-docs/hsp-coupling.md:45]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:91]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:94]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:100]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-dynamic_inputs.npz]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:467]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:468]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:469]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:470]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:471]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:472]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:474]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:475]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:476]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:477]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:478]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-hsp_pin.py:20]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-report_joint_reactions.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-scripts/export_f4_dynamic_inputs.py:435]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-scripts/report_joint_reactions.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-tests/verification/rung4/test_f4_g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-tests/verification/rung4/test_f4_g41_dynamic.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-docs/milestones/R1.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:387]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:388]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:389]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:390]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:423]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:424]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:425]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:427]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:428]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1223-tests/regression/test_f6_deliverable_agrees_with_itself.py:317]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[(preamble)]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[2. GI3(a) \u2014 inertial versus joint reacti]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[3. GI3(b) \u2014 wall time of one FloatSim ru]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[6. The four blocking findings of the pla]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[7. ESCALATION \u2014 TWO items, Xabier's]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[8. Carried]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[9. The marker, and the two reds this rep]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_a_table_of_numbers_shows_where_it_came_from[8. Carried]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

## 14. CI at the judged commit, and the whole suite

## 0. CI at `4c19570`, the commit verdict 63 judged — conclusion **FAILURE**

<!-- generated: scripts/ci_section.py -->

Generated: `python scripts/ci_section.py`, anchored on verdict 63 at `4c19570` through the report's own `Answers:` line. Run `44140076843`, event `push`, conclusion **failure**.

| job | passed | failed | skipped |
|---|---|---|---|
| the verification ladder | 2143 | 1 | 0 |
| lint, unit and guards | 1103 | 146 | 1 |
| CI determinism -- leg | 0 | 0 | 0 |
| CI determinism -- ten legs agree | 0 | 0 | 0 |

**Job conclusions: 4 jobs, 2 not green.**

**2 job(s) SKIPPED, so unavailable rather than passing:** `CI determinism -- leg`, `CI determinism -- ten legs agree`. A skipped job measured nothing; its zeros are an absence of evidence and not a pass.

- the verification ladder (failure)
- lint, unit and guards (failure)

**Failing tests named in the log: 147.**

- `tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1197]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1198]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1199]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1200]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1213]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1214]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1215]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1221]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1222]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_the_finding[R1223]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_carried_item_carries_one_of_the_report_words` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_generator_would_catch_a_row_under_the_wrong_number` (lint, unit and guards)
- `tests/test_report_carried.py::test_there_are_pointers_to_resolve` (lint, unit and guards)
- `tests/test_report_carried.py::test_a_carried_row_points_at_a_section_that_discusses_it[(none)]` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_CI_SECTION` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_paragraph` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_report_carries_a_WHOLE_SUITE_count` (lint, unit and guards)
- `tests/test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-.claude/hooks/require-verdict.sh:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F2.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F2.md:10]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F3.md:9]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-F6a.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-R1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/milestones/R1.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/milestones/R1.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/reports/F2/step-4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-docs/reviews/F2/step-4.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:126]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:127]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:128]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:129]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/check_carried.py:130]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:98]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:99]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:100]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:101]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:102]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:103]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:104]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:105]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-scripts/ci_section.py:135]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1205-tests/test_report_carried.py:608]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1206-tests/corpus/plan_step_marker_resolution.txt]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1206-tests/test_report_carried.py:639]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-data/f4/dynamic_inputs.npz]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-data/platform/platform12_deck.yaml]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-export_f4_dynamic_inputs.py:390]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:467]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:468]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:469]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:470]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:471]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:472]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:474]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:475]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:476]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:477]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:478]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1207-scripts/export_f4_dynamic_inputs.py:479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-HSP-stable/studies/platform-12buoy/platform_common.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-export_platform_deck.py:75]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-report_joint_reactions.py:106]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-run_floatsim_design_waves.py:98]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/export_buoy_centers_ref.py:42]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/export_platform_deck.py:45]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/measure_platform_joints.py:48]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/report_joint_reactions.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/run_floatsim_design_waves.py:50]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1208-scripts/run_floatsim_design_waves.py:51]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-R2.md:253]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-R2.md:366]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-docs/hsp-coupling.md:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-export_platform_deck.py:77]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-report_joint_reactions.py:109]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-report_joint_reactions.py:121]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1213-run_floatsim_design_waves.py:138]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-data/platform/buoy_centers_ref.json]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-docs/hsp-coupling.md:45]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:91]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:92]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:94]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:95]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1214-floatfea/hsp_pin.py:100]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-dynamic_inputs.npz]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:467]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:468]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:469]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:470]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:471]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:472]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:473]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:474]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:475]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:476]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:477]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:478]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-export_f4_dynamic_inputs.py:479]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-hsp_pin.py:20]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-report_joint_reactions.py:96]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-scripts/export_f4_dynamic_inputs.py:435]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-scripts/report_joint_reactions.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-tests/verification/rung4/test_f4_g41_dynamic.py]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1215-tests/verification/rung4/test_f4_g41_dynamic.py:321]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-CLAUDE.md]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-docs/milestones/R1.md:3]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:387]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:388]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:389]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1221-tests/test_report_carried.py:390]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:423]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:424]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:425]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:426]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:427]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1222-tests/test_report_carried.py:428]` (lint, unit and guards)
- `tests/test_report_carried.py::test_every_named_site_is_touched_or_declared[R1223-tests/regression/test_f6_deliverable_agrees_with_itself.py:317]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[non_numeric_step_suffix]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[superscript_digit_step_number]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[draft_suffix_beside_a_step_report]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[step_number_is_the_empty_string]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[verdict_amended_after_the_commit_the_report_answers]` (lint, unit and guards)
- `tests/test_report_guard_states.py::test_the_guard_survives_the_state[zero_padded_step_number]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[(preamble)]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[2. GI3(a) \u2014 inertial versus joint reacti]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[3. GI3(b) \u2014 wall time of one FloatSim ru]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[6. The four blocking findings of the pla]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[7. ESCALATION \u2014 TWO items, Xabier's]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[8. Carried]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_every_number_in_prose_is_sourced_in_its_own_section[9. The marker, and the two reds this rep]` (lint, unit and guards)
- `tests/test_report_numbers_are_sourced.py::test_a_table_of_numbers_shows_where_it_came_from[8. Carried]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[legitimate_open_row]` (lint, unit and guards)
- `tests/test_report_vocabulary_corpus.py::test_the_guard_rules_on_the_spelling[two_spaces_before_the_item_number]` (lint, unit and guards)
- `tests.regression.test_f6_deliverable_agrees_with_itself::test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree` (the verification ladder)

### The whole-suite count, and why it is not in this commit

`test_the_report_carries_a_WHOLE_SUITE_count` is **red here, and FT1 names it as limb two
of the boundary predicate by construction**: `scripts/suite_count.py` measures a clean
worktree AT a commit, and the line naming that commit's sha cannot be inside the sha it
names. FT1's own wording — *"a red whose SUBJECT IS THE COMMIT CARRYING IT is a boundary
red"* — is written for this test and one other. It is recorded red with its cause named,
which is what EG3 asks, and it is not waived on a list: the predicate is applied to it
individually and it satisfies limb two.

What *can* be measured before the commit is the selection, and it is in §14's generated
table: the verification ladder at `4c19570` ran **2143 passed, 1 failed** — that one
failure is the staleness guard, which is the FQ3 escalation in §7(1) — and
`lint, unit and guards` ran **1103 passed, 146 failed, 1 skipped**, the reds being the
report guards this revision is repairing.

## 15. Every site verdict 63 names that this commit does not touch

*`test_every_named_site_is_touched_or_declared` gives a deliberate escape hatch -- the
report may write `no change` beside the exact site -- and its docstring says what it is
for: "FIVE consecutive rounds closed a site-naming condition at some of its sites and
recorded it as answered". Half of an item is not the item.*

```
claim  every site the newest verdict names is either touched by this diff or declared
cmd    the gate's own SITES list, against `git diff 0c5c864 -U0` on this tree
out    224 sites named, 13 touched, 211 declared below
rule   tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
judge  GENERATED, not typed. 211 rows written by hand is exactly how the five rounds
       that test's docstring describes went wrong, so this reads the SAME `SITES` the
       gate reads rather than reimplementing the pattern and getting a different answer
       from the thing it has to satisfy. Most of these are citations -- `CLAUDE.md`,
       earlier verdicts, files the finding quotes for context -- rather than sites
       needing a repair; the ones that needed one are in sec.6a and the 13 touched.
```

| finding | site | state |
|---|---|---|
| R1205 | `.claude/hooks/require-verdict.sh:105` | **no change** |
| R1205 | `CLAUDE.md` | **no change** |
| R1205 | `F2.md` | **no change** |
| R1205 | `F2.md:10` | **no change** |
| R1205 | `F3.md:9` | **no change** |
| R1205 | `F6a.md:3` | **no change** |
| R1205 | `R1.md` | **no change** |
| R1205 | `docs/milestones/R1.md` | **no change** |
| R1205 | `docs/milestones/R1.md:3` | **no change** |
| R1205 | `docs/milestones/R2.md` | **no change** |
| R1205 | `docs/reports/F2/step-4.md` | **no change** |
| R1205 | `docs/reviews/F2/step-4.md` | **no change** |
| R1205 | `scripts/check_carried.py` | **no change** |
| R1205 | `scripts/check_carried.py:126` | **no change** |
| R1205 | `scripts/check_carried.py:127` | **no change** |
| R1205 | `scripts/check_carried.py:128` | **no change** |
| R1205 | `scripts/check_carried.py:129` | **no change** |
| R1205 | `scripts/check_carried.py:130` | **no change** |
| R1205 | `scripts/ci_section.py` | **no change** |
| R1205 | `scripts/ci_section.py:98` | **no change** |
| R1205 | `scripts/ci_section.py:99` | **no change** |
| R1205 | `scripts/ci_section.py:100` | **no change** |
| R1205 | `scripts/ci_section.py:101` | **no change** |
| R1205 | `scripts/ci_section.py:102` | **no change** |
| R1205 | `scripts/ci_section.py:103` | **no change** |
| R1205 | `scripts/ci_section.py:104` | **no change** |
| R1205 | `scripts/ci_section.py:105` | **no change** |
| R1205 | `scripts/ci_section.py:106` | **no change** |
| R1205 | `scripts/ci_section.py:135` | **no change** |
| R1205 | `tests/test_report_carried.py:608` | **no change** |
| R1206 | `docs/milestones/R2.md` | **no change** |
| R1206 | `tests/corpus/plan_step_marker_resolution.txt` | **no change** |
| R1206 | `tests/test_report_carried.py:617` | **no change** |
| R1206 | `tests/test_report_carried.py:639` | **no change** |
| R1207 | `data/f4/dynamic_inputs.npz` | **no change** |
| R1207 | `data/platform/platform12_deck.yaml` | **no change** |
| R1207 | `export_f4_dynamic_inputs.py:390` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:467` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:468` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:469` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:470` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:471` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:472` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:473` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:474` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:475` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:476` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:477` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:478` | **no change** |
| R1207 | `scripts/export_f4_dynamic_inputs.py:479` | **no change** |
| R1208 | `HSP-stable/studies/platform-12buoy/platform_common.py` | **no change** |
| R1208 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1208 | `export_platform_deck.py:75` | **no change** |
| R1208 | `report_joint_reactions.py:106` | **no change** |
| R1208 | `run_floatsim_design_waves.py:98` | **no change** |
| R1208 | `scripts/export_buoy_centers_ref.py:42` | **no change** |
| R1208 | `scripts/export_platform_deck.py:45` | **no change** |
| R1208 | `scripts/measure_platform_joints.py:48` | **no change** |
| R1208 | `scripts/report_joint_reactions.py:96` | **no change** |
| R1208 | `scripts/run_floatsim_design_waves.py:50` | **no change** |
| R1208 | `scripts/run_floatsim_design_waves.py:51` | **no change** |
| R1213 | `R2.md:253` | **no change** |
| R1213 | `R2.md:366` | **no change** |
| R1213 | `docs/hsp-coupling.md:121` | **no change** |
| R1213 | `export_platform_deck.py:77` | **no change** |
| R1213 | `report_joint_reactions.py:109` | **no change** |
| R1213 | `report_joint_reactions.py:121` | **no change** |
| R1213 | `run_floatsim_design_waves.py` | **no change** |
| R1213 | `run_floatsim_design_waves.py:138` | **no change** |
| R1213 | `scripts/run_floatsim_design_waves.py:102` | **no change** |
| R1214 | `CLAUDE.md` | **no change** |
| R1214 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1214 | `docs/hsp-coupling.md:45` | **no change** |
| R1214 | `export_buoy_centers_ref.py` | **no change** |
| R1214 | `floatfea/hsp_pin.py:90` | **no change** |
| R1214 | `floatfea/hsp_pin.py:91` | **no change** |
| R1214 | `floatfea/hsp_pin.py:92` | **no change** |
| R1214 | `floatfea/hsp_pin.py:93` | **no change** |
| R1214 | `floatfea/hsp_pin.py:94` | **no change** |
| R1214 | `floatfea/hsp_pin.py:95` | **no change** |
| R1214 | `floatfea/hsp_pin.py:96` | **no change** |
| R1214 | `floatfea/hsp_pin.py:97` | **no change** |
| R1214 | `floatfea/hsp_pin.py:98` | **no change** |
| R1214 | `floatfea/hsp_pin.py:99` | **no change** |
| R1214 | `floatfea/hsp_pin.py:100` | **no change** |
| R1214 | `floatfea/hsp_pin.py:101` | **no change** |
| R1215 | `R2.md` | **no change** |
| R1215 | `docs/milestones/R2.md` | **no change** |
| R1215 | `docs/milestones/R2.md:5` | **no change** |
| R1215 | `dynamic_inputs.npz` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:467` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:468` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:469` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:470` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:471` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:472` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:473` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:474` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:475` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:476` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:477` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:478` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:479` | **no change** |
| R1215 | `floatfea/hsp_pin.py` | **no change** |
| R1215 | `hsp_pin.py:20` | **no change** |
| R1215 | `report_joint_reactions.py:96` | **no change** |
| R1215 | `scripts/export_f4_dynamic_inputs.py` | **no change** |
| R1215 | `scripts/export_f4_dynamic_inputs.py:435` | **no change** |
| R1215 | `scripts/report_joint_reactions.py` | **no change** |
| R1215 | `tests/verification/rung4/test_f4_g41_dynamic.py` | **no change** |
| R1215 | `tests/verification/rung4/test_f4_g41_dynamic.py:321` | **no change** |
| R1221 | `CLAUDE.md` | **no change** |
| R1221 | `docs/milestones/R1.md:3` | **no change** |
| R1221 | `docs/milestones/R2.md` | **no change** |
| R1221 | `docs/milestones/R2.md:12` | **no change** |
| R1221 | `tests/test_report_carried.py:387` | **no change** |
| R1221 | `tests/test_report_carried.py:388` | **no change** |
| R1221 | `tests/test_report_carried.py:389` | **no change** |
| R1221 | `tests/test_report_carried.py:390` | **no change** |
| R1222 | `tests/test_report_carried.py:423` | **no change** |
| R1222 | `tests/test_report_carried.py:424` | **no change** |
| R1222 | `tests/test_report_carried.py:425` | **no change** |
| R1222 | `tests/test_report_carried.py:426` | **no change** |
| R1222 | `tests/test_report_carried.py:427` | **no change** |
| R1222 | `tests/test_report_carried.py:428` | **no change** |
| R1223 | `hsp_pin.py` | **no change** |
| R1223 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:317` | **no change** |
| R1225 | `CLAUDE.md` | **no change** |
| R1225 | `R2.md` | **no change** |
| R1225 | `ci.yml:67` | **no change** |
| R1225 | `ci.yml:68` | **no change** |
| R1225 | `ci.yml:69` | **no change** |
| R1225 | `constraints-dev.txt` | **no change** |
| R1225 | `data/f4/dynamic_inputs.npz` | **no change** |
| R1225 | `dynamic_inputs.provenance.json` | **no change** |
| R1225 | `floatfea/determinism.py` | **no change** |
| R1225 | `floatfea/hsp_pin.py` | **no change** |
| R1225 | `pyproject.toml` | **no change** |
| R1225 | `results/F6/floatfea_results_report.md` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:476` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:477` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:478` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:479` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:480` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:481` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:482` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:483` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:484` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:485` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:486` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:487` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:488` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:489` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:490` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:491` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:492` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:493` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:494` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:495` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:496` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:497` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:498` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:499` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:500` | **no change** |
| R1225 | `tests/test_ci_canonical_environment.py` | **no change** |
| R1226 | `CLAUDE.md` | **no change** |
| R1226 | `HSP-stable/studies/platform-12buoy/platform_common.py` | **no change** |
| R1226 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1226 | `export_buoy_centers_ref.py` | **no change** |
| R1226 | `hsp_pin.py:36` | **no change** |
| R1226 | `hsp_pin.py:37` | **no change** |
| R1226 | `hsp_pin.py:38` | **no change** |
| R1226 | `hsp_pin.py:39` | **no change** |
| R1226 | `hsp_pin.py:40` | **no change** |
| R1226 | `hsp_pin.py:41` | **no change** |
| R1226 | `hsp_pin.py:42` | **no change** |
| R1226 | `hsp_pin.py:43` | **no change** |
| R1226 | `hsp_pin.py:44` | **no change** |
| R1226 | `hsp_pin.py:45` | **no change** |
| R1226 | `hsp_pin.py:46` | **no change** |
| R1226 | `run_floatsim_design_waves.py:112` | **no change** |
| R1226 | `scripts/export_buoy_centers_ref.py` | **no change** |
| R1226 | `scripts/export_buoy_centers_ref.py:172` | **no change** |
| R1227 | `test_report_carried.py:579` | **no change** |
| R1227 | `tests/test_report_carried.py:579` | **no change** |
| R1228 | `test_report_carried.py:236` | **no change** |
| R1229 | `test_report_numbers_are_sourced.py` | **no change** |
| R1229 | `tests/unit/test_hsp_worktree_resolution.py` | **no change** |
| R1229 | `tests/unit/test_hsp_worktree_resolution.py:123` | **no change** |
| R1230 | `CLAUDE.md` | **no change** |
| R1230 | `docs/reviews/R2/step-0.md` | **no change** |
| R1230 | `scripts/ci_section.py:203` | **no change** |
| R1230 | `tests/test_report_carried.py:406` | **no change** |
| R1230 | `tests/test_report_carried.py:407` | **no change** |
| R1230 | `tests/test_report_carried.py:408` | **no change** |
| R1230 | `tests/test_report_carried.py:409` | **no change** |
| R1230 | `tests/test_report_carried.py:410` | **no change** |
| R1230 | `tests/test_report_carried.py:411` | **no change** |
| R1230 | `tests/test_report_carried.py:412` | **no change** |
| R1230 | `tests/test_report_carried.py:514` | **no change** |
| R1231 | `CLAUDE.md` | **no change** |
| R1231 | `scripts/ci_section.py` | **no change** |
| R1232 | `floatfea/determinism.py` | **no change** |
| R1232 | `floatfea/determinism.py:96` | **no change** |
| R1232 | `scripts/export_f4_dynamic_inputs.py` | **no change** |
| R1233 | `results/R1/example/member_forces.csv` | **no change** |
| R1234 | `tests/corpus/report_status_vocabulary.txt` | **no change** |
| R1234 | `tests/test_report_vocabulary_corpus.py` | **no change** |
| R1236 | `R2.md` | **no change** |
| R1236 | `R2.md:15` | **no change** |

## 16. The carried items, and what each waits on

*Section 12 is the generated table; this is the section that does the work, because
`test_a_carried_row_points_at_a_section_that_discusses_it` forbids a row pointing at the
Carried table itself (R318: every row is in that table by construction, so such a pointer
resolves for every item and says nothing).*

**Answered in revision 1, and the answers stand.** R1205 (one live marker, `_active_step()`
to `('R2', 0)`), R1206 (exit (iii), and my escalation withdrawn because its premise was
unmeasured), R1207 (step 2's gate (ii) made a pair, (iii) read back from the npz), R1208
(two keys over seven assignments), R1213 (the DS0 name test beside the identity test),
R1214 (set-and-wrong refuses, unset falls through), R1215 (the marker comment), R1216 (the
census before and after), R1219 (relative keys anchored to the repo root), R1220 (the
resolver's ten tests with their revert-red-restore cycles), R1226 (the stable key refuses
a non-HSP-stable tree, sha taken from the bytes read), R1227 (`STEP > 0` to
`REPORTED & REVIEWED`), R1229 (the assertion that could not fail, deleted). Each is
measured in revision 1's sections 6 and 6a; nothing in revision 2 moved any of them.

**Answered in this revision.** R1221 and R1228 (R1235's point: they were due in the
commit that answered R1225, and they are in it now) -- `_mentions()` filters milestone
labels in BOTH the guard and `scripts/carried_table.py`, which is the second site and was
found by running the generator rather than reading it; and the quoted `STEP` expression
regenerated with the rule that moved. R1233 (the "no published number can move" sentence
narrowed to the one case measured, with all six periods made a condition of choosing the
re-base option). R1236 (the two stale figures: `('R2', 1)` corrected, and the red trace
rewritten after it predicted a red that passes while omitting the two that block).

**Open, and waiting on Xabier rather than on me.** R1225 and R1223 are one item: the
committed `dynamic_inputs.npz` does not regenerate from this tree, the difference is
round-off on the case measured, FQ3 already ruled that this is stop-and-report rather than
re-baseline, and R1223's deliverable red is downstream of the same cause. **The magnitude
and its command are in section 7**, which is where that figure is measured; it is cited by
name here rather than repeated, because a number restated away from its command is how a
figure goes stale. The decision between restoring the locked toolchain and accepting a
re-base is in section 7 with both costs. **R1232** stands for the write run and not for
this step: only `determinism.report()` is wired, because `pin_threads()` cannot be called
below the module's own `import numpy` -- its docstring says to call it first -- so wiring
it there would record a pinned thread count for a run whose BLAS had already initialised
at the ambient one, which is a false provenance field and worse than the null it replaces.

**Reviewer-side, recorded and not acted on.** **R1222** — the reviewer's own prediction
about its verdict heading format, which it then measured green at its own commit; and
**R1224** — its correction to its own reasoning about which test selections the diff could
reach, refuted by R1223. Both belong to the reviewer and neither asks anything of this
report beyond being carried, which is what §12 does.

**Open, and not mine to touch.** R1234, two vocabulary-corpus entries recorded
`measured=allowed` in a tree where the guard could not rule. That directory belongs to the
reviewer under BE3; the `PreToolUse` hook enforces it and refused one of my own paragraphs
until it went through the editing tool.

**Carried in from verdict 58, still open, and none of them a step-0 matter.** R835, R1186,
R1188, R1189, R1190, R1191, R1193, R1196, R1197, R1198, R1199, R1200, R1201, R1202, R1203,
R1204. Six are prose or one-line items in two files; R1193 and R1188 are discharged from
the reviewer's side (the dead corpus-pause clause, and GG3's per-commit concurrency group);
R1202 was answered before this milestone at `bb952e7`; R1203, R1204 and R835 are
reviewer-side or Xabier's. They carry to step 1, which GI6 holds.
