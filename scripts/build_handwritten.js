/**
 * SEM 5 · ISE Notes - Handwritten-Style Notebook Generator
 * Converts complete HTML unit notes page into an authentic handwritten notebook PDF.
 * Uses Playwright, KaTeX, Rough.js, local Google Fonts, and exact A4 pagination.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const REPO_ROOT = path.resolve(__dirname, '..');

// Subject Configurations & Pen Personalities
const SUBJECT_CONFIGS = {
  toc: {
    code: 'IS54',
    name: 'Theory of Computation',
    fontBody: "'Caveat', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#163660',
    inkDark: '#0f172a',
    inkAccent: '#6b21a8'
  },
  cn: {
    code: 'IS53',
    name: 'Computer Networks',
    fontBody: "'Kalam', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#1b3252',
    inkDark: '#0a0f1d',
    inkAccent: '#1d4ed8'
  },
  ai: {
    code: 'ISE552',
    name: 'Artificial Intelligence',
    fontBody: "'Caveat', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#1e3a8a',
    inkDark: '#111827',
    inkAccent: '#7c3aed'
  },
  ml: {
    code: 'IS51',
    name: 'Machine Learning',
    fontBody: "'Gaegu', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#163e54',
    inkDark: '#0f172a',
    inkAccent: '#0369a1'
  },
  reactjs: {
    code: 'ISAEC594',
    name: 'ReactJS',
    fontBody: "'Architects Daughter', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#1e293b',
    inkDark: '#0284c7',
    inkAccent: '#0284c7'
  },
  rmipr: {
    code: 'AL58',
    name: 'Research Methodology & IPR',
    fontBody: "'Indie Flower', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#1e3a5f',
    inkDark: '#111827',
    inkAccent: '#b45309'
  },
  se: {
    code: 'IS52',
    name: 'Software Engineering',
    fontBody: "'Kalam', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
    inkBlue: '#172554',
    inkDark: '#0f172a',
    inkAccent: '#2563eb'
  },
  evs: {
    code: 'HS510',
    name: 'Environmental Studies',
    fontBody: "'Patrick Hand', cursive, sans-serif",
    fontHeading: "'Patrick Hand', cursive, sans-serif",
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

  const htmlRelPath = `notes/${subId}/unit${unitNum}/unit-${unitNum}-notes.html`;
  const htmlFullPath = path.join(REPO_ROOT, htmlRelPath);
  if (!fs.existsSync(htmlFullPath)) {
    console.warn(`File not found: ${htmlFullPath}, skipping.`);
    return null;
  }

  const outDir = path.join(REPO_ROOT, `notes/${subId}/unit${unitNum}/handwritten`);
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const pdfName = `${subId}-unit${unitNum}-handwritten.pdf`;
  const pdfPath = path.join(outDir, pdfName);
  const previewPath = path.join(outDir, `${subId}-unit${unitNum}-preview.webp`);
  const debugHtmlPath = path.join(outDir, `${subId}-unit${unitNum}-handwritten.html`);

  console.log(`\n===============================================================`);
  console.log(`BUILDING HANDWRITTEN NOTEBOOK: ${cfg.code} Unit ${unitNum}`);
  console.log(`Source: ${htmlRelPath}`);
  console.log(`Output: ${pdfPath}`);
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
    // 1. Hero details
    const headlineEl = document.querySelector('.notes-headline') || document.querySelector('h1');
    const subheadlineEl = document.querySelector('.notes-subheadline') || document.querySelector('.hero-desc');
    const syllabusTopicsEl = document.querySelector('.syllabus-topics') || document.querySelector('.syllabus-card p');
    const syllabusCardEl = document.querySelector('.syllabus-card');
    const headerMetaEl = document.querySelector('.header-mono-label') || document.querySelector('.reading-meta-bar');

    const headline = headlineEl ? headlineEl.textContent.trim() : 'Unit Notes';
    const subheadline = subheadlineEl ? subheadlineEl.textContent.trim() : '';
    const syllabusText = syllabusTopicsEl ? syllabusTopicsEl.textContent.trim() : (syllabusCardEl ? syllabusCardEl.textContent.trim() : '');
    const headerMeta = headerMetaEl ? headerMetaEl.textContent.trim() : '';

    // 2. Sections: Extract all content sections inside main
    const sectionEls = Array.from(document.querySelectorAll('main > section'));
    const sections = sectionEls.map(sec => {
      const secId = sec.id || '';
      const h2 = sec.querySelector('h2');
      let title = h2 ? h2.textContent.trim() : (secId || 'Section');
      title = title.replace(/\$\s*\\epsilon\s*\$/g, 'ϵ').replace(/\\epsilon/g, 'ϵ').replace(/\$/g, '');

      // Clone section and transform elements for notebook look
      const clone = sec.cloneNode(true);
      // Remove any scripts and styles embedded in the section
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
          <div style="font-family: var(--font-heading); font-weight: bold; margin-bottom: 4px; color: #1e3a8a;">
            📝 Practice Problem:
          </div>
          <div style="margin-bottom: 6px;">${qText}</div>
          <div class="practice-ans-box">
            <span class="ans-badge">Ans</span>
            <div>${aHtml}</div>
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
          <span>💻 <strong>Interactive Tool Available Online:</strong> ${toolTitle}. Try the interactive step-by-step calculator and visualizer on the live site notes page.</span>
        `;
        ic.replaceWith(note);
      });

      // Transform callouts to hand-card
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
          badge = existingLabel.innerText.trim();
          existingLabel.remove();
        }

        c.classList.add('hand-card', `card-${type}`);
        const badgeEl = document.createElement('div');
        badgeEl.className = 'hand-badge';
        badgeEl.textContent = badge;
        c.insertBefore(badgeEl, c.firstChild);
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

      return {
        id: secId,
        title: title,
        html: clone.innerHTML
      };
    });

    return {
      headline,
      subheadline,
      syllabusText,
      headerMeta,
      sections
    };
  });

  // Relative URLs from output dir to root assets
  const fontsCssPath = path.relative(outDir, path.join(REPO_ROOT, 'fonts/fonts.css')).replace(/\\/g, '/');
  const katexCssPath = path.relative(outDir, path.join(REPO_ROOT, 'assets/katex/katex.min.css')).replace(/\\/g, '/');
  const katexJsPath = path.relative(outDir, path.join(REPO_ROOT, 'assets/katex/katex.min.js')).replace(/\\/g, '/');
  const katexAutoPath = path.relative(outDir, path.join(REPO_ROOT, 'assets/katex/contrib/auto-render.min.js')).replace(/\\/g, '/');
  const handCssPath = path.relative(outDir, path.join(REPO_ROOT, 'css/handwritten.css')).replace(/\\/g, '/');
  const roughJsPath = path.relative(outDir, path.join(REPO_ROOT, 'js/rough.js')).replace(/\\/g, '/');

  // Build the staging HTML shell
  const stagingHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>${escapeHtml(cfg.code)} Unit ${unitNum} - Handwritten Notes</title>
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

  fs.writeFileSync(debugHtmlPath, stagingHtml, 'utf8');

  // Load staging page
  const debugFileUrl = 'file:///' + debugHtmlPath.replace(/\\/g, '/');
  await page.goto(debugFileUrl, { waitUntil: 'load' });

  // Execute in-page pagination directly via evaluate with clean parameters
  const paginationResult = await page.evaluate(async ({ pageData, cfg, unitNum }) => {
    // 1. KaTeX render
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('staging-container'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
      });
    }

    await document.fonts.ready;

    const container = document.getElementById('notebook-container');
    const staging = document.getElementById('staging-container');

    let seed = 123456789;
    function seededRandom() {
      seed = (seed * 9301 + 49297) % 233280;
      return seed / 233280;
    }

    const MAX_PAGE_HEIGHT_PX = 940;
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
          <div class="cover-badge">${cfg.code} · ${cfg.name}</div>
          <h1 class="cover-title">Unit ${unitNum}: ${cleanTitle}</h1>
          <div class="cover-subtitle">Handwritten Student Notebook</div>
        </div>

        <div class="cover-syllabus-card">
          <strong style="color: #0f172a; font-family: var(--font-heading);">Syllabus Topics Covered:</strong>
          <p style="margin: 4px 0 0 0; color: #334155;">${syllabusShort}</p>
        </div>

        <div class="cover-toc-card">
          <div class="cover-toc-title">Table of Contents</div>
          <ul class="toc-list" id="cover-toc-list"></ul>
        </div>

        <div class="cover-footer">
          <div>Department of Information Science & Engineering · Semester V</div>
          <div style="margin-top: 2px;">Generated handwritten-style notes - verify with your textbook and faculty notes.</div>
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
          <span class="header-left">${cfg.code} · Unit ${unitNum}</span>
          <span class="header-right">${topic || ''}</span>
        </div>
        <div class="page-content"></div>
        <div class="page-footer">
          <span>Generated handwritten-style notes - verify with your textbook and faculty notes.</span>
          <span class="footer-page-num">Page ${pageNum}</span>
        </div>
      `;
      container.appendChild(p);
      const contentEl = p.querySelector('.page-content');
      pages.push({ el: p, contentEl, topic });
      return { pageEl: p, contentEl };
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

      const headerRight = currentRuled.pageEl.querySelector('.header-right');
      if (headerRight) headerRight.textContent = secTitle;

      const h2El = sec.querySelector('h2');
      const bodyEl = sec.querySelector('.staging-body');
      const items = [h2El, ...Array.from(bodyEl.children)];

      for (const item of items) {
        if (!item) continue;
        const itemHeight = item.offsetHeight || 32;

        if (currentHeight + itemHeight > MAX_PAGE_HEIGHT_PX && currentHeight > 100) {
          currentRuled = createRuledPage(secTitle);
          currentHeight = 0;
        }

        if (itemHeight > MAX_PAGE_HEIGHT_PX && item.children.length > 2 && !item.classList.contains('diagram-card') && !item.classList.contains('table-wrap') && !item.classList.contains('hand-card')) {
          const subChildren = Array.from(item.children);
          for (const sub of subChildren) {
            const subH = sub.offsetHeight || 26;
            if (currentHeight + subH > MAX_PAGE_HEIGHT_PX && currentHeight > 100) {
              currentRuled = createRuledPage(secTitle);
              currentHeight = 0;
            }
            const cloneSub = sub.cloneNode(true);
            currentRuled.contentEl.appendChild(cloneSub);
            currentHeight += subH + 6;
          }
        } else {
          const cloneItem = item.cloneNode(true);

          const r = seededRandom();
          if (cloneItem.tagName === 'P' || cloneItem.tagName === 'LI') {
            if (r < 0.25) cloneItem.classList.add('wobble-1');
            else if (r < 0.5) cloneItem.classList.add('wobble-2');
            else if (r < 0.75) cloneItem.classList.add('wobble-3');
            else cloneItem.classList.add('wobble-4');
          }

          currentRuled.contentEl.appendChild(cloneItem);
          currentHeight += itemHeight + 6;
        }
      }
    }

    // Populate TOC
    const tocListEl = document.getElementById('cover-toc-list');
    if (tocListEl) {
      tocListEl.innerHTML = tocEntries.map(e => `
        <li class="toc-item">
          <span>${e.title}</span>
          <span style="font-weight: bold; color: #1e3a8a;">p. ${e.page}</span>
        </li>
      `).join('');
    }

    // Footers
    const totalPages = pageNum;
    document.querySelectorAll('.footer-page-num').forEach((fn, idx) => {
      fn.textContent = `Page ${idx + 2} of ${totalPages}`;
    });

    // Diagram styling
    const diagramSvgs = document.querySelectorAll('.notebook-page svg');
    diagramSvgs.forEach(svg => {
      svg.style.strokeLinecap = 'round';
      svg.style.strokeLinejoin = 'round';
    });

    return {
      totalPages,
      tocEntries
    };
  }, { pageData, cfg, unitNum });

  console.log(`Pagination completed! Total Pages: ${paginationResult.totalPages}`);
  console.log(`TOC Sections: ${paginationResult.tocEntries.length}`);

  // Generate vector PDF
  console.log(`Generating vector PDF: ${pdfPath}...`);
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true
  });

  const pdfStats = fs.statSync(pdfPath);
  const pdfSizeMB = (pdfStats.size / (1024 * 1024)).toFixed(2);
  console.log(`PDF Generated successfully! Size: ${pdfSizeMB} MB`);

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

  // Generate 6 Representative Screenshots for Pilot Visual Inspection
  const screensDir = path.join(REPO_ROOT, `audit/screens/pilot_${subId}_u${unitNum}`);
  if (!fs.existsSync(screensDir)) fs.mkdirSync(screensDir, { recursive: true });

  const pageTypes = await page.evaluate(() => {
    const pages = Array.from(document.querySelectorAll('.notebook-page'));
    return pages.map((p, idx) => ({
      pageNum: idx + 1,
      hasDiagram: !!p.querySelector('svg[viewBox]'),
      hasTable: !!p.querySelector('table'),
      hasCallout: !!p.querySelector('.hand-card'),
      hasProblem: !!p.querySelector('.practice-card, .problem-card, .numerical-card'),
      textLength: p.innerText.length
    }));
  });

  const findPage = (filterFn, defaultPage) => {
    const match = pageTypes.find(filterFn);
    return match ? match.pageNum : defaultPage;
  };

  const coverP = 1;
  const textP = findPage(p => p.pageNum > 1 && !p.hasDiagram && !p.hasTable && p.textLength > 400, 2);
  const diagramP = findPage(p => p.hasDiagram && p.pageNum > 1, Math.min(3, paginationResult.totalPages));
  const tableP = findPage(p => p.hasTable && p.pageNum > 1, Math.min(4, paginationResult.totalPages));
  const calloutP = findPage(p => p.hasCallout && p.pageNum > 1, Math.min(5, paginationResult.totalPages));
  const numericalP = findPage(p => p.hasProblem && p.pageNum > 1, Math.min(6, paginationResult.totalPages));

  const reps = [
    { type: 'contents', pageNum: coverP },
    { type: 'text', pageNum: textP },
    { type: 'diagram', pageNum: diagramP },
    { type: 'table', pageNum: tableP },
    { type: 'callout', pageNum: calloutP },
    { type: 'numerical', pageNum: numericalP }
  ];

  for (const rep of reps) {
    const pageEl = await page.$(`#page-${rep.pageNum}`);
    if (pageEl) {
      const shotPath = path.join(screensDir, `${subId}_u${unitNum}_${rep.type}_p${rep.pageNum}.png`);
      await pageEl.screenshot({ path: shotPath, type: 'png' });
      rep.shotPath = shotPath;
    }
  }

  // Postprocess PDF: add bookmarks / outline and metadata using Python pypdf
  try {
    const pyScript = path.join(__dirname, 'postprocess_pdf.py');
    const tocJsonPath = path.join(outDir, 'toc.json');
    fs.writeFileSync(tocJsonPath, JSON.stringify(paginationResult.tocEntries, null, 2), 'utf8');
    const { execFileSync } = require('child_process');
    execFileSync('python', [
      pyScript,
      pdfPath,
      `${cfg.code} - Unit ${unitNum} Handwritten Notes`,
      cfg.name,
      tocJsonPath
    ], {
      cwd: REPO_ROOT
    });
    console.log(`PDF bookmarks and metadata added via pypdf.`);
  } catch (err) {
    console.warn(`Could not add pypdf bookmarks: ${err.message}`);
  }

  await page.close();

  return {
    subId,
    unitNum,
    code: cfg.code,
    name: cfg.name,
    pdfPath,
    pdfSizeMB: parseFloat(pdfSizeMB),
    totalPages: paginationResult.totalPages,
    previewPath,
    reps,
    tocEntries: paginationResult.tocEntries
  };
}

async function main() {
  const args = process.argv.slice(2);
  let targetSub = null;
  let targetUnit = null;
  let buildAll = false;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--subject' && args[i + 1]) targetSub = args[i + 1].toLowerCase();
    if (args[i] === '--unit' && args[i + 1]) targetUnit = parseInt(args[i + 1]);
    if (args[i] === '--all') buildAll = true;
  }

  const browser = await chromium.launch({
    executablePath: CHROME_PATH,
    headless: true
  });

  const allSubjects = ['cn', 'toc', 'ml', 'ai', 'se', 'rmipr', 'reactjs', 'evs'];

  try {
    if (buildAll) {
      for (const s of allSubjects) {
        for (const u of [1, 2, 3]) {
          await buildHandwrittenNotebook(browser, s, u);
        }
      }
    } else if (targetSub && targetUnit) {
      await buildHandwrittenNotebook(browser, targetSub, targetUnit);
    } else if (targetSub) {
      for (const u of [1, 2, 3]) {
        await buildHandwrittenNotebook(browser, targetSub, u);
      }
    } else {
      console.log('Running pilot on TOC Unit 1 and CN Unit 1...');
      await buildHandwrittenNotebook(browser, 'toc', 1);
      await buildHandwrittenNotebook(browser, 'cn', 1);
    }
  } finally {
    await browser.close();
  }
}

if (require.main === module) {
  main().catch(err => {
    console.error(err);
    process.exit(1);
  });
}

module.exports = { buildHandwrittenNotebook };
