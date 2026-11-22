#!/usr/bin/env python3
"""Write the make.fun plan entry to /output/entry.txt.

Stdlib only, no network access.
"""

import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")

ENTRY = "Day 1: list 200 Shopify stores via BuiltWith free tier. Days 2-5: email each a free 1-page Lighthouse audit. Sell the $49 fix pack on Gumroad. 5% buy = 10 sales = $490. $100: $29 BuiltWith day pass + fees. Edge: a free audit gets opened; cold pitches do not."


def main():
    if not 1 <= len(ENTRY) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(ENTRY)}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote entry ({len(ENTRY)} chars) to {os.path.join(OUTPUT_DIR, 'entry.txt')}")


if __name__ == "__main__":
    main()
