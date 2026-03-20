#!/usr/bin/env python3
"""
Fetch YouTube transcripts for new podcast episodes using youtube-transcript-api.
Reads feed-podcasts.json, adds transcript field to each episode, writes back.
Free, no API key needed.
"""

import json
import sys
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("youtube-transcript-api not installed, skipping transcripts", file=sys.stderr)
    sys.exit(0)

FEED_PATH = Path(__file__).parent.parent / "feed-podcasts.json"


def fetch_transcript(video_id):
    """Fetch transcript text for a YouTube video. Returns empty string on failure."""
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=["en", "zh-Hans", "zh-Hant"])
        return " ".join(snippet.text for snippet in transcript.snippets)
    except Exception as e:
        print(f"  Transcript unavailable for {video_id}: {e}", file=sys.stderr)
        return ""


def main():
    if not FEED_PATH.exists():
        print("feed-podcasts.json not found", file=sys.stderr)
        sys.exit(0)

    feed = json.loads(FEED_PATH.read_text())
    podcasts = feed.get("podcasts", [])

    if not podcasts:
        print("No new episodes, skipping transcript fetch", file=sys.stderr)
        sys.exit(0)

    print(f"Fetching transcripts for {len(podcasts)} episodes...", file=sys.stderr)

    for ep in podcasts:
        video_id = ep.get("videoId", "")
        if not video_id:
            continue
        print(f"  {ep['name']}: {ep['title'][:60]}...", file=sys.stderr)
        transcript = fetch_transcript(video_id)
        if transcript:
            ep["transcript"] = transcript
            print(f"    OK ({len(transcript)} chars)", file=sys.stderr)
        else:
            print(f"    No transcript available", file=sys.stderr)

    FEED_PATH.write_text(json.dumps(feed, indent=2, ensure_ascii=False))
    episodes_with_transcript = sum(1 for ep in podcasts if ep.get("transcript"))
    print(f"Done: {episodes_with_transcript}/{len(podcasts)} episodes have transcripts", file=sys.stderr)


if __name__ == "__main__":
    main()
