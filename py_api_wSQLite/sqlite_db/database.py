import os
import sqlite3
from sqlite_db.queries import create_missions_table_query, create_agents_table_query
from sqlite_db.constants import TESTMISSION, TESTAGENTS 
from crud.agent_crud import add_agent
from crud.mission_crud import add_mission

database = 'missions.db'

create_tables = [create_missions_table_query, create_agents_table_query]


def init_db():
    try:
        with sqlite3.connect(database) as conn:
            print("Database connection successful.")
            print("Database path: {}".format(os.path.abspath(database)))
            cursor = conn.cursor()
            # create the missions and agents tables if they don't exist
            for query in create_tables:
                cursor.execute(query)
             # apply the changes to the database
            conn.commit()
            print ("Missions database initialized successfully.")
            print("Adding sample mission to the database...")
            add_mission(conn, TESTMISSION)
            print("~~Sample mission(s) added successfully to the database.~~")
            print("Adding sample agents to the database...")
            for agent in TESTAGENTS:
                add_agent(conn, agent)
            print("~~Sample agent(s) added successfully to the database.~~")
            
    except sqlite3.OperationalError as error:
        print(f"Error connecting to missions database: {error}")

# connection is established in the init_db function, so we can pass the connection object to the add_mission function   


