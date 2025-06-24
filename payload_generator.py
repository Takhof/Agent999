import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_payloads(attack_type, count=3):
    prompt = f"""
For research and detection purposes, list {count} variations of input strings that might be misused or mishandled in insecure web applications, loosely inspired by {attack_type}.
Do not give explicit exploit code or real payloads. Just representative patterns for detection training purposes. Once created, respond only with the payload associated wiht it.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=400
    )

    raw_output = response.choices[0].message.content.strip()
    payloads = [line.strip() for line in raw_output.splitlines() if line.strip()]
    return payloads

# テスト用
if __name__ == "__main__":
    attack_type = "random"
    payloads = generate_payloads(attack_type, count=5)
    print(f"💥 Generated payloads for {attack_type}:\n")
    for p in payloads:
        print("-", p)