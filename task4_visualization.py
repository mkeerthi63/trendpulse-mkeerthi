import pandas as pd
import matplotlib.pyplot as plt
import os
INPUT_FILE = "data/trends_analysed.csv"
OUTPUT_DIR = "charts"  
# Create charts folder if not exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
def shorten_title(title, max_len=50):
    return title if len(title) <= max_len else title[:max_len] + "..."
def main():
    df = pd.read_csv(INPUT_FILE)
    # Chart 1: Top 10 Stories by Score
    top10 = df.nlargest(10, "score").copy()
    top10["short_title"] = top10["title"].apply(shorten_title)
    plt.figure()
    plt.barh(top10["short_title"], top10["score"])
    plt.xlabel("Score")
    plt.ylabel("Story Title")
    plt.title("Top 10 Stories by Score")
    plt.gca().invert_yaxis()
    plt.savefig(f"{OUTPUT_DIR}/chart1_top_stories.png")
    plt.close()
    # Chart 2: Stories per Category
    category_counts = df["category"].value_counts()
    plt.figure()
    plt.bar(category_counts.index, category_counts.values)
    plt.xlabel("Category")
    plt.ylabel("Number of Stories")
    plt.title("Stories per Category")
    plt.savefig(f"{OUTPUT_DIR}/chart2_categories.png")
    plt.close()
    # Chart 3: Score vs Comments
    popular = df[df["is_popular"] == True]
    not_popular = df[df["is_popular"] == False]
    plt.figure()
    plt.scatter(popular["score"], popular["num_comments"], label="Popular")
    plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
    plt.xlabel("Score")
    plt.ylabel("Number of Comments")
    plt.title("Score vs Comments")
    plt.legend()
    plt.savefig(f"{OUTPUT_DIR}/chart3_scatter.png")
    plt.close()
    # Dashboard
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    axes[0].barh(top10["short_title"], top10["score"])
    axes[0].set_title("Top Stories")
    axes[0].invert_yaxis()
    axes[1].bar(category_counts.index, category_counts.values)
    axes[1].set_title("Categories")
    axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
    axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
    axes[2].set_title("Score vs Comments")
    axes[2].legend()
    fig.suptitle("TrendPulse Dashboard")
    plt.savefig(f"{OUTPUT_DIR}/dashboard.png")
    plt.close()
    print("All charts saved in 'charts/' folder")
if __name__ == "__main__":
    main()
