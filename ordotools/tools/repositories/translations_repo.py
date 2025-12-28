# import json
# import sqlite3
from typing import Dict, Optional  #, List
# from datetime import datetime
from ordotools.tools.db import get_connection

class TranslationsRepository:
    def __init__(self, db_path: Optional[str] = None):
        self.conn = get_connection(db_path)
    
    def get_all_translations_for_feast(self, feast_id: str) -> Dict[str, str]:
        """IDs are now handled strictly as strings."""
        cursor = self.conn.execute(
            "SELECT language_code, translation FROM translations WHERE feast_id = ?",
            (str(feast_id),)
        )
        return {row[0]: row[1] for row in cursor.fetchall()}

    def get_translation(self, feast_id: str, lang: str) -> Optional[str]:
        cursor = self.conn.execute(
            "SELECT translation FROM translations WHERE feast_id = ? AND language_code = ?",
            (str(feast_id), lang)
        )
        row = cursor.fetchone()
        return row[0] if row else None
