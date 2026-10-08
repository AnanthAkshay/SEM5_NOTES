import os
import re
from html.parser import HTMLParser

class NotesStatsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h2_count = 0
        self.h3_count = 0
        self.callout_count = 0
        self.table_count = 0
        self.svg_count = 0
        self.pre_count = 0
        self.details_count = 0
        self.text_tokens = []
        self.in_script = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '').split()
        
        if tag == 'h2':
            self.h2_count += 1
        elif tag == 'h3':
            self.h3_count += 1
        elif tag == 'table':
            self.table_count += 1
        elif tag == 'svg':
            self.svg_count += 1
        elif tag == 'pre':
            self.pre_count += 1
        elif tag == 'details':
            self.details_count += 1
        elif tag in ('script', 'style'):
            self.in_script = True

        if any('callout' in c for c in classes):
            self.callout_count += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.in_script = False

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            words = re.findall(r'\b\w+\b', data)
            self.text_tokens.extend(words)

SUBJECTS = [
    ('ai', 'AI', 'ISE552'),
    ('cn', 'CN', 'IS53'),
    ('evs', 'EVS', 'HS510'),
    ('ml', 'ML', 'IS51'),
    ('reactjs', 'REACT_JS', 'ISAEC594'),
    ('rmipr', 'RMIPR', 'AL58'),
    ('se', 'SE', 'IS52'),
    ('toc', 'TOC', 'IS54')
]

def analyze_file(rel_path):
    with open(rel_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = NotesStatsParser()
    parser.feed(content)

    # Formulas in HTML notes:
    # They are written as $...$ or $$...$$ or \(...\) or \[...\] which KaTeX auto-render renders client-side.
    # Count inline ($...$ and \(...\)) and display ($$...$$ and \[...\])
    display_formulas = len(re.findall(r'\$\$[\s\S]*?\$\$', content)) + len(re.findall(r'\\\[[\s\S]*?\\\]', content))
    # Replace display formulas first to not double count
    temp = re.sub(r'\$\$[\s\S]*?\$\$', '', content)
    temp = re.sub(r'\\\[[\s\S]*?\\\]', '', temp)
    inline_formulas = len(re.findall(r'(?<!\$)\$(?!\$)[\s\S]*?(?<!\$)\$(?!\$)', temp)) + len(re.findall(r'\\\(.*?\\\)', temp))
    total_formulas = display_formulas + inline_formulas

    return {
        'h2': parser.h2_count,
        'h3': parser.h3_count,
        'callouts': parser.callout_count,
        'tables': parser.table_count,
        'svgs': parser.svg_count,
        'formulas': total_formulas,
        'code_blocks': parser.pre_count,
        'details': parser.details_count,
        'word_count': len(parser.text_tokens)
    }

def main():
    rows = []
    print("| Subject | Unit | File Path | Sections (h2/h3) | Callouts | Tables | SVG Diagrams | KaTeX Formulas | Code Blocks | Details Solved | Words |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    
    total_sections = 0
    total_callouts = 0
    total_tables = 0
    total_svgs = 0
    total_formulas = 0
    total_code = 0
    total_details = 0
    total_words = 0

    for sub_id, sub_label, code in SUBJECTS:
        for u in [1, 2, 3]:
            path = f"notes/{sub_id}/unit{u}/unit-{u}-notes.html"
            if not os.path.exists(path):
                continue
            stats = analyze_file(path)
            h_str = f"{stats['h2']} / {stats['h3']}"
            print(f"| {sub_label} ({code}) | Unit {u} | `{path}` | {h_str} | {stats['callouts']} | {stats['tables']} | {stats['svgs']} | {stats['formulas']} | {stats['code_blocks']} | {stats['details']} | {stats['word_count']:,} |")
            
            total_sections += stats['h2'] + stats['h3']
            total_callouts += stats['callouts']
            total_tables += stats['tables']
            total_svgs += stats['svgs']
            total_formulas += stats['formulas']
            total_code += stats['code_blocks']
            total_details += stats['details']
            total_words += stats['word_count']

    print(f"| **TOTAL (24 Units)** | **-** | **-** | **{total_sections}** | **{total_callouts}** | **{total_tables}** | **{total_svgs}** | **{total_formulas}** | **{total_code}** | **{total_details}** | **{total_words:,}** |")

if __name__ == '__main__':
    main()
