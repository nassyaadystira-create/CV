import re
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

matches = re.findall(r'IntersectionObserver\([\s\S]+?\}\);', js)
for m in matches:
    print(m)
