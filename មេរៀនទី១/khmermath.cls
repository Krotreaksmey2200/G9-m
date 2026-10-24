%% =========================================================================
%% khmermath.cls - LaTeX Document Class for Khmer Mathematics & Teaching
%% =========================================================================
%% Version: 1.0 (2026)
%% Description: A professional, modern LaTeX document class tailored for
%%              Khmer mathematics lesson summaries, cheat sheets, exercises,
%%              and exam papers using XeLaTeX.
%% =========================================================================

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{khmermath}[2026/09/03 v1.0 Khmer Mathematics Document Class]

% -------------------------------------------------------------------------
% Class Options Management
% -------------------------------------------------------------------------
\RequirePackage{kvoptions}
\SetupKeyvalOptions{
  family=KM,
  prefix=KM@
}

% Margin options: compact, normal, wide
\DeclareStringOption[compact]{margin}[compact]
% Color theme options: teal (default), magenta, blue, purple, green, orange
\DeclareStringOption[teal]{theme}[teal]
% Font size & paper options passed to article
\DeclareDefaultOption{\PassOptionsToClass{\CurrentOption}{article}}

\ProcessKeyvalOptions*
\LoadClass[a4paper]{article}

% -------------------------------------------------------------------------
% Core Packages
% -------------------------------------------------------------------------
\RequirePackage{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,mathrsfs}
\RequirePackage{tikz}
\usetikzlibrary{calc,shapes,shapes.callouts,arrows,decorations.pathreplacing}
\RequirePackage[most]{tcolorbox}
\tcbuselibrary{raster,skins}
\RequirePackage{enumitem}
\RequirePackage{multicol}
\RequirePackage{graphicx}
\RequirePackage{setspace}
\RequirePackage{eso-pic}
\RequirePackage{float}
\RequirePackage{tabto}
\RequirePackage{pifont}
\RequirePackage{xcolor}

% Optional tkz-tab if available
\IfFileExists{tkz-tab.sty}{\RequirePackage{tkz-tab}}{}

% -------------------------------------------------------------------------
% Page Geometry Configuration
% -------------------------------------------------------------------------
\def\KM@opt@compact{compact}
\def\KM@opt@normal{normal}
\def\KM@opt@wide{wide}

\ifx\KM@margin\KM@opt@compact
  \geometry{top=0.55cm, bottom=0.7cm, left=0.75cm, right=0.75cm}
\else
  \ifx\KM@margin\KM@opt@normal
    \geometry{top=1.2cm, bottom=1.2cm, left=1.2cm, right=1.2cm}
  \else
    \geometry{top=2.0cm, bottom=2.0cm, left=2.0cm, right=2.0cm}
  \fi
\fi

% -------------------------------------------------------------------------
% XeLaTeX & Khmer Font Setup
% -------------------------------------------------------------------------
\RequirePackage[no-math]{fontspec}

\XeTeXlinebreaklocale "km"
\XeTeXlinebreakskip = 0pt plus 0.5pt minus 0.25pt
\everymath{\displaystyle}
\DeclareMathSizes{12pt}{13pt}{11pt}{10pt}
\DeclareMathSizes{10pt}{11pt}{9pt}{8pt}

% Font declarations with graceful fallback
\IfFontExistsTF{Khmer OS Battambang}{%
  \setmainfont{Khmer OS Battambang}[
    Script=Khmer,
    AutoFakeBold=1.8,
    AutoFakeSlant=0.15
  ]
}{%
  \IfFontExistsTF{Battambang}{%
    \setmainfont{Battambang}[
      Script=Khmer,
      BoldFont=Battambang-Bold,
      ItalicFont=Battambang,
      ItalicFeatures={FakeSlant=0.15}
    ]
  }{%
    \setmainfont{Arial Unicode MS}[Script=Khmer]
  }
}

% Specialized Khmer Font Families
\IfFontExistsTF{Khmer OS Muol Light}{%
  \newfontfamily{\kml}{Khmer OS Muol Light}[Script=Khmer, AutoFakeBold=1.2]
  \newcommand{\khmermuol}{\kml}
}{%
  \IfFontExistsTF{Khmer OS Muol}{%
    \newfontfamily{\kml}{Khmer OS Muol}[Script=Khmer, AutoFakeBold=1.2]
    \newcommand{\khmermuol}{\kml}
  }{%
    \newcommand{\kml}{\bfseries}
    \newcommand{\khmermuol}{\bfseries}
  }
}

\IfFontExistsTF{Khmer OS Battambang}{%
  \newfontfamily{\kby}{Khmer OS Battambang}[Script=Khmer, AutoFakeBold=1.8]
}{%
  \newfontfamily{\kby}{Battambang}[Script=Khmer, BoldFont=Battambang-Bold]
}

