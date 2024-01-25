from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    password: str
    progress: int
    
    model_config = ConfigDict(
        from_attributes=True,
        strict=True
    )