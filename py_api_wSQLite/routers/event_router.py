from fastapi import APIRouter, FastAPI
import sqlite3
from fastapi import Depends
from sqlite_db.db_manager import get_db
import py_api_wSQLite.crud.event_crud as event_crud
from py_api_wSQLite.data_models.event import Event
from fastapi import APIRouter

router = APIRouter()

# ---------------------- 
# CREATE 
# ---------------------- 
@router.post("/")
def create_event(event: Event, conn: sqlite3.Connection = Depends(get_db)):
    event_crud.add_event(conn, event)
    return event

# ---------------------- 
# READ 
# ---------------------- 
@router.get("/")
def get_events(conn: sqlite3.Connection = Depends(get_db)):
    return event_crud.get_all_events(conn)

@router.get("/{user_id}")
def get_events_of_user(conn: sqlite3.Connection = Depends(get_db), user_id: int = None):
    return event_crud.get_events_of_user(conn, user_id)