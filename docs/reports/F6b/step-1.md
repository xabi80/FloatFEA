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
