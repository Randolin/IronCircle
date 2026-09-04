# CLAUDE.md — Iron Circle

Campaign wiki for a tabletop group. Markdown in `docs/`, built by MkDocs (Material theme), deployed to GitHub Pages by `.github/workflows/deploy.yml` on push to `main`. Aaron is the GM and owner; collaborators are players and co-GMs.

## The one rule that matters

**Anything under a `gm/` folder, or with `exposure: secret` in its frontmatter, is GM-only and must never be moved, copied, or summarized into a public page.** The site build excludes both automatically (`mkdocs.yml` `exclude_docs` + `hooks/exposure.py`). The repo is public on GitHub, so "GM-only" means "not on the wiki", not "encrypted" — still, treat it as confidential to the GM. If asked to make something player-visible, ask first, then flip the field deliberately and reread the page.

`exposure: public` and `exposure: rumored` both publish. Missing `exposure` publishes, **except under `docs/Stillwater Rise/`, where missing means secret** (`SECRET_BY_DEFAULT` in the hook). `[!secret]` callouts don't hide anything; pages publish whole or not at all.

## Layout

```
docs/
  index.md                  landing page
  Cadwallon/                Daggerheart setting wiki (numbered folders; schema in 00 Reference/Schema.md)
  Fate Foretold/            Daggerheart location + cast
  Documentation/            system references
  Stillwater Rise/          City of Mist noir; layout mirrors Cadwallon; SECRET BY DEFAULT
    Stillwater Rise.md      PUBLIC landing page — the spoiler-free case file
    00 Reference/           Reference.md (style), Schema.md (frontmatter), System Notes.md, Themes.md (Suno spine)
    01 The City/            places
    02 Institutions/        agency, Authority, precinct, media, lenders
    03 People/              one note per NPC (with its Suno cue); People.md holds the tier and motive tables
    04 Mythos/              the figures under the surface
    05 Timeline/            Day-N clock and background timeline
    06 Campaign/            Campaign.md = GM hub + CURRENT STATE; Party.md + Characters/ (public PCs);
                            Danger Board.md, Decisions.md, Plot Threads.md, Sessions/Session NN.md
.claude/commands/           slash commands — /wrap-session runs the end-of-session workflow below
hooks/exposure.py           the secret-page filter
tools/                      one-off scripts; build-cms-config.py regenerates docs/admin/config.yml
docs/admin/                 Sveltia CMS (in-browser editor at /admin/). config.yml is GENERATED — edit the script
```

Never commit PDFs (`.gitignore` enforces).

**When you add a folder under `docs/` or a new frontmatter field to a folder, update `tools/build-cms-config.py` and re-run it.** The web editor only saves declared fields and doesn't see undeclared folders.

## Conventions by project

### Cadwallon
Read `docs/Cadwallon/00 Reference/Reference.md` (prose style, canon hierarchy, templates) and `Schema.md` (frontmatter data dictionary) before editing. Conform to the schema; don't invent fields. Wikilinks `[[Page]]` and `> [!note]` callouts are the house style and render on the site. Dataview blocks don't execute outside Obsidian — leave them; they're documentation of intent.

### Stillwater Rise
Read `docs/Stillwater Rise/00 Reference/Reference.md` and `Schema.md` before editing; they carry the conventions below in full.
- **Reference material is dry.** Roster entries, design docs, tables: plain, pragmatic, no atmosphere. Stylized prose belongs only in in-world content (voice lines, read-aloud text).
- **Deduction over revelation.** The prior arc (Heliakros) was well-paced but revealed rather than deduced. Every design choice here serves players working it out: three-tier culprit structure, suspects who deflate slowly, sources distinguished by *access cost* not payload.
- **Tiers sort by relationship to the killings, not importance.** Tier A = suspect board (chain + decoys + next victims). Tier B = routes into Tier A. Tier C = texture.
- **Danger board sorts by actor.** Bunting kills entries; Maas kills nobody (institutional threat only); Weaver kills records, using water only when record and person are inseparable.
- **Image prompts** are style-free subject cores for ComfyUI. Headshot: opens "Bust-length view, cropped just below the collarbone", closes "At the bottom edge of the frame only: [collar]". Body: standing, no furniture, face unspecified. See `00 Reference/Reference.md`.
- **Suno cues** live in each character note under `## Theme (Suno)` and end with the locked spine string, byte-identical across all tracks. Don't edit it per-track. See `00 Reference/Themes.md`.
- No predominantly Greek cast; no music-heavy theming beyond the Piper; diversity is an active priority (the Flats is a Black and Puerto Rican district).
- Corrections from Aaron are applied directly — don't restate them back.

## Session workflow

At the end of any working session on Stillwater Rise, before stopping:

1. Update **`06 Campaign/Danger Board.md`** — move at least one entry, add triggers that fired.
2. Append to **`06 Campaign/Decisions.md`** — anything newly locked, dated.
3. Write or update **`06 Campaign/Sessions/Session NN.md`** — plan before, recap after.
4. Update the **CURRENT STATE** block at the top of **`06 Campaign/Campaign.md`** — what's locked, what's open, what's next. This block is the cross-session memory; keep it short and current.

Commit with a message that says what changed in the fiction, not just which files.

## Local preview

```
pip install -r requirements.txt
mkdocs serve
```

`mkdocs build` output in the Actions log will list unresolved wikilinks as warnings — the Cadwallon vault has a handful; they're not blockers.
