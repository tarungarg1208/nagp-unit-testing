"""Class containing helper methods/classes for database queries"""

from database.database_core import EBrokerDatabase


class UserRepo:

    def __init__(self):
        self.db = EBrokerDatabase()

    def get_user_info(self, user_id):
        print("HERE HERE")
        query_string = f'SELECT * FROM user WHERE user_id = {user_id}'
        rows = self.db.execute_query(query_string=query_string)
        info = dict(user_id=rows[0][0], user_name=rows[0]
                    [1], user_balance=rows[0][2])
        return info

    def update_user_balance(self, user_id, updated_balance):
        query_string = f"UPDATE user SET user_balance = {updated_balance} where user_id = {user_id}"
        self.db.execute_query(
            query_string, commit_required=True, return_row=False)

class EquityRepo:

    def __init__(self):
        self.db = EBrokerDatabase()

    def get_equity_info(self, equity_id):
        query_string = f'SELECT * FROM equity WHERE equity_id = {equity_id}'
        rows = self.db.execute_query(query_string=query_string)
        if rows:
            info = dict(equity_id=rows[0][0], equity_name=rows[0]
                        [1], equity_price=rows[0][2])
        else:
            info = None
        return info

class HoldingRepo:

    def __init__(self):
        self.db = EBrokerDatabase()

    def get_all_user_holdings(self, user_id):
        query_string = f'SELECT * FROM holding WHERE user_id = {user_id}'
        rows = self.db.execute_query(query_string=query_string)
        print(rows)
        return rows

    def get_user_equity_balance(self,user_id,equity_id):
        query_string = f'SELECT * FROM holding WHERE user_id = {user_id} and equity_id={equity_id}'
        rows=self.db.execute_query(query_string=query_string)
        if len(rows)>0:
            return dict(balance=rows[0][2], entry_present=True)
        else:
            return dict(balance=0,entry_present=False)

    def update_user_holding(self, user_id, equity_id, updated_balance):
        dict_info=self.get_user_equity_balance(user_id=user_id,equity_id=equity_id)
        if dict_info['entry_present']==True:
            query_string = f"UPDATE holding SET quantity = {updated_balance} where user_id = {user_id} and equity_id = {equity_id}"
        else:
            query_string = f"INSERT INTO holding (user_id, equity_id, quantity) VALUES ({user_id}, {equity_id}, {updated_balance})"
        self.db.execute_query(query_string, commit_required=True, return_row=False)
