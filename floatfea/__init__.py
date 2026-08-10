"""FloatFEA -- structural analysis of the floating platform from FloatSim loads.

Engineering analysis software. A wrong answer that looks right is worse than a
crash; most of the structure here exists to make wrongness loud.

Internally SI throughout: metres, kilograms, seconds, newtons, radians. Unit
conversion happens only at the I/O boundary -- a conversion inside the numerics
is a defect.

Every numerical tolerance lives in :mod:`floatfea.tolerances`.
Conventions are authoritative in ``docs/conventions.md``.
"""

from __future__ import annotations

__version__ = "0.1.0"
