from pydantic import BaseModel
from typing import Optional

class Agent(BaseModel):
    id: Optional[int] = None
    name: str
    code_name: str
    description: Optional[str] = None
    active: bool = True

    


    