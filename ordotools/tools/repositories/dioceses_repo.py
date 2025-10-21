"""Repository for dioceses and countries data."""
import sqlite3
from typing import Dict, Optional, List
from ordotools.tools.db import get_connection


class DiocesesRepository:
    """Repository for accessing dioceses and countries data from database."""
    
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_country(self, code: str) -> Optional[Dict]:
        """Get country by code."""
        cursor = self.conn.execute(
            "SELECT * FROM countries WHERE code = ?",
            (code,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return dict(row)
    
    def get_country_by_id(self, country_id: int) -> Optional[Dict]:
        """Get country by ID."""
        cursor = self.conn.execute(
            "SELECT * FROM countries WHERE id = ?",
            (country_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return dict(row)
    
    def get_all_countries(self) -> List[Dict]:
        """Get all countries."""
        cursor = self.conn.execute("SELECT * FROM countries")
        return [dict(row) for row in cursor.fetchall()]
    
    def get_diocese(self, code: str) -> Optional[Dict]:
        """Get diocese by code."""
        cursor = self.conn.execute(
            "SELECT * FROM dioceses WHERE code = ?",
            (code,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return dict(row)
    
    def get_diocese_by_id(self, diocese_id: int) -> Optional[Dict]:
        """Get diocese by ID."""
        cursor = self.conn.execute(
            "SELECT * FROM dioceses WHERE id = ?",
            (diocese_id,)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return dict(row)
    
    def get_all_dioceses(self) -> List[Dict]:
        """Get all dioceses."""
        cursor = self.conn.execute("SELECT * FROM dioceses")
        return [dict(row) for row in cursor.fetchall()]
    
    def get_dioceses_by_country(self, country_code: str) -> List[Dict]:
        """Get all dioceses in a country."""
        cursor = self.conn.execute(
            """
            SELECT d.* FROM dioceses d
            JOIN countries c ON d.country_id = c.id
            WHERE c.code = ?
            """,
            (country_code,)
        )
        return [dict(row) for row in cursor.fetchall()]
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

