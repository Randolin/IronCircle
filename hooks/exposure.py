"""
MkDocs hook: drop any page whose frontmatter says `exposure: secret`.

This is the GM-only switch. It uses the same `exposure` field the Cadwallon
schema already defines (public | rumored | secret), so nothing new to learn:
set `exposure: secret` in a note's frontmatter and it will never be built
into the public site. `rumored` and `public` both publish.

Belt-and-braces: mkdocs.yml also excludes any folder named `gm/` by path,
so a GM file with missing frontmatter is still safe as long as it lives there.
"""
import logging
import re

from mkdocs.structure.files import Files

log = logging.getLogger("mkdocs.hooks.exposure")

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---", re.S)
_SECRET = re.compile(r"^\s*exposure\s*:\s*['\"]?secret['\"]?\s*$", re.M | re.I)


def _is_secret(path: str) -> bool:
    try:
        with open(path, encoding="utf-8") as fh:
            head = fh.read(4000)
    except (OSError, UnicodeDecodeError):
        return False
    m = _FRONTMATTER.match(head)
    return bool(m and _SECRET.search(m.group(1)))


def on_files(files: Files, config) -> Files:
    kept = []
    dropped = 0
    for f in files:
        if f.is_documentation_page() and _is_secret(f.abs_src_path):
            log.info("exposure: secret — excluding %s", f.src_uri)
            dropped += 1
            continue
        kept.append(f)
    if dropped:
        log.info("exposure: excluded %d GM-only page(s)", dropped)
    return Files(kept)
