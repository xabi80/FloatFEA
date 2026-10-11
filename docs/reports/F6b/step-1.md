# F6b step 1 — the truss sizing

# Revision 1 — the sweep, the hand table confirmed, and a CoG that no truss in the grid can reach

Answers: FI opens the step
Answers file: `docs/reports/F6b/step-1-answers.json`

**2026-10-11.**

## 1. The schedule, and what this revision is

**Measured against FI5's 3 days, i.e. 14 October.** The deliverable exists on 11 October,
the day the directive landed. **The date holds** with margin.

Under FG1 this step gets one reviewed revision, then EQ0 closure. FI5 asks the reviewer to
recompute the governing chord force and its required area by hand; § 2 gives both with the
arithmetic laid out so that recomputation is a check rather than a re-derivation.

**Nothing in `floatfea/` or `tests/` changed.** FI0 says post-processing only, and that is
literally what this is:

```
claim  the increment touches no element, no solver and no test
cmd    git diff --stat HEAD -- floatfea tests
out    (empty)
rule   FI0: "Post-processing only: no FloatSim, and the frame model is unchanged"
```

## 2. The answer, and the arithmetic the reviewer is asked to check

| group | section | shallowest mass-consistent | chord `A` [m²] | line mass [kg/m] | `μ` [kg/m] | ratio |
|---|---|---|---|---|---|---|
| platform (4), L = 50 m | box | `h = 3`, `b = 8` | 0.2234 | 9175 | 9375 | **0.979** |
| platform (4), L = 50 m | triangle | `h = 4`, `b = 8` | 0.2688 | 8886 | 9375 | **0.948** |
| hubs (12), L = 25 m | box | `h = 2`, `b = 2` | 0.2454 | 10108 | 15000 | **0.674** |
| hubs (12), L = 25 m | triangle | `h = 2`, `b = 2` | 0.3332 | 9959 | 15000 | **0.664** |

**The governing chord, with every term shown.**

```
claim  the governing chord force at the platform's shallowest box, from FI1(a)'s formula
cmd    the sizing run's own output for (platform, box, h=3, b=8)
out    governing chord   : platform:hub2_arm ROOT T=12.5s chord bot_-b
       chord force       : -4.685711e+07 N   (inelastic)
       required chord A  : 0.223439 m^2
rule   FI1(a): `chord force = N/4 ± My/(2h) ± Mz/(2b)`, signs preserved
cell   the three terms at that row, one per line, so the total is checkable by addition:
         N/4        = -8.0025e+04 / 4      = -2.0006e+04
         My/(2h)    =  1.801835e+08 / 6    =  3.003058e+07
         Mz/(2b)    =  2.689043e+08 / 16   =  1.680652e+07
         bot_-b     = N/4 - My/(2h) - Mz/(2b)
                    = -2.0006e+04 - 3.003058e+07 - 1.680652e+07
                    = -4.685711e+07  N          <- matches the run
       and the area: compression governs over tension by 1.5% here, so
         A_tension  = 4.685711e+07 / 213.0e6   = 0.219987 m^2
         A_required = 0.223439 m^2              (section 3.2.2, K = 1.0, L = 3 m)
judge  **tension would give `0.2200 m²` and the clause gives `0.2234 m²`.** The chord is
       stocky at `KL/r` from a 3 m panel, so `F_a` sits just under `0.6 F_y` and the
       compression branch costs 1.5%.
```

**The line mass, likewise, so the `0.979` is checkable:**

```
claim  the line mass at that answer, from FI2's formula
cmd    4 chords + 4 braced faces of 45° diagonals, x rho, x the joint allowance
out    chord steel    = 4 x 0.223439              = 0.893756 m^2
       diagonal steel = 4 x 0.021670 / sin 45°    = 0.122584 m^2
       line mass      = (0.893756 + 0.122584) x 7850 x 1.15 = 9175.0 kg/m
       ratio          = 9175.0 / 9375             = 0.979
rule   FI2: `(Σ chord A + diagonal A·length per panel / panel length)·ρ`, x 1.15
judge  the diagonals are 12.1% of the steel area and the joint allowance is a flat 15%.
```

