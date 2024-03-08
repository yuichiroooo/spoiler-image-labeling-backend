from sqlalchemy import Column, String, Integer
from config.db import Base, db_engine

class ImageTable(Base):
    __tablename__ = "images"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    video_id = Column(String(255), nullable=False)
    channel = Column(String(255), nullable=False)

Base.metadata.create_all(bind=db_engine)