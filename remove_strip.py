import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<!-- ===== PHOTO STRIP ===== -->')
end_idx = content.find('<!-- ===== CONTACT SECTION ===== -->')

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Photo strip deleted.")
else:
    print("Could not find photo strip bounds.")
