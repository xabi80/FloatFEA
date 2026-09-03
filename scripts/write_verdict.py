#!/usr/bin/env python3
"""Write a supervisor verdict to docs/reviews/F<n>/step-<k>.md.

Used only by the gating-supervisor agent. The editing tools are blocked from
docs/reviews/ by a PreToolUse hook; this is the one sanctioned path in.

Usage:
    python scripts/write_verdict.py --milestone 2 --step 5 < review.md

The review body is read from stdin and must begin with a line
`Verdict: PASS|HOLD|STOP`. The script stamps the reviewed commit, refuses to
overwrite a PASS with anything but a fresh review of a *changed* report, and
refuses a body that lacks the mandatory sections, so a verdict cannot be
written by accident or by a summary that skipped the dependency re-read.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REQUIRED = ("## Carried", "## Findings", "## Tolerances touched", "## Next step opens when")
VERDICTS = ("PASS", "HOLD", "STOP")


def sha() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestone", type=int, required=True)
    ap.add_argument("--step", type=int, required=True)
    args = ap.parse_args()

    body = sys.stdin.read()
    m = re.match(r"\s*Verdict:\s*(\w+)", body)
    if not m or m.group(1) not in VERDICTS:
        sys.exit("refused: body must begin with 'Verdict: PASS|HOLD|STOP'")
    missing = [s for s in REQUIRED if s not in body]
    if missing:
        sys.exit(f"refused: missing sections {missing}")
    if re.search(r"^## Carried\s*\n\s*(?=## )", body, re.M):
        sys.exit("refused: '## Carried' is empty — write 'checked, nothing carried' if so")

    root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    report = root / f"docs/reports/F{args.milestone}/step-{args.step}.md"
    if not report.exists():
        sys.exit(f"refused: no step report at {report}")

    out = root / f"docs/reviews/F{args.milestone}/step-{args.step}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    header = f"# Review — F{args.milestone} step {args.step}\nReviewed commit: {sha()}\n"
    out.write_text(header + body.lstrip())
    print(f"wrote {out.relative_to(root)}  ({m.group(1)} @ {sha()[:10]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
