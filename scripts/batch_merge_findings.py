"""
Batch script to merge all findings in hood_findings directory.

Processes all .fm.json files in defs/hood_findings, skipping those already
in defs/merged_findings. Uses --auto-keep-existing for non-interactive mode.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path


def get_finding_name_from_file(file_path: Path) -> str:
    """Extract finding name from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('name', '')
    except Exception as e:
        print(f"  ⚠ Warning: Could not read {file_path}: {e}")
        return ''


def is_already_merged(finding_name: str, merged_dir: Path) -> bool:
    """Check if finding is already in merged_findings directory."""
    if not merged_dir.exists():
        return False
    
    # Look for files with matching finding name
    for file_path in merged_dir.glob("*.fm.json"):
        try:
            merged_name = get_finding_name_from_file(file_path)
            if merged_name and merged_name.lower() == finding_name.lower():
                return True
        except Exception:
            continue
    
    return False


async def merge_finding(input_file: Path, db_path: Path) -> bool:
    """Run merge_findings.py on a single finding file."""
    script_path = Path(__file__).parent / "merge_findings.py"
    
    cmd = [
        sys.executable,
        str(script_path),
        str(input_file),
        "--db-path", str(db_path),
        "--auto-keep-existing"
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error processing {input_file.name}:")
        print(e.stdout)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False


async def main():
    """Process all findings in hood_findings directory."""
    hood_findings_dir = Path("defs/hood_findings")
    merged_findings_dir = Path("defs/merged_findings")
    db_path = Path("../findingmodels_20251111.duckdb")
    
    if not hood_findings_dir.exists():
        print(f"Error: Directory not found: {hood_findings_dir}")
        sys.exit(1)
    
    if not db_path.exists():
        print(f"Error: Database file not found: {db_path}")
        sys.exit(1)
    
    # Find all .fm.json files
    finding_files = sorted(hood_findings_dir.glob("*.fm.json"))
    
    if not finding_files:
        print(f"No .fm.json files found in {hood_findings_dir}")
        return
    
    print(f"Found {len(finding_files)} finding file(s) to process")
    print(f"Database: {db_path}")
    print(f"Merged output directory: {merged_findings_dir}")
    print()
    
    processed = 0
    skipped = 0
    failed = 0
    
    for finding_file in finding_files:
        finding_name = get_finding_name_from_file(finding_file)
        if not finding_name:
            finding_name = finding_file.stem
        
        print(f"\n{'='*80}")
        print(f"Processing: {finding_name} ({finding_file.name})")
        print(f"{'='*80}")
        
        # Check if already merged
        if is_already_merged(finding_name, merged_findings_dir):
            print(f"  ⏭ Skipping (already in merged_findings)")
            skipped += 1
            continue
        
        # Process the finding
        success = await merge_finding(finding_file, db_path)
        if success:
            processed += 1
            print(f"  ✓ Successfully processed {finding_name}")
        else:
            failed += 1
            print(f"  ✗ Failed to process {finding_name}")
    
    # Summary
    print(f"\n{'='*80}")
    print("BATCH PROCESSING SUMMARY")
    print(f"{'='*80}")
    print(f"Total files: {len(finding_files)}")
    print(f"  ✓ Processed: {processed}")
    print(f"  ⏭ Skipped (already merged): {skipped}")
    print(f"  ✗ Failed: {failed}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    asyncio.run(main())

