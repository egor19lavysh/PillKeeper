from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, ForeignKey, Column
from .base import Base
from datetime import date

pill_symptom_association = Table(
    'pill_symptom_association', Base.metadata,
    Column('pill_id', ForeignKey('pills.id'), primary_key=True),
    Column('symptom_id', ForeignKey('symptoms.id'), primary_key=True)
)

pill_side_effect_association = Table(
    'pill_side_effect_association', Base.metadata,
    Column('pill_id', ForeignKey('pills.id'), primary_key=True),
    Column('side_effect_id', ForeignKey('side_effects.id'), primary_key=True)
)


class Symptom(Base):
    __tablename__ = "symptoms"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]

    pills: Mapped[list["Pill"]] = relationship(
        "Pill", secondary=pill_symptom_association, back_populates="symptoms"
    )


class SideEffect(Base):
    __tablename__ = "side_effects"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]

    pills: Mapped[list["Pill"]] = relationship(
        "Pill", secondary=pill_side_effect_association, back_populates="side_effects"
    )


class Pill(Base):
    __tablename__ = "pills"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str]
    expiration_date: Mapped[date]
    quantity: Mapped[int]

    symptoms: Mapped[list["Symptom"]] = relationship(
        "Symptom", secondary=pill_symptom_association
    )

    side_effects: Mapped[list["SideEffect"]] = relationship(
        "SideEffect", secondary=pill_side_effect_association
    )
