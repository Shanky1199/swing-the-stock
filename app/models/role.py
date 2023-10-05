from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)