# from fastapi import APIRouter, FastAPI
from http.client import HTTPException
import sqlite3
from fastapi import Depends
from sqlite_db.db_manager import get_db
import py_api_wSQLite.crud.user_crud as user_crud
from py_api_wSQLite.data_models.user import User
from fastapi import APIRouter
from fastapi import HTTPException


router = APIRouter()

# ---------------------- 
# CREATE 
# ---------------------- 
@router.post("/")
def add_new_user(user: User, conn: sqlite3.Connection = Depends(get_db)):
    try: 
        user_id =user_crud.add_user(conn, user)
        conn.commit() # commit the transaction to save the changes to the database
        return {"user_id": user_id}

    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="User already exists")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
      
  

# ---------------------- 
# READ 
# ---------------------- 
@router.get("/")
def get_all_users(conn: sqlite3.Connection = Depends(get_db)):
    return user_crud.get_all_users(conn)

# ---------------------- 
# UPDATE 
# ---------------------- 
# http:/localhost:8000/users/1
#@router.post("/{user_id}")
