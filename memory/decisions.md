# Decisions — durable choices and their rationale

## Positioning & pedagogy
- **Implicit apologetics, never branded as such** — the apologetic function shapes the substance (real objections, philosophical rigour, honest treatment) but never the tone or branding. The tone stays "a congregation studying together," not a fortress under siege.
- **Series organised by live pressure points, not the systematic-theology syllabus** — the traditional order (Theology → Revelation → Anthropology → …) is inward-facing; Aletheia follows the questions real people actually meet in an atheistic world. Each series answers the question the previous one leaves open. Master plan in `ROADMAP.md`.
- **Attie writes everything (2026-10-18)** — Attie Retief is sole author of all series content, systematic and pastoral; Douw Kruger is a podcast guest only. Supersedes the earlier dual-authorship decision.

## Theology / content
- **Never use Intelligent Design or creationist framing** — ID makes God a competing cause (a demiurge/engineer) and relies on god-of-the-gaps reasoning, which undermines the classical theism Reeks 1 establishes and weakens faith as gaps close. Reformed providence works *through* natural processes (HC Q27, NGB Art 13). Practically: no Behe/Dembski/irreducible-complexity as a Reformed position; no necessity/chance/design trilemma; frame fine-tuning as deepening the contingency argument, not evidence for a "Designer"; engage evolution honestly (enemy = philosophical naturalism, not the science); treat YEC briefly/respectfully but not as mainstream Reformed. `ontwerp` is fine ordinarily, risky where it echoes ID "design detection."
- **Ground content in the classical tradition** (Augustine, Aquinas, the Cappadocians, Bavinck, Kuyper, Warfield), not single modern sources.
- **Writing craft / humanisation discipline** — aim for the refined voice of the *Cosmic Wonder* book: warm, unhurried, precise, honest about uncertainty. Avoid AI tells: no em-dash overuse, no hollow intensifiers, no reflexive tricolons; read-aloud tested.

## Technical
- **Jekyll on GitHub Pages**, served at the custom domain aletheia.attieretief.com. Plugin set limited to what GitHub Pages allows.
- **Bilingual AF/EN** throughout — Afrikaans primary, English for the wider audience; parallel `lang-af`/`lang-en` blocks and `_data/i18n.yml` for UI strings.
- **YouTube embeds for session video** (moved off self-hosted video), with an end-overlay and a hard stop enforced at each session's `youtube_end`.
- **ElevenLabs for all Afrikaans TTS** — decided after Chatterbox, Fish Audio, multilingual/Dutch models, Synthesia and HeyGen all failed Afrikaans pronunciation or lip-sync. Prefer audio + AI-generated b-roll over talking-head avatars.
- **`crew/` production system is deliberately not autonomous** — file-based, in git, human approval required at two gates (script approved, audio approved). Nothing goes live without Attie's sign-off. Pipeline kept intentionally two-deep — no third script is written while a gate is closed.
- **`ROADMAP.md`, `crew/`, `podcast/` and internal drafts are excluded from the Jekyll build** (`_config.yml` `exclude`) — internal, not for publication.

## Prologue "Wat is Waarheid?" (2026-10-16)
- **Four essays (~3k words each), Attie only** — each hooks, teaches one thing and maps to one podcast episode.
- **Prologue does *that*, Reeks 4 does *how*** — avoids hollowing out Reeks 4 (Waarheid & Kennis).
- **Method = the *Reasonable Wonder* line** (realist about truth, arguments as pointers, method disagreement named openly) — the site currently contradicts itself (Reeks 2 s7:444-460 says Bavinck, Calvin, Van Til agree); that passage gets corrected.
- **No print copies bought** — quote only verified free text; paraphrase Bavinck, Schaeffer's "true truth", Frankfurt, Geisler.

## Afrikaans prose (2026-10-16)
- **Write Afrikaans first and natively; never translate the English** — Attie called a translated-feel draft "atrocious". Checklist from the proofread: verb-final in subclauses (incl. the court oath), closing *nie* after quoted questions, no calques ("sin maak", "teen 1907", "in my eie woorde", "die punt is", "X is wanneer…", "mis" for overlook, "boks"), month names lower case (AWS), *Hy/Hom* capitalised for Christ throughout, Bible quotes checked against the 1983 vertaling. Voice model: Attie's own stories in `~/Github/attieretief/writing/Short Stories/Afrikaans/`. Always run an independent taalversorging pass before showing him Afrikaans.
- **Hart is never on a pedestal (Attie, 2026-10-16)** — across aletheia, at most one attributed Hart aside per piece; load-bearing claims rest on Scripture, confessions and the classical/Reformed line; Hart stays out of reading lists. The work must not read as Hart in a Reformed veneer. Cite the original thinker (Origen, Nyssa, Socinus, Dostoevsky…), not Hart's restatement; quote Hart only where he is genuinely original. The position is Reformed, always: never neutral, never "Hart vs. us" as framing.
- **The Prologue precedes every series — refer forward, never back (Attie, 2026-10-16).** No "soos ons in Reeks 1 gesien het"; write "Reeks 1 gaan verder hierop in" / "ons kom in Reeks 2 weer hierby uit".
- **Stay out of party politics and inter-church differences (Attie, 2026-10-16).** No named political episodes (e.g. apartheid) and no naming of denominations against each other; make the point about "the church" or "Christians" generally, or personally. Doctrinal disagreement between *thinkers* (Bavinck/Van Til) is fine; between *churches* is not.
- **Audience widened beyond the congregation (Attie, 2026-10-17).** Aletheia is for anyone willing to think, ask and grow: believers going deeper and seekers wanting honest answers, with 18–35 in mind. The origin story (a congregation's honest wrestling) stays; the "gemeentelede" framing goes. Homepage updated.
- **Order is Mens (3) → Kennis (4) → Lyding & Kwaad (5) → Skrif (6) (Attie, 2026-10-18).** Evil needs the anthropology (fall, bound will) and the limits of knowing (Job 38–42) in place, and lament leads into Scripture. Cost: the #1 emotional objection waits until 5, so earlier series must point ahead to it honestly.
- **Goeie Vrae short-answer layer (2026-10-18)** — Aletheia exists to help struggling young Christians, and the series alone don't reach them: at 5–11k words a session, they are too long to read on a phone. So we add 30 objections in the words young people hear them, each answered in 400–550 words following the content recipe and linking into the series. It must be engaging and easy (Attie). Plan in `_werk/vrae/plan.md`.
