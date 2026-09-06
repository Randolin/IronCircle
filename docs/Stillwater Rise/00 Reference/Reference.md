---
type: reference
exposure: secret
aliases: ["Reference", "Style Guide"]
---
# Reference

Style guide and conventions for the Stillwater Rise wiki. This file governs **prose and house style**; [[Schema]] governs **frontmatter**; [[System Notes]] governs **mechanics**. Read all three before editing.

The folder mirrors [[Cadwallon]]'s layout so the two campaigns work the same way. What differs is tone, and the visibility default.

## Visibility

**Everything in this folder is GM-only unless its frontmatter says `exposure: public` or `exposure: rumored`.** The site build treats a missing `exposure` under `Stillwater Rise/` as `secret`. (Cadwallon defaults the other way.) Public today: the landing page, [[Party]] and the player characters, [[The Agency]], and a handful of place and institution stubs that repeat only what the landing page already says.

Making something player-visible is a deliberate act: flip the field, then reread the note for anything that shouldn't be there. `[!secret]` callouts do **not** hide text — the page publishes whole or not at all.

## Tone

**Reference material is dry.** Character notes, the danger board, timelines, design docs: plain, pragmatic, no atmosphere. Stylized prose belongs only in in-world content — voice lines, read-aloud text, documents the players can hold.

The lesson from Heliakros: well-paced, but revealed rather than deduced. Every design choice here serves players working it out — the three-layer culprit structure, suspects who deflate slowly, sources distinguished by *access cost* rather than payload.

## File structure

Every populated note has:

- **Frontmatter** conforming to [[Schema]] — exactly one `type`, `exposure` set explicitly.
- **H1 title** matching the file name.
- For characters: an italic epithet line, then a **three-line pitch** in plain language: `**Pitch:**` (who they are and where they sit in the case, one or two sentences), `**Wants:**` (one line), and `**Gives:**`, `**Threat:**`, or `**Clock:**` (what the players get from them, or what's coming). Someone reviewing the roster should be able to read only those three lines and run the character. Under `## Detail`: bullets only — `**Look:**`, `**Manner:**`, then a handful of facts the pitch left out (clocks, costs, what they look guilty of, what they give after they deflate). Voice lines stay as a short list. Image prompts and the stat block stub go under `## Prompts`. Then `## Theme (Suno)`.
- **Write the pitch like a young-adult novel, not a noir paperback.** Short sentences. Say what happens. No metaphors in the pitch; save them for the voice lines.
- For places and institutions: a one-line tag, a short overview, who's there, and hooks where useful.

Length: a character note should read in under a minute. Pitch plus a dozen bullets; the prompts and theme block are reference, not reading. Places and institutions 100–300. The moc notes ([[People]], [[The City]], [[Institutions]], [[Mythos]]) hold the tables that cut across entries.

## The tiers

The tiers sort by **relationship to the killings**, not by importance or screen time.

- **Tier A — the board.** Anyone who had a hand in the prior deaths, will have a hand in the next ones, or is shaped enough like a killer to survive scrutiny. Fifteen names; the `board` field splits them into `chain`, `suspect`, and `next`.
- **Tier B — the working surface.** The people the players spend sessions with. Each is a route into a Tier A name; the `opens` field says which. Distinguished by *what they cost*, not what they hold, because payloads overlap by design. The cost list lives in [[People]].
- **Tier C — the world.** Incidental texture. Promote anyone who earns a third scene.
- **Agency** and **victim** are their own tiers so they never sort into the board.

The [[Danger Board]] cuts across all three and sorts by *actor*: Bunting kills entries; Maas kills nobody (institutional threat only); Weaver harvests: the relocation feeds a web of wire and print she sits at the center of, and she kills whatever threatens the web's integrity.

## Callout types

- `> [!hook]` — seeds
- `> [!note]` — table-level meta or reminders
- `> [!warning]` — placeholders and to-dos
- `> [!secret]` — allowed, but see Visibility: it decorates, it doesn't hide

## Conventions

- Wikilink every named entity on first mention within a note: `[[Manny Bunting]]`, `[[The Flats]]`. File names are the everyday name (`Cutty Sloan`, `Gerry Fitch`, `Ottilie Mauser`); formal names are aliases.
- Dates inside the fiction are **Day N** relative to the discovery of the body (Day 1). The [[Timeline]] is authoritative; character notes' clocks must agree with it.
- No predominantly Greek cast; no music-heavy theming beyond the Piper; diversity is an active priority — [[The Flats]] is a Black and Puerto Rican district.
- Corrections from Aaron are applied directly, not restated.

## Image prompts

Style is handled downstream in ComfyUI, so every prompt is a **pure subject core** with zero rendering or medium language. Each character carries two:

- **Headshot** — opens *"Bust-length view, cropped just below the collarbone"* and closes *"At the bottom edge of the frame only: [collar]"*. Each character's neckline is specified and distinct; if a tie sneaks onto an open-collared character, weight `bare at the throat` or put `necktie` in the negative for that generation only.
- **Full body & wardrobe** — always **standing**, no furniture, props limited to what's carried or worn, face **unspecified** (tiny faces render badly; fix with a face-detailer pass, not prompt language).

Signature colors only where they're wardrobe facts. If a character drifts across generations, promote their two most distinctive features to the first sentence. Silhouette signatures for group shots: the two-tone suit, the seven-medallion necklace, the pearl choker and cigarette holder, the paper sack, the leather apron, the headphone collar, the barber's smock, the long silver hair over the ears; in the working ring the backwards cigarette, the headset band, the army-blanket cape, the loupe headband, the toothpick, the no-gold plainness, the walrus mustache, the eyeshade. Herminia Vega's is deliberately the plainest on the board.

## Suno cues

One instrumental cue per character, in that character's note under `## Theme (Suno)`. Every cue ends with the locked spine string, byte-identical across all tracks. Shared settings, the spine, the Piper's figure, and workshop notes are in [[Themes]]. Don't edit the spine per-track.

## For AI tooling

1. [[Schema]] is authoritative for frontmatter. Match an existing `type`; add new fields to Schema first.
2. Stamp full frontmatter on every new note, `exposure` included.
3. Keep reference notes dry. Don't add atmosphere to a roster entry.
4. Never move, copy, or summarize a `secret` note into a `public` one without asking.
5. At the end of a working session, run the wrap workflow in [[Campaign]] (also `/wrap-session`).
