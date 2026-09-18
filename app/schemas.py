from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LinkCreate(BaseModel):
    long_url: str


class LinkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    short_code: str
    long_url: str
    created_at: datetime
    