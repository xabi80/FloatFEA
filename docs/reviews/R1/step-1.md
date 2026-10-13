# Review — R1 step 1
Reviewed commit: 472bcd1a22175eae6e8e43aeffdbf109be0eaab0
Verdict: HOLD
Tests: 3356 passed, 37 failed, 1 skipped   (my own run, `python -m pytest -q`, 703.78s)

**WRITTEN BY HAND, AND THAT IS FINDING R804.** `scripts/write_verdict.py` is the one
sanctioned path into this directory and it cannot express `R1`:

```
cmd  echo "Verdict: HOLD" | python scripts/write_verdict.py --milestone R1 --step 1
out  write_verdict.py: error: argument --milestone: milestone 'R1' is not a label of the
     form 2, 2a, 6, 6a, F6a -- the value becomes a path segment
```

Passing `--milestone 1` to satisfy the validator would have written this verdict into
`docs/reviews/F1/step-1.md` (`:148` hard-codes the `F`), i.e. into another milestone's
record. So this entry is written directly, in the format `write_verdict.py` produces, and
the deviation is recorded here rather than left silent. The `PreToolUse` hook clears
`gating-supervisor`; the file is at the correct path.

## Carried

**Checked, nothing carried.** R1 step 1 is this milestone's first step, `docs/reviews/R1/`
did not exist before this entry, and `git log` confirms no prior verdict in R1 — FL opened
the step and FM0 re-locked the plan at `a507baf` before any code. Neither is a verdict with
findings. F6b closed at the verdict carrying `Closes: F6b` (FK1) with no blocking item
open; the report's section 8 makes CLAUDE.md's declaration and names R788-R791 as staying
on the F6a/F6b ledgers without reopening them. I confirm that disposition: none of the four
is in `floatfea/`, a tolerance, a gate assertion, or red here.

The report's `Answers:` header names "FL opens the step; FM0 amended the plan" rather than
a verdict. With no verdict in R1 there is none to name, so the superseded-round check is
vacuous and not a HOLD.

## Findings

Ten items. Eight are defects in `floatfea/` or in a published deliverable under `results/`
(EZ0) and block under CZ0(a); two are FF0 class in the gating apparatus. None is a
tolerance and none is a red test. Ordered by what a reader of the output loses.

**R804. `scripts/write_verdict.py` cannot write an R1 verdict — the SIXTH F-assumption, in
the gate's own writing path.** Section 5a found and repaired five sites (the hook,
`check_carried`, `ci_section`, `test_report_carried`, `test_plan_matches_tolerances`). This
one was missed by both passes, and it is the one that stops the gate working.

```
cmd  grep -n "_milestone|docs/reviews/F|docs/reports/F|F{cleaned}" scripts/write_verdict.py
out  :70   re.fullmatch(r"\d+[a-z]?", cleaned)      after stripping only a leading F/f
     :104  the same expression in _closes
     :110  return f"F{cleaned}"                     --closes could only ever emit `F...`
     :143  report = root / f"docs/reports/F{m}/step-{k}.md"
     :148  out    = root / f"docs/reviews/F{m}/step-{k}.md"
rule FF0: anything that reads the gating record, or decides whether a green is believed,
     is fixed in the NEXT commit under EK2's repair-not-extend rule
```

Five F-assumptions in one file, and `:148` is worse than a refusal: with the validator
satisfied by `--milestone 1` it silently targets F1's verdict file. FF0 class, so the next
commit and not the ledger. **Closed when** `--milestone R1 --step 1` writes this path,
`--closes R1/step-1` emits `Closes: R1/step-1`, and the report check reads
`docs/reports/R1/`; and when the search that found the other five is re-run over `scripts/`
without a pager, so a seventh site cannot hide behind `| head`.

**R805. `floatsim.froude_lambda` reaches the builder and NOT the dynamic scaling.** A
declared field, inside a declared range, that changes half the model.

