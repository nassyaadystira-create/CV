import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace fade out to be smoother
js = js.replace("lCtx.fillStyle = 'rgba(2, 2, 5, 0.4)';", "lCtx.fillStyle = 'rgba(5, 5, 16, 0.15)';") # Smooth trail

# Less random pause to make it continuous and smooth
js = js.replace("if(Math.random() > 0.4) {\n      setTimeout(() => requestAnimationFrame(drawLightning), 30);\n      return;\n    }", "if(Math.random() > 0.85) {\n      setTimeout(() => requestAnimationFrame(drawLightning), 10);\n      return;\n    }")

# Adjust horizontal zig-zag for smoother lines
js = js.replace("x += (Math.random() - 0.5) * 80;", "x += (Math.random() - 0.5) * 40;")
js = js.replace("y += Math.random() * 50;", "y += Math.random() * 30 + 10;")

# Make colors deep galaxy blue/purple
js = js.replace("rgba(150, 210, 255,", "rgba(100, 140, 255,")
js = js.replace("rgba(100, 180, 255,", "rgba(80, 100, 250,")
js = js.replace("lCtx.shadowColor = '#3b82f6';", "lCtx.shadowColor = '#4f46e5';") # indigo

# Background flash
js = js.replace("rgba(59, 130, 246, 0.15)", "rgba(30, 58, 138, 0.08)")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('script.js?v=3', 'script.js?v=4')

# Update the Welcome text glow to match galaxy colors
html = html.replace("text-shadow:0 0 15px rgba(59,130,246,0.8), 0 0 30px rgba(59,130,246,0.5);", "text-shadow:0 0 15px rgba(79,70,229,0.8), 0 0 30px rgba(79,70,229,0.5);color:#818cf8;")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Lightning smoothness and galaxy colors updated.")
