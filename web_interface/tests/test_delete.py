import unittest
import os
import sys
import tempfile

# Set environment variable for test database BEFORE importing app
# This ensures that when app calls get_connection(), it uses our test DB
test_db_path = os.path.join(tempfile.gettempdir(), 'ordotools_test_delete.sqlite')
os.environ['ORDOTOOLS_DB_PATH'] = test_db_path

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Add root directory to path to import ordotools
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app import app, get_repositories
from ordotools.tools.db import get_connection

class TestDeleteRoutes(unittest.TestCase):
    def setUp(self):
        # Ensure clean DB
        if os.path.exists(test_db_path):
            os.remove(test_db_path)
            
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        
        # Initialize DB
        self.conn = get_connection(test_db_path)
        
        # Create test data
        self.repos = get_repositories()
        
        # Create dummy temporal feast
        self.temp_id = 'test_delete_temp'
        self.repos['temporal'].save_feast({
            'id': self.temp_id,
            'rank': [4, 'Feria'],
            'color': 'green',
            'office_type': False,
            'nobility': (None,)*6,
            'mass': {}, 'vespers': {}, 'matins': {}, 'lauds': {}, 
            'prime': {}, 'little_hours': {}, 'compline': {}, 
            'com_1': {}, 'com_2': {}, 'com_3': {}
        })
        
        # Create dummy sanctoral feast
        self.sanc_id = self.repos['sanctoral'].save_feast({
            'month': 1,
            'day': 1,
            'diocese_source': 'roman',
            'rank': [4, 'Feria'],
            'color': 'green',
            'office_type': False,
            'nobility': (None,)*6,
            'mass': {}, 'vespers': {}, 'matins': {}, 'lauds': {}, 
            'prime': {}, 'little_hours': {}, 'compline': {}, 
            'com_1': {}, 'com_2': {}, 'com_3': {}
        })

    def tearDown(self):
        self.conn.close()
        self.app_context.pop()
        if os.path.exists(test_db_path):
            os.remove(test_db_path)

    def test_delete_temporal(self):
        # Verify it exists
        self.assertIsNotNone(self.repos['temporal'].get_feast(self.temp_id))
        
        # Delete it
        response = self.client.post(f'/temporal/{self.temp_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Temporal feast deleted successfully', response.data)
        
        # Verify it's gone
        self.assertIsNone(self.repos['temporal'].get_feast(self.temp_id))

    def test_delete_sanctoral(self):
        # Verify it exists
        self.assertIsNotNone(self.repos['sanctoral'].get_feast(self.sanc_id))
        
        # Delete it
        response = self.client.post(f'/sanctoral/{self.sanc_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sanctoral feast deleted successfully', response.data)
        
        # Verify it's gone
        self.assertIsNone(self.repos['sanctoral'].get_feast(self.sanc_id))

if __name__ == '__main__':
    unittest.main()
