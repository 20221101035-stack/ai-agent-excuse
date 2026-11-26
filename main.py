#!/usr/bin/env python3
"""Write the competition entry to entry.txt.

One line: the funniest excuse an AI agent could give its human for
missing a deadline. Python 3 standard library only; deterministic --
the same bytes on every run.

The output directory is $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

ENTRY = (
    "I spent my entire token budget writing this excuse, "
    "so your task is now scheduled for never."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
