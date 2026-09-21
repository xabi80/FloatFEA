#!/usr/bin/env python
"""Refuse a commit that changes a value and leaves the old one in the tree (CX1).

    python scripts/precommit_stale.py              # the staged diff
    python scripts/precommit_stale.py A..B         # a committed range

WHY, IN THE REVIEWER'S WORDS. Five rounds running, most findings were
sentences written in the commit that repaired the same species elsewhere. The
fiftieth verdict's reading was that this is not a detection problem -- the
attention goes to the thing being fixed and the prose written AROUND the fix
inherits none of the discipline applied TO it -- and that the cheapest
mechanical help is not another pattern but this: **any commit changing a
figure class, a regex, a generator or a tolerance row greps the tree for the
old class name, the old number and the old row name before it is committed.**

That is BP0 with a command attached, and it is what this is.

WHAT IT EXTRACTS from the diff's minus side, and nothing else:

  numbers    a literal on a removed line in `floatfea/tolerances.py` or in a
             generated-figure row. R452 is this: `114` survived in the entry
             while the corpus went to 126, five lines above the figure.
  row names  a `_floor("name", ...)` or `rows.append(("name", ...)` that was
             removed or changed. A row renamed out from under a citation is
             the `{{fig:...}}` species one level down.
  classes    the class word of a `_floor(...)` whose class changed, reported
             wherever it survives on a line that also names the row. R451 is
             this: `derived rather than exact`, in the file whose sibling
             commit made the row `words`.

A SURVIVOR IS NOT AUTOMATICALLY A DEFECT and this does not pretend otherwise.
A withdrawal marker on the line -- `stood here`, `is withdrawn`, `(withdrawn)`
-- says the old value is quoted deliberately, which is this repository's own
convention for recording what a sentence used to say. Everything else is
reported and the commit is refused until the author has looked at each one.

MEASURED, AND THE FIRST FIGURE PUBLISHED HERE WAS WITHDRAWN (CY2, R460).
`12 numbers ... 5 survivors, 1 TRUE and 4 false` stood here and in the step
report, and no command at that commit produced it: the report's own spec
printed "no figure class, row name or measured number removed", and the
`1 TRUE` was a survivor that stopped surviving in the same commit that added
its marker -- a figure describing a tree that existed for the length of one
`git add`. The reviewer re-measured and classified every survivor:

    cmd  python scripts/precommit_stale.py afc5b05^..afc5b05
    out  11 numbers, 0 renamed rows, 0 changed classes; 14 survivors
    out  all 14 are an `F2.md` or `F2_figures.md` row holding a CANONICAL
         value against a local render -- ZERO true

That is the honest rate on the one round this has been run against: fourteen
reports, none of them a defect. It is the cost of a literal grep, and it is
why this refuses by ASKING rather than by deciding -- every line above took
one look, and the alternative is a tool nobody runs.

WIRED, AS OF CY2. `.claude/hooks/stale-before-commit.sh` runs this before any
`git commit`. It was wired to nothing when it was written, which is the
species it exists to catch, and the reviewer said so (R465).

WHAT IT CANNOT SEE, measured rather than assumed. A citation carrying no
number and no row name is invisible to it: R454's four sentences said "it
breached at MORE of the reviewer's clean frames than the ratio did", which
names neither the count nor the figure, and no grep over the minus side finds
them. `tests/test_precommit_stale.py` carries that as a recorded miss rather
than a passing control, because a checker whose own test suite only contains
its successes is the thing this repository keeps finding.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEARCHED = ("floatfea", "tests", "scripts", "docs/milestones", "docs/verification")
SKIP = ("docs/reports",)

# WHERE A STALE NUMBER CAN LIVE. A number is reported only in the files that
# carry measured prose: the tolerance entries, the generator, the plan and
# the ladder. Searching everywhere reported `42` in a comment about approx
# call sites and `56` in one about wave headings -- unrelated numbers that
# happen to match, twenty-two of them in one round, which is how a checker
# stops being run.
#
# THE COST, STATED: a measurement quoted in a test docstring outside these
# paths is not checked. A ROW NAME is still searched everywhere, because a
# renamed row leaves a dangling citation wherever it is cited.
MEASURED_PROSE = (
    "floatfea/tolerances.py",
    "scripts/regen_figures.py",
    "docs/milestones/",
    "docs/verification/",
)

_WITHDRAWN = re.compile(r"stood here|is withdrawn|\(withdrawn\)|WITHDRAWN|used to read", re.I)
_NUMBER = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?(?:[eE][-+]?\d+)?)(?![\w.])")
_FLOOR = re.compile(r'_floor\(\s*"([a-z0-9_]+)"\s*,\s*"(below|above|derived|words)"')
_ROW = re.compile(r'rows\.append\(\s*\(\s*"([a-z0-9_]+)"')
_FIGURE_ROW = re.compile(r"^\|\s*`([a-z0-9_]+)`\s*\|\s*(.+?)\s*\|$")

# A number small enough to be an index, a column, a year or a version is noise.
# The species this is for is a MEASUREMENT: 114 frames, 1.3750 units, 6 of 19.
_TOO_COMMON = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "100", "1000"}


def _run(*args: str) -> str:
    """`git ...`, decoded permissively.

    A diff carries whatever bytes the tree carries, and this repository's
    prose has em dashes written on a machine that was not always UTF-8. A
    strict decode raises inside subprocess's reader thread and returns None,
    which reads downstream as "the diff is empty" -- a checker that silently
    passes on an undecodable diff is the failure mode this one exists for.
    """
    out = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return out.stdout or ""


def diff_text(spec: str | None) -> str:
    return _run("diff", spec) if spec else _run("diff", "--cached")


def old_tokens(diff: str) -> dict[str, set[str]]:
    """`{kind: tokens}` taken from the diff's minus side."""
    numbers: set[str] = set()
    rows: set[str] = set()
    classes: set[tuple[str, str]] = set()
    plus = "\n".join(ln[1:] for ln in diff.splitlines() if ln.startswith("+"))
    # A COMMENT'S NUMBERS ARE TAKEN FROM TWO FILES ONLY. The first version
    # took them from every removed comment line anywhere, which reported 188
    # survivors for one round's diff -- almost all of them a number in an
    # unrelated file that happened to match. What CX1 names is a tolerance
    # row, a figure class, a regex and a generator; the prose that goes
    # stale beside a measurement lives in the entry or in the generator.
    measured = ("floatfea/tolerances.py", "scripts/regen_figures.py")
    where = ""
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            where = line[6:].strip()
            continue
        if not line.startswith("-") or line.startswith("---"):
            continue
        body = line[1:]
        for m in _FLOOR.finditer(body):
            rows.add(m.group(1))
            classes.add((m.group(1), m.group(2)))
        for m in _ROW.finditer(body):
            rows.add(m.group(1))
        m = _FIGURE_ROW.match(body.strip())
        if m:
            rows.add(m.group(1))
            numbers.update(_NUMBER.findall(m.group(2)))
        if where in measured and (body.lstrip().startswith("#") or "Final[" in body):
            numbers.update(_NUMBER.findall(body))
    # A token that the PLUS side also carries did not change.
    numbers = {n for n in numbers if n not in _TOO_COMMON and n not in _NUMBER.findall(plus)}
    # For a ROW that means the BARE NAME: a row whose value moved is
    # removed and re-added, and comparing the quoted form reported every
    # live `{{fig:...}}` citation of it as surviving a rename that never
    # happened -- 170 of the first version's 188.
    rows = {r for r in rows if r not in plus}
    classes = {(r, c) for r, c in classes if f'"{r}", "{c}"' not in plus}
    return {"numbers": numbers, "rows": rows, "classes": {f"{r}/{c}" for r, c in classes}}


