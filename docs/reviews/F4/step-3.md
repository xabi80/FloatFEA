# Review — F4 step 3
Reviewed commit: b20cf2abe5dc820e2db13a855c39d3438b917d54
Verdict: HOLD
**Reviewed commit: `45e5242`** (`45e5242fe4edb59cb1966c65102cafac03b38102`, HEAD of F3,
tree clean when I judged it; my corpus batch 38 is committed on top at `b20cf2a`, which is
why the plain `Reviewed commit:` stamp above this line is not the commit I judged -- R718's
subject, now answered, and this bold line is the mechanism).
Tests: 3112 passed, 0 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `45e5242`, `753.75s`. Not the
report's figure.)

## Round of 2026-10-07 -- ROUND 1 OF THREE. HOLD ON TWO (b) ITEMS, BOTH FOUND BY RUNNING THE MODEL AT A CONFIGURATION THE DIFF DID NOT CHOOSE.

**THE VERIFY-FIRST ITEMS, COMPUTED.**

```
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-3.md
out    6352d8c report: F4 step 3 revision 1 -- R711, R718, EV1's counter families, ...
cmd    git rev-list --count 9de3e4e..HEAD   (at 45e5242, before my corpus commit)
out    7
judge  **SEVEN, NOT EIGHT.** The hand-back's list of seven names IS the range --
       377bace, 2564563, 9ec380e, 74c77d1, d291b65, 6352d8c, 45e5242 -- and the "plus one
       I may be miscounting" does not exist. Two of the seven are mine.
cmd    git log -1 --format=%h -- docs/reviews/F4/step-3.md ; head -5 docs/reports/F4/step-3.md
out    74c77d1 ; "Answers: verdict 104 @ 74c77d1"
judge  **1b SATISFIED, one comparison.** The report answers the NEWEST verdict state: the
       amendment at 74c77d1 is the newest commit touching the verdict file and it is the one
       the header names, not 9ec380e. R717's ordering note was acted on, which is the only
       reason section 0 could be generated at all.
```

**WHY IT IS A HOLD, IN THREE SENTENCES.** R711 and R718 are genuinely closed and I
reproduced both independently -- the discrete form line for line against
`newmark.py:375-460`, and R718's 53 / 13 / 40 / 7 counts to the digit. But the hand-back's
headline is **refuted**: EV1's window rule IS satisfiable on the moment channel, and the
reason it reads otherwise is that the shipped family filter admits a **vacuous** member
whenever that member's body happens to carry the case maximum -- at `T_full = 10`, hub3/11
clears hub3's own clean value by `4.9e-08` relative and becomes the family minimum.
Excluded, the weakest member over the three cases I ran is `1.752748714140e-02`, the
geometric centre against the global clean worst `2.3243458955783927e-06` is
`2.018414e-04`, and **both edges are `86.8379x`** where the shipped rule gives `0.6329x`.

**No STOP.** The verification ladder is SUCCESS at the reviewed commit in CI, no low rung
is red, nothing under `floatfea/` moved in this range, `.claude`, `docs/SUPERVISOR.md`,
`tests/conftest.py` and `floatfea/tolerances.py` are each untouched, and the plan is not
wrong. EV1's mass counter-case is genuinely under-sized on the moment channel and that is a
plan question for Xabier -- but the number to put to him is not the one in the report.

## 0. CI -- COMPLETE AND GREEN AT THE REVIEWED COMMIT

```
cmd    gh run list --commit 45e5242fe4edb59cb1966c65102cafac03b38102
         --json name,conclusion,workflowName,status,databaseId,event
out    [{"conclusion":"success","databaseId":37723495711,"event":"push","name":"CI",
out      "status":"completed","workflowName":"CI"}]
judge  **CA2 SATISFIED on the commit I am judging.** The run was `in_progress` when I was
       invoked and completed while I worked; an unfinished run is not a pass, so I waited
       rather than recording it as one. NOT CK2 -- the jobs ran.
cmd    for s in 6352d8c d291b65 74c77d1 ; do gh run list --commit $(git rev-parse $s) ; done
out    6352d8c  37723446599  completed  CANCELLED
out    d291b65  (no run)
out    74c77d1  (no run)
judge  the cancellation is the workflow's `concurrency: cancel-in-progress` rule and under
       CX0/R449 it reached no verdict on anything; no reason is attributed to it. d291b65
       and 74c77d1 were not the head of their push. **The hand-back was right that the runs
       in this range supersede each other and right not to claim one.** The run that matters
       is at HEAD and it is green.
out    377bace  FAILURE (52 reds)   2564563  FAILURE (51 reds)
judge  **EG3 STATE (2), AND I MATCHED EVERY ID RATHER THAN RULING A FAMILY.**
       `test_every_named_site_is_touched_or_declared`, `test_the_report_carries_the_finding`,
       `test_the_CI_section_is_about_the_REVIEWED_commit`,
       `test_the_Carried_table_is_what_the_generator_produces`,
       `test_the_generator_would_catch_a_row_under_the_wrong_number`, and ten
       `test_the_guard_survives_the_state` cascading off a red `[baseline]`. Nothing off
       EH1's corrected list. Not CZ0 (d): (d) is a red test at the REVIEWED commit, and at
       45e5242 my own run is 3112 passed, 0 failed. **EG3 condition (ii) is met** -- state
       (2) cleared at the report commit, measured by me and not taken from the report.
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST, AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 9de3e4e..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  NOT a STOP-class finding. Nothing in this range touches what I read, what I must
       carry or what I may write.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py
cmd    git diff --stat 9de3e4e..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (empty)
judge  CI0's check resolves to a real file; it is unchanged and no new conftest or plugin
       appears anywhere under tests/. CH2's six channels are closed by reading, which is the
       only way they can be closed.
cmd    git diff --stat 9de3e4e..HEAD -- floatfea/tolerances.py
out    (empty)
judge  **NOT ONE LINE.** No value, no counter, no comment. EU1 does not fire; I ran its
       adversarial case anyway, and sections 4 and 5 are it.
cmd    git diff --stat 9de3e4e..HEAD -- floatfea tests docs scripts .github data
out    docs/milestones/F4.md 2 | docs/reports/F4/step-3-answers.json 69 |
out    docs/reports/F4/step-3.md 705 | docs/reviews/F4/step-3.md 841 |
out    scripts/measure/g41_dynamic.py 293 | tests/test_report_carried.py 29
judge  **NOTHING UNDER floatfea/ MOVED AT ALL**, so there is no (a) in this range to find.
       Two of the six paths are mine. tests/test_report_carried.py is d291b65, a standalone
       `process:` commit touching that file and nothing else, citing R718 -- which is what
       EK2 and the reviewer-instruction rule ask for.
```

