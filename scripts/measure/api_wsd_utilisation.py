#!/usr/bin/env python
"""F6 step 1: API RP 2A-WSD utilisations per member-station, from F4's envelope.

    python scripts/measure/api_wsd_utilisation.py

**INDICATIVE SIZING SCREEN -- NOT A CODE CASE.** Every label F4's table carries applies
here unchanged, and this adds its own. The section is a stiffness stand-in for a truss of
undecided depth, the masses are assumed, `F_y` is assumed, and one wave heading has been
run. The output finds the governing members and clauses; it does not demonstrate adequacy.

WHAT IT READS. `docs/F4_member_forces.csv`, F4's own deliverable, on EZ2's **governing**
basis -- `T = 12.5, 14, 15, 16.2 s`. The two out-of-range cases are excluded by EZ2(b) and
cannot set a utilisation: `T = 10 s` exceeds the deep-water breaking steepness and
`T = 20 s` is too long for the height.

**ROOT AND TIP ONLY (FA3).** The MID column is excluded until R730's conditions are
discharged -- the closed-form midspan is a measured `4.0%` approximation on the bending term
and is unverified against a refined mesh. ROOT and TIP are verified exact against an
independent statics cut. The exclusion is in the code rather than in a note, so it cannot be
forgotten.

**EZ4's `K = 2.0`, with FA2's `K = 1.0` sensitivity column.** Each arm is a cantilever from
the body centre; the gimbal end bears on a floating body and gives no reliable lateral
restraint. That is not a scaling: at `K = 2.0` the 50 m platform arms cross `C_c` into
§ 3.2.2's elastic branch while the 25 m hub arms stay inelastic, so the four governing
members move onto a different formula. FA2 asks for the branch per member-station and for
`f_a` against `F_a` beside the bending terms, so a reader sees how little the axial
contributes rather than inferring it.

**AND FB2's `C_m = 1.0` COLUMN BESIDE IT.** `C_m = 0.85` is section 3.3.1 case (a), members
in frames subject to joint translation, which is the reading `K = 2.0`'s sidesway assumption
implies; `C_m = 1.0` is the alternative and it RAISES every compression utilisation, because
`C_m` multiplies the bending term. R743: the module stated that direction backwards.

**G6.1 IS GREEN** -- every clause here is verified against an independent hand calculation
in `tests/verification/rung5/test_g61_api_wsd_hand_calculations.py`, at two or more points
per branch, either side of every boundary (FB0). Before that gate existed this script's
output carried "clause implementations unverified".
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from floatfea.basis import FY_S355  # noqa: E402
from floatfea.checks.api_wsd import CM_JOINT_TRANSLATION, check_member  # noqa: E402
from floatfea.model.platform import _outer_diameter, build_superstructure  # noqa: E402

GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
"""EZ2(a). FA0: `T = 12.5 s` stays -- `0.3%` below the band is inside the guidance's own
precision, the case was chosen as the band's lower edge, and the response rises as `T` falls
across the band, so the lower edge is what governs."""

STATIONS_CHECKED = ("ROOT", "TIP")
"""FA3. MID waits on R730's discharge."""

K_LOCKED = 2.0
K_SENSITIVITY = 1.0

CM_LOCKED = CM_JOINT_TRANSLATION
CM_SENSITIVITY = 1.0
"""FB2's second sensitivity column, beside the `K = 1.0` one.

`C_m = 0.85` is section 3.3.1 case (a) -- members in frames **subject to joint translation**
-- which is the reading consistent with `K = 2.0`'s sidesway assumption. `C_m` MULTIPLIES
the bending term in section 3.3.2, so `C_m = 1.0` **raises** every compression utilisation
and `0.85` is the less onerous of the two (R743). The module's comment had that direction
backwards, and `C_m` is the second-largest lever in the check."""

