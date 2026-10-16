import re

# ==========================================
# 1. UPDATE CSS (Darken cards)
# ==========================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make cards solid dark with just 5% transparency
css = css.replace('--card-bg: rgba(30, 40, 70, 0.7);', '--card-bg: rgba(10, 14, 28, 0.95);')
css = css.replace('--glass-bg: rgba(20, 30, 60, 0.85);', '--glass-bg: rgba(12, 18, 35, 0.98);')

# Add photo marquee CSS
photo_marquee_css = """
/* ===== PHOTO MARQUEE ===== */
.photo-marquee-container {
  overflow: hidden;
  white-space: nowrap;
  width: 100%;
  padding: 20px 0;
  margin: 40px 0;
  position: relative;
}

.photo-marquee-content {
  display: inline-block;
  animation: scrollMarquee 50s linear infinite;
}

.photo-marquee-container:hover .photo-marquee-content {
  animation-play-state: paused;
}

.photo-marquee-content img {
  height: 280px;
  width: auto;
  border-radius: 12px;
  margin: 0 15px;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 8px 25px rgba(0,0,0,0.5);
  transition: transform 0.3s ease, border-color 0.3s ease;
  cursor: pointer;
}

.photo-marquee-content img:hover {
  transform: scale(1.05);
  border-color: #3b82f6;
}
"""
if "PHOTO MARQUEE" not in css:
    css += '\n' + photo_marquee_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# ==========================================
# 2. UPDATE HTML (Replace emoji + Add Capturing Moments)
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace lightning emoji with SVG
svg_lightning = '<svg viewBox="0 0 24 24" fill="currentColor" style="width:20px;height:20px;color:#3b82f6;margin-right:8px;vertical-align:middle;filter:drop-shadow(0 0 5px #3b82f6);"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"></path></svg>'
html = html.replace('<i>⚡</i>', svg_lightning)

# Add Capturing Moments
photos = [
  'WhatsApp Image 2026-10-08 at 11.04.40.jpeg',
  'WhatsApp Image 2026-10-08 at 11.04.43.jpeg',
  'WhatsApp Image 2026-10-08 at 11.04.46.jpeg',
  'WhatsApp Image 2026-10-08 at 11.04.47.jpeg',
  'WhatsApp Image 2026-10-08 at 11.04.52.jpeg',
  'WhatsApp Image 2026-10-08 at 11.05.07.jpeg',
  'WhatsApp Image 2026-10-08 at 11.05.08.jpeg',
  'WhatsApp Image 2026-10-08 at 11.05.09.jpeg'
]

img_tags = ''.join([f'<img src="{p}" alt="Moment">' for p in photos])
# duplicate for infinite scroll
full_img_content = img_tags + img_tags

capturing_moments_html = f"""
  <!-- ===== CAPTURING MOMENTS ===== -->
  <section class="section" id="moments">
    <div class="container">
      <h2 class="section-title">Capturing <span class="highlight">Moments</span></h2>
      <p class="section-subtitle">Beberapa momen berharga dalam perjalanan karir dan pendidikanku.</p>
    </div>
    <div class="photo-marquee-container">
      <div class="photo-marquee-content">
        {full_img_content}
      </div>
    </div>
  </section>
"""

# Insert before Contact section
if 'CAPTURING MOMENTS' not in html:
    html = html.replace('<!-- ===== CONTACT SECTION ===== -->', capturing_moments_html + '\n  <!-- ===== CONTACT SECTION ===== -->')

# Update cache buster
html = html.replace('style.css?v=12', 'style.css?v=13')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Boxes darkened, lightning icon upgraded to SVG, Capturing Moments marquee added.")
