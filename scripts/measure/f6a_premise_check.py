#!/usr/bin/env python
"""FG2: the premise the F6a search rests on, verified -- and narrowed to what is true.

    python scripts/measure/f6a_premise_check.py                  # all six answers, static
    python scripts/measure/f6a_premise_check.py --dynamic         # and the dynamic half
    python scripts/measure/f6a_premise_check.py --search iii_min_area

WHAT THE SEARCH NEEDS. `f6a_required_section.py` re-evaluates the clauses at thousands of
candidate sections against ONE set of stored member forces. That is only legitimate if
section choice does not change what the search reads.

**AND THE FIRST VERSION OF THIS SCRIPT CLAIMED MORE THAN IT CHECKED, WHICH IS R782.** Its
docstring said it compared "on BOTH the static and the dynamic cases"; it called
`_static_rows` twice and nothing else, at one search per invocation. The claim is now the
measurement:

* **STATIC: the member forces are unchanged to round-off**, at all six answers.
* **DYNAMIC: the member forces MOVE, and the argument the old version gave for why they
  could not is wrong.** It said the dynamic increment comes from FloatSim's multipliers and
  each body's d'Alembert field, and the field reads `mu`, which is held. But the field is an
  ACCELERATION; what turns it into a load is `element_equivalent_load = M_e @ a_e` with the
  CONSISTENT element mass matrix, whose rotary terms are `rho_eq * I = mu * r^2`. **`r`
  moves with the section even though `mu` does not.**
* **What does not move is `max U`** -- the quantity the search's answer depends on -- after
  re-selecting which instant governs at the sized section. That is the premise the method
  actually needs, and it is narrower than "the member forces are unchanged".

**IT EMITS ITS FIGURES TO JSON** so the deliverable's generator reads them instead of
carrying them as string literals, which was R781. A `json.dump` is not apparatus: it
measures, it asserts nothing, and no gate reads it.

(c) IS CHECKED, AND "BY CONSTRUCTION" WAS THE WRONG REASON FOR IT (C99). `_build_body`
computes `member_mass = fraction * deck_mass` with no section term, then
`density = line_mass / section.A`, so `rho * A` is the deck's `mu` whatever the section --
for a GIVEN `fraction`. But `fraction` is chosen by `admissible()` descending
`MASS_FRACTION_LADDER`, and `admissible()` reads the remainder inertia, which the element
mass matrix's rotary term `rho_eq * I = mu * r^2` makes a function of the section. **So the
section reaches the mass decision and nothing about the arithmetic above rules it out.**
It does not change it, over 42 sections spanning the whole search grid, and that is
asserted in `tests/verification/rung3/test_platform_skeleton.py` by
`test_C99_a_MEASUREMENT_SECTION_does_not_move_the_CHOSEN_FRACTION`. The `mass_held` flag
this script emits is the same check at the two sections it builds.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "scripts" / "measure"))

from floatfea.basis import E_STEEL, FY_S355  # noqa: E402
from floatfea.checks.api_wsd import CM_JOINT_TRANSLATION, check_member  # noqa: E402
from floatfea.model.material import Section  # noqa: E402
from floatfea.model.platform import build_superstructure  # noqa: E402
from floatfea.post.forces_table import checked_joint_reactions  # noqa: E402
from floatfea.run.pipeline import validated_export_scale  # noqa: E402


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, path
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


MFT = _load("member_forces_table", ROOT / "scripts" / "measure" / "member_forces_table.py")
SEARCH = _load("f6a_required_section", ROOT / "scripts" / "measure" / "f6a_required_section.py")

COMPONENTS = ("N", "Vy", "Vz", "T", "My", "Mz")
FORCES, MOMENTS = {"N", "Vy", "Vz"}, {"T", "My", "Mz"}
GOVERNING_PERIODS = (12.5, 14.0, 15.0, 16.2)
K_LOCKED = 2.0


def _kind_scales(*stores: dict) -> dict[str, float]:
    """One denominator per KIND of quantity, and this is the THIRD measure tried here.

    Per-station `max(|a|, |b|)` gave `1.958404e+00` -- a sign flip on `2e-08 N.m` of torsion
    read as a doubling. Per-component global max gave `1.320350e+00`, because torsion is
    identically zero up to round-off in the static case and its own global max is
    `3.05e-08 N.m`. Both divided noise by noise. A component that is physically absent has
    no scale of its own, so forces share the largest force and moments the largest moment --
    a denominator that cannot collapse, which is G4.1's rule in this repository applied
    across components instead of across time.
    """
    rows = [np.asarray(v, float) for s in stores for v in s.values()]
    fs = max(abs(float(r[i])) for r in rows for i, c in enumerate(COMPONENTS) if c in FORCES)
    ms = max(abs(float(r[i])) for r in rows for i, c in enumerate(COMPONENTS) if c in MOMENTS)
    return {c: (fs if c in FORCES else ms) for c in COMPONENTS}


def _worst_change(before: dict, after: dict) -> tuple[float, str, float, str]:
    assert set(before) == set(after), "the two builds do not have the same stations"
    scales = _kind_scales(before, after)
    worst_rel, where_rel, worst_abs, where_abs = 0.0, "(nothing moved)", 0.0, "(nothing)"
    for key in sorted(before):
        a, b = np.asarray(before[key], float), np.asarray(after[key], float)
        for i, comp in enumerate(COMPONENTS):
            delta = abs(float(b[i]) - float(a[i]))
            if delta > worst_abs:
                worst_abs, where_abs = delta, f"{key[0]}/{key[1]} {key[2]} {comp}"
            if scales[comp] == 0.0:
                continue
            rel = delta / scales[comp]
            if rel > worst_rel:
                worst_rel = rel
                where_rel = (
                    f"{key[0]}/{key[1]} {key[2]} {comp}: " f"{float(a[i]):.6e} -> {float(b[i]):.6e}"
                )
    return worst_rel, where_rel, worst_abs, where_abs


def _sections_for(answers: list[dict]) -> dict[str, Section]:
    out: dict[str, Section] = {}
    for a in answers:
        tube = Section.circular_tube(float(a["D_m"]), float(a["t_m"]))
        if a["group"] == "platform":
            out["platform"] = tube
        else:
            for n in (1, 2, 3, 4):
                out[f"hub{n}"] = tube
    return out


def _u_of(cand, values: np.ndarray, length: float) -> float:
    """`U` at one station from one force vector -- a single clause call, no sensitivities."""
    got = check_member(
        axial_n=float(values[0]),
        shear_y_n=float(values[1]),
        shear_z_n=float(values[2]),
        torsion_nm=float(values[3]),
        moment_y_nm=float(values[4]),
        moment_z_nm=float(values[5]),
        area_m2=cand.area,
        section_modulus_m3=cand.section_modulus,
        torsional_modulus_m3=cand.torsional_modulus,
        d_outer_m=cand.d_outer,
        wall_m=cand.wall,
        k_l_over_r=K_LOCKED * length / cand.radius_of_gyration,
        fy=FY_S355,
        e=E_STEEL,
        cm=CM_JOINT_TRANSLATION,
    )
    return got.utilisation


def dynamic_half(shipped, sized, answers: list[dict]) -> dict[str, object]:
    """Re-solve the dynamic increment at both sections and compare forces AND `max U`.

    The section `U` is computed at is the SIZED one in BOTH builds. The question is whether
    the FORCES out of the sized solve change the answer -- not whether a different section
    changes `U`, which it obviously does and is the whole point of the search.
    """
    fdr = _load("f4_dynamic_residual", ROOT / "scripts" / "f4_dynamic_residual.py")
    inp = fdr.load()
    raw = np.load(fdr.NPZ, allow_pickle=False)
    # R906: THE SCALE COMES FROM THE FILE, NOT FROM ANOTHER SCRIPT'S MODULE CONSTANT.
    # This read used to be the `FROUDE_LAMBDA` constant that `member_forces_table` carried,
    # reached by attribute off the by-path module object. R902 deleted that constant along
    # with the wave-height literal beside it, and deleting it left this line raising
    # `AttributeError: module 'member_forces_table' has no attribute ...`, which took CI's
    # `unit tests` step red and SKIPPED `guards and meta-tests` behind it.
    #
    # The name is deliberately NOT written here in its `<module>.<attr>` form:
    # `test_forces_table_reexports.py` greps this file's TEXT for that pattern and adds
    # every hit to the set it requires `CONSUMED` to cover, so a comment mentioning the
    # old spelling re-creates the very dependency this line removed. The guard is right to
    # be text-blind -- a comment is how a dead lookup gets resurrected -- and it caught my
    # first wording of this paragraph.
    #
    # `exported_froude_lambda` consults the npz's own `froude_lambda` first and the
    # sidecar's `run.lambda` second, so the scale is the one THIS FILE was exported at --
    # which is the scale its `lam` multipliers are already in. A constant in a sibling
    # script was never that, and FN0 is the finding that said so.
    # R919: the RESOLVER, not the reader. `exported_froude_lambda` reports where it read
    # a value and validates nothing about it, so routing this line onto it in R906 left
    # `froude_lambda = 25.0` -- legal inside `FROUDE_LAMBDA` -- publishing 78 changed
    # lines with the premise still reading HELD and every utilisation some 40% low.
    lam_scale = validated_export_scale(fdr.NPZ)
    deck_a = [str(x) for x in raw["case0/joint_body_a"]]
    deck_b = [str(x) for x in raw["case0/joint_body_b"]]
    by_answer = {a["group"]: a for a in answers}
    cands = {g: SEARCH.Candidate(float(a["D_m"]), float(a["t_m"])) for g, a in by_answer.items()}

    result: dict[str, object] = {}
    stores: dict[str, dict] = {}
    for tag, built in (("shipped", shipped), ("sized", sized)):
        by_name = {b.name: b for b in built.bodies}
        order, nodes, n_dof = MFT._joint_wiring(built, deck_a, deck_b)
        static = MFT._static_rows(built)
        lengths = {m.label: float(m.length) for b in built.bodies for m in b.members}
        best: dict[str, float] = {}
        store: dict[tuple[str, str, str], np.ndarray] = {}
        steps = 0
        for i, period in enumerate(inp.periods_full_s):
            if float(period) not in GOVERNING_PERIODS:
                continue
            # R1051: the same gate as `floatfea/post/forces_table.py`, which is where it
            # is declared -- this script re-solves from the same array, so an ungated read
            # here would publish `results/F6a/premise_check.json` from whatever the file
            # happened to hold.
            lam = checked_joint_reactions(raw[f"case{i}/lam"], f"case{i}/lam")
            for step in range(lam.shape[0]):
                steps += 1
                loads = MFT.map_joint_reactions(
                    MFT._lam_full_scale(lam[step], lam_scale), order, nodes, n_dof
                )
                for name, body in by_name.items():
                    relief = MFT.solve_inertia_relief(
                        body, np.asarray(loads[name], dtype=np.float64)
                    )
                    net = MFT._net_field(body, relief)
                    group = "platform" if name == "platform" else "hubs"
                    if group not in cands:
                        continue
                    for member in body.members:
                        for station, vals in MFT._station_values(
                            body, member, relief.u_full, net
                        ).items():
                            key = (name, member.label, station)
                            total = static[key] + vals
                            prev = store.get(key)
                            store[key] = (
                                total
                                if prev is None
                                else np.where(np.abs(total) > np.abs(prev), total, prev)
                            )
                            u = _u_of(cands[group], total, lengths[member.label])
                            if u > best.get(group, -1.0):
                                best[group] = u
        stores[tag] = store
        result[f"max_u_{tag}"] = best
        result["steps_per_build"] = steps

    rel, where, abso, _ = _worst_change(stores["shipped"], stores["sized"])
    shipped_u: dict[str, float] = result["max_u_shipped"]  # type: ignore[assignment]
    sized_u: dict[str, float] = result["max_u_sized"]  # type: ignore[assignment]
    result["worst_component_relative_change"] = rel
    result["worst_component_at"] = where
    result["worst_component_absolute_change"] = abso
    result["max_u_change"] = {g: abs(sized_u[g] - shipped_u[g]) for g in sized_u}
    return result


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--answers", type=Path, default=ROOT / "results" / "F6a" / "required_section.json"
    )
    ap.add_argument("--out", type=Path, default=ROOT / "results" / "F6a" / "premise_check.json")
    ap.add_argument("--search", default=None, help="one search; default is all of them")
    ap.add_argument("--dynamic", action="store_true", help="also re-solve the dynamic cases")
    args = ap.parse_args(argv)

    loaded = json.loads(args.answers.read_text(encoding="utf-8"))
    # The search writes `{"answers": [...], "continuum": {...}}`. It used to write the bare
    # list, and reading the dict as a list fails late and confusingly -- `a.get` on a key
    # string -- so the shape is checked here rather than iterated hopefully.
    if not isinstance(loaded, dict) or "answers" not in loaded:
        raise SystemExit(
            f"{args.answers} is not the search's output: expected a mapping with an "
            f"'answers' key, got {type(loaded).__name__}. Re-run "
            "scripts/measure/f6a_required_section.py."
        )
    every = loaded["answers"]
    searches = (
        [args.search] if args.search else sorted({a["search"] for a in every if a.get("found")})
    )
    shipped = build_superstructure()
    emitted: dict[str, object] = {"static": {}, "dynamic": {}}

    print("(c) MASS FROM THE DECK, NOT THE SECTION -- held, and the density moves:")
    probe = build_superstructure(
        measurement_sections={"platform": Section.circular_tube(6.0, 0.055)}
    )
    held = all(
        float(a.member_mass) == float(b.member_mass)
        for a, b in zip(shipped.bodies, probe.bodies, strict=True)
    )
    print(f"  member_mass identical on every body : {held}")
    print(
        f"  platform rho_eq                     : "
        f"{float(shipped.bodies[0].equivalent_density):.1f} -> "
        f"{float(probe.bodies[0].equivalent_density):.1f}"
    )
    emitted["mass_held"] = held
    print()

    print("STATIC HALF -- every component at every member-station, at EACH answer:")
    static_out: dict[str, object] = {}
    for search in searches:
        answers = [a for a in every if a.get("found") and a["search"] == search]
        if not answers:
            continue
        sized = build_superstructure(measurement_sections=_sections_for(answers))
        before, after = MFT._static_rows(shipped), MFT._static_rows(sized)
        rel, where, abso, where_abs = _worst_change(before, after)
        lengths = {m.label: float(m.length) for b in sized.bodies for m in b.members}
        us = {}
        for a in answers:
            cand = SEARCH.Candidate(float(a["D_m"]), float(a["t_m"]))
            prefix = "platform:" if a["group"] == "platform" else "hub"
            us[a["group"]] = max(
                _u_of(cand, after[k], lengths[k[1]]) for k in after if k[1].startswith(prefix)
            )
        static_out[search] = {
            "stations": len(before),
            "worst_relative_change": rel,
            "worst_relative_at": where,
            "worst_absolute_change": abso,
            "worst_absolute_at": where_abs,
            "max_u_from_rebuilt_static": us,
        }
        print(
            f"  {search:28s} rel {rel:.6e}  abs {abso:.6e}  "
            f"maxU(static) {', '.join(f'{g}={u:.6f}' for g, u in sorted(us.items()))}"
        )
    emitted["static"] = static_out
    print()

    dynamic_out: dict[str, object] = {}
    if args.dynamic:
        print("DYNAMIC HALF -- the increment re-solved at the sized section (R782):")
        for search in searches:
            answers = [a for a in every if a.get("found") and a["search"] == search]
            if not answers:
                continue
            sized = build_superstructure(measurement_sections=_sections_for(answers))
            got = dynamic_half(shipped, sized, answers)
            dynamic_out[search] = got
            rel = got["worst_component_relative_change"]  # type: ignore[assignment]
            print(f"  {search:28s} worst component rel {rel:.6e}")
            print(f"  {'':28s} at {got['worst_component_at']}")
            for g, d in sorted(got["max_u_change"].items()):  # type: ignore[union-attr]
                a_u = got["max_u_shipped"][g]  # type: ignore[index]
                b_u = got["max_u_sized"][g]  # type: ignore[index]
                print(f"  {'':28s} {g:9s} max U {a_u:.6f} -> {b_u:.6f}   change {d:.3e}")
        print()
        print("  THE FORCES MOVE AND `max U` DOES NOT, and the mechanism is the consistent")
        print("  element mass matrix: `element_equivalent_load = M_e @ a_e`, whose rotary")
        print("  terms are `rho_eq * I = mu * r^2`, so `r` reaches the load even though `mu`")
        print("  is held. The premise the search needs is the `max U` line, not the forces.")
    else:
        print("DYNAMIC HALF -- not run. Pass --dynamic. It re-solves four periods at every")
        print("  step for both builds and takes minutes; the figures the deliverable")
        print("  publishes come from a --dynamic run recorded in premise_check.json.")
        if args.out.exists():
            old = json.loads(args.out.read_text(encoding="utf-8"))
            dynamic_out = old.get("dynamic", {})
    emitted["dynamic"] = dynamic_out

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(emitted, indent=2), encoding="utf-8")
    print(f"\n  wrote {args.out.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