LABELS = (
    "INDICATIVE SIZING SCREEN -- NOT A CODE CASE. API RP 2A-WSD working-stress checks on a "
    "STAND-IN TUBE that is the stiffness equivalent of a triangulated truss of undecided "
    "depth (F1.md:390).",
    "Fy = 355 MPa (S355; ASSUMED). No one-third increase (EZ4 Q2, locked): section 3.1.2's "
    "increase is written for a declared extreme event and these are screening design waves "
    "with no return period.",
    "K = 2.0 for every arm, L = member length (EZ4 Q3): a cantilever from the body centre, "
    "the gimbal end on a floating body giving no reliable lateral restraint. A K = 1.0 "
    "column is reported beside it (FA2).",
    "C_m = 0.85 (section 3.3.1 case (a); members in frames subject to joint translation), "
    "consistent with K = 2.0's sidesway assumption. C_m MULTIPLIES the bending term, so "
    "C_m = 1.0 RAISES the compression utilisation and 0.85 is the LESS onerous of the two "
    "(R743). A C_m = 1.0 column is reported beside the K = 1.0 one (FB2).",
    "G6.1 is GREEN: every clause is verified against an independent hand calculation in "
    "tests/verification/rung5/, at two or more points per branch, either side of every "
    "boundary (FB0). R742: F_b is capped at 0.75 Fy -- the first reduced branch exceeded it "
    "to D/t = 30.60. R741: section 3.2.2(b) local buckling is implemented and D/t > 300 is "
    "refused rather than extrapolated.",
    "Governing basis: T = 12.5; 14; 15; 16.2 s (EZ2). T = 10 s and T = 20 s are outside the "
    "associated-period range for H = 24.2 m -- T = 10 s exceeds the breaking steepness -- "
    "and cannot govern.",
    "ROOT and TIP only (FA3). The MID column waits on R730's discharge: its closed form is "
    "a measured 4.0% approximation on bending, unverified against a refined mesh.",
    "Load basis: platform 20 kg / hub 12 kg model scale; 75% of body mass on arms; platform "
    "inertia scaled with mass (assumed). ER0. Hub line mass 15 t/m against the platform "
    "arms' 10.3 t/m.",
    "DZ5 / ER1(e): the hub arms carry an equivalent density above steel (11433.5 against "
    "7850 kg/m^3), so the mass does not fit inside F1's section at f = 0.75.",
    "EX3 / R724: all cases are heading 0 degrees. The heading dependence is UNTESTED, and "
    "the governing component on the transverse arms is entirely dynamic.",
    "R740: the utilisations are computed from F4's `total_instant` rows -- the six "
    "components AT the step where sigma peaks. The `total_max`/`total_min` envelope is a "
    "per-component upper bound whose values do not occur together, and it is NOT used here.",
    "R739: F4's N column is tension-positive (docs/conventions.md:320). It was published "
    "compression-positive, which put every over-unity station on section 3.3.1 instead of "
    "3.3.2 and reported F_a = 213.00 MPa where the column allowable is 73.25 (platform, "
    "elastic) or 161.02 (hubs, inelastic).",
)


def _section() -> tuple[float, float, float, float, float]:
    """`(A, W, W_t, D, t)` for the stand-in tube, all derived from the section (AS1)."""
    built = build_superstructure()
    member = built.bodies[0].members[0]
    s = member.section
    d_outer = _outer_diameter(s)
    wall = 0.5 * (d_outer - math.sqrt(d_outer * d_outer - 4.0 * s.A / math.pi))
    return float(s.A), 2.0 * float(s.I_y) / d_outer, 2.0 * float(s.J) / d_outer, d_outer, wall


