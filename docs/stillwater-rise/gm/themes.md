---
title: Character Themes — Suno
exposure: secret
campaign: Stillwater Rise
---

# Character Themes — Suno Prompts

Instrumental cues, one per character. Every prompt is Style-field only — **set the Instrumental toggle on**; there is no Lyrics field to paste. Built on V5.5 grammar (Style cap ~1,000 chars; all prompts below sit well under it).

## The locked spine

Album coherence comes from keeping the texture and era layers byte-identical across every track and varying only genre, instruments, mood, tempo, and key. Every prompt below already ends with this exact string:

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

## The victim

### Vera Kestrel — the victim

*The archive, the zine, the roll. Her theme should sound like work, not like mourning.*

```
Folk, chamber jazz. Fingerpicked nylon-string guitar is the central voice, answered by a lone muted trumpet; upright piano enters only in the last third; the percussion is a manual typewriter, keys and carriage return, played in strict time. Stubborn and unglamorous, small and unafraid, a woman working late at a kitchen table. 84 BPM, D minor, 4/4, sparse arrangement. + close-mic field-recording intimacy, but no rustic Americana twang, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~539 chars)*

**Tuning:** If it turns sentimental, drop `muted trumpet` and let the typewriter carry the second half alone.

---

## Tier A — the chain

### Manny Bunting — the Piper

*The compulsion tune itself. Play it diegetically — Toby humming, the Half Note bandstand, the pier. This is the arc's root motif; generate it first.*

```
Cool Jazz, solo instrumental. Unaccompanied tenor saxophone carries the entire piece: a slow four-note descending figure repeated with tiny variations, answered only by one distant upright bass note and a soft brushed cymbal. Courteous and terrible, a man knocking politely at a door. 58 BPM, C-sharp minor, rubato, no drum kit, long silences between phrases. + the repeated figure gradually phases out of time with itself, tape-loop minimalism, but keep the sax tone warm and human, never electronic, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~601 chars)*

**Tuning:** If it swings, it's wrong. Add `no swing feel, strictly rubato` before touching anything else.

### Vivian "Viv" Weaver — Anansi

*The only person in the City who never hums — so her theme never states a melody. Everything is accompaniment answering a lead line that is never played.*

```
Exotica, lounge orchestra. Lush strings, vibraphone, harp glissandi and nylon guitar arranged as pure accompaniment; the piece never states a melody, every instrument answers a lead that never arrives. Elegant, weightless, patient. 72 BPM, F-sharp minor, 4/4, glossy television-studio sheen. + the strings repeat one interlocking three-bar figure that never resolves, minimalist phasing, but keep the surface luxurious and inviting, never eerie on top, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~552 chars)*

**Tuning:** Suno badly wants to supply a melody. If it does, add `no lead instrument, no solo, no melodic statement` and pull six takes instead of four.

### Sterling Maas — Midas

*The model, the tour, the ribbon. A mid-century industrial-film score selling the future.*

```
Cinematic, orchestral. Wide brass fanfare over a striding string section, all glass and daylight; French horn carries the main theme, glockenspiel gilds the top. Proud, monumental, sincerely blind. 96 BPM, E-flat major, 4/4, dense production, big scoring-stage room. + in the last eight bars the low strings hold one unresolved dissonance underneath the fanfare while the brass plays on, unaware, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~496 chars)*

**Tuning:** The dissonance is the whole point and the first thing Suno drops. If four takes all resolve cleanly, generate the fanfare alone and add the sour ending as an Extend.

### Geraldine "Gerry" Fitch — the second hand

*Liaison scenes. Aspiration played one notch above her salary, exactly like the suits.*

```
Bossa Nova, cocktail jazz. Nylon guitar sway, brushed snare, vibraphone, and a flute line that keeps reaching for the melody and being answered by the guitar instead. Poised, aspirational, one notch too polished for the room. 108 BPM, B-flat major, 4/4, clean supper-club mix. + a desk clock ticks slightly ahead of the beat throughout and never resolves into the groove, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~471 chars)*

**Tuning:** The clock is fragile. If it vanishes, promote it into the instrument list as `ticking desk clock as percussion`.

### Mickey Shale — the Judas

*The bar, the letter, the pocket. A good tune played badly by someone who could still play it well.*

```
Cool Jazz, ballad. Solo upright piano, slightly out of tune, with a muted trumpet entering late, playing beautifully for four bars, then losing interest; a stand-up bass walks alone through the rest. Wasted talent, three in the morning, a man performing at his own wake. 66 BPM, E-flat major, rubato, very sparse. + leave one flubbed note in, no cleanup, no second take polish, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~477 chars)*

