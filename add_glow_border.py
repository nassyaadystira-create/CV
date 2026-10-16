import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

glow_css = """
/* ===== ANIMATED GLOW BORDER ===== */
@property --border-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.animated-glow-card {
  border: 1.5px solid transparent !important;
  background: 
    linear-gradient(var(--card-bg), var(--card-bg)) padding-box,
    conic-gradient(from var(--border-angle), 
      rgba(255,255,255,0.05) 0%, 
      transparent 10%, 
      transparent 40%, 
      #3b82f6 50%, 
      transparent 60%, 
      transparent 90%, 
      #ffffff 100%
    ) border-box !important;
  animation: glowRotate 3.5s linear infinite;
  position: relative;
}

.animated-glow-card::after {
  content: "";
  position: absolute;
  inset: -1.5px;
  border-radius: inherit;
  background: conic-gradient(from var(--border-angle), transparent 40%, rgba(59,130,246,0.3) 50%, transparent 60%, transparent 90%, rgba(255,255,255,0.3) 100%);
  filter: blur(8px);
  z-index: -1;
  animation: glowRotate 3.5s linear infinite;
}

@keyframes glowRotate {
  0% { --border-angle: 0deg; }
  100% { --border-angle: 360deg; }
}
"""

if "ANIMATED GLOW BORDER" not in css:
    css += '\n' + glow_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the class to the hero status cards
html = html.replace('class="hero-status-card compact-card"', 'class="hero-status-card compact-card animated-glow-card"')
# Maybe add to the About picture?
# html = html.replace('class="about-image glass-card animate-on-scroll"', 'class="about-image glass-card animate-on-scroll animated-glow-card"')

# Update cache buster
html = html.replace('style.css?v=8', 'style.css?v=9')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Animated glow card border implemented.")
