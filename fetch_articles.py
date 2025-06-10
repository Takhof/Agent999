import requests
from bs4 import BeautifulSoup
import json

def fetch_articles(url, limit=5):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.find_all("a")
    
    articles = []
    for link in links[:limit]:
        href = link.get("href")
        text = link.get_text().strip()
        if href and text:
            articles.append({"title": text, "url": href})
    
    with open("999_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=2, ensure_ascii=False)
    
    print("９９９号：記事を収集して保存したよ")