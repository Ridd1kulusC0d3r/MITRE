#!/usr/bin/env python3
"""build_catalog.py — atalho de compatibilidade para `python3 -m atlas`.

    python3 scripts/build_catalog.py          # = python3 -m atlas build
    python3 scripts/build_catalog.py --check  # = python3 -m atlas check && python3 -m atlas build --check
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from atlas.cli import main  # noqa: E402

if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(main(["check", "-q"]) or main(["build", "--check"]))
    sys.exit(main(["build"]))
