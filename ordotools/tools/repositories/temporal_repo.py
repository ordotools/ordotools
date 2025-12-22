"""Repository for temporal feasts data."""
import json
import sqlite3
from typing import Dict, Optional
from ordotools.tools.db import get_connection


class TemporalRepository:
    """Repository for accessing temporal feast data from database."""
    
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_feast(self, feast_id: str) -> Optional[Dict]:
        """Get a single temporal feast by ID."""
        cursor = self.conn.execute(
            """
            SELECT * FROM temporal_feasts WHERE id = ?
            """,
            (feast_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return self._row_to_dict(row)
    
    def get_all_feasts(self) -> Dict[str, Dict]:
        """Get all temporal feasts."""
        cursor = self.conn.execute("SELECT * FROM temporal_feasts")
        feasts = {}
        for row in cursor.fetchall():
            feast_dict = self._row_to_dict(row)
            feasts[feast_dict['id']] = feast_dict
        return feasts
    
    def _row_to_dict(self, row: sqlite3.Row) -> Dict:
        """Convert database row to feast dictionary format."""
        # Parse JSON fields
        mass = json.loads(row['mass_properties']) if row['mass_properties'] else {}
        vespers = json.loads(row['vespers_properties']) if row['vespers_properties'] else {}
        matins = json.loads(row['matins_properties']) if row['matins_properties'] else {}
        lauds = json.loads(row['lauds_properties']) if row['lauds_properties'] else {}
        prime = json.loads(row['prime_properties']) if row['prime_properties'] else {}
        little_hours = json.loads(row['little_hours_properties']) if row['little_hours_properties'] else {}
        compline = json.loads(row['compline_properties']) if row['compline_properties'] else {}
        com_1 = json.loads(row['com_1_properties']) if row['com_1_properties'] else {}
        com_2 = json.loads(row['com_2_properties']) if row['com_2_properties'] else {}
        com_3 = json.loads(row['com_3_properties']) if row['com_3_properties'] else {}
        
        # Convert office_type None back to False for compatibility
        office_type = row['office_type']
        if office_type is None:
            office_type = False
        
        return {
            'id': row['id'],
            'rank': [row['rank_numeric'], row['rank_verbose']],
            'color': row['color'],
            'office_type': office_type,
            'nobility': (
                row['nobility_1'], row['nobility_2'], row['nobility_3'],
                row['nobility_4'], row['nobility_5'], row['nobility_6']
            ),
            'mass': mass,
            'vespers': vespers,
            'matins': matins,
            'lauds': lauds,
            'prime': prime,
            'little_hours': little_hours,
            'compline': compline,
            'com_1': com_1,
            'com_2': com_2,
            'com_3': com_3,
        }
    
    def save_feast(self, feast_data: Dict):
        """Save a temporal feast (insert or update)."""
        # Prepare JSON fields
        mass = json.dumps(feast_data.get('mass', {}))
        vespers = json.dumps(feast_data.get('vespers', {}))
        matins = json.dumps(feast_data.get('matins', {}))
        lauds = json.dumps(feast_data.get('lauds', {}))
        prime = json.dumps(feast_data.get('prime', {}))
        little_hours = json.dumps(feast_data.get('little_hours', {}))
        compline = json.dumps(feast_data.get('compline', {}))
        com_1 = json.dumps(feast_data.get('com_1', {}))
        com_2 = json.dumps(feast_data.get('com_2', {}))
        com_3 = json.dumps(feast_data.get('com_3', {}))
        
        # Handle office_type boolean/None
        office_type = feast_data.get('office_type')
        if office_type is False:
            office_type = None
            
        nobility = feast_data.get('nobility', (None, None, None, None, None, None))
        
        # Check if exists
        exists = self.get_feast(feast_data['id'])
        
        if exists:
            self.conn.execute(
                """
                UPDATE temporal_feasts SET
                    rank_numeric = ?, rank_verbose = ?, color = ?, office_type = ?,
                    nobility_1 = ?, nobility_2 = ?, nobility_3 = ?,
                    nobility_4 = ?, nobility_5 = ?, nobility_6 = ?,
                    mass_properties = ?, vespers_properties = ?, matins_properties = ?,
                    lauds_properties = ?, prime_properties = ?, little_hours_properties = ?,
                    compline_properties = ?, com_1_properties = ?, com_2_properties = ?,
                    com_3_properties = ?
                WHERE id = ?
                """,
                (
                    feast_data['rank'][0], feast_data['rank'][1], feast_data['color'], office_type,
                    nobility[0], nobility[1], nobility[2], nobility[3], nobility[4], nobility[5],
                    mass, vespers, matins, lauds, prime, little_hours, compline,
                    com_1, com_2, com_3,
                    feast_data['id']
                )
            )
        else:
            self.conn.execute(
                """
                INSERT INTO temporal_feasts (
                    id, rank_numeric, rank_verbose, color, office_type,
                    nobility_1, nobility_2, nobility_3, nobility_4, nobility_5, nobility_6,
                    mass_properties, vespers_properties, matins_properties,
                    lauds_properties, prime_properties, little_hours_properties,
                    compline_properties, com_1_properties, com_2_properties, com_3_properties
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    feast_data['id'], feast_data['rank'][0], feast_data['rank'][1], feast_data['color'], office_type,
                    nobility[0], nobility[1], nobility[2], nobility[3], nobility[4], nobility[5],
                    mass, vespers, matins, lauds, prime, little_hours, compline,
                    com_1, com_2, com_3
                )
            )
        self.conn.commit()

    def delete_feast(self, feast_id: str):
        """Delete a temporal feast."""
        self.conn.execute("DELETE FROM temporal_feasts WHERE id = ?", (feast_id,))
        self.conn.commit()

    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

