from unittest.mock import patch, MagicMock
from unittest import TestCase
from handler.trade import Trader
import datetime


class mock_user:
    def get_user_info(self, user_id):
        if user_id == 999:
            return dict(user_id=user_id, user_name="NAME", user_balance=100)
        else:
            return dict(user_id=user_id, user_name="NAME", user_balance=10000)

    def update_user_balance(self, user_id, updated_balance):
        print("UPDATING USER BALANCE")


class mock_holding:
    def get_all_user_holdings(self, user_id):
        if user_id == 999:
            return [(999, 1, 1), (999, 2, 2)]
        else:
            return [(1, 1, 10), (1, 2, 10)]

    def get_user_equity_balance(self, user_id, equity_id):
        if user_id == 999:
            return dict(balance=0, entry_present=False)
        else:
            return dict(balance=100, entry_present=True)

    def update_user_holding(self, user_id, equity_id, updated_balance):
        print("UDPATING HOLDINGS")


class mock_equity:
    def get_equity_info(self, equity_id):
        return dict(equity_id=equity_id, equity_price=100)


class TraderTest(TestCase):
    """class containing test cases for trade.py"""

    def setUp(self):
        """setup method for test class"""
        self.trader = Trader()
        self.trader.user_repo = mock_user()
        self.trader.equity_repo = mock_equity()
        self.trader.holding_repo = mock_holding()

    def test_get_user_info(self):
        """tests get_user_info() method"""
        response = self.trader.get_user_info(user_id=999)
        print(response)
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response['user_info'], dict)
        self.assertEqual(response['user_info']['user_id'], 999)
        self.assertEqual(response['user_info']['user_balance'], 100)
        self.assertIsInstance(response['holding_info'], list)
        self.assertListEqual(response['holding_info'], [
                             (999, 1, 1), (999, 2, 2)])
        self.assertEqual(response['status'], "Success")

    def test_add_funds(self):
        """tests add_funds() method"""
        response = self.trader.add_funds(user_id=999, amount=1000)
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response['updated user info.'], dict)
        self.assertEqual(response['updated user info.']['user_id'], 999)
        self.assertEqual(response['message'],
                         "Successfully added funds to user balance")
        self.assertEqual(response['status'], "Success")

    @patch("handler.trade.Utility.is_trading_allowed")
    def test_sell_equity(self, mock_trading_allowed):
        """tests sell_equity() method"""
        # Testing all possible scenarios while selling equity
        mock_trading_allowed.return_value = True
        response = self.trader.sell_equity(
            user_id=999, equity_id=1, quantity=10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'], "Error while selling equity")
        self.assertEqual(response['status'], "Failed")

        mock_trading_allowed.return_value = True
        response = self.trader.sell_equity(
            user_id=1, equity_id=1, quantity=1000)
        self.assertIsInstance(response, dict)
        self.assertEqual(
            response['message'], "Cannot Sell quantity:1000 of equity:1. Available Balance:100")
        self.assertEqual(response['status'], "Failed")

        mock_trading_allowed.return_value = False
        response = self.trader.sell_equity(
            user_id=999, equity_id=1, quantity=10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'][:32],
                         "Trading not allowed at this time")
        self.assertEqual(response['status'], "ERROR")

        mock_trading_allowed.return_value = True
        response = self.trader.sell_equity(
            user_id=1, equity_id=1, quantity=10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'], "Equity Sold Successfully")
        self.assertEqual(response['status'], "Success")

    @patch("handler.trade.Utility.is_trading_allowed")
    def test_buy_equity(self, mock_trading_allowed):
        """tests sell_equity() method"""
        # Testing all possible scenarios while buying equity
        mock_trading_allowed.return_value = True
        response = self.trader.buy_equity(
            user_id=999, equity_id=1, quantity=10)
        self.assertIsInstance(response, dict)
        self.assertEqual(
            response['message'], "Please add funds before buying this much quantity")
        self.assertEqual(response['status'], "Failed")

        mock_trading_allowed.return_value = True
        response = self.trader.buy_equity(
            user_id=999, equity_id=1, quantity=1)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'], "Equity Bought Successfully")
        self.assertEqual(response['status'], "Success")

        mock_trading_allowed.return_value = True
        response = self.trader.buy_equity(
            user_id=1, equity_id=1, quantity=1)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'], "Equity Bought Successfully")
        self.assertEqual(response['status'], "Success")

        mock_trading_allowed.return_value = False
        response = self.trader.buy_equity(
            user_id=999, equity_id=1, quantity=10)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['message'][:32],
                         "Trading not allowed at this time")
        self.assertEqual(response['status'], "ERROR")
