import os
import re
import json
import hashlib
import subprocess
from collections import defaultdict

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Natural sort key
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def clean_title_from_filename(filename):
    base, ext = os.path.splitext(filename)
    low = base.lower()

    # 1. Past Papers: SEE, Make-Up, Supplementary
    if 'see' in low or 'makeup' in low or 'make-up' in low:
        year = re.search(r'20\d\d', low)
        yr_str = year.group(0) if year else ''
        term = ''
        if 'jan' in low: term = ' (Jan)'
        elif 'feb' in low: term = ' (Feb)'
        elif 'apr' in low: term = ' (Apr)'
        elif 'may' in low: term = ' (May)'
        elif 'july' in low: term = ' (July)'

        kind = 'SEE'
        if 'makeup' in low or 'make-up' in low:
            kind = 'SEE Make-Up'
        elif 'supply' in low or 'supplementary' in low:
            kind = 'SEE Supplementary'
        elif 'backlog' in low:
            kind = 'SEE Backlog'

        suffix = ''
        if low.endswith('-o') or '2025-o' in low:
            suffix = ' (Alternate Scheme)'
        elif 'old' in low:
            suffix = ' (Old Scheme)'

        return f"{kind} Question Paper {yr_str}{term}{suffix}".strip()

    # 2. CIE Papers
    if 'cie' in low:
        year = re.search(r'20\d\d', low)
        yr_str = f" ({year.group(0)})" if year else ''
        if 'sample-cie-question-board' in low:
            return "Sample CIE Question Board Reference"
        if 'cie1-and-2' in low or 'cie1-2' in low or 'cie-1-and-2' in low or 'cie1-and-cie2' in low:
            return f"CIE-1 & CIE-2 Question Papers{yr_str}"
        if 'cie1' in low or 'cie-1' in low:
            return f"CIE-1 Question Paper{yr_str}"
        if 'cie2' in low or 'cie-2' in low:
            return f"CIE-2 Question Paper{yr_str}"
        return f"CIE Question Paper{yr_str}"

    # 3. Unit slide decks / parts: e.g. unit-1-1, unit-1-2, unit-2-2
    m = re.match(r'^unit-(\d+)-(\d+)$', low)
    if m:
        return f"Unit {m.group(1)} · Part {m.group(2)}"

    # 4. Interactive unit notes: e.g. unit-1-notes, unit-2-notes
    m = re.match(r'^unit-(\d+)-notes$', low)
    if m:
        return f"Unit {m.group(1)}: Interactive Notes"

    # 5. Hand-written notebook PDFs
    if 'handwritten' in low:
        if 'pyq' in low:
            return "Handwritten PYQ Solutions (PDF)"
        m = re.search(r'unit[ -]?(\d+)|u(\d+)', low)
        if m:
            u_num = m.group(1) or m.group(2)
            return f"Unit {u_num}: Handwritten Notebook (PDF)"
        return "Handwritten Notebook (PDF)"

    # 6. PYQ solutions interactive
    if 'pyq-answers' in low:
        return "CIE-1 Solved PYQ Bank (Interactive)"

    # 7. Specific known course decks and resources
    custom_map = {
        'cn-unit1-complete': "Unit 1: Physical & Data Link Layer Complete Deck",
        'cn-unit2-complete': "Unit 2: Network Layer & Routing Complete Deck",
        'cn-unit3a-ipv4': "Unit 3A: IPv4 Addressing & Subnetting",
        'toc-notes-complete': "Theory of Computation Complete Handwritten Notebook",
        'ai-adversarial-search': "Unit 2: Adversarial Search & Game Playing",
        'ai-consolidated-ppts': "AI Consolidated Lecture Slide Decks",
        'ai-unit1-older-notes': "AI Unit 1 Archived Notes",
        'ai-unit2-older-notes': "AI Unit 2 Archived Notes",
        'rm-ipr-unit1': "Unit 1: Research Methodology Presentation",
        'rm-ipr-unit2': "Unit 2: Research Design & Sampling Presentation",
        'rm-ipr-unit3-part1': "Unit 3: IPR & Patents (Part 1) Presentation",
        'reactjs-unit1': "Unit 1: Foundations of React, Virtual DOM & JSX",
        'reactjs-unit2': "Unit 2: Components, State Management & Hooks",
        'evs-unit-1': "Unit 1: Ecosystems & Biodiversity Presentation",
        'evs-unit-2': "Unit 2: Natural Resources Presentation",
        'evs-unit-1-notes-mcq-questions': "Unit 1 Notes & MCQ Question Bank",
        'evs-unit-2-notes-mcq-questions': "Unit 2 Notes & MCQ Question Bank",
        'rmipr-assignment-1': "Assignment 1 (Research Problem Formulation)",
        'rmipr-assignment-2': "Assignment 2 (Research Design & Methods)",
        'rmipr-important-questions': "RM & IPR Important Questions & Model Answers",
        'rmipr-quiz': "RM & IPR Objective Practice Quiz",
        'rmipr-statistical-tables': "Statistical Tables & Distribution Reference",
        'rmipr-unit1-worksheet': "Unit 1 Revision Worksheet",
        'rmipr-unit2-worksheet': "Unit 2 Revision Worksheet",
        'rmipr-unit3-worksheet': "Unit 3 Revision Worksheet",
        'se-syllabus-2026-27': "Software Engineering Syllabus 2026–27",
        'se-kanban-agile-sprint-lab-manual': "Kanban & Agile Sprint Lab Manual",
        'ml-prog1-regression': "Lab Program 1 · Linear Regression",
        'ml-prog1-simple': "Lab Program 1 · Simple Linear Regression",
        'ml-prog2-logistic-regression': "Lab Program 2 · Logistic Regression",
        'ml-prog3': "Lab Program 3 · Decision Tree Classification",
        'tableau-introduction': "Introduction to Tableau Data Visualization",
        'weka-tutorial': "Weka Data Mining Toolkit Tutorial",
        'unit-2-system-modeling': "Unit 2 · System Modeling (UML)",
        'unit-2': "Unit 2 · Requirements Engineering",
        'is53-cn-unit1-archive': "Unit 1 Archived Notes (Past Batch)",
        'is53-cn-unit2-archive': "Unit 2 Archived Notes (Past Batch)",
        'se-unit1-archive': "Unit 1 Archived Notes (Past Batch)",
        'se-unit2-archive': "Unit 2 Archived Notes (Past Batch)",
        'rmipr-unit1-archive': "Unit 1 Archived Notes (Past Batch)",
        'rmipr-unit2-archive': "Unit 2 Archived Notes (Past Batch)",
        'rmipr-unit3-archive': "Unit 3 Archived Notes (Past Batch)",
        'ml-ch2-understanding-data': "Unit 2: Understanding Data & Preprocessing",
    }
    for k, v in custom_map.items():
        if k in low:
            return v

    # Strip subject prefix only once
    cleaned = re.sub(r'^(ml|se|cn|is53-cn|toc|ai|rmipr|rm-ipr|reactjs|evs)-', '', base)
    cleaned = cleaned.replace('-', ' ').replace('_', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned.title()

def sync_subjects():
    print("=" * 70)
    print("SYNCING data/subjects.js FROM notes/ DIRECTORY")
    print("=" * 70)

    # 1. Load scope.json
    scope_file = os.path.join(REPO_ROOT, 'data', 'scope.json')
    with open(scope_file, 'r', encoding='utf-8') as f:
        scope_data = json.load(f)

    # 2. Load existing subjects_data if present to preserve metadata
    subjects_js_file = os.path.join(REPO_ROOT, 'data', 'subjects.js')
    existing_subjects_map = {}
    existing_files_map = {} # path -> file metadata

    # 2a. Load rich baseline metadata from git pre-sync-folders tag
    try:
        raw_base = subprocess.check_output(['git', 'show', 'pre-sync-folders:data/subjects.js'], cwd=REPO_ROOT).decode('utf-8')
        m_base = re.search(r'window\.SEM5_DATA\s*=\s*(\{[\s\S]*?\n\});', raw_base)
        if m_base:
            parsed_base = json.loads(m_base.group(1))
            for s in parsed_base.get('subjects', []):
                existing_subjects_map[s['id']] = s
                for u in s.get('units', []):
                    for f in u.get('files', []):
                        if f.get('path'):
                            existing_files_map[f['path'].replace('\\', '/')] = f
    except Exception as e:
        print(f"Notice: git baseline load: {e}")

    # 2b. Overlay current subjects.js in working directory if available
    if os.path.exists(subjects_js_file):
        try:
            res = os.popen('node -e "console.log(JSON.stringify(require(\'./data/subjects.js\')));"').read()
            parsed = json.loads(res)
            for s in parsed.get('subjects', []):
                if s['id'] not in existing_subjects_map:
                    existing_subjects_map[s['id']] = s
                for u in s.get('units', []):
                    for f in u.get('files', []):
                        if f.get('path'):
                            norm_p = f['path'].replace('\\', '/')
                            existing_files_map[norm_p] = f
        except Exception as e:
            print(f"Warning parsing existing subjects.js: {e}")

    notes_dir = os.path.join(REPO_ROOT, 'notes')
    subjects_order = ['ml', 'se', 'cn', 'toc', 'ai', 'rmipr', 'reactjs', 'evs']

    new_subjects = []
    added_files = 0
    preserved_files = 0
    dropped_files = 0

    for sid in subjects_order:
        s_scope = scope_data['subjects'].get(sid, {})
        s_existing = existing_subjects_map.get(sid, {})

        s_obj = {
            'id': sid,
            'code': s_scope.get('code', s_existing.get('code', '')),
            'name': s_scope.get('name', s_existing.get('name', '')),
            'shortName': s_scope.get('short_name', s_existing.get('shortName', '')),
            'credits': s_scope.get('credits', s_existing.get('credits', '3:0:0')),
            'contactHours': s_existing.get('contactHours', '45L'),
            'coordinator': s_scope.get('coordinator', s_existing.get('coordinator', '')),
            'prerequisites': s_existing.get('prerequisites', 'NIL'),
            'description': s_existing.get('description', ''),
            'examDate': s_scope.get('exam_date', s_existing.get('examDate', '')),
            'examTime': s_scope.get('exam_time', s_existing.get('examTime', '')),
            'examSchedule': s_existing.get('examSchedule', ''),
            'cie1Scope': s_scope.get('cie1_scope_description', s_existing.get('cie1Scope', '')),
            'tags': s_existing.get('tags', ['Core ISE']),
            'status': s_existing.get('status', 'cie1_ready'),
            'units': []
        }

        if 'syllabus' in s_existing:
            s_obj['syllabus'] = s_existing['syllabus']
        if 'lab' in s_existing:
            s_obj['lab'] = s_existing['lab']

        sub_dir = os.path.join(notes_dir, sid)
        if not os.path.exists(sub_dir):
            continue

        in_scope_units = s_scope.get('in_scope_units', [1, 2])

        # Containers for units
        units_dict = {}

        # Scan sub_dir
        for root, dirs, files in os.walk(sub_dir):
            rel_dir = os.path.relpath(root, sub_dir).replace('\\', '/')
            if rel_dir == '.':
                continue

            # Skip held out-of-scope files
            if 'held' in rel_dir:
                continue

            top_folder = rel_dir.split('/')[0]

            # Check optional per-folder _meta.json
            meta_json = {}
            meta_file = os.path.join(root, '_meta.json')
            if os.path.exists(meta_file):
                try:
                    with open(meta_file, 'r', encoding='utf-8') as mf:
                        meta_json = json.load(mf)
                except Exception:
                    pass

            # Determine unit key & category
            if top_folder.startswith('unit'):
                try:
                    u_num = int(top_folder.replace('unit', ''))
                except ValueError:
                    u_num = top_folder
                if isinstance(u_num, int) and u_num not in in_scope_units:
                    continue # Out of scope
                unit_key = f"unit{u_num}"
                if unit_key not in units_dict:
                    scope_u_info = s_scope.get('units', {}).get(str(u_num), {})
                    units_dict[unit_key] = {
                        'unitNumber': u_num,
                        'title': scope_u_info.get('title', f"Unit {u_num}"),
                        'topics': ', '.join(scope_u_info.get('topics', []))[:160] + '...',
                        'isPractice': False,
                        'files': []
                    }
            elif top_folder == 'recent-notes':
                unit_key = 'recent'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'RECENT',
                        'title': 'Recent Notes (Latest Uploaded Material)',
                        'topics': 'Latest lecture slide decks, worksheets, and classroom materials uploaded for this course.',
                        'isPractice': False,
                        'files': []
                    }
            elif top_folder == 'older-versions':
                unit_key = 'older'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'ARCHIVE',
                        'title': 'Older Versions / Archived Notes (Past Semesters)',
                        'topics': 'Reference material from previous semesters and alternate professor lecture decks.',
                        'isPractice': False,
                        'files': []
                    }
            elif top_folder == 'practice':
                unit_key = 'practice'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'Practice',
                        'title': 'Practice, Question Banks & Examination Papers',
                        'isPractice': True,
                        'files': []
                    }
            elif top_folder == 'pyq':
                unit_key = 'pyq'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'PYQ',
                        'title': 'CIE-1 PYQ Bank & Model Answers',
                        'isPractice': True,
                        'files': []
                    }
            elif top_folder == 'syllabus':
                unit_key = 'syllabus'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'Syllabus',
                        'title': 'Official Syllabus Document',
                        'isPractice': False,
                        'files': []
                    }
            elif top_folder == 'lab':
                unit_key = 'lab'
                if unit_key not in units_dict:
                    units_dict[unit_key] = {
                        'unitNumber': 'Lab',
                        'title': 'Laboratory Manuals, Programs & Notebooks',
                        'isPractice': False,
                        'files': []
                    }
            else:
                continue

            for f in sorted(files, key=natural_sort_key):
                if f.endswith(('.webp', '.json', '.txt', '.csv', '.names', '.xlsx')):
                    continue # Assets, metadata, data

                ext = os.path.splitext(f)[1].lower()
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, REPO_ROOT).replace('\\', '/')
                sz = os.path.getsize(full_path)
                sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"

                # If this is an original source file (.pptx, .docx, .ipynb) whose converted version exists,
                # let the converted PDF/HTML be primary and attach this as originalPath
                if ext in ('.pptx', '.docx', '.ipynb'):
                    pdf_sibling = os.path.splitext(full_path)[0] + ('.pdf' if ext != '.ipynb' else '.html')
                    if os.path.exists(pdf_sibling):
                        continue # Registered via the PDF/HTML entry below

                # Determine primary type and originalPath
                is_converted = False
                original_path = None
                ftype = 'pdf'

                if f.endswith('.html'):
                    if 'pyq-answers' in f:
                        ftype = 'pyq'
                    elif 'unit-' in f:
                        ftype = 'notes'
                    elif full_path.replace('.html', '.ipynb') and os.path.exists(full_path.replace('.html', '.ipynb')):
                        ftype = 'ipynb'
                        is_converted = True
                        original_path = rel_path.replace('.html', '.ipynb')
                elif f.endswith('.pdf'):
                    if 'handwritten' in rel_path:
                        ftype = 'handwritten'
                    else:
                        ftype = 'pdf'
                        for src_ext in ['.pptx', '.docx', '.ppt', '.doc']:
                            src_candidate = full_path.replace('.pdf', src_ext)
                            if os.path.exists(src_candidate):
                                is_converted = True
                                original_path = rel_path.replace('.pdf', src_ext)
                                break

                # Generate unique ID
                file_id = re.sub(r'[^a-z0-9]+', '-', f.lower()).strip('-')
                file_id = f"{sid}-{file_id}"

                # Title and metadata
                clean_title = clean_title_from_filename(f)
                file_meta = {
                    'id': file_id,
                    'title': clean_title,
                    'originalName': f,
                    'path': rel_path,
                    'type': ftype,
                    'sizeBytes': sz,
                    'size': sz_fmt
                }

                if is_converted:
                    file_meta['isConverted'] = True
                if original_path:
                    file_meta['originalPath'] = original_path

                # Check if file was already in subjects.js to preserve hand-tuned title/tag/pages
                if rel_path in existing_files_map:
                    old_meta = existing_files_map[rel_path]
                    old_title = old_meta.get('title', '')
                    if old_title and len(old_title) >= 5 and not old_title.isdigit():
                        file_meta['title'] = old_title
                    else:
                        file_meta['title'] = clean_title
                    if 'tag' in old_meta:
                        file_meta['tag'] = old_meta['tag']
                    if 'pages' in old_meta:
                        file_meta['pages'] = old_meta['pages']
                    if 'readingTime' in old_meta:
                        file_meta['readingTime'] = old_meta['readingTime']
                    file_meta['id'] = old_meta.get('id', file_meta['id'])
                    preserved_files += 1
                else:
                    # Provide appropriate tags
                    if ftype == 'notes':
                        file_meta['tag'] = 'Interactive notes'
                    elif ftype == 'handwritten':
                        file_meta['tag'] = 'Vector Handwritten'
                    elif 'see' in rel_path:
                        file_meta['tag'] = 'SEE Past Paper'
                    elif 'cie' in rel_path:
                        file_meta['tag'] = 'CIE Question Paper'
                    elif 'worksheet' in rel_path:
                        file_meta['tag'] = 'Revision Worksheet'
                    elif 'assignment' in rel_path:
                        file_meta['tag'] = 'Assignment'
                    elif 'quiz' in rel_path:
                        file_meta['tag'] = 'Objective Quiz'
                    elif top_folder == 'recent-notes':
                        file_meta['tag'] = 'Recent Upload'
                    added_files += 1

                # Custom _meta.json overrides
                if f in meta_json:
                    override = meta_json[f]
                    file_meta.update(override)

                units_dict[unit_key]['files'].append(file_meta)

        # Sort files inside each unit sensibly:
        # Order: notes -> handwritten -> faculty pdf (natural sort) -> practice
        type_priority = {'notes': 1, 'handwritten': 2, 'ipynb': 3, 'pdf': 4, 'pyq': 5}
        for u_key, u_data in units_dict.items():
            u_data['files'].sort(key=lambda item: (type_priority.get(item['type'], 99), natural_sort_key(item['title'])))

        # Order units:
        # 1. recent (Recent Notes) if present, so student's latest material is right at top!
        # 2. unit1, unit2, unit3...
        # 3. older (Older Versions Archive)
        # 4. lab
        # 5. syllabus
        # 6. pyq
        # 7. practice
        ordered_units = []
        if 'recent' in units_dict and units_dict['recent']['files']:
            ordered_units.append(units_dict['recent'])
        for u_num in in_scope_units:
            u_k = f"unit{u_num}"
            if u_k in units_dict and units_dict[u_k]['files']:
                ordered_units.append(units_dict[u_k])
        if 'older' in units_dict and units_dict['older']['files']:
            ordered_units.append(units_dict['older'])
        if 'lab' in units_dict and units_dict['lab']['files']:
            ordered_units.append(units_dict['lab'])
        if 'syllabus' in units_dict and units_dict['syllabus']['files']:
            ordered_units.append(units_dict['syllabus'])
        if 'pyq' in units_dict and units_dict['pyq']['files']:
            ordered_units.append(units_dict['pyq'])
        if 'practice' in units_dict and units_dict['practice']['files']:
            ordered_units.append(units_dict['practice'])

        s_obj['units'] = ordered_units
        new_subjects.append(s_obj)

    # Compute overall meta
    total_files = sum(len(u['files']) for s in new_subjects for u in s['units'])
    total_size_bytes = sum(f.get('sizeBytes', 0) for s in new_subjects for u in s['units'] for f in u['files'])
    total_size_mb = f"{total_size_bytes / (1024 * 1024):.1f} MB"

    final_data = {
        'subjects': new_subjects,
        'meta': {
            'totalFiles': total_files,
            'totalSize': total_size_mb,
            'totalSizeBytes': total_size_bytes,
            'lastUpdated': '2026-10-10',
            'academicYear': '2026–2027',
            'semester': 'Semester V',
            'department': 'Department of Information Science & Engineering'
        }
    }

    # Write output to data/subjects.js
    header = """/**
 * SEM 5 · ISE Notes Portal - Official Course Registry & Metadata Single Source of Truth
 * Department of Information Science & Engineering
 * Auto-generated by scripts/sync_subjects_from_folders.py
 */

if (typeof window === 'undefined') {
  var window = typeof global !== 'undefined' ? global : this;
  window.window = window;
}

window.SEM5_DATA = """

    footer = """\n
if (typeof module !== 'undefined' && module.exports) {
  module.exports = window.SEM5_DATA;
}
"""

    js_content = header + json.dumps(final_data, indent=2) + ";" + footer

    with open(subjects_js_file, 'w', encoding='utf-8') as out_f:
        out_f.write(js_content)

    print(f"\nSuccessfully generated {subjects_js_file}!")
    print(f"Summary:")
    print(f"  Total Subjects: {len(new_subjects)}")
    print(f"  Total Registered Files: {total_files}")
    print(f"  Total Size: {total_size_mb}")
    print(f"  Preserved Files (existing metadata retained): {preserved_files}")
    print(f"  New Files Added: {added_files}")

if __name__ == '__main__':
    sync_subjects()
