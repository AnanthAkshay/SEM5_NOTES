import os
import re

SUBJECT_META = {
    "ml": {"name": "Machine Learning", "code": "IS51", "read_time": "~38 min read"},
    "se": {"name": "Software Engineering", "code": "IS52", "read_time": "~34 min read"},
    "cn": {"name": "Computer Networks", "code": "IS53", "read_time": "~40 min read"},
    "toc": {"name": "Theory of Computation", "code": "IS54", "read_time": "~42 min read"},
    "ai": {"name": "Artificial Intelligence", "code": "ISE552", "read_time": "~38 min read"},
    "rmipr": {"name": "Research Methodology & IPR", "code": "AL58", "read_time": "~38 min read"},
    "reactjs": {"name": "Front end Development using ReactJS", "code": "ISAEC594", "read_time": "~32 min read"},
    "evs": {"name": "Environmental Studies", "code": "HS510", "read_time": "~35 min read"},
}

def parse_and_rewrap(sub_id, unit_num, html_content):
    meta = SUBJECT_META[sub_id]
    
    # 1. Title & Description
    title_m = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    title = title_m.group(1).strip() if title_m else f"Unit {unit_num} Notes | {meta['code']}"
    
    desc_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html_content, re.IGNORECASE)
    desc = desc_m.group(1).strip() if desc_m else f"Exam-focused study notes for {meta['name']} Unit {unit_num}."
    
    # 2. H1 Headline
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)
    h1_text = h1_m.group(1).strip() if h1_m else f"Unit {unit_num}: {meta['name']}"
    
    # 3. Subheadline
    sub_m = re.search(r'<(?:p|div)[^>]*class=["\'](?:notes-subheadline|unit-subtitle)[^>]*>(.*?)</(?:p|div)>', html_content, re.IGNORECASE | re.DOTALL)
    if not sub_m:
        # Fallback: look for the first paragraph after h1
        h1_pos = html_content.find('<h1')
        p_m = re.search(r'<p[^>]*>(.*?)</p>', html_content[h1_pos:], re.IGNORECASE | re.DOTALL)
        subtitle = p_m.group(1).strip() if p_m else ""
    else:
        subtitle = sub_m.group(1).strip()
        
    # 4. Syllabus list items
    syl_list_m = re.search(r'<ul[^>]*class=["\']syllabus-list["\'][^>]*>(.*?)</ul>', html_content, re.IGNORECASE | re.DOTALL)
    if syl_list_m:
        syl_items = syl_list_m.group(1).strip()
    else:
        # Fallback to whatever list is inside syllabus-card or syllabus-box
        syl_box_m = re.search(r'class=["\'](?:syllabus-card|syllabus-box)["\'][\s\S]*?<ul[^>]*>(.*?)</ul>', html_content, re.IGNORECASE)
        syl_items = syl_box_m.group(1).strip() if syl_box_m else "<li>Complete unit syllabus topics.</li>"
        
    # 5. Source links (if present)
    source_links_m = re.search(r'<(?:div)[^>]*class=["\'](?:source-links-box|source-links-card)["\'][^>]*>([\s\S]*?)</(?:div)>', html_content, re.IGNORECASE)
    source_links_html = ""
    if source_links_m:
        source_links_html = f'\n        <div class="source-links-card">\n          {source_links_m.group(1).strip()}\n        </div>'
        
    # 6. Extract TOC Links
    aside_m = re.search(r'<aside\b[\s\S]*?</aside>', html_content, re.IGNORECASE)
    toc_links = []
    if aside_m:
        raw_links = re.findall(r'<a[^>]+href="(#[^"]+)"[^>]*>(.*?)</a>', aside_m.group(0), re.IGNORECASE | re.DOTALL)
        for href, text in raw_links:
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            # Clean up default arrows or prefixes if any
            clean_text = clean_text.replace('&times;', '').strip()
            if href not in ['#main-content', '#hero', '#']:
                toc_links.append((href, clean_text))
                
    # If no TOC links found in aside, extract from sections
    if not toc_links:
        sec_matches = re.findall(r'<section[^>]+id="([^"]+)"[\s\S]*?<h2[^>]*>(.*?)</h2>', html_content, re.IGNORECASE)
        for s_id, s_title in sec_matches:
            clean_title = re.sub(r'<[^>]+>', '', s_title).strip()
            toc_links.append((f"#{s_id}", clean_title))
            
    toc_items_html = "\n".join([f'          <li class="toc-item"><a href="{href}" class="toc-link">{text}</a></li>' for href, text in toc_links])
    
    # 7. Extract all sections VERBATIM
    sections = re.findall(r'<section\b[\s\S]*?</section>', html_content)
    sections_html = "\n\n      ".join(sections)
    
    # 8. Navigation footer buttons
    prev_btn = ""
    if unit_num > 1:
        prev_btn = f'''<a href="../unit{unit_num - 1}/unit-{unit_num - 1}-notes.html" class="nav-arrow-btn">
          <span class="nav-arrow-sub">← Previous</span>
          <span class="nav-arrow-title">Unit {unit_num - 1} Notes</span>
        </a>'''
        
    next_btn = ""
    if unit_num < 3:
        next_btn = f'''<a href="../unit{unit_num + 1}/unit-{unit_num + 1}-notes.html" class="nav-arrow-btn" style="text-align: right;">
          <span class="nav-arrow-sub">Next →</span>
          <span class="nav-arrow-title">Unit {unit_num + 1} Notes</span>
        </a>'''

    page_html = f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">

  <!-- Prevent Theme Flash -->
  <script>
    (function() {{
      var saved = localStorage.getItem('sem5_theme_v1');
      var theme = saved || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
      document.documentElement.setAttribute('data-theme', theme);
    }})();
  </script>

  <!-- Google Fonts Preconnect & Styles -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- Self-Hosted KaTeX Math Styles -->
  <link rel="stylesheet" href="../../../assets/katex/katex.min.css">

  <!-- Single Shared Notes Stylesheet -->
  <link rel="stylesheet" href="../../../css/notes.css">
