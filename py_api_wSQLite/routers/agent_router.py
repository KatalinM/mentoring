# from fastapi import APIRouter, FastAPI
import sqlite3
from fastapi import Depends
from sqlite_db.database import get_db
import crud.agent_crud as agent_crud
from data_models.agent import Agent
from fastapi import APIRouter


router = APIRouter()

# ---------------------- 
# CREATE 
# ---------------------- 
@router.post("/")
def add_new_agent(agent: Agent, conn: sqlite3.Connection = Depends(get_db)):
    agent_crud.add_agent(conn, agent)
    return agent

# ---------------------- 
# READ 
# ---------------------- 
# note that the get_agents function is decorated with @router.get("/") to handle GET requests to the /agents endpoint! 
# No need to add here /agents, because we already added the prefix /agents in the main.py when we included the router!
@router.get("/")
def get_all_agents(conn: sqlite3.Connection = Depends(get_db)):
    return agent_crud.get_all_agents(conn)