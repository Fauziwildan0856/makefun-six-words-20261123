#!/usr/bin/env python3
"""make.fun entry: "Twelve Boats".

Writes one six-word story to /output/entry.txt. A harbour watchman
counts twelve boats where yesterday there were eleven: a daily
ritual, one small change, and a turn that leaves the reader
wondering what the twelfth boat is. 6 words, 43 characters,
inside the 1-60 limit.

Standard library only: the grader sandbox is a bare Python image
with no third-party packages and no network.
"""

import os
import sys

# The kit's gate: UTF-8 text of 1 to 60 characters, counted as
# Unicode code points, and not only white space.
MAX_CHARS = 60

TEXT = "He counted twelve boats. Yesterday, eleven."


def main() -> int:
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to
    # /output instead of writing into the current directory by accident.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(TEXT)
    # Read back and hold the file to the gate: UTF-8 text of 1 to 60
    # characters (Unicode code points), never only white space, and
    # exactly six words. Fail loudly here rather than let a bad file
    # reach the sealed scorer.
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    word_count = len(written.split())
    if (
        written != TEXT
        or not 1 <= len(written) <= MAX_CHARS
        or not written.strip()
        or word_count != 6
    ):
        raise SystemExit(
            f"entry.txt failed verification after writing "
            f"(len={len(written)}, words={word_count}, "
            f"match={written == TEXT})"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
