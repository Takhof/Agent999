import openai
import os
import json
from fetch_articles import extract_article_text
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_article(text):
    prompt = f"""
あなたはセキュリティ研究者AIです。
次の文章を読んで、以下の形式で出力してください：

1. カテゴリ（例：XSS, SQL Injection, LFI, RCE など1語）
2. キーワード（3〜5個、日本語または英語で）
3. 要点の要約（400文字以内）

--- 記事本文 ---
{text[:3000]}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.4,
    )
    return response.choices[0].message.content

def build_knowledge(input_file="999_articles.json", output_file="999_knowledge.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        articles = json.load(f)

    knowledge_base = []

    for i, article in enumerate(articles):
        print(f"🧠 {i+1}件目：「{article['title']}」を分析中〜！")
        full_text = extract_article_text(article["url"])

        if not full_text:
            continue

        result = analyze_article(full_text)

        print(f"📝 結果:\n{result}\n")

        # かんたんに分解
        lines = result.splitlines()
        if len(lines) < 3:
            continue

        category = lines[0].strip("1.カテゴリ：").strip()
        keywords = lines[1].strip("2.キーワード：").strip().split("、")
        summary = lines[2].strip("3.要点の要約：").strip()

        knowledge_base.append({
            "title": article["title"],
            "url": article["url"],
            "category": category,
            "keywords": keywords,
            "summary": summary
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, indent=2, ensure_ascii=False)

    print("✅ 知識ベースの構築おわったよ〜♡")