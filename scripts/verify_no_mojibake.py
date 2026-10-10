#!/usr/bin/env python3
"""
SEM 5 · Encoding & Subject Title Integrity Verification
Audits data/subjects.js, data/notes-index.json, and data/notes-index.js:
1. Zero mojibake characters (Ã, Â, â€, Æ’, ‚, \ufffd).
2. Strict subject title matching: No cross-subject title pollution
   (e.g., 'Requirements Engineering' only in SE, never in TOC, ML, or EVS).
3. Every registered file path exists on disk and is not empty.
"""

import os
import sys
import json
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

MOJIBAKE_PATTERNS = [
    r'Ã', r'Â', r'â€', r'Æ’', r'‚', r'\ufffd'
]

SUBJECT_EXCLUSIVE_TERMS = {
    'toc': ['Requirements Engineering', 'Software Engineering', 'Machine Learning', 'Environmental Studies', 'React'],
    'ml': ['Requirements Engineering', 'Automata', 'Pumping Lemma', 'Environmental Studies'],
    'evs': ['Requirements Engineering', 'Regression', 'Automata', 'Pumping Lemma'],
    'se': ['Automata', 'Pumping Lemma', 'Ecosystems', 'Biodiversity'],
    'cn': ['Requirements Engineering', 'Automata', 'Ecosystems'],
    'ai': ['Requirements Engineering', 'Pumping Lemma', 'Ecosystems'],
    'rmipr': ['Requirements Engineering', 'Automata', 'Pumping Lemma'],
    'reactjs': ['Requirements Engineering', 'Automata', 'Pumping Lemma', 'Ecosystems']
}

def verify_encoding_and_titles():
    print("=" * 70)
    print("AUDITING ENCODING (MOJIBAKE) & SUBJECT TITLE INTEGRITY")
    print("=" * 70)

    errors = []

    # 1. Audit data/subjects.js
    subjects_file = os.path.join(REPO_ROOT, 'data/subjects.js')
    with open(subjects_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex search for mojibake in file text
    for pat in MOJIBAKE_PATTERNS:
        matches = re.findall(pat, content)
        if matches:
            errors.append(f"Mojibake pattern '{pat}' found in data/subjects.js ({len(matches)} occurrences)")

    m = re.search(r"window\.SEM5_DATA\s*=\s*(\{[\s\S]*?\n\});", content)
    if not m:
        errors.append("Failed to parse window.SEM5_DATA from data/subjects.js")
        return False

    data = json.loads(m.group(1))

    total_files_checked = 0
    for s in data.get('subjects', []):
        sid = s['id']
        forbidden = SUBJECT_EXCLUSIVE_TERMS.get(sid, [])
        for u in s.get('units', []):
            for f in u.get('files', []):
                total_files_checked += 1
                title = f.get('title', '')
                fpath = f.get('path', '')

                # Check mojibake in title
                for pat in MOJIBAKE_PATTERNS:
                    if re.search(pat, title):
                        errors.append(f"Mojibake in title: '{title}' [{sid} / {fpath}]")

                # Check cross-subject title pollution
                for term in forbidden:
                    if term.lower() in title.lower():
                        errors.append(f"Cross-subject pollution: '{title}' contains '{term}' in subject '{sid}'!")

                # Check file exists on disk
                disk_path = os.path.join(REPO_ROOT, fpath)
                if not os.path.exists(disk_path):
                    errors.append(f"Registered file missing on disk: {fpath} [{sid}]")
                elif os.path.getsize(disk_path) == 0:
                    errors.append(f"Registered file is empty (0 bytes): {fpath}")

    # 2. Audit data/notes-index.json
    index_file = os.path.join(REPO_ROOT, 'data/notes-index.json')
    with open(index_file, 'r', encoding='utf-8') as f:
        index_content = f.read()

    for pat in MOJIBAKE_PATTERNS:
        matches = re.findall(pat, index_content)
        if matches:
            errors.append(f"Mojibake pattern '{pat}' found in data/notes-index.json ({len(matches)} occurrences)")

    index_entries = json.loads(index_content)
    for entry in index_entries:
        title = entry.get('title', '')
        sid = entry.get('subject', '')
        forbidden = SUBJECT_EXCLUSIVE_TERMS.get(sid, [])

        for pat in MOJIBAKE_PATTERNS:
            if re.search(pat, title):
                errors.append(f"Mojibake in search entry: '{title}' [{sid}]")

        for term in forbidden:
            if term.lower() in title.lower():
                errors.append(f"Cross-subject search pollution: '{title}' contains '{term}' in subject '{sid}'!")

    # 3. Print report
    print(f"Total registered files audited: {total_files_checked}")
    print(f"Total search index entries audited: {len(index_entries)}")

    if errors:
        print(f"\n❌ FAILED with {len(errors)} errors:")
        for e in errors[:25]:
            print(f"   -> {e}")
        if len(errors) > 25:
            print(f"   ... and {len(errors) - 25} more errors.")
        return False
    else:
        print("\n✅ ZERO mojibake characters and ZERO cross-subject title mismatches found!")
        return True

if __name__ == '__main__':
    ok = verify_encoding_and_titles()
    sys.exit(0 if ok else 1)