\IfFontExistsTF{Khmer OS Bokor}{%
  \newfontfamily{\kbk}{Khmer OS Bokor}[Script=Khmer]
}{%
  \newcommand{\kbk}{\kml}
}

\IfFontExistsTF{Kh KoulenL}{%
  \newcommand{\kbf}{\fontspec{Kh KoulenL}\selectfont}
}{%
  \IfFontExistsTF{Koulen}{%
    \newcommand{\kbf}{\fontspec{Koulen}\selectfont}
  }{%
    \newcommand{\kbf}{\kml}
  }
}

\IfFontExistsTF{Times New Roman}{%
  \newcommand{\en}{\fontspec{Times New Roman}\selectfont}
}{%
  \newcommand{\en}{\rmfamily}
}

\newcommand{\z}[1]{\textbf{#1}}
\pagestyle{empty}

% -------------------------------------------------------------------------
% Color Palette & Theming
% -------------------------------------------------------------------------
\definecolor{kmTealMain}{RGB}{7, 94, 70}
\definecolor{kmTealSec}{RGB}{0, 150, 160}
\definecolor{kmTealBg}{RGB}{247, 253, 251}
\definecolor{kmTealBorder}{RGB}{101, 223, 190}

\definecolor{kmMagentaMain}{RGB}{190, 20, 110}
\definecolor{kmMagentaSec}{RGB}{220, 60, 140}
\definecolor{kmMagentaBg}{RGB}{255, 245, 250}
\definecolor{kmMagentaBorder}{RGB}{240, 150, 195}

\definecolor{kmBlueMain}{RGB}{12, 75, 145}
\definecolor{kmBlueSec}{RGB}{30, 120, 215}
\definecolor{kmBlueBg}{RGB}{245, 250, 255}
\definecolor{kmBlueBorder}{RGB}{140, 190, 245}

\definecolor{kmPurpleMain}{RGB}{95, 25, 140}
\definecolor{kmPurpleSec}{RGB}{145, 55, 190}
\definecolor{kmPurpleBg}{RGB}{252, 246, 255}
\definecolor{kmPurpleBorder}{RGB}{205, 150, 240}

% Apply chosen theme
\def\KM@theme@teal{teal}
\def\KM@theme@magenta{magenta}
\def\KM@theme@blue{blue}
\def\KM@theme@purple{purple}

\ifx\KM@theme\KM@theme@magenta
  \colorlet{themeMain}{kmMagentaMain}
  \colorlet{themeSec}{kmMagentaSec}
  \colorlet{themeBg}{kmMagentaBg}
  \colorlet{themeBorder}{kmMagentaBorder}
\else
  \ifx\KM@theme\KM@theme@blue
    \colorlet{themeMain}{kmBlueMain}
    \colorlet{themeSec}{kmBlueSec}
    \colorlet{themeBg}{kmBlueBg}
    \colorlet{themeBorder}{kmBlueBorder}
  \else
    \ifx\KM@theme\KM@theme@purple
      \colorlet{themeMain}{kmPurpleMain}
      \colorlet{themeSec}{kmPurpleSec}
      \colorlet{themeBg}{kmPurpleBg}
      \colorlet{themeBorder}{kmPurpleBorder}
    \else
      % Default: Teal
      \colorlet{themeMain}{kmTealMain}
      \colorlet{themeSec}{kmTealSec}
      \colorlet{themeBg}{kmTealBg}
      \colorlet{themeBorder}{kmTealBorder}
    \fi
  \fi
\fi

% Aliases for compatibility
\colorlet{colmain}{themeMain}
\colorlet{colsec}{themeSec}
\colorlet{colbg}{themeBg}
\colorlet{colborder}{themeBorder}
\colorlet{mycolor}{themeMain}

% -------------------------------------------------------------------------
% Khmer Counters & Numbering
% -------------------------------------------------------------------------
\makeatletter
% Khmer numbers conversion (0..9 -> ០..៩)
\def\@khmernum#1{\expandafter\@@khmernum\number#1\@nil}
\def\@@khmernum#1{%
  \ifx#1\@nil
  \else
  \char\numexpr#1+"17E0\relax
  \expandafter\@@khmernum\fi
}
\def\knum#1{\expandafter\@khmernum\csname c@#1\endcsname}
\def\khmernumeral#1{\@@khmernum#1\@nil}
\AddEnumerateCounter{\knum}{\@knum}{}

% Khmer Alphabet conversion (1..33 -> ក..អ)
\newcommand*{\kalph}[1]{\expandafter\@kalph\csname c@#1\endcsname}
\newcommand*{\@kalph}[1]{%
  \ifcase#1\or ក\or ខ\or គ\or ឃ\or ង\or ច\or ឆ\or ជ\or ឈ\or ញ\or ដ\or ឋ\or ឌ%
  \or ឍ\or ណ\or ត\or ថ\or ទ\or ធ\or ន\or ប\or ផ\or ព\or ភ\or ម\or យ\or រ\or ល%
  \or វ\or ស\or ហ\or ឡ\or អ%
  \else\@ctrerr\fi
}
\AddEnumerateCounter{\kalph}{\@kalph}{}
\makeatother

\renewcommand{\thepage}{\knum{page}}

% -------------------------------------------------------------------------
% Custom Badges, Numbers & Items
% -------------------------------------------------------------------------
% Circled red number
\newcommand*\rednum[1]{\tikz[baseline=(char.base)]{%
  \node[circle, draw=red!90!black, line width=0.85pt, inner sep=0.7pt, text=red!90!black, font=\bfseries\scriptsize] (char) {#1};}}

% Circled theme colored number
\newcommand*\themenum[1]{\tikz[baseline=(char.base)]{%
  \node[circle, draw=themeMain, fill=themeBg, line width=0.85pt, inner sep=0.7pt, text=themeMain, font=\bfseries\scriptsize] (char) {#1};}}

% Solid colored badge with white number
\newcommand*\circled[1]{\tikz[baseline=(char.base)]{%
  \node[circle, draw=none, fill=themeMain, minimum size=1.35em, inner sep=0pt, text=white, font=\bfseries\scriptsize] (char) {#1};}}

% Rectangular badge item
\newcommand\boxitem[1]{\tikz[baseline=(char.base)]{%
  \node[fill=themeBorder!40, rounded corners=1.5pt, minimum size=1.3em, inner sep=1.5pt, text=themeMain, font=\bfseries\scriptsize] (char) {#1};}}

% Inline tag box
\newtcbox{\tagbox}[1][themeMain]{on line,
  colback=#1,
  colframe=#1,
  fontupper=\bfseries\color{white}\footnotesize,
  boxrule=0pt,
  arc=3.5pt,
  boxsep=0pt,
  left=4pt, right=4pt, top=2pt, bottom=2pt}

% -------------------------------------------------------------------------
% Custom Pre-styled Boxes (tcolorbox)
% -------------------------------------------------------------------------

% 1. Main Document Title Banner
\newcommand{\lessontitle}[2][]{%
  \begin{center}
    \begin{tcolorbox}[
      enhanced,
      colframe=themeMain,
      colback=themeBg,
      boxrule=1.2pt,
      arc=4.5pt,
      width=0.82\textwidth,
      top=4pt, bottom=4pt,
      halign=center
    ]
      {\Large\kml\color{themeMain} #2}%
      \if\relax\detokenize{#1}\relax\else\\[1.5pt]{\small\bfseries\color{themeSec!80!black} #1}\fi
    \end{tcolorbox}
  \end{center}
  \vspace{-5pt}
}

% 2. Full-width Section Box
\newtcolorbox{sectionbox}[2][]{
  enhanced,
  colframe=themeMain,
  colback=white,
  boxrule=1.1pt,
  arc=3pt,
  left=6pt, right=6pt, top=5pt, bottom=5pt,
  title={\normalsize\kml #2},
  coltitle=white,
  colbacktitle=themeMain,
  attach boxed title to top left={yshift*=-\tcboxedtitleheight/2, xshift=8pt},
  boxed title style={
    boxrule=0.8pt,
    colframe=themeMain,
    arc=2.5pt,
    left=4pt, right=4pt, top=2pt, bottom=2pt
  },
  #1
}

% 3. Standard Lesson Summary / Rule Box
\newtcolorbox{summarybox}[2][]{
  enhanced,
  colframe=themeMain,
  colback=white,
  boxrule=1.0pt,
  sharp corners,
  left=6pt, right=6pt, top=4pt, bottom=4pt,
  #1
}

% 4. Definition / Formula Box
\newtcolorbox{formulabox}[2][]{
  enhanced,
  colframe=themeSec,
  colback=themeBg,
  boxrule=0.9pt,
  arc=3.5pt,
  left=5pt, right=5pt, top=4pt, bottom=4pt,
  title={\footnotesize\kml #2},
  coltitle=white,
  colbacktitle=themeSec,
  #1
}

% 5. Example Box
\newtcolorbox{examplebox}[2][]{
  enhanced,
  colframe=blue!80!black,
  colback=blue!3!white,
  boxrule=0.8pt,
  arc=3pt,
  left=5pt, right=5pt, top=3pt, bottom=3pt,
  title={\footnotesize\kml ឧទាហរណ៍៖ #2},
  coltitle=blue!90!black,
  colbacktitle=blue!10!white,
  #1
}

% 6. Exercise Box
\newtcolorbox{exercisebox}[2][]{
  enhanced,
  colframe=orange!85!black,
  colback=orange!3!white,
  boxrule=0.8pt,
  arc=3pt,
  left=5pt, right=5pt, top=3pt, bottom=3pt,
  title={\footnotesize\kml លំហាត់អនុវត្ត៖ #2},
  coltitle=orange!90!black,
  colbacktitle=orange!12!white,
  #1
}

% 7. Note / Warning Box
\newtcolorbox{notebox}[1][]{
  enhanced,
  colframe=red!80!black,
  colback=red!3!white,
  boxrule=0.8pt,
  arc=3pt,
  left=5pt, right=5pt, top=3pt, bottom=3pt,
  title={\footnotesize\kml សម្គាល់ / បម្រាម},
  coltitle=red!90!black,
  colbacktitle=red!10!white,
  #1
}

% 8. Multi-case horizontal sub-box
\newtcolorbox{casebox}[1][]{
  width=0.322\linewidth,
  nobeforeafter,
  equal height group=cases,
  colframe=themeMain!80!black,
  colback=themeBg,
  boxrule=0.7pt,
  arc=3.5pt,
  left=3pt, right=3pt, top=3pt, bottom=3pt,
  halign=center,
  #1
}

% -------------------------------------------------------------------------
% Header & Footer Decorative Background Bar
% -------------------------------------------------------------------------
\newcommand{\khmerschool}[1]{\gdef\KMschool{#1}}
\newcommand{\khmerteacher}[1]{\gdef\KMteacher{#1}}
\newcommand{\khmerphone}[1]{\gdef\KMphone{#1}}
\newcommand{\khmersubject}[1]{\gdef\KMsubject{#1}}
\newcommand{\khmergrade}[1]{\gdef\KMgrade{#1}}
\newcommand{\khmeryear}[1]{\gdef\KMyear{#1}}

% Aliases
\let\school\khmerschool
\let\teacher\khmerteacher
\let\phone\khmerphone
\let\subject\khmersubject
\let\grade\khmergrade
\let\academicyear\khmeryear

\gdef\KMschool{}
\gdef\KMteacher{}
\gdef\KMphone{}
\gdef\KMsubject{គណិតវិទ្យា}
\gdef\KMgrade{១២}
\gdef\KMyear{}

\newcommand{\enablebanner}{
  \AddToShipoutPictureBG{
    \begin{tikzpicture}[remember picture,overlay]
      % Top bar
      \fill[themeMain]([yshift=-0.35cm]current page.north west) rectangle (current page.north east);
      % Bottom bar
      \fill[themeMain]([yshift=0.85cm]current page.south west) rectangle (current page.south east);
      % Page circle
      \node[circle, draw=white, line width=1.5pt, minimum size=0.25cm, fill=themeMain] at ([yshift=0.42cm]current page.south){{\color{white}\fontsize{8}{8}\kml\thepage}};
      % Footer Left
      \node[anchor=west] at ([yshift=0.42cm, xshift=0.5cm]current page.south west){%
        {\textbf{\color{white}\fontsize{8}{8}\kby \KMsubject\hspace{0.25cm}}\hspace{0.25cm}\color{white}\fontsize{7.5}{7.5}\kby \KMschool}%
      };
      % Footer Right
      \node[anchor=east] at ([yshift=0.42cm, xshift=-0.5cm]current page.south east){%
        {\textbf{\color{white}\fontsize{8}{8}\kby \ifx\KMteacher\empty\else គ្រូបង្រៀន៖ \KMteacher\ \fi \ifx\KMphone\empty\else Tel: \KMphone\fi}}%
      };
    \end{tikzpicture}
  }
}

% -------------------------------------------------------------------------
% Pre-configured Khmer Enumerate List Environments
% -------------------------------------------------------------------------
\newlist{khmerenum}{enumerate}{2}
\setlist[khmerenum,1]{label=\protect\themenum{\arabic*}, leftmargin=14pt, labelsep=3.5pt, itemsep=2.5pt}
\setlist[khmerenum,2]{label=\kalph*), leftmargin=14pt, labelsep=3pt, itemsep=1.5pt}

\newlist{redenum}{enumerate}{2}
\setlist[redenum,1]{label=\protect\rednum{\arabic*}, leftmargin=14pt, labelsep=3.5pt, itemsep=2.5pt}
\setlist[redenum,2]{label=\kalph*), leftmargin=14pt, labelsep=3pt, itemsep=1.5pt}

\newlist{circleenum}{enumerate}{2}
\setlist[circleenum,1]{label=\protect\circled{\knum*}, leftmargin=14pt, labelsep=3.5pt, itemsep=2.5pt}
\setlist[circleenum,2]{label=\kalph*), leftmargin=14pt, labelsep=3pt, itemsep=1.5pt}

\endinput
%% End of file `khmermath.cls`.
