import sys
import os
import json
import pypdf

def main():
    if len(sys.argv) < 5:
        print("Usage: python postprocess_pdf.py <pdf_path> <title> <subject> <toc_json_or_file>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    title = sys.argv[2]
    subject = sys.argv[3]
    toc_arg = sys.argv[4]

    if os.path.exists(toc_arg):
        with open(toc_arg, 'r', encoding='utf-8') as f:
            toc_entries = json.load(f)
    else:
        try:
            toc_entries = json.loads(toc_arg)
        except Exception as e:
            print("Error parsing TOC JSON:", e)
            toc_entries = []

    if not os.path.exists(pdf_path):
        print("PDF does not exist:", pdf_path)
        sys.exit(1)

    reader = pypdf.PdfReader(pdf_path)
    writer = pypdf.PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    # Set metadata
    writer.add_metadata({
        '/Title': title,
        '/Author': 'SEM 5 ISE Notes',
        '/Subject': subject,
        '/Creator': 'Antigravity Handwritten Notebook Generator',
        '/Producer': 'Playwright & pypdf',
        '/Lang': 'en'
    })

    # Add outline bookmarks
    for entry in toc_entries:
        page_idx = max(0, entry.get('page', 1) - 1)
        clean_title = entry.get('title', 'Section')
        if clean_title and clean_title != 'Section':
            writer.add_outline_item(clean_title, page_idx)

    temp_path = pdf_path + ".tmp"
    with open(temp_path, 'wb') as f:
        writer.write(f)

    os.replace(temp_path, pdf_path)
    print(f"Postprocessed {pdf_path} with {len(toc_entries)} bookmarks.")

if __name__ == '__main__':
    main()
