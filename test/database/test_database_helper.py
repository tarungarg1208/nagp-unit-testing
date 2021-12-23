from database.database_helper import UserRepo, EquityRepo, HoldingRepo
from database.database_in_memory import EBrokerInMemoryDatabase
from unittest.mock import patch, MagicMock
from unittest import TestCase

class DatabaseHelperTest(TestCase):
    """class containing test cases for database_helper.py"""

    def setUp(self):
        """setup method for test class"""
        db=EBrokerInMemoryDatabase()
        db.setup_in_memory_db()
        self.user_repo = UserRepo()
        self.user_repo.db = db
        self.equity_repo = EquityRepo()
        self.equity_repo.db = db
        self.holding_repo = HoldingRepo()
        self.holding_repo.db = db

    def test_user_get_user_info(self):
        actual=self.user_repo.get_user_info(user_id=1)
        expected=dict(user_id=1, user_name="Trader_A", user_balance=10000)
        self.assertDictEqual(actual,expected)
    
    def test_update_user_balance(self):
        self.user_repo.update_user_balance(user_id=1, updated_balance=111)
        actual=self.user_repo.get_user_info(user_id=1)
        expected=dict(user_id=1, user_name="Trader_A", user_balance=111)
        self.assertDictEqual(actual,expected)

    def test_equity_get_equity_info(self):
        actual=self.equity_repo.get_equity_info(equity_id=1)
        expected = dict(equity_id=1, equity_name="ICICI", equity_price=300.0)
        self.assertDictEqual(actual, expected)
        
        actual=self.equity_repo.get_equity_info(equity_id=1111)
        expected = None
        self.assertEqual(actual, expected)

    def test_holding_get_all_user_holdings(self):
        actual=self.holding_repo.get_all_user_holdings(user_id=1)
        expected=[(1, 1, 10), (1, 2, 10)]
        self.assertListEqual(actual,expected)

    def test_holding_get_user_equity_balance(self):
        actual=self.holding_repo.get_user_equity_balance(user_id=1,equity_id=1)
        expected={'balance': 10, 'entry_present': True}
        self.assertDictEqual(actual,expected)

        actual=self.holding_repo.get_user_equity_balance(user_id=1,equity_id=111)
        expected={'balance': 0, 'entry_present': False}
        self.assertDictEqual(actual,expected)

    def test_holding_update_user_holding(self):
        self.holding_repo.update_user_holding(user_id=1,equity_id=1,updated_balance=111)
        self.holding_repo.db.print_all_data()
        actual=self.holding_repo.get_user_equity_balance(user_id=1,equity_id=1)
        expected={'balance': 111, 'entry_present': True}
        self.assertDictEqual(actual,expected)

    
