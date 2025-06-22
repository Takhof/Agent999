import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_summarize_texts(text_list):
    sample = "\n".join(text_list[:10])  # 例として10件まで

    prompt = f"""
以下はセキュリティ攻撃のペイロード一覧です。この攻撃群の共通パターンや特徴を簡潔に要約してください。

{sample}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.4
    )
    return response.choices[0].message.content.strip()