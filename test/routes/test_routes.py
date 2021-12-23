from unittest.mock import patch, MagicMock
from unittest import TestCase
from utility.utils import get_time, get_dow, Utility
import datetime
from flask import Response
from app import APP

class RoutesTest(TestCase):
    """class containing test cases for routes.py"""

    def setUp(self):
        """setup method for test class"""
        self.client=APP.test_client()

    @patch('routes.routes.Trader.get_user_info')
    def test_user_get(self, mock_get_user):
        """test get_user_info api"""
        mock_get_user.return_value=dict(key="value")
        response=self.client.get('v1/trader/1')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['key'],'value')

        mock_get_user.return_value=dict(key="value")
        response=self.client.get('v1/trader/')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,404)

    @patch('routes.routes.Trader.add_funds')
    def test_fund_add_post(self, mock_add_funds):
        """test add_funds api"""
        mock_add_funds.return_value=dict(key="value")
        response=self.client.post('v1/trader/1/fund/100')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['key'],'value')

        response=self.client.get('v1/trader/1/fund/100')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,405)

    @patch('routes.routes.Trader.sell_equity')
    def test_sell_equity_post(self, mock_sell_equity):
        """test sell_equity api"""
        mock_sell_equity.return_value=dict(key="value")
        response=self.client.post('v1/trader/1/sell/1/quantity/10')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['key'],'value')

        response=self.client.get('v1/trader/1/sell/1/quantity/10')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,405)

    @patch('routes.routes.Trader.buy_equity')
    def test_buy_equity_post(self, mock_buy_equity):
        """test buy_equity api"""
        mock_buy_equity.return_value=dict(key="value")
        response=self.client.post('v1/trader/1/buy/1/quantity/10')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json['key'],'value')

        response=self.client.get('v1/trader/1/buy/1/quantity/10')
        self.assertIsInstance(response,Response)
        self.assertEqual(response.status_code,405)
