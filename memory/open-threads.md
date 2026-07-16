# Open threads — unresolved work and things to revisit

## Podcast production (blocking, as of mid-July 2026)
- **Episode 1 script awaiting Attie's approval** — `podcast/voorbeeld-reeks01-sessie01-dialoog.md`, at stage `skrip-konsep` since 2026-06-25 (~3 weeks). This is the single gate holding the whole chain (production → publication → first data). Even tweaks unblock it.
- **Episode 2 script awaiting approval** — `podcast/aflewering-02-ontmasker-die-strooipop-god.md`, at `skrip-konsep` since 2026-06-29. Pipeline is intentionally held two-deep; no third script until a gate opens.
- Nothing has been published yet; the "Gepubliseer" board is empty.

## Crew automation not yet wired up
- **`crew/scripts/config.env` does not exist** — so `stats.py` (GoatCounter + MailerLite) cannot run and `produce.py` (ElevenLabs audio) can't go full-auto. Copy `crew/scripts/config.example.env` and fill in the ElevenLabs API key + voice IDs, GoatCounter and MailerLite tokens. Until then weekly analyst reports have no live data.
- Spotify upload stays manual (no API); the analyst pastes any non-API stats by hand.

## Roadmap / content
- **Reeks 3–8 unwritten.** Next up is Reeks 3 — Lyding & Kwaad (problem of evil), placed early because it is the #1 emotional blocker. See `ROADMAP.md` for the full plan and per-series notes (including the "Hart" anti-theodicy hinge to engage in Reeks 3).
- Continue applying the refined *Cosmic Wonder* humanisation discipline to existing Reeks 1–2 content going forward.

## Distribution / platform notes to revisit
- suggested: Decide whether to disconnect the RSS→YouTube pipe and upload video episodes natively to YouTube Studio, to avoid duplicate episodes when a direct video upload coexists with the RSS feed.
- suggested: Apple Podcasts video (iOS 26.4) requires HLS via a supported hosting provider; Spotify for Creators is not currently a supported host — revisit if video-on-Apple becomes a goal.