</head>
<body>
  <!-- Accessibility Skip Link -->
  <a href="#main-content" class="skip-link">Skip to main notes</a>

  <!-- Top Reading Progress Bar -->
  <div id="reading-progress-bar" role="progressbar" aria-label="Reading progress" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>

  <!-- Sticky Topbar Navigation -->
  <header class="notes-topbar">
    <div class="notes-topbar-inner">
      <div class="topbar-left">
        <a href="../../../index.html#subject/{sub_id}" class="back-btn" title="Return to {meta['name']} Page">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
          <span>← {meta['code']} Overview</span>
        </a>
        <nav class="breadcrumb-trail" aria-label="Breadcrumbs">
          <span class="breadcrumb-sep">/</span>
          <a href="../../../index.html">Semester V</a>
          <span class="breadcrumb-sep">/</span>
          <a href="../../../index.html#subject/{sub_id}">{meta['name']}</a>
          <span class="breadcrumb-sep">/</span>
          <span class="breadcrumb-current">Unit {unit_num}</span>
        </nav>
      </div>

      <div class="topbar-right">
        <button id="mark-done-btn" class="pill-action-btn" data-file-id="{sub_id}-u{unit_num}-notes" title="Mark this unit as studied">
          <svg class="check-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>MARK AS DONE</span>
        </button>

        <button id="print-btn" class="pill-action-btn" title="Print notes or save as PDF">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>
          <span class="btn-label-desktop">PRINT</span>
        </button>

        <button id="theme-toggle-btn" class="pill-action-btn icon-only" aria-label="Switch Theme" title="Toggle Dark/Light Mode">
          <span id="theme-icon"></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile 'On this page' Trigger Pill (under 1024px only) -->
  <div class="mobile-toc-bar">
    <button id="mobile-toc-btn" class="mobile-toc-pill" aria-expanded="false" aria-controls="notes-sidebar">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      <span>On this page</span>
      <span class="toc-badge">Unit {unit_num}</span>
    </button>
  </div>

  <!-- Page Layout Container (max-width 1200px, 2 columns on desktop) -->
  <div class="notes-container">
    <!-- Desktop Sticky Sidebar / Mobile Sheet Modal -->
    <aside class="notes-sidebar" id="notes-sidebar" aria-label="Table of Contents">
      <div class="sidebar-header">
        <span class="sidebar-label">Unit {unit_num} contents</span>
        <button id="close-toc-btn" class="close-toc-btn" aria-label="Close Table of Contents">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <nav class="toc-nav" id="toc-nav">
        <ol class="toc-list">
{toc_items_html}
        </ol>
      </nav>
    </aside>
    <div id="sidebar-backdrop" class="sidebar-backdrop" aria-hidden="true"></div>

    <!-- Main Content Column (max-width 760px, 72ch line length) -->
    <main class="notes-main" id="main-content">
      <!-- Unit Header Hero Card -->
      <header class="notes-header-card" id="hero">
        <div class="header-mono-label">{meta['code']} · UNIT {unit_num} · {meta['read_time']}</div>
        <h1 class="notes-headline">{h1_text}</h1>
        <p class="notes-subheadline">{subtitle}</p>

        <div class="syllabus-card">
          <div class="syllabus-header-row">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
            <span>OFFICIAL SYLLABUS TOPICS COVERED</span>
          </div>
          <ul class="syllabus-list">
            {syl_items}
          </ul>
        </div>{source_links_html}
      </header>

      <!-- Exact Article Content Sections (preserved byte-for-byte) -->
      {sections_html}

      <!-- Unit Navigation Footer -->
      <footer class="unit-nav-footer">
        {prev_btn}
        <a href="../../../index.html#subject/{sub_id}" class="nav-arrow-btn nav-back-center" style="text-align: center;">
          <span class="nav-arrow-sub">Course Portal</span>
          <span class="nav-arrow-title">{meta['code']} Overview</span>
        </a>
        {next_btn}
      </footer>

      <!-- Prescribed Syllabus Disclaimer -->
      <p class="reference-disclaimer">
        AI-assisted study notes written from the official syllabus. Verify against the prescribed textbook and your faculty's notes before the exam.
      </p>
    </main>
  </div>

  <!-- Shared Scripts: KaTeX Auto-Render & Notes Client Engine -->
  <script src="../../../assets/katex/katex.min.js"></script>
  <script src="../../../assets/katex/contrib/auto-render.min.js"></script>
  <script src="../../../js/notes.js"></script>
