from sqlalchemy import Column, Text, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from config.db import Base, db_engine

class UserTable(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, nullable=False)
    progress = Column(Integer, nullable=False)
    updated_at = Column(TIMESTAMP, server_default=current_timestamp())

Base.metadata.create_all(bind=db_engine)