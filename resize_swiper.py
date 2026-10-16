import sys

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the swiper-slide dimensions
old_css_mobile = '''
.swiper-slide {
  background-position: center;
  background-size: cover;
  width: 280px;
  height: 380px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.05);
}
'''

new_css_mobile = '''
.swiper-slide {
  background-position: center;
  background-size: cover;
  width: 180px;
  height: 240px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.5);
  border: 1px solid rgba(255,255,255,0.05);
}
'''

old_css_desktop = '''
@media (min-width: 768px) {
  .swiper-slide {
    width: 320px;
    height: 420px;
  }
}
'''

new_css_desktop = '''
@media (min-width: 768px) {
  .swiper-slide {
    width: 220px;
    height: 300px;
  }
}
'''

css = css.replace(old_css_mobile.strip(), new_css_mobile.strip())
css = css.replace(old_css_desktop.strip(), new_css_desktop.strip())

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update cache buster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('style.css?v=2', 'style.css?v=3')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Swiper resized to be much smaller.")