```
cmd  grep -n "FROUDE_LAMBDA|froude_lambda" floatfea/post/forces_table.py
out  83:  FROUDE_LAMBDA = 50.0
     120: to_full_scale(block, "joint_multiplier_yaw_locked", FROUDE_LAMBDA)
cmd  inspect.signature(forces_table._lam_full_scale)
out  (lam_row: NDArray[np.float64]) -> NDArray[np.float64]      -- no lambda parameter
cmd  build at the declared lambda, and print the factor the dynamic path applies
out  config froude_lambda = 50 -> platform deck_mass 2500000.0, arm length 50.0
     config froude_lambda = 25 -> platform deck_mass  312500.0, arm length 25.0
     the dynamic multipliers are scaled by 50.0 in BOTH cases
     to_full_scale(ones, "joint_multiplier_yaw_locked", 25) = [15625 15625 15625 390625]
     to_full_scale(ones, "joint_multiplier_yaw_locked", 50) = [125000 125000 125000 6250000]
     ratio applied/correct at a declared lambda = 25 build = [8 8 8 16]
rule FL1(a): the deck reference "and optional overrides, declared and recorded in
     provenance"; CLAUDE.md: never assume a unit
```

`FROUDE_LAMBDA`'s declared range is `[1, 1000]`. A configuration declaring `25.0` builds
the geometry and the masses at scale 25 and scales every joint reaction as if at 50 —
**8x too large on force, 16x on the locked moment** — and `provenance()` prints
`froude_lambda: 25.0` into the CSV header and the report, so the artifact says the run was
at 25. This is the same hazard `_lam_full_scale`'s own docstring records being caught once
("the symptom was a PLAUSIBLE WRONG ANSWER rather than a crash"), now reachable from a
declared field with nothing refusing it. `pipeline.py`'s docstring enumerates four fields
that reach the model and two that are refused; `froude_lambda` is in neither list and is
the fifth.

Nothing in the suite can see it: the example declares `50.0`, `forces_table` hard-codes
`50.0`, and the two agree at exactly one point of a three-decade range. The only test that
touches the field —
`tests/unit/test_run_pipeline_refusals.py::test_provenance_records_every_declared_thing:253`
— asserts that it is *printed*, which is the half that makes the defect dangerous.

**Closed when** the scale the dynamic path applies comes from the configuration (a
parameter on `_lam_full_scale` / `compute_rows`), or a declared value other than the one
`forces_table` can honour is refused by name; and a test builds at two different declared
lambda and shows the applied factor following it.

**R806. The published artifacts under `results/R1/example/` drop the label blocks their own
numbers carry in `docs/`, and `cli.py`'s `LABEL` says they are in the run report when they
are not.** EZ0: anything under `results/` is a published deliverable.

```
cmd  grep -c '^#' docs/F4_member_forces.csv results/R1/example/member_forces.csv
out  docs/F4_member_forces.csv              17
     results/R1/example/member_forces.csv   11  (1 generic line + 10 provenance key-values)
cmd  grep -c '^#' docs/F6_utilisation.csv results/R1/example/utilisation.csv
out  docs/F6_utilisation.csv                12
     results/R1/example/utilisation.csv     11  (1 generic line + 10 provenance key-values)
cmd  for each caveat, grep results/R1/example/report.md
out  TENSION 0 / tension 0 / R739 0 / R740 0 / "UPPER BOUND" 0 / "upper bound" 0 /
     heading 0 / EX3 0 / R724 0 / R730 0 / PRELIMINARY 0 / total_max 0 / DZ5 1
rule floatfea/cli.py:31-35 -- "every assumption it rests on is listed in the run report"
```

