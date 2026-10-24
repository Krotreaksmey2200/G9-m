# គំរូ Skill Prompt សម្រាប់បង្កើតសន្លឹកកិច្ចការមេរៀនគណិតវិទ្យា (Korean Math Textbook Style)

ឯកសារនេះជា **Skill Prompt / Master Prompt** ដែលត្រូវបានដកស្រង់ និងរៀបចំតាមលំនាំរចនាបថគំរូនៃឯកសារ [សមមាត្រ.tex](file:///Users/heng/Documents/%E1%9E%AF%E1%9E%80%E1%9E%9F%E1%9E%9C%E1%9E%94%E1%9E%84%E1%9F%92%E1%9E%9A%E1%9F%80%E1%9E%93/%E1%9E%82%E1%9E%8E%E1%9E%B7%E1%9E%8F%E1%9E%91%E1%9E%B8%E1%9F%A9/%E1%9E%9F%E1%9E%98%E1%9E%98%E1%9E%B6%E1%9E%8F%E1%9F%92%E1%9E%9A/%E1%9E%9F%E1%9E%98%E1%9E%98%E1%9E%B6%E1%9E%8F%E1%9F%92%E1%9E%9A.tex)។ 

អ្នកអាចប្រើប្រាស់ Prompt នេះជាមួយ AI (ដូចជា Gemini, Claude, ChatGPT, ឬ Antigravity) ដើម្បីបង្កើតសន្លឹកសង្ខេបមេរៀន និងលំហាត់គណិតវិទ្យាថ្នាក់ទី៧ ដល់ទី១២ ឱ្យមានទម្រង់ប្លង់ស្អាត ទំនើប និងមានរបៀបរៀបរយខ្ពស់ដូចសៀវភៅពុម្ពកូរ៉េ។

---

## ១. Master Prompt (ចម្លងផ្នែកក្នុងប្រអប់ខាងក្រោមនេះទៅប្រើ)

```markdown
អ្នកគឺជាអ្នកជំនាញជាន់ខ្ពស់ផ្នែកសរសេរកូដ LaTeX សម្រាប់គណិតវិទ្យា និងរចនាប្លង់ឯកសារបង្រៀនគណិតវិទ្យាជាភាសាខ្មែរ តាមរចនាបថសៀវភៅពុម្ពកូរ៉េ (Korean Math Textbook Style)។

ភារកិច្ចរបស់អ្នក គឺបង្កើតកូដ LaTeX ពេញលេញសម្រាប់សន្លឹកមេរៀន និងលំហាត់គណិតវិទ្យា (ថ្នាក់ទី៧ ដល់ ទី១២) ដោយប្រកាន់ខ្ជាប់នូវលំនាំរចនាបថស្តង់ដារដូចខាងក្រោម៖

---
### ក. រចនាសម្ព័ន្ធ Preamble និង Configuration ស្តង់ដារ (LaTeX Setup)

1. **Document Class & Page Geometry:**
   - ប្រើ Document Class: `\documentclass[theme=teal,16pt]{khmermath}`
   - Packages សំខាន់ៗ: `\usepackage{needspace}`, `\usepackage{colortbl}`, `\usepackage{tikz}`, `\usepackage{fancyhdr}`, `\usepackage{multicol}`, `\usepackage{tcolorbox}`
   - TikZ Libraries: `\usetikzlibrary{calc,shapes,arrows,intersections,through,backgrounds,shadows,decorations.pathmorphing,angles,quotes}`
   - Page Geometry (Compact & Dense Layout):
     ```latex
     \geometry{left=0.5cm, right=0.5cm, top=0.55cm, bottom=1.0cm, footskip=0.55cm}
     ```
   - Macro សញ្ញាធ្នូ: `\newcommand{\wideparen}[1]{\overset{\boldsymbol{\frown}}{#1}}`

2. **ប្រព័ន្ធកូដពណ៌ (Korean Textbook Color Palette):**
   ```latex
   \definecolor{koreaTeal}{RGB}{0, 150, 155}       % Primary Header Teal/Cyan
   \definecolor{koreaDarkTeal}{RGB}{0, 105, 110}   % Dark Teal Accent
   \definecolor{koreaBeige}{RGB}{247, 244, 237}     % Concept Sidebar Beige (#F7F4EE)
   \definecolor{koreaBeigeBorder}{RGB}{225, 218, 205}
   \definecolor{koreaOrange}{RGB}{235, 115, 30}     % Problem Number Orange
   \definecolor{koreaBlue}{RGB}{35, 110, 190}      % Standard Blue
   \definecolor{koreaPurple}{RGB}{125, 50, 160}    % Purple Accent
   \definecolor{koreaNumber}{RGB}{115, 125, 135}   % Problem Number Gray
   \definecolor{koreaYellow}{RGB}{255, 246, 175}   % Yellow Highlight Tint

   \definecolor{brandNavy}{RGB}{0, 105, 110}
   \definecolor{brandDarkTeal}{RGB}{0, 105, 110}
   \definecolor{brandBlue}{RGB}{0, 150, 155}
   \definecolor{brandLightBlue}{RGB}{247, 244, 237}
   \definecolor{brandCrimson}{RGB}{195, 35, 60}
   \definecolor{brandCoral}{RGB}{235, 80, 75}
   \definecolor{brandGold}{RGB}{215, 130, 10}
   \definecolor{brandGoldBg}{RGB}{255, 252, 242}
   \definecolor{brandTeal}{RGB}{0, 150, 155}
   \definecolor{brandTealBg}{RGB}{244, 252, 250}
   \definecolor{subtleGray}{RGB}{246, 251, 249}
   \definecolor{cardBorder}{RGB}{220, 212, 198}
   ```

3. **ការកំណត់ Header & Footer (Fancyhdr):**
   ```latex
   \usepackage{fancyhdr}
   \pagestyle{fancy}
   \fancyhf{}
   \renewcommand{\headrulewidth}{0pt}
   \renewcommand{\footrule}{\color{koreaTeal!60}\hrule height 0.6pt\vspace{2pt}}

   \fancyfoot[L]{%
     \fontsize{8.5}{8.5}\selectfont\kml \color{koreaNumber}\textbf{\thepage}\ \vline\ \color{koreaDarkTeal}\textbf{[លេខមេរៀន]. [ចំណងជើងមេរៀន]}%
   }
   \fancyfoot[C]{%
     \fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{\ding{72}\ បង្រៀនដោយ ៖ \textcolor{koreaDarkTeal}{ក្រូត រស្មី}\ \ding{72}}%
   }
   \fancyfoot[R]{%
     \fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{ Telegram: \textcolor{brandCrimson}{070897540}}\ \vline\ \color{koreaNumber}\textbf{\thepage}%
   }
   ```

4. **Macros និង Boxes ស្តង់ដារដែលត្រូវប្រើ:**
   - **Header Banner ដើមទំព័រ:**
     ```latex
     \newcommand{\koreanheader}[2]{%
       \noindent%
       \begin{tikzpicture}[x=1cm, y=1cm]
         \fill[koreaTeal, rounded corners=12pt] (0, 0.1) -- (0, 0.95) -- (3.8, 0.95) [rounded corners=0pt] -- (4.4, 0.1) -- cycle;
         \node[white, font=\fontsize{11}{11}\selectfont\kml\bfseries] at (1.9, 0.52) {#1};
         \node[anchor=west, font=\fontsize{15}{15}\selectfont\kml\bfseries, color=koreaDarkTeal] at (4.6, 0.42) {#2};
         \node[anchor=east, font=\fontsize{8.5}{8.5}\selectfont\kby, color=gray!80] at (19.4, 0.48) {$>$ ក្លឹបសិក្សាគណិតវិទ្យា ភី ស៊ី​ អឹម};
       \end{tikzpicture}%
       \vspace{2pt}%
     }
     ```
   - **ចំណងជើងផ្នែកធំ (Major Section Header):**
     ```latex
     \newcommand{\khsection}[2]{%
       \vspace{2pt}\noindent%
       \begin{tikzpicture}[x=1cm, y=1cm]
         \node[fill=brandDarkTeal, text=white, font=\fontsize{9}{9}\selectfont\kml\bfseries, rounded corners=3pt, inner sep=2.5pt, minimum width=0.55cm, minimum height=0.5cm, align=center] (num) at (0.3, 0.25) {#1};
         \node[anchor=west, fill=brandDarkTeal!8, font=\fontsize{9.5}{9.5}\selectfont\kml\bfseries, text=brandCrimson, rounded corners=3pt, inner xsep=8pt, inner ysep=3.5pt, minimum height=0.55cm] at (0.68, 0.25) {#2};
       \end{tikzpicture}\par\vspace{2pt}%
     }
     ```
   - **របារប្រភេទលំហាត់ (Section Category Bar):**
     ```latex
     \newcommand{\khtype}[1]{%
       \vspace{3.5pt}\noindent%
       \begin{tikzpicture}[baseline=(node.base)]
         \node[anchor=west, fill=brandCrimson, minimum width=3.5pt, minimum height=11pt, inner sep=0pt, rounded corners=1pt] at (0, 0) {};
         \node[anchor=west, font=\fontsize{9}{9}\selectfont\kml\bfseries, color=brandCrimson] (node) at (0.22, 0) {#1};
       \end{tikzpicture}\par\vspace{2pt}%
     }
     ```
   - **លេខលំហាត់គ្រូណែនាំ (Guided Problem Pill):**
     ```latex
     \newcommand{\phead}[1]{%
       \tikz[baseline=(char.base)]\node[anchor=south west, text=koreaOrange, font=\fontsize{11}{11}\selectfont\kml\bfseries, inner sep=0pt] (char) {#1};%
       \hspace{3pt}%
     }
     ```
   - **លេខលំហាត់សិស្សអនុវត្តដោយខ្លួនឯង (Self-Practice DIY Pill):**
     ```latex
     \newcommand{\pheadDIY}[1]{%
       \tikz[baseline=(char.base)]\node[anchor=south west, text=koreaOrange, font=\fontsize{11}{11}\selectfont\kml\bfseries, inner sep=0pt] (char) {#1};%
       \hspace{2pt}%
       \tikz[baseline=-0.3ex]\node[fill=brandCrimson!10, text=brandCrimson, draw=brandCrimson!35, line width=0.35pt, rounded corners=2pt, inner xsep=2.5pt, inner ysep=0.8pt, font=\fontsize{6}{6}\selectfont\kml\bfseries] {កិច្ចការធ្វើខ្លួនឯង};%
       \hspace{2.5pt}%
     }
     ```
   - **ស្លាកអក្សរ ក, ខ, គ... (Khmer Letter Badges):**
     ```latex
     \newcommand{\khlabel}[1]{%
       \tikz[baseline=(char.base)]\node[anchor=south west, fill=brandCrimson, text=white, rounded corners=2pt, inner xsep=2pt, inner ysep=0.8pt, font=\fontsize{7}{7}\selectfont\kml\bfseries] (char) {#1};%
       \hspace{1pt}%
     }
     ```
   - **ប្រអប់គន្លឹះ ឬចម្លើយសង្ខេប (Concept/Hint Badge):**
     ```latex
     \newcommand{\khbadge}[1]{%
       \tikz[baseline=(char.base)]\node[anchor=south west, fill=brandTealBg, text=blue, draw=blue!30, line width=0.4pt, rounded corners=2.5pt, inner xsep=3.5pt, inner ysep=1.5pt, font=\fontsize{7.5}{7.5}\selectfont\kml\bfseries] (char) {#1};%
     }
     ```
   - **ពណ៌ហាយឡាយរូបមន្ត (Formula Highlight):**
     ```latex
     \newcommand{\koreahl}[1]{\colorbox{koreaYellow}{\fontsize{8.2}{8.2}\selectfont\textbf{#1}}}
     ```
   - **ប្រអប់សង្ខេបទ្រឹស្ដី «ជាទូទៅ» (General Rule Box):**
     ```latex
     \newtcolorbox{khboxorange}[1][]{
       enhanced,
       colframe=brandNavy!40,
       colback=brandLightBlue,
       boxrule=0.7pt,
       arc=4.5pt,
       borderline west={3.5pt}{0pt}{brandNavy},
       drop fuzzy shadow=brandNavy!15,
       left=7pt, right=7pt, top=4pt, bottom=4pt,
       colupper=blue,
       title={\fontsize{8.5}{8.5}\selectfont\kml\color{white}\ding{72}\ ជាទូទៅ},
       coltitle=white,
       colbacktitle=brandNavy,
       boxed title style={boxrule=0pt, arc=3pt, left=5pt, right=5pt, top=1.5pt, bottom=1.5pt},
       attach boxed title to top left={yshift*=-\tcboxedtitleheight/2, xshift=10pt},
       before skip=4pt, after skip=4pt,
       #1
     }
     ```
   - **ប្រអប់ទ្រឹស្ដីចំណងជើងជាក់លាក់ (Custom Title Box):**
     ```latex
     \newtcolorbox{khboxtitle}[2][]{
       enhanced,
       colframe=brandNavy!40,
       colback=brandLightBlue,
       boxrule=0.7pt,
       arc=4.5pt,
       borderline west={3.5pt}{0pt}{brandNavy},
       drop fuzzy shadow=brandNavy!15,
       left=7pt, right=7pt, top=4pt, bottom=4pt,
       colupper=blue,
       title={\fontsize{8.5}{8.5}\selectfont\kml\color{white}\ding{72}\ #2},
       coltitle=white,
       colbacktitle=brandNavy,
       boxed title style={boxrule=0pt, arc=3pt, left=5pt, right=5pt, top=1.5pt, bottom=1.5pt},
       attach boxed title to top left={yshift*=-\tcboxedtitleheight/2, xshift=10pt},
       before skip=4pt, after skip=4pt,
       #1
     }
     ```

5. **ការកំណត់គម្លាត និងពណ៌អក្សរក្នុង Document:**
   ```latex
   \setlength{\parindent}{0pt}
   \setlength{\parskip}{2.5pt}
   \setlength{\columnsep}{14pt}

   \begin{document}
   \globalcolor{black}
   \fontsize{11}{11.8}\selectfont
   \everymath{\color{blue}}
   \everydisplay{\color{black}}
   ```

---
### ខ. វិធានរៀបចំខ្លឹមសារមេរៀន (Pedagogical & Structural Rules)

1. **ទម្រង់ក្បាលទំព័រ និងការបែងចែកផ្នែក:**
   - លើទំព័រទី១ ត្រូវផ្ដើមដោយ `\koreanheader{មេរៀនទី...}{[ឈ្មោះមេរៀន]}`។
   - ចែកខ្លឹមសារជាផ្នែកធំៗដោយប្រើ `\khsection{[លេខ]}{[ចំណងជើងផ្នែក]}`។
   - ផ្នែកនីមួយៗអាចចាប់ផ្ដើមទំព័រថ្មីដោយ `\newpage` ប្រសិនបើមេរៀនមានប្រវែងវែង (ឧ. ១ ទំព័រ សម្រាប់ ១ ផ្នែកធំ)។

2. **ប្រអប់សង្ខេបទ្រឹស្ដី និងរូបមន្តគន្លឹះ (Dual-Column Theory Box):**
   - ក្នុងប្រអប់ `\begin{khboxorange}` ឬ `\begin{khboxtitle}` ត្រូវចែកជាពីរផ្នែកតាមរយៈ `minipage`:
     - **ខាងឆ្វេង (0.68\textwidth ដល់ 0.75\textwidth):** ចំណុចសំខាន់ៗ និយមន័យ រូបមន្តគណនា និង `\koreahl{...}`។
     - **ខាងស្ដាំ (0.25\textwidth ដល់ 0.30\textwidth):** រូបគំនូរ TikZ តារាងបំប្លែង ឬដ្យាក្រាមសង្ខេបគន្លឹះដើម្បីឱ្យសិស្សងាយយល់ភ្លាមៗ។

3. **ការបែងចែកលំហាត់តាមប្រភេទ (Type-based Exercises):**
   - បន្ទាប់ពីប្រអប់ទ្រឹស្ដី ត្រូវបើក `\begin{multicols}{2}` ដើម្បីចែកលំហាត់ជា ២ ជួរឈរ។
   - ដាក់ចំណងជើងប្រភេទលំហាត់ដោយ `\khtype{ប្រភេទទី ១ ៖ [ឈ្មោះប្រភេទ]}`។
   - ក្នុងប្រភេទនីមួយៗ ត្រូវមាន៖
     - **លំហាត់គ្រូណែនាំ:** ចាប់ផ្ដើមដោយ `\phead{01}`, `\phead{02}`, ...
     - **លំហាត់សិស្សអនុវត្តខ្លួនឯង:** ចាប់ផ្ដើមដោយ `\pheadDIY{03}`, `\pheadDIY{04}`, ...
     - **ស្លាកចម្លើយ/គន្លឹះសង្ខេប (បើចាំបាច់):** ដាក់នៅក្រោមលំហាត់ស្មុគស្មាញដោយប្រើ `\centerline{\khbadge{...}}`។

4. **អក្ខរាវិរុទ្ធភាសាខ្មែរ និងរូបមន្តគណិតវិទ្យា:**
   - រាល់សញ្ញាខណ្ឌ `។` និងសញ្ញាចុចពីរ `៖` ត្រូវតែមានដកឃ្លាមុន និងក្រោយជានិច្ច។
   - លេខ និងអក្សរគណិតវិទ្យាត្រូវដាក់ក្នុង Math Mode ដូចជា $x$, $y$, $15\%$, $500\,000\text{ ៛}$, $60\text{km/h}$។
   - លេខខ្ទង់ពាន់ ត្រូវប្រើ `\,` ដើម្បីខណ្ឌ (ឧទាហរណ៍៖ $32\,200$ រៀល)។
   - រៀបចំគម្លាតឱ្យតឹងណែន ស្អាត មិនឱ្យហៀរទំព័រឥតប្រយោជន៍ឡើយ។

---
### គ. ព័ត៌មានដែលត្រូវផ្ដល់ឱ្យ AI ពេលចង់បង្កើតមេរៀនថ្មី

- **លេខ និងចំណងជើងមេរៀន:** [ឧទាហរណ៍៖ មេរៀនទី ២ ៖ សមមាត្រ]
- **កម្រិតថ្នាក់:** [ឧទាហរណ៍៖ ថ្នាក់ទី៩]
- **ផ្នែកធំៗ (Sections):**
  1. ផ្នែក ១ ៖ [ឧទាហរណ៍៖ សមមាត្រស្រប និងសមមាត្រច្រាស]
  2. ផ្នែក ២ ៖ [ឧទាហរណ៍៖ ភាគរយ]
  3. ផ្នែក ៣ ៖ [ឧទាហរណ៍៖ ភាគរយកើន ឬថយ]
  4. ផ្នែក ៤ ៖ [ឧទាហរណ៍៖ ការប្រាក់សាមញ្ញ និងការប្រាក់សមាស]
- **រូបមន្ត និងទ្រឹស្ដីសំខាន់ៗដែលត្រូវសង្ខេប:** [...]
- **ចំនួន និងប្រភេទលំហាត់ដែលចង់បាន:** [...]

សូមបង្កើតកូដ LaTeX ពេញលេញ ចាប់ពី `\documentclass` រហូតដល់ `\end{document}` ដោយមិនកាត់ ឬសរសេរ `...` ឡើយ។
```

---

## ២. ឧទាហរណ៍នៃការប្រើប្រាស់ Prompt ជាក់ស្ដែង

### ឧទាហរណ៍ ៖ មេរៀន «សមមាត្រ និងភាគរយ» (ផ្អែកលើ `សមមាត្រ.tex`)

> **បញ្ចូលព័ត៌មានទៅក្នុង AI ៖**
> 
> **លេខ និងចំណងជើងមេរៀន:** មេរៀនទី ២ ៖ សមមាត្រ (ថ្នាក់ទី៩)  
> **ផ្នែកធំៗ:**  
> 1. **ផ្នែក ១ ៖** ចំណោទដែលទាក់ទងនឹងសមមាត្រ (ការប្ដូរខ្នាត Metric $\leftrightarrow$ Imperial, សមមាត្រស្រប, សមមាត្រច្រាស)  
> 2. **ផ្នែក ២ ៖** ចំណោទដែលទាក់ទងនឹងភាគរយ (ការស្វែងរក $n$, ភាគរយនៃបរិមាណ, ភាគរយតម្លៃ និងកម្រៃជើងសារ)  
> 3. **ផ្នែក ៣ ៖** ចំណោទនៃភាគរយកើន ឬ ថយ (រូបមន្ត $\frac{b-a}{a}\times 100\%$, ការស្វែងរកតម្លៃដើមមុនកើន/ចុះថ្លៃ)  
> 4. **ផ្នែក ៤ ៖** ការប្រាក់ (ការប្រាក់សាមញ្ញ $I = P_0 \cdot r \cdot t$ និងការប្រាក់សមាស $P_t = P_0(1+r)^t$)  
>
> **លក្ខណៈពិសេសដែលត្រូវបញ្ចូល:**  
> - ផ្នែកនីមួយៗត្រូវមានប្រអប់ `\khboxorange` ឬ `\khboxtitle` សង្ខេបរូបមន្ត ដោយខាងឆ្វេងជារូបមន្ត និងខាងស្ដាំជាគំនូរ TikZ / តារាងបំបែកខ្នាត។
> - លំហាត់ត្រូវរៀបជា ២ ជួរឈរ (`multicols{2}`) ដោយមានទាំងលំហាត់ធម្មតា (`\phead`) និងលំហាត់ធ្វើខ្លួនឯង (`\pheadDIY`)។
> - ដាក់ badge គន្លឹះដោះស្រាយ (`\khbadge`) ក្រោមលំហាត់សំខាន់ៗមួយចំនួន។

---

## ៣. របៀប Compile ឯកសារ LaTeX ឱ្យចេញជា PDF ត្រឹមត្រូវ

1. ត្រូវប្រាកដថា file [khmermath.cls](file:///Users/heng/Documents/%E1%9E%AF%E1%9E%80%E1%9E%9F%E1%9E%9C%E1%9E%94%E1%9E%84%E1%9F%92%E1%9E%9A%E1%9F%80%E1%9E%93/%E1%9E%82%E1%9E%8E%E1%9E%B7%E1%9E%8F%E1%9E%91%E1%9E%B8%E1%9F%A9/%E1%9E%9F%E1%9E%98%E1%9E%98%E1%9E%B6%E1%9E%8F%E1%9F%92%E1%9E%9A/khmermath.cls) ស្ថិតនៅក្នុង Folder តែមួយជាមួយឯកសារ `.tex`។
2. ត្រូវ compile ដោយប្រើ **XeLaTeX**៖
   ```bash
   xelatex -interaction=nonstopmode -synctex=1 "ឈ្មោះឯកសារ.tex"
   ```
3. ពុម្ពអក្សរខ្មែរដែលត្រូវមានក្នុងម៉ាស៊ីន (macOS)៖
   - `Khmer OS Battambang` ឬ `Battambang`
   - `Khmer OS Muol Light`
   - `Khmer OS Bokor`
