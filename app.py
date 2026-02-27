"""
Zenith — System Diagnostics Controller (Presentation Layer).

This module is the Streamlit entrypoint. It captures user input,
delegates to the Service layer, and renders results via UI renderers.
No business logic or data access lives here.
"""

import streamlit as st
import streamlit.components.v1 as components


from domain.models import TelemetryInput
from domain.exceptions import ZenithException
from service.diagnostics_service import DiagnosticsService
from ui.renderers import render_full_results, render_error
from ui.components import HARDWARE_TOPOLOGY_HTML
from ui_constants import BRUTALIST_CSS

# ──────────────────────────────────────────────────────────────
# 1. PAGE CONFIG (must be first Streamlit call)
# ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ZENITH // System Diagnostics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────
# 2. EMBEDDED CSS — Retro CRT / Terminal Aesthetic
# ──────────────────────────────────────────────────────────────
st.markdown(BRUTALIST_CSS, unsafe_allow_html=True)


# ──────────────────────────────────────────────────────────────
# 3. HEADER & NAVIGATION
# ──────────────────────────────────────────────────────────────

st.markdown(
    """
    <div class="qf-nav-grid">
        <div class="qf-nav-item">
            <span style="margin-right:0.5rem;">&#x2630;</span> ZENITH
        </div>
        <div class="qf-nav-link">Architecture</div>
        <div class="qf-nav-link">Diagnostics</div>
        <div class="qf-nav-link">Manifesto</div>
    </div>
    """,
    unsafe_allow_html=True,
)

head_col1, head_col2 = st.columns([1.5, 1], gap="large")

with head_col1:
    st.markdown(
        """
        <div class="header-banner">
            <h1 class="brutalist-title">Hardware Insights &gt;&gt;&gt;<br>&gt;&gt;&gt; Peak Performance</h1>
            <div class="header-subtitle"><br>ZENITH Is A Diagnostic Tool Built To Power The Foundations Of Digital Infrastructure.<br><strong style="color:var(--text-main);">CPU, GPU, RAM, Storage, And Software</strong> All Run On Fast, Scalable Analysis Designed For Real-World Impact.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with head_col2:
    components.html(HARDWARE_TOPOLOGY_HTML, height=280)

# ──────────────────────────────────────────────────────────────
# 4. INPUT PORTAL (MAIN PAGE GRID)
# ──────────────────────────────────────────────────────────────

st.markdown("<hr style='margin: 0;'>", unsafe_allow_html=True)
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    st.markdown(
        """
        <div style="padding: 2rem 0; height: 100%;">
            <h2 style="border:none; padding:0; margin:0; font-size: 3rem; line-height:1; letter-spacing:-0.03em;">
                DIAGNOSTIC<br>TELEMETRY<br>PORTAL
            </h2>
            <p style="color:var(--text-muted); font-family:var(--font-mono); font-size:0.9rem; margin-top: 2rem; line-height: 1.6;">
            &gt;&gt; Initialize telemetry gathering.<br><br>
            Provide absolute hardware specifications and software parameters. ZENITH will execute a multi-vector analysis to identify processing bottlenecks, memory leaks, and render delays.<br><br>
            <strong style="color:var(--text-main);">INPUT REQUIRED TO PROCEED.</strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_right:
    st.markdown("### >>> SYSTEM_SPECS_CONFIG")

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        cpu = st.text_input("CPU TIER", placeholder="e.g. AMD Ryzen 5", key="input_cpu")
    with row1_col2:
        gpu = st.text_input("GPU COMPUTE", placeholder="e.g. NVIDIA RTX 3050", key="input_gpu")

    row2_col1, row2_col2, row2_col3 = st.columns(3)
    with row2_col1:
        ram = st.text_input("RAM ALLOCATION", placeholder="e.g. 16GB", key="input_ram")
    with row2_col2:
        os_name = st.selectbox("OPERATING_SYSTEM", options=["Windows 10", "Windows 11", "Linux", "macOS"], index=None, placeholder="Select OS...", key="input_os")
    with row2_col3:
        storage = st.selectbox("STORAGE_CLASS", options=["NVMe SSD", "SATA SSD", "HDD"], index=None, placeholder="Select Storage...", key="input_storage")
        
    st.markdown("### >>> TARGET_OPERATION")

    application = st.text_input("APPLICATION DEPLOYMENT", placeholder="e.g. Elden Ring, VS Code", key="input_app")
    symptoms = st.text_area("ANOMALY_SYMPTOMS", placeholder="Describe the performance issue in detail...", height=120, key="input_symptoms")

    st.markdown("<br>", unsafe_allow_html=True)
    diagnose_clicked = st.button(">>> INITIALIZE_DIAGNOSTIC_SEQUENCE", use_container_width=True)


# ──────────────────────────────────────────────────────────────
# 5. MAIN EXECUTION (Controller Logic)
# ──────────────────────────────────────────────────────────────

if diagnose_clicked:
    # 1. Capture Domain Model Input
    telemetry = TelemetryInput(
        cpu=cpu,
        gpu=gpu,
        ram=(ram or "").strip() if (ram or "").strip() else "Not specified",
        storage=storage,
        os_name=os_name,
        application=application,
        symptoms=(symptoms or "").strip() if (symptoms or "").strip() else "Not specified"
    )

    try:
        # 2. Spin up the specific business logic application service
        service = DiagnosticsService()

        # 3. Present Feedback
        with st.spinner(""):
            st.markdown(
                """
                <div style="font-family:var(--font-mono); color:var(--text-muted); font-size:0.85rem; text-transform:uppercase; margin-bottom:2rem;">
                    >>> EXECUTING DIAGNOSTIC PROTOCOL...<br>
                    [■■■■■■■■■■□□□□□□]
                </div>
                """,
                unsafe_allow_html=True,
            )
            # 4. Invoke Core Domain Use Case
            result = service.run_diagnostics(telemetry)

        # 5. Render Response
        render_full_results(result)

    except ZenithException as internal_err:
        render_error(type(internal_err).__name__, str(internal_err))
    except Exception as raw_sys_err:
        render_error("UNHANDLED_SYSTEM_FAULT", f"A critical unhandled error occurred: {raw_sys_err}")

else:
    st.markdown(
        """
        <div style="padding:4rem 0; color:var(--text-muted); font-family:var(--font-mono); font-size:0.9rem;">
            >>> AWAITING_INPUT<br><br>
            [ PLEASE CONFIGURE SYSTEM TELEMETRY ABOVE ]
        </div>
        """,
        unsafe_allow_html=True
    )

# ──────────────────────────────────────────────────────────────
# 6. FOOTER
# ──────────────────────────────────────────────────────────────

st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; padding:1rem 0; color:var(--text-muted); font-size:0.75rem; letter-spacing:0.5px;">
        <span style="color:var(--text-main); font-weight:600;">ZENITH DIAGNOSTICS</span> • All recommendations are safe & reversible<br>
        <span style="color:var(--status-green);">✓</span> No hardware modifications
        <span style="color:var(--border-main); margin:0 0.5rem;">|</span>
        <span style="color:var(--status-green);">✓</span> No permanent changes
        <span style="color:var(--border-main); margin:0 0.5rem;">|</span>
        <span style="color:var(--status-green);">✓</span> Always reversible
    </div>
    """,
    unsafe_allow_html=True,
)
