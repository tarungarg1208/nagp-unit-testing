"""File containing methods and code for init. database setup
   Executed only if we want to setup a fresh database"""

import sqlite3
import os
import sys

if __name__ == "__main__": # pragma: no cover
    path = os.path.realpath(__file__)
    path = os.path.join(path, os.pardir, os.pardir, "ebroker.db")
    path = os.path.abspath(path)
    db_file = path

    if os.path.exists(db_file):
        print(f"Database already exists at path:{db_file}\nPlease Delete the existing file if a new db has to be created\n...EXITING...")
        sys.exit(0)

    conn = sqlite3.connect(db_file)

    # Creating Tables
    # 1.USER Table   : user_id, user_name, user_balance
    # 2.equity Table : equity_id, equity_name, equity_price
    # 3.holding Table  : trade_id, user_id, equity_id, timestamp

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
    conn.execute(query_create_user_table)
    conn.execute(query_create_equity_table)
    conn.execute(query_create_holding_table)

    # Inserting records in Database
    conn.execute("""INSERT INTO user (user_id, user_name, user_balance) VALUES (1, "Trader_A", "10000")""")
    conn.execute("""INSERT INTO user (user_id, user_name, user_balance) VALUES (2, "Trader_B", "15000")""")

    conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (1, "ICICI", "300")""")
    conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (2, "HDFC", "400")""")
    conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (3, "SBI", "200")""")
    conn.execute("""INSERT INTO equity (equity_id, equity_name, equity_price) VALUES (4, "PNB", "100")""")

    conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (1, 1, 10)""")
    conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (1, 2, 10)""")
    conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (2, 3, 10)""")
    conn.execute("""INSERT INTO holding (user_id, equity_id, quantity) VALUES (2, 4, 10)""")
    
    conn.commit()
    conn.close()
    print("Database/Tables created successfully...")
    # os.remove(db_file)
