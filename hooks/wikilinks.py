"""
MkDocs hook: disambiguate bare [[Wikilinks]] before roamlinks resolves them.

roamlinks matches a bare [[Name]] against every file in docs/ by basename and
the LAST match on disk wins — so once two campaigns both have a Reference.md,
Schema.md, Party.md, etc., Cadwallon's [[Reference]] silently pointed at the
Stillwater Rise one (which is also GM-only, so the link broke on the site).

This hook runs before roamlinks (event_priority 100) and rewrites any bare
[[Name]] whose basename exists more than once into roamlinks' explicit path
form, [[Top Folder/Sub/Name]], preferring the match inside the same top-level
campaign folder as the page doing the linking. Unique names are left alone.
"""
import os
import re
from collections import defaultdict

from mkdocs.plugins import event_priority

# [[target#anchor|alias]] — same shape roamlinks accepts; images (![[...]]) skipped.
_LINK = re.compile(r"(?<!!)\[\[([^\]\|#]+)(#[^\]\|]*)?(\|[^\]]*)?\]\]")

_index = defaultdict(list)  # simplified basename -> [docs-relative path without .md]


def _simplify(name: str) -> str:
    return name.strip().lower()


def on_config(config):
    _index.clear()
    docs = config["docs_dir"]
    for root, _dirs, files in os.walk(docs):
        for name in files:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(root, name), docs).replace(os.sep, "/")
            _index[_simplify(name[:-3])].append(rel[:-3])
    return config


@event_priority(100)
def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    top = src.split("/", 1)[0] if "/" in src else ""

    def fix(m):
        target, anchor, alias = m.group(1), m.group(2) or "", m.group(3) or ""
        if "/" in target or "http" in target:
            return m.group(0)
        cands = _index.get(_simplify(target), [])
        if len(cands) < 2:
            return m.group(0)
        same = [c for c in cands if c.split("/", 1)[0] == top]
        chosen = (same or cands)[0]
        return f"[[{chosen}{anchor}{alias}]]"

    return _LINK.sub(fix, markdown)
