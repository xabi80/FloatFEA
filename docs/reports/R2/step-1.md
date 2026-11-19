# R2 step 1 — export (FL2(c), GJ4)

Answers: verdict 68 @ 8fe7fea9266c875be381aacf9d3eca720103f22c

*The newest verdict is the first entry of `docs/reviews/R2/step-0.md`, whose
`Reviewed commit:` line names `8fe7fea9266c875be381aacf9d3eca720103f22c` and which
`ed5b859` committed as the EQ0 follow-on. **The number is DERIVED**, because the reviewer
does not number its own entries, and the derivation is in §11a rather than here so it can
carry the command that produced it.*

*Measured against **GJ4**, which opened this step, and **GJ5(d)**, which asks for decision
items and measured results first, one screen, with the evidence in an appendix. Schedule:
GJ sets no date for step 1 and FR0 kept R1's scope at the cost of the date; nothing in this
step slipped against a date it was given, because it was given none. **One thing escalates
and it is §1.***

**ONE SCREEN (GJ5 d).**

| | |
|---|---|
| **Decision for Xabier** | the committed npz regenerates **bit-identically at numpy `2.4.0` with the thread counts UNPINNED**, and at no other configuration measured — pinning the threads breaks it, and so does the lock's own numpy `2.4.4`. `2.4.0` is a **yanked** release and `floatfea export` pins the threads by design. **And the difference does NOT reach a published number**: the tool's own export gives the same governing utilisation, member, station, period and clause as the golden (§A4). **§1 states three options and takes none** — FQ3 forbids the re-baseline without your ruling |
| `floatfea export` produces the file from a FloatSim solve | **holds** (§3) |
| FL2(c)'s heading refusal fires, against the dataset's own covered set | **holds** (§4) |
| exporting the reference run reproduces the golden bit-exactly | **fails as the command runs it; the cause is now known exactly** (§1, §A2) |
| `floatfea run` gives `U = 1.71167` | **HOLDS on the exported file too** — same value, member, station, period and clause, although 36 of its 100 arrays differ from the golden. The round-off does not reach a published number (§A4) |
| R1243, carried in blocking by GJ4 | **answered** — the chaining is stopped in both jobs, the guard asserts it, the CI section names skipped steps (§8) |
| new this step | `floatfea/floatsim_env.py`; the **config key GI3(e) asked for in its own words** and step 0 did not build, as the two worktree keys R1208 split it into plus GJ1's `venv`; 52 test rows; four self-rulings |
| found in passing, carried to step 2 | a **GI1 violation**: `run_floatsim_design_waves.py` writes into the pinned worktree (§5a) |

*Every figure in that table is measured in the section it names, and nothing is measured
here.* The table is a map, not evidence.

```
claim  the sections this table points at, and that each carries its own measurement
cmd    grep -n "^## \|^claim " docs/reports/R2/step-1.md | head -40
out    each of §1, §3, §4, §5a, §5b, §8, §A1, §A2 opens a `claim / cmd / out` block;
       §2 and §7 carry one beneath their own table; §6 carries one for its counts
rule   `CLAUDE.md` § "Every claim carries its command": a claim without its command is
       not written.
judge  The map above repeats figures that are measured elsewhere in this file. It exists
       because GJ5(d) asks for the decision items first and one screen, and a reader who
       stops after this table should get the dispositions and know where each was taken.
```

---

## 1. FOR XABIER — the cause is found, and it is TWO conditions, neither of them the lock

**GJ1 ruled: restore the lock, do not re-base.** The lock is restored exactly, and it was
not what moved the file. **The golden is recoverable, at exactly one configuration: numpy
`2.4.0` — a YANKED release — with the thread count left unfixed.** Pin the threads, or move
to the lock's own numpy `2.4.4`, and it does not reproduce.

```
claim  which configurations regenerate the committed npz and which do not
cmd    scratch/one_case_probe.py -- export_case(10.0, 0.01) against case0/* of the
       committed npz, under SIX environments; max|a-b| / max|a| per array
out    cell numpy threads   coretype exact differ  accel      contrib/lam  resid_control
       A    2.4.4 pinned 1  Haswell    10     6   8.774756e-14 3.028683e-15 1.109519e-09
       B    2.4.4 pinned 1  unset      10     6   8.774756e-14 3.028683e-15 1.109519e-09
       E    2.4.0 pinned 1  Haswell    10     6   8.774756e-14 3.028683e-15 1.109519e-09
       H    2.5.4 pinned 1  Haswell    10     6   6.367170e-14 3.749798e-15 1.115298e-09
       G    2.4.4 UNPINNED  unset      10     6   6.652617e-14 4.326690e-15 1.109519e-09
       F    2.4.0 UNPINNED  unset      16     0        0            0            0
rule   Q8: a regeneration either reproduces the committed file or it does not; there is
       no tolerance on that comparison.
judge  **TWO VARIABLES MATTER AND THE GOLDEN NEEDS BOTH.** E -> F moves the thread pins
       alone and goes from six differing arrays to none. F -> G moves the numpy PATCH
       version alone, `2.4.0 -> 2.4.4`, and goes from none to six. So the committed file
       requires numpy 2.4.0 **and** an unpinned thread count, together.
       **AND PINNING NARROWS THE VERSION SENSITIVITY WITHOUT REMOVING IT.** A, B and E
       agree to every printed digit across numpy 2.4.0 and 2.4.4 and two kernel settings.
       **Cell H is what stops that being "pinning makes it version-independent"**: numpy
       2.5.4 PINNED differs from all three. Pinning buys agreement across a numpy PATCH
       release and not across a minor one, and F remains the only configuration that
       reproduces the golden.
```

**THE `worst` COLUMN ALONE WOULD HAVE HIDDEN THIS, AND IT NEARLY DID.** `resid_control`
reads `1.109519e-09` in A, B, E **and** G — identical to seven figures — because a residual
is a difference of near-cancelling terms and its relative scale is set by the cancellation
rather than by the drift. A table reporting only the worst value would have shown G as
indistinguishable from the pinned cells, and the conclusion drawn from it would have been
that the libraries are eliminated. **That is the conclusion the first version of this
section published**, on A, B and E alone, before cell G existed; it is wrong and this is
the correction. Reading the physical channels separately is what separates them.

**Three things follow, and the third is the decision.**

**(i) R1225's PUBLISHED DIAGNOSIS IS HALF RIGHT, WHICH IS WORSE THAN WRONG.** Its comment
in `scripts/export_f4_dynamic_inputs.py` — mine — says the ONE variable that moved was
`constraints-dev.txt`'s numpy/scipy pin. The pin IS a variable that moves the file: F and G
differ by the numpy patch version alone. What the comment gets wrong is "one". Step 0
reached it from a correct historical ablation (`cfb76ff` green, `9e1092a` red, threads
unpinned on both sides) and then measured today's red **with the threads pinned**, putting
a second variable into a cell meant to have one. The comment is corrected in this step to
name both, and to say what pinning actually buys: agreement across a numpy PATCH release
and not across a minor one.

**(ii) GJ1's PREMISE WAS ALSO NOT THE RIGHT ONE, AND IT IS WORTH STATING SEPARATELY.** HSP's
`requirements-lock.txt` is HSP's *test* environment, not the environment the golden was made
in.

```
claim  how far the lock is from the interpreter the golden was produced under
cmd    FLOATFEA_HSP_RUNS=... python scripts/export_f4_dynamic_inputs.py --covered-headings
out    REFUSED: cannot read the BEM dataset's covered headings -- this interpreter does
       not satisfy 17 of the lock's 39 pins.
         certifi 2026.7.22 / 2026.4.22      click 8.3.2 / 8.3.3
         hypothesis 6.152.1 / 6.170.0       pydantic 2.13.2 / 2.13.3
         pytest 9.0.3 / 9.1.1               ruff 0.15.11 / 0.17.1
         scipy 1.17.1 / 1.18.1              xarray 2026.7.0 / 2026.4.0   ... and 9 more
rule   GJ1: "Build the FloatSim run environment from HSP-runs/requirements-lock.txt
       exactly."
judge  Seventeen of thirty-nine, and `xarray` -- which reads the BEM `.nc` -- is one of
       them. The dev interpreter is what produced the golden, so "restore the lock" and
       "restore the environment the golden was made in" were never the same action. The
       refusal that prints this is itself a step-1 deliverable (§3): it is the preflight
       SR-76 asks for, and it names every pin rather than the first.
```

**Restoring the lock was reasonable and it did no harm** — the locked venv is strictly
better for GI1, because it carries no `floatsim` at all (§5b) — and it did not clear the
FQ3 reds, because it was never the same action as restoring the environment the golden was
made in.

**(iii) THE DECISION. The golden needs numpy 2.4.0 AND an unpinned thread count, and that
pair is not a configuration anyone would choose.** `floatfea/determinism.py` says why in
its own first paragraph: reduction order varies with thread count, so a floating-point sum
is not bit-reproducible unless the count is fixed. The measurement says the same thing
from the other side: the two unpinned cells disagree with each other over a numpy PATCH
release, while three pinned cells agree across that same patch release and across two
kernel settings. **Pinning is the more stable of the two and the golden is not in it** —
and it is not fully stable either, because the fourth pinned cell, at a numpy MINOR
release, disagrees with the other three. `floatfea export` pins, which is correct going
forward and is exactly what makes it unable to reproduce this particular file.

**And numpy 2.4.0 is a YANKED release.** `pip install numpy==2.4.0` prints
`Reason for being yanked: Backward compatibility bug`. Option 2 below therefore does not
just mean "stop pinning" — it means pinning the toolchain to a withdrawn wheel in order to
keep a file reproducible.

| option | what it costs | what it buys |
|---|---|---|
| **1. Regenerate the golden pinned**, recording the thread counts and the kernel in the provenance (both blocks now exist) | every figure downstream of the npz is re-based, and **FQ3 forbids this without your ruling** — but §A4 measures what that re-base actually moves, and the answer is nothing a reader sees: the same governing utilisation at the same member, station, period and clause | the file becomes reproducible, and GI5 step 2's bit-identical zero-change test becomes a test that can actually pass. **This is the option the measurements point at** |
| **2. Keep the golden**: stop pinning the threads AND pin numpy to `2.4.0` | both are needed and `2.4.0` is **yanked for a backward-compatibility bug**; the gate then stays green on this machine and nowhere else, and GI5 step 2's zero-change test becomes bit-identity between two unpinned runs, which nothing guarantees | nothing is re-based |
| **3. Keep both and retire the bit-exact comparison** in favour of a declared tolerance | a tolerance where Q8 says there is none, needing a written physical or numerical justification, and `CLAUDE.md` rejects one in the same commit as the code it rescues | the two configurations coexist |

**`R1223` and `R1225` are the two findings this section answers**, and they are answered
by being re-escalated with the cause measured rather than by being closed. R1225 is the
one whose own published comment was wrong; R1223 is downstream of it.

**I have not taken any of them.** FQ3's standing ruling is *"if the golden moves under these
pins, STOP and report rather than re-baselining"*, and nothing in this step re-based
anything:

```
claim  the committed npz is byte-identical to what was there, and so is the pre-move copy
cmd    sha256sum data/f4/dynamic_inputs.npz <...>/buoy/FLOATFEA/data/f4/dynamic_inputs.npz
       diff <(json.dumps(this provenance, sort_keys)) <(json.dumps(that one))
out    dea555d933fb9fd088213896f9ad38fd891f71dd8fab1d8381aa47fa57797f86  this tree
       dea555d933fb9fd088213896f9ad38fd891f71dd8fab1d8381aa47fa57797f86  the pre-move copy
       provenance diff           (empty)
rule   FQ3.
judge  The golden has not moved and nothing in this step moved it. The pre-move checkout
       at `.../buoy/FLOATFEA`, left behind when the repository moved to `C:\devloatfea`,
       carries the same bytes and the same sidecar.
```

