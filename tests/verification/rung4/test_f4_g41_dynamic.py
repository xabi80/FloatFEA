"""Rung 4, F4 step 3: EV1's G4.1 dynamic gate, on EX0's committed inputs.

WHAT THE PLAN LOCKS. DQ8 as amended by EV1 and re-locked by EX0 (`F4.md` § 4a) gates the
dynamic reaction/inertia balance per FE body and per case over the DQ6 window, as TWO
dimensionless numbers, each gated and never combined:

    force  :  max_t |Sum_j F_j - M.a|                          /  max_t Sum_j |F_j|
    moment :  max_t |Sum_j (r_j x F_j + M_j) - J.alpha - ...|  /
              max_t Sum_j (|r_j x F_j| + |M_j|)

The denominators are sums of MAGNITUDES, so cancellation in a quiet window cannot shrink
them and manufacture a large relative residual out of nothing.

**IT RUNS WITHOUT AN HSP WORKTREE, AND R721 IS WHY THAT SENTENCE IS AT THE TOP.** The first
version of this file solved through `scripts/report_joint_reactions.py`, which resolves
`ROOT.parent / "HSP-runs"` and imports `platform_rao_pilot`. Neither is tracked and CI
checks out no HSP worktree, so **124 of its 126 cases errored in CI while all 126 passed on
the machine that wrote them** -- `run_rung: 354 collected, 0 failed, 124 errored` against
`126 passed in 1539.78s`. That is R670 for the second time in this directory, and
`test_f4_static_and_mapping.py:848` and `:1028` already said in their own words that a
rung-4 gate must run without an HSP worktree. Everything here reads
`data/f4/dynamic_inputs.npz` through `scripts/f4_dynamic_residual.py`, which imports
nothing outside `numpy` and the standard library.

ABSENCE AND STALENESS ARE REFUSALS, NEVER SKIPS (EX0(b)), and
`test_the_inputs_REFUSE_rather_than_skip` is what holds that in place. A skipped gate
reports green, and that outcome must not be reachable from a missing file. The six-solve
regeneration lives in the `workflow_dispatch` determinism leg (EX0(c)).

EVERY CEILING HERE IS DECLARED OVER EV1's WHOLE COUNTER FAMILY -- BOTH INJECTIONS (R722).
The force ceiling, its counter and its EH4 bound were each first declared over the
joint-drop family alone, and the mass injection binds five decades below it: the weakest
live joint-drop response is `0.14137099995337896` and the weakest live mass response is
`3.385828902450096e-08`. The published upper edge was `2.82742e+07x` where the true one is
`6.77166x`, the published EH4 rise bound was out by `4.17537e+06x` in the one direction EH4
exists to force, and the declared counter sat `2.95e+06` times ABOVE a defect this gate
asserts it must fail.
"""

from __future__ import annotations

import importlib.util
import math
import pathlib
import sys
from pathlib import Path
from typing import Any

import pytest

from floatfea.tolerances import (
    F4_G41_DECOMPOSITION_AGREEMENT,
    F4_G41_DECOMPOSITION_AGREEMENT_COUNTER,
    F4_G41_DYNAMIC_FORCE,
    F4_G41_DYNAMIC_FORCE_COUNTER,
    F4_G41_DYNAMIC_MOMENT,
    F4_G41_DYNAMIC_MOMENT_COUNTER,
    F4_WINDOW_RULE_MIN_EDGE,
)

_ROOT = Path(__file__).resolve().parents[3]


def _module() -> Any:
    """`scripts/f4_dynamic_residual.py`, loaded by path.

    `scripts/` is not a package. Loading by path is what lets the gate read the one
    implementation of the balance instead of carrying a second -- and R711 is what a second
    costs: two forms of this residual differing by `2.2e+13`, one matching its docstring
    and one not. The module is `mypy`-clean and HSP-free; the EXPORT script, which is
    neither, is not on this path.
    """
    name = "floatfea_f4_dynamic_residual"
    if name in sys.modules:
        return sys.modules[name]
    path = _ROOT / "scripts" / "f4_dynamic_residual.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, f"cannot load {path}"
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


