#!/usr/bin/env python3
"""
Khmer Math Pro Geometry Engine
Renders mathematical & geometric figures in 3 formats:
1. SVG for instant live web preview
2. TikZ for vector XeLaTeX PDF compilation
3. High-res PNG for Microsoft Word (.docx) insertion
"""

import io
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

DIAGRAM_PRESETS = {
    "circle_tangent": {
        "title": "រង្វង់ និងបន្ទាត់ប៉ះ (Circle & Tangent Line)",
        "desc": "រង្វង់ផ្ចិត O កាំ r ប៉ះបន្ទាត់ (d) ត្រង់ចំណុច T (OT ⟂ d)",
        "tikz": r"""\begin{tikzpicture}[scale=0.7]
  \draw[thick, color=brandNavy] (0,0) circle (1.2);
  \coordinate (O) at (0,0);
  \coordinate (T) at (1.2,0);
  \draw[thick, color=brandCrimson] (O) -- (T) node[midway, above] {\footnotesize $r$};
  \draw[thick, color=brandTeal] (1.2, -1.3) -- (1.2, 1.3) node[above] {\footnotesize $(d)$};
  \draw[color=brandCrimson, line width=0.5pt] (1.2, 0.2) -- (1.0, 0.2) -- (1.0, 0);
  \fill[brandNavy] (O) circle (1.5pt) node[left] {$O$};
  \fill[koreaOrange] (T) circle (1.5pt) node[below right] {$T$};
\end{tikzpicture}""",
        "svg": """<svg viewBox="-80 -80 160 160" width="140" height="140" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="45" fill="none" stroke="#0F2C59" stroke-width="2.2"/>
  <line x1="0" y1="0" x2="45" y2="0" stroke="#C3233C" stroke-width="2"/>
  <line x1="45" y1="-55" x2="45" y2="55" stroke="#00969B" stroke-width="2.2"/>
  <rect x="35" y="-10" width="10" height="10" fill="none" stroke="#C3233C" stroke-width="1"/>
  <circle cx="0" cy="0" r="3" fill="#0F2C59"/>
  <circle cx="45" cy="0" r="3" fill="#EB731E"/>
  <text x="-12" y="4" font-size="11" font-weight="bold" fill="#0F2C59">O</text>
  <text x="20" y="-5" font-size="10" font-weight="bold" fill="#C3233C">r</text>
  <text x="50" y="5" font-size="11" font-weight="bold" fill="#EB731E">T</text>
  <text x="48" y="-50" font-size="10" font-weight="bold" fill="#00969B">(d)</text>
</svg>"""
    },

    "right_triangle": {
        "title": "ត្រីកោណកែងពីតាករ (Right Triangle)",
        "desc": "ត្រីកោណ ABC កែងត្រង់ A (BC² = AB² + AC²)",
        "tikz": r"""\begin{tikzpicture}[scale=0.7]
  \coordinate (A) at (0,0);
  \coordinate (B) at (2.8,0);
  \coordinate (C) at (0,2.1);
  \draw[thick, color=brandNavy] (A) node[below left] {$A$} -- (B) node[below right] {$B$} -- (C) node[above left] {$C$} -- cycle;
  \draw[color=brandCrimson, line width=0.5pt] (0, 0.25) -- (0.25, 0.25) -- (0.25, 0);
  \node[below, color=brandNavy] at (1.4, 0) {\footnotesize $c$};
  \node[left, color=brandNavy] at (0, 1.05) {\footnotesize $b$};
  \node[above right, color=brandCrimson] at (1.4, 1.05) {\footnotesize $a$};
\end{tikzpicture}""",
        "svg": """<svg viewBox="-20 -20 160 140" width="140" height="120" xmlns="http://www.w3.org/2000/svg">
  <polygon points="10,100 110,100 10,20" fill="none" stroke="#0F2C59" stroke-width="2.2"/>
  <rect x="10" y="85" width="15" height="15" fill="none" stroke="#C3233C" stroke-width="1.2"/>
  <text x="-4" y="112" font-size="11" font-weight="bold" fill="#0F2C59">A</text>
  <text x="114" y="108" font-size="11" font-weight="bold" fill="#0F2C59">B</text>
  <text x="4" y="14" font-size="11" font-weight="bold" fill="#0F2C59">C</text>
  <text x="55" y="114" font-size="10" font-weight="bold" fill="#0F2C59">c</text>
  <text x="-4" y="60" font-size="10" font-weight="bold" fill="#0F2C59">b</text>
  <text x="68" y="55" font-size="10" font-weight="bold" fill="#C3233C">a</text>
</svg>"""
    },

    "two_tangents": {
        "title": "បន្ទាត់ប៉ះពីរចេញពីចំណុចក្រៅ (Two Tangents from P)",
        "desc": "បន្ទាត់ប៉ះ PA និង PB ស្មើគ្នា (PA = PB, OP ជាកន្លះបន្ទាត់ពុះមុំ)",
        "tikz": r"""\begin{tikzpicture}[scale=0.7]
  \coordinate (O) at (0,0);
  \draw[thick, color=brandNavy] (O) circle (1.2);
  \coordinate (P) at (2.6, 0);
  \coordinate (A) at (0.55, 1.06);
  \coordinate (B) at (0.55, -1.06);
  \draw[thick, color=brandTeal] (P) node[right] {$P$} -- (A) node[above left] {$A$};
  \draw[thick, color=brandTeal] (P) -- (B) node[below left] {$B$};
  \draw[dashed, color=gray] (O) node[left] {$O$} -- (P);
  \draw[thick, color=brandCrimson] (O) -- (A);
  \draw[thick, color=brandCrimson] (O) -- (B);
  \fill[brandNavy] (O) circle (1.5pt);
  \fill[koreaOrange] (A) circle (1.5pt);
  \fill[koreaOrange] (B) circle (1.5pt);
  \fill[brandTeal] (P) circle (1.5pt);
\end{tikzpicture}""",
        "svg": """<svg viewBox="-60 -70 180 140" width="150" height="120" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="42" fill="none" stroke="#0F2C59" stroke-width="2"/>
  <line x1="0" y1="0" x2="90" y2="0" stroke="#94a3b8" stroke-dasharray="3,3"/>
  <line x1="90" y1="0" x2="20" y2="-37" stroke="#00969B" stroke-width="2"/>
  <line x1="90" y1="0" x2="20" y2="37" stroke="#00969B" stroke-width="2"/>
  <line x1="0" y1="0" x2="20" y2="-37" stroke="#C3233C" stroke-width="1.8"/>
  <line x1="0" y1="0" x2="20" y2="37" stroke="#C3233C" stroke-width="1.8"/>
  <circle cx="0" cy="0" r="3" fill="#0F2C59"/>
  <circle cx="90" cy="0" r="3" fill="#00969B"/>
  <circle cx="20" cy="-37" r="3" fill="#EB731E"/>
  <circle cx="20" cy="37" r="3" fill="#EB731E"/>
  <text x="-14" y="4" font-size="11" font-weight="bold" fill="#0F2C59">O</text>
  <text x="96" y="4" font-size="11" font-weight="bold" fill="#00969B">P</text>
  <text x="16" y="-42" font-size="11" font-weight="bold" fill="#EB731E">A</text>
  <text x="16" y="52" font-size="11" font-weight="bold" fill="#EB731E">B</text>
</svg>"""
    },

    "inscribed_angle": {
        "title": "មុំផ្ចិត និងមុំចារឹកក្នុងរង្វង់ (Central & Inscribed Angles)",
        "desc": "មុំចារឹកស្មើពាក់កណ្តាលមុំផ្ចិត (∠ACB = 1/2 ∠AOB)",
        "tikz": r"""\begin{tikzpicture}[scale=0.7]
  \coordinate (O) at (0,0);
  \draw[thick, color=brandNavy] (O) circle (1.3);
  \coordinate (A) at (-1.0, -0.83);
  \coordinate (B) at (1.0, -0.83);
  \coordinate (C) at (0, 1.3);
  \draw[thick, color=brandTeal] (C) node[above] {$C$} -- (A) node[below left] {$A$};
  \draw[thick, color=brandTeal] (C) -- (B) node[below right] {$B$};
  \draw[thick, color=brandCrimson] (O) node[above] {$O$} -- (A);
  \draw[thick, color=brandCrimson] (O) -- (B);
  \fill[brandNavy] (O) circle (1.5pt);
  \fill[brandTeal] (C) circle (1.5pt);
  \fill[koreaOrange] (A) circle (1.5pt);
  \fill[koreaOrange] (B) circle (1.5pt);
\end{tikzpicture}""",
        "svg": """<svg viewBox="-80 -80 160 160" width="140" height="140" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="50" fill="none" stroke="#0F2C59" stroke-width="2"/>
  <line x1="0" y1="0" x2="-38" y2="32" stroke="#C3233C" stroke-width="2"/>
  <line x1="0" y1="0" x2="38" y2="32" stroke="#C3233C" stroke-width="2"/>
  <line x1="0" y1="-50" x2="-38" y2="32" stroke="#00969B" stroke-width="2"/>
  <line x1="0" y1="-50" x2="38" y2="32" stroke="#00969B" stroke-width="2"/>
  <circle cx="0" cy="0" r="3" fill="#0F2C59"/>
  <circle cx="0" cy="-50" r="3" fill="#00969B"/>
  <circle cx="-38" cy="32" r="3" fill="#EB731E"/>
  <circle cx="38" cy="32" r="3" fill="#EB731E"/>
  <text x="3" y="-3" font-size="11" font-weight="bold" fill="#0F2C59">O</text>
  <text x="-4" y="-55" font-size="11" font-weight="bold" fill="#00969B">C</text>
  <text x="-52" y="40" font-size="11" font-weight="bold" fill="#EB731E">A</text>
  <text x="44" y="40" font-size="11" font-weight="bold" fill="#EB731E">B</text>
</svg>"""
    },

    "two_circles_touch": {
        "title": "រង្វង់ពីរប៉ះគ្នាក្រៅ (Two Touching Circles)",
        "desc": "រង្វង់ពីរមានកាំ R និង r ប៉ះគ្នាក្រៅត្រង់ T (O₁O₂ = R + r)",
        "tikz": r"""\begin{tikzpicture}[scale=0.6]
  \coordinate (O1) at (0,0);
  \coordinate (O2) at (2.4, 0);
  \coordinate (T) at (1.4, 0);
  \draw[thick, color=brandNavy] (O1) circle (1.4);
  \draw[thick, color=brandTeal] (O2) circle (1.0);
  \draw[thick, color=brandCrimson] (O1) -- (O2);
  \draw[thick, color=koreaOrange] (1.4, -1.5) -- (1.4, 1.5) node[above] {\footnotesize $(d)$};
  \fill[brandNavy] (O1) circle (1.5pt) node[left] {$O_1$};
  \fill[brandTeal] (O2) circle (1.5pt) node[right] {$O_2$};
  \fill[brandCrimson] (T) circle (1.5pt) node[below right] {$T$};
\end{tikzpicture}""",
        "svg": """<svg viewBox="-70 -60 190 120" width="160" height="110" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="44" fill="none" stroke="#0F2C59" stroke-width="2"/>
  <circle cx="74" cy="0" r="30" fill="none" stroke="#00969B" stroke-width="2"/>
  <line x1="0" y1="0" x2="74" y2="0" stroke="#C3233C" stroke-width="2"/>
  <line x1="44" y1="-50" x2="44" y2="50" stroke="#EB731E" stroke-width="1.8"/>
  <circle cx="0" cy="0" r="3" fill="#0F2C59"/>
  <circle cx="74" cy="0" r="3" fill="#00969B"/>
  <circle cx="44" cy="0" r="3" fill="#C3233C"/>
  <text x="-16" y="4" font-size="11" font-weight="bold" fill="#0F2C59">O₁</text>
  <text x="80" y="4" font-size="11" font-weight="bold" fill="#00969B">O₂</text>
  <text x="46" y="14" font-size="10" font-weight="bold" fill="#C3233C">T</text>
</svg>"""
    },

    "intersecting_chords": {
        "title": "អង្កត់ធ្នូពីរជួបគ្នាក្នុងរង្វង់ (Intersecting Chords)",
        "desc": "អង្កត់ធ្នូ AB និង CD កាត់គ្នាត្រង់ P (PA · PB = PC · PD)",
        "tikz": r"""\begin{tikzpicture}[scale=0.7]
  \coordinate (O) at (0,0);
  \draw[thick, color=brandNavy] (O) circle (1.3);
  \coordinate (A) at (-1.2, 0.5);
  \coordinate (B) at (1.1, -0.7);
  \coordinate (C) at (-0.6, -1.15);
  \coordinate (D) at (0.8, 1.02);
  \coordinate (P) at (0.1, -0.15);
  \draw[thick, color=brandCrimson] (A) node[above left] {$A$} -- (B) node[below right] {$B$};
  \draw[thick, color=brandTeal] (C) node[below left] {$C$} -- (D) node[above right] {$D$};
  \fill[koreaOrange] (P) circle (1.5pt) node[below] {$P$};
\end{tikzpicture}""",
        "svg": """<svg viewBox="-70 -70 140 140" width="130" height="130" xmlns="http://www.w3.org/2000/svg">
  <circle cx="0" cy="0" r="48" fill="none" stroke="#0F2C59" stroke-width="2"/>
  <line x1="-42" y1="20" x2="40" y2="-25" stroke="#C3233C" stroke-width="2"/>
  <line x1="-20" y1="-44" x2="25" y2="41" stroke="#00969B" stroke-width="2"/>
  <circle cx="4" cy="-3" r="3" fill="#EB731E"/>
  <text x="-54" y="24" font-size="11" font-weight="bold" fill="#C3233C">A</text>
  <text x="44" y="-22" font-size="11" font-weight="bold" fill="#C3233C">B</text>
  <text x="-24" y="-50" font-size="11" font-weight="bold" fill="#00969B">C</text>
  <text x="26" y="52" font-size="11" font-weight="bold" fill="#00969B">D</text>
  <text x="8" y="10" font-size="11" font-weight="bold" fill="#EB731E">P</text>
</svg>"""
    },

    "coordinate_plane": {
        "title": "ប្លង់កូអរដោនេ និងបន្ទាត់ (Cartesian Plane Oxy)",
        "desc": "ក្រាបបន្ទាត់ (d): y = ax + b ក្នុងប្លង់កូអរដោនេ",
        "tikz": r"""\begin{tikzpicture}[scale=0.6]
  \draw[->, color=gray!80, line width=0.6pt] (-2.2,0) -- (2.5,0) node[right] {\footnotesize $x$};
  \draw[->, color=gray!80, line width=0.6pt] (0,-2.0) -- (0,2.3) node[above] {\footnotesize $y$};
  \node[below left, font=\footnotesize] at (0,0) {$O$};
  \draw[thick, color=brandCrimson] (-1.8, -1.3) -- (1.8, 1.7) node[above right] {\footnotesize $(d): y=ax+b$};
  \fill[brandNavy] (0, 0.2) circle (1.5pt) node[left] {\footnotesize $b$};
\end{tikzpicture}""",
        "svg": """<svg viewBox="-80 -80 160 160" width="140" height="140" xmlns="http://www.w3.org/2000/svg">
  <line x1="-65" y1="0" x2="65" y2="0" stroke="#64748b" stroke-width="1.2"/>
  <polygon points="65,0 58,-3 58,3" fill="#64748b"/>
  <line x1="0" y1="65" x2="0" y2="-65" stroke="#64748b" stroke-width="1.2"/>
  <polygon points="0,-65 -3,-58 3,-58" fill="#64748b"/>
  <line x1="-50" y1="35" x2="50" y2="-45" stroke="#C3233C" stroke-width="2.2"/>
  <text x="56" y="14" font-size="10" fill="#64748b">x</text>
  <text x="6" y="-56" font-size="10" fill="#64748b">y</text>
  <text x="-12" y="12" font-size="10" fill="#64748b">O</text>
  <text x="25" y="-50" font-size="10" font-weight="bold" fill="#C3233C">(d)</text>
</svg>"""
    }
}

