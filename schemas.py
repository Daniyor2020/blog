from pydantic import BaseModel
from database import SessionLocal
from typing import List, Annotated
from sqlalchemy.orm import Session
from fastapi import Depends


class ShowUser(BaseModel):
    username: str
    password: str
    id: int
    
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True  # Enables Pydantic to interact with ORM objects.

class LinksBase(BaseModel):
    title: str
    url: str
    thumbnail: str
    user_id: int

    class Config:
        orm_mode = True  # Enables Pydantic to interact with ORM objects.

class UserLinksBase(BaseModel):
    links: List[LinksBase]

    class Config:
        orm_mode = True  # Ensures the model can serialize ORM objects.


  
class AllUsers(BaseModel):
    users: List[ShowUser]
    
    class Config:
        orm_mode = True   

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Annotated type to provide a database dependency
db_dependency = Annotated[Session, Depends(get_db)]
