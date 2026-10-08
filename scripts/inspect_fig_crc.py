with open('notes/cn/unit2/unit-2-notes.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if any(k in l for k in ['id="sec-4"', 'id="sec-5"', 'id="fig-crc-division"', 'id="crc-explorer-widget"']):
        print(f"Line {i+1}: {l.strip()[:70]}")
