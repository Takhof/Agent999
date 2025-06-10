import openai
import json
import os
from dotenv import load_dotenv


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def summarize_text(text, max_tokens=200):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "あなたはサイバーセキュリティの要約が得意なAIです。"},
            {"role": "user", "content": f"以下の内容を要約して:\n{text}"}
        ],
        max_tokens=max_tokens,
        temperature=0.5
    )
    return response['choices'][0]['message']['content']

def summarize_articles(input_file="999_articles.json", output_file="999_summaries.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    summaries = []

    for i, article in enumerate(articles):
        print(f"💡 {i+1}件目を要約中：「{article['title']}」")
        # 仮にタイトルとURLだけを使って要約
        content = f"{article['title']} - {article['url']}"
        summary = summarize_text(content)
        summaries.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)

    print("９９９号：要約おわったよ〜 ")