from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
#from data_models.agent import Agent
from data_models.mission import Mission
#from sqlite_db.database import create_table_query, insert_mission_query, insert_agent_query
from sqlite_db.database import add_agent, add_mission, init_db

# parameters only optional for better documentation, not required for the API to work
# app = FastAPI() is also fine 
app = FastAPI(title="Mission Management API", description="only for learning purposes", version="1.0.0") 

def main():
    # Create the database if not exists and add a sample mission and agents to it
    init_db()

# This is the main entry point of the application, where we initialize the database and add a sample mission to it. The init_db function will create the necessary tables if they don't exist, and the add_mission function will insert the sample mission into the missions table. We can run this script to set up our database and add the initial data before starting the FastAPI server.
if __name__ == "__main__":
    main()    

