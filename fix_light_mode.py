import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add new variables to :root
root_new = '''
  --card-bg: rgba(10,15,36,0.6);
  --nav-bg: rgba(5,5,16,0.85);
  --modal-bg: rgba(5,5,16,0.95);
'''
css = css.replace('--glass-bg: rgba(15, 23, 42, 0.4);', '--glass-bg: rgba(10,15,36,0.7);\n' + root_new)

# 2. Add new variables to light mode
light_new = '''
  --card-bg: rgba(255, 255, 255, 0.9);
  --nav-bg: rgba(255, 255, 255, 0.85);
  --modal-bg: rgba(255, 255, 255, 0.95);
'''
css = css.replace('--glass-bg: rgba(255, 255, 255, 0.85);', '--glass-bg: rgba(255, 255, 255, 0.85);\n' + light_new)

# 3. Replace hardcoded backgrounds
css = re.sub(r'background(?:-color)?:\s*rgba\(10,15,36,0\.7\);', 'background: var(--glass-bg);', css)
css = re.sub(r'background(?:-color)?:\s*rgba\(10,15,36,0\.6\);', 'background: var(--card-bg);', css)
css = re.sub(r'background(?:-color)?:\s*rgba\(10,15,36,0\.85\);', 'background: var(--nav-bg);', css)
css = re.sub(r'background(?:-color)?:\s*rgba\(5,5,16,0\.85\);', 'background: var(--nav-bg);', css)
css = re.sub(r'background(?:-color)?:\s*rgba\(5,5,16,0\.95\);', 'background: var(--modal-bg);', css)

# 4. Fix some text colors
css = re.sub(r'color:\s*#fff;', 'color: var(--text);', css)
css = re.sub(r'color:\s*white;', 'color: var(--text);', css)
# EXCEPT for primary buttons where text should stay white
css = css.replace('.btn-primary {\n  color: var(--text);', '.btn-primary {\n  color: #fff;')
css = css.replace('.sc-icon {\n  color: var(--text);', '.sc-icon {\n  color: #fff;')
css = css.replace('.gallery-overlay {\n  background: linear-gradient(to top, rgba(5,5,16,0.95)', '.gallery-overlay {\n  background: linear-gradient(to top, var(--modal-bg)')

# Save
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('style.css?v=3', 'style.css?v=4')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS updated for light mode.")
