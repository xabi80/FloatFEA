#!/usr/bin/env python
"""How far the fixture's channels are from this machine's closed form (CJ1).

    python scripts/measure_channel_drift.py

G1.1 asserts that a record the writer produced round-trips against the closed
forms the generator used. It asserted BIT-EXACTNESS, and on CI thirteen of the
pairs fail: `sin` and `cos` are not correctly rounded, no two libm
implementations are obliged to agree in the last bit, and the fixture is a
committed golden produced on one machine.

That is Q8's second local class -- "through `sin`, `cos`, or a factorisation:
`<= 2` ULP of the channel's own amplitude" -- and this is the measurement the
class's tolerance is declared from. It prints, per channel:

    amplitude      max |value| over the channel, which is what an ULP is of
    max abs diff   the largest disagreement with the fixture
    ULP of ampl.   that difference in ULP of the amplitude
    exact          how many of the channel's values agree bit for bit

It asserts nothing. Run it on the canonical machine and on a laptop, and the
tolerance is declared from the pair -- with the stamp of the machine printed
beside it, because a drift figure with no machine attached is the defect this
whole line of work exists to remove.
"""

from __future__ import annotations

import math
import os
import platform
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "writer_output.flr"
N, NB, DT = 24, 2, 0.05
NDOF = 6 * NB


def expected() -> dict[str, np.ndarray]:
    """The generator's closed forms, as `tests/verification/rung4` restates them."""
    t = np.arange(N + 1) * DT
    j = np.arange(NDOF)[None, :]
    rot = (np.arange(NDOF) % 6) >= 3
    xi = np.sin(1.7 * t[:, None] + 0.31 * j) * (1.0 + 0.05 * j)
    xi[:, rot] *= 0.02
    return {
        "t": t,
        "xi": xi,
        "xi_dot": np.cos(2.3 * t[:, None] - 0.17 * j) * (2.0 + 0.03 * j),
        "xi_ddot": np.sin(3.1 * t[:, None] + 0.09 * j) * (3.0 - 0.02 * j),
        "lam": np.cos(1.1 * t[:, None] + 0.5 * np.arange(4)[None, :]),
    }


DATASETS = {
    "xi": ("kinematics/{body}/position", "kinematics/{body}/rotation"),
    "xi_dot": ("kinematics/{body}/velocity", "kinematics/{body}/angular_velocity"),
    "xi_ddot": ("kinematics/{body}/acceleration", "kinematics/{body}/angular_acceleration"),
}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    import h5py

    want = expected()
    print(f"machine     {sys.platform} / {platform.machine()}")
    print(f"python      {platform.python_version()}   numpy {np.__version__}")
    print(f"coretype    {os.environ.get('OPENBLAS_CORETYPE', 'unset')}")
    print(f"fixture     {FIXTURE.relative_to(ROOT)}")
    print()
    print(
        f"{'channel':<34} {'amplitude':>12} {'max abs diff':>14} {'ULP of ampl':>12} {'exact':>10}"
    )
    worst = 0.0
    with h5py.File(FIXTURE, "r") as f:
        rows: list[tuple[str, np.ndarray, np.ndarray]] = [
            ("joints/lam", f["joints/lam"][...], want["lam"])
        ]
        rows.append(("time/t", f["time/t"][...], want["t"]))
        for k, body in enumerate(("bodyA", "bodyB")):
            for channel, paths in DATASETS.items():
                for offset, path in zip((0, 3), paths, strict=True):
                    name = path.format(body=body)
                    got = f[name][...]
                    ref = want[channel][:, 6 * k + offset : 6 * k + offset + 3]
                    rows.append((name, got, ref))
        for name, got, ref in rows:
            ampl = float(np.max(np.abs(ref)))
            if ampl == 0.0:
                # R329/R338: THE SECOND SITE. The test helper was repaired and
                # this one was not, so the same invented scale survived in the
                # instrument the plan's basis is measured with -- which is the
                # worse of the two places for it.
                raise ValueError(
                    f"{name} is identically zero in the reference, so there is "
                    "no amplitude to measure ULP against. A channel that "
                    "should be zero and is not is a defect, not a rounding "
                    "question."
                )
            diff = float(np.max(np.abs(got - ref)))
            ulp = diff / math.ulp(ampl)
            exact = int(np.count_nonzero(got == ref))
            worst = max(worst, ulp)
            print(f"{name:<34} {ampl:12.6e} {diff:14.6e} {ulp:12.4f} {exact:>6}/{ref.size}")
    print()
    print(f"worst channel drift  {worst:.4f} ULP of that channel's amplitude")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
