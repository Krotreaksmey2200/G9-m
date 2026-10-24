---
name: skill_for_lesson
description: "បង្កើតឯកសារមេរៀន និងលំហាត់គណិតវិទ្យាជាទម្រង់ LaTeX (Korean Math Textbook Style) ដោយផ្អែកលើស្តង់ដារនៃឯកសារ សមមាត្រ.tex។ ប្រើនៅពេលដែលអ្នកប្រើប្រាស់ចង់បង្កើតមេរៀន សន្លឹកកិច្ចការ ឬសង្ខេបមេរៀនគណិតវិទ្យាថ្មីៗ។"
---

# Skill for Khmer Math Lesson (Korean Math Textbook Style)

ជំនាញនេះប្រើសម្រាប់បង្កើតកូដ LaTeX សម្រាប់សន្លឹកកិច្ចការ និងសង្ខេបមេរៀនគណិតវិទ្យាជាភាសាខ្មែរ តាមរចនាបថសៀវភៅពុម្ពកូរ៉េ (Korean Math Textbook Style) ដូចគ្នានឹង [សមមាត្រ.tex](file:///Users/heng/Documents/%E1%9E%AF%E1%9E%80%E1%9E%9F%E1%9E%9C%E1%9E%94%E1%9E%84%E1%9F%92%E1%9E%9A%E1%9F%80%E1%9E%93/%E1%9E%82%E1%9E%8E%E1%9E%B7%E1%9E%8F%E1%9E%91%E1%9E%B8%E1%9F%A9/%E1%9E%9F%E1%9E%98%E1%9E%98%E1%9E%B6%E1%9E%8F%E1%9F%92%E1%9E%9A/%E1%9E%9F%E1%9E%98%E1%9E%98%E1%9E%B6%E1%9E%8F%E1%9F%92%E1%9E%9A.tex)។

## គោលការណ៍សំខាន់ៗពេលបង្កើតមេរៀន៖

1. **Document Class & Layout:**
   - `\documentclass[theme=teal,16pt]{khmermath}`
   - `\usepackage{needspace, colortbl, tikz, fancyhdr, multicol, tcolorbox}`
   - Geometry តឹងណែន និងសន្សំសំចៃទំព័រ៖
     `\geometry{left=0.5cm, right=0.5cm, top=0.55cm, bottom=1.0cm, footskip=0.55cm}`

2. **Colors & Design System:**
   - បណ្ដុំពណ៌ចម្បង៖ `koreaTeal`, `koreaDarkTeal`, `brandNavy`, `brandCrimson`, `koreaOrange`, `koreaYellow`, `brandTealBg`, `brandLightBlue`។
   - ពណ៌អក្សររូបមន្ត Math Mode ប្រើពណ៌ខៀវ (`\everymath{\color{blue}}`)។

3. **សមាសធាតុ Header & Footer:**
   - ប្រើ `fancyhdr` ដោយមានបន្ទាត់ footrule ពណ៌ `koreaTeal!60`។
   - ខាងឆ្វេង៖ លេខទំព័រ និងឈ្មោះមេរៀន។
   - កណ្ដាល៖ ព័ត៌មានគ្រូបង្រៀន (`បង្រៀនដោយ ៖ ក្រូត រស្មី`)។
   - ស្ដាំ៖ ព័ត៌មានទំនាក់ទំនង (`Telegram: 070897540`)។

4. **រចនាសម្ព័ន្ធមេរៀន (Lesson Architecture):**
   - **Header Banner:** `\koreanheader{[លេខមេរៀន]}{[ចំណងជើងមេរៀន]}`
   - **Section:** `\khsection{[លេខ]}{[ចំណងជើងផ្នែកធំ]}`
   - **ប្រអប់ទ្រឹស្ដី «ជាទូទៅ»:** `\begin{khboxorange}` ចែកជា 2 minipages (ខាងឆ្វេងរូបមន្តសង្ខេប, ខាងស្ដាំដ្យាក្រាម/រូបតំណាង TikZ)។
   - **លំហាត់ ២ ជួរឈរ:** ប្រើ `\begin{multicols}{2}`។
   - **ចំណាត់ថ្នាក់ប្រភេទ:** `\khtype{ប្រភេទទី ... ៖ ...}`។
   - **លេខលំហាត់គ្រូ:** `\phead{01}`, `\phead{02}`...
   - **លេខលំហាត់សិស្ស:** `\pheadDIY{03}`, `\pheadDIY{04}`...
   - **ស្លាកគន្លឹះចម្លើយ:** `\centerline{\khbadge{...}}` នៅក្រោមលំហាត់សំខាន់ៗ។
