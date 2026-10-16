import sys

# 1. Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

preloader_html = '''
  <!-- ===== PRELOADER ===== -->
  <div id="preloader">
    <svg class="lightning-bolt" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
      <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
    </svg>
  </div>
'''

if 'id="preloader"' not in html:
    html = html.replace('<body>', f'<body>\n{preloader_html}')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

preloader_css = '''
/* ===== PRELOADER ===== */
#preloader {
  position: fixed;
  inset: 0;
  background: var(--bg);
  z-index: 999999;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity 0.5s ease-out, visibility 0.5s ease-out;
}

.lightning-bolt {
  width: 80px;
  height: 80px;
  stroke: var(--primary-light);
  fill: transparent;
  stroke-dasharray: 100;
  stroke-dashoffset: 100;
  animation: drawLightning 1.2s forwards ease-in-out, flashLightning 0.6s 1.2s forwards ease-in-out;
}

@keyframes drawLightning {
  to {
    stroke-dashoffset: 0;
  }
}

@keyframes flashLightning {
  0% {
    fill: transparent;
    filter: none;
  }
  20%, 60%, 100% {
    fill: var(--primary-light);
    filter: drop-shadow(0 0 25px var(--primary-light));
  }
  40%, 80% {
    fill: transparent;
    filter: none;
  }
}

body.loaded #preloader {
  opacity: 0;
  visibility: hidden;
}
'''
if '#preloader' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(preloader_css)

# 3. Update JS
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

preloader_js = '''
/* ===== PRELOADER LOGIC ===== */
window.addEventListener('load', () => {
  setTimeout(() => {
    document.body.classList.add('loaded');
  }, 1900); // Wait for the lightning animation to finish
});
'''
if 'PRELOADER LOGIC' not in js:
    with open('script.js', 'a', encoding='utf-8') as f:
        f.write('\n' + preloader_js)

print("Preloader added.")
