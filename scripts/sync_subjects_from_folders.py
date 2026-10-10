#!/usr/bin/env python3
"""
SEM 5 · ISE Notes Portal - Official Course Registry & Metadata Synchronizer
Single Source of Truth: data/subjects.js

Enforces Strict Policy:
Every unit shows ONLY (in this exact order):
  1. Interactive HTML Notes (Unit N: Interactive Notes)
  2. Handwritten Notebook (PDF)
  3. Recent Notes (from subject's recent-notes/ folder, mapped to appropriate unit)

All older faculty slides, alternate/condensed notes, and past archives are
moved to archive/removed-from-site/ and never registered or served.
"""

import os
import re
import json
import hashlib
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

# Authoritative Recent Notes Mapping per Subject
RECENT_NOTES_REGISTRY = {
    'ml': {
        'ml-ch2-understanding-data.pdf': {
            'unit': 1,
            'title': "Unit 1 - Chapter 2: Understanding Data & Preprocessing",
            'tag': "Recent Notes"
        },
        'ml-ch3-basic-concepts-of-learning.pdf': {
            'unit': 1,
            'title': "Unit 1 - Chapter 3: Basic Concepts of Learning",
            'tag': "Recent Notes"
        },
        'ml-ch3-5-inductive-bias-bias-variance.pdf': {
            'unit': 1,
            'title': "Unit 1 - Section 3.5: Inductive Bias & Bias-Variance Dilemma",
            'tag': "Recent Notes"
        },
        'ml-ch3-6-modeling-ml-detailed.pdf': {
            'unit': 1,
            'title': "Unit 1 - Section 3.6: Modeling in Machine Learning",
            'tag': "Recent Notes"
        },
        'ml-ch3-7-learning-frameworks-detailed.pdf': {
            'unit': 1,
            'title': "Unit 1 - Section 3.7: Learning Frameworks (PAC Learning)",
            'tag': "Recent Notes"
        },
        'ml-ch4-similarity-based-learning.pdf': {
            'unit': 2,
            'title': "Unit 2 - Chapter 4: Similarity-Based Learning & k-NN",
            'tag': "Recent Notes"
        },
        'ml-ch5-regression-analysis-detailed.pdf': {
            'unit': 3,
            'title': "Unit 3 - Chapter 5: Regression Analysis & Gradient Descent",
            'tag': "Recent Notes"
        },
        'ml-ch5-regression-problems-solutions.pdf': {
            'unit': 3,
            'title': "Unit 3 - Chapter 5: Regression Numerical Worked Problems",
            'tag': "Recent Notes"
        },
        'ml-ch5-4-validation-of-regression-methods.pdf': {
            'unit': 3,
            'title': "Unit 3 - Section 5.4: Validation of Regression Methods",
            'tag': "Recent Notes"
        }
    },
    'se': {
        'unit-1-1.pdf': {
            'unit': 1,
            'title': "Unit 1 - Part 1: Professional Software Development & Ethics",
            'tag': "Recent Notes"
        },
        'unit-1-2.pdf': {
            'unit': 1,
            'title': "Unit 1 - Part 2: Software Process Models",
            'tag': "Recent Notes"
        },
        'unit-1-3.pdf': {
            'unit': 1,
            'title': "Unit 1 - Part 3: Agile Software Development & Scrum",
            'tag': "Recent Notes"
        },
        'unit-2-2.pdf': {
            'unit': 2,
            'title': "Unit 2 - Part 2: Requirements Specification & Modeling",
            'tag': "Recent Notes"
        },
        'unit-2-system-modeling.pdf': {
            'unit': 2,
            'title': "Unit 2 - System Modeling (Context, Interaction, Structural, Behavioral)",
            'tag': "Recent Notes"
        }
    },
    'cn': {
        'cn-unit1-complete.pdf': {
            'unit': 1,
            'title': "Unit 1 - Complete Lecture Deck: Physical & Data Link Layer",
            'tag': "Recent Notes"
        },
        'cn-unit2-complete.pdf': {
            'unit': 2,
            'title': "Unit 2 - Complete Lecture Deck: Network Layer & Routing Protocols",
            'tag': "Recent Notes"
        },
        'cn-unit3a-ipv4.pdf': {
            'unit': 3,
            'title': "Unit 3A - IPv4 Addressing & Subnetting (CIDR & VLSM)",
            'tag': "Recent Notes"
        }
    },
    'toc': {
        'toc-notes-complete.pdf': {
            'unit': 1,
            'title': "Theory of Computation Complete Course Notebook",
            'tag': "Recent Notes",
            'coverageTag': "Covers Units 1-2",
            'scopeTag': "Partly beyond CIE-1 scope"
        }
    },
    'ai': {
        'ai-adversarial-search.pdf': {
            'unit': 2,
            'title': "Unit 2 - Adversarial Search & Game Playing (Minimax & Alpha-Beta)",
            'tag': "Recent Notes"
        }
    },
    'rmipr': {
        'rm-ipr-unit1.pdf': {
            'unit': 1,
            'title': "Unit 1 - Research Methodology Presentation Deck",
            'tag': "Recent Notes"
        },
        'rm-ipr-unit2.pdf': {
            'unit': 2,
            'title': "Unit 2 - Research Design & Sampling Presentation Deck",
            'tag': "Recent Notes"
        },
        'rm-ipr-unit3-part1.pdf': {
            'unit': 3,
            'title': "Unit 3 - Intellectual Property Rights & Patents (Part 1)",
            'tag': "Recent Notes"
        }
    },
    'reactjs': {
        'reactjs-unit1.pdf': {
            'unit': 1,
            'title': "Unit 1 - Foundations of React, Virtual DOM & JSX",
            'tag': "Recent Notes"
        },
        'reactjs-unit2.pdf': {
            'unit': 2,
            'title': "Unit 2 - Components, State Management & Hooks",
            'tag': "Recent Notes"
        }
    },
    'evs': {
        'evs-unit-1.pdf': {
            'unit': 1,
            'title': "Unit 1 - Ecosystems & Biodiversity Presentation Deck",
            'tag': "Recent Notes"
        },
        'evs-unit-2.pdf': {
            'unit': 2,
            'title': "Unit 2 - Natural Resources & Conservation Presentation Deck",
            'tag': "Recent Notes"
        }
    }
}

