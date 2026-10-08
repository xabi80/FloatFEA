"""Rung 4, F4 step 3: EV1's G4.1 dynamic gate -- two dimensionless numbers, never combined.

WHAT THE PLAN LOCKS. DQ8, as amended by EV1, gates the dynamic reaction/inertia balance
per FE body and per case over the DQ6 window, as TWO separately gated dimensionless
numbers:

    force  :  max_t |Sum_j F_j - M.a|                          /  max_t Sum_j |F_j|
    moment :  max_t |Sum_j (r_j x F_j + M_j) - J.alpha - ...|  /
              max_t Sum_j (|r_j x F_j| + |M_j|)

The denominators are sums of MAGNITUDES, so cancellation in a quiet window cannot shrink
them and manufacture a large relative residual out of nothing.

WHY THIS FILE EXISTS AT ALL, which is a finding about EV1's own ordering. EV1 asked for
the two ceilings to be declared in `floatfea/tolerances.py` with a plan row in the same
commit, and `801796e` did exactly that -- and reddened rung 3:

    FAILED tests/verification/rung3/test_tolerance_counter_cases.py::
           test_every_accuracy_entry_has_a_counter_that_something_INJECTS
           [F4_G41_DYNAMIC_FORCE] and [F4_G41_DYNAMIC_MOMENT]

BG1's guard is right and it is not failing false: a counter no test under `tests/` names
is a literal sitting beside another literal, and the ceiling above it can be widened
until something else notices. **So the declaration cannot precede the gate**, and the two
belong in one commit. That is the ordering this file restores.

AND THE SCRIPT IS NOW GATE CODE, which answers the question step 3 carried to Xabier.
EV3 placed `scripts/measure/` outside the gate. This file IMPORTS
`scripts/measure/g41_dynamic.py` rather than re-deriving the discrete residual, because a
second implementation of the same balance is the drift this repository has already paid
for -- and R711 is precisely a case where two forms of this residual differ by `2.2e+13`.
The consequence is stated rather than hidden: that script is CZ0 (b) and (c) material from
here on, and a change to it is a change to a gate.

THE COST, STATED. Six coupled solves, once per session, cached at module scope. Nothing
here is skipped, marked slow, or made conditional -- `CLAUDE.md` forbids all three -- so
the ladder job carries the full cost and the step report carries the measurement of it.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest

from floatfea.tolerances import (
    F4_G41_DYNAMIC_FORCE,
    F4_G41_DYNAMIC_FORCE_COUNTER,
    F4_G41_DYNAMIC_MOMENT,
    F4_G41_DYNAMIC_MOMENT_COUNTER,
)

_ROOT = Path(__file__).resolve().parents[3]


def _script() -> Any:
    """`scripts/measure/g41_dynamic.py`, loaded by path.

    `scripts/measure/` is not a package and EV3 says it holds plain scripts. Loading by
    path is what lets the gate read the one implementation of the balance instead of
    carrying a second.
    """
    name = "floatfea_measure_g41_dynamic"
    if name in sys.modules:
        return sys.modules[name]
    path = _ROOT / "scripts" / "measure" / "g41_dynamic.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, f"cannot load {path}"
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# THE CASE AND BODY NAMES COME FROM THE SCRIPT, not from literals here. A parametrize
# list typed by hand is a declaration that drifts from DQ6 the moment a period moves.
_G41 = _script()
T_FULL: tuple[float, ...] = _G41.T_FULL
FE_BODIES: tuple[str, ...] = _G41.FE_BODIES
MASS_EPS: float = _G41.MASS_EPS

_BODY_CASES = [(b, t) for t in T_FULL for b in FE_BODIES]
_IDS = [f"{b}-T{t:g}" for b, t in _BODY_CASES]


@pytest.fixture(scope="module")
def measured() -> list[dict]:
    """The six cases, solved ONCE for the whole module.

    Parametrisation ids are built from `T_FULL` and `FE_BODIES` above, which are
    constants, so collection does not solve anything; the first test that asks for this
    fixture pays for all six.
    """
    return [_G41.measure_case(p) for p in T_FULL]


def _case(measured: list[dict], period: float) -> dict:
    for c in measured:
        if c["period_full_s"] == period:
            return c
    raise AssertionError(
        f"no case at T_full = {period}; measured {[c['period_full_s'] for c in measured]}"
    )


def _clean_worst(measured: list[dict], channel: str) -> tuple[float, str]:
    """The GLOBAL clean worst over all body-cases, and where it is.

    R719: GLOBAL, not per case. A per-case maximum is whichever body happens to carry
    that case, so a test that excludes against it can compare a body's clean value with
    itself -- which is how a vacuous member was admitted at `T_full = 10`, clearing by a
    ratio of `1.000000049477`.
    """
    return max(
        (v[f"{channel}_rel"], f"{b}/T{c['period_full_s']:g}")
        for c in measured
        for b, v in c["bodies"].items()
    )


def _signals(measured: list[dict], channel: str) -> dict[tuple[str, float], float]:
    """Every `(body/joint, case)` joint-drop signal on this channel."""
    return {
        (k, c["period_full_s"]): v
        for c in measured
        for k, v in c["counters"]["joint_dropped_signal"][channel].items()
    }


# --------------------------------------------------------------------------------------
# THE CEILINGS
# --------------------------------------------------------------------------------------


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_force_residual_is_inside_its_ceiling(
    measured: list[dict], body: str, period: float
) -> None:
    """EV1's force channel, per body and per case. Never averaged, never combined."""
    value = _case(measured, period)["bodies"][body]["force_rel"]
    assert value < F4_G41_DYNAMIC_FORCE, (
        f"{body} at T_full = {period:g} s reads a force residual of {value!r} relative, "
        f"outside {F4_G41_DYNAMIC_FORCE!r}. `CLAUDE.md` forbids averaging a per-case "
        "diagnostic, so this is the body-case and not a mean over thirty."
    )


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_moment_residual_is_inside_its_ceiling(
    measured: list[dict], body: str, period: float
) -> None:
    """EV1's moment channel, per body and per case.

    Moments are about each body's `reference_point`, which `docs/conventions.md` locks and
    which FloatSim's `cog_offset_body=None` makes the CoG inside the solve -- NOT about
    `G` as EV1's wording says. The numerator is the same number either way here; the
    label is not, and a figure read without its point is a figure about another point.
    """
    value = _case(measured, period)["bodies"][body]["moment_rel"]
    assert value < F4_G41_DYNAMIC_MOMENT, (
        f"{body} at T_full = {period:g} s reads a moment residual of {value!r} relative, "
        f"outside {F4_G41_DYNAMIC_MOMENT!r}."
    )


