from sqlalchemy.orm import Session
from models.label import LabelTable
import schemas.label as label_schema

def post_label(db: Session, label: label_schema.Label) -> LabelTable:
    new_label = LabelTable(**label.model_dump())
    db.add(new_label)
    db.commit()
    db.refresh(new_label)
    return new_label