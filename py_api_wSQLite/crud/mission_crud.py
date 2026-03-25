import sqlite3
from sqlite_db.queries import add_mission_query

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
    