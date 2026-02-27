"""
Zenith — Embedded SVG Components.

Contains inline SVG/HTML rendered via st.markdown(unsafe_allow_html=True).
No iframe (components.html) is used — this prevents iframe re-mount
overhead on Streamlit reruns.
"""

HARDWARE_TOPOLOGY_SVG = """
<div style="border: 1px solid #1a1b1d; margin-top: 2rem; padding: 0.5rem;
            background:
                linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 30px 30px;">
<svg viewBox="0 0 480 240" preserveAspectRatio="xMidYMid meet"
     style="width:100%; height:auto; display:block;"
     xmlns="http://www.w3.org/2000/svg">
  <style>
    .tl { stroke:#555; stroke-width:1; opacity:0.35; }
    .ng { fill:rgba(255,255,255,0.08); }
    .nc { fill:#fff; }
    .na { fill:#888; }
    .nm { fill:#333; stroke:#fff; stroke-width:1; }
    .nb { fill:#555; stroke:#fff; stroke-width:1; }
    .nn { fill:#444; stroke:#fff; stroke-width:1; }
    .nl { fill:#8a8d91; font-size:9px; font-family:'JetBrains Mono',monospace; text-anchor:middle; }
  </style>

  <!-- Connection lines -->
  <line class="tl" x1="80"  y1="60"  x2="180" y2="45"  />
  <line class="tl" x1="80"  y1="60"  x2="150" y2="130" />
  <line class="tl" x1="180" y1="45"  x2="280" y2="70"  />
  <line class="tl" x1="180" y1="45"  x2="150" y2="130" />
  <line class="tl" x1="150" y1="130" x2="280" y2="70"  />
  <line class="tl" x1="150" y1="130" x2="240" y2="180" />
  <line class="tl" x1="280" y1="70"  x2="380" y2="50"  />
  <line class="tl" x1="280" y1="70"  x2="350" y2="140" />
  <line class="tl" x1="380" y1="50"  x2="420" y2="130" />
  <line class="tl" x1="350" y1="140" x2="420" y2="130" />
  <line class="tl" x1="350" y1="140" x2="240" y2="180" />
  <line class="tl" x1="240" y1="180" x2="100" y2="200" />
  <line class="tl" x1="100" y1="200" x2="80"  y2="60"  />
  <line class="tl" x1="420" y1="130" x2="400" y2="210" />
  <line class="tl" x1="240" y1="180" x2="400" y2="210" />

  <!-- CPU_CORE_0 -->
  <circle class="ng" cx="80"  cy="60"  r="8" />
  <circle class="nc" cx="80"  cy="60"  r="4" />
  <text class="nl" x="80"  y="45">CPU_CORE_0</text>

  <!-- CPU_CORE_1 -->
  <circle class="ng" cx="180" cy="45"  r="8" />
  <circle class="nc" cx="180" cy="45"  r="4" />
  <text class="nl" x="180" y="30">CPU_CORE_1</text>

  <!-- GPU_CUDA -->
  <circle class="ng" cx="280" cy="70"  r="8" />
  <circle class="na" cx="280" cy="70"  r="4" />
  <text class="nl" x="280" y="55">GPU_CUDA</text>

  <!-- SYS_MEM -->
  <circle class="ng" cx="150" cy="130" r="8" />
  <circle class="nm" cx="150" cy="130" r="4" />
  <text class="nl" x="150" y="115">SYS_MEM</text>

  <!-- NPU_ACCEL -->
  <circle class="ng" cx="380" cy="50"  r="8" />
  <circle class="na" cx="380" cy="50"  r="4" />
  <text class="nl" x="380" y="35">NPU_ACCEL</text>

  <!-- L3_CACHE -->
  <circle class="ng" cx="420" cy="130" r="8" />
  <circle class="nm" cx="420" cy="130" r="4" />
  <text class="nl" x="420" y="115">L3_CACHE</text>

  <!-- BUS_CTRL -->
  <circle class="ng" cx="350" cy="140" r="8" />
  <circle class="nb" cx="350" cy="140" r="4" />
  <text class="nl" x="350" y="125">BUS_CTRL</text>

  <!-- NVME_0 -->
  <circle class="ng" cx="240" cy="180" r="8" />
  <circle class="nm" cx="240" cy="180" r="4" />
  <text class="nl" x="240" y="165">NVME_0</text>

  <!-- VRAM_BANK -->
  <circle class="ng" cx="100" cy="200" r="8" />
  <circle class="nm" cx="100" cy="200" r="4" />
  <text class="nl" x="100" y="215">VRAM_BANK</text>

  <!-- NET_NIC -->
  <circle class="ng" cx="400" cy="210" r="8" />
  <circle class="nn" cx="400" cy="210" r="4" />
  <text class="nl" x="400" y="225">NET_NIC</text>
</svg>
</div>
"""
