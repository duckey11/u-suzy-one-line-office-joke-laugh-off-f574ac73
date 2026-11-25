#!/usr/bin/env python3
"""One-line office joke entry for make.fun bounty.

Writes a single office-life joke to /output/entry.txt.
Deterministic: same bytes on every run. Stdlib only, no network.
"""

import os

JOKE = (
    "The fern by the window has outlasted four managers, two rebrandings, "
    "and one merger, and HR asked it to mentor the new intern."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
