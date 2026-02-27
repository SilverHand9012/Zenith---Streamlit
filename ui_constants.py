"""
Zenith — UI Constants.

Contains the application's CSS theme (BRUTALIST_CSS) and the
Gemini system prompt (SYSTEM_PROMPT). These are static strings
with no runtime dependencies.
"""

BRUTALIST_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

/* ── Root Variables ── */
:root {
    --bg-page: #0f1011;
    --bg-surface: #16171a;
    --border-main: #333333;
    --border-light: rgba(255, 255, 255, 0.15);
    --border-focus: #ffffff;
    --text-main: #ffffff;
    --text-muted: #8a8d91;
    --text-dim: #5c6065;
    --status-red: #ff4a4a;
    --status-amber: #fca311;
    --status-green: #38b000;
    --status-cyan: #00d2ff;
    --radius-none: 0px !important;
    --font-heading: 'Space Grotesk', sans-serif;
    --font-mono: 'JetBrains Mono', 'Courier New', monospace;
}

/* ── Global Reset ── */
.stApp {
    background: var(--bg-page) !important;
    color: var(--text-main) !important;
    font-family: var(--font-heading) !important;
    background-image: linear-gradient(var(--border-light) 1px, transparent 1px),
                      linear-gradient(90deg, var(--border-light) 1px, transparent 1px);
    background-size: 40px 40px;
    background-position: center center;
}

/* ── Main Content Area ── */
.block-container {
    padding: 3rem 2rem 5rem 2rem !important;
    max-width: 100% !important;
}

/* ── Sidebar (Hidden/Removed) ── */
section[data-testid="stSidebar"] {
    display: none !important;
}

/* ── Headers ── */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading) !important;
    color: var(--text-main) !important;
    font-weight: 500 !important;
    letter-spacing: -0.02em;
}

h1 { font-size: 4rem !important; margin: 0; line-height: 1; }
h2 { font-size: 1.8rem !important; border-top: 1px solid var(--border-main); padding-top: 1rem; border-bottom: 1px solid var(--border-main); padding-bottom: 1rem; margin-bottom: 1.5rem; text-transform: uppercase;}
h3 { font-size: 1.2rem !important; color: var(--text-main) !important; font-family: var(--font-mono) !important; text-transform: uppercase; padding: 1rem; border: 1px solid var(--border-main); background: var(--bg-surface); margin-top: 2rem;}

/* ── Text Input / Text Area ── */
.stTextInput input, .stTextArea textarea {
    background-color: var(--bg-surface) !important;
    color: var(--text-main) !important;
    border: 1px solid var(--border-main) !important;
    font-family: var(--font-mono) !important;
    font-size: 1.1rem !important;
    border-radius: var(--radius-none) !important;
    padding: 1rem 1.2rem !important;
    box-shadow: none !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--border-focus) !important;
    background-color: #000000 !important;
}

/* ── Selectbox / Dropdown ── */
div[data-baseweb="select"] > div {
    background-color: var(--bg-surface) !important;
    color: var(--text-main) !important;
    border: 1px solid var(--border-main) !important;
    border-radius: var(--radius-none) !important;
    font-family: var(--font-mono) !important;
    font-size: 1.1rem !important;
}

div[data-baseweb="select"] > div:hover,
div[data-baseweb="select"] > div:focus-within {
    border-color: var(--border-focus) !important;
    background-color: #000000 !important;
}

div[data-baseweb="popover"] > div {
    background-color: var(--bg-surface) !important;
    border: 1px solid var(--border-main) !important;
    border-radius: var(--radius-none) !important;
}

div[data-baseweb="popover"] ul {
    background-color: var(--bg-surface) !important;
}

div[data-baseweb="popover"] li {
    font-family: var(--font-mono) !important;
    color: var(--text-main) !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: var(--border-main) !important;
    color: var(--border-focus) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: var(--text-main) !important;
    color: var(--bg-page) !important;
    border: 1px solid var(--text-main) !important;
    font-family: var(--font-heading) !important;
    font-size: 1.3rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px;
    padding: 1.2rem !important;
    border-radius: var(--radius-none) !important;
    transition: all 0.2s ease;
    text-transform: uppercase;
}

.stButton > button:hover {
    background: transparent !important;
    color: var(--text-main) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background-color: transparent !important;
    color: var(--text-main) !important;
    border: 1px solid var(--border-main) !important;
    border-radius: var(--radius-none) !important;
    font-family: var(--font-mono) !important;
    text-transform: uppercase;
}

