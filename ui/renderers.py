"""
Zenith — Presentation layer renderers.

All functions in this module accept strictly-typed domain models
and produce Streamlit-rendered HTML. User-facing strings from external
sources (Gemini API) are sanitized via html.escape() before injection
to mitigate XSS risk.
"""

import html
from typing import List

import streamlit as st

from domain.models import DiagnosticResponse, Diagnosis, Compatibility, Tweak, DoNotDo


def _sanitize(text: str) -> str:
    """Escape HTML entities in untrusted text to prevent XSS injection.

    Every dynamic value originating from the Gemini API response MUST
    pass through this function before being embedded in an HTML template.
    """
    return html.escape(str(text), quote=True)


def _severity_color(score: int) -> str:
    """Map severity 1-10 to a CSS color variable."""
    if score <= 3:
        return "var(--status-green)"
    if score <= 6:
        return "var(--status-amber)"
    return "var(--status-red)"


def _safety_badge_class(safety: str) -> str:
    """Map safety level to a badge CSS class."""
    mapping = {
        "safe": "badge-safe",
        "caution": "badge-caution",
        "advanced": "badge-risky",
    }
    return mapping.get(safety.lower(), "badge-safe")


def render_diagnosis_header(diagnosis: Diagnosis) -> None:
    """Render the bottleneck type badge and severity bar."""
    color = _severity_color(diagnosis.severity)
    bottleneck = _sanitize(diagnosis.bottleneck_type)

    secondary_html = ""
    if diagnosis.secondary_bottleneck:
        secondary = _sanitize(diagnosis.secondary_bottleneck)
        secondary_html = (
            f'<span class="badge badge-caution" style="margin-left:0.5rem;">'
            f'Secondary: {secondary}</span>'
        )

    html_content = (
        '<div class="result-card fade-in">'
        '<div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem;">'
        '<div>'
        f'<span class="badge badge-bottleneck">{bottleneck} BOTTLENECK</span>'
        f'{secondary_html}'
        '</div>'
        '<div style="color:var(--text-dim); font-size:0.75rem;">'
        f'SEVERITY: <span style="color:{color}; font-weight:700;">{diagnosis.severity}/10</span>'
        '</div>'
        '</div>'
        '<div class="severity-bar-track" style="margin-top:0.8rem;">'
        f'<div class="severity-bar-fill" style="width:{diagnosis.severity * 10}%; background:linear-gradient(90deg, var(--status-green), {color});"></div>'
        '</div>'
        '</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)


def render_plain_english(diagnosis: Diagnosis) -> None:
    """Render the plain English diagnosis card."""
    plain = _sanitize(diagnosis.plain_english)

    reasoning_html = ""
    if diagnosis.reasoning:
        reasoning = _sanitize(diagnosis.reasoning)
        reasoning_html = (
            '<details style="margin-top:0.8rem; cursor:pointer;">'
            '<summary style="color:var(--text-dim); font-size:0.75rem; letter-spacing:1px;">▸ TECHNICAL REASONING</summary>'
            f'<p style="color:var(--text-dim); font-size:0.8rem; margin-top:0.5rem; line-height:1.6;">{reasoning}</p>'
            '</details>'
        )

    html_content = (
        '<div class="result-card fade-in">'
        '<div class="terminal-prompt">diagnosis.summary</div>'
        f'<p style="margin:0.5rem 0 0 0; font-size:0.9rem !important; line-height:1.8 !important;">{plain}</p>'
        f'{reasoning_html}'
        '</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)


def render_compatibility(compat: Compatibility) -> None:
    """Render the compatibility score."""
    if compat.score >= 70:
        color = "var(--status-green)"
    elif compat.score >= 40:
        color = "var(--status-amber)"
    else:
        color = "var(--status-red)"

    note = _sanitize(compat.note)

    html_content = (
        '<div class="result-card fade-in">'
        '<div style="display:flex; align-items:center; gap:1rem;">'
        f'<div style="font-size:2rem; font-weight:700; color:{color};">{compat.score}<span style="font-size:0.9rem; color:var(--text-dim);">%</span></div>'
        '<div>'
        '<div class="terminal-prompt">compatibility.score</div>'
        f'<p style="margin:0.2rem 0 0 0; font-size:0.8rem;">{note}</p>'
        '</div>'
        '</div>'
        '</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)


def render_tweak_card(idx: int, tweak: Tweak) -> None:
    """Render a single optimization tweak card."""
    badge_cls = _safety_badge_class(tweak.safety)
    title = _sanitize(tweak.title)
    tweak_type = _sanitize(tweak.type)
    safety = _sanitize(tweak.safety)
    rationale = _sanitize(tweak.rationale)

    steps_html = "".join(
        f"<li style='margin:0.3rem 0; font-size:0.82rem;'>{_sanitize(step)}</li>"
        for step in tweak.steps
    )

    commands_html = ""
    filtered_cmds = [c for c in tweak.commands if c and c != "null"]
    if filtered_cmds:
        cmd_lines = "\n".join(_sanitize(c) for c in filtered_cmds)
        commands_html = f'<div class="cmd-block">{cmd_lines}</div>\n'

    revert_html = ""
    if tweak.revert:
        revert = _sanitize(tweak.revert)
        revert_html = (
            '<div style="margin-top:0.6rem; padding:0.5rem 0.8rem; background:rgba(0,255,136,0.03); border-radius:3px; border:1px dashed rgba(0,255,136,0.1);">'
            '<span style="color:var(--text-dim); font-size:0.7rem; letter-spacing:1px;">↩ REVERT: </span>'
            f'<span style="font-size:0.8rem;">{revert}</span></div>\n'
        )

    html_content = (
        '<div class="tweak-card fade-in">'
        '<div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.5rem; margin-bottom:0.8rem;">'
        '<div style="display:flex; align-items:center; gap:0.6rem;">'
        f'<span style="color:var(--status-cyan); font-weight:700; font-size:1.2rem;">{idx + 1:02d}</span>'
        f'<span style="font-weight:600; font-size:0.9rem; color:var(--text-main);">{title}</span>'
        '</div>'
        '<div style="display:flex; gap:0.4rem;">'
        f'<span class="badge badge-type">{tweak_type}</span>'
        f'<span class="badge {badge_cls}">{safety}</span>'
        '</div>'
        '</div>'
        f'<ol style="margin:0; padding-left:1.2rem; color:var(--text-main);">{steps_html}</ol>'
        f'{commands_html}<p style="margin:0.6rem 0 0 0; font-size:0.78rem; color:var(--text-dim); font-style:italic;">⟐ {rationale}</p>'
        f'{revert_html}</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)


def render_do_not_do(items: List[DoNotDo]) -> None:
    """Render the 'Do Not Do' warnings section."""
    st.markdown("### ⚠ Do Not Do")
    for item in items:
        action = _sanitize(item.action)
        reason = _sanitize(item.reason)
        html_content = (
            '<div class="warning-card fade-in">'
            f'<div style="font-weight:600; color:var(--status-red); font-size:0.85rem; margin-bottom:0.3rem;">✕ {action}</div>'
            f'<p style="margin:0; font-size:0.8rem; color:var(--text-dim);">{reason}</p>'
            '</div>'
        )
        st.markdown(html_content, unsafe_allow_html=True)


def render_error(error_code: str, error_message: str) -> None:
    """Render an error message in the retro terminal style.

    Both arguments are sanitized because error_message may contain
    user-supplied or LLM-supplied text.
    """
    code = _sanitize(error_code)
    message = _sanitize(error_message)
    html_content = (
        '<div class="warning-card" style="border-left-color:var(--status-red);">'
        '<div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">'
        '<span style="color:var(--status-red); font-weight:700; font-size:0.85rem;">⚠️ ERROR</span>'
        f'<span class="badge badge-risky">{code}</span>'
        '</div>'
        f'<p style="margin:0; font-size:0.82rem; color:var(--text-main);">{message}</p>'
        '</div>'
    )
    st.markdown(html_content, unsafe_allow_html=True)


def render_full_results(result: DiagnosticResponse) -> None:
    """Orchestrate rendering of the full diagnostic result typed objects."""
    st.markdown("## Diagnosis")
    render_diagnosis_header(result.diagnosis)
    render_plain_english(result.diagnosis)

    if result.compatibility:
        st.markdown("## Compatibility")
        render_compatibility(result.compatibility)

    if result.tweaks:
        st.markdown("## Optimizations")
        for idx, tweak in enumerate(result.tweaks[:3]):
            render_tweak_card(idx, tweak)

    if result.do_not_do:
        st.markdown("---")
        render_do_not_do(result.do_not_do)
