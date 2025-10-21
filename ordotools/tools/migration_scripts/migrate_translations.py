#!/usr/bin/env python3
"""
Migrate translation data from Python files to database.
"""
import sys
import os
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.db import get_connection
from ordotools.tools.translations import Translations


def migrate_translations():
    """Extract translation data from translations.py and insert into database."""
    conn = get_connection()
    
    # Get translations data
    trans = Translations()
    translations_data = trans.translations()
    
    print(f"Found {len(translations_data)} feast IDs with translations to migrate")
    
    migrated = 0
    errors = 0
    
    with conn:
        for feast_id, translations in translations_data.items():
            # Determine feast type: numeric IDs are sanctoral, string IDs are temporal
            # But the translations.py uses numeric keys, so they're sanctoral
            feast_type = 'sanctoral'
            
            for lang_code, translation in translations.items():
                try:
                    # Skip empty translations
                    if not translation or translation.strip() == '':
                        continue
                    
                    # Latin is the default language
                    is_default = 1 if lang_code == 'la' else 0
                    
                    conn.execute(
                        """
                        INSERT OR REPLACE INTO translations (feast_id, feast_type, language_code, translation, is_default)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        (str(feast_id), feast_type, lang_code, translation, is_default)
                    )
                    migrated += 1
                    
                except Exception as e:
                    errors += 1
                    print(f"✗ Error migrating translation for feast {feast_id}, lang {lang_code}: {e}")
            
            if migrated % 100 == 0:
                print(f"  Migrated {migrated} translations...")
    
    # Now add temporal feast translations (using feast IDs as translations)
    # For temporal feasts, we'll need to create basic Latin translations from the IDs
    cursor = conn.execute("SELECT id FROM temporal_feasts")
    temporal_ids = [row[0] for row in cursor.fetchall()]
    
    print(f"\nAdding basic translations for {len(temporal_ids)} temporal feasts...")
    
    with conn:
        for feast_id in temporal_ids:
            try:
                # Check if translation already exists
                cursor = conn.execute(
                    "SELECT id FROM translations WHERE feast_id = ? AND feast_type = 'temporal'",
                    (feast_id,)
                )
                if not cursor.fetchone():
                    # Add a basic Latin translation using the ID itself
                    # This is temporary - proper translations should be added separately
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO translations (feast_id, feast_type, language_code, translation, is_default)
                        VALUES (?, 'temporal', 'la', ?, 1)
                        """,
                        (feast_id, feast_id)  # Using ID as temporary translation
                    )
                    migrated += 1
            except Exception as e:
                errors += 1
                print(f"✗ Error adding temporal translation for {feast_id}: {e}")
    
    # Verify migration
    cursor = conn.execute("SELECT COUNT(*) FROM translations")
    count = cursor.fetchone()[0]
    
    cursor = conn.execute("SELECT COUNT(DISTINCT feast_id) FROM translations")
    unique_feasts = cursor.fetchone()[0]
    
    print(f"\n✓ Successfully migrated: {migrated} translations")
    print(f"✗ Errors: {errors}")
    print(f"Total translations in database: {count}")
    print(f"Unique feasts with translations: {unique_feasts}")
    
    conn.close()
    return migrated


if __name__ == '__main__':
    print("=" * 60)
    print("MIGRATING TRANSLATIONS")
    print("=" * 60)
    result = migrate_translations()
    print(f"\nMigration complete: {result} translations migrated")