What is published without them: **R739** (the `N` column is tension-positive, the convention
that, published the other way, "put every over-unity station on API 3.3.1 instead of
3.3.2"); **R740** (288 `total_max` and 288 `total_min` rows whose six components do not
occur together and from which a utilisation is an upper bound, shipped here with no warning
at all); **EX3/R724** ("all cases are heading 0 degrees. The heading dependence is
UNTESTED"); **R743** (`C_m = 0.85` is the LESS onerous of the two); **FA3**, **FA0**,
**FA1**, **R730**, **R741/R742**, and **"PRELIMINARY until F4 closes"**. The utilisation CSV
carries the governing `U = 1.71167` someone sizes steel against and none of its twelve
committed caveats.

The `LABEL` sentence is a CW0 claim about the code, published verbatim into all three
artifacts, and the grep above refutes it. **Closed when** the caveats a reader must act on
travel with the artifact that carries the numbers, and `LABEL`'s sentence is either true or
deleted.

**R807. The builder's own findings are dropped by the whole run path, including five that
say these bodies are not shippable.**

```
cmd  grep -rn "findings" floatfea/run/ floatfea/cli.py floatfea/post/forces_table.py
out  (no output)
cmd  Superstructure.findings for the DEFAULT descent vs for the shipped example
out  default descent (what the measure script builds) : 4 findings
     the example, f handed in by the config           : 9 findings, of which five read
       "<body>: the mass fraction is 0.75, handed in by the caller rather than taken from
        (0.75, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0), so `admissible()` was never consulted for
        it. This body is a MEASUREMENT, not one to ship."
cmd  grep -c "not one to ship|MEASUREMENT|handed in by the caller" results/R1/example/report.md
out  0  0  0
rule floatfea/model/platform.py:607-618, which writes that finding precisely so a caller
     cannot take an unladdered body for a shipped one
```

Declaring `f: 0.75` explicitly is physically identical to the descent — the example's
comment says so and it is true — but it sets `laddered=False`, which is what *creates*
these five findings. So the findings R1 newly provokes are exactly the ones R1 silently
discards, and `_check_material` re-derives the density one in its own words while the other
five vanish. Its re-derivation also has a narrower domain than the builder's: it fires on
`rho_eq > declared.rho`, so a configuration declaring `rho: 20000` would publish silently
where the builder still flags above-steel.

**Closed when** `floatfea run` surfaces `Superstructure.findings` in the report and in the
CSV headers, and the re-derived density note is either removed in favour of the builder's or
keyed on the same threshold.

**R808. `results/R1/example/report.md:20` publishes a doubled body prefix on the one line a
reader acts on.**

```
cmd  grep -n "^..U =" results/R1/example/report.md
out  20:**U = 1.71167** at `platform:platform:hub4_arm` ROOT, `T_full = 12.5 s`, ...
rule floatfea/cli.py:126-129 formats `{governing[body]}:{governing[member]}` while
     `member` already carries the body prefix
```

The identification of the governing member is malformed in the published artifact, and a
reader cannot grep for that string in either CSV. **Closed when** the line names
`platform:hub4_arm` and the golden test asserts the published string, not only the dict
fields.

**R809. A refused run writes every artifact first.** `floatfea/cli.py:201-208` places the
`required_section` / `truss_sizing` refusal AFTER the three writes and after the governing
line is printed.

```
cmd  floatfea run on a copy of the example with outputs.required_section: true
out  ... 1248 member-force rows in 71.5 s ... 32 checked stations
     floatfea: outputs.required_section / outputs.truss_sizing are FL2(b) and are not
       wired in R1 step 1 ... Refused rather than silently skipped.
     wrote .../member_forces.csv (1248 rows) / .../utilisation.csv (32 rows) / .../report.md
     governing U = 1.71167 at platform:hub4_arm ROOT
     EXIT CODE: 2
     files left by the REFUSED run: member_forces.csv 186958 B, report.md 3575 B,
       utilisation.csv 8280 B
     any of the three mentions the refusal: no
rule CLAUDE.md -- never let a validation failure degrade to a warning
```

"Refused rather than silently skipped" is what the message says; what the disk holds is a
complete, unmarked artifact set indistinguishable from a successful run, with the declared
`required_section` output absent and nothing recording that. A refusal that arrives after
its own side effects is a warning. **Closed when** the check runs before the pipeline — it
is knowable at `load_config` — so a refused run writes nothing, with the measurement that
the output directory is empty.

**R810. A physically unrealisable mass distribution runs to completion and publishes a
screen.** Solved in the weakening direction (EH4): the grid rises until a clean case trips.

```
cmd  build at f = 0.0, 1e-9, 0.5, 0.999999, 1.0 (MASS_FRACTION declared range [0, 1])
out  f = 0.999999  all four hubs and the platform PSD=False, rho_eq 15244.7 / 9527.9
     f = 1.0       the four hubs PSD=False, the platform PSD=True   -- non-monotone
     f = 0.0       member_mass 0.0 on every body, rho_eq = 0.0      -- massless members
     f = 0.5, 0.75 PSD=True everywhere
cmd  grep -rn "admissible|psd" floatfea/run/pipeline.py floatfea/cli.py
out  pipeline.py:290 psd_admissible=bool(admissible(body))
     cli.py:148      OK if entry.psd_admissible else FAILS
rule the golden test's own message: "a non-PSD remainder is not a body"
```

Nothing refuses it. A non-PSD remainder reaches the reader as the word `FAILS` in one cell
of a markdown table, beside a governing utilisation computed on it. And `f = 0.0` yields an
equivalent density of `0.0 kg/m^3`, two decades below the config's own `DENSITY` floor of
`100` — the schema bounds the declared NOMINAL and not the value the model uses. Before R1
no caller could reach a non-PSD `f`: the builder descended `MASS_FRACTION_LADDER` and
`admissible()` gated each rung. The configuration is what opened the range, and it opened it
without the gate. The non-monotonicity at `f = 1.0` is why a spot check would have missed
this.

**Closed when** a configuration whose remainder is not PSD, or whose members come out
massless, is refused by name with the body and the fraction — or the decision to run anyway
is recorded as a locked one and printed where the number is. Solve the boundary both ways:
the largest `f` that is PSD on every body and the smallest that is not.

**R811. Duplicate YAML keys are silently last-wins, which is the exact failure
`_reject_unknown` exists to prevent.**

```
cmd  load a configuration declaring one key twice
out  Fy: 355000000.0 then Fy: 275000000.0   -> ACCEPTED, cfg Fy = 2.75e+08
     platform: {f: 0.75} then {f: 0.30}     -> ACCEPTED, cfg f(platform) = 0.3
     code_check {K: 2.0} then {K: 3.0}      -> ACCEPTED, cfg K = 3.0
rule floatfea/run/config.py:113-127 -- "the reader sets `fy: 420`, the tool runs at 355,
     and the report carries a number nobody asked for. Spelling is part of the interface."
```

`yaml.safe_load` keeps the last duplicate. A misspelling is refused and a duplication is
not, though the duplication is worse: the reader sees `Fy: 355000000.0` on the line they
wrote and the tool runs 275. `Fy` happens to be saved by `_check_material`'s cross-check;
`f`, `K`, `Cm`, `d_outer` and `wall` are cross-checked against nothing. None of the 34
refusal tests covers the shape and section 4's table does not list it. **Closed when** a
duplicate key is refused naming the key and both values.

**R812. `load_cases.window_rule` is accepted, stored, and consumed by nothing.**

```
cmd  grep -rn "window_rule" floatfea/ examples/
out  config.py:234  window_rule: str = ""
     config.py:510  listed in _reject_unknown's known set
     config.py:562  window_rule=str(block.get("window_rule", ""))
     examples/platform12_placeholder.yaml:84  window_rule: "the committed window per case"
cmd  grep -c "window" results/R1/example/member_forces.csv results/R1/example/report.md
out  0  0
rule pipeline.py:8-28 -- "Two do not [reach the model] ... so they are CHECKED AND REFUSED
     rather than ignored"
```

It is in neither the reaching list nor the refused list: it reaches nothing, is refused by
nothing, and is not even in `provenance()`. A user writing `window_rule: "the peak 3
cycles"` gets the committed window and no word about it. Same class as `rho` and `G`, which
were handled. **Closed when** it is refused, consumed, or at minimum recorded in
provenance — and when `pipeline.py`'s enumeration is complete, which R805 also requires.

**R813. EG3's state (1) list is short by three names, and the report's trace proves
reproducibility rather than cause.** The report compares this tree against `e001aec` (F6b's
first-report commit) and finds the two FAILED lists identical. I reproduced that exactly —
and both commits are instances of THE SAME state, so the comparison cannot separate "caused
by the absent verdict" from "red in both trees for another reason". The control that does
separate them is a commit where a verdict exists:

```
cmd  worktree at e001aec, run the two report-guard files, comm against this tree
out  there 37 / here 37 / here-not-there (none) / there-not-here (none)
cmd  worktree at bd315a1 (a verdict EXISTS, report closed), the same two files
out  0 failed
cmd  comm -12 (this tree's 37) (bd315a1's reds)
out  (empty)  -- not one of the 37 is red where a verdict exists
```

So all 37 are verdict-dependent BY MEASUREMENT, EG3(i) is discharged, and **no red here is
CZ1 (iv)**. But three of them are on neither EG3 list and each needed its own run (R644's
discipline): `test_the_reported_CI_counts_are_not_all_zero` ("every CI row in step-1.md
reports zero passed and zero failed"), `test_the_report_carries_a_CI_SECTION`, and
`test_the_R507_cases_rule_as_measured[frames.txt]` — whose failure line mentions no verdict
at all (`_is_a_site('frames.txt')` is `True`, expected `False`) and which is nonetheless
green the moment a verdict exists. The EG3 lists are named in FF0, so this is FF0 class.

**Closed when** the three are on state (1)'s list, or the list's membership rule is stated
as "verdict-dependent, measured against a verdict-exists control" rather than enumerated.

## The five claims the report asked to have attacked - my rulings

**1. Byte-identity: VERIFIED, and the re-key is correct. Its stated justification is not.**

```
cmd  regenerate with the refactored script; diff and sha256 against the committed file
out  CSV IDENTICAL
     ed089b780e34db049059f671e1a09ed09d7ee679e48a4b4fcf97139e08258686  regenerated
     ed089b780e34db049059f671e1a09ed09d7ee679e48a4b4fcf97139e08258686  docs/F4_member_forces.csv
cmd  git diff a507baf..HEAD --stat -- docs/F4_member_forces.csv docs/F6_utilisation.csv
out  (empty)  -- the comparison target was not regenerated to match
cmd  python -m pytest -q tests/regression/test_r1_example_golden.py
out  8 passed in 70.45s
```

The move changed no number, and the baseline it is compared against is untouched, which is
the strong form of the claim. On the re-key, the many-build case the byte diff cannot reach:

```
cmd  eight sequential builds at eight sections; count distinct id(body.model) and retained
out  distinct ids over 8 sequential builds: 8        (8 = no id reuse)
     models held alive by the cache: 10
```

Correct: the entry holds the model, so the id cannot be recycled, and step 2 will not get
stale rotations. The REASON given at the site is refuted by one command and is closure item
C1: node coordinates do NOT move with the section, so the old `(body.name, member.label)`
key returned a numerically correct matrix for exactly the case the docstring names. The
re-key is still the right change — FL2(a) puts topology in the config, where coordinates
will move — but it is a precaution, not a repair, and the cache now retains every model
ever built.

**2. The rounding-boundary row: NOT a blocking defect. I rule with you.** The committed
`0.0738577` is the correct output of a documented two-stage path that writes six significant
figures and reads them back; the configured run is the more accurate of the two; the station
is at 7.4% of allowable and no decision rests on its sixth figure. Your weaker statement is
the honest one and it is sufficient: it does not matter whether other rows are AFFECTED by
the intermediate rounding, only whether any row's PUBLISHED DIGIT changes, and that is
measured at one of 32. The test is the right shape — it names the row, pins the difference
at one unit in the last published digit, reddens on a second differing row, reddens on a
different magnitude, and reddens if the row starts agreeing. Independently: 0 of 7488 force
cells differ at the shipped configuration.

**3. The one-third increase: refusing is correct, and no locked decision is reopened.**
FL1(a) lists the FIELD; EZ4 Q2 fixes its only admissible VALUE. A directive naming an option
does not overrule a Q&A that locked the option off, and a field whose refusal cites the
clause is a declared option, not an omission. The message names EZ4 Q2 and what to do. One
closure item only (C4): the refusal fires in `_utilisations` after a 67-second solve though
it is decidable at `load_config` — the same misplacement as R809, without R809's
consequence.

**4. The field ranges are NOT tolerances. I agree, explicitly, because the rule's wording is
absolute and the ruling needs to be on the record.** A tolerance in this repository is a
value against which a RESULT is compared, or one introduced to make two numbers agree;
CLAUDE.md's own list is convergence thresholds, comparison epsilons, small-number guards and
tier cutoffs. A `Bound` in `config.py` is the declared DOMAIN OF AN INPUT: no result is
compared against it, nothing is made to agree by it, and widening one can only admit a
configuration that was previously refused outright. It cannot turn a red into a green, which
is the property the prohibition exists to protect. They stay in `config.py`, and FL3(a)
wants them documented there. I verified nothing tolerance-shaped was added:

```
cmd  grep -nE "isclose|abs_tol|rel_tol|approx|2\*\*-|atol|rtol" over the five new/moved files
out  four hits, all the word "approximation" in prose
cmd  git diff d29bf6b..HEAD --stat -- floatfea/tolerances.py
out  (empty)
```

Both tolerances you removed before committing were right to remove: the implied-`nu`
`isclose` compared two declared constants with nothing to be approximate about, and the
residual is exactly `0.0` on all five bodies because the two halves sum to the whole. Note
R810 as the one place this ruling has a limit — a bound on a declared NOMINAL (`rho`) that
the model does not use does not bound the value the model computes.

**5. Section groups keyed by body name: not a finding for step 1.** Measured, per body:

```
out  platform D=3.000 A=1.5947 ; hub1..hub4 D=2.500 A=1.3119  (platform group changed alone)
     a group the deck does not have -> REFUSED naming it and the deck's bodies
     a group the deck has and the config does not -> REFUSED naming it
```

The per-group dict reaches each body correctly and both directions of the mismatch are
refused. See C8 for the two siblings that will break with it in FL2(a).

**And the three corrections you offered.** `hub4_arm` is right and `hub2_arm` was an artifact
of maxing a rounded deliverable; the golden's three-way assertion (published value, body and
station, plus hub4 ranked first at full precision and strictly ahead of hub2) is the correct
shape and does not pin a tie-break. The twelve test names in section 4's table all resolve
to a real `def` at the path given, checked mechanically. The FF0 repair is additive and
deletes no guard — I diffed `.claude/hooks/require-verdict.sh` line by line: `1e330cc` is
standalone, cites FF0, touches nothing under `floatfea/` or `tests/`, the label validator
still refuses `R1draft`, `F6ab`, `Freports`, `F6-draft`, `1` and the empty string, the tie
is still refused naming both paths, `m_body` survives only in a comment, and the widened
glob admits no non-plan file (`docs/milestones/*.md` yields exactly `R1.md` under the marker
grep). **Not a STOP.**

## The adversarial case, and what the gate detects

The step's gate carries its own failure. One variable moved, in process, against the
committed deliverable, and repeated once:

```
cmd  run the pipeline at wall = 0.1818 (1% thicker) on every group; compare all 7488
     published cells and the governing U against docs/F4_member_forces.csv
out  CONTROL unmutated              : 0/7488 differ, governing U = 1.71167     -> GREEN
     wall 1% thicker on every group : 2058/7488 differ, governing U = 1.69845  -> RED
       by basis: dynamic_max 491, dynamic_min 518, total_max 461, total_min 459,
                 total_instant 79, static 50 ; worst relative 1.458e+02
rule the force-cell and governing-U assertions in tests/regression/test_r1_example_golden.py
```

So the golden is live on the quantity the configuration most directly controls, and it is
live despite `rho_eq` being back-computed to hold `rho*A` invariant — the motion is mostly
in the dynamic bases, which is F6a's recorded rotary-inertia mechanism, with 50 static cells
moving too. The adversarial cases it is BLIND to are R805's (lambda agrees at the single
point the example sits on) and R810's (the shipped fraction is PSD, so no assertion in the
suite ever sees a non-PSD build).

