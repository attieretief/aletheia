# Aletheia Video Generator

Turns ElevenLabs audiobook output (audio + SRT) into a faceless video with AI-generated contextual visuals.

## Setup

```bash
pip install replicate anthropic moviepy srt
```

Set your API keys:
```bash
export REPLICATE_API_TOKEN="r8_your_key_here"
export ANTHROPIC_API_KEY="sk-ant-your_key_here"
```

## Workflow

### Step 1: Generate prompts only (review before spending on video generation)

```bash
python generate_video.py \
    --srt reeks01.srt \
    --audio reeks01.mp3 \
    --prompts-only \
    --save-prompts prompts.json
```

This parses your SRT, groups cues into paragraphs, and uses Claude to generate a cinematic video prompt per paragraph. The output `prompts.json` looks like:

```json
[
  {
    "type": "paragraph",
    "start": 0.0,
    "end": 17.0,
    "duration": 17.0,
    "text": "Sessie 1: Wat bedoel ons met God...",
    "prompt": "Slow dolly through ancient cathedral nave, golden light streaming through stained glass"
  },
  {
    "type": "separator",
    "start": 38.0,
    "end": 40.0
  }
]
```

**Edit the prompts** in this file if any don't feel right, then proceed to step 2.

### Step 2: Generate video using your reviewed prompts

```bash
python generate_video.py \
    --srt reeks01.srt \
    --audio reeks01.mp3 \
    --prompts-file prompts.json \
    --output reeks01_video.mp4
```

This calls Replicate Wan 2.1 for each paragraph, then stitches the clips with the audio into a final MP4.

### One-shot (skip review)

```bash
python generate_video.py \
    --srt reeks01.srt \
    --audio reeks01.mp3 \
    --output reeks01_video.mp4 \
    --save-prompts prompts.json
```

Generates prompts, saves them for reference, generates clips, and stitches — all in one go.

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--srt` | required | Path to SRT file from ElevenLabs |
| `--audio` | required | Path to audio file (MP3/WAV) |
| `--output` | `output.mp4` | Output video path |
| `--cues-per-clip` | `4` | Number of SRT cues grouped per video clip |
| `--prompts-file` | — | Load prompts from JSON (skips Claude) |
| `--save-prompts` | — | Save prompts to JSON for review |
| `--prompts-only` | — | Only generate prompts, don't make video |
| `--video-model` | `wavespeedai/wan-2.1-t2v-480p` | Replicate model to use |

## Tuning

**`--cues-per-clip`** controls visual pacing. With the default of 4, you get a new visual roughly every 10–15 seconds. Set it lower (2–3) for faster cuts, higher (6–8) for longer held shots.

**Video model alternatives on Replicate:**
- `wavespeedai/wan-2.1-t2v-480p` — fastest, cheapest (~$0.02/clip)
- `wan-video/wan-2.1-t2v-720p` — higher resolution, slower (~$0.08/clip)

## Cost estimate

For 8 sessions (~2,400 words, ~18 min audio):
- ~40–50 paragraphs at 4 cues each
- Claude prompt generation: ~$0.10
- Replicate Wan 480p: ~$0.02 × 45 clips = ~$0.90
- **Total: ~$1.00**

## After generation

Drop the final MP4 into ElevenLabs Studio to:
1. Add captions (Studio auto-transcribes)
2. Add background music
3. Fine-tune any cuts
