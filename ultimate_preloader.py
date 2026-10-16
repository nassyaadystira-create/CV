import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the entire PRELOADER LOGIC block
idx = js.find('/* ===== PRELOADER LOGIC ===== */')
if idx != -1:
    js = js[:idx].strip() + '\n\n'

smooth_js = """
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

  let bolts = [];

  class Bolt {
    constructor() {
      this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 200;
      this.y = 0;
      this.path = [{x: this.x, y: this.y}];
      this.active = true;
      this.color = `rgba(100, 150, 255, ${Math.random() * 0.4 + 0.6})`;
      this.lineWidth = Math.random() * 4 + 2;
    }
    
    update() {
      if(!this.active) return;
      
      // snake downwards smoothly
      let lastPoint = this.path[this.path.length - 1];
      let newX = lastPoint.x + (Math.random() - 0.5) * 40;
      let newY = lastPoint.y + Math.random() * 30 + 10;
      
      this.path.push({x: newX, y: newY});
      
      if(newY > lCanvas.height) {
        this.active = false; // finished striking
      }
    }
    
    draw(ctx) {
      if(this.path.length < 2) return;
      ctx.beginPath();
      ctx.moveTo(this.path[0].x, this.path[0].y);
      for(let i=1; i<this.path.length; i++) {
        ctx.lineTo(this.path[i].x, this.path[i].y);
      }
      ctx.strokeStyle = this.color;
      ctx.lineWidth = this.lineWidth;
      ctx.shadowBlur = 40;
      ctx.shadowColor = '#4f46e5';
      ctx.stroke();
    }
  }

  function animateLightning() {
    if(!document.getElementById('preloader')) return;
    
    // Very smooth trailing fade (galaxy dark background)
    lCtx.fillStyle = 'rgba(2, 2, 6, 0.2)';
    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    
    // Occasionally spawn a new main bolt
    if(Math.random() < 0.1 && bolts.filter(b => b.active).length < 2) {
      bolts.push(new Bolt());
    }
    
    // Occasional background flash for galaxy storm feel
    if(Math.random() < 0.05) {
      lCtx.fillStyle = 'rgba(40, 30, 120, 0.05)';
      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    }
    
    // Remove old bolts that finished striking a while ago
    if(bolts.length > 5) bolts.shift();
    
    bolts.forEach(bolt => {
      for(let i=0; i<3; i++) bolt.update(); // draw 3 segments per frame for speed
      bolt.draw(lCtx);
    });
    
    requestAnimationFrame(animateLightning);
  }
  
  animateLightning();
  
  // Progress Bar Logic
  const lBar = document.getElementById('loadingBar');
  const lPercent = document.getElementById('loadingPercent');
  let progress = 0;
  
  const pInterval = setInterval(() => {
    progress += Math.random() * 8; // smooth increment
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
      }, 500);
    }
  }, 120);
}
"""

js += smooth_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update text to look like particles and cache buster
html = html.replace('script.js?v=4', 'script.js?v=5')

# Make the text look like dotted particles as in the screenshot
html = html.replace('color:#e2e8f0;font-size:clamp(2rem, 5vw, 4rem);text-shadow:0 0 10px rgba(255,255,255,0.5), 0 0 20px rgba(255,255,255,0.3);', 'color:transparent;background-image:radial-gradient(circle, #e2e8f0 35%, transparent 35%);background-size:6px 6px;-webkit-background-clip:text;font-size:clamp(2rem, 5vw, 4rem);filter:drop-shadow(0 0 5px rgba(255,255,255,0.8));')

html = html.replace('color:#818cf8;font-size:clamp(2.5rem, 6vw, 5rem);text-shadow:0 0 15px rgba(79,70,229,0.8), 0 0 30px rgba(79,70,229,0.5);', 'color:transparent;background-image:radial-gradient(circle, #818cf8 35%, transparent 35%);background-size:6px 6px;-webkit-background-clip:text;font-size:clamp(2.5rem, 6vw, 5rem);filter:drop-shadow(0 0 8px rgba(79,70,229,0.8));')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Smoothed out lightning, added dotted particle text, changed to 60fps requestAnimationFrame.")
