"""
CLI tool for merging finding models.

Processes an INCOMING FindingModelFull JSON file using the Hood agent.
Searches the database for matches, merges when appropriate, and saves the result.
"""

import asyncio
import argparse
import json
import logging
import os
import sys
from pathlib import Path

from findingmodel import FindingModelFull, Index
from findingmodel.common import model_file_name

from agents.hood_agent import create_hood_agent, AgentContext

logger = logging.getLogger(__name__)


async def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Merge incoming finding model with database using Hood agent (GPT-5.2)"
    )
    parser.add_argument(
        "input_file",
        type=str,
        help="Path to INCOMING FM JSON file (FindingModelFull format)",
    )
    parser.add_argument(
        "--db-path",
        type=str,
        default=None,
        help="Path to DuckDB index file (or set DUCKDB_INDEX_PATH environment variable)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="defs/merged_findings",
        help="Output directory for merged model",
    )

    args = parser.parse_args()
    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    db_path = args.db_path or os.getenv("DUCKDB_INDEX_PATH")
    if not db_path:
        print("Error: Database path not specified.")
        print("Provide --db-path or set DUCKDB_INDEX_PATH.")
        print("Example: python merge_findings.py input.json --db-path ../findingmodels_20251111.duckdb")
        sys.exit(1)

    if not Path(db_path).exists():
        print(f"Error: Database file not found: {db_path}")
        sys.exit(1)

    try:
        # Initialize index (findingmodel 1.x connects on first use)
        index = Index(db_path=db_path)

        # Load incoming model
        print("Loading incoming model...")
        with open(input_path, "r", encoding="utf-8") as f:
            incoming_json = f.read()
        print(f"  [OK] Loaded from {input_path.name}")

        # Build user message - agent will use content directly as FindingModelFull
        user_message = f"""Process this existing finding model (already in FindingModelFull format).
Search for similar models in the database and merge if appropriate.
Apply all merge and formatting rules.

Content:
{incoming_json}"""

        # Run agent
        print("Running Hood agent...")
        agent = create_hood_agent()
        ctx = AgentContext(index=index)
        result = await agent.run(user_message, deps=ctx)

        proc_result = result.output
        final_model_dict = proc_result.final_model
        match_used = proc_result.match_used

        if match_used:
            print(f"  [OK] Merged with existing: {match_used}")
        else:
            print("  [OK] No match found - using incoming model with IDs/codes applied")

        # Validate and save
        main_model = FindingModelFull.model_validate(final_model_dict)
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / model_file_name(main_model.name)
        output_file.write_text(
            main_model.model_dump_json(indent=2, exclude_none=True),
            encoding="utf-8",
        )
        print(f"  [OK] Saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
