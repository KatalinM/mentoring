import sqlite3
from sqlite_db.queries import add_mission_query, get_missions_with_agents_query
from data_models.mission import Mission

def add_mission(conn, mission):
    try:
        cursor = conn.cursor()
        cursor.execute(add_mission_query, (mission.title, mission.target, mission.target_id, mission.status, mission.reward, mission.agent))
        # apply the changes to the database
        conn.commit()
        print ("Mission with id {} added successfully to the database.".format(cursor.lastrowid))
        # return the id of the newly added mission
        return cursor.lastrowid

    except sqlite3.Error as error:
        print(f"Error during add new mission to missions database: {error}")
    
def get_all_missions(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM missions")
        missions = cursor.fetchall()
        for row in missions:
            print (row, len(row))
        return [Mission(id=row[0], title=row[1], target=row[2], target_id=row[3], status=row[4], reward=row[5], agent=row[6]) for row in missions]
    except sqlite3.Error as error:
        print(f"Error retrieving missions from the database: {error}") 

def get_missions_with_agents(conn, code_name):
    try:
        cursor = conn.cursor()
        cursor.execute(get_missions_with_agents_query, (code_name,)) # here we can pass the codename of the agent we want to filter by, for example "007" for James Bond
        missions_of_agent = cursor.fetchall()
        for row in missions_of_agent:
            print(row)
        return [{"agent's name": row[0],
                 "agent's codename": row[1],
                 "target of the mission": row[2],
                 "mission reward": row[3]}
                 for row in missions_of_agent]
    except sqlite3.Error as error:
        print(f"Error retrieving missions with agents from the database: {error}")          