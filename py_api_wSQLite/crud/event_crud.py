import sqlite3
from sqlite_db.queries import add_event_query
from py_api_wSQLite.data_models.event import Event

def add_event(conn, event):
   cursor = conn.cursor()
   cursor.execute(add_event_query, ()) # TODO 
    
   event_id = cursor.lastrowid
   print(f"User with ID {event_id} added successfully to the database.")
   return event_id

def get_events_of_user(conn, user_id):
    # TODO implementation
   pass
