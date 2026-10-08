const fs = require('fs');
const path = require('path');

const stats = JSON.parse(fs.readFileSync('audit/handwritten_stats.json', 'utf8'));
let code = fs.readFileSync('data/subjects.js', 'utf8');

// Load existing data
let window = {};
eval(code);
let semData = window.SEM5_DATA;

for (const sub of semData.subjects) {
  const subId = sub.id;
  for (const unit of sub.units || []) {
    const uNum = unit.unitNumber;
    if (typeof uNum === 'number' && [1, 2, 3].includes(uNum) && stats[subId] && stats[subId][String(uNum)]) {
      const uStats = stats[subId][String(uNum)];
      
      // Remove any existing handwritten entries so we can add the clean pairs
      unit.files = (unit.files || []).filter(f => f.type !== 'handwritten' && f.type !== 'handwritten-web' && !f.id.includes('handwritten'));
      
      // Find index of notes file to place handwritten right next to it
      const notesIdx = unit.files.findIndex(f => f.type === 'notes');
      
      const hwPdfEntry = {
        id: `${subId}-u${uNum}-handwritten-pdf`,
        title: "Handwritten notebook (PDF)",
        originalName: `${subId}-unit${uNum}-handwritten.pdf`,
        path: `notes/${subId}/unit${uNum}/handwritten/${subId}-unit${uNum}-handwritten.pdf`,
        type: "handwritten",
        tag: "PDF Notebook",
        generated: true,
        pages: uStats.pages,
        size: uStats.pdfSizeMB,
        sizeBytes: uStats.pdfSizeBytes,
        previewImage: `notes/${subId}/unit${uNum}/handwritten/${subId}-unit${uNum}-preview.webp`,
        sourceHtml: `notes/${subId}/unit${uNum}/unit-${uNum}-notes.html`
      };

      const hwWebEntry = {
        id: `${subId}-u${uNum}-handwritten-web`,
        title: "Handwritten notebook (web)",
        originalName: `${subId}-unit${uNum}-handwritten.html`,
        path: `notes/${subId}/unit${uNum}/handwritten/${subId}-unit${uNum}-handwritten.html`,
        type: "handwritten-web",
        tag: "Web Notebook",
        generated: true,
        pages: uStats.pages,
        size: `Web Edition (${uStats.htmlSizeKB})`,
        sizeBytes: uStats.htmlSizeBytes,
        previewImage: `notes/${subId}/unit${uNum}/handwritten/${subId}-unit${uNum}-preview.webp`,
        sourceHtml: `notes/${subId}/unit${uNum}/unit-${uNum}-notes.html`
      };

      if (notesIdx !== -1) {
        unit.files.splice(notesIdx + 1, 0, hwPdfEntry, hwWebEntry);
      } else {
        unit.files.push(hwPdfEntry, hwWebEntry);
      }
    } else if (typeof uNum === 'number' && [4, 5].includes(uNum)) {
      unit.isSyllabusOnly = true;
      if (!unit.files) unit.files = [];
    }
  }
}

// Format back to window.SEM5_DATA = ...;
const newContent = `/**
 * SEM 5 · ISE Notes - Central Data Store
 * Source of Truth: ISE III Year Syllabus (2024 Batch Final) - V Semester
 * Total Credits: 22 (L: 18, T: 1, P: 3)
 */

window.SEM5_DATA = ${JSON.stringify(semData, null, 2)};
`;

fs.writeFileSync('data/subjects.js', newContent, 'utf8');
console.log('Successfully updated data/subjects.js with all 24 pairs of handwritten notebooks and syllabus-only flags!');
