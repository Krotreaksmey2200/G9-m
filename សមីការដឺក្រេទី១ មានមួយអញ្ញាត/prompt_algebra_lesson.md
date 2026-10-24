# គំរូ Master Prompt សម្រាប់បង្កើតមេរៀនពីជគណិត (LaTeX KhmerMath - Korean Style)

ឯកសារនេះផ្ទុកនូវ **Master Prompt និងកូដគំរូ** សម្រាប់បង្កើតមេរៀនពីជគណិត និងសមីការ (ថ្នាក់ទី៩ ឬកម្រិតផ្សេងទៀត) ឱ្យមានរចនាបថសៀវភៅពុម្ពកូរ៉េ (Korean Math Textbook Style) ដូចគ្នាបេះបិទទៅនឹងឯកសារ [សមីការដឺក្រេទី១.tex](file:///Users/heng/Documents/ឯកសារវបង្រៀន/គណិតទី៩/សមីការដឺក្រេទី១%20មានមួយអញ្ញាត/សមីការដឺក្រេទី១.tex)។

---

## ១. គោលការណ៍រចនាបថ និងស្តង់ដារ (Design Standards)

1. **Document Class & Geometry:**
   - `\documentclass[theme=teal]{khmermath}`
   - `\geometry{left=0.85cm, right=0.85cm, top=0.75cm, bottom=1.5cm, footskip=0.7cm}`

2. **Header & Footer (Fancyhdr):**
   - **Footer ឆ្វេង:** `\fancyfoot[L]{\fontsize{8.5}{8.5}\selectfont\kml \color{koreaNumber}\textbf{\thepage}\ \vline\ \color{koreaDarkTeal}\textbf{[លេខមេរៀន]. [ចំណងជើងមេរៀន]}}`
   - **Footer កណ្ដាល:** `\fancyfoot[C]{\fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{\ding{72}\ បង្រៀនដោយ ៖ \textcolor{koreaDarkTeal}{ក្រូត រស្មី}\ \ding{72}}}`
   - **Footer ស្ដាំ:** `\fancyfoot[R]{\fontsize{8.5}{8.5}\selectfont\kby \color{koreaDarkTeal}\textbf{ Telegram: \textcolor{brandCrimson}{070897540}}\ \vline\ \color{koreaNumber}\textbf{\thepage}}`

3. **លេខរៀងលំហាត់ស្ទីលកូរ៉េ (Two-Tone Korean Numbers):**
   - ប្រើម៉ាក្រូ `\koreannum[size]{number}` សម្រាប់បង្កើតលេខរៀង `01`, `02`, `03` (ខ្ទង់ដប់ពណ៌ប្រផេះ `koreaNumber!65` និងខ្ទង់រាយពណ៌ទឹកក្រូច `koreaOrange`)។
   - ក្បាលលំហាត់ឧទាហរណ៍ ៖ `\koreanexhead{1}{ចូរដោះស្រាយសមីការខាងក្រោម ៖}` $\rightarrow$ ចេញជា **`01`** ចូរដោះស្រាយសមីការខាងក្រោម ៖
   - ក្បាលលំហាត់ប្រតិបត្តិ ៖ `\koreanphead{3}{ចូរដោះស្រាយសមីការ ៖}` $\rightarrow$ ចេញជា **`03`** **`[ប្រតិបត្តិ]`** ចូរដោះស្រាយសមីការ ៖

4. **ប្រអប់វិធាន និងប្រអប់ប្រតិបត្តិ (tcolorbox):**
   - ប្រអប់វិធាន/រូបមន្ត ៖ `\begin{khboxorange} ... \end{khboxorange}` មានរំលេចពណ៌ `\koreahl{...}`
   - ប្រអប់ប្រតិបត្តិ ៖ `\begin{khboxpractice} ... \end{khboxpractice}`

5. **ប្លង់ជួរឈរ (Multicols & Tabularx):**
   - សមីការជាក្រុមច្រើនប្រើ `\begin{multicols}{2}` ឬ `\begin{multicols}{3}`។
   - លំហាត់ប្រតិបត្តិក្នុងប្រអប់ប្រើ `\begin{tabularx}{\linewidth}{@{}X@{}X@{}X@{}}` ដើម្បីកុំឱ្យជាន់ ឬបាក់បន្ទាត់ខណ្ឌ។

---

## ២. កូដគំរូ Preamble & Macros

```latex
\documentclass[theme=teal]{khmermath}
\usepackage{needspace}
\usepackage{colortbl}
\usepackage{tikz}
\usetikzlibrary{calc,shapes,arrows,intersections,through,backgrounds,shadows,decorations.pathmorphing}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{tabularx}

\geometry{left=0.85cm, right=0.85cm, top=0.75cm, bottom=1.5cm, footskip=0.7cm}

% Korean Palette
\definecolor{koreaTeal}{RGB}{0, 150, 155}
\definecolor{koreaDarkTeal}{RGB}{0, 105, 110}
\definecolor{koreaOrange}{RGB}{235, 115, 30}
\definecolor{koreaNumber}{RGB}{115, 125, 135}
\definecolor{koreaYellow}{RGB}{255, 246, 175}
\definecolor{brandNavy}{RGB}{0, 105, 110}
\definecolor{brandCrimson}{RGB}{195, 35, 60}
\definecolor{brandLightBlue}{RGB}{247, 244, 237}
\definecolor{brandTealBg}{RGB}{244, 252, 250}
\definecolor{brandGold}{RGB}{215, 130, 10}

% Header Banner
\newcommand{\koreanheader}[2]{%
  \noindent%
  \begin{tikzpicture}[x=1cm, y=1cm]
    \fill[koreaTeal, rounded corners=12pt] (0, 0.1) -- (0, 0.95) -- (3.8, 0.95) [rounded corners=0pt] -- (4.4, 0.1) -- cycle;
    \node[white, font=\fontsize{11}{11}\selectfont\kml\bfseries] at (1.9, 0.52) {#1};
    \node[anchor=west, font=\fontsize{18}{18}\selectfont\kml\bfseries, color=koreaDarkTeal] at (4.6, 0.42) {#2};
    \node[anchor=east, font=\fontsize{8.5}{8.5}\selectfont\kby, color=gray!80] at (19.2, 0.48) {$>$ ក្លឹបសិក្សាគណិតវិទ្យា PCM};
  \end{tikzpicture}%
  \vspace{3pt}%
}

% Yellow Formula Highlight Box
\newcommand{\koreahl}[1]{\colorbox{koreaYellow}{\fontsize{8.5}{8.5}\selectfont\textbf{#1}}}

% General Rule Box (Teal/Emerald Theme - វិធាន)
\newtcolorbox{khboxorange}[1][]{
  enhanced, colframe=brandNavy!40, colback=brandLightBlue, boxrule=0.7pt, arc=5.0pt,
  borderline west={3.5pt}{0pt}{brandNavy}, drop fuzzy shadow=brandNavy!15,
  left=9pt, right=9pt, top=6pt, bottom=5pt,
  title={\fontsize{9.5}{9.5}\selectfont\kml\color{white}\ding{72}\ វិធាន},
  coltitle=white, colbacktitle=brandNavy,
  boxed title style={boxrule=0pt, arc=3.5pt, left=7pt, right=7pt, top=2.5pt, bottom=2.5pt},
  attach boxed title to top left={yshift*=-\tcboxedtitleheight/2, xshift=12pt}, #1
}

% Practice Card Box
\newtcolorbox{khboxpractice}[1][]{
  enhanced, colframe=brandTeal, colback=brandTealBg, boxrule=0.8pt, arc=4.5pt,
  borderline west={3.5pt}{0pt}{brandCrimson}, drop fuzzy shadow=brandNavy!12,
  left=9pt, right=9pt, top=6pt, bottom=6pt, #1
}

% Korean Number Macros (01, 02, 03...)
\def\splitnum#1#2{\color{koreaNumber!65}#1\color{koreaOrange}#2}
\newcommand{\koreannum}[2][16]{%
  \mbox{\fontsize{#1}{#1}\selectfont\bfseries%
    \ifnum#2<10\relax\color{koreaNumber!65}0\color{koreaOrange}#2%
    \else\expandafter\splitnum#2\fi}\,\ %
}
\newcommand{\koreanexhead}[2]{%
  \vspace{3pt}%
  \noindent\koreannum[17]{#1}{\fontsize{10.5}{10.5}\selectfont\kml\bfseries\color{brandNavy} #2}\par\vspace{3pt}%
}
\newcommand{\phead}[1]{%
  \tikz[baseline=-0.6ex]{\node[fill=brandCrimson, rounded corners=2.5pt, inner sep=2.5pt, text=white, font=\fontsize{8}{8}\selectfont\kml\bfseries] {#1};}\,\ %
}
\newcommand{\koreanphead}[2]{%
  \vspace{3pt}%
  \noindent\koreannum[17]{#1}\phead{ប្រតិបត្តិ}{\fontsize{10.5}{10.5}\selectfont\kml\bfseries\color{brandNavy} #2}\par\vspace{3pt}%
}
```

---

## ៣. ឯកសារយោង និងលទ្ធផលសម្រេច
- កូដប្រភពដើម ៖ [សមីការដឺក្រេទី១.tex](file:///Users/heng/Documents/ឯកសារវបង្រៀន/គណិតទី៩/សមីការដឺក្រេទី១%20មានមួយអញ្ញាត/សមីការដឺក្រេទី១.tex)
- ឯកសារ PDF ចេញជាផ្លូវការ (៤ ទំព័រ) ៖ [សមីការដឺក្រេទី១.pdf](file:///Users/heng/Documents/ឯកសារវបង្រៀន/គណិតទី៩/សមីការដឺក្រេទី១%20មានមួយអញ្ញាត/សមីការដឺក្រេទី១.pdf)
