# Review — F4 step 3
Reviewed commit: d39e34a9e80839881e646b4f4ca7449c779f635c
Verdict: HOLD
**Reviewed commit: `d09a237`** (`d09a2370a258c30e540b3bdf1df15696e83b2e2c`, HEAD of F3,
tree clean when I judged it; my corpus batch 39 is committed on top at `d39e34a`, which is
why the plain `Reviewed commit:` stamp above this line is not the commit I judged -- R718's
subject, and this bold line is the mechanism.)
Tests: 3267 passed, 8 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `d09a237`, `713.35s`. Not the
report's figure.)

## Round of 2026-10-08 -- ROUND 2 OF THREE. HOLD. ONE REVISION REMAINS.

**WHY IT IS A HOLD AND NOT A PASS, IN FIVE SENTENCES.** R721 is substantively closed and I
verified it the only way that counts: the verification ladder is **SUCCESS in CI, rung 4 and
rung 5 both, at `8ae9acc`, at `380184e` and at `d16a46b`**, on runners with no HSP worktree,
where two commits earlier 124 of 126 cases errored. But the step boundary did not clear --
`test_the_answered_verdict_is_the_NEWEST_one` is RED at the reviewed commit because revision
2 `Answers:` line names the commit verdict 106 **reviewed** instead of the commit it was
**written at**, and seven planted states cascade off that red baseline (R725, CZ0 (d)). The
staleness defence the hand-back asked me to attack hardest does not hold: I constructed the
stale-but-accepted state, ran it, and got `112 passed` (R726). Two more blocking items came
out of running the declaration at values the diff did not choose -- a ceiling that may rise
eleven decades past its own counter with nothing red (R727), and one constant that is a
floor in three assertions and a ceiling in a fourth (R728) -- plus the injection size EV1
locks and nothing asserts (R729). Each repair is one or two lines and no new file.

**No STOP.** No low rung is red; the ladder is green locally and in CI at the reviewed tree;
the plan re-locked by EX is right and I am not reopening it. `.claude`,
`docs/SUPERVISOR.md` and `tests/conftest.py` are untouched in this range.

**And one thing on the record before the findings.** Verdict 106 was a STOP and this revision
answered all four of its findings, with every published figure in the re-derived tolerance
entries reproducing on my own independent run. The seven self-reported findings in section 6
are the practice I keep asking for, and the pattern the report draws from them -- the work
done *around* a repair inherits none of the discipline applied *to* it -- is correct and is
why I went looking where I did. Four of my five findings came from running the gate at a
value the commit did not choose, which is EU1 whole argument; the fifth came from running
the suite. None of them is a figure or a sentence.

## 0. CI -- THE LADDER IS GREEN, AND THE REVIEWED COMMIT HAS NO RUN BY DESIGN

```
cmd    gh run list --commit d09a2370a258c30e540b3bdf1df15696e83b2e2c --json ...
out    []
cmd    gh run list --limit 15 --json databaseId,headSha,conclusion,status
out    newest run 37796814444 at d16a46b, completed, failure
cmd    git diff --stat d16a46b..HEAD -- tests scripts .github floatfea data
out    (empty)   -- the only change in this commit is docs/reports/F4/step-3.md, 931 lines
cmd    head -25 .github/workflows/ci.yml
out    paths-ignore: docs/reports/**
judge  **CA2, THE THIRD STATE, AND IT IS NOT CK2.** There is no run at the reviewed commit
       because the commit touches only an ignored path. That is an UNAVAILABLE check and I
       record it as that rather than skipping over it -- and the condition my instructions
       attach to it is satisfied: no code moved since the last run that executed, so
       `d16a46b` result describes the tree under review. NOT CK2: the jobs ran, and the
       guards step took 338 s.
cmd    gh run view <id> --json jobs   for 37790839814 / 37794940102 / 37796814444
out    the verification ladder     SUCCESS   SUCCESS   SUCCESS
out        ladder 4 -- the loads are the loads     success  success  success
out        ladder 5 -- independent confirmation    success  success  success
out    lint, unit and guards       failure   failure   failure
out        actionlint, ruff, black, mypy, unit tests   success on all three runs
out        guards and meta-tests                      failure on all three runs
judge  **R721 IS CLOSED AND THIS IS THE MEASUREMENT THAT CLOSES IT.** Rung 4 ran and passed
       on three successive CI runs on ubuntu-latest with no HSP-runs beside it, and rung 5
       -- which was SKIPPED behind the red at `f07bcb8` -- ran and passed too. The controlled
       pair is free and it is in the history: `becf47c` green, `f07bcb8` ladder-4 FAILURE
       with 124 errors, `8ae9acc` green again with the data path replaced.
cmd    gh run view 37796814444 --log-failed | grep -oE FAILED.tests/[^ ]* | sort | uniq -c
out    15 test_report_carried.py::test_the_Carried_table_is_what_the_generator_produces
out     7 test_report_guard_states.py::test_the_guard_survives_the_state[...]
out    8 failed, 1053 passed in 338.37s
judge  at `d16a46b` those eight ARE the boundary, and the report traces them by name and
       separates the one that is its own (section 6(f)). **They do not clear at `d09a237`,
       and that is R725.**
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST, AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 0949047..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  NOT a STOP-class finding. Nothing in this range touches what I read, what I must
       carry, or what I may write.
cmd    git ls-files -- tests/conftest.py tests/**/conftest.py
out    tests/conftest.py
cmd    git diff --stat 0949047..HEAD -- tests/conftest.py tests/**/conftest.py
out    (empty)
cmd    git ls-files -- *conftest.py
out    tests/conftest.py
judge  CI0 check resolves to a real file, it is unchanged, and the tree still holds exactly
       ONE conftest. **CH2 channel is wider than a conftest again this round and I read the
       new path line by line.** The gate loads `scripts/f4_dynamic_residual.py` by
       `importlib` into `sys.modules` at module scope (`test_f4_g41_dynamic.py:64-85`). That
       module defines NO pytest hook, rewrites no report, touches no collection. It does
       `sys.path.insert(0, ROOT)` at `:59`, and I checked what that could shadow -- `ls
       *.py` at the repository root is empty -- so it shadows nothing. Read, and clean.
       **And the gate own `test_the_module_the_gate_IMPORTS_reaches_nothing_but_numpy_and_
       the_stdlib` is the right shape for this**: the AST rather than the runtime, and it
       verifies the `floatfea` allowance over the whole package rather than asserting it.
cmd    git diff --stat 0949047..HEAD -- floatfea tests docs scripts .github data
out    .github/workflows/ci.yml 19 | data/f4/dynamic_inputs.npz (bin 9928349) |
out    data/f4/dynamic_inputs.provenance.json 41 | docs/milestones/F4.md 86 |
out    floatfea/tolerances.py 221 | scripts/export_f4_dynamic_inputs.py 427 |
out    scripts/f4_dynamic_residual.py 460 | tests/.../test_f4_g41_dynamic.py 613
judge  **NOTHING UNDER floatfea/ MOVED EXCEPT tolerances.py**, so there is no (a) in this
       range outside the tolerance block. BR0 is satisfied in both directions: `c8cb5f6` and
       `d16a46b` are standalone `plan:` commits, and the second exists because the
       implementer found its own missing row (section 6(g)).
cmd    git diff 0949047..HEAD -- floatfea/tolerances.py | grep -E ^[-+][A-Z0-9_]+:.Final
out    -F4_G41_DYNAMIC_FORCE = 5.0e-9          +F4_G41_DYNAMIC_FORCE = 2.5e-12
out    -F4_G41_DYNAMIC_FORCE_COUNTER = 0.1     +F4_G41_DYNAMIC_FORCE_COUNTER = 3.0e-8
out    +F4_WINDOW_RULE_MIN_EDGE = 2.0
out    +F4_G41_DECOMPOSITION_AGREEMENT = 1.0e-12
out    +F4_G41_DECOMPOSITION_AGREEMENT_COUNTER = 0.1
judge  two values moved and three were declared, so **EU1 fires and the adversarial case is
       mandatory**. Sections 2 and 3 are it, and four of my five findings came out of it. No
       existing value, counter or comment was widened: the force ceiling tightened by three
       decades and its counter by six, both in the strengthening direction.
```

## 2. EVERY PUBLISHED FIGURE REPRODUCES ON MY OWN RUN, TO THE DIGIT

```
cmd    python scripts/f4_dynamic_residual.py      (mine, at d09a237)
rule   docs/milestones/F4.md:145-148 and the F4_WINDOW_RULE_MIN_EDGE entry -- geometric
       centre, both edges at least 2x, over EV1 WHOLE counter family
out    force  clean worst 2.112671361106528e-16  at platform/T20
out    force  150 live, 0 vacuous; weakest 3.385828903353713e-08 at (mass, hub3, 10.0)
out    force  centre 2.674536e-12; EH4 fall to 4.225343e-16, rise to 1.692914e-08
out    moment clean worst 2.324345895610256e-06  at platform/T15
out    moment 108 live, 42 vacuous; weakest 0.017528231438113724 at (drop, hub3/8, 10.0)
out    moment centre 2.018457e-04; EH4 fall to 4.648692e-06, rise to 8.764116e-03
out    the 42 vacuous keys: hub1/3 and hub3/11 in 6 of 6 cases, plus all 30 mass members
judge  **EVERY NUMBER IN ALL SIX TOLERANCE ENTRIES AND ALL SEVEN PLAN ROWS REPRODUCES** --
       both clean worsts, both weakest members and where they are, both centres, both pairs
       of EH4 bounds, the vacuous count and its exact key set. The edges at the declared
       values are arithmetic on two printed lines and I recomputed all four: force
       `11833.4x` / `13543.3x`, moment `86.0457x` / `87.6412x`. The counter margins
       `1.12861x` and `1.7528x` and the weakenings `0.8860` and `0.5705` reproduce too.
cmd    python -m pytest tests/verification/rung4/test_f4_g41_dynamic.py -q -p no:randomly
out    112 passed in 1.28s
judge  the report `1.22s` against my `1.28s`, and `1539.78s` before. The 25 minutes did not
       move to CI; they moved to an on-demand script, which is the right place for them.
```

## 3. TRY TO BREAK IT -- WHAT I RAN AND WHAT IT SAID

Every cell below restored the tree with `git checkout --`, and `git status --porcelain` was
empty after each.

* **The stale-but-accepted state, constructed and run** -- found R726. `heading_deg=0.0` to
  `90.0` in `scripts/report_joint_reactions.py`, which the export calls through `solve_one`,
  changes every array the npz would hold. `112 passed in 1.33s`, and the staleness test
  alone `1 passed in 0.15s`.
* **The same at two more inputs** -- `floatfea/io/integrator.py`, which produces the
  `alpha_m` the npz stores, and `data/platform/platform12_deck.yaml`: `1 passed` each. **The
  control**, touching the one file the provenance does name: `1 FAILED`. One variable at a
  time, and the needle is alive.
* **The decomposition ceiling raised until something trips** (EH4 weakening direction) --
  found R727. `1e-8`, `1e-4`, `1e-2`, `0.1`, `0.1413` all give `112 passed`; `0.1414` goes
  red. Eleven decades, and at `0.1413` the ceiling is ABOVE its own declared counter.
* **The window-rule constant raised in the direction that STRENGTHENS it** -- found R728.
  `1.0`, `2.0`, `3.0`, `10.0`, `86.0` all green; `87.0` red. At `86.0` the vacuity assertion
  is back at `1.999e-04`, which is R723 reinstated.
* **The injection size solved in both directions** -- found R729. With all 112 green,
  `mass_eps` may range over `[8.8605e-07, 2.8385e-05]`, and the window centre moves `5.66x`
  across that band.