## 3. FI4, item by item

**(i) the `My`/`Mz` split.**

```
claim  the split at the governing station, and the group's two envelopes
cmd    the sizing run's own `splits` block for the platform group
out    governing station        : platform:hub2_arm ROOT, T = 12.5 s
         My                     : 1.801835e+08 N.m
         Mz                     : 2.689043e+08 N.m
         resultant              : 3.236906e+08 N.m   Mz/resultant = 0.831
       dynamic envelope, group  : max|My| = 2.232419e+08, max|Mz| = 2.689043e+08
       static, group            : max|My| = 1.916016e+08, max|Mz| = 0.000000e+00
rule   EZ2/FA0's governing basis, enveloped over the group's members and stations
judge  the static `max|Mz|` is **identically** zero, not round-off: gravity is vertical
       and the arms lie in one plane, so there is no horizontal static load to produce
       any. **All of the horizontal demand is dynamic.** `Mz/resultant` is a direction
       cosine and is named as one rather than as a share -- the two components are
       orthogonal, so nothing is "83% Mz" in an additive sense.
```

**THE SPLIT IS THE ARM'S ORIENTATION, NOT THE PHYSICS, AND IT IS THIS REVISION'S ONE REAL
DECISION.**

```
claim  Mz is large on two platform arms and round-off on the other two, and the four are
       geometrically identical
cmd    the per-arm envelope over the governing basis
out    platform:hub1_arm  max|My| = 2.1826e+08   max|Mz| = 2.8505e-01
       platform:hub2_arm  max|My| = 1.8018e+08   max|Mz| = 2.6890e+08
       platform:hub3_arm  max|My| = 2.2324e+08   max|Mz| = 3.2489e-01
       platform:hub4_arm  max|My| = 1.8018e+08   max|Mz| = 2.6890e+08
rule   the local triads, computed rather than assumed: all four arms have local z
       vertical, so My is vertical bending and Mz horizontal
       (`docs/milestones/F6b.md` § 2a)
judge  at heading 0° the along-wave arms take the demand as `My` and the transverse arms
       take the SAME demand as `Mz`. **So `b` may not be made small because `Mz` is small
       on the arm one happens to read**, and one section per group has to carry the larger
       moment in both planes. Sizing each arm for its own orientation would deliver four
       different platform arms at one heading and is void the moment increment 3 moves the
       heading. Decided, not asked; § 2b of the plan records it and the deliverable states
       it as a finding rather than burying it as an assumption.
```

**WIDTH BUYS MORE THAN DEPTH, which inverts the premise behind a *shallow* truss** — at
`h = 3` only `b = 8` is mass-consistent, while at `b = 8` every `h ≥ 3` is.

**(ii) The stiffness proxy**, reported as a note, as FI4 asks.

```
claim  the truss's bending-stiffness proxy against the stand-in tube's second moment
cmd    the sizing run's own EI_proxy fields at the headline answer
out    the stand-in tube            : I = 0.888 m^4
       the headline truss, A_c h^2  : 2.0110 m^4   = 2.26x the stand-in
       the headline truss, A_c b^2  : 14.3001 m^4
rule   FI4(ii), and the stand-in's `I` is F6/F6a's own tube
judge  **it is an UPPER bound**: a chord pair at separation `h` contributes `A_c h^2/2`,
       so the proxy counts both pairs at full lever. Forces do not depend on it here
       (FI0), which is why this is a note.
``` **It is an upper bound** — a chord pair at separation `h` contributes `A_c h²/2` — and
the honest consequence is that a truss stiffer than the stand-in by this much would change
the dynamic response, so F4 wants re-running once a form is chosen. That is a pointer, not a
correction to anything here.

**(iii) The hand table is CONFIRMED, to every figure given.**

