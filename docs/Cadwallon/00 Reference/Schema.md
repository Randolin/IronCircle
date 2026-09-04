---
type: reference
exposure: public
aliases: ["Schema", "Frontmatter Schema", "Data Schema", "Dataview Reference"]
---
# Schema

> "Name a thing properly and it stays where you put it. Name it twice and it walks off."

The **data dictionary** for the Cadwallon vault. This is the authoritative spec for YAML frontmatter (Obsidian Properties) and the [Dataview](https://blacksmithgu.github.io/obsidian-dataview/) queries built on top of it. [[Reference]] governs *prose* and house style; this file governs *metadata*. [[Conversion Notes]] governs *Daggerheart mechanics*. Keep the three concerns in their three files.

Every populated note carries frontmatter that conforms to exactly one **type** below. Conform to the schema; don't invent fields. If a note genuinely needs a field that doesn't exist here, add it *to this file first*, then use it — so it stays queryable.

---

## Conventions (apply to all frontmatter)

- **Field names are `kebab-case`** — `ruling-house`, `faction-type`, never `rulingHouse` or `Ruling House`.
- **Links are unquoted wikilinks** — write `fief: [[The Rampart]]`, not `fief: "[[The Rampart]]"`. Unquoted, Obsidian stores it as a real Link property (clickable, rename-aware) and Dataview reads it as a `Link` object you can filter and group on. Quoting turns it into a plain string.
- **Multi-value link fields are YAML lists**, one link per line:
  ```yaml
  faction:
    - [[Court of Shadows]]
    - [[Acheron]]
  ```
  Never cram several links into one value (`faction: "[[A]] / [[B]] (origin)"` is unqueryable).
- **Values are atomic** — one fact per field, no parenthetical annotations. Put nuance in the body, not the property. If a character's allegiance "depends," that's a body sentence, not a frontmatter value.
- **Dates are bare integer years AF** — `date: 900`, not `"900"` or `900 AF`. This lets Dataview sort and compare numerically. (See [[Calendar]] for the dating system.)
- **Enums are lowercase** — `exposure: secret`, `tier: lower`, `completeness: stub`.
- **Prose strings get quotes only when YAML needs them** (a value containing `:` or starting with `[`). Plain words don't.

---

## Universal fields

Every note may carry these. `type` is required; the rest default as noted.

| Field | Values | Default | Meaning |
|---|---|---|---|
| `type` | one of the controlled vocabulary below | — (required) | What kind of note this is. Drives every `FROM`/`WHERE`. |
| `exposure` | `public` \| `rumored` \| `secret` | `public` | In-world knowledge tier. `secret` = GM-only; the GM-index queries key off this. |
| `canon` | `core` \| `homebrew` | `core` | Source of truth. `core` = drawn from PHB / Secrets / Marine Ruins. `homebrew` = our table's invention or override (**authoritative** per [[Reference#Canon Hierarchy]]). |
| `completeness` | `stub` \| `draft` \| `complete` | `draft` | Build state of the note itself. Lets us query "what still needs writing." |
| `tags` | list | — | Cross-cutting facets that aren't a `type` (e.g. `rag-narok`, `desire-waking`, `arcana`). Optional. |
| `aliases` | list | — | Alternate names so wikilinks and search resolve. Optional but encouraged for anything with in-world variant names. |

> [!note] `status` vs `completeness` vs `canon`
> These three were all crammed into `status` historically. They are now distinct:
> **`canon`** = where it came from · **`completeness`** = how finished the note is · **`status`** = the thing's *in-world* condition (only on types that have one — see below).

---

## The `type` vocabulary

Seventeen types across the eight content folders plus reference and campaign. Each section gives the type's extra fields and a paste-ready template (universal fields included).

### Meta & reference

#### `moc` — map of content / directory note
Index notes that orient and link out (`Nations.md`, `Districts.md`, `Fiefs.md`, `Factions.md`, `Cultures.md`, `People.md`, `Underground.md`, `Cosmology.md`, all `Homebrew.md` indexes, `Houses of Peers.md`, `Campaign.md`).

```yaml
---
type: moc
exposure: public
---
```

#### `reference` — style / meta / conversion docs
The `00 Reference/` working docs: [[Reference]], [[Glossary]], [[Calendar]], [[Conversion Notes]], and this file.

```yaml
---
type: reference
exposure: public
---
```

### 01 World

#### `nation` — foreign powers of Aarklash

| Field | Values | Meaning |
|---|---|---|
| `alliance` | `Ways of Light` \| `Meanders of Darkness` \| `Paths of Destiny` \| `neutral` | Bloc membership ([[The Three Alliances]]). Proper-case — it's a named entity. |
| `culture` | totem name (e.g. `Stag`, `Lion`, `Rat`) | The nation's totem-culture. |
| `race` | free text | Dominant people. |
| `embassy` | `[[District]]` link \| `none` | Where (if anywhere) it keeps an embassy in Cadwallon. |

```yaml
---
type: nation
alliance: Meanders of Darkness
culture: Stag
race: human (living-dead)
embassy: none
exposure: public
canon: core
completeness: complete
aliases: ["Acheron", "The living-dead of Acheron"]
---
```

#### `place` — geography & physical locations (not fiefs/districts/delve-sites)
The continent, harbors, forts, edge-features, city-overview pieces ([[Aarklash]], [[The Outskirts]], [[Kraken Harbor]], [[Shipwreck Bay]], [[Fort Griffin]], [[The Watching Tower]], [[Immobilis]], [[Tractor]], [[Wall of Earth]], etc.).

| Field | Values | Meaning |
|---|---|---|
| `region` | free text or `[[link]]` | Where it sits (continent, fief, beyond the walls). Optional. |
| `controlled-by` | `[[faction]]` / `[[character]]` | Who holds it, if anyone. Optional. |

```yaml
---
type: place
region: Aarklash
exposure: public
canon: core
completeness: complete
---
```

#### `concept` — lore & metaphysical abstractions
Non-physical, non-divine ideas: [[The Three Alliances]], [[The Rag'narok]], [[Cadwë Dream]], [[The 22 Arcana]], [[Mana & Magic]], [[Incarnates]], [[Desire|the mechanics of Desire's dreaming]], etc.

```yaml
---
type: concept
exposure: secret
canon: core
completeness: complete
---
```

#### `deity` — gods
[[Desire]], [[Conscience]], [[Maloth]], [[Vile-Tis]], [[Vortiris]], [[Yllia]].

| Field | Values | Meaning |
|---|---|---|
| `alliance` | as `nation` \| `none` | Cosmic alignment, where one applies. Optional. |
| `domain` | free text | What the god is *of* (desire, conscience, the moon, slaughter). Optional. |

```yaml
---
type: deity
domain: desire
exposure: secret
canon: core
completeness: complete
---
```

### 02 City

#### `fief` — the eleven fiefdoms

| Field | Values | Meaning |
|---|---|---|
| `tier` | `lower` \| `upper` | Lower or upper city. |
| `ruling-house` | `[[faction]]` link | The house note (type `faction`, `faction-type: house`). |
| `peer` | `[[character]]` link (or list, for joint peerages) | The ruling Peer(s). |

```yaml
---
type: fief
tier: lower
ruling-house: [[Houses of Peers]]
peer: [[Bismuth von Kraken of Odazzur]]
exposure: public
canon: core
completeness: complete
---
```

#### `district` — districts within fiefs

| Field | Values | Meaning |
|---|---|---|
| `fief` | `[[Fief]]` link | Parent fief (authoritative). |
| `tier` | `lower` \| `upper` | Inherited from the fief, stored for direct query. |
| `attitude` | `Style` \| `Subtlety` \| `Opportunism` \| `Pugnacity` \| ... | The PHB "dominant attitude" of the district, where one is given. Optional. |

```yaml
---
type: district
fief: [[The Rampart]]
tier: lower
attitude: Pugnacity
exposure: public
canon: core
completeness: stub
---
```

### 03 Cultures

#### `culture` — peoples & ancestries
*All* of `03 Cultures/`, canonical and homebrew alike. The old `type: people` is retired; homebrew ancestries are `type: culture` + `canon: homebrew`.

| Field | Values | Meaning |
|---|---|---|
| `origin` | `native` \| `immigrant` \| `created` \| `ancient` | How they came to be on the peninsula. Optional. |
| `size` | `small` \| `medium` \| `large` | If a Daggerheart ancestry size has been assigned. Optional; mechanics live in [[Conversion Notes]]. |
| `alliance` | as `nation` | If the people maps to a totem-culture bloc. Optional. |

```yaml
---
type: culture
origin: native
size: large
exposure: public
canon: homebrew
completeness: complete
aliases: ["Firbolg", "Firbolgs", "The Quiet Folk", "Grove-keepers"]
---
```

### 04 Factions

#### `faction` — every organized body
Guilds, free leagues, noble houses, the Militia, and other orders/networks. The old `guild` / `faction` / `organization` types collapse into this one, distinguished by `faction-type`.

| Field | Values | Meaning |
|---|---|---|
| `faction-type` | `guild` \| `free-league` \| `house` \| `militia` \| `order` \| `network` | The kind of organization. |
| `hq` | `[[District]]` / `[[site]]` link | Seat of operations. Optional. |
| `sphere` | list | What they do/control (`theft`, `smuggling`, `law-enforcement`). Optional. |
| `leader` | `[[character]]` link | Current head, where known. Optional. |
| `status` | `active` \| `ascendant` \| `declining` \| `defunct` \| `hidden` | In-world condition. Optional. |

```yaml
---
type: faction
faction-type: guild
hq: [[Morgue Street]]
sphere:
  - theft
  - smuggling
  - black-market
leader: 
status: active
exposure: public
canon: core
completeness: complete
---
```

### 05 People

#### `character` — NPCs

| Field | Values | Meaning |
|---|---|---|
| `faction` | `[[faction]]` link or list | Allegiance(s). List if more than one. |
| `location` | `[[fief]]` / `[[district]]` / `[[site]]` link | Where they're usually found (single link — no prose). |
| `ancestry` | `[[culture]]` link | Their people. Optional. |
| `role` | free text | Title or function (`Peer`, `Constable`, `King of Ashes`). Optional. |
| `status` | `alive` \| `dead` \| `undead` \| `missing` \| `cursed` | In-world life-state. |

```yaml
---
type: character
faction:
  - [[Court of Shadows]]
  - [[Acheron]]
location: [[Court of Ashes]]
ancestry: 
role: King of Ashes
status: cursed
exposure: secret
canon: core
completeness: complete
---
```

### 06 History

#### `history` — historical events

| Field | Values | Meaning |
|---|---|---|
| `date` | integer year AF | When it happened. Sortable. Use the earliest year for multi-year events. |
| `era` | `elder` \| `lost-city` \| `free-city` | Which era ([[Timeline]]'s three buckets). |

```yaml
---
type: history
date: 900
era: free-city
exposure: public
canon: core
completeness: complete
---
```

#### `timeline` — the chronology index
Just [[Timeline]] itself. Behaves like a `moc` but kept distinct so it never sweeps into `moc` directory queries.

```yaml
---
type: timeline
exposure: public
---
```

### 07 Cosmology & Magic
Uses `concept` and `deity` (above). No folder-specific type.

### 08 Underground

#### `site` — delve locations & underground features
[[The Sewers]], [[Court of Ashes]], [[The Labyrinth]], [[Marine Ruins]], the vestiges, etc. Distinct from surface `place` because these are the dungeon-crawl layer.

| Field | Values | Meaning |
|---|---|---|
| `layer` | `surface` \| `shallow` \| `deep` \| `labyrinth` | Depth band of the underground stack. |
| `access` | `[[district]]` / `[[place]]` link or list | Where you get in from. Optional. |

```yaml
---
type: site
layer: shallow
access:
  - [[Gamehead]]
  - [[Drakaër]]
exposure: public
canon: core
completeness: complete
---
```

### 09 Campaign

#### `pc` — player characters
A **mechanics-light identity note**, distinct from `character` (NPC) so the party never mixes into NPC rosters. It captures the durable build — who they are and what they play. Live state (current HP, Stress, Hope, gold, trait scores) is *not* stored here; that stays on the app or paper sheet. Narrative lives in the body — see the **Player Character** template in [[Reference#Templates]].

Heritage in Daggerheart is **ancestry + community**. This table splits community into the Cadwallon belonging (`community`, a link into the vault) and the core archetype it maps onto (`community-archetype`).

| Field | Values | Meaning |
|---|---|---|
| `player` | free text | Who plays them. |
| `pronouns` | free text | — |
| `ancestry` | `[[culture]]` link; a list of two for mixed ancestry | Their people, linked to the `culture` notes (core or homebrew). Daggerheart mixed-ancestry characters list both. |
| `community` | `[[fief]]` / `[[culture]]` / `[[faction]]` link | The Cadwallon community they belong to (per [[Conversion Notes]]' community mapping). |
| `community-archetype` | `Highborne` \| `Loreborne` \| `Orderborne` \| `Ridgeborne` \| `Seaborne` \| `Slyborne` \| `Underborne` \| `Wanderborne` \| `Wildborne` (or homebrew) | The core Daggerheart community the Cadwallon one maps onto. |
| `class` | any class in [[Daggerheart Content]] — the 9 core plus the Void classes (Assassin, Bloodhunter, Brawler, Warlock, Witch) | DH class. Free-text so playtest/homebrew classes fit. |
| `subclass` | free text (see [[Daggerheart Content]] for each class's options) | The chosen subclass. |
| `domains` | list of two, from the eleven in [[Daggerheart Content]]: the nine core (`Arcana`…`Valor`) plus the Void `Blood` and `Dread` | The class's two domains; usually fixed by the class. Lets you query who can reach a given domain. |
| `level` | integer 1–10 | Current level. Tier is **derived** (1 → T1, 2–4 → T2, 5–7 → T3, 8–10 → T4), so query on `level` — `tier` stays reserved for fiefs/districts. |
| `status` | `active` \| `retired` \| `dead` \| `guest` | In-play state. |
| `transformation` | `Vampire` \| `Werewolf` \| `Reanimated` \| `Shapeshifter` \| `Ghost` \| `Demigod` | A Void Transformation augmenting the character, if any. Optional. |
| `image` | `[[Portrait.png]]` link | Character portrait, stored in `09 Campaign/Characters/Portraits/`. Embed it in the body with `![[Portrait.png]]`. Optional. |

> [!note] Conventions for this type
> Proper-noun values (`class`, `domains`, `community-archetype`, and totem `culture` on nations) keep their capitalization; only the lowercase-style enums (`status`, `exposure`) are lowercased. `canon` is omitted for PCs — a player creation isn't core-vs-homebrew lore. Numeric build stats (traits, Evasion, thresholds, Proficiency) are deliberately absent: this is the identity note, not the play sheet.

```yaml
---
type: pc
player: 
pronouns: 
ancestry: [[Drakona]]
community: [[Drakaër]]
community-archetype: Highborne
class: Sorcerer
subclass: 
domains:
  - Arcana
  - Midnight
level: 1
status: active
image: 
exposure: public
aliases: []
---
```

#### `thread` — plot threads

| Field | Values | Meaning |
|---|---|---|
| `status` | `open` \| `active` \| `resolved` \| `dormant` | Where the thread stands. |
| `stakes` | free text | One line: what's at risk. Optional. |
| `related` | list of `[[links]]` | NPCs/fiefs/sites the thread touches. Optional. |

```yaml
---
type: thread
status: active
stakes: Desire is waking and the city doesn't know
related:
  - [[Desire]]
  - [[Coiling Emissaries]]
exposure: secret
---
```

#### `session` — session logs

| Field | Values | Meaning |
|---|---|---|
| `date` | real-world date `YYYY-MM-DD` | When you played. |
| `session-number` | integer | Sequence. |
| `present` | list | Who attended. Optional. |

```yaml
---
type: session
date: 2026-06-02
session-number: 1
exposure: public
---
```

---

## Dataview cookbook

Paste these into any note (inside a ` ```dataview ` fence). They run in Obsidian's reader view — they can't be executed from outside Obsidian. `this.file.link` refers to the note the query lives in, which is how the per-fief and per-faction blocks self-populate.

> [!warning] Folder filters are vault-root-relative
> This vault's root is the **`TTRPG`** folder, with **`Cadwallon/`** as a subfolder — so every folder path takes the prefix: `FROM "Cadwallon/05 People"`, not `FROM "05 People"`. A missing prefix returns an *empty* table, not an error. (If the Cadwallon wiki ever becomes its own vault, drop the `Cadwallon/` prefix everywhere.)

**Everything still to write (build backlog):**
````
```dataview
TABLE type, completeness, file.folder AS "Folder"
FROM "Cadwallon"
WHERE completeness = "stub" OR completeness = "draft"
SORT file.folder ASC
```
````

**The GM index — every secret in the vault:**
````
```dataview
TABLE type, exposure
FROM "Cadwallon"
WHERE exposure = "secret" OR exposure = "rumored"
SORT type ASC
```
````

**All homebrew (the authoritative overrides):**
````
```dataview
TABLE type, file.folder AS "Folder"
FROM "Cadwallon"
WHERE canon = "homebrew"
SORT type ASC, file.name ASC
```
````

**Nations grouped by alliance:**
````
```dataview
TABLE culture, race, embassy
FROM "Cadwallon/01 World/Nations"
WHERE type = "nation"
GROUP BY alliance
```
````

**Districts of this fief** (paste into each `fief` note — self-filters):
````
```dataview
TABLE tier, attitude, completeness
FROM "Cadwallon"
WHERE type = "district" AND fief = this.file.link
SORT attitude ASC
```
````

**Everyone who belongs to this faction** (paste into each `faction` note):
````
```dataview
TABLE role, location, status
FROM "Cadwallon"
WHERE type = "character" AND contains(faction, this.file.link)
SORT file.name ASC
```
````

**NPCs by fief** (a master roster):
````
```dataview
TABLE location AS "Found in", faction AS "Allegiance", status
FROM "Cadwallon/05 People"
WHERE type = "character"
SORT location ASC
```
````

**The history timeline, sorted:**
````
```dataview
TABLE date AS "Year AF", era
FROM "Cadwallon/06 History"
WHERE type = "history"
SORT date ASC
```
````

**Open plot threads:**
````
```dataview
TABLE status, stakes
FROM "Cadwallon/09 Campaign"
WHERE type = "thread" AND status != "resolved"
SORT status ASC
```
````

**The party roster** (paste into [[Party]]):
````
```dataview
TABLE ancestry AS "Ancestry", community AS "Of", row["community-archetype"] AS "Archetype", class, level, status
FROM "Cadwallon/09 Campaign"
WHERE type = "pc"
SORT level DESC, file.name ASC
```
````

> [!warning] Hyphenated field names in DQL
> Dataview reads a bare `community-archetype` as *subtraction* (`community` minus `archetype`). Any kebab-case field must be accessed as `row["community-archetype"]` in a `TABLE`/`WHERE`/`SORT` expression — same for `ruling-house`, `faction-type`, etc. Plain non-hyphenated fields (`class`, `level`, `status`, `fief`) need no brackets.

**Underground by depth:**
````
```dataview
TABLE layer, access
FROM "Cadwallon/08 Underground"
WHERE type = "site"
SORT layer ASC
```
````

**Orphans — notes nothing links to** (find the disconnected):
````
```dataview
LIST
FROM "Cadwallon"
WHERE length(file.inlinks) = 0 AND type != "moc" AND type != "reference"
SORT file.name ASC
```
````

**Schema drift detector — notes missing a `type`:**
````
```dataview
LIST
FROM "Cadwallon"
WHERE !type
```
````

> [!tip] `dataviewjs` for the harder questions
> Anything needing computed columns, multi-hop link-walking, or custom grouping (e.g. "NPCs whose faction is declining") wants a `dataviewjs` block instead of plain DQL. Ask and one can be written for the specific view.

---

## Where existing notes deviate (migration targets)

The vault predates this schema, so most notes need normalizing. The recurring fixes:

- `type: people` → `type: culture` (canonical cultures)
- `type: guild` / `type: organization` → `type: faction` + a `faction-type`
- `type: concept` on gods → `type: deity`; on geography (e.g. [[Aarklash]]) → `type: place`
- `status: stub` → `completeness: stub`; `status: homebrew` → `canon: homebrew`; `status: alive` stays as `status` (in-world)
- quoted links `"[[X]]"` → unquoted `[[X]]`
- compound link strings (`faction: "[[A]] / [[B]] (origin)"`, `location: "... beneath [[X]]"`) → atomic lists / single links
- missing `type` on `Houses of Peers.md`, `Reference.md`, `Conversion Notes.md`, the `Homebrew.md` indexes, and the `09 Campaign` files → add `moc`/`reference`
- the `Bismuth von Kraken` note is missing its `# H1` title (see [[Reference#File Structure]])

This is a mechanical pass and can be done folder-by-folder on request.

## See Also

- [[Reference]] — prose style, canon hierarchy, note templates, and the AI operating guide
- [[Conversion Notes]] — Daggerheart mechanical mappings (kept *out* of frontmatter)
- [[Glossary]] · [[Calendar]] — the other reference docs
