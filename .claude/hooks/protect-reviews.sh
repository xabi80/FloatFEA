#!/usr/bin/env bash
# PreToolUse hook: the reviewer's directories are not the implementer's.
#
#   docs/reviews/    verdicts, written through scripts/write_verdict.py
#   tests/corpus/    adversarial test data written by the reviewer (BE3)
#
# WHO IS ASKING, and how this hook knows (BG6). The hook's stdin JSON carries
# `agent_type` and `agent_id` when the caller is a SUBAGENT, and omits both when
# it is the main session. Measured, by dumping the JSON from both:
#
#   main session   keys: cwd, effort, hook_event_name, permission_mode,
#                        prompt_id, scratchpad_dir, session_id, tool_input,
#                        tool_name, tool_use_id, transcript_path
#   subagent       the same keys PLUS agent_id and agent_type
#
# So the earlier note that "hook protection is honour-based between two agents on
# one machine" is wrong, and this hook now keys on the identifier: the
# gating-supervisor may write those directories and nothing else may.
#
# IT ALSO COVERS Bash NOW. The previous version matched Write|Edit|MultiEdit
# only, so a shell redirect went straight past it -- the implementer could have
# written a verdict with `>`.
#
# The Bash rule looks for WRITE INTENT, not for the directory name. A first
# version scanned the whole command string and denied this hook's own commit,
# because the commit MESSAGE mentioned `docs/reviews/` -- it would equally have
# denied `grep`, `cat` and `git log` on those paths, which is both useless and
# the kind of guard people route around. So the match is:
#
#   * a redirect (`>` / `>>`) whose target contains the directory;
#   * a mutating verb -- tee, cp, mv, rm, install, truncate, dd, touch -- in the
#     same command segment as the directory;
#   * `sed -i` in the same segment;
#   * `git checkout|restore|rm|mv` in the same segment.
#
# LIMITATION, stated because it decides what this is worth: it would not catch a
# path assembled at runtime from pieces, nor a verb outside that list. It takes
# accidental writes to zero and makes a deliberate one require intent; the
# outside witness's commit-separation check remains the guard that does not
# depend on this hook at all.

input=$(cat)

# python3 does not exist on every machine this repo is worked on (Windows/Git
# Bash has `python`). Both hooks FAIL CLOSED when the interpreter is missing.
PY_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PY_BIN" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"No python interpreter found; protect-reviews.sh cannot resolve the target path and would FAIL OPEN. Denying by default."}}\n'
  exit 0
fi

read -r agent hit <<EOF
$(printf '%s' "$input" | "$PY_BIN" -c '
import json, re, sys

PROTECTED = r"(?:docs[/\\]+reviews|tests[/\\]+corpus)"
VERBS = r"(?:tee|cp|mv|rm|install|truncate|dd|touch)"

d = json.load(sys.stdin)
ti = d.get("tool_input", {}) or {}
agent = d.get("agent_type") or "-"

path = ti.get("file_path") or ti.get("path") or ""
command = ti.get("command") or ""

hit = "none"
if re.search(PROTECTED, path):
    hit = "reviews" if re.search(r"docs[/\\]+reviews", path) else "corpus"
elif command:
    # Write intent only -- see the header. Segments split on ; | && so a verb in
    # one command does not tar the path in another.
    for seg in re.split(r"[;|&]+", command):
        if not re.search(PROTECTED, seg):
            continue
        writes = (
            re.search(r">>?\s*[\x27\"]?\S*" + PROTECTED, seg)
            or re.search(r"\b" + VERBS + r"\b[^\n]*" + PROTECTED, seg)
            or re.search(r"\bsed\b[^\n]*-i[^\n]*" + PROTECTED, seg)
            or re.search(r"\bgit\b[^\n]*\b(?:checkout|restore|rm|mv)\b[^\n]*"
                         + PROTECTED, seg)
        )
        if writes:
            hit = ("reviews" if re.search(r"docs[/\\]+reviews", seg)
                   else "corpus")
            break
print(agent, hit)
' 2>/dev/null)
EOF

# The reviewer writes these directories. Nobody else does, including any other
# subagent: a general-purpose agent has no business writing a verdict either.
if [ "$agent" = "gating-supervisor" ]; then
  exit 0
fi

case "$hit" in
  reviews)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"docs/reviews/ is written only by the gating-supervisor, through scripts/write_verdict.py. The implementer does not write, edit, or delete verdicts -- and this now covers Bash as well as the editing tools, so a shell redirect is refused too."}}
EOF
    ;;
  corpus)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"tests/corpus/ holds adversarial cases written by the REVIEWER (BE3). A check measured against a corpus its own author wrote measures nothing; that is why this directory is not the implementer's. Write the check, not the cases it is scored against."}}
EOF
    ;;
esac
exit 0
