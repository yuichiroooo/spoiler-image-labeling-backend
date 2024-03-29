from config.db import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud.image as image_crud
import schemas.image as image_schema


image = APIRouter(prefix="/image")


@image.get("/{progress}", response_model=list[image_schema.Image])
def get_unlabeled_images(progress: int, db: Session = Depends(get_db)):    
    return image_crud.get_images(db, progress)