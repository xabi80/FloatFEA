# Code checks — API RP 2A-WSD tubular members — DRAFT FOR LOCK (EY4)

**Status: DRAFT. Not locked, not open for execution.** Drafted by EY4 for Xabier's lock
by 12 October. Two steps, per EY4.

---

## 0. THE MILESTONE NUMBER NEEDS DECIDING BEFORE THIS LOCKS

**EY4 says "the code-check plan (F5 per PLAN.md)". `PLAN.md` puts code checks at F6, not
F5**, and the two are different milestones with different gates:

```
cmd    grep -n "^### F5\|^### F6" PLAN.md
out    346:### F5 — Screening and load case generation · *Week 6*
out    357:### F6 — Post-processing and code checks · *Week 7–8*
```

`PLAN.md`'s F5 is "response metric extraction, snapshot selection, envelope convergence
check", with **G5.1** (the case list is reproducible) and **G5.2** (envelope convergence).
Its F6 is "member force recovery, stress recovery at circumferential points on tubulars,
member utilisation, envelope reporting, VTK output", with **G6.1** (each check against an
independent hand calculation), **G6.2** (stress recovery against CalculiX) and **G6.3**
(the envelope report regenerates identically).

**The content EY4 specifies is F6's, and the gate it most needs is G6.1.** But three
directives have now called the next milestone F5 — EV1's third assertion was "deferred to
F5", EX4 recorded that deferral in `F4.md` § 8, and EY3 sends step 3's carried items to
"F5's ledger". Those are structural-FE items; they sit naturally beside code checks and
not beside screening.

So one of two things is true and I am not guessing which:

1. **Screening is being skipped or folded**, and the next milestone is code checks called
   F5. Then `PLAN.md` § F5/F6 needs renumbering, and G5.1/G5.2 need a home or an explicit
   withdrawal — G5.2's envelope convergence is the one that matters here, because this
   plan's utilisations ARE the governing quantities it would converge.
2. **The numbering in EV1/EX4/EY3/EY4 is loose** and this is F6. Then the deferred items
   go to F6's ledger, and F5's screening still sits between F4 and this.

**This file is named `F5-DRAFT-code-checks.md` so that locking it does not silently
decide the question.** On lock it becomes `F5.md` or `F6.md` and the gate labels below
become G5.x or G6.x to match. Everything else in this draft is independent of the answer.

---

## 1. WHAT THIS MILESTONE IS, AND THE LABEL IT CARRIES ON EVERY OUTPUT

API RP 2A-WSD tubular member checks, per member-station, on F1's stand-in tube, from F4
step 3's envelope.

**`PLAN.md`'s own framing is adopted verbatim and is not softened:** these checks are a
**sizing screen, not a compliance calculation**. API RP 2A and ISO 19902 are written for
fixed jackets; neither is a certification basis for a floating platform. Certification
lives in the DNV series, and shell buckling of the buoy cans is DNV-RP-C202 territory —
sub-model work, not a beam-level check.

**Every report this milestone generates carries this label on its face**, extending F4's:

> **INDICATIVE SIZING SCREEN — NOT A CODE CASE.** API RP 2A-WSD working-stress checks on a
> **stand-in tube** that is the stiffness equivalent of a triangulated truss of undecided
> depth (`F1.md:390`), under **assumed masses** (platform 20 kg / hub 12 kg model scale,
> 75% of body mass on arms, platform inertia scaled with mass). `F_y` assumed. One wave
> heading has been run. Utilisations are for finding the governing members, not for
> demonstrating adequacy.

**And it inherits F4's three live limitations by name**, because a utilisation computed on
them inherits them:

* the equivalent density of the hub arms is above steel — `11433.5 kg/m^3` against `7850`
  — so the mass does not fit inside F1's section at `f = 0.75` (DZ5 / ER1(e));
* **all six F4 cases are heading 0 degrees and the heading dependence is untested**
  (EX3 / R724);
