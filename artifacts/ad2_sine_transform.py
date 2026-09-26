"""AD2 -- close the A channel by DIRECT MEASUREMENT, not by inference.

AA1 argued the A channel needed no test: a purely quadrature residual *is* the
statement that A is faithful. AD1 shows that decomposition rests on an invalid
bridge, so AA1 is retracted and A must be measured the same way B was.

The two halves of the Ogilvie pair:

    B(w) =        integral K(t) cos(w t) dt          <- already measured
    A(w) = A_inf - integral K(t) sin(w t) dt / w     <- this script

Same kernel, same grid, one line different. Needs NO simulation and NO record --
which is why it runs while the record regenerates.

RAW OUTPUT ONLY (docs/instrumentation.md). Ratios are derived in the write-up.

Index spaces: the kernel is 102-DOF GLOBAL, the hydro database is 72-DOF. That
mixture is the trap that already bit once (it put structural hub2 opposite a
hydro DOF and returned B_eff = 0, which read as spectacular confirmation). Every
cross-space index below goes through floatfea.io.frames.
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

from floatfea.io.frames import HYDRO_GLOBAL_DOF, N_DOF_HYDRO  # noqa: E402

W_CASE = 2.0 * np.pi / 3.141

hdb = pff._hdb("0215")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    setup = pff._build(0.215, 5.0, hdb)

K = np.asarray(setup.kernel.K)          # (102, 102, N_t) GLOBAL
tk = np.asarray(setup.kernel.t)
w = np.asarray(hdb.omega)
A_tab = np.asarray(hdb.A)               # (72, 72, n_w)
B_tab = np.asarray(hdb.B)
A_inf = np.asarray(hdb.A_inf)           # (72, 72)

g = np.asarray(HYDRO_GLOBAL_DOF)
Kh = K[np.ix_(g, g)]                    # (72, 72, N_t) -- hydro subset, safely

print(f"kernel lags            {tk.size}  (memory {tk[-1]:.1f} s, dt {tk[1] - tk[0]:.4f} s)")
print(f"kernel shape global    {K.shape}   -> hydro subset {Kh.shape}")
print(f"hydro omega grid       {w.size} points, {w[0]:.4f} .. {w[-1]:.4f} rad/s")
print(f"case frequency         {W_CASE:.4f} rad/s\n")


def transforms(omega: float) -> tuple[np.ndarray, np.ndarray]:
    """(A_eff, B_eff) at ``omega`` by trapezoid over the kernel's own grid."""
    c = np.cos(omega * tk)
    s = np.sin(omega * tk)
    B_eff = np.trapezoid(Kh * c, tk, axis=2)
    A_eff = A_inf - np.trapezoid(Kh * s, tk, axis=2) / omega
    return A_eff, B_eff


def interp_tab(omega: float) -> tuple[np.ndarray, np.ndarray]:
    k = int(np.clip(np.searchsorted(w, omega), 1, w.size - 1))
    f = (omega - w[k - 1]) / (w[k] - w[k - 1])
    return (A_tab[:, :, k - 1] * (1 - f) + A_tab[:, :, k] * f,
            B_tab[:, :, k - 1] * (1 - f) + B_tab[:, :, k] * f)


# --- at the case frequency -------------------------------------------------
Ae, Be = transforms(W_CASE)
At, Bt = interp_tab(W_CASE)

dA = Ae - At
dB = Be - Bt
Aexc = At - A_inf                       # the quantity mu actually multiplies

print("AD2 -- A channel at the case frequency, measured from the kernel")
print(f"  ||A_tab - A_inf||_F        {np.linalg.norm(Aexc):12.6e}   <- what mu uses")
print(f"  ||A_eff - A_tab||_F        {np.linalg.norm(dA):12.6e}")
print(f"  ratio dA / (A_tab-A_inf)   {np.linalg.norm(dA) / np.linalg.norm(Aexc):12.6f}")
print(f"  ||B_tab||_F                {np.linalg.norm(Bt):12.6e}")
print(f"  ||B_eff - B_tab||_F        {np.linalg.norm(dB):12.6e}")
print(f"  ratio dB / B_tab           {np.linalg.norm(dB) / np.linalg.norm(Bt):12.6f}\n")

print("  largest-|A_tab-A_inf| diagonal entries")
print(f"  {'hydro':>6} {'global':>7} {'A_tab-A_inf':>13} {'A_eff-A_inf':>13} {'ratio':>9}")
diag = np.argsort(-np.abs(np.diag(Aexc)))[:6]
for j in diag:
    num, den = Ae[j, j] - A_inf[j, j], Aexc[j, j]
    print(f"  {j:6d} {HYDRO_GLOBAL_DOF[j]:7d} {den:13.5e} {num:13.5e} "
          f"{num / den if den else np.nan:9.4f}")

# --- across the band -------------------------------------------------------
print("\n  frequency-resolved, Frobenius, over the tabulated grid")
print(f"  {'omega':>8} {'|dA|/|A-Ainf|':>14} {'|dB|/|B|':>10} {'|A-Ainf|_F':>12} {'|B|_F':>11}")
rows = []
for i, om in enumerate(w):
    if not 0.5 <= om <= 8.0:
        continue
    Aei, Bei = transforms(float(om))
    ex = A_tab[:, :, i] - A_inf
    ra = np.linalg.norm(Aei - A_tab[:, :, i]) / np.linalg.norm(ex)
    rb = np.linalg.norm(Bei - B_tab[:, :, i]) / np.linalg.norm(B_tab[:, :, i])
    rows.append((om, ra, rb))
    if i % 6 == 0:
        print(f"  {om:8.4f} {ra:14.4f} {rb:10.4f} "
              f"{np.linalg.norm(ex):12.4e} {np.linalg.norm(B_tab[:, :, i]):11.4e}")
ra = np.array([r[1] for r in rows])
rb = np.array([r[2] for r in rows])
print(f"\n  median over {len(rows)} in-band frequencies:  "
      f"dA/(A-Ainf) {np.median(ra):.4f}   dB/B {np.median(rb):.4f}")
print(f"  max:                            dA/(A-Ainf) {ra.max():.4f}   dB/B {rb.max():.4f}")
np.savez_compressed(Path(__file__).resolve().parent / "ad2_transforms.npz",
                    omega=np.array([r[0] for r in rows]), ra=ra, rb=rb)
print("  wrote ad2_transforms.npz")
