import openai
from openai import OpenAI
import json
import os
from dotenv import load_dotenv
from fetch_articles import extract_article_text


load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))




def summarize_text(text, max_tokens=200):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "あなたはサイバーセキュリティの要約が得意なAIです。セキュリティ対策などに必要な事を抜き出して要約してください。"},
            {"role": "user", "content": f"以下の内容のセキュリティ関連に重要な事などを要約して:\n{text}"}
        ],
        max_tokens=max_tokens,
        temperature=0.5
    )
    return response.choices[0].message.content


def summarize_articles(input_file="999_articles.json", output_file="999_summaries.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    summaries = []

    for i, article in enumerate(articles):
        print(f"📘 {i+1}件目：「{article['title']}」の本文読んでるよ〜")
        article_text = extract_article_text(article['url'])

        if not article_text:
            article_text = article['title']

        summary = summarize_text(article_text[:3000])  # 長すぎ防止
        summaries.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)

    print("✅ 要約ぜんぶ終わったよ〜♡")