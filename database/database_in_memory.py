import sqlite3
import os
# from sqlite3.dbapi2 import connect

class EBrokerInMemoryDatabase:
    """Class containing Methods for creating and querying in memory database"""

    def __init__(self):
        """Constructor"""
        self.db_file=":memory:"
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

    def setup_in_memory_db(self):
        """creates tables within in memory database"""
        query_create_user_table = '''CREATE TABLE user
            (user_id INT PRIMARY KEY NOT NULL,
            user_name TEXT NOT NULL,
            user_balance REAL NOT NULL);'''

        query_create_equity_table = '''CREATE TABLE equity
            (equity_id INT PRIMARY KEY NOT NULL,
            equity_name TEXT NOT NULL,
            equity_price REAL NOT NULL);'''
            
        query_create_holding_table = '''CREATE TABLE holding
            (user_id INT NOT NULL,
            equity_id INT NOT NULL,
            quantity INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES user(user_id),
            FOREIGN KEY(equity_id) REFERENCES equity(equity_id),
            PRIMARY KEY (user_id,equity_id));'''

        print("Creating Tables")
        self.conn.execute(query_create_user_table)
        self.conn.execute(query_create_equity_table)
        self.conn.execute(query_create_holding_table)

        # Inserting records in Database
        self.conn.execute("""INSERT INTO user (user_id, user_name, user_balance) VALUES (1, "Trader_A", "10000")""")
        self.conn.execute("""INSERT INTO user (user_id, user_name, user_balance) VALUES (2, "Trader_B", "15000")""")

        self.conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (1, "ICICI", "300")""")
        self.conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (2, "HDFC", "400")""")
        self.conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (3, "SBI", "200")""")
        self.conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (4, "PNB", "100")""")

        self.conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (1, 1, 10)""")
        self.conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (1, 2, 10)""")
        self.conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (2, 3, 10)""")
        self.conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (2, 4, 10)""")
        
        self.conn.commit()
        # self.conn.close()
        print("Database/Tables created successfully...")

    def print_all_data(self):
        if not self.conn:
            return
        
        cursor=self.conn.cursor()

        cursor.execute("""SELECT * FROM user""")
        print(cursor.fetchall())

        cursor.execute("""SELECT * FROM equity""")
        print(cursor.fetchall())

        cursor.execute("""SELECT * FROM holding""")
        print(cursor.fetchall())

    def execute_query(self, query_string, commit_required=False, return_row=True):
        if not self.conn:
            self.connect()
        cursor=self.conn.cursor()
        cursor.execute(query_string)
        if commit_required:
            self.conn.commit()
        if return_row:
            return cursor.fetchall()

# ob=EBrokerDatabase()
# ob.connect()
# ob.print_all_data()


