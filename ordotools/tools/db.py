import os
import sqlite3
from typing import Optional


def _default_db_path() -> str:
    """Return a default on-disk path for the SQLite database."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, "ordotools.sqlite3")


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """Create (and initialize) a SQLite connection for the sanctoral store."""
    path = db_path or os.environ.get("ORDOTOOLS_DB_PATH", _default_db_path())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    with conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
    init_schema(conn)
    return conn


def init_schema(conn: sqlite3.Connection) -> None:
    """Create tables and indexes if they do not already exist."""
    with conn:
        # Countries table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                name_latin TEXT NOT NULL,
                name_english TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        
        # Dioceses table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS dioceses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                name_latin TEXT NOT NULL,
                name_english TEXT,
                country_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (country_id) REFERENCES countries(id)
            );
            """
        )
        
        # Temporal feasts table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS temporal_feasts (
                id TEXT PRIMARY KEY,
                rank_numeric INTEGER NOT NULL,
                rank_verbose TEXT NOT NULL,
                color TEXT NOT NULL,
                office_type TEXT,
                nobility_1 INTEGER DEFAULT 0,
                nobility_2 INTEGER DEFAULT 0,
                nobility_3 INTEGER DEFAULT 0,
                nobility_4 INTEGER DEFAULT 0,
                nobility_5 INTEGER DEFAULT 0,
                nobility_6 INTEGER DEFAULT 0,
                mass_properties TEXT,
                vespers_properties TEXT,
                matins_properties TEXT,
                lauds_properties TEXT,
                prime_properties TEXT,
                little_hours_properties TEXT,
                compline_properties TEXT,
                com_1_properties TEXT,
                com_2_properties TEXT,
                com_3_properties TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        
        # Sanctoral feasts table (new structure)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sanctoral_feasts_new (
                id INTEGER PRIMARY KEY,
                diocese_id INTEGER,
                rank_numeric INTEGER NOT NULL,
                rank_verbose TEXT NOT NULL,
                color TEXT NOT NULL,
                office_type TEXT,
                nobility_1 INTEGER DEFAULT 0,
                nobility_2 INTEGER DEFAULT 0,
                nobility_3 INTEGER DEFAULT 0,
                nobility_4 INTEGER DEFAULT 0,
                nobility_5 INTEGER DEFAULT 0,
                nobility_6 INTEGER DEFAULT 0,
                mass_properties TEXT,
                vespers_properties TEXT,
                matins_properties TEXT,
                lauds_properties TEXT,
                prime_properties TEXT,
                little_hours_properties TEXT,
                compline_properties TEXT,
                com_1_properties TEXT,
                com_2_properties TEXT,
                com_3_properties TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (diocese_id) REFERENCES dioceses(id)
            );
            """
        )
        
        # Feast date assignments table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS feast_date_assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feast_id INTEGER NOT NULL,
                month INTEGER NOT NULL,
                day INTEGER NOT NULL,
                diocese_id INTEGER,
                UNIQUE(feast_id, month, day, diocese_id),
                FOREIGN KEY (feast_id) REFERENCES sanctoral_feasts_new(id),
                FOREIGN KEY (diocese_id) REFERENCES dioceses(id)
            );
            """
        )
        
        # Translations table
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS translations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                feast_id TEXT NOT NULL,
                feast_type TEXT NOT NULL,
                language_code TEXT NOT NULL,
                translation TEXT NOT NULL,
                is_default INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(feast_id, feast_type, language_code)
            );
            """
        )
        
        # Legacy table for backward compatibility (keep temporarily)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS sanctoral_feasts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year INTEGER NOT NULL,
                month INTEGER NOT NULL,
                day INTEGER NOT NULL,
                diocese TEXT NOT NULL,
                feast_id TEXT NOT NULL,
                properties TEXT NOT NULL,
                UNIQUE(year, month, day, diocese)
            );
            """
        )
        
        # Indexes
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_sanctoral_lookup
            ON sanctoral_feasts(year, diocese);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_temporal_id
            ON temporal_feasts(id);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_sanctoral_new_diocese
            ON sanctoral_feasts_new(diocese_id);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_feast_dates
            ON feast_date_assignments(month, day, diocese_id);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_translations_lookup
            ON translations(feast_id, feast_type, language_code);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_dioceses_code
            ON dioceses(code);
            """
        )
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_countries_code
            ON countries(code);
            """
        )
