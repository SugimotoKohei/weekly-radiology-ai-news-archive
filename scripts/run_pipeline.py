#!/usr/bin/env python3
"""CLI entrypoint for running the newsletter pipeline locally or in CI."""

import argparse
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

for path in (PROJECT_ROOT, SRC_DIR):
    path_str = str(path)
    if path_str not in sys.path:
        sys.path.insert(0, path_str)

from src.pipeline import run_dry_run, run_pipeline


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the newsletter pipeline.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without external API calls (uses fixture papers and writes a _dry_run markdown).",
    )
    parser.add_argument(
        "--fixture",
        default="tests/fixtures/pubmed_sample.xml",
        help="Path to a PubMed XML fixture (only used with --dry-run).",
    )
    args = parser.parse_args()

    if args.dry_run:
        run_dry_run(fixture_path=Path(args.fixture))
    else:
        run_pipeline()