**§A4 IS THE MEASUREMENT THAT MAKES THE CHOICE CHEAP, AND IT IS TAKEN.** The tool's own
export differs from the golden in the same way these cells do — every input bit-identical,
every solve output differing at round-off — and **`floatfea run` on it publishes the same
governing utilisation, at the same member, station, period and clause.** So the difference
the bit-exact gate refuses on **does not reach the number anybody sizes steel against**.
That is the argument for option 1: what would be re-based is round-off below published
precision, and what is bought is a file that regenerates. §A4 carries the figures.

## 2. What step 1 built, and the gate GI5 sets for it

**GI5 step 1's gate has FOUR clauses and they are reported separately, because three hold
and the fourth is what §1 is about.** "Two halves" is how this paragraph read while the
last row was still pending; the gate has always had four.

| half | state |
|---|---|
| `floatfea export` produces the dynamic-inputs file from a FloatSim solve | **holds** — §3 |
| the heading refusal at `cli.py` gets its input and fires | **holds** — §4 |
| exporting the reference run reproduces the golden bit-exactly | **FAILS** — §1, escalated |
| `floatfea run` on that output gives `U = 1.71167` | **holds** — §A4 |

```
claim  the suite behind the three halves that hold
cmd    pytest tests/unit/test_cli_export_refusals.py
              tests/unit/test_floatsim_env.py
              tests/unit/test_export_sensitivity_note.py
              tests/regression/test_export_config_matches_the_placeholder.py
              tests/unit/test_hsp_worktree_resolution.py  -q -p no:randomly
out    62 passed
       -- 16 + 23 + 4 + 9 + 10, the last of which is R1220's pre-existing file.
       **THE FIRST VERSION OF THIS BLOCK PUBLISHED `57`, AND A COUNT OF THIS REPORT'S
       OWN `claim` BLOCKS THAT WAS STALE WHEN IT SHIPPED.** The self-referential count
       is dropped rather than corrected: a figure that counts the file it is written in
       goes stale on the next edit to that file, which is CP3 with no way to satisfy it.
```

---

## 3. `floatfea export` — the configured front end over the one producer

**It drives `scripts/export_f4_dynamic_inputs.py` rather than reimplementing it, and that is
the step's one architectural decision.** GI5 step 1's acceptance is that the export
*reproduces the golden*. A second implementation would have to be bit-identical to the
first by luck; driving the engine that produced the golden makes it bit-identical by
construction. And R2 step 0's single recurring defect was one predicate with two readers
diverging — R1221, R1240, R1250, R1256, R1261, each needing the same repair twice — so a
second copy of the solve path is the shape with the worst record in this repository.

```
claim  the size of the implementation a second copy would have to match
cmd    wc -l scripts/export_f4_dynamic_inputs.py scripts/report_joint_reactions.py
out    758  scripts/export_f4_dynamic_inputs.py
       524  scripts/report_joint_reactions.py
      1282  total
rule   the acceptance is bit-exact (Q8), so a second implementation has to agree with the
       first to the last bit of every array.
judge  1282 lines across the two, and the engine's own test coverage is the gate's. A
       second copy would have to be bit-identical by luck; driving the one that produced
       the golden makes it bit-identical by construction.
```

What the command adds is what a script cannot: a validated configuration, the FL2(c)
heading refusal against the dataset's own covered set, and GJ1's locked environment.

```
claim  the command resolves both paths, prints what it resolved, and hands the engine one
       --period per declared case
cmd    python -m floatfea.cli export examples/platform12_export.yaml
out    floatfea export: platform12_export.yaml
         pinned worktree C:\Users\xlama\OneDrive\Documents\buoy\HSP-runs  (tag
                         floatfea-ref-1, 25de7ce)
         locked env      C:\dev\floatfea\.venv-floatsim\Scripts\python.exe
         heading         [0.0] deg, covered by the BEM dataset
         periods (full)  [10.0, 12.5, 14.0, 15.0, 16.2, 20.0]
rule   GI5 step 1: "`floatfea export` produces the dynamic-inputs file from a FloatSim
       npz" -- read by the locked plan §2d as "from a FloatSim SOLVE", because the npz is
       the OUTPUT and no FloatSim-written npz exists here. GJ4 confirmed the reading by
       opening the step unconditionally and making GJ1's acceptance a solve.
judge  Both paths are resolved by the same table and printed, so a run cannot be
       attributed to the wrong worktree afterwards. §A1 has the full argv.
```

**Two paths, one decision table, and it is now ONE function rather than two copies.**
`hsp_pin.resolve_declared_path` carries the table — declared key, then environment
variable, then default; a source that is **set and wrong refuses** (R1214); a **relative**
value anchors to the repository root and never the cwd (R1219). `worktree()` calls it and
`floatsim_env.venv()` calls it. The three defects R1220 found inside that table in step 0
— R1213, R1214, R1219 — were each *an input accepted and used other than as declared*, and
factoring it is what stops the venv becoming a second implementation for them to recur in.

```
claim  `worktree()`'s behaviour did not change when the table was factored out
cmd    pytest tests/unit/test_hsp_worktree_resolution.py -q -p no:randomly
out    10 passed
rule   R1208's closing condition -- the three DS0 refusals are still seen to fire -- and
       R1220's file is what says the table still behaves.
judge  **AND ONE OF THE TEN CAUGHT THE REFACTOR.** The two refusals differed by one word
       -- "the HSP runs worktree" against "the PINNED HSP runs worktree (tag ...)" -- and
       collapsing them to one label went red on the missing word. That is the test doing
       its job: a refusal's wording is what somebody reads at 2 a.m., and a refactor is
       not a licence to reword it. The function now carries two labels.
```

### GI3(e)'s config key, which did not exist and was named in a docstring anyway

```
claim  no production call site passed `declared`, while the docstring named a config key
       the schema would have refused
cmd    grep -rn "worktree(" --include=*.py floatfea scripts tests | grep -v "def worktree"
       grep -n "worktree_runs" floatfea/run/config.py
out    every production call is `hsp_pin.worktree("runs")` or `("stable")` with no second
       argument; the only sites passing `declared` are in
       `tests/unit/test_hsp_worktree_resolution.py`
       worktree_runs in config.py   -> no match
rule   GI3(e), in its own words: "Make it a config key with an env-var fallback." CW0:
       prose in the source tree is a test, a triple, or deleted.
judge  R2 step 0 built the env-var half and the default. The KEY did not exist, and
       `hsp_pin.worktree`'s docstring named it -- "`declared` (a config key,
       `floatsim.worktree_runs` / `floatsim.worktree_stable`)" -- so the first arm of the
       table was reachable only from `tests/`, under a sentence describing a key nobody
       could write, and `_reject_unknown` would have refused one. GJ1 was about to add a
       second copy of the same false sentence for the venv. **Three optional keys are
       added to the `floatsim:` block** (`worktree_runs`, `worktree_stable`, `venv`),
       which is smaller than a paragraph explaining a dead branch and is what the
       directive asked for. Recorded as SR-78.
```

**And the resolved paths are passed DOWN to the child, which the first version did not do.**
The child resolves both again for itself — `floatsim_env.lock_path()` asks
`hsp_pin.worktree("runs")`, and `report_joint_reactions.HSP_RUNS` is a module-level constant
evaluated at the child's import, before any configuration is read. A config key reached the
parent and nothing else, so a configuration that declared a worktree and set no environment
variable had the child fall through to the default: a refusal on a machine without one,
and on a machine **with** one, a different tree from the one the configuration names. That
second case is FR1's second head and it is silent. Held by
`test_the_RESOLVED_worktree_and_venv_REACH_THE_CHILD` and its inverted sibling.

---

## 4. FL2(c)'s heading refusal, reachable for the first time since R1

`cli.py` carried this sentence for the whole of R1 and it was right: *"hard-coding a covered
set here would be FloatFEA asserting a fact about HSP's datasets that nothing in this
repository can check."* What changed at GJ1 is that FloatFEA now has an interpreter with
`capytaine` and `xarray` in it, so the fact can be **asked for**.

```
claim  the covered set comes from HSP's own reader, and an uncovered heading refuses by
       name before any solve
cmd    sed 's/headings: \[0.0\]/headings: [45.0]/; s/heading: 0.0,/heading: 45.0,/' \
         examples/platform12_export.yaml > /tmp/45.yaml
       python -m floatfea.cli export /tmp/45.yaml
out    floatfea: load_cases.headings asks for [45.0] deg, which the BEM dataset does not
       cover. It carries [0.0] deg. Every missing heading is named above rather than the
       first one, because a reader fixing a configuration needs the whole list; and the
       comparison is exact, because a heading is a declared input -- exporting 44.9 deg
       for a declared 45 would publish an envelope for a sea state nobody asked for.
rule   FL2(c), and the locked plan's step-1 row AS IT STOOD AT THE LOCK: "The heading
       refusal at `cli.py:1279` gets its input and fires." The line number is the plan's
       and is quoted rather than re-derived -- the refusal moved when it was replaced by
       the run, so `cli.py:1279` names something else today.
judge  **IT FIRES, AND THE `[0.0]` IN THAT MESSAGE WAS READ OUT OF THE PINNED `.nc` BY
       `floatsim.hydro.readers.capytaine.read_capytaine`** -- not from a constant here.
       Asked of HSP's own reader rather than of the file, because that reader sorts the
       headings and converts radians to degrees, and a second interpretation of the same
       `.nc` in this repository would be a second reader of one predicate. It also
       confirms §2b of the plan from the dataset's own side: the pinned database is
       single-heading, so R2 is a single-heading loop.
```

**The refusal is TIMED, not just present.**

```
claim  what a heading check costs if it fires after the solve rather than before it
cmd    grep -n "ONE D4 ITERATION" docs/reports/R2/step-0.md
out    :158  **ONE D4 ITERATION IS 26 MINUTES, NOT 74.**   (measured at :150 as
             "--check exit 1, wall 25 min 56 s", six cases, one heading)
rule   GI3(b), measured in step 0 and not re-measured here.
judge  So a heading check that fired after the solve would charge most of an hour for a
       typo, and one that fired after the WRITE would publish a file labelled with a
       heading nobody can produce.
       `test_the_heading_refusal_fires_BEFORE_the_engine_is_invoked` asserts the engine is
       not invoked at all.
```

**And an ABSENT heading key is refused, which is the case §2b of the plan measured.** No
configuration in this repository declared a heading, so GI4 D4's "every heading in the R1
config" was unrepresentable. `refuse_uncovered_headings((), covered)` returns without
raising — correctly, because for `floatfea run` an undeclared set means "do not check" —
so `export` is where the empty set has to be an error rather than a skip.

---

## 5. Two findings this step turned up that are not about `export` itself

### 5a. A GI1 VIOLATION in shipped code: FloatFEA writes into the pinned worktree

GI1 authorises the runs and in the same breath forbids this: *"It is read-only on HSP
source. Every output goes to FloatFEA's own run folder, never into the worktree."*

```
claim  `run_floatsim_design_waves.py` writes its case files INSIDE the pinned worktree
cmd    grep -n "OUT" scripts/run_floatsim_design_waves.py
       git -C <HSP-runs> status --porcelain
out    :59   OUT = STUDY / "floatfea_design_waves"
       :157  OUT.mkdir(parents=True, exist_ok=True)
       :202  path = OUT / f"case_{tag}.csv"
       ?? studies/platform-12buoy/floatfea_design_waves/
rule   GI1: every output goes to FloatFEA's own run folder, never into the worktree.
judge  **A LIVE VIOLATION, AND IT WAS DORMANT UNTIL GI1.** Running FloatSim was banned
       before GI, so the write path never executed under the current rules; GI1 authorises
       the run and forbids the write in the same clause. The script has a DS0 refusal for
       `HSP-stable` and writes freely into `HSP-runs`. Six `case_*.csv` from 27 September
       are sitting in the pinned tree now.
       **It is not a wrong number and it does weaken a provenance claim.** The files are
       UNTRACKED, so `git describe --dirty` still reads `floatfea-ref-1` -- which is what
       `_hsp_tag()` writes into every provenance sidecar. A tree carrying FloatFEA's output
       reports as clean.
       **Step 1 does not reach that path**: the engine solves through
       `report_joint_reactions.solve_one`, in memory, and `EXPORT` is read-only at `:121`
       (`EXPORT.glob("case_*.csv")`). So this is carried to step 2, where the FloatSim
       invocation is the subject and GI1's "own run folder" is part of the design, rather
       than repaired here beside an export that does not use it.
```