```
claim  the two-chord table, reproduced, and what it omits
cmd    F = M/h at M = 324 MN.m; A = F/sigma at sigma = 213 MPa; then section 3.2.2
out     h [m]    F = M/h [N]  A tension [m2]  A compression   ratio       branch
             3     1.0800e+08          0.5070         0.5121   1.010   inelastic
             4     8.1000e+07          0.3803         0.3863   1.016   inelastic
             5     6.4800e+07          0.3042         0.3113   1.023   inelastic
             6     5.4000e+07          0.2535         0.2616   1.032   inelastic
rule   Xabier's table: 0.51 / 0.38 / 0.30 / 0.25 m^2
judge  **confirmed at all four depths.** `sigma = 213 MPa` is `0.6 F_y` for `F_y = 355`,
       so the table is a tension-only, bending-only, two-chord figure and it is right as
       that. **Compression buckling adds 1.0% to 3.2%** -- little, because `K = 1.0` with
       `L` = the panel length leaves the chord stocky. What it omits that matters more is
       the diagonals (12.1% of the steel area) and the joint allowance (a flat 15%), so a
       four-chord box at the same depth lands near 2x the hand figure once both are in.
```

**(v) The CoG flag, and it is sharper than a sensitivity.** The remainder's height is **not
a modelling choice** — it is forced.

```
claim  the remainder's height is what the deck CoG REQUIRES, in closed form
cmd    `_build_body`'s own placement rule, inverted, against the built model
out    z_remainder(f) = (z_cog - f z_joint) / (1 - f)
         joints      z = 24.668 m
         deck CoG    z = 35.000 m   (10.33 m above the joints)
         remainder   z = 65.995 m   (41.33 m above), 6.2500e+05 kg at f = 0.75
         closed form   65.995 m, error 1.42e-14 m
       the highest CoG a truss of depth h can reach is z_joint + h/2:
         h =  2 m -> 25.668 m, shortfall  +9.332 m
         h =  6 m -> 27.668 m, shortfall  +7.332 m
         h = 10 m -> 29.668 m, shortfall  +5.332 m
rule   every arm midpoint lies in the joint plane, so the arms' first moment is
       `f·deck_mass·z_joint` and the remainder's height follows exactly
judge  **the closed form reproduces the model's own remainder height to 1.42e-14 m**, so
       this is the model's arithmetic and not an approximation of it. The deck CoG needs a
       truss **20.66 m deep** for steel to reach it, against a sweep that stops at 10 m.
       **So the inconsistency is not between the truss and the remainder's HEIGHT — it is
       between the truss and the deck CoG itself**, at every depth in the grid and whatever
       `f` is, because the closed form puts the leftover mass HIGHER as `f` falls.
```

**And the narrow answer to what FI4(v) literally asks.** None of the governing *horizontal*
moment comes from the remainder's height: the remainder sits on the centreline, so its
weight produces no horizontal-plane moment, and a horizontal acceleration at `41.33 m`
produces an overturning couple about a *horizontal* axis, which the arms carry as `My`. The
height's consequence is in `My` and in the CoG arithmetic above. **Stated as narrowly as it
was measured** — this is a geometric argument plus the per-arm table in (i), not a re-solve,
and a re-solve is what it would take to attribute `My` between the remainder and the arms'
own mass.

## 4. One finding of my own, in the torsion term

FI1 specifies a torsion shear flow, and the torque it acts on is tiny:

```
claim  the torque available to the shear-flow term, against the moments beside it
cmd    the governing envelope's max|T| per group
out    platform  max|T| = 2.4832e+02 N.m
       hubs      max|T| = 1.1175e+03 N.m
rule   against `max|My|` and `max|Mz|` of order `1e+08 N.m` in the same envelope
judge  so the term was expected to vanish -- which is the circumstance in which a term
       gets dropped, and the reason it was kept.
```

**It was first computed by differencing, and the differencing returned exactly zero.**

