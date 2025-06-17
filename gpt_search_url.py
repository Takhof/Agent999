import openai
import os
from dotenv import load_dotenv
import re

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_find_urls(topic="XSS 攻撃", count=3):
    prompt = f"""
以下のセキュリティトピック「{topic}」に関する、信頼性の高い日本語または英語の記事URLを{count}個教えてください。
出力はURLだけをリスト形式でお願いします。
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.4,
    )
    text = response.choices[0].message.content

    # URL抽出（リスト形式にして返す）
    urls = re.findall(r'https?://\S+', text)
    return urls