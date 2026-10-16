# DIRECTIVE FP — step 2 opens; directive record; push rule; R822–R824

**Provenance: verbatim from the directive message.**

---

FP0 — DIRECTIVE RECORD (standing rule, C25): on receipt, every directive is
  committed verbatim to docs/directives/<ID>.md as the first commit of the
  turn (a standalone plan: commit). Backfill FL, FM, FN, FO and FP now.
  Plans and reports cite those files. Add the rule to CLAUDE.md in the same
  commit.
FP1 — PUSH RULE (standing): push the report commit and the verdict commit
  BEFORE invoking the reviewer, so the judged commit always has a CI run. The
  report's CI section is generated from that run. Add it to CLAUDE.md with FP0.
FP2 — STEP 2's FIRST COMMIT (FO3): R817–R824 and C19–C25.
  - R820: the "no threshold remains" test must be able to fail. Proof:
    reintroducing the 100 kg/m³ floor by ANY route (a local binding, an
    import, a literal) reddens it. Test the behaviour (f = 0.0106 runs and is
    unlabelled), not the source text.
  - R821: restore a test that asserts study_only's behaviour: without it,
    refusal; with it, the run completes and "STUDY — NOT FOR DESIGN" appears
    in every output.
  - --check is a GATE: it exits non-zero on any NaN or inf, and on any
    difference that is not exactly zero (the Q8 golden rule). A NaN pair must
    fail.
  - R822: the duplicate check compares CONSTRUCTED keys (the reviewer's
    prototype: keep the text check, flatten_mapping, then compare
    len(mapping) against len(node.value); typed in the pinned stubs, with no
    ignore). Counter-cases: all five classes refuse (no / No, yes / true,
    ~ / null, 1 / 01, 1.0 / 1.00), plus line_masses {1: …, 01: …}; the
    text-identical control still refuses.
  - R823: merge keys (<<) are REFUSED with a message. The input language does
    not widen silently. Counter-case included.
  - R824: pin the dev toolchain exactly (mypy, types-PyYAML, ruff, black,
    pytest) in one constraints file used by CI and by the documented local
    setup. Paste the local and CI versions, which must be identical.
FP3 — Then FL2 (generality: member topology, the required_section and
  truss_sizing options with FM0's re-solve loop, headings, the period-band
  check) without stopping between items. Target 28 Oct; report the date the
  moment it is at risk.