**Tuning:** Suno will not play badly on request. If every take is pretty, lower Style Influence to 70% and raise Weirdness to 55% — the sloppiness has to come from the model, not the words.

### Walt Herzog — city editor

*The copy desk, the relay, the arithmetic he did once at three in the morning and put away.*

```
Cool Jazz, minimalist. A muted trumpet plays one careful phrase and stops; upright piano answers with a single chord and waits; the percussion is a copy-desk pencil, a spike, and a telephone lifted before the second ring. Careful, complicit, precise. 74 BPM, E minor, 4/4, dry newsroom acoustic. + the phrase restarts four times and never gets past its fourth bar, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```

**Tuning:** If it develops into a full head, add `no development and no resolution`. Two takes is enough; this one is short by design.

### Sgt. Roy Pruitt — the Cordon

*The envelope and the corner call box. Small, sweaty, uniformed.*

```
Military march, jazz. A single cheap snare drum plays a parade cadence slightly too fast; a lone piccolo attempts the melody; a baritone saxophone undercuts it with two sour notes per bar. Petty, nervous, correct in every visible way. 116 BPM, B-flat major, 2/4. + the cadence tightens and rushes when the baritone enters, no full band, no glory, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~446 chars)*

**Tuning:** If it comes back stately, cut `military march` to `snare cadence` and let the baritone lead the genre.

---

## Tier A — the suspects

### Sal "Big Bad" Lupo — the Wolf at the Door

*The crew, the yard, the screaming match at the Authority. Obsolete and loud about it.*

```
Garage Rock, big band. Fuzz-toned baritone electric guitar plays the hook, answered by a full brass section stabbing on the offbeat; floor tom and crash carry it with no cymbal restraint anywhere. Thuggish, loud, obsolete and furious. 124 BPM, E minor, 4/4, hot overloaded mix. + 1962 surf-guitar tremolo picking over swing-band brass, the two never quite locking, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~464 chars)*

**Tuning:** The not-locking is the joke. If it tightens up, add `the rhythm section and the brass disagree by a hair`.

### Raymond "Ray" Sato — the Watcher

*The furnished room, the wall of photographs, the darkroom. Obsession without malice.*

```
Minimalist, chamber strings. A single viola ostinato repeats without variation for the whole piece; a muted piano adds one note per bar; a darkroom timer and shutter clicks keep time. Obsessive, contained, righteous. 90 BPM, F-sharp minor, 4/4, dry close mix. + a koto plays four notes near the end and stops, unaccompanied, with no other ornament, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~448 chars)*

**Tuning:** The koto is one gesture, not a texture. If it becomes the arrangement, move the clause to the very end and add `only once`.

### Nathaniel Pell — the Adjuster

*Eleven claim files. The waltz repeats eleven times and loses an instrument each pass.*

```
Ballad, soul jazz. Wurlitzer electric piano and warm vibraphone carry a gentle doorstep waltz; upright bass and brushes barely move; a muted trumpet plays one descending phrase and withdraws. Kind, respectable, guilty. 76 BPM, B-flat major, 3/4. + the waltz repeats identically eleven times, one instrument dropping out each pass, ending nearly silent, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~452 chars)*

**Tuning:** Suno will not count to eleven. If the structure matters, generate the full arrangement and thin it in an edit — or accept `gradually stripping away` as the honest version.

### Councilwoman Maeve Brogan — the Widow's Seat

*The club, the committee, the wake. A sincere air over an insincere trio.*

```
Celtic, lounge jazz. Tin whistle plays a mourning air over a smoky trio — brushed drums, upright bass, and a piano that keeps turning the air into a slow waltz. Elegant, funereal, transactional. 84 BPM, D minor, 3/4, back-room club mix. + the whistle is sincere and the trio beneath it is not, the two arrangements slightly disagreeing throughout, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~447 chars)*

**Tuning:** If the trio wins and the whistle disappears, name the whistle first and demote `lounge jazz` to the mood layer.

### Greta Milner — Spindle & Milner Credit

*The ledgers. Rumpelstiltskin as a spinning wheel: exact, legal, and impossible to argue with.*

```
Baroque, jazz. Harpsichord plays tight interlocking counterpoint, wound like a spinning wheel; pizzicato cello marks time; a walking upright bass joins from the jazz side and matches it perfectly. Precise, legal, unblinking. 98 BPM, D minor, 4/4. + a two-voice Baroque invention over a noir walking bass, but no swing feel and no rubato, everything metronomically exact, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~470 chars)*

