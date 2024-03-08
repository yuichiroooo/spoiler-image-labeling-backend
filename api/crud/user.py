from models.user import UserTable
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from sqlalchemy import select


def get_all_users(db: Session) -> list[UserTable]:
    result: Result = db.execute(
        select(UserTable)
    )
    
    return result.scalars().all()


def get_me(db: Session, name: str) -> UserTable:
    result: Result = db.execute(
        select(UserTable).filter(UserTable.name == name)
    )
    
    return result.scalars().first()


def update_progress(db: Session, original: UserTable) -> UserTable:
    original.progress += 5
    db.add(original)
    db.commit()
    db.refresh(original)
    
    return original