import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Find the first occurrence of PRELOADER LOGIC and truncate the string there
idx = js.find('/* ===== PRELOADER LOGIC ===== */')
if idx != -1:
    js = js[:idx].strip() + '\n\n'

# Add the correct Canvas Lightning JS
epic_js = """
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
    lCtx.strokeStyle = `rgba(150, 210, 255, ${Math.random() * 0.5 + 0.5})`;
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
        lCtx.strokeStyle = `rgba(100, 180, 255, ${Math.random() * 0.4 + 0.2})`;
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
        lCtx.strokeStyle = `rgba(150, 210, 255, ${Math.random() * 0.5 + 0.5})`;
        lCtx.lineWidth = Math.random() * 5 + 2;
      }
    }
    lCtx.stroke();
    
    // Background flash effect
    if(Math.random() < 0.2) {
      lCtx.fillStyle = `rgba(59, 130, 246, 0.15)`;
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
"""

js += epic_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('script.js?v=2', 'script.js?v=3')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed script.js syntax errors and cleaned up preloader logic.")
