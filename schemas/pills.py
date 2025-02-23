from pydantic import BaseModel
from datetime import date


class PillCreateSchema(BaseModel):
    name: str
    symptoms: list[int]
    expiration_date: date
    side_effects: list[int]
    quantity: int = 0


class PillSchema(PillCreateSchema):
    id: int