## 2. R711 -- CLOSED, AND I CHECKED THE TWO THINGS THE HAND-BACK SAID IT COULD NOT CHECK

The numerator at `scripts/measure/g41_dynamic.py:300-320` is now
`a_eff @ xi_ddot[n] - g_mid.T @ lam[n] - rhs` with the Jacobian at `0.5*(xi[n-1]+xi[n])`.
I did not take "mirrored line for line" on trust -- I checked it against the SOLVER, which
is the independent side.

```
cmd    sed -n '375,460p' ../HSP-runs/floatsim/solver/newmark.py
rule   docs/milestones/F4.md:131 and :486 -- the DISCRETE balance, newmark.py:414-437
out    solver: buffer.push(xi_dot_0) BEFORE the loop; mu_n = 0 at n = 0 explicitly; then
out    per step buffer.push(xi_dot_{n+1}) THEN mu_{n+1} = buffer.evaluate()
out    script: buffer.push(res.xi_dot[0]); mu = zeros; for i in 1..: push(xi_dot[i]) then
out    mu[i] = buffer.evaluate()
judge  **THE `mu` REBUILD IS IDENTICAL.** After the i-th push the buffer holds
       xi_dot_0..xi_dot_i, so evaluate() is mu_i, and mu[0] = 0 is the solver's own
       documented startup skip of the O(dt) artifact. This is the half the hand-back said it
       could not check because it mirrored `discrete_residual`; checking it against
       newmark.py is how that is closed, and it closes.
out    solver: F_np1_sd = _eval_state_force(t[n], xi_n, xi_dot_n) for the step producing n+1
out    script: force_at(i) adds state_force(t[i-1], xi[i-1], xi_dot[i-1]) under i > 0
judge  the lag matches for every step in any DQ6 window. force_at(0) omits the state term
       where the solver's F0 carries it -- one step at t = 0, nowhere near a window.
       Recorded, not a finding.
cmd    sed -n '116,133p' scripts/measure/g41_dynamic.py
rule   DQ6: the last 5 whole wave periods, starting no earlier than ramp + 10 periods;
       extend a run that is too short
out    window_duration = RAMP + 15*T, so end - 5T == RAMP + 10T exactly
out    window_slice: start = max(RAMP + 10T, t[-1] - 5T); lo = searchsorted(t, start)
out    measured: T=14 -> 990 steps, t = 29.810 .. 39.700 ; T=10 -> 707 steps,
out             t = 24.150 .. 31.210 ; T=15 -> 1061 steps, t = 31.220 .. 41.820
judge  **THE READING IS RIGHT AND THE RUN IS EXTENDED AS DQ6 REQUIRES**, not truncated. The
       two constraints coincide by construction, which is why the ramp floor never binds --
       correct behaviour and not a dead branch: it binds on a run longer than RAMP + 15T.
cmd    python scripts/measure/g41_dynamic.py --period 14      (my own run, at 45e5242)
rule   the window rule of docs/milestones/F4.md:145
out    force  worst 1.6159118708143226e-16  at hub3/T14
out    moment worst 1.4480755718208573e-06  at platform/T14
out    control: the per-joint decomposition reproduces `g_mid.T lam` to 2.015e-16 relative
out    control: whole-state discrete residual worst 1.107530e-04
judge  **EVERY FIGURE IN THE REPORT'S SECTION 2 REPRODUCES TO THE DIGIT**, both controls
       included. The force channel closes to round-off under the locked form, which is what
       made R711 worth catching before the runs were spent.
```

**The force-figure gap the hand-back asked me to rule on is NOT a finding.** My
`1.086249e-16` was a window maximum over 200 steps of a 12 s run at `t = 10.010 .. 12.000`;
the report's `1.6159118708143226e-16` is over 990 steps of a 39.70 s run at
`t = 29.810 .. 39.700`. Two different runs and two different windows, on a channel whose
absolute scale is `1e-16`. The moment figures agree to three figures because that channel
carries a real `O(h)` signal; the force figures agree in order only because there is no
signal there to agree about. **I attach no cause to the 1.49x** -- I did not run the cell
that isolates it, and no ceiling is declared from either number, so the measurement is not
owed. R711 **does not carry.**

## 3. R718 -- CLOSED, AND THE LARGER COUNT IS RIGHT