```
claim  the torsion share, by two routes
cmd    route 1: resolve each row twice, with T and with T = 0, and subtract
       route 2: form the term from its own formula, q·h / face shear
out    route 1: 0.000e+00                 <- published, and wrong
       route 2: 2.984057271793956e-17     <- and it matches the hand value exactly
cell   one variable moved: how the same quantity is formed. At the governing row
       `T = -1.411678e-09 N·m` against a face shear of `2.956708e+06 N`, so the two
       resolutions agree to 16 significant figures and the subtraction underflows.
rule   G4.1's rule in another guise: a small quantity is formed from its own terms, never
       by subtracting two large ones
judge  **`0.000e+00` would have been a cancellation published as a result.** Caught by the
       figure disagreeing with a hand calculation, not by any test. The worst share over
       any face at the headline answer is `2.275e-04`, which is the number worth having.
```

**And the repair was present and correct for one run while the document still said zero**,
because two stale differencing lines survived three rows below the new assignment and
overwrote it. The lesson is the ordering, not the arithmetic: a replacement that leaves the
thing it replaced still executing is not a replacement.

## 5. What was built

* `scripts/measure/f6b_truss_sizing.py` — FI1's two resolutions, FI2's sizing by bisection
  on `D` at the declared `D/t`, FI3's sweep, FI4(i)/(iii)/(v)'s measurements. Reuses
  `floatfea/checks/api_wsd.py`'s clause functions rather than transcribing them a second
  time.
* `scripts/measure/f6b_report.py` — FI5's deliverable, generated end to end.
* `results/F6b/truss_sizing.md` and `.csv`, plus the JSON the generator reads.
* `docs/milestones/F6b.md` — the plan, with FI verbatim and the derivations § 2 records.

## 6. Tolerances

**None.** Every number FI fixes is a declared input, carried in the deliverable's label
rather than in `tolerances.py`:

```
claim  no tolerance was added or moved, and what the declared inputs are instead
cmd    git diff --stat HEAD -- floatfea/tolerances.py
out    (empty)
rule   FI's declared inputs, reproduced from the directive: D/t = 24; joint allowance
       1.15; diagonals at 45 deg; rho = 7850 kg/m^3; F_y = 355 MPa; tension 0.6 F_y;
       compression section 3.2.2 at K = 1.0 with L = the panel length; h in
       {2,3,4,5,6,8,10} m and b in {2,3,4,5,6,8} m
judge  none of them is chosen to make two numbers agree, which is the test `CLAUDE.md`
       applies, and no counter is declared, so EU1 does not arise.
```

## 7. The suite, lint and the boundary state

```
claim  lint, format and types at this tree
cmd    python -m ruff check floatfea tests scripts ; python -m black --check ... ; mypy
out    All checks passed!
       137 files would be left unchanged.
       Success: no issues found in 37 source files
```

**The suite is not re-run and the reason is a measurement, not an omission:** `git diff
--stat HEAD -- floatfea tests` is empty, so no test's subject changed. The whole-suite line
and the CI table are FC1's class and land in the follow-on commit.

**The boundary state (EG3).** This is the milestone's first report, so there is no prior
verdict and the state-(1) ids are red until this revision's verdict exists. **The
`step-under-execution` marker moves from `F6a.md` to `F6b.md` in the same commit as this
report**, which is what `CLAUDE.md` requires and what the repaired hook now checks: the
marker decides which verdict is read, and the no-verdict sweep (R799, R800) refuses this
report until a verdict exists for it.

## 8. Carried

**Checked, nothing carried.** F6a closed with no blocking item open; its ledger — R788,
R789, R790, R791 — stays on `docs/closure/F6a.md` and is not re-opened here. R793 and R798
through R800 were closed or withdrawn in the hook sequence that preceded this increment.

```
claim  there is no prior verdict for this milestone, so the carry is empty by fact
cmd    ls docs/reports/F6b/ ; ls the reviews directory for F6b
out    step-1.md
       (no such directory)
rule   CZ0: a blocking item still open carries by name into the next step's `Carried`.
       There is none.
```

