import asyncio
import json
import os
from typing import Dict, List
from pathlib import Path

from findingmodel import FindingModelFull, FindingInfo
from findingmodel.common import model_file_name
from findingmodel.tools.markdown_in import create_model_from_markdown


class MarkdownToFindingModel:
    @staticmethod
    def _generate_model_id(filename: str) -> str:
        """Generate a FindingModel ID from a filename."""
        import hashlib
        hash_obj = hashlib.md5(filename.encode())
        number = int(hash_obj.hexdigest()[:6], 16) % 999999
        return f"OIFM_MD_{number:06d}"

    @staticmethod
    def _generate_attribute_id(filename: str, attribute_name: str, index: int) -> str:
        """Generate an attribute ID from filename and attribute."""
        import hashlib
        combined = f"{filename}_{attribute_name}_{index}"
        hash_obj = hashlib.md5(combined.encode())
        number = int(hash_obj.hexdigest()[:6], 16) % 999999
        return f"OIFMA_MD_{number:06d}"

    @staticmethod
    def _create_oidm_organization() -> Dict:
        """Create the OIDM organization contributor."""
        return {
            "name": "Open Imaging Data Model",
            "code": "OIDM",
            "url": "https://openimagingdata.org"
        }

    @staticmethod
    def _create_person() -> Dict:
        """Create the C. Michael Hood person contributor."""
        return {
            "github_username": "hoodcm",
            "email": "chood@mgh.harvard.edu",
            "name": "C. Michael Hood, MD",
            "organization_code": "MGB"
        }

    @staticmethod
    def _create_default_contributors() -> List[Dict]:
        """Create the default contributors for markdown finding models."""
        return [
            MarkdownToFindingModel._create_oidm_organization(),
            MarkdownToFindingModel._create_person()
        ]

    @staticmethod
    def _extract_finding_name_from_filename(filename: str) -> str:
        """Extract finding name from kebab-case filename."""
        # Remove .md extension and convert kebab-case to title case
        name = filename.replace('.md', '').replace('-', ' ').title()
        return name

    @staticmethod
    def _create_finding_info(finding_name: str, markdown_content: str) -> FindingInfo:
        """Create a FindingInfo object from the finding name and markdown content."""
        # Extract description from the first paragraph after the title
        lines = markdown_content.split('\n')
        description = ""
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('**'):
                description = line
                break
        
        return FindingInfo(
            name=finding_name,
            description=description or f"Finding model for {finding_name}"
        )

    @staticmethod
    async def process_file(input_file: str, output_dir: str) -> bool:
        """Process a single markdown file."""
        try:
            # Read markdown file
            with open(input_file, "r", encoding="utf-8") as f:
                markdown_content = f.read()
            
            # Get filename without path
            filename = Path(input_file).name
            finding_name = MarkdownToFindingModel._extract_finding_name_from_filename(filename)
            
            # Create FindingInfo
            finding_info = MarkdownToFindingModel._create_finding_info(finding_name, markdown_content)
            
            # Convert markdown to FindingModel using the existing tool
            finding_model = await create_model_from_markdown(
                finding_info=finding_info,
                markdown_text=markdown_content
            )
            
            # Convert to FindingModelFull and add IDs and contributors
            model_dict = finding_model.model_dump()
            
            # Add IDs
            model_dict["oifm_id"] = MarkdownToFindingModel._generate_model_id(filename)
            
            # Add contributors
            model_dict["contributors"] = MarkdownToFindingModel._create_default_contributors()
            
            # Add IDs to attributes
            for i, attr in enumerate(model_dict.get("attributes", [])):
                attr["oifma_id"] = MarkdownToFindingModel._generate_attribute_id(filename, attr["name"], i)
                
                # Add value codes to choice attributes
                if attr.get("type") == "choice" and "values" in attr:
                    for j, value in enumerate(attr["values"]):
                        value["value_code"] = f"{attr['oifma_id']}.{j}"
            
            # Create FindingModelFull and write
            fm = FindingModelFull(**model_dict)
            output_file = Path(output_dir) / model_file_name(fm.name)
            
            # Ensure output directory exists
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Write using the package's method
            output_file.write_text(fm.model_dump_json(indent=2, exclude_none=True))
            
            print(f"Converted {input_file} -> {output_file}")
            return True
                
        except Exception as e:
            print(f"Error processing {input_file}: {str(e)}")
            return False

    @staticmethod
    async def process_directory(input_dir: str, output_dir: str):
        """Process all markdown files in a directory."""
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Process all markdown files
        for filename in os.listdir(input_dir):
            if filename.endswith(".md"):
                input_file = os.path.join(input_dir, filename)
                await MarkdownToFindingModel.process_file(input_file, output_dir)


async def main():
    """Main function to process markdown files."""
    # Hardcoded paths
    input_dir = "../CDEStaging/definitions/hood_CT_chest"
    output_dir = "defs/markdown_findings"
    
    print(f"Converting markdown files from {input_dir}")
    print(f"Output directory: {output_dir}")
    
    await MarkdownToFindingModel.process_directory(input_dir, output_dir)


if __name__ == "__main__":
    asyncio.run(main()) 