</body>
</html>'''

    return page_html

if __name__ == "__main__":
    import hashlib
    import json

    with open("audit/content_hashes_before.json", "r", encoding="utf-8") as f:
        baseline_hashes = json.load(f)

    subjects = ["ml", "se", "cn", "toc", "ai", "rmipr", "reactjs", "evs"]
    processed = 0
    hash_matches = 0

    for sub in subjects:
        for unit in [1, 2, 3]:
            path = f"notes/{sub}/unit{unit}/unit-{unit}-notes.html"
            if not os.path.exists(path):
                print(f"File not found: {path}")
                continue

            with open(path, "r", encoding="utf-8") as f:
                original_html = f.read()

            new_html = parse_and_rewrap(sub, unit, original_html)

            # Check that content hash of sections matches baseline
            new_sections = re.findall(r'<section\b[\s\S]*?</section>', new_html)
            new_norm = re.sub(r'\s+', ' ', "".join(new_sections)).strip()
            new_hash = hashlib.sha256(new_norm.encode("utf-8")).hexdigest()

            key = f"{sub}_u{unit}"
            expected_hash = baseline_hashes[key]["hash"]

            if new_hash == expected_hash:
                hash_matches += 1
            else:
                print(f"WARNING: Hash mismatch for {key}! Expected: {expected_hash}, Got: {new_hash}")

            with open(path, "w", encoding="utf-8") as f:
                f.write(new_html)

            processed += 1
            print(f"Standardized {sub.upper()} Unit {unit} -> {path} (Sections: {len(new_sections)}, Hash Match: {new_hash == expected_hash})")

    print(f"\nCOMPLETED: Processed {processed} files. Exact content hash matches: {hash_matches}/{processed}")