def clean_practice_title(filename):
    base, ext = os.path.splitext(filename)
    low = base.lower()

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
        elif 'supply' in low or 'supplementary' in low or 'supple' in low:
            kind = 'SEE Supplementary'
        elif 'backlog' in low:
            kind = 'SEE Backlog'

        suffix = ''
        if low.endswith('-o') or '2025-o' in low:
            suffix = ' (Alternate Scheme)'
        elif 'old' in low:
            suffix = ' (Old Scheme)'

        return f"{kind} Question Paper {yr_str}{term}{suffix}".strip()

    if 'cie' in low:
        year = re.search(r'20\d\d', low)
        yr_str = f" ({year.group(0)})" if year else ''
        if 'sample-cie-question-board' in low:
            return "Sample CIE Question Board Reference"
        if 'cie1-and-2' in low or 'cie1-2' in low or 'cie-1-and-2' in low:
            return f"CIE-1 & CIE-2 Question Papers{yr_str}"
        if 'cie1' in low or 'cie-1' in low:
            return f"CIE-1 Question Paper{yr_str}"
        if 'cie2' in low or 'cie-2' in low:
            return f"CIE-2 Question Paper{yr_str}"
        return f"CIE Question Paper{yr_str}"

    custom_practice = {
        'rmipr-assignment-1': "Assignment 1 (Research Problem Formulation)",
        'rmipr-assignment-2': "Assignment 2 (Research Design & Methods)",
        'rmipr-important-questions': "RM & IPR Important Questions & Model Answers",
        'rmipr-quiz': "RM & IPR Objective Practice Quiz",
        'rmipr-unit1-worksheet': "Unit 1 Revision Worksheet",
        'rmipr-unit2-worksheet': "Unit 2 Revision Worksheet",
        'rmipr-unit3-worksheet': "Unit 3 Revision Worksheet",
        'unit-1-qb': "Unit 1 Question Bank & Exercises",
    }
    for k, v in custom_practice.items():
        if k in low:
            return v

    cleaned = re.sub(r'^(ml|se|cn|is53-cn|toc|ai|rmipr|rm-ipr|reactjs|evs)-', '', base)
    cleaned = cleaned.replace('-', ' ').replace('_', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned.title()

def sync_subjects():
    print("=" * 70)
    print("SYNCING data/subjects.js (ONLY: HTML Notes + Handwritten + Recent Notes)")
    print("=" * 70)

    # 1. Load scope.json
    scope_file = os.path.join(REPO_ROOT, 'data', 'scope.json')
    with open(scope_file, 'r', encoding='utf-8') as f:
        scope_data = json.load(f)

    # 2. Baseline course schemas from git pre-sync-folders
    existing_subjects_map = {}
    try:
        raw_base = subprocess.check_output(['git', 'show', 'pre-sync-folders:data/subjects.js'], cwd=REPO_ROOT).decode('utf-8')
        m_base = re.search(r'window\.SEM5_DATA\s*=\s*(\{[\s\S]*?\n\});', raw_base)
        if m_base:
            parsed_base = json.loads(m_base.group(1))
            for s in parsed_base.get('subjects', []):
                existing_subjects_map[s['id']] = s
    except Exception as e:
        print(f"Notice: git baseline load: {e}")

    notes_dir = os.path.join(REPO_ROOT, 'notes')
    subjects_order = ['ml', 'se', 'cn', 'toc', 'ai', 'rmipr', 'reactjs', 'evs']

    new_subjects = []
    total_registered = 0
    total_size_bytes = 0

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
            'status': 'cie1_ready',
            'units': []
        }

        if 'syllabus' in s_existing:
            s_obj['syllabus'] = s_existing['syllabus']
        if 'lab' in s_existing:
            s_obj['lab'] = s_existing['lab']

        in_scope_units = s_scope.get('in_scope_units', [1, 2])
        units_list = []

        # --- A. In-Scope Numeric Units (Unit 1, Unit 2, Unit 3 where in CIE-1 scope) ---
        for u_num in in_scope_units:
            scope_u_info = s_scope.get('units', {}).get(str(u_num), {})
            unit_data = {
                'unitNumber': u_num,
                'title': scope_u_info.get('title', f"Unit {u_num}"),
                'topics': ', '.join(scope_u_info.get('topics', []))[:160] + '...',
                'isPractice': False,
                'files': []
            }

            # 1. Interactive HTML Notes (FIRST)
            html_rel = f"notes/{sid}/unit{u_num}/unit-{u_num}-notes.html"
            html_full = os.path.join(REPO_ROOT, html_rel)
            if os.path.exists(html_full):
                sz = os.path.getsize(html_full)
                sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                unit_data['files'].append({
                    'id': f"{sid}-u{u_num}-notes",
                    'title': f"Unit {u_num}: Interactive Notes",
                    'originalName': f"unit-{u_num}-notes.html",
                    'path': html_rel,
                    'type': 'notes',
                    'sizeBytes': sz,
                    'size': sz_fmt,
                    'tag': "Interactive notes"
                })

            # 2. Handwritten Notebook (PDF) (SECOND)
            hw_rel = f"notes/{sid}/unit{u_num}/handwritten/{sid}-unit{u_num}-handwritten.pdf"
            hw_full = os.path.join(REPO_ROOT, hw_rel)
            if os.path.exists(hw_full):
                sz = os.path.getsize(hw_full)
                sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                hw_meta = {
                    'id': f"{sid}-u{u_num}-handwritten-pdf",
                    'title': f"Handwritten notebook (PDF)",
                    'originalName': f"{sid}-unit{u_num}-handwritten.pdf",
                    'path': hw_rel,
                    'type': 'handwritten',
                    'sizeBytes': sz,
                    'size': sz_fmt,
                    'tag': "Vector Handwritten"
                }
                # Check toc.json for page counts
                toc_path = os.path.join(REPO_ROOT, f"notes/{sid}/unit{u_num}/handwritten/toc.json")
                if os.path.exists(toc_path):
                    try:
                        with open(toc_path, 'r', encoding='utf-8') as tf:
                            tdata = json.load(tf)
                            if 'totalPages' in tdata:
                                hw_meta['pages'] = tdata['totalPages']
                    except Exception:
                        pass
                unit_data['files'].append(hw_meta)

            # 3. Recent Notes (THIRD - only files from subject's recent-notes folder assigned to this unit)
            recent_dict = RECENT_NOTES_REGISTRY.get(sid, {})
            recent_for_unit = []
            for r_file, r_info in recent_dict.items():
                if r_info.get('unit') == u_num:
                    r_rel = f"notes/{sid}/recent-notes/{r_file}"
                    r_full = os.path.join(REPO_ROOT, r_rel)
                    if os.path.exists(r_full):
                        sz = os.path.getsize(r_full)
                        sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                        
                        file_id = re.sub(r'[^a-z0-9]+', '-', r_file.lower()).strip('-')
                        file_id = f"{sid}-{file_id}"
                        
                        f_entry = {
                            'id': file_id,
                            'title': r_info['title'],
                            'originalName': r_file,
                            'path': r_rel,
                            'type': 'pdf',
                            'sizeBytes': sz,
                            'size': sz_fmt,
                            'tag': r_info.get('tag', 'Recent Notes')
                        }

                        if 'coverageTag' in r_info:
                            f_entry['coverageTag'] = r_info['coverageTag']
                        if 'scopeTag' in r_info:
                            f_entry['scopeTag'] = r_info['scopeTag']

                        # Check if converted from pptx or docx
                        for src_ext in ['.pptx', '.docx', '.ppt', '.doc']:
                            src_cand = r_full.replace('.pdf', src_ext)
                            if os.path.exists(src_cand):
                                f_entry['isConverted'] = True
                                f_entry['originalPath'] = r_rel.replace('.pdf', src_ext)
                                break

                        recent_for_unit.append(f_entry)

            # Natural sort recent notes by title
            recent_for_unit.sort(key=lambda x: natural_sort_key(x['title']))
            unit_data['files'].extend(recent_for_unit)

            units_list.append(unit_data)

        # --- B. Laboratory Programs & Manuals (if course has lab) ---
        lab_dir = os.path.join(REPO_ROOT, f"notes/{sid}/lab")
        if os.path.exists(lab_dir):
            lab_files = []
            for root, dirs, files in os.walk(lab_dir):
                for f in sorted(files, key=natural_sort_key):
                    if f.endswith(('.pptx', '.docx', '.ipynb', '.xlsx', '.csv')):
                        continue
                    if f.endswith(('.html', '.pdf')):
                        f_full = os.path.join(root, f)
                        f_rel = os.path.relpath(f_full, REPO_ROOT).replace('\\', '/')
                        sz = os.path.getsize(f_full)
                        sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                        
                        file_id = re.sub(r'[^a-z0-9]+', '-', f.lower()).strip('-')
                        file_id = f"{sid}-{file_id}"

                        ftype = 'ipynb' if f.endswith('.html') and os.path.exists(f_full.replace('.html', '.ipynb')) else 'pdf'
                        is_converted = ftype == 'ipynb'
                        orig_path = f_rel.replace('.html', '.ipynb') if ftype == 'ipynb' else None

                        title = f.replace('-', ' ').replace('_', ' ').replace('.html', '').replace('.pdf', '').title()
                        if 'prog1' in f: title = "Lab Program 1 - Regression"
                        elif 'prog2' in f: title = "Lab Program 2 - Logistic Regression"
                        elif 'prog3' in f: title = "Lab Program 3 - Decision Tree Classification"
                        elif 'tableau' in f: title = "Introduction to Tableau Data Visualization"
                        elif 'kanban' in f: title = "Kanban & Agile Sprint Lab Manual"

                        lab_entry = {
                            'id': file_id,
                            'title': title,
                            'originalName': f,
                            'path': f_rel,
                            'type': ftype,
                            'sizeBytes': sz,
                            'size': sz_fmt
                        }
                        if is_converted: lab_entry['isConverted'] = True
                        if orig_path: lab_entry['originalPath'] = orig_path
                        lab_files.append(lab_entry)

            if lab_files:
                units_list.append({
                    'unitNumber': 'Lab',
                    'title': 'Laboratory Manuals, Programs & Notebooks',
                    'isPractice': False,
                    'files': lab_files
                })

        # --- C. Official Syllabus Document ---
        syl_dir = os.path.join(REPO_ROOT, f"notes/{sid}/syllabus")
        if os.path.exists(syl_dir):
            syl_files = []
            for root, dirs, files in os.walk(syl_dir):
                for f in sorted(files, key=natural_sort_key):
                    if f.endswith(('.docx', '.doc')):
                        continue
                    if f.endswith(('.pdf', '.png', '.jpg', '.jpeg', '.webp')):
                        f_full = os.path.join(root, f)
                        f_rel = os.path.relpath(f_full, REPO_ROOT).replace('\\', '/')
                        sz = os.path.getsize(f_full)
                        sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                        
                        file_id = f"{sid}-syllabus-{f.split('.')[0]}"
                        title = f"{s_obj['name']} Official Syllabus Document"
                        syl_files.append({
                            'id': file_id,
                            'title': title,
                            'originalName': f,
                            'path': f_rel,
                            'type': 'pdf' if f.endswith('.pdf') else 'png',
                            'sizeBytes': sz,
                            'size': sz_fmt
                        })
            if syl_files:
                units_list.append({
                    'unitNumber': 'Syllabus',
                    'title': 'Official Syllabus Document',
                    'isPractice': False,
                    'files': syl_files
                })

        # --- D. Solved PYQs Hub ---
        pyq_dir = os.path.join(REPO_ROOT, f"notes/{sid}/pyq")
        if os.path.exists(pyq_dir):
            pyq_files = []
            pyq_html = f"notes/{sid}/pyq/pyq-answers.html"
            if os.path.exists(os.path.join(REPO_ROOT, pyq_html)):
                sz = os.path.getsize(os.path.join(REPO_ROOT, pyq_html))
                pyq_files.append({
                    'id': f"{sid}-pyq-answers",
                    'title': "CIE-1 Solved PYQ Bank (Interactive)",
                    'originalName': "pyq-answers.html",
                    'path': pyq_html,
                    'type': 'pyq',
                    'sizeBytes': sz,
                    'size': f"{sz / 1024:.0f} KB",
                    'tag': "Solved PYQ Bank"
                })
            pyq_hw = f"notes/{sid}/pyq/handwritten/{sid}-pyq-handwritten.pdf"
            if os.path.exists(os.path.join(REPO_ROOT, pyq_hw)):
                sz = os.path.getsize(os.path.join(REPO_ROOT, pyq_hw))
                pyq_files.append({
                    'id': f"{sid}-pyq-handwritten",
                    'title': "Handwritten PYQ Solutions (PDF)",
                    'originalName': f"{sid}-pyq-handwritten.pdf",
                    'path': pyq_hw,
                    'type': 'handwritten',
                    'sizeBytes': sz,
                    'size': f"{sz / 1024:.0f} KB",
                    'tag': "Vector Handwritten"
                })
            if pyq_files:
                units_list.append({
                    'unitNumber': 'PYQ',
                    'title': 'CIE-1 PYQ Bank & Model Answers',
                    'isPractice': True,
                    'files': pyq_files
                })

        # --- E. Practice, Question Banks & Examination Papers ---
        prac_dir = os.path.join(REPO_ROOT, f"notes/{sid}/practice")
        if os.path.exists(prac_dir):
            prac_files = []
            for root, dirs, files in os.walk(prac_dir):
                for f in sorted(files, key=natural_sort_key):
                    if f.endswith(('.docx', '.doc')):
                        continue
                    if f.endswith(('.pdf', '.jpeg', '.jpg', '.png')):
                        f_full = os.path.join(root, f)
                        f_rel = os.path.relpath(f_full, REPO_ROOT).replace('\\', '/')
                        sz = os.path.getsize(f_full)
                        sz_fmt = f"{sz / 1024:.0f} KB" if sz < 1024 * 1024 else f"{sz / (1024 * 1024):.1f} MB"
                        
                        file_id = re.sub(r'[^a-z0-9]+', '-', f.lower()).strip('-')
                        file_id = f"{sid}-{file_id}"
                        title = clean_practice_title(f)
                        tag = "SEE Past Paper" if "see" in f.lower() else ("CIE Question Paper" if "cie" in f.lower() else "Practice")

                        prac_files.append({
                            'id': file_id,
                            'title': title,
                            'originalName': f,
                            'path': f_rel,
                            'type': 'pdf' if f.endswith('.pdf') else 'image',
                            'sizeBytes': sz,
                            'size': sz_fmt,
                            'tag': tag
                        })
            if prac_files:
                # Sort practice files: CIE first, then SEE
                prac_files.sort(key=lambda x: (0 if 'cie' in x['path'].lower() else 1, natural_sort_key(x['title'])))
                units_list.append({
                    'unitNumber': 'Practice',
                    'title': 'Practice, Question Banks & Examination Papers',
                    'isPractice': True,
                    'files': prac_files
                })

        s_obj['units'] = units_list
        new_subjects.append(s_obj)

    # Compute overall statistics
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

    # Strict Mojibake & Subject Title Consistency Audit Before Writing
    mojibake_re = re.compile(r'(Ã[^\s]|[Ââ€Æ’‚])')
    for s in new_subjects:
        sid = s['id']
        for u in s['units']:
            for f in u['files']:
                title = f.get('title', '')
                if mojibake_re.search(title):
                    raise ValueError(f"Mojibake detected in title: {title} ({f['path']})")
                # Cross-subject check
                if sid != 'se' and 'Requirements Engineering' in title:
                    raise ValueError(f"Cross-subject pollution detected: '{title}' in subject '{sid}'!")

    # Write output to data/subjects.js with universal JS export
    subjects_js_file = os.path.join(REPO_ROOT, 'data', 'subjects.js')
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

    js_content = header + json.dumps(final_data, indent=2, ensure_ascii=False) + ";" + footer

    with open(subjects_js_file, 'w', encoding='utf-8') as out_f:
        out_f.write(js_content)

    print(f"\nSuccessfully generated {subjects_js_file}!")
    print(f"Summary:")
    print(f"  Total Subjects: {len(new_subjects)}")
    print(f"  Total Registered Files: {total_files}")
    print(f"  Total Size: {total_size_mb}")
    for s in new_subjects:
        unit_counts = [f"{u['unitNumber']}: {len(u['files'])}f" for u in s['units']]
        total_sub_files = sum(len(u['files']) for u in s['units'])
        print(f"  - [{s['id']}] {s['name']}: {total_sub_files} files ({', '.join(unit_counts)})")

if __name__ == '__main__':
    sync_subjects()
