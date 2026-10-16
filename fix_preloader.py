import sys
import re

# 1. HTML Update
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Strip out old preloader HTML
html = re.sub(r'<!-- ===== PRELOADER ===== -->.*?</div>\s*<!-- Starfield Canvas -->', '<!-- Starfield Canvas -->', html, flags=re.DOTALL)

# Insert the exact new preloader
new_preloader = '''<!-- ===== PRELOADER ===== -->
  <div id="preloader" style="position:fixed;inset:0;background:#020205;z-index:999999;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;transition:opacity 0.8s ease-out;">
    <canvas id="lightningCanvas" style="position:absolute;inset:0;pointer-events:none;"></canvas>
    
    <div style="position:relative;z-index:2;text-align:center;pointer-events:none;">
      <h1 style="color:#e2e8f0;font-size:clamp(2rem, 5vw, 4rem);text-shadow:0 0 10px rgba(255,255,255,0.5), 0 0 20px rgba(255,255,255,0.3);margin:0;letter-spacing:3px;font-family:'Space Grotesk',sans-serif;text-transform:uppercase;">Welcome To My</h1>
      <h1 style="color:#3b82f6;font-size:clamp(2.5rem, 6vw, 5rem);text-shadow:0 0 15px rgba(59,130,246,0.8), 0 0 30px rgba(59,130,246,0.5);margin:10px 0 0 0;letter-spacing:3px;font-family:'Space Grotesk',sans-serif;text-transform:uppercase;">Portfolio Website</h1>
      
      <div style="margin-top:50px;display:flex;align-items:center;justify-content:center;gap:20px;font-family:'Space Grotesk',sans-serif;color:white;font-size:1.2rem;font-weight:bold;letter-spacing:2px;">
        <span>Loading</span>
        <div style="width:250px;height:4px;background:rgba(255,255,255,0.2);position:relative;border-radius:2px;overflow:hidden;">
          <div id="loadingBar" style="width:0%;height:100%;background:#3b82f6;box-shadow:0 0 10px #3b82f6;transition:width 0.2s ease;"></div>
        </div>
        <span id="loadingPercent" style="width:50px;text-align:left;">0%</span>
      </div>
    </div>
  </div>
  
  '''

html = html.replace('<body>', '<body>\n  ' + new_preloader)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. JS Update
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove old preloader JS
js = re.sub(r'/\* ===== PRELOADER LOGIC ===== \*/.*?(?=$)', '', js, flags=re.DOTALL)

# Insert the epic Canvas Lightning JS
epic_js = '''
/* ===== PRELOADER LOGIC ===== */
const lCanvas = document.getElementById('lightningCanvas');
if(lCanvas) {
  const lCtx = lCanvas.getContext('2d');
  
  function resizeLCanvas() {
    lCanvas.width = window.innerWidth;
    lCanvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeLCanvas);
  resizeLCanvas();

  function drawLightning() {
    if(!document.getElementById('preloader')) return; // stop if preloader removed
    
    // fade out previous frame slightly to create trailing effect, or clear completely
    lCtx.fillStyle = 'rgba(2, 2, 5, 0.4)';
    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    
    // Random pause between strikes
    if(Math.random() > 0.4) {
      setTimeout(() => requestAnimationFrame(drawLightning), 30);
      return;
    }

    // Main bolt
    const startX = lCanvas.width / 2 + (Math.random() - 0.5) * 400;
    let x = startX;
    let y = 0;
    
    lCtx.beginPath();
    lCtx.moveTo(x, y);
    lCtx.strokeStyle = gba(150, 210, 255, );
    lCtx.lineWidth = Math.random() * 5 + 2;
    lCtx.shadowBlur = 30;
    lCtx.shadowColor = '#3b82f6';
    
    while(y < lCanvas.height) {
      x += (Math.random() - 0.5) * 80; // horizontal zig-zag
      y += Math.random() * 50; // vertical step
      lCtx.lineTo(x, y);
      
      // Branching
      if(Math.random() < 0.15) {
        let bx = x, by = y;
        lCtx.beginPath();
        lCtx.moveTo(bx, by);
        lCtx.strokeStyle = gba(100, 180, 255, );
        lCtx.lineWidth = Math.random() * 2 + 1;
        for(let i=0; i<8; i++) {
          bx += (Math.random() - 0.5) * 60;
          by += Math.random() * 40;
          lCtx.lineTo(bx, by);
        }
        lCtx.stroke();
        
        // restore main bolt styling
        lCtx.beginPath();
        lCtx.moveTo(x, y);
        lCtx.strokeStyle = gba(150, 210, 255, );
        lCtx.lineWidth = Math.random() * 5 + 2;
      }
    }
    lCtx.stroke();
    
    // Background flash effect
    if(Math.random() < 0.2) {
      lCtx.fillStyle = gba(59, 130, 246, 0.15);
      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    }
    
    setTimeout(() => requestAnimationFrame(drawLightning), 50);
  }
  
  drawLightning();
  
  // Progress Bar Logic
  const lBar = document.getElementById('loadingBar');
  const lPercent = document.getElementById('loadingPercent');
  let progress = 0;
  
  const pInterval = setInterval(() => {
    progress += Math.random() * 12; // random increment
    if(progress >= 100) progress = 100;
    
    lBar.style.width = progress + '%';
    lPercent.textContent = Math.floor(progress) + '%';
    
    if(progress === 100) {
      clearInterval(pInterval);
      setTimeout(() => {
        const preloader = document.getElementById('preloader');
        preloader.style.opacity = '0';
        setTimeout(() => {
          preloader.remove();
          document.body.classList.add('loaded');
        }, 800);
      }, 500); // short pause at 100%
    }
  }, 150); // tick every 150ms
}
'''

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(epic_js)


# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('style.css?v=6', 'style.css?v=7')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Epic photorealistic canvas lightning preloader added.")
