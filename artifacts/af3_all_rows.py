"""AF3, all 72 rows -- rotational rows included, via Capytaine's own DOF fields.

The generalized force for DOF j is

    F_j = -sum_p  p_p (n_p . d_j,p) A_p

with d_j the DOF's displacement field. Using CAPYTAINE'S OWN field avoids
assuming a rotation centre: the rotational DOF here are built about
`rotation_center`, which is NOT the body reference point conventions.md makes the
moment reference, so reconstructing the arm by hand would assume exactly what
conventions.md forbids assuming.

Reference is the FULL 72x72 from the SAME solve at the exact case frequency -- no
interpolation anywhere, which is what frames.assert_reference_supports demands at
round-off tolerance.

RAW OUTPUT ONLY.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from floatfea.io.frames import (
    Reference,
    assert_reference_supports,
    live_dof,
)

HERE = Path(__file__).resolve().parent
p = np.load(HERE/"panels_w2.npz", allow_pickle=True)
d = np.load(HERE/"dof_fields.npz", allow_pickle=True)
W = float(p["omega"][0]); rad = p["radiation"][0]
area = p["area"]; normal = p["normal"]
names = [str(x) for x in p["dof_names"]]
assert [str(x) for x in d["names"]] == names, "DOF ordering differs between files"
D = d["dofs"]                                   # (72, P, 3)
A_full = p["A_full"]; B_full = p["B_full"]      # (72, 72) same solve, exact omega

ref = Reference(B_full, omega=W, interpolated=False, source="same BEM solve, exact omega")
assert_reference_supports(ref, tolerance=1e-12, what="AF3 all-rows")

# n . d_j  per panel, weighted by area: the generalized-force weights.
w_jp = np.einsum("pc,jpc->jp", normal, D) * area          # (72, P)
R = -np.einsum("jp,kp->jk", w_jp, rad)                    # (72, 72) influenced j, radiating k
T = W**2 * A_full + 1j * W * B_full

DOF = ("surge", "sway", "heave", "roll", "pitch", "yaw")
print(f"omega {W:.6f}   panels {area.size}   reference: {ref!r}")
print(f"\nAF3 -- ALL 72 ROWS")
print(f"  ||R-T||_F / ||T||_F        {np.linalg.norm(R-T)/np.linalg.norm(T):.3e}")
print(f"  ||R||_F / ||T||_F          {np.linalg.norm(R)/np.linalg.norm(T):.9f}")

tr = [6*b+c for b in range(12) for c in range(3)]
ro = [6*b+c for b in range(12) for c in (3, 4, 5)]
for label, rows in (("translational (was covered)", tr), ("ROTATIONAL (was not)", ro)):
    sub_r, sub_t = R[np.ix_(rows, range(72))], T[np.ix_(rows, range(72))]
    print(f"  {label:28s} {np.linalg.norm(sub_r-sub_t)/np.linalg.norm(sub_t):.3e}")

print(f"\n  per influenced DOF, aggregated over the 12 bodies")
print(f"  {'DOF':>7} {'||T||_F':>12} {'||R-T||/||T||':>15} {'worst entry':>13}")
# AI4: the dead-DOF exclusion applies EVERYWHERE a norm is formed, including
# here. Yaw's ||T|| is 1.4e-14 -- a ratio of two round-off quantities looks like a
# pass and is not one, which is precisely the failure live_dof exists to prevent.
per_dof_ref = np.array([np.linalg.norm(T[[6*b+c for b in range(12)]]) for c in range(6)])
alive = live_dof(per_dof_ref)
for c, nm in enumerate(DOF):
    rows = [6*b+c for b in range(12)]
    sr, st = R[rows], T[rows]
    if not alive[c]:
        print(f"  {nm:>7} {np.linalg.norm(st):12.4e} {'EXCLUDED':>15} "
              f"{'dead DOF':>13}   <- round-off / round-off is not a pass")
        continue
    e = np.abs(sr-st)/np.abs(st)
    print(f"  {nm:>7} {np.linalg.norm(st):12.4e} "
          f"{np.linalg.norm(sr-st)/np.linalg.norm(st):15.3e} "
          f"{np.max(e[np.abs(st) > np.abs(T).max()*1e-12]):13.3e}")
print(f"\n  live DOF {[DOF[c] for c in range(6) if alive[c]]}")
