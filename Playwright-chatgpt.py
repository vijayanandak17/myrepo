import feedparser

def get_latest_news(query="Trump vs Modi", max_results=5):
    # Replace spaces with '+' for URL encoding
    query_encoded = query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={query_encoded}"

    print(f"Fetching news for: {query}\n")

    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    if not feed.entries:
        print("No news articles found.")
        return

    for i, entry in enumerate(feed.entries[:max_results], 1):
        print(f"{i}. {entry.title}")
        print(f"   {entry.link}\n")

if __name__ == "__main__":
    get_latest_news()
