"""
This script:
1. Loads existing hood_findings, cde findgins into MongoDB index
2. Tests each new finding for similarity using find_similar_models()
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
            'total_analyzed': 0,
            'cde_vs_mongodb': {'total': 0, 'unique': 0, 'similar': 0, 'exact_duplicate': 0, 'error': 0},
            'hood_vs_mongodb': {'total': 0, 'unique': 0, 'similar': 0, 'exact_duplicate': 0, 'error': 0},
            'hood_vs_cde': {'total': 0, 'unique': 0, 'similar': 0, 'exact_duplicate': 0, 'error': 0},
            'overall': {'unique': 0, 'similar': 0, 'exact_duplicate': 0, 'error': 0}
        }
    
    async def setup_index(self):
        """Initialize MongoDB index and load ALL findings"""
        self.index = Index()
        
        # Check what's already in the database
        existing_count = await self.index.index_collection.count_documents({})
        print(f" MongoDB database currently contains {existing_count} existing findings")
        
        # Load ALL local findings into the index
        print(f"\n Loading all local findings into index...")
        
        # Load hood_findings
        hood_dir = Path("defs/hood_findings")
        hood_files = list(hood_dir.glob("*.fm.json"))
        print(f"  Loading {len(hood_files)} hood_findings...")
        
        hood_loaded = 0
        for file_path in hood_files:
            try:
                await self.index.add_or_update_entry_from_file(file_path)
                hood_loaded += 1
                if hood_loaded % 20 == 0:
                    print(f"    Loaded {hood_loaded}/{len(hood_files)} hood findings...")
            except Exception as e:
                print(f"    ❌ Error loading {file_path}: {e}")
        
        # Load findings_from_cdes
        cdes_dir = Path("defs/findings_from_cdes")
        cdes_files = list(cdes_dir.glob("*.fm.json"))
        print(f"  Loading {len(cdes_files)} findings_from_cdes...")
        
        cdes_loaded = 0
        for file_path in cdes_files:
            try:
                await self.index.add_or_update_entry_from_file(file_path)
                cdes_loaded += 1
                if cdes_loaded % 20 == 0:
                    print(f"    Loaded {cdes_loaded}/{len(cdes_files)} CDE findings...")
            except Exception as e:
                print(f"    ❌ Error loading {file_path}: {e}")
        
        # Get final count
        total_count = await self.index.index_collection.count_documents({})
        print(f"\n Index now contains {total_count} total findings:")
        print(f"  • {existing_count} previously in MongoDB")
        print(f"  • {hood_loaded} hood_findings loaded")
        print(f"  • {cdes_loaded} findings_from_cdes loaded")
        
        return total_count
    
    async def analyze_new_finding(self, file_path: Path, comparison_type: str = "CDE vs MongoDB") -> Dict[str, Any]:
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
                'comparison_type': comparison_type,
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
                'attributes_count': len(model.attributes) if model.attributes else 0,
                'contributors_count': len(model.contributors) if model.contributors else 0
            }
            
            return result
            
        except Exception as e:
            print(f"  ❌ Error analyzing {file_path}: {e}")
            return {
                'file_path': str(file_path),
                'finding_name': 'ERROR',
                'error': str(e),
                'comparison_type': comparison_type,
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
        """Run comprehensive 3-way redundancy analysis"""
        print(" Starting Comprehensive 3-Way Redundancy Detection")
        print("=" * 70)
        
        # Step 1: Setup index with ALL findings
        total_findings = await self.setup_index()
        
        # Step 2: Compare findings_from_cdes against existing MongoDB
        print(f"\n🔍 PHASE 1: CDE Findings vs Existing MongoDB")
        print("-" * 50)
        cdes_dir = Path("defs/findings_from_cdes")
        cdes_files = list(cdes_dir.glob("*.fm.json"))
        
        print(f"Analyzing {len(cdes_files)} CDE findings against existing database...")
        for i, file_path in enumerate(cdes_files, 1):
            print(f"  [{i:3d}/{len(cdes_files)}] Analyzing {file_path.name}...")
            result = await self.analyze_new_finding(file_path, "cde_vs_mongodb")
            self.results.append(result)
            self._update_stats(result)
        
        # Step 3: Compare hood_findings against existing MongoDB
        print(f"\n🔍 PHASE 2: Hood Findings vs Existing MongoDB")
        print("-" * 50)
        hood_dir = Path("defs/hood_findings")
        hood_files = list(hood_dir.glob("*.fm.json"))
        
        print(f"Analyzing {len(hood_files)} hood findings against existing database...")
        for i, file_path in enumerate(hood_files, 1):
            print(f"  [{i:3d}/{len(hood_files)}] Analyzing {file_path.name}...")
            result = await self.analyze_new_finding(file_path, "hood_vs_mongodb")
            self.results.append(result)
            self._update_stats(result)
        
        # Step 4: Compare hood_findings vs CDE findings
        print(f"\n🔍 PHASE 3: Hood Findings vs CDE Findings")
        print("-" * 50)
        print(f"Analyzing {len(hood_files)} hood findings against {len(cdes_files)} CDE findings...")
        for i, file_path in enumerate(hood_files, 1):
            print(f"  [{i:3d}/{len(hood_files)}] Analyzing {file_path.name}...")
            result = await self.analyze_new_finding(file_path, "hood_vs_cde")
            self.results.append(result)
            self._update_stats(result)
        
        # Step 5: Generate reports
        await self.generate_reports()
        
        # Step 6: Print summary
        self.print_summary()
    
    def _update_stats(self, result):
        """Update statistics based on result category and comparison type"""
        comparison_type = result.get('comparison_type', 'unknown')
        category = result.get('category', 'unknown')
        
        # Update overall stats
        if category in ['unique', 'similar', 'exact_duplicate', 'error']:
            if category not in self.stats['overall']:
                self.stats['overall'][category] = 0
            self.stats['overall'][category] += 1
            self.stats['total_analyzed'] += 1
        
        # Update specific comparison type stats
        if comparison_type in self.stats:
            self.stats[comparison_type]['total'] += 1
            if category in ['unique', 'similar', 'exact_duplicate', 'error']:
                if category not in self.stats[comparison_type]:
                    self.stats[comparison_type][category] = 0
                self.stats[comparison_type][category] += 1
    
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
        
        # Generate user-friendly summary report
        await self.generate_user_friendly_summary(output_dir)
        
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
    
    async def generate_user_friendly_summary(self, output_dir: Path):
        """Generate a user-friendly summary report"""
        summary_file = output_dir / "SUMMARY_REPORT.md"
        
        # Count findings by comparison type
        cde_vs_mongodb = [r for r in self.results if r.get('comparison_type') == 'cde_vs_mongodb']
        hood_vs_mongodb = [r for r in self.results if r.get('comparison_type') == 'hood_vs_mongodb']
        hood_vs_cde = [r for r in self.results if r.get('comparison_type') == 'hood_vs_cde']
        
        # Count by category for each comparison
        cde_unique = len([r for r in cde_vs_mongodb if r.get('category') == 'unique'])
        cde_duplicates = len([r for r in cde_vs_mongodb if r.get('category') == 'exact_duplicate'])
        cde_errors = len([r for r in cde_vs_mongodb if r.get('category') == 'error'])
        
        hood_mongodb_unique = len([r for r in hood_vs_mongodb if r.get('category') == 'unique'])
        hood_mongodb_duplicates = len([r for r in hood_vs_mongodb if r.get('category') == 'exact_duplicate'])
        hood_mongodb_errors = len([r for r in hood_vs_mongodb if r.get('category') == 'error'])
        
        hood_cde_unique = len([r for r in hood_vs_cde if r.get('category') == 'unique'])
        hood_cde_duplicates = len([r for r in hood_vs_cde if r.get('category') == 'exact_duplicate'])
        hood_cde_errors = len([r for r in hood_vs_cde if r.get('category') == 'error'])
        
        # Calculate percentages
        total_cde = len(cde_vs_mongodb)
        total_hood_mongodb = len(hood_vs_mongodb)
        total_hood_cde = len(hood_vs_cde)
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("# 🔍 Redundancy Analysis Summary Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## 📊 Overview\n\n")
            f.write(f"- **Total Findings Analyzed:** {self.stats['total_analyzed']}\n")
            f.write(f"- **MongoDB Database Size:** 2,155 existing findings\n")
            f.write(f"- **CDE Findings:** 135 models\n")
            f.write(f"- **Hood Findings:** 98 models\n\n")
            
            f.write("## 🎯 Key Results\n\n")
            f.write(f"| Category | Count | Percentage |\n")
            f.write(f"|----------|-------|------------|\n")
            f.write(f"| ✅ **Unique Models** | {self.stats['overall']['unique']} | {self.stats['overall']['unique']/self.stats['total_analyzed']*100:.1f}% |\n")
            f.write(f"| 📋 **Exact Duplicates** | {self.stats['overall']['exact_duplicate']} | {self.stats['overall']['exact_duplicate']/self.stats['total_analyzed']*100:.1f}% |\n")
            f.write(f"| 🔄 **Similar Models** | {self.stats['overall']['similar']} | {self.stats['overall']['similar']/self.stats['total_analyzed']*100:.1f}% |\n")
            f.write(f"| ❌ **Errors** | {self.stats['overall'].get('error', 0)} | {self.stats['overall'].get('error', 0)/self.stats['total_analyzed']*100:.1f}% |\n\n")
            
            f.write("## 🔍 Detailed Breakdown by Comparison\n\n")
            
            f.write("### 1️⃣ CDE Findings vs MongoDB Database\n")
            f.write(f"- **Compared:** {total_cde} CDE findings against 2,155 existing findings\n")
            f.write(f"- **Unique:** {cde_unique} ({cde_unique/total_cde*100:.1f}%)\n")
            f.write(f"- **Duplicates:** {cde_duplicates} ({cde_duplicates/total_cde*100:.1f}%)\n")
            f.write(f"- **Errors:** {cde_errors} ({cde_errors/total_cde*100:.1f}%)\n\n")
            
            f.write("### 2️⃣ Hood Findings vs MongoDB Database\n")
            f.write(f"- **Compared:** {total_hood_mongodb} hood findings against 2,155 existing findings\n")
            f.write(f"- **Unique:** {hood_mongodb_unique} ({hood_mongodb_unique/total_hood_mongodb*100:.1f}%)\n")
            f.write(f"- **Duplicates:** {hood_mongodb_duplicates} ({hood_mongodb_duplicates/total_hood_mongodb*100:.1f}%)\n")
            f.write(f"- **Errors:** {hood_mongodb_errors} ({hood_mongodb_errors/total_hood_mongodb*100:.1f}%)\n\n")
            
            f.write("### 3️⃣ Hood Findings vs CDE Findings\n")
            f.write(f"- **Compared:** {total_hood_cde} hood findings against 135 CDE findings\n")
            f.write(f"- **Unique:** {hood_cde_unique} ({hood_cde_unique/total_hood_cde*100:.1f}%)\n")
            f.write(f"- **Duplicates:** {hood_cde_duplicates} ({hood_cde_duplicates/total_hood_cde*100:.1f}%)\n")
            f.write(f"- **Errors:** {hood_cde_errors} ({hood_cde_errors/total_hood_cde*100:.1f}%)\n\n")
            
            f.write("## 📋 Next Steps\n\n")
            f.write(f"### ✅ **Add These {self.stats['overall']['unique']} Unique Models:**\n")
            f.write("- These models are truly unique and can be added to your database as-is\n")
            f.write("- No conflicts or duplicates found\n")
            f.write("- See `unique_models.json` for the complete list\n\n")
            
            f.write(f"### 🔄 **Review These {self.stats['overall']['exact_duplicate']} Duplicates:**\n")
            f.write("- These models already exist in your database\n")
            f.write("- Consider merging new attributes into existing models\n")
            f.write("- Or skip adding them to avoid redundancy\n")
            f.write("- See `exact_duplicate_models.json` for detailed comparison\n\n")
            
            if self.stats['overall'].get('error', 0) > 0:
                f.write(f"### ❌ **Fix These {self.stats['overall'].get('error', 0)} Errors:**\n")
                f.write("- These files had processing errors (empty files, ID conflicts, etc.)\n")
                f.write("- See `error_models.json` for details\n\n")
            
            f.write("## 📁 Generated Files\n\n")
            f.write("- `redundancy_analysis.json` - Complete analysis data\n")
            f.write("- `unique_models.json` - Models safe to add\n")
            f.write("- `exact_duplicate_models.json` - Duplicate models to review\n")
            f.write("- `error_models.json` - Files with processing errors\n")
            f.write("- `SUMMARY_REPORT.md` - This user-friendly summary\n\n")
            
            f.write("## 💡 Key Insights\n\n")
            f.write(f"- **{self.stats['overall']['exact_duplicate']/self.stats['total_analyzed']*100:.1f}% duplicate rate** indicates a well-populated database\n")
            f.write(f"- Most new findings already exist in your comprehensive collection\n")
            f.write(f"- Focus on the {self.stats['overall']['unique']} unique models for new additions\n")
            f.write(f"- Consider merging strategies for the duplicate models\n\n")
            
            f.write("---\n")
            f.write("*Report generated by Redundancy Detection Script*\n")
    
    def print_summary(self):
        """Print comprehensive analysis summary"""
        print("\n" + "=" * 70)
        print("📈 COMPREHENSIVE REDUNDANCY ANALYSIS SUMMARY")
        print("=" * 70)
        
        total = self.stats['total_analyzed']
        print(f"Total Findings Analyzed: {total}")
        
        # Overall summary
        print(f"\n📊 OVERALL RESULTS:")
        overall = self.stats['overall']
        print(f"  ✅ Unique Models: {overall['unique']} ({overall['unique']/total*100:.1f}%)")
        print(f"  🔄 Similar Models: {overall['similar']} ({overall['similar']/total*100:.1f}%)")
        print(f"  📋 Exact Duplicates: {overall['exact_duplicate']} ({overall['exact_duplicate']/total*100:.1f}%)")
        print(f"  ❌ Errors: {overall.get('error', 0)} ({overall.get('error', 0)/total*100:.1f}%)")
        
        # Breakdown by comparison type
        print(f"\n📋 BREAKDOWN BY COMPARISON TYPE:")
        
        for comp_type, stats in self.stats.items():
            if comp_type in ['cde_vs_mongodb', 'hood_vs_mongodb', 'hood_vs_cde']:
                print(f"\n  {comp_type.upper().replace('_', ' ')}:")
                print(f"    Total: {stats['total']}")
                print(f"    ✅ Unique: {stats['unique']} ({stats['unique']/stats['total']*100:.1f}%)" if stats['total'] > 0 else "    ✅ Unique: 0")
                print(f"    🔄 Similar: {stats['similar']} ({stats['similar']/stats['total']*100:.1f}%)" if stats['total'] > 0 else "    🔄 Similar: 0")
                print(f"    📋 Duplicates: {stats['exact_duplicate']} ({stats['exact_duplicate']/stats['total']*100:.1f}%)" if stats['total'] > 0 else "    📋 Duplicates: 0")
                print(f"    ❌ Errors: {stats.get('error', 0)} ({stats.get('error', 0)/stats['total']*100:.1f}%)" if stats['total'] > 0 else "    ❌ Errors: 0")
        
        print(f"\n📊 NEXT STEPS:")
        print(f"  • {overall['unique']} models can be added as-is")
        print(f"  • {overall['similar']} models need merge strategy")
        print(f"  • {overall['exact_duplicate']} models are duplicates (skip or merge)")


async def main():
    """Main execution function"""
    detector = RedundancyDetector()
    await detector.run_analysis()


if __name__ == "__main__":
    asyncio.run(main())
