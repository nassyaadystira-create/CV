import re

# 1. Update HTML Z-Index
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Current canvas: <canvas id="lightningCanvas" style="position:absolute;inset:0;pointer-events:none;"></canvas>
# We need it to be OVER the text. So z-index: 10.
html = html.replace('id="lightningCanvas" style="position:absolute;inset:0;pointer-events:none;"', 'id="lightningCanvas" style="position:absolute;inset:0;pointer-events:none;z-index:10;"')

# Ensure the background is totally black for the galaxy
html = html.replace('background:#020205', 'background:#000002')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update JS to add stars, shooting stars, and brighter core lightning
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('/* ===== PRELOADER LOGIC ===== */')
if idx != -1:
    js = js[:idx].strip() + '\n\n'

advanced_js = """
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
  let stars = [];
  let shootingStars = [];

  // Generate background stars
  for(let i=0; i<150; i++) {
    stars.push({
      x: Math.random() * lCanvas.width,
      y: Math.random() * lCanvas.height,
      radius: Math.random() * 1.5,
      alpha: Math.random(),
      blinkSpeed: Math.random() * 0.05
    });
  }

  class Bolt {
    constructor(isMain) {
      this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 500;
      this.y = 0;
      this.path = [{x: this.x, y: this.y}];
      this.active = true;
      this.isMain = isMain;
      this.baseWidth = isMain ? Math.random() * 3 + 4 : Math.random() * 2 + 1;
    }
    
    update() {
      if(!this.active) return;
      
      let lastPoint = this.path[this.path.length - 1];
      let newX = lastPoint.x + (Math.random() - 0.5) * 50;
      let newY = lastPoint.y + Math.random() * 30 + 15; // move down faster
      
      this.path.push({x: newX, y: newY});
      
      if(newY > lCanvas.height) {
        this.active = false;
      }
    }
    
    draw(ctx) {
      if(this.path.length < 2) return;
      
      // 1. Draw Outer Blue Glow
      ctx.beginPath();
      ctx.moveTo(this.path[0].x, this.path[0].y);
      for(let i=1; i<this.path.length; i++) {
        ctx.lineTo(this.path[i].x, this.path[i].y);
      }
      ctx.strokeStyle = `rgba(59, 130, 246, 0.8)`;
      ctx.lineWidth = this.baseWidth * 2;
      ctx.shadowBlur = 40;
      ctx.shadowColor = '#60a5fa'; // bright blue
      ctx.stroke();

      // 2. Draw White Hot Core
      ctx.beginPath();
      ctx.moveTo(this.path[0].x, this.path[0].y);
      for(let i=1; i<this.path.length; i++) {
        ctx.lineTo(this.path[i].x, this.path[i].y);
      }
      ctx.strokeStyle = `rgba(255, 255, 255, 0.9)`;
      ctx.lineWidth = this.baseWidth * 0.5;
      ctx.shadowBlur = 10;
      ctx.shadowColor = '#ffffff';
      ctx.stroke();
    }
  }

  class ShootingStar {
    constructor() {
      this.x = Math.random() * lCanvas.width;
      this.y = 0;
      this.length = Math.random() * 80 + 20;
      this.speed = Math.random() * 10 + 15;
      this.active = true;
    }
    update() {
      this.x -= this.speed; // move left
      this.y += this.speed; // move down
      if(this.x < 0 || this.y > lCanvas.height) this.active = false;
    }
    draw(ctx) {
      ctx.beginPath();
      ctx.moveTo(this.x, this.y);
      ctx.lineTo(this.x + this.length, this.y - this.length);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.8)';
      ctx.lineWidth = 2;
      ctx.shadowBlur = 10;
      ctx.shadowColor = 'white';
      ctx.stroke();
    }
  }

  function animateLightning() {
    if(!document.getElementById('preloader')) return;
    
    // Fade out for lightning trail, clear dark enough to maintain galaxy black
    lCtx.fillStyle = 'rgba(0, 0, 3, 0.25)';
    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    
    // Draw background stars
    stars.forEach(star => {
      star.alpha += star.blinkSpeed;
      if(star.alpha > 1 || star.alpha < 0) star.blinkSpeed *= -1;
      lCtx.beginPath();
      lCtx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
      lCtx.fillStyle = `rgba(255, 255, 255, ${Math.abs(star.alpha)})`;
      lCtx.shadowBlur = 0;
      lCtx.fill();
    });

    // Spawn shooting stars
    if(Math.random() < 0.03) {
      shootingStars.push(new ShootingStar());
    }

    shootingStars = shootingStars.filter(s => s.active);
    shootingStars.forEach(s => {
      s.update();
      s.draw(lCtx);
    });
    
    // Spawn lightning bolts
    if(Math.random() < 0.15 && bolts.filter(b => b.active).length < 3) {
      bolts.push(new Bolt(true));
      // spawn branch
      if(Math.random() < 0.5) bolts.push(new Bolt(false));
    }
    
    // Background lightning flash
    if(Math.random() < 0.08) {
      lCtx.fillStyle = 'rgba(30, 60, 150, 0.15)';
      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);
    }
    
    bolts = bolts.filter(b => b.active || Math.random() < 0.95); // keep dead bolts shortly for glow trail
    bolts.forEach(bolt => {
      for(let i=0; i<4; i++) bolt.update(); // fast strike
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
    progress += Math.random() * 8; 
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

js += advanced_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update cache buster
html = html.replace('script.js?v=5', 'script.js?v=6')
html = html.replace('style.css?v=7', 'style.css?v=8')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Galaxy lightning engine implemented.")
