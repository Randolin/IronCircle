# Reference

Style guide and conventions for the Cadwallon wiki. Read this before populating other notes; follow the templates below for consistency. This file governs **prose and house style**; [[Schema]] governs **frontmatter/metadata**; [[Conversion Notes]] governs **Daggerheart mechanics**.

## Tone

Field guide, not encyclopedia. Sigil-of-Planescape energy — colorful, scuzzy, lived-in. Evocative one-liners over paragraphs of exposition. A casual reader should grasp a note's vibe in 10 seconds and find a hook within 30.

## Canon Hierarchy

When the wiki has multiple sources of truth, resolve in this order:

1. **`Homebrew.md` files** in each category — our table's invented, replaced, or overridden material. **Authoritative.** (In frontmatter, such notes carry `canon: homebrew`.)
2. **Populated canon notes** — material drawn from the official source books (PHB, Secrets Vol 1, Marine Ruins). These carry `canon: core`.
3. **Source PDFs in `Rulebooks/`** — fall back here only when the wiki hasn't captured something yet.

If a canon note and a `Homebrew.md` entry conflict, **the homebrew wins.** When AI tooling answers questions about any category, it should check that category's `Homebrew.md` first.

## File Structure

Every populated note has:

- **Frontmatter** (Obsidian Properties) for metadata — **conforming to [[Schema]]**. Exactly one `type`; universal fields (`exposure`, `canon`, `completeness`) as applicable; links stored unquoted.
- **H1 title** matching the filename
- **Pull-quote or tagline** as the first line — a Cadwë saying, source quote, or one-line vibe statement
- **Short overview** (2–4 sentences) — what is this thing
- **Bulleted sub-sections** for details
- **Hooks** at the end — 3–5 adventure seeds where they make sense

## Length Budget

- Districts, NPCs, locations: 150–300 words
- Fiefs, major concepts: 300–600 words
- Anything longer probably wants to split

## Conventions

- Every named entity wikilinked on first mention
- Source quotes in `>` blockquotes with attribution
- Daggerheart conversion details belong in `Conversion Notes.md`, not inline in canon notes
- Metadata belongs in frontmatter per [[Schema]], not buried in prose — and prose belongs in the body, not in frontmatter values

### Callout Types

- `> [!hook]` — adventure seeds
- `> [!secret]` — GM-only content (pairs with `exposure: secret`)
- `> [!quote]` — rumors, what people say
- `> [!note]` — table-level meta or reminders

## Templates

Frontmatter in these templates conforms to [[Schema]]; see that file for the full `type` vocabulary and every field's allowed values. Below are the four most common.

### Fief

````
---
type: fief
tier: lower | upper
ruling-house: [[House note]]
peer: [[Peer character]]
exposure: public
canon: core
completeness: draft
---

> Evocative one-line tag.

**Vibe:** 2–3 sentences. What you feel walking in.

## Districts
- [[District]] — one-line flavor

## Power & Politics
- Who rules, what they care about, current tensions

## NPCs of Note
- [[Name]] — role

## Hooks
> [!hook] Title
> Seed in 1–2 sentences.
````

### District

````
---
type: district
fief: [[Fief]]
tier: lower | upper
attitude: Style | Subtlety | Opportunism | Pugnacity
exposure: public
canon: core
completeness: stub
---

> One-line tag.

**Day:** what it looks like.
**Night:** what it looks like.

## Locations
- **Name** — one-line description

## NPCs
- [[Name]] — role

## Hooks
> [!hook] Title
> Seed.
````

### Character

````
---
type: character
faction: [[Faction]]
location: [[Fief or district or site]]
ancestry: [[Culture]]
role: 
status: alive | dead | undead | missing | cursed
exposure: public
canon: core
completeness: draft
---

> Role-and-attitude one-liner.

**Wants:** one sentence.
**Will:** what they'd do for it.
**Won't:** their line.

> [!secret] What they're hiding
> ...

## Hooks
> [!hook] ...
````

### Player Character

A mechanics-light identity note for a party member (`type: pc`). Build and identity live in the frontmatter per the `pc` schema in [[Schema]]; live stats (HP, Stress, Hope, traits, gold) stay on the app or paper sheet. Distinct from the **Character** (NPC) template above so the party never mixes into NPC rosters.

