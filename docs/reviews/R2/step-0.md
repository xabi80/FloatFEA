# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 3d24e1c3808cd6be35490eab76b43f5ccf9d175b
**Reviewed commit: `3d24e1c3808cd6be35490eab76b43f5ccf9d175b`.**
Verdict: HOLD
Scope: **ES0 INTERIM CHECK on the OPEN step** -- no new report revision exists
(`git ls-files docs/reports/R2` is empty; `docs/reports/R2/step-0.md` is untracked), so this
**counts against none of step 0's three revisions** and closes nothing, and `--closes` is
correctly absent (FK1). Light scope per ES0: the suite, CI at the commit, and a CZ0 (a)-(d)
scan of the diff. **Ruled under FR1 with EZ0**, and each blocking finding names the silently
wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.**
**EU1 DOES NOT ARISE, MEASURED RATHER THAN TAKEN:** `git diff adc6c3c..3d24e1c --
floatfea/tolerances.py` is empty, so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`,
and no declared counter moves anywhere in the diff. **I took the diff from `91c2d2e`, the last
JUDGED commit, not from `adc6c3c`**, so `8c0edce` is inside it and is judged below.
**GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the
overrun is the per-id trace of 108 reds with its one-variable control (EG3 (i) forbids ruling
a cascade by family), two blocking findings with their cells, and the four rulings you asked
for by name.
Tests: **MY OWN RUNS, in my own worktree at the judged sha, `-p no:randomly`, and the first
reproduces your figure exactly rather than taking it.**
* your stated selection -- `tests/unit` + the four root guards +
  `rung3/test_platform_deck_export.py` + `rung4/test_f4_g41_dynamic.py`:
  **1 failed, 828 passed in 365.65s**, and the one failure is the staleness guard.
* the six report-guard files: **108 failed, 557 passed, 1 skipped in 442.68s**, traced per
  id below. Your selection excludes all six, so your report's "1 failed" is true of what it
  ran and silent about the file where the marker decision lands.
* CI's own guards selection, `pytest tests --ignore=tests/unit --ignore=tests/verification
  --ignore=tests/regression`, in a second worktree: **108 failed, 1047 passed, 1 skipped in
  903.77s -- THE SAME 108, id for id.** `comm -23` and `comm -13` over the two sorted FAILED
  lists are BOTH EMPTY, so **no root test outside the six report-guard files is red at this
  commit** and nothing is hiding inside CI's aggregate.
* the one-variable control (marker back on R1 step 4, this commit's code unchanged):
  **8 failed, 849 passed in 607.41s** -- see the trace.
* `ruff check floatfea tests scripts`, `black --check floatfea tests scripts`,
  `mypy floatfea`: **all clean, my own runs.**
* **NOT RUN LOCALLY and I say which rather than implying coverage**: rungs 1, 2, 5, 6 and
  `tests/regression`. The reason is measured, not assumed:
  `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` alone, and
  `git grep -ln hsp_pin -- tests` outside the corpus returns only
  `rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py`, so no test in
  those rungs reaches a changed line. FV1 puts the whole of `tests/regression` on CI.
CI: **run `44118920983` at the FULL sha `3d24e1c3808cd6be35490eab76b43f5ccf9d175b` EXISTS
and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with
`actionlint`, `ruff`, `black --check`, `mypy` and `unit tests` all **success** before it --
so the guards step is seen to have RUN rather than been skipped behind an earlier red
(CZ1 iii). **`the verification ladder` had NOT finished when I ruled** (`in_progress`, both
runners assigned, started 15:50:31Z); a run that has not finished is not a pass. Expect it
to redden at `ladder 4` on the same staleness guard -- and note CI orders `ladder 6 --
tests/regression` BEFORE `ladder 4`, so that rung is not hidden behind it. Both determinism
jobs `skipped` by their own `workflow_dispatch` condition. **This is NOT CK2**: runners
`GitHub Actions 1000001916` and `1000001917` were assigned and the jobs executed for
minutes. **CA2 IS REACHED -- CI is red at the judged commit** -- and the per-id list is
**unavailable, not skipped over**: `gh run view --log` refuses while any job is in progress
(*"logs will be available when it is complete"*), so the id-for-id agreement between my 108
and CI's list is deferred to the next revision. FP1 held: the commit was pushed before I was
invoked. GC2 does not arise -- `git diff --name-only 91c2d2e..HEAD` touches `floatfea/` and
`scripts/`, so the push triggered a run of its own. **One throughput observation, not a
finding:** the runs at `91c2d2e` and `8c0edce` are STILL `in_progress` after 1h18 and 1h00,
their ladders unfinished, because GG3's per-commit group no longer cancels them -- three
ladders now run in parallel and CI's answer arrives long after the commit.
Door (FV2 / GG2): `git worktree add -b review/3d24e1c3808c <a path outside the repository>
3d24e1c3808cd6be35490eab76b43f5ccf9d175b` **succeeded on the first try, so no review of this
commit existed**; `git push origin review/3d24e1c3808c` likewise. Every measurement above was
taken in that worktree, and this verdict is written there through `scripts/write_verdict.py`,
committed on that branch and pushed -- merge it with `git merge --ff-only
origin/review/3d24e1c3808c`. **Three writes of my own, all in my own worktree and all
reverted before committing** -- the marker-1 cell, the marker control, and a second DETACHED
worktree for CI's wide selection, which I removed with `rm -rf` followed by `git worktree
prune` -- the one `.git`-metadata write I made in `C:\dev\floatfea`, which touches no file
in the working tree and which I disclose rather than leave for you to find. `git status --porcelain` there is empty
and both marker lines read as committed. In `C:\dev\floatfea` I ran only read-only `git` and
`gh`, and the one write-shaped thing I did touch -- `preflight()` against the real
`HSP-stable` -- reads only (`git describe`, `git hash-object` without `-w`) and wrote nothing.

## Carried

Verdict 59's four blocking findings, its four closing conditions, and verdict 58's items
routed to R2's first report. **Three of four answered; two halves open.**

* **R1205 (two live markers; the `Carried` gate reporting on F2 step 4) -- ANSWERED, and I
  re-ran both checks the condition asked for rather than reading them.**
  `docs/milestones/R1.md:3` now reads `<!-- step-under-execution: moved to R2 at step 0
  (GI) -->`, the `F2.md:10` form.
  ```
  cmd  grep -rnE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
  out  docs/milestones/R2.md:3   (one plan, not two)
  cmd  python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
  out  ('R2', 0)
  cmd  python scripts/check_carried.py ; echo exit=$?
  out  check_carried: .../docs/reviews/R2/step-0.md or .../docs/reports/R2/step-0.md missing
       exit=1
  cmd  python -c "import sys; sys.path.insert(0,'.'); import scripts.ci_section as c; print(c.MILESTONE, c.STEP)"
  out  R2 0
  ```
  The gate that was green about the wrong milestone is now red about the right one, naming
  the file the next revision adds. That is the repair.

* **R1206 (`0` is both a legal step number and the resolvers' sentinel) -- STILL OPEN,
  still blocking, and it carries by name into step 0's list.** You do not claim it
  answered; what shipped is verdict 59's **cell 2**, not exit (ii) -- see R1215 and
  ruling (1), where I withdraw the escalation by measurement.

* **R1207 (step 2's gates (ii) and (iii) both passable by a no-op) -- ANSWERED in the
  plan, at `docs/milestones/R2.md:317-332`.** (ii) is now a pair with the inverted half
  stated as the gate ("a run at a PERTURBED mass does *not* [reproduce], differing in
  `case<i>/body_mass`, `m_xddot` and `accel`"), and (iii) closes against
  `case<i>/body_mass` read back from the npz. Both citations resolve in substance; one
  line number is off by three (R1217).

* **R1208 (one key is silent in one direction) -- HALF ANSWERED. The two keys are
  written and routed correctly; the half that says "the three DS0 refusals shown firing
  after the change" FAILS BY MEASUREMENT.** The routing I checked site by site, as you
  asked:
  ```
  cmd  git grep -n "hsp_pin.worktree(" -- scripts
  out  export_buoy_centers_ref.py:42   "stable"     <- correct, the no-refusal site
       export_platform_deck.py:45      "runs"
       measure_platform_joints.py:52   "runs"
       report_joint_reactions.py:96    "runs"
       run_floatsim_design_waves.py:55 "runs"   :56 "stable"   <- both, correct
  cmd  for each touched script: import it with NO worktree present and NO env var set
  out  OK export_buoy_centers_ref / export_platform_deck / measure_platform_joints /
       report_joint_reactions / run_floatsim_design_waves / f4_dynamic_residual /
       export_f4_dynamic_inputs      (7 of 7 -- `require=False` does what its docstring
       claims and R670's import-time ImportError is avoided, measured not argued)
  ```
  The refusals are **R1213**: two of the three fire on the adversarial input, one does not.

* **Verdict 59's ledger -- R1209, R1210, R1211, the Â§4 row-1 form, the CP3 header, the
  triple grammar, and Â§5's DO-NOT-HAND-EDIT line: all SIX addressed in the plan diff.**
  I read each against its site. R1209's census is rewritten with a needle that finds all
  seven (`git grep -nE '(ROOT|parents?\[[0-9]\])...'`) and now splits runs from stable;
  R1210's false `out` line is replaced by what the command returns, with the consequence
  for D4 stated; R1211 gains the one-body/three-component limit and the GI1 declared-file
  distinction; Â§5 gains the deck bullet; the CP3 header names its two carried figures; the
  triple-grammar paragraph is accurate -- `grep -c "^cmd:" docs/milestones/R2.md` is `0`
  and the file says so rather than pretending otherwise. **The Â§4 row-1 form is half
  right and I re-open that half as a ledger item (R1218).**

* **R1212 -- unchanged, mine, Xabier's.** The verdict is at `step-0.md` and not `plan.md`
  for the reason recorded there; this entry accumulates into the same file under DX2.

* **Verdict 58's items -- R1196 to R1201, R1186, R1188, R1189 (c), R1190, R1191, R1193 --
  STILL OPEN, due in R2's first report**, which is in flight. None is answerable by this
  commit and none is a plan matter. **R1193 stays discharged from my side** (I am
  operating under the post-`2e08766` text). **R1203, R1204 -- reviewer-side or Xabier's.**

* **Verdict 59's four "things for step 0's report" -- not yet due**, and three of the four
  are the report that is in flight. The `--check` determinism run is ruling (4) below,
  where I correct what it can and cannot clear.

## The 108, per id, at this commit -- traced from each id's own message (EG3 (i))

```
cmd    python -m pytest -q -p no:randomly <the six report-guard files>, my own run in my
       own worktree at the judged sha
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    grep "^FAILED" | strip the parameter | sort | uniq -c
out    50  test_every_named_site_is_touched_or_declared[...]
       21  test_the_report_carries_the_finding[...]
       19  test_the_guard_survives_the_state[...]
       18  singletons in test_report_carried / test_report_guard_states /
             test_report_numbers_are_sourced
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST verdict
       (verdict 59, `adc6c3c`, whose entry is in this same file). Limb two: its SUBJECT is
       the commit carrying it.
```

**The 50 and the 21 are parametrised over verdict 59's OWN findings and sites**, so limb one
holds by construction, and their messages say what clears them: *"...the step's diff does not
touch it, and the newest report revision does not say..."* and *"the report does not carry
..."*. EG3 state (2), cleared by the answering report. **Three of the 50 are worth naming
rather than waiving silently, because their content IS R1213:**
`[R1208-run_floatsim_design_waves.py:98]`, `[R1208-report_joint_reactions.py:106]` and
`[R1208-export_platform_deck.py:75]` -- the three DS0 refusals -- are red because *the diff
does not touch them*. The guard is enforcing CLAUDE.md's *a closing condition that names
sites is closed site by site*, mechanically, and it is right: two of the three needed no
change and one did.

**The 19 share ONE cause with the singleton `test_R887_...`, and the harness names it
itself** rather than being ruled by class: R887 reports *"the harness copies FROM step-0.md,
which does not exist. Every state built by a `copy2` dies in `_build` before planting
anything."* State (2). Two of the 19 additionally report `<state>: expected a clean run`,
which is the same absence seen from inside the inner run.

**The 18 singletons, each read individually. SIXTEEN are state (2) in their own words** --
*"the newest report revision has no `Answers:` header"*, *"...no Carried section"*, *"...no
`## ... CI ...` section"*, *"the CI section names no commit"*, *"no step report found
under docs/reports/R2"*, *"step-0-answers.json is not committed ... That is EG3 state (2)"*.
That sixteen includes the two names FC1 put under limb two,
`test_the_report_carries_a_WHOLE_SUITE_count` and
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` -- **and limb two is not needed for either
here**, because at this commit they fail on report absence like the rest (*"the newest
revision carries no whole-suite line"*, *"the 0a table has neither a run row nor the
generator's zero-run row"*). Measured, not assumed from the name. **And two are neither,
and they are the two that matter:**

* **`test_the_plan_names_the_step_under_execution` is R1206 ITSELF.** The marker count is
  now 1, so the first assertion passes; it dies at `assert _plan_step() > 0`. It is not a
  boundary red and it needs no waiver -- it is the true, loud symptom of an open blocking
  finding carried from verdict 59, and it clears when exit (iii) is taken and not when a
  report is written.

* **`test_a_blocking_item_is_not_routed_to_4a` IS MINE, AND NO REPORT CAN CLEAR IT --
  R1222 under Findings.** It is red on verdict 59's heading FORMAT, not on anything the
  implementer did or can do.

**So: of 108, ONE HUNDRED AND SIX are EG3 state (2) and the waiver covers them --
50 + 21 + 19 + 16, which sums exactly; ONE is R1206, already blocking and already carried;
ONE is mine (R1222). The 109th red, `test_the_npz_is_NOT_STALE...` in the separate rung-4
run, fails the predicate and is CZ1 (iv) unchanged.**

**THE CONTROL, ONE VARIABLE, AND IT IS THE MEASUREMENT THAT SETTLES OWNERSHIP OF ALL 108.**
A list of names cannot be checked against a failure message and a family cannot be ruled as a
cascade (EG3 (i)), so I moved the marker back to `8c0edce`'s state **with this commit's CODE
DIFF LEFT IN PLACE** -- R1 at step 4, R2's retired -- and re-ran the identical selection in my
own worktree, then reverted (`git status --porcelain` empty, both marker lines back):

```
cmd    the judged tree (R1 retired, R2 at step 0), six report-guard files
out    108 failed, 557 passed, 1 skipped in 442.68s
cmd    ONE VARIABLE MOVED -- the marker back on R1 step 4, R2's retired, same code
out      8 failed, 849 passed in 607.41s
cmd    the eight, by name
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
       test_the_guard_survives_the_state[baseline, non_numeric_step_suffix,
         superscript_digit_step_number, draft_suffix_beside_a_step_report,
         step_number_is_the_empty_string,
         verdict_amended_after_the_commit_the_report_answers, zero_padded_step_number]
rule   FS1/FT1 per id, and `8c0edce`'s own trace of the same eight
judge  **THE EIGHT ARE EXACTLY THE SET `8c0edce` TRACED BY NAME, id for id**, including the
       one it showed red at `251af69` before this turn began. So **not one of the 108 is
       caused by the code in this commit** -- the hundred extra are a function of the
       marker/no-report state alone, and the collection total moves with it (666 vs 857)
       because both guards are parametrised over the active report's verdict (R861).
```

That is the control R1 step 1's report got wrong by comparing two instances of the SAME state:
here the two cells differ in one variable and the code is held fixed, so it separates "red
because no report exists" from "red because of this diff". The answer is all of the first.

## Findings

**R1213. (BLOCKS) The DS0 refusal in `run_floatsim_design_waves.py` DOES NOT FIRE on the
input this diff newly admits, and I ran it against the real production worktree rather than
reasoning about it.**

```
claim  verdict 59's condition 4 -- "the three DS0 refusals shown still firing" -- holds
       after the change
cmd    FLOATFEA_HSP_RUNS=C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable, the stable key
       UNSET and its legacy sibling absent (the state measured at C:\dev\floatfea);
       import scripts/run_floatsim_design_waves and call preflight() -- preflight only,
       nothing written
out    RUNS   = C:\Users\xlama\OneDrive\Documents\buoy\HSP-stable
       STABLE = ...\scratchpad\HSP-stable            (the legacy candidate, absent)
       worktree  HSP-stable at floatfea-ref-1
       database  blob f26501001916, sha256 3dca8b131b4a028b -- matches the commit
       output    ...\HSP-stable\studies\platform-12buoy\floatfea_design_waves
       >>> preflight() RETURNED. DS0 did not fire.
cmd    the same input, through the OTHER two refusals' predicate
out    "HSP-stable" in RUNS.resolve().parts  ->  True     (they DO fire)
       RUNS.resolve() == STABLE.resolve()    ->  False    (this one does not)
rule   scripts/run_floatsim_design_waves.py:102 -- the refusal is an IDENTITY test against
       the other key, not a NAME test. report_joint_reactions.py:109 and
       export_platform_deck.py:77 test the name and are unaffected.
cell   one variable: at `91c2d2e`, `RUNS = Path(__file__).resolve().parents[2] /
       "HSP-runs"` reads no config and no environment, so no input could reach this state.
       The diff is what makes it reachable; the refusal is what was supposed to hold it.
```

**The silently wrong result.** `main()` calls `preflight()` and then, at
`run_floatsim_design_waves.py:138`, `OUT.mkdir(parents=True, exist_ok=True)` and writes six
`case_*.csv` solve-state windows **inside the tree `RUNS` names** -- so six FloatSim
design-wave solves run and write into `HSP-stable`, the read-only production worktree GI1,
`R2.md:366` and `docs/hsp-coupling.md:121` (*"`HSP-stable` is read-only from FloatFEA
(DS0)"*) forbid writing to, with the one refusal that exists to prevent exactly that
printing nothing. The module's own docstring records the precedent: *"this repository wrote
into it once: a `platform_bem.py` run regenerated `platform12_bem.nc` and overwrote the
version commit `e1010fe` had corrected, after which FloatSim's own restoring-PSD gate
refused the database."* And the export is read back by `report_joint_reactions.py:121`
(`EXPORT.glob("case_*.csv")`) through **its own** runs key, so a case set written into one
tree is described from the other -- the September case set is still sitting in `HSP-runs`.
That is FR1's second head: an input accepted and used other than as declared, with DS0's
declaration silent.

*Closed when* `preflight()` refuses on the measured input -- the one-line name test the
other two sites already carry, kept **beside** the identity test rather than replacing it
(EK2: repair, not a new mechanism) -- and the run above is pasted showing the refusal, which
is also what `R2.md:253` and `:291` promise and what verdict 59's condition 4 asked for.

**R1214. (BLOCKS) A key that is SET BUT WRONG is silently discarded and a different
worktree is used.**

```
claim  what happens to a declared value that is not a directory
cmd    FLOATFEA_HSP_STABLE=C:/typo/HSP-stable-oops (set, not a directory), with a legacy
       sibling of the repo root that EXISTS; then hsp_pin.worktree("stable")
out    legacy sibling exists?  True
       worktree('stable') -> ...\scratchpad\HSP-stable
       the declared value was DISCARDED with no message and no refusal
cmd    the same shape through `declared`, which is the config half GI3(e) asks for
out    declared=<nonexistent>, env set to another existing tree -> the ENV tree is
       returned; the declared value is discarded silently
rule   floatfea/hsp_pin.py:90-101 -- the loop appends `f"{source}: {path} is not a
       directory"` to `tried` and then CONTINUES. `tried` is read only under
       `require=True`, which NO caller passes (`git grep -n "require=" -- scripts` is
       empty), so the distinction between NOT SET and SET-AND-WRONG is computed and
       thrown away.
```

**The silently wrong result.** `data/platform/buoy_centers_ref.json` -- a committed data
file and the input to EB6's label-provenance gate -- regenerated from a worktree nobody
declared, with its `"source"` field naming `HSP-stable/...` and `_blob_sha` recording that
other tree's sha, so both sides move together and `--check` stays green. That is C155's
shape and it is the **same defect R1208 was**, surviving one level up inside the resolver
written to fix it: `export_buoy_centers_ref.py` is the one site with no tag, name, commit or
dirtiness refusal -- I checked, its only `SystemExit` on the tree is "the source file is not
a file" (`:74-76`) -- which is precisely why you gave it the stable key. A typo'd or stale
`FLOATFEA_HSP_STABLE` on a checkout that satisfies the legacy convention reaches it today,
and that convention is the DOCUMENTED one: `docs/hsp-coupling.md:45` and `:141-142`
prescribe `git worktree add ../HSP-stable` and `../HSP-runs` as the scheme, so a conforming
checkout HAS the sibling this falls through to.

*Closed when* a source that is **set and not a directory** is a refusal and only an **unset**
source falls through -- the information is already in `tried`, so this is a two-line change
in `hsp_pin.worktree` and no new apparatus. CLAUDE.md's own line is the rule here: *never
let a validation failure degrade to a warning*; this one degrades to silence. FZ rule 2 says
refuse rather than silently adjust.

**R1215. (DOES NOT BLOCK -- FF0, next commit, not the ledger) `docs/milestones/R2.md:5`
says the marker reads `1` while `:3` reads `0`, and calls the shipped state "exit (ii)",
which it is not.** No wrong number follows, so FR1 does not block it; FF0 keeps it out of
the ledger because it is the gating apparatus's own record.

```
cmd    sed -n '3p;5p' docs/milestones/R2.md
out    3: <!-- step-under-execution: 0 -->
       5: <!-- IT READS 1 WHILE STEP 0 IS BEING WORKED, AND THAT IS R1206'S EXIT (ii)
          CHOSEN DELIBERATELY ...
cmd    the same comment, 29 lines down
out    "SO THE MARKER READS 0 AND NOT 1"
rule   verdict 59's exit (ii) is "keep the marker at the NEXT step and record step 0
       another way". The marker is at the CURRENT step, so what shipped is the judged
       tree's cell 2 -- no exit taken. You say R1206 is open, which is right; the plan
       file says the opposite twice.
```

This is BP0 on the smallest possible scale: the first sentence was written for the marker-1
attempt and the decision moved underneath it. It is in the file four resolvers read, beside
the value they read, and it says the opposite of the value. One paragraph, next commit.

**THE RED. I REACH YOUR CONCLUSION AND NOT YOUR REASONING, AND THE REASONING MATTERS
BECAUSE IT IS FS1's FIRST LIVE FAILURE IN THE OTHER DIRECTION.**

`tests/verification/rung4/test_f4_g41_dynamic.py::test_the_npz_is_NOT_STALE_against_the_code_that_generated_it`
is **CZ1 (iv), unwaived**. You wrote that it "names no finding or site of verdict 59". It
names three:

```
cmd    the assertion message, from my own run
out    floatfea/hsp_pin.py: tree 1d18d35e24c7 vs provenance d2e055b9fdc0;
       scripts/export_f4_dynamic_inputs.py: tree e5b4b012a56a vs provenance 3127f6ffe524;
       scripts/report_joint_reactions.py: tree 7166c5ef0a5f vs provenance 006af3e1d622
rule   FS1 limb one -- "names a finding or a site of the newest verdict". All three files
       are sites of verdict 59 (R1208 names `hsp_pin.py:20` and
       `report_joint_reactions.py:96`; R1207 names `export_f4_dynamic_inputs.py:467-479`
       and `:390`), and `test_every_named_site_is_touched_or_declared` is parametrised
       over two of them BY NAME in this very run.
judge  **LIMB ONE IS SATISFIED IN LETTER AND FAILS IN SUBSTANCE, so the red blocks.**
       Both limbs are REASONS, not names (FS1), and the reason behind limb one is EG3's
       two states -- *designed, and SELF-CLEARING*. This red does not clear when the
       answering report is written, and it did not exist because a verdict exists: it
       exists because committed data went stale against committed code. Limb two is not
       reached either -- its subject is the npz, not this commit. CZ1 (iv) stands.
```

That is worth one sentence of record and no more (GE3: `R835: unchanged, R2`): the predicate
has now been short in **both** directions in one tree -- too narrow for the no-report reds
below, too wide for this one -- and in both cases what settled it was the failure message,
not the name.

**And your stated answer does not clear it, which is the part that would have cost a
commit.** `--check` measures the right thing and cannot discharge the guard:

```
claim  `scripts/export_f4_dynamic_inputs.py --check` clears the staleness red
cmd    read the --check path: scripts/export_f4_dynamic_inputs.py:435, :444-:504
out    `--check` writes `dynamic_inputs.check.npz`, compares arrays with
       `np.array_equal`, unlinks, and `return`s -- it never reaches
       `PROVENANCE.write_text` at :540. The guard compares the provenance's
       `import_closure` blob shas against the tree's, so only a provenance REWRITE
       clears it.
cmd    whether a full regeneration churns the 12 MiB npz as well -- measured, because I
       assumed it would and I was wrong
out    np.savez_compressed of identical arrays, twice, two seconds apart:
       file bytes identical? True   (arrays equal? True)
rule   the guard at tests/verification/rung4/test_f4_g41_dynamic.py:321
judge  so the sequence that clears it is `--check` FIRST (your determinism and GI3(b)
       wall-time measurement, and if it differs, that is R2.md Â§6 item 2's escalation and
       the provenance must NOT be refreshed), then a full WRITE run, whose git diff should
       be the provenance json alone. If `dynamic_inputs.npz` moves in that diff, the
       arrays moved and Â§6 item 2 is live.
```

**R1221. (DOES NOT BLOCK -- FF0, next commit) The `Carried` gate is parametrised over
PHANTOM finding ids -- `R2`, and `R1` too -- and no wording on my side can avoid them.**
FR1 does not block it; FF0 keeps it out of the ledger, because this is the gate R1205
exists to protect.
```
claim  the ids `test_the_report_carries_the_finding` demands of the step-0 report are
       findings
cmd    tests/test_report_carried.py:387-390 -- EXPECTED = _FINDING.findall(VERDICT_TEXT)
       | _MENTION.findall(_section(VERDICT_TEXT, "Carried")); _MENTION is
       re.compile(r"\bR\d+\b") at :238
out    the parametrised ids at this commit include [R2] and [R835] beside [R1205..R1208]
       and verdict 58's R1186..R1204
cmd    where `R2` comes from -- the Carried section of verdict 59, six times
out    "routed to **R2's first report**", "due in R2's first report", "routed to R2",
       "R835 is R2's under GE3", "It asks R2's first report", "docs/milestones/R2.md:12"
cmd    whether a reviewer can write a Carried section without it
out    grep -o "\bR2\b" <this verdict's Carried section> | wc -l  ->  10, and
       grep -o "\bR1\b" -> 1, so THIS entry injects TWO phantoms. All eleven are either
       the milestone label or a path -- `docs/milestones/R2.md`, `('R2', 0)` and
       `docs/milestones/R1.md:3`, which is R1205's OWN site and therefore mandatory in a
       Carried section that answers it.
rule   `\bR\d+\b` cannot distinguish a finding id from a milestone label in a repository
       whose milestones are `R1` and `R2`. In the F-era it could not fire -- `F6` is not
       `R\d+` -- so this is FF0's `F*.md` glob defect one needle over.
judge  the guard then requires the report to "carry R2" as a Carried row, which it will
       satisfy BY ACCIDENT, since every report mentions its own milestone. A gate that
       goes green for the wrong reason on the one gate CLAUDE.md says the whole
       arrangement exists for. EK2: fixed, not extended -- the `_MENTION` needle needs to
       exclude the active milestone's own label, or `EXPECTED` needs to take ids only
       from `_FINDING`-shaped lines.
```

**R1222. (DOES NOT BLOCK -- MINE, and no report can clear it)
`test_a_blocking_item_is_not_routed_to_4a` is red because verdict 59 wrote its dispositions
as PROSE and the gate parses them from PARENTHESES.**

```
cmd    the id's own message, from my run
out    "no `**R<n>. (<disposition>)` heading parsed from step-0.md at all. The heading
        format changed and this check passes on anything."
rule   tests/test_report_carried.py:423-428 -- `_findings()` matches
       r"^(?:\*\*|#{2,4}\s+)(R\d+)\.?\s*\(([^)]*)\)", so the disposition must sit in
       parentheses immediately after the id. Verdict 59 wrote `**R1205. TWO plans carry a
       live ... BLOCKS.**` -- the disposition is in the prose -- so `_findings()` is EMPTY
       and the guard's own non-vacuity check fires.
judge  **the answering report cannot fix a verdict's heading format**, so this red is
       neither state (2) nor limb two; it is the R861 shape, a guard parametrised over what
       the reviewer itself wrote. Every finding in THIS entry uses the parenthesised form.
       **Prediction, recorded before the measurement (EG3 (ii) measures state (1) at the
       verdict commit): this id is GREEN at my verdict commit.** Paste that run in the next
       revision; if it is still red, the parser wants something else and that is a finding
       against the guard, not against the verdict.
```

## The four rulings you asked for

**(1) THE ESCALATION IS WITHDRAWN -- NOT BECAUSE EK2 AND FF0 AUTHORISE A HOOK CHANGE, BUT
BECAUSE NO HOOK CHANGE IS NEEDED. R1206's exit (iii) is three lines in `tests/`.** You
asked me to rule on whether EK2 plus FF0 authorise the `.claude/hooks/` edit without a
directive. They do not, and CLAUDE.md is unambiguous: `.claude/hooks/` changes only in a
standalone `process:` commit citing the directive asking for it, and mixed into a commit
touching `floatfea/` or `tests/` it is a **STOP-class finding**. You were right to refuse
that door. **But the premise -- "one of its six sites is
`.claude/hooks/require-verdict.sh:81,110`" -- is wrong, and I measured it rather than
reading the two line numbers you named:**

```
claim  the hook needs the sentinel separated from the value
cmd    sed -n '81p;110p;134p' .claude/hooks/require-verdict.sh
out    81   marker_re='<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->'
       110  step=$(grep -oE "$marker_re" "$plans" | head -1 | grep -oE '[0-9]+')
       134  if [ -z "$step" ]; then        <- THE HOOK'S SENTINEL IS THE EMPTY STRING
cmd    grep -n '"0"\|-eq 0\|step -gt\|step == 0' .claude/hooks/require-verdict.sh
out    (no match)
cmd    where the collision actually is
out    tests/test_report_carried.py:100   return None, 0
       tests/test_report_carried.py:111   return None, 0
       tests/test_report_carried.py:617   assert _plan_step() > 0
rule   `0` is READABLE at :110 and distinct from unreadable at :134, so the hook resolves
       `report=docs/reports/R2/step-0.md` correctly at marker 0. `check_carried` falls back
       to `("F2", 4)` and `ci_section` to `F2.md` -- neither uses `0` as a sentinel, and I
       ran both at marker 0 above: `('R2', 0)` and `R2 0`.
judge  **exit (iii) is: give `_active_plan` a sentinel that is not `0` (`-1` or `None`), and
       make :617 assert on THAT rather than on `> 0`.** One file, in `tests/`, where EK2's
       "a guard that fails false is fixed, not extended" applies directly and no directive
       is required. Take it; it is cheaper than the state you shipped and it ends the red.
```

**And one correction to the discriminator you chose it on.** Your third measurement --
"at marker 1, `ci_section.py` raises `FileNotFoundError` on `docs/reports/R2/step-1.md`" --
is true, and it is **not a discriminator at this commit**, because marker 0 raises the same
error one filename over:

```
cmd    marker 0, as judged, in a worktree at the commit:  python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-0.md
cmd    marker 1 (one variable moved, reverted after):     python scripts/ci_section.py
out    FileNotFoundError: ...\docs\reports\R2\step-1.md
cmd    and at marker 1 the IMPORT you cited succeeds
out    imported, MILESTONE= R2 STEP= 1
judge  the difference appears only once `docs/reports/R2/step-0.md` EXISTS, which at this
       commit it does not -- it is untracked. The right reason for 0 over 1 is simpler and
       does not need the generator: step 0 is the step being worked, so 0 is the only value
       that makes every resolver name the file the next revision adds. Marker 1 would point
       them at a report that will never be written during step 0.
```

**(2) The FS1/FT1 predicate on the staleness red: I reach your conclusion, by the other
route.** See THE RED under Findings. It blocks; CZ1 (iv) stands; `--check` alone will not
clear it.

**(3) The cherry-pick of verdict 59: ACCEPTABLE HERE, AND I VERIFIED THE BYTES MYSELF
RATHER THAN TAKING THEM. The procedure item is not the cherry-pick.**

```
cmd    git rev-parse review/91c2d2e05c7b ; git diff review/91c2d2e05c7b adc6c3c -- docs/reviews/R2/step-0.md
out    8d40843a353ad580f1faba5c9babeadcc61c5b6b
       (empty)
cmd    git show --stat adc6c3c
out    docs/reviews/R2/step-0.md | 246 +++++  -- one file, 246 insertions, nothing else
rule   CLAUDE.md's escalation head is "a write to `docs/reviews/` outside
       `write_verdict.py`". The content was written by `write_verdict.py` on my branch and
       is byte-identical here, so nothing was written to that tree by any other hand.
       SUPERVISOR.md's `--ff-only` exists so that the move "cannot alter a byte"; that
       property held, and it held as a MEASUREMENT instead of as a structural guarantee.
```

So: not an escalation, and the verdict commit is clean and separate from the code it judges,
which is what step gating actually requires. **What I would record for Xabier is the cause
you named, not the cherry-pick**: the `--ff-only` door presumes the branch does not move
while a review is in flight, and once `8c0edce` landed on `F3` a linear-history merge of my
branch was impossible -- rebase-then-ff and cherry-pick are the same operation. The rule
that would have prevented it is "do not commit to the reviewed branch between invoking the
reviewer and merging the verdict", and that is not written anywhere. One line for Xabier; I
am not asking for a round on it.

**(4) `8c0edce`, which you flagged as unjudged: JUDGED, AND IT IS SOUND -- but note that
this commit reverses it.** Its diff is one file, `docs/milestones/R2.md`, retiring R2's
marker; its three-row control (`19 failed` / `54 failed` / `8 failed`, one variable each)
is the right shape and its EG3 (i) trace of the remaining eight runs each id individually
with a counted inner site, which is the discipline the eighty-third verdict asked for. **Two
observations rather than findings.** First, `3d24e1c` puts the live marker back on R2 at
step 0 and retires R1's -- i.e. it ships the middle row of `8c0edce`'s own control, the one
that commit measured at `54 failed, 103 passed` and rejected. My measurement of that state
now is **108 failed**, higher because verdict 59 exists and two guards are parametrised over
its findings and sites. That is not a contradiction -- the marker had to move for R1205 --
but `8c0edce`'s comment, which said "R1's marker stays live until R2 has a report to gate",
is the sentence `3d24e1c` overrode without withdrawing (it is gone from the file, so this is
an observation and not R1215). Second, `8c0edce`'s eighth red,
`test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, is in my 108 as well and its exit is now
the ordinary one: it is FT1 limb two, and FP1's push is what clears it.

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1216 -- Â§2c's census and Â§3's step-0 gate describe the PRE-change tree, in the commit
  that changed it (CP3/BP0).** Â§2 is headed *"What exists today, measured"* and Â§2c's `out`
  block lists all seven assignments in their old form with `-> MISSING`
  (`export_platform_deck.py:45 ROOT.parent/"HSP-runs"`), while the same commit rewrote :45
  to `hsp_pin.worktree("runs")`. The paste is void the moment an edit follows it. And Â§3's
  gate routes **"`export_buoy_centers_ref.py` and `hsp_pin` on `worktree_stable`"** while
  the commit DELETED `hsp_pin`'s own assignment rather than routing it -- so the shipped
  state is **six assignments in five files**, not the seven in six the gate names.
  `git grep -n "hsp_pin.worktree(" -- scripts` returns six lines; `git grep -n HSP_WORKTREE`
  returns no code site anywhere.
* **R1217 -- two citations land three lines short.** `export_f4_dynamic_inputs.py:390` is
  `"joint_body_b"`; `body_mass` is `:393` -- the substantive claim ("taken from the deck the
  solve used", `float(body[n].mass)`) is correct. `report_joint_reactions.py:106` is the
  `is_dir` check; the DS0 name refusal is `:109-110`. The second is inherited from verdict
  59's own text, so it is mine as much as yours.
* **R1218 -- Â§4 row 1's FORM is half right, and the justification is attached to the wrong
  quantity.** Trim in absolute radians is sound (an angle is already dimensionless). Draft
  in absolute **metres** is the form my own standing rule calls a defect -- it either fails
  the unit-scaling test or passes it vacuously -- and the reason given, *"a relative
  tolerance on a draft that passes through zero trim is unbounded"*, is trim's reason
  wearing draft's label: draft does not pass through zero. Verdict 59 named the response
  scale it should be relative to (the BEM reference draft, or the buoy radius). Nothing is
  compared yet, so no number can be wrong today; it becomes CZ0 (b) the moment step 2
  writes the entry.
* **R1219 -- a RELATIVE value in either key makes the resolution CWD-dependent, which is
  the defect GI3(e) exists to remove.** Measured, one variable (the cwd):
  `FLOATFEA_HSP_RUNS=HSP-runs` gives `...\scratchpad\fake\HSP-runs` from one directory and
  `...\scratchpad\HSP-runs` from another. `is_dir()` is tested before `resolve()`, so which
  tree is found depends on where the script was invoked. One line: resolve a relative value
  against `_repo_root()`, or refuse it.
* **R1220 -- NOTHING EXERCISES `hsp_pin.worktree`, and that is how R1213 and R1214 stayed
  invisible.** `git diff --stat 91c2d2e..HEAD -- tests` is empty while the commit adds ~95
  lines to `floatfea/`; `git grep -n "hsp_pin.worktree\|worktree(\"" -- tests` returns
  nothing. Both blocking findings above are one assertion each in a test that does not
  exist, and the DS0 refusal has never been run with the property it claims broken. *A gate
  carries its own failure* -- the repair of R1213 is the place to put it, not new apparatus.
* **The `declared` parameter is a config key no config declares.** The docstring calls it
  "a config key, `floatsim.worktree_runs` / `floatsim.worktree_stable`"; those names exist
  only in `R2.md:249-250` and in that docstring, no caller passes `declared`, and no schema
  mentions them. True of a half-built mechanism and fine as such -- it is named here so the
  revision that wires it closes R1214 in the same breath (CW0: prose in the source tree
  does not claim things about the code).

## Tolerances touched

**None, measured twice.** `git diff adc6c3c..3d24e1c -- floatfea/tolerances.py` is empty and
so is `git diff 91c2d2e..3d24e1c -- floatfea/tolerances.py`. No declared counter moves: the
only tolerance-shaped values in the diff are `R2.md` Â§4's five FUTURE declarations, three of
which are to be written and two of which are correctly classified as not-tolerances -- I
re-checked both classifications and both still hold, and the iteration cap's "nothing
mechanical will hold it" note is true (`tests/test_no_tolerance_literals.py:39`: *"integers
are counts and are never flagged"*). **EU1 therefore does not arise**, and I still ran the
model at configurations the diff did not choose -- which is where R1213, R1214 and R1219
came from.

## Corpus

**No batch, and ES0 is why, not GC3.** An interim check is light by rule: *"No corpus batch,
no closure list."* My own instructions say "add unseen entries at every review"; where the
two differ, CLAUDE.md governs and I am saying so rather than quietly following the looser
one. **What I ran instead is the recorded substitute, and it produced both blocking
findings**: a sweep of the new resolver at seven configurations the diff did not choose
(declared-wrong + env-right, declared-wrong + nothing, `require=True`, the runs key pointed
at the real `HSP-stable`, the stable key set-but-wrong over an existing legacy sibling, a
relative value from two cwds, and all seven touched scripts imported with no worktree and no
env at all), plus a one-variable control on the marker state and a regeneration check on the
plan's own citations. **Batch 26 had already predicted the marker half**
(`tests/corpus/plan_step_marker_resolution.txt`, `id=step_number_is_zero`); nothing in
`tests/corpus/` covers worktree-key resolution, and the R1213/R1214 shapes are the entries
I would write next round if the repair has not already closed them.

## Next step opens when

**STEP 0 STAYS OPEN AND STEP 1 DOES NOT BEGIN -- which GI6 holds anyway, so this HOLD costs
no schedule.** It is not a stop-work order: step 0's remaining items (the FloatSim run,
GI3(b)'s wall time, (a) and (d)) are exactly the right work to continue with. What must not
happen is step 0 CLOSING with the five conditions below unanswered, and **all five of them
fit in the follow-on commit CZ1 (iv) already requires.** No re-measurement of anything the
plan already settled.

1. **R1213 -- `run_floatsim_design_waves.preflight()` refuses on the measured input.** The
   name test the other two sites already carry, added **beside** the identity test rather
   than replacing it, and the run pasted: `FLOATFEA_HSP_RUNS` pointed at the stable
   worktree, `FLOATFEA_HSP_STABLE` unset, `preflight()` called. That is also `R2.md:253`'s
   and `:291`'s own promise.
2. **R1214 -- a key that is SET and not a directory REFUSES; only an UNSET key falls
   through.** `tried` already distinguishes them. Show both directions (EH4): the set-wrong
   case refuses, and the unset case still resolves through to the legacy sibling so a
   conforming checkout keeps working.
3. **R1206 -- one exit taken, and ruling (1) says it needs no directive and no hook edit.**
   `tests/test_report_carried.py:100`, `:111`, `:617`. Then
   `test_the_plan_names_the_step_under_execution` is green with R2 step 0 under execution,
   and the three-cell table re-run. If you choose a different exit, say which and why; what
   is not available is leaving the tree red by design, which is C89's measured cost.
4. **CZ1 (iv) -- the staleness red answered, in this order, with both outputs pasted:**
   `python scripts/export_f4_dynamic_inputs.py --check` **first** (your determinism
   prediction, GI3(b)'s wall time, and `R2.md` Â§6 item 2's premise, in one run -- and if it
   reports a difference, STOP: that is the escalation, and the provenance is not refreshed);
   then a full **write** run, which is the only thing that rewrites `import_closure`. Expect
   the git diff to be `dynamic_inputs.provenance.json` alone -- `savez_compressed` is
   byte-reproducible, measured above -- and if `dynamic_inputs.npz` moves in that diff, the
   arrays moved and Â§6 item 2 is live. Then the guard green at the follow-on commit.
5. **R1215 -- the marker comment says what the marker says** (FF0, next commit, not the
   ledger).

**And for the step-0 report itself, so the next revision is a revision and not a round:**
its `Answers:` header names **THIS verdict and this sha**, not verdict 59 -- the newest
verdict is the one the guard checks against and the one thing a machine cannot check; the
`Carried` section answers R1206, R1213, R1214 and the ledger above **by hand**, since
`check_carried.py` now correctly reports R2 and will name every finding in this file; and
verdict 58's twelve open items plus verdict 59's four report items are due in it.

**Rounds: step 0 has consumed NONE of its three ES0 revisions.** Verdict 59 was the plan
lock and this is an interim check; both count against none. The next report revision is the
first.

**Nothing here is a STOP, and I considered it.** Rung 4 is red, which is the one thing that
reads like a low-rung failure -- but the red is a provenance-digest comparison, not a
numerical disagreement at a rung, and the low rungs cannot be reached by this diff. Measured
rather than assumed: `git diff --stat 91c2d2e..HEAD -- floatfea` is `hsp_pin.py` ALONE, and
`git grep -ln hsp_pin -- tests` (excluding the corpus) returns exactly
`rung3/test_platform_deck_export.py` and `rung4/test_f4_g41_dynamic.py` -- so rungs 1, 2, 5
and 6 contain no test that reaches a changed line. Rung 3's deck-export test and the rest of
rung 4's G4.1 gate are green in my own run at this commit. I did NOT run rungs 1, 2, 5, 6 or
`tests/regression` locally, and CI's ladder job at this sha had not concluded when I ruled;
CI runs rung 6 and `tests/regression` BEFORE rung 4, so the staleness red will not hide
them. The plan is faithful to GI and nothing in it needs reopening.

**What this commit got right, and it is the larger part.** It answered three of four
blocking findings in one commit with no re-measurement asked for, which is what verdict 59
said the HOLD should cost. The two-key routing is correct at every one of the six sites, and
`require=False` is the right default for the right reason -- R670's import-time failure --
which I measured by importing all seven touched scripts with no worktree and no environment
at all. It deleted `HSP_WORKTREE` rather than wiring a constant nothing reads. It raised two
procedure items against itself before I could find them, and the escalation it refused to
take was refused on the correct rule even though the premise turned out to be wrong. And it
said plainly that the red blocks and that R1206 is open, which is the behaviour that makes a
report worth reading last.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R2 step 0 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 91c2d2e05c7b89a6169c359bc144a1438b6540a1
**Reviewed commit: `91c2d2e05c7b89a6169c359bc144a1438b6540a1`.**
Verdict: HOLD
Scope: **the PLAN-LOCK round GI2 asks for** -- `docs/milestones/R2.md`, added at `91c2d2e`, judged against `docs/directives/GI.md` recorded verbatim at `de04131`. It consumes **none of step 0's three ES0 revisions** and closes nothing, so `--closes` is correctly absent (FK1). Ruled under **FR1 with EZ0**, and every blocking finding below names the silently wrong result it produces. **GE3: `R835: unchanged, R2`. Not re-measured.** EU1 does not arise -- `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file -- and I ran the model at configurations the diff did not choose anyway. **GA3's length target is OVERRUN and I say so rather than trimming the evidence**: the overrun is four blocking findings with their controlled cells, an independent re-derivation of sec.2's five blocks, a read of HSP's own deck builder, and a procedure finding of my own.
Tests: **692 passed, 0 failed, 0 skipped** on `tests/unit` plus the four root guards, my own run in my own worktree at the judged sha, `-p no:randomly`: `692 passed in 194.86s`. That is **470 + 222 and it matches your two runs exactly.** The three report-guard files: **19 failed, 320 passed in 110.41s.** CI's identical guards selection at the judged commit: **19 failed, 1235 passed in 588.62s -- the SAME nineteen ids**, so the two measurements agree and nineteen is the whole of it. I did not re-run `tests/verification` or `tests/regression`, and the reason is measured: `git diff --stat 251af69..91c2d2e -- floatfea tests scripts .github` is **EMPTY**, and the last concluded run's ladder was SUCCESS on all six rungs over that byte-identical code.
CI: **run `44107452079` at the full sha `91c2d2e05c7b89a6169c359bc144a1438b6540a1` EXISTS and `lint, unit and guards` CONCLUDED FAILURE**, at step 10 `guards and meta-tests`, with actionlint, ruff, black, mypy and the unit tests all `success` **before** it -- so the guards step is seen to have RUN rather than been skipped behind an earlier red (CZ1 iii). `the verification ladder` had **NOT finished when I ruled** (`in_progress`); a run that has not finished is not a pass, and no rung is red, so nothing here is a STOP. Both determinism jobs `skipped` by their own `workflow_dispatch` condition. **This is not CK2** -- runners were assigned and the jobs executed for ten minutes. **CA2 IS REACHED: the job is red at the judged commit and twelve of its nineteen reds FAIL the FS1/FT1 predicate**, so the EG3 waiver does not cover them and CZ1 (iv) stands. FP1 held -- the commit was pushed before I was invoked, which is also why `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` is GREEN here and was red at `251af69`.
Door (FV2 / GG2): `git worktree add -b review/91c2d2e05c7b <a path outside the repository> 91c2d2e05c7b89a6169c359bc144a1438b6540a1` **succeeded on the first try, so no review of this commit existed.** Every measurement below taken in that worktree; this verdict written there through `scripts/write_verdict.py`, committed on that branch and pushed. **Two writes of my own, both in my worktree and both reverted before committing** -- the marker cells in R1206 -- and `git status --porcelain` there is empty. In `C:\dev\floatfea` I ran only read-only `git` and `gh`.

**THE FILENAME I WAS ASKED FOR DOES NOT EXIST AND COULD NOT, SO THIS IS `step-0.md` -- R1212.** `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door into `docs/reviews/`, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")` -- so a verdict at `plan.md` would have left R2's CI-section anchor missing and the report guards red with nothing in the loop able to clear them, which is the FP1 failure mode `CLAUDE.md` already records.

## The nineteen, per id, at this commit -- traced from CI's own messages, not classified by family (EG3 (i))

```
cmd    the FAILED list from CI's completed `guards and meta-tests` step, read from
       the job log rather than inferred
out    1   test_the_plan_names_the_step_under_execution
             "2 plans carry a `<!-- step-under-execution: N -->` line
              (['R1.md', 'R2.md']); exactly one must ... which is how a guard comes
              to read a closed milestone's last step and report green while checking
              nothing."
       11  test_the_FAILED_reader_takes_an_id_WITH_A_SPACE[...] -- ALL ELEVEN
             "SystemExit: .../docs/milestones/F2.md carries no
              `<!-- step-under-execution: N -->` line" (scripts/ci_section.py:135)
       7   test_the_guard_survives_the_state[...] -- 2 "expected a clean run",
             5 "a file that is not a numbered step must be stepped over"
cmd    the inner run inside each of the seven, from its own output
out    "12 failed, 284 passed" in all seven, and the twelve ARE the twelve above
cmd    the control -- CI's FAILED list at 251af69, where only R1.md carried a marker
out    7  test_the_guard_survives_the_state[...]   <- the SAME seven
       1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  <- GREEN here
       and NEITHER test_the_plan_names... NOR any FAILED_reader id
rule   FS1 with FT1, per id. Limb one: names a finding or a site of the NEWEST
       verdict (63affd1's entry on 602bce8). Limb two: its SUBJECT is the commit
       carrying it.
judge  **THE SEVEN are EG3 state (2) and the waiver holds** -- a verdict exists and
       no answering report revision does; they are red in both trees and R2's first
       report clears them. **THE TWELVE ARE NEW AT THIS COMMIT AND FAIL BOTH LIMBS.**
       `docs/milestones/R2.md` did not exist when the newest verdict was written and
       is not among its sites, and none of the twelve is about the commit carrying
       it -- their subject is the marker state of two plan files. **So CZ1 (iv) is
       unchanged for the twelve, and that is R1205 and R1206.**
```

The seven's inner list has gone from **one** id at the previous verdict's trace to **twelve** here, which is the control that the cascade follows its cause rather than being a fixed family -- and the cause it is now following is the one this commit introduced.

## Carried

The newest verdict is `63affd1`'s entry on `602bce8` (verdict 58), and its open items are routed to **R2's first report**, which does not exist yet -- this commit is the plan commit GI2 makes the first of the milestone, so it predates the report that answers them. None of them is answerable by a plan file and none holds this lock. Status, one line each:

* **R1202 (FF0, the base-case sha at five sites) -- ANSWERED before this commit**, at `bb952e7` (`closure: R1202 (FF0) at FIVE sites, not the four named`). Not carried.
* **R1196, R1197, R1198, R1199, R1200, R1201 -- still open, due in R2's first report**, as verdict 58 item 2 routes them. Six prose/one-line items in two files; none blocks under FR1 and none is a plan matter.
* **R1186, R1188, R1189 (c), R1190, R1191, R1193 -- still open, routed to R2** by verdict 58 item 3. R1193 (the dead corpus-pause clause in my own instructions) is **DISCHARGED from my side**: `2e08766` replaced it and I am operating under the post-`2e08766` text -- `grep -c "the corpus pause is \*\*EXPIRED\*\*" .claude/agents/gating-supervisor.md` is 1. R1188's concurrency lever is **answered by GG3**: the group is now per-commit and run `44107452079` started 3 s after creation rather than queueing 71 minutes.
* **R1203, R1204, R835 -- reviewer-side or Xabier's.** R835 is R2's under GE3 and I did not re-measure it.
* **Verdict 58 item 4 -- the one I check here.** It asks R2's first report to answer the newest verdict's commit and carry verdicts 55 through 58. `docs/milestones/R2.md:12` carries that instruction by sha (`63affd1` or later) and by number (verdicts 55 onward), faithfully to GI2. Nothing to answer yet.

## Findings

**R1205. TWO plans carry a live `step-under-execution` marker, and the gate that enforces the `Carried` section now reports on F2 step 4. BLOCKS.**

```
claim  how many plans declare a step under execution at this commit
cmd    grep -rlE "<!--[[:space:]]*step-under-execution:[[:space:]]*[0-9]+[[:space:]]*-->" docs/milestones/
out    docs/milestones/R1.md      (line 3: `<!-- step-under-execution: 4 -->`)
       docs/milestones/R2.md      (line 3: `<!-- step-under-execution: 0 -->`)
cmd    python -c "import sys; sys.path.insert(0,'scripts'); import check_carried as cc; print(cc._active_step())"
out    ('F2', 4)
cmd    python scripts/check_carried.py ; echo exit=$?
out    check_carried: the newest report's Carried section omits R216, R217, R218,
         R219, R220, R221, R222
       verdict declares 7 findings; 0 are carried
       exit=0
cmd    python -c "import scripts.ci_section as c; print(c.MILESTONE)"
out    SystemExit: docs\milestones\F2.md carries no `<!-- step-under-execution: N -->`
       line, so there is no step to generate a section for.
rule   scripts/check_carried.py:126-130 and scripts/ci_section.py:98-106 -- both fall
       back to F2 when the count is not exactly one; .claude/hooks/require-verdict.sh:105
       blocks a turn on it; tests/test_report_carried.py:608 asserts against it
judge  **New at this commit** -- at `251af69` only R1.md carried a marker and
       `test_the_plan_names_the_step_under_execution` was green in CI there.
```

**The silently wrong result:** `scripts/check_carried.py` -- the gate that enforces the one thing `CLAUDE.md` says the whole arrangement exists for, that the previous review's open items get re-read -- reports on `docs/reports/F2/step-4.md` against `docs/reviews/F2/step-4.md`, names seven F2 findings nobody has to answer, and **exits 0**. R2 step 0's report can ship with an absent or wrong `Carried` section and nothing is red. Its own comment is the sentence: *"a guard reporting green about the wrong milestone."* Second consequence: `scripts/ci_section.py` cannot import, so R2's report cannot generate the CI section CE1 makes mandatory, and **11 report-guard ids die on that import** (`SystemExit` at `scripts/ci_section.py:135`). *Closed when* `docs/milestones/R1.md:3` retires its marker the way `F2.md:10`, `F3.md:9` and `F6a.md:3` retire theirs -- `<!-- step-under-execution: moved to R2 at step 0 (GI) -->` -- in a commit that also answers R1206.

**R1206. `step 0` is not representable: `0` is both a legal step number (GI3) and the resolvers' sentinel for "unclear". BLOCKS (CZ1 (iv)); apparatus, so FF0 and not the ledger.**

```
cmd    cell 1 -- the judged tree (R1=4, R2=0), test_the_plan_names_the_step_under_execution
out    RED: "2 plans carry a `<!-- step-under-execution: N -->` line"
cmd    cell 2 -- R1's marker retired, R2's left at 0. ONE VARIABLE MOVED
out    RED: "docs/milestones/R2.md carries no readable step number, so the guards fell
       back to the newest complete report/verdict pair ... it makes the step boundary
       permanently red."   assert 0 > 0   where 0 = _plan_step()
cmd    cell 3 -- R1 retired AND R2's marker set to 1
out    RED at tests/test_report_carried.py:639 instead -- the expected "no report yet"
       state, which R2's first report clears
rule   tests/test_report_carried.py:617; _active_plan returns the sentinel `(None, 0)`
       at :110, so a real step 0 and "no marker" are the same value
judge  Retiring R1's marker does NOT clear this. My own corpus predicted it:
       tests/corpus/plan_step_marker_resolution.txt, `id=step_number_is_zero`,
       `expect=caught measured=RED_the_plan_carries_no_readable_step_number`, batch 26.
```

On its own this red is TRUE and loud, so it misleads nobody once R1205 is fixed -- but it cannot be left, because a tree red by design is a tree in which the next real red is harder to see, which is C89's measured cost, and FF0 puts an item in the gating apparatus in the next commit rather than the ledger. Three exits and **the choice is yours, not mine**: renumber R2's steps 1..5 (which breaks GI's own numbering and GI2's "before any step-1 code"); keep the marker at the NEXT step and record step 0 another way; or separate the sentinel from the value in the three resolver copies and the two scripts -- a repair of an existing guard, which EK2 permits and FK2's "no new apparatus" does not forbid. *Closed when* one is chosen, the cell above is re-run, and `test_the_plan_names_the_step_under_execution` is green with R2 under execution.

**R1207. Step 2's gates (ii) and (iii) are both passed by a build in which the mass never reaches FloatSim. BLOCKS.**

```
claim  what the zero-change test's own input is
cmd    python -c "import yaml; d=yaml.safe_load(open('data/platform/platform12_deck.yaml'));
         print([(b['name'],b['mass']) for b in d['bodies'] if b['name'] in ('platform','hub1')])"
out    [('buoy1', 28.67)... ('hub1', 12.0), ('platform', 20.0)]
cmd    python -c "import numpy as np; z=np.load('data/f4/dynamic_inputs.npz');
         print(list(z['case0/body_mass']))"
out    [20.0, 12.0, 12.0, 12.0, 12.0]
rule   GI5 step 2: "feeding today's masses reproduces the reference run ... bit-identical"
judge  the committed deck's masses ARE today's masses, so a build whose override
       plumbing is a NO-OP reproduces the reference run EXACTLY. (ii) is green on code
       that ignores its mass input entirely.
claim  whether (iii) can fail
rule   D1: `body mass = m_nonstruct + k x m_steel`; GI5 step 2: "member steel +
       non-structural + ballast = body mass, exactly"
judge  D1 DEFINES body mass as that sum, so the identity is over FloatFEA's own
       arithmetic and cannot fail on anything but an addition bug.
```

**The silently wrong result:** the converged design step 3 publishes -- its sections, member forces, utilisations, the iteration table, and everything it writes under `results/` -- computed from FloatSim runs that used the deck's own masses rather than the sized ones, with gates (ii) and (iii), `pytest`, `ruff`, `black`, `mypy` and all six ladder rungs green. That is the loop still open at exactly the end GI0 exists to close, and no gate in the locked set would say so.

**The repair needs no new apparatus, because the mechanism already ships, inverted.** `scripts/export_f4_dynamic_inputs.py:467-479` is already Q8's rule -- `np.array_equal` over every array, *"there is no tolerance on this comparison"*, non-finite failing in its own right. So **(ii) becomes a pair**: the zero-change run reproduces bit-identically **and** a run at a perturbed mass does NOT, differing in `case<i>/body_mass`, `m_xddot` and `accel`. And **(iii) closes against the run's own record** -- `case<i>/body_mass`, which `export_f4_dynamic_inputs.py:390` takes from the deck the solve actually used -- rather than against the tool's variables. Provenance, not existence. *Closed when* sec.3's step-2 gate carries the inverted half of (ii) and (iii) reads back from the npz.

**R1208. sec.2c specifies ONE config key routed to all six sites, and the six sites are not one worktree. BLOCKS.**

```
cmd    for each: test -d and git describe --tags
out    C:/Users/xlama/OneDrive/Documents/buoy/HSP-stable  EXISTS  floatfea-ref-1
       C:/Users/xlama/OneDrive/Documents/buoy/HSP-runs    EXISTS  floatfea-ref-1
       ../HSP-stable and ../HSP-runs from C:\dev\floatfea  BOTH MISSING
cmd    git grep -nE '(ROOT|parents?\[[0-9]\])\s*(\.parent)?\s*/\s*"HSP-' -- '*.py'
out    scripts/export_buoy_centers_ref.py:42    HSP_STABLE -> HSP-stable
       scripts/export_platform_deck.py:45       HSP_RUNS   -> HSP-runs
       scripts/measure_platform_joints.py:48    HSP_RUNS   -> HSP-runs
       scripts/report_joint_reactions.py:96     HSP_RUNS   -> HSP-runs
       scripts/run_floatsim_design_waves.py:50  RUNS       -> HSP-runs
       scripts/run_floatsim_design_waves.py:51  STABLE     -> HSP-stable
rule   DS0, enforced by three refusals keyed on the NAME `HSP-stable`:
       report_joint_reactions.py:106, export_platform_deck.py:75,
       run_floatsim_design_waves.py:98
judge  five of the six sites want HSP-runs, one wants HSP-stable, and the three
       refusals make a single key pointed at HSP-stable loud. **The remaining
       direction is silent**: a single key pointed at HSP-runs sends
       `export_buoy_centers_ref` there, and that script has no DS0 refusal of its own.
```

**The silently wrong result:** `data/platform/buoy_centers_ref.json` -- a shipped data file, the input to EB6's label-provenance gate -- regenerated from `HSP-runs` while its `"source"` field declares `HSP-stable/studies/platform-12buoy/platform_common.py` and `_blob_sha` records that tree's sha. `--check` stays green because both sides move together, which is C155's shape, recorded in that file's own docstring. Both worktrees are at `floatfea-ref-1` today, so the bytes match and nothing shows -- and R2 is about to start running FloatSim in one of them. That is FR1's second head verbatim: an input accepted and used other than as declared. **FZ rule 7 would probably reach the right answer on its own**, and I block anyway because the plan's own words specify the wrong thing and GI2 gives no review between this one and step 0's close. *Closed when* sec.2c and sec.3's step-0 gate say TWO keys, name which sites take which, keep `export_buoy_centers_ref` on the stable key, and show the three DS0 refusals still firing.

## The four rulings you asked for

**(1) Is the plan faithful to GI? YES on every gate, with two departures you should state.** GI5 step 2's four sub-gates are all present at `R2.md:173-180` and GI5 step 3's acceptance at `:182-187`, none softened. Five additions are all STRICTER and each traces to GI's own text: read-only-on-HSP and the run folder on (i) (GI1), "not warned" on (iv), the refusal-by-name for a non-converged design on step 3 (D3's last sentence, which GI5 step 3 did not itself carry), the heading refusal on step 1 (FL2(c)), and "never the witness" on step 4. The departures:

* **GI5 step 1's input is "a FloatSim npz"; `R2.md:168` makes it "a FloatSim solve".** sec.2d's reading is right and I measured it: `scripts/export_f4_dynamic_inputs.py:187-196` calls `solve_one`, and the npz is that run's OUTPUT -- there is no FloatSim-written npz in this repository to read. But the consequence is that **step 1 performs the FloatSim invocation GI5 assigns to step 2**, which GI6 gates, and the plan does not say so. State which, and which part of GI6's hold it crosses.
* **`R2.md:165` drops GI3(d)'s purpose clause** "so draft can be held (GI4 D2)". One clause; sec.4 row 1 carries the tie. Prose.

And one addition I checked rather than accepted: step 1's `U = 1.71167` **"at `platform:hub4_arm` ROOT"** is right as the TOOL's own line, and it is a **tie at six figures** -- `docs/F6_utilisation.csv:40` and `:44` give `hub2_arm` and `hub4_arm` the same `1.71167`, and `docs/USER_GUIDE.md:966-975` records the full-precision split. An acceptance that asserts the member NAME must read the tool's line, never a `max()` over the rounded CSV.

**(2) Are sec.2's five measured blocks true? Four yes, one wrong in its `out` line, and the census in sec.2c wrong three ways.**

* **sec.2a -- TRUE, and the "no escalation" conclusion is RIGHT.** The census reproduces line for line (four sites, the numbers as printed), and the mechanism reproduces by reading: `solve_one` builds the deck from `prp._deck_with_drag()`, mutates it at `report_joint_reactions.py:158-163`, and runs `integrate_cummins` -- a FloatSim **time-domain** integration, in-process, HSP source untouched. `case0/body_mass = [20.0, 12.0, 12.0, 12.0, 12.0]` reproduces too. **I went one step further than the plan and read HSP's own builder, which settles GI3(c) harder than sec.2a does:** `platform_rao_pilot._deck_with_drag()` **takes no arguments and reads no file** -- it constructs all 17 bodies in Python from `platform_common.py:41` (`PLATFORM_MASS = 10.0`), `:158` (`mass=cc.ARM_MASS_TOTAL`), `:159` (`Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)`, the hubs) and `:177-178` (the platform). So there is **no file input to HSP's builder at all**, the returned object is the only override point, and the escalation GI1 contemplates is not merely unnecessary -- it is the ONLY alternative, and it would be an edit to FloatSim source. **Your reading is right; raise no escalation.** And an independent corroboration the plan does not give: GI4 D1's own `625 t` and `375 t` are `(1 - 0.75) x 2500 t` and `(1 - 0.75) x 1500 t`, i.e. ER0's platform at lambda = 50, not HSP's 1250 t -- **GI4's numbers confirm sec.2a's reading of "today's masses"**. Caveats are R1207 and R1211.
* **sec.2b -- the conclusion is TRUE and reproduces; one `out` line is FALSE.** `periods_full_s = [10, 12.5, 14, 15, 16.2, 20]`, six cases in the npz, one heading => **six FloatSim cases per iteration** YES, and D4 needs no working-set escalation on heading count YES. But "config declares ONE heading" is not what the command returns: `grep -n heading examples/platform12_placeholder.yaml` returns exactly one line and it is **a comment at line 8**. The config declares **no heading key at all**; heading 0 lives in `report_joint_reactions.WAVE_HEADING_DEG` and in `data/f4/dynamic_inputs.provenance.json`'s `run.heading_deg: 0.0`. **That matters forward**: D4's "every heading in the R1 config" is *unrepresentable* today, and that absent key is what step 1's heading refusal has to grow into. **The 3.66 h / 40.6 GB figures ARE good enough for a plan row, and the reason is specific**: the second heading is excluded by GI1's ban on `platform_bem.py`, not by its cost, so the figures could be wrong by a decade and sec.2b's conclusion would not move. The plan attributes them to the docstring, which is what BP0 needs. One wording point -- sec.2b bolds them as "**measured**" when they are *recorded as measured elsewhere*; if any decision ever rests on them, they get re-taken.
* **sec.2c -- the diagnosis is RIGHT, the WIDER READING IS AUTHORISED, and the census is wrong three ways.** See the ruling below and R1208/R1209.
* **sec.2d -- TRUE and measured.** `cli.py:1279` is the FL2(c) comment, `:1291-1297` the refusal, and the command validates its config and the declared cases before refusing.
* **sec.2e -- TRUE, and I reproduced the consequence rather than reading it.** `rho_eq = f.M_b/(L_b.A)` by construction (`floatfea/model/platform.py:47-48`), so at the shipped config the builder gives platform `rho_eq = 7146.0` / member mass `1875.0 t` and each hub `11433.5` / `1125.0 t` -- **independent of the section, exactly as claimed**. `cli.py:830-833` ships the same sentence to every reader. The second sentence (three configurations, identical densities) carries no triple and I did not reproduce it; the mechanism half is enough to carry sec.2e.

**THE RULING ON THE SIX-SITE READING, WHICH YOU ASKED FOR DIRECTLY: YOUR READING IS RIGHT AND I WOULD GO FURTHER.** GI3(e) names `hsp_pin.HSP_WORKTREE` as the symptom -- *"It does not resolve from `C:\dev\floatfea`"* -- and prescribes a mechanism (*"a config key with an env-var fallback"*). Fixing only that constant fixes **nothing**, and that is measured: `git grep -n HSP_WORKTREE` over the whole tree returns the definition at `floatfea/hsp_pin.py:20` and three documentation hits, and **no consumer**. GI3(e) exists so that step 0's own items (b) and (d) can open the worktree, so routing the sites that actually open it through the new key is the **same item**, not new scope. It is authorised; write it. **R1208 is the one condition on it**: two keys, not one.

**(3) The two "not a tolerance" classifications -- BOTH CORRECT, and one has a shipped precedent.**

* **The iteration cap `8` -- correctly not a tolerance.** Nothing is compared against `8` to decide a result is good; exceeding it produces a **refusal** (D3's "stop and report", `R2.md:186`'s "refused by name"), not an accepted number. That is this repository's own test, stated in `PLATFORM_MASS_OVERRIDE`'s docstring: *"not-a-tolerance: ... Nothing is compared against them."* **But the classification is only as safe as that refusal, and nothing mechanical will hold the value**: `tests/test_no_tolerance_literals.py`'s own docstring says *"integers are counts and are never flagged"*, so `8` becoming `80` is invisible to the one guard that would look. Declare it as a named module constant with a `not-a-tolerance:` justification -- the convention `PLATFORM_OVERRIDE` and `hsp_pin.BASELINE` already use -- so raising it is a visible act. And `R2.md:195` says "**Every** value below goes in `floatfea/tolerances.py`" while two rows say they are not tolerances: say where those two live.
* **The determinism bound -- correctly not a tolerance, and row 5 is not a declaration to write at all.** The comparison already exists in exactly the right form at `scripts/export_f4_dynamic_inputs.py:467-479`: `np.array_equal` on the raw arrays, *"A regeneration either reproduces it exactly or it does not (Q8); there is no tolerance on this comparison"*, with non-finite values failing in their own right rather than comparing equal to zero. Step 2 reuses it rather than re-deriving it. **And that makes sec.6 item 2 measurable today -- see (4).**

**(4) What sec.6 should settle now. Three things, and the first is nearly free.**

**(a) sec.6 item 2's premise is measurable TODAY, and the whole of step 2's (ii) rests on it.** `python scripts/export_f4_dynamic_inputs.py --check` re-runs all six cases through `solve_one` and compares bit-exactly against the committed npz. That single command **is** GI3(b)'s wall-time measurement *and* the determinism measurement; running it twice costs one more pass. Nothing in this repository has published a measurement of FloatSim's determinism on this path, and Q8's premise is the thing step 2's bit-identical gate is built on. Convert the argument into a measurement.

**(b) sec.6 does not carry the contradiction between D1 and the step-2 bookkeeping identity, and GI6 is the only scheduled point where D1-D4 can be corrected.** D1: `body mass = m_nonstruct + k x m_steel`. GI5 step 2 (iii): `member steel + non-structural + ballast = body mass, exactly`. **The two are consistent only if ballast == 0** -- and if ballast is identically zero then D2's draft can never be held when `m_steel` moves, so (iv)'s refusal fires on the design rather than on a test. One of the two has to gain a ballast term and Xabier is the one who says which. This is loud rather than silent when it bites, so it does not block; it belongs in step 0's report because that is where it can still be cheap.

**(c) sec.6 item 3 is not a contingency -- it is a number, available today, and step 0 (d) should publish it.** Measured at this commit from the shipped deck and the shipped builder:

```
cmd    which bodies carry a hydro label
out    buoy1..buoy12  hydro_body_label = 'buoy1'...   platform, hub1..hub4  None
cmd    the builder's own member geometry and D1 at k = 1.0, lambda = 50
out    platform  steel 2059.7 t vs 1875.0 t allocated   steel/alloc = 1.0985
       each hub  steel  772.4 t vs 1125.0 t allocated   steel/alloc = 0.6866
       D1: platform 2500 -> 2684.7 t (+7.39%), each hub 1500 -> 1147.4 t (-23.51%)
       the five bodies 8500 -> 7274.3 t = -1225.7 t (-14.42%)
       the 12 buoys carry 43005 t, so the deficit is 2.85% of them
rule   D3's convergence band is 0.5% per body between iterations
judge  **the bodies whose mass D1 changes carry NO buoyancy, and the bodies that
       carry buoyancy are not changed by sizing.** So D2's "every floating body (or
       the buoy carrying a changed body) gets compensating ballast" is written for a
       picture this deck does not have: ballast has to sit on the NON-wetted bodies,
       and "the draft is held" becomes a condition on total weight and its
       distribution, measured per BUOY. And iteration one moves every mass one to two
       decades outside D3's band, so the loop certainly iterates -- what nobody has
       measured is whether the BEM reference survives the ballast it implies.
```

This also reproduces both near ends of `R2.md:31`'s range (`+10%` -> `+9.85%`, `-31%` -> `-31.34%`) at this commit, which is the re-measurement sec.0 routes to step 0 (a).

## Ledger (FR1: none of these can cause a silently wrong result; one line each)

* **R1209 -- sec.2c's census is wrong three ways, in the R755/R1147 shape: an `out` block that reports more than its own `cmd` returns.** The heading says "five sites" and the body says "SIX sites in five files"; it is **six files**, not five; counting assignments it is **seven**, because `run_floatsim_design_waves.py` has two (`RUNS` at `:50`, `STABLE` at `:51`) at line numbers the plan prints as `49-50`; and **the quoted needle cannot see either of them** -- `grep -rn "HSP_RUNS\s*[:=]\|HSP_STABLE\s*[:=]\|HSP_WORKTREE" --include=*.py .` returns **five** lines, not the six printed. The needle that finds all seven is in R1208's block. The plan's `HSP_WORKTREE`-has-no-consumer claim is **TRUE** -- I ran it over the whole tree, not just `*.py`.
* **R1210 -- sec.2b's "config declares ONE heading" is false as measured** (see ruling 2). The conclusion is unaffected.
* **R1211 -- sec.2a and sec.3 use one word for two mechanisms, GI3(c)'s first half is unanswered, and four of the five bodies have never been overridden by anything.** GI1 requires mass changes to go *"through HSP's deck builder with a declared override file, as ER0 did"*; `R2.md:174` says FloatFEA "writes the override file" YES, while sec.2a's judge says step 2 must "move it out of a script global into the tool", which is the **in-memory** path where nothing on disk declares what was applied. ER0 did BOTH -- `export_platform_deck.apply_override` mutates in memory **and serialises to `data/platform/platform12_deck.yaml`**, and `export_f4_dynamic_inputs` records the dict in `dynamic_inputs.provenance.json`'s `"override"` block. Step 2 says which, and the declared-on-disk half is what makes the override auditable. GI3(c)'s first half -- *how* mass and inertia enter the builder -- has the precise answer in ruling 2 and the plan does not state it. And **the existing helper is the wrong shape to generalise**: `_apply_platform_override` selects `b.name == "platform"` and sets three inertia components, while `_inertia_matrix` reads six and *"the off-diagonals are read rather than assumed zero"*; the four hubs sit at `cc.ARM_MASS_TOTAL` and the literal `Inertia(Ixx=0.5, Iyy=0.5, Izz=1.0)` with **no override anywhere in this repository**. One body -> five, three components -> six, and `export_platform_deck.apply_override`'s generic dict walk is the better shape.
* **sec.4 row 1 does not declare the FORM of the equilibrium-drift tolerance, and draft is a LENGTH.** An absolute tolerance on a dimensional quantity either fails the unit-scaling test or passes it vacuously, so the entry has to be relative to a stated response scale -- the BEM reference draft, or the buoy radius -- and dimensionless, with trim against a stated angle scale. sec.4's stated purpose is to be reviewable before the value exists, so the form belongs there now.
* **sec.2's CP3 header overclaims.** It says "Figures taken at this commit, after the last edit", and two are not: sec.0's `+10% to +29% / -31% to -55%` (attributed to pre-R2 work and correctly routed to step 0 (a) -- both near ends reproduce, ruling 4c) and sec.2e's "three configurations" (no triple at all, and a causal "so" with no cell, BG0). Say which figures are this commit's and which are carried.
* **sec.2's five triples are not machine-checked and two are not runnable.** `tests/test_tree_prose_consistent.py` reads `^claim:` / `^cmd:` / `^out:`; `grep -c "^cmd:" docs/milestones/*.md` is 0 everywhere, so the space-aligned form R1.md and R2.md both use is invisible to the guard that scans `docs/milestones`. And `python -c "...np.load(NPZ)..."` has no `NPZ`, while sec.2b's is an ellipsis. R1.md uses the same form, so this is the house convention and not a new deviation -- but a `cmd` a reader cannot run is not a check.
* **sec.5 does not carry GI1's "the deck stays DO-NOT-HAND-EDIT".** One line; it belongs beside the three prohibitions.
* **R1212 -- MINE, and it goes to Xabier, not into a round.** I was asked to write `docs/reviews/R2/plan.md`. That path does not exist and cannot: `scripts/write_verdict.py` writes `docs/reviews/<milestone>/step-<step>.md` and has no other path, the `PreToolUse` hook refuses every other door, and `scripts/ci_section.py:153-157` globs `step-*.md` with `re.fullmatch(r"step-0*([0-9]+)")`, so a file named `plan.md` would not be found and R2's CI-section anchor would stay missing -- the FP1 failure mode `CLAUDE.md` already records. I used `--step 0 --interim`: no report revision exists, it consumes none of step 0's three ES0 revisions, and it closes nothing. **The `--interim` header the tool stamps says "ES0 INTERIM CHECK", which is accurate about rounds and mislabels the round's nature** -- this is GI2's plan lock. If a separate plan-lock artifact is wanted, that is an edit to `write_verdict.py` and to `ci_section.py`'s glob, and it is Xabier's to authorise.

## Tolerances touched

**None.** `git diff de04131..HEAD -- floatfea/tolerances.py` is empty and the commit touches one file. sec.4 declares five future entries and I ruled on their classification above; **"None of them exists yet" is true** -- the only convergence entry in the file is `BOUNDARY_BISECTION_CONVERGENCE` at `:1290`, which is a solver-internal bisection and not D3's loop. EU1 does not arise.

## Corpus

**No new batch, and GC3 leaves that to me.** What I ran instead is the substitute GG1 records, and it is where three of the four blocking findings came from: a **continuum grid over the parameter space D1's rule guards** (all five bodies, steel against allocated mass, through the shipped builder -- ruling 4c), a **regeneration check on the published figures** (sec.0's two ranges, sec.2a's npz block, sec.2e's densities, all re-derived at this commit), and **three controlled cells on the marker state**, one variable each. A batch would have bought none of them on a commit that contains no code.

