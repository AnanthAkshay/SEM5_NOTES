import os
import re

def check_paths():
    fs = {}
    for root, dirs, files in os.walk('.'):
        if '.git' in root:
            continue
        for f in files:
            rel = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
            if rel.startswith('./'):
                rel = rel[2:]
            fs[rel.lower()] = rel

    print(f'Total files indexed in filesystem: {len(fs)}')

    # Check data/subjects.js
    with open('data/subjects.js', 'r', encoding='utf-8') as f:
        text = f.read()

    matches = re.findall(r'(?:path|originalPath|preview)\s*:\s*[\'"]([^\'"]+)[\'"]', text)
    errors = []
    for p in matches:
        clean = p.lstrip('./').replace('\\', '/')
        low = clean.lower()
        if low not in fs:
            errors.append(f'MISSING FILE: {p}')
        elif fs[low] != clean:
            errors.append(f'CASE MISMATCH: in subjects.js: "{clean}" vs on disk: "{fs[low]}"')

    # Also check index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    html_refs = re.findall(r'(?:src|href)\s*=\s*[\'"]([^\'":#]+)[\'"]', html)
    for ref in html_refs:
        clean = ref.lstrip('./').replace('\\', '/')
        if clean.startswith('data:') or clean.startswith('http'):
            continue
        low = clean.lower()
        if low not in fs:
            errors.append(f'MISSING FILE IN index.html: {ref}')
        elif fs[low] != clean:
            errors.append(f'CASE MISMATCH in index.html: "{clean}" vs on disk: "{fs[low]}"')

    if errors:
        print(f'Found {len(errors)} issues:')
        for e in errors:
            print(' ', e)
    else:
        print('SUCCESS: All checked paths match existing files on disk with exact case!')

if __name__ == '__main__':
    check_paths()
