const fs = require('fs');
const path = require('path');

const METADATA = {
  ml: {
    1: { pages: 43, size: "2.00 MB", sizeBytes: 2098816 },
    2: { pages: 39, size: "1.96 MB", sizeBytes: 2055211 },
    3: { pages: 36, size: "1.84 MB", sizeBytes: 1930287 }
  },
  se: {
    1: { pages: 29, size: "1.77 MB", sizeBytes: 1856139 },
    2: { pages: 18, size: "0.89 MB", sizeBytes: 933714 },
    3: { pages: 17, size: "0.76 MB", sizeBytes: 799097 }
  },
  cn: {
    1: { pages: 32, size: "1.70 MB", sizeBytes: 1779368 },
    2: { pages: 24, size: "1.50 MB", sizeBytes: 1569603 },
    3: { pages: 35, size: "1.74 MB", sizeBytes: 1825351 }
  },
  toc: {
    1: { pages: 25, size: "1.40 MB", sizeBytes: 1463729 },
    2: { pages: 35, size: "1.74 MB", sizeBytes: 1821232 },
    3: { pages: 31, size: "1.59 MB", sizeBytes: 1666363 }
  },
  ai: {
    1: { pages: 32, size: "1.93 MB", sizeBytes: 2019909 },
    2: { pages: 31, size: "1.79 MB", sizeBytes: 1875329 },
    3: { pages: 27, size: "1.68 MB", sizeBytes: 1765061 }
  },
  rmipr: {
    1: { pages: 27, size: "1.10 MB", sizeBytes: 1156312 },
    2: { pages: 24, size: "1.01 MB", sizeBytes: 1058973 },
    3: { pages: 24, size: "1.02 MB", sizeBytes: 1067043 }
  },
  reactjs: {
    1: { pages: 27, size: "1.42 MB", sizeBytes: 1492417 },
    2: { pages: 26, size: "1.29 MB", sizeBytes: 1347673 },
    3: { pages: 20, size: "1.08 MB", sizeBytes: 1127989 }
  },
  evs: {
    1: { pages: 25, size: "1.22 MB", sizeBytes: 1282581 },
    2: { pages: 25, size: "1.24 MB", sizeBytes: 1300156 },
    3: { pages: 24, size: "1.19 MB", sizeBytes: 1248345 }
  }
};

let content = fs.readFileSync('data/subjects.js', 'utf8');

let count = 0;
for (const sub of Object.keys(METADATA)) {
  for (const u of [1, 2, 3]) {
    const meta = METADATA[sub][u];
    const notesIdRegex = new RegExp(`id:\\s*"${sub}-u${u}-notes"[\\s\\S]*?\\},`, 'm');
    const match = content.match(notesIdRegex);
    if (!match) {
      console.error(`Could not find notes entry for ${sub}-u${u}`);
      continue;
    }

    const handwrittenObj = `
            {
              id: "${sub}-u${u}-handwritten",
              title: "Handwritten notes",
              originalName: "${sub}-unit${u}-handwritten.pdf",
              path: "notes/${sub}/unit${u}/handwritten/${sub}-unit${u}-handwritten.pdf",
              type: "handwritten",
              tag: "Generated",
              generated: true,
              pages: ${meta.pages},
              size: "${meta.size}",
              sizeBytes: ${meta.sizeBytes},
              previewImage: "notes/${sub}/unit${u}/handwritten/${sub}-unit${u}-preview.webp",
              sourceHtml: "notes/${sub}/unit${u}/unit-${u}-notes.html"
            },`;

    const replacement = match[0] + handwrittenObj;
    content = content.replace(match[0], replacement);
    count++;
  }
}

console.log(`Successfully injected ${count} handwritten entries into subjects.js`);
fs.writeFileSync('data/subjects.js', content, 'utf8');