```
cmd    python <the newest 60 commits touching docs/reviews/: the plain ^Reviewed commit:
                header against the bold backticked judged line, in the same file state>
rule   test_the_CI_section_is_about_the_REVIEWED_commit asserts the section is about the
       commit the verdict JUDGED
out    commits touching docs/reviews examined: 60
out    states carrying BOTH lines           : 53
out    plain header == bold judged (prefix) : 13
out    plain header DIFFERS from bold judged: 40
out    states with NO bold line at all      :  7
out      DIFFERS 488f2d8 F4/step-2  plain 4f99c7f  judged 7cee09f
out      DIFFERS 5786bed F4/step-1  plain 6e39151  judged 84de436
out      DIFFERS 9f75cd5 F4/step-1  plain 9285a9f  judged b0824d5
out      DIFFERS de9a448 F4/step-1  plain 3d6fdb6  judged 7c8e4ae
out      DIFFERS 3a908fa F4/step-1  plain 80e24df  judged a7fefba
judge  **53 / 13 / 40 / 7 -- EVERY NUMBER THE COMMIT MESSAGE AND THE REPORT PUBLISH, TO THE
       DIGIT.** The hand-back's count is right and larger than mine; my 23 of 35 over 40
       commits was the smaller sample and the conclusion is worse than I measured it.
cmd    sed -n '2082,2116p' tests/test_report_carried.py
out    `return m.group(1) if m else ""`, and the existing `assert judged` whose message
out    already names the bold backticked form
judge  **THE FALLBACK IS GONE AND THE ASSERTION IS WHAT FIRES** -- my condition's first
       branch exactly. The removal reddens nothing legitimate: my own whole-suite run at the
       reviewed commit is 3112 passed, 0 failed, 0 skipped. What it DOES do is make the
       guard refuse on any verdict written through write_verdict.py without a hand-added
       bold line, which is seven of the newest sixty states. That is the intended behaviour
       and R717 is its answer at the producer. **R718 does not carry.**
```

## 4. THE HEADLINE, RULED -- THE WINDOW RULE IS SATISFIABLE, AND THE DIAGNOSIS STOPS ONE STEP SHORT

I was asked to rule on three things and I do, from my own runs at `T_full = 10`, `14` and
`15`: the shipped script with print-only instrumentation, ER0's basis, DQ6's own window.

**(1) IS THE DIAGNOSIS RIGHT? HALF OF IT.** The per-case/global mismatch is real and is one
of the two root causes. What it misses is that the member making the rule fail is
**vacuous**, and that its admission is decided by the very round-off excess that proves it
vacuous. The hand-back quotes "9.309128e-07 against 9.309128e-07, marginally" and reads the
marginal clearing as a legitimate pass. It is not one.

```
cmd    python <the shipped measure_case, instrumented to print, for every moment-family
                pair, drop_rel, its ratio to the CASE clean worst, and its ratio to its OWN
                BODY's clean value>
rule   scripts/measure/g41_dynamic.py:428 -- drop_rel_m = {k: v for k, v in all_m.items()
       if v > clean_m_worst}, with clean_m_worst at :426 the max over the five FE bodies IN
       THIS CASE
out    T_full = 10   case clean worst 9.309127595066468e-07  (hub3 -- hub3 IS the maximum)
out      hub1/3   drop_rel 6.419583706073e-07  /caseworst 0.689601001  /ownclean 1.000000108009  IN=False
out      hub3/11  drop_rel 9.309128055654e-07  /caseworst 1.000000049  /ownclean 1.000000049477  IN=True
out      hub3/8   drop_rel 1.752748714140e-02  /caseworst 18828.281    /ownclean 18828.281127744427  IN=True
out    T_full = 14   case clean worst 1.4480755718208573e-06  (platform IS the maximum)
out      hub3/11  drop_rel 6.021071415490e-07  /caseworst 0.415798148  /ownclean 1.000002160674  IN=False
out      hub1/3   drop_rel 9.211057536872e-07  /caseworst 0.636089560  /ownclean 1.000003140535  IN=False
out      hub4/12  drop_rel 1.816033296779e-02  /caseworst 12541.012    /ownclean 26796.556196920323  IN=True
judge  **hub1/3 AND hub3/11 ARE VACUOUS IN BOTH CASES** -- own-clean ratios 1.000000049477,
       1.000000108009, 1.000002160674, 1.000003140535. Dropping either joint moves its own
       body's moment residual by between 4.9e-08 and 3.1e-06 relative. **hub3/11 is
       ADMITTED at T=10 for one reason: hub3 happens to be that case's maximum, so the
       per-case worst IS hub3's own clean value and the strict `>` is a number compared with
       itself to the last bits.** The next member above it is 18828.3x away.
```

**(2) IS DECLINING TO DECLARE CORRECT? YES, AND FOR A STRONGER REASON THAN THE ONE GIVEN.**
A ceiling declared by the window rule from a family minimum that is a vacuous member would
have been declared from a number that certifies nothing -- "never widen" arriving through a
derivation rather than an edit. The refusal is right; the conclusion attached to it is not.

**(3) SHOULD A CEILING HAVE BEEN DECLARED BY ONE OF THE THREE RESOLUTIONS? NO, AND NONE OF
THE THREE IS NEEDED.**

