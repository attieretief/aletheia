# Prologue "Wat is Waarheid?" — Phase 1 research brief

Status: Phase 1 complete, 2026-10-16. **Stop point: shape review with Attie (§5).**
Spec: `~/Downloads/aletheia-prologue-spec.md`. Lives in `_werk/` so Jekyll never builds it.

Verification marks: ✅ verified online this session · ⚠️ verify against print · ❓ not verified, do not use until checked.

---

## 1. Coherence check (read this first)

Checked against Reeks 1–2, `ROADMAP.md`, *Reasonable Wonder* (cosmic-wonder `Book/`) and Paper 1
(`Papers/1-conditional-consonance/`). Ranked by how much each one matters.

1. **The prologue collides with Reeks 5.** ROADMAP.md:52-56 already plans "Waarheid & Kennis":
   *"Kan ons enigiets met sekerheid weet? Wie se waarheid is 'die' waarheid?"*, drukpunt relativism
   and pluralism. The spec's core questions 3 and 4 are Reeks 5's syllabus. A prologue that does
   them fully hollows out Reeks 5 and breaks the "each series answers the question the previous
   one leaves open" rule (ROADMAP.md:11).
   **Proposal:** the prologue establishes *that* truth is real, personal and knowable-but-humbly;
   Reeks 5 does *how* we know (warrant, testimony, pluralism, the full method debate). The
   prologue ends each hard question with a forward pointer to Reeks 5 rather than a full answer.
   Update ROADMAP.md Reeks 5 to say so once the shape is agreed.

2. **Aletheia already contradicts itself on apologetic method, and Geisler sharpens it.**
   - Reeks 2 sessie1.md:380: *"Die bewyse is oorweldigend."*
   - Reeks 2 sessie7.md:444-460 endorses Van Til and says *"Bavinck, Calvyn, en Van Til sê in
     wese dieselfde ding"*. That is wrong as stated: Van Til rejected Thomistic natural theology and
     common-ground proofs, which Reeks 1 uses throughout.
   - *Reasonable Wonder* takes a third, clearer line: Aquinas's contingency argument is sound
     but "runs through premises that careful people deny" (Ch 22:187); theistic arguments are
     "pointer, not proof" (Ch 21); Parts 2–4 are McGrath-style "seeing from inside the faith"
     (Ch 12:31); the cumulative case was explicitly dropped (Ch 23:53).
   - Van Til, Geisler, Schaeffer and Reformed epistemology appear **nowhere** in the book or papers.
   **Proposal:** the prologue adopts the *Reasonable Wonder* stance (realist about truth, humble
   about our grip, arguments as pointers) and names the method disagreement openly, as spec §6a
   asks. Then fix sessie7.md:444-460 in Reeks 2 so the site stops saying the three agree. This is
   the prologue's first public epistemology stance and will bind the book and papers later, so
   it is your call, not mine.

3. **Geisler & Turek is an ID book after chapter 3.** Their cosmological/teleological chapters
   lean on design inference and irreducible complexity, which Aletheia's AGENTS.md forbids.
   ❓ (chapter contents from memory of the book; confirm when you have a copy.)
   Use chapter 1 only, for its definition of truth and the self-defeat test. Never put the book in
   an *Aanbevole Leeswerk* list without that warning.

