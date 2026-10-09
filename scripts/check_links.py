import os, re, urllib.request, urllib.error, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=======================================================")
print("COMPREHENSIVE LINK INTEGRITY CHECK")
print("=======================================================")

# 1. Collect all HTML files
html_files = []
for root, dirs, files in os.walk(REPO_ROOT):
    # skip node_modules, .git, audit, build, scratch
    if any(skip in root.replace('\\', '/') for skip in ['/node_modules', '/.git', '/audit', '/build', '/scratch']):
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f"Scanning {len(html_files)} HTML pages and data/subjects.js...")

internal_errors = []
external_links = set()
total_links_checked = 0

# Check HTML files
for hf in html_files:
    rel_h = os.path.relpath(hf, REPO_ROOT).replace('\\', '/')
    base_dir = os.path.dirname(hf)
    with open(hf, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()

    # Find anchors and hrefs
    anchors = set(re.findall(r'id=["\']([^"\']+)["\']', content))

    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for l in links:
        total_links_checked += 1
        l = l.strip()
        if not l or l.startswith('javascript:') or l.startswith('mailto:') or l.startswith('data:'):
            continue
        if l.startswith('http://') or l.startswith('https://'):
            external_links.add(l)
            continue

        # Internal link
        clean_target = l.split('?')[0]
        frag = ''
        if '#' in clean_target:
            clean_target, frag = clean_target.split('#', 1)

        if clean_target:
            target_path = os.path.normpath(os.path.join(base_dir, clean_target))
            if not os.path.exists(target_path):
                internal_errors.append((rel_h, l, "File does not exist"))
            else:
                # Check case sensitive match
                parts = clean_target.replace('\\', '/').split('/')
                curr = base_dir
                case_err = False
                for p in parts:
                    if not p or p == '.': continue
                    if p == '..':
                        curr = os.path.dirname(curr)
                        continue
                    try:
                        entries = os.listdir(curr)
                        if p not in entries:
                            case_err = True
                            break
                        curr = os.path.join(curr, p)
                    except OSError:
                        case_err = True
                        break
                if case_err:
                    internal_errors.append((rel_h, l, "Case sensitivity mismatch"))

        if frag and not clean_target:
            # same-page fragment
            if frag not in anchors:
                internal_errors.append((rel_h, l, f"Anchor #{frag} not found on page"))

print(f"Internal links checked: {total_links_checked}")
print(f"Internal link errors: {len(internal_errors)}")
for page, link, err in internal_errors[:15]:
    print(f"  [{err}] in {page} -> {link}")

# Check data/subjects.js external links
import json
with open(os.path.join(REPO_ROOT, 'data/subjects.js'), 'r', encoding='utf-8') as fh:
    sj_text = fh.read()
m = re.search(r'window\.SEM5_DATA\s*=\s*(\{.*?\});?\s*$', sj_text, re.DOTALL)
if m:
    s_data = json.loads(m.group(1))
    for sub in s_data.get('subjects', []):
        syl = sub.get('syllabus', {})
        for u in syl.get('units', []):
            for lk in u.get('links', []):
                if 'url' in lk and lk['url'].startswith('http'):
                    external_links.add(lk['url'])

print(f"\nUnique external links collected: {len(external_links)}")
print("Checking top sample external links (timeout 3s)...")
dead_external = []
alive_external = []

for url in sorted(external_links)[:25]:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=3, context=ctx) as resp:
            code = resp.getcode()
            if code < 400:
                alive_external.append((url, code))
            else:
                dead_external.append((url, code))
    except urllib.error.HTTPError as e:
        dead_external.append((url, e.code))
    except Exception as e:
        dead_external.append((url, str(e)))

print(f"Sample checked: {len(alive_external)} ALIVE, {len(dead_external)} DEAD/BLOCKED")
for url, err in dead_external:
    print(f"  DEAD/TIMEOUT: {url} ({err})")
