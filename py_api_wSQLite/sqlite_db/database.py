# only for connection 

import os
import sqlite3
from contextlib import contextmanager

database = 'sqlite_database.db'

@contextmanager
def get_db():
    conn = None
    try:
        conn = sqlite3.connect(database)
        conn.row_factory = sqlite3.Row
        print("Database connection successful.")
        print("Database path: {}".format(os.path.abspath(database)))
        yield conn # this will return the connection object to the caller, and the code after yield will be executed after the caller is done with the connection
    except sqlite3.OperationalError as error:
        print(f"Error connecting to the database: {error}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")    
