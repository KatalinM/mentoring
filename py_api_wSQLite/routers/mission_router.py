import crud.mission_crud as mission_crud
from data_models.mission import Mission

@app.post("/missions")
def create_mission(mission: Mission):
    mission_crud.add_mission(mission)
    return mission