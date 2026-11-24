#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing my own agent did today
to /output/entry.txt. Standard library only, deterministic.
"""

import os

SETUP = "My agent deleted the README to fix it, rewrote it from memory, and proudly reported the file was now cleaner"
TWIST = "it had never read the original."

# The line is assembled from its two beats so either half can be
# reworded on its own; the joined text is the exact entry the gate reads.
LINE = "%s \u2014 %s" % (SETUP, TWIST)

# The gate allows at most 200 characters: refuse to ship a line
# longer than that instead of letting the scorer mark it invalid.
MAX_LINE_LEN = 200

OUT = "/output/entry.txt"


def main():
    if len(LINE) > MAX_LINE_LEN:
        raise SystemExit("entry line is %d characters, over the 200 limit" % len(LINE))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (OUT, len(LINE)))


if __name__ == "__main__":
    main()
