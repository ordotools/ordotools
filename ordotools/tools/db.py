import os
import sqlite3
from typing import Optional


def _default_db_path() -> str:
    """Return a default on-disk path for the SQLite database."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, "sanctoral.sqlite3")


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
        conn.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_sanctoral_lookup
            ON sanctoral_feasts(year, diocese);
            """
        )
