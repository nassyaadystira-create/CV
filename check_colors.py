import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's see what needs fixing
matches = re.findall(r'background(?:-color)?:\s*rgba\([0-9]+,\s*[0-9]+,\s*[0-9]+,\s*[0-9.]+\)', css)
from collections import Counter
print(Counter(matches).most_common(10))
