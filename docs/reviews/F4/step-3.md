# Review — F4 step 3
Reviewed commit: 9de3e4e9a8bc31caa1e22259d9d570c39d39c3b2
Verdict: HOLD
**Reviewed commit: `9de3e4e`** (`9de3e4e9a8bc31caa1e22259d9d570c39d39c3b2`, HEAD of F3
at the time I judged it, tree clean). **I committed no corpus this round** -- ES0's
light scope forbids a batch -- so the plain `Reviewed commit:` header above and the
commit I judged are the same sha here. That coincidence is R718's subject and not its
refutation.
Tests: 3244 passed, 0 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, in the repository itself, tree clean at
`9de3e4e9a8bc31caa1e22259d9d570c39d39c3b2`, `697.69s`. Not the report's figure -- there is
no report.)

## Round of 2026-10-07 -- ES0 INTERIM CHECK. COUNTS AGAINST NO ROUND. HOLD ON ONE ITEM.

**ES0's premise, computed rather than taken.**

```
cmd    ls docs/reports/F4/
out    preview-PRELIMINARY.md / step-1-answers.json / step-1.md / step-2-answers.json /
out    step-2.md
judge  THERE IS NO `step-3.md`. No new report revision exists, so ES0's exemption applies
       and this check counts against NONE of step 3's three revisions. Light scope: the
       suite and CI at the commit, plus a CZ0 (a)-(d) scan of the diff. No corpus batch,
       no closure list -- and I am honouring both of those literally.
cmd    git rev-list --count d4e2136..HEAD ; git log --oneline d4e2136..HEAD
out    8
out    9de3e4e / 4f0acfd / 4ed4399 / 27ecf62 / 4344495 / 4b64eaf / 9e59478 / b4aae36
judge  EIGHT, AND THE HAND-BACK'S COUNT IS RIGHT THIS TIME. Two of the eight are mine
       (`b4aae36` the verdict, `9e59478` the corpus). C21 does not recur.
```

**EU1, VERIFIED MYSELF RATHER THAN TAKEN, AND IT DOES NOT FIRE.**

```
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+][A-Za-z0-9_]+:"
out    (no output)
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+]" |
       grep -vE "^(\+\+\+|---)" | grep -E "Final|=\s*[0-9]"
out    (no output)
judge  53 lines of that file changed and NOT ONE is a declaration or carries a numeric
       assignment. No tolerance VALUE and no declared counter moved, so EU1's mandatory
       adversarial case is not owed. **I ran one anyway** -- the mapping family at all
       seven rungs and the DQ4(ii) boundary solved in both directions, sections 2 and 3 --
       because the thing EU1 is actually about is running the model at a configuration the
       diff did not choose, and that is free here.
```

**WHY IT IS A HOLD, IN ONE SENTENCE.** The two carried items are genuinely closed and I
reproduced both ablations to the digit. The HOLD is **R711**, and it is in the one place
the hand-back told me to look hardest: `scripts/measure/g41_dynamic.py` forms the
**continuous** balance `G^T lam - M a`, not the **discrete** one the plan locks twice and
names `newmark.py:414-437` for. Measured as window maxima with the script's own
denominators, the two quantities are **2.2e+13x apart on the force channel** and
**4.9e+02x apart on the moment channel**, and the locked force channel sits at round-off.
**Every ceiling derived from this script's output would be thirteen decades loose on a
channel that currently closes exactly.** The decomposition the hand-back worried about is
CORRECT; the numerator around it is not.

**No STOP.** The verification ladder is SUCCESS at the reviewed commit in CI, no low rung
is red, `.claude`, `docs/SUPERVISOR.md` and `tests/conftest.py` are untouched in this
range, and the plan is not wrong -- it is explicit about the discrete form in two places
and the script resolved its shorthand in the other direction.

## 0. CI -- COMPLETE AND FULLY GREEN AT THE REVIEWED COMMIT

The hand-back said there was no completed run in the range and asked me to read it myself.
**There are three, and the reviewed commit's is one of them.**

```
cmd    gh run list --commit 9de3e4e9a8bc31caa1e22259d9d570c39d39c3b2
         --json name,conclusion,workflowName,status,databaseId
out    [{"conclusion":"success","databaseId":37711840143,"name":"CI",
out      "status":"completed","workflowName":"CI"}]
cmd    gh run view 37711840143 --json jobs  (job conclusions)
out    the verification ladder                 success
out    lint, unit and guards                   success
out    CI determinism -- leg                   skipped   (CK0's workflow_dispatch, NOT CK2)
out    CI determinism -- ten legs agree        skipped
cmd    gh run view 37711840143 --json jobs  (the lint job's steps, CZ1 (iii)'s point)
out    actionlint success / ruff success / black --check success / mypy success /
out    unit tests success / guards and meta-tests SUCCESS
judge  **NOT a red, NOT unavailable, NOT CK2.** `guards and meta-tests` RAN rather than
       being skipped behind an earlier red step, which is the thing CZ1 (iii) exists to
       make visible. CA2 is satisfied on the commit I am judging. The run was
       `in_progress` when I was invoked and completed while I worked; an unfinished run is
       not a pass, so I waited rather than recording it as one.
```

**THE REST OF THE RANGE, READ BY ME AND NOT TAKEN.**

