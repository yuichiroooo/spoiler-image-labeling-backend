from config.db import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud.user as user_crud
import schemas.user as user_schema


user = APIRouter(prefix="/users")


@user.get("/all", response_model=list[user_schema.User])
def get_all_users(db: Session = Depends(get_db)):
    return user_crud.get_all_users(db)


@user.get("/me", response_model=user_schema.User)
def get_me(name: str, db: Session = Depends(get_db)):
    return user_crud.get_me(db, name)


@user.put("/update", response_model=user_schema.User)
def update_progress(name: str, db: Session = Depends(get_db)):
    user = user_crud.get_me(db, name)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_crud.update_progress(db, user)