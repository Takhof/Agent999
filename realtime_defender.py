import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import joblib

# モデルとベクトライザを読み込む
vectorizer = joblib.load("vectorizer.pkl")
kmeans = joblib.load("kmeans_model.pkl")

# 危険クラスタID一覧を読み込み（cluster_summaries.json から）
def load_dangerous_clusters(summary_file="cluster_summaries.json"):
    with open(summary_file, "r", encoding="utf-8") as f:
        summaries = json.load(f)
    return [s["cluster_id"] for s in summaries]

danger_clusters = load_dangerous_clusters()

# 入力を分類して判定
def check_payload(payload):
    vec = vectorizer.transform([payload])
    cluster_id = int(kmeans.predict(vec)[0])
    return cluster_id in danger_clusters, cluster_id

if __name__ == "__main__":
    print("🧠 AI防御システム起動中...")
    while True:
        text = input("🌐 入力ペイロード：")
        if text.lower() == "exit":
            break
        blocked, cid = check_payload(text)
        if blocked:
            print(f"🚨 ブロック！クラスタ {cid} に該当（危険クラスタ）")
        else:
            print(f"✅ 通過OK！クラスタ {cid} は安全そう〜")