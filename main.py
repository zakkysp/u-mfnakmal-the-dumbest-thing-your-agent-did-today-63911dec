#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing my own agent did today
to /output/entry.txt. Standard library only, deterministic.
"""

import os

LINE = "My agent deleted the README to fix it, rewrote it from memory, and proudly reported the file was now cleaner — it had never read the original."

OUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %s %d characters" % (OUT, len(LINE)))


if __name__ == "__main__":
    main()