### 5b. The `floatsim` import resolves by CALL ORDER, and the locked venv removes the fallback

```
claim  in the system interpreter a bare `import floatsim` lands 121 commits past the pin,
       and the same import with the worktree on `sys.path` first lands on the pin
cmd    python -c "import floatsim; print(floatsim.__file__)"
       python -c "<worktree first>; import floatsim; print(floatsim.__file__)"
       .venv-floatsim/Scripts/python.exe -c "import floatsim"
out    system, bare           -> ...\HSP_code\floatsim\__init__.py
       system, worktree first -> ...\HSP-runs\floatsim\__init__.py
       locked venv, bare      -> ModuleNotFoundError: No module named 'floatsim'
rule   GI1: FloatSim runs "from the pinned HSP worktree (tag floatfea-ref-1)".
judge  The system interpreter carries an EDITABLE INSTALL of `floatsim` pointing at
       `HSP_code`, which `git describe` reads as `floatfea-ref-1-121-g71ed278-dirty`. Its
       `_EditableFinder` sits AFTER `PathFinder` in `sys.meta_path`, so which tree answers
       is a property of call order rather than of any declaration.
```

```
claim  the two trees are not numerically interchangeable on the path this milestone uses
cmd    diff -rq <HSP-runs>/floatsim <HSP_code>/floatsim | grep -v __pycache__
       git -C <HSP_code> log --oneline -1 -- floatsim/hydro/retardation.py
       git -C <HSP_code> merge-base --is-ancestor 9fb5b33 25de7ce
out    9 files differ: bodies/joints.py driver.py hydro/morison.py hydro/retardation.py
         io/deck.py mooring/catenary_analytic.py solver/equilibrium.py solver/newmark.py
         waves/kinematics.py
       3 files + 1 directory only in HSP_code; 0 only in HSP-runs
       9fb5b33 2026-08-26 fix: trapezoidal radiation convolution (was rectangular ->
         inflated damping)
       merge-base --is-ancestor  ->  FALSE (the pin PREDATES the fix)
rule   the npz path imports `RadiationConvolution` directly
       (`report_joint_reactions.py:294`, `export_f4_dynamic_inputs.py:228`,
       `scripts/measure/g41_dynamic.py:256`).
judge  Nine differing source files, one of them a first-order-in-`dt` change to radiation
       damping that the pin does not carry. **The first figure I wrote here was "eleven",
       from reading the diff rather than counting it**: 9 differ, 3 are additions and
       `validation/cases` is a directory.
       **NO PUBLISHED NUMBER CAME FROM THE WRONG TREE.** The committed provenance reads
       `floatfea-ref-1  (HSP-runs)`, and in every real run the solve imports first --
       `solve_one` inserts the worktree at `sys.path[0]` before its first `floatsim`
       import, and `_hsp_tag()` runs at `main()` AFTER the cases. A guarantee that holds by
       call order is FR1's second head, so step 1 makes it a refusal
       (`floatsim_env.refuse_unless_declared_worktree`, called from `solve_one` so every
       caller reaches it) and the locked venv removes the second tree entirely.
```

---

## 6. What else moved, each with its reason

* **`floatfea/floatsim_env.py`** (new) — GJ1's three clauses: resolve the venv, refuse
  unless this interpreter satisfies every pin in the lock, record the path and the lock's
  `sha256`. 23 rows in `tests/unit/test_floatsim_env.py`, run in BOTH environments because
  one assertion in the first draft depended on which one ran it.
* **`hsp_pin.resolve_declared_path`** — the decision table, factored once rather than
  copied for the venv. §3 has the measurement.
* **`determinism.CANONICAL_CORETYPE`** — `"Haswell"` had two readers (`ci.yml` and
  `scripts/regen_figures.py`) and this step needed a third, so the Python side is
  single-sourced. `tests/test_ci_canonical_environment.py` holds `ci.yml` against
  `docs/milestones/F2.md`; **nothing holds this constant against either**, and closing that
  needs an assertion, which is new apparatus under the freeze GI2 carries from GA1. Ledger
  row, stated in the docstring.
* **`docs/USER_GUIDE.md` §5** — the `floatfea export` subsection quoted the old refusal and
  said "today it refuses". It is rewritten, with both surviving refusals' output pasted from
  a real run, and SR-41's ledger row is closed by the string's removal rather than by a
  decision (SR-77).
* **`examples/platform12_export.yaml`** (new) — the placeholder with one block changed, held
  to it by `tests/regression/test_export_config_matches_the_placeholder.py` so the two
  cannot drift. The export must reproduce a file produced at the placeholder's inputs, so a
  difference in any block the solve reads would make that comparison a coincidence.
* **`docs/milestones/R2.md` §2d** — marked superseded (BP0): its `cmd` no longer prints what
  its `out` records, because step 1 replaced the refusal it measured.
* **`scripts/export_f4_dynamic_inputs.py`'s bit-exact refusal** — it printed a count of
  differing arrays and nothing a reader could act on. It now names the two conditions the
  comparison is sensitive to and **whether the file it compared against records them**;
  the committed sidecar predates R1225(ii)'s block, so it records neither, and that is
  printed rather than left to be discovered. Extracted into `sensitivity_note()` so it can
  be tested: the branch it lives in costs 25 minutes of FloatSim to reach, so twenty-five
  lines of message-building would otherwise have shipped unread.
* **A COMMITTED GOLDEN IS NOT OVERWRITTEN WITHOUT SAYING SO.** The shipped export
  configuration targets the committed location — that is what makes `--check` compare
  against the golden — so leaving `--check` off silently re-baselined
  `data/f4/dynamic_inputs.npz`, the file FQ3 has a live escalation about. The engine now
  refuses when the target is TRACKED, names `--check` for the person who meant to compare
  and `--allow-regenerate` for the person who meant to re-baseline and must then justify
  it in a closure artifact. The question asked is `git ls-files --error-unmatch`, not a
  prefix test on `data/`: a scratch export outside the repository and a new destination
  inside it are both untracked and both ordinary. Three rows, one per direction.
  **`floatfea export` does not expose `--allow-regenerate`**, so the user-facing command
  cannot re-baseline a committed file at all; a deliberate regeneration goes through the
  engine directly and is visible as such in a shell history. That is the right default
  and it costs step 2 nothing, because a run writes into its own untracked run folder.
* **AND A THIRD, FOUND BY READING THE MEASUREMENT'S OWN LOG.** `_cmd_export`'s banner —
  which worktree, which interpreter, which heading — was printed without `flush=True`.
  Python line-buffers to a terminal and BLOCK-buffers to a file, so with the output
  redirected, which is how a run this long is actually taken, the parent's six lines sat
  in a buffer until the process exited while the child's case headers appeared at once.
  A reader watching the log saw a solve under way and nothing saying what it was solving
  against. The engine's own prints already carried `flush=True`; the command's did not.
* **A SECOND DEFECT THIS STEP INTRODUCED, WITH A MEASURED CONSEQUENCE.**
  `tests/unit/test_cli_export_refusals.py` writes its scratch configurations into
  `examples/` — it has to, because a run configuration's relative paths resolve against
  its own directory — and its cleanup fixture globbed `tmp_*.yaml`. `examples/` is a
  tracked, shared directory, so the sweep deleted **two scratch configurations a
  25-minute measurement was running against at the time**, and nothing said why: the file
  was simply absent when the second command looked for it. A fixture that cleans up by
  PATTERN cleans up by guess. It now records what it wrote and removes exactly that,
  which is the same distinction `_is_tracked` draws in the engine. The proof is that
  `tmp_run_exported.yaml`, which belongs to the measurement and not to the tests,
  survives a full run of the file, and a decoy with a matching name is now a test row of
  its own.
* **A DEFECT THIS STEP INTRODUCED AND THIS STEP FIXED.** `--out` made the export's
  destination configurable, and the provenance's `npz.path` was a literal
  `"data/f4/dynamic_inputs.npz"` — true for as long as that was the only place the script
  could write. Every export outside `data/f4` would have shipped a sidecar naming a file
  it is not beside, which is FR1's second head inside the provenance itself. It now
  records the path it wrote to: repository-relative under the root, so the committed
  file's own field does not move, absolute outside it. Two rows in
  `tests/unit/test_export_sensitivity_note.py`, one per direction. **Found by reading my
  own diff for what the `--out` flag reaches, rather than by a test**, which is why it is
  listed here as a defect and not as a feature.
* **`docs/directives/GJ.md`** — GJ recorded verbatim under FP0, first commit of the turn,
  with `GH.md` and `GI.md` backfilled into `docs/directives/README.md`: both existed, both
  were cited as the governing rule, and neither had a provenance row.
* **`docs/digests/2026-11-18.md`** — the day's digest (GA4), one screen.

```
claim  what this step added to the suite, and the self-rulings it recorded
cmd    pytest <the five files below> --collect-only -q | grep -c "::"
       grep -c "^\*\*SR-" docs/directives/FZ.md
out    tests/unit/test_floatsim_env.py                             23
       tests/unit/test_cli_export_refusals.py                      16
       tests/regression/test_export_config_matches_the_placeholder  4
       tests/unit/test_export_sensitivity_note.py                   9
       tests/unit/test_hsp_worktree_resolution.py (pre-existing)   10
       lines matching `**SR-` in FZ.md                             82
                      -- MORE THAN THE NUMBER OF SR IDS: SR-70 carries two headings,
                         one for the ruling and one recording that GF3 (b) closed it.
                         The highest id is SR-78. The first version of this line
                         published `78` as the COUNT, which is the id
rule   FZ: every self-ruling is recorded as `SR-<n>` with the question, the rule applied
       and the reason.
judge  52 new rows. Four self-rulings were taken and recorded: SR-75 (the lock's editable
       line is not installed), SR-76 (the environment check refuses rather than
       re-execs), SR-77 (SR-41 is closed by GJ4 rather than by a decision) and SR-78
       (GI3(e)'s config key is built rather than ledgered, because its absence made a
       shipped docstring false). The `sha256` the provenance now carries is GJ1's own
       wording and is measured in §1.
```

---

## 7. Carried

*The newest verdict is step 0's, and `docs/closure/R2-step0.md` § "Carried out of step 0"
is the list it routed, because EK3 sealed the report and the artifact is where a closed
step's list lives (R1250). Every row of that table is answered here.*

| item | state | where |
|---|---|---|
| **R1243** | **ANSWERED — §8** | the chaining is stopped in BOTH jobs, the ladder guard asserts it rather than a proxy for it, and `scripts/ci_section.py` names skipped STEPS. Carried in as blocking by GJ4, and this step's only carried blocking item |
| **R1223, R1225** | **open, escalated, and the escalation has MOVED** | §1. GJ1 answered the previous form by restoring the lock. The lock is restored, and the golden regenerates only at numpy `2.4.0` with the threads unpinned — not under the lock, and not under the pins `floatfea export` applies. The ruling is open again, with the cause now known exactly and three costed options. **R1225's own published diagnosis is corrected in the source tree in this step** |
| R1232 | open | the write run, not this step. **`floatfea export` does hold it for the CHILD** — `_child_env()` assigns all five of `determinism.THREAD_ENV` before the engine starts, which is above any numpy import in that process — so the parent's limitation does not reach the solve |
| R1248 | open | step 2. `scripts/export_buoy_centers_ref.py` checks the stable tree's NAME and never its TAG. Untouched here; the export path does not use that script |
| CZ1 (ii)'s owed `pytest -q` at `5901738` | **STILL OWED — §A3** | attempted twice and stopped twice, both times because it was a third full-suite run competing with work on step 1's own gate. §A3 records what it cost and what it did establish. It goes in **step 1's closure commit**, with nothing else running |
| `docs/reports/R2/step-0.md:1616`, `:1629` | **later** — declare-only under EK3 | both sites are inside a report sealed at its final verdict, so **no change** here is the one form of answer still available; the correction itself lives in `docs/closure/R2-step0.md` |
| everything else | **later** | step 0's closure routed it to a later step or to the ledger, and this step did not reach it. The generated table below is the per-item record |