def render_diagram_png(preset_key):
    """
    Renders diagram as transparent PNG bytes for Word DOCX.
    """
    fig, ax = plt.subplots(figsize=(2.2, 2.0), dpi=180)
    ax.axis('off')

    if preset_key == "circle_tangent":
        c = plt.Circle((0, 0), 1, color='#0F2C59', fill=False, linewidth=1.8)
        ax.add_patch(c)
        ax.plot([0, 1], [0, 0], color='#C3233C', linewidth=1.8)
        ax.plot([1, 1], [-1.3, 1.3], color='#00969B', linewidth=1.8)
        ax.plot(0, 0, 'o', color='#0F2C59', markersize=4)
        ax.plot(1, 0, 'o', color='#EB731E', markersize=4)
        ax.text(-0.15, -0.05, 'O', fontsize=9, fontweight='bold', color='#0F2C59')
        ax.text(0.45, 0.08, 'r', fontsize=8.5, fontweight='bold', color='#C3233C')
        ax.text(1.06, -0.15, 'T', fontsize=9, fontweight='bold', color='#EB731E')
        ax.text(1.05, 1.1, '(d)', fontsize=8.5, fontweight='bold', color='#00969B')
        ax.set_xlim(-1.4, 1.5)
        ax.set_ylim(-1.4, 1.4)

    elif preset_key == "right_triangle":
        ax.plot([0, 2.5, 0, 0], [0, 0, 1.8, 0], color='#0F2C59', linewidth=1.8)
        # right angle box
        ax.plot([0, 0.25, 0.25], [0.25, 0.25, 0], color='#C3233C', linewidth=1)
        ax.text(-0.18, -0.15, 'A', fontsize=9, fontweight='bold', color='#0F2C59')
        ax.text(2.55, -0.15, 'B', fontsize=9, fontweight='bold', color='#0F2C59')
        ax.text(-0.18, 1.85, 'C', fontsize=9, fontweight='bold', color='#0F2C59')
        ax.text(1.2, -0.22, 'c', fontsize=8.5, fontweight='bold')
        ax.text(-0.25, 0.9, 'b', fontsize=8.5, fontweight='bold')
        ax.text(1.3, 1.0, 'a', fontsize=8.5, fontweight='bold', color='#C3233C')
        ax.set_xlim(-0.4, 2.8)
        ax.set_ylim(-0.4, 2.1)

    elif preset_key == "two_tangents":
        c = plt.Circle((0, 0), 1, color='#0F2C59', fill=False, linewidth=1.8)
        ax.add_patch(c)
        ax.plot([0, 2.4], [0, 0], '--', color='gray', linewidth=1)
        ax.plot([2.4, 0.42], [0, 0.91], color='#00969B', linewidth=1.8)
        ax.plot([2.4, 0.42], [0, -0.91], color='#00969B', linewidth=1.8)
        ax.plot([0, 0.42], [0, 0.91], color='#C3233C', linewidth=1.5)
        ax.plot([0, 0.42], [0, -0.91], color='#C3233C', linewidth=1.5)
        ax.plot(0, 0, 'o', color='#0F2C59', markersize=3.5)
        ax.plot(2.4, 0, 'o', color='#00969B', markersize=3.5)
        ax.plot(0.42, 0.91, 'o', color='#EB731E', markersize=3.5)
        ax.plot(0.42, -0.91, 'o', color='#EB731E', markersize=3.5)
        ax.text(-0.2, 0, 'O', fontsize=9, fontweight='bold')
        ax.text(2.5, 0, 'P', fontsize=9, fontweight='bold', color='#00969B')
        ax.text(0.35, 1.05, 'A', fontsize=9, fontweight='bold', color='#EB731E')
        ax.text(0.35, -1.2, 'B', fontsize=9, fontweight='bold', color='#EB731E')
        ax.set_xlim(-1.3, 2.8)
        ax.set_ylim(-1.3, 1.3)

    elif preset_key == "inscribed_angle":
        c = plt.Circle((0, 0), 1, color='#0F2C59', fill=False, linewidth=1.8)
        ax.add_patch(c)
        ax.plot([0, -0.7], [0, -0.71], color='#C3233C', linewidth=1.8)
        ax.plot([0, 0.7], [0, -0.71], color='#C3233C', linewidth=1.8)
        ax.plot([0, -0.7], [1, -0.71], color='#00969B', linewidth=1.8)
        ax.plot([0, 0.7], [1, -0.71], color='#00969B', linewidth=1.8)
        ax.plot(0, 0, 'o', color='#0F2C59', markersize=3.5)
        ax.plot(0, 1, 'o', color='#00969B', markersize=3.5)
        ax.plot(-0.7, -0.71, 'o', color='#EB731E', markersize=3.5)
        ax.plot(0.7, -0.71, 'o', color='#EB731E', markersize=3.5)
        ax.text(0.05, 0.05, 'O', fontsize=9, fontweight='bold')
        ax.text(-0.05, 1.1, 'C', fontsize=9, fontweight='bold', color='#00969B')
        ax.text(-0.9, -0.85, 'A', fontsize=9, fontweight='bold', color='#EB731E')
        ax.text(0.75, -0.85, 'B', fontsize=9, fontweight='bold', color='#EB731E')
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)

    elif preset_key == "two_circles_touch":
        c1 = plt.Circle((0, 0), 1.0, color='#0F2C59', fill=False, linewidth=1.8)
        c2 = plt.Circle((1.7, 0), 0.7, color='#00969B', fill=False, linewidth=1.8)
        ax.add_patch(c1)
        ax.add_patch(c2)
        ax.plot([0, 1.7], [0, 0], color='#C3233C', linewidth=1.8)
        ax.plot([1.0, 1.0], [-1.2, 1.2], color='#EB731E', linewidth=1.5)
        ax.plot(0, 0, 'o', color='#0F2C59', markersize=3.5)
        ax.plot(1.7, 0, 'o', color='#00969B', markersize=3.5)
        ax.plot(1.0, 0, 'o', color='#C3233C', markersize=3.5)
        ax.text(-0.25, -0.05, 'O₁', fontsize=8.5, fontweight='bold')
        ax.text(1.8, -0.05, 'O₂', fontsize=8.5, fontweight='bold', color='#00969B')
        ax.text(1.05, 0.1, 'T', fontsize=8.5, fontweight='bold', color='#C3233C')
        ax.set_xlim(-1.3, 2.7)
        ax.set_ylim(-1.3, 1.3)

    elif preset_key == "intersecting_chords":
        c = plt.Circle((0, 0), 1, color='#0F2C59', fill=False, linewidth=1.8)
        ax.add_patch(c)
        ax.plot([-0.9, 0.8], [0.43, -0.6], color='#C3233C', linewidth=1.8)
        ax.plot([-0.4, 0.6], [-0.91, 0.8], color='#00969B', linewidth=1.8)
        ax.plot(0.1, -0.22, 'o', color='#EB731E', markersize=3.5)
        ax.text(-1.1, 0.45, 'A', fontsize=9, fontweight='bold', color='#C3233C')
        ax.text(0.85, -0.65, 'B', fontsize=9, fontweight='bold', color='#C3233C')
        ax.text(-0.5, -1.1, 'C', fontsize=9, fontweight='bold', color='#00969B')
        ax.text(0.65, 0.85, 'D', fontsize=9, fontweight='bold', color='#00969B')
        ax.text(0.18, -0.35, 'P', fontsize=9, fontweight='bold', color='#EB731E')
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)

    elif preset_key == "coordinate_plane":
        ax.plot([-1.5, 1.5], [0, 0], color='gray', linewidth=1)
        ax.plot([0, 0], [-1.5, 1.5], color='gray', linewidth=1)
        ax.plot([-1.2, 1.2], [-1.0, 1.4], color='#C3233C', linewidth=1.8)
        ax.text(1.4, -0.2, 'x', fontsize=8.5, color='gray')
        ax.text(0.1, 1.4, 'y', fontsize=8.5, color='gray')
        ax.text(-0.2, -0.2, 'O', fontsize=8.5, color='gray')
        ax.text(0.5, 1.2, '(d)', fontsize=8.5, fontweight='bold', color='#C3233C')
        ax.set_xlim(-1.6, 1.6)
        ax.set_ylim(-1.6, 1.6)

    ax.set_aspect('equal')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close(fig)
    return buf.getvalue()
