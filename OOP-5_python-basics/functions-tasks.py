"""Solutions for slide 9 — Functions. Tasks.

Run: python slide09_functions.py
"""


# ---------------------------------------------------------------- Task 1
def greet(name, greeting="Hello"):
    """Return a greeting such as 'Hello, Ana!'."""
    return f"{greeting}, {name}!"


# ---------------------------------------------------------------- Task 2
def average(numbers):
    """Return the mean rounded to 1 decimal, or 0 for an empty list."""
    if not numbers:  # an empty list is falsy
        return 0
    return round(sum(numbers) / len(numbers), 1)


# ---------------------------------------------------------------- Task 3
def min_max(numbers):
    """Return the smallest and the largest value as a tuple."""
    return min(numbers), max(numbers)


# ---------------------------------------------------------- Project step
# Data from the handout (handout_videos.py)
videos = [
    {"id": "abc123", "title": "Python Tips", "channel": "CodeChannel",
     "published": "2026-09-28T14:00:00Z"},
    {"id": "def456", "title": "Learn OOP", "channel": "DevSchool",
     "published": "2026-09-27T09:30:00Z"},
    {"id": "ghi789", "title": "Sets Explained", "channel": "CodeChannel",
     "published": "2026-09-25T18:15:00Z"},
]
seen_ids = {"def456"}


def format_video(video):
    """Return a one-line, human-readable description of a video."""
    date = video["published"][:10]  # first 10 characters: YYYY-MM-DD
    return f"[{date}] {video['title']} — by {video['channel']} ({video['id']})"


def find_new_videos(videos, seen_ids):
    """Return only the videos whose id is not in seen_ids."""
    new_videos = []
    for video in videos:
        if video["id"] not in seen_ids:
            new_videos.append(video)
    return new_videos


# ------------------------------------------------------------- Try it out
print("Task 1")
print(greet("Ana"))                  # Hello, Ana!
print(greet("Ana", greeting="Labas"))  # Labas, Ana!

print("\nTask 2")
print(average([88, 92, 79]))         # 86.3
print(average([]))                   # 0

print("\nTask 3")
low, high = min_max([4, 9, 2])
print(low, high)                     # 2 9

print("\nProject step")
print(format_video(videos[0]))       # [2026-09-28] Python Tips — by CodeChannel (abc123)
for video in find_new_videos(videos, seen_ids):
    print(format_video(video))       # abc123 and ghi789, not def456