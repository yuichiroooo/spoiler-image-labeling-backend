from pydantic import BaseModel, ConfigDict

class Image(BaseModel):
    video_id: str
    channel: str
    
    model_config = ConfigDict(
        from_attributes=True,
        strict=True
    )