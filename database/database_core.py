import sqlite3
import os
# from sqlite3.dbapi2 import connect

class EBrokerDatabase:
    """Class containing Methods for database connection and query"""

    def __init__(self):
        """Constructor"""
        path=os.path.realpath(__file__)
        path=os.path.join(path,os.pardir,os.pardir,"ebroker.db")
        path=os.path.abspath(path)
        self.db_file=path

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)

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


