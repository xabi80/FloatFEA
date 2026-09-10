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
which is what `scripts/run_rung.sh` reads. A test cannot write another test's
report element, so there is nothing to forge.

Loaded by the rung script as `-p rung_no_xpass` with `scripts/` on the path. It
is deliberately NOT in the project's `addopts`: outside a ladder rung an
explicit `strict=False` is the author's decision to make.
"""

from __future__ import annotations

from typing import Any

import pytest


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
        report.longrepr = (
            f"{report.nodeid}: marked xfail and PASSED. A ladder rung fails on "
            "an unexpected pass whatever the marker's `strict` says -- "
            "CLAUDE.md forbids xfail for a green build, and a test that passes "
            "while declaring it will not is asserting the opposite of what it "
            "says."
        )