## CI at the reviewed commit: UNAVAILABLE (not red, not green)

```
cmd  gh run list --commit 472bcd1 --json name,conclusion,workflowName
out  []
cmd  git ls-remote --heads origin | grep F3 ; git rev-parse HEAD
out  bd315a17...  refs/heads/F3
     472bcd1a...  (local)
```

No workflow ran on the reviewed commit, nor on any of the four in scope: they are not
pushed. This is NOT CK2's exhausted-allowance state — there are no started-but-unrun jobs,
no empty `runner_name`, no spending annotation; there is simply no run. Recorded as
unavailable rather than skipped over. The last run that executed is `bd315a1` (workflow CI,
`success`, 2026-10-12T05:47Z), and CK2's follow-up question has a non-empty answer:

```
cmd  git diff bd315a1..HEAD --stat -- tests/verification scripts .github
out  scripts/check_carried.py 12 +- / scripts/ci_section.py 12 +- /
     scripts/measure/member_forces_table.py 482 +------ /
     tests/verification/rung3/test_closure_evidence_exists.py 8 +-
```

So that green does NOT describe the tree under review — the 482-line extraction from the
deliverable-producing script is inside the gap. The step is judged on everything else, and
the three lint gates are green under my own run: `ruff check floatfea tests scripts` gives
`All checks passed!`, `black --check floatfea tests scripts` gives `146 files would be left
unchanged`, `mypy floatfea` gives `Success: no issues found in 42 source files`.

