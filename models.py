from sqlalchemy import Column, Integer, String, ForeignKey
from  database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    password = Column(String(255))
    
    links = relationship("Links", back_populates="user")
    
class Links(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    url = Column(String(255))
    thumbnail = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="links")