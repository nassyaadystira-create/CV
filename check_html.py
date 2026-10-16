with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('projectModal')
if idx != -1:
    print(content[idx-50:idx+800])
else:
    print('projectModal not found in index.html')
