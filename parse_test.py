import sqlite3

def inspect_db(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    print("--- Database Inspection ---")
    
    # Check language codes
    cur.execute("SELECT DISTINCT language_code FROM translations")
    codes = [row[0] for row in cur.fetchall()]
    print(f"Available Language Codes: {codes}")
    
    # Check feast types
    cur.execute("SELECT DISTINCT feast_type FROM translations")
    types = [row[0] for row in cur.fetchall()]
    print(f"Available Feast Types: {types}")
    
    # Check if any assignments exist
    cur.execute("SELECT COUNT(*) FROM feast_date_assignments")
    count = cur.fetchone()[0]
    print(f"Total Assignments in DB: {count}")
    
    conn.close()

inspect_db("ordotools/ordotools.sqlite3")
