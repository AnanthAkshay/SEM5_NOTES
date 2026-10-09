import json, os, re
from pypdf import PdfReader

# 1. Collect accurate metadata for all 24 PDFs
SUBS = ['ai', 'cn', 'evs', 'ml', 'reactjs', 'rmipr', 'se', 'toc']
pdf_stats = {}

for s in SUBS:
    pdf_stats[s] = {}
    for u in [1, 2, 3]:
        pdf_p = f"notes/{s}/unit{u}/handwritten/{s}-unit{u}-handwritten.pdf"
        if os.path.exists(pdf_p):
            reader = PdfReader(pdf_p)
            pages = len(reader.pages)
            size_bytes = os.path.getsize(pdf_p)
            size_mb = size_bytes / (1024 * 1024)
            pdf_stats[s][u] = {
                "pages": pages,
                "sizeMB": f"{size_mb:.2f} MB",
                "sizeBytes": size_bytes
            }

# 2. Read data/subjects.js
with open('data/subjects.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract json inside window.SEM5_DATA = ...;
match = re.search(r'window\.SEM5_DATA\s*=\s*(\{.*?\});?\s*$', content, re.DOTALL)
if not match:
    raise ValueError("Could not find window.SEM5_DATA in data/subjects.js")

data = json.loads(match.group(1))

total_all_files = 0
total_all_size_bytes = 0

for sub in data['subjects']:
    sub_id = sub['id']
    is_lab = sub.get('isLab', False) or ('lab' in sub_id.lower()) or sub.get('category') == 'lab'
    if is_lab:
        sub['isLab'] = True

    sub_file_count = 0
    sub_size_bytes = 0

    for unit in sub.get('units', []):
        u_num = unit.get('unitNumber')
        files = unit.get('files', [])

        # Filter out any handwritten-web or old handwritten entries
        clean_files = [f for f in files if f.get('type') not in ('handwritten', 'handwritten-web') and 'handwritten' not in f.get('id', '')]

        if isinstance(u_num, int) and u_num in [1, 2, 3] and sub_id in pdf_stats and u_num in pdf_stats[sub_id]:
            stat = pdf_stats[sub_id][u_num]
            hw_entry = {
                "id": f"{sub_id}-u{u_num}-handwritten-pdf",
                "title": "Handwritten notebook (PDF)",
                "originalName": f"{sub_id}-unit{u_num}-handwritten.pdf",
                "path": f"notes/{sub_id}/unit{u_num}/handwritten/{sub_id}-unit{u_num}-handwritten.pdf",
                "type": "handwritten",
                "tag": "PDF Notebook",
                "generated": True,
                "pages": stat["pages"],
                "size": stat["sizeMB"],
                "sizeBytes": stat["sizeBytes"],
                "previewImage": f"notes/{sub_id}/unit{u_num}/handwritten/{sub_id}-unit{u_num}-preview.webp",
                "sourceHtml": f"notes/{sub_id}/unit{u_num}/unit-{u_num}-notes.html"
            }
            # Insert after notes entry if present
            notes_idx = next((i for i, f in enumerate(clean_files) if f.get('type') == 'notes'), -1)
            if notes_idx != -1:
                clean_files.insert(notes_idx + 1, hw_entry)
            else:
                clean_files.insert(0, hw_entry)
            unit['isSyllabusOnly'] = False
        else:
            if isinstance(u_num, int) and u_num in [4, 5]:
                unit['isSyllabusOnly'] = True
            elif is_lab:
                unit['isSyllabusOnly'] = True

        unit['files'] = clean_files
        sub_file_count += len(clean_files)
        for f in clean_files:
            sb = f.get('sizeBytes', 0)
            sub_size_bytes += sb

    sub['fileCount'] = sub_file_count
    sub['totalSizeBytes'] = sub_size_bytes
    sub['totalSize'] = f"{sub_size_bytes / (1024 * 1024):.1f} MB" if sub_size_bytes > 0 else "0 MB"
    total_all_files += sub_file_count
    total_all_size_bytes += sub_size_bytes

# Update site metadata stats
if 'meta' in data:
    data['meta']['totalFiles'] = total_all_files
    data['meta']['totalSizeBytes'] = total_all_size_bytes
    data['meta']['totalSize'] = f"{total_all_size_bytes / (1024 * 1024):.1f} MB"

new_js = f"""/**
 * SEM 5 · ISE Notes - Central Data Store
 * Source of Truth: ISE III Year Syllabus (2024 Batch Final) - V Semester
 * Total Credits: 22 (L: 18, T: 1, P: 3)
 */

window.SEM5_DATA = {json.dumps(data, indent=2)};
"""

with open('data/subjects.js', 'w', encoding='utf-8') as f:
    f.write(new_js)

print(f"Successfully updated data/subjects.js! Total files: {total_all_files}, Total size: {total_all_size_bytes / (1024*1024):.2f} MB")