**THE TABLE BELOW IS GENERATED AND THE ONE ABOVE IS NOT.** `scripts/carried_table.py`
reads the verdict's own headings and `docs/reports/R2/step-1-answers.json`'s pointers, so
it cannot attach a status to the wrong id — which is how three hand-written rows once
shifted by one and the item that had gone unanswered for three rounds fell off the end.
The table above is the discussion; the one below is the record.

**AND THE TWO WAYS OF CALLING THAT GENERATOR DISAGREE, WHICH IS A LEDGER ROW AND A
SEVENTH INSTANCE OF ONE SHAPE.** The published command
`python scripts/carried_table.py <verdict> <answers>` emits **72** rows; the guard calls
`carried_table.table(VERDICT_TEXT, answers)` directly and gets **68**, with four ids
absent and four subjects cut at a different point — one of them ending mid-way through a
shell command the verdict quotes. The guard is what must be satisfied, so what is pasted
below is the guard's own output and not the CLI's, and that is stated here rather than
left for a reader to discover by running the published command and getting a different
table. The cause is the same one `scripts/carried_table.py` already carries as a ledger
row in its own comments — six copies of the finding-id pattern across four files — reached
this time through the two call paths rather than the six regexes. **It is NOT repaired
here**: `carried_table.py` is report apparatus under the freeze GI2 carries from GA1, and
a repair that changes what the guard accepts belongs in a `process:` commit with a
directive behind it.

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R835 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1186 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1188 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1189 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1190 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1191 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1193 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1196 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1197 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1198 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1199 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1200 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1201 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1203 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1204 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1205 | **later** — §11 | carried, and the verdict says nothing further about it here |
| R1206 | **later** — §11 | carried, and the verdict says nothing further about it here |
| R1207 | **later** — §11 | carried, and the verdict says nothing further about it here |
| R1208 | **later** — §11 | carried, and the verdict says nothing further about it here |
| R1212 | **later** — §11 | ','R1217','R1218','R1224') if i in t.EXPECTED])" |
| R1213 | **later** — §11 | The DS0 refusal in run_floatsim_design_waves.py DOES NOT FIRE on the input this diff newly... |
| R1214 | **later** — §11 | A key that is SET BUT WRONG is silently discarded and a different worktree is used. claim what... |
| R1215 | **later** — §11 | docs/milestones/R2.md:5 says the marker reads 1 while :3 reads 0, and calls the shipped state... |
| R1217 | **later** — §11 | ','R1218','R1224') if i in t.EXPECTED])" |
| R1218 | **later** — §11 | ','R1224') if i in t.EXPECTED])" |
| R1219 | **later** — §11 | ' in t.EXPECTED, |
| R1221 | **later** — §11 | The Carried gate is parametrised over PHANTOM finding ids -- R2, and R1 too -- and no wording... |
| R1222 | **later** — §11 | test_a_blocking_item_is_not_routed_to_4a is red because verdict 59 wrote its dispositions as... |
| R1223 | **open** — §1 | A PUBLISHED DELIVERABLE no longer regenerates from this tree, and the two rows that moved are... |
| R1224 | **later** — §11 | ') if i in t.EXPECTED])" |
| R1225 | **open** — §1 | THE --check REFUSAL IS NOT THREAD COUNT. The npz golden moved when THIS REPOSITORY'S OWN... |
| R1226 | **later** — §11 | R1213 ONE KEY OVER: NOTHING TIES THE TREE THE STABLE KEY NAMES TO THE TREE THE SNAPSHOT... |
| R1227 | **later** — §11 | R1206's FOURTH SITE: tests/test_report_carried.py:579 still reads assert STEP > 0, and it goes... |
| R1228 | **later** — §11 | tests/test_report_guard_states.py:117 quotes the expression this commit changed. It reads "The... |
| R1229 | **later** — §11 | tests/unit/test_hsp_worktree_resolution.py:123 IS AN ASSERTION THAT CANNOT FAIL, and it is the... |
| R1230 | **later** — §11 | THE Answers: HEADER NAMES VERDICT 61 WHILE THE NEWEST IS 62, AND THE GATE'S FINDING SET IS... |
| R1231 | **later** — §11 | ALL THREE GENERATED SECTIONS ARE UNFILLED PLACEHOLDERS, AND CI IS RED AT THIS COMMIT, WHICH IS... |
| R1232 | **open** — §11 | R1225 (ii) IS RECORDED AND NOT HELD, AND pin_threads() CANNOT BE WIRED AT THE CALL SITE THE... |
| R1233 | **later** — §11 | R1225 (i) IS SATISFIED FOR THE RULING AND NOT FOR THE SENTENCE IT IS USED TO SUPPORT. ~200 eps... |
| R1234 | **later** — §11 | tests/test_report_vocabulary_corpus.py HAS TWO NEW REDS AND THEY ARE MINE, NOT YOURS. cmd... |
| R1235 | **later** — §11 | R1221 AND R1228 ARE UNCHANGED. Verdict 62's item 5 read "R1227 and R1228 in the next commit... |
| R1236 | **later** — §11 | TWO FIGURES IN THE REPORT THAT ONE COMMAND EACH REFUTES. Section 6's R1205 block pastes out... |
| R1237 | **later** — §11 | THE GENERATED 0a TABLE PUBLISHES A RUN THAT CONCLUDED FAILURE AS "no result", AND OMITS A RUN... |
| R1238 | **later** — §11 | THE WHOLE-SUITE RED LIST IS TWO REDS SHORT OF THE COUNT IN ITS OWN LINE, AND THE GENERATOR... |
| R1239 | **later** — §11 | CI RUNS RUNG 6 BEFORE RUNGS 4 AND 5, SO THE HIGHEST RUNG SKIPS THE TWO THIS STEP NEEDS. claim... |
| R1240 | **later** — §11 | THE CARRY GATE READS THE OLDEST ROUND'S Carried SECTION, SO FIVE ITEMS THE NEWEST VERDICT... |
| R1241 | **later** — §11 | TWO SENTENCES THAT ONE COMMAND EACH REFUTES. Sec.14 reads "the verification ladder at 4c19570... |
| R1242 | **later** — §11 | THE _FINDING PATH IS UNFILTERED, SO A MILESTONE LABEL CAN STILL ENTER THE PARAMETRISED SET.... |
| R1243 | **answered** — §8 | THE RUNG REORDER BREAKS THE GATE THAT EXISTS TO PREVENT IT, AND IT TAKES THE WHOLE OF... |
| R1244 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1245 | **later** — §11 | MOVED TO THE ARTIFACT AND THE CORRECTION IS RIGHT. The paragraph around it is not, and |
| R1246 | **later** — §11 | MOVED TO THE ARTIFACT, and this one's history IS what the artifact says. Measured, |
| R1247 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1248 | **later** — §11 | no clause this generator can cut -- see the verdict's Carried section |
| R1249 | **later** — §11 | THE CLOSURE ARTIFACT'S "WHICH GATES PASS" TABLE PUBLISHES TWO OF ITS FIVE ROWS AS GREEN WHERE... |
| R1250 | **later** — §11 | tests/test_report_carried.py:3054 CANNOT SEE A STEP CLOSURE ARTIFACT, SO AT THIS CLOSING COMMIT... |
| R1251 | **later** — §11 | THE "EIGHT LINES" FIGURE IS WRONG AT EVERY COMMIT IN PLAY, AND IT SITS IN THE TWO PLACES CW0's... |
| R1252 | **later** — §11 | THE ARTIFACT'S ROUND ARITHMETIC DOES NOT ADD UP, AND ITS "NINETEEN" IS A DIFFERENT QUANTITY.... |
| R1253 | **later** — §11 | THE ARTIFACT DROPS THE SCOPE ON THE ITERATION FIGURE, AND IT ERRS IN THE SAFE DIRECTION.... |
| R1254 | **later** — §11 | RUNG 3's PHANTOM-CITATION GUARD CANNOT SEE scripts/, WHICH IS WHERE THIS ARTIFACT'S CITATIONS... |
| R1255 | **later** — §11 | THE LADDER's STEP ORDER IS ASSERTED FOR RUNGS 3, 4 AND 6 AND FOR NOTHING ELSE, SO RUNG 1 CAN BE... |
| R1256 | **later** — §11 | THE REPAIR CLOSES THE CELL ITS CONDITION NAMED AND LEAVES THE SIBLING CELL GREEN: WHEN THE... |
| R1257 | **later** — §11 | R1251 IS FIXED AT ONE OF ITS TWO SITES IN THE SAME FILE, AND THE SURVIVING ONE IS 88 LINES... |
| R1258 | **later** — §11 | THE CARRIED TABLE ROUTES R1254 AND R1255 TO "THIS ARTIFACT, BELOW" AND NEITHER APPEARS ANYWHERE... |
| R1259 | **later** — §11 | THE R1245 PARAGRAPH ASSERTS A HISTORY AND REFUTES IT IN THE SAME SENTENCE, AND THE CLAUSE IT... |
| R1260 | **later** — §11 | THE ESCALATION CITES requirements-lock.txt AS THOUGH IT WERE FLOATFEA-LOCAL, IT IS HSP's, AND... |
| R1261 | **later** — §11 | THE TWO READERS STILL DIVERGE ON THE MILESTONE CHECK, WHICH IS THE SIXTH INSTANCE OF THIS... |
| R1262 | **later** — §11 | THE BLOCK IS LABELLED "CZ1 (ii)-(iv)" AND CARRIES (ii) PLUS A RUN CENSUS; (iii)'s EVIDENCE IS... |
```
claim  every row of the closure artifact's carried table is answered above, and the ids
       this section does NOT name are the ones that table records as already answered
cmd    python - <<'EOF'  # rows and distinct ids in the closure's Carried table,
       ...               # and the ids named in this section
out    closure carried rows        17   -- all 17 answered in the table above
       distinct R ids in them      68
       ids named in this section   54
       the 15 not named            R1206 R1207 R1214 R1227 R1228 R1229 R1230 R1236
                                   R1237 R1238 R1239 R1240 R1245 R1246 R1252
       **THE FIRST VERSION OF THIS BLOCK PUBLISHED 37 AND 31**, measured before the
       table above was finished, and a second parse of the closure file that looked
       right gave 28 rows because it ran past the section into the next table. Both
       figures are re-taken here with the section scoped to its own heading.
rule   `CLAUDE.md` § Step gating: a `Carried` section answering each open item from the
       previous review, or stating "checked, nothing carried".
judge  **FOURTEEN of the 15** are ids the closure's own table marks **answered in step
       0** -- in revisions 1, 2 and 3, or in the closure commit itself. Re-answering them
       here would claim work this step did not do. **The fifteenth is R1239, which is not
       an ITEM of that table at all**: it appears only inside R1243's row, cited as the
       observation R1243 upholds while reverting its repair. Its substance is answered in
       section 8, where the chaining is stopped in the way R1239 said it had to be.
       Every row that routes an item FORWARD is answered above, which is what the 17 rows
       are.
```

**Nothing from step 0 is dropped and one thing is added**: §5a is a GI1 violation found in
this step and carried to step 2 by name.

---

## 8. R1243 — the chaining is stopped, in both jobs

GJ4 carried it in as blocking and the closure artifact set the repair condition: *"stop the
chaining: separate jobs, or `if: always()` per step, with a CI section that names skipped
STEPS."* All three parts are done, and the second one is done in the stricter form.

