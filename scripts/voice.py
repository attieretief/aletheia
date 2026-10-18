#!/usr/bin/env python3
"""Generate spoken audio for Aletheia pages with ElevenLabs.

    python3 scripts/voice.py vrae            # every Goeie Vrae answer, AF + EN
    python3 scripts/voice.py vrae/galileo.md  # one page
    python3 scripts/voice.py vrae --dry-run   # print the spoken text, no API calls
    python3 scripts/voice.py vrae --lang=af   # one language only

Writes assets/audio/<course>/<slug>.<af|en>.mp3. The site's player finds them by path.
Skips a file whose spoken text has not changed (hashes in assets/audio/manifest.json).

The API key is never stored in the repo. It comes from $ELEVENLABS_API_KEY, or from the
macOS Keychain item service "elevenlabs", account "attie" (shared with hub/voice).
Voices and models per language are set in VOICES below (overridable with
$ELEVENLABS_VOICE_ID_AF/_EN and $ELEVENLABS_MODEL_AF/_EN).
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AUDIO = ROOT / "assets" / "audio"
MANIFEST = AUDIO / "manifest.json"
# Per language: (voice, model, send language_code?). Chosen by Attie 2026-10-18 by ear:
# his Afrikaans clone on v3 *without* a language hint keeps his accent; the hint flattens it.
VOICES = {
    "af": (os.environ.get("ELEVENLABS_VOICE_ID_AF", "DSwyBx6e1OLYAa1efPJC"),
           os.environ.get("ELEVENLABS_MODEL_AF", "eleven_v3"), False),
    # English: the Hub voice, picked by Attie 2026-10-18 after his own clones came out too British.
    "en": (os.environ.get("ELEVENLABS_VOICE_ID_EN", "G17SuINrv2H9FC6nvetn"),
           os.environ.get("ELEVENLABS_MODEL_EN", "eleven_multilingual_v2"), False),
}
FORMAT = "mp3_44100_64"
FORMAT_BY_LANG = {"en": "mp3_44100_128"}   # 64 kbps sounded tinny in English
STOP_HEADINGS = ("Gaan dieper", "Go deeper", "Bibliografie", "Bibliography",
                 "Aanbevole Leeswerk", "Recommended Reading")


def api_key():
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        return key
    try:
        return subprocess.check_output(
            ["security", "find-generic-password", "-s", "elevenlabs", "-a", "attie", "-w"],
            text=True, stderr=subprocess.DEVNULL).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.exit("No ElevenLabs key: set $ELEVENLABS_API_KEY or add Keychain item service 'elevenlabs', account 'attie'.")


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = {}
    for line in (m.group(1) if m else "").splitlines():
        k, _, v = line.partition(":")
        if v.strip():
            meta[k.strip()] = v.strip().strip('"')
    return meta, text[m.end():] if m else text


def lang_block(body, lang):
    m = re.search(rf'<div class="lang-{lang}"[^>]*>(.*?)\n</div>', body, re.S)
    return m.group(1) if m else ""


def to_speech(md, question):
    out = []
    for line in md.splitlines():
        h = re.match(r"#+\s*(.*)", line)
        if h and h.group(1).strip().startswith(STOP_HEADINGS):
            break
        line = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", line)        # links -> text
        line = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", line)    # emphasis
        line = re.sub(r"^\s*(>|#+|[-*]\s)\s*", "", line)            # quote/heading/bullet marks
        line = re.sub(r"<[^>]+>|\{\{.*?\}\}|\{%.*?%\}", "", line)
        line = line.replace("'n ", "’n ").strip()
        if line:
            out.append(line if line[-1] in ".?!:”\"…" else line + ".")
    question = question.replace("'n ", "’n ")
    return "\n\n".join(([question] if question else []) + out)


def speak(text, lang, dest, key):
    voice, model, hint = VOICES[lang]
    payload = {"text": text, "model_id": model}
    if hint:
        payload["language_code"] = lang
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format={FORMAT_BY_LANG.get(lang, FORMAT)}",
        data=json.dumps(payload).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json", "Accept": "audio/mpeg"})
    with urllib.request.urlopen(req, timeout=600) as r:
        dest.write_bytes(r.read())


def pages(args):
    for a in args:
        p = ROOT / a
        yield from sorted(p.glob("*.md")) if p.is_dir() else [p]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    rebuild = "--rebuild-manifest" in sys.argv   # trust existing files, record their hashes
    langs = [a.split("=", 1)[1] for a in sys.argv if a.startswith("--lang=")] or ["af", "en"]
    if not args:
        sys.exit(__doc__)
    manifest = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    key = None
    for page in pages(args):
        meta, body = front_matter(page.read_text())
        course = meta.get("course")
        if not course:
            continue
        for lang in langs:
            q = meta.get("vraag" if lang == "af" else "vraag_en", "")
            text = to_speech(lang_block(body, lang), q)
            if not text:
                continue
            rel = f"{course}/{page.stem}.{lang}.mp3"
            digest = hashlib.sha256(("|".join(map(str, VOICES[lang])) + text).encode()).hexdigest()[:16]
            if dry:
                print(f"\n===== {rel} ({len(text)} chars)\n{text}")
                continue
            dest = AUDIO / rel
            if rebuild:
                if dest.exists():
                    manifest[rel] = digest
                continue
            if dest.exists() and manifest.get(rel) == digest:
                print(f"skip  {rel}")
                continue
            key = key or api_key()
            dest.parent.mkdir(parents=True, exist_ok=True)
            speak(text, lang, dest, key)
            if MANIFEST.exists():   # another run may have written meanwhile
                manifest = {**json.loads(MANIFEST.read_text()), **manifest}
            manifest[rel] = digest
            MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True))
            print(f"wrote {rel} ({dest.stat().st_size // 1024} KB)")


    if rebuild:
        MANIFEST.write_text(json.dumps(manifest, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
