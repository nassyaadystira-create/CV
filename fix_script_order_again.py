import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# remove script tag
content = content.replace('<script src="script.js"></script>', '')

# insert it right before </body>
content = content.replace('</body>', '<script src="script.js"></script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed script tag order again.")
