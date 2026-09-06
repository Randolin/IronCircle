"""
MkDocs hook: drop any page whose frontmatter says `exposure: secret`.

This is the GM-only switch. It uses the same `exposure` field the Cadwallon
schema already defines (public | rumored | secret), so nothing new to learn:
set `exposure: secret` in a note's frontmatter and it will never be built
into the public site. `rumored` and `public` both publish.

Belt-and-braces: mkdocs.yml also excludes any folder named `gm/` by path,
so a GM file with missing frontmatter is still safe as long as it lives there.

Secret-by-default folders: for the prefixes in SECRET_BY_DEFAULT, a page is
published only if its frontmatter says `exposure: public` or `exposure: rumored`.
Missing or malformed frontmatter means the page stays off the site.
"""
import logging
import os
import re

from mkdocs.structure.files import Files

log = logging.getLogger("mkdocs.hooks.exposure")

# Local GM preview: set IRON_GM=1 to build EVERYTHING, secret pages and gm/
# folders included. Never set this in CI; the deploy workflow doesn't.
GM_PREVIEW = os.environ.get("IRON_GM", "") not in ("", "0", "false")

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---", re.S)
_SECRET = re.compile(r"^\s*exposure\s*:\s*['\"]?secret['\"]?\s*$", re.M | re.I)
_PUBLISHED = re.compile(r"^\s*exposure\s*:\s*['\"]?(public|rumored)['\"]?\s*$", re.M | re.I)

# Folders (docs-relative prefixes) where a page must opt IN to publishing.
SECRET_BY_DEFAULT = ("Stillwater Rise/",)


def _is_secret(path: str, src_uri: str = "") -> bool:
    try:
        with open(path, encoding="utf-8") as fh:
            head = fh.read(4000)
    except (OSError, UnicodeDecodeError):
        return src_uri.startswith(SECRET_BY_DEFAULT)
    m = _FRONTMATTER.match(head)
    if src_uri.startswith(SECRET_BY_DEFAULT):
        return not (m and _PUBLISHED.search(m.group(1)))
    return bool(m and _SECRET.search(m.group(1)))


def on_config(config):
    if GM_PREVIEW:
        log.warning("exposure: IRON_GM set — GM PREVIEW, secret pages and gm/ folders INCLUDED")
        config["exclude_docs"] = ""
    return config


def on_files(files: Files, config) -> Files:
    if GM_PREVIEW:
        return files
    kept = []
    dropped = 0
    for f in files:
        if f.is_documentation_page() and _is_secret(f.abs_src_path, f.src_uri):
            log.info("exposure: secret — excluding %s", f.src_uri)
            dropped += 1
            continue
        kept.append(f)
    if dropped:
        log.info("exposure: excluded %d GM-only page(s)", dropped)
    return Files(kept)
