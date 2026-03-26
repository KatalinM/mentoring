from fastapi import APIRouter, FastAPI
import sqlite3
from fastapi import Depends
from sqlite_db.database import get_db
import crud.mission_crud as mission_crud
from data_models.mission import Mission
from fastapi import APIRouter

router = APIRouter()

# ---------------------- 
# CREATE 
# ---------------------- 
@router.post("/")
def create_mission(mission: Mission, conn: sqlite3.Connection = Depends(get_db)):
    mission_crud.add_mission(conn, mission)
    return mission


# ---------------------- 
# READ 
# ---------------------- 
# note that the get_missions function is decorated with @router.get("/") to handle GET requests to the /missions endpoint! 
# No need to add here /missions, because we already added the prefix /missions in the main.py when we included the router!
@router.get("/")
def get_missions(conn: sqlite3.Connection = Depends(get_db)):
    return mission_crud.get_all_missions(conn)