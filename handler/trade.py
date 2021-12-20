from utility.utils import Utility
class Trader:

    def __init__(self) -> None:
        self.balance=1000
        self.name="trader1"
        
    def buy_equity(self, equity, quantity):
        print(f"Processing Buy Request for:{equity} for quantity:{quantity}")
        print(f"Trading Allowed?:{Utility.is_trading_allowed()}")

    def sell_equity(self, equity, quantity):
        print(f"Processing Sell Request for:{equity} for quantity:{quantity}")
        print(f"Trading Allowed?:{Utility.is_trading_allowed()}")

    def add_funds(self, amount):
        print(f"Processing Add Fund Request for amount:{amount}")
        self.balance=self.balance+float(amount)
        return dict(status="success",updated_balance=self.balance)