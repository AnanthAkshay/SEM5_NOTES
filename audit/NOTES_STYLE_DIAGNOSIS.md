# Notes Style Diagnosis Report

## Executive Summary
- **Total Pages Audited:** 24 units across all 8 subjects.
- **Asset Loading (HTTP Status):** 100% PASS (0 asset failures across all 24 pages). CSS, JS, KaTeX CSS/JS/fonts, and images return HTTP 200 with valid MIME types under the `/SEM5_NOTES/` sub-path.
- **Console Errors:** 0 errors across all pages.
- **Root Cause of Visual Breakdown:** **Markup Structure Inconsistency**.
  - 4 pages (**ML Units 1, 2, 3** and **TOC Unit 1**) use the canonical template structure (`.notes-container`, `.notes-sidebar`, `.notes-header-card`, `.notes-headline`, `.notes-section`, `ol.toc-list > li.toc-item > a`).
  - 20 pages (**SE 1-3, CN 1-3, TOC 2-3, AI 1-3, RMIPR 1-3, ReactJS 1-3, EVS 1-3**) use an alternate wrapper markup (`.notes-layout`, `.unit-hero` or `.notes-header`, `.unit-title`, `.note-section` or `.content-section`, `.toc-link` or `.toc-list a`).
  - Because `css/notes.css` was authored against the Group A template tokens, the other 20 pages failed to match layout rules, resulting in unstyled gray sheets, blue underlined links, unconstrained full-width text, oversized H1 headings, unstyled callout boxes, and mobile drawers appearing on desktop.

## Page-by-Page Audit Matrix

| Subject | Unit | HTTP Status | Asset Errors | Container Class | Max Width | TOC Underline | H1 Line Height | Mobile Btn @ 1280px | Status |
|---|---|---|---|---|---|---|---|---|---|
| IS51 | Unit 1 | 200 | 0 | `notes-container` | 1240px | none | 46px | flex | **PASS (Canonical)** |
| IS51 | Unit 2 | 200 | 0 | `notes-container` | 1240px | none | 46px | flex | **PASS (Canonical)** |
| IS51 | Unit 3 | 200 | 0 | `notes-container` | 1240px | none | 46px | flex | **PASS (Canonical)** |
| IS52 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS52 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS52 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS53 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS53 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS53 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS54 | Unit 1 | 200 | 0 | `notes-container` | 1240px | none | 46px | flex | **PASS (Canonical)** |
| IS54 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| IS54 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| ISE552 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| ISE552 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| ISE552 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | block | **BROKEN (Markup Mismatch)** |
| AL58 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| AL58 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| AL58 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| ISAEC594 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| ISAEC594 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| ISAEC594 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| HS510 | Unit 1 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| HS510 | Unit 2 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |
| HS510 | Unit 3 | 200 | 0 | `notes-layout` | none | underline | 54.4px | inline-block | **BROKEN (Markup Mismatch)** |

## Groups & Root Causes

### Group A: Correct Template (4 Pages)
- **Pages:** IS51 Unit 1, IS51 Unit 2, IS51 Unit 3, IS54 Unit 1
- **Markup:** `.notes-container` with grid layout (260px sticky sidebar + 760px main content), `.notes-header-card`, `.notes-headline` with tight line-height, `.notes-section` card containers with 24px padding and rounded borders, `.toc-item a` with no underline and muted ink color.

### Group B: Broken Wrapper Markup (20 Pages)
- **Pages:** IS52 Unit 1, IS52 Unit 2, IS52 Unit 3, IS53 Unit 1, IS53 Unit 2, IS53 Unit 3, IS54 Unit 2, IS54 Unit 3, ISE552 Unit 1, ISE552 Unit 2, ISE552 Unit 3, AL58 Unit 1, AL58 Unit 2, AL58 Unit 3, ISAEC594 Unit 1, ISAEC594 Unit 2, ISAEC594 Unit 3, HS510 Unit 1, HS510 Unit 2, HS510 Unit 3
- **Root Causes:**
  1. **Container class name mismatch:** Uses `div.notes-layout` instead of `div.notes-container`. `notes.css` defines rules for `.notes-container` (max-width: 1200px, margin: 0 auto, display: grid). Hence `.notes-layout` falls back to default `display: block` with 100% width and 0 padding, sitting flush against the left screen edge.
  2. **TOC markup and class mismatch:** Uses `<a class="toc-link">` or `<ol class="toc-list">` instead of `<ol><li class="toc-item"><a ...>`. `notes.css` styles `.toc-item a`. Unmatched links render as browser-default blue underlined text.
  3. **Section card class mismatch:** Uses `.note-section` (singular) or `.content-section` instead of `.notes-section` (plural). `notes.css` styles `.notes-section` with white surface, rounded border, and padding. Unmatched sections render unstyled.
  4. **Header and title mismatch:** Uses `.unit-hero` / `.unit-title` instead of `.notes-header-card` / `.notes-headline`. H1 falls back to default line-height (~1.2 - 1.3) and unformatted font styling.
  5. **Mobile drawer toggle trigger:** In Group B/C, the mobile TOC button (`#mobile-toc-btn` or `.toc-mobile-toggle`) was placed outside or styled with custom classes, lacking media-query hiding (`@media (min-width: 1024px) { display: none; }`). Hence it appears on wide desktop viewports as an unstyled gray bar with a browser default `x` button.

## Remediation Plan
1. **Unified Standardization via Script:** Write `scripts/apply_notes_template.py` to parse every unit's HTML, preserve 100% of the article section content byte-for-byte, and standardize the outer shell (head, sticky topbar, `.notes-container`, sticky `.notes-sidebar`, `.mobile-toc-toggle-wrap`, `.notes-header-card`, footer navigation) into the canonical Hope Rise template.
2. **Defensive, Self-Sufficient CSS:** Update `css/notes.css` to:
   - Ensure all Hope Rise design tokens are self-defined with robust fallbacks.
   - Provide dual-class coverage where appropriate (e.g., both `.notes-section` and `.note-section`, `.toc-link` and `.toc-item a`, `.notes-container` and `.notes-layout`).
   - Set a bulletproof CSS reset.
   - Ensure `.mobile-toc-toggle-wrap` is strictly `display: none` at `>= 1024px` and only visible on mobile `< 1024px`.
   - Provide a styled circular 44px close button for the mobile TOC sheet.
3. **Automated Verification:** Run `scripts/check_notes_style.js` using Playwright across all 24 pages at 1280px, 768px, 390px, and 320px in light and dark modes, verify content hashes match before and after, and generate a contact sheet.
