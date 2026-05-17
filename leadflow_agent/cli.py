from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from .drafts import build_reply_draft, summarize_lead
from .scoring import score_lead


def process_csv(input_path: Path, output_path: Path) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0

    with input_path.open(newline="", encoding="utf-8") as input_file, output_path.open(
        "w", encoding="utf-8"
    ) as output_file:
        reader = csv.DictReader(input_file)
        for lead in reader:
            scored = score_lead(lead)
            record = {
                "lead": lead,
                "summary": summarize_lead(lead),
                "score": scored.score,
                "priority": scored.priority,
                "next_action": scored.next_action,
                "reason": scored.reason,
                "reply_draft": build_reply_draft(lead, scored.priority),
            }
            output_file.write(json.dumps(record, ensure_ascii=True) + "\n")
            count += 1

    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Score leads and generate reply drafts.")
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_jsonl", type=Path)
    args = parser.parse_args()

    count = process_csv(args.input_csv, args.output_jsonl)
    print(f"Processed {count} leads -> {args.output_jsonl}")


if __name__ == "__main__":
    main()