## 9. What this revision does NOT do

No joint or connection design, no secondary bending, no system buckling of the bracing, no
heading but 0°, no mass iteration, and no re-solve — so the stiffness note in § 3(ii) is a
pointer to a future F4 run and not a result. It also does not attribute `My` between the
remainder and the arms' own mass, which § 3's narrow answer says plainly and which a
re-solve is what it would take.

# Revision 2 — R801: the panel geometry had two readings and I used half of each

Answers: verdict 124 @ 6e32716
Answers file: `docs/reports/F6b/step-1-answers.json`

**2026-10-11.**

## 1. The schedule, and what this revision is

**Still measured against FI5's 3 days, i.e. 14 October.** Revision 1 landed on 11 October
and this repair lands the same day. **The date holds.**

Verdict 124 held on one item. It is a real geometry defect of mine, it is CZ0 (a) as
amended by EZ0, and **it moved the headline** — which is the strongest form the finding
could have taken.

## 2. R801 — the defect, and why the repair is not a patch

**What was wrong.** `f6b_truss_sizing.py` sized the chord with `panel_length=min(h, b)`
while its own comment said *"panel length = the face dimension"*. A box of depth `h` and
width `b` has **two** face dimensions, so FI1's "diagonals at 45° (panel length = the face
dimension)" has two self-consistent readings — and I took **the shorter buckling length
from one and the shorter diagonal from the other**. That is the favourable half of each,
and it is not a reading of FI1 at all.

```
claim  the two readings, and that the published cell fails under BOTH of them
cmd    the sweep re-run with each reading computed separately
out    platform box h=3 b=8   per_face_45 = 1.023 (chord L = 8 m)
                              uniform_panel = 1.027 (chord L = 3 m)
                              consistent under both: False
       the cell revision 1 published as 0.979
rule   mass-consistency is `truss line mass / assumed μ ≤ 1.0`
judge  **the answer was taken at the grid's most extreme aspect ratio, 8:3, which is
       exactly where `min(h, b)` is most wrong.** Under `per_face_45` a corner chord is
       braced every `h` by the vertical faces and every `b` by the horizontal ones; the
       chord is a circular tube so `r_y = r_z`, and it buckles over `max(h, b) = 8`, not
       3. Under `uniform_panel` the chord's `L = 3` stands but the two 8 m faces'
       diagonals are then at `atan(8/3)` and `hypot(3, 8)` long, not `3·√2`.
```

**What the repair is.** The geometry is **stated once**, in a named constant and a single
`panel_and_diagonal()` that returns the chord's buckling length, the diagonal's length and
the diagonal's steel per unit length for a given reading — so the two cannot drift apart
again. **Both readings are swept and both are published**, because which one FI means
changes the answer and a reader needs to see the recommendation survive either.

**Three things changed with it**, and each is a consequence rather than an extra:

* **Each face's diagonals are sized for that face's own shear.** Revision 1 sized one
  diagonal area from the worst face shear anywhere and applied it to all four faces. FI2
  asks for each member's governing case and station, which that cannot give.
* **The diagonal's buckling length is its own length**, `hypot(panel, dimension)`, not the
  panel.
* **`mass_ratio` is gone as a single column.** The CSV and JSON now carry
  `mass_ratio_per_face_45`, `mass_ratio_uniform_panel` and `mass_ratio_worst`, and the
  headline is keyed on `consistent_under_both`. **BP0: the `A` column, the line-mass
  column and both ratio tables are regenerated, not patched** — the deliverable is
  produced end to end from the new JSON.

**The corrected answer.**

