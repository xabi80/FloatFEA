# F2 step 7 — V2.5, V2.6 and the V6.1 golden · CLOSURE

**Status:** closing on the sixty-third verdict. **Two verdicts on this step, 62
and 63**, which is DK2's cap. **The first real element defect in sixty-three
verdicts was found in this step, by the reviewer, in the mass matrix this step
shipped.**

---

## 1. What was built

| case | what ships |
|---|---|
| **V2.5** | the consistent mass matrix including rotary inertia; the exact Timoshenko pinned-pinned reference; `ΦᵀMΦ` against the analytic mass and inertia tensor |
| **V2.6** | end-release condensation, DJ0's two-rotation gimbal, rigid links as master-slave constraints |
| **V6.1** | `tests/regression/f2_shipped_matrices.json`, 126 invariants, produced by `scripts/regen_f2_golden.py` |

**Two planned tolerances were not created**, and both omissions are recorded
rather than silent: `FREE_FREE_FREQUENCY` (no band is asserted on the order) and
`RIGID_LINK_CONSTRAINT` (rigid kinematics is exact, so `ROUNDOFF_IDENTITY` is the
stronger assertion). An absent assertion is not a tighter one and the closure
says so; what is tighter is the constant the assertions actually use.

## 2. R541 — the defect, and the blast radius measured rather than argued

**The shear term's sign in `bending_interpolation` was `+Φξ/6` and should have
been `−Φξ/6`.** Found by the reviewer at the sixty-second verdict, attacking the
cell it had been asked to attack.

### What it broke

```
cmd    det of the interpolation matrix, L = 4
out    shipped   Phi=0 +6.667e-01   Phi=0.5 +3.333e-01   Phi=1 +0.000e+00   Phi=2 -6.667e-01
       corrected Phi=0 +6.667e-01   Phi=0.5 +1.000e+00   Phi=1 +1.333e+00   Phi=2 +2.000e+00
rule   the determinant must be positive for the interpolation to be solvable;
       corrected it is L(1+Phi)/6, the classical shear-flexible denominator
out    SINGULAR AT Phi = 1, negative above -- so `local_mass` returned
       max|m| = 1.62e+30 for a 46 kg member, or raised LinAlgError, at
       L/D = 2.64 which is INSIDE F3's own L/D >= 2 limit
```

### Unchanged under the fix

```
claim  the stiffness matrix is BIT-IDENTICAL across the fix
cmd    local_stiffness at L = 1, 4, 60 m, built in worktrees at 968435a~1 and at HEAD,
       compared as raw bytes
out    True at all three spans
rule   bit-identity, not agreement to a tolerance
claim  `bending_interpolation` has exactly one caller
cmd    grep -rn bending_interpolation floatfea scripts --include=*.py
out    its definition, and `bending_mass` at floatfea/element/beam.py:306
```

So: **rung 1 stands** — the patch test, nodal exactness and the transform tests
never touch the interpolation. **`ΦᵀMΦ` and the six rigid-body inertias stand** —
they are quadratic forms of vectors whose `c3` is zero, and `c3` is the only
coefficient the shear term multiplies. **F4's inertia relief was never affected**,
for the same reason: it multiplies the mass matrix by rigid-body accelerations.

### Moved under the fix

```
cmd    python -m pytest tests/regression -q, before regenerating the golden
out    36 failed, 98 passed -- every mass-matrix invariant and every rigid-body
       form of an element whose Phi is non-zero
cmd    python scripts/regen_f2_golden.py
out    126 recorded quantities; 56 values changed
```

The frequency tables in `tests/verification/rung2` moved with it; every figure
in this artifact and in §141 of the plan is re-taken on the corrected element.
**V6.1 caught the change one commit after it was added**, which is the whole
argument for having added it.

### The consumer chain, named in full

`bending_interpolation` → `bending_mass` → `local_mass` → `element_global_mass` →
`assemble_mass_dense`, plus `scripts/regen_f2_golden.py`. **Nothing else**:
`floatfea/post/`, `floatfea/export/`, `floatfea/solve/` and `floatfea/checks/`
are empty stubs at F2, so **no stress recovery calls it, and F6's will read the
stiffness path rather than the mass**. That is a statement about the tree today
and it is worth re-checking when `post/` is written.

### Why every V2.5 check was blind, which is the part worth carrying

The Euler-Bernoulli checkpoint is at `Φ = 0` by construction. The rigid inertias
and `ΦᵀMΦ` are quadratic forms of rigid vectors, whose `c3` is zero. **The
rigid-inertia parametrisation runs at `Φ = 2.509` and `Φ = 10.169` and passed on
the defective sign.** All 60 rung-2 tests pass on both signs.

**The check that would have caught it on the day now ships (DN1):** `qᵀkq` against
the interpolated field's own strain energy, at `Φ ∈ {1e-3, 1e-2, 0.1, 1, 10}`,
convention-free because eq. 5.36 *is* that field's energy. Its counter is the
shipped sign flip: `3.90e-03`, `3.87e-02`, `0.330`, LinAlgError, `0.330`.

**And the counter missed on its first attempt**, by patching
`floatfea.element.beam.bending_interpolation` while the helper read the name
imported into the test module — the same resolution mistake the reviewer had
recorded against its own first cell one verdict earlier. The interpolation is a
parameter now, so there is no name to miss.

## 3. G2.4 — what is asserted, and what goes to F3

| half | state |
|---|---|
| **sign** — the error against the exact Timoshenko pinned-pinned frequency is positive and falling | **asserted**, `n = 4` to `128`, both planes, all three modes |
| **order** — DL0's `[12, 20]` window on the ratio | **not asserted**; goes to F3 |

**The order question, with the two cells that refused to explain it.** The ratios
run `13.63, 10.31, 6.63, 4.82, 4.34` — sagging from fourth order toward second.

```
out    round-off floor: at n = 16 the error is 1.9494e-06 against
       0.5 * eps * lambda_max/lambda_1 = 1.9340e-10, four orders below, while the
       ratio has already sagged to 10.31. Comparable only at n = 128.
out    rotary inertia off, against its own closed form: 13.63, 10.31, 6.62, 4.47 --
       identical to four figures.
rule   DN0's branch: recover toward 16 and it was conditioning; do not and the
       order question goes to F3
```

The residual signature is an `h²` term taking over from `h⁴` and it is **not
identified**. Recorded as an open question with its starting point, not as a
property of the element.

## 4. Deferred, carried, and frozen

* **The G2.4 band** joins `docs/milestones/F2a.md`'s frozen list with its
  one-line adoption written down, per DM1.
* **Frequencies are excluded from V6.1** because the cross-platform `eigh` drift
  is unmeasured — noted on the frozen list as the reason, so whoever tightens it
  knows what measurement is missing.
* **V1.3, V2.3, V2.4** stay deferred with the reasons in
  `docs/closure/F2-step6.md` §6.
* **C1–C13** from verdict 61 and **C14–C19** from verdict 62 carry as a list,
  unchanged and not re-reviewed.

## 5. The lesson

**An FE convergence result that contradicts the textbook is a reason to suspect
the code.** The element produced frequencies that rose under refinement; a
mechanism was found for it, written into a report, a plan section and a closure
artifact, and endorsed — and the mechanism was a sign. What broke it was not more
reasoning but a check the four existing ones could not reach: the energy identity
against the stiffness, which is convention-free and needs no reference at all.

Step 6's lesson was that a dropped assertion needs its replacement carrier in the
same commit. This step's is narrower and harder: **a gate whose checks all live
where a coefficient cannot be seen is not a gate on that coefficient**, and the
way to find out is to ask which term each check would notice.