````
---
type: pc
player: 
pronouns: 
ancestry: [[Ancestry]]
community: [[Cadwallon fief / culture / faction]]
community-archetype: Highborne | Wanderborne | ...
class: 
subclass: 
domains:
  - 
  - 
level: 1
status: active
image: 
exposure: public
---

![[Portrait.png]] *(drop a portrait into `Characters/Portraits/`; see [[Daggerheart Content]] for class/community options)*

> A line in the character's own voice.

**Concept:** one line — who they are at a glance.

## Look
Appearance, bearing, the detail people remember.

## Background
Where they came from and why they're in Cadwallon — the Call pulled them here, or they were born to it (see [[Cadwë Dream]]).

## Drives
**Wants:** the goal that pulls them forward.
**Bond:** the person or principle they won't abandon.
**Flaw:** the lever the city can pull.

## Experiences
- *Experience Name* (+2) — one line on how it reads in the fiction

## Connections
- [[Other PC]] — the tie between you (the session-zero connection)
- [[NPC]] / [[Faction]] — a standing relationship in the city

## Hooks
> [!hook] Personal thread
> A seed tied to this character; link it to a [[Plot Threads|plot thread]] where you can.
````

### Concept

For metaphysical or lore concepts like Desire, the Arcana, the Labyrinth. (Gods use `type: deity`; physical places use `type: place` — see [[Schema]].)

````
---
type: concept
exposure: public | rumored | secret
canon: core
completeness: draft
---

> One-line tag.

## What It Is
2–3 paragraphs.

> [!secret] What's Actually Going On
> GM truth.

## Why It Matters Now
- 
````

---

## For AI Tooling: Dataview & Frontmatter

Operating instructions for an AI assistant working in this vault. Treat this section as a skill: load it before touching metadata or writing queries.

### Ground rules

1. **[[Schema]] is authoritative for all frontmatter.** Read it before creating or editing any note's properties. Match an existing `type`; never invent a field that isn't in Schema. If a new field is genuinely needed, add it to [[Schema]] first, then use it — otherwise it won't be queryable and the next session won't know it exists.
2. **Stamp full frontmatter on every new note**, per its `type`'s template — including the universal fields (`exposure`, `canon`, `completeness`). A note with no `type` is invisible to Dataview.
3. **Follow the link convention exactly:** wikilinks in frontmatter are **unquoted** (`fief: [[The Rampart]]`), multi-value link fields are YAML lists, values are atomic, years are bare integers. (Full rules in [[Schema#Conventions]].)
4. **When you notice schema drift while editing a note for another reason, normalize that note's frontmatter** as part of the edit. Don't leave a note half-migrated.
5. **Respect the canon hierarchy.** Before answering a lore question about a category, check that category's `Homebrew.md` and any `canon: homebrew` notes first; they override source canon.

### Working with Dataview

- **Dataview runs only inside Obsidian's renderer.** An AI cannot execute a query or report its results from outside the app. When asked for "a list of X," the correct deliverable is a **DQL block written into the relevant note**, not a fabricated table of results. Never invent query output.
- **Use the cookbook.** [[Schema#Dataview cookbook]] has paste-ready queries for the common views (build backlog, GM secret-index, homebrew roster, NPCs by fief, per-fief district lists, history timeline, plot threads, orphans). Start there and adapt.
- **Self-filtering blocks** (`this.file.link`) are how index views live inside the entity they describe — e.g. the "districts of this fief" block goes in each fief note and needs no editing per-fief. Prefer these over hand-maintained lists.
- **Don't break existing query blocks.** When editing a note that contains a ` ```dataview ` or ` ```dataviewjs ` fence, leave it intact unless explicitly asked to change it.
- **Reach for `dataviewjs`** only when plain DQL can't express the view (computed columns, multi-hop link-walking, custom grouping). Otherwise prefer readable DQL.

### Quick reference

- Full `type` vocabulary, per-type fields, and templates → [[Schema]]
- Prose style, tone, length, callouts → this file
- Daggerheart mechanical conversion → [[Conversion Notes]]
- In-world terminology → [[Glossary]] · dating → [[Calendar]]
