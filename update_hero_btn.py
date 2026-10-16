import sys

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Let's talk button in hero
    target = 'href="mailto:nassyaadystira@gmail.com" class="btn-outline-hero"'
    replacement = 'href="#contact" class="btn-outline-hero"'
    
    if target in content:
        content = content.replace(target, replacement)
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Hero button updated.")
    else:
        print("Hero button not found.")

update_html()