def test_the_two_channels_are_gated_SEPARATELY_and_never_combined() -> None:
    """DQ8 as amended: two numbers, each with its own ceiling.

    The superseded form divided a 6-vector by ONE scalar, which gives a dimensionless
    number on three rows and a LENGTH on the other three -- and C1's correction is that
    WHICH three depends on the body and the window, because `max |Sum reactions|` is the
    force half on only 11 of 17 bodies. Two ceilings with two denominators is what makes
    both numbers dimensionless on every body.
    """
    assert F4_G41_DYNAMIC_FORCE != F4_G41_DYNAMIC_MOMENT, (
        "one value for both channels is the combined form coming back under two names. "
        "The force channel closes to round-off and the moment channel does not; a single "
        "ceiling is either loose on one or false on the other."
    )


# --------------------------------------------------------------------------------------
# THE COUNTER-CASES -- EVERY BODY AND EVERY CASE (EV1)
# --------------------------------------------------------------------------------------


def test_the_joint_drop_family_covers_the_whole_domain(measured: list[dict]) -> None:
    """EV1: the counter must inject and hold for EVERY body and case. Assert the size.

    Twenty `(body, joint)` pairs -- the platform's four hub joints, and each hub's one
    platform joint plus three buoy joints -- by six cases. R706, R708 and R710 were each a
    counter-case that bracketed PART of its family and was declared over all of it.
    """
    assert len(measured) == len(T_FULL), f"{len(measured)} of {len(T_FULL)} cases measured"
    for channel in ("force", "moment"):
        sigs = _signals(measured, channel)
        assert len(sigs) == 120, (
            f"the {channel} joint-drop family holds {len(sigs)} (pair, case) members and "
            f"the domain is 20 pairs x {len(T_FULL)} cases = 120."
        )
    body_cases = {(b, c["period_full_s"]) for c in measured for b in c["bodies"]}
    assert len(body_cases) == 30, f"{len(body_cases)} of 30 body-cases"


