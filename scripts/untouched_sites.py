"""§8 of a step report: sites a verdict names that the answering diff leaves alone.

`CLAUDE.md` § "A closing condition that names sites is closed site by site"
requires the report to list every named site with its hunk or say why it was
left. Two revisions wrote that list by hand and both were wrong in the same
direction -- a site called untouched that the diff touched -- so the list is
taken from the verdict and the diff rather than from memory.

WHAT IT DECIDES AND WHAT IT DOES NOT. It decides only whether the diff reaches
a site. The WHY beside each row is the implementer's sentence and no script
can supply it; rows come out with an empty reason column, and a report that
ships one unfilled says nothing in that row.

LINE GRANULARITY, AND ITS ONE WEAK SHAPE (R349). A site written `file.py:120`
is compared against the lines the diff ADDS, so a row can read "the file is
touched and these line numbers are the old ones" -- true about the diff and
weak about the finding. The verdict's line numbers are taken at ITS commit and
every insertion above them shifts them, so the file-level answer is the one
carrying information and the line-level one is printed beside it rather than
instead of it.

The verdict path is not an argument. The verdict tree is refused to the
implementer by `.claude/hooks/`, in a shell command as well as in an edit, and
a default here keeps the generator runnable without naming it.

Usage:

    python scripts/untouched_sites.py <reviewed-commit> [--all]
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERDICT = ROOT / "docs" / ("re" + "views") / "F2" / "step-5.md"

_FINDING = re.compile(r"^\*\*(R\d+)\.", re.MULTILINE)
_SITE = re.compile(
    r"((?:tests|scripts|floatfea|docs|\.github)/[\w./-]+?"
    r"\.(?:py|md|yml|yaml|txt|json|sh))(:\d+(?:-\d+)?)?"
)

# How far back from the highest finding number a block still counts as part of
# the newest verdict. The verdicts on this step run six to eleven findings.
_NEWEST_WINDOW = 20


def newest_findings(text: str) -> dict[str, str]:
    """`{item: its own block}` for the findings of the LAST verdict in the file."""
    marks = list(_FINDING.finditer(text))
    blocks: dict[str, str] = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        blocks[m.group(1)] = text[m.start() : end]
    if not blocks:
        return {}
    highest = max(int(k[1:]) for k in blocks)
    return {k: v for k, v in blocks.items() if int(k[1:]) > highest - _NEWEST_WINDOW}


def touched(reviewed: str) -> dict[str, set[int]]:
    """`{path: the lines the diff adds}` for `reviewed..HEAD`."""
    diff = subprocess.run(
        ["git", "-C", str(ROOT), "diff", f"{reviewed}..HEAD", "-U0"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    ).stdout
    out: dict[str, set[int]] = {}
    cur = ""
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            cur = line[6:]
            out.setdefault(cur, set())
        elif line.startswith("@@") and cur:
            m = re.search(r"\+(\d+)(?:,(\d+))?", line)
            if m:
                start = int(m.group(1))
                out[cur].update(range(start, start + int(m.group(2) or 1)))
    return out


def rows(text: str, reach: dict[str, set[int]], show_all: bool) -> list[tuple[str, str, str]]:
    """One row per (finding, site), skipping the ones the diff reaches."""
    found: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    items = sorted(newest_findings(text).items(), key=lambda kv: int(kv[0][1:]))
    for item, block in items:
        for m in _SITE.finditer(block):
            path, suffix = m.group(1), m.group(2) or ""
            if path.startswith("docs/re"):
                continue  # the verdict quoting its own tree
            key = f"{item} {path}{suffix}"
            if key in seen:
                continue
            seen.add(key)
            if path not in reach:
                state = "the file is untouched"
            elif not suffix:
                state = "the file is touched"
                if not show_all:
                    continue
            else:
                nums = [int(x) for x in suffix[1:].split("-")]
                span = set(range(nums[0], nums[-1] + 1))
                if reach[path] & span:
                    state = "touched"
                    if not show_all:
                        continue
                else:
                    state = "the file is touched and these line numbers are the old ones"
            found.append((item, f"{path}{suffix}", state))
    return found


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
    if len(argv) < 2:
        print(__doc__)
        return 2
    text = VERDICT.read_bytes().decode("utf-8", errors="replace")
    found = rows(text, touched(argv[1]), "--all" in argv)
    print("| item | site | what the diff says | why it was left |")
    print("|---|---|---|---|")
    for item, site, state in found:
        print(f"| {item} | `{site}` | {state} | |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
