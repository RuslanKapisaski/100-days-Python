import os
import json

SCORES_FILE = os.path.join(os.path.dirname(__file__), "typing_scores.json")

def load_scores() -> list:
    try:
        with open(SCORES_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_score(wpm: float, accuracy: float, title: str):
    scores = load_scores()
    scores.append({"wpm": round(wpm, 1), "accuracy": round(accuracy, 1), "title": title})
    scores.sort(key=lambda s: s["wpm"], reverse=True)
    scores = scores[:10]          # keep top-10
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)