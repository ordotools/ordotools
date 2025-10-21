#!/usr/bin/env python3
"""
Migrate country data from Python files to database.
"""
import sys
import os
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.db import get_connection


def migrate_countries():
    """Extract country information from country/*.py files and insert into database."""
    conn = get_connection()
    
    # Define countries based on existing files
    countries = [
        {
            'code': 'australiae',
            'name_latin': 'Australiae',
            'name_english': 'Australia'
        },
        {
            'code': 'hispaniae',
            'name_latin': 'Hispaniae',
            'name_english': 'Spain'
        },
    ]
    
    with conn:
        for country in countries:
            try:
                conn.execute(
                    """
                    INSERT OR REPLACE INTO countries (code, name_latin, name_english)
                    VALUES (?, ?, ?)
                    """,
                    (country['code'], country['name_latin'], country['name_english'])
                )
                print(f"✓ Migrated country: {country['name_latin']}")
            except Exception as e:
                print(f"✗ Error migrating country {country['code']}: {e}")
    
    # Verify migration
    cursor = conn.execute("SELECT COUNT(*) FROM countries")
    count = cursor.fetchone()[0]
    print(f"\nTotal countries in database: {count}")
    
    conn.close()
    return count


if __name__ == '__main__':
    print("=" * 60)
    print("MIGRATING COUNTRIES")
    print("=" * 60)
    result = migrate_countries()
    print(f"\nMigration complete: {result} countries migrated")

