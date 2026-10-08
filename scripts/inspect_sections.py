with open('notes/cn/unit2/unit-2-notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
secs = re.findall(r'<section id="([^"]+)"', text)
print('Sections found:', secs)
for s in secs:
    m = re.search(r'<section id="' + s + r'".*?</section>', text, re.DOTALL)
    if m:
        print(f"Section {s}: start={m.start()}, end={m.end()}, len={m.end()-m.start()}")
