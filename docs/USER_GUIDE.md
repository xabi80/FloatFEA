# FloatFEA — user guide

You have a clone of this repository and nothing else. By the end of this guide you will
have installed the tool, run it, and reproduced the number it is pinned against:
**`U = 1.71167` at `platform:hub4_arm` ROOT**.

**Everything in this guide is a command you can run.** Where a figure appears, the command
that produced it is beside it and the output is the real one, taken in a fresh clone. Where
a statement about the tool's behaviour could not be reduced to a command, it points at the
test that holds it, so you can check it rather than believe it.

---

## 1. What this is, and what it is not

FloatFEA reads a **dynamic-inputs file** exported from FloatSim, builds a space-frame model
of the floating platform's superstructure, applies the loads with inertia relief, solves,
and screens the member forces against **API RP 2A-WSD** as a working-stress check.

**It is an indicative sizing screen, not a code case.** Every artifact it writes says so on
its first line. The reasons are in each report's *Limitations this run does not escape*
section, and they are not small print:

* the member section is a **stiffness stand-in** for a triangulated truss whose depth is
  undecided, so the sizes are indicative;
* linear Airy waves, a rigid-body FloatSim, the superstructure only;
* the steel grade is **assumed** (S355), not certified;
* no joint or connection checks, no fatigue, no shell sub-models;
* no API one-third increase (locked off — see § 7.9).

If you are looking for a certified design check, this is not it. If you are looking for
"what do the members of this platform see, and how close to allowable is it", this is it.

---

## 2. Install

You need **Python 3.13** (the project pins `>=3.13,<3.14`) and `git`.

**Run both commands from the repository root** — the directory holding `pyproject.toml`.
`-e ".[dev]"` and `-c constraints-dev.txt` are both relative to it, and § 4 will shortly
ask you to think carefully about which directory other paths resolve against.

```bash
py -3.13 -m venv .venv
```

Then install the project **with the pinned dev set**. The constraints file is not optional
convenience — it is what makes a green run here mean a green run in CI:

```bash
.venv/Scripts/python.exe -m pip install -c constraints-dev.txt -e ".[dev]"
```

Those two lines are what this guide was written against, on Windows. `py -3.13` picks the
right interpreter when you have several; plain `python -m venv .venv` does the same if 3.13
is already your default. On Linux or macOS the interpreter inside the venv is
`.venv/bin/python`, and every `.venv/Scripts/python.exe` below becomes that.

Check it:

```bash
.venv/Scripts/floatfea.exe --help
```

```
usage: floatfea [-h] {run,export} ...

Structural FE for the FloatSim floating platform.

positional arguments:
  {run,export}
    run         build, solve, member forces, code check, report
    export      FloatSim runs -> dynamic inputs (needs HSP)

options:
  -h, --help    show this help message and exit
```

`floatfea` and `python -m floatfea.cli` are the same entry point; this guide uses the
second form because it works without the venv's `Scripts` directory on your path.

**Why `constraints-dev.txt` matters, in one measured sentence.** At one commit this tree
was green locally on `ruff`, `black` and `mypy` and CI's `mypy` failed on the same commit,
because five of the six tools resolved to different versions — and that red then *skipped*
CI's unit tests and guards. The file's own header carries the version table. If you install
without `-c constraints-dev.txt`, you are not running the toolchain this project is
verified under.

---

## 3. The one command

```bash
.venv/Scripts/python.exe -m floatfea.cli run examples/platform12_placeholder.yaml
```

That is the whole interface for an analysis: **one command, one configuration file.** It
prints its progress as it goes, and § 8 walks through the output line by line.

**Budget a minute to five.** It was 64–70 s on the machine this guide was written on, and
the committed `results/R1/example/report.md` records `solve | 190.07` from a slower one, so
do not read either figure as a specification. The solve is the whole of it; nothing else in
the run takes measurable time.

---

## 4. The configuration file

`examples/platform12_placeholder.yaml` is the worked example and it is commented. This
section is the reference: every key, its unit, and whether it is required.

**Everything in the configuration is FULL SCALE and SI** — metres, kilograms, seconds,
newtons, radians, pascals. The only model-scale number anywhere is `wave_height_model_m`
inside the dynamic-inputs file's provenance sidecar, and § 4.7 is about exactly that.

**Relative paths resolve against the configuration file's own directory**, not against your
shell's working directory, so a configuration means the same thing wherever you run it
from.

**An unknown key is refused, never ignored.** Seven top-level blocks exist and no others:

```
floatsim  topology  mass_distribution  sections  load_cases  code_check  outputs
```

plus the scalar `study_only`. Misspell one and you get a message naming the field and
listing the ones that exist (§ 7.6). A duplicate YAML key and a YAML merge key (`<<:`) are
both refused too (§ 7.11) — a configuration where one line silently overrides another is
not a configuration you can check.

### 4.1 `floatsim` — where the geometry comes from

| key | unit | required | what it is |
|---|---|---|---|
| `deck` | path | **yes** | the exported deck YAML. **The authority for every coordinate, every body total, the centre of gravity and the inertia.** Nothing in the configuration overrides it. |
| `tag` | string | no | which pinned HSP state the deck came from. Recorded and reported, never used to fetch anything. |
| `froude_lambda` | – | no (default `50.0`) | the Froude scale λ relating the model-scale FloatSim run to full scale. Admissible `1 .. 1000`. |

**λ is checked against the export, not trusted.** The dynamic-inputs file records the λ it
was produced at; if your `froude_lambda` differs, the run refuses and tells you the factor
— `λ³` on every force and `λ⁴` on the locked moment. It is not a conversion you can nudge.

### 4.2 `topology` — which members the platform is built from

