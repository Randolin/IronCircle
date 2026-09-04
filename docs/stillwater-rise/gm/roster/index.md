---
title: Roster
exposure: secret
campaign: Stillwater Rise
---

# Roster

Companion to the [campaign doc](../campaign.md) and the [danger board](../danger-board.md). Narrative identity, table handles, visuals, and prompt text. Stat blocks are stubbed for later mechanical passes once the system question (Daggerheart vs. hybrid) is settled.

## How the tiers work

The tiers sort by **relationship to the killings**, not by importance or screen time. A Tier B character may get more table time than half of Tier A; that isn't a demotion, it's the job.

- **Tier A — the board.** Anyone who had a hand in the prior deaths, will have a hand in the next ones, or is shaped enough like a killer to survive scrutiny. This is the list the players are trying to shorten. Six of the fourteen names on it are innocent of murder and guilty of something else.
- **Tier B — the working surface.** The people the players actually spend sessions with. Each one is a route into a Tier A name: what that person did, why, and where the paper is. Sorted below by *who they open* and *what they cost*, because their payloads deliberately overlap and the scenes have to be distinguished by price rather than by prize.
- **Tier C — the world.** Incidental. Texture, atmosphere, the occasional receipt. If one of them gets more than two scenes, promote them and rewrite the entry.

**On the name.** *Stillwater Rise* is the Authority's brand for the whole riverfront project — the Span, the cleared Flats, and the plaza at its foot, sold as one thing. The word does triple duty and none of it is accidental: Maas means elevation and civic ascent; Weaver *is* the still water, and her rise from silk money to a media empire in under six years is the mythic tell; Bunting's marks walk calm into still water, and his own rise never came. Eleven people went into that river and none of them came back up. Vera is the only one who rose.

Cutting across all three: **the danger board** — who dies or gets destroyed if the players are slow. It lives in its own file — [danger-board.md](../danger-board.md) — because it changes every session.

---

## Prompt Convention (subject-only)

Style is handled downstream in ComfyUI (moodboard, style transfer, LoRAs), so every prompt below is a **pure subject core**: who the character is visually — with zero rendering or medium language. Each character carries **two prompts**: a *headshot* (face, hair, expression — the identity anchor, and the better LoRA/reference-training source) and a *full body & wardrobe* (build, posture, clothing, props — the recognition-at-distance layer). Face details repeat only minimally in the body prompt so the two don't fight; generate the headshot first if you're building a character reference, then condition the body shot on it.

Signature colors are kept **only where they're wardrobe facts** (Bunting's two-tone suit, Ottilie's medallions), not as palette direction — recolor freely at the style layer.

Full-body convention: every body prompt is **standing** — no chairs, stools, bars, desks, or scene furniture; props are limited to what's carried or worn. Keep faces *unspecified* in body prompts (no eye color, no expression detail) — at full-figure scale the model renders tiny faces badly (the black-eyes-with-a-white-dot artifact); the face belongs to the headshot, and the reliable fix for body-shot faces is a face-detailer/inpaint pass in ComfyUI, not prompt language.

Headshot framing convention: every headshot opens with **"bust-length view, cropped just below the collarbone"** and closes with **"at the bottom edge of the frame only: [collar description]"** — the two phrases together pin the crop and stop the model from inventing a default collared-shirt-and-black-tie. Each character's neckline is specified and distinct; if a tie still sneaks onto an open-collared character, add `bare at the throat` weight or put `necktie` in your negative for that generation only.

---

## Files

- [The victim](victim.md)
- [Tier A — the board](tier-a.md)
- [Tier B — the working surface](tier-b.md)
- [The agency](agency.md)
- [Tier C — the world](tier-c.md)
- [Character themes (Suno)](../themes.md)

## Prompt workshop notes
- All prompts are style-free subject cores — pair them in ComfyUI with your moodboard/style-transfer/LoRA layer; iterate one clause at a time.
- Silhouette signatures for group/scene compositions (where faces shrink and identity must survive at distance): the two-tone suit, the seven-medallion necklace, the pearl choker and cigarette holder, the paper sack, the leather apron, the headphone collar, the barber's smock, the long silver hair over the ears — and in the working ring: the backwards cigarette, the headset band, the army-blanket cape, the loupe headband, the toothpick, the no-gold plainness, the walrus mustache, the eyeshade.
- If a character drifts across generations, the fix is usually to promote their most distinctive two features (Bunting: suit + case; Rimm: eyes + gold teeth; Ottilie: medallion necklace + braid; Viv: chignon + choker) to the first sentence.
- Stat blocks: run `/adversary` passes (daggerheart-forge) once the system question settles; profiles above carry the narrative fuel those blocks need.
- Herminia Vega's silhouette signature is deliberately the plainest on the board: housedress, cardigan, slippers, beaded glasses chain. She should be the only figure in a group composition who reads as *not dressed for anything*.
