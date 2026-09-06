---
type: reference
exposure: secret
aliases: ["Themes", "Suno Cues"]
---
# Themes

Instrumental cues, one per character. Every prompt is Style-field only — **set the Instrumental toggle on**; there is no Lyrics field to paste. Built on V5.5 grammar (Style cap ~1,000 chars; all prompts below sit well under it).

## The locked spine

Album coherence comes from keeping the texture and era layers byte-identical across every track and varying only genre, instruments, mood, tempo, and key. Every cue already ends with this exact string:

```
mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```

Don't edit it per-character. If the whole set needs to move — grittier, cleaner, a different year — change it once and regenerate everything, or the tracks stop sounding like they came from the same city.

## The Piper's figure

Bunting's four-note descending phrase is the arc's root motif. It appears by description in **Toby** (the whistle quote — the tell) and, transformed, in **Ida Maas** (her father's fanfare in minor).

Be warned: **Suno cannot carry a literal melody between generations.** Identical descriptive wording buys a family resemblance, not the same notes. If you want an actual quotation the players can recognize by ear, generate Bunting first, then build Toby's and Ida's cues as **Covers** of that track (Audio Influence 55–65%) rather than fresh generations. That's the only reliable route, and it costs a take or two of experimentation.

## Settings (all tracks)

| Setting | Value |
|---|---|
| Model | V5.5 |
| Mode | Custom, Instrumental toggle ON |
| Weirdness | 35% |
| Style Influence | 90% |
| Takes before judging | 4 |

Two of four takes will be wrong in ways that aren't the prompt's fault. Exceptions are noted per character. Where a cue asks for something deliberately broken (Shale) or structurally counted (Pell), the tuning note says so.

---

> [!note] Where the cues are
> Each character's cue lives in that character's note under `## Theme (Suno)` — see [[People]]. Only the shared material is here.

---

## Tier C — the precinct bed (shared)

*One cue for all of Tier C. Individual themes for bit players cost generations and buy nothing; vary this one instead.*

```
Noir Jazz, ambient. Walking upright bass and brushed snare loop beneath a room of typewriters, ringing telephones, and a radiator; a tenor saxophone offers only occasional two-note comments. Procedural, indifferent, ordinary. 96 BPM, A minor, 4/4, medium swing, mid-distance room mix. + this is background rather than a theme, and nothing in it should ask to be listened to, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~474 chars)*

**Tuning:** Per-name variants, one axis each: Boyd `+ a young tenor sax phrase that tries to finish and gets cut off`; Kowalczyk `+ drop the sax entirely`; Brack `+ raise the telephones over the band`; Feeny `+ add switchboard tones` (this ties her to Mabel Cho, deliberately); Dubcek `+ replace the radiator with harbor water and a distant bell`. Feeny and Dubcek have moved up to Tier B but still work off this bed rather than taking standalone cues; add Herzog as `+ replace the typewriters with a single copy desk and a telephone answered before the second ring` if you want a newsroom variant of the same texture; Ard `+ replace the typewriters with a squash ball against a wall and a committee gavel`.

---

## The investigators

Two cues each: a **Logos** theme for the character at rest, and a **Mythos** cue for surfacing (one action, a scene, or an Incarnation; see [[Two Sheets]]). Built only from what the players wrote and the Mythos figure; nothing about their pasts. If a player wants a different sound, theirs wins. These are not on the public PC pages.

### Arthur Rook — Logos
*Down on his luck. A detective's patience and a draft-dodger's exits.*

```
Noir jazz, slow. A muted trumpet carrying a tired, careful melody over brushed snare and a walking upright bass, a rainy-window piano answering in the gaps, one revolver-cylinder click used as a rhythmic accent every sixteen bars. Patient, worn, watching the door. 70 BPM, D minor, 4/4, small office mix. + the trumpet never resolves its last phrase, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~430 chars)*

### Arthur Rook — Mythos: The Tower
*Illusions fail. The wrong path comes down.*

