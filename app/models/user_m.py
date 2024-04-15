import enum
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
