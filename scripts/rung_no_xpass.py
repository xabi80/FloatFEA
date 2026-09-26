"""A ladder rung fails on an unexpected pass, whatever the marker says.

`CLAUDE.md` names `xfail` in the same sentence as `skip`: neither may be used to
get a green build. `xfail_strict = true` in `pyproject.toml` states that for the
project, and a marker written `@pytest.mark.xfail(strict=False)` overrides it
per test -- so a rung whose only test is marked that way and then PASSES exits
zero, and pytest's junit report records a plain passing case. There is no
structured field that distinguishes it.

Every earlier attempt read the terminal output instead, and each was defeated by
text some other part of the process controls: an `atexit` hook printing after
the summary, `-ra`'s short summary carrying an xfail `reason=` or a parametrize
id, a conftest `pytest_report_header`, a `pytest_terminal_summary`, a
`warnings.warn` from inside the test. There is no last position in that list,
and the rule that chased it reddened a clean rung whose test merely warned the
word.

This plugin turns the report itself. `wasxfail` is set by pytest on a report
that carried an xfail marker; a report that carries it and passes is an
unexpected pass, and here that is a failure -- recorded as one in the junit XML,
which is what `scripts/run_rung.sh` reads.

WHAT THAT DOES AND DOES NOT BUY, because the sentence that stood here said "a
test cannot write another test's report element, so there is nothing to forge"
and it is false. A TEST cannot; a `conftest.py` in the rung's own directory can,
through this very hook, in the opposite direction -- and `pytest_ignore_collect`
and `pytest_collection_modifyitems` do better than forge a report, by removing
the failing test before any report exists. What this plugin buys is that the
four TEXT channels are dead and that an unexpected pass has a structured
signal. What it cannot buy is protection from code that runs inside the same
session, and nothing in this position can. `scripts/run_rung.sh` states the
property and names the bound: review of `tests/**/conftest.py`, in the
supervisor's per-step diff list.

Loaded by the rung script as `-p rung_no_xpass` with `scripts/` on the path. It
is deliberately NOT in the project's `addopts`: outside a ladder rung an
explicit `strict=False` is the author's decision to make.
"""

from __future__ import annotations

import os
from typing import Any

import pytest

_SEEN: dict[str, set[str]] = {"ran": set(), "raised": set(), "skipped": set()}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Any, call: Any) -> Any:
    """Turn an unexpected pass into a failure BEFORE anything records it.

    A wrapper on `makereport`, not a listener on `logreport`: the junit plugin
    is one of the listeners, so mutating the report after it has been broadcast
    changes the terminal and leaves the XML saying `passed`. The XML is what
    the rung reads, so the change has to happen while the report is still being
    built.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.passed and hasattr(report, "wasxfail"):
        # `wasxfail` GOES TOO. The junit writer keys on it and records a
        # `<skipped>` element whatever the outcome says, so leaving it turned
        # an unexpected pass into a reported SKIP -- a true failure with the
        # wrong cause printed, which is its own kind of wrong answer.
        del report.wasxfail
        report.outcome = "failed"
        # AND INTO THE TALLY. This is a failure this plugin creates rather
        # than one the call raised, so the cross-check below would otherwise
        # see junit say `1 failed` against a tally of none and redden the rung
        # for a disagreement of its own making.
        _SEEN["raised"].add(report.nodeid)
        report.longrepr = (
            f"{report.nodeid}: marked xfail and PASSED. A ladder rung fails on "
            "an unexpected pass whatever the marker's `strict` says -- "
            "CLAUDE.md forbids xfail for a green build, and a test that passes "
            "while declaring it will not is asserting the opposite of what it "
            "says."
        )


# CI0: A SECOND RECORD OF THE SAME RUN.
#
# `scripts/run_rung.sh` reads pytest's junit XML. A `conftest.py` anywhere on
# the collection path can write that XML -- through `pytest_sessionfinish`, or
# by removing items before anything records them -- and the reviewer measured
# both, from `tests/conftest.py` and from a rung's own directory. No gate
# closes that; a gate reading a record cannot outrank code that writes it.
#
# What a second record buys is CONSISTENCY, not resistance (CJ0). The two
# records catch each other when one of them stops describing the run by
# accident -- a plugin that fails to load, a junit writer that changes what it
# records. It does not make forgery harder in any way worth claiming: a
# `pytest_runtest_call` wrapper with `trylast=True` calling
# `outcome.force_result(None)` defeats both at once, because this tally is
# taken inside the hook such a wrapper wraps.
#
# The boundary is in the plan: in-tree code is trusted under review, and the
# defence is the supervisor's per-step diff of every conftest and plugin path.


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item: Any) -> Any:
    """The tally is taken from the CALL, not from the report.

    Taking it from `pytest_runtest_logreport` measured the same object the
    attack rewrites: a conftest hookwrapper on `makereport` flips the report
    to `passed`, every listener sees the flipped one, and the two records
    agree because they are one record. The exception raised by the test body
    is upstream of every report, and a conftest that swallows it there has
    changed what the test DID rather than what was written about it.

    THE CLASSIFICATION MIRRORS JUNIT'S, because the comparison is against
    junit: a `Skipped` raised by `pytest.skip()` is a skip, a test carrying an
    `xfail` marker that raises is recorded by the junit writer as `<skipped>`
    whatever it raised, and everything else is a failure. Getting either wrong
    would redden clean rungs for a disagreement this file invented.
    """
    _SEEN["ran"].add(item.nodeid)
    outcome = yield
    info = getattr(outcome, "excinfo", None)
    if info is None:
        return
    kind = info[0]
    skipped = kind is not None and kind.__name__ == "Skipped"
    if skipped or item.get_closest_marker("xfail") is not None:
        _SEEN["skipped"].add(item.nodeid)
    else:
        _SEEN["raised"].add(item.nodeid)


def pytest_runtest_logreport(report: Any) -> None:
    """Setup and teardown are not `call`, and a rung can fail in either."""
    if report.when == "setup":
        _SEEN["ran"].add(report.nodeid)
        if report.failed:
            _SEEN["raised"].add(report.nodeid)
        elif report.skipped and not hasattr(report, "wasxfail"):
            _SEEN["skipped"].add(report.nodeid)
    elif report.when == "teardown" and report.failed:
        _SEEN["raised"].add(report.nodeid)


def pytest_sessionfinish(session: Any, exitstatus: int) -> None:
    path = os.environ.get("RUNG_TALLY")
    if not path:
        return
    collected = _SEEN["ran"] | _SEEN["raised"] | _SEEN["skipped"]
    failed = _SEEN["raised"]
    skipped = _SEEN["skipped"] - failed
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(f"{len(collected)} {len(failed)} {len(skipped)}" + chr(10))
