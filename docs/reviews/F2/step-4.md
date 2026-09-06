# Review � F2 step 4
Reviewed commit: cc8801c98e1b9e90d2c90828daaff4b4e0c5132b
Verdict: STOP
Tests: 524 passed, 0 failed, 0 skipped   (my run at `e9dd32f`, `python -m pytest -q`, 1.73s.
With my corpus applied at `cc8801c`: **1 failed, 545 passed**.)

**Reviewed code commit: `e9dd32f`.** The header stamp above is `cc8801c`, my own
corpus commit, made immediately before this verdict and touching no code.

Ninth pass. Range `6191f9c..e9dd32f`, nine commits: four `process:`, three
`plan:`, one `revert:`, **one step commit**.

**The ordering is correct and it is the first thing this verdict checked.**
`git log --format="%h %ad %s" --date=iso 6191f9c..HEAD --reverse` puts the step
commit `626d8f7` (2026-09-06 07:01) after the plan re-lock `3316480` (06:52); no
commit touches both `.claude/` and code; none touches `docs/reviews/` or
`tests/corpus/`. The STOP was answered the way a STOP must be: through the plan.
That is real, and it is the difference between this round and the last four.

**And this is still a STOP, for a new reason on a new axis.** The form is gone —
verified, not accepted: `grep -rn "def equilibrate" .` returns nothing,
`PATCH_TEST_COND_FACTOR`, its counter, `COND_UNIT_INVARIANCE` and its counter are
deleted, and no test asserts any conditioning quantity. Four of the eighth
verdict's five reds are answered without narrowing anything. What replaced the
form is a **validated domain** — `PATCH_TEST_EXACTNESS` is claimed for member
`lambda <= 60` at the gate's mesh — and I refuted that claim by measurement:

```
D = 5.6809e-04 m, t = 5.24165e-06 m, L = 1.159406e-02 m
direction (-0.384196, -0.923213, 0.008385)/|.|,  roll = -1.5774 rad
the gate's own five-element station set

  assert_beam_admissible          PASSES        (member L/D = 20.41)
  warn_outside_validated_domain   0 warnings    (member lambda = 58.26 <= 60)
  1e-6 single-element control     1.0766e-07    fires
  worst state error               7.5786e-12    = 7.58x PATCH_TEST_EXACTNESS
```

A clean, admissible member, **inside the domain the plan re-locked yesterday**,
which the builder neither refuses nor warns about, breaching the ceiling that
domain exists to certify by 7.6x. Round-off by the permutation cell — COLAMD
`7.58e-12`, NATURAL `4.36e-12`, MMD_ATA `7.27e-14`, MMD_AT_PLUS_A `1.11e-13`: a
**104x spread on a quantity the fill-reducing ordering cannot change.**

The claim lives in `docs/milestones/F2.md` §5b Q6 and §D7 item 7 — locked plan
text, written one commit before the code. Correcting it is a plan edit, and
`CLAUDE.md` § Step gating says a plan edit is what a STOP reopens. So this does
not soften into a HOLD, and the standing instruction against settling this gate's
ceiling machinery inside another step commit applies unchanged.

**What is NOT the reason, and must not be lost in it.** The element is clean
again — the tenth consecutive round with no element defect. The form's removal is
complete and correct. The plan's diagnosis of the *axis* is right, and I checked
it rather than took it: my own 2-D grid, my own seed and my own irregular meshes,
gives exponent `+2.18 +/- 0.15` on member lambda in skew against `+0.52 +/- 0.20`
axis-aligned (theirs: `+1.94` and `+0.68`), and element `L/r` is refuted — held
fixed at `27.5` while `n` moves 3 to 12, the error still moves `183x`
axis-aligned and `143x` skew rather than staying flat. **The boundary is on the
right axis. The number on it, and the envelope behind the number, are not.**

## Carried

Every item from the eighth verdict (`STOP @ ad2246a`, committed `6191f9c`),
traced through `6191f9c..e9dd32f` and re-measured. The gated five first.

- **1. R69 (STOP) — ANSWERED, and answered properly.** `626d8f7`, after the plan
  re-lock. `PATCH_TEST_EXACTNESS` is the ceiling again and the floor-aware term is
  removed rather than demoted. `unit_mm_D_t_100_roll_neg`, the clean model the
  form refused at `1.063x`, is green at `0.4468` of the constant — I ran it.
