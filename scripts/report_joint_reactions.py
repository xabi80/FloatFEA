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
from floatfea.io.integrator import (  # noqa: E402
    generalized_alpha_coefficients,
    rho_inf_from_deck,
)

# C131 (CW0). `rho_inf` was written twice -- passed to the integrator in
# `solve_one` and re-declared in `discrete_residual` with a comment asserting the
# two agreed. A comment is not a mechanism: ONE constant, both call sites, so
# they cannot disagree. The value is the study's own:
#   cmd: sed -n 291p ../HSP-runs/studies/platform-12buoy/platform_rao_pilot.py
#   out: rho_inf=0.8,
#
# IT IS A REPRODUCIBILITY CONSTANT AND NOT A TOLERANCE, so it does not belong in
# `floatfea/tolerances.py`. The repository's own evidence, not a reading:
#   cmd: grep -n rho_inf floatfea/io/reader.py
#   out: 50: {"scheme", "rho_inf", "alpha_m", "alpha_f", "beta", "gamma", ...}
#   cmd: grep -n rho_inf tests/verification/rung4/test_validator_matrix.py
#   out: 65: "rho_inf": 0.9,
# -- a declared interchange SCHEME FIELD, exercised at another value, compared
# against nothing.
#
# THE JUSTIFICATION THIS COMMENT FIRST CARRIED IS RETRACTED (R653). It said a
# 0.05 drift makes the residual "429x louder". That figure measured a MISMATCH
# BETWEEN TWO COPIES, and a single constant makes a mismatch unconstructible;
# varying the value moves the residual by about 1.0005x. The behaviour is correct
# and must not be undone -- the residual stays sensitive to a wrong RECONSTRUCTION
# by two to three decades.
#
# R653 IS ANSWERED (EQ2(e)). The constant and the derivation that follows from it now
# live in `floatfea/io/integrator.py`, where the FE side declares them and
# `tests/verification/rung4/test_f4_static_and_mapping.py` asserts them against
# `docs/load-interchange-v1.md` sec.6's own published coefficients. The grep that used
# to return nothing now returns the declaration and the gate:
#   cmd: grep -rln RHO_INF floatfea/ tests/
#   out: floatfea/io/integrator.py, tests/verification/rung4/test_f4_static_and_mapping.py
# The condition verdict 92 set for it to become blocking has arrived: F4 step 2's G4.1
# cites this residual per body and per case.
RHO_INF = rho_inf_from_deck()

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
        rho_inf=RHO_INF,
        constraints=setup.constraints,
        external_force=ext,
        state_force=setup.state_force,
        projection_interval=1,
    )
    return res, setup, deck, ext


