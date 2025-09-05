from flask import Flask, request, render_template_string
import feedparser

app = Flask(__name__)

# HTML template using Jinja2 (can be placed in templates folder if preferred)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Latest News</title>
</head>
<body>
    <h1>Latest News for "{{ query }}"</h1>
    <form method="get">
        <input type="text" name="q" value="{{ query }}" placeholder="Enter search term">
        <button type="submit">Search</button>
    </form>
    <ul>
    {% if entries %}
        {% for entry in entries %}
            <li>
                <a href="{{ entry.link }}" target="_blank">{{ entry.title }}</a>
            </li>
        {% endfor %}
    {% else %}
        <li>No news articles found.</li>
    {% endif %}
    </ul>
</body>
</html>
"""

def fetch_news(query="Trump vs Modi", max_results=5):
    query_encoded = query.replace(" ", "+")
    rss_url = f"https://news.google.com/rss/search?q={query_encoded}"
    feed = feedparser.parse(rss_url)
    return feed.entries[:max_results]

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('q', 'Trump vs Modi')
    entries = fetch_news(query)
    return render_template_string(HTML_TEMPLATE, query=query, entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
