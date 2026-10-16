import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see what classes the status cards use
matches = re.findall(r'<div class="([^"]*card[^"]*)">', html)
print("Cards found:", set(matches))
