import sys
import re

# UPDATE CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

light_mode_vars = '''
/* ===== LIGHT MODE VARIABLES ===== */
[data-theme="light"] {
  --bg: #f8fafc;
  --text: #0f172a;
  --text-muted: #475569;
  --primary: #2563eb;
  --primary-light: #3b82f6;
  --secondary: #6366f1;
  --glass-bg: rgba(255, 255, 255, 0.85);
  --glass-border: rgba(0, 0, 0, 0.08);
  --glass-hover: rgba(255, 255, 255, 1);
}
'''
if '[data-theme="light"]' not in css:
    css = css.replace(':root {', light_mode_vars + '\n:root {')

cursor_css = '''
/* ===== CUSTOM CURSOR ===== */
@media (min-width: 1024px) {
  body {
    cursor: none;
  }
  a, button, input, textarea, .gallery-item img, .swiper-slide, .nav-link, .project-card {
    cursor: none;
  }
  .custom-cursor {
    position: fixed;
    width: 8px;
    height: 8px;
    background: var(--primary-light);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99999;
    transform: translate(-50%, -50%);
    transition: width 0.2s, height 0.2s, background 0.2s;
  }
  .custom-cursor-follower {
    position: fixed;
    width: 30px;
    height: 30px;
    border: 1px solid var(--primary-light);
    border-radius: 50%;
    pointer-events: none;
    z-index: 99998;
    transform: translate(-50%, -50%);
    transition: width 0.2s, height 0.2s, border-color 0.2s;
    transition-timing-function: ease-out;
  }
  .custom-cursor.hover {
    width: 20px;
    height: 20px;
    background: rgba(59,130,246,0.3);
  }
  .custom-cursor-follower.hover {
    width: 50px;
    height: 50px;
    border-color: rgba(59,130,246,0.1);
    background: rgba(59,130,246,0.1);
  }
}
'''
if '.custom-cursor' not in css:
    css += cursor_css

theme_btn_css = '''
.theme-toggle {
  background: none;
  border: none;
  color: var(--text);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  border-radius: 50%;
  transition: all 0.3s;
  margin-left: 10px;
}
.theme-toggle:hover {
  background: var(--glass-border);
  color: var(--primary-light);
}
'''
if '.theme-toggle' not in css:
    css += theme_btn_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# UPDATE JS
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

features_js = '''
/* ===== THEME TOGGLE ===== */
const themeToggle = document.getElementById('themeToggle');
const sunIcon = document.querySelector('.sun-icon');
const moonIcon = document.querySelector('.moon-icon');

function setTheme(isLight) {
  if (isLight) {
    document.documentElement.setAttribute('data-theme', 'light');
    sunIcon.style.display = 'block';
    moonIcon.style.display = 'none';
  } else {
    document.documentElement.removeAttribute('data-theme');
    sunIcon.style.display = 'none';
    moonIcon.style.display = 'block';
  }
}

if (themeToggle) {
  let isLight = false;
  themeToggle.addEventListener('click', () => {
    isLight = !isLight;
    setTheme(isLight);
    // Restart starfield with new colors
    if (window.stars) {
      window.stars.forEach(s => s.color = isLight ? 'rgba(0,0,0,' + s.alpha + ')' : 'rgba(255,255,255,' + s.alpha + ')');
    }
  });
}

/* ===== CUSTOM CURSOR ===== */
const cursor = document.getElementById('customCursor');
const cursorFollower = document.getElementById('cursorFollower');

if (cursor && cursorFollower && window.matchMedia("(min-width: 1024px)").matches) {
  let mouseX = 0, mouseY = 0;
  let followerX = 0, followerY = 0;

  document.addEventListener('mousemove', (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    cursor.style.left = mouseX + 'px';
    cursor.style.top = mouseY + 'px';
  });

  function animateFollower() {
    followerX += (mouseX - followerX) * 0.15;
    followerY += (mouseY - followerY) * 0.15;
    cursorFollower.style.left = followerX + 'px';
    cursorFollower.style.top = followerY + 'px';
    requestAnimationFrame(animateFollower);
  }
  animateFollower();

  const interactables = document.querySelectorAll('a, button, input, textarea, .gallery-item, .project-card, .swiper-slide, .nav-link');
  interactables.forEach(el => {
    el.addEventListener('mouseenter', () => {
      cursor.classList.add('hover');
      cursorFollower.classList.add('hover');
    });
    el.addEventListener('mouseleave', () => {
      cursor.classList.remove('hover');
      cursorFollower.classList.remove('hover');
    });
  });
}
'''
if 'THEME TOGGLE' not in js:
    js += features_js

# Update starfield initial color
js = js.replace("const color = gba(255, 255, 255, );", "const isLight = document.documentElement.getAttribute('data-theme') === 'light';\n      const color = isLight ? gba(0,0,0,) : gba(255, 255, 255, );")
# Wait, I can just use the window.stars global to store stars so theme toggle can update them
js = js.replace("const stars = [];", "window.stars = [];\n  const stars = window.stars;")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("CSS and JS updated.")
