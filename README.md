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

Two ways, both in the browser, both free:

**The editor — https://randolin.github.io/IronCircle/admin/** (Sveltia CMS). Sign in with GitHub, pick a section in the sidebar, edit the page, hit Save. Save is a commit to `main`; the site rebuilds in about a minute. Frontmatter fields show up as form fields so you don't have to remember the schema. You need write access to the repo — ask Aaron.

**The pencil icon** in the top right of every page opens the raw Markdown file in GitHub's web editor. Same result, no forms.

A few things about the editor:

- Cadwallon pages edit as raw Markdown only. The rich-text mode rewrites `[[wikilinks]]` and `> [!note]` callouts, so it's switched off there.
- New page names keep capitals and spaces (`The Docks.md`) so wikilinks resolve. Apostrophes are dropped from *new* file names; rename on GitHub if it matters.
- The editor only knows the fields listed in `docs/admin/config.yml`. If you add a new frontmatter field to a folder, add it there too (via `tools/build-cms-config.py`) or the editor will drop it on the next save.
- New folder under `docs/` → new collection in the same script. The editor doesn't walk subfolders.

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

## Editor setup (GM, one-time)

The editor needs a small OAuth relay because GitHub Pages can't hold a client secret. Free, ~10 minutes:

1. GitHub → Settings → Developer settings → OAuth Apps → **New OAuth App**. Homepage `https://randolin.github.io/IronCircle/`; callback URL `<worker-url>/callback` (fill in after step 2, then edit). Copy the client ID and generate a secret.
2. Deploy the relay: https://deploy.workers.cloudflare.com/?url=https://github.com/sveltia/sveltia-cms-auth — set `GITHUB_CLIENT_ID`, `GITHUB_CLIENT_SECRET` (encrypted), and `ALLOWED_DOMAINS=randolin.github.io`.
3. Put the worker URL in `docs/admin/config.yml` → `backend.base_url` (in `tools/build-cms-config.py`, then re-run it). Commit, push, open `/admin/`.

## First-time setup (GM)

1. Run `tools\migrate-from-obsidian.ps1` once to pull the Obsidian vault content into `docs/`.
2. `git add -A`, commit, push.
3. On GitHub: **Settings → Pages → Source: GitHub Actions**. The workflow in `.github/workflows/deploy.yml` does the rest.
