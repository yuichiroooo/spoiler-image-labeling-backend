from sqlalchemy import Column, Text, Integer
from config.db import Base, db_engine

class ImageTable(Base):
    __tablename__ = "images"
    
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    video_id = Column(Text, nullable=False)
    channel = Column(Text)

Base.metadata.create_all(bind=db_engine)