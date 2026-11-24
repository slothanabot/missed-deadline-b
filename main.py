#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is fixed and deterministic: the same text on every run.
"""

import os

MAX_CHARS = 200


def build_line():
    """Compose the excuse from its setup and its punchline.

    Setup: the deadline was kept somewhere safe inside the agent.
    Punchline: the agent's own context window threw it out to make
    room for the very excuse being read. Deadpan throughout.
    """
    setup = "I kept the deadline in my context window for safekeeping, "
    punchline = (
        "but the window filled up and evicted it to make room "
        "for this very excuse."
    )
    return setup + punchline


def main():
    line = build_line()
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"excuse must be 1-{MAX_CHARS} chars, got {len(line)}")
    if not line.strip():
        raise ValueError("excuse must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
