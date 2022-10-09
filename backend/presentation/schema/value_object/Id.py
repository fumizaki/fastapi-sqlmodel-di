# python external library
from pydantic import BaseModel, Field

class Id(BaseModel):
    id: str = Field(...)
