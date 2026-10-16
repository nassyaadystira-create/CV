import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

matches = re.findall(r'\.glass-card \{[^}]+\}', css)
for m in matches:
    print(m)
