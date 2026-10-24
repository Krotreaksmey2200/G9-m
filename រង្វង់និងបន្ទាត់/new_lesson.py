#!/usr/bin/env python3
"""
Khmer Math Lesson Generator
Usage:
    python3 new_lesson.py <number> "<title>"
Example:
    python3 new_lesson.py 13 "អនុគមន៍ និងក្រាប"
"""

import sys
import os
import shutil
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_new_lesson(lesson_num_str, lesson_title):
    # Normalize number
    clean_num = re.sub(r'[^\d]', '', lesson_num_str) or lesson_num_str
    tex_filename = f"lesson_{clean_num}.tex"
    docx_filename = f"lesson_{clean_num}.docx"

    tex_target = os.path.join(BASE_DIR, tex_filename)
    docx_target = os.path.join(BASE_DIR, docx_filename)

    # 1. Create .tex file from lesson_template.tex
    template_tex_path = os.path.join(BASE_DIR, "lesson_template.tex")
    if os.path.exists(template_tex_path):
        with open(template_tex_path, 'r', encoding='utf-8') as f:
            tex_content = f.read()

        # Replace LessonNum and LessonTitle
        tex_content = re.sub(r'\\newcommand\{\\LessonNum\}\{.*?\}', f'\\\\newcommand{{\\\\LessonNum}}{{មេរៀនទី {clean_num}}}', tex_content)
        tex_content = re.sub(r'\\newcommand\{\\LessonTitle\}\{.*?\}', f'\\\\newcommand{{\\\\LessonTitle}}{{{lesson_title}}}', tex_content)

        with open(tex_target, 'w', encoding='utf-8') as f:
            f.write(tex_content)
        print(f"✅ Created LaTeX file: {tex_filename}")

    # 2. Create .docx using server.py export engine
    try:
        from live_editor.server import build_docx_from_data
        sample_data = {
            "lesson_num": f"មេរៀនទី {clean_num}",
            "lesson_title": lesson_title,
            "section_num": "១",
            "section_title": f"ចំណុចសំខាន់នៃ {lesson_title}",
            "subsec_title": "១.១ ខ្លឹមសារ និងនិយមន័យ",
            "teacher": "ក្រូត រស្មី",
            "phone": "070897540",
            "motto": "➤ ខំរៀនដើម្បីខ្លួនឯង និងអនាគតដ៏ភ្លឺស្វាង ➤",
            "theories": [
                f"ទ្រឹស្តីបទ ឬរូបមន្តសំខាន់ទី ១ ៖ $f(x) = ...$",
                f"ទ្រឹស្តីបទ ឬរូបមន្តសំខាន់ទី ២ ៖ $...$"
            ],
            "exercises": [
                {
                    "num": "01",
                    "text": "លំហាត់ទី ០១ ៖ គណនាតម្លៃ...",
                    "subs": [{"label": "គ", "text": "រូបមន្ត ៖ $...$"}]
                },
                {
                    "num": "02",
                    "text": "លំហាត់ទី ០២ ៖ ដោះស្រាយ...",
                    "subs": [
                        {"label": "ក", "text": "សំណួរទីមួយ"},
                        {"label": "ខ", "text": "សំណួរទីពីរ"}
                    ]
                }
            ]
        }
        docx_bytes = build_docx_from_data(sample_data)
        with open(docx_target, 'wb') as f:
            f.write(docx_bytes)
        print(f"✅ Created Word file with Microsoft Equations: {docx_filename}")
    except Exception as e:
        print(f"⚠️ Could not generate docx automatically: {e}")

    # 3. Automatically compile to PDF via XeLaTeX
    try:
        import subprocess
        env = os.environ.copy()
        env['TEXINPUTS'] = f'.:{BASE_DIR}:'
        cmd = ['xelatex', '-interaction=nonstopmode', tex_filename]
        res = subprocess.run(cmd, cwd=BASE_DIR, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Clean aux files
        clean_exts = ['.aux', '.log', '.out']
        for ext in clean_exts:
            aux_file = os.path.join(BASE_DIR, f"lesson_{clean_num}{ext}")
            if os.path.exists(aux_file):
                os.remove(aux_file)
        pdf_filename = f"lesson_{clean_num}.pdf"
        if os.path.exists(os.path.join(BASE_DIR, pdf_filename)):
            print(f"✅ Compiled PDF file (XeLaTeX): {pdf_filename}")
    except Exception as e:
        print(f"⚠️ Could not compile PDF: {e}")

    print("\n🎉 រួចរាល់! លោកគ្រូអាចបើកកែសម្រួល ឬប្រើ Live Editor នៅ http://localhost:8080 បានភ្លាមៗ!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 new_lesson.py <number> \"<title>\"")
        print("Example: python3 new_lesson.py 13 \"អនុគមន៍ និងក្រាប\"")
        sys.exit(1)

    num_arg = sys.argv[1]
    title_arg = sys.argv[2]
    create_new_lesson(num_arg, title_arg)