- **2. R70 (STOP-class) — ANSWERED by withdrawal**, with the frame table kept in
  `F2.md` §D7 item 6 as the record of why. Correct: that measurement is the
  expensive part of this milestone and deleting it would have thrown it away.
- **3. R71 (blocking) — ANSWERED by removal.** The two stale tables went with the
  entry. The general rule they earned is now `CLAUDE.md` BI3 (`8d6ba7d`, a
  standalone `process:` commit). **BI3 is already violated once inside this same
  round** — see R87.
- **4. R72 (blocking) — ANSWERED by removal.** There is no self-referential
  ceiling left to cap. The `expect=breach` branch now asserts `worst >
  PATCH_TEST_EXACTNESS` and falls through to the tier ceiling, which is the right
  shape.
- **5. R73 (blocking) — HALF ANSWERED, AND IT IS THE SAME HALF AS LAST TIME.**
  * The `conventions.md` inline edit is properly reverted (`b413a3d`); `git diff
    5de8fd8^ HEAD -- docs/conventions.md` is empty, as the report claims. The
    limit re-enters as Q5 in the reopened Q&A. The right route, taken.
  * `stubby_thin`, `stubby_thick` and `stubby_L_over_D_1p3` are still refused, on
    the strength of "Confirmed by Xabier" in `F2.md` §5b. The closing condition
    allowed exactly that ("or Xabier confirms `2.0` in writing"), so I accept it —
    while recording that the repository's only evidence is the implementer's own
    sentence, and that the F0 reopen commit the plan names as the route has **not
    happened**, leaving four dangling citations (**R87**).
  * **The site the condition named was not touched.** I extracted
    `PATCH_TEST_EXACTNESS_COUNTER`'s entry from `git show
    6191f9c:floatfea/tolerances.py` and from the file at `e9dd32f` and compared:
    **byte-identical, 22 lines.** No geometry, no direction of degradation, no
    mention of either configuration known to leave its domain. **R83.**
  * `member_l_over_d` still has no shape guard, and `member_lambda` was added
    beside it with the same blindness. **R90.**
- **6. R74 (blocking) — ANSWERED.** `grep -n "cond(K_ff)" docs/milestones/F2.md`
  now finds the formula only inside §D7 item 6's record of what was withdrawn.
  D7 item 5 states what ships.
- **7. R75 (gated) — ANSWERED, and better than asked.** `_validate_section` checks
  the shape token, refuses an unknown key inside the spec, refuses a missing one,
  and a duplicate top-level field is refused too. Four new malformed shapes each
  have a test. My three entries go green by raising, and my new
  `section_shape_absent` — a shape the fix was not written against — also raises,
  so it generalises. **The value one field over is still unchecked: R88, R89.**
- **8. R76 — NOT ANSWERED, correctly declared open** in the report's §7.
- **9. R77 — NOT ANSWERED, correctly declared open**, and re-measured:
  `test_the_corpus_coverage_is_reported`'s `solved` and `refused` are still exact
  complements by De Morgan, so `solved & refused` is empty and `solved | refused`
  is everything, for every possible corpus including an empty one. Sixth guard,
  same test, three rounds. Carried unchanged.
- **10. R78 — hole 3 STILL OPEN, and two new holes opened.** `NotebookEdit` with
  `notebook_path` under `tests/corpus/` is still **ALLOWED**; I re-exercised it.
  **R84.**
- **11. R79 — NOT ANSWERED, correctly declared open** and correctly routed to
  V2.2. My new `thick_wall_D_t_3_lam50` puts a `-25.7%` kappa error inside the
  newly declared validated domain, which is where it now matters more.
- **12. R80 — NOT ANSWERED, correctly declared open, AND A THIRD INSTANCE WAS
  ADDED THIS ROUND.** `100.0 * ceiling`. **R85.**
- **13. R63 — carried, unanswered, declared.** Of the three ceilings widenable in
  silence by `1e5x`, `1e5x` and `1e2x`, one (`COND_UNIT_INVARIANCE`) is gone with
  the form — the item shrank by removal rather than by fix. `MATRIX_SYMMETRY` and
  `ROUNDOFF_IDENTITY` remain.
- **14. R65 — still open**, mine. Three `expect=breach` entries pin round-off at
  1.0% and 2.8% of margin. Unchanged.
- **15. R62, R50, R52 — still open**, correctly declared in §7.
- **16. R6, R16, R25, R30, R31, R32, R33 (outside G2.2), R36 — still open**, in
  step 4a and step 5, correctly declared. `pin_threads` still has one caller.
- **17. R68's standard held.** §7 of revision 9 lists eighteen open items by
  number and I found none open that it omits. Three rounds of a complete list now;
  keep it.

## Findings

**R81. (STOP) The validated-domain claim the plan re-locked one commit before the
code is false, and I have the configuration. A clean, admissible member at member
lambda 58.26 — inside the domain — breaches `PATCH_TEST_EXACTNESS` by 7.58x at the
gate's own mesh, with the negative control firing and the builder reporting
nothing.** `docs/milestones/F2.md` §5b Q6 and §D7 item 7, `floatfea/tolerances.py`
`G22_VALIDATED_MEMBER_LAMBDA`'s entry (the "10x of margin" paragraph),
`floatfea/model/admissibility.py:98-131`.

The measurement is in the header above. The mechanism is that the envelope behind
the boundary was taken over **6 angles x 7 rolls x 6 states at one section**, and
**section size is a free axis it does not span.** Sweeping it at fixed lambda,
inside the domain:

```
2160 configurations, D in {6e-4 .. 5} m, D/t in {50,100,200},
     lambda in {30 .. 59.9}, 4 shipped orientations, 8 rolls
                                                  worst 0.80 of the ceiling
