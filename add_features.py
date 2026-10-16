import re

# ==========================================
# 1. UPDATE CSS
# ==========================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make cards more distinct by lightening them slightly and adding a bright thin border
css = css.replace('--card-bg: rgba(10,15,36,0.6);', '--card-bg: rgba(30, 40, 70, 0.7);')
css = css.replace('--glass-bg: rgba(10,15,36,0.7);', '--glass-bg: rgba(20, 30, 60, 0.85);')

if "/* ===== PROGRESS BAR ===== */" not in css:
    css += """
/* ===== PROGRESS BAR ===== */
#scrollProgress {
  position: fixed;
  top: 0;
  left: 0;
  height: 4px;
  background: #3b82f6;
  box-shadow: 0 0 10px #3b82f6, 0 0 20px #818cf8;
  width: 0%;
  z-index: 9999999;
  transition: width 0.1s ease-out;
}

/* ===== MARQUEE ===== */
.marquee-container {
  overflow: hidden;
  white-space: nowrap;
  width: 100%;
  background: var(--nav-bg);
  padding: 15px 0;
  border-top: 1px solid var(--glass-border);
  border-bottom: 1px solid var(--glass-border);
  margin-top: 30px;
  position: relative;
}

.marquee-content {
  display: inline-block;
  animation: scrollMarquee 25s linear infinite;
}

.marquee-content span {
  display: inline-block;
  margin: 0 30px;
  font-size: 1.2rem;
  font-weight: 600;
  color: var(--text);
  font-family: 'Space Grotesk', sans-serif;
  letter-spacing: 1px;
}

.marquee-content span i {
  color: #3b82f6;
  margin-right: 8px;
}

@keyframes scrollMarquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); } /* Scrolls exactly half to loop perfectly */
}
"""

# Make sure normal glass cards have a visible border
css = css.replace('border: 1px solid var(--glass-border);', 'border: 1px solid rgba(255, 255, 255, 0.15); box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);')
# Fix the glow card border to be more distinct too
css = css.replace('border: 1.5px solid transparent !important;', 'border: 1.5px solid rgba(255, 255, 255, 0.1) !important;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# ==========================================
# 2. UPDATE HTML
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="scrollProgress"' not in html:
    html = html.replace('<body>', '<body>\n  <div id="scrollProgress"></div>')

marquee_html = """
    <!-- Marquee -->
    <div class="marquee-container">
      <div class="marquee-content">
        <!-- Original set -->
        <span><i>⚡</i> C++</span>
        <span><i>⚡</i> Python</span>
        <span><i>⚡</i> MATLAB</span>
        <span><i>⚡</i> Arduino IDE</span>
        <span><i>⚡</i> Proteus</span>
        <span><i>⚡</i> IoT Development</span>
        <span><i>⚡</i> Embedded Systems</span>
        <span><i>⚡</i> Machine Learning</span>
        <span><i>⚡</i> YOLO</span>
        <!-- Duplicated set for seamless infinite loop -->
        <span><i>⚡</i> C++</span>
        <span><i>⚡</i> Python</span>
        <span><i>⚡</i> MATLAB</span>
        <span><i>⚡</i> Arduino IDE</span>
        <span><i>⚡</i> Proteus</span>
        <span><i>⚡</i> IoT Development</span>
        <span><i>⚡</i> Embedded Systems</span>
        <span><i>⚡</i> Machine Learning</span>
        <span><i>⚡</i> YOLO</span>
      </div>
    </div>
"""

# Insert marquee after the about section container
if 'marquee-container' not in html:
    html = html.replace('</section>\n\n  <!-- ===== PORTFOLIO SECTION ===== -->', marquee_html + '\n  </section>\n\n  <!-- ===== PORTFOLIO SECTION ===== -->')

html = html.replace('style.css?v=11', 'style.css?v=12')
html = html.replace('script.js?v=9', 'script.js?v=10')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ==========================================
# 3. UPDATE JS
# ==========================================
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

features_js = """
/* ===== SCROLL PROGRESS BAR ===== */
const progressBar = document.getElementById('scrollProgress');
window.addEventListener('scroll', () => {
  if (!progressBar) return;
  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (scrollTop / scrollHeight) * 100;
  progressBar.style.width = scrolled + '%';
});

/* ===== UI SOUND EFFECTS ===== */
const AudioContext = window.AudioContext || window.webkitAudioContext;
let audioCtx;

function initAudio() {
  if (!audioCtx) {
    audioCtx = new AudioContext();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

function playHoverSound() {
  if (!audioCtx) return;
  const osc = audioCtx.createOscillator();
  const gainNode = audioCtx.createGain();
  
  osc.type = 'sine';
  osc.frequency.setValueAtTime(600, audioCtx.currentTime); // futuristic high beep
  osc.frequency.exponentialRampToValueAtTime(1000, audioCtx.currentTime + 0.05);
  
  gainNode.gain.setValueAtTime(0.015, audioCtx.currentTime); // Very quiet and subtle
  gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.05);
  
  osc.connect(gainNode);
  gainNode.connect(audioCtx.destination);
  
  osc.start();
  osc.stop(audioCtx.currentTime + 0.05);
}

// Add event listeners to all interactive elements for the sound
// We init AudioContext on first user interaction (click/mousemove) because browsers block audio otherwise
document.addEventListener('mousemove', initAudio, { once: true });
document.addEventListener('click', initAudio, { once: true });

document.querySelectorAll('a, button, .glass-card, .animated-glow-card').forEach(el => {
  el.addEventListener('mouseenter', () => {
    playHoverSound();
  });
});
"""

if "SCROLL PROGRESS BAR" not in js:
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write('\n' + features_js)

print("Features 2, 3, 4 added and box styles updated.")
