import os
import time
import praw

# Expected environment variables:
# REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
# READ-ONLY: fetches recent posts and prints titles + links.

SUBREDDITS = ["stocks", "options", "investing", "securityanalysis", "thetagang"]

def main():
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ["REDDIT_USER_AGENT"],
        check_for_async=False,
    )

    for sub in SUBREDDITS:
        print(f"\n=== r/{sub} ===")
        for post in reddit.subreddit(sub).new(limit=25):
            print(f"- {post.title} ({post.url})")
            time.sleep(0.25)  # light pacing; real tool should cache

if __name__ == "__main__":
    main()
