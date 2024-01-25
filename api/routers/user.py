from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.user as user_crud
import schemas.user as user_schema
from config.db import get_db

user = APIRouter(prefix="/users")

@user.post("", response_model=user_schema.User)
def create_user(user_body: user_schema.User, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user_body)


@user.get("/me", response_model=user_schema.User)
def get_me(name: str, password: str, db: Session = Depends(get_db)):
    return user_crud.get_user(db, name, password)


@user.put("/update/{id}", response_model=user_schema.User)
def update_progress(user_body: user_schema.User, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_body.name, user_body.password)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_crud.update_progress(db, user_body, original=user)