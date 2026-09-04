---
description: End-of-session wrap for Stillwater Rise — danger board, decisions, session file, CURRENT STATE, commit
---

Run the Stillwater Rise end-of-session workflow from CLAUDE.md. Do every step; don't skip one because nothing obvious changed — check and say so.

1. **`docs/Stillwater Rise/06 Campaign/Danger Board.md`** — Review what happened this session. Move at least one entry forward; record any trigger that fired; note if a window closed or a name was saved (saving moves the date, it doesn't erase it).
2. **`docs/Stillwater Rise/06 Campaign/Decisions.md`** — Append a dated section (today's date, ISO) for anything newly locked this session, with the *why*. Newest at the bottom.
3. **`docs/Stillwater Rise/06 Campaign/Sessions/Session NN.md`** — If we planned a session, the plan is written. If we played one, fill in the Recap and set `status: played` and `date:`. Create the next session's file from the same template if the plan for it is already clear.
4. **`docs/Stillwater Rise/06 Campaign/Campaign.md`** — Rewrite the CURRENT STATE block: update the "As of" date, the Locked line, the Open list, and the single Next line. Keep it short; it is the cross-session memory.
5. Show me `git diff --stat`, then commit with a message that says what changed in the fiction, not just which files. Do not push unless I say so.

Reference material stays dry. Don't restate corrections back to me.
