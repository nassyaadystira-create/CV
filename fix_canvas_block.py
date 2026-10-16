import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the canvas covering the text:
# Replace the solid fill with destination-out fade
old_fade = "lCtx.fillStyle = 'rgba(0, 0, 3, 0.25)';\n    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);"
new_fade = "lCtx.globalCompositeOperation = 'destination-out';\n    lCtx.fillStyle = 'rgba(0, 0, 0, 0.15)';\n    lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);\n    lCtx.globalCompositeOperation = 'source-over';"
js = js.replace(old_fade, new_fade)

# Fix background lightning flash
old_flash = "lCtx.fillStyle = 'rgba(30, 60, 150, 0.15)';\n      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);"
new_flash = "lCtx.fillStyle = 'rgba(60, 100, 255, 0.05)';\n      lCtx.fillRect(0, 0, lCanvas.width, lCanvas.height);"
js = js.replace(old_flash, new_flash)

# Make the lightning spawn everywhere and zig-zag wildly (menyebar)
js = js.replace("this.x = lCanvas.width / 2 + (Math.random() - 0.5) * 500;", "this.x = Math.random() * lCanvas.width;")
js = js.replace("let newX = lastPoint.x + (Math.random() - 0.5) * 50;", "let newX = lastPoint.x + (Math.random() - 0.5) * 150; // wildly zig-zag")
js = js.replace("let newY = lastPoint.y + Math.random() * 30 + 15;", "let newY = lastPoint.y + Math.random() * 40 + 10;")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update cache buster
html = html.replace('script.js?v=6', 'script.js?v=7')

# To be safe against text rendering bugs, let's remove filter:drop-shadow and use text-shadow again but keep dotted look.
# Actually, the text was covered by the canvas. The CSS was fine. But just to be sure.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed canvas blocking text and made lightning spread out.")
