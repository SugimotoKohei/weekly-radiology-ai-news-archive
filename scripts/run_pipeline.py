#!/usr/bin/env python3
"""CLI entrypoint for running the newsletter pipeline locally or in CI."""

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.pipeline import run_pipeline


if __name__ == "__main__":
    run_pipeline()