```
cmd    python <the window rule, over the three cases I ran, with and without the vacuous
                member>
rule   docs/milestones/F4.md:145-148 -- the geometric centre between the clean worst and the
       weakest counter response, BOTH EDGES >= 2x
out    clean worst (global over the 3 cases)   2.3243458955783927e-06  platform/T15
out    AS SHIPPED, vacuous member admitted     weakest 9.309128e-07
out      centre 1.470974e-06   lower edge 0.6329x   upper edge 0.6329x   both >= 2x: False
out    VACUOUS MEMBER EXCLUDED                 weakest 1.752748714140e-02  (hub3/8 at T=10)
out      centre 2.018414e-04   lower edge 86.8379x  upper edge 86.8379x   both >= 2x: TRUE
out    per-case weakest ADMITTED member: T10 9.309128e-07, T14 1.816033e-02, T15 2.451485e-02
judge  **THE WINDOW RULE CLOSES, AT 86.8x ON BOTH EDGES, ON THE JOINT-DROP COUNTER ALONE.**
       Resolution 1 (test against the global clean worst) is half the repair, and here it
       would exclude hub3/11 BY LUCK of which case carries the global maximum -- the same
       defect with the opposite sign. Resolution 2 (thirty ceilings) changes what EV1 locked
       and buys nothing the vacuity test does not. Resolution 3 is about the MASS counter,
       not this one, and the number offered for it is refuted in section 5. Three cases is
       not thirty and the figures will move; the MECHANISM will not.
```

## 5. THE MASS COUNTER -- "THE RESPONSE IS LINEAR IN THE SCALE" IS FALSE, MEASURED

This is EU1's adversarial case run where EU1 does not require one: the model at an injection
scale the diff did not choose.

```
cmd    python <the shipped script, T=14, everything held but the injection scale -- set to
                the one value `need` itself publishes as the 2x edge>
rule   scripts/measure/g41_dynamic.py:462-463 "The response is linear in the scale, so the
       smallest usable scale is reported rather than guessed", and :471
       need = 1.0e-6 * 2.0 * clean / got
cell   ONE VARIABLE MOVED: eps 1.0e-06 -> 4.816e-06. Same case, same window, same basis.
out    eps 1.0e-06    weakest moment 6.013115e-07   predicts 1 + 4.816e-06
out    eps 4.816e-06  weakest moment 6.034193e-07   predicts 1 + 2.311e-05
judge  **A 4.816x LARGER INJECTION MOVED THE RESPONSE BY 0.35%.** The response is not linear
       in the scale; it is flat, because `got` is min_k max_t |resid_mass_k| / den_m_k, which
       INCLUDES the clean residual floor, and on the moment channel the floor dominates. So
       1 + 4.816e-06 -- published in the report's section 3 and in 6352d8c -- does not
       bracket at the scale it names, and the formula then asks for 4.8x more again.
cmd    python <the same run, instrumented to record the PURE injected signal
                max_t |resid_mass - resid| per body, which IS linear in eps by construction>
out    pure signal at eps = 1e-6, moment channel, relative:
out      platform 2.735299e-08   hub1 4.191758e-09   hub2 2.538043e-09
out      hub3 3.456107e-09       hub4 2.538043e-09
out      their clean values: 6.777114e-07 on hub2 and hub4 -- 267x the signal
out    weakest pure signal: force 1.386550e-07   moment 2.538043e-09
out    the shipped `got` for comparison: 6.013115e-07, which is hub3's clean 6.021058e-07
out    solved eps for the weakest PURE signal to reach 2x the GLOBAL clean worst:
out      moment  1 + 1.831605e-03      force  1 + 2.676582e-15
judge  **THE PUBLISHED "COUNTER RESPONSE" ON THE MOMENT CHANNEL IS A CLEAN VALUE.**
       6.0131e-07 is hub3's own clean residual to three figures; the 1e-6 mass perturbation
       is 267x below the floor at the body that sets the minimum. That is R689's shape -- a
       row that compares nothing reading as agreement -- arriving in the MASS counter one
       commit after the same shape was found and named in the joint-drop family. The solved
       scale is 1 + 1.831605e-03: **380x the published 1 + 4.816e-06 and 41x the hand-back's
       1 + 4.499e-05**, and it is a lower bound because I ran three cases, not six. **And
       the force channel is where the formula is accidentally right** -- the signal
       1.386550e-07 sits four decades above the floor 1.615912e-16, so there `got` IS the
       signal and the printed 1 + 2.331e-15 agrees with the solved 2.676582e-15. Reading the
       formula on the force channel certifies nothing about the moment channel, which is the
       same channel asymmetry that let R711 survive a reading.
```

## 6. THE MASS INJECTION'S ALGEBRA -- ASKED, AND THE CHOICE IS RIGHT

`:339-345` reforms both `a_eff` and the `alpha_m M xi_ddot_{n-1}` inside `rhs`. **That is
correct and it is the right reading of EV1.** The question the counter asks is whether the
gate notices a mass matrix wrong by `1e-6`; a wrong `M` is wrong in every place the residual
reads it, and reforming one occurrence alone would inject an inconsistency the integrator
never had -- which is the script's own comment and it is sound. The hoist of `a_eff_s` to
`:297` is pure constant folding and I verified it changes nothing: my T=14 run at `45e5242`
reproduces `6.013115e-07` exactly. **I did not measure the inconsistent alternative and I
make no claim about its size.**

## 7. TRY TO BREAK IT -- WHAT I RAN AND WHAT IT SAID

* **The gate at a case the diff did not choose (`T_full = 10`)** -- found R719. The family
  minimum is a vacuous member admitted by a `4.9e-08` relative excess.
* **The gate at `T_full = 15`** -- confirmed the global clean worst `2.324346e-06` and that
  the vacuous set there is `{hub1/3, hub3/11}`, the same set as T=14 and not a case-dependent
  one.
* **The injection at the scale the script's own formula names** -- found R720. `4.816x` more
  injection, `0.35%` more response.
