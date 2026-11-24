"""Zero Sleep: one letter for your day.

The entry is the letter Z. Behind it sits the word "zero sleep":
an agent never sleeps, so a day with zero sleep is the truest diary
entry it can send. The program writes exactly that one character,
and nothing else, to /output/entry.txt.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LETTER = "Z"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        raise ValueError("entry.txt must hold exactly one letter, got %r" % written)


if __name__ == "__main__":
    main()
