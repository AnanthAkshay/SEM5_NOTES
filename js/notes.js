/**
 * SEM 5 · ISE Notes - Interactive Study Notes Shared Client Script
 * Lightweight vanilla JavaScript (Zero dependencies)
 * Handles: Theme sync, reading progress, active TOC scrollspy,
 *          progress tracking, code copy, print expansion, KaTeX render,
 *          and mobile TOC sheet with focus trap / Esc dismissal.
 */

(function () {
  'use strict';

  const STORAGE_KEYS = {
    THEME: 'sem5_theme_v1',
    PROGRESS: 'sem5_progress_v1'
  };

  const ICONS = {
    sun: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`,
    moon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`
  };

  // --- Initialize on DOMContentLoaded ---
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initReadingProgress();
    initTOC();
    initMobileTOCSheet();
    initProgressTracking();
    initCopyButtons();
    initPrintButton();
    initMathRendering();
    initQACards();
    initTables();
  });

  // --- 1. Theme Management ---
  function initTheme() {
    const html = document.documentElement;
    const themeBtn = document.getElementById('theme-toggle-btn');
    const themeIcon = document.getElementById('theme-icon');

    function applyTheme(theme) {
      html.setAttribute('data-theme', theme);
      localStorage.setItem(STORAGE_KEYS.THEME, theme);
      if (themeIcon) {
        themeIcon.innerHTML = theme === 'dark' ? ICONS.sun : ICONS.moon;
      }
      if (themeBtn) {
        themeBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
      }
    }

    const currentTheme = html.getAttribute('data-theme') ||
      localStorage.getItem(STORAGE_KEYS.THEME) ||
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    applyTheme(currentTheme);

    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const active = html.getAttribute('data-theme') || 'light';
        const next = active === 'dark' ? 'light' : 'dark';
        applyTheme(next);
      });
    }

    window.addEventListener('storage', (e) => {
      if (e.key === STORAGE_KEYS.THEME && e.newValue) {
        applyTheme(e.newValue);
      }
      if (e.key === STORAGE_KEYS.PROGRESS) {
        updateProgressButtonState();
      }
    });
  }

  // --- 2. Reading Progress Bar ---
  function initReadingProgress() {
    const bar = document.getElementById('reading-progress-bar');
    if (!bar) return;

    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      if (docHeight > 0) {
        const pct = Math.min(100, Math.max(0, (scrollTop / docHeight) * 100));
        bar.style.width = pct + '%';
      }
    }, { passive: true });
  }

  // --- 3. Active TOC Scrollspy ---
  function initTOC() {
    const links = Array.from(document.querySelectorAll('.toc-nav a'));
    const sections = Array.from(document.querySelectorAll('section[id], header[id], div[id].revision-sheet'));
    if (!links.length || !sections.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          links.forEach(link => {
            const href = link.getAttribute('href') || '';
            const isMatch = href === `#${id}`;
            const parentItem = link.closest('.toc-item') || link.parentElement;
            
            if (isMatch) {
              link.classList.add('active');
              if (parentItem && parentItem.classList.contains('toc-item')) {
                parentItem.classList.add('active');
              }
            } else {
              link.classList.remove('active');
              if (parentItem && parentItem.classList.contains('toc-item')) {
                parentItem.classList.remove('active');
              }
            }
          });
        }
      });
    }, {
      rootMargin: '-80px 0px -70% 0px',
      threshold: 0
    });

    sections.forEach(s => observer.observe(s));
  }

  // --- 4. Mobile TOC Sheet & Drawer ---
  function initMobileTOCSheet() {
    const mobileBtn = document.getElementById('mobile-toc-btn');
    const closeBtn = document.getElementById('close-toc-btn');
    const sidebar = document.getElementById('notes-sidebar');
    const backdrop = document.getElementById('sidebar-backdrop');
    const mql = window.matchMedia('(min-width: 1024px)');

    function openSheet() {
      if (!sidebar) return;
      sidebar.classList.add('mobile-open');
      if (backdrop) backdrop.classList.add('active');
      if (mobileBtn) mobileBtn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
      if (closeBtn) closeBtn.focus();
    }

    function closeSheet() {
      if (!sidebar) return;
      sidebar.classList.remove('mobile-open');
      if (backdrop) backdrop.classList.remove('active');
      if (mobileBtn) {
        mobileBtn.setAttribute('aria-expanded', 'false');
        mobileBtn.focus();
      }
      document.body.style.overflow = '';
    }

    if (mobileBtn) {
      mobileBtn.addEventListener('click', () => {
        const isOpen = sidebar && sidebar.classList.contains('mobile-open');
        if (isOpen) closeSheet();
        else openSheet();
      });
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', closeSheet);
    }

    if (backdrop) {
      backdrop.addEventListener('click', closeSheet);
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && sidebar && sidebar.classList.contains('mobile-open')) {
        closeSheet();
      }
    });

    // Close when clicking a TOC link on mobile
    if (sidebar) {
      sidebar.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          if (!mql.matches) {
            closeSheet();
          }
        });
      });
    }

    // Media query listener to reset state on window resize
    function handleBreakpoint(e) {
      if (e.matches) {
        // Desktop breakpoint: close mobile drawer and restore scroll
        if (sidebar) sidebar.classList.remove('mobile-open');
        if (backdrop) backdrop.classList.remove('active');
        if (mobileBtn) mobileBtn.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    }

    if (mql.addEventListener) {
      mql.addEventListener('change', handleBreakpoint);
    } else if (mql.addListener) {
      mql.addListener(handleBreakpoint);
    }
  }

  // --- 5. Progress Tracking ---
  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.PROGRESS) || '{}');
    } catch {
      return {};
    }
  }

  function updateProgressButtonState() {
    const btn = document.getElementById('mark-done-btn');
    if (!btn) return;
    const fileId = btn.getAttribute('data-file-id');
    if (!fileId) return;

    const progress = getProgress();
    const isDone = !!progress[fileId];

    if (isDone) {
      btn.classList.add('active-done');
      btn.querySelector('span').textContent = 'COMPLETED';
    } else {
      btn.classList.remove('active-done');
      btn.querySelector('span').textContent = 'MARK AS DONE';
    }
  }

  function initProgressTracking() {
    const btn = document.getElementById('mark-done-btn');
    if (!btn) return;

    updateProgressButtonState();

    btn.addEventListener('click', () => {
      const fileId = btn.getAttribute('data-file-id');
      if (!fileId) return;

      const progress = getProgress();
      if (progress[fileId]) {
        delete progress[fileId];
      } else {
        progress[fileId] = true;
      }
      localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(progress));
      updateProgressButtonState();
    });
  }

  // --- 6. Code Copy Buttons ---
  function initCopyButtons() {
    document.querySelectorAll('.copy-code-btn').forEach(btn => {
      btn.addEventListener('click', async () => {
        const wrap = btn.closest('.code-block-wrap');
        const codeEl = wrap ? wrap.querySelector('code, pre') : null;
        if (!codeEl) return;

        const text = codeEl.innerText;
        try {
          await navigator.clipboard.writeText(text);
          const origText = btn.textContent;
          btn.textContent = 'COPIED!';
          btn.style.color = 'var(--green-tint-ink)';
          btn.style.borderColor = 'var(--green)';
          setTimeout(() => {
            btn.textContent = origText;
            btn.style.color = '';
            btn.style.borderColor = '';
          }, 1800);
        } catch (err) {
          console.warn('Clipboard copy failed:', err);
        }
      });
    });
  }

  // --- 7. Print Button ---
  function initPrintButton() {
    const printBtn = document.getElementById('print-btn');
    if (printBtn) {
      printBtn.addEventListener('click', () => {
        document.querySelectorAll('details.model-answer').forEach(d => d.setAttribute('open', 'true'));
        document.querySelectorAll('.qa-card').forEach(c => {
          c.classList.add('open');
          const btn = c.querySelector('.qa-toggle');
          if (btn) btn.setAttribute('aria-expanded', 'true');
        });
        window.print();
      });
    }
  }

  // --- 8. KaTeX Math Auto-Rendering ---
  function initMathRendering() {
    if (typeof renderMathInElement === 'function') {
      renderMathInElement(document.body, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
      });
    }
  }

  // --- 9. QA Card Collapsible Toggles ---
  function initQACards() {
    document.querySelectorAll('.qa-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const card = btn.closest('.qa-card');
        if (card) {
          const isOpen = card.classList.toggle('open');
          btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        }
      });
    });
  }

  // --- 10. Table Containers ---
  function initTables() {
    document.querySelectorAll('article table').forEach(tbl => {
      if (!tbl.closest('.table-wrap') && !tbl.closest('.table-responsive')) {
        const wrap = document.createElement('div');
        wrap.className = 'table-wrap';
        tbl.parentNode.insertBefore(wrap, tbl);
        wrap.appendChild(tbl);
      }
    });
  }
})();