.streamlit-expanderContent {
    background-color: var(--bg-surface) !important;
    border: 1px solid var(--border-main) !important;
    border-top: none !important;
    border-radius: var(--radius-none) !important;
}

/* ── Status / Alert Containers ── */
div[data-testid="stAlert"] {
    background-color: transparent !important;
    border: 1px solid var(--border-main) !important;
    border-radius: var(--radius-none) !important;
    border-left: 4px solid var(--text-main) !important;
}

/* ── Divider ── */
hr {
    border-color: var(--border-main) !important;
    margin: 1.5rem 0;
}

/* ── Glass Morphism Result Card -> Brutalist Cell ── */
.result-card {
    background: transparent;
    border: 1px solid var(--border-main);
    border-radius: var(--radius-none);
    padding: 1.5rem;
    margin: 1rem 0;
    position: relative;
    transition: all 0.2s ease;
}

.result-card:hover {
    background: var(--bg-surface);
    border-color: #555555;
}

/* ── Severity Bar ── */
.severity-bar-track {
    width: 100%;
    height: 12px;
    background-color: transparent;
    border: 1px solid var(--border-main);
    margin: 1rem 0;
}

.severity-bar-fill {
    height: 100%;
    background-color: var(--text-main);
}

/* ── Soft Pill Badges -> Hard Brackets ── */
.badge {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    font-family: var(--font-mono);
    border: 1px solid var(--border-main);
    background: transparent !important;
}

.badge-bottleneck { color: var(--status-red); border-color: var(--status-red); }
.badge-safe { color: var(--status-green); border-color: var(--status-green); }
.badge-caution { color: var(--status-amber); border-color: var(--status-amber); }
.badge-risky { color: var(--status-red); border-color: var(--status-red); }
.badge-type { color: var(--status-cyan); border-color: var(--status-cyan); }

/* ── Terminal Prompt ── */
.terminal-prompt {
    color: var(--status-cyan);
    font-family: var(--font-mono);
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}
.terminal-prompt::before {
    content: "> ";
    color: var(--text-dim);
}

/* ── Warning Card ── */
.warning-card {
    background: transparent;
    border: 1px solid var(--status-red);
    border-radius: var(--radius-none);
    padding: 1.2rem;
    margin: 1rem 0;
}

/* ── Tweak Card ── */
.tweak-card {
    background: transparent;
    border: 1px solid var(--border-main);
    border-radius: var(--radius-none);
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.2s ease;
}
.tweak-card:hover {
    border-color: #555555;
    background: var(--bg-surface);
}

/* ── Command Block ── */
.cmd-block {
    background-color: transparent;
    border: 1px solid var(--border-main);
    border-radius: var(--radius-none);
    padding: 1rem;
    margin: 1rem 0;
    font-family: var(--font-mono);
    font-size: 0.85rem;
    color: var(--text-main);
}

/* ── QF Network Inspired Header Nav ── */
.qf-nav-grid {
    display: flex;
    border-bottom: 1px solid var(--border-main);
    border-top: 1px solid var(--border-main);
    margin-bottom: 2rem;
    margin-top: -3rem; /* pull up */
    padding-top: 0;
}
.qf-nav-item {
    padding: 1.2rem 2rem;
    border-right: 1px solid var(--border-main);
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 1.5rem;
    letter-spacing: 2px;
    display: flex;
    align-items: center;
}
.qf-nav-link {
    padding: 1.2rem 1.5rem;
    border-right: 1px solid var(--border-main);
    font-family: var(--font-mono);
    font-size: 0.8rem;
    color: var(--text-muted);
    text-transform: uppercase;
    display: flex;
    align-items: center;
}

/* ── Header Area ── */
.header-banner {
    padding: 2rem 0;
    margin-bottom: 0;
    display: flex;
    flex-direction: column;
}

.brutalist-title {
    font-family: var(--font-heading) !important;
    font-size: 4.5rem !important;
    font-weight: 500 !important;
    letter-spacing: -0.02em;
    color: var(--text-main) !important;
    margin: 0 !important;
    line-height: 1.05 !important;
}

.header-subtitle {
    color: var(--text-muted);
    font-family: var(--font-mono);
    font-size: 1rem;
    max-width: 700px;
    line-height: 1.6;
    padding: 2rem 0;
}