**Tuning:** The tension is Baroque rigidity vs. bass swing. If it collapses into one, keep the harpsichord and re-add the bass as an Add Instrumental pass.

### Preston Day — the Voice of the City

*Apollo's sign-on. Magnificent, twenty years old, and ending on a three-inch speaker.*

```
Orchestral, easy listening. A golden-age radio sign-on theme — massed strings rising, French horn fanfare, celeste sparkle, sunrise in every bar. Vain, warm, magnificent, two decades out of date. 100 BPM, C major, 4/4, lush broadcast-studio mix, dense production. + the final chord is played on a small thin AM radio speaker instead of by the orchestra, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~453 chars)*

**Tuning:** The speaker collapse is the character. If Suno ends full and lush, do it as an Extend with `heavily band-limited AM radio, tinny, mono` and cut in the last four seconds.

---

## Tier A — the next one

### Toby Small — Ratatoskr

*Runner scenes — and the tell. The whistle quotes Bunting's figure while the band ignores it.*

```
Latin Boogaloo, bebop. Timbales and cowbell drive it, piano montuno underneath, a bright muted trumpet trading eight-bar phrases with a kid's tin whistle. Quick, cocky, all elbows and errands. 132 BPM, G minor, 4/4, room-mic energy. + the whistle keeps quoting a slow four-note descending figure that does not belong to this song, and the band ignores it, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~455 chars)*

**Tuning:** Boogaloo is four years early on purpose. If you want it period-legal, swap to `Mambo` — same energy, correct year.

---

## The danger board

### Herminia Vega — the next name

*The apartment, the coffee, the drawer with three letters in it. The only cue in the set that isn't about the case.*

```
Bolero, acoustic. A single Puerto Rican cuatro carries a slow unhurried melody; a nylon guitar answers in thirds; a soft guiro keeps time and stops before the piece does. Domestic, unafraid, entirely ordinary. 64 BPM, A minor, 4/4, small kitchen-room recording. + no orchestration and no drama of any kind, and the piece simply stops mid-phrase rather than ending, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```

**Tuning:** If it swells or turns romantic, cut `nylon guitar` and let the cuatro play alone — one instrument in a kitchen is the entire idea. The mid-phrase stop is the cue; if four takes all resolve, trim the audio manually rather than fighting the prompt.

---

## Tier B — the working surface

### Hal Rimm — Heimdall

*The Exchange, the tape racks, the window. Vigilance as texture rather than tension.*

```
Musique concrete, ambient. Reel-to-reel tape hiss and machine hum as the bed; one sustained Hammond organ drone; sparse plucked upright bass notes set far apart; the rhythm is relay clicks and a wire recorder starting and stopping. Vigilant, sleepless, waiting. 52 BPM, drone on B, free time, extremely sparse. + one distant unaccompanied trumpet note near the end, held too long, a horn that never quite sounds, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~512 chars)*

**Tuning:** If it fills in, cut `Hammond organ drone` to `single sustained low organ note` — the word drone invites pads.

### Dez Okafor — the Griot

*The barbershop. The trio is the shop; the talking drum is the recitation nobody outside gets to hear.*

```
Soul Jazz, organ trio. Hammond B-3, hollow-body electric guitar comping, brushed drums, and beneath them a West African talking drum holding a conversation the trio never acknowledges. Warm, proud, guarded. 92 BPM, F major, 4/4, medium swing, small-room mix. + the guitar and organ trade a call-and-response phrase that repeats like a recited list, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~448 chars)*

**Tuning:** If the talking drum gets averaged into the kit, name it first in the instrument list and demote the Hammond.

### August Klein — the Golem

*The pressroom. Machinery is the drum kit; the cello is the word in his pocket.*

```
Industrial, orchestral. Letterpress machinery is the entire percussion section — platen, cylinder, hand-set type dropped into a stick; low brass and contrabass move beneath in slow whole notes; a solo cello states the theme as a wordless cantorial line. Immense, patient, protective. 60 BPM, D minor, 4/4, half-time feel. + the cello phrase is a synagogue melody, but no liturgical choir and no vocals of any kind, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~514 chars)*

**Tuning:** If the press sounds like a drum machine, add `irregular mechanical percussion, not on a grid`.

### "Queen" Ottilie Mauser — the Mouse Queen

*Court under the on-ramp. Ceremonial, not comic — the tin is a crown, played straight.*

```
Cabaret, brass band. Junkyard percussion — struck tin cans, brake drums, oil-barrel bass — under a battered trombone and clarinet playing a slow processional march. Regal, defiant, warm at the center. 88 BPM, C minor, 4/4, raw outdoor recording. + Weimar cabaret harmony played on scrap, but keep the arrangement proud and ceremonial, never ramshackle or comic, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~461 chars)*

