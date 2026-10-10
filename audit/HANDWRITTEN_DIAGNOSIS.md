# Handwritten Notebook Pipeline - Comprehensive Diagnosis Report

## Executive Summary
All 24 unit handwritten notebooks (`*-handwritten.pdf`) were analyzed across all 8 subjects (AI, CN, EVS, ML, ReactJS, RMIPR, SE, TOC). The audit confirms five major root-cause defect categories:
1. **Font Degradation & Type 3 Embedding**: Headings and titles in earlier builds degraded to Comic Sans due to missing basic Latin (`U+0000-00FF`) unicode ranges. Furthermore, previous Caveat `.woff2` files were Variable Fonts (`fvar`/`gvar` tables); Chromium's Skia PDF engine cannot embed variable fonts as Type 0 CID fonts, converting them to unsearchable Type 3 streams without `BaseFont` descriptors.
2. **Leaked Figure Text & Shrunk Diagrams**: In RMIPR Unit 1 and ReactJS Unit 1, SVG diagrams are restricted to ~50–60% of the column width with tiny illegible labels (~8–10px). In RMIPR, math tokens inside SVG (`$H_0$`) triggered redundant KaTeX text expansion (`H0H_0H0`), leaking through the text layer.
3. **Severe Pagination Defects & Stranded Heading Orphans**: Element-by-element height accumulation without lookahead causes headings (e.g., ReactJS p. 2 "2. The Virtual DOM", TOC p. 2 "Deterministic Finite Automata", RMIPR p. 3 "3. Types of Research") to be stranded at the page bottom. Callouts (e.g., RMIPR p. 2 Quick Recall) are cut off mid-card across the footer.
4. **Ruled-Grid Baseline Drift**: Text baselines float arbitrarily across ruled notebook lines rather than sitting squarely on them, because heading line-heights, card margins, and paddings are not strictly quantized to the `28px` rule spacing.
5. **Web-UI Visual Artifacts**: Rigid 1px rectangular CSS borders, desktop pill badges, and mechanical table layouts detract from the authentic student notebook aesthetic.

---

## Detailed Evidence & Root Cause Analysis

### 1. Font Degradation & Variable Font Skia Incompatibility
- **Evidence**:
  - `pypdf` extraction on earlier generated PDFs revealed empty `BaseFont` entries for heading fonts, and `pdffonts` showed Type 3 font definitions rather than true Type 0 CID TrueType fonts.
  - Basic Latin glyphs in older font packages were omitted due to comment-splitting issues in font downloaders.
  - Inspection of `fonts/caveat-400-latin.woff2` and `fonts/caveat-700-latin.woff2` with `fontTools` revealed variable font tables (`fvar`, `gvar`). When Skia encounters variable TrueType fonts during PDF printing, it falls back to Type 3 glyph streams or system fallbacks.
- **Root Cause & Fix**:
  - Download and bundle clean, static (non-variable) WOFF2 fonts from `@fontsource` for Caveat (400, 700), Patrick Hand (400), Kalam (400, 700), and JetBrains Mono (400, 700).
  - Verify with `fontTools` that `fvar` is absent and full Latin glyph coverage (A-Z, a-z, 0-9, common punctuation/math) is present.
  - Rebuilding `fonts/fonts.css` with comprehensive `unicode-range` rules and verified static fonts results in clean Type 0 CID embedding: `/AAAAAA+Caveat-Bold`, `/BAAAAA+PatrickHand-Regular`, `/CAAAAA+Kalam-Regular`, `/DAAAAA+JetBrainsMono-Regular`.

### 2. Leaked Figure Text & Diagram Scaling
- **Evidence**:
  - In `notes/rmipr/unit1/handwritten/rmipr-unit1-handwritten.pdf` page 2, Figure 1.1 displays `Formulate H0H_0H0 & H1H_1H1` and `Accept or Reject H0H_0H0`.
  - In `notes/reactjs/unit1/handwritten/reactjs-unit1-handwritten.pdf` page 2, SVG flowchart boxes have miniature text.
- **Root Cause & Fix**:
  - The source HTML contains raw math strings `$H_0$` inside `<text>` tags of SVGs. When KaTeX processed the container, it injected multiple hidden DOM/MathML spans into the SVG text stream.
  - SVGs lacked explicit full-column width scaling rules in `css/handwritten.css`, causing diagrams to render at narrow fixed pixel widths.
  - Fix: Pre-sanitize SVG text nodes to convert LaTeX math ($H_0$, $H_1$, $\theta$, $\epsilon$) to clean Unicode characters (H₀, H₁, θ, ϵ) and ensure KaTeX strictly ignores `<svg>`. Set SVG width to 100% of text column, with font sizes scaled to >= 12–13px equivalent.

### 3. Pagination & Stranded Headings (Orphans)
- **Evidence**:
  - Visual contact sheet confirms multiple pages ending in stranded H2/H3 titles with their explanatory text pushed to the subsequent page.
  - Page 2 of RMIPR ends with a sliced `Quick Recall:` card whose bottom lines collide with the footer rule.
- **Root Cause & Fix**:
  - The greedy height accumulator pushed headings whenever `currentHeight + h_height <= MAX_PAGE_HEIGHT_PX`, without checking if the heading's immediate child paragraph fits.
  - Callout cards were split indiscriminately or pushed past page bounds.
  - Fix: Enforce atomic heading grouping (a heading MUST be followed by at least 120px of its first content element or it automatically starts a new page). Atomic callouts under 220px must not be split across pages.

### 4. Ruled-Grid Baseline Misalignment
- **Evidence**:
  - Rendered contact sheet pages show text baselines intersecting the 28px blue ruled lines at arbitrary fractional offsets.
- **Root Cause & Fix**:
  - Headings had line heights like `35px` or `42px` and arbitrary margins (`6px`, `8px`), desynchronizing all subsequent lines from the 28px background grid.
  - Fix: Quantize every vertical block (heading height, margins, padding, card heights) to integer multiples of `28px` (`line-height: 28px` or `56px`, margins in multiples of `28px`), with a calibrated `padding-top` offset to anchor the font baseline directly onto the rule.

### 5. Notebook Styling & Web Edition Removal
- **Evidence**:
  - Pill badges (`QUICK RECALL`, `DEFINITION`) and rigid CSS tables gave the appearance of a web app rather than handwritten student notes.
  - Dual editions (`*-handwritten.html` and `*-handwritten.pdf`) created redundant maintenance and bloated disk footprint.
- **Decision & Fix**:
  - Per project decision, eliminate the separate "Handwritten notebook (web)" edition. Intermediate HTML used during Playwright generation resides in git-ignored `build/handwritten/`.
  - Redraw callouts, underlines, and tables with organic hand-drawn aesthetics using Rough.js or styled SVG borders.
  - Retain the restrained student pen palette: blue ink for body text, black ink for headings, green ink for definitions, red ink for tips/mistakes, and purple ink for formulas.
