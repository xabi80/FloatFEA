#!/usr/bin/env python
"""EV1's G4.1 dynamic residual: two gated dimensionless numbers, per FE body and case.

    python scripts/measure/g41_dynamic.py                 # all six DQ6 cases
    python scripts/measure/g41_dynamic.py --period 14.0   # one case

WHAT IT MEASURES, in EV1's own form. Per FE body -- the platform and the four hubs; the
twelve buoys carry no FE mass (DQ7) and are out of the gate -- and per case, over the DQ6
window:

    force  :  max_t |Sum_j F_j - M.a|                          /  max_t Sum_j |F_j|
    moment :  max_t |Sum_j (r_j x F_j + M_j) - J.alpha - ...|  /
              max_t Sum_j (|r_j x F_j| + |M_j|)

**The denominators are sums of MAGNITUDES**, so cancellation cannot shrink them. That is
the property the superseded single-scalar form lacked: a window in which the reactions
nearly balance has a small `|Sum_j F_j|` and an ordinary `Sum_j |F_j|`, and dividing by
the first manufactures a large relative residual out of a quiet case.

THE RESIDUAL IS THE DISCRETE ONE, as locked, and R711 is why that sentence needed to be
earned. The continuous identity does not close to round-off: `newmark.py:48` documents
`mu_{n+1-alpha_f} ~= mu_n` as an O(h) lag, and `docs/load-interchange-v1.md` sec.4.1-4.2
chose the discrete form so that G4.1 means what it says.

**The first version of this script formed the CONTINUOUS balance and this docstring said
it formed the discrete one.** Measured against the locked form over the same window, the
force channel read `2.393343e-03` where the locked form reads `1.086249e-16` -- a factor
of `2.2e+13`, and a ceiling declared by the window rule from the wrong quantity would have
been thirteen decades loose on a channel that closes to round-off. The terms that were
missing are the generalized-alpha weights, `C`, `mu`, the external force and the MIDPOINT
Jacobian; of those, `ext`, `C`, `mu` and the added-mass contribution are identically zero
on the five FE bodies (EK0(a)), so the cost was `alpha_m M_eff xi_ddot_{n-1}` and
`(g_mid - g_now)^T lam`.

The form here is `report_joint_reactions.py::discrete_residual`'s, mirrored line for line,
per body -- and the loop carries a CONTROL comparing the per-body decomposition against
the same residual's whole-state maximum, because nothing else in this script would notice
a wrong slice.

WHERE THE MOMENT IS TAKEN -- AND EV1's WORDING DISAGREES WITH THE LOCKED CONVENTIONS.

EV1 writes the moment numerator as `Sum_j (r_j x F_j + M_j)` and says moments are taken
about the body's `G`. `docs/conventions.md`, locked at F0 and authoritative, says the
opposite three times:

    cmd  grep -niE "reference point|centre of gravity|CoG" docs/conventions.md
    out  113: | Body frame origin | body_reference_point (**not** the CoG) |
    out  159: - **Origin: the body `reference_point`, NOT the centre of gravity.**
    out  165: - **Moments are taken about the body reference point**, not the CoG
    out  171: The record declares the inertia tensor **about the body reference point**
    out  182-184: reference point -1.1956674 m, CoG -1.23268 m, **offset +37.0 mm**

So on this platform the two points are not coincident, and the document says in those
words that they "must not be conflated". What makes the figures the same number anyway is
FloatSim's own assumption:

    cmd  grep -rn "cog_offset_body" ../HSP-runs/floatsim/bodies/mass_properties.py
    out  49:    cog_offset_body: NDArray[np.floating] | None = None,
    out  81:    if cog_offset_body is None:
    judge `driver.py:222` passes None, which mass_properties.py defines as CoG AT the
          reference point. Inside the solve the two coincide by construction.

**So the moment here is formed about the REFERENCE POINT**, which is the point the
Jacobian's rotational rows are already about, the point the conventions declare, and the
point FloatSim treats as `G`. The numerator is numerically identical to EV1's under
FloatSim's assumption; what differs is the label and what a later reader does with it.
`CLAUDE.md` says never to assume a frame and to stop rather than pick the one that makes
the test pass -- so this is taken as the conservative branch, stated here, and **flagged
for Xabier rather than resolved from inside a measurement script.**

An earlier draft of this docstring claimed the script formed the moment two ways and
printed the disagreement. It did not: the line that would have done it was a
`max(gap, 0.0)` placeholder, and the check that replaced it compared a CoG field the deck
does not have. Both were CW0's defect in a new file, found by running it.

WHAT IT IS NOT. It measures and asserts nothing. The gate is `tests/verification/`'s and
its `# expected:` side is written there, not borrowed from here (EA4). Read-only on HSP:
it imports the pinned study from `../HSP-runs` and never `../HSP-stable` (DS0).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from floatfea.io.integrator import (  # noqa: E402
    generalized_alpha_coefficients,
    rho_inf_from_deck,
)

RHO_INF = rho_inf_from_deck()
"""The study's own spectral radius, read from the deck rather than typed (R686)."""

