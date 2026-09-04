# CLAUDE.md — Iron Circle

Campaign wiki for a tabletop group. Markdown in `docs/`, built by MkDocs (Material theme), deployed to GitHub Pages by `.github/workflows/deploy.yml` on push to `main`. Aaron is the GM and owner; collaborators are players and co-GMs.

## The one rule that matters

**Anything under a `gm/` folder, or with `exposure: secret` in its frontmatter, is GM-only and must never be moved, copied, or summarized into a public page.** The site build excludes both automatically (`mkdocs.yml` `exclude_docs` + `hooks/exposure.py`). The repo is public on GitHub, so "GM-only" means "not on the wiki", not "encrypted" — still, treat it as confidential to the GM. If asked to make something player-visible, ask first, then move it deliberately.

`exposure: public` and `exposure: rumored` both publish. Missing `exposure` publishes (unless under `gm/`).

## Layout

```
docs/
  index.md                  landing page
  Cadwallon/                Daggerheart setting wiki (numbered folders; schema in 00 Reference/Schema.md)
  Fate Foretold/            Daggerheart location + cast
  Documentation/            system references
  stillwater-rise/
    index.md                PUBLIC player-facing case file — spoiler-free
    gm/                     everything else about the campaign (GM-only)
      index.md              hub + CURRENT STATE block
      campaign.md           design doc
      danger-board.md       who's at risk next — changes every session
      decisions.md          dated log of locked design decisions
      themes.md             Suno instrumental cues, one per character
      roster/               character profiles, split by tier
      sessions/             per-session plans and recaps
hooks/exposure.py           the secret-page filter
tools/                      one-off scripts
```

Never commit PDFs (`.gitignore` enforces).

## Conventions by project

### Cadwallon
Read `docs/Cadwallon/00 Reference/Reference.md` (prose style, canon hierarchy, templates) and `Schema.md` (frontmatter data dictionary) before editing. Conform to the schema; don't invent fields. Wikilinks `[[Page]]` and `> [!note]` callouts are the house style and render on the site. Dataview blocks don't execute outside Obsidian — leave them; they're documentation of intent.

### Stillwater Rise
- **Reference material is dry.** Roster entries, design docs, tables: plain, pragmatic, no atmosphere. Stylized prose belongs only in in-world content (voice lines, read-aloud text).
- **Deduction over revelation.** The prior arc (Heliakros) was well-paced but revealed rather than deduced. Every design choice here serves players working it out: three-tier culprit structure, suspects who deflate slowly, sources distinguished by *access cost* not payload.
- **Tiers sort by relationship to the killings, not importance.** Tier A = suspect board (chain + decoys + next victims). Tier B = routes into Tier A. Tier C = texture.
- **Danger board sorts by actor.** Bunting kills entries; Maas kills nobody (institutional threat only); Weaver kills records, using water only when record and person are inseparable.
- **Image prompts** are style-free subject cores for ComfyUI. Headshot: opens "Bust-length view, cropped just below the collarbone", closes "At the bottom edge of the frame only: [collar]". Body: standing, no furniture, face unspecified. See `roster/index.md`.
- **Suno cues** end with the locked spine string, byte-identical across all tracks. Don't edit it per-track. See `themes.md`.
- No predominantly Greek cast; no music-heavy theming beyond the Piper; diversity is an active priority (the Flats is a Black and Puerto Rican district).
- Corrections from Aaron are applied directly — don't restate them back.

## Session workflow

At the end of any working session on Stillwater Rise, before stopping:

1. Update **`gm/danger-board.md`** — move at least one entry, add triggers that fired.
2. Append to **`gm/decisions.md`** — anything newly locked, dated.
3. Write or update **`gm/sessions/session-NN.md`** — plan before, recap after.
4. Update the **CURRENT STATE** block at the top of **`gm/index.md`** — what's locked, what's open, what's next. This block is the cross-session memory; keep it short and current.

Commit with a message that says what changed in the fiction, not just which files.

## Local preview

```
pip install -r requirements.txt
mkdocs serve
```

`mkdocs build` output in the Actions log will list unresolved wikilinks as warnings — the Cadwallon vault has a handful; they're not blockers.
