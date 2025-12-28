import os
import sqlite3
from typing import Optional

def _default_db_path() -> str:
    """Return the absolute path to the database within the package folder."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "ordotools.sqlite3")

def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    path = db_path or os.environ.get("ORDOTOOLS_DB_PATH", _default_db_path())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    with conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
    init_db(conn)
    return conn

def init_db(conn: sqlite3.Connection):
    """Initializes the schema using the unified 'feasts' table name."""
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS countries (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_english TEXT UNIQUE, 
            name_latin TEXT,
            code TEXT
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS dioceses (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            country_id INTEGER, 
            name_english TEXT UNIQUE, 
            name_latin TEXT,
            code TEXT,
            FOREIGN KEY(country_id) REFERENCES countries(id)
        )
    """)

    # Unified table for both Sanctoral and Temporal data
    cur.execute("""
        CREATE TABLE IF NOT EXISTS feasts (
            id TEXT PRIMARY KEY, 
            rank_verbose TEXT,
            rank_numeric INTEGER,
            color TEXT,
            office_type TEXT,
            mass_properties TEXT, -- JSON string
            alt_mass_properties TEXT, -- JSON string
            nobility TEXT -- JSON list
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS translations (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            feast_id TEXT, 
            language_code TEXT, 
            translation TEXT,
            is_default INTEGER DEFAULT 1,
            feast_type TEXT,
            FOREIGN KEY(feast_id) REFERENCES feasts(id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS feast_date_assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            diocese_id INTEGER, 
            feast_id TEXT, 
            month INTEGER, 
            day INTEGER,
            FOREIGN KEY(diocese_id) REFERENCES dioceses(id),
            FOREIGN KEY(feast_id) REFERENCES feasts(id)
        )
    """)
    conn.commit()
