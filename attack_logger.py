import json
import os
from datetime import datetime

LOG_FILE = "attack_logs.json"

def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_log(entry):
    logs = load_logs()
    logs.append(entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

def log_attack(vector, payload, target_url, response_html, success=True):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "vector": vector,
        "payload": payload,
        "target_url": target_url,
        "success": success,
        "response_excerpt": response_html[:500]  # 重くならないように一部だけ
    }
    save_log(entry)
    print("📝 攻撃ログ保存したよ〜♡")