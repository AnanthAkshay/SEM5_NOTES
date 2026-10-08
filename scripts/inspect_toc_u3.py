import re

with open('notes/toc/unit3/unit-3-notes.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('fig-pda-trace in text?', 'fig-pda-trace' in text)
print('pda-simulator-widget in text?', 'pda-simulator-widget' in text)
print('fig-ambiguity-trees in text?', 'fig-ambiguity-trees' in text)
sec7_pos = text.find('id="sec-7"')
sec8_pos = text.find('id="revision-sheet"')
print('sec-7 snippet around end:')
print(text[sec8_pos-500:sec8_pos])
