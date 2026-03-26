# This file contains the SQL queries used to create the missions and agents tables, as well as the queries to add new missions and agents to the database.
create_missions_table_query = """
    CREATE TABLE IF NOT EXISTS missions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        target VARCHAR(255),
        target_id INTEGER,
        status VARCHAR(255) NOT NULL,
        reward REAL NOT NULL,
        agent VARCHAR,
        FOREIGN KEY (agent) REFERENCES agents(codename)
          ON DELETE SET NULL
          ON UPDATE CASCADE
    )
"""
create_agents_table_query = """
    CREATE TABLE IF NOT EXISTS agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        codename VARCHAR(255) NOT NULL UNIQUE,
        description VARCHAR,
        active BOOLEAN NOT NULL
    )
"""

add_mission_query = """
                INSERT INTO missions (title, target, target_id, status, reward, agent)
                VALUES (?, ?, ?, ?, ?, ?)
            """

add_agent_query = """
                INSERT INTO agents (name, codename, description, active)
                VALUES (?, ?, ?, ?)
            """