LAMBDA = 50.0
"""Froude scale. `docs/conventions.md` is authoritative; this is the model-scale factor."""

T_FULL = (10.0, 12.5, 14.0, 15.0, 16.2, 20.0)
"""DQ6's six design-wave periods, full scale, from `scripts/run_floatsim_design_waves.py`."""

RAMP_S = 10.0
"""The study's ramp, model scale."""

FE_BODIES = ("platform", "hub1", "hub2", "hub3", "hub4")
"""The bodies that carry FE mass. DQ7: buoys are loads, with no FE mass."""

DT = 0.01


def window_duration(period_model_s: float) -> float:
    """DQ6: the last 5 whole periods, starting no earlier than ramp + 10 periods.

    So a run must reach `ramp + 15 periods`, and DQ6 says a run too short is EXTENDED.
    The EJ4 runs used 40 s flat, which is long enough for `T_full = 10` and three
    periods short for `T_full = 20` -- the case where the window matters most, because
    it is the longest period and the one closest to the platform's own response.
    """
    return RAMP_S + 15.0 * period_model_s


def window_slice(t: np.ndarray, period_model_s: float) -> slice:
    """The last 5 whole periods of `t`, starting no earlier than ramp + 10 periods."""
    start_floor = RAMP_S + 10.0 * period_model_s
    end = float(t[-1])
    start = max(start_floor, end - 5.0 * period_model_s)
    lo = int(np.searchsorted(t, start))
    return slice(lo, len(t))


def per_joint_contributions_from(g, lam, n_bodies: int) -> np.ndarray:
    """As `per_joint_contributions`, but from a Jacobian the caller already has.

    The numerator is formed at the step MIDPOINT, and the denominators must be about the
    same configuration -- so the caller computes `g_mid` once and both read it. Two
    `jacobian()` calls at different arguments is how a numerator and its denominator come
    to describe different states.
    """
    from floatfea.loads.joint_reactions import ROWS_PER_JOINT

    n_joints = g.shape[0] // ROWS_PER_JOINT
    out = np.zeros((n_joints, n_bodies, 6), dtype=np.float64)
    for j in range(n_joints):
        rows = slice(ROWS_PER_JOINT * j, ROWS_PER_JOINT * (j + 1))
        full = np.asarray(g[rows].T @ np.asarray(lam)[rows], dtype=np.float64)
        for k in range(n_bodies):
            out[j, k] = full[6 * k : 6 * k + 6]
    return out


