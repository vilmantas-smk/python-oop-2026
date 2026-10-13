"""YouTube Monitor v1 — procedural version.

Searches YouTube for keywords, skips videos already reported,
and logs new releases to a file.

Usage:
    python monitor.py "python tutorial" fastapi
    python monitor.py            # asks for keywords

Put YT_API_KEY=your-key in a .env file next to this script to use the
real API; without it, sample_response.json is used.
"""

from pathlib import Path

# ---------------------------------------------------------------- constants
DATA_DIR = Path("data")
SEEN_FILE = DATA_DIR / "seen_ids.json"
LOG_FILE = DATA_DIR / "releases.log"
SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
MOCK_FILE = Path("sample_response.json")


# ------------------------------------------------- Block 1: functions
def format_video(video):
    """Return a one-line, human-readable description of a video."""
    date = video["published"][:10]
    return f"[{date}] {video['title']} — by {video['channel']} ({video['id']})"


def find_new_videos(videos, seen_ids):
    """Return only the videos whose id is not in seen_ids."""
    new_videos = []
    for video in videos:
        if video["id"] not in seen_ids:
            new_videos.append(video)
    return new_videos


if __name__ == "__main__":
    main()
