#!/usr/bin/env python3
"""The Lake Library - a travel poster for a place that isn't there.

Writes the poster image bundled with this repository to /output/entry.png.
Standard library only; no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "poster.png")
OUTPUT = os.path.join("/output", "entry.png")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    print(f"wrote {OUTPUT} ({os.path.getsize(OUTPUT)} bytes)")


if __name__ == "__main__":
    main()
