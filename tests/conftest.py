"""Shared pytest configuration.

Two things are enforced here rather than left to convention.

**Hypothesis determinism.** The profile below is registered and activated so
property tests explore the same examples on every run. The default
(``derandomize=False``) draws a fresh seed per run, which makes two runs
incomparable — and G1.5 asks for bit-identical results across two provisionings.
A randomised strategy cannot deliver that, and the resulting failure would look
like an export-branch defect rather than a harness artifact. The `.hypothesis`
example database is also gitignored, so a fresh checkout would not otherwise
reproduce a corner that a developer's working copy had found and stored.

**Ladder ordering.** ``docs/verification/README.md`` orders the verification
ladder by dependency: a failure at rung *n* makes every rung above it
uninterpretable. Tests are collected in rung order so a red rung 1 is read
before a red rung 5, and so nobody investigates a rung 5 discrepancy while a
rung 1 test is failing.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from hypothesis import HealthCheck, Verbosity, settings

settings.register_profile(
    "floatfea",
    derandomize=True,
    print_blob=True,
    deadline=None,  # numerics: a slow example is not a failing example
    suppress_health_check=[HealthCheck.too_slow],
)
settings.register_profile(
    "debug",
    parent=settings.get_profile("floatfea"),
    verbosity=Verbosity.verbose,
)
settings.load_profile("floatfea")

_RUNG_ROOT = "verification"


def _rung_of(path: Path) -> int:
    """Return the ladder rung a test file belongs to, or 0 if it is not on the ladder."""
    for part in path.parts:
        if part.startswith("rung") and part[4:].isdigit():
            return int(part[4:])
    return 0


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Apply the rung marker from the directory, then order collection by rung.

    The marker is derived from location rather than written by hand so that
    adding a test to a rung is a matter of putting the file in the right
    directory — one less step that can be forgotten, and one less place for the
    marker and the directory to disagree.
    """
    for item in items:
        rung = _rung_of(Path(str(item.fspath)))
        if rung:
            item.add_marker(getattr(pytest.mark, f"rung{rung}"))
    # Unit tests first (they are the cheapest signal), then the ladder in order,
    # then regression.
    items.sort(key=lambda it: (_rung_of(Path(str(it.fspath))) or -1))