4. **Self-refutation of relativism is already done in Reeks 2** (sessie7.md:233-239; moral
   relativism in Reeks 1 sessie6.md:60-70). The prologue should become its home and Reeks 2
   cross-link back (Phase 4). Tone: *Reasonable Wonder* hedges its one self-refutation argument
   (against eliminativism, Ch 21:182). Match that: self-defeat kills **global** relativism
   ("there is no truth"), not the modest truth in perspectivism ("where you stand shapes what you
   see"), which the prologue should grant.

5. **Science and models: Reeks 2 is softer than the book.** Reeks 2 sessie1.md:100-118 concedes
   "geen 'God's-eye view' in die wetenskap nie" and Polanyi's "objectivity is 'n mite". *Reasonable
   Wonder* is an explicit realist (Ch 8:78: realism is "a philosophical commitment the book brings
   to the physics"), separates models from reality (Ch 21:81) and uses correspondence language
   ("a determinate truth-maker", P1:53).
   **The bridge:** archetypal/ectypal knowledge. There *is* a God's-eye view, and it is God's;
   ours is ectypal, real and partial. That reconciles Reeks 2's humility with the book's realism
   in one move and is the strongest original contribution the prologue can make.

6. **Heidegger and the site's own name.** Heidegger's *a-lētheia* ("un-concealment") etymology is
   contested, and Heidegger himself later conceded that the natural Greek concept of truth did not
   mean unconcealment ("The End of Philosophy and the Task of Thinking", 1964) ✅ (secondary;
   ⚠️ verify wording). Do not build the prologue on the etymology. Use it as a door, then pivot to
   *emet* and John 14:6 (index.md already anchors the name there).

7. **Common grace is consistent everywhere.** Reeks 2 sessie2.md:289 (Calvin *Inst.* II.2.15),
   sessie8.md:372 (Augustine), Kuyper on science; Paper 1:91-97 uses Bavinck's common grace as its
   source discipline ("neither baptize the source nor refuse the gift"). Echo that phrasing.

8. **Phrases worth echoing from the book:** "awe that survives scrutiny"; "pointer, not proof";
   "do not mistake a method for a metaphysics"; "that the world is readable at all… is not
   something we are owed" (Prologue:41). The last one is a natural line for essay 2.

9. **Spec assumptions that don't match the repo.**
   - *Reading times:* no series has them; no field, include or i18n key exists. Either add a
     `leestyd` front-matter field site-wide or drop it. Default: drop it.
   - *Discussion questions:* Reeks 2 sessions 1, 2, 4 and 7 have none. The prologue will have them.
   - *Length:* sessions run 5–11k words per language. "Smaller" suggests 2.5–4k per essay.
   - Unrelated bugs found in passing: `assets/definitions.js:38,44` hardcode `/aletheia/woordelys.html`
     though `baseurl` is `""` (glossary tooltips likely broken live); Reeks 1 sessions 2–8 have
     front-matter titles that don't match their H1s.

---

## 2. Annotated sources

### Classical
- **Aristotle, *Metaphysics* Γ.7, 1011b26–27** ✅. "To say of what is that it is not, or of what is
  not that it is, is false; to say of what is that it is… is true." The classic correspondence
  intuition in plain words; ideal for an 18-year-old. (Scholars debate whether it is a full
  correspondence theory; don't overclaim.)
- **Plato** — *Theaetetus* (knowledge as more than true belief), *Republic* VII (the cave as
  "coming out of hiding"). ⚠️ cite by Stephanus number once chosen.
- **Augustine, *De doctrina christiana* II.18.28** ✅. "Every good and true Christian should
  understand that wherever truth may be found, it belongs to his Master" (wording varies by
  translation; Latin *Domini sui esse intellegat*). Source of "all truth is God's truth".
  *Confessions* X and *De Magistro* (Christ the inner teacher): ⚠️ locate passages.
- **Aquinas, *ST* I q.16** ✅ (q.16 a.1–2; *De veritate* q.1 a.1). *Veritas est adaequatio rei et
  intellectus*. Aquinas attributes it to Isaac Israeli, but the formula is not in any known text
  of Isaac ✅ (Rocznik Tomistyczny 2015). Say "the medieval formula Aquinas made famous". Key
  move for us: things are true first because they match *God's* mind, then our minds match
  things. That is the theological spine of the prologue.

### Reformed
- **Calvin, *Institutes* I.1–5** (knowledge of God and self, *sensus divinitatis*) and **II.2.15**
  ✅ (already cited in Reeks 2): the Spirit as sole fountain of truth; don't despise truth
  wherever it appears. ⚠️ quote from Battles/McNeill.
- **Junius → Bavinck, archetypal/ectypal** ✅ (Junius, *A Treatise on True Theology*, RHB transl.;
  distinction taken up by Polanus, Turretin, Owen, Bavinck, Kuyper). Bavinck *RD* vol. 1
  Prolegomena: ⚠️ locate exact section. Contribution: humble-but-real knowledge in one image.
- **Kuyper** — two kinds of people, two kinds of science; but common grace makes shared
  knowledge possible. Already in Reeks 2.
- **Van Til** — no neutral ground; the unbeliever knows God and suppresses it (Rom 1). Steelman
  him honestly in the method section. ❓ quote nothing yet.
- **Plantinga, *Warranted Christian Belief*** (OUP 2000) ✅. A/C model: belief in God can be
  properly basic, produced by the *sensus divinitatis*; sin damages it (ch. 7). **Free full text
  on CCEL.** Gives the prologue "knowing without proof-first" in everyday terms (you don't infer
  your mother exists).
- **Frame, *The Doctrine of the Knowledge of God*** (P&R 1987). Triperspectivalism; presuppositional
  but gentler than Van Til. ⚠️ freely available on frame-poythress.org (verify link).
- **Wolterstorff**, *Reason within the Bounds of Religion*; **Dooyeweerd** — background only.
- **SA voice: H.G. Stoker** (Potchefstroom, 1899–1993) ✅. Reformational philosopher, influenced
  and was praised by Van Til; contributed to *Jerusalem and Athens* (1971) ❓ (forum claim only).
  A GKSA/Potchefstroom anchor that fits the audience. Most work is in Afrikaans — worth a look.
- **Confessions:** NGB art. 2–7 (two books; Scripture), HK V.1 (comfort = trust in a faithful
  Person), HK V.21 (true faith as knowledge *and* trust) — the confessional form of *emet*.

### Biblical
- **Hebrew *emet*** ✅ (from *ʾ-m-n*: firm, reliable, faithful; ~127× in OT, often "faithfulness").
  Ex 34:6 *ḥesed we-ʾemet*. Truth as something you can lean your weight on.
- **Greek *alētheia*** — John 1:14 ("full of grace and truth", echoing Ex 34:6), 8:32, 14:6,
  17:17, 18:37–38 (Pilate). Truth as a Person; Pilate asks "what" while standing in front of "who".
  This is the natural hook for essay 1.

### Modern and critical
- **Nietzsche, "On Truth and Lies in a Nonmoral Sense"** (1873, unpublished in his lifetime) ✅.
  "A mobile army of metaphors…" ⚠️ quote from Kaufmann's *Portable Nietzsche*. Steelman: language
  does shape what we can see.
- **Lyotard, *The Postmodern Condition*** (1979) ✅: "incredulity toward metanarratives".
  Steelman: big stories have been used to crush people.
- **Rorty, Foucault** — truth as what our peers let us get away with; truth and power. Grant:
  claims to truth are often power plays. ❓ quotes.
- **Heidegger** — *Being and Time* §44, "On the Essence of Truth"; 1964 concession (see §1.6).
- **Frankfurt, *On Bullshit*** (Princeton UP 2005; essay 1986). The liar cares about truth; the
  bullshitter doesn't. The best single tool for post-truth culture and very readable.
  ⚠️ quote from print.
- **Oxford Word of the Year 2016, "post-truth"** ✅: "circumstances in which objective facts are
  less influential in shaping public opinion than appeals to emotion and personal belief."
- **Theories of truth** (correspondence, coherence, pragmatic, deflationary): use the SEP entry
  "Truth" for checking, explain each with one kitchen example. No quotes needed.

### Flagged by Attie (§5a)
- **Geisler & Turek, ch. 1** ✅ (secondary only). Truth defined as "telling it like it is" is
  *not* their wording; they define it as "that which corresponds to its object" / "describes an
  actual state of affairs". "Road Runner tactic" for turning a self-defeating claim on itself
  (p. 39). Useful for clarity and tone; see §1.3 for the ID warning.
- **Geisler & Bocchino, *Unshakable Foundations*** (Bethany House 2001) ✅ exists; ❓ could not find
  its table of contents. I can't say which chapters handle truth/relativism without a copy.
- **Schaeffer, *The Mark of the Christian*** — your extracts (pp. 13–36). Usable verbatim:
  - "men no longer believe even in the possibility of absolute truth" (p. 25–28 section)
  - John 17:21 as "the final apologetic"
  - "Not his holiness without his love: that is only harshness. Not his love without his
    holiness: that is only compromise." (pp. 35–36)
  - Caution: his "true Christians only" framing and the call to visible oneness across church
    lines will land differently in a GKSA/GKB/APK readership. Use the oneness point; don't import
    his ecclesiology.
- **Schaeffer, "true truth"** (*The God Who Is There*, 1968; *He Is There and He Is Not Silent*,
  1972). Secondary sources confirm the term and its sense (truth about what is really there, not
  religious feeling). ❓ no verified quotation. Also note his history-of-ideas narrative ("line of
  despair") is widely criticised as too neat; borrow the concept, not the history.

---

## 3. Where the richest material is

| Spec question | Richness | Best material | Overlap risk |
|---|---|---|---|
| 1 What is truth? | High | Aristotle, Aquinas (God's mind first), theories in kitchen terms, Heidegger as door | low |
| 2 Biblical vocabulary | **Highest** | *emet* + Ex 34:6 → John 1:14 → 14:6 → Pilate 18:38 | none — unique to prologue |
| 3 Can we know? | High | archetypal/ectypal, analogy, noetic effects of sin, Plantinga | **Reeks 5** |
| 4 Whose truth? | High, topical | post-truth, deepfakes, Frankfurt, steelmanned Nietzsche/Lyotard | **Reeks 5**, Reeks 2 s7 |
| 5 God's truth & ours | Medium | common grace, Augustine/Calvin, two books (NGB 2) | Reeks 2 s2, s8 |
| 6 Science | Medium | ectypal knowledge as the bridge; models vs reality; *RW* realism | Reeks 2 s1 |
| 7 Living the truth | High | *emet* as faithfulness, Schaeffer, Frankfurt, Eph 4:15, HK V.112 (9th commandment) | none |

Q2 and Q7 are the prologue's unique ground. Q3–4 must stay at "that, not how".

---

## 4. Books whose actual text would materially improve this

1. **Bavinck, *Reformed Dogmatics* vol. 1** — to quote the archetypal/ectypal passage, which
   carries question 3 and the science bridge. Highest value.
2. **Schaeffer, *Trilogy*** (one volume, includes *The God Who Is There* and *He Is There…*) — for a
   verified "true truth" quotation.
3. **Frankfurt, *On Bullshit*** — short and cheap; one quote anchors essay 3.
4. **Geisler & Turek** — only if you want to quote ch. 1; otherwise the secondary record suffices.
5. Not needed: Plantinga *WCB* (free on CCEL); Frame *DKG* (free online, verify); *Unshakable
   Foundations* (low marginal value given §1.3).

---

## 5. Three possible shapes

### A. One essay, "Wat is Waarheid?" (~7k words per language)
Hook: Pilate in John 18:38, set beside a viral deepfake. Seven movements following the spec.
- For: one front-door page; matches "smaller".
- Against: too long to read in one sitting, and at this length Q3–4 either swamp the essay or
  get thinned to slogans.

### B. Four essays (~3k each) — **recommended**
1. **Wat is waarheid?** Hook: a courtroom oath, "the truth, the whole truth". Theories of truth
   in kitchen terms; Aquinas's two directions (things match God's mind, our minds match things);
   *emet* → John 1:14 → 14:6 → Pilate asking "what" in front of "who".
2. **Kan ons dit weet?** Hook: the deepfake you shared before you checked. Scepticism steelmanned;
   limits of senses and reason; noetic effects of sin; archetypal/ectypal; analogy; science's
   models as ectypal knowledge ("the world is readable at all… is not owed"). Christians disagree
   on method (Geisler/Van Til/Plantinga) told plainly. Pointer to Reeks 5.
3. **Wie se waarheid?** Hook: "you do you" at a braai. What relativism gets right (power, perspective,
   humility); why global relativism defeats itself (hedged); Frankfurt's bullshit and post-truth;
   AI-generated content; common grace — all truth is God's truth.
4. **Waarheid wat gesien moet word.** Hook: a whistle-blower, or Schaeffer's "they have a right to
   judge us". Truth as faithfulness (*emet* again); holiness and love together; truth spoken in
   love (Eph 4:15); the final apologetic.
- For: each essay hooks, teaches one thing and fits a podcast episode; essays 1 and 4 bracket
  the whole with *emet*. Clean Reeks 5 boundary.
- Against: four pieces before Reeks 1 may feel like a toll gate. Mitigate by making the
  prologue optional-but-recommended in the nav.

### C. Three essays: What / Know / Live
Folds "whose truth" into essay 2. Shortest route, but post-truth and relativism are the most
topical pressure point for 18–35 readers; burying them wastes the best hook.

---

## 6. Decisions (Attie, 2026-10-16)
1. **Shape: B**, four essays of ~3k words per language.
2. **Reeks 5 boundary agreed:** prologue = *that*, Reeks 5 = *how*. ROADMAP.md updated.
3. **Method: the *Reasonable Wonder* line** — realist about truth, humble about our grip,
   arguments as pointers not proofs; name the Geisler / Van Til / Plantinga disagreement plainly.
   Correct Reeks 2 sessie7.md:444-460 (separate edit).
4. **Books: none.** Phase 2 quotes only from verified free text (Aristotle, Augustine, Aquinas,
   Calvin public-domain translations, Plantinga *WCB* on CCEL, the Schaeffer extracts, Scripture,
   confessions, and Hart from the local full texts, §7). Bavinck, Schaeffer's "true truth", Frankfurt and Geisler are paraphrased and
   attributed, never quoted.
5. **Authorship: Attie only.**
6. Brief stays local (not pushed to the public repo).

---

## 7. David Bentley Hart on truth (added 2026-10-16)

Rule carried over from cosmic-wonder `memory/decisions.md`:37: Hart is a **philosophical
interlocutor, not a theological authority**. Attie, 2026-10-16: never put him on a pedestal or let
an essay read as Hart in a Reformed veneer. **Budget: at most one attributed Hart aside per essay;
every load-bearing claim rests on Scripture, the confessions, or the classical/Reformed line
(Augustine, Aquinas, Calvin, Bavinck, Kuyper). Hart never appears in Aanbevole Leeswerk.** Quotes below were checked against the full texts in
`~/Github/attieretief/david-bentley-hart/*.txt` (✅ = read in local text; line numbers refer to those
files) unless marked otherwise. EoG = *The Experience of God* (2013); ATFG = *All Things Are Full of
Gods* (2024); AD = *Atheist Delusions* (2009); TASBS = *That All Shall Be Saved* (2019).

### Usable insights, by essay
| # | Insight | Source | Essay |
|---|---|---|---|
| 1 | Pilate's "What is truth?" is a question about power, "expecting and needing no reply"; truth in his world = who may kill. Nietzsche saw the scene as a clash of worlds. | AD, "The Face of the Faceless", l.1132 ✅ | 1 (hook), 3 |
| 2 | The resurrection "reverses the meaning of this scene entirely" — where truth stood is re-judged. | "Christ and Nothing", *First Things* Oct 2003 (web ✅, ⚠️ print) | 1 (John 14:6 ↔ 18:38) |
| 3 | "The very search for truth is implicitly a search for God (properly defined, that is)." | EoG ch.4, l.4496 ✅ | 1, 2 |
| 4 | The mind can be "a true mirror of objective reality because we assume that objective reality is already a mirror of mind." Correspondence grounded in God: Aquinas q.16 in one sentence. | EoG ch.4, l.4500 ✅ | 1, 2 |
| 5 | "There is no one single discourse of truth as such, no single path to the knowledge of reality"; empirical findings are revisable, unlike logic and mathematics. | EoG ch.2, l.1420 ✅ | 2 (science/models) |
| 6 | One can't believe in facts without "Truth as such": "the very concept of 'fact' is entirely dependent on the mind's prior devotion to such Truth." | EoG ch.5, l.4835 ✅ | 3 (relativism) |
| 7 | Reductionism can't "retreat into postmodern relativism"; disenchantment is "the will to power wrapping itself in the stolen garments of disinterested reason." | ATFG Coda, l.17524, 17604 ✅ | 3 |
| 8 | Postmodernity as "the truth of no truth"; Christianity answers violence with the persuasion of beauty. | *Beauty of the Infinite* (2003), Intro — only via Leithart's outline (❓ no local text) | 3, 4 |
| 9 | Every movement toward truth "is already an act of devotion"; we accept unwelcome truths because truth is an end, not a tool; "the only way to know the truth of things is… the way of bliss." | EoG ch.5, l.4726-4793 ✅ | 4 (truth lived) |

The strongest pair: **#1 + #2** give essay 1 its spine (Pilate asks "what" in front of "who",
and Easter answers), and **#9** gives essay 4 a non-moralistic ground (truth is loved before it
is obeyed), which sits well beside Schaeffer's holiness-and-love line.

### Safe bridge (where Hart, Aquinas and Bavinck agree)
- God is Truth itself; truth is a transcendental, convertible with being (EoG pp.243-51 per index;
  Aquinas *ST* I q.16; Bavinck *RD* 2 on God's truth).
- Analogy rather than univocity: fits archetypal/ectypal.
- A Logos-structured, participatory creation: fits Bavinck's common grace and Paper 1's
  source discipline.
- Self-refutation of reason-denial, framed as a pointer: fits the agreed method line.
- Hart is also an **ally on ID**: "a massive distraction" (EoG l.750-754 ✅).

### Tensions (do not import)
- **Calvinism:** TASBS pp.48-49 calls Calvin's God a "metaphysical absurdity" and the picture a
  "moral horror". A GKSA reader who looks Hart up will find this within minutes. Cite him
  sparingly and say once, plainly, that he is a critic of the Reformed tradition.
- **Universalism:** argued from the same metaphysics of the Good we would borrow for truth.
  Borrow the metaphysics; keep Dort as confession (same move as *Reasonable Wonder* Ch 22:177).
- **Scripture:** EoG l.550-562 dismisses the Bible as "a collection of 'inerrant' oracles". His
  target is flat literalism (Bavinck rejects that too), but never quote it near NGB 5/7.
- **Noetic effects of sin:** Hart has no real doctrine of them, and TASBS says reason "must"
  judge God's goodness. Essay 2 must not lean on Hart; use Calvin, Bavinck, Plantinga there.
- **Register and idiom:** Vedanta and theosis language (sat-chit-ananda, "atman is Brahman",
  ATFG Day Six) and his polemical scorn. Translate into Thomist vocabulary; drop the scorn.

### Reusable in the Hart repo
`graph/nodes/`: the-transcendentals, minds-transcendent-horizon, being-and-knowledge-are-one,
knowledge-as-love, normativity-of-reason, friedrich-nietzsche, naturalism-as-picture-not-truth.
Reformed responses already drafted in `graph/responses/` (incl. the Calvinist-sovereignty one).
`graph/scripts/search.py` gives BM25 search over 2,974 cited passages for Phase 2.

Gaps: *Beauty of the Infinite*, *Tradition and Apocalypse*, *Roland in Moonlight* and *You Are
Gods* are not local. *Beauty of the Infinite* Part 1 is the one that would matter, for essay 3.

---

## 8. Phase 2 log

- **Essay 1 drafted 2026-10-16** → `_werk/proloog/essay1-wat-is-waarheid.md` (AF ~3.2k, EN ~2.9k words).
  Kept in `_werk/` until approved; on approval it moves to `proloog/sessie1.md` with a `proloog.md`
  landing page (`order: 0`).
  - Verified: CPA 51/1977 s162(1) oath wording; Aristotle 1011b26–27; Hart EoG l.4500 and AD l.1132
    (local text); Hart "Christ and Nothing" (web).
  - Own translation: Aristotle (AF and EN paraphrase-level), Hart quotes in AF marked "my vertaling".
  - Glossary candidates: waarheid/aletheia, korrespondensieteorie, koherensieteorie, pragmatisme,
    deflasionisme, emet.
- Essay 1 Hart pass (2026-10-16): mirror quote replaced by John 1:3, 1:9 + Bavinck (⚠️ locate the
  RD 1 Logos passage before publication); resurrection line now in own words; Hart kept once
  (Pilate and power, AD); reading list now Aquinas + Bavinck *Wonderful Works of God*.
- **Essay 2 drafted 2026-10-16** → `_werk/proloog/essay2-kan-ons-dit-weet.md`. AF written first,
  independent proofread applied (~45 edits). 1 Kor 13:12 verified (1983); Rom 1:18 paraphrased,
  ⚠️ unverified against 1983. Hart: none. Kept site title-case headings (proofreader preferred
  sentence case; site convention wins).
- **Reeks 2 sessie7 corrected 2026-10-16:** Van Til was born in the Netherlands, not SA; "Bavinck,
  Calvyn en Van Til sê in wese dieselfde" replaced by "Waar hulle saamstem, en waar nie" (Bavinck:
  proofs as testimonies ⚠️ locate RD 2 passage). Still open: sessie1.md:380 "Die bewyse is
  oorweldigend"; sessie7 ~l.470 quotes Rom 1:18 in 1953 wording.
- **Essay 3 drafted 2026-10-16** → `_werk/proloog/essay3-wie-se-waarheid.md`. AF first; proofread
  applied (~30 edits incl. apartheid wording naming NGK, NHK, GKSA "elkeen op sy eie manier", and
  apartheid's critics as believers and unbelievers). Hart: none. Kept lower-case *sy* for God's
  possessive (1983 convention, consistent with essays 1–2). Augustine/Calvin paraphrased as own
  translation; Oxford definition verified; Frankfurt paraphrased.
- **Essay 4 drafted 2026-10-17** → `_werk/proloog/essay4-waarheid-wat-gesien-word.md`. AF first; two
  proofread passes applied. Bible quotes checked against 1983 (Joh 13:35, 17:21, 1:14; Ef 4:15 now
  "in liefde by die waarheid bly"; Joh 16:13 = the Spirit leads; "die waarheid doen" framed as the
  Greek, 1983 = "volgens die waarheid handel"). HK 1 and 112 quoted from the site's own text.
  Schaeffer quote = own AF translation of Attie's extracts (pp. 35–36). Hart: none.
- **Phase 2 drafts complete.** Remaining: glossary entries, `proloog.md` landing page, move drafts to
  `proloog/`, Phase 3 podcast notes, Phase 4 cross-links.
