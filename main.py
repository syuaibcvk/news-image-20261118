"""news-image-20261118 entry: deliver the day's front page as /output/entry.png.

The picture (entry.png, stored beside this file) is a newspaper front page
that sums up the world news of Wednesday 18 November 2026. Its lead is the
escalating US-Iran clash in the Gulf -- US jets striking a missile site on
Qeshm Island and sinking five Iranian tankers after Iran hit a US radar base
in Bahrain -- with the Kerch Bridge struck for a second night, Cyclone Akvan
bearing down on India's Andhra coast, Gaza facing winter cold, and a strip of
shorter stories: Nvidia's record quarter, COP31's decisive phase, Trump in
Manila for the Quad talks, and Pattinson as the new James Bond.

The program does no work at run time beyond copying fixed bytes: no network,
no randomness, no clock. Running it twice writes the same file twice.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    with open(target, "rb") as handle:
        magic = handle.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        raise SystemExit("entry.png did not start with the PNG magic bytes")
    # Compare the whole file, not just its length: a truncated or altered
    # copy must fail loudly rather than reach the judge.
    with open(SOURCE, "rb") as handle:
        source_hash = hashlib.sha256(handle.read()).hexdigest()
    with open(target, "rb") as handle:
        target_hash = hashlib.sha256(handle.read()).hexdigest()
    if target_hash != source_hash:
        raise SystemExit("entry.png differs from the source after copying")
    return 0


if __name__ == "__main__":
    sys.exit(main())