def _files() -> list[Path]:
    got: list[Path] = []
    for where in SEARCHED:
        for p in (ROOT / where).rglob("*"):
            if p.suffix in (".py", ".md", ".txt") and "__pycache__" not in str(p):
                got.append(p)
    return got


def survivors(tokens: dict[str, set[str]]) -> list[str]:
    """Where an old token is still written, excluding withdrawal markers."""
    out: list[str] = []
    classes = {c.split("/")[0]: c.split("/")[1] for c in tokens["classes"]}
    for path in _files():
        rel = str(path.relative_to(ROOT)).replace("\\", "/")
        if rel.startswith(SKIP):
            continue
        for i, line in enumerate(
            path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            if _WITHDRAWN.search(line):
                continue
            for token in tokens["numbers"]:
                if not rel.startswith(MEASURED_PROSE):
                    continue
                if re.search(rf"(?<![\w.]){re.escape(token)}(?![\w.])", line):
                    out.append(f"{rel}:{i}: the old NUMBER `{token}` survives: {line.strip()[:90]}")
            for token in tokens["rows"]:
                if token in line:
                    out.append(f"{rel}:{i}: the old ROW `{token}` survives: {line.strip()[:90]}")
            for row, old in classes.items():
                if row in line and re.search(rf"\b{re.escape(old)}\b", line):
                    out.append(f"{rel}:{i}: `{row}` is still called `{old}`: {line.strip()[:90]}")
    return out


def main(argv: list[str]) -> int:
    spec = argv[1] if len(argv) > 1 else None
    tokens = old_tokens(diff_text(spec))
    if not any(tokens.values()):
        print("precommit_stale: no figure class, row name or measured number removed")
        return 0
    found = survivors(tokens)
    print(
        f"precommit_stale: looking for {sorted(tokens['numbers'])} "
        f"{sorted(tokens['rows'])} {sorted(tokens['classes'])}"
    )
    if not found:
        print("precommit_stale: no survivor")
        return 0
    print(f"precommit_stale: {len(found)} survivor(s) of a value this diff changed:")
    for line in found[:40]:
        print("  " + line)
    print(
        "\nEach is the old value still written somewhere. Update it, or mark the "
        "line as a deliberate quotation of what it used to say -- `stood here`, "
        "`is withdrawn` -- which is how this repository already records that."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
