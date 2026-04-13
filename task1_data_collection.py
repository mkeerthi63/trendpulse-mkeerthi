import requests
import json
import os
import time
# API URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")
def fetch_top_story_ids():
    """Fetch list of top story IDs"""
    response = requests.get(TOP_STORIES_URL)
    return response.json()
def fetch_story_details(story_id):
    """Fetch details for a single story"""
    response = requests.get(ITEM_URL.format(story_id))
    return response.json()
def extract_required_fields(story):
    """Extract only required fields"""
    return {
        "id": story.get("id"),
        "title": story.get("title"),
        "by": story.get("by"),
        "score": story.get("score"),
        "time": story.get("time"),
        "url": story.get("url"),
        "descendants": story.get("descendants", 0)
    }
def main():
    print("Fetching top stories...")
    story_ids = fetch_top_story_ids()
    collected_stories = []
    # Loop through story IDs and collect 110 valid stories
    for story_id in story_ids:
        story = fetch_story_details(story_id)
        # Check valid story
        if story and story.get("type") == "story" and story.get("title"):
            cleaned_story = extract_required_fields(story)
            collected_stories.append(cleaned_story)
        # Stop when 110 stories are collected
        if len(collected_stories) >= 110:
            break
        # Delay to avoid hitting API limits
        time.sleep(0.2)
    # Save to JSON file
    file_path = "data/top_stories.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(collected_stories, file, indent=4)
    print(f"Successfully saved {len(collected_stories)} stories to {file_path}")
if __name__ == "__main__":
    main()
