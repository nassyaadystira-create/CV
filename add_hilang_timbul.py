import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the animation observer logic
old_observer = """const animObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => entry.target.classList.add('visible'), i * 90);
      animObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });"""

new_observer = """const animObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    } else {
      // Hilang timbul effect! Fade out when out of view
      entry.target.classList.remove('visible');
    }
  });
}, { threshold: 0.05, rootMargin: "-50px 0px" });

// Automatically add animate-on-scroll to key elements if they don't have it
document.querySelectorAll('section > .container > p, section > .container > h2, .contact-layout > div').forEach(el => {
  if(!el.classList.contains('animate-on-scroll')) {
    el.classList.add('animate-on-scroll');
    animObserver.observe(el);
  }
});
"""

js = js.replace(old_observer, new_observer)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Update style.css to make the slide up slightly more dramatic
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('transform: translateY(28px);', 'transform: translateY(40px) scale(0.98);')
css = css.replace('transform: translateY(0);', 'transform: translateY(0) scale(1);')

# Smooth scroll behavior for entire page
if "html {" not in css:
    css = "html { scroll-behavior: smooth; }\n" + css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update cache buster
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('script.js?v=11', 'script.js?v=12')
html = html.replace('style.css?v=15', 'style.css?v=16')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Dynamic fade in/out (hilang timbul) scroll effect implemented.")
