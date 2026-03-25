from pydantic import BaseModel
from typing import Optional

class Mission(BaseModel):
    id: Optional[int] = None
    title: str
    target: Optional[str] = None
    target_id: Optional[int] = None
    status: str
    reward: float
    agent: str