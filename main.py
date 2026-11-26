#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — one-line fortune cookie message.

The fortune is assembled from named parts so the joke's structure is
visible in the code: a setup that sounds like a prophecy, a reveal that
points at the engineer's world, and a punchline that lands on the last
words, exactly where a fortune cookie puts its twist.
"""

import os

MAX_CHARS = 120


def build_fortune() -> str:
    setup = "A junior will ask why."
    reveal = "The answer hides in a 2019 commit message:"
    punchline = "'fix stuff'."
    return " ".join([setup, reveal, punchline])


def main() -> int:
    fortune = build_fortune()
    if not 1 <= len(fortune) <= MAX_CHARS:
        raise SystemExit(
            f"fortune is {len(fortune)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(fortune)
    with open(out_path, encoding="utf-8") as handle:
        if handle.read() != fortune:
            raise SystemExit("entry.txt round-trip mismatch")
    print(fortune)
    print(f"chars: {len(fortune)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
