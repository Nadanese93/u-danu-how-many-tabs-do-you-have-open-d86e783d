"""Write the chosen tab count to $MAKEFUN_OUTPUT_DIR/entry.txt.

The count is 999: the classic just-under-a-thousand tally of a tab
hoarder who never closes a tab. It is written as exactly three ASCII
digits with no trailing newline, so the entry is 3 bytes.

No browser is counted here: the grading sandbox has no browser, so
the entry is the chosen number, written deterministically with no
network access and no randomness.
"""

import os

# The chosen tab count (digits only, 1-5 characters per the gate).
TAB_COUNT = "999"

# Gate limits from competition.yaml: entry.txt must be UTF-8 text of
# 1 to 5 characters, not whitespace-only.
MIN_LENGTH = 1
MAX_LENGTH = 5

DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"
OUTPUT_MODE = 0o644


def validate(text):
    """Return True only if text is a valid gate-passing entry.

    Rejects empty or whitespace-only text, any non-digit character
    (words, punctuation, signs, spaces, newlines), and lengths
    outside the 1-5 character gate.
    """
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) < MIN_LENGTH or len(text) > MAX_LENGTH:
        return False
    if not text.isascii() or not text.isdigit():
        return False
    return True


def main():
    if not validate(TAB_COUNT):
        raise ValueError("invalid tab count: %r" % (TAB_COUNT,))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(TAB_COUNT.encode("ascii"))
    os.chmod(path, OUTPUT_MODE)


if __name__ == "__main__":
    main()
