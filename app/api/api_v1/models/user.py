
# File Explained: This file contains the User model which is used to create a new user in the database.
# In this example, the User object is defined with three fields:
# id, username, email, and is_active.
# The id field is optional, and is usually assigned by the database when a new user is created.
# The username and email fields are required, while the is_active field is optional and defaults to True.
#
# The UserBase model contains the username and email fields, which are common to both creating and updating a user.
# The UserCreate model extends UserBase to include the password field, which is required when creating a new user.
#
# Finally, the Config class is used to enable SQLAlchemy integration with Pydantic.
# The orm_mode flag tells Pydantic to allow ORM models to be passed as input and output,
# allowing the User model to be used in SQLAlchemy queries.

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base

from pydantic import BaseModel

class User(Base):
    __tablename__ = "T_user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")
class UserBase(BaseModel):
    __tablename__ = "T_user"
    username: str
    email: str

class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: str = None


class User(UserBase):
    id: int
    is_active: bool


    class Config:
        orm_mode = True
