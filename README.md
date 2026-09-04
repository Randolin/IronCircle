# Iron Circle

The Iron Circle table's campaign wiki. Plain Markdown in `docs/`, built into a website by MkDocs and published to GitHub Pages on every push to `main`.

**Live site:** https://randolin.github.io/IronCircle/

## What's here

| Folder | What it is |
|---|---|
| `docs/Cadwallon/` | The Free City of Cadwallon — Daggerheart setting guide and wiki |
| `docs/Fate Foretold/` | Kalystra / Heliakros — Daggerheart location and cast |
| `docs/stillwater-rise/` | *Stillwater Rise* — 1962 period-noir murder mystery (City of Mist) |
| `docs/Documentation/` | System references |

## Editing

Every page on the site has an **edit (pencil) icon** in the top right. It opens the Markdown file in GitHub's web editor — change it, commit, and the site rebuilds in about a minute. No local tools required.

If you'd rather work locally or with an agent (Claude Code etc.), clone the repo and edit anything under `docs/`. Markdown, wikilinks (`[[Page Name]]`), and Obsidian-style callouts (`> [!note]`) all render.

### Local preview

```
pip install -r requirements.txt
mkdocs serve
```

then open http://127.0.0.1:8000.

## GM-only pages

Some files are for planning and preserving campaign data and are **not** published to the site. Two ways a file gets excluded — either one is enough:

1. It lives in any folder named **`gm/`**.
2. Its frontmatter contains **`exposure: secret`** (the same field the Cadwallon schema already uses).

Players: please don't read those. Yes, the repo is public and you *could*. That's the honor system, and the honor system is the whole hobby.

> If you ever want the GM files genuinely hidden rather than just unpublished, the one-toggle upgrade is a GitHub Pro account, which lets Pages build from a private repo.

## Not in the repo

Rulebook and SRD PDFs are copyrighted and stay on the GM's machine. `.gitignore` blocks `*.pdf` so they can't be committed by accident.

## First-time setup (GM)

1. Run `tools\migrate-from-obsidian.ps1` once to pull the Obsidian vault content into `docs/`.
2. `git add -A`, commit, push.
3. On GitHub: **Settings → Pages → Source: GitHub Actions**. The workflow in `.github/workflows/deploy.yml` does the rest.
