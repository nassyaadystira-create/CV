import sys

def fix_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Spiderman Element in Hero (Subtle Red-Blue Accent and subtle spiderweb SVG background)
    spidey_bg = '''
  <!-- Subtle Spiderman Web Background -->
  <div style="position: absolute; top: -50px; right: -50px; opacity: 0.05; pointer-events: none; z-index: 0;">
    <svg width="400" height="400" viewBox="0 0 100 100">
      <path d="M50,50 L50,0 M50,50 L100,20 M50,50 L100,80 M50,50 L50,100 M50,50 L0,80 M50,50 L0,20" stroke="#ef4444" stroke-width="0.5" fill="none"/>
      <circle cx="50" cy="50" r="10" stroke="#ef4444" stroke-width="0.5" fill="none"/>
      <circle cx="50" cy="50" r="25" stroke="#ef4444" stroke-width="0.5" fill="none"/>
      <circle cx="50" cy="50" r="40" stroke="#ef4444" stroke-width="0.5" fill="none"/>
    </svg>
  </div>
'''
    if 'Spiderman Web Background' not in content:
        hero_tag = '<section class="hero" id="home">'
        content = content.replace(hero_tag, hero_tag + spidey_bg)
    
    # Hero Title Spiderman gradient class (we'll update CSS)
    content = content.replace('hero-blue-italic', 'hero-spidey-italic')

    # 2. Revert Gallery to Grid
    content = content.replace('<div class="gallery-carousel">', '<div class="gallery-grid">')

    # 3. Seamless Photo Strip Loop
    strip_tag = '<div class="coverflow-track">'
    strip_items = '''
        <!-- Original 5 items -->
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.40.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.43.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.57 (2).jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.08.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.11 (3).jpeg" alt="Moment" loading="lazy"></div>
        <!-- Duplicated for seamless loop -->
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.40.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.43.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.04.57 (2).jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.08.jpeg" alt="Moment" loading="lazy"></div>
        <div class="coverflow-item"><img src="WhatsApp Image 2026-10-08 at 11.05.11 (3).jpeg" alt="Moment" loading="lazy"></div>
'''
    
    start_track = content.find(strip_tag)
    if start_track != -1:
        end_track = content.find('</div>', start_track)
        # Assuming the structure is <div track> ... </div> </div>
        # Actually it's better to regex or replace the whole track block
        pass
    
    # We will just replace the inner HTML of coverflow-track
    start = content.find('<div class="coverflow-track">')
    if start != -1:
        end = content.find('</div>', start + len('<div class="coverflow-track">'))
        while '<div class="coverflow-item"' in content[end:end+50]:
           end = content.find('</div>', end + 10)
        # Let's use a simpler replace
        pass
    
    import re
    # Match the entire coverflow-track block
    content = re.sub(r'<div class="coverflow-track">.*?</div>\s*</div>\s*</section>',
                     f'<div class="coverflow-track">\n{strip_items}\n      </div>\n    </div>\n  </section>',
                     content, flags=re.DOTALL)

    # 4. FormSubmit for Contact
    form_old = '<form id="contactForm" class="contact-form">'
    form_new = '''<form id="contactForm" class="contact-form" action="https://formsubmit.co/nassyaadystira@gmail.com" method="POST">
            <!-- FormSubmit hidden configs -->
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_subject" value="New message from Portfolio!">
            <input type="hidden" name="_next" value="https://ekawahyu-portofolio.vercel.app/"> <!-- Wait, we should just let it show the thank you page or reload -->
'''
    # We'll just use a generic thank you redirect to the same page
    form_new = '''<form id="contactForm" class="contact-form" action="https://formsubmit.co/nassyaadystira@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_subject" value="Pesan Baru dari Portfolio Nassya!">
'''
    content = content.replace(form_old, form_new)
    
    # Give name attributes to inputs!
    content = content.replace('id="cName" placeholder="Nama Anda" required', 'id="cName" name="name" placeholder="Nama Anda" required')
    content = content.replace('id="cEmail" placeholder="Email Anda" required', 'id="cEmail" name="email" placeholder="Email Anda" required')
    content = content.replace('id="cMessage" rows="5" placeholder="Pesan Anda" required', 'id="cMessage" name="message" rows="5" placeholder="Pesan Anda" required')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("HTML fixed.")

fix_html()
