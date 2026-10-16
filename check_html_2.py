import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

if 'id="pm-icon"' not in html:
    print("pm-icon missing in index.html!")
else:
    print("pm-icon exists.")

