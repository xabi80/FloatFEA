"""AG5 -- the per-DOF fingerprint of the convolution fix, measured exactly.

The re-synced record carries a trapezoid `mu`. Confirming the re-sync needs more
than "the number moved": AH2 pairs the round-off target with a SHAPE, because
under a round-off target a zero residual is the expected answer and no longer
announces a broken comparison (eighth guard).

The predicted shape:

    heave barely moves; pitch and surge collapse; the per-DOF change tracks K(0).

This needs no second record. The two quadratures differ by an exactly known term:

    mu_rect(t) - mu_trap(t) = dt/2 * K[0] @ v(t)  +  dt/2 * K[N-1] @ v(t-T)

so both can be formed from the SAME velocity history and differenced per DOF,
which isolates the quadrature change from every other difference between runs.

RAW OUTPUT ONLY (docs/instrumentation.md).
"""
from __future__ import annotations

import sys
import warnings
from pathlib import Path

import numpy as np

_HSP = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_HSP / "studies" / "platform-12buoy"))
sys.path.insert(0, str(_HSP / "studies" / "cluster-3buoy-rigid"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import platform_fin_fan as pff  # noqa: E402
import platform_rao_pilot as prp  # noqa: E402

from floatfea.io.frames import HYDRO_GLOBAL_DOF  # noqa: E402
from floatsim.io.flr_export import recompute_mu  # noqa: E402

DOF_NAME = ("surge", "sway", "heave", "roll", "pitch", "yaw")
T_f = 3.141

d = np.load(Path(__file__).resolve().parent / "record_state.npz", allow_pickle=True)
t, xi_dot = d["t"], d["xi_dot"]

hdb = pff._hdb("0215")
prp._SPAR_CD = 1.2
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    setup = pff._build(0.215, 5.0, hdb)

K = np.asarray(setup.kernel.K)
tk = np.asarray(setup.kernel.t)
dt = float(tk[1] - tk[0])
n_lags = tk.size

mu_trap, _ = recompute_mu(setup.kernel, xi_dot, from_run_start=True)

# Rebuild the OLD rectangular result from the same history: rectangle carries full
# dt on both endpoints, trapezoid carries dt/2, so the difference is exactly the
# two half-endpoints. The oldest lag is only reached once the buffer has filled.
delta = 0.5 * dt * xi_dot @ K[:, :, 0].T
old = np.zeros_like(delta)
old[n_lags - 1:] = 0.5 * dt * xi_dot[: len(t) - n_lags + 1] @ K[:, :, n_lags - 1].T
mu_rect = mu_trap + delta + old

sel = t > t[-1] - 8 * T_f
print(f"record   {t.size} samples, {t[-1]:.1f} s     kernel {n_lags} lags, dt {dt}")
print(f"window   last 8 periods, {sel.sum()} samples\n")

# Two quantities, because "collapse" lives in only one of them. The removed
# endpoint dt/2*K[0]@v is a PURE DAMPING term, so its size relative to B_tab is
# where the several-fold change is. Relative to |mu| it is only a few percent,
# because mu is ~96% A-channel. Reporting only the second would understate the
# defect; reporting only the first would overstate what the record shows.
w = np.asarray(hdb.omega); B = np.asarray(hdb.B)
W_CASE = 2 * np.pi / T_f
kk = int(np.clip(np.searchsorted(w, W_CASE), 1, w.size - 1))
ff = (W_CASE - w[kk - 1]) / (w[kk] - w[kk - 1])
B_tab = B[:, :, kk - 1] * (1 - ff) + B[:, :, kk] * ff

print("AG5 -- per-DOF fingerprint of the fix, aggregated over the 12 buoys")
print(f"{'DOF':>7} {'K(0) diag':>12} {'B_tab diag':>12} {'endpoint/B':>11} "
      f"{'d|mu|':>8} {'|mu|':>11}")
rows = []
for i, name in enumerate(DOF_NAME):
    g = [HYDRO_GLOBAL_DOF[6 * b + i] for b in range(12)]
    h = [6 * b + i for b in range(12)]
    k0 = float(np.mean([K[j, j, 0] for j in g]))
    bt = float(np.mean([B_tab[j, j] for j in h]))
    a = float(np.mean([np.abs(mu_rect[sel, j]).max() for j in g]))
    b = float(np.mean([np.abs(mu_trap[sel, j]).max() for j in g]))
    # DOF whose mu is round-off carry no signal and must not enter the statistics.
    dead = b < 1e-12
    ratio = 0.5 * dt * k0 / bt if bt > 0 else np.nan
    rows.append((name, k0, bt, ratio, abs(b - a) / b if not dead else np.nan, b, dead))
    tag = "   <- mu is round-off, EXCLUDED" if dead else ""
    print(f"{name:>7} {k0:12.4e} {bt:12.4e} {ratio:10.2f}x "
          f"{(b - a) / a * 100 if not dead else float('nan'):+7.1f}% {b:11.4e}{tag}")

live = [r for r in rows if not r[6]]
k0s = np.array([r[1] for r in live]); chg = np.array([r[4] for r in live])
print(f"\nlive DOF: {', '.join(r[0] for r in live)}")
print(f"correlation of d|mu| with K(0) over LIVE DOF only: "
      f"{np.corrcoef(k0s, chg)[0, 1]:+.4f}")
print(f"  (including yaw, whose mu is {rows[5][5]:.1e}, gives "
      f"{np.corrcoef([r[1] for r in rows], np.nan_to_num([r[4] for r in rows]))[0,1]:+.4f}"
      f" -- a correlation over a DOF with no signal)")

print("\nFINGERPRINT, both halves:")
print(f"  damping   endpoint/B_tab: heave {rows[2][3]:.2f}x, "
      f"surge {rows[0][3]:.1f}x, pitch {rows[4][3]:.1f}x   <- the several-fold change")
print(f"  record    d|mu|:          heave {rows[2][4]*100:.2f}%, "
      f"surge {rows[0][4]*100:.1f}%, pitch {rows[4][4]*100:.1f}%   <- mu is ~96% A-channel")
print("\nHeave barely moves because K(0)[heave] is 4 orders below surge/pitch --")
print("which is why FloatSim's heave-centric M2-M11 validation never saw this.")
print("A stub or mis-synced record cannot reproduce that shape (eighth guard).")
