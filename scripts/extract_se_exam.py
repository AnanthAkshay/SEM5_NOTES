import os
import pypdf

os.makedirs('audit/scratch/se_exam', exist_ok=True)
reader = pypdf.PdfReader('notes/se/practice/se-cie-1-and-2.pdf')
print(f"Total pages: {len(reader.pages)}")

for i, page in enumerate(reader.pages):
    for j, img in enumerate(page.images):
        img_name = f"audit/scratch/se_exam/page_{i+1}_{j+1}.jpg"
        with open(img_name, "wb") as f:
            f.write(img.data)
        print(f"Saved {img_name} ({len(img.data)} bytes)")
