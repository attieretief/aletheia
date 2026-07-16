# History — how we got here

A chronological narrative of what has been worked on in Aletheia and its surrounding projects.

## Site foundation (Jekyll)
- Built as a Jekyll site (GitHub Pages, `github-pages` gem) and pointed at the custom domain **aletheia.attieretief.com** (CNAME added; `baseurl`/`url` updated in `_config.yml`).
- SEO and structure hardened: `jekyll-seo-tag`, sitemap, feed, structured data, og:image / social sharing image, page descriptions and `lang`.
- Navigation and responsiveness iterated on: sidebar nav, desktop nav overlap fixes, and a **bilingual (AF/EN) toggle** with full English translations added across content; later fixed the language toggle overlapping the mobile hamburger menu.

## Course content (the Reekse)
- **Reeks 1 — Grondslag** written and completed: 8 sessions on the reality of God (classical theism, metaphysics, consciousness, morality, desire) plus oorsig/slot and a `draaiboek`.
- **Reeks 2 — Wetenskap & Werklikheid** written and completed: 8 sessions on science and faith.
- Confessional/reference material added: Heidelberg Catechism (`kategismus/`), Canons of Dort (`leerreels/`), confessions (`belydenisse/`), glossary (`woordelys/`).
- Major refinement pass (latest commit): "Refine Reeks 1–2, ground material in the classical tradition, tidy bibliographies" — pulling content firmly onto Augustine/Aquinas/Cappadocians/Bavinck and away from single modern sources, and away from any ID/creationist framing.

## Video pipeline
- Session pages moved from self-hosted video to **YouTube embeds** with an end-overlay and a hard-stop enforced at each session's `youtube_end` timestamp.
- A faceless-video generator (`scripts/generate_video.py`, `scripts/README.md`) was built: ElevenLabs audio + SRT → Claude-generated cinematic prompts per paragraph → Replicate Wan clips → stitched MP4. Prompts can be reviewed before spending on generation.

## Voice / TTS exploration (migrated conversations, PRECEDENCE 4)
- Extensive testing of Afrikaans TTS and avatar tools. Chatterbox, Fish Audio, and multilingual/Dutch models all failed Afrikaans pronunciation; Synthesia and HeyGen were unsatisfactory for Afrikaans lip-sync. **ElevenLabs settled on as the only tool that handles Afrikaans properly.**
- A working ElevenLabs API podcast generator (`aletheia_elevenlabs.py`) was built (reads CSV scripts, per-speaker voice IDs, controls inter-speaker gaps, stitches to WAV). A full Chatterbox pipeline was built and tested on an M4 MacBook Pro (48GB) then abandoned.
- HeyGen's browser editor caused severe Mac CPU issues (runaway `HCWebControlService`), reinforcing the move away from talking-head avatar platforms toward audio + AI b-roll. Noted ElevenLabs' own Image & Video beta (Studio 3.0) as a way to keep the whole workflow in one place.
- Dropped from a higher ElevenLabs plan to Creator after CSV analytics showed video generation was ~79% of monthly credit spend.

## Podcast launch & the Crew
- Podcast defined: "Aletheia: Gesprekke oor Geloof, Waarheid en die Werklikheid van God" — two-person Afrikaans format, first episode recorded on iPhone with JDI Mic Mini mics, guest **Douw Kruger**. Advice covered minimal iMovie punch-in editing, a reusable branded intro/outro (piano sting — Attie is a pianist), and distribution across Spotify for Creators (host) → Apple Podcasts / YouTube.
- Built the file-based **`crew/`** production system (role playbooks, `production-board.md`, weekly reports, `produce.py`/`stats.py`) with a weekly heartbeat and two human approval gates.
- Two episode scripts drafted (Afl. 1 from Reeks 1 Sessie 1; Afl. 2 "Ontmasker die strooipop-god"). As of mid-July 2026 both sit at `skrip-konsep` awaiting Attie's approval; nothing published yet.

## Parallel project (context, not in this repo)
- Attie is simultaneously writing a book, *Cosmic Wonder — Superfluid Vacuum Theology* (at `~/Documents/Streams/Cosmic Wonder`), mapping Euler's identity onto the Christian narrative via the superfluid-vacuum hypothesis. Its refined humanisation voice discipline is the standard Aletheia content should move toward.