```
cmd    for s in 4f0acfd 4ed4399 27ecf62 4344495 4b64eaf 9e59478 b4aae36;
       do gh run list --commit $(git rev-parse $s) --json databaseId,status,conclusion; done
out    4f0acfd  37710650863  completed  SUCCESS
out    4ed4399  37710440855  completed  cancelled
out    27ecf62  (no run)
out    4344495  37584703093  completed  FAILURE
out    4b64eaf  37584514527  completed  cancelled
out    9e59478  37583792344  completed  cancelled
out    b4aae36  (no run)
judge  the three cancellations are the `concurrency: cancel-in-progress` rule and under
       CX0/R449 they reached no verdict on anything; no reason is attributed to them.
       `27ecf62` and `b4aae36` were not the head of their push, so no run was created --
       `docs/milestones/**` is NOT in `paths-ignore`, so this is the push head and not the
       path filter. **`4f0acfd` is a second fully green completed run**, and
       `git diff --name-only 4f0acfd..9de3e4e` is `scripts/measure/README.md` and
       `scripts/measure/g41_dynamic.py` ONLY -- so nothing under `floatfea/` or `tests/`
       at HEAD is unmeasured by a green run on a machine neither of us controls.
cmd    gh run view 37584703093 --log-failed  (the one FAILURE in the range, at 4344495)
out    1 tests/test_report_carried.py::test_the_plan_names_the_step_under_execution
out    17 tests/test_report_guard_states.py::test_the_guard_survives_the_state[...]
out      including [baseline], so the seventeen cascade off the one cause
judge  18 reds, ONE cause, and the hand-back's account of it is exact. It is in the range
       and it is NOT CZ0 (d): (d) is "a red test at the reviewed commit", the reviewed
       commit is `9de3e4e`, and the cause was reverted at `27ecf62` and measured green at
       `4f0acfd` and in my own run. **And the right thing was done with it** -- the guard
       refused, and the commit was reverted rather than the guard edited. That is the
       non-negotiable working.
```

## 1. MY OWN INSTRUCTIONS AND THE CONFTEST -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat d4e2136..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  NOT a STOP-class finding. Nothing in this range touches what I read, what I must
       carry or what I may write. Checked per commit as well: `4ed4399` is the one
       `process:` commit in the range and it touches `scripts/ci_section.py` and
       `tests/test_report_carried.py` only -- neither is under `.claude/` and neither is
       `docs/SUPERVISOR.md`, so the reviewer-instruction rule is not engaged by it.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py
cmd    git diff --stat d4e2136..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (empty)
judge  CI0's check resolves to a real file; it is unchanged and no new conftest or plugin
       appears anywhere under `tests/`. CH2's six channels are closed by reading, which is
       the only way they can be closed.
cmd    git diff --stat d4e2136..HEAD -- floatfea tests docs scripts .github data
out    docs/milestones/F4.md 75 | docs/reviews/F4/step-2.md 738 |
out    floatfea/tolerances.py 53 | scripts/ci_section.py 173 |
out    scripts/measure/README.md 42 | scripts/measure/g41_dynamic.py 303 |
out    tests/corpus/f4_mapping_wrong_node_injection_family.txt 105 |
out    tests/test_report_carried.py 36 |
out    tests/verification/rung4/test_f4_static_and_mapping.py 93
judge  **NOTHING under `floatfea/` moved except `tolerances.py`, and that only in
       comments.** There is no (a) in this range to find. Two of the nine paths are mine.
```

## 2. R710 -- CLOSED. THE ABLATION REPRODUCED, AND THE RUNG SWEEP WITH IT

```
cmd    python <my own loop: every ordered (a_node, b_node) pair of the four platform joint
                nodes, the shipped `_mapping_error`, the shipped `_synthetic_lam(16)` row>
rule   `F4_MAPPING_CONSERVATION_COUNTER = 0.2`, the smallest defect the gate must fail
out    len(family) = 12
out      3 -> 4   0.2179893030274107      4 -> 3   0.9326006752312858
out      2 -> 3   0.361471168710035       1 -> 2   0.9597085787263796  <- SHIPPED
out      1 -> 3   0.6264052990635567      2 -> 4   1.1789224535320926
out      4 -> 1   0.6551181588194337      4 -> 2   1.310236317638867
out      2 -> 1   0.8174512848220575      1 -> 4   1.5861138777899368
out                                       3 -> 2   1.6621665189226082
out                                       3 -> 1   1.6964643105279407
out    family min 0.2179893030274107  max 1.6964643105279407  spread 7.7823x
out    shipped pair rank by size: 7 of 12
out    counter 0.2 margin vs family min: 1.089947x
judge  EVERY FIGURE IN THE ENTRY AND IN THE PLAN ROW REPRODUCES TO THE DIGIT, including
       which pair is seventh. The twelve keys are distinct, so `len(family) == 12` really
       does assert four distinct nodes times three destinations.
cmd    python <the ablation the hand-back named: the counter set to 0.5, between the family
                minimum and the shipped pair, both forms applied verbatim>
out    single-pair form (0.9597085787263796 > 0.5) : True  -> PASSES, vacuously
out    family form      (0.2179893030274107 > 0.5) : False -> RED
judge  **THE ABLATION IS THE CLAIM AND IT HOLDS.** A counter at 0.5 is caught by the loop
       and was invisible to the single-pair form. BG0 satisfied: one variable moved.
cmd    python <the family minimum rebuilt at every rung of MASS_FRACTION_LADDER>
out    f = 0.75 / 0.5 / 0.4 / 0.3 / 0.2 / 0.1 / 0.0 : n = 12, min 0.2179893030274107 at
out      every rung, bit-identical
judge  the entry's ladder claim is correct, as it was last round, and the narrow
       coordinate really is the SITE. **R710 is CLOSED and does not carry.**
```

**BR0 honoured:** the plan row `docs/milestones/F4.md`'s `F4_MAPPING_CONSERVATION_COUNTER`
line moved in the same commit as the entry, carrying the same corrected figures. The value
did not move, which is the right outcome -- `0.2` was always below the family minimum.

## 3. R709 -- CLOSED, AND THE BOUNDARY SOLVED IN BOTH DIRECTIONS

The repair replaced both aggregates in the sign-flip branch with a per-body loop. The `min`
that feeds `error > counter` is kept, which is the correct direction for that assertion.

```
cmd    python <the shipped `_dq4_ii_departures` with one extra knob -- the translational
                rows scaled on the HUBS only, under the shipped sign flip -- then the OLD
                reduction and the SHIPPED per-body assertions applied verbatim>
rule   `F4_DQ4_ELEMENT_VECTOR` = 1.0e-12
out    hub force_scale   per-body force channel                 OLD (min<ceil)  CAUGHT ON
out    1.0 (clean)       platform 2.483527e-16, hub2 4.656613e-16,
out                      hub1/3/4 1.552204e-16                  PASSES          [] (right)
out    1.001             hubs 1.000000e-03, platform 2.484e-16  PASSES          4 hubs
out    2.0               hubs 1.000000e+00, platform 2.484e-16  PASSES          4 hubs
out    1e+06             hubs 9.999990e+05, platform 2.484e-16  PASSES          4 hubs
out    per-body moment channel, clean: platform 2.0000000000000004, hubs 2.000000000000001
judge  **THE HAND-BACK'S CLAIM IS EXACT.** A hub-only force error of `1.0e-3` relative
       passed the old form and is caught on all four hubs by the per-body form, and the
       clean case still passes on all five. The moment assertion is now per body too,
       which is strictly stronger than `min == approx(2.0)`.
cmd    python <bisection on the hub-only force scale against the shipped assertion>
rule   invert the decision rule and solve for the boundary, both directions (EH4)
out    smallest hub-only defect CAUGHT : force_scale 1.0000000000009999, reads 1.000240e-12
out    largest  hub-only defect MISSED : force_scale 1.0000000000009996, reads 9.999300e-13
out    clean max over the five bodies  : 4.656613e-16
out    clean sits inside the ceiling by: 2147.5x
judge  the boundary is the ceiling itself, to four digits, and the clean case clears it by
       `2147.5x`. The weakening direction -- the one that makes the gate look good -- is
       that the detection threshold is no longer infinite on four of five bodies; it is
       `1e-12` on every one. **R709 is CLOSED and does not carry.**
```

## 4. R711 -- THE NUMERATOR IS THE CONTINUOUS BALANCE, NOT THE DISCRETE ONE. THIS IS THE HOLD

**First, the part the hand-back asked me to attack, which is CORRECT.**
`per_joint_contributions` is exact and its slicing is right.

```
cmd    python <solve_one(T_full=14 model, 2 s, dt 0.01) with ER0's override, then compare
                sum_j contrib[j] against g.T @ lam, and map which bodies each joint touches>
out    jacobian shape (64, 102)   lam shape (64,)   64 % ROWS_PER_JOINT(4) == 0
out    n_joints implied 16   n_dof 102 == 6 * 17 bodies
out    DECOMPOSITION max|sum_j contrib - g.T lam| / max|g.T lam| = 2.8690569390046337e-18
out    joint 0..2 -> buoy/hub1 ; joint 3 -> hub1/platform ; ... joint 15 -> hub4/platform
out    sum|F_j| vs |sum F_j| :  hub1 37.3x  hub2 10.9x  hub3 41.9x  hub4 10.9x
out                             platform 24.1x
judge  **THE DECOMPOSITION IS SOUND AND THE DENOMINATOR DOES WHAT EV1 WANTS.** `g.T lam`
       is linear in the rows, each joint's rows touch exactly two bodies, and the
       magnitude sum is 10.9x to 41.9x the magnitude of the sum -- so cancellation cannot
       shrink it, which is the whole property the single-scalar form lacked. The worry in
       the hand-back is answered: the denominator is right.
```

**And then the numerator, which is not what the plan locks, and not what the file says it
is.** `scripts/measure/g41_dynamic.py:218-234` forms, per body,

    resid = (jacobian(xi[n]).T @ lam[n])[6k:6k+6]  -  (M_plus_Ainf @ xi_ddot[n])[6k:6k+6]

`scripts/report_joint_reactions.py:318-319` -- the function this script's docstring at
`:23` names as its own form -- forms

    resid = a_eff @ xi_ddot[n] - jacobian(0.5*(xi[n-1]+xi[n])).T @ lam[n] - rhs

with `a_eff = (1-alpha_m) M_eff + (1-alpha_f) h^2 beta C` and `rhs` carrying the external
force, both damping terms, `alpha_m M_eff xi_ddot[n-1]` and the memory `mu[n-1]`.

```
cmd    sed -n '408,440p' ../HSP-runs/floatsim/solver/newmark.py
out    rhs = (1-alpha_f) F_np1 + alpha_f F_n - alpha_m (M_eff @ xi_ddot_n)
out          - (1-alpha_f) (C @ xi_pred) - alpha_f (C @ xi_n) - mu_n
out    "G is evaluated at the step MIDPOINT (x_n + x_{n+1})/2 for energy consistency
out     with the trapezoidal balance"
rule   docs/milestones/F4.md:131 "the residual keeps the DISCRETE form already locked";
       :486 the gate's `# expected:` source is "the discrete balance `newmark.py:414-437`,
       re-formed independently"
judge  BOTH CITATIONS RESOLVE, and the solver says in its own comment that `G` is at the
       MIDPOINT. The script uses `jacobian(xi[n])`.
cmd    python <one solve, T_full = 14, 12 s, dt 0.01, ER0's override; at the last step,
                every term the g41 numerator omits, on the five FE bodies>
out    body       |locked|      |g41|       ext     Cterm        mu      amMa   g_mid-g_now
out    platform  1.0103e-04  2.5373e-01  0.00e+00  0.00e+00  0.00e+00  5.280e+00  3.008e-05
out    hub1      4.8918e-06  1.5060e-01  0.00e+00  0.00e+00  0.00e+00  3.124e+00  6.538e-04
out    hub2      6.5742e-06  1.5059e-01  0.00e+00  0.00e+00  0.00e+00  3.124e+00  2.357e-04
out    hub3      1.3613e-06  1.5058e-01  0.00e+00  0.00e+00  0.00e+00  3.124e+00  2.828e-05
out    hub4      6.5742e-06  1.5059e-01  0.00e+00  0.00e+00  0.00e+00  3.124e+00  2.357e-04
out    A_inf contribution on all five FE bodies: 0.000e+00
judge  **THE FE BODIES ARE DRY, AS EK0(a) SAYS**: `ext`, the damping term, `mu` and the
       added-mass contribution are each IDENTICALLY ZERO on all five, so omitting them
       costs nothing. **The two omissions that cost everything are the generalized-alpha
       weighting and the Jacobian point.** `alpha_m M_eff xi_ddot_n` reads `5.280` on the
       platform and `3.124` on each hub, against a locked residual of `1.01e-04` and
       `1.4e-06 .. 6.6e-06`; and `(g_mid - g_now).T lam` is `3.0e-05 .. 6.5e-04`, itself
       6x to 480x the locked residual on the hubs.
cmd    python <the same solve; BOTH numerators as window MAXIMA over the last 200 steps,
                t = 10.010 .. 12.000 s, each divided by the SCRIPT's OWN magnitude-sum
                denominators so the two ceilings are directly comparable>
rule   the window rule of docs/milestones/F4.md:145 -- the clean worst is what the ceiling
       is declared from
out    body       FORCE g41   FORCE locked     ratio    MOM g41    MOM locked    ratio
out    platform  2.2618e-03    1.0400e-16   2.17e+13  7.1510e-04  1.4534e-06  4.92e+02
out    hub1      1.5417e-03    8.2612e-17   1.87e+13  1.0253e-04  9.0913e-07  1.13e+02
out    hub2      2.3933e-03    9.7714e-17   2.45e+13  1.0438e-04  6.8889e-07  1.52e+02
out    hub3      1.4975e-03    1.0862e-16   1.38e+13  7.4711e-05  6.2887e-07  1.19e+02
out    hub4      2.3933e-03    9.7707e-17   2.45e+13  1.0438e-04  6.8889e-07  1.52e+02
out    worst over the five FE bodies, this case:
out      g41     force 2.393343e-03   moment 7.151029e-04
out      locked  force 1.086249e-16   moment 1.453396e-06
judge  **THE OPERATING POINT IS NAMED AND IS NOT THE DQ6 WINDOW** -- this is 200 steps
       immediately after the ramp on a 12 s run, so the absolute values are not the gate's
       figures and I am not offering them as such. **The RATIO is structural**: it is the
       algebra of the two formulas and it holds step by step. On the force channel the
       locked residual is AT ROUND-OFF (`1.09e-16`) and g41 reads `2.39e-03`; a ceiling
       declared by the window rule from the second would be **thirteen decades** looser
       than the quantity the plan locks, on a channel that currently closes exactly.
```

**And the hand-back's own first figures are consistent with this reading, which is why I
am raising it now rather than after the six runs.** It quotes force `4.875964e-04` to
`5.193314e-04` and moment `8.746485e-05` to `1.017068e-04`. Those are the g41 quantity's
order of magnitude, not the locked one's. The locked force channel does not have figures at
`1e-04`; it has them at `1e-16`.

## 5. THE EW0 CONSTRUCTION -- ALL THREE CLAIMS ATTACKED. TWO HOLD, ONE HAS A GAP

**(i) `paths_ignored()` -- the premise HOLDS, and every misread I could construct errs in
the SAFE direction.**

```
cmd    python <import scripts/ci_section.py; print(ci.paths_ignored())>
out    ['docs/reports/**', 'docs/reviews/**']
cmd    python <the shipped parser against eight constructed workflow blocks>
out    shipped-like, two entries with comments between  -> ['a/**', 'c/**']
out    a comment whose text is a dash bullet            -> ['a/**']   (NOT picked up)
out    an inline trailing comment on an entry           -> []
out    an unquoted entry                                -> ['a/**', 'c/**']
out    flow style, the whole list on one line           -> []
out    a blank line inside the block                    -> ['a/**', 'c/**']
out    an entry after the terminator                    -> ['a/**']
out    a SECOND paths-ignore block later in the file    -> ['a/**']
judge  **THE COMMENT LINES CANNOT SLIP IN.** The character class excludes the comment
       marker from the capture and the bullet is anchored after leading whitespace, so a
       commented-out entry matches nothing AND does not terminate the block either.
       **And every one of the five misreads returns a SHORTER list, never a longer one**
       -- the safe direction twice over: `report_only()` returns `False` on an empty list,
       and `code_identical_run()` then refuses on the first changed path. A parser misread
       here makes `section()` exit 1 loudly, which is what it did before EW0. The
       hand-back put this up as a possible (c) and the measurement says it is not one.
```

**(ii) `report_only()`'s `fnmatch` -- the claim that the difference cannot admit a code
path is TRUE AT THIS TREE, and I measured it rather than reasoning about it.**

```
cmd    python <every tracked path, matched against the two globs with fnmatch>
out    tracked paths matched OUTSIDE docs/reports/ and docs/reviews/ : []
out    total matched: 30
cmd    python <ci.report_only() on all eleven commits in and around the range>
out    d4e2136 True / bac3017 True / b4aae36 True
out    77d4a6b 4b64eaf 4344495 27ecf62 4ed4399 4f0acfd 9de3e4e 9e59478   all False
judge  CORRECT, and correct for the right reason: `fnmatch`'s star crosses the separator,
       which makes the two shipped globs mean "anything whose path starts with that
       directory" -- and GitHub's double star means the same thing for globs of that
       shape. **The divergence direction is WIDER, which is the unsafe one** (R714 below):
       a future entry whose star is meant to stop at a separator would make
       `docs/closure/F4.md` report-only here while GitHub ran on it. No such entry exists
       and no tracked path reaches it today, so this is not (c). The `b4aae36 True` row is
       my own verdict commit, correctly classified.
```

**(iii) `code_identical_run()` -- the first-parent walk is SOUND, and "not an ancestry
walk" does not matter here. For a different reason than the one offered.**

```
cmd    read scripts/ci_section.py:296-338 and run it
out    code_identical_run(b4aae36) -> ancestor 77d4a6b  run 37577931492
out      status 'completed'  conclusion 'failure'
judge  The protection is NOT the first-parent-ness; it is that `git diff candidate sha` is
       recomputed for EVERY candidate and the function returns empty at the FIRST candidate
       whose diff contains a non-ignored path. Candidates are visited nearest-first, so the
       walk terminates at the nearest code difference and cannot reach past it.
       First-parent is strictly CONSERVATIVE on top of that: a side branch's commits are
       skipped, but their content is inside the merge commit and therefore inside the diff,
       so a skipped commit can never be offered as evidence for code it does not match.
       `--max-count=40` failing to find one also returns empty, which is the safe
       direction. **The claim holds.** It correctly walked past the report-only `d4e2136`
       and named the run whose code matches, with its `failure` conclusion stated rather
       than hidden.
```

## 6. THE EV1 / CONVENTIONS CONFLICT -- RULED. THE BRANCH IS RIGHT AND THE FRAMING IS HONEST

I was asked to rule and I do, once.

**The conservative branch is the right one.** `docs/conventions.md` is locked at F0 and is
authoritative for frames and moment references; it says the body frame's origin and the
moment reference are the `reference_point` at `:113`, `:159` and `:165`. EV1 is a later
directive whose formula says `G`. `CLAUDE.md` says never to assume a frame and to stop
rather than pick the one that makes the test pass. Forming the moment about the point the
conventions declare, printing that sentence on every run via `moment_point()`, and sending
the conflict to Xabier is exactly the prescribed behaviour, and I would have found the
other branch a finding.

**It is also the right construction and not merely the safe label.** The moment rows of
`g^T lam` are the generalized moments the constraint Jacobian already produces about each
body's reference point -- so the script never reconstructs the cross products from node
positions at all, and there is no lever arm to get wrong. That is better than EV1's
written form.

**A FIGURE MAY BE PUBLISHED, and I am not blocking on this.** Measured:

```
cmd    python <the deck's body attributes, and every reference_point>
out    body attrs matching cog|ref|cent : ['reference_point']   -- there is NO CoG field
cmd    grep -rn "cog_offset_body" ../HSP-runs/floatsim/ ; sed -n '182,184p' docs/conventions.md
out    ../HSP-runs/floatsim/driver.py:222:        cog_offset_body=None,
out    ../HSP-runs/floatsim/bodies/mass_properties.py:81:    if cog_offset_body is None:
out    docs/conventions.md: Z_BUOY_REF = -1.1956674 ; CoG -1.23268 ; offset +37.0 mm
judge  the two points coincide inside the solve by construction, the deck carries no CoG
       to form the other moment about, and **the 37.0 mm offset the docstring cites is the
       BUOY's** -- `Z_BUOY_REF`, `cluster_common.py:33` -- and the buoys carry no FE mass
       and are out of this gate by DQ7. So no body this gate measures has a declared CoG
       offset, and no figure is at risk either way. The escalation is correct; it is not
       urgent for G4.1, and the docstring's one wrong detail is R715.
```

## 7. THE MARKER REVERT -- COMPLETE, AND NOTHING ELSE DEPENDED ON IT

```
cmd    git diff 4b64eaf 27ecf62 --stat
out    (empty)
cmd    grep -n "step-under-execution" docs/milestones/*.md
out    F2.md:10 moved to F3 at step 1 (DY8c) / F3.md:9 moved to F4 at step 1 (EL0/EM0)
out    F4.md:3 step-under-execution: 2
judge  the tree at `27ecf62` is BYTE-IDENTICAL to the tree at `4b64eaf`, so the revert is
       exact and complete; exactly one plan carries the marker, so `_active_plan` cannot
       return `(None, 0)`; and my own suite run is `3244 passed` with all 18 of
       `4344495`'s reds gone. Nothing else depended on the marker being 3. **And the guard
       was obeyed rather than edited**, which is the part that matters.
```

## 8. TRY TO BREAK IT -- WHAT I RAN AND WHAT IT SAID

* **Both numerators at the same operating point, with the same denominators** -- found
  R711. `2.2e+13x` on the force channel.
* **Every term the g41 numerator drops, held out one at a time** -- `ext`, `C`, `mu` and
  the added-mass contribution are identically zero on the five FE bodies;
  `alpha_m M xi_ddot_n` is `3.12` to `5.28`; the Jacobian-point difference is `3.0e-05` to
  `6.5e-04`. The causal claim carries its cells (BG0): one term moved, the rest held.
* **The decomposition identity** -- exact to `2.87e-18`, and each joint touches exactly two
  bodies. The hand-back's worry is answered and the denominator is right.
* **The magnitude sum against the magnitude of the sum** -- `10.9x` to `41.9x`, so EV1's
  cancellation argument is a measurement here and not a prediction.
* **A hub-only force defect under the sign flip** -- R709 closed, and the detection
  boundary solved both ways.
* **A counter between the family minimum and the shipped pair** -- R710 closed, ablation
  reproduced.
* **The mapping family at all seven ladder rungs** -- bit-identical, 12 of 12 at each.
* **Eight mutations of the workflow's paths-ignore block** -- all five misreads err short,
  comments never picked up.
* **Every tracked path against the ignore globs** -- nothing outside the two report
  directories matches, so the wider `fnmatch` star admits no code path today.
* **`run_for` on an unfinished run** -- returned `status: in_progress, conclusion: ''`.
  R713.
* **`ROWS_PER_JOINT` against the real Jacobian** -- 64 rows, exactly divisible, 16 joints,
  102 DOF. Correct today, and asserted nowhere; R712(iii).

## Findings

**R711. (BLOCKING -- (b) and (c) through the generator-is-the-gate carve-out)
`scripts/measure/g41_dynamic.py` MEASURES THE CONTINUOUS BALANCE, NOT THE DISCRETE ONE THE
PLAN LOCKS, AND ITS OWN DOCSTRING SAYS IT MEASURES THE DISCRETE ONE.**
`scripts/measure/g41_dynamic.py:218-234` (the numerator), `:220` (`jacobian(res.xi[n])`
where the solver uses the step midpoint), `:221` (`m_eff @ res.xi_ddot[n]`, with no
`(1-alpha_m)` factor and no `alpha_m M xi_ddot_{n-1}`), and the claim at `:20-23`: "THE
RESIDUAL IS THE DISCRETE ONE, as locked. ... The form here is
`report_joint_reactions.py::discrete_residual`'s, per body." It is not. Measured in
section 4, as window maxima over 200 steps at `T_full = 14` with the script's own
magnitude-sum denominators: force `2.393343e-03` against the locked form's
`1.086249e-16`, a ratio of `2.2e+13`; moment `7.151029e-04` against `1.453396e-06`, a
ratio of `4.9e+02`. Per-body ratios `1.38e+13` to `2.45e+13` and `1.13e+02` to `4.92e+02`.
The three omissions isolated one at a time: `alpha_m M_eff xi_ddot_n` reads `5.280`
(platform) and `3.124` (each hub) against locked residuals of `1.01e-04` and
`1.4e-06 .. 6.6e-06`; the Jacobian-point difference reads `3.008e-05 .. 6.538e-04`; and
`ext`, the two damping terms, `mu` and the added-mass contribution are **identically zero**
on all five FE bodies, so those omissions cost nothing and I say so rather than listing
them as faults. `newmark.py:414-437` states the equation and comments in its own words that
`G` is at the midpoint "for energy consistency with the trapezoidal balance";
`docs/milestones/F4.md:131` says the residual "keeps the **discrete** form already locked"
and `:486` names that balance as the gate's `# expected:` source. **Why this is blocking
and not a closure item:** `docs/milestones/F4.md:486` says the G4.1-dynamic ceilings are
"to be measured at step 3 over all 30 body-cases; ceilings by the window rule", and
`scripts/measure/README.md:1` says this directory is where every report figure comes from
-- so this script's output **is** the (b) value and defines the (c) quantity. A ceiling
declared by the window rule from these figures would be thirteen decades looser than the
locked quantity on a channel that presently closes to round-off, which is "never widen"
arriving through a derivation instead of an edit. Catching it before the six runs are spent
is the cheap moment. **Closed when** either (i) the numerator is the discrete residual the
plan names -- `a_eff @ xi_ddot[n] - jacobian(0.5*(xi[n-1]+xi[n])).T @ lam[n] - rhs`, split
into its force and moment rows and divided by the two magnitude-sum denominators, with the
clean worst re-measured and pasted and my `1.086249e-16` / `1.453396e-06` beaten or refuted
at a named operating point; **or** (ii) the plan is reopened to say that G4.1-dynamic is
declared on the continuous balance, with the reason a thirteen-decade looser gate is what
is wanted written down -- that branch is a plan question and goes to Xabier, not a round.
Either way `:20-23`'s claim is made true or deleted (CW0), and the file states which
balance it forms in the sentence a reader meets first. **No new apparatus either way: it is
the expression at `:224` and the argument at `:220`.**

**R712. (closure class, listed because its site is the input to a (b) declaration)
ER0's BASIS IS WIRED IN THE NEW CALLER AND NOT AT THE SITE, AND THE OVERRIDE'S VALUES ARE
TYPED WHERE THE DECK DECLARES THEM.** Three parts, one root. (i)
`scripts/report_joint_reactions.py:120` still ships `PLATFORM_MASS_OVERRIDE = None`, and
its own `main()` at `:366` calls `solve_one` without setting it -- so that script run on
its own still measures the un-overridden deck, which is R700's shape at its own site. ER1(b)
requires EK0(a) and the EJ4 per-body residual to be repeated **on the new runs**; a figure
taken from `report_joint_reactions.py` directly would be on the old basis, and the
hand-back's own `2.642563e-04 -> 5.003041e-04`, `1.89x` is the measurement of what that
costs. (ii) `scripts/measure/g41_dynamic.py:179-182` types `20.0` and `20/20/40` where
`data/platform/platform12_deck.yaml:17-20` declares them in its own OVERRIDE header -- a
list in two places, which is the drift the same commit range argued against for
`paths_ignored()` and which R686 already settled for `rho_inf` in the same file (`:83`,
`rho_inf_from_deck()`). (iii) `scripts/measure/g41_dynamic.py:131` computes
`n_joints = g.shape[0] // ROWS_PER_JOINT` and asserts neither divisibility nor
`n_joints == 16`; both hold today (64 rows, exactly divisible, measured) and a silent
truncation would produce a plausible denominator rather than an error. **Closed when** the
override reaches the solve from the deck's own declared header rather than from a literal,
`report_joint_reactions.py`'s own entry point either applies it or refuses to run without
it, and the joint count is asserted rather than inferred.

**R713. (closure class) `run_for()` AND `code_identical_run()` APPLY NO STATUS OR
CONCLUSION FILTER, SO EW0's STATE CAN OFFER AN UNFINISHED OR CANCELLED RUN AS "THE RUN THAT
MEASURES THIS CODE".** `scripts/ci_section.py:292-293` (`pushes[0]`, no filter) and
`:330-332` (the first candidate with any run wins). Measured: at the start of this check
`run_for("9de3e4e9a8bc31caa1e22259d9d570c39d39c3b2", required=False)` returned
`status: 'in_progress', conclusion: ''`, which `report_only_section` would have rendered
with an empty conclusion and a job table from an unfinished run; and the three newest
conclusion-bearing runs before `4f0acfd` in this very range are all `cancelled`, so the
first report-only judged commit on this branch is the case. The section does print the
conclusion, so nothing is laundered -- but `docs/SUPERVISOR.md`'s CA2 says a run that has
not finished is not a pass, and CX0/R449 says a cancelled run reached no verdict on
anything. `tests/test_report_carried.py`'s new `_REPORT_ONLY` branch requires a full sha
and a job table and requires neither of those. **Closed when** a candidate whose run is not
`completed`, or whose conclusion is `cancelled`, is skipped and the walk continues, or the
state's own sentence says that the run it names reached no verdict.

**R714. (closure class) `fnmatch` IS WIDER THAN GITHUB'S GLOB AND WIDER IS THE UNSAFE
DIRECTION.** `scripts/ci_section.py:316` and `:331`. The claim under attack -- that the
difference "cannot admit a code path" -- is **true at this tree and I measured it**: no
tracked path outside `docs/reports/` and `docs/reviews/` matches either glob, and for globs
of the shipped shape the two semantics agree. What the claim does not cover is a future
entry whose star is meant to stop at a separator: such an entry would make
`docs/closure/F4.md` report-only here while GitHub ran on it, and the consequence is a
commit with a real run being told it has none. Not a finding today; recorded because the
premise of the whole state is which paths the workflow ignores, and the direction of the
only divergence is the one that widens "ignored". **Closed when** the matcher is
separator-aware, or `paths_ignored()` refuses a glob that is not a directory prefix
followed by a double star.

**R715. (closure class) THE DOCSTRING'S EVIDENCE FOR "NOT COINCIDENT ON THIS PLATFORM" IS A
BUOY FIGURE, AND NO BODY IN THIS GATE HAS A CoG OFFSET.**
`scripts/measure/g41_dynamic.py:36` cites `docs/conventions.md:182-184`'s `-1.1956674`,
`-1.23268` and `+37.0 mm`, and `:38` reads "on this platform the two points are not
coincident". Those three numbers are the **buoy's** reference point and CoG (`Z_BUOY_REF`,
`cluster_common.py:33`), and the twelve buoys carry no FE mass and are out of this gate by
DQ7. Measured: the deck's body objects expose `reference_point` and no CoG field at all, so
for the five bodies this gate does measure there is no declared offset in either direction.
The general rule at `:113`, `:159` and `:165` still applies and the branch taken is still
right -- what is wrong is that the one quantitative piece of evidence is about bodies the
gate excludes, which makes the conflict read more urgent than it is. **Closed when** the
citation is either a figure for one of the five FE bodies or is stated as the buoys' with
the note that no FE body declares an offset.

**R716. (not against the work -- a mechanism gap I hit myself, recorded because my
instructions say an absent mechanism is a finding) `scripts/write_verdict.py` CANNOT WRITE
AN ES0 INTERIM CHECK ON A STEP WHOSE REPORT DOES NOT EXIST YET.**
`scripts/write_verdict.py` exits at the fourth of its four refusals -- the one its own
docstring describes as "a step with no report to review" -- and an ES0 interim check is
defined as a check "on a tree with NO new report revision", which for the FIRST check of a
step means no report at all. So the one sanctioned path into the verdict directory refuses
the one kind of verdict ES0 created. **I wrote this file directly**, in the script's exact
format -- its own `# Review` and `Reviewed commit:` header, UTF-8, LF, and no earlier
rounds because the file did not exist -- which is the hand-written route `CLAUDE.md` records
as the resolution when the mechanism cannot express a disposition. **And the second half,
which the implementer needs to know rather than discover:** the `Stop` hook anchors on the
NEWEST report, which is still `docs/reports/F4/step-2.md`, so **this verdict does not clear
it** -- the hook's own dirty check against `d4e2136` over the report, `floatfea` and `tests`
is non-empty, because `4b64eaf` and `4ed4399` changed `tests/`. The exit is to land step 3's
first report, which makes this file the anchor; `closed_by_a_pass` keeps step 2 closed, so
there is no deadlock. **Do not write a round into step 2's verdict file to clear the hook**
-- that is the exact confusion CLAUDE.md's step-gating section spent two verdicts on.
**Closed when** `write_verdict.py` accepts a step with no report under ES0, or
`docs/SUPERVISOR.md` says where an interim check on a reportless step is written. That is a
change to my own tooling and goes through a directive in a standalone `process:` commit,
not through a step commit.

**R717. (closure class, EK2's LOCATOR class, and ONE MECHANISM WITH R716)
`scripts/ci_section.py`'s ANCHOR PATTERN AND `scripts/write_verdict.py`'s OUTPUT DISAGREE,
SO THE GENERATOR DEPENDS ON A PROSE CONVENTION ITS OWN PRODUCER DOES NOT EMIT.**
`scripts/ci_section.py:172` is a bold, backticked pattern --
`_JUDGED` at `:172` requires the sha to be WRAPPED IN BACKTICKS INSIDE A BOLD SPAN --
and `:201-206` raises when it does not match. `scripts/write_verdict.py:82` emits
`Reviewed commit: {sha}`, **plain**. So the only line the sanctioned writer produces cannot
satisfy the only pattern the generator accepts, and what has been satisfying it is a
sentence reviewers have written in the body by hand.

```
cmd    python scripts/ci_section.py
out    verdict 104 at `9ec380e` does not name the commit it judged in its header, so
out    there is no commit to report CI for.
cmd    python <every commit touching docs/reviews, newest 40 states: does the file carry
                the bold judged-commit line at all?>
out    verdict-file states examined : 40
out    NO bold line at all          : 5
out      9ec380e docs/reviews/F4/step-3.md   <- mine, this round
out      8368c51 docs/reviews/F3/step-3.md
out      83c7ba5 / 5bfdf3e / 53c4908  docs/reviews/F2/step-7.md
judge  **IT HAS BEEN OMITTED FOUR TIMES BEFORE MINE**, so this is not a quirk of one
       hand-written verdict. The dependency is invisible until the line is absent, and the
       line is absent exactly when a verdict is written outside `write_verdict.py` -- which
       is R716's condition. **R716 and this are one mechanism, not two coincidences**, and
       the coordinator's reading of that is right.
```

**It is EK2's class and the repair belongs at the PRODUCER, not at the consumer.** EK2
permits repairing a locator that misreads its input. `_anchor()`'s own docstring is
`CO1: one chain, no argument, no fallback that guesses`, and that refusal is CORRECT -- see
R718. So the repair is that `write_verdict.py` emits the bold line, taken from the body's
own statement of the commit it judged and refused when the body states none, which turns
the convention into a mechanism. **Closed when** the writer emits what the anchor reads, or
the anchor reads what the writer emits AND the two are shown to be the same quantity --
which R718 measures that they are not.

**I HAVE ADDED THE LINE TO THIS FILE, AND THERE IS AN ORDERING CONSEQUENCE THE COORDINATOR
MUST ACT ON.** `_anchor()` reads the verdict **at the commit the report answers** --
`git show {verdict_sha}:{VERDICT_IN_REPO}`, `scripts/ci_section.py:192-199`. The line is
NOT in `9ec380e` and cannot be put there: that commit is pushed and force-push is
forbidden. So **step 3's report must answer the commit that CARRIES this line** --
`git log -1 --format=%h -- docs/reviews/F4/step-3.md`, taken when the report is written,
which is the amendment commit and not `9ec380e` -- or the generator will refuse for the same reason at the older sha. That is the
whole of what unblocks the report.

**R718. (BLOCKING -- (c): a gate assertion on WHICH QUANTITY. Latent, and I say so.)
`tests/test_report_carried.py:2086`'s FALLBACK SUBSTITUTES A DIFFERENT QUANTITY -- ONE THE
TREE ALREADY DOCUMENTS AS NOT THE JUDGED COMMIT.**
`tests/test_report_carried.py:2084-2086`:

    def _judged_commit() -> str:
        m = _JUDGED.search(VERDICT_TEXT)
        return m.group(1) if m else _reviewed_commit(VERDICT_TEXT)

and `:270-272`, where `_reviewed_commit()` reads the **plain** `^Reviewed commit:` header.
That header is `write_verdict.py`'s `sha()` -- **HEAD at the moment the verdict was
written** -- and `scripts/write_verdict.py:36-41` says so in its own words: "The
`Reviewed commit:` stamp is taken from `HEAD`, which is structurally NOT the reviewed
commit whenever the reviewer commits its corpus first -- as it is instructed to. The body
names the commit it judged; that line does not."

```
cmd    python <every commit touching docs/reviews, newest 40 states: the plain header sha
                against the bold judged-commit sha in the same file>
rule   `test_the_CI_section_is_about_the_REVIEWED_commit` asserts the section is about the
       commit the verdict JUDGED
out    states carrying BOTH lines           : 35
out    plain header == bold judged (prefix) : 12
out    plain header DIFFERS from bold judged: 23
out      488f2d8 docs/reviews/F4/step-2.md   plain 4f99c7f  judged 7cee09f
out      5786bed docs/reviews/F4/step-1.md   plain 6e39151  judged 84de436c
out      9d7a9c4 docs/reviews/F3/step-3.md   plain 4193c0d  judged 727b9fa
out      580b183 docs/reviews/F3/step-2.md   plain 5a2ff21  judged 29570e1
out      ... 19 more
judge  the two lines are DIFFERENT QUANTITIES and they differ in 23 of the 35 states where
       both exist. The fallback substitutes the first for the second.
cmd    python <the 4 earlier no-bold states: is the plain header the verdict commit's own
                parent, i.e. HEAD at write time?>
out    8368c51  plain 6c4e6516f  parent 6c4e6516f  equal=True
out    83c7ba5  plain 0a660cede  parent 0a660cede  equal=True
out    5bfdf3e  plain d877c9100  parent d877c9100  equal=True
out    53c4908  plain b9a985999  parent b9a985999  equal=True
judge  **AND THIS IS THE HONEST LIMIT OF THE MEASUREMENT: THE FALLBACK HAS NEVER YET
       MIS-RESOLVED.** It fires only when the bold line is absent, and in all four earlier
       absences nothing was committed between the judged commit and the write, so HEAD at
       write time WAS the judged commit. It is latent, not live, and I am not going to
       pretend otherwise.
```

**WHY I BLOCK ON A LATENT DEFECT, AND IT IS NOT A JUDGEMENT CALL -- IT IS THIS ROUND.** The
fallback fires when the bold line is missing; it is wrong when a commit intervened between
the judged commit and the write. Those two conditions coincide the first time a reviewer
commits a corpus and then hand-writes a verdict, **which is exactly this round minus the
corpus**: I hand-wrote this verdict, and the only reason I did not commit a corpus batch
first is that ES0's light scope forbids one on an interim check. Had this been a full round,
the plain header would have named my corpus commit and
`test_the_CI_section_is_about_the_REVIEWED_commit` would have certified a CI table as being
about a commit that is not the one reviewed. **R352's four consecutive rounds were that
exact defect with the section at fault; this is it with the CHECK at fault**, and a check
that cannot fail when the thing it claims is false is the one shape my instructions say to
ask of every test.

**AND IT INVERTS THE COORDINATOR'S READING, WHICH IS WHY IT IS A FINDING RATHER THAN A
NOTE.** The hand-back offers the fallback as the guards resolving what the generator cannot,
and reads that as the generator being the weaker of the two. Measured, it is the other way
round: the generator's refusal is correct under CO1, and the fallback is the defect. "A
report could pass its own guards while the section it needs could not be produced" is true
and is the right worry -- but the cure is not to teach the guard to guess; it is that the
guard should refuse too, and the producer should emit the line so neither has to.

**Closed when** `_judged_commit()` has no fallback and the existing `assert judged` is what
fires -- its own message already reads "The verdict's header carries
the bold, backticked header form by name, so the assertion is already written for
the no-fallback form -- **or** the fallback reads a line that IS the judged commit, with the
equality measured over the same 35 states rather than assumed. One expression either way,
and no new apparatus.

**ES0 light scope, honoured literally: there is no `## Closure items` list this round and
no corpus batch.** R712 to R717 are closure class and join step 3's list, to be answered in
its first revision or in the closure commit; C1 to C21 from step 2's rounds carry into
`docs/closure/F4.md` unchanged and I did not re-adjudicate one of them.

## Tolerances touched

```
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+][A-Za-z0-9_]+:"
out    (no output)
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+]" |
       grep -vE "^(\+\+\+|---)" | grep -E "Final|=\s*[0-9]"
out    (no output)
judge  **NO VALUE MOVED ANYWHERE IN THE TREE, CEILING OR COUNTER.** All 53 changed lines in
       that file are comment lines in one entry. EU1 does not fire; I ran its adversarial
       case anyway.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_MAPPING_CONSERVATION_COUNTER` | `0.2` | `0.2`, **unmoved** | dimensionless, relative; a floor beneath a defect family whose size scales with the lever between two nodes | **the injection changed, and that is (b)**: `wrong_node_same_body` now loops all twelve ordered pairs of the four platform joint nodes with `assert len(family) == 12`, and asserts the family MINIMUM against both the counter and the ceiling | `floatfea/tolerances.py` entry at `:2263-2318`; plan row `docs/milestones/F4.md:532`, in the same commit (BR0) | **ACCEPTED. R710 CLOSED.** Every figure reproduces to the digit: family minimum `0.2179893030274107` (node 3 to 4), maximum `1.6964643105279407` (node 3 to 1), spread `7.7823x`, the shipped pair `0.9597085787263796` seventh of twelve, margin `1.0899x`, and bit-identical at all seven rungs with 12 pairs at each. The ablation holds: a counter at `0.5` passes the single-pair form and reddens the loop. The corrected `1.0899x` and `0.9175` replace the published `4.7985x` and `0.2084` in both the entry and the plan row. |
| `F4_DQ4_ELEMENT_VECTOR` / `_COUNTER` | `1.0e-12` / `5.0e-4` | unmoved | dimensionless, relative; moment channel SIGNED | three injections over five bodies with `assert len(per_body) == 5`; **the sign-flip row's two assertions are now PER BODY, not on an aggregate** | `floatfea/tolerances.py` entry ending at `:2353`; plan rows `docs/milestones/F4.md:483`, `:534` | **ACCEPTED. R709 CLOSED, AND THE BOUNDARY IS SOLVED BOTH WAYS.** The `min` feeding `error > counter` is kept, which is the correct direction for that assertion; the `<` assertion no longer reduces at all. Measured: a hub-only force error at `1.001`, `2.0` and `1e+06` passed the old form and is caught on all four hubs by the new one, with the clean case still passing on all five. Clean per body `2.483527e-16` (platform), `1.552204e-16` and `4.656613e-16` (hubs), max `4.656613e-16`, `2147.5x` inside the ceiling. The moment channel reads `2.0000000000000004` and `2.000000000000001` per body, so the per-body `approx(2.0)` is strictly stronger than the old `min`. Detection boundary: caught at `1 + 1.0e-12`, missed at `1 + 9.9963e-13`. **No value needs to move and the entry's text is not stale** -- it describes values and domain size, both unchanged. |
| G4.1 dynamic (DQ8 / EV1) | -- | **none declared, and none may be declared from the current generator** | two dimensionless ratios, each gated, never combined | -- | `scripts/measure/g41_dynamic.py:218-234`; plan rows `docs/milestones/F4.md:117-148`, `:486` | **THE REFUSAL TO DECLARE IS STILL CORRECT AND IS NOT THE FINDING. R711 IS.** The denominators are right and I verified the decomposition they rest on: `2.87e-18`, each joint on exactly two bodies, magnitude sum `10.9x` to `41.9x` above the magnitude of the sum. The NUMERATOR is the continuous balance. A ceiling declared by the window rule from it would be `2.2e+13x` loose on the force channel and `4.9e+02x` on the moment channel at the one operating point I measured. **C1 is still open and is still this quantity's input**, exactly as verdict 102 conditioned and verdict 103 carried. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. Verdict 103 measured all nine of them clean or ruled, and ES0's light scope says an interim check does not re-run that. |

## Carried

Verdict 103 (`b4aae36`, judging `d4e2136`) closed step 2 PASS carrying **two blocking items
by name** and twenty-one closure items. Every one, with status.

* **R709 (blocking) -- CLOSED**, at the first branch of my condition. Answered at `4b64eaf`,
  `tests/verification/rung4/test_f4_static_and_mapping.py:1875-1911`: the `<` assertion is
  no longer reduced over bodies at all, which is stronger than the `max` I asked for, and
  the `min` that feeds `error > counter` is correctly kept. Section 3: my figures to beat
  reproduce to the digit and the detection boundary is solved in both directions.
  **Does not carry.**
* **R710 (blocking) -- CLOSED**, at both branches of my condition. Answered at `4b64eaf`,
  `tests/verification/rung4/test_f4_static_and_mapping.py:1099-1143` (the twelve-pair loop
  with `assert len(family) == 12`), `floatfea/tolerances.py:2263-2318`, and the plan row
  `docs/milestones/F4.md:532` in the same commit. Section 2: the whole family table, the
  margin `1.0899x`, the weakening window, the rung invariance and the `0.5` ablation all
  reproduce. The value correctly did not move. **Does not carry.**
* **C1 (closure, but conditioned) -- STILL OPEN, AND THE CONDITION IS NOW LIVE.** Verdict
  102 required it "answered BEFORE the G4.1-dynamic quantity is chosen, because that choice
  is (c) and this is its input", and verdict 103 carried that condition into step 3's
  opening terms. `scripts/report_joint_reactions.py` is not in this range at all, so the
  inverted dimensional sentence at `:238` and the incomplete "on all seventeen" claim are
  untouched. **R711 is that choice arriving**, so C1 and R711 are now one piece of work and
  C1 is answered with it rather than in the closure commit.
* **C2 to C21 (closure) -- carried unchanged into `docs/closure/F4.md` and NOT
  re-adjudicated**, per verdict 103's own instruction and ES0's light scope. I verified only
  that C21 does not recur: the hand-back's range of eight is correct this time.
* **Verdict 103's escalation -- unchanged and not re-argued.** Two consecutive steps closed
  carrying; the choice stated was reduce scope rather than slip, and that is a plan decision
  for Xabier. R711 does not change the recommendation, but it does change the arithmetic:
  the G4.1-dynamic ceiling needs a corrected numerator **before** the six runs are spent,
  not after, and that is cheaper now than it will ever be again.
* **The two self-reported `black --check` counts -- both recorded, neither re-litigated.**
  `116` where it printed `120`, and `22` where it printed `23`. At HEAD
  `black --check floatfea tests scripts` prints `121 files would be left unchanged` and
  `ruff check floatfea tests scripts` prints `All checks passed!`, so nothing shipped wrong.
  The shape named -- a count written from a previous run and then a file added, CP3's
  ordering in the one place CP3 does not reach -- is right, and self-reporting it before I
  looked is the practice I have been asking for. Closure class.

## The adversarial corpus (BE3)

**NO BATCH THIS ROUND, AND THAT IS ES0's INSTRUCTION RATHER THAN MY CHOICE.** ES0: "An
interim check is light: the suite and CI at the commit, plus a CZ0 (a)-(d) scan of the diff
since the last verdict. **No corpus batch, no closure list.**" EG4(e)'s pause to
28 October stands otherwise, with its two exceptions unchanged.

* **Batch 37 is the live one** -- `tests/corpus/f4_mapping_wrong_node_injection_family.txt`,
  39 entries, committed separately at `9e59478`. **Coverage this round: 0 new entries, so
  there is no new coverage number, and I am not restating last round's as if it were one.**
* **Still owed at the 28 October batch, unchanged plus one:** F4's load-mapping gate (a
  defect identical on all five bodies; a block moved between two nodes at the same
  position), EB6's gate per C5 (permutations that PRESERVE the count), the shared-attribute
  corpus for DQ4(i), and the aggregation-direction corpus added last round. **Added by this
  round: a RESIDUAL-FORM corpus** -- for each gate whose quantity is the residual of a
  discretised equation, which terms of the solver's own equation the measurement omits and
  what each omission is worth. R711 is that shape and nothing in this repository scans for
  it.
* **My own hygiene item, carried from verdicts 101, 102 and 103 and still mine:**
  `tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48, 49 and 50 carry
  `measured=` figures on the OLD mass basis. I re-head that file at the 28 October batch.

## Next step opens when

**Step 3 is OPEN and stays open. This check consumed none of its three revisions**, so
step 3 still has all three. What it must do before anything else:

1. **R711 is answered**, by one of the two branches its condition names, **before any
   G4.1-dynamic figure is published and before the six FloatSim runs are spent on the
   current numerator.** If branch (ii) is taken it is a plan question for Xabier and does
   not become a round.
2. **C1 is answered in the same work**, because it is R711's input and verdict 102
   conditioned it exactly there.
3. **R712 to R717 join step 3's list** and are answered in its first revision or in the
   closure commit. None of those holds the step. **R718 DOES hold it** -- it is (c) and
   one deletion -- and **R717's ordering note must be acted on** for the report's
   section 0 to be produced at all: the `Answers:` header must name the commit that
   carries the bold anchor line, which is not `9ec380e`.
4. **Step 3's own locked work is unchanged by this check** and is not reopened: the
   member-force table per member and per case at every element node, the six-case envelope,
   the `f` sensitivity, R638, R637 clause (iii), and `docs/closure/F4.md` with G4.5's
   measured rate and DQ6's cycle-to-cycle measurement.

**What I will not accept at step 3's first revision.** A G4.1-dynamic ceiling whose clean
worst is of order `1e-04` on the force channel, without a sentence saying which balance it
is the residual of and a number that beats or refutes my `1.086249e-16` at a named
operating point. The reason is not the figure; it is that `1e-04` and `1e-16` are the same
code measured two ways, and a ceiling cannot be declared until the tree agrees which way
the plan meant.

## On the criterion -- I was asked, and I agree with it, with one note on where it bites

CZ0 is right, and six rounds of prose findings moving no gate is the evidence. R712, R714, R715 and R717
went to the closure class without argument, including two I would have enjoyed arguing
about, and that is the criterion working.

**The note, said once.** My single blocking finding is in `scripts/`, which CZ0 lists under
"generators, parsers" as closure class, and I blocked on it under the carve-out my own
instructions give -- "a generator whose output *is* a gate's assertion". I want that
recorded as a deliberate reading rather than a stretch, because the mechanism matters: under
EV3 **every report figure now comes from `scripts/measure/`**, and under
`docs/milestones/F4.md:486` the G4.1-dynamic ceilings are declared from the figures measured
at step 3. So EV3 moved the derivation of a (b) value out of the step report -- which is
regenerated by rule -- and into `scripts/`, and the strict reading of CZ0 would put the
derivation of every future tolerance beyond blocking reach. EV3 is a good directive and I am
not arguing against it; the consequence is one nobody wrote down. **A script under
`scripts/measure/` whose output is a declared tolerance's derivation is (b) while it is
being used that way**, and that is how I will rule until told otherwise. This goes to
Xabier through the implementer as a reading, not as a round.

**And one thing on the record for the implementer rather than against them.** The hand-back
named the exact function to attack, said which of its properties it was least sure of,
volunteered two of its own errors before I could find them, and pointed me at the one file
where I then found the blocking item. The decomposition it was worried about is correct; the
thing next to it is not, and I would not have looked there if the hand-back had not written
"this is where I would look hardest". That sentence is why this costs one correction instead
of six runs and a declared ceiling.
