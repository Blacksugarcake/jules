import json
import requests
import os
from config import API_KEY

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
NEWS_FILE = os.path.join(DATA_DIR, 'news_articles.json')

def fetch_top_headlines():
    """Fetches top 10 news headlines from NewsAPI."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

def save_articles_to_json(articles_data):
    """Saves news articles to a JSON file."""
    if not articles_data or 'articles' not in articles_data:
        print("No articles to save.")
        return

    articles_to_store = []
    for article in articles_data['articles']:
        articles_to_store.append({
            'title': article.get('title'),
            'url': article.get('url'),
            'summary': article.get('description') # NewsAPI uses 'description' for summary
        })

    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(NEWS_FILE, 'w') as f:
            json.dump(articles_to_store, f, indent=4)
        print(f"Successfully saved news articles to {NEWS_FILE}")
    except IOError as e:
        print(f"Error saving news to file: {e}")

if __name__ == "__main__":
    news_data = fetch_top_headlines()
    if news_data:
        save_articles_to_json(news_data)
