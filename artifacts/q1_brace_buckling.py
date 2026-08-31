"""Q1 -- P/P_E for the worst brace. CORRECTED for sigma_allow (AP1/AP2).

Decision rule (locked): P/P_E < 0.1 -> deferral defensible; > 0.2 -> include;
between -> UNDECIDED pending F3's real sections, not a split difference.

CORRECTION, 2026-08-30
----------------------
The first run used `f_y / 1.5 = 236.7 MPa`. The PROJECT BASIS is `0.6 f_y =
213.0 MPa` (docs/milestones/F1.md sec. 8) -- 11.11% lower, exactly (1/1.5)/0.6.
Every P/P_E in the first run was 11.11% high, and the lambda threshold for
P/P_E = 0.2 was quoted as 41.9 when it is 44.1.

A lower threshold-lambda is CONSERVATIVE for the include decision; a HIGHER one is
not, because it widens the range of sections that qualify for deferral. So the
"not reachable by a real section" claim is re-checked here rather than assumed to
carry.

sigma_allow and kappa now both come from `floatfea/sections.py`. They had each
appeared with two values in two documents -- which is the failure the kappa pin
was built to prevent, arriving one constant over.

THE INVARIANCE IS THE RESULT
----------------------------
For a strength-sized member,

    P/P_E = (P/A) (K L / r)^2 / (pi^2 E) = sigma_allow * lambda^2 / (pi^2 E)

The axial load cancels against the area it sized, so **P/P_E does not depend on
the design moment at all.** The 150-300 MN.m uncertainty -- which dominates every
other structural number in this project -- cannot reach this decision.

What the moment DOES set is which proportions are buildable: A scales with P, so
D/t at a given D scales as D^2/A. That is why the buildability boundary below is
swept per moment while the ratio itself is not.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from floatfea.sections import (  # noqa: E402
    E_STEEL,
    SIGMA_ALLOW_S355,
    chs_class_limits,
    tube_area,
    tube_radius_of_gyration,
)

DEPTH = 10.0
ARM = 50.0
THETA = math.radians(45.0)
K = 1.0
L = DEPTH / math.sin(THETA)
SIG = SIGMA_ALLOW_S355
C1, C2, C3 = chs_class_limits()


def ratio_from_lambda(lam: float) -> float:
    return SIG * lam**2 / (math.pi**2 * E_STEEL)


def lambda_at(ratio: float) -> float:
    return math.sqrt(ratio * math.pi**2 * E_STEEL / SIG)


print(f"L = {L:.2f} m at {math.degrees(THETA):.0f} deg, K = {K}")
print(f"sigma_allow = {SIG/1e6:.1f} MPa  (0.6 f_y, the PROJECT basis)")
print(f"EN 1993-1-1 CHS class limits, D/t: {C1:.0f} / {C2:.0f} / {C3:.0f}\n")
print(f"lambda at P/P_E = 0.1: {lambda_at(0.1):.1f}    at 0.2: {lambda_at(0.2):.1f}")
print(f"  (first run quoted 29.6 / 41.9 on the wrong sigma_allow)\n")

print("Ratio for a fixed section -- INDEPENDENT of the design moment:")
print(f"{'D (m)':>7} {'r (m)':>7} {'lambda':>7} {'P/P_E':>7}  verdict")
for D in (0.6, 0.8, 0.9, 1.0, 1.2, 1.5):
    # t only enters r weakly; use the class-3 boundary wall so r is realistic.
    t = D / C3
    r = tube_radius_of_gyration(D, t)
    lam = K * L / r
    rr = ratio_from_lambda(lam)
    verdict = "INCLUDE" if rr > 0.2 else "defer-ok" if rr < 0.1 else "UNDECIDED"
    print(f"{D:7.2f} {r:7.4f} {lam:7.1f} {rr:7.3f}  {verdict}")

print("\nBUILDABILITY BOUNDARY -- the STOCKIEST section that is still class 3,")
print("which is the best available case for deferral. A scales with the load, so")
print("this boundary moves with the design moment even though the ratio does not:")
print(f"\n{'M (MN.m)':>9} {'P (MN)':>8} {'A (m^2)':>9} {'D_max (m)':>10} "
      f"{'t (mm)':>7} {'lambda':>7} {'P/P_E':>7}  verdict")
worst = 1e9
for M in (150e6, 200e6, 250e6, 300e6):
    P = (M / ARM) / math.sin(THETA)
    A_req = P / SIG
    # Largest D whose wall still satisfies D/t <= C3, at the required area.
    # t = D / C3, so A(D) is monotonic in D; solve A(D) = A_req.
    lo, hi = 0.05, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if tube_area(mid, mid / C3) < A_req:
            lo = mid
        else:
            hi = mid
    D = 0.5 * (lo + hi)
    t = D / C3
    r = tube_radius_of_gyration(D, t)
    lam = K * L / r
    rr = ratio_from_lambda(lam)
    worst = min(worst, rr)
    verdict = "INCLUDE" if rr > 0.2 else "defer-ok" if rr < 0.1 else "UNDECIDED"
    print(f"{M/1e6:9.0f} {P/1e6:8.2f} {A_req:9.4f} {D:10.3f} {t*1e3:7.1f} "
          f"{lam:7.1f} {rr:7.3f}  {verdict}")

print(f"\nworst (stockiest buildable, across 150-300 MN.m): P/P_E = {worst:.3f}")
print(f"margin over the 0.2 include threshold: {(worst/0.2 - 1)*100:+.0f}%")
print(f"amplification 1/(1 - P/P_E) at that point: {1/(1-worst):.2f}")
