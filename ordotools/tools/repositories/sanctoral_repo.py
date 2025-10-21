"""Repository for sanctoral feasts data."""
import json
import sqlite3
from typing import Dict, Optional, List
from datetime import datetime
from ordotools.tools.db import get_connection


class SanctoralRepository:
    """Repository for accessing sanctoral feast data from database."""
    
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_feast(self, feast_id: int, diocese_code: Optional[str] = None) -> Optional[Dict]:
        """Get a single sanctoral feast by ID."""
        if diocese_code:
            cursor = self.conn.execute(
                """
                SELECT sf.* FROM sanctoral_feasts_new sf
                JOIN dioceses d ON sf.diocese_id = d.id
                WHERE sf.id = ? AND d.code = ?
                """,
                (feast_id, diocese_code)
            )
        else:
            cursor = self.conn.execute(
                """
                SELECT * FROM sanctoral_feasts_new
                WHERE id = ? AND diocese_id IS NULL
                """,
                (feast_id,)
            )
        
        row = cursor.fetchone()
        if not row:
            return None
        return self._row_to_dict(row)
    
    def get_feasts_for_date(self, month: int, day: int, diocese_code: str = 'roman') -> List[Dict]:
        """Get all feasts for a specific date and diocese."""
        if diocese_code == 'roman':
            # Get universal Roman feasts
            cursor = self.conn.execute(
                """
                SELECT sf.* FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                WHERE fda.month = ? AND fda.day = ? AND fda.diocese_id IS NULL
                """,
                (month, day)
            )
        else:
            # Get diocese-specific and Roman feasts
            cursor = self.conn.execute(
                """
                SELECT sf.* FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                LEFT JOIN dioceses d ON fda.diocese_id = d.id
                WHERE fda.month = ? AND fda.day = ? 
                AND (fda.diocese_id IS NULL OR d.code = ?)
                """,
                (month, day, diocese_code)
            )
        
        return [self._row_to_dict(row) for row in cursor.fetchall()]
    
    def get_year_calendar(self, diocese_code: str = 'roman') -> Dict[datetime, Dict]:
        """Get all feasts for a diocese as a calendar dictionary."""
        # Dummy year for date keys (will be replaced by caller with actual year)
        year = 2024
        
        if diocese_code == 'roman':
            cursor = self.conn.execute(
                """
                SELECT sf.*, fda.month, fda.day
                FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                WHERE fda.diocese_id IS NULL
                ORDER BY fda.month, fda.day
                """
            )
        else:
            # Get diocese ID
            diocese_cursor = self.conn.execute(
                "SELECT id FROM dioceses WHERE code = ?",
                (diocese_code,)
            )
            diocese_row = diocese_cursor.fetchone()
            if not diocese_row:
                return {}
            diocese_id = diocese_row[0]
            
            cursor = self.conn.execute(
                """
                SELECT sf.*, fda.month, fda.day
                FROM sanctoral_feasts_new sf
                JOIN feast_date_assignments fda ON sf.id = fda.feast_id
                WHERE fda.diocese_id IS NULL OR fda.diocese_id = ?
                ORDER BY fda.month, fda.day
                """,
                (diocese_id,)
            )
        
        calendar = {}
        for row in cursor.fetchall():
            month = row['month']
            day = row['day']
            date_key = datetime(year=year, month=month, day=day)
            feast_dict = self._row_to_dict(row)
            calendar[date_key] = feast_dict
        
        return calendar
    
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
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

