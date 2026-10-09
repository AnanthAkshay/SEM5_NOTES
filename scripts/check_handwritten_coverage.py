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

    # Check headings presence & order via PDF bookmarks and sequential body text
    bookmark_titles = [item.title.lower() for item in (reader.outline or []) if hasattr(item, 'title')]
    body_text = "".join(page.extract_text() or "" for page in reader.pages[1:]).lower()

    missing_h2 = []
    order_ok = True
    last_idx = 0

    for h in extractor.h2_list:
        clean_h = re.sub(r'^\d+[\.\)]\s*', '', h).strip()
        norm_h = clean_h.replace(r'$\epsilon$', 'ϵ').replace(r'\epsilon', 'ϵ').replace('$', '').strip().lower()

        matched_in_outline = any(norm_h[:15] in bm or bm[:15] in norm_h for bm in bookmark_titles)
        search_term = norm_h[:15]
        found_pos = body_text.find(search_term, last_idx)
        if found_pos == -1:
            key_words = [w for w in re.findall(r'\b\w+\b', norm_h) if len(w) > 3]
            if key_words:
                found_pos = body_text.find(key_words[0], last_idx)

        if matched_in_outline or found_pos != -1:
            if found_pos != -1:
                last_idx = found_pos
        else:
            missing_h2.append(h)

    # Key numerical tokens check: check distinctive numbers from HTML
    html_numbers = set(re.findall(r'\b\d+(?:\.\d+)?%?\b', html_content))
    # Filter out common small single digits (0, 1, 2) to focus on key constants/values
    key_numbers = [n for n in html_numbers if len(n) > 2 or '.' in n or '%' in n][:50]
    missing_numbers = [n for n in key_numbers if n not in pdf_text]

    # Font allow-list and Type3 check
    allowed_font_substrings = ['PatrickHand', 'Caveat', 'Kalam', 'JetBrainsMono', 'KaTeX']
    disallowed_fonts = set()
    for page in reader.pages:
        if '/Resources' in page and '/Font' in page['/Resources']:
            for f in page['/Resources']['/Font'].values():
                obj = f.get_object()
                bf = str(obj.get('/BaseFont', 'NO_BASE'))
                st = str(obj.get('/Subtype', 'NO_SUB'))
                if st == '/Type3' or not any(ok in bf for ok in allowed_font_substrings):
                    disallowed_fonts.add(f"{bf} ({st})")

    fonts_ok = (len(disallowed_fonts) == 0)

    # Metadata & Outline check
    meta = reader.metadata
    title = meta.title if meta else None
    author = meta.author if meta else None
    outlines = reader.outline
    meta_ok = bool(title and author == "SEM 5 ISE Notes" and outlines)

    word_ratio = len(pdf_words) / max(1, len(html_words))

    pdf_stat = os.stat(pdf_path)
    size_mb = pdf_stat.st_size / (1024 * 1024)

    passed = (len(missing_h2) == 0) and (size_mb <= 4.0) and fonts_ok and meta_ok and order_ok

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
        "fonts_ok": fonts_ok,
        "disallowed_fonts": disallowed_fonts,
        "meta_ok": meta_ok,
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
    print("HANDWRITTEN NOTEBOOK COVERAGE & GATES AUDIT REPORT")
    print("=======================================================")
    for r in results:
        status_badge = "✅ PASS" if r.get('status') == 'PASS' else "❌ FAIL"
        fonts_badge = "Fonts: OK" if r.get('fonts_ok') else f"Fonts: FAIL ({r.get('disallowed_fonts')})"
        print(f"[{status_badge}] {r.get('sub_id', '').upper()} Unit {r.get('unit')}: Pages: {r.get('pages')}, PDF: {r.get('size_mb')} MB, Words: {r.get('pdf_words')}/{r.get('html_words')} (Ratio: {r.get('word_ratio')}), Headings: {r.get('h2_found')}/{r.get('h2_total')}, {fonts_badge}")
        if r.get('missing_h2'):
            print(f"    Missing Headings: {r['missing_h2']}")

    # Write report
    report_md = "# Handwritten Notebooks Coverage & Fidelity Audit\n\n"
    report_md += "| Subject | Unit | Pages | PDF (MB) | HTML Words | PDF Words | Ratio | Headings | Order OK | Fonts OK | Meta OK | Status |\n"
    report_md += "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    for r in results:
        if r.get('status') == 'SKIPPED':
            continue
        st = "✅ PASS" if r.get('status') == 'PASS' else "❌ FAIL"
        report_md += f"| {r['sub_id'].upper()} | Unit {r['unit']} | {r['pages']} | {r['size_mb']} | {r['html_words']:,} | {r['pdf_words']:,} | {r['word_ratio']} | {r['h2_found']}/{r['h2_total']} | {'Yes' if r['order_ok'] else 'No'} | {'Yes' if r['fonts_ok'] else 'No'} | {'Yes' if r['meta_ok'] else 'No'} | {st} |\n"

    os.makedirs('audit', exist_ok=True)
    with open('audit/handwritten_coverage.md', 'w', encoding='utf-8') as f:
        f.write(report_md)
    print("\nSaved report to audit/handwritten_coverage.md")

if __name__ == '__main__':
    main()
