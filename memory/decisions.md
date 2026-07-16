# Decisions — durable choices and their rationale

## Positioning & pedagogy
- **Implicit apologetics, never branded as such** — the apologetic function shapes the substance (real objections, philosophical rigour, honest treatment) but never the tone or branding. The tone stays "a congregation studying together," not a fortress under siege.
- **Series organised by live pressure points, not the systematic-theology syllabus** — the traditional order (Theology → Revelation → Anthropology → …) is inward-facing; Aletheia follows the questions real people actually meet in an atheistic world. Each series answers the question the previous one leaves open. Master plan in `ROADMAP.md`.
- **Dual authorship maintained** — Attie Retief (philosophical/systematic) + Douw Kruger (pastoral/practical). The two-voice design is intentional.

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
