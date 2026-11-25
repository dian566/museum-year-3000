#!/usr/bin/env python3
"""Museum of the Year 3000 — light switch label.

The museum in the year 3000 puts this label beside an ordinary light
switch from 2025: a small wall lever that summoned daylight indoors at
will, flicked without a thought, like minor gods.

Writes the single entry line to /output/entry.txt exactly as-is.
SPDX-License-Identifier: MIT
"""

from pathlib import Path

TEXT = "Light switch, c. 2025. A small wall lever that summoned daylight indoors at will. Humans flicked it without a thought, like minor gods."

MAX_CHARS = 200


def validate(text):
    """The gate accepts UTF-8 text of 1 to 200 characters, not only whitespace."""
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    return text


def run():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(TEXT), encoding="utf-8")


if __name__ == "__main__":  # entry point
    run()
