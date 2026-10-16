import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<section class="section" id="about">')
if start_idx != -1:
    end_idx = content.find('</section>', start_idx)
    about_content = content[start_idx:end_idx]
    
    lines = about_content.split('\n')
    new_lines = []
    for line in lines:
        if 'Download CV' in line and '<a' in line:
            continue
        new_lines.append(line)
        
    new_about_content = '\n'.join(new_lines)
    
    content = content[:start_idx] + new_about_content + content[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")
else:
    print("About section not found")

