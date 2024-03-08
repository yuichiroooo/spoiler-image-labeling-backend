from sqlalchemy import Column, String, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from config.db import Base, db_engine

class LabelTable(Base):
    __tablename__ = "labels"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    video_id = Column(String(255), nullable=False)
    channel = Column(String(255), nullable=False)
    user = Column(String(255), nullable=False)
    spoiler_degree = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=current_timestamp())

Base.metadata.create_all(bind=db_engine)