# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 57cfae6683d6dbdd14f47d4e38aaf481ab26d79a
**Reviewed commit: `57cfae6683d6dbdd14f47d4e38aaf481ab26d79a`.**
Verdict: HOLD
**Reviewed commit: `57cfae6683d6dbdd14f47d4e38aaf481ab26d79a`.**
Tests: 408 failed, 3695 passed, 1 skipped, 2 warnings in 1210.93 s (0:20:10)   (my own whole-suite run at the reviewed commit, `-p no:randomly`, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the tenth in step 3.** There is still no `docs/reports/R1/step-3.md`, so no reviewed revision has been consumed -- **0 of 3** -- and this counts against no round.

**TWO FINDINGS BLOCK: R902 and R903.** Both are in `scripts/measure/`, both are EZ0 surface by name, both put a wrong number into a published deliverable at exit 0, and both were found by running the generator this diff changed at a configuration the diff did not choose.

**R897 IS ANSWERED ON ITS REDS, and its closing condition's SECOND clause is not met.** Both ids are gone -- locally and in CI, with `comm -3` between the two id sets empty -- all four `_build` death greps are `0` on both machines, the counter-case reddens and the turn's ablation reproduces exactly. But the assertion was repaired as TWO SCALARS where the condition said "every copy the harness will make", and I measured it BLIND ON THREE CONFIGURATIONS, one of them R897's own `src == dst`, with both new assertions reading `True`. That is R904: FF0-class, next commit, does not block.

**R896 IS ANSWERED FOR THE WAVE BASIS AND THE DOOR IS CORRECT.** I reproduced the before/after rows, the subprocess ablation, the EH4 boundary in both directions at the NEW call site, and a full regeneration of the shipped deliverable, which is byte-clean. **R902 and R903 are not a failure to close R896** -- they are the next two doors in the same wall, and R903 is the exact question the previous verdict told the turn to ask and which the turn honestly declared it had not answered.

**Both of the turn's self-reported corrections are accepted and verified.** R900 reproduces more sharply than stated, and the `black` figure is `74` for `tests` against `116` for the pair -- I ran both.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1"; `docs/directives/FR.md`). For each blocking finding I name the silently wrong result, as FR1's last sentence requires. R904 does NOT block: no number is wrong in any artifact, and its disposition is FF0's "fixed in the next commit", not the ledger.

```
cmd    git log --oneline 6e24b44..HEAD ; git diff --numstat 6e24b44..HEAD
out    57cfae6 aaa95ab c255751 94d1adc -- FOUR commits, one of them my own verdict.
       docs/reviews/R1/step-3.md 759/0 (my own previous verdict) |
       floatfea/run/pipeline.py 46/7 | scripts/measure/f6_results_report.py 8/1 |
       tests/regression/test_f6_deliverable_agrees_with_itself.py 59/0 |
       tests/test_report_guard_states.py 34/23
cmd    git diff 6e24b44..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 6e24b44..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py        -- a file, as my instructions say it must be
cmd    git diff --stat 6e24b44..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)   -- my own instructions untouched by all three commits. NOT A STOP.
cmd    git diff --numstat 6e24b44..HEAD -- floatfea/run/config.py
out    (empty)  -- `HEADING` and `WAVE_HEIGHT` sit at config.py:189-190 unchanged, so NO
       BOUND VALUE MOVED. That is EU1's worst case, not its safest.
cmd    git show --stat aaa95ab
out    (no file rows) -- aaa95ab is an EMPTY commit, as the turn says
cmd    black --check tests ; black --check floatfea tests
out    74 files would be left unchanged / 116 files would be left unchanged
       -- **THE CORRECTION IS RIGHT.** 74 is `tests`; 116 is the pair.
cmd    ruff check floatfea tests scripts ; black --check scripts ; mypy floatfea
out    All checks passed! / 34 files would be left unchanged /
       Success: no issues found in 42 source files
cmd    git status --porcelain  (before anything, and after one disposable worktree, 10
                               NEXT configurations, 27 generator runs, 3 ablations and
                               one regeneration -- the worktree then removed)
out    (empty) / (empty)
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** `ls docs/reports/R1/` is `step-1.md step-2.md` and their two answers files, so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The newest report revision in the tree is still step 2's third, and **ten verdicts are now newer than it.** That is EG3 state (2).

**R855's standing condition is MET for the third time in this step, and I record the repeat the turn asked me to record.** `c255751` and `57cfae6` both decline to claim a whole-suite figure and name what they ran; `aaa95ab` exists BECAUSE the turn re-took a figure it had pasted wrong, which is CP3 working rather than CP3 failing. **The repeat is real and the pattern is narrower than "CP3 again":** both times the number was correct for a command the turn did not run, and both times the part that was dropped was the SCOPE TOKEN -- `tests` against `floatfea tests`. A remembered figure loses its argument list before it loses its digits.

## The rulings the turn asked for, and EU1

### 0. EU1 does NOT strictly apply; I ran the adversarial case anyway, and it is where every finding below came from

```
claim  neither commit moves a tolerance VALUE or a declared `_COUNTER`, so EU1's trigger
       is not met on its own terms -- and EU1's REASON is met by the second commit exactly
rule   `CLAUDE.md` section Step gating (EU1): "An interim check whose diff moves a
       tolerance VALUE or a declared counter includes the adversarial case"
cmd    git diff 6e24b44..HEAD -- floatfea/tolerances.py ; grep -n "_COUNTER" over the five
       changed files ; git diff --numstat 6e24b44..HEAD -- floatfea/run/config.py
out    (empty) / (empty) / (empty)
judge  `NEXT` is a harness constant, not a tolerance and not a declared counter, so
       `c255751` does not trip EU1 by the letter. **`57cfae6` is EU1's own worst case
       stated in EU1's own words:** `RECORDED_BOUNDS`' justification was re-derived and
       rewritten while `WAVE_HEIGHT` stayed at `("m", 0.0, 100.0)` -- "a value that does
       not move is the worst case for this, not the safest". So I ran the configuration
       nobody chose at both sites. **The flag was right and it paid. R902 and R903 are
       both from the generator run at sidecars the diff did not write; R904 is from the
       harness resolved at marker pairs the diff did not have.** None came from reading
       the diff: a grep over this diff finds every changed line and cannot find the line
       that should have changed.
```

### 1. R895: the escalation asked for a ruling the previous verdict had already written, and R902 now DECIDES the route on a measurement

```
claim  the previous verdict ruled on both routes, declared both legitimate, and named the
       property it would measure rather than the route
rule   `docs/reviews/R1/step-3.md`, R895's `Closed when`: "one of the two published
       numbers is DERIVED from the other and the already-validated lambda, OR the pair is
       CHECKED against lambda"; and its question 1, which ruled the split right under
       `CLAUDE.md` section Tolerances and pre-authorised the epsilon route's plan re-lock
       under DK0
judge  **The escalation is not a breach, it cost nothing, and it asked for a ruling that
       already existed.** The turn was never asked to pick between a schema change and a
       tolerance; it was asked for a repair with a stated property, by either route, with
       the re-lock pre-authorised. **What is NEW is that R902 decides the route on a
       measurement rather than a preference:** a THIRD consumer of this quantity exists,
       the band and steepness table, and it reads a module literal. An epsilon between
       the two recorded numbers leaves that consumer on `24.2` whatever the sidecar says;
       a DERIVATION from one source does not. **The derivation route closes R895 and R902
       together; the epsilon route closes one of three.** That is the previous round's
       "one of three" arithmetic, one level out.
cmd    is the single source already in the tree?
out    scripts/export_f4_dynamic_inputs.py:525-526
         "wave_height_model_m": float(rjr.WAVE_HEIGHT_MODEL_M)
         "wave_height_full_m":  float(rjr.WAVE_HEIGHT_MODEL_M) * float(g41.LAMBDA)
       scripts/report_joint_reactions.py:90  WAVE_HEIGHT_MODEL_M: Final[float] = 0.484
       -- ONE source, ONE product, FOUR hand copies of the product downstream (R902).
```

**R895 CARRIES AS BLOCKING** into step 3's first reviewed revision. Its first half is closed and I verified it; its second half is untouched and is now joined by R902, which is the same relation defect with a literal on one side instead of the sidecar.

### 2. R898: the refutation of the NAIVE fix REPRODUCES EXACTLY; the conclusion does not, and the mechanism is already in the same file

```
claim  the turn's census is right to the row
cmd    for each of the 17 review files: count `^Verdict: *PASS`, count `^Closes:`, and
       whether the file's MILESTONE directory carries any `^Closes:` at all
out    Closes=0 on 14 of 17; Closes=1 on F6b/step-1, R1/step-1, R1/step-2
       -- the turn's figure EXACTLY.
       MILESTONE_HAS_CLOSES:  F2 0  F3 0  F4 0  F6 0  F6a 0  F6b 1  R1 2
judge  **The turn is right that `^Closes:` alone makes 14 closed steps read open, and
       right that no TEXTUAL MARKER can discriminate.** FK1 was adopted after those 14
       files were written, so no property of their text distinguishes them: the
       distinction is HISTORICAL, not textual. **And this hook already has an idiom for a
       historical distinction, nineteen lines above the defect:**
cmd    grep -n "pre_gating" .claude/hooks/require-verdict.sh
out    :237  pre_gating="docs/reports/F2/step-1.md ... step-3.md"   (three entries)
       :257  for known in $pre_gating; do
       -- a FROZEN exemption list, for "the three reports that predate their milestone's
          first verdict". The pre-FK1 REVIEW set is equally frozen: no new file can enter
          it, because every verdict from FK1 onward either carries `Closes:` or is not a
          closing verdict.
```

**So the answer to "name it and I will implement it next commit" is: not a marker. A frozen `pre_fk1` list beside `pre_gating`, the predicate reading `^Closes:` for everything not on that list, and the function renamed to say which of the two it reads.** I solved that boundary in BOTH directions (EH4):

* **Weakening, direction one** -- can an OPEN step read CLOSED? Only if its file carries `^Closes:`, which FK1 permits only in a closing verdict and which the `PreToolUse` hook makes unwritable by the implementer. No.
* **Weakening, direction two** -- can a CLOSED step read OPEN? Only a pre-FK1 closure not on the list, and the list is finite, enumerable today at 14, and frozen.

**The alternative I measured and am NOT recommending, with its residual named**, because the turn should see why it is the weaker of the two: a per-milestone feature detect -- use `^Closes:` where the milestone directory uses it, fall back to PASS where it does not -- is correct on all 17 files today and leaves ONE residual, the first step of every FUTURE milestone before any verdict in it carries `Closes:`, where R898 recurs for exactly that step. The frozen list has no residual.

**R898's practical effect today is still nil, measured rather than assumed**, which is why it does not block: the blocking branch requires `stepnum(newest report) > stepnum(held step)`, the newest report is `docs/reports/R1/step-2.md`, and `2 > 3` is false. It is FF0-class rather than ledgered because it is the predicate that decides whether a step is closed.

### 3. The generator's bare traceback: FR1 covers it, and I read it the same way the turn does

```
claim  the refusal's outcome is right and nothing is published
cmd    27 generator runs on mutated sidecars, each checking whether the `--out` file
       exists after a refusal
out    every refusal: EXIT=1, out_written=False -- no partial deliverable, no zero-byte
       file, and the ConfigError names the field
rule   FR1's first non-blocking class: "a refusal whose message is unclear but whose
       outcome is right"
judge  **AGREED. Ledger item, not a round.** `out_written=False` is the property that
       makes it safe and it held at every cell I ran -- which also says the R878 failure
       mode, a zero-byte artifact left behind by a refusal after the solve, does not
       recur at this door. One ledger observation and not a condition: the new test's
       second assertion, `"wave_height_full_m" in combined`, is satisfied by the
       traceback TEXT, and I produced a sidecar giving `KeyError: 'wave_height_full_m'`
       with the validator never reached -- so that assertion ALONE cannot tell a refusal
       from an unrelated crash on the same key. The ablation that matters DOES redden
       (`1 failed, 20 deselected`, reproduced), so the test is not vacuous; the second
       assertion is weaker than it reads.
```

### 4. R899's `process:` commit: not before step 3's first revision, and the trigger is not a date

```
claim  nothing is reading `docs/SUPERVISOR.md` on R1 today
cmd    gh pr list --state all ; gh pr view 1 --json comments ;
       grep -c "FR1\|FR0" docs/SUPERVISOR.md
out    one PR, #1, head `F2`, base `master`, OPEN, **0 comments**
       grep -c -> 0   (R899 still live, unchanged by this diff)
judge  **FS0's ordering stands: FL2 first.** There is no witness comment anywhere and no
       PR for R1, so the document that misstates the criterion is not instructing
       anybody. The moment a witness IS invoked on R1 the finding becomes live, so the
       `process:` commit lands **before any witness invocation** -- a trigger rather than
       a date, and one that does not compete with FL2.
```

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R895** (the recorded pair never checked against lambda; `WAVE_HEIGHT` a full-scale domain on a model-scale field) | **HALF ANSWERED, HALF STILL OPEN AND STILL BLOCKING** | `57cfae6`. Condition (i) is MET: the `RECORDED_BOUNDS` docstring no longer claims a configured counterpart for `wave_height_model_m` and says in terms which of its three keys the old reason was false for. Its two figures are CORRECT -- I re-derived them: `100/0.484 = 206.6` -> `207x`, `2.0/0.484 = 4.13` -> `4.1x`. Conditions (ii) and (iii) are UNTOUCHED: the relation is unpoliced and my predecessor's cases C and D are in no test. Ruled above under heading 1; it carries as blocking, and R902 now decides its route. |
| **R896** (the second door: the generator read `prov["run"]` raw) | **ANSWERED for the wave basis, and the repair is good** | `57cfae6`. `wave_basis_from_sidecar` is public, `exported_wave_basis` delegates, the generator calls it, and no raw read of a BASIS key remains in that script. I verified the caller is held by running the real script as a subprocess with the call removed: `1 failed, 20 deselected`; restored, `1 passed, 20 deselected`. The residue is R903 and R902, both new. |
| **R896, the turn's own question (b)** | **ANSWERED NO, MEASURED** | `run = {**prov["run"], **basis}` cannot leak an unvalidated BASIS value. `basis` is empty only when NONE of the four keys is in the block, and the script then raises `KeyError: wave_height_full_m` at exit 1 -- I ran that cell. A list, a string and an absent `run` block all crash rather than publish. The merge is also a no-op on values, since `basis` holds the same objects for those keys; the validation is enforced by the RAISE and not by the merge, which is worth a sentence because the line reads as if it sanitised. |
| **R897** (two states died in `_build`; the new assertion compared the wrong pair) | **ANSWERED ON THE REDS; THE CONDITION'S SECOND CLAUSE NOT MET -- see R904** | `c255751`. Both ids are gone from my 408 and from CI's 408, and `comm -3` between the two id sets is EMPTY. `grep -c` over my whole-suite output AND over CI's own failure log: `SameFileError 0`, `FileNotFoundError 0`, `PermissionError 0`, `FileExistsError 0` -- all four names, on both machines, not one. Counter-case, one variable moved at the reviewed commit: reverting `NEXT` to `STEP + 1` gives `3 failed in 2.59s` (the two states PLUS the new assertion); restored, `3 passed in 30.86s`. **So the repaired assertion carries its own failure, which the one it replaced did not.** The file is `7 failed, 17 passed`, which beats the condition's `8 failed, 14 passed`, and `newest_report_has_no_verdict_yet` went green as well. |
| **R898** (`closed_by_a_pass` reads any `Verdict: PASS`) | **STILL OPEN, FF0-class, and the turn's refutation of the NAIVE fix is CORRECT** | ruled above under heading 2, with the census reproduced row for row and a repair named that has no residual. Not blocking. |
| **R899** (`docs/SUPERVISOR.md` states CZ0 and never names FR1) | **STILL OPEN, correctly not taken** | `grep -c "FR1\|FR0" docs/SUPERVISOR.md` is still `0`; the `.claude docs/SUPERVISOR.md` diff is empty. Ruled above under heading 4. |
| **R900** (two of four commits had no CI run) | **ANSWERED, and the mechanism reproduces a second time** | `gh run list --commit` is `[]` for `c255751` and `aaa95ab` and `gh run list -L 10` shows no run at either. The only new run is `40265555791` at `57cfae6`, the push tip -- so FP1 is satisfied only when the reviewer is invoked ON the tip, which it was. |
| **R901** (two stacked docstrings on `NEXT`) | **ANSWERED** | `c255751`. One docstring now, and deleting rather than correcting the orphan was right: it described F2-era `step-6` states. |
| **R882** (the heading refusal routes a reader from the refusal to the publication) | **STILL OPEN, AND THE FINDING AS WORDED IS NOW STALE -- the declaration it needs has changed** | the clause "or remove `load_cases.headings` so no comparison is claimed" is still at `pipeline.py:596-597`, but the route it names is CLOSED: `exported_wave_basis` is called unconditionally at `pipeline.py:1019` as `wave_basis=`, not only inside the coverage check, so the reader validates `heading_deg` whether or not a heading is declared. **The sentence is still wrong, and it is now wrong in the opposite direction -- it names a remedy that no longer works.** The declaration the turn owes should say that rather than restate R882. |
| **R883** (`10**400` "is caught before `float()` raises") | **STILL OPEN, re-measured live** | the sentence is now at `pipeline.py:746`; `float(value)` is at `:771`. Unchanged in substance. |
| **R884** (a list `run` block yields an empty `present` and publishes "NOT RECORDED" at exit 0) | **STILL OPEN, and I measured a SECOND sub-case the finding does not name** | `wave_basis_from_sidecar` on a `run` of `[1, 2]` returns `{}`; on a `run` of `["heading_deg", 0.0]` it raises an UNCAUGHT `TypeError: list indices must be integers or slices, not str` at `pipeline.py:869`, because `key in run_block` is a membership test on a list. Both predate this diff. **And the two doors now disagree in the OTHER direction:** the generator crashes on a list `run` where `floatfea run` publishes "NOT RECORDED". |
| **R885** (`HEADING`'s raw `0..360` refuses a legally signed `-90`) | **STILL OPEN** | `config.py:189` unchanged. |
| **R886** (blanket `# noqa: F401`) | **STILL OPEN** | `tests/unit/test_headings_and_bem_coverage.py:35` unchanged. |
| **R882-R886: the declaration is now owed by name, and the preferred trigger has been spent TWICE** | **all five still open** | my predecessor named `6e24b44` and it was spent; `57cfae6` touches `_validated_wave_basis`'s own module and is a second spent trigger. The remaining place is step 3's first reviewed revision -- each with what was left and why, and R882's carrying the correction above. |
| **R867, R868, R869** (eight topologies, one runs) | **still open, blocking by name into the first revision** | `git diff --stat 6e24b44..HEAD -- floatfea/model floatfea/solve` is empty. FT2.7 is in the plan row as of `ece0ebe`. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a)) | **still open** | the `pipeline.py` diff is R896's door and R895's docstring; no topology code moved. |
| **R862** (three hand copies of the stage set) | **still open and STILL NOT DUE -- trigger re-measured, not taken on trust** | `git diff 6e24b44..HEAD -- floatfea/cli.py` is EMPTY. It blocks in the commit that adds a timed stage. |
| **R863, R864, R865** | **all three still open, untouched** | the `tests/regression` diff is the one new R896 test and nothing else; R864's condition still needs a report revision that does not exist. |
| **R891, R892** (replay 1's void paste; the control that moved two variables) | **still open, untouched** | ledger items; neither is in this diff. |
| **R847 / C43, R848, R849 with R854** | **all still open, all correctly so** | `floatfea/cli.py` and the rest of `tests/regression` are untouched. |
| **R852** | **ROUTED, not open** | FS3 ledgers it to FL3; `docs/directives/FS.md`. |
| **R880** (my own definition cites "their two corrected lists", which FS1 deleted) | **STILL OPEN, STILL CORRECTLY NOT TAKEN, and it did not misdirect me a fifth time** | `git diff --stat 6e24b44..HEAD -- .claude/agents` is empty. I ruled under `CLAUDE.md`'s predicate as FT1 narrowed it, applied PER ID to all 408 reds. **Do not take it first.** |
| **R881, R888, R889, R890, R893, R894** | **answered in earlier rounds and not reopened by this diff** | R881's repair is still in place and the three published deliverables still regenerate byte-clean -- re-measured, because `pipeline.py` moved again. |
| **R835, R836, R871** (EG3's lists; FS1's deletion of FC1's reason) | **ANSWERED, and FT1's narrowing orphans nothing at this commit either** | the two limb-two ids are `test_the_report_carries_a_WHOLE_SUITE_count` and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`, both present, both with their own commit as SUBJECT. Full per-id trace below. |
| **C45** (a mirror going stale) | **DOES NOT RECUR in this diff; still live as R899** | `CLAUDE.md`, `docs/SUPERVISOR.md` and `.claude/` are untouched by all three commits. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally and on a machine neither of us controls** | mine above; CI run `40265555791`, job `lint, unit and guards`: actionlint, ruff, `black --check`, mypy and **unit tests** all SUCCESS. |
| **C42, C44** | **mine, accepted, carried** | unchanged by this diff. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **EG3(ii): the verdict commit measured** | **NOT redone this round, and I say so** | ES0's light scope. What I ran instead is sharper for R897's purpose: the counter-case reddens and clears the two ids AT the reviewed commit with nothing written to `docs/reports/` or `docs/reviews/`, which separates the two causes without a second commit to compare against. |
| the suite-count line, and CZ1 (ii)/(iii)'s four outputs | **still owed, still structurally unpayable until step 3's report exists** | limb two of the predicate by construction; two of this round's 408 reds ARE it. |

## Findings

**R902 and R903 BLOCK. R904 and R905 do not.** No tolerance value moved, no conftest moved, nothing in the diff is a tolerance under another name, and my own instructions are untouched.

---

**R902. (BLOCKS) THE GENERATOR NOW VALIDATES THE RECORDED WAVE HEIGHT AND THEN IGNORES IT. EVERY NUMBER THE DELIVERABLE COMPUTES FROM THAT QUANTITY -- THE ASSOCIATED-PERIOD BAND, THE STEEPNESS RATIO AND THE `BREAKING` VERDICT -- IS TAKEN FROM A MODULE LITERAL `WAVE_HEIGHT_FULL_M = 24.2`, IN TWO SEPARATE `scripts/measure/` GENERATORS, WITH NOTHING ANYWHERE TYING EITHER LITERAL TO THE SIDECAR OR TO EACH OTHER. THE SAME DOCUMENT PRINTS BOTH NUMBERS AND PRESENTS THEM AS ONE QUANTITY.**

```
claim  the published full-scale height and the height the physics screen is computed at
       are two independent sources, and only one of them is now validated
cmd    grep -n "WAVE_HEIGHT_FULL_M" scripts/measure/f6_results_report.py
         scripts/measure/member_forces_table.py ; grep -rn "WAVE_HEIGHT_FULL_M" tests/
out    f6_results_report.py:76   WAVE_HEIGHT_FULL_M = 24.2
                         :402   lo, hi = _band(WAVE_HEIGHT_FULL_M)
                         :417   "the associated-period band for H = {WAVE_HEIGHT_FULL_M} m"
                         :425   steep = _steepness(period, WAVE_HEIGHT_FULL_M)
       member_forces_table.py:143 WAVE_HEIGHT_FULL_M = 24.2
                              :176-178  s = WAVE_HEIGHT_FULL_M / lam ; lo, hi from it
       grep over tests/            -> **(empty). NOTHING asserts either literal.**
cell   ONE VARIABLE MOVED -- the recorded pair -- through the REAL generator, at a pair
       that is INSIDE `WAVE_HEIGHT`'s domain and CONSISTENT with the recorded lambda, so
       R895's own relation check would pass it too
out    model=1.0  full=50.0  lambda=50   EXIT=0, deliverable written:
         "wave height, full scale  : 50.0 m (1.0 m model, Froude lambda = 50.0)"
         "the associated-period band for H = 24.2 m, DNV practice:"
         "sqrt(6.5 H) = 12.5419 s    sqrt(11 H) = 16.3156 s"
         row  12.5   H/lambda 0.0992        ok    no   0.334% short   GOVERNING
         row  16.2   H/lambda 0.0591        ok   yes            -     GOVERNING
cell   THE ABLATION, one variable: the literal set to the height the document publishes
out    model=1.0  full=50.0  literal=50.0  EXIT=0:
         "the associated-period band for H = 50.0 m"
         "sqrt(6.5 H) = 18.0278 s    sqrt(11 H) = 23.4521 s"
         row  12.5   H/lambda 0.2050  BREAKING   no  30.662% short   GOVERNING
         row  16.2   H/lambda 0.1221        ok    no  10.139% short   GOVERNING
rule   FR1's first limb with EZ0; and EZ2's associated-period rule, which is what these
       columns implement
judge  **IT BLOCKS. THE SILENTLY WRONG RESULT IT PRODUCES:**
       `results/F6/floatfea_results_report.md` stating `wave height, full scale : 50.0 m`
       and then, nine lines later, that the governing period `T = 12.5 s` has
       `H/lambda = 0.0992`, is `ok` against the `1/7` breaking limit and sits `0.334%`
       below the band -- when at the height the same document publishes it is `0.2050`,
       **BREAKING**, and `30.662%` short. A breaking, out-of-band sea state published as
       admissible, at exit 0, in the document that carries the utilisations. **And FR1's
       SECOND limb applies verbatim and independently:** the recorded
       `wave_height_full_m` is declared as the run's wave height, is now validated as
       such, and is then not used -- a literal is used in its place while the artifact
       presents the two as one quantity. That is "an input accepted and used other than
       as declared".
```

**And the file says the lesson one constant above the one that breaks it**, which is why I am not calling this an oversight about an unlikely input:

```
claim  `member_forces_table.py` records this exact defect class as already learned
cmd    sed -n '138,144p' scripts/measure/member_forces_table.py
out    "STATED HERE, BY THE CALLER, because `floatfea.post.forces_table` no longer carries
        it (R805 / FN0): A MODULE CONSTANT THERE SILENTLY OVERRODE A CONFIGURED SCALE."
       then, seven lines later:  WAVE_HEIGHT_FULL_M = 24.2
       with the docstring  """The DS1 design wave at full scale, `0.484 m` model times the
       Froude factor."""   -- a DERIVATION stated in prose and performed by hand. CW0.
judge  R805/FN0 is `lambda`; this is `H`. The same shape, in the same file, one constant
       apart, with the lesson written between them.
```

**And the mitigation, stated honestly rather than inflated, exactly as my predecessor stated R896's.** The shipped sidecar records `wave_height_full_m = 24.2` and both literals are `24.2`, so **no committed artifact is wrong today** -- the regeneration check below is byte-clean and that is the control saying so. The defect needs a sidecar re-exported at a different wave height. **That is FT2.6's own work, in this step**: the multi-npz heading envelope means several dynamic-inputs files with their own recorded bases, and the first one recorded at a different `H` publishes a band table for `24.2 m`.

**Closed when** the full-scale wave height reaches every consumer from ONE place -- derived from the recorded model height and the already-validated lambda, or read from the validated recorded value -- so that `scripts/measure/f6_results_report.py` and `scripts/measure/member_forces_table.py` carry no independent literal for it. **Three conditions:** (i) a test asserts the agreement, because `grep -rn "WAVE_HEIGHT_FULL_M" tests/` is empty today and a pass/fail cannot show where a value came from; (ii) the CALLER is held per FT2's standing rule -- the revert-red-restore cycle covers the two generators, not a helper; (iii) **the counter-case is my `model=1.0, full=50.0` row**, because it is inside `WAVE_HEIGHT`'s domain and consistent with lambda, so neither the existing bound nor R895's relation check reddens on it. If the single source is instead a literal that the sidecar is checked AGAINST, that comparison is a tolerance under another name and goes to `floatfea/tolerances.py` with its `_COUNTER` -- an exact equality is not, and is the cheaper repair.

---

**R903. (BLOCKS) THE REPAIR ROUTED THE FOUR `WAVE_BASIS_KEYS` AND LEFT FIVE RECORDED FIELDS AT THE SAME READER UNVALIDATED -- `lambda`, `rho_inf`, `dt`, `ramp_s` AND `hsp_tag`. `lambda` IS PUBLISHED IN THE SAME PRINTED SENTENCE AS THE TWO WAVE HEIGHTS THE REPAIR JUST PROTECTED, AND IT IS THE ONE FIELD WHOSE CONFIGURED COUNTERPART GENUINELY EXISTS: `FROUDE_LAMBDA = ("-", 1.0, 1000.0)` AT `config.py:196`. SO `RECORDED_BOUNDS`' ORIGINAL JUSTIFICATION IS LITERALLY TRUE OF THE ONE KEY THAT IS NOT IN IT.**

The turn declared this and asked me to probe it. I probed it, and it is worse than "not routed": the field it leaves out is the one the entry's own stated reason fits.

```
claim  five recorded numeric fields reach the deliverable from the raw block
cmd    grep -n "run\[\|prov\[" scripts/measure/f6_results_report.py
out    :282  run = {**prov["run"], **basis}
       :405  prov['hsp_tag']        :408  run['lambda']
       :412  run['rho_inf']         :413  run['dt'], run['ramp_s']
       :424  run["periods_full_s"]
       -- `basis` covers heading_deg, wave_height_full_m, wave_height_model_m and window.
          The other five arrive RAW.
cell   ONE VARIABLE MOVED each time, the REAL generator, the shipped example otherwise
out    lambda = -50.0        EXIT=0  "24.2 m (0.484 m model, Froude lambda = -50.0)"
       lambda =   0.0        EXIT=0  "... Froude lambda = 0.0)"
       lambda =  True        EXIT=0  "... Froude lambda = True)"
       lambda = "fifty"      EXIT=0  "... Froude lambda = fifty)"
       lambda =   1e9        EXIT=0  "... Froude lambda = 1000000000.0)"
       rho_inf = -5.0        EXIT=0  "rho_inf = -5.0, dt = 0.01 s, ramp 10.0 s"
       dt      = -0.01       EXIT=0  "rho_inf = 0.8, dt = -0.01 s, ramp 10.0 s"
       ramp_s  = False       EXIT=0  "... ramp False s"
       hsp_tag = True        EXIT=0  "provenance tag           : True"
cmd    does the configured side bound `lambda`, and does the PRODUCTION path?
out    config.py:196  FROUDE_LAMBDA: Final[Bound] = ("-", 1.0, 1000.0)
       config.py:733  froude_lambda=_checked(lam, ..., FROUDE_LAMBDA)
       pipeline.py:961-981  the RECORDED lambda is cross-checked against the CONFIGURED
       one and a mismatch is refused by name -- so `floatfea run` is protected by the
       comparison, and the generator has no config to compare against at all.
rule   FR1's first limb with EZ0; and `RECORDED_BOUNDS`' own surviving sentence, which
       after this diff still reads that a recorded value is checked against "the same
       bound its CONFIGURED counterpart gets in `config.py`"
judge  **IT BLOCKS. THE SILENTLY WRONG RESULT IT PRODUCES:**
       `results/F6/floatfea_results_report.md` carrying
       `wave height, full scale  : 24.2 m (0.484 m model, Froude lambda = fifty)` -- or
       `-50.0`, or `0.0` -- at exit 0, in the SAME SENTENCE as two numbers the same
       commit made refusable, from a sidecar whose other fields the same reader now
       validates. A reader of that line cannot tell which of the three numbers in it was
       checked. **And `lambda` is not decorative in that sentence: it is the factor that
       makes the model and full heights mean the same sea state**, so a wrong lambda
       there misstates the relation R895 exists to police. The mitigation is R896's and I
       state it the same way: R756's gate means the bad number reaches the committed file
       only through a human regeneration, which is the step the gate's own message asks
       for.
```

**Closed when** every recorded numeric field this generator PUBLISHES has a declared domain -- which is `6e24b44`'s own subject line, "every recorded numeric field has a declared domain", applied at the reader that writes the deliverable. **`lambda` at minimum**, because its bound already exists and is already applied to the configured side, which makes it the one entry `RECORDED_BOUNDS`' stated reason covers without amendment. For the others, either a bound or a sentence saying why a published recorded number needs none. **And the counter-case is the ROW, not the field:** `Froude lambda = fifty` must redden an assertion in the same quantity, because a type check on `dt` is evidence for a different test.

---

**R904. (DOES NOT BLOCK -- FF0-class; fix it in the next commit) THE REPAIRED ASSERTION IS TWO SCALAR COMPARISONS WHERE THE CLOSING CONDITION SAID "EVERY COPY THE HARNESS WILL MAKE". I RESOLVED THE HARNESS AT TEN MARKER/VERDICT-STEP CONFIGURATIONS AND IT IS BLIND ON THREE OF THEM -- ONE OF WHICH IS R897's OWN `src == dst` -- WITH BOTH NEW ASSERTIONS READING `True` IN ALL THREE.**

This is the half of R897 the condition named and the repair did not reach, and it is the third occurrence in this file of the same shape: *the collection the assertion inspects cannot contain the failure.*

```
rule   the previous verdict's `Closed when`, verbatim: "the assertion's third property is
       stated over EVERY COPY THE HARNESS WILL MAKE rather than over the one pair its
       author had in mind: for each entry in `STATES`, each `copy2`'s resolved source
       exists and differs from its destination"
cmd    what shipped (tests/test_report_guard_states.py:851-861)
out    assert NEXT != STEP ; assert NEXT != VERDICT_STEP
       -- two scalars. `STATES` is not enumerated, `copy2`'s resolved paths are not
          checked, and the REPORT source's existence is checked while the VERDICT
          source's is not.
cell   the harness RESOLVED at ten (marker, reports, reviews) configurations in a
       disposable worktree, enumerating every `copy2` and every `mkdir` plant per state
out    LIVE      marker=3 rep{1,2}   rev{1,2,3}  -> STEP 2 VS 3 NEXT 4   clean
       EQUAL     marker=2 rep{1,2}   rev{1,2}    -> STEP 2 VS 2 NEXT 3   clean
       V<S       marker=3 rep{1,2,3} rev{1,2}    -> STEP 3 VS 2 NEXT 4   clean
       V>S+1     marker=2 rep{1,2}   rev{1..4}   -> STEP 2 VS 4 NEXT 5   clean
       MARKER_AHEAD marker=4 rep{1,2} rev{1,2,3} -> STEP 2 VS 3 NEXT 4   clean
       STEP9     marker=9 rep{9}     rev{9}      -> STEP 9 VS 9 NEXT 10  clean
       -- and the three that are not:
       NO_REVIEWS   marker=2 rep{1,2} rev{}      -> STEP 2 VS 2 NEXT 3
         SRC-MISSING docs/reviews/R1/step-2.md on report_file_is_a_directory,
         two_digit_step_number_discriminating,
         zero_padded_step_number_beside_the_unpadded_one
         -- `_verdict_step()` falls back to `STEP` when no review file exists, so
            `copy_verdict` reads a file that is not there. THREE states die in `_build`
            on `FileNotFoundError`, which is R887's original failure verbatim. This is
            the first step of EVERY NEW MILESTONE, before its first verdict.
       STEP9V       marker=9 rep{9}  rev{9,10}   -> STEP 9 VS 10 NEXT 11
         SRC==DST docs/reviews/R1/step-10.md on two_digit_step_number_discriminating
         -- its destination is the LITERAL "10", not `NEXT`, so `NEXT != VERDICT_STEP`
            structurally cannot see it. **This is R897's own collision, at the one state
            whose name is about two-digit step numbers.**
       REP_AHEAD    marker=2 rep{1,2,3} rev{1,2} -> STEP 2 VS 2 NEXT 3
         DST-EXISTS docs/reports/R1/step-3.md on five states, and MKDIR-OVER-FILE on
         report_file_is_a_directory
         -- the plant lands on a report that already exists: `copy_report` silently
            OVERWRITES it, so "a newer report appeared" is built on a tree that already
            had one, and `mkdir` over the existing file is the `FileExistsError` the
            docstring this diff DELETED used to describe.
       -- **IN ALL THREE, `NEXT != STEP` is True AND `NEXT != VERDICT_STEP` is True.**
judge  **It does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none today** -- the
       live configuration is clean, measured above and in CI. It is FF0-class rather than
       ledgered because this harness is what decides whether a green here is believed,
       and under CZ0 (c) unamended it would have blocked; **I am ruling under FR1, which
       is in force, and saying which clause I ruled under rather than stretching it.**
       The reason it is worth a finding rather than a line: `NEXT` was wrong twice and
       both repairs were correct about the numbers their author was looking at. A
       predicate over `STATES` cannot be wrong that way, and the condition asked for one.
```

**Closed when** the third property is stated over the COLLECTION rather than over two scalars: for each entry in `STATES`, each `copy2`'s resolved source exists and differs from its destination, and each plant's destination does not already exist. That is one loop inside an assertion that already exists -- EK2, fixed not extended, and no new apparatus. The `"10"` literal in `two_digit_step_number_discriminating` is then either covered by that loop or derived from `NEXT` like its siblings.

---

**R905. (DOES NOT BLOCK -- ledgered as prose) R895's REPAIR REPLACED ONE UNVERIFIABLE ABSENCE CLAIM IN `floatfea/` WITH ANOTHER, AND ADDED TWO FIGURES WITH NO COMMAND. CW0 SAYS A CLAIM ABOUT THIS REPOSITORY IN A DOCSTRING IS A TEST, A TRIPLE, OR DELETED.**

```
claim  the new docstring states an absence and two measurements, and carries neither a
       needle nor a command
cmd    sed -n '689,711p' floatfea/run/pipeline.py
out    "It is false for `wave_height_model_m`, which **has no configured counterpart at
        all** -- no declaration anywhere expresses a model-scale wave height."
       "at `lambda = 50` the declared model headroom is `207x` where the legal headroom
        is `4.1x`, and `FROUDE_LAMBDA` admits `lambda` up to `1000`."
       -- an absence over the whole configuration schema, and two ratios.
cmd    are the figures right? (I checked rather than assumed)
out    100/0.484 = 206.61... -> `207x` correct;  2.0/0.484 = 4.132... -> `4.1x` correct;
       config.py:196 FROUDE_LAMBDA = ("-", 1.0, 1000.0) -> `1000` correct.
judge  **It does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- every figure
       in it is correct at this commit and I verified all three. It is ledgered because
       the absence claim is the kind CW0 exists for: the previous version of this same
       paragraph was a false claim about the configured side, R895 is what that cost, and
       the repair is a new claim about the configured side with nothing that would refute
       it. `tests/prose_triple_controls.txt` is the mechanism this tree already has.
```

**Closed when** the absence is a `claim:`/`cmd:`/`out:` triple with a needle that `tests/prose_triple_controls.txt` plants a line for, or the paragraph says only what a reader can check in the file in front of them. The two ratios belong in the step report, which is regenerated by rule.

---

**The standing criterion observation, not a new one, with this round's number.** The predicate reads "a finding or a site of **the newest verdict**". Measured strictly, per id, at this commit against the newest verdict's 56192 characters: **49 of the 57 finding ids and 327 of the 339 site ids satisfy limb one literally**; 20 do not, and they are the ids of eight findings of EARLIER unanswered step-3 verdicts -- R851, R853, R857, R860, R872, R873, R874, R875. My predecessors measured the same quantity as 67, then 14, now 20, and the quantity moves because it is **a function of how exhaustively each verdict's own prose names earlier findings** -- which is R861's lesson applied to the predicate itself. I followed my predecessors' reading, a finding or site of a verdict with no answering report revision, under which **0 of 408 block**. **This is said once and it is already said: the escalation is open and belongs to Xabier, not to another round.**

## CI at the reviewed commit: the run EXISTS, it COMPLETED, the ladder is GREEN, the guards step is RED

**`gh run list --commit 57cfae6` returns an empty list and the run EXISTS** -- CK2's third state does NOT apply: run **40265555791** has real jobs, real steps and real durations, and the allowance is not exhausted. **It was `in_progress` when I began and `completed / failure` when I read it, and I waited rather than recording a conclusion I had not seen.**

```
job  the verification ladder      SUCCESS   (ladder 1, 2, 3, 4, 5 and 6 all SUCCESS)
job  lint, unit and guards        FAILURE
     Set up job / checkout / setup-python / pip install  SUCCESS
     actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
     unit tests SUCCESS / guards and meta-tests FAILURE
     -- every step RAN. Nothing was skipped behind an earlier red, which is what
        CZ1 (iii) exists to see, and FP1's CI-only types-PyYAML red has stayed fixed.
job  CI determinism -- leg        skipped
job  CI determinism -- ten legs   skipped
```

**TWO INDEPENDENT RUNS AGREE ON THE ID SET, NOT MERELY ON THE COUNT.** CI: `408 failed, 1109 passed, 1 skipped, 1 warning in 631.88s`. Mine: `408 failed, 3695 passed, 1 skipped, 2 warnings in 1210.93s`. `comm -3` between my 408 sorted ids and CI's 408 is **(empty)** -- the same tests, on two operating systems. `git status --porcelain` is empty before and after, which is also the control saying my probes did not leak.

The 408, each id tested against the FS1 predicate AS NARROWED BY FT1, per id and not by family:

```
339  test_every_named_site_is_touched_or_declared[<finding>-<path>[:line]]   limb one.
       Every finding prefix lies in R850..R899, all findings of step 3's ten interim
       verdicts, none of which has an answering report revision. 327 of the 339 also
       satisfy the STRICT reading; the 12 that do not are R851's and R853's eight
       `tests/regression/test_r1_example_regenerates.py` lines and four siblings.
 57  test_the_report_carries_the_finding[R845..R901]   limb one -- each NAMES a finding.
       49 satisfy the strict reading; 8 do not (R851, R853, R857, R860, R872-R875).
  1  test_the_CI_section_is_about_the_REVIEWED_commit   limb one -- keyed on a CI section
       that cannot exist until a step-3 report does
  1  test_the_Carried_table_is_what_the_generator_produces   limb one, same premise
  1  test_the_generator_would_catch_a_row_under_the_wrong_number  limb one, that
       generator's own control, same premise
  1  test_the_report_carries_a_WHOLE_SUITE_count   **LIMB TWO under FT1** -- its subject
       IS the commit carrying it: suite_count.py measures a clean worktree AT a commit,
       so the line naming a sha cannot be inside that sha
  1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  **LIMB TWO under FT1** -- no run
       exists for a commit before it is pushed
  7  test_the_guard_survives_the_state[baseline,
       verdict_amended_after_the_commit_the_report_answers, non_numeric_step_suffix,
       superscript_digit_step_number, draft_suffix_beside_a_step_report,
       step_number_is_the_empty_string, zero_padded_step_number]
       limb one, and I read each state's REQUIREMENT rather than ruling them as a family:
       **2 are require=green** (baseline, verdict_amended...) and **5 are
       require=ignored**, which also asserts exit 0. All seven need a CLEAN nested run,
       and no nested run can be clean while the 401 above exist. Boundary consequence.
---
408  **NOT ONE FAILS THE PREDICATE.** R897's two ids -- report_file_is_a_directory and
       zero_padded_step_number_beside_the_unpadded_one -- are GONE from both sets, and
       newest_report_has_no_verdict_yet went green as well: 10 harness reds became 7.
       The growth from 351 to 408 is entirely in `test_report_carried.py`'s
       parametrisation over the newest verdict's own findings and sites (286->339 sites,
       50->57 findings), which is R861's measurement and not a new red.
```

**EG3(i) is satisfied by the trace above, and by the control my predecessor built, which I re-ran:** the two formerly-blocking ids go red and green at the SAME commit under a one-line change to `NEXT`, with nothing written to `docs/reports/` or `docs/reviews/` -- `3 failed in 2.59s` against `3 passed in 30.86s`, the third being the assertion itself. A boundary red cannot be cleared by a change to the harness. These were, so their cause was the harness; it is now fixed and they are green on both machines.

## Corpus (EG4(e))

**THE PAUSE HELD. I added no entries and committed nothing to `tests/corpus/`.** Batches are paused until 28 October except mutation work on F4's load-mapping gate and EB6's label-provenance gate; this diff touches neither. **0 entries are new this round, so there is no caught-of-new count to report**, and I say that rather than quoting a coverage figure I did not measure.

**What I ran instead -- the recorded substitute, and BOTH halves produced findings for the fourth round running:**

* **A continuum grid over the parameter space the decision rules guard.** Three rules, three spaces, 37 cells, every one in a disposable worktree I then removed:
  - **The recorded sidecar through the REAL generator, 27 cells.** **This produced R902 and R903.** `lambda` at `{-50, 0, True, "fifty", 1e9}`, `rho_inf = -5`, `dt = -0.01`, `ramp_s = False`, `hsp_tag = True`, all nine at EXIT=0 with the value published; the two heights at `{(1.0, 50.0), (0.3, 15.0)}` self-consistent and legal, both publishing a band table for `24.2 m`; the three basis keys dropped, giving `KeyError` at exit 1 rather than a publication; `window` dropped, giving the PARTIAL refusal by name; `heading_deg = 450`, refused by name.
  - **EH4 at the NEW call site, in BOTH directions, because the repair put a new caller behind an unmoved bound.** The injection rising: `full = 100.1` and `full = -1e-9` both refuse, `out_written=False`. **The direction that WEAKENS the gate:** the ceiling falling to `24.19` TRIPS THE CLEAN CASE and falling to `24.3` does not -- so the shipped `24.2` is pinned within `0.1 m` from above at the generator door too, and **the assertion is not vacuous there, which I measured rather than inferred from the pipeline door.**
  - **The harness resolved at ten marker/verdict-step configurations, 10 cells. This produced R904**, and six of the ten are clean, which is the half that says the repair is right where it was aimed.
* **One-at-a-time ablation of each repair, 3 cells.** The generator's call removed -> `1 failed, 20 deselected`, the one being `test_R896_the_GENERATOR_refuses_a_sidecar_the_run_reader_refuses`; restored -> `1 passed, 20 deselected`. **The turn's figures reproduce EXACTLY.** `NEXT` reverted to `STEP + 1` -> `3 failed in 2.59s`; restored -> `3 passed in 30.86s`.
* **A regeneration check on a published deliverable: RUN, and CLEAN.** Both producers moved in this diff, so the check can differ. `scripts/measure/f6_results_report.py` at `57cfae6` against the committed `results/F6/floatfea_results_report.md`, compared on decoded text: **28 differing lines out of 464, and every one of the 28 is the `--no-gates` effect** -- the eight gate rows' status column and the `pytest's own summary` block. **Every other line, and every number in them, is identical.** That is the control saying R896's repair moved no published figure, and also how I know R902's two literals and the recorded value agree TODAY.
* **The harness's own measuring capacity, since R904 is about it.** Of the 46 entries in `tests/corpus/report_guard_states.txt`, 22 are built as states and 24 await transcription. Of the 22: **8 require a clean nested run and 7 of those are red** (one went green), 12 pass on `assert code != 0` which the 401 boundary reds satisfy whatever the plant does, and **0 die in `_build`** -- which is the number that moved. Last round it was 2, and 2 was R897.

Neither half would have come from reading the diff. R902 lives at a sidecar nobody wrote, R903 at fields the diff deliberately left, and R904 at a marker pair that does not exist today.

## Tolerances touched

**None.** `git diff 6e24b44..HEAD -- floatfea/tolerances.py` is empty, and so is `git diff 6e24b44..HEAD -- floatfea/run/config.py`, so `HEADING` and `WAVE_HEIGHT` are unmoved at `("deg", 0.0, 360.0)` and `("m", 0.0, 100.0)`.

**And nothing in the diff is a tolerance under another name, which I checked rather than assumed.** `RECORDED_BOUNDS` gains no key and loses none; the only change to it is prose. `wave_basis_from_sidecar` introduces no number. The harness change is one `max()` and two scalar comparisons. The new regression test compares for refusal and for a published substring, not against a threshold. The only numerals added anywhere in the diff are line numbers, step numbers, the two ratios R905 is about, and `-24.2`/`-0.484` as inputs to a refusal.

**R895's repair is still the one place a tolerance may be needed, and R902 narrows that.** If the full-scale height is DERIVED from one source, neither R895 nor R902 needs an epsilon. If either is instead a comparison between two independently maintained numbers, that comparison is a tolerance under another name, goes to `floatfea/tolerances.py` with its `_COUNTER` -- the smallest inconsistency the same assertion in the same quantity detects -- and re-locks R1 section 4's "None expected" in the same commit (DK0). **An exact equality is not a tolerance and is the cheaper repair for both.**

## Next step opens when

**This is a HOLD on step 3, which stays open. It is the tenth interim check, it counts against no round, and all three reviewed revisions remain available -- 0 of 3 spent.**

**R904 is answered in the NEXT commit, with R898.** That is FF0's own wording for this class, not my preference, and the two are one file each and one loop and one expression between them. The conditions are measured, so there is nothing to interpret: the third property is stated over `STATES` -- for each entry, each `copy2`'s resolved source exists and differs from its destination, and each plant's destination does not already exist -- and it goes red at my `NO_REVIEWS`, `STEP9V` and `REP_AHEAD` configurations, which is the check that it is no longer blind. `closed_by_a_pass` reads `^Closes:` with a frozen `pre_fk1` list beside `pre_gating`, and the function's name says which of the two it reads. The full-file count stays at `7 failed, 17 passed` or better with the marker left at 3, and all four `_build` death greps stay at `0`.

**Then R902, R903 and R895 together, as ONE repair on ONE quantity.** They are the same defect at three distances from the sidecar -- a literal, an unrouted field, and an unpoliced relation -- and splitting them repeats the shape that produced R866, R877, R881 and R896: a correct, tested check that one of the callers does not use. The conditions are in their own `Closed when` paragraphs. **The parts I will test myself** are that `model=1.0, full=50.0` is a row in a test (because it is legal under every bound and consistent with lambda, so nothing in the tree reddens on it today), that `Froude lambda = fifty` reddens an assertion in the same quantity, and that `grep -rn "WAVE_HEIGHT_FULL_M" tests/` is no longer empty.

**R882-R886 now have ONE place left and the trigger has been spent twice.** They are declared by name in step 3's first reviewed revision -- each with what was left and why -- or they are taken. R882's declaration has to carry my correction: the route its wording names is closed, so the sentence is wrong in the opposite direction now.

**Then FL2, in FT2's order, and nothing in this list displaces it.** FT2.3's period-band check is unbuilt and **R902 is now the strongest argument for building it next**: the band and steepness columns are the thing FT2.3 generalises, and they are computed from a literal. R867-R869 are FT2.7. R891, R892, R899, R900, R901 and R905 are sentences, and R899's repair is a `process:` commit whose trigger is the first witness invocation on R1.

**R880 still waits**, and for the fifth round running it did not misdirect me: I ruled under `CLAUDE.md`'s predicate as FT1 narrowed it, per id, over all 408. Do not take it first.

**What I did NOT ask for.** No new guard, scanner, meta-test, detector or report generator. R904 and R898 are repairs to existing apparatus under EK2 -- one loop and one expression. R902 and R903 call validators the tree already has, from places that already read the sidecar. Everything else is a sentence. `docs/milestones/F2a.md` is where anything larger goes.

**Schedule, since FT3 asks for it at every reviewed revision and the turn reported slippage on the day it was known.**

**The slippage is reported correctly and I am not re-escalating.** FS4's 26 October checkpoint does not hold; the turn says so today, which is what `CLAUDE.md` asks, and FR0 already answered the escalation with "slip the date, keep the scope". Three observations, each a measurement:

1. **The turn's estimate has now moved EARLIER twice while the calendar moved later, and the second move is larger than the first.** 17 November, then 12 November, and FT2.3 through FT2.7 are unbuilt at both readings -- `git diff --stat 6e24b44..HEAD -- floatfea/model floatfea/solve` is empty and the only `floatfea/` change in three commits is one function and one docstring. I am not ruling on a figure in a message (R890's rule, which I am keeping), but an estimate that improves on no new evidence about the work is the shape the last three checkpoints had.
2. **This is the fourth consecutive round in which the finding came from RUNNING something rather than reading it, and the second in which `scripts/measure/` carried it.** R887 then R897 then R904; R896 then R902 and R903. The cost is not the repairs -- R902's and R903's are each a handful of lines -- it is that four rounds have now been spent on apparatus and on the two `scripts/measure/` readers while FT2.3 through FT2.7 have not started.
3. **The risk my predecessor concentrated in FT2.4 and FT2.5 is now measured twice over, and it has moved up to FT2.3.** R896 was one `scripts/measure/` reader publishing an unvalidated recorded number; R902 and R903 are the same reader publishing four more, one of them a physics verdict. **FT2.3 is the period-band check, which is exactly the computation R902 found wrong**, so the item that was third in the order is now the one whose surface is known to be defective. I would do FT2.3 before FT2.6 and fold R902's single-source repair into it, because they are the same change, and I would still load FT2.4 and FT2.5 by more than x1.5.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 6e24b4432ab023e0a0c02c6320120e930d5b91c7
**Reviewed commit: `6e24b4432ab023e0a0c02c6320120e930d5b91c7`.**
Verdict: HOLD
Tests: 3676 passed, 351 failed, 1 skipped, 2 warnings in 1211.45 s (0:20:11)   (my own whole-suite run at the reviewed commit, `-p no:randomly`, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the ninth in step 3.** There is still no `docs/reports/R1/step-3.md`, so no reviewed revision has been consumed -- **0 of 3** -- and this counts against no round.

**THREE FINDINGS BLOCK: R895, R896 and R897.** Two of them are one defect at two doors on the
same quantity, and the third is the half of R887 that its closing condition named and its
repair did not reach. **R881 itself is ANSWERED and the repair is good** -- I reproduced both
of its revert cells exactly and added three more, and the published deliverables regenerate
byte-clean. The hook commit `8ee62f6` deletes no guard and is **not a STOP**; I measured that
rather than read it. Both of the turn's withdrawals reproduce and I accept them. The two
questions the turn asked are ruled below under their own heading, and on the second one the
turn's proposed next commit is **wrong as stated** -- I measured two configurations it does
not catch.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For R895 and R896 I name the silently wrong result, as FR1's last
sentence requires. **R897 blocks under CZ1 (iv) with EG3's predicate and FF0, not under FR1's
head**, and I name the clause rather than stretching FR1 to fit -- which is what my
predecessor did for R887 one round ago, in the same file, for the same reason.

```
cmd    git log --oneline cd126a6..HEAD ; git diff --numstat cd126a6..HEAD
out    6e24b44 ece0ebe 8ee62f6 c3bf24f -- FOUR commits.
       .claude/hooks/require-verdict.sh 15/2 | docs/milestones/F2.md 14/3 |
       docs/milestones/R1.md 18/0 | floatfea/run/pipeline.py 52/24 |
       tests/test_report_guard_states.py 84/1 |
       tests/unit/test_headings_and_bem_coverage.py 60/0 |
       docs/reviews/R1/step-3.md 659/0  (my own previous verdict)
cmd    git diff cd126a6..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff cd126a6..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py        -- a file, as my instructions say it must be
cmd    git diff --numstat cd126a6..HEAD -- .claude docs/SUPERVISOR.md
out    15  2  .claude/hooks/require-verdict.sh      -- and NOTHING else
cmd    git diff --stat cd126a6..HEAD -- .claude/agents
out    (empty)   -- my own definition is untouched
cmd    git diff cd126a6..HEAD -- .claude | grep "^-" | grep -v "^---"
out    -for rep in docs/reports/F*/step-*.md; do
       -for r in $(ls docs/reviews/F*/step-*.md 2>/dev/null); do
       -- **THE ONLY TWO DELETED LINES IN `.claude/` ARE THE TWO NARROW GLOBS, each
          replaced by a wider one. NO GUARD IS DELETED. NOT A STOP.** `8ee62f6` is a
          standalone `process:` commit citing R888/FT0's FF0 class whose only file is the
          hook; `c3bf24f` and `6e24b44` touch `tests/` and `floatfea/` and touch neither
          `.claude/` nor `docs/SUPERVISOR.md`. Measured per commit, not over the range.
cmd    git diff --stat cd126a6..HEAD -- results scripts/measure docs/reports
out    (empty)   -- no published deliverable FILE moved and no step report was touched (EK3)
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ;
         mypy floatfea     (at 6e24b44, clean worktree)
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 42 source files
cmd    git status --porcelain   (before anything, and after two worktrees, 17 bound cells,
                                13 CLI runs, 5 ablations, 2 NEXT cells and one regeneration,
                                every one of them in a disposable worktree I then removed)
out    (empty) / (empty)
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** `ls docs/reports/R1/` is
`step-1.md step-2.md` and their two answers files, so there is no `Answers: verdict N @ <sha>`
header to compare against the newest verdict. The newest report revision in the tree is still
step 2's third, and **nine verdicts are now newer than it.** That is EG3 state (2) and it is
the cause of 341 of this tree's 351 reds -- but not of all of them, which is R897.

**R855's standing condition is MET, and more than met.** `6e24b44`'s message says plainly
"NO WHOLE-SUITE FIGURE IS CLAIMED HERE", names exactly what it did run, and says why an
earlier run was void (it overlapped the revert cycle). That is the right answer and it is
the second time this step has been given.

## The questions the turn asked

### 1. Was it right to split the lambda half out of `6e24b44`? YES, AND THE RULE REQUIRES IT

```
claim  a relative epsilon on `model * lambda == full` is a tolerance under another name, so
       it cannot ride along beside the code change it holds in place
rule   `CLAUDE.md` section Tolerances -- "The same rule applies to anything that functions as
       a tolerance under another name: convergence thresholds, COMPARISON EPSILONS, 'small
       number' guards ... and any factor introduced to make two numbers agree"; and "A
       tolerance change in the same commit as the code change it rescues will be rejected in
       review"
cmd    grep -n "None expected" docs/milestones/R1.md ; sed -n '395,404p' docs/milestones/R1.md
out    section 4 Tolerances: "**None expected, under FM0.**" and "the config's ranges are
       declared validation bounds" -- so R1's locked plan says the config ranges are NOT
       tolerances (which is why `WAVE_HEIGHT` belongs in `config.py` and I raise nothing
       about its location) and ALSO says no tolerance is expected in this milestone
judge  **THE SPLIT WAS RIGHT AND I WOULD HAVE BLOCKED ON THE ALTERNATIVE.** A relative
       epsilon folded into `6e24b44` would have been a tolerance in the same commit as the
       code it rescues, which `CLAUDE.md` says is rejected. It also needs a plan line,
       because R1 section 4 currently says no tolerance is expected -- so the commit that
       introduces one re-locks that row (DK0: a re-lock does not restart the round count,
       and this step has spent none of its three). The turn reached the right answer for a
       reason it only half-stated, and the full reason is the Tolerances section, not FT2.3's
       wording.
```

### 2. Is the lambda-scaled bound ALONE the correct next commit? NO -- IT CATCHES ONE OF THREE

This is the one place I disagree with the turn, and it is a measurement and not a reading.
Three sidecars through the real CLI, one variable moved each time, every number below read
out of the artifacts the run wrote.

```
rule   the proposed next commit as the turn states it: `wave_height_model_m` gets its own
       ceiling, `WAVE_HEIGHT[2] / lambda` = 2.0 m at the shipped lambda = 50
cmd    floatfea run on the shipped example with the sidecar's `run` block mutated, outputs
       redirected to a scratch directory, at 6e24b44 in a disposable worktree
out    B  model=100.0  full=24.2   EXIT=0
          report.md     * **wave height** - 24.2 m full scale (100.0 m model)
          BOTH CSVs     # wave basis: heading 0.0 deg; H_full 24.2 m; H_model 100.0 m
          -- the proposed bound CATCHES this one (100.0 > 2.0)
       C  model=0.484  full=2.0    EXIT=0
          report.md     * **wave height** - 2.0 m full scale (0.484 m model)
          BOTH CSVs     # wave basis: ... H_full 2.0 m; H_model 0.484 m
          -- **the proposed bound MISSES it.** The model value is legal; the FULL one is the
             wrong number, and 0.484 m at lambda = 50 is a 24.2 m wave, not a 2.0 m one.
       D  model=1.9    full=24.2   EXIT=0
          report.md     * **wave height** - 24.2 m full scale (1.9 m model)
          BOTH CSVs     # wave basis: ... H_full 24.2 m; H_model 1.9 m
          -- **the proposed bound MISSES it too**: 1.9 <= 2.0, and the pair is off by 3.9x
judge  **ONE OF THREE.** A ceiling on one member of a pair cannot police a relation between
       them, and two of the three configurations I tried put the defect where the ceiling
       cannot see it. The load-bearing form here is the RELATION, not the bound -- which is
       my own instructions' "State bounds, not identities" read in the direction it is
       usually read backwards: the inequality is the weaker proxy and the identity is the
       thing that holds. The bound is worth having as a FLOOR beneath every lambda (R694's
       own repair shape, a constant demoted beneath the closed form), but shipped alone it
       would publish "the recorded pair is checked" when one third of it is.
```

**And there is a repair that needs no tolerance at all, which I name because R1 section 4
says none is expected.** `scripts/export_f4_dynamic_inputs.py:526` already writes
`wave_height_full_m` as `WAVE_HEIGHT_MODEL_M * LAMBDA`: the pair has one degree of freedom
by construction. A reader that DERIVES one number from the other and the already-validated
lambda cannot publish an inconsistent pair, needs no epsilon, and is the same "ONE SOURCE
FOR THE SCALE" discipline `pipeline.py:916` already states for lambda itself. The property
the repair must have is what I will measure, not which of the two routes it takes:
**one of the two published numbers is derived from the other, or the pair is checked against
lambda.** The epsilon route is legitimate and needs the plan row; the derivation route is
legitimate and needs a sentence in the report saying the published full-scale height is
derived rather than recorded, because a reader of `report.md` is told it is the recorded
basis.

### 3. Marking F2's retired premise in place: RIGHT CALL, and the census still finds it

```
claim  marking in place keeps the record, removes the CW0 defect, and does not blind the
       census that found it
cmd    grep -c "advanced in the commit" docs/milestones/F2.md ; grep -c "not before"
         docs/milestones/F2.md ; grep -c "RETIRED BY DIRECTIVE FT0" docs/milestones/F2.md
out    1 / 1 / 1   -- the sentence is quoted VERBATIM, so R893's own needle still finds it,
       and it now finds it labelled with the directive that retired it
judge  **RIGHT.** F2 is closed and its plan is a record; moving the sentence elsewhere would
       have left a reader who finds F2's convention section finding nothing, and deleting it
       would have destroyed the record of what the rule was. Quoted, attributed, and
       superseded in place is the form that satisfies both CW0 and the record. I would have
       objected only if the quotation had been paraphrased, because then the census that
       catches the next occurrence would no longer match it. It is not paraphrased.
```

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R887** (15 of 23 negative-control states die in `_build` before planting) | **PARTLY ANSWERED, STILL OPEN -- see R897** | `c3bf24f`. The `FileNotFoundError` half is CLOSED and I confirmed it on a machine neither of us controls: CI run 40260335508's own log has `grep -c FileNotFoundError` = **0**, and the `_step()` resolver now agrees with the guard (`STEP == guard.STEP == 2`), asserted rather than promised. The condition's FIRST clause -- "so that no state dies in `_build`" -- is NOT met: two states now die there with `shutil.SameFileError`. Half of an item is not the item. |
| **R888** (the orphan sweep globs `F*`) | **ANSWERED** | `8ee62f6`, both sites. The old glob sees 14 review files; the new one sees 17, the three new ones being R1's. The label guard at `:129` admits one uppercase letter, digits and an optional suffix, so the glob and the label guard cannot disagree about what a milestone is. And it opened R898. |
| **R889** (the deadlock "had absorbed seven interim checks") | **WITHDRAWN BY THE TURN, AND THE WITHDRAWAL IS CORRECT** | I re-took the cell myself. `git log --reverse --format="%h %ad %s" --date=short 8542d79..HEAD -- floatfea tests` gives eleven commits, and each of the seven interim checks sits at a turn boundary carrying new implementer commits, so ES0 forces one regardless of the hook's message. The withdrawal is not itself wrong. |
| **R890** ("two FL2 items and five repairs to those two") | **WITHDRAWN BY THE TURN, AND THE WITHDRAWAL IS CORRECT** | same log: `d3306a6` FL2(a) and `cadbbf7` FL2(c) are the two items; `e945b13`, `ff48a6d`, `154261e` are the **three** repairs to them; `e818375`, `e6a20e3`, `d89566d` are earlier in history than both items and cannot be repairs to them. The corrected figures reproduce exactly. |
| **R891, R892** (replay 1's void paste; the control that moved two variables) | **still open, untouched** | ledger items, FR1's third class. Neither is in this diff. |
| **R893** (F2.md states FT0's retired premise as a live rule) | **ANSWERED** | `ece0ebe`, marked in place; ruled above under question 3. |
| **R894** (R1's step-3 gate row omits FT2.6 and FT2.7) | **ANSWERED** | `ece0ebe`. A grep for the two item numbers and the directive gives 5 at this commit against 0 at `HEAD~1`; both items and FT2's caller rule are in the row. |
| **R881** (two recorded wave heights get two of three checks) | **ANSWERED, and it produced R895 and R896** | `6e24b44`. Both of the turn's revert cells reproduce EXACTLY (`14 failed, 53 passed`; `1 failed, 66 passed`, the one being the caller test), the three published deliverables regenerate byte-clean, and the bound is pinned within 0.09 m above and 1e-10 below. See the corpus section. |
| **R882, R883, R884, R885, R886** | **ALL FIVE STILL OPEN, AND THE PREFERRED TRIGGER HAS NOW BEEN SPENT** | my predecessor routed these to "the next commit that touches `_validated_wave_basis`, **or** into the first reviewed revision as declarations of what was left and why". `6e24b44` IS that commit and none of the five was taken; its message does not name them. The second half of the disjunct is still open, so this is not a breach -- but it is now the ONLY remaining place. All five re-measured live at this commit: `pipeline.py:595` still routes a reader from the refusal to the publication (R882); `:732` still claims `10**400` "is caught before `float()` raises" when `float(value)` at `:756` is where it raises (R883); a `run` block that is a list still yields an empty `present` and publishes "NOT RECORDED" at exit 0 (R884); `HEADING`'s raw `0..360` still refuses a legally signed `-90` (R885); `tests/unit/test_headings_and_bem_coverage.py:35` still carries the blanket `# noqa: F401` (R886). |
| **R867, R868, R869** (eight topologies, one runs) | **still open, and now IN THE PLAN** | FT2.7 is in the step-3 gate row as of `ece0ebe`, which is R894's repair. The `floatfea/model` and `floatfea/solve` diffs since `cd126a6` are empty. They remain blocking by name into the first reviewed revision. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a)) | **still open** | the `pipeline.py` diff is R881's loop and nothing else; no topology code moved. |
| **R862** (three hand copies of the stage set) | **still open and STILL NOT DUE -- trigger re-measured, not taken on trust** | `git diff cd126a6..HEAD -- floatfea/cli.py` is EMPTY. It blocks in the commit that adds a timed stage, which is FL2 item 4 or 5. |
| **R863, R864, R865** | **all three still open, untouched** | the `tests/regression` diff since `cd126a6` is empty; R864's condition still needs a report revision that does not exist. |
| **R847 / C43, R848, R849 with R854** | **all still open, all correctly so** | `floatfea/cli.py` and `tests/regression` are untouched. FR1's second and third non-blocking classes. |
| **R852** | **ROUTED, not open** | FS3 ledgers it to FL3; `docs/directives/FS.md`. |
| **R880** (my own agent definition cites "their two corrected lists", which FS1 deleted) | **STILL OPEN, STILL CORRECTLY NOT TAKEN, and it did not misdirect me a fourth time** | `git diff --stat cd126a6..HEAD -- .claude/agents` is empty. I ruled under `CLAUDE.md`'s predicate as FT1 narrowed it and applied it PER ID to all 351 reds. **Do not take it first.** It did, however, point me at R899. |
| **R855** (a whole-suite figure at a commit carrying no report revision) | **condition MET, and the turn went further than the condition asks** | `6e24b44`'s message declines to claim a whole-suite figure and says why the earlier one was void. Mine is in the header, and it agrees with CI on 351 and on the id set exactly. |
| **R856** (the verdict tool refused a step with no report) | **ANSWERED, exercised a sixth time -- this file went through `--interim`** | `scripts/write_verdict.py`, untouched by this diff. |
| **R835, R836, R871** (EG3's lists; FS1's deletion of FC1's reason) | **ANSWERED, and FT1's narrowing orphans nothing at this commit either** | the two limb-two ids are `test_the_report_carries_a_WHOLE_SUITE_count` and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`; both have their own commit as SUBJECT. Full per-id trace in the CI section. |
| **C45** (a mirror going stale) | **DOES NOT RECUR in this diff -- and it is LIVE in the one document FE1 did not clear. See R899.** | `CLAUDE.md`, `docs/SUPERVISOR.md` and `.claude/agents/` are all untouched by these four commits, so the diff introduces nothing. What the diff did not introduce, it also did not fix: a grep for FR1 in `docs/SUPERVISOR.md` gives **0**. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally in CI's own three forms AND on a machine neither of us controls** | mine above; CI run 40260335508, job `lint, unit and guards`, steps actionlint, ruff, black, mypy and unit tests all SUCCESS. |
| **C42, C44** | **mine, accepted, carried** | unchanged by this diff. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **EG3(ii): the verdict commit measured** | **DONE at `bd315a1` three rounds back and not redone -- and I ran a SHARPER control this round** | ES0's light scope. R897's cell clears two reds at the reviewed commit itself with no report and no verdict written, which separates the two causes without needing a second commit to compare against. |
| the suite-count line, and CZ1 (ii)/(iii)'s four outputs | **still owed, still structurally unpayable until step 3's report exists** | limb two of the predicate by construction; two of this round's 351 reds ARE it. |

## Findings

**R895, R896 and R897 BLOCK. R898..R901 do not.** No tolerance value moved, no conftest
moved, no published deliverable FILE moved, and nothing in the diff is a tolerance under
another name.

---

**R895. (BLOCKS) THE RECORDED WAVE-HEIGHT PAIR IS NEVER CHECKED AGAINST LAMBDA, AND
`WAVE_HEIGHT`'s `[0, 100] m` IS A FULL-SCALE DOMAIN APPLIED UNCHANGED TO A MODEL-SCALE FIELD.
THE MODEL SIDE'S CEILING IS VACUOUS BY EXACTLY LAMBDA -- 50x AS SHIPPED, UP TO 1000x AT
`FROUDE_LAMBDA`'s OWN CEILING -- AND `RECORDED_BOUNDS`' DOCSTRING JUSTIFIES IT WITH A
CONFIGURED COUNTERPART THAT DOES NOT EXIST.**

The turn found this itself, declared it, and asked me to rule. It blocks, and the half the
turn did not state is the one that makes the bound WRONG rather than merely incomplete.

```
claim  `WAVE_HEIGHT` bounds a FULL-SCALE quantity, and `RECORDED_BOUNDS` applies it to a
       MODEL-SCALE one, so one of its three entries has no configured counterpart at all
rule   floatfea/run/pipeline.py:682-696 -- "A recorded value is checked against the same
       bound its CONFIGURED counterpart gets in `config.py`, because the question both ask
       is identical"
cmd    grep -rn "WAVE_HEIGHT" floatfea/ --include=*.py ; sed -n '396,401p' floatfea/run/config.py
out    the ONLY configured use is config.py:931, `cases[i].H`, and `class WaveCase` reads
       "One regular wave: heading, height, period. **Full scale, SI.**"
       -- so `heading_deg` and `wave_height_full_m` have configured counterparts and
          **`wave_height_model_m` has none.** The docstring's stated reason is false for one
          of the three entries it covers, and it is the entry the bound is wrong for (CW0).
cmd    the vacuity, at its operating point rather than as a bare ratio
out    at lambda = 50 the declared model ceiling is 100 m; the full-scale ceiling implies
       100/50 = 2.0 m. The committed model height is 0.484 m, so the DECLARED headroom is
       207x where the LEGAL headroom is 4.1x. The factor is exactly lambda, and
       `FROUDE_LAMBDA` admits lambda up to 1000.
cmd    floatfea run, shipped example, outputs redirected, three mutated sidecars (the full
       grid is under "What I ran instead")
out    model=100.0 full=24.2 lambda=50   EXIT=0
         report.md          * **wave height** - 24.2 m full scale (100.0 m model)
         member_forces.csv  # wave basis: heading 0.0 deg; H_full 24.2 m; H_model 100.0 m
         utilisation.csv    # wave basis: heading 0.0 deg; H_full 24.2 m; H_model 100.0 m
       model=0.484 full=2.0 lambda=50    EXIT=0  -> "2.0 m full scale (0.484 m model)"
       model=1.9  full=24.2 lambda=50    EXIT=0  -> "24.2 m full scale (1.9 m model)"
       -- **THREE artifacts, not two.** Both CSVs carry the basis in a header comment.
cmd    does anything anywhere relate the two numbers?
out    `grep -rn "wave_height" floatfea/ scripts/` gives six live sites: the two
       `RECORDED_BOUNDS` entries, the two `WAVE_BASIS_KEYS` entries, cli.py:147-148 and
       cli.py:265-266 (both PUBLISH), and scripts/measure/f6_results_report.py:400-401
       (also publishes). **No site relates the two numbers, and no site relates either to
       lambda.** The heights are never used in a computation -- they are published only --
       so nothing downstream can notice.
rule   FR1's first limb, with EZ0
judge  **IT BLOCKS. THE SILENTLY WRONG RESULT IT PRODUCES:** `report.md` publishes
       `* **wave height** - 24.2 m full scale (100.0 m model)` and both CSVs publish
       `H_full 24.2 m; H_model 100.0 m`, at exit 0, for a sea state that cannot exist -- at
       lambda = 50 a 100 m model wave is a 5000 m full-scale wave. One of the two numbers is
       necessarily wrong, nothing says which, and the artifact prints the correct lambda
       beside them so the contradiction is readable only to someone who does the division.
       This is R694's shape inside the repair of R881: a constant that is right at the
       configuration the author chose.
```

**Closed when** one of the two published numbers is DERIVED from the other and the
already-validated lambda, or the pair is CHECKED against lambda -- and either way
`wave_height_model_m` no longer carries a ceiling taken from the full-scale quantity.
**Three conditions on the repair, and the third is the one the turn's proposal fails:**
(i) `RECORDED_BOUNDS`' docstring stops claiming a configured counterpart for a field that has
none, or the entry stops being `WAVE_HEIGHT` (CW0); (ii) the CALLER is held, per FT2's
standing rule -- the revert-red-restore cycle covers `exported_wave_basis`, not only the
helper; (iii) **the counter-case is the configuration the repair did not choose**, which means
at minimum my cases C (`model=0.484, full=2.0`) and D (`model=1.9, full=24.2`) are rows in the
test, because a ceiling on one member of the pair is green on both. If the repair takes the
epsilon route the entry is in `floatfea/tolerances.py` with its `_COUNTER` -- the smallest
pair inconsistency the same assertion in the same quantity detects -- and R1 section 4's
"None expected" is re-locked in the same commit (DK0).

---

**R896. (BLOCKS) THE SAME DEFECT AT A SECOND DOOR, AND IT IS THE ONE EZ0 NAMES BY NAME.
`scripts/measure/f6_results_report.py` READS THE SAME SIDECAR'S `run` BLOCK DIRECTLY, WITH NO
VALIDATION OF ANY KIND. THE NEGATED HEIGHTS THAT `floatfea run` NOW REFUSES BY NAME IT
PUBLISHES AT EXIT 0, INTO A SHIPPED DELIVERABLE THAT A REGRESSION GATE THEN CERTIFIES AS "A
REGENERATION OF THE CURRENT TREE".**

`6e24b44`'s subject is "every recorded numeric field has a declared domain". The claim is
wider than the repair.

```
claim  one sidecar, two readers, and only one of them has a domain
cmd    grep -n "prov\[\|run\[" scripts/measure/f6_results_report.py
out    :274  prov = json.loads(args.provenance.read_text(encoding="utf-8"))
       :275  run = prov["run"]
       :400  f"wave height, full scale  : {run['wave_height_full_m']} m "
       :401  f"({run['wave_height_model_m']} m model, Froude lambda = {run['lambda']})"
       -- it never calls `_validated_wave_basis`, `exported_wave_basis`, or `_checked`
cell   ONE VARIABLE MOVED -- the sidecar -- and BOTH readers run on it, at 6e24b44, in a
       disposable worktree I then removed
out    full= 24.2 model= 0.484   DOOR1 ACCEPTED   DOOR2 EXIT=0
         "wave height, full scale  : 24.2 m (0.484 m model, Froude lambda = 50.0)"
       full=-24.2 model=-0.484   DOOR1 **REFUSED** -- "`run.wave_height_full_m` is -24.2,
                                 outside the declared domain 0..100 m"
                                 DOOR2 **EXIT=0** --
         "wave height, full scale  : -24.2 m (-0.484 m model, Froude lambda = 50.0)"
       full= 24.2 model= 100.0   DOOR1 ACCEPTED   DOOR2 EXIT=0
         "wave height, full scale  : 24.2 m (100.0 m model, Froude lambda = 50.0)"
cmd    is that script live, and is its output a deliverable?
out    tests/regression/test_f6_deliverable_agrees_with_itself.py:235 sets
       GENERATOR = scripts/measure/f6_results_report.py, and
       test_R756_the_SHIPPED_report_IS_a_regeneration_of_the_current_tree compares
       results/F6/floatfea_results_report.md against a fresh run of it, with the repair
       instruction "re-run `python scripts/measure/f6_results_report.py`" at :322
rule   EZ0 -- "A PUBLISHED DELIVERABLE is any file sent to Xabier, and anything under
       `results/` or `scripts/measure/` that produces one"
judge  **IT BLOCKS. THE SILENTLY WRONG RESULT IT PRODUCES:**
       `results/F6/floatfea_results_report.md` carrying
       `wave height, full scale : -24.2 m (-0.484 m model, Froude lambda = 50.0)`, written at
       exit 0 by the generator the repository's own gate tells a reader to re-run, from a
       sidecar the production path refuses. **And I state the mitigation honestly rather than
       inflating this:** R756's gate compares shipped against regenerated, so the bad number
       cannot reach the committed file without someone regenerating and committing. That is
       one human step, the regeneration is the step the gate's own message asks for, and the
       gate's question afterwards is "does this file match the tree" -- which would be TRUE
       and is the wrong question. The asymmetry is the finding: the same recorded field has a
       declared domain at one reader and none at the other, which is FR1's second limb
       verbatim -- an input accepted and used other than as declared. **This is the class
       CLAUDE.md records as having produced verdict 108's two highest findings and verdict
       109's single blocking one**, both in `scripts/`, both invisible to a green suite, and
       it is why EZ0 exists.
```

**Closed when** `scripts/measure/f6_results_report.py` reads the recorded basis through the
same validator the production path uses -- or the shipped deliverable it writes stops carrying
recorded numbers that nothing validated -- and the revert-red-restore cycle covers THAT call
site, which is the only thing that distinguishes this from R866, R877 and R881. R895's repair
lands at both doors or it lands at one of two.

---

**R897. (BLOCKS) R887 IS NOT CLOSED. TWO NEGATIVE-CONTROL STATES NOW DIE IN `_build` WITH
`shutil.SameFileError` INSTEAD OF `FileNotFoundError`, BECAUSE `NEXT == VERDICT_STEP == 3`.
THE NEW ASSERTION WRITTEN TO CATCH EXACTLY THIS COMPARES THE WRONG PAIR OF NUMBERS. BOTH REDS
CLEAR WITH A ONE-LINE CHANGE AT THIS SAME COMMIT, WITH NO REPORT AND NO VERDICT WRITTEN -- SO
THEY ARE NOT BOUNDARY REDS AND THEY FAIL THE PREDICATE.**

My predecessor's closing condition said it in advance, in these words: "**Two numbers, not
one:** `_step()`'s plant base and `NEXT` are different concerns -- my probe conflated them and
brought back the `copy2` src==dst collision in `report_file_is_a_directory` -- so the repair
states what each is for." The repair stated what each is for, in two new docstrings, and left
the collision where it was. It turns out to be THREE numbers.

```
claim  the plant destination collides with the verdict copy's SOURCE, not with the report's
cmd    import the module at 6e24b44 and print the four numbers
out    STEP 2  REPORT_NAME step-2.md
       VERDICT_STEP 3  REVIEW_PATH docs/reviews/R1/step-3.md
       NEXT 3
       copy_verdict src step = 3  dst step = 3  COLLIDE = True
       states using ("copy_verdict", str(NEXT)): ["report_file_is_a_directory",
                                                  "zero_padded_step_number_beside_the_unpadded_one"]
       -- exactly the two reds, and tests/test_report_guard_states.py:536 is
          `shutil.copy2(reviews / f"step-{VERDICT_STEP}.md", reviews / f"step-{arg}.md")`
cmd    what the new assertion actually compares (:847-850)
out    assertion 3: `f"step-{NEXT}.md" != REPORT_NAME`  ->  "step-3.md" != "step-2.md" -> True
       -- **it compares the REPORT pair and the live collision is the REVIEW pair.** The third
          property exists because "the destination is NOT the source" failed once; it was
          written against the one pair of numbers that cannot collide here. That is assertion
          domain blindness: the collection the assertion inspects cannot contain the failure.
cmd    CI's own log for the two ids (a machine neither of us controls), run 40260335508
out    shutil.SameFileError: ".../repo/docs/reviews/R1/step-3.md" and
       ".../repo/docs/reviews/R1/step-3.md" are the same file   -- twice, raised in `_build`
cell   **THE CONTROL EG3(i) WANTS, AND IT IS SHARPER THAN A COMPARISON AGAINST ANOTHER
       COMMIT.** ONE VARIABLE MOVED: `NEXT = STEP + 1` -> `NEXT = max(STEP, VERDICT_STEP) + 1`,
       same tree, same commit, no report written, no verdict written, those two ids only
out    UNPATCHED (NEXT = 3 == VERDICT_STEP)   2 failed in  2.24s
       PATCHED   (NEXT = 4)                   2 passed in 28.11s
       -- 2.24 s is dying in setup; 28.11 s is building the tree, planting the defect and
          running the nested guard. **A boundary red cannot be cleared by a change to the
          harness.** These two can, so their cause is the harness and not the boundary.
rule   the FS1 predicate as narrowed by FT1
cmd    limb one, per id, against the newest verdict's 46564 characters
out    "report_file_is_a_directory" -- the newest verdict MENTIONS this name inside R887's
         cell, but a "site" in this repository is a path (`_is_a_site`) and a "finding" is an
         R-number; this id is neither, and the path it dies on, `docs/reviews/R1/step-3.md`,
         is the VERDICT FILE and not a site the verdict names as an open item. Limb one: NO.
       "zero_padded_step_number_beside_the_unpadded_one" -- 0 occurrences anywhere in the
         newest verdict. Limb one: NO.
       limb two: their subject is the harness's own arithmetic, not the commit carrying
         them. NO.
       -- **BOTH FAIL THE PREDICATE. They are CZ1 (iv).**
judge  **IT BLOCKS, and I name the clause rather than stretching FR1, which is what my
       predecessor did for R887 one round ago.** Under FR1's head I cannot name a wrong number
       in an artifact and I will not invent one. It blocks under **CZ1 (iv) with EG3's
       predicate**, tested per id, and its disposition is **FF0**: "Anything that reads the
       gating record, or decides whether a green is believed -- the report guards ... -- is
       FIXED IN THE NEXT COMMIT", under EK2's repair-not-extend rule.
       **And the reason it matters more than two reds look.** Of the 22 states this harness
       builds at this commit: the 8 whose requirement is a clean nested run (3 `green`,
       5 `ignored`) are ALL RED, because no nested run can be clean on a tree carrying 341
       boundary reds; 12 pass on `assert code != 0`, which those same 341 satisfy whatever the
       plant does, so they pass VACUOUSLY; and 2 die in `_build`. **Not one of the 22 is
       measuring anything at this commit**, and `10 failed, 13 passed` is the number that
       hides it. The one thing a repair here can still buy is that the two states reach their
       assertion -- which is what 2.24 s against 28.11 s is the measurement of.
```

**Closed when** no state dies in `_build` -- a grep for both `SameFileError` and
`FileNotFoundError` over the file's own run is `0`, both names and not one -- and the
assertion's third property is stated over **every copy the harness will make** rather than
over the one pair its author had in mind: for each entry in `STATES`, each `copy2`'s resolved
source exists and differs from its destination. The full-file count is then
`8 failed, 14 passed` or better, not `10 failed, 13 passed`: 10 is not better than 8, and my
predecessor's "or better" is what let the collision through. EK2: fixed or deleted, never
extended, and no new apparatus -- this is one expression inside an assertion that already
exists.

---

**R898. (DOES NOT BLOCK -- FF0-class; fix it in the same commit as R897) `closed_by_a_pass`
READS ANY `Verdict: PASS` IN A STEP'S REVIEW FILE AS CLOSURE, AND R888's GLOB WIDENING JUST
PUT R1's REVIEW FILES INTO ITS DOMAIN FOR THE FIRST TIME. STEP 3 NOW READS **CLOSED** TO THE
LATER-STEP GUARD WHILE ITS NEWEST VERDICT IS HOLD AND IT HAS NO REPORT. FK1 GIVES THE EXACT
DISCRIMINATOR AND THE HOOK DOES NOT USE IT.**

```
claim  five ES0 interim checks that happened to be PASS make an open step read closed
cmd    .claude/hooks/require-verdict.sh:285-289, then the predicate over R1's three files
out    closed_by_a_pass() tests `grep -cE "^Verdict: *PASS"` against zero
       docs/reviews/R1/step-1.md  PASS lines=3  Closes lines=1
       docs/reviews/R1/step-2.md  PASS lines=1  Closes lines=1
       docs/reviews/R1/step-3.md  PASS lines=5  **Closes lines=0**
       -- step 3's eight rounds are 5 PASS and 3 HOLD, the newest is HOLD, and **not one of
          the eight carries a `Closes:` line**, because every one is an interim check and
          --interim and --closes are mutually exclusive by refusal.
cell   ONE VARIABLE MOVED -- the glob -- same tree
out    the old F-only form  -> 14 review files, R1's three INVISIBLE
       the new A-Z form     -> 17 review files, R1's three now read
       -- so before `8ee62f6` the loop skipped step 3 entirely and after it the loop reads it
          as CLOSED. The widening is right (R888) and it exposed a second defect behind it.
rule   FK1 -- the signal is the `Closes:` line; and DD1, whose sentence is "a step whose
       CLOSURE verdict is PASS is closed", not "a step with a PASS somewhere in its file"
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none today**, and I
       measured the thing that would make it one: the orphan sweep at `:252`, widened in the
       same commit, still refuses an unreviewed `docs/reports/R1/step-4.md` by name -- the
       turn's own cell -- so the state this predicate would wave through is caught one loop
       earlier. It is FF0-class rather than ledgered because it is the predicate that decides
       whether a step is closed, and the repair is one expression. FK1 made `Closes:` the
       signal precisely because no boolean inferred from the tree could carry the
       distinction, and three routers tried.
```

**Closed when** `closed_by_a_pass` reads `^Closes:` rather than `^Verdict: *PASS`, and the
function's name and comment say which of the two it reads. The DD1 comment above it is
correct about the defect it fixed and silent about the one that replaced it.

---

**R899. (DOES NOT BLOCK -- ledgered; its repair is a standalone `process:` commit)
`docs/SUPERVISOR.md` STATES CZ0's FOUR HEADS AS THE CRITERION BOTH REVIEWERS RULE UNDER, NAMES
FR1 NOWHERE, AND TELLS A WITNESS THAT A HOLD OUTSIDE (a)-(d) IS ILLEGITIMATE. THAT IS C45's
SHAPE IN THE ONE DOCUMENT FE1 DID NOT CLEAR.**

```
claim  the outside witness is instructed to rule under a criterion FR1 narrows for R1, and
       the instruction says so in terms
cmd    grep -c "FR1" docs/SUPERVISOR.md ; grep -c "FR1" .claude/agents/gating-supervisor.md
out    0 / 0
cmd    docs/SUPERVISOR.md:24-33, quoted
out    "**both rule under the same blocking criterion (CZ0)** ... a finding blocks only if it
       is a defect in `floatfea/` or in a published deliverable (EZ0), a tolerance value or
       form, a gate assertion, or a red test at the reviewed commit ... **A witness HOLD on
       something outside (a)-(d) is not a stricter verdict; it is a verdict under a criterion
       this repository retired.**"
rule   C45 -- a mirror of a living document is a figure whose rule moves underneath it; and
       `CLAUDE.md` section Step gating, "treat a witness HOLD exactly like an inside HOLD ...
       the stricter verdict stands"
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- no number is
       wrong anywhere and no witness comment exists on R1. It is on the list because FE1
       deleted the criterion mirror from my own definition for exactly this reason and left
       this one standing, and because the two documents now disagree about what blocks in the
       milestone under execution. I read FR1 from `CLAUDE.md` and from my invocation; a
       witness has neither. **The repair is a standalone `process:` commit citing FR1, never
       a step commit** -- which is the rule that makes this a finding I report rather than one
       I could ever fix.
```

**Closed when** `docs/SUPERVISOR.md` cites `CLAUDE.md` section "What blocks for the rest of
R1" rather than restating a criterion, as my own definition now does for CZ0 -- or states FR1
beside CZ0 with the fact that it narrows it for R1.

---

**R900. (DOES NOT BLOCK -- ledgered) "ALL FOUR ARE PUSHED (FP1), SO EACH HAS A CI RUN
AVAILABLE" IS FALSE. TWO OF THE FOUR HAVE NO RUN AT ALL, BECAUSE GITHUB BUILDS THE PUSH TIP.**

```
claim  a run exists at two of the four commits, not four
cmd    gh run list --commit <sha> for each of the four, then gh run list -L 12 (because
       --commit returns an empty list even where a run exists -- CK2's trap, which I did not
       take for an unavailable check)
out    c3bf24f  no run                8ee62f6  no run
       ece0ebe  40256590041 failure        6e24b44  40260335508 failure
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- FP1's actual
       requirement is that the commit UNDER JUDGEMENT has a run, and `6e24b44` has one that
       completed while I worked. It is on the list because the belief is load-bearing for the
       next round: an implementer who thinks every commit gets a run will cite a run that does
       not exist, and CE1 made the CI section mandatory because three reviewed commits in a
       row had no run and no revision said so.
```

**Closed when** the sentence says what FP1 actually gives: the push tip gets a run, so the
commit the reviewer is invoked on has to be the tip.

---

**R901. (DOES NOT BLOCK -- ledgered) `NEXT` CARRIES TWO STACKED DOCSTRINGS AND THE SECOND IS A
DEAD STRING LITERAL.**

```
claim  the new docstring displaced the old one rather than replacing it
cmd    sed -n '168,185p' tests/test_report_guard_states.py
out    `NEXT = STEP + 1`, then "The step the harness PLANTS INTO...", then "The step AFTER the
       one under execution. ..."
       -- only the first is `NEXT`'s docstring; the second is an expression statement nothing
       reads. Both are true; one is unreachable.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** Ledgered as prose.
       It is worth one line because the orphaned paragraph is the one that explains why the
       states plant at `NEXT` at all, which is the thing R897 turns on.
```

**Closed when** the two paragraphs are one, in the commit that fixes R897.

---

**One criterion observation, not a finding, said once -- and the number my predecessor
reported has moved, for the reason R861 names.** The predicate reads "a finding or a site of
**the newest verdict**". Measured strictly, per id, at this commit: **44 of the 50 finding ids
and 278 of the 286 site ids satisfy limb one literally**; 14 ids do not, and they are the ids
of six findings of EARLIER unanswered step-3 verdicts -- R858, R859, R861, R876, R878, R879.
My predecessor measured the same quantity as 67 and reported it as a criterion question.
**The difference is not that the tree changed; it is that this round's `Carried` table names
more findings by name than the last one did, so more ids satisfy a literal reading.** That is
R861's own lesson applied to the predicate itself: the baseline is a function of what the
reviewer writes. A predicate whose strict reading makes a red blocking or not depending on how
exhaustive my own prose was cannot be the intended reading, so I followed my predecessors'
reading -- a finding or site of a verdict with no answering report revision -- and I say so
plainly. **If that reading is wrong it is a criterion question for Xabier and not a round**,
and the number to give him is this one: under the strict reading 14 of 351 reds would block,
and which 14 depends on my wording.

## CI at the reviewed commit: the run EXISTS, it COMPLETED, the ladder is GREEN, the guards step is RED

**`gh run list --commit 6e24b44` returns an empty list and the run EXISTS** -- CK2's third
state does not apply: run **40260335508** has real jobs, real steps and real durations. **It
was `in_progress` when I began and `completed / failure` when I read it, and I waited rather
than recording a conclusion I had not seen.**

```
job  the verification ladder      SUCCESS   (rungs 1, 2, 3, 4, 5 and 6 all SUCCESS)
job  lint, unit and guards        FAILURE
     actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
     unit tests SUCCESS / guards and meta-tests FAILURE
     -- every step RAN. Nothing was skipped behind an earlier red, which is what CZ1 (iii)
        exists to see, and FP1's CI-only types-PyYAML red has stayed fixed.
job  CI determinism -- leg        skipped
job  CI determinism -- ten legs   skipped
```

**THREE INDEPENDENT RUNS AGREE ON THE ID SET, NOT MERELY ON THE COUNT.** CI:
`351 failed, 1091 passed, 1 skipped in 615.08s`. Mine: `351 failed, 3676 passed, 1 skipped in
1211.45s`. The turn's: `351 failed, 3676 passed, 1 skipped in 1246.94s`. `comm -3` between my
351 ids and CI's 351 ids is **(empty)** -- the same tests, on two operating systems. And
`git status --porcelain` is empty before and after, which is also the control saying my probes
did not leak.

The 351, each id tested against the FS1 predicate AS NARROWED BY FT1, per id and not by
family:

```
286  test_every_named_site_is_touched_or_declared[<finding>-<path>[:line]]   limb one. Every
       finding prefix lies in R850..R894, all findings of step 3's nine interim verdicts,
       none of which has an answering report revision. 278 of the 286 also satisfy the
       STRICT reading -- the finding or the path is named in the newest round -- and the 8
       that do not are listed under the criterion observation above.
 50  test_the_report_carries_the_finding[R845..R894]   limb one -- each NAMES a finding.
       44 satisfy the strict reading; 6 do not (R858, R859, R861, R876, R878, R879).
  1  test_the_CI_section_is_about_the_REVIEWED_commit   limb one -- "the CI section's first
       commit is d205833 and the verdict judged cd126a6", both of them verdict shas
  1  test_the_Carried_table_is_what_the_generator_produces      limb one -- keyed on a table
       that cannot exist until a step-3 report does
  1  test_the_generator_would_catch_a_row_under_the_wrong_number limb one, that generator's
       own control, same premise
  1  test_the_report_carries_a_WHOLE_SUITE_count   **LIMB TWO under FT1** -- its subject IS
       the commit carrying it: suite_count.py measures a clean worktree AT a commit, so the
       line naming a sha cannot be inside that sha
  1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  **LIMB TWO under FT1** -- no run exists
       for a commit before it is pushed
  8  test_the_guard_survives_the_state[baseline, verdict_amended_after_the_commit_the_report
       _answers, newest_report_has_no_verdict_yet, non_numeric_step_suffix,
       superscript_digit_step_number, draft_suffix_beside_a_step_report,
       step_number_is_the_empty_string, zero_padded_step_number]
       limb one, and I read the MESSAGE of each rather than ruling them as a family. Three
       distinct messages, one cause: 3 are "expected a clean run" (require=green), 5 are "a
       file that is not a numbered step must be stepped over, not reacted to"
       (require=ignored, which also asserts exit 0), and newest_report_has_no_verdict_yet is
       "the test that carries the diagnosis is not among [R845, R846, R847 ...]" -- whose
       printed list IS the boundary reds. **All eight assert a CLEAN nested run, and no
       nested run can be clean while the 341 above exist.** Boundary consequence.
  2  test_the_guard_survives_the_state[report_file_is_a_directory,
       zero_padded_step_number_beside_the_unpadded_one]
       **FAIL BOTH LIMBS. CZ1 (iv). THIS IS R897.** shutil.SameFileError in `_build` on
       docs/reviews/R1/step-3.md, and both go GREEN at this same commit under a one-line
       change to `NEXT` -- which no boundary red can do.
---
351  349 with an exit, 2 WITHOUT.
```

**EG3(i) is satisfied by the trace above and by one thing more that no list of names can
give:** the two blocking ids were cleared at the reviewed commit itself, with nothing written
to `docs/reports/` or `docs/reviews/`, by moving one variable in the harness. That separates
"red because no report exists" from "red because the harness is wrong" without needing a
second commit to compare against -- which is the comparison R1 step 1 got wrong by choosing
two instances of the same state.

## Corpus (EG4(e))

**THE PAUSE HELD. I added no entries and committed nothing to `tests/corpus/`.** Batches are
paused until 28 October except mutation work on F4's load-mapping gate and EB6's
label-provenance gate; this diff touches neither. **0 entries are new this round, so there is
no caught-of-new count to report**, and I say that rather than quoting a coverage figure I did
not measure.

**What I ran instead -- the recorded substitute, and BOTH halves produced a blocking finding
this time:**

* **A continuum grid over the parameter space the decision rules guard.** Four rules, four
  spaces, 37 cells, every one in a disposable worktree I then removed:
  - `WAVE_HEIGHT = (low, high)` against the whole of `test_headings_and_bem_coverage.py`,
    17 cells, **EH4 in all three directions including the two that WEAKEN the gate**: the
    ceiling may rise to `100.05` and `100.09` with `67 passed` and trips 2 cases at `100.1`;
    the floor may fall to `-1e-10` silently and trips 2 at `-1e-9`; the ceiling falling to
    `99.9` trips 1 and to `24.19` trips 14. So the shipped domain is pinned within 0.09 m
    above and 1e-10 below -- **the assertion is not vacuous in either direction, and I
    measured that rather than assuming it.**
  - the recorded sidecar against lambda through the REAL CLI, 13 cells. **This produced
    R895**, and cases C and D are what refute the turn's proposed next commit. Two of the 13
    are the new check working end to end: `full=100.1` and `full=-1e-9` both give EXIT=2 with
    the field named and nothing written.
  - one-at-a-time ablation of the repair, 5 cells. The range check disabled ->
    `14 failed, 53 passed`; the call removed from the reader -> `1 failed, 66 passed`, the one
    being `test_R877_the_READER_ITSELF_validates_not_only_the_helper`. **Both of the turn's
    figures reproduce EXACTLY.** And three the turn did not take, each dropping ONE
    `RECORDED_BOUNDS` entry: model -> `7 failed`, full -> `8 failed`, heading -> `10 failed`.
    **Every entry is individually load-bearing, and dropping the heading also kills the NaN
    and the two infinity cases** -- which is the measurement that the type and finiteness
    checks now live inside the same `RECORDED_BOUNDS` loop, and why
    `test_R881_EVERY_numeric_recorded_field_HAS_a_declared_domain`'s set equality is the thing
    holding them there.
  - `NEXT` against the two colliding states, 2 cells. **This produced R897.**
* **A regeneration check on a published deliverable: RUN, and CLEAN.** Unlike last round,
  `floatfea/run/pipeline.py` IS in this diff, so a producer moved and the check can differ.
  `floatfea run` on the shipped example with outputs redirected, compared against the three
  committed files with the wall-clock rows excluded: `report.md` 105 lines, `member_forces.csv`
  1289, `utilisation.csv` 73, and the **only** differing lines in all three are the config
  filename of my redirected copy. **Every number in all three published deliverables
  reproduces at `6e24b44`** -- the control saying R881's repair moved no published figure, and
  also how I know R896's second door is a live generator rather than a dead one.
* **The harness's own measuring capacity, since it is the subject of R897.** Of the 46 entries
  in `tests/corpus/report_guard_states.txt`, 22 are built as states and 24 await
  transcription. Of the 22 built, at this commit **8 can measure anything and all 8 are red,
  12 pass vacuously on exit-non-zero, and 2 die in setup.** That is the coverage number this
  round and it is zero.

Neither half would have come from reading the diff. The diff's configuration is the one the
commit chose; R895 lives at a configuration nobody chose, and R896 lives in a file the diff
does not touch.

## Tolerances touched

**None.** `git diff cd126a6..HEAD -- floatfea/tolerances.py` is empty.

**And nothing in the diff is a tolerance under another name, which I checked rather than
assumed.** `RECORDED_BOUNDS` introduces no number: it maps three field names onto two bounds
that already existed in `config.py` and are already applied to the configured side. R1's
locked plan section 4 settles the classification explicitly -- "the config's ranges are
declared validation bounds" and "None expected, under FM0" -- so `WAVE_HEIGHT`'s home in
`config.py` is correct and I raise nothing about its location. The hook change is two globs,
the harness change is a resolver and an assertion, and the two plan changes move no number.
The only numerals added anywhere in the diff are line numbers, commit shas and step numbers
inside comments.

**R895's repair is the one place a tolerance may be needed**, and that is the whole reason the
split was right. If it takes the epsilon route, the entry goes in `floatfea/tolerances.py`
with its `_COUNTER` and its justification, in its own commit, and R1 section 4's "None
expected" is re-locked in the same commit. If it takes the derivation route it needs none.

## Next step opens when

**This is a HOLD on step 3, which stays open. It is the ninth interim check, it counts against
no round, and all three reviewed revisions remain available -- 0 of 3 spent.**

**R897 and R898 are answered in the NEXT commit** -- that is FF0's own wording for this class,
not my preference -- and they are one file and two expressions between them. The conditions
are measured, so there is nothing to interpret: `tests/test_report_guard_states.py` runs with
a grep for BOTH `SameFileError` and `FileNotFoundError` equal to `0`, a full-file count of
`8 failed, 14 passed` or better with the marker left at 3, and the assertion's third property
stated over every `copy2` the harness will make rather than over one pair. `closed_by_a_pass`
reads `^Closes:`.

**Then R895 and R896 together, as ONE repair at TWO doors, before step 3's first reviewed
revision.** They are the same defect, and splitting them would repeat the shape that produced
R866, R877, R881 and now this: a correct, tested check that one of the callers does not use.
The conditions are in their own `Closed when` paragraphs, and the part I will test myself is
that my cases C and D are rows in the test, because a ceiling on one member of the pair is
green on both.

**R882-R886 now have ONE place left.** The commit my predecessor named as their preferred home
has been spent without them, so they are declared by name in step 3's first reviewed revision
-- each with what was left and why -- or they are taken. Not silence.

**Then FL2, in FT2's order, and nothing in this list displaces it.** FT2.3's period-band check
is still unbuilt and is the item R881 was meant to ride with. R867-R869 are FT2.7 and are now
in the plan row. R889 and R890 are withdrawn. R891, R892, R899, R900 and R901 are sentences,
and R899's repair is a `process:` commit that belongs to nobody in this loop but Xabier.

**R880 still waits**, and for the fourth round running it did not misdirect me: I ruled under
`CLAUDE.md`'s predicate as FT1 narrowed it, per id. Do not take it first.

**What I did NOT ask for.** No new guard, scanner, meta-test, detector or report generator.
R897 and R898 are repairs to existing apparatus under EK2; R895 and R896 call a validator the
tree already has from a second place; everything else is a sentence or a glob.
`docs/milestones/F2a.md` is where anything larger goes.

**Schedule, since FT3 asks for it at every reviewed revision and the turn reported slippage on
the day it was known.**

**The slippage is reported correctly and I am not re-escalating.** FS4's 26 October checkpoint
for FL2's first reviewed revision does not hold; the turn says so today, which is what
`CLAUDE.md` asks -- "Slippage is reported the day it is known" -- and FR0 already answered the
escalation with "slip the date, keep the scope". Three observations, each a measurement:

1. **The estimate moved EARLIER while the calendar moved later, and that is worth a sentence
   to Xabier.** My predecessor's round read 17 November as credible for the work; this turn's
   estimate is R1 finishing around 12 November. Nothing in FT2.4-FT2.7 was built between the
   two, so the estimate improved on no new evidence about the work. I am not ruling on a
   figure in a message -- R890's rule, which I am keeping -- but an estimate that falls five
   days while five days pass and nothing ships is the shape the previous two checkpoints had.
2. **This is the third consecutive round in which gating apparatus, not the element, carried
   the finding.** R887 then R897; R888 then R898. Each repair is one or two expressions, and
   each was found by RUNNING the harness rather than reading it. The cost is not the repairs
   -- it is that `tests/test_report_guard_states.py` has been certifying nothing at all for
   nine interim checks, measured above as 0 of 22 states live, and the only thing that clears
   that is step 3's report existing.
3. **The risk is still concentrated in FT2.4 and FT2.5, and R896 is the first measured
   evidence for it.** Those two move `scripts/measure/f6a_required_section.py` and
   `scripts/measure/f6b_truss_sizing.py` onto the production path, and `scripts/measure/` is
   EZ0 surface by name. R896 is a `scripts/measure/` reader publishing an unvalidated recorded
   number into a shipped deliverable TODAY, before either of those items has started. **I
   would load items 4 and 5 by more than x1.5 and hold a day for the second door at each**,
   because the lesson of R896 is that moving a measurement script onto the production path
   means auditing what it READS, not only what it computes.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: cd126a65ffdc7b84d419922e3f54272d1ff0b7b5
**Reviewed commit: `cd126a65ffdc7b84d419922e3f54272d1ff0b7b5`.**
Verdict: HOLD
Tests: 3647 passed, 299 failed, 1 skipped, 2 warnings in 1033.69 s (0:17:13)   (my own whole-suite run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the eighth in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available.
**ONE FINDING BLOCKS -- R887 -- and it is in the commit that moved the marker, not in the
hook.** FT0's repair is SOUND and I confirmed it by running the gate rather than reading it:
the deadlock is gone, the gate now names step 3's own reviewed commit, and a step-3 verdict
clears it. The guard change in `ba0ce03` is a REPAIR and not a widening, and I can say so as
a 2x2 measurement. What `ba0ce03` also did, and did not measure, is move the plant target of
the negative-control harness onto a file that does not exist: **fifteen of the twenty-three
states that exist to prove the report guards CAN fail now die before planting a defect, eight
of them newly.**

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For each finding I state the silently wrong result it produces, or
that it produces none. **R887 blocks under CZ1 (iv) with FF0, not under FR1's head**, and I
say so in its own words rather than stretching FR1 to fit -- see the ruling under R887.

```
cmd    git log --oneline 5ca5496..HEAD ; git diff --stat 5ca5496..HEAD
out    cd126a6 ba0ce03 f9954f7 f39cbd6 -- FOUR commits.
       .claude/hooks/require-verdict.sh 34 ++ | CLAUDE.md 19 ++ |
       docs/SUPERVISOR.md 19 ++ | docs/directives/FT.md 79 ++ |
       docs/directives/README.md 2 | docs/milestones/R1.md 2 |
       tests/test_report_carried.py 26 ++
       -- 7 files, 167 insertions, 14 deletions
cmd    git diff --stat 5ca5496..HEAD -- floatfea ; -- scripts ; -- floatfea/tolerances.py
out    (empty) / (empty) / (empty)
       -- NO `floatfea/` change in this diff at all, which is why R881..R886 are all still
          open below and why no regeneration check could differ: the producers did not move.
cmd    git diff 5ca5496..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py        -- a file, as my instructions say it must be
cmd    git diff --stat 5ca5496..HEAD -- .claude docs/SUPERVISOR.md
out    .claude/hooks/require-verdict.sh 34 ++ ; docs/SUPERVISOR.md 19 ++
       -- **NOT a STOP, and I read every line of both.** `f9954f7` is a standalone
          `process:` commit citing FT0 whose ONLY file is `.claude/hooks/require-verdict.sh`;
          `cd126a6` is a standalone `process:` commit citing FT1 whose only files are
          `CLAUDE.md` and `docs/SUPERVISOR.md`. `ba0ce03`, which touches `tests/`, touches
          NEITHER -- measured per commit, not over the range.
cmd    git diff --stat 5ca5496..HEAD -- results scripts/measure docs/reports
out    (empty)   -- no published deliverable moved, and no step report was touched (EK3)
cmd    git status --porcelain   (before anything, and after ~30 hook probes, four harness
                                runs, three mutated-marker test runs and one patched-harness
                                run, all in a disposable worktree under my scratch directory)
out    (empty) / (empty)
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ;
         mypy floatfea scripts/f4_dynamic_residual.py       (CI's own three forms)
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 43 source files
cmd    the turn's three cited figures, re-taken by me at this commit
out    tests/test_plan_figures.py                                    -> 195 passed
       test_report_carried.py -k "plan_names_the_step or guard..."   -> 2 passed
       tests/test_tree_prose_consistent.py                           -> 34 passed
       -- all three reproduce EXACTLY. **The file the turn did NOT run is
          `tests/test_report_guard_states.py`, and that is where R887 is.**
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third and eight verdicts are now newer than it.
That is EG3 state (2) and it is the cause of 282 of this tree's 299 reds -- but not of all of
them, which is the whole of R887.

**R855's standing condition is MET.** The turn states plainly that it made no whole-suite run
at this sha and names exactly what it did run. No green is claimed that was not measured.
Mine is in the header, and it agrees with CI id-for-id (299 each).

## The question the turn asked: is the gate's new behaviour RIGHT, not merely green?

**YES, AND THE CONFIRMATION IS A RUN OF THE GATE AND NOT A READING OF IT.** I rebuilt every
replay in `f9954f7`'s message plus five the turn did not run, in a worktree at `cd126a6`.

```
claim  the deadlock is gone and the gate is now CLEARABLE by a step-3 verdict
rule   the block at `.claude/hooks/require-verdict.sh:407` -- `git diff --quiet $reviewed --
       $report floatfea tests ':(exclude)tests/corpus'` -- with `$reviewed` picked by
       ancestry from the MARKED step's review file
cmd    printf '{"stop_hook_active":false}' | bash .claude/hooks/require-verdict.sh, at
       cd126a6, clean tree
out    BLOCK "floatfea/, tests/, or docs/reports/R1/step-3.md changed since the verdict at
       154261e..." -- **step 3's OWN newest reviewed commit**, where the old hook named
       8542d79, step 2's
cell   ONE VARIABLE MOVED: a step-3 verdict naming `cd126a6` committed into
       `docs/reviews/R1/step-3.md`, nothing else
out    (empty) exit=0   <- **THE GATE CLEARS.** This is the property that did not exist
                           before FT0 and it is the one that matters: the thing the hook
                           asks for is a thing that can be delivered.
cmd    the marker at 4, and at 9 -- a step with neither file
out    BLOCK "...NEITHER docs/reports/R1/step-9.md NOR docs/reviews/R1/step-9.md exists..."
       -- refused in both, so the new key is not vacuous
cmd    the OLD hook on THIS tree (the turn's control, re-run with ONE variable moved)
out    BLOCK "...step 3 of R1 is under execution and docs/reports/R1/step-3.md does not
       exist." -- the OTHER horn. See R892: the turn's stated control moved two variables
       and reported the first horn.
cmd    marker 3, the review file moved aside, a report planted
out    BLOCK "Step report docs/reports/R1/step-3.md has no supervisor verdict at
       docs/reviews/R1/step-3.md" -- R799's refusal still fires for the marked step
cmd    EH4, the direction that WEAKENS the gate: how far forward can the marker go?
out    admitted markers are exactly {steps with a report} u {steps with a review} = {1,2,3};
       4 and 9 refused. The implementer CAN admit 4 by writing `docs/reports/R1/step-4.md`
       -- and the hook then refuses it at `:292` for having no verdict (measured). The
       review half of the disjunct is a path `protect-reviews.sh` denies the implementer,
       so **the new escape hatch is one only the reviewer can open.** That is the property
       I would have asked for had the turn not already had it.
```

**The one thing I will not certify is enforcement, and it is the turn's own discovery.**
`stop_hook_active` waives the hook after it has blocked once, so this gate surfaces its reason
once per turn and cannot bar the turn. That is a property of the mechanism, not of this change
-- and it means the bound on an unreviewed report is this review, not the hook. That is CJ0's
sentence in my own instructions ("a gate that reads a record cannot outrank code that writes
the record. Review is the bound"), reached from the other side.

## Widened, or repaired? REPAIRED, and here is the 2x2 that says so

The turn asked for this judgement explicitly and named it the one it was least certain of.

```
claim  the new assertion's admissible set is the old one plus exactly the live step, and the
       addition is reviewer-controlled
rule   `assert _plan_step() in REPORTED or _plan_step() in REVIEWED`
       (tests/test_report_carried.py:536)
cmd    the four states, each run twice -- the shipped assertion and `git show
       5ca5496:tests/test_report_carried.py` -- one variable moved each time
out                           marker 2     marker 3     marker 4 / 9 (neither file)
       old (`in REPORTED`)    1 passed     1 FAILED     1 FAILED
       new (shipped)          1 passed     1 passed     1 FAILED
       -- the admissible marker set grew from {1,2} to {1,2,3}: by the live step and nothing
          else. It is NOT vacuous in either direction.
cell   does the marker move change WHICH report the module's other guards read? ONE VARIABLE
       MOVED, the marker, same tree, module re-imported
out    marker 2 -> STEP=2 STEP_REPORT=2 _PAIRED=2 REPORT=step-2.md VERDICT=step-3.md
       marker 3 -> STEP=2 STEP_REPORT=2 _PAIRED=2 REPORT=step-2.md VERDICT=step-3.md
       -- IDENTICAL. `STEP = max(_PLAN_STEP if _PLAN_STEP in REPORTED else 0, _PAIRED)`
          already falls back, so no sibling guard changed its subject or went vacuous.
rule   EK2 -- a guard that fails false is fixed, not extended; and the premise the guard
       encoded ("never before it") is retired by FT0, by directive
judge  **A REPAIR.** The retired premise was retired by the directive that ordered the marker
       move; the guard asserted it verbatim; the repair removes exactly that premise, keeps
       the guarantee that a marker naming a step with neither file is refused, and the new
       disjunct's domain is a directory the implementer cannot write. I would have objected
       had the repair been `in REPORTED or True`, or had it moved the sibling guards' subject.
       Neither happened.
```

**And the census the family's history demands, because a one-site repair of a premise with
siblings is how R871, R875 and R813 happened.** `grep -rn "advanced in the commit"` finds five
live sites: two are the new comments quoting the premise as RETIRED (the hook and the guard,
correct), two are closed milestones' own records (`docs/milestones/F6.md:145`,
`docs/reports/F6/step-1.md:22`), and one states it as a LIVE RULE --
`docs/milestones/F2.md:22`. That is R893.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R881** (two recorded wave heights get two of three checks; `wave_height_full_m: -24.2` publishes a negative height at exit 0) | **STILL OPEN, correctly, and correctly NOT in this diff** | `git diff 5ca5496..HEAD -- floatfea` is EMPTY. My own placement stands: it lands IN the commit that builds FL2 item 3, and **it blocks there if item 3 is built without it.** Nothing in these four commits brings a recorded height nearer a number. |
| **R882** (the refusal still recommends removing `load_cases.headings`), **R883** (`10**400` "caught before `float()` raises" -- it raises, from inside the check), **R884** (a `run` block of the wrong TYPE publishes "NOT RECORDED" at exit 0), **R885** (the raw domain refuses a legally signed recording), **R886** (a blanket `# noqa: F401` over four names) | **ALL FIVE STILL OPEN, ALL UNTOUCHED, AND CORRECTLY SO** | the `floatfea/` and `tests/unit/` diffs since 5ca5496 are both empty. Under FS0/FT2 the order is the plan's and none of the five is FR1-blocking, so none earns a commit ahead of FL2 item 3. They go in the next commit that touches `_validated_wave_basis`, or into the first reviewed revision as declarations of what was left and why. |
| **R867, R868, R869** (of eight non-default topologies one runs; the rest die in a `platform:hub1_arm_tip` lookup) | **still open, and now SCOPED BY DIRECTIVE: FT2.7 makes them an item of step 3** | `docs/directives/FT.md:27-29`. The diff over `floatfea/model`, `floatfea/solve` and the topology test file is empty. They remain blocking by name into the first reviewed revision. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a); two future-tense sentences) | **still open, untouched** | the `floatfea/run/pipeline.py` diff since 5ca5496 is empty. |
| **R862** (three hand copies of the stage set; the published total is the sum of a hand-copied four) | **still open and STILL NOT DUE -- trigger re-measured, not taken on trust** | `git diff 5ca5496..HEAD -- floatfea/cli.py` is EMPTY and no `timings[...]` assignment moved. It blocks in the commit that adds a timed stage, which is FL2 item 4 or 5. |
| **R863, R864, R865** (the exclusion set defined by the code under test; the byte-identity witness blind to its subject; a docstring in the regenerates test) | **all three still open, untouched** | the `tests/regression` diff since 5ca5496 is empty; R864's condition still needs a report revision that does not exist. |
| **R847 / C43, R848, R849 with R854** | **all still open, all untouched, all correctly so** | the `floatfea/cli.py` and `tests/regression` diffs are empty. FR1's second and third non-blocking classes. |
| **R852** | **ROUTED, not open -- FS3 ledgers it to FL3** | `docs/directives/FS.md`. Not open against step 3. |
| **R880** (my own agent definition cites "their two corrected lists", which FS1 deleted) | **STILL OPEN, STILL CORRECTLY NOT TAKEN, and it did not misdirect me a third time** | I ruled under `CLAUDE.md`'s predicate as narrowed by FT1 and applied it PER ID to all 299 reds. `.claude/agents/` is untouched by this diff -- which is right: it is not FR1-blocking and FS0 says apparatus waits for FL2. **Do not take it first.** |
| **R855** (the whole suite at a commit carrying no report revision) | **condition MET, and I took the number myself as I do by rule** | see the header: 299 failed, 3647 passed, 1 skipped. |
| **R856** (the verdict tool refused a step with no report) | **ANSWERED, exercised a fifth time -- this file went through `--interim`** | `scripts/write_verdict.py`, untouched by this diff. |
| **R835, R836, R871** (EG3's lists; FS1's deletion of FC1's reason) | **ANSWERED, and now NARROWED by FT1 -- and I checked the narrowing in the direction that could have cost something** | the two limb-two ids at this commit are `test_the_report_carries_a_WHOLE_SUITE_count` and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`; both have their own commit as SUBJECT, so **the narrowing orphans neither.** EH4's weakening direction applied to a criterion edit: no currently-red id loses its exit by FT1. See the CI section. |
| **C45** (a mirror going stale) | **DOES NOT RECUR in this diff, and the turn took the one precaution that prevents it** | `CLAUDE.md` and `docs/SUPERVISOR.md` were edited in the SAME commit; the two sections now differ in exactly 4 lines, all second-person framing ("in the reviewer's own wording" vs "in your own wording"). The rule text is byte-identical. Measured, not read. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally in CI's own three forms AND on a machine neither of us controls** | mine above; CI run 40251519070, job `lint, unit and guards`, steps `actionlint` `ruff` `black --check` `mypy` `unit tests` all SUCCESS. Every step RAN. |
| **C42, C44** | **mine, accepted, carried** | unchanged by this diff. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **EG3(ii): the verdict commit measured** | **DONE at `bd315a1` two rounds back (149 passed, 0 failed) and not redone** | ES0's light scope; the control's conclusion is unchanged. |
| the suite-count line, and CZ1 (ii)/(iii)'s four outputs | **still owed, still structurally unpayable until step 3's report exists** | limb two of the predicate by construction; two of this round's 299 reds ARE it. |

## Findings

**R887 BLOCKS. R888..R894 do not.** No tolerance moved, no conftest moved, no `floatfea/`
file moved, no published deliverable moved.

---

**R887. (BLOCKS) `ba0ce03` MOVED THE MARKER TO A STEP WITH NO REPORT, AND THE NEGATIVE-CONTROL
HARNESS DERIVES ITS PLANT TARGET FROM THE MARKER. FIFTEEN OF THE TWENTY-THREE STATES IN
`tests/test_report_guard_states.py` NOW DIE IN `_build` ON A FILE THAT DOES NOT EXIST, BEFORE A
SINGLE DEFECT IS PLANTED. EIGHT OF THEM WERE GREEN ON THIS SAME TREE ONE MARKER VALUE AGO.
THIS IS R601a, THIRD OCCURRENCE, AND THE DOCSTRING FORTY LINES ABOVE THE CAUSE PROMISES IT
CANNOT HAPPEN AGAIN.**

```
claim  the two resolvers have drifted apart: the guard reads step 2, the harness plants into
       step 3
rule   tests/test_report_guard_states.py:90-91 -- "Every path the harness builds derives from
       this name, so the place it plants and the place the guard reads cannot drift apart
       again."; and :94 -- "_step(): The step the guard reads, TAKEN THE WAY THE GUARD TAKES
       IT (DB2)."
cmd    import both modules at cd126a6 and print what each resolves
out    test_report_carried.py   : marker=3  STEP the guard READS=2   REPORT=step-2.md
       test_report_guard_states : marker=3  STEP it PLANTS into=3    REPORT_NAME=step-3.md
       -- the guard takes `max(_PLAN_STEP if _PLAN_STEP in REPORTED else 0, _PAIRED)`; the
          harness takes the RAW MARKER. The docstring's claim is false at this commit, and
          it is false about the one thing it promises.
cmd    the plant target's existence
out    docs/reports/R1/step-3.md exists: False      (marker 3, shipped)
       docs/reports/R1/step-2.md exists: True       (marker 2, before ba0ce03)
cell   ONE VARIABLE MOVED -- the marker, same tree, same harness, the full file both ways
out    marker 3 (shipped) : 17 failed,  6 passed in 83.30s
       marker 2           : 10 failed, 13 passed in 279.89s
       8 ids GREEN at marker 2 and RED at marker 3:
         answers_header_names_a_sha_that_is_not_a_commit
         answers_header_names_an_older_verdict_commit
         guard_state_a_report_commit_messaged_docs_that_also_edits_the_guards_measuring_it
         guard_state_declared_GREEN_in_REQUIREMENT_CHANGED_while_the_state_actually_REDDENS_CONTROL
         newest_verdict_file_present_but_empty
         two_digit_step_number_discriminating
         two_reports_ahead_of_the_newest_verdict
         verdict_file_is_a_directory
       1 id RED at marker 2 and green at 3 (`report_file_is_a_directory`): at marker 2
         `NEXT == VERDICT_STEP == 3`, so `_build` ran `shutil.copy2(src, dst)` with src ==
         dst. A pre-existing collision, surfaced by the same number -- see the repair note.
cmd    the failure reason for each of the 17, from CI's own log at run 40251519070 (a machine
       neither of us controls)
out    15 x FileNotFoundError: .../repo/docs/reports/R1/step-3.md, raised from
         tests/test_report_guard_states.py:494 inside `_build`
        1 x [baseline] AssertionError: baseline: expected a clean run.
        1 x [verdict_amended_after_the_commit_the_report_answers] expected a clean run.
       -- only the last two have the boundary cause. The 15 die in SETUP.
rule   the FS1 predicate as narrowed by FT1 -- "a red that names a finding or a site of the
       newest verdict, OR whose SUBJECT IS THE COMMIT CARRYING IT, is a boundary red; any
       other red blocks"
cmd    does any of the 15 name a finding or a site of the newest verdict? (the newest round
       of docs/reviews/R1/step-3.md, 39829 chars, searched for the path they name)
out    'docs/reports/R1/step-3.md' : 0 occurrences
       'docs/reports/R1'           : 0 occurrences
       'step-3.md'                 : 0 occurrences
       -- limb one: NO. limb two: their subject is a report that does not exist, not the
          commit carrying them: NO. **All 15 FAIL THE PREDICATE. They are CZ1 (iv).**
cell   AND THE REPAIR IS MEASURED, NOT ASSERTED. One variable moved -- the plant target
       resolved the way the guard resolves it (fall back to the newest step that HAS a
       report), marker left at 3, in a disposable worktree I then deleted
out    17 failed, 6 passed   ->   10 failed, 13 passed, and `grep -c FileNotFoundError` = 0
       -- identical to marker 2's count WITH THE MARKER STILL AT 3. The marker move does not
          have to be undone; the resolver has to agree with the guard, which is what its own
          docstring already claims.
judge  **IT BLOCKS, and I name the clause rather than stretching FR1.** Under FR1's head I
       cannot name a wrong number in an artifact today, and I will not invent one. It blocks
       under **CZ1 (iv) with EG3's predicate** -- a red at the reviewed commit that fails the
       predicate, tested per id -- and its disposition is set by **FF0**, which is
       unambiguous: "Anything that reads the gating record, or decides whether a green is
       believed -- the report guards ... -- is FIXED IN THE NEXT COMMIT", under EK2's
       repair-not-extend rule. `tests/test_report_guard_states.py` IS the witness for the
       report guards; with 15 of 23 states dark, "the report guards are green" and "the
       report guards cannot see anything" are the same observation for the whole of FL2's
       remaining build. That is FF0's own recorded cost -- "a tree that is red by design is a
       tree in which the next real red is harder to see" -- and the eighth member of exactly
       such a group was a real defect once (R629). The step-3 report is the artifact these
       guards protect, and R1's closure is a published deliverable under EZ0.
```

**Closed when** the harness resolves its plant base the way `tests/test_report_carried.py`
resolves `STEP` -- the newest step that actually has a report -- or synthesises the missing
report explicitly, so that no state dies in `_build`; `grep -c FileNotFoundError` over the
file's own run is `0`; and the full-file count is back to `10 failed, 13 passed` or better
WITH THE MARKER AT 3. **Two numbers, not one:** `_step()`'s plant base and `NEXT` are
different concerns -- my probe conflated them and brought back the `copy2` src==dst collision
in `report_file_is_a_directory` -- so the repair states what each is for. EK2: fixed or
deleted, never extended, and no new apparatus.

---

**R888. (DOES NOT BLOCK -- FF0-class; fix it in the same commit as R887) THE R799/R800 ORPHAN
SWEEP GLOBS `docs/reports/F*/step-*.md`, AND R1 IS THE ACTIVE MILESTONE. AN UNREVIEWED
`docs/reports/R1/step-4.md` ENDS THE TURN. THE SAME FILE AS `docs/reports/F7/step-1.md` DOES
NOT. THE REFUSAL'S OWN MESSAGE SAYS IT "SWEEPS EVERY REPORT".**

```
claim  the sweep that exists to catch an unreviewed report cannot see the milestone under
       execution
cmd    the two globs, and their blame
out    .claude/hooks/require-verdict.sh:240  for rep in docs/reports/F*/step-*.md   (60bb3f0)
       .claude/hooks/require-verdict.sh:276  ls docs/reviews/F*/step-*.md           (ddabd44)
       -- both PRE-DATE this diff. FF0 widened the PLANS glob at :97 and left these two; the
          comment at :92 says "THE SAME DEFECT WAS IN ALL FOUR RESOLVERS", and these are a
          fifth and sixth site in the same file.
cell   ONE VARIABLE MOVED -- the milestone letter -- with the gate otherwise CLEAR (a probe
       verdict naming cd126a6 committed first, so nothing else can block) and both files
       COMMITTED so git diff can see them
out    docs/reports/R1/step-4.md, unreviewed  -> exit=0, (empty)      <- ALLOWED
       docs/reports/F7/step-1.md, unreviewed  -> BLOCK "these step reports have no
                                                 supervisor verdict: docs/reports/F7/step-1.md
                                                 ... This sweeps EVERY report except the three
                                                 that predate their milestone's first verdict"
rule   CW0 -- prose in the source tree does not claim things about the code; and the hook's
       own FT0 comment at :165, "Refusing on neither keeps R799's guarantee -- a report with
       no verdict is still refused at line 262 below, whatever the marker says"
cmd    is the guarantee kept for the MARKED step? (the half the comment is right about)
out    marker 3, step-3 report committed, no newer verdict -> BLOCK (check_carried, then the
       diff at :407). YES for the marked step; NO for any other step of R1. And the line the
       comment cites, 262, is inside the DD1/DE1 comment; the refusals are at :251 and :292.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none today** -- no number
       is wrong anywhere and the marked step is still gated. It is FF0-class rather than
       ledgered because it is the sweep that decides whether an unreviewed report can end a
       turn, and the repair is one character of glob. The line-276 blindness has no
       consequence at this commit (R1 steps 1, 2 and 3 each carry a Verdict: PASS, so that
       loop would skip them anyway) and is named here so one repair covers both.
```

**Closed when** both globs reach every milestone, as `:97` already does -- and the refusal
message's "sweeps EVERY report" is true, or says what it actually sweeps.

---

**R889. (DOES NOT BLOCK -- ledgered, and it is the one going to Xabier) "A DEADLOCK THAT HAD
ABSORBED SEVEN INTERIM CHECKS" IS A CAUSAL CLAIM IN THREE SHIPPED PLACES WITH NO CELL, AND THE
TIMELINE DOES NOT SUPPORT IT. THE SEVEN CHECKS EACH REVIEWED A REAL COMMIT AND PRODUCED FORTY
FINDINGS, TWO OF THEM BLOCKING DEFECTS IN `floatfea/run/`.**

```
claim  the deadlock did not consume the seven rounds; it made the hook's message useless for
       seven rounds, which is a different loss
cmd    docs/directives/FT.md:44 ; .claude/hooks/require-verdict.sh:157 ; f9954f7's message
out    "FT0 resolves a deadlock that had absorbed seven interim checks." / "This one forced
       seven." / "it masked the deadlock for seven rounds"
cell   the counterfactual, from the commit timeline: WHAT WOULD HAVE HAPPENED WITH A CORRECT
       HOOK? Each of the seven checks sits at a turn boundary that carried NEW implementer
       commits (0aa0c4a after e818375, 948b36a after e6a20e3, eb85d08 after d89566d,
       d06c577 after 945d250, 0a6edba after 82f922c, 52d3b7a after ff48a6d, 5ca5496 after
       154261e)
out    ES0 forces an interim check at exactly such a boundary REGARDLESS of the hook's
       message, so the COUNT is unchanged by FT0. What the deadlock changed is the MESSAGE:
       the gate named a diff against 8542d79 that no step-3 verdict could clear, so for
       seven rounds nothing in the loop was measuring "has this work been reviewed" -- that
       measurement came from the reviewer being invoked, which happened anyway. And the seven
       were not idle: R866 and R877 are two defects in floatfea/run/ those rounds found.
rule   BG0 -- a causal sentence carries the cell that isolates it; one variable moved, the
       rest held, or the sentence is rewritten as the bare measurement
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** It is on the list
       because FT3's checkpoint report goes to Xabier in this same turn and this sentence is
       part of the slippage account. Seven rounds attributed to a hook bug reads as seven
       rounds wasted; the measurement says the hook's SIGNAL was wasted and the rounds bought
       two element-adjacent defects. The honest form is the second, and it is also the better
       argument for FT0.
```

**Closed when** the sentence in `docs/directives/FT.md`'s commentary -- not the verbatim
directive block, which is Xabier's text and stays as received -- and in the hook comment says
what was measured: the gate's refusal named an unclearable diff for seven rounds, and
`stop_hook_active` is what ended the turns.

---

**R890. (DOES NOT BLOCK -- ledgered) THE CHECKPOINT'S "OF STEP 3'S NINE CODE COMMITS, TWO WERE
NEW FL2 ITEMS AND FIVE WERE REPAIRS TO THOSE TWO" DOES NOT REPRODUCE. THREE WERE. TWO OF THE
FIVE PREDATE BOTH FL2 COMMITS AND CANNOT BE REPAIRS TO THEM.**

```
claim  the 2-vs-5 input to the x1.5 loading is a miscount
cmd    git log --reverse --format="%h %ad %s" --date=short 8542d79..HEAD -- floatfea tests
out    10-18 e818375  R845/R846, step 2's carried items          <- repair, not to FL2
       10-18 e6a20e3  R850/R851/R853, "my own gate failed false" <- repair, PREDATES FL2
       10-18 d89566d  R860 "BEFORE FL2 LANDS", three figures     <- repair, PREDATES FL2
       10-19 d3306a6  FL2(a) member topology                     <- NEW ITEM 1
       10-19 cadbbf7  FL2(c) headings as a declared list         <- NEW ITEM 2
       10-19 e945b13  R866                                       <- repair TO item 2
       10-19 ff48a6d  R872/R873/R874                             <- repair TO that repair
       10-19 154261e  R877                                       <- repair TO that repair
       10-25 ba0ce03  the marker and the guard                   <- apparatus
       -- nine commits: 2 items, 3 repairs to them, 3 repairs to other step-3 findings (two
          of which are EARLIER in history than the items), 1 apparatus.
cmd    the two figures in the same table that DO reproduce
out    wc -l scripts/measure/f6a_required_section.py scripts/measure/f6b_truss_sizing.py
         -> 581 + 685 = 1266                                      EXACT
       grep -n "| total |" results/R1/example/report.md
         -> results/R1/example/report.md:89 carries | total | 97.27 |   EXACT
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none in this repository**
       -- the checkpoint report is a message and not a file, so neither FR1's head nor EZ0's
       surface reaches it, and I cannot review a document that is not in the tree. It is on
       the list because the number is the stated basis for the x1.5 loading and one command
       refutes it. **My schedule reading is below and it does not turn on this figure.**
```

**Closed when** the figure is re-derived from the log at the commit it is published at, or the
sentence states what it actually counts: repairs TO the two items, 3; repair commits in the
step, 6 of 9.

---

**R891. (DOES NOT BLOCK -- ledgered) REPLAY 1 IN `f9954f7`'s MESSAGE -- "(empty) exit=0 <- THIS
TREE CLEARS" -- IS FALSE AT HEAD. AT `cd126a6` THE HOOK BLOCKS, AND IT BLOCKS CORRECTLY.**

```
claim  the paste was taken before a later edit in the same turn changed its subject
cmd    the hook, at cd126a6, clean tree
out    BLOCK "floatfea/, tests/, or docs/reports/R1/step-3.md changed since the verdict at
       154261e..."  -- because `ba0ce03`, the NEXT commit, changed
       `tests/test_report_carried.py`, which is inside the gate's own pathspec
rule   CP3 -- a figure is pasted from the run that produced the artifact it is pasted into,
       and the pasting is the LAST edit; if an edit follows the paste, the paste is void
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- and the state
       that makes the figure false is itself the gate working: a tests/ change since the last
       verdict blocks until a new verdict covers it. The SUBSTANCE of replay 1 -- the deadlock
       is gone and the gate is clearable -- I verified independently by committing a step-3
       verdict at cd126a6 and watching it clear. The figure, not the finding.
```

**Closed when** the replay is re-run at the tip of the group it describes, or the message says
which commit each output was taken at.

---

**R892. (DOES NOT BLOCK -- ledgered) "AND THE CONTROL, ONE VARIABLE MOVED -- THE OLD HOOK ON
THIS SAME TREE" MOVED TWO. THE STASH RESTORED THE OLD HOOK AND THE OLD MARKER TOGETHER.**

```
claim  the control's output is the marker-2 horn, not the one-variable horn
cmd    old hook (git show 5ca5496:.claude/hooks/require-verdict.sh), marker left at 3 --
       ONE variable moved
out    BLOCK "...step 3 of R1 is under execution and docs/reports/R1/step-3.md does not
       exist." -- the OUTRIGHT REFUSAL horn
cmd    old hook, marker reverted to 2 -- TWO variables moved, which is what the stash did
out    BLOCK "...docs/reports/R1/step-2.md changed since the verdict at 8542d79..."
       -- the turn's stated output, reproduced exactly
rule   BG0 -- the cell is one variable moved, everything else held
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none**, and the deadlock is
       established either way: both horns are described in the commit's prose and I measured
       both. The label is what is wrong, and labelling a two-variable cell as one-variable is
       the specific thing BG0 was earned on.
```

**Closed when** the control says which two states it compares, or is re-run with the marker
held.

---

**R893. (DOES NOT BLOCK -- ledgered) ONE LIVE SITE STILL STATES THE PREMISE FT0 RETIRED AS A
RULE, AND NO LIVE PLAN STATES THE RULE THAT REPLACED IT.**

```
claim  a reader who finds the convention before finding the hook finds the retired version
cmd    grep -rn "advanced in the commit" (five live sites, classified)
out    docs/milestones/F2.md:22 -- "**It is advanced in the commit that adds the next step's
       report, not before.**"   <- stated as a RULE, in a plan
       docs/milestones/F6.md:145, docs/reports/F6/step-1.md:22 <- closed milestones' records
       the hook and the guard <- the new comments, quoting it as RETIRED (correct)
cmd    does the LIVE plan say what the rule is now?
out    docs/milestones/R1.md:5-6 -- the FB4 comment explains how the marker ARRIVED, not when
       it advances. grep -c "FT0" docs/milestones/R1.md -> 0
rule   CW0; and FP0 -- plans cite the directive files rather than paraphrasing them
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** F2 is closed and
       its plan is a record; the gap that matters is the live one -- R1's plan carries a
       marker at a step with no report and nothing beside it says that is now legal.
```

**Closed when** `docs/milestones/R1.md` names FT0 beside the marker (one line), and F2.md's
sentence is marked as the convention of its own milestone.

---

**R894. (DOES NOT BLOCK -- ledgered) R1's STEP-3 GATE ROW DOES NOT CARRY FT2's ITEMS 6 AND 7,
AND THE STEP WILL BE CLOSED AGAINST THAT ROW.**

```
claim  the plan's step-3 gate is now a strict subset of what step 3 must build
cmd    docs/milestones/R1.md:352-358, the step 3 row
out    it names: topology with the star default; the sizing analyses re-solving; optional
       analyses off by default; headings as a list with export refusing uncovered ones; the
       band check per case. **It does not name the multi-npz heading envelope (FT2.6) or
       R867-R869's eight topologies (FT2.7).**
cmd    grep -c "FT2\|FT0\|FT1" docs/milestones/R1.md
out    0
rule   FP0 -- "Plans and reports cite those files rather than paraphrasing them"; and R870,
       which is this same shape with the subset on the other side
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** It is on the list
       because a step's closure is judged against its gate row, and two of the five remaining
       items are not in it. One line citing `docs/directives/FT.md` closes it.
```

**Closed when** the step-3 row cites FT2's list, or the plan is re-locked with it (DK0: a
re-lock does not restart the round count, and this step has spent none of its three).

---

**One criterion observation, not a finding, said once.** The predicate reads "a finding or a
site of **the newest verdict**". 67 of this round's 299 reds name findings of EARLIER
unanswered verdicts (R846, R851, R853, R857-R860, R866, R873, R875), because the guard
parametrises over every unanswered finding in the file rather than over the newest round. My
predecessor read limb one as "the findings of verdicts with no answering report revision" and
I followed that reading, because the CAUSE is identical per id and EG3(i) asks for the cause.
A literal reading would make 67 reds blocking at every boundary, which cannot be the
intention. **If that reading is wrong, it is a criterion question for Xabier and not a round.**

## CI at the reviewed commit: the run EXISTS, the ladder is GREEN, the guards step is RED

**`gh run list --commit cd126a6` returns `[]` and the run EXISTS -- I did not take the empty
result for an unavailable check (CK2).** `gh run list -L 5` gives
`headSha cd126a65ffdc7b84d419922e3f54272d1ff0b7b5, workflowName CI`, run id **40251519070**,
with a runner, real steps and real durations, so CK2's third state does not apply. **It was
`in_progress` when I began and `completed / failure` when I read it, and I waited rather than
recording a conclusion I had not seen** -- which is the half my predecessor could not finish.

```
job  the verification ladder      SUCCESS   (rungs 1, 2, 3, 4, 5 and 6 all SUCCESS)
job  lint, unit and guards        FAILURE
     actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
     unit tests SUCCESS / guards and meta-tests FAILURE
     -- every step RAN. Nothing was skipped behind an earlier red, which is what CZ1 (iii)
        exists to see, and FP1's CI-only types-PyYAML red has stayed fixed.
job  CI determinism -- leg        skipped
job  CI determinism -- ten legs   skipped
```

**And the previous commit's run, which my predecessor could only record as unfinished:** run
39376665176 at `154261e` concluded **failure**, in the same `guards and meta-tests` step, with
the ladder green. The state has not changed shape between the two commits; the COUNT has.

CI: `299 failed, 1076 passed, 1 skipped in 663.08s` (305 FAILED lines, 299 unique -- three ids
appear three times each in the fetched log). Mine: `299 failed, 3647 passed, 1 skipped in
1033.69s`. **The two agree on 299 and on the per-test breakdown**, which is also the control
saying my probes did not leak: every probe ran in a worktree I then deleted, and the main
tree's `git status --porcelain` is empty.

The 299, each id tested against the FS1 predicate AS NARROWED BY FT1, per id and not by family:

```
235  test_every_named_site_is_touched_or_declared[<finding>-<path>[:line]]   limb one. Every
       finding prefix lies in R845..R886 -- the findings of step 3's seven interim verdicts,
       none of which has an answering report revision. Zero prefixes outside that range,
       checked mechanically.
 42  test_the_report_carries_the_finding[R845..R886]     limb one -- each NAMES a finding
  1  test_the_CI_section_is_about_the_REVIEWED_commit    limb one -- names 154261e, the
       newest verdict's reviewed commit
  1  test_the_Carried_table_is_what_the_generator_produces          limb one -- "47 generated
       rows are not in the report's Carried section", keyed on a table that cannot exist yet
  1  test_the_generator_would_catch_a_row_under_the_wrong_number    limb one, that generator's
       own control, same premise
  1  test_the_report_carries_a_WHOLE_SUITE_count         LIMB TWO under FT1 -- its subject IS
       the commit carrying it: suite_count.py measures a clean worktree AT a commit, so the
       line naming a sha cannot be inside that sha
  1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW      LIMB TWO under FT1 -- same shape: no
       run exists for a commit before it is pushed
  2  test_the_guard_survives_the_state[baseline] and
       [verdict_amended_after_the_commit_the_report_answers] -- both "expected a clean run",
       which no state can get on a tree carrying 282 boundary reds. Boundary consequence.
 15  test_the_guard_survives_the_state[...]  **FAIL BOTH LIMBS. CZ1 (iv). THIS IS R887.**
       FileNotFoundError in `_build` on docs/reports/R1/step-3.md, a path the newest verdict
       does not name (0 occurrences, measured).
---
299  284 with an exit, 15 WITHOUT. **FT1's narrowing orphans none of the 284** -- the two
     limb-two ids both have their own commit as subject, so the direction that could have
     cost something costs nothing (EH4 applied to a criterion edit).
```

## Corpus (EG4(e))

**THE PAUSE HELD. I added no corpus entries and committed nothing to `tests/corpus/`.**
Batches are paused until 28 October except mutation work on F4's load-mapping gate and EB6's
label-provenance gate; this diff touches neither.

**What I ran instead -- the recorded substitute, and the grid half produced the blocking
finding:**

* **A continuum grid over the parameter space the decision rule guards.** The decision rules
  here are the hook's refusal and the guard's assertion, and their parameter space is
  (marker value) x (which of the two files exist) x (which version of the rule). I ran it:
  markers 2, 3, 4 and 9; report-only, review-only, both, neither; the shipped hook and
  `5ca5496`'s; the shipped assertion and `5ca5496`'s; with and without a committed verdict at
  cd126a6; the planted report tracked and untracked; and the milestone letter swapped R1 ->
  F7 with everything else held. **That grid produced R887, R888, R891 and R892.** Twelve of
  its cells are pasted above with their outputs.
* **A regeneration check on a published deliverable: NOT RUN, and the premise is why.**
  `git diff 5ca5496..HEAD` over `floatfea`, `scripts` and `results` is empty on all three, so
  a regeneration cannot differ from the committed artifacts by construction. I verified the
  one deliverable figure the checkpoint cites instead (`results/R1/example/report.md:89`,
  exact). I record the substitution rather than claiming a run I did not make.
* **Twenty-three-state mutation work over the step's own apparatus, four full harness runs**
  (marker 3, marker 2, marker 3 with the probe repair, and the whole suite) -- the measured
  pair and the repair demonstration under R887.

Neither half would have come from reading the diff: the diff's configuration is the one the
commit chose, and R887 lives in the one file the turn did not run.

## Tolerances touched

**None.** `git diff 5ca5496..HEAD -- floatfea/tolerances.py` is empty, and the diff contains
no `floatfea/` change of any kind.

**And nothing in the diff is a tolerance under another name**, which I checked rather than
assumed: the hook change is a file-existence disjunction, the guard change is a set-membership
disjunction, and the two documentation changes move no number. The only numerals in the diff
are line counts and commit shas inside comments. No convergence threshold, no comparison
epsilon, no "small number" guard, no factor introduced to make two numbers agree.

## Next step opens when

**This is a HOLD on step 3, which stays open. It is the eighth interim check and it counts
against no round, so all three reviewed revisions remain available.**

**R887 is answered in the NEXT commit** -- that is FF0's own wording for this class, not my
preference -- together with **R888**, which is the same file and one character of glob. Both
are one-line resolver repairs and neither is new apparatus. **The condition is measured, so
there is nothing to interpret:** `tests/test_report_guard_states.py` runs with
`grep -c FileNotFoundError` equal to `0` and a full-file count of `10 failed, 13 passed` or
better, with the marker left at 3.

**Then FL2, in FT2's order, and nothing in this list displaces it.** R881 goes IN the commit
that builds FL2 item 3 and blocks there if item 3 ships without it. R882-R886 go in the next
commit that touches `_validated_wave_basis`, or into the first reviewed revision as
declarations of what was left and why. R867-R869 are FT2.7. R889-R894 are sentences and one
plan line; the two worth doing before the checkpoint goes out are **R889** and **R890**,
because both are in the account of the slippage.

**R880 still waits**, and for the third round running it did not misdirect me: I ruled under
`CLAUDE.md`'s predicate as FT1 narrowed it. Do not take it first.

**What I did NOT ask for.** No new guard, scanner, meta-test, detector or report generator.
R887 and R888 are repairs to existing apparatus under EK2; everything else is a sentence, a
glob, or a plan line. `docs/milestones/F2a.md` is where anything larger goes.

**Schedule, since FT3 asks for it at every reviewed revision and the turn asked me for a
sentence on the x1.5.**

**The loading is defensible as an average and it is on the wrong axis.** Three measurements:

1. **The build was fast and so were the repairs.** FL2(a), FL2(c) and all three repairs to
   them landed between 19:46 and 22:46 on 10-19 -- two items and three repairs in three hours,
   with four interim reviews inside the same window.
2. **The calendar cost was elsewhere.** `git log` shows no commit of any kind between
   `5ca5496` (10-19 23:22) and `f39cbd6` (10-25 17:46): **six days, and FT0's deadlock sat
   across all of them.** A repair-tail multiplier cannot model that, and x1.5 on 11 nominal
   days reserves nothing for it. The schedule has no line for interim checks either, and step
   3 has had eight.
3. **The risk is concentrated in items 4 and 5, not spread.** Those two move
   `scripts/measure/f6a_required_section.py` and `scripts/measure/f6b_truss_sizing.py` --
   1266 lines, measured, the figure reproduces -- onto the production path, and
   `scripts/measure/` is EZ0 surface: every number they publish becomes a number
   `floatfea run` publishes, and FM0's re-solve loop changes those numbers. That is the one
   remaining blocking head under FR1, and four consecutive rounds found their blocking finding
   by regenerating a deliverable. **I would load 4 and 5 by more than x1.5, 3, 6 and 7 close
   to nominal, and I would hold a day for the apparatus** -- this round is the second time in
   step 3 that gating apparatus, not the element, took the round.

**17 November is a credible date for the work. It is not credible for the work plus another
six-day apparatus stall, and FT0 removes the specific stall that caused the last one.** I am
not re-escalating: FR0 answered the escalation with "slip the date, keep the scope", the turn
is reporting the trajectory to Xabier on the day it is known, and FT2.6 and FT2.7 are new
scope added after 5 November was set -- which belongs in the checkpoint beside the date, and
the turn says it is there.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 154261e77740692b08917a1ff89b5fdfc7e5ced5
**Reviewed commit: `154261e77740692b08917a1ff89b5fdfc7e5ced5`.**
Verdict: PASS
Tests: 3649 passed, 271 failed, 1 skipped, 2 warnings in 1115.20 s (0:18:35)   (my own whole-suite run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the seventh in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **NOTHING
BLOCKS. R877 is answered, at the place my predecessor's condition named, and I verified it
through the real CLI on the configuration the defect lived on rather than by reading the
diff.** R876, R878 and R879's heading half are answered and I attacked each. Six ledger items
below, one of them placed into a specific future commit.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For each finding I state the silently wrong result it produces, or
that it produces none. **Not one of this round's six can be given FR1's sentence**, which is
why this is a PASS and not a HOLD with a caveat.

```
cmd    git log --oneline 52d3b7a..HEAD ; git diff --name-status 52d3b7a..HEAD
out    154261e -- ONE commit. M floatfea/run/pipeline.py /
       M tests/unit/test_headings_and_bem_coverage.py
       -- 2 files, 275 insertions, 8 deletions. floatfea/ and tests/ and NOTHING else.
cmd    git diff 52d3b7a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 52d3b7a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py        -- a file, as my instructions say it must be
cmd    git diff --stat 52d3b7a..HEAD -- .claude docs/SUPERVISOR.md
out    (empty)   -- NOT a STOP, and nothing to read line by line this round
cmd    git diff --stat 52d3b7a..HEAD -- results scripts/measure docs/reports
out    (empty)   -- no published deliverable moved in the diff, and no step report was
                    touched (EK3). I checked the deliverables by REGENERATING them anyway.
cmd    git status --porcelain      (before anything, and after fourteen mutation runs and
                                   seven CLI runs against a perturbed sidecar)
out    (empty) / (empty)   -- every probe restored from a saved copy; the md5 of
       data/f4/dynamic_inputs.provenance.json is 64a8ab15cc9b95739b55972d6609f81b before and
       after, and floatfea/run/pipeline.py compares byte-identical to its backup
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ;
         mypy floatfea scripts/f4_dynamic_residual.py       (CI's own three forms)
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 43 source files
cmd    python -m pytest -q tests/unit tests/regression/test_r1_published_artifacts.py
out    306 passed in 149.17s
       -- the turn's headline figure. **It reproduces exactly.** So does the prose guard:
          34 passed.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third and seven verdicts are now newer than it.
That is EG3 state (2) and it is the whole of this tree's red.

## The question the turn asked: the two uses of 360

**THE SPLIT IS RIGHT, AND I CAN NOW SAY SO AS A MEASUREMENT. I ALSO HAVE A STRONGER STATEMENT
THAN THE TURN MAKES ABOUT ITS OWN FIRST VERSION: THAT VERSION WAS NOT MERELY WRONG AT `450`,
IT WAS VACUOUS.**

```
claim  the normalised range check could not reject ANY finite value, so `450` was the first
       value tried and not the only one that passed
rule   `0.0 <= h % 360.0 <= 360.0`, the predicate the first version ran
cmd    the hand grid, then 200000 uniform draws on (-1e6, 1e6), seed 0
out    normalised form rejects: []                       <- from
         [-1e-16, -10.0, -360.0, 0.0, 45.0, 359.9, 360.0, 360.1, 450.0, 720.0, 1e6, +-1e300]
       raw form rejects: [-1e-16, -10.0, -360.0, 360.1, 450.0, 720.0, 1e6, 1e300, -1e300]
       random grid, 200000 draws, normalised form rejects: 0
judge  a check that cannot fail is the standing guard I apply to every gate, and the first
       version was one. `% 360.0` maps every finite real into `[0, 360)`, so the interval test
       downstream of it is a tautology; the only inputs it could ever have rejected are the
       non-finite ones the line above already rejects. **RAW IS STRICTLY STRONGER THAN
       NORMALISED HERE -- not better calibrated, strictly stronger.**
cmd    the second half of the turn's argument, checked rather than agreed
out    with the range check in place both arguments to `uncovered_headings` are confined to
       `[0, 360]`, so the surviving modulo can identify exactly ONE pair, `{0.0, 360.0}`.
       The equivalence is still an identity on a direction of travel (R872's argument, which
       I measured last round over the whole covered axis), and the raw domain check does not
       weaken it: `360.0` is admitted at the reader and still matches a declared `0.0`.
       Measured: heading_deg `360.0` ACCEPTED; `nextafter(360.0, 400.0)` REFUSED; `-0.0`
       ACCEPTED; `-1e-16` REFUSED by the domain rather than by the modulo, which also retires
       my own R872 caveat about `(-1e-16) % 360.0` being `360.0`.
```

**I did not find the contradiction the turn asked for. What I found is one consequence worth
recording rather than leaving, and it is R885 below** -- the raw domain refuses a legally
SIGNED recording, which `docs/conventions.md:150` says the BEM reader passes through with no
offset.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R877** (the wave basis validated behind `load_cases.headings`; `heading_deg: true` published `heading True deg` into three artifacts at exit 0) | **ANSWERED ON ITS BLOCKING SUBSTANCE, AT THE SITE MY CONDITION NAMED, AND I MEASURED IT ON THE CONFIGURATION THE DEFECT LIVED ON RATHER THAN THE ONE THE DIFF CHOSE. The second site the condition named is untouched -- R882 -- and it cannot produce a wrong result.** | `_validated_wave_basis`, called from `exported_wave_basis`. The validation is path-independent BY CONSTRUCTION: `exported_wave_basis(...)` is an ARGUMENT at the `refuse_headings_this_run_cannot_cover` call site, so it is evaluated before the early return that hid the first repair. My own runs, shipped example, NO `headings:` key, real CLI, outputs to a temporary directory: `heading_deg=true` -> EXIT=2, wrote=[]; `wave_height_full_m=true` -> EXIT=2, wrote=[]; a mapping `window` -> EXIT=2, wrote=[]; partial sidecar -> EXIT=2, wrote=[]. **Nothing is written in any of the four, so no zero-byte artifact survives either.** And the control: the untouched sidecar regenerates all three artifacts identically to the committed deliverables except the three provenance lines naming my temporary config and the wall-time table, with `governing U = 1.71167 at platform:hub4_arm ROOT` and `# wave basis: heading 0.0 deg; H_full 24.2 m; H_model 0.484 m` unchanged. The repair is inert on the default path, measured by running the model. |
| **R876** (nothing held the modulus; `% 180.0` and `% 90.0` were both green on 29) | **ANSWERED, and I re-solved the grid myself rather than reading the row** | three parametrisations in `tests/unit/test_headings_and_bem_coverage.py`. My mutation runs, file restored from a saved copy each time: `% 180.0` -> 2 failed, 51 passed; `% 90.0` -> 3 failed, 50 passed; baseline 53 passed. Both figures reproduce the turn's exactly. The row that does the work is `uncovered_headings((180.0,), (0.0,)) == (180.0,)` -- a head sea is not covered by a following sea -- and it reddens at every modulus below 360. |
| **R878** (`cli.py` subscripts four keys the reader built one at a time; a partial sidecar was a `KeyError` after the solve and a zero-byte CSV) | **ANSWERED, and the direction chosen is the one the repository's own discipline asks for** | complete-or-empty. Measured through the CLI: partial -> EXIT=2 with the missing key named, `wrote=[]`. Ablation: `missing = []` -> 5 failed, 48 passed, reproducing the turn's figure. **MY FIRST ATTEMPT AT THAT ABLATION WAS WRONG AND I SAY SO: I anchored on `if missing:`, which occurs THREE times in the pipeline module, so a single replacement mutated line 128 instead and the file reported 53 passed. The turn's figure is right and my first measurement of it was not.** New ground one level up is R884. |
| **R879** (NaN not refused by name; the recorded heading not range-checked at all) | **ANSWERED ON BOTH HALVES FOR `heading_deg`. NOT ANSWERED FOR THE TWO WAVE HEIGHTS, AND NOT DECLARED LEFT -- R881.** | NaN, `+inf` and `-inf` refused by name with "not finite"; `450.0`, `-10.0` and `360.1` refused by name against `HEADING`'s domain. Ablations: the finite check removed -> 3 failed, 50 passed; the range check removed -> 3 failed, 50 passed; the range check normalised again -> 3 failed, 50 passed; **the bool half alone removed -> 3 failed, 50 passed, so the bool check is still not redundant with the type check.** EH4's weakening direction, which nobody ran: the bound widened to `-1.0e9, 1.0e9` -> 3 failed, 50 passed, so the domain cannot be widened silently. |
| **R880** (my own agent definition cites "their two corrected lists", which FS1 deleted) | **STILL OPEN, CORRECTLY NOT IN THIS COMMIT, AND I ANSWER THE TURN'S QUESTION: DO NOT TAKE IT FIRST.** | It did not misdirect me this round or last: I ruled under `CLAUDE.md`'s FS1 predicate, per id, and said so both times. FS0 is explicit that apparatus work waits for FL2's items except an FR1-blocking finding, and R880 is not one; a standalone `process:` commit beside step code is what `CLAUDE.md` forbids, and the turn did not do it. **It waits. FL2 items 3, 4 and 5 are what the next commits are for.** |
| **R867, R868, R869** (of eight non-default topologies only one runs; the rest die in a `platform:hub1_arm_tip` lookup) | **still open, correctly, and correctly NOT in this commit -- carried by name into the first reviewed revision** | the diff since 52d3b7a over `floatfea/model`, `floatfea/solve` and the topology test file is empty. I did not reopen them. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a); two future-tense sentences) | **still open, untouched** | the two sentences at lines 123 and 180 of the pipeline module are unchanged; the diff's only pipeline hunks are the two import lines, the `_recorded_heading` comment, `WAVE_BASIS_KEYS` with `_validated_wave_basis`, and four lines inside `exported_wave_basis`. |
| **R862** (three hand copies of the stage set; the published total is the sum of a hand-copied four) | **still open and STILL NOT DUE -- I measured the trigger rather than taking the word for it** | the diff since 52d3b7a over `floatfea/cli.py` is EMPTY and no `timings[...]` assignment moved. No timed stage was added, so the understatement is not reachable at this commit. It blocks in the commit that adds one -- FL2 item 4 or 5, which is also where R881 lands. |
| **R863** (the exclusion set is defined by the code under test), **R864** (the byte-identity claim's witness is blind to its own subject), **R865** (a docstring in the regenerates test) | **all three still open, untouched** | the diff over `tests/regression` since 52d3b7a is empty; R864's condition is a sentence in a report revision that does not exist. |
| **R847 / C43** ("0 of 49 rows" does not reproduce), **R848** (the empty-directory refusal admits a bare dot), **R849 with R854** (four gates quantify over hard-coded three-file tuples) | **all still open, all untouched, all correctly so** | the diff over `floatfea/cli.py` is empty, which covers R848; the regression diff is empty, which covers R849 and R854; R847 needs a revision that does not exist. FR1's second and third non-blocking classes. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **ROUTED, not open -- FS3 ledgers it to FL3** | `docs/directives/FS.md`. Not open against step 3. |
| **R855** (the whole suite at a commit carrying no report revision) | **the standing condition IS MET, and I took the whole-suite number myself as I do by rule** | the turn states plainly which runs it made (306 over `tests/unit` plus the published-artifacts file, and the three lint forms in CI's own shapes) and that it made no whole-suite run at this sha. **No green is claimed that was not measured.** Mine: 271 failed, 3649 passed, 1 skipped. |
| **R856** (the verdict tool refused a step with no report) | **ANSWERED, and exercised a fourth time -- this file went through `--interim`** | `scripts/write_verdict.py`, unchanged by this diff. |
| **R835, R836, R871** (EG3's enumerated lists, and FS1's deletion of FC1's reason) | **ANSWERED by FS1, and I applied the PREDICATE PER ID to all 271 reds. 269 under limb one, 2 under limb two. NONE WITHOUT AN EXIT.** | measured in the CI section. The count moved 165 -> 271 because two guards parametrise over the newest verdict's OWN findings and sites, and the newest verdict is mine -- R861's point, and the reason there is no list to be short of. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally in CI's own three forms AND on a machine neither of us controls** | mine above; CI run 39376665176, job `lint, unit and guards`, read at STEP level: actionlint, ruff, black --check, mypy and **unit tests** all SUCCESS. Every step RAN. |
| **C42** (U+FFFD in historical verdict headers), **C44** | **mine, accepted, carried** | unchanged by this diff. |
| **C45** | **DOES NOT RECUR IN `CLAUDE.md` OR `docs/SUPERVISOR.md`, neither of which this diff touches. It still recurs in my own agent definition as R880**, eighth occurrence of the family. | measured in R880's row. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE two rounds ago by the control at `bd315a1` (149 passed, 0 failed) and I did not redo it** | ES0's light scope. The control's conclusion is unchanged and this round's 271 are the same two files. |
| the suite-count line, and CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer; it is limb two of the predicate by construction, and two of this round's 271 reds ARE it. |

## Findings

**NONE BLOCKS.** No tolerance moved, no conftest moved, no `.claude` or `docs/SUPERVISOR.md`
file moved, no published deliverable moved in the diff -- and I established the last of those
by regenerating all three from this tree rather than by reading it.

**AND THE TWO THINGS THE TURN CAUGHT ITSELF ARE BOTH REAL, AND ONE OF THEM IS WORSE THAN THE
TURN SAYS.** The normalise-before-comparing bug was VACUOUS and not merely wrong at `450`
(measured above). The R828 hole is closed by a case that reads a real sidecar off disk, and I
verified the cycle myself: the reader's call to the validator removed -> 1 failed, 52 passed.
**A self-caught item reported with its ablation is worth more than an item I find, and both
were.**

---

**R881. (DOES NOT BLOCK -- ledgered, and it is the highest-value item on this list) THE
RECORDED HEADING GETS ALL THREE OF THE DECLARED SIDE'S CHECKS AND THE TWO RECORDED WAVE
HEIGHTS GET TWO. `WAVE_HEIGHT` IS DECLARED IN THE SAME MODULE THE NEW CODE ALREADY IMPORTS
`HEADING` FROM, AND IT IS NOT APPLIED. A SIDECAR RECORDING `wave_height_full_m: -24.2` RUNS
TO EXIT 0 AND PUBLISHES A NEGATIVE WAVE HEIGHT INTO ALL THREE ARTIFACTS.**

```
claim  the repair's own stated discipline is three checks, and it is three for one field of
       three
rule   the docstring of `_validated_wave_basis`: "the declared side's discipline is three
       checks, not one. `config.py`'s `_checked` rejects a bool by name, rejects a
       non-number, and range-checks."
cmd    the declared side's bound, and the one line that uses it
out    floatfea/run/config.py:190  WAVE_HEIGHT: Final[Bound] = ("m", 0.0, 100.0)
       floatfea/run/config.py:931  height_m=_checked(_require(item, "H", at), f"{at}.H",
                                     WAVE_HEIGHT)
       -- a DECLARED wave height is bool-checked, NaN-checked AND range-checked, which is
          the exact asymmetry R879 was about, in the same function, one key over
cmd    the recorded side, at the reviewed commit
out    floatfea/run/pipeline.py:722 -- the loop runs the type check and the finite check over
       all three numeric fields; the range check below it reads `present["heading_deg"]`
       alone, and `HEADING` is the only bound imported at floatfea/run/pipeline.py:52
cell   ONE VARIABLE MOVED: one field of the committed sidecar, nothing else, through the real
       CLI, outputs to a temporary directory, sidecar restored and md5-verified after each
out    wave_height_full_m = -24.2   -> EXIT=0, three artifacts written
         report.md            * **wave height** - -24.2 m full scale (0.484 m model)
         member_forces.csv    # wave basis: heading 0.0 deg; H_full -24.2 m; H_model 0.484 m
         utilisation.csv      the same header block
       wave_height_model_m = 1e9    -> EXIT=0, three artifacts written
         report.md            * **wave height** - 24.2 m full scale (1000000000.0 m model)
       -- and the second pair cannot both be true: the same sidecar records `lambda = 50.0`,
          so a model height of 1e9 m beside a full-scale height of 24.2 m is a published
          contradiction, at exit 0, in every artifact
rule   FR1 head one, tested and NOT met: the number published is the number recorded, and
       nothing in `floatfea/` computes with the recorded wave height at this commit -- the
       period-band check is FL2 item 3 and is unbuilt, and the measure scripts compute their
       band from their own `WAVE_HEIGHT_FULL_M = 24.2` rather than from the sidecar. FR1 head
       two is the closer call and I rule it out on the ground my predecessor's R874 used:
       `-24.2 m` is absurd on the face of the artifact rather than plausible, and the range
       check would not catch a PLAUSIBLE wrong height anyway -- every plausible value is
       inside [0, 100].
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES AT THIS COMMIT: none.**
       **IT BLOCKS IN THE COMMIT THAT MAKES A RECORDED WAVE HEIGHT REACH A NUMBER -- FL2
       ITEM 3, THE PERIOD-BAND CHECK, WHICH IS KEYED ON H** -- the same placement R862 has,
       and for the same reason. Half of R877's closing condition said these two fields get
       the heading's treatment ("`wave_height_full_m` and `wave_height_model_m` the same"),
       half of R879's offered the escape that the revision states which check was left and
       why, and this commit takes neither. One `for` loop and one bound.
```

**Closed when** the two recorded wave heights are range-checked against `WAVE_HEIGHT` by name
in `_validated_wave_basis`, or the first reviewed revision states that the range was left for
the heights and why -- and if it is left, the sentence says what happens when FL2 item 3
reads it.

---

**R882. (DOES NOT BLOCK -- ledgered) R877's CLOSING CONDITION NAMED TWO SITES AND THE SECOND
IS UNTOUCHED AND NOT DECLARED LEFT. THE REFUSAL STILL SAYS "OR REMOVE `load_cases.headings` SO
NO COMPARISON IS CLAIMED" -- ADVICE THAT IS NOW FALSE RATHER THAN DANGEROUS, AND THAT NO
PRODUCTION RUN CAN EVER PRINT.**

```
claim  the clause the condition named is unchanged, and the commit says nothing about it
cmd    the condition, and the line
out    my own previous verdict: "The refusal message's last clause, which currently reads
       'or remove `load_cases.headings` so no comparison is claimed', stops recommending the
       unvalidated path."
       floatfea/run/pipeline.py:597 -- "Fix the sidecar beside the npz, or remove
       `load_cases.headings` so no comparison is claimed." UNCHANGED by this diff.
cmd    whether the advice is still dangerous, or merely wrong
out    `heading_deg = true` with NO `headings:` declared -> EXIT=2, wrote=[]. **Following the
       advice no longer publishes anything, because the reader refuses first.** So the clause
       cannot route anyone to a publication; what it can still do is tell a reader that
       removing a configuration key will make a refused run proceed, which it will not.
cmd    and whether the sentence is reachable at all
out    `_recorded_heading` is called only from `refuse_headings_this_run_cannot_cover`
       (floatfea/run/pipeline.py:633), whose only production caller passes
       `exported_wave_basis(...)` -- a basis already refused if it is bad. So the refusal at
       floatfea/run/pipeline.py:589 is UNREACHABLE on every production path and survives only
       as a unit-tested defence.
rule   FR1's FIRST non-blocking class, verbatim -- "a refusal whose message is unclear but
       whose outcome is right"; and `CLAUDE.md`, "a closing condition that names sites is
       closed site by site. Half of an item is not the item."
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** It is on the list
       because a condition named it, the commit neither did it nor declared it left, and the
       turn's own summary reads "answered at the place you named" -- true of the first site
       and not of the second. I am not asking for a prettier comment: I am asking that the
       one sentence in this repository that tells a reader how to make this refusal go away
       stops naming a key that no longer has that effect.
```

**Closed when** that clause says what is true at this commit, or the first reviewed revision
records that it was left and why -- and, in the same place, whether a defence no production
path can reach is kept deliberately or deleted.

---

**R883. (DOES NOT BLOCK -- ledgered) TWO SENTENCES IN `_validated_wave_basis`'s OWN DOCSTRING
AND REFUSAL TEXT ARE FALSE AT THIS COMMIT, AND ONE IS FALSE ABOUT THE CASE IT NAMES.
`10**400` IS NOT "CAUGHT BEFORE `float()` RAISES `OverflowError`" -- IT RAISES
`OverflowError`, FROM INSIDE THE VALIDATOR.**

```
claim  the docstring states an outcome the code does not produce
cmd    the sentence
out    floatfea/run/pipeline.py:712 -- "NaN and infinity are refused here BY NAME rather than
       one line later by the coverage message, and `10**400` is caught before `float()`
       raises `OverflowError`."
cell   the committed sidecar with `heading_deg` set to `10**400` -- a JSON bignum, which
       `json.loads` parses as an `int` -- and nothing else changed, through the real CLI
out    EXIT=1, traceback, wrote=[]
         if not math.isfinite(float(value)):
                              ~~~~~^^^^^^^
         OverflowError: int too large to convert to float
       -- the `float()` that raises IS the one inside the claimed check. Same at the function
          level, for `heading_deg` and for `wave_height_full_m` alike.
cmd    the second sentence, which is the refusal a bad WAVE HEIGHT prints
out    `wave_height_full_m = true` -> "`run.wave_height_full_m` is True (bool), not a number.
       A LIST here is a multi-heading export meeting a single-heading reader" -- a wave height
       is told it might be a multi-heading export. The text is the heading's, used for three
       fields.
rule   CW0 -- prose in the SOURCE TREE does not claim things about the code: "a claim about
       this repository written in a comment, a docstring or a plan is one of three things: a
       test, a triple, or deleted"; and FR1's first non-blocking class for the message half.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- exit 1, a
       traceback, and nothing written, which is the outcome my predecessor recorded for this
       input one function away. It is on the list because the sentence was written in the
       course of answering a finding, which is CP2's exact shape, and because a later reader
       who believes it will not add the guard it describes.
```

**Closed when** the bignum is refused by name -- an `abs(value) > sys.float_info.max` test,
or an `except OverflowError` around the existing line -- or the sentence is deleted; and the
three fields' refusal text names the field's own failure mode rather than the heading's.

---

**R884. (DOES NOT BLOCK -- ledgered) COMPLETE-OR-EMPTY HOLDS ONLY WHEN `run` IS A MAPPING. A
SIDECAR WHOSE `run` BLOCK IS A LIST PUBLISHES "wave basis: NOT RECORDED" AT EXIT 0 -- WHICH IS
THE "WRONG, NOT ABSENT" DISTINCTION R878 WAS BUILT ON, APPLIED ONE LEVEL UP.**

```
claim  the new rule is enforced on the four keys and not on the container they come from
cmd    the line that reads the container
out    floatfea/run/pipeline.py:802 -- `run_block = recorded.get("run", {})`, with no type
       check, and the `except` above it covers `(OSError, json.JSONDecodeError)` only -- so a
       well-formed JSON of the wrong SHAPE is not an unreadable file
cell   `exported_wave_basis` against six sidecars that are all valid JSON, one variable each
out    {"run": [1, 2]}        -> {}     <- publishes "wave basis: NOT RECORDED by the export
                                            of this dynamic-inputs file", at exit 0
       {"other": 1}           -> {}     <- legitimate, and indistinguishable from the above
       {"run": "heading_deg"} -> *** TypeError: string indices must be integers
       {"run": 5}             -> *** TypeError: argument of type 'int' is not iterable
       [1, 2]                 -> *** AttributeError: 'list' object has no attribute 'get'
       "nope"                 -> *** AttributeError: 'str' object has no attribute 'get'
rule   the commit's own reason for R878, quoted: "A partial sidecar is refused by name rather
       than downgraded to 'not recorded', because a sidecar missing one field is WRONG and not
       ABSENT." A `run` block of the wrong type is wrong and not absent by the same argument,
       and it is the one case of the six that reaches exit 0.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- four of the six
       are exit-1 tracebacks with nothing written, and the fifth publishes a statement that
       WITHHOLDS a fact rather than asserting a wrong one. "NOT RECORDED ... no caveat below
       should be read as supplying them" is the conservative direction, which is why this is
       a ledger item and not a block. It is on the list because the commit chose a rule and
       the rule's own argument reaches one level further than the code does. Pre-existing in
       shape; newly inconsistent with a rule this commit wrote.
```

**Closed when** `run` is refused by name unless it is a mapping, in the same function -- or
the first reviewed revision records that a malformed container is deliberately read as NOT
RECORDED, with the sentence a reader of the artifact is entitled to.

---

**R885. (DOES NOT BLOCK -- ledgered) THE RAW DOMAIN CHECK REFUSES A SIGNED RECORDING, AND
`docs/conventions.md:150` RECORDS THAT THE BEM READER CONVERTS A HEADING "STRAIGHT THROUGH ...
WITH NO SIGN FLIP AND NO OFFSET". THE CHOICE IS RIGHT AND IT IS RECORDED ON ONE SIDE ONLY.**

```
claim  `0..360` raw is a claim about what a RECORDED heading is, and a producer exists that
       can record the other thing
cmd    the only producer of this sidecar, at this commit
out    scripts/export_f4_dynamic_inputs.py:524 -- `"heading_deg": float(rjr.WAVE_HEADING_DEG)`
       scripts/report_joint_reactions.py:93    -- `WAVE_HEADING_DEG: Final[float] = 0.0`
       -- a hand-set constant, in [0, 360] by construction. **NOTHING IS BROKEN TODAY.**
cmd    the producer named in the conventions, which is the one FL(c) reaches for
out    docs/conventions.md:150 -- "`readers/capytaine.py:191-194` converts it straight through
       as `heading_deg = rad2deg(wave_direction)` with no sign flip and no offset"
       -- a dataset carrying `wave_direction = -0.1745` rad records `-10.0`, a legal 350 deg
          heading, which `_validated_wave_basis` now refuses by name
cell   `_validated_wave_basis` with heading_deg `-10.0` -> ConfigError, "outside the declared
       domain 0.0..360.0 deg"; and the comparison side, measured last round, ACCEPTS `-10.0`
       against a declared `350.0` as the same direction of travel
rule   EH4 -- a boundary is solved in both directions, including the two that weaken a gate.
       This is the direction that STRENGTHENS one, and the cost of a strengthening is an
       over-refusal; FR1 then says an over-refusal does not block, because it cannot
       under-refuse.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- exit 2, nothing
       written, a message naming the domain. It is on the list because the turn asked me to
       contradict the split and this is the only thing I found: the two uses of 360 now
       disagree about what a heading IS, the disagreement is CORRECT, and the code records
       only one half of it. R872's closing condition asked for exactly that choice to be
       recorded on the declared side and it was; this is the recorded side's half.
```

**Closed when** the comment in `_validated_wave_basis` says which of the two the repository
means -- a recorded heading is bounded `0..360` RAW and a signed recording is a refusal, or a
signed recording is normalised at the reader before the domain check -- naming
`docs/conventions.md:150` as the reason the question exists.

---

**R886. (DOES NOT BLOCK -- one line) THE `# noqa: F401` THIS COMMIT ADDED SUPPRESSES NOTHING
TODAY AND COVERS FOUR IMPORTS TOMORROW.**

```
claim  the suppression is dead, and ruff is green without it
cmd    the line, then ruff with it and with it removed
out    tests/unit/test_headings_and_bem_coverage.py:35 --
         `from floatfea.run.pipeline import (  # noqa: F401`
       all four names are used in the file (`_validated_wave_basis` 10 times,
       `refuse_headings_this_run_cannot_cover` 13, `refuse_uncovered_headings` 8,
       `uncovered_headings` 18)
       `ruff check floatfea tests scripts`             -> All checks passed!
       the same with the `# noqa` deleted              -> All checks passed!
       pyproject.toml:110 `select = ["E","F","I","UP","B","SIM","NPY"]` -- RUF100 is not
       selected, so nothing in this repository reports a dead suppression
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none.** A blanket F401 on
       a four-name import is a guard switched off for a block rather than for a line, in the
       one place a reader looks when a helper stops being exercised.
```

**Closed when** the `# noqa: F401` is deleted, or it sits on the single name it is for.

## CI at the reviewed commit: the run EXISTS, the guard step had NOT FINISHED, 271 local reds

**`gh run list --commit 154261e` returns `[]` and the run EXISTS. I did not take the empty
result for an unavailable check (CK2).** `gh run list -L 6` gives
`headSha 154261e77740692b08917a1ff89b5fdfc7e5ced5, workflowName CI`, run id **39376665176**.
It has a runner, real steps and real durations, so CK2's third state -- allowance exhausted --
does not apply.

```
job  the verification ladder      SUCCESS   (rungs 1, 2, 3, 4, 5 and 6 all SUCCESS)
job  lint, unit and guards        actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS /
                                  mypy SUCCESS / unit tests SUCCESS /
                                  guards and meta-tests IN PROGRESS when I read it
     -- every step RAN. Nothing was skipped behind an earlier red, which is what CZ1 (iii)
        exists to see, and FP1's CI-only `types-PyYAML` red has stayed fixed.
job  CI determinism -- leg        skipped
job  CI determinism -- ten legs   skipped
```

**THE GUARD STEP HAD NOT FINISHED WHEN I READ IT, AND A RUN THAT HAS NOT FINISHED IS NOT A
PASS.** I record that rather than a conclusion I did not see. What I did instead is the
measurement that step takes: my own whole-suite run at the reviewed commit, **271 failed,
3649 passed, 1 skipped**, with every red inside the two report-guard files -- which is also
the control that says my fourteen mutation runs did not leak, because
`tests/unit/test_headings_and_bem_coverage.py` is GREEN in that output while every one of the
ablations reddens it.

The 271, each id tested against the FS1 predicate rather than against any list:

```
220  test_every_named_site_is_touched_or_declared[...]   limb one. Each id is
       `<finding>-<path>[:line]`, and I checked the finding prefix of all 220 mechanically:
       every one lies in R850..R880, the findings of verdicts with no answering report
       revision. Zero prefixes outside that range.
 36  test_the_report_carries_the_finding[R845..R880]     limb one -- each NAMES a finding,
       contiguous; 31 last round plus R876..R880
 10  test_the_guard_survives_the_state[...]              limb one via the red `baseline`,
       which is itself in the FAILED list; the cascade is identified by the baseline being
       red and by each state's own failure line, not by its name
  1  test_the_CI_section_is_about_the_REVIEWED_commit     limb one -- names the reviewed commit
  1  test_the_Carried_table_is_what_the_generator_produces        limb one
  1  test_the_generator_would_catch_a_row_under_the_wrong_number  limb one, the generator's
       own control, keyed on a Carried table that cannot exist yet
  1  test_the_report_carries_a_WHOLE_SUITE_count         LIMB TWO -- "the newest revision
       carries no whole-suite line"; the suite-count script measures a clean worktree AT a
       commit, so the line naming a sha cannot be inside that sha
  1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW      LIMB TWO -- "run 39162423263: the
       table says `no result (status in_progress)`, gh says `failure`". The table recorded
       the only status that existed when the revision was written
---
271  269 under limb one, 2 under limb two. NONE WITHOUT AN EXIT. No red is CZ1 (iv).
```

## Corpus (EG4(e))

**THE PAUSE HELD. I added no corpus entries and committed nothing to `tests/corpus/`.**
Batches are paused until 28 October except mutation work on F4's load-mapping gate and EB6's
label-provenance gate, and this diff touches neither.

**What I ran instead, which is the recorded substitute, and both halves produced a finding:**

* **A continuum grid over the parameter space the decision rule guards** -- the two 360s: the
  normalised predicate over a hand grid of twelve values and 200000 uniform draws (0
  rejections, the vacuity measurement above), the raw predicate over the same grid, and
  fifteen single-field perturbations of the committed sidecar at the function level (`True`,
  `[0.0, 45.0]`, `{"a": 1}`, `"0.484"`, `None`, `nan`, `+inf`, `-inf`, `10**400`, `-0.0`,
  `-1e-16`, `360.0`, `nextafter(360)`, `-24.2`, `1e9`). That grid produced **R881** and
  **R883**, and six malformed containers produced **R884**.
* **A regeneration check on a published deliverable** -- `report.md`, `member_forces.csv` and
  `utilisation.csv` regenerated from this tree through the real CLI seven times: once clean,
  against the three committed files, and six times against a perturbed sidecar. The clean run
  is identical except the three provenance lines naming my temporary config and the wall-time
  table. The perturbed runs are where **R881** became a publication rather than a return
  value, and where R877's repair was measured on the path that had no `headings:` key.
* **Fourteen mutation runs over the step's own gate**, including the four ablations the turn
  published -- all four reproduce exactly -- and EH4's weakening direction on the new bound,
  which nobody had run: the domain widened to `-1.0e9, 1.0e9` gives 3 failed, 50 passed.

Neither half would have been found by reading the diff: the diff's configuration is the one
the commit chose, and R881 lives on a field the commit's own cases do not vary.

## Tolerances touched

**None.** `git diff 52d3b7a..HEAD -- floatfea/tolerances.py` is empty.

**And the new function carries NO local numeric literal, which I checked rather than
assumed.** `_validated_wave_basis` reads its bound as `low, high = HEADING[1], HEADING[2]`
from `floatfea/run/config.py`, which this commit added to the import at
`floatfea/run/pipeline.py:52`. There is no new comparison epsilon, no "small number" guard and
no factor introduced to make two numbers agree: `math.isfinite` is a predicate, not a
threshold, and the `360.0` in the function's comment is prose about a modulus that lives
elsewhere and did not move. **A repair that needed a bound and imported the declared one is
the right shape** -- and it is why R881 is a one-loop item rather than an argument about what
the bound should be.

## Next step opens when

**This is a PASS. Step 3 stays open because its work is not finished -- this is the seventh
interim check and it counts against no round -- and all three reviewed revisions remain
available. Nothing here displaces FL2.**

**WHAT I AM ASKING FOR NEXT IS FL2 ITEMS 3, 4 AND 5, NOT THIS LIST.** Under FS0 the order is
the plan's, and none of R881..R886 is FR1-blocking, so none of them earns a commit of its own
ahead of the period-band check. The placements:

* **R881 goes IN the commit that builds FL2 item 3**, the period-band check, because that is
  the commit where a recorded wave height stops being provenance and starts being a number --
  the same placement R862 has, and R862 lands in item 4 or 5 by the same rule. **If item 3 is
  built without it, it blocks there.**
* **R882, R883, R884 and R885 are four sentences and one type check in one function**, and go
  in the next commit that touches `_validated_wave_basis` for any reason, or into the first
  reviewed revision as declarations of what was left and why. R886 is one line.
* **Still blocking by name into the first reviewed revision, unchanged:** R867, R868, R869 as
  one repair, and R870.
* **R880 waits**, and the turn placed it correctly: it is my own instructions, it is not
  FR1-blocking, FS0 says apparatus waits for FL2, and it did not misdirect me in either of
  the two rounds since it was written -- I ruled under `CLAUDE.md`'s predicate and said so
  both times. Do not take it first.

**What I did NOT ask for.** No new guard, scanner, meta-test, detector or report generator.
R881 is a bound already declared in a module already imported, R882/R883/R885 are sentences,
R884 is a type check in an existing function, R886 is a deletion. `docs/milestones/F2a.md` is
where anything larger goes.

**Schedule, since the turn stated it and was right to.** FS4's checkpoint is 26 October, seven
days out; FL2 items 3, 4 and 5 plus FM0's re-solve loop are what remains; step 3 has now spent
seven interim checks and no reviewed revision. **I am not re-escalating** -- FR0 already
answered the escalation with "slip the date, keep the scope", and the turn is reporting the
trajectory to Xabier in the same turn, which is what `CLAUDE.md` asks for on the day it is
known. What I record is the pattern the turn names and the measurement that supports it: four
of the last five blocking findings were on the unmeasured half of a repair, each was one
function, and **every one was found by running the model at a configuration the diff did not
choose.** Seven CLI runs is twelve minutes. That is the trade EU1 and FR1 were both written to
make, and it is cheaper than the round it saves.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: ff48a6d4b60919485e1bf76fa9a81972f22d31b9
**Reviewed commit: `ff48a6d4b60919485e1bf76fa9a81972f22d31b9`.**
Verdict: HOLD
Reviewed commit: ff48a6d4b60919485e1bf76fa9a81972f22d31b9
Tests: 3617 passed, 165 failed, 1 skipped, 2 warnings in 1131.79 s (0:18:51)   (my own whole-suite run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the sixth in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available.
**ONE FINDING BLOCKS -- R877 -- and it is a correction to my predecessor's closing condition
rather than a failure of the repair that answered it.** R872 and R873 are answered and I
attacked both rather than reading them. R874 is answered AT THE SITE THE CONDITION NAMED and
the defect it was written about is still live one function away, on the default path.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For each finding I state the silently wrong result it produces, or
that it produces none. **R877 blocks under FR1's SECOND LIMB -- "an input accepted and used
other than as declared" -- which is the limb `CLAUDE.md` says is easy to read past, and which
my own previous verdict read past on this exact finding.** I say that plainly below because
the cost of the round is mine, not the implementer's.

```
cmd    git diff --name-status 0a6edba..HEAD
out    M docs/SUPERVISOR.md / M floatfea/run/pipeline.py /
       M tests/unit/test_headings_and_bem_coverage.py
       -- 3 files, 129 insertions, 9 deletions. TWO commits, correctly split:
          a4ab04d touches docs/SUPERVISOR.md and NOTHING else; ff48a6d touches
          floatfea/ and tests/ and NOTHING else.
cmd    git diff 0a6edba..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0a6edba..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py        -- a file, as my instructions say it must be
cmd    git diff --stat 0a6edba..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 6 +----- (1 insertion, 5 deletions); .claude EMPTY
       -- NOT a STOP. a4ab04d is a STANDALONE process: commit citing FS1 whose only file is
          docs/SUPERVISOR.md. I read every one of the six lines: the dangling "The two lists,
          corrected (EH1)" paragraph goes, and the "only those" clause is rewritten as the
          claim it actually makes. **No guard was removed and nothing was weakened.** R875 is
          answered.
cmd    git diff --stat 0a6edba..HEAD -- results scripts/measure docs/reports
out    (empty)   -- no published deliverable moved in the diff, and no step report was
                    touched (EK3). I checked the deliverables by REGENERATING them anyway,
                    which is where R877 and R878 came from.
cmd    git status --porcelain
out    (empty)   -- clean before I ran anything and after. My mutation runs were reverted
                    from a saved copy and the tree is byte-identical to ff48a6d.
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ;
         mypy floatfea scripts/f4_dynamic_residual.py       (CI's own three forms)
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 43 source files
cmd    python -m pytest -q tests/unit            -- the commit's own headline figure, re-taken
out    236 passed in 133.64s
       -- the report claims 236 passed. **It reproduces exactly.** So does the prose guard:
          34 passed.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third and six verdicts are now newer than it.
That is EG3 state (2) and it is the whole of this tree's red.

**WHERE MY OWN INSTRUCTIONS DISAGREE WITH `CLAUDE.md`, I RULED UNDER `CLAUDE.md` AND SAY SO.**
My agent definition cites "**EG3**, **EH1**, **EJ2** and **FC1** -- the two boundary states,
their two corrected lists". FS1 replaced the lists with the predicate and `CLAUDE.md` carries
the predicate. I classified all 165 reds under the FS1 PREDICATE, not under any list. That
disagreement is R880 and it is a `process:` commit for Xabier, not a round.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R872** (`headings: [360.0]` refused against an export at 0 deg, the same wave direction) | **ANSWERED, AND I ATTACKED IT IN THE DIRECTION THE COMMIT DID NOT RUN -- THE COVERED SIDE, WHICH `HEADING` DOES NOT BOUND. The modulo is sound and I can now say so as a measurement rather than as agreement.** | `floatfea/run/pipeline.py:558-559`. The implementer named the gap itself -- "I did not test a negative covered heading" -- so I ran the covered axis as a continuum grid: `-10.0` against declared `350.0` ACCEPTED, `450.0` against `90.0` ACCEPTED, `-360.0` and `720.0` against `0.0` ACCEPTED, and every one of those is the same direction of travel under `docs/conventions.md:143-147`, which fixes heading 0 on +X as direction-of-travel in a right-handed frame and places no bound on the sense. **There is no pair that passes under the modulo and is a different direction**, because mod-360 equivalence on a direction of travel is an identity and not an approximation. `inf`, `nan`, a `dict` and `1e40` are all refused. The near-miss survives: `44.9` against `45.0` refused, and `450.0000000001` against `90.0` refused. **Two caveats recorded rather than left: the repair is at `uncovered_headings` and not at the site my predecessor's condition named (`:586`), so it also normalises the BEM-dataset caller where that condition said exact equality was right -- sound, but wider than asked, and the report revision should say so; and `% 360.0` is NOT canonical at the negative epsilon -- `(-1e-16) % 360.0` is `360.0`, not `359.99...`, so a recorded `-1e-16` against a declared `0.0` or `360.0` is REFUSED. That is an over-refusal at 1e-16 deg and it cannot under-refuse.** Not a finding. |
| **R873** (a sidecar whose `heading_deg` is a LIST makes the comparison raise `TypeError` instead of comparing) | **ANSWERED on two of the three sites the condition named. THE THIRD -- NaN BY NAME -- IS NOT DONE AND THE COMMIT DOES NOT DECLARE IT UNANSWERED. R879.** | `floatfea/run/pipeline.py:580-593`. A list and a dict are refused by name, verified. The condition read "a non-scalar, a bool and a NaN each refused by name". `{"heading_deg": nan}` passes `_recorded_heading` (`isinstance(nan, float)` is `True`) and is then caught one line later by the COVERAGE message -- "this run covers nan deg" -- not by name. The declared side refuses NaN by name at `floatfea/run/config.py:208-211` with "NaN is not a value", which is the discipline R874's condition asked for. Half of an item is not the item. |
| **R874** (the declared side refuses a bool by name in eleven places and the recorded side coerces one; a run publishes `heading True deg`) | **ANSWERED AT THE SITE THE CONDITION NAMED AND THE DEFECT IS LIVE ONE FUNCTION AWAY. R877, AND IT BLOCKS.** | `_recorded_heading` is called from inside `refuse_headings_this_run_cannot_cover`, which returns at `:629-630` when `declared` is empty. **With no `load_cases.headings` -- the default, what the shipped example declares and what the regression golden runs -- `_recorded_heading` never executes and `heading True deg` reaches `report.md` and both CSVs at EXIT 0.** Measured through the real CLI. My predecessor's condition named `floatfea/run/pipeline.py:583-586` and that site was the wrong site for the defect its own `cmd` row described (`floatfea/cli.py:146 prints basis["heading_deg"] verbatim`). The condition is mine to correct. |
| **R875** (`docs/SUPERVISOR.md` carried a paragraph introducing a quote that is gone, and `CLAUDE.md` did not) | **ANSWERED, and the audit the condition asked for is the one that was done.** | The condition read "after the whole EG3 section has been read top to bottom rather than grepped". a4ab04d did exactly that and its commit message says so with the line counts. I re-measured both files: "The two lists, corrected", "short by two names", "only those", "LIST GAINS" and "The only failures are" are all 0 in both. The surviving sentence states the claim and points at no deleted set. |
| **R867, R868, R869** (of eight non-default topologies only one runs; the rest die in a `platform:hub1_arm_tip` lookup) | **still open, correctly, and correctly NOT in this commit** | the diff over `floatfea/model`, `floatfea/solve` and `tests/unit/test_topology_from_config.py` since 0a6edba is empty. Placed as one repair in the first reviewed revision and the turn carries them there. I did not reopen them. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a); two future-tense sentences) | **still open, untouched** | `floatfea/run/pipeline.py:123` and `:180` unchanged; the only pipeline hunks in this diff are `uncovered_headings`, `_recorded_heading` and two lines in `refuse_headings_this_run_cannot_cover`. |
| **R862** (three hand copies of the stage set; the published total is the sum of a hand-copied four) | **still open and STILL NOT DUE -- I measured the trigger rather than taking the word for it** | the five `timings[...]` assignments are unchanged, `WALL_TIME_STAGES` at `floatfea/cli.py:37-43` is unchanged, and the diff over `floatfea/cli.py` is EMPTY. No timed stage was added, so the understatement is not reachable at this commit. It blocks in the commit that adds one -- FL2 item 4 or 5. |
| **R863** (the exclusion set is defined by the code under test), **R864** (the byte-identity claim's witness is blind to its own subject), **R865** (the docstring at `tests/regression/test_r1_example_regenerates.py:224`) | **all three still open, untouched** | the diff over `tests/regression` since 0a6edba is empty; R864's condition is a sentence in a report revision that does not exist. |
| **R847 / C43** ("0 of 49 rows" does not reproduce), **R848** (the empty-directory refusal admits a bare dot), **R849 with R854** (four gates quantify over hard-coded three-file tuples) | **all still open, all untouched, all correctly so** | the diff over `floatfea/cli.py` is empty, which covers R848; the regression diff is empty, which covers R849 and R854; R847 needs a revision that does not exist. FR1's second and third non-blocking classes. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **ROUTED, not open -- FS3 ledgers it to FL3** | `docs/directives/FS.md:28`. Not open against step 3. |
| **R855** (the whole suite at a commit carrying no report revision) | **the standing condition IS MET, and I took the whole-suite number myself as I do by rule** | the turn states plainly which runs it made (`tests/unit` 236, the prose guard 34, the three lint forms) and that it made no whole-suite run at this sha. **No green is claimed that was not measured.** My own whole-suite run: 165 failed, 3617 passed, 1 skipped. |
| **R856** (write_verdict.py refused a step with no report) | **ANSWERED, and exercised for the third time -- this file went through `--interim`** | `scripts/write_verdict.py:166-180` and `:233-236`, unchanged by this diff. |
| **R835, R836, R871** (EG3's enumerated lists, and FS1's deletion of FC1's reason) | **ANSWERED by FS1 as completed by 82f922c and a4ab04d, and I applied the PREDICATE PER ID to all 165 reds. 163 under limb one, 2 under limb two. NONE WITHOUT AN EXIT.** | `CLAUDE.md:429-449`, `docs/SUPERVISOR.md`. Measured in the CI section. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally in CI's own three forms AND on a machine neither of us controls** | mine above; CI run 39371705159, job `lint, unit and guards`, read at STEP level: actionlint, ruff, black --check, mypy and **unit tests** all SUCCESS, only `guards and meta-tests` FAILURE. Every step RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. The verification ladder job is SUCCESS on all six rungs. |
| **C42** (U+FFFD in historical verdict headers), **C44** | **mine, accepted, carried** | unchanged by this diff. |
| **C45** | **DOES NOT RECUR IN `CLAUDE.md` OR `docs/SUPERVISOR.md`. IT RECURS IN MY OWN AGENT DEFINITION, as R880** -- seventh occurrence of the family, and the second running where the divergence is in the file governing the reviewer rather than in the criterion. | measured in R880. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE last round by the control at `bd315a1` (149 passed, 0 failed) and I did not redo it** | ES0's light scope. The control's conclusion is unchanged: not one of this tree's reds is red where the boundary state is absent, and this round's 165 are the same two files. |
| `scripts/suite_count.py`'s own line, and CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer; it is limb two of the predicate by construction, and two of this round's 165 reds ARE it. |

## Findings

**ONE BLOCKS. No tolerance moved, no conftest moved, no `.claude` file moved, and the one
`docs/SUPERVISOR.md` change is a standalone `process:` commit citing FS1 that removes no
guard.** The three ablation figures the report publishes all reproduce exactly on my machine:
the modulo reverted gives `2 failed, 27 passed`, `_recorded_heading` bypassed gives
`3 failed, 26 passed`, and the bool half alone removed gives `1 failed, 28 passed`. The third
is the one that matters and it is right: the bool check is not redundant with the type check.

---

**R877. (BLOCKS -- FR1 LIMB TWO) R874's REPAIR IS GATED BEHIND `load_cases.headings` BEING
DECLARED, AND R874's OWN PUBLISHED DEFECT LIVES ON THE PATH WHERE IT IS NOT. A SIDECAR WHOSE
`heading_deg` IS `true` RUNS TO EXIT 0 AND PUBLISHES `heading True deg` INTO `report.md` AND
BOTH CSVs -- WHICH IS THE SENTENCE `_recorded_heading`'s OWN DOCSTRING GIVES AS ITS REASON FOR
EXISTING. AND THE REFUSAL MESSAGE RECOMMENDS THAT PATH BY NAME.**

```
claim  the repair runs only when a heading set is declared, and the default declares none
cmd    the early return
out    floatfea/run/pipeline.py:629-630
         if not declared:
             return
       -- `_recorded_heading` is called at :631, AFTER it. refuse_headings_this_run_cannot_cover
          is the function's only caller; grep for `_recorded_heading` over floatfea gives two
          lines, the definition and that one call.
cmd    whether the default path is a real path
out    examples/platform12_placeholder.yaml declares NO `headings:` key -- the shipped
       fixture, and what tests/regression/test_r1_example_golden.py runs
cell   ONE VARIABLE MOVED: the presence of `load_cases.headings`. Same deck, same npz, same
       sidecar with `run.heading_deg` set to `true`, outputs to a temporary directory,
       through the real CLI.
out    [a] no headings declared   -> EXIT=0
           report.md:23              * **heading** - True deg
           member_forces.csv         # wave basis: heading True deg
           utilisation.csv           same header block
       [b] headings: [1.0] declared -> EXIT=2
           floatfea: the dynamic-inputs file's recorded `heading_deg` is True (bool), which
             is not a single heading in degrees. ... Fix the sidecar beside the npz, OR
             REMOVE `load_cases.headings` SO NO COMPARISON IS CLAIMED.
       -- the refusal's own last clause routes the reader from [b] to [a].
cmd    the three sibling fields read by the same function, in the same dict, from the same
       file, and published to the same three artifacts
out    floatfea/run/pipeline.py:695-699 -- exported_wave_basis returns heading_deg,
       wave_height_full_m, wave_height_model_m and window. ONLY the first is validated, and
       only when a heading set is declared. With wave_height_full_m `true`,
       wave_height_model_m `[0.484, 1.0]` and window a mapping, EXIT=0 and report.md reads
         * **wave height** - True m full scale ([0.484, 1.0] m model)
         * **window** - {'from': 1, 'to': 2}
       and member_forces.csv reads
         # wave basis: heading 0.0 deg; H_full True m; H_model [0.484; 1.0] m; ...
       -- the comma-stripping for CSV safety has turned the list's comma into a semicolon in
          the published header.
rule   FR1's SECOND limb, and CLAUDE.md's own gloss on it: "it is what the R825/R834/R837
       family was: a declared name or path arriving as a different type, accepted, and used.
       NO NUMBER WAS WRONG IN ANY ARTIFACT AT THE TIME, and the input was used other than as
       declared, so that family blocks." `heading_deg` is declared as a number in degrees by
       docs/conventions.md:143-147 and bounded by HEADING; a bool is accepted and used as the
       run's published wave basis.
judge  **IT BLOCKS. THE SILENTLY WRONG RESULT IT PRODUCES, in FR1's required form: an input
       declared as a heading in degrees is accepted as a bool, a list, a string or a mapping
       and USED -- published as the wave basis of three deliverables at exit 0 -- other than
       as declared. No number in those artifacts is wrong at the time, which is exactly the
       condition under which CLAUDE.md says this family still blocks.**
```

**AND THE ROUND IS MINE, WHICH I SAY RATHER THAN SMUGGLE.** My predecessor's R874 ruled "it
does not block ... the published value is the recorded object, so the contradiction is on the
face of the artifact rather than hidden in it", and set the closing condition at
`floatfea/run/pipeline.py:583-586`. That ruling applied FR1's FIRST limb and never tested the
second, and the condition named a site twelve lines below an early return. **The implementer
satisfied the condition as written.** The condition was wrong about where the defect was, and
the finding was wrong about which limb it fell under.

**Closed when** the recorded wave basis is validated WHERE IT IS READ -- `exported_wave_basis`
at `floatfea/run/pipeline.py:687-699`, which is the single reader of the sidecar and already
filters it key by key -- so that validation does not depend on what the configuration happens
to declare, and so that all four published fields get it rather than one. Specifically:
`heading_deg` refused unless it is a real non-bool number (and see R879 for NaN and range);
`wave_height_full_m` and `wave_height_model_m` the same; `window` refused unless it is the
string the report prints it as. A run that reaches exit 0 must not be able to publish a
wave-basis line carrying a bool, a list or a mapping. `_recorded_heading` then becomes a read
rather than a validator, and R878 is in the same function.

---

**R876. (DOES NOT BLOCK -- ledgered, and it is the highest-value item on the list) R872 PUT AN
EQUIVALENCE RELATION INSIDE A GATE AND CALLED IT ARITHMETIC. NOTHING IN THE 29 TESTS HOLDS THE
MODULUS. `% 180.0` IS GREEN ON ALL 29, AND SO IS `% 90.0` -- A MODULUS UNDER WHICH A FOLLOWING
SEA COVERS A HEAD SEA.**

```
claim  the gate does not pin the number the repair's own argument rests on
rule   the assertions in tests/unit/test_headings_and_bem_coverage.py, 29 of them, including
       the three R872 rows and the 44.9 near-miss
cmd    the injection that WEAKENS the gate, solved as a grid rather than at one point (EH4):
       `% 360.0` replaced by `% M` at both sites in uncovered_headings, for M in
       {180, 90, 45, 1}, test file re-run, file restored from a saved copy each time
out    modulus 180.0 -> 29 passed            <- declared 180 deg covered by recorded 0 deg
       modulus  90.0 -> 29 passed
       modulus  45.0 -> 1 failed, 28 passed
       modulus   1.0 -> 3 failed, 26 passed
       baseline      -> 29 passed            (and `git status --porcelain` empty after)
cmd    why the declared counter does not reach it
out    the 44.9-against-45.0 row measures the FINENESS of the comparison WITHIN a turn. The
       360-against-0 row measures that ONE turn is identified. Together they admit every
       modulus from 90 to 360. **The counter is in the right quantity for slack and in the
       wrong quantity for the modulus, which is what R872 actually changed.**
rule   FR1's third non-blocking class, "a census, needle or grep that is too narrow where no
       wrong result follows" -- a test too narrow is the same class, and the code at this
       commit is CORRECT.
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES AT THIS COMMIT: none** --
       `360.0` is the right number and I verified the whole covered axis under it. I would
       have blocked under CZ0 (c), because the modulus is what the gate claims and on which
       quantity; FR1 narrows that and I am ruling under FR1, not around it. Recorded as the
       first item on the list because it is one row.
```

**Closed when** one row asserts that a head sea is not covered by a following sea --
`uncovered_headings((180.0,), (0.0,)) == (180.0,)` -- which reddens at every modulus below 360
and is the counter-case in the quantity the repair moved.

---

**R878. (DOES NOT BLOCK -- ledgered) `floatfea/cli.py:146-149` SUBSCRIPTS FOUR KEYS THAT
`exported_wave_basis` BUILDS ONE KEY AT A TIME. A SIDECAR RECORDING A HEADING AND NOT A WAVE
HEIGHT IS A `KeyError` AFTER THE SOLVE, AND IT LEAVES A ZERO-BYTE `member_forces.csv` IN THE
OUTPUTS DIRECTORY.**

```
claim  the CSV header path and the report path disagree about a partial sidecar
cmd    the three sites
out    floatfea/cli.py:146-149  basis["heading_deg"], basis["wave_height_full_m"], ...
       floatfea/cli.py:262-265  basis.get('heading_deg', '(not recorded)'), ...
       floatfea/run/pipeline.py:695-699  {key: run_block[key] for ... if key in run_block}
       -- `if basis:` is true for ANY non-empty subset, and only the report path tolerates one
cell   the shipped example with `wave_height_full_m` removed from the sidecar's `run` block
       and nothing else changed, through the real CLI
out    EXIT=1, traceback, KeyError: 'wave_height_full_m' at cli.py:147, raised from
       _write_member_forces -> _write_header -> _header_lines
       and the outputs directory contains:  member_forces.csv   0 bytes
cmd    the commit that made it reachable
out    the comment at floatfea/cli.py:136-141 records it -- R829/FQ3 replaced the CSV path's
       field-by-field `(not recorded)` fallbacks with a single branch, for the right reason,
       and the report path kept its four `.get` calls. The partial case was not swept.
rule   FR1's first non-blocking class -- the outcome is right, the message is a traceback
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- exit 1 and a
       traceback. What it leaves behind is a zero-length artifact in the outputs directory,
       which floatfea/cli.py:395-397 names in as many words as the thing this project is
       built to prevent, and the exit code is what separates the two. Same function as R877.
```

**Closed when** `exported_wave_basis` returns either the whole wave basis or nothing -- so
`if basis:` means what both call sites assume -- or the CSV path uses the same four `.get`
calls the report path does, and either way one test records a partial sidecar's outcome.

---

**R879. (DOES NOT BLOCK -- ledgered) TWO OF THE THREE THINGS R873's AND R874's CONDITIONS NAMED
ARE NOT DONE AND NOT DECLARED UNANSWERED: NaN IS NOT REFUSED BY NAME, AND THE RECORDED HEADING
IS NOT RANGE-CHECKED AT ALL.**

```
claim  "the same discipline the declared side uses" is three checks and the repair has one
cmd    the declared side, in order
out    floatfea/run/config.py:202  bool or non-number  -> refused by name
       floatfea/run/config.py:208  NaN                 -> refused by name, "NaN is not a value"
       floatfea/run/config.py:212  outside [low, high] -> refused by name
cmd    the recorded side
out    floatfea/run/pipeline.py:581-593 -- the first check only
cell   refuse_headings_this_run_cannot_cover((0.0,), {"heading_deg": float("nan")})
out    REFUSED, but by the COVERAGE message: "this run covers nan deg -- the one heading its
       dynamic-inputs file was exported at". Not by name.
cell   refuse_headings_this_run_cannot_cover((90.0,), {"heading_deg": 450.0})
out    ACCEPTED -- and 450 is outside HEADING's declared domain, which the declared side
       refuses at config.py:212. The modulo is what makes it reachable: before R872 an
       out-of-domain recorded value could only match by exact equality.
cmd    one more, for the record
out    {"heading_deg": 10**400} -- a JSON bignum, which json.loads parses as an int -- is
       isinstance(x, int), passes _recorded_heading, and raises OverflowError inside float().
       Exit 1 and a traceback, same class as R878.
rule   FR1's first non-blocking class for the NaN half (the outcome is a refusal); and
       CLAUDE.md -- "A closing condition that names sites is closed site by site. Half of an
       item is not the item."
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- every case here
       is refused or crashes. It is on the list because a condition named three checks, two
       are absent, and the commit records neither as left. The range half is the one I would
       do first: it is what makes the modulo act only on `360.0 -> 0.0` inside the declared
       domain, which is the whole of what R872 argued for.
```

**Closed when** `exported_wave_basis` -- with R877 -- refuses a NaN recorded heading by name
and refuses one outside `HEADING`'s declared domain by name, or the report revision states
which of the three named checks was left and why.

---

**R880. (DOES NOT BLOCK -- apparatus, FF0 class: fixed in the next commit, not ledgered)
`.claude/agents/gating-supervisor.md` TELLS ME TO READ "EH1, EJ2 AND FC1 -- THE TWO BOUNDARY
STATES, THEIR TWO CORRECTED LISTS" FROM `CLAUDE.md`. FS1 DELETED THE LISTS. THE CITATION
RESOLVES AND THE RULE IT NAMES IS GONE, WHICH IS FE1's OWN TEST FAILING IN THE MIRROR.**

```
cmd    the citation, in my own instructions
out    .claude/agents/gating-supervisor.md -- "**CZ1** ... **EG3**, **EH1**, **EJ2** and
       **FC1** -- the two boundary states, their two corrected lists, and the two CZ1-class
       guards that cannot pass in the commit they describe."
cmd    what CLAUDE.md now carries under those codes
out    CLAUDE.md:429  "**THE ENUMERATED LISTS ARE REPLACED BY THE PREDICATE (FS1).**"
       EH1, EJ2 and FC1 survive there only as the HISTORY of why the lists went --
       CLAUDE.md:458-479, "Why the lists went, stated as the count rather than as a
       preference". There are no lists to read.
cmd    the grep that shows the lists are gone from all three governing files
out    "LIST GAINS THREE NAMES"   -> (none in .claude, docs/SUPERVISOR.md, CLAUDE.md)
       "state (2)'s list gains"   -> (none)
       "The two lists, corrected" -> (none)
rule   FE1's own note, inverted: "if a citation does not resolve and the rule is not stated
       beside it, the rule is gone." Here the citation resolves to a clause whose rule has
       been superseded, and my instructions still describe the superseded rule. FE1 deleted
       the copies to stop them going stale; the citations around them can go stale too.
judge  **it does not block under FR1 -- no wrong result follows -- and it is the gating
       apparatus, which FF0 takes out of the ledger and into the next commit. THE SILENTLY
       WRONG RESULT IT PRODUCES: none.** I ruled under CLAUDE.md, as my instructions say to
       where the two disagree, and I say which: all 165 reds classified under the FS1
       PREDICATE per id, no list consulted. Seventh occurrence of the C45 family. The reason
       I record it rather than let it pass is the one C45 was earned on: a reviewer reading
       an instruction that names a rule nobody can find has no way to know whether the rule
       was deleted or whether it is looking in the wrong place.
```

**Closed when** that sentence in `.claude/agents/gating-supervisor.md` names the FS1 predicate
instead of two lists, in a standalone `process:` commit citing FS1 -- and, as with R875, after
the paragraph around it is read rather than grepped.

## CI at the reviewed commit: RED, 165 reds, EVERY ONE BOUNDARY BY THE PREDICATE

**`gh run list --commit ff48a6d` returns `[]` and the run EXISTS. I did not take the empty
result for an unavailable check (CK2).** `gh run list -L 8` gives
`headSha ff48a6d4b60919485e1bf76fa9a81972f22d31b9, workflowName CI, status completed,
conclusion failure`, run id **39371705159**. This is not an allowance-exhausted run: it has a
runner, real steps and a real duration.

```
job  lint, unit and guards        FAILURE
     actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
     unit tests SUCCESS / guards and meta-tests FAILURE
     -- every step RAN. Nothing was skipped behind an earlier red, which is what CZ1 (iii)
        exists to see, and FP1's CI-only `types-PyYAML` red has stayed fixed.
job  the verification ladder      SUCCESS   (rungs 1, 2, 3, 4, 5 and 6 all SUCCESS)
job  CI determinism -- leg        skipped
job  CI determinism -- ten legs   skipped
```

My own whole-suite run agrees with CI's shape: **165 failed, 3617 passed, 1 skipped**, and the
165 are ENTIRELY inside the two report-guard files -- I ran those two alone and got
`165 failed, 183 passed, 1 skipped`, the same number. **Nothing outside them is red, which is
also the control that says my mutation runs did not leak into the whole-suite run: `% 1.0` and
the three ablations each redden `tests/unit/test_headings_and_bem_coverage.py`, and that file
is green in the whole-suite output.**

The 165, each id tested against the FS1 predicate rather than against any list:

```
119  test_every_named_site_is_touched_or_declared[...]   limb one -- each id NAMES a site of
       a verdict with no answering report revision, R874's three pipeline.py lines among them
 31  test_the_report_carries_the_finding[R845..R875]     limb one -- each NAMES a finding
 10  test_the_guard_survives_the_state[...]              limb one via the red `baseline`,
       which is itself in the list; the cascade is identified by the baseline being red and
       by each state's own failure line, not by its name
  1  test_the_CI_section_is_about_the_REVIEWED_commit     limb one -- names the reviewed commit
  1  test_the_Carried_table_is_what_the_generator_produces        limb one
  1  test_the_generator_would_catch_a_row_under_the_wrong_number  limb one, the generator's
       own control, keyed on the Carried table it cannot have yet
  1  test_the_report_carries_a_WHOLE_SUITE_count         LIMB TWO -- scripts/suite_count.py
       measures a clean worktree AT a commit, so the line naming a sha cannot be inside it
  1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW      LIMB TWO -- needs a RUN, and no run
       exists for a commit before it is pushed
---
165  163 under limb one, 2 under limb two. NONE WITHOUT AN EXIT. No red is CZ1 (iv).
```

## Corpus (EG4(e))

**THE PAUSE HELD. I added no corpus entries and committed nothing to `tests/corpus/`.** Batches
are paused until 28 October except mutation work on F4's load-mapping gate and EB6's
label-provenance gate, and this diff touches neither.

**What I ran instead, which is the recorded substitute, and both halves produced a finding:**

* **A continuum grid over the parameter space the decision rule guards** -- the RECORDED
  heading axis, which `HEADING` does not bound and which the commit's own report says it did
  not test: `-10.0`, `-360.0`, `-1e-16`, `405.0`, `450.0`, `450.0000000001`, `720.0`, `1e40`,
  `10**400`, `nan`, `inf`, `True`, `"0"`, `[0.0, 45.0]`, `{"a": 1}`, `None`; and a grid over
  the MODULUS itself, `{360, 180, 90, 45, 1}`. The modulus grid produced **R876** and the
  out-of-domain rows produced **R879**.
* **A regeneration check on a published deliverable** -- `report.md`, `member_forces.csv` and
  `utilisation.csv` regenerated from this tree against three perturbed sidecars rather than
  read in the diff. That produced **R877**, the blocking finding, and **R878**.

Neither would have been found by reading the diff: the diff's configuration is the one the
commit chose, and R877 lives on the configuration it did not -- a config with no `headings:`
key, which is the shipped example.

## Tolerances touched

**None.** `git diff 0a6edba..HEAD -- floatfea/tolerances.py` is empty.

**And I considered `% 360.0` against the tolerance rule rather than accepting the commit's
word for it.** `CLAUDE.md` extends the rule to "anything that functions as a tolerance under
another name: convergence thresholds, comparison epsilons, 'small number' guards ... and any
factor introduced to make two numbers agree". The modulus is **not** one: it introduces no
slack, and I measured that rather than reasoning it -- `h % 360.0` is exactly `h` for every
value in `[0, 360)` and exactly `0.0` at `360.0`, so the near-miss `44.9` against `45.0` is
still refused and the comparison is as fine as it was. It is a change to the EQUIVALENCE the
comparison uses, not to its tolerance, and the quantity it is an equivalence on is a direction
of travel, where mod-360 is an identity. **The commit's claim that this is arithmetic is
correct and now measured.** What is missing is not a tolerance entry but a counter in the right
quantity, which is R876.

## Next step opens when

**This is a HOLD, so step 3 stays open and the next step does not begin. The three reviewed
revisions are all still available -- this is the sixth interim check and counts against none.**

**R877 is answered first, and it is answered in `exported_wave_basis` rather than at the site
my predecessor named.** The specific condition: the recorded wave basis is validated where the
sidecar is read, so that validation does not depend on what the configuration declares, and
all four published fields get it. A run that reaches exit 0 cannot publish a wave-basis line
carrying a bool, a list or a mapping in any of the three artifacts, and the measurement that
shows it is the shipped example -- no `headings:` key -- run against a sidecar whose
`heading_deg` is `true`, with the exit code and the three regenerated artifacts pasted. The
refusal message's last clause, which currently reads "or remove `load_cases.headings` so no
comparison is claimed", stops recommending the unvalidated path.

**R878 and R879's range half are the same function and go in the same commit.** R876 is one
test row. R880 is a `process:` commit and not the implementer's step work.

**Still blocking by name into the first reviewed revision, unchanged:** R867, R868, R869 as
one repair, and R870. **R862 remains not due** and blocks in the commit that adds a timed
stage -- FL2 item 4 or 5, by the implementer's own sequencing.

**What I did NOT ask for.** No new guard, scanner, meta-test or detector: R876 is a row in an
existing file, R877/R878/R879 are checks inside an existing function, and R880 is a sentence.
`docs/milestones/F2a.md` is where anything larger goes.

**Schedule, since the turn stated it.** FS4's checkpoint is 26 October, seven days out, and
FL2 items 3, 4 and 5 plus FM0's re-solve loop are what remains. Step 3 has now spent six
interim checks and no reviewed revision. **I am not re-escalating**: FR0 already answered the
escalation `CLAUDE.md` requires with "slip the date, keep the scope", and R877 is one function
in one commit. What I record is that this round's blocking finding came from running the model
at a configuration nobody chose, which is the trade EU1 and FR1 were both written to make.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 82f922c4227656e597ea35be7b7aa5137f3cc4f4
**Reviewed commit: `82f922c4227656e597ea35be7b7aa5137f3cc4f4`.**
Verdict: PASS
Tests: 3607 passed, 145 failed, 1 skipped, 2 warnings in 1129.39 s (0:18:49)   (my own run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the fifth in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **NOTHING
BLOCKS.** R866 -- my predecessor's single blocking finding -- is answered, and I verified it
by ABLATION in six directions rather than by reading the diff, including the one direction
the commit did not run. Three new ledger items and one apparatus item below, plus the
criterion ruling the turn asked for by name.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For each finding I state the silently wrong result it produces, or
that it produces none. **No finding in this check can be given FR1's sentence**, which is
why the verdict is PASS and not a HOLD with a caveat.

```
cmd    git diff --name-status d06c577..HEAD
out    M CLAUDE.md / M docs/SUPERVISOR.md / M floatfea/run/pipeline.py /
       M tests/unit/test_headings_and_bem_coverage.py /
       M tests/unit/test_run_pipeline_refusals.py
       -- 5 files, 227 insertions, 3 deletions. TWO commits, and the split is correct:
          e945b13 touches floatfea/ and tests/ and NOTHING else; 82f922c touches
          CLAUDE.md and docs/SUPERVISOR.md and NOTHING else.
cmd    git diff d06c577..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff d06c577..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                      -- a file, as my instructions say it must be
cmd    git ls-files | grep -i conftest        -- the whole-tree census (CH2/CI0)
out    tests/conftest.py
       tests/test_supervisor_conftest_pathspec.py  -- one conftest, depth one, unchanged
cmd    git diff --stat d06c577..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 21 ++++++++--   (19 insertions, 2 deletions); .claude EMPTY
       -- NOT a STOP. It is in 82f922c, a STANDALONE process: commit citing FS1 whose only
          other file is CLAUDE.md. I read every line of it: the two enumerations in the EG3
          quote go (which is what FS1 ordered), and one clause is ADDED. **No guard was
          removed, and the addition RESTORES one.** The residue it did not catch is R875.
cmd    git diff --stat d06c577..HEAD -- results scripts/measure docs/reports
out    (empty)   -- no published deliverable moved, and no step report was touched (EK3)
cmd    git status --porcelain
out    (empty)   -- clean before I ran anything and after
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ;
         mypy floatfea scripts/f4_dynamic_residual.py      (CI's own three forms)
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 43 source files
cmd    python -m pytest -q tests/unit        -- the commit's own headline figure, re-taken
out    228 passed in 159.77s
       -- `e945b13` claims `228 passed in 147.40s`. **The count reproduces exactly.** I
          re-took it because the previous four rounds each carried one wrong figure
          (R853, R857, R844, and the 290/267 correction), and this one is right.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`) and five
verdicts are now newer than it. That is EG3 state (2), and it is the whole of this tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R866** (`load_cases.headings` parsed, validated and read by nothing; three deliverables published for a configuration declaring three headings) | **ANSWERED, AND I ATTACKED THE REPAIR RATHER THAN READING IT -- SIX ABLATIONS, ALL CAUGHT, INCLUDING THE ONE THE COMMIT DID NOT RUN.** | `floatfea/run/pipeline.py:543-600` is the refusal; `:711-717` is the call site, above `t0` and before `build_model`. The ablation table is in "Try to break it" below. The row that matters most is **M2, which the commit did not run**: the refusal MOVED to after the three writes -- R809's original defect shape, exit code still 2 -- is caught by the call-site case through its empty-directory assertion. **The placement is BETTER than my predecessor's condition asked for.** That condition named the form at `floatfea/cli.py:354`; the repair sits in `run()`, which `tests/regression/test_r1_example_golden.py:63` and `:425` also call directly, so it covers callers `_cmd_run` does not. A grep for the three writers in `floatfea` reaches only `_cmd_run`, which calls `run_pipeline` before its first write, so the refusal gates every path to a published artifact. The first reviewed revision states the placement choice in prose; the commit message already does. |
| **The SPECIES, not just the instance** | **I CENSUSED THE WHOLE SCHEMA AND IT IS NOW CLEAN** -- the half of R866 the instance repair does not cover, and nobody asked for it | Every key `_reject_unknown` admits, traced to a consumer: `deck`, `froude_lambda`, `groups`, `material`, `governing_periods`, `f`, `K`, `Cm`, `K_sensitivity`, `Cm_sensitivity`, `directory`, the three output flags, `study_only` and `topology.platform.members` are CONSUMED; `tag` and `window_rule` are PUBLISHED by `config.provenance()` (R812's own repair); `one_third_increase`, `required_section`, `truss_sizing`, `line_masses`/`lumped` and a per-body fraction split are REFUSED by name; and `cases` is mutually exclusive with `npz` at `floatfea/run/config.py:909` while `run()` refuses a config with no `npz`, so a declared wave case can never sit unread beside a dataset. **`headings` was the last field that was none of the three. There is no second instance.** |
| **R867, R868, R869** (of eight non-default topologies one runs; the test builds the order that cannot run; a declared topology need not reach the centre) | **still open, correctly, and correctly NOT in this commit** | the diff over `floatfea/model`, `floatfea/solve` and `tests/unit/test_topology_from_config.py` since d06c577 is empty. My predecessor placed them as one repair in the first reviewed revision and the turn carried them there. I did not re-open them. |
| **R870** (FL2(a) as shipped is a subset of the locked plan's (a); two future-tense sentences) | **still open, untouched** | `floatfea/run/pipeline.py:123` and `:180` are unchanged; the only pipeline hunks in this diff are the new function and the new call. |
| **R871** (FS1's commit left a hand list in `docs/SUPERVISOR.md` and deleted FC1's reason from both files) | **ANSWERED ON BOTH HALVES, and the second half's repair is EXERCISED BY THE VERY RUN THAT JUDGES IT. A SIBLING RESIDUE SURVIVES TWO PARAGRAPHS ABOVE THE ONE THAT WAS FIXED -- R875.** | Half one: a grep for "The only failures are" over both files gives 0 and 0, and the same for `test_every_named_site_is_touched_or_declared`. Half two: the second limb is back at `CLAUDE.md:434-449` and `docs/SUPERVISOR.md:566-581`, and **its first application is in my CI section below** -- the two ids that had NO EXIT at 102 of 104 last round are red again here with failure lines naming no finding and no site, and the restored limb is what admits them. **That is the measurement that settles the turn's criterion question.** |
| **R862** (three hand copies of the stage set; the published total is the sum of a hand-copied four) | **still open, correctly, and STILL NOT DUE -- I measured the trigger rather than taking the word for it** | the five `timings[...]` assignments in `floatfea/run/pipeline.py` are unchanged (721, 769, 780, 785, with 788-789 summing four of them), `WALL_TIME_STAGES` at `floatfea/cli.py:37-43` is unchanged, and the diff over `floatfea/cli.py` is EMPTY. The new refusal sits ABOVE `t0` and times nothing. **No timed stage was added, so the understatement is not reachable at this commit.** It blocks in the commit that adds one -- FS0's item 4 or 5. |
| **R863** (the exclusion set is defined by the code under test), **R865** (the docstring at `tests/regression/test_r1_example_regenerates.py:224`) | **both still open, untouched** | the diff over `tests/regression` since d06c577 is empty. |
| **R864** (the byte-identity claim's witness is blind to its own subject) | **still open; its condition is a sentence in the report and no report revision exists** | unchanged by this diff. |
| **R847 / C43** ("0 of 49 rows" does not reproduce), **R848** (the empty-directory refusal admits a bare dot), **R849 with R854** (four gates quantify over hard-coded three-file tuples) | **all still open, all untouched, all correctly so** | the diff over `floatfea/cli.py` is empty, which covers R848; the regression diff is empty, which covers R849 and R854; R847 needs a revision that does not exist. FR1's second and third non-blocking classes. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **ROUTED, not open -- FS3 ledgers it to FL3** | `docs/directives/FS.md:28`. Not open against step 3. |
| **R855** (the whole suite at a commit carrying no report revision) | **WITHDRAWN, and the standing condition IS MET at this commit** | the turn states plainly which runs it made (228 passed on `tests/unit`, 34 passed on the prose guard) and that it made NO whole-suite run at this sha, relying on the ruling rather than claiming a green it had not taken. **No green is stated that was not measured. I produced the whole-suite number, as I do by rule: 145 failed, 3607 passed, 1 skipped.** |
| **R856** (write_verdict.py refused a step with no report) | **ANSWERED, and exercised for the second time -- this file went through `--interim`** | `scripts/write_verdict.py:166-180` and `:233-236`, unchanged by this diff. |
| **R835, R836** (EG3's enumerated lists, wrong in both directions over ten measurements) | **ANSWERED by FS1 as completed by 82f922c, and I applied the predicate PER ID to all 145 reds: 143 under limb one, 2 under limb two. NONE WITHOUT AN EXIT, which is the first round in step 3 where that is true.** | `CLAUDE.md:429-449`, `docs/SUPERVISOR.md:560-581`. Measured in the CI section. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally in CI's own three forms AND on a machine neither of us controls** | mine above; CI run 39367249326, job `lint, unit and guards`, read at STEP level: actionlint, ruff, black --check, mypy and unit tests all SUCCESS, only `guards and meta-tests` FAILURE. Every step RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see, and mypy is green there, so FP1's CI-only `types-PyYAML` red has stayed fixed. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | unchanged by this diff. A replacement character surfaced again inside one guard's own failure message this round; same byte question, same disposition. |
| **C44, C45** | **C44 carries. C45 DOES NOT RECUR IN `CLAUDE.md` -- the clause was added to both files identically. IT RECURS IN `docs/SUPERVISOR.md` ALONE, as R875**, where a paragraph survives that `CLAUDE.md` does not have. | measured in R875. Sixth occurrence of the family, and the first where the divergence runs the wrong way: the file that governs what I read carries more stale text than the criterion does. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE, by the control rather than by family** | at `bd315a1` -- a commit where a verdict exists WITH its answering report -- the two report-guard files are **149 passed, 0 failed**, re-measured by me in a worktree at that sha. Not one of this tree's 145 reds is red where the boundary state is absent. |
| scripts/suite_count.py's own line, and CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer; it is limb two of the predicate by construction. |

## Findings

**NONE BLOCKS.** No tolerance moved, no conftest moved, no published deliverable moved -- and
I established the last of those by REGENERATING the deliverables from this tree rather than by
reading the diff: the default path and a config declaring `headings: [0.0]` both reproduce
`**U = 1.71167** at platform:hub4_arm ROOT` identically with `results/R1/example/report.md:63`.
**The repair is inert on the default path, measured by running the model.**

**R872. (DOES NOT BLOCK -- ledgered) `headings: [360.0]` IS INSIDE THE DECLARED DOMAIN AND IS
REFUSED AGAINST AN EXPORT AT 0 DEG, WHICH IS THE SAME WAVE DIRECTION. The exact comparison was
the right call while `covered` was the CALLER's fact; this commit made the function build
`covered` ITSELF, and the modular-360 identity became its question at that moment.**

```
claim  a configuration that declares exactly the heading the run covers can be refused
cmd    HEADING's declared domain
out    floatfea/run/config.py:189 -- HEADING = ("deg", 0.0, 360.0), INCLUSIVE, so 360.0 is
       a declarable heading and `_parse_headings` admits it
cell   the shipped example with headings: [360.0] and nothing else changed, through the real
       CLI, outputs redirected to a temporary directory
out    $ python -m floatfea.cli run <that config>
       EXIT=2
       floatfea: load_cases.headings declares [360.0] deg and this run covers 0.0 deg --
         the one heading its dynamic-inputs file was exported at. [360.0] deg would never
         be computed ...
       the output directory was never created
cmd    the direction it fails in, solved BOTH ways before I claimed either (EH4)
out    exact equality is strictly FINER than equality mod 360, so there is no pair that
       passes under exact and fails under modular. 360 declared / 0 recorded -> refused;
       0 declared / 360 recorded -> refused. **It over-refuses and it cannot under-refuse.**
       I checked the weakening direction first and there is nothing in it.
rule   FR1 -- "a refusal whose message is unclear but whose outcome is right" does not block.
       Here the MESSAGE is right and the OUTCOME is wrong, which is the mirror of that class
       and is still not a silently wrong result; and BP0, because the figure that cleared
       this axis last round was measured against a rule this commit moved.
judge  **it does not block, and the reason is the direction**: nothing is published, no number
       is wrong, and the failure mode is a refused run rather than an accepted one. **THE
       SILENTLY WRONG RESULT IT PRODUCES: none.** What it costs is a false refusal on a legal
       declaration. Recorded now rather than at the close because the previous round swept
       "360 against 0" on `uncovered_headings` and concluded the function was sound --
       correctly, because the covered set was then a parameter. The call site is what made
       that conclusion stale.
```

**Closed when** either the comparison is taken mod 360 at the one place that builds `covered`
from a recorded value (`floatfea/run/pipeline.py:586`), or `HEADING`'s upper bound becomes
exclusive so 360 is refused at parse with a message naming 0 -- and the choice is recorded,
because the two are different claims about what a declared heading IS.

**R873. (DOES NOT BLOCK AT THIS COMMIT -- ledgered, WITH ITS TRIGGER NAMED) A SIDECAR WHOSE
`heading_deg` IS A LIST MAKES THE COMPARISON RAISE `TypeError` INSTEAD OF COMPARING. The one
check that exists to catch a heading mismatch crashes at exactly the shape FL(c)'s mechanism
would introduce.**

```
claim  float() on the recorded value is unguarded, so a non-scalar recording is a traceback
cmd    the coercion
out    floatfea/run/pipeline.py:586 -- covered = (float(recorded),), with no type check
cell   refuse_headings_this_run_cannot_cover((0.0,), {"heading_deg": [0.0, 45.0]})
out    TypeError: float() argument must be a string or a real number, not 'list'
       -- uncaught; `cli.main` catches only ConfigError, so this is exit 1 and a traceback
cmd    whether the shape is reachable today
out    the committed sidecar records heading_deg 0.0 (a float), and the npz carries NO
       heading key at all -- I listed its hundred keys and `heading` is not among them, so
       there is no second source that could disagree with the sidecar
cmd    the trigger, named rather than left as a hypothetical
out    my predecessor's own scope statement, which Xabier now holds: "a list of npz files,
       each with its own recorded heading, envelope over the union". A multi-heading export
       is the commit where `heading_deg` plausibly stops being a scalar, and it is FL(c)'s
       mechanism half -- the half that "waits on nothing".
rule   FR1's first head; and my own guard that a gate carries its own failure -- a gate that
       raises before it compares has not failed, it has abstained
judge  **it does not block at this commit and it is one export format away from doing so.
       THE SILENTLY WRONG RESULT IT PRODUCES TODAY: none** -- exit 1, a traceback, nothing
       written. At the commit that records a heading list, the refusal that is supposed to
       compare declared against covered raises instead, and whether that is loud depends on
       where the exception is caught. Same shape as R869 and recorded the same way.
```

**Closed when** the recorded heading is validated before it is coerced -- a non-scalar, a bool
and a NaN each refused by name -- or the multi-heading case is handled, at
`floatfea/run/pipeline.py:583-586`.

**R874. (DOES NOT BLOCK -- ledgered) THE DECLARED SIDE REFUSES A BOOL BY NAME AND THE RECORDED
SIDE COERCES ONE. `heading_deg: true` IN A SIDECAR IS ACCEPTED AS 1.0, AND A CONFIGURATION
DECLARING `[1.0]` AGAINST IT RUNS AND PUBLISHES.**

```
claim  the two sides of the one comparison have different type discipline
cmd    the declared side
out    floatfea/run/config.py:199 `_checked` refuses a bool for every declared NUMBER, and
       :255 `_require_string` refuses one for every declared STRING, with R825's recorded
       reason -- "YAML reads bare words like `no`, `yes`, `true` ... as booleans"
cmd    the recorded side
out    floatfea/run/pipeline.py:586 -- float(recorded), and float(True) is 1.0
cell   refuse_headings_this_run_cannot_cover((1.0,), {"heading_deg": True})
out    ACCEPTED -- no refusal; the run proceeds and publishes
cmd    what the artifact would then say
out    floatfea/cli.py:146 prints basis["heading_deg"] verbatim, so the header line reads
       `wave basis: heading True deg` -- the published statement is absurd, not plausible
rule   FR1's second head, tested and NOT met: the input is accepted and used as 1.0, and the
       artifact states `True` rather than `1.0`, so nothing downstream reads a wrong number;
       and the schema's own refuse-not-coerce discipline, which this site departs from
judge  **it does not block. THE SILENTLY WRONG RESULT IT PRODUCES: none** -- the published
       value is the recorded object, so the contradiction is on the face of the artifact
       rather than hidden in it. Recorded because the asymmetry is the finding: this
       repository refuses a bool by name in eleven places and coerces one here, and the
       sidecar is JSON rather than YAML only by luck of the format. One line, with R873.
```

**Closed when** `floatfea/run/pipeline.py:583-586` validates the recorded heading with the same
discipline the declared side uses, in one place with R873.

**R875. (DOES NOT BLOCK -- apparatus, FF0 class: fixed in the next commit, not ledgered)
82f922c FIXED THE LIST R871 NAMED AND LEFT ITS SIBLING TWO PARAGRAPHS ABOVE. `docs/SUPERVISOR.md`
NOW CARRIES A PARAGRAPH THAT INTRODUCES A QUOTE THAT IS NOT THERE AND TELLS ME TO READ AGAINST
LISTS THAT NO LONGER EXIST -- AND `CLAUDE.md` DOES NOT HAVE IT.**

```
cmd    the surviving paragraph
out    docs/SUPERVISOR.md:555-557
         "**The two lists, corrected (EH1).** The clause above was written from one
          observation and was short by two names on each side. The reviewer's wording,
          adopted unparaphrased:"
       ... and the next line is the FS1 heading. The colon introduces NOTHING: the quote it
       introduced WAS the list, and e227200 removed the list and left the introduction.
cmd    the same two phrases in both files
out    "The two lists, corrected" -> docs/SUPERVISOR.md:555 only; CLAUDE.md: nothing
       "short by two names"       -> docs/SUPERVISOR.md:556 only; CLAUDE.md: nothing
       -- the two files DIVERGE, and in the direction that matters: the file that governs
          what I read carries stale text the criterion does not.
cmd    the second residue, same commit
out    docs/SUPERVISOR.md:549 -- 'and "only those" is a claim that carries the `FAILED` list
       as its command'. "only those" referred to the enumerations. It has no referent now.
cmd    which commit introduced each
out    git log -L on those lines -> e227200 (FS1's own commit), not 82f922c. **82f922c is the
       commit whose whole purpose was to finish cleaning that file, and its needle was "The
       only failures are" -- which cannot see a paragraph introduced by "The reviewer's
       wording, adopted unparaphrased:".** That is R871's own defect, repeated inside R871's
       repair, and it is the shape R842, C27 and R871 already are.
rule   C45 -- a mirror of a living document is a figure whose rule moves underneath it; and
       the census shape, a needle whose domain cannot contain the thing it is looking for
judge  **it does not block under FR1: no wrong result follows, and it is the gating apparatus,
       which FF0 takes out of the ledger and into the next commit. THE SILENTLY WRONG RESULT
       IT PRODUCES: none.** I am recording the fix condition as a READING and not as a needle,
       because three needles in a row have been short: the EG3 section in `docs/SUPERVISOR.md`
       is forty-five lines, and the only check that has worked on it is someone reading all
       forty-five.
```

**Closed when** `docs/SUPERVISOR.md:549` and `:555-557` say what is true -- in one standalone
`process:` commit citing FS1 -- after the whole EG3 section has been read top to bottom rather
than grepped.

## The ruling the turn asked for: is restoring CZ1's reusable half a REPAIR or an AMENDMENT?

**IT IS A REPAIR, IT STANDS, AND YOU DID NOT TAKE A RULING THAT WAS NOT YOURS.** You asked me
to check this and you were right to. The reasoning and the measurement:

```
claim  FS1 did not ask for FC1's reason to go, so restoring it is not an amendment to FS1
cmd    FS1's verbatim text
out    docs/directives/FS.md:17-20 -- "EG3's enumerated LISTS are REPLACED by the predicate
       ... No more hand lists."
       -- the object of that sentence is LISTS. FC1's clause was a list of two names AND a
          reason. Deleting the reason was collateral, not instruction.
cmd    where the restored sentence comes from
out    it is a composition of two ALREADY-ADOPTED clauses: FC1's "neither can pass in the
       commit it describes", and CZ1's reusable half, "a check whose input is the commit
       itself cannot be measured before the commit exists". Neither is new, and 82f922c
       names FC1 in the text. **A repair is checkable against an adopted directive; this
       one is.**
cmd    the measurement that settles it, taken on this tree rather than argued
out    at this commit `test_the_report_carries_a_WHOLE_SUITE_count` fails with "the newest
       revision carries no whole-suite line", and `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW`
       with "run 39162423263: the table says in_progress, gh says failure". **Neither names
       a finding. Neither names a site.** Under the one-limb predicate they block, CZ1 (iv),
       and the tree cannot reach a green by any act of the implementer's. Under the restored
       limb they are boundary reds. **The limb's FIRST application is the run that judges
       the commit that restored it, and it is load-bearing in that run.**
rule   CLAUDE.md section "The reviewer's own instructions are not edited inside a step" --
       a standalone process: commit citing the directive asking for the change. 82f922c is
       standalone (CLAUDE.md and docs/SUPERVISOR.md, nothing else) and cites FS1 and FC1.
judge  **A repair. Not a STOP, not a HOLD, and not an amendment you had no standing to make.**
```

**ONE THING FOR XABIER, SAID ONCE, AND IT IS NOT A HOLD.** The restored limb is BROADER than
FC1 was. FC1 added two names; the limb adds a reason, and CZ1's own statement of that reason
names a wide class -- "anything reading `git log`, `git diff` or `git merge-base`", which is
most of both report-guard files. Read literally, limb two could waive a red that limb one
correctly blocks. Measured against this tree it does not: of 145 reds, 143 satisfy limb one and
only 2 reach limb two, and both are self-referential in the exact sense CZ1 means -- a line
that names its own sha cannot be inside that sha, and a run does not exist for a commit before
it is pushed. **So the limb is doing the narrow job, and the broadening was my predecessor's
own proposal, which I am not reversing.** The sentence I would add is one line and it is
Xabier's to authorise rather than a round's to spend: *limb two is about a check whose SUBJECT
is the commit carrying it, not about a check that reads the commit graph.* Without that
distinction the next reviewer has a waiver wide enough to cover every guard in those two files,
which is the opposite of the problem FS1 solved.

## Try to break it -- what I ran, and what it found

**THE ABLATION TABLE, which is what the turn asked me to attack.** Six mutations, one variable
moved each, in a detached worktree outside the repository so the judged tree was never touched.
The three ids are the two new end-to-end cases plus the whole of
`tests/unit/test_headings_and_bem_coverage.py`.

```
rule   each row is "the claimed property broken; does the assertion go red"
out    BASELINE                                        23 passed
       M1  the call site removed from run()             1 failed   <- the hole R866 WAS
       M2  the refusal MOVED to AFTER the three writes  1 failed   <- NOT RUN BY THE COMMIT
       M3  subset -> any-overlap (weakening, EH4)       2 failed
       M4  the refusal degraded to a warning            3 failed
       M5  a missing recorded heading assumed zero      1 failed
       M6  the refusal made unconditional               2 failed   <- the CONTROL earns its
                                                                       place
       RESTORED                                        23 passed
cell   M1 and M2 both leave the FUNCTION's five cases GREEN and are caught only by
       test_R866_a_declared_heading_the_RUN_CANNOT_COVER_refuses_AT_THE_CALL_SITE
judge  **M2 is the row that matters and the commit did not run it.** It keeps the refusal, the
       message and exit code 2, and moves it past `_write_member_forces` -- which is R809's
       recorded defect verbatim, "a refusal that arrives after the outputs is a warning with a
       non-zero exit code". It is caught, and it is caught by the ONE assertion in the pair
       that a weaker test would have left out: `assert not out.exists() or not
       list(out.iterdir())`. The claim "nothing is written" is held by a measurement of the
       directory and not by the exit code. **M6 says the control is not decorative**: making
       the refusal unconditional reddens the accepting case in 0.68 s, so "the refusal fires"
       and "the right runs still run" are two assertions and not one.
```

* **A continuum grid over the one parameter space the new rule guards: eleven points on the
  RECORDED side, which is the side the diff created.** `heading_deg` as `0.0`; `-0.0` declared
  against it; `360.0` declared against it; a partial overlap `(0.0, 45.0)`; the string `"0.0"`;
  the int `0`; the bool `True`; `None`; `nan`; a two-element list; and an empty basis with
  nothing declared. **Three of the eleven produced findings** -- R872 (360), R873 (list), R874
  (bool) -- all on the axis the commit did not sweep, because its own four-row table is about
  the DECLARED side.
* **A regeneration check on a published deliverable, in both directions.** Three full
  `floatfea run` executions into a temporary directory: the default path reproduces the
  committed governing `U = 1.71167 at platform:hub4_arm ROOT` on `report.md:63` exactly, with
  1248 member-force rows and 32 stations; `headings: [0.0]` reproduces the same line, so the
  repair is inert where it must be inert; `headings: [360.0]` exits 2 with nothing on disk,
  which is R872.
* **The whole config schema censused for a second instance of R866's species**, key by key
  against a consumer, a publisher or a refusal. There is none. It is in the Carried table
  because it is the half of the finding the instance repair does not cover.
* **The structural question rather than the pass/fail one (provenance, not existence).** A grep
  for the three writers in `floatfea` reaches `_cmd_run` only, and `_cmd_run` calls
  `run_pipeline` before its first write, so the refusal in `run()` gates every path to a
  published artifact -- asserted from the call graph, not inferred from a green.
* **The predicate applied to 145 ids one at a time, with the ten cascade ids read off their OWN
  inner FAILED lists** rather than ruled by family, plus the `bd315a1` control.
* **My own 145 against CI's 145, both directions.** `comm -3` over the two sorted lists is
  empty: the SAME SET, id for id, on two operating systems. My first capture looked six short
  and that was my own `tail -140` truncating pytest's output, not a difference -- I re-ran the
  two files alone to get the complete list rather than report a discrepancy I had manufactured.

**What I did not find, and it is much the larger part.** The repair is the right size and in
the right place: it uses only the local fact, it declines the envelope rather than inventing
it, it refuses a sidecar-less npz instead of assuming the commonest declared value, and it sits
above `t0` so no stage is timed and R862 stays not-due. **It is held at the place that matters,
which is the thing R866 was about** -- and the turn found that hole itself, by ablating its own
first version, which is discipline rather than luck. The CLI contract was measured rather than
assumed: `pytest.raises(ConfigError)` passed its control and failed its subject, and
`cli.py:447` is why. The process commit is standalone, cites its directive, removes no guard
and restores one that is load-bearing in this very run. And the species census came out clean,
which is a better outcome than the instance repair promised.

## CI at the reviewed commit: RED, 145 reds, ALL 145 BOUNDARY BY THE PREDICATE AND BY THE CONTROL

```
cmd    gh run list --commit 82f922c4227656e597ea35be7b7aa5137f3cc4f4
         --json conclusion,status,databaseId,workflowName
out    one run: databaseId 39367249326, workflowName CI, status completed,
       conclusion failure
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The judged commit had a run because it was pushed
          first (FP1).
cmd    gh run view 39367249326 --json jobs, read at STEP level
out    the verification ladder : SUCCESS   (04:00:24Z -> 04:04:53Z)
         ladder 1, 2, 3, 6, 4 and 5 -- all six rungs SUCCESS. No rung is red, so nothing
         above is uninterpretable and THERE IS NO STOP.
       lint, unit and guards : FAILURE     (04:00:24Z -> 04:18:08Z)
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
         -- every step RAN rather than being skipped behind an earlier red (CZ1 (iii))
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39367249326 --log-failed, unique ids
out    103  test_every_named_site_is_touched_or_declared[R8xx-<site>]
        27  test_the_report_carries_the_finding[R845..R871]
        10  test_the_guard_survives_the_state[baseline + 9]
         5  the five singletons named below
       --- 103 + 27 + 10 + 5 = 145 exactly, with no remainder, and all 145 inside
           tests/test_report_carried.py and tests/test_report_guard_states.py
cmd    the two files alone, my own run, for the complete list
out    145 failed, 181 passed, 1 skipped in 181.89s
       -- so the whole suite's 145 reds are exactly these two files' 145, and the other 3426
          tests in the tree are green
cmd    my 145 against CI's 145, both directions
out    comm -3 (mine) (CI's)   (empty)   -- the SAME SET, two machines, two OSes
cmd    THE PREDICATE, PER ID (FS1 as completed by 82f922c), not by family
out    103  named_site[R8xx-<site>]  every id carries an R-number prefix -- 103 of 103 by a
              grep count on "^R[0-9]+-" -- so each names a finding AND a site     LIMB 1
        27  carries_the_finding[R845..R871]  names a finding                      LIMB 1
        10  survives_the_state[...]  satisfied through its INNER FAILED list, which I read
              for each of the ten: every inner id is a named_site or carries_the_finding
              case on R867-R871                                                   LIMB 1
         1  the_CI_section_is_about_the_REVIEWED_commit  "the CI section's first commit is
              d205833 and the verdict judged 945d250" -- names the newest verdict's own
              judged commit                                                       LIMB 1
         1  the_Carried_table_is_what_the_generator_produces  "32 generated rows are not in
              the report's Carried section", generated FROM docs/reviews/R1/step-3.md
                                                                                  LIMB 1
         1  the_generator_would_catch_a_row_under_the_wrong_number  StopIteration off that
              same empty baseline -- names nothing in its own line, and is verdict-dependent
              by the control below, which is the R507/frames.txt lesson            LIMB 1
         1  the_report_carries_a_WHOLE_SUITE_count  "the newest revision carries no
              whole-suite line" -- names NO finding, NO site                  **LIMB 2**
         1  the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  "run 39162423263: the table says
              in_progress, gh says failure" -- names NO finding, NO site      **LIMB 2**
       --- 143 under limb one, 2 under limb two, 145 total, NONE WITHOUT AN EXIT
cmd    the control that makes the trace a measurement and not a classification
out    bd315a1 (a verdict WITH its answering report), the two report-guard files, run by me in
       a worktree at that sha -> **149 passed, 0 failed**
       -- not one of the 145 is red where the boundary state is absent, so all 145 are
          boundary-dependent BY MEASUREMENT rather than by family
cmd    the two warnings, traced rather than left as a count
out    a numpy overflow in dot, from tests/verification/rung1/test_corpus_configurations.py on
       the orient_norm_overflow entry -- a reviewer corpus entry whose whole purpose is to
       overflow a norm. Designed.
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with FS1's predicate as completed by 82f922c; EG3 (i)
       -- every red tested INDIVIDUALLY or it is CZ1 (iv) unchanged
judge  **145 of 145 satisfy the predicate, so the waiver applies in full and CA2's HOLD is not
       reached by CI.** FR1's red-test head does not stand on the boundary reds. **This is the
       first round in step 3 in which no id had to be ruled by hand**, and that is the restored
       limb earning its place at its first application.
```

**Not CK2's exhausted-allowance state.** `runner_name` is null for all four jobs INCLUDING the
ladder job that SUCCEEDED, so an empty runner name cannot separate the states in this
repository and I did not use it. What separates them: both real jobs carry per-step
conclusions, real counts and eighteen- and four-minute durations, and the two skipped jobs are
the determinism workflow's own event gate (CK0) at a zero-second duration, which arises from a
designed condition and not from an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after.** Neither exception opens: this diff touches no part of F4's
load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a heading field. The last corpus commit remains
`ba1527e` (batch 47).

**I ran the recorded substitute and both halves paid again, for the ninth consecutive round.**
The continuum grid was eleven points on the RECORDED side of the new comparison -- the side the
commit created and did not sweep -- and it produced R872, R873 and R874. The regeneration check
was three full runs writing the three R1 deliverables, and its control half is what says the
repair is inert on the default path: `U = 1.71167` reproduced exactly against a deliverable
committed five commits earlier. **Every finding in this check came from one of those two, and
none from reading the diff.**

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff d06c577..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    the diff's added lines grepped for isclose, abs_tol, rel_tol, approx, atol, rtol,
       _COUNTER, tolerance, slack, epsilon and decimal literals
out    only heading VALUES -- 0.0, 45.0, 90.0, 44.9 -- in docstrings, refusal messages and
       test arguments. No comparison threshold, no new constant.
claim  the one thing in this diff that could function as a tolerance under another name is the
       heading comparison, and it is EXACT by decision
cmd    the comparison and the reason given for it
out    floatfea/run/pipeline.py:538 (uncovered_headings) -- "An EXACT comparison, because a
       heading is a declared input and not a measurement ... there is no tolerance here to
       choose." I tested the near miss through the NEW caller:
       refuse_headings_this_run_cannot_cover((44.9,), {"heading_deg": 45.0}) -> REFUSED.
rule   CLAUDE.md section Tolerances, its clause on anything that functions as a tolerance under
       another name; EU1
judge  **EU1 DOES NOT ATTACH BY ITS OWN WORDS** -- no tolerance value and no declared counter
       moves -- **and I ran the adversarial configuration anyway**, because R694's lesson is
       that a value which does not move is the worst case and not the safest. The
       configurations the diff did not choose are the eleven recorded-side points and the three
       full runs, and three findings came out of them. **The exact comparison remains the right
       FORM and I am not asking for a tolerance: a declared input compared with a tolerance is
       how 44.9 becomes 45.** R872 is not a tolerance request -- it is the question of whether
       360 and 0 are the same VALUE, which is arithmetic and not slack.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0; FK1 -- no `Closes:`
line, deliberately).** Step 3 remains open with all three reviewed revisions available, and
this check consumes none of them.

1. **FL2's items 3, 4 and 5, which is FS0's order and is where the turn said it is going.**
   Nothing in this check stands in the way. **R862 goes in the first of those that adds a timed
   stage, not after it** -- I verified the trigger has not fired rather than taking the word for
   it, and `floatfea/cli.py` is untouched by this diff.
2. **R867, R868 and R869 together in the first reviewed revision, or a stated reason not to.**
   Unchanged and correctly carried. One repair: refuse the topologies that cannot be built into
   a frame (R869 subsumes five of R867's seven), make the two that should run actually run
   (R867), and put one declared topology through a run (R868). `U = 1.82047` and `1.71167` are
   both already measured, so either is an assertable number.
3. **R872, R873 and R874 are ONE repair at `floatfea/run/pipeline.py:583-586`**, in the first
   reviewed revision or at the close: validate the recorded heading the way the declared side
   is validated, and decide once whether 360 is 0. Three lines and one recorded decision.
4. **R875 in one standalone `process:` commit citing FS1** -- `docs/SUPERVISOR.md:549` and
   `:555-557`. FF0 takes it into the next commit rather than the closure list, and it is not
   part of this verdict. **Read the whole EG3 section rather than grepping it**; three needles
   in a row have been short and the section is forty-five lines.
5. **R863, R864 and R865 in the first reviewed revision**, each with its figure regenerated at
   that commit (CP3). R847, R848, and R849 with R854, unchanged. R870 at the close or earlier.
   R852 is routed to FL3 and is not open.
6. **The FC1 criterion question is ANSWERED HERE as a repair** -- it does not go to Xabier as a
   ruling you took wrongly, because you did not. **The one line I would have him authorise** is
   in my section above and it narrows limb two; it leaves the loop and is not a round.
7. **The schedule, and FS4's checkpoint.** FR0's 5 November stands. FS4 asks for FL2 in its
   first reviewed revision by **26 October**: two of five items are built and verified on
   19 October, and the two sizing items carry FM0's re-solve loop and R862 with them. **Nothing
   has slipped and I am not re-opening the escalation FR0 answered.** If the 26th arrives with
   items 4 and 5 unbuilt, FS4 asks for that report ON THE 26TH with a realistic date, not at
   the step's close.
8. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 145
   reds identical to mine id for id on a different operating system, all six ladder rungs green,
   and mypy green on the machine where it was once red.

**What this turn got right, and it is the larger part.** It took the previous verdict's single
blocking finding, reproduced it through the CLI before touching anything, repaired it with the
local fact rather than waiting for the export path, and then **ablated its own first repair and
found that the new refusal was held by nothing at the call site** -- which is the defect R866
itself was, one layer over, found by the author rather than by me. The end-to-end pair it added
survives six mutations including one it did not run. The process commit is standalone, cites
its directive, deletes no guard, and restores one whose absence would have left this very run
with two reds and no exit. And it asked me, by name, to attack the one case standing between
the repair and a repeat of the finding, which is the right question to be asked.


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3 — ES0 INTERIM CHECK (counts against no round)
Reviewed commit: 945d250941b9fe8f79b16bd4170dbef225628348
**Reviewed commit: `945d250941b9fe8f79b16bd4170dbef225628348`.**
Verdict: HOLD
Tests: 3595 passed, 104 failed, 1 skipped, 2 warnings in 1005.68 s (0:16:45)   (my own run, at the reviewed commit, tree clean before and after)
Scope: **ES0 INTERIM CHECK, the fourth in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **ONE FINDING
BLOCKS (R866)** and it is in FL2(c), the item this turn shipped: `load_cases.headings` is
accepted, validated, and read by nothing, and `floatfea run` publishes all three deliverables
for a configuration declaring three headings. Five more findings are ledgered.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1";
`docs/directives/FR.md`). For R866 I state the silently wrong result it produces; for each of
the other five I state that it produces none, and for the one that will produce one later
(R869) I name the trigger.

**SIX COMMITS IN ONE TURN IS ONE CHECK, which is my own ruling from the previous round and I
hold to it.** The sequencing is better than one diff would have been: each item's own commit
told me which configuration its author chose, and both of the configurations that produced
findings are ones no commit chose.

```
cmd    git diff --name-status eb85d08..HEAD
out    M CLAUDE.md / M docs/SUPERVISOR.md / A docs/directives/FS.md /
       M docs/directives/README.md / M examples/platform12_placeholder.yaml /
       M floatfea/cli.py / M floatfea/model/platform.py / M floatfea/run/config.py /
       M floatfea/run/pipeline.py / M scripts/write_verdict.py /
       A tests/unit/test_headings_and_bem_coverage.py /
       A tests/unit/test_topology_from_config.py
cmd    git diff eb85d08..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff eb85d08..HEAD -- tests/conftest.py and the double-star pathspec
out    (empty)
cmd    git ls-files -- tests/conftest.py and the double-star pathspec
out    tests/conftest.py                       -- a file, as my instructions say it must be
cmd    git ls-files | grep -i conftest          -- the whole-tree census (CH2/CI0)
out    tests/conftest.py
       tests/test_supervisor_conftest_pathspec.py   -- one conftest, depth one, unchanged
cmd    git diff --stat eb85d08..HEAD -- .claude docs/SUPERVISOR.md
out    docs/SUPERVISOR.md | 99 +++------  (26 insertions, 73 deletions)
       -- NOT a STOP. It is in e227200, a STANDALONE process: commit citing FS1, whose only
          other file is CLAUDE.md; git show --stat e227200 touches no floatfea/ and no
          tests/. I read every removed line: the enumerations go, CZ1 (iv) stays, EG3 (i)
          stays and now cites the predicate. No guard was removed. One sentence SURVIVED
          that FS1 retired -- R871 below.
cmd    git diff --stat eb85d08..HEAD -- results scripts/measure
out    (empty)                                 -- no published deliverable moved
cmd    git status --porcelain
out    (empty)                                 -- clean before I ran anything and after
cmd    ruff check floatfea tests scripts ; black --check floatfea tests scripts ; mypy floatfea
out    All checks passed! / 150 files would be left unchanged /
       Success: no issues found in 42 source files
cmd    <this body> | python scripts/write_verdict.py --milestone R1 --step 3 --interim
out    the file you are reading
       -- **FS2's WRITE PATH IS EXERCISED AND IT WORKS. R856 IS ANSWERED.** This is the
          first verdict in step 3 that is not hand-written, and the implementer was right
          that the write was the one half it could not measure.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`) and four
verdicts are now newer than it. That is EG3 state (2) and it is the whole of this tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R856** (write_verdict.py refuses a step with no report) | **ANSWERED, and I verified the half the implementer could not: the WRITE.** | `scripts/write_verdict.py:166-180` adds `--interim`; `:233-236` puts "ES0 INTERIM CHECK (counts against no round)" in the header. This file went through it. I also checked what the new header could break and it breaks nothing: a grep for the heading across `scripts`, `tests` and `.claude` reaches `write_verdict.py:234`, two synthetic fixtures in `tests/test_report_carried.py` and the agent template; the `Stop` hook and all four resolvers read the `Verdict:` and `Reviewed commit:` lines, both unchanged. |
| **R835, R836** (EG3's enumerated lists, nine measurements, wrong in both directions) | **ANSWERED by FS1/e227200, and I applied the predicate per id to all 104 reds rather than ruling a cascade. 102 satisfy it; TWO DO NOT -- R871 and my criterion note.** | `CLAUDE.md:429-477`, `docs/SUPERVISOR.md:556-585`. The predicate is right where the lists were wrong, and its first application is measured in the CI section below. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **ANSWERED as a ROUTING decision: FS3 ledgers it to FL3**, and the directive is now recorded where a repair can be checked against it (`docs/directives/FS.md:28`, FP0). | Not the implementer's to repair in code, and no longer open against step 3. |
| **R862** (three hand copies of the stage set; the pipeline computes the published total) | **still open, correctly, and NOT YET DUE -- I measured that the trigger has not fired rather than taking the commit's word.** | The five timing assignments in `floatfea/run/pipeline.py` are unchanged (653, 701, 712, 717, with 720-721 summing four of them) and `WALL_TIME_STAGES` at `floatfea/cli.py:37-43` is unchanged. **No timed stage was added, so the 40.000 s understatement is not reachable at this commit.** It blocks in the commit that adds one, which is FS0's item 4 or 5. |
| **R863** (the exclusion set is now defined by the code under test) | **still open, untouched** | the diff over `tests/regression` since eb85d08 is empty. |
| **R864** (the byte-identity claim's witness is blind to its own subject) | **still open; its condition is a sentence in the report and no report revision exists** | unchanged by this diff. |
| **R865** (the docstring at `tests/regression/test_r1_example_regenerates.py:224`) | **still open, untouched, correctly so** | same empty diff over `tests/regression`. |
| **R847 / C43** (section 3's "0 of 49 rows" does not reproduce) | **still open; FR1's third class, and no revision exists in which it could be answered** | unchanged. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot, a padded dot) | **still open, untouched** | the diff over `floatfea/cli.py` since eb85d08 is one comment block inside `_cmd_export`. |
| **R849 with R854** (four gates quantify over hard-coded three-file tuples) | **still open, both sites; step 3 has added no deliverable yet, so it is not yet worse** | `tests/regression/test_r1_example_regenerates.py:51`; `tests/regression/test_r1_published_artifacts.py:69`. R862 is the same species in a third place. |
| **R855** (the suite at a commit carrying no report revision) | **WITHDRAWN, and the standing condition IS MET at this commit** | the turn states plainly which runs it made (267 passed on two subsets, 2516 passed over three directories) and that it did NOT measure the whole suite at 945d250. No green is stated that was not taken. **I produced the whole-suite number, as I do by rule: 104 failed, 3595 passed, 1 skipped.** |
| **The fourth wrong figure** (290 where the run printed 267) | **CORRECTED ON THE RECORD, and I re-took the figure rather than accepting that it had been checked** | `945d250` names the pattern (R853, R857, R844, this) instead of the instance, which is what BP0 asks for. I re-ran the command `cadbbf7` cites -- `pytest -q tests/unit tests/regression/test_r1_published_artifacts.py` -> **267 passed** at this commit. The nine refusal messages reproduce and the 19-passed revert-red-restore baseline reproduces. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally AND on a machine neither of us controls** | mine above; CI run 39361398619, job `lint, unit and guards`, read at STEP level: actionlint, ruff, black --check, mypy and unit tests all SUCCESS, only `guards and meta-tests` FAILURE. Every step RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | unchanged by this diff. |
| **C44, C45** | **C44 carries. C45 RECURRED IN THIS TURN'S OWN PROCESS COMMIT and that is R871** -- the commit that retired the hand lists left one in my instructions and removed it from `CLAUDE.md`. | measured in R871. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE, by the control rather than by family** | at `bd315a1` -- a commit where a verdict exists WITH its answering report -- the two report-guard files are **149 passed, 0 failed**, so not one of this tree's 104 reds is red where the boundary state is absent. That is the measurement that separates "red because no answering report exists" from "red for another reason", and it is what covers the two ids the predicate does not admit. |
| scripts/suite_count.py's own line, and CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## Findings

**ONE BLOCKS.** No tolerance moved, no conftest moved, no published deliverable moved -- and I
established the last of those by regenerating the deliverables from this tree rather than by
reading the diff: **the default star is unmoved, `U = 1.71167 at platform:hub4_arm ROOT
(T = 12.5 s, 3.3.2 interaction)`, identical to the committed `results/R1/example/report.md:63`.**
The label-preservation property FL2(a) was built around holds, and I checked it by running the
model rather than by reading `_platform_label`.

**R866. (BLOCKS -- FR1's second head, an input accepted and used other than as declared)
`load_cases.headings` IS PARSED, RANGE-CHECKED, REPEAT-CHECKED -- AND READ BY NOTHING.
`floatfea run` ACCEPTS A CONFIGURATION DECLARING THREE HEADINGS, EXITS 0, AND WRITES ALL THREE
PUBLISHED DELIVERABLES FOR ONE. This repository already refuses exactly this situation twelve
lines away (R809), and the new field departs from that pattern.**

```
claim  nothing in floatfea/ reads the declared heading set
cmd    grep -rn "headings" --include=*.py floatfea
out    floatfea/run/config.py       -- the field (:421) and its parser (:866)
       floatfea/run/pipeline.py:515 -- uncovered_headings
       floatfea/run/pipeline.py:543 -- refuse_uncovered_headings
       floatfea/cli.py:407          -- a COMMENT saying where the call site would go
       -- ZERO call sites of either function in floatfea/; the only callers are the new tests
cell   the shipped example with load_cases.headings [0.0, 45.0, 90.0] and NOTHING else
       changed, through the real CLI, outputs redirected to a temporary directory
out    $ python -m floatfea.cli run <that config>
       EXIT=0
       wrote member_forces.csv (1248 rows) / utilisation.csv (32 rows) / report.md
       governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       total wall time 77.35 s
       -- 1248 rows and 32 stations, the same as the single-heading baseline, because the
          declared set reached nothing
cmd    what the three artifacts say about the heading they were produced at
out    report.md:7   * **config** -- headings_three_declared.yaml
       report.md:23  * **heading** -- 0.0 deg
       report.md:55  EX3/R724: where a run covers a SINGLE heading the heading dependence
                     is UNTESTED ...
       utilisation.csv line 3: "# caveat: ... where a run covers a SINGLE heading ..."
       -- the caveat is TRUE OF THE RUN AND FALSE OF THE CONFIGURATION, and nothing anywhere
          names the two declared headings that were never run
cmd    the pattern this repository already has for a declared input it cannot honour
out    floatfea/cli.py:354-362, R809:
         if cfg.outputs.required_section or cfg.outputs.truss_sizing:
             raise ConfigError("... are FL2(b) and are not wired in R1 step 1 ... Refused
               before any output is written, so nothing on disk describes a run that did
               not happen.")
       -- the same shape, in the same function, twelve lines above the run_pipeline call,
          and R809's own recorded reason is that three artifacts had been left on disk
          mentioning the refusal nowhere
cmd    whether the missing check is buildable HERE, which is the question the turn asked me
out    floatfea/run/pipeline.py:558 exported_wave_basis ALREADY reads the heading the npz was
       exported at, from the sidecar, in this repository, with no HSP worktree -- measured on
       the committed data/f4/dynamic_inputs.npz it returns heading_deg 0.0. So "the declared
       set must be exactly the heading this npz carries" is one comparison between two
       values that are both already in hand.
rule   FR1's second head, verbatim -- "an input accepted and used other than as declared";
       and CLAUDE.md's non-negotiable that a validation failure never degrades to a warning
judge  **THE SILENTLY WRONG RESULT, stated as FR1 requires: `results/<dir>/utilisation.csv`
       and `report.md` published as the output of a configuration declaring headings
       [0, 45, 90], with U = 1.71167 presented as THE governing utilisation, when it is the
       envelope over heading 0 alone.** Someone sizes steel against a U that covers one of
       three declared wave directions, and no line in any artifact and no exit code says so.
       The field's own docstring at `floatfea/run/config.py:425` ANTICIPATES the reader who
       will expect the envelope -- which makes this the known case rather than the missed
       one, and the docstring is in the file that reader does not open. `examples/` documents
       the new `topology` block in twenty-two lines and the new `headings` field in none.
```

**Closed when** `floatfea run` refuses a declared `load_cases.headings` it cannot honour,
before any output is written, in the form R809 already uses at `floatfea/cli.py:354` -- and the
sharper form is available for free: refuse unless the declared set is exactly the heading
`exported_wave_basis` read from the npz, naming both values. The ENVELOPE is not what I am
asking for; see the scope answer below.

**R867. (DOES NOT BLOCK -- ledgered) DECLARATION ORDER AND DIRECTION DECIDE WHETHER A DECLARED
TOPOLOGY CAN BE RUN AT ALL. The schema says order and direction do not identify a member (it
compares a frozenset); the builder's node NAMES say they do. Measured: the same five members
declared brace-first die with a KeyError three layers downstream -- and that is the exact order
the turn's own test uses.**

```
claim  a valid declared topology is runnable or not depending on the order it is written in
cell   nine topologies through the real builder, then joint_nodes_of, then the real CLI; one
       variable moved each; outputs redirected so no committed artifact was touched
out    the declared star                  run OK   U = 1.71167   (identical to the default)
       braced star, ARMS FIRST            run OK   U = 1.82047   1326 rows, 34 stations
       braced star, BRACE FIRST           EXIT 1   KeyError: no node named
                                                   'platform:hub1_arm_tip'   (0.1 s)
       one arm written [hub1, centre]     EXIT 1   KeyError, the same
       hub4 reached only by a brace       EXIT 1   KeyError, the same
       a ring with no centre member       EXIT 1   KeyError, the same
       three arms only                    EXIT 1   KeyError, the same
       a single member                    EXIT 1   KeyError, the same
       an unknown node hub9               REFUSED at build, by name, as designed
cmd    why order decides it, from the code rather than from the run
out    floatfea/model/platform.py:629 -- node() dedups by COORDINATE and keeps the name of
       whichever label reached the point FIRST. A brace declared before the arm that shares
       its hub takes the node, so the arm's platform:<hub>_arm_tip name is never created;
       and [hub1, centre] names it _arm_a rather than _arm_tip.
       floatfea/solve/static.py:135 and floatfea/post/forces_table.py:169 then look that
       name up and nodes.index raises.
cmd    the schema's own position on whether order identifies a member
out    floatfea/run/config.py:898 -- the duplicate key is a frozenset, so [hub1, centre] is
       refused as a duplicate of [centre, hub1]. The two layers disagree about whether
       direction matters.
cmd    the direction that is SAFE, measured before I claimed the one that is not (EH4)
out    for the name platform:<hub>_arm_tip to exist at all, some member must be labelled
       platform:<hub>_arm with its END away from the body centre, which requires the FIRST
       declared end to be centre -- so the tip name, WHEN IT EXISTS, is always at that hub's
       own deck joint. **A declared topology can lose a support node; it cannot silently
       acquire the wrong one.** That is why this is loud rather than silent, and I measured
       it rather than assuming it.
rule   FR1 -- a refusal whose message is unclear but whose outcome is right does not block;
       and my own guard that a gate carries its own failure, applied to the feature itself
judge  **it does not block: exit 1, a traceback, and nothing written** -- I checked the last
       clause by listing the output directory after the brace-first run, and no directory was
       created. What it costs is the feature: FL2(a)'s whole subject is non-star topologies,
       and of the eight non-default topologies I declared, exactly ONE runs. The two that
       SHOULD run and do not (brace-first, and an arm written the other way round) are
       rejected by a name lookup rather than by a refusal, which is why no reader would get
       "write the arms first" out of the message.
```

**Closed when** the node name is independent of declaration order and direction, or the schema
refuses the orders the builder cannot honour and names what to change -- in
`floatfea/run/config.py` if it is a schema rule, at `floatfea/model/platform.py:629` if it is a
naming one.

**R868. (DOES NOT BLOCK -- ledgered) THE COMMITTED TEST FOR "A NON-STAR TOPOLOGY" BUILDS THE
ONE ORDER THAT CANNOT BE RUN, AND NO TEST IN THE DIFF PUTS ANY DECLARED TOPOLOGY THROUGH A
SOLVE. The shipped example's comment shows the runnable order; the shipped test shows the
other one, and nothing compares them.**

```
claim  the new tests stop at the builder, so R867 was outside the collection they inspect
cmd    tests/unit/test_topology_from_config.py:92
out    braced = (("hub1", "hub2"), *STAR)      <- the brace FIRST, the order that dies
       ... and the case asserts labels, the centre name, the centre xy and len(members) == 5
cmd    how far the file reaches
out    a grep for solve, joint_nodes_of, compute_rows and run( in that file finds nothing.
       Nineteen cases, every one of them at build_superstructure or load_config.
cmd    the shipped documentation on the same question
out    examples/platform12_placeholder.yaml:35 lists the four arms and THEN [hub1, hub2] --
       the order that runs. The example and the test disagree and nothing compares them.
rule   my own recorded guard -- check that the collection the assertion inspects can actually
       contain the failure; and BE3's species, a check verified against inputs its own author
       chose
judge  **it does not block** -- no number is wrong and every one of the nineteen cases asserts
       something true. It is recorded because it is the reason R867 shipped: nineteen green
       cases over a feature whose failure is three layers past where all nineteen stop.
```

**Closed when** one case takes a declared non-default topology through `floatfea run` (or at
minimum through `joint_nodes_of` and `compute_rows`) and asserts a published number -- the
braced star's `U = 1.82047` is a value this round has already measured.

**R869. (DOES NOT BLOCK AT THIS COMMIT -- ledgered, WITH ITS TRIGGER NAMED) A DECLARED TOPOLOGY
THAT DOES NOT REACH THE CENTRE BUILDS HAPPILY, AND `_build_body` RIGID-LINKS THE WHOLE PLATFORM
REMAINDER -- 1.875e+06 kg at the shipped f -- TO A `platform_centre` NODE THAT IS AN ENDPOINT OF
NO MEMBER. Nothing refuses the disconnection; the only thing that stops it is R867's name
lookup.**

```
claim  the builder has no connectivity check, so the remainder can hang off nothing
cell   the ring ([hub1,hub2], [hub2,hub3], [hub3,hub4], [hub4,hub1]), built
out    members: platform:hub1_hub2, platform:hub2_hub3, platform:hub3_hub4,
                platform:hub4_hub1
       node names: platform_centre, platform:hub1_hub2_a, platform:hub1_hub2_tip,
                   platform:hub2_hub3_tip, platform:hub3_hub4_tip, platform_remainder
       -> platform_centre is node 0 and NO member has it as an endpoint
       check_limits, check_rigid_modes and admissible all pass; the build RETURNS
cmd    what centre_node carries
out    floatfea/model/platform.py:626 creates it unconditionally, and rigid_links (:762) ties
       remainder_node to it and measures the offset from it. remainder_mass at the shipped
       f = 0.5 is 1.875e+06 kg -- the same magnitude as every member's share put together.
cmd    whether anything refuses the disconnection
out    a grep for connected, connectivity and component in floatfea/model/platform.py finds
       nothing. The refusal that does fire is KeyError: no node named
       'platform:hub1_arm_tip', which is about a NAME and not about a graph.
cmd    why it does not block TODAY, measured rather than asserted
out    every path from a declared topology to a number goes through
       floatfea/post/forces_table.py:169 or floatfea/solve/static.py:135; the CLI has exactly
       two subcommands (run, export), export refuses unconditionally, and the ring run raised
       in 0.1 s with no output directory created.
rule   FR1's first head; and my own guard that a residual destroys information, applied to a
       mass that is present in the mass report and absent from the stiffness
judge  **it does not block at this commit and it is one accident away from doing so.** The
       accident is any path that solves a body without looking a tip name up -- a
       topology-aware support scheme is the obvious one, and FS0's items 4 and 5 re-solve.
       **At the commit where that happens, the platform's entire remainder mass and the loads
       reaching it are structurally absent from the frame, every member force is low by the
       share it carried, and the mass report still balances.** That is the defect the turn
       correctly found in geometry[0][1], one step further out: the centre is now in the right
       PLACE and still need not be attached to anything.
```

**Closed when** the builder refuses a declared platform topology whose members do not connect
the centre to every hub the deck owns, naming the hubs that are unreachable -- which also
subsumes five of R867's seven refusing cases and leaves R867 as the two that should run.

**R870. (DOES NOT BLOCK -- ledgered) FL2(a) AS SHIPPED IS A SUBSET OF THE LOCKED PLAN'S (a),
AND TWO SENTENCES IN `floatfea/run/pipeline.py` NOW DESCRIBE IT IN THE FUTURE TENSE WHILE IT HAS
LANDED.**

```
claim  the plan's (a) names four things and two of them are not built
cmd    docs/milestones/R1.md:81
out    "Member topology from the config: a list of members (body, end A / end B by node,
        joint label or coordinates, section group)."
       built:     ends by NODE NAME, platform only
       not built: COORDINATES (an end can only be centre or a deck hub, so a brace to a
                  mid-arm point cannot be declared) and SECTION GROUP per member; and body
                  is platform-only, which the commit justifies and I accept -- the hub
                  tripods are the deck's fact
cmd    the two source-tree sentences
out    floatfea/run/pipeline.py:123 "FL2(a) replaces this with a member list carrying its own
         group labels"  -- FL2(a) has landed and it does not
       floatfea/run/pipeline.py:180 "FL2(a) is where the builder gains per-body fractions"
         -- it did not
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; and the step-3 gate at
       docs/milestones/R1.md:352, which is what the closing revision is judged against
judge  **it does not block**: no number is wrong, and both sentences sit inside refusals whose
       OUTCOMES are right. It is recorded now rather than at the close, because the closing
       revision will be read against FL2(a) and not against the commit message, and because
       the two refusals currently point a reader at a milestone that has already happened.
```

**Closed when** the first reviewed revision either builds the two remaining axes or records the
deviation with its reason, and the two sentences say what is true at their own commit.

**R871. (DOES NOT BLOCK -- apparatus, FF0 class: fixed in the next commit, not ledgered) FS1'S
OWN COMMIT LEFT A HAND LIST IN MY INSTRUCTIONS AND REMOVED IT FROM `CLAUDE.md`. Its check could
not see it, because the needle looked for the words "state (2) list" and the surviving list is
introduced by "The only failures are". AND FC1'S CLAUSE IS NOW ABSENT FROM BOTH FILES, so the
two reds FC1 existed to admit have no clause under which they are boundary reds.**

```
cmd    the two files on the same sentence
out    CLAUDE.md:421           "(2) Verdict written, answering report not yet. The answering
                                report clears them."
       docs/SUPERVISOR.md:547  "(2) ... THE ONLY FAILURES ARE
                                test_every_named_site_is_touched_or_declared,
                                test_the_report_carries_the_finding,
                                test_the_CI_section_is_about_the_REVIEWED_commit,
                                test_the_Carried_table_is_what_the_generator_produces and
                                test_the_generator_would_catch_a_row_under_the_wrong_number,
                                each naming a finding or a site of the newest verdict."
cmd    the commit's own check, re-run
out    grep -c over both files for the three list phrases
       -> CLAUDE.md:0   docs/SUPERVISOR.md:0      -- TRUE, and blind to the surviving list
cmd    the needle that does find it
out    grep -c test_every_named_site_is_touched_or_declared CLAUDE.md docs/SUPERVISOR.md
       -> CLAUDE.md:0   docs/SUPERVISOR.md:1
cmd    FC1 clause
out    grep -c for the FC1 heading in both files
       -> 0 and 0                                   -- removed from both
rule   C45, which is this item own name -- a mirror of a living document is a figure whose
       rule moves underneath it, which is BP0 applied to the criterion; and R755/R770 shape,
       a census whose domain cannot contain the thing it is looking for
judge  **it does not block under FR1**: no wrong result follows, and it is the gating
       apparatus, which FF0 takes out of the ledger and into the next commit. Two separate
       things in one finding -- the surviving list is C45 fifth occurrence and is one line to
       delete, and the missing FC1 clause is the criterion gap in my disagreement section
       below, which I ruled around with the bd315a1 control rather than holding the tree on.
```

**Closed when** `docs/SUPERVISOR.md:547` stops enumerating and cites the predicate, in a
standalone `process:` commit citing FS1 -- and the FC1 question is answered by Xabier.

The three commands above, verbatim, so the next reader re-runs them rather than reconstructing:

```
grep -c "state (1)'s list\|state (2)'s list\|own list" CLAUDE.md docs/SUPERVISOR.md
grep -c "test_every_named_site_is_touched_or_declared" CLAUDE.md docs/SUPERVISOR.md
grep -c "The two CZ1-class guards join state (2)" CLAUDE.md docs/SUPERVISOR.md
```

## Where I disagree with the CRITERION rather than with the work (said once, for Xabier)

**FS1's predicate is better than the lists at every id I tested but two, and those two are
structurally unpassable, so a literal reading of it has no exit.**

```
cmd    the predicate applied to all 104 reds, one id at a time
out    68  test_every_named_site_is_touched_or_declared[R85x-<site>]  names a finding AND a
                                                                      site of the newest
                                                                      verdict           OK
       21  test_the_report_carries_the_finding[R845..R865]             names a finding   OK
       10  test_the_guard_survives_the_state[...]                      satisfied only
             through its INNER FAILED list, which names R862, R863 and R865 sites -- I ran
             them and read the inner lists rather than ruling them by family            OK
        1  test_the_CI_section_is_about_the_REVIEWED_commit            "the CI section's
             first commit is d205833 and the verdict judged d89566d"    names the newest
                                                                        verdict          OK
        1  test_the_Carried_table_is_what_the_generator_produces       "26 generated rows
             are not in the report's Carried section" -- generated FROM the newest verdict OK
        1  test_the_generator_would_catch_a_row_under_the_wrong_number  StopIteration off
             that same baseline                                                         OK
        1  test_the_report_carries_a_WHOLE_SUITE_count   "the newest revision carries no
             whole-suite line"               -- names NO finding and NO site       **NOT OK**
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW  "run 39162423263: the table says
             in_progress, gh says failure"   -- names NO finding and NO site       **NOT OK**
cmd    what the two are, and why no commit can ever clear them
out    they are FC1's pair. scripts/suite_count.py measures a CLEAN WORKTREE AT A COMMIT, so
       the line naming a sha cannot be inside that sha; scripts/ci_section.py --rounds needs
       a RUN, and no run exists for a commit before it is pushed. **FC1's clause was deleted
       from CLAUDE.md by this turn's own process commit** and survives only as a bullet
       explaining why the lists went.
cmd    the control I ruled on instead
out    bd315a1 (a verdict WITH its answering report), the two report-guard files
       -> 149 passed, 0 failed, and every one of this tree's 104 absent from that set
judge  **I ruled both as boundary reds under CZ1's own reusable half** -- "a check whose input
       is the commit itself cannot be measured before the commit exists" -- and I measured it
       rather than asserting it. I am not expressing this as a HOLD: it is not one of FR1's
       heads, and the right answer is a clause and not a commit. **The fix is one sentence:
       the predicate, OR CZ1's reusable half.** Without it the next reviewer reads "any other
       red blocks", finds two, and has no exit -- which is DD1's shape, and DD1 cost two
       verdicts that were not about the work.
```

## Try to break it -- what I ran, and what it found

* **Nine declared topologies, none of them the two the commits chose**, through the real
  builder, then `joint_nodes_of`, then the real CLI with outputs redirected: a ring with no
  centre member, a single member, three arms only, hub4 reached only by a brace, an arm written
  `[hub1, centre]`, the brace declared first, the brace declared last, the declared star, and an
  unknown node name. **One of the eight non-default topologies runs.** That produced R867, R868
  and R869. The implementer named three of these cases itself and was right that they were the
  ones to try.
* **Three full `floatfea run` executions writing all three deliverables into a temporary
  directory**: the baseline-equivalent (`U = 1.71167`, 1248 rows, 32 stations, identical to the
  committed `results/R1/example/report.md:63`), the braced star (`U = 1.82047`, 1326 rows, 34
  stations) and the three-heading configuration (`U = 1.71167`, 1248 rows -- R866). The first is
  the control that says both commits moved nothing on the default path, taken by running the
  model rather than by reading the diff. The second says a declared topology is NOT inert: it
  reaches the published number.
* **Both EH4 directions on the one new decision rule.** Strengthening: every malformation of
  `covered` I could construct makes `uncovered_headings` refuse MORE and never less -- a string
  `0,45`, radians and an empty tuple all return the declared heading as uncovered, `None` raises
  a `TypeError`, and ints, `numpy.float64`, `float32` and a plain list all compare equal, so no
  declared heading passes that should not. Weakening: the only input that could make a declared
  heading pass wrongly is a `covered` set that contains it, which is the caller's fact and is
  precisely why the parameter is a parameter. **The function is sound; what is missing is a
  caller, and that is R866.**
* **The schema's refusals re-run rather than read**: the nine `topology` cases and the seven
  `headings` cases all refuse with the needles claimed, and `_checked` at
  `floatfea/run/config.py:202` refuses a bool and a NaN explicitly, so `headings` reuses the one
  declared domain rather than a second copy of it. That half of FL2(c) is solid.
* **The predicate's first application, 104 ids one at a time**, with the cascade read off its own
  inner FAILED lists, plus the `bd315a1` control. That produced R871 and the criterion note.
* **My own set against CI's, both directions.** `comm -23` and `comm -13` over the two sorted
  104-id lists are both empty: the SAME SET, id for id, on two operating systems.
* **The new verdict header against every resolver that reads a verdict file, before I used it.**
  No guard keys on the heading line, so FS2's suffix cannot make this verdict invisible to the
  hook or to the three report guards.

**What I did not find, and it is the larger part.** FL2(a) found and fixed a real defect its own
feature would have created, in the place that is hardest to see -- a centre inferred from the
first member, which is correct for every configuration that existed before the commit -- and
fixed it by passing the fact down from the layer that owns it rather than by adding an assertion.
The property that mattered most, the declared star being the generated star with its labels,
holds under a full run and not only under a unit test. The commit that corrected its own wrong
figure did it on the record rather than by amending, and named the pattern instead of the
instance. FS1 removes an enumeration that was wrong in both directions and keeps CZ1 (iv) and
EG3 (i) intact; FS2's message says plainly which half it could not measure, which is exactly the
half I measured, and it works. `uncovered_headings` is a good function with its covered set
correctly parameterised.

## The two scope questions, answered

**On FL(c)'s third part: your reading is RIGHT and I am not asking you to build the envelope.**
A dynamic-inputs npz records one heading -- `exported_wave_basis` returns a single `heading_deg`,
the committed npz carries no heading key at all and the value lives in the sidecar -- so an
envelope over several headings needs load data at several headings, and manufacturing it is
"never invent a load distribution", which is CLAUDE.md's own non-negotiable and not a judgement
call. **What I would separate out, as a scope statement for Xabier and not as a finding:** the
MECHANISM is buildable here and the DATA is not. `load_cases.npz` is a single path; making it a
list, one file per heading, each carrying its own recorded heading, with the envelope over the
union and the governing heading reported, needs no HSP worktree -- it needs a second file, and
the second file is `export`'s job. Put that way the item stops being "underdetermined" and
becomes "the mechanism waits on nothing, the data waits on FL1", which is a smaller thing to
carry into FL3.

**On the BEM covered set being a parameter: AGREED, and that is not what R866 is.** Which
headings the dataset carries is the pinned HSP state's fact, a hard-coded list here would be
FloatFEA asserting something nothing in this tree can check, and taking it as an argument is the
right call -- I tried to break the function and could not. The step that went one too far is the
next one: "the covered set is HSP's fact" was used to leave the refusal with **no call site at
all**, while the fact that IS local -- the heading the npz in hand was exported at, which
`exported_wave_basis` already reads -- is compared against nothing. So, to your question as you
asked it: no, you have not used "it is HSP's fact" to avoid building the BEM check. You have
used the absence of a call site for THAT check as the reason there is no heading check at all in
`run`, and the local one is buildable today.

## CI at the reviewed commit: RED, 104 reds, ALL 104 boundary by MEASUREMENT

```
cmd    gh run list --commit 945d250941b9fe8f79b16bd4170dbef225628348
         --json conclusion,status,databaseId,workflowName
out    one run: databaseId 39361398619, workflowName CI, status completed,
       conclusion failure
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The judged commit had a run because it was pushed
          first (FP1).
       A NOTE FOR WHOEVER GENERATES THE CI SECTION: the same command with the SHORT sha,
          945d250, returns an empty list. The full sha returns the run. No bearing on this
          verdict; recorded because the generator takes a sha.
cmd    gh run view 39361398619 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1, 2, 3, 6, 4 and 5 -- all six rungs SUCCESS. No rung is red, so nothing
         above is uninterpretable and there is no STOP.
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS / guards and meta-tests FAILURE
         -- every step RAN rather than being skipped behind an earlier red, which is what
            CZ1 (iii) exists to see, and mypy is green there, so FP1's CI-only types-PyYAML
            red has stayed fixed
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39361398619 --log-failed, unique ids
out    68  test_every_named_site_is_touched_or_declared[...]
       21  test_the_report_carries_the_finding[R845..R865]
       10  test_the_guard_survives_the_state[baseline + 9]
        5  the five named in my criterion section above
       --- 68 + 21 + 10 + 5 = 104 exactly, with no remainder, and all 104 inside
           tests/test_report_carried.py and tests/test_report_guard_states.py
cmd    my own 104 against CI's 104, both directions
out    comm -23 (mine) (CI's)   (empty)
       comm -13 (mine) (CI's)   (empty)        -- the SAME SET, two machines, two OSes
cmd    the control that makes the trace a measurement and not a classification
out    bd315a1, the two report-guard files -> 149 passed, 0 failed
       -- not one of the 104 is red where a verdict exists WITH its answering report, so all
          104 are boundary-dependent BY MEASUREMENT rather than by family
cmd    the warning, traced rather than left as a count
out    a numpy overflow in dot, raised by
       tests/verification/rung1/test_corpus_configurations.py with the orient_norm_overflow
       entry -- a reviewer corpus entry whose whole purpose is to overflow a norm. Designed.
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with FS1's predicate; EG3 (i) -- every red tested
       INDIVIDUALLY or it is CZ1 (iv) unchanged
judge  **102 of 104 satisfy the predicate, the remaining two are FC1's pair and are boundary by
       the control, so the waiver applies in full and CA2's HOLD is not reached by CI.** FR1's
       red-test head does not stand on the boundary reds. **This verdict's HOLD is R866 and
       nothing else.**
```

**Not CK2's exhausted-allowance state.** `runnerName` is null for all four jobs including the two
that SUCCEEDED, so an empty runner name cannot separate the states in this repository and I did
not use it. What separates them: both real jobs carry per-step conclusions, real counts and four-
and fifteen-minute durations (02:54:02Z to 02:58:32Z, and 02:54:01Z to 03:09:30Z), and the two
skipped jobs are the determinism workflow's own event gate (CK0), with empty step lists at a
zero-second duration, which arises from a designed condition and not from an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after.** Neither exception opens: this diff touches no part of F4's load-mapping
gate, and EB6's label-provenance gate is about buoy-centre labels in `tests/verification/rung4/`,
not about a topology list or a heading field. The last corpus commit remains `ba1527e`
(batch 47).

**I ran the recorded substitute and both halves paid again, for the eighth consecutive round:**

* **A continuum grid over the parameter space the new decision rules guard.** Two axes, because
  the diff moved two. The TOPOLOGY axis: member count 1/3/4/5, centre-touching or not,
  declaration order brace-first against arms-first, direction centre-then-hub against
  hub-then-centre, a hub reachable by its own arm against by a brace, and a known against an
  unknown node name. The COVERED-SET axis for `uncovered_headings`: tuple, list, numpy float64,
  numpy float32, ints, a string, radians, empty, `None`, minus-zero against zero, and 360 against
  0. It produced **R867, R868 and R869**, every one from a point on the order/connectivity axis
  that no commit swept.
* **A regeneration check on a published deliverable, in both directions.** Three full runs
  writing the three R1 artifacts: the default path reproduces the committed governing
  `U = 1.71167` exactly, which is the control; the braced star moves it to `1.82047`, which says
  the feature is live; and the three-heading configuration reproduces `1.71167` while declaring
  two headings that never happened, which is **R866**, this round's blocking finding.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff eb85d08..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    the same diff, plus lines only, grepped for isclose, abs_tol, rel_tol, approx, atol,
       rtol, _COUNTER, tolerance, slack and epsilon
out    tests/unit/test_topology_from_config.py:70  "not-a-tolerance: the same two points"
       tests/unit/test_headings_and_bem_coverage.py:110  "not-a-tolerance: the declared
                                                          domain"
       -- two exactness comparisons, both annotated, neither introducing a value
claim  the one thing in this diff that could function as a tolerance under another name is the
       heading comparison in uncovered_headings, and it is EXACT by decision
cmd    the comparison, and the reason given for it
out    floatfea/run/pipeline.py:534 -- "An EXACT comparison, because a heading is a declared
       input and not a measurement ... there is no tolerance here to choose."
       I tested the near miss: uncovered_headings((44.9,), (0,45,90,135,180)) -> (44.9,)
rule   CLAUDE.md section Tolerances, its clause on anything that functions as a tolerance under
       another name; EU1
judge  **EU1 does not attach by its own words** -- no tolerance value and no declared counter
       moves -- **and I ran the adversarial case anyway**, because R694's lesson is that a value
       which does not move is the worst case and not the safest. The configurations the diff did
       not choose are the eight topologies and the three-heading config, and three findings came
       out of them. **The exact comparison is the right form here and I am not asking for a
       tolerance: a declared input compared with a tolerance is how 44.9 becomes 45.**
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line, deliberately, and the tool now writes a header that says which kind of verdict this is).**
Step 3 remains open with all three reviewed revisions available. **The HOLD is R866, and it is
answered before FL2's items 3, 4 and 5 continue** -- which costs FS0 nothing, because R866 IS an
FL2(c) item and the repair is the shape R809 already has twelve lines away.

1. **R866, before the next FL2 item.** A refusal in `_cmd_run`, before any output is written, for
   a declared `load_cases.headings` the run cannot honour -- and the sharper form is free: refuse
   unless the declared set is exactly the heading `exported_wave_basis` read from the npz, naming
   both values. One test that runs the shipped example with three declared headings and asserts
   the exit is non-zero AND the output directory is empty, which is R809's own two-part
   assertion.
2. **R867, R868 and R869 together in the first reviewed revision, or a stated reason not to.**
   They are one repair: refuse the topologies that cannot be built into a frame (R869 subsumes
   five of R867's seven), make the two that should run actually run (R867), and put one declared
   topology through a run (R868). The braced star's `U = 1.82047` and the default's `1.71167` are
   both measured in this verdict, so either is an assertable number.
3. **R862 IN THE COMMIT THAT ADDS A TIMED STAGE, not after it** -- unchanged, and verified not
   yet due. R863, R864 and R865 in the first reviewed revision, each with its figure regenerated
   at that commit (CP3). R847, R848, and R849 with R854, unchanged. R870 at the close or earlier.
4. **R871 in one standalone `process:` commit citing FS1** -- one sentence in
   `docs/SUPERVISOR.md:547`. It is apparatus, so FF0 takes it into the next commit rather than
   into the closure list, and it is not part of the HOLD.
5. **The FC1 question goes to Xabier with my criterion note, not into a round.** I ruled around
   it this time with the `bd315a1` control; the next reviewer reading "any other red blocks" will
   find two and have no exit.
6. **R852 is now routed rather than open** (FS3 to FL3). R856 and R835/R836 are ANSWERED by this
   turn's two process commits, and I exercised the write path that FS2's own message said it
   could not.
7. **The schedule, and FS4's checkpoint.** FR0's 5 November stands. FS4 asks for FL2 in its first
   reviewed revision by **26 October**: two of five items are built on 19 October, the band check
   is next, and the two sizing items carry FM0's re-solve loop and R862 with them. **Nothing has
   slipped yet and I am not re-opening the escalation FR0 answered** -- but the two sizing items
   are the large ones and they sit behind a checkpoint four days out. If the 26th arrives with
   items 4 and 5 unbuilt, FS4 asks for that report ON THE 26TH with a realistic date, not at the
   step's close.
8. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 104
   reds identical to mine id for id on a different operating system, and all six ladder rungs
   green.

**What this turn got right, and it is much the larger part.** It took FS0's order seriously and
built the model-facing item first. It found a real defect its own feature would have created and
fixed it at the layer that owns the fact, and it kept the published labels -- which I verified by
a full run against a deliverable written three commits earlier rather than by reading
`_platform_label`. It declined to invent the other headings' loads and said so, which is the most
valuable output available at that moment and is CLAUDE.md's own sentence for it. It corrected its
own figure on the record for the fourth time and named the pattern instead of the instance.
**And it asked me to attack the fix rather than the feature, which is where three of my six
findings came from: the fix is right, and the two layers around it -- the node names above it and
the connectivity below it -- are where a declared topology still goes wrong.**


---

<!-- EARLIER ROUNDS, VERBATIM. Appended by scripts/write_verdict.py under
     DX2: each round is added and no prior round is rewritten or removed. -->

# Review — R1 step 3
Reviewed commit: d89566d09019dc3bb744c3ad21e859d268ca21de
**Reviewed commit: `d89566d09019dc3bb744c3ad21e859d268ca21de`.**
Verdict: PASS
Tests: 3553 passed, 89 failed, 1 skipped, 2 warnings in 974.92 s (0:16:14)   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK, the third in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **Nothing
blocks.** R860 is answered at the site its condition named, and I checked the refactor
against artifacts committed three commits before it rather than against the diff. Four
findings below, none blocking, plus the one ruling the implementer asked for by name (R855)
and an answer to the sequencing question taken from the hook's own text.

**I RULED UNDER FR1 WITH EZ0** (`docs/directives/FR.md:14-26`, `CLAUDE.md` section "What
blocks for the rest of R1"). For each finding I say the silently wrong result it would
produce, or that it produces none. **This file is HAND-WRITTEN because the one sanctioned
path in refuses it -- R856, third measured occurrence.**

```
cmd    git diff --name-status 948b36a..HEAD
out    M  floatfea/cli.py
       M  tests/regression/test_r1_example_regenerates.py
       -- two files, 67 insertions, 12 deletions, nothing else
cmd    git diff --stat 948b36a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff 948b36a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 948b36a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
cmd    git ls-files | grep -i conftest             -- the whole-tree census, since the ladder's
                                                     gate reads a record a rung's own conftest
                                                     could write (CH2/CI0)
out    tests/conftest.py
       tests/test_supervisor_conftest_pathspec.py  -- one conftest, at depth one, unchanged
cmd    git diff --stat 948b36a..HEAD -- results scripts docs
out    (empty)                                   -- no published deliverable moved
cmd    git status --porcelain
out    (empty)                                   -- clean before I ran anything and after
cmd    printf <the four mandatory sections, with the Verdict line first> |
         python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       -- R856 again, at scripts/write_verdict.py:181. I also measured the ORDER of its
          refusals, which no previous round did: a body that does not begin with the
          Verdict line is refused FIRST, so the no-report refusal is reached only by a
          well-formed verdict and the file cannot be written by accident.
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict.
The newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`) and
three verdicts are newer than it. That is EG3 state (2) by definition, and it is the whole
of this tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R860** (`_TIMING_STAGES` was a hand copy of the literal at `floatfea/cli.py:297` and nothing compared them) | **ANSWERED AT THE SITE THE CONDITION NAMED, and I verified both halves myself. It has a REMAINDER that "there is no second copy" misses -- R862.** | `floatfea/cli.py:37-43` defines `WALL_TIME_STAGES`, `:320` iterates it, `tests/regression/test_r1_example_regenerates.py:45` imports it. The provenance is structural rather than inferred from a green: `grep -n "WALL_TIME_STAGES\|for stage in" floatfea/cli.py` is two lines, `37` and `320`, and the gate has no tuple of its own left. I reproduced their red (a sixth name in the tuple -> `10 passed, 1 failed`, `EXCLUSION_pin ('the SHIPPED report', ['build','code_check','load','solve','total'])`) and their baseline (`11 passed`). **And the pin cannot fail false**, which I measured rather than inferring from the generator's defensive `if stage in result.timings`: `grep -rn "RunResult(" floatfea` is ONE construction (`pipeline.py:675`), all five `timings[...]` assignments above it are unconditional, and every branch between them RAISES rather than returning. |
| **R857** (the comparable counts were measured against the rule the same commit deleted) | **ANSWERED, and the figure is right at this commit by my own measurement rather than by taking theirs** | `tests/regression/test_r1_example_regenerates.py:99` now reads 97/1286/70 and the file records all three wrong versions. Mine, through the gate's own `_lines()`: report.md total 105 comparable 97 timing 5 prov 3; member_forces.csv 1289 / 1286 / 0 / 3; utilisation.csv 73 / 70 / 0 / 3. The published arithmetic 105 - 8 = 97 holds, and the two CSV figures are unmoved because neither carries a timing row. **The rule did not move in this commit** -- the tuple's five names and their order are unchanged -- so 97 is measured against the rule the file runs (BP0), and the third statement of this number is the first correct one. |
| **R858** (the file claimed both excluded classes were "checked separately") | **ANSWERED, and the replacement sentence is TRUE -- I measured it over all FIVE rows and not the two it names** | `:55-66`. Mine: `| load |`, `| code_check |`, `| solve |`, `| total |` and `| build |` each edited in the shipped report, one at a time, each through the real eleven cases -> **11 passed, 0 failed on every one of the five**. And the broad half of the sentence, which is the half I could have let pass on the file's own authority: `grep -rn "Wall time\|wall_time\|timings" --include=*.py tests` reaches exactly one assertion on a wall clock, `test_the_run_reports_a_wall_time_for_every_stage`, and it reads `result.timings` from a LIVE run and never a published file. **So "no test in this repository reads a published wall-clock VALUE" is true as written.** |
| **R859** (the new comment named the wrong assertion) | **HALF ANSWERED. The pin comment is corrected and I confirmed every clause of it. THE DOCSTRING OF THE SAME FUNCTION, WHICH R859's OWN JUDGE NAMED, IS UNTOUCHED AND STILL FALSE -- R865.** "Half of an item is not the item" is CLAUDE.md's own sentence, and I apply it to my predecessor's condition rather than to the implementer's reading of it. | Corrected at `:241-245`, each clause measured: a sixth unrecognised `| mesh |` row reddens REGENERATES[report.md] (16 line(s) differ, shipped has 98 comparable lines against 97) with the pin GREEN; a duplicate `| total |` reddens the pin; a deleted `| code_check |` reddens the pin. Untouched: `:228`, "a fourth non-deterministic line reaching the deliverable reddens here instead of being absorbed". |
| **R861** (the baseline of nine was wrong within one commit; the trace is a predicate and not a count) | **ANSWERED, and the implementer did the half I could not check -- it corrected the figure TO XABIER and not only here** | I applied the predicate rather than a number: **89 reds, all 89 inside tests/test_report_carried.py (79) and tests/test_report_guard_states.py (10)**; the 17 carries_the_finding cases parametrised on exactly R845-R861; the 57 named_site cases on sites of R850-R861; ten survives_the_state cases whose inner runs read 77 failed, 160 passed, 1 skipped (two read 78) and name those. **And my set and CI's set are the SAME SET**: comm -23 and comm -13 over the two sorted id lists are both empty, 89 against 89. |
| **R855** (the suite was not run at a pushed reviewed commit, third occurrence; the implementer asks me to rule it once rather than keep deciding it) | **WITHDRAWN FOR A COMMIT THAT CARRIES NO REPORT REVISION, with one standing condition. Ruled once, in its own section below.** | The condition is met in this commit: it names the runs it made and states plainly that it has NOT measured the whole suite at this sha. An unmeasured green would be a different matter, and that section says what I would do about one. |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- C43, and there is no report revision in which it could be answered** | FR1's third class. Unchanged by this diff. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot and a padded dot) | **still open, untouched, correctly so** | `git diff 948b36a..HEAD -- floatfea` is floatfea/cli.py alone, and its two hunks are the constant and its use. Non-blocking, ruled three times. |
| **R849 with R854** (the caveat, disclaimer, provenance AND regeneration gates quantify over hard-coded three-file tuples, and step 3 publishes two more deliverables) | **still open, both sites, and it is the oldest live item FL2 lands on** | NAMES at tests/regression/test_r1_example_regenerates.py:51; ARTIFACTS at tests/regression/test_r1_published_artifacts.py:69. Answered WHILE step 3 is built, as verdict 9 ruled and verdicts 10 and 11 repeated. **R862 is the same species in a third place**, which is the reason to do it once rather than file by file. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **with Xabier, relayed verbatim, unchanged by this diff** | not the implementer's to repair in code. |
| **R856** (write_verdict.py refuses a step with no report) | **with Xabier; THIRD measured occurrence, in my command block above, with its refusal ORDER measured for the first time** | apparatus, not ledgered (FF0); the exit is a clause and not a commit. |
| **R835, R836** (EG3's enumeration; and R836) | **still open, still Xabier's; this commit is the TENTH measurement and it over-lists again** | run on their own rather than read off a cascade, which is EJ2's discipline: the two off-list state-(2) names give **24 passed in 0.29s**. Two of the enumerated names are green while seven fire. Relayed unchanged. |
| **C29, C34, C35** (ruff, black, mypy) | **green at this commit, locally AND on a machine neither of us controls** | mine: All checks passed! / 148 files would be left unchanged / Success: no issues found in 43 source files. CI run 39176380750, job `lint, unit and guards`, read at STEP level: actionlint SUCCESS, ruff SUCCESS, black --check SUCCESS, mypy SUCCESS, unit tests SUCCESS (186 passed in 163.91s), guards and meta-tests FAILURE. Every one RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried -- and I nearly filed a false sibling to it** | the em dash in _PROVENANCE_PATH and in the three published provenance lines is `e2 80 94`, U+2014, in BOTH files. My terminal rendered it as a replacement character and I was one step from writing a mojibake finding against a published deliverable; the bytes refuted it. Recorded because "verify the reference" is my own guard and this is the round it caught me rather than the code. |
| **C43, C44, C45** | **C43 and C44 carry; C45 unchanged and still unpayable before step 3's report exists** | verdict 10's process note stands, with verdict 11's correction to its baseline figure. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer and not the list. |
| **EG3(ii): the verdict commit measured** | **DONE at the reviewed commit; the measurement AT the verdict commit is owed to the next revision, as always, because I run before I write** | the two report-guard files hold 89 of the suite's 89 reds and the two id sets are identical to CI's, so no red sits outside the boundary. |
| scripts/suite_count.py's own line + CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## The R855 ruling, said once

**The implementer asked me to rule it rather than let it be re-decided every commit, and
that is the right request. R855 IS WITHDRAWN FOR A COMMIT THAT CARRIES NO REPORT REVISION,
with one standing condition.**

```
claim  nothing in the governing documents puts the whole suite on an interim COMMIT; ES0
       puts it on the interim CHECK, and the check is mine
cmd    CLAUDE.md, ES0's third bullet
out    "An interim check is light: the suite and CI at the commit, plus a CZ0 (a)-(d) scan
        of the diff since the last verdict."
       -- the subject of that sentence is the check
cmd    CLAUDE.md, section Step gating, item 1 -- where the implementer's own run IS required
out    "Write docs/reports/F<n>/step-<k>.md: what was built, the test counts from your own
        run ..."
       -- the obligation attaches to a REPORT, and an interim commit has none by FR3's
          own design
cmd    EG3(i), the clause R855 was argued from
out    "The PRE-INVOCATION GREEN REQUIREMENT is waived only if EVERY red traces by name to
        the step-boundary cause."
       -- it waives a requirement stated elsewhere; it does not create one, and the tree it
          speaks of is red by construction for the whole of step 3
cell   what the double run has bought where both halves were measured: verdict 10 ran the
       suite at e818375 against an implementer who had run a 400-case subset, and verdict
       11 at e6a20e3 against one who had run a single file
out    9 reds and 78 reds; in both, the whole suite's set and the two report-guard files'
       set were THE SAME SET, so nothing was hiding in either, and the reviewer's run
       produced the number both times. This commit is the third: 89 and 89, same set.
judge  **the information is never lost, because I run the suite at the reviewed commit by
       rule and I have no discretion to skip it.** A second sixteen-minute run inside the
       same turn boundary reaches no reader the first does not, and the loop pays for it
       twice at every turn against a 5 November date. **What I am NOT withdrawing is the
       claim discipline, and it is the whole of the condition:** a commit that has not
       measured the suite SAYS SO, as this one does, and never states or implies a green it
       did not take. An unmeasured green is a different finding with a different name --
       it is a claim with no command (BF0) about the one measure this loop cannot
       re-derive -- and I would hold the next revision on one.
       R855 stands unchanged for a commit that CARRIES a report revision (item 1's own
       words) and for a closure commit (CZ1 (ii)). It is withdrawn for an interim commit,
       and it is withdrawn by me rather than argued down by the implementer, which is the
       part of the record that matters.
rule   ES0 as written; CLAUDE.md Step gating item 1; EG3(i); and my own instruction to run
       the suite myself and never to accept a pass count from a report
```

## The sequencing question, answered from the hook's own text

**The implementer's premise is false, and that is the whole answer: five commits in ONE
TURN is ONE interim check, not five.**

```
claim  the hook fires at a TURN BOUNDARY on a TREE COMPARISON and has no notion of how
       many commits reached that tree
cmd    .claude/hooks/require-verdict.sh, the only comparison in the file that can refuse a
       step commit
out    if ! git diff --quiet "$reviewed" -- "$report" floatfea tests
             ':(exclude)tests/corpus' 2>/dev/null; then
         block "floatfea/, tests/, or $report changed since the verdict at $reviewed."
       -- a diff between two TREES. There is no commit walk and no commit count anywhere
          in the file; I read all of it.
cmd    the directive the implementer read as pointing the other way
out    docs/directives/FR.md, FR3: "Build ALL of it before the first reviewed revision.
       Interim checks run as the hook requires and count against no round."
       -- "all of it before the first reviewed REVISION" constrains the revision, not the
          commit, and the sentence after it anticipates interim checks in the plural
judge  **commit granularity is yours and it costs you nothing either way.** The number of
       interim checks is the number of turn boundaries. **I would rather have the five
       commits than the one**, and the reason is not reviewability in the abstract: three
       of the last four rounds' findings came from running the model at a configuration the
       commit did not choose, and with five commits each item's own diff tells me which
       configuration its author chose. One undifferentiated diff adding member topology,
       two optional analyses with a re-solve loop, a headings list with a refusal and a
       per-case band check gives me one surface and an ES0 scope that is light by rule.
       **But if the build is naturally one turn, make it one turn and as many commits as
       the work has shapes.** I will not spend a round on either choice, and I am not
       asking you to change the plan.
```

## Findings

**NOTHING BLOCKS.** The diff is one `floatfea/` refactor with no behavioural change and one
test file's comments. No tolerance moved. No published deliverable moved -- and I
established that by regenerating all three from this tree, not by reading the diff. Under
FR1 none of the four findings below can put a wrong number in front of anyone **at this
commit**, and for the two that could at a later one I name the number and what makes it
live.

**THE IMPLEMENTER'S OWN REQUEST IS WHERE TWO OF THE FOUR CAME FROM.** It asked me to check
independently that the refactor changed no published figure -- "the one thing I would least
like to have got wrong". The answer is that **the claim is true and the measurement offered
for it cannot see the thing it claims** (R864), and that the refactor's remainder is in the
copy nobody looked at (R862).

**R862. (DOES NOT BLOCK -- ledgered) "THERE IS NO SECOND COPY" IS REFUTED BY ONE GREP.
THREE HAND COPIES OF THE STAGE SET REMAIN AND ONE OF THEM COMPUTES THE PUBLISHED
`| total |`. The commit unified the WRITER and the EXCLUSION and left the PRODUCER. At
FL2's shape the published total understates the run by 40.000 s with both gates green.**

```
claim  the stage set still exists in three places the new constant does not reach
cmd    grep -rn 'for stage in ("build"' --include=*.py . and
       grep -rn '("build", "load", "solve", "code_check")' --include=*.py .
out    tests/regression/test_r1_example_golden.py:318
         for stage in ("build", "load", "solve", "code_check", "total"):   <- FIVE, a copy
       tests/regression/test_r1_example_golden.py:321
         parts = sum(result.timings[s] for s in ("build","load","solve","code_check"))
       floatfea/run/pipeline.py:673
         timings[k] for k in ("build", "load", "solve", "code_check") if k in timings
       -- the last of these IS the published `| total |` row
cmd    what the golden gate claims, in its own failure message
out    "`total` is ... and its parts sum to ...; the reported total must be the sum of the
        stages, not a separate measurement."
cell   FL2's shape, one variable moved: a sixth timed stage at 40.0 s, pipeline.py:673
       untouched, the REAL test_the_run_reports_a_wall_time_for_every_stage called on it
out    TODAY (five stages)     PASSED   published total 97.273 s, real 97.273 s
       a SIXTH timed stage     PASSED   published total 97.273 s, real 137.273 s
                                        -> understated by 40.000 s, and the gate whose own
                                           message is "total must be the sum of the
                                           stages" is GREEN
cmd    why the five-name copy at :318 cannot see it either
out    it asserts PRESENCE (`stage in result.timings`) over its own list, so a stage ADDED
       to the set is outside the collection the assertion inspects, by construction
rule   my own recorded guard, verbatim -- check that the collection the assertion inspects
       can actually contain the failure; FR1's first head, a wrong number in a report
judge  **it does not block at this commit, and I measured that rather than asserting it.**
       `| total | 97.27 |` is correct today: the five published rows are
       0.19 + 0.00 + 97.08 + 0.00 = 97.27, `grep -n "timings\[" pipeline.py` is five lines
       of which one IS total, so the four summands are the only timed stages, and the
       full-precision identity is green. **The silently wrong result it produces, for the
       record, is a published `| total |` row that is labelled the total and is not** --
       and it arrives from ONE new `timings[...] = ...` line, whether or not the new row is
       published, with test_the_run_reports_a_wall_time_for_every_stage certifying it.
       That is R860's own argument one level down: R860 said a hand copy cannot know, and
       the repair unified the copy that decides the COMPARISON and left the copy that
       decides the NUMBER. **At the commit that adds a timed stage this is a wrong number
       in a published deliverable and it blocks then.**
```

**Closed when** `floatfea/run/pipeline.py:673` derives its summands from `WALL_TIME_STAGES`
rather than restating four of them, and the two literals at
`tests/regression/test_r1_example_golden.py:318` and `:321` come from the same place -- at
the latest in the commit that adds a timed stage.

**R863. (DOES NOT BLOCK -- ledgered; it is the EH4 direction the repair opened) THE
EXCLUSION SET IS NOW DEFINED BY THE CODE UNDER TEST, SO A SIXTH PUBLISHED ROW IS EXEMPTED
SILENTLY. Measured: a sixth stage published AND named is green on 11 of 11 -- green even
when the shipped value is 4521.30 against a fresh 0.00.**

```
claim  the repair moves the exclusion's declaration from a place a reviewer reads to a
       place the generator decides, and the widening then needs no test-file diff
cell   the real gate's eleven cases, fresh side held fixed at my own 70.37 s regeneration,
       PUBLISHED redirected to a copy so the committed artifacts were never written
out    BASELINE (unmodified, HEAD as committed)                      11 passed,  0 failed
       a SIXTH stage in the TUPLE ONLY (the implementer's cell)      10 passed,  1 failed
         FAILED EXCLUSION_pin ('the SHIPPED report', [the five])
       a sixth stage PUBLISHED and NAMED (FL2's shape)               11 passed,  0 failed
       ... and its published value DIFFERS from the fresh run
           (| sizing | 4521.30 | against a fresh | sizing | 0.00 |)  11 passed,  0 failed
       RESTORED                                                      11 passed,  0 failed
cmd    the two configurations side by side, which is the whole of the finding
out    BEFORE this commit: widening the exemption meant editing `_TIMING_STAGES` in
         tests/regression/test_r1_example_regenerates.py -- a diff in a test file.
       AFTER: it means adding the name to WALL_TIME_STAGES in floatfea/cli.py, which is the
         SAME one-line change that makes the row publishable at all. The exemption becomes
         a side effect of the publication.
cmd    the row shape the exclusion keys on
out    r"^\|\s*(build|load|solve|code_check|total)\s*\|\s*[0-9.]+\s*\|\s*$"
       -- a NAME and a number. Nothing in it says "a time", and nothing says "inside the
          Wall time table".
cmd    whether a non-time quantity can reach an exempted row today, read rather than assumed
out    floatfea/run/pipeline.py:605, 653, 664, 669, 672 -- every member of the tuple is a
       time.perf_counter() delta, and the branches between them raise rather than return
cmd    the direction that is CLOSED, measured before I claimed the one that is open
out    an engineering `| total | 4521.30 |` row elsewhere in report.md  9 passed, 2 failed
         FAILED REGENERATES[report.md] -- 14 line(s) differ, 102 against 97
         FAILED EXCLUSION_pin -- (... ['total','total'])   the duplicate is caught
rule   EH4 -- the boundary is solved in the direction that WEAKENS the gate, and the
       injection rises until a clean case trips; my own guard that a gate carries its own
       failure
judge  **it does not block, and the reason is a measurement rather than a judgement of
       severity.** Every member of the tuple is a wall clock on every admissible config, so
       no engineering number is reachable through this door today, and a second occurrence
       of any of the five is caught by the pin. **What is reachable with no signal at all
       is a sixth wall clock** -- the thing R860 was about, in the direction R860 did not
       look. The repair is still the right one: before it the gate was machine-dependent,
       which is worse. **But the exclusion is no longer DECLARED, it is DERIVED, and a
       derived exemption cannot be reviewed in the diff that widens it.** Neither close
       below is new apparatus: anchor the regex to the `## Wall time` section so that an
       exempted row is exempt for WHERE it is; or state in the report, with the two green
       rows above, that adding a name to WALL_TIME_STAGES exempts a published row from
       comparison with nothing red, and that this is accepted for a wall clock.
```

**Closed when** an exempted row is exempt by its position in the `## Wall time` table rather
than by its name matching a tuple the generator controls -- or the report states that
widening with those two measurements beside it.

**R864. (DOES NOT BLOCK -- ledgered, FR1's third class) "THE REFACTOR PRODUCES BYTE-IDENTICAL
DELIVERABLES" IS TRUE, AND THE REGENERATION GATE CANNOT SEE IT EITHER WAY. The five lines
the refactor touches are the five it excludes: reordered, or with every value replaced, the
comparable-line lists are IDENTICAL and the pin is GREEN.**

```
claim  the witness offered for the claim is blind to the claim's own subject
cell   the gate's own _lines() and pin applied to the shipped report and to two mutations
       of it, one variable moved each, nothing regenerated
out    REORDERED (| total | first)      comparable lines identical: True   pin green: True
       ALL FIVE VALUES -> 999.99        comparable lines identical: True   pin green: True
cmd    the five single-value edits through the real eleven cases
out    | load | -> 999.99        11 passed       | total | -> 0.01      11 passed
       | code_check | -> 999.99  11 passed       | build | -> 999.99    11 passed
       | solve | -> 0.01         11 passed
cmd    the cell that DOES isolate the claim, which is the diff and not a run
out    git diff 948b36a..HEAD -- floatfea/cli.py: the five names and their order are
       unchanged, `_write_report`'s loop body is unchanged, and `if stage in
       result.timings` is unchanged. **That is the evidence, and it is sufficient.**
cmd    the independent half, which is stronger than the diff and which the implementer did
       not claim
out    the three artifacts were last written at 129747b, THREE commits before this refactor
       (git log --oneline -1 -- results/R1/example/), and my regeneration from THIS tree
       differs from them on 0 of 97, 0 of 1286 and 0 of 70 comparable lines, at
       governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
       -- a writer refactored at d89566d reproducing files written at 129747b is the
          statement that wanted making
cmd    and the claim as WORDED, tested
out    the deliverable is NOT byte-identical and never was: my run published
       `| solve | 70.20 |` against the shipped `| solve | 97.08 |`. It is identical on
       every COMPARABLE line, which is a different and true sentence.
rule   BF0 with BG0 -- a causal sentence carries the cell that isolates it, one variable
       moved; and my own guard that a residual destroys information, applied to a gate that
       drops the very lines it is being asked about
judge  **it does not block**: the claim is true, nothing in the deliverable moved, and I
       verified it by two routes. It is recorded for its shape, which is this project's own
       recurring one -- **the measurement cited for a claim excluded the claim's subject by
       construction.** The same constant's docstring says it is "the stages the published
       report's table carries, IN ORDER", and the order of that table is the one property
       of it nothing in the tree checks, which is the first measurement above.
```

**Closed when** the step's report states the claim as "identical on every comparable line,
and the five excluded rows are not compared in either direction", with the regeneration
against `129747b`'s artifacts as its command -- or drops the claim and cites the diff, which
is what actually carries it.

**R865. (DOES NOT BLOCK -- ledgered; R859's THIRD SITE, the one R859's own judge named) THE
DOCSTRING OF THE FUNCTION WHOSE COMMENT WAS CORRECTED STILL SAYS "A FOURTH NON-DETERMINISTIC
LINE REACHING THE DELIVERABLE REDDENS HERE INSTEAD OF BEING ABSORBED", AND IT IS FALSE IN
BOTH HALVES. The line is not absorbed, and this assertion cannot see it.**

```
claim  the pin's second assertion cannot fail in the direction the docstring claims for it
cmd    tests/regression/test_r1_example_regenerates.py:224-229, untouched by this diff
out    "This pins the excluded set by KEY in both the shipped and the fresh report, so a
        fourth non-deterministic line reaching the deliverable reddens here instead of
        being absorbed."
cell   a fourth provenance key injected into the shipped report, one line, nothing else
out    `# npz: /home/someone-else/junk/other_cases.npz`
       matched by _PROVENANCE_PATH : False      -> it is NOT absorbed
       excluded from the comparison: False
       comparable lines 97 -> 99                -> the COMPARISON reddens, loudly
       the pin's key set                        -> ['config','deck','load_cases'], GREEN
cmd    why it can never be otherwise, from the regex rather than from the run
out    ^(?:#\s*|\*\s+\*\*)(config|deck|load_cases)(?:\*\*)?\s*[:<em-dash>-]\s*(.+?)\s*$
       -- `keys` is drawn from that three-way alternation, so
          assert keys == ["config","deck","load_cases"] can fail only by OMISSION. A
          fourth key is outside the collection the assertion inspects.
rule   my own guard -- check that the collection the assertion inspects can contain the
       failure; CW0 -- prose in the source tree is a test, a triple, or deleted
judge  **it does not block**: the behaviour is the safe one, the red is loud, and no number
       moves. It carries because R859's judge named this docstring explicitly -- "the
       pre-existing docstring of that test has the same shape" -- and the comment eight
       lines below it was corrected while this was not. **The sentence is wrong in the
       direction that makes the gate sound stronger**, which is the direction R853, R857
       and R859 were each wrong in, in this same file, in three consecutive commits.
```

**Closed when** that docstring says which assertion fires for a fourth excluded line -- the
comparison, not the pin -- and says that the key assertion bounds omission only; or says
nothing and lets the five test functions speak.

## Try to break it -- what I ran, and what it found

* **One full regeneration of all three deliverables from this tree into a temporary
  directory**, with the fixture's own recipe: 70.37 s, `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)`, **0 differing comparable lines
  in all three files** at 97 / 1286 / 70. That is the control for everything below and the
  independent answer to the one thing the implementer asked me to check -- and it is a
  stronger answer than the diff, because the committed artifacts were written at `129747b`,
  three commits before this refactor.
* **Sixteen injections against the five real test functions**, fresh side held fixed, one
  edit each, with the gate's `PUBLISHED` root redirected to a copy so the committed
  artifacts were never written: baseline; a sixth stage in the tuple only; a sixth stage
  published and named; the same with a value differing by 4521.30 from the fresh run; an
  engineering `| total |` row elsewhere in the report; all five wall-clock values one at a
  time; the governing U; a duplicate `| total |`; a deleted `| code_check |`; a sixth
  unrecognised `| mesh |` row; a timing row in a CSV; and a restore.
  **Each of the gate's five functions was shown to carry its own failure by at least one
  red, and every injection was red somewhere except the rows the exclusion tolerates by
  design -- which is R863, and it now includes a sixth row nobody has published yet.**
* **Both EH4 directions on the thing the diff changed.** Strengthening: the pin requires
  exactly five rows, and I showed it cannot fail false by reading `pipeline.py` --
  `grep -rn "RunResult(" floatfea` is one construction, all five `timings[...]` are
  unconditional above it, and the branches between them raise rather than return.
  Weakening: the exclusion's membership now comes from the code under test (R863).
* **The gate's blindness to its own excluded rows, solved in the two directions the diff
  did not choose**: the five rows reordered, and all five values replaced -- identical
  comparable lines and a green pin in both. That is R864, and it is what makes the
  implementer's byte-identity claim true-but-unwitnessed rather than wrong.
* **A census of the stage set rather than a reading of the diff**, which is what found
  R862: three hand copies remain and one of them computes the published `| total |`. Then
  the FL2 cell on the real golden gate: a sixth timed stage, the published total 40.000 s
  short, and the gate that asserts the sum GREEN.
* **The fourth-provenance-key direction** of the pin, from the regex rather than from a
  run: the key assertion can fail only by omission (R865).
* **The 89 reds one id at a time**, with the cascade identified by its inner FAILED lists
  and by `[baseline]` being red rather than by its names, and the two off-list state-(2)
  names run on their own (24 passed).
* **The bytes of the one thing I was about to get wrong.** My terminal rendered the em dash
  in `_PROVENANCE_PATH` and in the three published provenance lines as a replacement
  character, and I was one command from filing a mojibake finding against a published
  deliverable. `e2 80 94` in both files. Recorded under C42.

**What I did not find, and it is the larger part.** The repair does what R860's condition
asked and the provenance is structural rather than inferred from a green: one definition in
`floatfea/cli.py`, one import, no tuple left in the test. The deliverables are unmoved and I
proved it against artifacts written three commits earlier rather than by reading the diff.
The pin's new strictness cannot fail false on any admissible config. R857's figure is right
at the third attempt and the file records all three versions, which is the behaviour BP0
wants and is rarer than it should be. R858's replacement sentence is true in the broad form
and not only in the two rows it names -- I checked the broad form. **All four of my findings
are in a copy, a derivation, a witness or a sentence; not one of them is a number in a gate
or in a deliverable at this commit.**

## CI at the reviewed commit: RED, 89 reds, ALL 89 traced to EG3 state (2)

```
cmd    gh run list --commit d89566d09019dc3bb744c3ad21e859d268ca21de
         --json conclusion,status,databaseId,workflowName
out    [{"conclusion":"failure","databaseId":39176380750,"status":"completed",
         "workflowName":"CI"}]
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is
          not a pass and I did not record one. The judged commit had a run because it was
          pushed first (FP1).
cmd    gh run view 39176380750 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         run_rung: ladder 1  1276 collected, 0 failed, 0 errored, 0 skipped
                   ladder 2    66 / ladder 3   314 / ladder 6   225 /
                   ladder 4   343 / ladder 5    87      -- all OK, all 0 failed
         -- 225 at e6a20e3 and 225 here, which is right: this commit adds no case
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 163.91s) /
         guards and meta-tests FAILURE (89 failed, 1056 passed, 1 skipped, 1 warning
                                        in 711.21s)
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39176380750 --log-failed, unique ids, matched against state (2)'s list
out    57  test_every_named_site_is_touched_or_declared[R850..R861-<site>]  -> state (2)
       17  test_the_report_carries_the_finding[R845..R861]                  -> state (2)
        1  test_the_CI_section_is_about_the_REVIEWED_commit                 -> state (2)
        1  test_the_Carried_table_is_what_the_generator_produces            -> state (2)
        1  test_the_generator_would_catch_a_row_under_the_wrong_number      -> state (2)
        1  test_the_report_carries_a_WHOLE_SUITE_count                      -> FC1
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                   -> FC1
       10  test_the_guard_survives_the_state[baseline + 9]                  -> the cascade
       --- 57 + 17 + 1 + 1 + 1 + 1 + 1 + 10 = 89 exactly, with no remainder
cmd    the control that makes the trace a measurement rather than a classification: my own
       89 sorted against CI's 89, both directions
out    comm -23 (mine) (CI's)   (empty)
       comm -13 (mine) (CI's)   (empty)
       -- the SAME SET, id for id, on two machines and two operating systems
cmd    the cascade identified by its own failure lines rather than by its names (EH1)
out    each inner run reads "77 failed, 160 passed, 1 skipped" (two read 78) and names the
       report-guard ids above; the [baseline] state is red, which is EH1's other half
cmd    the two state-(2) names that did NOT fire, run on their own (EJ2, R835)
out    test_the_answered_verdict_is_the_NEWEST_one and
       test_a_carried_row_points_at_a_section_that_discusses_it  -> 24 passed in 0.29s
cmd    the one warning, traced rather than left as a count
out    numpy/linalg/_linalg.py:2784 RuntimeWarning: overflow encountered in dot, raised by
       tests/verification/rung1/test_corpus_configurations.py::
         test_the_corpus_entry_behaves_as_the_reviewer_recorded[orient_norm_overflow]
       -- a reviewer corpus entry whose whole purpose is to overflow a norm. Designed.
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with EH1, EJ2 and FC1; EG3(i) -- EVERY red traces
       by name or it is CZ1 (iv) unchanged
judge  **all 89 trace, and the waiver applies in full: CZ0 (d) / FR1's red-test head does
       not stand and CA2's HOLD is not reached.** The predicate, not a count (R861): every
       red is in one of the two report-guard files, and each names a finding or a site of
       the newest verdict or is a survives_the_state case whose inner list names those.
       Both FC1 reds are unclearable before step 3's report exists. Every step in the lint
       job RAN rather than being skipped behind an earlier red, which is what CZ1 (iii)
       exists to see, and mypy is green there, so the CI-only types-PyYAML red FP1 found
       has stayed fixed.
```

**Not CK2's exhausted-allowance state.** `runnerName` is null for all four jobs including
the two that SUCCEEDED, so an empty runner name cannot separate the states in this
repository and I did not use it. What separates them: both real jobs carry per-step
conclusions, real counts and five- and fifteen-minute durations (23:24:27Z -> 23:29:11Z and
23:24:28Z -> 23:39:46Z), and the two skipped jobs are the determinism workflow's own event
gate (CK0) with empty step lists at a zero-second duration, which arises from a designed
`if:` and not from an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree
was clean before and after I wrote this file.** Neither exception opens: this diff touches
no part of F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre
labels in `tests/verification/rung4/`, not about a wall-clock table. The last corpus commit
remains `ba1527e` (batch 47).

**I ran the recorded substitute, and both halves paid again:**

* **A regeneration check on a published deliverable, in both directions** -- all three R1
  artifacts regenerated from this tree and diffed line for line (0 differing at 97 / 1286 /
  70), then sixteen injections against the gate that guards them, plus the two mutations
  the diff did not choose (reorder, and all five values). It produced **R863 and R864**.
* **A continuum grid over the parameter space the decision rule guards** -- the stage-set
  axis this time, since that is the axis the diff moved: the set's SOURCE (restated vs
  imported), its SIZE (five, six-in-tuple-only, six-published-and-named), the value axis
  (`0.00`, `0.01`, `999.99`, `1234.00`, `4521.30`), the position axis (inside the table,
  elsewhere in the report, in a CSV), and the order axis. It produced **R862**, from the
  one point on the source axis nobody swept: the copies that are not the gate's.

**This is the seventh consecutive round in which the regeneration check's weakening
direction produced the round's findings.**

## Tolerances touched

**None.** No value, no form, no counter, no injection -- and I treated the EXCLUSION as a
tolerance under another name and ran EU1's adversarial case anyway.

```
cmd    git diff 948b36a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 948b36a..HEAD | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance|slack|epsilon"
out    "tolerance because the rows are two-decimal, and that is a threshold this gate has
        no business introducing."   -- an unchanged line moved by context, recording a
        DECLINED threshold. No value is introduced.
claim  the one thing in this diff that functions as a tolerance under another name is the
       EXCLUSION, and its FORM moved even though no value did
cmd    the form, before and after
out    before: a tuple DECLARED in the test file
       after:  the same five names IMPORTED from the code under test
rule   CLAUDE.md section Tolerances, its clause on anything that functions as a tolerance
       under another name; EU1 -- an interim check whose diff moves a value or a declared
       counter includes the adversarial case, the model run at a configuration the diff did
       not choose
judge  **EU1 does not attach by its own words** -- no value and no declared counter moves --
       **and I ran it anyway, because R694's lesson is that a value which does not move is
       the worst case and not the safest.** The configuration the diff did not choose is a
       sixth stage published and named, and it is R863: eleven of eleven green with a
       published value 4521.30 away from the fresh one. The diff's own cell chose the
       tuple-only case, which reddens. **A form change with no value change is exactly the
       shape EU1 was earned on**, and it is why I ran the model at three stage-set sizes
       rather than reading the grep.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line, deliberately).** Step 3 remains open with all three reviewed revisions available.
Nothing blocks, so FR3's instruction stands and it is the only thing that matters this
week: **build the rest of FL2.**

1. **FL2, complete, before step 3's first reviewed revision (FR3).** Five items, none
   built: member topology from the config with the star as the default; `required_section`
   and `truss_sizing` in `floatfea run` with FM0's re-solve loop; the optional analyses off
   by default; headings as a list with the BEM refusal; the band check per case with
   out-of-band cases unable to govern. **This is the third commit of step 3 and all three
   have been spent on gate items the plan routes to the ledger.** I am recording the
   arithmetic and not a fault: FR0's date is 5 November, eighteen days out, five items.
2. **R862 IN THE COMMIT THAT ADDS A TIMED STAGE, not after it.** It is the one of my four
   that becomes a wrong number in a published deliverable, and `truss_sizing` with a
   re-solve loop is the thing that adds the stage. One derivation at
   `floatfea/run/pipeline.py:673`, and the two literals in
   `tests/regression/test_r1_example_golden.py` with it.
3. **R849 with R854, over TWO files, still answered WHILE step 3 is built**, and R862 makes
   it three places where the same set is restated. Two new deliverables are coming.
4. **R863, R864, R865 in the first reviewed revision**, each with its figure regenerated at
   that commit (CP3). R847, R848 unchanged; R850 is half paid and R851, R853, R857, R858
   are paid; R859 is paid at two of its three sites.
5. **R852 and R856 remain with Xabier**, relayed correctly this turn, and R835's tenth
   measurement with them. Neither R852 nor R856 is the implementer's to repair in code.
6. **R855 is withdrawn for interim commits, with the condition in its own section.** The
   whole-suite number at a reviewed commit is mine to produce, and I have produced it at
   all three commits of this step. A commit that has not measured it says so.
7. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 89
   reds identical to mine id for id on a different operating system, and all six ladder
   rungs green with rung 6 at the same 225 collected as before -- which is the right
   number for a commit that adds no case.
8. **The schedule.** FR0's 5 November stands and nothing has slipped against it yet. Step 3
   opened on 18 October; three commits in, FL2 is unbuilt by design under FR3. I am not
   re-opening the escalation FR0 answered. **The next progress statement is step 3's first
   reviewed revision (FR5), and the sequencing answer above says that revision may arrive
   on as many commits as the work has shapes, in one turn.**

**What this commit got right, and it is much the larger part.** It took R860 before FL2
rather than after, which was the whole reason the previous verdict named it, and it took it
in the form that removes a copy rather than the form that adds an assertion -- one
definition, one import, no tuple left in the test. It corrected a figure that had been wrong
twice and **recorded both wrong versions and why each was wrong**, which is what BP0 asks
for and what nothing in this repository would otherwise do. It replaced a false sentence
about the wall clock with a true one, and the true one is true in the broad form I tested
and not only in the two rows it cites. It corrected its own mechanism sentence to the
assertion that actually fires. **And it asked me to check the one thing it least wanted to
have got wrong, which is how two of my four findings exist**: the byte-identity claim is
true, its witness is blind, and the copy that decides the published number was never in the
diff.

---

<!-- EARLIER ROUNDS, VERBATIM. Hand-appended in the form
     scripts/write_verdict.py uses, under DX2: each round is added and no prior
     round is rewritten or removed. The tool refused this step (R856). -->

# Review — R1 step 3
Reviewed commit: e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
**Reviewed commit: `e6a20e330fa1afc91fdc32b3d4eb3292f45898a2`.**
Verdict: PASS
Tests: 3547 passed, 78 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK, the second in step 3.** No report revision exists for step 3, so
this counts against no round and all three reviewed revisions remain available. **Nothing
blocks.** Three of the four gate findings verdict 10 ledgered are repaired, and I verified each
by my own injections rather than by reading theirs; five findings below, none blocking.

**I RULED UNDER FR1 WITH EZ0** (`CLAUDE.md` section "What blocks for the rest of R1",
`docs/directives/FR.md`). For each finding I say the silently wrong result it would produce, or
that it produces none. **This file is HAND-WRITTEN because the one sanctioned path in refused it
again -- R856, second occurrence, measured below.**

```
cmd    git diff --name-status 0aa0c4a..HEAD
out    M  tests/regression/test_r1_example_regenerates.py
       -- one file, 68 insertions, 5 deletions, nothing else
cmd    git diff --stat 0aa0c4a..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff 0aa0c4a..HEAD -- floatfea
out    (empty)                                   -- FR1 head (a) is unreachable from this diff
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
cmd    git diff 0aa0c4a..HEAD -- results scripts docs
out    (empty)                                   -- no published deliverable moved
cmd    printf <the four mandatory sections> | python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1                                    -- R856, unchanged and unchangeable here
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report, so
there is no `Answers: verdict N @ <sha>` header to compare against the newest verdict. The
newest revision in the tree is still step 2's third (`Answers: verdict 8 @ a7b2f62`), and two
verdicts are newer than it. That is EG3 state (2) by definition, and it is the whole of this
tree's red.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R850** (the wall-clock exclusion covered three of the five rows the generator writes; and no check reads a published wall-clock value) | **HALF ANSWERED. The five-stage half is repaired and I verified it in both EH4 directions. THE PROSE HALF IS UNTOUCHED AND STILL FALSE -- see R858.** My closing condition named two things, and "half of an item is not the item" is CLAUDE.md's own sentence. | Repaired: `_TIMING_STAGES` feeds both the regex and the pin, so those two cannot drift apart. Verified by me: `| load |` and `| code_check |` set to `999.99` are now green (both were inside the byte comparison before); a DUPLICATE `| total | 1234.00 |` row reddens the pin; a MISSING `| code_check |` row reddens the pin; a timing-shaped row reaching a CSV reddens `test_R845_the_CSVs_carry_NO_excluded_timing_row`. **So the widening is bounded in all three files, which is the question the implementer asked me.** Still open: the claim that both excluded classes "ARE CHECKED SEPARATELY", while nothing in the tree reads a published wall-clock value. |
| **R851** (`_provenance` returned a dict so a duplicate `# deck:` line collapsed; the key-set pin read `report.md` alone) | **ANSWERED, and I reproduced my own exact injection against the repair rather than taking its counter-cases** | `_provenance_lines` and `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the same file. My verdict-10 injection -- a second `# deck:` line with the SAME basename and a different directory, green before -- now reddens, in utilisation.csv and in report.md, **and reddens exactly one case** (the new one), which is the measurement that says the repair and not something else caught it. Two evasions I had not tried are caught as well, by different tests: `# Deck:` (capital, unmatched by the exclusion) falls into the byte comparison; `#deck:` with no space is caught by the new test AND by the basename test. The FRESH half of the new test is live -- injecting into the regenerated side alone reddens it. |
| **R853** (the published "102, 1289 and 73 comparable lines" did not reproduce) | **ANSWERED IN FORM, WRONG IN SUBSTANCE -- the corrected figure is correct against the rule the SAME COMMIT deleted. See R857.** | The commit took my 99/1286/70 and published it while widening the exclusion from three stage rows to five, which makes the report's comparable count 97. BP0 names this exactly: when a decision rule changes, every figure citing the old rule is regenerated in the same commit. |
| **R852** (a caveat truncated to its own marker is green on 31 of 31) | **relayed to Xabier by the implementer, correctly, and unchanged by this diff** | Mine, not the implementer's to repair in code. No new measurement this round. |
| **R856** (`write_verdict.py` refuses a step with no report) | **relayed to Xabier, and this is its SECOND measured occurrence** | the refusal is in my command block above. Under FF0 it is apparatus and not ledgered; the exit remains a clause, not a commit. |
| **R855** (the suite was not run at a pushed reviewed commit, and the tree's reds were not recorded with their cause named) | **STILL OPEN, third commit running. The implementer ran one file and asked whether the light scope requires the full run. IT DOES. I ran it: 78 failed, 3547 passed, 1 skipped in 966.33 s, every red traced below one id at a time.** | The offer to produce it rather than argue the scope is the right instinct and I am recording that; the answer is that ES0's light scope is the suite, and EG3(i) makes the waiver conditional on a trace that is pasted. **And the baseline I gave for that trace was wrong within one commit -- R861.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- C43, and there is no report revision in which it could be answered** | FR1's third class. Unchanged by this diff. |
| **R848** (the empty-directory refusal admits a bare dot, a dot-slash, a double dot and a padded dot) | **still open, untouched, correctly so** | `git diff 0aa0c4a..HEAD -- floatfea` is empty. Non-blocking, same class as R843. |
| **R849 with R854** (the caveat, disclaimer, provenance AND regeneration gates quantify over hard-coded three-file tuples, and step 3 publishes two more files) | **still open, both sites, and now with a second reason to be done before FL2 lands** | the two constants are `NAMES` in the regeneration gate and `ARTIFACTS` in the published-artifacts gate. Answered WHILE step 3 is built, as verdict 9 ruled. R860 below gives the same item its sharper reason. |
| **R835, R836** (EG3's enumeration; and R836) | **still open, still Xabier's; this commit is the ninth measurement of the enumeration** | and it over-lists again: of state (2)'s enumerated names, seven fire and two (`test_the_answered_verdict_is_the_NEWEST_one`, `test_a_carried_row_points_at_a_section_that_discusses_it`) are green. Relayed unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, locally AND on a machine neither of us controls** | mine: `ruff` `All checks passed!`; `black` `148 files would be left unchanged`; `mypy` `Success: no issues found in 43 source files`. CI run 39173178232, job `lint, unit and guards`, step level: `actionlint` SUCCESS, `ruff` SUCCESS, `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 164.24s`). Every one RAN rather than being skipped behind an earlier red. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired here. |
| **C43, C44, C45** | **C43 and C44 carry; C45 is unchanged and still unpayable before step 3's report exists** | see verdict 10's process note, which stands except for its baseline figure (R861). |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| **The R850/R851/R853 ROUTING QUESTION the implementer asked me to check** | **ANSWERED: half right. EK2 governs the FORM of a repair and these repairs honour it; it is not a route that pre-empts the ledger, and FF0 does not reach this file.** | See the routing ruling below. No repair has to be undone. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files at e6a20e3: **78 failed, 165 passed, 1 skipped**, which is the same 78 as the whole suite's and the same 78 as CI's, id for id. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed and still structurally unpayable until step 3's report exists** | not a finding against the implementer. |

## The routing ruling

**The implementer asked for the classification to be checked as hard as the repairs, so it is
checked here and not glossed.** The answer is that it is half right, and nothing has to be
undone.

```
claim  EK2 is a constraint on the FORM of a repair, not a route that pre-empts the ledger
cmd    CLAUDE.md, the clause EK2 is cited from
out    "No new apparatus through F6. ... An existing guard that fails false is fixed or
        deleted, never extended."
       -- it says what a repair may be. It says nothing about when, or about the ledger.
claim  FF0's route does not reach this file
cmd    CLAUDE.md section "What blocks, and what is a closure item (CZ0)", the FF0 paragraph
out    "Anything that reads the gating record, or decides whether a green is believed -- the
        report guards, scripts/ci_section.py, scripts/suite_count.py, .claude/hooks/, the EG3
        lists -- is fixed in the next commit."
       -- tests/regression/test_r1_example_regenerates.py decides whether a PUBLISHED
          DELIVERABLE is believed. It reads no gating record and no green. Not FF0's class.
claim  the locked plan routes a non-blocking interim finding to the ledger, by name
cmd    docs/milestones/R1.md, step 3's paragraph
out    "Only FR1-blocking items from those checks are fixed in flight; everything else is
        ledgered. That ordering is the directive's answer to the measurement both reviewers
        reached independently -- the repairs were one line each and the rounds were the cost."
rule   FR1 -- R850, R851 and R853 were each ruled NON-blocking in verdict 10, so the plan's
       sentence routes all three to the ledger
judge  **the repairs are sound and I would rather have them than not; the route was the
       ledger.** Three consequences, and they are bookkeeping rather than rework. (i) EK2's
       form is honoured and conspicuously so: the set is NAMED rather than the comparison
       given slack, and the 0.02 tolerance I proposed against myself was declined -- that is
       the right call and it is the opposite of widening. (ii) R850, R851 and R853 stay on the
       R1 ledger as PAID EARLY, R850 as HALF paid, so the closure list does not lose them.
       (iii) The cost is the one the plan's sentence predicts: this is the second commit of
       step 3, and FL2 has five items with none of them built, against FR0's 5 November. The
       implementer says so plainly and claims none of it, which is the correct thing to have
       done; I am recording the arithmetic rather than a fault.
```

## Findings

**NOTHING BLOCKS.** The diff is one test file. No `floatfea/` line moved, no tolerance moved,
no published deliverable moved -- and I established the last of those by regenerating all three
artifacts twice rather than by reading the diff. Under FR1 none of the five findings below can
put a wrong number in front of anyone, and I say which for each.

**R857. (DOES NOT BLOCK -- ledgered) R853'S REPAIR REPUBLISHED R853'S DEFECT. The corrected
figure `99, 1286 and 70 COMPARABLE lines` in the exclusion comment was measured against the
THREE-stage exclusion that THIS COMMIT deleted. Under the shipped five-stage rule the report's
comparable count is 97. The two CSV figures are right.**

```
claim  the figure the file publishes as "the measurement that says the numbers are reproduced"
       is not a measurement of the rule the file now runs
cmd    the gate's own `_lines()` applied to the three shipped files, at this commit
out    report.md          total  105   comparable  97   timing-excluded 5   prov-excluded 3
       member_forces.csv  total 1289   comparable 1286  timing-excluded 0   prov-excluded 3
       utilisation.csv    total   73   comparable  70   timing-excluded 0   prov-excluded 3
cmd    the same three files under the regex this commit DELETED, (build|solve|total)
out    report.md 99, member_forces.csv 1286, utilisation.csv 70
       -- 99 is exactly the old rule's answer, which is where the published figure came from
cell   one variable moved and nothing else: the same `_PROVENANCE_PATH`, the same three files,
       the same `_lines`, the stage tuple three names versus five
out    99 -> 97 on report.md, 1286 -> 1286, 70 -> 70
cmd    what the gate's own failure message prints when it reddens, so the contradiction is
       inside the file rather than inferred
out    "report.md is not what this tree regenerates: 1 line(s) differ, shipped has 97
        comparable lines against 97"   -- from my injection of U = 0.99999
rule   BP0 -- when a decision rule changes, every figure citing the old rule is regenerated or
       withdrawn IN THE SAME COMMIT; CP2 -- a repair carries no new numeric claim outside a
       triple; and my own recorded guard that a reference is verified independently of the
       thing it measures
judge  **it does not block.** 97 against 99 is a claim about the gate's reach, not a number in
       a gate, a CSV, a report or a published deliverable: nothing asserts on it, and a reader
       of a RED is told 97 by the assertion message itself. No silently wrong result follows,
       so it is FR1's third class. **It is recorded because of what it is an instance of.**
       R853 was "a figure that is the total minus the wrong exclusion"; its repair is "a figure
       measured against the exclusion the same commit replaced". The attention went to the
       thing being fixed and the number written around the fix inherited none of the discipline
       being applied to it -- which is CP2's own sentence, and CZ0's: the highest-value finding
       in two of this project's rounds was a defect inside the repair of the previous finding.
```

**Closed when** the comparable counts in that comment are those of the rule the file actually
runs -- 97, 1286, 70 -- regenerated at the commit that publishes them (CP3), or the figure is
withdrawn and the claim left qualitative.

**R858. (DOES NOT BLOCK -- ledgered; it is the OPEN HALF of R850) THE FILE STILL ASSERTS THAT
BOTH EXCLUDED CLASSES "ARE CHECKED SEPARATELY", AND NOTHING IN THE TREE READS A PUBLISHED
WALL-CLOCK VALUE. The repair made that sentence LESS true, not more: the exclusion went from
three tolerated rows to five.**

```
claim  the file's own declared discipline is false for one of its two excluded classes
cmd    the header comment of tests/regression/test_r1_example_regenerates.py, first paragraph
out    "TWO DECLARED CLASSES OF LINE ARE EXCLUDED FROM THE BYTE COMPARISON, AND BOTH ARE
        CHECKED SEPARATELY. An excluded line is a line nothing checks unless something else
        checks it."
cell   my injections against the real gate's five test functions, the fresh side held fixed at
       my own 68.82 s regeneration, one edit each
out    CONTROL unmodified                                11 passed,  0 failed
       | load | 0.00 |       -> | load | 999.99 |        11 passed,  0 failed   <- GREEN
       | code_check | 0.00 | -> | code_check | 999.99 |  11 passed,  0 failed   <- GREEN
       -- before this commit both of these were COMPARED. The repair is right and the
          sentence describing it is now wrong about five rows instead of three.
cmd    whether anything anywhere reads a published wall-clock value
out    nothing. The provenance class has `test_R845_the_PROVENANCE_values_agree_by_BASENAME`
       and, since this commit, `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE`. The
       wall-clock class has no counterpart, by design and correctly -- I proposed the sum
       identity against myself in verdict 10 and withdrew it, and the commit records that
       withdrawal in the same comment, which is the right thing to have written down.
rule   CW0 -- prose in the source tree is a test, a triple, or deleted; and the closing
       condition of R850, which named this site
judge  **it does not block**: a wall-clock second is not a number anyone sizes steel against,
       and FR1's third class covers the sentence. It carries because R850's closing condition
       named two things and one of them was done. The repair I asked for is five words -- the
       wall-clock VALUES are excluded and unchecked -- plus the observation that the pin and
       `test_R845_the_CSVs_carry_NO_excluded_timing_row` bound WHERE they may appear rather
       than WHAT they say. That is the honest description of a structure that is, in fact,
       honest, and I measured its bound in both directions.
```

**Closed when** that paragraph says of the wall-clock class what the two green rows above say,
and the commit message's "BOTH are checked elsewhere rather than merely dropped" is corrected
with it.

**R859. (DOES NOT BLOCK -- ledgered) THE NEW COMMENT NAMES THE WRONG ASSERTION. It says a sixth
stage row "reddens HERE rather than being absorbed", where HERE is the key-set pin. It reddens
the byte comparison; the pin stays green. The pin catches a DUPLICATE of a named stage and a
MISSING one -- which it does, and that is the stronger property.**

```
claim  the mechanism sentence attached to the repair is not the mechanism
cmd    the comment above the pin's `assert stages == sorted(_TIMING_STAGES)`
out    "ALL FIVE STAGES `cli.py` WRITES (R850), so a sixth reddens here rather than being
        absorbed, and so `load` and `code_check` stop sitting inside the byte comparison"
cell   one injection at a time into the shipped report, every other input held
out    | mesh | 3.00 | added                     10 passed, 1 failed
         FAILED REGENERATES[report.md]: "16 line(s) differ, shipped has 98 comparable lines
         against 97"                            -- the COMPARISON, and the pin is GREEN
       | total | 1.2e3 | added                   10 passed, 1 failed
         FAILED REGENERATES[report.md]          -- scientific notation is unmatched by the
                                                   digit-and-dot class, so it is compared,
                                                   which is the safe direction
       a DUPLICATE | total | 1234.00 | row       10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', [... 'total', 'total'])   <- THE PIN
       the | code_check | row DELETED            10 passed, 1 failed
         FAILED EXCLUSION_pin: ('the SHIPPED report', ['build','load','solve','total'])
       | total | 5.00 | added to utilisation.csv 10 passed, 1 failed
         FAILED CSVs_NO_timing_row: "shipped utilisation.csv carries a timing row"
rule   BG0 -- a causal sentence carries the cell that isolates it; CW0; and my own recorded
       guard that a gate carries its own failure, asked of each of the five functions
judge  **it does not block** -- no number moves, and every one of those injections is red
       somewhere, so the gate is sound and only its description is wrong. The same error is in
       the report I was given ("a | mesh | row added -- a SIXTH row reddens the pin"), and the
       pre-existing docstring of that test has the same shape ("a fourth non-deterministic
       line ... reddens here"). **What the measurement shows is better than the claim**: a
       stage row can only be swallowed if it is one of exactly five names, in report.md,
       exactly once each -- a duplicate reddens the pin, a missing one reddens the pin, a sixth
       name reddens the comparison, and one in a CSV reddens the CSV test. That is the answer
       to "is the exclusion now too wide": **five tolerated rows, in one file, pinned by name
       and by count -- and the | mesh | case was not what bounded it.**
```

**Closed when** those two comments say which assertion fires for which class of intrusion, or
say nothing and let the five test functions speak.

**R860. (DOES NOT BLOCK -- ledgered, and it is the one of the five that step 3 is about to walk
into) `_TIMING_STAGES` IS A HAND COPY OF THE LITERAL TUPLE AT `floatfea/cli.py:297`, AND NOTHING
COMPARES THEM. R850 WAS THAT DRIFT. The repair removes the drift between the regex and the pin
and leaves the drift that caused it.**

```
claim  the repaired gate restates the generator's stage set in a second place instead of
       reading it from the one place it is defined
cmd    grep -rn "_TIMING_STAGES" --include=*.py .
out    tests/regression/test_r1_example_regenerates.py -- three hits: the tuple, the regex and
       the pin. All in the test file; nothing reads cli.py and nothing asserts equality.
cmd    the generator's own definition
out    floatfea/cli.py:297   for stage in ("build", "load", "solve", "code_check", "total"):
       -- a literal inside a function body; grep for a module-level STAGE constant in
          floatfea/ returns nothing
cmd    the sentence this leaves unchecked, which is a claim about the code in a comment
out    "floatfea/cli.py:297 writes build, load, solve, code_check, total."
       -- true today; nothing in the tree would notice it becoming false
cmd    whether the pin's new strictness can fail false instead, which is the direction that
       worried me more -- the generator guards its own loop with `if stage in result.timings`,
       so it contemplates a missing stage
out    floatfea/run/pipeline.py:605, 653, 664, 669, 672 -- all five assignments are
       unconditional on any run that returns a RunResult, and `_utilisations` is called
       unconditionally just above the code_check stamp. **So requiring all five rows cannot
       fail false on an admissible config today**, and I measured that rather than inferring it
       from the defensive guard.
rule   my own recorded guard -- provenance, not existence: that a value reaches the assertion
       through the thing that defines it is asserted structurally, not inferred from a passing
       test; EK2 -- a guard that fails false is fixed, and this is that fix one level up
judge  **it does not block.** The failure mode is a FALSE RED, which is loud, and the five
       names agree today -- CI's ladder 6 went 222 -> 225 collected with 0 failed, so the
       repair is green on a machine neither of us controls. **It carries because step 3 is the
       commit that makes it live.** FL2 adds `required_section` and `truss_sizing` to
       `floatfea run` with FM0's re-solve LOOP; a sizing loop that times itself adds a sixth
       stage to `result.timings` and a sixth row to that table, and the next sub-10-ms
       two-decimal row inside the byte comparison is R850 verbatim, in the step whose own gate
       is the thing that adds it. Two cheap closes, neither of them new apparatus: `cli.py`
       names the tuple as a module constant and the test imports it, or the pin asserts the
       gate's set against the generator's. The first also turns that comment sentence into a
       fact the tree holds.
```

**Closed when** the stage set reaches the regex and the pin from the one place the generator
defines it, or an assertion in the existing file compares the two sets.

**R861. (DOES NOT BLOCK -- it is a CORRECTION TO MY OWN VERDICT 10, and the implementer has
already relayed the wrong number) THE BASELINE OF NINE REDS WAS WRONG WITHIN ONE COMMIT OF MY
WRITING IT. The tree is at 78, and VERDICT 10 IS THE CAUSE: two of the report guards are
parametrised over the NEWEST VERDICT's findings and sites, so the baseline is a function of what
I write, not of what the implementer commits.**

```
claim  the number I told the implementer to trace against is not a constant
cmd    python -m pytest -q --tb=no -rf        (mine, at e6a20e3, tree clean)
out    78 failed, 3547 passed, 1 skipped in 966.33s (0:16:06)
cmd    verdict 10's own instruction, in this file below
out    "for the rest of step 3 the baseline is nine reds, every interim check traces against
        it one id at a time, and a tenth red is CZ1 (iv) unchanged"
cell   collection counted per file at both commits, in a worktree at e818375, nothing else
       moved
out    tests/regression/test_r1_example_regenerates.py     8 -> 11   (+3, the new test)
       tests/test_collected_set_golden.py                 77 -> 78   (+1, see below)
       tests/test_report_carried.py                      304 -> 221  (-83)
       tests/test_report_guard_states.py                  23 -> 23
       whole suite                                      3705 -> 3626  (-79, fully attributed)
       -- the -83 is `test_every_named_site_is_touched_or_declared` and
          `test_the_report_carries_the_finding`, parametrised over the newest verdict's sites
          and findings. Verdict 9 named a larger set and step 2's third revision ANSWERED it;
          verdict 10 names 12 findings and 51 sites and no report answers it, so 63 cases went
          from green to red while the parametrisation itself shrank.
cmd    the +1, so the delta is attributed and not rounded off
out    tests/test_collected_set_golden.py::test_every_test_name_cited_in_prose_exists gains the
       citation of `test_R845_each_PROVENANCE_key_appears_EXACTLY_ONCE` in the new helper's
       docstring, and it PASSES -- the "every citation resolves" guard working on this commit's
       own prose
cmd    the control that says nothing outside the two report-guard files is red
out    python -m pytest -q --tb=no tests/test_report_carried.py tests/test_report_guard_states.py
       78 failed, 165 passed, 1 skipped in 162.59s
       -- 78 in the whole suite and 78 in those two files is the same 78, so the other 3382
          collected cases are green. That is the statement that protects the trace, and it is a
          predicate rather than a count.
rule   EG3(i) -- every red traces BY NAME or it is CZ1 (iv) unchanged; EH1 -- the cascade is
       identified by the baseline being red and by each cascading state's own failure line; and
       C89's recorded lesson, that a tree red by design is a tree in which the next real red is
       harder to see
judge  **it does not block, and it is mine rather than the implementer's.** The operative
       correction, because the implementer will otherwise apply the wrong rule next commit:
       **"a tenth red is CZ1 (iv)" is WITHDRAWN.** The test is not a number. It is: every red
       is in `tests/test_report_carried.py` or `tests/test_report_guard_states.py`, and each
       either names a finding or a site of the newest verdict, or is a
       `test_the_guard_survives_the_state` case whose own inner FAILED list names those. A red
       that fails that predicate is CZ1 (iv) whether it is the tenth or the seventy-ninth.
       **And the count will move again at every verdict I write, including this one, because I
       am its input** -- which is the part worth keeping: a baseline whose value depends on the
       reviewer's own output cannot be handed to the implementer as a number.
```

**Closed when** nothing: it is a correction to a verdict, recorded so that the next commit
traces against the predicate rather than against nine.

## CI at the reviewed commit: RED, 78 reds, ALL 78 traced to EG3 state (2)

```
cmd    gh run list --commit e6a20e330fa1afc91fdc32b3d4eb3292f45898a2
         --json conclusion,status,databaseId,workflowName
out    [{"conclusion":"failure","databaseId":39173178232,"status":"completed",
         "workflowName":"CI"}]
       -- the run was IN PROGRESS when I began and I waited six polls for it. An unfinished
          run is not a pass and I did not record one.
cmd    gh run view 39173178232 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  225 collected, 0 failed  (222 at e818375, so the THREE new cases ran and
                                             passed on a Linux runner) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 164.24s) / guards and meta-tests FAILURE
         (78 failed, 1050 passed, 1 skipped in 693.69s)
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39173178232 --log-failed, the unique ids, matched against state (2)'s list
out    51  test_every_named_site_is_touched_or_declared[R850..R856-<site>]   -> EG3 state (2)
       12  test_the_report_carries_the_finding[R845..R856]                   -> EG3 state (2)
        1  test_the_CI_section_is_about_the_REVIEWED_commit                  -> EG3 state (2)
        1  test_the_Carried_table_is_what_the_generator_produces             -> EG3 state (2)
        1  test_the_generator_would_catch_a_row_under_the_wrong_number       -> EG3 state (2)
        1  test_the_report_carries_a_WHOLE_SUITE_count                       -> FC1
        1  test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW                    -> FC1
       10  test_the_guard_survives_the_state[baseline + 9]                   -> the cascade
       --- 51 + 12 + 1 + 1 + 1 + 1 + 1 + 10 = 78 exactly, with no remainder
cmd    the cascade identified by its own failure lines rather than by its names (EH1)
out    each inner run reads "66 failed, 154 passed, 1 skipped in 4.1-4.5s" and names
       test_the_report_carries_the_finding[R845] first; one reads 67 failed. The [baseline]
       state is red, which is EH1's other half.
cmd    the two state-(2) names that did NOT fire, so the enumeration is measured rather than
       assumed (R835)
out    test_the_answered_verdict_is_the_NEWEST_one                PASSED
       test_a_carried_row_points_at_a_section_that_discusses_it   all PASSED
       -- the enumeration over-lists here, for the ninth time
rule   CA2, which I keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD
       regardless of the local run; EG3 with EH1, EJ2 and FC1 -- state (2) is the
       verdict-written-report-not-yet boundary and it is designed; EG3(i) -- the waiver is
       conditional on the trace and the trace is pasted
judge  **all 78 trace, and the waiver applies in full: CZ0 (d) does not stand and CA2's HOLD is
       not reached.** I measured that rather than classifying it, and the control that makes it
       a measurement is the one in R861: the whole suite's 78 and the two report-guard files'
       78 are the same 78, so no red sits outside the boundary set. Every step in the lint job
       RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to
       see, and mypy is green there, so the CI-only types-PyYAML red FP1 found has stayed
       fixed. **The judged commit had a run because it was pushed first (FP1).**
```

**Not CK2's exhausted-allowance state, and the usual discriminator does not work here.**
`runnerName` is null in this repository's API output for ALL FOUR jobs including the one that
SUCCEEDED, so an empty runner name cannot separate the states on this project and I did not use
it. What separates them: both real jobs carry per-step conclusions, real counts and fifteen-
and ten-minute durations (22:39:22Z -> 22:54:19Z, 22:39:23Z -> 22:49:04Z), and the two skipped
jobs are the determinism workflow's own event gate (CK0) with empty step lists at a zero-second
duration -- which arises from a designed `if:` and not from an unstarted runner.

## Try to break it -- what I ran, and what it found

* **Two full regenerations of all three deliverables from this tree into temporary
  directories**, with the fixture's own recipe: 68.82 s and 70.55 s, `governing U = 1.71167 at
  platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)` both times, and **0 differing
  comparable lines in all three files** at 97 / 1286 / 70. That is the control for everything
  below and the fifth and sixth independent machine states for the wall clock.
* **Eighteen injections against the five real test functions**, fresh side held fixed, one edit
  each, with the gate's `PUBLISHED` root redirected to a copy so the committed artifacts were
  never touched: baseline; a sixth `| mesh |` row; `| load |` and `| code_check |` at `999.99`;
  a duplicated `| total |` row carrying an engineering-sized number; a deleted `| code_check |`
  row; a timing-shaped row in a CSV; `| total | 1.2e3 |`; duplicate `# deck:` lines with a
  DIFFERENT basename in all three files; duplicate `# deck:` lines with the SAME basename in
  two (my own verdict-10 green, now red); the same duplicate on the FRESH side only; `# Deck:`
  with a capital; `#deck:` with no space; and the governing `U` control. **Every one of the five
  test functions was shown to carry its own failure by at least one red, and every injection
  was red somewhere except the two rows the exclusion now tolerates by design.**
* **Both EH4 directions on the thing I was asked to attack.** The weakening direction: the
  exclusion is two rows wider than it was and no check reads a tolerated value (R858). The
  strengthening direction: the pin now requires EXACTLY five rows, so a duplicate or a missing
  one reddens it -- and I checked that this new strictness cannot fail false by reading
  `pipeline.py` rather than trusting the generator's defensive `if stage in result.timings`.
* **The comparable-line counts recomputed under both rules**, which is what found R857, and the
  per-file collection delta recomputed in a worktree at `e818375`, which is what found R861 and
  attributed all 79 of it.
* **The 78 reds one id at a time**, with each cascading state's inner FAILED list read rather
  than inferred from its name, and the two enumerated state-(2) names that do NOT fire named.

**What I did not find, and it is the larger part.** The R851 repair closes my own injection
exactly, in all three files, on both sides, with precisely one new case firing -- and two
evasions I invented afterwards are caught as well, by two different tests. The R850 repair
removes a real machine-dependent false red, derives the regex and the pin from one tuple, and
**declines the tolerance I offered it**, recording the refusal in the comment so that a later
reader does not re-propose it; that paragraph is the best thing in the diff. `ruff`, `black`,
`mypy`, 186 unit tests and all six ladder rungs are green, locally and in CI, and the three new
cases ran and passed on a Linux runner. Nothing in `floatfea/` moved and no deliverable moved.
**All five of my findings are in a figure, a sentence or a structural provenance -- not one of
them is a number in a gate.**

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree was
clean before and after I wrote this file.** Neither exception opens: this diff touches no part
of F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a published-artifact comparison. The last corpus commit
remains `ba1527e` (batch 47).

**I ran the recorded substitute, and both halves paid:**

* **A regeneration check on a published deliverable, in both directions** -- two independent
  full regenerations of all three R1 artifacts, diffed line for line, then eighteen injections
  against the gate that guards them. It produced **R857, R858 and R859**.
* **A continuum grid over the parameter space a decision rule guards** -- the exclusion's own
  space this time: the stage-name axis (three names, five names, a sixth name, a duplicate, a
  deletion), the value axis (`0.00`, `0.01`, `999.99`, `1234.00`, `1.2e3`), the file axis (all
  three artifacts), and the provenance axis (basename, directory, duplicate, capital, no space,
  fresh side). It produced **R860**, from the one axis the diff did not vary: WHERE the stage
  set comes from.

**This is the sixth consecutive round in which the regeneration check's weakening direction
produced the round's findings.**

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff 0aa0c4a..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff 0aa0c4a..HEAD | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance|slack"
out    "tolerance because the rows are two-decimal, and that is a threshold this gate has no
        business introducing. The reviewer proposed it against itself and withdrew it; I am
        recording that so the next reader does not re-propose it."
       -- a comment RECORDING A DECLINED threshold. No value is introduced.
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves, and the one threshold this step invited was declined by the implementer
       after I declined to ask for it. **EU1 does not attach** -- no value and no declared
       counter moves -- and I ran the adversarial configuration anyway, eighteen injections and
       two full model runs, because R694's lesson is that a value which does not move is the
       worst case and not the safest.
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1 -- no `Closes:`
line).** Step 3 remains open with all three reviewed revisions available. Nothing blocks, so
FR3's instruction stands and it is the only thing that matters this week: **build the rest of
FL2.**

1. **FL2, complete, before step 3's first reviewed revision (FR3).** Five items, none built:
   member topology from the config with the star as the default; `required_section` and
   `truss_sizing` in `floatfea run` with FM0's re-solve loop; the optional analyses off by
   default; headings as a list with the BEM refusal; the band check per case. The commit says
   so and claims none of it, which is correct. **This is the second commit of step 3 and both
   have been spent on ledgered gate items.** The locked plan routes those to the ledger by
   name, and FR0's date is 5 November.
2. **R860 before FL2 lands, not after.** It is the one of my five that FL2 itself makes live: a
   sizing loop that times itself puts a sixth sub-10-ms row in that table, and the hand copy of
   the stage tuple will not know. One import or one assertion.
3. **R849 with R854, over TWO files, still answered WHILE step 3 is built.** Two new
   deliverables are coming and both constants are hard-coded three-name tuples.
4. **R857, R858, R859 in the first reviewed revision**, with every figure regenerated at that
   commit (CP3) -- 97 rather than 99, the wall-clock sentence corrected, the mechanism sentences
   naming the assertion that actually fires. R847 and R848 unchanged; R850 is half paid, and
   R851 and R853 are paid.
5. **R852 and R856 remain with Xabier**, relayed correctly and verbatim this turn. Neither is
   the implementer's to repair in code.
6. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855, third
   occurrence), **against the PREDICATE in R861 and not against nine.** Every red in
   `tests/test_report_carried.py` or `tests/test_report_guard_states.py` naming a finding or a
   site of the newest verdict, or a `survives_the_state` case whose inner list names those;
   anything else is CZ1 (iv).
7. **The push (FP1) continued.** It gave this round a completed run at the judged commit, 78
   reds matching mine id for id, and the three new cases green inside ladder 6 on a machine
   neither of us controls. I waited for the run rather than recording an unfinished one.
8. **The schedule.** FR0's 5 November stands. Step 3 opened on 18 October; two commits in, FL2
   is unbuilt by design under FR3, and nothing has slipped against a date yet. **I am not
   re-opening the escalation FR0 answered, and I am recording one number rather than a warning:
   five items, eighteen days, two commits spent on the ledger.** The next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right.** It repaired a guard of its own that failed false, in the one way
EK2 permits -- by naming the real set rather than by giving the comparison slack -- and it wrote
down the tolerance it declined so that the next reader cannot re-propose it. It found the
dict-collapse in `_provenance` by reading the code I pointed at rather than taking my word,
extended the new check to all three artifacts and to both sides, and recorded the wrong figure
it was replacing instead of quietly substituting the right one. It accepted the two greens I had
reasoned were unreachable and did not pad the diff with them. **And it asked for its own
classification to be checked, which is how R861 got found: I went looking for the baseline I had
given it, and the baseline was wrong.**

---

<!-- EARLIER ROUNDS, VERBATIM. Hand-appended in the form
     scripts/write_verdict.py uses, under DX2: each round is added and no prior
     round is rewritten or removed. The tool refused this step (R856). -->

# Review — R1 step 3
Reviewed commit: e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
**Reviewed commit: `e818375beb4198f853d5c6427b0ea2c7bbbfe8c6`.**
Verdict: PASS
Tests: 3695 passed, 9 failed, 1 skipped   (my own run, at the reviewed commit, tree clean)
Scope: **ES0 INTERIM CHECK.** No report revision exists for step 3, so this counts against
no round and all three reviewed revisions remain available. **Nothing blocks.** Both
blocking items step 2 carried are ANSWERED, measured by me rather than read; six findings
are ledgered and one is an apparatus item that FF0 routes to the next commit.

**I RULED UNDER FR1 WITH EZ0** (`docs/directives/FR.md:14-26`, `CLAUDE.md` section "What
blocks for the rest of R1"). No finding below can cause a silently wrong result, and I say
so for each rather than leaving the classification implicit. **This file is HAND-WRITTEN
because the one sanctioned path in refuses it -- R856.**

```
cmd    git diff --stat e93becf..HEAD
out    tests/regression/test_r1_example_regenerates.py  | 201 +
       tests/regression/test_r1_published_artifacts.py  |  16 +
       -- two files, both tests, nothing else
cmd    git diff --stat e93becf..HEAD -- .claude docs/SUPERVISOR.md CLAUDE.md
out    (empty)                                   -- no STOP-class finding
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- tests/conftest.py 'tests/**/conftest.py'
out    (empty)
cmd    git ls-files -- tests/conftest.py 'tests/**/conftest.py'
out    tests/conftest.py                          -- a file, as my instructions say it must be
```

**STEP 1b DOES NOT FIRE, AND I SAY SO RATHER THAN SKIPPING IT.** There is no step-3 report,
so there is no `Answers:` header to compare. The newest revision in the tree is step 2's
third, `Answers: verdict 8 @ a7b2f62` (`docs/reports/R1/step-2.md:1302`), and verdict 9 is
newer -- which is EG3 state (2) by definition and is designed, not a defect.
`test_the_guard_reads_the_step_being_worked_on` is **green** in my run, which says
mechanically that state (1) is not in play.

## Carried

| item | status | where, measured by me |
|---|---|---|
| **R845** (not one number in the three published R1 deliverables is compared against anything) | **ANSWERED IN CODE, and I verified the repair by my own regeneration rather than by reading its counter-cases. The REPORT half of the condition is owed, correctly, at step 3's first reviewed revision.** | `tests/regression/test_r1_example_regenerates.py`, 8 cases. I ran `floatfea run` on the shipped example into a temp directory with the fixture's own recipe (68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`) and compared every line: **report.md 99 comparable lines, 0 differing; member_forces.csv 1286, 0 differing; utilisation.csv 70, 0 differing.** Then I injected: the governing `**U = 1.71167 -> 0.99999` reddens `REGENERATES[report.md]`; the **last digit of member_forces.csv line 701** and of **utilisation.csv line 60** each redden their own file's case, so the comparison reaches the middle of a 1289-line CSV and not only row 1. The condition asked for the wall clock excluded BY NAME rather than by tolerance, and it is a regex over stage names. **Closed in code.** Owed: the report pasting both directions, every figure regenerated at the report's own commit (CP3) -- three of the figures the new file already publishes are wrong, see R853. |
| **R846** (the R838 repair is green on three injections one step above the one it was built for) | **ANSWERED, and I reproduced all three injections and the restore** | `tests/regression/test_r1_published_artifacts.py:112-117` (nine distinct non-blank), `:139` (`LABEL.strip()`), `:171` (`caveat.strip()`). My own harness, 31 cases over the three artifacts: baseline **31 passed**; caveat 8 = a duplicate of caveat 4 -> **1 failed** (`NINE_caveats`, naming `9 entries and 8 distinct non-blank ones`); caveat 8 = `""` -> **4 failed** (three membership cases by file, plus the count); `LABEL = ""` -> **3 failed**, one per artifact; restored -> **31 passed**. The three doors verdict 9 measured open are shut. **The next injection up is still green -- R852 -- and it is not the implementer's to fix.** |
| **R847** (section 3's "0 of 49 rows" does not reproduce; the generator emits 23) | **still open, correctly -- ledgered, and there is no report revision in which it could be answered** | FR1's third class. It is C43 on the closure list. |
| **R848** (the empty-directory refusal admits `.`, `./`, `..`, `" . "`) | **still open, untouched by this diff, and correctly so** | `git diff e93becf..HEAD -- floatfea` is empty. Non-blocking, same class as R843, ruled twice. |
| **R849** (the caveat, disclaimer and provenance gates quantify over a hard-coded three-file tuple, and step 3 publishes two more files) | **still open, and it now has a SECOND site -- R854** | `ARTIFACTS` at `tests/regression/test_r1_published_artifacts.py:69` and now `NAMES` at `tests/regression/test_r1_example_regenerates.py:48`. Verdict 9 said R849 is answered WHILE step 3 is built; that is unchanged, and the condition now names two files. |
| **R835** (EG3's enumeration) | **still open, still Xabier's; this commit is its eighth measurement** | of state (2)'s enumerated names, **two fire and the rest are green**, and both that fire do so for FC1's reason. It over-lists here as it under-listed at EH1, FN2 and EJ2. Relayed unchanged. |
| **R836** | **recorded, no change in this diff** | unchanged. |
| **C29, C34, C35** (`ruff`, `black`, `mypy`) | **green at this commit, on a machine neither of us controls** | CI run 39169784204, job `lint, unit and guards`, read at step level: `actionlint` SUCCESS, `ruff` SUCCESS (`All checks passed!`), `black --check` SUCCESS, `mypy` SUCCESS, `unit tests` SUCCESS (`186 passed in 67.62s`). Every one RAN rather than being skipped behind an earlier red, which is what CZ1 (iii) exists to see. |
| **C42** (U+FFFD in historical verdict headers) | **mine, accepted, carried** | not repaired in this verdict; repaired by the rounds that touch the files. |
| **C43, C44, C45** | **C43 and C44 carry; C45's ROUTING WAS MINE AND IT WAS WRONG** | verdict 9 ledgered C45. **FF0 says a closure item in the gating apparatus is NOT ledgered** -- `scripts/ci_section.py` reads the gating record -- so C45 belonged in the next commit, not on the list. I am correcting my own routing. See the process note: it cannot in fact be fixed before step 3's report exists, and that is the thing worth recording rather than the misfiling. |
| **C26, C27, C28, C30, C31, C32, C33, C36, C37, C39** | **carry to the closure artifact as a list** | not re-reviewed item by item, per CZ0. An interim check writes no closure list (ES0); this row is the pointer, not the list. |
| `scripts/suite_count.py`'s own line + CZ1 (ii)/(iii)'s four outputs | **still owed, and now STRUCTURALLY UNPAYABLE until step 3's report exists** | see the process note. Not a finding against the implementer. |
| **EG3(ii): the verdict commit measured** | **DONE, by me, at this commit** | the two report-guard files: **9 failed, 320 passed, 1 skipped**, the same nine ids as verdict 9's and the same nine as CI's, traced one at a time under R855. |

## Findings

**NOTHING BLOCKS.** The diff is two test files, no `floatfea/` change, no tolerance, and the
three published deliverables are byte-unchanged -- which I established by regenerating them,
not by reading the diff. Both carried blocking items are answered at the layer they were
about. The seven findings below are the weakening directions I could still reach, and under
FR1 none of them can put a wrong number in front of anyone; I say which, for each.

**The implementer asked for the EXCLUSION to be attacked, and that is where four of the
seven are.** Two classes of line are dropped from the byte comparison and the commit message
claims "**BOTH are checked elsewhere rather than merely dropped**". For the provenance class
that is true in part and I measured its reach. **For the wall-clock class it is false:
nothing in the tree reads any published wall-clock value.**

**R850. (DOES NOT BLOCK -- ledgered) THE WALL-CLOCK EXCLUSION COVERS THREE OF THE FIVE ROWS
THE GENERATOR WRITES, SO TWO WALL-CLOCK ROWS SIT INSIDE A BYTE COMPARISON -- and in the other
direction no check anywhere reads a published wall-clock VALUE: `| total | 97.27 |` edited to
`| total | 999.99 |` and `| solve | 97.08 |` edited to `| solve | 0.01 |` are both green on
all 8 cases.**

```
claim  the exclusion's declared class and the generator's actual output are not the same set
cmd    floatfea/cli.py:296-299, the row loop
out    for stage in ("build", "load", "solve", "code_check", "total"):
           lines.append(f"| {stage} | {result.timings[stage]:.2f} |")
       -- FIVE stages, every one a time.perf_counter() delta (floatfea/run/pipeline.py:605,
          653, 664, 669, 672)
cmd    the exclusion regex, tests/regression/test_r1_example_regenerates.py:56
out    r"^\|\s*(build|solve|total)\s*\|\s*[0-9.]+\s*\|\s*$"       -- THREE
cmd    the file's own declared class, :54-55
out    "the report carries a `| stage | seconds |` table whose THREE rows cannot agree
        between two runs"
cell   my own injections against the real gate's four test functions, one edit each, the
       fresh side held fixed at my own 68.95 s run of the shipped example
out    CONTROL unmodified                        8 passed, 0 failed
       | total | 97.27 | -> | 999.99 |           8 passed, 0 failed   <- GREEN
       | solve | 97.08 | -> | 0.01 |             8 passed, 0 failed   <- GREEN
       | load | 0.00 | -> | 0.01 |               7 passed, 1 failed   <- COMPARED
       | code_check | 0.00 | -> | 0.01 |         7 passed, 1 failed   <- COMPARED
cell   the margin on the two compared rows, solved rather than sampled: the printed row
       flips at 5 ms, and the load stage is np.load + exported_froude_lambda + the period
       check
out    first pass 1.6 ms, then 0.7 ms (12.8 MB npz, lazy open)  -> margin 3.1x on the
       coldest sample I could take
cmd    the same two rows on a Linux runner with a different filesystem
out    ladder 6 (empty:tests/verification/rung6 full:tests/regression):
       214 collected at 8542d79 -> 222 collected here, 0 failed, 0 errored -- the 8 new
       cases RAN and passed there, so both compared rows printed 0.00 on that machine too
rule   my own recorded guard -- an excluded line is a line nothing checks unless something
       else checks it, which the file itself says at :50-51; EH4 -- the boundary is solved in
       the direction that weakens the gate
judge  **two statements in opposite directions, and neither is a silently wrong result.**
       (i) `load` and `code_check` are inside the comparison with a 3.1x margin to a FALSE
       RED. A false red is loud, so it does not block -- but the pressure a false red creates
       is to widen the exclusion, at the worst possible moment to be deciding what the
       exclusion means. (ii) No published wall-clock value is checked by anything, so the
       commit message's "both are checked elsewhere" is false for this class. That is prose
       (FR1's third class) and the number is a wall clock nobody sizes steel against, so it
       does not block either. **And I checked the obvious repair and WITHDREW it:**
       `timings["total"]` is the exact sum of the four at full precision
       (floatfea/run/pipeline.py:672), but the published rows are rounded to 2 dp, so
       `total == build + load + solve + code_check` on the PRINTED values needs up to 0.02
       of slack -- which is a tolerance, in `tolerances.py`, for a wall clock. I am not
       asking for it.
       What I would accept: the exclusion covers all five stages the generator writes, the
       pin at :172-175 lists all five, and the docstring says the wall-clock VALUES are
       excluded and unchecked instead of saying they are checked elsewhere.
```

**Closed when** the exclusion and its pin cover the same five stage names
`floatfea/cli.py:297` writes, and the two prose claims -- at
`tests/regression/test_r1_example_regenerates.py:54-55` and in the commit message -- are
corrected to what was measured.

**R851. (DOES NOT BLOCK -- ledgered) THE PROVENANCE EXCLUSION IS CHECKED BY BASENAME ONLY,
AND THE KEY-SET PIN READS `report.md` ALONE. Three injections measured green: the deck path's
DIRECTORY swapped in all three files, the `load_cases` MODE word changed, and a second
contradictory `# deck:` line inserted into a CSV.**

```
claim  the reach of the exclusion the implementer asked me to attack, solved from the side
       that weakens it (EH4)
cell   the real gate's four test functions, fresh side held fixed, one class of edit each
out    CONTROL unmodified                                            8 passed, 0 failed
       deck DIRECTORY swapped, basename kept, all three files        8 passed, 0 failed  <- GREEN
         data/platform/platform12_deck.yaml -> /home/someone-else/junk/platform12_deck.yaml
       CONTROL deck BASENAME changed, all three files                5 passed, 3 failed
         -> "the deck provenance names 'OTHER_deck.yaml' in the committed file and
             'platform12_deck.yaml' in a fresh run of this tree"   -- the basename half WORKS
       load_cases MODE word npz -> static, all three files           8 passed, 0 failed  <- GREEN
       a SECOND "# deck: /home/someone-else/junk/platform12_deck.yaml" line
         inserted into utilisation.csv                               8 passed, 0 failed  <- GREEN
       CONTROL an extra "| solve | 3.00 |" row in report.md          6 passed, 2 failed
         -> EXCLUSION pin: ('the SHIPPED report', ['build','solve','solve','total'])
       CONTROL the three provenance lines DELETED from report.md     6 passed, 2 failed
       CONTROL the three timing rows DELETED from report.md          7 passed, 1 failed
cmd    why the duplicate is invisible, read rather than guessed
out    tests/regression/test_r1_example_regenerates.py:105-112 -- _provenance returns a
         DICT keyed on config|deck|load_cases, so two lines with one key COLLAPSE and the
         last wins; :168-177 -- the pin iterates over report.md and the fresh report ONLY,
         so for the two CSVs the excluded set is pinned by nothing
rule   EH4; and my own recorded guard -- check that the collection the assertion inspects can
       contain the failure
judge  **it does not block, and I want the reason on the record rather than the ruling.** No
       number moves in any of the three. None of the three is a string this tool can emit:
       the directory component is a FUNCTION OF THE CONFIG'S OWN LOCATION
       (floatfea/run/config.py:507-523 -- anchored on source.parent, then its parent, then
       absolute), which is exactly why the exclusion exists and why the fixture's copy in a
       temp directory differs at all. So a wrong directory in a shipped artifact is reachable
       only by a hand-edit, and a hand-edited provenance path puts no wrong engineering
       number in front of anyone. Under FR1 that is not a silently wrong result, and under
       its second head nothing is accepted and used other than as declared -- the deck that
       was USED is the right one in every green row above.
       **What I would accept, if it is cheap:** the pin loop at :168 runs over all three
       files rather than over the report, which is the same loop already written; and the
       shipped path is compared by resolving it against the two anchors _relative uses
       instead of by rsplit("/", 1)[-1].
```

**Closed when** the excluded key set is pinned in all three artifacts rather than in the
report alone -- or the report states that the two CSVs' excluded set is pinned by nothing and
why that is acceptable.

**R852. (DOES NOT BLOCK -- ledgered, AND IT IS THE ONE I MOST WANT READ, because no repair the
implementer can write will close it) A CAVEAT TRUNCATED TO ITS OWN MARKER IS GREEN ON 31 OF
31 CASES. TABLE_CAVEATS[8] reduced from R743's sentence to the string "R743:" passes the new
distinct-and-non-blank count, passes all 27 membership cases, and passes after the artifacts
are regenerated. So does LABEL = "a". This is R831 returning in a new shape: R831 was "the
needle is the MARKER and the marker survives a rewording", and truncating the text to the
marker turns the needle back into a marker.**

```
claim  the repaired gate's boundary, one injection above the three it was built for
cell   floatfea.cli.TABLE_CAVEATS / LABEL rebound and the gate re-imported so it reads the
       mutated value, the three committed artifacts untouched, 31 cases (9 caveats x 3 files
       + 3 disclaimer + the count)
out    BASELINE                                              31 passed,  0 failed
       caveat 8 = DUPLICATE of caveat 4                      30 passed,  1 failed
       caveat 8 = ""                                         27 passed,  4 failed
       LABEL = ""                                            28 passed,  3 failed
       caveat 8 truncated to its first word, "R743:"         31 passed,  0 failed  <- GREEN
       caveat 8 = "C_m"                                      31 passed,  0 failed  <- GREEN
       LABEL = "a"                                           31 passed,  0 failed  <- GREEN
       RESTORED                                              31 passed,  0 failed
cmd    what the published caveat says, so the loss is stated rather than implied
out    floatfea/cli.py, TABLE_CAVEATS[8]:
       "R743: C_m MULTIPLIES the bending term in section 3.3.1's interaction, ..."
       -- the sentence that delegates the C_m DIRECTION to a published sensitivity column
cmd    whether the new R845 gate catches it instead
out    no. The regeneration gate compares the shipped files against a fresh run, so once the
       artifacts are regenerated BOTH sides carry the stub and both are green. The two gates
       compose against a stub that was never regenerated, and neither covers a regenerated
       one.
cmd    whether any record of the nine caveat TEXTS exists to compare against
out    grep -n "caveat" docs/directives/FO.md
       :20-22  "all nine caveats in the header; a test that reads the published .md and .csv
                files, not a stub. Each must redden when one caveat is removed"
       -- FO2 records the COUNT and the mechanism. It records no caveat text.
rule   my own recorded guard -- a gate carries its own failure, and "R743:" in text cannot
       fail against a file that contains R743's real caveat; EH4 -- the injection rises until
       a clean case trips
judge  **it does not block, for a reason that is not about severity.** The published outcome
       is the one verdict 9 stated for R846 -- a utilisation column whose C_m direction is a
       stub while the gate certifies nine of nine -- so by severity it IS R846. But **no
       comparison between the code and the files can detect it**, because both halves carry
       the stub; the only check that could is a comparison against an independent record of
       what the nine caveats SAY, and this repository has none. The cheap alternative is a
       minimum length or word count, which is a threshold for a sentence and belongs in
       tolerances.py if anywhere, and I am not asking for that. **So this is not the
       implementer's to repair in code.** It is a question for Xabier about FO2: if the nine
       caveats are load-bearing enough that their absence is a wrong result, their TEXTS
       belong in the directive record, and then one list comparison closes the class
       permanently. Recorded, measured and relayed -- not a round.
```

**Closed when** FO2's nine caveat texts exist in a record the gate can compare against -- or
the report states, with the three green rows above, that the caveat gate cannot distinguish a
caveat from its own marker and that this is accepted.

**R853. (DOES NOT BLOCK -- ledgered, FR1's third class) "102, 1289 AND 73 COMPARABLE LINES"
DOES NOT REPRODUCE. The comparable counts are 99, 1286 and 70. The published figures are the
report's total minus its three provenance lines, and the two CSVs' TOTAL line counts -- so the
timing exclusion was subtracted nowhere and the provenance exclusion was subtracted only for
the report.**

```
claim  the figure the new file offers as "the measurement that says the numbers are
       reproduced" (tests/regression/test_r1_example_regenerates.py:62-64)
cmd    the gate's own _lines() applied to the three shipped files and to my own fresh run
out    report.md          total 105   comparable 99    differing 0
       member_forces.csv  total 1289  comparable 1286  differing 0
       utilisation.csv    total 73    comparable 70    differing 0
cmd    where the published numbers come from
out    102 = 105 - 3   (the provenance lines only)
       1289, 73        = the TOTAL line counts, with nothing excluded
rule   BF0 with CP3 -- the figure is pasted from the run that produced the artifact and the
       paste is the last edit; BP0 -- a figure carries the rule it was measured against
judge  the substantive claim -- that nothing but the two declared classes differs -- is TRUE,
       and I verified it independently on a fourth machine state: 0 differing comparable
       lines in all three files. Only the three counts are wrong, and they are wrong in the
       direction that makes the gate sound wider than it is. FR1's third class; no number in
       a gate or a deliverable moves. **It is recorded because it is the figure the step's own
       repair is measured by**, which is exactly what R847 was two rounds ago.
```

**R854. (DOES NOT BLOCK -- ledgered; it joins R849) R849 NOW HAS A SECOND SITE. The new gate
repeats the hard-coded three-file tuple, so FR3's two further deliverables would arrive
UNCOMPARED as well as uncaveated.**

```
claim  the artifact set is fixed in the source in two files now, not one
cmd    the two constants
out    tests/regression/test_r1_published_artifacts.py:69  ARTIFACTS = (REPORT, FORCES,
                                                                        UTILISATION)
       tests/regression/test_r1_example_regenerates.py:48  NAMES = ("report.md",
                                                                    "member_forces.csv",
                                                                    "utilisation.csv")
cmd    what step 3 publishes, from the plan
out    docs/milestones/R1.md step 3 -- required_section and truss_sizing in `floatfea run`,
       both OFF in the shipped example today
rule   my own recorded guard -- check that the collection the assertion inspects can contain
       the failure
judge  not a defect today: the two outputs are off, the files do not exist, and the gate is
       green because main() writes exactly these three. Verdict 9 ruled R849 answered WHILE
       step 3 is built; the only change is that its closing condition now names two files,
       and the second is the one that compares NUMBERS. A fourth deliverable that arrives
       with no numeric comparison is R845 with a different file name, and that is the one of
       my seven findings that could later put a wrong number in front of someone.
```

**R855. (DOES NOT BLOCK -- ledgered, and it is the SECOND occurrence) THE SUITE WAS NOT RUN AT
A PUSHED, REVIEWED COMMIT, AND THE TREE'S NINE REDS WERE NOT RECORDED WITH THEIR CAUSE NAMED.
The implementer ran `tests/regression tests/unit` (408 passed) and asked whether the light
scope requires the full run. It does, and EG3(i) requires the FAILED list pasted with the
state named. I did both; nothing was hiding this time.**

```
claim  ES0's light scope is the suite, and EG3's waiver is conditional on a trace that was
       not written
cmd    python -m pytest -q --tb=no -rf        (mine, at the reviewed commit, tree clean)
out    9 failed, 3695 passed, 1 skipped in 957.64s (0:15:57)
cmd    the implementer's two figures, cross-checked against CI's own numbers rather than
       re-run
out    unit tests 186 passed + ladder 6 222 collected = 408   (this commit, run 39169784204)
       unit tests 186 passed + ladder 6 214 collected = 400   (8542d79, run 39164110433)
       -- both reported counts are exactly right, and the +8 is this gate
cmd    the nine reds, traced ONE ID AT A TIME per EG3(i), not as a family
out    test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW
         "run 39162423263: the table says no result (status in_progress), gh says failure"
                                                                      -> FC1, and C45
       test_the_report_carries_a_WHOLE_SUITE_count
         "the newest revision carries no whole-suite line ... Generate it with
          python scripts/suite_count.py"                              -> FC1
       test_the_guard_survives_the_state[baseline] and six others
         each inner run read individually: 2 failed, 301 passed, 1 skipped, and the two
         FAILED ids inside each are the two above                     -> the cascade
       test_the_guard_reads_the_step_being_worked_on                  -> PASSED
rule   ES0 -- an interim check is the suite and CI at the commit plus a CZ0 (a)-(d) scan;
       EG3(i) -- the waiver is conditional on the trace and the trace is pasted; CA2, which I
       keep in full because CLAUDE.md does not carry it -- a red CI is a HOLD regardless of
       the local run; EH1 -- the cascade is identified by the baseline being red and by each
       cascading state's own failure line, not by its name
judge  **all nine trace, to two names rather than to a family, and the waiver applies in full
       -- so CZ0 (d) does not stand and CA2's HOLD is not reached.** I measured that rather
       than classifying it. The finding is that the record did not say so at a pushed commit,
       for the second time in three commits: verdict 8's R841 was a NINTH red that an
       eight-file subset could not contain, and the subset is the same shape of choice. It
       does not block under FR1 -- no wrong number follows, and in fact nothing was hiding --
       but a tree whose reds are not traced is the tree in which the next real one is not
       seen, and R629 is this project's own measured instance of that.
```

**Closed when** the next commit in step 3 records the whole-suite run and names the EG3 state
with its FAILED list, as every revision in step 2 did.

**R856. (DOES NOT BLOCK -- APPARATUS, and under FF0 it is NOT LEDGERED: it is fixed in the next
commit) `scripts/write_verdict.py` REFUSES TO WRITE A VERDICT FOR A STEP THAT HAS NO REPORT,
AND FR3 PLUS ES0 MAKE THAT THE NORMAL STATE OF AN INTERIM CHECK. This verdict is hand-written
because the one sanctioned path into `docs/reviews/` refused it.**

```
claim  the sanctioned path cannot write the verdict the Stop hook requires
cmd    printf the four mandatory sections with a PASS header |
         python scripts/write_verdict.py --milestone R1 --step 3
out    refused: no step report at ...\docs\reports\R1\step-3.md
       EXIT=1
cmd    the refusal site
out    scripts/write_verdict.py:179-181
         report = root / f"docs/reports/{args.milestone}/step-{args.step}.md"
         if not report.exists(): sys.exit(f"refused: no step report at {report}")
cmd    whether the state is exceptional
out    docs/directives/FR.md:28-33 (FR3) -- "Build ALL of it before the first reviewed
       revision. Interim checks run as the hook requires and count against no round."
       CLAUDE.md (ES0) -- "a verdict the hook forces at a turn boundary mid-step, on a tree
       with NO new report revision, is an INTERIM CHECK"
rule   FF0 -- anything that reads the gating record, or decides whether a green is believed,
       is fixed in the next commit under EK2's repair-not-extend rule; and the file's own
       docstring already records the precedent: "the reviewer could not write an R1 verdict
       through the one sanctioned path in, and hand-wrote it instead"
judge  the refusal was right when every step's first reviewed artifact was its report. FR3
       inverted that: step 3's report comes after all of FL2, so every interim check in step 3
       is a verdict on a step with no report, and the only path in refuses all of them. The
       check that is wanted is "a step with no report AND no diff to judge"; here the diff is
       217 lines. **I am recording it rather than widening it** -- EK2 says a guard that fails
       false is fixed or deleted, never extended, and which of those this is, is Xabier's
       call, because it is the reviewer's own tooling and the file says so itself at :44-48.
       Until then the hand-written file IS the verdict, as it was for R1 step 1.
```

## The process note this tree is about to need, said once

**FR3 + FC1 + EK3 means the tree is RED BY TWO FOR THE WHOLE OF STEP 3, by construction, and
no file says so.** `test_the_report_carries_a_WHOLE_SUITE_count` wants a line inside the
newest report revision; `test_the_CI_TABLE_agrees_with_gh_FOR_EVERY_ROW` wants that revision's
CI table regenerated (C45). The newest revision is step 2's third, and **EK3 forbids any
commit touching a closed step report**, so neither can be written until step 3's first
revision exists -- which FR3 places after all five of FL2's items. FC1 says both are designed
and self-clearing "in the next commit"; FF0 says an apparatus item is "fixed in the next
commit". **Neither is available here, and that is neither the implementer's fault nor mine.**
The consequence is operational and I will act on it: for the rest of step 3 the baseline is
nine reds, every interim check traces against it one id at a time, and a tenth red is CZ1 (iv)
unchanged. This is C89's shape -- "a tree that is red by design is a tree in which the next
real red is harder to see" -- and it goes to Xabier with R856, because the exit is a clause
and not a commit.

## Try to break it -- what I ran, and what it found

* **A full regeneration of all three deliverables from this tree into a temp directory, with
  the fixture's own recipe.** 68.95 s, `governing U = 1.71167 at platform:hub4_arm ROOT`,
  **0 differing comparable lines in all three files** (99, 1286, 70). That is the control for
  everything below, and the fourth independent machine state for the wall clock.
* **Thirteen injections against the new gate**, each run against the real test functions with
  the fresh side held fixed: the governing U; the last digit of member_forces.csv line 701;
  the last digit of utilisation.csv line 60; five wall-clock edits; three provenance edits; a
  duplicated provenance line in a CSV; an extra timing-shaped row; and two deletion controls.
  **Three classes came back green -- R850, R851 -- and each of the gate's four test functions
  was shown to carry its own failure by at least one red.**
* **Seven injections against the repaired caveat gate**, including the three verdict 9
  measured (all three redden, 1 / 4 / 3 cases, and restore) and **three one step above
  (R852)**. My first pass of that harness had a bug -- three cases ran with the unmutated
  tuple and printed `31 passed`, which would have read as the repair not working. I found it
  because `R846 b` should have reddened and did not, fixed the harness and re-ran. Recorded
  because an instrument that silently fails to inject is the shape of every finding in this
  section.
* **The boundary on the two compared wall-clock rows, solved rather than sampled:** the
  printed row flips at 5 ms, and the load stage measures 1.6 ms cold and 0.7 ms warm --
  margin 3.1x.
* **CI read at the step level, both jobs**, including the ladder's rung-6 collected count
  before and after, which is what says the new gate RAN on a machine neither of us controls
  rather than being collected and skipped.
* **The nine reds one id at a time**, with each cascading state's inner FAILED list read
  rather than inferred from its name.

**What I did not find, and it is the larger part.** R845's repair does what verdict 9 asked
and it is stronger than the condition required: it reaches the last digit of any line in any
of the three files, it is redirected so it cannot overwrite the evidence it checks, and it
arrives green on a Linux runner as well as here. R846's three doors are shut. No `floatfea/`
line moved, no tolerance moved, the three deliverables are byte-unchanged, and `ruff`,
`black`, `mypy`, 186 unit tests and all six ladder rungs are green in CI. **The exclusion --
the thing I was asked to attack -- is honest in its structure: it is declared, it is pinned
for the report, and its deletion direction is backstopped. Where it leaks, it leaks on paths
and on a wall clock, and not on one engineering number.**

## CI at the reviewed commit: RED, nine reds, ALL NINE traced to FC1's designed pair

```
cmd    gh run list --commit e818375beb4198f853d5c6427b0ea2c7bbbfe8c6
         --json conclusion,status,databaseId
out    [{"conclusion":"failure","databaseId":39169784204,"status":"completed"}]
       -- the run was IN PROGRESS when I began and I waited for it. An unfinished run is not
          a pass and I did not record one. The SHORT sha returns an empty list; the flag
          needs the full sha, as verdict 9 recorded.
cmd    gh run view 39169784204 --json jobs, read at STEP level
out    the verification ladder : SUCCESS
         ladder 1  1276 collected, 0 failed / ladder 2  66 / ladder 3  314 /
         ladder 6  222 collected, 0 failed  (empty:rung6 full:tests/regression; 214 at
                                             8542d79, so the 8 new cases ran and passed) /
         ladder 4  343 / ladder 5  87
       lint, unit and guards : FAILURE
         actionlint SUCCESS / ruff SUCCESS / black --check SUCCESS / mypy SUCCESS /
         unit tests SUCCESS (186 passed in 67.62s) / guards and meta-tests FAILURE
       CI determinism -- leg / ten legs agree : SKIPPED (the workflow's own event gate, CK0)
cmd    gh run view 39169784204 --log-failed, the ids
out    identical to my own nine, id for id, and each cascading state's inner run reads
       "2 failed, 301 passed, 1 skipped" naming the two FC1 ids
rule   CA2 -- a red CI is a HOLD regardless of the local run; EG3 with FC1 -- the two
       CZ1-class names are state (2)'s and neither can pass in the commit it describes;
       EG3(i) -- EVERY red traces by name or it is CZ1 (iv) unchanged
judge  **all nine trace, and the waiver applies in full: CZ0 (d) does not stand.** Both FC1
       reds are designed and neither is clearable before step 3's report exists -- see the
       process note. Every step in the lint job RAN rather than being skipped behind an
       earlier red, which is what CZ1 (iii) exists to see, and mypy is green there, so the
       CI-only types-PyYAML red FP1 found has stayed fixed.
```

**Not CK2's exhausted-allowance state.** Both real jobs have per-step conclusions, real counts
and eight- and nine-minute durations; the two skipped jobs are the determinism workflow's own
event gate and not an unstarted runner.

## Corpus (EG4(e))

**The pause held. Zero new entries. `tests/corpus/` is untouched by me and the working tree
was clean before I wrote this file.** Neither exception opens: this diff touches no part of
F4's load-mapping gate, and EB6's label-provenance gate is about buoy-centre labels in
`tests/verification/rung4/`, not about a caveat tuple or a published-artifact comparison. The
last corpus commit remains `ba1527e` (batch 47).

**I ran the recorded substitute, and the half that paid is the one this step is about:**

* **A regeneration check on a published deliverable, taken in BOTH directions** -- all three
  R1 artifacts regenerated from this tree and diffed line for line (0 differing), then
  thirteen injections against the gate that now guards them. It produced R850, R851 and R853.
  **This is the fifth consecutive round in which the regeneration check's weakening direction
  produced the round's findings.**
* **A continuum grid over the parameter space a decision rule guards** -- the caveat gate's
  mutation space rather than the config's this time: duplicate, blank, whitespace-only,
  truncated-to-first-word, degenerate-substring, and the same five on LABEL. It produced
  **R852**, the one finding here that no code in this repository can close.

## Tolerances touched

**None.** No value, no form, no counter, no injection.

```
cmd    git diff e93becf..HEAD -- floatfea/tolerances.py
out    (empty)
cmd    git diff e93becf..HEAD -- floatfea tests scripts | grep "^+" |
       grep -nE "isclose|abs_tol|rel_tol|approx|atol|rtol|_COUNTER|tolerance"
out    (no match)
cmd    the same, widened to any literal comparison the diff adds
out    93:+   assert main(["run", str(cfg)]) == 0        -- an exit code
       210:+  assert len({c.strip() for c in TABLE_CAVEATS if c.strip()}) == 9
       -- FO2's own declared count, annotated at :204-209; ruled a declared quantity and not
          a threshold at verdict 9, and that ruling is unchanged by the new form
rule   CLAUDE.md section Tolerances, and its clause on anything that functions as a tolerance
       under another name
judge  nothing moves. **EU1 does not attach** -- no value and no declared counter moves --
       and I ran adversarial configurations anyway, twenty of them, because R694's lesson is
       that a value which does not move is the worst case and not the safest. And I declined
       to ask for the one new threshold this step invited: a slack on the published
       wall-clock sum (R850).
```

## Next step opens when

**This is an interim check, so it closes nothing and opens nothing (ES0, FK1).** Step 3
remains open with all three reviewed revisions available. Nothing blocks, so FR3's instruction
stands: build the rest of FL2.

1. **FL2, complete, before step 3's first reviewed revision (FR3):** member topology from the
   config with the star as the default; `required_section` and `truss_sizing` in `floatfea
   run` with FM0's re-solve loop; headings as a list with the BEM refusal; the period-band
   check. None of it is in this commit, as the commit says.
2. **R849 with R854 -- answered WHILE step 3 is built, over TWO files now.** The caveat,
   disclaimer, provenance AND regeneration gates are written over the artifact set the config
   declares, not over two hard-coded three-name tuples. A fifth deliverable arriving with no
   numeric comparison is R845 with a different file name.
3. **R850's two prose corrections and the five-stage exclusion**, R851's pin over three files,
   R853's three counts -- all in the first reviewed revision, with every figure regenerated at
   that commit (CP3). R847 and R848 unchanged.
4. **R852 and R856 go to Xabier, not into a round.** R852 needs FO2's caveat texts recorded
   before any gate can see the defect; R856 needs a clause about the reviewer's own tooling.
   Both are relayed with their measurements and neither is the implementer's to repair in code.
5. **The whole-suite run and the EG3 state recorded at every commit of step 3** (R855),
   against a baseline of nine, with a tenth red treated as CZ1 (iv).
6. **The push (FP1) continued.** It gave this round a completed CI run at the judged commit,
   nine reds matching mine id for id, and the new gate's 8 cases green inside the ladder's
   rung 6 on a machine neither of us controls. I waited for the run rather than recording an
   unfinished one.
7. **The schedule.** FR0's 5 November is the target. Step 3 opened on 18 October carrying two
   blocking items, both answered in its first commit, with FL2 unbuilt by design. Nothing has
   slipped and I am not re-opening the escalation FR0 answered; the next progress statement is
   step 3's first reviewed revision (FR5).

**What this commit got right, and it is much the larger part.** Two blocking items were
answered first, at the layer each was about, in one commit, with counter-cases in both EH4
directions and a redirected fixture so the gate cannot overwrite its own evidence. The
implementer reproduced my R845 finding independently instead of taking it, flagged the one
lint choice that reads like an omission (`strict=False`, and the reasoning is right -- the
length mismatch is reported with both counts, which I confirmed by injecting one), and found
the provenance exclusion by RUNNING the gate rather than by anticipating it, which is the only
way that class is ever found. **Every one of my seven findings is in the reach of a check, not
in a number: nothing in `floatfea/` moved, no deliverable moved, and the gate that now guards
them reaches the last digit of every line in all three files.**