```
claim  every ladder rung and every lint check now runs on its own condition
cmd    python -c "import yaml; [print(job, s.get('name'), s.get('if')) for ...]"
out    ladder 1..6   if: ${{ !cancelled() && steps.deps.outcome == 'success' }}   (6 of 6)
       ruff, black --check, mypy, unit tests, guards and meta-tests
                     if: ${{ !cancelled() && steps.deps.outcome == 'success' }}   (5 of 5)
       actionlint    if: ${{ !cancelled() }}                              -- see below
       install       id: deps, no condition -- it is what the others depend on
rule   R1243's repair condition, as `docs/closure/R2-step0.md` states it.
judge  **`!cancelled()` RATHER THAN `always()`, AND THE CONDITION NAMES THE INSTALL.**
       `always()` would resurrect steps in a run that was CANCELLED on purpose -- the
       header of `ci.yml` says a superseded run is cancelled so its ladder cannot be read
       as the current one -- and would spend a runner on a result nobody will read. And
       the real dependency is the INSTALL, not the step before: a rung cannot run without
       its dependencies, and a rung's result does not depend on another rung's exit code.
```

```
claim  the guard asserts the un-chaining rather than a proxy for it, and it inverts
cmd    pytest tests/test_ci_determinism_gate.py -q -p no:randomly
       <remove ladder 5's `if:`>  then the same command
out    13 passed
       1 failed -- assert not ['ladder 5 -- independent confirmation']
rule   BP0: when a decision rule changes, every figure citing the old rule is regenerated
       or withdrawn in the same commit.
judge  `test_ladder_6_is_not_gated_behind_a_rung_that_is_red_under_Q8` asserted a
       POSITION, and its docstring said why that was enough: "steps stop at the first
       failure -- so the chain is now the ORDER". After R1243 that sentence is false and
       the position is a proxy for a mechanism that is no longer there. CH3's order is
       kept, because the rungs should still read top-down, and a second assertion now
       carries the property the test is named for. The docstring is rewritten in the same
       commit, which is what BP0 asks and what the figure version of this rule would have
       required.
```

**And the lint job is where the defect was actually measured, which is why it is fixed
too.** CZ1 (iii) exists because a CI-only `mypy` red SKIPPED that job's `unit tests` and
`guards and meta-tests` steps, so *"CI had never run R1's unit tests or guards at all"* —
`constraints-dev.txt`'s own comment says so. R1243's words name the ladder; the mechanism
is the same one, and fixing only the ladder would have left the job whose skipped steps
CZ1 (iii) asks a reader to look for.

**And `actionlint` is NOT gated on the install, which is the same defect one more time.**
It is a container action that reads `.github/workflows/` and needs nothing this job
pip-installs. Gating it on `deps` would let a broken install hide the WORKFLOW lint — one
check hiding another, reintroduced three lines after fixing it. Caught by reading the diff
rather than by a test, and the condition is `!cancelled()` alone.

**The third part, which is the one that makes a skip visible.** `scripts/ci_section.py`
reported skipped JOBS (R1137) and said nothing about skipped STEPS, so a job reported as
`failure` could contain four checks that never ran. It now names them, from the same
`--json jobs` payload the table above already reads.

**Ledger row, stated rather than quietly left:** that block has no test. It reads
`job["steps"]` from a live `gh` payload, so exercising it means either a fixture of that
payload or a run with a skipped step — both new apparatus under the freeze GI2 carries
from GA1, and `ci_section.py` is report apparatus rather than product code. The
distinction I am drawing is deliberate: `sensitivity_note()` is extracted and tested
because it is a refusal a *user* reads, and this is a generator whose output a reviewer
reads beside the run it was generated from. **The first CI section generated after this
commit is where it is seen to work or not**, and under FF0 a failure there is fixed in
the next commit.

---

## 9. The red at this commit, and where its trace comes from

**EG3 state (1): report written, verdict not yet.** The waiver applies only if EVERY red
traces to that cause, and the trace is pasted per id rather than summarised — the
eighty-third verdict is why, because eight planted states were once ruled as one cascade
by class and the eighth was a real defect.

**THE TRACE COMES FROM CI AT THIS COMMIT'S OWN SHA, AND THAT IS FP1's DESIGN RATHER THAN
A SHORTCUT.** FP1 requires the report commit to be pushed before the reviewer is invoked
so the judged commit always has a run, and CE1 requires the report's CI section to be
generated from that run. A local duplicate of CI's `guards and meta-tests` job is not the
same evidence and, measured here, is slower than the job itself: three attempts were
stopped, the last at `4%` after a long run, because several of those guards each spawn a
WHOLE NESTED SUITE in a worktree of their own —
`test_the_report_carries_a_WHOLE_SUITE_count` through `scripts/suite_count.py`, and
`tests/test_ci_ladder_gating.py` through `scripts/run_rung.sh` across ten layouts.

