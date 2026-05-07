from fastapi import FastAPI
from sqlite_db.db_manager import init_db
from py_api_wSQLite.routers.event_router import router as event_router
from py_api_wSQLite.routers.user_router import router as user_router
import uvicorn

# parameters only optional for better documentation, not required for the API to work
# app = FastAPI() is also fine 
app = FastAPI(title="Event Planner API", description="only for learning purposes", version="1.0.0")
app.include_router(event_router, prefix="/events") 
app.include_router(user_router, prefix="/users") 
# http://localhost:8000/users/1 -> get user with id 1

def main():
    # Create the database if not exists and initialize the tables
    init_db()

# This is the main entry point of the application, where we initialize the database and add a sample mission to it. The init_db function will create the necessary tables if they don't exist, and the add_mission function will insert the sample mission into the missions table. We can run this script to set up our database and add the initial data before starting the FastAPI server.
if __name__ == "__main__":
    main() 
    uvicorn.run("main:app", reload=True)