```
claim  the shallowest truss consistent under BOTH readings, per group and section
cmd    the regenerated sweep
out    platform box       h = 4 m, b = 6 m   per_face_45 0.970   uniform_panel 0.963
       platform triangle  h = 4 m, b = 8 m               0.923               0.917
       hubs     box       h = 2 m, b = 2 m               0.652               0.652
       hubs     triangle  h = 2 m, b = 2 m               0.662               0.662
rule   FI3's headline: the shallowest mass-consistent truss per group
judge  **the platform box moves from (3, 8) to (4, 6)**, which is the verdict's own
       answer. The platform triangle stays at (4, 8). The hub answers are untouched
       because they sit at `h = b = 2`, where the two readings coincide.
```

**The control, and it is the reason to trust the rest of the grid:** where `h = b` the two
readings must give identical numbers, and they do.

```
claim  at h = b the two readings coincide, exactly
cmd    the regenerated sweep, the cells where h equals b
out    hubs     box       h=2 b=2   0.652 vs 0.652
       hubs     triangle  h=2 b=2   0.662 vs 0.662
       platform box       h=5 b=5   0.964 vs 0.964
rule   at h = b, `min(h,b) = max(h,b)` and every face has the same dimension, so the two
       readings are the same geometry and must give the same number
judge  they do, which is what says the difference elsewhere is the geometry and not a
       bug in one of the two paths.
```

```
claim  how much of the grid the choice of reading actually decides
cmd    count the cells where the two readings disagree about mass-consistency
out    cells swept                           : 168
       cells where the two readings DISAGREE :   1
         platform  triangle  h=5 b=6   1.003 vs 0.999
rule   consistency is `ratio ≤ 1.0` under each reading separately
judge  **one cell in 168**, and it is not a headline. So publishing both and requiring
       both costs almost nothing and the conclusion is robust to the reading — which is
       the fact revision 1 could not state, because it had computed neither reading.
```

**My figures differ from the verdict's at the old cell, and the reason is a change it did
not make.** It measured the two readings with revision 1's single diagonal area; I also
moved to per-face diagonal sizing, so the diagonal steel differs.

```
claim  the two measurements of the same cell, and what the difference is
cmd    the verdict's own figures for (platform, box, 3, 8), against mine
out    verdict 124 : per_face_45 = 1.007   uniform_panel = 1.009
       this sweep  : per_face_45 = 1.023   uniform_panel = 1.027
rule   both exceed 1.0, so the cell is mass-inconsistent under either, which is the
       finding and is unaffected by the difference
judge  mine are higher because each face is now sized for its OWN shear and each diagonal
       for its OWN length; the verdict's are the same geometry with revision 1's single
       diagonal. **The verdict's conclusion and its headline `(4, 6)` are reproduced.**
```

## 3. The two closure items

**The `1 skipped`, named — and it is NOT new this milestone.** The verdict records it as
"new this milestone, the only line my run has that F6a's did not". Measured:

```
claim  which test skips, why, and whether it is new
cmd    grep the skip site; then grep F6's own step-2 verdict for the same line
out    tests/test_report_carried.py:2771
         test_a_RED_suite_is_named_in_the_report
         pytest.skip("reported by test_the_report_carries_a_WHOLE_SUITE_count")
       docs/reviews/F6/step-2.md:3524
         out    SKIPPED [1] tests/test_report_carried.py:2429: reported by
rule   the project's rule is that an empty parameter set is an error, not a skip -- so a
       skip has to be accounted for by name
judge  **it is a deliberate deferral, not a gap**: `test_a_RED_suite_is_named_in_the_report`
       needs the whole-suite line, and when that line is absent it defers to the test whose
       job is to report its absence rather than double-reporting. **It is state-dependent,
       not new** -- it fires in exactly the states where the report has no whole-suite line
       yet, which is every pre-follow-on-commit state, and F6's step-2 verdict records it at
       the then line number 2429. The verdict's F6a runs were at commits where the line was
       already present.
```

**The caution is accepted and recorded.**

