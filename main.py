import requests
import subprocess
from bs4 import BeautifulSoup

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

# 実行
agent = Agent999()
agent.say_hello()
agent.search_web("XSS 攻撃とは")
agent.fetch_ctf_topics()