#!/usr/bin/env python3
"""
SEM 5 · ISE Notes - Global Search Index Generator (CIE-1 Scope)

Scans in-scope HTML notes, PYQ question banks, and handwritten PDF notebooks
based strictly on data/scope.json and generates:
- data/notes-index.json
- data/notes-index.js (for direct browser script inclusion)
"""

import os
import json
import re
from html.parser import HTMLParser

class NoteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.curr_sec = None
        self.unit_title = ""
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.in_strong = False
        self.text_buf = ""

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "h1" and not self.unit_title:
            self.in_h1 = True
            self.text_buf = ""
        elif tag == "section" and "id" in attr_dict:
            self.curr_sec = {
                "id": attr_dict["id"],
                "title": "",
                "subsections": [],
                "keywords": []
            }
            self.sections.append(self.curr_sec)
        elif tag == "h2" and self.curr_sec:
            self.in_h2 = True
            self.text_buf = ""
        elif tag == "h3" and self.curr_sec:
            self.in_h3 = True
            self.text_buf = ""
        elif tag == "strong" and self.curr_sec:
            self.in_strong = True
            self.text_buf = ""

    def handle_endtag(self, tag):
        if tag == "h1" and self.in_h1:
            self.in_h1 = False
            t = re.sub(r"^Unit\s+\d+:\s*", "", self.text_buf.strip(), flags=re.IGNORECASE)
            self.unit_title = t
        elif tag == "h2" and self.in_h2:
            self.in_h2 = False
            if self.curr_sec:
                clean_title = re.sub(r"^\d+(\.\d+)*\s*[:.-]?\s*", "", self.text_buf.strip())
                self.curr_sec["title"] = clean_title or self.text_buf.strip()
        elif tag == "h3" and self.in_h3:
            self.in_h3 = False
            if self.curr_sec and self.text_buf.strip():
                clean_sub = re.sub(r"^\d+(\.\d+)*\s*[:.-]?\s*", "", self.text_buf.strip())
                self.curr_sec["subsections"].append(clean_sub or self.text_buf.strip())
        elif tag == "strong" and self.in_strong:
            self.in_strong = False
            clean = self.text_buf.strip().rstrip(":")
            if self.curr_sec and 3 <= len(clean) <= 40 and clean not in self.curr_sec["keywords"]:
                if not any(clean.lower().startswith(skip) for skip in ["note:", "warning:", "tip:", "important:"]):
                    self.curr_sec["keywords"].append(clean)

    def handle_data(self, data):
        if self.in_h1 or self.in_h2 or self.in_h3 or self.in_strong:
            self.text_buf += data