```
claim  the two declared inputs the answer scales most directly with
cmd    the sizing run's own `inputs` block
out    D_over_t         : 24
       joint_allowance  : 1.15
rule   the line mass is linear in the joint allowance and the chord area scales with
       `D/t` through both the area formula and `r`
judge  they do behave like tolerances in that sense, which is the verdict's point.
``` They stay declared inputs rather than entries in
`tolerances.py` because neither was chosen to make two numbers agree — which is the test
`CLAUDE.md` applies — but **a reader sizing steel from this document should treat both as
dials, and the deliverable's label says INDICATIVE for that reason among others.** If
increment 2 wants either as a tolerance with a justification, that is a directive, not a
discretionary edit.

## 4. What the reviewer confirmed, recorded so it is not re-derived

**Every figure in this section is the reviewer's, quoted from verdict 124 rather than
re-measured by me** — that is the point of recording them, so the next revision does not
re-derive what has been checked.

```
claim  what verdict 124 confirmed, in its own figures
cmd    python -c "print the lines of this milestone's verdict that carry each result"
out    FI5's hand recomputation: chord force exact, area to five figures
         (A = 0.22345 by hand against the published 0.223439, at the old cell)
       FI1(b)'s triangle derived from first principles, independently: correct
       FI4(iii)'s four values confirmed by hand: 324/639, 324/852, 324/1065, 324/1278
       monotonicity: 7.54M evaluations, zero non-monotone pairs, never more than one
         sign change -- plus a proof, since at fixed D/t `r` is proportional to `D` so
         `F_a` rises to 0.6 F_y while |F|/A falls as D^2, and section 3.2.2(b)'s local
         reduction depends on D/t alone, which is held
       the torsion figure confirmed to six figures
       FI4(v)'s narrow answer: acceptable, no cell required
       the CoG closed form: reproduced independently
rule   FI5 asks the reviewer to recompute the governing chord force and its area by hand
judge  **the monotonicity result answers the one thing I flagged as unproven** -- I had
       said the bisection assumes a single root and that I had not shown it. It is shown,
       and the bisection's root is the root. The warning I gave about FI1(b) was also
       right: both equilibrium checks close for a wrong `I` with consistent levers, so the
       derivation and not the checks is what had to be read, and it was.
```

## 5. Tolerances

**None, unchanged.**

```
claim  no tolerance was added or moved by this revision either
cmd    git diff --stat HEAD -- floatfea tests floatfea/tolerances.py
out    (empty)
rule   no counter is declared, so EU1 does not arise
```

## 6. The suite, lint and the boundary state

```
claim  lint, format and types at this tree
cmd    python -m ruff check floatfea tests scripts ; python -m black --check ... ; mypy
out    All checks passed!
       137 files would be left unchanged.
       Success: no issues found in 37 source files
```

The deliverable regenerates byte-identically from the new JSON. **The suite is not re-run
and the reason is still a measurement:** `git diff --stat HEAD -- floatfea tests` is empty,
so no test's subject changed by this revision.

**The boundary state is EG3 state (2) now:** verdict 124 exists and this revision answers
it, so the state-(2) ids are red until this commit lands and clear with it. The
whole-suite line and the CI table remain FC1's class.

## 7. Carried

<!-- generated: scripts/carried_table.py -->

| item | status | the verdict's own subject |
|---|---|---|
| R788 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R791 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R800 | **not classified in this verdict** — carried in from an earlier one | no clause this generator can cut -- see the verdict's Carried section |
| R801 | **answered** — §2 | The declared truss geometry is self-inconsistent for h ≠ b, and BOTH ways of resolving it move... |

Every site verdict 124 names is touched: `scripts/measure/f6b_truss_sizing.py:298` and its
line 309 comment are both gone, replaced by `GEOMETRIES` and `panel_and_diagonal()`; the
deliverable and the CSV are regenerated.

## 8. What this revision does NOT do

It does not choose between the two readings. FI1's words admit both, the answer survives
both, and picking one is a design decision rather than a measurement — so the deliverable
reports both and says which cell survives either. If FI meant one of them specifically,
that is a one-line directive and the sweep already carries the numbers.
