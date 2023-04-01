import unittest
import requests
import logging

class TestVote(unittest.TestCase):
    def addvote(self):
        expected = 200
        response = requests.get('http://localhost:8080')
        actual = response.status_code
        self.assertEqual(actual, expected)
