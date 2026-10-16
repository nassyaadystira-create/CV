import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Theme Toggle to Navbar
toggle_btn = '''
        <button id="themeToggle" class="theme-toggle" aria-label="Toggle Theme">
          <svg class="sun-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
          <svg class="moon-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
'''
if 'id="themeToggle"' not in content:
    content = content.replace('</nav>', f'  {toggle_btn}\n      </nav>')

# 2. Add Custom Cursor
cursor_html = '''
  <div class="custom-cursor" id="customCursor"></div>
  <div class="custom-cursor-follower" id="cursorFollower"></div>
'''
if 'id="customCursor"' not in content:
    content = content.replace('</body>', f'{cursor_html}\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML updated.")
