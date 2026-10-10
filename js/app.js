/**
 * SEM 5 · ISE Notes - Core Application Logic
 * Department of Information Science & Engineering
 */

(function () {
  'use strict';

  // --- State & Constants ---
  const STORAGE_KEYS = {
    THEME: 'sem5_theme_v1',
    PROGRESS: 'sem5_progress_v5',
    PINNED: 'sem5_pinned_v1'
  };

  function loadAndMigrateProgress() {
    const validIds = new Set();
    if (window.SEM5_DATA && window.SEM5_DATA.subjects) {
      window.SEM5_DATA.subjects.forEach(s => {
        if (s.units) {
          s.units.forEach(u => {
            if (u.files) u.files.forEach(f => validIds.add(f.id));
          });
        }
      });
    }

    const raw = localStorage.getItem(STORAGE_KEYS.PROGRESS) ||
                localStorage.getItem('sem5_progress_v4') ||
                localStorage.getItem('sem5_progress_v3') ||
                localStorage.getItem('sem5_progress_v2') ||
                localStorage.getItem('sem5_progress_v1');
    if (raw) {
      try {
        const parsed = JSON.parse(raw);
        const migrated = {};
        Object.keys(parsed).forEach(k => {
          if (validIds.has(k) && parsed[k]) {
            migrated[k] = true;
          }
        });
        localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(migrated));
        return migrated;
      } catch (e) {
        return {};
      }
    }
    return {};
  }

  const state = {
    data: window.SEM5_DATA || { subjects: [], meta: {} },
    notesIndex: window.SEM5_NOTES_INDEX || [],
    theme: localStorage.getItem(STORAGE_KEYS.THEME) || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'),
    progress: loadAndMigrateProgress(),
    pinned: JSON.parse(localStorage.getItem(STORAGE_KEYS.PINNED) || '[]'),
    currentSubjectId: null,
    currentTab: 'notes',
    activeFilter: 'all',
    searchQuery: '',
    selectedSearchIdx: 0,
    searchResults: []
  };

  // --- DOM Elements Cache ---
  const elements = {
    html: document.documentElement,
    siteNav: document.getElementById('site-nav'),
    themeToggleBtn: document.getElementById('theme-toggle-btn'),
    themeIcon: document.getElementById('theme-icon'),
    mobileMenuBtn: document.getElementById('mobile-menu-btn'),
    closeMobileMenuBtn: document.getElementById('close-mobile-menu-btn'),
    mobileMenuDrawer: document.getElementById('mobile-menu-drawer'),
    drawerThemeToggleBtn: document.getElementById('drawer-theme-toggle-btn'),
    subjectsGrid: document.getElementById('subjects-grid'),
    filterPills: document.querySelectorAll('.filter-pill'),
    homeView: document.getElementById('home-view'),
    subjectView: document.getElementById('subject-view'),
    subjectContainer: document.getElementById('subject-container'),
    schemeView: document.getElementById('scheme-view'),
    schemeContainer: document.getElementById('scheme-container'),
    searchTriggerBtns: document.querySelectorAll('.search-trigger-btn'),
    searchModal: document.getElementById('search-modal'),
    searchInput: document.getElementById('search-input'),
    searchResultsBox: document.getElementById('search-results-box'),
    closeSearchBtn: document.getElementById('close-search-btn'),
    viewerModal: document.getElementById('viewer-modal'),
    viewerIframe: document.getElementById('viewer-iframe'),
    viewerImage: document.getElementById('viewer-image'),
    viewerImageWrap: document.getElementById('viewer-image-wrap'),
    viewerTitle: document.getElementById('viewer-title'),
    viewerDownloadBtn: document.getElementById('viewer-download-btn'),
    viewerNewTabBtn: document.getElementById('viewer-new-tab-btn'),
    closeViewerBtn: document.getElementById('close-viewer-btn'),
    resetProgressBtn: document.getElementById('reset-progress-btn'),
    currentYearSpan: document.getElementById('current-year-span')
  };

  // --- SVG Icons Map ---
  const ICONS = {
    sun: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`,
    moon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`,
    pin: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="17" x2="12" y2="22"></line><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24Z"></path></svg>`,
    pinnedFilled: `<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="17" x2="12" y2="22"></line><path d="M5 17h14v-1.76a2 2 0 0 0-1.11-1.79l-1.78-.9A2 2 0 0 1 15 10.76V6h1a1 1 0 0 0 1-1V3a1 1 0 0 0-1-1H8a1 1 0 0 0-1 1v2a1 1 0 0 0 1 1h1v4.76a2 2 0 0 1-1.11 1.79l-1.78.9A2 2 0 0 0 5 15.24Z"></path></svg>`,
    externalLink: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>`,
    download: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>`,
    eye: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>`,
    arrowLeft: `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>`,
    printer: `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"></polyline><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path><rect x="6" y="14" width="12" height="8"></rect></svg>`,
    check: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`
  };

  // --- Initial Setup ---
  function init() {
    applyTheme(state.theme);
    setupEventListeners();
    setupRouting();
    renderSubjectsGrid();

    // Load search index if not already present
    if (!state.notesIndex || state.notesIndex.length === 0) {
      if (window.SEM5_NOTES_INDEX) {
        state.notesIndex = window.SEM5_NOTES_INDEX;
      } else {
        fetch('data/notes-index.json')
          .then(res => res.ok ? res.json() : [])
          .then(data => { state.notesIndex = data; })
          .catch(() => {});
      }
    }
    
    // Platform-specific keyboard shortcut hint (Cmd K on Apple, Ctrl K elsewhere)
    const isMac = /(Mac|iPhone|iPod|iPad)/i.test(navigator.userAgent || navigator.platform || '');
    document.querySelectorAll('.search-keycap-hint').forEach(el => {
      el.textContent = isMac ? 'Cmd K' : 'Ctrl K';
    });
    if (elements.currentYearSpan) {
      elements.currentYearSpan.textContent = new Date().getFullYear();
    }
  }

  // --- Helpers for Date & CIE-1 Badges ---
  function getExamChip(subject) {
    if (!subject.examDate) return '';
    const parts = subject.examDate.split('-');
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    const day = parseInt(parts[2], 10);
    const mon = months[parseInt(parts[1], 10) - 1] || '';
    const startTime = (subject.examTime || '').split('–')[0].trim();
    const label = startTime ? `${day} ${mon} · ${startTime}` : `${day} ${mon}`;
    return `<span class="card-exam-chip" title="CIE-1 Exam Date & Time">${escapeHtml(label)}</span>`;
  }

  // --- Theme Management ---
  function applyTheme(theme) {
    state.theme = theme;
    elements.html.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
    const nextTheme = theme === 'dark' ? 'light' : 'dark';
    const nextLabel = `Switch to ${nextTheme} mode`;
    const iconSvg = theme === 'dark' ? ICONS.sun : ICONS.moon;

    if (elements.themeIcon) {
      elements.themeIcon.innerHTML = iconSvg;
    }
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.setAttribute('aria-label', nextLabel);
    }
    if (elements.drawerThemeToggleBtn) {
      elements.drawerThemeToggleBtn.innerHTML = `
        <span style="display:inline-flex; align-items:center; gap:0.5rem;">
          ${iconSvg}
          <span>SWITCH TO ${nextTheme.toUpperCase()} MODE</span>
        </span>
      `;
      elements.drawerThemeToggleBtn.setAttribute('aria-label', nextLabel);
    }
  }

  let lastThemeToggleTime = 0;
  function toggleTheme() {
    const now = Date.now();
    // Protect against rapid double-taps or duplicate event dispatches on mobile touch devices
    if (now - lastThemeToggleTime < 250) {
      return;
    }
    lastThemeToggleTime = now;
    applyTheme(state.theme === 'dark' ? 'light' : 'dark');
  }

  // --- Mobile Navigation Drawer ---
  function openMobileMenu() {
    if (elements.mobileMenuDrawer) {
      elements.mobileMenuDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeMobileMenu() {
    if (elements.mobileMenuDrawer) {
      elements.mobileMenuDrawer.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  // --- Routing & Navigation ---
  function setupRouting() {
    window.addEventListener('hashchange', handleHashChange);
    handleHashChange();
  }

  function handleHashChange() {
    const hash = window.location.hash.slice(1);
    if (hash === 'scheme') {
      openSchemeView(false);
    } else if (hash.startsWith('subject-') || hash.startsWith('subject/') || hash.startsWith('subject=')) {
      const subjectId = hash.replace(/^subject[-/=]/, '');
      openSubject(subjectId, false);
    } else {
      closeSubjectView(false);
      closeSchemeView(false);
    }
  }

  function openSubject(subjectId, pushHistory = true) {
    const subject = state.data.subjects.find(s => s.id === subjectId);
    if (!subject) {
      closeSubjectView(pushHistory);
      return;
    }
    state.currentSubjectId = subjectId;
    state.currentTab = subject.status === 'syllabus_only' ? 'syllabus' : 'notes';
    if (pushHistory) {
      window.location.hash = `subject/${subjectId}`;
    }

    renderSubjectDetail(subject);
    elements.homeView.classList.remove('active');
    if (elements.schemeView) elements.schemeView.classList.remove('active');
    elements.subjectView.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function closeSubjectView(pushHistory = true) {
    state.currentSubjectId = null;
    if (pushHistory) {
      window.location.hash = '';
    }
    elements.subjectView.classList.remove('active');
    if (elements.schemeView) elements.schemeView.classList.remove('active');
    elements.homeView.classList.add('active');
    renderSubjectsGrid();
  }

  function openSchemeView(pushHistory = true) {
    state.currentSubjectId = null;
    if (pushHistory) {
      window.location.hash = 'scheme';
    }
    renderSchemeView();
    elements.homeView.classList.remove('active');
    elements.subjectView.classList.remove('active');
    if (elements.schemeView) elements.schemeView.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function closeSchemeView(pushHistory = true) {
    if (pushHistory) {
      window.location.hash = '';
    }
    if (elements.schemeView) elements.schemeView.classList.remove('active');
    elements.homeView.classList.add('active');
    renderSubjectsGrid();
  }

  // --- Calculations & Progress Helpers ---
  function getSubjectFileCount(subject) {
    let count = 0;
    subject.units.forEach(u => {
      count += u.files.length;
    });
    return count;
  }

  function getSubjectProgress(subject) {
    let total = 0;
    let completed = 0;
    subject.units.forEach(u => {
      u.files.forEach(f => {
        total++;
        if (state.progress[f.id]) {
          completed++;
        }
      });
    });
    return {
      total,
      completed,
      pct: total > 0 ? Math.round((completed / total) * 100) : 0
    };
  }

  function toggleFileProgress(fileId) {
    if (state.progress[fileId]) {
      delete state.progress[fileId];
    } else {
      state.progress[fileId] = true;
    }
    localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(state.progress));
    
    // Update active UI elements without full page flicker
    if (state.currentSubjectId) {
      const subject = state.data.subjects.find(s => s.id === state.currentSubjectId);
      if (subject) {
        updateSubjectProgressUI(subject);
      }
    } else {
      renderSubjectsGrid();
    }
  }

  function resetAllProgress() {
    if (confirm("Are you sure you want to reset your study progress? All completed file marks will be cleared.")) {
      state.progress = {};
      localStorage.removeItem(STORAGE_KEYS.PROGRESS);
      if (state.currentSubjectId) {
        const subject = state.data.subjects.find(s => s.id === state.currentSubjectId);
        if (subject) renderSubjectDetail(subject);
      } else {
        renderSubjectsGrid();
      }
    }
  }

  // --- Favorites / Pinned Subjects ---
  function togglePinSubject(subjectId, e) {
    if (e) {
      e.stopPropagation();
      e.preventDefault();
    }
    const idx = state.pinned.indexOf(subjectId);
    if (idx > -1) {
      state.pinned.splice(idx, 1);
    } else {
      state.pinned.push(subjectId);
    }
    localStorage.setItem(STORAGE_KEYS.PINNED, JSON.stringify(state.pinned));
    renderSubjectsGrid();
    if (state.currentSubjectId === subjectId) {
      const pinBtn = document.getElementById('subject-header-pin-btn');
      if (pinBtn) {
        const isPinned = state.pinned.includes(subjectId);
        pinBtn.classList.toggle('pinned', isPinned);
        pinBtn.innerHTML = `${isPinned ? ICONS.pinnedFilled : ICONS.pin} <span>${isPinned ? 'Pinned Subject' : 'Pin Subject'}</span>`;
      }
    }
  }

  // --- Render Subjects Grid ("What We Do" Card Style) ---
  function renderSubjectsGrid() {
    if (!elements.subjectsGrid) return;

    // Filter & Sort subjects: Pinned first, then by configured order
    let list = [...state.data.subjects];
    if (state.activeFilter === 'core') {
      list = list.filter(s => s.tags && s.tags.some(t => t.toLowerCase().includes('core')));
    } else if (state.activeFilter === 'elective') {
      list = list.filter(s => !s.tags || !s.tags.some(t => t.toLowerCase().includes('core')));
    } else if (state.activeFilter === 'practice') {
      list = list.filter(s => s.units && s.units.some(u => u.isPractice || (u.files && u.files.some(f => f.type === 'pyq' || f.isPYQ))));
    }

    list.sort((a, b) => {
      const aPinned = state.pinned.includes(a.id);
      const bPinned = state.pinned.includes(b.id);
      if (aPinned && !bPinned) return -1;
      if (!aPinned && bPinned) return 1;
      return 0;
    });

    const renderedCards = [];
    list.forEach(subject => {
      try {
        const isPinned = state.pinned.includes(subject.id);
        const progress = getSubjectProgress(subject);
        const shortInitial = subject.shortName || subject.code;

        // Dynamic Hashtag chips based on actual contents
        const chips = [];
        const hasInteractiveNotes = subject.units && subject.units.some(u => u.files && u.files.some(f => f.type === 'notes'));
        if (hasInteractiveNotes) {
          chips.push('# Interactive notes');
        } else if (subject.status === 'full_notes') {
          chips.push('# Notes');
        } else {
          chips.push('# Syllabus only');
        }
        const hasHandwritten = subject.units && subject.units.some(u => u.files && u.files.some(f => f.type === 'handwritten'));
        if (hasHandwritten) {
          chips.push('# Handwritten notebooks');
        }
        if (subject.units && subject.units.some(u => u.isPractice)) {
          chips.push('# Practice');
        }
        if (subject.lab) {
          chips.push('# Lab (Syllabus only)');
        }

        renderedCards.push(`
          <a href="#subject/${subject.id}" class="subject-card" data-subject="${subject.id}" data-href="#subject/${subject.id}" onclick="window.SEM5_APP.openSubject('${subject.id}'); return false;" role="button" tabindex="0" aria-label="Open ${escapeHtml(subject.name)} notes" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault(); window.SEM5_APP.openSubject('${subject.id}');}">
            <div class="card-top-row">
              <div style="display:flex;align-items:center;gap:0.5rem;flex-wrap:wrap;">
                <span class="card-code-circle" aria-hidden="true">${escapeHtml(shortInitial)}</span>
                ${getExamChip(subject)}
              </div>
              <button class="pin-btn ${isPinned ? 'pinned' : ''}" onclick="window.SEM5_APP.togglePinSubject('${subject.id}', event)" title="${isPinned ? 'Unpin' : 'Pin subject to top'}" aria-label="${isPinned ? 'Unpin' : 'Pin'}">
                ${isPinned ? ICONS.pinnedFilled : ICONS.pin}
              </button>
            </div>

            <div class="card-main-info">
              <h3 class="card-title">${escapeHtml(subject.name)}</h3>
              <p class="card-desc">${escapeHtml(subject.description)}</p>
              <div class="card-meta-line">
                <span>${escapeHtml(subject.credits || 'TBD')} Credits</span>
                ${subject.coordinator ? ` · <span>${escapeHtml(subject.coordinator)}</span>` : ''}
                ${subject.contactHours ? ` · <span>${escapeHtml(subject.contactHours)}</span>` : ''}
              </div>
              ${progress.total > 0 ? `
                <div class="card-progress-pill" title="${progress.completed} of ${progress.total} studied (${progress.pct}%)">
                  <div class="card-progress-fill" style="width: ${progress.pct}%;"></div>
                </div>
              ` : ''}
            </div>

            <div class="card-footer-row">
              <div class="card-chips-left">
                ${chips.map(chip => `<span class="hash-chip">${escapeHtml(chip)}</span>`).join('')}
              </div>
              <span class="card-arrow-btn" aria-hidden="true">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
              </span>
            </div>
          </a>
        `);
      } catch (cardErr) {
        console.error(`Error rendering card for subject [${subject ? subject.id : 'unknown'}]:`, cardErr);
      }
    });

    elements.subjectsGrid.innerHTML = renderedCards.join('');
  }

  // --- Render Subject Detail View ---
  function renderSubjectDetail(subject) {
    if (!elements.subjectContainer) return;

    const isPinned = state.pinned.includes(subject.id);
    const progress = getSubjectProgress(subject);
    const hasRichSyllabus = !!subject.syllabus;
    const hasPractice = subject.units.some(u => u.isPractice);
    const hasLab = !!subject.lab;

    // Default tab logic
    if (state.currentTab === 'syllabus' && !hasRichSyllabus) {
      state.currentTab = 'notes';
    } else if (state.currentTab === 'practice' && !hasPractice) {
      state.currentTab = 'notes';
    } else if (state.currentTab === 'lab' && !hasLab) {
      state.currentTab = 'notes';
    }

    elements.subjectContainer.innerHTML = `
      <div class="subject-view-header">
        <div class="back-btn-row">
          <button class="back-pill-btn" onclick="window.SEM5_APP.closeSubjectView()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
            <span>ALL SUBJECTS</span>
          </button>
          <div class="subject-action-row" style="display:flex;gap:0.5rem;">
            <button id="subject-header-pin-btn" class="pill-btn-outline pill-btn-sm ${isPinned ? 'pinned' : ''}" onclick="window.SEM5_APP.togglePinSubject('${subject.id}', event)">
              ${isPinned ? ICONS.pinnedFilled : ICONS.pin} <span>${isPinned ? 'PINNED' : 'PIN'}</span>
            </button>
            ${hasRichSyllabus ? `
              <button class="pill-btn-outline pill-btn-sm" onclick="window.print()" title="Print Syllabus">
                ${ICONS.printer} <span>PRINT</span>
              </button>
            ` : ''}
          </div>
        </div>

        <div class="subject-meta-pill-bar">
          <span class="pill-tag-green">${escapeHtml(subject.code)}</span>
          <span class="pill-btn-outline pill-btn-sm" style="cursor:default;">${escapeHtml(subject.credits || '3')} CREDITS</span>
          ${subject.contactHours ? `<span class="card-meta-line">${escapeHtml(subject.contactHours)}</span>` : ''}
          ${subject.coordinator ? `<span class="card-meta-line">Coord: ${escapeHtml(subject.coordinator)}</span>` : ''}
          ${subject.prerequisites ? `<span class="card-meta-line">Prereq: ${escapeHtml(subject.prerequisites)}</span>` : ''}
        </div>

        <h1 class="subject-view-title">${escapeHtml(subject.name)}</h1>
        <p class="subject-view-desc">${escapeHtml(subject.description)}</p>

        ${subject.cie1Scope ? `
          <div class="subject-scope-line" style="margin-top: 0.75rem;">
            <span class="scope-pill-label">CIE-1 Scope:</span>
            <span class="scope-pill-text">${escapeHtml(subject.cie1Scope)}</span>
          </div>
        ` : ''}

        ${progress.total > 0 ? `
          <div class="overall-progress-box">
            <span class="card-meta-line" style="font-weight:700;color:var(--ink);">${progress.completed} of ${progress.total} Completed (${progress.pct}%)</span>
            <div class="progress-pill-track">
              <div id="subject-progress-fill" class="progress-pill-fill" style="width: ${progress.pct}%;"></div>
            </div>
          </div>
        ` : ''}
      </div>

      <!-- Notice card for Subjects without full unit notes yet -->
      ${subject.notesNotice ? `
        <div class="notice-card">
          <h4 class="notice-title">Status: Syllabus Only</h4>
          <p class="notice-text">${escapeHtml(subject.notesNotice)}</p>
        </div>
      ` : ''}

      <!-- Pill Segmented Control Tabs (Like One-Time/Monthly in Reference) -->
      <div class="subject-tabs-track">
        <button class="segmented-tab ${state.currentTab === 'notes' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('notes')">
          Notes &amp; Docs (${subject.units.filter(u => !u.isPractice && typeof u.unitNumber === 'number').reduce((acc, u) => acc + u.files.length, 0)})
        </button>
        <button class="segmented-tab ${state.currentTab === 'pyq' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('pyq')">
          Solved PYQs
        </button>
        ${hasPractice ? `
          <button class="segmented-tab ${state.currentTab === 'practice' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('practice')">
            Practice (${subject.units.filter(u => u.isPractice).reduce((acc, u) => acc + u.files.length, 0)})
          </button>
        ` : ''}
        ${hasLab ? `
          <button class="segmented-tab ${state.currentTab === 'lab' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('lab')">
            Laboratory (${escapeHtml(subject.lab.code || 'Lab')})
          </button>
        ` : ''}
        ${hasRichSyllabus ? `
          <button class="segmented-tab ${state.currentTab === 'syllabus' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('syllabus')">
            Syllabus &amp; Books
          </button>
        ` : ''}
      </div>

      <!-- Tab Content: Notes or Practice -->
      ${state.currentTab === 'notes' || state.currentTab === 'practice' ? `
        <div class="units-stack">
          ${renderUnitsList(subject, state.currentTab === 'practice')}
        </div>
      ` : ''}

      <!-- Tab Content: PYQ & Answers View -->
      ${state.currentTab === 'pyq' ? renderPyqTab(subject) : ''}

      <!-- Tab Content: Rich Syllabus View -->
      ${state.currentTab === 'syllabus' && hasRichSyllabus ? renderSyllabusView(subject) : ''}

      <!-- Tab Content: Laboratory Programs View -->
      ${state.currentTab === 'lab' && hasLab ? renderLabView(subject) : ''}
    `;
  }

  function updateSubjectProgressUI(subject) {
    const progress = getSubjectProgress(subject);
    const fillEl = document.getElementById('subject-progress-fill');
    if (fillEl) fillEl.style.width = `${progress.pct}%`;
  }

  function switchTab(tabName) {
    state.currentTab = tabName;
    const subject = state.data.subjects.find(s => s.id === state.currentSubjectId);
    if (subject) {
      renderSubjectDetail(subject);
    }
  }

  // --- Units Collapse/Expand State Helper ---
  function toggleAllUnits() {
    const container = document.getElementById('subject-container');
    if (!container) return;
    const detailsList = container.querySelectorAll('details.unit-pill-card');
    if (!detailsList.length) return;

    const anyOpen = Array.from(detailsList).some(d => d.open);
    const shouldOpen = !anyOpen;

    detailsList.forEach(d => {
      d.open = shouldOpen;
    });

    const toggleBtn = document.getElementById('toggle-all-units-btn');
    if (toggleBtn) {
      toggleBtn.setAttribute('aria-expanded', shouldOpen ? 'true' : 'false');
      toggleBtn.innerHTML = `<span>${shouldOpen ? 'COLLAPSE ALL' : 'EXPAND ALL'}</span>`;
    }

    if (state.currentSubjectId) {
      sessionStorage.setItem(`units_collapsed_${state.currentSubjectId}_${state.currentTab}`, shouldOpen ? 'false' : 'true');
    }
  }

  function syncToggleAllButton() {
    const toggleBtn = document.getElementById('toggle-all-units-btn');
    const container = document.getElementById('subject-container');
    if (!toggleBtn || !container) return;
    const detailsList = container.querySelectorAll('details.unit-pill-card');
    if (!detailsList.length) return;
    const anyOpen = Array.from(detailsList).some(d => d.open);
    toggleBtn.setAttribute('aria-expanded', anyOpen ? 'true' : 'false');
    toggleBtn.innerHTML = `<span>${anyOpen ? 'COLLAPSE ALL' : 'EXPAND ALL'}</span>`;
  }

  // --- Render PYQ & Answers Tab View ---
  function renderPyqTab(subject) {
    const pyqUnit = subject.units.find(u => u.unitNumber === 'PYQ');
    const pyqInteractiveFile = pyqUnit && pyqUnit.files ? pyqUnit.files.find(f => f.type === 'pyq') : null;
    const pyqHwFile = pyqUnit && pyqUnit.files ? pyqUnit.files.find(f => f.type === 'handwritten') : null;
    const pyqBundleFile = pyqUnit && pyqUnit.files ? pyqUnit.files.find(f => f.type === 'pdf') : null;

    const questions = (state.notesIndex || []).filter(e => e.type === 'pyq' && e.subject === subject.id);

    return `
      <div class="pyq-hub-container" style="display:flex; flex-direction:column; gap:1.5rem;">
        <!-- PYQ Quick Access Hero Cards -->
        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:1rem;">
          ${pyqInteractiveFile ? `
            <div class="scheme-section-card" style="padding:1.25rem 1.5rem; margin-bottom:0; display:flex; flex-direction:column; justify-content:space-between; gap:1rem; border:1.5px solid var(--green);">
              <div>
                <span class="pill-tag-green" style="font-size:11px;">Interactive Model Answers</span>
                <h3 style="font-family:var(--font-display); font-size:1.15rem; font-weight:700; color:var(--ink); margin:0.5rem 0 0.35rem 0;">${escapeHtml(pyqInteractiveFile.title)}</h3>
                <p style="font-size:12px; color:var(--ink-muted); margin:0;">Complete 2M, 5M &amp; 10M model answers with derivations, diagrams, worked arithmetic, and textbook citations.</p>
              </div>
              <div style="display:flex; gap:0.5rem;">
                <a href="${pyqInteractiveFile.path}" class="pill-btn-green pill-btn-sm" style="flex:1; justify-content:center;">
                  ${ICONS.eye} <span>OPEN ANSWERS</span>
                </a>
                <a href="${pyqInteractiveFile.path}" target="_blank" rel="noopener" class="pill-btn-outline pill-btn-sm" title="Open in new tab">
                  ${ICONS.externalLink}
                </a>
              </div>
            </div>
          ` : ''}

          ${pyqHwFile ? `
            <div class="scheme-section-card" style="padding:1.25rem 1.5rem; margin-bottom:0; display:flex; flex-direction:column; justify-content:space-between; gap:1rem;">
              <div>
                <span class="pill-tag-purple" style="font-size:11px;">Handwritten PDF Notebook</span>
                <h3 style="font-family:var(--font-display); font-size:1.15rem; font-weight:700; color:var(--ink); margin:0.5rem 0 0.35rem 0;">${escapeHtml(pyqHwFile.title)}</h3>
                <p style="font-size:12px; color:var(--ink-muted); margin:0;">${pyqHwFile.pages} Pages vector handwritten PDF formatted for quick mobile revision before the exam.</p>
              </div>
              <div style="display:flex; gap:0.5rem;">
                <button class="pill-btn-green pill-btn-sm" onclick="window.SEM5_APP.openViewer('${pyqHwFile.id}')" style="flex:1; justify-content:center;">
                  ${ICONS.eye} <span>VIEW PDF</span>
                </button>
                <a href="${pyqHwFile.path}" download class="pill-btn-outline pill-btn-sm" title="Download PDF">
                  ${ICONS.download}
                </a>
              </div>
            </div>
          ` : ''}

          ${pyqBundleFile ? `
            <div class="scheme-section-card" style="padding:1.25rem 1.5rem; margin-bottom:0; display:flex; flex-direction:column; justify-content:space-between; gap:1rem;">
              <div>
                <span class="pill-tag-amber" style="font-size:11px; background:rgba(245,158,11,0.15); color:#d97706; padding:2px 8px; border-radius:999px;">Original Papers Bundle</span>
                <h3 style="font-family:var(--font-display); font-size:1.15rem; font-weight:700; color:var(--ink); margin:0.5rem 0 0.35rem 0;">${escapeHtml(pyqBundleFile.title)}</h3>
                <p style="font-size:12px; color:var(--ink-muted); margin:0;">Official CIE and SEE question paper bundle scan (${pyqBundleFile.size}).</p>
              </div>
              <div style="display:flex; gap:0.5rem;">
                <button class="pill-btn-green pill-btn-sm" onclick="window.SEM5_APP.openViewer('${pyqBundleFile.id}')" style="flex:1; justify-content:center;">
                  ${ICONS.eye} <span>VIEW PAPER</span>
                </button>
                <a href="${pyqBundleFile.path}" download class="pill-btn-outline pill-btn-sm" title="Download PDF">
                  ${ICONS.download}
                </a>
              </div>
            </div>
          ` : ''}
        </div>

        <!-- Question Bank Filter & List -->
        <div class="scheme-section-card" style="margin-bottom:0;">
          <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:0.75rem; margin-bottom:1.25rem;">
            <div>
              <h2 class="syl-card-title" style="margin:0 0 0.25rem 0;">CIE-1 In-Scope Solved Questions (${questions.length})</h2>
              <p style="font-size:12px; color:var(--ink-muted); margin:0;">Click any question to view its verified model answer or mark it as revised.</p>
            </div>
            <a href="notes/${subject.id}/pyq/pyq-answers.html" class="pill-btn-outline pill-btn-sm">
              <span>VIEW FULL MODEL ANSWERS PAGE →</span>
            </a>
          </div>

          <div class="pyq-questions-stack" style="display:flex; flex-direction:column; gap:0.6rem;">
            ${questions.length > 0 ? questions.map(q => {
              const isDone = !!state.progress[q.questionId];
              return `
                <div class="file-row ${isDone ? 'is-done' : ''}" style="padding:0.75rem 1rem;">
                  <div class="file-info-group">
                    <label class="done-checkbox-wrap" title="Mark as revised">
                      <input type="checkbox" class="done-checkbox" ${isDone ? 'checked' : ''} onchange="window.SEM5_APP.toggleFileProgress('${q.questionId}')" />
                    </label>
                    <span class="file-type-pill file-type-pyq">${escapeHtml(q.marks || 'PYQ')}</span>
                    <div class="file-details-col">
                      <div class="file-title-wrap">
                        <a href="${q.path}" class="file-title" style="text-decoration:none; color:inherit; font-weight:600;">
                          ${escapeHtml(q.title)}
                        </a>
                      </div>
                      <div class="file-submeta">
                        <span class="code-mono">${escapeHtml(q.exam || 'CIE-1')}</span>
                        <span>·</span>
                        <span>Unit ${q.unit}</span>
                        ${q.sectionId ? `<span>· §${escapeHtml(q.sectionId)}</span>` : ''}
                      </div>
                    </div>
                  </div>
                  <div class="file-actions-group">
                    <a href="${q.path}" class="pill-btn-green pill-btn-sm">
                      ${ICONS.eye} <span>ANSWER</span>
                    </a>
                  </div>
                </div>
              `;
            }).join('') : `
              <p style="font-size:13px; color:var(--ink-muted); padding:1rem; text-align:center;">
                Visit the <a href="notes/${subject.id}/pyq/pyq-answers.html" style="color:var(--green); font-weight:700;">Solved PYQ Bank</a> for complete question list and answers.
              </p>
            `}
          </div>
        </div>
      </div>
    `;
  }

  // --- Render Units & Files List ---
  function renderUnitsList(subject, isPracticeOnly = false) {
    const units = subject.units.filter(u => isPracticeOnly ? u.isPractice : (!u.isPractice && typeof u.unitNumber === 'number'));

    if (units.length === 0) {
      return `
        <div class="notice-card">
          <p class="notice-text">No documents in this category yet. Check back soon!</p>
        </div>
      `;
    }

    const isCollapsed = sessionStorage.getItem(`units_collapsed_${subject.id}_${state.currentTab}`) === 'true';
    const isOpen = !isCollapsed ? 'open' : '';

    return `
      <div class="units-header-bar">
        <span class="units-count-label">${units.length} ${units.length === 1 ? 'UNIT' : 'UNITS'}</span>
        <button id="toggle-all-units-btn" class="pill-btn-outline pill-btn-sm toggle-all-btn" onclick="window.SEM5_APP.toggleAllUnits()" aria-expanded="${!isCollapsed ? 'true' : 'false'}">
          <span>${!isCollapsed ? 'COLLAPSE ALL' : 'EXPAND ALL'}</span>
        </button>
      </div>

      <div class="units-details-container">
        ${units.map((unit, idx) => {
          const isSyllabusOnly = unit.isSyllabusOnly || unit.unitNumber === 4 || unit.unitNumber === 5 || !unit.files || unit.files.length === 0;
          return `
          <details class="unit-pill-card" ${isOpen} ontoggle="window.SEM5_APP.syncToggleAllButton()">
            <summary class="unit-card-summary">
              <div class="unit-summary-info">
                <span class="pill-tag-green">
                  ${unit.isPractice ? 'Practice' : (typeof unit.unitNumber === 'number' ? `Unit ${unit.unitNumber}` : unit.unitNumber)}
                </span>
                <h3 class="unit-summary-title">${escapeHtml(unit.title)}</h3>
                ${isSyllabusOnly ? `
                  <span class="pill-tag-amber" style="font-size:11px;padding:2px 8px;margin-left:6px;background:rgba(245,158,11,0.15);color:#d97706;border:1px solid rgba(245,158,11,0.3);border-radius:999px;">Syllabus only</span>
                ` : ''}
              </div>
              <div class="unit-summary-meta">
                <span>${unit.files ? unit.files.length : 0} ${unit.files && unit.files.length === 1 ? 'file' : 'files'}</span>
                <span class="unit-chevron" aria-hidden="true">▾</span>
              </div>
            </summary>

            <div class="unit-card-body">
              ${unit.topics ? `
                <p class="unit-topics-snippet">
                  <strong>Key Coverage:</strong> ${escapeHtml(unit.topics)}
                </p>
              ` : ''}

              <div class="files-list">
                ${unit.files && unit.files.length > 0 ? unit.files.map(file => renderFileRow(file, subject)).join('') : `
                  <div class="empty-unit-notice" style="padding: 12px 16px; color: var(--text-muted); font-size: 13px; font-style: italic; background: rgba(0,0,0,0.02); border-radius: 6px;">
                    📋 Syllabus only — No HTML or handwritten study notes are uploaded for this unit.
                  </div>
                `}
              </div>
            </div>
          </details>
        `}).join('')}
      </div>
    `;
  }

  function renderFileRow(file, subject) {
    const isDone = !!state.progress[file.id];
    const isNotes = file.type === 'notes';
    const isHandwrittenPdf = file.type === 'handwritten';
    const isWebHtml = isNotes || (file.path && file.path.endsWith('.html'));
    const isLarge = file.sizeBytes && file.sizeBytes > 20000000;
    const largeNote = isLarge ? `(~${Math.round(file.sizeBytes / 1048576)} MB)` : '';

    let pillLabel = file.type.toUpperCase();
    if (isNotes) pillLabel = 'NOTES';
    else if (isHandwrittenPdf) pillLabel = 'NOTEBOOK (PDF)';
    else if (file.type === 'pyq') pillLabel = 'PYQ BANK';

    return `
      <div class="file-row ${isDone ? 'is-done' : ''}" id="file-row-${file.id}">
        <div class="file-info-group">
          <label class="done-checkbox-wrap" title="Mark as studied">
            <input type="checkbox" class="done-checkbox" ${isDone ? 'checked' : ''} onchange="window.SEM5_APP.toggleFileProgress('${file.id}')" aria-label="Mark ${escapeHtml(file.title)} as studied" />
          </label>

          <span class="file-type-pill ${isNotes ? 'file-type-notes' : ''} ${isHandwrittenPdf ? 'file-type-handwritten' : ''} ${file.type === 'pyq' ? 'file-type-pyq' : ''}">${pillLabel}</span>

          <div class="file-details-col">
            <div class="file-title-wrap">
              <span class="file-title">${escapeHtml(file.title)}</span>
              ${file.tag ? `<span class="${isHandwrittenPdf ? 'pill-tag-purple' : 'pill-tag-green'}" style="font-size:10px;padding:2px 7px;">${escapeHtml(file.tag)}</span>` : ''}
              ${file.coverageTag ? `<span class="pill-tag-green" style="font-size:10px;padding:2px 7px;">${escapeHtml(file.coverageTag)}</span>` : ''}
              ${file.scopeTag ? `<span class="pill-tag-amber" style="font-size:10px;padding:2px 7px;background:rgba(245,158,11,0.15);color:#d97706;border:1px solid rgba(245,158,11,0.3);border-radius:999px;">${escapeHtml(file.scopeTag)}</span>` : ''}
              ${file.isAlternate ? `<span class="pill-tag-green" style="font-size:10px;padding:2px 7px;">Condensed</span>` : ''}
              ${file.isConverted ? `<span class="file-tag-converted">(Converted for preview)</span>` : ''}
              ${isLarge ? `<span class="kbd-shortcut" title="Consider alternate notes on mobile data">${largeNote}</span>` : ''}
            </div>
            <div class="file-submeta">
              <span class="code-mono">${file.pages ? `${file.pages} pages · ` : ''}${file.readingTime || file.size}</span>
              <span>·</span>
              <span title="Original file name">${escapeHtml(file.originalName)}</span>
              ${file.generated ? `<span style="opacity:0.75; font-size: 11px;">· (generated from unit notes)</span>` : ''}
            </div>
          </div>
        </div>

        <div class="file-actions-group">
          ${isWebHtml ? `
            <a href="${file.path}" class="pill-btn-green pill-btn-sm view-btn" title="Read interactive unit notes">
              ${ICONS.eye} <span>READ</span>
            </a>
            <a href="${file.path}" target="_blank" rel="noopener" class="pill-btn-outline pill-btn-sm" title="Open notes in new browser tab">
              ${ICONS.externalLink} <span>NEW TAB</span>
            </a>
            ${file.originalPath ? `
              <a href="${file.originalPath}" download class="pill-btn-outline pill-btn-sm" title="Download original format (${file.type.toUpperCase()})">
                ${ICONS.download} <span>${file.originalPath.split('.').pop().toUpperCase()}</span>
              </a>
            ` : ''}
          ` : `
            <button class="pill-btn-green pill-btn-sm view-btn" onclick="window.SEM5_APP.openViewer('${file.id}')" title="Read in built-in PDF viewer">
              ${ICONS.eye} <span>VIEW</span>
            </button>
            <a href="${file.path}" download class="pill-btn-outline pill-btn-sm" title="Download PDF copy">
              ${ICONS.download} <span>DOWNLOAD</span>
            </a>
            ${file.originalPath ? `
              <a href="${file.originalPath}" download class="pill-btn-outline pill-btn-sm" title="Download original format (${file.type.toUpperCase()})">
                ${ICONS.download} <span>${file.originalPath.split('.').pop().toUpperCase()}</span>
              </a>
            ` : ''}
          `}
        </div>
      </div>
    `;
  }

  // --- Render Transcribed Syllabus & Books ---
  function renderSyllabusView(subject) {
    const syl = subject.syllabus;
    if (!syl) return '';

    const isCollapsed = sessionStorage.getItem(`units_collapsed_${subject.id}_${state.currentTab}`) === 'true';
    const isOpen = !isCollapsed ? 'open' : '';

    return `
      <div class="syllabus-container">
        <!-- Units Outline -->
        <div class="syllabus-section-card">
          <div class="units-header-bar">
            <h2 class="syl-card-title" style="margin-bottom:0;">Detailed Unit Syllabus &amp; NPTEL Video Lectures</h2>
            <button id="toggle-all-units-btn" class="pill-btn-outline pill-btn-sm toggle-all-btn" onclick="window.SEM5_APP.toggleAllUnits()" aria-expanded="${!isCollapsed ? 'true' : 'false'}">
              <span>${!isCollapsed ? 'COLLAPSE ALL' : 'EXPAND ALL'}</span>
            </button>
          </div>
          <div class="units-details-container" style="margin-top:1.25rem;">
            ${syl.units.map((u, idx) => `
              <details class="unit-pill-card" ${isOpen} ontoggle="window.SEM5_APP.syncToggleAllButton()" style="margin-bottom:1rem;">
                <summary class="unit-card-summary">
                  <div class="unit-summary-info">
                    <span class="pill-tag-green">Unit ${idx + 1}</span>
                    <h3 class="unit-summary-title">${escapeHtml(u.title)}</h3>
                  </div>
                  <div class="unit-summary-meta">
                    ${u.links && u.links.length > 0 ? `<span>${u.links.length} lectures</span>` : ''}
                    <span class="unit-chevron" aria-hidden="true">▾</span>
                  </div>
                </summary>
                <div class="unit-card-body" style="padding: 1.25rem 1.75rem;">
                  <p class="syl-unit-topics">${escapeHtml(u.topics)}</p>
                  ${u.pedagogy ? `<p class="syl-pedagogy" style="margin-top:0.5rem;"><strong>Pedagogy:</strong> ${escapeHtml(u.pedagogy)}</p>` : ''}
                  ${u.links && u.links.length > 0 ? `
                    <div class="syl-links-list">
                      ${u.links.map(l => `
                        <a href="${l.url}" target="_blank" rel="noopener noreferrer" class="syl-link-pill">
                          ${ICONS.externalLink} <span>${escapeHtml(l.label)}</span>
                        </a>
                      `).join('')}
                    </div>
                  ` : ''}
                </div>
              </details>
            `).join('')}
          </div>
        </div>

        <!-- Prescribed Textbooks & Reference Books -->
        <div class="syllabus-section-card">
          <h2 class="syl-card-title">Prescribed Textbooks & References</h2>
          <div class="books-grid">
            ${syl.textbook ? `
              <div class="book-card">
                <span class="book-tag">Prescribed Core Textbook</span>
                <h4 class="book-title">${escapeHtml(syl.textbook.title)}</h4>
                <p class="book-author">${escapeHtml(syl.textbook.authors)} (${escapeHtml(syl.textbook.edition)})</p>
                <p style="font-size:0.75rem;color:var(--text-muted);margin-top:0.25rem;">${escapeHtml(syl.textbook.publisher)}</p>
              </div>
            ` : ''}
            ${syl.referenceBooks ? syl.referenceBooks.map(b => `
              <div class="book-card">
                <span class="book-tag">Reference Book</span>
                <h4 class="book-title">${escapeHtml(b.title)}</h4>
                <p class="book-author">${escapeHtml(b.authors)} (${escapeHtml(b.edition)})</p>
                <p style="font-size:0.75rem;color:var(--text-muted);margin-top:0.25rem;">${escapeHtml(b.publisher)}</p>
              </div>
            `).join('') : ''}
          </div>
        </div>

        <!-- CIE-1 Academic Sources & Faculty Citations -->
        <div class="syllabus-section-card">
          <h2 class="syl-card-title">CIE-1 Academic Sources &amp; Faculty Citations</h2>
          <p style="font-size:13px; color:var(--ink-muted); line-height:1.5; margin-bottom:1rem;">
            Every definition, algorithm step, network diagram, automata state, and solved mathematical numerical in the CIE-1 notes is strictly traceable to prescribed textbooks and faculty materials:
          </p>
          <div class="books-grid">
            <div class="book-card">
              <span class="book-tag" style="background:var(--green-tint); color:var(--green-tint-ink);">Primary Scope Authority</span>
              <h4 class="book-title">MSRIT Department Syllabus &amp; CIE-1 Schedule</h4>
              <p class="book-author">Autonomous Scheme (2024 Batch, V Semester ISE)</p>
              <p style="font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem;">Exam Schedule: ${escapeHtml(subject.examSchedule || 'October 2026')}</p>
            </div>
            <div class="book-card">
              <span class="book-tag">Faculty Source Citations</span>
              <h4 class="book-title">Department Faculty Lecture Decks &amp; Question Papers</h4>
              <p class="book-author">Course Coordinator: ${escapeHtml(subject.coordinator || 'Department Faculty')}</p>
              <p style="font-size:0.75rem; color:var(--text-muted); margin-top:0.25rem;">Classroom slides, problem sheets, and authenticated examination papers</p>
            </div>
          </div>
        </div>

        <!-- Course Outcomes (if provided) -->
        ${syl.courseOutcomes ? `
          <div class="syllabus-section-card">
            <h2 class="syl-card-title">Course Outcomes (COs)</h2>
            <div class="table-responsive">
              <table class="custom-table">
                <thead>
                  <tr>
                    <th style="width: 80px;">CO</th>
                    <th>Outcome Statement</th>
                    <th style="width: 220px;">Programme Articulation</th>
                  </tr>
                </thead>
                <tbody>
                  ${syl.courseOutcomes.map(c => `
                    <tr>
                      <td><strong class="code-mono">${escapeHtml(c.co)}</strong></td>
                      <td>${escapeHtml(c.text)}</td>
                      <td><span style="font-family:var(--font-mono);font-size:0.78rem;">${escapeHtml(c.mapping)}</span></td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        ` : ''}

        <!-- Evaluation Scheme (if provided) -->
        ${syl.evaluationScheme ? `
          <div class="syllabus-section-card">
            <h2 class="syl-card-title">CIE & SEE Evaluation Scheme</h2>
            <div class="table-responsive">
              <table class="custom-table">
                <thead>
                  <tr>
                    <th>Assessment Component</th>
                    <th>Max Marks</th>
                    <th>Attained COs / Guidelines</th>
                  </tr>
                </thead>
                <tbody>
                  ${syl.evaluationScheme.details.map(d => `
                    <tr>
                      <td><strong>${escapeHtml(d.component)}</strong></td>
                      <td><span style="font-family:var(--font-mono);">${d.marks}</span></td>
                      <td>${d.cos ? `<span style="font-family:var(--font-mono);">${escapeHtml(d.cos)}</span>` : escapeHtml(d.note || '-')}</td>
                    </tr>
                  `).join('')}
                </tbody>
              </table>
            </div>
          </div>
        ` : ''}

        ${(() => {
          const sylUnit = subject.units.find(u => u.unitNumber === 'Syllabus');
          if (!sylUnit || !sylUnit.files || sylUnit.files.length === 0) return '';
          return `
            <div class="syllabus-section-card" style="margin-top:1.25rem;">
              <h2 class="syl-card-title">Official Syllabus &amp; Curriculum Documents</h2>
              <div class="files-list" style="margin-top:0.75rem;">
                ${sylUnit.files.map(f => renderFileRow(f, subject)).join('')}
              </div>
            </div>
          `;
        })()}
      </div>
    `;
  }

  // --- Render Laboratory Programs View ---
  function renderLabView(subject) {
    const lab = subject.lab;
    if (!lab) return '';

    return `
      <div class="lab-container">
        <div class="notice-card" style="margin-bottom: 1.25rem;">
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
            <span class="pill-tag-amber" style="font-size:11px;padding:2px 8px;background:rgba(245,158,11,0.15);color:#d97706;border:1px solid rgba(245,158,11,0.3);border-radius:999px;">Syllabus only</span>
            <h4 class="notice-title" style="margin:0;">Laboratory Curriculum &amp; Experiment Specifications</h4>
          </div>
          <p class="notice-text">Official laboratory syllabus, experiment list, and rubrics. Laboratory code solutions, manual write-ups, and viva notes are not published; verify with your course faculty.</p>
        </div>

        <div class="lab-info-banner">
          <div class="subject-view-meta-bar" style="margin-bottom: 0;">
            <span class="subject-code-tag">
              ${escapeHtml(lab.code)}
            </span>
            <span class="meta-text-item">Credits: ${escapeHtml(lab.credits)}</span>
            ${lab.contactHours ? `<span class="meta-text-item">${escapeHtml(lab.contactHours)}</span>` : ''}
            ${lab.coordinator ? `<span class="meta-text-item">Coord: ${escapeHtml(lab.coordinator)}</span>` : ''}
            ${lab.prerequisites ? `<span class="meta-text-item">Prereq: ${escapeHtml(lab.prerequisites)}</span>` : ''}
          </div>
          <h2 style="font-size:1.4rem;font-weight:700;color:var(--text-primary);">${escapeHtml(lab.title)}</h2>
          <p style="font-size:0.92rem;color:var(--text-secondary);">${escapeHtml(lab.description)}</p>
        </div>

        ${(() => {
          const labUnit = subject.units.find(u => u.unitNumber === 'Lab');
          if (!labUnit || !labUnit.files || labUnit.files.length === 0) return '';
          return `
            <div class="syllabus-section-card" style="margin-bottom:1.5rem;">
              <h3 class="syl-card-title" style="margin-bottom:0.75rem;">Laboratory Manuals, Programs &amp; Notebooks</h3>
              <div class="files-list">
                ${labUnit.files.map(f => renderFileRow(f, subject)).join('')}
              </div>
            </div>
          `;
        })()}

        ${lab.partA && lab.partA.length > 0 ? `
          <div class="lab-part-section">
            <div class="lab-part-header">
              <h3 class="lab-part-title">
                <span class="rule-type-badge">PART A</span>
                <span>${subject.id === 'ml' ? 'Tableau Data Visualization Dashboards' : (subject.id === 'cn' ? 'Network Protocol Implementation Programs' : 'Part A Experiments')}</span>
              </h3>
            </div>
            <div class="lab-programs-grid">
              ${lab.partA.map(prog => `
                <div class="lab-program-card">
                  <div class="lab-program-head">
                    <span class="lab-prog-num">#${prog.slNo}</span>
                    <h4 class="lab-prog-title">${escapeHtml(prog.title)}</h4>
                  </div>
                  ${prog.description ? `<p class="lab-prog-desc">${escapeHtml(prog.description)}</p>` : ''}
                  ${prog.tasks && prog.tasks.length > 0 ? `
                    <ul class="rule-bullet-list" style="margin-top:0.5rem;">
                      ${prog.tasks.map(t => `<li>${escapeHtml(t)}</li>`).join('')}
                    </ul>
                  ` : ''}
                  ${prog.dataset ? `
                    <div style="margin-top:0.75rem;">
                      <a href="${prog.dataset}" target="_blank" rel="noopener noreferrer" class="lab-prog-dataset">
                        ${ICONS.externalLink} <span>Dataset: ${escapeHtml(prog.dataset)}</span>
                      </a>
                    </div>
                  ` : ''}
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        ${lab.partB && lab.partB.length > 0 ? `
          <div class="lab-part-section">
            <div class="lab-part-header">
              <h3 class="lab-part-title">
                <span class="rule-type-badge">PART B</span>
                <span>${subject.id === 'ml' ? 'Machine Learning Python Implementations' : (subject.id === 'cn' ? 'NS-2 Network Topology Simulations' : 'Part B Experiments')}</span>
              </h3>
            </div>
            <div class="lab-programs-grid">
              ${lab.partB.map(prog => `
                <div class="lab-program-card">
                  <div class="lab-program-head">
                    <span class="lab-prog-num">#${prog.slNo}</span>
                    <h4 class="lab-prog-title">${escapeHtml(prog.title)}</h4>
                  </div>
                  ${prog.description ? `<p class="lab-prog-desc">${escapeHtml(prog.description)}</p>` : ''}
                  ${prog.tasks && prog.tasks.length > 0 ? `
                    <ul class="rule-bullet-list" style="margin-top:0.5rem;">
                      ${prog.tasks.map(t => `<li>${escapeHtml(t)}</li>`).join('')}
                    </ul>
                  ` : ''}
                  ${prog.dataset ? `
                    <div style="margin-top:0.75rem;">
                      <a href="${prog.dataset}" target="_blank" rel="noopener noreferrer" class="lab-prog-dataset">
                        ${ICONS.externalLink} <span>Dataset: ${escapeHtml(prog.dataset)}</span>
                      </a>
                    </div>
                  ` : ''}
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}

        ${lab.exercises && lab.exercises.length > 0 ? `
          <div class="lab-part-section">
            <div class="lab-part-header">
              <h3 class="lab-part-title">
                <span class="rule-type-badge">UNIT-WISE EXERCISES</span>
                <span>Integrated IPCC Laboratory Practicals</span>
              </h3>
            </div>
            <div class="lab-programs-grid">
              ${lab.exercises.map(ex => `
                <div class="lab-program-card">
                  <div class="lab-program-head">
                    <span class="lab-prog-num">${escapeHtml(ex.unit)}</span>
                    <h4 class="lab-prog-title">${escapeHtml(ex.title)}</h4>
                  </div>
                  ${ex.tasks && ex.tasks.length > 0 ? `
                    <ul class="rule-bullet-list" style="margin-top:0.5rem;">
                      ${ex.tasks.map(t => `<li>${escapeHtml(t)}</li>`).join('')}
                    </ul>
                  ` : ''}
                </div>
              `).join('')}
            </div>
          </div>
        ` : ''}
      </div>
    `;
  }

  // --- Render V Semester Scheme & Evaluation View ---
  function renderSchemeView() {
    if (!elements.schemeContainer) return;
    const scheme = state.data.scheme;
    if (!scheme) return;

    elements.schemeContainer.innerHTML = `
      <div class="scheme-hero-header">
        <div class="back-btn-row">
          <button class="back-btn" onclick="window.SEM5_APP.closeSchemeView()">
            ${ICONS.arrowLeft} <span>Back to Home</span>
          </button>
          <button class="btn-secondary" onclick="window.print()" title="Print Scheme & Guidelines">
            ${ICONS.printer} <span>Print Scheme</span>
          </button>
        </div>

        <p class="section-subtitle" style="margin-top: 1rem;">
          Official Autonomous Syllabus Scheme · ${escapeHtml(scheme.degree)}
        </p>

        <h1 class="subject-view-title" style="margin-top: 0.5rem;">${escapeHtml(scheme.title)}</h1>
        <p class="subject-view-desc">
          Complete structure of 5th semester courses, teaching department allocations, lecture-tutorial-practical-self study (L:T:P:S) credit breakdown, and examination evaluation regulations.
        </p>

        <div class="scheme-meta-summary">
          <div class="scheme-summary-item">
            <span class="meta-label">Total Scheme Credits:</span>
            <span class="meta-val">${scheme.totalCredits} Credits</span>
          </div>
          <div class="scheme-summary-item">
            <span class="meta-label">Total Contact Hours/Week:</span>
            <span class="meta-val">${scheme.totalContactHoursPerWeek} Hours</span>
          </div>
          <div class="scheme-summary-item">
            <span class="meta-label">Credit Split (L:T:P):</span>
            <span class="meta-val">${scheme.creditBreakdown.L} : ${scheme.creditBreakdown.T} : ${scheme.creditBreakdown.P}</span>
          </div>
          <div class="scheme-summary-item">
            <span class="meta-label">Self-Study Hours:</span>
            <span class="meta-val">${scheme.creditBreakdown.S} Hours</span>
          </div>
        </div>
      </div>

      <!-- Semester V Scheme Table -->
      <div class="scheme-section-card">
        <h2 class="scheme-section-title">
          <span>V Semester Teaching Scheme &amp; Course Matrix</span>
        </h2>
        <p class="scheme-section-subtitle">
          Prescribed autonomous credit scheme for Information Science &amp; Engineering 2024 Batch.
        </p>

        <div class="table-responsive">
          <table class="custom-table">
            <thead>
              <tr>
                <th style="width: 50px;">Sl</th>
                <th style="width: 90px;">Course Code</th>
                <th>Course Title</th>
                <th style="width: 70px;">Dept</th>
                <th style="width: 80px;">Category</th>
                <th style="width: 70px;">L:T:P</th>
                <th style="width: 80px;">Credits</th>
                <th style="width: 110px;">Contact Hrs</th>
                <th>Course Coordinator</th>
              </tr>
            </thead>
            <tbody>
              ${scheme.courses.map(c => `
                <tr>
                  <td><span class="code-mono">${c.slNo}</span></td>
                  <td><strong class="code-mono">${escapeHtml(c.code)}</strong></td>
                  <td><strong>${escapeHtml(c.name)}</strong></td>
                  <td><span>${escapeHtml(c.dept)}</span></td>
                  <td><span class="category-tag">${escapeHtml(c.category)}</span></td>
                  <td><span class="code-mono">${escapeHtml(c.credits)}</span></td>
                  <td><strong class="code-mono">${c.totalCredits}</strong></td>
                  <td><span class="code-mono">${escapeHtml(c.contactHours)}</span></td>
                  <td><span>${escapeHtml(c.coordinator)}</span></td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>

      <!-- CIE & SEE Evaluation Regulations -->
      <div class="scheme-section-card">
        <h2 class="scheme-section-title">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
          <span>Continuous Internal Evaluation (CIE) &amp; SEE Guidelines</span>
        </h2>
        <p class="scheme-section-subtitle">
          Official evaluation schemes for Integrated Courses (IPCC), Professional Core &amp; Electives (PCC/PEC/HSMC), Ability Enhancement Courses (AEC), Laboratory Courses, and NCMC courses.
        </p>

        <div class="rules-grid">
          ${scheme.evaluationRules.map(rule => `
            <div class="rule-card">
              <div class="rule-card-header">
                <span class="rule-type-badge">${escapeHtml(rule.category)}</span>
              </div>
              <h3 class="rule-card-title">${escapeHtml(rule.title)}</h3>
              <ul class="rule-bullet-list" style="margin-top:0.85rem;">
                ${rule.points.map(pt => `<li>${escapeHtml(pt)}</li>`).join('')}
              </ul>
            </div>
          `).join('')}
        </div>
      </div>
    `;
  }

  // --- PDF Viewer Modal Controller ---
  function openViewer(fileId) {
    let targetFile = null;
    let targetSubject = null;

    for (const sub of state.data.subjects) {
      for (const unit of sub.units) {
        const found = unit.files.find(f => f.id === fileId);
        if (found) {
          targetFile = found;
          targetSubject = sub;
          break;
        }
      }
      if (targetFile) break;
    }

    if (!targetFile) return;

    // Interactive HTML notes open directly in the same tab with back link
    if (targetFile.type === 'notes' || (targetFile.path && targetFile.path.endsWith('.html'))) {
      window.location.href = targetFile.path;
      return;
    }

    // Responsive Mobile check: on mobile screens, opening in native browser viewer
    const isMobile = window.innerWidth < 768;
    if (isMobile) {
      window.open(targetFile.path, '_blank');
      return;
    }

    // Desktop: Modal Viewer
    elements.viewerTitle.textContent = `${targetSubject.shortName}: ${targetFile.title}`;
    elements.viewerDownloadBtn.href = targetFile.path;
    elements.viewerNewTabBtn.href = targetFile.path;

    if (targetFile.type === 'png' || targetFile.type === 'jpg') {
      elements.viewerIframe.style.display = 'none';
      elements.viewerImageWrap.style.display = 'flex';
      elements.viewerImage.src = targetFile.path;
    } else {
      elements.viewerImageWrap.style.display = 'none';
      elements.viewerIframe.style.display = 'block';
      // Lazy-load iframe source
      elements.viewerIframe.src = targetFile.path;
    }

    elements.viewerModal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeViewer() {
    elements.viewerModal.classList.remove('open');
    // Clear iframe src to release memory
    elements.viewerIframe.src = 'about:blank';
    elements.viewerImage.src = '';
    document.body.style.overflow = '';
  }

  // --- Global Search Functionality ---
  function openSearch() {
    elements.searchModal.classList.add('open');
    document.body.style.overflow = 'hidden';
    elements.searchInput.value = '';
    elements.searchInput.focus();
    executeSearch('');
  }

  function closeSearch() {
    elements.searchModal.classList.remove('open');
    document.body.style.overflow = '';
  }

  function executeSearch(query) {
    state.searchQuery = query.trim().toLowerCase();
    state.selectedSearchIdx = 0;

    if (!state.searchQuery) {
      elements.searchResultsBox.innerHTML = `
        <div class="search-empty-state">
          Type subject names (e.g. <em>AI</em>, <em>TOC</em>, <em>EVS</em>), unit numbers, topics (e.g. <em>Pumping Lemma</em>, <em>Scrum</em>), or filenames to search instantly.
        </div>
      `;
      state.searchResults = [];
      return;
    }

    const results = [];

    // Match Scheme & Evaluation Guidelines
    if (state.data.scheme) {
      const schemeMatch = 'scheme'.includes(state.searchQuery) ||
                          'evaluation'.includes(state.searchQuery) ||
                          'cie'.includes(state.searchQuery) ||
                          'see'.includes(state.searchQuery) ||
                          'credit'.includes(state.searchQuery) ||
                          'credits'.includes(state.searchQuery) ||
                          state.data.scheme.title.toLowerCase().includes(state.searchQuery);
      if (schemeMatch) {
        results.push({
          type: 'scheme',
          title: 'V Semester Scheme of Teaching & Evaluation',
          subtitle: 'Official Autonomous Curriculum · 22 Credits · CIE/SEE Schemes',
          action: () => {
            closeSearch();
            openSchemeView();
          }
        });
      }
    }

    state.data.subjects.forEach(subject => {
      // Match Subject Level
      const subMatch = subject.name.toLowerCase().includes(state.searchQuery) ||
                       subject.shortName.toLowerCase().includes(state.searchQuery) ||
                       subject.code.toLowerCase().includes(state.searchQuery);
      if (subMatch) {
        results.push({
          type: 'subject',
          subjectId: subject.id,
          title: subject.name,
          subtitle: `${subject.code} · ${subject.shortName} · Subject Overview`,
          action: () => {
            closeSearch();
            openSubject(subject.id);
          }
        });
      }

      // Match Laboratory and Lab Programs
      if (subject.lab) {
        const labCodeMatch = subject.lab.code && subject.lab.code.toLowerCase().includes(state.searchQuery);
        const labTitleMatch = subject.lab.title && subject.lab.title.toLowerCase().includes(state.searchQuery);
        if (labCodeMatch || labTitleMatch) {
          results.push({
            type: 'lab',
            subjectId: subject.id,
            title: subject.lab.title,
            subtitle: `${subject.shortName} · Laboratory (${subject.lab.code})`,
            action: () => {
              closeSearch();
              openSubject(subject.id);
              switchTab('lab');
            }
          });
        }

        const labParts = [...(subject.lab.partA || []), ...(subject.lab.partB || [])];
        labParts.forEach(p => {
          const pMatch = p.title.toLowerCase().includes(state.searchQuery) ||
                         (p.description && p.description.toLowerCase().includes(state.searchQuery)) ||
                         (p.tasks && p.tasks.some(t => t.toLowerCase().includes(state.searchQuery)));
          if (pMatch) {
            results.push({
              type: 'lab-prog',
              subjectId: subject.id,
              title: p.title,
              subtitle: `${subject.shortName} Lab Program #${p.slNo}`,
              action: () => {
                closeSearch();
                openSubject(subject.id);
                switchTab('lab');
              }
            });
          }
        });

        if (subject.lab.exercises) {
          subject.lab.exercises.forEach(ex => {
            const exMatch = ex.title.toLowerCase().includes(state.searchQuery) ||
                            (ex.tasks && ex.tasks.some(t => t.toLowerCase().includes(state.searchQuery)));
            if (exMatch) {
              results.push({
                type: 'lab-prog',
                subjectId: subject.id,
                title: ex.title,
                subtitle: `${subject.shortName} Integrated Lab · ${ex.unit}`,
                action: () => {
                  closeSearch();
                  openSubject(subject.id);
                  switchTab('lab');
                }
              });
            }
          });
        }
      }

      // Match Unit Level & Files Level
      subject.units.forEach(unit => {
        const unitMatch = unit.title.toLowerCase().includes(state.searchQuery) ||
                          (unit.topics && unit.topics.toLowerCase().includes(state.searchQuery));
        if (unitMatch) {
          results.push({
            type: 'unit',
            subjectId: subject.id,
            title: unit.title,
            subtitle: `${subject.shortName} · ${unit.isPractice ? 'Practice' : 'Unit'}`,
            action: () => {
              closeSearch();
              openSubject(subject.id);
              switchTab(unit.isPractice ? 'practice' : 'notes');
            }
          });
        }

        // Match Files
        unit.files.forEach(file => {
          const fileMatch = file.title.toLowerCase().includes(state.searchQuery) ||
                            file.originalName.toLowerCase().includes(state.searchQuery) ||
                            (file.tag && file.tag.toLowerCase().includes(state.searchQuery)) ||
                            (file.type && file.type.toLowerCase().includes(state.searchQuery)) ||
                            (state.searchQuery.includes('handwritten') && file.type === 'handwritten');
          if (fileMatch) {
            results.push({
              type: 'file',
              subjectId: subject.id,
              fileId: file.id,
              title: file.title,
              subtitle: `${subject.shortName} · ${unit.title} · ${file.size}`,
              action: () => {
                closeSearch();
                openSubject(subject.id);
                switchTab(unit.isPractice ? 'practice' : 'notes');
                setTimeout(() => {
                  const targetRow = document.getElementById(`file-row-${file.id}`);
                  if (targetRow) {
                    const parentDetails = targetRow.closest('details.unit-pill-card');
                    if (parentDetails) parentDetails.open = true;
                    targetRow.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    targetRow.classList.add('file-row-highlighted');
                    setTimeout(() => targetRow.classList.remove('file-row-highlighted'), 2400);
                  }
                }, 220);
              }
            });
          }
        });
      });

      // Match Syllabus Units (if applicable)
      if (subject.syllabus && subject.syllabus.units) {
        subject.syllabus.units.forEach(sylUnit => {
          if (sylUnit.title.toLowerCase().includes(state.searchQuery) || sylUnit.topics.toLowerCase().includes(state.searchQuery)) {
            results.push({
              type: 'syllabus',
              subjectId: subject.id,
              title: sylUnit.title,
              subtitle: `${subject.shortName} Official Syllabus Topic`,
              action: () => {
                closeSearch();
                openSubject(subject.id);
                switchTab('syllabus');
              }
            });
          }
        });
      }
    });

    // Match Interactive Notes Sections & Key Terms
    if (state.notesIndex && state.notesIndex.length > 0) {
      const q = state.searchQuery;
      let noteSectionMatches = 0;
      state.notesIndex.forEach(entry => {
        if (noteSectionMatches >= 30) return; // Cap notes matches to prevent overwhelming list
        const titleMatch = entry.title && entry.title.toLowerCase().includes(q);
        const subMatch = entry.subsections && entry.subsections.some(s => s.toLowerCase().includes(q));
        const keyMatch = entry.keywords && entry.keywords.some(k => k.toLowerCase().includes(q));
        const unitMatch = entry.unitTitle && entry.unitTitle.toLowerCase().includes(q);
        const subIdMatch = entry.subject && entry.subject.toLowerCase() === q;

        if (titleMatch || subMatch || keyMatch || unitMatch || subIdMatch) {
          const subCode = (entry.subject || 'notes').toUpperCase();
          let badgeText = 'Interactive notes';
          let subtitleText = `${subCode} · Unit ${entry.unit}: ${entry.unitTitle} §${entry.sectionId || ''}`;
          if (entry.type === 'pyq') {
            badgeText = 'Solved PYQ';
            subtitleText = `${subCode} · Unit ${entry.unit} PYQ ${entry.exam ? '· ' + entry.exam : ''} ${entry.marks ? '(' + entry.marks + ')' : ''}`;
          } else if (entry.type === 'handwritten') {
            badgeText = 'PDF Notebook';
            subtitleText = `${subCode} · ${entry.unitTitle} · Handwritten PDF`;
          }
          results.push({
            type: entry.type || 'note-section',
            title: entry.title,
            subtitle: subtitleText,
            badge: badgeText,
            action: () => {
              closeSearch();
              window.location.href = entry.path;
            }
          });
        }
      });
    }

    state.searchResults = results;

    if (results.length === 0) {
      elements.searchResultsBox.innerHTML = `
        <div class="search-empty-state">
          No matches found for "<strong>${escapeHtml(query)}</strong>". Try another keyword.
        </div>
      `;
      return;
    }

    elements.searchResultsBox.innerHTML = results.map((res, index) => `
      <div class="search-result-item ${index === 0 ? 'selected' : ''}" data-idx="${index}" onclick="window.SEM5_APP.triggerSearchResult(${index})">
        <div class="search-res-info">
          <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;">
            <span class="search-res-title">${highlightMatch(res.title, state.searchQuery)}</span>
            ${res.badge ? `<span class="pill-tag-green" style="font-size:10px;padding:1px 6px;">${escapeHtml(res.badge)}</span>` : ''}
          </div>
          <span class="search-res-breadcrumbs">${escapeHtml(res.subtitle)}</span>
        </div>
        <span class="kbd-shortcut">↵ Open</span>
      </div>
    `).join('');
  }

  function triggerSearchResult(index) {
    if (state.searchResults[index] && state.searchResults[index].action) {
      state.searchResults[index].action();
    }
  }

  function highlightMatch(text, query) {
    if (!query) return escapeHtml(text);
    const escapedText = escapeHtml(text);
    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    return escapedText.replace(regex, '<mark class="search-highlight">$1</mark>');
  }

  // --- Event Listeners Setup ---
  function setupEventListeners() {
    // Theme toggles
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', toggleTheme);
    }
    if (elements.drawerThemeToggleBtn) {
      elements.drawerThemeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Mobile Menu Drawer
    if (elements.mobileMenuBtn) {
      elements.mobileMenuBtn.addEventListener('click', openMobileMenu);
    }
    if (elements.closeMobileMenuBtn) {
      elements.closeMobileMenuBtn.addEventListener('click', closeMobileMenu);
    }

    // Header Scroll State
    window.addEventListener('scroll', () => {
      if (elements.siteNav) {
        elements.siteNav.classList.toggle('is-scrolled', window.scrollY > 20);
      }
    }, { passive: true });

    // Filter Pills
    if (elements.filterPills) {
      elements.filterPills.forEach(btn => {
        btn.addEventListener('click', () => {
          elements.filterPills.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          state.activeFilter = btn.dataset.filter || 'all';
          renderSubjectsGrid();
        });
      });
    }

    // Search Triggers
    if (elements.searchTriggerBtns) {
      elements.searchTriggerBtns.forEach(btn => {
        btn.addEventListener('click', openSearch);
      });
    }

    if (elements.closeSearchBtn) {
      elements.closeSearchBtn.addEventListener('click', closeSearch);
    }

    // Search Input Typing
    if (elements.searchInput) {
      elements.searchInput.addEventListener('input', (e) => {
        executeSearch(e.target.value);
      });

      elements.searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          selectNextSearchResult(1);
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          selectNextSearchResult(-1);
        } else if (e.key === 'Enter') {
          e.preventDefault();
          triggerSearchResult(state.selectedSearchIdx);
        } else if (e.key === 'Escape') {
          closeSearch();
        }
      });
    }

    // Viewer Close
    if (elements.closeViewerBtn) {
      elements.closeViewerBtn.addEventListener('click', closeViewer);
    }

    // Reset Progress
    if (elements.resetProgressBtn) {
      elements.resetProgressBtn.addEventListener('click', resetAllProgress);
    }

    // Keyboard Shortcuts: '/' or 'Ctrl+K' or 'Cmd+K' for Search, 'Esc' for Modals
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openSearch();
      } else if (e.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        e.preventDefault();
        openSearch();
      } else if (e.key === 'Escape') {
        if (elements.mobileMenuDrawer && elements.mobileMenuDrawer.classList.contains('open')) {
          closeMobileMenu();
        } else if (elements.searchModal.classList.contains('open')) {
          closeSearch();
        } else if (elements.viewerModal.classList.contains('open')) {
          closeViewer();
        }
      }
    });

    // Close Modals on Backdrop Click
    elements.searchModal.addEventListener('click', (e) => {
      if (e.target === elements.searchModal) closeSearch();
    });

    elements.viewerModal.addEventListener('click', (e) => {
      if (e.target === elements.viewerModal) closeViewer();
    });
  }

  function selectNextSearchResult(delta) {
    if (state.searchResults.length === 0) return;
    state.selectedSearchIdx = (state.selectedSearchIdx + delta + state.searchResults.length) % state.searchResults.length;
    
    const items = elements.searchResultsBox.querySelectorAll('.search-result-item');
    items.forEach((item, idx) => {
      item.classList.toggle('selected', idx === state.selectedSearchIdx);
      if (idx === state.selectedSearchIdx) {
        item.scrollIntoView({ block: 'nearest' });
      }
    });
  }

  // --- Utility Functions ---
  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function escapeRegex(str) {
    return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // --- Public API ---
  window.SEM5_APP = {
    init,
    openSubject,
    closeSubjectView,
    openSchemeView,
    closeSchemeView,
    openMobileMenu,
    closeMobileMenu,
    toggleTheme,
    switchTab,
    toggleAllUnits,
    syncToggleAllButton,
    openViewer,
    closeViewer,
    toggleFileProgress,
    togglePinSubject,
    triggerSearchResult
  };

  // Run on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
