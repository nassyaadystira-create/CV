import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

matches = re.findall(r'(\.animate-on-scroll[^{]*{[^}]+})', css)
for m in matches:
    print(m)

matches2 = re.findall(r'(\.is-visible[^{]*{[^}]+})', css)
for m in matches2:
    print(m)
