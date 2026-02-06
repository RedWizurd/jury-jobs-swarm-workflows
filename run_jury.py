import argparse
import json
from collections import Counter
from pathlib import Path


def mock_vote(name: str, model: str, task: str) -> str:
    seed = f"{name}:{model}:{task}"
    return "accept" if sum(ord(ch) for ch in seed) % 2 == 0 else "revise"


def main() -> None:
    parser = argparse.ArgumentParser(description="Sequential jury run MVP")
    parser.add_argument("--config", required=True)
    parser.add_argument("--task", required=False)
    args = parser.parse_args()

    cfg = json.loads(Path(args.config).read_text())
    task = args.task or cfg.get("task", "review")

    votes = []
    for p in cfg.get("participants", []):
        decision = mock_vote(p["name"], p["model"], task)
        votes.append({"participant": p["name"], "model": p["model"], "decision": decision})

    counts = Counter(v["decision"] for v in votes)
    consensus = counts.most_common(1)[0][0] if votes else "no-votes"
    print(json.dumps({"task": task, "votes": votes, "consensus": consensus}, indent=2))


if __name__ == "__main__":
    main()
