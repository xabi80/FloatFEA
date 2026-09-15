"""AF3 -- G1.6 radiation: does integrating the panel field reproduce the loads?

Under the AF3 design (AH2) the quadrature is common-mode, so this measures PANEL
RECONSTRUCTION ALONE and the target is round-off.

The comparison is against the coefficients the KERNEL WAS BUILT FROM (hdb.A,
hdb.B). For a radiation problem with unit motion in DOF k, e^{-iwt}:

    F_j = w^2 A_jk + i w B_jk

integrating the per-panel radiation pressure over body j's panels.

SCOPE LIMIT, stated: integrate_panel_pressure returns a 3-component FORCE
resultant only. The 36 translational rows (12 buoys x 3) are checked here; the 36
rotational rows need moment arms the function does not provide, and are NOT
covered. Reporting this as 'G1.6 radiation passes' without that qualifier would
be a gate covering half its rows.

RAW OUTPUT ONLY.
"""
from __future__ import annotations
import sys, warnings
from pathlib import Path
import numpy as np
_H = Path(r"C:\Users\xlama\OneDrive\Documents\buoy\HSP_code")
sys.path.insert(0, str(_H/"studies"/"platform-12buoy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
warnings.simplefilter("ignore")
import platform_fin_fan as pff
from floatsim.io.flr_panels import PanelGeometry, integrate_panel_pressure

HERE = Path(__file__).resolve().parent
p = np.load(HERE/"panels_w2.npz", allow_pickle=True)
W = float(p["omega"][0]); rad = p["radiation"][0]; owner = p["owner"]
geom = PanelGeometry(centroid=p["centroid"], area=p["area"], normal=p["normal"])
names = [str(x) for x in p["dof_names"]]

hdb = pff._hdb("0215")
w = np.asarray(hdb.omega); A = np.asarray(hdb.A); B = np.asarray(hdb.B)
k = int(np.clip(np.searchsorted(w, W), 1, w.size-1)); f = (W-w[k-1])/(w[k]-w[k-1])
At = A[:,:,k-1]*(1-f)+A[:,:,k]*f; Bt = B[:,:,k-1]*(1-f)+B[:,:,k]*f
print(f"omega {W:.6f}   grid neighbours {w[k-1]:.6f} / {w[k]:.6f}   frac {f:.4f}")
print(f"panels {geom.n_panels}   radiating DOF {len(names)}\n")

# Per body, per radiating DOF: integrate that body's panels only.
idx = [np.flatnonzero(owner == b) for b in range(12)]
T = np.zeros((36, 72), dtype=np.complex128)   # translational rows only
R = np.zeros((36, 72), dtype=np.complex128)
for kk in range(72):
    for b in range(12):
        sub = PanelGeometry(centroid=geom.centroid[idx[b]], area=geom.area[idx[b]],
                            normal=geom.normal[idx[b]])
        F = integrate_panel_pressure(rad[kk][idx[b]], sub)
        for c in range(3):
            R[3*b+c, kk] = F[c]
            j = 6*b + c
            T[3*b+c, kk] = W**2 * At[j, kk] + 1j*W*Bt[j, kk]

num = np.linalg.norm(R-T); den = np.linalg.norm(T)
print("AF3 -- panel reconstruction against the coefficients the kernel was built from")
print(f"  translational rows only: 36 of 72   (rotational rows NOT covered)")
print(f"  ||R-T||_F / ||T||_F        {num/den:.6f}")
print(f"  ||R||_F / ||T||_F          {np.linalg.norm(R)/den:.6f}")
gl = np.vdot(T.ravel(), R.ravel())/np.vdot(T.ravel(), T.ravel())
print(f"  single global factor       {abs(gl):.6f} * exp({np.degrees(np.angle(gl)):+.3f} deg)")
print(f"  residual after removing it {np.linalg.norm(R-gl*T)/den:.6f}\n")

print("  largest-|T| entries")
print(f"  {'row':>5} {'dof_k':>16} {'|T|':>12} {'|R|':>12} {'|R|/|T|':>9} {'arg(R/T)':>10}")
flat = np.argsort(-np.abs(T).ravel())[:8]
for q in flat:
    r_, c_ = divmod(q, 72)
    print(f"  {r_:5d} {names[c_]:>16} {abs(T[r_,c_]):12.4e} {abs(R[r_,c_]):12.4e} "
          f"{abs(R[r_,c_])/abs(T[r_,c_]):9.4f} {np.degrees(np.angle(R[r_,c_]/T[r_,c_])):+9.2f}")

# ---------------------------------------------------------------------------
# The 5.9e-4 above is NOT panel error. T is interpolated between grid points
# 1.930166 and 2.074677 where B varies ~60%, while R was solved EXACTLY at omega.
# Comparing against the SAME SOLVE's own diagonals removes the interpolation and
# leaves only the reconstruction -- which is what AF3 asks for.
# ---------------------------------------------------------------------------
Ad = p["A_diag"]; Bd = p["B_diag"]
rows, ref, got = [], [], []
for b in range(12):
    for c in range(3):
        kdof = 6*b + c
        ref.append(W**2 * Ad[kdof] + 1j*W*Bd[kdof])
        got.append(R[3*b+c, kdof])
        rows.append(names[kdof])
ref = np.asarray(ref); got = np.asarray(got)
num2 = np.linalg.norm(got-ref); den2 = np.linalg.norm(ref)
print("\nSAME-SOLVE diagonals (no frequency interpolation anywhere):")
print(f"  ||R-T||_F / ||T||_F        {num2/den2:.3e}")
print(f"  ||R||_F / ||T||_F          {np.linalg.norm(got)/den2:.9f}")
print(f"  worst single entry         {np.max(np.abs(got-ref)/np.abs(ref)):.3e}  "
      f"({rows[int(np.argmax(np.abs(got-ref)/np.abs(ref)))]})")
import math
print(f"  interpolated comparison    {num/den:.3e}   -> "
      f"{math.log10((num/den)/(num2/den2)):.0f} ORDERS larger, and it is MY interpolation")
