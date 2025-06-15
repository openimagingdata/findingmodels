#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx>=0.24.0",
#     "openai>=1.0.0",
#     "python-dotenv>=1.0.0",
#     "pydantic>=2.0.0",
# ]
# ///
"""
Script to process Gamuts.net pages and convert them to structured JSONL files.

This script takes a URL from Gamuts.net, scrapes the medical terms from the page,
uses OpenAI's API to categorize and structure the terms, and saves the results
to a JSONL file with one categorized term per line.

Usage:
    uv run process_gamuts.py <url> [--output output.jsonl] [--chunk-size 20]

Example:
    uv run process_gamuts.py "https://www.gamuts.net/s/vi" --output chest_gamuts.jsonl
"""

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

import httpx
import openai
from dotenv import load_dotenv
from pydantic import BaseModel, Field


@dataclass(frozen=True)
class Gamut:
    """Represents a gamut term with ID and name."""

    id: str
    name: str


class CategorizedTerm(BaseModel):
    """Pydantic model for a categorized medical term."""

    gamuts_id: str = Field(description="The original Gamuts.net ID for the term")
    name: str = Field(description="The name of the medical term")
    seen_on_modalities: List[str] = Field(
        description="Imaging modalities where this finding is typically seen",
        examples=[["CT", "XR", "MR", "US"]],
    )
    description: str = Field(description="Brief description of the term (sentence or fragment)")
    synonyms: List[str] = Field(
        description="Alternative names, abbreviations, or acronyms for the term",
        default_factory=list,
    )
    category: str = Field(
        description="Primary category: 'finding' or 'diagnosis'",
        pattern="^(finding|diagnosis)$",
    )
    subcategories: List[str] = Field(
        description="Additional categorizations like anatomical location, process type",
        examples=[["mediastinum", "inflammatory", "neoplastic", "congenital anomaly"]],
    )
    radiologist_comments: bool = Field(
        description="Whether radiologists would typically comment on this in reports",
        default=True,
    )


class TermCategorizationResponse(BaseModel):
    """Response model containing all categorized terms."""

    categorized_terms: List[CategorizedTerm] = Field(description="List of categorized medical terms")


def load_gamuts(url: str) -> List[Gamut]:
    """
    Load gamut terms from a Gamuts.net URL.

    Args:
        url: The URL to scrape gamut terms from

    Returns:
        List of Gamut objects extracted from the page

    Raises:
        AssertionError: If the HTTP request fails
    """
    gamuts = []
    response = httpx.get(url)
    assert response.status_code == 200, f"Failed to retrieve URL: {url}"

    counter = 0
    for line in response.text.splitlines():
        counter += 1
        line = line.strip()
        if line.startswith('<a href="/display.php?id='):
            parts = line.split('">')
            id_part = parts[0].split("id=")[1]
            name_part = parts[1].split("</a>")[0]
            gamuts.append(Gamut(id=id_part, name=name_part))

    print(f"Loaded {len(gamuts)} gamuts from {url} (checked {counter} lines)")
    return gamuts


def generate_prompt(terms: List[Gamut]) -> List[dict[str, str]]:
    """
    Generate the prompt for OpenAI API to categorize gamut terms.

    Args:
        terms: List of Gamut objects to categorize

    Returns:
        List of message dictionaries for the OpenAI API
    """
    system_prompt = """
You are a medical informatics expert specializing in radiology. 
Your task is to analyze terms described on medical imaging and categorize them
to allow them to be used as identifiers for terms seen in radiology reports.
"""

    user_prompt = f"""
You will be given a list of medical terms and IDs from Gamuts.net. Your task is to categorize each term according to whether it represents a finding or diagnosis. 

For each term, provide:
- A brief description (sentence or fragment)
- Synonyms, abbreviations, or acronyms commonly used
- Primary category: "finding" or "diagnosis" 
- Subcategories like anatomical location (e.g., "mediastinum", "pleura", "lung") and process type (e.g., "inflammatory", "neoplastic", "congenital anomaly", "postop", "device")
- Whether radiologists would typically comment on this in reports
- Which imaging modalities it would be seen on: "CT", "XR", "MR", "US"

Terms to categorize:
{chr(10).join([f"{gamut.name} (ID: {gamut.id})" for gamut in terms])}
"""

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def categorize_terms(terms: List[Gamut], llm: openai.OpenAI) -> List[CategorizedTerm]:
    """
    Use OpenAI API to categorize a list of gamut terms using structured outputs.

    Args:
        terms: List of Gamut objects to categorize
        llm: OpenAI client instance

    Returns:
        List of CategorizedTerm Pydantic objects

    Raises:
        ValueError: If no valid response from the model
    """
    response = llm.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=generate_prompt(terms),  # type: ignore
        response_format=TermCategorizationResponse,
    )

    if not response.choices or not response.choices[0].message:
        raise ValueError("No valid response from the model.")

    parsed_response = response.choices[0].message.parsed
    if parsed_response is None:
        raise ValueError("No parsed content in the response from the model.")

    return parsed_response.categorized_terms


def process_gamuts_url(url: str, output_file: str, chunk_size: int = 20) -> None:
    """
    Process a Gamuts.net URL and save the categorized results to a JSONL file.

    Args:
        url: The Gamuts.net URL to process
        output_file: Path to save the output JSONL file
        chunk_size: Number of terms to process in each API call
    """
    # Load environment variables
    load_dotenv()

    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    # Initialize OpenAI client
    llm = openai.OpenAI()

    # Load gamuts from the URL
    print(f"Loading gamuts from: {url}")
    gamuts = load_gamuts(url)

    if not gamuts:
        print("No gamuts found at the provided URL.")
        return

    # Process gamuts in chunks
    all_categorized_gamuts = []
    total_chunks = (len(gamuts) + chunk_size - 1) // chunk_size

    for i in range(0, len(gamuts), chunk_size):
        chunk_num = (i // chunk_size) + 1
        print(
            f"Processing chunk {chunk_num}/{total_chunks}: gamuts {i} to {min(i + chunk_size, len(gamuts))} of {len(gamuts)}"
        )

        chunk = gamuts[i : i + chunk_size]
        try:
            result = categorize_terms(chunk, llm)
            all_categorized_gamuts.extend(result)
        except Exception as e:
            print(f"Error processing chunk {chunk_num}: {e}")
            print(f"Skipping terms: {[g.name for g in chunk]}")
            continue

    # Ensure output directory exists
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save results to file
    print(f"Saving {len(all_categorized_gamuts)} categorized gamuts to: {output_file}")
    with open(output_file, "w", encoding="utf-8") as f:
        for term in all_categorized_gamuts:
            f.write(term.model_dump_json(exclude_none=True) + "\n")

    print(f"Processing complete! Results saved to {output_file}")


def main() -> None:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Process Gamuts.net pages and convert them to structured JSONL files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run process_gamuts.py "https://www.gamuts.net/s/vi" --output chest_gamuts.jsonl
  uv run process_gamuts.py "https://www.gamuts.net/s/gi" --output gi_gamuts.jsonl --chunk-size 15
        """,
    )

    parser.add_argument("url", help="The Gamuts.net URL to process")

    parser.add_argument(
        "--output", "-o", default="gamuts_output.jsonl", help="Output JSONL file path (default: gamuts_output.jsonl)"
    )

    parser.add_argument(
        "--chunk-size", "-c", type=int, default=20, help="Number of terms to process in each API call (default: 20)"
    )

    args = parser.parse_args()

    try:
        process_gamuts_url(args.url, args.output, args.chunk_size)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
