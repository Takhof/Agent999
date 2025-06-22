import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def load_attack_texts(log_file="attack_logs.json"):
    with open(log_file, "r", encoding="utf-8") as f:
        logs = json.load(f)
    return [log["payload"] for log in logs]

def classify_patterns(texts, num_clusters=3):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)

    kmeans = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans.fit(X)

    return kmeans.labels_, vectorizer, kmeans


if __name__ == "__main__":
    texts = load_attack_texts()
    labels, vec, model = classify_patterns(texts)

    for i, label in enumerate(labels):
        print(f"攻撃 {i+1} はクラスター {label}")