**And batch 26 had already predicted both halves of R1205 and R1206.** `tests/corpus/plan_step_marker_resolution.txt` carries `id=two_plans_carry_it_F3_and_a_new_F4 ... expect=caught measured=RED_2_plans_carry_it` and `id=step_number_is_zero ... expect=caught measured=RED_the_plan_carries_no_readable_step_number`. **The tree is now in both states at once**, eleven batches later, and that is the corpus doing the job it exists for -- which is the reason I am not spending this round writing another one.

## Next step opens when

**STEP 0 DOES NOT OPEN YET, AND THE REASON IS CHEAP: one commit touching `docs/milestones/R1.md` and `docs/milestones/R2.md`, with no re-measurement of anything.** GI2 asks for one round and I am not asking for a second review before step 0's code -- **PASS follows automatically from the four conditions below being visible in the diff**, and I have written them so that the implementer can satisfy them without another invocation. What they must not do is start step 0's code with the gating apparatus in the state R1205 measures.

1. **R1205 -- `docs/milestones/R1.md:3`'s marker retired**, in the form `F2.md:10`, `F3.md:9` and `F6a.md:3` use. Then `python scripts/check_carried.py` names **R2**, not F2 step 4, and `python -c "import scripts.ci_section"` stops raising. Paste both.
2. **R1206 -- one of the three exits chosen for step 0's number**, with `test_the_plan_names_the_step_under_execution` green at R2 under execution, and the cell re-run. If the exit is renumbering, say what happens to GI2's "before any step-1 code".
3. **R1207 -- sec.3's step-2 gate carries the inverted half of (ii)**, and **(iii) reads `case<i>/body_mass` back from the npz the solve wrote.** Both are amendments to `R2.md`, not code: GI6 holds step-2 code regardless, and this is the only moment at which the gate is still free.
4. **R1208 -- sec.2c and sec.3's step-0 gate say TWO keys**, which sites take which, `export_buoy_centers_ref` on the stable key, and the three DS0 refusals shown still firing.