FL1(c) asks for a CI golden and the wiring is there: `tests/regression` runs in the `ladder`
job's rung-6 step (`.github/workflows/ci.yml:501`, `sh scripts/run_rung.sh
empty:tests/verification/rung6 full:tests/regression`), and `data/f4/dynamic_inputs.npz` is
tracked, so the golden is runnable on a clean checkout. It has simply never run.

## Corpus (EG4(e))

**The pause held; no batch, and no entry added.** R1 step 1 touches neither exception — not
F4's load-mapping gate and not EB6's label-provenance gate. I ran the recorded substitute
instead, both halves, and both produced blocking findings:

* **a continuum grid over the parameter space the decision rules guard** — `f` over
  `{0.0, 1e-9, 0.5, 0.999999, 1.0}`, `froude_lambda` over `{1, 25, 50}`, `d_outer` over
  `{2.5, 2.6..3.2, 3.0, 4.0}`, `wall` over `{0.18, 0.1818, 1.3}`, heading over
  `{0, 45, 360, 400}`, plus four duplicate-key shapes and the string / bool / NaN shapes.
  This produced R805, R810 and R811.
* **a regeneration check on a published deliverable** — regenerating
  `docs/F4_member_forces.csv` through the refactored script (sha256 identical) and comparing
  `results/R1/example/*` against the committed deliverables' label blocks. This produced
  R806, R807 and R808.

Twelve of the refusals in section 4's table I exercised myself against configurations the
implementer did not write; every one refused, and each message named the field, the value,
the range and the unit. The three holes above are not refusals that fail — each is a shape
with no refusal at all, which is why a grid over the declared domain found them and a list
of planted shapes would not have.

## Tolerances touched

**None, verified independently.** `git diff d29bf6b..HEAD -- floatfea/tolerances.py` is
empty. My own grep over `config.py`, `pipeline.py`, `cli.py`, `forces_table.py` and
`test_r1_example_golden.py` for `isclose|abs_tol|rel_tol|approx|2**-|atol|rtol` finds only
the word "approximation" in prose. The two the implementer removed before committing are
correctly gone and both replacements are exact comparisons. The 15 `Bound` constants in
`config.py` are declared input domains and not tolerances, ruled above under claim 4. One
cosmetic exception is C6.

## Closure items

Fixed once, in the step's closure commit; not re-reviewed item by item. C2 and C9 are FF0
class and belong in the next commit rather than the ledger.

* **C1.** `floatfea/post/forces_table.py:180-191` — the `_rotation` docstring's reason is
  refuted: "returns bodies with the SAME names at a different geometry" is false for a
  section change (node coordinates are identical across two builds at `D = 2.5` and
  `D = 4.0`, and the matrix is a pure function of the two end coordinates). The re-key is
  right; the justification should say it is unique by construction and that FL2(a) is what
  will move coordinates. Note also that the cache now retains every model built (10 models
  after 10 builds) under precisely the loop it was changed for.
* **C2.** `floatfea/run/pipeline.py:8-28` — the docstring enumerates four fields that reach
  the model and two that are refused. The true counts are five and two (R805, R812). It is
  prose a reader uses as a contract, so FF0 class alongside its code.
* **C3.** `tests/regression/test_r1_example_golden.py:190` — still reads "the station is at
  `U = 0.074`" after the report corrected that figure to `U = 0.0738576` elsewhere. Correct
  to two significant figures, so not false; inconsistent with the repair it belongs to.
* **C4.** The `one_third_increase` refusal fires in `_utilisations` after a 67-second solve
  though it is decidable at `load_config`.
* **C5.** `floatfea/post/forces_table.py` raises `SystemExit` in two places. Named in the
  report and correctly left out of a byte-identity commit; it belongs in the next one.
* **C6.** `floatfea/run/config.py:465` — `("m", -1.0e4, 1.0e4)` is an inline bound where the
  other fifteen are named module constants, so the lumped-mass position is the one field
  whose domain is not documented where the schema documents domains (FL3(a) will need it).
* **C7.** `floatfea/cli.py` has no test of any kind — 262 lines, FL1(b)'s deliverable, and
  the only file in the step with no coverage. R806, R808 and R809 all live in it. I am not
  asking for new apparatus: the two new test files cover `config.py` and `pipeline.py`, and
  the third file that shipped is the one nothing reads.
* **C8.** `_k_l_over_r` and `RunResult.section_properties` both take `body.members[0]` as the
  body's representative. True today (every body's members share one length: 25.0 on each hub,
  50.0 on the platform) and silently false under FL2(a)'s member list. `_sections_for`
  carries a note saying FL2(a) replaces it; these two do not, and `_rotation` is what that
  latency costs.
* **C9.** EG3's state (1) list (R813's three names). FF0 class.
* **C10.** `results/R1/example/utilisation.csv` repeats `utilisation` and `governing_clause`
  in trailing columns (`DictWriter` over the record's own keys), so the published screen has
  two columns carrying the same number under different headings.

## Next step opens when

Step 2 does not open. R804 is answered first, because nothing else can be recorded through
the sanctioned path until it is. Then, specifically:

1. **R805** — the scale applied to the dynamic multipliers follows the declared
   `froude_lambda`, or a value `forces_table` cannot honour is refused by name; with a test
   that builds at two declared lambda and shows the applied factor following it. Not a test
   that the value is printed.
2. **R806, R807, R808** — the artifacts under `results/R1/example/` carry the caveats their
   numbers carry in `docs/` (R739, R740, EX3/R724, R743, FA0, FA1, FA3, R730, R741/R742 at
   minimum); the builder's nine findings reach the report; the governing line names
   `platform:hub4_arm`; and `cli.py`'s `LABEL` sentence is true or deleted. Regenerated at
   the answering commit, not carried over (CP3).
3. **R809** — the `required_section` / `truss_sizing` check runs before the pipeline, with
   the measurement that a refused run leaves the output directory empty.
4. **R810** — a non-PSD remainder or a massless member is refused by name with the body and
   the fraction, and the boundary is solved in BOTH directions rather than sampled.
5. **R811** — a duplicate YAML key is refused naming the key and both values, with the three
   shapes above as the cases.
6. **R812** — `window_rule` is refused, consumed, or recorded; and `pipeline.py`'s
   enumeration is complete.
7. **R813 and C2 / C9** — the FF0-class items, in the next commit, not the ledger.

Everything FL1 asked for is present and the hardest part of it is right: the core moved
byte-identically against an untouched baseline, the example reproduces 7488 force cells and
31 of 32 utilisations exactly with the 32nd's cause isolated inside the test, the governing
`U = 1.71167` is confirmed on the correct arm, the twelve refusals all refuse with messages
a reader can act on, the gate reddens on a 1% section change, and the whole suite is green
outside a boundary state I measured to be verdict-dependent. What the ten findings have in
common is narrower than "the step is not done": with one exception they are about what the
tool SAYS about a run it has performed — a declared field that reaches half the model and is
reported as though it reached all of it, nine findings the builder wrote and the reporter
dropped, a label block that did not travel with its numbers, a refusal that arrives after
its own artifacts, a doubled prefix, a duplicate key accepted in silence. R1's whole subject
is a tool that someone else will point at a configuration nobody here has seen. On that
subject the output is the product, and FL1(a)'s "refusing with messages" is the deliverable
rather than the packaging.

The schedule is not at risk from this HOLD. Nine of the ten are small and local, and the
step's substance — the schema, the CLI, the extraction, the golden — stands.
