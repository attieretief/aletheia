#!/usr/bin/env python3
"""
Aletheia Video Generator
========================
Takes an SRT file + audio file from ElevenLabs audiobook generation,
auto-generates contextual video prompts per subtitle block using Claude,
generates video clips via Replicate (Wan 2.1), and stitches everything
together into a final video with MoviePy.

Usage:
    python generate_video.py \
        --srt reeks01.srt \
        --audio reeks01.mp3 \
        --output reeks01_video.mp4

Requirements:
    pip install replicate anthropic moviepy srt --break-system-packages

Environment variables:
    REPLICATE_API_TOKEN  - Your Replicate API key
    ANTHROPIC_API_KEY    - Your Anthropic API key (for prompt generation)
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import srt
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install replicate anthropic moviepy srt")
    sys.exit(1)

# Lazy imports — only load when actually needed
replicate = None
anthropic = None
moviepy_loaded = False


def _ensure_replicate():
    global replicate
    if replicate is None:
        import replicate as _replicate
        replicate = _replicate


def _ensure_anthropic():
    global anthropic
    if anthropic is None:
        import anthropic as _anthropic
        anthropic = _anthropic


def _ensure_moviepy():
    global moviepy_loaded, VideoFileClip, AudioFileClip, ImageClip, concatenate_videoclips
    if not moviepy_loaded:
        from moviepy import (
            VideoFileClip as _VFC,
            AudioFileClip as _AFC,
            ImageClip as _IC,
            concatenate_videoclips as _cv,
        )
        VideoFileClip = _VFC
        AudioFileClip = _AFC
        ImageClip = _IC
        concatenate_videoclips = _cv
        moviepy_loaded = True


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Replicate model for text-to-video
VIDEO_MODEL = "wavespeedai/wan-2.1-t2v-480p"

# How many subtitle cues to group into one video clip.
# A single SRT cue is often just a few words — grouping avoids
# generating hundreds of tiny clips. Adjust to taste.
CUES_PER_CLIP = 4

# Resolution (must match Wan output)
VIDEO_WIDTH = 848
VIDEO_HEIGHT = 480

# Scene separator patterns
SCENE_SEPARATOR = re.compile(r"^[\s.…]+$")           # ". . ." style
SESSION_HEADER = re.compile(r"^Sessie\s+\d+\s*:", re.IGNORECASE)  # "Sessie 1:" style


def _update_config(cues_per_clip: int, video_model: str):
    global CUES_PER_CLIP, VIDEO_MODEL
    CUES_PER_CLIP = cues_per_clip
    VIDEO_MODEL = video_model


# ---------------------------------------------------------------------------
# Step 1: Parse SRT into timed paragraphs
# ---------------------------------------------------------------------------

def parse_srt_file(srt_path: str) -> list[dict]:
    """Parse SRT and group cues into clip-sized paragraphs."""
    with open(srt_path, "r", encoding="utf-8") as f:
        cues = list(srt.parse(f.read()))

    paragraphs = []
    current_group = []

    for cue in cues:
        text = cue.content.strip().replace("\n", " ")

        # Check if this cue is a scene separator (". . ." style)
        if SCENE_SEPARATOR.match(text):
            if current_group:
                paragraphs.append(_make_paragraph(current_group))
                current_group = []
            paragraphs.append({
                "start": cue.start.total_seconds(),
                "end": cue.end.total_seconds(),
                "duration": (cue.end - cue.start).total_seconds(),
                "text": "",
                "is_separator": True,
            })
            continue

        # Check if this cue starts a new session ("Sessie X: ...")
        # If so, flush the previous group first to create a natural break
        if SESSION_HEADER.match(text) and current_group:
            paragraphs.append(_make_paragraph(current_group))
            current_group = []

        current_group.append(cue)

        if len(current_group) >= CUES_PER_CLIP:
            paragraphs.append(_make_paragraph(current_group))
            current_group = []

    # Flush remaining
    if current_group:
        paragraphs.append(_make_paragraph(current_group))

    return paragraphs


def _make_paragraph(cues: list) -> dict:
    """Combine a group of cues into one paragraph with timing info."""
    text = " ".join(c.content.strip() for c in cues)
    # Clean up whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return {
        "start": cues[0].start.total_seconds(),
        "end": cues[-1].end.total_seconds(),
        "duration": (cues[-1].end - cues[0].start).total_seconds(),
        "text": text,
        "is_separator": False,
    }


# ---------------------------------------------------------------------------
# Step 2: Generate video prompts using Claude
# ---------------------------------------------------------------------------

def generate_prompts(paragraphs: list[dict], batch_size: int = 10) -> list[str]:
    """Use Claude to generate cinematic video prompts for each paragraph."""
    _ensure_anthropic()
    client = anthropic.Anthropic()
    prompts = []

    # Filter to only non-separator paragraphs
    text_paragraphs = [p for p in paragraphs if not p["is_separator"]]

    print(f"\nGenerating prompts for {len(text_paragraphs)} paragraphs...")

    for i in range(0, len(text_paragraphs), batch_size):
        batch = text_paragraphs[i : i + batch_size]
        numbered = "\n".join(
            f"{j+1}. \"{p['text'][:300]}\"" for j, p in enumerate(batch)
        )

        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": f"""You are generating cinematic video prompts for an AI video model (Wan 2.1).