**Tuning:** `never ramshackle` is load-bearing. Drop it and you get novelty percussion.

### Dr. Ruth Halloran — Medical Examiner

*The van, the slab, the inquest clock. Precision with no comfort in it.*

```
Cool Jazz, minimalist. Vibraphone states a precise repeating figure; upright bass answers in exact intervals; a metronome and a ventilation hum sit in the mix as instruments. Clinical, unsentimental, exact. 76 BPM, A minor, 4/4, cold tiled-room reverb, sparse. + no drum kit at all and no expressive rubato, everything strictly on the grid, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~440 chars)*

**Tuning:** If it warms up, cut the vibraphone to `marimba, dry` — vibes carry vibrato and vibrato reads as feeling.

### Mabel Cho — the Exchange

*The switchboard. Forty conversations an hour, one person she ever repeated them to.*

```
Ambient, cool jazz. Switchboard tones — clean sine tones and ringback pulses — arranged as the melody, with a single clean-tone electric guitar answering them and a soft brushed cymbal keeping time. Careful, invisible, quietly brave. 80 BPM, A minor, 4/4, small close mix. + forty distant conversations mixed almost below audibility, no intelligible speech, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~457 chars)*

**Tuning:** If murmuring voices come through as vocals, cut that last clause entirely and add crowd noise in post.

### Elmore "Cutty" Sloan — the Witness

*Across the canal. One man, outdoors, telling the truth to nobody.*

```
Delta Blues, acoustic. Bottleneck slide on a resonator guitar is the lead voice, cross-harp harmonica answering, a foot stomp on planking for time, water lapping beneath it all. Weathered, dignified, unheard. 72 BPM, E, laid-back shuffle, single-microphone recording. + no band and no drum kit, one man playing outdoors, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~420 chars)*

**Tuning:** If it gets produced, add `1930s field recording fidelity` — the only place in the set where you should break the 1962 spine.

### Solly Grosz — Three Balls Loans

*The pawnshop. Everything for sale, including memory.*

```
Klezmer, jazz. Clarinet leads in a minor mode with lazy swing behind it; tenor banjo and upright bass keep a shuffling two-feel; a shelf of mismatched clocks ticks in the background. Shrewd, neutral, endlessly patient. 100 BPM, D harmonic minor, 4/4. + the clarinet bargains with itself, phrase and counter-phrase, and never lands on the tonic, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~444 chars)*

**Tuning:** If it turns celebratory, drop the tempo to 84 — klezmer at speed reads as a wedding.

### Det. Frank Casale — Homicide

*The stock detective theme, played well and on purpose. Its ordinariness is the characterization.*

```
Noir Jazz, hard bop. Walking upright bass, brushed snare, a tired tenor saxophone playing the most standard phrase in the book, piano comping behind it. Rumpled, competent, twenty-two years to the pension. 104 BPM, F minor, 4/4, medium swing. + this is deliberately the stock detective theme, played well and without a single surprise, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~435 chars)*

**Tuning:** This one is the control sample. If Casale comes back interesting, your Style Influence is too low across the whole set.

### Ida Maas — the Daughter

*Her father's fanfare, stripped of ceremony. Use it in any scene where Maas is discussed and absent.*

```
Chamber Jazz, ballad. Solo piano plays a brass fanfare slowly and in a minor key, one note at a time; a cello enters underneath halfway through; nothing else ever joins. Restrained, exhausted, two years of an unsent letter. 58 BPM, C minor, rubato, extremely sparse. + it is recognizably the same theme as a civic fanfare, with all ceremony removed, and no brass at all, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~470 chars)*

**Tuning:** For a real quotation rather than a family resemblance, generate Maas first, then run this as a Cover of his track at 60% Audio Influence.

### Rev. Eli Prosper — the Mission

*The pulpit and the checks. A hymn that keeps failing to finish.*

