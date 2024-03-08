from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    name: str
    progress: int
    
    model_config = ConfigDict(
        from_attributes=True,
        strict=True
    )