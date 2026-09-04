"""No numeric tolerance literals in assertions (BC2, enforcing AW2 mechanically).

`CLAUDE.md` § Tolerances says every numerical tolerance lives in
`floatfea/tolerances.py` -- no local literals. That was a rule, and it was broken
twice: `SUBDIVISION_INVARIANCE` shipped as an undeclared `rtol=1e-10` (AW2), and
two commits after AW2 closed, `rel=1e-6` and `> 1e4` appeared in new assertions
(R13). A rule the same hand keeps breaking is a rule that needs to be a test.

What this scans
---------------
Every `assert` statement under `tests/`, for a numeric literal that is being used
as a comparison threshold. A line is acceptable if it references a name imported
from `floatfea.tolerances`, or if it carries an explicit `# not-a-tolerance:`
annotation naming why.

The annotation is deliberately noisy rather than a quiet allow-list: an exemption
has to appear in the diff where a reviewer sees it, next to the line it exempts.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

TESTS = Path(__file__).resolve().parent
# A literal in a TOLERANCE POSITION -- not every number on an assert line.
#
# `pytest.approx(0.486, abs=5e-3)` contains two literals with different roles:
# `0.486` is a measured REFERENCE VALUE, which belongs in the test beside what it
# describes, and `5e-3` is a COMPARISON EPSILON, which `CLAUDE.md` names
# explicitly as a tolerance. Only the second is in scope. Flagging both would make
# the check unusable and it would be turned off, which is worse than not having it.
# A tolerance is a NON-TRIVIAL threshold on a discrepancy. Excluded by
# construction, because nothing about them can be widened to hide an error:
#   * comparisons against 0      -- 'is this non-zero?', a structural check
#   * comparisons against integers -- 'are there enough panels/bodies?', a count
# In a keyword position (rel=, abs=, atol=, rtol=) any literal counts, because
# there the number IS the tolerance whatever its value.
_KWNUM = r"\d+\.?\d*(?:[eE][-+]?\d+)?"
_CMPNUM = r"(?=\d*\.\d|\d+[eE])(?!0+\.?0*[,)\s])" + _KWNUM
_LITERAL = re.compile(
    r"(?:rel|abs|atol|rtol)\s*=\s*" + _KWNUM
    + r"|[<>]=?\s*" + _CMPNUM
)
_EXEMPT = re.compile(r"#\s*not-a-tolerance:")
_TOL_NAMES: set[str] = set()


def _tolerance_names() -> set[str]:
    global _TOL_NAMES
    if not _TOL_NAMES:
        from floatfea import tolerances

        _TOL_NAMES = {n for n in dir(tolerances) if n.isupper()}
    return _TOL_NAMES


def _offending_lines(path: Path) -> list[tuple[int, str]]:
    """Assertion lines carrying a bare numeric threshold."""
    out: list[tuple[int, str]] = []
    names = _tolerance_names()
    text = path.read_text(encoding="utf-8").splitlines()
    in_assert = False
    for i, line in enumerate(text, 1):
        stripped = line.strip()
        if stripped.startswith("assert ") or stripped.startswith("assert("):
            in_assert = True
        if not in_assert:
            continue
        if _LITERAL.search(line) and not _EXEMPT.search(line):
            if not any(n in line for n in names):
                out.append((i, stripped))
        # An assertion ends at the first line that is not obviously a continuation.
        if not line.rstrip().endswith((",", "(", "\\", "and", "or")):
            in_assert = False
    return out


def _test_files() -> list[Path]:
    return sorted(p for p in TESTS.rglob("test_*.py") if p.name != Path(__file__).name)


def test_there_are_test_files_to_scan() -> None:
    """Meta-test: an empty glob would make this pass while checking nothing."""
    files = _test_files()
    assert len(files) > 5, f"only {len(files)} test files found; the scan is vacuous"


def test_the_scanner_detects_a_known_violation() -> None:
    """Negative control, on the exact shape R13 found.

    Without this the scan could stop matching -- a regex that silently matches
    nothing reads identical to a clean repository.
    """
    import tempfile

    sample = (
        "def test_x():\n"
        "    assert cond_a == pytest.approx(cond_b, rel=1e-6), (\n"
        '        "message"\n'
        "    )\n"
        "    assert spread > 1e4\n"
    )
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "test_sample.py"
        p.write_text(sample, encoding="utf-8")
        found = _offending_lines(p)
    assert len(found) == 2, f"scanner found {len(found)} of 2 planted violations: {found}"


def test_the_annotation_exempts_a_line() -> None:
    """And the exemption must actually work, or it is not an escape hatch."""
    import tempfile

    sample = (
        "def test_x():\n"
        "    assert spread > 1e4  # not-a-tolerance: asserts the SPREAD is large\n"
    )
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "test_sample.py"
        p.write_text(sample, encoding="utf-8")
        assert _offending_lines(p) == []


@pytest.mark.parametrize("path", _test_files(), ids=lambda p: p.name)
def test_no_bare_tolerance_literals_in_assertions(path: Path) -> None:
    bad = _offending_lines(path)
    assert not bad, (
        f"{path.name} asserts against bare numeric literals:\n"
        + "\n".join(f"  line {n}: {s[:100]}" for n, s in bad)
        + "\n\nMove the value to floatfea/tolerances.py with a counter-case, or "
        "annotate the line `# not-a-tolerance: <why>` if it is not a threshold."
    )
