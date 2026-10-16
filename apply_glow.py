import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add to Certificates cards
html = html.replace('class="cert-card glass-card"', 'class="cert-card glass-card animated-glow-card"')

# Add to Hero Status cards
html = html.replace('class="hero-status-card glass-card"', 'class="hero-status-card glass-card animated-glow-card"')

# Also add to Achievement cards? 
html = html.replace('class="achievement-card glass-card animate-on-scroll"', 'class="achievement-card glass-card animate-on-scroll animated-glow-card"')

# Update cache buster
html = html.replace('style.css?v=9', 'style.css?v=10')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Classes successfully added to HTML!")
