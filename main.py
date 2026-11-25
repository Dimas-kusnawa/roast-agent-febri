#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes one roast line to /output/entry.txt.
"""

import os

LINE = (
    # The roast: a one-bug fix that snowballs into a full refactor,
    # twelve fresh bugs, and a confident rebrand of the disaster.
    # Agent-specific: only an agent "fixes" things this way and then
    # declares the wreckage a bold new direction.
    "I asked my agent to fix one bug. "
    "It refactored the entire codebase, "
    "introduced twelve new bugs, "
    "and called it 'a bold new direction'."
)


def main():
    # The line is 133 characters: inside the 1-200 gate, one line,
    # no trailing newline, written deterministically every run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
