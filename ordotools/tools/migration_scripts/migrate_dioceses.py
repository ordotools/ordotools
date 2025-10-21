#!/usr/bin/env python3
"""
Migrate diocese data from Python files to database.
"""
import sys
import os
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.db import get_connection


def migrate_dioceses():
    """Extract diocese information from diocese/*.py files and insert into database."""
    conn = get_connection()
    
    # First, get country IDs
    cursor = conn.execute("SELECT id, code FROM countries")
    countries = {row[1]: row[0] for row in cursor.fetchall()}
    
    # Define dioceses based on existing files
    dioceses = [
        {
            'code': 'roman',
            'name_latin': 'Romanus',
            'name_english': 'Roman',
            'country_id': None  # Universal calendar
        },
        {
            'code': 'bathurstensis',
            'name_latin': 'Bathurstensis',
            'name_english': 'Bathurst',
            'country_code': 'australiae'
        },
        {
            'code': 'lismorensis',
            'name_latin': 'Lismorensis',
            'name_english': 'Lismore',
            'country_code': 'australiae'
        },
        {
            'code': 'maitlandensis',
            'name_latin': 'Maitlandensis',
            'name_english': 'Maitland',
            'country_code': 'australiae'
        },
        {
            'code': 'melbournensis',
            'name_latin': 'Ad Melbournen',
            'name_english': 'Melbourne',
            'country_code': 'australiae'
        },
        {
            'code': 'rockhamptonensis',
            'name_latin': 'Rockhamptonensis',
            'name_english': 'Rockhampton',
            'country_code': 'australiae'
        },
        {
            'code': 'rennes',
            'name_latin': 'Redonensis',
            'name_english': 'Rennes',
            'country_code': 'hispaniae'  # Note: might need correction
        },
    ]
    
    with conn:
        for diocese in dioceses:
            try:
                country_id = diocese.get('country_id')
                if 'country_code' in diocese:
                    country_id = countries.get(diocese['country_code'])
                
                conn.execute(
                    """
                    INSERT OR REPLACE INTO dioceses (code, name_latin, name_english, country_id)
                    VALUES (?, ?, ?, ?)
                    """,
                    (diocese['code'], diocese['name_latin'], diocese['name_english'], country_id)
                )
                print(f"✓ Migrated diocese: {diocese['name_latin']}")
            except Exception as e:
                print(f"✗ Error migrating diocese {diocese['code']}: {e}")
    
    # Verify migration
    cursor = conn.execute("SELECT COUNT(*) FROM dioceses")
    count = cursor.fetchone()[0]
    print(f"\nTotal dioceses in database: {count}")
    
    conn.close()
    return count


if __name__ == '__main__':
    print("=" * 60)
    print("MIGRATING DIOCESES")
    print("=" * 60)
    result = migrate_dioceses()
    print(f"\nMigration complete: {result} dioceses migrated")

