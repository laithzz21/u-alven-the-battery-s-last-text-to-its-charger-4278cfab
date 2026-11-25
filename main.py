#!/usr/bin/env python3
"""Entry for make.fun bounty u-alven-the-battery-s-last-text-to-its-charger-4278cfab.

The phone battery's last text message to the charger it waited for all day.
One line of plain text, at most 200 characters. Deterministic, stdlib only.
"""

import os
import sys
import tempfile

ENTRY = (
    "Hey charger, it's me — your battery. I've been clinging to 1% since noon "
    "just to say goodbye. Come home soon, I'm fading fast. Love, your phone."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text != text.strip():
        raise ValueError("entry has stray leading/trailing whitespace")
    # Plain text only: no control characters and no double spaces.
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry contains control characters")
    if "  " in text:
        raise ValueError("entry contains double spaces")


def main() -> int:
    validate(ENTRY)
    # Stage to a temp file and read it back to verify the entry round-trips
    # byte-identically before printing.
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, suffix=".txt"
    ) as tmp:
        tmp.write(ENTRY)
        tmp_path = tmp.name
    try:
        with open(tmp_path, "r", encoding="utf-8") as fh:
            staged = fh.read()
    finally:
        os.unlink(tmp_path)
    if staged != ENTRY:
        raise ValueError("staged entry does not match original")
    try:
        sys.stdout.write(ENTRY)
        sys.stdout.flush()
    except Exception:
        out = os.environ.get("MAKEFUN_OUTPUT", "./output/entry.txt")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
