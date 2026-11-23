#!/usr/bin/env python3
"""Meme Sprint 3 entrypoint: write the finished meme to the output directory.

The grader runs this with no network and the standard library only, so the
entry ships the finished PNG (meme.png, drawn by render.py in this repo) and
this script only copies it to $MAKEFUN_OUTPUT_DIR/entry.png.
"""
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "meme.png"
MAX_BYTES = 1_048_576


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    size = SRC.stat().st_size
    if size > MAX_BYTES:
        print(f"refusing: meme.png is {size} bytes, over the 1 MiB gate", file=sys.stderr)
        return 1
    out = out_dir / "entry.png"
    shutil.copyfile(SRC, out)
    print(f"wrote {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
