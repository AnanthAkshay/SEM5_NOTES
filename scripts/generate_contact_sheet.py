import os
import pypdfium2 as pdfium

subjects = ['ai', 'cn', 'evs', 'ml', 'reactjs', 'rmipr', 'se', 'toc']
out_dir = 'audit/screens/initial_diagnosis'
os.makedirs(out_dir, exist_ok=True)

html_out = """<!DOCTYPE html>
<html>
<head>
<title>Initial Diagnosis Contact Sheet</title>
<style>
  body { font-family: sans-serif; background: #1e293b; color: white; padding: 20px; }
  h1 { text-align: center; margin-bottom: 24px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }
  .card { background: #334155; padding: 12px; border-radius: 8px; }
  .card img { width: 100%; height: auto; border: 1px solid #475569; border-radius: 4px; }
  .card-title { font-weight: bold; margin-bottom: 6px; font-size: 14px; }
</style>
</head>
<body>
<h1>SEM 5 Handwritten Notebooks - Initial Diagnosis Contact Sheet</h1>
<div class="grid">
"""

count = 0
for sub in subjects:
    pdf_path = f'notes/{sub}/unit1/handwritten/{sub}-unit1-handwritten.pdf'
    if not os.path.exists(pdf_path):
        continue
    pdf = pdfium.PdfDocument(pdf_path)
    total_p = len(pdf)
    # Pick pages: cover (0), text (1), and a mid page with diagrams/tables (2, 3, or 4)
    pages_to_pick = [0, 1, min(2, total_p-1), min(3, total_p-1)]
    for p_num in pages_to_pick:
        img_name = f'{sub}_u1_p{p_num+1}.png'
        img_path = os.path.join(out_dir, img_name)
        page = pdf[p_num]
        image = page.render(scale=1.5).to_pil()
        image.save(img_path)
        count += 1
        html_out += f"""
        <div class="card">
          <div class="card-title">{sub.upper()} Unit 1 - Page {p_num+1} of {total_p}</div>
          <img src="{img_name}" loading="lazy" />
        </div>
        """

html_out += """
</div>
</body>
</html>
"""

with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_out)

print(f"Rendered {count} sample pages across all 8 subjects into {out_dir}/index.html")
