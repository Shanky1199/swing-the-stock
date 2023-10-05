from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from models import Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)