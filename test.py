from app import app
from data_load import create_database
import sqlite3
import os
import unittest

class DataLoadTest(unittest.TestCase):
    # setup a temporary database
    def setUp(self):
        create_database('test.db')
        
    # delete the database
    def tearDown(self):
        os.remove('test.db')
    
    # ensure ships data is loaded correctly   
    def test_ships_load(self):
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM vessel")
        result = cur.fetchone()[0]
        self.assertEqual(result, 3)
    
    # ensure location data is loaded correctly   
    def test_positions_load(self):
        conn = sqlite3.connect("test.db")
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM position")
        result = cur.fetchone()[0]
        self.assertEqual(result, 2000)
        
class FlaskAppTest(unittest.TestCase):
	# ensure ships directory works as expected
    def test_ships_status(self):
        tester = app.test_client(self)
        response = tester.get('/api/ships', content_type='html/text')
        self.assertEqual(response.status_code, 200)

	# ensure positions directory works as expected
    def test_positions_status(self):
        tester = app.test_client(self)
        response = tester.get('/api/positions/9247455', content_type='html/text')
        self.assertEqual(response.status_code, 200) 

if __name__ == '__main__':
    unittest.main()