* **The clean worst re-formed inside the npz, one variable moved** -- `resid_control` gives
  `1.8176611902597044e-16` at hub2/**T16.2** against `2.112671361106528e-16` at
  platform/T20: ratio `1.1623`, a different body AND a different case. The shipped
  `2.5e-12` has lower edge `11833.4x` under one form and `13753.9x` under the other, so
  **the declaration survives this and I am not blocking on it.**
* **The decision rule inverted on the force channel** -- the smallest COMMON relative scale
  error on every `contrib` that breaches `2.5e-12` at `T_full = 20 s` is `3.6459e-12`
  (platform), `5.0583e-12` (hub1), `5.2859e-12` (hub2), `7.4410e-12` (hub3), `5.2859e-12`
  (hub4). **This is the answer to question 2 and it is a measurement, not an opinion.**
* **The refusal ablated** -- replacing the sha-mismatch branch with a constant false gives
  `1 failed` on `test_the_inputs_REFUSE_rather_than_skip`, `111 passed`. The four refusal
  paths are genuinely unconditional and the test is two-sided.
* **The whole suite at the reviewed commit** -- `3267 passed, 8 failed, 0 skipped`,
  `713.35s`, and the eight are R725.

## Findings

**R725. (BLOCKING -- (d): A RED TEST AT THE REVIEWED COMMIT) REVISION 2 ANSWERS LINE NAMES
THE COMMIT VERDICT 106 *REVIEWED* INSTEAD OF THE COMMIT IT WAS *WRITTEN AT*, SO THE GUARD
THAT MAKES THE ANSWERS HEADER MEAN ANYTHING IS RED, AND THE GENERATED CI SECTION IS
ANCHORED ON THE WRONG COMMIT.**
`docs/reports/F4/step-3.md:710` (`Answers: verdict 106 @ f07bcb8`),
`tests/test_report_carried.py:415-430`.

```
cmd    python -m pytest -q -p no:randomly          (whole suite, mine, at d09a237)
out    8 failed, 3267 passed, 2 warnings in 713.35s
out    FAILED tests/test_report_carried.py::test_the_answered_verdict_is_the_NEWEST_one
out    FAILED tests/test_report_guard_states.py::test_the_guard_survives_the_state[baseline]
out    + 6 more test_the_guard_survives_the_state states, cascading off that baseline
out    AssertionError: the report at `d09a237` is newer than the verdict at `0949047` and
out      names `f07bcb8`. Written with the newest verdict available, it must answer that one.
cmd    git log -1 --format=%H -- docs/reviews/F4/step-3.md
out    0949047104b776538ebe98ac025a95e9c0f11696
cmd    grep -n ^Answers: docs/reports/F4/step-3.md
out    5:Answers: verdict 104 @ 74c77d1        (revision 1 -- the verdict COMMIT, correct)
out    710:Answers: verdict 106 @ f07bcb8      (revision 2 -- the commit 106 REVIEWED)
judge  **THIS IS NOT EG3 STATE (2) AND IT MUST NOT BE FILED AS ONE.** The guard has an
       explicit ancestry carve-out for the step boundary at `:415-421` and it RETURNS EARLY
       there; it fires only when the report is the LATER of the two, which is the case here
       (`d09a237` descends from `0949047`). EH1 lists this id under state (2), and EH1 also
       says the cascade is identified by the baseline being red and by each failure line,
       **not by its name** -- so I traced it rather than ruling it by family, which is
       EG3(i) whole purpose. The cause is one token in one line.
```

**And the consequence is not cosmetic, which is why it is (d) rather than a closure item.**
`scripts/ci_section.py` anchors on that line, so revision 2 section 0 reads **CI at
`45e5242`, the commit verdict 106 judged -- conclusion SUCCESS**. Verdict 106 judged
`f07bcb8`, whose run `37733553932` was **FAILURE** with 124 errored cases. The report
section whose entire job is to carry the CI state of the judged commit carries a different
commit green, inside the revision that answers a STOP caused by that very red. That is
R717 and R718 class and it is why those two findings exist.

**Closed when** `:710` reads `Answers: verdict 106 @ 0949047`, sections 0 and 0a are
regenerated from it, and `python -m pytest tests/test_report_carried.py
tests/test_report_guard_states.py -q -p no:randomly` is run at the revision own commit and
pasted. **EG3(ii) measured, for the first time from this side:** state (2) did NOT clear at
the answering report, and the reason is in the report rather than in the boundary.

**R726. (BLOCKING -- (c): a gate assertion, on which quantity) THE STALENESS CHECK READS
TWO FILES AND THE NPZ IS A FUNCTION OF AT LEAST FIVE, SO A STALE-BUT-ACCEPTED STATE IS ONE
EDIT AWAY -- AND THE VARIABLE I MOVED IS THE ONE EX3 ITSELF DECLARES UNTESTED.**
`tests/verification/rung4/test_f4_g41_dynamic.py:224-267`,
`data/f4/dynamic_inputs.provenance.json:13-20`,
`scripts/export_f4_dynamic_inputs.py:148-159` and `:398-419`.

```
claim  the gate accepts an npz that no longer describes the tree it is run against
cmd    sed heading_deg=0.0 -> 90.0 in scripts/report_joint_reactions.py ; run the gate
out    112 passed in 1.33s
cmd    the staleness test alone, same edit in place
out    1 passed in 0.15s
cmd    the same, one file at a time, staleness test alone:
out    floatfea/io/integrator.py           1 passed in 0.17s
out    data/platform/platform12_deck.yaml  1 passed in 0.16s
out    scripts/export_f4_dynamic_inputs.py 1 FAILED      <- the control; the needle fires
rule   EX0(b) and the file own docstring: absence or STALENESS is a REFUSAL, never a skip
cell   ONE FILE TOUCHED AT A TIME, nothing else moved, tree restored each time
judge  **THE EXPORT IMPORTS `report_joint_reactions` FOR `solve_one`** (`:149-150`), which
       loads the deck, applies the override and sets the wave heading; it imports
       `generalized_alpha_coefficients` from `floatfea/io/integrator.py` (`:152`) and stores
       its `alpha_m`; and it reads `data/platform/platform12_deck.yaml` through the solve.
       The provenance records blob shas for exactly TWO files -- itself and
       `scripts/measure/g41_dynamic.py` -- so three of the inputs are outside the collection
       the assertion inspects. That is `CLAUDE.md` assertion domain blindness, and the
       heading is the single coordinate EX3 writes down as untested.
```

**I am blocking on this rather than filing it as apparatus because of what the gate now
is.** EX0 moved the whole of G4.1-dynamic onto a committed file, which was the right repair
and which created a defect class that did not exist before `d09a237`: a wrong answer no
longer needs wrong code, it needs a correct computation on a stale window. The sha256 and
the four refusal paths are both sound -- I ablated the sha branch and the test went red --
but the sha256 answers *does the npz match its provenance*, which is a different
proposition from *does the npz describe this tree*, and only the blob-sha list addresses the
second. A list is a domain.

**Closed when** the provenance records a digest for every file the npz content is a function
of -- at minimum `scripts/report_joint_reactions.py`, `floatfea/io/integrator.py` and
`data/platform/platform12_deck.yaml` -- and
`test_the_npz_is_NOT_STALE_against_the_code_that_generated_it` iterates that list instead of
two fixed keys, with the controlled pair above re-measured and pasted. **No new apparatus**:
it is one more loop over an existing field read by an existing test.

**R727. (BLOCKING -- (b): a tolerance value and the form of one; and (c): the assertion that
would bound it) `F4_G41_DECOMPOSITION_AGREEMENT` MAY RISE ELEVEN DECADES WITH ALL 112 CASES
GREEN, AND AT `0.1413` IT SITS ABOVE ITS OWN DECLARED COUNTER WITH NOTHING RED, BECAUSE THE
ONE TEST THAT CHECKS CEILING-BELOW-COUNTER NAMES ONLY THE OTHER TWO PAIRS.**
`floatfea/tolerances.py` (the `F4_G41_DECOMPOSITION_AGREEMENT` entry, the paragraph beginning
`Reason for 1.0e-12`), `tests/verification/rung4/test_f4_g41_dynamic.py:527-536` and
`:312-332`.

```
claim  the declared ceiling has no bound above it short of its counter family
cmd    the gate run with the constant patched, nothing else changed
rule   EH4: the ceiling rises until a clean case trips. Both directions, and this is the
       weakening one
out    1.0e-12   112 passed    (the shipped value)
out    1e-8      112 passed
out    1e-4      112 passed
out    1e-2      112 passed
out    0.1       112 passed    <- the ceiling now EQUALS its own declared counter
out    0.1413    112 passed    <- the ceiling now EXCEEDS its own declared counter
out    0.1414    1 failed      test_DROPPING_one_pair_from_the_sum_breaks_that_agreement
judge  **1.413e+11x of admissible widening, and the first thing that reddens is the family
       minimum `0.14137099995337896` -- not the ceiling relationship to the gap it gates.**
       `test_the_declared_ceilings_sit_inside_their_counters` at `:535-536` asserts exactly
       two inequalities, FORCE and MOMENT, and the docstring says it is there so that `a
       ceiling edited past its counter is caught without reading the npz at all`. The pair
       the same commit added is not in it. `test_the_window_rule_HOLDS_at_the_declared_
       ceiling` is parametrised over `_R.CHANNELS`, which is force and moment, so no window
       rule holds this one either.
```

**On the departure the hand-back asked me to rule on, separately, because the two answers
are different.** Declaring this ceiling at `1.0e-12` rather than at the window rule
geometric centre of about `5.5e-9` is **RIGHT and I endorse it**: the measured gap is
`2.111298e-16`, the rule centre would admit seven decades of genuine disagreement in a
quantity that is pure summation-order round-off, and tightening relative to the rule is the
safe direction. The entry says so in its own words and I agree with the words. **What is
wrong is the consequence nobody stated**: departing from the rule removes the only
assertion that bounds the value from above, and the entry publishes `eleven decades below
the weakest defect` as a virtue while that is exactly the EH4 weakening headroom.

**Closed when** both of these hold: (i) the decomposition pair is added to
`test_the_declared_ceilings_sit_inside_their_counters`; and (ii) the ceiling is pinned from
above on the quantity it actually gates -- the R694 shape, a stated multiple of the measured
gap with the multiple declared and its own rise bound measured and pasted, with `1.0e-12`
demoted to a floor beneath it. I am not asking for the window rule centre, and the entry
reason paragraph should keep saying why not.

**R728. (BLOCKING -- (b): the FORM of a tolerance) `F4_WINDOW_RULE_MIN_EDGE = 2.0` IS A
FLOOR ON A RATIO IN THREE OF ITS USES AND A CEILING ON A SIGNAL IN THE FOURTH, SO RAISING IT
IN THE STRENGTHENING DIRECTION OF THE RULE REINSTATES R723 -- MEASURED, AND GREEN.**
`floatfea/tolerances.py` (the `F4_WINDOW_RULE_MIN_EDGE` entry, the sentence `One constant,
because they are one rule`), `docs/milestones/F4.md:600` (the same sentence),
`tests/verification/rung4/test_f4_g41_dynamic.py:519`,
`scripts/f4_dynamic_residual.py:145-149` and `:401-402` and `:434-435`.

```
claim  one change to this constant tightens three assertions and loosens a fourth
cmd    the gate run with the constant patched, nothing else changed
rule   tolerance form -- a single number whose increase tightens one assertion and weakens
       another is two thresholds sharing a value
out    1.0    112 passed
out    2.0    112 passed    (the shipped value)
out    3.0    112 passed
out    10.0   112 passed
out    86.0   112 passed    <- the vacuity assertion is now `signal < 1.999e-04`
out    87.0   1 failed      test_the_window_rule_HOLDS_at_the_declared_ceiling[moment]
judge  **AT `86.0` THE VACUITY ASSERTION IS BACK WHERE R723 FOUND IT.** `86.0 x
       2.324345895610256e-06 = 1.999e-04`, which is the ceiling `2.0e-4` to four digits --
       R723 `43.0229x` of slack, reinstated by a change in the direction that makes the
       window rule STRICTER, with 112 of 112 green. Three uses read it as `>=` on a ratio
       (`:147-148`, `:459`, `:463`) and `eh4_fall_to`/`eh4_rise_to` derive from the same
       sense; the fourth reads it as `<` on a signal (`:519`).
cmd    grep -n v <= worst  scripts/f4_dynamic_residual.py
out    401:    live = {k: v for k, v in fam.items() if v > worst}
out    402:    vacuous = {k: v for k, v in fam.items() if v <= worst}
judge  **AND THE TREE ALREADY HOLDS TWO VACUITY THRESHOLDS DIFFERING BY EXACTLY THIS
       CONSTANT.** `family`, `window_rule`, `test_every_LIVE_counter_member_reddens_the_gate`
       and `test_the_VACUOUS_moment_members_...` all define vacuous as `v <= clean_worst`, at
       1x. `test_the_mass_scale_is_VACUOUS_on_the_moment_channel` uses `2 x clean_worst`. So
       `because they are one rule` is false as written: the rule own filter has no factor of
       2 in it. The band `(1x, 2x)` is covered -- a member landing there reddens the
       `len(vacuous) == 42` count and three other assertions, which I checked -- so the
       ENSEMBLE is sound and the FORM is not.
```

**My predecessor asked for `2.0 * _clean_worst` and the implementer delivered exactly that,
so this is my own condition being corrected rather than the work being wrong.** The sharp
flip point for the sentence `the mass injection is vacuous on this channel` is `1x`, which
is the definition the module itself uses four lines away. `2x` is better than `43x` and it
is still 2x of slack on a claim the file defines at 1x.

**Closed when** the vacuity threshold at `:519` is the family own definition
(`> clean_worst`, matching `:401-402`) or a separately named constant, so that no single
number is a floor in one assertion and a ceiling in another; and the `because they are one
rule` sentence in `floatfea/tolerances.py` and `docs/milestones/F4.md:600` is made true or
reduced to the bare measurement (BG0: it is a causal claim and the measurement above refutes
it). One expression and one sentence.

**R729. (BLOCKING -- (c): a gate assertion that the plan requires and nothing makes; and (b):
the size the counter is injected at) EV1 LOCKS THE SECOND INJECTION AT `1 + 1e-6`, THE GATE
READS IT OUT OF THE NPZ, AND NOTHING ASSERTS IT -- WHILE BOTH NEW FORCE VALUES ARE FUNCTIONS
OF IT.**
`tests/verification/rung4/test_f4_g41_dynamic.py:270-283` (where `fe_bodies` and
`periods_full_s` ARE pinned and `mass_eps` is not), `scripts/f4_dynamic_residual.py:206` and
`:323`, `data/f4/dynamic_inputs.provenance.json:33` (`mass_eps: 1e-06`, recorded and compared
with nothing).

```
cmd    grep -rn mass_eps tests/ floatfea/
out    tests/verification/rung4/test_f4_g41_dynamic.py:520 -- inside an f-string, in a
out      failure message. That is its ONLY appearance under tests/.
rule   EV1 specifies the injection as `M` scaled by `1 + 1e-6`; R694 -- a counter that
       depends on a model parameter is a function and not a number
out    the mass response is EXACTLY linear in eps, by the closed form at `:328`
out    and it IS the binding member of the force family: weakest live 3.385828903353713e-08
cmd    solve the band in which all 112 cases stay green, both directions
out    eps may RISE   x28.3849  to 2.8385e-05  before the moment vacuity assertion trips
out    eps may FALL   x0.886046 to 8.8605e-07  before weakest > counter 3.0e-8 trips
out    admissible band [8.8605e-07, 2.8385e-05]; the window centre over it moves 5.66x
judge  **`F4_G41_DYNAMIC_FORCE = 2.5e-12` AND `F4_G41_DYNAMIC_FORCE_COUNTER = 3.0e-8` ARE
       BOTH DECLARED FROM A NUMBER THAT SCALES WITH AN INPUT NO ASSERTION PINS.** The two
       values are correct AT `eps = 1e-6`, which is the configuration the commit chose, and
       the whole of R722 repair rests on the mass family binding -- which is an eps-dependent
       fact. The same shape sits at four more coordinates: `dt`, `rho_inf`, `lambda` and the
       ramp are all in the provenance `run` block and compared with nothing. `fe_bodies` and
       `periods_full_s` ARE asserted at `:276-277`, which is the right shape and is why these
       read as omissions rather than as a design.
```

**Closed when** `test_the_domain_is_thirty_body_cases`, or a sibling in the same file,
asserts `inputs.mass_eps == 1e-6` -- the value EV1 locks -- beside the two domain assertions
it already makes, with a failure message that says the declared force ceiling and counter are
functions of it. One line. The four run parameters are the same class and I would take them
in the same line, but I am requiring only `mass_eps`, because it is the one the declaration
depends on.

## On the questions I was asked

**1. R721 -- CLOSED, and the npz CAN be stale: R726.** The ladder is green in CI at three
commits, rung 4 and rung 5 both, on runners with no worktree. Of the three defences the
hand-back named: the four refusal paths are sound and two-sided (I ablated one and it went
red); the sha256 is sound for what it tests and tests the wrong proposition; **the blob-sha
list is the one that was supposed to catch staleness and it covers two of five inputs.** The
stale state I built is one `sed` and the variable is the heading, which EX3 names as the open
question in the same commit.

**2. The force channel lower edge -- IT IS MEANINGFUL, AND I MEASURED IT RATHER THAN RULING
ON IT.** The implementer position is that the upper edge carries the information and the
lower does not. That is half right and the missing half matters: `11833.4x` is indeed a
distance from round-off and not a physical margin, **but it is also the gate sensitivity to
any defect that enters the reactions proportionally**, and solved rather than sampled the
smallest common relative scale error on `contrib` that `2.5e-12` detects is `3.6459e-12` on
the platform, `5.0583e-12`, `5.2859e-12`, `7.4410e-12` and `5.2859e-12` on the four hubs.
A ceiling seven decades higher would detect nothing of that class. **So the window rule IS
the right instrument here and no different form is needed.** What should be published is
that detection threshold rather than the ratio to noise -- closure class, C28 below. And the
cell the report uses to make the round-off point compares two SCRIPTS, which moves more than
one variable; within the npz, one variable moved, it is `1.1623x` and hub2/**T16.2**, which
strengthens the point.

**3. The decomposition departure -- THE TIGHTENING IS RIGHT, THE MISSING UPPER PIN IS R727.**
Ruled above, separately from the value, because the two answers differ.

**4. One constant for four roles -- NO, AND IT IS MEASURED: R728.** Two of the four are
opposite senses, and `86.0` reinstates R723 with the suite green.

**5. The three departures from EX letter -- EACH ACCEPTED, and the implementer is right that
it should not be its own judge, so here is the ruling.** (a) Storing `base` and `m_xddot`
beside EX0(a) four arrays is **necessary, not a substitution**: I checked that `_residual` is
`base - sum contrib` (`:243-249`) and that is the discrete form the plan locks, and R711
measured what the continuous one costs. (b) The determinism leg genuinely cannot run
FloatSim on `ubuntu-latest`; the substitute is weaker than EX0(c) asked for and **R726 is
exactly the gap it leaves**, so I accept the departure and block on its incompleteness
rather than on the departure. (c) `two scripts` becoming one is **correct and is the repair**:
the export must not be on a gate path, and that asymmetry is R721 whole lesson. None of the
three is a plan conflict and none needs Xabier.

**6. Are the seven complete? NO -- there are five more and they are above.** On (a)
specifically: **I agree with the call.** A duplicate-`Final` check is a meta-test, CZ0 forbids
one through F6, and asking Xabier for the exception rather than building it is the correct
reading of the rule. I would add one thing to the request, because it strengthens it: the
failure was invisible to `ruff`, `black` and `mypy` *and* to a green suite *and* to a green
CI, which is the same four-way blindness EQ0 was written about -- so the exception is being
asked for on the one class of defect this project has already decided green cannot see.
Until then, printing the value back is the method and the report is right to say so.

**7. The guard that failed false -- YOU SHOULD HAVE FIXED THE GUARD, AND IT IS A CLOSURE
ITEM, NOT A HOLD.** CZ0 says a guard that fails false is fixed or deleted, never extended,
and citing the digest truncated is neither -- it is an accommodation, and it leaves the guard
able to fire false on the next digest anybody pastes. The fix is a fix and not an extension:
the needle is a 10-digit run inside a 64-character hex string, so requiring the run id to be
a standalone token rather than a substring is narrowing the guard to what it always meant.
Closure class because guards are closure class under CZ0, and I am not spending a round on
it. C29 below.

## Tolerances touched

```
cmd    git diff 0949047..HEAD -- floatfea/tolerances.py | grep -E ^-[A-Z] | grep -vE ^---
out    -F4_G41_DYNAMIC_FORCE: Final[float] = 5.0e-9
out    -F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 0.1
judge  **TWO VALUES REMOVED, BOTH REPLACED BY TIGHTER ONES, AND NOTHING WAS WIDENED.** The
       moment pair is unmoved except for its clean-worst figure, which moved in the 17th
       digit because the quantity is now recomputed from the npz.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_G41_DYNAMIC_FORCE` | `5.0e-9` | `2.5e-12` | dimensionless, relative; denominator a sum of magnitudes | `_COUNTER` `3.0e-8`, injected by the joint drop at `:312-332` and by the mass scaling at `:506-524`, both families entering `window_rule` | entry in `floatfea/tolerances.py`; plan `docs/milestones/F4.md:595`; module `:397-436` | **ADMISSIBLE, and R722 is genuinely closed.** Every figure reproduces, both edges hold at the declared value, and both EH4 bounds fire exactly where published -- I solved both: `1.69e-8` green and `1.7e-8` red, `4.3e-16` green and `4.2e-16` red. **Blocked only through R729**: the value is a function of `mass_eps` and nothing pins it. |
| `F4_G41_DYNAMIC_FORCE_COUNTER` | `0.1` | `3.0e-8` | dimensionless | is itself the counter | same entry; plan `:596` | **CORRECT, and the thin margin is by design.** `1.12861x` below the weakest live member over BOTH injections, which is the right reduction over the right family. R729 bites here hardest: at `eps = 0.886e-6` this assertion is the first thing to redden. |
| `F4_G41_DYNAMIC_MOMENT` | `2.0e-4` | unmoved | dimensionless, relative; about each body `reference_point`, stated | `_COUNTER` `0.01` over 108 live members; the mass family asserted vacuous at `:506-524` | same entry; plan `:597` | **CLEAN as a value.** The window over both families equals the window over the drop family because the whole mass family is vacuous here, and the entry now states that with all 42 keys. R724 cause is properly WITHDRAWN and replaced with the bare measurement plus the limitation. |
| `F4_G41_DYNAMIC_MOMENT_COUNTER` | `0.01` | unmoved | dimensionless | is itself the counter | same entry; plan `:598` | **CLEAN as a value, and R723 is answered.** The vacuity assertion moved off the ceiling. **Blocked by R728 as a FORM**: the threshold it moved to is a shared constant whose other three uses pull the opposite way, and the module defines vacuity at 1x four lines away. |
| `F4_WINDOW_RULE_MIN_EDGE` | -- | `2.0` | dimensionless, STRUCTURAL | none, correctly -- AO2 | entry; plan `:599-600` | **BLOCKED, R728.** Declaring EV1 2x as a constant rather than a literal is right, and CI catching the literal is the right order of events. One constant for four readings is not right, and `86.0` is the measurement. |
| `F4_G41_DECOMPOSITION_AGREEMENT` | -- | `1.0e-12` | dimensionless, relative; per body-case own denominator, worst over the window | `_COUNTER` `0.1`, injected by dropping one pair at `:312-332` | entry; plan `:601` | **BLOCKED, R727.** The value and the departure from the window rule are both right. It has no bound above it short of `0.1413`, and it crosses its own counter on the way there. |
| `F4_G41_DECOMPOSITION_AGREEMENT_COUNTER` | -- | `0.1` | dimensionless | is itself the counter | entry; plan `:602` | **CLEAN as a value**: a minimum over all 120 members at each member worse channel, `1.4137x` margin, reproduced. It is the only thing bounding its ceiling, which is R727 and not a defect in this row. |
| the FE inertia-relief acceleration (EV1 third bullet) | blocking in verdict 106 | **DEFERRED TO F5 BY EX4** | -- | -- | plan `:140-141` struck through; `:682-689` records the deferral | **WITHDRAWN AS A BLOCKING ITEM, and EX4 settled it correctly.** I ruled it (c) because the plan required the assertion; the plan no longer does, the deferral is recorded with its reason and with `no tolerance is declared for it in F4`, and EA4 forbids declaring one before the measurement exists. It does **not** carry into step 4. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 106 (`0949047`) was an **ES0 INTERIM CHECK and counted against no round**. It raised
four blocking items; verdict 105 raised two and a closure list. Every one, with status.

* **R721 (blocking, and the STOP) -- CLOSED, at a better shape than my condition named.** My
  condition was that the plan row say what the rung-4 gate READS and that the gate read it.
  Answered at `c8cb5f6` (plan section 4a and the rewritten G4.1-dynamic row) and `8ae9acc`
  (the npz, the provenance, the two scripts, the new gate). **The measurement that closes it
  is mine and not the report**: ladder 4 AND ladder 5 both SUCCESS in CI at `8ae9acc`,
  `380184e` and `d16a46b`, on runners with no `HSP-runs`. Three things I named and did not
  get, each better than what I asked for: the live six-solve did not go to the determinism
  leg, because that runner has no FloatSim either, and the report says so rather than
  substituting (section 7(b)); `base` and `m_xddot` were added to EX0(a) array list because
  the four it names cannot reproduce the discrete form; and the refusal is exercised on four
  unconditional paths rather than one. **Does not carry. Its residue is R726** -- the half of
  EX0(c) that CI can run, done over too small a domain.
* **R722 (blocking) -- CLOSED.** The force ceiling, its counter and both EH4 bounds are
  re-declared over both of EV1 injections; `window_rule` takes the minimum over `family`,
  which is both families keyed by kind (`:379-394`); the published upper edge and rise bound
  are the measured ones and I reproduced all four. **Does not carry, except that R729 is the
  parameter the new numbers depend on.**
* **R723 (blocking) -- CLOSED as to the quantity and the direction; the threshold it moved to
  is R728.** `:519` asserts against `F4_WINDOW_RULE_MIN_EDGE * worst` rather than the
  ceiling, which is literally what my condition asked for, and the failure message keeps the
  `raise the finding` wording I asked to survive. **My own condition said 2x and the file own
  definition is 1x; I am correcting my condition, not the work.** Carries as R728.
* **R724 (blocking) -- CLOSED at all three sites.** The false sentence is withdrawn in
  `floatfea/tolerances.py`, in `test_f4_g41_dynamic.py:470-483` and in
  `docs/milestones/F4.md:559-565`, with the deck four identical `attach_a_body` rows pasted,
  and the replacement is the bare measurement plus the limitation -- the x-axis observation
  and `all six cases are heading 0 degrees, so the heading dependence is UNTESTED`. That is
  the second branch of my condition and it is the honest one. **Does not carry.** Note that
  the untested heading is now also R726 worst case, which is not a coincidence: the gate
  cites the deck as evidence while not pinning it.
* **R719, R720 (blocking, verdict 105) -- remain closed.** Not re-raised, and the recomputed
  module carries the same corrections (`:295-334`): the drop signal is `contrib_p` and the
  mass signal is the closed form, so neither can pick the clean floor back up. I re-derived
  the linearity from `:328` and it is exact.
* **R712 (closure) -- the half that mattered is CLOSED.** `PLATFORM_MASS_OVERRIDE` is off the
  gate path: the export passes it explicitly at `export_f4_dynamic_inputs.py:154` and the
  gate imports a module that never mentions it. **The other half is now R726 and R729
  material**: the basis is RECORDED in the provenance and compared with nothing.
* **R713, R714, R716, R717 (closure) -- STILL OPEN**, correctly. R717 is the one whose cost
  showed up this round: `ci_section.py` anchor is what turned R725 wrong token into a
  published CI-SUCCESS heading for a commit that failed.
* **C2 to C15, C24 to C27 (closure) -- STILL OPEN**, carried in report section 9 and not
  re-reviewed item by item, per CZ0.
* **The verdict 103 and verdict 106 escalations -- ANSWERED BY EX4, and I record that rather
  than restating them.** EX4 moved the working target to 16 October and deferred the
  acceleration assertion to F5, which IS the `reduce scope` branch of the choice I put. The
  report states the date and says it holds. See the section below.

## Closure items

Named with their site and what would close each. The implementer fixes the whole list once,
in the step closure commit; they are not re-reviewed item by item and the step is not held
on one.

* **C28.** `floatfea/tolerances.py`, the `F4_G41_DYNAMIC_FORCE` entry paragraph beginning
  `AND THE LOWER EDGE IS NOT A PHYSICAL MARGIN`. The sentence is true and incomplete: the
  lower edge IS the gate detection threshold for a proportional defect in the reactions.
  **Closed when** the entry carries the solved threshold -- `3.6459e-12` on the platform at
  `T_full = 20 s`, the four hub figures beside it -- instead of, or beside, the ratio to
  noise, with the step report carrying the loop.
* **C29.** The `test_no_RUN_ID_appears_outside_THE_GENERATED_CI_SECTIONS` false positive on a
  sha256 substring, worked around in report section 6a by truncating the digest. **Closed
  when** the guard needle requires the run id to be a standalone token rather than a
  substring -- which is narrowing it to what it always meant, so a fix and not an extension
  -- or the guard is deleted. CZ0: fixed or deleted, never accommodated.
* **C30.** `scripts/f4_dynamic_residual.py:74-83`. `body_mass`, `body_J_G` and `accel` are
  loaded into `Inputs` and read by nothing. They satisfy EX0(a) as a list and are absent as
  evidence. **Closed when** either something asserts against them -- `body_mass[0]` against
  the provenance declared override is the cheap one and would close part of R726 -- or the
  docstring says they are stored for F5 and are not yet read.
* **C31.** `tests/verification/rung4/test_f4_g41_dynamic.py:33-34`. The module docstring
  publishes the weakest live mass response as `3.385828902450096e-08` where
  `floatfea/tolerances.py` and the module print `3.385828903353713e-08`. Mine reproduces the
  second. **Closed when** the docstring figure is the one the shipped path prints.
* **C32.** Report section 4 cell. `re-forming the reaction the second way` compares
  `scripts/f4_dynamic_residual.py` against `scripts/measure/g41_dynamic.py`, which are two
  different code paths with their own windows and denominators, so the cell moves more than
  one variable (BG0). **Closed when** the cell is taken inside the npz -- `_residual` against
  `resid_control`, which the file already stores -- where I measure `1.1623x` and
  hub2/**T16.2** against platform/T20. The conclusion strengthens; the cell as published does
  not isolate it.
* **C33.** `.github/workflows/ci.yml:374-395`. `mypy` now covers `floatfea` plus one named
  script. The comment explains the asymmetry well. **Closed when** the ledger says what
  happens the next time a gate imports a second script -- the rule, not the instance -- since
  the list will otherwise go stale the way R726 list did.

## The adversarial corpus (BE3)

**BATCH 39, committed separately at `d39e34a`:
`tests/corpus/g41_dynamic_committed_inputs_provenance.txt`, 14 entries, every one new this
round and none of them read by the implementer.** EG4(e) permits it: this is F4 load-mapping
gate, the surface where a miss reaches a member force, and verdict 106 recorded the batch as
owed at revision 2.

**COVERAGE: the shipped checks catch 4 of the 14.** That is the number, and it is better than
the last three rounds (4 of 11, 8 of 13, 5 of 10 were measured on other surfaces) only in
that **two of the ten misses are blocking findings in this verdict** -- R727 and R728 came
out of corpus entries, not out of reading the diff. The ten misses are one shape: a list is a
domain. The four catches are the controls, and two of them are measurements the implementer
asked for and did not have (the in-npz re-forming cell, and the inverted decision rule on the
force channel).

The hygiene item on `tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48,
49 and 50 is unchanged and still mine.

## On the criterion -- I was asked, and I agree

CZ0 is right and I applied it. All five of my findings are (b), (c) or (d): one red test, two
gate assertions, two tolerance forms. **Nothing in this verdict is held against a figure or a
sentence** -- six prose items I found went into the closure list above, including two
(`1.139x`, `3.385828902450096e-08`) that under the retired head would each have been a
finding and would each have moved nothing.

**One note, which is the same one I made in verdicts 104, 105 and 106 and which I now
withdraw.** I have been blocking on items in `scripts/` under the carve-out my instructions
give for a generator whose output IS a gate assertion. That carve-out is no longer needed and
I am not invoking it: as of `8ae9acc` the gate IMPORTS `scripts/f4_dynamic_residual.py`, the
plan row says so, `ci.yml` type-checks it, and `test_the_module_the_gate_IMPORTS_...` asserts
its import surface. It is gate code on the plain reading of CZ0 (c), and R726 and R727 are
filed as that rather than under a carve-out. The export, by the same reading, is NOT gate
code and I have treated it as closure class throughout.

**And the schedule, which I am recording rather than escalating.** EX4 took the `reduce
scope` branch of the choice verdict 106 put to Xabier: the acceleration assertion goes to F5,
the working target is 16 October, the committed date is unmoved at 19 October. The report
states it and says it holds. Step 3 is now carrying five blocking items into its last
revision, each one or two lines; EV2 items 2 to 5 are unstarted. **If revision 3 closes still
carrying any of R725 to R729, that is a third consecutive step closing with blocking items
and the choice has to be made again rather than restated.**

## Next step opens when

**Step 3 stays open. This was ROUND 2 OF THREE and ONE REVIEWED REVISION REMAINS.** In
order, cheapest first:

1. **R725 is answered** -- `docs/reports/F4/step-3.md:710` reads
   `Answers: verdict 106 @ 0949047`, sections 0 and 0a are regenerated from it, and
   `python -m pytest tests/test_report_carried.py tests/test_report_guard_states.py -q
   -p no:randomly` is run at the revision own commit and pasted. **This one is not optional
   and it is not a boundary state**: it is the only red at the reviewed commit and it is why
   this is not a PASS.
2. **R729 is answered** -- one assertion on `inputs.mass_eps == 1e-6` beside the two domain
   assertions at `:276-277`, because both new force values are functions of it.
3. **R728 is answered** -- the vacuity threshold at `:519` is the family own definition or a
   separately named constant, and `because they are one rule` is made true or reduced to the
   measurement at both of its sites.
4. **R727 is answered** -- the decomposition pair is added to
   `test_the_declared_ceilings_sit_inside_their_counters`, and the ceiling gains a bound
   above it on the quantity it gates, with the rise bound measured and pasted.
5. **R726 is answered** -- the provenance digests every file the npz is a function of, the
   staleness test iterates that list, and the controlled pair is re-measured. The heading
   cell is the one to paste, because it is the state I built.
6. **The closure list C28 to C33 lands in the step closure commit**, once, with CZ1 four
   outputs and CZ1 (iii) pushed-run paste. EQ0 applies to it: if that commit moves a gate or
   a tolerance -- and R727 and R728 repairs do -- it is reviewed, against no round.

**What I will not accept at revision 3.** A ceiling that can be widened eleven decades with
every assertion green, a single constant that is a floor in one assertion and a ceiling in
another, a declared counter whose anchor is an input no assertion pins, or a staleness check
over two of five inputs. None of those is a judgement about figures. All four are the same
question -- if the thing this assertion claims were false, would it go red -- and for all
four the measured answer today is no.

**And one thing on the record for the implementer rather than against them.** Verdict 106 was
a STOP and the answer arrived in four commits, with the plan reopened properly in a
standalone `plan:` commit, the gate rebuilt on committed inputs, 1539.78 s to 1.28 s, rung 4
AND rung 5 green in CI on a runner with no HSP worktree for the first time since this gate
existed, and every one of the forty-odd figures in six tolerance entries and seven plan rows
reproducing exactly on my own independent run. Seven findings were self-reported before I
looked, including the one no guard caught, and the pattern drawn from them -- that the work
done *around* a repair inherits none of the discipline applied *to* it -- is both true and
the reason I looked where I did. Four of my five findings came from running the gate at a
value the commit did not choose and the fifth from running the suite. Not one came from
reading the prose.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — F4 step 3
Reviewed commit: f07bcb853838c737a9002f5bc17d2f357b7724ac
Verdict: STOP
**Reviewed commit: `f07bcb8`** (`f07bcb853838c737a9002f5bc17d2f357b7724ac`, HEAD of F3,
tree clean when I judged it; **I committed no corpus this round** -- ES0's light scope
forbids a batch -- so the plain `Reviewed commit:` stamp above and the commit I judged are
the same sha. That coincidence is R718's subject and not its refutation.)
Tests: 3253 passed, 0 failed, 0 skipped   (MY OWN run, one invocation, no `-k`, no
`--ignore`, no deselection, `-p no:randomly`, tree clean at `f07bcb8`, `2202.30s`. Not the
report's figure -- there is no new report revision.)

## Round of 2026-10-08 -- ES0 INTERIM CHECK, COUNTS AGAINST NO ROUND. **STOP.**

**ES0's premise, computed rather than taken.**

```
cmd    git diff --stat 0e4188a..HEAD -- docs/reports/
out    (empty)
cmd    git log -1 --format='%h %s' -- docs/reports/F4/step-3.md ; head -4 docs/reports/F4/step-3.md
out    6352d8c report: F4 step 3 revision 1 -- ... ; "Answers: verdict 104 @ 74c77d1"
judge  **NO NEW REPORT REVISION EXISTS**, so ES0's exemption applies and this check counts
       against NONE of step 3's three revisions. Instruction 1b does NOT make this a HOLD
       on its own: 1b compares a REVISION's header against the newest verdict, and the
       revision in the tree is the one I already judged at verdict 105. This is EG3 state
       (2) by construction. **Revision 2 must say `verdict 105`, and if it says 104 that
       is 1b's HOLD.**
cmd    python -m pytest -q -p no:randomly tests/test_report_carried.py tests/test_report_guard_states.py
out    220 passed in 144.65s
judge  **EG3 CONDITION (ii), MEASURED -- AND STATE (2) DID NOT FIRE.** EG3 predicts seven
       named reds when a verdict is newer than its report. At `f07bcb8` the verdict IS
       newer and NONE of the seven fired, on 220 parametrisations. Recorded as the
       measurement EG3(ii) asks for, not as a claim about why.
```

**EU1 FIRES, AND THE ADVERSARIAL CASE IS WHAT THIS VERDICT IS MADE OF.**

```
cmd    git diff 0e4188a..HEAD -- floatfea/tolerances.py | grep -E "^[-+][A-Za-z0-9_]+(:|\s*=)"
out    +F4_G41_DYNAMIC_FORCE: Final[float] = 5.0e-9
out    +F4_G41_DYNAMIC_FORCE_COUNTER: Final[float] = 0.1
out    +F4_G41_DYNAMIC_MOMENT: Final[float] = 2.0e-4
out    +F4_G41_DYNAMIC_MOMENT_COUNTER: Final[float] = 0.01
judge  four VALUES and two declared COUNTERS move, so EU1's adversarial case is MANDATORY
       and not discretionary. I ran the model at all six cases myself and then solved the
       window rule over a counter family the diff did not choose. Three of the four
       findings below came out of that and nothing else.
```

**WHY IT IS A STOP, IN FOUR SENTENCES.** The whole of ladder rung 4 is RED in CI at the
reviewed commit -- `354 collected, 0 failed, 124 errored` -- and ladder 5 did not run
behind it, because the new gate's module fixture requires a FloatSim solve against
`../HSP-runs`, a sibling worktree outside the repository that CI does not check out. My own
suite at the same commit is `3253 passed, 0 failed, 0 skipped`, which is CA2's sentence
turned into a measurement: the gate is green on the one machine that has the worktree and
red on every other. **This exact failure already happened once in this milestone, in this
directory, and was recorded as R670** -- "CI IS RED AT THE REVIEWED COMMIT AND THE RED IS
LADDER 4" is a quotation from `docs/reports/F4/step-1.md` -- and its answer is two files
away: a committed snapshot under `data/`, produced by a committed exporter, with the gate
REFUSING rather than skipping if it is absent. The plan row written this round
(`docs/milestones/F4.md:486`: "The gate imports `scripts/measure/g41_dynamic.py`" and "Six
coupled solves per session") is the row that is wrong, so the plan is what reopens, which is
the STOP head exactly; and because that row is one sentence with a precedent already in the
tree, the reopen is cheap.

**I am not softening it.** My instructions and `CLAUDE.md` both attach "a low rung is red"
to STOP without qualification, and the reason is the one that applies here: step 3's entire
subject IS rung 4, and nothing about revision 2 is interpretable while rung 4 has not run
on CI at all.

## 0. CI -- RED AT THE REVIEWED COMMIT, WITH THE CONTROLLED PAIR

```
cmd    gh run list --commit f07bcb853838c737a9002f5bc17d2f357b7724ac
         --json name,conclusion,workflowName,status,databaseId,event
out    [{"conclusion":"failure","databaseId":37733553932,"event":"push","name":"CI",
out      "status":"completed","workflowName":"CI"}]
judge  **CA2: A RED CI IS A HOLD REGARDLESS OF WHAT THE LOCAL RUN SAYS**, and here it is
       worse than a HOLD because the red is a ladder rung. The run was `in_progress` when I
       was invoked and completed while I worked; an unfinished run is not a pass, so I
       waited. NOT CK2 -- the jobs ran and the step took 4.7 s because the fixture errored,
       not because it was never started.
cmd    gh run view 37733553932 --json jobs   (job and step conclusions)
out    the verification ladder     FAILURE
out        ladder 4 -- the loads are the loads   FAILURE
out        ladder 5 -- independent confirmation  SKIPPED
out    lint, unit and guards       success  (every step, guards and meta-tests included)
out    CI determinism -- leg / ten legs agree   skipped  (CK0 workflow_dispatch)
cmd    gh run view 37733553932 --log-failed | grep "run_rung:"
out    run_rung: 354 collected, 0 failed, 124 errored, 0 skipped
out    run_rung: FAIL -- tests/verification/rung4 is red.
out    124 x run_rung:   error  tests.verification.rung4.test_f4_g41_dynamic::<id>
judge  **124 OF THE GATE 126 CASES ERRORED.** The two that did not are the only two that do
       not take the `measured` fixture --
       `test_the_two_channels_are_gated_SEPARATELY_and_never_combined` and
       `test_the_declared_ceilings_sit_inside_their_counters`. The error is the fixture, on
       every parametrisation.
cmd    for s in 801796e 7799482 becf47c ; do gh run list --commit $s ; done
out    801796e  37729727113  completed  FAILURE   (the rung-3 counter red the hand-back named)
out    7799482  37729406337  completed  cancelled (concurrency cancel-in-progress; CX0/R449,
out             no verdict reached on anything, no reason attributed)
out    becf47c  37727415689  completed  SUCCESS
cell   ONE VARIABLE MOVED. becf47c -> f07bcb8, the gate file added:
out    becf47c  ladder 4 SUCCESS, whole run SUCCESS
out    f07bcb8  ladder 4 FAILURE, 124 errored, ladder 5 skipped
judge  **THE ABLATION IS CLEAN AND IT IS THE GATE FILE.** Rung 4 was green in CI two
       commits ago. BG0 cell, free, and it is the cell the hand-back could have had by
       waiting for one push.
```

## 1. MY OWN INSTRUCTIONS, THE CONFTEST, AND THE TOLERANCE FILE -- EACH DIFFED SEPARATELY

```
cmd    git diff --stat 0e4188a..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)
judge  NOT a STOP-class finding. Nothing in this range touches what I read, what I must
       carry, or what I may write. The STOP below is about the ladder, not about this.
cmd    git ls-files -- tests/conftest.py "tests/**/conftest.py"
out    tests/conftest.py
cmd    git diff --stat 0e4188a..HEAD -- tests/conftest.py "tests/**/conftest.py"
out    (empty)
cmd    git ls-files -- "*conftest.py"
out    tests/conftest.py
judge  CI0 check resolves to a real file; it is unchanged, and the repository still has
       exactly ONE conftest. **But CH2 channel is wider than a conftest this round and I
       read the new path line by line**: the gate loads `scripts/measure/g41_dynamic.py` by
       `importlib` into `sys.modules` at MODULE SCOPE (`test_f4_g41_dynamic.py:59-80`), and
       that module inserts ROOT and later ROOT/scripts onto `sys.path` and mutates
       `report_joint_reactions.PLATFORM_MASS_OVERRIDE` as a module global
       (`g41_dynamic.py:212-216`). No pytest hook is defined anywhere in it, nothing
       rewrites a report, nothing touches collection. Read, and clean. The global mutation
       is contained only because nothing else under `tests/` imports that module.