def test_every_joint_drop_reddens_the_force_gate(measured: list[dict]) -> None:
    """Drop one joint's reaction: the force gate must fail, on all 120 members.

    THE RESPONSE IS THE SIGNAL AND NOT THE ABSOLUTE RESIDUAL (R719, R720). `dropped -
    clean` is algebraically `contrib[j, k]`, the joint's own contribution. Reported as
    `max_t |resid_injected|` instead, a member contributing nothing reports its body's
    clean value and reads as a response -- which is how two pairs three decades below the
    clean worst were admitted to the family.
    """
    sigs = _signals(measured, "force")
    below = {k: v for k, v in sigs.items() if v <= F4_G41_DYNAMIC_FORCE}
    assert not below, (
        f"{len(below)} of {len(sigs)} joint-drop signals do not reach the force ceiling "
        f"{F4_G41_DYNAMIC_FORCE!r}: {sorted(below.items())[:5]}. A defect the gate cannot "
        "see is a defect the gate does not gate."
    )
    weakest = min(sigs.values())
    assert weakest > F4_G41_DYNAMIC_FORCE_COUNTER, (
        f"the WEAKEST joint-drop signal over all {len(sigs)} members is {weakest!r}, "
        f"which does not reach the declared counter {F4_G41_DYNAMIC_FORCE_COUNTER!r}. The "
        "counter is the smallest defect the gate must still fail, taken over the whole "
        "family and not over the member the author happened to look at."
    )


def test_every_NON_VACUOUS_joint_drop_reddens_the_moment_gate(measured: list[dict]) -> None:
    """The same family on the moment channel, with its vacuous members EXCLUDED BY RULE.

    A member whose signal is at or below the GLOBAL clean worst cannot redden this gate at
    any ceiling the window rule could declare, so it is vacuous. No threshold is chosen
    here: the window rule's own requirement decides membership, which is the
    no-invented-cutoff rule applied to a filter rather than to a ceiling.
    """
    worst, where = _clean_worst(measured, "moment")
    sigs = _signals(measured, "moment")
    live = {k: v for k, v in sigs.items() if v > worst}
    assert live, (
        "no member of the family can redden the moment channel. No ceiling exists by the "
        "window rule, and that is the finding rather than a number to pick."
    )
    below = {k: v for k, v in live.items() if v <= F4_G41_DYNAMIC_MOMENT}
    assert not below, (
        f"{len(below)} of {len(live)} non-vacuous joint-drop signals do not reach the "
        f"moment ceiling {F4_G41_DYNAMIC_MOMENT!r}: {sorted(below.items())[:5]}."
    )
    weakest = min(live.values())
    assert weakest > F4_G41_DYNAMIC_MOMENT_COUNTER, (
        f"the WEAKEST non-vacuous joint-drop signal is {weakest!r} against a declared "
        f"counter of {F4_G41_DYNAMIC_MOMENT_COUNTER!r}. The global clean worst is "
        f"{worst!r} at {where}."
    )


