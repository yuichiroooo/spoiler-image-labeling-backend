from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud.label as label_crud
import schemas.label as label_schema
from config.db import get_db

label = APIRouter(prefix="/labels")

@label.post("", response_model=label_schema.Label)
def post_label(label_body: label_schema.Label, db: Session = Depends(get_db)):
    return label_crud.post_label(db, label_body)