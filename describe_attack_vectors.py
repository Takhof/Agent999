from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

attack_vectors = [
    "DOM-based XSS",
    "Blind SQL Injection",
    "Stored XSS",
    "CSRF",
    "Command Injection"
]

def describe_vector(vector_name):
    prompt = f"""
セキュリティ攻撃「{vector_name}」について以下の形式で詳しく教えてください：

1. 名前（英語）：
2. 説明：
3. 攻撃の具体例（コード付き）：
4. 対策方法：
5. 使われやすいケースや脆弱性の発生しやすい場所：
"""
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=800,
        temperature=0.5,
    )
    return res.choices[0].message.content

results = []
for vec in attack_vectors:
    print(f"💬 {vec} を説明中…")
    description = describe_vector(vec)
    results.append({"vector": vec, "description": description})

# 保存！
with open("999_attack_descriptions.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ 攻撃ベクトルの詳細データ作成完了っ♡")