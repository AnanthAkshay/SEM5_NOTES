import os
import re
import sys
import pypdf
from html.parser import HTMLParser

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

class HtmlFeatureExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h2_list = []
        self.h3_list = []
        self.callout_count = 0
        self.table_count = 0
        self.svg_count = 0
        self.pre_count = 0
        self.details_count = 0
        self.text_tokens = []
        self.in_script = False
        self.in_style = False
        self.cur_tag = ''
        self.cur_text = ''

    def handle_starttag(self, tag, attrs):
        self.cur_tag = tag
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '').split()

        if tag == 'table':
            self.table_count += 1
        elif tag == 'svg' and 'viewBox' in attr_dict:
            # count diagram svgs
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
        if tag == 'h2':
            if self.cur_text.strip():
                self.h2_list.append(self.cur_text.strip())
            self.cur_text = ''
        elif tag == 'h3':
            if self.cur_text.strip():
                self.h3_list.append(self.cur_text.strip())
            self.cur_text = ''
        elif tag in ('script', 'style'):
            self.in_script = False
        self.cur_tag = ''

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            if self.cur_tag in ('h2', 'h3'):
                self.cur_text += data
            words = re.findall(r'\b\w+\b', data)
            self.text_tokens.extend(words)

def clean_str(s):
    return re.sub(r'\s+', ' ', s).strip()

def check_unit_coverage(sub_id, unit_num):
    html_path = f"notes/{sub_id}/unit{unit_num}/unit-{unit_num}-notes.html"
    pdf_path = f"notes/{sub_id}/unit{unit_num}/handwritten/{sub_id}-unit{unit_num}-handwritten.pdf"

    if not os.path.exists(html_path):
        return {"status": "SKIPPED", "reason": f"HTML not found: {html_path}"}
    if not os.path.exists(pdf_path):
        return {"status": "FAIL", "reason": f"PDF not found: {pdf_path}"}

    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    extractor = HtmlFeatureExtractor()
    extractor.feed(html_content)

    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text() or ""

    pdf_words = re.findall(r'\b\w+\b', pdf_text)
    html_words = extractor.text_tokens

    # Check headings presence & order
    missing_h2 = []
    found_h2_indices = []
    last_idx = -1
    order_ok = True

    for h in extractor.h2_list:
        clean_h = re.sub(r'^\d+[\.\)]\s*', '', h).strip()
        norm_h = clean_h.replace(r'$\epsilon$', 'ϵ').replace(r'\epsilon', 'ϵ').replace('$', '').strip()
        
        idx = pdf_text.lower().find(norm_h[:18].lower())
        if idx == -1:
            # Fallback to key words search
            key_words = [w.lower() for w in re.findall(r'\b\w+\b', norm_h) if len(w) > 3]
            if key_words and all(kw in pdf_text.lower() for kw in key_words):
                idx = pdf_text.lower().find(key_words[0])
            else:
                missing_h2.append(h)
        if idx != -1:
            if idx < last_idx:
                order_ok = False
            last_idx = idx
            found_h2_indices.append(idx)

    # Key numerical tokens check: check distinctive numbers from HTML
    html_numbers = set(re.findall(r'\b\d+(?:\.\d+)?%?\b', html_content))
    # Filter out common small single digits (0, 1, 2) to focus on key constants/values
    key_numbers = [n for n in html_numbers if len(n) > 2 or '.' in n or '%' in n][:50]
    missing_numbers = [n for n in key_numbers if n not in pdf_text]

    word_ratio = len(pdf_words) / max(1, len(html_words))

    pdf_stat = os.stat(pdf_path)
    size_mb = pdf_stat.st_size / (1024 * 1024)

    passed = (len(missing_h2) == 0) and (size_mb < 15.0)

    return {
        "status": "PASS" if passed else "FAIL",
        "sub_id": sub_id,
        "unit": unit_num,
        "html_path": html_path,
        "pdf_path": pdf_path,
        "pages": total_pages,
        "size_mb": round(size_mb, 2),
        "html_words": len(html_words),
        "pdf_words": len(pdf_words),
        "word_ratio": round(word_ratio, 2),
        "h2_total": len(extractor.h2_list),
        "h2_found": len(extractor.h2_list) - len(missing_h2),
        "missing_h2": missing_h2,
        "order_ok": order_ok,
        "missing_numbers": missing_numbers[:5],
        "tables": extractor.table_count,
        "callouts": extractor.callout_count,
        "diagrams": extractor.svg_count,
        "details": extractor.details_count
    }

def main():
    target_sub = None
    target_unit = None
    check_all = False

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '--subject' and i + 1 < len(sys.argv):
            target_sub = sys.argv[i+1].lower()
        if sys.argv[i] == '--unit' and i + 1 < len(sys.argv):
            target_unit = int(sys.argv[i+1])
        if sys.argv[i] == '--all':
            check_all = True

    ALL_SUBS = ['cn', 'toc', 'ml', 'ai', 'se', 'rmipr', 'reactjs', 'evs']
    units_to_check = []

    if check_all:
        for s in ALL_SUBS:
            for u in [1, 2, 3]:
                units_to_check.append((s, u))
    elif target_sub and target_unit:
        units_to_check.append((target_sub, target_unit))
    elif target_sub:
        for u in [1, 2, 3]:
            units_to_check.append((target_sub, u))
    else:
        # Check all existing PDFs or pilot
        for s in ALL_SUBS:
            for u in [1, 2, 3]:
                pdf_p = f"notes/{s}/unit{u}/handwritten/{s}-unit{u}-handwritten.pdf"
                if os.path.exists(pdf_p):
                    units_to_check.append((s, u))
        if not units_to_check:
            units_to_check = [('toc', 1), ('cn', 1)]

    results = []
    for s, u in units_to_check:
        res = check_unit_coverage(s, u)
        results.append(res)

    print("\n=======================================================")
    print("HANDWRITTEN NOTEBOOK COVERAGE AUDIT REPORT")
    print("=======================================================")
    for r in results:
        status_badge = "✅ PASS" if r.get('status') == 'PASS' else "❌ FAIL"
        print(f"[{status_badge}] {r.get('sub_id', '').upper()} Unit {r.get('unit')}: Pages: {r.get('pages')}, Size: {r.get('size_mb')} MB, Words: {r.get('pdf_words')}/{r.get('html_words')} (Ratio: {r.get('word_ratio')}), Headings: {r.get('h2_found')}/{r.get('h2_total')}")
        if r.get('missing_h2'):
            print(f"    Missing Headings: {r['missing_h2']}")

    # Write report
    report_md = "# Handwritten Notebooks Coverage & Fidelity Audit\n\n"
    report_md += "| Subject | Unit | Pages | Size (MB) | HTML Words | PDF Words | Ratio | Headings Present | Order OK | Status |\n"
    report_md += "|---|---|---|---|---|---|---|---|---|---|\n"
    for r in results:
        if r.get('status') == 'SKIPPED':
            continue
        st = "✅ PASS" if r.get('status') == 'PASS' else "❌ FAIL"
        report_md += f"| {r['sub_id'].upper()} | Unit {r['unit']} | {r['pages']} | {r['size_mb']} | {r['html_words']:,} | {r['pdf_words']:,} | {r['word_ratio']} | {r['h2_found']}/{r['h2_total']} | {'Yes' if r['order_ok'] else 'No'} | {st} |\n"

    os.makedirs('audit', exist_ok=True)
    with open('audit/handwritten_coverage.md', 'w', encoding='utf-8') as f:
        f.write(report_md)
    print("\nSaved report to audit/handwritten_coverage.md")

if __name__ == '__main__':
    main()