cmd    git diff --stat 0e4188a..HEAD -- floatfea tests docs scripts .github data
out    docs/milestones/F4.md 6 | floatfea/tolerances.py 126 |
out    scripts/measure/g41_dynamic.py 317 | scripts/report_joint_reactions.py 33 |
out    tests/verification/rung4/test_f4_g41_dynamic.py 355
judge  **NOTHING UNDER floatfea/ MOVED EXCEPT tolerances.py**, so there is no (a) in this
       range outside the tolerance block. BR0 is satisfied: the plan rows and the
       declarations are in one commit.
```

## 2. EVERY PUBLISHED FIGURE IN BOTH ENTRIES REPRODUCES, TO THE DIGIT, ON MY OWN SIX-CASE RUN

I ran the shipped script over all six cases myself and wrote the JSON out, so the boundary
arithmetic below is mine and not the entry's.

```
cmd    python scripts/measure/g41_dynamic.py --out <scratch>/g41_all6.json   (mine, f07bcb8)
rule   docs/milestones/F4.md:145-148 -- geometric centre, both edges >= 2x
out    clean worst force  : 1.8556070086831165e-16  at hub2/T20
out    clean worst moment : 2.3243458955783927e-06  at platform/T15
out    force  120 of 120 able to redden, 0 vacuous; weakest 0.14137099995337896 hub1/0/T12.5
out    moment 108 of 120 able to redden, 12 VACUOUS; weakest 0.017528231438113724 hub3/8/T10
out        vacuous hub1/3   9.544061e-10 .. 6.353783e-09  (6 of 6)
out        vacuous hub3/11  1.128147e-09 .. 7.310970e-09  (6 of 6)
out    centres 5.121807e-09 and 2.018457e-04; edges 27601784.6292x and 86.8398x
out    mass x(1+1e-6): force weakest 3.385829e-08 -- "brackets";
out                    moment weakest 1.360110e-09 -- "DOES NOT BRACKET at 2x"
out    solved 2x scales: force 1 + 1.096102e-14, moment 1 + 3.417879e-03
judge  **EVERY NUMBER IN BOTH TOLERANCE ENTRIES AND ALL FOUR PLAN ROWS REPRODUCES
       EXACTLY** -- the clean worsts, both weakest members, both centres, the vacuous
       ranges and counts, both EH4 bounds as the entries state them, and both solved mass
       scales. R719 and R720 are genuinely closed at the first branch of my conditions.
