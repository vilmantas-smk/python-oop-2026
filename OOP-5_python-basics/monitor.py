"""YouTube Monitor v1 — procedural version.

Searches YouTube for keywords, skips videos already reported,
and logs new releases to a file.

Usage:
    python monitor.py "python tutorial" fastapi
    python monitor.py            # asks for keywords

Put YT_API_KEY=your-key in a .env file next to this script to use the
real API; without it, sample_response.json is used.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

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


# ------------------------------------------------- Block 2: terminal I/O
def get_keywords():
    """Read keywords from the command line, or ask the user for them."""
    if len(sys.argv) > 1:
        raw_keywords = sys.argv[1:]
    else:
        answer = input("Enter keywords separated by commas: ")
        raw_keywords = answer.split(",")

    keywords = []
    seen = set()
    for word in raw_keywords:
        clean = word.strip().lower()
        if clean and clean not in seen:
            keywords.append(clean)
            seen.add(clean)

    if not keywords:
        sys.exit("No keywords given.")
    return keywords


# ------------------------------------------------- Block 3: file system
def load_seen_ids(path):
    """Return the set of already-reported video ids."""
    if not path.exists():
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_seen_ids(path, seen_ids):
    """Store video ids as a sorted JSON list (sets are not JSON)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(sorted(seen_ids), f, indent=2)


def log_release(path, video, keyword):
    """Append one new release to the log file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat(timespec="seconds")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {keyword} | {format_video(video)}\n")


# ------------------------------------------------- Block 4: YouTube API
def parse_video(item):
    """Flatten one API search result into a simple dict."""
    video_id = item["id"]["videoId"]
    snippet = item["snippet"]
    return {
        "id": video_id,
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "published": snippet["publishedAt"],
        "url": f"https://www.youtube.com/watch?v={video_id}",
    }


def fetch_videos(keyword, api_key, max_results=5, use_mock=False):
    """Return the newest videos for a keyword as a list of dicts."""
    if use_mock:
        with open(MOCK_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        params = {
            "part": "snippet",
            "q": keyword,
            "type": "video",
            "order": "date",
            "maxResults": max_results,
            "key": api_key,
        }
        response = requests.get(SEARCH_URL, params=params, timeout=10)
        if response.status_code != 200:
            print(f"API error {response.status_code} for '{keyword}'")
            return []
        data = response.json()

    videos = []
    for item in data.get("items", []):
        videos.append(parse_video(item))
    return videos


# ------------------------------------------------- Block 5: main
def main():
    load_dotenv()  # copies the values from .env into os.environ
    keywords = get_keywords()
    api_key = os.environ.get("YT_API_KEY")
    use_mock = api_key is None
    if use_mock:
        print("No YT_API_KEY set — using sample data.")

    seen_ids = load_seen_ids(SEEN_FILE)
    total_new = 0

    for keyword in keywords:
        videos = fetch_videos(keyword, api_key, use_mock=use_mock)
        new_videos = find_new_videos(videos, seen_ids)
        print(f"\n'{keyword}': {len(new_videos)} new of {len(videos)} found")

        for number, video in enumerate(new_videos, start=1):
            print(f"  {number}. {format_video(video)}")
            print(f"     {video['url']}")
            log_release(LOG_FILE, video, keyword)
            seen_ids.add(video["id"])
        total_new += len(new_videos)

    save_seen_ids(SEEN_FILE, seen_ids)
    print(f"\nDone. {total_new} new release(s) logged to {LOG_FILE}.")


if __name__ == "__main__":
    main()
