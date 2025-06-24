import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def load_labeled_attacks(filename="attack_logs.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    texts = [entry["payload"] for entry in data]
    labels = [entry["label"] for entry in data]
    return texts, labels

def train_classifier():
    texts, labels = load_labeled_attacks()
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.3, random_state=42
    )

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    print("📊 分類レポート:\n")
    print(classification_report(y_test, predictions))

    return model

if __name__ == "__main__":
    trained_model = train_classifier()