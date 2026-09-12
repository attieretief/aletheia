# Aletheia

Aletheia is an Afrikaans Reformed theological education site — a course series (kursusreeks) that weaves faith, philosophy and science together for thinking believers. It is built as a Jekyll site served at **https://aletheia.attieretief.com** via GitHub Pages. Its purpose is to be a very practical guide, with philosophical, metaphysical and theological depth, that equips congregations (GKSA/GKB/APK context) to face the most topical challenges to Christian faith. It functions as apologetics but deliberately never brands or presents itself as such — see "Positioning" below.

## Stack & build

- **Jekyll** (via the `github-pages` gem; `bundle exec jekyll serve` for local dev). Markdown is `kramdown`.
- Site config lives in `_config.yml`. Site language is Afrikaans (`lang: af`); content is bilingual AF/EN.
- Standard Jekyll layout: `_layouts/`, `_includes/`, `_sass/`, `_data/`, `_posts/`, `assets/`. `_site/` is the build output (do not edit).
- Plugins are limited to what GitHub Pages allows (see `_config.yml`): `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`, etc.
- One collection is defined: `courses` (`output: true`, `sort_by: lesson`).

## Content structure

- **Courses/series (reekse)** are the heart of the site. Each series lives in its own directory of session (`sessie1.md` … `sessieN.md`) files plus a `draaiboek.md` (screenplay/production script), with a top-level landing page `.md` (e.g. `reeks01-grondslag.md`, `reeks02-wetenskap.md`).
  - **Reeks 1 — Grondslag** (`reeks01-grondslag/`): 8 sessions on the reality of God — classical theism, metaphysics, consciousness, morality, desire. Complete.
  - **Reeks 2 — Wetenskap & Werklikheid** (`reeks02-wetenskap/`): 8 sessions on science and faith. Complete.
  - Series 3–8 are planned; see `ROADMAP.md`.
- **Confessional texts**: `belydenisse/`, `kategismus/` (Heidelberg Catechism), `leerreels/` (Canons of Dort), `woordelys/` (glossary).
- Session pages use `layout: lesson` with front matter: `course`, `lesson` (ordering), `title`/`title_en`, `description`/`description_en`, `youtubeurl`, `youtube_start`/`youtube_end`, `author`. Video is delivered via YouTube embeds with an end-overlay and a hard-stop enforced at `youtube_end`.
- **Bilingual pattern**: content is written in parallel `<div class="lang-af">` / `<div class="lang-en">` blocks with a site-wide AF/EN toggle; UI strings are in `_data/i18n.yml` keyed `<key>.af` / `<key>.en`.

## The ROADMAP

`ROADMAP.md` (repo root, excluded from the Jekyll build) is the master plan. Always consult it before planning new series content. Key structural principle: series are organised by **live pressure points** (the actual challenges believers meet — at work, university, on social media), NOT by the traditional systematic-theology syllabus. Each series answers the question the previous one leaves open. Progression: Metaphysics → Physical world → Problem of evil → What is man → What can we know → Scripture → Christ → The future.

## Podcast & production ("the Crew")

- **Podcast**: "Aletheia: Gesprekke oor Geloof, Waarheid en die Werklikheid van God" — a two-person Afrikaans podcast (host Attie + guest, first episode with Douw Kruger). Scripts derive from the Reeks sessions. Episode drafts live in `podcast/`.
- **`crew/`** is an internal, unpublished (excluded in `_config.yml`) file-based production system for the podcast: role playbooks (`rol-*.md`), a shared `production-board.md` tracking each episode through its stages, weekly reports (`crew/reports/`), and automation scripts (`crew/scripts/produce.py` for ElevenLabs audio, `stats.py` for GoatCounter + MailerLite). It is not autonomous bots — it is Claude "showing up to work" in each role on a weekly cadence, with two human approval gates (script approved, audio approved). Nothing goes live without Attie's approval at both gates. Keys go in `crew/scripts/config.env` (gitignored; copy from `config.example.env`).
- **`scripts/generate_video.py`**: turns ElevenLabs audio + SRT into a faceless video with AI-generated (Replicate Wan) contextual visuals. See `scripts/README.md`. Audio TTS is ElevenLabs (the only tool that handles Afrikaans well).

## Positioning & voice (important)

- **Implicit apologetics.** The apologetic function shapes the *substance* (rigorous engagement with real objections) but never the branding or tone. The tone is a congregation studying together, not a fortress under siege. Never advertise the site as "apologetics".
- **Dual authorship is intentional**: Attie Retief (philosophical/systematic) and Douw Kruger (pastoral/practical). Maintain both voices.
- **Ground everything in the classical tradition** (Augustine, Aquinas, the Cappadocians, Bavinck, Kuyper, Warfield), not single modern sources.
- **Never use Intelligent Design or creationist framing.** Classical theism and Reformed providence do not lean ID/YEC. God works through natural processes (HC Q27, NGB Art 13), not by filling gaps. Do NOT use the necessity/chance/design trilemma. Frame fine-tuning as deepening the contingency argument, not as evidence for a "Designer". Engage evolution honestly — the enemy is philosophical naturalism, not the science. Treat YEC briefly and respectfully but not as a mainstream Reformed position. `ontwerp` is fine in ordinary use but dangerous where it echoes ID "design detection".
- **Writing craft**: aim for the refined humanisation discipline of Attie's parallel book project (warm, unhurried, precise, honest about uncertainty). Avoid AI tells — no em-dash overuse, no hollow intensifiers, no reflexive tricolons. Read-aloud tested.

## Conventions

- Content language is Afrikaans; keep AF as primary, EN for the wider audience. This CLAUDE.md and `memory/` are in English by convention.
- These are working files in git — nothing is hidden. Do not `git add`/commit unless asked.