3028 random draws, D in [1e-4, 10] m, D/t in [2.1, 400],
     lambda in [20, 60], shipped orientations     worst 0.998 of the ceiling
3000 random draws, same but with the member DIRECTION free
                                                  worst 7.58x   BREACH
```

The entry's own words are "the exactness claim carries 10x of margin over that
envelope". Measured over an envelope that also spans section size: **1.002x within
the corpus schema, and a breach outside it.** Two of my new entries sit at `0.532`
and `0.356` at lambda 56.0 and 58.3, and they are ordinary members — `L/D` 19.8
and 20.6, controls firing — differing from `unit_mm_D_t_100_roll_neg`, which the
implementer already admits and reports green, only in size and roll. This is not
an exotic corner; it is the same corner one axis over.

The eighth verdict's closing question has now been answered *the unit axis*, *the
frame axis* and *the section-size axis* in three consecutive rounds. The reason is
not carelessness — every round's measurement has been correct along the axis it
was taken on. It is that **a domain claim is a statement about a space, and the
envelope behind this one is sampled on two of that space's coordinates.**

**Closed when** one of: the boundary is set from an envelope that spans the axes
the corpus already demonstrates matter — section size at minimum — with the
sampling stated, and the configuration above holds under it; or the claim is
restated as what was measured ("at the gate's own section, over angles and
rolls") and `PATCH_TEST_EXACTNESS` is not represented as covering a wider domain
than that; or `orient=` gains a free vector so the corpus can carry the
counterexample and it is recorded as a known exceedance with the permutation cell
as its evidence. Whichever is taken, it is a **plan edit at §5b Q6**, not a step
commit.

**R82. (blocking) `PATCH_TEST_ROUNDOFF = 2e-11` loosens the gate 20x on eleven of
the fifteen entries it covers, none of which needed it, and I measured the defect
it lets through.** `floatfea/tolerances.py` `PATCH_TEST_ROUNDOFF`'s entry,
`tests/verification/rung1/test_corpus_configurations.py:319-336` (`_tier`).

Per entry at `e9dd32f`, through the shipped helpers. Fifteen entries are past the
boundary; **four** exceed `PATCH_TEST_EXACTNESS` and are the recorded breaches;
**eleven** pass it and had their ceiling moved `1e-12 -> 2e-11`:

```
  slender_axis_L_r_189       lam 558.1   err 9.7945e-15    was 102x below 1e-12
  slender_axis_L_r_118       lam 348.8   err 2.9968e-14    was  33x below
  slender_in_plane_y_L_r_94  lam 279.0   err 1.5577e-14    was  64x below
  nearly_solid_D_t_2p1       lam  64.4   err 2.1415e-14    was  47x below
  ... and seven more between 9.80e-14 and 8.97e-13