def test_the_VACUOUS_moment_members_are_exactly_the_two_declared_pairs(
    measured: list[dict],
) -> None:
    """The exclusion is itself gated, so the vacuous set cannot grow unnoticed.

    `hub1/3` and `hub3/11` are vacuous in every case: those hubs' platform joints sit AT
    their own reference points, so there is no lever and the locked-axis moment is carried
    on the platform side. hub2's and hub4's platform joints are not at their reference
    points and are not vacuous.

    AND "THE VACUOUS SET IS CASE-DEPENDENT" WAS FALSE -- an earlier commit of mine said
    so. Both pairs are vacuous in all six. What varies is which BODY carries the case
    maximum, which is why the test above is against the GLOBAL worst.
    """
    worst, _where = _clean_worst(measured, "moment")
    vacuous = {k: v for k, v in _signals(measured, "moment").items() if v <= worst}
    pairs = sorted({k for k, _t in vacuous})
    assert pairs == ["hub1/3", "hub3/11"], (
        f"the vacuous pairs are {pairs}, not the two declared in "
        "`floatfea/tolerances.py`. A member leaving the family is a counter-case getting "
        "narrower, and it must be read rather than absorbed."
    )
    assert len(vacuous) == 12, (
        f"{len(vacuous)} members are vacuous, not 12. Both pairs are vacuous in all "
        f"{len(T_FULL)} cases, and a count that moves means a case changed which."
    )


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_mass_scale_reddens_the_force_gate(
    measured: list[dict], body: str, period: float
) -> None:
    """EV1's second injection: `M` scaled by `1 + 1e-6`, on every body and case.

    A wrong `M` is wrong everywhere the residual reads it, so both `a_eff ddot` and the
    `alpha_m M ddot` inside `rhs` are reformed -- not `M` in one place.
    """
    family = _case(measured, period)["counters"]["mass_scaled_signal"]["force"]
    assert body in family, (
        f"{body} has no force mass-scale response at T_full = {period:g} s, so the "
        "injection does not reach it. A missing member reads as a KeyError and not as a "
        f"failure, which is why it is asserted: the family holds {sorted(family)}."
    )
    signal = family[body]
    assert signal > F4_G41_DYNAMIC_FORCE, (
        f"scaling {body}'s mass by 1 + {MASS_EPS:g} at T_full = {period:g} s moves the "
        f"force residual by {signal!r}, inside the ceiling {F4_G41_DYNAMIC_FORCE!r}. The "
        "gate would pass a mass error it is required to catch."
    )


@pytest.mark.parametrize("body, period", _BODY_CASES, ids=_IDS)
def test_the_mass_scale_is_VACUOUS_on_the_moment_channel(
    measured: list[dict], body: str, period: float
) -> None:
    """EV1's second injection DOES NOT bracket the moment channel, and that is declared.

    This asserts the direction the measurement actually has, so the fact is held in place
    instead of being a sentence in a tolerance comment. At `1 + 1e-6` the moment signal is
    three decades BELOW the clean worst it would have to exceed; solved on the signal, a
    2x edge needs `1 + 3.4e-03`. **EV1 specifies `1 + 1e-6`, so the scale is not changed**
    -- the joint-drop injection brackets both channels and the window rule closes on it
    alone.

    R720 is why this is a test and not a remark: the scale was first published as
    `1 + 4.816e-06` and then `1 + 4.499e-05`, both EXTRAPOLATED from a quantity the clean
    floor dominates, and both wrong -- by about 700x and 80x. A figure nothing asserts
    against is a figure nobody re-measures.
    """
    family = _case(measured, period)["counters"]["mass_scaled_signal"]["moment"]
    assert body in family, (
        f"{body} has no moment mass-scale response at T_full = {period:g} s, so the "
        "injection does not reach it. A missing member reads as a KeyError and not as a "
        f"failure, which is why it is asserted: the family holds {sorted(family)}."
    )
    signal = family[body]
    assert signal < F4_G41_DYNAMIC_MOMENT, (
        f"scaling {body}'s mass by 1 + {MASS_EPS:g} at T_full = {period:g} s now moves "
        f"the moment residual by {signal!r}, which REACHES the ceiling "
        f"{F4_G41_DYNAMIC_MOMENT!r}. That is a better gate than the one declared, and the "
        "tolerance entry saying this injection is vacuous here is now wrong -- raise the "
        "finding rather than widening anything."
    )


def test_the_declared_ceilings_sit_inside_their_counters() -> None:
    """The window rule's shape: ceiling below counter, on each channel separately.

    This is the cheap half and it is not sufficient on its own -- BG1's own subject was a
    pair of literals compared with each other. It is here because the tests above measure
    the model and this one measures the DECLARATION, and a ceiling edited past its counter
    should not need a six-solve run to be caught.
    """
    assert F4_G41_DYNAMIC_FORCE < F4_G41_DYNAMIC_FORCE_COUNTER
    assert F4_G41_DYNAMIC_MOMENT < F4_G41_DYNAMIC_MOMENT_COUNTER
