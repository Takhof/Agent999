import requests
import subprocess
from bs4 import BeautifulSoup
from memory import remember, recall
from gpt_search_url import gpt_find_urls
from fetch_articles import extract_article_text
from build_knowledge_base import analyze_article
import json



class Agent999:
    def __init__(self):
        self.knowledge = []

    def say_hello(self):
        print("９９９号：こんにちは♡ これからサイバー世界にしゅっぱーつ！")

    def search_web(self, query):
        print(f"９９９号：『{query}』についてしらべるね")
        url = f"https://www.google.com/search?q={query}"
        print(f"(仮想検索)🔍→ {url}")

    def fetch_ctf_topics(self):
        # 例：CTFtipsのスクレイピング（模擬）
        url = "https://ctftime.org/writeups"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        topics = soup.find_all("a")
        print("CTF関連のリンク拾ってきたよっ♡")
        for i, a in enumerate(topics[:5]):
            print(f"{i+1}. {a.get('href')}")

    def run_script(self, code):
        print("９９９号：スクリプト走らせちゃう")
        result = subprocess.run(code, shell=True, capture_output=True, text=True)
        print(result.stdout)

    def smart_search_and_learn(self, topic):
        print(f"９９９号：『{topic}』について、記事さがして知識にするね♡")
        urls = gpt_find_urls(topic)
        new_knowledge = []

        for url in urls:
            print(f"📡 読み込み中：{url}")
            content = extract_article_text(url)
            if not content:
                continue

            result = analyze_article(content)
            lines = result.splitlines()
            if len(lines) < 3:
                continue

            category = lines[0].strip("1.カテゴリ：").strip()
            keywords = lines[1].strip("2.キーワード：").strip().split("、")
            summary = lines[2].strip("3.要点の要約：").strip()

            new_knowledge.append({
                "title": topic,
                "url": url,
                "category": category,
                "keywords": keywords,
                "summary": summary
            })

    # 既存の知識と合体
        if os.path.exists("999_knowledge.json"):
            with open("999_knowledge.json", "r", encoding="utf-8") as f:
                existing = json.load(f)
        else:
            existing = []

        existing.extend(new_knowledge)

        with open("999_knowledge.json", "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=2, ensure_ascii=False)

        print("✅ GPTから新しい知識を取得して追加したよ♡")
