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
  canvas { 
      display: block; 
      width: 100%; 
      height: 100%; 
  }
</style>
</head>
<body>
<canvas id="hardwareCanvas"></canvas>
<script>
  const canvas = document.getElementById('hardwareCanvas');
  const ctx = canvas.getContext('2d');
  
  function resize() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resize);
  resize();

  const hardwareNodes = [
      { id: "CPU_CORE_0", type: "compute" },
      { id: "CPU_CORE_1", type: "compute" },
      { id: "GPU_CUDA", type: "accel" },
      { id: "SYS_MEM", type: "mem" },
      { id: "VRAM_BANK", type: "mem" },
      { id: "NVME_0", type: "storage" },
      { id: "NPU_ACCEL", type: "accel" },
      { id: "L3_CACHE", type: "mem" },
      { id: "BUS_CTRL", type: "bus" },
      { id: "NET_NIC", type: "net" }
  ];

  const nodes = hardwareNodes.map(n => ({
      name: n.id,
      type: n.type,
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 1.0,
      vy: (Math.random() - 0.5) * 1.0,
      pulse: Math.random() * Math.PI * 2,
      pulseSpeed: 0.05 + Math.random() * 0.05
  }));

  let mouse = { x: -1000, y: -1000, active: false };
  window.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      mouse.x = e.clientX - rect.left;
      mouse.y = e.clientY - rect.top;
      mouse.active = true;
  });
  window.addEventListener('mouseleave', () => {
      mouse.active = false;
  });

  // Draw background grid with slight parallax
  function drawGrid() {
      const gridSize = 30;
      const offsetX = mouse.active ? (mouse.x - canvas.width/2) * -0.02 : 0;
      const offsetY = mouse.active ? (mouse.y - canvas.height/2) * -0.02 : 0;
      
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
      ctx.lineWidth = 1;
      
      for(let x = (offsetX % gridSize); x < canvas.width; x += gridSize) {
          ctx.beginPath();
          ctx.moveTo(x, 0);
          ctx.lineTo(x, canvas.height);
          ctx.stroke();
      }
      for(let y = (offsetY % gridSize); y < canvas.height; y += gridSize) {
          ctx.beginPath();
          ctx.moveTo(0, y);
          ctx.lineTo(canvas.width, y);
          ctx.stroke();
      }
  }

  function draw() {
      // Clear with trailing effect
      ctx.fillStyle = 'rgba(15, 16, 17, 0.3)';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      drawGrid();

      // Update nodes
      nodes.forEach(node => {
          node.x += node.vx;
          node.y += node.vy;
          node.pulse += node.pulseSpeed;

          // Bounce off walls softly
          if (node.x <= 30) { node.x = 30; node.vx *= -1; }
          if (node.x >= canvas.width - 30) { node.x = canvas.width - 30; node.vx *= -1; }
          if (node.y <= 30) { node.y = 30; node.vy *= -1; }
          if (node.y >= canvas.height - 30) { node.y = canvas.height - 30; node.vy *= -1; }

          // Mouse interaction (repel + speed up)
          if (mouse.active) {
              const dx = mouse.x - node.x;
              const dy = mouse.y - node.y;
              const dist = Math.sqrt(dx*dx + dy*dy);
              
              if (dist < 150) {
                  const force = (150 - dist) / 150;
                  node.vx -= (dx / dist) * force * 0.5;
                  node.vy -= (dy / dist) * force * 0.5;
                  
                  // Draw interaction line
                  ctx.beginPath();
                  ctx.moveTo(node.x, node.y);
                  ctx.lineTo(mouse.x, mouse.y);
                  ctx.strokeStyle = `rgba(255, 255, 255, ${force * 0.5})`;
                  ctx.lineWidth = 1;
                  ctx.stroke();
              }
          }
          
          // Friction max speed limit
          const speed = Math.sqrt(node.vx*node.vx + node.vy*node.vy);
          if (speed > 2.5) {
              node.vx = (node.vx / speed) * 2.5;
              node.vy = (node.vy / speed) * 2.5;
          }
      });

      // Draw connections
      for (let i = 0; i < nodes.length; i++) {
          for (let j = i + 1; j < nodes.length; j++) {
              const dx = nodes[i].x - nodes[j].x;
              const dy = nodes[i].y - nodes[j].y;
              const distSq = dx*dx + dy*dy;
              
              const connectDist = 30000;
              if (distSq < connectDist) {
                  const opacity = 1 - (distSq / connectDist);
                  ctx.beginPath();
                  ctx.moveTo(nodes[i].x, nodes[i].y);
                  ctx.lineTo(nodes[j].x, nodes[j].y);
                  ctx.strokeStyle = `rgba(136, 136, 136, ${opacity * 0.6})`;
                  ctx.lineWidth = 1.5;
                  ctx.stroke();
                  
                  // Data packet animation (flowing dots along lines)
                  if (Math.random() > 0.98) {
                      const packetX = nodes[i].x - dx * 0.5;
                      const packetY = nodes[i].y - dy * 0.5;
                      ctx.fillStyle = '#ffffff';
                      ctx.fillRect(packetX - 1, packetY - 1, 3, 3);
                  }
              }
          }
      }

      // Draw nodes
      ctx.font = '10px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      
      nodes.forEach(node => {
          // Node glowing pulse size
          const currentRadius = 4 + Math.sin(node.pulse) * 1.5;
          
          // Outer glow
          ctx.beginPath();
          ctx.arc(node.x, node.y, currentRadius + 3, 0, Math.PI * 2);
          ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
          ctx.fill();

          // Main dot
          ctx.beginPath();
          ctx.arc(node.x, node.y, currentRadius, 0, Math.PI * 2);
          
          // Color code by type
          if (node.type === 'compute') ctx.fillStyle = '#ffffff'; // White for CPU
          else if (node.type === 'accel') ctx.fillStyle = '#888888'; // Gray for GPU/NPU
          else ctx.fillStyle = '#111111'; // Dark for mem/storage
          
          ctx.fill();
          ctx.strokeStyle = '#ffffff';
          ctx.lineWidth = 1.5;
          ctx.stroke();

          // Label text
          ctx.fillStyle = '#8a8d91';
          ctx.fillText(node.name, node.x, node.y - 15);
      });

      // Target reticle on mouse
      if (mouse.active) {
          ctx.beginPath();
          ctx.arc(mouse.x, mouse.y, 8, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
          ctx.lineWidth = 1;
          ctx.stroke();
          
          ctx.beginPath();
          ctx.moveTo(mouse.x - 12, mouse.y);
          ctx.lineTo(mouse.x - 4, mouse.y);
          ctx.moveTo(mouse.x + 12, mouse.y);
          ctx.lineTo(mouse.x + 4, mouse.y);
          ctx.moveTo(mouse.x, mouse.y - 12);
          ctx.lineTo(mouse.x, mouse.y - 4);
          ctx.moveTo(mouse.x, mouse.y + 12);
          ctx.lineTo(mouse.x, mouse.y + 4);
          ctx.stroke();
      }

      requestAnimationFrame(draw);
  }
  draw();
</script>
</body>
</html>
"""
