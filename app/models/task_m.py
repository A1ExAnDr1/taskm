import enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.user_m import User






class Task (BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id:UUID
    name:str
    task_user:User | None = None

