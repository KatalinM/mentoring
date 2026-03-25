import sqlite3
from sqlite_db.queries import add_agent_query

def add_agent(conn, agent):
    try:
        cursor = conn.cursor()
        cursor.execute(add_agent_query, (agent.name, agent.code_name, agent.description, agent.active))
        conn.commit()
        agent_id = cursor.lastrowid
        print(f"Agent with ID {agent_id} added successfully to the database.")
    except sqlite3.Error as error:
        print(f"Error adding agent to the database: {error}")       