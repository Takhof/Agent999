def summarize_clusters(texts, labels):
    clusters = {}
    for text, label in zip(texts, labels):
        clusters.setdefault(label, []).append(text)

    return clusters