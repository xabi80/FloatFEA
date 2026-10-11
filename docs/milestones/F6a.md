# F6a — THE REQUIRED SECTION

<!-- step-under-execution: 1 -->

Increment 1 after F6's closure. **One step.** Opened by **DIRECTIVE FG**, recorded below
verbatim in the form `F6.md` uses for FA/FB/FC, so the plan and the directive do not have to
be read side by side.

---

## 0. WHAT THIS INCREMENT IS, AND THE LABEL IT CARRIES

F6 found that the **stand-in** tube does not pass: `U = 1.71167` at the worst member-station,
four of thirty-two over unity, and `1.0130` against `F_b` on a platform arm root under
self-weight alone. That is a finding about the section, and the obvious next question is the
one F6 could not answer: **what section would pass?**

This increment answers it and nothing else. **Every output carries the same label F6's
did** — INDICATIVE: a stand-in tube for a truss of undecided depth, placeholder masses,
heading 0° only, `F_y` assumed — plus one more that is specific to this increment and is
the reason FG4 exists: **the mass basis is held fixed while the section moves**, so a
required section heavier than the mass assumed for it is a contradiction this increment
reports rather than resolves.

---

## 1. THE PROCESS, LIGHTER (FG1)

Xabier agreed to this and it is narrower than F6's:

* **One step. One reviewed report revision, then EQ0 closure.**
* **CZ0's blocking criterion is unchanged**, EZ0's published deliverable included — so a
  wrong figure in `results/F6a/` or in the script that produces it blocks.
* **No new report guards and no new meta-tests.** DR1 stands. The report is EI4 minimum
  form plus the deliverable.
* **Corpus batches stay paused** (EG4(e)).
* **Review effort goes to the numbers:** the reviewer recomputes the governing required
  section by an independent route.

And FF0 now applies: a closure item in the gating apparatus is fixed in the next commit
rather than ledgered.

---

## 2. THE PREMISE (FG2) — ASSERTED, NOT ASSUMED

> Section choice does not change the loads or the member forces, because:
> **(a)** FloatSim's bodies are rigid, so the joint reactions in
> `data/f4/dynamic_inputs.npz` do not depend on section;
> **(b)** each body is statically determinate apart from the platform's single vertical
> redundancy, which uniform sizing per body leaves unchanged;
> **(c)** member mass comes from the deck `μ`, not from the section.
>
> So sizing is two groups: **all 4 platform arms together, and all 12 hub arms together.**
>
> **Verification:** re-run the FE static and dynamic cases with the required section of each
> group, and show the member forces unchanged (state the max relative change) and `U ≤ 1.0`
> everywhere.

**(c) holds by construction and the mechanism matters for FG4.**
`floatfea/model/platform.py` computes `member_mass = fraction * deck_mass` — no section
term — and then `density = line_mass / section.A`. **The equivalent density is
back-computed so that `ρ·A` equals the deck's `μ` whatever the section is.** So a section
change moves no self-weight in the model, which is what makes the premise true *and* what
makes the required section's real steel mass a separate question — FG4's.

---

## 3. THE SEARCH (FG3)

For each group, against F4's governing envelope (**EZ2 / FA0** basis), **per instant**,
ROOT / MID / TIP, with the same API RP 2A-WSD clauses as F6 — `F_y = 355 MPa`, `K = 2.0`,
`C_m = 0.85`, **no one-third increase**:

| | search | step |
|---|---|---|
| (i) | `D = 2.5 m` fixed: the minimum `t` for which `max U ≤ 1.0` | 5 mm |
| (ii) | `t = 180 mm` fixed: the minimum `D` | 0.1 m |
| (iii) | the minimum-**area** tube over `D ∈ [2.0, 6.0] m` and `t` in 5 mm steps | 0.1 m / 5 mm |

Within the API clause ranges — **a candidate outside them is REFUSED, not extrapolated.**

For each answer: `D`, `t`, `D/t`, `A`, `W`, the governing member-station, case, clause and
branch, `max U`, and the `K = 1.0` / `C_m = 1.0` sensitivities.

---

## 4. MASS CONSISTENCY (FG4) — THE KEY FINDING

For each answer, the steel line mass `ρ_steel·A_req` at `7850 kg/m³` against the assumed arm
line mass `μ` — platform `9.375 t/m`, hubs `15.0 t/m`. **Report the ratio.**

If it is `> 1.0`: state plainly that **the section needed to pass outweighs the mass assumed
for it**, so the mass basis and the section are inconsistent, and quantify what self-weight
the required section implies — the static root moment with `μ = ρ·A_req`.

**Do NOT iterate the mass.** That is increment 2's job, with Xabier's mass budget.

---

## 5. THE DELIVERABLE (FG5)

`results/F6a/required_section.md` plus a CSV. A **one-page table and a half page of
findings**, labelled INDICATIVE. **Sent the moment it exists.** Target **16 October**.

---

## 6. THEN STOP (FG6)

Until Xabier supplies the mass budget (increment 2) or a heading plan (increment 3).

---

## 7. TOLERANCES THIS INCREMENT DECLARES

**None so far.** The search is a comparison of a computed `U` against `1.0`, which is the
clause's own threshold and not a tolerance; the step is the search grid, declared above. If
the premise verification needs a "member forces unchanged" threshold, it goes in
`floatfea/tolerances.py` with its counter-case and both EH4 boundaries, and it is named
here before it is used.
