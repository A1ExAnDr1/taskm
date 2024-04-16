from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.schems.base_schema import Base

class User(Base):
   __tablename__ = 'users'

   id = Column(UUID(as_uuid=True), primary_key=True, index=True)
   name = Column(String)
