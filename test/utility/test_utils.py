from unittest.mock import patch, MagicMock
from unittest import TestCase
from utility.utils import get_time, get_dow, Utility
import datetime

class UtilsTest(TestCase):
    """class containing test cases for utils.py"""

    def setUp(self):
        """setup method for test class"""
        pass
    
    def test_get_dow(self):
        """test get_dow() method of utils.py"""
        expected=datetime.datetime.now().weekday()
        actual=get_dow()
        self.assertEqual(actual,expected)

    @patch('utility.utils.datetime.datetime')
    def test_get_time(self, mock_datetime):
        """test get_dow() method of utils.py"""
        expected=datetime.datetime.now().time()
        mock_datetime.time.return_value=expected
        actual=get_time()
        self.assertEqual(actual,expected)

    def test_get_current_time(self):
        """test get_current_time() method of utils.py"""
        actual=Utility.get_current_time()
        self.assertIsInstance(actual,dict)

    @patch('utility.utils.get_dow')
    @patch('utility.utils.get_time')
    def test_is_trading_allowed(self, mock_time, mock_dow):
        """test is_trading_allowed() method of utils.py"""
        # Testing Case when trading is allowed
        date_str = '01/12/21 11:12:13'
        time_object = datetime.time(10, 0, 0)
        mock_time.return_value=time_object
        mock_dow.return_value=3
        actual=Utility.is_trading_allowed()
        self.assertTrue(actual)

        # Testing Case when trading is not allowed
        mock_dow.return_value=5
        actual=Utility.is_trading_allowed()
        self.assertFalse(actual)
    

    