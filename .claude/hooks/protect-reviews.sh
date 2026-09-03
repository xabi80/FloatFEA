#!/usr/bin/env bash
# PreToolUse hook on Write|Edit|MultiEdit: deny edits under docs/reviews/.
# Verdicts are written only through scripts/write_verdict.py by the
# gating-supervisor. This blocks the editing tools; it cannot distinguish
# which agent is calling, so the independence of the verdict is ultimately
# checked by the outside witness (docs/SUPERVISOR.md), which verifies that
# verdict commits are separate from the code commits they judge.

input=$(cat)

# python3 does not exist on every machine this repo is worked on (Windows/Git
# Bash has `python`). Both hooks FAIL OPEN when the interpreter is missing --
# protect-reviews resolves an empty path and allows the edit; require-verdict
# emits invalid JSON and the stop is allowed. Resolve once, loudly.
PY_BIN=$(command -v python3 || command -v python || true)
if [ -z "$PY_BIN" ]; then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"No python interpreter found; protect-reviews.sh cannot resolve the target path and would FAIL OPEN. Denying by default."}}
'
  exit 0
fi
path=$(printf '%s' "$input" | "$PY_BIN" -c '
import json,sys
d=json.load(sys.stdin)
ti=d.get("tool_input",{})
print(ti.get("file_path") or ti.get("path") or "")
' 2>/dev/null)

case "$path" in
  *docs/reviews/*)
    cat <<'EOF'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"docs/reviews/ is written only by the gating-supervisor through scripts/write_verdict.py. The implementer does not write, edit, or delete verdicts."}}
EOF
    ;;
esac
exit 0
