import sys

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<!-- ===== CONTACT SECTION ===== -->'
    end_tag = '<!-- FOOTER -->'

    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag)

    if start_idx != -1 and end_idx != -1:
        new_contact = '''<!-- ===== CONTACT SECTION ===== -->
  <section class="section" id="contact">
    <div class="container">
      <div class="section-header">
        <span class="section-badge">Let's Connect</span>
        <h2 class="section-title">Get In <span class="gradient-text">Touch</span></h2>
        <p class="section-desc">Feel free to reach out for collaborations, opportunities, or just a friendly chat!</p>
      </div>
      
      <div class="contact-box glass-card animate-on-scroll" style="display: flex; flex-wrap: wrap; gap: 40px; justify-content: space-between; padding: 40px; max-width: 800px; margin: 0 auto;">
        
        <div class="contact-info-list" style="display: flex; flex-direction: column; gap: 20px;">
          <a href="mailto:nassyaadystira@gmail.com" class="contact-link" style="display: flex; align-items: center; gap: 12px; color: var(--text); text-decoration: none; font-size: 1.05rem; transition: color 0.3s;">
            <span class="contact-icon" style="font-size: 1.5rem; background: rgba(59,130,246,0.1); padding: 10px; border-radius: 12px;">✉️</span>
            nassyaadystira@gmail.com
          </a>
          <a href="https://www.linkedin.com/in/nassya-adystira-09b844319/" target="_blank" rel="noopener noreferrer" class="contact-link" style="display: flex; align-items: center; gap: 12px; color: var(--text); text-decoration: none; font-size: 1.05rem; transition: color 0.3s;">
            <span class="contact-icon" style="font-size: 1.5rem; background: rgba(59,130,246,0.1); padding: 10px; border-radius: 12px;">💼</span>
            Nassya Adystira
          </a>
          <a href="https://www.instagram.com/nassyaadystira" target="_blank" rel="noopener noreferrer" class="contact-link" style="display: flex; align-items: center; gap: 12px; color: var(--text); text-decoration: none; font-size: 1.05rem; transition: color 0.3s;">
            <span class="contact-icon" style="font-size: 1.5rem; background: rgba(59,130,246,0.1); padding: 10px; border-radius: 12px;">📸</span>
            @nassyaadystira
          </a>
          <div style="display: flex; align-items: center; gap: 12px; color: var(--text-muted); font-size: 0.9rem;">
            <span class="contact-icon" style="font-size: 1.5rem; background: rgba(59,130,246,0.1); padding: 10px; border-radius: 12px; color: var(--text);">🏛️</span>
            Politeknik Caltex Riau, Indonesia
          </div>
        </div>
        
        <div class="contact-cta" style="flex: 1; min-width: 280px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; background: rgba(59,130,246,0.05); padding: 30px; border-radius: 16px; border: 1px solid rgba(96,165,250,0.15);">
          <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.25rem; margin-bottom: 12px; color: white;">Have a project in mind?</h3>
          <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 24px; line-height: 1.6;">I'm currently open for new opportunities and collaborations.</p>
          <a href="mailto:nassyaadystira@gmail.com" class="btn-primary" style="width: 100%; justify-content: center;">
            <span class="btn-icon">🚀</span> Send Message
          </a>
        </div>

      </div>
    </div>
  </section>

  '''
        content = content[:start_idx] + new_contact + content[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Success")
    else:
        print("Tags not found")

update_html()
