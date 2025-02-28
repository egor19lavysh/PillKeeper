from pydantic import BaseModel
from datetime import date


class PillCreateSchema(BaseModel):
    name: str
    expiration_date: date
    quantity: int = 0


class PillSchema(BaseModel):
    id: int
    name: str
    expiration_date: date
    quantity: int = 0

    class Config:
        from_attributes = True
