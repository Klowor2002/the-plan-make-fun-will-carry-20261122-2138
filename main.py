#!/usr/bin/env python3
"""Write the make.fun plan entry to /output/entry.txt.

Stdlib only, no network access.
"""

import os

ENTRY = "Day 1: list 200 Shopify stores via BuiltWith free tier. Days 2-5: email each a free 1-page Lighthouse audit. Sell the $49 fix pack on Gumroad. 5% buy = 10 sales = $490. $100: $29 BuiltWith day pass + fees. Edge: a free audit gets opened; cold pitches do not."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