**Then step 0 opens and nothing else does.** GI6 holds step 2 regardless, and step 1's code waits on Xabier's answer to D1-D4 as well -- because ruling (1)'s first departure means step 1 as written performs the FloatSim invocation GI5 assigns to step 2. Say which in the amendment.

**And four things for step 0's report, none of which blocks and all of which are cheap now:** the `--check` determinism run (ruling 4a, one command, answers GI3(b) too); the D1/(iii) ballast contradiction put in front of Xabier (4b); GI3(d) answered with the wetted/non-wetted split and the `-1225.7 t` first iteration (4c); and GI3(c) answered in BOTH halves, with HSP's zero-argument builder named, because that is what tells Xabier the escalation is not merely unnecessary but impossible without an edit to FloatSim source.

**On the schedule.** GI sets no date and `R2.md:14-16` says so rather than inventing one, which is the right handling. This HOLD costs one commit and no measurement. **Nothing here is a STOP**: the plan is faithful to GI, the ladder was green on all six rungs at the last concluded run over code byte-identical to this tree, and no low rung is red.

**What the plan got right, and it is much the larger part.** It went and measured the five things the steps rest on instead of asserting them, and four of the five hold exactly as written. It found the override path GI3(c) asks about and read it correctly enough to withdraw an escalation -- which is the single most consequential call in the document, and it is right for a reason stronger than the one it gives. It noticed that "today's masses" is ambiguous and that `None` is a different run, which is the distinction the zero-change test lives or dies on. It read GI3(e) wider than GI wrote it and said why, on the half-an-item rule, rather than doing the literal minimum. And it declared two of its five tolerance rows as **not** tolerances with the reasoning attached, which is the step at which a tolerance usually ships without a counter.
