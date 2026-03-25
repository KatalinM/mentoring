from posixpath import abspath
import sqlite3
from data_models.mission import Mission
from data_models.agent import Agent
import os

testmission = Mission(title="Test Mission", target="Test Target", target_id=3, status="Urgent", reward=100.0, agent="Test Code Name") 
testagent1 = Agent(name="Test Agent", code_name="Test Code Name", description="Test Description", active=True)
testagent2 = Agent(name="Test Agent 2", code_name="Test Code Name 2", description="Test Description 2", active=False)

agents = [testagent1, testagent2]

database = 'missions.db'
create_missions_table_query = """
    CREATE TABLE IF NOT EXISTS missions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        target VARCHAR(255),
        target_id INTEGER,
        status VARCHAR(255) NOT NULL,
        reward REAL NOT NULL,
        agent VARCHAR NOT NULL
    )
"""
create_agents_table_query = """
    CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        codename VARCHAR(255) NOT NULL,
        description VARCHAR,
        active BOOLEAN NOT NULL
    )
"""
create_tables = [create_missions_table_query, create_agents_table_query]
add_mission_query = """
                INSERT INTO missions (title, target, target_id, status, reward, agent)
                VALUES (?, ?, ?, ?, ?, ?)
            """
add_agent_query = """
                INSERT INTO agents (name, codename, description, active)
                VALUES (?, ?, ?, ?)
            """

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
            add_mission(conn, testmission)
            print("Sample mission added successfully to the database.")
            print("Adding sample agents to the database...")
            for agent in agents:
                add_agent(conn, agent)
            print("Sample agents added successfully to the database.")
            
    except sqlite3.OperationalError as error:
        print(f"Error connecting to missions database: {error}")

# connection is established in the init_db function, so we can pass the connection object to the add_mission function   
def add_mission(conn, mission):
    try:
        cursor = conn.cursor()
        cursor.execute(add_mission_query, (mission.title, mission.target, mission.target_id, mission.status, mission.reward, mission.agent))
        # apply the changes to the database
        conn.commit()
        print ("Missions database initialized successfully.")
        # return the id of the newly added mission
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error during add new mission to missions database: {error}")    

def add_agent(conn, agent):
    try:
        cursor = conn.cursor()
        cursor.execute(add_agent_query, (agent.name, agent.code_name, agent.description, agent.active))
        conn.commit()
        agent_id = cursor.lastrowid
        print(f"Agent with ID {agent_id} added successfully to the database.")
    except sqlite3.Error as error:
        print(f"Error adding agent to the database: {error}")       