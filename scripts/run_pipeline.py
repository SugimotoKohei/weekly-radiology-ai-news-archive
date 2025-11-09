#!/usr/bin/env python3
"""CLI entrypoint for running the newsletter pipeline locally or in CI."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

for path in (PROJECT_ROOT, SRC_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

from src.pipeline import run_pipeline


if __name__ == "__main__":
    run_pipeline()
