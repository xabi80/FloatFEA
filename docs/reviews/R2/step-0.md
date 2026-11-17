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
