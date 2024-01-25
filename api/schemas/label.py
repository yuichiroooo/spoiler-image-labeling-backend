from pydantic import BaseModel, ConfigDict

class Label(BaseModel):
    video_id: str
    user: str
    spoiler_degree: int
    
    model_config = ConfigDict(
        from_attributes=True,
        strict=True
    )