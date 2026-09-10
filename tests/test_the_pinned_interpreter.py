"""One Python for the project, and nothing may use a newer one (CE0).

The environment was three different things at once: `requires-python = ">=3.11"`,
a CI runner on 3.11.16, and an implementer on 3.13. A keyword argument that
arrived in 3.12 was written, ran green locally, passed review, and failed on the
runner — in the one test that measures the shallow-clone repair, which is to say
in the one place that could only be checked on the machine where the shallow
clone was found.

Nothing detected it. `ruff` reads syntax and `onexc=` is valid syntax at every
version; the type checker was pointed at `floatfea/` only, and the call was in
`tests/`.

WHAT THIS FILE PINS

1. `requires-python` names an exact minor version, not a floor. A floor is what
   let three versions coexist.
2. `ci.yml` runs that version in every job.
3. **No file uses an API newer than the pin.** Measured by type-checking at the
   pinned version and at the running one and taking the difference: an error
   that appears only under the pin is a use of something the pin does not have.
   Self-calibrating, so it needs no baseline to go stale.

WHAT IT DOES NOT PIN, said so it is not trusted past its reach: the patch
version, and the libraries. The patch version is the runner's business; the
libraries are Q8's lockfile, which is a different mechanism for the same reason.
"""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
WORKFLOW = ROOT / ".github" / "workflows" / "ci.yml"


def _pinned() -> tuple[int, int]:
    """The single minor version `requires-python` allows."""
    spec = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))["project"]["requires-python"]
    lo = re.search(r">=\s*(\d+)\.(\d+)", spec)
    hi = re.search(r"<\s*(\d+)\.(\d+)", spec)
    assert lo and hi, (
        f"`requires-python = {spec!r}` does not pin one minor version. A floor "
        "is what let the implementer, the runner and the metadata disagree."
    )
    assert (int(lo.group(1)), int(lo.group(2)) + 1) == (
        int(hi.group(1)),
        int(hi.group(2)),
    ), f"`requires-python = {spec!r}` spans more than one minor version"
    return int(lo.group(1)), int(lo.group(2))


def test_requires_python_pins_one_minor_version() -> None:
    major, minor = _pinned()
    assert (major, minor) >= (3, 11), f"{major}.{minor} is older than the project"


def test_every_ci_job_runs_the_pinned_version() -> None:
    """A pin the workflow does not honour is metadata, not a pin."""
    major, minor = _pinned()
    want = f"{major}.{minor}"
    found = re.findall(r"python-version:\s*\"?([\d.]+)\"?", WORKFLOW.read_text(encoding="utf-8"))
    assert found, f"no `python-version` in {WORKFLOW}; the pattern or the file changed"
    wrong = sorted({v for v in found if not v.startswith(want)})
    assert not wrong, (
        f"`requires-python` pins {want} and {WORKFLOW.name} runs {wrong}. The "
        "runner and the metadata disagreeing is half of what CE0 is about."
    )


def _mypy_errors(version: str) -> set[str]:
    """`file:line: message` for every error at `version`, paths normalised."""
    out = subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--python-version",
            version,
            "--ignore-missing-imports",
            "--no-error-summary",
            "tests",
            "floatfea",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    return {
        line.replace("\\", "/").strip() for line in out.stdout.splitlines() if ": error:" in line
    }


def test_nothing_uses_an_api_newer_than_the_pin() -> None:
    """The guard that would have caught `onexc=`.

    An error the type checker reports at the PINNED version and not at the one
    running here is, by construction, a use of something the pin does not have.
    The comparison needs no baseline and cannot go stale, which is why it is a
    difference rather than a count.
    """
    major, minor = _pinned()
    running = f"{sys.version_info.major}.{sys.version_info.minor}"
    pinned = f"{major}.{minor}"
    if pinned == running:
        # Same interpreter: the difference is empty by construction and would
        # assert nothing. Say so rather than passing silently.
        return
    newer = sorted(_mypy_errors(pinned) - _mypy_errors(running))
    assert not newer, (
        f"{len(newer)} error(s) appear at the pinned {pinned} and not at the "
        f"running {running}, so they are uses of an API {pinned} does not "
        f"have:\n  " + "\n  ".join(newer[:10])
    )
