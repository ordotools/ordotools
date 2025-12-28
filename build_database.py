import yaml
import json
import sqlite3
from pathlib import Path
from ordotools.tools.db import get_connection

def build_from_yaml(data_dir="data"):
    conn = get_connection()
    cur = conn.cursor()

    print("🧹 Clearing existing data...")
    cur.execute("PRAGMA foreign_keys = OFF")
    for table in ["feast_date_assignments", "translations", "feasts", "dioceses", "countries"]:
        cur.execute(f"DELETE FROM {table}")
    cur.execute("PRAGMA foreign_keys = ON")

    data_path = Path(data_dir)
    yaml_files = list(data_path.glob("**/*.yaml"))

    for yfile in yaml_files:
        with open(yfile, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            
        is_temporal = "cycle" in data
        source_name = data.get("diocese_name") or data.get("cycle")
        print(f"🏗️  Building: {source_name}")

        # Metadata for Sanctoral files
        diocese_id = None
        if not is_temporal:
            country = data.get("country", "Universal")
            cur.execute("INSERT OR IGNORE INTO countries (name_english) VALUES (?)", (country,))
            cur.execute("SELECT id FROM countries WHERE name_english = ?", (country,))
            country_id = cur.fetchone()[0]

            cur.execute("INSERT OR IGNORE INTO dioceses (country_id, name_english) VALUES (?, ?)", (country_id, source_name))
            cur.execute("SELECT id FROM dioceses WHERE name_english = ?", (source_name,))
            diocese_id = cur.fetchone()[0]

        for feast in data.get("feasts", []):
            try:
                # FIX: Use .get('id') to avoid KeyError
                f_id = feast.get('id')
                if f_id is None:
                    print(f"   ⚠️ Skipping feast in {source_name}: No ID found.")
                    continue

                # 1. Insert Core Feast Data
                cur.execute("""
                    INSERT OR IGNORE INTO feasts 
                    (id, rank_verbose, rank_numeric, color, office_type, mass_properties, nobility)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    str(f_id), feast['rank_verbose'], feast['rank_numeric'], feast['color'],
                    str(feast.get('office_type', 'False')), json.dumps(feast.get('mass_properties')),
                    json.dumps(feast.get('nobility', []))
                ))

                # 2. Insert Translations
                f_type = 'temporal' if is_temporal else 'sanctoral'
                for lang, text in feast.get('name_translations', {}).items():
                    cur.execute("INSERT INTO translations (feast_id, language_code, translation, feast_type) VALUES (?, ?, ?, ?)", 
                                (str(f_id), lang, text, f_type))

                # 3. Insert Assignments
                if not is_temporal and diocese_id and 'date' in feast:
                    month, day = map(int, feast['date'].split('-'))
                    cur.execute("INSERT INTO feast_date_assignments (diocese_id, feast_id, month, day) VALUES (?, ?, ?, ?)", 
                                (diocese_id, str(f_id), month, day))

            except Exception as e:
                print(f"   ❌ Fatal error on feast {feast.get('id')}: {e}")

    conn.commit()
    conn.close()
    print("\n✨ Database successfully rebuilt.")

if __name__ == "__main__":
    build_from_yaml()
