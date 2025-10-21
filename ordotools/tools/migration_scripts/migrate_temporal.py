#!/usr/bin/env python3
"""
Migrate temporal feast data from Python files to database.
"""
import sys
import os
import json
from pathlib import Path

# Add parent directories to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from ordotools.tools.db import get_connection
from ordotools.tools.temporal_data import TemporalData


def serialize_property(prop):
    """Convert property to JSON string if it's a dict/list, otherwise return empty string."""
    if prop is None:
        return None
    if isinstance(prop, (dict, list)):
        return json.dumps(prop, ensure_ascii=False)
    return None


def migrate_temporal_feasts():
    """Extract temporal feast data from temporal_data.py and insert into database."""
    conn = get_connection()
    
    # Get all temporal data
    temporal_data = TemporalData()
    all_feasts = temporal_data.data
    
    print(f"Found {len(all_feasts)} temporal feasts to migrate")
    
    migrated = 0
    errors = 0
    
    with conn:
        for feast_id, feast_data in all_feasts.items():
            try:
                # Extract rank info
                rank = feast_data.get('rank', [0, ''])
                rank_numeric = rank[0] if len(rank) > 0 else 0
                rank_verbose = rank[1] if len(rank) > 1 else ''
                
                # Extract nobility tuple
                nobility = feast_data.get('nobility', (0, 0, 0, 0, 0, 0))
                nobility_values = list(nobility) + [0] * (6 - len(nobility))  # Pad to 6 values
                
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
                
                # Handle office_type - can be string or boolean
                office_type = feast_data.get('office_type')
                if office_type is False:
                    office_type = None
                elif isinstance(office_type, str):
                    office_type = office_type
                else:
                    office_type = None
                
                conn.execute(
                    """
                    INSERT OR REPLACE INTO temporal_feasts (
                        id, rank_numeric, rank_verbose, color, office_type,
                        nobility_1, nobility_2, nobility_3, nobility_4, nobility_5, nobility_6,
                        mass_properties, vespers_properties, matins_properties,
                        lauds_properties, prime_properties, little_hours_properties,
                        compline_properties, com_1_properties, com_2_properties, com_3_properties
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        feast_id, rank_numeric, rank_verbose, feast_data.get('color', ''), office_type,
                        nobility_values[0], nobility_values[1], nobility_values[2],
                        nobility_values[3], nobility_values[4], nobility_values[5],
                        mass_prop, vespers_prop, matins_prop, lauds_prop, prime_prop,
                        little_hours_prop, compline_prop, com_1_prop, com_2_prop, com_3_prop
                    )
                )
                migrated += 1
                if migrated % 50 == 0:
                    print(f"  Migrated {migrated} feasts...")
            except Exception as e:
                errors += 1
                print(f"✗ Error migrating feast {feast_id}: {e}")
    
    # Verify migration
    cursor = conn.execute("SELECT COUNT(*) FROM temporal_feasts")
    count = cursor.fetchone()[0]
    print(f"\n✓ Successfully migrated: {migrated} feasts")
    print(f"✗ Errors: {errors}")
    print(f"Total temporal feasts in database: {count}")
    
    conn.close()
    return migrated


if __name__ == '__main__':
    print("=" * 60)
    print("MIGRATING TEMPORAL FEASTS")
    print("=" * 60)
    result = migrate_temporal_feasts()
    print(f"\nMigration complete: {result} temporal feasts migrated")

