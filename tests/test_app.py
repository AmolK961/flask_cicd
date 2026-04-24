import unittest
from app import  app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_home(self):
        rv=self.client.get('/')
        self.assertEqual(rv.status_code,200)
        self.assertEqual(rv.data,b'Hello, World!')

if __name__ == '__main__':
    unittest.main()