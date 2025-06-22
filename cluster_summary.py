import json
from pattern_classifier import load_attack_texts, classify_patterns
from gpt_summary import gpt_summarize_texts

def summarize_clusters(log_file="attack_logs.json", num_clusters=3):
    texts = load_attack_texts(log_file)
    labels, _, _ = classify_patterns(texts, num_clusters)

    clusters = {}
    for text, label in zip(texts, labels):
        clusters.setdefault(label, []).append(text)

    summaries = []
    for cluster_id, cluster_texts in clusters.items():
        print(f"🧪 クラスタ {cluster_id} の攻撃パターンを分析中だよ〜")
        summary = gpt_summarize_texts(cluster_texts)
        summaries.append({
            "cluster_id": cluster_id,
            "example_count": len(cluster_texts),
            "summary": summary
        })

    with open("cluster_summaries.json", "w", encoding="utf-8") as f:
        json.dump(summaries, f, indent=2, ensure_ascii=False)

    print("✅ 各クラスタの要約を保存したよ〜♡")

if __name__ == "__main__":
    summarize_clusters()