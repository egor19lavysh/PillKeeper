from dataclasses import dataclass
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete, text, insert
from sqlalchemy.orm import Session
from models import Pill
from schemas import PillCreateSchema


@dataclass
class PillRepository:
    db_session: Session

    def ping_db(self) -> dict:
        with self.db_session as session:
            try:
                session.execute(text("SELECT 1"))
            except IntegrityError:
                raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database is not available")
            return {"text": "db is working"}

    def get_pills(self) -> list[Pill]:
        with self.db_session as session:
            pills: list[Pill] = session.execute(select(Pill)).scalars().all()
        return pills

    def get_pill(self, pill_id: int) -> Pill | None:
        query = select(Pill).where(Pill.id == pill_id)
        with self.db_session as session:
            pill: Pill = session.execute(query).scalar_one_or_none()
        return pill

    def create_pill(self, pill: PillCreateSchema) -> int:
        query = (insert(Pill)
                    .values(
            name=pill.name,
            expiration_date=pill.expiration_date,
            quantity=pill.quantity
        ).returning(Pill.id)
                    )
        with self.db_session as session:
            pill_id: int = session.execute(query).scalar_one_or_none()
            session.commit()
            return pill_id

    def get_quantity_pill(self, pill_id: int) -> int:
        with self.db_session as session:
            quantity: int = session.execute(select(Pill).where(Pill.id == pill_id)).scalar_one_or_none().quantity
        return quantity

    def update_quantity_pill(self, pill_id: int, quantity: int = -1) -> Pill:
        query = update(Pill).where(Pill.id == pill_id).values(
            quantity=self.get_quantity_pill(pill_id) + quantity).returning(Pill.id)
        with self.db_session as session:
            session.execute(query)
            session.commit()
        return self.get_pill(pill_id)

    def delete_pill(self, pill_id: int) -> None:
        query = delete(Pill).where(Pill.id == pill_id)
        with self.db_session as session:
            session.execute(query)
            session.commit()
