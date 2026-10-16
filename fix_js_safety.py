import sys

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace("const tags = card.dataset.tags.split(',');", "const tags = (card.dataset.tags || '').split(',');")
js = js.replace("const features = card.dataset.features.split('|');", "const features = (card.dataset.features || '').split('|');")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS safety check applied.")
