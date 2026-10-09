/**
 * SEM 5 · ISE Notes - Handwritten-Style Notebook Generator
 * Converts complete HTML unit notes page into an authentic handwritten notebook PDF.
 * Uses Playwright, KaTeX, local OFL Google Fonts, Rough.js, and exact A4 pagination.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const REPO_ROOT = path.resolve(__dirname, '..');

// Subject Configurations & Pen Personalities
const SUBJECT_CONFIGS = {
  toc: {
    code: 'IS54',
    name: 'Theory of Computation',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#163660',
    inkDark: '#0f172a',
    inkAccent: '#6b21a8'
  },
  cn: {
    code: 'IS53',
    name: 'Computer Networks',
    fontBody: "'Kalam', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#1b3252',
    inkDark: '#0a0f1d',
    inkAccent: '#1d4ed8'
  },
  ai: {
    code: 'ISE552',
    name: 'Artificial Intelligence',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#1e3a8a',
    inkDark: '#111827',
    inkAccent: '#7c3aed'
  },
  ml: {
    code: 'IS51',
    name: 'Machine Learning',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#163e54',
    inkDark: '#0f172a',
    inkAccent: '#0369a1'
  },
  reactjs: {
    code: 'ISAEC594',
    name: 'ReactJS',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#1e293b',
    inkDark: '#0284c7',
    inkAccent: '#0284c7'
  },
  rmipr: {
    code: 'AL58',
    name: 'Research Methodology & IPR',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#1e3a5f',
    inkDark: '#111827',
    inkAccent: '#b45309'
  },
  se: {
    code: 'IS52',
    name: 'Software Engineering',
    fontBody: "'Kalam', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#172554',
    inkDark: '#0f172a',
    inkAccent: '#2563eb'
  },
  evs: {
    code: 'HS510',
    name: 'Environmental Studies',
    fontBody: "'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    fontHeading: "'Caveat', 'Patrick Hand', 'KaTeX_Math', 'KaTeX_Main', 'KaTeX_AMS', 'JetBrains Mono', sans-serif",
    inkBlue: '#14532d',
    inkDark: '#064e3b',
    inkAccent: '#15803d'
  }
};

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

async function buildHandwrittenNotebook(browser, subId, unitNum) {
  const cfg = SUBJECT_CONFIGS[subId];
  if (!cfg) throw new Error(`Unknown subject ID: ${subId}`);

  const isPyq = (unitNum === 'pyq' || unitNum === 'pyq-answers');
  const htmlRelPath = isPyq
    ? `notes/${subId}/pyq/pyq-answers.html`
    : `notes/${subId}/unit${unitNum}/unit-${unitNum}-notes.html`;
  const htmlFullPath = path.join(REPO_ROOT, htmlRelPath);
  if (!fs.existsSync(htmlFullPath)) {
    console.warn(`File not found: ${htmlFullPath}, skipping.`);
    return null;
  }

  // Published output directory (PDF and preview image only, no published HTML)
  const outDir = isPyq
    ? path.join(REPO_ROOT, `notes/${subId}/pyq/handwritten`)
    : path.join(REPO_ROOT, `notes/${subId}/unit${unitNum}/handwritten`);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  // Intermediate build directory (git-ignored)
  const buildDir = path.join(REPO_ROOT, 'build/handwritten');
  if (!fs.existsSync(buildDir)) fs.mkdirSync(buildDir, { recursive: true });

  const pdfName = isPyq
    ? `${subId}-pyq-handwritten.pdf`
    : `${subId}-unit${unitNum}-handwritten.pdf`;
  const pdfPath = path.join(outDir, pdfName);
  const previewPath = isPyq
    ? path.join(outDir, `${subId}-pyq-preview.webp`)
    : path.join(outDir, `${subId}-unit${unitNum}-preview.webp`);
  const stagingHtmlPath = path.join(buildDir, `${subId}-${unitNum}-staging.html`);
  const finalHtmlPath = path.join(buildDir, `${subId}-${unitNum}.html`);
  const tocJsonPath = path.join(buildDir, `${subId}-${unitNum}-toc.json`);

  console.log(`\n===============================================================`);
  console.log(`BUILDING HANDWRITTEN NOTEBOOK PDF: ${cfg.code} ${isPyq ? 'CIE-1 PYQ Bank' : 'Unit ' + unitNum}`);
  console.log(`Source: ${htmlRelPath}`);
  console.log(`Output PDF: ${pdfPath}`);
  console.log(`===============================================================`);

  const page = await browser.newPage({
    viewport: { width: 1200, height: 1600 }
  });

  page.on('console', msg => {
    const text = msg.text();
    if (!text.includes('favicon') && !text.includes('ERR_FILE_NOT_FOUND')) {
      console.log('BROWSER LOG:', text);
    }
  });
  page.on('pageerror', err => console.log('BROWSER ERROR:', err.message));

  // Load the raw source page in browser so we can extract its rendered DOM structure cleanly
  const fileUrl = 'file:///' + htmlFullPath.replace(/\\/g, '/');
  await page.goto(fileUrl, { waitUntil: 'load' });

  // Extract structured content from source page
  const pageData = await page.evaluate(() => {
    const headlineEl = document.querySelector('.notes-headline') || document.querySelector('h1');
    const subheadlineEl = document.querySelector('.notes-subheadline') || document.querySelector('.hero-desc');
    const syllabusTopicsEl = document.querySelector('.syllabus-topics') || document.querySelector('.syllabus-card p');
    const syllabusCardEl = document.querySelector('.syllabus-card');
    const headerMetaEl = document.querySelector('.header-mono-label') || document.querySelector('.reading-meta-bar');

    const headline = headlineEl ? headlineEl.textContent.trim() : 'Unit Notes';
    const subheadline = subheadlineEl ? subheadlineEl.textContent.trim() : '';
    const syllabusText = syllabusTopicsEl ? syllabusTopicsEl.textContent.trim() : (syllabusCardEl ? syllabusCardEl.textContent.trim() : '');
    const headerMeta = headerMetaEl ? headerMetaEl.textContent.trim() : '';

    // Extract all content sections inside main
    const sectionEls = Array.from(document.querySelectorAll('main > section'));
    const sections = sectionEls.map(sec => {
      const secId = sec.id || '';
      const h2 = sec.querySelector('h2');
      let title = h2 ? h2.textContent.trim() : (secId || 'Section');
      title = title.replace(/\$\s*\\epsilon\s*\$/g, 'ϵ').replace(/\\epsilon/g, 'ϵ').replace(/\$/g, '');

      // Clone section and transform elements for notebook look
      const clone = sec.cloneNode(true);
      clone.querySelectorAll('script, style').forEach(s => s.remove());

      // Remove original h2 from clone as we render custom notebook h2
      const cloneH2 = clone.querySelector('h2');
      if (cloneH2) cloneH2.remove();

      // Transform details into open practice cards
      const detailsEls = Array.from(clone.querySelectorAll('details'));
      detailsEls.forEach(det => {
        const summary = det.querySelector('summary');
        const qText = summary ? summary.innerHTML : 'Practice Problem';
        if (summary) summary.remove();
        const aHtml = det.innerHTML;

        const card = document.createElement('div');
        card.className = 'practice-card';
        card.innerHTML = `
          <div class="card-content-inner">
            <div class="practice-header">Practice Problem:</div>
            <div style="margin-bottom: 4px;">${qText}</div>
            <div class="practice-ans-box">
              <span class="ans-badge">Solution:</span>
              <div>${aHtml}</div>
            </div>
          </div>
        `;
        det.replaceWith(card);
      });

      // Transform interactive cards/sections into clean handwritten reference note
      const interCards = Array.from(clone.querySelectorAll('.interactive-card, .interactive-section'));
      interCards.forEach(ic => {
        const titleEl = ic.querySelector('h3, h4, .interactive-title');
        const toolTitle = titleEl ? titleEl.innerText.trim() : 'Interactive Explorer Studio';
        const note = document.createElement('div');
        note.className = 'interactive-note';
        note.innerHTML = `
          <span><strong>[Interactive Visualizer Online]:</strong> ${toolTitle}. Explore the step-by-step visualizer on the live course notes page.</span>
        `;
        ic.replaceWith(note);
      });

      // Pre-sanitize and mark diagrams/SVGs as atomic, isolating diagram text
      const diagWrappers = Array.from(clone.querySelectorAll('.diagram-wrapper, .diagram-card, .diagram-container, figure'));
      diagWrappers.forEach(dw => {
        dw.setAttribute('data-atomic', 'true');
        dw.querySelectorAll('svg text').forEach(t => {
          let text = t.textContent;
          text = text.replace(/\$H_0\$/g, 'H0')
                     .replace(/\$H_1\$/g, 'H1')
                     .replace(/\$O\(n\)\$/g, 'O(n)')
                     .replace(/\$O\(n\^3\)\$/g, 'O(n^3)')
                     .replace(/\$q_0\$/g, 'q0')
                     .replace(/\$q_1\$/g, 'q1')
                     .replace(/\$q_2\$/g, 'q2')
                     .replace(/\$q_k\$/g, 'qk')
                     .replace(/\$r\$/g, 'r')
                     .replace(/\$\\theta\$/g, 'θ')
                     .replace(/\$\\epsilon\$/g, 'ϵ')
                     .replace(/\$/g, '')
                     .replace(/\u2080/g, '0')
                     .replace(/\u2081/g, '1')
                     .replace(/\u2082/g, '2')
                     .replace(/\u2083/g, '3')
                     .replace(/\u2084/g, '4')
                     .replace(/\u2085/g, '5')
                     .replace(/\u2086/g, '6')
                     .replace(/\u2087/g, '7')
                     .replace(/\u1d40/g, 'T')
                     .replace(/\u1d62/g, 'i')
                     .replace(/\u2c7c/g, 'j')
                     .replace(/\u2096/g, 'k')
                     .replace(/\u2071/g, 'i')
                     .replace(/\u2092/g, '0')
                     .replace(/\u1d34/g, 'H')
                     .replace(/\u1d30/g, 'A');
          t.textContent = text;
        });
      });

      // Transform callouts to authentic hand-card
      const calloutEls = Array.from(clone.querySelectorAll('[class*="callout"]'));
      calloutEls.forEach(c => {
        let type = 'def';
        let badge = 'Definition';
        const cls = c.className;
        if (cls.includes('formula')) { type = 'formula'; badge = 'Key Formula'; }
        else if (cls.includes('example')) { type = 'example'; badge = 'Worked Example'; }
        else if (cls.includes('tip')) { type = 'tip'; badge = 'Exam Tip'; }
        else if (cls.includes('warning') || cls.includes('mistake')) { type = 'warning'; badge = 'Common Mistake'; }
        else if (cls.includes('recall')) { type = 'recall'; badge = 'Quick Recall'; }
        else if (cls.includes('note')) { type = 'example'; badge = 'Note'; }

        const existingLabel = c.querySelector('.callout-label, .callout-tag');
        if (existingLabel) {
          const raw = existingLabel.innerText.trim().replace(/[∇★✦❖■▲▼⚡💻📝📌🎯💡⚠✓✗✕]/gu, '').trim();
          if (raw) badge = raw;
          existingLabel.remove();
        }

        const innerContent = c.innerHTML;
        c.className = `hand-card card-${type}`;
        c.innerHTML = `
          <div class="card-content-inner">
            <div class="hand-label label-${type}">${badge}:</div>
            ${innerContent}
          </div>
        `;
      });

      // Clean section badges
      clone.querySelectorAll('.section-badge').forEach(b => {
        b.textContent = b.textContent.replace(/[∇★✦❖■▲▼⚡💻📝📌🎯💡⚠✓✗✕]/gu, '').trim();
      });

      // Style tables
      const tables = Array.from(clone.querySelectorAll('table'));
      tables.forEach(t => {
        t.classList.add('hand-table');
        const wrap = t.closest('.table-wrap');
        if (wrap) wrap.classList.add('hand-table-wrap');
      });

      // Style code blocks
      const pres = Array.from(clone.querySelectorAll('pre'));
      pres.forEach(p => {
        p.classList.add('hand-code-box');
      });

      const sanitizedHtml = clone.innerHTML
        .replace(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g, ' ')
        .replace(/\u2588/g, '')
        .replace(/\u1d40/g, '<sup>T</sup>')
        .replace(/\u1d62/g, '<sub>i</sub>')
        .replace(/\u2c7c/g, '<sub>j</sub>')
        .replace(/\u2096/g, '<sub>k</sub>')
        .replace(/\u2071/g, '<sup>i</sup>')
        .replace(/\u2092/g, '<sub>o</sub>')
        .replace(/\u1d34/g, '<sup>H</sup>')
        .replace(/\u1d30/g, '<sup>A</sup>')
        .replace(/\u2080/g, '<sub>0</sub>')
        .replace(/\u2081/g, '<sub>1</sub>')
        .replace(/\u2082/g, '<sub>2</sub>')
        .replace(/\u2083/g, '<sub>3</sub>')
        .replace(/\u2084/g, '<sub>4</sub>')
        .replace(/\u2085/g, '<sub>5</sub>')
        .replace(/\u2086/g, '<sub>6</sub>')
        .replace(/\u2087/g, '<sub>7</sub>')
        .replace(/\u2088/g, '<sub>8</sub>')
        .replace(/\u2089/g, '<sub>9</sub>')
        .replace(/\u2207/g, 'del')
        .replace(/\u2500/g, '-')
        .replace(/\u2502/g, '|')
        .replace(/\u251c/g, '|')
        .replace(/\u2514/g, '`')
        .replace(/\u250c/g, '+')
        .replace(/\u2510/g, '+')
        .replace(/\u2524/g, '|')
        .replace(/\u252c/g, '+')
        .replace(/\u2534/g, '+')
        .replace(/\u253c/g, '+')
        .replace(/[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}]/gu, '');

      return {
        id: secId,
        title: title,
        html: sanitizedHtml
      };
    });

    return {
      headline,
      subheadline,
      syllabusText: syllabusText.replace(/[\x00-\x08\x0b\x0c\x0e-\x1f]/g, ' '),
      headerMeta,
      sections
    };
  });

  // Asset URLs relative to buildDir
  const fontsCssPath = path.relative(buildDir, path.join(REPO_ROOT, 'fonts/fonts.css')).replace(/\\/g, '/');
  const katexCssPath = path.relative(buildDir, path.join(REPO_ROOT, 'assets/katex/katex.min.css')).replace(/\\/g, '/');
  const katexJsPath = path.relative(buildDir, path.join(REPO_ROOT, 'assets/katex/katex.min.js')).replace(/\\/g, '/');
  const katexAutoPath = path.relative(buildDir, path.join(REPO_ROOT, 'assets/katex/contrib/auto-render.min.js')).replace(/\\/g, '/');
  const handCssPath = path.relative(buildDir, path.join(REPO_ROOT, 'css/handwritten.css')).replace(/\\/g, '/');
  const roughJsPath = path.relative(buildDir, path.join(REPO_ROOT, 'js/rough.js')).replace(/\\/g, '/');

  // Build the staging HTML shell
  const stagingHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${escapeHtml(cfg.code)} ${isPyq ? 'CIE-1 PYQ Bank' : 'Unit ' + unitNum} - Handwritten Notes</title>
  <link rel="stylesheet" href="${fontsCssPath}">
  <link rel="stylesheet" href="${katexCssPath}">
  <link rel="stylesheet" href="${handCssPath}">
  <style>
    :root {
      --font-body: ${cfg.fontBody};
      --font-heading: ${cfg.fontHeading};
      --ink-blue: ${cfg.inkBlue};
      --ink-dark: ${cfg.inkDark};
    }
    #staging-container {
      position: absolute;
      left: -9999px;
      top: 0;
      width: calc(210mm - 28mm - 14mm);
      opacity: 0;
      pointer-events: none;
    }
  </style>
  <script src="${katexJsPath}"></script>
  <script src="${katexAutoPath}"></script>
  <script src="${roughJsPath}"></script>
</head>
<body>
  <div id="staging-container">
    ${pageData.sections.map((sec, idx) => `
      <div class="staging-section" data-sec-id="${escapeHtml(sec.id)}" data-sec-title="${escapeHtml(sec.title)}" data-sec-index="${idx}">
        <h2 id="${escapeHtml(sec.id)}">${escapeHtml(sec.title)}</h2>
        <div class="staging-body">
          ${sec.html}
        </div>
      </div>
    `).join('\n')}
  </div>
  <div id="notebook-container"></div>
</body>
</html>`;

  fs.writeFileSync(stagingHtmlPath, stagingHtml, 'utf8');

  // Load staging page in Chrome
  const stagingFileUrl = 'file:///' + stagingHtmlPath.replace(/\\/g, '/');
  await page.goto(stagingFileUrl, { waitUntil: 'load' });

  const paginationResult = await page.evaluate(async ({ pageData, cfg, unitNum, isPyq }) => {
    function escapeHtml(str) {
      if (!str) return '';
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // 1. Font Validation Gate: Ensure handwriting fonts are fully loaded
    await document.fonts.ready;
    const requiredFonts = [
      '400 18px "Patrick Hand"',
      '700 24px "Caveat"',
      '400 24px "Caveat"',
      '400 18px "Kalam"',
      '700 18px "Kalam"',
      '400 14px "JetBrains Mono"',
      '700 14px "JetBrains Mono"'
    ];
    for (const f of requiredFonts) {
      await document.fonts.load(f);
      if (!document.fonts.check(f)) {
        throw new Error(`CRITICAL: Font check failed for "${f}". Embedding aborted.`);
      }
    }

    // 2. KaTeX Render: strictly IGNORE svg and diagrams so formulas never leak into diagrams
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('staging-container'), {
        output: 'html',
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'annotation', 'annotation-xml', 'svg', 'figure'],
        ignoredClasses: ['diagram-wrapper', 'diagram-card', 'diagram-container', 'svg-diagram'],
        throwOnError: false
      });
      // Remove hidden MathML nodes so system math fonts (Cambria, Times) are never invoked
      document.querySelectorAll('.katex-mathml').forEach(el => el.remove());
    }

    const container = document.getElementById('notebook-container');
    const staging = document.getElementById('staging-container');

    const MAX_PAGE_HEIGHT_PX = 952; // Exact 34 lines @ 28px
    let pageNum = 1;
    let pages = [];
    let tocEntries = [];

    // Create Page 1: Cover Page
    const coverPage = document.createElement('div');
    coverPage.className = 'notebook-page';
    coverPage.id = 'page-1';

    const cleanTitle = pageData.headline.replace(/^Unit\s*\d+:\s*/i, '');
    const syllabusShort = pageData.syllabusText.length > 320
      ? pageData.syllabusText.slice(0, 320) + '...'
      : pageData.syllabusText;

    coverPage.innerHTML = `
      <div class="punch-hole punch-top"></div>
      <div class="punch-hole punch-mid"></div>
      <div class="punch-hole punch-bot"></div>
      <div class="cover-page">
        <div class="cover-header">
          <div class="cover-badge">${escapeHtml(cfg.code)} · ${escapeHtml(cfg.name)}</div>
          <h1 class="cover-title">${isPyq ? 'CIE-1 PYQ Bank: Model Answers' : `Unit ${unitNum}: ${escapeHtml(cleanTitle)}`}</h1>
          <div class="cover-subtitle">${isPyq ? 'Handwritten Question Bank & Solutions' : 'Handwritten Student Notebook'}</div>
        </div>

        <div class="cover-syllabus-card">
          <strong style="color: #0f172a; font-family: var(--font-heading); font-size: 18px;">Syllabus Topics Covered:</strong>
          <p style="margin: 4px 0 0 0; color: #334155; line-height: 24px;">${escapeHtml(syllabusShort)}</p>
        </div>

        <div class="cover-toc-card">
          <div class="cover-toc-title">Table of Contents</div>
          <ul class="toc-list" id="cover-toc-list"></ul>
        </div>

        <div class="cover-footer">
          <div>Department of Information Science & Engineering · Semester V</div>
          <div style="margin-top: 2px;">Handwritten-style notes (generated from unit notes) - verify with your textbook and faculty notes.</div>
        </div>
      </div>
    `;
    container.appendChild(coverPage);
    pages.push({ el: coverPage, topic: 'Cover' });

    function createRuledPage(topic) {
      pageNum++;
      const p = document.createElement('div');
      p.className = 'notebook-page page-ruled';
      p.id = 'page-' + pageNum;
      p.innerHTML = `
        <div class="punch-hole punch-top"></div>
        <div class="punch-hole punch-mid"></div>
        <div class="punch-hole punch-bot"></div>
        <div class="page-header">
          <span class="header-left">${escapeHtml(cfg.code)} · ${isPyq ? 'CIE-1 PYQ Bank' : 'Unit ' + unitNum}</span>
          <span class="header-right">${escapeHtml(topic || '')}</span>
        </div>
        <div class="page-content"></div>
        <div class="page-footer">
          <span>AI-assisted study notes - verify with your textbook and faculty notes.</span>
          <span class="footer-page-num">Page ${pageNum}</span>
        </div>
      `;
      container.appendChild(p);
      const contentEl = p.querySelector('.page-content');
      pages.push({ el: p, contentEl, topic });
      return { pageEl: p, contentEl, topic };
    }

    let currentRuled = createRuledPage('Overview');
    let currentHeight = 0;

    const stagingSections = Array.from(staging.querySelectorAll('.staging-section'));

    for (const sec of stagingSections) {
      const secTitle = sec.getAttribute('data-sec-title') || 'Section';
      const secId = sec.getAttribute('data-sec-id') || '';

      tocEntries.push({
        id: secId,
        title: secTitle,
        page: pageNum
      });

      // Update header topic only if starting a fresh page
      if (currentHeight === 0) {
        const headerRight = currentRuled.pageEl.querySelector('.header-right');
        if (headerRight) headerRight.textContent = secTitle;
        currentRuled.topic = secTitle;
      }

      const h2El = sec.querySelector('h2');
      const bodyEl = sec.querySelector('.staging-body');
      const items = [h2El, ...Array.from(bodyEl.children)].filter(Boolean);

      for (let i = 0; i < items.length; i++) {
        const item = items[i];
        const isHeading = ['H1', 'H2', 'H3', 'H4'].includes(item.tagName) || item.classList.contains('subsection-title');

        // Heading orphan prevention:
        // A heading must never be placed alone at the bottom without its subsequent content
        if (isHeading) {
          const nextItem = (i + 1 < items.length) ? items[i + 1] : null;
          const nextH = nextItem ? (nextItem.offsetHeight || 60) : 60;
          const headingH = item.offsetHeight || 36;
          if (currentHeight + headingH + Math.min(nextH, 140) > MAX_PAGE_HEIGHT_PX && currentHeight > 60) {
            currentRuled = createRuledPage(secTitle);
            currentHeight = 0;
          }
        }

        const itemH = item.offsetHeight || 28;

        // If item fits completely on current page
        if (currentHeight + itemH <= MAX_PAGE_HEIGHT_PX) {
          currentRuled.contentEl.appendChild(item.cloneNode(true));
          currentHeight += itemH;
          continue;
        }

        // Item does NOT fit completely. Can it be split?
        // 1. Lists (ul, ol) with multiple li items
        if ((item.tagName === 'UL' || item.tagName === 'OL') && item.children.length > 2) {
          const lis = Array.from(item.children);
          let listClone = document.createElement(item.tagName);
          if (item.getAttribute('start')) listClone.setAttribute('start', item.getAttribute('start'));
          listClone.className = item.className;

          let liIndex = 0;
          let addedToCurrent = false;

          while (liIndex < lis.length) {
            const li = lis[liIndex];
            const liH = li.offsetHeight || 28;
            if (currentHeight + liH <= MAX_PAGE_HEIGHT_PX) {
              listClone.appendChild(li.cloneNode(true));
              currentHeight += liH;
              addedToCurrent = true;
              liIndex++;
            } else {
              break;
            }
          }

          if (addedToCurrent) {
            currentRuled.contentEl.appendChild(listClone);
          }

          // Remaining items go to next page
          if (liIndex < lis.length) {
            currentRuled = createRuledPage(secTitle);
            currentHeight = 0;
            let nextList = document.createElement(item.tagName);
            if (item.tagName === 'OL') nextList.setAttribute('start', String(liIndex + 1));
            nextList.className = item.className;
            while (liIndex < lis.length) {
              const li = lis[liIndex];
              const liH = li.offsetHeight || 28;
              if (currentHeight + liH > MAX_PAGE_HEIGHT_PX && currentHeight > 80) {
                currentRuled.contentEl.appendChild(nextList);
                currentRuled = createRuledPage(secTitle);
                currentHeight = 0;
                nextList = document.createElement(item.tagName);
                if (item.tagName === 'OL') nextList.setAttribute('start', String(liIndex + 1));
                nextList.className = item.className;
              }
              nextList.appendChild(li.cloneNode(true));
              currentHeight += liH;
              liIndex++;
            }
            currentRuled.contentEl.appendChild(nextList);
          }
          continue;
        }

        // 2. Tables with multiple rows: repeat thead
        const table = item.tagName === 'TABLE' ? item : item.querySelector('table');
        if (table && table.rows.length > 3 && !item.hasAttribute('data-atomic')) {
          const rows = Array.from(table.rows);
          const theadRow = rows[0];
          const theadH = theadRow.offsetHeight || 32;

          let tableClone = document.createElement('table');
          tableClone.className = table.className;
          tableClone.appendChild(theadRow.cloneNode(true));
          let currentTableH = theadH;

          let rIdx = 1;
          let addedRows = 0;
          while (rIdx < rows.length) {
            const r = rows[rIdx];
            const rH = r.offsetHeight || 28;
            if (currentHeight + currentTableH + rH <= MAX_PAGE_HEIGHT_PX) {
              tableClone.appendChild(r.cloneNode(true));
              currentTableH += rH;
              addedRows++;
              rIdx++;
            } else {
              break;
            }
          }

          if (addedRows >= 2) {
            currentRuled.contentEl.appendChild(tableClone);
            currentHeight += currentTableH;
          } else {
            rIdx = 1; // Move full table to next page
          }

          if (rIdx < rows.length) {
            currentRuled = createRuledPage(secTitle);
            currentHeight = 0;
            let nextTable = document.createElement('table');
            nextTable.className = table.className;
            nextTable.appendChild(theadRow.cloneNode(true));
            currentHeight += theadH;
            while (rIdx < rows.length) {
              const r = rows[rIdx];
              const rH = r.offsetHeight || 28;
              if (currentHeight + rH > MAX_PAGE_HEIGHT_PX && currentHeight > 80) {
                currentRuled.contentEl.appendChild(nextTable);
                currentRuled = createRuledPage(secTitle);
                currentHeight = 0;
                nextTable = document.createElement('table');
                nextTable.className = table.className;
                nextTable.appendChild(theadRow.cloneNode(true));
                currentHeight += theadH;
              }
              nextTable.appendChild(r.cloneNode(true));
              currentHeight += rH;
              rIdx++;
            }
            currentRuled.contentEl.appendChild(nextTable);
          }
          continue;
        }

        // 3. For any other item that doesn't fit (including callouts & figures), break page
        if (currentHeight > 60) {
          currentRuled = createRuledPage(secTitle);
          currentHeight = 0;
        }
        currentRuled.contentEl.appendChild(item.cloneNode(true));
        currentHeight += itemH;
      }
    }

    // 3. Vector Rough.js hand-drawn styling pass
    if (window.rough) {
      document.querySelectorAll('.hand-card, .practice-card').forEach((card, idx) => {
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('class', 'card-rough-svg');
        svg.style.position = 'absolute';
        svg.style.top = '0';
        svg.style.left = '0';
        svg.style.width = '100%';
        svg.style.height = '100%';
        svg.style.pointerEvents = 'none';
        svg.style.zIndex = '0';
        card.style.position = 'relative';
        card.style.borderLeft = 'none';
        card.insertBefore(svg, card.firstChild);

        const w = card.offsetWidth || 500;
        const h = card.offsetHeight || 60;
        svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
        const rc = rough.svg(svg, { options: { seed: 1000 + idx } });

        let strokeColor = '#163660';
        let fillColor = 'rgba(240, 249, 255, 0.4)';
        if (card.classList.contains('card-def')) {
          strokeColor = '#15803d';
          fillColor = 'rgba(240, 253, 244, 0.45)';
        } else if (card.classList.contains('card-tip')) {
          strokeColor = '#b91c1c';
          fillColor = 'rgba(254, 242, 242, 0.45)';
        } else if (card.classList.contains('card-formula')) {
          strokeColor = '#6b21a8';
          fillColor = 'rgba(250, 245, 255, 0.45)';
        } else if (card.classList.contains('card-example')) {
          strokeColor = '#b45309';
          fillColor = 'rgba(254, 243, 199, 0.45)';
        } else if (card.classList.contains('card-warning')) {
          strokeColor = '#c2410c';
          fillColor = 'rgba(255, 247, 237, 0.45)';
        } else if (card.classList.contains('practice-card')) {
          strokeColor = '#1d4ed8';
          fillColor = 'rgba(239, 246, 255, 0.45)';
        }

        const rectNode = rc.rectangle(2, 2, w - 4, h - 4, {
          stroke: strokeColor,
          strokeWidth: 1.5,
          roughness: 1.1,
          fill: fillColor,
          fillStyle: 'solid'
        });
        svg.appendChild(rectNode);
      });

      document.querySelectorAll('.page-ruled h2').forEach((h2, idx) => {
        h2.style.borderBottom = 'none';
        const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('class', 'h2-rough-line');
        svg.style.display = 'block';
        svg.style.width = '100%';
        svg.style.height = '6px';
        svg.style.marginTop = '1px';
        h2.parentNode.insertBefore(svg, h2.nextSibling);

        const w = Math.min(Math.max(h2.offsetWidth || 300, 200), 650);
        svg.setAttribute('viewBox', `0 0 ${w} 6`);
        const rc = rough.svg(svg, { options: { seed: 2000 + idx } });
        const lineNode = rc.line(0, 3, w, 3, {
          stroke: '#0f172a',
          strokeWidth: 1.8,
          roughness: 1.3
        });
        svg.appendChild(lineNode);
      });
    }

    // Populate Cover Table of Contents
    const tocListEl = document.getElementById('cover-toc-list');
    if (tocListEl) {
      tocListEl.innerHTML = tocEntries.map(e => `
        <li class="toc-item">
          <span>${e.title}</span>
          <span style="font-weight: 700; color: #1e3a8a;">p. ${e.page}</span>
        </li>
      `).join('');
    }

    // Footers
    const totalPages = pageNum;
    document.querySelectorAll('.footer-page-num').forEach((fn, idx) => {
      fn.textContent = `Page ${idx + 2} of ${totalPages}`;
    });

    // Remove staging container to keep final DOM clean
    staging.remove();

    return {
      totalPages,
      tocEntries
    };
  }, { pageData, cfg, unitNum, isPyq });

  console.log(`Pagination completed! Total Pages: ${paginationResult.totalPages}`);
  console.log(`TOC Sections: ${paginationResult.tocEntries.length}`);

  // Save intermediate serialized HTML into git-ignored build directory
  const finalHtml = await page.content();
  fs.writeFileSync(finalHtmlPath, finalHtml, 'utf8');
  if (fs.existsSync(stagingHtmlPath)) fs.unlinkSync(stagingHtmlPath);
  console.log(`Saved intermediate build HTML: ${finalHtmlPath}`);

  // Write TOC json for postprocessing
  fs.writeFileSync(tocJsonPath, JSON.stringify(paginationResult.tocEntries, null, 2), 'utf8');

  // Generate vector PDF
  console.log(`Generating vector PDF: ${pdfPath}...`);
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true
  });

  // Postprocess PDF metadata & bookmarks
  const pyPost = path.join(REPO_ROOT, 'scripts/postprocess_pdf.py');
  const pdfTitle = `${cfg.code} Unit ${unitNum} - Handwritten Notes`;
  execFileSync('python', [pyPost, pdfPath, pdfTitle, cfg.name, tocJsonPath]);

  const pdfStats = fs.statSync(pdfPath);
  const pdfSizeMB = (pdfStats.size / (1024 * 1024)).toFixed(2);
  console.log(`PDF Generated & Postprocessed! Size: ${pdfSizeMB} MB`);

  // Generate WebP Preview of Page 1 (Cover)
  console.log(`Generating Page 1 WebP preview: ${previewPath}...`);
  const page1El = await page.$('#page-1');
  if (page1El) {
    await page1El.screenshot({
      path: previewPath,
      type: 'webp',
      quality: 90
    });
    console.log(`Preview generated at ${previewPath}`);
  }

  await page.close();
  return {
    subId,
    unitNum,
    pages: paginationResult.totalPages,
    sizeMB: pdfSizeMB,
    sizeBytes: pdfStats.size
  };
}

