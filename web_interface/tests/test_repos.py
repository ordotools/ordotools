import unittest
import sqlite3
import os
import sys
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ordotools.tools.repositories.temporal_repo import TemporalRepository
from ordotools.tools.repositories.sanctoral_repo import SanctoralRepository

class TestRepositories(unittest.TestCase):
    def setUp(self):
        # Create a temporary database
        self.db_path = os.path.abspath('test_db.sqlite')
        # Ensure clean state if previous run failed
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            
        self.conn = sqlite3.connect(self.db_path)
        self.create_tables()
        
        self.temporal_repo = TemporalRepository(self.db_path)
        self.sanctoral_repo = SanctoralRepository(self.db_path)

    def tearDown(self):
        self.temporal_repo.close()
        self.sanctoral_repo.close()
        self.conn.close()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def create_tables(self):
        # Create minimal schema for testing
        self.conn.execute("""
            CREATE TABLE temporal_feasts (
                id TEXT PRIMARY KEY,
                rank_numeric INTEGER,
                rank_verbose TEXT,
                color TEXT,
                office_type BOOLEAN,
                nobility_1 INTEGER, nobility_2 INTEGER, nobility_3 INTEGER,
                nobility_4 INTEGER, nobility_5 INTEGER, nobility_6 INTEGER,
                mass_properties TEXT, vespers_properties TEXT, matins_properties TEXT,
                lauds_properties TEXT, prime_properties TEXT, little_hours_properties TEXT,
                compline_properties TEXT, com_1_properties TEXT, com_2_properties TEXT,
                com_3_properties TEXT
            )
        """)
        self.conn.execute("""
            CREATE TABLE sanctoral_feasts_new (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                rank_numeric INTEGER,
                rank_verbose TEXT,
                color TEXT,
                office_type BOOLEAN,
                diocese_id INTEGER,
                nobility_1 INTEGER, nobility_2 INTEGER, nobility_3 INTEGER,
                nobility_4 INTEGER, nobility_5 INTEGER, nobility_6 INTEGER,
                mass_properties TEXT, vespers_properties TEXT, matins_properties TEXT,
                lauds_properties TEXT, prime_properties TEXT, little_hours_properties TEXT,
                compline_properties TEXT, com_1_properties TEXT, com_2_properties TEXT,
                com_3_properties TEXT
            )
        """)
        self.conn.execute("""
            CREATE TABLE feast_date_assignments (
                feast_id INTEGER,
                month INTEGER,
                day INTEGER,
                diocese_id INTEGER
            )
        """)
        self.conn.execute("""
            CREATE TABLE dioceses (
                id INTEGER PRIMARY KEY,
                code TEXT,
                name_latin TEXT,
                name_english TEXT,
                country_id INTEGER
            )
        """)
        self.conn.commit()

    def test_temporal_save_and_delete(self):
        feast_data = {
            'id': 'test_feast',
            'rank': [1, 'Double'],
            'color': 'white',
            'office_type': True,
            'mass': {'introit': 'Test Introit'}
        }
        
        # Save
        self.temporal_repo.save_feast(feast_data)
        
        # Retrieve
        saved = self.temporal_repo.get_feast('test_feast')
        self.assertIsNotNone(saved)
        self.assertEqual(saved['rank'][0], 1)
        self.assertEqual(saved['mass']['introit'], 'Test Introit')
        
        # Update
        feast_data['color'] = 'red'
        self.temporal_repo.save_feast(feast_data)
        updated = self.temporal_repo.get_feast('test_feast')
        self.assertEqual(updated['color'], 'red')
        
        # Delete
        self.temporal_repo.delete_feast('test_feast')
        deleted = self.temporal_repo.get_feast('test_feast')
        self.assertIsNone(deleted)

    def test_sanctoral_save_and_delete(self):
        feast_data = {
            'month': 1,
            'day': 1,
            'rank': [2, 'Semidouble'],
            'color': 'white',
            'office_type': False,
            'diocese_source': 'roman'
        }
        
        # Save
        feast_id = self.sanctoral_repo.save_feast(feast_data)
        self.assertIsNotNone(feast_id)
        
        # Retrieve (need to mock get_feast logic or use direct DB check since get_feast is complex)
        cursor = self.conn.execute("SELECT * FROM sanctoral_feasts_new WHERE id = ?", (feast_id,))
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], 2) # rank_numeric
        
        # Check assignment
        cursor = self.conn.execute("SELECT * FROM feast_date_assignments WHERE feast_id = ?", (feast_id,))
        assignment = cursor.fetchone()
        self.assertIsNotNone(assignment)
        self.assertEqual(assignment[1], 1) # month
        
        # Update
        feast_data['id'] = feast_id
        feast_data['color'] = 'red'
        self.sanctoral_repo.save_feast(feast_data)
        
        cursor = self.conn.execute("SELECT color FROM sanctoral_feasts_new WHERE id = ?", (feast_id,))
        self.assertEqual(cursor.fetchone()[0], 'red')
        
        # Delete
        self.sanctoral_repo.delete_feast(feast_id)
        cursor = self.conn.execute("SELECT * FROM sanctoral_feasts_new WHERE id = ?", (feast_id,))
        self.assertIsNone(cursor.fetchone())

if __name__ == '__main__':
    unittest.main()
