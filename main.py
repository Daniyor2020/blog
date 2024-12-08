
from fastapi import FastAPI, HTTPException, status

import schemas
import models
from database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app =FastAPI()


origins = [
  "http://localhost",
  "http://localhost:3000",
  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Specify allowed methods
    allow_headers=["*"],  # Specify allowed headers
)


@app.get("/")
async def root():
    return {"message": "Hey there"}   

@app.get("/users", status_code=status.HTTP_200_OK, response_model=list[schemas.ShowUser])
async def get_users():
    db = SessionLocal()
    users = db.query(models.User).all()
    return users

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserBase):
    db = SessionLocal()
    db_user = db.query(models.User).filter(models.User.username== user.username).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User already exists")
    else:
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    
@app.get("/linksByUserId/{user_id}", status_code=status.HTTP_200_OK, response_model=schemas.UserLinksBase)
async def get_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    
    
@app.post("/links", status_code=status.HTTP_201_CREATED)
async def create_link(link: schemas.LinksBase):
    db = SessionLocal()
    new_link = models.Links(**link.dict())
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
    return new_link

@app.delete("/links/{link_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(link_id: int):
    db = SessionLocal()
    db_link = db.query(models.Links).filter(models.Links.id == link_id).first()
    if db_link:
        db.delete(db_link)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Link with id {link_id} not found")

