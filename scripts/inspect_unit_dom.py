import re

def inspect(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    print(f"=== {path} ===")
    print("Length:", len(html))
    print("h2 count:", len(re.findall(r'<h2', html)))
    print("h3 count:", len(re.findall(r'<h3', html)))
    print("svg count:", len(re.findall(r'<svg', html)))
    print("table count:", len(re.findall(r'<table', html)))
    print("details count:", len(re.findall(r'<details', html)))
    callout_matches = re.findall(r'class=[\'"][^\'"]*callout[^\'"]*[\'"]', html)
    print("callout count:", len(callout_matches))
    # Check section IDs
    h2_ids = re.findall(r'<h2[^>]*id=[\'"]([^\'"]+)[\'"]', html)
    print("h2 IDs:", h2_ids[:5], f"... total {len(h2_ids)}")

inspect('notes/toc/unit1/unit-1-notes.html')
inspect('notes/cn/unit1/unit-1-notes.html')
