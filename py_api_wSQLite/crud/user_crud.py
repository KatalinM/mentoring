import sqlite3

from fastapi import HTTPException
from py_api_wSQLite.data_models.user import User
from sqlite_db.queries import add_user_query

def add_user(conn, user):
    cursor = conn.cursor()
    cursor.execute(add_user_query, ()) # TODO pass the user data to the query, for example (user.name, user.code_name, user.description, user.active)
    
    user_id = cursor.lastrowid
    print(f"User with ID {user_id} added successfully to the database.")
    return user_id
    # conn.commit is in the calling method