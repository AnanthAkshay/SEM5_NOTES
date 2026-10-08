#!/usr/bin/env python3
"""
SEM 5 · ISE Notes - Global Search Index Generator

Scans all 24 HTML study notes across all 8 subjects (AI, CN, EVS, ML, ReactJS, RMIPR, SE, TOC),
extracts all sections, titles, subsections, and key concepts, and generates:
- data/notes-index.json
- data/notes-index.js (for direct browser script inclusion)
"""

import os
import json
import re
from html.parser import HTMLParser

SUBJECT_METADATA = [
    {"id": "ai", "units": [1, 2, 3]},
    {"id": "cn", "units": [1, 2, 3]},
    {"id": "evs", "units": [1, 2, 3]},
    {"id": "ml", "units": [1, 2, 3]},
    {"id": "reactjs", "units": [1, 2, 3]},
    {"id": "rmipr", "units": [1, 2, 3]},
    {"id": "se", "units": [1, 2, 3]},
    {"id": "toc", "units": [1, 2, 3]},
]

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
            # Clean unit title
            t = re.sub(r"^Unit\s+\d+:\s*", "", self.text_buf.strip(), flags=re.IGNORECASE)
            self.unit_title = t
        elif tag == "h2" and self.in_h2:
            self.in_h2 = False
            if self.curr_sec:
                # Remove leading section numbers like "1.1 " or "Section 1: "
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
    print("Building global search index for all 24 units...")

    for sub in SUBJECT_METADATA:
        sub_id = sub["id"]
        for u in sub["units"]:
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
                
                # Limit keywords to top 15 most relevant
                keywords = sec["keywords"][:15]

                entry = {
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

    print(f"Total indexed section records: {len(index_entries)}")

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
