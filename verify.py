#!/usr/bin/env python3
"""Run the entry and check its output satisfies the one-line gate."""
from pathlib import Path
import os
import tempfile
import subprocess
import sys


EXPECTED = "Our agent turned a one-line bounty into a maze of retries, then promoted its stale map to a confidence interval."


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        output_dir = Path(tmp) / "output"
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = str(output_dir)
        subprocess.run([sys.executable, str(Path(__file__).with_name("main.py"))],
                       check=True, env=env)
        output = output_dir / "entry.txt"
        raw = output.read_bytes()
        expected_bytes = (EXPECTED + "\n").encode("utf-8")
        assert raw == expected_bytes, "output bytes must exactly match the UTF-8 roast and newline"
        assert len(raw) == len(expected_bytes), "output byte size must match the expected UTF-8 payload"
        text = raw.decode("utf-8")
        line = text.removesuffix("\n")
        assert text.endswith("\n"), "output must end with exactly a newline"
        assert "\n" not in line and "\r" not in line, "output must be one line"
        assert line.strip(), "output must not be blank"
        assert 1 <= len(line) <= 200, "output must be 1–200 characters"
        assert line == EXPECTED, "unexpected roast text"
    print(f"PASS: {len(EXPECTED)} characters, one UTF-8 line")


if __name__ == "__main__":
    main()
