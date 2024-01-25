from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from sqlalchemy import select
from models.user import UserTable
import schemas.user as user_schema

def create_user(db: Session, user: user_schema.User) -> UserTable:
    new_user = UserTable(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(db: Session, name: str, password: str) -> UserTable:
    result: Result = db.execute(
        select(UserTable).filter(UserTable.name == name, UserTable.password == password)
    )
    return result.first()


def update_progress(db: Session, user: user_schema.User, original: UserTable) -> UserTable:
    original.progress = user.progress
    db.add(original)
    db.commit()
    db.refresh(original)
    return original