_R = _module()

# Collection must not read the npz: a missing file is a REFUSAL reported by a test, not a
# collection error that takes the whole rung down with it.
_PERIODS: tuple[float, ...] = (10.0, 12.5, 14.0, 15.0, 16.2, 20.0)
_BODIES: tuple[str, ...] = ("platform", "hub1", "hub2", "hub3", "hub4")
_BODY_CASES = [(b, t) for t in _PERIODS for b in _BODIES]
_IDS = [f"{b}-T{t:g}" for b, t in _BODY_CASES]


@pytest.fixture(scope="module")
def inputs() -> Any:
    """EX0's committed inputs, sha-checked. No solve, no FloatSim, no HSP."""
    return _R.load()


def _row(inputs: Any, body: str, period: float) -> Any:
    for r in _R.body_cases(inputs):
        if r.body == body and r.period_full_s == period:
            return r
    raise AssertionError(f"no row for {body} at T_full = {period}")


# --------------------------------------------------------------------------------------
# THE INPUTS THEMSELVES
# --------------------------------------------------------------------------------------


def test_the_inputs_REFUSE_rather_than_skip() -> None:
    """EX0(b): an absent or stale file fails. It never skips and never passes.

    THIS IS THE TEST THAT MAKES THE REST OF THE FILE MEAN ANYTHING. Every other test here
    reads the npz; if a missing npz produced a skip, the whole gate would report green on a
    machine that has no inputs -- which is R721 with the colours reversed. So the refusal
    is exercised on paths that cannot exist, in both directions: no npz, and an npz whose
    sha does not match its provenance.
    """
    import json
    import tempfile

    missing = _ROOT / "data" / "f4" / "does_not_exist.npz"
    with pytest.raises(_R.InputsMissing) as caught:
        _R.load(npz=missing)
    assert "REFUSES" in str(caught.value), (
        "the refusal must say what it is. A bare FileNotFoundError reads as a broken test "
        "rather than as a gate declining to measure nothing."
    )

    # AND THE SHA PATH, UNCONDITIONALLY. `load()` checks the digest BEFORE it reads the
    # archive, so this needs no valid npz -- which is the point: an earlier version of
    # this test guarded the sha half behind `if NPZ.exists()`, and on a machine without
    # the inputs it passed having checked one of the two refusals. A branch that silently
    # does nothing is the shape C158 is about.
    with tempfile.TemporaryDirectory() as tmp:
        fake_npz = pathlib.Path(tmp) / "dynamic_inputs.npz"
        fake_npz.write_bytes(b"not an archive, and it does not need to be")
        fake_prov = pathlib.Path(tmp) / "p.json"
        fake_prov.write_text(json.dumps({"npz": {"sha256": "0" * 64}}), encoding="utf-8")
        with pytest.raises(_R.InputsMissing) as stale:
            _R.load(npz=fake_npz, provenance=fake_prov)
        assert "stale" in str(stale.value), str(stale.value)

        # And a provenance that declares no digest at all is refused rather than trusted.
        fake_prov.write_text(json.dumps({"npz": {}}), encoding="utf-8")
        with pytest.raises(_R.InputsMissing) as nodigest:
            _R.load(npz=fake_npz, provenance=fake_prov)
        assert "no npz sha256" in str(nodigest.value), str(nodigest.value)

        # And an absent provenance beside a present npz.
        fake_prov.unlink()
        with pytest.raises(_R.InputsMissing) as noprov:
            _R.load(npz=fake_npz, provenance=fake_prov)
        assert "cannot be checked" in str(noprov.value), str(noprov.value)


