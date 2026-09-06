"""Regenerate docs/Documentation/Daggerheart SRD/*.md from the Daggerheart SRD PDF.

Usage: python tools/srd_split.py path/to/DH_SRD.pdf   (needs pypdf, fonttools)
The PDF is never committed. Page markers <!-- SRD p.N --> are what the wiki cites.
"""
import os, re, sys
from pypdf import PdfReader

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "DH_SRD.pdf")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "Documentation", "Daggerheart SRD")
os.makedirs(OUT, exist_ok=True)
r = PdfReader(SRC)
N = len(r.pages)

FILES = [
 ("01 Introduction and Character Creation", "Introduction and Character Creation", 2, 5),
 ("02 Domains and Classes", "Domains and Classes", 6, 30),
 ("03 Ancestries, Communities, Transformations", "Ancestries, Communities, and Transformations", 31, 44),
 ("04 Core Mechanics", "Core Mechanics", 45, 53),
 ("05 Equipment", "Equipment", 54, 83),
 ("06 Running an Adventure", "Running an Adventure (GM Guidance and Core GM Mechanics)", 84, 91),
 ("07 Adversaries", "Adversaries", 92, 157),
 ("08 Environments", "Environments", 158, 181),
 ("09 Additional GM Guidance and the Witherwild", "Additional GM Guidance and the Witherwild Campaign Frame", 182, 188),
 ("10 Supplemental Campaign Mechanics", "Supplemental Campaign Mechanics", 189, 204),
 ("11 Domain Card Appendix", "Domain Card Appendix", 205, N - 1),
]

sub = {}
def walk(items, d=0):
    for it in items:
        if isinstance(it, list):
            walk(it, d + 1)
        else:
            try:
                p = r.get_destination_page_number(it)
            except Exception:
                p = None
            if p is not None and d >= 1:
                sub.setdefault(p, []).append((d, it.title.strip()))
walk(r.outline)

FIX = {"\u25e6": "-", "\u2022": "-", "\uf0b7": "-", "\ufffd": "'", "\u2019": "'", "\u2018": "'",
       "\u201c": '"', "\u201d": '"', "\u2013": "-", "\u2014": " - ", "\xa0": " "}
def clean(t):
    for a, b in FIX.items():
        t = t.replace(a, b)
    t = re.sub(r"\b([A-Z]) ([a-z]{2,})", lambda m: m.group(1) + m.group(2), t)
    return t

HEAD = re.compile(r"^[A-Z0-9][A-Z0-9 ,&'()/:\-\.]{2,58}$")
MANUAL = {"Pla Yer": "Player", "Adv Antage": "Advantage", "Disadv Antage": "Disadvantage", "Ev Asion": "Evasion",
          "Gm ": "GM ", "Pc ": "PC ", "Pcs": "PCs", "Npc": "NPC", "Hp": "HP", "Domian": "Domain", "Startin ": "Starting ",
          "Witherwild": "Witherwild", "Srd": "SRD"}
SMALL = (" And ", " Of ", " The ", " A ", " To ", " In ", " For ", " On ", " Or ", " By ", " With ")
def fixhead(st):
    h = st.title().replace("'S", "'s")
    for w in SMALL:
        h = h.replace(w, w.lower())
    for a, b in MANUAL.items():
        h = h.replace(a, b)
    return h

def to_md(t, outline_titles):
    out = []
    for line in t.split("\n"):
        st = line.strip()
        if not st:
            out.append("")
            continue
        if HEAD.match(st) and sum(c.isalpha() for c in st) >= 3 and not st.endswith("."):
            lvl = "## " if st.lower() in outline_titles else "### "
            out += ["", lvl + fixhead(st), ""]
        elif st.startswith("-"):
            out.append("- " + st.lstrip("- ").strip())
        else:
            out.append(st)
    md = "\n".join(out)
    # merge a header that the PDF broke across two lines
    def merge(m):
        a, b = m.group(1), m.group(2)
        if a.rstrip().endswith(("&", " and", ",", " of", " the")) or len(a) < 14:
            return a + " " + b
        return m.group(0)
    md = re.sub(r"(#{2,3} [^\n]+)\n\n#{2,3} ([^\n]+)", merge, md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md

rows = []
for fname, title, a, b in FILES:
    parts = [f"""---
type: reference
exposure: public
source: Daggerheart SRD 2.0 (2026-08-25)
pages: "{a+1}–{b+1}"
aliases: ["{title}"]
---
# {title}

> [!note] Source
> Daggerheart System Reference Document 2.0, PDF pages {a+1}–{b+1}. Public Game Content under the Darrington Press Community Gaming License; see [[Daggerheart SRD]] for the notice and how to cite. Text is machine-extracted; tables lost their columns. When it matters, the PDF wins.
"""]
    for p in range(a, b + 1):
        titles = {t.lower() for d, t in sub.get(p, []) if d == 1}
        parts.append(f"\n<!-- SRD p.{p+1} -->\n*SRD p. {p+1}*\n")
        try:
            txt = r.pages[p].extract_text() or ""
        except Exception as e:
            txt = f"[extraction failed: {e}]"
        parts.append(to_md(clean(txt), titles))
    body = "\n".join(parts)
    with open(os.path.join(OUT, fname + ".md"), "w", encoding="utf-8") as fh:
        fh.write(body)
    heads = [t for p in range(a, b + 1) for d, t in sub.get(p, []) if d == 1]
    rows.append(f"| [[{fname}|{title}]] | {a+1}–{b+1} | {', '.join(heads)} |")
    print(fname, len(body))
with open(os.path.join(OUT, "_index_rows.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(rows))
print("done")