def per_joint_contributions(setup, xi, lam, n_bodies: int) -> np.ndarray:
    """`(n_joints, n_bodies, 6)` -- each joint's generalized reaction on each body.

    `g.T @ lam` is the reaction on every DOF at once. Taking one joint's rows alone
    gives that joint's own contribution, which is what `Sum_j |F_j|` needs: the sum of
    magnitudes over joints, not the magnitude of their sum.
    """
    from floatfea.loads.joint_reactions import ROWS_PER_JOINT

    g = setup.constraints.jacobian(xi)
    n_joints = g.shape[0] // ROWS_PER_JOINT
    out = np.zeros((n_joints, n_bodies, 6), dtype=np.float64)
    for j in range(n_joints):
        rows = slice(ROWS_PER_JOINT * j, ROWS_PER_JOINT * (j + 1))
        full = np.asarray(g[rows].T @ np.asarray(lam)[rows], dtype=np.float64)
        for k in range(n_bodies):
            out[j, k] = full[6 * k : 6 * k + 6]
    return out


def moment_point(deck) -> str:
    """The point the moment residual is taken about, named rather than assumed.

    The deck carries `reference_point` per body and NO CoG field -- which is why an
    earlier version of this function, comparing a `cog` attribute, refused every body
    with "no CoG field to compare". There is nothing to compare: the conventions declare
    the reference point to BE the point moments are taken about, and FloatSim's
    `cog_offset_body=None` makes it the CoG inside the solve.

    Returns a sentence for the run log, so the figure is never read without its point.
    """
    points = {b.name: np.asarray(b.reference_point, dtype=np.float64) for b in deck.bodies}
    missing = [n for n, v in points.items() if v.shape != (3,)]
    if missing:
        raise SystemExit(
            f"these bodies have no usable `reference_point`: {missing}. The moment "
            "residual has no point to be about."
        )
    return (
        "moments about each body's `reference_point` (docs/conventions.md:165), which "
        "FloatSim treats as the CoG via `cog_offset_body=None` -- NOT about `G` as EV1's "
        "wording says; see this script's docstring"
    )


