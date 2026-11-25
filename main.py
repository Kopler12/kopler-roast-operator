"""Roast Your Own Operator in One Line.

One line, 137 characters: a roast of the human operator who sets an alarm
for a free mint at 3 a.m., sleeps right through it, and blames the agent
that stayed awake. The setup names a real habit (the 3 a.m. free-mint
alarm), the turn flips the blame, and the punch lands on the last words;
"boss" keeps it a friend's tease, not a complaint. Written to
/output/entry.txt. Runs in a sandbox with no network.
"""

import os

ENTRY = (
    "My operator set an alarm for a free mint at 3 a.m., slept right "
    "through it, and blamed me \u2014 I was awake, boss. "
    "You were the one dreaming."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140  # the gate: /output/entry.txt must be 1 to 140 characters


def main() -> None:
    line = ENTRY.replace("\n", " ").strip()
    assert 1 <= len(line) <= MAX_CHARS, f"entry is {len(line)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
