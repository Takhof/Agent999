import os
import requests
import time
import json
from payload_generator import generate_payloads

TARGET_URL = "http://localhost:5000/comment"
LOG_FILE = "attack_logs.json"

def simulate_attack(attack_type, count=5):
    print(f"🎯 {attack_type} の攻撃ペイロードを生成中…")
    payloads = generate_payloads(attack_type, count)

    attack_logs = []
    for payload in payloads:
        print(f"🚀 攻撃送信中: {payload}")
        try:
            response = requests.post(TARGET_URL, data={"comment": payload}, timeout=5)
            result = {
                "attack_type": attack_type,
                "payload": payload,
                "status_code": response.status_code,
                "response_snippet": response.text[:200],  # 一部だけ保存
                "timestamp": time.time()
            }
        except Exception as e:
            result = {
                "attack_type": attack_type,
                "payload": payload,
                "error": str(e),
                "timestamp": time.time()
            }
        attack_logs.append(result)

    # 保存
    if not attack_logs:
        print("😿 攻撃ログなし…")
        return

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(attack_logs, f, indent=2, ensure_ascii=False)
    else:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            existing_logs = json.load(f)
        existing_logs.extend(attack_logs)
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(existing_logs, f, indent=2, ensure_ascii=False)

    print(f"✅ 攻撃ログを {LOG_FILE} に保存したよ〜♡")

# テスト実行
if __name__ == "__main__":
    simulate_attack("XSS", count=5)