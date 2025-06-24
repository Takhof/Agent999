import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_generate_defense(summary):
    prompt = f"""
以下の攻撃要約に基づいて、Webアプリケーションで使える防御ルールや検知パターンを1〜3個程度提案してください。
できればWAF（Web Application Firewall）向けルールのような形式でお願いします。

攻撃要約:
{summary}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

def generate_rules(input_file="cluster_summaries.json", output_file="defense_rules.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        summaries = json.load(f)

    rules = []
    for item in summaries:
        print(f"🛡️ クラスタ {item['cluster_id']} の防御ルール作ってるよ〜")
        rule = gpt_generate_defense(item["summary"])
        rules.append({
            "cluster_id": item["cluster_id"],
            "rule": rule
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(rules, f, indent=2, ensure_ascii=False)

    print("✅ 防御ルール作成完了っ♡")

if __name__ == "__main__":
    generate_rules()