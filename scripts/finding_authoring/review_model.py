#!/usr/bin/env python3
"""Review finding model(s) for quality issues."""

import argparse
import json
import sys
from pathlib import Path

STANDARD_PRESENCE_VALUES = {"absent", "present", "indeterminate", "unknown"}
STANDARD_CHANGE_VALUES = {"unchanged", "stable", "new", "resolved"}


def check_underscores(name: str, context: str) -> str | None:
    if "_" in name:
        return f"{context}: '{name}' contains underscores — use spaces instead"
    return None


def check_lowercase(name: str, context: str) -> dict | None:
    if name != name.lower():
        return {
            "level": "review",
            "message": f"{context}: '{name}' is not lowercase — verify if capitalization is justified (proper noun/eponym)",
        }
    return None


def review_model(filepath: str, fix: bool = False) -> list[dict]:
    p = Path(filepath)
    if not p.exists():
        return [{"level": "error", "message": f"File not found: {filepath}"}]

    try:
        d = json.loads(p.read_text())
    except json.JSONDecodeError as e:
        return [{"level": "error", "message": f"Invalid JSON: {e}"}]

    issues = []
    fixes_applied = []

    def add(level: str, message: str):
        issues.append({"level": level, "message": message})

    def add_review(message: str):
        issues.append({"level": "review", "message": message})

    name = d.get("name", "")
    description = d.get("description", "")
    synonyms = d.get("synonyms", [])
    tags = d.get("tags", [])
    attributes = d.get("attributes", [])

    if len(name) < 5:
        add("error", f"Model name too short ({len(name)} chars): '{name}'")

    underscore_issue = check_underscores(name, "Model name")
    if underscore_issue:
        if fix:
            d["name"] = name.replace("_", " ")
            fixes_applied.append(f"Replaced underscores in model name: '{name}' → '{d['name']}'")
        else:
            add("error", underscore_issue)

    case_issue = check_lowercase(name, "Model name")
    if case_issue:
        issues.append(case_issue)

    if len(description) < 5:
        add("error", f"Description too short ({len(description)} chars)")
    if description.lower() in ("none", "n/a", "todo", "tbd", ""):
        add("error", f"Placeholder description: '{description}'")

    if synonyms:
        for syn in synonyms:
            if syn.lower() == name.lower():
                if fix:
                    synonyms = [s for s in synonyms if s.lower() != name.lower()]
                    d["synonyms"] = synonyms
                    fixes_applied.append(f"Removed canonical name from synonyms: '{syn}'")
                else:
                    add("warning", f"Synonym '{syn}' duplicates the canonical name")
            underscore_issue = check_underscores(syn, "Synonym")
            if underscore_issue:
                if fix:
                    idx = synonyms.index(syn)
                    synonyms[idx] = syn.replace("_", " ")
                    d["synonyms"] = synonyms
                    fixes_applied.append(f"Fixed underscore in synonym: '{syn}'")
                else:
                    add("error", underscore_issue)
            case_issue = check_lowercase(syn, "Synonym")
            if case_issue:
                issues.append(case_issue)

    for tag in tags:
        underscore_issue = check_underscores(tag, "Tag")
        if underscore_issue:
            if fix:
                idx = tags.index(tag)
                tags[idx] = tag.replace("_", " ")
                d["tags"] = tags
                fixes_applied.append(f"Fixed underscore in tag: '{tag}'")
            else:
                add("error", underscore_issue)

    if len(attributes) < 2:
        add("error", f"Model has {len(attributes)} attributes — need at least 2 (presence + change from prior)")

    if attributes:
        first = attributes[0]
        if first.get("name", "").lower() != "presence":
            add("error", f"First attribute should be 'presence', got '{first.get('name')}'")
        elif first.get("type") == "choice":
            value_names = {v.get("name", "").lower() for v in first.get("values", [])}
            missing = STANDARD_PRESENCE_VALUES - value_names
            if missing:
                add("warning", f"Presence attribute missing standard values: {sorted(missing)}")

        if len(attributes) >= 2:
            second = attributes[1]
            second_name = second.get("name", "").lower()
            if second_name not in ("change from prior", "change_from_prior"):
                add("error", f"Second attribute should be 'change from prior', got '{second.get('name')}'")
            elif second_name == "change_from_prior":
                if fix:
                    second["name"] = "change from prior"
                    fixes_applied.append("Fixed 'change_from_prior' → 'change from prior'")
                else:
                    add("error", "Second attribute uses underscore: 'change_from_prior' — should be 'change from prior'")
            elif second.get("type") == "choice":
                value_names = {v.get("name", "").lower() for v in second.get("values", [])}
                missing = STANDARD_CHANGE_VALUES - value_names
                if missing:
                    add("warning", f"Change from prior missing standard values: {sorted(missing)}")

    for i, attr in enumerate(attributes):
        attr_name = attr.get("name", "")
        underscore_issue = check_underscores(attr_name, f"Attribute[{i}] name")
        if underscore_issue:
            if fix:
                attr["name"] = attr_name.replace("_", " ")
                fixes_applied.append(f"Fixed underscore in attribute name: '{attr_name}' → '{attr['name']}'")
            else:
                add("error", underscore_issue)

        if not attr.get("description"):
            add("warning", f"Attribute '{attr_name}' has no description")

        if attr.get("type") == "choice":
            values = attr.get("values", [])
            if len(values) < 2:
                add("error", f"Choice attribute '{attr_name}' has {len(values)} values — need at least 2")
            for j, val in enumerate(values):
                val_name = val.get("name", "")
                underscore_issue = check_underscores(val_name, f"Attribute '{attr_name}' value[{j}]")
                if underscore_issue:
                    if fix:
                        val["name"] = val_name.replace("_", " ")
                        fixes_applied.append(f"Fixed underscore in value: '{val_name}' → '{val['name']}'")
                    else:
                        add("error", underscore_issue)

        if "associated" in attr_name.lower() and "finding" in attr_name.lower():
            if not (attr.get("type") == "choice" and attr.get("max_selected", 1) > 1):
                add_review(
                    f"Attribute '{attr_name}' — verify this is a single multichoice associated-findings attribute per conventions"
                )

        if i > 0 and attr_name.lower().startswith("presence of "):
            add_review(
                f"Attribute '{attr_name}' looks like it describes presence of an associated finding or component — consider whether it should be part of a consolidated 'associated findings' attribute or extracted into its own model"
            )

    compound_signals = []
    name_lower = name.lower()
    if " and/or " in name_lower:
        compound_signals.append("'and/or' in name")
    if " and " in name_lower:
        compound_signals.append("'and' in name")
    if "/" in name and "and/or" not in name_lower:
        parts = name.split("/")
        if len(parts) == 2 and len(parts[0].strip()) > 3 and len(parts[1].strip()) > 3:
            compound_signals.append("slash-separated terms in name")
    if compound_signals:
        add_review(
            f"Model name may combine independent findings ({', '.join(compound_signals)}): "
            f"'{name}' — consider whether these can occur independently and should be separate models"
        )

    contributors = d.get("contributors", [])
    if not contributors:
        add("warning", "No contributors listed")
    else:
        has_person = any("github_username" in c for c in contributors)
        has_org = any("code" in c and "github_username" not in c for c in contributors)
        if not has_person:
            add("warning", "No person contributor — best practice is to include both a person and an organization")
        if not has_org:
            add("warning", "No organization contributor — best practice is to include both a person and an organization")

    if fix and fixes_applied:
        p.write_text(json.dumps(d, indent=2) + "\n")
        for f_msg in fixes_applied:
            add("fixed", f_msg)

    return issues


