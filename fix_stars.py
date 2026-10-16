import sys

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_color = "const color = `rgba(255, 255, 255, ${alpha})`;"
new_color = "const isLight = document.documentElement.getAttribute('data-theme') === 'light';\n      const color = isLight ? `rgba(0,0,0,${alpha})` : `rgba(255, 255, 255, ${alpha})`;"

if old_color in js:
    js = js.replace(old_color, new_color)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Starfield color updated.")