cmd    python <the four edge figures the script does NOT print, recomputed>
out    force : at centre 27601784.6292x twice ; at declared 5.0e-9  2.69454e+07x / 2.82742e+07x
out    moment: at centre 86.8398x twice      ; at declared 2.0e-4   86.0457x / 87.6412x
out    counter margins 1.413710x / 1.752823x ; shrinks 0.707359 / 0.570508
judge  **THE RE-SOURCING THE HAND-BACK ASKED ME TO CHECK IS CORRECT**, and the distinction
       it drew -- edges at the DECLARED bound, equal only at the centre -- is real and is
       stated. I found no further instance of the shape in either entry: I recomputed every
       number in both and each is either a line of the script output or named arithmetic on
       two such lines.
cmd    python <the LINEARITY of the mass signal, derived rather than measured>
out    resid_mass - resid = eps * [(1-alpha_m) M ddot_n + alpha_m M ddot_{n-1}]
judge  R720 repair is better than the condition I set. The signal is **exactly** linear in
       eps by construction -- a_eff_s - a_eff = (1-alpha_m) eps M and
       rhs_s - rhs = -alpha_m eps M ddot_n -- so `need` is a solve and not an
       extrapolation, and no re-measurement at the named scale is owed.
```

## 3. R719's REPAIR TOOK A DIFFERENT ROUTE THAN MY CONDITION NAMED, AND THE ROUTE IS BETTER

My condition asked for "a vacuity test on `drop_rel/clean_rel` against a **stated margin**,
with that margin's own boundary solved in both directions". The implementer did not do that:
the exclusion is `signal <= GLOBAL clean worst`, with no margin at all. **That is the
stronger answer and I withdraw my own condition's first clause.** Any ceiling the window
rule can declare is strictly above the clean worst, so a member at or below it cannot redden
the gate at any admissible ceiling -- the exclusion follows from the rule rather than from a
number somebody picked, and my condition would have required an invented cutoff where none
is needed. The implementer asked me to attack this; I attacked it and it holds.

**And the pin IS a guard, not a declaration -- which is question 2, answered.**
`test_the_VACUOUS_moment_members_are_exactly_the_two_declared_pairs` is two-sided: a third
pair becoming vacuous changes the `pairs` list, a pair becoming live changes the count from
12, and either reddens. Combined with
`test_every_NON_VACUOUS_joint_drop_reddens_the_moment_gate`, a member landing between the
clean worst and the ceiling reddens too, so the band the filter leaves open is itself
asserted. The mechanism is sound. **What is not sound is the warrant printed beside it, and
that is R724.**

## 4. TRY TO BREAK IT -- WHAT I RAN AND WHAT IT SAID

* **The window rule solved over EV1's OTHER counter-case** -- found R722. The force
  channel's weakest counter response over both injections is `3.385829e-08`, not
  `0.14137099995337896`, and the ceiling is `1994.78x` looser than its own rule's answer.
* **The ceiling's rise boundary solved against the injection that actually binds** (EH4's
  weakening direction) -- `1.692914e-08` against the published `7.068550e-02`, `4.17537e+06x`.
* **The mass-vacuity test's threshold solved against the claim it holds in place** -- found
  R723. `43.0229x` of slack between the test and the point the claim becomes false.
* **The deck, against the published cause of the exclusion** -- found R724. All four
  hub-platform joints carry `attach_a_body: [0.0, 0.0, 0.0]`.
* **hub2 against hub4, in the script own output** -- identical `moment_rel` to seven digits
  in all six cases. The coordinate separating the vacuous pairs from the live ones is the
  one the gate holds fixed.
* **The gate own 126 ids on a machine without the HSP worktree** -- 124 errors, which is
  CI, which is the STOP.
* **The decomposition control** -- `1.350e-16` to `3.778e-16` over the six cases, and
  asserted by nothing; see R722 last paragraph for the one place that matters.
* **The whole suite at the reviewed commit** -- `3253 passed, 0 failed, 0 skipped`.
* **The report guards alone at the reviewed commit** -- `220 passed`, EG3(ii).

## Findings

**R721. (BLOCKING -- (d), AND THE STOP) THE WHOLE OF LADDER RUNG 4 IS RED IN CI AT THE
REVIEWED COMMIT BECAUSE THE GATE FIXTURE NEEDS AN HSP WORKTREE CI DOES NOT HAVE, AND THIS IS
R670 FOR THE SECOND TIME IN THE SAME DIRECTORY.**
`tests/verification/rung4/test_f4_g41_dynamic.py:89-97` (the `measured` fixture) ->
`scripts/measure/g41_dynamic.py:202-204` (`import report_joint_reactions`, `solve_one`) ->
`scripts/report_joint_reactions.py:81` (`HSP_RUNS = ROOT.parent / "HSP-runs"`) and `:164`
(`import platform_rao_pilot`).

```
cmd    git ls-files | grep -i platform_rao_pilot
out    (nothing -- it is not in the repository)
cmd    ls ../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py
out    ../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py
cmd    grep -n "HSP\|checkout" .github/workflows/ci.yml
out    three actions/checkout@v4, no HSP worktree, no submodule, no fetch
judge  the dependency is a sibling directory outside the repository. FloatSim is not forked
       and HSP is pinned in a second worktree (`docs/hsp-coupling.md`), so this is not an
       oversight CI can be taught -- it is the coupling scheme.
