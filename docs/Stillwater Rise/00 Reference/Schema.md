---
type: reference
exposure: secret
aliases: ["Schema", "Frontmatter Schema"]
---
# Schema

The data dictionary for the Stillwater Rise folder. Same conventions as the [[Cadwallon]] schema (kebab-case fields, unquoted wikilinks, atomic values, lowercase enums); a smaller vocabulary. Conform to it; don't invent fields. If a note needs a field that isn't here, add it here first, then to `tools/build-cms-config.py`, then use it.

## Universal fields

| Field | Values | Default | Meaning |
|---|---|---|---|
| `type` | see below | required | What kind of note this is |
| `exposure` | `public` \| `rumored` \| `secret` | **`secret`** | Missing = secret in this folder (build hook). Only `public`/`rumored` publish |
| `completeness` | `stub` \| `draft` \| `complete` | `draft` | Build state of the note |
| `status` | per type | — | In-world condition |
| `aliases` | list | — | Alternate names |
| `tags` | list | — | Optional facets |

`title` is written only by the web editor when it creates a page. `canon` is not used here — everything is homebrew.

## Types

### `moc` — index notes
[[Stillwater Rise]], [[The City]], [[Institutions]], [[People]], [[Mythos]], [[Campaign]], [[Party]].

### `reference` — style, schema, system, themes, logs
[[Reference]], [[Schema]], [[System Notes]], [[Themes]], [[Decisions]].

### `place` — 01 The City

| Field | Values | Meaning |
|---|---|---|
| `district` | `[[place]]` link | Parent district, if any |
| `controlled-by` | `[[institution]]` link | Who holds it, if anyone |

### `institution` — 02 Institutions

| Field | Values | Meaning |
|---|---|---|
| `kind` | `agency` \| `government` \| `media` \| `police` \| `finance` \| `press` \| `church` \| `crime` \| `camp` | What sort of body |
| `hq` | `[[place]]` link | Where it sits |
| `leader` | `[[character]]` link | Head, where known |
| `status` | `active` \| `defunct` \| `hidden` | — |

### `character` — 03 People (NPCs)

| Field | Values | Meaning |
|---|---|---|
| `tier` | `a` \| `b` \| `c` \| `agency` \| `victim` | See [[Reference#The tiers]] |
| `board` | `chain` \| `suspect` \| `next` \| `route` \| `texture` \| `agency` \| `victim` | Relationship to the killings |
| `role` | free text | Epithet or job (`the Piper`, `Medical Examiner`) |
| `mythos` | free text | The figure under the surface, if any (`Anansi`, `Heimdall`) |
| `draws-fire` | `early` \| `early-mid` \| `mid` \| `mid-late` \| `late` | Suspects only: when they deflate |
| `opens` | free text | Tier B only: which Tier A name this route reaches |
| `faction` | `[[institution]]` link or list | Allegiance |
| `location` | `[[place]]` link | Where usually found |
| `status` | `alive` \| `dead` \| `missing` \| `taken` | `taken` = collected by the machine during play |

```yaml
---
type: character
tier: b
board: route
role: Heimdall
mythos: Heimdall
opens: "Everyone. Specifically: Day's on-air call, Fitch's calls, the shape of Weaver's traffic"
faction: [[The Exchange]]
location: [[The Exchange]]
status: alive
exposure: secret
completeness: complete
aliases: ["Rimm"]
---
```

### `pc` — player characters (06 Campaign/Characters)

City of Mist splits a character into **Logos** (the mundane self) and **Mythos** (the legend underneath). Builds use Daggerheart classes and domain cards for each side — see [[System Notes]]. Live stats stay on the sheet.

| Field | Values | Meaning |
|---|---|---|
| `player` | free text | Who plays them |
| `pronouns` | free text | — |
| `logos` | free text | The mundane identity's name (usually the file name) |
| `mythos` | free text | The figure (`The Tower`, `Sun Wukong`, `Coyote`) |
| `ancestry` | free text | Daggerheart ancestry of the Logos self |
| `mythos-ancestry` | free text | Ancestry the Mythos side expresses, if different |
| `community` | free text | Daggerheart community |
| `logos-class` / `logos-subclass` | free text | — |
| `mythos-class` / `mythos-subclass` | free text | — |
| `transformation` | free text | Void transformation template, if any |
| `experiences` | list | All experiences, both sides |
| `logos-cards` / `mythos-cards` | list | Domain cards per side |
| `level` | integer | — |
| `status` | `active` \| `retired` \| `dead` \| `guest` | — |
| `image` | `[[Portrait.png]]` | Portrait in `06 Campaign/Characters/Portraits/` |

PCs are `exposure: public`.

### `thread` — 06 Campaign/Plot Threads

| Field | Values |
|---|---|
| `status` | `open` \| `active` \| `resolved` \| `dormant` |
| `stakes` | one line |
| `related` | list of links |

### `session` — 06 Campaign/Sessions

| Field | Values |
|---|---|
| `date` | `YYYY-MM-DD`, blank until played |
| `session-number` | integer |
| `present` | list |
| `status` | `planning` \| `played` |

### `board` — the [[Danger Board]]
No extra fields. It's a single note that changes every session.

### `timeline` — [[Timeline]]
No extra fields. Days are relative to Day 1, the discovery of the body.

## Dataview

The queries in the Cadwallon [[Schema#Dataview cookbook|cookbook]] work here with `FROM "Stillwater Rise"`. The useful ones:

````
```dataview
TABLE tier, board, role, status
FROM "Stillwater Rise/03 People"
WHERE type = "character"
SORT tier ASC, board ASC
```
````

````
```dataview
TABLE player, mythos, row["logos-class"], row["mythos-class"], level
FROM "Stillwater Rise/06 Campaign/Characters"
WHERE type = "pc"
```
````

Hyphenated fields need `row["..."]`. Dataview runs only in Obsidian; on the site the blocks are documentation of intent.
