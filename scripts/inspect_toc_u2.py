import re

with open('notes/toc/unit2/unit-2-notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

secs = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>.*?<h2[^>]*>(.*?)</h2>', text, re.DOTALL)
for sid, t in secs:
    print(f"{sid} : {re.sub('<[^>]+>', '', t).strip()}")