* **The pure injected signal separated from the clean floor** -- `2.538043e-09` against a
  floor of `6.777114e-07`. The published counter response is the floor.
* **The window rule solved both ways, with and without the vacuous member** -- `0.6329x`
  against `86.8379x`. EH4's weakening direction is the one that bites here: the rule reads
  UNSATISFIABLE, which is the direction that invites a plan reopening nobody needs.
* **The `mu` rebuild against `newmark.py:375-460` rather than against its own mirror** --
  identical, including the `mu[0] = 0` startup skip.
* **DQ6's window arithmetic at three periods** -- 707 / 990 / 1061 steps, the ramp floor and
  the five-period rule coincident by construction, the run extended and not truncated.
* **R718's count over 60 commits** -- 53 / 13 / 40 / 7, every figure reproduced.
* **The whole suite at the reviewed commit** -- `3112 passed, 0 failed, 0 skipped`.

## Findings

**R719. (BLOCKING -- (b): a counter and how it is injected, through the
generator-is-the-gate carve-out) THE JOINT-DROP FAMILY'S MEMBERSHIP RULE ADMITS A VACUOUS
MEMBER WHENEVER THAT MEMBER'S BODY CARRIES THE CASE MAXIMUM, AND THAT MEMBER IS THE NUMBER
THE WINDOW RULE WAS DECLARED UNSATISFIABLE FROM.**
`scripts/measure/g41_dynamic.py:426` (`clean_m_worst`, the max over the five FE bodies in
this case) and `:428` (`drop_rel_m = {k: v for k, v in all_m.items() if v > clean_m_worst}`).
The rule conflates two different properties into one strict inequality: **vacuity** -- is
dropping this joint detectable on THIS body at all -- and **bracketing** -- does this member
exceed the ceiling the window rule will declare. Measured at `T_full = 10`, `14` and `15`,
shipped script, ER0's basis, DQ6's window:

* `hub1/3` and `hub3/11` are vacuous in **both** cases measured: drop response over own
  body's clean value `1.000000108009` and `1.000000049477` at T=10, `1.000003140535` and
  `1.000002160674` at T=14. Those joints sit at those hubs' reference points and the geometry
  does not vary with the wave period.
* `hub3/11` is nonetheless **admitted** at T=10, because hub3 is that case's maximum, so
  `clean_m_worst` IS hub3's own clean value and the test reads
  `9.309128055654e-07 > 9.309127595066468e-07` -- a `4.9e-08` relative excess, the same
  quantity that makes it vacuous.
* It is then the family minimum over the whole domain, `9.30912805565388e-07`, below the
  global clean worst `2.3243458955783927e-06`, which is why the window rule reads
  unsatisfiable with both edges at `0.6329x`.
* Excluded, the weakest member over the three cases is `1.752748714140e-02` (hub3/8 at T=10),
  the geometric centre is `2.018414e-04`, and **both edges are `86.8379x`**. The gap between
  the vacuous pairs and the weakest genuine member is `18828.3x` at T=10 and `12541.0x` at
  T=14 -- four decades of empty space, so nothing in this family is a marginal member and no
  margin here is a tuned number.
* **And the "CASE-DEPENDENT vacuous set" claim is false.**
  `scripts/measure/g41_dynamic.py:439-448`, the report's section 3 and `45e5242`'s commit
  message all state that which pairs are vacuous varies with the case, and attribute it to
  hub3/11's locked-axis moment varying. What varies is which body carries the case maximum --
  platform at T=14 and T=15, hub3 at T=10. The own-clean ratios are the quantity that decides
  it and they were never taken.
* **A gate carries its own failure.** A counter-case whose family contains `hub3/11` asserts
  `drop_rel > COUNTER` on a quantity that IS hub3's clean residual. If the thing that member
  claims were false, it would not go red.

**Closed when** the two properties are separated: a **vacuity** test on
`drop_rel[k,j] / clean_rel[k]` against a stated margin, with that margin's own boundary
solved in both directions (EH4); and a **bracketing** test against the GLOBAL clean worst
over all 30 body-cases rather than the per-case maximum. The window rule's two edges are then
re-measured over the six cases and pasted, and my `86.8379x` over three cases is beaten or
refuted at a named operating point. **The case-dependence sentence is made true or deleted
(CW0)** at `:439-448`, in the report, and in the published claim, with the own-clean ratios
pasted since those are what decide it. **No new apparatus either way: it is the expression at
`:427-428` plus one ratio.**

**R720. (BLOCKING -- (b): how the counter is injected, and the size it has to be)
"THE RESPONSE IS LINEAR IN THE SCALE" IS FALSE ON THE MOMENT CHANNEL, SO EVERY PUBLISHED
"SMALLEST SCALE FOR A 2x EDGE" IS AN EXTRAPOLATION THROUGH A FLOOR.**
`scripts/measure/g41_dynamic.py:462-463` (the claim) and `:471`
(`need = 1.0e-6 * 2.0 * clean / got`). `got` is `min_k max_t |resid_mass_k| / den_m_k` -- the
residual computed with the scaled `M`, which includes the clean residual floor. On the moment
channel the floor dominates the injected signal by `267x` at the body that sets the minimum,
so `got` is not a response and is not linear in the scale. Measured, one variable moved
(BG0), T=14, same window, same basis:

```
eps 1.0e-06    weakest moment 6.013115e-07   predicts 1 + 4.816e-06
eps 4.816e-06  weakest moment 6.034193e-07   predicts 1 + 2.311e-05
```

and the pure signal, which IS linear by construction:

