"""DY7: the joint reactions FloatSim computes, and the per-body equilibrium they close.

WHY THIS SCRIPT EXISTS. DX1 established that FloatSim retains all 64 constraint
multipliers every step (`floatsim/solver/newmark.py:132-137`, `lam: (N+1, m)`, "the
PHYSICAL constraint force ... N on translational rows, N*m on rotational rows;
dt-free") and that the study discards them: `platform_rao_pilot.py:284` binds
`res = integrate_cummins(...)` and reads only `res.t`, `res.xi` and `res.xi_ddot`. The
exported case files carry 21 columns -- time, platform HEAVE, and surge/sway/heave for
three of twelve buoys -- and no external force for any body, so the reactions cannot be
reconstructed from them.

So this reads them from the solve itself. It imports the pinned study read-only, runs
one short case, and reports:

    * what the CSV export actually contains, measured rather than described;
    * one snapshot's reaction at each of the 16 joints -- three forces and the
      locked-axis moment;
    * per-body equilibrium: reactions plus inertia relief minus applied, with the
      residual.

WHAT IT DOES NOT DO. It does not write into `../HSP-runs` and it does not modify the
study. A permanent export is an ADDITIVE change on the HSP side and it is F4's first
item; this is the measurement that says what that export has to carry.

    python scripts/report_joint_reactions.py --period 10.0 --duration 40.0
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from floatfea import hsp_pin  # noqa: E402

HSP_RUNS = ROOT.parent / "HSP-runs"
STUDY = HSP_RUNS / "studies" / "platform-12buoy"
EXPORT = STUDY / "floatfea_design_waves"


def _preflight() -> str:
    """Refuse anything but the pinned runs worktree (DS0)."""
    import subprocess

    if not HSP_RUNS.is_dir():
        raise SystemExit(f"{HSP_RUNS} is not a directory")
    if "HSP-stable" in HSP_RUNS.resolve().parts:
        raise SystemExit("refusing to run against HSP-stable, which is read-only (DS0)")
    described = subprocess.run(
        ["git", "describe", "--tags", "--always"], cwd=HSP_RUNS, capture_output=True, text=True
    ).stdout.strip()
    if not described.startswith(hsp_pin.HSP_TAG):
        raise SystemExit(f"{HSP_RUNS} is at {described!r}, not {hsp_pin.HSP_TAG!r}")
    return described


def report_export() -> None:
    """What the DS1 export carries, read off the file rather than described."""
    cases = sorted(EXPORT.glob("case_*.csv"))
    print(f"## The DS1 export: {len(cases)} case files")
    if not cases:
        print("  none found -- nothing to report")
        return
    header = cases[0].read_text(encoding="utf-8").splitlines()[0].split(",")
    families: dict[str, int] = {}
    for column in header:
        key = column.split("_")[0]
        families[key] = families.get(key, 0) + 1
    print(f"  {len(header)} columns in {cases[0].name}")
    print(f"  by leading token: {families}")
    wanted = [c for c in header if any(k in c.lower() for k in ("lam", "mult", "react", "joint"))]
    print(f"  columns naming a multiplier, reaction or joint: {len(wanted)} {wanted}")
    bodies = {c.split("_")[0] for c in header if c.startswith("buoy")}
    print(f"  buoys represented: {len(bodies)} of 12 -- {sorted(bodies)}")


def solve_one(period_s: float, duration_s: float, dt: float) -> tuple:
    """One short case, returning `(res, setup, deck, ext)`. Read-only on HSP."""
    for path in (HSP_RUNS, STUDY, STUDY.parent / "cluster-3buoy-rigid"):
        sys.path.insert(0, str(path))
    import warnings

    import platform_rao_pilot as prp
    from floatsim.hydro.excitation import make_regular_wave_force
    from floatsim.hydro.readers.capytaine import read_capytaine
    from floatsim.solver.newmark import integrate_cummins
    from floatsim.solver.ramp import HalfCosineRamp
    from floatsim.waves.regular import RegularWave

    deck = prp._deck_with_drag()
    hydro_dof = prp._hydro_dof(deck)
    hdb = read_capytaine(prp._PLAT_NC)
    # The study's own call, verbatim from `platform_rao_pilot.py:397-406`, including
    # the two overrides. Copying it rather than inventing arguments is the point: a
    # setup built differently is a different system and its reactions would not be
    # the ones the DS1 runs produced.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        setup = prp.build_system(
            deck,
            bem_databases={},
            dt=dt,
            t_max_kernel=30.0,
            solve_equilibrium=False,
            shared_hydro_database=hdb,
            asymptote_check_override=prp._ASYMPTOTE_OVR,
            kernel_decay_floor_override=prp._KERNEL_EXEMPT,
        )

    height_m = 0.484  # the DS1 design wave at model scale
    wave = RegularWave(amplitude=0.5 * height_m, omega=2.0 * np.pi / period_s, heading_deg=0.0)
    f72 = make_regular_wave_force(
        hdb=hdb, wave=wave, body_position=(0.0, 0.0, 0.0), ramp=HalfCosineRamp(duration=10.0)
    )
    n_dof = setup.lhs.shape[0] if hasattr(setup.lhs, "shape") else prp._N_DOF

    def ext(t: float) -> np.ndarray:
        f = np.zeros(n_dof, dtype=np.float64)
        f[hydro_dof] = f72(t)
        return f

    res = integrate_cummins(
        lhs=setup.lhs,
        kernel=setup.kernel,
        xi0=setup.xi0,
        xi_dot0=setup.xi_dot0,
        duration=duration_s,
        dt=dt,
        rho_inf=0.8,
        constraints=setup.constraints,
        external_force=ext,
        state_force=setup.state_force,
        projection_interval=1,
    )
    return res, setup, deck, ext


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--period", type=float, default=10.0, help="model-scale period, s")
    ap.add_argument("--duration", type=float, default=40.0, help="model-scale duration, s")
    ap.add_argument("--dt", type=float, default=0.01)
    args = ap.parse_args(argv)

    described = _preflight()
    print(f"HSP {described}\n")
    report_export()

    print(f"\n## One case solved here: T = {args.period:g} s, {args.duration:g} s, dt {args.dt:g}")
    res, setup, deck, ext = solve_one(args.period, args.duration, args.dt)
    if res.lam is None:
        raise SystemExit(
            "the solve returned no multipliers, which means `constraints` did not reach "
            "the integrator -- the whole premise of this report."
        )
    print(f"  res.lam shape {res.lam.shape}   res.xi shape {res.xi.shape}")
    joints = deck.joints
    rows = res.lam.shape[1] // len(joints)
    print(f"  {len(joints)} joints x {rows} rows = {res.lam.shape[1]} multipliers")

    step = -1  # the last step, after the ramp
    lam = res.lam[step]
    print(f"\n## Reactions at t = {res.t[step]:.3f} s (model scale), per joint")
    print(f"{'#':>3} {'A':<8} {'B':<9} {'Fx N':>12} {'Fy N':>12} {'Fz N':>12} {'Mz N.m':>12}")
    print("-" * 72)
    for i, joint in enumerate(joints):
        d = joint.model_dump()
        block = lam[i * rows : (i + 1) * rows]
        print(
            f"{i + 1:>3} {d['body_a']:<8} {d['body_b']:<9} "
            f"{block[0]:>12.4e} {block[1]:>12.4e} {block[2]:>12.4e} {block[3]:>12.4e}"
        )
    print(f"\n  |F| range {np.min(np.abs(lam)):.4e} to {np.max(np.abs(lam)):.4e}")
    # ---- what the reactions balance, and what this cannot close -------------
    print("\n## What the reactions balance, per body")
    g = setup.constraints.jacobian(res.xi[step])
    reaction = g.T @ lam
    t_now = float(res.t[step])
    applied = np.asarray(ext(t_now), dtype=np.float64)
    if getattr(setup, "state_force", None) is not None:
        applied = applied + np.asarray(
            setup.state_force(t_now, res.xi[step], res.xi_dot[step]), dtype=np.float64
        )
    names = [b.name for b in deck.bodies]
    print(f"{'body':<10} {'|reaction|':>13} {'|applied|':>13} {'|R + A|':>13}")
    print("-" * 52)
    for k, name in enumerate(names):
        sl = slice(6 * k, 6 * k + 6)
        r, a = reaction[sl], applied[sl]
        print(
            f"{name:<10} {np.max(np.abs(r)):>13.4e} {np.max(np.abs(a)):>13.4e} "
            f"{np.max(np.abs(r + a)):>13.4e}"
        )

    weight = 28.67 * 9.81
    buoy_fz = float(np.max(np.abs([lam[i * rows + 2] for i in range(12)])))
    print(
        "\n  WHAT THIS DOES NOT CLOSE, AND IT IS NOT A DEFECT IN THE NUMBERS."
        "\n  DY7 asks for `reactions + inertia relief - applied` with the residual. The"
        "\n  inertia term here is the CUMMINS operator: an infinite-frequency added mass"
        "\n  plus a convolution over the radiation kernel, plus the hydrostatic restoring"
        "\n  `C @ xi`. Closing the identity needs the per-body added-mass matrix and the"
        "\n  memory state at this step, and neither is exported -- the same gap DX1 found"
        "\n  for the multipliers, one level deeper. `|R + A|` above is the part that IS"
        "\n  available, not the residual DY7 wants."
        "\n"
        "\n  AND THE REACTIONS ARE PERTURBATIONS, NOT TOTALS. The study builds with"
        "\n  `solve_equilibrium=False` and `xi` is displacement from the reference, so"
        f"\n  `lam` is the reaction ABOUT the equilibrium state. The largest buoy-joint Fz"
        f"\n  is {buoy_fz:.4f} N against a buoy weight of 28.67 * 9.81 = {weight:.1f} N,"
        f"\n  a ratio of {buoy_fz / weight:.2e}, which is what says so. Member forces need"
        "\n  static PLUS dynamic, so F4's export has to carry the equilibrium reaction as"
        "\n  well as the history."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
