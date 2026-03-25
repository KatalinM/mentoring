from data_models.agent import Agent
from data_models.mission import Mission

TESTMISSION = Mission(title="Test Mission", target="Test Target", target_id=3, status="Urgent", reward=100.0, agent="Test Code Name") 
TESTAGENT_1 = Agent(name="Test Agent", code_name="Test Code Name", description="Test Description", active=True)
TESTAGENT_2 = Agent(name="Test Agent 2", code_name="Test Code Name 2", description="Test Description 2", active=False)

TESTAGENTS = [TESTAGENT_1, TESTAGENT_2]