"""Repository for translations data."""
import sqlite3
from typing import Dict, Optional, List
from ordotools.tools.db import get_connection


class TranslationsRepository:
    """Repository for accessing feast name translations from database."""
    
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_translation(self, feast_id: str, feast_type: str, language_code: str) -> Optional[str]:
        """Get a specific translation for a feast."""
        cursor = self.conn.execute(
            """
            SELECT translation FROM translations
            WHERE feast_id = ? AND feast_type = ? AND language_code = ?
            """,
            (str(feast_id), feast_type, language_code)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return row[0]
    
    def get_all_translations_for_feast(self, feast_id: str, feast_type: str) -> Dict[str, str]:
        """Get all translations for a feast."""
        cursor = self.conn.execute(
            """
            SELECT language_code, translation FROM translations
            WHERE feast_id = ? AND feast_type = ?
            """,
            (str(feast_id), feast_type)
        )
        return {row[0]: row[1] for row in cursor.fetchall()}
    
    def get_default_translation(self, feast_id: str, feast_type: str) -> Optional[str]:
        """Get the default (Latin) translation for a feast."""
        cursor = self.conn.execute(
            """
            SELECT translation FROM translations
            WHERE feast_id = ? AND feast_type = ? AND is_default = 1
            LIMIT 1
            """,
            (str(feast_id), feast_type)
        )
        row = cursor.fetchone()
        if not row:
            return None
        return row[0]
    
    def get_all_translations(self, language_code: str = 'la') -> Dict[str, str]:
        """Get all translations for a specific language, keyed by feast_id."""
        cursor = self.conn.execute(
            """
            SELECT feast_id, feast_type, translation FROM translations
            WHERE language_code = ?
            """,
            (language_code,)
        )
        # Return dictionary keyed by feast_id (as string or int depending on type)
        results = {}
        for row in cursor.fetchall():
            feast_id = row[0]
            # Convert to int if it's a sanctoral feast (numeric ID)
            if row[1] == 'sanctoral':
                try:
                    feast_id = int(feast_id)
                except ValueError:
                    pass
            results[feast_id] = row[2]
        return results
    
    def get_translations_by_type(self, feast_type: str, language_code: str = 'la') -> Dict[str, str]:
        """Get all translations for a specific feast type and language."""
        cursor = self.conn.execute(
            """
            SELECT feast_id, translation FROM translations
            WHERE feast_type = ? AND language_code = ?
            """,
            (feast_type, language_code)
        )
        # Return dictionary keyed by feast_id
        results = {}
        for row in cursor.fetchall():
            feast_id = row[0]
            # Convert to int if it's a sanctoral feast
            if feast_type == 'sanctoral':
                try:
                    feast_id = int(feast_id)
                except ValueError:
                    pass
            results[feast_id] = row[1]
        return results
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()

