from unittest.mock import patch, MagicMock
from unittest import TestCase
from utility.utils import get_time, get_dow, Utility
import datetime
from flask import Response
from app import APP

class StatusTest(TestCase):
    """class containing test cases for status routes"""

    def setUp(self):
        """setup method for test class"""
        self.client=APP.test_client()

    def test_get_status(self):
        """test get_status() api"""
        response=self.client.get('/v1/status')
        self.assertIsInstance(response,Response)
        print(response.json)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['status'],'healthy')
        self.assertEqual(response.json['version'],'v1')
