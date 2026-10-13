"""The configuration-driven run path (R1 / FL1).

`floatfea run <config.yaml>` and `floatfea export <config.yaml>`. Nothing in here
computes a member force or an allowable: it declares what a run IS, validates it, and
calls the same `floatfea` code the measure scripts call.
"""

from __future__ import annotations

__all__ = ["config", "pipeline"]
