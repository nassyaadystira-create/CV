import re

# ==========================================
# 1. UPDATE HTML
# ==========================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace static subtitle with typewriter
old_subtitle = """<p class="hero-subtitle">
            I'm an Electronics & Telecommunications Engineering Student with a passion for innovation.
          </p>"""
new_subtitle = """<p class="hero-subtitle" style="min-height: 60px;">
            <span id="typewriter-text"></span><span class="typewriter-cursor">|</span>
          </p>"""
html = html.replace(old_subtitle, new_subtitle)

# Update cache buster
html = html.replace('script.js?v=10', 'script.js?v=11')
html = html.replace('style.css?v=14', 'style.css?v=15')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# ==========================================
# 2. UPDATE CSS
# ==========================================
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

typewriter_css = """
/* ===== TYPEWRITER EFFECT ===== */
.typewriter-cursor {
  font-weight: bold;
  color: #3b82f6;
  animation: blink 0.8s step-end infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
"""
if "TYPEWRITER EFFECT" not in css:
    css += '\n' + typewriter_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# ==========================================
# 3. UPDATE JS
# ==========================================
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

features_js = """
/* ===== TYPEWRITER LOGIC ===== */
const typeText = document.getElementById('typewriter-text');
if (typeText) {
  const phrases = [
    "I'm an Electronics & Telecommunications Student.",
    "I'm an IoT Developer & Tech Enthusiast.",
    "I'm a Creative Problem Solver."
  ];
  let phraseIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  
  function typeEffect() {
    const currentPhrase = phrases[phraseIndex];
    if (isDeleting) {
      typeText.textContent = currentPhrase.substring(0, charIndex - 1);
      charIndex--;
    } else {
      typeText.textContent = currentPhrase.substring(0, charIndex + 1);
      charIndex++;
    }
    
    let typeSpeed = isDeleting ? 40 : 80;
    
    if (!isDeleting && charIndex === currentPhrase.length) {
      typeSpeed = 2000; // pause at end of word
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      phraseIndex = (phraseIndex + 1) % phrases.length;
      typeSpeed = 500; // pause before typing next
    }
    
    setTimeout(typeEffect, typeSpeed);
  }
  
  setTimeout(typeEffect, 1000);
}

/* ===== SUCCESS CONFETTI LOGIC ===== */
function fireConfetti() {
  const colors = ['#3b82f6', '#60a5fa', '#ffffff', '#f59e0b', '#ef4444'];
  for(let i=0; i<100; i++) {
    const conf = document.createElement('div');
    conf.style.position = 'fixed';
    conf.style.width = Math.random() * 8 + 4 + 'px';
    conf.style.height = Math.random() * 16 + 8 + 'px';
    conf.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
    conf.style.left = Math.random() * 100 + 'vw';
    conf.style.top = '-20px';
    conf.style.zIndex = '9999999';
    conf.style.pointerEvents = 'none';
    conf.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
    document.body.appendChild(conf);
    
    const animation = conf.animate([
      { transform: `translate3d(0, 0, 0) rotate(0deg)`, opacity: 1 },
      { transform: `translate3d(${(Math.random() - 0.5) * 300}px, ${window.innerHeight + 100}px, 0) rotate(${Math.random() * 720}deg)`, opacity: 0 }
    ], {
      duration: Math.random() * 2000 + 2000,
      easing: 'cubic-bezier(.37,0,.63,1)'
    });
    
    animation.onfinish = () => conf.remove();
  }
}

const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Stop page reload
    
    // FIRE CONFETTI!
    fireConfetti();
    playHoverSound(); // play a beep for success
    
    const btn = contactForm.querySelector('button');
    const originalText = btn.innerHTML;
    btn.innerHTML = '✨ Pesan Sedang Dikirim... ✨';
    btn.disabled = true;
    
    const formData = new FormData(contactForm);
    fetch(contactForm.action, {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json'
      }
    }).then(response => {
      contactForm.reset();
      btn.innerHTML = '✨ Pesan Berhasil Terkirim! ✨';
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }, 5000);
    }).catch(error => {
      btn.innerHTML = '❌ Gagal Mengirim';
      setTimeout(() => {
        btn.innerHTML = originalText;
        btn.disabled = false;
      }, 3000);
    });
  });
}
"""

if "TYPEWRITER LOGIC" not in js:
    js += '\n' + features_js
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Typewriter and Confetti implemented.")