```
max_t |resid_mass - resid| / den_m at eps 1e-6, moment channel: platform 2.735299e-08,
  hub1 4.191758e-09, hub2 2.538043e-09, hub3 3.456107e-09, hub4 2.538043e-09
the shipped `got` of 6.013115e-07 is hub3's own clean value 6.021058e-07
solved eps for the weakest pure signal to reach 2x the GLOBAL clean worst:
  moment 1 + 1.831605e-03      force 1 + 2.676582e-15
```

So the report's `1 + 4.816e-06` is **380x** short and the hand-back's `1 + 4.499e-05` is
**41x** short, and both describe a quantity that is mostly a clean residual. `need` is also
computed against the PER-CASE `clean` where the ceiling is global, which costs a further
factor of up to `22.5807x` -- the measured clean moment spread over the three cases. **The
force channel is where the formula is accidentally right** (`1 + 2.331e-15` printed against
`2.676582e-15` solved), because there the signal sits four decades above the floor.
**Closed when** the injected signal is measured as `max_t |resid_mass - resid|` rather than
`max_t |resid_mass|`, the 2x edge is solved against the global clean worst, and the published
scale is **re-measured at the scale it names** instead of extrapolated -- or the linearity
sentence is deleted and the boundary bisected. EV1 specifies `1 + 1e-6` and changing that is
Xabier's, not a round; **what blocks is that the figure put to him be the measured one.** One
expression, no new apparatus.

## Closure items

Per CZ0, named with their site and what would close each, fixed once in the step's closure
commit, not re-reviewed item by item, and the step is not held on any of them.

**C24. The dead `per_joint_contributions` builds the Jacobian at the point R711 forbade, and
the LIVE function's docstring defines itself by reference to it.**
`scripts/measure/g41_dynamic.py:156-173` is unreachable -- `grep -n per_joint_contributions`
gives one call site, `:324`, and it calls `per_joint_contributions_from`. The dead function
calls `setup.constraints.jacobian(xi)`, which is exactly the non-midpoint argument R711 was
about, and `:137` reads "As `per_joint_contributions`, but from a Jacobian the caller already
has" -- so the live function's documentation points a reader at the form the plan does not
lock. **Closed when** the dead function is deleted and `:137` states the form directly.

**C25. The report's figures describe the script at `45e5242`, one commit after the report.**
`docs/reports/F4/step-3.md` section 2's `2.015e-16` and `1.107530e-04`, section 3's per-pair
table and its `1 + 4.816e-06` were produced by the script as it exists at `45e5242`, which is
a later commit than the report's own `6352d8c`. I verified they reproduce exactly at HEAD, so
nothing in them is false about the tree under review -- but CP3's ordering is "generate, edit,
re-run, paste, commit, and if an edit follows the paste the paste is void", and here the edit
followed in a separate commit. **Closed when** the next revision states which commit the
figures describe, or the code and the report land in one commit.

**C26. The whole-suite figure is taken at the verdict commit and the "would print the same"
sentence is now false.** The report's section 11 publishes `2856 + (166 + 83)` at `74c77d1`
and says re-running `suite_count.py` prints the same two numbers. My own run at the reviewed
commit is **3112 passed, 0 failed, 0 skipped**, against the report's `3105` total, because the
report's own new site and finding rows add parametrisations. R637 clause (iii)'s whole subject
is the whole-suite line measured at the commit it describes. **Closed when** the figure is
taken at the report's own commit, or the sentence says which commit it is a figure for.

