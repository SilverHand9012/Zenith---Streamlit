"""
Zenith — Embedded HTML/JS Components.

Contains self-contained HTML documents rendered via Streamlit's
components.html(). These are purely visual and carry no application state.
"""

HARDWARE_TOPOLOGY_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
  body { 
      margin: 0; 
      overflow: hidden; 
      background-color: transparent; 
      color: #ffffff; 
      font-family: 'JetBrains Mono', monospace; 
  }
  .topology-container {
      width: 100%;
      height: 100%;
      border: 1px solid #1a1b1d;
      box-sizing: border-box;
      margin-top: 2rem;
      position: relative;
      background:
          linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
          linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
      background-size: 30px 30px;
  }
  svg { width: 100%; height: 100%; }

  /* Connection lines — subtle pulse */
  .topo-line {
      stroke: #555;
      stroke-width: 1;
      opacity: 0.4;
      animation: line-pulse 4s ease-in-out infinite alternate;
  }
  .topo-line:nth-child(even) { animation-delay: -2s; }
  .topo-line:nth-child(3n)   { animation-delay: -1s; }

  @keyframes line-pulse {
      0%   { opacity: 0.15; }
      100% { opacity: 0.5; }
  }

  /* Node outer glow */
  .node-glow {
      fill: rgba(255,255,255,0.08);
      animation: glow-pulse 3s ease-in-out infinite alternate;
  }
  .node-glow:nth-of-type(even) { animation-delay: -1.5s; }

  @keyframes glow-pulse {
      0%   { r: 7; opacity: 0.05; }
      100% { r: 10; opacity: 0.15; }
  }

  /* Node dots */
  .node-dot-compute { fill: #ffffff; }
  .node-dot-accel   { fill: #888888; }
  .node-dot-mem     { fill: #333333; stroke: #ffffff; stroke-width: 1; }
  .node-dot-bus     { fill: #555555; stroke: #ffffff; stroke-width: 1; }
  .node-dot-net     { fill: #444444; stroke: #ffffff; stroke-width: 1; }

  /* Labels */
  .node-label {
      fill: #8a8d91;
      font-size: 9px;
      font-family: 'JetBrains Mono', monospace;
      text-anchor: middle;
  }
</style>
</head>
<body>
<div class="topology-container">
<svg viewBox="0 0 480 240" preserveAspectRatio="xMidYMid meet">
  <!-- Connection lines -->
  <line class="topo-line" x1="80"  y1="60"  x2="180" y2="45"  />
  <line class="topo-line" x1="80"  y1="60"  x2="150" y2="130" />
  <line class="topo-line" x1="180" y1="45"  x2="280" y2="70"  />
  <line class="topo-line" x1="180" y1="45"  x2="150" y2="130" />
  <line class="topo-line" x1="150" y1="130" x2="280" y2="70"  />
  <line class="topo-line" x1="150" y1="130" x2="240" y2="180" />
  <line class="topo-line" x1="280" y1="70"  x2="380" y2="50"  />
  <line class="topo-line" x1="280" y1="70"  x2="350" y2="140" />
  <line class="topo-line" x1="380" y1="50"  x2="420" y2="130" />
  <line class="topo-line" x1="350" y1="140" x2="420" y2="130" />
  <line class="topo-line" x1="350" y1="140" x2="240" y2="180" />
  <line class="topo-line" x1="240" y1="180" x2="100" y2="200" />
  <line class="topo-line" x1="100" y1="200" x2="80"  y2="60"  />
  <line class="topo-line" x1="420" y1="130" x2="400" y2="210" />
  <line class="topo-line" x1="240" y1="180" x2="400" y2="210" />

  <!-- Nodes: glow + dot + label -->
  <!-- CPU_CORE_0 -->
  <circle class="node-glow" cx="80"  cy="60"  r="8" />
  <circle class="node-dot-compute" cx="80"  cy="60"  r="4" />
  <text class="node-label" x="80"  y="45">CPU_CORE_0</text>

  <!-- CPU_CORE_1 -->
  <circle class="node-glow" cx="180" cy="45"  r="8" />
  <circle class="node-dot-compute" cx="180" cy="45"  r="4" />
  <text class="node-label" x="180" y="30">CPU_CORE_1</text>

  <!-- GPU_CUDA -->
  <circle class="node-glow" cx="280" cy="70"  r="8" />
  <circle class="node-dot-accel" cx="280" cy="70"  r="4" />
  <text class="node-label" x="280" y="55">GPU_CUDA</text>

  <!-- SYS_MEM -->
  <circle class="node-glow" cx="150" cy="130" r="8" />
  <circle class="node-dot-mem" cx="150" cy="130" r="4" />
  <text class="node-label" x="150" y="115">SYS_MEM</text>

  <!-- NPU_ACCEL -->
  <circle class="node-glow" cx="380" cy="50"  r="8" />
  <circle class="node-dot-accel" cx="380" cy="50"  r="4" />
  <text class="node-label" x="380" y="35">NPU_ACCEL</text>

  <!-- L3_CACHE -->
  <circle class="node-glow" cx="420" cy="130" r="8" />
  <circle class="node-dot-mem" cx="420" cy="130" r="4" />
  <text class="node-label" x="420" y="115">L3_CACHE</text>

  <!-- BUS_CTRL -->
  <circle class="node-glow" cx="350" cy="140" r="8" />
  <circle class="node-dot-bus" cx="350" cy="140" r="4" />
  <text class="node-label" x="350" y="125">BUS_CTRL</text>

  <!-- NVME_0 -->
  <circle class="node-glow" cx="240" cy="180" r="8" />
  <circle class="node-dot-mem" cx="240" cy="180" r="4" />
  <text class="node-label" x="240" y="165">NVME_0</text>

  <!-- VRAM_BANK -->
  <circle class="node-glow" cx="100" cy="200" r="8" />
  <circle class="node-dot-mem" cx="100" cy="200" r="4" />
  <text class="node-label" x="100" y="215">VRAM_BANK</text>

  <!-- NET_NIC -->
  <circle class="node-glow" cx="400" cy="210" r="8" />
  <circle class="node-dot-net" cx="400" cy="210" r="4" />
  <text class="node-label" x="400" y="225">NET_NIC</text>
</svg>
</div>
</body>
</html>
"""
