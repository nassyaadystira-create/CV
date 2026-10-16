import sys
import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add Spidey Gradient
if '.hero-spidey-italic' not in css:
    css += '''
.hero-spidey-italic {
  font-style: italic;
  background: linear-gradient(135deg, #ef4444, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
'''

# Restore Gallery Grid (if it was overridden or if we need to ensure it's there)
# Actually, the user wants the gallery back to scroll down grid like before.
# I had replaced .gallery-grid with .gallery-carousel in the previous step via PowerShell replacement. Wait, I added .gallery-carousel but didn't remove .gallery-grid.
# Let's just make sure .gallery-grid is defined properly.
if '.gallery-grid' not in css or 'grid-template-columns' not in css.split('.gallery-grid')[1][:100]:
    css += '''
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}
.gallery-grid .gallery-item {
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  transition: transform 0.3s;
}
.gallery-grid .gallery-item:hover {
  transform: translateY(-5px);
}
.gallery-grid .gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
'''

# Fix Seamless Marquee Animation
css = re.sub(r'@keyframes scrollMarquee\s*\{[^}]*\}', 
             '@keyframes scrollMarquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }', 
             css)
# Wait, nested curly braces in regex is tricky. Let's do simple replace
css = css.replace('0% { transform: translateX(10%); }', '0% { transform: translateX(0); }')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# JS Update
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove the whole contactForm submit listener so it uses native form action
js = re.sub(r'const contactForm = document\.getElementById\(\'contactForm\'\);.*?\}\);?\s*\}', 
            '// Form handled natively by FormSubmit.co', js, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("CSS and JS updated.")