def test_the_module_the_gate_IMPORTS_reaches_nothing_but_numpy_and_the_stdlib() -> None:
    """R721, as a check rather than as a sentence (CW0).

    `scripts/f4_dynamic_residual.py`'s docstring claims it imports nothing outside `numpy`
    and the standard library. That claim is the entire reason this gate can run in CI, and
    the previous version of this file was green on one machine precisely because nobody
    was checking the equivalent claim. A docstring is not a check.

    THE AST, NOT THE RUNTIME. Importing the module and reading `sys.modules` would see
    whatever else the test session has already loaded; the source's own import statements
    are what a future edit would add `import report_joint_reactions` to.
    """
    import ast
    import sys

    path = _ROOT / "scripts" / "f4_dynamic_residual.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0 and node.module:
                roots.add(node.module.split(".")[0])
            else:
                roots.add("<relative>")
    # `floatfea` IS ALLOWED, AND THE ALLOWANCE IS VERIFIED BELOW RATHER THAN ASSUMED.
    # EV1's "both edges at least 2x" is a tolerance, so `CLAUDE.md` puts it in
    # `floatfea/tolerances.py` and the module must import it -- which this check caught
    # the moment the literal was replaced, and correctly.
    allowed = set(sys.stdlib_module_names) | {"numpy", "floatfea", "__future__"}
    outside = sorted(roots - allowed)
    assert not outside, (
        f"{path.name} imports {outside}, which is outside `numpy`, `floatfea` and the "
        "standard library. That is how R721 happened: the gate reached `HSP-runs` through "
        "an import chain and errored on 124 of 126 cases in CI while passing on the "
        "machine that wrote it. If a new dependency is genuinely needed, it belongs in the "
        "EXPORT script, which is not on this gate's path."
    )
    assert "numpy" in roots, (
        "the module imports no numpy at all, which means this check is reading the wrong "
        "file -- a needle that matches nothing proves nothing (CW0)."
    )

    # AND WHAT MAKES `floatfea` SAFE TO ALLOW: it reaches no HSP code itself, so the
    # allowance cannot become a back door. Asserted over the whole package, because the
    # risk is a FUTURE edit to some other `floatfea` module and not this import.
    reaching: list[str] = []
    for src in sorted((_ROOT / "floatfea").rglob("*.py")):
        for node in ast.walk(ast.parse(src.read_text(encoding="utf-8"))):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names = [a.name.split(".")[0] for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module.split(".")[0]]
            if {"floatsim", "platform_rao_pilot"} & set(names):
                reaching.append(str(src.relative_to(_ROOT)))
    assert not reaching, (
        f"{sorted(set(reaching))} import FloatSim or the study pilot, so allowing "
        "`floatfea` on this gate's import path is a back door to `HSP-runs`. FloatFEA is "
        "not forked from HSP and must not import it (`CLAUDE.md`)."
    )


