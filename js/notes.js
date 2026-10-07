/**
 * SEM 5 · ISE Notes - Interactive Study Notes Shared Client Script
 * Lightweight vanilla JavaScript (No frameworks)
 * Manages: Theme synchronization, Reading Progress, Active TOC Highlight,
 *          Progress Tracking ('sem5_progress_v1'), Copy Buttons, Print Trigger,
 *          and KaTeX math rendering.
 */

(function () {
  'use strict';

  const STORAGE_KEYS = {
    THEME: 'sem5_theme_v1',
    PROGRESS: 'sem5_progress_v1'
  };

  // --- SVG Icons ---
  const ICONS = {
    sun: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`,
    moon: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`,
    check: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`
  };

  // --- DOM Ready Execution ---
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initReadingProgress();
    initTOC();
    initProgressTracking();
    initCopyButtons();
    initPrintButton();
    initMathRendering();
    initMobileTOCToggle();
  });

  // --- 1. Theme Synchronization ---
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

    // Read stored or system theme
    const storedTheme = localStorage.getItem(STORAGE_KEYS.THEME) ||
      (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    applyTheme(storedTheme);

    if (themeBtn) {
      themeBtn.addEventListener('click', () => {
        const currentTheme = html.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
      });
    }

    // Listen for cross-tab or cross-page storage updates
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

  // --- 3. Active TOC Heading Highlighting ---
  function initTOC() {
    const tocItems = document.querySelectorAll('.toc-item');
    const sections = document.querySelectorAll('section[id], h2[id], h3[id]');
    if (!tocItems.length || !sections.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          tocItems.forEach(item => {
            const link = item.querySelector('a');
            if (link && link.getAttribute('href') === '#' + id) {
              item.classList.add('active');
            } else if (link && !link.getAttribute('href').endsWith('#' + id)) {
              item.classList.remove('active');
            }
          });
        }
      });
    }, {
      rootMargin: '-80px 0px -70% 0px',
      threshold: 0
    });

    sections.forEach(sec => observer.observe(sec));
  }

  // --- 4. Progress Tracking Integration ---
  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEYS.PROGRESS) || '{}');
    } catch (e) {
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
      btn.innerHTML = `${ICONS.check} <span>DONE</span>`;
      btn.title = 'Mark as incomplete';
    } else {
      btn.classList.remove('active-done');
      btn.innerHTML = `<span>MARK AS DONE</span>`;
      btn.title = 'Mark this unit notes as studied';
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

  // --- 5. Code Copy Buttons ---
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

  // --- 6. Print Button ---
  function initPrintButton() {
    const printBtn = document.getElementById('print-btn');
    if (printBtn) {
      printBtn.addEventListener('click', () => {
        // Expand all collapsible answers before printing
        document.querySelectorAll('details.model-answer').forEach(d => d.setAttribute('open', 'true'));
        window.print();
      });
    }
  }

  // --- 7. KaTeX Math Auto-Rendering ---
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

  // --- 8. Mobile TOC Sheet Toggle ---
  function initMobileTOCToggle() {
    const mobileBtn = document.getElementById('mobile-toc-btn');
    const sidebar = document.getElementById('notes-sidebar');
    if (mobileBtn && sidebar) {
      mobileBtn.addEventListener('click', () => {
        const isOpen = sidebar.classList.toggle('mobile-open');
        mobileBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });

      // Auto-collapse mobile TOC upon clicking a heading link
      sidebar.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          if (window.innerWidth <= 980) {
            sidebar.classList.remove('mobile-open');
            mobileBtn.setAttribute('aria-expanded', 'false');
          }
        });
      });
    }
  }
})();
