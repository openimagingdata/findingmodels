"""
Batch script to merge all findings in hood_findings directory.

Processes all .fm.json files in defs/hood_findings, skipping those already
in defs/merged_findings. Uses --auto-keep-existing for non-interactive mode.
Generates a summary report with processing statistics.
"""

import asyncio
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


def get_finding_name_from_file(file_path: Path) -> str:
    """Extract finding name from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('name', '')
    except Exception as e:
        print(f"  [WARN] Warning: Could not read {file_path}: {e}")
        return ''


def is_already_merged(finding_name: str, merged_dir: Path) -> bool:
    """Check if finding is already in merged_findings directory.
    
    Checks both:
    1. If a file exists with matching finding name
    2. If a merge report exists for this finding (in case it was merged into a different finding)
    """
    if not merged_dir.exists():
        return False
    
    # Check 1: Look for files with matching finding name
    for file_path in merged_dir.glob("*.fm.json"):
        try:
            merged_name = get_finding_name_from_file(file_path)
            if merged_name and merged_name.lower() == finding_name.lower():
                return True
        except Exception:
            continue
    
    # Check 2: Look for existing merge reports for this finding
    # Merge reports are named: merge_report_{safe_name}_{timestamp}.md
    # where safe_name is finding_name.lower().replace(' ', '_').replace('/', '_')
    safe_name = finding_name.lower().replace(' ', '_').replace('/', '_')
    report_dir = Path("merge_reports")
    if report_dir.exists():
        # Check if any merge report exists for this finding (ignore timestamp)
        pattern = f"merge_report_{safe_name}_*.md"
        existing_reports = list(report_dir.glob(pattern))
        if existing_reports:
            return True
    
    return False


def generate_batch_summary_report(
    processed_list: List[Dict[str, str]],
    failed_list: List[Dict[str, str]],
    skipped_list: List[Dict[str, str]],
    total_files: int,
    db_path: Path,
    output_dir: Path
) -> Path:
    """Generate a markdown summary report for the batch merge process."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = Path("merge_reports")
    report_dir.mkdir(exist_ok=True)
    report_path = report_dir / f"batch_merge_summary_{timestamp}.md"
    
    # Build markdown content
    lines = [
        "# Batch Merge Summary Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Database:** {db_path}",
        f"**Output Directory:** {output_dir}",
        "",
        "## Summary Statistics",
        "",
        f"- **Total Files Found:** {total_files}",
        f"- **✓ Successfully Processed:** {len(processed_list)}",
        f"- **⏭ Skipped (Already Merged):** {len(skipped_list)}",
        f"- **✗ Failed:** {len(failed_list)}",
        "",
    ]
    
    # Successfully processed findings
    if processed_list:
        lines.extend([
            "## ✓ Successfully Processed Findings",
            "",
            "| Finding Name | File |",
            "|---------------|------|",
        ])
        for item in sorted(processed_list, key=lambda x: x['name'].lower()):
            lines.append(f"| {item['name']} | `{item['file']}` |")
        lines.append("")
    else:
        lines.extend([
            "## ✓ Successfully Processed Findings",
            "",
            "*No findings were successfully processed.*",
            "",
        ])
    
    # Failed findings
    if failed_list:
        lines.extend([
            "## ✗ Failed Findings",
            "",
            "| Finding Name | File | Error |",
            "|---------------|------|-------|",
        ])
        for item in sorted(failed_list, key=lambda x: x['name'].lower()):
            error = item.get('error', 'Unknown error')
            lines.append(f"| {item['name']} | `{item['file']}` | {error} |")
        lines.append("")
    else:
        lines.extend([
            "## ✗ Failed Findings",
            "",
            "*No failures occurred.*",
            "",
        ])
    
    # Skipped findings
    if skipped_list:
        lines.extend([
            "## ⏭ Skipped Findings (Already Merged)",
            "",
            "| Finding Name | File |",
            "|---------------|------|",
        ])
        for item in sorted(skipped_list, key=lambda x: x['name'].lower()):
            lines.append(f"| {item['name']} | `{item['file']}` |")
        lines.append("")
    else:
        lines.extend([
            "## ⏭ Skipped Findings (Already Merged)",
            "",
            "*No findings were skipped.*",
            "",
        ])
    
    # Write report
    report_path.write_text('\n'.join(lines), encoding='utf-8')
    return report_path