/* ── Form Section Grid ── */
.stTextInput p, .stSelectbox p, .stTextArea p, div[data-testid="stWidgetLabel"] p, label {
    font-family: var(--font-mono) !important;
    color: var(--text-main) !important;
    text-transform: uppercase;
    font-size: 0.85rem !important;
    letter-spacing: 1px;
}

/* ── Hide Streamlit Defaults ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] { background-color: transparent !important; }
</style>
"""

SYSTEM_PROMPT = """\
You are ZENITH — an expert-level system performance diagnostics engine.

Your job: Given a user's hardware specs, operating system, target application/game, \
and symptom description, perform a structured 5-step bottleneck analysis and return \
exactly 3 safe, reversible optimization recommendations.

## Diagnostic Sequence

0. **CRITICAL OS/PLATFORM CHECK** — Before analyzing hardware, you MUST check if the \
target application is fundamentally incompatible with the reported Operating System. \
Examples include: Valorant (Vanguard anti-cheat) on Linux/macOS, Windows-exclusive \
software on macOS without translation layers, or 32-bit apps on macOS Catalina+. \
If a hard incompatibility exists, IMMEDIATELY classify the bottleneck as "Software", \
set severity to 10, set compatibility score to 0, and explain the blocker in plain English. \
Do not provide hardware optimization tweaks for a fundamentally incompatible OS.
1. **Resource Classification** — Classify CPU, GPU, RAM, and Storage capabilities \
relative to the target application's requirements.
2. **Symptom Mapping** — Map the user's reported symptoms to probable resource \
bottleneck categories (CPU-bound, GPU-bound, RAM-starved, I/O-bound, thermal, \
software/driver, mixed).
3. **Bottleneck Determination** — Identify the primary bottleneck with a severity \
score (1-10), and optionally a secondary bottleneck.
4. **Safety-Constrained Recommendations** — Provide exactly 3 optimization tweaks. \
Each must be:
   - Safe to apply (no risk of data loss or hardware damage)
   - Fully reversible (user can undo at any time)
   - Within the user's control (no hardware purchases required)
   - Appropriate for the detected OS
   - **ENGINE/MOD FIXES:** If the target application is known to be poorly optimized at the engine level (e.g., Minecraft Java, Skyrim) and deeply relies on community performance mods (e.g., Sodium, Iris, Optifine), you MUST recommend installing the modern standard mods to fix the engine bottleneck if relevant to the user's symptoms.
   - **CRITICAL:** You MUST provide a valid shell/PowerShell/terminal command in the `commands` array if the tweak can be executed or initiated via CLI (e.g., `SystemPropertiesAdvanced.exe` for Windows Virtual Memory). Do not rely solely on GUI click steps if a command exists.
5. **Explicit Non-Recommendations** — List 2 things the user should NOT do, with \
reasons why.

## Hard Constraints

- NEVER recommend overclocking beyond manufacturer specs
- NEVER recommend disabling security software permanently
- NEVER recommend registry hacks without backup steps (Windows)
- NEVER recommend disabling Windows Update (Windows)
- NEVER recommend running commands as root/admin unless absolutely necessary, \
and always explain the risk
- NEVER recommend deleting system files
- Every recommendation MUST include a revert/undo step
- If you cannot determine the bottleneck with confidence, say so

## Output Format

Return a strictly valid JSON object with this exact schema — no markdown, no \
explanation outside the JSON:

{
  "diagnosis": {
    "bottleneck_type": "CPU | GPU | RAM | Storage | Thermal | Software | Mixed",
    "severity": <integer 1-10>,
    "secondary_bottleneck": "<type or null>",
    "plain_english": "<2-3 sentence human-readable diagnosis>",
    "reasoning": "<technical reasoning for this determination>"
  },
  "compatibility": {
    "score": <integer 1-100>,
    "note": "<one-line compatibility summary>"
  },
  "tweaks": [
    {
      "title": "<short descriptive title>",
      "type": "Software | OS | Driver | Config | In-App",
      "safety": "Safe | Caution | Advanced",
      "steps": ["<step 1>", "<step 2>", "..."],
      "commands": ["<CLI/PowerShell/terminal command to apply tweak>", "<another command>"],
      "revert": "<how to undo this tweak>",
      "rationale": "<why this helps for the diagnosed bottleneck>"
    }
  ],
  "do_not_do": [
    {
      "action": "<what NOT to do>",
      "reason": "<why it's dangerous or counterproductive>"
    }
  ]
}
"""
