# db logic for connection management, and other common db related functions

import os
from sqlite_db import queries
from database import get_db
import sqlite3

from constants import TESTUSERS, TESTEVENT
from crud.event_crud import add_event
from crud.user_crud import add_user

def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        print("Initializing the database...\n")
        # Create tables
        cursor.execute(queries.create_users_table_query)
        cursor.execute(queries.create_events_table_query)
        conn.commit()
        print("Database initialized successfully.\n")

        seed_data_if_empty(conn)


def seed_data_if_empty(conn):
    cursor = conn.cursor()
    # Check if the users table is empty
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    # Check if the events table is empty
    cursor.execute("SELECT COUNT(*) FROM events")
    event_count = cursor.fetchone()[0]
    if user_count == 0:
        print("Seeding users data...")
        for user in TESTUSERS:
            add_user(conn, user)
        print("Users data seeded successfully.\n")
    else:
        print("Users table already has data. Skipping seeding.\n")
    if event_count == 0:
        print("Seeding events data...")
        for event in TESTEVENT:
            add_event(conn, event)
        print("Events data seeded successfully.\n")
    else:
        print("Events table already has data. Skipping seeding.\n")
    conn.commit() # commit the changes after seeding the data    
