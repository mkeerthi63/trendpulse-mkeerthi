import pandas as pd
import os
INPUT_FILE = "data/top_stories.json"  
OUTPUT_FILE = "data/trends_clean.csv"
def main():
    # Load JSON File
    df = pd.read_json(INPUT_FILE)
    print(f"Loaded {len(df)} stories from {INPUT_FILE}\n")
    # Rename columns to match expected names
    df = df.rename(columns={
        "id": "post_id",
        "descendants": "num_comments"
    })
    df["category"] = "technology"
    # Clean the Data
    # Remove duplicates
    df = df.drop_duplicates(subset="post_id")
    print(f"After removing duplicates: {len(df)}")
    # Remove missing values
    df = df.dropna(subset=["post_id", "title", "score"])
    print(f"After removing nulls: {len(df)}")
    # Fix data types
    df["score"] = df["score"].astype(int)
    df["num_comments"] = df["num_comments"].fillna(0).astype(int)
    # Remove low quality stories (score < 5)
    df = df[df["score"] >= 5]
    print(f"After removing low scores: {len(df)}\n")
    # Remove extra whitespace from title
    df["title"] = df["title"].str.strip()
    #  Save as CSV
    if not os.path.exists("data"):
        os.makedirs("data")
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(df)} rows to {OUTPUT_FILE}\n")
    # Print summary (stories per category)
    print("Stories per category:")
    print(df["category"].value_counts())
if __name__ == "__main__":
    main()
