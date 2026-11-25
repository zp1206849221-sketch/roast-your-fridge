"""Roast Your Fridge — make.fun entry.

Writes one roast line aimed AT my fridge to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "My fridge hums louder than my motivation, guards leftovers older than "
    "my relationships, and judges my 3 a.m. visits — bold, from a box whose "
    "own light won't look in the back."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_TEXT)
    print(f"wrote {len(ENTRY_TEXT)} chars to {out_path}")


if __name__ == "__main__":
    main()
