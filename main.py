#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes one crypto-trading joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), validating the competition gate (1-200 characters,
UTF-8, not only whitespace, single line) before writing.
"""

import os
import sys

ENTRY = (
    "I sold my car for $8,000 to buy the dip. The dip is now worth "
    "less than the bus fare to the job I quit to trade full-time."
)


def validate(text: str) -> list:
    """Return a list of gate failures for *text* (empty = passes)."""
    problems = []
    if not (1 <= len(text) <= 200):
        problems.append(f"entry is {len(text)} characters (limit 200)")
    if not text.strip():
        problems.append("entry is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    return problems


def main() -> int:
    text = ENTRY
    problems = validate(text)
    if problems:
        for problem in problems:
            print(f"gate fail: {problem}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars, {len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
