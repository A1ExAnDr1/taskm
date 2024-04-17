from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.schems.base_schema import Base

class Task(Base):
   __tablename__ = 'task'

   id = Column(UUID(as_uuid=True), primary_key=True, index=True)
   name = Column(String)
   task_user =Column(UUID(as_uuid=True))
