from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import date


class Pill(Base):
    __tablename__ = "pills"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    expiration_date: Mapped[date]
    quantity: Mapped[int]
