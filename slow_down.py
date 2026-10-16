import re

# 1. SLOW DOWN BORDER GLOW
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change from 3.5s to 8s for a very smooth, slow, elegant rotation
css = css.replace('animation: glowRotate 3.5s linear infinite;', 'animation: glowRotate 8s linear infinite;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. SLOW DOWN LIGHTNING
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Slow down lightning bolt falling speed
js = js.replace('let newY = lastPoint.y + Math.random() * 30 + 15;', 'let newY = lastPoint.y + Math.random() * 15 + 8;') # Falls 2x slower

# Reduce the background flashes that cause dizziness
js = js.replace('if(Math.random() < 0.08) {', 'if(Math.random() < 0.02) {') # Flash 4x less frequently
js = js.replace('lCtx.fillStyle = \'rgba(60, 100, 255, 0.05)\';', 'lCtx.fillStyle = \'rgba(60, 100, 255, 0.02)\';') # Even fainter flash

# Slow down the drawing interval
js = js.replace('for(let i=0; i<4; i++) bolt.update(); // fast strike', 'for(let i=0; i<2; i++) bolt.update(); // slower strike')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('script.js?v=8', 'script.js?v=9')
html = html.replace('style.css?v=10', 'style.css?v=11')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Slowed down animations to prevent dizziness.")
