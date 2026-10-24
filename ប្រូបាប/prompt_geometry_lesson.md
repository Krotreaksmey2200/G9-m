# គំរូ Master Prompt សម្រាប់បង្កើតមេរៀនធរណីមាត្រ (LaTeX KhmerMath)

ឯកសារនេះផ្ទុកនូវ **Master Prompt** ពេញលេញ សម្រាប់យកទៅប្រើប្រាស់ជាមួយ AI (Claude, ChatGPT, Gemini...) ដើម្បីបង្កើតឯកសារមេរៀនធរណីមាត្រថ្មីៗ (ថ្នាក់ទី៩ ឬកម្រិតផ្សេងទៀត) ឱ្យមានរចនាបថស្អាត ប្លង់សៀវភៅពុម្ពកូរ៉េ (Korean Math Textbook Style) ដូចគ្នាបេះបិទទៅនឹងឯកសារ `line_circle.tex`។

---

## ១. Master Prompt (ចម្លងផ្នែកខាងក្រោមនេះទៅដាក់ក្នុង AI)

```markdown
អ្នកគឺជាអ្នកជំនាញសរសេរកូដ LaTeX ឯកទេសខាងគណិតវិទ្យា និងរចនាប្លង់សៀវភៅពុម្ពគណិតវិទ្យាជាភាសាខ្មែរ (Korean Math Textbook Style)។
ភារកិច្ចរបស់អ្នក គឺបង្កើតឯកសារមេរៀនធរណីមាត្រពេញលេញមួយជាទម្រង់ LaTeX ដោយផ្អែកលើស្តង់ដារ និងរចនាបថដូចខាងក្រោម៖

---
### កម្រងរចនាសម្ព័ន្ធឯកសារ និង Preamble ស្តង់ដារ (LaTeX Configuration):
1. **Document Class & Geometry:**
   - ប្រើ `\documentclass[theme=teal]{khmermath}`
   - Geometry: `\geometry{left=0.85cm, right=0.85cm, top=0.75cm, bottom=1.5cm, footskip=0.7cm}`
2. **Packages & Libraries:**
   - `\usepackage{colortbl}`
   - `\usepackage{tikz}`
   - `\usetikzlibrary{calc,shapes,arrows,intersections,through,backgrounds,shadows,decorations.pathmorphing}`
   - `\usepackage{fancyhdr}`
   - Arc accent command: `\newcommand{\wideparen}[1]{\overset{\boldsymbol{\frown}}{#1}}`
3. **Color Palette (Korean Math Style):**
   - Teal Theme: `koreaTeal` (RGB: 0, 150, 155), `koreaDarkTeal` (RGB: 0, 105, 110), `brandNavy` (RGB: 0, 105, 110), `brandBlue` (RGB: 0, 150, 155)
   - Accent & Badges: `brandCrimson` (RGB: 195, 35, 60), `koreaOrange` (RGB: 235, 115, 30), `koreaPurple` (RGB: 125, 50, 160), `brandGold` (RGB: 215, 130, 10), `koreaYellow` (RGB: 255, 246, 175)
   - Backgrounds & Borders: `brandLightBlue` (RGB: 247, 244, 237), `brandTealBg` (RGB: 244, 252, 250), `cardBorder` (RGB: 220, 212, 198), `koreaNumber` (RGB: 115, 125, 135)
4. **Header & Footer Setup (Fancyhdr):**
   - `\pagestyle{fancy}`
   - `\renewcommand{\headrulewidth}{0pt}`
   - `\renewcommand{\footrule}{\color{koreaTeal!60}\hrule height 0.6pt\vspace{3pt}}`
   - Footer ឆ្វេង: `\fancyfoot[L]{\fontsize{8.5}{8.5}\selectfont\kml \color{koreaNumber}\textbf{\thepage}\ \vline\ \color{koreaDarkTeal}\textbf{[លេខមេរៀន]. [ចំណងជើងមេរៀន]}}`
   - Footer កណ្ដាល: `\fancyfoot[C]{\fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{\ding{72}\ បង្រៀនដោយ ៖ \textcolor{koreaDarkTeal}{ក្រូត រស្មី}\ \ding{72}}}`
   - Footer ស្ដាំ: `\fancyfoot[R]{\fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{ Telegram: \textcolor{brandCrimson}{070897540}}\ \vline\ \color{koreaNumber}\textbf{\thepage}}`
5. **Custom Macros & Badges ត្រូវតែមាន:**
   - **Header Banner:**
     ```latex
     \newcommand{\koreanheader}[2]{%
       \noindent%
       \begin{tikzpicture}[x=1cm, y=1cm]
         \fill[koreaTeal, rounded corners=12pt] (0, 0.1) -- (0, 0.95) -- (3.8, 0.95) [rounded corners=0pt] -- (4.4, 0.1) -- cycle;
         \node[white, font=\fontsize{11}{11}\selectfont\kml\bfseries] at (1.9, 0.52) {#1};
         \node[anchor=west, font=\fontsize{18}{18}\selectfont\kml\bfseries, color=koreaDarkTeal] at (4.6, 0.42) {#2};
         \node[anchor=east, font=\fontsize{8.5}{8.5}\selectfont\kby, color=gray!80] at (19.2, 0.48) {$>$ ក្លឹបសិក្សាគណិតវិទ្យា ភី ស៊ី​ អឹម};
       \end{tikzpicture}%
       \vspace{3pt}%
     }
     ```
   - **Section & Subsection:**
     - `\khsection{[លេខ]}{[ចំណងជើងផ្នែកធំ]}`
     - `\khsubsection{[លេខ.លេខ]}{[ចំណងជើងរង]}`
   - **ប្រអប់ទ្រឹស្ដី/រូបមន្ត (Rule Box):**
     - `\begin{khboxorange} ... \end{khboxorange}` មាន title: `\ding{72}\ ជាទូទៅ`
   - **កាតពន្យល់ទ្រឹស្ដី (Concept Card):**
     - `\begin{khcard}` ចែកជា ២ minipages (ខាងឆ្វេង 0.68\textwidth ពន្យល់អត្ថបទ និងខាងស្ដាំ 0.30\textwidth ជារូបគំនូរ TikZ)
   - **លេខរៀងលំហាត់ស្ទីលកូរ៉េ (Big Styled Number):**
     - `\exhead{1}`, `\exhead{2}`, ... ដោយប្រើម៉ាក្រូ `\koreannum`
   - **ស្លាកកម្រិតលំហាត់ (Difficulty Badges):**
     - `\badgebasic` (គ្រឹះ), `\badgestandard` (មធ្យម), `\badgeadvanced` (ជឿនលឿន), `\badgesolution` (ស្រាយបញ្ជាក់), `\phead` (ប្រតិបត្តិ)

---
### គោលការណ៍រៀបចំខ្លឹមសារ (Pedagogical & Layout Rules):
1. **ប្លង់លំហាត់ (Two-Column Multicols Layout):**
   - ប្រើ `\begin{multicols}{2}` មានបន្ទាត់ខណ្ឌកណ្ដាល `\columnseprule=0.5pt` និង `\def\columnseprulecolor{\color{koreaTeal!40}}`។
   - លំហាត់នីមួយៗត្រូវផ្ដើមដោយ `\exhead{X}` អមដោយសំណួរច្បាស់លាស់ និងរូបគំនូរ TikZ នៅចំកណ្ដាល (`\begin{center}\begin{tikzpicture}...\end{tikzpicture}\end{center}`)។
   - បើជួរបាក់មិនស្មើគ្នា អាចប្រើ `\columnbreak` ដើម្បីទម្លាក់ទៅជួរឈរបន្ទាប់។
2. **គំនូរធរណីមាត្រ TikZ (Geometrical Precision):**
   - ត្រូវគណនា និងកំណត់ Coordinate ឱ្យបានត្រឹមត្រូវតាមទ្រឹស្ដីធរណីមាត្រពិតប្រាកដ។
   - សញ្ញាកែង (Right angle) ត្រូវប្រើ TikZ calc library:
     `\draw[color=brandCrimson, line width=0.5pt] ($(M)!0.12cm!(B)$) -- ($($(M)!0.12cm!(B)$)+($(M)!0.12cm!(O)$)-(M)$) -- ($(M)!0.12cm!(O)$);`
   - បន្ទាត់ជំនួយ/កាំត្រូវប្រើ `dotted` និងពណ៌ `brandCrimson` ឬ `brandBlue`។
   - ឈ្មោះចំណុច (A, B, C, O) ត្រូវកំណត់ node [above], [below], [left], [right] ឱ្យច្បាស់ មិនជាន់លើបន្ទាត់។
3. **អក្ខរាវិរុទ្ធខ្មែរ និងរូបមន្តគណិតវិទ្យា:**
   - សញ្ញាខណ្ឌ `។` និងសញ្ញាចុចពីរ `៖` ត្រូវមានដកឃ្លាមុន និងក្រោយជានិច្ច។
   - ខ្នាតប្រវែងត្រូវសរសេរក្នុង Math mode ដូចជា $10\text{cm}$, $5\text{m}$, មុំ $\angle ABC = 60^\circ$។

---
### ព័ត៌មានលម្អិតនៃមេរៀនដែលត្រូវបង្កើត (សូមបំពេញព័ត៌មានខាងក្រោម)៖
- **លេខមេរៀន និងចំណងជើង:** [ឧទាហរណ៍៖ មេរៀនទី ១៣ ៖ មុំក្នុងរង្វង់]
- **ចំណងជើងផ្នែកធំ (Sections) និងចំណុចរង (Subsections):**
  1. [ផ្នែកទី ១...]
  2. [ផ្នែកទី ២...]
- **ខ្លឹមសារទ្រឹស្ដី/រូបមន្តដែលត្រូវសង្ខេបដាក់ក្នុងប្រអប់ «ជាទូទៅ»:**
  - [...]
- **ចំនួនលំហាត់ និងកម្រិតលំហាត់:** [ឧទាហរណ៍៖ ៨ ទៅ ១២ លំហាត់ ចែកជា ២ ជួរឈរ មានរូបគំនូរ TikZ គ្រប់លំហាត់]

សូមសរសេរកូដ LaTeX ពេញលេញ ចាប់ពី `\documentclass` រហូតដល់ `\end{document}` ដោយមិនកាត់ ឬសរសេរ `...` នៅកណ្ដាលកូដឡើយ។
```

---

## ២. ឧទាហរណ៍ជាក់ស្ដែងនៃការបំពេញ Prompt

### ឧទាហរណ៍ទី ១៖ មេរៀន «មុំក្នុងរង្វង់»
> **លេខមេរៀន និងចំណងជើង:** មេរៀនទី ១៣ ៖ មុំក្នុងរង្វង់  
> **ចំណងជើងផ្នែកធំ:**  
> - ផ្នែក ១ ៖ មុំផ្ចិត និងធ្នូស្ទាក់  
> - ផ្នែក ២ ៖ មុំចារឹកក្នុងរង្វង់  
> - ផ្នែក ៣ ៖ មុំចារឹកក្នុងកន្លះរង្វង់  
> **ខ្លឹមសារទ្រឹស្ដី:**  
> - រង្វាស់មុំផ្ចិតស្មើនឹងរង្វាស់ធ្នូស្ទាក់  
> - រង្វាស់មុំចារឹកក្នុងរង្វង់ស្មើពាក់កណ្ដាលនៃរង្វាស់ធ្នូស្ទាក់ (ឬពាក់កណ្ដាលមុំផ្ចិត)  
> - មុំចារឹកក្នុងកន្លះរង្វង់ជាមុំកែង ($90^\circ$)  
> **ចំនួនលំហាត់:** លំហាត់ចំនួន ៨ រៀបចំជា ២ ជួរឈរ (multicols) មានគំនូរ TikZ បង្ហាញរង្វង់ និងមុំ រួចឱ្យសិស្សរកតម្លៃ $x$, $y$ ឬរង្វាស់មុំនីមួយៗ។

---

### ឧទាហរណ៍ទី ២៖ មេរៀន «ទ្រឹស្ដីបទពីតាគ័រ»
> **លេខមេរៀន និងចំណងជើង:** មេរៀនទី ៨ ៖ ទ្រឹស្ដីបទពីតាគ័រ  
> **ចំណងជើងផ្នែកធំ:**  
> - ផ្នែក ១ ៖ ទ្រឹស្ដីបទពីតាគ័រ  
> - ផ្នែក ២ ៖ ចម្រាសទ្រឹស្ដីបទពីតាគ័រ  
> **ខ្លឹមសារទ្រឹស្ដី:**  
> - ក្នុងត្រីកោណកែង ការ៉េនៃអ៊ីប៉ូតេនុសស្មើផលបូកការ៉េនៃជ្រុងជាប់មុំកែង ($BC^2 = AB^2 + AC^2$)  
> - បើ $BC^2 = AB^2 + AC^2$ នោះត្រីកោណ $ABC$ ជាត្រីកោណកែងត្រង់ $A$  
> **ចំនួនលំហាត់:** លំហាត់ចំនួន ៨ មានរូបត្រីកោណកែង TikZ ដែលស្គាល់ជ្រុងពីរ រួចឱ្យគណនាជ្រុងទីបី និងចំណោទអនុវត្តជាក់ស្ដែង។

---

## ៣. ការចងក្រង (Compile) ឯកសារ
ដើម្បីចងក្រងឯកសារចេញជា PDF ឱ្យបានត្រឹមត្រូវ៖
1. ត្រូវប្រាកដថាឯកសារ `khmermath.cls` ស្ថិតនៅក្នុង Folder ជាមួយឯកសារ `.tex`។
2. ត្រូវ compile ដោយប្រើ **XeLaTeX** (ពីព្រោះវាគាំទ្រពុម្ពអក្សរខ្មែរ Unicode បានយ៉ាងល្អឥតខ្ចោះ)។