```

The error TEXT is not in the log: `scripts/run_rung.sh` prints the junit tally and the
failing ids and no message, so CI says *that* 124 cases errored and not *why*. I named the
cause from the dependency and the error signature -- exactly the 124 fixture-dependent ids,
4.7 s, no solve attempted -- and not from a traceback.

**And the three routes available inside the step are each measured-red or forbidden:**

* declare the ceilings without a gate -> rung 3 red, measured at `801796e`
  (`test_every_accuracy_entry_has_a_counter_that_something_INJECTS[F4_G41_DYNAMIC_FORCE]`
  and `[..._MOMENT]`). The hand-back is right that BG1 is not failing false.
* declare them with this gate -> rung 4 red, measured at `f07bcb8`.
* make the gate conditional -> forbidden by `CLAUDE.md` ("Never ... skip a test"), by the
  gate file own docstring `:35-37`, and mechanically by `scripts/run_rung.sh:235-249`, which
  exits FAIL on any skipped case.

**The answer is already in the tree and it is R670.** `docs/reports/F4/step-1.md:745-770`
records the identical red -- "CI IS RED AT THE REVIEWED COMMIT AND THE RED IS LADDER 4" is a
quotation from that file -- and the shape that cleared it: a committed snapshot
(`data/platform/buoy_centers_ref.json`) produced by a committed exporter
(`scripts/export_buoy_centers_ref.py`) carrying provenance and a `--check` in the DS0
preflight, **and no pytest skip**. Two files away,
`tests/verification/rung4/test_f4_static_and_mapping.py:848` and `:1028` say in their own
words that a rung-4 gate "must run without an HSP worktree -- the lesson of R670".

**Closed when** the plan row at `docs/milestones/F4.md:486` says what the rung-4 gate READS,
and the gate reads it. The shape I believe satisfies every locked rule at once, named so the
reopen is a sentence and not a redesign: `scripts/measure/g41_dynamic.py --out` already
writes the whole 30-body-case JSON including both counter families; commit it under `data/`
with its provenance (the HSP tag, the deck blob sha, `rho_inf`, `dt`, the six periods), have
the gate assert the ceilings, both counter families, the domain sizes and the vacuous set
against **that**, refuse rather than skip if it is absent or stale, and regenerate it only
under the golden-file rule -- "Golden-file changes require a written explanation of why the
numbers moved". That keeps EV1 30 body-cases, keeps BG1 satisfied, keeps the no-skip rule,
and answers the cost escalation in the same stroke. **The live six-solve run then belongs
where this repository already puts an expensive measurement: the `workflow_dispatch`
determinism leg (CK0), which is recorded as skipped and is explicitly NOT CK2.**

**R722. (BLOCKING -- (b): a tolerance value, its counter, and how the counter is injected)
THE FORCE CHANNEL CEILING, COUNTER AND EH4 BOUND ARE ALL DECLARED OVER ONE OF EV1 TWO
COUNTER-CASES, AND THE OTHER ONE BINDS.**
`floatfea/tolerances.py` (the `F4_G41_DYNAMIC_FORCE` and `F4_G41_DYNAMIC_FORCE_COUNTER`
entries), `docs/milestones/F4.md:539-540`, and `scripts/measure/g41_dynamic.py:519-522`
(`weakest = min(live.values())`, where `live` is the joint-drop family only).

`docs/milestones/F4.md:145-155` locks the ceiling as "the geometric centre between the clean
worst and **the weakest counter response**" and then lists **two** counter-cases that "must
hold for every body and every case". The gate asserts that both must hold --
`test_the_mass_scale_reddens_the_force_gate` is 30 parametrisations of
`signal > F4_G41_DYNAMIC_FORCE` -- so on the force channel the mass injection IS a member of
the family, and the script own output says so in those words:
`mass x(1+1e-06) signal: weakest 3.385829e-08 vs clean 1.855607e-16 -- brackets`. It is then
left out of the minimum computed one line below.

```
cmd    python <the window rule over BOTH families, my own six-case JSON at f07bcb8>
rule   docs/milestones/F4.md:145-155 -- the weakest counter response, both edges >= 2x,
       over the two injections EV1 names
