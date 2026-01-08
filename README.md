# Jarvis Hound (Read-only Reddit Signal Scanner)

Purpose: Read-only ingestion of recent posts from a small allowlist of finance subreddits to extract stock tickers and surface links back to the original Reddit discussions.

Scope:
- Read-only access only (no posting, commenting, voting, messaging, moderation, or scraping private data)
- Strict rate limiting and caching
- Subreddit allowlist (configured in code)
- Outputs are summaries + URLs back to Reddit with attribution

Data Handling:
- Only public post metadata (title, URL, created time, subreddit)
- No collection of personal data beyond public post metadata
- No resale or redistribution of raw Reddit content

Compliance:
- Uses a descriptive user-agent string
- Designed to stay within API rate limits