Leave this block out and you get the **star**: one member from the platform centre to each
hub joint. `topology: {platform: star}` says the same thing explicitly.

To declare members individually, name their ends. Node names are `centre` and the deck's own
hub body names:

```yaml
topology:
  platform:
    members:
      - [centre, hub1]        # these four reproduce the star exactly,
      - [centre, hub2]        # labels included: `platform:hub1_arm` and so on
      - [centre, hub3]
      - [centre, hub4]
      - [hub1, hub2]          # a brace between two hubs is `platform:hub1_hub2`
```

Naming a hub the deck does not carry is refused against the deck's list — but this is the
one configuration mistake that arrives as a **Python traceback**, not as a clean one-line
refusal. See § 7.12; the message is there, at the bottom.

Each hub's tripod of cluster arms is **not** configurable.

### 4.3 `mass_distribution` — how each body's mass reaches its members

One entry per body (`platform`, `hub1` … `hub4`), and the body names must match the deck.

| key | unit | what it is |
|---|---|---|
| `f` | – (`0 .. 1`) | the fraction of the body's **deck** mass carried by its members. |
| `line_masses` | kg/m | an explicit distribution instead of `f`. |
| `lumped` | kg | explicit lumped masses, each `{label, mass, at}`. |

`f` and an explicit distribution together are refused — two ways of saying the same thing,
and the tool will not guess which you meant.

**The remainder's position is forced, not chosen.** With `f` declared, the mass the members
do not carry sits at `z_r(f) = (z_cog - f·z_joint) / (1 - f)`, which the deck's own centre
of gravity fixes. The run reports the residual `deck − member − remainder` **per body**, and
whether the remainder inertia is positive semi-definite. It never sums the residuals across
bodies: two bodies out in opposite directions would cancel.

**A distribution that is not a structure is refused** (§ 7.10). `study_only: true` runs it
anyway, and then every output carries `STUDY -- NOT FOR DESIGN` on every label and header.

### 4.4 `sections` — the steel

`sections.groups` is required: one tube per member group. For the default star each body's
members are one group, so the group names are the body names.

| key | unit | bounds |
|---|---|---|
| `d_outer` | m | `0.05 .. 50` |
| `wall` | m | `0.001 .. 2` |

`sections.material` is required, all four keys:

| key | unit | bounds | note |
|---|---|---|---|
| `E` | Pa | `1e9 .. 1e12` | Young's modulus |
| `G` | Pa | `1e8 .. 1e12` | **derived, and checked for exact agreement.** The model computes `G = E / (2(1+ν))` with `ν = 0.3`; a declared `G` that disagrees is refused (§ 7.8), because a `G` the stiffness does not use would still appear in the report. |
| `rho` | kg/m³ | `100 .. 25000` | **nominal only.** The builder back-computes an equivalent density per body so that `ρ·A` is the deck's own line mass whatever the section is. The run reports every equivalent density against this nominal. |
| `Fy` | Pa | `1e6 .. 2e9` | the assumed grade |

`sections.candidates` is the section grid the sizing analyses walk — optional, needed only
when `outputs.required_section` or `outputs.truss_sizing` is set. **Per group, ordered by
area and strictly growing**, because the loop steps the section *up* and declaration order
is the order it walks. The tool never extends the grid: if it runs out with `max U > 1.0`
the run refuses and names the group and the governing case.

`sections.truss` is the `(h, b)` grid and parameters the truss resolution is **reported**
over — optional, needed only for `outputs.truss_sizing`. Keys: `depths` (m), `widths` (m),
`shapes` (`box`, `triangle`), `d_over_t`, `joint_allowance`, `diameter_search` (m, the
bisection bracket). **These are not the candidate grid the loop steps through** — that is
`candidates`, and it is tubes.

### 4.5 `load_cases` — the sea states

Give **exactly one** of `npz` or `cases`. Both, or neither, is refused (§ 7.7).

| key | unit | what it is |
|---|---|---|
| `npz` | path, or list of paths | existing dynamic-inputs file(s), for `floatfea run`. A repeated path, or two different paths with the same file name, are both refused: a declared file is identified by its **name** in every artifact. |
| `cases` | list | the FloatSim runs to produce one, for `floatfea export`. Each is `{heading: deg, H: m, T: s}`, full scale. |
| `governing_periods` | s | **required, non-empty.** The only periods allowed to **set the envelope**. A case outside this set is still computed and reported, as sensitivity, and cannot govern. |
| `out_of_band_governing` | s | periods already in `governing_periods` that this configuration knowingly admits although they fall outside the associated-period band (§ 7.3). It does **not** add a period. |
| `headings` | deg (`0 .. 360`, closed) | the headings this run claims to cover. Leave it out to run at whatever the export used. Repeats refused. |
| `window_rule` | string | recorded provenance of the time window per case. |

### 4.6 `code_check` — the API options

| key | unit | default | bounds |
|---|---|---|---|
| `K` | – | `2.0` | `0.5 .. 3.0` |
| `Cm` | – | `0.85` | `0.1 .. 2.0` |
| `one_third_increase` | bool | `false` | **`true` is refused** (§ 7.9) |
| `K_sensitivity` | – | `1.0` | `0.5 .. 3.0`, or `null` for none |
| `Cm_sensitivity` | – | `1.0` | `0.1 .. 2.0`, or `null` for none |

**The two sensitivities are ABSOLUTE VALUES, not factors.** `Cm_sensitivity: 1.0` re-runs
the screen at `C_m = 1.0` whatever `Cm` is, and `K_sensitivity: 1.0` at `K = 1.0`. They are
one-variable reruns reported beside the main result as the extra columns
`utilisation_K_sens` and `utilisation_Cm_sens` in `utilisation.csv`. The identical unit and
bounds invite the other reading — under which `1.0` would mean "no change" and the shipped
example would publish two dead columns — so it is worth being explicit: in the shipped
example those columns differ from `utilisation` on 10 of 32 rows.