def _kl_over_r(body: str) -> tuple[float, float]:
    """`(KL/r at K=2, KL/r at K=1)` for a body's arms.

    `r = sqrt(I/A)` from the section, and `L` is the member length -- 50 m on the platform
    arms and 25 m on the hub arms. Both are read from the built model, not typed.
    """
    built = build_superstructure()
    b = next(x for x in built.bodies if x.name == body)
    s = b.members[0].section
    r = math.sqrt(float(s.I_y) / float(s.A))
    span = float(b.members[0].length)
    return K_LOCKED * span / r, K_SENSITIVITY * span / r


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--forces", type=Path, default=ROOT / "docs" / "F4_member_forces.csv")
    ap.add_argument("--out", type=Path, default=ROOT / "docs" / "F6_utilisation.csv")
    ap.add_argument("--summary", type=Path, default=ROOT / "docs" / "F6_utilisation.md")
    args = ap.parse_args(argv)

    area, w_bend, w_tors, d_outer, wall = _section()
    lines = [ln for ln in args.forces.read_text(encoding="utf-8").splitlines() if ln[:1] != "#"]
    rows = list(csv.DictReader(lines))
    if not rows:
        raise SystemExit(f"{args.forces} carries no rows; run the member-force table first.")

    kl_cache: dict[str, tuple[float, float]] = {}
    out_rows: list[dict[str, object]] = []
    for r in rows:
        if r["station"] not in STATIONS_CHECKED:
            continue
        # R740: the PER-INSTANT row, not the per-component envelope. F4's `total_max` and
        # `total_min` max each of the six components INDEPENDENTLY over the window, so their
        # six values do not occur together and a utilisation from them is an upper bound --
        # which the label used to call per-instant. `total_instant` carries the components AT
        # the step where sigma peaks. The gap at the governing station is `0.103` in U,
        # `4.3x` the K sensitivity this summary reports.
        if r["basis"] != "total_instant":
            continue
        try:
            period = float(r["period_full_s"])
        except ValueError:
            continue
        if period not in GOVERNING_PERIODS:
            continue
        if r["body"] not in kl_cache:
            kl_cache[r["body"]] = _kl_over_r(r["body"])
        kl2, kl1 = kl_cache[r["body"]]
        common = dict(
            axial_n=float(r["N"]),
            shear_y_n=float(r["Vy"]),
            shear_z_n=float(r["Vz"]),
            torsion_nm=float(r["T"]),
            moment_y_nm=float(r["My"]),
            moment_z_nm=float(r["Mz"]),
            area_m2=area,
            section_modulus_m3=w_bend,
            torsional_modulus_m3=w_tors,
            d_outer_m=d_outer,
            wall_m=wall,
        )
        locked = check_member(k_l_over_r=kl2, cm=CM_LOCKED, **common)
        sens = check_member(k_l_over_r=kl1, cm=CM_LOCKED, **common)
        # FB2: the SECOND sensitivity, at the locked K. One variable moved from `locked`.
        sens_cm = check_member(k_l_over_r=kl2, cm=CM_SENSITIVITY, **common)
        out_rows.append(
            {
                "body": r["body"],
                "member": r["member"],
                "station": r["station"],
                "period_full_s": r["period_full_s"],
                "basis": r["basis"],
                "f_a_MPa": locked.f_a / 1e6,
                "F_a_MPa": locked.allow_axial / 1e6,
                "f_b_MPa": locked.f_b / 1e6,
                "F_b_MPa": locked.allow_bending / 1e6,
                "f_v_MPa": locked.f_v / 1e6,
                "f_vt_MPa": locked.f_vt / 1e6,
                "axial_branch": locked.axial_branch,
                "bending_branch": locked.bending_branch,
                "interaction_form": locked.interaction_form,
                "u_axial": locked.u_axial,
                "u_bending": locked.u_bending,
                "u_shear": locked.u_shear,
                "u_torsion": locked.u_torsion,
                "u_combined": locked.u_combined,
                "utilisation_K2": locked.utilisation,
                "utilisation_K1": sens.utilisation,
                "utilisation_Cm1": sens_cm.utilisation,
                "governing_clause": locked.governing,
            }
        )

    if not out_rows:
        raise SystemExit("no governing ROOT/TIP rows found; check the basis filters.")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        for label in LABELS:
            fh.write("# " + label.replace(",", ";") + chr(10))
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0]))
        w.writeheader()
        for row in out_rows:
            w.writerow({k: (f"{v:.6g}" if isinstance(v, float) else v) for k, v in row.items()})

    _write_summary(args.summary, out_rows, area, w_bend, w_tors, d_outer, wall, kl_cache)
    print(f"  wrote {args.out.relative_to(ROOT)} ({len(out_rows)} rows)")
    print(f"  wrote {args.summary.relative_to(ROOT)}")
    return 0


