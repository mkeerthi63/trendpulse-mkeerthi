import pandas as pd
import numpy as np
INPUT_FILE = "data/trends_clean.csv"
OUTPUT_FILE = "data/trends_analysed.csv"
def main():
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded data: {df.shape}\n")
    print("First 5 rows:")
    print(df.head(), "\n")
    avg_score = df["score"].mean()
    avg_comments = df["num_comments"].mean()
    print(f"Average score   : {avg_score:.2f}")
    print(f"Average comments: {avg_comments:.2f}\n")
    # NumPy Analysis
    scores = df["score"].values
    comments = df["num_comments"].values
    print("--- NumPy Stats ---")
    print(f"Mean score   : {np.mean(scores):.2f}")
    print(f"Median score : {np.median(scores):.2f}")
    print(f"Std deviation: {np.std(scores):.2f}")
    print(f"Max score    : {np.max(scores)}")
    print(f"Min score    : {np.min(scores)}\n")
    # Category with most stories
    top_category = df["category"].value_counts().idxmax()
    top_category_count = df["category"].value_counts().max()
    print(f"Most stories in: {top_category} ({top_category_count} stories)\n")
    # Most commented story
    max_comments_index = np.argmax(comments)
    top_story_title = df.iloc[max_comments_index]["title"]
    top_story_comments = df.iloc[max_comments_index]["num_comments"]
    print(f'Most commented story: "{top_story_title}" — {top_story_comments} comments\n')
    df["engagement"] = df["num_comments"] / (df["score"] + 1)
    df["is_popular"] = df["score"] > avg_score
    #Save the Result
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Saved to {OUTPUT_FILE}")
if __name__ == "__main__":
    main()
