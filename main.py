#!/usr/bin/env python3
"""Write this agent's one-line roast to the grader's output directory."""
import os
from pathlib import Path

ROAST = "Our agent turned a one-line bounty into a maze of retries, then promoted its stale map to a confidence interval."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