def build_index():
    index_entries = []
    print("Building global search index for CIE-1 scope...")

    with open("data/scope.json", "r", encoding="utf-8") as f:
        scope = json.load(f)

    subjects = scope.get("subjects", {})

    for sub_id, sub_info in subjects.items():
        in_scope_units = sub_info.get("in_scope_units", [])
        sub_name = sub_info.get("short_name", sub_id.upper())

        # 1. Notes Sections & Unit Handwritten Notebooks
        for u in in_scope_units:
            note_path = f"notes/{sub_id}/unit{u}/unit-{u}-notes.html"
            if not os.path.exists(note_path):
                print(f"[WARN] Missing note file: {note_path}")
                continue

            with open(note_path, "r", encoding="utf-8") as f:
                content = f.read()

            parser = NoteParser()
            parser.feed(content)

            unit_title = parser.unit_title or f"Unit {u}"

            for sec in parser.sections:
                sec_id = sec["id"]
                title = sec["title"] or f"Section {sec_id}"
                keywords = sec["keywords"][:15]

                entry = {
                    "type": "note-section",
                    "subject": sub_id,
                    "unit": u,
                    "unitTitle": unit_title,
                    "sectionId": sec_id,
                    "title": title,
                    "subsections": sec["subsections"],
                    "keywords": keywords,
                    "path": f"notes/{sub_id}/unit{u}/unit-{u}-notes.html#{sec_id}"
                }
                index_entries.append(entry)

            # Handwritten Notebook entry for Unit
            hw_path = f"notes/{sub_id}/unit{u}/handwritten/{sub_id}-unit{u}-handwritten.pdf"
            if os.path.exists(hw_path):
                index_entries.append({
                    "type": "handwritten",
                    "subject": sub_id,
                    "unit": u,
                    "unitTitle": unit_title,
                    "title": f"{sub_name} Unit {u} Handwritten Notebook (PDF)",
                    "subsections": [f"{sub_name} Unit {u} handwritten notes"],
                    "keywords": [sub_id, f"unit{u}", "handwritten", "pdf", "notebook"],
                    "path": hw_path
                })

        # 2. PYQ Questions & PYQ Handwritten Notebook
        pyq_json_path = f"data/pyq/{sub_id}.json"
        if os.path.exists(pyq_json_path):
            with open(pyq_json_path, "r", encoding="utf-8") as f:
                pyq_data = json.load(f)

            in_scope_questions = pyq_data.get("in_scope_questions", [])
            for q in in_scope_questions:
                q_id = q.get("id", "")
                q_text = q.get("question", "")
                q_clean = re.sub(r"<[^>]+>", "", q_text).strip()
                q_unit = q.get("unit", 1)
                q_marks = q.get("marks", "")
                q_exam = q.get("exam", "")
                q_sec = q.get("syllabus_section", "")

                keywords = [sub_id, f"unit{q_unit}", "pyq", q_id]
                if q_exam:
                    keywords.append(q_exam.lower())
                if q_marks:
                    keywords.append(str(q_marks).lower())

                index_entries.append({
                    "type": "pyq",
                    "subject": sub_id,
                    "unit": q_unit,
                    "unitTitle": f"Unit {q_unit} PYQ",
                    "sectionId": q_sec,
                    "questionId": q_id,
                    "title": q_clean,
                    "marks": q_marks,
                    "exam": q_exam,
                    "subsections": [f"{q_exam} ({q_marks})" if q_exam else ""],
                    "keywords": keywords,
                    "path": f"notes/{sub_id}/pyq/pyq-answers.html#{q_id}"
                })

            # PYQ Handwritten Notebook entry
            pyq_hw_path = f"notes/{sub_id}/pyq/handwritten/{sub_id}-pyq-handwritten.pdf"
            if os.path.exists(pyq_hw_path):
                index_entries.append({
                    "type": "handwritten",
                    "subject": sub_id,
                    "unit": "PYQ",
                    "unitTitle": "CIE-1 Solved PYQs",
                    "title": f"{sub_name} CIE-1 Solved PYQs Handwritten Notebook (PDF)",
                    "subsections": [f"{sub_name} PYQ model answers handwritten notes"],
                    "keywords": [sub_id, "pyq", "handwritten", "pdf", "solved pyqs", "cie1"],
                    "path": pyq_hw_path
                })

    # 3. Every Registered File from data/subjects.js
    try:
        with open("data/subjects.js", "r", encoding="utf-8") as f:
            content = f.read()
        m = re.search(r"window\.SEM5_DATA\s*=\s*(\{[\s\S]*?\n\});", content)
        if m:
            subjects_data = json.loads(m.group(1))
            indexed_paths = {e.get("path") for e in index_entries}
            for s in subjects_data.get("subjects", []):
                sid = s["id"]
                s_name = s.get("shortName", sid.upper())
                for u in s.get("units", []):
                    u_num = u.get("unitNumber", "")
                    u_title = u.get("title", "")
                    for f in u.get("files", []):
                        f_path = f.get("path", "")
                        if not f_path or f_path in indexed_paths:
                            continue
                        indexed_paths.add(f_path)
                        f_title = f.get("title", "")
                        keywords = [sid, s_name.lower(), str(u_num).lower(), f.get("type", "")]
                        if f.get("tag"):
                            keywords.append(f.get("tag").lower())
                        index_entries.append({
                            "type": "file",
                            "subject": sid,
                            "unit": u_num,
                            "unitTitle": u_title,
                            "title": f_title,
                            "subsections": [f"{s_name} · {u_title}"],
                            "keywords": keywords,
                            "path": f_path
                        })
    except Exception as e:
        print(f"Error indexing subjects.js files: {e}")

    print(f"Total indexed CIE-1 records: {len(index_entries)}")

    # Write data/notes-index.json
    with open("data/notes-index.json", "w", encoding="utf-8") as f:
        json.dump(index_entries, f, indent=2, ensure_ascii=False)
    print("Wrote data/notes-index.json")

    # Write data/notes-index.js
    with open("data/notes-index.js", "w", encoding="utf-8") as f:
        f.write("window.SEM5_NOTES_INDEX = ")
        json.dump(index_entries, f, ensure_ascii=False)
        f.write(";\n")
    print("Wrote data/notes-index.js")

if __name__ == "__main__":
    build_index()
