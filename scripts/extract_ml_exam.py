import os
import pypdf

os.makedirs('audit/scratch/ml_exam', exist_ok=True)
reader = pypdf.PdfReader('notes/ml/practice/ml-cie-1-2-see.pdf')
print(f"Total pages: {len(reader.pages)}")

for i, page in enumerate(reader.pages):
    for j, img in enumerate(page.images):
        ext = img.name.split('.')[-1] if '.' in img.name else 'png'
        filename = f'audit/scratch/ml_exam/page_{i+1}_{j+1}.{ext}'
        with open(filename, 'wb') as f:
            f.write(img.data)
        print(f"Extracted: {filename} ({len(img.data)} bytes)")
