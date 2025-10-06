import json
from datetime import datetime
from typing import Dict

from ordotools.tools.db import get_connection


class SanctoralRepository:
    """
    Simple repository to store and load sanctoral dict data by
    (diocese, year) into SQLite while preserving the existing
    shape expected by the application (date -> properties dict).
    """

    def __init__(self):
        self.conn = get_connection()

    def _has_year(self, diocese: str, year: int) -> bool:
        cur = self.conn.execute(
            "SELECT 1 FROM sanctoral_feasts WHERE diocese=? AND year=? LIMIT 1",
            (diocese, year),
        )
        return cur.fetchone() is not None

    def ensure_year(self, diocese: str, year: int, data: Dict[datetime, dict]) -> None:
        """
        Idempotently insert a year's worth of feasts if not present.
        Keys are datetime dates; values are dicts with an "id" and properties.
        """
        if self._has_year(diocese, year):
            return
        rows = []
        for dt, props in data.items():
            rows.append(
                (
                    year,
                    int(dt.strftime("%m")),
                    int(dt.strftime("%d")),
                    diocese,
                    str(props.get("id")),
                    json.dumps(props, ensure_ascii=False),
                )
            )
        with self.conn:
            self.conn.executemany(
                """
                INSERT OR IGNORE INTO sanctoral_feasts
                (year, month, day, diocese, feast_id, properties)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                rows,
            )

    def load_year(self, diocese: str, year: int) -> Dict[datetime, dict]:
        cur = self.conn.execute(
            "SELECT month, day, properties FROM sanctoral_feasts WHERE diocese=? AND year=?",
            (diocese, year),
        )
        results: Dict[datetime, dict] = {}
        for row in cur.fetchall():
            month = int(row["month"])  # type: ignore[index]
            day = int(row["day"])  # type: ignore[index]
            props = json.loads(row["properties"])  # type: ignore[index]
            results[datetime(year=year, month=month, day=day)] = props
        return results
