"""
This script:
1. Loads existing hood_findings into MongoDB index
2. Tests each new_finding for similarity using find_similar_models()
3. Generates a comprehensive redundancy report
4. Categorizes results for merge strategy
"""

import asyncio
import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

from findingmodel.tools import find_similar_models
from findingmodel.index import Index
from findingmodel import FindingModelFull


class RedundancyDetector:
    def __init__(self):
        self.index = None
        self.results = []
        self.stats = {
            'total_new_findings': 0,
            'unique_models': 0,
            'similar_models': 0,
            'exact_duplicates': 0,
            'errors': 0
        }
    
    async def setup_index(self):
        """Initialize MongoDB index and load existing hood_findings"""
        self.index = Index()
        
        # Load existing hood_findings into index
        hood_dir = Path("defs/hood_findings")
        hood_files = list(hood_dir.glob("*.fm.json"))
        
        print(f"Loading {len(hood_files)} existing hood_findings into index...")
        
        loaded_count = 0
        for file_path in hood_files:
            try:
                with open(file_path, 'r') as f:
                    model_data = json.load(f)
                
                # Add model to index using the correct method
                await self.index.add_or_update_entry_from_file(file_path)
                loaded_count += 1
                
                if loaded_count % 10 == 0:
                    print(f"  Loaded {loaded_count}/{len(hood_files)} models...")
                    
            except Exception as e:
                print(f"  ❌ Error loading {file_path}: {e}")
        
        print(f"✅ Successfully loaded {loaded_count} hood_findings into index")
        return loaded_count
    
    async def analyze_new_finding(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a single new finding for similarity"""
        try:
            with open(file_path, 'r') as f:
                model_data = json.load(f)
            
            # Check if file is empty or malformed
            if not model_data:
                raise ValueError("Empty JSON file")
            
            model = FindingModelFull(**model_data)
            
            # Extract information for similarity search
            finding_name = model.name
            description = model.description
            synonyms = getattr(model, 'synonyms', []) or []
            
            # Run similarity analysis
            analysis = await find_similar_models(
                finding_name=finding_name,
                description=description,
                synonyms=synonyms,
                index=self.index
            )
            
            # Categorize the result
            category = self._categorize_result(analysis)
            
            result = {
                'file_path': str(file_path),
                'finding_name': finding_name,
                'oifm_id': model.oifm_id,
                'description': description[:100] + "..." if len(description) > 100 else description,
                'synonyms': synonyms,
                'recommendation': analysis.recommendation,
                'confidence': analysis.confidence,
                'similar_models': [
                    {
                        'oifm_id': sim.get('oifm_id', ''),
                        'name': sim.get('name', ''),
                        'description': sim.get('description', '')[:100] + "..." if sim.get('description', '') and len(sim.get('description', '')) > 100 else sim.get('description', ''),
                        'synonyms': sim.get('synonyms', [])
                    }
                    for sim in analysis.similar_models
                ],
                'category': category,
                'attributes_count': len(model.attributes),
                'contributors_count': len(model.contributors)
            }
            
            return result
            
        except Exception as e:
            print(f"  ❌ Error analyzing {file_path}: {e}")
            self.stats['errors'] += 1
            return {
                'file_path': str(file_path),
                'finding_name': 'ERROR',
                'error': str(e),
                'category': 'error'
            }
    
    def _categorize_result(self, analysis) -> str:
        """Categorize the similarity analysis result"""
        if analysis.recommendation == "create_new":
            return "unique"  # All create_new recommendations are unique models
        elif analysis.recommendation == "edit_existing":
            if analysis.confidence >= 0.9:
                return "exact_duplicate"
            else:
                return "similar"
        else:
            return "unknown"
    
    async def run_analysis(self):
        """Run the complete redundancy analysis"""
        print("🚀 Starting Phase 1: Redundancy Detection")
        print("=" * 50)
        
        # Step 1: Setup index
        await self.setup_index()
        
        # Step 2: Analyze new findings
        new_dir = Path("defs/findings_from_cdes")
        new_files = list(new_dir.glob("*.fm.json"))
        self.stats['total_new_findings'] = len(new_files)
        
        print(f"\n🔍 Analyzing {len(new_files)} new findings...")
        
        for i, file_path in enumerate(new_files, 1):
            print(f"  [{i:3d}/{len(new_files)}] Analyzing {file_path.name}...")
            
            result = await self.analyze_new_finding(file_path)
            self.results.append(result)
            
            # Update stats
            if result.get('category') == 'unique':
                self.stats['unique_models'] += 1
            elif result.get('category') == 'similar':
                self.stats['similar_models'] += 1
            elif result.get('category') == 'exact_duplicate':
                self.stats['exact_duplicates'] += 1
        
        # Step 3: Generate reports
        await self.generate_reports()
        
        # Step 4: Print summary
        self.print_summary()
    
    async def generate_reports(self):
        """Generate detailed reports"""
        print("\n📊 Generating reports...")
        
        # Create output directory
        output_dir = Path("test_output/redundancy_analysis")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate JSON report
        json_file = output_dir / "redundancy_analysis.json"
        with open(json_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'stats': self.stats,
                'results': self.results
            }, f, indent=2)
        
        # Skip CSV report generation
        
        # Generate category-specific reports
        await self.generate_category_reports(output_dir)
        
        print(f"✅ Reports saved to {output_dir}")
    
    async def generate_category_reports(self, output_dir: Path):
        """Generate reports for each category"""
        categories = ['unique', 'similar', 'exact_duplicate', 'error']
        
        for category in categories:
            category_results = [r for r in self.results if r.get('category') == category]
            
            if category_results:
                category_file = output_dir / f"{category}_models.json"
                with open(category_file, 'w') as f:
                    json.dump(category_results, f, indent=2)
    
    def print_summary(self):
        """Print analysis summary"""
        print("\n" + "=" * 50)
        print("📈 REDUNDANCY ANALYSIS SUMMARY")
        print("=" * 50)
        
        total = self.stats['total_new_findings']
        print(f"Total New Findings Analyzed: {total}")
        print(f"  ✅ Unique Models: {self.stats['unique_models']} ({self.stats['unique_models']/total*100:.1f}%)")
        print(f"  🔄 Similar Models: {self.stats['similar_models']} ({self.stats['similar_models']/total*100:.1f}%)")
        print(f"  📋 Exact Duplicates: {self.stats['exact_duplicates']} ({self.stats['exact_duplicates']/total*100:.1f}%)")
        print(f"  ❌ Errors: {self.stats['errors']} ({self.stats['errors']/total*100:.1f}%)")
        
        print(f"\n📊 Next Steps:")
        print(f"  • {self.stats['unique_models']} models can be added as-is")
        print(f"  • {self.stats['similar_models']} models need merge strategy")
        print(f"  • {self.stats['exact_duplicates']} models are duplicates (skip or merge)")


async def main():
    """Main execution function"""
    detector = RedundancyDetector()
    await detector.run_analysis()


if __name__ == "__main__":
    asyncio.run(main())