out    clean worst                       1.8556070086831165e-16   hub2/T20
out    weakest over the DROP family      1.4137099995337896e-01   hub1/0/T12.5
out    weakest over BOTH families        3.385828902450096e-08    MASS/hub3/T10
out    centre over BOTH                  2.506545e-12   edges 13507.9518x / 13507.9518x
out    declared 5.0e-9 is                1994.78x LOOSER than its own rule answer
out    upper edge at the declared value, against the injection that BINDS:  6.77166x
out      (the entry and the plan row publish 2.82742e+07x)
out    EH4 rise bound, true              1.692914e-08
out      (the entry and the plan row publish 7.068550e-02 -- 4.17537e+06x out)
out    F4_G41_DYNAMIC_FORCE_COUNTER = 0.1 is 2.95e+06x ABOVE a defect the gate must still
out      fail; counter-above-weakest-over-both -> True
judge  **THE WINDOW RULE IS SATISFIABLE OVER BOTH FAMILIES AT 13508x ON EACH EDGE**, so
       nothing here is a plan conflict and no refusal is needed -- the rule simply was not
       applied to the family EV1 names. The declared 5.0e-9 is still ADMISSIBLE: both
       injections redden it and both edges clear 2x. What is wrong is the derivation and
       every number published for the headroom.
