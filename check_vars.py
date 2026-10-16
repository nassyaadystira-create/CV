import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's find all occurrences of --glass-bg
matches = re.findall(r'(--glass-bg: [^;]+;)', css)
print("Glass BG definitions:", matches)

matches2 = re.findall(r'(--card-bg: [^;]+;)', css)
print("Card BG definitions:", matches2)