def discrete_residual(res, setup, ext, window: int = 100) -> dict[str, float]:
    """The residual of the system `newmark.py:414-437` ACTUALLY solves.

    R646. An earlier version of this script printed that the identity could not be
    closed because "the per-body added-mass matrix and the memory state are not
    exported". Both are in process: `A_inf` is inside `setup.lhs.M_plus_Ainf`, and
    `mu_n = sum_k K_k @ xi_dot_{n-k} dt` is a deterministic function of
    `setup.kernel` and `res.xi_dot`, which this script already holds. So it is
    formed here rather than described.

    The continuous identity `sum(reactions) + applied - M a` does NOT close to
    round-off and is not meant to: `newmark.py:48` documents `mu_{n+1-alpha_f} ~=
    mu_n` as an O(h) lag, and `docs/load-interchange-v1.md` sec.4.1-4.2 chooses the
    discrete form for exactly that reason. Both are reported.
    """
    from floatsim.hydro.retardation import RadiationConvolution

    h = float(res.t[1] - res.t[0])
    # Every alpha/beta/gamma follows from `rho_inf`, and the formula is written once
    # in `floatfea/io/integrator.py` rather than here (R653).
    alpha_m, alpha_f, beta, _gamma = generalized_alpha_coefficients(RHO_INF)
    m_eff = setup.lhs.M_plus_Ainf
    c_mat = setup.lhs.C
    a_eff = (1.0 - alpha_m) * m_eff + (1.0 - alpha_f) * (h**2) * beta * c_mat

    # `mu`, rebuilt by pushing the solver's own velocity history through a fresh
    # buffer. The push of `xi_dot_0` BEFORE the loop and `mu_0 = 0` are both the
    # integrator's startup convention (`newmark.py:384-391`), not a choice here.
    buffer = RadiationConvolution(setup.kernel)
    buffer.push(res.xi_dot[0])
    n_steps = res.xi.shape[0]
    mu = np.zeros_like(res.xi_dot)
    for n in range(1, n_steps):
        buffer.push(res.xi_dot[n])
        mu[n] = buffer.evaluate()

    def force_at(n: int) -> np.ndarray:
        """`F_np1` as the loop builds it: time term at t_n, state term LAGGED."""
        f = np.asarray(ext(float(res.t[n])), dtype=np.float64)
        if getattr(setup, "state_force", None) is not None and n > 0:
            f = f + np.asarray(
                setup.state_force(float(res.t[n - 1]), res.xi[n - 1], res.xi_dot[n - 1]),
                dtype=np.float64,
            )
        return f

    worst_discrete = 0.0
    worst_mu = 0.0
    for n in range(max(1, n_steps - window), n_steps):
        xi_n, xi_dot_n, xi_ddot_n = res.xi[n - 1], res.xi_dot[n - 1], res.xi_ddot[n - 1]
        xi_pred = xi_n + h * xi_dot_n + (h**2) * (0.5 - beta) * xi_ddot_n
        rhs = (
            (1.0 - alpha_f) * force_at(n)
            + alpha_f * force_at(n - 1)
            - alpha_m * (m_eff @ xi_ddot_n)
            - (1.0 - alpha_f) * (c_mat @ xi_pred)
            - alpha_f * (c_mat @ xi_n)
            - mu[n - 1]
        )
        g_mid = setup.constraints.jacobian(0.5 * (xi_n + res.xi[n]))
        resid = a_eff @ res.xi_ddot[n] - g_mid.T @ res.lam[n] - rhs
        worst_discrete = max(worst_discrete, float(np.max(np.abs(resid))))
        worst_mu = max(worst_mu, float(np.max(np.abs(mu[n]))))
    return {"discrete_worst_N": worst_discrete, "mu_inf_N": worst_mu, "window": float(window)}


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

    # C38: THE BUOY JOINTS ARE NOT THE FIRST TWELVE. The joint order is interleaved --
    # three buoy joints then a hub->platform joint, four times over -- so `range(12)`
    # took in joints 3, 7 and 11, which are hub->platform, and left out buoy10, buoy11
    # and buoy12 entirely. Selected by NAME instead.
    buoy_rows = [
        i for i, joint in enumerate(joints) if joint.model_dump()["body_a"].startswith("buoy")
    ]
    assert len(buoy_rows) == 12, f"expected 12 buoy joints, found {len(buoy_rows)}"
    buoy_fz = float(np.max(np.abs([lam[i * rows + 2] for i in buoy_rows])))
    print(f"  largest buoy-joint Fz at this step  {buoy_fz:.4e} N")

    marks = discrete_residual(res, setup, ext)
    print("\n## The residual of the system the integrator ACTUALLY solves (R646)")
    print(f"  |mu|_inf over the window                          {marks['mu_inf_N']:.6e} N")
    print(
        f"  worst |A_eff a - G^T lam - rhs| over {int(marks['window'])} steps  "
        f"{marks['discrete_worst_N']:.6e} N"
    )
    print(
        "\n  The CONTINUOUS identity `sum(reactions) + applied - M a` does not close to"
        "\n  round-off and is not meant to: `newmark.py:48` documents"
        "\n  `mu_{n+1-alpha_f} ~= mu_n` as an O(h) lag, and `docs/load-interchange-v1.md`"
        "\n  sec.4.1-4.2 chooses the discrete form so that G4.1 means what it says. The"
        "\n  figure above is that discrete form, formed from `setup.kernel`,"
        "\n  `res.xi_dot` and `setup.lhs.M_plus_Ainf` -- every one of them in process."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
