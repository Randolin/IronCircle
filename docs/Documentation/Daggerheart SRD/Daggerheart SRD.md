---
type: reference
exposure: public
source: Daggerheart SRD 2.0 (2026-08-25)
aliases: ["Daggerheart SRD", "SRD", "Daggerheart Rules"]
---
# Daggerheart SRD

The Daggerheart System Reference Document 2.0 (25 August 2026), split into eleven markdown files. **This folder is the rules authority for every Daggerheart table in this wiki** (Cadwallon, Fate Foretold, Stillwater Rise). The text is machine-extracted from the PDF: prose is reliable, tables lost their columns, and a handful of headings are mangled. When the wording matters, the PDF wins; it's at `C:\Obsidian\Documentation\Daggerheart\` and at [daggerheart.com](https://www.daggerheart.com/).

## Sections

| File | PDF pages | Contents |
|---|---|---|
| [[01 Introduction and Character Creation]] | 3–6 | What the SRD is, the basics, character creation steps, Experiences, domain cards, starting equipment |
| [[02 Domains and Classes]] | 7–31 | The ten domains; the thirteen classes with subclasses and class features (Assassin, Bard, Brawler, Druid, Guardian, Ranger, Rogue, Seraph, Sorcerer, Warlock, Warrior, Witch, Wizard); leveling; tag team |
| [[03 Ancestries, Communities, Transformations]] | 32–45 | Ancestries, communities, transformation templates |
| [[04 Core Mechanics]] | 46–54 | Flow of the game, the spotlight, action rolls and Hope/Fear, special rolls (trait, spellcast, reaction, group, tag team), advantage, combat, Evasion, thresholds, Stress, attacking, damage, range and movement, conditions, downtime, death, leveling, multiclassing |
| [[05 Equipment]] | 55–84 | Weapons by tier, the combat wheelchair, armor, loot, consumables, gold |
| [[06 Running an Adventure]] | 85–92 | GM principles, core GM mechanics, **Difficulty benchmarks (p. 88)**, GM moves, countdowns |
| [[07 Adversaries]] | 93–158 | Stat block anatomy, building battles, Tier 1–4 adversaries |
| [[08 Environments]] | 159–182 | Environment stat blocks, Tier 1–4 |
| [[09 Additional GM Guidance and the Witherwild]] | 183–189 | Additional GM guidance; the Witherwild campaign frame |
| [[10 Supplemental Campaign Mechanics]] | 190–205 | Faction tracking, everyday-hero equipment, feasts, grimdark, tech, western, colossal adversaries, floating magic school, fairy tale, monster hunting, hex crawl |
| [[11 Domain Card Appendix]] | 206–224 | Every domain card by domain and level |

## How to find things (rules for Claude and for people)

1. **Every PDF page is marked** in the markdown as `<!-- SRD p.N -->` followed by a visible `*SRD p. N*`. Cite rules as **SRD p. N**, and only from a page you actually read.
2. **Grep for the page marker first, then the term.** `grep -n "SRD p.88" "06 Running an Adventure.md"` gets you to the Difficulty benchmarks. Don't read a 290 KB adversary file top to bottom; find the marker and read a window.
3. **Headings are `##` for the PDF's outline entries and `###` for the in-page caps headings.** A `###` heading that reads oddly ("Making Moves &" on one line, "Taking Action" on the next) is a two-line heading the extractor split; read both.
4. **Tables are flattened.** A benchmark or weapon table appears as one line per row with the columns run together. The numbers are right; the alignment isn't. Reconstruct in your head or check the PDF.
5. **Adversaries and environments** are one stat block per `###` heading, in tier order. Grep the name; the block runs until the next `###`.
6. **Domain cards** live twice: summarized under the class in file 02 and in full in file 11. Use file 11 for card text.
7. **Void content** (Assassin, Bloodhunter, Brawler, Warlock, Witch, and the transformations) is in this SRD 2.0 as core. Cadwallon's [[Daggerheart Content]] note still flags them "verify"; this document is now the verification.
8. **Don't edit these files by hand.** They're regenerated from the PDF by `tools/srd_split.py`. Corrections go in a campaign's own reference notes (for Stillwater Rise, `00 Reference/System Notes.md`), not here.

## Quick lookups

| Need | Where |
|---|---|
| Action roll procedure, Hope and Fear | [[04 Core Mechanics]], SRD p. 47–49 |
| Difficulty benchmarks by trait (5 / 10 / 15 / 20 / 25 / 30) | [[06 Running an Adventure]], SRD p. 88 |
| GM moves, spending Fear | [[04 Core Mechanics]] p. 48; [[06 Running an Adventure]] p. 86–87 |
| Group action and tag team rolls | [[04 Core Mechanics]], SRD p. 48 |
| Damage thresholds, HP, Stress, conditions | [[04 Core Mechanics]], SRD p. 50–51 |
| Downtime moves, death moves | [[04 Core Mechanics]], SRD p. 51–53 |
| Countdowns | [[06 Running an Adventure]], SRD p. 91 |
| Adversary stat block anatomy; building a battle | [[07 Adversaries]], SRD p. 93–95 |
| A specific adversary or environment | grep its name in 07 or 08 |
| A domain card's full text | [[11 Domain Card Appendix]] |
| Experiences | [[01 Introduction and Character Creation]], SRD p. 5 |

## License

This document, including the Witherwild Campaign Frame, is considered Public Game Content per the Darrington Press Community Gaming License. Please read the Darrington Press Community Gaming License before using this material. © 2026 Critical Role LLC. All rights reserved. For more information, please visit [darringtonpress.com/license](https://www.darringtonpress.com/license). SRD Writer: Rob Hebert. Technical Editor: Shawn Banerjee.

This wiki is a non-commercial, private-table reference. Daggerheart and all related marks are the property of Critical Role LLC and Darrington Press; this wiki is not affiliated with or endorsed by them.