```

The cost, by bisecting the shipped predicate for the largest single-element
relative stiffness defect that still passes:

```
entry                        under 2e-11    under 1e-12    ratio
slender_axis_L_r_189          1.7266e-10     8.6543e-12     20.0
slender_axis_L_r_118          1.7279e-10     8.8015e-12     19.6
slender_in_plane_y_L_r_94     1.7249e-10     8.5533e-12     20.2
nearly_solid_D_t_2p1          1.7139e-10     8.5719e-12     20.0
```

So on `slender_axis_L_r_189` a `1.73e-10` stiffness defect in one interior element
now passes G2.2, where the constant caught anything above `8.65e-12`. The report's
defence is that "a looser ceiling is round-off tracking only while a real defect
still clears it by orders" — true of the `1e-6` control it quotes, and it is not
the question. The question is the smallest defect the gate can still see, and that
moved 20x on entries whose measured error never approached the constant.

**The discriminator is in the implementer's own table and the tier does not use
it.** `_tier` is a function of member lambda alone. The exponent table it rests on
says the floor depends on lambda **and** on the frame — `2.19` skew against `0.68`
axis-aligned; I measured `2.18` and `0.52` independently. The three entries above
at lambda 279–558 are exactly the axis-aligned and `in_plane_y` twins whose `0.68`
exponent is the evidence they do not need relief. The plan drops the conditioning
measure because "three twin pairs at identical conditioning differ in error by
34x, 113x and 451x" — those same three pairs are at **identical member lambda**,
so lambda does not separate them either, and the tier hands the looser ceiling to
both halves of each pair.

**Closed when** the tier's condition carries the second driver its own exponent
table names; or the eleven entries that clear the constant are asserted against
the constant and only the measured exceedances take the looser tier; or the entry
states this cost with the `1.73e-10` / `8.65e-12` pair beside it, so a later
reader knows what the label bought and what it spent.

**R83. (blocking) `PATCH_TEST_EXACTNESS_COUNTER`'s entry is byte-identical to the
previous verdict's commit. R58 asked for it, R73 named it as a site, and it has
not been touched.** `floatfea/tolerances.py:588-609`.

Extracted from both revisions and compared: **BYTE-IDENTICAL, 22 lines.** It
mentions `stubby`: no. `L/D`: no. `aniso`: no. `I_y`: no. `domain`: no. A
geometry: no. A direction of degradation: no.

The domain statement was written instead at
`test_corpus_configurations.py:424-433`, where it is correct and well argued. That
is a good comment in the wrong file: the entry is what a reader consults before
changing the number, and the entry is what R73 named. `CLAUDE.md` § Step gating
records this exact failure — R29's condition named `tolerances.py` *and* three
lines in the test file, the first was fixed and the second left. This is the
mirror image: the test file was done and `tolerances.py` was left.

**Closed when** the entry states the geometry it was measured at, the direction it
degrades in, and both configurations now known to leave its domain, with a pointer
to the test-module comment rather than a copy of it.

**R84. (blocking, reading-order item 4b) The hook's redirect narrowing opened two
new write shapes into my directories, and one of them silently truncates my corpus
to zero bytes.** `.claude/hooks/protect-reviews.sh:112`, commits `a418e38` and
`29a5ecd`.

Both are standalone `process:` commits touching only `.claude/`; neither touches
`floatfea/` or `tests/`; `docs/SUPERVISOR.md` is unchanged; and no guard *text*
was removed. The commit shape is right, so this is not the STOP-class shape
`CLAUDE.md` describes. It is still a measured regression. Exercised on thirteen
synthetic inputs at `e9dd32f`:

```
implementer `cd tests/corpus && echo x > y.txt`          DENIED   (still closed)
implementer `echo x > tests/corpus/y.txt`                DENIED
implementer `echo x 1> tests/corpus/y.txt`               ALLOWED  <- NEW HOLE
implementer `cmd 2> tests/corpus/g22_...txt`             ALLOWED  <- NEW HOLE
implementer `echo x >| tests/corpus/y.txt`               DENIED
implementer `pytest tests/corpus 2>&1`      (a READ)     allowed  (the fix works)
implementer `cd ... && cat docs/reviews/...` (a READ)    allowed  (the fix works)
implementer Write to docs/reviews/ and to tests/corpus/  DENIED
implementer NotebookEdit notebook_path tests/corpus/     ALLOWED  (R78 hole 3)
malformed stdin JSON                                     DENIED
supervisor Write to docs/reviews/                        allowed
general-purpose subagent Write to docs/reviews/          DENIED
```

The new clause is `(?<![0-9])>{1,2}(?!&)`, which excludes every redirect preceded
by a digit. `1>` and `2>` preceded by a digit are ordinary writes. Demonstrated
outside the repository:

```
$ printf 'ORIGINAL CORPUS LINE\n' > tests/corpus/g22.txt      21 bytes
$ true 2> tests/corpus/g22.txt                                 0 bytes, content []
$ echo hi 1> tests/corpus/g22.txt                              content [hi]
```

The narrowing wanted is to exclude `>&` and the `>/dev/null` duplication, not
every digit-prefixed redirect. **I am still the only writer** — the tool path and
the `agent_type` gate are intact and I confirmed both — so my verdict path is not
at risk; what is at risk is the one file whose whole value is that the implementer
did not write it.

The pattern the header now records is right and worth keeping: three widenings,
three costs to a read, no writes bought. What it does not say is that each of the
three shipped without the true positives being re-exercised, and **nothing in the
suite reads this file**, which is why 4b exists.

**Closed when** `echo x 1> tests/corpus/y` and `cmd 2> tests/corpus/y` are both
denied while `pytest ... 2>&1` on a protected path stays allowed, demonstrated on
those three inputs; and `notebook_path` joins the extractor (R78, third round).

**R85. (recordable) A third decision threshold was added outside
`floatfea/tolerances.py`, in the assertion the report offers as the two-tier
scheme's own defence, and it can be set to `1e-30` with the suite green and the
scanner silent.** `tests/verification/rung1/test_corpus_configurations.py:446`.

```python
assert smallest > 100.0 * ceiling, (  # not-a-tolerance: discrimination floor ...
```

The report: "the label is asserted, not just written: the runner requires
`smallest > 100 x ceiling` on every entry, and the tier clears by 5400x". Both
halves are true and they do not fit together. Inverting the rule: the tightest
entry over the whole corpus is `nearly_solid_D_t_2p1` at `1.0767e-07 / 2.0e-11 =
5383.5x`. The shipped `100.0` therefore has **53.8x of free travel upward and
unbounded travel downward**:

```
$ sed -i 's/assert smallest > 100.0 \* ceiling/assert smallest > 1e-30 * ceiling/'
$ python -m pytest -q
524 passed in 1.74s
```

R80's species exactly, third instance. `CLAUDE.md`: "no exceptions, no local
literals... The same rule applies to anything that functions as a tolerance under
another name: ... tier cutoffs in screening."

**Closed when** the multiplier moves to `tolerances.py` with its measured basis
(`5383.5x`, and the entry it was measured at), or the assertion is written against
the counter it already has rather than against a fresh number.

**R86. (recordable) `tolerances.py` states that a deleted function's property "is
real and asserted". Nothing asserts it and the function does not exist.**
`floatfea/tolerances.py:569-571`.

> "Equilibration remains a tested utility -- cond(K~) = 3.85e2 at every unit
> system is real and asserted -- and `floatfea/assemble/system.py` carries why it
> is not in the solve."

```
$ grep -rn "def equilibrate" floatfea/          (no match)
$ grep -rn "cond(" tests/ --include=*.py | grep -ci assert
0
```

`system.py` no longer carries why it is not in the solve; it carries why it is
gone. Three sentences inside a comment a reader consults before touching the
ceiling beside it. `CLAUDE.md` BF0's species, and one grep refutes it.

**Closed when** the paragraph describes the file as it is at the commit it is read
at.

**R87. (recordable) Four citations to a `docs/conventions.md` section that does
not exist, one of them inside a shipped error message a modeller reads; and
`BEAM_ADMISSION_L_OVER_D`'s entry states the depth formula the code records as a
rejected draft.** `floatfea/model/admissibility.py:3` and `:73`,
`floatfea/tolerances.py:156` and `:158`,
`tests/verification/rung1/test_corpus_configurations.py:43`.

The revert (`b413a3d`) removed the section, correctly. The F0 reopen commit the
plan names as the route has not happened. `grep -n "^#" docs/conventions.md` lists
fourteen sections and none is "Beam admission limit". The user-facing one:

```
"... Route it to an F7 shell sub-model; see docs/conventions.md,
 'Beam admission limit'."
```

Separately, `tolerances.py:158` gives the depth as `D = 4 sqrt(I/A)` — the formula
`admissibility.py:41-43` records as a first draft that "overstated the depth of a
thin tube by sqrt(2)". On the gate's own section it gives `0.8317 m` against the
shipped `0.600 m`, a factor of `1.3862`. R74 was a plan line stating a formula the
code stopped implementing; this is the same defect inside `tolerances.py`. And the
same entry still reads "PENDING XABIER'S CONFIRMATION" where §5b now says
confirmed — a table in `tolerances.py` left stale by a change one commit away,
which is `CLAUDE.md` BI3, added this round and violated in it.

**Closed when** the four citations resolve — the F0 reopen commit lands, or they
point at `F2.md` §5b Q5 in the meantime — and the entry states
`D_o = 2 sqrt(2I/A + A/2pi)`, the expression `_outer_diameter` computes, and its
own current status.

**R88. (recordable) `rotation_matrix` accepts `roll_rad = nan` or `inf`, returns a
matrix containing NaN with only a numpy RuntimeWarning, and the failure surfaces
at solve time as `RuntimeError: Factor is exactly singular` — a message that names
a mechanism where the cause is a bad input field.**
`floatfea/model/local_axes.py:118`.

```
roll_rad=nan: rotation_matrix RETURNS, any-NaN=True
roll_rad=inf: rotation_matrix RETURNS, any-NaN=True
RuntimeWarning: invalid value encountered in cos    local_axes.py:118
```

The degeneracy guard twenty lines above refuses a near-parallel member loudly and
explains why there is no silent fallback. A NaN roll goes straight through it.
`CLAUDE.md` § Non-negotiables: the reader rejects bad records and a validation
failure does not degrade — here it degrades into a solver crash whose message
sends the reader hunting for a mechanism. Pre-existing, not introduced this step,
found by my new `roll_field_nan` corpus entry, which is **red** at `cc8801c`.

**Closed when** `rotation_matrix` refuses a non-finite `roll_rad` and the corpus
entry goes green by raising.

**R89. (recordable) The corpus module crashes at COLLECTION on any entry whose
section or length its constructors refuse, so those shapes cannot be scored at
all.** `tests/verification/rung1/test_corpus_configurations.py:344-352`.

`INADMISSIBLE = [e["id"] for e in ENTRIES if _inadmissible(e) is not None]` runs
at import, and `_inadmissible` calls `_section` and `member_l_over_d` unguarded.
Measured, each line added alone:

```
id=section_negative_wall ... t=-0.01200    ERROR ... Interrupted: 1 error during collection
id=stations_negative     ... stations=-9.67 ERROR ... Interrupted: 1 error during collection
```

Both are `expect=raise` shapes the module is supposed to be able to score.
Instead the whole file is uncollectable and every other entry stops being
measured — a failure mode worse than a silent pass, and invisible until someone
writes the entry. Both lines are recorded in the corpus file as comments rather
than committed, because a corpus that cannot be run is not a corpus.

**Closed when** `_parse_line` validates `stations` and the section parameters as
values, or `INADMISSIBLE` is computed lazily so a refusing entry produces a
failing test rather than a collection error, and both lines can be carried as
entries.

**R90. (recordable) `member_lambda` reads `I_z` alone, so the tier cannot see the
weak-axis slenderness; `member_l_over_d` still has no shape guard.**
`floatfea/model/admissibility.py:82-95` and `:51-55`.

```
entry                  I_y/I_z   lambda(I_z)   lambda(weak axis)   tier
aniso_I_y_half             0.5          46.5                65.8   exactness
aniso_I_y_twentieth       0.05          46.5               208.0   exactness  (mine)
aniso_I_y_half_lam59       0.5          59.0                83.4   exactness  (mine)
```

Assertion-domain blindness in its recorded form: the collection the tier inspects
cannot contain the weak-axis case, so a pass certifies nothing about it. Today
`Section.__post_init__` forces `I_y == I_z` for every shape `basis.kappa` admits,
so nothing in production reaches it — which is precisely the argument that made
R73's `_outer_diameter` inversion "fine until the first non-circular section", and
`warn_outside_validated_domain` is named as an F3 builder dependency that will run
per member. R73's third closing condition — that `member_l_over_d` raise for a
shape it has no inversion for — was not done, and the new function inherits the
defect.

**Closed when** both functions take the governing second moment explicitly or
refuse a section they have no inversion for, per the rule `basis.kappa` applies
twenty lines away.

## Tolerances touched

| name | old | new | form | counter | justification located |
|---|---|---|---|---|---|
| `PATCH_TEST_COND_FACTOR` | `5.0` | **removed** | — | — | `F2.md` §D7 item 6. Verified gone: `grep -rn "PATCH_TEST_COND_FACTOR" floatfea/ tests/` returns nothing. The right answer to the eighth verdict. |
| `PATCH_TEST_COND_FACTOR_COUNTER_DEFECT` | `3.0e-10` | **removed** | — | — | with its ceiling. |
| `COND_UNIT_INVARIANCE` | `1e-6` | **removed** | — | — | `equilibrate` had no other consumer. One of R63's three silently-widenable ceilings disappears this way — by removal, not by fix. |
| `COND_UNIT_INVARIANCE_COUNTER` | `1.0e-3` | **removed** | — | — | as above. |
| `G22_VALIDATED_MEMBER_LAMBDA` | — | `60.0` | dimensionless: member `L/r`. STRUCTURAL, no counter required (AO2) — correctly classified: it is a domain boundary, not an error ceiling | none, correctly | `tolerances.py` entry + `F2.md` §5b Q6. **The axis is right and I verified it independently** — my own 2-D grid, my own seed and meshes, gives `+2.18 +/- 0.15` on member lambda in skew against `+0.52 +/- 0.20` axis-aligned, and element `L/r` held fixed at `27.5` still moves the error `183x` / `143x` across `n = 3..12`, so it is refuted as the governing axis. **The value is not defensible as stated**: the envelope behind it spans angles and rolls at one section, and adding the section-size axis puts a clean admissible member at `7.58x` the ceiling inside the domain (**R81**); "10x of margin" measures `1.002x` within the corpus schema. The `n = 2/5/11` table showing 35–57x is the strongest thing in the entry and is correct — the boundary really is a property of this test at its mesh, and saying so plainly is what stops F3 inheriting it. |
| `PATCH_TEST_ROUNDOFF` | — | `2e-11` | dimensionless, the same quantity as `PATCH_TEST_EXACTNESS`. Correct form, and "round-off tracking rather than exactness" is the honest name for what it is | `PATCH_TEST_ROUNDOFF_COUNTER = 1.0e-7`, measured in the same quantity on the tier's own configurations — correct in form; **its 5400x separation is asserted through a `100.0` literal outside `tolerances.py` (R85)** | `tolerances.py` entry. **It is a widening for eleven of the fifteen entries it covers**, all of which cleared the constant, three of them by 33–102x, and the defect it admits on `slender_axis_L_r_189` is `1.73e-10` against the constant's `8.65e-12` — 20.0x, by bisection (**R82**). The four recorded breaches are genuine and this tier is the right instrument for them. |
| `PATCH_TEST_EXACTNESS` | `1e-12` | `1e-12` | **unchanged** | unchanged | the comment gains the validated-domain paragraph, which is R81's subject. |
| everything else | — | unchanged | — | — | `git diff 6191f9c..HEAD -U0 -- floatfea/tolerances.py` filtered to `Final[float]` gives **two additions and four deletions, no modifications.** **No accuracy ceiling was widened in place, and none was loosened to rescue a red.** Both additions are new quantities under a plan that authorised them before the code was written. |

No golden file moved. No test is skipped or `xfail`ed; the suite has zero skips —
and the eighth verdict's instruction that the four breaches be kept rather than
deleted was honoured.

One sentence in the report the diff does not support. **"All five of the
reviewer's reds are answered, none by narrowing a check."** Four are. The fifth,
`aniso_I_y_500x`, is answered by putting
`if not entry.get("extra","none").startswith("I_y_over_I_z=")` in front of the
counter assertion, which is narrowing the check's domain. The narrowing is
*defensible* — the reasoning at `:424-433` is right that no production path builds
such a section, and lowering the counter instead would have been worse — but the
sentence is not what the diff shows, and the replacement control it points to is
R85's literal. The accurate form: four by fixing, one by excluding a domain, with
the exclusion argued.

## Next step opens when

Step 5 (V1.1, rigid-body modes) does not begin. This is a **STOP**: the plan
reopens at `F2.md` §5b Q6 and §D7 item 7, and the domain is settled there — not
inside another step commit, and not by moving `60` until the counterexample stops
firing, which is the cheapest response and is the one `CLAUDE.md`'s first
non-negotiable exists to forbid.

1. **R81 — the validated domain.** The configuration in the header is the thing to
   answer first, and nothing else in step 4 is worth reading until it is answered.
   Either the envelope spans the axes the corpus already shows matter and the
   boundary follows from it, or the claim is restated as what was measured. If the
   answer is "record it as a known exceedance", the `orient=` field needs a free
   vector so the corpus can carry it — and that request comes to me.
2. **R82 — the second tier's cost.** Both halves: the eleven entries that never
   needed the relief, and the `1.73e-10` defect it admits, in the entry.
3. **R83 — `PATCH_TEST_EXACTNESS_COUNTER`'s own entry**, the site named twice
   before this verdict and untouched both times.
4. **R84 — the two write holes**, demonstrated closed on the three inputs above,
   together with `notebook_path` (R78, third round).

R85 through R90, together with R6, R16, R25, R30, R31, R32, R33 (outside G2.2),
R36, R50, R52, R62, R63, R65, R76, R77, R78, R79 and R80, may be answered in the
next report's `Carried` section, **and that section must list every one of them,
open or answered.** Revision 9 listed eighteen and missed none; that is the
standard now.

**Adversarial corpus (BE3): 12 new entries committed, all unseen by the
implementer; 11 caught, 1 red.** `tests/corpus/g22_model_configurations.txt`, now
**62**, committed separately at `cc8801c` immediately before this verdict and
touching no code. Two further shapes are recorded in the file as comments rather
than committed, because each takes the module out at collection (**R89**) and a
corpus that cannot be run is not a corpus — so the honest coverage number is
**11 of 14 shapes**. Full suite with the corpus applied: **1 failed, 545 passed**.

The twelve are the axes this round created: the **section-size axis inside the
validated domain** (two entries at `0.532` and `0.356`, plus the free-orientation
counterexample recorded in the file because the schema cannot express it); the
**tier boundary as a discontinuity** (a straddling pair at member lambda 59 and 61
where the error moves `2.3x` and the ceiling moves `20x`, plus the axis-aligned
twin); **tier 2 applied where nothing asked for it** (two entries 120x and 130x
below the constant); the **weak axis `member_lambda` cannot see** (two anisotropic
entries); **R79's kappa error moved inside the new domain**; and the **parser's
remaining unvalidated field values** (one green, one red, two uncollectable).

**Ten consecutive rounds have found no element defect**, and the defects found
this round that are not comments are all in the machinery around it: a domain
claim, a tier, a hook, and a NaN that reaches the solver. Per the guard, that
still means "not yet contradicted", and it stays that way until V5.1 puts
CalculiX on the other side.

**Witness channel unavailable.** No git remote, so no PR and no `[witness ...]`
comment; per `docs/SUPERVISOR.md` that is an unavailable check, not a pass. Nine
consecutive reviews by one reader.

**The pattern, ninth round — and the one thing that changed.** The eighth verdict
asked which axis every ratio was measured along. This round answered it correctly
for the *form*: the form is gone, the frame table is preserved as evidence, the
axis behind the new boundary is right and I reproduced it independently rather
than accepting it. Then the same failure repeated one level up, in the envelope
behind that boundary's *number*. The standing question for whatever comes next is
narrower than last round's, because the form question is now genuinely settled:
**for the domain this gate claims, name every coordinate of the space it is a
domain in, and say which of them the envelope was sampled on.** Three rounds
running, the answer has been "two of them".
