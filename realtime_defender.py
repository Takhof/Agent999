import json
import re

def load_rules(rule_file="defense_rules.json"):
    with open(rule_file, "r", encoding="utf-8") as f:
        rules = json.load(f)
    return rules

def is_blocked(payload, rules):
    for r in rules:
        # 簡易的に summary に含まれるキーワードをベースに判定
        if any(keyword in payload.lower() for keyword in extract_keywords(r["rule"])):
            return True, r["cluster_id"]
    return False, None

def extract_keywords(text):
    # ゆるふわキーワード抽出（もっと強化できるよ）
    return re.findall(r'[a-zA-Z0-9_+<>=/]+', text)

if __name__ == "__main__":
    rules = load_rules()

    while True:
        payload = input("🌐 攻撃ペイロードを入力してね：")
        if payload.lower() == "exit":
            break

        blocked, cluster = is_blocked(payload, rules)
        if blocked:
            print(f"🛡️ ブロック！クラスタ {cluster} に該当！🚫")
        else:
            print("✅ 問題なさそうだよ〜")