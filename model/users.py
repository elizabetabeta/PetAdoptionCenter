from . import Base
from sqlalchemy import *
import enum

class MyEnum(enum.Enum):
    admin = 'admin'
    user = 'user'

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    lastname = Column(String(25))
    email = Column(String(100))
    phone_number = Column(String(30))
    user_type = Column(Enum(MyEnum))