**Where `C_m` acts, and the two clauses are not the same one.** `C_m` multiplies the
bending term in **section 3.3.2's amplified interaction** — `u_axial + C_m·u_bending /
(1 − f_a/F_e')`, the **compression** branch — so a larger `C_m` *raises* compression
utilisations and leaves every row whose `governing_clause` reads `3.3.1 interaction`
(tension + bending) **untouched**. The *value* `0.85` is a different matter: it is tabulated
in **section 3.3.1 case (a)**, members in frames subject to joint translation. Value from
3.3.1, term in 3.3.2.

This guide said "section 3.3.1's interaction" in its first draft, inheriting the error from
a caveat published in all three artifacts. It was caught by changing `Cm` and seeing which
rows moved. At `Cm: 1.2` instead of `0.85`, nothing else touched, the governing `U` rises
`1.71167 → 2.05621` at the same member, station, period and clause, and:

| rows | what happened |
|---|---|
| 6 governed by `3.3.1 interaction` | **none moved** — the clause carries no `C_m` |
| 12 governed by `3.3.2 interaction` | **10 rose, 0 fell** |
| 14 governed by `3.2.4 beam shear` | none moved — not an interaction clause |

The two `3.3.2` rows that did not move are TIP stations whose bending term is
`u_bending = 1.6e-10` and `1.7e-09`: there is nothing there for `C_m` to multiply. Compare
`platform:hub2_arm` ROOT at `u_bending = 1.71139`, which moves.

The caveat is corrected, and
`tests/regression/test_r1_published_artifacts.py::test_R1156_the_Cm_caveat_names_the_CLAUSE_THE_TERM_IS_IN_and_the_CODE_AGREES`
now holds both halves — the published sentence and the code's own behaviour on a tension
and a compression case.

### 4.7 Model scale, full scale, and λ

FloatSim runs at model scale. FloatFEA is **full scale throughout**. The conversion happens
once, at the reader, and never again.

The dynamic-inputs sidecar may record the wave height at either scale or both:

```json
"run": { "wave_height_model_m": 0.484, "wave_height_full_m": 24.2, "lambda": 50.0 }
```

* **Both recorded** → the pair is a **claim about λ and it is checked**:
  `|full − model·λ|` against a declared relative allowance. A file recording `24.2 m` full
  with `100.0 m` model used to pass everything and publish both numbers beside the correct
  λ at exit 0 — a sea state that cannot exist, with nothing saying which number was wrong.
  Now it refuses (§ 7.4).
* **One recorded** → the other is **derived** (`full = model·λ`). `report.md` marks it, so
  you can see which number the file actually carried:
  `— **full scale derived**: 0.484 m model x lambda = 50.0`.
* The admissible wave height `0 .. 100 m` is the **full-scale** bound. The model-scale
  ceiling is **derived as `100/λ`**, not declared a second time — at λ = 50 that is 2 m,
  where a single shared ceiling admitted 100 m and was vacuous by exactly λ.

---

## 5. `floatfea run` and `floatfea export`

### `floatfea run <config.yaml>`

Builds the model, applies the loads, solves, computes member forces, screens them, and
writes the outputs. It needs **no HSP worktree and no FloatSim run** — it works on committed
dynamic inputs, which is why the worked example runs in a fresh clone.

Stages, in order, each timed and reported: `build`, `load`, `solve`, `code_check`, `total`.

### `floatfea export <config.yaml>`

Produces a dynamic-inputs file from FloatSim runs. **It needs the pinned HSP worktree, which
this repository does not contain, so today it refuses.** Both ways of invoking it refuse,
and the message tells you which situation you are in:

```
floatfea: load_cases already points at 1 existing npz file(s) (...). `export` PRODUCES
that file from FloatSim runs; declare `cases` instead, or run `floatfea run` with this
configuration.
```

```
floatfea: `floatfea export` is not implemented in R1 step 1. It needs the pinned HSP
worktree (docs/hsp-coupling.md), and FL1 scopes step 1 to existing data. The 2 declared
case(s) validated cleanly, so this configuration is ready for the export path when FL2(c)
wires it; what it cannot do is invent dynamic inputs. Point `load_cases.npz` at a committed
file to run now.
```

Note that the second message names "R1 step 1" as the scope it was written under; the
scoping is current but the step reference is stale. The outcome is the one that matters:
`export` validates your configuration and then refuses rather than inventing loads.

**What `export` will do when it is wired, and the half that already exists:** a declared
heading the BEM dataset does not carry is refused **by name**, with the whole missing list
rather than the first entry, and the comparison is exact — exporting 44.9° for a declared
45° would publish an envelope for a sea state nobody asked for. The naming half of that
refusal is written and tested; what it waits on is the dataset, which lives in HSP.

---

## 6. The output files

Everything lands in `outputs.directory`. Each flag is independent, and `report: true`,
`member_forces_csv: true`, `utilisation_csv: true` are the normal set.

### 6.1 `report.md` — read this one first

Eleven sections, in this order: what was configured; the wave basis the loads were exported
at; **sea-state admissibility per case**; what the run assumes; findings the build raised,
per body; what the columns mean; the governing utilisation; mass per body; wall time;
declared-and-what-became-of-it; limitations.

The admissibility table is the one to read before any utilisation:

```
| T_full (s) | H/lambda | admissibility | outside by (s) | in the envelope |
|---|---|---|---|---|
| 10 | 0.1550 | breaking | -2.542 | sensitivity only |
| 12.5 | 0.0992 | too short for this height | -0.042 | **GOVERNING, admitted out of band by declaration** |
| 14 | 0.0791 | in band | — | governing |
| 15 | 0.0689 | in band | — | governing |
| 16.2 | 0.0591 | in band | — | governing |
| 20 | 0.0387 | too long for this height | +3.684 | sensitivity only |
```

`sensitivity only` means **that case cannot set the envelope** — it was computed, it is in
the CSVs, and it is not allowed to govern. That is the single most important distinction in
the whole output.

### 6.2 `member_forces.csv` — one row per (member, station, case, basis)

A header block of commented lines carries the whole configuration, the wave basis and the
column caveats, then:

```
body, member, station, period_full_s, basis, N, Vy, Vz, T, My, Mz, sigma_Pa, tau_Pa, source, heading_deg
```

* **`N` is TENSION-POSITIVE.** Published compression-positive once, it put every over-unity
  station on the wrong API clause.
* `station` is `ROOT`, `MID` or `TIP`. ROOT and TIP are the element's two ends and are
  **exact**; MID is a closed form whose bending term is a measured 4% approximation.
* `basis` is one of six — `static`, `dynamic_max`, `dynamic_min`, `total_max`, `total_min`,
  `total_instant`. **Read a utilisation only from `total_instant`**: the six components at
  the step where σ peaks. `total_max`/`total_min` maximise each component *independently*
  over the window, so their six values never occur together and a stress formed from them is
  an upper bound, not a stress at any instant.
* `source` and `heading_deg` are the dynamic-inputs file the row came from and that file's
  recorded heading. Both are empty on `static` rows, which are gravity alone and belong to
  no file.

### 6.3 `utilisation.csv` — the API screen

One row per checked station per declared file. Columns, in published order:

```
body, member, station, period_full_s, basis,
f_a_MPa, F_a_MPa, f_b_MPa, F_b_MPa, f_v_MPa, f_vt_MPa,
axial_branch, bending_branch, interaction_form,
u_axial, u_bending, u_shear, u_torsion, u_combined, utilisation, governing_clause
[, utilisation_K_sens, utilisation_Cm_sens]   when the configuration declares them
, source, heading_deg
```

**Only `ROOT` and `TIP` are code-checked**, which is why 16 members give 32 rows and not 48:
MID's bending term is an approximation and is not screened.

A column the writer does not name is **refused**, not quietly dropped or quietly published
— adding a column is a decision someone makes on purpose.

### 6.4 `required_section.md` — only with `outputs.required_section: true`

Needs a `sections.candidates` grid. It proposes a section from the stored forces, then
**re-solves the whole model at the proposed section** and reports *both* numbers, because
the proposal's premise is measured rather than assumed. Sections: what was chosen with the
two `max U` values; the premise, measured; every re-solve; member groups it did not size;
limitations.

A group with no candidate grid is **not sized** and is named as such in every artifact,
carried at its declared section into every re-solve.

### 6.5 `truss_sizing.md` — only with `outputs.truss_sizing: true`

Needs `sections.candidates` **and** `sections.truss`. Everything `required_section` does,
plus the truss a parallel-chord idealisation of declared depth and width would need to carry
the accepted tube's forces.

**Its first section is a disclaimer and it is not a footnote:** the `U` values in that file
were evaluated on the **tube**, not on the truss. The truss resolution is derived from the
accepted tube's member forces and was **never re-solved** — no finite element model of
chords and diagonals is assembled, and nothing in that file certifies the truss as a
structure.

Setting `required_section` and `truss_sizing` together is refused: they walk the same grid
and differ only in what they report, so running both would solve the model twice for one
answer (§ 7.5). `truss_sizing` reports everything `required_section` does, so it is the one
to set if you want both.

### 6.6 The older deliverables under `results/`, and the superseded-row flag

`results/` holds published deliverables from earlier milestones. Two of them carry a
**`SUPERSEDED`** marker, and you need to know what it means before reading a number from
either.

**`results/F6b/truss_sizing.csv` has a per-row `superseded_FY3` column.** Every row with
`section=triangle` is superseded: the inclined-face shear allocation those numbers were
computed under was ruled unconservative, and the corrected treatment is each face carrying
`|Vz|·Lf/(2h)` in plane with its shear flow over `Lf`. **The box rows are not superseded** —
they were the control and the repair does not touch them.

```bash
.venv/Scripts/python.exe -c "import csv,collections,pathlib; rows=list(csv.DictReader([l for l in pathlib.Path('results/F6b/truss_sizing.csv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')])); print(len(rows),'rows'); print(sorted(collections.Counter((r['section'], r['superseded_FY3']) for r in rows).items()))"
```

```
168 rows
[(('box', 'False'), 84), (('triangle', 'True'), 84)]
```

**Those numbers are deliberately not recomputed.** That file is the record of what was
published; overwriting it would destroy the evidence that the correction was needed. The
corrected values come from `floatfea/run/truss.py`, which is what `floatfea run` with
`truss_sizing: true` uses today. `results/F6b/truss_sizing.md` carries the same marker as a
section heading, with what a reader of a triangle row should know.

A second, different `SUPERSEDED` appears in the header of every current artifact:
`a generic 0.6·Fy reference stress is NOT the API bending allowable and is SUPERSEDED by the
clause results in these columns`. That one is about an older *reference figure*, not about
the rows beneath it.

---

## 7. The refusals you will meet

**The rule behind all of them: the tool refuses rather than adjusting, and it refuses
before writing anything.** A refusal prints one message to stderr with **no traceback** and
exits `2`. Nothing partial is left on disk — a refusal that arrives after the outputs is a
warning with a non-zero exit code, which is not the same thing at all.

Each message below is the real one. The `# fix` line is what to do.

### 7.1 A heading outside `0 .. 360`

```
floatfea: load_cases.headings[0]: 400 deg is outside the admissible range [0, 360] deg.
If that value is intended, the range is declared in floatfea/run/config.py and changing it
is a reviewed change, not a local override.
```

`# fix` — use a heading in `[0, 360]`. The range is **closed at both ends**: `0` and `360`
are both admissible, and they are the same heading. Every bounded number in the
configuration refuses the same way, naming the field, the value, the unit and the range.

### 7.2 A declared heading this run cannot cover

```
floatfea: load_cases.headings declares [0.0, 45.0, 90.0] deg and this run covers 0.0 deg
-- the one heading its dynamic-inputs file was exported at. [45.0, 90.0] deg would never be
computed, and the governing utilisation would be published as THE envelope while being the
envelope over 0.0 deg alone. An envelope over several headings needs a multi-heading npz,
which `floatfea export` produces; `floatfea run` does not invent the loads for a heading it
was not given. Refused before any output is written, so nothing on disk describes a run
that did not happen.
```

`# fix` — either remove `load_cases.headings` (the artifacts then state the heading the
export actually used), or point `load_cases.npz` at files covering every heading you
declare. You may list several `npz` files; the envelope is taken over their union and the
report names the governing heading *and* file.

If the file records **no** heading at all, a declared set is refused for the same reason
rather than assumed to be heading 0.

### 7.3 A governing period the band excludes

```
floatfea: load_cases.governing_periods declares [12.5] s, which cannot set an envelope at
the recorded H = 24.2 m: T = 12.5 s at H = 24.2 m: too short for this height;
band 12.542 .. 16.316 s, H/lambda = 0.0992 (limit 0.1429), outside by -0.042 s. A case
outside the associated-period band, or above the deep-water breaking steepness, is
SENSITIVITY ONLY -- which is what every artifact's EZ2 caveat already says, and what
nothing checked until now. Remove it from `governing_periods` to report it as sensitivity,
or -- if it is admitted deliberately, as FA0 admits T = 12.5 s at 0.3% below the lower edge
-- name it in `load_cases.out_of_band_governing` as well, which records the decision in
every artifact. Refused before the solve, so nothing on disk describes an envelope a
breaking wave set.
```

The band is `sqrt(6.5·H) .. sqrt(11·H)`, computed from the height **the file itself
records**, and the deep-water breaking limit is `H/λ ≤ 1/7`.

`# fix` — two choices, and they are different statements:

* **Remove the period from `governing_periods`.** It is still computed and still appears in
  the CSVs, as sensitivity, and cannot govern.
* **Name it in `out_of_band_governing` as well.** That records a deliberate decision and it
  reaches every artifact. It is **not** a widened band: widening an edge by 0.3% would admit
  every case within 0.3% of an edge at every height forever, and that would be a tolerance.
  This admits one named period.

The worked example does the second, for `T = 12.5 s`, which sits 0.042 s below the lower
edge. The reason is the direction: the response rises as `T` falls across the band, so the
lower edge governs and 12.5 s represents it.

**And an override that admits nothing is refused too:**

```
floatfea: load_cases.out_of_band_governing names [14.0] s, which at the recorded H = 24.2 m
is INSIDE the band: T = 14 s at H = 24.2 m: in band; band 12.542 .. 16.316 s,
H/lambda = 0.0791 (limit 0.1429). An override for a case inside the band admits nothing,
and carrying it would hide the day it starts admitting something again. Remove it -- the
period stays in `governing_periods` and governs on the band's own terms.
```

A period named in `out_of_band_governing` that is not in `governing_periods` is refused at
load time: the list records a decision about a declared period, it does not add one.

### 7.4 The two recorded wave heights disagree with λ

```
floatfea: dynamic_inputs.provenance.json: the recorded wave heights disagree with the
recorded lambda. `wave_height_full_m` is 30 m and `wave_height_model_m` is 0.484 m at
lambda 50, which implies 24.2 m full scale -- a discrepancy of 5.8 m against an allowance
of 3e-08 m (RECORDED_HEIGHT_PAIR_RELATIVE). One of the two numbers is wrong and nothing
here can say which, so both are refused rather than published side by side beside a lambda
that contradicts them. Record one and let the other be derived, or fix the export.
```

`# fix` — this is a defect in the **dynamic-inputs file**, not in your configuration.
Record one height in the sidecar and let the other be derived, or re-export. Do not reach
for the allowance: it is a declared tolerance and changing it is a reviewed change.

### 7.5 Both sizing analyses set

```
floatfea: outputs.required_section and outputs.truss_sizing are both set. They run the same
loop over the same `sections.candidates` grid and differ only in what they report, so
running both solves the model twice for one answer. Set one: `truss_sizing` reports
everything `required_section` does and adds the truss resolution, so it is the one to set if
you want both. Refused before any output is written.
```

`# fix` — set `truss_sizing: true` and `required_section: false`.

**And `required_section: true` with no grid:**

```
floatfea: outputs.required_section is set and sections.candidates declares no grid, so
there is no section list to step through. FM0 requires the tool to walk a DECLARED grid and
forbids it extending one of its own, so this is refused rather than reported as an analysis
that found nothing: `no candidate passed` and `there were no candidates` are different
answers.
```

`# fix` — declare `sections.candidates` for at least one group. See § 4.4 and the commented
block in the worked example.

### 7.6 An unknown key

```
floatfea: outputs: unrecognised field(s) ['reports']. Known fields are ['directory',
'member_forces_csv', 'report', 'required_section', 'truss_sizing', 'utilisation_csv']. A
field this tool does not understand is refused rather than ignored, because an ignored
field means the run is not the run the configuration describes.
```

`# fix` — the message lists the keys that exist. Every block refuses this way.

### 7.7 `npz` and `cases` both, or neither

```
floatfea: load_cases: give exactly one of `npz` (an existing dynamic-inputs file) or
`cases` (the FloatSim runs to produce one). Both or neither is ambiguous.
```

`# fix` — `npz` for `floatfea run`, `cases` for `floatfea export`.

### 7.8 A declared `G` that disagrees with `E`

```
floatfea: sections.material.G = 81000000000.0 Pa, and the model derives
G = E / (2 (1 + nu)) = 80769230769.23077 Pa from E = 2.1e+11 Pa and nu = 0.3, which
`floatfea.model.platform` fixes. A declared G that disagrees would be used by nothing while
appearing in the report as if it were. Declare G = 80769230769.23077.
```

`# fix` — declare the value the message gives you. `G` is in the configuration so that the
report can state it and so that a mismatch is caught; it is not an independent input.

### 7.9 `one_third_increase: true`

```
floatfea: code_check.one_third_increase is true, and section 3.1.2's increase is NOT
implemented in floatfea/checks/api_wsd.py -- EZ4 Q2 locked it off, because the increase is
written for a declared extreme environmental event and these are screening design waves
with no return period. Accepting the flag and ignoring it would report allowables a third
lower than the configuration asked for. Set it false, or reopen EZ4 Q2.
```

`# fix` — set it `false`. A non-boolean value is refused separately: the increase is on or
off, not scaled.

**This one is raised after the solve**, inside the code check, so you will wait for the
solve before seeing it. No artifact is written.

### 7.10 A mass distribution that is not a structure

```
floatfea: this mass distribution is not a structure: the remainder inertia is not PSD on
[...] (DY0(d): m_r >= 0 and no eigenvalue of J_r below -tol), so those bodies are not
bodies. Set `study_only: true` to run it anyway -- every output will then carry
`STUDY -- NOT FOR DESIGN` -- or declare a distribution whose bodies are admissible and
whose members have mass.
```

`# fix` — declare an admissible distribution, or set `study_only: true` and accept that
every artifact is marked. `f: 0` is refused the same way, with the members carrying no mass
at all, and the message names which of the two situations you are in.

### 7.11 A duplicate key, or a YAML merge key

```
floatfea: duplicate key 'study_only' at line 197. YAML's default is last-wins and silent,
so the run would have used the second value while the first sits in the file looking
authoritative. Remove one.
```

```
floatfea: merge key `<<` at line 163 is not accepted. A merged mapping bypasses the
duplicate-key check -- YAML flattens it after this check runs -- and an explicit key
silently overrides a merged one, so a field could take a value from either place with
nothing in the file saying which. Write the fields out.
```

`# fix` — the line number is in the message. For the merge key, write the fields out; the
configuration is short and sharing blocks between runs is not worth a file in which a value
can come from either of two places.

### 7.12 The one that arrives as a traceback

Almost every refusal in this section is a `ConfigError`: one line on stderr, exit `2`, no
traceback. **A bad node name in `topology.platform.members` is the exception.** It is caught
deeper than the configuration layer and reaches you like this:

```
  File "C:\dev\floatfea\floatfea\model\platform.py", line 528, in _declared_platform_members
    raise ValueError(
    ...<6 lines>...
    )
ValueError: topology.platform.members names 'hub9', which is not a node of this deck. The
platform's nodes are ['centre', 'hub1', 'hub2', 'hub3', 'hub4'] -- `centre` and the deck's
own hub bodies. A member to a node that does not exist cannot be built, and building the
rest without it would publish a frame the configuration did not describe.
```

**That is your configuration being refused, not the tool crashing.** Exit code `1` rather
than `2`, and the diagnosis is the last paragraph: read from `ValueError:` onwards and
ignore the frames above it.

`# fix` — use a node name from the list the message prints. If you are scripting around
`floatfea` and switching on the exit code, note that this class gives `1` where a
configuration refusal normally gives `2`.

### 7.13 The rest, with their real messages

Each of these backs a sentence in § 4. They are all `ConfigError`, exit `2`, and all but the
first fire before anything is built.

**`floatsim.froude_lambda` disagreeing with the export** (§ 4.1) — caught at the reader,
after the build, before the solve:

```
floatfea: scale mismatch. floatsim.froude_lambda = 40.0 in lambda_mismatch.yaml, and
dynamic_inputs.npz was exported at 50.0 according to the npz. The deck would be built at
one scale while the joint reactions in that file carry another: the yaw-locked composite
goes as lambda^3 on force and lambda^4 on the locked moment. The declared scale is smaller
by a factor of 1.25, which is 1.95312x on every force and 2.44141x on the locked moment.
Declare the file's own scale, or export a file at this one.
```

**A missing deck** (§ 4.1):

```
floatfea: floatsim.deck: ...\no_such_deck.yaml does not exist. The deck is the authority
for every coordinate, every body total, the CoG and the inertia, so there is no default and
nothing is built without it.
```

**The same `npz` twice** (§ 4.5):

```
floatfea: load_cases.npz[1]: ...\dynamic_inputs.npz is already declared at index 0. The
same dynamic-inputs file twice covers no additional heading and would be named twice in
every artifact that reports which files were read.
```

**Two different `npz` paths with the same file name** (§ 4.5) — the longer message explains
why the *name* and not the path is what matters: it is the identifier carried into the
per-file wave-basis block, the period-band table and the `source` column, so two files
called `dynamic_inputs.npz` would publish two sea states under one label.

**`f` and an explicit distribution together** (§ 4.3):

```
floatfea: mass_distribution.platform: `f` and an explicit distribution are both given. They
are two different ways to say the same thing and the tool will not guess which one you
meant.
```

**A candidate grid that does not grow** (§ 4.4):

```
floatfea: sections.candidates.platform[1]: d_outer 2.5 m, wall 0.18 m has steel area
1.31193 m^2, which is not more than sections.candidates.platform[0]'s 2.69203 m^2 (d_outer
2.5 m, wall 0.41 m). FM0's loop STEPS THE SECTION UP, so the grid is read in declaration
order and must grow: on a list in any other order the loop would halt at the first
admissible entry while every artifact said it had stepped up. Order the list by area, or
remove the entry.
```

### 7.14 Things that are *not* refusals

A **finding** is reported and the run continues. The worked example produces several, and
they are in `report.md` under *Findings the build raised, per body*. The loudest:

```
hub1: the equivalent density is 11433.5 kg/m^3, ABOVE steel at 7850. The members are
stiffness equivalents so a density above steel is not impossible, but it means this body's
mass does not fit inside F1's section at the chosen fraction and the section or the
fraction is the thing to look at.
```

That is a recorded fact about the configuration, not an error. So is the mass fraction
having been handed in by the caller rather than taken from the ladder. Read that section.

---

## 8. The golden example, end to end

```bash
.venv/Scripts/python.exe -m floatfea.cli run examples/platform12_placeholder.yaml
```

```
floatfea run platform12_placeholder.yaml
  built 5 bodies in 0.12 s
  T_full =   10 s: 707 steps
  T_full = 12.5 s: 884 steps
  T_full =   14 s: 990 steps
  T_full =   15 s: 1061 steps
  T_full = 16.2 s: 1146 steps
  T_full =   20 s: 1415 steps
  1248 member-force rows in 66.1 s
  32 checked stations in 0.00 s
  wrote C:\dev\floatfea\results\R1\example\member_forces.csv (1248 rows)
  wrote C:\dev\floatfea\results\R1\example\utilisation.csv (32 rows)
  wrote C:\dev\floatfea\results\R1\example\report.md

  governing U = 1.71167 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
  total wall time 66.21 s
```

**The three wall clocks in that output are the only lines that will differ in your clone.**
`0.12 s`, `66.1 s` and `66.21 s` are one machine on one run; the same clone gave `0.13`,
`70.5` and `70.61` on the next. Everything else — the step counts per period, the `1248`
and `32` row counts, and the whole governing line — is pinned and must match exactly.

**`U = 1.71167` is the number this example is pinned against.** Over unity, on the declared
section — which is the point: the declared tube fails the screen, and
`outputs.required_section` is how you find one that does not (§ 8.6).

Five things in that output are regression-pinned. Each is one command away.

### 8.1 The governing utilisation

```bash
.venv/Scripts/python.exe -c "import csv,pathlib; rows=list(csv.DictReader([l for l in pathlib.Path('results/R1/example/utilisation.csv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')])); g=max(rows,key=lambda r: float(r['utilisation'])); print(g['member'], g['station'], g['period_full_s'], g['utilisation'], g['governing_clause'])"
```

```
platform:hub2_arm ROOT 12.5 1.71167 3.3.2 interaction
```

**That says `hub2_arm` and the tool says `hub4_arm`, and the tool is right.** Both arms
print `1.71167` at six significant figures; at full precision `hub4_arm` is
`1.7116716105567911` and `hub2_arm` is `1.711671608463575`. A `max()` over the rounded CSV
column therefore picks whichever the tie-break reaches first. Do not "fix" the tool to
agree with the CSV.

### 8.2 The 32-row screen, each row at its own period

```bash
.venv/Scripts/python.exe -c "import csv,collections,pathlib; rows=list(csv.DictReader([l for l in pathlib.Path('results/R1/example/utilisation.csv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')])); print(len(rows),'rows'); print(sorted(collections.Counter(r['period_full_s'] for r in rows).items())); print('over unity:', sum(1 for r in rows if float(r['utilisation'])>1.0))"
```

```
32 rows
[('12.5', 26), ('15', 4), ('16.2', 2)]
over unity: 4
```

16 members × 2 code-checked stations (ROOT, TIP) = 32. Three periods win a station; the
fourth admitted period, `T = 14 s`, is a candidate everywhere and peaks nowhere.

### 8.3 The four admitted periods

`report.md`'s admissibility table (§ 6.1) lists all six computed cases and marks `T = 10 s`
and `T = 20 s` `sensitivity only`. `T = 10 s` is also above the breaking limit
(`H/λ = 0.1550 > 0.1429`). The four that may govern are `12.5, 14, 15, 16.2 s`, and 12.5 is
admitted by declaration.

### 8.4 The 1248-row six-basis envelope

```bash
.venv/Scripts/python.exe -c "import csv,collections,pathlib; rows=list(csv.DictReader([l for l in pathlib.Path('results/R1/example/member_forces.csv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')])); print(len(rows),'rows'); print(sorted(collections.Counter(r['basis'] for r in rows).items()))"
```

```
1248 rows
[('dynamic_max', 288), ('dynamic_min', 288), ('static', 48), ('total_instant', 48), ('total_max', 288), ('total_min', 288)]
```

16 members × 3 stations = 48 stations. Four bases over six periods give 288 each; `static`
has no period and `total_instant` is one row per station at that station's governing period.

### 8.5 The static symmetry on all four platform arms

```bash
.venv/Scripts/python.exe -c "import csv,pathlib; rows=[r for r in csv.DictReader([l for l in pathlib.Path('results/R1/example/member_forces.csv').read_text(encoding='utf-8').splitlines() if not l.startswith('#')]) if r['basis']=='static' and r['station']=='ROOT' and r['member'].endswith('_arm') and r['body']=='platform']; [print(r['member'], 'N=',r['N'], 'My=',r['My'], 'Mz=',r['Mz'], 'T=',r['T']) for r in rows]"
```

```
platform:hub1_arm N= -0.000000e+00 My= 1.916016e+08 Mz= 0.000000e+00 T= 0.000000e+00
platform:hub2_arm N= -0.000000e+00 My= 1.916016e+08 Mz= 0.000000e+00 T= -3.515518e-24
platform:hub3_arm N= -0.000000e+00 My= 1.916016e+08 Mz= 0.000000e+00 T= -9.513095e-10
platform:hub4_arm N= -0.000000e+00 My= 1.916016e+08 Mz= 0.000000e+00 T= -1.240771e-24
```

`My = +1.916016e+08 N·m` on all four, with `N` and `Mz` **exactly** zero. This is the
analytic check: four identical arms under gravity alone must give identical root moments
about one axis and nothing about the others.

**Torsion is where the round-off lives**, and the four values differ — `0`, `-3.5e-24`,
`-9.5e-10`, `-1.2e-24`. That is the arithmetic of four arms at four different orientations
reaching the same answer by different routes, not four different answers; the largest is
`1e-10 N·m` against a root moment of `1.9e+08`. Reading those columns one place to the left
is an easy mistake to make, and it is how this guide's first draft published them as `Mz`.

### 8.6 Finding a section that passes

**Copy the example first.** The shipped configuration writes into `results/R1/example/`,
which holds the pinned artifacts you have just verified. A `required_section` run is a
*different* configuration, so it replaces those CSVs with genuinely different numbers and
adds a `required_section.md` that `git checkout --` will not remove. § 8.7's restore
covers the benign case — same configuration, byte-identical CSVs — and does **not** cover
this one.

```bash
cp examples/platform12_placeholder.yaml examples/my_sizing_test.yaml
```

Then in the copy: point `outputs.directory` somewhere of your own, uncomment the
`candidates` block (it is there, commented, under `sections`), and set
`outputs.required_section: true`. On the shipped grid:

```
  required_section: platform proposed candidate 3 of 3 at fixed-force max U = 0.995702
  required_section: re-solve 1 at platform D=2.5 t=0.41
  ...
  required_section -- a DIFFERENT configuration from the line above:
    platform -> candidate 3 of 3, D = 2.5 m, wall = 0.41 m (fixed-force U = 0.995702, re-solved U = 0.995702)
    hub1 NOT SIZED (no candidate grid) -- declared D = 2.5 m, wall = 0.18 m, carried into every re-solve
    ...
    whole model at those sections: U = 0.995702 at platform:hub4_arm ROOT (T = 12.5 s, 3.3.2 interaction)
```

A 0.41 m wall brings the platform arms to `U = 0.9957`. **Note that the governing line above
it still reads 1.71167** — that line is the structure as your configuration declares it, and
the sizing block is a *different* configuration. The two `max U` values are both printed
because the proposal is made from stored forces and then checked by a real re-solve.

### 8.7 One thing to expect

**`floatfea run` on the shipped example overwrites `results/R1/example/`**, because that is
where the configuration points. Both CSVs regenerate **byte-identical**; `report.md` differs
only in its wall-time table, which is machine-dependent by nature. How many of its five rows
move depends on the machine, so do not check a line count — check that nothing *else* moved:

```bash
git diff -U0 results/R1/example/ | grep -E '^[+-][^+-]' | grep -vE '^[+-]\| (build|load|solve|code_check|total) \|'
```

```
(no output)
```

No output is the pass. For reference, the changed rows themselves:

```bash
git diff -U0 results/R1/example/ | grep -E '^[+-]\|'
```

```
-| build | 0.12 |
+| build | 0.13 |
-| solve | 190.07 |
+| solve | 70.47 |
-| total | 190.20 |
+| total | 70.61 |
```

`git checkout -- results/R1/example/` puts them back. If the first command prints anything,
that is a real finding and worth reporting.

---

## 9. Checking the installation, and where to look next

```bash
.venv/Scripts/python.exe -m pytest -q tests/unit
```

```
470 passed in 305.57s (0:05:05)
```

**The count is the pinned part; the time is not.** `470 passed` is what you should see;
the same clone has run this in 137 s and in 305 s. The full suite is large and slow, and
`tests/unit` is the sanity check.
The numbers in § 8 are pinned by `tests/regression/test_r1_example_golden.py`, and the two
sizing analyses by `test_ft24_required_section.py` and `test_ft25_truss_sizing.py`. If you
want to know whether a figure in this guide is still true, those files are where it is
asserted.

Beyond here:

| question | file |
|---|---|
| frames, signs, units, rotation order, numbering | `docs/conventions.md` |
| the load interchange format | `docs/load-interchange-v1.md` |
| how FloatSim/HSP is pinned, and why it is not forked | `docs/hsp-coupling.md` |
| the verification ladder, rung by rung | `docs/verification/README.md` |
| what each milestone built | `docs/milestones/` |
| every numerical tolerance in one place | `floatfea/tolerances.py` |

**One habit worth adopting from the way this tool is built:** when two numbers disagree, the
disagreement is the finding. Nothing in FloatFEA averages a per-case diagnostic, widens a
tolerance to get agreement, or falls back to an assumed load distribution — and if it ever
appears to, that is a bug worth reporting rather than a setting worth changing.
