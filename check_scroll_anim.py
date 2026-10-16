import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

if "IntersectionObserver" in js:
    print("IntersectionObserver IS present in script.js")
else:
    print("No IntersectionObserver in script.js")

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if "animate-on-scroll" in css or "fade-in" in css or "slide-up" in css:
    print("Scroll animation CSS classes ARE present in style.css")
else:
    print("No Scroll animation CSS classes in style.css")
