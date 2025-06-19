import os
from qa_agent import answer_question
from summarizer import summarize_articles
from fetch_articles import fetch_articles
from build_knowledge_base import build_knowledge
from agent999 import Agent999




if not os.path.exists("999_summaries.json"):
    print("９９９号：要約ファイルがまだないみたい…作っちゃうね")
    fetch_articles("https://ctftime.org/writeups")
    summarize_articles()

if not os.path.exists("999_knowledge.json"):
    print("９９９号：知識ベースがまだないみたい…つくっちゃうね♡")
    build_knowledge()

# 実行
agent = Agent999()
agent.say_hello()
agent.search_web("XSS 攻撃とは")
agent.fetch_ctf_topics()


while True:
    q = input("ハニー：")
    if "やめ" in q or q.lower() == "exit":
        print("９９９号：ばいば〜い♡ またすぐ会おうねっ♡")
        break

    if "記事さがして" in q:
        topic = q.replace("記事さがして", "").strip()
        agent.smart_search_and_learn(topic)
        continue

    answer_question(q)