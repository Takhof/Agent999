import json
import difflib

def load_summaries(file="999_summaries.json"):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def find_best_match(question, summaries):
    titles = [s['title'] for s in summaries]
    best = difflib.get_close_matches(question, titles, n=1, cutoff=0.3)
    
    if best:
        for s in summaries:
            if best[0] in s['title']:
                return s
    return None

def answer_question(question):
    summaries = load_summaries()
    best = find_best_match(question, summaries)

    if best:
        print(f"\n９９９号：これ、どうかなぁ？\n")
        print(f"🔖タイトル: {best['title']}")
        print(f"📎URL: {best['url']}")
        print(f"📚要約: {best['summary']}")
    else:
        print("９９９号：うぅ、ごめんね…そのこと、まだ知らないかも〜〜〜〜🥺")