"""§8 of a step report: sites a verdict names that the answering diff leaves alone.

`CLAUDE.md` § "A closing condition that names sites is closed site by site"
requires the report to list every named site with its hunk or say why it was
left. Two revisions wrote that list by hand and both were wrong in the same
direction -- a site called untouched that the diff touched -- so the list is
generated.

IT IS THE GUARD'S OWN LIST, NOT A SECOND OPINION. `tests/test_report_carried.py`
is what decides whether a site was answered: it expands the verdict's sites,
diffs the step, and fails on any site the report does not either touch or
write `no change` beside. This imports that module and reads `SITES` and
`TOUCHED` from it, so the table cannot enumerate a different set than the
check does. A generator with its own regex is a second implementation of the
thing being satisfied, and the two drift -- which is how the first version of
this script produced 68 rows against the guard's 87.

WHAT IT DECIDES AND WHAT IT DOES NOT. It decides only which sites the diff
does not reach. The reason beside each row is the implementer's sentence and
no script can supply it; rows come out with an empty reason, and a row that
ships empty says nothing.

THE PHRASE `no change` IS NOT DECORATION. It is the literal string the guard
looks for on the site's own line, so a reason that omits it leaves the site
unanswered however well it reads.

R349 IS NARROWED, NOT CLOSED. The guard expands `file.py:289-327` into one
site per line, and a line number taken at the verdict's commit shifts under
every insertion above it -- so a moved block prints as "the line number is
the old one", which is true about the diff and weak about the finding.
Distinguishing a moved block from an untouched one still needs the hunk.

The verdict path is not an argument: that tree is refused to the implementer
by `.claude/hooks/`, in a shell command as well as in an edit.

Usage:

    python scripts/untouched_sites.py [--all]
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tests"))

# The import is by path, not by package: `tests/` is not importable as one.
from test_report_carried import (  # type: ignore[import-not-found]  # noqa: E402
    SITES,
    TOUCHED,
    TOUCHED_ERROR,
)


def state_of(path: str, line: int) -> str | None:
    """What the diff says about one site, or `None` when it reaches it."""
    hit = [p for p in TOUCHED if p.endswith(path)]
    if not hit:
        return "the file is untouched"
    if line == 0 or any(line in TOUCHED[p] for p in hit):
        return None
    return "the file is touched and this line number is the old one"


GENERATED_MARK = "<!-- generated: scripts/untouched_sites.py -->"


def _mark(text: str) -> str:
    """CY3: the generated/hand-written split keys on this line."""
    return GENERATED_MARK + "\n\n" + text


def main(argv: list[str]) -> int:
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[union-attr]
    if TOUCHED_ERROR is not None:
        print(f"the diff is not available: {TOUCHED_ERROR}", file=sys.stderr)
        return 1
    show_all = "--all" in argv
    print(GENERATED_MARK)
    print()
    print("| item | site | what the diff says | why it was left |")
    print("|---|---|---|---|")
    for finding, path, line in SITES:
        state = state_of(path, line)
        if state is None:
            if not show_all:
                continue
            state = "touched"
        site = f"{path}:{line}" if line else path
        print(f"| {finding} | `{site}` | {state} | |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
