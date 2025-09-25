"""
Attribute Data Merger Agent

This agent is specifically designed to merge detailed attribute data from full finding models
into stub entries in MongoDB. It finds exact attribute matches and transfers the complete
attribute data (values, descriptions, etc.) to the stub.
"""

import json
import os
from typing import Dict, Any, List, Literal, Optional
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AttributeDataMatch(BaseModel):
    """Represents a match between a stub attribute and a full attribute"""
    stub_attribute: Dict[str, Any]
    full_attribute: Dict[str, Any]
    is_exact_match: bool
    confidence: float
    reasoning: str


class AttributeDataMergeResult(BaseModel):
    """Result of merging attribute data from full model to stub"""
    finding_name: str
    oifm_id: str
    total_stub_attributes: int
    total_full_attributes: int
    exact_matches: List[AttributeDataMatch]
    unmatched_stub_attributes: List[Dict[str, Any]]
    unmatched_full_attributes: List[Dict[str, Any]]
    merged_attributes: List[Dict[str, Any]] = []
    summary: str


# Initialize the OpenAI model
model = OpenAIChatModel("gpt-4o-mini")


class AttributeDataMerger:
    """Merges detailed attribute data from full finding models into MongoDB stubs"""
    
    def __init__(self):
        self.agent = Agent(
            model=model,
            output_type=AttributeDataMergeResult,
            system_prompt="""You are a medical imaging expert. Match attributes between two finding models.

            RULES:
            1. Find EXACT matches only (confidence 0.8+)
            2. Match by: attribute_id (if both have it), then name+type
            3. Return exact matches, unmatched attributes, and summary
            4. Be conservative - only match when 100% certain

            OUTPUT FORMAT:
            - finding_name: string
            - oifm_id: string  
            - total_stub_attributes: number
            - total_full_attributes: number
            - exact_matches: list of AttributeDataMatch objects
            - unmatched_stub_attributes: list of attribute objects
            - unmatched_full_attributes: list of attribute objects
            - merged_attributes: empty list (will be filled later)
            - summary: string describing results

            Each AttributeDataMatch needs:
            - stub_attribute: dict
            - full_attribute: dict  
            - is_exact_match: true
            - confidence: 0.8-1.0
            - reasoning: string"""
        )
    
    async def merge_attribute_data(self, stub_data: Dict[str, Any], full_data: Dict[str, Any]) -> AttributeDataMergeResult:
        """Merge detailed attribute data from full model into stub model"""
        
        # Extract attribute information
        stub_attrs = self._extract_stub_attributes(stub_data.get('attributes', []))
        full_attrs = self._extract_full_attributes(full_data.get('attributes', []))
        
        # Create context for the AI
        context = f"""Stub Finding Model (from MongoDB):
        Name: {stub_data.get('name', 'Unknown')}
        OIFM ID: {stub_data.get('oifm_id', 'Unknown')}
        Stub Attributes: {stub_attrs}
        
        Full Finding Model (from JSON file):
        Name: {full_data.get('name', 'Unknown')}
        OIFM ID: {full_data.get('oifm_id', 'Unknown')}
        Full Attributes: {full_attrs}
        
        Please find exact matches between the stub and full attributes and merge the detailed data."""
        
        print(f"    DEBUG: Sending context to AI agent...")
        print(f"    DEBUG: Stub attributes count: {len(stub_attrs)}")
        print(f"    DEBUG: Full attributes count: {len(full_attrs)}")
        
        try:
            result = await self.agent.run(context)
            print(f"    DEBUG: AI agent completed successfully")
            print(f"    DEBUG: Number of exact matches returned: {len(result.output.exact_matches)}")
            if result.output.exact_matches:
                print(f"    DEBUG: First match full_attribute keys: {list(result.output.exact_matches[0].full_attribute.keys())}")
            return result.output
        except Exception as e:
            print(f"    DEBUG: AI agent failed with error: {e}")
            print(f"    DEBUG: Error type: {type(e)}")
            raise
    
    def _extract_stub_attributes(self, attributes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract attribute information from stub model"""
        stub_attrs = []
        
        for attr in attributes:
            stub_attr = {
                "attribute_id": attr.get('attribute_id', ''),
                "name": attr.get('name', ''),
                "type": attr.get('type', ''),
                "description": attr.get('description', '') or '',
                "required": attr.get('required', False),
                "max_selected": attr.get('max_selected', 1)
            }
            
            # Add values for choice attributes if they exist in stub
            if attr.get('type') == "choice" and 'values' in attr:
                values = []
                for value in attr['values']:
                    value_info = {
                        "value_code": value.get('value_code', ''),
                        "name": value.get('name', ''),
                        "description": value.get('description', '') or '',
                        "index_codes": value.get('index_codes', []) or []
                    }
                    values.append(value_info)
                stub_attr["values"] = values
            
            # Add numeric range for numeric attributes if they exist in stub
            elif attr.get('type') == "numeric":
                if 'min_value' in attr:
                    stub_attr["min_value"] = attr.get('min_value')
                if 'max_value' in attr:
                    stub_attr["max_value"] = attr.get('max_value')
                if 'unit' in attr:
                    stub_attr["unit"] = attr.get('unit', '')
            
            stub_attrs.append(stub_attr)
        
        return stub_attrs
    
    def _extract_full_attributes(self, attributes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract attribute information from full model"""
        full_attrs = []
        
        for attr in attributes:
            full_attr = {
                "oifma_id": attr.get('oifma_id', ''),
                "name": attr.get('name', ''),
                "type": attr.get('type', ''),
                "description": attr.get('description', '') or '',
                "required": attr.get('required', False),
                "max_selected": attr.get('max_selected', 1)
            }
            
            # Add values for choice attributes
            if attr.get('type') == "choice" and 'values' in attr:
                values = []
                for value in attr['values']:
                    value_info = {
                        "value_code": value.get('value_code', ''),
                        "name": value.get('name', ''),
                        "description": value.get('description', '') or '',
                        "index_codes": value.get('index_codes', []) or []
                    }
                    values.append(value_info)
                full_attr["values"] = values
            
            # Add numeric range for numeric attributes
            elif attr.get('type') == "numeric":
                if 'min_value' in attr:
                    full_attr["min_value"] = attr.get('min_value')
                if 'max_value' in attr:
                    full_attr["max_value"] = attr.get('max_value')
                if 'unit' in attr:
                    full_attr["unit"] = attr.get('unit', '')
            
            full_attrs.append(full_attr)
        
        return full_attrs
    
    def _merge_attribute_values(self, stub_attr: Dict[str, Any], full_attr: Dict[str, Any]) -> Dict[str, Any]:
        """Intelligently merge values from stub and full attributes"""
        # Start with full attribute as base (has complete data)
        merged_attr = full_attr.copy()
        
        # Preserve stub's attribute_id if it exists
        if stub_attr.get('attribute_id'):
            merged_attr['attribute_id'] = stub_attr['attribute_id']
        
        # Merge values for choice attributes
        if stub_attr.get('type') == 'choice' and 'values' in stub_attr and 'values' in full_attr:
            stub_values = stub_attr.get('values', [])
            full_values = full_attr.get('values', [])
            
            # Create a set of existing value names for deduplication
            existing_names = set()
            existing_codes = set()
            
            # Start with full values (they have complete data)
            merged_values = []
            for value in full_values:
                merged_values.append(value)
                if value.get('name'):
                    existing_names.add(value['name'].lower())
                if value.get('value_code'):
                    existing_codes.add(value['value_code'])
            
            # Add stub values that don't duplicate existing ones
            for stub_value in stub_values:
                stub_name = stub_value.get('name', '').lower()
                stub_code = stub_value.get('value_code', '')
                
                # Check if this value already exists (by name or code)
                if (not stub_name or stub_name not in existing_names) and \
                   (not stub_code or stub_code not in existing_codes):
                    merged_values.append(stub_value)
                    if stub_name:
                        existing_names.add(stub_name)
                    if stub_code:
                        existing_codes.add(stub_code)
            
            merged_attr['values'] = merged_values
        
        # Merge numeric attributes (prefer full values, but keep stub if full doesn't have them)
        elif stub_attr.get('type') == 'numeric':
            if 'min_value' not in merged_attr and 'min_value' in stub_attr:
                merged_attr['min_value'] = stub_attr['min_value']
            if 'max_value' not in merged_attr and 'max_value' in stub_attr:
                merged_attr['max_value'] = stub_attr['max_value']
            if 'unit' not in merged_attr and 'unit' in stub_attr:
                merged_attr['unit'] = stub_attr['unit']
        
        # Merge other fields (prefer full, but keep stub if full doesn't have them)
        for field in ['description', 'required', 'max_selected']:
            if field not in merged_attr or not merged_attr[field]:
                if field in stub_attr and stub_attr[field]:
                    merged_attr[field] = stub_attr[field]
        
        return merged_attr

    def create_merged_attributes(self, result: AttributeDataMergeResult) -> List[Dict[str, Any]]:
        """Create the final merged attributes list for the stub"""
        merged_attrs = []
        
        # Add matched attributes with merged data
        for match in result.exact_matches:
            if match.is_exact_match:
                # Intelligently merge stub and full attribute data
                merged_attr = self._merge_attribute_values(match.stub_attribute, match.full_attribute)
                merged_attrs.append(merged_attr)
        
        # Add unmatched stub attributes (keep as-is)
        for stub_attr in result.unmatched_stub_attributes:
            merged_attrs.append(stub_attr)
        
        return merged_attrs
