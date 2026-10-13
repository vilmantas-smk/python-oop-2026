"""Solutions for — YouTube API. Tasks.

Run: python slide15_youtube_api.py
Needs sample_response.json in the same folder.
Tasks 1 and 3 need YT_API_KEY in a .env file; without it they are skipped.
"""

import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
MOCK_FILE = Path("sample_response.json")


# ---------------------------------------------------------------- Task 1
def browser_url(api_key):
    """Return the request URL to paste into a browser.

    What to find in the JSON the browser shows:
        items -> 0 -> id -> videoId
        items -> 0 -> snippet -> title
    """
    return (
        f"{SEARCH_URL}?part=snippet&q=python&type=video"
        f"&order=date&maxResults=5&key={api_key}"
    )


# ---------------------------------------------------------------- Task 2
def print_sample_titles():
    """Load the sample response and print every title with its number."""
    with open(MOCK_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    for number, item in enumerate(data["items"], start=1):
        print(f"{number}. {item['snippet']['title']}")


# ---------------------------------------------------------------- Task 3
def first_call(keyword, api_key):
    """Call the API for one keyword and print the status and item count."""
    params = {
        "part": "snippet",
        "q": keyword,
        "type": "video",
        "order": "date",
        "maxResults": 5,
        "key": api_key,
    }
    response = requests.get(SEARCH_URL, params=params, timeout=10)
    print(response.status_code)  # 200 when everything is fine
    data = response.json()
    print(len(data.get("items", [])))  # up to 5


# ---------------------------------------------------------- Project step
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
    for item in data.get("items", []):  # no "items" key -> empty list
        videos.append(parse_video(item))
    return videos


# ------------------------------------------------------------- Try it out
def main():
    load_dotenv()
    api_key = os.environ.get("YT_API_KEY")

    print("Task 1")
    if api_key is None:
        print("No YT_API_KEY in .env — skipped.")
    else:
        print("Paste this into a browser:")
        print(browser_url(api_key))

    print("\nTask 2")
    print_sample_titles()

    print("\nTask 3")
    if api_key is None:
        print("No YT_API_KEY in .env — skipped.")
    else:
        first_call("python", api_key)

    print("\nProject step")
    for video in fetch_videos("python", api_key, use_mock=True):
        print(video)


if __name__ == "__main__":
    main()