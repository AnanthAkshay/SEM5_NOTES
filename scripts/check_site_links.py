import os
import re
import urllib.parse
import urllib.request
import concurrent.futures
from html.parser import HTMLParser

class AnchorLinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if 'id' in attr_dict:
            self.ids.add(attr_dict['id'])
        if tag == 'a' and 'name' in attr_dict:
            self.ids.add(attr_dict['name'])
        if tag in ('a', 'link') and 'href' in attr_dict:
            self.hrefs.append(attr_dict['href'].strip())
        if tag in ('script', 'img', 'iframe') and 'src' in attr_dict:
            self.hrefs.append(attr_dict['src'].strip())

def check_site():
    print("=== Scanning Internal Files & Anchors ===")
    fs_files = {}
    html_anchors = {}
    html_hrefs = {}

    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root or 'audit' in root:
            continue
        for f in files:
            rel = os.path.normpath(os.path.join(root, f)).replace('\\', '/')
            if rel.startswith('./'):
                rel = rel[2:]
            fs_files[rel.lower()] = rel

    # Collect IDs and links from HTML files
    for low, orig in fs_files.items():
        if orig.endswith('.html'):
            try:
                with open(orig, 'r', encoding='utf-8', errors='ignore') as fp:
                    parser = AnchorLinkParser()
                    parser.feed(fp.read())
                    html_anchors[low] = parser.ids
                    html_hrefs[low] = parser.hrefs
            except Exception as e:
                pass

    print(f"Indexed {len(fs_files)} files and {len(html_anchors)} HTML documents.")

    internal_errors = []
    external_links = set()

    # Scan HTML files for links
    for low, hrefs in html_hrefs.items():
        orig = fs_files[low]
        for href in hrefs:
            if not href or href.startswith('javascript:') or href.startswith('mailto:') or href.startswith('data:'):
                continue
            if href.startswith('http://') or href.startswith('https://'):
                external_links.add(href)
            elif href.startswith('#'):
                # Same page anchor
                anchor_id = href[1:]
                if anchor_id and anchor_id not in html_anchors.get(low, set()):
                    if not (orig == 'index.html' and (anchor_id.startswith('subject=') or anchor_id in ['scheme', 'home', 'subjects-section'])):
                        internal_errors.append(f"Broken anchor '{href}' in {orig}")
            else:
                parsed = urllib.parse.urlparse(href)
                path_part = parsed.path
                frag = parsed.fragment
                
                curr_dir = os.path.dirname(orig)
                target_rel = os.path.normpath(os.path.join(curr_dir, path_part)).replace('\\', '/')
                if target_rel.startswith('./'):
                    target_rel = target_rel[2:]
                target_low = target_rel.lower()

                if target_low not in fs_files:
                    internal_errors.append(f"Missing file target '{href}' in {orig} (resolved to {target_rel})")
                elif frag and target_low in html_anchors:
                    if frag not in html_anchors[target_low]:
                        internal_errors.append(f"Missing anchor '#{frag}' in target '{target_rel}' referenced from {orig}")

    # Extract external links from data/subjects.js
    with open('data/subjects.js', 'r', encoding='utf-8') as f:
        js_text = f.read()

    js_ext_urls = re.findall(r'https?://[^\s\'"<>]+', js_text)
    for u in js_ext_urls:
        external_links.add(u.rstrip('",\''))

    print(f"\n=== Internal Link Analysis ===")
    print(f"Total internal link errors: {len(internal_errors)}")
    for err in internal_errors[:15]:
        print(f"  {err}")

    # Check external links
    print(f"\n=== Checking {len(external_links)} External Links ===")
    dead_links = []
    passed_links = []

    def check_ext_url(url):
        req = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            }
        )
        try:
            req.get_method = lambda: 'HEAD'
            with urllib.request.urlopen(req, timeout=8) as resp:
                code = resp.getcode()
                if code < 400:
                    return (url, code, None)
        except Exception:
            try:
                req.get_method = lambda: 'GET'
                req.add_header('Range', 'bytes=0-1024')
                with urllib.request.urlopen(req, timeout=10) as resp:
                    return (url, resp.getcode(), None)
            except urllib.error.HTTPError as he:
                return (url, he.code, str(he))
            except Exception as e:
                return (url, 0, str(e))

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(check_ext_url, url): url for url in external_links}
        for future in concurrent.futures.as_completed(future_to_url):
            url, code, err = future.result()
            if code and 200 <= code < 400:
                passed_links.append((url, code))
            elif code in (403, 401, 405, 418, 429):
                passed_links.append((url, f"UP ({code} protected)"))
            else:
                dead_links.append((url, code, err))

    print(f"External Links Verified: {len(passed_links)} alive/responding, {len(dead_links)} failed/flagged.")
    if dead_links:
        print("Flagged external links:")
        for url, code, err in dead_links:
            print(f"  [{code}] {url} -> {err}")

    return internal_errors, dead_links

if __name__ == '__main__':
    check_site()