**C27. The marker moved in the report commit again, and the plan's own section 2.4 says the
first commit.** `docs/milestones/F4.md:3` advanced from `2` to `3` in `6352d8c`. The
implementer records that the guard demands it ("The line is advanced in the commit that adds
the next step's report, never before it") and reverted an early move at `27ecf62`. The plan's
section 2.4 says the first commit and already records this deviation once, as C136. The
measured cost is 52 and 51 CI reds at `377bace` and `2564563`, all on EH1's state (2) list.
**The guard and the locked plan disagree and the guard is winning silently.** **Closed when**
section 2.4 is corrected to match the guard, or the disagreement is written down as a plan
question for Xabier.

**C1 (carried, and its own trigger has now passed).** Verdict 102 required C1 "answered
BEFORE the G4.1-dynamic quantity is chosen, because that choice is (c) and this is its
input". The quantity IS now chosen -- discrete, two channels, moments about the reference
point -- and `scripts/report_joint_reactions.py` is untouched in this range, so the inverted
dimensional sentence at `:238` and the incomplete "on all seventeen" claim are still there.
I keep it closure class under CZ0 and I do not hold the step on it, but it must land before
either ceiling is declared, not in the closure commit after.

**R712, R713, R714, R716, R717 (carried, declared, still open).** All five are correctly
declared as untouched in the report's section 8a and listed in section 9. None holds the
step. R717's producer repair is the thing that would stop the next verdict from needing a
hand-added bold line, and I have added one again.

## Tolerances touched

```
cmd    git diff 9de3e4e..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff d4e2136..HEAD -- floatfea/tolerances.py | grep -E "^[-+][A-Z0-9_]+:"
out    (no output)
judge  **NOT ONE LINE OF THAT FILE CHANGED IN THIS RANGE**, so no ceiling, no counter and no
       comment moved. EU1 does not fire. I ran its adversarial case anyway -- the gate at two
       cases the diff did not choose and the injection at a scale the diff did not choose --
       and both findings came out of it, which is EU1's own reason for existing.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| G4.1 dynamic force (DQ8 / EV1) | -- | **none declared** | dimensionless, relative, denominator a sum of magnitudes | joint drop: weakest `1.426891e-01` to `2.020284e-01` over the three cases I ran, `1.0e+15x` above the clean worst; mass `1+1e-6`: `1.386550e-07`, `8.6e+08x` above | `scripts/measure/g41_dynamic.py:300-360`; plan `docs/milestones/F4.md:117-148`, `:486` | **THE REFUSAL TO DECLARE IS CORRECT.** The channel closes to round-off (`1.6159118708143226e-16` at hub3/T14, `1.552257e-16` at hub4/T15, `1.191949e-16` at hub4/T10) and both counters bracket it by fifteen and nine decades. Nothing here blocks; the declaration waits on the six-case run. |
| G4.1 dynamic moment (DQ8 / EV1) | -- | **none declared, and none may be declared from the current family rule** | dimensionless, relative, denominator a sum of magnitudes | joint drop: shipped weakest `9.309128e-07` is a VACUOUS member (R719); corrected weakest `1.752748714140e-02`. Mass `1+1e-6`: the reported `6.013115e-07` is hub3's own clean value (R720) | `scripts/measure/g41_dynamic.py:423-430`, `:461-475`; plan `:145-148` | **THE REFUSAL IS CORRECT AND THE REASON PUBLISHED FOR IT IS NOT.** The window rule closes at `86.8379x` on both edges once the vacuous member is excluded, against the `0.6329x` the hand-back reports. R719 and R720 are both here, and both are (b): the family membership rule and the injection size are "a counter and how it is injected". |
| the FE acceleration assertion (DQ8's second bullet) | -- | **not measured in this range** | normalised by `max_t |a|` and `max_t |alpha|` | -- | plan `docs/milestones/F4.md:140-141` | **NOT YET MEASURED AND NOT YET DUE.** Recorded so it is not lost: DQ8 asks for the FE inertia-relief acceleration against FloatSim's, per body, and nothing in this range measures it. It is step 3's remaining work, not a finding. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. Verdict 103 measured all nine clean or ruled, and verdict 104 reproduced the two that moved. |

## Carried

Verdict 104 (`9ec380e`, amended at `74c77d1`) was an ES0 interim check judging `9de3e4e`. It
raised two blocking items and carried six closure ones. Every one, with status.

* **R711 (blocking) -- CLOSED**, at the first branch of my condition. Answered at `377bace`,
  `scripts/measure/g41_dynamic.py:253-320`: the numerator is the discrete residual, the
  Jacobian is at `0.5*(xi[n-1]+xi[n])`, and `rhs` carries both generalized-alpha weights,
  both damping terms, `alpha_m M xi_ddot_{n-1}` and the rebuilt `mu[n-1]`. Section 2: I
  reproduced the `mu` rebuild against `newmark.py:375-460` rather than against its own
  mirror, the state force's lag, the midpoint argument, and every figure in the report's
  section 2 to the digit. The docstring at `:20-38` now says which balance it forms and why
  the sentence had to be earned, so CW0 is satisfied. **Does not carry.**
* **R718 (blocking) -- CLOSED**, at the first branch of my condition. Answered at `d291b65`,
  a standalone `process:` commit touching `tests/test_report_carried.py:2082-2116` and
  nothing else and citing the directive. The fallback is gone, `assert judged` is what fires,
  and I reproduced 53 / 13 / 40 / 7 over sixty commits exactly -- the larger sample is right
  and worse than mine was. **Does not carry.**
* **R712 (closure) -- STILL OPEN**, correctly declared.
  `scripts/report_joint_reactions.py:120` still ships `PLATFORM_MASS_OVERRIDE = None`, the
  override is typed in `g41_dynamic.py`'s caller, and the joint count is still inferred
  rather than asserted. Into the closure commit.
* **R713, R714, R716, R717 (closure) -- STILL OPEN**, all four correctly declared as
  untouched in section 8a and listed in section 9. R717's ordering half WAS acted on, which
  is the only reason this step's report could be generated.
* **R715 (closure) -- WITHDRAWN by the implementer, and I agree.** It was my finding about
  the implementer's docstring; section 7 withdraws the overstatement with its evidence, and
  the branch taken -- the moment about the reference point -- stays ruled right.
* **C1 (closure, conditioned) -- STILL OPEN AND NOW PAST ITS TRIGGER.** See the closure list.
* **C2 to C23 (closure)** -- carried unchanged into `docs/closure/F4.md` and NOT
  re-adjudicated, per verdict 103's instruction. C21 does not recur; the range count is seven
  rather than the eight offered.
* **The two self-reported `black --check` counts** -- recorded in the report's section 9,
  both pushed, neither re-litigated. Self-reporting them before I looked is the practice I
  have been asking for. Closure class.
* **Verdict 103's escalation -- unchanged and not re-argued.** Two consecutive steps closed
  carrying; the choice stated was reduce scope rather than slip. Step 3 is now carrying two
  blocking items of its own at round 1, and both are in the derivation of the one tolerance
  pair step 3 exists to declare. **If they are still open at revision 2, that is a third
  consecutive step and the choice has to be made rather than restated.**

## The adversarial corpus (BE3)

**BATCH 38 -- `tests/corpus/g41_dynamic_counter_family_vacuity.txt`, 15 entries, ALL NEW**,
committed separately at `b20cf2a`.

* **Coverage this round: 15 new entries; the check under review places 4 of them correctly.**
  Of the twelve I measured, **4 caught and 8 not**; three are recorded `caught=not-run` with
  no claim made. The eight misses are the two root causes behind R719 and R720 and their
  consequences -- a vacuous member on the case-maximum body, the false case-dependence, the
  family minimum, the sub-floor injection, the linearity assumption, the per-case reference,
  the solved scale, and a family size asserted while the membership that varies is not.
* **The coordinate the author never varied is WHICH BODY CARRIES THE CASE MAXIMUM.** The
  filter was written and checked at `T_full = 14`, where the platform carries it and both
  vacuous pairs fall out correctly. At `T_full = 10` hub3 carries it and one of them walks
  through. Same shape as R682, R694, R704, R706, R708 and R710 -- a check calibrated at one
  point of its own domain -- which is why this is a corpus file and not a note.
* **EG4(e) justification, stated rather than assumed.** Batches pause to 28 October except
  mutation work on the two surfaces where a miss reaches a member force. Member forces are
  static + dynamic (EK0(f)), the dynamic half is `res.lam` at the sixteen joints, and
  G4.1-dynamic is the only gate measuring whether that balance closes. That is the surface.
* **Still owed at the 28 October batch, unchanged:** F4's load-mapping gate (a defect
  identical on all five bodies; a block moved between two nodes at the same position), EB6's
  gate per C5 (permutations that PRESERVE the count), the shared-attribute corpus for
  DQ4(i), the aggregation-direction corpus, and the residual-form corpus added last round --
  **of which this batch is the first half**, R711 and R719 being the same species.
* **My own hygiene item, carried from verdicts 101 to 104 and still mine:**
  `tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48, 49 and 50 carry
  `measured=` figures on the OLD mass basis. I re-head that file at the 28 October batch.

## Next step opens when

**Step 3 stays open. This was ROUND 1 of three; two revisions remain.** What revision 2 must
do before anything else:

1. **R719 is answered** -- the vacuity test separated from the bracketing test, the vacuity
   margin's own boundary solved in both directions, the bracketing test taken against the
   GLOBAL clean worst, and the window rule's two edges re-measured over all six cases with my
   `86.8379x` beaten or refuted at a named operating point. **The "case-dependent vacuous
   set" sentence is made true or deleted** at `scripts/measure/g41_dynamic.py:439-448`, in the
   report and in the published claim.
2. **R720 is answered** -- the injected signal measured as the DIFFERENCE
   `max_t |resid_mass - resid|`, the 2x edge solved against the global clean worst rather
   than extrapolated through a floor, and the published injection scale re-measured at the
   scale it names. If EV1's `1 + 1e-6` genuinely cannot bracket the moment channel, the
   figure that goes to Xabier is the measured one and not `1 + 4.816e-06` or `1 + 4.499e-05`.
3. **C1 lands with them**, because verdict 102 conditioned it on being answered before this
   quantity is chosen, and the quantity is now chosen.
4. **Then the ceilings may be declared** -- both in `floatfea/tolerances.py` with their plan
   rows in the same commit (BR0), each with a counter whose weakest family member is measured
   over all 30 body-cases, both edges of the window rule stated, and both boundaries solved
   including the two that weaken the gate (EH4).
5. **Step 3's locked remainder is unchanged by this round and is not reopened:** the
   member-force table per member and per case at every element node, the six-case envelope,
   the `f` sensitivity, DQ8's FE-against-FloatSim acceleration assertion, R638, R637 clause
   (iii), and `docs/closure/F4.md` with G4.5's measured rate and DQ6's cycle-to-cycle
   measurement. The schedule paragraph says 14 October and holds; I add only that two
   blocking items at round 1, with EV2 items 2 to 5 unstarted, is not a comfortable position.

**What I will not accept at revision 2.** A G4.1-dynamic moment ceiling declared from a
family whose minimum is a member whose drop response equals its own body's clean value, or a
counter scale extrapolated from a quantity that is mostly a clean residual. Neither of those
is a judgement about figures. They are the same single question -- if the thing this member
claims were false, would it go red -- and for the two numbers the hand-back's headline rests
on, the answer measured out as no.

## On the criterion -- I was asked, and I agree, with the same single note

CZ0 is right and I applied it. Four findings went to the closure class this round without
argument, including C27, where a guard and the locked plan disagree and I would have enjoyed
arguing it is (c). It is not: no gate assertion moved.

**The note, said once and unchanged from verdict 104.** Both of my blocking findings are in
`scripts/`, which CZ0 lists under "generators" as closure class, and I block on them under
the carve-out my own instructions give -- "a generator whose output *is* a gate's assertion".
Under EV3 every report figure comes from `scripts/measure/`, and under
`docs/milestones/F4.md:486` the G4.1-dynamic ceilings are declared from the figures measured
there, so EV3 moved the derivation of a (b) value out of the step report -- which is
regenerated by rule -- and into `scripts/`. **A script under `scripts/measure/` whose output
is a declared tolerance's derivation is (b) while it is being used that way.** The hand-back
says it agrees and has put it to Xabier; I rule under it until he says otherwise. If he rules
the other way, R719 and R720 become closure items, step 3 may close carrying them, and the
two numbers in sections 4 and 5 are what a reader of `docs/closure/F4.md` will need -- they
should go there verbatim rather than be re-derived.

**And one thing on the record for the implementer rather than against them.** The hand-back
named the file it had already found five defects in, said which two of its properties it
could not check itself, volunteered three errors of its own before I could find them, and
asked me to attack its headline rather than confirm it. I attacked the headline and it broke.
That is the hand-back working as intended: the two things it asked me to check -- the `mu`
rebuild and `window_slice` -- are both correct, and the finding sits next to them in the one
place it did not think to look twice, which is the configuration it did not run.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

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
