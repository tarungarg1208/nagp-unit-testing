from typing import final
from utility.utils import Utility
from database.database_helper import UserRepo,EquityRepo,HoldingRepo
class Trader:

    def __init__(self) -> None:
        self.user_repo= UserRepo()
        self.equity_repo = EquityRepo()
        self.holding_repo=HoldingRepo()
        
    def buy_equity(self, user_id, equity_id, quantity):
        print(f"Processing Buy Request for:{equity_id} for quantity:{quantity}")
        trading_allowed=Utility.is_trading_allowed()
        print("TRADING FLAG=",trading_allowed)
        if not trading_allowed:
            return dict(status="ERROR",message=f"Trading not allowed at this time(Time={Utility.get_current_time()}")
        else:
            try:
                response = dict(status="Failed",message="Error while buying equity")
                user_info=self.user_repo.get_user_info(user_id=user_id)
                equity_info=self.equity_repo.get_equity_info(equity_id=equity_id)
           
                # Checking User Balance
                user_balance=user_info['user_balance']
                equity_price=equity_info['equity_price']
                if user_balance>=equity_price*quantity:
                    
                    holding_info=self.holding_repo.get_user_equity_balance(user_id=user_id,equity_id=equity_id)
                    if holding_info['entry_present']==True:
                        updated_equity_balance=quantity+holding_info['balance']
                    else:
                        updated_equity_balance=quantity
                    updated_account_balance=user_balance-(quantity*equity_price)
                    print("updated",updated_account_balance,updated_equity_balance)
                    self.holding_repo.update_user_holding(user_id=user_id,equity_id=equity_id,updated_balance=updated_equity_balance)
                    self.user_repo.update_user_balance(user_id=user_id,updated_balance=updated_account_balance)
                    response['status']="Success"
                    response['message']="Equity Bought Successfully"
                    response['updated user info.']=self.user_repo.get_user_info(user_id=user_id)
                    response['updated holding info.']=self.holding_repo.get_all_user_holdings(user_id=user_id)
                else:
                    response['message']="Please add funds before buying this much quantity"
            except Exception as exp:
                raise TradeError("Error while Buying an equity", str(exp)) from exp
            finally:
                return response

    def sell_equity(self,user_id, equity_id, quantity):
        print(f"Processing Sell Request for:{equity_id} for quantity:{quantity}")
        trading_allowed=Utility.is_trading_allowed()
        print("TRADING FLAG=",trading_allowed)
        if not trading_allowed:
            return dict(status="ERROR",message=f"Trading not allowed at this time(Time={Utility.get_current_time()}")
        else:
            try:
                response = dict(status="Failed",message="Error while selling equity")
                user_info=self.user_repo.get_user_info(user_id=user_id)
                equity_info=self.equity_repo.get_equity_info(equity_id=equity_id)
                holding_info=self.holding_repo.get_user_equity_balance(user_id=user_id,equity_id=equity_id)
           
                if holding_info['entry_present']==True:
                    print("OVERALL HOLDING",holding_info)
                    if holding_info['balance']<quantity:
                        response['message']=f"Cannot Sell quantity:{quantity} of equity:{equity_id}. Available Balance:{holding_info['balance']}"
                    else:
                        user_balance=user_info['user_balance']
                        equity_price=equity_info['equity_price']
                        updated_equity_balance=holding_info['balance']-quantity
                        updated_account_balance=user_balance+quantity*equity_price
                        self.holding_repo.update_user_holding(user_id=user_id,equity_id=equity_id,updated_balance=updated_equity_balance)
                        self.user_repo.update_user_balance(user_id=user_id,updated_balance=updated_account_balance)
                        response['status']="Success"
                        response['message']="Equity Sold Successfully"
                        response['updated user info.']=self.user_repo.get_user_info(user_id=user_id)
                        response['updated holding info.']=self.holding_repo.get_all_user_holdings(user_id=user_id)
                else:
                    response['message']==f"Cannot Sell {quantity} of equity:{equity_id}. Available Balance:{holding_info['balance']}"
            except Exception as exp:
                raise TradeError("Error while Selling an equity", str(exp)) from exp
            finally:
                return response

    def add_funds(self, user_id, amount):
        print(f"Processing Add Fund Request for user:{user_id} for amount:{amount}")
        response=dict(status="Failed",message="Error while adding funds")
        try:
            print("HERE")
            user_info=self.user_repo.get_user_info(user_id=user_id)
            print(user_info)
            user_balance=user_info['user_balance']
            print("UBNA",type(user_balance))
            print(type(amount))
            updated_account_balance=user_balance+amount
            print(updated_account_balance)
            self.user_repo.update_user_balance(user_id=user_id,updated_balance=updated_account_balance)
            response['status']="Success"
            response['message']="Successfully added funds to user balance"
            response['updated user info.']=self.user_repo.get_user_info(user_id=user_id)
        except Exception as exp:
            raise TradeError("Error while Adding Funds", str(exp)) from exp
        finally:
            return response

    def get_user_info(self, user_id):
        print(f"Processing get_user_info request for user_id:{user_id}")
        response=dict(status="Failed",message="Cannot fetch user info.")
        try:
            user=self.user_repo.get_user_info(user_id=user_id)
            holding=self.holding_repo.get_all_user_holdings(user_id=user_id)
            response=dict(status="Success",user_info=user,holding_info=holding)
            return response
        except Exception as exp:
            raise TradeError("Error while getting user info",str(exp))
        finally:
            return response

class TradeError(Exception):
    """Class representing Errors in trading."""
