from database import base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
class users(base):
    __tablename__ = "users"

    user_id = Column(Integer,primary_key=True,index = True)
    username =Column(String,unique = True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    roles = Column(String)




class jobs(base):
    __tablename__ = "jobs"

    job_id = Column(Integer,primary_key = True,index = True)
    tittle = Column(String)
    completed = Column(Boolean, default=False)
    priority = Column(Integer)
    owner_id = Column(Integer,ForeignKey("users.user_id"))

