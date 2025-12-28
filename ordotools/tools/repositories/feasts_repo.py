"""Repository for all feast data (Sanctoral and Temporal)."""
import json
import sqlite3
from typing import Dict, Optional, List
from datetime import datetime
from ordotools.tools.db import get_connection

class FeastsRepository:
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_feast(self, feast_id: str) -> Optional[Dict]:
        """Get a single feast by ID (numeric string or temporal name)."""
        cursor = self.conn.execute("SELECT * FROM feasts WHERE id = ?", (feast_id,))
        row = cursor.fetchone()
        return self._row_to_dict(row) if row else None
    
    def get_feasts_for_date(self, month: int, day: int, diocese_name: str = 'Roman') -> List[Dict]:
        """Get feasts for a date, resolving Diocese -> Country -> Roman priority."""
        cursor = self.conn.execute(
            """
            SELECT f.* FROM feasts f
            JOIN feast_date_assignments fda ON f.id = fda.feast_id
            JOIN dioceses d ON fda.diocese_id = d.id
            WHERE fda.month = ? AND fda.day = ? 
            AND (d.name_english = ? OR d.name_english = 'Roman')
            ORDER BY CASE WHEN d.name_english = ? THEN 1 ELSE 2 END ASC, f.rank_numeric ASC
            """,
            (month, day, diocese_name, diocese_name)
        )
        return [self._row_to_dict(row) for row in cursor.fetchall()]

    def _row_to_dict(self, row: sqlite3.Row) -> Dict:
        """Convert new schema row to dictionary with parsed JSON."""
        return {
            'id': row['id'],
            'rank': [row['rank_numeric'], row['rank_verbose']],
            'color': row['color'],
            'office_type': row['office_type'] if row['office_type'] != 'False' else False,
            'mass_properties': json.loads(row['mass_properties']) if row['mass_properties'] else {},
            'alt_mass_properties': json.loads(row['alt_mass_properties']) if row['alt_mass_properties'] else {},
            'nobility': json.loads(row['nobility']) if row['nobility'] else []
        }

    def save_feast(self, feast_data: Dict):
        """Insert or update a feast using the unified schema."""
        self.conn.execute(
            """
            INSERT INTO feasts (id, rank_verbose, rank_numeric, color, office_type, mass_properties, alt_mass_properties, nobility)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                rank_verbose=excluded.rank_verbose, rank_numeric=excluded.rank_numeric,
                color=excluded.color, office_type=excluded.office_type,
                mass_properties=excluded.mass_properties, alt_mass_properties=excluded.alt_mass_properties,
                nobility=excluded.nobility
            """,
            (
                str(feast_data['id']), feast_data['rank'][1], feast_data['rank'][0], 
                feast_data['color'], str(feast_data.get('office_type', False)),
                json.dumps(feast_data.get('mass_properties', {})),
                json.dumps(feast_data.get('alt_mass_properties', {})),
                json.dumps(feast_data.get('nobility', []))
            )
        )
        self.conn.commit()
