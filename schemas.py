from pydantic import BaseModel
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
class UserBase(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True
        
class LinksBase(BaseModel):
    title: str
    url: str
    thumbnail: str
    user_id: int
    
class UserLinksBase(BaseModel):
    links: list[LinksBase]
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]