from models.image import ImageTable
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from sqlalchemy import select

def get_images(db: Session, progress: int) -> list[ImageTable]:
    limit: int = 5
    result: Result = db.execute(
        select(ImageTable).filter(progress + 1 <= ImageTable.id, ImageTable.id <= progress + limit)
    )
    
    return result.scalars().all()