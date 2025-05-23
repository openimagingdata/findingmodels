#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
"""
Example usage of the process_gamuts.py script.

This script demonstrates how to process different Gamuts.net pages
and save them to appropriately named JSONL files.
"""

import subprocess
import sys
from pathlib import Path

# Common Gamuts.net URLs and their corresponding output files
GAMUT_CONFIGS = [
    {"url": "https://www.gamuts.net/s/vi", "output": "data/chest_gamuts.jsonl", "description": "Chest/Thoracic gamuts"},
    {"url": "https://www.gamuts.net/s/gi", "output": "data/gi_gamuts.jsonl", "description": "Gastrointestinal gamuts"},
    {"url": "https://www.gamuts.net/s/gu", "output": "data/gu_gamuts.jsonl", "description": "Genitourinary gamuts"},
    {"url": "https://www.gamuts.net/s/hn", "output": "data/hn_gamuts.jsonl", "description": "Head & Neck gamuts"},
]


def run_process_gamuts(url: str, output: str, description: str) -> bool:
    """
    Run the process_gamuts.py script for a given URL.

    Args:
        url: The Gamuts.net URL to process
        output: The output file path
        description: Description for logging

    Returns:
        True if successful, False otherwise
    """
    print(f"\n{'=' * 60}")
    print(f"Processing: {description}")
    print(f"URL: {url}")
    print(f"Output: {output}")
    print(f"{'=' * 60}")

    try:
        # Ensure output directory exists
        Path(output).parent.mkdir(parents=True, exist_ok=True)

        # Run the script
        result = subprocess.run(
            ["uv", "run", "process_gamuts.py", url, "--output", output, "--chunk-size", "20"],
            check=True,
            capture_output=True,
            text=True,
        )

        print("✅ Success!")
        print(result.stdout)
        return True

    except subprocess.CalledProcessError as e:
        print("❌ Failed!")
        print(f"Error: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main() -> None:
    """Process all configured Gamuts.net URLs."""
    print("Gamuts.net Processing Example")
    print("This script will process multiple Gamuts.net pages and save them as JSON files.")

    # Check if we're in the right directory
    if not Path("process_gamuts.py").exists():
        print("❌ Error: process_gamuts.py not found in current directory.")
        print("Please run this script from the scripts/ directory.")
        sys.exit(1)

    successful = 0
    total = len(GAMUT_CONFIGS)

    for config in GAMUT_CONFIGS:
        if run_process_gamuts(**config):
            successful += 1

    print(f"\n{'=' * 60}")
    print("Processing Complete!")
    print(f"Successful: {successful}/{total}")

    if successful == total:
        print("🎉 All gamuts processed successfully!")
    else:
        print(f"⚠️  {total - successful} gamuts failed to process.")

    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
