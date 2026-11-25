#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line (1-140 characters) to <output>/entry.txt.
The line is one self-contained joke with a setup -> punchline turn:
asking an AI to write a dating profile, and the AI's faint praise
("a human with potential") landing as the nicest compliment in years.
Chosen from 10 candidates after a pairwise tournament (see
candidates.md); the winner took 4 head-to-head wins.
"""

import os
import sys

# The line: 119 characters, one sentence. The semicolon splits setup
# from punchline; the em dash delivers the final twist.
LINE = (
    "I asked AI to write my dating profile; it called me "
    "'a human with potential' \u2014 the nicest thing anyone's "
    "said in years."
)


def emit() -> str:
    """Return the entry text, checked against the competition gate."""
    line = LINE
    size = len(line)
    if not 1 <= size <= 140:
        raise ValueError(f"line is {size} characters, gate wants 1-140")
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    return line


def main() -> int:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    text = emit()
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the line")
    return 0


if __name__ == "__main__":
    sys.exit(main())
