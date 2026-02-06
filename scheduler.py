import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple jobs scheduler MVP")
    parser.add_argument("--jobs", required=True)
    args = parser.parse_args()

    config = json.loads(Path(args.jobs).read_text())
    now = datetime.now(timezone.utc).isoformat()
    runs = []
    for job in config.get("jobs", []):
        runs.append({"job_id": job["id"], "scheduled": job["schedule"], "executed_at": now, "status": "queued"})

    print(json.dumps({"runs": runs}, indent=2))


if __name__ == "__main__":
    main()
