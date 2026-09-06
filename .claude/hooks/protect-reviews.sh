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
# THREE HOLES THE REVIEWER MEASURED, TWO CLOSED HERE (BH5):
#
#   1. `cd tests/corpus && echo x > y` was ALLOWED -- the protected path is in
#      one segment and the write in another. Closed: for a caller that is not the
#      supervisor, ANY command mentioning a protected directory together with a
#      redirect or a mutating verb ANYWHERE in it is denied.
#
#      "Over-blocking the implementer costs nothing" was WRONG as first written.
#      The scan also listed a bare `cd` as write intent, which denied every READ
#      of a verdict made from a command beginning with `cd` -- nearly all of
#      them, and it blocked the first attempt to read the eighth verdict. The
#      `cd` clause bought nothing: `cd tests/corpus && echo x > y` is already
#      caught by the redirect in the same command string. Over-blocking a WRITE
#      costs nothing; over-blocking a READ costs the ability to work.
#
#      That sentence had to be applied twice more. The whole-command redirect
#      match also fired on `2>&1`, so `pytest ... 2>&1` on a path under
#      tests/corpus/ was denied -- a read, again. The redirect clause now ignores
#      file-descriptor redirections. THE PATTERN, recorded because it is the
#      third instance: every widening of this rule has cost a read and bought
#      nothing, because the implementer's writes here are already caught by the
#      narrow forms.
#   2. Malformed JSON FAILED OPEN -- the python helper printed nothing, `agent`
#      and `hit` came back empty, and the case fell through to `exit 0`. Closed:
#      the helper prints a sentinel on any parse failure and the hook denies.
#   3. `NotebookEdit` was not in the matcher. Closed in settings.json.
#
# LIMITATION that remains, stated because it decides what this is worth: a path
# assembled at runtime from pieces is not caught, and neither is a mutating verb
# outside the list. It takes accidental writes to zero and makes a deliberate one
# require intent; the outside witness's commit-separation check remains the guard
# that does not depend on this hook at all.

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

try:
    d = json.load(sys.stdin)
    ti = d.get("tool_input", {}) or {}
except Exception:
    # FAIL CLOSED. Input this hook cannot parse is input it cannot clear.
    print("- unparseable")
    raise SystemExit(0)
agent = d.get("agent_type") or "-"

path = ti.get("file_path") or ti.get("path") or ""
command = ti.get("command") or ""

hit = "none"
if re.search(PROTECTED, path):
    hit = "reviews" if re.search(r"docs[/\\]+reviews", path) else "corpus"
elif command and re.search(PROTECTED, command):
    # WHOLE COMMAND, not per segment (BH5 hole 1). Segmenting let
    # `cd tests/corpus && echo x > y` through: the path was in one segment and
    # the write in another. A caller that is not the supervisor has no
    # legitimate write here, so any write shape anywhere in a command that
    # mentions a protected directory is refused.
    writes = (
        # A redirect, but NOT a file-descriptor one: `2>&1` and `2>/dev/null`
        # are not writes to anything, and matching a bare `>` denied every
        # `pytest ... 2>&1` that mentioned a protected path. Third false
        # positive from this clause; see the header.
        re.search(r"(?<![0-9])>{1,2}(?!&)", command)
        or re.search(r"\b" + VERBS + r"\b", command)
        or re.search(r"\bsed\b[^\n]*-i", command)
        or re.search(r"\bgit\b[^\n]*\b(?:checkout|restore|rm|mv)\b", command)
    )
    if writes:
        hit = ("reviews" if re.search(r"docs[/\\]+reviews", command)
               else "corpus")
print(agent, hit)
' 2>/dev/null)
EOF

# The reviewer writes these directories. Nobody else does, including any other
# subagent: a general-purpose agent has no business writing a verdict either.
if [ "$agent" = "gating-supervisor" ]; then
  exit 0
fi

case "$hit" in
  unparseable)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"protect-reviews.sh could not parse its own hook input. A hook that cannot read the request cannot clear it, so this fails CLOSED (BH5)."}}
EOF
    ;;
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