def test_the_npz_is_NOT_STALE_against_the_code_that_generated_it() -> None:
    """EX0(c)'s staleness half, in the only form CI can run.

    **EX0(c) ASKS FOR SOMETHING NO CI JOB HERE CAN DO, AND THAT IS REPORTED RATHER THAN
    SUBSTITUTED.** It moves the live six-solve regeneration to the `workflow_dispatch`
    determinism leg. That leg runs on `ubuntu-latest` with no HSP worktree
    (`ci.yml:84-90`), and the regeneration needs FloatSim -- which is the whole reason the
    npz exists. So the re-solve stays a local, on-demand step
    (`python scripts/export_f4_dynamic_inputs.py --check`) and is pasted in the step
    report.

    What CI *can* check is the half that actually goes stale: whether the code that wrote
    the npz is still the code in the tree. EX0(b)'s sha256 catches an edited npz; this
    catches the opposite and more likely case -- the GENERATOR moved and the npz did not.
    `git hash-object` is the same digest the provenance recorded.
    """
    import json
    import subprocess

    prov = _ROOT / "data" / "f4" / "dynamic_inputs.provenance.json"
    if not prov.exists():
        pytest.fail(
            "the provenance is absent, so staleness cannot be judged at all. EX0(b): "
            "refuse, never skip."
        )
    declared = json.loads(prov.read_text(encoding="utf-8"))
    for key in ("generating_script", "measurement_module"):
        entry = declared.get(key, {})
        path = _ROOT / str(entry.get("path", ""))
        assert path.exists(), f"the provenance names {entry.get('path')!r}, which is gone"
        out = subprocess.run(
            ["git", "hash-object", str(path)],
            cwd=_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        assert out.stdout.strip() == str(entry.get("blob_sha")), (
            f"{entry.get('path')} has blob sha {out.stdout.strip()} and the npz's "
            f"provenance was taken at {entry.get('blob_sha')}. The generator moved and "
            "the committed inputs did not, so every figure below is a correct computation "
            "on a stale window. Regenerate with "
            "`python scripts/export_f4_dynamic_inputs.py` -- it needs an HSP worktree."
        )


def test_the_domain_is_thirty_body_cases(inputs: Any) -> None:
    """Five FE bodies by six DQ6 cases, asserted rather than assumed.

    DQ7: the twelve buoys carry no FE mass and are out of this gate. A domain that shrank
    would otherwise make every other assertion here quietly narrower.
    """
    assert tuple(inputs.fe_bodies) == _BODIES, f"{inputs.fe_bodies}"
    assert tuple(inputs.periods_full_s) == _PERIODS, f"{inputs.periods_full_s}"
    rows = _R.body_cases(inputs)
    assert len(rows) == 30, f"{len(rows)} of 30 body-cases"
    assert not any(math.isnan(r.force_rel) or math.isnan(r.moment_rel) for r in rows), (
        "a body-case with a zero denominator reads NaN, and NaN fails every comparison "
        "silently in the passing direction."
    )


@pytest.mark.parametrize("period", _PERIODS, ids=[f"T{t:g}" for t in _PERIODS])
def test_the_two_WAYS_of_forming_the_reaction_agree(inputs: Any, period: float) -> None:
    """The per-pair sum against the one-matvec reaction, per case.

    **THIS IS NOT A REDUNDANT CHECK AND THE FORCE CHANNEL IS WHY.** `base - sum_p contrib_p`
    and `a_eff xi_ddot - (g_mid.T lam) - rhs` are equal in exact arithmetic. The force
    residual closes to about `1e-16` RELATIVE, so there the summation order is comparable to
    the whole quantity: measured across the two implementations with nothing else changed,
    the force clean worst moved from `1.8556070086831165e-16` at hub2/T20 to
    `2.112671361106528e-16` at platform/T20 -- a factor of `1.139` and a different body --
    while the moment channel agreed to `1.371e-11` relative.

    Everything the ceilings in this file are declared against is computed the FIRST way. So
    the second is stored and compared, instead of anyone asserting in prose that the orders
    agree.
    """
    i = list(inputs.periods_full_s).index(period)
    gap = _R.decomposition_gap(inputs, i)
    assert gap < F4_G41_DECOMPOSITION_AGREEMENT, (
        f"at T_full = {period:g} s the per-pair sum and the one-matvec reaction differ by "
        f"{gap!r} relative, outside {F4_G41_DECOMPOSITION_AGREEMENT!r}. The bodies do not "
        "partition the state as the export assumes, and every figure in this file is then "
        "a correct computation of the wrong thing."
    )


def test_DROPPING_one_pair_from_the_sum_breaks_that_agreement(inputs: Any) -> None:
    """The counter-case for the check above, over the WHOLE family.

    Drop one pair and the two forms differ by exactly that pair's own contribution, so the
    gap IS the joint-drop signal -- which is why no separate injection is needed and why the
    counter can be read off the family. The reduction is a MINIMUM over all 120 members,
    each at its worse channel: a counter taken at the member a loop starts at brackets that
    member and not the family, which is R706, R708, R710 and R722's shared subject.
    """
    gaps = _R.drop_one_pair_gaps(inputs)
    assert len(gaps) == 120, f"{len(gaps)} of 120 (pair, case) members"
    (label, period), weakest = min(gaps.items(), key=lambda kv: kv[1])
    assert weakest > F4_G41_DECOMPOSITION_AGREEMENT_COUNTER, (
        f"the WEAKEST drop-one-pair gap over all 120 members is {weakest!r} at {label} / "
        f"T_full = {period:g} s, which does not reach the declared counter "
        f"{F4_G41_DECOMPOSITION_AGREEMENT_COUNTER!r}."
    )
    assert weakest > F4_G41_DECOMPOSITION_AGREEMENT, (
        "a dropped pair must breach the agreement ceiling, or the check above cannot see "
        "the defect it exists for."
    )


# --------------------------------------------------------------------------------------
# THE CEILINGS
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_force_residual_is_inside_its_ceiling(inputs: Any, body: str, period: float) -> None:
    """EV1's force channel, per body and per case. Never averaged, never combined."""
    value = _row(inputs, body, period).force_rel
    assert value < F4_G41_DYNAMIC_FORCE, (
        f"{body} at T_full = {period:g} s reads a force residual of {value!r} relative, "
        f"outside {F4_G41_DYNAMIC_FORCE!r}. `CLAUDE.md` forbids averaging a per-case "
        "diagnostic, so this is the body-case and not a mean over thirty."
    )


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_moment_residual_is_inside_its_ceiling(inputs: Any, body: str, period: float) -> None:
    """EV1's moment channel, per body and per case.

    Moments are about each body's `reference_point`, which `docs/conventions.md:165` locks
    and which FloatSim's `cog_offset_body=None` makes the CoG inside the solve -- NOT about
    `G` as EV1's wording says. The numerator is the same number either way here; the label
    is not, and a figure read without its point is a figure about another point.
    """
    value = _row(inputs, body, period).moment_rel
    assert value < F4_G41_DYNAMIC_MOMENT, (
        f"{body} at T_full = {period:g} s reads a moment residual of {value!r} relative, "
        f"outside {F4_G41_DYNAMIC_MOMENT!r}."
    )


def test_the_two_channels_are_gated_SEPARATELY_and_never_combined() -> None:
    """DQ8 as amended: two numbers, each with its own ceiling.

    The superseded form divided a 6-vector by ONE scalar, which gives a dimensionless
    number on three rows and a LENGTH on the other three -- and C1's correction is that
    WHICH three depends on the body and the window, because `max |Sum reactions|` is the
    force half on only 11 of 17 bodies.
    """
    assert F4_G41_DYNAMIC_FORCE != F4_G41_DYNAMIC_MOMENT, (
        "one value for both channels is the combined form coming back under two names. "
        "The force channel closes to round-off and the moment channel does not."
    )


# --------------------------------------------------------------------------------------
# THE COUNTER-CASES -- EVERY BODY, EVERY CASE, AND BOTH INJECTIONS (EV1, R722)
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("channel", _R.CHANNELS)
def test_the_counter_family_covers_the_whole_domain(inputs: Any, channel: str) -> None:
    """EV1: the counters inject and hold for EVERY body and case. Assert the size.

    150 members per channel: 20 `(body, joint)` pairs plus 5 bodies, by six cases. R706,
    R708, R710 and R722 were each a counter declared over PART of its family -- and R722 is
    this exact shape at the family level, the mass injection having been left out of the
    window rule entirely.
    """
    drop = _R.joint_drop_signals(inputs, channel)
    mass = _R.mass_scale_signals(inputs, channel)
    assert len(drop) == 120, f"{len(drop)} of 120 (pair, case) joint-drop members"
    assert len(mass) == 30, f"{len(mass)} of 30 (body, case) mass members"
    assert len(_R.family(inputs, channel)) == 150, "the two families must not collide by key"


@pytest.mark.parametrize("channel", _R.CHANNELS)
def test_every_LIVE_counter_member_reddens_the_gate(inputs: Any, channel: str) -> None:
    """Every defect above the clean floor must breach the ceiling. Both injections.

    A member at or below the GLOBAL clean worst is VACUOUS: it cannot redden the gate at
    any ceiling the window rule could declare, so it leaves the family by the rule's own
    requirement and not by a cutoff anyone chose. R719: global, not per case -- a per-case
    maximum is whichever body carries that case, and excluding against it once compared a
    body's clean value with itself and cleared by `1.000000049477`.
    """
    ceiling = F4_G41_DYNAMIC_FORCE if channel == "force" else F4_G41_DYNAMIC_MOMENT
    worst, where = _R.clean_worst(inputs, channel)
    live = {k: v for k, v in _R.family(inputs, channel).items() if v > worst}
    assert live, (
        f"no member of the {channel} family can redden the gate. No ceiling exists by the "
        "window rule, and that is the finding rather than a number to pick."
    )
    below = {k: v for k, v in live.items() if v <= ceiling}
    assert not below, (
        f"{len(below)} of {len(live)} live {channel} members do not reach {ceiling!r}: "
        f"{sorted(below.items())[:5]}. The global clean worst is {worst!r} at {where}."
    )


@pytest.mark.parametrize("channel", _R.CHANNELS)
def test_the_counter_sits_below_the_WEAKEST_live_member_of_the_WHOLE_family(
    inputs: Any, channel: str
) -> None:
    """R722: the counter is taken over both injections, not over the one that is largest.

    `F4_G41_DYNAMIC_FORCE_COUNTER` was `0.1`, from the joint-drop family's weakest member
    `0.14137099995337896`, while the mass injection's weakest live response is
    `3.385828902450096e-08` -- so the declared counter sat `2.95e+06` times ABOVE a defect
    this gate asserts it must fail, and the suite was green.
    """
    counter = F4_G41_DYNAMIC_FORCE_COUNTER if channel == "force" else F4_G41_DYNAMIC_MOMENT_COUNTER
    rule = _R.window_rule(inputs, channel)
    assert rule.weakest > counter, (
        f"the WEAKEST live {channel} member over the whole family is {rule.weakest!r} at "
        f"{rule.weakest_at}, which does not reach the declared counter {counter!r}. The "
        "counter is the smallest defect the gate must still fail, taken over the family "
        "and not over the member a loop starts at."
    )


@pytest.mark.parametrize("channel", _R.CHANNELS)
def test_the_window_rule_HOLDS_at_the_declared_ceiling(inputs: Any, channel: str) -> None:
    """EV1's rule, at the value that SHIPS and not at the geometric centre.

    The centre's two edges are equal by construction, so checking them there cannot fail on
    a rounded declaration. These are the edges the declared number actually has, and EH4's
    weakening direction is the one that bites: R722's published rise bound was `7.068550e-02`
    where the true one is `1.692914e-08`.
    """
    tol = F4_G41_DYNAMIC_FORCE if channel == "force" else F4_G41_DYNAMIC_MOMENT
    rule = _R.window_rule(inputs, channel)
    lower, upper = tol / rule.clean_worst, rule.weakest / tol
    assert lower >= F4_WINDOW_RULE_MIN_EDGE, (
        f"the {channel} ceiling {tol!r} is {lower:.6g}x the clean worst "
        f"{rule.clean_worst!r} at {rule.clean_at}, inside the window rule's 2x."
    )
    assert upper >= F4_WINDOW_RULE_MIN_EDGE, (
        f"the weakest live {channel} member {rule.weakest!r} at {rule.weakest_at} is only "
        f"{upper:.6g}x the ceiling {tol!r}, inside the window rule's 2x. This is EH4's "
        "weakening direction and it is the one that caught R722."
    )


def test_the_VACUOUS_moment_members_are_the_two_x_axis_hub_pairs_and_the_mass_family(
    inputs: Any,
) -> None:
    """The exclusion is gated, so the vacuous set cannot grow unnoticed.

    WHAT IS MEASURED: `hub1/3` and `hub3/11` are vacuous in every case, and EV1's mass
    injection is vacuous on this channel for every body and case.

    WHAT IS NOT KNOWN, per EX3 / R724: those two hubs are the ones on the **x axis**, which
    is the wave axis, and **all six cases are heading 0 degrees, so the heading dependence
    is untested.** The earlier published cause -- that two hubs' platform joints sit at
    their reference points and two do not -- is WITHDRAWN: the deck's joints 3, 7, 11 and
    15 all carry `attach_a_body: [0.0, 0.0, 0.0]`, so all four are at their hub's own
    reference point, and the four hubs are identical in mass, inertia and buoy layout.
    """
    worst, _where = _R.clean_worst(inputs, "moment")
    vacuous = {k: v for k, v in _R.family(inputs, "moment").items() if v <= worst}
    drops = sorted({label for kind, label, _t in vacuous if kind == "drop"})
    masses = sorted({label for kind, label, _t in vacuous if kind == "mass"})
    assert drops == ["hub1/3", "hub3/11"], (
        f"the vacuous joint-drop pairs are {drops}, not the two recorded in "
        "`floatfea/tolerances.py`. A member leaving the family is a counter-case getting "
        "narrower and it must be read rather than absorbed."
    )
    assert masses == sorted(_BODIES), (
        f"the mass injection is vacuous on {masses} and the entry records all five. If it "
        "has stopped being vacuous on some body, that is a BETTER gate than the one "
        "declared -- raise the finding rather than widening anything."
    )
    assert len(vacuous) == 42, (
        f"{len(vacuous)} moment members are vacuous, not 42 (2 pairs x 6 cases, plus 5 "
        "bodies x 6 cases of the mass family). A count that moves means a case changed "
        "which."
    )


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_mass_scale_is_VACUOUS_on_the_moment_channel(
    inputs: Any, body: str, period: float
) -> None:
    """EV1's mass injection does not bracket the moment channel, and that is asserted.

    EX2 / R723: THE THRESHOLD IS `2 x` THE GLOBAL CLEAN WORST, WHICH IS WHERE THE CLAIM
    FLIPS -- not the ceiling. Asserting `signal < 2.0e-4` left `43.0229x` of slack, inside
    which the tolerance entry's sentence is false, the moment ceiling's own derivation has
    moved, and this test is still green.
    """
    signal = _R.mass_scale_signals(inputs, "moment")[(body, period)]
    worst, _where = _R.clean_worst(inputs, "moment")
    assert signal < F4_WINDOW_RULE_MIN_EDGE * worst, (
        f"scaling {body}'s mass by 1 + {inputs.mass_eps:g} at T_full = {period:g} s moves "
        f"the moment residual by {signal!r}, which is at or above 2x the global clean "
        f"worst {worst!r}. The entry saying this injection is vacuous here is now wrong, "
        "and so is the moment channel's window-rule derivation -- raise the finding."
    )


def test_the_declared_ceilings_sit_inside_their_counters() -> None:
    """The window rule's shape: ceiling below counter, on each channel separately.

    The cheap half, and not sufficient alone -- BG1's own subject was a pair of literals
    compared with each other. It is here because every other test measures the model and
    this one measures the DECLARATION, so a ceiling edited past its counter is caught
    without reading the npz at all.
    """
    assert F4_G41_DYNAMIC_FORCE < F4_G41_DYNAMIC_FORCE_COUNTER
    assert F4_G41_DYNAMIC_MOMENT < F4_G41_DYNAMIC_MOMENT_COUNTER