* F4's envelope is **per component**, so a utilisation formed from its six values is an
  upper bound; the per-instant value is the physical one. F4's table already reports both
  and this milestone must keep the distinction rather than collapse it.

---

## 2. THE OPEN QUESTIONS, FOR THE LOCK

**Q1 — `F_y`.** EY4 says 355 MPa unless Xabier says otherwise. `floatfea/basis.py` already
declares `FY_S355` and `SIGMA_ALLOW_S355 = 0.6 F_y = 213.0 MPa`, so 355 is the default and
no new constant is needed for it.

**Q2 — the one-third increase. EY4 defaults it to NO and this draft asserts NO.** API RP
2A-WSD § 3.1.2 permits a one-third increase in allowable stresses for storm loading. It is
**not applied**, and the reason is stated rather than left as a default: the increase is
written for the extreme environmental event in a fixed-jacket design basis, and F4's six
cases are design waves from a screening sweep rather than a declared extreme event with a
return period. Applying it would widen every allowable by 33% on the strength of a
categorisation the schema does not carry — which is the same argument `PLAN.md` uses to
reject ISO 19902's partial factors. **If Xabier wants it, it is one declared boolean and a
row in the results label, never a silent default.**

**Q3 — `K` and `L` for column buckling, which this draft does NOT decide.** The platform
arms are 50 m and the hub arms 25 m, and `K` depends on end restraint that the frame's
topology does not settle: each arm meets three others at a centre node and a joint at the
far end. API RP 2A § 3.2.2 recommends `K = 1.0` for jacket legs with no bracing and
`K = 0.8` for braced portions. **The draft's position: `K = 1.0` and `L` = the member
length, both DECLARED and both on the label**, because the conservative choice is the
defensible one for a screen and because the members are stand-ins for trusses whose real
buckling length is a property of a truss that has not been designed. This is the single
biggest sensitivity in the whole check and it is a modelling assumption, not a measurement.

**And it is measurable now, which makes the sensitivity concrete rather than asserted:**

```
cmd    python -c "from floatfea.model.platform import build_superstructure; import math;
       s=build_superstructure(); m=s.bodies[0].members[0];
       print(math.sqrt(m.section.I_y/m.section.A))"
out    r = 0.8227 m
out    platform arm, L = 50 m, K = 1.0  ->  KL/r = 60.8
out    hub arm,      L = 25 m, K = 1.0  ->  KL/r = 30.4
cmd    python -c "import math; from floatfea.basis import FY_S355;
       print(math.sqrt(2*math.pi**2*2.1e11/FY_S355))"
out    C_c = 108.1
rule   API RP 2A § 3.2.2: the inelastic branch applies below `C_c`, the elastic above
judge  **both arms are below `C_c` at `K = 1.0`, so the INELASTIC branch governs both** and
       the elastic branch is not reached until `K > 1.78` on the platform arm. So `K` moves
       the allowable continuously rather than switching branches, which bounds how much
       this assumption can distort the screen -- and it is still the largest single
       modelling choice in the check.
```

**Q4 — the station set.** F4 reports ROOT / MID / TIP, with MID closed-form at F3's
one-element mesh. `PLAN.md`'s F6 asks for stress recovery at **circumferential points** on
tubulars. Those are different axes of refinement — along the member, and around the
section. This draft checks the three F4 stations and does **not** add circumferential
points; `G6.2` (CalculiX cross-check on the same section) is where that belongs and it is
out of these two steps. Stated so the omission is visible.

---

## 3. STEP 1 — THE CHECKS, EACH AGAINST A HAND CALCULATION

`floatfea/checks/api_wsd.py`. Closed-form, one function per clause, no envelope logic.

1. **Axial tension** — § 3.2.1, `F_t = 0.6 F_y`.
2. **Axial compression** — § 3.2.2. Column buckling with `C_c = sqrt(2 pi^2 E / F_y)`, the
   inelastic branch for `K L / r < C_c` and the elastic branch above it. **`D/t` is checked
   against the local-buckling limit first**, because beyond it the global check is not the
   binding one: `basis.chs_class_limits()` gives `33.1 / 46.3 / 59.6` at `F_y = 355` and the
   stand-in tube is `D/t = 13.9`, comfortably class 1 — so local buckling does not govern
   *this* section and the check must still refuse rather than pass silently on one that is
   slender.
