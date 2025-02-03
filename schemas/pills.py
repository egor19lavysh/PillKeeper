from pydantic import BaseModel
from datetime import date


class PillCreateSchema(BaseModel):
    name: str
    description: str
    symptoms: list[int]
    expiration_date: date
    side_effects: list[int]
    amount: int = 0


class PillSchema(PillCreateSchema):
    id: int
