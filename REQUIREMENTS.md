# Requirements — Iron Circle repo

Aaron's requirements for moving the table's campaign material out of Claude Projects + Obsidian and into this repo. Recorded 2026-09-04 after the original list was lost to an app crash. This file is the source of truth; if anything in `CLAUDE.md`, `README.md`, `mkdocs.yml`, or the migration script disagrees with it, this wins.

## The five requirements

1. **A repo with a wiki-facing site hostable on GitHub Pages.** Plain Markdown in the repo, built into a website automatically on push.

2. **Public player docs and "hidden" GM docs share the same repo.** Player-facing pages publish to the site. GM-only pages stay in the repo but never appear on the site. (Hidden means unpublished, not encrypted — the repo is public. Acceptable for now; see the GitHub Pro note in README if that ever changes.)

3. **Contributors can see and edit the files as living docs.** Players and co-GMs edit without needing local tooling — GitHub's web editor is enough. No paywall to contribute (the reason Obsidian was abandoned).

4. **Migrate the Obsidian vault**, minus Obsidian-specific files and the Hot Springs Eternal material.
   - Bring: Cadwallon, Fate Foretold, Documentation.
   - Leave: `.obsidian/`, `Projects/` (Hot Springs Eternal), `TTRPG/` (stale duplicate), commercial PDFs.

5. **A good file structure for tracking a TTRPG campaign.** The Cadwallon vault is the reference point for what works (numbered folders, a schema, reference docs), but the structure is open to revision — suggestions welcome.

## Where each requirement is implemented

| Req | Implemented by | Status |
|---|---|---|
| 1 | `mkdocs.yml` (Material theme), `.github/workflows/deploy.yml` | Built; not yet pushed or verified in Actions |
| 2 | `exclude_docs: gm/` in `mkdocs.yml` + `hooks/exposure.py` honoring `exposure: secret` | Built; not yet verified in a live build |
| 3 | `edit_uri` in `mkdocs.yml` (pencil icon on every page), README editing section | Built |
| 4 | `tools/migrate-from-obsidian.ps1` | Written; **not yet run** |
| 5 | `docs/stillwater-rise/` layout (public `index.md` + `gm/` with hub, campaign, danger-board, decisions, themes, roster by tier, sessions) | Built for Stillwater Rise; Cadwallon keeps its own schema; no cross-campaign structure decided yet |

## Open questions on requirement 5

- Should Cadwallon and Fate Foretold adopt the Stillwater Rise `gm/` split, or keep their `exposure:` frontmatter approach? Both work with the build; the question is which is easier to maintain.
- Is there a shared structure worth imposing across campaigns (e.g. every campaign gets `index.md` public, `gm/index.md` with a CURRENT STATE block, `gm/decisions.md`, `gm/sessions/`)?
- Where do system references live — `docs/Documentation/` as-is, or split per system?

## Next steps, in order

1. Run `tools\migrate-from-obsidian.ps1` from the repo root in PowerShell.
2. `git add -A`, commit, push. Check the Actions tab for the first build.
3. On GitHub: Settings → Pages → Source = GitHub Actions.
4. Retrieve the Stillwater Rise campaign doc from the Aug 21 chat's file card; paste into `docs/stillwater-rise/gm/campaign.md`; work the reconciliation checklist there.
5. Decide the open questions above.
6. Plan session 1.
