#!/usr/bin/env python3
"""
Migrate sanctoral feast data from Python files to database.
"""
import sys
import os
import json
from pathlib import Path
from datetime import datetime

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.db import get_connection
from ordotools.sanctoral.diocese import roman
import glob
import importlib


def serialize_property(prop):
    """Convert property to JSON string if it's a dict/list, otherwise return empty string."""
    if prop is None:
        return None
    if isinstance(prop, (dict, list)):
        return json.dumps(prop, ensure_ascii=False)
    return None


def migrate_roman_sanctoral():
    """Migrate Roman sanctoral calendar."""
    conn = get_connection()
    
    # Get roman diocese ID
    cursor = conn.execute("SELECT id FROM dioceses WHERE code = 'roman'")
    roman_diocese_row = cursor.fetchone()
    if not roman_diocese_row:
        print("✗ Error: Roman diocese not found in database!")
        return 0
    roman_diocese_id = roman_diocese_row[0]
    
    # Get roman sanctoral data
    sanctoral = roman.Sanctoral(2024)  # Year doesn't matter for structure
    feasts_data = sanctoral.data
    
    print(f"Found {len(feasts_data)} Roman sanctoral feasts to migrate")
    
    migrated_feasts = 0
    migrated_dates = 0
    errors = 0
    
    with conn:
        for date_obj, feast_data in feasts_data.items():
            try:
                feast_id = feast_data.get('id')
                
                # Check if feast already exists (it might be used across multiple dates)
                cursor = conn.execute(
                    "SELECT id FROM sanctoral_feasts_new WHERE id = ?",
                    (feast_id,)
                )
                existing = cursor.fetchone()
                
                if not existing:
                    # Extract rank info
                    rank = feast_data.get('rank', [0, ''])
                    rank_numeric = rank[0] if len(rank) > 0 else 0
                    rank_verbose = rank[1] if len(rank) > 1 else ''
                    
                    # Extract nobility tuple
                    nobility = feast_data.get('nobility', (0, 0, 0, 0, 0, 0))
                    nobility_values = list(nobility) + [0] * (6 - len(nobility))
                    
                    # Serialize complex properties
                    mass_prop = serialize_property(feast_data.get('mass'))
                    vespers_prop = serialize_property(feast_data.get('vespers'))
                    matins_prop = serialize_property(feast_data.get('matins'))
                    lauds_prop = serialize_property(feast_data.get('lauds'))
                    prime_prop = serialize_property(feast_data.get('prime'))
                    little_hours_prop = serialize_property(feast_data.get('little_hours'))
                    compline_prop = serialize_property(feast_data.get('compline'))
                    com_1_prop = serialize_property(feast_data.get('com_1'))
                    com_2_prop = serialize_property(feast_data.get('com_2'))
                    com_3_prop = serialize_property(feast_data.get('com_3'))
                    
                    # Handle office_type
                    office_type = feast_data.get('office_type')
                    if office_type is False:
                        office_type = None
                    elif isinstance(office_type, str):
                        office_type = office_type
                    else:
                        office_type = None
                    
                    # Insert feast
                    conn.execute(
                        """
                        INSERT INTO sanctoral_feasts_new (
                            id, diocese_id, rank_numeric, rank_verbose, color, office_type,
                            nobility_1, nobility_2, nobility_3, nobility_4, nobility_5, nobility_6,
                            mass_properties, vespers_properties, matins_properties,
                            lauds_properties, prime_properties, little_hours_properties,
                            compline_properties, com_1_properties, com_2_properties, com_3_properties
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            feast_id, None, rank_numeric, rank_verbose, 
                            feast_data.get('color', ''), office_type,
                            nobility_values[0], nobility_values[1], nobility_values[2],
                            nobility_values[3], nobility_values[4], nobility_values[5],
                            mass_prop, vespers_prop, matins_prop, lauds_prop, prime_prop,
                            little_hours_prop, compline_prop, com_1_prop, com_2_prop, com_3_prop
                        )
                    )
                    migrated_feasts += 1
                
                # Insert date assignment for Roman calendar
                conn.execute(
                    """
                    INSERT OR IGNORE INTO feast_date_assignments (feast_id, month, day, diocese_id)
                    VALUES (?, ?, ?, NULL)
                    """,
                    (feast_id, date_obj.month, date_obj.day)
                )
                migrated_dates += 1
                
                if migrated_feasts % 50 == 0 and migrated_feasts > 0:
                    print(f"  Migrated {migrated_feasts} feasts, {migrated_dates} date assignments...")
                    
            except Exception as e:
                errors += 1
                print(f"✗ Error migrating feast on {date_obj}: {e}")
    
    print(f"\n✓ Successfully migrated: {migrated_feasts} unique feasts")
    print(f"✓ Successfully migrated: {migrated_dates} date assignments")
    print(f"✗ Errors: {errors}")
    
    conn.close()
    return migrated_feasts


def migrate_diocese_sanctoral():
    """Migrate diocese-specific sanctoral calendars."""
    conn = get_connection()
    
    # Get diocese mapping
    cursor = conn.execute("SELECT id, code FROM dioceses WHERE code != 'roman'")
    dioceses = {row[1]: row[0] for row in cursor.fetchall()}
    
    total_migrated = 0
    
    for diocese_code, diocese_id in dioceses.items():
        try:
            # Import the diocese module
            module = importlib.import_module(f'ordotools.sanctoral.diocese.{diocese_code}')
            diocese_obj = module.Diocese(2024)
            
            # Get only local data (not the combined calendar)
            local_data = diocese_obj.data
            
            print(f"\nProcessing diocese: {diocese_code} ({len(local_data)} local feasts)")
            
            migrated = 0
            with conn:
                for date_obj, feast_data in local_data.items():
                    try:
                        feast_id = feast_data.get('id')
                        
                        # Check if feast already exists
                        cursor = conn.execute(
                            "SELECT id FROM sanctoral_feasts_new WHERE id = ? AND diocese_id = ?",
                            (feast_id, diocese_id)
                        )
                        existing = cursor.fetchone()
                        
                        if not existing:
                            # Extract rank info
                            rank = feast_data.get('rank', [0, ''])
                            rank_numeric = rank[0] if len(rank) > 0 else 0
                            rank_verbose = rank[1] if len(rank) > 1 else ''
                            
                            # Extract nobility
                            nobility = feast_data.get('nobility', (0, 0, 0, 0, 0, 0))
                            nobility_values = list(nobility) + [0] * (6 - len(nobility))
                            
                            # Serialize properties
                            mass_prop = serialize_property(feast_data.get('mass'))
                            vespers_prop = serialize_property(feast_data.get('vespers'))
                            matins_prop = serialize_property(feast_data.get('matins'))
                            lauds_prop = serialize_property(feast_data.get('lauds'))
                            prime_prop = serialize_property(feast_data.get('prime'))
                            little_hours_prop = serialize_property(feast_data.get('little_hours'))
                            compline_prop = serialize_property(feast_data.get('compline'))
                            com_1_prop = serialize_property(feast_data.get('com_1'))
                            com_2_prop = serialize_property(feast_data.get('com_2'))
                            com_3_prop = serialize_property(feast_data.get('com_3'))
                            
                            # Handle office_type
                            office_type = feast_data.get('office_type')
                            if office_type is False:
                                office_type = None
                            
                            # Insert feast
                            conn.execute(
                                """
                                INSERT INTO sanctoral_feasts_new (
                                    id, diocese_id, rank_numeric, rank_verbose, color, office_type,
                                    nobility_1, nobility_2, nobility_3, nobility_4, nobility_5, nobility_6,
                                    mass_properties, vespers_properties, matins_properties,
                                    lauds_properties, prime_properties, little_hours_properties,
                                    compline_properties, com_1_properties, com_2_properties, com_3_properties
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                """,
                                (
                                    feast_id, diocese_id, rank_numeric, rank_verbose,
                                    feast_data.get('color', ''), office_type,
                                    nobility_values[0], nobility_values[1], nobility_values[2],
                                    nobility_values[3], nobility_values[4], nobility_values[5],
                                    mass_prop, vespers_prop, matins_prop, lauds_prop, prime_prop,
                                    little_hours_prop, compline_prop, com_1_prop, com_2_prop, com_3_prop
                                )
                            )
                        
                        # Insert date assignment
                        conn.execute(
                            """
                            INSERT OR IGNORE INTO feast_date_assignments (feast_id, month, day, diocese_id)
                            VALUES (?, ?, ?, ?)
                            """,
                            (feast_id, date_obj.month, date_obj.day, diocese_id)
                        )
                        migrated += 1
                        
                    except Exception as e:
                        print(f"✗ Error migrating feast in {diocese_code}: {e}")
            
            print(f"  ✓ Migrated {migrated} feasts for {diocese_code}")
            total_migrated += migrated
            
        except Exception as e:
            print(f"✗ Error processing diocese {diocese_code}: {e}")
    
    conn.close()
    return total_migrated


if __name__ == '__main__':
    print("=" * 60)
    print("MIGRATING SANCTORAL FEASTS")
    print("=" * 60)
    
    print("\n[1/2] Migrating Roman Sanctoral Calendar...")
    roman_count = migrate_roman_sanctoral()
    
    print("\n[2/2] Migrating Diocese-Specific Calendars...")
    diocese_count = migrate_diocese_sanctoral()
    
    print("\n" + "=" * 60)
    print(f"Migration complete:")
    print(f"  Roman feasts: {roman_count}")
    print(f"  Diocese feasts: {diocese_count}")
    print(f"  Total: {roman_count + diocese_count}")
    print("=" * 60)