```
Gospel, ballad. Church Hammond organ and a wheezing pump harmonium play a hymn together, slightly out of tune with each other; a tambourine enters and stops; upright bass hesitates on the downbeats. Devout, ashamed, sweating. 68 BPM, G major turning to G minor, 6/8. + the hymn breaks down and restarts twice, but no choir and no congregation, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~443 chars)*

**Tuning:** The major-to-minor turn is the cue. If takes pick one key and stay, split it: generate the major hymn, then Extend into the minor collapse.

---

## The Agency

### Odessa Cole — Operations

*Briefings. Worst bleeding first, feelings later.*

```
Hard Bop, jazz. Drum kit forward — crisp ride and snare in conversation — with tenor saxophone stating a brisk unsentimental head and piano stabbing chords behind it. Triage, competence, no time for you. 132 BPM, C minor, 4/4, tight fast swing. + the head is stated once cleanly and never repeated, no solos and no ornament, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~424 chars)*

**Tuning:** If takes wander into a solo section, add `under ninety seconds, no development` — hard bop's default shape is long.

### Esther Blum — Counsel

*Warrants and their absence. Fast, dry, three moves ahead.*

```
Chamber Jazz, bebop. Clarinet and pizzicato violin trade quick precise phrases; upright bass walks a straight line beneath them; brushes only. Sharp, dry, several moves ahead of the room. 118 BPM, G minor, 4/4, close intimate mix, sparse. + every phrase ends a beat earlier than expected, leaving a small silence, and there are no drum fills, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~442 chars)*

**Tuning:** If the clarinet turns klezmer (it shares vocabulary with Grosz), add `bebop phrasing, no minor-mode ornament`.

### George Oyama — Records

*The archive. Paper as percussion, and nothing beneath it.*

```
Minimalist, cool jazz. Prepared piano with muted papery strings plays a repeating figure; solo vibraphone answers; the percussion is card-file drawers and a rubber stamp in strict time. Cold, thorough, unforgetting. 70 BPM, E minor, 4/4, very sparse, dry archive-room acoustic. + no bass instrument at all and no swing, everything filed exactly on the beat, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~457 chars)*

**Tuning:** The missing bass is what makes it sound like a room with no comfort in it. Don't add one back to fix `thin`.

---

## Tier C

### The precinct bed (shared)

*One cue for all of Tier C. Individual themes for bit players cost generations and buy nothing; vary this one instead.*

```
Noir Jazz, ambient. Walking upright bass and brushed snare loop beneath a room of typewriters, ringing telephones, and a radiator; a tenor saxophone offers only occasional two-note comments. Procedural, indifferent, ordinary. 96 BPM, A minor, 4/4, medium swing, mid-distance room mix. + this is background rather than a theme, and nothing in it should ask to be listened to, mono-leaning tape, warm room reverb, light vinyl noise, 1962 recording, no vocals, no modern polish
```
*(~474 chars)*

**Tuning:** Per-name variants, one axis each: Boyd `+ a young tenor sax phrase that tries to finish and gets cut off`; Kowalczyk `+ drop the sax entirely`; Brack `+ raise the telephones over the band`; Feeny `+ add switchboard tones` (this ties her to Mabel Cho, deliberately); Dubcek `+ replace the radiator with harbor water and a distant bell`. Feeny and Dubcek have moved up to Tier B but still work off this bed rather than taking standalone cues; add Herzog as `+ replace the typewriters with a single copy desk and a telephone answered before the second ring` if you want a newsroom variant of the same texture.

---

## Theme Workshop Notes

- **Log three things per track** as you generate: the Style field verbatim, the take number you kept, and whatever you had to change. The third is the one everyone skips and the one that saves the most time on the next batch.
- **Unexpected-cue inventory** — the deliberate anachronisms and outside-genre intrusions, so you can dial the whole set toward or away from strangeness: Bunting (tape-loop phasing), Toby (boogaloo, four years early), Klein (cantorial cello over industrial percussion), Okafor (talking drum), Ottilie (Weimar cabaret on scrap), Sato (koto), Milner (Baroque counterpoint), Lupo (surf guitar vs. swing brass), Cutty (1930s field-recording fidelity — the one intentional break in the spine), Day (AM-speaker collapse).
- **Diegetic vs. score.** Bunting's tune, Cutty's playing, and Okafor's shop radio can exist inside the fiction; everything else is score. Keep that line clear at the table or the players will start listening for clues in the underscore.
- **Batch order:** Bunting first (everything references it), then the Tier A board, then decoys, then the working ring. Tier C's shared bed can wait until the rest of the set has settled its texture.
- **Two cues added in draft-2:** Herminia Vega (the only domestic cue in the set — generate it late, after the rest of the score has established how grim the baseline is, so the contrast lands) and Walt Herzog (short, unresolved, cheap to generate).
