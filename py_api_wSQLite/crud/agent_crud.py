import sqlite3
from data_models.agent import Agent
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

def get_all_agents(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM agents")
        agents = cursor.fetchall()
        for row in agents:
            print (row, len(row))
        return [Agent(id=row[0], name=row[1], code_name=row[2], description=row[3], active=row[4]) for row in agents]
    except sqlite3.Error as error:
        print(f"Error retrieving agents from the database: {error}")   