async function main() {
  const args = process.argv.slice(2);
  let targetSub = null;
  let targetUnit = null;
  let doAll = false;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--subject') targetSub = args[++i];
    else if (args[i] === '--unit') {
      const uVal = args[++i];
      targetUnit = (uVal === 'pyq' || uVal === 'pyq-answers') ? 'pyq' : parseInt(uVal, 10);
    }
    else if (args[i] === '--pyq') targetUnit = 'pyq';
    else if (args[i] === '--all') doAll = true;
  }

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--allow-file-access-from-files']
  });

  try {
    if (targetSub && targetUnit) {
      await buildHandwrittenNotebook(browser, targetSub, targetUnit);
    } else if (targetSub) {
      for (const u of [1, 2, 3]) {
        await buildHandwrittenNotebook(browser, targetSub, u);
      }
      await buildHandwrittenNotebook(browser, targetSub, 'pyq');
    } else if (doAll) {
      for (const s of Object.keys(SUBJECT_CONFIGS)) {
        for (const u of [1, 2, 3]) {
          await buildHandwrittenNotebook(browser, s, u);
        }
        await buildHandwrittenNotebook(browser, s, 'pyq');
      }
    } else {
      console.log('Usage: node scripts/build_handwritten.js [--subject <id> --unit <N|pyq>] [--all]');
    }
  } finally {
    await browser.close();
  }
}

if (require.main === module) {
  main().catch(err => {
    console.error('Build failed:', err);
    process.exit(1);
  });
}

module.exports = { buildHandwrittenNotebook };
