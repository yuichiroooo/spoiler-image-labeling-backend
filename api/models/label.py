from sqlalchemy import Column, Text, Integer, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from config.db import Base, db_engine

class LabelTable(Base):
    __tablename__ = "labels"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    video_id = Column(Text, nullable=False)
    user = Column(Text, nullable=False)
    spoiler_degree = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=current_timestamp())

Base.metadata.create_all(bind=db_engine)