```
Orchestral noir, sudden. A single struck bell followed by a descending brass chord that collapses into low strings and timpani, then silence, then the same muted trumpet from before playing alone in a much larger room. Revelation, then rubble. 60 BPM, D minor, free meter, cathedral-to-office mix. + a stone door closing somewhere far off at the very end, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~420 chars)*

### Zu Cheng — Logos
*Little China, uphill. A Taoist who is usually right about it.*

```
Cool jazz with Chinese instrumentation. A clean-toned electric guitar playing a spare, superior melody over a soft ride cymbal and upright bass, a guzheng answering in short precise phrases, a wooden fish block keeping a second, slower time. Composed, disdainful, exact. 84 BPM, A minor pentatonic, 4/4, temple-courtyard mix. + the guzheng corrects the guitar once, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~440 chars)*

### Zu Cheng — Mythos: Sun Wukong
*Knowledge for Strength. The Monkey is out.*

```
Percussive, driving. Chinese opera drums and gongs breaking into a hard-bop rhythm section at double time, a suona blaring a war-cry figure over it, the guzheng from before now hammered, every phrase landing like a blow. Joyous, violent, immortal. 168 BPM, A minor pentatonic, 4/4, wide live-room mix. + one bar of total silence before the last hit, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~420 chars)*

### Jack Rivers — Logos
*Chain-smoking, dive-bar, a joker who keeps his distance.*

```
Barroom jazz, loose. An upright piano slightly out of tune playing a wry, shuffling melody over a brushed kit and a lazy bass, a harmonica commenting from the far end of the bar, glasses and a slow ceiling fan in the room. Easy, amused, one step back from everyone. 96 BPM, F major, 4/4 shuffle, end-of-the-bar mix. + the piano quotes a different song for two bars and grins about it, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~450 chars)*

### Jack Rivers — Mythos: Coyote
*Herald of the strange. The dark inside the closet.*

```
Dark folk-jazz, uncanny. A bowed double bass and a lone clarinet in a minor mode trading a crooked, curious melody, a soft frame drum, wind through a gap somewhere, and under it all a low animal breath kept in time. Whimsical, wrong, waiting around the bend. 72 BPM, E minor, 6/8, night-street mix. + the clarinet laughs once, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~400 chars)*

**Tuning:** Generate the Logos cues after the Tier A board so they sit inside the same city. The Mythos cues should share one instrument with their Logos cue (the trumpet, the guzheng, the clarinet answering the harmonica) so surfacing sounds like the same person.

## Locations

Twelve location beds (the pier at dawn, the print shop, Tin City at night, the Half Note on a Thursday, the precinct desk, the Exchange upstairs, the Model Room, the Span field office, Studio B, Delancey Street, the agency, the temple hall, the morgue) are in [[Location Prompts]] with their splash-art prompts. Same spine.

## Theme Workshop Notes

- **Log three things per track** as you generate: the Style field verbatim, the take number you kept, and whatever you had to change. The third is the one everyone skips and the one that saves the most time on the next batch.
- **Unexpected-cue inventory** — the deliberate anachronisms and outside-genre intrusions, so you can dial the whole set toward or away from strangeness: Bunting (tape-loop phasing), Toby (boogaloo, four years early), Klein (cantorial cello over industrial percussion), Okafor (talking drum), Ottilie (Weimar cabaret on scrap), Sato (koto), Milner (Baroque counterpoint), Lupo (surf guitar vs. swing brass), Cutty (1930s field-recording fidelity — the one intentional break in the spine), Day (AM-speaker collapse).
- **Diegetic vs. score.** Bunting's tune, Cutty's playing, and Okafor's shop radio can exist inside the fiction; everything else is score. Keep that line clear at the table or the players will start listening for clues in the underscore.
- **Batch order:** Bunting first (everything references it), then the Tier A board, then decoys, then the working ring. Tier C's shared bed can wait until the rest of the set has settled its texture.
- **Two cues added in draft-2:** Herminia Vega (the only domestic cue in the set — generate it late, after the rest of the score has established how grim the baseline is, so the contrast lands) and Walt Herzog (short, unresolved, cheap to generate).