3. **Bending** — § 3.2.3, `F_b` by `D/t` class: `0.75 F_y` below `1500/F_y`, then the two
   reduced branches.
4. **Shear** — § 3.2.4, `F_v = 0.4 F_y` on the beam shear, with the transverse shear taken
   as `V / (0.5 A)` per the clause rather than `V / A`.
5. **Torsional shear** — § 3.2.4's torsion form on `W_t = 2J/D`.
6. **The combined interaction** — § 3.3.1 for tension-plus-bending and § 3.3.2 for
   compression-plus-bending, including the amplification `C_m / (1 - f_a/F_e')`.

**Gate (G6.1 / G5.1 depending on § 0): every one of the six verified against an independent
hand calculation**, written out in `docs/verification/api_wsd/`, with the clause number, the
arithmetic, and the source for every input. EA4: the hand calculation is not derived from
the code, and the code does not read its expected value from the object under test.

**Counter-case per check**, because a check that cannot redden certifies nothing: each
gets an injected input that must push the utilisation past 1.0, and the injection size is a
declared constant with a plan row.

**Tolerances this step declares:** none are invented here. Each is measured at this step
and declared with the window rule where one applies — and `CLAUDE.md`'s rule holds, so the
closed-form clauses are compared to the hand calculations at a tolerance that reflects
float arithmetic and nothing else.

---

## 4. STEP 2 — THE UTILISATION TABLE AND THE TOP TEN

`scripts/measure/` reads F4 step 3's envelope and produces, per member-station:

* each of the six checks' utilisation, and the **governing** one named;
* the combined interaction value;
* the governing case and station, carried through from F4;
* the `f` sensitivity at the root for `f = 0.5 / 0.75 / 1.0`, static, as F4 does;
* a **top-ten list by governing utilisation**, with the clause that governs each.

**Both of F4's stress columns carry through** — per-instant and envelope upper bound — and
the utilisation is computed from each, labelled. Collapsing them would be the one thing
this milestone could do that makes F4's table less honest than it is.

**Gate: the table regenerates identically from stored results** (G6.3's shape), and the
top-ten list is stable under a re-run.

**What step 2 does NOT do:** no VTK output, no circumferential stress recovery, no
CalculiX cross-check. Those are `PLAN.md`'s F6/F7 and they are named here so the two-step
scope is visibly narrower than the milestone `PLAN.md` describes.

---

## 5. WHAT THIS MILESTONE INHERITS AS ALREADY-KNOWN FINDINGS

F4 step 3's table, on the stand-in tube, already reports:

* **the static root stress exceeds `0.6 F_y` at every `f` on the ladder** — `323.7` /
  `269.7` / `215.8 MPa` at `f = 0.5 / 0.75 / 1.0` against `213.0` — under self-weight
  alone, before any wave load;
* **`742.6 MPa` per-instant at the platform root** at `T_full = 10 s`, about `3.5x` the
  allowable;
* the governing component on the transverse arms is `Mz = 4.94e+08 N.m`, **entirely
  dynamic** — static `Mz` is zero there, because those arms sit on the `y` axis and the
  wave runs along `x`, which is also why R724's untested heading matters most exactly here.

**So the expected outcome of this milestone is utilisations well above 1.0, and that is a
finding about the SECTION rather than about the platform.** The plan says so in advance so
that the result is not read as news, and so that nobody is tempted to tune anything to
bring it under 1.0. The stand-in tube is a stiffness equivalent for a truss that has not
been designed; the useful output is **which members and which clauses govern**, which is
what `PLAN.md` says F6 exists for.

---

## 6. DATES

EY4: drafted for the lock by **12 October**. The working target for the code check is
**22 October** and the committed date is **28 October**, both unchanged by EY3's cut.
