#!/usr/bin/env python3
"""
Run all database migrations in the correct order.
"""
import sys
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.migration_scripts.migrate_countries import migrate_countries
from ordotools.tools.migration_scripts.migrate_dioceses import migrate_dioceses
from ordotools.tools.migration_scripts.migrate_temporal import migrate_temporal_feasts
from ordotools.tools.migration_scripts.migrate_sanctoral import migrate_roman_sanctoral, migrate_diocese_sanctoral
from ordotools.tools.migration_scripts.migrate_translations import migrate_translations


def run_all_migrations():
    """Run all migrations in sequence."""
    print("\n" + "=" * 70)
    print(" " * 20 + "DATABASE MIGRATION")
    print("=" * 70)
    
    results = {}
    
    try:
        print("\n[Step 1/6] Migrating Countries...")
        print("-" * 70)
        results['countries'] = migrate_countries()
        
        print("\n[Step 2/6] Migrating Dioceses...")
        print("-" * 70)
        results['dioceses'] = migrate_dioceses()
        
        print("\n[Step 3/6] Migrating Temporal Feasts...")
        print("-" * 70)
        results['temporal'] = migrate_temporal_feasts()
        
        print("\n[Step 4/6] Migrating Roman Sanctoral Feasts...")
        print("-" * 70)
        results['roman_sanctoral'] = migrate_roman_sanctoral()
        
        print("\n[Step 5/6] Migrating Diocese-Specific Sanctoral Feasts...")
        print("-" * 70)
        results['diocese_sanctoral'] = migrate_diocese_sanctoral()
        
        print("\n[Step 6/6] Migrating Translations...")
        print("-" * 70)
        results['translations'] = migrate_translations()
        
    except Exception as e:
        print(f"\n✗ MIGRATION FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # Summary
    print("\n" + "=" * 70)
    print(" " * 22 + "MIGRATION SUMMARY")
    print("=" * 70)
    print(f"Countries:                  {results.get('countries', 0):>6}")
    print(f"Dioceses:                   {results.get('dioceses', 0):>6}")
    print(f"Temporal Feasts:            {results.get('temporal', 0):>6}")
    print(f"Roman Sanctoral Feasts:     {results.get('roman_sanctoral', 0):>6}")
    print(f"Diocese Sanctoral Feasts:   {results.get('diocese_sanctoral', 0):>6}")
    print(f"Translations:               {results.get('translations', 0):>6}")
    print("=" * 70)
    print("\n✓ ALL MIGRATIONS COMPLETED SUCCESSFULLY")
    print("=" * 70 + "\n")
    
    return True


if __name__ == '__main__':
    success = run_all_migrations()
    sys.exit(0 if success else 1)

