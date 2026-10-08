import os
import json
import glob
import pypdf

ALL_SUBS = ['ai', 'cn', 'evs', 'ml', 'reactjs', 'rmipr', 'se', 'toc']
stats = {}

for s in ALL_SUBS:
    stats[s] = {}
    for u in [1, 2, 3]:
        pdf_path = f"notes/{s}/unit{u}/handwritten/{s}-unit{u}-handwritten.pdf"
        html_path = f"notes/{s}/unit{u}/handwritten/{s}-unit{u}-handwritten.html"
        if os.path.exists(pdf_path):
            reader = pypdf.PdfReader(pdf_path)
            pages = len(reader.pages)
            pdf_bytes = os.path.getsize(pdf_path)
            html_bytes = os.path.getsize(html_path)
            stats[s][str(u)] = {
                "pages": pages,
                "pdfSizeMB": f"{pdf_bytes / (1024 * 1024):.2f} MB",
                "pdfSizeBytes": pdf_bytes,
                "htmlSizeKB": f"{html_bytes / 1024:.0f} KB",
                "htmlSizeBytes": html_bytes
            }

os.makedirs('audit', exist_ok=True)
with open('audit/handwritten_stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, indent=2)

print("Saved audit/handwritten_stats.json")