```

**The harm is concrete and it is in EH4 weakening direction, which is why EH4 exists.** A
later reader acting on the published EH4 bound would raise this ceiling toward `7.068550e-02`
believing 2x remained. At any ceiling above `3.385829e-08` the mass injection is no longer
detected -- and that one assertion, at a margin of `6.77x`, is also the ONLY thing in the
gate that would notice the per-joint decomposition being wrong by a common scale factor:
inflate `contrib` by k and `force_rel` falls by k, so the ceiling test gets EASIER; the drop
signals are unchanged because they are `contrib/den`; only the mass signal moves. The script
own decomposition control at `:332-334` is a print statement, so `6.77x` is the whole
interlock -- and `2.82742e+07x` is what the file says it is.

**Closed when** the force ceiling and `F4_G41_DYNAMIC_FORCE_COUNTER` are declared from the
weakest response over **both** of EV1 injections -- `3.385829e-08` on my run, to be
re-measured with the repair -- or EV1 "weakest counter response" is ruled to mean
per-counter-case, by Xabier and not inside the step, with the published upper edge and EH4
bound corrected to the measured ones either way. `scripts/measure/g41_dynamic.py:519-522` is
one expression and it already has both families in hand at `:485-489` and `:537`. **The
moment channel is NOT affected and I checked it**: the mass injection there is vacuous under
the same rule (`1.360110e-09 <= 2.3243458955783927e-06`), so the window over both equals the
window over the drop family -- `0.990856x`, identical edges. The moment entry survives this
attack.

**R723. (BLOCKING -- (c): a gate assertion, on the right quantity at the wrong threshold)
`test_the_mass_scale_is_VACUOUS_on_the_moment_channel` CANNOT FAIL AT THE POINT ITS OWN
CLAIM BECOMES FALSE.**
`tests/verification/rung4/test_f4_g41_dynamic.py:312-343`, the assertion at `:337`
(`signal < F4_G41_DYNAMIC_MOMENT`).

The test exists -- correctly, and its docstring says so -- to hold in place the tolerance
entry statement that EV1 second injection does not BRACKET the moment channel. That
statement flips at the window rule own 2x requirement, `signal >= 2 x clean worst`. The test
threshold is the ceiling instead.

```
cmd    python <max moment mass signal over 30 body-cases, and the flip point, my own JSON>
rule   :337 asserts signal < 2.0e-4 ; the entry claims "three decades BELOW the clean
       worst" and the script prints "DOES NOT BRACKET at 2x"
out    max moment mass signal   1.6377355440545113e-07   platform/T20
out    flip point, 2 x clean    4.648692e-06
out    the test threshold is    43.0229x ABOVE the flip point
out    the max signal is        28.3849x below the flip point, 1221.2x below the threshold
out    at the flip point the window-rule centre becomes 3.287121e-06, so the declared
out      2.0e-4 would then sit 60.84x above its own rule answer
judge  **43x OF SLACK BETWEEN THE CHECK AND THE CLAIM.** Anywhere in that band the entry
       sentence is false, the moment ceiling derivation has moved underneath it by 61x, and
       the test is green. The quantity is right; the threshold is the ceiling where it
       should be twice the clean worst -- and `_clean_worst(measured, "moment")` is already
       computed in this very file at `:109-121`, so the right number is one call away.
```

**Closed when** `:337` asserts against `2.0 * _clean_worst(measured, "moment")[0]` -- the
rule the claim is actually about -- with the resulting margin measured and pasted, and with
the failure message still saying "raise the finding rather than widening anything", which is
the right instruction and should survive. **No new apparatus: one expression and one call
already in the file.**

**R724. (BLOCKING -- (b): the warrant for excluding 12 of 120 counter-family members) THE
PUBLISHED CAUSE OF THE MOMENT CHANNEL VACUITY IS REFUTED BY THE DECK, AND THE COORDINATE
THAT DOES SEPARATE THE TWO PAIRS IS ONE THE GATE HOLDS FIXED IN ALL SIX CASES.**
`floatfea/tolerances.py` (the `F4_G41_DYNAMIC_MOMENT` entry, the paragraph beginning "The
cause is geometric and it is only two of the four hubs"),
`tests/verification/rung4/test_f4_g41_dynamic.py:266-269`, and `docs/milestones/F4.md:541`
("because those joints sit at their hubs reference points").

The claim: "hub1 and hub3 platform joints sit AT those hubs reference points, so there is no
lever ... **hub2 and hub4 platform joints are not at their reference points and are not
vacuous.**"

```
cmd    python -I <read data/platform/platform12_deck.yaml, print every platform joint>
rule   the quoted sentence, which is the stated reason 12 of 120 members are excluded
out     3  hub1 -> platform   attach_a [0.0, 0.0, 0.0]
out     7  hub2 -> platform   attach_a [0.0, 0.0, 0.0]
out    11  hub3 -> platform   attach_a [0.0, 0.0, 0.0]
out    15  hub4 -> platform   attach_a [0.0, 0.0, 0.0]
out    all four hubs: mass 12.0, inertia 0.5/0.5/1.0, z 0.4933695679797303, buoy anchors
out      (0.5,0,0) and (-0.25,+-0.433013,0) in body frame -- identical, all four
judge  **ALL FOUR SIT AT THEIR HUBS REFERENCE POINTS.** The second half of the sentence is
       false as written, and the first half cannot be the discriminator, because the four
       hubs are identical in mass, inertia, anchor and buoy layout. The split it is offered
       to explain is 3e+07 wide -- hub1/3 and hub3/11 at 1e-09, hub2/7 and hub4/15 at
       3.03e-02 .. 4.25e-02 -- and no lever-versus-no-lever story covers that, because none
       of the four has a lever.
cmd    python <hub2 against hub4, moment_rel, every case, from my own run>
out    T10 2.435996e-07 / 2.435996e-07   T14 6.777114e-07 / 6.777115e-07
out    T15 7.318866e-07 / 7.318866e-07   T16.2 6.978779e-07 / 6.978779e-07
out    T20 4.221282e-07 / 4.221283e-07   and hub2/7 against hub4/15 agree to 7 digits too
out    hub1 and hub3, by contrast, differ from each other in every case
judge  hub2 and hub4 sit at x = 0 and hub1/hub3 at x = +-1; the wave runs along +x
       (`scripts/report_joint_reactions.py:193`, `heading_deg=0.0`, and
       `scripts/run_floatsim_design_waves.py:177` tags every case head0). The two bodies at
       the same wave phase produce the same number to seven digits, and **the two excluded
       pairs are exactly the two hubs ON the wave axis.** I attach no cause: I did not run
       the heading cell. What is measured is that the stated cause is false and that the
       variable correlated with the exclusion is one all six cases hold fixed.
```

This is R719 own defect with the sign reversed. R719 was "the vacuous set is case-dependent",
attributed to a mechanism nobody measured; the repair replaced it with "the cause is
geometric", attributed to a mechanism nobody measured, and the deck refutes it in one line. I
block rather than filing it as prose because under CZ0 it is the **only statement of why 12
counter-family members are excluded**, which is "a counter and how it is injected", and
because it is the stated warrant for the pin at `:278-286` being a structural fact rather
than a heading-0 artifact. The pin mechanism is sound (section 3); its justification is not.

**Closed when** the sentence is made true or deleted (CW0) at all three sites --
`floatfea/tolerances.py`, `test_f4_g41_dynamic.py:266-269` and `docs/milestones/F4.md:541`
-- with the deck four identical `attach_a_body` rows pasted, and **BG0 cell for whatever
cause replaces it**: one variable moved. The cheap one is one case at `heading_deg = 90`; if
the vacuous pairs move to `hub2/7` and `hub4/15`, the cause is the heading and the pin own
scope is a heading-0 statement, which the entry should then say. If no cause is measured, the
correct text is the bare measurement -- the four signal ranges with nothing attached to them.

## Tolerances touched

```
cmd    git diff 0e4188a..HEAD -- floatfea/tolerances.py | grep -E "^[-]" | grep -vE "^---"
out    (no output)
judge  **126 LINES ADDED, NOT ONE LINE REMOVED OR CHANGED.** No existing value, counter or
       comment moved; nothing was widened. The four new declarations are the whole subject.
