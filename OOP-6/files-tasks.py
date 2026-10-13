"""Solutions for — Files & JSON. Tasks.

Run: python slide13_files_json.py     (run it 3 times for Task 1)

The project-step demo writes to data/demo_seen_ids.json and
data/demo_releases.log, so it never touches the real monitor files.
"""

import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
DIARY_FILE = DATA_DIR / "diary.txt"
SETTINGS_FILE = Path("settings.json")


# ---------------------------------------------------------------- Task 1
def write_diary():
    """Append the current time to data/diary.txt."""
    DATA_DIR.mkdir(exist_ok=True)
    with open(DIARY_FILE, "a", encoding="utf-8") as f:  # "a" = append
        f.write(f"{datetime.now()}\n")                  # add \n yourself


# ---------------------------------------------------------------- Task 2
def count_lines():
    """Return how many lines data/diary.txt has."""
    count = 0
    with open(DIARY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            count += 1
    return count


# ---------------------------------------------------------------- Task 3
def save_and_load_settings():
    """Save settings as JSON, load them back and return the volume."""
    settings = {"theme": "dark", "volume": 7}
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    return loaded["volume"]


# ---------------------------------------------------------- Project step
def format_video(video):
    """From slide 9: one-line description of a video."""
    date = video["published"][:10]
    return f"[{date}] {video['title']} — by {video['channel']} ({video['id']})"


def load_seen_ids(path):
    """Return the set of already-reported video ids."""
    if not path.exists():
        return set()  # first run: nothing seen yet
    with open(path, "r", encoding="utf-8") as f:
        return set(json.load(f))  # JSON list -> set


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


# ------------------------------------------------------------- Try it out
def main():
    print("Task 1")
    write_diary()
    print(f"Added one line to {DIARY_FILE}")

    print("\nTask 2")
    print(f"{DIARY_FILE} has {count_lines()} line(s)")

    print("\nTask 3")
    print(f"Volume: {save_and_load_settings()}")  # Volume: 7

    print("\nProject step")
    seen_file = DATA_DIR / "demo_seen_ids.json"
    log_file = DATA_DIR / "demo_releases.log"
    video = {"id": "abc123", "title": "Python Tips", "channel": "CodeChannel",
             "published": "2026-09-28T14:00:00Z"}

    seen_ids = load_seen_ids(seen_file)
    print(f"Loaded {len(seen_ids)} seen id(s): {sorted(seen_ids)}")
    if video["id"] not in seen_ids:
        log_release(log_file, video, "python")
        seen_ids.add(video["id"])
        print(f"Logged {video['id']} to {log_file}")
    else:
        print(f"{video['id']} was already seen, nothing logged")
    save_seen_ids(seen_file, seen_ids)


if __name__ == "__main__":
    main()