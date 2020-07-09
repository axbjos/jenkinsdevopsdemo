#!/usr/bin/env python
import unittest
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello, World!')

    def test_about(self):
        rv = self.app.get('/about')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Joe Axberg made this')
    
    def test_nopage(self):
        rv = self.app.get('/nopage')
        self.assertEqual(rv.status, '404 NOT FOUND')

if __name__ == '__main__':
    unittest.main()
