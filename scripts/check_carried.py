"""Every finding in the newest verdict appears in the newest report's `Carried`.

BS0. Twice in three rounds the report's `Carried` section dropped a whole
verdict's findings -- eleven items once, five of them blocking or STOP-class,
four untouched in the repository. Both times a review found it. `CLAUDE.md`
§ "Every claim carries its command" says the dependency list is part of what gets
re-read at every step, by a reader that was not the one who skipped it; this
makes that mechanical, so a report that does not carry every finding cannot end a
turn.

WHAT IT CHECKS AND WHAT IT DOES NOT. It compares the SET of `R<n>` identifiers
declared as findings in the newest verdict against the set mentioned anywhere in
the newest report's `Carried` section. It does not check that the status written
beside each one is true -- a report can carry `R142` and lie about it. That half
is the reviewer's, and this is the half a script can hold.

Exit status is 0 when every finding is carried, 1 otherwise. Usage:

    python scripts/check_carried.py [--verdict PATH] [--report PATH]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# A finding is declared as a bolded `**R<n>. (class)` heading in a verdict. The
# same file mentions many other `R<n>` in prose -- carried items, cross-
# references -- and those are not this verdict's findings.
_FINDING = re.compile(r"^\*\*(R\d+)\.", re.MULTILINE)
_MENTION = re.compile(r"\bR\d+\b")


def _read(path: Path) -> str:
    """Both files are hand-written markdown and are not reliably UTF-8.

    A verdict written with a Windows-1252 dash would make this script raise, and
    a guard that raises is a guard that gets removed. Decoded permissively: the
    only thing extracted is `R<n>`, which is ASCII in every encoding here.
    """
    return path.read_bytes().decode("utf-8", errors="replace")


def _newest_report_carried(report: Path) -> tuple[str, set[str]]:
    """The `Carried` section of the LAST revision in the report file."""
    text = _read(report)
    revisions = [m.start() for m in re.finditer(r"^# Revision \d+", text, re.MULTILINE)]
    body = text[revisions[-1] :] if revisions else text
    heads = [m for m in re.finditer(r"^##+ .*Carried.*$", body, re.MULTILINE)]
    if not heads:
        return body, set()
    start = heads[-1].end()
    nxt = re.search(r"^##+ ", body[start:], re.MULTILINE)
    section = body[start : start + nxt.start()] if nxt else body[start:]
    return section, set(_MENTION.findall(section))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verdict", default="docs/reviews/F2/step-4.md")
    ap.add_argument("--report", default="docs/reports/F2/step-4.md")
    args = ap.parse_args(argv)

    verdict, report = ROOT / args.verdict, ROOT / args.report
    if not verdict.exists() or not report.exists():
        print(f"check_carried: {verdict} or {report} missing", file=sys.stderr)
        return 1

    findings = set(_FINDING.findall(_read(verdict)))
    if not findings:
        # A verdict with no findings parsed is a parse failure, not a clean bill.
        print(
            "check_carried: no findings parsed from the verdict -- the format "
            "changed and this check would pass on anything",
            file=sys.stderr,
        )
        return 1

    section, carried = _newest_report_carried(report)
    if not section.strip():
        print("check_carried: the newest revision has no Carried section", file=sys.stderr)
        return 1

    missing = sorted(findings - carried, key=lambda r: int(r[1:]))
    if missing:
        print(
            "check_carried: the newest report's Carried section omits " f"{', '.join(missing)}",
            file=sys.stderr,
        )
        print(
            f"  verdict declares {len(findings)} findings; "
            f"{len(findings) - len(missing)} are carried",
            file=sys.stderr,
        )
        return 1

    print(f"check_carried: all {len(findings)} findings carried")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