The source material is an Afrikaans Christian apologetics series called "Aletheia" about the reality of God.

For each numbered paragraph below, write ONE short English video prompt (max 30 words) describing
a cinematic, atmospheric visual that matches the theological/philosophical theme being discussed.

Rules:
- NO text, words, letters or titles in the video
- NO faces or identifiable people
- Cinematic, contemplative, beautiful imagery
- Use nature, architecture, light, space, abstract visuals
- Match the emotional tone (wonder, depth, warmth, mystery)
- Each prompt must be visually distinct from the others

Paragraphs:
{numbered}

Reply with ONLY a JSON array of strings, one prompt per paragraph. No other text.""",
                }
            ],
        )

        # Parse the JSON response
        response_text = response.content[0].text.strip()
        # Handle potential markdown code blocks
        if response_text.startswith("```"):
            response_text = re.sub(r"```(?:json)?\s*", "", response_text)
            response_text = response_text.rstrip("`").strip()

        batch_prompts = json.loads(response_text)
        prompts.extend(batch_prompts)
        print(f"  Generated prompts {i+1}–{i+len(batch)} of {len(text_paragraphs)}")

    return prompts


# ---------------------------------------------------------------------------
# Step 3: Generate video clips via Replicate
# ---------------------------------------------------------------------------

def generate_clips(
    paragraphs: list[dict],
    prompts: list[str],
    output_dir: Path,
) -> list[Path]:
    """Generate a video clip for each paragraph using Replicate Wan 2.1."""
    _ensure_replicate()

    clips_dir = output_dir / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)

    clip_paths = []
    prompt_idx = 0

    for i, para in enumerate(paragraphs):
        clip_path = clips_dir / f"clip_{i:03d}.mp4"

        if para["is_separator"]:
            # Generate a simple black clip for separators
            clip_paths.append(("black", para["duration"], clip_path))
            continue

        if clip_path.exists():
            print(f"  Clip {i:03d} already exists, skipping")
            clip_paths.append(("file", 0, clip_path))
            prompt_idx += 1
            continue

        prompt = prompts[prompt_idx]
        prompt_idx += 1

        print(f"  Generating clip {i:03d}: \"{prompt[:60]}...\"")

        max_retries = 3
        for attempt in range(max_retries):
            try:
                output = replicate.run(
                    VIDEO_MODEL,
                    input={
                        "prompt": prompt,
                    },
                )

                # Output is a FileOutput — read the URL and download
                import urllib.request
                video_url = str(output)
                urllib.request.urlretrieve(video_url, str(clip_path))
                clip_paths.append(("file", 0, clip_path))
                print(f"    Saved to {clip_path}")
                break

            except Exception as e:
                err_str = str(e)
                if ("429" in err_str or "402" in err_str) and attempt < max_retries - 1:
                    wait = 15 * (attempt + 1)
                    print(f"    Rate limited, waiting {wait}s before retry...")
                    time.sleep(wait)
                else:
                    print(f"    ERROR generating clip {i:03d}: {e}")
                    # Fall back to black clip
                    clip_paths.append(("black", para["duration"], clip_path))
                    break

    return clip_paths


# ---------------------------------------------------------------------------
# Step 4: Stitch everything together with MoviePy
# ---------------------------------------------------------------------------

def stitch_video(
    paragraphs: list[dict],
    clip_paths: list[tuple],
    audio_path: str,
    output_path: str,
):
    """Combine all clips with the audio into a final video."""
    _ensure_moviepy()
    print("\nStitching video...")

    audio = AudioFileClip(audio_path)
    video_clips = []

    for i, (clip_type, fallback_duration, clip_path) in enumerate(clip_paths):
        para = paragraphs[i]
        target_duration = para["duration"]

        if clip_type == "black":
            # Create a black frame for separators/failures
            import numpy as np
            black_frame = np.zeros((VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
            clip = ImageClip(black_frame, duration=target_duration).with_fps(24)
        else:
            # Load the generated video clip
            clip = VideoFileClip(str(clip_path))

            # Adjust clip duration to match paragraph timing:
            # If clip is shorter than needed, slow it down
            # If clip is longer than needed, speed it up
            if clip.duration > 0 and abs(clip.duration - target_duration) > 0.1:
                speed_factor = clip.duration / target_duration
                clip = clip.with_speed_scaled(speed_factor)

        video_clips.append(clip)

    # Concatenate all clips
    final_video = concatenate_videoclips(video_clips, method="compose")

    # Set the audio
    final_video = final_video.with_audio(audio)

    # If video is longer than audio, trim. If shorter, the audio will be cut.
    if final_video.duration > audio.duration:
        final_video = final_video.subclipped(0, audio.duration)

    # Write output
    print(f"Writing to {output_path}...")
    final_video.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        fps=24,
        preset="medium",
        bitrate="4000k",
    )

    # Cleanup
    for clip in video_clips:
        clip.close()
    audio.close()
    final_video.close()

    print(f"\nDone! Output: {output_path}")


# ---------------------------------------------------------------------------
# Step 5: Save/load prompts for review
# ---------------------------------------------------------------------------

def save_prompts(paragraphs: list[dict], prompts: list[str], output_path: Path):
    """Save prompts alongside their paragraph text for review."""
    data = []
    prompt_idx = 0
    for para in paragraphs:
        if para["is_separator"]:
            data.append({
                "type": "separator",
                "start": para["start"],
                "end": para["end"],
            })
        else:
            data.append({
                "type": "paragraph",
                "start": para["start"],
                "end": para["end"],
                "duration": para["duration"],
                "text": para["text"],
                "prompt": prompts[prompt_idx],
            })
            prompt_idx += 1

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Prompts saved to {output_path}")
    print("Review and edit if needed, then re-run with --prompts-file to skip generation.")


def load_prompts(prompts_path: Path) -> list[str]:
    """Load previously saved prompts."""
    with open(prompts_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [item["prompt"] for item in data if item["type"] == "paragraph"]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Aletheia Video Generator — SRT + Audio → Contextual Video"
    )
    parser.add_argument("--srt", required=True, help="Path to SRT subtitle file")
    parser.add_argument("--audio", required=True, help="Path to audio file (MP3/WAV)")
    parser.add_argument("--output", default="output.mp4", help="Output video path")
    parser.add_argument(
        "--cues-per-clip",
        type=int,
        default=CUES_PER_CLIP,
        help=f"Number of SRT cues to group per video clip (default: {CUES_PER_CLIP})",
    )
    parser.add_argument(
        "--prompts-file",
        help="Path to previously saved prompts JSON (skips Claude prompt generation)",
    )
    parser.add_argument(
        "--save-prompts",
        help="Save generated prompts to this JSON file for review before generating video",
    )
    parser.add_argument(
        "--prompts-only",
        action="store_true",
        help="Only generate and save prompts, don't generate video clips",
    )
    parser.add_argument(
        "--video-model",
        default=VIDEO_MODEL,
        help=f"Replicate video model (default: {VIDEO_MODEL})",
    )

    args = parser.parse_args()

    # Update module-level config from args
    _update_config(args.cues_per_clip, args.video_model)

    # Check env vars
    if not args.prompts_file and not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: Set ANTHROPIC_API_KEY environment variable")
        sys.exit(1)
    if not args.prompts_only and not os.environ.get("REPLICATE_API_TOKEN"):
        print("ERROR: Set REPLICATE_API_TOKEN environment variable")
        sys.exit(1)

    # Parse SRT
    print(f"Parsing {args.srt}...")
    paragraphs = parse_srt_file(args.srt)
    text_count = sum(1 for p in paragraphs if not p["is_separator"])
    sep_count = sum(1 for p in paragraphs if p["is_separator"])
    total_duration = sum(p["duration"] for p in paragraphs)
    print(f"  {text_count} text paragraphs, {sep_count} separators")
    print(f"  Total duration: {total_duration:.1f}s ({total_duration/60:.1f} min)")

    # Generate or load prompts
    if args.prompts_file:
        print(f"\nLoading prompts from {args.prompts_file}...")
        prompts = load_prompts(Path(args.prompts_file))
    else:
        prompts = generate_prompts(paragraphs)

    # Save prompts if requested
    if args.save_prompts or args.prompts_only:
        save_path = Path(args.save_prompts or "prompts.json")
        save_prompts(paragraphs, prompts, save_path)
        if args.prompts_only:
            print("\nPrompts-only mode — stopping here.")
            return

    # Generate video clips
    output_dir = Path(args.output).parent / f"{Path(args.output).stem}_assets"
    print(f"\nGenerating {text_count} video clips...")
    print(f"  Model: {VIDEO_MODEL}")
    print(f"  Assets directory: {output_dir}")
    clip_paths = generate_clips(paragraphs, prompts, output_dir)

    # Stitch
    stitch_video(paragraphs, clip_paths, args.audio, args.output)


if __name__ == "__main__":
    main()
