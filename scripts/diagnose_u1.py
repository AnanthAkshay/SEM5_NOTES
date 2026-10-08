from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', headless=True)
    page = browser.new_page()
    
    # Track 404s
    failed_reqs = []
    page.on('response', lambda resp: failed_reqs.append((resp.status, resp.url)) if resp.status >= 400 else None)

    page.set_viewport_size({"width": 320, "height": 800})
    page.goto('http://localhost:8088/SEM5_NOTES/notes/cn/unit1/unit-1-notes.html', wait_until='networkidle')

    # Find overflowing elements
    overflow_elements = page.evaluate('''() => {
        const elements = [];
        const winW = window.innerWidth;
        document.querySelectorAll('*').forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.right > winW + 1) {
                elements.push({
                    tag: el.tagName,
                    id: el.id,
                    className: el.className,
                    width: rect.width,
                    right: rect.right
                });
            }
        });
        return elements;
    }''')

    print("Failed requests (status >= 400):")
    for status, url in failed_reqs:
        print(f"  {status}: {url}")

    print("\nOverflowing elements at 320px:")
    for el in overflow_elements[:10]:
        print(f"  <{el['tag']} id='{el['id']}' class='{el['className']}'> width={el['width']}, right={el['right']}")

    browser.close()