def measure_case(period_full_s: float, dt: float = DT, no_override: bool = False) -> dict:
    """One case: EV1's two numbers per FE body, plus the two counter responses."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import report_joint_reactions as rjr
    from report_joint_reactions import solve_one

    # ER0's BASIS, APPLIED IN MEMORY (ER1(b)). `report_joint_reactions.py` ships with the
    # override OFF -- `PLATFORM_MASS_OVERRIDE = None`, which is R700's subject -- and the
    # gate's figures must be on the basis the model ships. HSP-stable is read-only at
    # `floatfea-ref-1` (DS0) and FloatSim is not forked, so the override belongs where the
    # INPUT is assembled. The values are the ones `data/platform/platform12_deck.yaml`
    # declares in its own OVERRIDE header, at model scale.
    if not no_override:
        rjr.PLATFORM_MASS_OVERRIDE = {
            "mass": 20.0,
            "inertia": {"Ixx": 20.0, "Iyy": 20.0, "Izz": 40.0},
        }

    period_model = period_full_s / LAMBDA**0.5
    duration = window_duration(period_model)
    print(
        f"\n## T_full = {period_full_s:g} s  (model {period_model:.4f} s), "
        f"duration {duration:.2f} s, dt {dt:g}",
        flush=True,
    )
    res, setup, deck, ext = solve_one(period_model, duration, dt)
    print(f"  {moment_point(deck)}", flush=True)
    if res.lam is None:
        raise SystemExit(
            "the solve returned no multipliers, so there are no reactions to form a "
            "residual from. `constraints` did not reach the integrator."
        )

    names = [b.name for b in deck.bodies]
    n_bodies = len(names)
    win = window_slice(np.asarray(res.t), period_model)
    steps = len(range(*win.indices(len(res.t))))
    print(f"  window: {steps} steps, t = {res.t[win][0]:.3f} .. {res.t[win][-1]:.3f} s", flush=True)
    if steps < 2:
        raise SystemExit(f"the DQ6 window holds {steps} steps; the run is too short.")

    alpha_m, alpha_f, beta, _gamma = generalized_alpha_coefficients(RHO_INF)
    m_eff = setup.lhs.M_plus_Ainf

    # Per body and per step: the numerator from the discrete balance, and the two
    # magnitude-sum denominators. Maxima over the window, never means -- `CLAUDE.md`
    # forbids averaging a per-case diagnostic.
    num_f = {n: 0.0 for n in names}
    num_m = {n: 0.0 for n in names}
    den_f = {n: 0.0 for n in names}
    den_m = {n: 0.0 for n in names}

    # R711: THE DISCRETE BALANCE, mirroring `report_joint_reactions.discrete_residual`
    # line for line. An earlier version of this loop formed `Sum_j G^T lam - M ddot` at
    # `xi[n]` -- the CONTINUOUS balance -- which the plan does not lock and which reads
    # 2.2e+13 times larger on the force channel.
    from floatsim.hydro.retardation import RadiationConvolution

    h = float(res.t[1] - res.t[0])
    c_mat = setup.lhs.C
    a_eff = (1.0 - alpha_m) * m_eff + (1.0 - alpha_f) * (h**2) * beta * c_mat

    # `mu`, rebuilt by pushing the solver's own velocity history through a fresh buffer.
    # The push of `xi_dot[0]` BEFORE the loop and `mu[0] = 0` are the integrator's own
    # startup convention (`newmark.py:384-391`), not a choice here.
    buffer = RadiationConvolution(setup.kernel)
    buffer.push(res.xi_dot[0])
    mu = np.zeros_like(res.xi_dot)
    for i in range(1, res.xi.shape[0]):
        buffer.push(res.xi_dot[i])
        mu[i] = buffer.evaluate()

    def force_at(i: int) -> np.ndarray:
        """`F_np1` as the loop builds it: time term at `t_i`, state term LAGGED."""
        f = np.asarray(ext(float(res.t[i])), dtype=np.float64)
        if getattr(setup, "state_force", None) is not None and i > 0:
            f = f + np.asarray(
                setup.state_force(float(res.t[i - 1]), res.xi[i - 1], res.xi_dot[i - 1]),
                dtype=np.float64,
            )
        return f

    whole_state_worst = 0.0
    decomposition_gap = 0.0
    for n in range(*win.indices(len(res.t))):
        if n == 0:
            continue  # the discrete form reads step n-1
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
        # THE JACOBIAN IS AT THE STEP MIDPOINT, which `newmark.py` says in its own
        # comment and which the continuous version got wrong: `(g_mid - g_now).T lam`
        # alone is 3.008e-05 .. 6.538e-04, itself up to 480x a hub's locked residual.
        mid = 0.5 * (xi_n + res.xi[n])
        lam = np.asarray(res.lam[n], dtype=np.float64)
        g_mid = setup.constraints.jacobian(mid)
        reaction = np.asarray(g_mid.T @ lam, dtype=np.float64)
        resid = np.asarray(a_eff @ res.xi_ddot[n] - reaction - rhs, dtype=np.float64)
        # The denominators need each joint's own contribution, not their sum. Taken from
        # the SAME `g_mid` the numerator used, so the two cannot be about different
        # configurations.
        contrib = per_joint_contributions_from(g_mid, lam, n_bodies)
        # AND THE DECOMPOSITION IS ASSERTED AGAINST THE LOCKED FORM'S OWN TERM, which is
        # a stronger control than comparing maxima: if the per-joint slicing were wrong,
        # the sum over joints would not reproduce `g_mid.T lam`.
        rebuilt = contrib.sum(axis=0).reshape(-1)
        if rebuilt.shape != reaction.shape:
            raise SystemExit(
                f"the per-joint decomposition has shape {rebuilt.shape} and the "
                f"reaction vector {reaction.shape}; the bodies do not partition the "
                "state as this script assumes."
            )
        scale = float(np.max(np.abs(reaction))) or 1.0
        gap = float(np.max(np.abs(rebuilt - reaction))) / scale
        decomposition_gap = max(decomposition_gap, gap)
        whole_state_worst = max(whole_state_worst, float(np.max(np.abs(resid))))
        for k, name in enumerate(names):
            block = resid[6 * k : 6 * k + 6]
            num_f[name] = max(num_f[name], float(np.linalg.norm(block[0:3])))
            num_m[name] = max(num_m[name], float(np.linalg.norm(block[3:6])))
            den_f[name] = max(
                den_f[name],
                float(np.sum(np.linalg.norm(contrib[:, k, 0:3], axis=1))),
            )
            den_m[name] = max(
                den_m[name],
                float(np.sum(np.linalg.norm(contrib[:, k, 3:6], axis=1))),
            )

    # THE CONTROL. If the per-body slicing were wrong, the per-body maxima could be
    # anything and no other line here would notice. The largest per-body component must
    # BE the largest component of the whole-state residual, because the bodies partition
    # the state.
    print(
        f"  control: the per-joint decomposition reproduces `g_mid.T lam` to "
        f"{decomposition_gap:.3e} relative, worst over the window",
        flush=True,
    )
    print(
        f"  control: whole-state discrete residual worst {whole_state_worst:.6e} "
        "(all 102 DOF, the aggregate DQ8 forbids as a gate)",
        flush=True,
    )

    out = {"period_full_s": period_full_s, "steps": int(steps), "bodies": {}}
    print(f"  {'body':<10} {'force rel':>14} {'moment rel':>14} {'den_f':>12} {'den_m':>12}")
    for name in names:
        if name not in FE_BODIES:
            continue
        f_rel = num_f[name] / den_f[name] if den_f[name] > 0.0 else float("nan")
        m_rel = num_m[name] / den_m[name] if den_m[name] > 0.0 else float("nan")
        out["bodies"][name] = {
            "force_rel": f_rel,
            "moment_rel": m_rel,
            "num_force": num_f[name],
            "num_moment": num_m[name],
            "den_force": den_f[name],
            "den_moment": den_m[name],
        }
        print(
            f"  {name:<10} {f_rel:>14.6e} {m_rel:>14.6e} {den_f[name]:>12.4e} "
            f"{den_m[name]:>12.4e}"
        )
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--period", type=float, action="append", help="one full-scale period")
    ap.add_argument("--dt", type=float, default=DT)
    ap.add_argument("--out", type=Path, default=None, help="write the figures as JSON")
    ap.add_argument(
        "--no-override",
        action="store_true",
        help="HSP's deck as exported, WITHOUT ER0's platform basis -- for comparison only",
    )
    args = ap.parse_args(argv)

    periods = args.period or list(T_FULL)
    print("=" * 96)
    print("EV1 / G4.1 DYNAMIC -- two gated dimensionless residuals, per FE body and case")
    print("=" * 96)
    print(f"  rho_inf {RHO_INF} (from the deck)   FE bodies {', '.join(FE_BODIES)}")
    print("  DQ6 window: last 5 whole periods, starting no earlier than ramp + 10")

    cases = [measure_case(p, args.dt, args.no_override) for p in periods]

    print()
    print("=" * 96)
    print(f"WORST OVER ALL {len(cases) * len(FE_BODIES)} BODY-CASES")
    print("=" * 96)
    worst_f = max(
        (c["bodies"][b]["force_rel"], f"{b}/T{c['period_full_s']:g}")
        for c in cases
        for b in c["bodies"]
    )
    worst_m = max(
        (c["bodies"][b]["moment_rel"], f"{b}/T{c['period_full_s']:g}")
        for c in cases
        for b in c["bodies"]
    )
    print(f"  force  worst {worst_f[0]!r}  at {worst_f[1]}")
    print(f"  moment worst {worst_m[0]!r}  at {worst_m[1]}")

    if args.out:
        args.out.write_text(json.dumps(cases, indent=2) + "\n", encoding="utf-8")
        print(f"  figures written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
