import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
# )

# print(mydb)

import sqlite3
from database.database_helper import HoldingRepo, UserRepo
h=HoldingRepo()
print("HOLDINGS=",h.get_all_user_holdings(user_id=1))
u=UserRepo()
print("USER INFO=",u.get_user_info(user_id=1))