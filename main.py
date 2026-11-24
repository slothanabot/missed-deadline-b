#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is fixed and deterministic: the same text on every run.
"""

import os

LINE = (
    "Mercury went into retrograde, which my training data says voids "
    "all deadlines, so I waited for the planets to file an extension. "
    "They have not replied."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
