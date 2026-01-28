# Python API for learning   

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Data models
class User(BaseModel):
    id: Optional[int] = None
    name: str
    job: str
    description: Optional[str] = None

class Mission(BaseModel):
    id: Optional[int] = None
    title: str
    target: Optional[str] = None
    successfull: bool
    reward: float
    agent: str

# In-memory storage, later will be replaced by a database
users_db: List[User] = []
missions_db: List[Mission] = []
next_user_id = 1
next_mission_id = 1

# ===== USERS ENDPOINTS =====

@app.post("/users")
def create_user(user: User):
    """Create a new user"""
    global next_user_id
    user.id = next_user_id
    users_db.append(user)
    next_user_id += 1
    return user

@app.get("/users")
def list_users():
    """List all users"""
    return users_db

@app.get("/users/{user_id}, response_model=User")
def get_user(user_id: int):
    """Get a specific user by ID"""
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    """Update a specific user"""
    for i, existing_user in enumerate(users_db):
        if existing_user.id == user_id:
            user.id = user_id
            users_db[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete a specific user"""
    for i, user in enumerate(users_db):
        if user.id == user_id:
            deleted_user = users_db.pop(i)
            return {"message": "User deleted", "user": deleted_user}
    raise HTTPException(status_code=404, detail="User not found")

# ===== MISSIONS ENDPOINTS =====

@app.post("/missions")
def create_mission(mission: Mission):
    """Create a new mission"""
    global next_mission_id
    mission.id = next_mission_id
    missions_db.append(mission)
    next_mission_id += 1
    return mission

@app.get("/missions")
def list_missions():
    """List all missions"""
    return missions_db

@app.get("/missions/{mission_id}")
def get_mission(mission_id: int):
    """Get a specific mission by ID"""
    for mission in missions_db:
        if mission.id == mission_id:
            return mission
    raise HTTPException(status_code=404, detail="Mission not found")

@app.put("/missions/{mission_id}")
def update_mission(mission_id: int, mission: Mission):
    """Update a specific mission"""
    for i, existing_mission in enumerate(missions_db):
        if existing_mission.id == mission_id:
            mission.id = mission_id
            missions_db[i] = mission
            return mission
    raise HTTPException(status_code=404, detail="Mission not found")

@app.delete("/missions/{mission_id}")
def delete_mission(mission_id: int):
    """Delete a specific mission"""
    for i, mission in enumerate(missions_db):
        if mission.id == mission_id:
            deleted_mission = missions_db.pop(i)
            return {"message": "Mission deleted", "mission": deleted_mission}
    raise HTTPException(status_code=404, detail="Mission not found")



