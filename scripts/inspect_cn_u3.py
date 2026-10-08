import re

with open('notes/cn/unit3/unit-3-notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.findall(r'<section\s+id="([^"]+)"[^>]*>.*?<h2[^>]*>(.*?)</h2>', text, re.DOTALL)
for sid, title in sections:
    # clean tags
    title_clean = re.sub(r'<[^>]+>', '', title).strip()
    print(f"{sid} : {title_clean}")