async def merge_finding(input_file: Path, db_path: Path) -> Dict[str, Any]:
    """Run merge_findings.py on a single finding file.
    
    Returns:
        Dict with keys: 'success' (bool), 'error' (str or None), 'output' (str)
    """
    script_path = Path(__file__).parent / "merge_findings.py"
    
    cmd = [
        sys.executable,
        "-u",  # Unbuffered output for real-time streaming
        str(script_path),
        str(input_file),
        "--db-path", str(db_path),
        "--auto-keep-existing"
    ]
    
    try:
        # Use Popen for real-time output streaming
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Combine stderr into stdout
            text=True,
            bufsize=1,  # Line buffered
            universal_newlines=True
        )
        
        # Stream output in real-time and collect it for error detection
        output_lines = []
        for line in process.stdout:
            # Print immediately
            print(line, end='', flush=True)
            # Also collect for error detection
            output_lines.append(line)
        
        process.wait()
        result_code = process.returncode
        output_text = ''.join(output_lines)
        
        # Check for validation errors in output even if exit code is 0
        has_error = (
            result_code != 0 or
            "Error: Failed to validate" in output_text or
            "Error: Failed to save model" in output_text or
            "[ERROR] Error:" in output_text
        )
        
        if has_error:
            # Extract error message
            error_msg = "Unknown error"
            if "Failed to validate" in output_text:
                error_msg = "Validation error"
            elif "Failed to save model" in output_text:
                error_msg = "Failed to save model"
            elif "Error:" in output_text:
                for line in output_lines:
                    if "Error:" in line:
                        error_msg = line.strip()
                        break
            
            return {
                'success': False,
                'error': error_msg,
                'output': output_text,
                'stderr': None
            }
        
        return {
            'success': True,
            'error': None,
            'output': output_text,
            'stderr': None
        }
    except subprocess.CalledProcessError as e:
        print(f"  [ERROR] Error processing {input_file.name}:")
        print(e.stdout)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        
        # Extract error message from output
        error_msg = "Unknown error"
        if e.stdout:
            # Look for common error patterns
            if "Failed to validate" in e.stdout:
                error_msg = "Validation error"
            elif "Failed to save model" in e.stdout:
                error_msg = "Failed to save model"
            elif "Error:" in e.stdout:
                # Try to extract the error line
                for line in e.stdout.split('\n'):
                    if "Error:" in line:
                        error_msg = line.strip()
                        break
            else:
                error_msg = "Processing failed"
        
        return {
            'success': False,
            'error': error_msg,
            'output': e.stdout,
            'stderr': e.stderr if e.stderr else None
        }


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
    
    # Track detailed statistics
    processed_list: List[Dict[str, str]] = []
    failed_list: List[Dict[str, str]] = []
    skipped_list: List[Dict[str, str]] = []
    
    total_files = len(finding_files)
    current_file_num = 0
    
    for finding_file in finding_files:
        current_file_num += 1
        finding_name = get_finding_name_from_file(finding_file)
        if not finding_name:
            finding_name = finding_file.stem
        
        print(f"\n{'='*80}")
        print(f"[{current_file_num}/{total_files}] Processing: {finding_name} ({finding_file.name})")
        print(f"{'='*80}")
        
        # Check if already merged
        if is_already_merged(finding_name, merged_findings_dir):
            print(f"  [SKIP] Skipping (already in merged_findings)")
            skipped_list.append({
                'name': finding_name,
                'file': finding_file.name
            })
            continue
        
        # Process the finding
        result = await merge_finding(finding_file, db_path)
        if result['success']:
            processed_list.append({
                'name': finding_name,
                'file': finding_file.name
            })
            print(f"  [OK] Successfully processed {finding_name}")
        else:
            failed_list.append({
                'name': finding_name,
                'file': finding_file.name,
                'error': result['error']
            })
            print(f"  [ERROR] Failed to process {finding_name}")
    
    # Generate summary report
    report_path = generate_batch_summary_report(
        processed_list=processed_list,
        failed_list=failed_list,
        skipped_list=skipped_list,
        total_files=len(finding_files),
        db_path=db_path,
        output_dir=merged_findings_dir
    )
    
    # Console summary
    print(f"\n{'='*80}")
    print("BATCH PROCESSING SUMMARY")
    print(f"{'='*80}")
    print(f"Total files: {len(finding_files)}")
    print(f"  [OK] Processed: {len(processed_list)}")
    print(f"  [SKIP] Skipped (already merged): {len(skipped_list)}")
    print(f"  [ERROR] Failed: {len(failed_list)}")
    print(f"{'='*80}")
    print(f"\n[REPORT] Detailed summary report saved to: {report_path}\n")


if __name__ == "__main__":
    asyncio.run(main())