def _and_list(items: list[str]) -> str:
    """`a`, `a and b`, `a, b and c` -- so a generated sentence reads as one."""
    if not items:
        return "nothing"
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + " and " + items[-1]


def _write_summary(
    path: Path,
    rows: list[dict[str, object]],
    area: float,
    w_bend: float,
    w_tors: float,
    d_outer: float,
    wall: float,
    kl_cache: dict[str, tuple[float, float]],
) -> None:
    worst: dict[tuple[str, str, str], dict[str, object]] = {}
    for r in rows:
        key = (str(r["body"]), str(r["member"]), str(r["station"]))
        if key not in worst or float(r["utilisation_K2"]) > float(worst[key]["utilisation_K2"]):
            worst[key] = r
    top = sorted(worst.values(), key=lambda r: -float(r["utilisation_K2"]))[:10]

    out = [
        "# F6 step 1 — API RP 2A-WSD utilisations, INDICATIVE",
        "",
        "**A sizing screen, not a compliance calculation.** The labels below are the "
        "deliverable as much as the numbers are.",
        "",
    ]
    out += [f"* {label}" for label in LABELS]
    out += [
        "",
        "## The ten most utilised member-stations",
        "",
        "| # | body | member | station | case | governing clause | U (K=2) | U (K=1) "
        "| U (C_m=1) |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for n, r in enumerate(top, start=1):
        out.append(
            f"| {n} | {r['body']} | `{r['member']}` | {r['station']} | "
            f"T = {r['period_full_s']} s | {r['governing_clause']} | "
            f"{float(r['utilisation_K2']):.3f} | {float(r['utilisation_K1']):.3f} "
            f"| {float(r['utilisation_Cm1']):.3f} |"
        )
    out += [
        "",
        "## FA2: how little the axial term contributes",
        "",
        "| # | member | station | f_a (MPa) | F_a (MPa) | u_axial | f_b (MPa) | F_b (MPa) "
        "| u_bending | axial branch |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for n, r in enumerate(top, start=1):
        out.append(
            f"| {n} | `{r['member']}` | {r['station']} | {float(r['f_a_MPa']):.2f} | "
            f"{float(r['F_a_MPa']):.2f} | {float(r['u_axial']):.4f} | "
            f"{float(r['f_b_MPa']):.1f} | {float(r['F_b_MPa']):.1f} | "
            f"{float(r['u_bending']):.3f} | {r['axial_branch']} |"
        )
    out += [
        "",
        "## The section and the slenderness",
        "",
        f"* `D = {d_outer:.4f} m`, `t = {wall:.5f} m`, `D/t = {d_outer / wall:.1f}` — "
        f"**compact**, so § 3.2.3 gives `F_b = 0.75 F_y = {0.75 * FY_S355 / 1e6:.2f} MPa`.",
        f"* `A = {area:.4f} m²`, `W = {w_bend:.4f} m³`, `W_t = {w_tors:.4f} m³`.",
        f"* `C_m = {CM_LOCKED}` (§ 3.3.1 case (a), members in frames subject to joint "
        f"translation — consistent with `K = 2.0`'s sidesway assumption). `C_m` multiplies "
        f"the bending term, so the `C_m = {CM_SENSITIVITY}` column is the HIGHER of the two "
        f"(R743).",
        "",
        "| body | L (m) | KL/r at K=2 | KL/r at K=1 | branch at K=2 |",
        "|---|---|---|---|---|",
    ]
    for body, (kl2, kl1) in sorted(kl_cache.items()):
        built = build_superstructure()
        span = float(next(x for x in built.bodies if x.name == body).members[0].length)
        branch = "elastic" if kl2 >= 108.059 else "inelastic"
        out.append(f"| {body} | {span:.0f} | {kl2:.1f} | {kl1:.1f} | **{branch}** |")
    # FA2's question answered as a NUMBER rather than left to the per-row table: how much
    # does the K lock actually move the governing utilisation?
    branches: dict[str, int] = {}
    for r in rows:
        key = str(r["axial_branch"])
        branches[key] = branches.get(key, 0) + 1
    # `max` on (float, dict) tuples compares the dicts when the floats tie, which raises.
    # A key function compares only the number.
    worst_k_row = max(
        rows, key=lambda r: abs(float(r["utilisation_K2"]) - float(r["utilisation_K1"]))
    )
    worst_k = (
        abs(float(worst_k_row["utilisation_K2"]) - float(worst_k_row["utilisation_K1"])),
        worst_k_row,
    )
    over = {
        (str(r["body"]), str(r["member"]), str(r["station"]))
        for r in rows
        if float(r["utilisation_K2"]) > 1.0
    }
    all_stations = {(str(r["body"]), str(r["member"]), str(r["station"])) for r in rows}
    compression = [r for r in rows if r["axial_branch"] != "tension"]
    # R739's consequence: with the axial sign corrected AND only per-instant rows kept,
    # the set can be empty -- there is one row per station now rather than a max/min pair
    # of opposite axial sign, so a station is tension or compression but not both. An empty
    # set is reported as such rather than crashing or being quietly omitted.
    worst_compression = (
        max(float(r["utilisation_K2"]) for r in compression) if compression else float("nan")
    )
    worst_overall = max(float(r["utilisation_K2"]) for r in rows)
    # R747: EVERY SENTENCE BELOW IS GENERATED FROM THE SET IT DESCRIBES.
    #
    # Four hand-written sentences stood here and all four contradicted the table in the
    # same file -- the clause attribution on the over-unity stations ("all governed by
    # 3.3.1" against a 2/2 split), the K sensitivity ("at most 0.024" against 0.034238
    # printed three lines above), the worst station's two utilisations (`0.0004` and
    # `1.815`, the second being the envelope figure R740 removed), and a causal claim that
    # the amplification "never bites" refuted by the C_m column this script added. They
    # were correct before R739 and R740 and nothing re-took them, which is BP0: a figure
    # whose rule moved underneath it.
    #
    # So the sets are formed first and the sentences read from them. The only words left
    # are the ones that are true whatever the numbers are.
    worst_row = max(rows, key=lambda r: float(r["utilisation_K2"]))
    over_rows = [r for r in rows if float(r["utilisation_K2"]) > 1.0]
    over_clauses: dict[str, int] = {}
    for r in over_rows:
        key = str(r["governing_clause"])
        over_clauses[key] = over_clauses.get(key, 0) + 1
    over_bodies = sorted({str(r["body"]) for r in over_rows})
    over_stations = sorted({str(r["station"]) for r in over_rows})
    # **R752: WHICH FORM GOVERNS IS READ FROM THE CHECK, NOT INFERRED FROM A SENSITIVITY
    # COLUMN.** This counted rows where `utilisation_Cm1 != utilisation_K2` and called them
    # the amplified ones. Published: `10 of 17` AMPLIFIED. True: **7 of 17 amplified, 10 of
    # 17 simple**, and the ten the sentence counted were the simple ones.
    #
    # **AND THE EXPLANATION OF *WHY* WAS WRONG TOO (C66), WHICH IS WORTH MORE THAN THE
    # COUNT.** It said the seven missed rows "are TIPs whose bending moment is `~1e-08 MPa`
    # and whose `U` is beam shear, so `C_m` cannot reach `U` there at all" -- a conjunction
    # asserted of all seven where each half holds of a different subset, with a `so` spanning
    # two mechanisms and no cell under it. Measured over the 17 rows:
    #
    #   all 10 that FIRE are an OVERTAKE: amplified(C_m = 1.0) exceeds simple, by 0.1153%
    #     to 1.3129%. That is what the predicate detects -- not which form governs.
    #   5 of the 7 that MISS miss because `u_combined` is not the governing channel at all:
    #     beam shear governs those TIPs.
    #   2 miss because the bending term is negligible -- platform:hub1_arm and hub3_arm TIP,
    #     bending share 0.0000%, where the AMPLIFIED form IS governing and `C_m` DOES reach
    #     `U`, by about 1e-10. "Cannot reach it at all" is false on exactly those two.
    #   0 of the 7 are the both-halves case the old sentence described of all seven.
    #
    # So "bending-dominated ROOT" is a CORRELATE of the overtake and not its cause, and the
    # coincidence is contingent at one part in a thousand: the tightest overtake is 0.1153%.
    # **That contingency is the argument for publishing both counts separately**, which is
    # what the two lines below do.
    #
    # `MemberCheck.interaction_form` records which half of `max(amplified, simple)` was
    # taken, so there is nothing left to infer.
    amplified_rows = [r for r in compression if r["interaction_form"] == "amplified"]
    simple_rows = [r for r in compression if r["interaction_form"] == "simple"]
    cm_visible = [
        r
        for r in compression
        if f"{float(r['utilisation_Cm1']):.6g}" != f"{float(r['utilisation_K2']):.6g}"
    ]
    worst_cm_row = max(
        rows, key=lambda r: abs(float(r["utilisation_Cm1"]) - float(r["utilisation_K2"]))
    )
    worst_cm = abs(float(worst_cm_row["utilisation_Cm1"]) - float(worst_cm_row["utilisation_K2"]))

    out += [
        "",
        "**The `K = 2.0` lock moves the platform arms onto a different formula** — at "
        "`K = 1.0` every arm is inelastic and at `K = 2.0` the 50 m platform arms cross "
        "`C_c = 108.06` into § 3.2.2's elastic branch. How much it moves a utilisation, "
        "and how much `C_m` does, are the two numbers FA2 and FB2 ask for:",
        "",
        "```",
        f"axial branch over {len(rows)} rows : "
        + "; ".join(f"{k} {v}" for k, v in sorted(branches.items())),
        f"largest |U(K=2) - U(K=1)|      : {worst_k[0]:.6f}  "
        f"at {worst_k[1]['member']} {worst_k[1]['station']} ({worst_k[1]['axial_branch']})",
        f"largest |U(C_m=1) - U(C_m={CM_LOCKED})| : {worst_cm:.6f}  "
        f"at {worst_cm_row['member']} {worst_cm_row['station']} "
        f"({worst_cm_row['axial_branch']})",
        (
            f"worst compression station      : U = {worst_compression:.5f}"
            if compression
            else f"compression stations           : NONE of {len(rows)} per-instant rows"
        ),
        f"section 3.3.2 over {len(compression)} compression rows: AMPLIFIED governs on "
        f"{len(amplified_rows)}, SIMPLE on {len(simple_rows)}  (read from "
        f"interaction_form, not inferred -- R752)",
        f"C_m visibly moves U on {len(cm_visible)} of {len(compression)} -- a DIFFERENT "
        f"question: those are the rows where amplified(C_m = 1.0) OVERTAKES simple",
        f"worst station {worst_row['member']} {worst_row['station']}: "
        f"u_axial = {float(worst_row['u_axial']):.6f}  "
        f"u_bending = {float(worst_row['u_bending']):.5f}  "
        f"({worst_row['governing_clause']}, {worst_row['axial_branch']})",
        "```",
        "",
        "**Bending governs and the axial term is three orders smaller** — the ratio is in "
        "the block above, at the worst station, read from the row the table publishes. "
        "Neither modelling lever moves the governing number much, and the reason is the "
        "clause rather than the structure: § 3.3.2 takes the larger of its amplified and "
        "simple forms, the simple form carries no `F_a` and no `C_m`, and it is the one "
        "that governs wherever bending dominates.",
        "",
        f"**{len(over)} of {len(all_stations)} member-stations exceed `U = 1.0`**, the worst "
        f"at `{worst_overall:.3f}`. "
        + (
            f"They are on {_and_list(over_bodies)}, at {_and_list(over_stations)}, "
            f"and the governing clause is "
            + "; ".join(f"{k} on {v}" for k, v in sorted(over_clauses.items()))
            + "."
            if over_rows
            else "There are none."
        ),
        "",
        "## What this does NOT do",
        "",
        "* **No MID station** (FA3) — it waits on R730's discharge.",
        "* **No circumferential stress recovery**, no CalculiX cross-check, no VTK. Those "
        "are G6.2 and F7.",
        "* **No one-third increase** (EZ4 Q2).",
        "* **No hydrostatic or shell-buckling check.** The buoy cans are DNV-RP-C202 and F7.",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    raise SystemExit(main())
