"""
Zenith — Shared JavaScript embedded components.
"""

AUTO_SCROLL_JS = """
<script>
    let attempts = 0;
    const scroller = setInterval(() => {
        try {
            const doc = window.parent.document;
            const headers = Array.from(doc.querySelectorAll('h2'));
            const target = headers.find(h => h.textContent && h.textContent.includes('Diagnosis'));
            
            if (target) {
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                clearInterval(scroller);
            }
            
            attempts++;
            if (attempts > 15) {
                clearInterval(scroller); // Timeout after ~4.5 seconds
            }
        } catch (e) {
            console.error("Auto-scroll error:", e);
            clearInterval(scroller);
        }
    }, 300);
</script>
"""

HOW_TO_USE_DIALOG_HTML = """
<div style="margin-top: 1rem;">
    <button onclick="openHelpDialog()" style="background:transparent; border:1px solid #3d3d3d; color:#e0e0e0; font-family:'JetBrains Mono', monospace; font-size:0.8rem; padding:0.5rem 1rem; cursor:pointer; text-transform:uppercase; letter-spacing:1px; transition: all 0.2s;">
        [HOW_TO_USE_ZENITH_PROTOCOL]
    </button>
</div>

<div id="zenith-help-overlay" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; background:rgba(10,10,12,0.85); z-index:9998; backdrop-filter:blur(4px);"></div>
<div id="zenith-help-dialog" style="display:none; position:fixed; top:50%; left:50%; transform:translate(-50%, -50%); width:600px; max-width:90vw; background:#0f1011; border:1px solid #333; z-index:9999; padding:2rem; box-shadow:0 10px 30px rgba(0,0,0,0.5); font-family:'JetBrains Mono', monospace;">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1.5rem; border-bottom:1px solid #333; padding-bottom:1rem;">
        <h2 style="margin:0; font-size:1.5rem; color:#fff; letter-spacing:-0.03em;">HOW TO USE ZENITH</h2>
        <button onclick="closeHelpDialog()" style="background:transparent; border:none; color:#888; font-size:1.5rem; cursor:pointer; padding:0;">×</button>
    </div>
    <div style="color:#a0a0a0; font-size:0.9rem; line-height:1.6;">
        <p><strong style="color:#fff;">1. INPUT TELEMETRY:</strong> Provide your system's hardware specs (CPU, GPU, RAM) and environment details (OS, Storage).</p>
        <p><strong style="color:#fff;">2. DEFINE TARGET:</strong> Enter the application or game you are trying to run.</p>
        <p><strong style="color:#fff;">3. DESCRIBE ANOMALY:</strong> (Optional) Describe the specific performance issue you are experiencing (e.g., "stuttering in dense areas", "long load times").</p>
        <p><strong style="color:#fff;">4. INITIALIZE:</strong> Click the sequence button. Zenith will analyze the telemetry against its LLM diagnostic engine.</p>
        <p><strong style="color:#fff;">5. REVIEW:</strong> Zenith will output the primary bottleneck, a compatibility score, and safe, reversible optimization tweaks to improve performance.</p>
    </div>
    <div style="margin-top:2rem; text-align:right;">
         <button onclick="closeHelpDialog()" style="background:#fff; color:#000; border:none; padding:0.6rem 1.2rem; font-family:'JetBrains Mono', monospace; font-weight:700; cursor:pointer; font-size:0.9rem;">ACKNOWLEDGE &gt;&gt;</button>
    </div>
</div>

<script>
    function openHelpDialog() {
        const doc = window.parent.document;
        // Inject elements into parent document body if they don't exist
        if (!doc.getElementById('zenith-help-overlay')) {
            const overlay = document.createElement('div');
            overlay.id = 'zenith-help-overlay';
            overlay.innerHTML = document.getElementById('zenith-help-overlay').outerHTML;
            doc.body.appendChild(overlay.firstElementChild);
            
            const dialog = document.createElement('div');
            dialog.id = 'zenith-help-dialog';
            dialog.innerHTML = document.getElementById('zenith-help-dialog').outerHTML;
            doc.body.appendChild(dialog.firstElementChild);

            // Re-bind close function in parent context
            doc.defaultView.closeHelpDialog = function() {
                doc.getElementById('zenith-help-overlay').style.display = 'none';
                doc.getElementById('zenith-help-dialog').style.display = 'none';
            };
        }
        
        doc.getElementById('zenith-help-overlay').style.display = 'block';
        doc.getElementById('zenith-help-dialog').style.display = 'block';
    }
    
    // Bind hover effect
    const btn = document.querySelector('button');
    btn.addEventListener('mouseover', () => {
        btn.style.color = '#fff';
        btn.style.borderColor = '#555';
        btn.style.background = '#1a1b1d';
    });
    btn.addEventListener('mouseout', () => {
        btn.style.color = '#e0e0e0';
        btn.style.borderColor = '#3d3d3d';
        btn.style.background = 'transparent';
    });
</script>
"""
