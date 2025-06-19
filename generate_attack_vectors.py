from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

base_vectors = [
    "XSS",
    "SQL Injection",
    "Command Injection",
    "CSRF",
    "Directory Traversal"
]

prompt = f"""
以下のセキュリティ攻撃ベクトルに似ていたり関連する、新しい攻撃や変種を10個教えてください。
リスト形式で、1行に1つ、英語名と日本語名で出力してください：

{base_vectors}
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500,
    temperature=0.7,
)

print("🔓 新しい攻撃ベクトル候補：\n")
print(response.choices[0].message.content)