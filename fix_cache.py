import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add cache buster to style.css
content = content.replace('href="style.css"', 'href="style.css?v=2"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cache buster added to style.css")
