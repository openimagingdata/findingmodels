import asyncio
import json
import os
from typing import List
from pathlib import Path

from dotenv import load_dotenv
from findingmodel import FindingModelFull, FindingInfo
from findingmodel.common import model_file_name
from findingmodel.contributor import Person, Organization
from findingmodel.tools import (
    create_model_from_markdown,
    add_ids_to_model,
    add_standard_codes_to_model
)

load_dotenv()


class MarkdownToFindingModelAdapter:
    @staticmethod
    def _create_oidm_organization() -> Organization:
        """Create the OIDM organization contributor."""
        return Organization(
            name="Open Imaging Data Model",
            code="OIDM",
            url="https://openimagingdata.org"
        )

    @staticmethod
    def _create_person() -> Person:
        """Create the C. Michael Hood person contributor."""
        return Person(
            github_username="hoodcm",
            email="chood@mgh.harvard.edu",
            name="C. Michael Hood, MD",
            organization_code="MGB"
        )

    @staticmethod
    def _create_default_contributors() -> List:
        """Create the default contributors for markdown finding models."""
        return [
            MarkdownToFindingModelAdapter._create_oidm_organization(),
            MarkdownToFindingModelAdapter._create_person()
        ]

    @staticmethod
    async def process_markdown_file(input_file: str, output_dir: str) -> bool:
        """Process a single markdown file to FindingModel."""
        try:
            # Read the markdown file
            with open(input_file, "r", encoding="utf-8") as f:
                markdown_content = f.read()
            
            # Extract finding name from filename
            filename = Path(input_file).stem
            finding_name = filename.replace('-', ' ').replace('_', ' ').title()
            
            print(f"Processing {filename}.md...")
            
            # Create basic finding info (create_model_from_markdown will generate description via AI)
            finding_info = FindingInfo(
                name=finding_name.lower(),
                description=""  # Empty - create_model_from_markdown will generate this
            )
            
            # Create complete model from markdown (includes AI description generation)
            model = await create_model_from_markdown(
                finding_info,
                markdown_text=markdown_content
            )
            print(f"  Generated description for '{finding_name}': {model.description[:100]}...")
            
            # Add our custom enhancements
            full_model = add_ids_to_model(model, source="MGB")
            add_standard_codes_to_model(full_model)
            full_model.contributors = MarkdownToFindingModelAdapter._create_default_contributors()
            
            # Convert to FindingModelFull and save
            fm = FindingModelFull(**full_model.model_dump())
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True), encoding='utf-8')
            
            print(f"  Created model with {len(fm.attributes)} attributes")
            print(f"  Adapted {filename}.md -> {output_file.name}")
            return True
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            import traceback
            traceback.print_exc()
            return False

    @staticmethod
    async def process_directory(input_dir: str, output_dir: str):
        """Process all markdown files in a directory."""
        os.makedirs(output_dir, exist_ok=True)
        
        # Track success and failure counts
        successful_count = 0
        failed_count = 0
        total_files = 0
        
        print(f"Starting to process markdown files in: {input_dir}")
        print("="*60)
        
        for filename in os.listdir(input_dir):
            if filename.endswith(".md"):
                total_files += 1
                input_file = os.path.join(input_dir, filename)
                
                if await MarkdownToFindingModelAdapter.process_markdown_file(input_file, output_dir):
                    successful_count += 1
                else:
                    failed_count += 1
                    print(f"Failed to process {filename}")
        
        # Count unique output files generated
        unique_output_files = len([f for f in os.listdir(output_dir) if f.endswith('.fm.json')])
        
        # Print summary
        print("="*60)
        print("PROCESSING SUMMARY")
        print("="*60)
        print(f"Total markdown files found: {total_files}")
        print(f"Successfully converted: {successful_count}")
        print(f"Failed to convert: {failed_count}")
        print(f"Success rate: {(successful_count/total_files*100):.1f}%" if total_files > 0 else "Success rate: N/A")
        print(f"Unique finding models generated: {unique_output_files}")
        print(f"Files overwritten: {successful_count - unique_output_files}")
        print("="*60)
        print("Processing complete!")


async def main():
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/hood_findings"
    
    print(f"Converting markdown files from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    await MarkdownToFindingModelAdapter.process_directory(input_dir, output_dir)


if __name__ == "__main__":
    asyncio.run(main())
