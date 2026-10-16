import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Swiper CSS
if 'swiper-bundle.min.css' not in content:
    content = content.replace('</head>', '  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n</head>')

# Rewrite Photo Strip Section
start_idx = content.find('<!-- ===== PHOTO STRIP ===== -->')
end_idx = content.find('<!-- ===== CONTACT SECTION ===== -->')

new_photo_strip = '''<!-- ===== PHOTO STRIP ===== -->
  <section class="section photo-strip-section">
    <div class="container" style="margin-bottom: 20px; text-align: center;">
      <h3 class="section-title animate-slide-up" style="font-size: 1.8rem;">Capturing <span class="gradient-text">Moments</span></h3>
    </div>
    
    <div class="swiper mySwiper animate-fade-in" style="padding: 50px 0;">
      <div class="swiper-wrapper">
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.04.40.jpeg" alt="Moment"></div>
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.04.43.jpeg" alt="Moment"></div>
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.04.57 (2).jpeg" alt="Moment"></div>
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.05.08.jpeg" alt="Moment"></div>
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.05.11 (3).jpeg" alt="Moment"></div>
        <!-- Extra images to make it look full -->
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.04.40.jpeg" alt="Moment"></div>
        <div class="swiper-slide"><img src="WhatsApp Image 2026-10-08 at 11.04.43.jpeg" alt="Moment"></div>
      </div>
      <div class="swiper-pagination"></div>
    </div>
  </section>

  '''

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_photo_strip + content[end_idx:]

# Add Swiper JS and Initialization
if 'swiper-bundle.min.js' not in content:
    swiper_js = '''
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script>
    var swiper = new Swiper(".mySwiper", {
      effect: "coverflow",
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: "auto",
      loop: true,
      coverflowEffect: {
        rotate: 30,
        stretch: 0,
        depth: 150,
        modifier: 1,
        slideShadows: true,
      },
      autoplay: {
        delay: 2500,
        disableOnInteraction: false,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });
  </script>
  <script src="script.js"></script>
'''
    content = content.replace('<script src="script.js"></script>', swiper_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html for Swiper")