```

| name | old | new | form | counter | justification located | ruling |
|---|---|---|---|---|---|---|
| `F4_G41_DYNAMIC_FORCE` | -- | `5.0e-9` | dimensionless, relative; denominator a sum of magnitudes | `_COUNTER` 0.1 injected by the joint drop at `test_f4_g41_dynamic.py:208-230`; EV1 mass injection at `:289-309` | `floatfea/tolerances.py` entry; plan `docs/milestones/F4.md:539`; script `:519-522` | **BLOCKED, R722.** The value is admissible and every figure in the entry reproduces, but it is `1994.78x` looser than the window rule over EV1 two injections, its real upper edge is `6.77166x` and not `2.82742e+07x`, and its EH4 rise bound is `1.692914e-08` and not `7.068550e-02`. |
| `F4_G41_DYNAMIC_FORCE_COUNTER` | -- | `0.1` | dimensionless | is itself the counter | same entry; plan `:540` | **BLOCKED, R722.** Declared as "the SMALLEST defect the gate must still fail, over the whole family" and sitting `2.95e+06x` above a defect the same gate asserts it must fail (`3.385829e-08`). The two injections are held to two different thresholds -- the drop to the counter, the mass to the ceiling -- which is the inconsistency that reveals it. |
| `F4_G41_DYNAMIC_MOMENT` | -- | `2.0e-4` | dimensionless, relative; moments about each body `reference_point`, stated | `_COUNTER` 0.01 over the 108 non-vacuous members at `:233-258`; the mass injection asserted VACUOUS at `:312-343` | same entry; plan `:541`; script `:490-528` | **BLOCKED on R724 only.** The window rule, the exclusion rule and every figure are right and I reproduced all of them; the window over both families equals the window over the drop family (`0.990856x`), so R722 does not touch this channel. What blocks is the warrant printed for the exclusion. |
| `F4_G41_DYNAMIC_MOMENT_COUNTER` | -- | `0.01` | dimensionless | is itself the counter | same entry; plan `:542` | **CLEAN as a value, blocked by R723 as an assertion.** `0.017528231438113724` over 108 members, margin `1.7528x`, reproduced exactly; the `1 + 3.417879e-03` figure is an exact solve rather than an extrapolation and I verified the linearity algebraically. The entry statement that EV1 `1 + 1e-6` does not bracket is held in place by a test `43.0229x` too loose. |
| the FE inertia-relief acceleration (EV1 third bullet) | -- | **still not built, and I rule it BLOCKING by name** | would be normalised by `max_t abs(a)` and `max_t abs(alpha)` | -- | plan `docs/milestones/F4.md:140-141`; NO row in the plan tolerance table | **(c), AND DEFERRING IT TO EV2 ITEM 2 COMMIT IS CORRECT.** `grep -c inertia_relief` is `0` in both the gate and the script; I verified it. The plan requires the assertion, so its absence is (c) and not a closure item, and the hand-back is right to carry it by name. It does **not** have to land in this commit -- nothing in EV1 orders the three bullets -- but it must land before step 3 closes, and if step 3 closes with it open it carries by name into step 4. Note that by `:145-148` it needs a THIRD pair of declarations, and the plan tolerance table has no row for them. |
| everything else in the F4 block | -- | unmoved | -- | -- | -- | Not touched in this range and not re-swept. |

## Carried

Verdict 105 (`0e4188a`) was ROUND 1 OF THREE. It raised two blocking items and carried a
closure list. Every one, with status.

* **R719 (blocking) -- CLOSED, and I withdrew one clause of my own condition.** Answered at
  `becf47c`. The bracketing test is against the GLOBAL clean worst over all 30 body-cases
  (`scripts/measure/g41_dynamic.py:496-497`, `test_f4_g41_dynamic.py:109-121`), the signal is
  the joint own contribution rather than the absolute residual (`:359-369`), the exclusion is
  pinned two-sided (`:261-286`), the case-dependence sentence is gone and replaced, and my
  three-case `86.8379x` becomes `86.8398x` over six -- confirmed, not beaten. **My "stated
  margin" clause is WITHDRAWN**: the repair needs no margin and mine would have invented a
  cutoff. **Does not carry, except that the replacement warrant is R724.**
* **R720 (blocking) -- CLOSED, at the first branch of my condition.** Answered at `becf47c`.
  `max_t abs(resid_mass - resid)` is what is measured (`:353-358`), the 2x edge is solved
  against the global clean worst (`:539`), and the linearity is now exact rather than
  assumed -- I derived it rather than taking it:
  `resid_mass - resid = eps * [(1-alpha_m) M ddot_n + alpha_m M ddot_{n-1}]`. Both
  `1 + 3.417879e-03` and `1 + 1.096102e-14` reproduce. **Does not carry.**
* **C1 (closure, past its trigger) -- CLOSED.** Answered at `7799482`,
  `scripts/report_joint_reactions.py:232-258`. Both halves: `N.m / N` is a LENGTH, so the
  direction was inverted, **and** the premise that `max abs(Sum reactions)` is always the
  force half was wrong, 11 of 17. Verdict 102 condition was that it land before the
  G4.1-dynamic quantity is chosen; it landed in the same range as the declaration. **Does
  not carry.**
* **C24 (closure) -- CLOSED.** The dead `per_joint_contributions` is deleted and `:145-162`
  states the form directly instead of by reference to it.
* **C25, C26, C27 (closure) -- STILL OPEN**, and correctly so: all three are about the step
  report, and there is no new report revision. They are revision 2.
* **R712, R713, R714, R716, R717 (closure) -- STILL OPEN.** R712:
  `scripts/report_joint_reactions.py:120` still ships `PLATFORM_MASS_OVERRIDE = None` and the
  override is still typed in `g41_dynamic.py:212-216` -- **and that matters more than it did
  last round**, because the gate figures now depend on a module global the gate own fixture
  writes. R717 producer repair is still the thing that would stop this verdict from needing a
  hand-added bold line, and I have added one again.
* **The three commit-message figure errors the hand-back volunteered** (`116` for `120`, `22`
  for `23`, and `grep -c "1/length"` pasted as `0` where it prints `1`) -- recorded, not
  re-litigated, closure class. Self-reporting them before I looked is the practice I keep
  asking for and it is worth saying so.
* **Verdict 103 escalation and verdict 105 warning -- NOW DUE.** Verdict 105 said: "If they
  are still open at revision 2, that is a third consecutive step and the choice has to be
  made rather than restated." R719 and R720 are closed, so that particular sentence does not
  fire -- but the STOP does, and it fires at the same place. The escalation is stated with
  its choice under "On the questions I was asked".

## The adversarial corpus (BE3)

**NO BATCH THIS ROUND, AND NO COVERAGE NUMBER.** ES0 light scope says "no corpus batch" and
I honour it literally, as verdict 104 did. EG4(e) would otherwise have permitted one here --
G4.1-dynamic is the surface verdict 105 justified -- so the batch is owed at revision 2 or at
the 28 October batch, whichever comes first, and it now has four shapes to plant that were
not in batch 38: a counter family split across two injections with the minimum taken over
one; a check whose threshold is looser than the claim it holds in place; a vacuous set whose
stated cause is refuted by the input file; and **a gate that is green only on the machine
that has the out-of-tree dependency.** My own hygiene item on
`tests/corpus/f4_static_case_and_member_force_recovery.txt` lines 40, 48, 49 and 50 is
unchanged and still mine.

## On the questions I was asked

**1. The gate assertions, run.** `3253 passed, 0 failed, 0 skipped` here, and `124 errored`
in CI. Both are the answer and the second is the one that counts: CA2 exists because a
measurement taken only where it was written is a claim about a machine. The hand-back was
right to say it was not claiming the gate passes, and right that a red would be CZ1 (iv)
rather than a boundary state. It is.

**2. Is the vacuity rule a disguised invented cutoff? NO, and the pin IS a guard.** Section
3. The exclusion follows from the window rule rather than from a chosen number, and it is
better than the margin my own condition asked for -- I withdraw that clause. The pin is
two-sided in both directions and the band the filter leaves open is asserted elsewhere.
**But its stated warrant is false (R724)**, and the warrant is what the question was really
about: the pin will not be "edited the next time a case moves" by its mechanism, and it will
be if the reason printed beside it is wrong about which coordinate it depends on.

**3. EU1 adversarial case.** Run, and mandatory here because four values moved. The
injection the hand-back most expected to be wrong --
`test_the_mass_scale_is_VACUOUS_on_the_moment_channel` -- does not reach the ceiling on any
body or case: the maximum over 30 body-cases is `1.6377355440545113e-07` against `2.0e-4`.
**The direction is right and the threshold is not (R723).** The finding the hand-back did not
expect is next door: the same injection on the FORCE channel brackets, binds, and was left
out of the minimum (R722). The script prints the word "brackets" one line above the minimum
it is excluded from.

**4. The script as gate code -- I AGREE, ON THE WORK AND ON THE CRITERION.** Importing one
implementation of the residual rather than carrying a second is right, and R711 is the
measured reason. The plan row records it in the same commit (BR0). I ruled in verdict 105
that a script under `scripts/measure/` whose output is a declared tolerance derivation is (b)
while it is used that way; this is the stronger form of the same thing, and the question I
put to Xabier last round is answered by the work, in the direction I favoured. **Two
consequences that follow from the ruling rather than from me, and which nobody has stated:**
`mypy` does not cover `scripts/` -- `.github/workflows/ci.yml:386` is `mypy floatfea`, while
`ruff` and `black` at `:382-384` do include `scripts` -- so the gate numerics are now the
only gate code in the repository that is not type-checked, and
`per_joint_contributions(g, lam, ...)` and `moment_point(deck)` are untyped. And R712
`PLATFORM_MASS_OVERRIDE` is a module global that the gate own fixture writes, so the gate
SETS its basis rather than reading it.

**5. The four re-sourced figures.** Correct, and the distinction drawn is real. I recomputed
every number in both entries and found no further instance of the same shape. The residual
BI3 exposure is that the four edges at the declared bound are arithmetic the script does not
print, so they go stale silently if the model moves -- two extra print lines in a script that
already holds both inputs. Recorded, not blocking.

**6. EV1 third assertion.** Ruled in the tolerances table: (c), blocking by name, and
deferring it to EV2 item 2 commit is correct. It needs a third pair of declarations for which
the plan tolerance table has no row.

**7. The cost -- IT IS XABIER CALL, AND R721 PROBABLY DISSOLVES IT.** Reducing the gate from
30 body-cases to 5 is a change to what the gate asserts, which is (c), and EV1 locked "every
body and every case" -- so the implementer may not make that trade inside the step and
neither may I. **But the trade as offered is the wrong one.** R721 repair -- the gate reads a
committed 30-body-case measurement, refuses if it is absent or stale, and the live six-solve
run moves to the `workflow_dispatch` leg -- keeps all 30 body-cases, costs CI nothing per
push, and is the pattern R670 already established in this directory. I would put that to
Xabier rather than the choice between 30 cases and 5. I attach **no figure** to the gate
cost: my `2202.30s` against verdict 105 `753.75s` is not a controlled pair, because my own
six-case script run shared this machine for most of it.

**And the escalation, stated rather than restated.** Step 3 is past round 1 with a STOP, EV2
items 2 to 5 unstarted, and a 14 October date. Two consecutive steps have already closed
carrying blocking items. **The choice is: slip the date, or cut scope to EV1 two channels
plus the member-force table and defer the acceleration assertion, the `f` sensitivity and the
six-case envelope to F5.** That is Xabier, it goes out through the implementer, and it should
go out today rather than at closure -- `CLAUDE.md` says slippage is reported the day it is
known.

## On the criterion -- I was asked, and I agree, with one note I have made before

CZ0 is right and I applied it. Three of my four findings are (b) or (c) and the fourth is
(d); nothing in this verdict is a figure or a sentence held against the step, and the closure
class took the rest. Per ES0 light scope I have written **no closure list** -- the items I
noticed and did not block on are named inline where they arise (the `mypy` gap, the BI3
exposure on the four arithmetic edges, the decomposition control that is printed rather than
asserted, and `run_rung.sh` swallowing the error text of a 124-error rung) and they go into
revision 2 closure list rather than into this verdict as a heading.

**The note, unchanged from verdicts 104 and 105.** Two of my findings live in `scripts/`,
which CZ0 lists under "generators" as closure class, and I block on them under the carve-out
my own instructions give -- a generator whose output *is* a gate assertion. **That carve-out
is no longer needed for this file**: as of `f07bcb8` the gate IMPORTS it, so it is gate code
on the plain reading and the plan row says so. What I would add is that a file which becomes
gate code should enter the lint and type gates in the same commit, and this one did not.

## Next step opens when

**Step 3 does not resume on the current plan row. This was an ES0 INTERIM CHECK and it counts
against NO round -- two reviewed revisions remain -- but the STOP halts implementation until
the plan row is decided.** In order:

1. **R721 is resolved at the plan, not inside the step.** `docs/milestones/F4.md:486` says
   what the rung-4 gate READS. Until it does, rung 4 is red on every machine but one and
   nothing above it runs. The repair I believe satisfies EV1, BG1, the no-skip rule and the
   cost at once is named in the finding, and R670 own mechanism is two files away.
2. **R722 is answered** -- the force ceiling and counter declared from the weakest response
   over **both** of EV1 injections, or EV1 wording ruled by Xabier; and the published upper
   edge and EH4 rise bound corrected to the measured ones either way.
3. **R723 is answered** -- `:337` asserts against `2.0 * _clean_worst(measured, "moment")`,
   with the resulting margin pasted.
4. **R724 is answered at all three sites** -- the deck four identical `attach_a_body` rows
   pasted, and either BG0 cell for the cause that replaces it (the `heading_deg = 90` case is
   the cheap one) or the bare measurement with no cause attached.
5. **EV1 third assertion carries by name**, blocking, into EV2 item 2 commit, with the third
   pair of declarations and a plan row for them.
6. **The escalation goes to Xabier today**, with the choice stated, per the section above.
7. **Revision 2 header says `verdict 106`** -- instruction 1b, and the thing that makes
   `tests/test_report_carried.py` mean anything.

**What I will not accept at revision 2.** A ceiling whose published headroom is six decades
larger than its distance to the injection that binds it, or a test that holds a tolerance
entry statement in place at forty-three times the threshold the statement is about. Neither
is a judgement about figures. Both are the same single question -- if the thing this
assertion claims were false, would it go red -- and for the force channel EH4 bound the
answer is that it would go red four million times later than the file says.

**And one thing on the record for the implementer rather than against them.** Every one of
the forty-odd figures in two new tolerance entries and four new plan rows reproduced exactly
on my own independent six-case run: both clean worsts, both weakest members, both centres,
all four edges, both EH4 bounds, the twelve vacuous signals and both solved mass scales. R719
and R720 were closed properly, and one of them with a better repair than the condition I set,
which I have withdrawn in its favour. The hand-back named the one thing it had not been able
to run, said so plainly, and asked me to run it. I ran it, and what it found was not in the
numbers -- it was that the gate had never been run anywhere except here.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

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