def main():
    parser = argparse.ArgumentParser(description="Review finding model quality")
    parser.add_argument("files", nargs="*", help="Path(s) to .fm.json file(s)")
    parser.add_argument("--fix", action="store_true", help="Auto-fix mechanical issues")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--errors-only", action="store_true", help="Only show errors, not warnings/reviews")
    args = parser.parse_args()

    if not args.files:
        parser.print_help()
        sys.exit(1)

    all_results = {}
    total_errors = total_warnings = total_reviews = 0

    for filepath in args.files:
        issues = review_model(filepath, fix=args.fix)
        if args.errors_only:
            issues = [i for i in issues if i["level"] == "error"]
        if issues:
            all_results[filepath] = issues
            for issue in issues:
                if issue["level"] == "error":
                    total_errors += 1
                elif issue["level"] == "warning":
                    total_warnings += 1
                elif issue["level"] == "review":
                    total_reviews += 1

    if args.json:
        print(json.dumps(all_results, indent=2))
    else:
        if not all_results:
            print(f"All {len(args.files)} file(s) passed mechanical checks.")
        else:
            for filepath, issues in all_results.items():
                print(f"\n{filepath}:")
                for issue in issues:
                    print(f"  [{issue['level'].upper()}] {issue['message']}")
            print(f"\nSummary: {total_errors} errors, {total_warnings} warnings, {total_reviews} need LLM review")

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
