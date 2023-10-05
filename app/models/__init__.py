from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import your models here
from .user import User
from .role import Role
from .permissions import Permission