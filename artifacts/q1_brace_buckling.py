"""Q1 -- P/P_E for the worst brace, to settle geometric stiffness in or out of F2.

Decision rule (locked): P/P_E < 0.1 -> deferral defensible (amplification < 11%);
> 0.2 -> include (> 25%); between -> UNDECIDED pending F3's real sections, not a
split difference.

INPUT PROVENANCE, stated because the answer is conditional on it
---------------------------------------------------------------
From `docs/milestones/F1.md` §8, all PLACEHOLDER:

  design moment at truss centre   150-300 MN.m   (antisymmetric differential,
                                                  dynamic; statics cannot pin it)
  arm length                      50 m
  truss depth                     10 m
  material                        S355, E = 210 GPa, f_y = 355 MPa

NOT in the placeholder set: **brace sections**. The F1 sizing stops at chords
(0.094 m^2 each at 200 MN.m). So a brace has to be assumed, and the assumption is
swept rather than picked.

The braces are sized by STRENGTH here, then checked against Euler. Sizing them for
buckling instead would make P/P_E whatever it was designed to be -- circular. The
question is: if braces are proportioned for strength, how close to Euler do they
land?

Closed form used, so the sweep is checkable by hand. For a strength-sized member
with axial stress sigma and slenderness lambda = L/r:

    P/P_E = P / (pi^2 E I / (K L)^2)
          = (P/A) * (K L / r)^2 / (pi^2 E)
          = sigma * lambda_eff^2 / (pi^2 E)

so P/P_E depends on the section only through its slenderness -- the axial load
cancels against the area it sized. Thin tube: r = D / (2*sqrt(2)).
"""
from __future__ import annotations

import math

E = 210e9
FY = 355e6
UTIL = 1.5           # strength sizing: allowable = f_y / UTIL
DEPTH = 10.0
ARM = 50.0
THETA = math.radians(45.0)
K = 1.0              # pinned-pinned; a braced truss diagonal is close to this
L = DEPTH / math.sin(THETA)

sigma_allow = FY / UTIL
print(f"brace length L = {L:.2f} m at {math.degrees(THETA):.0f} deg, K = {K}")
print(f"strength sizing at f_y/{UTIL} = {sigma_allow/1e6:.0f} MPa\n")

print("P/P_E = sigma * lambda^2 / (pi^2 E), lambda = K L / r, r = D/(2 sqrt2)")
print(f"  thresholds: P/P_E = 0.1 at lambda = "
      f"{math.sqrt(0.1*math.pi**2*E/sigma_allow):.1f}, "
      f"0.2 at lambda = {math.sqrt(0.2*math.pi**2*E/sigma_allow):.1f}\n")

print(f"{'M (MN.m)':>9} {'V (MN)':>8} {'P (MN)':>8} {'D (m)':>7} {'t (mm)':>7} "
      f"{'D/t':>6} {'lambda':>7} {'P/P_E':>7}  verdict")
rows = []
for M in (150e6, 200e6, 300e6):
    V = M / ARM                      # equivalent tip shear on one arm
    P = V / math.sin(THETA)          # diagonal force
    A = P / sigma_allow              # strength-sized area
    for D in (0.6, 0.8, 1.0, 1.2, 1.5):
        t = A / (math.pi * D)        # thin tube
        r = D / (2.0 * math.sqrt(2.0))
        lam = K * L / r
        ratio = sigma_allow * lam**2 / (math.pi**2 * E)
        verdict = ("INCLUDE" if ratio > 0.2 else
                   "defer-ok" if ratio < 0.1 else "UNDECIDED")
        rows.append((M, D, ratio, t, verdict))
        print(f"{M/1e6:9.0f} {V/1e6:8.2f} {P/1e6:8.2f} {D:7.2f} {t*1e3:7.1f} "
              f"{D/t:6.0f} {lam:7.1f} {ratio:7.3f}  {verdict}")

print("\nNote P/P_E is INDEPENDENT of the design moment: sigma is fixed by the")
print("strength sizing, so a larger load buys a larger area and lambda is unchanged.")
print("The ratio is set by the brace's PROPORTIONS (D and L), not by the load.\n")

# D/t is the check that says whether a slender brace is even buildable: a very
# thin tube fails locally long before Euler, so those rows are not real options.
# EN 1993-1-1 Table 5.2, CHS in compression: class limits are D/t <= 50 eps^2
# (class 1), 70 eps^2 (class 2), 90 eps^2 (class 3), with eps^2 = 235/f_y.
# For S355, eps^2 = 0.662, so the limits are 33 / 46 / 60. Above class 3 the
# section is slender, local buckling governs, and the Euler number is not the
# binding one -- those rows are not real options regardless of their P/P_E.
EPS2 = 235e6 / FY
C1, C2, C3 = 50 * EPS2, 70 * EPS2, 90 * EPS2
print(f"D/t screening -- EN 1993-1-1 Table 5.2, CHS compression, S355 "
      f"(eps^2 = {EPS2:.3f}):")
print(f"  class 1 <= {C1:.0f}, class 2 <= {C2:.0f}, class 3 <= {C3:.0f}; "
      f"beyond class 3 the section is slender")
for M, D, ratio, t, verdict in rows:
    if M != 200e6:
        continue
    dt = D / t
    cls = ("class 1" if dt <= C1 else "class 2" if dt <= C2 else
           "class 3" if dt <= C3 else "SLENDER -- not a real option")
    print(f"  D = {D:.2f} m   D/t = {dt:5.0f}   {cls:32s} P/P_E = {ratio:.3f}")
