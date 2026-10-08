"""
extract_rmipr_exam.py - Extract and inspect authentic RMIPR exam questions
"""

import pypdf

files = [
    "notes/rmipr/practice/rmipr-cie-1-and-2.pdf",
    "notes/rmipr/practice/rmipr-makeup-apr-2025.pdf",
    "notes/rmipr/practice/rmipr-see-feb-mar-2025.pdf"
]

for filepath in files:
    print(f"\n==================== {filepath} ====================")
    try:
        reader = pypdf.PdfReader(filepath)
        print(f"Num pages: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            print(f"--- Page {i+1} ({len(text)} chars) ---")
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            for line in lines[:35]:
                print(line)
            if len(lines) > 35:
                print(f"... and {len(lines) - 35} more lines ...")
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
