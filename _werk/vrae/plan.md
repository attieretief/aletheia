# Goeie Vrae — short-answer layer

Decision (Attie, 2026-10-18): Aletheia was started to support struggling young Christians in a
loud, confused world. The series give depth but run to 5–11k words a session, too long for a young
person on a phone. This layer sits on top: the questions they actually hear, answered short,
engaging and easy, each linking down into the depth. Never branded "apologetics".

Name: **Goeie Vrae / Good Questions**: the question is welcomed, not defended against.
Lives in `_werk/vrae/` until Attie approves; then `vrae.md` (root) + `vrae/*.md`.
Nav: `order: -1`, so it sits first, above the Prologue (cosmetic call).

## Format (every answer)

Follows `hub/guides/content-recipe.md`.

- **Title = the verdict**, plain ("Die wetenskap het God nie oorbodig gemaak nie"). No clickbait.
- `vraag:` the objection in the words young people hear it (lecturer, TikTok, a friend).
- **Kort antwoord**: two sentences, bold, for the reader who reads nothing else.
- **Felt hook** in second person ("jy"). No invented first-person anecdotes.
- **Mechanism**: short paragraphs, one link at a time. Concede what is true first.
- **The click**: the reframe.
- **End small**: one thing you can say or do the next time you hear it.
- **Gaan dieper**: 2–3 links into the sessions.
- 400–550 words per language. One hard specific per answer. Reformed, original thinkers, no
  Hart, no ID. Same AF/EN parallel blocks as the rest of the site.

## The 30 questions (✍️ = sample drafted)

| # | Tema | Vraag soos jy dit hoor | Diepte |
|---|---|---|---|
| 1 | God | "As alles 'n oorsaak het, wie het God gemaak?" ✍️ | R1 S1, S4 |
| 2 | God | "Geloof is 'n kruk vir swak mense." | R1 S6, Proloog 2 |
| 3 | God | "Daar is geen bewys vir God nie." | R1 S4, Proloog 2 |
| 4 | God | "As God bestaan, hoekom wys Hy Homself nie?" | R1 S6–7 |
| 5 | Wetenskap | "Die wetenskap kan alles verklaar. Waarvoor het ons God nog nodig?" ✍️ | R2 S1, S7; R1 S3 |
| 6 | Wetenskap | "Die heelal het uit niks gekom." | R2 S3; R1 S4 |
| 7 | Wetenskap | "Evolusie bewys daar is nie 'n God nie." | R2 S5 |
| 8 | Wetenskap | "Die kerk het Galileo vervolg. Geloof is teen wetenskap." | R2 S2 |
| 9 | Wetenskap | "Jou brein is net chemie. Daar is nie 'n siel nie." | R2 S6; R3 S3 |
| 10 | Wetenskap | "Die multiversum verklaar die fyninstelling." | R2 S4 |
| 11 | Waarheid | "Dis jou waarheid, nie myne nie." | Proloog 3 (kortvideo 1) |
| 12 | Waarheid | "Alle godsdienste sê basies dieselfde." | Proloog 3; R4 |
| 13 | Waarheid | "Jy glo net omdat jy in 'n Christelike huis grootgeword het." | Proloog 2; R4 |
| 14 | Mens | "Ons is maar net slim ape." ✍️ | R3 S1; R2 S5–6 |
| 15 | Mens | "Ek kan goed wees sonder God." | R1 S5; R3 S4 |
| 16 | Mens | "Niemand kan vir my sê wie ek is nie." | R3 S6 |
| 17 | Mens | "Wat is die punt van alles?" | R3 S7 |
| 18 | Lyding | "As God goed is, hoekom kry kinders kanker?" | R5 |
| 19 | Lyding | "Hoe kan 'n goeie God mense hel toe stuur?" | R5; R8 |
| 20 | Bybel | "Die Bybel is vol teenstrydighede." | R6 |
| 21 | Bybel | "Die Bybel is oor eeue verander. Dis 'n telefoonspeletjie." | R6 |
| 22 | Bybel | "Mense het besluit watter boeke in die Bybel kom." | R6 |
| 23 | Bybel | "Die God van die Ou Testament is wreed." | R6; R5 |
| 24 | Jesus | "Jesus het nooit bestaan nie." | R7 |
| 25 | Jesus | "Die opstanding is 'n mite." | R7 |
| 26 | Jesus | "Jesus was net 'n goeie mens." | R7; R1 S8 |
| 27 | Kruis | "Hoekom moes Jesus sterf? 'n Vader wat sy seun laat doodmaak?" | R8 |
| 28 | Kerk | "Die kerk is vol skynheiliges." | Proloog 4 |
| 29 | Kerk | "Godsdiens veroorsaak oorloë." | R9 |
| 30 | Toekoms | "KI sal binnekort alles kan doen wat 'n mens doen." | R9; R3 |

Questions whose series is not written yet (R4–R9) can still get a short answer now. The "Gaan
dieper" line then points to the Reeks 1–3 material that exists, plus "Reeks N (beplan)" in plain text.

## Status

- 2026-10-18: plan, landing page with card grid + theme filter, and samples #1, #5, #14 drafted.
  Needs one layout change at integration: `_layouts/course.html` skips the default lesson list
  for `course_name == "vrae"`, because the landing page draws its own cards.
- Noticed in passing: `_werk/kortvideo/01-road-runner.md` opens on "my neef" at a braai. The content
  recipe forbids invented anecdotes; it needs either Attie's real story or `[AUTHOR: INSERT]`.
