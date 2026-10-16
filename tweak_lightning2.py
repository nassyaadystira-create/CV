import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Less spread (not too wide horizontally)
js = js.replace("this.x = Math.random() * lCanvas.width;", "this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 400;")
js = js.replace("let newX = lastPoint.x + (Math.random() - 0.5) * 150; // wildly zig-zag", "let newX = lastPoint.x + (Math.random() - 0.5) * 60; // controlled zig-zag")
js = js.replace("let newY = lastPoint.y + Math.random() * 40 + 10;", "let newY = lastPoint.y + Math.random() * 30 + 15;")

# 2. Don't make too many bolts (spawn rate and max active)
js = js.replace("if(Math.random() < 0.15 && bolts.filter(b => b.active).length < 3)", "if(Math.random() < 0.06 && bolts.filter(b => b.active).length < 2)")
# Keep dead bolts a bit longer for glow, but fewer
js = js.replace("bolts = bolts.filter(b => b.active || Math.random() < 0.95);", "bolts = bolts.filter(b => b.active || Math.random() < 0.90);")

# 3. Make lightning glow even more (lebih kilau)
# Outer glow
js = js.replace("ctx.shadowBlur = 40;", "ctx.shadowBlur = 80;")
js = js.replace("ctx.shadowColor = '#60a5fa';", "ctx.shadowColor = '#818cf8';") # use indigo/violet glow
# Core glow
js = js.replace("ctx.shadowBlur = 10;", "ctx.shadowBlur = 25;")
js = js.replace("this.baseWidth = isMain ? Math.random() * 3 + 4 : Math.random() * 2 + 1;", "this.baseWidth = isMain ? Math.random() * 4 + 5 : Math.random() * 2 + 2;")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update cache buster
html = html.replace('script.js?v=7', 'script.js?v=8')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Lightning parameters tweaked: less spread, fewer bolts, much brighter glow.")
