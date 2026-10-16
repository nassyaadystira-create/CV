import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's see the :root block
root_match = re.search(r':root \{([^}]+)\}', css)
if root_match:
    root_content = root_match.group(1)
    new_vars = """
  --glass-bg: rgba(12, 16, 32, 0.95);
  --card-bg: rgba(15, 20, 38, 0.98);
  --nav-bg: rgba(8, 12, 24, 0.95);
  --modal-bg: rgba(10, 15, 30, 0.98);
"""
    if "--glass-bg" not in root_content:
        new_root = root_content + new_vars
        css = css.replace(root_content, new_root)
        
        with open('style.css', 'w', encoding='utf-8') as f:
            f.write(css)
        print("Variables added to :root!")
    else:
        print("Variables already exist in :root.")
else:
    print("Could not find :root")

# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('style.css?v=13', 'style.css?v=14')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