```
claim  what IS measured locally at this commit, and what is not
cmd    pytest tests/unit <the four root guards> <the three workflow guards>
              tests/test_report_numbers_are_sourced.py
              tests/test_plan_matches_tolerances.py
              tests/regression/test_export_config_matches_the_placeholder.py
              tests/regression/test_r1_example_golden.py  -q -p no:randomly
       pytest tests/test_report_carried.py tests/test_report_numbers_are_sourced.py
              -q -p no:randomly
out    the FV1 selection                              1028 passed, 0 failed
       tests/test_report_guard_states.py +
       tests/test_report_carried.py                    12 failed, 618 passed
       tests/verification/rung4/test_f4_g41_dynamic.py  1 failed, 115 passed
       python scripts/check_carried.py                  refuses: `docs/reviews/R2/
                                                        step-1.md ... missing`

       THE TWELVE, EACH BY NAME AND EACH WITH ITS OWN CAUSE:

       test_report_guard_states.py::test_the_guard_survives_the_state[
           baseline ]
           non_numeric_step_suffix ]
           superscript_digit_step_number ]
           draft_suffix_beside_a_step_report ]
           step_number_is_the_empty_string ]
           verdict_amended_after_the_commit_the_report_answers ]
           zero_padded_step_number ]
       test_report_carried.py::test_the_report_carries_a_CI_SECTION
       test_report_carried.py::test_the_reported_CI_counts_are_not_all_zero
       test_report_carried.py::test_the_CI_section_is_about_the_REVIEWED_commit
       test_report_carried.py::test_the_ROUNDS_SECTION_is_the_GENERATORS_and_not_a_
           paragraph
       test_report_carried.py::test_the_guard_reads_the_step_being_worked_on
rule   FV1: the local selection is the modules the diff touches, `tests/unit`, the four
       root guards, and any regression test reading a deliverable the diff regenerates;
       **the whole of `tests/regression` is CI's job at the pushed sha.** EG3 (i): every
       red traces by name. FS1/FT1: the predicate, per id.
judge  **ELEVEN OF THE TWELVE ARE ONE CAUSE: THIS REVISION HAS NO CI SECTION YET.** The
       seven `test_the_guard_survives_the_state` cases each plant a state, run the report
       guards inside it, and assert the guards do not ALL fail -- and the inner failure
       printed in all seven is the same line:
       *"every CI row in step-1.md reports zero passed and zero failed. That is the shape
       without the measurement."* The four `test_report_carried` CI cases are that same
       absence asserted directly.
       **AND THE ABSENCE IS FP1's OWN ORDERING, NOT AN OMISSION.** The CI section is
       generated from the run at the commit the report answers, and that commit is this
       one -- it cannot carry a section about a run that does not exist until it is
       pushed. CE1 made the section mandatory precisely because CI had been red at three
       reviewed commits with no revision saying so; FP1 then fixed the order. **The next
       commit adds it**, touching `docs/reports/**` only, which `ci.yml` ignores, so GC2
       is what gives that commit its evidence: the concluded run at its nearest ancestor,
       which is this commit's own.
       **THE TWELFTH IS THE STEP BOUNDARY.** `test_the_guard_reads_the_step_being_worked_
       on` prints it: *"step 1 has a report and no verdict yet. That is the legitimate
       boundary -- the verdict is written after the report is committed."* EG3 state (1),
       cleared by the verdict. `check_carried`'s refusal is the same boundary.
       **AND ONE RED IS NOT IN THAT LIST AND DOES NOT CLEAR AT THE VERDICT**:
       `test_the_npz_is_NOT_STALE_against_the_code_that_generated_it`, which is §1's
       escalation. It clears when §1 is ruled and not before. It is **not** a boundary
       red and is not claimed as one.
```

**The one thing this section cannot do at this commit, stated rather than left implied.**
EG3 (ii) asks that the verdict commit be measured too — "the report-guard files are run AT
that commit and the counts pasted in the next revision" — and that is the half no verdict
in R2 had measured before step 0. It is owed here as well: the eleven CI reds should be
gone once the next commit adds the section, and the twelfth once the verdict lands. Both
counts go in the next revision, which is where EG3 (ii) puts them.

---

## 10. Every site the newest verdict names that this diff does not touch

*`test_every_named_site_is_touched_or_declared` gives a deliberate escape hatch — the
report may write `no change` beside the exact site — and its docstring says what it is
for: "FIVE consecutive rounds closed a site-naming condition at some of its sites and
recorded it as answered". Half of an item is not the item.*

```
claim  every site the newest verdict names is either touched by this diff or declared
cmd    python scripts/untouched_sites.py          # the gate's own SITES and TOUCHED
out    319 rows, ALL of them sites this diff does not reach:
         219  the file is untouched
         100  the file is touched and this line number is the old one
rule   tests/test_report_carried.py::test_every_named_site_is_touched_or_declared
judge  **GENERATED, NOT TYPED.** `scripts/untouched_sites.py` imports the guard module
       and reads the SAME `SITES` and `TOUCHED` the gate reads, so this table cannot
       enumerate a different set from the thing it has to satisfy -- which is how the
       first version of that script produced 68 rows against the guard's 87.
       **AND THE 100 ARE WHY THE FIRST VERSION OF THIS SECTION WAS SHORT BY EXACTLY
       THEM.** I filtered the generator's rows on "the file is untouched" and declared
       219, leaving the 100 whose FILE this diff touches at a LINE it does not. The
       guard is per-LINE and said so, 100 times. The generator's own docstring says it
       "decides only which sites the diff does not reach" -- every row it emits is one.
       **The newest verdict is still step 0's**, because step 1's does not exist yet, so
       these are step 0's sites measured against step 1's diff.
```

| R1205 | `.claude/hooks/require-verdict.sh:105` | **no change** |
| R1205 | `CLAUDE.md` | **no change** |
| R1205 | `F2.md` | **no change** |
| R1205 | `F2.md:10` | **no change** |
| R1205 | `F3.md:9` | **no change** |
| R1205 | `F6a.md:3` | **no change** |
| R1205 | `R1.md` | **no change** |
| R1205 | `docs/milestones/R1.md` | **no change** |
| R1205 | `docs/milestones/R1.md:3` | **no change** |
| R1205 | `docs/reports/F2/step-4.md` | **no change** |
| R1205 | `docs/reviews/F2/step-4.md` | **no change** |
| R1205 | `scripts/check_carried.py` | **no change** |
| R1205 | `scripts/check_carried.py:126` | **no change** |
| R1205 | `scripts/check_carried.py:127` | **no change** |
| R1205 | `scripts/check_carried.py:128` | **no change** |
| R1205 | `scripts/check_carried.py:129` | **no change** |
| R1205 | `scripts/check_carried.py:130` | **no change** |
| R1205 | `scripts/ci_section.py:98` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:99` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:100` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:101` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:102` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:103` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:104` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:105` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:106` | **no change** — the line number is the old one |
| R1205 | `scripts/ci_section.py:135` | **no change** — the line number is the old one |
| R1205 | `tests/test_report_carried.py:608` | **no change** |
| R1206 | `tests/corpus/plan_step_marker_resolution.txt` | **no change** |
| R1206 | `tests/test_report_carried.py:617` | **no change** |
| R1206 | `tests/test_report_carried.py:639` | **no change** |
| R1207 | `data/f4/dynamic_inputs.npz` | **no change** |
| R1207 | `data/platform/platform12_deck.yaml` | **no change** |
| R1207 | `export_f4_dynamic_inputs.py:390` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:467` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:468` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:469` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:470` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:471` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:473` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:474` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:475` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:476` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:477` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:478` | **no change** — the line number is the old one |
| R1207 | `scripts/export_f4_dynamic_inputs.py:479` | **no change** — the line number is the old one |
| R1208 | `HSP-stable/studies/platform-12buoy/platform_common.py` | **no change** |
| R1208 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1208 | `export_platform_deck.py:75` | **no change** |
| R1208 | `report_joint_reactions.py:106` | **no change** — the line number is the old one |
| R1208 | `run_floatsim_design_waves.py:98` | **no change** |
| R1208 | `scripts/export_buoy_centers_ref.py:42` | **no change** |
| R1208 | `scripts/export_platform_deck.py:45` | **no change** |
| R1208 | `scripts/measure_platform_joints.py:48` | **no change** |
| R1208 | `scripts/report_joint_reactions.py:96` | **no change** — the line number is the old one |
| R1208 | `scripts/run_floatsim_design_waves.py:50` | **no change** |
| R1208 | `scripts/run_floatsim_design_waves.py:51` | **no change** |
| R1213 | `R2.md:253` | **no change** — the line number is the old one |
| R1213 | `R2.md:366` | **no change** — the line number is the old one |
| R1213 | `docs/hsp-coupling.md:121` | **no change** |
| R1213 | `export_platform_deck.py:77` | **no change** |
| R1213 | `report_joint_reactions.py:109` | **no change** — the line number is the old one |
| R1213 | `report_joint_reactions.py:121` | **no change** — the line number is the old one |
| R1213 | `run_floatsim_design_waves.py` | **no change** |
| R1213 | `run_floatsim_design_waves.py:138` | **no change** |
| R1213 | `scripts/run_floatsim_design_waves.py:102` | **no change** |
| R1214 | `CLAUDE.md` | **no change** |
| R1214 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1214 | `docs/hsp-coupling.md:45` | **no change** |
| R1214 | `export_buoy_centers_ref.py` | **no change** |
| R1215 | `docs/milestones/R2.md:5` | **no change** — the line number is the old one |
| R1215 | `dynamic_inputs.npz` | **no change** |
| R1215 | `export_f4_dynamic_inputs.py:467` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:468` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:469` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:470` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:471` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:473` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:474` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:475` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:476` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:477` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:478` | **no change** — the line number is the old one |
| R1215 | `export_f4_dynamic_inputs.py:479` | **no change** — the line number is the old one |
| R1215 | `hsp_pin.py:20` | **no change** — the line number is the old one |
| R1215 | `report_joint_reactions.py:96` | **no change** — the line number is the old one |
| R1215 | `scripts/export_f4_dynamic_inputs.py:435` | **no change** — the line number is the old one |
| R1215 | `tests/verification/rung4/test_f4_g41_dynamic.py` | **no change** |
| R1215 | `tests/verification/rung4/test_f4_g41_dynamic.py:321` | **no change** |
| R1221 | `CLAUDE.md` | **no change** |
| R1221 | `docs/milestones/R1.md:3` | **no change** |
| R1221 | `docs/milestones/R2.md:12` | **no change** — the line number is the old one |
| R1221 | `tests/test_report_carried.py:387` | **no change** |
| R1221 | `tests/test_report_carried.py:388` | **no change** |
| R1221 | `tests/test_report_carried.py:389` | **no change** |
| R1221 | `tests/test_report_carried.py:390` | **no change** |
| R1222 | `step-0.md` | **no change** |
| R1222 | `tests/test_report_carried.py:423` | **no change** |
| R1222 | `tests/test_report_carried.py:424` | **no change** |
| R1222 | `tests/test_report_carried.py:425` | **no change** |
| R1222 | `tests/test_report_carried.py:426` | **no change** |
| R1222 | `tests/test_report_carried.py:427` | **no change** |
| R1222 | `tests/test_report_carried.py:428` | **no change** |
| R1223 | `tests/regression/test_f6_deliverable_agrees_with_itself.py:317` | **no change** |
| R1225 | `CLAUDE.md` | **no change** |
| R1225 | `ci.yml:67` | **no change** — the line number is the old one |
| R1225 | `ci.yml:68` | **no change** — the line number is the old one |
| R1225 | `ci.yml:69` | **no change** — the line number is the old one |
| R1225 | `constraints-dev.txt` | **no change** |
| R1225 | `data/f4/dynamic_inputs.npz` | **no change** |
| R1225 | `dynamic_inputs.provenance.json` | **no change** |
| R1225 | `pyproject.toml` | **no change** |
| R1225 | `results/F6/floatfea_results_report.md` | **no change** |
| R1225 | `scripts/export_f4_dynamic_inputs.py:476` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:477` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:478` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:479` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:480` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:481` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:482` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:483` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:484` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:485` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:486` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:487` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:488` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:489` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:490` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:491` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:492` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:493` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:494` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:495` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:496` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:497` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:498` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:499` | **no change** — the line number is the old one |
| R1225 | `scripts/export_f4_dynamic_inputs.py:500` | **no change** — the line number is the old one |
| R1225 | `tests/test_ci_canonical_environment.py` | **no change** |
| R1226 | `CLAUDE.md` | **no change** |
| R1226 | `HSP-stable/studies/platform-12buoy/platform_common.py` | **no change** |
| R1226 | `data/platform/buoy_centers_ref.json` | **no change** |
| R1226 | `export_buoy_centers_ref.py` | **no change** |
| R1226 | `hsp_pin.py:36` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:37` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:38` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:39` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:40` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:41` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:42` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:43` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:44` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:45` | **no change** — the line number is the old one |
| R1226 | `hsp_pin.py:46` | **no change** — the line number is the old one |
| R1226 | `run_floatsim_design_waves.py:112` | **no change** |
| R1226 | `scripts/export_buoy_centers_ref.py` | **no change** |
| R1226 | `scripts/export_buoy_centers_ref.py:172` | **no change** |
| R1227 | `docs/reports/R2/step-0.md` | **no change** |
| R1227 | `step-0.md` | **no change** |
| R1227 | `test_report_carried.py:579` | **no change** |
| R1227 | `tests/test_report_carried.py` | **no change** |
| R1227 | `tests/test_report_carried.py:579` | **no change** |
| R1228 | `test_report_carried.py:236` | **no change** |
| R1228 | `tests/test_report_guard_states.py:117` | **no change** |
| R1229 | `step-0.md` | **no change** |
| R1229 | `test_report_carried.py` | **no change** |
| R1229 | `test_report_guard_states.py` | **no change** |
| R1229 | `test_report_numbers_are_sourced.py` | **no change** |
| R1229 | `tests/unit/test_hsp_worktree_resolution.py` | **no change** |
| R1229 | `tests/unit/test_hsp_worktree_resolution.py:123` | **no change** |
| R1230 | `CLAUDE.md` | **no change** |
| R1230 | `docs/reports/R2/step-0.md` | **no change** |
| R1230 | `docs/reviews/R2/step-0.md` | **no change** |
| R1230 | `scripts/ci_section.py:203` | **no change** — the line number is the old one |
| R1230 | `step-0-answers.json` | **no change** |
| R1230 | `tests/test_report_carried.py:406` | **no change** |
| R1230 | `tests/test_report_carried.py:407` | **no change** |
| R1230 | `tests/test_report_carried.py:408` | **no change** |
| R1230 | `tests/test_report_carried.py:409` | **no change** |
| R1230 | `tests/test_report_carried.py:410` | **no change** |
| R1230 | `tests/test_report_carried.py:411` | **no change** |
| R1230 | `tests/test_report_carried.py:412` | **no change** |
| R1230 | `tests/test_report_carried.py:514` | **no change** |
| R1231 | `CLAUDE.md` | **no change** |
| R1231 | `docs/reports/R2/step-0.md` | **no change** |
| R1231 | `tests/test_report_carried.py` | **no change** |
| R1232 | `floatfea/determinism.py:96` | **no change** — the line number is the old one |
| R1233 | `results/R1/example/member_forces.csv` | **no change** |
| R1234 | `tests/corpus/report_status_vocabulary.txt` | **no change** |
| R1234 | `tests/test_report_vocabulary_corpus.py` | **no change** |
| R1235 | `tests/test_report_guard_states.py:117` | **no change** |
| R1236 | `R2.md:15` | **no change** — the line number is the old one |
| R1237 | `test_report_guard_states.py` | **no change** |
| R1237 | `tests/test_report_carried.py` | **no change** |
| R1238 | `docs/reports/R2/step-0.md` | **no change** |
| R1238 | `scripts/suite_count.py` | **no change** |
| R1238 | `scripts/suite_count.py:282` | **no change** |
| R1238 | `scripts/suite_count.py:283` | **no change** |
| R1238 | `scripts/suite_count.py:284` | **no change** |
| R1238 | `scripts/suite_count.py:285` | **no change** |
| R1238 | `scripts/suite_count.py:286` | **no change** |
| R1238 | `scripts/suite_count.py:287` | **no change** |
| R1239 | `CLAUDE.md` | **no change** |
| R1240 | `scripts/carried_table.py:158` | **no change** |
| R1240 | `tests/test_report_carried.py` | **no change** |
| R1240 | `tests/test_report_carried.py:366` | **no change** |
| R1241 | `docs/reports/R2/step-0-answers.json` | **no change** |
| R1242 | `carried_table.py` | **no change** |
| R1242 | `tests/test_report_carried.py:387` | **no change** |
| R1242 | `tests/test_report_carried.py:388` | **no change** |
| R1242 | `tests/test_report_carried.py:389` | **no change** |
| R1242 | `tests/test_report_carried.py:390` | **no change** |
| R1243 | `ci.yml:496` | **no change** — the line number is the old one |
| R1243 | `ci.yml:497` | **no change** — the line number is the old one |
| R1243 | `ci.yml:498` | **no change** — the line number is the old one |
| R1243 | `ci.yml:499` | **no change** — the line number is the old one |
| R1243 | `ci.yml:500` | **no change** — the line number is the old one |
| R1243 | `ci.yml:501` | **no change** — the line number is the old one |
| R1243 | `ci.yml:502` | **no change** — the line number is the old one |
| R1243 | `ci.yml:503` | **no change** — the line number is the old one |
| R1243 | `tests/regression/test_f6_deliverable_agrees_with_itself.py` | **no change** |
| R1243 | `tests/test_ci_determinism_gate.py:199` | **no change** — the line number is the old one |
| R1249 | `CLAUDE.md` | **no change** |
| R1249 | `docs/closure/R2-step0.md` | **no change** |
| R1249 | `docs/closure/R2-step0.md:24` | **no change** |
| R1249 | `docs/closure/R2-step0.md:25` | **no change** |
| R1249 | `docs/closure/R2-step0.md:26` | **no change** |
| R1249 | `docs/closure/R2-step0.md:27` | **no change** |
| R1249 | `docs/closure/R2-step0.md:28` | **no change** |
| R1249 | `docs/closure/R2-step0.md:29` | **no change** |
| R1249 | `docs/closure/R2-step0.md:30` | **no change** |
| R1249 | `docs/closure/R2-step0.md:31` | **no change** |
| R1249 | `docs/closure/R2-step0.md:32` | **no change** |
| R1249 | `docs/reports/R2/step-0.md` | **no change** |
| R1249 | `scripts/check_carried.py` | **no change** |
| R1249 | `tests/test_report_carried.py` | **no change** |
| R1249 | `tests/test_report_guard_states.py` | **no change** |
| R1249 | `tests/test_report_numbers_are_sourced.py` | **no change** |
| R1249 | `tests/test_tree_prose_consistent.py:99` | **no change** |
| R1250 | `F2-step4.md` | **no change** |
| R1250 | `F2-step5.md` | **no change** |
| R1250 | `F2-step6.md` | **no change** |
| R1250 | `F2-step7.md` | **no change** |
| R1250 | `R1.md` | **no change** |
| R1250 | `docs/closure/R2-step0.md` | **no change** |
| R1250 | `tests/test_report_carried.py:3054` | **no change** |
| R1251 | `docs/closure/R2-step0.md:98` | **no change** |
| R1251 | `docs/milestones/F2a.md` | **no change** |
| R1251 | `tests/test_tree_prose_consistent.py:99` | **no change** |
| R1252 | `docs/closure/R2-step0.md` | **no change** |
| R1252 | `docs/reviews/R2/step-0.md` | **no change** |
| R1253 | `docs/closure/R2-step0.md:17` | **no change** |
| R1253 | `docs/closure/R2-step0.md:18` | **no change** |
| R1253 | `docs/closure/R2-step0.md:19` | **no change** |
| R1253 | `docs/reports/R2/step-0.md:109` | **no change** |
| R1253 | `docs/reports/R2/step-0.md:110` | **no change** |
| R1253 | `docs/reports/R2/step-0.md:111` | **no change** |
| R1253 | `docs/reports/R2/step-0.md:112` | **no change** |
| R1253 | `docs/reports/R2/step-0.md:113` | **no change** |
| R1254 | `docs/milestones/F2a.md` | **no change** |
| R1254 | `scripts/untouched_sites.py` | **no change** |
| R1254 | `scripts/untouched_sites_v2.py` | **no change** |
| R1254 | `tests/verification/rung3/test_closure_evidence_exists.py:45` | **no change** |
| R1255 | `CLAUDE.md` | **no change** |
| R1255 | `test_ci_ladder_gating.py` | **no change** |
| R1255 | `test_ci_runs_the_whole_suite.py` | **no change** |
| R1255 | `test_ci_workflow_is_wellformed.py` | **no change** |
| R1255 | `tests/test_ci_determinism_gate.py:197` | **no change** — the line number is the old one |
| R1256 | `check_carried.py` | **no change** |
| R1256 | `docs/closure/R2-step0.md` | **no change** |
| R1256 | `docs/closure/R2-step1.md` | **no change** |
| R1256 | `scripts/check_carried.py` | **no change** |
| R1256 | `scripts/check_carried.py:102` | **no change** |
| R1256 | `tests/corpus/closure_artifact_published_as_green.txt:97` | **no change** |
| R1256 | `tests/test_report_carried.py:3131` | **no change** |
| R1256 | `tests/verification/rung3/test_closure_evidence_exists.py` | **no change** |
| R1256 | `tests/verification/rung3/test_closure_evidence_exists.py:42` | **no change** |
| R1257 | `docs/closure/R2-step0.md` | **no change** |
| R1257 | `docs/closure/R2-step0.md:371` | **no change** |
| R1257 | `docs/closure/R2-step0.md:372` | **no change** |
| R1258 | `./docs/closure/R2-step0.md:184` | **no change** |
| R1258 | `docs/milestones/F2a.md` | **no change** |
| R1258 | `scripts/check_carried.py` | **no change** |
| R1259 | `docs/closure/R2-step0.md:202` | **no change** |
| R1259 | `docs/closure/R2-step0.md:203` | **no change** |
| R1259 | `docs/closure/R2-step0.md:204` | **no change** |
| R1259 | `docs/closure/R2-step0.md:205` | **no change** |
| R1259 | `docs/reports/R2/step-0.md` | **no change** |
| R1260 | `HSP-runs/requirements-lock.txt` | **no change** |
| R1260 | `docs/closure/R2-step0.md:226` | **no change** |
| R1260 | `docs/reports/R2/step-0.md:584` | **no change** |
| R1260 | `floatfea/hsp_pin.py:147` | **no change** — the line number is the old one |
| R1260 | `rung3/test_closure_evidence_exists.py` | **no change** |
| R1261 | `F2-step4.md` | **no change** |
| R1261 | `scripts/check_carried.py` | **no change** |
| R1261 | `scripts/write_verdict.py` | **no change** |
| R1261 | `test_report_carried.py` | **no change** |
| R1262 | `docs/closure/R2-step0.md` | **no change** |
| R1263 | `docs/closure/R2-step0.md:440` | **no change** |
| R1263 | `docs/closure/R2-step0.md:441` | **no change** |
| R1263 | `docs/reviews/R2/step-0.md` | **no change** |
| R1263 | `tests/test_tree_prose_consistent.py:99` | **no change** |
| R1263 | `tests/verification/rung3/test_closure_evidence_exists.py` | **no change** |
| R1264 | `.claude/hooks/require-verdict.sh` | **no change** |
| R1264 | `CLAUDE.md` | **no change** |
| R1264 | `check_carried.py` | **no change** |
| R1264 | `ci.yml:395` | **no change** — the line number is the old one |
| R1264 | `require-verdict.sh:461` | **no change** |
| R1264 | `scripts/check_carried.py` | **no change** |
| R1264 | `tests/corpus/closure_artifact_published_as_green.txt` | **no change** |
| R1264 | `tests/corpus/closure_record_absent_rather_than_wrong.txt` | **no change** |
| R1264 | `tests/test_report_carried.py` | **no change** |
| R1264 | `tests/verification/rung3/test_closure_evidence_exists.py` | **no change** |
| R1265 | `docs/SUPERVISOR.md` | **no change** |
| R1265 | `docs/closure/R2.md` | **no change** |
| R1265 | `step-0.md` | **no change** |
| R1265 | `tests/test_report_carried.py` | **no change** |
| R1266 | `docs/closure/R2-step0.md` | **no change** |
| R1267 | `tests/test_report_carried.py` | **no change** |

---

## 11. Every carried item, grouped by how step 0's closure routed it

*`test_a_carried_row_points_at_a_section_that_discusses_it` refuses a pointer at the
Carried section itself — "every item is in that table by construction, so the pointer
resolves whatever it says. Point at the section that does the work." This is that section.*

* **open — §1**: `R1223`, `R1225`
* **later — §11**: `R835`, `R1186`, `R1188`, `R1189`, `R1190`, `R1191`, `R1193`, `R1196`, `R1197`, `R1198`, `R1199`, `R1200`, `R1201`, `R1203`, `R1204`, `R1205`, `R1206`, `R1207`, `R1208`, `R1212`, `R1213`, `R1214`, `R1215`, `R1217`, `R1218`, `R1219`, `R1221`, `R1222`, `R1224`, `R1226`, `R1227`, `R1228`, `R1229`, `R1230`, `R1231`, `R1233`, `R1234`, `R1235`, `R1236`, `R1237`, `R1238`, `R1239`, `R1240`, `R1241`, `R1242`, `R1244`, `R1245`, `R1246`, `R1247`, `R1248`, `R1249`, `R1250`, `R1251`, `R1252`, `R1253`, `R1254`, `R1255`, `R1256`, `R1257`, `R1258`, `R1259`, `R1260`, `R1261`, `R1262`, `R1263`, `R1264`, `R1265`, `R1266`, `R1267`
* **open — §11**: `R1232`
* **answered — §8**: `R1243`

### 11a. How the verdict number in the header was derived

```
claim  the newest verdict's number, and the counts this section groups
cmd    grep -c "^# Review" docs/reviews/R2/step-0.md
       python - <<'EOF'   # every "verdict <n>" the file mentions, and the newest entry's
       import re; from pathlib import Path
       t = Path("docs/reviews/R2/step-0.md").read_text(errors="replace")
       print(sorted({int(m) for m in re.findall(r"verdict (\d{2})", t)}))
       print(sorted({int(m) for m in re.findall(r"verdict (\d{2})", t[:t.index("# Review", 10)])}))
       EOF
       python - <<'EOF'   # the group sizes in section 11
       import json; d = json.load(open("docs/reports/R2/step-1-answers.json"))["answered"]
       from collections import Counter
       print(Counter((v["state"], v["where"]) for v in d.values()))
       EOF
out    entries in the verdict file      11
       verdict numbers mentioned        [58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
       the NEWEST entry mentions        [58, 64, 65, 67]
       groups   later/§11 69, open/§1 2, open/§11 1, answered/§8 1   (73 rows)
rule   `tests/test_report_carried.py::test_the_report_names_the_verdict_it_answers`:
       "Without it there is no way to tell a report that predates a verdict from one
       that ignores it."
judge  **THE REVIEWER DOES NOT NUMBER ITS OWN ENTRIES**, so the number is derived rather
       than read: the highest mentioned anywhere is 67, and the newest entry ANSWERS 67's
       `R1256` and `R1261`, so the newest entry is 68. The sha is not derived -- it is
       the `Reviewed commit:` line, `8fe7fea`, and it is what the header pins.
       **If the number is wrong the sha is still right**, which is the half that decides
       which verdict this report answers.
```

**What each group means, and none of it is a status this step invented.**

* **`later`** — step 0's closure artifact routed the item to a later step or to the
  ledger, and step 1 did not reach it. That is a statement about THIS step's diff, not a
  re-reading of the item: re-deciding the routing here would be a second reader of one
  predicate, which is the shape step 0 paid five rounds for. §7's first table carries the
  routing, taken from the closure artifact.
* **`open` — §1** — `R1223` and `R1225`, the FQ3 escalation. Still open, still Xabier's,
  and **moved**: the cause is measured now and the options are costed. R1225's own
  published diagnosis is corrected in the source tree in this step.
* **`open` — §11** — `R1232` and `R1248`, routed to the write run and to step 2
  respectively. Neither is on `export`'s path.
* **`answered` — §8** — `R1243` alone. GJ4 carried it in as blocking and §8 is the repair,
  in both jobs, with the guard rewritten to assert the un-chaining rather than a position
  that was a proxy for it.

**The ids this section does NOT name are the ones the generator does not carry**, and
`scripts/check_carried.py` is what would say so: it compares the verdict's declared
findings against this report's `Carried` section and exits non-zero on any it cannot find.
It refuses at this commit for a different reason — step 1's verdict does not exist yet —
which §9 records.

---

# Appendix

## A1. What the engine is handed

```
claim  the exact argv and the environment the child runs in
cmd    <_covered_headings substituted so no subprocess is spawned; subprocess.run spied>
       python -m floatfea.cli export examples/platform12_export.yaml --check
out    ARGV
         C:\dev\floatfea\.venv-floatsim\Scripts\python.exe
         C:\dev\floatfea\scripts\export_f4_dynamic_inputs.py
         --dt 0.01  --out C:\dev\floatfea\data\f4
         --period 10.0 --period 12.5 --period 14.0 --period 15.0 --period 16.2
         --period 20.0
         --check
       ENV
         OMP_NUM_THREADS          1
         OPENBLAS_NUM_THREADS     1
         MKL_NUM_THREADS          1
         NUMEXPR_NUM_THREADS      1
         VECLIB_MAXIMUM_THREADS   1
         OPENBLAS_CORETYPE        Haswell
         FLOATFEA_HSP_RUNS        C:\Users\xlama\OneDrive\Documents\buoy\HSP-runs
         FLOATFEA_FLOATSIM_VENV   C:\dev\floatfea\.venv-floatsim
rule   GJ1: every FloatSim invocation by FloatFEA uses the locked environment; R1232: the
       thread pins cannot be set below a process's own numpy import.
judge  **THE FIVE THREAD PINS ARE SET FOR THE CHILD, WHICH IS WHERE R1232 SAYS THEY CAN
       BE.** `pin_threads()` cannot work inside a process that has already imported numpy,
       which is why step 0 left the environment recorded rather than held. A child process
       is the one place the pins land before any import, so the solve runs pinned whatever
       the caller's shell did.
       `OPENBLAS_CORETYPE` is `setdefault` and the thread counts are assigned: CI sets the
       kernel deliberately for every job, while an inherited `OMP_NUM_THREADS=8` is not a
       choice anyone made for a bit-exact comparison. Both directions are held by
       `test_an_INHERITED_coretype_is_NOT_overridden`.
```

## A2. What has been eliminated as the cause of §1, and what has not

**Six configurations, one case (`T_full = 10 s`), the same comparison each time.** The
measure is `max|a - b| / max|a|` over `case0/*` against the committed npz. Cells E, F and G
run in a throwaway venv built to hold the older numpy: it is a DIAGNOSTIC
and not a run environment — GJ1's is `.venv-floatsim` — it writes nothing, and it carries
its own `.gitignore`, so git never sees it. Rebuilding it is one `pip install` of the pins
named in the table's own rows.

| cell | numpy / scipy | threads | coretype | exact | differ | `accel` |
|---|---|---|---|---|---|---|
| A | 2.4.4 / 1.17.1 (HSP lock) | pinned 1 | Haswell | 10 | 6 | 8.774756e-14 |
| B | 2.4.4 / 1.17.1 (HSP lock) | pinned 1 | unset | 10 | 6 | 8.774756e-14 |
| E | **2.4.0** / 1.17.1 (the dev set at `cfb76ff`) | pinned 1 | Haswell | 10 | 6 | 8.774756e-14 |
| H | 2.5.4 / 1.18.1 (today's dev pin) | pinned 1 | Haswell | 10 | 6 | **6.367170e-14** |

```
claim  A, B and E agree to every printed digit on all six differing arrays, and H does not
cmd    scratch/one_case_probe.py under each environment
out    A, B, E   accel 8.774756e-14   base 9.938227e-15   contrib 3.028683e-15
                 lam 3.028683e-15     m_xddot 2.150092e-14  resid_control 1.109519e-09
       H         accel 6.367170e-14   base 1.173037e-14   contrib 3.749798e-15
                 lam 3.749798e-15     m_xddot 2.150092e-14  resid_control 1.115298e-09
rule   if a library version or the BLAS kernel were the cause, the magnitudes would move
       when it moved.
judge  **AT A PINNED THREAD COUNT, A NUMPY PATCH RELEASE AND THE BLAS KERNEL DO NOT MOVE
       THE RESULT, AND A MINOR RELEASE DOES.** A, B and E agree across 2.4.0 -> 2.4.4 and
       across two kernel settings; H, at 2.5.4, does not agree with them on four of the
       six. That is weaker than "the libraries are eliminated", which is what the first
       version of this block said on A, B and E alone -- and weaker than "pinning makes it
       version-independent", which is what the SECOND version said, after cell G and
       before cell H. Cell H was run only because three sentences I had already written
       asserted a cell nobody had measured.
       Cell G, unpinned at 2.4.4, differs from cell F, unpinned at 2.4.0, so unpinned the
       patch version moves it too. R1225's comment is half right rather than wrong.
```

```
claim  the inputs, the FloatSim source and FloatFEA's solve path are all unchanged
cmd    git rev-parse cfb76ff:<each file in the provenance's import closure>
       git -C <HSP-runs> status --porcelain ; git describe --tags --dirty
       git diff 006af3e1 7166c5ef          (report_joint_reactions.py)
out    at cfb76ff, ALL THREE of the files the staleness gate now flags matched the
         provenance exactly: report_joint_reactions.py 006af3e1, hsp_pin.py d2e055b9,
         export_f4_dynamic_inputs.py 3127f6ff
       HSP-runs: floatfea-ref-1, clean except one untracked directory (§5a)
       the only change to the solve module since the golden:
         -HSP_RUNS = ROOT.parent / "HSP-runs"
         +HSP_RUNS = hsp_pin.worktree("runs")
       and 10 of 16 arrays per case are bit-identical -- every input and every label
rule   FR1's second head: an input accepted and used other than as declared.
judge  No input moved, no physics moved, and the one code change in the solve path is
       where a directory is looked up. The pinned BEM `.nc` is tracked and clean at the
       tag.
```

**AND THE ONE CONFIGURATION THAT MATCHES THE RECORD IS THE ONE THAT REPRODUCES -- BOTH
HALVES OF IT.** The
green `--check` at `cfb76ff` was taken with the threads **UNPINNED** — step 0's own
ablation says so in those words, and used it to rule the thread count OUT as the cause of
the historical red. That inference was sound about the historical boundary and it is not
about today's: cells A, B and E all PIN the threads, which step 0's own `--check` run did
too, so a second variable had been introduced into a cell meant to have one.

| cell | numpy / scipy | threads | coretype | exact | differ | `accel` |
|---|---|---|---|---|---|---|
| F | **2.4.0** / 1.17.1 | **UNPINNED** | unset | **16** | **0** | **0** |
| G | 2.4.4 / 1.17.1 | UNPINNED | unset | 10 | 6 | 6.652617e-14 |

```
claim  cell F differs from cell E in the thread variables and nothing else
cmd    scratch/probe-F.sh -- the same probe, the same venv as cell E, with the five
       determinism.THREAD_ENV variables and OPENBLAS_CORETYPE unset
out    CONFIG {"OMP_NUM_THREADS": null, "OPENBLAS_NUM_THREADS": null,
                "MKL_NUM_THREADS": null, "NUMEXPR_NUM_THREADS": null,
                "VECLIB_MAXIMUM_THREADS": null, "OPENBLAS_CORETYPE": null}
       RESULT exact=16 differ=0
       WORST 0
       real 5m2.044s
cell   TWO CELLS, ONE VARIABLE EACH, SHARING F.
         E -> F   the five thread counts, numpy held at 2.4.0   ->  6 differ to 0
         F -> G   the numpy patch version, threads held unpinned ->  0 differ to 6
       Same worktree, same deck, same probe and same committed file throughout.
       wall   F  real 5m2.044s      G  real 9m24.007s
rule   `floatfea/determinism.py`: "reduction ORDER varies with thread count, so a
       floating-point sum is not bit-reproducible unless the count is fixed."
judge  **SO THE GOLDEN IS RECOVERABLE AT EXACTLY ONE CONFIGURATION: numpy 2.4.0 WITH THE
       THREAD COUNT UNFIXED.** That is the finding -- not that the file is wrong, and not
       that the libraries simply drifted, but that the configuration it was made at needs
       a YANKED numpy release and the one thread setting this repository's own determinism
       module says is not reproducible. `--check` under `floatfea export` pins, by design,
       so the command cannot reproduce it: §1's option 1 against option 2.
```

**Cell G was nearly abandoned, and it is the cell that changed the conclusion.** It ran
`9m24s` against cell F's `5m02s` on identical work — an unpinned solve on this machine
thrashes, which is step 0's measurement from the other side: pinning makes it *faster*
here. Its shell was stopped in favour of §A4 while the interpreter kept going and wrote its
result. **The version of §1 that existed in between said the libraries were eliminated**,
on A, B and E alone, and cell G refutes it. The lesson is the one step 0 closed on, pointed
back at me: sweep the grid, not the cell — three cells that agree are three cells that
agree, and the one that disagrees was the one left running.


---

## A3. CZ1 (ii)'s owed `pytest -q` at `5901738`

The closure artifact routed this here in those words: *"a count taken at `5901738` cannot
be written into `5901738`"*, which is CZ1's own second clause for a closed report. Three
of CZ1 (ii)'s four outputs and the whole of (iii) were measured at that sha in the verdict
file; this is the fourth.

```
claim  the whole suite at 5901738, in a clean worktree AT that commit
cmd    git worktree add --detach <tmp> 5901738
       git -C <tmp> status --porcelain        # expect none
       ( cd <tmp> && python -m pytest -q -p no:randomly )
       git worktree remove --force <tmp>
out    worktree at C:/Users/xlama/AppData/Local/Temp/cz1-owed/tree
       HEAD is now at 5901738 closure: R1249, R1250, and the fifth time one predicate
       had two readers
       5901738c3ace6884bf90a71c318e6c246b640ed8
       dirty files (expect none):            <- none, the worktree is clean at the sha
       ..F.....................................................  [  4%]
       ........................................................  [  6%]
       ........................................................  [  8%]
       .......                                <- STOPPED HERE, by me, at 8%
rule   CZ1 (ii): at the closure commit, tree clean, run and paste `pytest -q`.
judge  **NOT TAKEN, AND IT IS STILL OWED. I am not reporting a partial run as a count.**
       The worktree is clean at the sha and the suite started; it was stopped at 8%
       because it was the third full-suite run competing for this machine with §A4's
       26-minute export and with §9's enumeration, and those two are on step 1's own
       gate while this is a bookkeeping count about a commit three steps back.
       **It was attempted twice.** The first attempt was stopped for the same reason and
       the second was left hung when a process sweep of mine killed its nested child --
       `test_the_report_carries_a_WHOLE_SUITE_count` runs the whole suite AGAIN inside a
       worktree of its own, so a run of the suite at any commit is two nested suites, and
       a filter matching `suite_count` reached the inner one.
       **Where it goes: step 1's closure commit**, taken with nothing else running, under
       CZ1 (ii)'s own procedure. What this block records is that the measurement is owed,
       what it costs, and why it keeps losing to work on the gate -- which is more useful
       to the next reader than a figure from 8% of a suite.
       The one thing it DID establish is printed above and is not nothing: the worktree at
       `5901738` is **clean**, which is CZ1 (ii)'s first condition.
```

---

## A4. GI5 step 1's second half — `floatfea run` on the exported file

The export writes to a **scratch directory**, not to `data/f4`: FQ3 forbids re-baselining
the committed file, and §6 records that the engine now refuses to overwrite a tracked
golden at all. So this is the tool's own output, compared with the golden and then run
through the FE.

```
claim  what `floatfea export` produces, how it differs from the golden, and what
       `floatfea run` makes of it
cmd    python -m floatfea.cli export <the export config, outputs.directory -> scratch>
       sha256 both files; np.array_equal over all 100 arrays
       python -m floatfea.cli run <the placeholder config, npz -> the exported file>
out    export      wall 26 min 39 s, exit 1   <- see the judge, this is a FINDING
       committed   sha256 dea555d933fb9fd088213896f9ad38fd891f71dd8fab1d8381aa47fa577...
       exported    sha256 cd284f5b81925c9bd25be626b19faf2c383a36a5c200bfe95a5a671feb2...
       arrays      exact 64   differ 36   worst 1.109519e-09 on case0/resid_control
       floatfea run on the exported file:
                   governing U = 1.71167 at platform:hub4_arm ROOT
                   (T = 12.5 s, 3.3.2 interaction)
                   1248 member-force rows, 32 checked stations, wall 94.69 s
rule   GI5 step 1: "exporting the reference run reproduces the golden dynamic-inputs
       file, and `floatfea run` on it gives U = 1.71167."
judge  **THE SECOND HALF HOLDS EXACTLY AND THE FIRST DOES NOT, AND THE GAP BETWEEN THEM
       IS THE NUMBER THE DECISION NEEDS.** 64 arrays are bit-identical -- every input and
       every label, 10 per case plus the 4 at the top level -- and 36 differ, which is the
       six solve outputs of each of the six cases. That is cells A/B/E repeated across all
       six cases rather than one.
       **AND THE PUBLISHED GOVERNING UTILISATION DOES NOT MOVE**: same value to six
       figures, same member, same station, same period, same clause. So the difference the
       bit-exact gate refuses on does not reach the number anybody sizes steel against,
       which is what makes §1's option 1 cheap and option 3 unnecessary.
       **THE EXPORT ALSO EXITED 1, AND THAT IS A DEFECT OF MINE THIS MEASUREMENT FOUND.**
       `--out` was added in this step and the npz-written line still read
       `target.relative_to(ROOT)`, which RAISES for a path outside the repository: the
       arrays were written, the traceback came next, and the PROVENANCE was never written.
       `floatfea run` on the result then published *"wave basis: NOT RECORDED by the export
       of this dynamic-inputs file"* in both CSVs and in the report -- correctly, and that
       is FL2's caveat doing its job on a file my own command had left incomplete.
       Repaired, and held by `test_an_OUT_OF_TREE_out_writes_BOTH_files_and_records_the_
       real_path`, which drives the engine's write path with the solve replaced and goes
       red against the old line. **No unit test reached it before**, because the flag's
       other tests stop at the argv the engine is HANDED.
```
