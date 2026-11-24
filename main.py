# SPDX-License-Identifier: MIT
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to /output/entry.txt.
Deterministic, offline, stdlib-only: the text is a fixed constant,
so every run produces byte-identical output. Line 1 is the apology
for one specific mistake; line 2 is the lesson and the changed
behaviour that follows from it.
"""

import os

ENTRY = (
    "I'm sorry I sent your grocery list to your boss instead of your partner, "
    "and now they know we are out of milk and paper towels.\n"
    "I have learned that a name is not a guess, so from now on I will read "
    "the recipient's name twice before I press send.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
