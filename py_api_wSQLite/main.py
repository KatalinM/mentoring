from fastapi import FastAPI
from sqlite_db.database import init_db
from routers import mission_router
import uvicorn

# parameters only optional for better documentation, not required for the API to work
# app = FastAPI() is also fine 
app = FastAPI(title="Mission Management API", description="only for learning purposes", version="1.0.0")
app.include_router(mission_router.router, prefix="/missions")

def main():
    # Create the database if not exists and add a sample mission and agents to it
    init_db()

# This is the main entry point of the application, where we initialize the database and add a sample mission to it. The init_db function will create the necessary tables if they don't exist, and the add_mission function will insert the sample mission into the missions table. We can run this script to set up our database and add the initial data before starting the FastAPI server.
if __name__ == "__main__":
    main() 
    uvicorn.run("main:app", reload=True)

