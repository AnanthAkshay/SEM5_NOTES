/**
 * SEM 5 · ISE Notes - Core Application Logic
 * Department of Information Science & Engineering
 */

(function () {
  'use strict';

  // --- State & Constants ---
  const STORAGE_KEYS = {
    THEME: 'sem5_theme_v1',
    PROGRESS: 'sem5_progress_v1',
    PINNED: 'sem5_pinned_v1',
    RECENT: 'sem5_recent_v1'
  };

  const state = {
    data: window.SEM5_DATA || { subjects: [], timetable: {}, meta: {} },
    theme: localStorage.getItem(STORAGE_KEYS.THEME) || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'),
    progress: JSON.parse(localStorage.getItem(STORAGE_KEYS.PROGRESS) || '{}'),
    pinned: JSON.parse(localStorage.getItem(STORAGE_KEYS.PINNED) || '[]'),
    recent: JSON.parse(localStorage.getItem(STORAGE_KEYS.RECENT) || '[]'),
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
    themeToggleBtn: document.getElementById('theme-toggle-btn'),
    themeIcon: document.getElementById('theme-icon'),
    heroSection: document.getElementById('hero-section'),
    recentSection: document.getElementById('recent-section'),
    recentList: document.getElementById('recent-list'),
    subjectsGrid: document.getElementById('subjects-grid'),
    filterBtns: document.querySelectorAll('.filter-btn'),
    homeView: document.getElementById('home-view'),
    subjectView: document.getElementById('subject-view'),
    subjectContainer: document.getElementById('subject-container'),
    totalFilesCount: document.getElementById('total-files-count'),
    completedFilesCount: document.getElementById('completed-files-count'),
    overallProgressBar: document.getElementById('overall-progress-bar'),
    overallProgressPct: document.getElementById('overall-progress-pct'),
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
    timetableGrid: document.getElementById('timetable-grid'),
    resetProgressBtn: document.getElementById('reset-progress-btn'),
    currentYearSpan: document.getElementById('current-year-span'),
    lastUpdatedSpan: document.getElementById('last-updated-span')
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
    renderHeroStats();
    renderRecentlyOpened();
    renderSubjectsGrid();
    renderTimetables();
    
    // Update dates
    if (elements.lastUpdatedSpan) {
      elements.lastUpdatedSpan.textContent = state.data.meta?.lastUpdated || 'October 2026';
    }
    if (elements.currentYearSpan) {
      elements.currentYearSpan.textContent = new Date().getFullYear();
    }
  }

  // --- Theme Management ---
  function applyTheme(theme) {
    state.theme = theme;
    elements.html.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEYS.THEME, theme);
    if (elements.themeIcon) {
      elements.themeIcon.innerHTML = theme === 'dark' ? ICONS.sun : ICONS.moon;
      elements.themeToggleBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
    }
  }

  function toggleTheme() {
    applyTheme(state.theme === 'dark' ? 'light' : 'dark');
  }

  // --- Routing & Navigation ---
  function setupRouting() {
    window.addEventListener('hashchange', handleHashChange);
    handleHashChange();
  }

  function handleHashChange() {
    const hash = window.location.hash.slice(1);
    if (hash.startsWith('subject-')) {
      const subjectId = hash.replace('subject-', '');
      openSubject(subjectId, false);
    } else {
      closeSubjectView(false);
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
      window.location.hash = `subject-${subjectId}`;
    }

    renderSubjectDetail(subject);
    elements.homeView.classList.remove('active');
    elements.subjectView.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function closeSubjectView(pushHistory = true) {
    state.currentSubjectId = null;
    if (pushHistory) {
      window.location.hash = '';
    }
    elements.subjectView.classList.remove('active');
    elements.homeView.classList.add('active');
    renderSubjectsGrid();
    renderHeroStats();
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

  function getGlobalProgress() {
    let total = 0;
    let completed = 0;
    state.data.subjects.forEach(s => {
      s.units.forEach(u => {
        u.files.forEach(f => {
          total++;
          if (state.progress[f.id]) {
            completed++;
          }
        });
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
    renderHeroStats();
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
      renderHeroStats();
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
    if (e) e.stopPropagation();
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

  // --- Recently Opened Tracking ---
  function trackOpenedFile(file, subject) {
    const item = {
      fileId: file.id,
      title: file.title,
      path: file.path,
      subjectId: subject.id,
      subjectShort: subject.shortName,
      type: file.type,
      timestamp: Date.now()
    };
    state.recent = [item, ...state.recent.filter(r => r.fileId !== file.id)].slice(0, 4);
    localStorage.setItem(STORAGE_KEYS.RECENT, JSON.stringify(state.recent));
    renderRecentlyOpened();
  }

  function renderRecentlyOpened() {
    if (!elements.recentSection || !elements.recentList) return;
    if (state.recent.length === 0) {
      elements.recentSection.style.display = 'none';
      return;
    }
    elements.recentSection.style.display = 'block';
    elements.recentList.innerHTML = state.recent.map(r => `
      <a href="#subject-${r.subjectId}" class="recent-pill" data-file-id="${r.fileId}" title="Jump to ${escapeHtml(r.title)}">
        <span class="file-type-icon ${r.type}" style="width:20px;height:20px;font-size:0.6rem;">${r.type.toUpperCase()}</span>
        <strong style="color:var(--text-primary);">${escapeHtml(r.subjectShort)}</strong>: ${escapeHtml(r.title.slice(0, 30))}${r.title.length > 30 ? '...' : ''}
      </a>
    `).join('');
  }

  // --- Hero Section Stats ---
  function renderHeroStats() {
    const stats = getGlobalProgress();
    if (elements.totalFilesCount) elements.totalFilesCount.textContent = stats.total;
    if (elements.completedFilesCount) elements.completedFilesCount.textContent = stats.completed;
    if (elements.overallProgressBar) elements.overallProgressBar.style.width = `${stats.pct}%`;
    if (elements.overallProgressPct) elements.overallProgressPct.textContent = `${stats.pct}%`;
  }

  // --- Render Subjects Grid ---
  function renderSubjectsGrid() {
    if (!elements.subjectsGrid) return;

    // Filter & Sort subjects: Pinned first, then by configured order
    let list = [...state.data.subjects];
    if (state.activeFilter === 'core') {
      list = list.filter(s => s.tags && s.tags.some(t => t.toLowerCase().includes('core')));
    } else if (state.activeFilter === 'elective') {
      list = list.filter(s => s.tags && s.tags.some(t => t.toLowerCase().includes('elective')));
    } else if (state.activeFilter === 'practice') {
      list = list.filter(s => s.units.some(u => u.isPractice));
    }

    list.sort((a, b) => {
      const aPinned = state.pinned.includes(a.id);
      const bPinned = state.pinned.includes(b.id);
      if (aPinned && !bPinned) return -1;
      if (!aPinned && bPinned) return 1;
      return 0;
    });

    elements.subjectsGrid.innerHTML = list.map(subject => {
      const isPinned = state.pinned.includes(subject.id);
      const fileCount = getSubjectFileCount(subject);
      const progress = getSubjectProgress(subject);
      const unitCount = subject.units.filter(u => !u.isPractice).length;
      const hasPractice = subject.units.some(u => u.isPractice);

      return `
        <div class="subject-card" style="--card-accent: ${subject.accent.primary};" onclick="window.SEM5_APP.openSubject('${subject.id}')">
          <div class="card-top-row">
            <div class="card-badge-group">
              <span class="code-badge">${escapeHtml(subject.code)}</span>
              ${subject.status === 'full_notes' 
                ? `<span class="status-badge full">Full Notes</span>`
                : `<span class="status-badge syllabus">Syllabus & Info</span>`
              }
              ${hasPractice ? `<span class="status-badge full" style="background:var(--status-warning-bg);color:var(--status-warning);border-color:rgba(245,158,11,0.3)">Practice Ready</span>` : ''}
            </div>
            <button class="pin-btn ${isPinned ? 'pinned' : ''}" onclick="window.SEM5_APP.togglePinSubject('${subject.id}', event)" title="${isPinned ? 'Unpin' : 'Pin subject to top'}">
              ${isPinned ? ICONS.pinnedFilled : ICONS.pin}
            </button>
          </div>

          <h3 class="card-title">${escapeHtml(subject.name)}</h3>
          <p class="card-desc">${escapeHtml(subject.description)}</p>

          <div class="card-meta-list">
            <div class="meta-row">
              <span class="meta-label">Credits / Hours:</span>
              <span class="meta-val">${escapeHtml(subject.credits || 'Pending')} ${subject.contactHours ? `· ${escapeHtml(subject.contactHours)}` : ''}</span>
            </div>
            ${subject.coordinator ? `
              <div class="meta-row">
                <span class="meta-label">Coordinator:</span>
                <span class="meta-val">${escapeHtml(subject.coordinator)}</span>
              </div>
            ` : ''}
            <div class="meta-row">
              <span class="meta-label">Coverage:</span>
              <span class="meta-val">${unitCount} Units · ${fileCount} Files</span>
            </div>
          </div>

          <div class="card-progress-wrap">
            <div class="progress-header" style="margin-bottom: 0.35rem;">
              <span style="color:var(--text-muted);font-size:0.75rem;">Study Progress</span>
              <span style="font-weight:600;font-size:0.75rem;color:var(--text-primary);">${progress.completed} / ${progress.total} (${progress.pct}%)</span>
            </div>
            <div class="card-progress-bar">
              <div class="card-progress-fill" style="width: ${progress.pct}%;"></div>
            </div>
          </div>
        </div>
      `;
    }).join('');
  }

  // --- Render Subject Detail View ---
  function renderSubjectDetail(subject) {
    if (!elements.subjectContainer) return;

    const isPinned = state.pinned.includes(subject.id);
    const progress = getSubjectProgress(subject);
    const hasRichSyllabus = !!subject.syllabus;
    const hasPractice = subject.units.some(u => u.isPractice);

    // Default tab logic
    if (state.currentTab === 'syllabus' && !hasRichSyllabus) {
      state.currentTab = 'notes';
    } else if (state.currentTab === 'practice' && !hasPractice) {
      state.currentTab = 'notes';
    }

    elements.subjectContainer.innerHTML = `
      <div class="subject-view-header" style="--subject-glow: ${subject.accent.glow};">
        <div class="back-btn-row">
          <button class="back-btn" onclick="window.SEM5_APP.closeSubjectView()">
            ${ICONS.arrowLeft} <span>Back to All Subjects</span>
          </button>
          <div class="subject-action-row">
            <button id="subject-header-pin-btn" class="btn-secondary ${isPinned ? 'pinned' : ''}" onclick="window.SEM5_APP.togglePinSubject('${subject.id}', event)">
              ${isPinned ? ICONS.pinnedFilled : ICONS.pin} <span>${isPinned ? 'Pinned Subject' : 'Pin Subject'}</span>
            </button>
            ${hasRichSyllabus ? `
              <button class="btn-secondary" onclick="window.print()" title="Print Syllabus">
                ${ICONS.printer} <span>Print Syllabus</span>
              </button>
            ` : ''}
          </div>
        </div>

        <div class="subject-view-meta-bar">
          <span class="meta-pill-tag" style="color:${subject.accent.primary};border-color:${subject.accent.primary};font-weight:700;">
            ${escapeHtml(subject.code)}
          </span>
          <span class="meta-pill-tag">
            Credits: ${escapeHtml(subject.credits || 'TBD')}
          </span>
          ${subject.contactHours ? `<span class="meta-pill-tag">${escapeHtml(subject.contactHours)}</span>` : ''}
          ${subject.coordinator ? `<span class="meta-pill-tag">Coord: ${escapeHtml(subject.coordinator)}</span>` : ''}
          ${subject.prerequisites ? `<span class="meta-pill-tag">Prereq: ${escapeHtml(subject.prerequisites)}</span>` : ''}
        </div>

        <h1 class="subject-view-title">${escapeHtml(subject.name)}</h1>
        <p class="subject-view-desc">${escapeHtml(subject.description)}</p>

        <div class="overall-progress-box" style="max-width: 380px;">
          <div class="progress-header">
            <span style="color:var(--text-muted);">Subject Study Progress</span>
            <span id="subject-progress-text" style="font-weight:700;color:var(--text-primary);">${progress.completed} of ${progress.total} items completed (${progress.pct}%)</span>
          </div>
          <div class="progress-track">
            <div id="subject-progress-fill" class="progress-fill" style="width: ${progress.pct}%; background: ${subject.accent.primary};"></div>
          </div>
        </div>
      </div>

      <!-- Notice card for Subjects without full unit notes yet -->
      ${subject.notesNotice ? `
        <div class="notice-card">
          <div class="notice-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          </div>
          <div class="notice-content">
            <h4 class="notice-title">Notes Status: In Preparation</h4>
            <p class="notice-text">${escapeHtml(subject.notesNotice)}</p>
          </div>
        </div>
      ` : ''}

      <!-- Subject Tabs -->
      <div class="subject-tabs-nav">
        <button class="subject-tab-btn ${state.currentTab === 'notes' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('notes')">
          Unit Notes & Documents (${subject.units.filter(u => !u.isPractice).reduce((acc, u) => acc + u.files.length, 0)})
        </button>
        ${hasPractice ? `
          <button class="subject-tab-btn ${state.currentTab === 'practice' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('practice')">
            Practice & Question Banks (${subject.units.filter(u => u.isPractice).reduce((acc, u) => acc + u.files.length, 0)})
          </button>
        ` : ''}
        ${hasRichSyllabus ? `
          <button class="subject-tab-btn ${state.currentTab === 'syllabus' ? 'active' : ''}" onclick="window.SEM5_APP.switchTab('syllabus')">
            Official Syllabus & Pedagogy
          </button>
        ` : ''}
      </div>

      <!-- Tab Content: Notes or Practice -->
      ${state.currentTab === 'notes' || state.currentTab === 'practice' ? `
        <div class="units-stack">
          ${renderUnitsList(subject, state.currentTab === 'practice')}
        </div>
      ` : ''}

      <!-- Tab Content: Rich Syllabus View -->
      ${state.currentTab === 'syllabus' && hasRichSyllabus ? renderSyllabusView(subject) : ''}
    `;
  }

  function updateSubjectProgressUI(subject) {
    const progress = getSubjectProgress(subject);
    const textEl = document.getElementById('subject-progress-text');
    const fillEl = document.getElementById('subject-progress-fill');
    if (textEl) textEl.textContent = `${progress.completed} of ${progress.total} items completed (${progress.pct}%)`;
    if (fillEl) fillEl.style.width = `${progress.pct}%`;
  }

  function switchTab(tabName) {
    state.currentTab = tabName;
    const subject = state.data.subjects.find(s => s.id === state.currentSubjectId);
    if (subject) {
      renderSubjectDetail(subject);
    }
  }

  // --- Render Units & Files List ---
  function renderUnitsList(subject, isPracticeOnly = false) {
    const units = subject.units.filter(u => isPracticeOnly ? u.isPractice : !u.isPractice);

    if (units.length === 0) {
      return `
        <div class="notice-card">
          <p class="notice-text">No documents in this category yet. Check back soon!</p>
        </div>
      `;
    }

    return units.map(unit => {
      return `
        <div class="unit-card">
          <div class="unit-card-header">
            <div class="unit-header-info">
              <span class="unit-badge ${unit.isPractice ? 'practice' : ''}">
                ${unit.isPractice ? 'Practice' : (typeof unit.unitNumber === 'number' ? `Unit ${unit.unitNumber}` : unit.unitNumber)}
              </span>
              <h3 class="unit-title-text">${escapeHtml(unit.title)}</h3>
            </div>
            <span style="font-size:0.75rem;font-family:var(--font-mono);color:var(--text-muted);">
              ${unit.files.length} ${unit.files.length === 1 ? 'file' : 'files'}
            </span>
          </div>

          ${unit.topics ? `
            <div class="unit-topics-snippet">
              <strong>Key Coverage:</strong> ${escapeHtml(unit.topics)}
            </div>
          ` : ''}

          <div class="files-list">
            ${unit.files.map(file => renderFileRow(file, subject)).join('')}
          </div>
        </div>
      `;
    }).join('');
  }

  function renderFileRow(file, subject) {
    const isDone = !!state.progress[file.id];

    return `
      <div class="file-row" id="file-row-${file.id}">
        <div class="file-info-group">
          <label class="done-checkbox-wrap" title="Mark as studied">
            <input type="checkbox" class="done-checkbox" ${isDone ? 'checked' : ''} onchange="window.SEM5_APP.toggleFileProgress('${file.id}')" />
          </label>

          <span class="file-type-icon ${file.type}">${file.type.toUpperCase()}</span>

          <div class="file-details-col">
            <div class="file-title-wrap">
              <span class="file-title">${escapeHtml(file.title)}</span>
              ${file.isAlternate ? `<span class="pill-alt-notes">Alternate / Condensed</span>` : ''}
              ${file.isConverted ? `<span style="font-size:0.7rem;color:var(--text-muted);font-family:var(--font-mono);">(Converted for browser viewing)</span>` : ''}
            </div>
            <div class="file-submeta">
              <span>${file.size}</span>
              <span>•</span>
              <span title="Original file name">${escapeHtml(file.originalName)}</span>
            </div>
          </div>
        </div>

        <div class="file-actions-group">
          <button class="btn-file-action view-btn" onclick="window.SEM5_APP.openViewer('${file.id}')" title="Read in built-in PDF viewer">
            ${ICONS.eye} <span>View</span>
          </button>
          
          <a href="${file.path}" download class="btn-file-action" title="Download PDF copy">
            ${ICONS.download} <span>PDF</span>
          </a>

          ${file.originalPath ? `
            <a href="${file.originalPath}" download class="btn-file-action" title="Download original format (${file.type.toUpperCase()})">
              ${ICONS.download} <span>Original (${file.originalPath.split('.').pop().toUpperCase()})</span>
            </a>
          ` : ''}
        </div>
      </div>
    `;
  }

  // --- Render Transcribed Syllabus & Books ---
  function renderSyllabusView(subject) {
    const syl = subject.syllabus;
    if (!syl) return '';

    return `
      <div class="syllabus-container">
        <!-- Units Outline -->
        <div class="syllabus-section-card">
          <h2 class="syl-card-title">Detailed Unit Syllabus & NPTEL Video Lectures</h2>
          ${syl.units.map(u => `
            <div class="syl-unit-block">
              <h3 class="syl-unit-heading">${escapeHtml(u.title)}</h3>
              <p class="syl-unit-topics">${escapeHtml(u.topics)}</p>
              ${u.pedagogy ? `<p class="syl-pedagogy"><strong>Pedagogy:</strong> ${escapeHtml(u.pedagogy)}</p>` : ''}
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
          `).join('')}
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
                      <td><strong style="color:var(--brand-primary);">${escapeHtml(c.co)}</strong></td>
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

    // Track recently opened
    trackOpenedFile(targetFile, targetSubject);

    // Responsive Mobile check: on narrow screens, opening in new tab is often cleaner
    const isMobile = window.innerWidth < 768;
    if (isMobile && targetFile.type === 'pdf') {
      // Direct opening in new tab provides native pinch-to-zoom on iOS/Android
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

  // --- Exam Timetable Section ---
  function renderTimetables() {
    if (!elements.timetableGrid) return;
    const tt = state.data.timetable;
    if (!tt || !tt.enabled || !tt.items) {
      const sec = document.getElementById('timetable-section');
      if (sec) sec.style.display = 'none';
      return;
    }

    elements.timetableGrid.innerHTML = tt.items.map(item => `
      <div class="timetable-card">
        <div class="timetable-top">
          <span class="category-tag">${escapeHtml(item.category)}</span>
          <span class="${item.statusBadge === 'Completed' ? 'badge-completed' : 'badge-pending'}">
            ${escapeHtml(item.status)}
          </span>
        </div>
        <h4 class="timetable-title">${escapeHtml(item.title)}</h4>
        <p class="timetable-desc">${escapeHtml(item.description)}</p>
        <div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between;padding-top:1rem;border-top:1px solid var(--border-subtle);font-size:0.8rem;color:var(--text-muted);font-family:var(--font-mono);">
          <span>${escapeHtml(item.dateRange)}</span>
          ${item.pdfUrl ? `
            <a href="${item.pdfUrl}" target="_blank" class="btn-file-action" style="padding:0.3rem 0.65rem;">
              ${ICONS.eye} <span>View Schedule</span>
            </a>
          ` : `
            <span style="font-style:italic;">PDF Pending</span>
          `}
        </div>
      </div>
    `).join('');
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
            }
          });
        }

        // Match Files
        unit.files.forEach(file => {
          const fileMatch = file.title.toLowerCase().includes(state.searchQuery) ||
                            file.originalName.toLowerCase().includes(state.searchQuery);
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
                setTimeout(() => openViewer(file.id), 200);
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
          <span class="search-res-title">${highlightMatch(res.title, state.searchQuery)}</span>
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
    return escapedText.replace(regex, '<mark style="background:rgba(99,102,241,0.3);color:inherit;border-radius:2px;padding:0 2px;">$1</mark>');
  }

  // --- Event Listeners Setup ---
  function setupEventListeners() {
    // Theme toggle
    if (elements.themeToggleBtn) {
      elements.themeToggleBtn.addEventListener('click', toggleTheme);
    }

    // Filter Buttons
    if (elements.filterBtns) {
      elements.filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          elements.filterBtns.forEach(b => b.classList.remove('active'));
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
      } else if (e.key === '/' && document.activeElement.tagName !== 'INPUT') {
        e.preventDefault();
        openSearch();
      } else if (e.key === 'Escape') {
        if (elements.searchModal.classList.contains('open')) {
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
    switchTab,
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
